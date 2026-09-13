# Erdős Problem 699 — i=3 progress beyond the current GitHub state

Date: 2026-09-13

## 0. Purpose and status discipline

This note records **only the progress obtained after the current GitHub i=3 notes** in
`yoshiyoyoyo44/erdos699`, so another agent can continue without redoing the same work.

The relevant GitHub baseline already contains, among other things:

- the nonsquare reduction for \(i=3\);
- \(n=2^uM\), \(u\ge 49\), \(M\) odd, \(M^3<2^{u-2}\);
- the normalization
  \[
  \gamma=\begin{cases}3&v_3(M)=1\\1&v_3(M)\ne1,\end{cases}
  \qquad T=M/\gamma,\qquad n=\gamma 2^uT,\qquad j=Tk;
  \]
- the four possible branches
  \[
  (\gamma,\delta_1,\delta_2)\in
  \{(1,1,1),(1,1,3),(1,3,1),(3,1,1)\};
  \]
- the factorization \(Q_1=RS,\ Q_2=ABC\), the positive integers
  \(a,b,g,h\), and the identities
  \[
  k=SBg,\quad j-1=RAa,\quad H-k=RCh,\quad n-j-1=SAb,
  \]
  \[
  T^2BCgh-A^2ab=\delta_1;
  \]
- the center variable \(c=n/2-j\), the center integer \(w\), and
  \[
  z^2=\delta_1^2+wQ,\qquad 4c^2=n+2Q_1z;
  \]
- the factorization
  \[
  w=e_cf_c,\qquad
  e_c=\delta A-2s,\qquad
  f_c=\delta BC-2Aab,
  \]
  \[
  Af_c-BCe_c=2\delta_1,
  \]
  where
  \[
  \delta=\delta_1\delta_2,\qquad s=T^2gh;
  \]
- the unitary condition
  \[
  T\mid w-c_0,\qquad
  \gcd\!\left(T,\frac{w-c_0}{T}\right)=1,
  \qquad c_0=\delta_1^2\delta_2;
  \]
- the exclusion of the square branch and the fixed-\(w\)/fixed-\(\lambda\)
  elliptic-curve finiteness results.

This file distinguishes four levels:

1. **proved algebraically below**;
2. **closed by an explicit finite argument in this continuation, but not yet committed/certified in the repository**;
3. **supported by external complete elliptic-curve data**;
4. **observed/conjectural and still requiring a proof**.

This is **not** a complete proof of the \(i=3\) case or of Erdős Problem 699.

---

## 1. Exact 2-adic valuation of the center cofactor

Let
\[
v=v_2(j).
\]
For odd \(j\), take \(v=0\). For even \(j\), the existing 2-adic bounds and the
small-gap exclusions below imply that the two terms in the exact center identity
have distinct 2-adic valuations.

Using
\[
\frac{w-c_0}{T}
=
w\gamma2^{u-1}-\delta_2TZ^2,
\]
with
\[
z=TZ,\qquad v_2(Z)=2v+1,
\]
one obtains

\[
\boxed{v_2(w-c_0)=4v+2.}
\]

Hence there is a unique positive odd integer \(m\) such that

\[
\boxed{w=c_0+T2^{4v+2}m.}
\]

The unitary condition already present in the GitHub notes then gives

\[
\boxed{\gcd(m,T)=1.}
\]

This strictly strengthens the previous low-modulus information such as
\(w\bmod 64\) and \(w\bmod1024\).

### Auxiliary exact identity

A useful algebraic identity, obtained from
\(w=e_cf_c\), \(Af_c-BCe_c=2\delta_1\), and \(e_c=\delta A-2s\), is

\[
\boxed{
A(w-c_0)
=
\delta_1K(\delta A-4s)+4BCs^2,
}
\]

where
\[
K=n/2.
\]

For even \(j\), \(v_2(s)=2v\). This identity gives an alternative route to the
same exact valuation \(v_2(w-c_0)=4v+2\) once the relevant gap inequality is known.

**Status:** algebraic derivation; should be promoted into the main GitHub proof after a line-by-line rewrite.

---

## 2. The gap parameter

Define for even \(j\)

\[
\boxed{g=u-4v_2(j).}
\]

The existing branchwise inequalities first imply \(g\ge 2\). The cases \(g=2,3\)
can be eliminated directly; hence

\[
\boxed{g\ge4.}
\]

The important point is that the exact center valuation turns every fixed \(g\)
into a finite Diophantine problem.

