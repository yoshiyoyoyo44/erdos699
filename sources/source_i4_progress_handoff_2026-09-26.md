# Erdős Problem 699 — i=4 continuation handoff

Date: 2026-09-26 JST  
Repository: `yoshiyoyoyo44/erdos699`  
GitHub baseline checked: `5024fc5fb1beec81e4a8c1d2eee4ff4230c58cc4`  
Primary source handoff: `erdos699_single_handoff_github_assumed_2026-09-26.md`

## Status warning

This note records continuation research beyond GitHub HEAD `5024fc5`.

It does **not** claim a complete solution of Erdős Problem 699, nor a complete solution of `i=4`.

The original problem remains:

\[
1\le i<j\le n/2,\qquad
\exists p\ge i:\quad p\mid\gcd\!\left(\binom ni,\binom nj\right).
\]

Do not replace `p>=i` by `p>i`.

At the checked GitHub baseline, the solved indices are

\[
\boxed{i=1,2,29\quad\text{and}\quad i\ge35},
\]

and the unresolved indices are

\[
\boxed{3\le i\le34,\qquad i\ne29}.
\]

The work below concentrates on `i=4`.

---

# 1. Baseline i=4 structure inherited from GitHub + previous handoff

For an `i=4` counterexample, only the primes `2,3` may divide

\[
\gcd\!\left(\binom n4,\binom nj\right).
\]

For `s=0,1,2,3`, define the `p>=5` part

\[
R_s=\frac{n-s}{2^{v_2(n-s)}3^{v_3(n-s)}}.
\]

For a counterexample, Kummer gives

\[
R_s\mid\prod_{k=0}^{s}(j-k).
\]

Define

\[
B_{s,k}=\gcd(R_s,j-k),\qquad0\le k\le s.
\]

Then

\[
R_s=\prod_{k=0}^{s}B_{s,k}.
\]

All nontrivial `B_{s,k}` are pairwise coprime across distinct cells.

The column/diagonal divisibilities are

\[
\prod_{s=k}^{3}B_{s,k}\mid j-k,
\]

and

\[
\prod_{s=v}^{3}B_{s,s-v}\mid n-j-v.
\]

For `n>=10^87`, the checked GitHub pairwise-position theorem yields

\[
\boxed{B_xB_y\le3(n-3)}
\]

for any two distinct cells.

The earlier continuation classified every `i=4` counterexample into

\[
\boxed{n\bmod36\in\{4,8,9,12,16,18,20,27,28,32\}}.
\]

The classes

\[
\{4,8,12,16,32\}\pmod{36}
\]

transfer directly to the existing `i=3` counterexample machinery.

The genuinely `i=4` classes left for direct treatment are therefore

\[
\boxed{9,18,20,27,28\pmod{36}}.
\]

---

# 2. First strengthening: two non-q rows split independently of q

For each of the five genuinely `i=4` residue classes, among rows `1,2,3` there is one row carrying the largest relevant small-prime power `q`:

- `9 mod 36`: q-row = row 1, with a large power of `2`;
- `18 mod 36`: q-row = row 2, with a large power of `2`;
- `27 mod 36`: q-row = row 3, with a large power of `2`;
- `20 mod 36`: q-row = row 2, with a large power of `3`;
- `28 mod 36`: q-row = row 1, with a large power of `3`.

The other two rows have `R_s` bounded below by a fixed positive multiple of `n`, independently of the size of `q`.

If one such non-q row had only one occupied cell, then its unique cell would be `\gg n`. The pairwise bound

\[
B_xB_y\le3(n-3)
\]

would force every cell in the other non-q row to be `O(1)`. Since that row has at most four cells, its row product would become `O(1)`, contradicting its `\gg n` lower bound for `n>=10^87`.

Hence:

\[
\boxed{\text{each of the two non-q rows has at least two occupied cells}.}
\]

This conclusion is independent of the magnitude of `q`.

Therefore, if fewer than six cells are occupied among rows `1,2,3`, only two structural possibilities remain:

1. q-row has exactly one occupied cell and the two non-q rows have exactly two each (`2+2+1=5`);
2. q-row has zero occupied cells and the two non-q rows have `2+3=5` cells in total.

