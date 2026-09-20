"""Independent replay of the lower range needed for the i=119, n<=10^87 result."""
from repo_paths import artifact_path
from math import isqrt
from pathlib import Path
import json
from replay_interval_indices import log_bounds,LOG2,possible_carry


def main():
    cert=json.loads(artifact_path('i119_finite_certificate.json').read_text(encoding='utf-8'))
    assert cert['schema']==1 and cert['i']==119 and cert['C']==16598
    i=119;C=16598;end=194871828
    assert cert['interval_upper']==end
    primes=[p for p in range(2,i) if all(p%d for d in range(2,isqrt(p)+1))]
    constant=(2*i*(i-1)*LOG2[0]-2*sum(k*log_bounds(k)[1] for k in range(1,i+1))
              +4*i*(i-1)*(log_bounds(C-1)[0]-log_bounds(C)[1]))
    expected_lo=C*i
    for lo,hi in cert['interval_leaves']:
        assert lo==expected_lo and lo<=hi<=end
        expected_lo=hi+1;upper=0
        for p in primes:
            q=p;exp=0
            while q<=hi:
                exp+=int(possible_carry(lo,hi,q,i%q));q*=p
            upper+=exp*log_bounds(p)[1]
        assert constant+i*(i-1)*log_bounds(lo)[0]-4*(i-1)*upper>0
    assert expected_lo==end+1
    assert cert['tested_nodes']==2*len(cert['interval_leaves'])-1
    data=cert['small'];N=data['sieve_limit'];assert N>C*i
    flags=bytearray(b'\x01')*(N+1);flags[:2]=b'\x00\x00'
    for p in range(2,isqrt(N)+1):
        if flags[p]:flags[p*p::p]=b'\x00'*((N-p*p)//p+1)
    previous=2;count=1;gaps=[]
    for p in range(3,N+1):
        if flags[p]:
            if p-previous>i:gaps.append([previous,p])
            previous=p;count+=1
    assert previous>=C*i-1
    assert (previous,count,gaps)==(data['last_prime'],data['prime_count'],data['long_gaps'])
    needed={n for a,b in gaps for n in range(a+i,b) if 2*i+2<=n<C*i}
    assert [r['n'] for r in data['exceptions']]==sorted(needed)

    def constraint(c,n):
        p,e,r=c['p'],c['e'],c['r']
        assert p>119 and e>=1 and all(p%d for d in range(2,isqrt(p)+1))
        assert 0<=r<i and n%p**e==r
        return p**e,r

    for row in data['exceptions']:
        n=row['n'];q,r=constraint(row['anchor'],n);candidates=[]
        for k in range(120//q,n//(2*q)+1):
            candidates.extend(range(max(120,k*q),min(n//2,k*q+r)+1))
        assert len(candidates)==row['initial_count']
        for c in row['constraints']:
            q,r=constraint(c,n)
            kept=[j for j in candidates if j%q<=r]
            assert len(candidates)-len(kept)==c['eliminated'];candidates=kept
        assert not candidates
    result={'status':'verified','i':119,'lower_range_upper':end,
            'interval_leaves':len(cert['interval_leaves']),'small_pairs':len(needed),
            'combined_with_a100_near_collision_proof':'no counterexample for n <= 10^87',
            'requires_replay':'replay_near_collisions_a100.py',
            'all_i119_solved':False}
    artifact_path('verification_i119_finite.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
