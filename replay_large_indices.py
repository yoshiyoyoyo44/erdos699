"""Replay the large-index certificate using only Python's standard library."""
from math import isqrt
import json
from certify_large_indices import certify_index, prove_analytic_tail, trial_primes

with open('large_index_certificate.json',encoding='utf-8') as f:
    cert=json.load(f)
with open('prime_gap_certificate.json',encoding='utf-8') as f:
    gap_cert=json.load(f)

assert cert['C']==16598 and cert['min_i']==205
assert cert['analytic_tail']==prove_analytic_tail()
assert [r['i'] for r in cert['rows']]==list(range(205,900))
primes_small=trial_primes(900)
for row in cert['rows']:
    assert row==certify_index(row['i'],primes_small)
assert cert['maximum_danger_n']==max(b for r in cert['rows'] for a,b in r['danger_intervals'])

# A separate bytearray implementation of the complete odd-number sieve.
N=gap_cert['sieve_limit']
assert N>max(4021520,cert['maximum_danger_n'])
length=(N+1)//2
flags=bytearray(b'\x01')*length
flags[0]=0
for p in range(3,isqrt(N)+1,2):
    if flags[p//2]:
        start=p*p//2
        count=(length-1-start)//p+1
        flags[start::p]=b'\x00'*count
last=2
count=1
maximum=0
small_maximum=0
long_gaps=[]
for k in range(1,length):
    if flags[k]:
        p=2*k+1
        gap=p-last
        maximum=max(maximum,gap)
        if last<=4021520:
            small_maximum=max(small_maximum,gap)
        if gap>205:
            long_gaps.append([last,p])
        count+=1
        last=p
assert last>cert['maximum_danger_n']
assert (last,count,maximum,small_maximum,long_gaps)==(
    gap_cert['last_prime'],gap_cert['prime_count'],gap_cert['maximum_gap'],
    gap_cert['small_n_gap_max'],gap_cert['long_gaps'])
assert small_maximum<205

exceptions=set()
for row in cert['rows']:
    i=row['i']
    for left,right in long_gaps:
        for lo,hi in row['danger_intervals']:
            exceptions.update((i,n) for n in range(max(lo,left+i),min(hi,right-1)+1))
assert sorted(exceptions)==[(r['i'],r['n']) for r in gap_cert['residue_certificates']]
assert len(exceptions)==gap_cert['exception_count']

def check_constraint(c,i,n):
    p,e,q,r=c['p'],c['e'],c['q'],c['r']
    assert p>i and e>=1 and q==p**e and 0<=r<i
    # Independent elementary trial division proves primality.
    assert all(p%d for d in range(2,isqrt(p)+1))
    assert n%q==r

for row in gap_cert['residue_certificates']:
    i,n=row['i'],row['n']
    anchor=row['anchor']
    check_constraint(anchor,i,n)
    q,r=anchor['q'],anchor['r']
    # Enumerate by successive blocks rather than residue classes.
    candidates=[]
    for block in range((i+1)//q,n//(2*q)+1):
        candidates.extend(range(max(i+1,block*q),min(n//2,block*q+r)+1))
    assert len(candidates)==row['initial_count']
    for c in row['constraints_used']:
        check_constraint(c,i,n)
        kept=[j for j in candidates if j%c['q']<=c['r']]
        assert len(candidates)-len(kept)==c['eliminated']
        candidates=kept
    assert not candidates

result={'status':'verified','all_indices_at_least':205,
        'finite_indices':len(cert['rows']),
        'rationally_checked_segments':sum(r['tested_segments'] for r in cert['rows']),
        'prime_sieve_limit':N,'residue_pairs_eliminated':len(exceptions),
        'uses_external_prime_estimates':True,
        'complete_proof_of_erdos699':False,'new_lean_verification':False}
with open('verification_large_indices.json','w',encoding='utf-8') as f:
    json.dump(result,f,indent=2)
    f.write('\n')
print(json.dumps(result,indent=2))
