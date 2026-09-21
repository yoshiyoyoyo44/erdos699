"""Exact audits for quadratic twists and the Kummer cofactor bridge.

General proofs are in the accompanying note. Symbolic identities and six
residue classes are checked exactly; finite valuation diagnostics supplement
them. External curve-table completeness and height theorems are not reproved.
"""
import json
from fractions import Fraction

import sympy as sp

from repo_paths import artifact_path


def symbolic_checks():
    D, A, B, C, N, X = sp.symbols('D A B C N X')
    a2 = (D*A-1)/4
    a4 = D**2*N*B/16
    a6 = D**3*N**2*C/64
    b2 = 1+4*a2
    b4 = 2*a4
    b6 = 4*a6
    b8 = (1+4*a2)*a6-a4*a4
    c4 = b2*b2-24*b4
    c6 = -b2**3+36*b2*b4-216*b6
    delta = -b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
    H = A*A-3*N*B
    J = 2*A**3-9*N*A*B+27*N*N*C
    cubic_delta = sp.discriminant(N+A*X+B*X*X+C*X**3, X)
    checks = {
        'twist_c4': c4-D*D*H,
        'twist_c6': c6+D**3*J/2,
        'twist_discriminant': delta-D**6*N*N*cubic_delta/256,
        'twist_j_invariant': c4**3/delta-256*H**3/(N*N*cubic_delta),
    }
    A0, B0, C0, R0, S0, T, a, b, G0, H0 = sp.symbols(
        'A0 B0 C0 R0 S0 T a b G0 H0', nonzero=True)
    eps, eta, gam, d1, d2, x = sp.symbols(
        'eps eta gam d1 d2 x', nonzero=True)
    jj = T*S0*B0*G0
    yy = T*R0*C0*H0
    jm1 = R0*A0*a
    ym1 = S0*A0*b
    nm1 = d1*R0*S0
    nm2 = 2*d2*A0*B0*C0
    K = x*gam*T
    g = eta*A0
    ell = nm2/(2*g)
    k = K/eps
    ss = (3*jj*yy/(K*nm1))/(k*ell)
    ww = 3*jm1*ym1/(g*g*nm1)
    s_bridge = 3*eps*eta*G0*H0/(x*x*gam*gam*d1*d2)
    w_bridge = 3*a*b/(d1*eta*eta)
    delta_blocks = 27*a*b*G0*G0*H0*H0/(x**4*gam**4*d1**3*d2**2)
    delta_direct = 108*jj**2*yy**2*jm1*ym1/(K**4*nm1**3*nm2**2)
    checks.update({
        's_kummer_bridge': ss-s_bridge,
        'W_kummer_bridge': ww-w_bridge,
        'discriminant_direct_blocks': delta_direct-delta_blocks,
        'discriminant_s_W_blocks': s_bridge**2*w_bridge/eps**2-delta_blocks,
    })
    for name, expression in checks.items():
        assert sp.cancel(expression) == 0, name
    return list(checks)


def nonnegative_polynomial(expression, a, z):
    # With a,z >= 0, nonnegative coefficients give a general certificate.
    return all(coefficient >= 0 for coefficient in sp.Poly(expression, a, z).coeffs())


def residue_certificates():
    a, z = sp.symbols('a z', integer=True, nonnegative=True)
    rows = []
    for r in range(6):
        m = 6*a+r
        d = int(r >= 3)
        q = a+d
        c4_order = sp.expand(m+2*d+z-4*q)
        c6_order = sp.expand(m+3*d-6*q)
        delta_order = sp.expand(2*m+6*d-12*q)
        assert nonnegative_polynomial(c4_order, a, z)
        assert 0 <= c6_order < 6  # q works, but q+1 cannot work
        assert delta_order == 2*(r % 3)
        if delta_order:
            assert nonnegative_polynomial(c4_order-1, a, z)
        # Any twist has one of these two residues modulo 12. A minimal
        # integral model has nonnegative valuation, proving optimality.
        alternatives = [(2*r+6*choice) % 12 for choice in (0, 1)]
        assert min(alternatives) == delta_order
        rows.append({
            'm_mod_6':r, 'twist_order':d, 'scale_order':str(q),
            'minimal_c4_order':str(c4_order),
            'minimal_c6_order':int(c6_order),
            'minimal_delta_order':int(delta_order),
            'alternative_residues_mod_12':alternatives,
        })
    return rows


def valuation_diagnostics():
    count = 0
    for m in range(1, 601):
        for ell_order in range(15):
            choices = []
            for d in (0, 1):
                q = min((m+2*d+ell_order)//4, (m+3*d)//6)
                choices.append(2*m+6*d-12*q)
            selected = int(m % 6 >= 3)
            assert choices[selected] == min(choices) == 2*(m % 3)
            assert (min(choices) == 0) == (m % 3 == 0)
            count += 1
    # Sign choices always retain an integral a2 at 2.
    sign_cases = 0
    for A in range(1, 32, 2):
        for d_abs in range(1, 32, 2):
            D = d_abs if (d_abs*A) % 4 == 1 else -d_abs
            assert (D*A-1) % 4 == 0
            sign_cases += 1
    # Exact threshold used by the inherited conductor-height bound.
    ratio = Fraction(972*900, 2**20)+Fraction(124, 2**40)
    assert ratio < 1
    return {'local_valuation_pairs':count, 'odd_sign_cases':sign_cases,
            'growth_threshold_ratio':str(ratio)}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    identities = symbolic_checks()
    residues = residue_certificates()
    diagnostics = valuation_diagnostics()
    result = {
        'status':'passed',
        'symbolic_identities':identities,
        'symbolic_residue_certificates':residues,
        'diagnostics':diagnostics,
        'conclusions':[
            'An explicit odd quadratic twist preserves the minimal discriminant valuation at 2.',
            'For p>=5 dividing s, the optimal minimal discriminant valuation among quadratic twists is 2*(v_p(s) mod 3).',
            'For p>=5 dividing W, no quadratic twist has good reduction.',
            'The conductor is 2*3^f3*Q with Q=rad_ge5(ab)*rad_ge5(cubefree(G0*H0))^2 and 0<=f3<=5.',
            'All previous support-table and growth exclusions apply to this smaller support.',
        ],
        'external_dependencies':[
            'Concrete small-support exclusions reuse vKM full curve lists audited in verification_i3_discriminant_support.json.',
            'The growth bound reuses von Kaenel arXiv:1310.7263v2, Corollary 6.2.',
        ],
        'remaining':'No uniform upper bound on Q from all-digit Kummer conditions; i=3 remains unresolved.',
    }
    output = artifact_path('verification_i3_twist_and_kummer_support.json')
    output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'status':'passed', 'symbolic_identities':len(identities),
                      'symbolic_residue_classes':len(residues), **diagnostics,
                      'output':'data/results/verification_i3_twist_and_kummer_support.json'}, indent=2))


if __name__ == '__main__':
    main()
