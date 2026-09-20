"""Symbolic checks for the structural identities introduced by the handoff."""
from repo_paths import artifact_path
from pathlib import Path
import json
import sympy as S


def main():
    n,j,d1,d2=S.symbols('n j d1 d2',nonzero=True)
    c=n/2-j;Q1=(n-1)/d1;Q=(n/2-1)/d2;c0=d1*d1*d2
    r=(4*c*c-1)/Q1;z=(r-d1)/2;w=((r+d1)*(r-3*d1))/(4*Q)
    identities=[z-(d1*n/2-2*d1*j*(n-j)/(n-1)),
                w-c0-(w*n/2-d2*z*z),
                4*c*c-n-2*Q1*z]
    gamma,T,x,Z,Cc,m,q,bg=S.symbols('gamma T x Z Cc m q bg',nonzero=True)
    # bg=2^(gap-3); n=8*gamma*T*bg*x^4.
    nn=8*gamma*T*bg*x**4;zz=2*T*x*x*Z;ww=c0+4*T*x**4*m
    identities.append((d2*zz**2-ww*nn/2+ww-c0)/(4*T*x**4)
                      -(d2*T*Z**2-gamma*c0*bg+m-4*T*m*gamma*bg*x**4))
    identities.append((4*(T*x*Cc)**2-nn-2*(nn-1)/d1*zz)*d1/(4*T*x*x)
                      -(d1*T*Cc**2-2*d1*gamma*bg*x*x-(nn-1)*Z))
    A,Bc,s=S.symbols('A Bc s',nonzero=True)
    delta=d1*d2;ab=(Bc*s-d1)/A**2
    ec=delta*A-2*s;fc=delta*Bc-2*A*ab;K=d2*A*Bc+1
    identities.append(A*(ec*fc-c0)-d1*K*(delta*A-4*s)-4*Bc*s*s)
    mm,tt,ZZ=S.symbols('mm tt ZZ',nonzero=True)
    XX=16*mm*tt*tt;YY=4*mm*tt*ZZ
    identities.append((YY*YY-XX**3-mm*(64-mm)*XX).subs(ZZ**2,256*mm*tt**4+64-mm))
    aa,bb,xx,yy=S.symbols('aa bb xx yy',nonzero=True)
    identities.append(((aa*xx*yy)**2-(aa*xx*xx)**3-aa*bb*(aa*xx*xx)).subs(yy**2,aa*xx**4+bb))
    for expression in identities:assert S.factor(expression)==0
    result={'status':'verified','symbolic_identities':len(identities),
            'scope':'algebra only; completeness and inequalities are proved separately'}
    artifact_path('verification_handoff_algebra.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':main()
