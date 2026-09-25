#!/usr/bin/env python3
"""Find a certified common divisor supported on primes >= i.

Does not compute C(n,j) and does not factor n or C(n,i).
Usage: python common_divisor.py i n j
The underlying theorem is proved in REPORT.md.
"""
from math import comb,gcd,lcm,isqrt
import argparse,json,sys

if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SLOPES=((1,2),(1,3),(1,4),(1,5),(2,5))

def primes_below(i):
    return [p for p in range(2,i) if all(p%d for d in range(2,isqrt(p)+1))]

def fact_v(n,p):
    v=0
    while n:n//=p;v+=n
    return v

def find_common_divisor(i,n,j):
    if not 3<=i<j<=n//2:raise ValueError('Require 3 <= i < j <= n/2.')
    A=comb(n,i);small=1
    for p in primes_below(i):
        e=fact_v(n,p)-fact_v(i,p)-fact_v(n-i,p)
        small*=p**e
    Q=A//small
    out=[];combined=1
    for a,b in SLOPES:
        delta=b*j-a*n;image=set();res=set()
        for s in range(i):
            for t in range(s+1):
                c=b*t-a*s;image.add(c)
                if c==delta:res.add(s)
        covered=1
        # Each gcd and each partial lcm divides Q, so no enormous uncapped
        # product of linear forms needs to be constructed.
        for c in image:
            if c!=delta:covered=lcm(covered,gcd(Q,abs(delta-c)))
        for s in res:covered=lcm(covered,gcd(Q,n-s))
        W=Q//covered
        combined=lcm(combined,W)
        out.append(dict(a=a,b=b,delta=str(delta),resonant_rows=sorted(res),common_divisor=str(W)))
    return dict(i=i,n=str(n),j=str(j),large_part=str(Q),
        common_divisor=str(combined),certified_common_prime_exists=combined>1,
        status='CERTIFIED' if combined>1 else 'INCONCLUSIVE',slopes=out,
        theorem='The returned common_divisor divides gcd(C(n,i),C(n,j)); every prime factor is >= i.')

if __name__=='__main__':
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('i',type=int);p.add_argument('n',type=int);p.add_argument('j',type=int)
    x=p.parse_args()
    print(json.dumps(find_common_divisor(x.i,x.n,x.j),indent=2))
