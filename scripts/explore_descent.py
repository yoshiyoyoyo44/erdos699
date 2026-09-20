"""Search for obstructions to possible universal descent lemmas.

Here C can have arbitrary prime factors. Such systems are not counterexamples
to Erdős 699; they expose which hypotheses a descent must preserve.
"""
from math import gcd
from sieve_i3 import certified_factors, roots_zero_or_C, valuation, binomial_valuation

found = []
for C in range(16, 200001, 16):
    T = 1
    d1 = 3 if valuation(C-1, 3) == 1 else 1
    d2 = 3 if valuation(C//2-1, 3) == 1 else 1
    Q1, Q2 = (C-1)//d1, (C//2-1)//d2
    roots, modulus = roots_zero_or_C(C, certified_factors(Q1))
    for r in roots:
        k = r + max(0, (4-r+Q1-1)//Q1)*Q1
        while k < C//2:
            if k*(C//2-k)*(C-k) % Q2 == 0:
                ps = set(p for t in (C,C-1,C-2) for p,e in certified_factors(t) if p>2)
                common = [p for p in sorted(ps) if binomial_valuation(C,3,p)>0
                          and binomial_valuation(C,k,p)>0]
                found.append((C,k,d1,d2,common))
                print(found[-1], flush=True)
            k += Q1
    if len(found) >= 15:
        break
print('systems', len(found), 'last_C', C)
