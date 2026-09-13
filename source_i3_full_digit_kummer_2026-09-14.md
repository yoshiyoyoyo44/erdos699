# Erdős Problem 699 — i=3 full-digit Kummer continuation beyond commit f99cbce
Date: 2026-09-14

## 0. Purpose

This note records progress obtained in a dedicated research thread whose task was:

> Extract genuinely new general restrictions from the full-digit Kummer conditions for the \(i=3\) case, beyond the low-level divisibility conditions
> \[
> Q_1\mid j(j-1),\qquad Q_2\mid j(j-1)(j-2),\qquad T\mid j.
> \]

The GitHub baseline is commit `f99cbce` of `yoshiyoyoyo44/erdos699`.

This note does **not** claim a proof of \(i=3\) or Erdős Problem 699.
It distinguishes:
- algebraically proved statements;
- explicit computational checks actually performed;
- structural conjectures / open next steps.

The repo baseline already has
\[
n=2^uM,\qquad u\ge49,\qquad M\text{ odd},\qquad M^3<2^{u-2},
\]
\[
\gamma=\begin{cases}3,&v_3(M)=1,\\1,&\text{otherwise},\end{cases}
\qquad T=M/\gamma,\qquad H=\gamma2^u,\qquad n=HT,\qquad j=Tk,
\]
and
\[
Q_1=\frac{n-1}{\delta_1}=RS,\qquad
Q_2=\frac{n/2-1}{\delta_2}=ABC,
\]
with
\[
(\gamma,\delta_1,\delta_2)\in
\{(1,1,1),(1,1,3),(1,3,1),(3,1,1)\}.
\]

The factorization variables satisfy
\[
k=SBg,\qquad j-1=RAa,\qquad H-k=RCh,\qquad n-j-1=SAb.
\]

The repo also already contains the quotient-lift Kummer lemma and the signed-deviation formulation. The purpose here is to push that condition back into the established factors \(A,B,C,R,S,a,b,g,h\).

---

## 1. Blockwise carry-free factorization theorem

Let \(q=p^e\) be a full \(p\)-power component of one of the six blocks.
Write \(U\) for the corresponding block divided by \(q\).

For a putative \(i=3\) counterexample, quotient-lift Kummer gives the following additions, each of which must be **carry-free in base \(p\)**.

### \(T\)-block
If \(q=p^e\parallel T\), \(U=T/q\), then
\[
\boxed{
USB\,g+URC\,h=UH.
}
\]

### \(R\)-block
If \(q=p^e\parallel R\), \(U=R/q\), then
\[
\boxed{
UAa+UTC\,h=\delta_1US.
}
\]

### \(S\)-block
If \(q=p^e\parallel S\), \(U=S/q\), then
\[
\boxed{
UTB\,g+UAb=\delta_1RU.
}
\]

### \(A\)-block
If \(q=p^e\parallel A\), \(U=A/q\), then
\[
\boxed{
URa+USb=2\delta_2UBC.
}
\]

### \(B\)-block
If \(q=p^e\parallel B\), \(U=B/q\), then
\[
\boxed{
TSU\,g+\left(2\delta_2AUC-TSU\,g\right)=2\delta_2AUC.
}
\]

### \(C\)-block
If \(q=p^e\parallel C\), \(U=C/q\), then
\[
\boxed{
\left(2\delta_2ABU-TRU\,h\right)+TRU\,h=2\delta_2ABU.
}
\]

This is the same full Kummer information already present abstractly in signed-digit form, but now expressed directly in the established arithmetic blocks.

---

## 2. Exact digit-sum identities

Let \(s_p(x)\) denote the sum of the base-\(p\) digits of \(x\).

Carry-free addition is equivalent to digit-sum additivity. Hence:

\[
\boxed{
s_p(USB\,g)+s_p(URC\,h)=s_p(UH)
}
\tag{2.1}
\]

for \(p^e\parallel T\);

\[
\boxed{
s_p(UAa)+s_p(UTC\,h)=s_p(\delta_1US)
}
\tag{2.2}
\]

for \(p^e\parallel R\);

\[
\boxed{
s_p(UTB\,g)+s_p(UAb)=s_p(\delta_1RU)
}
\tag{2.3}
\]

for \(p^e\parallel S\);

\[
\boxed{
s_p(URa)+s_p(USb)=s_p(2\delta_2UBC)
}
\tag{2.4}
\]

for \(p^e\parallel A\);

with analogous formulas for \(B,C\).

Equivalently, for the relevant quotient pair \((N,J)\),
\[
\boxed{
v_p\binom nj
=
\frac{s_p(J)+s_p(N-J)-s_p(N)}{p-1}.
}
\]

---

