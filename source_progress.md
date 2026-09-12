# Erdős Problem 699: determinant bounds, a large-index range, and restrictions at index 3

Date: 2026-09-11. Working research note generated in this conversation.

**Status.** The original sections below give a derivation of a determinant lower bound and a proof, using the explicitly stated published prime estimates, that the assertion of Erdős Problem 699 holds whenever the smaller index is at least **3,000,000**. A 2026-09-11 continuation, recorded in §11, keeps the factorial product in the determinant estimate and obtains a substantially stronger lower bound. Combined with deterministic local prime-gap sieving and exact prime-power residue certificates, this continuation has provisionally reduced the contiguous large-index range to **all indices i >= 304**. The algebraic strengthening is proved below; the new finite boundary is still labelled provisional until every determinant crossing used in the finite scan is replayed with the exact integer certificate (11.5), rather than high-precision logarithmic comparisons. This remains a partial result, not a complete solution of #699. No independent review or proof-assistant verification has occurred, and priority/novelty in the literature are not established.

**日本語の要点。** 共通因数を行列式で評価することで、\(i\ge3{,}000{,}000\) の場合を、すべての \(n,j\) について扱う証明を以下に記す。後続の強化では大きい添字の暫定連続境界を \(i\ge304\) まで下げている。\(i=3\) では、反例なら \(n=2^uM\)、\(u\ge13\)、\(M\) 奇数であり、3進例外を統一した因数分解降下からさらに \(M^3<162\,2^u\)、従って \(M<5.452\,2^{u/3}\) まで必要形を薄くできる。これにより反例候補となる \(n\le X\) の個数は \(E_3(X)=O(X^{1/4})\) まで改善する。なお \(i=3\) の完全排除はまだ閉じておらず、これらは #699 の完全証明ではない。独立レビュー・proof assistant 検証・文献上の新規性確認も未完である。

## 1. Statement and notation

Throughout,

\[
1\le i<j\le n/2,\qquad
A=\binom ni,\quad B=\binom nj,\quad D=\gcd(A,B).
\]

