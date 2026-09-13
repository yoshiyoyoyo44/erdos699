"""Exploratory modular and factorization screen of the new fixed-gap equations."""
from fractions import Fraction
from math import gcd,isqrt
from collections import Counter

BRANCHES=[(1,1,1,Fraction(1,112)),(1,1,3,Fraction(9,112)),
          (1,3,1,Fraction(27,80)),(3,1,1,Fraction(3,112))]
PERIOD=360
MODULI=[5,7,13,17,19,31,37,73,97,109,181]


def rows(gap):
    for gamma,d1,d2,bound in BRANCHES:
        B=gamma*d1*d1*d2*2**(gap-3)
        for T in range(1,B,2):
            if T**3>=bound*2**gap or gcd(T,gamma*d1*d2)>1:
                continue
            if gamma==1 and T%3==0 and T%9!=0:
                continue
            for m in range(1,B,2):
                if (B-m)%T or gcd(m,T)>1:
                    continue
                q=(B-m)//T
                alpha=m*gamma*2**(gap-1)
                # Z0 odd, and v >= 10 in these layers.
                if (q-d2)%8:
                    continue
                yield dict(gap=gap,gamma=gamma,d1=d1,d2=d2,T=T,m=m,q=q,alpha=alpha)


def admissible_branch(row,v):
    g,d1,d2,T=(row[k] for k in ('gamma','d1','d2','T'))
    u=4*v+row['gap']
    n9=g*T*pow(2,u,9)%9
    half9=g*T*pow(2,u-1,9)%9
    if (3 if n9 in (4,7) else 1)!=d1:
        return False
    if (3 if half9 in (4,7) else 1)!=d2:
        return False
    if d1==3:
        w=(d1*d1*d2+T*pow(2,4*v+2,9)*row['m'])%9
        if w not in (0,1,4,7):
            return False
    return True


def local(row,v,l):
    g,d1,d2,T,alpha,q=(row[k] for k in ('gamma','d1','d2','T','alpha','q'))
    p4=pow(4,v,l);p16=p4*p4%l
    n=g*T*pow(2,row['gap'],l)*p16%l
    rhs=(alpha*p16+q)%l
    squares={z*z%l for z in range(l)}
    cterms={d1*T*s%l for s in squares}
    zvalues=[z for z in range(l) if d2*z*z%l==rhs]
    return any((d1*g*pow(2,row['gap']-2,l)*p4+(n-1)*z)%l in cterms for z in zvalues)


def factor_bound(row):
    A=row['d2']*row['alpha'];B=row['d2']*row['q']
    b=isqrt(B)
    if b*b!=B:
        return None
    odd=A
    while odd%2==0:odd//=2
    two_b=2*b
    twopart=two_b&-two_b
    small=twopart*odd
    return small*(small+two_b),A


if __name__=='__main__':
    for gap in range(4,10):
        count=Counter();remaining=[]
        for row in rows(gap):
            count['initial']+=1
            fb=factor_bound(row)
            vmin=max(2,(49-gap+3)//4)
            if fb and fb[1]*16**vmin>fb[0]:
                count['factor']+=1;continue
            possible=[v for v in range(12,12+PERIOD) if admissible_branch(row,v)]
            for l in MODULI:
                assert pow(4,PERIOD,l)==1
                possible=[v for v in possible if local(row,v,l)]
                if not possible:break
            if not possible:
                count['local']+=1
            else:
                remaining.append((row,[v%PERIOD for v in possible]))
        print('GAP',gap,dict(count),'remaining',remaining,flush=True)