The second possibility was an important caveat discovered during the continuation: `R_q=1` can occur, so a q-row must **not** automatically be assumed occupied.

---

# 3. q-row occupied: complete 5-cell elimination for 18, 20, 27 mod 36

## 3.1 The class n ≡ 20 (mod 36)

Here

\[
R_1=n-1,\qquad
R_2=\frac{n-2}{2q},\qquad
R_3=n-3,
\]

where

\[
q=3^{\max_{0\le s\le3}v_3(n-s)}=3^{v_3(n-2)}.
\]

Assume the q-row is occupied and there are only five occupied cells. Then rows 1 and 3 have exactly two cells each, and row 2 has exactly one.

Column/diagonal capacity arguments reduce the support to two branches.

### Branch A

Use

\[
B_{1,0}=A,\quad B_{1,1}=B,\quad B_{2,2}=E,\quad
B_{3,0}=C,\quad B_{3,2}=D.
\]

The line divisibilities force

\[
j=AC,\qquad y-1=2AD,\qquad y=n-j.
\]

The row products give

\[
AB-CD=2.
\]

Introduce `t>0` by

\[
D=A+2t.
\]

Then

\[
F:=\frac{A^2-1}{t},
\]

and

\[
C=2A+F,\qquad B=4A+4t+F.
\]

Equivalently,

\[
\boxed{tB=D^2-1}.
\]

The previously unused column condition

\[
B\mid j-1=AC-1
\]

reduces to

\[
\boxed{B\mid4Dt-3}.
\]

Set

\[
m=\frac{4Dt-3}{B}.
\]

Then

\[
0<m<D,
\]

and, using `tB=D^2-1`,

\[
m\equiv3t\pmod D.
\]

Since `D>2t`, only two cases are possible.

- `m=3t` gives `3D=4t`, contradicting `D>2t`.
- `m=3t-D` gives
  \[
  D^2-3Dt+4t^2-1=0.
  \]
  As a quadratic in `D`, its discriminant is
  \[
  4-7t^2<0.
  \]

Hence Branch A is impossible.

### Branch B

Use

\[
B_{1,0}=A,\quad B_{1,1}=B,\quad B_{2,0}=E,\quad
B_{3,1}=C,\quad B_{3,3}=D.
\]

One obtains

\[
D=B+2t,
\]

\[
F=\frac{B^2-1}{t},
\]

\[
C=2B+F,\qquad A=4B+4t+F.
\]

Again

\[
tA=D^2-1.
\]

The unused column condition `A|j` becomes

\[
\boxed{A\mid4Dt-1}.
\]

Set

\[
m=\frac{4Dt-1}{A}.
\]

Then

\[
0<m<D,\qquad m\equiv t\pmod D.
\]

Since `0<t<D`, one must have `m=t`, hence

\[
D^2-1=4Dt-1,
\]

so

\[
D=4t.
\]

But `D` is an odd product of primes `>=5`, contradiction.

Therefore:

\[
\boxed{\text{for }n\equiv20\pmod{36},\text{ the occupied-q-row 5-cell branch is impossible}.}
\]

---

## 3.2 The class n ≡ 18 (mod 36)

Here

\[
R_1=n-1,\qquad
R_2=\frac{n-2}{q},\qquad
R_3=\frac{n-3}{3},
\]

with the q-row equal to row 2.

If the q-row is occupied and there are only five cells, row 1 has both cells occupied and row 3 has exactly two cells. There are six possible supports in row 3:

\[
\{0,1\},\{0,2\},\{0,3\},\{1,2\},\{1,3\},\{2,3\}.
\]

All six are eliminated.

### Support {0,1}

Writing the row-1 cells as `A,B` and the row-3 cells as `C,D`, one has

\[
AB-3CD=2.
\]

Line divisibilities yield

\[
j=rAC,\qquad j-1=sBD,
\]

with small positive integers `r,s`.

From `j<=n/2`,

\[
2rC\le B,\qquad2sD\le A.
\]

Multiplying gives

\[
4rsCD\le AB=3CD+2,
\]

impossible because `r,s>=1` and `CD>=25`.

### Support {0,3}

One obtains

\[
j=rAC,\qquad y=sBD.
\]

The row relation gives

\[
rA<3D,
\]

while the complementary bound gives

