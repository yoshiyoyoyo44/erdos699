# i=3：新成果の統合、素数冪の合同式、指数差の明示的有限化

[入口](../../README.md) · [現在地](../../docs/STATUS.md) · [二次捻りとKummer](i3_quadratic_twist_and_kummer_support_2026-09-21.md)

2026-09-21。[今回の添付原文](../../sources/source_i3_new_chat_results_2026-09-21.md)をバイトを変えず保存した。
基準は `71df9d56e3acd8fcddd88aa54e065e4cb7ac85d8`。
**問題699全体も $i=3$ 全体も未解決。** 以下は偶数 $j$ の枝についての必要条件である。
添付の主張を既存の式から監査し、その先を進めた。

今回の追加結果は、$W_*$ 全体を含む平方合同式と、指数差 $G=u-4v_2(j)$ による
計算可能な上限

$$
\boxed{u<\frac{6561}{4}\,2^G(G+10)^2+124}
$$

である。固定した $G$ の有限性を、具体的な上限を持つ有限性に強める。
また $G$ 自体が増大する場合も、$u\ge2^{42}$ なら $G>\tfrac12\log_2u$ が必要になる。

## 1. 記号と採用した結果

六ブロックの記号を用いる。$n=\gamma T2^u$, $u\ge51$, $v=v_2(j)\ge1$、
$x=2^v$, $G=u-4v\ge14$, $\delta=\delta_1\delta_2$, $c_0=\delta_1^2\delta_2$。
可能な $(\gamma,\delta_1,\delta_2)$ は $(1,1,1),(1,1,3),(1,3,1),(3,1,1)$。
$a,b,g_0,h_0,T,A,B,C,R,S$ は正の奇数で、$P=g_0h_0$ とする。
以前の $G_0,H_0$ は、ここでは $xg_0,xh_0$ に等しい。

$$
\begin{aligned}
n-1&=\delta_1RS,&(n-2)/2&=\delta_2ABC,\\
j&=TSBxg_0,&n-j&=TRCxh_0,\\
j-1&=RAa,&n-j-1&=SAb,\\
T^2x^2BCP-A^2ab&=\delta_1.
\end{aligned}
\tag{1}
$$

[既存の $W_*$ の稿](i3_digit_reciprocity_and_W_continuation.md)により

$$
W_* =\frac{\delta BC-Aab}{Tx^2}>0\text{ は奇数},\qquad
AW_*+TBCP=\delta_1\gamma2^{u-2v-1},
$$
$$
aBg_0+bCh_0=2xW_*,\qquad
\gcd(W_*,TABC)=1,\quad \gcd(W_*,P)\mid\delta_1\gamma.
\tag{2}
$$

$W_*$ は三次判別式を分解する以前の $W$ とは別の整数である。

| 添付の結果 | 監査と統合 |
|---|---|
| $q=TPW_*$、$T^2\mid B_G-m$ | 第2節で既存の中心式から直接証明 |
| $\gcd(m,q)\mid\gamma c_0$ | $m+Tq=B_G$ と $m$ が奇数であることから従う |
| $P$ の上界、$W_*$ の下界 | 第3節で確認。さらに $abP^2$ 全体に上界を付ける |
| $W_*$ と $abP$ の5以上の素数台の分離 | (2)と $\delta BC-Aab=Tx^2W_*$ から従う |
| $(-\delta AP/p)=1$ と2進平方条件 | 第4節で素数冪を含む法 $2^{v+1}W_*$ の平方合同式へ強化 |
| endpoint の付値と整除性 | 第5節で除数を明示し、対称側も確認 |
| $S$-unit 型の和 | 等式として採用。ただし $S$ は候補ごとに変わるため、固定 $S$ の有限性をそのまま全体へ適用しない |

## 2. 二つの商の同定

[指数差の既存稿](i3_exact_gap_and_g9_continuation.md)の中心の整数は

$$
w=(\delta A-2T^2x^2P)(\delta BC-2Aab)
=c_0+4Tx^4m,
$$
$$
B_G=\gamma c_0 2^{G-3},\quad 0<m<B_G,\quad m\text{ 奇数},\quad
\gcd(m,T)=1,\quad q=(B_G-m)/T>0.
$$

(1)と $n=2\delta_2ABC+2$ を使って展開すると

$$
c_0(n+2)-2w=8T^3x^4PW_*.
$$

一方 $w=c_0+4Tx^4m$ と $n=\gamma T2^Gx^4$ を代入すれば左辺は $8T^2x^4q$。
従って添付の正確な同定

