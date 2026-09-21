# i=3：二次捻りによる3乗因子の除去と、Kummer補助因子への還元

[入口](../../README.md) · [現在地](../../docs/STATUS.md) · [前稿：楕円曲線と増大速度](i3_discriminant_support_and_elliptic_curve_2026-09-21.md)

2026-09-21。**問題699全体も $i=3$ 全体も未解決。**
前稿の6乗因子の除去を3乗因子まで強める。
さらに、残る素数集合をKummerの四つの補助因子だけで正確に表す。
以下は反例の必要条件であり、この条件を満たす数から反例が作れるという主張ではない。

## 1. 引き継ぐ式

[4チャット統合稿](i3_four_chat_integration_2026-09-21.md)と前稿の記号を使う。
$n=2^uM$, $u\ge51$, $v=v_2(j)$, $K=2^vM$, $h=u-v$, $N=2^h$、$y=n-j$。
三次式を $P(1+z)=N+Az+Bz^2+Cz^3$ と書くと、$A$ は奇数で全係数は整数。
$\Delta=\operatorname{Disc}(P)>0$ として

$$
H=A^2-3NB=\frac{3\ell s}{\varepsilon},\qquad
J=2A^3-9NAB+27N^2C=-\frac{18st}{\varepsilon^2},\qquad
\Delta=\frac{s^2W}{\varepsilon^2}.
\tag{1}
$$

ここで $\varepsilon\in\{1,3\}$、$s$ は正の奇数。
前稿第6節は、$p\ge5$ について次を証明している。

* $p\mid W$ なら $p\nmid s\ell$。
* $p\mid s$ なら $p\nmid Wt$。

これにより、前稿の曲線の $p\mid s$ における不変量の付値は
$v_p(c_4)=m+v_p(\ell)$, $v_p(c_6)=m$, $v_p(\Delta(E))=2m$、$m=v_p(s)$ だった。

## 2. 2進条件を保つ二次捻り

奇数の平方因子を持たない整数 $D$ を取り、符号を $DA\equiv1\pmod4$ となるように選ぶ。
曲線 $Y^2=X^3+AX^2+NBX+N^2C$ の $D$ による二次捻りから、整数モデル

$$
E_D:\quad z^2+xz=x^3+\frac{DA-1}{4}x^2
+\frac{D^2NB}{16}x+\frac{D^3N^2C}{64}
\tag{2}
$$

を得る。$h\ge42$ なので係数は全て整数。不変量を直接計算すると

$$
c_4(E_D)=D^2H,\qquad c_6(E_D)=-D^3J/2,\qquad
\Delta(E_D)=D^6 2^{2h-8}\Delta.
\tag{3}
$$

$D,H$ は奇数なので、このモデルは2で最小で乗法的還元を持つ。
従って前稿の強い2進条件をそのまま保つ。

$$
v_2(\Delta_{\min}(E_D))=
\begin{cases}
2u+w-7,&j\text{ 奇数},\\
2(u-v)-8,&j\text{ 偶数},
\end{cases}
\qquad v_2(\Delta_{\min})\ge76.
\tag{4}
$$

$j$ 不変量も二次捻りで変わらず、前稿の $1728$ への接近条件を保つ。

## 3. 5以上の素数で最小となる捻りの選択

各 $p\ge5$, $p\mid s$ について $m=v_p(s)=6a+r$, $0\le r\le5$ と書き、

$$
d_p=\begin{cases}0,&r=0,1,2,\\1,&r=3,4,5\end{cases},
\qquad |D|=\prod_{p\ge5,\ p\mid s}p^{d_p}
\tag{5}
$$

と選ぶ。$D$ の符号は第2節の条件で決める。
捻り直後の付値は $m+2d_p+v_p(\ell)$, $m+3d_p$, $2m+6d_p$。
$p\ge5$ では短いWeierstrassモデルの分母48・864は単元なので、最大の最小化スケールは

$$
q_p=\left\lfloor\frac{m+3d_p}{6}\right\rfloor=a+d_p.
$$

実際、$4q_p\le m+2d_p+v_p(\ell)$ と $6q_p\le m+3d_p$ が成り立ち、
$q_p+1$ は後者を満たさない。従って

$$
\boxed{v_p(\Delta_{\min}(E_D))=2(m\bmod3)\qquad(p\ge5,\ p\mid s).}
\tag{6}
$$

