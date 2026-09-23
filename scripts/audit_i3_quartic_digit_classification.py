"""Exact audits of the unbounded quartic digit-polynomial classification.

The proof is in the note. The CRT scan is a finite, supplementary diagnostic,
not the justification for completeness. Requires SymPy; uses no external table.
"""

import json
from fractions import Fraction
from itertools import combinations, product
from math import isqrt, lcm

import sympy as sp

from repo_paths import artifact_path


X = sp.symbols("X")


def poly(expression):
    return sp.Poly(expression, X, domain=sp.QQ)


def audit_symbolic_reduction():
    names = []

    def check(name, expression):
        assert sp.cancel(expression) == 0, name
        names.append(name)

    t, Z = sp.symbols("t Z")
    U0 = 1+Z
    V0 = (1+t*U0)/(1+t)
    L0 = t*U0-1-t
    F0 = 2+(1+2*t)*Z/(1+t)+t*Z**2/(1+t)
    J0 = t**2*Z*(Z+1)/(1+t)
    check("constant H: F formula", F0-(U0*V0+1))
    check("constant H: J formula", J0-(1+V0*L0))
    check("constant H: second fiber value", J0.subs(Z, -(1+2*t)/t)-(1+2*t))
    k = sp.symbols("k")
    check("constant H: composed F", F0.subs({t: sp.Rational(1,2), Z: 6*k})
          -(12*k*k+8*k+2))
    check("constant H: composed J", J0.subs({t: sp.Rational(1,2), Z: 6*k})
          -(6*k*k+k))

    Y, a, b, R, r = sp.symbols("Y alpha beta R r")
    U = 1/b+Y/(R+1)-a*Y**2/(b*R*(R+1))
    C = a*Y+b
    V = sp.cancel((U*C-1)/Y)
    D = a*Y**2+b*Y-R*(R+1)
    Q = (a*Y-R*b)**2-a*R*(R+1)
    check("linear H: Bezout identity", U*C-V*Y-1)
    check("double fiber proportionality", R*U-Y+D/(b*(R+1)))
    check("factorization of F-2", U*V-1-D*Q/(R**2*b**2*(R+1)**2))
    rem = (-Y+R*b/a)/(R+1)
    check("U modulo Q with exact quotient", U-rem+Q/(a*b*R*(R+1)))
    yy = (Z+R*b)/a
    rho = -(R+1)*(1+R*b/Z)
    check("remaining root value", yy/rem.subs(Y, yy)-rho)
    check("remaining root trace", rho+rho.subs(Z, -Z)+2*(R+1))
    root_product = sp.cancel(rho*rho.subs(Z, -Z)).subs(Z**2, a*R*(R+1))
    check("remaining root product", root_product-((R+1)**2-R*(R+1)*b*b/a))
    br = 1+(1-a)*r
    check("restore X=0", (U.subs(Y, r)-1).subs(b, br)
          -(r-R)*r*(R-a*(R+1))/(br*R*(R+1)))

    h = sp.symbols("h")
    substitution = {a: 5, b: -2, R: sp.Rational(-5,4), Y: h*X+sp.Rational(3,4)}
    UU = 1+8*h*X+8*h*h*X*X
    VV = 1+24*h*X+40*h*h*X*X
    LL = 1+3*h*X+2*h*h*X*X
    check("exceptional U", U.subs(substitution)-UU)
    check("exceptional V", V.subs(substitution)-VV)
    check("exceptional L", UU/4+h*X+sp.Rational(3,4)-LL)
    check("integrality Bezout", 11*(32*h)-13*(27*h)-h)
    return {"identities": len(names), "names": names}


def audit_exhaustive_scalar_cases():
    fiber_rows = []
    for eps in (-1, 0, 1):
        t = sp.Rational(eps+2, 4)
        R = eps-t
        others = [e-t for e in (-1, 0, 1) if e != eps]
        assert sum(others) == -2*(R+1)
        ratio = sp.cancel(((R+1)**2-sp.prod(others))/(R*(R+1)))
        fiber_rows.append({"double_J_value": eps+1, "t": str(t),
                           "R": str(R), "beta_squared_over_alpha": str(ratio),
                           "positive_ratio": bool(ratio > 0)})
    assert [r["beta_squared_over_alpha"] for r in fiber_rows] == ["4/5", "-4", "4/5"]

    a = sp.symbols("alpha")
    R = sp.Rational(-5,4)
    origin_rows = []
    for s in (0, 1, 2):
        r = s-sp.Rational(5,4)
        b = 1+(1-a)*r
        origin_residual = sp.factor((r-R)*r*(R-a*(R+1))/(b*R*(R+1)))
        ratio_residual = sp.factor(b*b-sp.Rational(4,5)*a)
        row = {"s": s, "r": str(r), "beta": str(b),
               "origin_residual": str(origin_residual),
               "ratio_residual": str(ratio_residual)}
        if s == 0:
            assert origin_residual == 0
            assert sp.expand(80*ratio_residual) == 125*a*a-114*a+5
            discriminant = 114**2-4*125*5
            assert discriminant == 256*41
            assert isqrt(discriminant)**2 != discriminant
            row.update(discriminant=discriminant, rational_alpha=False,
                       allowed=False, reason="quadratic discriminant is not a rational square")
        else:
            numerator = sp.fraction(origin_residual)[0]
            assert sp.solve(numerator, a) == [5]
            beta = b.subs(a, 5)
            assert ratio_residual.subs(a, 5) == 0
            allowed = beta < 0
            row.update(alpha="5", beta_at_alpha_5=str(beta),
                       allowed=bool(allowed), reason="positive leading coefficient requires beta<0")
        origin_rows.append(row)
    assert [r["s"] for r in origin_rows if r["allowed"]] == [2]
    return {"fiber_cases": fiber_rows, "origin_cases": origin_rows}


