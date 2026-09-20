"""Replay exact arithmetic for the direct center curve and saved Magma runs.

Completeness of the three successful integer-point lists depends on Magma;
this script verifies flags, model/input provenance, each point, both signs,
all inverse transformations, and the finite residue deductions independently.
The timed-out w=317 attempt is recorded as incomplete and is not used to
exclude any candidate. Its known positive example is checked directly.
"""
from repo_paths import artifact_path
import hashlib
import json
import re
import xml.etree.ElementTree as ET
from fractions import Fraction
from math import gcd
from pathlib import Path

import sympy as sp
from make_center_curve_magma import CASES, ENDPOINT_CASES, source, endpoint_source
from audit_i3_integrated_digits import family_values


def symbolic_audit():
    z,c,w,d1,d2=sp.symbols('z c w d1 d2',nonzero=True)
    c0=d1*d1*d2
    n=2*d2*(z*z-d1*d1)/w+2
    cubic=(z+d1)*(2*d2*z*z-d1*d2*z+w-c0)-2*w*d1*c*c
    checks=[]
    def check(name, expr):
        assert sp.factor(expr)==0, name
        checks.append(name)
    check('eliminate n', (4*c*c-n-2*(n-1)*z/d1)*w*d1/2+cubic)
    X,Y=4*w*d1*d2*(z+d1),8*w*w*c0*c
    a2,a4=-10*w*c0,8*w*w*c0*(w+2*c0)
    check('integral elliptic map',
          Y*Y-X**3-a2*X*X-a4*X+32*d1**3*d2*d2*w**3*cubic)
    check('nonzero discriminant',
          16*a4*a4*(a2*a2-4*a4)-4096*w**6*c0**3*(w+2*c0)**2*(9*c0-8*w))
    xp,yp=2*w*c0,4*w*w*c0
    check('universal rational point',yp*yp-xp**3-a2*xp*xp-a4*xp)
    slope=(3*xp*xp+2*a2*xp+a4)/(2*yp)
    check('double universal point',slope*slope-a2-2*xp-(2*w+3*c0)**2/4)
    x,y=sp.symbols('x y',nonzero=True)
    # On y^2=x^3+a2*x^2+a4*x, this is the duplication formula.
    check('duplication identity',
          (3*x*x+2*a2*x+a4)**2-4*(x**3+a2*x*x+a4*x)*(a2+2*x)
          -(x*x-a4)**2)
    lam,rho,j=sp.symbols('lam rho j',nonzero=True)
    endpoint_cubic=(16*d2*rho**3-16*d1*d2*rho*rho+8*lam*rho+d1*lam
                    -d1*lam*(2*j-1)**2)
    endpoint_n=2*d2*rho*(rho-d1)/lam+2
    check('endpoint eliminate n',
          (j*(j-1)-2*(endpoint_n-1)*rho/d1)*4*lam*d1+endpoint_cubic)
    ex,ey=16*d1*d2*lam*rho,16*c0*lam*lam*(2*j-1)
    ea2,ea4,ea6=-16*c0*lam,128*c0*lam**3,256*c0*c0*lam**4
    check('endpoint integral elliptic map',
          ey*ey-ex**3-ea2*ex*ex-ea4*ex-ea6
          +256*d1**3*d2*d2*lam**3*endpoint_cubic)
    check('endpoint nonzero discriminant',
          16*sp.discriminant(x**3+ea2*x*x+ea4*x+ea6,x)
          +1048576*c0**3*lam**7*(128*lam*lam+107*c0*lam-64*c0*c0))
    assert 210**2 < 107**2+4*128*64 < 211**2
    # A rational constant term times n does not affect the leading shape;
    # both cofactor upper bounds are exact rational consequences.
    return checks


