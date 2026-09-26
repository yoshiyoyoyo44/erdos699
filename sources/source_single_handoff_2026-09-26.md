# Erdős Problem 699 — Single Handoff (GitHub assumed available)

Date: 2026-09-26 JST  
Repository: `yoshiyoyoyo44/erdos699`  
GitHub baseline checked: `5024fc5fb1beec81e4a8c1d2eee4ff4230c58cc4`  
Status: research handoff. No claim of complete solution to Problem 699, nor complete solution of `i=3`, `i=4`, or `i=28,31,34`.

---

## 0. How the next AI should use this document

This note is intentionally **not self-contained with respect to the whole GitHub repository**.

Assume the next AI can read GitHub. Start by reading:

1. `docs/STATUS.md`
2. `research/general/weighted_cover_and_integration_2026-09-26.md`
3. `archive/attachments/incoming_2026-09-26/erdos699_coupled_factor_constraints_2026-09-26/REPORT.md`
4. `research/general/critical_indices_and_handoff_integration.md`
5. for `i=3`:
   - `research/i3/i3_nonsquare_merged_continuation.md`
   - `research/i3/i3_integrated_digits_and_center.md`
   - `research/i3/i3_quadratic_twist_and_kummer_support_2026-09-21.md`
   - `research/i3/i3_growing_gap_and_auxiliary_frey_2026-09-21.md`
   - `research/i3/i3_uniform_digit_descent_2026-09-23.md`

The purpose of the present note is to record **what has been added beyond GitHub HEAD 5024fc5**, what was audited, what is still tentative, and what the next research target should be.

Problem statement must remain the original one:

\[
1\le i<j\le n/2,\qquad
\exists p\ge i:\quad p\mid\gcd\!\left(\binom ni,\binom nj\right).
\]

Do **not** replace `p>=i` by the stronger false variant `p>i`.

---

## 1. Current global status from GitHub

At commit `5024fc5` the repository records:

\[
\boxed{i=1,2,29\quad\text{and}\quad i\ge35}
\]

as solved for all `n,j`.

Therefore the remaining indices are

\[
\boxed{3\le i\le34,\qquad i\ne29},
\]

i.e. exactly **31 indices**.

The 2026-09-26 weighted-cover result closed `i=29` and `35<=i<=119`; combined with the older `i>=120` result this produces the range above.

No new index is fully solved in the work recorded below.

---

# Part I. Common structure for the remaining 31 indices

## 2. Cofactor-defect inequality

Fix an unresolved `i`.

Let

\[
A=\binom ni,\qquad m=\pi(i-1).
\]

For each prime `p<i`, define

\[
E_p=\max_{0\le r<i}v_p(n-r),
\]

choose any maximizing row

\[
r_p\in\operatorname{argmax}_{0\le r<i}v_p(n-r),
\]

and define

\[
a_p=\frac{n-r_p}{p^{E_p}}.
\]

Set

\[
h=i-1,\qquad
b=\left\lceil\frac{2h}{3}\right\rceil,\qquad
d=3b-h,\qquad
S=\frac{b(b+1)}2,
\]

and

\[
i_<:=\prod_{p<i}p^{v_p(i)}.
\]

From the GitHub weighted-cover inequality for a counterexample,

\[
Q^d\le4^{-S}n^{3S},
\]

where `Q` is the `p>=i` part of `A`.

From the small-prime valuation estimate,

\[
Q\ge
\frac{i_<\left(\prod_{p<i}a_p\right)(n-i+1)^i}{i!\,n^m}.
\]

Hence every counterexample satisfies

\[
\boxed{
\prod_{p<i}a_p
\le
\frac{i!}{i_<4^{S/d}}
\left(\frac{n}{n-i+1}\right)^i
n^{\beta_i},
}
\]

where

\[
\boxed{
\beta_i=\frac{3S}{d}-(i-m).
}
\]

This is the **cofactor-defect inequality**.

It is not in GitHub HEAD as a named theorem in this form.

Important checked special values:

\[
\beta_3=\frac14,\qquad
\beta_4=1,
\]

and

\[
\boxed{\beta_{28}=\beta_{31}=\beta_{34}=0.}
\]

For the remaining `i>=5`, one has

\[
m-\beta_i>1.
\]

---

## 3. Collision bound for the maximizing rows

Let

\[
R=\{r_p:p<i\},\qquad \rho=|R|.
\]

If multiple small primes share the same maximizing row, grouping them row-by-row gives

