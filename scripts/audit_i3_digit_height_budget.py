"""Audit the all-prime digit-height budget and polynomial factor degrees.

The unbounded results are proved in the accompanying note. Composed polynomial
examples below are diagnostics, not counterexamples to Erdos problem 699 and
not an exhaustive classification. Requires SymPy.
"""

import json
from itertools import product

import sympy as sp

from repo_paths import artifact_path


def audit_symbolic_identities():
    identities = []

    def check(name, expression):
        assert sp.expand(expression) == 0, name
        identities.append(name)

    w = sp.symbols("w0:3")
    y = sp.symbols("y0:3")
    mass = sum(w)
    first = sum(wi * yi for wi, yi in zip(w, y))
    second = sum(wi * yi**2 for wi, yi in zip(w, y))
    variance = sum(w[i] * w[j] * (y[i] - y[j])**2
                   for i in range(3) for j in range(i + 1, 3))
    check("weighted Cauchy identity", mass * second - first**2 - variance)

    a, b, M, d, ell = sp.symbols("a b M d ell")
    C = 2 * a * M**2 + b * M
    f = ell**2 - C * ell - 2 * a * M**2 * d
    check("quadratic at C+d", f.subs(ell, C + d) - d * (M*b + d))
    z = sp.symbols("z")
    check("quadratic past C+d", f.subs(ell, C+d+z)
          - (d*(M*b+d) + z*(C+2*d) + z**2))

    # z stands for F-2. The remainder identity holds in an abstract ring;
    # it is not tested only on a finite list of digit polynomials.
    U, L = sp.symbols("U L")
    UJ = U + (z + 1) * L
    numerator = sp.expand(UJ * (UJ-U) * (UJ-2*U))
    remainder = (L+U) * L * (L-U)
    quotient, rem = sp.div(numerator - remainder, z, z)
    check("F-2 transfer remainder", rem)
    check("F-2 transfer full identity", numerator - remainder - z*quotient)

    E, K = sp.symbols("E K")
    for s in range(3):
        # Here z stands for F-1, so DE=z-1.
        EJ = s*E + (z-1)*K
        numerator = sp.expand(EJ*(EJ-E))
        remainder = (s*E-K)*((s-1)*E-K)
        quotient, rem = sp.div(numerator - remainder, z, z)
        check(f"F-1 transfer remainder s={s}", rem)
        check(f"F-1 transfer full identity s={s}",
              numerator - remainder - z*quotient)

    F, J = sp.symbols("F J")
    check("complement at F=1", ((F-J)*(F-J-1)-J*(J-1)).subs(F, 1))
    check("complement at F=2",
          ((F-J)*(F-J-1)*(F-J-2)+J*(J-1)*(J-2)).subs(F, 2))
    return {"count": len(identities), "identities": identities}


def audit_integer_thresholds():
    checked = 0
    for H, m in product(range(1, 41), range(1, 21)):
        old = 6*H*(H+1)*(H+2)**(2*m+2) + 2
        new = 7*(H+2)**(2*m+4)
        assert old <= new
        checked += 1
    return {"integer_comparisons": checked,
            "fixed_multiplicity_exponents": {
                str(M): 2*M*M + 4*M for M in (1, 2, 3, 4, 10)}}


X = sp.symbols("X")


def poly(expression):
    return sp.Poly(expression, X, domain=sp.QQ)


def assert_coefficient_order(F, J):
    for k in range(F.degree()+1):
        assert 0 <= J.nth(k) <= F.nth(k)


def audit_compositions():
    rows = []
    for kind, degree, extra_linear in product(
            ("quadratic", "cubic"), range(1, 5), (False, True)):
        K = X**degree + (X if extra_linear else 0)
        if kind == "quadratic":
            F = poly(12*K**2 + 8*K + 2)
            J = poly(6*K**2 + K)
        else:
            F = poly(216*K**3 + 162*K**2 + 27*K + 2)
            J = poly(72*K**3 + 78*K**2 + 23*K + 2)
        for complement in (False, True):
            J0 = F-J if complement else J
            assert_coefficient_order(F, J0)
            assert J0 not in (poly(0), poly(1), F-1, F)
            assert (J0*(J0-1)).rem(F-1).is_zero
            assert (J0*(J0-1)*(J0-2)).rem(F-2).is_zero
            m = int(F.degree())
            U, V = (F-1).gcd(J0), (F-1).gcd(J0-1)
            assert U.gcd(V).degree() == 0
            assert (U*V).monic() == (F-1).monic()
            assert m <= 3*U.degree() <= 2*m
            assert m <= 3*V.degree() <= 2*m
            Ds = [(F-2).gcd(J0-s) for s in range(3)]
            assert sp.prod(Ds).monic() == (F-2).monic()
            assert all(2*D.degree() <= m for D in Ds)
            assert all(Ds[i].gcd(Ds[j]).degree() == 0
                       for i in range(3) for j in range(i+1, 3))
            rows.append({"family": kind, "inner_degree": degree,
                         "extra_linear_term": extra_linear,
                         "complement": complement, "m": m,
                         "F_minus_1_degrees": [int(U.degree()), int(V.degree())],
                         "F_minus_2_degrees": [int(D.degree()) for D in Ds]})
    return {"nontrivial_pairs": len(rows),
            "degrees": sorted({r["m"] for r in rows}), "rows": rows}


