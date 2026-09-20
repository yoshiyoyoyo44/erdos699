# Erdős Problem 699 — Pure-power i=3 continuation handoff

Date: 2026-09-14
Scope: pure-power branch \(n=2^u\), prioritizing even \(j\).
Baseline: `yoshiyoyoyo44/erdos699`, commit `f99cbce`.

This note records only the new progress from this continuation so another AI can continue without repeating the same work.

## 1. Problem and current scope

Erdős Problem 699 asks whether for all integers
\[
1\le i<j\le n/2
\]
the gcd
\[
\gcd\!\left(\binom ni,\binom nj\right)
\]
always has a prime factor \(p\ge i\).

Assigned subproblem:

> Solve the \(i=3\), \(n=2^u\) branch for all \(u\), with even \(j\) prioritized.

Do not replace \(p\ge i\) by the stronger \(p>i\).

At commit `f99cbce`, the repository already has:
- for \(i=3\), any counterexample has \(u\ge49\);
- for even \(j\),
  \[
  g=u-4v_2(j)\ge14;
  \]
- fixed gap \(g\le13\) has been completely excluded;
- the former Pell valuation formulas
  \[
  v_2(A_k)=3+v_2(3k+5),\qquad
  v_2(B_k)=3+v_2(3k-5)
  \]
  are false and must not be reused.

## 2. Pure-power normalization

Assume
\[
n=2^u,\qquad j\ \text{even},\qquad v=v_2(j),\qquad x=2^v.
\]

Let
\[
Q_1=\frac{2^u-1}{\delta_1},\qquad
Q_2=\frac{2^{u-1}-1}{\delta_2}=ABC,
\]
where \(\delta_1,\delta_2\in\{1,3\}\) are the standard 3-adic correction factors.

Use the existing factorization
\[
j=SBg,\qquad
j-1=RAa,\qquad
2^u-j=RCh,\qquad
2^u-j-1=SAb,
\]
with
\[
g=xg_0,\qquad h=xh_0,
\]
and \(g_0,h_0\) odd.

The existing determinant equation becomes
\[
\boxed{x^2BCg_0h_0-A^2ab=\delta_1.}
\tag{1}
\]

Also
\[
\boxed{\delta_2ABC+1=2^{u-1}.}
\tag{2}
\]

The known size condition specializes to
\[
\boxed{\delta_1\delta_2 A>2x^2g_0h_0.}
\tag{3}
\]

## 3. New exact 2-adic valuation

Set
\[
\delta=\delta_1\delta_2.
\]

Then
\[
\boxed{v_2(\delta BC-Aab)=2v.}
\tag{4}
\]

### Proof

Let
\[
q=x^2=2^{2v}.
\]

Because the repository already gives
\[
u\ge4v+14,
\]
we have \(2q\mid 2^{u-1}\).

From
\[
\delta_2ABC+1=2^{u-1}
\]
we get modulo \(2q\)
\[
\delta BC\equiv-\delta_1A^{-1}\pmod{2q}.
\]

From (1),
\[
qBCg_0h_0-A^2ab=\delta_1.
\]
Since \(BCg_0h_0\) is odd,
\[
A^2ab\equiv q-\delta_1\pmod{2q},
\]
hence
\[
Aab\equiv A^{-1}(q-\delta_1)\pmod{2q}.
\]

Subtracting gives
\[
\delta BC-Aab\equiv-qA^{-1}\equiv q\pmod{2q},
\]
because \(A^{-1}\) is odd. Therefore
\[
v_2(\delta BC-Aab)=2v.
\]

## 4. Equivalent exact valuation in the split variables

Normalize the existing \(\eta,\zeta\) variables by
\[
\eta=2\eta_0,\qquad
\zeta=2\zeta_0,\qquad
t=2^{v-1}.
\]

The repository identities become
\[
\delta B=a\zeta_0+tbh_0,
\tag{5}
\]
\[
\delta C=b\eta_0+tag_0,
\tag{6}
\]
\[
\eta_0\zeta_0=\delta A+t^2g_0h_0.
\tag{7}
\]

