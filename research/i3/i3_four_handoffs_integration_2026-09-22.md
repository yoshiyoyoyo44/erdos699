# $i=3$・偶数 $j$：9月22日の四つの進捗メモの統合

[入口](../../README.md) · [現在地](../../docs/STATUS.md) · [読む順序](../../docs/READING_GUIDE.md)

2026-09-22 の四つの引継ぎメモを、2026-09-21 時点の `0d2262f3beb7c5ce0535ce4fe998832d558ad965` を基準に整理した。**Erdős Problem 699 全体も $i=3$ 全体も未解決。** 以下で「新規報告」と書く結果は添付原文からの統合であり、このコミットで全ての長い証明・有限計算・外部入力を独立に再認証したという意味ではない。既存結果の証明は従来のノートを、各新規報告の詳しい議論は対応する原文を参照する。

原文： [全桁 Kummer](../../sources/source_i3_full_digit_kummer_progress_2026-09-22.md)（担当1）、[マスター](../../sources/source_i3_master_progress_2026-09-22.md)、[非平方中心](../../sources/source_i3_nonsquare_center_progress_2026-09-22.md)（担当2）、[二曲線](../../sources/source_i3_two_curves_progress_2026-09-22.md)（担当3）。原文は改訂せず保存した。

**9月23日追記：** [一般偶数枝の続稿](i3_multiplicity_budget_and_fresh_support_2026-09-23.md)で、中心比率と中心ノルムの恒等式、n−1,n−2 の直接曲線を独立に証明・検算し、T と高い冪の同時制約、補助因子の外の素数台の下界を得た。以下の「未監査」は9月22日の取り込み時点の分類であり、更新した範囲は続稿第8節に記載する。担当2原文の「少なくとも13個の素因数」は引用元の誤読で、正しくは「13以上の素因数が少なくとも一つ」である。

## 1. 共通の出発点と記号

偶数 $j$ の仮想反例に対し、既存の正規化では

$$
n=\gamma T2^u,\quad u\ge51,\quad v=v_2(j)\ge1,\quad x=2^v,
\quad G=u-4v\ge14,
$$

$$
(\gamma,\delta_1,\delta_2)\in
\{(1,1,1),(1,1,3),(1,3,1),(3,1,1)\},\quad
\delta=\delta_1\delta_2,\quad c_0=\delta_1^2\delta_2.
$$

六つの互いに素な奇数ブロック $A,B,C,R,S,T$ と奇数補助因子 $a,b,g_0,h_0$ を用い、$P=g_0h_0$ と置く。基本式は

$$
\begin{aligned}
n-1&=\delta_1RS, & (n-2)/2&=\delta_2ABC,\\
j&=TSBxg_0, & n-j&=TRCxh_0,\\
j-1&=RAa, & n-j-1&=SAb,\\
T^2x^2BCP-A^2ab&=\delta_1.
\end{aligned}
$$

既存の $W_*=(\delta BC-Aab)/(Tx^2)>0$ は奇数で、$\gcd(W_*,TABC)=1$、$\gcd(W_*,P)\mid\delta_1\gamma$。中心変数について

$$
B_G=\gamma c_0 2^{G-3},\quad q=TPW_*,\quad
m+T^2PW_*=B_G,
$$

$$
\delta_2Z^2=m\gamma2^{u-1}+q,\qquad
\delta_1TC_{\rm cen}^2=\delta_1\gamma2^{G-2+2v}+(n-1)Z.
$$

ここで $C_{\rm cen}$ はブロック $C$ とは別の奇数である。第一曲線の導手を支配する量と第二曲線の素数台はそれぞれ

$$
\mathcal Q=\operatorname{rad}_{p\ge5}(ab)
\operatorname{rad}_{p\ge5}(\operatorname{cf}_3(P))^2,\qquad
R_F=\operatorname{rad}_{p\ge5}(mTPW_*).
$$

