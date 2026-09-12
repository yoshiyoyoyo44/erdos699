"""Deterministic Eratosthenes sieve, gap covering, and residue certificates."""
from math import isqrt, prod
import json
import time
import numpy as np

started=time.monotonic()
with open('large_index_certificate.json',encoding='utf-8') as f:
    cert=json.load(f)
N=max(4021520,cert['maximum_danger_n'])+10000
# Array index t represents the odd number 2*t+1.
sieve=np.ones((N+1)//2,dtype=np.bool_)
sieve[0]=False
for p in range(3,isqrt(N)+1,2):
    if sieve[p//2]:
        sieve[p*p//2::p]=False
primes=np.concatenate((np.array([2],dtype=np.int64),2*np.flatnonzero(sieve)+1))
assert primes[-1]>cert['maximum_danger_n']
gaps=np.diff(primes)
small=gaps[primes[:-1]<=4021520]
assert int(small.max())<cert['min_i']
large_positions=np.flatnonzero(gaps>cert['min_i'])
exceptions=[]
for row in cert['rows']:
    i=row['i']
    for index in large_positions:
        left,right=int(primes[index]),int(primes[index+1])
        if right-left<=i:
            continue
        for lo,hi in row['danger_intervals']:
            for n in range(max(lo,left+i),min(hi,right-1)+1):
                exceptions.append((i,n))
exceptions=sorted(set(exceptions))
trial=[int(p) for p in primes if p<=isqrt(N)]

def factor(n):
    original=n
    factors=[]
    for p in trial:
        if p*p>n:
            break
        if n%p==0:
            e=0
            while n%p==0:
                n//=p
                e+=1
            factors.append([p,e])
    if n>1:
        factors.append([n,1])
    assert prod(p**e for p,e in factors)==original
    return factors

residue_rows=[]
for i,n in exceptions:
    constraints=[]
    for r in range(i):
        for p,e in factor(n-r):
            if p>i:
                constraints.append((p**e,r,p,e))
    constraints.sort(reverse=True)
    q,r,p,e=constraints[0]
    candidates=[]
    for residue in range(r+1):
        first=residue+max(0,(i+1-residue+q-1)//q)*q
        candidates.extend(range(first,n//2+1,q))
    initial_count=len(candidates)
    used=[]
    for modulus,rem,prime,exponent in constraints:
        rejected=[j for j in candidates if j%modulus>rem]
        if rejected:
            candidates=[j for j in candidates if j%modulus<=rem]
            used.append({'q':modulus,'r':rem,'p':prime,'e':exponent,
                         'eliminated':len(rejected)})
        if not candidates:
            break
    assert not candidates, (i,n,candidates)
    residue_rows.append({'i':i,'n':n,'anchor':{'q':q,'r':r,'p':p,'e':e},
                         'initial_count':initial_count,'constraints_used':used})

out={'sieve_limit':N,'last_prime':int(primes[-1]),'prime_count':len(primes),
     'maximum_gap':int(gaps.max()),'small_n_gap_max':int(small.max()),
     'long_gaps':[[int(primes[k]),int(primes[k+1])] for k in large_positions],
     'exception_count':len(exceptions),'residue_certificates':residue_rows}
with open('prime_gap_certificate.json','w',encoding='utf-8') as f:
    json.dump(out,f,indent=2)
    f.write('\n')
print(json.dumps({k:v for k,v in out.items() if k!='residue_certificates'},indent=2))
print('Residue pairs:',exceptions)
print('Elapsed seconds:',time.monotonic()-started)
