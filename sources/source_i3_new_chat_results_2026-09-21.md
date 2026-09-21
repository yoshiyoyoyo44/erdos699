# Erdős Problem 699 — i=3 新規チャット成果まとめ

日付: 2026-09-21
対象: `yoshiyoyoyo44/erdos699`
基準: GitHub 最新確認コミット `71df9d56e3acd8fcddd88aa54e065e4cb7ac85d8`

## この文書の範囲

この文書には、上記GitHubコミットまでに**既にリポジトリへ載っている成果は原則として再録しない**。
この会話中に新しく導出し、既存のリポジトリ上の恒等式・不等式へ戻って再監査できた結果のみを記録する。
未証明の研究方針・次に試すこと・有限探索の提案は含めない。

以下では偶数 `j` の反例を仮定し、既存記号

\[
n=\gamma T2^u,\qquad v=v_2(j),\qquad x=2^v,\qquad G=u-4v,
\]

\[
g=xg_0,\qquad h=xh_0,\qquad P=g_0h_0,
\]

\[
Q=(n/2-1)/\delta_2=ABC,\qquad c_0=\delta_1^2\delta_2,
\]

および既存の全桁Kummer量

\[
W_*=\frac{\delta BC-Aab}{Tx^2}>0
\]

を用いる。

---

## 1. exact-gap の商 `q` と全桁Kummer量 `W_*` の正確な同定

既存の exact-gap 側では

\[
B_G=\gamma c_0 2^{G-3},\qquad
q=\frac{B_G-m}{T}>0,
\]

\[
\delta_2 Z_0^2=m\gamma2^{G-1}x^4+q
\]

が成立する。

一方、既存のKummer側には

\[
AW_*+TBCP=\delta_1\gamma2^{u-2v-1}
\]

がある。

これらを同じ中心変数へ戻して比較すると、exact-gap の補助商は独立な新変数ではなく

\[
\boxed{q=TPW_*=Tg_0h_0W_*}
\tag{1}
\]

と完全に一致する。

したがって

\[
\boxed{B_G-m=T^2g_0h_0W_*}
\tag{2}
\]

および

\[
\boxed{m+T^2g_0h_0W_*=\gamma c_0 2^{G-3}}
\tag{3}
\]

を得る。

特に既存の `T | B_G-m` は

\[
\boxed{T^2\mid B_G-m}
\tag{4}
\]

へ強化される。

### 独立再監査

中心の式を直接展開すると

\[
c_0(n+2)-2w=8T^3x^4g_0h_0W_*.
\]

一方、`q=(B_G-m)/T` の定義から同じ左辺は

\[
8T^2x^4q
\]

となるため、再び `(1)` が得られる。

---

## 2. `m` と `q` の大きい素数台は分離する

既存の exact-gap 条件により

\[
\gcd(m,T)=1,
\]

かつ

\[
Tq=B_G-m.
\]

したがって、任意の `d | gcd(m,q)` は `B_G` も割る。`m` は奇数なので `d` は2を含まず、

\[
B_G=\gamma c_0 2^{G-3}
\]

から

\[
\boxed{\gcd(m,q)\mid \gamma c_0.}
\tag{5}
\]

従って、5以上の素数について `m` と `q` の素数台は完全に互いに素である。

式 `(3)` はこの意味で、右辺が2の冪と3の例外因子だけからなる二項和へ正規化された形になっている。

---

## 3. `g_0h_0` の一様上界

既存のサイズ条件

\[
\delta A>2T^2x^2P
\]

と、`A`-block に対する一般上界

\[
4(n-1)A^2\le \delta_1(n-2)^2
\]

を直接合成する。

まず

\[
A>\frac{2T^2x^2P}{\delta}
\]

なので

\[
\frac{4T^4x^4P^2}{\delta^2}<A^2
\le \frac{\delta_1(n-2)^2}{4(n-1)}.
\]

従って

\[
P^2<
\frac{\delta_1^3\delta_2^2(n-2)^2}
{16T^4x^4(n-1)}.
\]

`n=\gamma T2^{G+4v}` を代入すると

\[
\boxed{
(g_0h_0)^2<
\frac{\delta_1^3\delta_2^2\gamma}{16}
\frac{(n-2)^2}{n(n-1)}
\frac{2^G}{T^3}
}
\tag{6}
\]

特に

\[
\boxed{
(g_0h_0)^2<
\frac{\delta_1^3\delta_2^2\gamma}{16}
\frac{2^G}{T^3}
}.
\tag{7}
\]

主枝 `(\gamma,\delta_1,\delta_2)=(1,1,1)` では

\[
\boxed{4g_0h_0<\sqrt{2^G/T^3}}.
\tag{8}
\]

これは、3乗因子として楕円曲線の導手から消え得る `g_0h_0` 自体の大きさにも一様な制限を与える。

---

## 4. `W_*` の一様下界

既存の

\[
W_*>rac{\delta BC}{2Tx^2}
\]

と

\[
BC=\frac{n-2}{2\delta_2A}
\]

から

\[
W_*>rac{\delta_1(n-2)}{4TAx^2}.
\]

再び

\[
4(n-1)A^2\le\delta_1(n-2)^2
\]

を用いると

\[
A\le\frac{\sqrt{\delta_1}(n-2)}{2\sqrt{n-1}},
\]

よって

\[
\boxed{
W_*>
\frac{\sqrt{\delta_1(n-1)}}{2Tx^2}
}.
\tag{9}
\]