\[
sD<A.
\]

Thus `rs<3`. Parity forces `r=s=1`.

With

\[
H=B-C,\qquad T=A-D,
\]

one derives

\[
HT=CD-1
\]

and finally

\[
\boxed{C(D^2-DT+T^2)=D+3T}.
\]

Since `0<T<2D`,

\[
D^2-DT+T^2\ge\frac34D^2,
\]

forcing `C<2`, contradicting `C>=5`.

### Support {1,2}

One gets

\[
j-1=rBC,\qquad y-1=sAD.
\]

The size bounds force `rs=1`, hence `r=s=1`.

With

\[
H=A-C,\qquad T=B-D,
\]

one obtains

\[
HT=CD+1
\]

and

\[
\boxed{C(D^2-DT+T^2)=T-D}.
\]

The right side is positive, so `T>D`. Put `x=T-D>0`; then

\[
D^2-DT+T^2=D^2+Dx+x^2>x,
\]

forcing `C<1`, contradiction.

### Support {0,2}

One has

\[
j=rAC,\qquad y-1=sAD.
\]

Define

\[
L=3D-rA>0.
\]

Then

\[
CL=sAD-2,
\]

and

\[
B=\frac{3sD^2-2r}{L}.
\]

The remaining column condition gives

\[
\boxed{B\mid sDL-3r}.
\]

Set

\[
m=\frac{sDL-3r}{B}.
\]

Reduction mod `D` yields

\[
2m\equiv3L\pmod D.
\]

Size bounds reduce the integer parameter to `k=-4` or `k=-3` in

\[
2m=3L+kD.
\]

For `k=-3`,

\[
s(2L^2-9DL+9D^2)=6r,
\]

and the only boundary candidate forces an occupied cell equal to `2`, impossible.

For `k=-4`,

\[
s(2L^2-9DL+12D^2)=8r.
\]

The quadratic on the left is at least `(15/8)D^2`, so the left side exceeds `46`, while `8r<=32`, contradiction.

### Support {1,3}

After reduction to the final local cases, only the coefficient pair `r=3,s=2` survives preliminary constraints.

Writing `L=3H`, the cell `C` must equal one of

\[
C=\frac{4(3H-2D)}3,
\]

or

\[
C=\frac{6H-5D}{3}.
\]

Since `3` does not divide the occupied large-prime cell product `D`, neither expression is integral. Contradiction.

### Support {2,3}

Introduce

\[
H=sB^2-3rC^2>0.
\]

Then

\[
DH=B+2rC,
\]

\[
AH=2sB+3C,
\]

and elimination gives

\[
\boxed{H(rA^2-3sD^2)=4rs-3}.
\]

Let

\[
c=\frac{4rs-3}{H}.
\]

Then

\[
rA^2-3sD^2=c,
\]

\[
B=\frac{2rA-3D}{c},\qquad
C=\frac{2sD-A}{c}.
\]

From `j>=5`,

\[
A>sD.
\]

If `rs>=3`, then

\[
c=rA^2-3sD^2>4rs-3,
\]

contradicting `c | (4rs-3)`.

Hence `rs=2`.

- `(r,s)=(1,2)` forces `c=1` and
  \[
  A^2-6D^2=1,
  \]
  impossible mod `8` for odd `A,D`.
- `(r,s)=(2,1)` forces `c=5` and
  \[
  2A^2-3D^2=5,
  \]
  again impossible mod `8` for odd `A,D`.

Therefore all six row-3 supports are impossible:

\[
\boxed{\text{for }n\equiv18\pmod{36},\text{ the occupied-q-row 5-cell branch is impossible}.}
\]

---

## 3.3 The class n ≡ 27 (mod 36)

Here the q-row is row 3. In a five-cell occupied-q configuration, row 1 has both cells occupied and row 2 has two of its three cells occupied.

Write row-1 cells as `A,B`. The row products give an identity of the form

\[
\boxed{2AB-CD=1}
\]

for the two occupied row-2 cells `C,D`.

There are three row-2 supports.

### Support {0,1}

Line divisibilities give

\[
j=rAC,\qquad y-1=sAD.
\]

The row identities imply

\[
D>rA.
\]

Also

\[
BD\mid j-1.
\]

Set

