"""Exact algebraic exploration of invariants of the four cubic orbit values."""
import sympy as S
j, y, x = S.symbols('j y x')
Z = [j*(j-1)*(j-2), j*(j-1)*y, j*y*(y-1), y*(y-1)*(y-2)]
poly = sum(S.binomial(3,h)*Z[h]*x**(3-h) for h in range(4))
disc = S.factor(S.discriminant(poly, x))
print('discriminant',disc)
print('total degree',S.Poly(disc,j,y).total_degree())
H = [Z[0]*Z[2]-Z[1]**2, Z[0]*Z[3]-Z[1]*Z[2], Z[1]*Z[3]-Z[2]**2]
print('quadratic Hessian discriminant',S.factor(H[1]**2-4*H[0]*H[2]))
for n in (16,32,64):
    print('example normalized discriminant',n,S.factor(disc.subs(y,n-j)))
