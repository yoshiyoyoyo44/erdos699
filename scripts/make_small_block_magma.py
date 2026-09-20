"""Generate elliptic-curve audits for a fixed A, B, or C block.

For C=5,7,9 the inequality delta1*delta2*C > 4*T gives very few T.
This script constructs necessary square equations, never sufficient conditions.
"""
from repo_paths import artifact_path
import argparse
import json
from math import gcd, isqrt
from pathlib import Path


def cases_for(C, role='C'):
    rows=[]
    for gamma,d1,d2 in [(1,1,1),(1,1,3),(1,3,1),(3,1,1)]:
        K=d1*d2*C
        if gcd(C,gamma*d1*d2)!=1:
            continue
        if role == 'C':
            parameters = [(r,T) for r in range(1,(K-1)//4+1)
                          for T in range(1,r+1,2) if r%T==0]
        elif role == 'B':
            parameters = [(r,T) for r in range(K//4+1,K)
                          for T in range(1,r+1,2) if r%T==0]
        else:
            # r = T^2*g*h; v2(g)=v2(h), so v2(g*h) is even.
            parameters = [(r,T) for r in range(1,(K-1)//2+1)
                          for T in range(1,isqrt(r)+1,2)
                          if r%(T*T)==0 and ((r & -r).bit_length()-1)%2==0]
        for r,T in parameters:
            if gcd(T,C*d1*d2)!=1:
                continue
            if T%3==0 and (gamma==3 or T%9!=0):
                continue
            for parity in (0,1):
                D=gamma*T*2**parity
                # Existence of the required delta pair is periodic mod 6.
                possible=False
                for u in range(6+parity,12,2):
                    n=gamma*T*2**u
                    e1=3 if (n-1)%3==0 and (n-1)%9 else 1
                    e2=3 if (n//2-1)%3==0 and (n//2-1)%9 else 1
                    possible |= (e1,e2)==(d1,d2)
                if not possible:
                    continue
                if role == 'A':
                    Kcurve=2*K
                    aa,bb,cc=Kcurve*(Kcurve-4*r)*D*D,12*Kcurve*r*D,-8*Kcurve*r
                else:
                    aa,bb,cc=4*K*r*D*D,-12*K*r*D,K*K+8*K*r
                rows.append(dict(**{role:C},gamma=gamma,delta1=d1,delta2=d2,T=T,
                                 r=r,parity=parity,D=D,K=K,
                                 quartic=[aa,0,bb,0,cc]))
    return rows


def main():
    parser=argparse.ArgumentParser()
    parser.add_argument('--C',type=int,default=5)
    parser.add_argument('--role', choices=['A','B','C'], default='C')
    parser.add_argument('--value', type=int)
    parser.add_argument('--modular', action='store_true', help='Use saved periodic congruence certificates for B')
    args=parser.parse_args()
    value=args.C if args.value is None else args.value
    role=args.role
    rows=cases_for(value,role)
    modular=(json.loads(artifact_path('fixed_block_modular_exclusions.json').read_text()).get(f'{role}{value}',{})
             if args.modular else {})
    artifact_path(f'small_{role}{value}_cases.json').write_text(json.dumps(rows,indent=2)+'\n',encoding='utf-8')
    lines=['// Complete integer-point audit for NECESSARY equations at a fixed block.',
           '// No GRH class-group option is enabled; default proof is unconditional.',
           'SetSeed(699);']
    for i,row in enumerate(rows):
        aa,_,bb,_,cc=row['quartic']
        lines += [f'print "CASE_{i}", {value};', f'aa:={aa}; bb:={bb}; cc:={cc};']
        if role=='B':
            T,K,r,d1=row['T'],row['K'],row['r'],row['delta1']
            lines += [f'TT:={T}; KK:={K}; rr:={r}; dd:={d1}; FF:={value};',
                      'options:=[];',
                      'for b0 in Divisors(2*rr div TT) do',
                      ' h0:=(2*rr div TT) div b0;',
                      ' vv:=Valuation(h0,2);',
                      ' need:=dd*(vv eq 0 select 0 else (vv eq 1 select 3 else -1));',
                      ' for a0 in Divisors(2*(KK-rr)) do',
                      '  z0:=2*(KK-rr) div a0;',
                      '  if (a0+h0) mod 2 eq 1 and (b0+h0) mod 2 eq 1 and',
                      '     (z0-h0) mod 2 eq 0 and (a0*b0-need) mod 8 eq 0 and',
                      '     exists{x0:x0 in [0..TT^2*FF-1] | (a0*b0*x0^2+dd) mod (TT^2*FF) eq 0} then',
                      '    Append(~options,<a0,b0,h0,z0>);',
                      '  end if;',
                      ' end for;',
                      'end for;',
                      'print "BOUNDARY_OPTIONS",options;']
            if str(i) in modular:
                cert=modular[str(i)]
                period,mods=cert['period'],cert['moduli']
                D=row['D']
                d2=row['delta2']
                lines += [f'period:={period}; moduli:=[Integers()|'+','.join(map(str,mods))+'];',
                          f'assert 4^period mod 9 eq 1 and 4^period mod {d2*value} eq 1;',
                          'ex3:=func<zz | zz mod 3 eq 0 and zz mod 9 ne 0 select 3 else 1>;',
                          f'residues:=[mm:mm in [0..period-1] | ({D}*4^mm-2) mod {d2*value} eq 0 and',
                          f' ex3({D}*4^mm-1) eq {d1} and ex3(5*{D}*4^mm-1) eq {d2}];',
                          'for modulus in moduli do',
                          ' assert 4^period mod modulus eq 1;',
                          ' squares:={xx^2 mod modulus:xx in [0..modulus-1]};',
                          ' residues:=[mm:mm in residues | (aa*4^(2*mm)+bb*4^mm+cc) mod modulus in squares];',
                          'end for;',
                          'assert #residues eq 0;',
                          'print "MODULAR_CERT",period,moduli;',
                          'print "MODULAR_EXCLUSION";']
            lines += [('if true then' if str(i) in modular else 'if #options eq 0 then'),
                      ' print "ARITHMETIC_EXCLUSION";',
                      'else']
        lines += [
                  'E:=EllipticCurve([0,bb,0,aa*cc,0]);',
                  'G,mp,rank_proved,group_proved:=MordellWeilGroup(E);',
                  'print "PROOF_FLAGS",rank_proved,group_proved;',
                  'assert rank_proved and group_proved;',
                  'basis:=[mp(G.i):i in [1..Ngens(G)] | Order(G.i) eq 0];',
                  'print "FREE_BASIS",basis;',
                  'points:=IntegralPoints(E:FBasis:=basis,SafetyFactor:=2);',
                  'print "INTEGRAL_POINTS",points;',
                  'ts:={};',
                  'for P in points do',
                  '  xx:=Integers()!P[1];',
                  '  if xx gt 0 and xx mod aa eq 0 then',
                  '    square,t:=IsSquare(xx div aa);',
                  '    if square and t gt 0 then',
                  '      yy:=P[2]/(aa*t);',
                  '      if Denominator(yy) eq 1 then',
                  '        assert yy^2 eq aa*t^4+bb*t^2+cc;',
                  '        Include(~ts,t);',
                  '      end if;',
                  '    end if;',
                  '  end if;',
                  'end for;',
                  'print "POSITIVE_T",ts;',
                  f'assert not exists{{t:t in ts | t eq 2^Valuation(t,2) and 2*Valuation(t,2)+{row["parity"]} ge 49}};']
        if role=='B':
            lines += ['end if;']
        lines += [f'print "CASE_{i}_COMPLETE";']
    lines.append(f'print "SMALL_{role}{value}_COMPLETE";')
    artifact_path(f'i3_small_{role}{value}.magma').write_text('\n'.join(lines)+'\n',encoding='utf-8')
    print(json.dumps(dict(role=role,value=value,cases=len(rows))))


if __name__=='__main__':
    main()
