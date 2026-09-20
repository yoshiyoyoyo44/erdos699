"""Independent finite audit of the all-M square exclusion; no Lean calls."""
from repo_paths import artifact_path
import json
from fractions import Fraction
from math import isqrt
from pathlib import Path
import sympy as sp


def v2(x):
    assert x > 0
    return (x & -x).bit_length() - 1


def main():
    n, ell, sigma, r = sp.symbols('n ell sigma r')
    j = r*n/6 - sigma*ell
    residual = ell**2*(n-1)-j*(n-j)
    square = (6*ell+sigma*(3-r))**2-r*(6-r)*n-(3-r)**2
    for sign in (-1, 1):
        assert sp.expand((n*square-36*residual).subs(sigma, sign)) == 0

    L, H, q = sp.symbols('L H q')
    quad = (L+H)*q**2+2*H*(L-1)*q-(L-H)*L*(L-1)
    R = (L+H)*q+H*(L-1)
    assert sp.expand(R**2-(L-1)*(L**3-H**2)-(L+H)*quad) == 0
    qp = L*(L-1)/q
    assert sp.simplify(q*(H*(q+qp+2*L-2)-L*(qp-q))-quad) == 0

    # Exact endpoint inequalities; their exponent differences increase with u.
    u = 16
    assert 4*u-2 <= 6*u-30
    assert 3*2**(u-6)+2 < 2**(u-3)
    assert 3*2**(u-5)+2 < 2**(u+2)

    rows = ell_checks = square_hits = divisibility_hits = 0
    exceptional = []
    for u in range(4, 21):
        M = 1
        while M**3 < 2**(u-2):
            rows += 1
            n = (1 << u)*M
            g = 3 if M % 3 == 0 and M % 9 else 1
            T = M//g
            for ell in range(1, isqrt(n//4)+1):
                ell_checks += 1
                disc = n*n-4*ell*ell*(n-1)
                assert disc >= 0
                root = isqrt(disc)
                if root*root != disc or (n-root) % 2:
                    continue
                j = (n-root)//2
                if not 4 <= j < n//2:
                    continue
                square_hits += 1
                assert j*(n-j) == ell*ell*(n-1)
                if j % T:
                    continue
                divisibility_hits += 1
                assert ell % T == 0
                if v2(j) > u//4:
                    continue
                exceptional.append({'u':u, 'M':M, 'n':n, 'j':j, 'ell':ell})
                assert u < 16, 'Contradiction to the square exclusion lemma'
            M += 2

    n, j = 76672, 26775
    assert j*(n-j) % (n-1) == 0
    L = j*(n-j)//(n-1)
    assert L*(n//2-j) % (n//2-1) == 0
    H = L*(n//2-j)//(n//2-1)
    q, qp = j-L, n-j-L
    R = (L+H)*q+H*(L-1)
    assert q*qp == L*(L-1)
    assert R*R == (L-1)*(L**3-H**2)
    other = -Fraction((L-H)*qp, L+H)
    assert other < 0 and other.denominator != 1
    assert (n//(1 << v2(n)))**3 >= 2**(v2(n)-2)
    report = {
        'status':'all assertions passed; finite audit, not a complete proof of Erdős 699',
        'symbolic_identities':3,
        'u_range':[4,20], 'M_rows':rows, 'ell_checks':ell_checks,
        'integer_square_hits':square_hits,
        'hits_with_T_dividing_j':divisibility_hits,
        'hits_also_satisfying_v_bound':exceptional,
        'hits_for_u_at_least_16':0,
        'relaxed_example':{'n':n,'j':j,'L':L,'H':H,'q':q,'q_prime':qp,
                           'R':R,'other_q_root':str(other)},
        'lean_calls':0,
    }
    artifact_path('verification_i3_all_square.json').write_text(
        json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
