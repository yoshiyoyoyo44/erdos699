# Erdős Problem 699 — Progress beyond the current GitHub version
## i = 3 nonsquare branch handoff note
Date: 2026-09-12

## 0. Purpose and baseline

This note records only the progress that goes beyond the current GitHub state of
`yoshiyoyoyo44/erdos699`, together with one correction to the attached evening continuation.

The GitHub baseline already contains the following established facts for a putative
counterexample at the smaller index \(i=3\):

\[
n=2^uM,\qquad u\ge 43,\qquad M\text{ odd},\qquad M^3<2^{u-2},
\]

and all branches in which

\[
\frac{j(n-j)}{n-1}
\]

is an integer square have been excluded for every odd \(M\) under the established
necessary conditions.  Thus the remaining problem is the nonsquare branch.

Nothing below is a complete proof of the \(i=3\) case or of Erdős Problem 699.

---

## 1. Symmetric quotient structure

Write

\[
n=CT,\qquad j=kT,
\]

with \(T\) odd, and define

\[
Q_1=\frac{CT-1}{\delta_1},\qquad
Q_2=\frac{CT/2-1}{\delta_2},
\qquad \delta_1,\delta_2\in\{1,3\}.
\]

Set

\[
L=\frac{k(C-k)}{Q_1}
 =\frac{\delta_1k(C-k)}{CT-1},
\]

and

\[
q=\delta_1k-TL,\qquad
q'=\delta_1(C-k)-TL.
\]

Then

\[
qQ_1=k(Tk-1),
\]

and symmetrically

\[
q'Q_1=(C-k)(T(C-k)-1).
\]

The two exact identities

