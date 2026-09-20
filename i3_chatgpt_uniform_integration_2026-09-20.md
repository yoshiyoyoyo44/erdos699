# ChatGPT回答の統合：変換の範囲、Dの局所構造、共通因子

2026-09-20。**i=3全体も問題699全体も未解決。**
ChatGPT「GitHubの続きを進める」の研究回答を、広い再探索をせず統合した。
[取得した回答本文](source_chatgpt_uniform_response_2026-09-20.md)を別ファイルに保存した。
保存ファイルのSHA-256は `526419a0f67b6831fd4246be5bd2b21b878b8cd5d52f3fb7346c09c57142862a`。
回答の基準は8072705、本統合直前のHEADは89dbe20。

以下は回答に示された証明を既存の記号へ接続したもの。
指数の減少とnの減少を区別し、共通因子の小素数の例外を明示する。
個々の因子の平方剰余条件は素数冪を含む法全体に強められる。

## 1. 共通の記号

[混合した差の稿](i3_mixed_parameter_bound_2026-09-20.md)に従い、

\[
n=\gamma T2^u=TH,\quad j=Tk,\quad v=v_2(j),\quad
Q_1=(n-1)/\delta_1=RS,\quad Q=(n-2)/(2\delta_2)=ABC,
\]
\[
Z=\frac{(n-2j)^2-n}{2Q_1},\quad
\rho=\frac{j(j-1)}{2Q_1},\quad R_0=2\rho-\delta_1,
\]
\[
Z^2=\delta_1^2+wQ,\quad \rho(\rho-\delta_1)=\lambda Q,
\quad D=w-4\lambda,\quad c_0=\delta_1^2\delta_2.
\]

u≥49、Z>0、T∣Z、v₂(Z)=2v+1 は既存の結果。
最後の付値は[exact-gap稿・第2節](i3_exact_gap_and_g9_continuation.md)にある。

## 2. 変換後の添字は確かに範囲内に入る

既存の g=2^v g₀、h=2^v h₀ を用いて

\[
N=\delta_1\gamma2^{u-1-2v},\qquad J=BCTg_0h_0
\]

と置く。元の変数では

\[
N=\frac{\delta_1n}{T2^{2v+1}},\qquad
J=\frac{\delta_1j(n-j)}{T2^{2v}(n-1)}.
\]

代入すると

\[
\boxed{N-2J=\frac{Z}{T2^{2v}}.}
\tag{1}
\]

従って N−2J は正で、その2進付値は1。
g₀,h₀,B,C,T は正の奇数、B,C≥11 より

\[
\boxed{J\text{ は奇数},\quad121\le J<N/2,\quad
N/2-J\text{ は正の奇数}.}
\tag{2}
\]

N の奇数部分はδ₁γ∈{1,3}なので、変換後の正規化ではT′=1。
U=u−1−2v はuより小さい。u≥49 と u≥4v+14（v=0でも自明に成立）から U≥31。
従って変換後の奇数部分M′∈{1,3}には (M′)³<2^(U−2) も成立する。

**補足：n自体が必ず小さくなるわけではない。**
N/n=δ₁/(T2^(2v+1)) なので、(δ₁,T,v)=(3,1,0) では N=3n/2。
他の枝ではN<n。減少する量として保証されるのは指数uである。

この結果で[添付統合稿](i3_handoff_uniform_integration_2026-09-20.md)に残していた
添字の範囲の確認は完了する。しかし変換後の

\[
Q'_1\mid J(J-1),\qquad Q'_2\mid J(J-1)(J-2)
\]

と全桁Kummer条件の保存は、一般には未証明。
T=δ₁=1、v=0で第一条件が保存される既存の特殊ケースは引き続き有効である。
**今回の写像を反例から反例への降下と呼ぶことはできない。**

## 3. D−c₀のTで割った商を決定する

E=(D−c₀)/T と置くと

\[
\boxed{E\equiv\frac{c_0}{2}(H-4k)\pmod T.}
\tag{3}
\]

ここで1/2は奇数の法Tでの逆元を表す。
証明は Z=Tz、ρ=Tr、Q=(TH/2−1)/δ₂ を
DQ=Z²−(2ρ−δ₁)² に代入し、mod T²で比較する。
r≡δ₁k/2 (mod T) を使えば (3) が得られる。

gcd(T,2c₀)=1 より

\[
\boxed{\gcd\left(T,\frac{D-c_0}{T}\right)=\gcd(T,4k-H).}
\tag{4}
\]

同じ展開から

\[
\frac{w-c_0}{T}\equiv\frac{c_0H}{2},\qquad
\frac{\lambda}{T}\equiv\frac{c_0k}{2}\pmod T.
\tag{5}
\]

