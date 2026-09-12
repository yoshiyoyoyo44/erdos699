"""Exact audits of the merged nonsquare lemmas, not an unbounded proof.

The scan deliberately relaxes the special shape of H, so its examples exist.
All factorizations in this small scan are independently trial-divided.
Run with assertions enabled. No Lean or external service is used.
"""
import argparse
import json
from collections import Counter
from fractions import Fraction
from math import gcd, prod
from pathlib import Path

import sympy as sp


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def exceptional_three(n):
    return 3 if n % 3 == 0 and n % 9 != 0 else 1


def prime_powers(n):
    original, result, p = n, [], 3
    assert n % 2 == 1
    while p*p <= n:
        power = 1
        while n % p == 0:
            n //= p
            power *= p
        if power > 1:
            result.append(power)
        p += 2
    if n > 1:
        result.append(n)
    assert prod(result) == original
    return result


def roots01(powers):
    roots, modulus = [0], 1
    for power in powers:
        inverse = pow(modulus, -1, power)
        roots = [r+modulus*((target-r)*inverse % power)
                 for r in roots for target in (0, 1)]
        modulus *= power
    assert len(set(roots)) == len(roots)
    return roots, modulus


def symbolic_audit():
    H, T, k, d1, d2 = sp.symbols('H T k d1 d2', nonzero=True)
    L = d1*k*(H-k)/(H*T-1)
    q, qp = d1*k-T*L, d1*(H-k)-T*L
    assert sp.factor(q*qp-L*(T*T*L-d1)) == 0
    assert sp.factor(q+qp+2*T*L-d1*H) == 0
    X, Y = 2*T*q+T*T*L, 2*T*qp+T*T*L
    assert sp.factor(X-d1*(k*T)*(H*T+k*T-2)/(H*T-1)) == 0
    assert sp.factor(Y-d1*((H-k)*T)*(2*H*T-k*T-2)/(H*T-1)) == 0
    assert sp.factor(X*Y-T*T*L*(T*T*L+2*d1*(H*T-2))) == 0
    A, B, C, a, b, g, h = sp.symbols('A B C a b g h')
    linear = T*(B*a*g+C*b*h)+2*A*a*b-2*d1*d2*B*C
    # The integer product identity follows from the earlier linear equation.
    residual = ((2*A*a+T*C*h)*(2*A*b+T*B*g)
                - B*C*(T*T*g*h+4*d1*d2*A))
    assert sp.expand(residual-2*A*linear) == 0
    eta, zeta = (2*A*a+T*C*h)/B, (2*A*b+T*B*g)/C
    assert sp.expand(C*(a*zeta+T*b*h-2*d1*d2*B)-linear) == 0
    assert sp.expand(B*(b*eta+T*a*g-2*d1*d2*C)-linear) == 0
    # Equivalent formula for the product of square-lift quotients.
    E, F = T*g*(2*A*a+T*C*h)/B, T*h*(2*A*b+T*B*g)/C
    assert sp.factor(E*F-T*T*g*h*(T*T*g*h+4*d1*d2*A)
                     -2*A*T*T*g*h*linear/(B*C)) == 0
    # Squaring the whole integer quotient gives the exact size inequality.
    x, p, Q = sp.symbols('x p Q')
    assert sp.expand(A*(T*T*B*C*x-A*A*p-d1)
                     -(T*T*A*B*C*x-A**3*p-d1*A)) == 0
    return 10


