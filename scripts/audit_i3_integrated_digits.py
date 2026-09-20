"""Audit the 2026-09-13 integration and new center-cofactor identities.

Run with assertions enabled. SymPy checks polynomial/rational identities;
all finite digit checks use exact integers. This is a finite audit, not a
proof of the unbounded conjecture or of Siegel's theorem. No Magma is used.
"""
from repo_paths import artifact_path
import json
from fractions import Fraction
from math import comb, gcd, prod
from pathlib import Path

import sympy as sp


def valuation(n, p):
    assert n > 0
    answer = 0
    while n % p == 0:
        n //= p
        answer += 1
    return answer


def factorial_valuation(n, p):
    answer = 0
    while n:
        n //= p
        answer += n
    return answer


def binomial_valuation(n, j, p):
    assert 0 <= j <= n
    return (factorial_valuation(n, p) - factorial_valuation(j, p)
            - factorial_valuation(n-j, p))


def digits(n, p):
    result = []
    while n:
        result.append(n % p)
        n //= p
    return result or [0]


def digitwise_allowed(n, j, p):
    while n or j:
        if j % p > n % p:
            return False
        n //= p
        j //= p
    return True


def signed_set(n, p):
    values, place = {0}, 1
    for digit in digits(n, p):
        values = {v + d*place for v in values
                  for d in range(-digit, digit+1, 2)}
        place *= p
    return values


def signed_gap(n, p):
    assert n > 0
    odd_positions = [i for i, d in enumerate(digits(n, p)) if d % 2]
    if odd_positions:
        power = p**max(odd_positions)
        return power - n % power
    # This also covers p | n, beyond the complete-prime-power setting.
    return 2*p**valuation(n, p)


def symbolic_audit():
    checked = []

    def check(name, expression):
        assert sp.cancel(sp.expand(expression)) == 0, name
        checked.append(name)

    A, B, C, a, b, g, h, s, T, W, d1, d2 = sp.symbols(
        'A B C a b g h s T W d1 d2', nonzero=True)
    determinant = B*C*s-A*A*a*b-d1
    check('compressed product', s*a*b/(B*C)-s/A*(s/A-d1/(A*B*C))
          + s*determinant/(A*A*B*C))
    D = sp.symbols('D')
    check('unitary odd-part expansion',
          a*b*(T*W-1)**2+d1*D**2
          -(a*b+d1*D**2-2*T*W*a*b+T*T*W*W*a*b))

    m = sp.symbols('m')
    af, bf, cf = 18*m+11, 144*m+85, 72*m+41
    aa, bb, gg, hh = sp.Integer(2), 128*m+72, 8*m+5, sp.Integer(1)
    sf, rf = 108*m+63, 3456*m*m+4104*m+1217
    nf, jf = 2*af*bf*cf+2, sf*bf*gg
    for name, expression in [
        ('family RS', rf*sf-(nf-1)),
        ('family j-1', jf-1-rf*af*aa),
        ('family n-j', nf-jf-rf*cf*hh),
        ('family n-j-1', nf-jf-1-sf*af*bb),
        ('family determinant', bf*cf*gg*hh-af**2*aa*bb-1),
        ('family center', nf/2-jf-af*(3456*m*m+3816*m+1051)),
        ('family linear S', sf-af*aa-cf*hh),
        ('family linear R', rf-af*bb-bf*gg),
        ('family cubic', nf/4-(93312*m**3+165240*m*m+97497*m+19168)),
    ]:
        check(name, expression)
    polynomial = sp.Poly(nf/4, m)
    assert [int(x) % 2 for x in polynomial.all_coeffs()] == [0, 0, 1, 0]
    assert all(int(x) % 9 == 0 for x in sp.Poly(nf-1, m).all_coeffs())

    Q, c, r, z, w, Z = sp.symbols('Q c r z w Z', nonzero=True)
    Q1 = (2*d2*Q+1)/d1
    r_of_c = (4*c*c-1)/Q1
    tau = c*(c*c-1)/Q
    check('center elimination',
          2*Q*(2*d1*tau-d2*c*r_of_c)-c*(r_of_c-3*d1))
    r0 = d1*(4*c*c-1)
    check('center residue compression',
          (r+d1)*(r-3*d1)-16*d1*d1*c*c*(c*c-1)
          -(r-r0)*(r+r0-2*d1))
    check('center square completion',
          (r+d1)*(r-3*d1)-((r-d1)**2-4*d1*d1))
    ec, fc = d1*d2*A-2*s, d1*d2*B*C-2*A*a*b
    check('central factors', A*fc-B*C*ec-2*d1-2*determinant)
    r_from_blocks = 3*d1+2*B*C*ec
    check('central quotient from blocks',
          r_from_blocks-(d1*(2*d2*A*B*C+3)-4*B*C*s))
    check('central cofactor product',
          (r_from_blocks+d1)*(r_from_blocks-3*d1)/(4*A*B*C)
          -ec*fc+2*ec*determinant/A)
    check('center reconstruction',
          (d1+2*z)*Q1+1-(2*d2*Q+2+2*Q1*z))
    # Q = (TW-1)/d2, not (TW-1)/(2*d2).
    check('center unitary identity',
          w-d1*d1*d2-T*(w*W-d2*T*Z*Z)
          -d2*(T*T*Z*Z-d1*d1-w*(T*W-1)/d2))
    rho, j = sp.symbols('rho j')
    check('rho residue compression',
          4*rho*(rho-d1)-d1*d1*j*(j-1)*(j-2)*(j+1)
          -(2*rho-d1*j*(j-1))*(2*rho+d1*j*(j-1)-2*d1))

    X = sp.symbols('X')
    check('degenerate center factorization',
          2*X*X+2*(2*X*X-1)*X-2*X*(2*X-1)*(X+1))
    L = sp.symbols('L')
    check('w=5 size contradiction', (L-1)**2-(10*L+1)-L*(L-12))
    alpha, beta, t, Y = sp.symbols('alpha beta t Y')
    check('Mordell map',
          (alpha*Y)**2-(alpha*t)**3-alpha*alpha*beta
          -alpha*alpha*(Y*Y-alpha*t**3-beta))
    check('fixed-w curve coefficients',
          d2*d2*(d1*d1+w*(T*W-1)/d2)
          -(w*T*d2*W+d2*(d1*d1*d2-w)))
    t0 = sp.symbols('t0')  # t0 = n/2, divisible by 2^(u-1).
    z_of_c = d1*(2*c*c-t0)/(2*t0-1)
    w_of_c = d2*(z_of_c*z_of_c-d1*d1)/(t0-1)
    denominator = (t0-1)*(2*t0-1)**2  # odd in the application
    numerator = sp.cancel((w_of_c-d1*d1*d2*(1-4*c**4))*denominator)
    assert sp.rem(numerator, t0, t0) == 0
    checked.append('central fourth-power congruence with odd denominator')
    return checked


