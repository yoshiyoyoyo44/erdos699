"""Independent coefficient-box replay and exact algebra for cubic minima.

Does not import the certificate generator or rely on a number-field database.
The proof of the finite search bounds and of the dyadic descent is in the note.
SymPy checks polynomial identities; all enumeration uses exact integers.
"""
import hashlib
import json
from itertools import product
from math import comb

import sympy as sp

from repo_paths import artifact_path


def disc(f):
    a, b, c, d = f
    return b*b*c*c + 18*a*b*c*d - 4*a*c**3 - 4*b**3*d - 27*a*a*d*d


def hessian(f):
    a, b, c, d = f
    return b*b-3*a*c, b*c-9*a*d, c*c-3*b*d


def has_rational_root(f):
    a, b, c, d = f
    if d == 0:
        return True
    # Unreduced fractions are harmless.  This differs from the generator's
    # divisor-based implementation of the rational root test.
    for q in range(1, abs(a)+1):
        for p in range(-abs(d), abs(d)+1):
            if a*p**3 + b*p*p*q + c*p*q*q + d*q**3 == 0:
                return True
    return False


def v2(value):
    assert value != 0
    value = abs(value)
    return (value & -value).bit_length()-1


def root_count_mod2(f):
    a, b, c, d = f
    return sum((a % 2 == 0, d % 2 == 0, (a+b+c+d) % 2 == 0))


def transform(f, matrix):
    a, b, c, d = f
    p, q, r, s = matrix
    return (a*p**3+b*p*p*r+c*p*r*r+d*r**3,
            3*a*p*p*q+b*(p*p*s+2*p*q*r)+c*(2*p*r*s+q*r*r)+3*d*r*r*s,
            3*a*p*q*q+b*(2*p*q*s+q*q*r)+c*(p*s*s+2*q*r*s)+3*d*r*s*s,
            a*q**3+b*q*q*s+c*q*s*s+d*s**3)


MATRICES = tuple(m for m in product(range(2), repeat=4)
                 if abs(m[0]*m[3]-m[1]*m[2]) == 1)


def normalize_double_root(f):
    for matrix in MATRICES:
        candidate = transform(f, matrix)
        if tuple(c % 2 for c in candidate) == (0, 1, 0, 0):
            return candidate
    raise AssertionError(('No distinct simple and double root mod 2', f))