従ってw−c₀でのTの単約数性は既存の結果どおり常に成立する。
D−c₀については gcd(T,4k−H)=1 の場合にちょうど成立する。
各p^e∥Tに対して、(4) は商の付値をeで打ち切った値を決定するのであり、
v_p(4k−H)≥e の場合にそれより上の付値まで決定する主張ではない。

## 4. Dの二因子の共通部分

d=Z−R₀、s₊=Z+R₀ と書き、既存の分解

\[
d=AC\ell,\qquad s_+=Bm,\qquad D=\ell m
\]

を使う。ℓは0でない奇数、mは正の奇数。ブロック上の剰余から
gcd(ℓ,B)=gcd(m,AC)=1 が従うので

\[
G:=\gcd(|\ell|,m)=\gcd(|d|,s_+).
\]

直接計算により

\[
\boxed{s_+-3d=\delta_1(4j-n-4).}
\tag{6}
\]

G₀=G/gcd(G,δ₁) とすると4j≡n+4 (mod G₀)。
また

\[
2Q_1d=P_-:=2j^2-4jn+2j+n^2+n-2.
\]

従ってG₀∣P₋。上記の一次合同式を8P₋へ代入すれば

\[
\boxed{G_0\mid F(n):=n^2-12n+16=(n-6)^2-20,\qquad G^2\mid D.}
\tag{7}
\]

p∣G、p∤5δ₁ なら pは奇数で、(5/p)=1、すなわち p≡±1 (mod 5) が必要。

**統合時の補足。** 小さい素数の重複度と、元のブロックとの共通部分も決まる。

\[
\boxed{v_3(G)\le v_3(\delta_1)\le1,\quad v_5(G)\le1,\quad
\gcd(G,TQ)=1,\quad\gcd(G,Q_1)\mid5.}
\tag{8}
\]

F(n)≡n²+1 (mod 3) は0にならないので、最初の主張が従う。
5∣F(n)なら n−6は5の倍数で、F(n)=(n−6)²−20の5進付値はちょうど1。
Qとの互いに素性は先の二つのgcd条件から従い、Tとの互いに素性はD≡c₀ (mod T)から従う。
最後にF(n)≡5 (mod Q₁)、gcd(δ₁,Q₁)=1を使えばgcd(G,Q₁)∣5。

## 5. 個々の因子の平方剰余条件を法全体に拡張

\[
P_+:=2Q_1s_+=6j^2-4jn-2j+n^2-3n+2
\]

と置く。平方完成により

\[
(2j-2n+1)^2=(2n^2-6n+5)+2P_-,
\]
\[
(6j-2n-1)^2=-(2n^2-22n+11)+6P_+.
\]

従って素数だけでなく、素数冪を含む法全体で

\[
\boxed{2n^2-6n+5\text{ は法 }|\ell|\text{ で平方},}
\tag{9}
\]
\[
\boxed{-(2n^2-22n+11)\text{ は法 }m\text{ で平方}.}
\tag{10}
\]

平方には0を含む。法が1のときは条件は自明。
回答の素数ごとの条件を、そのまま各完全素数冪にも適用できる形にした。

## 6. C側の対称な上限

[B側の証明](i3_mixed_parameter_bound_2026-09-20.md)でjをn−jに置き換えると

\[
L_C=\frac{\delta_1(n-j)(2n-j-2)}{(n-1)C^2}\in\mathbb Z_{>0},
\quad\chi_vT\mid L_C.
\]

従って

\[
\boxed{C^2\le\frac{\delta_1(n-j)(2n-j-2)}{\chi_vT(n-1)}.}
\tag{11}
\]

ここでχᵥ=1 (v=0)、8 (v=1)、2^(v+1) (v≥2)。
証明にはv₂(n−j)=vを使う。元のj≤n/2は、商の整数性と付値の議論には不要である。

## 7. 確認範囲と残る核心

```
python -X utf8 audit_i3_chatgpt_uniform_integration.py
```

[短い記号検算](audit_i3_chatgpt_uniform_integration.py)と
[結果](verification_i3_chatgpt_uniform_integration.json)を付属した。
広い係数探索、過去の整数点計算、添付全体の再監査は実施していない。

これらは既存の反例の代数条件から導く全指数の必要条件であり、
新たに全桁Kummer条件の保存や一様なDの上限を証明したものではない。
またGが小さい場合、|ℓ/G|とm/Gの**両方**が大きくなるとは限らず、一方だけが増える場合も残る。
回答末尾の二分を使う際は、この場合を落としてはいけない。