\[
m=\frac{j-1}{B}.
\]

Then `D|m`, but `j<=AB` implies

\[
m<A<D,
\]

impossible.

### Support {0,2}

Here

\[
j=rAC,\qquad y=sBD.
\]

Again `D>rA`.

Eliminating the row identities gives

\[
\boxed{\frac{j-1}{B}=2A-sD}.
\]

The left side is positive, so `2A>sD`.

Parity gives `rs>=2`, while `D>rA` implies

\[
sD>rsA\ge2A,
\]

contradiction.

### Support {1,2}

Here

\[
y-1=rAC,\qquad y=sBD.
\]

Set

\[
H=2sB^2-rC^2.
\]

Then

\[
DH=2B+rC,
\]

\[
AH=sB+C.
\]

For `rs>2`, elimination shows that positivity of `C` requires

\[
2A-sD<0,
\]

but `j>=5` gives

\[
j=B(2A-sD)+1,
\]

so `2A-sD>0`, contradiction.

For `rs=2`, the two possibilities force either `D=A` or `D=2A`, both impossible for distinct odd occupied cell products.

Therefore:

\[
\boxed{\text{for }n\equiv27\pmod{36},\text{ the occupied-q-row 5-cell branch is impossible}.}
\]

---

# 4. Empty q-row branches: all five pure-power escape families eliminated

A q-row is empty exactly when its large-prime part is `1`. This produces a very rigid pure-power neighbor equation. All five genuinely `i=4` residue classes were checked.

## 4.1 n ≡ 18 (mod 36): n = 2^e + 2

Empty row 2 gives

\[
n-2=2^e,
\]

so

\[
\boxed{n=2^e+2,\qquad e\equiv4\pmod6}.
\]

Let

\[
T=3^{v_3(2^{e-1}+1)}.
\]

LTE gives

\[
T=3^{1+v_3(e-1)}\le3(e-1).
\]

Let

\[
R_0=\frac{n}{2T}.
\]

Row 0 gives

\[
j=aR_0,\qquad1\le a\le T.
\]

Since `n-1` is coprime to `6`, row 1 gives

\[
n-1\mid j(j-1).
\]

Using `2TR_0=n\equiv1 (mod n-1)` gives

\[
\boxed{n-1\mid a(a-2T)}.
\]

But

\[
0<|a(a-2T)|\le T^2\le9(e-1)^2.
\]

For `e>=10`,

\[
9(e-1)^2<2^e+1=n-1,
\]

contradiction. The only smaller congruent exponent `e=4` gives `n=18`, which is directly non-counterexample.

Thus the empty row-2 branch is completely eliminated.

---

## 4.2 n ≡ 20 (mod 36): n = 2(3^a + 1)

Empty row 2 gives

\[
n-2=2\cdot3^a,
\]

hence

\[
\boxed{n=2(3^a+1),\qquad a\ge2}.
\]

Let

\[
S=2^{v_2(3^a+1)}.
\]

Then `S` is `2` or `4`, so `S<=4`.

Put

\[
R_0=\frac{3^a+1}{S}.
\]

Then `n=2SR_0`, and row 0 yields

\[
j=bR_0,\qquad1\le b\le S.
\]

Since

\[
R_1=n-1=2\cdot3^a+1,
\]

row 1 gives

\[
n-1\mid j(j-1).
\]

Using `2SR_0=n\equiv1 (mod n-1)` yields

\[
\boxed{n-1\mid b(b-2S)}.
\]

But

\[
0<|b(b-2S)|\le S^2\le16<n-1,
\]

contradiction.

Thus the empty row-2 branch is completely eliminated.

---

## 4.3 n ≡ 27 (mod 36): n = 3(2^e + 1)

Empty row 3 gives

\[
n-3=3\cdot2^e,
\]

hence

\[
\boxed{n=3(2^e+1)},
\]

with `e` odd (and the residue condition fixes the appropriate odd congruence class).

Let

\[
T=3^{v_3(2^e+1)}=3^{1+v_3(e)}.
\]

Put

\[
R_0=\frac{2^e+1}{T},
\]

so `n=3TR_0`.

Row 0 yields

\[
j=aR_0,
\]

with `a` bounded by `O(T)` because `j<=n/2`.

Row 2 has

