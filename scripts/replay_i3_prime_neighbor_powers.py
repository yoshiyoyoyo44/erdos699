"""Independently replay prime-neighbor power certificates (standard library).

Includes finite algebra audits of the universal proof. These audits do not
replace the unbounded argument given in the accompanying mathematical note.
"""
from repo_paths import artifact_path

import hashlib
import json
from itertools import product
from math import comb, gcd, isqrt, prod
from pathlib import Path


def prime_by_trial(n):
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    return all(n % q for q in range(3, isqrt(n) + 1, 2))


def valuation(n, p):
    e = 0
    while n % p == 0:
        n //= p
        e += 1
    return e


def polynomial_remainder(B):
    m = len(B)
    R = [-b for b in B]
    for s, a in enumerate(B):
        for t, b in enumerate(B):
            R[(s + t) % m] += a * b
    return R


def audit_polynomials():
    counts = dict(digit_polynomials=0, zero_remainders=0,
                  signed_coefficient_polynomials=0)
    for m in range(1, 6):
        H = 3 ** m - 2 ** m
        K = H * (H + 1)
        for A in product(*(range(comb(m, r) + 1) for r in range(m))):
            # B(x)=A(x-1), with degree below m.
            B = [sum(A[r] * comb(r, s) * (-1) ** (r - s)
                     for r in range(s, m)) for s in range(m)]
            assert sum(abs(b) for b in B) <= H
            R = polynomial_remainder(B)
            assert sum(abs(r) for r in R) <= K
            zero = not any(R)
            assert zero == (A[0] in (0, 1) and not any(A[1:]))
            counts["digit_polynomials"] += 1
            counts["zero_remainders"] += zero
            # Evaluate the remainder at a point beyond the proved bound.
            x = 3 * K + 2
            value = sum(r * x ** s for s, r in enumerate(R))
            assert abs(3 * value) < x ** m - 1
            assert (value == 0) == zero
    for m in range(1, 7):
        for B in product(range(-2, 3), repeat=m):
            zero = not any(polynomial_remainder(B))
            assert zero == (B[0] in (0, 1) and not any(B[1:]))
            counts["signed_coefficient_polynomials"] += 1
    return counts


def convolution(A, B):
    result = [0] * (len(A) + len(B) - 1)
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            result[i + j] += a * b
    return result


