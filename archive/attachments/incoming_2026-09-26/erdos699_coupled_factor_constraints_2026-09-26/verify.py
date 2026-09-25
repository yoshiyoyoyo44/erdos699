#!/usr/bin/env python3
"""Independent exact checks; finite tests do not prove the infinite theorems."""
from fractions import Fraction
from itertools import combinations
from math import comb, gcd, isqrt, lcm, prod
from pathlib import Path
import hashlib
import json
import random
from factor_allocation import (row_data, determinant, minimum_slots, analyze)

ROOT = Path(__file__).resolve().parent


def factor(n):
    out = {}
    p = 2
    while p*p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0)+1
            n //= p
        p += 1
    if n > 1:
        out[n] = 1
    return out


def valuation(n, p):
    ans = 0
    while n and n % p == 0:
        n //= p
        ans += 1
    return ans


def main():
    stats = {}
    cert = json.loads((ROOT/'certificate.json').read_text())
    old = json.loads((ROOT/'previous_phase/certificate.json').read_text())
    assert len(cert['rows']) == 117
    const_checks = count_checks = 0
    for row, previous in zip(cert['rows'], old['rows']):
        i = row['i']
        assert i == previous['i']
        ps = [p for p in range(2, i) if factor(p) == {p: 1}]
        pi = len(ps)
        eps = i if factor(i) == {i:1} else 1
        L = 1
        for v in range(1, pi+1): L = L*v//gcd(L,v)
        C = eps*L
        assert (pi, eps, C) == (row['pi'], row['epsilon'], int(row['high_row_constant']))
        inherited = next(x for x in previous['cases']
                         if x['n_power'] == 87 and not x['uses_a100'])
        assert inherited['excluded_denominator_B'] >= i-1
        assert row['inherited_denominator_bound'] == inherited['excluded_denominator_B']
        assert 512**(pi+1) > 2*C*(i-1)**(pi+1)
        assert 10**550 > (512*C)**32
        assert pi+1 <= i-1 and pi+1 <= 31
        const_checks += 1
        for item in row['count_certificates']:
            n = 10**item['n_power']; k = item['prefix_last_row']
            lk = lcm(*range(1,k+1)); c = eps*lk
            assert str(c) == item['prefix_constant']
            # Direct stronger target, independent of generator's 4*h*C**2 test.
            assert (n-k)**2 > c*c*(i-1)*(n-i+1)
            assert n > 4*(i-1)*c*c
            if k < i-1:
                cn = eps*lcm(*range(1,k+2))
                assert n <= 4*(i-1)*cn*cn
            g = k+1-pi
            assert item['guaranteed_regular_rows'] == g
            assert item['distinct_large_prime_lower_bound'] == max(0,2*g-1)
            if item['n_power'] == 105: assert k == i-1
            count_checks += 1
    stats['independent_index_constant_checks'] = const_checks
    stats['prime_count_certificate_checks'] = count_checks
    e = cert['numerical_examples']; n = 10**200
    a = e['i119_high_rows_minimum_cofactor']; C = lcm(*range(1,31))
    assert C*(118*(a-1))**31 < n-30 <= C*(118*a)**31
    b = e['high_rows_uniform_minimum_cofactor']
    assert (512*(b-1))**31 <= n < (512*b)**31
    assert (a,b) == (9568,5526)

    # Exhaustive low-range checks of unconditional identities, including
    # candidate triples that fail the necessary counterexample conditions.
    triples = row_checks = active_pair_checks = 0
    prime_i_restorations = prime_i_exclusions = 0
    for n in range(10, 121):
        facts = {s:factor(n-s) for s in range(12) if n-s > 0}
        for i in range(3, min(12,n//2-1)+1):
            A = comb(n,i)
            for j in range(i+1, n//2+1):
                rows = row_data(n,i,j)
                all_cells = []
                for r in rows:
                    s = r['s']
                    rs = prod(p**ex for p,ex in facts[s].items()
                              if p >= i and A % p == 0)
                    assert rs == r['R_s']
                    qs = prod(p**valuation(A,p) for p in facts[s]
                              if p >= i and A % p == 0)
                    assert qs == r['Q_s']
                    assert prod(r['cells'])*r['uncovered'] == rs
                    if factor(i) == {i:1} and n % i == s % i:
                        E = facts[s].get(i,0)
                        if E >= 2:
                            assert rs == i*qs
                            prime_i_restorations += 1
                        elif E == 1:
                            assert rs % i != 0
                            prime_i_exclusions += 1
                    for u,b in enumerate(r['cells']):
                        if b > 1: all_cells.append((s,u,b))
                    row_checks += 1
                for (s,u,b),(r,v,c) in combinations(all_cells,2):
                    assert gcd(b,c) == 1
                    D = determinant(n,j,(s,u),(r,v))
                    # Independent 3x3 determinant expansion.
                    D2 = n*(u-v)-j*(s-r)+s*v-u*r
                    assert D == -D2
                    assert D % (b*c) == 0
                    assert abs(D) <= (i-1)*(n-i+1)
                    if D: assert b*c <= abs(D)
                    active_pair_checks += 1
                for u in range(i):
                    assert (j-u) % prod(r['cells'][u] for r in rows if r['s']>=u) == 0
                    assert (n-j-u) % prod(r['cells'][r['s']-u]
                                              for r in rows if r['s']>=u) == 0
                triples += 1
    stats.update(exhaustive_triples=triples, full_row_factor_checks=row_checks,
        active_pair_checks=active_pair_checks, prime_i_restorations=prime_i_restorations,
        prime_i_exclusions=prime_i_exclusions)

    # Structural tests on arbitrary grid points, not just existing prime blocks.
    rng = random.Random(699260926)
    geometric = zero_cases = 0
    for _ in range(12000):
        i = rng.randrange(3,120); h=i-1
        n = rng.randrange(max(h*h+h+1,2*i+2),10**8)
        j = rng.randrange(i+1,n//2+1)
        s = rng.randrange(i);u=rng.randrange(s+1)
        r = rng.randrange(i);v=rng.randrange(r+1)
        D = determinant(n,j,(s,u),(r,v))
        assert abs(D) <= h*(n-h)
        geometric += 1
    # Deliberately build zero determinants with reduced denominator <=i-1.
    for i in range(3,40):
        for b in range(2,i):
            for a in range(1,b//2+1):
                if gcd(a,b) != 1: continue
                n = b*(i*i+101);j=a*(i*i+101)
                assert determinant(n,j,(0,0),(b,a)) == 0
                t=Fraction(j,n)
                assert 0<t<=Fraction(1,2) and t.denominator<=i-1
                zero_cases += 1
    stats.update(random_geometric_checks=geometric, constructed_zero_lines=zero_cases)

    # Essential negative example: dropping the nonzero-line hypothesis is false.
    demo = analyze(535,10,214)
    x = demo['rows'][0]['cells'][0];y=demo['rows'][5]['cells'][2]
    assert (x,y) == (107,53)
    assert x*y > demo['pair_bound'] and determinant(535,214,(0,0),(5,2)) == 0
    split = row_data(36,3,15)[1]['cells']
    assert split == [5,7]
    for cap in range(2,30):
        for value in range(1,200):
            k = minimum_slots(value,cap)
            assert value <= cap**k and (k == 0 or cap**(k-1)<value)
    stats['capacity_integer_checks']=28*199
    stats['negative_examples'] = [dict(n=535,i=10,j=214,first_cell=[0,0,107],
        second_cell=[5,2,53],product=5671,pair_bound=4734,determinant=0),
        dict(n=36,i=3,j=15,row=1,cells=[5,7])]

    old_hashes = json.loads((ROOT/'previous_phase/SHA256.json').read_text())
    # The preceding package stores a plain relative-path -> SHA-256 map.
    if 'files' in old_hashes: old_hashes = old_hashes['files']
    for path, digest in old_hashes.items():
        assert hashlib.sha256((ROOT/'previous_phase'/path).read_bytes()).hexdigest() == digest
    stats['previous_package_hashes_verified'] = len(old_hashes)
    stats.update(status='PASS', finite_test_note='Infinite claims rely on REPORT.md proofs.',
        exhaustive_domain='10<=n<=120, 3<=i<=min(12,floor(n/2)-1), i<j<=floor(n/2)')
    (ROOT/'verification.json').write_text(json.dumps(stats,indent=2)+'\n')
    print(json.dumps(stats,indent=2))


if __name__ == '__main__': main()
