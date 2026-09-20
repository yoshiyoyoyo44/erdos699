"""Short modular checks for i3_finite_prime_obstruction_2026-09-20.md.

The universal claims are proved in the note. These checks never construct
2**u for the enormous exponents in the second construction.
"""

import json
from math import comb, lcm
from pathlib import Path


def empty_witness_set():
    primes = (3,5,7,11,13,17,19,23,29,31)
    period = lcm(6, *(p-1 for p in primes if p >= 5))
    assert period == 55440
    checked = 0
    for k in (1,2,7,100):
        for gamma, u in ((1,2+k*period),(3,k*period)):
            for p in primes:
                if p == 3:
                    nmod = gamma*pow(2,u,9) % 9
                    assert comb(nmod,3) % 3 != 0
                else:
                    nmod = gamma*pow(2,u,p) % p
                    assert nmod*(nmod-1)*(nmod-2)*pow(6,-1,p) % p != 0
                checked += 1
    return {'primes': primes, 'period': period, 'modular_checks': checked,
            'families': ['n=2^(2+55440*k)', 'n=3*2^(55440*k)'],
            'claim': 'None of the listed odd primes divides C(n,3), for all k>=1.'}


def nonvacuous_full_digit_pass():
    primes = (3,5,7)
    v = lcm(2, *(p*(p-1) for p in primes))
    j = 2**v
    data = []
    moduli = []
    for p in primes:
        K, pk = 1,p
        while pk <= j:
            K,pk = K+1,pk*p
        assert j % (p*p) == 1
        data.append({'p': p, 'K': K})
        moduli.append((p,K,pk))
    period = lcm(*(pk//p*(p-1) for p,K,pk in moduli))
    checked = 0
    for k in (1,2,3):
        u = v+k*period
        assert u >= 49 and u >= 4*v+14 and u > v+1
        for p,K,pk in moduli:
            nmod = pow(2,u,pk)
            assert nmod == j and pow(2,u,p*p) == 1
            # The lower K digits agree; every higher digit of j is zero.
            # Thus Lucas gives C(n,j) == 1 mod p, regardless of higher n digits.
            aa,bb,product = nmod,j,1
            while bb:
                product = product*comb(aa%p,bb%p) % p
                aa,bb = aa//p,bb//p
            assert product == 1
            checked += 1
    return {'primes': primes, 'v': v, 'j_bit_length': j.bit_length(),
            'prime_power_precisions': data, 'period_bit_length': period.bit_length(),
            'modular_checks': checked,
            'claim': 'Every listed p divides C(n,3), while Lucas gives C(n,j)=1 mod p.',
            'limitation': 'j is fixed; these are not counterexamples and fail the eventual endpoint bound.'}


def endpoint_identities():
    import sympy as s

    n,j,c0 = s.symbols('n j c0')
    minus = 2*j*j-4*j*n+2*j+n*n+n-2
    plus = 6*j*j-4*j*n-2*j+n*n-3*n+2
    mixed = c0*minus*plus/(2*(n-2)*(n-1)**2)
    assert s.factor(mixed.subs(j,0)-c0*(1+n/2)) == 0
    assert s.factor(mixed.subs(j,n)-c0*(1-3*n/2)) == 0
    return 2


def main():
    result = {'status': 'passed', 'absent_prime_construction': empty_witness_set(),
              'full_digit_construction': nonvacuous_full_digit_pass(),
              'endpoint_identities': endpoint_identities(),
              'scope': 'Method limitations only; no new counterexample or full exclusion.'}
    path = Path(__file__).with_name('verification_i3_finite_prime_obstruction.json')
    path.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(json.dumps(result,ensure_ascii=False,indent=2))


if __name__ == '__main__':
    main()
