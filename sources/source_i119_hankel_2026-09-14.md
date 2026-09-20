# Erdős Problem 699 — i=119 Hankel / maximal-minor handoff

Date: 2026-09-14
Reference baseline: `yoshiyoyoyo44/erdos699`, commit `f99cbce`.

**Status:** This note does **not** prove `i=119`. It records new verified reductions beyond the baseline and isolates the remaining lemma. Do not promote the unproved content bound below to a theorem.

## 0. Problem and inherited facts

Erdős Problem 699 asks whether, for every integer

\[
1\le i<j\le n/2,
\]

\[
D:=\gcd\!\left(\binom ni,\binom nj\right)
\]

has a prime divisor `p >= i`.

For `i=119`, the repository already proves the statement for `n <= 10^87`, but `n>10^87` remains open. The known discriminant argument gives a lower bound of order `n^(119/4)=n^29.75` for `D`, while a counterexample has only prime divisors `<119`, with the crude upper exponent `n^30`. The remaining issue is to save just over `n^(1/4)` in the small-prime upper bound, or equivalently strengthen the control of

\[
a:=\binom n{119}/D.
\]

The older `H(A)` / near-collision route is not used as an unproved uniform polynomial bound here.

## 1. Orbit coefficients and normalized coefficients

Write

\[
y=n-j,
\qquad
X_h=\binom j{119-h}\binom yh \quad (0\le h\le119).
\]

From the repository's orbit-coefficient identity, `a` divides every `X_h`.

Define the factorially normalized sequence

\[
Z_h:=(119-h)!\,h!\,X_h=(j)_{119-h}(y)_h,
\]

where `(x)_m=x(x-1)\cdots(x-m+1)` is the falling factorial.

Therefore

\[
\boxed{a\mid Z_h\qquad(0\le h\le119).}
\]

Hence every `r x r` minor formed from the `Z_h` is divisible by `a^r`.

This is the basic new invariant.

## 2. Hankel minors

For integers `r>=1` and shift `s`, define

\[
H_s^{(r)}:=\det\bigl(Z_{u+v+s}\bigr)_{0\le u,v<r}.
\]

Whenever all indices lie in `0,...,119`,

\[
\boxed{a^r\mid H_s^{(r)}.}
\]

Exact symbolic calculations for small `i,r` show, and the determinant factorization derivation supports, the degree formula

\[
\boxed{\deg H_s^{(r)}=ri-\binom r2.}
\]

For `i=119`, `r=60` this gives

\[
\deg H_s^{(60)}=60\cdot119-\binom{60}{2}=5370,
\]

so a single Hankel determinant gives only

\[
a\ll n^{5370/60}=n^{89.5}.
\]

The target is below exponent `89`, so one determinant alone misses by `1/2` in the exponent.

## 3. Maximal minors of a 60 x 61 Hankel block

Consider

\[
M=(Z_{u+v})_{\substack{0\le u<60\\0\le v\le60}}.
\]

It has 61 maximal `60 x 60` minors, indexed by the omitted column `t` (`0<=t<=60`). Every such minor is divisible by `a^60`.

A common polynomial factor `G` can be factored from all 61 minors. Its total degree is

\[
\boxed{\deg G=3\binom{60}{2}=5310.}
\]

After removal of `G`, the residual factor for omitted column `t` is

\[
\boxed{
R_t=\binom{60}{t}(j-60+t)_t\,(y-t)_{60-t}.
}
\tag{1}
\]

Equivalently,

\[
\boxed{
R_t=60!\binom{j-60+t}{t}\binom{y-t}{60-t}.
}
\tag{2}
\]

Thus

\[
\boxed{
a^{60}\mid G\cdot\gcd(R_0,R_1,\ldots,R_{60}).
}
\tag{3}
\]

This is the main reduction.

## 4. Content formulation

Define

\[
S_t:=\frac{R_t}{60!}
=\binom{j-60+t}{t}\binom{y-t}{60-t},
\qquad 0\le t\le60.
\]

Let

\[
P(z)=\sum_{t=0}^{60}S_t z^t.
\]

A Vandermonde calculation after the integer translation `z=1+w` gives the exact identity

\[
\boxed{
[w^k]P(1+w)
=
\binom{j-60+k}{k}
\binom{n-59}{60-k}
\qquad(0\le k\le60).
}
\tag{4}
\]

The change of coefficients induced by `z -> 1+z` is an integer unimodular transformation, hence preserves the gcd of the coefficient vector. Therefore

\[
\boxed{
\gcd_{0\le t\le60}S_t
=
\gcd_{0\le k\le60}
\left(
\binom{j-60+k}{k}
\binom{n-59}{60-k}
\right).
}
\tag{5}
\]

This converts the Hankel-minor content problem into a completely explicit gcd of 61 binomial-coefficient products.

A useful check is the Vandermonde sum

\[
\sum_{t=0}^{60}S_t=\binom{n-59}{60}.
\]

## 5. Large-prime local classification

The following local pattern has been derived for the residual content in the general `r`-version and specializes to `r=60`.

Let `p>2r-2` be prime, and let

\[
J=j\bmod p,\qquad Y=y\bmod p,
\qquad 0\le J,Y<p.
\]

Then

\[
\boxed{
p\mid \gcd_{0\le t\le r}S_t
\iff
J<r,\quad Y<r,\quad J+Y\ge r-1.
}
\tag{6}
\]