Set

\[
B_g=\gamma c_0\,2^{g-3}.
\]

From the center upper bound one obtains

\[
1\le m<B_g,
\]

and from the exact center identity

\[
T\mid B_g-m.
\]

Write

\[
q=\frac{B_g-m}{T},\qquad x=2^v.
\]

After dividing out the exact power \(2^{2v+1}\) from \(Z\), one gets

\[
\boxed{
\delta_2 Z_0^2
=
m\gamma2^{g-1}x^4+q.
}
\]

Thus, for fixed \(g\), only finitely many triples \((m,T,\text{branch})\) are possible.

Multiplying through gives quartics of the form

\[
Y^2=\alpha x^4+\beta,
\]

which map to nonsingular elliptic curves

\[
V^2=X^3+\alpha\beta X.
\]

Therefore:

\[
\boxed{\text{For each fixed }g,\text{ the even-}j\text{ candidate set is finite.}}
\]

In particular, any hypothetical infinite sequence of even-\(j\) candidates must satisfy

\[
\boxed{u-4v_2(j)\to\infty.}
\]

**Status:** algebraic reduction plus Siegel finiteness; repository-grade proof still needs to be written cleanly.

---

## 3. Elimination of \(g=4\)

The branchwise size bounds leave only two possible branches at \(g=4\), and both
force \(T=1\).

### Branch \((\gamma,\delta_1,\delta_2)=(1,1,3)\)

Here \(c_0=3\), \(B_g=6\). The normalized quartic and the oddness of \(Z_0\) force
\(m=3\), \(q=3\), hence

\[
Z_0^2=8x^4+1.
\]

Then

\[
(Z_0-1)(Z_0+1)=8x^4.
\]

The two factors differ by \(2\) and are powers of \(2\), forcing only the tiny
solution \(x=1\), incompatible with the large-\(u\) counterexample range.

### Branch \((1,3,1)\)

Here \(c_0=9,\ B_g=18,\ T=1\). Modulo \(8\),

\[
m\in\{1,9,17\}.
\]

The \(m=17\) case is eliminated by the existing mod-\(9\) restriction on \(w\).

The \(m=9\) case again reduces to

\[
Z^2=8x^4+1.
\]

The \(m=1\) case becomes

\[
Z^2=8x^4+17,
\]

equivalently

\[
Z^2-17=2^{4v+3}.
\]

The published classification of \(y^2-17=2^k\) gives only
\(k=3,5,6,9\), whereas the \(i=3\) counterexample has \(u\ge49\).

Therefore

\[
\boxed{g=4\text{ is impossible}.}
\]

---

## 4. Elimination of \(g=5\) via one elliptic curve

After the branch restrictions, the only unresolved \(g=5\) equation reduces to

\[
\boxed{3Z^2=16x^4+11,\qquad x=2^v.}
\]

Equivalently,

\[
(3Z)^2=48x^4+33.
\]

Under

\[
X=12x^2,\qquad Y=18xZ,
\]

this maps to

\[
\boxed{E:\ Y^2=X^3+99X.}
\]

This is Cremona curve **34848l1**.

The complete integral \(X\)-coordinate list in John Cremona's `ecdata` is

\[
\boxed{\{0,1,3,12,33,49,99,192\}.}
\]

The `ecdata` generation code computes integral points independently with
both Sage and Magma and compares the outputs.

Because our points require

\[
X=12\cdot4^v,
\]

the only possibilities in the complete list are

\[
v=0\quad\text{or}\quad v=2.
\]

But for \(g=5\),

\[
u=4v+5\ge49,
\]

so \(v\ge11\), contradiction.

Hence

\[
\boxed{g=5\text{ is impossible}.}
\]

**Status:** externally strongly certified by Cremona/Sage/Magma complete integral-point data.
For a fully repository-local proof certificate, rerun Magma with proved Mordell-Weil flags
as in the existing `i3_center_*.magma` files.

---

## 5. Re-audited exclusions of \(g=6,7,8\)

These exclusions were rechecked in the continuation using the normalized fixed-gap
quartics, branchwise size bounds, small-prime quadratic-residue tests, and fixed-difference
factorizations.

### \(g=6\)

Only the \((\delta_1,\delta_2)=(3,1)\) and \(\gamma=3\) branches survive the coarse
size restrictions. The finite \(m\)-sets are eliminated by congruences except for
a terminal equation of the form

\[
Z^2=2208\cdot16^v+1.
\]

