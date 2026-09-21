# i=3：三次整環の判別式と連分数末尾の制約

[入口](../../README.md) · [現在地](../../docs/STATUS.md) · [前稿](i3_dyadic_denominators_and_continued_fractions_2026-09-21.md)

2026-09-21。[添付原文](../../sources/source_progress_2026-09-21_cubic_discriminant_cf.md)を統合した。
**問題699全体も $i=3$ 全体も未解決。** 原文第5節の交差積を最大公約数に訂正し、結論を補って証明する。
定数49には既知の数体判別式下界を使う。37・71・229は確認待ちであり、以下の確定した必要条件には使わない。

**続報：** [小判別式の独立証明](i3_cubic_discriminant_minima_2026-09-21.md)で、この保留を解消した。
37を79へ改善し、71・229・961を外部の数体表なしで証明した。49の下界も独立に再証明している。
以下の「確認待ち」は本稿執筆時点の記録である。

## 1. 前提と判別式

反例を仮定する。既存の正規化により

$$
n=2^uM,\quad u\ge49,\quad M\text{ は正の奇数},\quad
4\le j<n/2,\quad v=v_2(j)<u,\quad K=2^vM.
$$

$y=n-j$ と置く。[既約性の稿](i3_irreducible_cubic_and_rational_gaps_2026-09-20.md)により

$$
F(z)=\sum_{r=0}^3\binom j{3-r}\binom yr z^r,\qquad
P(z)=\frac{6F(z)}{K(n-1)(n-2)}\in\mathbb Z[z]
$$

は既約で、三つの根は全て実数である。既存の判別式公式を定数倍すると

$$
\Delta:=\operatorname{Disc}(P)=
\frac{108j^2y^2(j-1)(y-1)}{K^4(n-1)^3(n-2)^2}.
\tag{1}
$$

$j^2y^2\le n^4/16$、$(j-1)(y-1)<n^2/4$ より、$n\ge64$ では

$$
0<\Delta<\frac{27n^6}{16K^4(n-1)^3(n-2)^2}<\frac{2n}{K^4}.
\tag{2}
$$

最後の不等式には $(1-1/n)^3(1-2/n)^2\ge(63/64)^3(62/64)^2>27/32$ を使った。
$\Delta$ は正の整数なので、外部分類を使わなくても $K^4<2n$ が従う。

## 2. モニックでない三次式から整環を作る

$P(z)=Az^3+Bz^2+Cz+E$、その根を $\theta$ とし、
$L=\mathbb Q(\theta)$、$\omega=A\theta$、$\eta=A\theta^2+B\theta$ と置く。
階数3の格子 $R=\mathbb Z+\mathbb Z\omega+\mathbb Z\eta$ は、

$$
\omega^2=A\eta-B\omega,\qquad
\omega\eta=-C\omega-AE,\qquad
\eta^2=-C\eta-E\omega-BE
$$

により乗法で閉じており、$L$ の整環（order）になる。
基底 $(1,\theta,\theta^2)$ からの変換行列の行列式は $A^2$ なので

$$
\operatorname{Disc}(R)=A^4\operatorname{Disc}(1,\theta,\theta^2)
=\operatorname{Disc}(P).
$$

