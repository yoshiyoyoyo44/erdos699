# i=3：一般の偶数 j に対する冪の重複と Kummer ブロックの素数台

[入口](../../README.md) · [現在地](../../docs/STATUS.md) · [9月22日の統合](i3_four_handoffs_integration_2026-09-22.md)

2026-09-23。基準コミット `5481bbd29dc0f7523e9099aa06fafd54a9a9742c`。
**一般枝の完全解決には至っていない。** 本稿は、T=1 や少数素数台を仮定せず、偶数 j の四分岐全てに使える必要条件を証明する。奇数 j は本稿の対象外である。

第一曲線の導手に現れない高い冪を数える整数を導入し、それと T を同時に抑える。次に n−1 と n−2 の直接の二曲線を独立に確認し、補助因子 abP の外に必要な Kummer ブロックの素数台を評価する。G が log₂u に近い領域では、T と高い冪は u の任意の固定正冪より遅くしか増えず、ブロック側には少なくとも u に近い大きさの素数の積が必要になる。

## 1. 仮定と既存入力

[既存の正規化](i3_new_chat_integration_and_effective_gap_2026-09-21.md)を用い、

$$
n=\gamma T2^u,\quad u\ge51,\quad x=2^v,\quad v=v_2(j)\ge1,
\quad G=u-4v\ge14,
$$

$$
(\gamma,\delta_1,\delta_2)\in\{(1,1,1),(1,1,3),(1,3,1),(3,1,1)\},
\quad\delta=\delta_1\delta_2,\quad c_0=\delta_1^2\delta_2,\quad P=g_0h_0.
$$

六ブロックは正の互いに素な奇数で、

$$
n-1=\delta_1RS,\quad n-2=2\delta_2ABC,\quad
j=TSBxg_0,\quad n-j=TRCxh_0,
$$

$$
j-1=RAa,\quad n-j-1=SAb,\quad
T^2x^2BCP-A^2ab=\delta_1.
\tag{1}
$$

以後 rad₅ は p≥5 の異なる素因数の積、cf₃ は各素数の指数を 3 で割った余りに落とす演算とする。

$$
\mathcal Q=\operatorname{rad}_5(ab)\operatorname{rad}_5(\operatorname{cf}_3(P))^2,
\qquad \kappa=\frac{\gamma\delta_1^3\delta_2^2}{16}\le\frac{27}{16}.
$$

[第一曲線の既存評価](i3_quadratic_twist_and_kummer_support_2026-09-21.md)と[指数差の評価](i3_new_chat_integration_and_effective_gap_2026-09-21.md)は

$$
u\le972\mathcal Q\lceil\log_2(486\mathcal Q)\rceil^2+124,
\qquad abP^2<\frac{\kappa2^G}{T^3}.
\tag{2}
$$

