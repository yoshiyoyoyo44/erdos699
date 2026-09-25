#!/usr/bin/env python3
"""Exact independent checks for the general regular-row argument and bridge."""
from pathlib import Path
from fractions import Fraction
from math import comb, gcd, lcm, isqrt, prod
import json
import random
from digit_bridge import bridge_certificate, degree, trim, add, scale, mul, norm, evaluate

ROOT=Path(__file__).resolve().parent

def vp(n,p):
    e=0
    while n%p==0:
        e+=1;n//=p
    return e

def primes_to(n):
    out=[]
    for p in range(2,n+1):
        if all(p%d for d in range(2,isqrt(p)+1)):out.append(p)
    return out

def row_part(n,i,r,ps):
    q=n-r
    for p in ps:
        if p>=i:break
        while q%p==0:q//=p
    if i in ps and q%i==0:q//=i
    return q

def rational_remainder(A,B):
    """Ordinary long division over Q, distinct from integer pseudo-division."""
    A=list(map(Fraction,trim(A)));B=list(map(Fraction,trim(B)))
    while degree(A)>=degree(B):
        t=A[-1]/B[-1];offset=degree(A)-degree(B)
        for k,x in enumerate(B):A[k+offset]-=t*x
        A=trim(A)
    return A

def main():
    obj=json.loads((ROOT/'certificate.json').read_text())
    old=json.loads((ROOT/'previous_phase/certificate.json').read_text())
    ps=primes_to(200)
    counts=dict(prefix_count_constants=0,uniform_size_constants=0,
        regular_rows=0,row_part_matches=0,prefix_resonance_checks=0,
        nonzero_linear_products=0,nontrivial_elimination_divisibilities=0,
        polynomial_cases=0,rational_remainder_checks=0,
        conditional_filter_checks=0)
    for row in obj['rows']:
        i=row['i'];pi=sum(p<i for p in ps)
        assert pi==row['pi']
        epsilon=i if i in ps else 1
        source=next(r for r in old['rows'] if r['i']==i)
        for t in row['cases']:
            B=next(x['B'] for x in source['thresholds']
                   if (x['n_power'],x['uses_a100'])==(t['n_power'],t['uses_a100']))
            assert B==t['excluded_denominator_B']
            # Find the least usable prefix by enumerating the pigeonhole count.
            D=next(v for v in range(1,i+1) if v-(v+B)//(B+1)>pi)
            assert D==t['D'] and t['prefix_last_row']==D-1
            C=epsilon
            small_lcm=1
            for x in range(1,D):small_lcm=lcm(small_lcm,x)
            C*=small_lcm
            assert C==int(t['row_constant'])
            assert 512**D>2*C*(i-1)**D
            counts['prefix_count_constants']+=1
            counts['uniform_size_constants']+=1
    rng=random.Random(6992509)
    # Do not search for absent counterexamples and call the test non-vacuous:
    # test the unconditional regular-row lemma directly.
    for i in range(3,120):
        pi=sum(p<i for p in ps)
        for n in [2*i+2,2*i+17,10**15+i]+[rng.randrange(2*i+2,10000) for _ in range(3)]:
            for k in sorted({pi,pi+1,min(i-1,pi+4)}):
                exceptions={max(range(k+1),key=lambda r:vp(n-r,p)) for p in ps if p<i}
                L=lcm(*range(1,k+1))
                for r in range(k+1):
                    if r in exceptions:continue
                    smooth=prod(p**vp(n-r,p) for p in ps if p<i)
                    assert L%smooth==0
                    Qr=row_part(n,i,r,ps)
                    epsilon=i if i in ps else 1
                    assert n-r<=epsilon*L*Qr
                    counts['regular_rows']+=1
        for n in (2*i+2,3*i+19):
            A=comb(n,i);Q=A
            for p in ps:
                if p>=i:break
                while Q%p==0:Q//=p
            for r in range(i):
                assert gcd(Q,n-r)==row_part(n,i,r,ps)
                counts['row_part_matches']+=1
    # Construct lattice resonances, keeping zero products out of the proof.
    for _ in range(6000):
        i=rng.randrange(3,120);s=rng.randrange(i);u=rng.randrange(s+1)
        a=rng.randrange(2,120);t=rng.randrange(1,a//2+1);q=rng.randrange(i,2000)
        n=a*q+s;j=t*q+u
        if not i<j<=n//2:continue
        g=gcd(a,t);alpha=t//g;b=a//g
        pi=sum(p<i for p in ps)
        D=pi+1+(pi+b-1)//(b-1)
        if D>i:continue
        k=D-1;delta=b*j-alpha*n
        R=[r for r in range(k+1) if any(delta==b*v-alpha*r for v in range(r+1))]
        assert len(R)<=(D+b-1)//b
        exceptions={max(range(k+1),key=lambda r:vp(n-r,p)) for p in ps if p<i}
        good=[r for r in range(k+1) if r not in R and r not in exceptions]
        assert good
        counts['prefix_resonance_checks']+=1
        for r in good:
            terms=[b*(u-v)+alpha*(r-s) for v in range(r+1)]
            assert all(terms)
            assert all(abs(z)<=b*(i-1) for z in terms)
            P=prod(terms)
            assert P!=0 and abs(P)<=(b*(i-1))**(r+1)
            counts['nonzero_linear_products']+=1
            Qr=row_part(n,i,r,ps)
            fall=prod(j-v for v in range(r+1))
            if Qr>1 and fall%Qr==0:
                assert P%Qr==0
                C=(i if i in ps else 1)*lcm(*range(1,k+1))
                assert n-k<=C*(b*(i-1))**D
                counts['nontrivial_elimination_divisibilities']+=1
    assert counts['nontrivial_elimination_divisibilities']>0
    improved=0;poly_examples=[]
    for z in range(1200):
        m=1+z%12
        F=[2]+[rng.randrange(21) for _ in range(m-1)]+[rng.randrange(1,21)]
        J=[rng.randrange(x+1) for x in F]
        cert=bridge_certificate(F,J)
        T=cert['T'];c=cert['c'];d=cert['d']
        assert degree(T)<m and gcd(c,d)==1
        for part in cert['parts']:
            s=part['s'];G=[1]
            for k in range(s+1):G=mul(G,add(T,[c*s-d*k]))
            R=rational_remainder(G,add(F,[-s]))
            multiplier=F[-1]**part['pseudo_exponent']
            assert trim(scale(R,multiplier))==part['remainder']
            assert norm(part['remainder'])<=int(part['remainder_bound'])
            counts['rational_remainder_checks']+=1
        counts['polynomial_cases']+=1
        improved+=int(int(cert['adaptive_threshold'])<int(cert['old_threshold']))
    for ex in obj['bridge_diagnostics']:
        assert bridge_certificate(ex['F'],ex['J'])['adaptive_threshold']==ex['adaptive_threshold']
        assert int(ex['adaptive_threshold'])<int(ex['old_threshold'])
        # These are known polynomial solutions excluded arithmetically by n=2 mod 4.
        for x in (1,2,5,101):assert evaluate(ex['F'],x)%4==2
        poly_examples.append(dict(m=ex['m'],r=ex['r'],adaptive_threshold=ex['adaptive_threshold'],
                                  old_threshold=ex['old_threshold']))
    # Independent direct integer inequalities for the index's conditional filter.
    for row in obj['conditional_index_filters']['rows']:
        m=row['m'];want={}
        for k in range(m+1):
            t=Fraction(k,m)
            valid=[]
            for r in range(m):
                ok=192*r>=145*m+8
                if t==Fraction(1,2):ok=ok and 6*r>5*m
                if t in (Fraction(1,4),Fraction(3,4)):ok=ok and 96*r>=79*m
                if t in (0,1):ok=ok and 12*r>=11*m
                if ok:valid.append(r)
                counts['conditional_filter_checks']+=1
            if valid:want[str(t)]=min(valid)
        assert want=={x['t']:x['r_min'] for x in row['allowed']}
        assert {t:r for t,r in want.items() if Fraction(t)<=Fraction(1,2)}=={
            x['t']:x['r_min'] for x in row['allowed_in_counterexample_orientation']}
    # The old single-base condition is genuinely restrictive; it is not automatic.
    F=[2,2,2,1];J=[1,1,1]
    assert rational_remainder(mul(J,add(J,[-1])),add(F,[-1]))==[0]
    assert rational_remainder(mul(mul(J,add(J,[-1])),add(J,[-2])),add(F,[-2]))!=[0]
    # n >= 10^200: the uniform exponent forces integer cofactors >= 3474.
    assert (512*3473)**32<10**200<(512*3474)**32
    c119=lcm(*range(1,32))
    assert c119*(118*5559)**32<10**200-31<=c119*(118*5560)**32
    result=dict(status='PASS',counts=counts,
        random_polynomial_cases_with_strictly_improved_threshold=improved,
        bridge_examples=poly_examples,
        explicit_large_n_cofactor=dict(n_min='10^200',a_min=3474,i119_a_min=5560),
        missing_manuscript_bodies=[
            'erdos699_all_degree_prime_power_bridge_2026-09-23.md',
            'erdos699_uniform_three_quarter_obstruction_2026-09-25.md',
            'erdos699_moving_quotient_and_ramification_2026-09-25.md'],
        scope='General proofs are in REPORT.md. Degree filters retain the supplied index as a conditional input.')
    (ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