def lower_discriminant(f):
    delta = disc(f)
    assert delta > 0 and v2(delta) >= 4
    a, b, c, d = normalize_double_root(f)
    assert a % 2 == 0 and b % 2 == 1 and c % 4 == d % 4 == 0
    result = (2*a, b, c//2, d//4)
    assert 4*disc(result) == delta
    return result


def audit_symbolic_identities():
    a, b, c, d, x, y = sp.symbols('a b c d x y')
    f = (a, b, c, d)
    h0, h1, h2 = hessian(f)
    jac = 2*b*h0-3*a*h1
    identities = [4*h0*h2-h1*h1-3*disc(f),
                  jac*jac+27*a*a*disc(f)-4*h0**3,
                  4*disc((2*a, b, c/2, d/4))-disc(f)]
    for matrix in MATRICES:
        transformed = transform(f, matrix)
        identities.append(disc(transformed)-disc(f))
        p, q, r, s = matrix
        t0, t1, t2 = hessian(transformed)
        identities.append(t0*x*x+t1*x*y+t2*y*y
                          -h0*(p*x+q*y)**2-h1*(p*x+q*y)*(r*x+s*y)-h2*(r*x+s*y)**2)
    aa, cc, dd = sp.symbols('aa cc dd')
    # With a=2aa, c=2cc, d=2dd, Delta/4 modulo 4 is b^2 cc^2-2b^3 dd.
    quotient = sp.Poly(sp.expand(disc((2*aa, b, 2*cc, 2*dd))/4
                                -b*b*cc*cc+2*b**3*dd), aa, b, cc, dd)
    assert all(int(value) % 4 == 0 for value in quotient.coeffs())
    for identity in identities:
        assert sp.expand(identity) == 0
    return len(identities)+1


def replay_box():
    rows = []
    checked = 0
    for a, b, c, d in product(range(1, 3), range(-8, 9), range(-21, 22), range(-22, 23)):
        checked += 1
        f = a, b, c, d
        h0, h1, h2 = hessian(f)
        if not (0 < h0 <= 31 and abs(h1) <= h0 <= h2):
            continue
        delta = disc(f)
        if not 0 < delta <= 961 or has_rational_root(f):
            continue
        rows.append({'coefficients': list(f), 'discriminant': delta,
                     'hessian': [h0, h1, h2]})
    return sorted(rows, key=lambda row: (row['discriminant'], row['coefficients'])), checked


def audit_dyadic_descent(rows):
    # All six distinct-simple/double-root forms over F_2 are covered by GL_2(F_2).
    patterns = {tuple(value % 2 for value in transform((0, 1, 0, 0), m)) for m in MATRICES}
    assert len(patterns) == 6
    for pattern in patterns:
        assert tuple(c % 2 for c in normalize_double_root(pattern)) == (0, 1, 0, 0)
    residue_checks = 0
    for a, b, c, d in product(range(0, 16, 2), range(1, 16, 2), range(0, 16, 2), range(0, 16, 2)):
        if disc((a, b, c, d)) % 16 == 0:
            assert c % 4 == d % 4 == 0
            residue_checks += 1

    # Invert the scaling from representative v2=2 and v2=3 cubics, then
    # apply nontrivial unimodular transformations before descending again.
    cases = steps = 0
    for delta in (316, 568):
        base = tuple(next(row['coefficients'] for row in rows if row['discriminant'] == delta))
        a, b, c, d = normalize_double_root(base)
        # Base a is even, making this first inverse scaling integral.
        lifted = (a//2, b, 2*c, 4*d)
        for height in range(1, 9):
            if height > 1:
                a, b, c, d = normalize_double_root(current_base)
                assert a % 2 == 0
                lifted = (a//2, b, 2*c, 4*d)
            current_base = normalize_double_root(lifted)
            assert disc(lifted) == delta*4**height
            for matrix in MATRICES:
                current = transform(lifted, matrix)
                while v2(disc(current)) >= 4:
                    current = lower_discriminant(current)
                    steps += 1
                assert disc(current) == delta
                cases += 1
    return residue_checks, cases, steps


def audit_orbit_parity():
    cases = {'odd_j': 0, 'v_1': 0, 'v_at_least_2': 0}
    for u in range(4, 11):
        for odd in (1, 3, 5):
            n = odd << u
            for j in range(4, min(n//2, 100)):
                v = v2(j)
                if v >= u:
                    continue
                y = n-j
                # The omitted B_odd denominator is odd; if P is integral,
                # it has exactly this coefficient parity. These examples
                # are diagnostic, not alleged counterexamples.
                coefficients = [comb(j, 3-r)*comb(y, r) for r in (3, 2, 1, 0)]
                assert all(c % (1 << v) == 0 for c in coefficients)
                parity = tuple((c >> v) % 2 for c in coefficients)
                delta_v = (2+2*v2(j)+2*v2(y)+v2(j-1)+v2(y-1)
                           -4*v-3*v2(n-1)-2*v2(n-2))
                if v == 0:
                    assert parity in ((1, 1, 0, 0), (0, 0, 1, 1))
                    w = max(v2(j-1), v2(y-1))
                    assert min(v2(j-1), v2(y-1)) == 1
                    assert delta_v == w+1
                    cases['odd_j'] += 1
                else:
                    assert delta_v == 0
                    assert parity == ((0, 1, 1, 0) if v == 1 else (1, 0, 0, 1))
                    cases['v_1' if v == 1 else 'v_at_least_2'] += 1
    return cases


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    path = artifact_path('i3_cubic_discriminant_minima_certificate.json')
    certificate = json.loads(path.read_text(encoding='utf-8'))
    assert certificate['schema'] == 'erdos699-binary-cubic-minima-v1'
    assert certificate['limit_inclusive'] == 961
    # Integer checks for the bounds used in the independent search box.
    assert 729*3**4 > 16*961 and 32**2 > 961
    assert (2*9-3*2)**2 > 4*31
    assert (64-1)//3 == 21 and (8*21+31)//9 == 22
    rows, checked = replay_box()
    assert rows == certificate['forms']
    predicates = {
        'all': lambda row: True,
        'discriminant_v2_2': lambda row: v2(row['discriminant']) == 2,
        'discriminant_v2_2_with_simple_and_double_root_mod2': lambda row: v2(row['discriminant']) == 2 and root_count_mod2(row['coefficients']) == 2,
        'discriminant_v2_3': lambda row: v2(row['discriminant']) == 3,
        'odd_discriminant_one_projective_root_mod2': lambda row: row['discriminant'] % 2 == 1 and root_count_mod2(row['coefficients']) == 1,
        'odd_discriminant_three_projective_roots_mod2': lambda row: row['discriminant'] % 2 == 1 and root_count_mod2(row['coefficients']) == 3,
    }
    minima = {name: min(row['discriminant'] for row in rows if predicate(row))
              for name, predicate in predicates.items()}
    assert minima == certificate['claimed_minima']
    identities = audit_symbolic_identities()
    residues, cases, steps = audit_dyadic_descent(rows)
    for row in rows:
        f = tuple(row['coefficients'])
        for matrix in MATRICES:
            assert root_count_mod2(transform(f, matrix)) == root_count_mod2(f)
    result = {
        'status': 'passed',
        'certificate_sha256': hashlib.sha256(path.read_bytes()).hexdigest(),
        'coefficient_boxes_checked': checked,
        'reduced_irreducible_forms': len(rows),
        'distinct_discriminants': sorted({row['discriminant'] for row in rows}),
        'minima': minima,
        'symbolic_identities': identities,
        'dyadic_residue_checks': residues,
        'dyadic_lift_diagnostics': cases,
        'dyadic_lowering_steps': steps,
        'normalized_orbit_parity_diagnostics': audit_orbit_parity(),
        'external_number_field_classification_used': False,
        'complete_solution': False,
        'scope': 'Finite enumeration plus symbolic identities; general completeness and descent are proved in the note.',
    }
    output = artifact_path('verification_i3_cubic_discriminant_minima.json')
    output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
