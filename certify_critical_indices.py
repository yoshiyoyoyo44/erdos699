"""Finite Kummer certificate below the new near-collision tail bounds."""
from functools import lru_cache
from math import isqrt,prod
from pathlib import Path
import json


def main():
    import numpy as np
    indices=[96,100,120]
    near=1771561
    bounds={i:max(16598*i-1,near+i-1) for i in indices}
    N=max(bounds.values())+100
    flags=np.ones((N+1)//2,dtype=np.bool_);flags[0]=False
    for p in range(3,isqrt(N)+1,2):
        if flags[p//2]:flags[p*p//2::p]=False
    primes=np.concatenate((np.array([2],dtype=np.int64),2*np.flatnonzero(flags)+1))
    assert primes[-1]>max(bounds.values())
    gaps=[(int(a),int(b)) for a,b in zip(primes[:-1],primes[1:]) if b-a>min(indices)]
    exceptions=sorted({(i,n) for i in indices for a,b in gaps
                       for n in range(max(a+i,2*i+2),min(b,bounds[i]+1))})
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
    for i,n in exceptions:
        constraints=sorted([(p**e,r,p,e) for r in range(i)
                            for p,e in factor(n-r) if p>i],reverse=True)
        q,r,p,e=constraints[0]
        candidates=[]
        for rem in range(r+1):
            first=rem+max(0,(i+1-rem+q-1)//q)*q
            candidates.extend(range(first,n//2+1,q))
        initial=len(candidates);used=[]
        for modulus,rem,prime,exponent in constraints[1:]:
            kept=[j for j in candidates if j%modulus<=rem]
            if len(kept)<len(candidates):
                used.append({'p':prime,'e':exponent,'r':rem,'eliminated':len(candidates)-len(kept)})
                candidates=kept
            if not candidates:break
        assert not candidates,(i,n)
        rows.append({'i':i,'n':n,'anchor':{'p':p,'e':e,'r':r},
                     'initial_count':initial,'constraints':used})
    cert={'schema':1,'indices':indices,'upper_bounds':bounds,'sieve_limit':N,
          'prime_count':len(primes),'last_prime':int(primes[-1]),'long_gaps':gaps,'exceptions':rows}
    Path('critical_index_certificate.json').write_text(json.dumps(cert,indent=2)+'\n',encoding='utf-8')
    from collections import Counter
    print('COMPLETE',dict(Counter(r['i'] for r in rows)),bounds)


if __name__=='__main__':main()
