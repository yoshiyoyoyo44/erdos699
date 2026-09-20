"""Save complete residue/factorization coverage for gap layers 4 through 9."""
from repo_paths import artifact_path
import json
from pathlib import Path
from explore_gap_layers import rows, factor_bound, admissible_branch, local, PERIOD, MODULI


def main():
    result=[]
    for gap in range(4,10):
        for row in rows(gap):
            row=dict(row)
            vmin=max(2,(49-gap+3)//4)
            fb=factor_bound(row)
            if fb and fb[1]*16**vmin>fb[0]:
                row.update(method='factor',product_bound=fb[0])
            else:
                permitted={v%PERIOD for v in range(12,12+PERIOD)
                           if admissible_branch(row,v)}
                eliminated=[]
                for ell in MODULI:
                    rejected=sorted(v for v in permitted if not local(row,v,ell))
                    if rejected:
                        eliminated.append({'modulus':ell,'residues':rejected})
                        permitted-=set(rejected)
                if permitted:
                    assert gap==9 and (row['gamma'],row['d1'],row['d2'],row['T'])==(1,1,1,1)
                    assert row['m'] in (7,23,31,47)
                    row.update(method='elliptic',a4=row['m']*(64-row['m']),
                               surviving_residues=sorted(permitted))
                else:
                    row.update(method='modular')
                row['eliminations']=eliminated
            result.append(row)
    cert={'schema':1,'min_u':49,'gap_range':[4,9],'period':PERIOD,
          'moduli':MODULI,'cases':result}
    artifact_path('i3_gap_certificate.json').write_text(json.dumps(cert,indent=2)+'\n',encoding='utf-8')
    from collections import Counter
    print(len(result),'cases',dict(Counter(r['method'] for r in result)))


if __name__=='__main__':
    main()
