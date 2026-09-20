"""Exact arithmetic for the dyadic denominator and continued-fraction bounds."""

import json
from fractions import Fraction
from math import gcd
from pathlib import Path

from audit_i3_irreducible_cubic_and_rational_gaps import (
    binary_cubic, coefficients, v2,
)


def denominator_weight(b, h):
    s = v2(b)
    if s == 0:
        return 1
    return 1 << (h+1 if s == h else min(s, h))


def convergents(numerator, denominator):
    previous_p, p = 0, 1
    previous_q, q = 1, 0
    out = []
    while denominator:
        digit, remainder = divmod(numerator, denominator)
        previous_p, p = p, digit*p+previous_p
        previous_q, q = q, digit*q+previous_q
        out.append((digit, p, q))
        numerator, denominator = denominator, remainder
    return out


def valuation_checks():
    count = 0
    equal_valuations = 0
    derivatives = 0
    for u in range(3, 14):
        for odd in (1, 3, 5, 9):
            n = odd << u
            for j in range(4, min(n//2, 44)+1):
                v = v2(j)
                if v >= u:
                    continue
                xs = coefficients(n, j)
                derivative = sum(h*xs[h] for h in range(4))
                assert derivative == (n-j)*(n-1)*(n-2)//2
                assert v2(derivative) == v
                derivatives += 1
                h = u-v
                for exponent in range(1, h+3):
                    for odd_b in (1, 3, 5):
                        b = odd_b << exponent
                        for a in (1, 3, 5):
                            if a >= b or gcd(a, b) != 1:
                                continue
                            value = binary_cubic(n, j, a, b)
                            weight = denominator_weight(b, h)
                            assert value % ((1 << (v+1))*weight) == 0
                            if exponent == h:
                                if value:
                                    assert v2(value) >= u+2
                                equal_valuations += 1
                            else:
                                assert value != 0
                                assert v2(value) == v+1+min(exponent, h)
                            count += 1
    return {'derivatives': derivatives, 'weighted_values': count,
            'equal_minimum_cases': equal_valuations}


def continued_fraction_checks():
    pairs = 0
    transitions = 0
    final_equalities = 0
    for n in range(8, 150):
        for j in range(1, n//2+1):
            cf = convergents(j, n)
            assert Fraction(cf[-1][1], cf[-1][2]) == Fraction(j, n)
            for k, (_, a, b) in enumerate(cf[:-1]):
                _, next_a, next_b = cf[k+1]
                assert abs(a*next_b-next_a*b) == 1
                error = abs(b*j-a*n)
                assert error*next_b <= n
                if k+2 == len(cf):
                    assert error*next_b == n
                    final_equalities += 1
                else:
                    assert error*next_b < n
                transitions += 1
            pairs += 1
    return {'fractions': pairs, 'transitions': transitions,
            'penultimate_equalities': final_equalities}


def diagnostic_family():
    output = []
    for m in (17, 20, 40, 100):
        r = 1 << m
        n = r**3
        j = (1 << (3*m-4))+3*(1 << (2*m-5))+1
        u, v = v2(n), v2(j)
        assert u == 3*m and v == 0 and 4 < j < n//2
        a, b = 1, 16
        weight = denominator_weight(b, u-v)
        assert weight == 16
        x = abs(b*j-a*n)+2*b
        assert x == 3*r*r//2+48
        assert 4*weight*weight*n >= 27*b**6
        # Old majorant passes for the same fraction, new gap rejects.
        assert 4*(n-1)*(n-2) <= 4*x**3+3*b*b*n*x
        assert 4*x**3 < weight*n*n
        assert 4*weight*(n-1)*(n-2) > 4*x**3+3*b*b*n*x
        cf = convergents(j, n)
        assert [row[0] for row in cf[:3]] == [0, 15, 1]
        assert cf[2][1:] == (1, 16)
        _, next_a, next_b = cf[3]
        # The exact bound in (8) fails; compare the cube after clearing
        # denominators instead of approximating its cube root.
        assert 4*(n+2*b*next_b)**3 <= weight*n*n*next_b**3
        if m in (17, 20):
            output.append({'m': m, 'n': n, 'j': j,
                           'convergent': [a, b], 'weight': weight,
                           'next_convergent': [next_a, next_b],
                           'old_same_fraction_majorant_passes': True,
                           'new_exact_bound_rejects': True})
    assert Fraction(99, 64)**3 < 4
    return {'exponents_checked': [17, 20, 40, 100], 'examples': output,
            'scope': 'Normalized diagnostic family, not putative counterexamples passing all conditions.'}


def constants():
    # The proof reduces L_b > 4b to 27*n^3 > 512^2.
    assert 27*64**3 > 512**2
    count = 0
    for n in (64, 128, 65536, 1 << 49):
        for kk in (1, 3, 16, 128):
            for b in range(2, 100):
                if 4*kk*kk*n < 27*b**6:
                    continue
                assert kk*n*n > 256*b**3
                count += 1
    return count


def main():
    result = {'status': 'passed', 'valuations': valuation_checks(),
              'continued_fractions': continued_fraction_checks(),
              'diagnostic_family': diagnostic_family(),
              'constant_checks': constants(),
              'scope': 'Checks of proof components and diagnostic cases, not a solution of i=3.'}
    path = Path(__file__).with_name('verification_i3_dyadic_denominators_and_continued_fractions.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
