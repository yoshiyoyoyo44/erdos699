"""Exact local audits for the September 20 complement-digit bounds.

The note proves the unrestricted statements. These audits test boundary cases
and sparse additions, not a complete range of Erdos 699 counterexamples.
"""

import hashlib
import json
from itertools import combinations_with_replacement
from pathlib import Path

from audit_i3_low_digit_continuation import digits, primes_below, v2


def audit_complement_congruence():
    counts = dict(numbers=0, low_digit_cases=0)
    digest = hashlib.sha256()
    for p in primes_below(200):
        w = v2(p + 1)
        if w < 3:
            continue
        for u in range(w + 1, w + 9):
            for M in range(1, 64, 2):
                for c in (1, 2):
                    Z = (M << u) - c
                    ds = digits(Z, p)
                    D, O = sum(ds), sum(ds[1::2])
                    modulus = 1 << (w + 1)
                    assert Z % modulus == (D - 2 * O + (O << w)) % modulus
                    counts["numbers"] += 1
                    if D <= (1 << w) - c:
                        assert (D + c) % 4 == 0
                        counts["low_digit_cases"] += 1
                        digest.update(f"{p},{u},{M},{c},{D}\n".encode())
    assert counts["low_digit_cases"] > 0
    return dict(counts=counts, record_sha256=digest.hexdigest())


def sparse_numbers(p, weight, places=6):
    return [sum(p ** a for a in exponents)
            for exponents in combinations_with_replacement(range(places), weight)]


def audit_low_digit_block_additions():
    counts = dict(Q1_weight_five_additions=0, Q2_weight_four_additions=0,
                  Q1_equal_valuation_boundary=0, Q2_equal_valuation_boundary=0)
    examples = {}
    for p in primes_below(100):
        w = v2(p + 1)
        if w < 3:
            continue
        twos = sparse_numbers(p, 2)
        threes = sparse_numbers(p, 3)
        marked = [X for X in twos if v2(X) >= 3]
        other_twos = [Y for Y in twos if v2(Y) == 1]
        assert all(v2(X) == w for X in marked)
        for X in marked:
            for Y in threes:
                assert Y % 2 == 1
                N = X + Y
                assert sum(digits(N, p)) == 5
                for e in range(1, 5):
                    n = p ** e * N + 1
                    assert v2(n) <= w
                    counts["Q1_weight_five_additions"] += 1
                    if v2(n) == w:
                        counts["Q1_equal_valuation_boundary"] += 1
                        examples.setdefault("Q1", dict(p=p, e=e, X=X, Y=Y,
                                                       n=n, u=v2(n), v=w))
            for Y in other_twos:
                N = X + Y
                assert sum(digits(N, p)) == 4
                for e in range(1, 5):
                    n = p ** e * N + 2
                    assert v2(n) <= w
                    counts["Q2_weight_four_additions"] += 1
                    if v2(n) == w:
                        counts["Q2_equal_valuation_boundary"] += 1
                        examples.setdefault("Q2", dict(p=p, e=e, X=X, Y=Y,
                                                       n=n, u=v2(n), v=w))
    assert all(counts.values())
    return dict(counts=counts, local_boundary_examples=examples)


def audit_necessary_hypotheses():
    # At v=2 the two low digit patterns exist even with u>v.
    # These are local models, not full counterexamples to Erdos 699.
    p, e = 11, 1
    X, Y = 12, 33
    n = p ** e * (X + Y) + 1
    assert sum(digits(X, p)) == 2 and sum(digits(Y, p)) == 3
    assert sum(digits(X + Y, p)) == 5
    assert v2(X) == 2 and v2(n) > 2
    q1 = dict(p=p, e=e, X=X, Y=Y, n=n, u=v2(n), v=2)
    X, Y = 12, 22
    n = p ** e * (X + Y) + 2
    assert sum(digits(X + Y, p)) == 2 + 2 == 4
    assert v2(X) == 2 and v2(Y) == 1 and v2(n) > 2
    q2 = dict(p=p, e=e, X=X, Y=Y, n=n, u=v2(n), v=2)
    # The next possible digit weight above 2^w-c can fail the conclusion.
    p = 7
    boundaries = []
    for c, n in ((1, 112), (2, 64)):
        D = sum(digits(n - c, p))
        assert v2(n) > v2(p + 1)
        assert D == (1 << v2(p + 1)) - c + 2
        assert (D + c) % 4 != 0
        boundaries.append(dict(p=p, n=n, c=c, D=D))
    return dict(valuation_two_local_models=dict(Q1=q1, Q2=q2),
                beyond_digit_threshold_examples=boundaries)


def main():
    if not __debug__:
        raise RuntimeError("Run without -O.")
    result = dict(
        scope="Local finite audits; no complete counterexample search.",
        complement_congruence=audit_complement_congruence(),
        low_digit_additions=audit_low_digit_block_additions(),
        necessary_hypotheses=audit_necessary_hypotheses(),
    )
    path = Path(__file__).with_name("verification_i3_complement_digit_bounds.json")
    path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()
