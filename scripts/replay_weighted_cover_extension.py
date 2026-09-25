"""Independently replay every interval, tail and small-n exception of the extension.

No certificate generator is imported. The unmodified attached verifier
uses direct rational logarithm series, different from the generation engine.
Only the advertised index set is extended; all numerical bounds are recomputed.
"""
import gzip
import hashlib
import json

from weighted_cover_sources import CERTIFICATES, INDICES, ROOT, load_source


def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled; do not use python -O.')
    manifest = json.loads((CERTIFICATES / 'manifest.json').read_text())
    assert manifest['schema'] == 1 and manifest['indices'] == INDICES
    for name, digest in manifest['files'].items():
        assert hashlib.sha256((CERTIFICATES/name).read_bytes()).hexdigest() == digest
    cert = json.loads(gzip.decompress((CERTIFICATES/'intervals.json.gz').read_bytes()))
    assert cert['schema'] == 1 and [r['i'] for r in cert['rows']] == INDICES
    verifier = load_source('verify.py', 'weighted_extension_verifier')
    verified = []
    for row in cert['rows']:
        verifier.INDICES = [row['i']]
        verified += verifier.check_intervals(dict(schema=1, rows=[row]))
        verifier.log_interval.cache_clear()
    assert sum(r['interval_count'] for r in verified) == manifest['interval_count']
    verifier.INDICES = INDICES
    small_cert = json.loads(gzip.decompress((CERTIFICATES/'small.json.gz').read_bytes()))
    small = verifier.check_small(small_cert)
    assert small['exception_count'] == manifest['small_exceptions']
    assert small_cert['covered_upper'] == manifest['small_upper'] == 1_999_999
    formulas = verifier.check_formula()
    result = dict(status='PASS', proved_indices=INDICES,
                  domain='All integers i<j<=n/2 for each listed i; all n.',
                  interval_count=manifest['interval_count'], interval_rows=verified,
                  small_range=small, formula_tests=formulas,
                  uses_a100_certificate=False, uses_discriminant=False,
                  missing_i3_manuscripts_used=False,
                  independent_peer_review=False, formal_lean_verification=False)
    output = ROOT / 'data/results/verification_weighted_cover_extension.json'
    output.write_text(json.dumps(result, indent=2)+'\n', encoding='utf-8', newline='\n')
    print(json.dumps({k: v for k, v in result.items() if k != 'interval_rows'}, indent=2))


if __name__ == '__main__':
    main()
