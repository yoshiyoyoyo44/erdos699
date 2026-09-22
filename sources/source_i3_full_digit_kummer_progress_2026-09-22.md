# Erdős 699 — i=3 担当1「全桁 Kummer 条件」進捗総まとめ

作成日: 2026-09-22

## 0. この文書の範囲

この文書は、Erdős Problem 699 の i=3、偶数 j の枝について、このチャットで進めた「全桁 Kummer 条件」「moving prime powers」「balanced support 枝」「endpoint / center 再構成」「第一・第二 Frey 曲線への bridge」をまとめた研究ノートである。

目的は完全解決の主張ではなく、

- 何が厳密に証明できたか、
- どの条件が既存稿からの入力か、
- どの途中主張が監査で修正されたか、
- balanced \((2,4)\) および \((3,3)\) の残枝がどこまで縮んだか、
- 次にどこを攻めるべきか

を一つに統合すること。

GitHub への書き込みはしていない。

---

# 1. 基本正規化と既存入力

偶数 \(j\) の反例を仮定する。

\[
n=\gamma T2^u,\qquad u\ge 51,
\]

\[
v=v_2(j)\ge1,\qquad x=2^v,\qquad G=u-4v\ge14.
\]

四分岐は

\[
(\gamma,\delta_1,\delta_2)
=(1,1,1),(1,1,3),(1,3,1),(3,1,1).
\]

六ブロック \(A,B,C,R,S,T\) は正の奇数で pairwise coprime、

\[
\gcd(T,\gamma\delta_1\delta_2)=1,
\]

かつ補助奇数 \(a,b,g_0,h_0\) を用いて

\[
n-1=\delta_1RS,
\qquad
\frac{n-2}{2}=\delta_2ABC,
\]

\[
j=TSBxg_0,
\qquad
n-j=TRCxh_0,
\]

\[
j-1=RAa,
\qquad
n-j-1=SAb.
\]

\[
P=g_0h_0.
\]

基本 determinant は

\[
\boxed{T^2x^2BCP-A^2ab=\delta_1.}
\tag{1.1}
\]

さらに

\[
\delta_1S=Aa+TCxh_0,
\qquad
\delta_1R=Ab+TBxg_0.
\]

既存の \(W_*\) は

\[
\boxed{W_*=
\frac{\delta_1\delta_2BC-Aab}{Tx^2}>0}
\tag{1.2}
\]

で、奇数。

\[
\boxed{AW_*+TBCP=\delta_1\gamma2^{u-2v-1}}
\tag{1.3}
\]

\[
\boxed{aBg_0+bCh_0=2xW_*}
\tag{1.4}
\]

および

\[
\gcd(W_*,TABC)=1,
\qquad
\gcd(W_*,P)\mid\delta_1\gamma.
\]

### 既存 repo 参照

- `research/i3/i3_digit_reciprocity_and_W_continuation.md`
- `research/i3/i3_new_chat_integration_and_effective_gap_2026-09-21.md`
- `research/i3/i3_quadratic_twist_and_kummer_support_2026-09-21.md`
- `research/i3/i3_growing_gap_and_auxiliary_frey_2026-09-21.md`
- `research/i3/i3_cross_modulus_and_digit_height_2026-09-20.md`
- `research/i3/i3_gap_square_obstructions_2026-09-21.md`

このチャットで主に照合した基準コミットは

`0d2262f3beb7c5ce0535ce4fe998832d558ad965`

付近。

---

# 2. center 方程式と二つの Frey 量

既存の中心正規化では

\[
c_0=\delta_1^2\delta_2,
\qquad
B_G=\gamma c_0 2^{G-3}.
\]

正の奇数 \(m\) と

\[
q=TPW_*
\]

に対し

\[
\boxed{m+T^2PW_*=\gamma c_0 2^{G-3}}
\tag{2.1}
\]

かつ

\[
\gcd(m,T)=1,
\qquad
\gcd(m,q)\mid\gamma c_0.
\]

第一 center 式・第二 center 式は

\[
\boxed{
\delta_2Z^2=m\gamma2^{u-1}+q
}
\tag{2.2}
\]

