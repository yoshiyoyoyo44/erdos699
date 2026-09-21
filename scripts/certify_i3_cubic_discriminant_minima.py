"""Enumerate all Hessian-reduced irreducible binary cubics of discriminant <= 961.

Completeness bounds are proved in the accompanying note.  This enumerates
integer forms, including nonmaximal orders; it does not query a field table.
The independent replay uses a rectangular coefficient search instead.
"""
import json
from math import gcd, isqrt

from repo_paths import artifact_path


LIMIT = 961


def discriminant(a, b, c, d):
    return b*b*c*c - 4*a*c**3 - 4*b**3*d - 27*a*a*d*d + 18*a*b*c*d


def divisors(n):
    small = [r for r in range(1, isqrt(n)+1) if n % r == 0]
    return sorted(set(small + [n//r for r in small]))


def irreducible(a, b, c, d):
    if not a or not d:
        return False
    for q in divisors(a):
        for numerator in divisors(abs(d)):
            if gcd(numerator, q) != 1:
                continue
            for p in (numerator, -numerator):
                if a*p**3 + b*p*p*q + c*p*q*q + d*q**3 == 0:
                    return False
    return True


def reduced_forms():
    rows = []
    a = 1
    while 729*a**4 <= 16*LIMIT:
        for h0 in range(1, isqrt(LIMIT)+1):
            # A safe ceiling for |b| <= sqrt(h0) + 3a/2.
            bmax = isqrt(h0)+1+(3*a+1)//2
            for b in range(-bmax, bmax+1):
                excess = 2*abs(b)-3*a
                if excess > 0 and excess**2 > 4*h0:
                    continue
                if (b*b-h0) % (3*a):
                    continue
                c = (b*b-h0)//(3*a)
                for h1 in range(-h0, h0+1):
                    if (b*c-h1) % (9*a):
                        continue
                    d = (b*c-h1)//(9*a)
                    h2 = c*c-3*b*d
                    delta = discriminant(a, b, c, d)
                    if h2 < h0 or not 0 < delta <= LIMIT:
                        continue
                    assert 4*h0*h2-h1*h1 == 3*delta
                    if irreducible(a, b, c, d):
                        rows.append({'coefficients': [a, b, c, d],
                                     'discriminant': delta,
                                     'hessian': [h0, h1, h2]})
        a += 1
    return sorted(rows, key=lambda row: (row['discriminant'], row['coefficients']))


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    rows = reduced_forms()
    result = {
        'schema': 'erdos699-binary-cubic-minima-v1',
        'limit_inclusive': LIMIT,
        'coefficient_order': 'a*x^3+b*x^2*y+c*x*y^2+d*y^3',
        'reduction': 'a>0 and |H1|<=H0<=H2',
        'forms': rows,
        'claimed_minima': {
            'all': 49,
            'discriminant_v2_2': 148,
            'discriminant_v2_2_with_simple_and_double_root_mod2': 316,
            'discriminant_v2_3': 568,
            'odd_discriminant_one_projective_root_mod2': 229,
            'odd_discriminant_three_projective_roots_mod2': 961,
        },
        'scope': 'Complete small-discriminant enumeration, not counterexample enumeration.',
    }
    path = artifact_path('i3_cubic_discriminant_minima_certificate.json')
    path.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status': 'generated', 'forms': len(rows),
                      'distinct_discriminants': sorted({r['discriminant'] for r in rows}),
                      'output': str(path)}, indent=2))


if __name__ == '__main__':
    main()
