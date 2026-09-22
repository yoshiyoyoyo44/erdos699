"""Audit the all-even-j multiplicity budget and fresh-support product.

Infinite statements are proved in the accompanying note. Symbolic identities
are exact; exponent patterns and artificial support allocations are checks of
the algebra, not a search for counterexamples to Erdos 699.
"""

import json
from fractions import Fraction
from itertools import product
from math import gcd

import sympy as sp

from repo_paths import artifact_path


def symbolic_checks():
    A, Bc, T, x, P, ab, d1, d2 = sp.symbols(
        'A Bc T x P ab d1 d2', nonzero=True)
    delta, c0 = d1*d2, d1*d1*d2
    n = 2*d2*A*Bc+2
    H1, H2 = delta*A-2*T*T*x*x*P, delta*A-T*T*x*x*P
    W = (delta*Bc-A*ab)/(T*x*x)
    w = H1*(delta*Bc-2*A*ab)
    m = (w-c0)/(4*T*x**4)
    BG = c0*n/(8*T*x**4)
    q = T*P*W
    Z = (A*W-T*Bc*P)/2
    D = d1*n/(4*T*x*x)
    lam = H1/(delta*A)
    scale = d1**3*d2**2*n/(16*T**4*x**4)
    substitute = {Bc: (A*A*ab+d1)/(T*T*x*x*P)}
    checks = {
        'center_sum': BG-m-T*q,
        'center_factor_plus': D+Z-A*W,
        'center_factor_minus': D-Z-T*Bc*P,
        'center_difference_of_squares': D*D-Z*Z-q*A*Bc,
        'center_first_square': d2*Z*Z-m*n/(2*T)-q,
        'center_linear': d2*A*Z-T*P-n*H1/(4*T*x*x),
        'center_m_norm': d2*m*A*A+T**3*P*P-n*H1**2/(8*T*x**4),
        'center_q_norm': d2*q*A*A-T*T*P*P-n*P*H2/(2*x*x),
        'lambda_center_ratio': m/BG-lam**2+2*(1-lam)**2/n,
        'exact_abP_squared': ab*P*P-scale*(1-lam)**2*((n-2)*(1-lam)-4)/n,
        'ab_q_bridge': T*T*x**4*q-c0-A*ab*H2,
        'ab_m_bridge': c0*(n-8)-8*T*x**4*m-8*A*ab*H2,
    }
    for name, expression in checks.items():
        assert sp.cancel(expression.subs(substitute)) == 0, name

    z = sp.Symbol('z')
    a1, a2, a3, a4, a6 = 1, z/4, 0, z/16, 0
    b2 = a1*a1+4*a2
    b4 = 2*a4+a1*a3
    b6 = a3*a3+4*a6
    b8 = a1*a1*a6+4*a2*a6-a1*a3*a4+a2*a3*a3-a4*a4
    c4 = b2*b2-24*b4
    c6 = -b2**3+36*b2*b4-216*b6
    disc = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    curve_checks = {
        'direct_c4': c4-(z*z-z+1),
        'direct_c6': c6+(z+1)*(2*z*z-5*z+2)/2,
        'direct_discriminant': disc-z*z*(z-1)**2/256,
        'invariant_relation': c4**3-c6**2-1728*disc,
        'c4_mod_z': c4.subs(z, 0)-1,
        'c4_mod_z_minus_one': c4.subs(z, 1)-1,
    }
    for name, expression in curve_checks.items():
        assert sp.expand(expression) == 0, name
    return list(checks)+list(curve_checks)


def multiplicity_patterns():
    rows = []
    # At p>=5 the determinant prevents p|ab and p|P simultaneously.
    for ea, ep in product(range(25), repeat=2):
        if ea and ep:
            continue
        eq = int(ea > 0)+2*int(ep % 3 != 0)
        defect = ea+2*ep-eq
        reconstructed = max(ea-1, 0)+6*(ep//3)+2*int(ep % 3 == 2)
        assert defect == reconstructed >= 0
        assert defect >= 6*(ep//3)
        if ea >= 2:
            assert defect >= 1
        if ep >= 2:
            assert defect >= 2
        rows.append({'v_ab':ea, 'v_P':ep, 'v_Q':eq, 'v_defect':defect})
    return rows


def support_patterns():
    rows = []
    # Complete block allocation: a prime is in at most one of these blocks.
    for block, in_ab, in_P in product(('T','A','B','C','R','S','none'), (0,1), (0,1)):
        if in_ab and in_P:
            continue
        if in_ab and block in ('T','B','C'):
            continue
        if in_P and block == 'A':
            continue
        rt = int(block == 'T')
        r1 = int(block in ('T','R','S'))
        r2 = int(block in ('T','A','B','C'))
        fresh = int((block == 'A' and not in_ab) or (block in ('B','C') and not in_P)
                    or (block in ('R','S') and not in_ab and not in_P))
        assert r1+r2 <= 2*rt+in_ab+in_P+fresh
        rows.append({'block':block, 'in_ab':in_ab, 'in_P':in_P,
                     'left_exponent':r1+r2, 'right_exponent':2*rt+in_ab+in_P+fresh})
    return rows


def direct_curve_diagnostics():
    count = 0
    for z in range(16, 16001, 16):
        c4 = z*z-z+1
        numerator = z*z*(z-1)**2
        assert numerator % 256 == 0
        disc = numerator//256
        assert gcd(c4, z*(z-1)) == 1
        assert disc > Fraction(z**4, 1024)
        v2_z = (z & -z).bit_length()-1
        assert (disc & -disc).bit_length()-1 == 2*v2_z-8
        count += 1
    return count


def constants():
    rows = []
    for gamma,d1,d2 in ((1,1,1),(1,1,3),(1,3,1),(3,1,1)):
        kappa = Fraction(gamma*d1**3*d2**2,16)
        assert 486*kappa < 2**10
        assert 972*kappa <= Fraction(6561,4)
        assert 1/(81*kappa) >= Fraction(16,2187)
        rows.append({'branch':[gamma,d1,d2], 'kappa':str(kappa),
                     'budget_coefficient':str(972*kappa),
                     'fresh_support_coefficient':str(1/(81*kappa))})
    # Direct models: log_2 Delta > 4u-10 or 4u-14;
    # log_2 Delta < 18 R b^2+186.
    assert Fraction(186+10,4) == 49
    assert Fraction(186+14,4) == 50
    assert Fraction(6561,4)*Fraction(2**20,2**20-124) < 1641
    return rows


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    identities = symbolic_checks()
    valuations = multiplicity_patterns()
    allocations = support_patterns()
    curves = direct_curve_diagnostics()
    branch_constants = constants()
    result = {
        'status':'passed',
        'symbolic_identities':identities,
        'multiplicity_patterns':valuations,
        'support_allocations':allocations,
        'synthetic_direct_curves':curves,
        'branch_constants':branch_constants,
        'external_input':'von Kaenel, arXiv:1310.7263v2, Corollary 6.2; inherited first-curve bound and normalization.',
        'scope':'General necessary inequalities for all even-j branches, not elimination of the general branch. Finite diagnostics do not prove the infinite statements.',
        'complete_solution':False,
    }
    artifact_path('verification_i3_multiplicity_and_fresh_support.json').write_text(
        json.dumps(result,indent=2)+'\n',encoding='utf-8',newline='\n')
    print(json.dumps({'status':'passed','symbolic_identities':len(identities),
                      'multiplicity_patterns':len(valuations),'support_allocations':len(allocations),
                      'synthetic_direct_curves':curves,'branch_constants':len(branch_constants)},indent=2))


if __name__ == '__main__':
    main()
