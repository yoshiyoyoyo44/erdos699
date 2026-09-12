"""Package the proof notes and replayable certificates without intermediate runs."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

FILES = [
    'README.md', 'erdos699_continuation_2026-09-12.md', 'source_progress.md',
    'AlgebraCertificates.lean', 'verification_lean.txt', 'verification_summary.json',
    'audit_algebra.py', 'sieve_i3.py', 'make_certificate.py', 'replay_certificate.py',
    'explore_descent.py', 'explore_invariants.py', 'package_results.py',
    'i3_original_replay.json', 'i3_u42.json', 'prime_certificates.json',
]

manifest = {name: hashlib.sha256(Path(name).read_bytes()).hexdigest() for name in FILES}
Path('SHA256.json').write_text(json.dumps(manifest, indent=2), encoding='utf-8')
archive = Path('erdos699_continuation_2026-09-12.zip')
with ZipFile(archive, 'w', compression=ZIP_DEFLATED, compresslevel=9) as z:
    for name in FILES + ['SHA256.json']:
        z.write(name)
with ZipFile(archive) as z:
    assert z.testzip() is None
    for name, digest in manifest.items():
        assert hashlib.sha256(z.read(name)).hexdigest() == digest
print(archive.resolve(), archive.stat().st_size)
