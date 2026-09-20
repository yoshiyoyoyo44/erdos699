"""Exact audits of the complete cubic digit-polynomial classification.

Standard library only. The unbounded classification is proved in the note;
the bounded coefficient search is a supplementary check, not its proof.
"""
from repo_paths import artifact_path

import json
from fractions import Fraction as Q
from itertools import combinations, product
from pathlib import Path


def trim(A):
    A = list(A)
    while A and A[-1] == 0:
        A.pop()
    return A


def shift(A, c):
    A = list(A) or [0]
    A[0] -= c
    return trim(A)


def mul(A, B):
    result = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            result[i + j] += a * b
    return trim(result)


def remainder(A, B):
    """Integer pseudo-remainder; zero iff the rational remainder is zero."""
    A = trim(A)
    while len(A) >= len(B):
        leading, offset = A[-1], len(A) - len(B)
        A = [B[-1] * a for a in A]
        for i, b in enumerate(B):
            A[offset + i] -= leading * b
        A = trim(A)
    return A


def rational_division(A, B):
    """Separate exact rational implementation for the exceptional family."""
    A = [Q(a) for a in trim(A)]
    B = [Q(b) for b in B]
    quotient = [Q(0)] * max(0, len(A) - len(B) + 1)
    while len(A) >= len(B):
        offset = len(A) - len(B)
        c = A[-1] / B[-1]
        quotient[offset] += c
        for i, b in enumerate(B):
            A[offset + i] -= c * b
        A = trim(A)
    return trim(quotient), A


def evaluate(A, x):
    value = 0
    for a in reversed(A):
        value = value * x + a
    return value


def audit_nine_cases():
    rows, survivors = [], []
    for s in range(3):
        for z, w in combinations(range(3), 2):
            D = Q(z + w + s - 2, 3)
            L = 1 + D - s
            row = dict(s=s, z=z, w=w, D=str(D), L=str(L))
            if not L:
                row.update(allowed=False, reason="L=0 contradicts the root identity")
            else:
                C = Q((z - s) * (w - s)) / (L * L) - 1
                B = C - 1 + 1 / L
                allowed = 0 <= D <= 1 and C >= 0 and B > 0
                row.update(C=str(C), B=str(B), allowed=allowed)
                if allowed:
                    survivors.append((s, z, w, D, C, B))
            rows.append(row)
    assert survivors == [(2, 0, 1, Q(1, 3), Q(7, 2), Q(1))]
    return dict(cases=len(rows), survivors=1, rows=rows)


def audit_trace_and_remainder():
    count = 0
    for s in range(3):
        for B, C, D in product((Q(1, 3), Q(1), Q(7, 2)), repeat=3):
            F = [Q(2), 1 + C, B + C, B]
            J = [Q(s), D + (s - 1) * C, C * D + (s - 1) * B, B * D]
            P = [1 + C, B + C, B]
            L = 1 + D - s
            _, R = rational_division(J, P)
            u, v = s + L * (1 + C), L * B
            assert R == trim([u, v])
            root_sum, root_product = -(B + C) / B, (1 + C) / B
            S = 2 * u + v * root_sum
            T = u * u + u * v * root_sum + v * v * root_product
            assert S == 2 * s + L * (2 + C - B)
            assert T - s * S + s * s == L * L * (1 + C)
            count += 1
    return dict(rational_identity_cases=count)


def audit_bounded_coefficients():
    counts = dict(F_polynomials=0, pairs=0, first_condition=0,
                  both_conditions=0, nontrivial_pairs=0)
    for leading in range(1, 7):
        for linear, quadratic in product(range(13), repeat=2):
            F = [2, linear, quadratic, leading]
            F1, F2 = shift(F, 1), shift(F, 2)
            trivial = ([], [1], F1, F)
            for coeffs in product(*(range(f + 1) for f in F)):
                J = trim(coeffs)
                counts["pairs"] += 1
                G = mul(J, shift(J, 1))
                if remainder(G, F1):
                    continue
                counts["first_condition"] += 1
                if remainder(mul(G, shift(J, 2)), F2):
                    continue
                counts["both_conditions"] += 1
                assert J in trivial  # Exceptional leading coefficient is >=216.
                counts["nontrivial_pairs"] += J not in trivial
            counts["F_polynomials"] += 1
    assert counts["pairs"] == 670761
    assert counts["both_conditions"] == 4 * counts["F_polynomials"]
    return counts


