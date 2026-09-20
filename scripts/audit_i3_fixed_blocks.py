"""Check the fixed-block reduction and the arithmetic of saved Magma outputs.

This does NOT reprove completeness of a Mordell--Weil basis or of the integer
point list. Those steps rely on Magma and can be rerun with the supplied inputs.
Run with assertions enabled. SymPy is used only for symbolic identities.
"""
from repo_paths import artifact_path, CASES_DIR
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path

import sympy as sp


def symbolic_audit():
    n,j,K,r,D,t=sp.symbols('n j K r D t')
    aa,bb,cc=sp.symbols('aa bb cc')
    y=sp.symbols('y')
    equations=[]
    # The r_C and r_B identities become this polynomial after cancellation.
    equations.append((K*(2*j-1))**2-(K*K+4*K*r*(n-1)*(n-2))
                     -4*K*(K*j*(j-1)-r*(n-1)*(n-2)))
    equations.append((K*(n-2*j))**2-((K*K-4*K*r)*n*n+12*K*r*n-8*K*r)
                     +4*K*(K*j*(n-j)-r*(n-1)*(n-2)))
    X,V=aa*t*t,aa*t*y
    equations.append(V*V-(X**3+bb*X*X+aa*cc*X)-aa*aa*t*t*(y*y-aa*t**4-bb*t*t-cc))
    qa,qb,qc=4*K*r*D*D,-12*K*r*D,K*K+8*K*r
    equations.append(qb*qb-4*qa*qc-16*K*K*r*D*D*(r-K))
    qa,qb,qc=K*(K-4*r)*D*D,12*K*r*D,-8*K*r
    equations.append(qb*qb-4*qa*qc-16*K*K*r*D*D*(r+2*K))
    # Endpoint bounds in the two ratios.
    equations.append((n-1)*(n-2)-4*(n/2-1)*(n/2-2)-3*(n-2))
    equations.append(4*(n/2+1)*(n/2)-(n-1)*(n-2)-(5*n-2))
    delta,d2,A,B,C=sp.symbols('delta d2 A B C')
    den=(n-1)*(n-2)
    equations.append(sp.cancel(2*delta*j*(n-j)/den
                               +delta*(n-j)*(n-j-1)/den
                               +delta*j*(j-1)/den-delta*n/(n-2)))
    # Boundary quartics before n=t^2 or 2*t^2 is inserted.
    A,C=sp.symbols('A C')
    equations.append(3*(C*C+8*A*A)**2-(8*(6*A*C+2)**2-24*(6*A*C+2)+19)
                     -3*(C*C-8*A*C-8*A*A-1)*(C*C+8*A*C-8*A*A+1))
    # In the second boundary case, the quadratic relation is used to reduce.
    relation=8*C*C-4*A*C-A*A-3
    expression=(A*A+8*C*C)**2-3*(4*(2*A*C+2)**2-12*(2*A*C+2)+11)
    assert sp.rem(expression,relation,C)==0
    assert all(sp.expand(e)==0 for e in equations)
    # Exhaust the two positive-even summands in a*zeta+b*h=6.
    odd=[]; even=[]
    for a in range(1,7):
        for b in range(1,7):
            for h in range(1,7):
                for z in range(1,7):
                    if a*z+b*h!=6 or (a*z)%2 or (b*h)%2:
                        continue
                    if a%2==b%2==0 and h%2==z%2==1:
                        odd.append((a,b,h,z))
                    if a%2==b%2==1 and h%2==z%2==0:
                        even.append((a,b,h,z))
    # The products 2 and 4 permit h or z=3 only with product 6, which is excluded.
    assert set(odd)=={(2,4,1,1),(4,2,1,1)}
    assert set(even)=={(1,1,2,4),(1,1,4,2)}
    residues=[]
    for b,h,z,a in [(2,1,1,4),(4,1,1,2),(1,4,2,1),(1,2,4,1)]:
        residues.append({(cc*((z*cc-2*aa*b))*h-aa*aa*a*b)%8
                         for aa in (1,3,5,7) for cc in (1,3,5,7)})
    assert residues==[{5},{1},{7},{3}]
    # A known relaxed positive example checks normalization, not the special n.
    n,j,A,B,C=76672,26775,11,85,41
    rB,rC,s=36,5,5
    den=(n-1)*(n-2)
    assert Fraction(rC,C)==Fraction(j*(j-1),den)
    assert Fraction(rB,B)==Fraction((n-j)*(n-j-1),den)
    assert Fraction(s,2*A)==Fraction(j*(n-j),den)
    assert Fraction(s,A)+Fraction(rB,B)+Fraction(rC,C)==1+Fraction(1,A*B*C)
    # The difficult B=7, T=r=11 curve has a short local obstruction.
    assert {m for m in range(6) if 11*pow(4,m,7)%7==2}=={1,4}
    values={(111804*pow(4,m,13)**2-30492*pow(4,m,13)+2289)%13 for m in (1,4)}
    assert values=={2,11} and not values & {x*x%13 for x in range(13)}
    return len(equations)+1