Direct expansion gives
\[
\boxed{\delta BC-Aab
=2^{v-1}(ag_0B+bh_0C).}
\tag{8}
\]

Combining (4) and (8):
\[
\boxed{v_2(ag_0B+bh_0C)=v+1.}
\tag{9}
\]

This is an exact valuation.

## 5. New odd variable \(W\)

Define
\[
\boxed{
W=\frac{\delta BC-Aab}{2^{2v}}.
}
\tag{10}
\]

By (4), \(W\) is odd.

Using the known size condition (3) together with (1), one gets
\[
\delta BC>Aab,
\]
so
\[
\boxed{W>0.}
\]

Thus
\[
\boxed{\delta BC=Aab+2^{2v}W.}
\tag{11}
\]

## 6. New Mersenne sum identity

Eliminating \(ABC\) between (1), (2), and (11) gives
\[
\boxed{
\delta_1\,2^{u-2v-1}
=
AW+BCg_0h_0.
}
\tag{12}
\]

In the main branch \(\delta_1=1\),
\[
\boxed{
2^{u-2v-1}=AW+BCg_0h_0.
}
\tag{13}
\]

## 7. New gcd restrictions on \(W\)

Using the existing facts that \(A,B,C\) are pairwise coprime and
\[
\gcd(ab,BC)=1,
\]
equation (11) gives
\[
\boxed{\gcd(W,ABC)=1.}
\tag{14}
\]

Also, from (1) and (11),
\[
\boxed{\gcd(W,g_0h_0)\mid\delta_1.}
\tag{15}
\]

Hence if \(\delta_1=1\),
\[
\boxed{\gcd(W,ABCg_0h_0)=1.}
\tag{16}
\]

Therefore the two summands in (13) are coprime:
\[
\boxed{
\gcd(AW,BCg_0h_0)=1
\qquad(\delta_1=1).
}
\tag{17}
\]

This has not yet been turned into a contradiction.

## 8. Important failed strategy: weak determinant system is insufficient

A tempting weaker system is
\[
2^{2v}BCg_0h_0-A^2ab=\delta_1,
\]
\[
\delta A>2^{2v+1}g_0h_0,
\]
plus the Mersenne factorization condition.

This is not enough.

A concrete large fake solution exists already in the main branch:
\[
\boxed{u=613,\qquad v=1,\qquad A=13,\qquad g_0h_0=1.}
\]

Let
\[
Q=2^{612}-1,\qquad
K=\frac{Q}{13}.
\]

Then
\[
4K\equiv1\pmod{13^2},
\]
so
\[
ab=\frac{4K-1}{169}
\]
is a positive odd integer and satisfies
\[
\boxed{4K-13^2ab=1.}
\]

Also
\[
13>8,
\]
so the size condition passes.

The phenomenon is periodic: the relevant congruence reduces to
\[
2^{u+1}\equiv17\pmod{13^3},
\]
and
\[
\operatorname{ord}_{13^3}(2)=2028.
\]

Hence the same weak fake family recurs for
\[
\boxed{u=613+2028k.}
\]

Conclusion:

> Do not try to solve the pure-power branch using only the determinant equation, Mersenne factorization, unitary-divisor information, and coarse size bounds.

The split information in \(B,C,\eta,\zeta\), higher Kummer conditions, or an equivalent genuinely stronger condition is necessary.

## 9. Another false generalization

The following abstract statement is false:
\[
Q\ \text{odd},\quad
2Q+1\mid j(j-1),\quad
Q\mid j(j-1)(j-2),\quad
4\le j\le Q+1
\]
implies impossibility.

Counterexample:
\[
\boxed{Q=38335,\qquad j=26775.}
\]

Thus oddness of \(Q\) is not enough.

For the actual pure-power problem, one must use the stronger Mersenne property
\[
\boxed{Q+1=2^m}
\]
or another equivalent pure-power condition.

## 10. Finite computations actually performed

These are computational observations only, not general proofs.

### 10.1 Corrected low-level divisibility conditions

The corrected necessary conditions
\[
\frac{2^u-1}{\delta_1}\mid j(j-1),
\]
\[
\frac{2^{u-1}-1}{\delta_2}\mid j(j-1)(j-2)
\]
were exhaustively checked for even
\[
4\le j<2^{u-1}.
\]

