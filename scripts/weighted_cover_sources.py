"""Locate the byte-preserved September 26 proof package without changing it."""
import importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INCOMING = ROOT / 'archive/attachments/incoming_2026-09-26'
FIVE = INCOMING / 'erdos699_five_indices_complete_2026-09-26'
CERTIFICATES = ROOT / 'data/certificates/weighted_cover_2026-09-26'
INDICES = [29, *range(35, 120)]


def load_source(filename, module_name):
    spec = importlib.util.spec_from_file_location(module_name, FIVE / filename)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module