def audit_digits():
    primes = (3, 5, 7, 11, 13)
    comb_checks = lift_checks = signed_checks = gap_checks = 0
    for p in primes:
        for n in range(181):
            for j in range(n+1):
                assert valuation(comb(n, j), p) == binomial_valuation(n, j, p)
                comb_checks += 1
        for e in range(1, 4):
            q = p**e
            for N in range(33):
                for r in range(p):
                    for s in range(r+1):
                        n = q*N+r
                        for J in range(N+1):
                            j = q*J+s
                            assert binomial_valuation(n, j, p) == binomial_valuation(N, J, p)
                            assert n-2*j-r+2*s == q*(N-2*J)
                            lift_checks += 1
        for N in range(1, 301):
            values = signed_set(N, p)
            assert len(values) == prod(d+1 for d in digits(N, p))
            assert (0 in values) == all(d % 2 == 0 for d in digits(N, p))
            assert min(v for v in values if v > 0) == signed_gap(N, p)
            gap_checks += 1
            for J in range(N+1):
                allowed = N-2*J in values
                assert allowed == digitwise_allowed(N, J, p)
                assert allowed == (binomial_valuation(N, J, p) == 0)
                signed_checks += 1
    n, j = 76672, 26775
    assert ((n-2)//17, j//17) == (4510, 1575)
    assert (4510 % 17, 1575 % 17) == (5, 11)
    assert ((n-2)//41, (j-2)//41) == (1870, 653)
    assert signed_gap(1870, 41) == 1492 > 1870-2*653 == 564
    witnesses = []
    for p in (17, 41, 599):
        v3, vj = binomial_valuation(n, 3, p), binomial_valuation(n, j, p)
        assert v3 > 0 and vj > 0
        witnesses.append(dict(p=p, valuation_choose_3=v3, valuation_choose_j=vj))
    return dict(primes=primes, exact_binomial_checks=comb_checks,
                quotient_lift_checks=lift_checks, signed_membership_checks=signed_checks,
                signed_gap_checks=gap_checks, regression_witnesses=witnesses)


def family_values(m):
    A, B, C = 18*m+11, 144*m+85, 72*m+41
    a, b, g, h = 2, 128*m+72, 8*m+5, 1
    S, R = 108*m+63, 3456*m*m+4104*m+1217
    n, j = 2*A*B*C+2, S*B*g
    return A, B, C, a, b, g, h, S, R, n, j


def audit_family():
    rows, example = 0, None
    for m in range(513):
        A, B, C, a, b, g, h, S, R, n, j = family_values(m)
        Q, Q1 = A*B*C, n-1
        assert n % 9 == 1 and n % 4 == 0
        assert n & (n-1)  # No sampled member is a power of two.
        assert min(A, B, C) == A and gcd(A, B) == gcd(B, C) == gcd(A, C) == 1
        assert R*S == n-1 and gcd(R, S) == 1
        assert j-1 == R*A*a and n-j == R*C*h and n-j-1 == S*A*b
        assert B*C*g*h-A*A*a*b == 1
        assert 4 <= j < n//2 and gcd(n, j) == 1
        s, rB, rC = g*h, b*h//2, a*g//2
        assert gcd(s, A) == gcd(rB, B) == gcd(rC, C) == gcd(a*b, B*C) == 1
        x, y, z = Fraction(s, A), Fraction(rB, B), Fraction(rC, C)
        eps = Fraction(1, Q)
        assert x+y+z == 1+eps and 4*y*z == x*(x-eps)
        c = n//2-j
        assert (4*c*c-1) % Q1 == c*(c*c-1) % Q == 0
        r, tau = (4*c*c-1)//Q1, c*(c*c-1)//Q
        assert r > 3 and 2*Q*(2*tau-c*r) == c*(r-3)
        assert (r+1)*(r-3) % (4*Q) == 0
        w, z0 = (r+1)*(r-3)//(4*Q), (r-1)//2
        ec, fc = A-2*s, B*C-2*A*a*b
        assert ec > 0 and fc > 0 and w == ec*fc and gcd(ec, fc) == 1
        assert A*fc-B*C*ec == 2
        assert w > 0 and w % 2 == 1 and z0 % 2 == 0
        assert z0*z0 == 1+w*Q and 4*c*c == n+2*Q1*z0
        assert (w-(1-4*c**4)) % (n//2) == 0
        assert 4*c**4 > w*Q*Q1*Q1 and c**3 > Q*Q
        rho = A*B*rC
        assert j*(j-1) == 2*Q1*rho
        assert rho*(rho-1) % (2*Q) == 0
        assert j**4 > 8*Q*Q1*Q1
        rows += 1
        if m == 0:
            example = dict(m=m, n=n, j=j, Q=Q, c=c, rho=rho, r=r, z0=z0,
                           w=w, ec=ec, fc=fc)
    # These are relaxed T=1 examples, never positive normalized candidates.
    root, records = 0, []
    P = lambda m: 93312*m**3+165240*m*m+97497*m+19168
    for exponent in range(1, 129):
        modulus = 2**exponent
        candidates = [root, root+modulus//2]
        roots = [r for r in candidates if P(r) % modulus == 0]
        assert len(roots) == 1
        root = roots[0]
        large_m = root+modulus
        assert P(large_m) % modulus == 0
        if exponent in (1, 2, 8, 16, 32, 64, 128):
            records.append(dict(exponent=exponent, least_root=root,
                                sample_m=large_m, valuation_n=valuation(4*P(large_m), 2)))
    return dict(relaxed_rows=rows, normalized_positive_rows=0,
                regression=example, hensel_levels=128, hensel_samples=records,
                scope='The family audit does not test any genuine T>1 positive candidate.')


def audit_center_constants():
    squares = {(2*x)**2 % 128 for x in range(64)}
    result = []
    for d1, d2, threshold, exceptional in [(1, 1, 29, [1]),
                                         (1, 3, 23, [3]),
                                         (3, 1, 37, [5, 9])]:
        Qmod = -pow(d2, -1, 128) % 128
        survivors = [w for w in range(1, threshold, 2)
                     if (d1*d1+w*Qmod) % 128 in squares]
        assert survivors == exceptional
        assert (d1*d1+threshold*Qmod) % 128 in squares
        result.append(dict(delta1=d1, delta2=d2, Q_mod_128=Qmod,
                           excluded_below=threshold, exceptions_requiring_proof=survivors))
    # For w=d1^2*d2, the factor 2X-1 must be an odd square or three
    # times one, contradicting 2X-1 = 7 (mod 8) when 4 | X.
    assert {x*x % 8 for x in (1, 3, 5, 7)} == {1}
    assert {3*x*x % 8 for x in (1, 3, 5, 7)} == {3}
    assert all((2*X-1) % 8 == 7 for X in range(4, 101, 4))
    # An even shorter exclusion of w=5 uses d1=3 => n=1 (mod 3), Q=1 (mod 3).
    assert (3*3+5*1) % 3 not in {x*x % 3 for x in range(3)}
    # For w=5, d1=3, d2=1, the odd divisor T of w-9 is necessarily 1.
    assert [t for t in range(1, 5, 2) if 4 % t == 0] == [1]
    assert 16*(16-12) > 0  # L(L-12)>0 for L=2^(u-4)>=16.
    return result


def audit_fourth_power_constants():
    result = []
    for d1, d2, odd_min, even_min in ((1, 1, 61, 961),
                                     (1, 3, 55, 835),
                                     (3, 1, 37, 457)):
        c0 = d1*d1*d2
        odd_residues = {c0*(1-4*c**4) % 64 for c in range(1, 64, 2)}
        even_residues = {c0*(1-4*c**4) % 1024 for c in range(0, 1024, 2)}
        assert odd_residues == {odd_min}
        assert even_residues == {c0, even_min}
        assert c0 < odd_min < even_min < c0+1024
        # The value c0 itself is excluded by the proof's degenerate-factor lemma.
        assert all((r-c0) % 4 == 0 for r in odd_residues | even_residues)
        assert all((r-c0) % 64 == 0 for r in even_residues)
        result.append(dict(delta1=d1, delta2=d2, c0=c0,
                           odd_j_min_w=odd_min, even_j_min_w=even_min,
                           odd_c_residues_mod_64=sorted(odd_residues),
                           even_c_residues_mod_1024=sorted(even_residues)))
    return result


def audit_unitary_and_curves():
    # Congruence-level checks deliberately include non-powers-of-two T.
    # The variables below test the algebra; they are not actual n,j examples.
    checks = 0
    for T in (1, 5, 7, 9, 11, 13, 25, 35, 49, 55):
        for d1, d2 in ((1, 1), (1, 3), (3, 1)):
            if gcd(T, d1*d2) != 1:
                continue
            for gamma in (1, 3):
                if gamma == 3 and (d1, d2) != (1, 1):
                    continue
                if gcd(T, gamma) != 1:
                    continue
                W = gamma*2**48
                if (T*W-1) % d2:
                    continue
                Q = (T*W-1)//d2
                # Force z0=T*Z and the square relation only modulo T^2.
                w = -d1*d1*pow(Q, -1, T*T) % (T*T) if T > 1 else 0
                w += 2*T*T
                assert (w-d1*d1*d2) % T == 0
                assert gcd(T, (w-d1*d1*d2)//T) == 1
                # This catches a spurious factor 2 in the central congruence.
                assert (w*Q+d1*d1) % (T*T) == 0
                checks += 1
    maps = 0
    for alpha in (1, 3, 5, 29, 37, 135):
        for beta in (-1, -4, -28, -84):
            for t in (1, 2, 16, 65536):
                # An identity even when the curve RHS is not a square.
                rhs = alpha*t**3+beta
                assert alpha*alpha*rhs == (alpha*t)**3+alpha*alpha*beta
                assert -432*(alpha*alpha*beta)**2 != 0
                maps += 1
    return dict(unitary_congruence_checks=checks, Mordell_map_checks=maps,
                integer_point_completeness='Not computed; finiteness uses Siegel in the proof.')


def main():
    assert __debug__, 'Run without -O: this audit uses assertions.'
    report = dict(status='all assertions passed; finite audit, not a solution',
                  symbolic_identities=symbolic_audit(), digits=audit_digits(),
                  obstruction_family=audit_family(),
                  preliminary_square_constants=audit_center_constants(),
                  stronger_fourth_power_constants=audit_fourth_power_constants(),
                  unitary_and_curves=audit_unitary_and_curves(),
                  magma_calls=0, lean_calls=0)
    out = artifact_path('verification_i3_integrated_digits.json')
    out.write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(report, indent=2))


if __name__ == '__main__':
    main()