## 3. Prefix forcing lemma

Suppose
\[
X+Y=N
\]
is carry-free in base \(p\).

If for some \(\ell\ge1\),
\[
N\bmod p^\ell=d<p,
\]
then
\[
\boxed{
X\bmod p^\ell=t,\qquad
Y\bmod p^\ell=d-t
}
\]
for some
\[
t\in\{0,1,\dots,d\}.
\]

In particular, if
\[
N\equiv1\pmod{p^\ell},
\]
then
\[
\boxed{
(X,Y)\equiv(0,1)\ \text{or}\ (1,0)\pmod{p^\ell}.
}
\tag{3.1}
\]

This converts higher Kummer digits into actual high-power divisibility constraints on the factor variables.

---

## 4. Dynamic \(p^\lambda\)-forcing

### \(T\)-block

Let \(q=p^e\parallel T\), \(U=T/q\), and
\[
\lambda_T(q)
=
v_p(UH-1)
=
v_p\!\left(\gamma2^u\frac{T}{p^e}-1\right).
\]

If \(\lambda_T(q)>0\), then the prefix lemma gives
\[
USB\,g\equiv0\text{ or }1\pmod{p^{\lambda_T(q)}}.
\]

Since \(p\nmid USB\),
\[
\boxed{
p^{\lambda_T(q)}
\text{ divides exactly one of }g,h.
}
\tag{4.1}
\]

Equivalently,
\[
\boxed{
U(H-2k)\equiv\pm1
\pmod{p^{\lambda_T(q)}}.
}
\tag{4.2}
\]

### \(R,S,A\)-blocks

If \(q=p^e\parallel R\), \(U=R/q\), and
\[
\lambda_R(q)=v_p(\delta_1US-1)>0,
\]
then
\[
\boxed{
p^{\lambda_R(q)}
\text{ divides exactly one of }a,h.
}
\tag{4.3}
\]

If \(q=p^e\parallel S\), \(U=S/q\), and
\[
\lambda_S(q)=v_p(\delta_1RU-1)>0,
\]
then
\[
\boxed{
p^{\lambda_S(q)}
\text{ divides exactly one of }g,b.
}
\tag{4.4}
\]

If \(q=p^e\parallel A\), \(U=A/q\), and
\[
\lambda_A(q)=v_p(2\delta_2UBC-1)>0,
\]
then
\[
\boxed{
p^{\lambda_A(q)}
\text{ divides exactly one of }a,b.
}
\tag{4.5}
\]

---

## 5. Dynamic product obstruction

Define
\[
\Pi_T
=
\prod_{\substack{p^e\parallel T\\ \lambda_T(p^e)>0}}
p^{\lambda_T(p^e)}.
\]
Then
\[
\boxed{\Pi_T\mid gh.}
\tag{5.1}
\]

Using the existing inequality
\[
\delta A>2T^2gh,
\]
we get
\[
\boxed{
2T^2\Pi_T<\delta A.
}
\tag{5.2}
\]

More explicitly,
\[
\boxed{
2T^2
\prod_{p^e\parallel T}
p^{
v_p(\gamma2^uT/p^e-1)
}
<\delta A,
}
\tag{5.3}
\]
with zero exponents omitted.

Analogously define \(\Pi_A,\Pi_R,\Pi_S\). Combining with
\[
ab<\frac{\delta BC}{2A},
\qquad
gh<\frac{\delta A}{2T^2},
\]
gives the working inequality
\[
\boxed{
4T^2\Pi_A\Pi_R\Pi_S\Pi_T
<
\delta^2BC.
}
\tag{5.4}
\]

This is a dynamic condition: the moduli and exponents depend on the actual prime-power factorization of the candidate, so it is not covered by the fixed-modulus local-solubility obstruction from the latest gap/descent note.

---

## 6. New lower bounds for \(R,S\)

Using
\[
\delta_1R=Ab+TBg,
\qquad
\delta_1S=Aa+TCh,
\]
together with
\[
A>\frac{2T^2}{\delta},
\qquad
B\ge\frac{T+1}{\delta},
\qquad
C>\frac{4T}{\delta},
\qquad
\delta=\delta_1\delta_2,
\]
and positivity,
\[
\boxed{
R>\frac{3T^2+T}{\delta_1^2\delta_2},
}
\tag{6.1}
\]
\[
\boxed{
S>\frac{6T^2}{\delta_1^2\delta_2}.
}
\tag{6.2}
\]

In particular,
\[
\boxed{R>1,\qquad S>1.}
\tag{6.3}
\]

These bounds are useful for preventing degenerate pure-\(p\)-power quotient summands.

---

## 7. Digit-sum lower bounds

### \(Q_1\)-side

