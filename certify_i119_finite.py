"""Close the finite range left below the A=100 near-collision bootstrap."""
from math import isqrt,prod
from functools import lru_cache
from pathlib import Path
import json
from certify_large_indices import C,LOG2,log_interval,trial_primes


def cover(end):
    i=119
    ps=trial_primes(i-1)
    constant=(2*i*(i-1)*LOG2[0]-2*sum(k*log_interval(k)[1] for k in range(1,i+1))
              +4*i*(i-1)*(log_interval(C-1)[0]-log_interval(C)[1]))
    data=[]
    for p in ps:
        powers=[];q=p
        while q<=end:
            if i%q:powers.append((q,i%q))
            q*=p
        data.append((log_interval(p)[1],powers))
    stack=[(C*i,end)];leaves=[];nodes=0
    while stack:
        lo,hi=stack.pop();upper=0
        for logp,powers in data:
            exponent=sum(q<=hi and (lo%q<r or hi//q>lo//q) for q,r in powers)
            upper+=exponent*logp
        margin=constant+i*(i-1)*log_interval(lo)[0]-4*(i-1)*upper
        nodes+=1
        if margin>0:leaves.append([lo,hi])
        else:
            assert lo<hi,('unresolved singleton',lo)
            mid=(lo+hi)//2;stack.extend([(mid+1,hi),(lo,mid)])
    return leaves,nodes


def small():
    import numpy as np
    end=C*119-1;N=end+100
    flags=np.ones((N+1)//2,dtype=np.bool_);flags[0]=False
    for p in range(3,isqrt(N)+1,2):
        if flags[p//2]:flags[p*p//2::p]=False
    primes=np.concatenate((np.array([2],dtype=np.int64),2*np.flatnonzero(flags)+1))
    assert primes[-1]>end
    gaps=[[int(a),int(b)] for a,b in zip(primes[:-1],primes[1:]) if b-a>119]
    exceptions=sorted({n for a,b in gaps for n in range(max(a+119,240),min(b,end+1))})
    trial=[int(p) for p in primes if p<=isqrt(N)]

    @lru_cache(None)
    def factor(n):
        original=n;out=[]
        for p in trial:
            if p*p>n:break
            e=0
            while n%p==0:n//=p;e+=1
            if e:out.append((p,e))
        if n>1:out.append((n,1))
        assert prod(p**e for p,e in out)==original
        return out

    rows=[]
    for n in exceptions:
        constraints=sorted([(p**e,r,p,e) for r in range(119) for p,e in factor(n-r) if p>119],reverse=True)
        q,r,p,e=constraints[0]
        js=[]
        for rem in range(r+1):
            first=rem+max(0,(120-rem+q-1)//q)*q
            js.extend(range(first,n//2+1,q))
        initial=len(js);used=[]
        for mod,rem,prime,exp in constraints[1:]:
            kept=[j for j in js if j%mod<=rem]
            if len(kept)<len(js):
                used.append({'p':prime,'e':exp,'r':rem,'eliminated':len(js)-len(kept)});js=kept
            if not js:break
        assert not js
        rows.append({'n':n,'anchor':{'p':p,'e':e,'r':r},'initial_count':initial,'constraints':used})
    return {'sieve_limit':N,'last_prime':int(primes[-1]),'prime_count':len(primes),
            'long_gaps':gaps,'exceptions':rows}


def main():
    near=json.loads(Path('verification_near_collisions_a100.json').read_text(encoding='utf-8'))
    end=near['maximum_close_value']+118
    leaves,nodes=cover(end)
    result={'schema':1,'i':119,'C':C,'interval_upper':end,'interval_leaves':leaves,
            'tested_nodes':nodes,'small':small()}
    Path('i119_finite_certificate.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print('COMPLETE','intervals',len(leaves),'small pairs',len(result['small']['exceptions']),'end',end)


if __name__=='__main__':main()
