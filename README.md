# Erdős 699 — 2026-09-12–19 continuation

This is a partial mathematical result, not a solution of Erdős Problem 699.

**2026-09-19 続編：全六ブロックを合わせた桁和の下界を証明しました。**
4∣j のとき、j 側と n−j 側で桁和2を取る加数はそれぞれ高々一つです。
これにより、T=1 を含めて総桁和≥8ω(T)+7ω(Q₁)+6ω(Q₂)−4 が必要になります。
桁和を別の素数での繰り上がりに移す補題も証明し、6〜256の各偶数桁和について
素数 p の一部の合同類を排除する8,127個の分割証明書を追加しました。
γ=3、3∤j では、奇数 j の桁和6も排除し、偶数 j の一部では下界を16以上に強めました。
[証明と残る障害](i3_global_digit_constraints_2026-09-19.md)・
[検算器](audit_i3_global_digit_constraints.py)・
[全証明書](verification_i3_global_digit_constraints.json)。完全解決には至っていません。

```text
python -X utf8 audit_i3_global_digit_constraints.py
```

**2026-09-19：桁和6の排除と、条件付きの桁和12の下界を証明しました。**
v₂(j)≥3 なら T のどの素因数でも対応する商の桁和6は不可能です。
さらに γ=3、3∤j なら、5以外の各素因数で桁和≥12、5では桁和≥8となります。
桁和8の中心への整除性には添付メモで抜けていた p=5,γ=3 の例外を明記し、
通常の整除性を p≡3 (mod 8) にも拡張しました。
素数冪 T=5^e の偶数 j・桁和4では、u の奇数部分が7以下の場合を全て排除しています。
[新しい証明と修正](i3_low_digit_continuation_2026-09-19.md)と
[再現用検算](audit_i3_low_digit_continuation.py)を追加しました。
i=3 全体、T=1、一般の非平方の分岐は未解決です。

```text
python -X utf8 audit_i3_low_digit_continuation.py
```

**2026-09-15 追加：** [新しい2つの添付ZIP](incoming_2026-09-15/README.md)を原本のまま公開しました。
ユーザーの依頼により今回は検算していません。以下の証明済み結果とは区別しています。

**成果の全体像と今後の方向：[これまでの成果と、次に進む五つの方向](STATUS_AND_DIRECTIONS.md)**

**2026-09-14：追加の3種類の資料を検証・統合し、その先の一般的な制約を証明しました。**
i=3 では、4|j のとき T の素因数で対応する商の桁和が4となるものは高々一つです。
二つ存在すると平方剰余の相互法則に矛盾します。純粋冪の W の式も一般の M に拡張し、
添付の弱い条件を満たす u=613+2028k の無限族は、分割した式を使って法53で全て排除しました。
[全桁・相互法則・W の新稿](i3_digit_reciprocity_and_W_continuation.md)。

i=119 の Hankel 案では、共通因子を定数まで明示し、全ての最大小行列式と局所付値を
一般次数で証明しました。固定した中央からの差についての係数 gcd の上界も得ています。
一方、中央の成長次数を全ての j,y に拡張する一般次数の予想には、r=2 の無限反例族を示しました。
r=60 の一様な g₆₀≪n³⁰ は未証明です。
[Hankel 還元の証明と残る上界](i119_hankel_content_continuation.md)。
今回も i=3・i=119 全体や問題699の完全解決は主張していません。

さらに解決作業を進め、**i=119ではn≤10^87の全範囲を排除**しました。
資料で探索段階だったA=100の近接計算を、213万組の厳密な不等式と全指数の還元で証明し、
その下も62区間と41組のKummer条件で閉じています。
[i=119の続編](i119_a100_continuation.md)。n>10^87は残っています。

二つの新資料を統合・検証し、成立範囲を **全ての i≥120、および i=96,97,100,101** へ広げました。
追加の96・100・120は、Matveevの定理による指数上限、74,976組の近似不等式、
最後の432組の有限排除を、独立した整数・有理数の検証器で確認した結果です。
詳細は [新資料の統合と臨界添字の証明](critical_indices_and_handoff_integration.md) を参照してください。

i=3 の最新資料も検証し、そこで未解決だった **g=13 の56ケースを全て排除**しました。
偶数 j の必要条件は **u≥4v₂(j)+14** です。g=10,…,13 の5099ケースを独立に再検証し、
最後の56曲線では Magma の完全な群と全整数点計算を使用、245点を整数演算で検算しました。
[g=13と降下案の検証](i3_gap13_and_descent_continuation.md)には、
有限個の合同式が止まる理由の証明と、降下式が既存の因子積に一致することも記録しています。
主枝全体の無限降下は未完成です。

前回までに、二つの追加資料を統合し、中心側の w と添字側の λ それぞれについて、
T や指数を分岐せずに一つの楕円曲線へ還元しました。
これにより、任意の固定 K>0 に対し min{j,n/2−j}≤K n^(3/4) の候補は有限個と証明しています。
さらに5曲線の整数点計算により、主要分岐の必要条件は
c=n/2−j>125^(1/4)Q^(3/4)、j>2^(3/2)Q^(3/4) に強まりました。
i=3 の u≥49、A,B,C≥11 などの既存成果も引き継いでいます。
残る添字は **3≤i≤119、ただし96,97,100,101を除く**。i=3 の一般の非平方の枝も残っています。
既知の S-part 定理と判別式から、i≥5 の反例候補全体が有限個であることも確認しました。
その有限性は上限の具体値や、候補が0個という結論を与えません。
詳細な優先順位・障害・検証の保証区分は上の文書を参照してください。

