"""Exact audit of the 2-adic inequalities and the 3*2^u square branch."""
from fractions import Fraction as Q
from math import gcd, isqrt
import json

def v2(n):
    assert n>0
    return (n & -n).bit_length()-1

constant=Q(27,16)*Q(64**5,63**3*62**2)
assert constant==Q(16777216,8899821) and constant<2

# The complete arithmetic list in equation (9), without a bound on u.
r1=[]
for d in (1,3,5,15):
    for sign in (-1,1):
        value=Q(d*(d+sign),15)
        if value.denominator==1 and value>0:
            power=int(value)
            if power & (power-1)==0:
                r1.append({'d':d,'sign':sign,'power':power,'u':v2(power)+4})
assert r1==[{'d':5,'sign':1,'power':2,'u':5},
            {'d':15,'sign':1,'power':16,'u':8}]
r2=[]
for d in (1,3):
    for sign in (-1,1):
        value=Q(d*(d+sign),3)
        if value.denominator==1 and value>0:
            power=int(value)
            if power & (power-1)==0:
                r2.append(v2(power)-1)
assert r2==[0,1]

# Independent enumeration of modest cases audits the classification.
square_cases=[]
for u in range(3,15):
    n=3*(1<<u)
    for j in range(4,n//2):
        L=Q(j*(n-j),n-1)
        if L.denominator!=1 or isqrt(L.numerator)**2!=L.numerator:
            continue
        ell=isqrt(L.numerator)
        assert (j-ell)*(j+ell)==n*(j-L)
        residue=j*(n//2-j)*(n-j)%(n//2-1)
        assert residue!=0
        square_cases.append([n,j,int(L),residue])
assert square_cases==[[96,20,16,25],[768,118,100,173]]

valuation_checks=0
for n in range(8,513,4):
    u=v2(n)
    for j in range(4,n//2+1):
        y=n-j
        disc=Q(j*j*y*y*(j-1)*(y-1)*(n-1)*(n-2)**2,12)
        assert disc.denominator==1
        s=v2(disc.numerator)
        if j%2:
            assert s==v2(j-1)+v2(y-1)
            assert min(v2(j-1),v2(y-1))==1 and s>=3
        else:
            assert s==2*v2(j)+2*v2(y)
            if v2(j)<u:
                assert s==4*v2(j)
            else:
                assert s>=4*u
        valuation_checks+=1

out={'rational_constant':str(constant),'r1_complete_power_cases':r1,
     'r2_complete_exponents':r2,'square_cases':square_cases,
     'valuation_identity_checks':valuation_checks,
     'complete_proof_of_erdos699':False,'new_lean_verification':False}
with open('verification_i3_2adic_square.json','w',encoding='utf-8') as f:
    json.dump(out,f,indent=2)
    f.write('\n')
print(json.dumps(out,indent=2))