def remainder_at_power(poly, m, value):
    result = [0] * m
    for degree, coefficient in enumerate(poly):
        result[degree % m] += coefficient * value ** (degree // m)
    return result


def audit_fixed_cofactor_polynomials():
    counts = dict(polynomials=0, simultaneous_zero_remainders=0)
    for a in range(1, 4):
        for m in range(1, 4):
            A = a ** m
            H = (3 * a) ** m
            K1 = H * (H + A)
            K2 = 8 * H * (H + A) * (H + 2 * A)
            L = a * H + 6 * K2 + 3
            for coeffs in product(*(range(comb(m, r) * a ** r + 1)
                                    for r in range(m + 1))):
                # C(x)=a^m*J((x-1)/a) is an integer polynomial.
                C = [sum(coeffs[r] * a ** (m - r) * comb(r, s)
                         * (-1) ** (r - s) for r in range(s, m + 1))
                     for s in range(m + 1)]
                assert sum(abs(c) for c in C) <= H
                C1, C2 = list(C), list(C)
                C1[0] -= A
                C2[0] -= 2 * A
                R1 = remainder_at_power(convolution(C, C1), m, 1)
                R2 = remainder_at_power(convolution(convolution(C, C1), C2), m, 2)
                assert sum(abs(r) for r in R1) <= K1
                assert sum(abs(r) for r in R2) <= K2
                if not any(R1) and not any(R2):
                    # Nonnegative bounded digit coefficients leave only
                    # j=0,1,n-1,n among the six algebraic possibilities.
                    assert C[1:m] == [0] * (m - 1)
                    assert (C[0], C[m]) in ((0, 0), (A, 0), (-A, A), (0, A))
                    counts["simultaneous_zero_remainders"] += 1
                x = L + 1
                v1 = sum(r * x ** d for d, r in enumerate(R1))
                v2 = sum(r * x ** d for d, r in enumerate(R2))
                assert abs(3 * v1) < x ** m - 1
                assert abs(6 * v2) < x ** m - 2
                assert (v1 == 0) == (not any(R1))
                assert (v2 == 0) == (not any(R2))
                counts["polynomials"] += 1
    return counts


def audit_general_four_power_remainder(bounds):
    # Exhaust the bounded primes directly; no prior u>=49 result is used.
    summaries = []
    small_pairs = 0
    for entry in bounds[:4]:
        m, maximum = entry["m"], entry["bound"]
        for p in (2, 3):
            n = (p + 1) ** m
            for j in range(4, n // 2 + 1):
                D = gcd(comb(n, 3), comb(n, j))
                while D % 2 == 0:
                    D //= 2
                assert D > 1
                small_pairs += 1
        prime_count = candidate_count = 0
        for p in range(5, maximum):
            if not prime_by_trial(p):
                continue
            prime_count += 1
            n = (p + 1) ** m
            digits, t = [], n
            while t:
                digits.append(t % p)
                t //= p
            assert sum(d * p ** r for r, d in enumerate(digits)) == n
            assert comb(n, 3) % p == 0
            for coeffs in product(*(range(d + 1) for d in digits)):
                j = sum(c * p ** r for r, c in enumerate(coeffs))
                if not 4 <= j <= n // 2:
                    continue
                candidate_count += 1
                if 3 * j * (j - 1) % (n - 1):
                    continue
                assert n % 4 == 0
                assert 6 * j * (j - 1) * (j - 2) % (n - 2) != 0
        summaries.append(dict(m=m, primes=prime_count,
                              digit_candidates=candidate_count, survivors=0))
    return dict(small_prime_direct_pairs=small_pairs,
                total_digit_candidates=sum(r["digit_candidates"] for r in summaries),
                per_m=summaries)


def main():
    if not __debug__:
        raise RuntimeError("Run without -O.")
    source = artifact_path("i3_prime_neighbor_power_certificate.json")
    data = json.loads(source.read_text(encoding="utf-8"))
    assert data["max_multiplier"] == 8
    expected_bounds = []
    cases = []
    for m in range(1, 9):
        H = 3 ** m - 2 ** m
        maximum = 3 * H * (H + 1) + 1
        expected_bounds.append(dict(m=m, H=H, bound=maximum))
        k = 2
        while 1 << k <= maximum:
            if prime_by_trial((1 << k) - 1):
                cases.append(dict(m=m, k=k, u=m * k))
            k += 1
    assert data["analytic_bounds"] == expected_bounds
    assert data["bounded_mersenne_cases"] == cases
    expected_u = {c["u"] for c in cases if c["u"] >= 3}
    rows = {r["u"]: r for r in data["rows"]}
    assert len(rows) == len(data["rows"]) and set(rows) == expected_u
    certificates = data["prime_certificates"]
    proved = {2}

    def prove_prime(p):
        if p in proved:
            return
        assert isinstance(p, int) and p > 2
        entry = certificates[str(p)]
        fs = entry["factors"]
        assert len({q for q, _ in fs}) == len(fs)
        assert all(isinstance(q, int) and isinstance(e, int) and 2 <= q < p
                   and e > 0 for q, e in fs)
        assert prod(q ** e for q, e in fs) == p - 1
        witnesses = dict(entry["witnesses"])
        assert len(witnesses) == len(entry["witnesses"])
        assert set(witnesses) == {q for q, _ in fs}
        for q, _ in fs:
            prove_prime(q)
            a = witnesses[q]
            assert isinstance(a, int) and 1 < a < p
            assert pow(a, p - 1, p) == 1
            assert gcd(pow(a, (p - 1) // q, p) - 1, p) == 1
        proved.add(p)

    summaries = []
    digest = hashlib.sha256()
    for u in sorted(expected_u):
        n = 1 << u
        Q1 = (n - 1) // (3 if valuation(n - 1, 3) == 1 else 1)
        Q2 = (n // 2 - 1) // (3 if valuation(n // 2 - 1, 3) == 1 else 1)
        factors = rows[u]["Q1_factors"]
        assert len({p for p, _ in factors}) == len(factors)
        assert all(isinstance(e, int) and e > 0 for _, e in factors)
        assert prod(p ** e for p, e in factors) == Q1
        for p, _ in factors:
            prove_prime(p)
        # Construct CRT residues by iterative lifting, different from the
        # generator's factor-partition formula.
        residues, modulus = [0], 1
        for p, e in factors:
            q = p ** e
            inv = pow(modulus, -1, q)
            residues = [r + modulus * ((b - r) * inv % q)
                        for r in residues for b in (0, 1)]
            modulus *= q
        assert modulus == Q1
        assert len(set(residues)) == 2 ** len(factors)
        candidates = set()
        for r in residues:
            lo = max(0, (4 - r + Q1 - 1) // Q1)
            hi = (n // 2 - r) // Q1
            for t in range(lo, hi + 1):
                j = r + t * Q1
                assert 4 <= j <= n // 2 and j * (j - 1) % Q1 == 0
                assert j * (j - 1) * (j - 2) % Q2 != 0
                candidates.add(j)
        assert len(candidates) == rows[u]["CRT_candidates"]
        for j in sorted(candidates):
            digest.update(f"{u},{j}\n".encode())
        summaries.append(dict(u=u, CRT_candidates=len(candidates), survivors=0))
    result = dict(
        scope="Unbounded families use the paper proof plus this finite remainder. "
              "This is not a complete solution of i=3.",
        dependency="Only the elementary Kummer and divisibility lemmas in the note.",
        bounded_cases=len(cases),
        remainder_rows=len(rows),
        CRT_candidates=sum(r["CRT_candidates"] for r in summaries),
        primes_recursively_verified=len(proved),
        CRT_record_sha256=digest.hexdigest(),
        general_four_power_remainder=audit_general_four_power_remainder(expected_bounds),
        polynomial_audits=audit_polynomials(),
        fixed_cofactor_polynomial_audits=audit_fixed_cofactor_polynomials(),
        per_u=summaries,
    )
    out = artifact_path("verification_i3_prime_neighbor_powers.json")
    out.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
