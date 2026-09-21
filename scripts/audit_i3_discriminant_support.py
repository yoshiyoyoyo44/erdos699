"""Elliptic j-invariant gap and unbounded-exponent support exclusions.

The exact algebra and table-row checks are local. Completeness of elliptic
curve lists is external: von Kaenel--Matschke, arXiv:1605.06079, Section 4.2.5,
Algorithm 4.6 and its applications. We do not rerun Tate's algorithm or their
Mordell-Weil computations. Raw sources are stored losslessly in gzip files.
"""
import gzip
import hashlib
import json
import re
from fractions import Fraction
from math import gcd, isqrt, prod

import sympy as sp

from repo_paths import ROOT, artifact_path


SOURCES = (
    {'file': 'curves__S_2_3_5_7_11.txt.gz',
     'url': 'https://www.math.u-bordeaux.fr/~bmatschke/data/curves__S_2_3_5_7_11.txt',
     'raw_sha256': 'ca59125f39550b71d0a633cd6cd4414df1beef4d7522b3236cdb5176cdabecd9',
     'rows': 592192, 'sets': 1, 'minimum_gap': Fraction(59643, 1826132)},
    {'file': 'curves_maxNS_1000.txt.gz',
     'url': 'https://www.math.u-bordeaux.fr/~bmatschke/data/curves_maxNS_1000.txt',
     'raw_sha256': '18e4efa02d1b8b11f91b0588455caa78e109127a90bfb4934fb62bbd9625473c',
     'rows': 1221342, 'sets': 607, 'minimum_gap': Fraction(4892187, 1740800000)},
)


def symbolic_checks():
    n,j,K,x=sp.symbols('n j K x', nonzero=True)
    y=n-j; N=n/K
    A=3*y/K; B=3*y*(y-1)/(K*(n-1))
    C=y*(y-1)*(y-2)/(K*(n-1)*(n-2))
    H=9*j*y/(K*K*(n-1))
    J=-54*j*y*(n-2*j)/(K**3*(n-1)*(n-2))
    delta=108*j*j*y*y*(j-1)*(y-1)/(K**4*(n-1)**3*(n-2)**2)
    ji=1728*j*y*(n-2)**2/(n*n*(j-1)*(y-1))
    checks={
        'H_at_marked_point': A*A-3*N*B-H,
        'J_at_marked_point': 2*A**3-9*N*A*B+27*N*N*C-J,
        'syzygy': 4*H**3-J**2-27*N*N*delta,
        'elliptic_discriminant': 16*sp.discriminant(x**3+A*x*x+N*B*x+N*N*C,x)-16*N*N*delta,
        'elliptic_j': 256*H**3/(N*N*delta)-ji,
        'j_gap': ji-1728-1728*(n-1)*(n-2*j)**2/(n*n*(j-1)*(y-1)),
    }
    # The integer system in the preceding note gives a stronger exact norm
    # identity, rather than just its earlier low-precision congruence.
    eps,g,ell,k,t=sp.symbols('eps g ell k t', nonzero=True)
    nn=2*(g*ell+1); jj=1+g*(ell-k*t)
    ss=3*jj*(nn-jj)/(eps*k*k*ell*(2*g*ell+1))
    ww=3*(ell*ell-k*k*t*t)/(2*g*ell+1)
    aa=(g*ell+1)/(eps*k)
    checks['norm_identity']=eps*ell**3*ss-3*t*t-eps*eps*ww*aa*aa
    # An explicit sign twist followed by scaling gives an integral model
    # with c4 odd, hence minimal at 2. N is divisible by 2^42 in our use.
    AA,BB,CC,NN=sp.symbols('AA BB CC NN')
    for sig in (1,-1):
        a2=(sig*AA-1)/4; a4=NN*BB/16; a6=sig*NN*NN*CC/64
        b2=1+4*a2; b4=2*a4; b6=4*a6; b8=a6+4*a2*a6-a4*a4
        c4=b2*b2-24*b4
        c6=-b2**3+36*b2*b4-216*b6
        de=-b2*b2*b8-8*b4**3-27*b6*b6+9*b2*b4*b6
        cubic_delta=sp.discriminant(CC*x**3+BB*x*x+AA*x+NN,x)
        checks[f'minimal_at_2_c4_{sig}']=c4-(AA*AA-3*NN*BB)
        checks[f'minimal_at_2_c6_{sig}']=c6+sig*(2*AA**3-9*NN*AA*BB+27*NN*NN*CC)/2
        checks[f'minimal_at_2_discriminant_{sig}']=de-NN*NN*cubic_delta/256
    # Invariants of the marked cubic stay fixed during a dyadic lowering.
    a,b,c,d,X,Y=sp.symbols('a b c d X Y')
    def Hess(f):
        a,b,c,d=f
        return (b*b-3*a*c)*X*X+(b*c-9*a*d)*X*Y+(c*c-3*b*d)*Y*Y
    f=(a,b,c,d); ft=(2*a,b,c/2,d/4)
    checks['marked_H_descent']=Hess(ft).subs(Y,2*Y)-Hess(f)
    for name, expression in checks.items():
        assert sp.cancel(expression)==0, name
    # n >= 2^51 and c0 >= 1 force the integer index j >= 2^34.
    assert (2**34-1)**3 < (2**51-1)*(2**51-2)
    return list(checks)


