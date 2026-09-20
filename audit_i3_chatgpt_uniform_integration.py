"""Short exact checks for the September 20 ChatGPT integration.

These checks support the paper proofs; they are not a search for counterexamples.
"""

import json
from fractions import Fraction as F
from math import gcd
from pathlib import Path

import sympy as s

from audit_i3_mixed_parameter_bound import chi, delta, quantities, v2


def algebra():
    n,j,a,b,T,H,k,x = s.symbols('n j a b T H k x')
    q1=(n-1)/a
    q=(n-2)/(2*b)
    z=((n-2*j)**2-n)/(2*q1)
    rho=j*(j-1)/(2*q1)
    r=2*rho-a
    w=(z*z-a*a)/q
    lam=rho*(rho-a)/q
    D=w-4*lam
    pm=2*j*j-4*j*n+2*j+n*n+n-2
    pp=6*j*j-4*j*n-2*j+n*n-3*n+2
    checks=[
        a*n/(2*T*x*x)-2*a*j*(n-j)/(T*x*x*(n-1))-z/(T*x*x),
        (z+r)-3*(z-r)-a*(4*j-n-4),
        2*q1*(z-r)-pm,
        2*q1*(z+r)-pp,
        (2*j-2*n+1)**2-(2*n*n-6*n+5)-2*pm,
        (6*j-2*n-1)**2+(2*n*n-22*n+11)-6*pp,
        (8*pm).subs(j,(n+4)/4)-(n*n-12*n+16),
        ((n-j)*(2*n-j-2)-j*(j-1))-(n-1)*(2*n-3*j),
    ]
    for expr in checks:
        assert s.factor(expr)==0
    c0=a*a*b
    expansions=[(D,c0,c0*(H-4*k)/2),
                (w,c0,c0*H/2),(lam,0,c0*k/2)]
    for expr,constant,linear in expansions:
        residual=s.cancel(expr.subs({n:T*H,j:T*k})-constant-T*linear)
        num,den=s.fraction(residual)
        assert s.rem(num,T*T,T)==0
        # The rational denominators are units at odd primes dividing T.
        assert den.subs(T,0) != 0
    return {'identities':len(checks),'first_order_expansions':len(expansions)}


def modular_cases():
    count=0
    for T in (1,5,7,25,35):
        for u in (12,19):
            for gamma,d1,d2 in ((1,1,1),(1,1,3),(1,3,1),(3,1,1)):
                H=gamma*2**u
                n=T*H
                for k in (1,2,3,7,12,19):
                    j=T*k
                    z,rho,r,w,lam=quantities(n,j,d1,d2)
                    c0=d1*d1*d2
                    for value,target in (((w-4*lam-c0)/T,F(c0*(H-4*k),2)),
                                         ((w-c0)/T,F(c0*H,2)),
                                         (lam/T,F(c0*k,2))):
                        diff=value-target
                        assert gcd(diff.denominator,T)==1
                        assert diff.numerator % T==0
                    count+=1
    return count


def relaxed_examples():
    pairs=[]
    for t in range(12):
        A,B,C=18*t+11,144*t+85,72*t+41
        pairs.append((2*A*B*C+2,(108*t+63)*B*(8*t+5)))
    pairs.append((175492,60606))
    for n,j in pairs:
        d1,d2=delta(n-1),delta(n//2-1)
        z,rho,r,w,lam=quantities(n,j,d1,d2)
        assert all(v.denominator==1 for v in (z,rho,r,w,lam))
        z,r=int(z),int(r)
        q=(n//2-1)//d2
        q1=(n-1)//d1
        A,B,C=gcd(q,j-1),gcd(q,j),gcd(q,j-2)
        d,plus=z-r,z+r
        ell,m=d//(A*C),plus//B
        assert ell*A*C==d and m*B==plus
        G=gcd(abs(ell),m)
        G0=G//gcd(G,d1)
        assert G==gcd(abs(d),plus)
        assert (n*n-12*n+16)%G0==0
        assert (int(w-4*lam))%(G*G)==0
        assert G%9!=0 and G%25!=0
        assert gcd(G,q)==1 and 5%gcd(G,q1)==0
        assert ((2*j-2*n+1)**2-(2*n*n-6*n+5))%abs(ell)==0
        assert ((6*j-2*n-1)**2+(2*n*n-22*n+11))%m==0
        LC=F(d1*(n-j)*(2*n-j-2),(n-1)*C*C)
        assert LC.denominator==1 and LC%chi(v2(j))==0
        # T=1 is only a relaxed normalization for these examples.
        N=F(d1*n,2**(2*v2(j)+1))
        J=F(d1*j*(n-j),2**(2*v2(j))*(n-1))
        assert N-2*J==F(z,2**(2*v2(j)))
    return len(pairs)


def small_prime_checks():
    for n in range(75):
        value=n*n-12*n+16
        assert value%3!=0
        if value%5==0:
            assert value%25!=0
    return 75


def main():
    result={'status':'passed','symbolic':algebra(),
            'modular_parameter_cases':modular_cases(),
            'relaxed_examples':relaxed_examples(),
            'small_prime_residues':small_prime_checks(),
            'scope':'Short exact checks only; neither a Kummer-preserving descent nor a full solution.'}
    path=Path(__file__).with_name('verification_i3_chatgpt_uniform_integration.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__=='__main__':
    main()