Factoring

\[
(Z-1)(Z+1)=2208\cdot16^v
\]

shows that only a tiny \(v\) can occur, outside the counterexample range.

Thus the chat-level re-audit gives

\[
\boxed{g=6\text{ impossible}.}
\]

### \(g=7\)

The same finite-gap reduction leaves finitely many \(m\)-cases. Small-prime
congruences eliminate most of them, while the remaining terminal cases reduce to

\[
Z^2=960\cdot16^v+1
\]

and

\[
Z^2=9024\cdot16^v+1.
\]

Again, fixed-difference factorization excludes all sufficiently large \(v\), and
the surviving tiny cases are outside \(u\ge49\).

Hence

\[
\boxed{g=7\text{ impossible}.}
\]

### \(g=8\)

At \(g=8\), the first center-square condition alone leaves a small finite list of
quartics. Four of the residual curves have square constant term and are eliminated by

\[
(Z-s)(Z+s)=A16^v.
\]

For the other cases, using **both** center-square conditions is substantially stronger
than using the quartic alone. Small-prime residue sieves plus a few additional
fixed-difference factorizations close the remaining cases.

The initial claim that a single \(v\bmod90\) sieve closed everything was too strong:
one residue class survived that first sieve. After adding the missing local condition
and the second center-square constraint, the continuation closed the remaining cases.

The chat-level audit therefore gives

\[
\boxed{g=8\text{ impossible}.}
\]

### Consequence

Accepting the above finite audits,

\[
\boxed{
g\notin\{4,5,6,7,8\},
}
\]

so every even-\(j\) counterexample must satisfy

\[
\boxed{
u\ge4v_2(j)+9.
}
\]

**Status of \(g=6,7,8\):** finite proofs were reconstructed and re-audited in chat,
but the explicit residue tables / replayable certificates have not yet been written
to GitHub. They should be treated as strong working results pending repository certification.

---

## 6. \(g=9\): first genuinely new obstruction

At \(g=9\), the finite-gap mechanism changes character.

A \(T=5\) branch appears for the first time. In the continuation, all of its finite
\(m\)-cases were eliminated by small-prime congruences.

The other non-principal branches were also eliminated by a mixture of congruence
conditions and square-constant factorizations.

The remaining hard cases lie in the principal branch

\[
T=\gamma=\delta_1=\delta_2=1.
\]

Only

\[
\boxed{m\in\{7,23,31,47\}}
\]

remain.

Let

\[
R=2^{2v+4}.
\]

Then all four cases have the uniform form

\[
\boxed{
Z^2-mR^2=64-m,
}
\]

or equivalently

\[
\boxed{
Z^2-64=m(R^2-1).
}
\]

Thus

\[
\boxed{
(Z-8)(Z+8)=m(R-1)(R+1).
}
\]

This is substantially more rigid than a generic generalized Pell equation because
the two left factors differ by \(16\), while \(R-1\) and \(R+1\) differ by \(2\).

---

## 7. The ghost solution and why local congruences stop working at \(g=9\)

Formally set \(v=-2\), so \(R=1\). Then for every \(m\),

\[
(Z,R)=(8,1)
\]

solves

\[
Z^2-mR^2=64-m.
\]

This explains the persistent residue classes seen in local sieves: for many moduli,
large positive \(v\) can imitate the formal \(v=-2\) point modulo the multiplicative
order of \(2\).

So the failure of a finite local sieve at \(g=9\) is structural rather than accidental.

In particular, the \(g=9\) step likely requires one of:

- a global Pell/Lucas descent;
- a full integral-point calculation on a fixed elliptic curve;
- or a descent using the original \(A,B,C,e_c,f_c\) factorization in addition to the center equations.

This is an important qualitative change from \(g\le8\).

---

## 8. Generalized Pell structure for \(m=7\) and \(m=23\)

### \(m=23\)

The equation is

\[
Z^2-23R^2=41.
\]

The fundamental unit is

\[
24+5\sqrt{23}.
\]

Using the standard finite-representative theorem for generalized Pell equations,
the representative bound reduces the primitive representatives to

\[
(\pm8,\pm1).
\]

Thus the \(R\)-coordinates lie in two recurrence orbits satisfying

\[
\boxed{
X_{n+2}=48X_{n+1}-X_n.
}
\]

Two convenient initializations are

\[
A_0=1,\qquad A_1=64,
\]

and

\[
B_0=1,\qquad B_1=-16.
\]

