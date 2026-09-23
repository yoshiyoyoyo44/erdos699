"""Exact finite diagnostics for the conditional, all-degree digit descent.

The note supplies the unbounded proof. These tests neither prove that a
descent base always exists nor assert that the artificial lifts are candidates.
Only Python's standard library is used.
"""

import json
from math import comb, gcd, lcm

from repo_paths import artifact_path


def factor(n):
    result = {}
    q = 2
    while q*q <= n:
        while n % q == 0:
            result[q] = result.get(q, 0)+1
            n //= q
        q = 3 if q == 2 else q+2
    if n > 1:
        result[n] = result.get(n, 0)+1
    return result


def valuation(n, q):
    assert n > 0
    e = 0
    while n % q == 0:
        n //= q
        e += 1
    return e


def choose_three_v(n, q):
    assert n >= 3
    return sum(valuation(n-r, q) for r in range(3))-valuation(6, q)


def legendre_binomial_v(n, j, q):
    """Independent factorial-floor formula, also usable for huge inputs."""
    assert 0 <= j <= n
    k = n-j
    total = 0
    while n:
        n, j, k = n//q, j//q, k//q
        total += n-j-k
    return total


def carry_levels(n, j, q):
    result = []
    power, k = q, 1
    while power <= n:
        if j % power > n % power:
            result.append(k)
        power *= q
        k += 1
    return result


def modulus(h):
    m = 8
    for q in factor(comb(h, 3)):
        if q == 2:
            continue
        power = q
        while power*q <= h:
            power *= q
        m *= power
    return m


def digit_sum(n, base):
    total = 0
    while n:
        n, remainder = divmod(n, base)
        total += remainder
    return total


def audit_valuation_transfer(limit=192):
    row_pairs = valuation_checks = lifted_checks = certificate_checks = 0
    max_shared_power = 0
    examples = {}
    small_lcm = 1
    for h in range(1, limit+1):
        small_lcm = lcm(small_lcm, h)
        if h < 4:
            continue
        m = modulus(h)
        if h >= 8:
            assert small_lcm % m == 0
        primes = [q for q in factor(comb(h, 3)) if q != 2]
        for a in range(h+1):
            row_pairs += 1
            source_binomial = comb(h, a)
            for q in primes:
                source_3 = valuation(comb(h, 3), q)
                source_a = valuation(source_binomial, q)
                levels = carry_levels(h, a, q)
                assert source_3 == choose_three_v(h, q)
                assert source_a == len(levels) == legendre_binomial_v(h, a, q)
                valuation_checks += 1
                shared = min(source_3, source_a)
                max_shared_power = max(max_shared_power, shared)
                for row_multiple, index_multiple in ((3, 1), (5, 2)):
                    n, j = h+row_multiple*m, a+index_multiple*m
                    target_3 = choose_three_v(n, q)
                    target_a = legendre_binomial_v(n, j, q)
                    assert 0 <= j <= n and n > h
                    assert target_3 >= source_3
                    assert target_a >= source_a
                    assert min(target_3, target_a) >= shared
                    lifted_checks += 1
                if not shared:
                    continue
                e = max(levels[0], 2 if q == 3 else 1)
                qe = q**e
                assert qe <= h
                # Use just the local certificate modulus, not the full M(h).
                n, j = h+3*qe, a+qe
                assert gcd(n-h, j-a) % qe == 0
                assert choose_three_v(n, q) >= 1
                assert legendre_binomial_v(n, j, q) >= 1
                certificate_checks += 1
                sample = {"H": h, "A": a, "q": q,
                          "first_carry_level": levels[0], "certificate_exponent": e,
                          "shared_exponent": shared}
                if q == 3 and levels[0] == 1:
                    examples.setdefault("3_requires_modulus_9", sample)
                if shared >= 3:
                    examples.setdefault("shared_cube_or_higher", sample)
    assert max_shared_power >= 3 and len(examples) == 2
    return {"H_range": [4, limit], "all_indices_in_each_row": True,
            "row_index_pairs": row_pairs, "source_valuation_checks": valuation_checks,
            "lifted_valuation_checks": lifted_checks,
            "local_certificate_checks": certificate_checks,
            "maximum_shared_prime_exponent": max_shared_power, "examples": examples}


