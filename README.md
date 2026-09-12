# Erdős 699 — 2026-09-12 continuation

This is a partial mathematical result, not a solution of Erdős Problem 699.

Read `erdos699_continuation_2026-09-12.md` for the Japanese proof writeup,
corrections to the supplied note, exact scope of the computations, and remaining gaps.

The continuation proves, with the stated elementary arguments and finite certificates,
that any counterexample at the smaller index i=3 must satisfy

    n = 2^u M,  u >= 43,  M odd,  M^3 < 2^(u+1).

It also gives an unconditional n^(3/4) lower bound for the gcd when i=3,
and excludes the branches where either normalized adjacent modulus is a prime power.
The two-modulus condition alone does not close the unbounded case.

## Replay the finite certificates

Python standard library only, with assertions enabled (do not use `python -O`):

```text
python replay_certificate.py i3_original_replay.json i3_u42.json
```

The verifier independently reconstructs all CRT roots and checks every odd M
in the indicated bounds. All prime factors are proved by recursive elementary
Lucas certificates, using only integer modular exponentiation and gcd.

## Regenerate and audit

Generation and symbolic auditing were run with Python 3.14.3 and SymPy 1.14.0:

```text
python sieve_i3.py --original --max-u 12 --output i3_original_replay.json
python sieve_i3.py --max-u 42 --output i3_u42.json
python make_certificate.py i3_original_replay.json i3_u42.json
python replay_certificate.py i3_original_replay.json i3_u42.json
python audit_algebra.py
```

`AlgebraCertificates.lean` verifies three algebraic identities only.
It was checked using Lean 4.33.0-rc1 and Mathlib v4.33.0-rc1
(Mathlib commit 79d0395a1825a6264ad5d269e35e60537518955e).
From a matching Mathlib project, run:

```text
lake env lean /absolute/path/to/AlgebraCertificates.lean
```

`verification_lean.txt` records the axiom output. The entire mathematical
argument and the finite verifier are not formalized in Lean.

`explore_descent.py` and `explore_invariants.py` are reproducible exploratory
calculations; they are not needed to replay the finite certificates.

The original supplied note is preserved as `source_progress.md`.
No claim of literature priority is made.
