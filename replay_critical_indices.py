"""Independent standard-library replay of the critical-index finite remainder.

Run replay_near_collisions.py as well: the saved report alone is not a proof of
its analytic tail, approximation inequalities, or close-power enumeration.
"""
from collections import Counter
from fractions import Fraction as F
from math import comb,gcd,isqrt,prod
from pathlib import Path
import json


def val(n,p):
    e=0
    while n%p==0:n//=p;e+=1
    return e


def algebra_checks():
    count=0
    for n in range(10,201):
        for i in range(3,min(n,121)+1):
            for p in (2,3,5,7,11,13):
                if p>=i:continue
                E=max(val(n-r,p) for r in range(i))
                assert val(comb(n,i),p)<=E-val(i,p)
                count+=1
    return count


def main():
    cert=json.loads(Path('critical_index_certificate.json').read_text(encoding='utf-8'))
    assert cert['schema']==1 and cert['indices']==[96,100,120]
    bounds={i:max(16598*i-1,1771561+i-1) for i in cert['indices']}
    assert {int(k):v for k,v in cert['upper_bounds'].items()}==bounds
    N=cert['sieve_limit'];assert N>max(bounds.values())
    flags=bytearray(b'\x01')*(N+1);flags[:2]=b'\x00\x00'
    for p in range(2,isqrt(N)+1):
        if flags[p]:flags[p*p::p]=b'\x00'*((N-p*p)//p+1)
    previous=2;count=1;gaps=[]
    for p in range(3,N+1):
        if flags[p]:
            if p-previous>96:gaps.append([previous,p])
            previous=p;count+=1
    assert previous>max(bounds.values())
    assert (count,previous,gaps)==(cert['prime_count'],cert['last_prime'],cert['long_gaps'])
    required=set()
    for a,b in gaps:
        for n in range(a+96,b):
            for i in cert['indices']:
                if n>=a+i and 2*i+2<=n<=bounds[i]:required.add((i,n))
    assert [(r['i'],r['n']) for r in cert['exceptions']]==sorted(required)

    def check(c,i,n):
        p,e,r=c['p'],c['e'],c['r']
        assert p>i and all(p%d for d in range(2,isqrt(p)+1)) and e>=1
        assert 0<=r<i and n%p**e==r
        return p**e,r

    maximum=0
    for row in cert['exceptions']:
        i,n=row['i'],row['n'];q,r=check(row['anchor'],i,n)
        candidates=[]
        for k in range((i+1)//q,n//(2*q)+1):
            candidates.extend(range(max(i+1,k*q),min(n//2,k*q+r)+1))
        assert len(candidates)==row['initial_count']
        maximum=max(maximum,len(candidates))
        for c in row['constraints']:
            q,r=check(c,i,n)
            kept=[j for j in candidates if j%q<=r]
            assert len(candidates)-len(kept)==c['eliminated']
            candidates=kept
        assert not candidates
    result={'status':'verified','new_indices':[96,100,120],
            'finite_bounds':bounds,'residual_pairs_by_i':Counter(i for i,n in required),
            'residual_pairs':len(required),'largest_anchor_candidate_count':maximum,
            'cofactor_valuation_checks':algebra_checks(),
            'analytic_tail_requires':'replay_near_collisions.py and its Matveev specialization',
            'combined_range':'all i >= 120 and i=96,97,100,101',
            'complete_solution':False}
    Path('verification_critical_indices.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
