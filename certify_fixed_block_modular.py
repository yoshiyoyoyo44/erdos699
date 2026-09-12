"""Generate finite periodic obstructions for fixed B and all exponents u.

No primality claim is needed: all square residues modulo each odd modulus are
enumerated. The full exponent period is certified by modular exponentiation.
"""
import json
from math import lcm
from pathlib import Path


def delta(x):
    return 3 if x%3==0 and x%9 else 1


def main():
    period=2520
    candidates=[(q,{x*x%q for x in range(q)}) for q in range(3,500,2)
                if pow(4,period,q)==1]
    out={}
    for F in (5,7,9):
        rows=json.loads(Path(f'small_B{F}_cases.json').read_text())
        exclusions={}
        for i,row in enumerate(rows):
            a,_,b,_,c=row['quartic']
            D,d1,d2=row['D'],row['delta1'],row['delta2']
            assert pow(4,period,lcm(9,d2*F))==1
            alive={m for m in range(period)
                   if (D*pow(4,m,d2*F)-2)%(d2*F)==0
                   and delta(D*pow(4,m,9)-1)==d1
                   and delta(5*D*pow(4,m,9)-1)==d2}
            used=[]
            for modulus,squares in candidates:
                if not alive:
                    break
                reduced={m for m in alive
                         if (a*pow(4,2*m,modulus)+b*pow(4,m,modulus)+c)%modulus in squares}
                if len(reduced)<len(alive):
                    used.append(modulus)
                    alive=reduced
            if not alive:
                exclusions[str(i)]={'period':period,'moduli':used}
        out[f'B{F}']=exclusions
        print(f'B={F}: {len(exclusions)}/{len(rows)} excluded by periodic congruences')
    Path('fixed_block_modular_exclusions.json').write_text(json.dumps(out,indent=2)+'\n',encoding='utf-8')


if __name__=='__main__':
    main()
