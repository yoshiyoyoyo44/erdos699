"""Exact checks for the discriminant continuation; no Lean invocation.

The general proof is in discriminant_continuation.md. These checks audit
the formula and its application; finite checks do not prove the conjecture.
"""
from repo_paths import artifact_path
from fractions import Fraction
from math import comb, gcd, prod, isqrt
import json
import sympy as S

j, y, z = S.symbols('j y z')

def falling(x, k):
    return prod(x-t for t in range(k))

def orbit_poly(i):
    return sum(falling(j, i-h)*falling(y, h)
               / (S.factorial(i-h)*S.factorial(h))*z**h
               for h in range(i+1))

def expected_discriminant(i, j, y):
    denominator = prod(r**(r-2) for r in range(2, i+1))
    denominator *= prod(S.factorial(r) for r in range(1, i))**2
    return (prod(((j-t)*(y-t))**(i-1-t) for t in range(i-1))
            * prod((j+y-s)**s for s in range(1, i)) / denominator)

symbolic_degrees = []
for i in range(2, 6):
    F = orbit_poly(i)
    ode = (z*(1-z)*S.diff(F,z,2)
           + (j-i+1+(i+y-1)*z)*S.diff(F,z) - i*y*F)
    assert S.expand(ode) == 0
    assert S.expand(S.diff(F,z) - y*orbit_poly(i-1).subs(y,y-1)) == 0
    actual = S.discriminant(F,z)
    assert S.factor(actual-expected_discriminant(i,j,y)) == 0
    symbolic_degrees.append(i)
    print('symbolic discriminant and differential identities:', i, flush=True)

numeric_discriminants = 0
for i in range(2, 9):
    for n in range(2*i+2, 2*i+12):
        for k in {i+1, n//2}:
            F = sum(comb(k,i-h)*comb(n-k,h)*z**h for h in range(i+1))
            assert S.discriminant(F,z) == expected_discriminant(i,k,n-k)
            numeric_discriminants += 1

gcd_checks = 0
odd_part_checks = 0
for n in range(8, 201):
    for k in range(4, n//2+1):
        A = comb(n,3)
        B = comb(n,k)
        D = gcd(A,B)
        a = A//D
        d = expected_discriminant(3,k,n-k)
        assert d.is_Integer and d > 0 and d % a**4 == 0
        assert 108*D**4*k*k*(n-k)**2*(k-1)*(n-k-1) >= n**4*(n-1)**3*(n-2)**2
        assert 27*n*n*D**4 > 16*(n-1)**3*(n-2)**2
        gcd_checks += 1
        if n % 4 == 0:
            assert d % 8 == 0
            odd_a = a // (a & -a)
            odd_d = int(d) // (int(d) & -int(d))
            assert odd_d % odd_a**4 == 0
            odd_part_checks += 1

constant = Fraction(27,128)*Fraction(64**5,63**3*62**2)
assert constant == Fraction(2097152,8899821)
assert constant < Fraction(1,4)
square_branch_cases = []
for u in range(3,13):
    n = 1 << u
    for k in range(4,n//2):
        numerator = k*(n-k)
        if numerator % (n-1):
            continue
        L = numerator//(n-1)
        ell = isqrt(L)
        if ell*ell != L:
            continue
        assert u % 2 == 0 and L == n//4 and k+ell == n//2
        Q = n//2-1
        assert Q % 3 and gcd(Q,ell*(n-1)) == 1
        assert k*(n//2-k)*(n-k) % Q != 0
        square_branch_cases.append([n,k,L])
result = {
    'symbolic_degrees': symbolic_degrees,
    'numeric_discriminants': numeric_discriminants,
    'gcd_checks': gcd_checks,
    'odd_part_checks': odd_part_checks,
    'uniform_M_cubic_constant': str(constant),
    'square_branch_cases': square_branch_cases,
    'complete_proof_of_erdos699': False,
    'new_lean_verification': False,
}
with artifact_path('verification_discriminant.json').open('w', encoding='utf-8') as f:
    json.dump(result,f,indent=2)
    f.write('\n')
print(json.dumps(result,indent=2),flush=True)
