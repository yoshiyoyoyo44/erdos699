"""Build the adaptive valuation certificate for i=97,101 and 121..204.

All proof comparisons use rigorous integer-scaled logarithm enclosures.
The independent replay is replay_interval_indices.py.
"""
from functools import lru_cache
from math import isqrt, prod
from pathlib import Path
import json
import time

from certify_large_indices import C, LOG2, log_interval, trial_primes

INDICES = [97, 101] + list(range(121, 205))
OUTPUT = 'interval_index_certificate.json'


def certify(i, primes):
    ps = [p for p in primes if p < i]
    assert i > 4*len(ps)
    const = (2*i*(i-1)*LOG2[0]
             -2*sum(k*log_interval(k)[1] for k in range(1, i+1))
             +4*i*(i-1)*(log_interval(C-1)[0]-log_interval(C)[1]))
    E = (C*i).bit_length()
    while const+(i-4*len(ps))*(i-1)*E*LOG2[0] <= 0:
        E += 1
    cap = 1 << E
    data = []
    for p in ps:
        q = p
        powers = []
        while q < cap:
            if i % q:
                powers.append((q, i % q))
            q *= p
        data.append((log_interval(p)[1], powers))
    stack = [(C*i, cap-1)]
    leaves = []
    tested = 0
    while stack:
        lo, hi = stack.pop()
        upper = 0
        for logp, powers in data:
            exponent = 0
            for q, r in powers:
                if q > hi:
                    break
                if lo % q < r or hi//q > lo//q:
                    exponent += 1
            upper += exponent*logp
        tested += 1
        margin = const+i*(i-1)*log_interval(lo)[0]-4*(i-1)*upper
        if margin > 0:
            leaves.append([lo, hi])
        else:
            assert lo < hi, ('unresolved singleton', i, lo)
            mid = (lo+hi)//2
            stack.extend([(mid+1, hi), (lo, mid)])
    return {'i': i, 'tail_power_of_2': E, 'tested_nodes': tested,
            'leaves': leaves}


def small_range_certificate():
    import numpy as np
    limit = 4021520
    sieve = np.ones((limit+1)//2, dtype=np.bool_)
    sieve[0] = False
    for p in range(3, isqrt(limit)+1, 2):
        if sieve[p//2]:
            sieve[p*p//2::p] = False
    ps = np.concatenate((np.array([2], dtype=np.int64),
                         2*np.flatnonzero(sieve)+1))
    gaps = [[int(a), int(b)] for a, b in zip(ps[:-1], ps[1:])
            if b-a > min(INDICES)]
    assert ps[-1] >= C*max(INDICES)-1
    exceptions = sorted({(i, n) for i in INDICES for a, b in gaps
                         for n in range(max(a+i, 2*i+2), min(b, C*i))})
    factor_primes = trial_primes(isqrt(limit))

    @lru_cache(None)
    def factor(m):
        original = m
        factors = []
        for p in factor_primes:
            if p*p > m:
                break
            e = 0
            while m % p == 0:
                m //= p
                e += 1
            if e:
                factors.append((p, e))
        if m > 1:
            factors.append((m, 1))
        assert prod(p**e for p, e in factors) == original
        return factors

    rows = []
    for i, n in exceptions:
        constraints = sorted(((p**e, r, p, e) for r in range(i)
                              for p, e in factor(n-r) if p > i), reverse=True)
        q, r, p, e = constraints[0]
        candidates = []
        for residue in range(r+1):
            first = residue + max(0, (i+1-residue+q-1)//q)*q
            candidates.extend(range(first, n//2+1, q))
        initial = len(candidates)
        used = []
        for modulus, rem, prime, exponent in constraints[1:]:
            kept = [j for j in candidates if j % modulus <= rem]
            if len(kept) < len(candidates):
                used.append({'p': prime, 'e': exponent, 'r': rem,
                             'eliminated': len(candidates)-len(kept)})
                candidates = kept
            if not candidates:
                break
        assert not candidates, (i, n, candidates[:20])
        rows.append({'i': i, 'n': n, 'anchor': {'p': p, 'e': e, 'r': r},
                     'initial_count': initial, 'constraints': used})
    return {'limit': limit, 'last_prime': int(ps[-1]), 'prime_count': len(ps),
            'maximum_gap': int(np.diff(ps).max()), 'long_gaps': gaps,
            'exceptions': rows}


def main():
    start = time.monotonic()
    ps = trial_primes(204)
    rows = []
    for i in INDICES:
        row = certify(i, ps)
        rows.append(row)
        print(i, 'E', row['tail_power_of_2'], 'leaves', len(row['leaves']),
              'seconds', round(time.monotonic()-start, 2), flush=True)
    small = small_range_certificate()
    result = {'schema': 1, 'indices': INDICES, 'C': C,
              'construction_log_bits': 100, 'rows': rows, 'small_range': small}
    Path(OUTPUT).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print('COMPLETE', len(rows), 'indices', sum(len(r['leaves']) for r in rows),
          'leaves', len(small['exceptions']), 'small pairs', flush=True)


if __name__ == '__main__':
    main()