Problem 699 asks whether \(D\) always has a prime divisor \(p\ge i\). Its statement is recorded in [Formal Conjectures, problem 699](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/699.lean) and in [Erdős–Szekeres, 1978, Conjecture 1](https://users.renyi.hu/~p_erdos/1978-46.pdf).

For a nonnegative integer \(r\), write

\[
(x)_{\underline r}=x(x-1)\cdots(x-r+1),\qquad
(x)_{\overline r}=x(x+1)\cdots(x+r-1),
\]

with both empty products equal to 1. Define

\[
L_i=\operatorname{lcm}_{0\le h\le i}\binom ih,
\qquad m=\lfloor i/2\rfloor,\quad s=i-2m\in\{0,1\},\quad t=m+1.
\]

All logarithms are natural.

## 2. A common divisor of orbit coefficients

Put \(a=A/D\), \(b=B/D\); then \(\gcd(a,b)=1\). For \(0\le h\le i\), define

\[
X_h=\binom j{i-h}\binom{n-j}h.
\]

The factorial identity

\[
A\binom ih\binom{n-i}{j-i+h}=B X_h
\tag{2.1}
\]

implies \(a\mid X_h\) for every \(h\). All indices in (2.1) are in their permitted ranges because \(i<j\le n/2\). This orbit identity is also the starting point of [Bergman, *On common divisors of multinomial coefficients*, §2](https://arxiv.org/abs/0806.0607).

Set

\[
Y_h=\frac{L_i}{\binom ih}X_h
=\frac{L_i}{i!}(j)_{\underline{i-h}}(n-j)_{\underline h}.
\tag{2.2}
\]

Crucially, \(L_i/\binom ih\) is an integer, so \(a\mid Y_h\). The rational factor \(L_i/i!\) in the second expression is only an alternative formula for the same integer.

Let \(H=(Y_{r+q})_{0\le r,q<t}\). The indices do not exceed \(2t-2=2m\le i\), so every entry is defined. Consequently,

\[
a^t\mid\det H.
\tag{2.3}
\]

We must also establish that this determinant is nonzero before using its magnitude.

## 3. Evaluation of the determinant

We first prove a general identity:

\[
\det_{0\le r,q<t}
\left[\frac{(\alpha)_{\overline{r+q}}}{(\gamma)_{\overline{r+q}}}\right]
=\prod_{k=0}^{t-1}
\frac{k!(\alpha)_{\overline k}(\gamma-\alpha)_{\overline k}}
{(\gamma)_{\overline{t+k-1}}},
\tag{3.1}
\]

whenever the denominators are nonzero, first treating parameters for which the row factorizations are valid and then extending the rational identity where defined.

Factor \((\alpha)_{\overline r}/(\gamma)_{\overline{r+t-1}}\) from row \(r\). The remaining entry in column \(q\) is the polynomial

\[
P_q(r),\qquad
P_q(x)=(\alpha+x)_{\overline q}
(\gamma+x+q)_{\overline{t-1-q}}.
\]

Each polynomial has degree at most \(t-1\). Its evaluation matrix at \(x_r=-\alpha-r\) is lower triangular, since \(P_q(x_r)=0\) for \(q>r\), and its diagonal is

\[
P_r(x_r)=(-1)^r r!(\gamma-\alpha)_{\overline{t-1-r}}.
\]

Dividing this evaluation determinant by its Vandermonde determinant shows that the determinant of the polynomial coefficient matrix is

\[
\prod_{k=0}^{t-1}(\gamma-\alpha)_{\overline k}.
\]

The Vandermonde determinant at \(0,1,\ldots,t-1\) is 

\[
\prod_{k=0}^{t-1}k!.
\]

Restoring the row factors proves (3.1).

Now set

\[
Z_h=(j)_{\underline{i-h}}(n-j)_{\underline h},
\quad \alpha=j-n,\quad\gamma=j-i+1.
\]

Then

\[
Z_h=(j)_{\underline i}(-1)^h
\frac{(j-n)_{\overline h}}{(j-i+1)_{\overline h}}.
\]

The row and column signs cancel in the determinant. Using (3.1), cancelling falling-factorial factors, and taking absolute values gives

\[
T:=\left|\det_{0\le r,q<t}[Z_{r+q}]\right|
=\prod_{k=0}^{t-1}
k!\,(j)_{\underline{i-t-k+1}}
(n-j)_{\underline k}(n-i+1)_{\overline k}.
\tag{3.2}
\]

Every factor is strictly positive. In particular, \(i-t-k+1\ge0\), since \(t=m+1\) and \(i-2m=s\ge0\). This proves the required nonvanishing.

By (2.2),

\[
|\det H|=\left(\frac{L_i}{i!}\right)^t T.
\]

Combining this with (2.3), using that a nonzero integer multiple of \(a^t\) has magnitude at least \(a^t\), yields the exact lower bound

\[
\boxed{\displaystyle D\ge
\frac{(n)_{\underline i}}{L_i\,T^{1/t}}.}
\tag{3.3}
\]

## 4. A uniform lower bound

If \(i=2m\), formula (3.2) becomes

\[
T=\prod_{k=0}^{m}
k!\,(j)_{\underline k}(n-j)_{\underline k}
(n-i+1)_{\overline k}.
\]

If \(i=2m+1\), there is the additional factor \((j)_{\underline{m+1}}\) in this expression. In both cases,

\[
(j)_{\underline k}(n-j)_{\underline k}
\le(n^2/4)^k,\qquad
(n-i+1)_{\overline k}\le n^k,\qquad
k!\le m^k.
\]

The first inequality follows by pairing \((j-r)(n-j-r)\le n^2/4\); all these factors are positive. In the odd case, \((j)_{\underline{m+1}}\le(n/2)^{m+1}\). Hence

\[
T^{1/t}\le(n/2)^s(mn^3/4)^{m/2}.
\]

Since \((n)_{\underline i}\ge(n-i+1)^i\), (3.3) gives, for every \(i\ge2\),

\[
\boxed{\displaystyle
D\ge F_i(n):=
\frac{2^s}{L_i}
\left(\frac{4n}{m}\right)^{m/2}
\left(1-\frac{i-1}{n}\right)^i.}
\tag{4.1}
\]

For fixed \(i\), the exponent of \(n\) in this lower bound is 

\[
\frac12\lfloor i/2\rfloor.
\]

The normalization by \(L_i\), rather than by \(i!\), is essential to the uniform large-index argument.

## 5. Upper bound under the counterexample hypothesis

For any prime \(p\) and \(0\le k\le N\), Legendre's formula gives

\[
v_p\binom Nk=\sum_{e\ge1}
\left(\left\lfloor\frac N{p^e}\right\rfloor
-\left\lfloor\frac k{p^e}\right\rfloor
-\left\lfloor\frac{N-k}{p^e}\right\rfloor\right).
\]

Every summand is either 0 or 1, and summands with \(p^e>N\) vanish. Thus

\[
v_p\binom Nk\le\lfloor\log_p N\rfloor.
\tag{5.1}
\]

In particular,

\[
L_i\mid\operatorname{lcm}(1,\ldots,i),\qquad
\log L_i\le\psi(i),
\tag{5.2}
\]

where \(\psi(x)=\sum_{p^e\le x}\log p\).

If \(D\) has no prime divisor \(p\ge i\), let \(r_i=\pi(i-1)\). By (5.1),

\[
\boxed{D\le\prod_{p<i}p^{\lfloor\log_p n\rfloor}
\le n^{r_i}.}
\tag{5.3}
\]

Therefore \(F_i(n)>n^{r_i}\) is a rigorous sufficient condition for #699.

## 6. Explicit theorem for all indices at least 3,000,000

**Theorem.** For all integers

\[
3{,}000{,}000\le i<j\le n/2,
\]

there is a prime \(p\ge i\) dividing both \(\binom ni\) and \(\binom nj\).

### Published inputs

We use the following unconditional estimates, recorded in [Dusart, *Estimates of Some Functions Over Primes without R.H.*, arXiv:1002.0442](https://arxiv.org/abs/1002.0442):

1. Proposition 5.1: \(\theta(x)<(1+1/36260)x\) for \(x>0\).
2. Proposition 3.2: \(\psi(x)-\theta(x)<1.00007\sqrt{x}+1.78x^{1/3}\) for \(x>0\).
3. Theorem 6.9, (6.6): \(\pi(x)\le x/(\log x-1.1)\) for \(x>60{,}184\).
4. Schoenfeld's prime interval theorem, recalled at the start of Dusart §6.1.3: for \(x>2{,}010{,}759.9\), a prime lies strictly between \(x\) and \(x+x/16{,}597\).

These are external proven inputs; the finite arithmetic checks accompanying this note do not re-prove them.

### Proof: the range \(n<10{,}000i\)

Set \(x=n-i\). Then \(x\ge i+2>2{,}010{,}759.9\), and 

\[
x<9{,}999i,\qquad x/16{,}597<i.
\]

The fourth input supplies a prime

\[
n-i<p<n.
\]

Also \(p>n/2\ge j>i\). The factor \(p\) occurs in both falling products \((n)_{\underline i}\) and \((n)_{\underline j}\), and in neither denominator \(i!\), \(j!\). It therefore divides both binomial coefficients.

### Proof: the range \(n\ge10{,}000i\)

Put \(I=3{,}000{,}000\), \(C=10{,}000\). The first two inputs imply, for \(i\ge I\),

\[
\frac{\psi(i)}i
<1+\frac1{36260}+\frac{1.00007}{\sqrt{i}}+
\frac{1.78}{i^{2/3}}<1.001.
\tag{6.1}
\]

For example, \(\sqrt I>1700\) and \(I^{2/3}>20000\) verify the last strict inequality with rational bounds; all terms decrease as \(i\) increases. Thus \(\log L_i<1.001i\).

By (4.1), \(m\le i/2\), and \(m\ge(i-1)/2\),

\[
\frac{\log F_i(Ci)}i
\ge\left(\frac14-\frac1{4I}\right)\log(8C)
+\log(1-1/C)-1.001
>1.82.
\tag{6.2}
\]

For an entirely rational check of the strict margin, use

\[
\log80000>11.289,\qquad
\log(1-1/10000)\ge-1/9999.
\]

The resulting rational lower bound is greater than 1.82. Conversely, by the third input,

\[
\frac{r_i\log(Ci)}i
\le\frac{\log(Ci)}{\log i-1.1}
=1+\frac{\log C+1.1}{\log i-1.1}
<1+\frac{9.211+1.1}{14.9-1.1}
<1.75.
\tag{6.3}
\]

Here \(\log C<9.211\) and \(\log I>14.9\). The accompanying code certifies these logarithmic inequalities by rational series with a proved remainder bound, rather than relying on floating-point rounding.

Equations (6.2)–(6.3) show \(F_i(Ci)>(Ci)^{r_i}\). Finally,

\[
\frac{m}{2i}\ge\frac14-\frac1{4I}
>\frac1{\log i-1.1}\ge\frac{r_i}{i}.
\]

Hence \(m/2-r_i>0\), and

\[
\frac{F_i(n)}{n^{r_i}}
=\frac{2^s}{L_i}(4/m)^{m/2}
n^{m/2-r_i}\left(1-\frac{i-1}{n}\right)^i
\]

is increasing for real \(n\ge Ci\): both factors depending on \(n\) are positive and increasing. Therefore \(F_i(n)>n^{r_i}\) throughout this range, contradicting (5.3) for a putative counterexample. This completes the proof of the stated large-index theorem.

## 7. What remains for a complete solution

The elementary inequality \(D\ge\binom ni/\binom ji\ge2^i\) proves #699 when \(i=1,2\). The theorem above excludes every counterexample with \(i\ge3{,}000{,}000\). Thus a counterexample, if one exists, must have

\[
3\le i<3{,}000{,}000.
\]

This is a finite set of **indices**, not a finite set of triples: for each such \(i\), \(n\) is still unbounded. The determinant criterion gives effective cutoffs for fixed indices satisfying \(\lfloor i/2\rfloor/2>\pi(i-1)\), but that does not address every smaller index. In particular, it does not settle \(i=3\).

A natural next step is to use prime-power residue conditions in the remaining ranges. For example, if \(p>i\) and \(p^e\mid n-r\) with \(0\le r<i\), then \(p\mid\binom ni\). If also \(j\bmod p^e>r\), Legendre's formula shows \(p\mid\binom nj\). This supplies exact certificates, but a proof that an appropriate certificate always exists is still missing.

## 8. The case \(i=3\): necessary conditions for any counterexample

This section is elementary and independent of the prime-distribution estimates in §6. Throughout it, \(4\le j\le n/2\), so \(n\ge8\), and

\[
A=\binom n3,\qquad B=\binom nj,\qquad D=\gcd(A,B).
\]

A counterexample at \(i=3\) means precisely that \(D\) is a power of 2.

### 8.1. Two size bounds

The \(h=0\) case of (2.1) implies \(A/D\mid\binom j3\). Therefore

\[
D\ge\frac{\binom n3}{\binom j3}
=\frac{n(n-1)(n-2)}{j(j-1)(j-2)}>8.
\tag{8.1}
\]

Indeed \(n\ge2j\), and \((n-r)/(j-r)>2\) for \(r=1,2\).

For a short, self-contained specialization of the determinant argument, put \(a=A/D\) and

\[
Y_0=\frac{j(j-1)(j-2)}2,\qquad
Y_1=\frac{j(j-1)(n-j)}2,\qquad
Y_2=\frac{j(n-j)(n-j-1)}2.
\]

Equation (2.1) shows that these three integers are divisible by \(a\): they are respectively \(3X_0,X_1,X_2\). Direct expansion gives

\[
Y_0Y_2-Y_1^2
=-\frac{j^2(j-1)(n-j)(n-2)}4\ne0.
\]

Since \(a^2\) divides this determinant, it follows that

\[
D\ge
\frac{n(n-1)\sqrt{n-2}}{3j\sqrt{(j-1)(n-j)}}
\ge\frac{4(n-1)}{3n}\sqrt{n-2}
>\sqrt{n-2}.
\tag{8.2}
\]

For the middle inequality, \(j\le n/2\) and
\((j-1)(n-j)<j(n-j)\le n^2/4\). The last inequality uses \(n>4\).

### 8.2. A prime-power residue certificate

For a prime \(p\) and \(q=p^e\), Legendre's formula gives

\[
\nu_p\binom nj
=\sum_{k\ge1}
\left(
\left\lfloor\frac n{p^k}\right\rfloor
-\left\lfloor\frac j{p^k}\right\rfloor
-\left\lfloor\frac{n-j}{p^k}\right\rfloor
\right).
\]

Every summand is either 0 or 1. The summand at \(k=e\) is 1 exactly when \(j\bmod q>n\bmod q\). Consequently,

\[
j\bmod q>n\bmod q\quad\Longrightarrow\quad p\mid B.
\tag{8.3}
\]

Now let \(r\in\{0,1,2\}\), and let \(q=p^{\nu_p(n-r)}>3\) be a full odd prime-power component of \(n-r\). Then \(p\mid A\): for \(p\ge5\) there is no cancellation by 6, and for \(p=3\) the condition \(q>3\) leaves at least one factor of 3 after cancellation. Also \(n\bmod q=r\). Hence a counterexample necessarily satisfies

\[
j\bmod q\le r
\quad\text{for every such }(q,r).
\tag{8.4}
\]

Only necessity is asserted here; the congruences are not claimed to be sufficient for a counterexample.

One further elementary consequence will be useful. The identity
\(jB=n\binom{n-1}{j-1}\) gives

\[
\frac n{\gcd(n,j)}\mid B.
\tag{8.5}
\]

If \(p\) is odd, \(p\mid n\), and \(p\mid A\), absence of an odd common prime therefore forces
\(p^{\nu_p(n)}\mid j\).
Writing \(n=2^uM\) with \(M\) odd, a counterexample must satisfy

\[
\begin{cases}
M\mid j,&\nu_3(n)\ne1,\\
(M/3)\mid j,&\nu_3(n)=1.
\end{cases}
\tag{8.6}
\]

The exception for \(\nu_3(n)=1\) is necessary: that single factor of 3 is canceled in \(A=n(n-1)(n-2)/6\).

### 8.3. Odd \(n\) are impossible for a counterexample

If \(n\) is odd and \(\nu_3(n)\ne1\), (8.6) gives \(n\mid j\), contradicting \(0<j<n\). In the other case, \(n=3M\) with \(M\) odd and \(3\nmid M\), and (8.6) gives \(M\mid j\). Since \(j\le3M/2\), necessarily \(j=M\), so \(n=3j\).

Choose a prime divisor \(p\) of \(n-2\). The integer \(n-2>1\) is odd and not divisible by 3, so \(p\ge5\), and \(p\mid A\). But \(3j\equiv2\pmod p\). The residue \(j\bmod p\) cannot be 0, 1, or 2: these would imply respectively \(p\mid2\), \(p\mid1\), or \(p\mid4\). Thus \(j\bmod p>2=n\bmod p\), and (8.3) gives \(p\mid B\), a contradiction.

### 8.4. The case \(n\equiv2\pmod4\) is also impossible

Write \(n=2M\) with \(M\) odd. Equation (8.6), together with \(j\le M\), leaves only

\[
j=n/2,\quad j=n/3,\quad\text{or}\quad j=n/6.
\]

The last two possibilities arise only when \(\nu_3(n)=1\). Each can be excluded:

- If \(j=n/2\), take any full prime-power component \(q>3\) of the odd integer \(n-1\). Equation (8.4) requires \(j\bmod q\in\{0,1\}\), whereas \(2j\equiv1\pmod q\); neither residue works. Such a \(q\) exists, since the only positive odd integers with every full prime-power component at most 3 are 1 and 3, while \(n-1\ge7\).
- If \(j=n/3\), choose any prime \(p\mid n-1\). Here \(n-1\) is odd and not divisible by 3, so \(p\ge5\). The residues 0 and 1 for \(j\bmod p\) contradict \(3j\equiv1\pmod p\), and (8.3) supplies an odd common prime.
- If \(j=n/6\), every full prime-power component \(q\) of \(n-1\) has underlying prime at least 5. Equation (8.4) requires \(j\bmod q=s\in\{0,1\}\), and \(6j\equiv1\pmod q\) implies \(q\mid6s-1\). Thus necessarily \(q=5\). Unique factorization then gives \(n-1=5\), contrary to \(n\ge8\). Using full prime powers here rules out \(5^e\) with \(e>1\).

### 8.5. A sparse, explicitly described set of possible \(n\)

By §§8.3–8.4 a counterexample has \(4\mid n\). Write \(n=2^uM\), \(M\) odd, \(u\ge2\). Since \(\nu_2(n-1)=0\), \(\nu_2(n-2)=1\), and \(\nu_2(6)=1\),

\[
\nu_2(A)=u.
\]

If \(D\) is a power of 2, this gives \(D\le2^u\). Equations (8.1)–(8.2) imply

\[
2^u>8,\qquad n-2<2^{2u}.
\]

The first inequality gives \(u\ge4\). From the second and divisibility by \(2^u\), we have \(n\le2^{2u}\); equality is impossible since \(M=n/2^u\) is odd. Thus

\[
\boxed{\text{Any counterexample at }i=3\text{ must have }
n=2^uM,\quad u\ge4,\quad M\text{ odd},\quad1\le M<2^u.}
\tag{8.7}
\]

This already proves #699 for \(i=3\) and every \(n\) outside that explicit set, uniformly for all permitted \(j\).

Let \(E_3(X)\) count integers \(n\le X\) for which at least one \(j\) violates #699 at \(i=3\). Ignoring the restriction that \(M\) is odd only enlarges the count in (8.7). Put \(K=\lfloor\log_2\sqrt X\rfloor\). For \(X\ge1\),

\[
\begin{aligned}
E_3(X)
&\le\sum_{u=0}^{K}2^u+\sum_{u=K+1}^{\infty}\frac X{2^u}\\
&<2^{K+1}+\frac X{2^K}
\le3\sqrt X.
\end{aligned}
\tag{8.8}
\]

The last inequality follows from
\(\sqrt X/2<2^K\le\sqrt X\) and
\((2\cdot2^K-\sqrt X)(2^K-\sqrt X)\le0\).
Thus the set of \(n\) that admit an \(i=3\) counterexample has density 0, with an explicit square-root bound. This does not prove that the set is empty.

### 8.6. A finite, exact sieve excludes \(u\le12\)

For fixed \(u\), (8.7) leaves exactly \(2^{u-1}\) possible odd \(M\). The accompanying program checks all such \(M\) for \(4\le u\le12\). For each \(n=2^uM\), it factors \(n,n-1,n-2\) by certified trial division and applies every condition (8.4). A largest modulus \(q\) first restricts \(j\) to intervals \([bq,bq+r]\); only integers in those intervals and in \(4\le j\le n/2\) need testing against the remaining moduli. This covers every candidate \(j\) under the necessary conditions.

| \(u\) | Values of \(n\) examined | Candidate values of \(j\) examined | Survivors |
|---:|---:|---:|---:|
| 4 | 8 | 16 | 0 |
| 5 | 16 | 62 | 0 |
| 6 | 32 | 324 | 0 |
| 7 | 64 | 1,162 | 0 |
| 8 | 128 | 3,596 | 0 |
| 9 | 256 | 13,380 | 0 |
| 10 | 512 | 79,802 | 0 |
| 11 | 1,024 | 307,646 | 0 |
| 12 | 2,048 | 1,186,060 | 0 |
| **Total** | **4,088** | **1,592,048** | **0** |

The largest tested \(n\) is \(4096\cdot4095=16{,}773{,}120\). These finite computations, together with the proved reduction (8.7), exclude **all** \(n\) having \(\nu_2(n)\le12\), including arbitrarily large such \(n\): those larger than the bound in (8.7) are already excluded analytically. The resulting computer-assisted conclusion is

\[
\boxed{\text{Any counterexample at }i=3\text{ must satisfy }8192\mid n.}
\tag{8.9}
\]

This is a finite exhaustive computation with an explicit mathematical reduction, not proof-assistant verification. The cases with \(u\ge13\) remain unbounded, and neither (8.4) nor this finite sieve proves they are all impossible.

## 9. A density bound for each fixed index

There is also a general consequence of (4.1). Fix \(i\ge3\), and set

\[
d=\frac{\lfloor i/2\rfloor}{2},\qquad
r=\pi(i-1),\qquad \delta=d/r.
\]

Let \(E_i(X)\) count integers \(n\le X\) for which at least one \(j\) violates #699 at this particular \(i\). Then

\[
E_i(X)=
\begin{cases}
O_i(X^{1-\delta}),&0<\delta<1,\\
O_i(\log X),&\delta=1,\\
O_i(1),&\delta>1.
\end{cases}
\tag{9.1}
\]

In particular, for every fixed \(i\), the assertion holds for every permitted \(j\) for a set of \(n\) of natural density 1.

To prove this, (4.1) and \(n\ge2i\) give the uniform bound

\[
D\ge c_i n^d,\qquad
c_i=\frac{2^{s-i}}{L_i}(4/m)^{m/2}>0.
\tag{9.2}
\]

If all prime divisors of \(D\) are smaller than \(i\), then
\(D\le\prod_{p<i}p^{\nu_p\binom ni}\).
Consequently, for at least one of the \(r\) primes \(p<i\),

\[
p^{\nu_p\binom ni}\ge c_i^{1/r}n^\delta.
\tag{9.3}
\]

For this \(p\), let
\(V=\max_{0\le h<i}\nu_p(n-h)\).
Legendre's formula expresses \(\nu_p\binom ni\) as a sum of terms

\[
\#\{0\le h<i:p^k\mid n-h\}-\lfloor i/p^k\rfloor.
\]

Each term is 0 or 1, since it counts multiples in a block of \(i\) consecutive integers. Terms for \(k>V\) vanish: there are no such multiples, and necessarily \(p^k>i\), since a block of length at least \(p^k\) would contain one. Thus
\(\nu_p\binom ni\le V\).
There is therefore some \(h<i\) such that

\[
p^{\nu_p(n-h)}\ge c_i^{1/r}n^\delta.
\tag{9.4}
\]

Now restrict to \(N\le n<2N\), with \(N\) sufficiently large that \(T=c_i^{1/r}N^\delta>1\). For each prime \(p<i\), choose the single prime power
\(q_p=p^{\lceil\log_p T\rceil}\).
Equation (9.4) forces \(n\equiv h\pmod{q_p}\) for some \(p<i\) and \(0\le h<i\). For each of these \(ir\) possibilities there are at most \(N/q_p+1\le N/T+1\) integers in the interval. Hence

\[
\#\{N\le n<2N:\ n\text{ admits a counterexample at }i\}
\le ir\bigl(c_i^{-1/r}N^{1-\delta}+1\bigr).
\tag{9.5}
\]

Summing over dyadic intervals proves the first two cases of (9.1). If \(\delta>1\), the bound \(D\le n^r\) from (5.3) contradicts \(D\ge c_i n^d\) for all sufficiently large \(n\); this proves the third case. All implied constants may depend on the fixed \(i\); no uniform claim as \(i\) varies is being made.

## 10. Verification and novelty limits

The file `erdos699_verify.py` uses only Python's standard library. It verifies, with exact integer and rational arithmetic, the orbit divisibility, the normalized determinant formula, determinant nonvanishing, divisibility by \(a^t\), and both lower bounds for 2,898 selected triples. The triples comprise all admissible \(i\ge2\) for \(6\le n\le44\), plus 28 reproducibly selected larger triples, up to \(n=10{,}000\), \(i=30\). It also checks the explicit numerical margins by certified rational logarithmic bounds.

These computations are consistency checks. The universal claims depend on the algebraic proofs above and the four cited analytic inputs. No proof-assistant verification or independent mathematical review has occurred. The literature search performed here is insufficient to establish that the determinant argument or its consequence is new.

The updated script additionally checks the \(i=3\) residue implication against 14,884 directly computed binomial pairs with \(8\le n\le250\), including 49,292 witnessed odd common-prime divisibilities. It runs the exhaustive sieve in §8.6 using integers only, with no external dependencies. The sieve certifies precisely the finite range listed there, in combination with the analytic reduction; it is not evidence of exhaustion for \(u\ge13\).

The remaining task has not been closed: \(i=3\) with \(u\ge13\) still has infinitely many possible \(n\), and the other indices \(4\le i<3{,}000{,}000\) have not all been settled. The density conclusions in §§8–9 do not exclude a sparse nonempty set of counterexamples.


## 11. Strengthened determinant bound and provisional reduction to indices at least 331

This section records a continuation obtained on 2026-09-11. It strengthens §4 by retaining the factorial product that was previously bounded termwise by powers of \(m\).

### 11.1. Keeping the factorial product

Put

\[
G_m:=\prod_{k=0}^{m}k!.
\]

Recall from (3.2) that, with \(t=m+1\),

\[
T=\prod_{k=0}^{m}
 k!\,(j)_{\underline{k}}(n-j)_{\underline{k}}
 (n-i+1)_{\overline{k}}
\]

when \(i=2m\), and in the odd case \(i=2m+1\) there is one additional factor \((j)_{\underline{m+1}}\). Keeping \(G_m\) intact while using

\[
(j)_{\underline{k}}(n-j)_{\underline{k}}\le \left(\frac{n^2}{4}\right)^k,
\qquad
(n-i+1)_{\overline{k}}\le n^k,
\]

and, in the odd case, \((j)_{\underline{m+1}}\le(n/2)^{m+1}\), gives

\[
T^{1/t}
\le
G_m^{1/(m+1)}
\left(\frac{n^3}{4}\right)^{m/2}
\left(\frac n2\right)^s.
\]

Substituting into the exact determinant lower bound (3.3) yields

\[
\boxed{
D\ge
\widetilde F_i(n):=
\frac{2^{m+s}}
{L_iG_m^{1/(m+1)}}
 n^{m/2}
\left(1-\frac{i-1}{n}\right)^i.
}
\tag{11.1}
\]

Compared with the older bound (4.1),

\[
\boxed{
\frac{\widetilde F_i(n)}{F_i(n)}
=
\frac{m^{m/2}}{G_m^{1/(m+1)}}.
}
\tag{11.2}
\]

Thus the gain is exponential in \(i\). A completely elementary explicit lower bound for the gain follows from

\[
\log r
\le
\log m-\frac{m-r}{m}
\qquad(1\le r\le m),
\]

which is just \(\log x\le x-1\) applied to \(x=r/m\). Since

\[
\log G_m
=\sum_{r=1}^{m}(m-r+1)\log r,
\]

we obtain

\[
\log G_m
\le
\frac{m(m+1)}2\log m
-
\frac{(m-1)m(m+1)}{3m}.
\]

Hence

\[
\boxed{
G_m^{1/(m+1)}
\le
m^{m/2}e^{-(m-1)/3},
\qquad
\widetilde F_i(n)\ge e^{(m-1)/3}F_i(n).
}
\tag{11.3}
\]

### 11.2. Use the exact smooth upper bound, not only \(n^{\pi(i-1)}\)

Under the counterexample hypothesis, keep the first bound in (5.3):

\[
\boxed{
D\le
U_i(n):=
\prod_{p<i}p^{\lfloor\log_p n\rfloor}.
}
\tag{11.4}
\]

For fixed \(i\), \(U_i(n)\) is a step function whose jumps occur only at prime powers \(p^e\) with \(p<i\), whereas \(\widetilde F_i(n)\) is strictly increasing in \(n\). Thus the regions where the determinant estimate alone does not defeat the counterexample hypothesis are finite unions of intervals beginning at such prime-power jumps, once one has reached a range where the coarser asymptotic comparison is permanently positive.

The comparison can be made without floating point. With \(t=m+1\), the inequality \(\widetilde F_i(n)>U_i(n)\) is equivalent to the pure integer inequality

\[
\boxed{
2^{2t(m+s)}(n-i+1)^{2it}
>
L_i^{2t}G_m^2U_i(n)^{2t}
 n^{(2i-m)t}.
}
\tag{11.5}
\]

This is the intended final certificate for every determinant crossing used in the finite computation below.

### 11.3. Local prime-gap covering plus residue certificates

Suppose a remaining integer \(n\) lies in one of the determinant-danger intervals. If there is a prime

\[
n-i<p<n,
\]

then \(p>n/2\ge j>i\), so \(p\) occurs in the falling numerators of both \(\binom ni\) and \(\binom nj\), and in neither denominator. This immediately supplies the required common prime.

Only the portions of determinant-danger intervals intersecting prime gaps of length at least \(i\) therefore require further work. These exceptional \(n\) are handled by a general residue certificate. Let \(0\le r<i\), let \(p>i\) be prime, and let

\[
q=p^{\nu_p(n-r)}.
\]

Then \(p\mid\binom ni\), while the \(q\)-term in Legendre's formula implies

\[
j\bmod q>r\quad\Longrightarrow\quad p\mid\binom nj.
\]

Consequently any counterexample must satisfy, simultaneously for every such full prime-power component,

\[
\boxed{j\bmod q\le r.}
\tag{11.6}
\]

In the finite checks below, the largest modulus reduces \(i<j\le n/2\) to a small explicit list, and all remaining conditions (11.6) are then tested with exact integer arithmetic. The strict condition \(p>i\) is used throughout; this avoids any cancellation issue from a prime equal to \(i\).

### 11.4. Current finite computation

A deterministic odd-only segmented sieve was used only on the union of determinant-danger ranges; it was not used to scan all integers from 1 to the final cutoff. Prime gaps meeting the relevant threshold were extracted, and only the finitely many \(n\) at the upper ends of those gaps for which \((n-i,n)\) contains no prime were passed to the exact residue test (11.6).

The continuation has so far checked every index

\[
\boxed{i\ge304}
\]

by this combined method. Some intermediate milestones of the contiguous boundary were

\[
3{,}000{,}000\to3000\to391\to385\to384\to366\to360\to356
\to344\to338\to334\to332\to331\to330\to328\to326\to324
\to322\to320\to318\to316\to314\to312\to310\to308\to306\to304.
\]

Representative finite checks include:

- for \(i=390\), the last local danger interval had maximum prime gap 330;
- for \(i=385\), the only obstruction to the short-prime argument came from the record gap \(22367084959\to22367085353\) of length 394; the resulting ten exceptional \(n\) had no surviving \(j\) under (11.6);
- for \(i=384\), only the gaps of lengths 384 and 394 contributed, producing twelve exceptional \(n\), again with no survivor;
- for \(i=363,362\), the relevant gaps were 376, 366, 372, and 384; the exact residue intersections were empty;
- for \(i=361,360\), the finite exceptional sets had 148 and 157 integers \(n\), respectively, and no residue survivor;
- for \(344\le i\le355\), a shared deterministic scan found only 25 prime gaps of length at least 344 in the union of relevant ranges; all resulting residue systems were empty;
- for \(i=333,332\), the exceptional sets had 582 and 631 integers \(n\), respectively, with no residue survivor;
- for \(i=331\), 184 exceptional integers \(n\) were reduced by the largest modulus to at most 88 candidate values of \(j\) per \(n\), and all were eliminated by the remaining exact residue conditions.

**Certification status.** The segmented sieve and the residue checks were deterministic integer computations. The algebraic bound (11.1) and the exact comparator (11.5) are rigorous. However, the present run located the determinant-danger interval endpoints by high-precision logarithmic comparison before performing the deterministic prime-gap and residue stages. Before promoting the provisional boundary \(i\ge304\) to a theorem in a paper, every such endpoint must be replayed using (11.5), preferably with a machine-readable certificate. Until that replay is complete, the original theorem \(i\ge3{,}000{,}000\) in §6 remains the fully documented theorem in this note, while \(i\ge304\) is a strongly checked provisional improvement.


### 11.5. Continuation from 331 down to 304

The same determinant-danger / local-prime-gap / residue-certificate pipeline was continued below 331. For even indices, the danger region was rescanned at the new even gap threshold; for the following odd index, the even-gap data were reused and only newly exposed danger pieces were scanned. This is valid because all prime gaps beyond the initial small range are even, so the threshold for an odd index \(2h-1\) is effectively the same as for \(2h\).

The residue stage was also reimplemented in C++ using interval trial-sieve factorization. Because only primes \(p>i\) are used, any such prime can divide at most one member of the block

\[
n,n-1,\ldots,n-i+1.
\]

This permits all full prime-power components relevant to (11.6) to be generated simultaneously for one exceptional \(n\), instead of factoring each \(n-r\) independently. The resulting residue checks are exact integer computations.

The following contiguous indices were eliminated in this continuation:

\[
330,329,328,327,326,325,324,323,322,321,320,319,318,317,
316,315,314,313,312,311,310,309,308,307,306,305,304.
\]

Representative counts from the deterministic runs were:

- \(i=330\): 23 relevant long prime gaps, 215 exceptional integers \(n\), no residue survivor;
- \(i=329\): 336 exceptional integers, no survivor;
- \(i=328\): 36 relevant gaps, 432 exceptional integers, no survivor;
- \(i=327\): 936 exceptional integers, no survivor;
- \(i=326\): 64 relevant gaps, 1,100 exceptional integers, no survivor;
- \(i=325\): 1,692 exceptional integers, no survivor;
- \(i=324\): 93 relevant gaps, 1,791 exceptional integers, no survivor;
- \(i=323\): 2,720 exceptional integers, no survivor;
- \(i=322\): 147 relevant gaps, 2,887 exceptional integers, no survivor;
- \(i=321\): 5,274 exceptional integers, no survivor; the C++ residue stage handled this set in well under one second on the working machine;
- \(i=320\): 284 relevant gaps, 5,716 exceptional integers, no survivor;
- \(i=319\): 9,204 exceptional integers, no survivor;
- \(i=318\): 485 relevant gaps, 9,945 exceptional integers, no survivor;
- \(i=317\): 5,722 exceptional integers, no survivor;
- \(i=316\): 311 relevant gaps, 6,319 exceptional integers, no survivor;
- \(i=315\): 8,740 exceptional integers, no survivor;
- \(i=314\): 444 relevant gaps, 9,500 exceptional integers, no survivor;
- \(i=313\): 4,558 exceptional integers, no survivor;
- \(i=312\): 246 relevant gaps, 5,020 exceptional integers, no survivor;
- \(i=311\): 2,662 exceptional integers, no survivor;
- \(i=310\): 135 relevant gaps, 2,827 exceptional integers, no survivor;
- \(i=309\): 3,190 exceptional integers, no survivor;
- \(i=308\): 163 relevant gaps, 3,541 exceptional integers, no survivor;
- \(i=307\): 2,194 exceptional integers, no survivor;
- \(i=306\): 124 relevant gaps, 2,368 exceptional integers, no survivor;
- \(i=305\): 2,954 exceptional integers, no survivor;
- \(i=304\): 165 relevant gaps, 3,239 exceptional integers, no survivor.

Thus the presently checked contiguous boundary is

\[
\boxed{i\ge304.}
\]

As in §11.4, this boundary is still labelled **provisional** until every endpoint of every determinant-danger interval used in these scans is regenerated and certified directly by the integer inequality (11.5). The local prime-gap sieves and all residue intersections in this continuation were deterministic integer computations; the remaining certification issue is the danger-interval endpoint generation, not the residue stage.


## References

- P. Erdős and G. Szekeres, *Some number theoretic problems on binomial coefficients*, Australian Mathematical Society Gazette 5 (1978), 97–99. [Original paper](https://users.renyi.hu/~p_erdos/1978-46.pdf).
- G. M. Bergman, *On common divisors of multinomial coefficients*. [arXiv:0806.0607](https://arxiv.org/abs/0806.0607), especially §2.
- P. Dusart, *Estimates of Some Functions Over Primes without R.H.* (2010). [arXiv:1002.0442](https://arxiv.org/abs/1002.0442), Propositions 3.2 and 5.1, Theorem 6.9, and the beginning of §6.1.3.
- L. Schoenfeld, *Sharper bounds for the Chebyshev functions θ(x) and ψ(x). II*, Mathematics of Computation 30 (1976), 337–360. The short prime-interval result used above is also stated in Dusart §6.1.3.


## 12. Delta-compression, quadratic orbit identities, and a j-sensitive determinant bound

This section records additional deductions obtained in a parallel continuation and checked against the notation of this note.

### 12.1. Compressing all large-prime residue conditions into the central deviation

Put
\[
\Delta=n-2j,
\qquad
R_h=\prod_{\substack{p>i\\p\mid n-h}}p^{v_p(n-h)}
\qquad(0\le h<i).
\]
For a full prime power \(q=p^{v_p(n-h)}\) with \(p>i\), the residue certificate (11.6) gives \(j\bmod q=\ell\le h\). Hence
\[
q\mid (n-h)-2(j-\ell)=\Delta-h+2\ell.
\]
Distinct full prime powers are pairwise coprime, so
\[
\boxed{
R_h\mid P_h(\Delta):=\prod_{\ell=0}^{h}(\Delta-h+2\ell).
}
\tag{12.1}
\]
If \(n-h\) is odd and no factor on the right vanishes, then every prime \(p>i\) dividing \(n-h\) satisfies
\[
p\le \Delta+h.
\tag{12.2}
\]
Thus small central deviation forces strong smoothness of the block \(n,n-1,\ldots,n-i+1\).

For central choices \(j=\lfloor n/2\rfloor\), this can be combined with theorems on the greatest prime factor of products in arithmetic progression. In particular, results of Laishram--Shorey and subsequent sharpenings for odd step-2 progressions show that many central cases are excluded uniformly. For the special case \(i=3\), however, §13 below gives a stronger elementary treatment that does not require this external input.

### 12.2. Closed quadratic orbit combinations

For every \(r\ge1\) and \(s+2r\le i\), define
\[
\mathcal Q_{s,r}
=\sum_{h<r}(-1)^{r-h}\binom{2r}{h}
Y_{s+h}Y_{s+2r-h}
+\frac12\binom{2r}{r}Y_{s+r}^{2}.
\]
Exact symbolic and integer checks agree with the factorization
\[
\boxed{
\mathcal Q_{s,r}
=
\left(\frac{L_i}{i!}\right)^2
\frac{(2r-1)!}{(r-1)!}
(j)_{\underline{i-s-2r}}^2
(n-j)_{\underline s}^2
(n-j-s)_{\underline r}
(j-i+s+r+1)_{\overline r}
(n-i+1)_{\overline r}.
}
\tag{12.3}
\]
The hypergeometric reduction is a terminating Dixon \({}_3F_2(1)\) identity. Since \(A/D\mid Y_h\) for every \(h\), one always has
\[
(A/D)^2\mid \mathcal Q_{s,r}.
\tag{12.4}
\]
For \(r=2,s=0\), the left-hand side is exactly
\[
Y_0Y_4-4Y_1Y_3+3Y_2^2,
\]
which closes the direction explicitly suggested but left open in Bergman's discussion of linear combinations of \(Q_0Q_4,Q_1Q_3,Q_2^2\).

### 12.3. A j-sensitive determinant lower bound

Keeping the exact \(j\)-dependence in the determinant estimate, rather than replacing \(j(n-j)\) immediately by \(n^2/4\), gives
\[
\boxed{
D\ge
\frac{(n-i+1)^i}
{L_iG_m^{1/(m+1)}[n j(n-j)]^{m/2}j^s},
\qquad i=2m+s.
}
\tag{12.5}
\]
This dominates the uniform estimate when \(j\ll n\), so it is a natural auxiliary certificate near the edge of the admissible interval.


## 13. Further attack on the case i=3

Throughout this section assume a counterexample at \(i=3\). By §8, \(4\mid n\), \(4\le j\le n/2\), and \(D\) is a power of two.

### 13.1. The p=3 enhancement of delta-compression

For \(i=3\), the prime \(3\) can be included in (12.1) whenever its full power in one of \(n,n-1,n-2\) has exponent at least two. Indeed, if \(3^e\mid n-h\) with \(e\ge2\), then one factor of 3 is cancelled by \(3!\) but at least one remains in \(\binom n3\); absence of a common factor 3 therefore forces the same residue inequality \(j\bmod 3^e\le h\).

Write \(n=2N\) and \(\Delta=2d\). Define
\[
e_1=
\begin{cases}
3,&v_3(2N-1)=1,\\
1,&\text{otherwise},
\end{cases}
\qquad
 e_2=
\begin{cases}
3,&v_3(N-1)=1,\\
1,&\text{otherwise}.
\end{cases}
\]
Then every counterexample satisfies
\[
\boxed{
\frac{2N-1}{e_1}\mid (2d-1)(2d+1),
\qquad
\frac{N-1}{e_2}\mid d(d-1)(d+1).
}
\tag{13.1}
\]
This is the central-deviation form of the earlier \(d_1,d_2\) descent.

A first immediate consequence is that the exact central case is impossible. If \(d=0\), then the first divisibility in (13.1) gives
\[
(2N-1)/e_1\mid -1.
\]
For \(n\ge8\) this is impossible. Thus
\[
\boxed{\Delta>0\text{ in every }i=3\text{ counterexample}.}
\tag{13.2}
\]
This eliminates the central family directly, including the classical numbers \(n=3^{2a+1}+1\), without invoking an arithmetic-progression theorem.

Also, since \(e_1\le3\), (13.1) gives the elementary size restriction
\[
\boxed{n-1\le3(\Delta^2-1).}
\tag{13.3}
\]

### 13.2. Simultaneous use of the two adjacent 2x2 minors

For \(i=3\), put \(a=A/D\). Because \(D\) contains the full 2-adic part of \(A\), the integer \(a\) is odd. Besides the minor used in §8.1, one may also use the adjacent minor and the cross minor:
\[
\begin{aligned}
Y_0Y_2-Y_1^2
&=-\frac{j^2(j-1)(n-j)(n-2)}4,\\
Y_0Y_3-Y_1Y_2
&=\frac{j(j-1)(n-j)(n-j-1)(n-2)}2,\\
Y_1Y_3-Y_2^2
&=-\frac{j(n-j)^2(n-j-1)(n-2)}4.
\end{aligned}
\tag{13.4}
\]
Since \(a^2\) divides all three minors, and \(a\) is odd, it divides the gcd of the three cleared numerators. Writing \(y=n-j\), the remaining gcd is
\[
\gcd(j(j-1),(j-1)(y-1),y(y-1))
\]
and factors exactly as
\[
\gcd(j,y-1)\,\gcd(j-1,y)\,\gcd(j-1,y-1).
\]
The three factors are pairwise coprime; the first two have product dividing \(n-1\), and the last divides \(\Delta=n-2j\). Consequently
\[
\boxed{
 a^2\le j(n-j)(n-2)(n-1)\Delta.
}
\tag{13.5}
\]
Equivalently, for every noncentral candidate,
\[
\boxed{
D^2\ge
\frac{n^2(n-1)(n-2)}{36j(n-j)\Delta}
=
\frac{n^2(n-1)(n-2)}{9(n^2-\Delta^2)\Delta}.
}
\tag{13.6}
\]
This is a new \(\Delta\)-sensitive lower bound obtained by intersecting several quadratic orbit certificates rather than using a single determinant minor.

### 13.3. A four-stage integer descent in the main e1=e2=1 branch

Use the normalization from the earlier descent: write
\[
n=2BR,\qquad j=kR,\qquad 0<k<B,
\]
where the odd factor \(R\) is chosen so that the full odd part of \(n\) relevant to the counterexample has been divided from \(j\). Consider the main branch
\[
e_1=e_2=1.
\]
Set
\[
d_1=2BR-1,\qquad d_2=BR-1,
\]
and define the two known quotient integers
\[
L=\frac{k(2B-k)}{d_1},
\qquad
H=\frac{L(B-k)}{d_2}.
\tag{13.7}
\]
Because \(Rk=j\ge4\),
\[
0<H<L<k,
\qquad
k>RL,
\qquad
L>RH.
\tag{13.8}
\]
Define
\[
q:=k-RL,
\qquad
y:=L-RH.
\]
Then \(q,y\) are positive integers and direct elimination of \(d_1,d_2\) gives
\[
\boxed{2Bq=k^2-L,}
\qquad
\boxed{By=kL-H.}
\tag{13.9}
\]
Moreover
\[
L^2-kH=B(ky-2qL)>0.
\]
The quantity in parentheses simplifies further:
\[
ky-2qL=\frac{Ly}{2B-k}.
\]
Thus
\[
\boxed{
w:=\frac{Ly}{2B-k}=ky-2qL
}
\tag{13.10}
\]
is a positive integer. Since \(L<k<B<2B-k\),
\[
\boxed{0<w<y<L<k.}
\tag{13.11}
\]
In fact
\[
\frac{w}{y}=\frac{L}{2B-k}=\frac{k}{2BR-1}<\frac1R,
\]
so
\[
\boxed{y>Rw.}
\tag{13.12}
\]
Thus the previous three-stage descent \(k>L>H\) extends to a new four-stage pure-integer descent \(k>L>y>w\), with a multiplicative shrink by at least \(R\) at the last step.

There is also a canonical global quotient
\[
\boxed{
s:=\frac{k(Rk-1)(Rk-2)}{(2BR-1)(BR-1)}\in\mathbb Z_{>0},
}
\tag{13.13}
\]
which is the quotient obtained after combining the \(h=0,1,2\) residue moduli. It satisfies
\[
\boxed{Bs=kq-y,}
\tag{13.14}
\]
and hence
\[
0<s<q<k.
\tag{13.15}
\]
These identities give two intertwined descent chains, one arising from successive residue quotients and one from quadratic minors. A complete proof for \(i=3\) would follow if one can show that the pair \((y,w)\), or equivalently the factorized variables behind (13.10), satisfies a closed recurrence of the same type and hence can be iterated indefinitely.

### 13.4. SL(2,Z)-type factorization behind the descent

Factor the full prime powers of \(d_1\) according to which factor they divide:
\[
d_1=cf,
\qquad
k=c\alpha,
\qquad
2B-k=f\beta,
\qquad
L=\alpha\beta.
\]
Likewise factor \(d_2=gh\) with \(g\mid L\) and \(h\mid B-k\), then split \(g=g_1g_2\), \(\alpha=g_1a\), \(\beta=g_2b\), and write \(B-k=hz\). Define
\[
m=\frac{c-R\beta}{h},
\qquad
n=\frac{f-R\alpha}{h}.
\]
The earlier factorization identities become
\[
\boxed{n\beta=m\alpha+2z,}
\tag{13.16}
\]
\[
\boxed{h^2mn=R^2L-1,}
\tag{13.17}
\]
and, with \(C=(m\alpha+n\beta)/2\),
\[
\boxed{B=RL+hC,\qquad g=RC+hmn.}
\tag{13.18}
\]
In particular
\[
(R\alpha)(R\beta)-(hm)(hn)=1.
\tag{13.19}
\]
Thus
\[
\begin{pmatrix}R\alpha&hm\\hn&R\beta\end{pmatrix}\in SL_2(\mathbb Z)
\]
with all entries positive. This exposes an Euclidean/continued-fraction structure behind the descent. Also
\[
C^2-Lmn=z^2,
\tag{13.20}
\]
so the symmetric matrix
\[
\begin{pmatrix}L&C\\C&mn\end{pmatrix}
\]
has determinant \(-z^2\). The remaining task is to turn this positive \(SL_2(\mathbb Z)\) structure into a genuinely self-similar descent that preserves the counterexample conditions.

### 13.5. Unified treatment of the 3-adic exception and a cube-root thinning

The two divisibility branches in §8.2 and the descent variables of §13.3 can be written in a single normalization. Write

\[
a=2^u,
\qquad
\varepsilon=
\begin{cases}
1,&\nu_3(M)=1,\\
0,&\text{otherwise},
\end{cases}
\qquad
T=\frac{M}{3^\varepsilon},
\qquad
C=3^\varepsilon a.
\]

Then
\[
n=CT,\qquad j=kT,\qquad 1\le k\le C/2.
\]
Put
\[
N_1=CT-1,\qquad N_2=\frac{CT}{2}-1,
\]
and remove the single exceptional factor 3 exactly when it occurs to the first power:
\[
Q_r=\frac{N_r}{\delta_r},\qquad \delta_r\in\{1,3\}.
\]
Thus \(\delta_r=3\) precisely when \(\nu_3(N_r)=1\), and otherwise \(\delta_r=1\). Since \(N_1=2N_2+1\), one has
\[
\gcd(Q_1,Q_2)=1.
\]
Moreover, if \(\varepsilon=1\), then \(C\equiv0\pmod3\), so both \(N_1,N_2\equiv-1\pmod3\) and hence
\[
\delta_1=\delta_2=1.
\]
If \(\varepsilon=0\), at most one of \(\delta_1,\delta_2\) can equal 3. In particular,
\[
\delta_1\delta_2C\le 3a.
\tag{13.21}
\]

For every full odd prime-power component of \(Q_1\), the residue condition gives \(j\bmod q\in\{0,1\}\). Using \(CT\equiv1\pmod q\) and \(j=kT\), one obtains
\[
\boxed{Q_1\mid k(C-k).}
\tag{13.22}
\]
Similarly, the full prime-power components of \(Q_2\) give
\[
\boxed{Q_2\mid k\left(\frac C2-k\right)(C-k).}
\tag{13.23}
\]
Because the prime factors of \(Q_1Q_2\) are coprime to \(C\), while the pairwise gcds of
\[
k,\qquad \frac C2-k,\qquad C-k
\]
have no prime factor outside those of \(C\), the two divisibilities combine without overlap:
\[
\boxed{
Q_1Q_2\mid k(C-k)\left(\frac C2-k\right).
}
\tag{13.24}
\]
The central case \(k=C/2\) is already excluded by §13.1, so \(0<k<C/2\). Therefore, with \(x=k/C\),
\[
k(C-k)(C/2-k)=C^3x(1-x)(1/2-x)
\]
and
\[
\max_{0<x<1/2}x(1-x)(1/2-x)=\frac{\sqrt3}{36}.
\]
Consequently
\[
\frac{(CT-1)(CT/2-1)}{\delta_1\delta_2}
\le \frac{\sqrt3}{36}C^3,
\]
so, using (13.21),
\[
\boxed{
T^2-\frac{3T}{C}+\frac{2}{C^2}
\le \frac{\sqrt3}{6}\,2^u.
}
\tag{13.25}
\]
In particular
\[
\boxed{
T^2<\frac{\sqrt3}{6}\,2^u+3.
}
\tag{13.26}
\]
For \(u\ge13\), this gives the explicit square-root thinning
\[
T<0.537626\,2^{u/2}.
\tag{13.27}
\]
Thus the number of possible \(n\le X\) in the \(i=3\) counterexample set satisfies the improved coarse estimate
\[
E_3(X)=O(X^{1/3}).
\tag{13.28}
\]

The same normalization also unifies the quotient descent. Define
\[
L:=\frac{\delta_1k(C-k)}{CT-1}\in\mathbb Z_{>0},
\qquad
H:=\frac{\delta_2L(C/2-k)}{CT/2-1}\in\mathbb Z_{>0}.
\tag{13.29}
\]
Then
\[
L<\frac{\delta_1k}{T},
\qquad
H<\frac{\delta_1\delta_2k}{T^2}\le\frac{3k}{T^2}.
\tag{13.30}
\]
For \(T\ge5\) this gives \(k>L>H>0\). Writing \(b=C/2\), direct reduction of the defining equations gives
\[
\boxed{L\equiv\delta_1k^2\pmod b,\qquad
H\equiv\delta_1\delta_2k^3\pmod b.}
\tag{13.31}
\]
Moreover the whole system combines into the exact identity
\[
\boxed{
\delta_1\delta_2\,k(C-k)(C/2-k)
=H(CT-1)(CT/2-1).
}
\tag{13.32}
\]

These congruences give a uniform 2-adic descent. Let \(v=v_2(k)\). In the branch \(T\ge5\), the bounds in (13.30), together with the fact that \(\delta_1,\delta_2,T\) are odd, imply \(0<L,H<2^{u-1}\). Reducing (13.31) modulo \(2^{u-1}\) therefore yields
\[
\boxed{
\nu_2(L)=2v,\qquad \nu_2(H)=3v,\qquad 3v<u-1.
}
\tag{13.33}
\]
Equivalently, if \(k=2^v k_0\) with \(k_0\) odd, then the size bound for \(H\) gives
\[
\boxed{
2^{2v}T^2<\delta_1\delta_2\,k_0\le 3k_0.
}
\tag{13.34}
\]

Finally, combining this unified notation with the factorization mechanism of §13.4 gives a stronger cubic thinning. Since \(Q_1\mid k(C-k)\), split the full prime powers of \(Q_1\) between the two coprime factors and write
\[
Q_1=cf,\qquad k=c\alpha,\qquad C-k=f\beta,\qquad L=\alpha\beta.
\]
Likewise, from \(Q_2\mid L(C/2-k)\), split
\[
Q_2=gh,\qquad g\mid L,\qquad h\mid(C/2-k).
\]
Because \(\gcd(Q_1,Q_2)=1\), the same calculation as in §13.4 gives positive integers \(m,n\) satisfying
\[
h^2mn=T^2L-\delta_1.
\]
As \(g\mid L\), this implies the square divisibility
\[
\boxed{
Q_2^2\mid L^2(T^2L-\delta_1).
}
\tag{13.35}
\]
Hence
\[
Q_2^2<T^2L^3.
\]
Now
\[
Q_2=\frac{CT/2-1}{\delta_2}>\frac{CT}{4\delta_2},
\qquad
L<\frac{\delta_1(C/2)}{T},
\]
and therefore
\[
\frac{C^2T^2}{16\delta_2^2}
< T^2\left(\frac{\delta_1C}{2T}\right)^3.
\]
After cancellation,
\[
\boxed{
T^3<2\delta_1^3\delta_2^2C.
}
\tag{13.36}
\]
Thus, if \(\varepsilon=0\), then \(C=2^u\) and at most one of \(\delta_1,\delta_2\) equals 3, so
\[
\boxed{M^3<54\,2^u.}
\tag{13.37}
\]
If \(\varepsilon=1\), then \(C=3\cdot2^u\), \(\delta_1=\delta_2=1\), and \(M=3T\), so
\[
\boxed{M^3<162\,2^u.}
\tag{13.38}
\]
Uniformly,
\[
\boxed{
M<\sqrt[3]{162}\,2^{u/3}<5.452\,2^{u/3}.
}
\tag{13.39}
\]
This asymptotically improves the square-root thinning (13.27); for explicit finite work one should retain the minimum of (13.27) and the cubic bounds (13.37)--(13.39). Counting dyadically from the cubic bound gives
\[
\boxed{E_3(X)=O(X^{1/4}).}
\tag{13.40}
\]
Thus the known necessary set for an \(i=3\) counterexample is substantially thinner than the original \(O(\sqrt X)\) estimate from §8.5.

### 13.6. Additional Kummer constraints from prime divisors of the normalized odd part

The divisibility \(T\mid j\) (after removal of the single cancelled factor 3 when \(\nu_3(M)=1\)) is not the end of the information coming from primes dividing \(n\). Let \(p^e\Vert T\), and write
\[
S=T/p^e.
\]
Then \(p^e\) divides both \(n=CT\) and \(j=kT\). Legendre's formula, or equivalently the digit-sum formula for factorial valuations, gives the exact scaling identity
\[
\boxed{
\nu_p\binom{CT}{kT}
=
\nu_p\binom{CS}{kS}.
}
\tag{13.41}
\]
Indeed multiplication of both upper and lower arguments by \(p^e\) appends \(e\) zero base-\(p\) digits and does not change the number of carries.

For every prime \(p\mid T\) which survives in \(\binom n3\), a counterexample therefore requires
\[
\boxed{
p\nmid\binom{CS}{kS}.}
\tag{13.42}
\]
When \(p=3\), this applies whenever the 3-adic exponent of \(n\) is at least two; the branch \(\nu_3(M)=1\) was precisely normalized so that the single cancelled factor 3 is absent from \(T\).

By Kummer's theorem, (13.42) is equivalent to the absence of carries when adding \(kS\) and \((C-k)S\) in base \(p\). Equivalently, for every \(r\ge1\),
\[
\boxed{
(kS\bmod p^r)\le(CS\bmod p^r).
}
\tag{13.43}
\]
Thus every prime divisor of \(T\) contributes an additional tower of residue inequalities after the first normalization \(T\mid j\). These conditions are independent of the adjacent-number certificates (13.22)--(13.23) and can be intersected with them.

As a consistency check on the strength of this extra condition, in the earlier \(C=8192\) first-stage survivors
\[
(T,k)=(19,3437),\qquad (23,4005),
\]
one finds exactly
\[
\nu_{19}\binom{8192}{3437}=2,
\qquad
\nu_{23}\binom{8192}{4005}=1,
\]
so both are already eliminated by (13.42), before using the second adjacent modulus \(Q_2\). This is only an illustrative finite check; the universal content is the exact identity (13.41) and the necessary no-carry system (13.43).

### 13.7. Further unified descent: quotient remainders, a central-distance bound, and a sharper cubic constant

Continue with the unified notation of §§13.5--13.6. Define
\[
q:=\delta_1 k-TL,
\qquad
y:=\delta_2 L-TH.
\]
Using (13.29) directly gives
\[
\boxed{
q(CT-1)=\delta_1 k(Tk-1),
}
\tag{13.44}
\]
and
\[
\boxed{
y(CT/2-1)=\delta_2 L(Tk-1).
}
\tag{13.45}
\]
In particular \(q,y\in\mathbb Z_{>0}\) because \(Tk=j\ge4\), and
\[
\boxed{
TL+q=\delta_1k,
\qquad
TH+y=\delta_2L.
}
\tag{13.46}
\]
Thus the first two quotient steps are genuine Euclidean-type decompositions with the same scaling factor \(T\); after one step the complementary factor \(C-k\) has been replaced by the common smaller factor \(Tk-1\). This formulation includes the one-factor-of-3 exceptional branches without changing the recurrence shape.

There is also a useful lower bound on the portion of \(Q_2\) allocated to the central displacement. As in §13.5, write
\[
Q_1=cf,
\quad k=c\alpha,
\quad C-k=f\beta,
\quad L=\alpha\beta,
\]
and
\[
Q_2=gh,
\qquad g\mid L,
\qquad h\mid d:=C/2-k.
\]
Define the positive integers
\[
m=\frac{\delta_1c-T\beta}{h},
\qquad
n'=\frac{\delta_1f-T\alpha}{h}.
\]
(The symbol \(n'\) is used here to avoid conflict with the original upper binomial parameter.) Then
\[
\boxed{h^2mn'=T^2L-\delta_1.}
\tag{13.47}
\]
If
\[
W:=\frac{m\alpha+n'\beta}{2},
\]
then direct elimination gives
\[
\delta_1\frac C2=TL+hW,
\qquad
\boxed{\delta_1\delta_2 g=TW+hmn'.}
\tag{13.48}
\]
Since \(g\mid L\), hence \(g\le L\), and
\[
W\ge\sqrt{mn'L}
\]
by AM--GM. Combining this with (13.47) yields the rigorous lower bound
\[
\boxed{
h>\frac{2(T^2-\delta_1)}{\delta_1\delta_2}.}
\tag{13.49}
\]
For the main branch \(\delta_1=\delta_2=1\), this implies the integer estimate
\[
\boxed{h\ge2T^2-1.}
\tag{13.50}
\]
Since \(h\mid d=C/2-k\), the main branch therefore satisfies
\[
\boxed{
C/2-k\ge2T^2-1,
\qquad
\Delta=2T(C/2-k)\ge4T^3-2T.
}
\tag{13.51}
\]
Thus a putative counterexample with nontrivial normalized odd part must lie a distance of order at least \(T^3\) from the center.

For \(T>1\), necessarily \(T\ge5\). From (13.47), \(mn'\ge1\), and the quotient bound \(L<\delta_1C/(2T)\),
\[
h^2<T^2L<\frac{\delta_1CT}{2}.
\]
Together with (13.49) this gives
\[
\boxed{
8(T^2-\delta_1)^2
<\delta_1^3\delta_2^2CT.
}
\tag{13.52}
\]
This improves the finite constant in the cubic thinning. Indeed, for \(T\ge5\),
\[
\frac{T^3}{C}
<\frac{\delta_1^3\delta_2^2}{8}
\left(\frac{T^2}{T^2-\delta_1}\right)^2,
\]
and the last factor decreases with \(T\). Checking the finitely many possible \((\varepsilon,\delta_1,\delta_2)\) branches at \(T=5\) gives the uniform consequence
\[
\boxed{T>1\Longrightarrow M^3<11\,2^u.}
\tag{13.53}
\]
The worst branch for this coarse uniform constant is \(\varepsilon=1\), where \(C=3\cdot2^u\), \(M=3T\), and \(\delta_1=\delta_2=1\). The constant 11 is therefore a safe simple integer constant; branchwise constants are smaller.

The case \(T=1\) simplifies in a different direction. Since \(C\equiv1\pmod{Q_1}\) and \(C/2\equiv1\pmod{Q_2}\), (13.22)--(13.23) reduce to
\[
\boxed{Q_1\mid k(k-1),
\qquad
Q_2\mid k(k-1)(k-2).}
\tag{13.54}
\]
As \(\gcd(Q_1,Q_2)=1\),
\[
\boxed{Q_1Q_2\mid k(k-1)(k-2).}
\tag{13.55}
\]
This is a particularly rigid residual branch. It is not yet proved here that (13.54)--(13.55) force the inadmissible value \(k=1\) in all cases; closing that implication is one of the cleanest remaining subproblems for the \(i=3\) case.