\[
\boxed{
\delta_1TC_{\rm cen}^2
=
\delta_1\gamma2^{G-2+2v}+(n-1)Z
}
\tag{2.3}
\]

である。

合同条件

\[
\boxed{q\equiv c_0T^2\pmod{16}},
\qquad
\boxed{m\equiv-c_0T^3\pmod{16}}
\tag{2.4}
\]

も必要。

## 第一 Frey 側

第一曲線の導手を支配する量を

\[
\mathcal Q
=
\operatorname{rad}_{\ge5}(ab)
\operatorname{rad}_{\ge5}(\operatorname{cf}_3(P))^2
\]

とする。

既存上界

\[
\boxed{
abP^2
<
\frac{\gamma\delta_1^3\delta_2^2}{16T^3}2^G
}
\tag{2.5}
\]

から

\[
\mathcal Q\le abP^2.
\]

さらに

\[
\boxed{
u\le972\mathcal Q
\left\lceil\log_2(486\mathcal Q)\right\rceil^2+124
}
\tag{2.6}
\]

が既存の一般定理入力から得られている。

## 第二 Frey 側

第二曲線の量

\[
\boxed{
R_F=
\operatorname{rad}_{\ge5}(mTPW_*)
}
\tag{2.7}
\]

に対し既存結果は

\[
\boxed{R_F>166}
\tag{2.8}
\]

および

\[
\boxed{
G<\frac92R_F
\left\lceil\log_2(6R_F)\right\rceil^2+52
}
\tag{2.9}
\]

である。

このチャットの目標の一つは、全桁 Kummer 側から同一 candidate の \(\mathcal Q\) と \(R_F\) を同時に決定・拘束することだった。

---

# 3. full-digit Kummer の六ブロック条件

各完全素数冪 \(p^e\) が各ブロックに属する場合、以下の加法が base \(p\) で全桁無繰り上がり。

### T

\[
\frac{j}{p^e}
+
\frac{n-j}{p^e}
=
\frac{n}{p^e}.
\]

### R

\[
\frac{j-1}{p^e}
+
\frac{n-j}{p^e}
=
\frac{n-1}{p^e}.
\]

### S

\[
\frac{j}{p^e}
+
\frac{n-j-1}{p^e}
=
\frac{n-1}{p^e}.
\]

### A

\[
\frac{j-1}{p^e}
+
\frac{n-j-1}{p^e}
=
\frac{n-2}{p^e}.
\]

### B

\[
\frac{j}{p^e}
+
\frac{n-j-2}{p^e}
=
\frac{n-2}{p^e}.
\]

### C

\[
\frac{j-2}{p^e}
+
\frac{n-j}{p^e}
=
\frac{n-2}{p^e}.
\]

## q-chunk 化

\(q=p^e\) とし、p進桁を e 桁ずつ束ねる。

無繰り上がりなら、各 q-chunk についても p進係数ごとの優越関係が成り立つ。

たとえば A/B/C 側で block residue を

\[
s=1,0,2
\]

とすると

\[
X=\frac{j-s}{q},
\qquad
N_q=\frac{n-2}{q}
\]

に対し、各 chunk \(k\) で

\[
\boxed{X_k\preceq_p(N_q)_k}
\tag{3.1}
\]

が必要。

これは単なる低位合同

\[
j\equiv s\pmod q
\]

より強い。

---

# 4. support 最小枝の分類

\[
Q_1=\frac{n-1}{\delta_1},
\qquad
Q_2=\frac{n-2}{2\delta_2}.
\]

## 4.1 最小 support \((2,3)\) の排除

\(T=1,\gamma=1\) で

\[
\omega(Q_1)=2,
\qquad
\omega(Q_2)=3
\]

を仮定すると、Zsigmondy 型の primitive divisor 数え上げから

\[
u=2s+1,
\qquad u,s\text{ prime}
\]

まで絞れる。

さらに

\[
D=2^s,
\]

\[
M=D-1,
\qquad
N=\frac{D+1}{3}.
\]

最終的に

\[
\omega(M)=2,
\qquad
\omega(N)=1
\]

の三配置 \(A=N,B=N,C=N\) をそれぞれ排除できる。

