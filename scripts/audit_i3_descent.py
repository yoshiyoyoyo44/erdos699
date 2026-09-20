"""Check the descent identities and constructive local-solubility examples.

The general proofs are in i3_gap13_and_descent_continuation.md. The modular
examples below are checks of that construction, not evidence for integer points.
"""
from repo_paths import artifact_path
import json
from math import gcd
from pathlib import Path
import sympy as sy


def algebra():
    n, j, x, d1, d2 = sy.symbols('n j x d1 d2')
    r = j / x
    a = d1 * j * (j - 1) / (x * (n - 1))
    b = d2 * a * (j - 2) / (n - 2)
    E = 2 * (d2 * a - b) / x
    D = 2 * (d2 * a * a - d1 * b * r) / x
    identities = [(j - 1) * D - a * E,
                  (n - 1) * D - d1 * r * E,
                  (n - 2) * E - 2 * d2 * a * (n - j) / x,
                  D - 2 * d1**2 * d2 * j**2 * (j - 1) * (n - j) / (x**3 * (n - 1)**2 * (n - 2)),
                  (n - 2) * (d2 * a**2 - d1 * b * r) - d2 * a * (d1 * r - a),
                  d1 * r - a - x * d1 * r**2 + n * a]
    A, B, C, R, S, aa, G, H, T = sy.symbols('A B C R S aa G H T')
    jj = T * S * B * x * G
    complement = T * R * C * x * H
    jm1 = R * A * aa
    q1, q2 = R * S, A * B * C
    identities += [jj * jm1 * complement / (x**2 * q1 * q2) - T**2 * R * aa * G * H,
                   jj**2 * jm1 * complement / (x**3 * q1**2 * q2) - T**3 * B * aa * G**2 * H]
    assert all(sy.factor(expr) == 0 for expr in identities)
    return len(identities)


def fourth_root(q, precision):
    assert q % 16 == 1
    c = 1
    for k in range(4, precision):
        if (c**4 - q) % 2**(k + 1):
            c += 2**(k - 2)
        assert (c**4 - q) % 2**(k + 1) == 0
    assert (c**4 - q) % 2**precision == 0
    return c


def local_examples():
    checked = 0
    for h in (2, 3, 4):
        gap = 4 * h + 1
        B = 2**(gap - 3)
        for m in sorted({15, B // 2 - 1, B - 17, B - 1}):
            assert 0 < m < B and m % 16 == 15
            for precision in (1, 4, 8, 16, 32):
                twopart = 2**precision
                c2 = fourth_root(B - m, precision)
                z2 = -c2 * c2 % twopart
                for odd in (3, 5, 7, 9, 17, 35, 73, 97, 151):
                    order = 1
                    while pow(2, order, odd) != 1:
                        order += 1
                    v = (-h) % order
                    minimum = max(precision, 9)
                    v += max(0, (minimum - v + order - 1) // order) * order
                    zstar, cstar = 2**(2 * h - 1), 2**h
                    z = z2 + twopart * ((zstar - z2) * pow(twopart, -1, odd) % odd)
                    c = c2 + twopart * ((cstar - c2) * pow(twopart, -1, odd) % odd)
                    modulus = twopart * odd
                    xx = pow(2, v, modulus)
                    n = pow(2, 4 * v + gap, modulus)
                    assert (z*z - m * 2**(gap-1) * xx**4 - B + m) % modulus == 0
                    assert (c*c - 2**(gap-2) * xx**2 - (n-1)*z) % modulus == 0
                    assert z % 2 and c % 2
                    checked += 1
    return checked


def failed_general_shift():
    # This satisfies the relaxed divisibilities; it is not an Erdos counterexample.
    n, j = 175492, 60606
    assert j * (j-1) % (n-1) == 0
    assert j * (j-1) * (j-2) % (n//2-1) == 0
    s = j * (j-1) // (n-1)
    t = s * (j-2) // (n//2-1)
    assert s * (j-2) % (n//2-1) == 0 and 0 < t < s < j//2
    smaller_n, smaller_j = n//2, s//2
    assert smaller_j * (smaller_j-1) % (smaller_n-1) == 0
    residue = smaller_j * (smaller_j-1) * (smaller_j-2) % (smaller_n//2-1)
    assert residue == 27840
    return {'original_n': n, 'original_j': j, 's': s, 't': t,
            'smaller_n': smaller_n, 'smaller_j': smaller_j,
            'second_condition_remainder': residue,
            'pure_power_of_two': False, 'erdos_counterexample': False}


def main():
    result = {'status': 'verified', 'symbolic_identities': algebra(),
              'constructed_modular_examples': local_examples(),
              'general_shift_failure': failed_general_shift(),
              'independent_new_constraint_from_D_E': False,
              'complete_descent': False, 'complete_i3_solution': False}
    artifact_path('verification_i3_descent.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
