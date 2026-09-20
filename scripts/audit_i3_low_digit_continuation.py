"""Exact finite audits for i3_low_digit_continuation_2026-09-19.md.

The unbounded assertions are proved in the accompanying note. These finite
audits exercise their hypotheses and record a counterexample to an incomplete
local inference in the supplied handoff. They do not solve Erdos 699.
Python standard library only; run without -O.
"""
from repo_paths import artifact_path

import hashlib
import json
from itertools import product
from math import gcd
from pathlib import Path


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def primes_below(n):
    sieve = bytearray(b"\1") * n
    sieve[:2] = b"\0\0"
    for p in range(2, n):
        if sieve[p]:
            for m in range(p * p, n, p):
                sieve[m] = 0
    return [p for p in range(3, n) if sieve[p]]


def digits(n, p):
    result = []
    while n:
        n, d = divmod(n, p)
        result.append(d)
    return result


def digit_data(n, p):
    d = digits(n, p)
    even = sum(d[::2])
    odd = sum(d[1::2])
    return even + odd, even - odd


def has_other_odd_factor(n, p):
    n >>= v2(n)
    while n % p == 0:
        n //= p
    return n > 1


def check_single_numbers():
    counts = dict(numbers=0, two_adic_bound=0, alternating_bound=0,
                  weight_two=0, weight_four=0)
    for p in primes_below(60):
        w = v2(p + 1)
        for z in range(1, 50001):
            s, alt = digit_data(z, p)
            v = v2(z)
            counts["numbers"] += 1
            assert (z - s) % (p - 1) == 0
            assert (z - alt) % (p + 1) == 0
            assert abs(alt) <= s
            assert s >= 1 << min(v, v2(p - 1))
            counts["two_adic_bound"] += 1
            if w > v:
                assert s >= 1 << v
            else:
                assert z % (p + 1) == 0 or s >= 1 << w
            counts["alternating_bound"] += 1
            if v < 3:
                continue
            if s == 2:
                assert p % 4 == 3 and w == v
                assert z % (p + 1) == 0
                counts["weight_two"] += 1
            if s == 4 and p % 4 == 3:
                assert alt == 0
                assert z % (p + 1) == 0
                assert v > w
                assert z % (p * p - 1) == 2 * (p + 1) % (p * p - 1)
                counts["weight_four"] += 1
    return counts