Extensive exact computation suggests, for odd \(n\),

\[
\boxed{
v_2(A_n)=3+v_2(3n+5),
}
\]

and

\[
\boxed{
v_2(B_n)=3+v_2(3n-5).
}
\]

If these identities are proved, then an \(A_n\) or \(B_n\) which is itself a power
of \(2\) has size only \(O(n)\), whereas the Pell recurrence grows exponentially.
That reduces the power-of-two terms to a finite small check.

**Status:** the recurrence is rigorous; the displayed exact valuation formulas are
currently **conjectural/experimentally verified**, not yet proved.

### \(m=7\)

The generalized Pell equation

\[
Z^2-7R^2=57
\]

has the explicit complete families

\[
\pm(8\pm\sqrt7)(8+3\sqrt7)^n,
\]

and

\[
\pm(13\pm4\sqrt7)(8+3\sqrt7)^n.
\]

Observed valuation patterns are analogous. For one orbit, odd \(n\) satisfy

\[
v_2(R_n)=3+v_2(n+3),
\]

while the second orbit exhibits a shifted formula with a small exceptional solution
around \(n=3\).

Again, these valuation formulas still need a full LTE/induction proof.

Small exact searches show only small power-of-two \(R\)-values, all below the
\(v\ge10\) range required by an actual \(g=9,\ u\ge49\) counterexample.

---

## 9. Elliptic-curve formulation of the four \(g=9\) hard cases

Let

\[
t=2^v,\qquad R=16t^2.
\]

Then

\[
Z^2=256mt^4+(64-m).
\]

The standard quartic-to-cubic transformation gives

\[
\boxed{
E_m:\ y^2=x^3+m(64-m)x,
}
\]

with

\[
x=16mt^2,\qquad y=4mtZ.
\]

For the four remaining values of \(m\), the curves are

\[
\begin{array}{c|c}
m & E_m\\
\hline
7 & y^2=x^3+399x,\\
23 & y^2=x^3+943x,\\
31 & y^2=x^3+1023x,\\
47 & y^2=x^3+799x.
\end{array}
\]

Therefore a complete integral-point computation on these four fixed curves,
followed by the restriction

\[
x=16m\,4^v,
\]

would settle the entire remaining \(g=9\) layer.

This is probably the shortest computational route, while the Pell/Lucas valuation
route is the most promising route to a reusable theoretical lemma.

---

## 10. Current strongest working picture

For even \(j\), the new continuation gives the exact structural formula

\[
\boxed{
v_2(w-c_0)=4v_2(j)+2,
}
\]

and the fixed-gap reduction

\[
\boxed{
\delta_2Z_0^2
=
m\gamma2^{g-1}2^{4v}+q.
}
\]

The layers

\[
\boxed{
g=4,5,6,7,8
}
\]

have been eliminated at the working-proof level, with \(g=5\) additionally backed
by complete Cremona/Sage/Magma integral-point data.

Thus the strongest current working bound is

\[
\boxed{
u\ge4v_2(j)+9.
}
\]

The \(g=9\) layer is reduced to the four principal equations with

\[
m=7,23,31,47.
\]

If those four are eliminated, the bound improves to

\[
\boxed{
u\ge4v_2(j)+10.
}
\]

The main open subtask is therefore:

> Prove that the four equations
> \[
> Z^2-mR^2=64-m,\qquad
> m\in\{7,23,31,47\},\qquad
> R=2^{2v+4},\ v\ge10,
> \]
> have no solutions.

Two concrete approaches:

1. prove the observed exact \(2\)-adic valuation formulas in the Pell recurrences;
2. compute complete integral points on \(E_7,E_{23},E_{31},E_{47}\) and filter by
   \(x=16m4^v\).

---

## 11. Important caution for the next agent

Do **not** treat every statement in Sections 5 and 8 as repository-certified yet.

- Sections 1–2 are algebraic structural advances.
- \(g=4\) has a concrete proof, including the published \(y^2-17=2^k\) classification.
- \(g=5\) is strongly supported by complete external integral-point data.
- \(g=6,7,8\) were finite-case audited in chat but still need explicit residue/factorization
  tables or replayable certificates added to the repository.
- \(g=9\) is **not solved**.
- The Pell valuation identities in Section 8 are conjectural until a general proof is written.

The best next move is to close \(g=9\) rigorously, then convert the \(g=6,7,8\)
finite audits into reproducible certificates and integrate the exact gap lemma into
the main GitHub proof.
