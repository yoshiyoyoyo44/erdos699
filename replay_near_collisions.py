"""Independent exact replay of the bounded-coefficient near-collision theorem.

The deep input is Matveev's explicit logarithmic-form lower bound, stated and
specialized in critical_indices_and_handoff_integration.md. Everything after
that specialization is rechecked with rational intervals and integer arithmetic.
"""
from fractions import Fraction as F
from functools import lru_cache
from math import gcd,isqrt
from pathlib import Path
import json

SCALE=1<<320
TERMS=120
M=10**16
CUTOFF=120
FINAL_EXPONENT_LIMIT=128
PRIMES=[p for p in range(2,120) if all(p%d for d in range(2,isqrt(p)+1))]


def series(a,b):
    t=F(a-b,a+b)
    assert 0<=t<=F(1,3)
    total=2*sum((t**(2*k+1)/F(2*k+1) for k in range(TERMS)),F(0))
    tail=2*t**(2*TERMS+1)/(F(2*TERMS+1)*(1-t*t))
    lower=total*SCALE;upper=(total+tail)*SCALE
    return lower.numerator//lower.denominator,-((-upper.numerator)//upper.denominator)


LOG2=series(2,1)


@lru_cache(None)
def log(n):
    e=n.bit_length()-1
    lo,hi=series(n,1<<e)
    return lo+e*LOG2[0],hi+e*LOG2[1]


def quotient(numerator,denominator):
    corners=[F(n,d) for n in numerator for d in denominator]
    lo=min(corners)*SCALE;hi=max(corners)*SCALE
    return lo.numerator//lo.denominator,-((-hi.numerator)//hi.denominator)


def norm_lower(interval):
    lo,hi=interval
    first_integer=-((-lo)//SCALE)
    if first_integer*SCALE<=hi:return 0
    return min(lo-(first_integer-1)*SCALE,first_integer*SCALE-hi)


def analytic_checks():
    # Matveev's t<=3, D=1 constant; log p,log q<5 and h(a/b)<3.
    K=2*10**13
    assert F(7,5)*30**6*3**5*5*5*3<K
    assert log(113)[1]<5*SCALE and log(18)[1]<3*SCALE
    assert 100*LOG2[0]>69*SCALE
    assert log(238)[1]<6*SCALE and log(M)[1]<37*SCALE
    assert 69*M>100*(6+38*K)
    assert F(69,100)>F(K,M)  # Positive derivative on B>=M.
    assert 238*100<400*69
    return K


def approximations(cert):
    expected=[(p,q) for p in PRIMES for q in PRIMES if p<q]
    assert [(r['p'],r['q']) for r in cert['rows']]==expected
    count=0;maxQ=0
    for row in cert['rows']:
        p,q=row['p'],row['q']
        alpha=quotient(log(p),log(q))
        witnesses=row['approximations']
        for w in witnesses:
            P,Q=w['P'],w['Q']
            assert P>=0 and Q>6*M and gcd(P,Q)==1
            maxQ=max(maxQ,Q)
        w=witnesses[0];P,Q=w['P'],w['Q']
        error=max(abs(Q*alpha[0]-P*SCALE),abs(Q*alpha[1]-P*SCALE))
        assert 2*M*error<SCALE and p**CUTOFF>800*Q
        expected_coefficients={(a,b) for a in range(1,19) for b in range(1,19)
                               if a!=b and gcd(a,b)==1 and gcd(a*b,p*q)==1}
        cases=row['inhomogeneous']
        assert len(cases)==len(expected_coefficients)
        assert {(a,b) for a,b,k in cases}==expected_coefficients
        for a,b,k in cases:
            w=witnesses[k];P,Q=w['P'],w['Q']
            la,lb=log(a),log(b)
            mu=quotient((la[0]-lb[1],la[1]-lb[0]),log(q))
            error=max(abs(Q*alpha[0]-P*SCALE),abs(Q*alpha[1]-P*SCALE))
            epsilon=norm_lower((Q*mu[0],Q*mu[1]))-M*error
            assert epsilon>0 and epsilon*p**CUTOFF>400*Q*SCALE
            count+=1
    return count,maxQ


def enumerate_collisions():
    # Enumerate independently by merging one prime's sorted list with another's.
    # p-free coefficients make the representation unique within each list.
    lists={p:sorted((a*p**e,a,e) for e in range(FINAL_EXPONENT_LIMIT)
                    for a in range(1,19) if a%p) for p in PRIMES}
    maxima={14:(0,None),15:(0,None),18:(0,None)}
    pairs=0
    for p in PRIMES:
        xs=lists[p]
        for q in PRIMES:
            if q<=p:continue
            ys=lists[q];start=0
            for x,a,e in xs:
                while start<len(ys) and ys[start][0]<x-119:start+=1
                k=start
                while k<len(ys) and ys[k][0]<=x+119:
                    y,b,f=ys[k]
                    pairs+=1
                    for A in maxima:
                        if max(a,b)<=A and max(x,y)>maxima[A][0]:
                            maxima[A]=(max(x,y),{'p':p,'q':q,'a':a,'b':b,'e':e,'f':f,
                                                     'left':x,'right':y,'difference':abs(x-y)})
                    k+=1
    assert maxima[18][0]==1771561
    return pairs,{A:{'maximum':maximum,'witness':w} for A,(maximum,w) in maxima.items()}


def coefficient_margins():
    result={}
    C=16598
    for i,A in ((96,14),(100,15),(120,18)):
        r=sum(p<i for p in PRIMES)
        assert i==4*r
        # 2(i-1) log(i*kappa_i*(A+1)^(r-1)), rounded downward.
        lower=(2*(i-1)*log(i)[0]+i*(i-1)*LOG2[0]
               -sum(k*log(k)[1] for k in range(1,i+1))
               +2*i*(i-1)*(log(C-1)[0]-log(C)[1])
               +2*(i-1)*(r-1)*log(A+1)[0])
        assert lower>0
        result[i]=str(F(lower,2*(i-1)*SCALE))
    return result


def main():
    cert=json.loads(Path('near_collision_certificate.json').read_text(encoding='utf-8'))
    assert cert['schema']==1 and cert['initial_exponent_bound']==M
    assert cert['normalized_exponent_cutoff']==CUTOFF
    assert cert['coefficient_bound']==18 and cert['difference_bound']==119
    K=analytic_checks()
    count,maxQ=approximations(cert)
    pairs,maxima=enumerate_collisions()
    result={'status':'verified','prime_pairs':len(cert['rows']),
            'inhomogeneous_cases':count,'homogeneous_cases':len(cert['rows']),
            'initial_exponent_bound':M,'normalized_exponent_cutoff':CUTOFF,
            'enumerated_exponents':'0 <= e,f < 128','matveev_constant_upper':K,
            'maximum_approximation_denominator':maxQ,'enumerated_close_pairs':pairs,
            'maxima':maxima,'coefficient_log_margins_lower':coefficient_margins(),
            'deep_external_input':'Matveev explicit logarithmic-form lower bound',
            'independent_log_bits':320}
    Path('verification_near_collisions.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
