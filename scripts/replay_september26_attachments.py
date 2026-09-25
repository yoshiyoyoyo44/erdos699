"""Replay all six supplied audits in disposable copies and check source hashes.

Raw attachments, including historical verification.json files, are immutable.
The independent denominator results are checked along with the parent packages;
the optional A=100 baseline itself is not replayed by this command.
"""
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import zipfile

from weighted_cover_sources import INCOMING, ROOT


def check_hashes():
    imports = json.loads((INCOMING/'import_manifest.json').read_text())
    for item in imports['files']:
        file = ROOT/item['file']
        assert file.stat().st_size == item['bytes']
        assert hashlib.sha256(file.read_bytes()).hexdigest() == item['sha256']
        if file.suffix == '.zip':
            # Tie the extracted manifest and code themselves to the original ZIP,
            # not just to a possibly edited extracted SHA256.json.
            with zipfile.ZipFile(file) as archive:
                for entry in archive.infolist():
                    if entry.is_dir():
                        continue
                    extracted = (INCOMING/entry.filename).resolve()
                    assert extracted.is_relative_to(INCOMING.resolve())
                    assert extracted.read_bytes() == archive.read(entry)
    count = 0
    for manifest in sorted(INCOMING.rglob('SHA256.json')):
        for name, digest in json.loads(manifest.read_text()).items():
            file = (manifest.parent/name).resolve()
            assert file.is_relative_to(INCOMING.resolve())
            assert hashlib.sha256(file.read_bytes()).hexdigest() == digest, str(file)
            count += 1
    return len(imports['files']), count


def main():
    if not __debug__:
        raise RuntimeError('Assertions must be enabled; do not use python -O.')
    originals, entries = check_hashes()
    five = 'erdos699_five_indices_complete_2026-09-26'
    coupled = 'erdos699_coupled_factor_constraints_2026-09-26'
    cases = [(five, 'verify.py', 'verification.json'),
             (five, 'audit_cover.py', 'cover_audit.json')]
    cases += [(coupled + '/previous_phase'*level, 'verify.py', 'verification.json')
              for level in range(4)]
    # The temporary tree contains only these copies; it is verified before cleanup.
    temp_parent = Path(tempfile.gettempdir()).resolve()
    temp = Path(tempfile.mkdtemp(prefix='erdos699-attachments-', dir=temp_parent)).resolve()
    runs = []
    try:
        for package in (five, coupled):
            shutil.copytree(INCOMING/package, temp/package)
        for package, script, output in cases:
            process = subprocess.run([sys.executable, '-X', 'utf8', str(temp/package/script)],
                                     capture_output=True, text=True, encoding='utf-8', timeout=600)
            assert process.returncode == 0, process.stdout[-2000:] + process.stderr
            observed = json.loads((temp/package/output).read_text())
            expected = json.loads((INCOMING/package/output).read_text())
            assert observed == expected, f'Result mismatch: {package}/{output}'
            runs.append(dict(script=f'{package}/{script}', result=observed,
                             matches_supplied_result=True))
            print(f'PASS {package}/{script}', flush=True)
    finally:
        assert temp.parent == temp_parent and temp.name.startswith('erdos699-attachments-')
        shutil.rmtree(temp)
    assert check_hashes() == (originals, entries)
    result = dict(status='PASS', original_attachments=originals,
                  package_hash_entries=entries, runs=runs,
                  raw_files_unchanged=True, missing_i3_bodies_verified=False,
                  a100_baseline_replayed=False)
    output = ROOT/'data/results/verification_september26_attachments.json'
    output.write_text(json.dumps(result, ensure_ascii=False, indent=2)+'\n',
                      encoding='utf-8', newline='\n')
    print(json.dumps(dict(status='PASS', audits=len(runs), hash_entries=entries)))


if __name__ == '__main__':
    main()