def family_one(a, b):
    K = a*X+b*X*X
    return poly(12*K*K+8*K+2), poly(6*K*K+K)


def family_two(h):
    y = h*X
    return (poly(320*y**4+512*y**3+240*y*y+32*y+2),
            poly(80*y**4+168*y**3+114*y*y+27*y+2))


def identify(F, J):
    """Check the explicit classification without using the reduction variables."""
    for complement in (False, True):
        J0 = F-J if complement else J
        if J0.nth(0) == 0:
            a = J0.nth(1)
            b = J0.nth(2)-6*a*a
            if a.q == b.q == 1 and a >= 0 and b > 0:
                FF, JJ = family_one(a, b)
                if F == FF and J0 == JJ:
                    return {"family": "I", "a": int(a), "b": int(b),
                            "complement": complement}
        if J0.nth(0) == 2:
            h = F.nth(1)/32
            if h.q == 1 and h > 0:
                FF, JJ = family_two(h)
                if F == FF and J0 == JJ:
                    return {"family": "II", "h": int(h), "complement": complement}
    return None


def audit_families():
    identities = []
    y = sp.symbols("y")
    F, J = family_two(1)
    forms = {
        "quartic F-1": (F-1, (8*X*X+8*X+1)*(40*X*X+24*X+1)),
        "quartic F-2": (F-2, 16*X*(2*X+1)*(10*X*X+11*X+2)),
        "quartic J": (J, (8*X*X+8*X+1)*(10*X*X+11*X+2)),
        "quartic J-1": (J-1, (X+1)*(2*X+1)*(40*X*X+24*X+1)),
        "quartic J-2": (J-2, X*(80*X**3+168*X*X+114*X+27)),
    }
    for name, (lhs, rhs) in forms.items():
        assert lhs == poly(rhs)
        identities.append(name)
    F1, J1 = 12*y*y+8*y+2, 6*y*y+y
    for name, lhs, rhs in [
        ("composed F-1", F1-1, (6*y+1)*(2*y+1)),
        ("composed F-2", F1-2, 4*y*(3*y+2)),
        ("composed J", J1, y*(6*y+1)),
        ("composed J-1", J1-1, (3*y-1)*(2*y+1)),
        ("composed J-2", J1-2, (3*y+2)*(2*y-1)),
    ]:
        assert sp.expand(lhs-rhs) == 0
        identities.append(name)

    pairs, integer_values = 0, 0
    denominators = {"I": set(), "II": set()}
    parameters = [("I", a, b) for a, b in product(range(5), range(1, 6))]
    parameters += [("II", h, 0) for h in range(1, 26)]
    for kind, a, b in parameters:
        F, J = family_one(a, b) if kind == "I" else family_two(a)
        modulus = 4 if kind == "I" else 16
        assert all(F.nth(k) % modulus == 0 for k in range(1, 5))
        for J0 in (J, F-J):
            assert all(0 <= J0.nth(k) <= F.nth(k) for k in range(5))
            assert all(c.q == 1 for c in F.all_coeffs()+J0.all_coeffs())
            assert identify(F, J0) is not None
            q1, r1 = (J0*(J0-1)).div(F-1)
            q2, r2 = (J0*(J0-1)*(J0-2)).div(F-2)
            assert r1.is_zero and r2.is_zero
            denominator = lcm(*(int(c.q) for c in q2.all_coeffs()))
            denominators[kind].add(denominator)
            assert sorted(int((F-1).gcd(J0-s).degree()) for s in (0, 1)) == [2, 2]
            expect = [0, 2, 2] if kind == "I" else [1, 1, 2]
            assert sorted(int((F-2).gcd(J0-s).degree()) for s in (0, 1, 2)) == expect
            pairs += 1
        for x in range(-10, 11):
            assert F.eval(x) % modulus == 2
            integer_values += 1
    assert denominators == {"I": {4}, "II": {16}}
    return {"factorization_identities": len(identities), "names": identities,
            "nontrivial_polynomial_pairs": pairs, "integer_value_checks": integer_values,
            "second_quotient_denominators": {k: sorted(v) for k, v in denominators.items()}}


