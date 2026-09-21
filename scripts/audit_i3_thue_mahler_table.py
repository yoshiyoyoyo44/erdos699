"""Audit published Thue-Mahler data and its interface with our cubics.

Completeness of the listed solutions is EXTERNAL: von Kaenel--Matschke,
Theorem E (arXiv:1605.06079). This does not rerun their elliptic-logarithm
sieve. Locally we verify every row, the exponent maximum, and coverage of
our independently enumerated irreducible Hessian-reduced forms.
"""
import ast
import hashlib
import json
import re
from itertools import product
from math import gcd

from repo_paths import ROOT, artifact_path
from replay_i3_cubic_discriminant_minima import disc, hessian, has_rational_root, transform

SHA256='01ea6aa44010574101abba19c88165d1e6bb460e23583f47fb8cd313bf1291b2'


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    path=ROOT/'sources/thueMahler__maxD3000_n2.txt'
    raw=path.read_bytes()
    assert hashlib.sha256(raw).hexdigest()==SHA256
    headers={}; rows=[]; pairs=0; positive_pairs=0
    f=None
    for line in raw.decode('utf-8').splitlines():
        m=re.fullmatch(r'# \(a,b,c,d\) = (\(.*\)) and D = (-?\d+):',line)
        if m:
            f=ast.literal_eval(m[1]); label=int(m[2]); delta=disc(f)
            # Salmon/vKM use the opposite sign from the standard polynomial
            # discriminant used throughout this repository.
            assert delta==-label and 0<abs(delta)<=3000
            assert f not in headers
            headers[f]=delta
        elif line.startswith('('):
            assert f is not None
            x,y=ast.literal_eval(line); a,b,c,d=f
            z=a*x**3+b*x*x*y+c*x*y*y+d*y**3
            assert gcd(x,y)==1 and z!=0
            residual=abs(z)
            for p in (2,3):
                while residual%p==0:
                    residual//=p
            assert residual==1
            pairs+=1
            if delta>0:
                positive_pairs+=1
                if abs(z)&(abs(z)-1)==0:
                    rows.append({'E':abs(z).bit_length()-1,'delta':delta,
                                 'form':f,'point':[x,y],'value':z})
    assert len(headers)==4961 and pairs==33456
    assert max(row['E'] for row in rows)==28

    # Complete box for irreducible forms with 0<Delta<=3000:
    # a<=2, A<=54, |b|<=10, |c|<=33, |d|<=42.
    forms=[]; tested=0
    for f0 in product(range(1,3),range(-10,11),range(-33,34),range(-42,43)):
        tested+=1
        delta0=disc(f0)
        if not 0<delta0<=3000:
            continue
        A,B,C=hessian(f0)
        if not (0<A and abs(B)<=A<=C) or has_rational_root(f0):
            continue
        forms.append(f0)
    matrices=[m for m in product(range(-2,3),repeat=4) if abs(m[0]*m[3]-m[1]*m[2])==1]
    coverage=[]
    for f0 in sorted(forms):
        for mat in matrices:
            target=transform(f0,mat)
            if target in headers:
                coverage.append({'form':f0,'matrix':mat,'table_form':target,'delta':disc(f0)})
                break
        else:
            raise AssertionError(('Missing GL2 certificate',f0,disc(f0)))
    result={'status':'passed','source_url':'https://www.math.u-bordeaux.fr/~bmatschke/data/thueMahler__maxD3000_n2.txt',
            'source_sha256':SHA256,'source_license':'CC BY-NC 3.0; Rafael von Kaenel and Benjamin Matschke (2015)',
            'external_completeness':'Theorem E, arXiv:1605.06079; NOT independently recomputed here',
            'discriminant_label_is_negative_of_our_discriminant':True,
            'table_forms':len(headers),'checked_primitive_2_3_unit_pairs':pairs,
            'positive_discriminant_pairs':positive_pairs,'positive_discriminant_2power_pairs':len(rows),
            'maximum_E':28,'maximum_rows':[r for r in rows if r['E']==28],
            'independent_box_tuples':tested,'hessian_reduced_irreducible_forms':len(forms),
            'coverage':coverage,
            'consequence':'A counterexample must have terminal discriminant >3000; hence (16000/9)*M^3 < 2^u.'}
    artifact_path('verification_i3_thue_mahler_table.json').write_text(json.dumps(result,indent=2)+'\n',encoding='utf-8')
    print(json.dumps({k:v for k,v in result.items() if k!='coverage'},indent=2))


if __name__=='__main__':
    main()
