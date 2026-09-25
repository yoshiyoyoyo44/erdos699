#!/usr/bin/env python3
"""Independent arithmetic checks; see REPORT.md for the infinite proofs."""
from math import comb, factorial, gcd, isqrt, lcm, prod
from pathlib import Path
import json
import random
import sys
from row_common_divisor import row_common_divisor

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parent

def primes_to(cap):
    out=[]
    for k in range(2, cap+1):
        if all(k%p for p in out if p*p<=k):
            out.append(k)
    return out

def factor(n, ps):
    out={}
    for p in ps:
        if p*p>n:
            break
        while n%p==0:
            out[p]=out.get(p,0)+1
            n//=p
    if n>1:
        out[n]=out.get(n,0)+1
    return out

def vp(n,p):
    e=0
    while n and n%p==0:
        n//=p
        e+=1
    return e

def carry_count(n,j,p,levels=None):
    q=p
    out=0
    k=1
    while q<=n and (levels is None or k<=levels):
        out += j%q>n%q
        q*=p
        k+=1
    return out

def old_global(Q,i,n,j,a,b):
    delta=b*j-a*n
    M=1
    for s in range(i):
        for t in range(s+1):
            z=delta-(b*t-a*s)
            M=lcm(M,gcd(Q,abs(z) if z else n-s))
    return Q//M

def main():
    cert=json.loads((ROOT/'certificate.json').read_text())
    maxb=max(t['first_failed_b'] for r in cert['rows'] for t in r['thresholds'])
    ps=primes_to(maxb*118)
    counts=dict(constant_checks=0,denominator_6_7_checks=0,
                passed_denominator_thresholds=0,first_failed_thresholds=0,
                row_divisor_checks=0,local_exact_carry_checks=0,
                projection_dominance_checks=0,cofactor_projection_checks=0)
    rough={(r['i'],r['b']):r for r in cert['denominator_6_7_checks']}
    for row in cert['rows']:
        i=row['i'];pi=sum(p<i for p in ps)
        f=factorial(i)//(1 if i in ps else i)
        assert (pi,f)==(row['pi'],int(row['factorial_constant']))
        eta8=i-pi-(i+7)//8
        assert eta8==row['eta8'] and 3*eta8>=i-1
        assert 2**i*f<=2048**eta8
        counts['constant_checks']+=2
        maxrowb=max(t['first_failed_b'] for t in row['thresholds'])
        # Independent of the generator's prime-power event array:
        # build each lcm part directly from maximal prime powers.
        lcms={}
        for b in range(6,maxrowb+1):
            H=b*(i-1);L=1
            for p in ps:
                if p>H:
                    break
                if p<i:
                    continue
                q=p
                while q*p<=H:
                    q*=p
                L*=q
            lcms[b]=L
            if b in (6,7):
                eta=i-pi-(i+b-1)//b
                assert int(rough[(i,b)]['large_lcm'])==L
                assert 10**(11*eta)>2**i*f*L
                counts['denominator_6_7_checks']+=1
        for t in row['thresholds']:
            N=10**t['n_power'];C=101**(pi-1) if t['uses_a100'] else 1
            left=C*(N-i+1)**i
            for b in range(6,t['B']+1):
                e=(i+b-1)//b
                assert left>f*N**(pi+e)*lcms[b],(i,t,b)
                counts['passed_denominator_thresholds']+=1
            b=t['first_failed_b'];e=(i+b-1)//b
            assert b==t['B']+1
            assert left<=f*N**(pi+e)*lcms[b]
            assert int(t['failed_large_lcm'])==lcms[b]
            counts['first_failed_thresholds']+=1
    small_ps=[p for p in ps if p<=1000]
    tuples=[]
    for n in range(8,81):
        for i in range(3,min(12,n//2)):
            for j in range(i+1,n//2+1):
                tuples.append((i,n,j))
    rng=random.Random(699120)
    for _ in range(300):
        n=rng.randrange(242,1001);i=rng.randrange(3,120)
        j=rng.randrange(i+1,n//2+1)
        tuples.append((i,n,j))
    examples=[]
    for i,n,j in tuples:
        result=row_common_divisor(i,n,j)
        Q=int(result['large_part']);W=int(result['common_divisor'])
        A=comb(n,i);B=comb(n,j)
        assert gcd(A,B)%W==0
        assert prod(int(r['large_row_part']) for r in result['rows'])==Q
        counts['row_divisor_checks']+=1
        for s in range(i):
            for p,E in factor(n-s,small_ps).items():
                if p<i:
                    continue
                v=E-(p==i)
                if v<=0:
                    continue
                assert vp(W,p)==carry_count(n,j,p,v)
                counts['local_exact_carry_checks']+=1
                if carry_count(n,j,p)==0:
                    q=p**E;a=(n-s)//q;t,u=divmod(j,q)
                    assert 1<=t and 2*t<=a and u<=s
                    g=gcd(t,a);alpha=t//g;b=a//g
                    delta=b*j-alpha*n
                    assert 2<=b<=a
                    assert delta==b*u-alpha*s
                    assert -alpha*(i-1)<=delta<=(b-alpha)*(i-1)
                    counts['cofactor_projection_checks']+=1
        for a,b in ((1,2),(1,3),(1,4),(1,5),(2,5)):
            old=old_global(Q,i,n,j,a,b)
            assert W%old==0
            counts['projection_dominance_checks']+=1
    # A global projection can lose useful factors; row information recovers them.
    for i,n,j in ((3,9,4),(3,15,4),(3,151,50)):
        r=row_common_divisor(i,n,j);Q=int(r['large_part']);W=int(r['common_divisor'])
        old=lcm(*(old_global(Q,i,n,j,a,b) for a,b in ((1,2),(1,3),(1,4),(1,5),(2,5))))
        examples.append(dict(i=i,n=n,j=j,five_projection_divisor=old,
            row_divisor=W,actual_gcd=gcd(comb(n,i),comb(n,j))))
    assert examples[0]['five_projection_divisor']<examples[0]['row_divisor']
    assert vp(examples[2]['row_divisor'],5)==0
    assert vp(examples[2]['actual_gcd'],5)>0
    # A whole composite row need not belong to one factor j-t.
    assert 15*14%35==0 and 15%35 and 14%35
    result=dict(status='PASS',counts=counts,examples=examples,
        limitations={'higher_layers_may_add_common_factors':True,
                     'composite_row_may_split_between_j_minus_t':True,
                     'no_proof_that_row_divisor_always_exceeds_one':True})
    (ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':
    main()
