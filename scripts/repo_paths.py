"""Resolve archived basenames without changing certificate or transcript bytes.

Explicit relative paths are relative to the repository root. Absolute paths
are respected. Historical bare names resolve through the migration manifest;
new generated artifacts use the same directory conventions.
"""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS_DIR = ROOT / 'scripts'
CASES_DIR = ROOT / 'data' / 'cases'
CERTIFICATES_DIR = ROOT / 'data' / 'certificates'
RESULTS_DIR = ROOT / 'data' / 'results'
_manifest = json.loads((ROOT / 'archive' / 'reorganization_2026-09-21.json').read_text(encoding='utf-8'))
_legacy = {entry['old']: entry['new'] for entry in _manifest['files']}


def artifact_path(name):
    path = Path(name)
    if path.is_absolute():
        return path
    key = path.as_posix()
    if key in _legacy:
        return ROOT / _legacy[key]
    if path.parent != Path('.'):
        return ROOT / path
    if key.startswith('verification_'):
        return RESULTS_DIR / path
    if key.endswith('_cases.json'):
        return CASES_DIR / path
    if key.endswith('_certificate.json') or key.startswith(('prime_certificates', 'i3_u')):
        return CERTIFICATES_DIR / path
    if path.suffix == '.magma':
        return ROOT / 'magma' / 'inputs' / path
    if path.suffix == '.xml':
        return ROOT / 'magma' / 'outputs' / path
    if path.suffix == '.py':
        return SCRIPTS_DIR / path
    return ROOT / path
