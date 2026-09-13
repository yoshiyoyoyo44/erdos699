"""Independent replay, using only the Python standard library.

All finite branch/residue coverage, coordinates, and inverse maps are checked.
Completeness of integral points relies on Magma's proved full Mordell--Weil
groups and IntegralPoints, not on this local coordinate check.
"""
from collections import Counter
from math import gcd, isqrt
from pathlib import Path
import json
import re
import xml.etree.ElementTree as ET

KEYS = ('gap', 'gamma', 'd1', 'd2', 'T', 'm', 'q', 'alpha')


def v2(n):
    assert n > 0
    return (n & -n).bit_length() - 1


def independent_cases():
    answer = []
    branches = [(1, 1, 1, 1, 112), (1, 1, 3, 9, 112),
                (1, 3, 1, 27, 80), (3, 1, 1, 3, 112)]
    for gap in range(10, 14):
        for gamma, d1, d2, numerator, denominator in branches:
            T = 1
            B = gamma * d1**2 * d2 * 2**(gap - 3)
            while denominator * T**3 < numerator * 2**gap:
                allowed = gcd(T, gamma * d1 * d2) == 1
                allowed &= not (gamma == 1 and T % 3 == 0 and T % 9 != 0)
                if allowed:
                    for q in range(1, B + 1):
                        m = B - T * q
                        if 0 < m < B and m % 2 and gcd(m, T) == 1 and q % 8 == d2:
                            answer.append((gap, gamma, d1, d2, T, m, q, m * gamma * 2**(gap - 1)))
                T += 2
    return sorted(answer)