def exceptional_three(n):
    return 3 if n%3==0 and n%9!=0 else 1


def independent_parameter_keys(role,value):
    """Enumerate n mod 18 first, not the generator's delta/parity branches."""
    keys=set()
    for gamma in (1,3):
        for T in range(1,3*value+1,2):
            M=gamma*T
            if exceptional_three(M)!=gamma:
                continue
            for u in range(48,54):
                n=M*2**u
                d1,d2=exceptional_three(n-1),exceptional_three(n//2-1)
                if gcd(value,gamma*d1*d2*T)!=1:
                    continue
                K=d1*d2*value
                for r in range(1,3*value):
                    if role=='A':
                        good=(2*r<K and r%(T*T)==0
                              and ((r & -r).bit_length()-1)%2==0)
                    else:
                        good=(r%T==0 and (4*r<K if role=='C' else K<4*r and r<K))
                    if good:
                        keys.add((gamma,d1,d2,T,r,u%2))
    return keys


def model_for(row,role):
    K=row['delta1']*row['delta2']*row[role]
    D=row['gamma']*row['T']*2**row['parity']
    r=row['r']
    assert (K,D)==(row['K'],row['D'])
    if role=='A':
        K*=2
        coeff=(K*(K-4*r)*D*D,12*K*r*D,-8*K*r)
    else:
        coeff=(4*K*r*D*D,-12*K*r*D,K*K+8*K*r)
    a,b,c=coeff
    assert row['quartic']==[a,0,b,0,c]
    assert a>0 and c!=0 and b*b-4*a*c!=0
    return coeff


def boundary_options(row):
    B,T,K,r,d1=[row[k] for k in ['B','T','K','r','delta1']]
    out=[]
    # Enumerate the two bounded product equations with elementary division.
    for h in range(1,2*r//T+1):
        if (2*r//T)%h:
            continue
        b=(2*r//T)//h
        v=(h & -h).bit_length()-1
        need=d1*(0 if v==0 else 3 if v==1 else -1)%8
        for z in range(1,2*(K-r)+1):
            if 2*(K-r)%z:
                continue
            a=2*(K-r)//z
            if (a+h)%2!=1 or (b+h)%2!=1 or (z-h)%2 or a*b%8!=need:
                continue
            modulus=T*T*B
            if not any((a*b*x*x+d1)%modulus==0 for x in range(modulus)):
                continue
            out.append((a,b,h,z))
    return sorted(out)


def verify_modular_exclusion(row,certificate):
    period,moduli=certificate['period'],certificate['moduli']
    assert period>0
    F,D,d1,d2=row['B'],row['D'],row['delta1'],row['delta2']
    for modulus in [9,d2*F]+moduli:
        assert modulus>1 and modulus%2 and pow(4,period,modulus)==1
    square_sets={q:{x*x%q for x in range(q)} for q in moduli}
    a,_,b,_,c=row['quartic']
    for m in range(period):
        n9=D*pow(4,m,9)%9
        if exceptional_three(n9-1)!=d1 or exceptional_three(5*n9-1)!=d2:
            continue
        if D*pow(4,m,d2*F)%(d2*F)!=2%(d2*F):
            continue
        assert any((a*pow(4,m,q)**2+b*pow(4,m,q)+c)%q not in square_sets[q] for q in moduli)


def transcript(path):
    root=ET.fromstring(artifact_path(path).read_bytes())
    result='\n'.join(root.find('results').itertext())
    assert not re.search(r'Runtime error|User error|Assertion failed|Time limit',result)
    if root.get('aggregate')=='true':
        provenance=root.find('sources')
        source=artifact_path(provenance.get('full_input'))
        assert hashlib.sha256(source.read_bytes()).hexdigest()==provenance.get('sha256')
        fullcode=source.read_text()
        fullpieces=re.findall(r'print "CASE_\d+", \d+;.*?print "CASE_\d+_COMPLETE";',fullcode,re.S)
        allpieces=[]
        alloutput=[]
        for entry in provenance:
            ip,op=artifact_path(entry.get('input')),artifact_path(entry.get('response'))
            assert hashlib.sha256(ip.read_bytes()).hexdigest()==entry.get('input_sha256')
            assert hashlib.sha256(op.read_bytes()).hexdigest()==entry.get('response_sha256')
            allpieces+=re.findall(r'print "CASE_\d+", \d+;.*?print "CASE_\d+_COMPLETE";',ip.read_text(),re.S)
            raw=ET.parse(artifact_path(op)).getroot()
            assert raw.get('aggregate') is None
            alloutput += [node.text or '' for node in raw.find('results')]
        assert allpieces==fullpieces
        assert [node.text or '' for node in root.find('results')][:-1]==alloutput
    return result,root.findtext('headers/version')


def parse_points(text,label):
    part=re.search(label+r'\s*\[(.*?)\]',text,re.S).group(1)
    triples=re.findall(r'\(\s*([\d/\-]+)\s*:\s*([\d/\-]+)\s*:\s*1\s*\)',part)
    assert len(triples)==part.count('(')
    return [(Fraction(x),Fraction(y)) for x,y in triples]


def audit_curve(text,coeff):
    a,b,c=coeff
    assert text.count('PROOF_FLAGS true true')==1
    points=parse_points(text,'INTEGRAL_POINTS')
    basis=parse_points(text,'FREE_BASIS')
    for x,y in points+basis:
        assert y*y==x*x*x+b*x*x+a*c*x
    assert all(x.denominator==y.denominator==1 for x,y in points)
    assert len({x for x,y in points})==len(points)  # points are returned up to sign
    ts=set()
    for x,y in points:
        x,y=int(x),int(y)
        if x<=0 or x%a:
            continue
        t=isqrt(x//a)
        if t*t!=x//a or y%(a*t):
            continue
        q=y//(a*t)
        assert q*q==a*t**4+b*t*t+c
        ts.add(t)
    printed=set(map(int,re.findall(r'\d+',re.search(r'POSITIVE_T\s*\{([^}]*)\}',text).group(1))))
    assert ts==printed
    return dict(positive_t=sorted(ts),integer_points_up_to_sign=len(points),free_rank=len(basis))


def main():
    report={'symbolic_identities':symbolic_audit(),
            'completeness_dependency':'Magma 2.29-10, full Mordell-Weil proof flags and IntegralPoints; not independently certified by this Python audit',
            'boundary':[],'fixed_blocks':[]}
    modular=json.loads(artifact_path('fixed_block_modular_exclusions.json').read_text())
    report['modular_certificates']={}
    for name,certificates in modular.items():
        rows=json.loads(artifact_path(f'small_{name}_cases.json').read_text())
        for number,certificate in certificates.items():
            verify_modular_exclusion(rows[int(number)],certificate)
        report['modular_certificates'][name]=len(certificates)
    text,version=transcript('magma_boundary_quartics.xml')
    chunks=text.split('ELLIPTIC_MODEL ')[1:]
    assert len(chunks)==2 and 'BOUNDARY_QUARTICS_COMPLETE' in text
    for chunk,coeff,expected,parity in zip(chunks,[(96,-144,57),(12,-36,33)],[[1],[1,2,83]],[1,0]):
        result=audit_curve(chunk,coeff)
        assert result['positive_t']==expected
        result['quartic_coefficients']=list(coeff)
        assert all(t&(t-1) or 2*(t.bit_length()-1)+parity<49 for t in expected)
        report['boundary'].append(result)
    for path in sorted(CASES_DIR.glob('small_*_cases.json')):
        match=re.fullmatch(r'small_([ABC])(\d+)_cases.json',path.name)
        if not match:
            continue
        role,value=match[1],int(match[2])
        xml=artifact_path(f'magma_small_{role}{value}.xml')
        if not xml.exists():
            continue
        rows=json.loads(path.read_text())
        keys={(r['gamma'],r['delta1'],r['delta2'],r['T'],r['r'],r['parity']) for r in rows}
        assert len(keys)==len(rows)
        assert keys==independent_parameter_keys(role,value)
        text,version=transcript(xml)
        assert f'SMALL_{role}{value}_COMPLETE' in text
        chunks=re.findall(r'CASE_(\d+) '+str(value)+r'\s(.*?)CASE_\1_COMPLETE',text,re.S)
        assert len(chunks)==len(rows)
        source=artifact_path(f'i3_small_{role}{value}.magma').read_text()
        constants=[tuple(map(int,m)) for m in re.findall(r'aa:=(-?\d+); bb:=(-?\d+); cc:=(-?\d+);',source)]
        assert len(constants)==len(rows)
        results=[]
        for i,((number,chunk),row) in enumerate(zip(chunks,rows)):
            assert int(number)==i
            coeff=model_for(row,role)
            assert coeff==constants[i]
            if role=='B':
                options=boundary_options(row)
                part=re.search(r'BOUNDARY_OPTIONS\s*\[(.*?)\]',chunk,re.S).group(1)
                printed=sorted(tuple(map(int,m)) for m in re.findall(r'<\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*,\s*(\d+)\s*>',part))
                assert printed==options
            if 'ARITHMETIC_EXCLUSION' in chunk:
                assert role=='B' and 'PROOF_FLAGS' not in chunk
                if 'MODULAR_EXCLUSION' in chunk:
                    cert=modular[f'{role}{value}'][str(i)]
                    printed=re.search(r'MODULAR_CERT\s*(\d+)\s*\[(.*?)\]',chunk,re.S)
                    assert int(printed[1])==cert['period']
                    assert list(map(int,re.findall(r'\d+',printed[2])))==cert['moduli']
                    verify_modular_exclusion(row,cert)
                else:
                    assert not options
                result=dict(positive_t=[],arithmetic_exclusion=True,
                            modular_exclusion='MODULAR_EXCLUSION' in chunk)
            else:
                assert role!='B' or options
                result=audit_curve(chunk,coeff)
            assert all(t&(t-1) or 2*(t.bit_length()-1)+row['parity']<49 for t in result['positive_t'])
            result['case']=i
            results.append(result)
        report['fixed_blocks'].append(dict(role=role,value=value,cases=results,magma_version=version,
                                           source_sha256=hashlib.sha256(artifact_path(f'i3_small_{role}{value}.magma').read_bytes()).hexdigest(),
                                           transcript_sha256=hashlib.sha256(xml.read_bytes()).hexdigest()))
    artifact_path('verification_i3_fixed_blocks.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(dict(symbolic_identities=report['symbolic_identities'],boundary_curves=2,
                          blocks=[(b['role'],b['value'],len(b['cases'])) for b in report['fixed_blocks']],
                          modular_certificates=report['modular_certificates'],
                          complete_integer_point_lists_depend_on_magma=True)))


if __name__=='__main__':
    main()