既存の評価は $u\le972\mathcal Q\lceil\log_2(486\mathcal Q)\rceil^2+124$、$G<(9/2)R_F\lceil\log_2(6R_F)\rceil^2+52$。$\delta_2q$ の平方枝は全 $G$ で排除済み。根拠は[二次捻りと Kummer](i3_quadratic_twist_and_kummer_support_2026-09-21.md)、[第二曲線](i3_growing_gap_and_auxiliary_frey_2026-09-21.md)、[平方枝](i3_gap_square_obstructions_2026-09-21.md)。

## 2. 全桁・素数台の報告（担当1）

**新規報告。** $Q_1=RS=(n-1)/\delta_1$, $Q_2=ABC=(n-2)/(2\delta_2)$ とし、$\omega$ を異なる素因数の個数とする。$T=\gamma=1$ の最小配置 $\bigl(\omega(Q_1),\omega(Q_2)\bigr)=(2,3)$ を排除し、$(3,3)$ の $u$ 奇数枝も排除したという報告である。$(3,3)$ の $u$ 偶数枝は $u=2r$（$r$ は奇素数）、$R/S$ は混合分割、各分割からの $j$ の lift は高々2本まで圧縮される。詳しい primitive divisor の数え上げと法 $13,19,73$ の末端排除は[担当1原文 §§4–6](../../sources/source_i3_full_digit_kummer_progress_2026-09-22.md)にある。これらの素数台排除を、この統合だけで独立証明済みと扱わない。

同じ原文は balanced $(2,4)$ 配置を主要残枝として特定する。報告された必要条件は $u=2r+1$ で $u,r$ がともに素数、$D=2^r$、$M=D-1=M_1M_2$、$N=(D+1)/3=N_1N_2$、$ABC=MN$。$M_i,N_i$ は完全素数冪で、$A,B,C$ の二成分ブロックは一つの $M_i$ と一つの $N_j$ を含む。endpoint の再構成を用いた報告上の上界は

$$
(M/72)^{1/3}<M_i<72^{1/3}M^{2/3},\qquad
N_i<18N^{2/3}
$$

である。ただし後者には **$N$ 側の $B$ singleton 例外**が残る。例外の inverse interval、合同式、$2$ 進条件は[担当1原文 §§23–26, 30](../../sources/source_i3_full_digit_kummer_progress_2026-09-22.md)を参照。$(3,3)$ 偶数枝、support 総数7以上の枝も残る。ここでの上界は各因子が消えたという意味ではない。

全桁条件は各完全素数冪 $p^e\parallel T,R,S,A,B,C$ について対応する二項和が底 $p$ で carry-free であるという条件。既存の六ブロック桁和下界に対し、原文は moving prime powers と endpoint の同じ候補から $a,b,P,W_*,m$ を復元し、$\mathcal Q$ と $R_F$ を同時に計算する道筋を示す。一方、原文は **base-$q$ の整合性だけでは full $p$-adic Kummer ではない**、center の平方条件と block の条件を独立と数えてはならない、と訂正している。

## 3. 中心二式からの再構成（担当2）

**新規の代数報告。** $D_c=\delta_1\gamma2^{u-2v-2}$、$Q_2=ABC$ と置くと、中心式をブロックへ戻す次の因数分解を報告する。

$$
D_c+Z=AW_*,\qquad D_c-Z=TBCP,\qquad
D_c^2-Z^2=qQ_2.
$$

$\gcd(W_*,BC)=1$ から $A=\gcd(D_c+Z,Q_2)$ であり、

$$
W_*=(D_c+Z)/A,\quad BC=Q_2/A,\quad
P=A(D_c-Z)/(TQ_2),\quad
ab=\bigl(Tx^2(D_c-Z)-\delta_1\bigr)/A^2.
$$

これは中心候補を単なる平方テストで終わらせず、第一曲線の $\mathcal Q$ と第二曲線の $R_F$ まで戻す手順を与える。別の報告された恒等式は、$H_1=\delta A-2T^2x^2P$, $H_2=\delta A-T^2x^2P$ として