\[
R_2=n-2=3\cdot2^e+1.
\]

Hence

\[
R_2\mid j(j-1)(j-2).
\]

Using `3TR_0=n\equiv2 (mod R_2)` gives

\[
\boxed{R_2\mid2a(2a-3T)(2a-6T)}.
\]

The right side is `O(T^3)=O(e^3)`, while `R_2` grows like `2^e`. Thus all sufficiently large `e` are excluded by size. The remaining small odd exponents were checked directly; no counterexample survives.

Thus the empty row-3 branch is completely eliminated.

---

## 4.4 n ≡ 9 (mod 36): n = 2^e + 1

Empty row 1 gives

\[
n-1=2^e,
\]

so

\[
\boxed{n=2^e+1,\qquad e\equiv3\pmod6}.
\]

Let

\[
T=3^{1+v_3(e)}
\]

and

\[
R_0=\frac{n}{T}.
\]

Row 0 yields

\[
j=aR_0,\qquad2a<T.
\]

Row 2 has

\[
R_2=n-2=2^e-1.
\]

Hence

\[
R_2\mid j(j-1)(j-2).
\]

Using `TR_0=n\equiv2 (mod R_2)` gives

\[
\boxed{2^e-1\mid2a(2a-T)(2a-2T)}.
\]

The right side is `O(T^3)=O(e^3)`, while the left side is exponential in `e`. Thus large exponents are impossible; the finite small exponents are directly excluded.

Therefore the empty row-1 branch is completely eliminated.

---

## 4.5 n ≡ 28 (mod 36): n = 3^a + 1

Empty row 1 gives

\[
n-1=3^a,
\]

so

\[
\boxed{n=3^a+1},
\]

with the relevant residue forcing odd `a>=3`.

Then

\[
v_2(n)=2,
\]

so

\[
R_0=\frac n4.
\]

Row 0 gives

\[
j=bR_0,\qquad b\in\{1,2\}.
\]

Row 2 has

\[
R_2=\frac{n-2}{2}=\frac{3^a-1}{2}.
\]

Because `2R_0\equiv1 (mod R_2)`, row 2 gives

\[
R_2\mid b(b-2)(b-4).
\]

For `b=1`, this forces `R_2|3`, impossible. Hence `b=2`, so

\[
j=n/2.
\]

Now

\[
R_3=n-3=3^a-2.
\]

Row 3 gives

\[
R_3\mid j(j-1)(j-2)(j-3).
\]

Multiplying by `16` and using `2j=n\equiv3 (mod R_3)` yields

\[
\boxed{R_3\mid9},
\]

but `R_3>=25`, contradiction.

Thus the empty row-1 branch is completely eliminated.

---

# 5. Consequence: unconditional six-cell theorem for 18, 20, 27 mod 36

For each of

\[
\boxed{18,20,27\pmod{36}},
\]

we now have:

1. the two non-q rows each have at least two occupied cells;
2. the q-row cannot be empty;
3. the q-row cannot have exactly one occupied cell in a five-cell configuration.

Therefore every `i=4` counterexample with `n>=10^87` in these three residue classes must satisfy

\[
\boxed{
\#\{(s,k):1\le s\le3,\ B_{s,k}>1\}\ge6.
}
\]

Since all occupied `B_{s,k}` are pairwise coprime and each contains at least one prime `>=5`, this implies at least six distinct primes `>=5` occur across the row factors.

This improves the previous conditional six-prime theorem: for these three classes, the condition of the form

\[
n-3>Cq^4
\]

is no longer needed.

---

# 6. What remains for five-cell geometry: only 9 and 28 mod 36

The empty-q-row branches for `9` and `28 mod 36` have also been eliminated, but the occupied-q-row five-cell configurations have not yet all been eliminated.

Because the two non-q rows each have at least two cells, every hypothetical five-cell configuration in these two classes has exactly

\[
\boxed{2+2+1}
\]

occupied cells:

- q-row: exactly one occupied cell;
- each non-q row: exactly two occupied cells.

The raw support count is

\[
2\cdot\binom32\binom42=36.
\]

Here the factor `2` is the choice of the one occupied cell in the two-cell q-row.

---

## 6.1 n ≡ 28 (mod 36)

