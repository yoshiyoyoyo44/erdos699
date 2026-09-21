"""Extend the i=3 CRT exclusion to u=49,50 using 284*M^3 < 2^u.

The analytic bound is proved in i3_cubic_discriminant_minima_2026-09-21.md.
All inputs to the existing factorization generator remain below 2^64.
Independent replay proves primality recursively and enumerates all CRT roots.
"""
import hashlib
import json
from time import perf_counter

import make_certificate
from repo_paths import artifact_path
from replay_certificate import cube_root
from sieve_i3 import scan_row


def main():
    if not __debug__:
        raise RuntimeError('Run without -O.')
    start = perf_counter()
    certificates, rows = [], []
    source = artifact_path('i3_cubic_discriminant_minima_certificate.json')
    digest = hashlib.sha256(source.read_bytes()).hexdigest()
    for u in (49, 50):
        bound = cube_root(((1 << u)-1)//284)
        assert (bound << u) < 2**64
        totals = dict(u=u, M_bound=bound, rows=0, first_stage=0, second_stage=0)
        for odd in range(1, bound+1, 2):
            first, second, survivors = scan_row(u, odd, certificates)
            assert not survivors
            assert second == 0, 'A second-stage candidate needs an expanded replay.'
            totals['rows'] += 1
            totals['first_stage'] += first
        rows.append(totals)
        result = dict(method='cubic minima 284*M^3<2^u', min_u=49, max_u=u,
                      analytic_certificate=source.name, analytic_certificate_sha256=digest,
                      rows=rows, certificates=certificates)
        artifact_path('i3_u49_to_u50.json').write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
        print(json.dumps({**totals, 'elapsed_seconds': round(perf_counter()-start, 2)}), flush=True)
    for row in certificates:
        for p, _ in row['Q1_factors']:
            make_certificate.prove(p)
    artifact_path('prime_certificates_u50.json').write_text(
        json.dumps(make_certificate.cert, indent=2)+'\n', encoding='utf-8')
    print(json.dumps({'prime_certificates': len(make_certificate.cert),
                      'elapsed_seconds': round(perf_counter()-start, 2)}), flush=True)


if __name__ == '__main__':
    main()