### A=N

中心距離 \(c=D^2-j=Nt\) から

\[
ab
=
\frac{9(D-1)^2-t^2}{2D^2-1}
<\frac92.
\]

\(ab\) は正の奇数なので \(ab=1,3\)。

すると mod16 で

\[
t^2\equiv10\text{ または }12
\]

となり不可能。

### C=N

endpoint から

\[
L=\frac{N-1}{2}=\frac{D-2}{6},
\qquad v=1.
\]

平方判別式が mod13 で \(5\) または \(7\) となり非平方。

### B=N

対称 endpoint を精密に扱うと、lift が 3 ケースに分かれ、

- 一つは同じ mod13 非平方、
- 一つは \(v=s\) となり \(G<0\)、
- 最後は mod19 / mod73 の非平方

で排除。

従って

\[
\boxed{
\omega(Q_1)=2,
\ \omega(Q_2)=3
\text{ は不可能}
}
\tag{4.1}
\]

よって少なくとも

\[
\boxed{
\omega(Q_1)\ge3
\quad\text{または}\quad
\omega(Q_2)\ge4.
}
\tag{4.2}
\]

---

# 5. \((3,3)\) odd-u 枝の完全排除

\[
u\text{ odd},
\qquad
\omega(Q_1)=\omega(Q_2)=3
\]

を仮定する。

primitive divisor 数え上げから

\[
u=2s+1,
\qquad s\text{ prime}
\]

まで縮む。

さらに \(3\mid u\) なら prime-neighbor power 排除に落ちるため不可能。

従って

\[
s\equiv5\pmod6.
\]

\[
Q_2=(D-1)(D+1)/3
\]

の support 3 から

\[
\omega(D-1)=2,
\qquad
\omega((D+1)/3)=1.
\]

したがって N-side 全体が A/B/C のどれか1ブロックになるが、前節の whole-side block 排除は \(s\equiv5\pmod6\) のみで成立する。

よって

\[
\boxed{
(\omega(Q_1),\omega(Q_2))=(3,3),
\quad u\text{ odd}
\text{ は不可能}.
}
\tag{5.1}
\]

これは以前残していた semiprime \(u=pq\) 枝も消す。

---

# 6. \((3,3)\) even-u 枝の圧縮

残る \((3,3)\) は even-u。

\[
u=2r,
\qquad r\text{ odd prime}.
\]

Q1 側の pure split \(\{R,S\}=\{M,N\}\) は偶数 j と両立しない。

したがって R/S は mixed split に強制される。

各 split につき j の lift は高々2本なので、Q1 factorization が与えられれば j 候補は全体で高々8本。

この branch は完全排除までは未完。

---

# 7. balanced \((2,4)\) 枝の構造

最も重要な残枝。

\[
\omega(Q_1)=2,
\qquad
\omega(Q_2)=4.
\]

分類を進めると

\[
\boxed{
u=2r+1,
\qquad u,r\text{ prime}.
}
\tag{7.1}
\]

\[
D=2^r,
\qquad
M=D-1,
\qquad
N=\frac{D+1}{3}.
\]

\[
M=M_1M_2,
\qquad
N=N_1N_2,
\]

各 \(M_i,N_i\) は complete prime power。

\[
Q_2=ABC=MN.
\]

---

# 8. whole-side block 排除

balanced 枝で

\[
A,B,C\notin\{M,N\}.
\]

つまり M-side 全体も N-side 全体も一ブロックにはなれない。

従って4原子

\[
M_1,M_2,N_1,N_2
\]

を A/B/C の3ブロックへ分けるとき、二成分ブロックは必ず

\[
\boxed{M_iN_j}
\tag{8.1}
\]

という mixed block。

各ブロックは M-side を高々1個、N-side を高々1個しか含まない。

---

# 9. endpoint 再構成

balanced 枝では

\[
Q=Q_2=ABC,
\qquad
Q_1=n-1.
\]

C を仮定し

\[
K=Q/C.
\]

\[
L_C=\operatorname{leastpos}(K^{-1}\bmod C).
\]

真の反例なら

\[
\boxed{L_C<\frac45C}
\tag{9.1}
\]

