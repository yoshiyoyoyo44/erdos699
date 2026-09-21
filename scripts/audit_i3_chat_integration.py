"""Exact algebra and finite diagnostics for the four-chat integration.

These checks supplement the proofs in the note; diagnostics are not proofs
of the absence of counterexamples. External Thue-Mahler completeness is
deliberately handled separately.
"""
import json
from itertools import product
from math import gcd

import sympy as sp

from repo_paths import artifact_path
from replay_i3_cubic_discriminant_minima import disc, transform, MATRICES


def value(f, x, y):
    a, b, c, d = f
    return a*x**3+b*x*x*y+c*x*y*y+d*y**3


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    n, j, K, z = sp.symbols('n j K z', nonzero=True)
    y = n-j
    coeff = [j*(j-1)*(j-2), 3*j*(j-1)*y,
             3*j*y*(y-1), y*(y-1)*(y-2)]
    coeff = [c/(K*(n-1)*(n-2)) for c in coeff]
    P = sum(c*z**i for i, c in enumerate(coeff))
    delta = 108*j**2*y**2*(j-1)*(y-1)/(K**4*(n-1)**3*(n-2)**2)
    identities = {
        'value_at_one': P.subs(z, 1)-n/K,
        'derivative_at_one': sp.diff(P,z).subs(z,1)-3*y/K,
        'middle_sum': coeff[1]+coeff[2]-3*j*y/(K*(n-1)),
        'central_gap': P.subs(z,-1)+(n-2*j)*((n-2*j)**2-3*n+2)/(K*(n-1)*(n-2)),
        'discriminant': disc(tuple(reversed(coeff)))-delta,
    }
    X = sp.symbols('X')
    dX = 108*X**2*(X-n+1)/(K**4*(n-1)**3*(n-2)**2)
    identities['integer_middle_bound'] = dX.subs(X,n*(n-1)/4)-27*n**2*(n-4)/(16*K**4*(n-2)**2)
    identities['strict_upper_gap'] = 27*n/(16*K**4)-dX.subs(X,n*(n-1)/4)-27*n/(4*K**4*(n-2)**2)
    eps,k,a,e,L,q = sp.symbols('eps k a e L q', nonzero=True)
    nc=2*eps*k*a; jc=k*(eps*a-e); yc=k*(eps*a+e); Lc=eps*k*a-1
    cc=[sp.factor(c.subs({n:nc,j:jc,K:eps*k})) for c in coeff]
    qc=3*k*(eps**2*a*a-e*e)/(eps*(2*Lc+1))
    identities['corrected_c1'] = cc[1]-qc*(Lc-k*e)/(2*Lc)
    identities['corrected_c2'] = cc[2]-qc*(Lc+k*e)/(2*Lc)
    identities['endpoint_difference'] = cc[3]-cc[0]-(6*e/eps-qc*k*e/Lc)/3
    g,ell,t,s,W=sp.symbols('g ell t s W', nonzero=True)
    nn=2*(g*ell+1); jj=1+g*(ell-k*t)
    ss=3*jj*(nn-jj)/(eps*k*k*ell*(2*g*ell+1))
    ww=3*(ell*ell-k*k*t*t)/(2*g*ell+1)
    identities['integer_system_first'] = g*g*ww+3-eps*k*k*ell*ss
    identities['integer_system_discriminant'] = delta.subs({n:nn,j:jj,K:eps*k})-ss*ss*ww/eps**2
    b,A=sp.symbols('b A')
    S=-n*(n-1)*(n-2)*A**3+3*j*(n-1)*(n-2)*A*A*b-3*j*(j-1)*(n-2)*A*b*b+j*(j-1)*(j-2)*b**3
    identities['neighbor_rational_gap'] = S.subs({A:j-1,b:n})-n*(j-1)*(4*j*j-3*j*n-2*j-n*n+3*n-2)
    aq,dq,N=sp.symbols('aq dq N')
    bq=(aq-dq)/2; cq=(aq+dq)/2
    identities['kummer_R_quotient'] = 2*bq*cq*(aq+bq)-(aq*aq-dq*dq)*(3*aq-dq)/4
    identities['kummer_S_quotient'] = 2*bq*cq*(aq+cq)-(aq*aq-dq*dq)*(3*aq+dq)/4
    for name, expr in identities.items():
        assert sp.cancel(expr)==0, name

    # Arbitrary diagnostic cubics with a simple root at [1:0].
    # The proof of primitiveness and exponent transport is in the note.
    transported=0
    for aa,bb,cc0,dd0 in product(range(-2,3),range(-3,4,2),range(-2,3),range(-2,3)):
        f=(2*aa,bb,4*cc0,4*dd0)
        ft=(4*aa,bb,2*cc0,dd0)
        assert 4*disc(ft)==disc(f)
        for x,y0 in ((1,0),(1,2),(3,2),(5,-2)):
            assert gcd(x,2*y0)==1
            assert value(ft,x,2*y0)==2*value(f,x,y0)
            assert (bb*x*x+2*(2*cc0)*x*(2*y0)+3*dd0*(2*y0)**2)%2==1
            transported+=1
    # GL2(Z) coordinate transport used before each lowering.
    for matrix in MATRICES:
        p,q0,r,s0=matrix; det=p*s0-q0*r
        f=(2,1,4,8); pt=(3,2)
        invpt=((s0*pt[0]-q0*pt[1])//det,(-r*pt[0]+p*pt[1])//det)
        assert value(transform(f,matrix),*invpt)==value(f,*pt)
        assert gcd(*invpt)==1
    # The rational maximum needed by the w bound: f(x)<=5/6 is sharpened
    # enough to absorb (n-1)(n-2)/n^2 for n>=1000.
    xx=sp.symbols('xx')
    critical=(3+sp.sqrt(21))/12
    maximum=sp.simplify((xx+3*xx**2-4*xx**3).subs(xx,critical))
    assert maximum < sp.Rational(33,40)
    assert sp.Rational(33,40)*1000**2/(999*998) < sp.Rational(5,6)
    result={'status':'passed','symbolic_identities':list(identities),
            'marked_point_diagnostics':transported,'coordinate_transports':len(MATRICES),
            'interval_polynomial_maximum':str(maximum),
            'scope':'Algebra and diagnostics; see note for all-range proofs.'}
    artifact_path('verification_i3_chat_integration.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,indent=2))


if __name__=='__main__':
    main()
