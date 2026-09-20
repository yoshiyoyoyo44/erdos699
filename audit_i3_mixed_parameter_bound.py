"""Exact checks and finite fibers for the mixed parameter D = w - 4*lambda.

The proof is in i3_mixed_parameter_bound_2026-09-20.md. Fiber outputs satisfy
only the stated relaxed conditions. They are NOT Erdos 699 counterexamples.
No attachment-wide search or previous integer-point computation is repeated.
"""

import argparse
import json
from fractions import Fraction
from math import gcd, isqrt
from pathlib import Path


def v2(value):
    assert value
    value = abs(value)
    return (value & -value).bit_length() - 1


def delta(value):
    return 3 if value % 3 == 0 and value % 9 != 0 else 1


def chi(v):
    return 1 if v == 0 else 8 if v == 1 else 2 ** (v + 1)


def quantities(n, j, d1, d2):
    q = Fraction(n - 2, 2 * d2)
    z = Fraction(d1 * ((n - 2 * j) ** 2 - n), 2 * (n - 1))
    rho = Fraction(d1 * j * (j - 1), 2 * (n - 1))
    r = 2 * rho - d1
    w = (z * z - d1 * d1) / q
    lam = rho * (rho - d1) / q
    return z, rho, r, w, lam


def quadratic_coefficients(D, d, d1, d2):
    dd = d1 * d2
    return (
        D * D - 12 * dd * d * D + 4 * dd * dd * d * d,
        4 * d2 * d * d * (2 * dd * d - 3 * D - 8 * d1 * dd),
        4 * d2 * d2 * d * d * (9 * d * d - 16 * d1 * d - 4 * d1 * d1),
    )


def integer_roots(a, b, c):
    assert a != 0
    disc = b * b - 4 * a * c
    if disc < 0:
        return []
    root = isqrt(disc)
    if root * root != disc:
        return []
    return sorted({num // (2 * a) for num in (-b - root, -b + root)
                   if num % (2 * a) == 0})


