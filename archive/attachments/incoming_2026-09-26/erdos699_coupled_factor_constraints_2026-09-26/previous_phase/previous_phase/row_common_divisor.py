#!/usr/bin/env python3
"""A certified common divisor using only C(n,i) and O(i) modular products.

No factorization of n or C(n,i), and no computation of C(n,j), is required.
This gives a lower bound on the common divisor, not necessarily its exact value.
"""
from math import comb, gcd, isqrt
import argparse
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

def primes_below(i):
    return [p for p in range(2,i) if all(p%d for d in range(2,isqrt(p)+1))]

def row_common_divisor(i,n,j):
    if not 3 <= i < j <= n//2:
        raise ValueError('Require 3 <= i < j <= n/2.')
    Q = comb(n,i)
    for p in primes_below(i):
        while Q%p == 0:
            Q //= p
    W = 1
    falling = 1
    rows = []
    for s in range(i):
        q = gcd(Q,n-s)
        falling = falling*(j-s)%Q
        covered = gcd(q,falling)
        w = q//covered
        W *= w
        rows.append(dict(s=s,large_row_part=str(q),covered=str(covered),
                         common_divisor=str(w)))
    return dict(i=i,n=str(n),j=str(j),large_part=str(Q),common_divisor=str(W),
                certified_common_prime_exists=W>1,
                status='CERTIFIED' if W>1 else 'INCONCLUSIVE',rows=rows)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('i','n','j'):
        parser.add_argument(name,type=int)
    args = parser.parse_args()
    print(json.dumps(row_common_divisor(args.i,args.n,args.j),indent=2))
