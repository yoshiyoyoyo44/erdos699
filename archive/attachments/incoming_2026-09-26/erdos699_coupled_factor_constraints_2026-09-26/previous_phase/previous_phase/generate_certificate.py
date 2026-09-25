#!/usr/bin/env python3
"""Exact, integer-only denominator and prime-power cofactor certificates."""
from math import factorial, isqrt
from pathlib import Path
import json
import sys

if hasattr(sys, 'set_int_max_str_digits'):
    sys.set_int_max_str_digits(0)

ROOT = Path(__file__).resolve().parent
EXPONENTS = (11, 20, 50, 87, 100)
MAX_B = 500

def prime_power_events(cap):
    sieve = bytearray(b'\1') * (cap + 1)
    sieve[:2] = b'\0\0'
    for p in range(2, isqrt(cap) + 1):
        if sieve[p]:
            sieve[p*p:cap+1:p] = b'\0' * ((cap-p*p)//p+1)
    primes = [p for p in range(2, cap+1) if sieve[p]]
    events = [0] * (cap+1)
    for p in primes:
        q = p
        while q <= cap:
            events[q] = p
            q *= p
    return primes, events

def main():
    ps, events = prime_power_events(MAX_B * 118)
    records = []
    rough_checks = []
    for i in range(3, 120):
        pi = sum(p < i for p in ps)
        f = factorial(i) // (1 if i in ps else i)
        eta8 = i-pi-(i+7)//8
        assert 3*eta8 >= i-1
        assert 2**i*f <= 2048**eta8
        caps = {}
        answers = {}
        for d in EXPONENTS:
            N = 10**d
            for enhanced in (False, True):
                key = (d, enhanced)
                C = 101**(pi-1) if enhanced else 1
                # L <= cap is exactly C*(N-i+1)^i > f*N^(pi+e)*L.
                caps[key] = {
                    e: (C*(N-i+1)**i - 1)//(f*N**(pi+e))
                    for e in range(1, (i+5)//6+1)
                }
        L = 1
        cursor = 0
        for b in range(1, MAX_B+1):
            H = b*(i-1)
            for x in range(cursor+1, H+1):
                if events[x] >= i:
                    L *= events[x]
            cursor = H
            if b < 6:
                continue
            e = (i+b-1)//b
            eta = i-pi-e
            assert eta > 0
            if b in (6, 7):
                assert (10**11)**eta > 2**i*f*L
                rough_checks.append(dict(i=i,b=b,eta=eta,large_lcm=str(L)))
            for key in caps:
                if key in answers:
                    continue
                if L > caps[key][e]:
                    answers[key] = dict(B=b-1,first_failed_b=b,
                        failed_resonant_bound=e,failed_large_lcm=str(L))
            if len(answers) == len(caps):
                break
        assert len(answers) == len(caps), (i, 'MAX_B too small')
        records.append(dict(i=i,pi=pi,factorial_constant=str(f),eta8=eta8,
            thresholds=[dict(n_power=d,uses_a100=en,**answers[(d,en)])
                        for d in EXPONENTS for en in (False,True)]))
    obj = dict(i_range=[3,119],n_powers=list(EXPONENTS),
        common_independent_cutoff=10**11,logarithmic_bound=dict(multiplier=2048,base=64),
        denominator_6_7_checks=rough_checks,rows=records)
    (ROOT/'certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
    summary=[]
    for d in EXPONENTS:
        for en in (False,True):
            matches=[(t['B'],r['i']) for r in records for t in r['thresholds']
                     if t['n_power']==d and t['uses_a100']==en]
            lo=min(x[0] for x in matches)
            i119=next(t['B'] for r in records if r['i']==119 for t in r['thresholds']
                      if t['n_power']==d and t['uses_a100']==en)
            summary.append(dict(n_power=d,uses_a100=en,uniform_B=lo,
                bottleneck_indices=[i for B,i in matches if B==lo],i119_B=i119))
    (ROOT/'threshold_summary.json').write_text(json.dumps(summary,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__ == '__main__':
    main()