def can_partition(weights, bins, cap, lower=0):
    """Whole irreducible powers are indivisible items, including multiplicity."""
    totals = [0]*bins

    def visit(i):
        if i == len(weights):
            return all(lower <= total <= cap for total in totals)
        seen = set()
        for b in range(bins):
            if totals[b] in seen or totals[b]+weights[i] > cap:
                continue
            seen.add(totals[b])
            totals[b] += weights[i]
            found = visit(i+1)
            totals[b] -= weights[i]
            if found:
                return True
        return False

    return visit(0)


def whole_power_degrees(F):
    _, factors = sp.factor_list(F)
    return sorted((int(f.degree())*int(e) for f, e in factors), reverse=True)


def audit_factor_obstructions():
    # The first example has an irreducible linear+cubic split in F-1.
    # The second has a 2+2 split there, but X^3 cannot be split among the
    # three residues on the F-2 side. No integer counterexample is claimed.
    examples = [
        ("linear plus irreducible cubic", poly(2+3*X+3*X**2+4*X**3+4*X**4)),
        ("triple zero in F-2", poly(2+4*X**3+3*X**4)),
        ("surviving composed quadratic", poly(12*(X+X**2)**2+8*(X+X**2)+2)),
    ]
    rows = []
    for name, F in examples:
        m = int(F.degree())
        d1, d2 = whole_power_degrees(F-1), whole_power_degrees(F-2)
        ok1 = can_partition(d1, 2, (2*m)//3, (m+2)//3)
        ok2 = can_partition(d2, 3, m//2)
        rows.append({"name": name, "F_minus_1_whole_power_degrees": d1,
                     "F_minus_2_whole_power_degrees": d2,
                     "F_minus_1_partition_possible": ok1,
                     "F_minus_2_partition_possible": ok2})
    assert [(r["F_minus_1_partition_possible"], r["F_minus_2_partition_possible"])
            for r in rows] == [(False, True), (True, False), (True, True)]

    tables = {}
    for m in range(1, 25):
        f1 = [(a, m-a) for a in range(m+1)
              if a >= m-a and m <= 3*a <= 2*m and m <= 3*(m-a) <= 2*m]
        f2 = [(a, b, m-a-b) for a in range(m+1) for b in range(a+1)
              if 0 <= m-a-b <= b and 2*a <= m]
        tables[str(m)] = {"F_minus_1": f1, "F_minus_2": f2}
    assert tables["4"] == {"F_minus_1": [(2, 2)],
                            "F_minus_2": [(2, 1, 1), (2, 2, 0)]}
    assert tables["5"] == {"F_minus_1": [(3, 2)], "F_minus_2": [(2, 2, 1)]}
    assert tables["6"] == {"F_minus_1": [(3, 3), (4, 2)],
                            "F_minus_2": [(2, 2, 2), (3, 2, 1), (3, 3, 0)]}
    return {"diagnostics": rows, "degree_tables": tables}


def audit_aggregate_inequality():
    """Exact rational diagnostics for the general aggregation implication.

    y_i,a,M etc. are abstract rational inputs to (2), not logarithms obtained
    from a purported counterexample. The proof itself is the symbolic identity.
    """
    checked = 0
    for weights in product(range(1, 4), repeat=3):
        for heights in ((1, 2, 3), (2, 5, 11), (5, 7, 13)):
            M = sum(weights)
            ell = sum(w*y for w, y in zip(weights, heights))
            d = sp.Rational(1, 2)
            L = ell+d
            for a, c in product((sp.Rational(1, 2), sp.Rational(2)),
                                (sp.Rational(1), sp.Rational(3))):
                b = c+4*a
                if not all(y*y <= b*y+2*L*a for y in heights):
                    continue
                second = sum(w*y*y for w, y in zip(weights, heights))
                assert ell**2 <= M*second <= M*b*ell+2*L*a*M*M
                C = 2*a*M*M+b*M
                assert L < C+2*d
                checked += 1
    return {"rational_implication_diagnostics": checked}


def main():
    result = {
        "status": "passed",
        "scope": "general proofs in note; no general i=3 resolution claimed",
        "symbolic": audit_symbolic_identities(),
        "thresholds": audit_integer_thresholds(),
        "compositions": audit_compositions(),
        "factor_obstructions": audit_factor_obstructions(),
        "aggregation": audit_aggregate_inequality(),
    }
    path = artifact_path("verification_i3_digit_height_budget.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n",
                    encoding="utf-8", newline="\n")
    print(json.dumps({"status": result["status"], "output": str(path),
                      "symbolic_identities": result["symbolic"]["count"],
                      "integer_comparisons": result["thresholds"]["integer_comparisons"],
                      "nontrivial_composed_pairs": result["compositions"]["nontrivial_pairs"],
                      **result["aggregation"]}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
