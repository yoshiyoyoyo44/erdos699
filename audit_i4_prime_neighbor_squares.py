"""Exact finite remainder for i=4, n=(p+1)^2 with p prime.

The note excludes every p>=134 analytically. This script enumerates every
remaining prime and every j left by Kummer at p, and records odd prime
witnesses >=5. Standard library only; no existing i=3 bound is used.
"""

import json
from math import comb, gcd, isqrt
from pathlib import Path


def prime(n):
    return n >= 2 and all(n % d for d in range(2, isqrt(n) + 1))


def factors(n):
    result = set()
    d = 2
    while d * d <= n:
        if n % d == 0:
            result.add(d)
            while n % d == 0:
                n //= d
        d += 1
    if n > 1:
        result.add(n)
    return result


def carry_free(n, j, p):
    while n or j:
        if j % p > n % p:
            return False
        n //= p
        j //= p
    return True


def main():
    if not __debug__:
        raise RuntimeError("Run without -O.")
    algebra_cases = 0
    for p in range(5, 1001, 2):
        n = (p + 1) ** 2
        js = (p, p + 1, 2 * p, 2 * p + 1)
        remainders = (13 * p - 5, 4 * p - 2, 68 * p - 28, 38 * p - 16)
        for j, R in zip(js, remainders):
            assert (j * (j - 1) * (j - 2) - R) % (n - 2) == 0
            assert 0 < R <= 68 * p - 28
            if p >= 134:
                assert (n - 2) // 2 > R
            algebra_cases += 1
    records = []
    coverage = 0
    for p in range(2, 134):
        if not prime(p):
            continue
        n = (p + 1) ** 2
        A = comb(n, 4)
        if p >= 5:
            assert A % p == 0
            assert n % 4 == 0 and (n - 2) % 3 != 0
            candidates = {p, p + 1, 2 * p, 2 * p + 1}
            actual = {j for j in range(5, n // 2 + 1) if carry_free(n, j, p)}
            assert actual == candidates
            coverage += n // 2 - 4
        else:
            candidates = set(range(5, n // 2 + 1))
            coverage += len(candidates)
        eligible = sorted(set().union(*(factors(n - r) for r in range(4))) - {2, 3})
        eligible = [q for q in eligible if A % q == 0]
        witnesses = []
        for j in sorted(candidates):
            D = gcd(A, comb(n, j))
            q = next(q for q in eligible if D % q == 0)
            assert prime(q) and q >= 5
            assert A % q == 0 and comb(n, j) % q == 0
            witnesses.append(dict(j=j, common_prime=q))
        records.append(dict(p=p, n=n, witnesses=witnesses))
    result = dict(
        scope="Finite remainder for the unrestricted prime-neighbor square "
              "theorem at i=4; not a solution of general i=4.",
        independent_of_i3=True,
        analytic_tail="All primes p>=134 are excluded in the note.",
        finite_primes=len(records),
        max_n=max(r["n"] for r in records),
        covered_pairs=coverage,
        explicit_witnesses=sum(len(r["witnesses"]) for r in records),
        remainder_identity_audits=algebra_cases,
        records=records,
    )
    path = Path(__file__).with_name("verification_i4_prime_neighbor_squares.json")
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in result.items() if k != "records"}, indent=2))


if __name__ == "__main__":
    main()