かつ

\[
\boxed{v=1+v_2(L_C)}
\tag{9.2}
\]

なので

\[
\boxed{G=u-4-4v_2(L_C)}.
\tag{9.3}
\]

さらに

\[
\Delta_C=1+8Q_1KL_C
\]

が平方で、平方根 \(z=2j-1\) は

\[
\boxed{z\equiv3\pmod{2C}}
\tag{9.4}
\]

を満たす必要がある。

\(z\equiv-3\) は偽 endpoint root。

j が出れば block 割当ては

\[
\boxed{A=\gcd(Q,j-1)}
\]

\[
\boxed{B=\gcd(Q,j)}
\]

\[
\boxed{C=\gcd(Q,j-2)}
\]

\[
\boxed{R=\gcd(Q_1,j-1)}
\]

\[
\boxed{S=\gcd(Q_1,j)}
\]

で一意。

したがって balanced 枝は C 候補高々8本から j 候補高々8本まで圧縮される。

---

# 10. endpoint から補助因子を完全再構成

\[
\rho=\frac{j(j-1)}{2Q_1},
\qquad
\rho_y=\frac{(n-j)(n-j-1)}{2Q_1}.
\]

\[
\rho=ABa2^{v-1}g_0,
\qquad
\rho_y=ACb2^{v-1}h_0.
\]

\[
c=\frac n2-j.
\]

\[
\boxed{\rho_y-\rho=c.}
\tag{10.1}
\]

C-side endpoint quotient

\[
L_C=a2^{v-1}g_0.
\]

B-side quotient

\[
L_B=b2^{v-1}h_0.
\]

従って

\[
\boxed{abP=\frac{L_CL_B}{2^{2v-2}}.}
\tag{10.2}
\]

また

\[
\boxed{W_*=
\frac{BL_C+CL_B}{2^{2v}}.}
\tag{10.3}
\]

よって block と endpoint が決まれば \(abP,W_*\) が決まる。

さらに

\[
\boxed{
\frac{W_*}{abP}
=
\frac14\left(\frac B{L_B}+\frac C{L_C}\right)
}
\tag{10.4}
\]

から

\[
\boxed{W_*>\frac25abP}
\tag{10.5}
\]

という粗い一様比較も得られた。

---

# 11. 監査訂正：独立でなかった平方条件

途中で

- determinant square,
- 第一 center square,
- 第二 center square

を endpoint square と独立の平方条件として数えたが、これは訂正。

完全な block candidate が出た後では多くが恒等式に還元される。

たとえば

\[
1+16\rho\rho_y
=
(2j-1-4\rho)^2.
\]

従って determinant の「平方性」は新情報ではなく、真に必要なのは quotient の整数性、奇偶性、正値性、support/gcd 条件。

center 変数も

\[
C_{\rm cen}=\frac{c}{2^v}
\]

および

\[
Z=
\frac{4c^2-n}{2^{2v+2}(n-1)}
\]

で j から再構成され、center の平方表示自体は後から恒等式になる。

したがって独立に攻めるべきものは「真の full-digit upper chunks」。

---

# 12. M-side 第2チャンク

M-side complete prime power

\[
q=p^e\mid M,
\qquad
a=M/q
\]

に対し

\[
D=aq+1.
\]

正確に

\[
\boxed{
\frac{n-2}{q}=2a^2q+4a.
}
\tag{12.1}
\]

したがって \(q>4a\) なら low q-chunk は \(4a\)。

block residue を \(s=1,0,2\) とすると

\[
\boxed{
\left(\frac{j-s}{q}\bmod q\right)
\preceq_p4a.
}
\tag{12.2}
\]

さらに \(q>2a^2\) なら q-chunk は正確に2段だけ。

---

# 13. singleton endpoint M-factor theorem

q が B または C singleton endpoint に入るとき、endpoint inverse と第2チャンクを mod \(q^2\) で結合できる。

最終的に正の奇数 h が存在し

\[
\boxed{v=v_2(a-3h)}
\tag{13.1}
\]

となる。

C-side では strong asymmetry \(q>36a\) なら

\[
0<h<a/6,
\]