$$
\delta_2mA^2+T^3P^2=\gamma2^{G-3}H_1^2,
\quad
\delta_2qA^2-T^2P^2=\gamma TP2^{u-2v-1}H_2.
$$

従って両辺の正確な $2$ 進付値を使う moving modulus 条件が得られるという報告である。[担当2原文 §§5–11](../../sources/source_i3_nonsquare_center_progress_2026-09-22.md)に導出と素数配置の表がある。

**限定された枝の新規報告。** $T=\gamma=1$、$G$ 偶数では $Q_2=2^{u-1}-1$ の各完全素数冪 $p^e$ に対し $s_p(2Q_2/p^e)\ge6$。$p\bmod24$ によって下界8または14に強まる場合がある。$v\ge3$ の $Q_1$ 側の桁和5は、$2^v-1$ が素数かつ $v\mid G$ となる Mersenne 例外へ絞られるという報告で、例外の cyclotomic 因子は残る。これは $T=\gamma=1$、$G$ 偶数という仮定の下の結論であり、全枝の最小桁和ではない。[担当2原文 §§17–26](../../sources/source_i3_nonsquare_center_progress_2026-09-22.md)を参照。有限剰余類リストと初期の square-root split は独立再監査前に定理として転用しない。

## 4. 二曲線を結ぶ量（担当3）

**新規の代数報告。** $e_c=\delta A-2T^2x^2P$ とし、$\lambda=e_c/(\delta A)$、$t=m/B_G$ と置く。$0<\lambda<1$ で

$$
\lambda=1-\frac{4j(n-j)}{(n-1)(n-2)}
=\frac{(n-2j)^2-3n+2}{(n-1)(n-2)},
$$

最初の等号は $j(n-j)=T^2x^2RSBCP$ と $(n-1)(n-2)=2\delta A RSBC$ の代入で直接確認できる。二番目の等号は $(n-2j)^2=n^2-4j(n-j)$ である。

$$
t=\lambda^2-\frac{2(1-\lambda)^2}{n},
\qquad
abP^2=\frac{\kappa2^G}{T^3}(1-\lambda)^2
\frac{(n-2)(1-\lambda)-4}{n},\quad
\kappa=\frac{\gamma\delta_1^3\delta_2^2}{16}.
$$

従って $\mathcal Q\le abP^2<(\kappa2^G/T^3)(1-\sqrt t)^3$ という、第一曲線の導手量と第二曲線の中心分割の量的な橋を報告する。これは両者の一様上界を得たという主張ではない。導出・適用の範囲は[担当3原文 §§4–9](../../sources/source_i3_two_curves_progress_2026-09-22.md)。

別の正の恒等式

$$
T^2x^4q-c_0=Aab(\delta A-T^2x^2P)
$$

この式は $q=TPW_*$、$Tx^2W_*=\delta BC-Aab$ と行列式 $T^2x^2BCP=A^2ab+\delta_1$ を順に代入すると確認できる。

ここから、$p^e\mid ab$、$p\ge5$ なら $\delta_2q$ は法 $p^e$ で平方。また $p\mid ab$ が第二曲線の素数台にも入るなら $p\mid m$、かつ $n\equiv8\pmod p$。第一・第二曲線の共有素数は、$P$ 経由と $ab$–$m$ 経由に分かれ、後者の endpoint 条件が可視化される。原文は

$$
\gcd(\mathcal Q,R_F)=
\operatorname{rad}_{p\ge5}(\operatorname{cf}_3(P))\,
\gcd\bigl(\operatorname{rad}_{p\ge5}(ab),n-8\bigr)
$$

も主張する。これは局所平方条件が共有素数を即座に排除するという主張ではなく、むしろそこで中心の平方条件が自動化する障害を示す。[担当3原文 §§13–18](../../sources/source_i3_two_curves_progress_2026-09-22.md)参照。

