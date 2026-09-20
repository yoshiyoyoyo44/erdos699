"""Exact necessary-condition sieve for Erdős 699 at i=3.

This is finite verification, not a proof for unbounded u.
Requires SymPy. Every factorization is checked by multiplication and isprime;
all primality inputs are < 2**64 (SymPy's deterministic range).
"""
from repo_paths import artifact_path
import argparse
import json
from math import prod
from pathlib import Path
from time import perf_counter
from sympy import factorint, isprime, integer_nthroot


def valuation(n, p):
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def binomial_valuation(n, k, p):
    total, q = 0, p
    while q <= n:
        total += n // q - k // q - (n-k) // q
        q *= p
    return total


def certified_factors(n):
    assert 0 < n < 2**64
    fs = [(int(p), int(e)) for p, e in sorted(factorint(n).items())]
    assert prod(p**e for p, e in fs) == n
    assert all(e > 0 and p < 2**64 and isprime(p) for p, e in fs)
    return fs


def roots_zero_or_C(C, fs):
    """All roots of x(C-x)=0 modulo Q; gcd(C,Q)=1 is checked."""
    roots, modulus = [0], 1
    for p, e in fs:
        q = p**e
        assert C % p != 0
        inv = pow(modulus, -1, q)
        roots = [r + modulus*((target-r)*inv % q)
                 for r in roots for target in (0, C % q)]
        modulus *= q
    assert len(roots) == len(set(roots))
    assert all(0 <= r < modulus and r*(C-r) % modulus == 0 for r in roots)
    return roots, modulus


def scan_row(u, M, certificates):
    a = 2**u
    eps = int(valuation(M, 3) == 1)
    T, C = M // 3**eps, a*3**eps
    n = C*T
    N1, N2 = n-1, n//2-1
    d1 = 3 if valuation(N1, 3) == 1 else 1
    d2 = 3 if valuation(N2, 3) == 1 else 1
    Q1, Q2 = N1//d1, N2//d2
    fs = certified_factors(Q1)
    roots, modulus = roots_zero_or_C(C, fs)
    assert modulus == Q1
    candidates = []
    for r in roots:
        low = max(1, (4+T-1)//T)
        first = r + max(0, (low-r+Q1-1)//Q1)*Q1
        candidates.extend(range(first, C//2, Q1))
    survivors = []
    second_stage = []
    for k in candidates:
        if k*(C//2-k)*(C-k) % Q2:
            continue
        second_stage.append(k)
        j = k*T
        ps = set()
        for v in (n, n-1, n-2):
            ps.update(p for p, _ in certified_factors(v) if p != 2)
        witnesses = [p for p in sorted(ps)
                     if binomial_valuation(n, 3, p) > 0
                     and binomial_valuation(n, j, p) > 0]
        if not witnesses:
            survivors.append((n, 3, j))
    certificates.append({'u': u, 'M': M, 'Q1_factors': fs,
                         'first_stage': len(candidates),
                         'second_stage': second_stage,
                         'survivors': survivors})
    return len(candidates), len(second_stage), survivors


def run(max_u, original, output):
    start = perf_counter()
    rows, certificates = [], []
    for u in range(4, max_u+1):
        a = 2**u
        # Original n reduction gives M<a. New theorem gives M^3<2a.
        bound = a-1 if original else int(integer_nthroot(2*a-1, 3)[0])
        totals = {'u': u, 'M_bound': bound, 'rows': 0,
                  'first_stage': 0, 'second_stage': 0, 'survivors': []}
        for M in range(1, bound+1, 2):
            first, second, survivors = scan_row(u, M, certificates)
            totals['rows'] += 1
            totals['first_stage'] += first
            totals['second_stage'] += second
            totals['survivors'].extend(survivors)
        rows.append(totals)
        print(json.dumps(totals), flush=True)
        artifact_path(output).write_text(json.dumps({
            'method': 'original M<2^u' if original else 'new M^3<2^(u+1)',
            'max_u': u, 'rows': rows, 'certificates': certificates,
            'elapsed_seconds': perf_counter()-start}, indent=2), encoding='utf-8')
    assert not any(row['survivors'] for row in rows), 'Surviving candidate needs review'


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--max-u', type=int, default=32)
    ap.add_argument('--original', action='store_true')
    ap.add_argument('--output', default='i3_sieve.json')
    args = ap.parse_args()
    run(args.max_u, args.original, args.output)
