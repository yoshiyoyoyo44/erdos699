#!/usr/bin/env python3
"""Exact certificate generator; all thresholds are integer comparisons."""
from pathlib import Path
from math import factorial, gcd, prod, isqrt
import json

ROOT=Path(__file__).resolve().parent
SLOPES=[(1,2),(1,3),(1,4),(1,5),(2,5)]

def primes_to(n):
    sieve=bytearray(b'\1')*(n+1)
    sieve[:2]=b'\0\0'
    for p in range(2,isqrt(n)+1):
        if sieve[p]:sieve[p*p:n+1:p]=b'\0'*((n-p*p)//p+1)
    return [k for k in range(2,n+1) if sieve[k]]

def large_lcm_part(cap,i,ps):
    out=1
    for p in ps:
        if p<i:continue
        if p>cap:break
        q=p
        while q*p<=cap:q*=p
        out*=q
    return out

def main():
    ps=primes_to(590)
    rows=[];exceptions=[];comparisons=0
    for i in range(3,120):
        pi=sum(p<i for p in ps)
        small_i=i if i not in ps else 1
        f=factorial(i)//small_i
        row=dict(i=i,pi=pi,factorial_constant=str(f),slopes=[])
        for a,b in SLOPES:
            degree=b*(i-1)+1
            assert (7*b+1)*(i-pi)>=4*degree
            assert 10**degree>2**i*f
            N=200000000;cof=101**(pi-1)
            assert 4**degree*cof*(N-i+1)**i>f*N**i
            lo=-a*(i-1);hi=(b-a)*(i-1)
            delta_rows=[]
            for delta in range(lo,hi+1):
                resonant=[s for s in range(i) if (delta+a*s)%b==0 and 0<=(delta+a*s)//b<=s]
                e=len(resonant);gain=i-pi-e
                if gain<=0:
                    exceptions.append([i,a,b,delta]);continue
                cap=max(delta-lo,hi-delta)
                L=large_lcm_part(cap,i,ps)
                for N,cof in [(10**11,1),(200000000,101**(pi-1))]:
                    assert cof*(N-i+1)**i>f*N**(pi+e)*L,(i,a,b,delta,N)
                    comparisons+=1
                delta_rows.append(dict(delta=delta,resonant_count=e,large_lcm=str(L)))
            row['slopes'].append(dict(a=a,b=b,degree=degree,rows=delta_rows))
        rows.append(row)
    result=dict(source_commit='f5a28d1037f35fdccc7a014e958db6fd666d220b',
        i_range=[3,119],unresolved=[i for i in range(3,120) if i not in (96,97,100,101)],
        standalone=dict(n_min=10**11,constant_denominator=10),
        with_a100=dict(n_min=200000000,constant_denominator=4),
        exceptions=exceptions,integer_threshold_comparisons=comparisons,rows=rows)
    (ROOT/'certificate.json').write_text(json.dumps(result,separators=(',',':'))+'\n')
    print(json.dumps(dict(status='GENERATED',indices=len(rows),unresolved=len(result['unresolved']),
        slopes=len(SLOPES),finite_cells=sum(len(s['rows']) for r in rows for s in r['slopes']),
        comparisons=comparisons,exception_cases=exceptions),indent=2))

if __name__=='__main__':main()
