#!/usr/bin/env python3
"""Test unconditional versions of the weighted product identities.

The tests are not restricted to counterexamples (which may not exist).
For arbitrary triples, use the covered divisor T of Q and prove/check the
weighted bound on T. For a hypothetical counterexample, T=Q by Kummer.
"""
from math import comb,gcd,isqrt,prod
from pathlib import Path
import json,random

ROOT=Path(__file__).resolve().parent

def primes(bound):
    return [p for p in range(2,bound) if all(p%d for d in range(2,isqrt(p)+1))]

def audit(n,i,j):
    h=i-1;b=(2*h+1)//3;a=h-b;d=2*b-a;S=b*(b+1)//2
    assert d>0
    Q=comb(n,i)
    for p in primes(i):
        while Q%p==0:Q//=p
    qs=[gcd(Q,n-s) for s in range(i)]
    assert prod(qs)==Q
    cells={(s,u):gcd(qs[s],j-u) for s in range(i) for u in range(s+1)}
    nonunit=[v for v in cells.values() if v>1]
    for k,x in enumerate(nonunit):
        assert all(gcd(x,y)==1 for y in nonunit[k+1:])
    T=prod(cells.values())
    assert Q%T==0
    columns=[prod(cells[s,u] for s in range(u,i)) for u in range(i)]
    diagonals=[prod(cells[s,s-v] for s in range(v,i)) for v in range(i)]
    assert all((j-u)%columns[u]==0 for u in range(i))
    assert all((n-j-v)%diagonals[v]==0 for v in range(i))
    M=(prod((n-s)**max(0,s-a) for s in range(i))
       *prod(((j-u)*(n-j-u))**max(0,b-u) for u in range(i)))
    assert M%T**d==0
    assert 4**S*T**d<=4**S*M<=n**(3*S)
    # Stronger unconditional count: all carried primes cannot be covered fully.
    B=comb(n,j)
    if gcd(Q,B)==1:assert T==Q
    return int(T>1),int(i in primes(i+1) and Q%i==0)

def main():
    count=nontrivial=prime_boundary=0
    for i in range(3,16):
        for n in range(2*i+2,101):
            for j in range(i+1,n//2+1):
                x,y=audit(n,i,j);count+=1;nontrivial+=x;prime_boundary+=y
    rng=random.Random(699095119)
    extra=[]
    for i in [95,99,103,107,119]:
        ns=[2*i+2,10*i+7,i*i,i*i+i-1]
        for n in ns:
            j=rng.randrange(i+1,n//2+1)
            x,y=audit(n,i,j);nontrivial+=x;prime_boundary+=y
            extra.append([n,i,j])
    result=dict(status='PASS',exhaustive_triples=count,
        nontrivial_covered_divisor_cases=nontrivial,
        prime_equals_i_active_cases=prime_boundary,
        target_index_boundary_cases=extra,
        note='Unconditional identities tested; infinite proof is in REPORT.md.')
    (ROOT/'cover_audit.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