def audit_row(n, j, T=1):
    assert n % 16 == 0 and 4 <= j < n//2 and n % T == j % T == 0
    assert T % 2 == 1
    H, k = n//T, j//T
    d1, d2 = exceptional_three(n-1), exceptional_three(n//2-1)
    Q1, Q2 = (n-1)//d1, (n//2-1)//d2
    assert gcd(Q1, Q2) == gcd(T, Q1*Q2) == 1
    assert j*(j-1) % Q1 == j*(j-1)*(j-2) % Q2 == 0
    R = S = A = B = C = 1
    for P in prime_powers(Q1):
        residue = j % P
        assert residue in (0, 1)
        if residue == 1:
            R *= P
        else:
            S *= P
    for P in prime_powers(Q2):
        residue = j % P
        assert residue in (0, 1, 2)
        if residue == 1:
            A *= P
        elif residue == 0:
            B *= P
        else:
            C *= P
    assert R*S == Q1 and A*B*C == Q2
    assert k % (S*B) == (H-k) % (R*C) == 0
    assert (j-1) % (R*A) == (n-j-1) % (S*A) == 0
    g, h = k//(S*B), (H-k)//(R*C)
    a, b = (j-1)//(R*A), (n-j-1)//(S*A)
    assert min(a, b, g, h) > 0
    L = B*C*g*h
    q, qp = A*B*a*g, A*C*b*h
    assert L*Q1 == k*(H-k)
    assert q == d1*k-T*L and qp == d1*(H-k)-T*L
    assert T*T*L-A*A*a*b == d1
    assert d1*S == A*a+T*C*h and d1*R == A*b+T*B*g
    assert T*(B*a*g+C*b*h)+2*A*a*b == 2*d1*d2*B*C
    # These identities justify cancellation of R or S, not of g or h.
    assert R*(2*A*a+T*C*h) == n+j-2
    assert S*(2*A*b+T*B*g) == 2*n-j-2
    assert gcd(R, B) == gcd(S, C) == 1
    assert (2*A*a+T*C*h) % B == (2*A*b+T*B*g) % C == 0
    eta, zeta = (2*A*a+T*C*h)//B, (2*A*b+T*B*g)//C
    assert eta*zeta == T*T*g*h+4*d1*d2*A
    assert a*zeta+T*b*h == 2*d1*d2*B
    assert b*eta+T*a*g == 2*d1*d2*C
    assert (a*zeta) % 2 == (b*h) % 2 == (b*eta) % 2 == (a*g) % 2 == 0
    assert d1*d2*B >= T+1 and d1*d2*C >= T+1
    E, F = T*g*eta, T*h*zeta
    assert B*B*E == 2*T*q+T*T*L
    assert C*C*F == 2*T*qp+T*T*L
    assert E*F == T*T*g*h*(T*T*g*h+4*d1*d2*A)
    assert gcd(A, T*T*g*h) == 1
    assert (4*d1*d2) % gcd(T*T*g*h, eta*zeta) == 0
    if d1 == d2 == 1:
        assert gcd(g*h, eta*zeta) == (4 if k % 2 == 0 else 1)
    # No special shape of H is used for this size inequality.
    assert B*C > d1
    W = T*T*L
    assert W <= d1*n//4
    assert B*C*(2*T*T*g*h-d1*d2*A) <= d1
    assert d1*d2*A > 2*T*T*g*h
    assert A > 1
    if T >= 5 or d1*d2 == 1:
        assert B > 1 and C > 1
    assert (n-2)*d1**3*d2**2 > 16*a*b*T**4*(g*h)**2
    v = v2(k)
    assert v2(g) == v2(h) == v
    assert (a*b-d1*(k*k-1)) % 8 == 0
    if v:
        s = (3 if d1 == 1 else 1) if v == 1 else (7 if d1 == 1 else 5)
        assert a*b >= s
        assert n*d1**3*d2**2 > 16*s*T**4*2**(4*v)
    else:
        w = max(v2(j-1), v2(n-j-1))
        assert v2(a*b) == w+1
        assert n*d1**3*d2**2 > 32*T**4*2**w*(g*h)**2
    return dict(n=n, j=j, T=T, delta1=d1, delta2=d2,
                A=A, B=B, C=C, R=R, S=S, a=a, b=b, g=g, h=h,
                eta=eta, zeta=zeta, gcd_B_g=gcd(B,g), gcd_C_h=gcd(C,h))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-n', type=int, default=1000000)
    parser.add_argument('--output', default='verification_i3_nonsquare_lifts.json')
    args = parser.parse_args()
    identities = symbolic_audit()
    hits, examples, branches, noncoprime = 0, [], Counter(), []
    first_candidates = 0
    for n in range(16, args.max_n+1, 16):
        d1, d2 = exceptional_three(n-1), exceptional_three(n//2-1)
        Q1, Q2 = (n-1)//d1, (n//2-1)//d2
        roots, modulus = roots01(prime_powers(Q1))
        assert modulus == Q1
        for root in roots:
            first = root+max(0, (4-root+Q1-1)//Q1)*Q1
            for j in range(first, n//2, Q1):
                first_candidates += 1
                if j*(j-1)*(j-2) % Q2:
                    continue
                common = gcd(n, j)
                odd_common = common >> v2(common)
                for T in sp.divisors(odd_common):
                    row = audit_row(n, j, int(T))
                    hits += 1
                    branches[str((d1, d2, 'T=1' if T == 1 else 'T>1'))] += 1
                    if len(examples) < 12:
                        examples.append(row)
                    if (row['gcd_B_g'] > 1 or row['gcd_C_h'] > 1) and len(noncoprime) < 12:
                        noncoprime.append(row)
    special = audit_row(76672, 26775)
    assert (special['gcd_B_g'], special['eta'], special['zeta']) == (5, 1, 49)
    constants = []
    for gamma, d1, d2 in [(1,1,1),(1,1,3),(1,3,1),(3,1,1)]:
        constants.append(dict(gamma=gamma, delta1=d1, delta2=d2,
            v1=str(Fraction(gamma**4*d1**3*d2**2,16*(3 if d1 == 1 else 1))),
            v_at_least_2=str(Fraction(gamma**4*d1**3*d2**2,16*(7 if d1 == 1 else 5))),
            odd_j_w_weighted=str(Fraction(gamma**4*d1**3*d2**2,32))))
    report = dict(status='all assertions passed; finite audit, not a complete proof',
                  symbolic_identities=identities, max_n=args.max_n,
                  n_step=16, first_candidates=first_candidates, normalized_rows=hits,
                  branch_counts=dict(branches), examples=examples,
                  examples_with_repeated_block_primes=noncoprime,
                  regression_example=special, constants=constants, lean_calls=0)
    Path(args.output).write_text(json.dumps(report, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({k:v for k,v in report.items() if k not in
                     ('examples','examples_with_repeated_block_primes')}, indent=2))


if __name__ == '__main__':
    main()