\[
\boxed{
\prod_{p<i}a_p\ge(n-i+1)^{m-\rho}.
}
\]

Combined with the cofactor-defect inequality, this forces

\[
\rho\ge m-\beta_i-o(1)
\]

for large `n`.

Consequences:

- if `beta_i<1`, then for sufficiently large counterexamples all `r_p` are distinct;
- for all unresolved `i>=5`, because `beta_i<2`, at most one collision among the maximizing rows can persist asymptotically.

Interpretation: a counterexample must place the largest powers of the small primes in almost all distinct rows of the short interval

\[
n,n-1,\dots,n-i+1.
\]

This suggests a multi-prime near-power cluster attack.

---

## 4. Max-row polynomial and a second proof of finite counterexample sets

Define

\[
P_R(X)=\prod_{r\in R}(X-r).
\]

Let

\[
q_p=p^{E_p}.
\]

For each row `r`, the product of the `q_p` assigned to that row divides `n-r`, hence

\[
\prod_{p<i}q_p\mid P_R(n).
\]

All these `q_p` are supported on primes `<i`, so if `S_i={p:p<i}`,

\[
[P_R(n)]_{S_i}\ge\prod_{p<i}q_p.
\]

Since

\[
q_p=\frac{n-r_p}{a_p},
\]

the cofactor-defect inequality implies

\[
\boxed{
[P_R(n)]_{S_i}\gg_i n^{m-\beta_i}.
}
\]

For every unresolved fixed `i>=5`,

\[
m-\beta_i>1.
\]

Using the Bugeaud-Evertse-Győry `S`-part theorem for a squarefree polynomial with at least two distinct roots gives

\[
[P_R(n)]_{S_i}\ll n^{1+\varepsilon |R|}.
\]

Choosing small enough `epsilon` yields a contradiction for sufficiently large `n`.

Therefore:

\[
\boxed{\text{for each fixed unresolved }i\ge5,\text{ the counterexample set is finite}.}
\]

This is a **new alternate proof** of finite counterexample sets. GitHub already had finite counterexample sets for fixed `i>=5` by another route, so do not present this as the first proof of finiteness.

The key value is structural: it localizes the obstruction to the maximizing rows of small primes.

---

# Part II. Effective progress for i = 28, 31, 34

## 5. Explicit effective bound

For

\[
i\in\{28,31,34\},
\]

we have

\[
\beta_i=0.
\]

For `n>=68`,

\[
\frac{n}{n-i+1}\le2,
\]

and therefore

\[
\prod_{p<i}a_p
\le2^i i!
\le2^{34}34!
<2^{162}.
\]

In particular,

\[
a_2,a_3<2^{162}.
\]

### Case 1: `r_2=r_3`

Then `2^{E_2}` and `3^{E_3}` both divide `n-r`, hence

\[
a_2a_3
=
\frac{(n-r)^2}{2^{E_2}3^{E_3}}
\ge n-r.
\]

Thus

\[
n<2^{162}+33.
\]

### Case 2: `r_2\ne r_3`

Then

\[
a_22^{E_2}-a_33^{E_3}=r_3-r_2,
\qquad
0<|r_3-r_2|\le33.
\]

Set

\[
\Lambda=\frac{a_2}{a_3}2^{E_2}3^{-E_3}-1.
\]

Then

\[
0<|\Lambda|
\le\frac{33}{n-33}
<\frac{66}{n}.
\]

With

\[
t=\log_2 n,
\]

we have `E_2,E_3<=t`.

Apply the positive-rational Matveev bound to at most the three rationals

\[
2,\quad3,\quad a_2/a_3.
\]

The height parameters may be bounded by

\[
A_1=\frac7{10},\qquad
A_2=\frac{11}{10},\qquad
A_3=114.
\]

A safe constant is

\[
C=13\,200\,000\,000\,000
\]

with

\[
\log|\Lambda|>-C(1+\log t).
\]

Combining with the upper bound gives

\[
\frac23t<5+C(1+\log t).
\]

For

\[
t_0=10^{15},
\]

define

\[
f(t)=\frac23t-5-C(1+\log t).
\]

Using `log 10 < 7/3`,

\[
f(t_0)>
\frac23\,10^{15}-5-36C>0.
\]

Also

\[
f'(t)=\frac23-\frac Ct>0
\qquad(t\ge10^{15}).
\]

Hence `t>=10^15` is impossible.

Therefore

