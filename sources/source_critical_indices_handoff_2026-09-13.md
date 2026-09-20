# Erdős Problem 699 — Progress beyond current GitHub state (2026-09-13)

This note records only progress obtained after the current GitHub state of `yoshiyoyoyo44/erdos699` (latest checked commit: `9a2243f5203b1962fe039da76cb0f4a0cf1c645f`, “Prove all indices at least 121 with interval valuation certificates”). It is intended as a handoff note for the next research agent. It does not repeat older i=3 material or the already-committed interval-valuation proof for all i>=121 and i=97,101.

## 1. New cofactor upper bound at the critical indices

Fix i and suppose a counterexample exists. For each prime p<i, let

\[
E_p=\max_{0\le r\le i-1}v_p(n-r),
\]

choose an integer

\[
m_p=n-r_p=a_pp^{E_p},\qquad 0\le r_p\le i-1,
\]

with maximal p-adic valuation, and call a_p the p-free cofactor.

Using

\[
v_p\binom ni=\sum_{k\ge1}\mathbf 1_{\{n\bmod p^k<i\bmod p^k\}},
\]

one gets

\[
\boxed{v_p\binom ni\le E_p-v_p(i).}
\]

Therefore, if D=gcd(C(n,i),C(n,j)) is a counterexample gcd containing no prime >=i,

\[
\boxed{
D\le \frac{n^{\pi(i-1)}}{i\prod_{p<i}a_p}.
}
\tag{1}
\]

This strengthens the previous crude bound D<=n^{pi(i-1)} by inserting the full product of p-free cofactors.

## 2. The exact exponent-tie indices 96, 100, 120

The discriminant lower bound in the repository has the form

\[
D>\kappa_i n^{i/4},
\]

where, for n>=16598 i,

\[
\kappa_i=
\frac{2^{i/2}}{P_i^{1/(2i-2)}}
\left(\frac{16597}{16598}\right)^i,
\qquad
P_i=\prod_{r=1}^i r^r.
\]

In the range relevant to the present continuation, the equality

\[
\frac{i}{4}=\pi(i-1)
\]

occurs at

\[
\boxed{i=96,100,120.}
\]

For these three indices the exponent comparison alone is exactly tied, but (1) allows the coefficient to be improved.

The following thresholds are enough:

\[
(i,A)=(96,14),(100,15),(120,18).
\]

If all but at most one of the cofactors satisfy a_p>=A+1, then

\[
D\le \frac{n^{i/4}}{i(A+1)^{\pi(i-1)-1}}.
\]

Exact numerical margins against the discriminant lower bound are

\[
96:\ 1.4729019\ldots,
\qquad
100:\ 2.6289997\ldots,
\qquad
120:\ 2.3222539\ldots.
\]

Thus each of i=96,100,120 is reduced to proving that two distinct primes p,q<i cannot both have small cofactors a_p,a_q<=A once n is large enough.

## 3. Reduction to a finite near-collision problem

If two small cofactors occur, then for distinct primes p,q<i,

\[
a_pp^e-a_qq^f=d,
\qquad |d|\le i-1.
\]

For the largest threshold A=18 and i<=120 it is enough to solve

\[
\boxed{
|ap^e-bq^f|\le119,
\quad
1\le a,b\le18,
\quad
p\ne q<120.
}
\tag{2}
\]

The route checked in this continuation is:

- a Matveev lower bound for a linear form in three logarithms gives a safe initial exponent bound E,F<7*10^13;
- after removing cross-prime factors from a and b, the non-homogeneous branches are reduced by Dujella-Petho continued-fraction reduction;
- the homogeneous branch is treated by Legendre's continued-fraction criterion plus certified lower bounds for |P log p-Q log q|.

For the non-homogeneous normalized branches, 228,172 cases were covered, reducing to exponents at most about the high 60s. For the homogeneous branch, all convergents with denominator <=7*10^13 for all ordered p!=q<120 were checked with outward-rounded high-precision rational intervals; no convergent can support exponents >=64.

A final exact integer enumeration of the resulting small exponent range gives the largest near-collision

\[
\boxed{
10\cdot3^{11}=1,771,470,
\qquad
11^6=1,771,561,
}
\]

with difference 91.

Hence beyond this scale, two cofactors <=18 cannot occur simultaneously.

Important status note: the mathematics above has been worked through in this continuation, but the full Matveev/continued-fraction certificate and independent replay script have NOT yet been committed to GitHub. Treat this as a theorem package ready for formal packaging, not yet as a repository-finalized proof.

## 4. Consequence for i=96,100,120

Combining the cofactor coefficient improvement with the near-collision bound reduces the remaining n-ranges to finite ranges. These were then checked by the same Kummer-style prime-power congruence logic used in the repository's existing interval verifier.

Residual n-values after the prime-gap shortcut:

\[
\begin{array}{c|c}
i & \text{residual }n\text{-values}\\
\hline
96 & 234\\
100 & 162\\
120 & 36
\end{array}
\]

For all 432 residual n-values, intersecting the necessary Kummer conditions

\[
j\bmod q\le n\bmod q
\]

for suitable prime powers q=p^e with p>i leaves no admissible j.

Therefore the current continuation strongly supports the following extension of the GitHub result:

\[
\boxed{
\text{Erdos 699 holds for }i=96,97,100,101\text{ and every }i\ge120.
}
\]

The new indices relative to GitHub are i=96,100,120. The remaining task before calling these repository-final results is to package the analytic reduction and finite certificates into an independently replayable verifier and proof note.

## 5. New i=119 bootstrap

For i=119, pi(118)=30 while i/4=29.75, so there is an exponent deficit of only 1/4. The cofactor upper bound gives

\[
D\le \frac{n^{30}}{119\prod_{p<119}a_p},
\]

whereas the discriminant lower bound is

\[
D>\kappa_{119}n^{29.75},
\qquad
\kappa_{119}\approx4.243921226\times10^{-39}.
\]

Thus every counterexample must satisfy

\[
\boxed{
\prod_{p<119}a_p
<1.9800936203\times10^{36}\,n^{1/4}.
}
\tag{3}
\]

So only an n^{1/4} gain in the cofactor product is needed to close i=119.

Define H(A) to be the largest scale at which two distinct small cofactors <=A can occur through a near-collision

\[
|ap^e-bq^f|\le118,
\qquad a,b\le A,
\qquad p\ne q<119.
\]

If n>H(A)+118, then at most one of the 30 cofactors can be <=A, and hence

\[
\prod_{p<119}a_p\ge(A+1)^{29}.
\]

Combining this with (3) excludes counterexamples whenever

\[
n<N(A),
\qquad
\boxed{
N(A)=\left(119\kappa_{119}(A+1)^{29}\right)^4.
}
\]

Therefore every A for which

\[
\boxed{H(A)+118<N(A)}
\]

produces an explicit eliminated interval. Since

\[
N(A)\asymp A^{116},
\]

a uniform effective estimate

\[
\boxed{H(A)\ll A^C\quad\text{for some }C<116}
\]

would make these intervals eventually overlap forever and would close i=119 completely.

For scale only: at A=100,

\[
N(100)\approx2.06318\times10^{87}.
\]

An exploratory finite search found a largest near-collision near 1.95*10^8 in that range, showing an enormous empirical margin. This A=100 value is exploratory only until the exponent range is certified uniformly in A.

## 6. Additional Kummer restriction for large prime powers

There is another useful necessary condition. Let p>i and let

\[
q_p=p^{v_p(\binom ni)}.
\]

In a counterexample, Kummer's no-carry condition implies

\[
j\bmod q_p\le n\bmod q_p<i.
\]

If q_p>j, then j mod q_p=j>i, impossible. Therefore

\[
\boxed{q_p\le j\le n/2.}
\tag{4}
\]

Thus every large-prime contribution to C(n,i) is forced below j. This may provide an independent way to strengthen the discriminant or cofactor estimates for i=119 and below.

## 7. Global fixed-i finiteness from known S-part theory

There is also a conceptual global result not used in the current GitHub proof.

Let

\[
F_i(X)=X(X-1)\cdots(X-i+1)
\]

and S={p:p<i}. Classical S-part results of Mahler, and later quantitative formulations by Bugeaud-Evertse-Gyory, imply for fixed i and every epsilon>0 that the S-part of F_i(n) grows essentially like

\[
[F_i(n)]_S\ll_{i,S,\epsilon}|F_i(n)|^{1/i+\epsilon}
\ll n^{1+i\epsilon}.
\]

A counterexample gcd D is supported on primes <i, so

\[
D\le[F_i(n)]_S.
\]

Combined with the repository's discriminant lower bound D>>_i n^{i/4}, this implies that for every fixed

\[
\boxed{i\ge5}
\]

only finitely many n can be counterexamples: choose epsilon with

\[
1+i\epsilon<i/4.
\]

This is non-effective in the form useful here, so it does not itself solve any remaining fixed i. Its importance is conceptual: the infinite tail for every fixed i>=5 is already ruled out abstractly; the remaining research problem is to make the bound explicit and computationally usable.

## 8. Best next target

The highest-value next step is no longer another raw interval search. It is to prove an effective uniform near-collision bound for the fixed prime set p,q<119:

\[
|ap^e-bq^f|\le118,
\qquad a,b\le A.
\]

A bound H(A)<<A^C with any C<116 would close the i=119 infinite range through the bootstrap above. Because p and q come from a fixed set of only 30 primes, pairwise Matveev + continued-fraction reduction is likely much sharper than a general S-unit theorem.

In parallel, the i=96,100,120 package should be converted into a repository proof note plus an independent exact verifier. Those three indices are much closer to finished than i=119.
