#!/usr/bin/env python3
"""Exact, factorization-free necessary conditions for Erdos 699 candidates.

Full-row divisibility is NECESSARY, not sufficient: carries above a row's
valuation are not tested. No factorization of a large integer is performed.
"""
from math import comb, gcd, isqrt, lcm, prod
import argparse
import json


def primes_below(bound):
    return [p for p in range(2, bound)
            if all(p % d for d in range(2, isqrt(p) + 1))]


def row_data(n, i, j):
    if not (3 <= i < j <= n // 2):
        raise ValueError('Require integers 3 <= i < j <= n/2.')
    small = primes_below(i)
    Q = comb(n, i)
    for p in small:
        while Q % p == 0:
            Q //= p
    prime_i = i in primes_below(i + 1)
    rows = []
    for s in range(i):
        qs = gcd(Q, n - s)
        # Restore the removed factor i only when p=i actually divides C(n,i).
        rs = qs * (i if prime_i and qs % i == 0 else 1)
        cells = [gcd(rs, j - u) for u in range(s + 1)]
        covered = prod(cells)
        assert rs % covered == 0
        rows.append(dict(s=s, Q_s=qs, R_s=rs, cells=cells,
                         uncovered=rs // covered))
    return rows


def determinant(n, j, first, second):
    s, u = first
    r, v = second
    return (s-r)*(j-u) - (u-v)*(n-s)


def minimum_slots(value, cap):
    """Least k>=0 with value <= cap**k; None if impossible with cap<=1."""
    if value <= 1:
        return 0
    if cap <= 1:
        return None
    k, power = 0, 1
    while power < value:
        power *= cap
        k += 1
    return k


def analyze(n, i, j):
    rows = row_data(n, i, j)
    cells = [(r['s'], u, b) for r in rows
             for u, b in enumerate(r['cells']) if b > 1]
    pair_violations = []
    zero_lines = []
    K = (i - 1) * (n - i + 1)
    for k, (s, u, b) in enumerate(cells):
        for r, v, c in cells[k+1:]:
            D = determinant(n, j, (s, u), (r, v))
            assert gcd(b, c) == 1 and D % (b*c) == 0
            assert abs(D) <= K
            if D == 0:
                zero_lines.append([[s, u], [r, v]])
            if b*c > K:
                pair_violations.append([[s, u], [r, v]])
    columns = [prod(r['cells'][u] for r in rows if r['s'] >= u)
               for u in range(i)]
    diagonals = [prod(r['cells'][r['s'] - v]
                      for r in rows if r['s'] >= v) for v in range(i)]
    assert all((j-u) % c == 0 for u, c in enumerate(columns))
    assert all((n-j-v) % d == 0 for v, d in enumerate(diagonals))
    capacity = None
    if cells and n >= 10**87 and i <= 119:
        s0, u0, M = max(cells, key=lambda x: x[2])
        T = K // M
        necessary = []
        for row in rows:
            r = row['s']
            rest = row['R_s'] // M if r == s0 else row['R_s']
            slots = minimum_slots(rest, T)
            necessary.append(dict(s=r,
                minimum_other_occupied_cells=slots,
                available_other_cells=r if r == s0 else r+1))
        capacity = dict(largest_cell=[s0, u0], M=M, T=T, rows=necessary)
    return dict(n=n, i=i, j=j, rows=rows, columns=columns,
        diagonals=diagonals, pair_bound=K, zero_determinant_pairs=zero_lines,
        forbidden_large_pair_count=len(pair_violations),
        forbidden_large_pairs=pair_violations,
        full_row_conditions_pass=all(r['uncovered'] == 1 for r in rows),
        pair_bound_applicable_to_counterexamples=(3 <= i <= 119 and n >= 10**87),
        capacity=capacity,
        warning='Necessary conditions only; not a counterexample certificate.')


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('n', type=int)
    parser.add_argument('i', type=int)
    parser.add_argument('j', type=int)
    args = parser.parse_args()
    print(json.dumps(analyze(args.n, args.i, args.j), indent=2))


if __name__ == '__main__':
    main()