def local_diagnostics():
    # Samples of the integer system (no claim that these are counterexamples).
    # Check gcd(W,s) and gcd(W,ell) at every prime >=5.
    cases=0
    for g in range(1,51,2):
        for ell in range(1,61,2):
            for t in range(1,ell,2):
                if gcd(ell,t)!=1:
                    continue
                for k in (1,2,3,4,5):
                    if k*t>=ell or gcd(k,ell)!=1:
                        continue
                    W=Fraction(3*(ell*ell-k*k*t*t),2*g*ell+1)
                    if W.denominator!=1:
                        continue
                    W=int(W)
                    for eps in (1,3):
                        ss=Fraction(g*g*W+3,eps*k*k*ell)
                        if ss.denominator!=1 or ss.numerator%2==0:
                            continue
                        ss=int(ss);cases+=1
                        for shared in (gcd(W,ss),gcd(W,ell)):
                            while shared%2==0:shared//=2
                            while shared%3==0:shared//=3
                            assert shared==1
    # Exact local valuation calculation in characteristic >=5.
    valuations=0
    for m in range(1,301):
        for ell_order in range(0,15):
            q=m//6
            assert m+ell_order>=4*q and m>=6*q
            assert not (m+ell_order>=4*(q+1) and m>=6*(q+1))
            assert 2*m-12*q==2*(m%6)
            valuations+=1
    assert cases>0
    return {'integer_system_diagnostics':cases,'odd_prime_valuation_diagnostics':valuations}


def squarefree_support(n):
    factors=[]; p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0:
                return None
            factors.append(p)
        p+=1
    if n>1:
        factors.append(n)
    return tuple(factors)


def growth_bound_checks():
    # Corollary 6.2 of arXiv:1310.7263v2 is an external theorem, not
    # established by these checks. The note derives the universal bound
    # and monotonicity; here we check its explicit threshold exactly.
    ratio = Fraction(972*900, 2**20) + Fraction(124, 2**40)
    assert ratio < 1
    assert Fraction(1, 30) < Fraction(1, 3)  # logarithmic derivative < 0
    assert 486 < 2**9
    return {
        'external_theorem': 'https://arxiv.org/html/1310.7263v2#S6.SS1, Corollary 6.2',
        'theorem': 'log(abs(Delta_min)) <= 3*N_E*(log(N_E))^2 + 124',
        'derived_integer_bound': 'u <= 972*Q*bit_length(486*Q)^2 + 124; Q=R_W*R_s^2',
        'slow_growth_exclusion': 'Q=o(u/(log(u))^2) is impossible along counterexamples with u tending to infinity',
        'explicit_threshold': 'u>=2^40 implies R>u^(1/4)',
        'threshold_ratio_exact': str(ratio),
        'scope': 'Only the explicit constant and slope comparisons are checked here; the general proof is in Section 6.3 of the note.',
    }


def bounds(gap):
    bound=1+Fraction(1728,1)/gap  # j < bound, strictly
    jmax=(bound.numerator-1)//bound.denominator
    nmax=2+isqrt(jmax**3-1)  # (n-2)^2 < j^3
    return {'j_strict_upper':str(bound),'j_max':jmax,'n_max':nmax}


