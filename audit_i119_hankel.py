"""Exact finite checks for the independently proved Hankel/content identities.

The general proofs are in i119_hankel_content_continuation.md. In particular,
these checks do not establish the proposed uniform r=60 content bound.
"""
import json
from functools import reduce
from math import comb, factorial, gcd, prod
from pathlib import Path
from random import Random

import sympy as sy


def falling(x,k):
    return prod(x-s for s in range(k))


def coefficients(r,j,y):
    return [comb(j-r+t,t)*comb(y-t,r-t) for t in range(r+1)]


def common_factor(r,j,y):
    return ((-1)**(r*(r-1)//2)*prod(factorial(k) for k in range(r))
            *prod(((j-s)*(y-s)*(j+y-2*r+2+s))**(r-1-s) for s in range(r-1)))


def determinant_mod(matrix,p):
    a=[list(map(lambda x:int(x)%p,row)) for row in matrix]
    d=1
    for col in range(len(a)):
        pivot=next((i for i in range(col,len(a)) if a[i][col]),None)
        if pivot is None:
            return 0
        if pivot!=col:
            a[pivot],a[col]=a[col],a[pivot]
            d=-d
        entry=a[col][col]
        d=d*entry%p
        inv=pow(entry,-1,p)
        for row in range(col+1,len(a)):
            multiple=a[row][col]*inv%p
            a[row][col]=0
            for k in range(col+1,len(a)):
                a[row][k]=(a[row][k]-multiple*a[col][k])%p
    return d%p


def minors():
    exact=modular=kernel=translations=0
    for r in range(1,7):
        for j,y in ((2*r+3,2*r+3),(2*r+1,3*r+7)):
            Z=[falling(j,2*r-1-h)*falling(y,h) for h in range(2*r)]
            M=sy.Matrix([[Z[u+v] for v in range(r+1)] for u in range(r)])
            G=common_factor(r,j,y)
            S=coefficients(r,j,y)
            for t in range(r+1):
                minor=M.copy()
                minor.col_del(t)
                assert minor.det()==G*factorial(r)*S[t]
                exact+=1
            for k in range(r+1):
                assert sum(comb(t,k)*S[t] for t in range(k,r+1))==comb(j-r+k,k)*comb(j+y-r+1,r-k)
                translations+=1
    r,j,y=60,137,211
    Z=[falling(j,2*r-1-h)*falling(y,h) for h in range(2*r)]
    S=coefficients(r,j,y)
    G=common_factor(r,j,y)
    for u in range(r):
        assert sum((-1)**t*S[t]*Z[u+t] for t in range(r+1))==0
        kernel+=1
    for k in range(r+1):
        assert sum(comb(t,k)*S[t] for t in range(k,r+1))==comb(j-r+k,k)*comb(j+y-r+1,r-k)
        translations+=1
    for p in (1000000007,1000000009):
        assert sy.isprime(p)
        for removed in (0,1,29,30,59,60):
            matrix=[[Z[u+v] for v in range(r+1) if v!=removed] for u in range(r)]
            answer=determinant_mod(matrix,p)
            assert answer==G*factorial(r)*S[removed]%p
            assert answer!=0
            modular+=1
    return dict(small_exact_minors=exact,r60_modular_minors=modular,
                r60_exact_kernel_relations=kernel,exact_translation_coefficients=translations)


def v_p(n,p):
    assert n>0
    v=0
    while n%p==0:
        n//=p
        v+=1
    return v


def local_content():
    rng=Random(699119)
    count=positive=0
    for r in (1,2,3,4,6,60):
        primes=list(map(int,sy.primerange(max(2,2*r-1),max(20,2*r+40))))[:4]
        for p in primes:
            for case in range(160):
                J=rng.randrange(p) if case<80 else rng.randrange(r)
                Y=rng.randrange(p) if case<80 else rng.randrange(r)
                e,f=rng.randrange(1,5),rng.randrange(1,5)
                j=J+p**e*(2*r+1)
                y=Y+p**f*(2*r+3)
                content=reduce(gcd,coefficients(r,j,y))
                ok=J<r and Y<r and J+Y>=r-1
                actual=v_p(content,p)
                assert (actual>0)==ok
                if ok:
                    assert actual==min(v_p(j-J,p),v_p(y-Y,p))
                    assert (j+y-J-Y)%p**actual==0
                    positive+=1
                count+=1
    return dict(local_valuation_cases=count,positive_cases=positive)


def polynomial_checks():
    x=sy.symbols('x')
    count=0
    for r in range(1,10):
        for d in range(r+3):
            polynomials=[sy.Poly(comb(r,t)*falling(x-r+t,t)*falling(x+d-t,r-t),x) for t in range(r+1)]
            common=reduce(sy.gcd,polynomials).monic()
            roots=[s for s in range(r) if s+d<r and 2*s+d>=r-1]
            expected=sy.Poly(prod(x-s for s in roots),x,domain=sy.QQ)
            assert common==expected
            degree=(r-d+1)//2 if d<r else 0
            assert common.degree()==degree
            count+=1
    examples=[]
    for d in (2,3,10,100,1000):
        j=d*d+d+1
        y=d*j+1
        S=coefficients(2,j,y)
        predicted=d*(d+1)*(d*d+d+1)//2
        assert S==[(d*d+1)*predicted,2*d*predicted,predicted]
        assert reduce(gcd,S)==predicted
        examples.append(dict(parameter=d,j=j,y=y,n=j+y,g2=predicted))
    return dict(polynomial_gcd_cases=count,r2_counterfamily=examples)


def main():
    result=dict(status='verified',minors=minors(),local_content=local_content(),
                polynomial_content=polynomial_checks(),
                uniform_r60_n30_bound_proved=False,complete_i119_solution=False,
                inherited_proved_n_cutoff='10^87')
    Path('verification_i119_hankel.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
