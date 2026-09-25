"""Extend the supplied weighted-cover proof to i=29 and 35<=i<=119.

The generator reuses the supplied 192-bit outward-rounded interval engine.
Its output must be checked by replay_weighted_cover_extension.py, which uses
the separate 128-bit rational-series verifier and exact tail comparisons.
"""
import argparse
import gzip
import hashlib
import json
from math import factorial

from weighted_cover_sources import CERTIFICATES, INDICES, ROOT, load_source


def save_gzip(path, obj):
    payload = (json.dumps(obj, separators=(',', ':')) + '\n').encode()
    path.write_bytes(gzip.compress(payload, mtime=0))


def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled; do not use python -O.')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--reuse-cache', action='store_true',
                        help='Reuse experimental interval rows; independent replay is still required.')
    args = parser.parse_args()
    gen = load_source('generate.py', 'weighted_interval_generator')
    small = load_source('generate_small.py', 'weighted_small_generator')
    CERTIFICATES.mkdir(parents=True, exist_ok=True)
    cache = ROOT / 'dist/weighted_extension'
    cache.mkdir(parents=True, exist_ok=True)
    rows = []
    for i in INDICES:
        file = cache / f'i{i}.json'
        if args.reuse_cache and file.exists():
            row = json.loads(file.read_text())
            assert row['i'] == i
        else:
            a, b, d, S = gen.parameters(i)
            ps = gen.primes(i)
            hsmall = 1 if gen.primes(i+1)[-1] == i else i
            gap = d * (i-len(ps)) - 3*S
            assert gap > 0
            # The original search stopped at 10^99. Extend the finite search;
            # every accepted cutoff is established by exact integer arithmetic.
            for exponent in range(1, 513):
                n = 10**exponent
                if n >= 2*i+2 and (4**S * hsmall**d * (n-i+1)**(i*d)
                                  > factorial(i)**d * n**(len(ps)*d+3*S)):
                    break
            else:
                raise RuntimeError(f'No tail cutoff for {i}')
            tail = dict(n_power=exponent, small_part_correction=hsmall, degree_gap=gap)
            intervals = gen.generate_intervals(i, 2_000_000, n, d, S, ps)
            if intervals is None:
                raise RuntimeError(f'Weighted coverage failed for {i}; no theorem claimed')
            row = dict(i=i, pi=len(ps), a=a, b=b, d=d, S=S, tail=tail,
                       intervals=intervals)
            file.write_text(json.dumps(row, separators=(',', ':'))+'\n')
        rows.append(row)
        gen.logs.cache_clear()
        print(json.dumps(dict(i=i, intervals=len(row['intervals']['leaves']),
                              tail_power=row['tail']['n_power'])), flush=True)
    save_gzip(CERTIFICATES / 'intervals.json.gz', dict(schema=1, rows=rows))
    small.INDICES = INDICES
    small.ROOT = cache
    small.main()
    small_data = json.loads((cache / 'small_certificate.json').read_text())
    save_gzip(CERTIFICATES / 'small.json.gz', small_data)
    manifest = dict(schema=1, indices=INDICES, small_upper=1_999_999,
                    interval_count=sum(len(r['intervals']['leaves']) for r in rows),
                    small_exceptions=len(small_data['exceptions']),
                    files={name: hashlib.sha256((CERTIFICATES/name).read_bytes()).hexdigest()
                           for name in ('intervals.json.gz', 'small.json.gz')})
    (CERTIFICATES / 'manifest.json').write_text(json.dumps(manifest, indent=2)+'\n',
                                             encoding='utf-8', newline='\n')
    print(json.dumps(manifest, indent=2))


if __name__ == '__main__':
    main()