def read_case(row):
    w,d1,d2=row['w'],row['delta1'],row['delta2']
    input_bytes=artifact_path(row['input']).read_bytes()
    assert input_bytes.decode('utf-8').replace('\r\n','\n')==source(w,d1,d2)
    response=artifact_path(row['response']).read_bytes()
    root=ET.fromstring(response)
    text='\n'.join(root.itertext())
    result=dict(w=w,delta1=d1,delta2=d2,
                input_sha256=hashlib.sha256(input_bytes).hexdigest(),
                response_sha256=hashlib.sha256(response).hexdigest(),
                magma_version=root.findtext('headers/version'))
    if row['role']=='regression_attempt':
        assert 'CENTER_CASE_COMPLETE' not in text
        assert 'exceeded the time limit' in text
        result.update(status='incomplete: service time limit; not used for exclusion')
        return result
    assert 'Runtime error' not in text and 'User error' not in text
    assert 'Assertion failed' not in text and 'exceeded the time limit' not in text
    assert f'CENTER_CASE {w} {d1} {d2}' in text
    assert f'CENTER_CASE_COMPLETE {w} {d1} {d2}' in text
    assert text.count('PROOF_FLAGS true true')==1
    points=[tuple(map(int, pair)) for pair in re.findall(r'^POINT (-?\d+) (-?\d+)$',text,re.M)]
    count=int(re.search(r'^POINT_COUNT (\d+)$',text,re.M).group(1))
    assert count==len(points)==len(set((x,abs(y)) for x,y in points))
    c0=d1*d1*d2
    a2,a4=-10*w*c0,8*w*w*c0*(w+2*c0)
    dx,dy=4*w*d1*d2,8*w*w*c0
    preimages=[]
    for x,y in points:
        assert y*y==x**3+a2*x*x+a4*x
        # The inverse uses |Y|, accounting for both P and -P.
        if x%dx or abs(y)%dy:
            continue
        z,c=x//dx-d1,abs(y)//dy
        if min(z,c)<=0:
            continue
        n=Fraction(2*d2*(z*z-d1*d1),w)+2
        assert 4*c*c==n+2*(n-1)*z/d1
        if n.denominator!=1:
            continue
        n=int(n)
        j=Fraction(n,2)-c
        preimages.append(dict(n=n,j=str(j),c=c,z=z))
        assert not (n%2==0 and 4<=j<n//2)
    expected={(61,1,1):[(2,0),(120,0),(128,1)],
              (55,1,3):[(2,0)],(37,3,1):[(2,0)]}
    assert sorted((p['n'],Fraction(p['j'])) for p in preimages)==expected[w,d1,d2]
    result.update(status='complete according to Magma; all point arithmetic replayed',
                  rank=int(re.search(r'^RANK (\d+)$',text,re.M).group(1)),
                  point_count=count,points=points,positive_integral_preimages=preimages,
                  surviving_index_pairs=0)
    return result


def read_endpoint(row):
    lam,d1,d2=row['lam'],row['delta1'],row['delta2']
    raw_input=artifact_path(row['input']).read_bytes()
    assert raw_input.decode('utf-8').replace('\r\n','\n')==endpoint_source(lam,d1,d2)
    raw_response=artifact_path(row['response']).read_bytes()
    root=ET.fromstring(raw_response)
    text='\n'.join(root.itertext())
    assert 'Runtime error' not in text and 'User error' not in text
    assert 'Assertion failed' not in text and 'exceeded the time limit' not in text
    assert f'ENDPOINT_CASE {lam} {d1} {d2}' in text
    assert f'ENDPOINT_CASE_COMPLETE {lam} {d1} {d2}' in text
    assert text.count('PROOF_FLAGS true true')==1
    points=[tuple(map(int,pair)) for pair in re.findall(r'^POINT (-?\d+) (-?\d+)$',text,re.M)]
    count=int(re.search(r'^POINT_COUNT (\d+)$',text,re.M).group(1))
    assert count==len(points)==len(set((x,abs(y)) for x,y in points))
    c0=d1*d1*d2
    a2,a4,a6=-16*c0*lam,128*c0*lam**3,256*c0*c0*lam**4
    dx,dy=16*d1*d2*lam,16*c0*lam*lam
    preimages=[]
    for x,y in points:
        assert y*y==x**3+a2*x*x+a4*x+a6
        if x%dx or abs(y)%dy:
            continue
        rho=x//dx
        j=Fraction(abs(y)//dy+1,2)
        if rho<=0 or j.denominator!=1:
            continue
        j=int(j)
        n=Fraction(2*d2*rho*(rho-d1),lam)+2
        assert j*(j-1)==2*(n-1)*rho/d1
        if n.denominator!=1:
            continue
        n=int(n)
        preimages.append(dict(n=n,j=j,rho=rho))
        assert n%16!=0
    expected={(2,1,1):[(2,2),(4,4),(8,7),(22,15),(134,57),(2072,437)],
              (2,1,3):[(2,2),(218,63)]}
    assert sorted((p['n'],p['j']) for p in preimages)==expected[lam,d1,d2]
    return dict(lam=lam,delta1=d1,delta2=d2,
                input_sha256=hashlib.sha256(raw_input).hexdigest(),
                response_sha256=hashlib.sha256(raw_response).hexdigest(),
                magma_version=root.findtext('headers/version'),
                status='complete according to Magma; all point arithmetic replayed',
                rank=int(re.search(r'^RANK (\d+)$',text,re.M).group(1)),
                point_count=count,points=points,positive_integral_preimages=preimages,
                surviving_index_pairs=0)


def extra_audit():
    # Residue obstruction in d1=3,d2=1: Q=1 mod 3. If 3|w,
    # z^2=9+wQ forces 3|z and hence 9|w.
    possible={w for w in range(9) if any((z*z-9-w*Q)%9==0
              for z in range(9) for Q in (1,4,7))}
    assert possible=={0,1,4,7}
    assert 2 not in possible  # Also excludes lambda=2 when delta1=3.
    next_bounds=[]
    for d1,d2,removed,even_min,target in [(1,1,61,961,125),
                                       (1,3,55,835,119),(3,1,37,457,229)]:
        c0=d1*d1*d2
        residues=[]
        for w in range(c0+2,even_min+1,2):
            if w==removed:
                continue
            if w<even_min and (w+3*c0)%64:
                continue
            if d1==3 and w%9 not in possible:
                continue
            residues.append(w)
        assert min(residues)==target
        next_bounds.append(dict(delta1=d1,delta2=d2,w_at_least=target))
    # Verify the integral map on a known relaxed infinite family, not just
    # on rejected inverse points of the three small-w curves.
    examples=[]
    for m in range(65):
        A,B,C,a,b,g,h,S,R,n,j=family_values(m)
        c=n//2-j
        r=(4*c*c-1)//(n-1)
        z=(r-1)//2
        w=(z*z-1)//(A*B*C)
        x,y=4*w*(z+1),8*w*w*c
        assert y*y==x**3-10*w*x*x+8*w*w*(w+2)*x
        assert Fraction(2*(z*z-1),w)+2==n
        rho=Fraction(j*(j-1),2*(n-1))
        lam=Fraction(rho*(rho-1),A*B*C)
        assert rho.denominator==lam.denominator==1 and lam>0
        rho,lam=int(rho),int(lam)
        ex,ey=16*lam*rho,16*lam*lam*(2*j-1)
        assert ey*ey==ex**3-16*lam*ex*ex+128*lam**3*ex+256*lam**4
        assert Fraction(2*rho*(rho-1),lam)+2==n
        if m==0:
            assert (w,n,j)==(317,76672,26775)
            examples.append(dict(w=w,lam=lam,n=n,j=j,z=z,c=c,X=x,Y=y))
    # Exact initial doubling valuations for the universal point, in several
    # parameter values. The proof gives all iterated doublings.
    doubling_checks=0
    for w in (1,37,55,61,317):
        for c0 in (1,3,9):
            a2,a4=-10*w*c0,8*w*w*c0*(w+2*c0)
            x=Fraction((2*w+3*c0)**2,4)
            for r in range(1,6):
                assert x.denominator & -x.denominator == 4**r
                assert x.numerator%2==1
                x=(x*x-a4)**2/(4*x*(x*x+a2*x+a4))
                doubling_checks+=1
    return dict(w_mod_9_when_delta1_is_3=sorted(possible),new_bounds=next_bounds,
                relaxed_map_checks=65,regression_examples=examples,
                exact_doubling_checks=doubling_checks)


def main():
    assert __debug__, 'Run with assertions enabled.'
    rows=json.loads(artifact_path('center_curve_cases.json').read_text())
    endpoint_rows=json.loads(artifact_path('endpoint_curve_cases.json').read_text())
    assert [(r['w'],r['delta1'],r['delta2']) for r in rows]==CASES
    assert [(r['lam'],r['delta1'],r['delta2']) for r in endpoint_rows]==ENDPOINT_CASES
    report=dict(status='all required audits passed; not a proof of Erdős 699',
                symbolic_checks=symbolic_audit(),cases=[read_case(r) for r in rows],
                endpoint_cases=[read_endpoint(r) for r in endpoint_rows],
                additional_checks=extra_audit(),
                completeness_dependency='Magma 2.29-10, proved full Mordell--Weil groups; not re-proved by Python')
    artifact_path('verification_i3_center_curve.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in ('cases','endpoint_cases')},indent=2))
    print(json.dumps([{k:v for k,v in r.items() if k in ('w','delta1','delta2','status','rank','point_count','positive_integral_preimages')} for r in report['cases']],indent=2))
    print(json.dumps([{k:v for k,v in r.items() if k in ('lam','delta1','delta2','status','rank','point_count','positive_integral_preimages')} for r in report['endpoint_cases']],indent=2))


if __name__=='__main__':
    main()
