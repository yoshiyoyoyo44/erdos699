"""Independent standard-library replay of the gap-layer certificate.

The arithmetic and residue covering are re-proved here. Completeness of the four
elliptic integral-point lists still depends on Magma's proved full groups and
IntegralPoints; the point coordinates and every inverse filter are checked here.
"""
from collections import Counter
from fractions import Fraction
from math import gcd,isqrt
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET


def valuation(n,p=2):
    assert n
    n=abs(n);e=0
    while n%p==0:n//=p;e+=1
    return e


def independent_cases():
    branches=[(1,1,1,1,112),(1,1,3,9,112),(1,3,1,27,80),(3,1,1,3,112)]
    result=[]
    for gap in range(4,10):
        for gamma,d1,d2,num,den in branches:
            T=1
            B=gamma*d1*d1*d2*(1<<(gap-3))
            while den*T**3<num*(1<<gap):
                if gcd(T,gamma*d1*d2)==1 and not (gamma==1 and valuation(T,3)==1):
                    for q in range(1,B+1):
                        m=B-T*q
                        if 0<m<B and m%2 and gcd(m,T)==1 and (q-d2)%8==0:
                            result.append((gap,gamma,d1,d2,T,m,q,m*gamma*(1<<(gap-1))))
                T+=2
    return sorted(result)


KEYS=('gap','gamma','d1','d2','T','m','q','alpha')