B-side では \(q>39a\) なら

\[
a/6<h<a/2.
\]

特に

\[
2^v<a
\]

(C)

および

\[
2^v<a/2
\]

(B)

が得られる。

---

# 14. mixed endpoint M-factor theorem

endpoint block を

\[
E=qc
\]

とする。

q は M-side、c は N-side constituent。

endpoint 一次式は

\[
\boxed{2aL=3c+kq.}
\tag{14.1}
\]

第2 q-chunk を mod \(q^2\) で比較すると

\[
\boxed{9ct\equiv27ac+2k\pmod q.}
\tag{14.2}
\]

C-side で \(q>36ac\)、B-side で \(q>39ac\) なら合同式が整数等式へ昇格し

\[
\boxed{k=9ch}
\tag{14.3}
\]

\[
\boxed{t=3a+2h}
\tag{14.4}
\]

となる。

そして驚くべきことに c が消え

\[
\boxed{v=v_2(a-3h)}.
\tag{14.5}
\]

さらに

\[
\boxed{a\ell-3qh=1}
\tag{14.6}
\]

という Bezout 型の式まで得られる。

---

# 15. M-side 第3チャンクと二次バランス

\(q>2a^2\) なら

\[
\frac{w-2}{q}=t+sq
\]

と正確に書ける。

endpoint を mod \(q^3\) まで展開すると

\[
\boxed{
3s+a^2-15ah+4h^2\equiv0\pmod q.
}
\tag{15.1}
\]

C-endpoint では

\[
0<h<a/6,
\qquad
0\le s\le a^2.
\]

左辺の絶対値は \(<4a^2\)。

もし \(q>4a^2\) なら左辺は0になるが、mod3 で

\[
a^2+h^2\not\equiv0
\]

となり矛盾。

したがって strong-asymmetry C branch では

\[
\boxed{q<4a^2.}
\tag{15.2}
\]

B-endpoint でも同様に

\[
\boxed{q<5a^2.}
\tag{15.3}
\]

---

# 16. block-size と合わせた endpoint M-side 無条件上界

mixed endpoint \(E=qc\) 自体に cross-modulus bound をかける。

C-block では

\[
qc<2D
\]

なので

\[
\boxed{c\le2a-1.}
\tag{16.1}
\]

これと第3チャンク上界を合わせると

\[
\boxed{q\mid C\Longrightarrow q<72a^2.}
\tag{16.2}
\]

B-block は強い block bound から

\[
c<\frac54a
\]

が得られ

\[
\boxed{q\mid B\Longrightarrow q<49a^2.}
\tag{16.3}
\]

従って N-side constituent と mixed しても巨大 q は逃げられない。

---

# 17. A-block と第一 Frey の直接 bridge

ここが後半の重要成果。

第一 Frey の

\[
abP^2<\frac9{16}2^G
\]

と determinant

\[
x^2BCP-A^2ab=1
\]

を直接消去する。

\[
x^4=\frac n{2^G}
\]

を用いると \(G,P\) が消えて

\[
\boxed{
A^2ab
<
\frac14\bigl(n(n-2)^2\bigr)^{1/3}
<\frac n4
=\frac{D^2}{2}.
}
\tag{17.1}
\]

さらに

\[
(j-1)(n-j-1)=(n-1)A^2ab.
\]

左辺は \(1\pmod4\)、\(n-1\equiv3\pmod4\) なので

\[
\boxed{ab\equiv3\pmod4.}
\tag{17.2}
\]

従って

\[
\boxed{ab\ge3.}
\tag{17.3}
\]

したがって

\[
\boxed{A<D/\sqrt6.}
\tag{17.4}
\]

---

# 18. A-singleton M-factor の強い排除

A=q とする。

\[
BC=aN.
\]

Determinant を mod N で見ると

\[
\boxed{N\mid a^2+4ab_{\rm aux}}
\]

（ここでこの節の \(ab_{\rm aux}\) は六ブロック補助積。記号衝突回避のため、厳密には上節の \(ab\) を指す）。

Frey bridge から補助積が \(\ll a^2\) なので

\[
N<\frac{10}{3}a^2.
\]