def relaxed_candidate(n, j, d1, d2, D, d):
    if n < 35 or n % 4 or not (4 <= j <= n // 2):
        return False
    if (delta(n - 1), delta(n // 2 - 1)) != (d1, d2):
        return False
    q1, q = (n - 1) // d1, (n // 2 - 1) // d2
    if j * (j - 1) % q1 or j * (j - 1) * (j - 2) % q:
        return False
    z, rho, r, w, lam = quantities(n, j, d1, d2)
    if any(t.denominator != 1 for t in (z, rho, w, lam)):
        return False
    return z - r == d and w - 4 * lam == D


def finite_fiber(D):
    """Exhaust all relaxed candidates with this D and n >= 35, via (9)-(11)."""
    if not D or D % 2 == 0:
        return {'D': D, 'quadratics_checked': 0, 'relaxed_candidates': []}
    sign = 1 if D > 0 else -1
    candidates = []
    count = 0
    for d1, d2 in ((1, 1), (1, 3), (3, 1)):
        dd = d1 * d2
        max_abs_d = (4 * abs(D) - 1) // dd
        for abs_d in range(1, max_abs_d + 1, 2):
            d = sign * abs_d
            coeffs = quadratic_coefficients(D, d, d1, d2)
            count += 1
            for x in integer_roots(*coeffs):
                n = x + 2
                if n < 35 or n >= 18 * D * D + 21:
                    continue
                numerator = (D + 2 * dd * d) * x + 6 * d2 * d * (2 * d1 - d)
                denominator = 8 * dd * d
                if numerator % denominator:
                    continue
                j = numerator // denominator
                if relaxed_candidate(n, j, d1, d2, D, d):
                    candidates.append({'n': n, 'j': j, 'delta1': d1,
                                       'delta2': d2, 'd': d})
    return {'D': D, 'quadratics_checked': count,
            'relaxed_candidates': sorted(candidates, key=lambda c: (c['n'], c['j'])),
            'interpretation': 'Necessary relaxed conditions only; not counterexamples.'}


def fixed_n_index(n, D, d1, d2):
    """Find the unique possible index by monotonicity of equation (15)."""
    assert n >= 16
    c0 = d1*d1*d2
    denominator = 2*(n-2)*(n-1)**2

    def compare(j):
        minus = 2*j*j-4*j*n+2*j+n*n+n-2
        plus = 6*j*j-4*j*n-2*j+n*n-3*n+2
        return c0*minus*plus-D*denominator

    lo, hi = 4, n//2+1
    while lo < hi:
        mid = (lo+hi)//2
        if compare(mid) > 0:
            lo = mid+1
        else:
            hi = mid
    return lo if lo <= n//2 and compare(lo) == 0 else None


def normalized_fiber(D):
    """Enumerate normalized necessary candidates using (13)-(15)."""
    from sympy import divisors

    candidates = []
    counts = {'odd_divisors_checked': 0, 'n_values_checked': 0}
    if not D or D % 2 == 0:
        return {'D': D, **counts, 'normalized_necessary_candidates': []}
    for gamma, d1, d2 in ((1,1,1), (1,1,3), (1,3,1), (3,1,1)):
        c0 = d1*d1*d2
        if D == c0:
            continue  # Equation (1) contradicts the inherited u >= 49 bound.
        for T in divisors(abs(D-c0)):
            T = int(T)
            if T % 2 == 0 or gcd(T, gamma*d1*d2) != 1:
                continue
            counts['odd_divisors_checked'] += 1
            M = gamma*T
            if (3 if M % 3 == 0 and M % 9 else 1) != gamma:
                continue
            u = 49
            while d1*gamma*T*T*2**u < 18*D*D+21*d1*T:
                n = gamma*T*2**u
                if M**3 < 2**(u-2) and (delta(n-1),delta(n//2-1)) == (d1,d2):
                    counts['n_values_checked'] += 1
                    j = fixed_n_index(n,D,d1,d2)
                    if j is not None and j % T == 0:
                        z,rho,r,w,lam = quantities(n,j,d1,d2)
                        d = z-r
                        if d.denominator == 1 and relaxed_candidate(n,j,d1,d2,D,int(d)):
                            v = v2(j)
                            if (v == 0 or u >= 4*v+14) and d1*chi(v)*T*(n-21) < 18*D*D:
                                candidates.append({'n': n, 'j': j, 'T': T, 'u': u,
                                                   'gamma': gamma, 'delta1': d1, 'delta2': d2})
                u += 1
    return {'D': D, **counts, 'normalized_necessary_candidates': candidates,
            'interpretation': 'Full Kummer conditions still required if any candidate survives.'}


def symbolic_checks():
    import sympy as s

    n, j, a, b, d, D, x, y = s.symbols('n j a b d D x y')
    z = a * ((n - 2 * j) ** 2 - n) / (2 * (n - 1))
    r = a * j * (j - 1) / (n - 1) - a
    P = 6 * x * x - 4 * x + 1
    f = a * (2 * j*j - 4*j*n + 2*j + n*n + n - 2) - 2*d*(n-1)
    g = D*(n-2)*(n-1) - a*b*d*(6*j*j - 4*j*n - 2*j + n*n - 3*n + 2)
    coeffs = quadratic_coefficients(D, d, a, b)
    polynomial = sum(c * (n - 2) ** (2 - i) for i, c in enumerate(coeffs))
    checks = [
        z-r - a*(2*j*j - 4*j*n + 2*j + n*n + n-2)/(2*(n-1)),
        z+r - a*(6*j*j - 4*j*n - 2*j + n*n - 3*n+2)/(2*(n-1)),
        10*P-(6*x+1) - (60*(x-s.Rational(23,60))**2+s.Rational(11,60)),
        9*(18*P**2-4*x*(x+1)).subs(x,(y+1)/3)
        - (72*y**4+68*(y-s.Rational(5,34))**2+s.Rational(9,17)),
        s.resultant(f,g,j)-4*a*a*(n-1)**2*polynomial,
        g+3*b*d*f-(n-1)*(D*(n-2)-8*a*b*d*j+2*a*b*d*n+8*a*b*d-6*b*d*d),
        (j*(4-j))*(j*(4-j)-3)*(j*(4-j)-6)
        + j*(j-1)*(j-3)*(j-4)*((j-2)**2+2),
        (2*n*n-22*n+11)*4-6*(n-1)*(n-2)-2*(n*n-35*n+16),
        s.diff((z*z-r*r)*2*b/(n-2),j)
        - 4*a*a*b*(6*j*(n-j)**2-n**3+3*j*j-3*j+n*n-n+1)/((n-2)*(n-1)**2),
    ]
    for expr in checks:
        assert s.factor(expr) == 0
    return len(checks)


def valuation_checks():
    count = 0
    seen = set()
    for u in (3, 4, 8, 16):
        for T in (1, 5, 7, 25):
            n = T * 2**u
            for k in range(1, min(2**(u-1), 65)):
                j = T * k
                v = v2(j)
                numerator = j * (j+n-2)
                value = v2(numerator)
                if v == 0:
                    assert value == 0
                elif v == 1:
                    assert value >= 3
                else:
                    assert value == v+1
                assert numerator % (chi(v)*T) == 0
                seen.add('odd' if v == 0 else 'v=1' if v == 1 else 'v>=2')
                count += 1
    assert len(seen) == 3
    return {'numerators_checked': count, 'branches': sorted(seen)}


def check_model(n, j):
    d1, d2 = delta(n-1), delta(n//2-1)
    z, rho, r, w, lam = quantities(n,j,d1,d2)
    assert all(t.denominator == 1 for t in (z,rho,r,w,lam))
    z, r, w, lam = map(int,(z,r,w,lam))
    q1, q = (n-1)//d1, (n//2-1)//d2
    assert j*(j-1) % q1 == 0 and j*(j-1)*(j-2) % q == 0
    A, B, C = gcd(q,j-1), gcd(q,j), gcd(q,j-2)
    assert A*B*C == q
    d, D = z-r, w-4*lam
    assert d % (A*C) == 0 and (z+r) % B == 0
    ell, m = d//(A*C), (z+r)//B
    assert ell*m == D and D % 2 and m > 0
    L = Fraction(d1*j*(j+n-2), (n-1)*B*B)
    # T=1 is valid for the relaxed theorem; it is not a claim about M=n/2^u.
    assert L.denominator == 1 and L % chi(v2(j)) == 0
    assert d1*chi(v2(j))*(n-21) < 18*D*D
    assert d1*d2*abs(d) < 4*abs(D)
    a,b,c = quadratic_coefficients(D,d,d1,d2)
    assert a*(n-2)**2+b*(n-2)+c == 0
    assert fixed_n_index(n,D,d1,d2) == j
    return {'n': n, 'j': j, 'D': D, 'd': d, 'v': v2(j), 'L_B': int(L)}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--D', type=int, help='Enumerate this signed fixed mixed parameter.')
    parser.add_argument('--normalized-D', type=int, help='Use divisors and n=gamma*T*2^u for this D.')
    args = parser.parse_args()
    if args.D is not None:
        print(json.dumps(finite_fiber(args.D), ensure_ascii=False, indent=2))
        return
    if args.normalized_D is not None:
        print(json.dumps(normalized_fiber(args.normalized_D), ensure_ascii=False, indent=2))
        return
    symbolic = symbolic_checks()
    valuations = valuation_checks()
    models = []
    for t in range(12):
        A, B, C = 18*t+11, 144*t+85, 72*t+41
        n, j = 2*A*B*C+2, (108*t+63)*B*(8*t+5)
        models.append(check_model(n,j))
    models.append(check_model(175492,60606))
    fibers = [finite_fiber(-1963), finite_fiber(-4189)]
    for fiber, expected in zip(fibers, ((76672,26775),(175492,60606))):
        assert expected in {(c['n'],c['j']) for c in fiber['relaxed_candidates']}
    normalized = [normalized_fiber(D) for D in (67108865,-67108865)]
    result = {'status': 'passed', 'symbolic_identities': symbolic,
              'valuation_checks': valuations, 'relaxed_models_checked': len(models),
              'diagnostic_models': [models[0],models[-1]], 'fixed_parameter_fibers': fibers,
              'normalized_fixed_parameter_fibers': normalized,
              'scope': 'Exact algebra and finite-fiber checks, not a complete solution of i=3.'}
    path = Path(__file__).with_name('verification_i3_mixed_parameter_bound.json')
    path.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(result, ensure_ascii=False, indent=2))


if __name__ == '__main__':
    main()