| $m\bmod6$ | $d_p$ | 最小判別式の付値 | 還元 |
|---:|---:|---:|---|
| 0 | 0 | 0 | 良い |
| 1 | 0 | 2 | 加法的 |
| 2 | 0 | 4 | 加法的 |
| 3 | 1 | 0 | 良い |
| 4 | 1 | 2 | 加法的 |
| 5 | 1 | 4 | 加法的 |

悪い場合は最小 $c_4$ の付値も正である。従って導手の指数は2。
$p\mid W$ では $p\nmid D$ なので、前稿と同じく乗法的還元、導手の指数は1。
それ以外の $p\ge5$ では良い還元である。

**この除去は二次捻りの範囲で最適である。** 任意の二次捻りは、局所的に $d_p=0$ または1へ帰着する。
最小化による判別式の付値の変化は12の倍数なので、$p\mid s$ における付値は
$2m$ または $2m+6$ と法12で合同になる。
どちらかが0となる必要十分条件は $3\mid m$。
(5)は可能な最小値 $2(m\bmod3)$ を実際に達成する。
$p\mid W$ で捻ると $c_4$ の付値は2となり最小化できず、判別式の付値は $v_p(W)+6$。
これも良い還元にはならない。

## 4. 3乗を除いた素数集合と、その増大速度

$s=s_{\rm cube}^{\,3}s_3$、$0\le v_p(s_3)\le2$ と分け、

$$
R_W=\prod_{p\ge5,\ p\mid W}p,\qquad
R_3=\prod_{p\ge5,\ p\mid s_3}p,\qquad
\mathcal R=R_WR_3,\qquad \mathcal Q=R_WR_3^2
\tag{7}
$$

と置く。前稿の6乗を除いた $R_s,R,Q$ と混同しないよう、別記号にする。
この曲線の導手は正確に

$$
\boxed{N_{E_D}=2\cdot3^{f_3}\mathcal Q,\qquad 0\le f_3\le5.}
\tag{8}
$$

従って、前稿の全曲線リストによる排除と判別式・導手の評価を、より小さい集合へ適用できる。

$$
\boxed{\mathcal R>166,\qquad \mathcal R\text{ は13以上の素因数を持つ。}}
\tag{9}
$$
$$
\boxed{u\le972\mathcal Q\left\lceil\log_2(486\mathcal Q)\right\rceil^2+124.}
\tag{10}
$$

