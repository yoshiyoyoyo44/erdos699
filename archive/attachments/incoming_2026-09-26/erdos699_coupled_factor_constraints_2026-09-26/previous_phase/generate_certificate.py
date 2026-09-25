#!/usr/bin/env python3
"""Generate exact constants and explicitly conditional index consequences."""
from math import lcm, isqrt
from fractions import Fraction
from pathlib import Path
import json
from digit_bridge import bridge_certificate

ROOT=Path(__file__).resolve().parent

def main():
    old=json.loads((ROOT/'previous_phase/certificate.json').read_text())
    primes=[p for p in range(2,120) if all(p%d for d in range(2,isqrt(p)+1))]
    rows=[]
    for row in old['rows']:
        i=row['i'];pi=row['pi'];epsilon=i if i in primes else 1
        cases=[]
        for t in row['thresholds']:
            B=t['B']
            D=pi+1+(pi+B)//B
            k=D-1
            C=epsilon*lcm(*range(1,k+1))
            assert D<=i and D-(D+B)//(B+1)>=pi+1
            assert 512**D>2*C*(i-1)**D
            cases.append(dict(n_power=t['n_power'],uses_a100=t['uses_a100'],
                excluded_denominator_B=B,D=D,prefix_last_row=k,row_constant=str(C)))
        rows.append(dict(i=i,pi=pi,prime_correction=epsilon,cases=cases))
    summary=[]
    for t in old['rows'][0]['thresholds']:
        selected=[(r['i'],x['D']) for r in rows for x in r['cases']
                  if (x['n_power'],x['uses_a100'])==(t['n_power'],t['uses_a100'])]
        maximum=max(d for _,d in selected)
        summary.append(dict(n_power=t['n_power'],uses_a100=t['uses_a100'],D_max=maximum,
            indices_at_max=[i for i,d in selected if d==maximum]))
    # These consequences use the attached index's unverified body-level inputs.
    filters=[]
    for m in range(1,25):
        allowed=[]
        for k in range(m+1):
            t=Fraction(k,m)
            lower=(145*m+8+191)//192
            if t==Fraction(1,2):lower=max(lower,5*m//6+1)
            if t in (Fraction(1,4),Fraction(3,4)):lower=max(lower,(79*m+95)//96)
            if t in (0,1):lower=max(lower,(11*m+11)//12)
            if lower<m:
                allowed.append(dict(t=str(t),r_min=lower))
        filters.append(dict(m=m,allowed=allowed,
            allowed_in_counterexample_orientation=[x for x in allowed if Fraction(x['t'])<=Fraction(1,2)]))
    examples=[]
    for k in (1,2,4,6,10):
        F=[0]*(2*k+1);J=[0]*(2*k+1)
        F[0]=2;F[k]=8;F[2*k]=12;J[k]=1;J[2*k]=6
        x=bridge_certificate(F,J)
        assert all(p['zero_remainder'] for p in x['parts'])
        examples.append(dict(F=F,J=J,**x))
    obj=dict(status='GENERATED',source_commit='f5a28d1037f35fdccc7a014e958db6fd666d220b',
        uniform_constant=512,rows=rows,summary=summary,
        conditional_index_filters=dict(status='PROVED-CONDITIONAL',
            reason='Three manuscript bodies named in the attachment were not accessible.',rows=filters),
        bridge_diagnostics=examples)
    (ROOT/'certificate.json').write_text(json.dumps(obj,indent=2)+'\n')
    print(json.dumps(summary,indent=2))

if __name__=='__main__':main()