def branch_ok(row, v):
    gap, gamma, d1, d2, T, m, q, alpha = (row[k] for k in KEYS)
    # Evaluate actual integers at a positive representative of the period.
    n = gamma * T * 2**(4 * (v + 360) + gap)
    actual1 = 3 if (n - 1) % 3 == 0 and (n - 1) % 9 != 0 else 1
    actual2 = 3 if (n // 2 - 1) % 3 == 0 and (n // 2 - 1) % 9 != 0 else 1
    if (d1, d2) != (actual1, actual2):
        return False
    w = d1**2 * d2 + T * 2**(4 * (v + 360) + 2) * m
    return d1 != 3 or w % 9 in (0, 1, 4, 7)


def feasible(row, v, modulus):
    gap, gamma, d1, d2, T, m, q, alpha = (row[k] for k in KEYS)
    x = pow(2, v, modulus)
    n = gamma * T * pow(2, gap, modulus) * x**4 % modulus
    possible_C = {d1 * T * c**2 % modulus for c in range(modulus)}
    for z in range(modulus):
        if (d2 * z**2 - alpha * x**4 - q) % modulus:
            continue
        if (d1 * gamma * pow(2, gap - 2, modulus) * x**2 + (n - 1) * z) % modulus in possible_C:
            return True
    return False


def read_and_check_curves():
    records = json.loads(Path('gap13_curve_cases.json').read_text(encoding='utf-8'))
    # Independently enumerate the 64 two-adic cases and remove the 8 square q.
    expected = [m for m in range(15, 1024, 16) if isqrt(1024 - m)**2 != 1024 - m]
    assert sorted(row['m'] for row in records) == expected and len(expected) == 56
    results = {}
    for batch in range(7):
        subset = records[8 * batch:8 * batch + 8]
        name = f'i3_gap13_batch{batch}.magma'
        src = Path(name).read_text(encoding='utf-8')
        assert src.count('assert rank_proved and group_proved;') == 8
        assert src.count('IntegralPoints(E:FBasis:=basis,SafetyFactor:=2)') == 8
        assert src.count('Order(G.i) eq 0') == 8
        assert 'GRH' not in src.replace('// Full group proof flags are required; no GRH setting is used.', '')
        assert 'SetClassGroupBounds' not in src
        text = '\n'.join(ET.parse(f'magma_gap13_batch{batch}.xml').getroot().itertext())
        assert 'G13_BATCH_COMPLETE' in text
        for bad in ('Runtime error', 'User error', 'Assertion failed', 'Time limit'):
            assert bad not in text
        blocks = re.findall(r'GAP_CURVE (\d+)\n(.*?)GAP_CURVE_COMPLETE \1(?:\n|$)', text, re.S)
        assert [int(a4) for a4, _ in blocks] == [row['a4'] for row in subset]
        for row, (a4, block) in zip(subset, blocks):
            a4 = int(a4)
            m = row['m']
            assert a4 == m * (1024 - m)
            assert row['input'] == name and row['response'] == f'magma_gap13_batch{batch}.xml'
            assert f'a4:={a4};' in src
            assert block.count('PROOF_FLAGS true true') == 1
            points = [tuple(map(int, p)) for p in re.findall(r'^POINT (-?\d+) (-?\d+)$', block, re.M)]
            count = int(re.search(r'POINT_COUNT (\d+)', block).group(1))
            rank = int(re.search(r'^RANK (\d+)$', block, re.M).group(1))
            assert len(points) == len(set(points)) == count
            inverse = []
            for X, Y in points:
                assert Y**2 == X**3 + a4 * X
                if X <= 0 or X % (64 * m):
                    continue
                value = X // (64 * m)
                exponent = v2(value)
                if value != 2**exponent or exponent % 2:
                    continue
                v = exponent // 2
                scale = 8 * m * 2**v
                if Y % scale:
                    continue
                Z = Y // scale
                assert Z**2 == 4096 * m * 16**v + 1024 - m
                assert 4 * v + 13 < 49
                inverse.append({'v': v, 'abs_Z': abs(Z)})
            results[m] = {'a4': a4, 'rank': rank, 'point_count': count, 'inverse': inverse}
    return results


def main():
    cert = json.loads(Path('i3_gap13_certificate.json').read_text(encoding='utf-8'))
    assert cert['schema'] == 1 and cert['min_u'] == 49 and cert['gap_range'] == [10, 13]
    assert cert['period'] == 360
    keys = [tuple(row[k] for k in KEYS) for row in cert['cases']]
    assert len(keys) == len(set(keys)) == 5099
    assert sorted(keys) == independent_cases()
    for modulus in cert['moduli']:
        assert modulus % 2 and pow(4, 360, modulus) == 1
    curves = read_and_check_curves()
    counts = {}
    exclusions = 0
    elliptic_m = []
    for row in cert['cases']:
        gap = row['gap']
        method = row['method']
        counts.setdefault(gap, Counter())[method] += 1
        if method == 'factor':
            A, B = row['d2'] * row['alpha'], row['d2'] * row['q']
            b = isqrt(B)
            assert b * b == B
            small = 2**v2(2 * b) * (A // 2**v2(A))
            bound = small * (small + 2 * b)
            assert bound == row['product_bound']
            assert A * 16**((49 - gap + 3) // 4) > bound
        elif method == 'two_adic':
            assert row['q'] % 16 != row['d1']**2 * row['d2'] * row['T']**2 % 16
        else:
            allowed = {v for v in range(360) if branch_ok(row, v)}
            for step in row['eliminations']:
                modulus = step['modulus']
                assert modulus in cert['moduli']
                rejected = set(step['residues'])
                assert len(rejected) == len(step['residues']) and rejected <= allowed
                for v in rejected:
                    assert not feasible(row, v, modulus)
                exclusions += len(rejected)
                allowed -= rejected
            if method == 'modular':
                assert not allowed
            else:
                assert method == 'elliptic' and gap == 13
                assert (row['gamma'], row['d1'], row['d2'], row['T']) == (1, 1, 1, 1)
                assert sorted(allowed) == row['surviving_residues']
                assert row['a4'] == curves[row['m']]['a4']
                elliptic_m.append(row['m'])
    assert sorted(elliptic_m) == sorted(curves)
    result = {'status': 'verified', 'case_count': len(keys), 'layers': counts,
              'period': 360, 'modular_residue_exclusions': exclusions,
              'curve_count': len(curves), 'curve_points_checked': sum(r['point_count'] for r in curves.values()),
              'curves': curves, 'even_j_necessary_bound': 'u >= 4*v2(j)+14',
              'g10_through_g12_magma_dependency': False, 'g13_magma_dependency': True,
              'complete_i3_solution': False}
    Path('verification_i3_gap13.json').write_text(json.dumps(result, indent=2) + '\n', encoding='utf-8')
    print(json.dumps({k: v for k, v in result.items() if k != 'curves'}, indent=2))
    print('Inverse cases:', {m: r['inverse'] for m, r in curves.items() if r['inverse']})


if __name__ == '__main__':
    main()