def check_reciprocity():
    counts = dict(prime_pairs=0, odd_negative_power_pairs=0,
                  delta_residues=0)
    ps = primes_below(200)
    ls = primes_below(1000)
    for p in ps:
        if p % 4 != 3:
            continue
        for ell in ls:
            if p == ell:
                continue
            counts["prime_pairs"] += 1
            odd_part = (ell - 1) >> v2(ell - 1)
            # This is equivalent to the existence of an odd r with p^r=-1.
            if pow(p, odd_part, ell) == ell - 1:
                assert pow(ell, (p - 1) // 2, p) == 1
                counts["odd_negative_power_pairs"] += 1
        for delta in (1, 3):
            if delta % p == 0:
                continue
            if pow(-delta % p, (p - 1) // 2, p) == 1:
                assert delta == 3 and p % 12 == 7
            counts["delta_residues"] += 1
    return counts


def check_carry_free_splits():
    """Exhaust all digit partitions for each selected low-weight total.

    U ranges over odd integers, not just prime powers. No factorization or
    primality assumption is imposed on U. gcd(U, 3p)=1 in the gamma=3 branch.
    This is a finite audit of local necessary conditions, not a list of
    counterexample candidates satisfying Q1 and Q2.
    """
    counts = dict(totals=0, low_weight_totals=0, partitions=0,
                  equal_valuations=0, normalized_splits=0,
                  balanced_eight=0, center_congruences=0,
                  center_exceptions=0, gamma3_coprime3=0,
                  nontrivial_U=0)
    examples = []
    digest = hashlib.sha256()
    for p in primes_below(100):
        for gamma in (1, 3):
            if p == 3 and gamma == 3:
                continue
            for U in range(1, 200, 2):
                if gcd(U, p * gamma) != 1:
                    continue
                for u in range(4, 33):
                    N = gamma * U * (1 << u)
                    ds = digits(N, p)
                    total = sum(ds)
                    counts["totals"] += 1
                    if total not in (4, 6, 8, 10, 12):
                        continue
                    counts["low_weight_totals"] += 1
                    terms = [(p ** i, d) for i, d in enumerate(ds) if d]
                    for part in product(*(range(d + 1) for _, d in terms)):
                        sx = sum(part)
                        sy = total - sx
                        if sx < 2 or sy < 2 or sx % 2 or sy % 2:
                            continue
                        X = sum(a * q for a, (q, _) in zip(part, terms))
                        Y = N - X
                        if not 0 < X < Y:
                            continue
                        counts["partitions"] += 1
                        v = v2(X)
                        if v < 3 or v >= u or v2(Y) != v:
                            continue
                        counts["equal_valuations"] += 1
                        # No weight-six sum can have the two exact valuations.
                        assert total != 6
                        assert total >= 1 << (1 + min(v, v2(p - 1)))
                        if X % U or Y % U:
                            continue
                        eps = gcd(X // U // (1 << v), gamma)
                        assert gcd(X, Y) == U * (1 << v) * eps
                        counts["normalized_splits"] += 1
                        if U > 1:
                            counts["nontrivial_U"] += 1
                        if sx == sy == 4:
                            counts["balanced_eight"] += 1
                            modulus = p * p - 1
                            if (X - Y) % modulus == 0:
                                counts["center_congruences"] += 1
                            else:
                                assert p == 5 and gamma == 3 and eps == 1
                                assert (X - Y) % 24 in (8, 16)
                                counts["center_exceptions"] += 1
                                if len(examples) < 8:
                                    examples.append(dict(p=p, gamma=gamma, U=U,
                                                         u=u, v=v, X=X, Y=Y))
                            if p % 4 == 3:
                                assert v > v2(p + 1)
                                odd = (p + 1) >> v2(p + 1)
                                assert U * eps % odd == 0
                                assert gcd(U, p - 1) == 1
                                if gamma == 3:
                                    assert eps == 3
                        if gamma == 3 and eps == 1:
                            counts["gamma3_coprime3"] += 1
                            assert total >= (8 if p == 5 else 12)
                        digest.update(f"{p},{gamma},{U},{u},{X},{Y}\n".encode())
    assert counts["gamma3_coprime3"] > 0
    assert counts["center_congruences"] > 0
    assert counts["center_exceptions"] > 0
    return dict(counts=counts, exceptional_local_examples=examples,
                normalized_record_sha256=digest.hexdigest())


def explicit_handoff_gap():
    # Both numbers have nontrivial odd factors outside p. This example tests
    # the local inference only: it does not satisfy the full Q1/Q2 conditions
    # or the established u>=49 bound for a counterexample to Erdos 699.
    p, gamma, U, u, X, Y = 5, 3, 1, 9, 760, 776
    assert X == 5 ** 4 + 5 ** 3 + 2 * 5
    assert Y == 5 ** 4 + 5 ** 3 + 5 ** 2 + 1
    assert digit_data(X, p) == (4, -2)
    assert digit_data(Y, p) == (4, 2)
    assert v2(X) == v2(Y) == 3
    assert gcd(X, Y) == 8
    assert has_other_odd_factor(X, p) and has_other_odd_factor(Y, p)
    assert X + Y == gamma * U * (1 << u)
    assert sum(digits(X + Y, p)) == 8
    assert (X - Y) % 24 == 8
    # Take e=1 to translate to center variables, still only a local model.
    n, j = 5 * (X + Y), 5 * X
    c = n // 2 - j
    assert c == 40 and c // 5 == 8 and (c // 5) % 12 != 0
    assert X * Y % (n - 1) != 0
    return dict(p=p, gamma=gamma, U=U, u=u, X=X, Y=Y,
                n=n, j=j, c=c, c_over_p=c // p,
                scope="Local inference only; not an Erdos 699 counterexample")


def trial_factors(n):
    out = {}
    p = 2
    while p * p <= n:
        while n % p == 0:
            out[p] = out.get(p, 0) + 1
            n //= p
        p += 1
    if n > 1:
        out[n] = out.get(n, 0) + 1
    return out


def check_stronger_order_obstruction():
    count = 0
    for p in primes_below(42):
        if p % 3 != 2:
            continue
        for a in (2, 4, 6, 8):
            for c in (1, 3):
                D = (1 << a) * p ** c - 1
                assert D % 4 == 3 and D % 3 == 1
                fs = trial_factors(D)
                witness = next(q for q, f in fs.items()
                               if q % 4 == 3 and f % 2 == 1)
                assert witness != 3
                # The exponent is odd, so this proves odd order without
                # trusting a multiplicative-order library.
                assert pow(p, (witness - 1) // 2, witness) == 1
                for h in range(4):
                    u, e = a * (1 << h), c * (1 << h)
                    assert v2(u) >= v2(e) + 1
                    assert (pow(2, u, witness) * pow(p, e, witness) - 1) % witness == 0
                    count += 1
    # Pure T=5^e, odd part of u equal to 7: the size condition forces
    # e=2^t, hence 71 | 640^(2^t)-1 for every t>=0.
    assert 5 ** 3 < 2 ** 7 < 5 ** 6
    assert trial_factors(71) == {71: 1}
    assert (640 - 1) % 71 == 0 and pow(5, 5, 71) == 1
    assert 5 % 71 != 1
    return dict(cases=count, p5_odd_part_7=dict(prime=71, odd_order=5,
                                              base=640))


def main():
    if not __debug__:
        raise RuntimeError("Run with assertions enabled (without -O).")
    result = dict(
        scope="Finite audits supporting the unbounded proofs in the note; "
              "no global finite exclusion or full solution is asserted.",
        single_numbers=check_single_numbers(),
        reciprocity=check_reciprocity(),
        stronger_order_obstruction=check_stronger_order_obstruction(),
        carry_free_splits=check_carry_free_splits(),
        handoff_inference_gap=explicit_handoff_gap(),
    )
    target = artifact_path("verification_i3_low_digit_continuation.json")
    target.write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n",
                      encoding="utf-8")
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    main()
