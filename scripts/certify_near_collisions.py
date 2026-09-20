"""Certify bounded-coefficient near collisions via elementary approximation bounds.

The analytic initial exponent bound is proved separately in the accompanying note.
No unproved numerical sign or exhaustive continued-fraction assumption is used.
"""
from repo_paths import artifact_path
from math import gcd,isqrt
from pathlib import Path
import json
from near_collision_arithmetic import SCALE,log,ratio,distance_lower,approximants

M=10**16
EXPONENT_CUTOFF=120
PRIMES=[p for p in range(2,120) if all(p%d for d in range(2,isqrt(p)+1))]


def main():
    rows=[];total=0;largest_Q=0
    for p in PRIMES:
        for q in PRIMES:
            if p>=q:continue
            alpha=ratio(log(p),log(q))
            candidates=approximants(alpha,6*M)
            assert candidates
            h,Q=next((h,Q) for h,Q in candidates
                     if 2*M*max(abs(Q*alpha[0]-h*SCALE),abs(Q*alpha[1]-h*SCALE))<SCALE
                     and p**EXPONENT_CUTOFF>800*Q)
            used={(h,Q):0};witnesses=[{'P':h,'Q':Q}];cases=[]
            for a in range(1,19):
                for b in range(1,19):
                    if a==b or gcd(a,b)>1 or gcd(a*b,p*q)>1:continue
                    la,lb=log(a),log(b)
                    mu=ratio((la[0]-lb[1],la[1]-lb[0]),log(q))
                    for h,Q in candidates:
                        error=max(abs(Q*alpha[0]-h*SCALE),abs(Q*alpha[1]-h*SCALE))
                        epsilon=distance_lower(Q*mu[0],Q*mu[1])-M*error
                        if epsilon>0 and epsilon*p**EXPONENT_CUTOFF>400*Q*SCALE:
                            if (h,Q) not in used:
                                used[h,Q]=len(witnesses);witnesses.append({'P':h,'Q':Q})
                            cases.append([a,b,used[h,Q]])
                            largest_Q=max(largest_Q,Q)
                            break
                    else:raise AssertionError(('unresolved',p,q,a,b))
            rows.append({'p':p,'q':q,'approximations':witnesses,'inhomogeneous':cases})
            total+=len(cases)
        print('prime',p,'pairs',len(rows),'cases',total,flush=True)
    cert={'schema':1,'initial_exponent_bound':M,'normalized_exponent_cutoff':EXPONENT_CUTOFF,
          'coefficient_bound':18,'difference_bound':119,'rows':rows}
    artifact_path('near_collision_certificate.json').write_text(json.dumps(cert,indent=2)+'\n',encoding='utf-8')
    print('COMPLETE',len(rows),total,'max denominator',largest_Q,flush=True)


if __name__=='__main__':main()