$$
\boxed{q=TPW_*,\qquad m+T^2PW_*=\gamma c_0 2^{G-3},\qquad T^2\mid B_G-m}
\tag{3}
$$

を得る。$d\mid\gcd(m,q)$ なら $d\mid B_G$、$m$ は奇数だから
$\gcd(m,q)\mid\gamma c_0$。特に $m$ と $q$ の5以上の素数台は分離する。

## 3. 大きさの評価と、判別式の積全体への強化

[ブロックの上界](i3_cross_modulus_and_digit_height_2026-09-20.md)と既存の正値性は

$$
4(n-1)A^2\le\delta_1(n-2)^2,\qquad \delta A>2T^2x^2P,\qquad
W_*>\frac{\delta BC}{2Tx^2}
$$

を与える。添付の計算をそのまま確認すると

$$
P^2<\frac{\gamma\delta_1^3\delta_2^2}{16T^3}
\frac{(n-2)^2}{n(n-1)}2^G,
\qquad
W_*^2>\frac{\delta_1\gamma}{4T}\left(1-\frac1n\right)2^G.
\tag{4}
$$

この二式を割れば、追加の比率制約も得られる。

$$
\boxed{\frac{W_*}{P}>\frac{2T}{\delta}\frac{n-1}{n-2}.}
\tag{5}
$$

さらに[二次捻りの稿の判別式公式](i3_quadratic_twist_and_kummer_support_2026-09-21.md)へ
$G_0=xg_0,H_0=xh_0$ を代入すると、三次判別式は

$$
\Delta=\frac{27abP^2}{\gamma^4\delta_1^3\delta_2^2}.
$$

[整数係数からの評価](i3_four_chat_integration_2026-09-21.md) $\Delta<27n/(16K^4)$、
$K=x\gamma T$ を用い、

$$
\boxed{abP^2<\kappa\frac{2^G}{T^3},\qquad \kappa=\frac{\gamma\delta_1^3\delta_2^2}{16}}
\tag{6}
$$

を得る。$\kappa$ は四分岐の順に $1/16,9/16,27/16,3/16$。
これは $P$ だけでなく、残る導手を支配する積全体の上界である。
より精密には右辺に $n(n-4)/(n-2)^2<1$ を掛けられるが、以下では(6)で十分。

## 4. 全ての素数冪を含む平方合同式

添付の素数ごとの条件を、一つの法へまとめて強める。

$$
L_*=2xW_*,\qquad U=aBg_0,\qquad V=bCh_0.
$$

(2)から $U+V=L_*$。また $v\ge1$ なので $2x\mid x^2$、従って
$\delta BC\equiv Aab\pmod{L_*}$。
$\gcd(BC,L_*)=1$ だから逆元を使って

$$
r\equiv AU(BC)^{-1}\equiv Aa g_0 C^{-1}\pmod{L_*}
$$

と置ける。$U^2\equiv-UV=-abBCP$ より

$$
\boxed{r^2\equiv-\delta AP\pmod{2^{v+1}W_*}.}
\tag{7}
$$

これは $W_*$ の各素因数だけでなく、そこに含まれる全素数冪の指数まで保つ。
代数的には次の正確な恒等式に対応する。

$$
B\bigl((Aa g_0)^2+\delta AP C^2\bigr)
=A g_0 xW_*\bigl(2Aa+TxCh_0\bigr).
\tag{8}
$$

右辺は $2xW_*$ の倍数である。
$p\ge5$, $p\mid W_*$ では $p\nmid abPABC$ なので、(7)から添付の
$(-\delta AP/p)=1$ を回収する。$v\ge2$ では $r$ は奇数なので $\delta AP\equiv-1\pmod8$。
ただし(7)は既存の因子恒等式から従う条件であり、全桁Kummerとは独立の新しい仮定ではない。

素数台の分離も明記する。$p\ge5$, $p\mid W_*$ なら(2)から $p\nmid TABC P$。
$\delta BC\equiv Aab\pmod p$ の左辺は単元なので $p\nmid ab$。
従って $W_*$ に現れるこの素数は、三次判別式 $\Delta$ の素因数ではない。
$W_*$ の増大だけから、三次判別式側の素数集合が増えるとは結論できない。

## 5. 二つのendpointの正確な商

$Q_1=(n-1)/\delta_1$, $Q_2=(n-2)/(2\delta_2)=ABC$ とする。
$\rho=j(j-1)/(2Q_1)$、$\lambda=\rho(\rho-\delta_1)/Q_2$ について、(1)より

$$
\rho=T ABa\,2^{v-1}g_0,
\qquad
\boxed{\lambda=T2^{v-1}ag_0\,\frac{\rho-\delta_1}{C}.}
\tag{9}
$$