Using CRT generation over prime-power factors, no candidates were found for
\[
\boxed{10\le u\le179.}
\]

The \(u=180\) run was not completed because the CRT root count became too large.

This does not prove the general case.

### 10.2 Main-branch first condition plus the \(p=3\) Lucas condition

For the main branch \(u\equiv0,1\pmod6\), the first Mersenne divisibility condition together with the requirement that \(3\) not become a common prime factor was checked.

In the tested range through \(u\le179\), no even candidate survived in the counterexample range.

Again, this is finite evidence only.

### 10.3 Primitive-prime phenomenon

In the tested range \(u\le179\), whenever the first-condition CRT set was nonempty, at least one primitive prime divisor
\[
p\mid 2^{u-1}-1,\qquad \operatorname{ord}_p(2)=u-1
\]
simultaneously killed all first-condition candidates by
\[
j\bmod p\notin\{0,1,2\}.
\]

This is an empirical phenomenon only. No general proof has been obtained.

## 11. A previous descent remains incomplete

The map
\[
(n,j)\mapsto\left(\frac n2,\frac s2\right),
\qquad
s=\frac{j(j-1)}{n-1},
\]
does preserve the next first divisibility condition in the uncorrected main branch.

However, the next second condition involving
\[
\frac n4-1
\]
has not been proved to be preserved.

Therefore this is not yet a valid infinite descent.

The former normalized variables \(D,E\) also reduce exactly to existing factor products:
\[
E=T^2Ra g_0h_0,\qquad
D=T^3Ba g_0^2h_0.
\]

So they are not independent new constraints.

## 12. Current best target

The most promising current system is
\[
\boxed{x^2BCg_0h_0-A^2ab=\delta_1}
\]
together with
\[
\boxed{\delta BC-Aab=2^{2v}W}
\]
and
\[
\boxed{\delta_1\,2^{u-2v-1}=AW+BCg_0h_0},
\]
plus
\[
\boxed{\gcd(W,ABC)=1},
\qquad
\boxed{\gcd(W,g_0h_0)\mid\delta_1},
\]
and the split equations
\[
\boxed{\delta B=a\zeta_0+2^{v-1}bh_0},
\]
\[
\boxed{\delta C=b\eta_0+2^{v-1}ag_0},
\]
\[
\boxed{\eta_0\zeta_0=\delta A+2^{2v-2}g_0h_0}.
\]

The weak determinant system admits infinite fake Mersenne solutions, so the next proof must use these split \(B,C,\eta,\zeta\) constraints or stronger Kummer digit information.

A good next subproblem is:

> Show that
> \[
> v_2(ag_0B+bh_0C)=v+1
> \]
> is incompatible with the three split equations above, the pairwise coprimality of \(A,B,C\), and
> \[
> u\ge4v+14.
> \]

If that fails, the next candidate is to combine primitive prime divisors of \(2^{u-1}-1\) with the CRT roots coming from \(2^u-1\).

## 13. Status discipline

Proved algebraically in this continuation:
- \(v_2(\delta BC-Aab)=2v\);
- \(v_2(ag_0B+bh_0C)=v+1\);
- positivity and oddness of \(W\);
- \(\delta BC=Aab+2^{2v}W\);
- \(\delta_1 2^{u-2v-1}=AW+BCg_0h_0\);
- \(\gcd(W,ABC)=1\);
- \(\gcd(W,g_0h_0)\mid\delta_1\);
- the weak determinant system is insufficient, via the explicit \(u=613\) periodic fake family;
- the odd-\(Q\) abstract generalization is false via \(Q=38335,j=26775\).

Finite computational observations only:
- no corrected low-level candidates for \(10\le u\le179\);
- no tested main-branch even candidates after the first condition plus the 3-adic Lucas screen;
- the primitive-prime divisor killing phenomenon through the tested range.

Still unproved:
- complete exclusion of the pure-power \(n=2^u\), \(i=3\) branch;
- a genuine infinite descent;
- a general primitive-prime theorem killing all CRT roots;
- contradiction from the new exact-valuation / \(W\)-system.