def audit_integrality_and_exception():
    integral = 0
    for a in range(1, 361):
        F = [Q(2), Q(9 * a, 2), Q(9 * a * a, 2), Q(a ** 3)]
        J = [Q(2), Q(23 * a, 6), Q(13 * a * a, 6), Q(a ** 3, 3)]
        all_integral = all(c.denominator == 1 for c in F + J)
        assert all_integral == (a % 6 == 0)
        integral += all_integral
    identities = 0
    for h in range(1, 61):
        F = [2, 27 * h, 162 * h * h, 216 * h ** 3]
        J = [2, 23 * h, 78 * h * h, 72 * h ** 3]
        complement = [f - j for f, j in zip(F, J)]
        assert all(0 <= j <= f for j, f in zip(J, F))
        for K in (J, complement):
            G = mul(K, shift(K, 1))
            quotient1, R1 = rational_division(G, shift(F, 1))
            quotient2, R2 = rational_division(mul(G, shift(K, 2)), shift(F, 2))
            assert not R1 and not R2
            assert all(c.denominator == 1 for c in quotient1)
            assert all((27 * c).denominator == 1 for c in quotient2)
            assert quotient2[0].denominator == 27
            identities += 2
        E = mul(mul([2, 3 * h], [1, 6 * h]),
                mul([1, 21 * h, 36 * h * h], [23, 78 * h, 72 * h * h]))
        assert [27 * c for c in mul(mul(J, shift(J, 1)), shift(J, 2))] == mul(shift(F, 2), E)
        assert E[0] % 3 == 1 and all(e % 3 == 0 for e in E[1:])
        assert F[0] % 3 == 2 and all(f % 3 == 0 for f in F[1:])
    return dict(scale_cases=360, integral_scales=integral,
                polynomial_division_identities=identities, exception_scales=60)


def audit_common_three():
    def v3(n):
        e = 0
        while n % 3 == 0:
            n //= 3
            e += 1
        return e

    def factorial_valuation(n, p):
        total = 0
        while n:
            n //= p
            total += n
        return total

    def binomial_valuation(n, j, p):
        return factorial_valuation(n, p) - factorial_valuation(j, p) - factorial_valuation(n - j, p)

    count = 0
    for h, x in product(range(1, 33), repeat=2):
        y = h * x
        n = 216 * y ** 3 + 162 * y * y + 27 * y + 2
        j = 72 * y ** 3 + 78 * y * y + 23 * y + 2
        assert 4 <= j <= n // 2 and n % 3 == 2
        assert v3(j * (j - 1) * (j - 2)) == v3(n - 2) - 3
        assert binomial_valuation(n, 3, 3) >= 2
        assert binomial_valuation(n, j, 3) >= 1
        assert binomial_valuation(n, n - j, 3) >= 1
        count += 1
    return dict(integer_specializations=count, common_prime=3,
                compatible_with_n_equal_three_times_power_of_two=False)


def main():
    if not __debug__:
        raise RuntimeError("Run without -O.")
    result = dict(
        scope="Supplementary exact checks of the complete cubic polynomial classification; not a solution of i=3.",
        normalized_classification=audit_nine_cases(),
        trace_identities=audit_trace_and_remainder(),
        bounded_coefficient_search=audit_bounded_coefficients(),
        exception_integrality=audit_integrality_and_exception(),
        common_prime=audit_common_three(),
    )
    path = artifact_path("verification_i3_cubic_digit_classification.json")
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
