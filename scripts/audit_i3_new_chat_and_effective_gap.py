"""Audit the new chat results and the effective bound in G=u-4*v.

Symbolic identities complement the general proofs in the note. Modular
diagnostics check a local consequence only, not actual counterexamples.
The conductor-height theorem is an external, previously verified input.
"""
import hashlib
import json
from fractions import Fraction
from math import gcd
from random import Random

import sympy as sp

from repo_paths import ROOT, artifact_path


def symbolic_checks():
    A, Z, T, x, P, a, b, d1, d2 = sp.symbols(
        'A Z T x P a b d1 d2', nonzero=True)
    delta = d1*d2
    c0 = d1*d1*d2
    n = 2*d2*A*Z+2
    F = T*T*x*x*Z*P-A*A*a*b-d1
    w = (delta*A-2*T*T*x*x*P)*(delta*Z-2*A*a*b)
    W = (delta*Z-A*a*b)/(T*x*x)
    m = (w-c0)/(4*T*x**4)
    BG = c0*n/(8*T*x**4)
    q = (BG-m)/T
    checks = {
        'center_identity_mod_determinant': c0*(n+2)-2*w-8*T**3*x**4*P*W+4*delta*F,
        'q_exact_identification': (q-T*P*W).subs(Z, (A*A*a*b+d1)/(T*T*x*x*P)),
        'mersenne_sum': (A*W+T*Z*P-d1*n/(2*T*x*x)).subs(Z, (A*A*a*b+d1)/(T*T*x*x*P)),
    }
    B, C, g, h, ww = sp.symbols('B C g h ww', nonzero=True)
    F1 = a*B*g+b*C*h-2*x*ww
    F2 = delta*B*C-A*a*b-T*x*x*ww
    norm = B*((A*a*g)**2+delta*A*g*h*C*C)-A*g*x*ww*(2*A*a+T*x*C*h)
    checks['prime_power_norm_certificate'] = norm-A*g*(A*a*F1+C*h*F2)
    R, S = sp.symbols('R S', nonzero=True)
    j = T*S*B*x*g
    y = T*R*C*x*h
    jm1 = R*A*a
    ym1 = S*A*b
    rho = j*jm1/(2*R*S)
    rho_y = y*ym1/(2*R*S)
    checks.update({
        'rho_block_identity':rho-T*A*B*a*x*g/2,
        'rho_y_block_identity':rho_y-T*A*C*b*x*h/2,
        'lambda_quotient':rho*(rho-d1)/(A*B*C)-T*x*a*g*(rho-d1)/(2*C),
        'lambda_y_quotient':rho_y*(rho_y-d1)/(A*B*C)-T*x*b*h*(rho_y-d1)/(2*B),
    })
    nn, gam, E = sp.symbols('nn gam E', positive=True)
    p_bound = d1**3*d2*d2*(nn-2)**2/(16*T**4*x**4*(nn-1))
    w_bound = d1*(nn-1)/(4*T*T*x**4)
    coef = gam*d1**3*d2*d2/16
    checks['P_bound_reexpression'] = p_bound.subs(nn,gam*T*E*x**4)-(coef*E/T**3*(nn-2)**2/(nn*(nn-1))).subs(nn,gam*T*E*x**4)
    checks['W_bound_reexpression'] = w_bound.subs(nn,gam*T*E*x**4)-(d1*gam*E/(4*T)*(1-1/nn)).subs(nn,gam*T*E*x**4)
    checks['W_to_P_bound_ratio'] = w_bound/p_bound-(2*T/delta*(nn-1)/(nn-2))**2
    K = x*gam*T
    scale = gam**4*d1**3*d2*d2/27
    checks['abP_squared_bound'] = (27*nn/(16*K**4)*scale).subs(nn,gam*T*E*x**4)-coef*E/T**3
    checks['refined_abP_bound'] = 27*nn**2*(nn-4)/(16*K**4*(nn-2)**2)*scale-(27*nn/(16*K**4)*scale)*nn*(nn-4)/(nn-2)**2
    checks['even_discriminant'] = 27*a*b*(x*g)**2*(x*h)**2/(x**4*gam**4*d1**3*d2**2)-27*a*b*(g*h)**2/(gam**4*d1**3*d2**2)
    for name, expression in checks.items():
        assert sp.cancel(expression) == 0, name
    return list(checks)


def modular_diagnostics():
    rng = Random(699)
    count = 0
    w_values = (1, 5, 7, 9, 25, 27, 49, 125, 343, 385)
    def unit(modulus):
        while True:
            value = rng.randrange(1, modulus)
            if gcd(value, modulus) == 1:
                return value
    for v in range(1, 9):
        for W in w_values:
            L = 2**(v+1)*W
            for delta in (1, 3):
                if gcd(delta, L) != 1:
                    continue
                for _ in range(10):
                    A, B, C, a, g = (unit(L) for _ in range(5))
                    b = delta*B*C*pow(A*a, -1, L) % L
                    h = -a*B*g*pow(b*C, -1, L) % L
                    assert (a*B*g+b*C*h) % L == 0
                    assert (delta*B*C-A*a*b) % L == 0
                    root = A*a*g*pow(C, -1, L) % L
                    assert (root*root+delta*A*g*h) % L == 0
                    if v >= 2:
                        assert (delta*A*g*h) % 8 == 7
                    count += 1
    return {'local_congruence_cases':count,
            'scope':'Artificial local data satisfying the two input congruences; not solutions of the full counterexample system.'}


def effective_bound_checks():
    rows = []
    for gam, d1, d2 in ((1,1,1),(1,1,3),(1,3,1),(3,1,1)):
        C = Fraction(gam*d1**3*d2**2, 16)
        assert 486*C < 2**10
        assert 972*C == Fraction(243*gam*d1**3*d2**2,4)
        rows.append({'gamma':gam,'delta1':d1,'delta2':d2,
                     'C':str(C),'u_bound_coefficient':str(972*C)})
    threshold = Fraction(6561*31**2,4*2**21)+Fraction(124,2**42)
    assert threshold == Fraction(826424819743,1099511627776) < 1
    assert Fraction(1,31) < Fraction(1,3)  # log(2)>2/3 gives negative derivative
    return {'branches':rows,'threshold_ratio':str(threshold),
            'explicit_bound':'u < (6561/4)*2^G*(G+10)^2 + 124',
            'slow_gap_exclusion':'u>=2^42 implies G>(log_2 u)/2',
            'asymptotic':'G >= log_2(u)-2*log_2(log_2(u))-O(1)',
            'external_input':'von Kaenel, arXiv:1310.7263v2 Corollary 6.2, through the previous note'}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    identities = symbolic_checks()
    diagnostics = modular_diagnostics()
    bounds = effective_bound_checks()
    source = ROOT/'sources'/'source_i3_new_chat_results_2026-09-21.md'
    result = {
        'status':'passed','source_file':str(source.relative_to(ROOT)),
        'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
        'symbolic_identities':identities,'diagnostics':diagnostics,'bounds':bounds,
        'scope':'Even j only. General proofs are in the note; finite diagnostics do not prove infinite statements.',
        'complete_solution':False,
        'remaining':'G satisfying the logarithmic lower bound can still grow; odd j is not treated in this note.',
    }
    artifact_path('verification_i3_new_chat_and_effective_gap.json').write_text(
        json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','symbolic_identities':len(identities),
                      **diagnostics,'threshold_ratio':bounds['threshold_ratio']},indent=2))


if __name__ == '__main__':
    main()