\[
3N=aq+2
\]

より

\[
\boxed{q<10a.}
\tag{18.1}
\]

つまり A-singleton は線形 balanced。

---

# 19. A-mixed M-factor

\[
A=qc,
\qquad
N=cd.
\]

\[
BC=ad.
\]

Determinant を mod d で見ると

\[
\boxed{d\mid a^2+4c^2ab.}
\tag{19.1}
\]

Frey bridge から

\[
c^2ab\ll a^2.
\]

安全側で

\[
\boxed{d<\frac{10}{3}a^2.}
\tag{19.2}
\]

さらに A-block cross-modulus から

\[
\boxed{c<\frac34a.}
\tag{19.3}
\]

\[
3cd=aq+2
\]

を使うと

\[
\boxed{q<8a^2.}
\tag{19.4}
\]

従って

\[
\boxed{q\mid A\Longrightarrow q<8a^2.}
\tag{19.5}
\]

---

# 20. M-side 全配置の global cubic balance

まとめると

\[
q\mid A\Rightarrow q<8a^2,
\]

\[
q\mid B\Rightarrow q<49a^2,
\]

\[
q\mid C\Rightarrow q<72a^2.
\]

従って大きい方の M-side complete prime power q は無条件で

\[
\boxed{q<72a^2.}
\tag{20.1}
\]

\[
M=aq
\]

より

\[
\boxed{
(M/72)^{1/3}<a\le q<72^{1/3}M^{2/3}.
}
\tag{20.2}
\]

つまり M-side 2因子は全配置で cubic-balanced。

これはこのチャットの最も強い総合成果の一つ。

---

# 21. N-side A-block 上界

N-side complete prime power を

\[
Q,
\qquad
c=N/Q
\]

とする。

A-block が

\[
A=Qb
\]

で M-side constituent b を含むとする。

M-side 残りを m とすると

\[
M=mb,
\qquad
BC=mc.
\]

Determinant を mod m で見ると

\[
\boxed{m\mid9c^2+4b^2ab.}
\tag{21.1}
\]

Frey bridge より

\[
\boxed{b^2ab<\frac92c^2.}
\tag{21.2}
\]

従って

\[
\boxed{m<27c^2.}
\tag{21.3}
\]

さらに \(A<D/\sqrt6\) より

\[
\boxed{b<\sqrt{3/2}\,c<\frac54c.}
\tag{21.4}
\]

\[
3cQ=mb+2
\]

から

\[
\boxed{Q\mid A\Longrightarrow Q<12c^2.}
\tag{21.5}
\]

A-singleton ならさらに

\[
\boxed{Q<10c.}
\tag{21.6}
\]

従って A-block は N-side 巨大 factor の逃げ場でもない。

---

# 22. N-side endpoint 第3チャンク

N-side complete prime power

\[
Q=\pi^f,
\qquad
c=N/Q
\]

endpoint block を

\[
E=Qb
\]

とする。

\[
2cL=kQ-b
\]

となる正の奇数 k が存在し、mixed の場合

\[
\boxed{\gcd(k,b)=1.}
\tag{22.1}
\]

N-side quotient は

\[
\boxed{
\frac{n-2}{Q}
=(18c^2-1)Q+(Q-12c).
}
\tag{22.2}
\]

mod \(Q^2\) で

\[
\boxed{
3bt\equiv-(27bc+2k)\pmod Q.
}
\tag{22.3}
\]

mod \(Q^3\) で

\[
\boxed{
27b^2s
+81b^2c^2
-135bc\,k
+4k^2
\equiv0\pmod Q.
}
\tag{22.4}
\]

---

# 23. N-side mixed endpoint の絶対上界

mixed なので \(b>1\)。

もし Q が (22.4) 左辺の絶対値より大きければ整数等式になる。

mod b で

\[
4k^2\equiv0\pmod b
\]

となるが \(\gcd(k,b)=1\) に矛盾。

安全側の定数として

### C-mixed

\[
\boxed{Q<325b^2c^2.}
\tag{23.1}
\]

### B-mixed

\[
\boxed{Q<375b^2c^2.}
\tag{23.2}
\]

