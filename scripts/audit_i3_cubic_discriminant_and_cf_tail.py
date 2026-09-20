"""Targeted exact checks; does not enumerate counterexamples or cubic fields."""
import hashlib
import json
from fractions import Fraction
from math import gcd

import sympy as sp

from repo_paths import ROOT, artifact_path
from audit_i3_irreducible_cubic_and_rational_gaps import coefficients, v2
from audit_i3_dyadic_denominators_and_continued_fractions import convergents


def main():
    z, n, j, k = sp.symbols('z n j k')
    y = n-j
    f = (j*(j-1)*(j-2)/6 + j*(j-1)*y*z/2
         + j*y*(y-1)*z**2/2 + y*(y-1)*(y-2)*z**3/6)
    p = 6*f/(k*(n-1)*(n-2))
    expected = 108*j**2*y**2*(j-1)*(y-1)/(k**4*(n-1)**3*(n-2)**2)
    assert sp.factor(sp.discriminant(p, z)-expected) == 0
    a, b, c, e = sp.symbols('A B C E')
    poly = a*z**3+b*z**2+c*z+e
    omega, eta = a*z, a*z**2+b*z
    relations = [omega**2-a*eta+b*omega,
                 omega*eta+c*omega+a*e,
                 eta**2+c*eta+e*omega+b*e]
    for relation in relations:
        assert sp.rem(relation, poly, z) == 0

    assert Fraction(63, 64)**3*Fraction(62, 64)**2 > Fraction(27, 32)
    assert sp.expand(16*(n-1)*(n-2)-5*n*(3*n+16)) == n*n-128*n+32
    assert 128**2-128*128+32 > 0
    assert Fraction(1, 2**24) < Fraction(1, 1000)
    assert Fraction(17, 10)**3 < 5
    assert (Fraction(17, 10)-Fraction(1, 10))/2 == Fraction(4, 5)
    assert Fraction(32)/Fraction(4, 5)**3 == Fraction(125, 2)
    assert 8**2 > Fraction(125, 2)

    tails = noncoprime = even_final = parity = 0
    for nn in range(8, 257):
        for jj in range(4, nn//2+1):
            conv = convergents(jj, nn)
            _, aa, qq = conv[-2]
            gg = gcd(nn, jj)
            assert abs(qq*jj-aa*nn) == gg
            assert conv[-1][2] == nn//gg
            tails += 1
            noncoprime += gg > 1
            if (nn//gg) % 2 == 0:
                assert qq % 2 == 1
                even_final += 1
    for u in range(4, 11):
        for odd in (1, 3, 5):
            nn = odd << u
            for jj in range(4, min(nn//2, 100)+1, 2):
                v = v2(jj)
                if v >= u:
                    continue
                xs = coefficients(nn, jj)
                assert all(x % (1 << v) == 0 for x in xs)
                actual = [(x >> v) % 2 for x in xs]
                assert actual == ([0, 1, 1, 0] if v == 1 else [1, 0, 0, 1])
                assert gcd(nn, jj) <= (odd << v)
                parity += 1

    source = ROOT/'sources/source_progress_2026-09-21_cubic_discriminant_cf.md'
    result = {
        'status': 'passed',
        'symbolic_discriminant_identity': True,
        'order_multiplication_identities': len(relations),
        'exact_constant_checks': True,
        'rational_cf_tails': tails,
        'noncoprime_tails': noncoprime,
        'even_final_denominators_with_odd_predecessor': even_final,
        'normalized_coefficient_parity_cases': parity,
        'source_sha256': hashlib.sha256(source.read_bytes()).hexdigest(),
        'external_input': {
            'minimal_totally_real_cubic_field_discriminant': 49,
            'reference': 'https://www.lmfdb.org/NumberField/3.3.49.1',
            'independently_reproved_here': False,
        },
        'unadopted_classification_constants': [37, 71, 229],
        'scope': 'Symbolic identities and diagnostic checks, not a solution of problem 699.',
    }
    output = artifact_path('verification_i3_cubic_discriminant_and_cf_tail.json')
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