$L$ は全実三次数体である。既知の最小判別式49を用いると
$\operatorname{Disc}(R)=[\mathcal O_L:R]^2\operatorname{Disc}(L)\ge49$。
下界の参照先は [LMFDB・全実三次数体の最小判別式49](https://www.lmfdb.org/NumberField/3.3.49.1)。
この最小性は外部の既知の結果として使用し、今回のPython検算で全数体の分類を再証明したとは扱わない。

(2)と合わせて、反例の必要条件は

$$
\boxed{49K^4<2n,\qquad 49K^3<2^{u-v+1},\qquad
49\,2^{4v}M^3<2^{u+1}.}
\tag{3}
$$

従来の $K^4<2n$ を強める。他の枝ごとに得た評価も引き続き併用する。

## 3. 分母の大きさに追加条件を置かない下界

$h=u-v$、$s=v_2(b)$ とし、前稿と同じく

$$
\Lambda(b)=
\begin{cases}
1&s=0,\\
2^{\min(s,h)}&s>0,\ s\ne h,\\
2^{h+1}&s=h.
\end{cases}
$$

既約分数 $0<a/b<1$ に対して $t=bj-an$、$x=|t|+2b$、$K_b=K\Lambda(b)$ とする。
前稿の基本不等式と $b\le x/2$ から

$$
\boxed{x^3\ge\frac{16K_b(n-1)(n-2)}{3n+16}>5K_bn.}
\tag{4}
$$

最後の不等式は $n^2-128n+32>0$、従って $n\ge128$ で成立する。
「追加条件なし」とは分母に関する適用条件が不要という意味で、反例を仮定する点は変わらない。

**端点 $0/1$ への拡張。** 前稿の三次式の値は、この場合
$\mathcal S=j(j-1)(j-2)=6F(0)>0$。
$K(n-1)(n-2)\mid\mathcal S$ は $P(0)\in\mathbb Z$ から従い、同じ上側評価も成立する。
従って(4)、および前稿の条件付き下界と次分母上界は $0/1$ にも拡張できる。

## 4. 最大公約数を補正した連分数末尾

$j/n$ の正規連分数（最後の部分商が2以上）の最後から一つ前の収束分数を $a/q$ とする。
$G=\gcd(n,j)$ と置くと、連続する収束分数の行列式から正しくは

$$
\boxed{|qj-an|=G,\qquad x=G+2q.}
\tag{5}
$$

原文の1は $j/G,n/G$ に約分した後の交差積であり、元の $j,n$ には使えない。
例えば $6/16=3/8=[0;2,1,2]$ の一つ前は $1/3$ で、$|3\cdot6-16|=2$。
これは恒等式の診断例であり、反例候補ではない。

$v_2(G)=v<u$ なので最後の分母 $n/G$ は偶数。その直前の $q$ は奇数で $\Lambda(q)=1$。
また $G=2^v\gcd(M,j/2^v)\le K$。
$H=(Kn)^{1/3}$ と置くと、(2)からの $K^4<2n$ と $n\ge2^{49}$ によって

$$
\left(\frac GH\right)^3\le\frac{K^2}{n}
<\sqrt{\frac2n}\le2^{-24}<10^{-3}.
$$

従って $G<H/10$。一方(4)より $G+2q>5^{1/3}H>(17/10)H$ なので

$$
\boxed{q>\frac45(Kn)^{1/3}.}
\tag{6}
$$

この証明は判別式49の外部定理には依存しない。
特に $q>1$ なので、一つ前にさらに収束分数が存在する。その分母を $c$ とする。
その分数が $0/1$ の場合も、第3節の拡張を使う。
もし前稿の適用条件

$$
4K^2\Lambda(c)^2n\ge27c^6
\tag{7}
$$

が成り立つなら、次分母上界と(6)から

$$
\frac{64}{125}Kn<q^3<\frac{32n}{K\Lambda(c)},\qquad
\boxed{K^2\Lambda(c)<\frac{125}{2}.}
\tag{8}
$$

従って $K\ge8$ の反例では必ず

$$
\boxed{4K^2\Lambda(c)^2n<27c^6.}
\tag{9}
$$

**$K\ge8$ 全体を排除したのではない。** (9)の領域は残る。
より一般には $K^2\Lambda(c)\ge125/2$ なら同じ結論になる。

## 5. 法2の形と確認待ちの定数

偶数 $j$ では $B_{\rm odd}$ は奇数なので、$P$ の係数の偶奇は $X_r/2^v$ から分かる。
$v=1$ のとき端の係数の付値は $v$ より大きく、中は $2v-1=v$。
$v\ge2$ のとき端の付値は $v$、中は $2v-1>v$。従って

$$
v=1:\ P(z)\equiv z+z^2\pmod2,\qquad
v\ge2:\ P(z)\equiv1+z^3=(z+1)(z^2+z+1)\pmod2.
$$

原文が提案する次の強化は、対応する数体分類・整環の指数の扱いを確認するまでは採用しない。

| 条件 | 確認待ちの強化 |
|---|---|
| 奇数 $j$、$w=\max(v_2(j-1),v_2(y-1))$ が奇数 | $37\,2^wM^3<2^u$ |
| 奇数 $j$、$w$ が偶数 | $71\,2^wM^3<2^u$ |
| $v\ge2$ | $\operatorname{Disc}(P)\ge229$ |

## 6. 検算と次の論点

```text
python -X utf8 scripts/audit_i3_cubic_discriminant_and_cf_tail.py
```

[検算器](../../scripts/audit_i3_cubic_discriminant_and_cf_tail.py)で判別式恒等式、整環の乗法、
有理数の末尾の最大公約数、係数の偶奇、定数評価を確認し、
[結果](../../data/results/verification_i3_cubic_discriminant_and_cf_tail.json)に保存する。
有限診断例は一般証明の代わりではなく、実在する反例を通過させた検算でもない。

次の焦点は、全桁Kummer条件などから(7)を満たす末尾構造が強制されるか、
あるいは残る(9)の領域を別の近似で排除できるかである。
現状ではその強制は証明できておらず、増大するパラメータの一様な排除は残る。