\[
\boxed{qq'=L(T^2L-\delta_1)}
\]

and

\[
\boxed{q+q'+2TL=\delta_1C}
\]

are useful for exposing the second adjacent modulus.

---

## 2. Three-residue partition of \(Q_2\)

For each full prime-power component \(P\mid Q_2\), put

\[
x\equiv Tk\pmod P.
\]

Since \(CT\equiv2\pmod P\), the second adjacent congruence forces

\[
\boxed{x\in\{0,1,2\}\pmod P.}
\]

Moreover

\[
T^2L\equiv\delta_1x(2-x)\pmod P,
\]

\[
Tq\equiv\delta_1x(x-1)\pmod P,
\]

\[
Tq'\equiv\delta_1(x-1)(x-2)\pmod P.
\]

Partition the full prime-power factors of \(Q_2\) by these three residues:

\[
Q_2=ABC,
\]

where

- \(A\): \(x=1\),
- \(B\): \(x=0\),
- \(C\): \(x=2\).

Then \(A,B,C\) are pairwise coprime and

\[
\boxed{AB\mid q,\qquad AC\mid q',\qquad BC\mid L.}
\]

At the \(A\)-block both \(q\) and \(q'\) contain the full prime-power component,
while \(L\) is a unit, hence

\[
\boxed{A^2\mid T^2L-\delta_1.}
\]

Thus one may write

\[
q=ABa_0,\qquad
q'=ACb_0,\qquad
L=BCc_0,\qquad
T^2L-\delta_1=A^2d_0,
\]

with

\[
\boxed{a_0b_0=c_0d_0.}
\]

Combining the sum identity with \(CT=2\delta_2ABC+2\) gives

\[
\boxed{
T(Ba_0+Cb_0)+2Ad_0
=
2\delta_1\delta_2BC.
}
\]

This is a general positive-integer normal form for the remaining nonsquare branch.

---

## 3. Principal branch and correction to the evening note

In the principal branch

\[
T=1,\qquad \delta_1=\delta_2=1,
\]

put

\[
Q=\frac C2-1,
\qquad Q_2=Q,
\qquad Q+1=\frac C2.
\]

Since \(q,q'\) are even, write

\[
q=2r,\qquad q'=2r'.
\]

Then

\[
\boxed{4rr'=L(L-1)}
\]

and

\[
\boxed{L+r+r'=Q+1.}
\]

For every full prime-power component \(P\mid Q\), exactly one of
\(L,r,r'\) is \(1\pmod P\) and the other two are \(0\pmod P\).

With the same \(A,B,C\) convention as above:

- \(A\): \(L\equiv1\),
- \(B\): \(r'\equiv1\),
- \(C\): \(r\equiv1\).

The attached evening note has an assignment error in the formulas for \(r,r'\).
The correct parametrization is

\[
\boxed{
L=BCx,\qquad
r=ABz,\qquad
r'=ACy.
}
\]

Since \(L-1=A^2w\), the correct principal system is

\[
\boxed{
BCx-A^2w=1,
}
\]

\[
\boxed{
Bz+Cy+Aw=BC,
}
\]

\[
\boxed{
xw=4yz.
}
\]

Also \(A,B,C>1\), so

\[
\boxed{\omega(Q)\ge3.}
\]

The previously obtained quantitative bounds remain:

\[
r>\sqrt Q,
\]

\[
k>2Q^{3/4},
\]

\[
L>Q^{3/4},
\]

hence

\[
Q^{3/4}<L<\frac{Q+1}{2}.
\]

---

## 4. New second partition: complete four-corner factorization

A further structural step is obtained by factoring the first adjacent modulus

\[
Q_1=RS
\]

according to its two allowed residue classes.

Choose the convention

- \(R\): full prime-power components on which \(Tk\equiv1\),
- \(S\): full prime-power components on which \(Tk\equiv0\).

Then the two quotient identities force positive integers \(a,b,g,h\) such that

\[
\boxed{
k=SBg,
}
\]

\[
\boxed{
Tk-1=RAa,
}
\]

\[
\boxed{
C-k=RCh,
}
\]

\[
\boxed{
T(C-k)-1=SAb.
}
\]

This immediately yields

\[
\boxed{
q=ABag,
}
\]

\[
\boxed{
q'=ACbh,
}
\]

and, directly from

\[
L=\frac{k(C-k)}{Q_1},
\]

one gets

\[
\boxed{
L=BCgh.
}
\]

Using \(qq'=L(T^2L-\delta_1)\),

\[
\boxed{
T^2BCgh-A^2ab=\delta_1.
}
\]

Equivalently,

\[
\boxed{
T^2L-\delta_1=A^2ab.
}
\]

The linear relations are

\[
\boxed{
\delta_1S=Aa+TCh,
}
\]

\[
\boxed{
\delta_1R=Ab+TBg.
}
\]

Thus the earlier relation \(a_0b_0=c_0d_0\) is not merely an accidental product
identity: after the \(Q_1\)-partition, the four cofactors split into a genuine
rank-one four-corner structure

\[
a_0=ag,\qquad
b_0=bh,\qquad
c_0=gh,\qquad
d_0=ab.
\]

This is one of the main new structural advances beyond the GitHub version.

---

## 5. Unimodular structure in the principal branch

For

\[
T=\delta_1=\delta_2=1,
\]

the four-corner identity reduces to

\[
\boxed{
BCgh-A^2ab=1.
}
\]

Equivalently,

\[
\boxed{
(Ch)(Bg)-(Aa)(Ab)=1.
}
\]

Hence

\[
\det
\begin{pmatrix}
Aa & Ch\\
Bg & Ab
\end{pmatrix}
=-1.
\]

So the principal nonsquare branch contains a positive unimodular
\(2\times2\) matrix hidden inside the two adjacent-modulus factorizations.

This implies strong cross-coprimality.  In particular, any common divisor of a
factor from \(Ch,Bg\) and a factor from \(Aa,Ab\) must be \(1\).  Examples include

\[
\gcd(Ch,Aa)=1,\qquad
\gcd(Ch,Ab)=1,
\]

\[
\gcd(Bg,Aa)=1,\qquad
\gcd(Bg,Ab)=1.
\]

The likely next route is to exploit this unimodular/continued-fraction structure
together with the special shape

\[
ABC+1=2^m
\quad\text{or}\quad
ABC+1=3\cdot2^m.
\]

---

## 6. Two additional square-divisibility lifts

The \(x=0\) and \(x=2\) blocks yield two further square divisibilities that were
not present in the GitHub version.

Define

\[
X:=2Tq+T^2L,
\qquad
Y:=2Tq'+T^2L.
\]

Then

\[
X
=
\frac{\delta_1\,j(n+j-2)}{n-1},
\]

so on the \(B\)-block both factors in the numerator vanish. Therefore

\[
\boxed{B^2\mid 2Tq+T^2L.}
\]

Similarly,

\[
Y
=
\frac{\delta_1\,(n-j)(2n-j-2)}{n-1},
\]

and on the \(C\)-block both numerator factors vanish. Therefore

\[
\boxed{C^2\mid 2Tq'+T^2L.}
\]

Write

\[
B^2E=2Tq+T^2L,
\]

\[
C^2F=2Tq'+T^2L.
\]

Using only the exact quotient identities,

\[
\boxed{
EF
=
T^2c_0\left(T^2c_0+4\delta_1\delta_2A\right).
}
\]

After the four-corner factorization \(c_0=gh\),

\[
\boxed{
EF
=
T^2gh\left(T^2gh+4\delta_1\delta_2A\right).
}
\]

This gives a second layer of square-divisibility structure after the
\(A^2\mid T^2L-\delta_1\) lift.

---

## 7. Important caution: quarter-root descent is not yet proved

A tempting next step is to try to divide the new quotients \(E,F\) further by
\(g,h\) and derive a relation of the form

\[
\eta\zeta=T^2gh+4\delta_1\delta_2A.
\]

At present this is **not justified in full generality**.

The obstruction is that one cannot simply assume

\[
\gcd(B,g)=1
\quad\text{or}\quad
\gcd(C,h)=1.
\]

The full \(B\)- or \(C\)-prime-power appearing in \(Q_2\) may occur with additional
valuation inside \(g\) or \(h\).  Thus the square divisibility

\[
B^2\mid B\,g(\cdots)
\]

does not by itself imply that the remaining parenthesis is divisible by \(B\).

Therefore the stronger claimed “quarter-root descent” should currently be treated
as a promising target, not as an established lemma.

A refined \(p\)-adic splitting of the \(B\)- and \(C\)-blocks may recover such a
descent, but that additional partition has not yet been completed.

---

## 8. Best current targets for continuation

The strongest clean new structure beyond GitHub is now:

\[
Q_2=ABC
\]

together with

\[
Q_1=RS,
\]

and the four-corner factorization

\[
k=SBg,\qquad
Tk-1=RAa,
\]

\[
C-k=RCh,\qquad
T(C-k)-1=SAb,
\]

plus

\[
L=BCgh,
\]

\[
T^2BCgh-A^2ab=\delta_1,
\]

\[
\delta_1S=Aa+TCh,
\]

\[
\delta_1R=Ab+TBg.
\]

In the principal branch this becomes the unimodular equation

\[
(Ch)(Bg)-(Aa)(Ab)=1.
\]

The most promising next directions are:

1. exploit the positive unimodular matrix via continued fractions / best approximants;
2. combine that structure with \(ABC+1=2^m\) or \(3\cdot2^m\);
3. refine the \(B\)- and \(C\)-blocks \(p\)-adically so that the new square lifts
   \(B^2\mid X\), \(C^2\mid Y\) produce a genuine smaller self-similar system;
4. use the cross-coprimality forced by the determinant \(=\pm1\) to constrain
   which primes can reappear in the second-layer cofactors.

---

## 9. Current status

What is new beyond the GitHub version:

- symmetric \(q'\) quotient and exact \(qq'\) / sum identities;
- full three-residue decomposition \(Q_2=ABC\);
- \(A^2\mid T^2L-\delta_1\);
- general positive-integer normal form;
- corrected principal parametrization;
- \(\omega(Q)\ge3\) in the principal branch;
- principal \(Q^{3/4}\)-scale lower bounds;
- second decomposition \(Q_1=RS\);
- complete four-corner factorization \(a_0=ag,\ b_0=bh,\ c_0=gh,\ d_0=ab\);
- principal unimodular determinant structure;
- new square lifts on the \(B\)- and \(C\)-blocks;
- product identity for the two new square-lift quotients.

Still unresolved:

- principal nonsquare branch;
- general \(T>1\) nonsquare branch;
- a valid self-similar infinite descent;
- a universal upper bound on \(v_2(Q+1)\);
- the full \(i=3\) case;
- Erdős Problem 699.
