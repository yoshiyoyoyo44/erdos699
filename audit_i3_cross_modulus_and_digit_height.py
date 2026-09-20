"""Audit universal cross-modulus bounds and polynomial rigidity for i=3.

Standard library only. Finite checks supplement the proofs in the note;
they do not exhaust the candidates of Erdos Problem 699.
"""

import json
from itertools import product
from math import prod
from pathlib import Path


def trim(poly):
    poly = list(poly)
    while poly and poly[-1] == 0:
        poly.pop()
    return poly


def mul(A, B):
    out = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            out[i + j] += a * b
    return trim(out)


def shifted(A, c):
    out = list(A) or [0]
    out[0] -= c
    return trim(out)


def evaluate(poly, x):
    value = 0
    for c in reversed(poly):
        value = value * x + c
    return value


def pseudo_remainder(G, D):
    R = trim(G)
    Q = [0]
    scale = 1
    a = D[-1]
    while len(R) >= len(D):
        leading = R[-1]
        gap = len(R) - len(D)
        R = [a * r for r in R]
        Q = [a * q for q in Q]
        Q += [0] * max(0, gap + 1 - len(Q))
        Q[gap] += leading
        for i, d in enumerate(D):
            R[gap + i] -= leading * d
        R = trim(R)
        scale *= a
    return R, trim(Q), scale


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def norm(poly):
    return sum(abs(c) for c in poly)


def audit_rigidity():
    counts = dict(polynomial_pairs=0, zero_remainders=0,
                  nonmonic_pairs=0, mixed_support_counterexample_checked=False)
    for m in range(1, 5):
        for constant in range(3):
            for middle in product(range(3), repeat=m - 1):
                for leading in (1, 2):
                    F = [constant, *middle, leading]
                    support = [i for i, f in enumerate(F) if i and f]
                    if constant == 2 and len({v2(i) for i in support}) != 1:
                        continue
                    H = sum(F)
                    K = H * (H + 1) * (H + 2) ** (2 * m + 2)
                    shift = 2 if constant == 1 else 1
                    D = shifted(F, shift)
                    for J in product(*(range(f + 1) for f in F)):
                        J = trim(J)
                        G = mul(J, shifted(J, 1))
                        if shift == 2:
                            G = mul(G, shifted(J, 2))
                        R, Q, scale = pseudo_remainder(G, D)
                        assert norm(R) <= K
                        assert len(R) <= m
                        # Check the exact polynomial identity, not just a sample.
                        right = mul(Q, D)
                        size = max(len(right), len(R), len(G))
                        right += [0] * (size - len(right))
                        for i, r in enumerate(R):
                            right[i] += r
                        left = [scale * g for g in G] + [0] * (size - len(G))
                        assert left == right
                        if not R:
                            allowed = ([], trim(F)) if constant == 0 else (
                                [], [1], shifted(F, 1), trim(F))
                            assert J in allowed
                            counts["zero_remainders"] += 1
                        p = 6 * K + 3
                        assert abs(6 * evaluate(R, p)) < evaluate(F, p) - shift
                        assert (evaluate(R, p) == 0) == (not R)
                        counts["polynomial_pairs"] += 1
                        counts["nonmonic_pairs"] += leading > 1
    # Dropping the support condition from the constant-2 proof is invalid.
    # This pair satisfies F-1 | J(J-1), with nontrivial bounded coefficients.
    F, J = [2, 2, 2, 1], [1, 1, 1]
    assert not pseudo_remainder(mul(J, shifted(J, 1)), shifted(F, 1))[0]
    assert pseudo_remainder(mul(mul(J, shifted(J, 1)), shifted(J, 2)),
                            shifted(F, 2))[0]
    counts["mixed_support_counterexample_checked"] = True
    return counts


