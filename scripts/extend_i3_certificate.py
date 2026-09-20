"""Extend the independently replayable i=3 exclusion to 43 <= u <= 48.

Uses the already proved M^3 < 2^(u-2), without assuming the new lift lemma.
The upper limit keeps every factorization input below 2^64. Recursive Lucas
certificates subsequently remove dependence on the generator's primality test.
"""
from repo_paths import artifact_path
import argparse
import json
from pathlib import Path
from time import perf_counter

import make_certificate
from replay_certificate import cube_root
from sieve_i3 import scan_row


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--max-u', type=int, default=48)
    parser.add_argument('--output', default='i3_u43_to_u48.json')
    parser.add_argument('--primes', default='prime_certificates_u48.json')
    args = parser.parse_args()
    assert 43 <= args.max_u <= 48
    start = perf_counter()
    certificates, rows = [], []
    for u in range(43, args.max_u+1):
        bound = cube_root((1 << (u-2))-1)
        totals = dict(u=u, M_bound=bound, rows=0, first_stage=0, second_stage=0)
        for M in range(1, bound+1, 2):
            first, second, survivors = scan_row(u, M, certificates)
            assert not survivors
            assert second == 0, 'A new second-stage candidate requires a richer replay'
            totals['rows'] += 1
            totals['first_stage'] += first
            totals['second_stage'] += second
        rows.append(totals)
        result = dict(method='discriminant M^3<2^(u-2)', min_u=43, max_u=u,
                      rows=rows, certificates=certificates,
                      elapsed_seconds=perf_counter()-start)
        artifact_path(args.output).write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8')
        print(json.dumps(totals), flush=True)
    for row in certificates:
        for p, _ in row['Q1_factors']:
            make_certificate.prove(p)
    artifact_path(args.primes).write_text(json.dumps(make_certificate.cert, indent=2)+'\n', encoding='utf-8')
    print(json.dumps(dict(prime_certificates=len(make_certificate.cert),
                          elapsed_seconds=perf_counter()-start)), flush=True)


if __name__ == '__main__':
    main()