Quick links: [overall status and directions](STATUS_AND_DIRECTIONS.md) ·
[global digit bounds and transfer certificates](i3_global_digit_constraints_2026-09-19.md) ·
[latest low-digit proofs and correction](i3_low_digit_continuation_2026-09-19.md) ·
[preceding digit/reciprocity proof](i3_digit_reciprocity_and_W_continuation.md) ·
[new Hankel/content proof](i119_hankel_content_continuation.md) ·
[latest i=119 proof](i119_a100_continuation.md) ·
[latest critical-index proof](critical_indices_and_handoff_integration.md) ·
[latest i=3 gap proof](i3_gap13_and_descent_continuation.md) ·
[interval proof](interval_valuation_continuation.md) ·
[direct-curve proof](i3_direct_center_and_endpoint_curves.md) ·
[digit integration](i3_integrated_digits_and_center.md) ·
[fixed-block proof](i3_boundary_and_fixed_blocks.md) ·
[integrated nonsquare proof](i3_nonsquare_merged_continuation.md) ·
[complete artifact ZIP](erdos699_continuation_2026-09-12.zip).

The latest 2026-09-14 notes are **`i3_digit_reciprocity_and_W_continuation.md`**
and **`i119_hankel_content_continuation.md`**. They prove additional necessary
conditions and exact general identities; they do not solve i=3 or the remaining
i=119 tail. The inherited complete finite-exclusion ranges remain unchanged.

```text
python audit_i3_digit_reciprocity.py
python audit_i119_hankel.py
```

Read **`critical_indices_and_handoff_integration.md` and
`i3_gap13_and_descent_continuation.md` for the latest Japanese continuations**.
The first certifies i=96,100,120 through a cofactor bound and a complete
bounded-coefficient close-power calculation. Its initial exponent bound uses
Matveev's theorem; 435 prime pairs and 74,976 inhomogeneous cases are replayed with
independent 320-bit rational logarithm intervals. All 432 remaining finite pairs
are excluded by Kummer congruences.

The second raises the even-j bound to u>=4*v2(j)+14. Its 5,099 additional cases
use congruences and factorizations, with 56 complete Magma integral-point
calculations closing g=13. A separate audit shows why the proposed descent
still lacks a preserved second divisibility condition. The preceding g<=9
proof and its correction of the two false Pell valuation identities remain available.

```text
python replay_near_collisions.py
python replay_critical_indices.py
python replay_i3_gap_layers.py
python replay_i3_gap13.py
python audit_i3_descent.py
python replay_near_collisions_a100.py
python replay_i119_finite.py
```

**`interval_valuation_continuation.md` is the preceding index continuation**.
The exact formula v_p(binom(n,i)) = sum_e [n mod p^e < i mod p^e] gives
uniform upper bounds on integer intervals. Combined with the discriminant lower
bound and a proved infinite tail, it certifies i=97,101 and every i from 121 to 204.
Together with the earlier theorem, it covered all i>=121.
Those 86 indices use no Magma or external prime estimates; the inherited
i>=205 theorem retains its two published prime-estimate dependencies.

```text
python replay_interval_indices.py
python replay_large_indices.py
```

That certificate contains 11,521 intervals and 830 small-range pairs.
Its replay uses independent 144-bit outward-rounded logarithms and a complete
standard-library sieve. The infinite tails are proved analytically, not sampled.

**`i3_direct_center_and_endpoint_curves.md` is the preceding continuation**.
Eliminating n gives one nonsingular elliptic curve for each fixed center cofactor w,
and one for each fixed endpoint cofactor lambda=rho*(rho-delta1)/Q. This proves
finiteness in each bounded-cofactor range without splitting T or the exponent.
As a consequence, for every fixed K>0, only finitely many candidates satisfy

    min(j,n/2-j) <= K*n^(3/4).

An elementary doubling argument also proves that every center curve has positive
rank, so a rank-zero exclusion strategy cannot apply to this family.
Five Magma runs with proved full Mordell--Weil groups exclude w=61,55,37 in their
respective branches and lambda=2 in every branch (the delta1=3 endpoint case is
excluded modulo 3). The new w lower bounds are 125,119,229. Integer-point
completeness depends on Magma; the general finiteness proof uses Siegel's theorem.
An additional w=317 attempt timed out and is explicitly excluded from these claims.

```text
python audit_i3_center_curve.py
```

This checks nine symbolic identities and discriminants, exact arithmetic for all
55 returned points, both-sign inverse maps, and the new residue deductions.
The source, raw responses, and the incomplete attempt are preserved separately.

**`i3_integrated_digits_and_center.md` is the preceding Japanese continuation**.
It integrates both new attachments, proves the general-T endpoint bounds, and derives

    r = (4c^2-1)/Q1,  w = (r+delta1)(r-3delta1)/(4Q),  c = n/2-j,
    T | (w-delta1^2*delta2),  gcd(T,(w-delta1^2*delta2)/T) = 1,
    w = (delta*A-2*s)(delta*B*C-2*A*a*b),
    w = delta1^2*delta2*(1-4c^4) (mod n/2).

The degenerate value w=delta1^2*delta2 is excluded for every M by an elementary
factorization. The remaining fixed-w cases map to finitely many nonsingular
Mordell curves, so Siegel's theorem proves finiteness for each fixed bound on w.
That earlier note did not enumerate the integer points; the five completed
calculations in the latest note are described above.
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

After the new critical-index certificate, the remaining smaller indices are
3 <= i <= 119, excluding 96,97,100,101; the problem is not solved.
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
