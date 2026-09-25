#!/usr/bin/env python3
"""Independent standard-library checker. Does not import the generator."""
from pathlib import Path
from math import comb, factorial, gcd, lcm, prod, isqrt
from fractions import Fraction
from itertools import product
from collections import Counter
from random import Random
import json

ROOT=Path(__file__).resolve().parent
SLOPES=((1,2),(1,3),(1,4),(1,5),(2,5))
counts=Counter()

def trial_primes(limit):
    return [p for p in range(2,limit+1) if all(p%q for q in range(2,isqrt(p)+1))]

PRIMES=trial_primes(700)

def vp(x,p):
    assert x!=0
    x=abs(x);v=0
    while x%p==0:x//=p;v+=1
    return v

def small_part(value,i):
    out=1
    for p in PRIMES:
        if p>=i:break
        while value%p==0:value//=p;out*=p
    return out

def form_data(i,a,b):
    # Build the image of the actual triangular lattice. The generator used
    # modular tests instead; here resonance is reconstructed from this map.
    fibers={}
    for s in range(i):
        for t in range(s+1):fibers.setdefault(b*t-a*s,set()).add(s)
    return fibers

def verify_certificate():
    cert=json.loads((ROOT/'certificate.json').read_text())
    assert cert['i_range']==[3,119]
    assert cert['unresolved']==[i for i in range(3,120) if i not in (96,97,100,101)]
    assert len(cert['unresolved'])==113
    assert [r['i'] for r in cert['rows']]==list(range(3,120))
    # Build lcm(1,...,cap) without prime-factor formulas.
    lc=[1]
    for k in range(1,591):lc.append(lcm(lc[-1],k))
    exceptions=[]
    for row in cert['rows']:
        i=row['i'];pi=sum(p<i for p in PRIMES)
        small_i=small_part(i,i);F=factorial(i)//small_i
        assert row['pi']==pi and int(row['factorial_constant'])==F
        assert [(s['a'],s['b']) for s in row['slopes']]==list(SLOPES)
        lparts=[z//small_part(z,i) for z in lc]
        for sr in row['slopes']:
            a,b=sr['a'],sr['b'];lo=-a*(i-1);hi=(b-a)*(i-1)
            m=hi-lo+1
            assert sr['degree']==m
            alpha=Fraction(i-pi,m)
            assert alpha>=Fraction(4,7*b+1)
            assert 10**m>2**i*F
            N=200000000
            assert 4**m*101**(pi-1)*(N-i+1)**i>F*N**i
            counts['uniform_exponent_checks']+=1
            counts['uniform_constant_checks']+=2
            fibers=form_data(i,a,b)
            expected=[]
            supplied={r['delta']:r for r in sr['rows']}
            assert len(supplied)==len(sr['rows'])
            for delta in range(lo,hi+1):
                e=len(fibers.get(delta,set()));gain=i-pi-e
                if gain<=0:
                    exceptions.append([i,a,b,delta]);continue
                expected.append(delta)
                r=supplied[delta];cap=max(delta-lo,hi-delta);L=lparts[cap]
                assert r['resonant_count']==e and int(r['large_lcm'])==L
                assert gain>=1
                for N,cofactor in [(10**11,1),(200000000,101**(pi-1))]:
                    left=cofactor*(N-i+1)**i
                    right=F*N**(pi+e)*L
                    assert left>right,(i,a,b,delta,N)
                    counts['finite_threshold_comparisons']+=1
                counts['finite_offset_cells']+=1
            assert sorted(supplied)==expected
    assert exceptions==cert['exceptions']
    expected_exceptions=[[i,1,2,0] for i in range(3,10)]
    expected_exceptions += [[i,1,2,d] for i in (4,6,8) for d in (-1,1)]
    expected_exceptions += [[4,1,3,0]]
    assert sorted(exceptions)==sorted(expected_exceptions)
    counts['analytic_exception_cells']=len(exceptions)
    assert counts['finite_threshold_comparisons']==cert['integer_threshold_comparisons']

def verify_small_support_cases():
    sizes={3:1,4:2,5:2,6:3,7:3,8:4,9:4}
    for i,m in sizes.items():
        ps=[p for p in PRIMES if 2<p<=i]
        subsets=[tuple(p for z,p in enumerate(ps) if mask>>z&1) for mask in range(1,1<<len(ps))]
        possible=[]
        for pattern in product(subsets,repeat=m):
            counts['small_support_assignments']+=1
            # Each odd term is >i; at a prime threshold, that prime can
            # appear only once and therefore cannot be the term's only prime.
            if i in PRIMES and any(part==(i,) for part in pattern):continue
            if any((v-u)%p for u in range(m) for v in range(u+1,m) for p in set(pattern[u])&set(pattern[v])):continue
            possible.append(pattern)
        if i<=7:assert not possible
        else:
            assert set(possible)=={((3,),(5,),(7,),(3,)),((3,),(7,),(5,),(3,))}
            # Paper proof: the two endpoint powers of 3 differ by 6,
            # forcing them to be 3 and 9, impossible when all terms exceed i.
            assert 3**2-3==6
        counts['small_support_cases']+=1
    # The additional i=4, slope 1/3, delta=0 exception reduces to two
    # consecutive 3-smooth integers. Its general mod-8/factorization proof
    # is in the report. This list is a finite arithmetic diagnostic only.
    smooth=sorted({2**a*3**b for a in range(20) for b in range(20)})
    pairs=[(x,x+1) for x in smooth if x+1 in set(smooth)]
    assert pairs==[(1,2),(2,3),(3,4),(8,9)]
    counts['smooth_pair_diagnostic_pairs']=len(pairs)

def large_avoided_factors(n,i,j):
    A=comb(n,i);B=comb(n,j);factors=[]
    for p in PRIMES:
        if p<i:continue
        if p>n:break
        if A%p==0 and B%p:
            v=vp(A,p);q=p**v;s=n%q;t=j%q
            assert 0<=t<=s<i
            full_q=p**(v+int(p==i))
            assert n%full_q==s and j%full_q==t
            assert sum((n-r)%p==0 for r in range(i))==1
            counts['local_prime_power_transfers']+=1
            if p==i:counts['prime_equals_i_transfers']+=1
            factors.append((p,q,s,t))
    return A,B,factors

def check_tuple(n,i,j):
    A,B,factors=large_avoided_factors(n,i,j)
    pi=sum(p<i for p in PRIMES)
    assert small_part(A,i)*small_part(i,i)<=n**pi
    counts['binomial_tuples']+=1
    if factors:counts['nonvacuous_binomial_tuples']+=1
    Q=prod(q for p,q,s,t in factors)
    Qall=A//small_part(A,i);combined=1
    for a,b in SLOPES:
        delta=b*j-a*n;fibers=form_data(i,a,b)
        res=fibers.get(delta,set())
        nonzero=[abs(delta-c) for c in fibers if c!=delta]
        L=lcm(*nonzero)
        Qnon=prod(q for p,q,s,t in factors if s not in res)
        assert L%Qnon==0
        union=lcm(L,*(n-s for s in res))
        assert union%Q==0
        W=Qall//gcd(Qall,union)
        assert A%W==0 and B%W==0
        combined=lcm(combined,W)
        counts['unconditional_common_divisor_checks']+=1
        if W>1:counts['nontrivial_common_divisors']+=1
        counts['rational_form_divisibility_checks']+=1
        # Also test the deliberately larger interval hull used in estimates.
        lo=-a*(i-1);hi=(b-a)*(i-1)
        if delta<lo or delta>hi:
            product_value=prod(abs(delta-c) for c in range(lo,hi+1))
            m=hi-lo+1
            twice_center=abs(2*delta-lo-hi)
            assert 2**m*product_value<twice_center**m
            counts['centered_product_checks']+=1
    assert gcd(A,B)%combined==0

def finite_probes():
    for n in range(8,101):
        for i in range(3,min(13,n//2)):
            for j in range(i+1,n//2+1):check_tuple(n,i,j)
    rng=Random(69920260925)
    for _ in range(1000):
        n=rng.randrange(242,701);i=rng.randrange(3,min(120,n//2));j=rng.randrange(i+1,n//2+1)
        check_tuple(n,i,j)
    # A prime equal to i loses one valuation in i!, which is explicitly
    # tested rather than treating every p>=i as a denominator-free prime.
    for p in [3,5,7,11,13]:
        n=(4 if p==3 else 3)*p*p+1;i=p;j=p*p
        check_tuple(n,i,j)
    # One local layer is not the whole Kummer condition.
    n,i,j,p=151,3,50,5
    assert vp(comb(n,i),p)==2
    assert j%25<=n%25
    assert j%125>n%125 and comb(n,j)%p==0
    counts['insufficient_layer_counterexamples']=1

if __name__=='__main__':
    verify_certificate()
    verify_small_support_cases()
    finite_probes()
    result=dict(status='PASS',counts=dict(counts),
        independent_claim='All 3<=i<=119, n>=10^11: five rational neighborhoods excluded with constant 1/10.',
        inherited_claim='With the repository A=100 near-collision theorem, n>=2*10^8 and constant 1/4.',
        inherited_source_commit='f5a28d1037f35fdccc7a014e958db6fd666d220b',
        limits='A=100 baseline certificate not replayed here. Infinite arguments and exceptional smooth-number classifications are proved in REPORT.md; finite probes alone do not prove them. No global resolution of any remaining i is claimed.')
    (ROOT/'verification.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))