def audit_grouped_digits():
    checks = strict_decreases = 0
    for p in (3, 5, 7, 11, 13):
        for degree in range(2, 19):
            for pattern in range(4):
                f = [(i*i+pattern+2) % p for i in range(degree+1)]
                f[-1] = 1+pattern % (p-1)
                g = [(i+pattern) % (v+1) for i, v in enumerate(f)]
                n = sum(v*p**i for i, v in enumerate(f))
                j = sum(v*p**i for i, v in enumerate(g))
                assert legendre_binomial_v(n, j, p) == 0
                for d in range(1, degree+1):
                    base = p**d
                    h, a, b = (digit_sum(z, base) for z in (n, j, n-j))
                    assert h == a+b
                    assert n >= base and h < n
                    assert (n-h) % (base-1) == (j-a) % (base-1) == 0
                    checks += 1
                    strict_decreases += int(h < n)
    return {"primes": [3, 5, 7, 11, 13], "degrees": [2, 18],
            "grouped_digit_checks": checks, "strict_decreases": strict_decreases}


def audit_unbounded_family(sample_count=24):
    j0 = 1+11**2+2*11**4
    assert j0 == 29404 and j0 % 56 == 4 and pow(11, 6, 56) == 1
    assert modulus(8) == 56
    for m in range(1, sample_count+1):
        n, j = j0*(1+11**(6*m)), j0
        h, a = digit_sum(n, 11), digit_sum(j, 11)
        assert (h, a) == (8, 4)
        assert n % 11 == 1 and choose_three_v(n, 11) >= 1
        assert legendre_binomial_v(n, j, 11) == 0
        assert gcd(n-h, j-a) % modulus(h) == 0
        assert (11-1) % modulus(h) != 0
        assert choose_three_v(n, 7) >= 1
        assert legendre_binomial_v(n, j, 7) >= 1
        assert 4 <= j <= n//2 and h*h > 11
    return {"samples": sample_count, "maximum_digit_degree": 6*sample_count+4,
            "base": 11, "H": 8, "A": 4, "lifted_prime": 7,
            "base_minus_one_condition_fails": True,
            "claim": "finite diagnostics of the proved infinite non-counterexample family"}


def audit_range_and_modulus(limit=512):
    rows = 0
    for h in range(8, limit+1, 8):
        b3 = comb(h, 3)
        odd_b3 = b3 >> valuation(b3, 2)
        h_odd = h >> valuation(h, 2)
        m = modulus(h)
        assert valuation(b3, 2) == valuation(h, 2)
        assert 6*odd_b3 == h_odd*(h-1)*(h-2)
        assert m % (8*odd_b3) == 0
        if h >= 16:
            assert 8*odd_b3 > h*h
        q = next(q for q in factor(h-1) if q >= 5)
        for a in (2, 3):
            assert gcd(b3, comb(h, a)) % q == 0
        rows += 1
    assert factor(57) == {3: 1, 19: 1}
    # Examples where the stronger sufficient condition does hold.
    strong_examples = []
    for p, d in ((113, 1), (13, 2)):
        base = p**d
        n, j = 1+6*base+base*base, 4*base
        h, a = digit_sum(n, base), digit_sum(j, base)
        assert (h, a) == (8, 4) and (base-1) % modulus(h) == 0
        assert legendre_binomial_v(n, j, p) == 0
        assert gcd(n-h, j-a) % modulus(h) == 0
        assert h*h < base
        if d == 2:
            z, position = n, 0
            while z:
                z, v = divmod(z, p)
                assert position % 2 == 0 or v == 0
                position += 1
        strong_examples.append({"p": p, "d": d, "H": h, "A": a})
    return {"multiples_of_8_checked": rows, "maximum_H": limit,
            "strong_condition_examples": strong_examples}


def main():
    result = {
        "status": "passed",
        "scope": "conditional all-degree descent; existence of a usable base remains unproved",
        "valuation_transfer": audit_valuation_transfer(),
        "grouped_digits": audit_grouped_digits(),
        "unbounded_family": audit_unbounded_family(),
        "range_and_modulus": audit_range_and_modulus(),
    }
    path = artifact_path("verification_i3_uniform_digit_descent.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n",
                    encoding="utf-8", newline="\n")
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
