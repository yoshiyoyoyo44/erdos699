"""Extend the close-power certificate to coefficients <=100, compactly."""
from math import gcd,isqrt
from pathlib import Path
import json
from near_collision_arithmetic import SCALE,log,ratio,distance_lower,approximants

M=10**16
CUTOFF=128
A=100
PRIMES=[p for p in range(2,120) if all(p%d for d in range(2,isqrt(p)+1))]


def main():
    rows=[];count=0
    for p in PRIMES:
        for q in PRIMES:
            if p>=q:continue
            alpha=ratio(log(p),log(q));candidates=approximants(alpha,6*M)
            h,Q=next((h,Q) for h,Q in candidates
                     if 2*M*max(abs(Q*alpha[0]-h*SCALE),abs(Q*alpha[1]-h*SCALE))<SCALE
                     and p**CUTOFF>800*Q)
            witnesses=[(h,Q)]
            cached=[(h,Q,max(abs(Q*alpha[0]-h*SCALE),abs(Q*alpha[1]-h*SCALE))) for h,Q in candidates]
            for a in range(1,A+1):
                for b in range(a+1,A+1):
                    # mu and -mu have the same distance from an integer.
                    if gcd(a,b)>1 or gcd(a*b,p*q)>1:continue
                    la,lb=log(a),log(b)
                    mu=ratio((la[0]-lb[1],la[1]-lb[0]),log(q))
                    for h,Q,error in cached:
                        epsilon=distance_lower(Q*mu[0],Q*mu[1])-M*error
                        if epsilon>0 and epsilon*p**CUTOFF>400*Q*SCALE:
                            if (h,Q) not in witnesses:witnesses.append((h,Q))
                            break
                    else:raise AssertionError(('unresolved',p,q,a,b))
                    count+=2
            rows.append({'p':p,'q':q,'approximations':witnesses})
        print('prime',p,'pairs',len(rows),'cases',count,flush=True)
    result={'schema':1,'A':A,'difference':119,'M':M,'cutoff':CUTOFF,
            'inhomogeneous_count':count,'rows':rows}
    Path('near_collision_a100_certificate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('COMPLETE',count,flush=True)


if __name__=='__main__':main()