平方して `n=\gamma T2^{G+4v}` を入れると

\[
\boxed{
W_*^2>
\frac{\delta_1\gamma}{4T}
\left(1-\frac1n\right)2^G
}.
\tag{10}
\]

したがって `G` が増大する反例列では `W_*` 自体も少なくとも概ね `2^{G/2}/\sqrt T` の速度で増大する必要がある。

---

## 5. `W_*` の5以上の素因数は既存の判別式因子と分離する

既存の

\[
\delta BC-Aab=Tx^2W_*
\]

を `p\ge5`, `p|W_*` で見る。

既存の `gcd(W_*,TABC)=1` と `gcd(W_*,g_0h_0)|\delta_1\gamma` により

\[
p\nmid TABCg_0h_0.
\]

さらに

\[
\delta BC\equiv Aab\pmod p.
\]

左辺は非零なので `p\nmid ab` も従う。

従って

\[
\boxed{
\gcd_{\ge5}(W_*,\,ab\,g_0h_0\,TABC)=1
}
\tag{11}
\]

という意味で、`W_*` の5以上の素数台は、既存の三次判別式

\[
\Delta\propto ab(g_0h_0)^2
\]

に現れる補助因子の素数台から分離している。

---

## 6. `W_*` の素因数に対する一様な平方剰余条件

既存の正確式

\[
W_*=rac{aBg_0+bCh_0}{2^{v+1}}
\]

に対し

\[
U=aBg_0,\qquad V=bCh_0
\]

と置くと

\[
U+V=2^{v+1}W_*,
\qquad
UV=abBCg_0h_0.
\tag{12}
\]

### 奇素数 `p | W_*`

`p\ge5`, `p|W_*` なら `(11)` により `p\nmid UV` であり

\[
U\equiv -V\pmod p.
\]

従って

\[
(U-V)^2\equiv-4UV\pmod p.
\]

一方

\[
\delta BC\equiv Aab\pmod p
\]

なので、整理すると

\[
\boxed{
\left(\frac{-\delta A g_0h_0}{p}\right)=1
\qquad(p\ge5,\ p\mid W_*)
}.
\tag{13}
\]

すなわち `W_*` の全ての5以上の素因数は、同一の二次剰余条件を満たす。

### 2進版

`U+V=2^{v+1}W_*` から

\[
U\equiv -V\pmod{2^{v+1}}.
\]

また `Tx^2W_*` は `2^{v+1}` で0なので

\[
\delta BC\equiv Aab\pmod{2^{v+1}}.
\]

これらを `UV=abBCg_0h_0` に代入すると

\[
\boxed{
-\delta A g_0h_0
\text{ は }2^{v+1}\text{ を法として平方}
}.
\tag{14}
\]

特に `v\ge2` では奇数平方は mod 8 で1なので

\[
\boxed{
\delta A g_0h_0\equiv-1\pmod8
}.
\tag{15}
\]

---

## 7. endpoint 側の2進付値の強化

既存の中心・endpoint 変数

\[
\rho=\frac{j(j-1)}{2Q_1},
\qquad
\lambda=\frac{\rho(\rho-\delta_1)}Q
\]

を用いる。

偶数 `j` で `v=v_2(j)\ge2` のとき、`Q_1,Q` は奇数で `j-1` も奇数なので

\[
v_2(\rho)=v-1.
\]

このとき `\rho` は偶数、`\delta_1` は奇数だから `\rho-\delta_1` は奇数。従って

\[
\boxed{v_2(\lambda)=v-1.}
\tag{16}
\]

さらにKummer因子分解を代入すると

\[
\rho=TABa\,2^{v-1}g_0,
\]

よって整数性と互いに素性から

\[
\boxed{T2^{v-1}ag_0\mid\lambda.}
\tag{17}
\]

対称に `y=n-j` に対して

\[
\rho_y=\frac{y(y-1)}{2Q_1},
\qquad
\lambda_y=\frac{\rho_y(\rho_y-\delta_1)}Q
\]

と置けば

\[
\boxed{v_2(\lambda_y)=v-1,}
\tag{18}
\]

\[
\boxed{T2^{v-1}bh_0\mid\lambda_y.}
\tag{19}
\]

従って、従来の片側endpointだけでなく `ag_0` と `bh_0` の両側が2つのendpoint量へ強制的に現れる。

---

## 8. gap 方程式の S-unit 形

式 `(3)` を

\[
X=\frac{m}{\gamma c_0 2^{G-3}},
\qquad
Y=\frac{T^2g_0h_0W_*}{\gamma c_0 2^{G-3}}
\]

と正規化すると

\[
\boxed{X+Y=1.}
\tag{20}
\]

また `(5)` により、5以上の素数について2項の素数台は互いに素である。

これは exact-gap 系を、右辺が2と3の例外因子だけからなる明示的な S-unit 型方程式として扱えることを示す構造的帰結である。

---

## 9. 今回の成果の依存関係

この文書の主結果は、すべて既存リポジトリで既に証明されている次の入力から代数的に導いた。

- exact-gap の `B_G,m,q,Z_0` 系
- 六ブロック Kummer 因子分解
- `W_*` の正確な定義と Mersenne 型和恒等式
- `A`-block の一般上界
- `\delta A>2T^2x^2g_0h_0`
- 各ブロックと補助因子の互いに素性

この文書自体は Problem 699、または `i=3` の完全解決を主張しない。
