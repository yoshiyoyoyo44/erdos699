"""Independent symbolic audit of the supplied progress note."""
import sympy as S
from fractions import Fraction
from math import comb, factorial, gcd, lcm, prod

j, z = S.symbols('j z', positive=True)
y = [j*(j-1)*(j-2)/2, j*(j-1)*z/2,
     j*z*(z-1)/2, z*(z-1)*(z-2)/2]
for label, value in [('minor02', y[0]*y[2]-y[1]**2),
                     ('minor03', y[0]*y[3]-y[1]*y[2]),
                     ('minor13', y[1]*y[3]-y[2]**2)]:
    print(label, S.factor(value))

B, R, k = S.symbols('B R k', positive=True)
L = k*(2*B-k)/(2*B*R-1)
H = L*(B-k)/(B*R-1)
q = k-R*L
y = L-R*H
checks = {
    '13.9a': 2*B*q-(k*k-L),
    '13.9b': B*y-(k*L-H),
    '13.10': k*y-2*q*L-L*y/(2*B-k),
    '13.14': B*k*(R*k-1)*(R*k-2)/((2*B*R-1)*(B*R-1))-(k*q-y),
}
for name, value in checks.items():
    residual = S.factor(value)
    print(name, residual)
    assert residual == 0

# Independently check the orbit divisibility and the repaired simultaneous
# minor bound on every admissible (n,3,j) through n=300.
minor_checks = 0
for n in range(8, 301):
    for j in range(4, n//2+1):
        z = n-j
        A, B = comb(n, 3), comb(n, j)
        D = gcd(A, B)
        a = A//D
        Y = [3*comb(j, 3), comb(j, 2)*z,
             j*comb(z, 2), 3*comb(z, 3)]
        assert all(v % a == 0 for v in Y)
        minors = (Y[0]*Y[2]-Y[1]**2,
                  Y[0]*Y[3]-Y[1]*Y[2],
                  Y[1]*Y[3]-Y[2]**2)
        assert all(v % (a*a) == 0 for v in minors)
        quartic = minors[1]**2 - 4*minors[0]*minors[2]
        assert 4*quartic == -j*j*z*z*(j-1)*(z-1)*(n-2)**2*(n-1)
        assert quartic < 0 and quartic % (a**4) == 0
        assert 324*D**4*j*j*z*z*(j-1)*(z-1) >= n**4*(n-1)**3*(n-2)**2
        assert 81*n*n*D**4 > 16*(n-1)**3*(n-2)**2
        g = gcd(j*(j-1), (j-1)*(z-1), z*(z-1))
        assert g == gcd(j, z-1)*gcd(j-1, z)*gcd(j-1, z-1)
        if n % 2 == 0 and 2*j < n:
            eta = 1 if j % 2 else 2
            gp = gcd(j*(j-1), 2*(j-1)*(z-1), z*(z-1))
            assert gp == eta*g
            assert gcd(*minors) == j*z*(n-2)*eta*g//4
            assert 9*eta*j*z*(n-2*j)*D*D >= n*n*(n-1)*(n-2)
            minor_checks += 1
print('repaired even-n minor bound checks:', minor_checks)

# Exact rational constants in the new M^3<2*2^u argument.
F = Fraction
constants = [F(1,48)*F(25,24)**2*F(80,79),
             F(9,48)*F(25,24)**2*F(80,79),
             F(27,16)*F(49,46)**2*F(112,111),
             F(81,48)*F(25,24)**2*F(80,79)]
assert all(c < 2 for c in constants)
print('four exact branch constants:', [str(c) for c in constants])

# The two small rows needed when T=5, epsilon=0, and u<6.
for n in (80, 160):
    assert all(any(p >= 3 for p in S.factorint(gcd(comb(n,3), comb(n,j))))
               for j in range(4, n//2+1))
print('n=80,160: all i=3 pairs pass')
