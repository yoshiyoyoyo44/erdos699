"""Finite certificates for gap layers 10--13; elliptic completeness uses Magma."""
import json
from collections import Counter
from pathlib import Path

from explore_gap_layers import rows, factor_bound, admissible_branch, local, PERIOD, MODULI
from make_gap_curve_magma import source

EXTRA_MODULI = [11, 41, 61, 151, 241, 257, 331, 577, 673]


def main():
    moduli = MODULI + EXTRA_MODULI
    cases = []
    curves = []
    counts = {}
    for gap in range(10, 14):
        counts[gap] = Counter()
        for original in rows(gap):
            row = dict(original)
            fb = factor_bound(row)
            vmin = (49 - gap + 3) // 4
            if fb and fb[1] * 16**vmin > fb[0]:
                row.update(method='factor', product_bound=fb[0])
            elif (row['q'] - row['d1']**2 * row['d2'] * row['T']**2) % 16:
                row['method'] = 'two_adic'
            else:
                permitted = {v for v in range(PERIOD) if admissible_branch(row, v)}
                eliminations = []
                for ell in moduli:
                    rejected = sorted(v for v in permitted if not local(row, v, ell))
                    if rejected:
                        eliminations.append({'modulus': ell, 'residues': rejected})
                        permitted -= set(rejected)
                    if not permitted:
                        break
                row['eliminations'] = eliminations
                if permitted:
                    assert gap == 13
                    assert (row['gamma'], row['d1'], row['d2'], row['T']) == (1, 1, 1, 1)
                    m = row['m']
                    assert m % 16 == 15
                    a4 = m * (1024 - m)
                    row.update(method='elliptic', a4=a4, surviving_residues=sorted(permitted))
                    curves.append({'m': m, 'q': 1024 - m, 'a4': a4})
                else:
                    row['method'] = 'modular'
            counts[gap][row['method']] += 1
            cases.append(row)
    assert len(cases) == 5099 and len(curves) == 56
    for batch in range(7):
        subset = curves[8 * batch:8 * batch + 8]
        name = f'i3_gap13_batch{batch}.magma'
        code = '\n'.join(source(row['a4']) for row in subset)
        code += '\nprint "G13_BATCH_COMPLETE";\n'
        Path(name).write_text(code, encoding='utf-8')
        for row in subset:
            row.update(input=name, response=f'magma_gap13_batch{batch}.xml')
    Path('gap13_curve_cases.json').write_text(json.dumps(curves, indent=2) + '\n', encoding='utf-8')
    cert = {'schema': 1, 'min_u': 49, 'gap_range': [10, 13], 'period': PERIOD,
            'moduli': moduli, 'cases': cases}
    Path('i3_gap13_certificate.json').write_text(json.dumps(cert, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(counts, indent=2))


if __name__ == '__main__':
    main()
