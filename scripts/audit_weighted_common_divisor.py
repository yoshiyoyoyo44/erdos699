"""Audit the quantitative common-divisor consequence and optimal ramp weights.

General proofs, including divisibility and monotonicity, are in the research
note. Finite tuples exercise unconditional statements, not absent counterexamples.
"""
from fractions import Fraction
from math import comb, gcd, isqrt, prod
import json

from weighted_cover_sources import INDICES, ROOT


def primes_below(i):
    return [p for p in range(2, i) if all(p % d for d in range(2, isqrt(p)+1))]


def weights(i):
    h = i-1
    b = (2*h+2)//3
    return h-b, b, 3*b-h, b*(b+1)//2


def check_tuple(n, i, j):
    a, b, d, S = weights(i)
    Q = comb(n, i)
    for p in primes_below(i):
        while Q % p == 0:
            Q //= p
    rows = [gcd(Q, n-s) for s in range(i)]
    assert prod(rows) == Q
    covered = []
    cells = {}
    for s, value in enumerate(rows):
        product_j = prod(j-u for u in range(s+1))
        covered.append(gcd(value, product_j))
        for u in range(s+1):
            cells[s, u] = gcd(value, j-u)
        assert covered[-1] == prod(cells[s, u] for u in range(s+1))
    T = prod(covered)
    W = Q//T
    common_large_part = gcd(Q, comb(n, j))
    assert common_large_part % W == 0
    assert W**d*n**(3*S) >= 4**S*Q**d
    hsmall = 1 if i in primes_below(i+1) else i
    assert Q*n**len(primes_below(i)) >= hsmall*comb(n, i)
    return W > 1, common_large_part > W


def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled; do not use python -O.')
    parameters = []
    comparisons = 0
    positive = []
    for i in range(3, 120):
        a, b, d, S = weights(i)
        ratio = Fraction(3*S, d)
        for candidate in range((i-1)//3+1, i):
            other = Fraction(3*candidate*(candidate+1), 2*(3*candidate-(i-1)))
            assert ratio <= other
            comparisons += 1
        pi = len(primes_below(i))
        gap = d*(i-pi)-3*S
        if gap > 0:
            positive.append(i)
        parameters.append(dict(i=i, pi=pi, a=a, b=b, d=d, S=S,
                               degree_gap=gap, growth_exponent=str(Fraction(gap, d))))
    assert positive == INDICES
    count = nontrivial = strict = 0
    for i in range(3, 16):
        for n in range(2*i+2, 101):
            for j in range(i+1, n//2+1):
                useful, extra = check_tuple(n, i, j)
                count += 1
                nontrivial += useful
                strict += extra
    boundary = []
    for i in INDICES:
        for n in (2*i+2, i*i+i-1):
            j = n//2
            check_tuple(n, i, j)
            boundary.append([n, i, j])
    # Higher Kummer layers may make the true common part larger than W.
    assert check_tuple(151, 3, 50)[1]
    result = dict(status='PASS', index_parameter_rows=parameters,
                  weight_comparisons=comparisons, positive_gap_indices=positive,
                  exhaustive_triples=count, nontrivial_divisor_cases=nontrivial,
                  strict_common_part_cases=strict, boundary_cases=boundary,
                  scope='Unconditional divisor and lower bound; general proof in research note.')
    (ROOT/'data/results/verification_weighted_common_divisor.json').write_text(
        json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps(dict(status='PASS', exhaustive_triples=count,
                         nontrivial_divisor_cases=nontrivial,
                         boundary_cases=len(boundary), weight_comparisons=comparisons)))


if __name__ == '__main__':
    main()
