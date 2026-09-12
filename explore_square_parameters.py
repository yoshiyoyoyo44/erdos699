"""Test whether the square exclusion could hold without n's special shape.

This is an exploration of necessary conditions, not a proof or a search
covering all triples. Here ell^2=L, lambda=j-L, and
n=2L+lambda+L(L-1)/lambda follows from lambda(n-1)=j(j-1).
"""
from sympy import divisors

found=[]
for ell in range(2,3001):
    L=ell*ell
    for lam in divisors(L*(L-1)):
        if lam>=L:
            break
        j=L+lam
        n=2*L+lam+L*(L-1)//lam
        if n%16 or 2*j>=n:
            continue
        Q=n//2-1
        if Q%3==0 and Q%9!=0:
            Q//=3
        if L*(n//2-j)%Q==0:
            found.append([n,j,L,lam])
            print(found[-1],flush=True)
    if len(found)>=5:
        break
print({'last_ell':ell,'systems':found},flush=True)
