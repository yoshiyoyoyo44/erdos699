# i=3：増大するGにも通用する平方枝の一様排除

[入口](../../README.md) · [現在地](../../docs/STATUS.md) · [第二のFrey曲線](i3_growing_gap_and_auxiliary_frey_2026-09-21.md)

2026-09-21。基準コミットは `072a662549e76290084b0ec22b03cd2715e17b9e`。
**問題699全体も $i=3$ 全体も未解決。** 偶数 $j$ の増大する指数差 $G$ を引き続き扱う。

固定した $G$ の有限処理で使った因数分解を、$G$ が任意に増える場合に適用し直す。
今回は、既存の反例必要条件の下で

$$
\boxed{\delta_2q=\delta_2TPW_*\text{ は平方ではない}}
\tag{A}
$$

を全ての $G\ge14$ について証明する。
さらに中心方程式の先頭係数が平方になる場合は

$$
\boxed{G\text{ は奇数},\quad \gamma T\equiv7\pmod8,\quad
2G-u\ge7}
\tag{B}
$$

が必要である。従って **$G<(u+7)/2$ では、この先頭係数も平方にならない**。
$T=1$ を含め、$T$ 自体が平方の場合も先頭係数の平方を全て排除できる。
今回は新たな楕円曲線表や判別式・導手の一般定理を使わず、整数の因数分解と合同式で示す。

## 1. 出発点となる二つの中心条件

$u\ge51$, $v=v_2(j)\ge1$, $G=u-4v\ge14$、$n=\gamma T2^u$ とする。
四分岐 $(\gamma,\delta_1,\delta_2)$ は $(1,1,1),(1,1,3),(1,3,1),(3,1,1)$。
$T$ は正の奇数、$\gcd(T,\gamma\delta_1\delta_2)=1$。
$c_0=\delta_1^2\delta_2$, $B_G=\gamma c_0 2^{G-3}$ と置く。
[既存の中心式](i3_gap13_and_descent_continuation.md)と
[商の同定](i3_new_chat_integration_and_effective_gap_2026-09-21.md)により

$$
0<m<B_G,\quad m\text{ は奇数},\quad q=(B_G-m)/T=TPW_*>0,
$$
$$
\delta_2Z^2=m\gamma2^{u-1}+q,
\qquad
\delta_1T C_{\rm cen}^2=\delta_1\gamma2^{G-2+2v}+(n-1)Z
\tag{1}
$$

を満たす正の奇数 $Z,C_{\rm cen}$ が必要。
$C_{\rm cen}$ は六ブロックの $C$ とは異なる。
$Y=\delta_2Z$ とすれば第一式は

$$
Y^2=A_o2^{u-1}+\delta_2q,
\qquad A_o=\delta_2\gamma m\text{ は正の奇数}.
\tag{2}
$$

また $G-2+2v\ge14$, $u\ge51$ なので、(1)を法16で見ると
$Z\equiv-\delta_1T C_{\rm cen}^2$、$q\equiv\delta_2Z^2$。
奇数の四乗は法16で1であるから

$$
\boxed{q\equiv c_0T^2\pmod {16},\qquad
m\equiv-c_0T^3\pmod {16}.}
\tag{3}
$$

この合同式は小さい $G$ の列挙に限らず、今回の全範囲で使える。

## 2. 定数項が平方の枝をGに依存せず排除する

$\delta_2q=b_0^2$ と仮定する。$b_0$ は正の奇数で、(2)より $Y>b_0$。

$$
(Y-b_0)(Y+b_0)=A_o2^{u-1}.
$$

二因子の差は $2b_0$ なので、一方の2進付値は正確に1。
その因子の奇数部分は $A_o$ の約数であり、因子は $2A_o$ 以下。
もう一方も $2A_o+2b_0$ 以下なので

$$
2^{u-1}\le4A_o+4b_0.
\tag{4}
$$

$H=2^{G-3}\ge1$ と置く。四分岐を全て通じて

$$
A_o<\delta_2\gamma^2c_0 H=(\gamma\delta_1\delta_2)^2H\le9H,
$$
$$
b_0^2=\delta_2q<\frac{\delta_2\gamma c_0}{T}H\le9H.
$$

従って $4A_o+4b_0<36H+12\sqrt H\le48H$。
ところが $u=G+4v$, $v\ge1$ より
$2^{u-1}=H2^{4v+2}\ge64H$。これは(4)に矛盾する。
これで(A)を得る。証明の比較自体には $G\ge3$ で十分だが、
反例への適用は既に確立した $G\ge14$ の正規化の下で行う。

さらに(3)から $\delta_2q\equiv(\delta_1\delta_2T)^2\pmod {16}$。
$\operatorname{sf}(z)$ を平方因子を除いた正の整数とすれば

$$
\boxed{\operatorname{sf}(\delta_2TPW_*)\equiv1\pmod8,
\qquad \operatorname{sf}(\delta_2TPW_*)\ge17.}
\tag{5}
$$

非自明な平方因子を除いた奇数で法8が1となる最小値は17である。
これは個々の素因数が17以上という意味ではない。
例えば相異なる素数の積がこの条件を満たすこともある。

## 3. 先頭係数が平方ならGはuの半分より大きい

(2)を $Y^2=\mathcal A16^v+\delta_2q$ と書き、
$\mathcal A=\delta_2\gamma m2^{G-1}$ が平方だと仮定する。
$A_o$ は奇数なので $G$ は奇数、$A_o=s^2$、$s$ は正の奇数。
$u=G+4v$ も奇数である。(3)より