導手と判別式の定量評価に使う外部入力は、[von Känel, Corollary 6.2](https://arxiv.org/html/1310.7263v2#S6.SS1) の

$$
\log|\Delta_{\min}(E)|\le3N_E(\log N_E)^2+124
\tag{3}
$$

である。自然対数の式を用いる。公開全曲線表の完全性、9月22日の h₅ の排除、有限 lifting ladder は本稿の新しい評価には使わない。

## 2. 中心比率を使う正確な式の独立検算

9月22日の二曲線メモが報告した比率を、以前の整数の商 λ と区別して、本稿では η と書く。

$$
H_1=\delta A-2T^2x^2P,\quad
\eta=\frac{H_1}{\delta A},\quad \theta=1-\eta.
$$

既存の正値性 H₁>0 より 0<η,θ<1。(1)から

$$
\theta=\frac{2T^2x^2P}{\delta A}
=\frac{4j(n-j)}{(n-1)(n-2)}.
\tag{4}
$$

**補題1。** 次の完全恒等式が成り立つ。

$$
\boxed{abP^2=\frac{\kappa2^G}{T^3}\,
\theta^2\frac{(n-2)\theta-4}{n}
<\frac{\kappa2^G}{T^3}\theta^3.}
\tag{5}
$$

証明：δ₂ABC=(n−2)/2 と θ の定義を行列式へ入れると

$$
A^2ab=\delta_1\left(\frac{(n-2)\theta}{4}-1\right),
\quad P=\frac{\delta A\theta}{2T^2x^2}.
$$

二式を掛け合わせ、n=γT2ᴳx⁴ を使えば等号を得る。右辺は正であり、((n−2)θ−4)/n<θ なので不等号も従う。□

同じ代数監査では、W*=(δBC−Aab)/(Tx²)、w=H₁(δBC−2Aab)、m=(w−c₀)/(4Tx⁴)、B_G=c₀n/(8Tx⁴) に対して

$$
\frac m{B_G}=\eta^2-\frac{2\theta^2}{n}
\tag{6}
$$

および担当2の中心因数分解・ノルム式も確認した。Z は (AW*−TBCP)/2 と置くと第一中心式を満たす。AW*>TBCP は

$$
AW_*-TBCP=\frac{H_1BC+\delta_1}{Tx^2}>0
$$

から分かるので、既存の正の中心 Z と一致する。これは中心式を新しい独立条件として数え増す操作ではない。

## 3. T と高い冪を同時に抑える

$$
A_0=\operatorname{rad}_5(ab),\quad
V=\operatorname{rad}_5(\operatorname{cf}_3(P)),\quad
\mathcal E:=\frac{abP^2}{\mathcal Q}.
$$

E は正の整数である。具体的に

$$
C_P=\prod_{p\ge5}p^{\lfloor v_p(P)/3\rfloor},\qquad
V_2=\prod_{\substack{p\ge5\\v_p(P)\equiv2\ (3)}}p
$$

と置くと

$$
\boxed{\mathcal E=\frac{ab}{A_0}\,3^{2v_3(P)}C_P^6V_2^2.}
\tag{7}
$$

証明は素数ごとの指数比較である。p≥5、e=vₚ(P)=3k+r の寄与は、r=0,1 では 6k、r=2 では 6k+2。ab 側の寄与は vₚ(ab)−1、3 の寄与はそのまま残る。□

**定理2。** u>124 なら、

$$
\boxed{T^3\mathcal E<\mathcal B(u,G)\theta^3,
\qquad
\mathcal B(u,G):=\frac{972\kappa2^G(G+10)^2}{u-124}.}
\tag{8}
$$

特に T³C_P⁶< B(u,G)、従って T C_P²< B(u,G)^(1/3)。

証明：486Q<486κ2ᴳ<2^(G+10) なので、⌈log₂(486Q)⌉≤G+10。(2)から

$$
\mathcal Q\ge\frac{u-124}{972(G+10)^2}.
$$

一方 Q E=abP² である。(5)と合わせると(8)を得る。□

この式は元の粗い T³<κ2ᴳ を、第一曲線が必要とする導手の大きさで割ったものになっている。T だけでなく、ab の重複素因数、P の三乗部分、P で指数が 2 mod 3 となる素数を同時に制限する。

**系2.1。** 仮想反例列で u→∞、

$$
G\le\log_2u+c\log_2\log_2u+C
$$

（c≥0 と C は固定）なら

$$
T^3\mathcal E=O((\log u)^{c+2}),\quad
T=O((\log u)^{(c+2)/3}),\quad
C_P=O((\log u)^{(c+2)/6}).
\tag{9}
$$

さらに p²|ab なら p≤E、p²|P かつ p≥5 なら p²≤E。この領域で十分大きい素数は T を割れず、ab と P には高々一乗でしか現れない。G=(1+o(1))log₂u という緩い条件でも T,E,C_P=u^{o(1)} が従う。

例えば u≥2²⁰、G≤log₂u では、四分岐を通じて

$$
T^3\mathcal E<1641(\log_2u+10)^2.
\tag{10}
$$

ここでは (6561/4)u/(u−124)<1641 を使った。これは有限個の u を調べた結論ではない。

**系2.2（端に近い j の制限）。** 同じ仮定 u>124 の下で

$$
\boxed{j>\frac{(n-1)(n-2)}{4n}
\left(\frac{T^3\mathcal E}{\mathcal B(u,G)}\right)^{1/3}.}
\tag{11}
$$

実際、(8)から θ>(T³E/B)^(1/3) であり、(4)と n−j<n を使えばよい。特に G≤log₂u+O(1) では j/n≫(log u)^(−2/3)。

## 4. n−1 と n−2 の直接の曲線

9月22日のマスターに報告されていた曲線を、ここで独立に導出する。16|z を満たす正整数 z に対し

$$
E(z):\quad y^2+xy=x^3+\frac z4x^2+\frac z{16}x.
$$

整数係数モデルの不変量は

$$
c_4=z^2-z+1,\quad
c_6=-\frac{(z+1)(2z^2-5z+2)}2,\quad
\Delta=\frac{z^2(z-1)^2}{256}.
\tag{12}
$$

gcd(c₄,z(z−1))=1 である。従って判別式を割る全素数でこのモデルは最小かつ乗法的還元を持ち、導手は rad(z(z−1))。z=n と z=n/2 を取れば

$$
R_T=\operatorname{rad}_5(T),\quad
R_1=\operatorname{rad}_5(TRS),\quad
R_2=\operatorname{rad}_5(TABC),\quad N_i\le6R_i.
$$

Δ(E(z))>z⁴/1024 より、それぞれ log₂Δ>4u−10、log₂Δ>4u−14。(3)と 2/3<log 2<1 を使うと

$$
\boxed{u<\frac92R_1\lceil\log_2(6R_1)\rceil^2+49,\qquad
u<\frac92R_2\lceil\log_2(6R_2)\rceil^2+50.}
\tag{13}
$$

Lᵤ=⌈log₂u⌉+3 と置く。Rᵢ<u なら ⌈log₂(6Rᵢ)⌉≤Lᵤ、Rᵢ≥u なら以下の下界は自明。従って u≥128 で

$$
\boxed{R_1,R_2>\frac{u}{9L_u^2}.}
\tag{14}
$$

これは表の完全性ではなく、(3)と明示モデルの局所計算から得た結果である。

## 5. 補助因子に吸収されない素数の積

次の三つは実際の Kummer ブロックから取った平方自由整数である。

$$
F_A=\prod_{\substack{p\ge5\\p\mid A,\ p\nmid ab}}p,\quad
F_{BC}=\prod_{\substack{p\ge5\\p\mid BC,\ p\nmid P}}p,\quad
F_{RS}=\prod_{\substack{p\ge5\\p\mid RS,\ p\nmid abP}}p,
\quad F_K=F_AF_{BC}F_{RS}.
$$

三つの素数台は互いに素である。F_K は ABC RS を割り abP を割らない p≥5 の積に等しい。従来の R_A=rad₅(A) を用いた積を割り、F_K|R_A F_BC F_RS である。(1)から p≥5 について p|A ⇒ p∤P、p|BC ⇒ p∤ab、また gcd(ab,P) に p は現れない。

**補題3。**

$$
R_1R_2\mid R_T^2\,A_0\operatorname{rad}_5(P)\,F_K,
\qquad
R_1R_2\le R_T^2abP F_K.
\tag{15}
$$

証明：T の素数は左辺に二回現れる。A の素数は ab または F_A へ、BC の素数は P または F_BC へ、RS の素数は abP または F_RS へ割り当てる。六ブロックが互いに素なので、P の同じ素数を RS と BC に二重計上する必要はない。最後に A₀≤ab、rad₅(P)≤P を使う。□

**定理4。** u≥128 なら

$$
\boxed{F_K>
\frac{u^2T^3P}{81\kappa\,2^G R_T^2L_u^4\theta^3}
\ge\frac{16u^2TP}{2187\,2^G L_u^4}.}
\tag{16}
$$

証明：(5)より abP<κ2ᴳθ³/(T³P) なので、(15)から

$$
F_K>\frac{R_1R_2T^3P}{\kappa2^GR_T^2\theta^3}.
$$

(14)、R_T≤T、θ<1、κ≤27/16 を代入する。□

例えば G≤c log₂u+O(1)（c<2 は固定）なら

$$
F_K\gg\frac{u^{2-c}TP}{(\log u)^4}.
\tag{17}
$$

従ってこの領域で F_K=o(u^(2−c)/(log u)⁴) となる無限反例列は存在しない。T=1 や純2冪の cyclotomic 分解を仮定していない点が適用範囲の違いである。

逆に(16)を G の下界として書くと、全ての u≥128 で

$$
G>2\log_2u+\log_2(TP)-\log_2F_K-4\log_2L_u-\log_2(2187/16).
\tag{17a}
$$

例えば F_K が有界な枝では G≥2log₂u−O(log log u) が必要。従来の一様な log₂u−O(log log u) という下限を、この枝で約二倍へ強める。より一般に F_K≤u^β なら G≥(2−β)log₂u−O(log log u) となる。

G=(1+o(1))log₂u なら

$$
\boxed{T,\mathcal E=u^{o(1)},\qquad F_K\ge u^{1-o(1)}TP.}
\tag{18}
$$

このとき P≥u^ε の部分列では F_K≥u^(1+ε−o(1))。一方 P=u^{o(1)} の部分列では、(2)の導手下界から ab≥u^(1−o(1))。高い冪が小さいという(9)と併せ、後者では大きい素数の一乗からなる ab を処理する必要がある。

## 6. ブロック全体の下界も改善する

(14)から rad₅(RS),rad₅(ABC)>u/(9T Lᵤ²)。さらに(8)で E≥1、θ<1 を使うと

$$
\boxed{\operatorname{rad}_5(RS),\operatorname{rad}_5(ABC)
>\frac{u}{9L_u^2}
\left(\frac{u-124}{972\kappa2^G(G+10)^2}\right)^{1/3}.}
\tag{19}
$$

従って G≤c log₂u+O(1)、c<4 の領域で、両ブロックの radical は

$$
\gg\frac{u^{(4-c)/3}}{(\log u)^{8/3}}
$$

と増大しなければならない。T<2^((G+1)/3) だけを使う評価では c<3 までだった条件を、一段広げられる。

## 7. 何がまだ足りないか

必要条件(8),(16)に反する一般の偶数枝は排除できる。しかし、F_K は n に比べればまだ非常に小さくてもよく、その下界だけで矛盾にはならない。特に次は残る。

1. G が log₂u より速く増える領域。冪の重複 E と T の上界も緩くなる。
2. 小さい G でも、ab の大きい一乗素数と F_K の増大を両立させる full-digit 配置。
3. P が大きく、(16)の大きい F_K を供給する配置。
4. 奇数 j の一般枝。

次の直接の課題は、各完全素数冪の carry-free 条件から F_K の上界を作ること、または(16)と両立する素数配置を一様に排除することである。原文で報告された局所平方条件は、共有素数 n≡8 のところで自動的に成立するため、その条件だけではこの課題を満たさない。

研究の入力について一点訂正する。[担当2原文 §3.2](../../sources/source_i3_nonsquare_center_progress_2026-09-22.md)の「少なくとも13個の素因数」は、引用元の結論より強すぎる。既存の曲線表排除が示すのは「**13以上の素因数が少なくとも一つ存在する**」であり、異なる素因数の個数が13以上という意味ではない。本稿ではその誤った個数下界を使っていない。

## 8. 再生と証明の範囲

```text
python -X utf8 scripts/audit_i3_multiplicity_and_fresh_support.py
```

[検算器](../../scripts/audit_i3_multiplicity_and_fresh_support.py)と[保存した結果](../../data/results/verification_i3_multiplicity_and_fresh_support.json)は、18個の記号恒等式、49個の素数指数パターン、17個の素数配置、1,000個の人工的な直接曲線、四分岐の定数を確認する。素数指数を25以上で打ち切った計算が一般証明なのではなく、(7)の指数公式と(15)の素数ごとの割当てが一般証明である。人工的な曲線や配置を元の問題の反例候補とは扱わない。

原本4件は変更していない。9月22日の中心式のうち本稿で証明・検算した式は昇格するが、少数 support 排除、h₅ の modular reduction、全 shifted-pattern 証明書までをこの検算が保証するわけではない。
