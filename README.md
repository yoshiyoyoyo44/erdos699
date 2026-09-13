# Erdős 699 — 2026-09-12–13 continuation

This is a partial mathematical result, not a solution of Erdős Problem 699.

**成果の全体像と今後の方向：[これまでの成果と、次に進む五つの方向](STATUS_AND_DIRECTIONS.md)**

2026-09-13の二つの追加資料を統合し、Kummer の全桁条件を一般の T に整理しました。
新しく、中心距離 c=n/2−j から正の奇数 w を導入し、T が w−δ₁²δ₂ の単約数になることと、
任意の固定 W₀ に対して w≤W₀ の候補が有限個になることを証明しています。
主要分岐では c>61^(1/4)Q^(3/4) と、一般の T で j>2^(5/4)T^(1/4)Q^(3/4) が必要です。
全ての i≥205、i=3 の u≥49、A,B,C≥11 などの既存成果も引き継いでいます。
三因子と w がともに増える一般の場合、および4≤i≤204は残ります。
詳細な優先順位・障害・検証の保証区分は上の文書を参照してください。

Quick links: [overall status and directions](STATUS_AND_DIRECTIONS.md) ·
[latest integration and center proof](i3_integrated_digits_and_center.md) ·
[fixed-block proof](i3_boundary_and_fixed_blocks.md) ·
[integrated nonsquare proof](i3_nonsquare_merged_continuation.md) ·
[complete artifact ZIP](erdos699_continuation_2026-09-12.zip).

Read **`i3_integrated_digits_and_center.md` for the latest Japanese continuation**.
It integrates both new attachments, proves the general-T endpoint bounds, and derives

    r = (4c^2-1)/Q1,  w = (r+delta1)(r-3delta1)/(4Q),  c = n/2-j,
    T | (w-delta1^2*delta2),  gcd(T,(w-delta1^2*delta2)/T) = 1,
    w = (delta*A-2*s)(delta*B*C-2*A*a*b),
    w = delta1^2*delta2*(1-4c^4) (mod n/2).

The degenerate value w=delta1^2*delta2 is excluded for every M by an elementary
factorization. The remaining fixed-w cases map to finitely many nonsingular
Mordell curves, so Siegel's theorem proves finiteness for each fixed bound on w.
No new complete integer-point enumeration or Magma run is claimed.
The attached relaxed infinite family proves that the weakened factor identities
and high v2(n) alone cannot bound min(A,B,C); every member fails the genuine
normalization and has an odd common prime divisor.

```text
python audit_i3_integrated_digits.py
```

This audits 25 symbolic identities/divisibilities, 346,698 quotient-lift cases,
227,250 signed-digit membership cases, 1,500 signed gaps, the obstruction family,
and the new center congruences. The unbounded statements are proved in the note;
finite checks do not replace those proofs. Both attachments are preserved in
`source_direction2_progress_2026-09-13.md` and
`source_kummer_all_digits_progress_2026-09-13.md`.

**`i3_boundary_and_fixed_blocks.md` is the preceding Japanese continuation**.
It proves a general reduction: fixing any one of the residue blocks A, B, C
gives finitely many nonsingular elliptic curves. Siegel's theorem then implies
that, for every fixed F, only finitely many candidates have min(A,B,C) <= F.
This does not supply a uniform F or solve the case where all three blocks grow.

The new integer-ratio identities give delta1*delta2*C > 4*T by an elementary proof.
Two boundary quartics exclude the previously remaining B=1 branch at M=1,
using Magma's complete integer-point routines with proved full Mordell--Weil
groups. Consequently omega(Q2) >= 3 now holds for **every M**.
The additional fixed-block audits exclude A,B,C in {5,7,9}, giving **A,B,C >= 11**.
The input covers 196 parameter cases; periodic congruence certificates already
exclude 38/42, 60/68, and 10/16 cases for B=5,7,9 respectively.

```text
python audit_i3_fixed_blocks.py
```

This checks all symbolic identities, parameter coverage, periodic congruence
certificates, transcript provenance, and the exact arithmetic of returned
points. Completeness of the Mordell--Weil groups and integer-point lists still
depends on Magma 2.29-10; the Python audit does not reprove those steps.
The detailed note gives the exact dependencies and commands to rerun Magma.

**`i3_nonsquare_merged_continuation.md` is the preceding integrated writeup**.
It merges the supplied beyond-GitHub handoff with the previous local results,
corrects the overloaded C notation, and proves the previously missing integer
quotients without assuming gcd(B,g)=gcd(C,h)=1. It also gives stronger size and
2-adic bounds, and proves omega(Q2) >= 3 for every remaining branch with M > 1.
The original handoff is preserved byte-for-byte in
`source_nonsquare_handoff_2026-09-12.md`.

The finite i=3 certificates now exclude **every u <= 48** under the established
necessary conditions. The extension checks all 75,046 pairs (u,M) for 43 <= u <= 48,
excludes all 595 first-congruence candidates, and recursively verifies 177,312
primes using a standard-library-only replay. Thus a counterexample must satisfy

    n = 2^u M,  u >= 49,  M odd,  M^3 < 2^(u-2).

The branch-specific bounds in the integrated note are stronger still.
The additional integer quotients do not yet give a self-similar infinite descent.

```text
python audit_i3_nonsquare_lifts.py
python replay_certificate.py i3_u43_to_u48.json --primes prime_certificates_u48.json --output verification_u48.json
```

`discriminant_continuation.md` proves the assertion for **every smaller index i >= 205**, using a general
discriminant formula, two stated published prime estimates, and finite certificates
checked with rational intervals and deterministic integer arithmetic.
The previous provisional i >= 304 computations are not used.

The remaining smaller indices are 3 <= i <= 204; the problem is not solved.
Further Lean verification is deferred at the user's request.

The preceding i=3 continuation is **`i3_all_square_branches.md`**.
It extends the exclusion of integer-square j(n-j)/(n-1) to **every odd M**,
using the previously established necessary conditions for a counterexample.
The new lemma is proved for all u >= 16, without an upper bound on u or M.
It also records a necessary quartic square identity for a nonsquare branch
and explains why the associated Vieta step does not give a positive descent.
The nonsquare branches remain unresolved; this is not a complete proof.

```text
python audit_i3_all_square.py
```

The previous continuation is **`i3_2adic_and_square_continuation.md`**.
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

The previous continuation established, with the stated elementary arguments and
finite certificates, the following bound, now superseded by u >= 49 above:

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
python replay_certificate.py i3_u43_to_u48.json --primes prime_certificates_u48.json --output verification_u48.json
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

To regenerate the new extension and its separate prime certificates:

```text
python extend_i3_certificate.py
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
