"""Exact checks for the descent update and its local Kummer obstruction.

The diagnostic families are not counterexamples to Erdos 699.
"""

import json
from fractions import Fraction as F
from math import gcd
from pathlib import Path

import sympy as s

from audit_i3_mixed_parameter_bound import delta, quantities, v2


def digits(n,p):
    out=[]
    while n:
        out.append(n%p)
        n//=p
    return out or [0]


def lucas_pass(n,j,p):
    while n or j:
        if j%p>n%p:
            return False
        n//=p
        j//=p
    return True


def binomial_valuation(n,j,p):
    def fact(a):
        total=0
        while a:
            a//=p
            total+=a
        return total
    return fact(n)-fact(j)-fact(n-j)


def algebra():
    n,j,b,ep,w,z,X=s.symbols('n j b ep w z X')
    N=n/2
    J=j*(n-j)/(n-1)
    oldz=((n-2*j)**2-n)/(2*(n-1))
    oldw=2*b*(oldz**2-1)/(n-2)
    zp=b*((N-2*J)**2-N)/(2*(N-1))
    rp=b*J*(J-1)/(2*(N-1))
    P=j*(j-1)*(j-2)
    nn=612+56108*X
    jj=235+21580*X
    JJ=145+13280*X
    checks=[
        zp-(oldw-b)/2,
        rp-(b*n+2*oldw-2*b-4*b*oldz)/16,
        4*ep*(((w-b)/2)**2-b*b)/(n-4)-ep*(w-3*b)*(w+b)/(n-4),
        (b*(2*(j-1)**2-1))**2-b*b-4*b*b*P*(j-1),
        (b*j*(j-1)/2)*(b*j*(j-1)/2-b)-b*b*P*(j+1)/4,
        P*(j+1)-P*(j-1)-2*P,
        jj*(nn-jj)-(nn-1)*JJ,
        nn-(13*(47+4316*X)+1),
        jj-5*(47+4316*X),
    ]
    for expr in checks:
        assert s.factor(expr)==0
    return len(checks)


def modular_equivalence():
    count=0
    for q in (3,5,7,9,15,25,27,35,49,81,125):
        for J in range(q):
            P=J*(J-1)*(J-2)
            assert (P%q==0)==(P*(J-1)%q==0 and P*(J+1)%q==0)
            count+=1
    for J,center,endpoint in ((6,True,False),(24,False,True)):
        P=J*(J-1)*(J-2)
        assert (P*(J-1)%25==0)==center
        assert (P*(J+1)%25==0)==endpoint
        assert P%25!=0
    return count


def two_condition_example():
    n,j=3258244432,1087547175
    N=n//2
    J=j*(n-j)//(n-1)
    assert (delta(n-1),delta(n//2-1))==(1,1)
    assert j*(j-1)%(n-1)==0
    assert j*(j-1)*(j-2)%(n//2-1)==0
    assert n%8==0 and j%2 and J%2 and 4<=J<N//2
    assert 5*7*53*593*1481==n//2-1
    p=53
    assert lucas_pass(n,j,p) and not lucas_pass(N,J,p)
    assert binomial_valuation(n,3,p)==1 and binomial_valuation(N,3,p)==1
    assert binomial_valuation(n,j,p)==0 and binomial_valuation(N,J,p)>0
    assert (J-1)%(p*p)==0
    z,rho,r,w,lam=quantities(n,j,1,1)
    ep=delta(N//2-1)
    zp=(w-1)/2
    rp=F(J*(J-1),n-2)
    wp=ep*(w-3)*(w+1)/(n-4)
    lp=F(4*ep)*rp*(rp-1)/(n-4)
    assert zp.denominator==1 and rp.denominator==1
    assert wp.denominator>1 and lp.denominator>1
    return {'n':n,'j':j,'N':N,'J':J,'p':p,'v2_n':v2(n),
            'digits_low_to_high':{str(a):digits(a,p) for a in (n,j,N,J)},
            'old_binomial_p_valuation':binomial_valuation(n,j,p),
            'new_binomial_p_valuation':binomial_valuation(N,J,p),
            'w_prime':str(wp),'lambda_prime':str(lp),
            'counterexample_to_erdos_699':False}


def infinite_family_checks():
    assert lucas_pass(612,235,5) and lucas_pass(56108,21580,5)
    assert not lucas_pass(306,145,5)
    checked=0
    for k in (4,5,7,13,31,61):
        n,j=612+56108*5**k,235+21580*5**k
        N,J=306+28054*5**k,145+13280*5**k
        assert n//2==N and j*(n-j)==(n-1)*J
        assert n%8==0 and j%2 and J%2 and 4<=j<n//2 and 4<=J<N//2
        assert gcd(n,j)==1
        assert lucas_pass(n,j,5) and not lucas_pass(N,J,5)
        assert binomial_valuation(n,3,5)==1 and binomial_valuation(N,3,5)==1
        assert binomial_valuation(n,j,5)==0 and binomial_valuation(N,J,5)>0
        if k%6==1:
            assert n%9==1 and (delta(n-1),delta(n//2-1))==(1,1)
        checked+=1
    return {'direct_examples_checked':checked,
            'block_digits_low_to_high':{str(a):digits(a,5) for a in (612,235,56108,21580,306,145)}}


def exponent_for_precision(U):
    assert U>=5
    precision=U-2
    modulus=2**precision
    target=-153*pow(14027,-1,modulus)%modulus
    assert target%4==1
    k=0
    for r in range(3,precision+1):
        if pow(5,k,2**r)!=target%(2**r):
            k+=2**(r-3)
        assert pow(5,k,2**r)==target%(2**r)
    period=2**(U-4)
    k+=((1-k)*pow(period,-1,3)%3)*period
    while k<4:
        k+=3*period
    assert k%6==1
    assert (612+56108*pow(5,k,2**U))%(2**U)==0
    assert (612+56108*pow(5,k,9))%9==1
    return {'minimum_v2_n':U,'k':k,'k_period':3*period}


def main():
    result={'status':'passed','symbolic_identities':algebra(),
            'modular_equivalence_residues':modular_equivalence(),
            'two_divisibility_diagnostic':two_condition_example(),
            'infinite_family':infinite_family_checks(),
            'high_2adic_precision_examples':[exponent_for_precision(U) for U in (5,16,49,100)],
            'scope':'Updates and non-preservation under stated partial hypotheses; not a solution of Erdos 699.'}
    path=Path(__file__).with_name('verification_i3_descent_kummer_obstruction.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