が得られる。

---

# 24. N-side B-singleton 例外

唯一 cubic balance から逃げやすい枝。

\[
B=Q,
\qquad
b=1.
\]

第3チャンクが整数等式になる領域では

\[
k=9g
\]

まで強制される。

さらに

\[
\boxed{
\frac c2\le g<\frac{5c}{9}
}
\tag{24.1}
\]

に改善。

endpoint 2進式は

\[
\boxed{v=v_2(3g-c).}
\tag{24.2}
\]

従って

\[
\boxed{
\frac c2\le3g-c<\frac{2c}{3}
}
\]

より

\[
\boxed{2^v<\frac{2c}{3}.}
\tag{24.3}
\]

すなわち

\[
\boxed{c>\frac32 2^v.}
\tag{24.4}
\]

さらに

\[
\boxed{9gQ\equiv1\pmod c}
\tag{24.5}
\]

なので g は

\[
\boxed{
g=\operatorname{leastpos}((9Q)^{-1}\bmod c)
}
\tag{24.6}
\]

で一意。

しかもこの逆元が狭い区間

\[
[c/2,5c/9)
\]

に入らなければならない。

---

# 25. N-side global cubic balance

N-side の大きい complete prime power を Q、相方を c とする。

M-side global cubic balance により mixed constituent の M-factor にも下界が入る。

A / C-singleton / mixed B/C を合わせると通常は

\[
\boxed{Q<18N^{2/3}.}
\tag{25.1}
\]

唯一の例外は N-side B-singleton branch。

この例外でも

\[
\boxed{Q<\frac{2N}{3\cdot2^v}.}
\tag{25.2}
\]

つまり N-side もほぼ cubic-balanced。

---

# 26. balanced \((2,4)\) の現在の姿

### M-side

無条件で

\[
\boxed{
(M/72)^{1/3}<M_i<72^{1/3}M^{2/3}.
}
\tag{26.1}
\]

### N-side

通常は

\[
\boxed{N_i<18N^{2/3}.}
\tag{26.2}
\]

唯一の例外は大きい N-factor が B-singleton で、

\[
\frac c2\le g<\frac{5c}{9},
\]

\[
9gQ\equiv1\pmod c,
\]

\[
v=v_2(3g-c),
\]

\[
2^v<\frac{2c}{3}.
\]

この例外枝は非常に薄い。

---

# 27. 第一・第二 Frey への再構成 bridge

balanced candidate で j と block が決まれば、六ブロック商から

\[
a=\frac{j-1}{RA},
\qquad
b=\frac{n-j-1}{SA},
\]

\[
g_0=\frac{j}{SB2^v},
\qquad
h_0=\frac{n-j}{RC2^v}.
\]

よって

\[
P=g_0h_0.
\]

また center 再構成から

\[
W_*,m
\]

も決まる。

したがって同一 endpoint candidate から

\[
\boxed{\mathcal Q}
\]

と

\[
\boxed{R_F}
\]

の両方を計算できる。

これは最初の担当目標

> 第一曲線の \(\mathcal Q\) と第二曲線の \(R_F\) が両方速く増える枝を、同じ全桁構造から結び付ける

への直接 bridge。

---

# 28. 監査で撤回・修正した事項

## 28.1 r=41, u=83 の 72-CRT 例

以前、72個の低位 CRT 配置が全滅する具体例として使ったが、

\[
Q_1=167\cdot57912614113275649087721
\]

の巨大因子が既存 Q1 complete-prime-power \(O(n^{2/3})\) 上界を先に破る。

したがって「72 CRT が必要な例」としては撤回。

## 28.2 determinant square / center square の独立性

これらは完全な candidate 再構成後には多くが恒等式。

「4個の独立平方条件」という以前の説明は撤回。

## 28.3 base-q compatibility と full p-adic Kummer

p進 e 桁を q=p^e で束ねた q-chunk compatibility は

full p-adic no-carry から従うが、逆は成り立たない。

したがって以前構成した grouped obstruction family は e>1 で真の full Kummer 反例族ではない。

## 28.4 moving-prime bounds

途中で未監査の moving-prime bounds を使いかけた箇所があった。