The q-row is row 1. The heavy rows are rows 2 and 3, with

\[
R_2=\frac{n-2}{2},\qquad
R_3=n-3.
\]

Hence

\[
R_2R_3=\frac{(n-2)(n-3)}2>\frac{n^2}{4}
\]

for the large-n range under consideration.

If the four heavy cells can be covered by two permitted column/diagonal lines, with at least one line a column, then their product is at most

\[
\frac n2\cdot n=\frac{n^2}{2},
\]

and in the sharper configurations the column/diagonal capacities give the needed contradiction against the exact heavy-row product. Likewise, if all five cells lie on two diagonals, the q-row cell contributes at least `5`, so the full product exceeds the two-diagonal capacity in the relevant configurations.

A direct support enumeration using these simultaneous line capacities eliminates exactly half of the raw supports:

\[
\boxed{36\to18}.
\]

A particularly useful exact row identity for the remaining analysis is the following. If the two occupied row-2 cells have product `AB` and the two occupied row-3 cells have product `CD`, then

\[
AB=\frac{n-2}{2},\qquad CD=n-3,
\]

so

\[
\boxed{2AB-CD=1}.
\]

This is the recommended next target.

---

## 6.2 n ≡ 9 (mod 36)

The q-row is row 1. The heavy rows are rows 2 and 3, with

\[
R_2=n-2,
\]

and, after removing the `2,3` part,

\[
R_3=\frac{n-3}{6}.
\]

Thus

\[
R_2R_3=\frac{(n-2)(n-3)}6.
\]

Because the q-row is occupied in the five-cell case, the total five-cell product is at least

\[
5R_2R_3
=\frac{5(n-2)(n-3)}6.
\]

Simultaneous column/diagonal capacity eliminates every support where all five occupied cells are covered by two allowed lines and at least one of those lines is a column.

This gives the first reduction

\[
\boxed{36\to30}.
\]

For the heavy rows, if the row-2 occupied product is `AB` and the row-3 occupied product is `CD`, then

\[
AB=n-2,
\]

\[
CD=\frac{n-3}{6},
\]

so

\[
\boxed{AB-6CD=1}.
\]

This is the natural exact identity to combine with the remaining support geometries.

---

# 7. Important correction to preserve in future work

During the continuation there was an intermediate overstatement that, after eliminating the one-cell q-row branches, the residue classes immediately had six occupied cells.

That was not yet justified because the q-row can have **zero** occupied cells when its large-prime part is `R_q=1`.

This issue has now been repaired:

- the empty-q pure-power branch was identified in every one of the five genuinely `i=4` residue classes;
- all five pure-power branches were eliminated;
- therefore the unconditional six-cell conclusion is now valid for `18,20,27 mod 36` because their one-cell q-row branches were also completely eliminated.

Do not omit this logical distinction in a formal write-up.

---

# 8. Current i=4 research status

For `n>=10^87`:

### Fully established in this continuation

\[
\boxed{n\equiv18,20,27\pmod{36}\Longrightarrow\text{at least six occupied cells in rows }1,2,3.}
\]

The empty-q branches are impossible for **all five** genuinely `i=4` classes

\[
\boxed{9,18,20,27,28\pmod{36}}.
\]

### Remaining five-cell branches

Only

\[
\boxed{9\pmod{36}\quad\text{and}\quad28\pmod{36}}
\]

still have unresolved occupied-q five-cell geometries.

Current support counts after line-capacity pruning:

\[
\boxed{28\pmod{36}:18\text{ supports remain}},
\]

\[
\boxed{9\pmod{36}:30\text{ supports remain}}.
\]

### Not proved

This work does **not** yet prove:

- that six occupied cells are themselves impossible;
- that `i=4` is solved;
- that the remaining `9,28 mod 36` five-cell branches are impossible;
- that the transferred classes `4,8,12,16,32` are solved solely by this continuation.

---

# 9. Next research tasks — recommended order

## Priority 1: finish the 28 mod 36 five-cell support classification

This is currently the cleanest target.

There are only 18 supports left after simultaneous column/diagonal pruning.

For each remaining support:

1. name the two row-2 occupied cells `A,B` and the two row-3 occupied cells `C,D`;
2. impose
   \[
   \boxed{2AB-CD=1};
   \]
