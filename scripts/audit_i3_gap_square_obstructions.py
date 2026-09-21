"""Exact certificates for uniform square obstructions in the gap equation.

The infinite statements are proved in the accompanying note. Finite checks
below audit branch constants and synthetic factorization cases only.
"""
import json
from fractions import Fraction
from math import gcd, isqrt

import sympy as sp

from repo_paths import artifact_path


BRANCHES = ((1,1,1),(1,1,3),(1,3,1),(3,1,1))


def symbolic_checks():
    d1,d2,gamma,T,B,m,q,Z,Cc,N,L,n,j,A,x,W,R,S = sp.symbols(
        'd1 d2 gamma T B m q Z Cc N L n j A x W R S', nonzero=True)
    # N=n/2, B=gamma*c0*2^(G-3), q=(B-m)/T,
    # d2*Z^2=m*N/T+q. Thus T*Z^2-m*(N-1)/d2=B/d2.
    center = d2*T*Z**2-m*N-(B-m)
    norm = T*Z**2-m*(N-1)/d2-B/d2
    checks = {'center_norm':center-d2*norm,
              'difference_of_squares':(Z-L)*(Z+L)-(Z**2-L**2),
              'square_gap':(L+1)**2-L**2-(2*L+1),
              'W_norm':(n-2*j)**2+n*(n-2)-
                       4*(n-1)*(n/2-j*(n-j)/(n-1)),
              'W_norm_bridge':4*(n-1)*A*T*x*x*W/d1-4*R*S*A*T*x*x*W}
    checks['W_norm_bridge'] = checks['W_norm_bridge'].subs(n,d1*R*S+1)
    for name, expression in checks.items():
        assert sp.cancel(expression) == 0, name
    return list(checks)


def constant_certificates():
    rows = []
    thresholds = (13,11,7,13)
    for (gamma,d1,d2), gap in zip(BRANCHES, thresholds):
        c0 = d1*d1*d2
        A_bound = d2*gamma*gamma*c0
        q_bound = d2*gamma*c0
        assert A_bound <= 9 and q_bound <= 9
        # For G>=3 and v>=1, square constant would imply
        # 64 <= 2^(4v+2) < 4*9+4*3=48.
        assert 4*A_bound+12 <= 48 < 64
        coefficient = d2*gamma*c0*c0
        assert coefficient in (1,27,81,3) and coefficient < 128
        T_min = 5 if gamma == 3 else 7
        m_min = 1 if d2*gamma == 1 else 3
        # 2G-u is odd. Show its value must exceed gap-2.
        ratio = Fraction(128*m_min*T_min*T_min, coefficient)
        assert ratio > 2**(gap-2)
        rows.append({'gamma':gamma,'delta1':d1,'delta2':d2,
                     'A_odd_bound_coefficient':A_bound,
                     'square_constant_bound_coefficient':q_bound,
                     'leading_square_size_coefficient':coefficient,
                     'T_lower':T_min,'m_lower':m_min,
                     'lower_ratio_for_2_power_gap':str(ratio),
                     'necessary_2G_minus_u_at_least':gap})
    return rows


def residue_certificates():
    rows = []
    for gamma,d1,d2 in BRANCHES:
        c0 = d1*d1*d2
        for T in range(1,16,2):
            for Z in range(1,16,2):
                for Cc in range(1,16,2):
                    # Center equation modulo 16 once G>=14, v>=1:
                    # d1*T*Cc^2 = -Z. Its other term has exponent >=14.
                    if (d1*T*Cc*Cc+Z)%16:
                        continue
                    q = d2*Z*Z%16
                    assert q == c0*T*T%16
                    m = -T*q%16
                    assert m == -c0*T**3%16
                    if (d2*gamma*m)%16 in (1,9):
                        assert gamma*T%8 == 7
                    rows.append({'branch':[gamma,d1,d2],'T_mod16':T,
                                 'Z_mod16':Z,'C_mod16':Cc,'q_mod16':q,'m_mod16':m})
    return rows


def synthetic_factor_diagnostics():
    # Every found equation Y^2=Aodd*2^e+b^2 with odd positive inputs
    # must obey the factor bound. This is a diagnostic, not the proof.
    cases = 0
    for Aodd in range(1,100,2):
        for b in range(1,40,2):
            for e in range(3,16):
                value = Aodd*2**e+b*b
                Y = isqrt(value)
                if Y*Y != value:
                    continue
                lower,upper = Y-b,Y+b
                assert lower > 0 and lower*upper == Aodd*2**e
                assert min((lower & -lower).bit_length()-1,
                           (upper & -upper).bit_length()-1) == 1
                assert Aodd*2**e <= 2*Aodd*(2*Aodd+2*b)
                cases += 1
    assert cases > 0
    return {'difference_of_squares_synthetic_cases':cases}


def small_center_residue_examples():
    # Show that the leading-square restrictions do not all contradict the
    # coarse size and 2-adic conditions. This is not an actual solution.
    gamma,d1,d2,T,G,v,m = 1,3,1,7,53,10,1
    u = G+4*v
    B = gamma*d1*d1*d2*2**(G-3)
    # No assertion of q integrality is made here; the example is only a
    # comparison of the necessary inequalities and modulo-16 restrictions.
    assert gamma*T%8 == 7 and gcd(T,gamma*d1*d2) == 1
    assert (m+d1*d1*d2*T**3)%16 == 0
    assert u >= 51 and G >= 14 and 2*G-u >= 7
    assert 2**u*m*T*T < (d2*gamma*(d1*d1*d2)**2)*2**(2*G-7)
    return {'scope':'Only coarse inequalities and residues; not a center-equation solution or counterexample.',
            'parameters':{'gamma':gamma,'delta1':d1,'delta2':d2,'T':T,'G':G,'v':v,'u':u,'m':m}}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    identities = symbolic_checks()
    constants = constant_certificates()
    residues = residue_certificates()
    diagnostics = synthetic_factor_diagnostics()
    result = {'status':'passed','symbolic_identities':identities,
              'branch_certificates':constants,'residue_certificates':residues,
              'diagnostics':diagnostics,'limitation_example':small_center_residue_examples(),
              'conclusions':[
                  'delta2*q=delta2*T*P*W_star is never a square for any even-j counterexample.',
                  'If delta2*gamma*m*2^(G-1) is a square, G is odd, gamma*T=7 mod 8, and 2G-u>=7.',
                  'The sharper branch lower bounds for 2G-u are 13,11,7,13.',
                  'All T=1 or square T branches have nonsquare leading coefficient.'],
              'external_dependencies':'Inherited normalization and G>=14 only; no new elliptic tables or height theorem.',
              'remaining':'Both coefficients nonsquare, and leading-square branches meeting the linear gap bound, remain.'}
    artifact_path('verification_i3_gap_square_obstructions.json').write_text(
        json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','symbolic_identities':len(identities),
                      'branch_certificates':len(constants),'residue_certificates':len(residues),
                      **diagnostics,'leading_square_gap_lower_bounds':[z['necessary_2G_minus_u_at_least'] for z in constants]},indent=2))


if __name__ == '__main__':
    main()
