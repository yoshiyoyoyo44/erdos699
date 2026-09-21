"""Audit the auxiliary Frey curve for growing G and its support exclusions.

General algebra and inequalities are proved in the research note. This audit
replays exact curve-table filters and every surviving gap-sum case. Completeness
of the published tables and the conductor-height theorem are external inputs.
"""
import gzip
import hashlib
import json
import re
from fractions import Fraction
from math import gcd, isqrt

import sympy as sp

from audit_i3_discriminant_support import SOURCES, squarefree_support
from repo_paths import ROOT, artifact_path


def symbolic_checks():
    a, b, X, Y = sp.symbols('a b X Y')
    c = a+b
    H = a*a+a*b+b*b
    checks = {'positive_product_bound': a*b-(c-1)-(a-1)*(b-1)}
    for sig in (1, -1):
        A = a+c
        a2 = (sig*A-1)/4
        a4 = a*c/16
        b2 = 1+4*a2
        b4 = 2*a4
        b8 = -a4*a4
        c4 = b2*b2-24*b4
        c6 = -b2**3+36*b2*b4
        delta = -b2*b2*b8-8*b4**3
        checks[f'c4_{sig}'] = c4-H
        checks[f'c6_{sig}'] = c6-sig*(a-b)*(2*a+b)*(a+2*b)/2
        checks[f'discriminant_{sig}'] = delta-(a*b*c)**2/256
        roots = [sig*(2*a+b), sig*(b-a), -sig*(a+2*b)]
        checks[f'two_torsion_roots_{sig}'] = (
            sp.prod(X-r for r in roots)-(X**3-3*c4*X-2*c6))
        # Shift by a, sign-twist, then X_old=4X, Y_old=8Y+4X.
        old = (8*Y+4*X)**2-(4*X)*((4*X)+sig*a)*((4*X)+sig*c)
        new = Y*Y+X*Y-X**3-a2*X*X-a4*X
        checks[f'integral_model_{sig}'] = old-64*new
    # At an odd prime dividing exactly one of a,b,c, c4 is a unit.
    checks['c4_mod_a'] = H.subs(a,0)-b*b
    checks['c4_mod_b'] = H.subs(b,0)-a*a
    checks['c4_mod_c'] = H.subs(b,-a)-a*a
    for name, expression in checks.items():
        assert sp.expand(expression) == 0, name
    return list(checks)