def audit_table(source):
    path=ROOT/'sources'/source['file']
    compressed=path.read_bytes();raw=gzip.decompress(compressed)
    assert hashlib.sha256(raw).hexdigest()==source['raw_sha256']
    per_set={}; rows=0; global_min=None; global_witness=None; header_count=None
    active=None; distinct_pairs=set(); max_v2=-1; max_v2_witness=None; minimal2_rows=0
    for line in raw.decode('utf-8').splitlines():
        m=re.search(r'S = \{([\d, ]+)\}',line)
        if m:
            active=tuple(map(int,m[1].split(',')))
            assert tuple(sorted(set(active)))==active
            for p in active:
                assert p>=2 and all(p%d for d in range(2,isqrt(p)+1))
            assert active not in per_set
            per_set[active]={'rows':0,'positive_nonzero_c6':0,'minimum':None}
        elif line.startswith('# It contains '):
            header_count=int(re.search(r'contains (\d+)',line)[1])
        elif line.startswith('('):
            assert active is not None
            m=re.fullmatch(r'\((-?\d+),(-?\d+)\)',line)
            assert m, line
            c4,c6=map(int,m.groups())
            distinct_pairs.add((c4,c6))
            difference=c4**3-c6*c6
            assert difference and difference%1728==0
            discriminant=difference//1728
            remaining=abs(discriminant)
            for p in active:
                while remaining%p==0:
                    remaining//=p
            assert remaining==1, (active,c4,c6,discriminant)
            rows+=1; row=per_set[active];row['rows']+=1
            if discriminant>0 and c4%2:
                minimal2_rows+=1
                order=(discriminant&-discriminant).bit_length()-1
                if order>max_v2:
                    max_v2=order
                    max_v2_witness={'S':active,'c4':c4,'c6':c6,'discriminant':discriminant}
            if discriminant>0 and c6!=0:
                # j(E)-1728 = c6^2/Delta_min, with no floating point.
                gap=Fraction(c6*c6,discriminant)
                row['positive_nonzero_c6']+=1
                if row['minimum'] is None or gap<row['minimum']:
                    row['minimum']=gap
                if global_min is None or gap<global_min:
                    global_min=gap
                    global_witness={'S':active,'c4':c4,'c6':c6,'discriminant':discriminant}
    assert rows==source['rows'] and len(per_set)==source['sets']
    assert len(distinct_pairs)==header_count
    assert global_min==source['minimum_gap']
    assert max_v2==(48 if source['sets']==1 else 51)
    assert max_v2<76
    if source['sets']==1:
        assert set(per_set)=={(2,3,5,7,11)}
    else:
        expected={squarefree_support(m) for m in range(2,1001)}-{None}
        assert set(per_set)==expected
        assert all(prod(S)<=1000 for S in per_set)
    max_bounds=bounds(global_min)
    assert max_bounds['n_max']<2**51
    assert global_min>Fraction(1728,2**34-1)
    return {
        'source':source['url'],'file':source['file'],
        'raw_sha256':source['raw_sha256'],
        'gzip_sha256':hashlib.sha256(compressed).hexdigest(),
        'license':'CC BY-NC 3.0, Rafael von Kaenel and Benjamin Matschke (2015)',
        'raw_bytes':len(raw),'gzip_bytes':len(compressed),
        'header_claimed_rows':header_count,'rows_recounted_and_checked':rows,
        'distinct_pairs_checked':len(distinct_pairs),
        'sets_checked':len(per_set),'minimum_gap':str(global_min),
        'minimum_witness':global_witness,**max_bounds,
        'odd_c4_positive_discriminant_rows':minimal2_rows,
        'maximum_minimal_discriminant_v2':max_v2,'maximum_v2_witness':max_v2_witness,
        'odd_index_u_max':(max_v2+5)//2,
        'even_index_u_max':(2*max_v2+2)//3,
        'per_set':[{'S':S,**{key:val for key,val in data.items() if key!='minimum'},
                    'minimum_gap':str(data['minimum']) if data['minimum'] is not None else None}
                   for S,data in sorted(per_set.items())],
    }


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    algebra=symbolic_checks()
    diagnostics=local_diagnostics()
    tables=[]
    for source in SOURCES:
        row=audit_table(source);tables.append(row)
        print(json.dumps({key:val for key,val in row.items() if key!='per_set'},indent=2),flush=True)
    result={
        'status':'passed','symbolic_identities':algebra,'diagnostics':diagnostics,'tables':tables,
        'growth_bound':growth_bound_checks(),
        'external_completeness':'vKM Section 4.2.5 / Algorithm 4.6 and published full curve lists; not independently rerun',
        'conclusions':[
            'Any fixed finite odd-prime support of terminal discriminant gives finitely many counterexample candidates (Shafarevich plus j gap).',
            'A counterexample has an odd prime divisor >=13 in the terminal discriminant, regardless of prime exponents.',
            'The product of distinct odd primes in the terminal discriminant is >500, regardless of prime exponents.',
            'Let s6 be the sixth-power-free part of s. A counterexample has rad_{p>=5}(W*s6)>166 and this support contains a prime >=13. Primes with v_p(s) divisible by 6 may be arbitrarily large.',
        ],
        'remaining':'No uniform bound on the varying prime support; i=3 remains unresolved.',
    }
    artifact_path('verification_i3_discriminant_support.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','symbolic_identities':len(algebra),
                      'curve_rows_checked':sum(t['rows_recounted_and_checked'] for t in tables),
                      'output':'data/results/verification_i3_discriminant_support.json'},indent=2))


if __name__=='__main__':
    main()