def audit_transfer_identities():
    counts = dict(Q1_parameter_cases=0, Q2_parameter_cases=0)
    for a in range(3, 82, 2):
        for q in range(3, 84, 2):
            n = a * q + 1
            for b in range(1, (a - 1) // 2 + 1):
                for s in (0, 1):
                    j = b * q + s
                    if not 4 <= j <= n // 2:
                        continue
                    P = (b + a * s) * (b + a * (s - 1)) * (b + a * (s - 2))
                    assert (a ** 3 * j * (j - 1) * (j - 2) - P) % (n - 2) == 0
                    assert 0 < 27 * P * P <= 4 * a ** 6
                    counts["Q1_parameter_cases"] += 1
    for a in range(2, 82, 2):
        for q in range(3, 84, 2):
            n = a * q + 2
            for b in range(1, a // 2 + 1):
                for s in (0, 1, 2):
                    j = b * q + s
                    if not 4 <= j <= n // 2:
                        continue
                    P = (a * s - b) * (a * (s - 1) - b)
                    assert (a * a * j * (j - 1) - P) % (n - 1) == 0
                    assert 0 < abs(P) <= 2 * a * a - 3 * a + 1
                    assert 4 * abs(P) <= (3, 1, 8)[s] * a * a
                    counts["Q2_parameter_cases"] += 1
    return counts


def audit_quadratic_classification():
    counts = dict(polynomial_pairs=0, simultaneous_zero_remainders=0,
                  nontrivial_exceptions=0)
    for a in range(1, 17):
        for b in range(25):
            F = [2, b, a]
            for c, e, d in product(range(3), range(b + 1), range(a + 1)):
                J = trim([c, e, d])
                G = mul(J, shifted(J, 1))
                R1 = pseudo_remainder(G, shifted(F, 1))[0]
                R2 = pseudo_remainder(mul(G, shifted(J, 2)), shifted(F, 2))[0]
                counts["polynomial_pairs"] += 1
                if R1 or R2:
                    continue
                counts["simultaneous_zero_remainders"] += 1
                if J in ([], [1], shifted(F, 1), F):
                    continue
                assert b % 8 == 0
                h = b // 8
                assert h >= 1 and a == 12 * h * h
                assert J in ([0, h, 6 * h * h], [2, 7 * h, 6 * h * h])
                assert all(evaluate(F, x) % 4 == 2 for x in range(4))
                counts["nontrivial_exceptions"] += 1
    assert counts["nontrivial_exceptions"] == 2
    # Verify every coefficient of the general exceptional identities.
    for h in range(1, 101):
        F = [2, 8 * h, 12 * h * h]
        for J in ([0, h, 6 * h * h], [2, 7 * h, 6 * h * h]):
            G = mul(J, shifted(J, 1))
            assert not pseudo_remainder(G, shifted(F, 1))[0]
            assert not pseudo_remainder(mul(G, shifted(J, 2)), shifted(F, 2))[0]
    counts["exception_family_identity_audits"] = 200
    return counts


def audit_cubic_obstruction():
    F = [2, 54, 648, 1728]
    J = [2, 46, 312, 576]
    E = [46, 2934, 55620, 454464, 1850688, 3732480, 2985984]
    G1 = mul(J, shifted(J, 1))
    G2 = mul(G1, shifted(J, 2))
    assert not pseudo_remainder(G1, shifted(F, 1))[0]
    assert [27 * g for g in G2] == mul(shifted(F, 2), E)
    assert E[0] % 3 == 1 and all(e % 3 == 0 for e in E[1:])
    assert all(0 <= j <= f for j, f in zip(J, F))

    def v3(n):
        e = 0
        while n % 3 == 0:
            n //= 3
            e += 1
        return e

    def carry_free(n, j, p):
        while n or j:
            if j % p > n % p:
                return False
            n //= p
            j //= p
        return True

    for x in range(1, 201):
        n, j = evaluate(F, x), evaluate(J, x)
        assert 4 <= j <= n // 2
        assert (n % 4 == 0) == (x % 2 == 1)
        assert j * (j - 1) % (n - 1) == 0
        assert v3(j * (j - 1) * (j - 2)) == v3(n - 2) - 3
        assert 6 * j * (j - 1) * (j - 2) % (n - 2) != 0
        assert not carry_free(n, j, 3) and not carry_free(n, 3, 3)
    return dict(polynomial_identities=2, integer_specializations=200,
                common_prime=3, is_counterexample=False)


def factor(n):
    out = []
    p = 2
    while p * p <= n:
        e = 0
        while n % p == 0:
            n //= p
            e += 1
        if e:
            out.append((p, e))
        p += 1
    if n > 1:
        out.append((n, 1))
    return out


def delta(n):
    return 3 if n % 3 == 0 and n % 9 != 0 else 1


def crt_candidates(n, Q1, powers):
    residues, modulus = [0], 1
    for q in powers:
        inv = pow(modulus, -1, q)
        residues = [r + modulus * ((s - r) * inv % q)
                    for r in residues for s in (0, 1)]
        modulus *= q
    assert modulus == Q1 and len(set(residues)) == 2 ** len(powers)
    for r in residues:
        lo = max(0, (4 - r + Q1 - 1) // Q1)
        hi = (n // 2 - r) // Q1
        for t in range(lo, hi + 1):
            yield r + t * Q1


def audit_relaxed_pairs():
    counts = dict(n_values=0, CRT_candidates=0, relaxed_pairs=0,
                  block_checks=0, prime_power_checks=0, examples=[])
    for n in [*range(8, 5001, 4), 76672]:
        d1, d2 = delta(n - 1), delta(n // 2 - 1)
        Q1, Q2 = (n - 1) // d1, (n - 2) // (2 * d2)
        powers1 = [p ** e for p, e in factor(Q1)]
        powers2 = [p ** e for p, e in factor(Q2)]
        for j in crt_candidates(n, Q1, powers1):
            counts["CRT_candidates"] += 1
            if j * (j - 1) * (j - 2) % Q2:
                continue
            counts["relaxed_pairs"] += 1
            if len(counts["examples"]) < 8 or (n, j) == (76672, 26775):
                counts["examples"].append(dict(n=n, j=j))
            blocks1 = [prod(q for q in powers1 if j % q == s) for s in (0, 1)]
            blocks2 = [prod(q for q in powers2 if j % q == s) for s in (0, 1, 2)]
            for blocks, powers, r in ((blocks1, powers1, 1), (blocks2, powers2, 2)):
                for q in [*blocks, *powers]:
                    if q == 1:
                        continue
                    a = (n - r) // q
                    s = j % q
                    assert s in range(r + 1)
                    if r == 1:
                        assert 27 * (n - 2) ** 2 <= 16 * d2 ** 2 * a ** 6
                    else:
                        assert n - 1 <= d1 * (2 * a * a - 3 * a + 1)
                        assert q * q < 2 * d1 * n
                        if s < 2:
                            assert 4 * (n - 1) * q * q <= (3, 1)[s] * d1 * (n - 2) ** 2
                counts["block_checks"] += sum(q != 1 for q in blocks)
                counts["prime_power_checks"] += len(powers)
        counts["n_values"] += 1
    assert counts["relaxed_pairs"] > 0
    assert dict(n=76672, j=26775) in counts["examples"]
    return counts


def main():
    if not __debug__:
        raise RuntimeError("Run without -O.")
    result = dict(
        scope="Finite audits of universal paper proofs. Not a complete exclusion of i=3.",
        dependency="Only elementary Kummer/divisibility lemmas; no u>=49 or Magma dependency.",
        transfer_identities=audit_transfer_identities(),
        polynomial_rigidity=audit_rigidity(),
        quadratic_classification=audit_quadratic_classification(),
        cubic_obstruction=audit_cubic_obstruction(),
        relaxed_candidates=audit_relaxed_pairs(),
    )
    path = Path(__file__).with_name("verification_i3_cross_modulus_and_digit_height.json")
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