$j\equiv2$, $n\equiv2\pmod C$ だから $\rho\equiv\delta_1\pmod C$。
分母 $2(n-1)$ は $C$ と互いに素なので、この合同式には逆元の問題がない。
従って右端の商も整数。
対称に $y=n-j$ を使えば

$$
\rho_y=T ACb\,2^{v-1}h_0,
\qquad
\boxed{\lambda_y=T2^{v-1}bh_0\,\frac{\rho_y-\delta_1}{B}.}
\tag{10}
$$

$v\ge2$ では $\rho,\rho_y$ は偶数、$\delta_1,B,C$ は奇数なので
$v_2(\lambda)=v_2(\lambda_y)=v-1$。
添付の両側の整除性が従う。$v=1$ にこの付値の結論を拡張しない。

## 6. 新しい帰結：固定した指数差の計算可能な上限

二次捻り後の導手の量は、5以上の素数だけを残す記号を用いて

$$
\mathcal Q=\operatorname{rad}_{\ge5}(ab)
\operatorname{rad}_{\ge5}(\operatorname{cf}_3(P))^2\le abP^2.
$$

従って(6)から $\mathcal Q<\kappa2^G/T^3$。
前稿は [von Känel, Corollary 6.2](https://arxiv.org/html/1310.7263v2#S6.SS1)を使い、

$$
u\le972\mathcal Q b_*^2+124,\qquad b_*=\lceil\log_2(486\mathcal Q)\rceil
$$

を証明している。$486\kappa\le486\cdot27/16<2^{10}$ と $T\ge1$ より $b_*\le G+10$。
従って

$$
\boxed{u<\frac{243\gamma\delta_1^3\delta_2^2}{4T^3}
2^G(G+10)^2+124
\le\frac{6561}{4}2^G(G+10)^2+124.}
\tag{11}
$$

前の固定 $G$ の有限性は、有限個の四次曲線にSiegelの定理を適用するものだった。
(11)は $G$ から直接計算できる上限であり、曲線ごとの整数点の完全決定を前提としない。
さらに(6)の $abP^2\ge1$ から $T^3<\kappa2^G$ なので、$G$ の上限があれば
$T,u,n,j$ の明示的な有限範囲が得られる。
ただし、この範囲が実用的な大きさだとは主張しない。

この帰結には既知の判別式・導手の一般定理を使う。
前稿の小さい素数集合の排除に用いた公開曲線全リストの完全性には依存しない。
前提の $G\ge14$ などが持つ既存の証明依存は引き継ぐ。

## 7. 指数差も増大する枝への制約

(11)から、$u\to\infty$ の反例列では

$$
\boxed{G\ge\log_2u-2\log_2\log_2u-O(1).}
\tag{12}
$$

実際 $G\le\log_2u$ の場合は、(11)の $(G+10)^2$ を $(\log_2u+10)^2$ で置き換えて対数を取ればよい。
$G>\log_2u$ の場合も(12)は自動的に成り立つ。
従って任意の固定した $\epsilon>0$ に対し、
$G\le(1-\epsilon)\log_2u$ の枝は十分大きい $u$ で不可能である。

一つの閾値を完全に明示すると

$$
\boxed{u\ge2^{42}\quad\Longrightarrow\quad G>\tfrac12\log_2u.}
\tag{13}
$$

証明：$z=\log_2u\ge42$ とし、逆に $G\le z/2$ と仮定する。(11)を $u$ で割ると

$$
1<\frac{6561(z/2+10)^2}{4\cdot2^{z/2}}+\frac{124}{2^z}.
$$

右辺は $z\ge42$ で減少する。
第一項の対数微分は $1/(z/2+10)-(\log2)/2<0$、第二項も減少。
$z=42$ での値は厳密に $826424819743/1099511627776<1$ であり矛盾する。

## 8. 残ることと検算

添付により指数差と $W_*$ の対応が明確になり、(6)が導手との橋を与えた。
今回は固定 $G$ の有効有限化と、$G$ が遅く増大する枝の制限まで得た。
**$G$ が(12)を満たして増大する領域は残る。**
(3)の $S$-unit 型の式や(7)の平方条件だけから、その領域の排除は示していない。
奇数 $j$ の全領域も、この稿の対象外である。

```text
python -X utf8 scripts/audit_i3_new_chat_and_effective_gap.py
```

[検算器](../../scripts/audit_i3_new_chat_and_effective_gap.py)と
[結果](../../data/results/verification_i3_new_chat_and_effective_gap.json)を保存した。
記号恒等式と一般証明を中心にし、有限の合同式診断は補助として区別する。