**外部入力と別途監査が必要な報告。** 第二曲線の指数の最大公約数 $h_5$、3-free residual level $L_3$、mod $3,7,\ell$ 表現、pure septic unit descent による枝の排除は[担当3原文 §§20–30](../../sources/source_i3_two_curves_progress_2026-09-22.md)の研究成果として保存した。原文は $2,3,5,7\nmid h_5$、$h_5>1$ の素因数は $11$ 以上かつ法4で3、と結論するが、この統合では modularity、数体の unit 情報、局所計算を独立再検証していないため、既存の確立済み範囲を更新する根拠にはまだ用いない。$h_5=1$ の一般枝は原文でも残る。

## 5. マスターメモから追加された経路

[マスター原文 §§14–22](../../sources/source_i3_master_progress_2026-09-22.md)は、$BC,W_*$ の fresh support、$A/BC/RS$ の Kummer ブロック、$u-G=4v$ を測る補曲線、桁遷移の shifted lemma、有限 lifting ladder を結ぶ。特に $T$ 用の shift-free 議論を $R,S,A,B,C$ に転用しない訂正が重要である。$L_{1000}$ に関する大きな桁和障壁は、保存された全 shifted-pattern 証明書とその再生器がこのリポジトリにまだないため、ここでは「原文報告」として扱う。$L_H\mid\operatorname{lcm}(1,\ldots,H+2)$ という一般形も原文の導出と適用条件を確認してから再利用する。

担当3「二曲線」原文の第2節にある「$\alpha,\beta,\chi$ は奇数」という記述は誤記である。$d=\gcd(m,T^2PW_*)$ は奇数なので $\alpha=m/d$, $\beta=T^2PW_*/d$ は奇数だが、$\chi=\alpha+\beta=3^r2^{G-3}$ は偶数である。この訂正は第二曲線の既存の式とも一致する。初版の統合ノートでは、この誤記の所在をマスター原文と取り違えていたため訂正した。

## 6. 今回の統合で維持する境界

| 対象 | 現在の扱い |
|---|---|
| $i=3$ 全体と問題699全体 | 未解決 |
| 9月21日までの正規化、二曲線評価、平方枝排除 | 既存ノートと検算器に依拠 |
| 9月22日の中心因数分解、$\lambda$、共有素数の式 | 原文に導出がある新規代数結果。統合時の全式の独立監査は未完 |
| 担当1の少数 support 排除と cubic balance | 原文の証明報告。素数台分類と末端合同計算の独立再生が必要 |
| 担当2の純2冪・偶数 $G$ の低桁排除 | 仮定付きの原文報告。有限剰余類計算の再監査が必要 |
| 担当3の $h_5$ と residual level | 外部定理・数体計算に依存する原文報告。現状の主定理に組み込まない |
| マスターの有限 lifting ladder | 証明書未移植。数値下界を確立済みとは表示しない |

原文が明示的に撤回した旧 Pell 付値予想、mod $23$ だけによる指数 gcd の排除、誤った $abP^2$ 上界、中心平方条件の二重計上は使用しない。固定 $G$ の有効有限性を $G$ 全体の有限性へ拡張しない。

## 7. 次の検証と研究の順序

1. 担当1の $(2,3)$、$(3,3)$ 奇数枝、balanced $(2,4)$ の endpoint 排除を、各末端合同式と完全素数冪分割まで独立に再生する。残る $N$ 側 $B$ singleton 例外を先に調べる。
2. 担当2の中心再構成と $T=\gamma=1$、偶数 $G$ の桁和4排除を、全シフトの Kummer 条件まで監査する。Mersenne 例外は未排除のまま保持する。
3. 担当3の $\lambda$ と共有素数の代数を既存のブロック系から形式的に再導出し、$h_5$ の主張は外部出典・局所条件・unit descent の証明書を別に点検する。
4. 第一曲線の $\mathcal Q$ と第二曲線の $R_F$ が共に速く増える枝を、中心復元と full-digit 条件の同じ候補で制限する。巨大な radical 自体は矛盾ではなく、一様上界または衝突する桁条件が必要である。