特に $u\to\infty$ となる反例の列で $\mathcal Q=o(u/(\log u)^2)$ は不可能。
具体的に $u\ge2^{40}$ なら $\mathcal R>u^{1/4}$。
(9)は公開曲線リストの完全性に依存し、(10)は
[von Känel, Corollary 6.2](https://arxiv.org/html/1310.7263v2#S6.SS1)に依存する。
これらの数値や外部定理を新たに証明したのではなく、前稿の適用対象を強めた。

例えば $s=\rho^3$ なら $\rho$ の素数も指数も全て自由に増やせる。
$W$ の5以上の素因数が全て $5,7,11$ に含まれる場合、(9)により反例ではない。
前稿では $\rho$ の素数が $s$ に指数 $3\bmod6$ で現れると、この排除を適用できなかった。

## 5. Kummerの補助因子との正確な対応

ここだけは[全桁条件の稿](i3_digit_reciprocity_and_W_continuation.md)の六ブロックを使い、
本稿の $A,B,C$ と区別して $A_0,B_0,C_0,R_0,S_0,T$ と書く。
$\gamma,\delta_1,\delta_2\in\{1,3\}$ は既存の3の例外で、$M=\gamma T$。
正整数 $a,b,G_0,H_0$ を

$$
\begin{aligned}
n-1&=\delta_1R_0S_0,& (n-2)/2&=\delta_2A_0B_0C_0,\\
j&=TS_0B_0G_0,&y&=TR_0C_0H_0,\\
j-1&=R_0A_0a,&y-1&=S_0A_0b
\end{aligned}
\tag{11}
$$

で定義する。これは完全素数冪に対するKummerの低位桁の割当てから得る。
四つの補助因子は、割り当てた完全素数冪を取り除いた後の商である。

整数系の $g$ は $g=\gcd((n-2)/2,j-1)$ とも書ける。
完全素数冪の割当てから $A_0\mid g$ であり、$B_0,C_0$ は $j-1$ と互いに素。
従ってある $\eta\mid\delta_2$ により

$$
g=\eta A_0,\qquad \eta\in\{1,3\},\qquad
\ell=\delta_2B_0C_0/\eta.
$$

ここで、$\gcd(K,(n-2)/2)=1$ なので、前稿の $g=\gcd((n-2)/2,e)$ と一致する。
(11)を $s$ と $W$ の式へ代入すると、全ての例外因子を残した正確な式

$$
\boxed{s=\frac{3\varepsilon\eta G_0H_0}{2^{2v}\gamma^2\delta_1\delta_2},
\qquad W=\frac{3ab}{\delta_1\eta^2}}
\tag{12}
$$

を得る。従って任意の $p\ge5$ で

$$
\boxed{v_p(s)=v_p(G_0H_0),\qquad v_p(W)=v_p(ab).}
\tag{13}
$$

整合性の別の確認として、三次判別式を直接(11)で書けば

$$
\Delta=\frac{27abG_0^2H_0^2}{2^{4v}\gamma^4\delta_1^3\delta_2^2}.
\tag{14}
$$

$A_0,B_0,C_0,R_0,S_0,T$ は消える。
これらのブロックが有界になったという意味ではない。

$\operatorname{rad}_{\ge5}(z)$ を $z$ の異なる5以上の素因数の積、
$\operatorname{cf}_3(z)$ を $z$ の3乗を除いた部分と書くと、(7)は

$$
\boxed{\mathcal Q=
\operatorname{rad}_{\ge5}(ab)\,
\operatorname{rad}_{\ge5}(\operatorname{cf}_3(G_0H_0))^2.}
\tag{15}
$$

さらに、四因子 $a,b,G_0,H_0$ のどの二つも5以上の共通素因数を持たない。
$a,b$ の場合は、共通素数が $j-1,y-1,n-2$ を割るため $A_0$ へ完全冪が割り当てられ、
両者でその指数を超えると $n-2=(j-1)+(y-1)$ の付値に反する。
$G_0,H_0$ の場合は $n=2^u\gamma T$ と $T$ の完全冪を除いたことから従う。
$a,G_0$ および $b,H_0$ は隣接整数の互いに素性、
残る組は既存の恒等式 $T^2B_0C_0G_0H_0-A_0^2ab=\delta_1$ から従う。

## 6. 大きい素数と全桁条件の間に残る障害

(15)はKummerの因子表示と導手を結ぶが、まだ上界ではない。
とくに $p\ge5$, $p\nmid n(n-1)(n-2)$ なら、全ての割当てブロックで $p$ は単元。
この場合、捻り後の曲線の局所導手指数は正確に

$$
f_p=\begin{cases}
1,&p\mid(j-1)(y-1),\\
2,&v_p(jy)\not\equiv0\pmod3,\\
0,&\text{その他}.
\end{cases}
\tag{16}
$$

最初の二条件は同時には成立しない。
これらの素数は $\binom n3$ を割らないため、その素数自身については
「共通素因数を避ける」というKummer条件がかからない。
従って $\binom n3$ の素因数での桁条件を個別に並べるだけでは、(15)の全素数を直接検査していない。
これをKummer法の不可能性の証明とは解釈しない。異なる素数の条件が同じ $j$ を通じて
これらの補助因子を制約する余地は残っている。

完全解決へ残る具体的な対象は(15)の積である。
この積の上界を(10)と衝突する強さで導くか、全桁条件を使う別の矛盾が必要になる。
今回は3乗因子を含む新しい無限枝を排除し、二次捻りで残った5以上の素数を消すだけでは先へ進めない境界も確定した。

## 7. 検算

```text
python -X utf8 scripts/audit_i3_twist_and_kummer_support.py
```

[検算器](../../scripts/audit_i3_twist_and_kummer_support.py)は、任意の $D$ のモデルと不変量、
六つの剰余類の局所最小化と最適性、Kummerブロックとの恒等式を記号計算する。
小さい整数での補助診断も行うが、それを上の一般証明の代わりにしない。
[結果](../../data/results/verification_i3_twist_and_kummer_support.json)に実行内容を保存する。
