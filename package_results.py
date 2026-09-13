"""Package the proof notes and replayable certificates without intermediate runs."""
import hashlib
import json
from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED
import xml.etree.ElementTree as ET

FILES = [
    'STATUS_AND_DIRECTIONS.md',
    'README.md', 'erdos699_continuation_2026-09-12.md', 'source_progress.md',
    'AlgebraCertificates.lean', 'verification_lean.txt', 'verification_summary.json',
    'audit_algebra.py', 'sieve_i3.py', 'make_certificate.py', 'replay_certificate.py',
    'explore_descent.py', 'explore_invariants.py', 'package_results.py',
    'i3_original_replay.json', 'i3_u42.json', 'prime_certificates.json',
    'discriminant_continuation.md', 'i3_square_branch.md',
    'audit_discriminant.py', 'verification_discriminant.json',
    'certify_large_indices.py', 'certify_prime_gaps.py', 'replay_large_indices.py',
    'large_index_certificate.json', 'prime_gap_certificate.json',
    'verification_large_indices.json', 'explore_large_indices.py',
    'i3_2adic_and_square_continuation.md', 'audit_i3_2adic_square.py',
    'verification_i3_2adic_square.json', 'explore_square_parameters.py',
    'i3_all_square_branches.md', 'audit_i3_all_square.py',
    'verification_i3_all_square.json',
    'source_nonsquare_handoff_2026-09-12.md', 'i3_nonsquare_merged_continuation.md',
    'audit_i3_nonsquare_lifts.py', 'verification_i3_nonsquare_lifts.json',
    'extend_i3_certificate.py', 'i3_u43_to_u48.json', 'prime_certificates_u48.json',
    'verification_u48.json', 'verification_existing_replay.json',
    'i3_boundary_and_fixed_blocks.md', 'i3_boundary_quartics.magma',
    'magma_boundary_quartics.xml', 'make_small_block_magma.py',
    'run_magma_audit.py', 'run_magma_batches.py', 'audit_i3_fixed_blocks.py',
    'verification_i3_fixed_blocks.json', 'certify_fixed_block_modular.py',
    'fixed_block_modular_exclusions.json',
    'source_direction2_progress_2026-09-13.md',
    'source_kummer_all_digits_progress_2026-09-13.md',
    'i3_integrated_digits_and_center.md', 'audit_i3_integrated_digits.py',
    'verification_i3_integrated_digits.json',
    'i3_direct_center_and_endpoint_curves.md', 'make_center_curve_magma.py',
    'audit_i3_center_curve.py', 'center_curve_cases.json',
    'endpoint_curve_cases.json', 'verification_i3_center_curve.json',
    'interval_valuation_continuation.md', 'certify_interval_indices.py',
    'replay_interval_indices.py', 'interval_index_certificate.json',
    'verification_interval_indices.json', 'explore_interval_valuations.py',
    'source_critical_indices_handoff_2026-09-13.md',
    'source_i3_gap_handoff_2026-09-13.md',
    'critical_indices_and_handoff_integration.md',
    'near_collision_arithmetic.py', 'certify_near_collisions.py',
    'near_collision_certificate.json', 'replay_near_collisions.py',
    'verification_near_collisions.json', 'certify_critical_indices.py',
    'critical_index_certificate.json', 'replay_critical_indices.py',
    'verification_critical_indices.json',
    'i3_exact_gap_and_g9_continuation.md', 'explore_gap_layers.py',
    'certify_i3_gap_layers.py', 'i3_gap_certificate.json',
    'replay_i3_gap_layers.py', 'verification_i3_gap_layers.json',
    'make_gap_curve_magma.py', 'gap_curve_cases.json',
    'audit_handoff_algebra.py', 'verification_handoff_algebra.json',
    'i119_a100_continuation.md', 'certify_near_collisions_a100.py',
    'near_collision_a100_certificate.json', 'replay_near_collisions_a100.py',
    'verification_near_collisions_a100.json', 'certify_i119_finite.py',
    'i119_finite_certificate.json', 'replay_i119_finite.py', 'verification_i119_finite.json',
    'source_pure_power_descent_2026-09-13.md', 'i3_gap13_and_descent_continuation.md',
    'certify_i3_gap13.py', 'replay_i3_gap13.py', 'i3_gap13_certificate.json',
    'gap13_curve_cases.json', 'verification_i3_gap13.json',
    'audit_i3_descent.py', 'verification_i3_descent.json',
]

for batch in range(7):
    FILES += [f'i3_gap13_batch{batch}.magma', f'magma_gap13_batch{batch}.xml']

for case_file in ('center_curve_cases.json', 'endpoint_curve_cases.json', 'gap_curve_cases.json'):
    for row in json.loads(Path(case_file).read_text(encoding='utf-8')):
        FILES += [row['input'], row['response']]

for role in 'ABC':
    for value in (5,7,9):
        FILES += [f'small_{role}{value}_cases.json', f'i3_small_{role}{value}.magma',
                  f'magma_small_{role}{value}.xml']
        root = ET.parse(f'magma_small_{role}{value}.xml').getroot()
        if root.get('aggregate') == 'true':
            for entry in root.find('sources'):
                FILES += [entry.get('input'), entry.get('response')]
assert len(FILES) == len(set(FILES))

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