def audit_crt_scan():
    # Bounded diagnostic: all unordered pairs from 96 integer quadratics,
    # followed by explicit cases reaching the two classified families.
    # Individual factors may have negative linear coefficients; only F is
    # assumed coefficientwise nonnegative in the classification theorem.
    factors = [poly(1+a*X+b*X*X) for a, b in product(range(-4, 8), range(1, 9))]
    cases = list(combinations(factors, 2))
    for a, b in product(range(4), range(1, 4)):
        K = a*X+b*X*X
        cases.append((poly(1+6*K), poly(1+2*K)))
    for h in (1, 2, 3):
        cases.append((poly(1+8*h*X+8*h*h*X*X),
                      poly(1+24*h*X+40*h*h*X*X)))
    counts = {"factor_pairs": len(cases), "nonnegative_F_pairs": 0, "coprime_pairs": 0,
              "CRT_polynomials": 0, "integer_coefficient_ordered": 0,
              "both_divisibilities": 0}
    survivors = []
    for U, V in cases:
        F = U*V+1
        if not all(c >= 0 for c in F.all_coeffs()):
            continue
        counts["nonnegative_F_pairs"] += 1
        if U.gcd(V).degree() != 0:
            continue
        counts["coprime_pairs"] += 1
        base = U*U.invert(V)
        for s in range(3):
            J = base+(s-base.nth(0))*(F-1)
            counts["CRT_polynomials"] += 1
            assert J.nth(0) == s
            assert J.rem(U).is_zero and (J-1).rem(V).is_zero
            if not all(J.nth(k).q == 1 and 0 <= J.nth(k) <= F.nth(k) for k in range(5)):
                continue
            counts["integer_coefficient_ordered"] += 1
            if not (J*(J-1)*(J-2)).rem(F-2).is_zero:
                continue
            answer = identify(F, J)
            assert answer is not None, (F.as_expr(), J.as_expr())
            counts["both_divisibilities"] += 1
            survivors.append(answer)
    assert {s["family"] for s in survivors} == {"I", "II"}
    return {**counts, "survivors": survivors,
            "scope": "finite supplement only; unbounded completeness is the scalar-case proof"}


def audit_general_trace():
    def power_sums(coefficients, level):
        values = list(map(Fraction, coefficients))
        values[0] -= level
        m = len(values)-1
        c = [Fraction(1)] + [values[m-i]/values[m] for i in range(1, m+1)]
        sums = [Fraction(m)]
        for k in range(1, m+1):
            sums.append(-sum(c[i]*sums[k-i] for i in range(1, k))-k*c[k])
        return sums

    checked, repeated_root_cases = 0, 0
    for m in range(1, 17):
        Fs = [[(3*i+seed*seed) % 11-5 for i in range(m)] + [seed]
              for seed in range(1, 7)]
        # F-1=X^m or (X+1)^m includes repeated roots explicitly.
        Fs += [[1]+[0]*(m-1)+[1],
               [int(sp.binomial(m, i))+(1 if i == 0 else 0) for i in range(m+1)]]
        for index, coefficients in enumerate(Fs):
            J = [Fraction((i*7+index) % 13-6, i+1) for i in range(m+1)]
            p1 = power_sums(coefficients, 1)
            p2 = power_sums(coefficients, 2)
            assert p1[:m] == p2[:m]
            assert p2[m]-p1[m] == Fraction(m, coefficients[m])
            difference = sum(J[i]*(p2[i]-p1[i]) for i in range(m+1))
            assert difference == m*J[m]/coefficients[m]
            checked += 1
            repeated_root_cases += int(index >= 6 and m >= 2)
    table = []
    for degrees in ((2, 2, 1), (2, 1, 2), (1, 2, 2)):
        t = Fraction(degrees[1]+2*degrees[2]-3, 5)
        table.append({"degrees": degrees, "t": str(t)})
    assert [r["t"] for r in table] == ["1/5", "2/5", "3/5"]
    return {"exact_Newton_diagnostics": checked,
            "repeated_root_cases": repeated_root_cases, "quintic_table": table}


def main():
    result = {"status": "passed",
              "scope": "complete quartic polynomial classification; general i=3 remains open",
              "symbolic_reduction": audit_symbolic_reduction(),
              "scalar_cases": audit_exhaustive_scalar_cases(),
              "families": audit_families(),
              "CRT_scan": audit_crt_scan(),
              "general_trace": audit_general_trace()}
    path = artifact_path("verification_i3_quartic_digit_classification.json")
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+"\n",
                    encoding="utf-8", newline="\n")
    print(json.dumps({"status": "passed", "output": str(path),
                      "symbolic_identities": result["symbolic_reduction"]["identities"],
                      "factorization_identities": result["families"]["factorization_identities"],
                      "nontrivial_pairs": result["families"]["nontrivial_polynomial_pairs"],
                      "integer_values": result["families"]["integer_value_checks"],
                      "CRT_candidates": result["CRT_scan"]["CRT_polynomials"],
                      "CRT_survivors": result["CRT_scan"]["both_divisibilities"],
                      "Newton_diagnostics": result["general_trace"]["exact_Newton_diagnostics"]},
                     ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