Let \(q=p^e\) be a full prime-power component of \(Q_1\).
Using \(A,B,C\ge11\) and \(R,S>1\), both quotient summands in the \(R\)- or \(S\)-block addition have a nontrivial \(p\)-unit factor and therefore cannot be pure powers of \(p\).

Each summand therefore has digit sum at least \(2\).
The quotient \((n-1)/q\) is odd, so its base-\(p\) digit sum is odd. Hence
\[
\boxed{
s_p\!\left(\frac{n-1}{q}\right)\ge5.
}
\tag{7.1}
\]

Thus
\[
\boxed{
q\le\frac{n-1}{5}.
}
\tag{7.2}
\]

A working corollary is that \(Q_1\) cannot consist of one full prime-power block only; this suggests
\[
\boxed{\omega(Q_1)\ge2.}
\]
This corollary should be re-audited carefully with the exceptional removed \(3\)-factor before manuscript promotion.

### \(Q_2\)-side

For any full prime-power component \(q=p^e\parallel Q_2\),
\[
\boxed{
s_p\!\left(\frac{n-2}{q}\right)\ge4.
}
\tag{7.3}
\]

For an \(A\)-block prime power and even \(j\), parity gives the stronger working bound
\[
\boxed{
s_p\!\left(\frac{n-2}{q}\right)\ge6.
}
\tag{7.4}
\]

---

## 8. \(T>1\) digit-sum restrictions

Let \(q=p^e\parallel T\), \(U=T/q\).

From
\[
USB\,g+URC\,h=UH
\]
and carry-free addition,
\[
\boxed{
s_p(UH)\ge4
}
\tag{8.1}
\]
for even \(j\), and
\[
\boxed{
s_p(UH)\ge6
}
\tag{8.2}
\]
for odd \(j\).

If \(T=p^e\), then
\[
\boxed{
s_p(\gamma2^u)\ge4
}
\]
and for odd \(j\),
\[
\boxed{
s_p(\gamma2^u)\ge6.
}
\]

If additionally \(p\equiv1\pmod4\), then
\[
s_p(UH)\equiv UH\pmod{p-1},
\]
and \(4\mid p-1\), while \(4\mid UH\). Therefore \(s_p(UH)\) is divisible by \(4\), so
\[
\boxed{
p\equiv1\pmod4,\quad p^e\parallel T,\quad j\text{ odd}
\Longrightarrow
s_p(UH)\ge8.
}
\tag{8.3}
\]

---

## 9. Multiplicative-order interpretation

For odd \(d>1\) with \((d,p)=1\), define
\[
\mu_p(d)=\min_{m\ge1}s_p(dm).
\]

Then
\[
\boxed{
\mu_p(d)=2
\iff
\exists r\ge1:\ p^r\equiv-1\pmod d.
}
\tag{9.1}
\]

Proof: a positive integer with base-\(p\) digit sum \(2\) is either \(2p^a\) or \(p^a+p^b\). An odd \(d>1\) coprime to \(p\) cannot divide \(2p^a\), so divisibility forces \(d\mid p^{a-b}+1\). The converse is immediate.

For the \(T\)-block,
\[
\boxed{
s_p(UH)\ge
\mu_p(USB)+\mu_p(URC).
}
\tag{9.2}
\]

If equality \(s_p(UH)=4\) holds, then there exist \(r_1,r_2\ge1\) with
\[
\boxed{
p^{r_1}\equiv-1\pmod{USB},
\qquad
p^{r_2}\equiv-1\pmod{URC}.
}
\tag{9.3}
\]

Thus low digit sum forces multiplicative-order synchronization across independent blocks.

---

## 10. Even-\(j\) refinement at minimal digit sum \(4\)

Assume
\[
v=v_2(j)\ge2,
\]
and \(q=p^e\parallel T\).

If
\[
s_p(UH)=4,
\]
then each positive quotient summand has digit sum exactly \(2\), so up to a power of \(p\) it is of the form
\[
p^r+1.
\]

Because both quotient summands have \(2\)-adic valuation \(v\), LTE gives
\[
\boxed{
r\text{ odd},\qquad v_2(p+1)=v.
}
\tag{10.1}
\]

Hence
\[
\boxed{
p\mid T,\qquad v_2(p+1)\ne v_2(j)
\Longrightarrow
s_p(UH)\ge6.
}
\tag{10.2}
\]

If \(p\equiv1\pmod4\), then \(v_2(p+1)=1\), so for \(v_2(j)\ge2\), digit sum \(4\) is impossible. Since the digit sum is then constrained modulo \(p-1\),
\[
\boxed{
p\equiv1\pmod4,\quad
p\mid T,\quad
j\text{ even},\quad
v_2(j)\ge2
\Longrightarrow
s_p(UH)\ge8.
}
\tag{10.3}
\]

