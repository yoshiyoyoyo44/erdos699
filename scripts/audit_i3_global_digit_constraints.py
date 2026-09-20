"""Exact audits and finite certificates for the accompanying global digit note.

Standard library only. Run without -O. This does not enumerate all possible
counterexamples and does not prove a full solution of Erdos 699.
"""
from repo_paths import artifact_path

import hashlib
import json
from itertools import product
from math import comb, gcd, isqrt, lcm
from pathlib import Path

from audit_i3_low_digit_continuation import (
    digit_data, digits, primes_below, trial_factors, v2,
)


def audit_unique_weight_two(limit=200000):
    spf = list(range(limit + 1))
    for p in range(2, isqrt(limit) + 1):
        if spf[p] == p:
            for k in range(p * p, limit + 1, p):
                if spf[k] == k:
                    spf[k] = p
    counts = dict(integers=0, prime_divisors=0, weight_two=0,
                  reciprocity_constraints=0)
    examples = []
    for J in range(4, limit + 1, 4):
        counts["integers"] += 1
        t, factors = J, []
        while t > 1:
            p = spf[t]
            if p != 2:
                factors.append(p)
            while t % p == 0:
                t //= p
        special = []
        for p in factors:
            counts["prime_divisors"] += 1
            if sum(digits(J, p)) != 2:
                continue
            special.append(p)
            counts["weight_two"] += 1
            assert p % 4 == 3 and v2(p + 1) == v2(J)
            for ell in factors:
                if ell != p:
                    assert pow(ell, (p - 1) // 2, p) == 1
                    counts["reciprocity_constraints"] += 1
        assert len(special) <= 1
        if special and len(examples) < 8:
            examples.append(dict(J=J, p=special[0]))
    assert counts["weight_two"] and counts["reciprocity_constraints"]
    # Divisibility by 4 is essential: both bases work at valuation 1.
    assert digit_data(30, 3)[0] == digit_data(30, 5)[0] == 2
    return dict(limit=limit, counts=counts, examples=examples,
                valuation_one_exception=dict(J=30, primes=[3, 5]))


def audit_loss_bookkeeping():
    # One prime per block suffices to exercise the six marked positions.
    # More primes repeat positions; the proof counts at most one exception
    # per side independently of their number.
    count = 0
    for tj, ty, ry, sj, bj, cy in product((0, 1), repeat=6):
        if tj + sj + bj > 1 or ty + ry + cy > 1:
            continue
        T = (4 - 2 * tj) + (4 - 2 * ty)
        R, S = 7 - 2 * ry, 7 - 2 * sj
        A, B, C = 6, 6 - 2 * bj, 6 - 2 * cy
        assert T + R + S + A + B + C >= 8 + 2 * 7 + 3 * 6 - 4
        count += 1
    return dict(admissible_six_position_patterns=count)


def make_row_certificate(D):
    splits = set(range(2, D // 2 + 1))
    C3 = comb(D, 3)
    candidates = []
    for q in trial_factors(C3):
        if q == 2:
            continue
        power, K = q, 1
        while power <= D:
            if q != 3 or K >= 2:
                covered = {a for a in splits if D % power < a % power}
                if covered:
                    candidates.append((q, K, power, covered))
            power *= q
            K += 1
    uncovered, selected = set(splits), []
    while uncovered:
        assert candidates, (D, sorted(uncovered))
        best = max(candidates,
                   key=lambda x: (len(x[3] & uncovered), -x[2]))
        assert best[3] & uncovered, (D, sorted(uncovered))
        selected.append(best)
        uncovered -= best[3]
        candidates.remove(best)
    modulus = lcm(*(x[2] for x in selected))
    witnesses = []
    for a in sorted(splits):
        q, K, power, _ = next(x for x in selected if a in x[3])
        assert C3 % q == 0 and comb(D, a) % q == 0
        assert D % power < a % power
        assert modulus % power == 0
        witnesses.append(dict(a=a, q=q, K=K))
    return dict(D=D, modulus=modulus, witnesses=witnesses)


def verify_row_certificate(row):
    # Verification uses the recorded certificate, without greedy selection.
    D, L = row["D"], row["modulus"]
    assert [w["a"] for w in row["witnesses"]] == list(range(2, D // 2 + 1))
    lifts = 0
    for w in row["witnesses"]:
        a, q, K = w["a"], w["q"], w["K"]
        assert trial_factors(q) == {q: 1}
        assert q >= 3 and K >= (2 if q == 3 else 1)
        Q = q ** K
        assert L % Q == 0 and comb(D, 3) % q == 0
        assert D % Q < a % Q
        # Check both a and D-a: the carry criterion is symmetric.
        assert D % Q < (D - a) % Q
        # Congruence transfer works for any integer base ==1 mod L.
        # Primality of the original base is unnecessary for this identity.
        base = 1 + L * (D + 1)
        assert base > D
        for e in (1, 2, 5):
            # Shifted units keep digit sums exactly D,a at nonconstant N,X.
            N = (D - 1) + base ** 2
            X = (a - 1) + base ** 2
            Y = N - X
            assert sum(digits(N, base)) == D
            assert sum(digits(X, base)) == a
            assert sum(digits(Y, base)) == D - a
            n, j = base ** e * N, base ** e * X
            assert comb(n, 3) % q == 0
            assert n % Q < j % Q
            assert n % Q < (n - j) % Q
            lifts += 1
    return lifts


def audit_row_certificates():
    rows = [make_row_certificate(D) for D in range(6, 257, 2)]
    lifts = sum(verify_row_certificate(row) for row in rows)
    raw = json.dumps(rows, sort_keys=True, separators=(",", ":")).encode()
    # The missing D=4 row is real, not a certificate-generator limitation.
    assert gcd(comb(4, 3), comb(4, 2)) == 2
    # q^b+1 theorem: these simple certificates work for every split.
    prime_power_cases = 0
    for q in primes_below(100):
        for b in range(1, 6):
            if q == 3 and b == 1:
                continue
            Q = q ** b
            D = Q + 1
            assert comb(D, 3) % q == 0
            for a in {2, D // 2, D - 2}:
                assert D % Q < a % Q
            prime_power_cases += 1
    return dict(D_min=6, D_max=256, rows=len(rows),
                split_witnesses=sum(len(r["witnesses"]) for r in rows),
                lifted_integer_checks=lifts,
                prime_power_boundary_cases=prime_power_cases,
                certificate_sha256=hashlib.sha256(raw).hexdigest(),
                certificates=rows)


def audit_gamma3_refinements():
    counts = dict(single_numbers=0, positive_alternating_sum=0,
                  individual_bound_at_least_8=0,
                  local_totals=0, local_odd_splits=0,
                  low_weight_odd_normalized_splits=0,
                  weight_six_odd_splits=0, weight_six_size_failures=0)
    for p in primes_below(100):
        if p % 3 == 2:
            for X in range(2, 20001, 2):
                if X % 3 == 0:
                    continue
                s, alt = digit_data(X, p)
                lower = 1 << min(v2(X), v2(p + 1))
                assert alt != 0 and alt % lower == 0
                assert s >= abs(alt) >= lower
                counts["single_numbers"] += 1
                counts["positive_alternating_sum"] += alt > 0
                counts["individual_bound_at_least_8"] += lower >= 8
        if p == 3:
            continue
        for U in range(1, 100, 2):
            if gcd(U, 3 * p) != 1:
                continue
            for u in range(4, 33):
                N = 3 * U * (1 << u)
                ds = digits(N, p)
                total = sum(ds)
                counts["local_totals"] += 1
                if total not in (6, 8):
                    continue
                terms = [(p ** i, d) for i, d in enumerate(ds) if d]
                for part in product(*(range(d + 1) for _, d in terms)):
                    sx = sum(part)
                    if sx < 3 or total - sx < 3 or sx % 2 != 1:
                        continue
                    X = sum(a * Q for a, (Q, _) in zip(part, terms))
                    Y = N - X
                    if not 0 < X < Y:
                        continue
                    assert X % 2 == Y % 2 == 1
                    counts["local_odd_splits"] += 1
                    if X % U or Y % U or X % 3 == 0:
                        continue
                    assert gcd(X, Y) == U
                    counts["low_weight_odd_normalized_splits"] += 1
                    if total == 6:
                        counts["weight_six_odd_splits"] += 1
                        assert p % 8 == 7 and p % 3 == 2
                        assert u == v2(p + 1)
                        assert (3 * U * p) ** 3 >= 1 << (u - 2)
                        counts["weight_six_size_failures"] += 1
                    if (3 * U * p) ** 3 < 1 << (u - 2):
                        assert total >= 8
    assert counts["individual_bound_at_least_8"] > 0
    assert counts["low_weight_odd_normalized_splits"] > 0
    return counts


def main():
    if not __debug__:
        raise RuntimeError("Run without -O.")
    result = dict(
        scope="Finite audits plus explicit digit-transfer certificates. "
              "Not a full solution or a new global n/u bound.",
        unique_weight_two=audit_unique_weight_two(),
        loss_bookkeeping=audit_loss_bookkeeping(),
        row_transfer=audit_row_certificates(),
        gamma3_refinements=audit_gamma3_refinements(),
    )
    path = artifact_path("verification_i3_global_digit_constraints.json")
    path.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")
    display = dict(result)
    display["row_transfer"] = {k: v for k, v in result["row_transfer"].items()
                               if k != "certificates"}
    print(json.dumps(display, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
