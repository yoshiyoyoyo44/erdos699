"""Reproduce the checks added when integrating the two September 26 handoffs.

This does not certify the omitted occupied-q case reductions, the i3 support
identity, or external theorems. Small-n diagnostics are not infinite proofs.
The line-cover enumeration is exhaustive over its explicitly listed supports.
"""
import hashlib
import json
from fractions import Fraction
from itertools import combinations, product
from math import comb, factorial, prod

from repo_paths import ROOT, RESULTS_DIR


def valuation(n, p):
    assert n > 0
    e = 0
    while n % p == 0:
        e += 1
        n //= p
    return e


def large_part(n):
    for p in (2, 3):
        n //= p ** valuation(n, p)
    return n


def check_source_hashes():
    manifest = json.loads((ROOT / 'sources/handoff_import_2026-09-26.json').read_text(encoding='utf-8'))
    for entry in manifest['files']:
        data = (ROOT / entry['path']).read_bytes()
        assert len(data) == entry['bytes'], entry['path']
        assert hashlib.sha256(data).hexdigest() == entry['sha256'], entry['path']
    return len(manifest['files'])


def cofactor_checks():
    primes = [p for p in range(2, 35) if all(p % d for d in range(2, p))]
    beta_rows, diagnostics = [], 0
    for i in range(3, 35):
        if i == 29:
            continue
        small = [p for p in primes if p < i]
        m = len(small)
        h = i - 1
        b = (2 * h + 2) // 3
        d = 3 * b - h
        S = b * (b + 1) // 2
        beta = Fraction(3 * S, d) - (i - m)
        assert beta < 2
        if i >= 5:
            assert m - beta > 1
        beta_rows.append({'i': i, 'm': m, 'b': b, 'd': d, 'S': S, 'beta': str(beta)})
        i_small = prod(p ** valuation(i, p) for p in small)
        for n in range(2 * i + 2, 301):
            A = comb(n, i)
            Q = A
            cofactors, powers, rows = [], [], []
            for p in small:
                row_values = [valuation(n - r, p) for r in range(i)]
                E = max(row_values)
                r = row_values.index(E)
                vA = valuation(A, p)
                assert vA <= E - valuation(i, p)
                Q //= p ** vA
                cofactors.append((n - r) // p ** E)
                powers.append(p ** E)
                rows.append(r)
            a_product = prod(cofactors)
            distinct = set(rows)
            assert Q * factorial(i) * n ** m >= i_small * a_product * (n - i + 1) ** i
            assert a_product >= (n - i + 1) ** (m - len(distinct))
            assert prod(n - r for r in distinct) % prod(powers) == 0
            diagnostics += 1
    values = {r['i']: Fraction(r['beta']) for r in beta_rows}
    assert values[3] == Fraction(1, 4) and values[4] == 1
    assert [i for i, beta in values.items() if beta == 0] == [28, 31, 34]
    return {'beta_values': beta_rows, 'local_n_i_diagnostics': diagnostics,
            'diagnostic_n_max': 300, 'tie_choice_in_diagnostics': 'first maximizing row'}


def constant_checks():
    assert 2 ** 34 * factorial(34) < 2 ** 162
    C = 13_200_000_000_000
    # Square the irrational 3**4.5 term to compare the claimed coefficient
    # exactly. This is arithmetic only, not an audit of Matveev's theorem.
    squared = (Fraction(14, 10) * 30 ** 6 * Fraction(7, 10)
               * Fraction(11, 10) * 114) ** 2 * 3 ** 9
    assert squared < C ** 2
    assert Fraction(2, 3) * 10 ** 15 - 5 - 36 * C > 0
    assert Fraction(2, 3) > Fraction(C, 10 ** 15)
    assert (9 * 2 ** 3, 27 * 2 ** 4, 9 * 3 ** 3, 27 * 3 ** 4) == (72, 432, 243, 2187)
    assert 2 ** 289 < 10 ** 87 <= 2 ** 290
    assert 3 ** 182 < 10 ** 87 <= 3 ** 183
    assert 2 ** 290 - 3 > 2187 * 290 ** 4
    assert 3 ** 183 - 3 > 2187 * (4 * 183) ** 4
    # Correction: the source's strict comparison here is an equality.
    assert Fraction(432) * Fraction(3, 2) ** 4 == 2187
    for u in range(2, 501):
        q = 3 ** max(valuation(2 ** u - s, 3) for s in (1, 2, 3))
        m = u // 2 if u % 2 == 0 else (u - 1) // 2
        assert q == 3 ** (1 + valuation(m, 3))
        assert 2 * q <= 3 * u
    for a in range(2, 301):
        q = 2 ** max(valuation(3 ** a - s, 2) for s in (1, 2, 3))
        b = a if a % 2 == 0 else a - 1
        assert q == 2 ** (2 + valuation(b, 2))
        assert q <= 4 * a
    assert 2 * 290 ** 4 > 291 ** 4 and 3 * 183 ** 4 > 184 ** 4
    return {'Matveev_coefficient_arithmetic_only': True,
            'pure_2_power_diagnostics': 499, 'pure_3_power_diagnostics': 299,
            'corrected_equality': '432*(3/2)^4 = 2187'}


def empty_q_checks():
    # For e>=32 the note bounds both cubic expressions by 54*T**3,
    # with T<=3e. The ratio 2**e/e**3 increases from this endpoint.
    assert 2 ** 32 - 1 > 1458 * 32 ** 3
    assert 2 * 32 ** 3 > 33 ** 3
    assert 2 ** 10 > 9 * 9 ** 2
    assert 2 * 9 ** 2 > 10 ** 2
    records = []
    families = [(18, 4, 18)]
    for residue in (9, 27):
        for e in range(1, 32, 2):
            n = 2 ** e + 1 if residue == 9 else 3 * (2 ** e + 1)
            if n >= 10 and n % 36 == residue:
                families.append((residue, e, n))
    for residue, exponent, n in families:
        R = [large_part(n - s) for s in range(4)]
        rejected = []
        for a in range(1, n // (2 * R[0]) + 1):
            j = a * R[0]
            if j < 5:
                continue
            failing = [s for s in range(1, 4)
                       if prod(j - k for k in range(s + 1)) % R[s]]
            assert failing, (residue, exponent, n, j)
            rejected.append({'a': a, 'j': j, 'failing_row': failing[0]})
        records.append({'residue': residue, 'exponent': exponent, 'n': n,
                        'row_0': R[0], 'rejected_candidates': rejected})
    return {'tail_exponent': 32, 'tail_bound': '2^32-1 > 1458*32^3',
            'finite_families_checked': len(records),
            'finite_candidates_excluded': sum(len(r['rejected_candidates']) for r in records),
            'finite_certificate': records}


def support_covers():
    cells = {(s, k) for s in range(1, 4) for k in range(s + 1)}
    lines = [(f'C{k}', {x for x in cells if x[1] == k}) for k in range(4)]
    lines += [(f'D{v}', {x for x in cells if x[0] - x[1] == v}) for v in range(4)]
    pairs = list(combinations(lines, 2))
    records = {28: [], 9: []}
    for q, row2, row3 in product(range(2), combinations(range(3), 2), combinations(range(4), 2)):
        heavy = {(2, k) for k in row2} | {(3, k) for k in row3}
        full = heavy | {(1, q)}
        for residue in records:
            witness = None
            for (an, ac), (bn, bc) in pairs:
                has_column = an.startswith('C') or bn.startswith('C')
                if residue == 28 and heavy <= ac | bc and has_column:
                    witness = {'kind': 'heavy_two_lines_with_column', 'lines': [an, bn]}
                    break
                if residue == 28 and full <= ac | bc and not has_column:
                    witness = {'kind': 'full_two_diagonals', 'lines': [an, bn]}
                    break
                if residue == 9 and full <= ac | bc and has_column:
                    witness = {'kind': 'full_two_lines_with_column', 'lines': [an, bn]}
                    break
            records[residue].append({'cells': sorted(full), 'excluded_by': witness})
    # At n=10 all three lower products exceed the respective capacity.
    # On writing n=10+x, each gap numerator has positive coefficients:
    # n²-10n+12 = x²+10x+12;
    # 3n²-25n+30 = 3x²+35x+80;
    # 7n²-50n+60 = 7x²+90x+260.
    for coefficients in ((12, -10, 1), (30, -25, 3), (60, -50, 7)):
        shifted = [sum(coefficients[k] * comb(k, j) * 10 ** (k - j)
                       for k in range(j, 3)) for j in range(3)]
        assert all(c > 0 for c in shifted)
    counts = {}
    for residue, rows in records.items():
        assert len(rows) == 36
        remaining = sum(r['excluded_by'] is None for r in rows)
        assert remaining == (18 if residue == 28 else 28)
        counts[residue] = {'raw': 36, 'excluded': 36 - remaining,
                           'remaining': remaining, 'supports': rows}
    two_columns = [r for r in records[9] if r['excluded_by'] and
                   all(x.startswith('C') for x in r['excluded_by']['lines'])]
    assert len(two_columns) == 4
    return {'capacity_proof_valid_for_n_at_least': 10,
            'source_9_class_reported_remaining': 30,
            'two_column_exclusions': two_columns, 'residue_classes': counts}


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    result = {
        'status': 'passed',
        'scope': 'source preservation, arithmetic diagnostics, empty-q finite certificate, and exact two-line support enumeration',
        'not_certified': ['omitted occupied-q five-cell reductions for 18,20,27',
                          'i3 odd support identity with missing definitions',
                          'external S-part and Matveev theorems',
                          'complete solution of any remaining index'],
        'source_hashes_checked': check_source_hashes(),
        'cofactors': cofactor_checks(),
        'constants': constant_checks(),
        'empty_q': empty_q_checks(),
        'line_covers': support_covers(),
    }
    output = RESULTS_DIR / 'verification_handoff_integration_2026-09-26.json'
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2) + '\n',
                      encoding='utf-8', newline='\n')
    print(json.dumps({'status': result['status'], 'source_hashes': result['source_hashes_checked'],
                      'cofactor_diagnostics': result['cofactors']['local_n_i_diagnostics'],
                      'empty_q_candidates': result['empty_q']['finite_candidates_excluded'],
                      'remaining_supports': {r: v['remaining'] for r, v in result['line_covers']['residue_classes'].items()},
                      'output': output.relative_to(ROOT).as_posix()}, indent=2))


if __name__ == '__main__':
    main()
