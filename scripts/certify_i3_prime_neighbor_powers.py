"""Generate the bounded remainder for the prime-neighbor power theorem.

SymPy is used only to propose factorizations. The separate standard-library
replayer checks every prime using recursive Lucas certificates and enumerates
the full CRT remainder independently.
"""
from repo_paths import artifact_path

import json
from itertools import product
from math import prod
from pathlib import Path

from sympy import factorint, isprime

import make_certificate


def v3(n):
    e = 0
    while n % 3 == 0:
        n //= 3
        e += 1
    return e


def bound(m):
    H = 3 ** m - 2 ** m
    return 3 * H * (H + 1) + 1


def row(u):
    n = 1 << u
    d1 = 3 if v3(n - 1) == 1 else 1
    d2 = 3 if v3(n // 2 - 1) == 1 else 1
    Q1 = (n - 1) // d1
    Q2 = (n // 2 - 1) // d2
    factors = sorted((int(p), int(e)) for p, e in factorint(Q1).items())
    powers = [p ** e for p, e in factors]
    candidates = set()
    for bits in product((0, 1), repeat=len(powers)):
        a = prod(q for q, b in zip(powers, bits) if b)
        b = Q1 // a
        residue = 0 if b == 1 else a * pow(a, -1, b) % Q1
        j = residue + max(0, (4 - residue + Q1 - 1) // Q1) * Q1
        while j <= n // 2:
            candidates.add(j)
            j += Q1
    survivors = [j for j in candidates if j * (j - 1) * (j - 2) % Q2 == 0]
    assert not survivors, (u, survivors)
    for p, _ in factors:
        make_certificate.prove(p)
    return dict(u=u, Q1_factors=factors, CRT_candidates=len(candidates))


def main():
    multipliers = range(1, 9)
    bounds = [dict(m=m, H=3 ** m - 2 ** m, bound=bound(m)) for m in multipliers]
    cases = []
    for m in multipliers:
        for k in range(2, bound(m).bit_length()):
            assert (1 << k) <= bound(m)
            if isprime((1 << k) - 1):
                cases.append(dict(m=m, k=k, u=m * k))
    # n=4 has no eligible j. Include all other bounded cases so this
    # theorem does not depend on the earlier u>=49 computation.
    needed = sorted({case["u"] for case in cases if case["u"] >= 3})
    rows = []
    for u in needed:
        entry = row(u)
        rows.append(entry)
        print(json.dumps(entry), flush=True)
    result = dict(
        scope="Finite remainder for the all-exponent theorem; not a complete "
              "solution of i=3 or a contiguous u-range extension.",
        dependency="Only the elementary Kummer and divisibility lemmas in the note.",
        max_multiplier=8,
        analytic_bounds=bounds,
        bounded_mersenne_cases=cases,
        rows=rows,
        prime_certificates=make_certificate.cert,
    )
    path = artifact_path("i3_prime_neighbor_power_certificate.json")
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(dict(rows=len(rows),
                          CRT_candidates=sum(r["CRT_candidates"] for r in rows),
                          prime_certificates=len(make_certificate.cert))))


if __name__ == "__main__":
    main()
