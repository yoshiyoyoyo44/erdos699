"""Rational-interval certificates for all large indices.

No floating-point comparisons are used. See discriminant_continuation.md.
The prime-gap and residue verification is implemented separately.
"""
from fractions import Fraction as Q
from functools import lru_cache
from math import isqrt
import argparse
import heapq
import json

SCALE = 1 << 100
TERMS = 40
C = 16598

def series_interval(a, b):
    """Enclose log(a/b), for 1 <= a/b <= 2, in units 1/SCALE."""
    assert b <= a <= 2*b
    t = Q(a-b, a+b)
    total = sum((t**(2*k+1)/Q(2*k+1) for k in range(TERMS)), Q(0))*2
    tail = 2*t**(2*TERMS+1)/(Q(2*TERMS+1)*(1-t*t))
    lower, upper = SCALE*total, SCALE*(total+tail)
    return lower.numerator//lower.denominator, -((-upper.numerator)//upper.denominator)

LOG2 = series_interval(2, 1)

@lru_cache(None)
def log_interval(n):
    assert isinstance(n,int) and n>=1
    e = n.bit_length()-1
    lo, hi = series_interval(n,1<<e)
    return lo+e*LOG2[0], hi+e*LOG2[1]

def trial_primes(bound):
    return [p for p in range(2,bound+1)
            if all(p%d for d in range(2,isqrt(p)+1))]

def prove_analytic_tail():
    """Strict rational margins for all i >= 900, at n=C*i and beyond."""
    I=900
    ci_lo, ci_hi = log_interval(C)
    i_lo, i_hi = log_interval(I)
    lhs = (Q(ci_lo,4*SCALE)+Q(LOG2[0],2*SCALE)+Q(1,8)
           -Q(3*i_hi,4*(I-1)*SCALE)-Q(1,C-1))
    rhs = (1+Q(ci_hi,i_lo))*(1+Q(6381*SCALE,5000*i_lo))
    slope = Q(SCALE,i_lo)*(1+Q(6381*SCALE,5000*i_lo))
    assert lhs>rhs and slope<Q(1,4)
    return {'threshold':I,'margin_lower':str(lhs-rhs),
            'slope_upper':str(slope)}

def certify_index(i, primes):
    ps=[p for p in primes if p<i]
    r=len(ps)
    assert i>4*r
    # 4(i-1)*log(F_i(n)/U_i(n)), where the correction factor
    # is replaced by the smaller constant ((C-1)/C)^i.
    constant_lo=(2*i*(i-1)*LOG2[0]
        -2*sum(k*log_interval(k)[1] for k in range(1,i+1))
        +4*i*(i-1)*(log_interval(C-1)[0]-log_interval(C)[1]))
    slope=i*(i-1)
    smooth_slope=4*(i-1)
    tail_slope=(i-4*r)*(i-1)
    E=0
    while constant_lo+tail_slope*E*LOG2[0]<=0 or (1<<E)<C*i:
        E+=1
    cap=1<<E
    queue=[]
    logU_hi=0
    for p in ps:
        power=p
        e=1
        while power*p<=C*i:
            power*=p
            e+=1
        logU_hi+=e*log_interval(p)[1]
        heapq.heappush(queue,(power*p,p,e+1))
    start=C*i
    logstart_lo=log_interval(start)[0]
    bad=[]
    checked=0
    while start<cap:
        nxt,p,e=queue[0]
        end=min(nxt,cap)-1
        margin=constant_lo+slope*logstart_lo-smooth_slope*logU_hi
        checked+=1
        if margin<=0:
            bad.append([start,end])
        if nxt>=cap:
            break
        heapq.heappop(queue)
        logU_hi+=log_interval(p)[1]
        heapq.heappush(queue,(nxt*p,p,e+1))
        start=nxt
        logstart_lo=e*log_interval(p)[0]
    return {'i':i,'prime_count':r,'tail_power_of_2':E,
            'tested_segments':checked,'danger_intervals':bad}

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--min-i',type=int,default=205)
    args=ap.parse_args()
    tail=prove_analytic_tail()
    primes=trial_primes(900)
    rows=[certify_index(i,primes) for i in range(args.min_i,900)]
    max_n=max(b for row in rows for a,b in row['danger_intervals'])
    output={'min_i':args.min_i,'C':C,'log_scale_bits':100,
            'log_series_terms':TERMS,'analytic_tail':tail,
            'maximum_danger_n':max_n,'rows':rows}
    with open('large_index_certificate.json','w',encoding='utf-8') as f:
        json.dump(output,f,indent=2)
        f.write('\n')
    print(json.dumps({'min_i':args.min_i,'max_danger_n':max_n,
        'indices':len(rows),'segments':sum(r['tested_segments'] for r in rows),
        'danger_intervals':sum(len(r['danger_intervals']) for r in rows),
        'analytic_tail':tail},indent=2),flush=True)

if __name__=='__main__':
    main()