\[
\boxed{
i\in\{28,31,34\}\text{ counterexample}
\Longrightarrow
n<2^{10^{15}}.
}
\]

This is an actual explicit effective bound, though far too large for naive enumeration.

This theorem does **not** solve these three indices.

---

# Part III. i = 4: global classification and six-prime support

## 6. Correct definition of i=4 counterexample

For `i=4`, a counterexample means

\[
5\le j\le n/2
\]

and

\[
\gcd\!\left(\binom n4,\binom nj\right)
\]

has no prime divisor `p>=4`. Since the only prime `<4` are `2,3`, equivalently there is no common prime `p>=5`.

Important correction: one earlier draft accidentally described the counterexample condition in the opposite direction in one introductory sentence. The proofs below use the correct condition.

---

## 7. Large-prime row decomposition

For `s=0,1,2,3`, put

\[
R_s=
\frac{n-s}{2^{v_2(n-s)}3^{v_3(n-s)}}.
\]

Thus `R_s` is the entire `p>=5` part of `n-s`.

For a counterexample, Kummer gives

\[
\boxed{
R_s\mid\prod_{k=0}^{s}(j-k).
}
\]

Define

\[
B_{s,k}=\gcd(R_s,j-k),\qquad0\le k\le s.
\]

Then

\[
R_s=\prod_{k=0}^{s}B_{s,k}.
\]

All nontrivial `B_{s,k}` are pairwise coprime across distinct positions.

The column and diagonal products satisfy the standard GitHub divisibilities.

For `n>=10^87`, the GitHub two-position theorem gives

\[
\boxed{
B_{s,k}B_{t,l}\le3(n-3)
\qquad((s,k)\ne(t,l)).
}
\]

---

## 8. Exclusion of three rational ratios

For any `i=4` counterexample,

\[
\boxed{
j\ne n/2,\qquad
j\ne n/3,\qquad
j\ne n/6.
}
\]

Proof template: if `n=kj`, multiply the row-divisibility by `k^{s+1}` and use `n≡s mod R_s` to get

\[
R_s\mid\prod_{a=0}^{s}(s-ka).
\]

For `k=2,3,6`, specific rows force the relevant `R_s` to be tiny, contradicting `n>=10`.

This argument is valid for all allowed `n`, not just large `n`.

---

## 9. Global classification of the maximizing rows of 2 and 3

Let `r_2,r_3` be arbitrary rows achieving

\[
\max_{0\le r\le3}v_2(n-r),
\qquad
\max_{0\le r\le3}v_3(n-r).
\]

If both are nonzero, maximality implies

\[
2^{v_2(n)}3^{v_3(n)}\mid6.
\]

Since `R_0|n` and `R_0|j`, the reduced denominator of `j/n` divides `6`, hence

\[
j/n\in\{1/2,1/3,1/6\},
\]

all excluded above.

Therefore for **every choice** of maximizing rows,

\[
\boxed{
0\in\{r_2,r_3\}.
}
\]

If both `r_2=r_3=0`, then exact row formulas give

\[
R_1=n-1,\qquad
R_2=(n-2)/2,\qquad
R_3=(n-3)/3.
\]

A weighted column/diagonal inequality yields

\[
R_1^3R_2^2R_3
\le
j^2(j-1)(n-j)^2(n-j-1)
\le
\frac{n^4(n-2)^2}{64}.
\]

Thus

\[
16(n-1)^3(n-3)\le3n^4,
\]

but for `n>=8` the left minus right is

\[
13x^4+320x^3+2880x^2+11104x+15152>0,
\qquad x=n-8.
\]

Contradiction.

So exactly one of `2,3` has row 0 as maximizing row.

Tie analysis then sharpens this to:

\[
\boxed{
n\bmod36\in
\{4,8,9,12,16,18,20,27,28,32\}.
}
\]

This classification is valid for all `i=4` counterexamples, not only `n>=10^550`.

---

## 10. Direct transfer of five i=4 classes to i=3

Using

\[
4\binom n4=(n-3)\binom n3
\]

and

\[
3\nmid\binom n3
\iff
n\bmod9\in\{3,4,5,6,7,8\},
\]

the classes

\[
\boxed{
n\bmod36\in\{4,8,12,16,32\}
}
\]

have the property that an `i=4` counterexample `(n,j)` is automatically an `i=3` counterexample for the same `(n,j)`.

Therefore all existing `i=3` necessary conditions from GitHub apply, including

\[
n=2^uM,\qquad
u\ge51,\qquad
\frac{16000}{9}M^3<2^u
\]

