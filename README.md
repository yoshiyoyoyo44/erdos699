# Erdős 699 — 2026-09-12 continuation

This is a partial mathematical result, not a solution of Erdős Problem 699.

Read **`discriminant_continuation.md` for the latest Japanese proof writeup**.
It proves the assertion for **every smaller index i >= 205**, using a general
discriminant formula, two stated published prime estimates, and finite certificates
checked with rational intervals and deterministic integer arithmetic.
The previous provisional i >= 304 computations are not used.

The remaining smaller indices are 3 <= i <= 204; the problem is not solved.
Further Lean verification is deferred at the user's request.

The latest i=3 continuation is **`i3_2adic_and_square_continuation.md`**.
It proves, for a putative counterexample with even j=2^v J (J odd),

    2^(4v) M^3 < 2^(u+1),  hence v <= floor(u/4).

For odd j, put w=max(v_2(j-1),v_2(n-j-1)); it proves 2^w M^3 < 2^u.
It also completely classifies the integer-square cases of j(n-j)/(n-1)
when n=3*2^u: only (n,j)=(96,20),(768,118) occur, and both are excluded.
Together with the preceding proof for n=2^u, this rules out the square
branches for M=1 and M=3 without an upper bound on u.

Audit these new identities and the finite arithmetic in the classification:

```text
python audit_i3_2adic_square.py
```

`erdos699_continuation_2026-09-12.md` preserves the preceding continuation,
corrections to the supplied note, and the earlier i=3 finite certificates.

The continuation proves, with the stated elementary arguments and finite certificates,
that any counterexample at the smaller index i=3 must satisfy

    n = 2^u M,  u >= 43,  M odd,  M^3 < 2^(u-2).

It also gives an unconditional n^(3/4) lower bound for the gcd when i=3,
and excludes the branches where either normalized adjacent modulus is a prime power.
The two-modulus condition alone does not close the unbounded case.
`i3_square_branch.md` additionally excludes n=2^u when j(n-j)/(n-1)
is an integer square, by a proof without an upper bound on u.

## Replay the new large-index proof

Python standard library only, with assertions enabled:

```text
python replay_large_indices.py
```

This reconstructs all 38,025 checked intervals for 205 <= i <= 899,
checks the analytic tail for i >= 900, independently sieves prime gaps,
and eliminates the final 12 residue pairs. It relies on the two published
prime estimates explicitly quoted in the proof, not on unrecorded gap data.

To regenerate the certificates (NumPy for the prime sieve generator), or audit
the discriminant identities (SymPy):

```text
python certify_large_indices.py
python certify_prime_gaps.py
python audit_discriminant.py
```

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
`explore_square_parameters.py` tests a proposed broader square exclusion
after removing the special shape of n. Its finite search is not used as a proof.

The original supplied note is preserved as `source_progress.md`.
No claim of literature priority is made.
