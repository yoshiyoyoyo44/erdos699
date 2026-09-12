"""Replay the finite i=3 proof certificates using only Python's standard library.

This independently enumerates CRT roots by coprime factor partitions, verifies
coverage of every odd M within the claimed analytic bound, and recursively
proves all primes by an elementary Lucas order criterion.
"""
import argparse
import json
from itertools import product
from math import gcd, prod
from pathlib import Path


def v3(n):
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    return e


def cube_root(n):
    lo, hi = 0, 1
    while hi**3 <= n:
        hi *= 2
    while hi-lo > 1:
        mid = (lo+hi)//2
        if mid**3 <= n:
            lo = mid
        else:
            hi = mid
    return lo


def replay(filename, primes_filename):
    data = json.loads(Path(filename).read_text(encoding='utf-8'))
    cert = json.loads(Path(primes_filename).read_text(encoding='utf-8'))
    proved = {2}

    def prove(p):
        assert isinstance(p, int) and p >= 2
        if p in proved:
            return
        entry = cert[str(p)]
        fs = entry['factors']
        assert len({q for q, _ in fs}) == len(fs)
        assert all(2 <= q < p and e > 0 for q, e in fs)
        assert prod(q**e for q, e in fs) == p-1
        ws = dict(entry['witnesses'])
        assert set(ws) == {q for q, _ in fs}
        for q, _ in fs:
            prove(q)
            a = ws[q]
            assert 1 < a < p
            assert pow(a, p-1, p) == 1
            assert gcd(pow(a, (p-1)//q, p)-1, p) == 1
        proved.add(p)

    records = {(r['u'], r['M']): r for r in data['certificates']}
    assert len(records) == len(data['certificates'])
    assert data['method'] in ('original M<2^u', 'new M^3<2^(u+1)')
    expected, total_candidates = set(), 0
    per_u = []
    for u in range(4, data['max_u']+1):
        a = 2**u
        bound = a-1 if data['method'].startswith('original') else cube_root(2*a-1)
        nrows, first_stage = 0, 0
        for M in range(1, bound+1, 2):
            expected.add((u, M))
            row = records[(u, M)]
            eps = int(v3(M) == 1)
            C, T = a*3**eps, M//3**eps
            n = C*T
            d1 = 3 if v3(n-1) == 1 else 1
            d2 = 3 if v3(n//2-1) == 1 else 1
            Q1, Q2 = (n-1)//d1, (n//2-1)//d2
            fs = row['Q1_factors']
            assert all(isinstance(e, int) and e >= 1 for _, e in fs)
            assert len({p for p, _ in fs}) == len(fs)
            assert prod(p**e for p, e in fs) == Q1
            assert gcd(Q1, C) == 1
            for p, _ in fs:
                prove(p)
            prime_powers = [p**e for p, e in fs]
            roots = set()
            for mask in product((False, True), repeat=len(prime_powers)):
                c = prod(q for q, take in zip(prime_powers, mask) if take)
                f = Q1//c
                # k=0 mod c, k=C mod f; c and f are coprime.
                r = 0 if f == 1 else c*((C*pow(c, -1, f)) % f)
                roots.add(r)
            assert len(roots) == 2**len(prime_powers)
            candidates = set()
            low = max(1, (4+T-1)//T)
            for r in roots:
                k = r + max(0, (low-r+Q1-1)//Q1)*Q1
                while k < C//2:
                    assert k*(C-k) % Q1 == 0
                    candidates.add(k)
                    k += Q1
            # No full valuation computation is needed: the second necessary
            # congruence alone excludes every candidate in these artifacts.
            assert all(k*(C//2-k)*(C-k) % Q2 != 0 for k in candidates)
            assert row['first_stage'] == len(candidates)
            assert row['second_stage'] == [] and row['survivors'] == []
            first_stage += len(candidates)
            nrows += 1
        total_candidates += first_stage
        per_u.append({'u': u, 'rows': nrows, 'CRT_candidates': first_stage})
    assert set(records) == expected
    result = {'file': filename, 'max_u': data['max_u'], 'rows': len(expected),
              'CRT_candidates': total_candidates, 'survivors': 0,
              'primes_recursively_verified': len(proved), 'per_u': per_u}
    print(json.dumps(result))
    return result


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('files', nargs='+')
    ap.add_argument('--primes', default='prime_certificates.json')
    args = ap.parse_args()
    results = [replay(f, args.primes) for f in args.files]
    Path('verification_summary.json').write_text(json.dumps(results, indent=2), encoding='utf-8')