(with the same external-dependence caveat as in GitHub),

and

\[
T\mid j
\]

with the standard `gamma` correction.

For even `j`:

\[
u\ge4v_2(j)+14.
\]

The genuinely `i=4`-specific classes remaining after this transfer are

\[
\boxed{
n\bmod36\in\{9,18,20,27,28\},
\qquad
3\mid\binom nj.
}
\]

---

## 11. New i=4 three-row splitting theorem

Assume now

\[
n\ge10^{87}.
\]

### Type A

Suppose row 0 is the unique maximizing row for `2`, hence `4|n`.

Let

\[
q=3^{\max_{0\le s\le3}v_3(n-s)}.
\]

The maximizing row for `3` is nonzero.

If

\[
\boxed{n-3>432q^4,}
\]

then each of rows

\[
s=1,2,3
\]

contains at least **two occupied positions** `B_{s,k}>1`.

### Type B

Suppose row 0 is the unique maximizing row for `3`, hence `9|n`.

Let

\[
q=2^{\max_{0\le s\le3}v_2(n-s)}.
\]

The maximizing row for `2` is nonzero.

If

\[
\boxed{n-3>2187q^4,}
\]

then again each of rows `1,2,3` has at least two occupied positions.

Hence in either case,

\[
\boxed{
\#\{p\ge5:p\mid\binom n4\}\ge6
}
\]

and more strongly

\[
\boxed{
\#\{p\ge5:p\mid(n-s)\}\ge2
\qquad(s=1,2,3).
}
\]

### Proof skeleton

Write

\[
c=
\begin{cases}
2&\text{Type A},\\
3&\text{Type B}.
\end{cases}
\]

Then for `s=1,2,3`,

\[
R_s\ge\frac{n-3}{cq}.
\]

If some row `s` has only one occupied position, then that occupied `B` equals `R_s`.

For every different row `t` and every position `(t,l)`,

\[
B_{t,l}
\le
\frac{3(n-3)}{R_s}
\le3cq.
\]

Since row `t` has `t+1` positions,

\[
R_t\le(3cq)^{t+1}.
\]

But also

\[
R_t\ge\frac{n-3}{cq}.
\]

Therefore

\[
n-3\le cq(3cq)^{t+1}.
\]

Choosing the smallest useful other row produces the constants

\[
72,\quad432,\quad243,\quad2187.
\]

The fourth-power hypotheses exclude singleton rows `1,2,3`.

An intermediate result is:

- Type A: if `n-3>72q^3`, rows 2 and 3 split;
- Type B: if `n-3>243q^3`, rows 2 and 3 split.

Together with at least one occupied position in row 1, this already gives at least five distinct primes `p>=5`.

---

## 12. Pure-power consequences

### 12.1 `n=2^u`

For `u>=2`, row 0 is the maximizing row for `2`.

For the `3`-power over rows `1,2,3`,

\[
q=3^{1+v_3(m)},
\]

where

\[
m=
\begin{cases}
u/2&u\text{ even},\\
(u-1)/2&u\text{ odd}.
\end{cases}
\]

Hence

\[
q\le\frac{3u}{2}.
\]

Since

\[
2^{289}<10^{87}\le2^{290}
\]

and

\[
2^{290}-3>2187\cdot290^4
>
432\left(\frac{3\cdot290}{2}\right)^4,
\]

and `2^u/u^4` is increasing for `u>=290`, the six-prime theorem applies for all

\[
\boxed{u\ge290}.
\]

Thus any `i=4` counterexample with `n=2^u`, `u>=290`, would require each of

\[
2^u-1,\quad2^u-2,\quad2^u-3
\]

to have at least two distinct prime divisors `p>=5`.

### 12.2 `n=3^a`

For `a>=2`, row 0 is maximizing for `3`.

For the `2`-power over rows `1,2,3`,

\[
q=2^{2+v_2(b)},
\]

where

\[
b=
\begin{cases}
a&a\text{ even},\\
a-1&a\text{ odd}.
\end{cases}
\]

Hence

\[
q\le4a.
\]

Since

\[
3^{182}<10^{87}\le3^{183}
\]

and

\[
3^{183}-3>2187(4\cdot183)^4,
\]

the six-prime theorem applies for all

\[
\boxed{a\ge183}.
\]

So any `i=4` counterexample with `n=3^a`, `a>=183`, forces each of

\[
3^a-1,\quad3^a-2,\quad3^a-3
\]