Moreover, in this situation,

\[
\boxed{
v_p\!\left(\gcd_tS_t\right)
=
\min\{v_p(j-J),v_p(y-Y)\}.
}
\tag{7}
\]

Consequently

\[
\boxed{
p^{v_p(\gcd S_t)}\mid n-(J+Y),
\qquad r-1\le J+Y\le2r-2.
}
\tag{8}
\]

For `r=60`, every prime `p>118` occurring in the residual content is therefore attached to one of the 60 integers

\[
n-59,\ n-60,\ldots,\ n-118.
\]

This is a strong Kummer-like localization for the new content invariant.

**Important:** the final global product bound obtained from (6)-(8) has not yet been proved.

## 6. Center case and the expected scale

For the symmetric case `j=y=x`, exact factorization for small `r` shows

\[
\gcd_{\mathbf Q[x]}(R_0,\ldots,R_r)
\propto
\prod_{s=\lfloor r/2\rfloor}^{r-1}(x-s),
\]

whose degree is

\[
\left\lceil\frac r2\right\rceil.
\]

This was checked exactly for `r=2,...,8`.

Thus for `r=60`, the center case naturally has residual polynomial growth degree `30`.

This is exactly the scale needed for `i=119`:

from (3), if one can prove a uniform explicit estimate

\[
\boxed{
g_{60}(j,y):=
\gcd_{0\le t\le60}
\binom{j-60+t}{t}\binom{y-t}{60-t}
\ \ll\ n^{30}
}
\tag{9}
\]

with a sufficiently controlled constant, then

\[
a^{60}\ll n^{5310+30}=n^{5340},
\]

hence

\[
a\ll n^{89}.
\]

Since

\[
\binom n{119}\asymp n^{119},
\]

this would give

\[
D=\binom n{119}/a\gg n^{30},
\]

which is exactly the critical exponent needed to beat the counterexample-side small-prime upper bound after comparing constants.

Therefore the current core target is precisely (9), not a larger finite search.

## 7. Related lower-rank / shifted-Hankel observations

For odd `i=2m-1`, exact symbolic calculations for `i=3,5,7` show that the two maximal `m x m` Hankel determinants

\[
H_0=\det(Z_{r+s}),\qquad H_1=\det(Z_{r+s+1})
\]

have a common polynomial factor `G` with

\[
H_0/G\propto(j)_m,
\qquad
H_1/G\propto(y)_m.
\]

For `i=119`, `m=60`, this explains why using only two maximal Hankel determinants is insufficient: at `j=y` the residual gcd can still grow like degree 60.

Using all maximal minors is what reduces the residual scale to the expected degree 30.

## 8. Exact computational checks actually performed

The following checks were performed with exact symbolic/integer arithmetic; they are not floating-point heuristics.

1. The translated-coefficient identity (4) was expanded and checked for `r=1,...,6`.
2. The center-case residual polynomial gcd degree `ceil(r/2)` was checked by exact factorization for `r=2,...,8`.
3. Nontrivial integer contents occur in practice, so polynomial gcd `1` does **not** imply bounded integer content. Example:
   for `r=4`, `(j,y)=(51,52)`, the residual content is
   \[
   1225=5^2\cdot7^2.
   \]
4. Earlier symbolic experiments on shifted Hankel determinants agree with the common-factor degree `3*binom(r,2)` pattern.
5. Heavy Gröbner-basis calculations that timed out are **not** counted as verified results.

## 9. What is proved vs. what remains open

### Proved / derived in this handoff

- `a` divides every normalized coefficient `Z_h`.
- Every `r x r` minor is divisible by `a^r`.
- The 60 x 61 maximal minors reduce, after a common factor of degree 5310, to the explicit residuals (1)-(2).
- The translation identity (4) and gcd-preservation identity (5).
- The large-prime local classification (6)-(8), subject to rechecking in any formal integration.
- Exact small-r symbolic checks listed above.

### Not proved

- `i=119` as a whole.
- The uniform global content bound (9).
- A constant comparison strong enough to finish the critical exponent after (9).
- Any claim that the non-effective S-part theorem yields an effective cutoff.
- Any uniform polynomial bound `H(A) << A^C` from Matveev alone.

## 10. Recommended next task

Do **not** spend the main effort extending the known `n<=10^87` finite range.

Instead, attack

\[
g_{60}(j,y)=
\gcd_{0\le k\le60}
\left[
\binom{j-60+k}{k}
\binom{n-59}{60-k}
\right].
\]

The best route is local prime-by-prime analysis:

1. For `p>118`, use (6)-(8) to assign the full `p`-part to one of `n-59,...,n-118` and sum exponents without overcounting.
2. For the finitely many `p<=118`, derive an explicit uniform valuation bound from the 61 coefficients in (5).
3. Aim for
   \[
   g_{60}(j,y)\le C\,n^{30}
   \]
   with explicit `C`.
4. Then combine with the exact discriminant / small-prime constants already present in the repository to test whether the critical constant is favorable.

If this succeeds, `i=119` is closed with no upper bound on `n` and without extending the A=100 computation.

## 11. Integration warning

This note is a research handoff, not a completed proof of Erdős 699 for `i=119`.
Any future integrator should independently verify the determinant factorization and local valuation lemma before upgrading them to repository theorems.