その後の主要結論では、repo 内で監査済みの cross-modulus / prime-neighbor results またはこのチャットで直接証明した chunk argument に置換した。

---

# 29. 既存固定合同だけでは不十分

repo には固定された有限個の法に対し中心合同条件を全て通る任意に大きい退化族が存在することが証明されている。

従って成功した今回の条件はすべて

- moving modulus \(q=p^e\),
- q² / q³ までの lift,
- full-digit chunk,
- endpoint inverse,
- block-size,
- Frey / determinant bridge

を使っており、固定合同の羅列ではない。

---

# 30. 現在もっとも重要な未解決点

## A. balanced \((2,4)\) の N-side B-singleton exception

現在もっとも薄い残枝。

必要条件は

\[
B=Q,
\]

\[
N=cQ,
\]

\[
\frac c2\le g<\frac{5c}{9},
\]

\[
9gQ\equiv1\pmod c,
\]

\[
v=v_2(3g-c),
\]

\[
2^v<\frac{2c}{3},
\]

さらに base-\(\pi\) full-digit condition を全部満たすこと。

ここを閉じれば N-side も完全 cubic-balanced になる。

## B. cubic-balanced 4-factor system 自体の排除

M-side は完全 cubic-balanced、N-side もほぼ cubic-balanced。

残る可能性では4 complete prime powers が極端には偏れない。

次の目標は order 条件

\[
\operatorname{ord}_{p}(2)=r
\]

(M-side)

\[
\operatorname{ord}_{p}(2)=2r
\]

(N-side)

と full-digit chunk を同時化し、cubic window 内の全配置を排除すること。

## C. \((3,3)\) even-u

odd-u は閉じたが even-u はまだ残る。

Q1 mixed split + 高々8 j 候補まで圧縮済み。

## D. support total >=7

support 6 の最小枝がかなり縮んだが、より多くの complete prime powers を持つ一般枝を全て排除したわけではない。

---

# 31. 現時点の重要な結論一覧

1. \((2,3)\) support は排除。
2. \((3,3)\) odd-u は排除。
3. balanced \((2,4)\) では \(u=2r+1\), u,r prime。
4. balanced では whole M/N block は不可能、必ず一つ mixed block。
5. endpoint C 候補は高々8個。
6. endpoint inverse から v,G,j が決定。
7. j から A,B,C,R,S が gcd で一意。
8. 補助因子 \(P,W_*,m\) まで再構成可能。
9. 第一・第二 Frey の \(\mathcal Q,R_F\) を同一 candidate から同時決定可能。
10. M-side endpoint chunk を mod q²/q³ まで上げ、strong asymmetry を排除。
11. M-side factor は全配置で \(q<72a^2\)。
12. よって M-side は無条件 cubic-balanced。
13. N-side A / mixed endpoint も二次・cubic bound を持つ。
14. N-side は B-singleton 例外を除き \(Q<18N^{2/3}\)。
15. B-singleton 例外も inverse interval + v2 条件まで一意化。
16. 固定合同だけではなく moving full-digit chunks が本質。

---

# 32. 次にやるべき順序

優先度1:

N-side B-singleton exception

\[
9gQ\equiv1\pmod c,
\qquad
c/2\le g<5c/9
\]

と full base-\(\pi\) no-carry を直接結合する。

優先度2:

M/N の cubic-balanced factor window と order \(r,2r\) 条件を結合。

優先度3:

balanced support を閉じた後、support >=7 へ一般化。

優先度4:

\((3,3)\) even-u の8候補系を full-digit chunk で排除。

---

# 33. ステータス

Erdős Problem 699 全体の完全解決はまだ主張しない。

i=3 全体の完全解決もまだ主張しない。

ただし担当1の「全桁 Kummer 条件」については、単純な桁和下界から大きく進み、

\[
\boxed{
\text{full-digit chunk}
\to
\text{endpoint}
\to
\text{factor balance}
\to
\text{Frey quantities}
}
\]

という大域的な bridge が構成できた。

特に balanced \((2,4)\) の M-side は、配置に依存せず cubic-balanced まで証明できたことが現在の最大成果。
