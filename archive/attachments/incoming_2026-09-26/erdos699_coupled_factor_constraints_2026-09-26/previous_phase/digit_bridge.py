#!/usr/bin/env python3
"""Exact adaptive bounds for the two i=3 polynomial divisibilities.

Coefficient lists are in ascending order. No external libraries are needed.
"""
from math import gcd, prod

def trim(a):
    a=list(a)
    while len(a)>1 and a[-1]==0:a.pop()
    return a or [0]

def degree(a):
    a=trim(a)
    return -1 if a==[0] else len(a)-1

def add(a,b):
    c=[0]*max(len(a),len(b))
    for k,v in enumerate(a):c[k]+=v
    for k,v in enumerate(b):c[k]+=v
    return trim(c)

def scale(a,c):return trim([c*x for x in a])

def mul(a,b):
    c=[0]*(len(a)+len(b)-1)
    for k,x in enumerate(a):
        for l,y in enumerate(b):c[k+l]+=x*y
    return trim(c)

def evaluate(a,x):
    r=0
    for v in reversed(a):r=r*x+v
    return r

def norm(a):return sum(abs(v) for v in a)

def pseudo_remainder(G,D):
    """Return exponent nu, quotient Q, remainder R: lc(D)^nu G = QD+R."""
    G=trim(G);D=trim(D);R=G;Q=[0];nu=0;a=D[-1];m=degree(D)
    while degree(R)>=m:
        k=degree(R)-m;c=R[-1]
        Q=add(scale(Q,a),[0]*k+[c])
        R=add(scale(R,a),[0]*k+scale(D,-c))
        nu+=1
    return nu,Q,R

def bridge_certificate(F,J):
    F=trim(F);J=trim(J);m=degree(F)
    if m<1 or F[0]!=2 or degree(J)>m:
        raise ValueError('Require deg F >= 1, F(0)=2, deg J <= deg F.')
    J=J+[0]*(m+1-len(J))
    if not all(0<=x<=y for x,y in zip(J,F)):
        raise ValueError('Require coefficientwise 0 <= J <= F.')
    top=J[m];lead=F[m];g=gcd(top,lead);c=top//g;d=lead//g
    T=add(scale(J,d),scale(F,-c));r=max(0,degree(T));h=norm(T);H=sum(F)
    parts=[]
    for s in (1,2):
        D=add(F,[-s]);G=[1]
        for k in range(s+1):G=mul(G,add(T,[c*s-d*k]))
        growth=max(lead,H-s-lead)
        steps=max(0,(s+1)*r-m+1)
        M=growth**steps*prod(h+abs(c*s-d*k) for k in range(s+1))
        nu,Q,R=pseudo_remainder(G,D)
        assert nu<=steps and norm(R)<=M
        assert add(mul(Q,D),R)==scale(G,lead**nu)
        parts.append(dict(s=s,growth=growth,step_bound=steps,remainder_bound=str(M),
            pseudo_exponent=nu,remainder=R,zero_remainder=R==[0]))
    new=6*max(int(v['remainder_bound']) for v in parts)+2
    old=6*H*(H+1)*(H+2)**(2*m+2)+2
    return dict(m=m,H=H,c=c,d=d,T=T,r=r,tail_norm=h,parts=parts,
        adaptive_threshold=str(new),old_threshold=str(old),best_threshold=str(min(new,old)),
        newton_denominator_compatible=(m%d==0))