def branch_ok(row,v):
    gap,gamma,d1,d2,T,m,q,alpha=(row[k] for k in KEYS)
    u=4*(v+360)+gap
    n=gamma*T*(1<<u)
    actual1=3 if valuation(n-1,3)==1 else 1
    actual2=3 if valuation(n//2-1,3)==1 else 1
    if (d1,d2)!=(actual1,actual2):return False
    w=d1*d1*d2+T*(1<<(4*(v+360)+2))*m
    return d1!=3 or w%9 in (0,1,4,7)


def feasible_at_modulus(row,v,ell):
    gap,gamma,d1,d2,T,m,q,alpha=(row[k] for k in KEYS)
    x=pow(2,v,ell)
    n=gamma*T*pow(2,gap,ell)*pow(x,4,ell)%ell
    rhs=(alpha*pow(x,4,ell)+q)%ell
    # Enumerate the two unknown residues, with a different evaluation order.
    allowed_c={d1*T*c*c%ell for c in range(ell)}
    for z in range(ell):
        if d2*z*z%ell!=rhs:continue
        second=(d1*gamma*pow(2,gap-2,ell)*x*x+(n-1)*z)%ell
        if second in allowed_c:return True
    return False


def read_curves():
    expected={99,399,943,1023,799}
    rows=json.loads(Path('gap_curve_cases.json').read_text(encoding='utf-8'))
    assert {r['a4'] for r in rows}==expected
    all_points={}
    for row in rows:
        a4=row['a4']
        src=Path(row['input']).read_text(encoding='utf-8')
        assert f'a4:={a4};' in src and 'SetClassGroupBounds' not in src
        assert 'assert rank_proved and group_proved;' in src
        assert 'IntegralPoints(E:FBasis:=basis,SafetyFactor:=2)' in src
        assert 'Order(G.i) eq 0' in src
        transcript='\n'.join(ET.parse(row['response']).getroot().itertext())
        for bad in ('Runtime error','User error','Assertion failed','Time limit'):
            assert bad not in transcript
        assert f'GAP_CURVE {a4}' in transcript
        assert f'GAP_CURVE_COMPLETE {a4}' in transcript
        assert 'PROOF_FLAGS true true' in transcript
        pts=[(int(a),int(b)) for a,b in re.findall(r'^POINT (-?\d+) (-?\d+)$',transcript,re.M)]
        count=int(re.search(r'POINT_COUNT (\d+)',transcript).group(1))
        assert len(pts)==count and len(set(pts))==count
        for x,y in pts:assert y*y==x*x*x+a4*x
        all_points[a4]=pts
    assert sorted(x for x,y in all_points[99])==[0,1,3,12,33,49,99,192]
    return all_points


def check_inverse(points,m):
    found=[]
    for X,Y in points:
        if X<=0 or X%(16*m):continue
        value=X//(16*m)
        exponent=valuation(value)
        if value!=(1<<exponent) or exponent%2:continue
        v=exponent//2
        scale=4*m*(1<<v)
        if Y%scale:continue
        Z=Y//scale
        assert Z*Z==256*m*(16**v)+64-m
        found.append(v)
        assert 4*v+9<49
    return sorted(found)


def check_small_gaps():
    # Only branch (1,3,1), T=1 survives the exact coarse size bound at g=2,3.
    for gap in (2,3):
        possible=[]
        for ga,d1,d2,num,den in [(1,1,1,1,112),(1,1,3,9,112),
                                (1,3,1,27,80),(3,1,1,3,112)]:
            for T in range(1,10,2):
                if den*T**3<num*2**gap:possible.append((ga,d1,d2,T))
        assert possible==[(1,3,1,1)]
    # g=2: w=9+2^(4v+1)*h, 0<h<9 odd; Z0^2=h*16^v+(9-h)/2.
    assert [h for h in range(1,9,2) if ((9-h)//2)%8==1]==[7]
    # g=3: w=9+2^(4v+2)*h, 0<h<9 even; Z0^2=9+h*(2^(4v+2)-1).
    assert [h for h in range(2,9,2) if (9-h)%8==1]==[8]
    for v in range(3):
        assert (7*pow(2,4*v+1,9))%9 not in (0,1,4,7)
        assert (8*pow(2,4*v+2,9))%9 not in (0,1,4,7)


def recurrence_audit():
    found={}
    for name,second,shift,limit in [('A',64,5,681),('B',-16,-5,343)]:
        previous,current=1,second
        for n in range(1,limit+1):
            if n%2:
                expected=3+valuation(3*n+shift)
                actual=valuation(current)
                if expected!=actual:
                    assert n==limit
                    found[name]={'index':n,'actual_v2':actual,'claimed_v2':expected,
                                 'residue_mod_131072':current%131072}
                    break
            previous,current=current,48*current-previous
        else:raise AssertionError('missing counterexample')
    assert found['A']['actual_v2']==13 and found['B']['actual_v2']==16
    return found


def main():
    check_small_gaps()
    cert=json.loads(Path('i3_gap_certificate.json').read_text(encoding='utf-8'))
    assert cert['schema']==1 and cert['min_u']==49 and cert['gap_range']==[4,9]
    period=cert['period']
    assert period==360
    assert sorted(tuple(row[k] for k in KEYS) for row in cert['cases'])==independent_cases()
    assert len({tuple(row[k] for k in KEYS) for row in cert['cases']})==len(cert['cases'])
    for ell in cert['moduli']:
        assert ell%2 and pow(4,period,ell)==1
    curves=read_curves()
    inverses={m:check_inverse(curves[m*(64-m)],m) for m in (7,23,31,47)}
    covered=0
    counts={}
    for row in cert['cases']:
        gap=row['gap']
        counts.setdefault(gap,Counter())[row['method']]+=1
        if row['method']=='factor':
            A=row['d2']*row['alpha'];B=row['d2']*row['q']
            b=isqrt(B);assert b*b==B
            odd=A//2**valuation(A)
            small=2**valuation(2*b)*odd
            bound=small*(small+2*b)
            assert bound==row['product_bound']
            vmin=(49-gap+3)//4
            assert A*16**vmin>bound
        else:
            permitted={v for v in range(period) if branch_ok(row,v)}
            for step in row['eliminations']:
                ell=step['modulus'];assert ell in cert['moduli']
                rejected=set(step['residues'])
                assert len(rejected)==len(step['residues']) and rejected<=permitted
                for v in rejected:
                    assert not feasible_at_modulus(row,v,ell)
                    covered+=1
                permitted-=rejected
            if row['method']=='modular':assert not permitted
            else:
                assert row['method']=='elliptic' and gap==9
                assert (row['gamma'],row['d1'],row['d2'],row['T'])==(1,1,1,1)
                assert row['m'] in inverses
                assert sorted(permitted)==row['surviving_residues']
                assert row['a4']==row['m']*(64-row['m'])
    result={'status':'verified','case_count':len(cert['cases']),'layers':counts,
            'modular_residue_exclusions':covered,'period':period,
            'curve_points_checked':sum(map(len,curves.values())),
            'g9_curve_inverse_v':inverses,'pell_conjecture_counterexamples':recurrence_audit(),
            'even_j_necessary_bound':'u >= 4*v2(j)+10',
            'g4_through_g8_magma_dependency':False,'g9_magma_dependency':True,
            'complete_i3_solution':False}
    Path('verification_i3_gap_layers.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
