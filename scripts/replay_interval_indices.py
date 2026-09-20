"""Independent standard-library replay of interval_index_certificate.json.

Does not import the generator or the earlier logarithm implementation.
Uses 144-bit outward-rounded fixed-point logarithms and a complete bytearray
sieve. All valuation bounds, coverage and residue exclusions are recomputed.
"""
from repo_paths import artifact_path
from functools import lru_cache
from math import comb, isqrt
from pathlib import Path
import json

BITS = 144
SCALE = 1 << BITS
TERMS = 64
C = 16598
INDICES = [97, 101] + list(range(121, 205))


def ceildiv(a, b):
    return -((-a)//b)


def atanh_log(a, b):
    assert b <= a <= 2*b
    # t=(a-b)/(a+b); 0 <= t <= 1/3.
    low = SCALE*(a-b)//(a+b)
    high = ceildiv(SCALE*(a-b), a+b)
    square_low = low*low//SCALE
    square_high = ceildiv(high*high, SCALE)
    power_low, power_high = low, high
    result_low = result_high = 0
    for k in range(TERMS):
        result_low += 2*(power_low//(2*k+1))
        result_high += 2*ceildiv(power_high, 2*k+1)
        power_low = power_low*square_low//SCALE
        power_high = ceildiv(power_high*square_high, SCALE)
    # Analytic tail <= (9/4)*3^(-129)/129 < 1/SCALE.
    assert 9*SCALE < 4*(2*TERMS+1)*3**(2*TERMS+1)
    return result_low, result_high+1


LOG2 = atanh_log(2, 1)


@lru_cache(None)
def log_bounds(n):
    assert isinstance(n, int) and n > 0
    exponent = n.bit_length()-1
    low, high = atanh_log(n, 1 << exponent)
    return low+exponent*LOG2[0], high+exponent*LOG2[1]


def prime(p):
    return p >= 2 and all(p % d for d in range(2, isqrt(p)+1))


def possible_carry(lo, hi, q, r):
    # [lo,hi] meets [k*q,k*q+r-1] for some integer k.
    return r > 0 and ceildiv(lo-r+1, q) <= hi//q


def formula_checks():
    count = 0
    for n in range(2, 201):
        for i in range(1, n+1):
            binomial = comb(n, i)
            for p in (2, 3, 5, 7, 11):
                actual, remainder = 0, binomial
                while remainder % p == 0:
                    actual += 1
                    remainder //= p
                q, expected = p, 0
                while q <= n:
                    expected += int(n % q < i % q)
                    q *= p
                assert actual == expected
                count += 1
    intersections = 0
    for q in range(2, 30):
        for r in range(q):
            for lo in range(2*q):
                for width in (0, 1, q//2, q, 2*q):
                    hi = lo+width
                    assert possible_carry(lo, hi, q, r) == any(
                        n % q < r for n in range(lo, hi+1))
                    intersections += 1
    return count, intersections


def replay_intervals(cert):
    ps = [p for p in range(2, 205) if prime(p)]
    assert [row['i'] for row in cert['rows']] == INDICES
    total = 0
    minimum_margin = None
    for row in cert['rows']:
        i, E = row['i'], row['tail_power_of_2']
        primes = [p for p in ps if p < i]
        assert i > 4*len(primes)
        cap = 1 << E
        assert cap >= C*i
        const = (2*i*(i-1)*LOG2[0]
                 -2*sum(k*log_bounds(k)[1] for k in range(1, i+1))
                 +4*i*(i-1)*(log_bounds(C-1)[0]-log_bounds(C)[1]))
        assert const+(i-4*len(primes))*(i-1)*E*LOG2[0] > 0
        data = []
        for p in primes:
            powers = []
            q = p
            while q < cap:
                powers.append((q, i % q))
                q *= p
            data.append((log_bounds(p)[1], powers))
        expected_lo = C*i
        for lo, hi in row['leaves']:
            assert lo == expected_lo and lo <= hi < cap
            expected_lo = hi+1
            upper = 0
            for logp, powers in data:
                exponent = 0
                for q, r in powers:
                    if q > hi:
                        break
                    exponent += int(possible_carry(lo, hi, q, r))
                upper += exponent*logp
            margin = const+i*(i-1)*log_bounds(lo)[0]-4*(i-1)*upper
            assert margin > 0, (i, lo, hi)
            # This is a lower bound for log(f_i(lo)/U_i([lo,hi])).
            scaled_margin = margin//(4*(i-1))
            minimum_margin = (scaled_margin if minimum_margin is None else
                              min(minimum_margin, scaled_margin))
            total += 1
        assert expected_lo == cap
        assert row['tested_nodes'] == 2*len(row['leaves'])-1
    return total, str(minimum_margin)+'/'+str(SCALE)


def replay_small(cert):
    data = cert['small_range']
    N = data['limit']
    assert N == 4021520
    # A different indexing convention: one byte for every integer.
    sieve = bytearray(b'\x01')*(N+1)
    sieve[0:2] = b'\x00\x00'
    for p in range(2, isqrt(N)+1):
        if sieve[p]:
            first = p*p
            sieve[first:N+1:p] = b'\x00'*((N-first)//p+1)
    previous, count, maximum = 2, 1, 0
    gaps = []
    for p in range(3, N+1):
        if sieve[p]:
            gap = p-previous
            maximum = max(maximum, gap)
            if gap > min(INDICES):
                gaps.append([previous, p])
            previous = p
            count += 1
    assert previous >= C*max(INDICES)-1
    assert (previous, count, maximum, gaps) == (
        data['last_prime'], data['prime_count'], data['maximum_gap'], data['long_gaps'])
    required = set()
    for left, right in gaps:
        for i in INDICES:
            for n in range(left+i, right):
                if 2*i+2 <= n < C*i:
                    required.add((i, n))
    assert [(r['i'], r['n']) for r in data['exceptions']] == sorted(required)

    def constraint(c, i, n):
        p, e, r = c['p'], c['e'], c['r']
        assert prime(p) and p > i and e >= 1 and 0 <= r < i
        q = p**e
        assert n % q == r
        return q, r

    max_candidates = 0
    for row in data['exceptions']:
        i, n = row['i'], row['n']
        q, r = constraint(row['anchor'], i, n)
        candidates = []
        for k in range((i+1)//q, n//(2*q)+1):
            candidates.extend(range(max(i+1, k*q), min(n//2, k*q+r)+1))
        assert len(candidates) == row['initial_count']
        max_candidates = max(max_candidates, len(candidates))
        for c in row['constraints']:
            modulus, rem = constraint(c, i, n)
            kept = [j for j in candidates if j % modulus <= rem]
            assert c['eliminated'] == len(candidates)-len(kept)
            candidates = kept
        assert not candidates
    return len(required), max_candidates


def main():
    cert = json.loads(artifact_path('interval_index_certificate.json').read_text(encoding='utf-8'))
    assert cert['schema'] == 1 and cert['indices'] == INDICES and cert['C'] == C
    valuation_tests, intersection_tests = formula_checks()
    leaves, margin = replay_intervals(cert)
    small_pairs, max_candidates = replay_small(cert)
    result = {'status': 'verified', 'new_indices': INDICES,
              'new_index_count': len(INDICES), 'verified_interval_leaves': leaves,
              'independent_log_bits': BITS, 'minimum_log_margin_lower': margin,
              'small_range_pairs_eliminated': small_pairs,
              'largest_anchor_candidate_count': max_candidates,
              'binomial_valuation_checks': valuation_tests,
              'interval_intersection_checks': intersection_tests,
              'combined_with_previous_result_all_i_at_least': 121,
              'additional_isolated_indices': [97, 101],
              'uses_external_prime_gap_estimate_for_new_indices': False,
              'previous_all_i_at_least_205_uses_external_prime_estimates': True,
              'complete_solution': False, 'magma_dependency_for_new_result': False}
    artifact_path('verification_interval_indices.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
