#!/usr/bin/env python3
from math import lcm
from pathlib import Path
import json
from factor_allocation import primes_below

ROOT = Path(__file__).resolve().parent


def first_true(predicate, high=10**12):
    lo, hi = 1, high
    assert predicate(hi)
    while lo < hi:
        mid = (lo+hi)//2
        if predicate(mid): hi = mid
        else: lo = mid+1
    return lo


def main():
    previous = json.loads((ROOT/'previous_phase/certificate.json').read_text())
    rows = []
    for old in previous['rows']:
        i, pi, eps = old['i'], old['pi'], old['prime_correction']
        inherited = next(c for c in old['cases']
                         if c['n_power'] == 87 and not c['uses_a100'])
        assert inherited['excluded_denominator_B'] >= i-1
        C = eps*lcm(*range(1, pi+1))
        assert 512**(pi+1) > 2*C*(i-1)**(pi+1)
        assert 10**550 > (512*C)**32
        counts = []
        for x in (87, 100, 105):
            good = [k for k in range(i)
                    if 10**x > 4*(i-1)*(eps*lcm(*range(1, k+1)))**2]
            k = max(good)
            regular = k+1-pi
            counts.append(dict(n_power=x, prefix_last_row=k,
                prefix_constant=str(eps*lcm(*range(1, k+1))),
                guaranteed_regular_rows=regular,
                distinct_large_prime_lower_bound=max(0, 2*regular-1)))
        assert counts[-1]['prefix_last_row'] == i-1
        rows.append(dict(i=i, pi=pi, epsilon=eps,
            inherited_denominator_bound=inherited['excluded_denominator_B'],
            high_row_range=[pi+1, i-1], high_row_degree=pi+1,
            high_row_constant=str(C), count_certificates=counts))
    n = 10**200
    i119_C = lcm(*range(1,31))
    a119 = first_true(lambda a: i119_C*(118*a)**31 >= n-30)
    au = first_true(lambda a: (512*a)**31 > n)
    obj = dict(source_commit=previous['source_commit'], status='GENERATED',
        theorem_status='PROVED; independent of the missing index manuscripts',
        pair_bound_n_power=87, all_rows_count_n_power=105,
        zero_row_n_power=550, rows=rows,
        numerical_examples=dict(n_power=200,
            high_rows_uniform_minimum_cofactor=au,
            i119_high_rows_minimum_cofactor=a119),
        no_global_novelty_claim=True)
    (ROOT/'certificate.json').write_text(json.dumps(obj, indent=2)+'\n')
    print(json.dumps(obj['numerical_examples']))


if __name__ == '__main__':
    main()
