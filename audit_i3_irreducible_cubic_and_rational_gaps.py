"""Exact checks for the irreducible orbit cubic and rational-gap bounds.

The conditional theorem is proved in the accompanying note. No counterexample
is available for testing its hypotheses, and no finite search proves it.
"""

import json
from functools import reduce
from math import comb, gcd
from pathlib import Path

import sympy as s


def v2(k):
    assert k
    k = abs(int(k))
    return (k & -k).bit_length() - 1


def coefficients(n, j):
    return [comb(j, 3-h)*comb(n-j, h) for h in range(4)]


def binary_cubic(n, j, a, b):
    return (-n*(n-1)*(n-2)*a**3
            + 3*j*(n-1)*(n-2)*a*a*b
            - 3*j*(j-1)*(n-2)*a*b*b
            + j*(j-1)*(j-2)*b**3)


def shifted_cubic(n, j, a, b):
    t = b*j-a*n
    d = 2*a-b
    aa = a*(b-a)
    return t**3+3*d*t*t+(2*d*d+2*aa-3*aa*n)*t-2*d*aa*n


def algebra():
    n, j, a, b, z, t = s.symbols('n j a b z t')
    y = n-j
    xs = [j*(j-1)*(j-2)/6, j*(j-1)*y/2,
          j*y*(y-1)/2, y*(y-1)*(y-2)/6]
    f = sum(xs[h]*z**h for h in range(4))
    expected = j*j*y*y*(j-1)*(y-1)*(n-1)*(n-2)**2/12
    expressions = [
        f.subs(z, 1)-n*(n-1)*(n-2)/6,
        6*sum(xs[h]*(-a)**h*(b-a)**(3-h) for h in range(4))
        - binary_cubic(n, j, a, b),
        binary_cubic(n, j, a, b)-shifted_cubic(n, j, a, b),
        s.discriminant(f, z)-expected,
        2*(t+2*b)**3-(2*t**3+6*b*t*t+5*b*b*t)
        -(6*b*t*t+19*b*b*t+16*b**3),
    ]
    for expression in expressions:
        assert s.factor(expression) == 0
    return len(expressions)


def valuation_argument():
    pairs = 0
    denominator_checks = 0
    branches = set()
    for u in range(3, 10):
        for odd in (1, 3, 5, 9, 17):
            n = (1 << u)*odd
            for j in range(4, min(n//2, 96)+1):
                v = v2(j)
                if v >= u:
                    continue
                assert v2(n-j) == v
                xs = coefficients(n, j)
                assert min(map(v2, xs)) == v
                assert sum(xs) == comb(n, 3)
                assert v2(comb(n, 3)) == u
                branches.add('odd' if v == 0 else 'v=1' if v == 1 else 'v>=2')
                for exponent in range(1, u+3):
                    a, b = 1, 1 << exponent
                    terms = [-n*(n-1)*(n-2)*a**3,
                             3*j*(n-1)*(n-2)*a*a*b,
                             -3*j*(j-1)*(n-2)*a*b*b,
                             j*(j-1)*(j-2)*b**3]
                    actual = list(map(v2, terms))
                    expected = [u+1, v+1+exponent,
                                v+v2(j-1)+1+2*exponent,
                                v+v2(j-1)+v2(j-2)+3*exponent]
                    assert actual == expected
                    assert actual[2] > actual[1] and actual[3] > actual[1]
                    if exponent != u-v:
                        assert sum(terms) != 0
                        assert v2(sum(terms)) == min(actual[:2])
                    denominator_checks += 1
                pairs += 1
    assert len(branches) == 3
    return {'pairs': pairs, 'denominator_checks': denominator_checks,
            'branches': sorted(branches)}


def reducible_diagnostics():
    z = s.symbols('z')
    checked = 0
    reducible = 0
    noncentral = []
    cases = [(n, j) for n in range(8, 121, 4) for j in range(4, n//2+1)]
    cases += [(232, 70), (800, 324), (2756, 494)]
    for n, j in cases:
        u = v2(n)
        odd_part = comb(n, 3) >> u
        v = v2(j)
        if v >= u:
            continue
        xs = coefficients(n, j)
        f = s.Poly(sum(xs[h]*z**h for h in range(4)), z)
        linear = [factor for factor, multiplicity in s.factor_list(f)[1]
                  if factor.degree() == 1]
        checked += 1
        if not linear:
            continue
        reducible += 1
        # A rational root contradicts the required odd content; actual
        # small binomial coefficients provide a separate diagnostic.
        assert any(x % odd_part for x in xs)
        common = gcd(comb(n, 3), comb(n, j))
        common_odd = common >> v2(common)
        assert common_odd > 1
        for factor in linear:
            c, a = map(int, factor.all_coeffs())
            if c < 0:
                c, a = -c, -a
            assert c > 0 and a > 0 and gcd(a, c) == 1
            b = a+c
            assert binary_cubic(n, j, a, b) == 0
            quotient = s.div(f, s.Poly(c*z+a, z))[0]
            assert all(q.is_Integer and q > 0 for q in quotient.all_coeffs())
        if 2*j < n and len(noncentral) < 6:
            noncentral.append({'n': n, 'j': j, 'common_odd': common_odd,
                               'linear_factors': [str(f.as_expr()) for f in linear]})
    assert reducible > 0
    assert len(noncentral) == 3
    return {'cubics_checked': checked, 'reducible_cubics': reducible,
            'noncentral_examples': noncentral,
            'scope': 'These are examples violating the counterexample hypotheses.'}


def bound_checks():
    estimates = 0
    contents = 0
    for n, j in ((8, 4), (32, 10), (76, 19), (256, 85),
                 (76672, 26775), (175492, 60606),
                 (3258244432, 1087547175)):
        xs = coefficients(n, j)
        content = reduce(gcd, xs)
        for b in range(2, 19):
            for a in range(1, b):
                if gcd(a, b) != 1:
                    continue
                value = binary_cubic(n, j, a, b)
                assert value == shifted_cubic(n, j, a, b)
                assert value % (6*content) == 0
                if value:
                    assert abs(value) >= 6*content
                    contents += 1
                x = abs(b*j-a*n)+2*b
                assert 4*abs(value) <= 4*x**3+3*b*b*n*x
                estimates += 1
    threshold_checks = 0
    for kk in (1, 2, 3, 8, 27, 256):
        for n in (6, 8, 100, 1000, 10**6, 1 << 49):
            for b in range(2, 33):
                if 4*kk*kk*n < 27*b**6:
                    continue
                x = int(s.integer_nthroot(kk*n*n//4, 3)[0])
                assert 4*x**3 <= kk*n*n
                assert 3*b*b*x <= kk*n
                assert 2*x**3+s.Rational(3, 2)*b*b*n*x <= kk*n*n
                assert 4*kk*(n-1)*(n-2) > 4*x**3+3*b*b*n*x
                threshold_checks += 1
    example_bound = 16*7**6
    assert example_bound == 1882384 and example_bound < 1 << 49
    return {'majorant_checks': estimates, 'nonzero_content_checks': contents,
            'threshold_checks': threshold_checks,
            'bound_for_abs_3j_minus_n_le_sqrt_n': example_bound}


def main():
    result = {'status': 'passed', 'symbolic_identities': algebra(),
              'valuation_argument': valuation_argument(),
              'rational_factor_diagnostics': reducible_diagnostics(),
              'bounds': bound_checks(),
              'scope': 'Exact checks of the new proof components; not a solution of i=3.'}
    path = Path(__file__).with_name('verification_i3_irreducible_cubic_and_rational_gaps.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