to have at least two distinct prime divisors `p>=5`.

The finite diagnostic script for these constants was independently rerun and passed.

---

# Part IV. i = 3 odd-j branch beyond GitHub HEAD

## 13. Existing GitHub setup

For an `i=3` counterexample write

\[
n=\gamma T2^u,\qquad M=\gamma T,
\]

with the standard `gamma` correction at `3`.

For odd `j`, use the six-block decomposition from GitHub:

\[
n-1=\delta_1RS,\qquad
(n-2)/2=\delta_2ABC,
\]

\[
j=TSBg,\qquad
y=TRCh,
\]

\[
j-1=RAa,\qquad
y-1=SAb,
\qquad y=n-j.
\]

Let

\[
\delta=\delta_1\delta_2.
\]

The common identities include

\[
T^2BCgh-A^2ab=\delta_1,
\]

\[
\delta_2ABC+1=\gamma T2^{u-1},
\]

\[
\delta A>2T^2gh.
\]

Let

\[
w=\max(v_2(j-1),v_2(y-1)).
\]

Then

\[
v_2(ab)=w+1.
\]

---

## 14. Odd-branch strengthening retained from the integrated work

The integrated work supplements the GitHub odd branch by carefully restoring the `3`-power in the primitive factorization, checking the `M=1` boundary, and tracking the sign twist of the auxiliary Frey curve.

The resulting connection between the two Frey-support quantities is

\[
\boxed{
R_{\rm odd}^2
=
R_E\,\mathcal Q\,F_{\rm odd}^2.
}
\]

This is the key new structural identity from the odd branch.

The exact definitions are those of the integrated note:

- `R_odd`: odd radical/support from the odd-branch Frey curve after primitive reduction;
- `R_E`: odd conductor-support quantity from the other Frey/elliptic curve;
- `mathcal Q`: the Kummer auxiliary-support quantity already appearing in GitHub;
- `F_odd`: the remaining odd factor produced by the primitive normalization.

The point is that the two previously separate support-growth mechanisms are no longer independent: they satisfy an exact multiplicative relation.

Combining the known lower bounds gives a necessary growth condition of the schematic form

\[
\boxed{
R_E\mathcal QF_{\rm odd}^2
\gg
\frac{u^2}{(\log u)^4}.
}
\]

This is **not yet a contradiction**. It is a lower bound on a product of moving support quantities. A complete proof still requires an upper bound or rigidity principle for the same product.

Do not claim the odd branch solved.

---

# Part V. What was actually audited

## 15. Mechanical checks completed

The following checks were done in the session that produced this handoff:

1. The two uploaded integrated-continuation markdown files were byte-identical / SHA-identical.
2. The `i=4` six-prime verification script was rerun successfully.
3. Its regenerated JSON matched the supplied JSON.
4. Exact integer checks confirmed:
   - constants `72,432,243,2187`;
   - 499 tested powers of `2`;
   - 299 tested powers of `3`;
   - `2^289<10^87<=2^290`;
   - `3^182<10^87<=3^183`;
   - both endpoint fourth-power inequalities.
5. The cofactor-defect algebra was rechecked.
6. The special beta-values `1/4`, `1`, and `0` for `i=3,4,28,31,34` were rechecked.
7. The Matveev constant chain for `i=28,31,34` was checked for internal consistency.
8. The `i=4` modulo-36 classification and the transfer of five classes to `i=3` were rechecked.
9. The six-prime proof was checked against the pairwise-position inequality from GitHub.

---

## 16. Important caveats

### 16.1 No new solved index

This handoff does **not** prove any of the remaining 31 indices completely.

### 16.2 `i=28,31,34`

The explicit bound

\[
n<2^{10^{15}}
\]

is meaningful, but the whole region below it has not been eliminated.

### 16.3 `i=4`

The global congruence classification is strong, but the five genuinely `i=4` classes remain.

The six-prime theorem is conditional on a bound of the form

\[
n-3>Cq^4.
\]

If the non-row-0 small-prime power `q` is as large as about `n^{1/4}` or larger, the theorem does not force full six-position splitting.

### 16.4 `i=3`

The exact support identity in the odd branch is a bridge, not a contradiction.

The central unsolved issue remains to convert all-digit Kummer information into a sufficiently strong uniform upper bound on the moving conductor/support quantities, or into a genuine descent available for every hypothetical counterexample.

### 16.5 External results

Several statements rely on external published theorems already used or cited in GitHub:

- Bugeaud-Evertse-Győry `S`-part theorem;
- Matveev-type explicit lower bounds for linear forms in logarithms;
- the external elliptic-curve / Thue-Mahler completeness inputs already documented in GitHub.

The present note does not reprove those external theorems.

---

# Part VI. Best next research directions

## 17. Priority 1 — finish i=4 through the occupied-position geometry

This now looks like the most concrete target.

Known for the large-`n` splitting regime:

- rows `1,2,3` each contain at least 2 occupied positions;
- all occupied `B_{s,k}` are pairwise coprime;
- every pair satisfies
  \[
  B_xB_y\le3(n-3);
  \]
- column products divide `j-k`;
- diagonal products divide `n-j-v`.

The next target is to prove that six occupied positions cannot simultaneously fit all column and diagonal capacity constraints.

This should be treated as a finite combinatorial/inequality classification over the triangular cells

\[
(s,k),\qquad 1\le s\le3,\ 0\le k\le s.
\]

Do not merely reuse pairwise bounds; use column and diagonal products simultaneously.

A successful result here could solve the entire large-`n` branch of `i=4`.

---

## 18. Priority 2 — treat the complementary large-q branch for i=4

The six-prime theorem fails only when the non-row-0 small-prime power satisfies roughly

\[
q\gtrsim n^{1/4}.
\]

This branch is itself extremely rigid.

Study separately:

- Type A:
  \[
  q=3^e\gtrsim n^{1/4};
  \]
- Type B:
  \[
  q=2^e\gtrsim n^{1/4}.
  \]

Since `q` divides one of `n-1,n-2,n-3`, this gives a near-pure-power equation

\[
n-r=a q
\]

with small `r` and relatively small cofactor `a`.

Combine this with the modulo-36 classification and the row-divisibility conditions.

This is likely the other half needed for a complete `i=4` proof.

---

## 19. Priority 3 — compress the explicit bound for i=28,31,34

The bound

\[
2^{10^{15}}
\]

is far too large.

Possible reductions:

1. use two or three near-power equations simultaneously instead of only `p=2,3`;
2. apply a Dujella-Pethő / continued-fraction reduction after Matveev;
3. exploit the fact that, for large `n`, the maximizing rows for all small primes are distinct;
4. combine several equations
   \[
   a_pp^{E_p}-a_qq^{E_q}=r_q-r_p
   \]
   sharing the same short set of row differences.

The real target is a **multi-prime near-collision lemma**, not independent two-prime estimates.

---

## 20. Priority 4 — i=3 odd branch: turn the support identity into a contradiction

Use

\[
R_{\rm odd}^2=R_E\mathcal QF_{\rm odd}^2.
\]

The next useful result would be any one of:

- an upper bound
  \[
  R_E\mathcal QF_{\rm odd}^2
  =o\!\left(\frac{u^2}{(\log u)^4}\right);
  \]
- a divisibility restriction forcing one factor to be bounded;
- a Kummer argument proving that large support forces a good digit-descent base;
- an incompatibility between the prime support of `F_odd` and that of `mathcal Q`.

This is the natural place to connect the odd-branch Frey work with the all-degree digit descent.

---

# Final status summary

As of this handoff:

\[
\boxed{i=1,2,29\text{ and }i\ge35\text{ are solved}}
\]

from GitHub.

The remaining indices are

\[
\boxed{3\le i\le34,\quad i\ne29}.
\]

New progress beyond GitHub HEAD 5024fc5:

1. cofactor-defect inequality for all remaining indices;
2. max-row polynomial formulation and alternate finite-counterexample proof for each fixed unresolved `i>=5`;
3. explicit effective bound
   \[
   n<2^{10^{15}}
   \]
   for `i=28,31,34`;
4. full-`n` maximizing-row classification for `i=4`;
5. exact ten residue classes modulo 36 for `i=4`;
6. transfer of five of those classes directly to `i=3`;
7. `i=4` three-row splitting theorem and six-large-prime necessary condition;
8. pure-power consequences for `2^u` (`u>=290`) and `3^a` (`a>=183`);
9. odd-`j`, `i=3` support identity
   \[
   R_{\rm odd}^2=R_E\mathcal QF_{\rm odd}^2.
   \]

No remaining index is completely solved by these additions.

The most promising immediate target is `i=4`: combine the six occupied positions with column/diagonal capacities, and separately handle the complementary branch where the non-row-0 small-prime power is at least on the order of `n^{1/4}`.