$$
s^2=\delta_2\gamma m\equiv-\gamma\delta_1^2\delta_2^2T^3
\equiv-\gamma T\pmod8,
$$

従って $\gamma T\equiv7\pmod8$。
特に $T$ が平方なら $\gamma T\equiv\gamma\in\{1,3\}$ なので不可能。

$L=s2^{(u-1)/2}$ は正の偶数であり、(2)は $Y^2=L^2+\delta_2q$。
$Y$ は整数で $Y\ge L+1$ なので

$$
\delta_2q\ge2L+1>2s2^{(u-1)/2}.
$$

$q<B_G/T$ と合わせて二乗し、$s^2=\delta_2\gamma m$ を代入すると

$$
\boxed{2^u mT^2< C_{\rm br}2^{2G-7},\qquad
C_{\rm br}=\delta_2\gamma c_0^2\in\{1,27,81,3\}.}
\tag{6}
$$

既に $C_{\rm br}\le81<128$, $mT^2\ge1$ なので $u<2G$ が従う。
合同条件を加えると、さらに次の整数下界になる。

| $(\gamma,\delta_1,\delta_2)$ | $C_{\rm br}$ | $T$ の下界 | $m$ の下界 | 必要な $2G-u$ の下界 |
|---|---:|---:|---:|---:|
| $(1,1,1)$ | 1 | 7 | 1 | 13 |
| $(1,1,3)$ | 27 | 7 | 3 | 11 |
| $(1,3,1)$ | 81 | 7 | 1 | 7 |
| $(3,1,1)$ | 3 | 5 | 3 | 13 |

$T$ の下界は $\gamma T\equiv7\pmod8$、$m$ の下界は
$\delta_2\gamma m$ が平方であることから得られる。
(6)は $2^{2G-u}>128mT^2/C_{\rm br}$ を意味する。
$2G-u$ が奇数であることも使い、四行の下界を得る。
従って全分岐共通の(B)が従う。
同じ条件を $G,v$ で書けば $G\ge4v+7$ である。

## 4. mとW_*の素数の平方条件も照合する

新しいFrey曲線で現れる素数と元の中心条件の関係を調べた。
第一の中心式へ $q=(B_G-m)/T$ を代入し、
$n/2-1=\delta_2ABC$ を使うと

$$
\boxed{TZ^2-mABC=\gamma\delta_1^2 2^{G-3}.}
\tag{7}
$$

従って $p\ge5$, $p\mid m$ では、$\gcd(m,T)=1$ より

$$
\left(\frac{\gamma T2^{G-3}}p\right)=1.
\tag{8}
$$

$G$ が奇数なら $\gamma T$、偶数なら $2\gamma T$ が平方剰余になる。
これは $m$ の素数が任意に大きくても課せる条件だが、元の中心式の帰結である。

一方、$D=n-2j$ とし、
$AW_*+TBCP=\delta_1\gamma2^{u-2v-1}$ へ $Tx^2$ を掛けると

$$
\delta_1n/2-\frac{\delta_1j(n-j)}{n-1}=ATx^2W_*.
$$

従って $n-1=\delta_1RS$ より

$$
\boxed{D^2+n(n-2)=4RSATx^2W_*.}
\tag{9}
$$

$p\ge5$, $p\mid W_*$ では $n(n-2)$ は単元なので $-n(n-2)$ は平方剰余。
これは既知の $(-\delta AP/p)=1$ と同じ平方類を表す。
実際、同じ法で $n\equiv2T^2x^2BCP/\delta_1$、$n-2=2\delta_2ABC$ より

$$
-n(n-2)\equiv-\delta AP\left(\frac{2TxBC}{\delta_1}\right)^2\pmod p.
$$

従って、$W_*$ で曲線と中心式を照合するだけでは、独立したもう一つの平方条件は増えない。
今回の実際の排除は、第2–3節の大きさと整数の平方の間隔を使う点にある。

## 5. 残る領域

第2節は前稿の表に残った四ケースを個別処理した因数分解を、全ての $G$ に広げたもの。
今後は $\delta_2q$ が平方のケースを、生成の時点で一律に除ける。

また前稿の対数的下限を超え、なお $G<(u+7)/2$ にとどまる広い領域では、
$\mathcal A$ と $\delta_2q$ の両方が非平方でなければならない。
$T=1$、より一般に $T$ が平方の場合も両方が非平方である。
ここでの二つの非平方は、以前排除した $j(n-j)/(n-1)$ の平方とは対象が違う。

**両方が非平方の方程式を今回排除したわけではない。**
先頭係数が平方でも $G\ge(u+7)/2$、$\gamma T\equiv7\pmod8$ と(6)を満たす枝は残る。
また(8)は素数の合同制約であり、$R_F$ の一様な上界にはなっていない。
引き続き、これらの非平方条件と全桁Kummer条件を結ぶ大域的な議論が必要である。

## 6. 検算

```text
python -X utf8 scripts/audit_i3_gap_square_obstructions.py
```

[検算器](../../scripts/audit_i3_gap_square_obstructions.py)と
[結果・分岐証明書](../../data/results/verification_i3_gap_square_obstructions.json)を保存した。
記号恒等式、四分岐の厳密な定数比較、256件の法16の条件、
317件の平方差の人工的な診断を確認する。
有限診断が無限領域の証明を代替するわけではなく、一般証明は本文の通り。
新たな外部計算は用いないが、既存の正規化と $G\ge14$ の証明依存は引き継ぐ。
