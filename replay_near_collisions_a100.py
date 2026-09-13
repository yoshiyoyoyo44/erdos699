"""Independent rational replay for coefficient bound 100 and the i=119 bootstrap."""
from fractions import Fraction as F
from math import gcd
from pathlib import Path
import json
from replay_near_collisions import SCALE,log,LOG2,quotient,norm_lower,PRIMES

M=10**16
CUTOFF=128
LIMIT=144


def main():
    cert=json.loads(Path('near_collision_a100_certificate.json').read_text(encoding='utf-8'))
    assert (cert['schema'],cert['A'],cert['difference'],cert['M'],cert['cutoff'])==(1,100,119,M,CUTOFF)
    K=4*10**13
    assert F(7,5)*30**6*3**5*5**3<K
    assert log(113)[1]<5*SCALE and log(100)[1]<5*SCALE
    assert log(238)[1]<6*SCALE and log(M)[1]<37*SCALE
    assert 100*LOG2[0]>69*SCALE and 69*M>100*(6+38*K)
    assert F(69,100)>F(K,M)
    expected=[(p,q) for p in PRIMES for q in PRIMES if p<q]
    assert [(r['p'],r['q']) for r in cert['rows']]==expected
    count=0;max_den=0
    for row in cert['rows']:
        p,q=row['p'],row['q'];alpha=quotient(log(p),log(q));p_power=p**CUTOFF
        approx=[]
        for P,Q in row['approximations']:
            assert Q>6*M and P>0 and gcd(P,Q)==1
            error=max(abs(Q*alpha[0]-P*SCALE),abs(Q*alpha[1]-P*SCALE))
            approx.append((Q,error))
            max_den=max(max_den,Q)
        Q,error=approx[0]
        assert 2*M*error<SCALE and p_power>800*Q
        for a in range(1,101):
            for b in range(a+1,101):
                if gcd(a,b)!=1 or gcd(a*b,p*q)!=1:continue
                la,lb=log(a),log(b)
                mu=quotient((la[0]-lb[1],la[1]-lb[0]),log(q))
                for Q,error in approx:
                    epsilon=norm_lower((Q*mu[0],Q*mu[1]))-M*error
                    if epsilon>0 and epsilon*p_power>400*Q*SCALE:break
                else:raise AssertionError(('missing approximation',p,q,a,b))
                count+=2
    assert count==cert['inhomogeneous_count']
    print('APPROXIMATIONS_VERIFIED',count,flush=True)
    # Normalization costs <=6 in either exponent. E<128 gives e<=133;
    # q^f <=100*p^133+119 <101*q^133 <q^138, hence f<=137.
    assert 2**6<=100<2**7 and 101<3**5
    lists={p:sorted((a*p**e,a,e) for e in range(LIMIT) for a in range(1,101) if a%p)
           for p in PRIMES}
    maximum=0;witness=None;pairs=0
    for p in PRIMES:
        for q in PRIMES:
            if q<=p:continue
            ys=lists[q];start=0
            for x,a,e in lists[p]:
                while start<len(ys) and ys[start][0]<x-119:start+=1
                k=start
                while k<len(ys) and ys[k][0]<=x+119:
                    y,b,f=ys[k];pairs+=1
                    if max(x,y)>maximum:
                        maximum=max(x,y)
                        witness={'p':p,'q':q,'a':a,'b':b,'e':e,'f':f,'left':x,'right':y,'difference':abs(x-y)}
                    k+=1
    i=119;r=30;C=16598
    assert sum(p<i for p in PRIMES)==r
    # Lower bound for 2(i-1)*[4 log(i*kappa_i*101^29)-87 log10].
    margin=(8*(i-1)*log(i)[0]+4*i*(i-1)*LOG2[0]
            -4*sum(k*log(k)[1] for k in range(1,i+1))
            +8*i*(i-1)*(log(C-1)[0]-log(C)[1])
            +8*(i-1)*29*log(101)[0]-2*(i-1)*87*log(10)[1])
    assert margin>0
    result={'status':'verified','A':100,'inhomogeneous_cases':count,'homogeneous_cases':435,
            'maximum_approximation_denominator':max_den,'normalized_exponents_less_than':128,
            'enumerated_exponents_less_than':144,'close_pairs':pairs,
            'maximum_close_value':maximum,'witness':witness,
            'i119_bootstrap_lower_exclusive':maximum+118,
            'i119_bootstrap_upper_inclusive':'10^87',
            'i119_log_margin_lower':str(F(margin,2*(i-1)*SCALE)),
            'all_i119_solved':False}
    Path('verification_near_collisions_a100.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