3. introduce the small quotients coming from the relevant column and diagonal products, e.g.
   \[
   j-k=r\cdot(\text{column product}),
   \]
   \[
   n-j-v=s\cdot(\text{diagonal product});
   \]
4. use `j<=n/2` and the pairwise bound to show that `r,s` lie in a tiny finite set;
5. eliminate variables until one obtains either
   - a sign contradiction,
   - a parity contradiction,
   - a congruence contradiction mod `3`, `4`, or `8`,
   - or a Pell-type equation with impossible local data.

The successful patterns for `18` and `27 mod 36` should be reused aggressively.

The objective is

\[
\boxed{28\pmod{36}:18\to0}.
\]

If achieved, then every large counterexample in the `28 mod 36` class also has at least six occupied cells.

---

## Priority 2: finish the 9 mod 36 five-cell support classification

After the 28-class method is stabilized, apply the same machinery to the 30 remaining supports for `9 mod 36`.

Use the exact heavy-row identity

\[
\boxed{AB-6CD=1}.
\]

Because the coefficient `6` is larger than the coefficient `1` in the 28-class identity, the quotient inequalities may actually become stronger in supports where the row-3 cells share a line with row-2 cells.

The objective is

\[
\boxed{9\pmod{36}:30\to0}.
\]

If both priorities 1 and 2 succeed, all five genuinely `i=4` residue classes would satisfy the same unconditional six-cell condition for `n>=10^87`.

---

## Priority 3: prove six occupied cells are globally impossible

Once every residue class has at least six occupied cells, return to the original global target from the handoff:

- all occupied cells are pairwise coprime;
- every pair satisfies
  \[
  B_xB_y\le3(n-3);
  \]
- column products divide numbers `<=n/2`;
- diagonal products divide numbers `<n`;
- each row product is explicitly a large part of `n-s`.

The task is to show that six pairwise-coprime factors cannot simultaneously fit the row products and all line capacities.

Do **not** use only pairwise bounds. The point is to multiply several column and diagonal capacities simultaneously and compare against the exact product of row factors.

A useful computational subtask is a finite weighted-cover/linear-program search over the triangular cells

\[
(s,k),\qquad1\le s\le3,\quad0\le k\le s,
\]

looking for a universal combination of row-product lower bounds and column/diagonal upper bounds with exponent gap.

Any candidate inequality should then be converted to an exact symbolic proof.

---

## Priority 4: lower-n certification only after the infinite geometry closes

The present continuation is aimed at the large-`n` branch (`n>=10^87`) because the pairwise-position theorem is available there.

If a complete large-`n` contradiction for `i=4` is obtained, then treat the finite region below the threshold using the existing certificate infrastructure rather than mixing huge finite computation into the structural proof.

---

# 10. Suggested next-chat prompt

> Continue Erdős 699 at `i=4` from `erdos699_i4_progress_handoff_2026-09-26.md` and GitHub HEAD `5024fc5`. Do not redo the eliminated `18,20,27 mod 36` five-cell branches or any empty-q pure-power branch. Start with the 18 remaining occupied-q five-cell supports for `n≡28 (mod 36)`. Use `2AB-CD=1`, all column/diagonal divisibilities, `j<=n/2`, pairwise cell bounds, parity, and small quotient parameters. Goal: eliminate all 18 supports, with exact symbolic proofs rather than finite numerical search.

---

# Final checkpoint

The strongest clean new statement from this continuation is:

\[
\boxed{
\begin{array}{c}
\text{For }n\ge10^{87}\text{ and an }i=4\text{ counterexample,}\\[2mm]
 n\equiv18,20,27\pmod{36}
 \Longrightarrow
 \text{at least six occupied }B_{s,k}\text{ cells in rows }1,2,3.
\end{array}}
\]

In addition, the empty-q pure-power escape branch is impossible in every genuinely `i=4` residue class

\[
\boxed{9,18,20,27,28\pmod{36}}.
\]

The immediate frontier is therefore the finite occupied-q five-cell geometry for

\[
\boxed{28\pmod{36}\ (18\text{ supports})}
\]

and

\[
\boxed{9\pmod{36}\ (30\text{ supports})}.
\]

No claim of complete `i=4` solution is made at this checkpoint.