This is a full-\(u\) restriction, not a finite-gap extension.

---

## 11. Explicit check: stronger than low-level divisibility

Use the repo's low-level relaxation family at \(m=0\):
\[
A=11,\quad B=85,\quad C=41,\quad
R=1217,\quad S=63,\quad
g=5,
\]
with
\[
(n,j)=(76672,26775).
\]

This example satisfies the low-level factorization/divisibility system recorded in the repo.

### At \(p=17\)

Since \(17\mid B\),
\[
N=\frac{n-2}{17}=4510,
\qquad
J=\frac{j}{17}=1575.
\]

But
\[
J\bmod17=11,\qquad
N\bmod17=5,
\]
so the first quotient digit already violates Lucas/Kummer:
\[
11>5.
\]

Digit sums give
\[
s_{17}(J)=23,\qquad
s_{17}(N-J)=23,\qquad
s_{17}(N)=30,
\]
hence
\[
v_{17}\binom nj
=
\frac{23+23-30}{16}
=1.
\]

### At \(p=41\)

Since \(41\mid C\),
\[
N=\frac{n-2}{41}=1870,
\]
and the relevant quotient summand has residue
\[
28>25=N\bmod41.
\]

Digit sums give
\[
53+57-30=80=2(41-1),
\]
hence
\[
v_{41}\binom nj=2.
\]

Therefore the new full-digit restrictions are genuinely stronger than the low-level divisibility conditions.

---

## 12. What was actually computed

The following checks were actually performed in this research thread:

1. Prefix/carry-free validation over many small cases, including \(p=3,5,7,11\), with tens of thousands of applicable prefix checks and no contradiction to the prefix lemma.

2. The explicit relaxed-family example above was checked directly at \(p=17\) and \(p=41\), including quotient residues and digit-sum valuation identities.

3. GitHub search at commit `f99cbce` did not reveal these digit-sum / multiplicative-order theorems in the existing i=3 notes.

No Magma, Sage, PARI, or external integer-point computation was used for the new theorems in this note.

---

## 13. Main unresolved target

The most promising next step is to convert the necessary digit-sum/order restrictions into a global contradiction.

The strongest current route is the \(T\)-block:
\[
s_p(UH)\ge \mu_p(USB)+\mu_p(URC).
\]

If the right side is small, then different blocks must divide sparse base-\(p\) polynomials such as
\[
p^r+1,\qquad
p^r+p^s+1,\qquad
2p^r+1.
\]

Promising tools:
- multiplicative-order incompatibility across prime powers of \(B,C,R,S,T\);
- \(2\)-adic valuations of those orders;
- LTE;
- sparse-polynomial divisibility;
- interaction with \(M^3<2^{u-2}\) and the known size inequalities.

A particularly attractive target is:

> Show that for every nontrivial \(T>1\), at least one prime \(p\mid T\) forces
> \[
> s_p\!\left(\gamma2^uT/p^{v_p(T)}\right)
> \]
> to be too large to coexist with the factor-size inequalities.

If successful, this would eliminate an infinite class of general-\(M\) candidates and would be qualitatively different from extending the finite gap exclusions.

---

## 14. Status summary for the next agent

### Proved in this continuation
- blockwise carry-free factorization in \(A,B,C,R,S,T,a,b,g,h\);
- exact digit-sum identities;
- prefix forcing lemma;
- dynamic \(p^\lambda\)-forcing;
- dynamic product obstruction;
- lower bounds for \(R,S\);
- multiplicative-order characterization
  \[
  \mu_p(d)=2\iff p^r\equiv-1\pmod d;
  \]
- even-\(j\) minimal-digit-sum condition
  \[
  s_p(UH)=4\Rightarrow v_2(p+1)=v_2(j).
  \]

### Explicitly checked
- the low-level relaxed family contains examples rejected by the new full-digit conditions;
- concrete rejection at \(p=17\) and \(p=41\) for \((n,j)=(76672,26775)\).

### Needs extra audit before manuscript promotion
- the clean corollary \(\omega(Q_1)\ge2\), especially the treatment of the exceptional removed \(3\)-factor;
- the strongest parity upgrades in the \(Q_2\) \(A\)-block;
- whether the \(R,S\) quantitative lower bounds can be sharpened without hidden branch assumptions.

### Still open
- no contradiction for all \(T>1\);
- no complete elimination of odd \(j\);
- no proof of \(i=3\);
- no proof of Erdős Problem 699.

The best continuation direction is to combine multiplicative-order synchronization forced by small digit sum with the size inequalities already present in the repo.