def curve_diagnostics():
    count = 0
    for k in range(11, 18):
        for r in range(3):
            c = 3**r*2**k
            for a in range(1, 302, 2):
                b = c-a
                if gcd(a,b) != 1:
                    continue
                sig = 1 if (2*a+b)%4 == 1 else -1
                assert (sig*(2*a+b)-1)%4 == 0 and a*c%16 == 0
                c4 = a*a+a*b+b*b
                c6 = sig*(a-b)*(2*a+b)*(a+2*b)//2
                delta = (a*b*c//16)**2
                assert c4**3-c6*c6 == 1728*delta
                assert gcd(c4, a*b*c) == 1
                assert (delta & -delta).bit_length()-1 == 2*k-8
                assert gcd(3*a, 3*b) == 3
                count += 1
    return {'synthetic_coprime_sum_curves':count,
            'scope':'Diagnostics of Frey models, not examples of problem-699 counterexamples.'}


def table_checks(source):
    raw = gzip.decompress((ROOT/'sources'/source['file']).read_bytes())
    assert hashlib.sha256(raw).hexdigest() == source['raw_sha256']
    candidates = {}
    row_count = square_rows = 0
    sets = set()
    for line in raw.decode('utf-8').splitlines():
        match = re.search(r'S = \{([\d, ]+)\}', line)
        if match:
            support = tuple(map(int, match[1].split(',')))
            sets.add(support)
        if not line.startswith('('):
            continue
        match = re.fullmatch(r'\((-?\d+),(-?\d+)\)', line)
        assert match
        c4, c6 = map(int, match.groups())
        row_count += 1
        difference = c4**3-c6*c6
        assert difference != 0 and difference%1728 == 0
        if c4%2 == 0:
            continue
        delta = difference//1728
        if delta <= 0 or isqrt(delta)**2 != delta:
            continue
        square_rows += 1
        order = (delta & -delta).bit_length()-1
        if order >= 14:
            candidates.setdefault((c4,c6), (order,support,delta))
    assert row_count == source['rows'] and len(sets) == source['sets']
    if len(sets) == 1:
        assert sets == {(2,3,5,7,11)}
    else:
        assert sets == {squarefree_support(m) for m in range(2,1001)}-{None}
    X = sp.Symbol('X')
    certificates = []
    passed = []
    normalized = set()
    primes = tuple(sp.primerange(2, 200))
    for (c4,c6),(order,support,delta) in sorted(candidates.items()):
        row = {'c4':c4,'c6':c6,'delta':delta,'v2_delta':order,'S':support}
        # A rational root of this monic integer cubic is integral. A prime
        # with no modular root therefore certifies failure of full 2-torsion.
        prime = next((p for p in primes
                      if all((z**3-3*c4*z-2*c6)%p for z in range(p))), None)
        if prime is not None:
            row.update({'reason':'no rational root','no_root_modulus':prime})
            certificates.append(row)
            continue
        roots = sp.polys.polytools.ground_roots(X**3-3*c4*X-2*c6, X)
        assert len(roots) == 3 and all(m == 1 for m in roots.values())
        assert all(root.is_Integer for root in roots)
        roots = sorted(map(int, roots))
        assert sp.expand(sp.prod(X-r for r in roots)-(X**3-3*c4*X-2*c6)) == 0
        v,w = roots[1]-roots[0], roots[2]-roots[1]
        divisor = gcd(v,w)
        a,b = sorted((v//divisor, w//divisor))
        c = a+b
        normalized.add((order,a,b,c))
        row.update({'roots':roots,'root_gap_gcd':divisor,'normalized_abc':[a,b,c]})
        if divisor != 3:
            row['reason'] = 'not the coprime semistable gap model'
        elif c%2:
            row['reason'] = 'the largest root gap is odd'
        elif c//(c & -c) not in (1,3,9):
            row['reason'] = 'the even sum has wrong odd part'
        else:
            k = (c & -c).bit_length()-1
            assert order == 2*k-8
            row.update({'reason':'gap-sum candidate','G':k+3})
            passed.append({'G':k+3,'a':a,'b':b,'c':c,'c4':c4,'c6':c6})
        certificates.append(row)
    expected = ([(17,49,16335,16384)] if len(sets)==1 else
                [(14,23,2025,2048),(14,243,1805,2048)])
    assert sorted((z['G'],z['a'],z['b'],z['c']) for z in passed) == expected
    return {'file':source['file'],'source':source['url'],
            'raw_sha256':source['raw_sha256'],'rows_checked':row_count,
            'sets_checked':len(sets),'odd_c4_positive_square_delta_rows':square_rows,
            'distinct_high_valuation_candidates':len(candidates),
            'modular_nonsplitting_certificates':sum('no_root_modulus' in z for z in certificates),
            'normalized_split_triples':sorted(normalized),
            'gap_sum_candidates':passed,'certificates':certificates}


def finish_cases(tables):
    branches = ((1,1,1),(1,1,3),(1,3,1),(3,1,1))
    triples = {(z['G'],z['a'],z['b'],z['c'])
               for table in tables for z in table['gap_sum_candidates']}
    exclusions = []
    survivors = []
    for G,a,b,c in sorted(triples):
        assert c == 2**(G-3)  # Hence d = gamma*c0 in these remaining cases.
        v_min = (51-G+3)//4
        assert v_min >= 2
        for gamma,d1,d2 in branches:
            c0 = d1*d1*d2
            d = gamma*c0
            for beta,alpha in ((a,b),(b,a)):
                for T in range(1,isqrt(beta)+1,2):
                    if beta%(T*T):
                        continue
                    m = d*alpha
                    q = d*beta//T
                    row = {'G':G,'gamma':gamma,'delta1':d1,'delta2':d2,
                           'T':T,'m':m,'q':q,'v_min':v_min}
                    if gcd(T,gamma*d1*d2) != 1:
                        row['reason'] = 'T is not coprime to the branch constants'
                    elif (q-c0*T*T)%16:
                        row['reason'] = 'q is not c0*T^2 modulo 16'
                    else:
                        # The two center equations imply Y^2=A*16^v+b0^2.
                        b0 = isqrt(d2*q)
                        assert b0*b0 == d2*q
                        Aodd = d2*m*gamma
                        assert Aodd%2 and b0%2
                        S = 2*Aodd
                        lower = Aodd*2**(G-1+4*v_min)
                        upper = S*(S+2*b0)
                        assert lower > upper
                        row.update({'reason':'fixed difference of two factors',
                                    'square_constant_root':b0,'A_odd':Aodd,
                                    'product_lower':lower,'product_upper':upper})
                        survivors.append(row)
                    exclusions.append(row)
    assert len(survivors) == 4
    assert sorted((z['G'],z['gamma'],z['delta1'],z['delta2'],z['T']) for z in survivors) == [
        (14,1,1,1,9),(17,1,1,1,1),(17,1,1,3,1),(17,1,3,1,1)]
    return {'all_oriented_branch_cases':exclusions,
            'after_coprimality_and_mod16':survivors,
            'remaining':0}


def growth_checks():
    # ln(2) lies between 2/3 and 1. With b=ceil(log2(6R)),
    # 4G-22 < 3*N*b^2+186 <= 18*R*b^2+186.
    ratio = Fraction(9*14**2,2*2**10)+Fraction(52,2**20)
    assert ratio == Fraction(225805,262144) < 1
    assert Fraction(1,14) < Fraction(1,3)
    return {'bound':'G < (9/2)*R_F*ceil(log2(6*R_F))^2+52',
            'threshold':'G>=2^20 implies R_F>sqrt(G)',
            'threshold_ratio':str(ratio),
            'asymptotic':'R_F=o(G/(log(G))^2) is impossible as G tends to infinity',
            'external_theorem':'von Kaenel arXiv:1310.7263v2, Corollary 6.2'}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    identities = symbolic_checks()
    diagnostics = curve_diagnostics()
    tables = [table_checks(source) for source in SOURCES]
    endings = finish_cases(tables)
    growth = growth_checks()
    result = {'status':'passed','symbolic_identities':identities,
              'diagnostics':diagnostics,'tables':tables,'gap_case_exclusions':endings,
              'growth':growth,
              'external_dependencies':[
                  'Completeness of vKM full curve lists, arXiv:1605.06079 Section 4.2.5 / Algorithm 4.6; not independently recomputed.',
                  'von Kaenel conductor-height theorem; not proved by this audit.',
                  'Previously established even-j normalization, six-block identities and G>=14.'],
              'conclusions':['N_F>1000','R_F>166',
                             'm*T*P*W_star has a prime factor at least 13'],
              'remaining':'R_F and G may both grow fast. No full solution of i=3 is claimed.'}
    path = artifact_path('verification_i3_growing_gap_frey.json')
    path.write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({'status':'passed','symbolic_identities':len(identities),
                      **diagnostics,'curve_rows_checked':sum(z['rows_checked'] for z in tables),
                      'table_gap_sum_candidates':sum(len(z['gap_sum_candidates']) for z in tables),
                      'remaining_gap_sum_cases':endings['remaining'],'growth':growth},indent=2))


if __name__ == '__main__':
    main()
