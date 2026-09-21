# チャット原文：判別式降下研究

取得日：2026-09-21
チャットID：6ab01718-f9a0-83e8-8734-d83dc7676c07
参照：https://chatgpt.com/c/6ab01718-f9a0-83e8-8734-d83dc7676c07

以下は取得できたAI回答の原文を古い順に保存したもの。未検証の主張と後続回答による訂正を含む。


## 回答 6cfb3739-92d4-4ef3-a69e-a80545bbc61f

かなり有望です。結論を先に言うと、**三次形式の判別式降下は「反例→反例」の降下としては保存に失敗するものの、判別式を一様な終端型まで落とし、その終端形式に純 \(2\)-冪の Thue–Mahler 型整数点を保存することで、一様有限化への明確な橋を作れます。** さらに監査すると、奇数 \(j\) について既存の \(284M^3<2^u\) をかなり細分化できます。

## 1. 判別式降下は必ず有限回で標準終端に着く

奇数 \(j\) では

\[
\nu_2(\Disc f)=w+1,\qquad
w=\max\{\nu_2(j-1),\nu_2(y-1)\}\ge2.
\]

1回の降下で判別式の2進付値がちょうど2減るので、最大

\[
\boxed{t=\left\lfloor\frac{w-1}{2}\right\rfloor}
\]

回降下できます。

したがって終端形式 \(f_t\) は

\[
\nu_2(\Disc f_t)=
\begin{cases}
2,&w\text{ odd},\\[2mm]
3,&w\text{ even}.
\end{cases}
\]

ここまでは完全に一様です。\(w\) がいくら大きくても、判別式の2進的複雑さは最終的に **2または3** の二型しか残りません。

さらに各段階は単なる形式的変形ではありません。正規化後

\[
f=aX^3+bX^2Y+cXY^2+dY^3,\qquad
2\mid a,c,d,\quad b\text{ odd},\quad4\mid c,d
\]

とすると、\(\theta\) を \(f(X,1)\) の根として対応する order を

\[
R=\mathbf Z[1,a\theta,a\theta^2+b\theta]
\]

と書けます。降下後は根が \(\theta/2\) なので、

\[
R^*=
\mathbf Z\left[1,a\theta,\frac{a\theta^2+b\theta}{2}\right].
\]

従って

\[
\boxed{R\subset R^*,\qquad [R^*:R]=2,\qquad
\Disc(R^*)=\Disc(R)/4.}
\]

つまりこの判別式降下は、数体を変える操作ではなく、**同じ全実三次数体の中で2進的に index \(2\) の overorder へ上がっていく操作**と解釈できます。これはかなり強い構造です。

---

## 2. 終端判別式は実は \(148,568\) より強く絞れる

終端でも法2では「単根＋二重根」が保存されます。最後に \(\mathrm{GL}_2(\mathbf Z)\) で

\[
f_t(X,Y)\equiv X^2Y\pmod2
\]

と取れます。

対応する order \(R_t\) では、適当な基底 \(1,\omega,\eta\) に対して

\[
\omega^2=\omega,\qquad
\omega\eta=0,\qquad
\eta^2=0
\pmod2.
\]

従って

\[
\boxed{
R_t/2R_t\simeq
\mathbf F_2\times\mathbf F_2[\varepsilon]/(\varepsilon^2)
}
\tag{A}
\]

であり、特に非自明な冪等元を持ちます。

これを小判別式の全実三次数体と照合すると面白いことが起きます。全実三次数体の小さい判別式は

\[
49,81,148,169,229,257,316,\ldots,568,\ldots
\]

という順です。:chatgpt-content-reference{index="0"}

### \(w\) が奇数の場合

終端では \(\nu_2(\Disc R_t)=2\)。

一見、最小候補は

\[
148=4\cdot37
\]

です。しかし判別式148の数体は

\[
x^3-x^2-3x+1
\]

で生成され、mod \(2\) では

\[
x^3+x^2+x+1=(x+1)^3.
\]

したがって

\[
\mathcal O_L/2\mathcal O_L
\simeq\mathbf F_2[\varepsilon]/(\varepsilon^3)
\]

は局所環です。これは (A) の非自明な冪等元を持つ型とは両立しません。:chatgpt-content-reference{index="1"}

もう一つ注意すべき候補は

\[
49\cdot2^2=196,
\]

すなわち判別式49の体の index \(2\) suborder です。しかし判別式49の最小全実三次数体は

\[
x^3-x^2-2x+1
\]

で、mod \(2\) は

\[
x^3+x^2+1
\]

となり \(\mathbf F_2\) 上既約です。よって \(2\) は inert で

\[
\mathcal O_L/2\mathcal O_L\simeq\mathbf F_8.
\]

もし index \(2\) suborder \(R\) があれば

\[
2\mathcal O_L\subset R\subset\mathcal O_L
\]

なので \(R/2\mathcal O_L\) は \(\mathbf F_8\) の4元部分環になります。有限体の部分環は体なので \(\mathbf F_4\) でなければなりませんが、\(\mathbf F_8\) は \(\mathbf F_4\) を部分体に持ちません。したがってこの場合も不可能です。判別式49が全実三次数体の最小値であることも LMFDB で確認できます。:chatgpt-content-reference{index="2"}

次の適合候補が

\[
\boxed{316=4\cdot79}.
\]

実際、判別式316の体は

\[
x^3-x^2-4x+2
\]

で、mod \(2\) は

\[
x^2(x+1),
\]

まさに単根＋二重根型です。:chatgpt-content-reference{index="3"}

したがって、外部の小判別式分類を使えば

\[
\boxed{w\text{ odd}\quad\Longrightarrow\quad
\Disc(f_t)\ge316.}
\tag{1}
\]

GitHub の未確認稿にある \(148=4\cdot37\) は、**法2型を入れると 316 まで改善できます。**

### \(w\) が偶数の場合

終端では \(\nu_2(\Disc f_t)=3\)。

整数の数体判別式は \(0\) または \(1\bmod4\) なので2進付値1はありません。したがってこの場合、対応する三次数体自身の判別式の2進付値が3でなければなりません。

最初の全実三次数体は

\[
\boxed{568=8\cdot71}.
\]

その定義多項式

\[
x^3-x^2-6x-2
\]

も mod \(2\) で \(x^2(x+1)\) となるので型も適合します。:chatgpt-content-reference{index="4"}

従って

\[
\boxed{w\text{ even}\quad\Longrightarrow\quad
\Disc(f_t)\ge568.}
\tag{2}
\]

こちらは定数71がそのまま残ります。

---

## 3. 新しい奇数 \(j\) の一様必要条件

奇数 \(j\) なので \(K=M\)。既存の厳密な判別式上界は

\[
\Disc(f)<\frac{2n}{M^4}
=\frac{2^{u+1}}{M^3}.
\tag{3}
\]

### \(w\) 奇数

このとき \(4^t=2^{w-1}\)。よって

\[
316
\le\frac{\Disc(f)}{2^{w-1}}
<
\frac{2^{u-w+2}}{M^3}.
\]

整理すると

\[
\boxed{
79\,2^wM^3<2^u
\qquad(w\ {\rm odd}).
}
\tag{4}
\]

### \(w\) 偶数

今度は \(4^t=2^{w-2}\) なので

\[
568
<
\frac{2^{u-w+3}}{M^3},
\]

すなわち

\[
\boxed{
71\,2^wM^3<2^u
\qquad(w\ {\rm even}).
}
\tag{5}
\]

これはかなりきれいです。

特に \(w\ge2\) だから、偶数枝の最小 \(w=2\) で

\[
71\cdot4M^3=284M^3<2^u,
\]

となり、あなたが引き継いでいる

\[
284M^3<2^u
\]

をちょうど回収します。一方、例えば

\[
w=3:\quad632M^3<2^u,
\]

\[
w=4:\quad1136M^3<2^u,
\]

と急速に強くなります。

したがって **284 は判別式降下を parity 情報を潰して一様化した最弱ケース**と解釈できます。

---

## 4. 一様有限化への本当の接続点

ここが重要です。次を置きます。

\[
\mathcal R:=\frac{2^{u-w}}{M^3}.
\]

降下後の終端判別式は、

\[
\boxed{
316\le\Disc(f_t)<4\mathcal R
\qquad(w\text{ odd}),
}
\tag{6}
\]

\[
\boxed{
568\le\Disc(f_t)<8\mathcal R
\qquad(w\text{ even}).
}
\tag{7}
\]

したがって、**全桁 Kummer 条件など別の議論から**

\[
\boxed{\mathcal R\le B}
\tag{8}
\]

という絶対定数 \(B\) が一度でも出れば、終端判別式は絶対有界になります。

すると判別式が有界な整数三次形式は \(\mathrm{GL}_2(\mathbf Z)\) 同値を除いて有限個です。したがって終端形式 \(f_t\) 自体が有限個に落ちます。

ここまではかなり直接的な一様有限化です。

ただし現在の

\[
284M^3<2^u
\]

や (4),(5) は

\[
\mathcal R>71\ \text{or}\ 79
\]

という**下界**しか与えません。したがって判別式降下だけではまだ有限化は閉じません。

---

## 5. ただし \(P(1)=2^u\) は「別の形」で保存できる

ここが今回の保存監査で一番使えそうな点です。

各降下をまとめると、整数行列 \(A_t\) が存在して

\[
\boxed{
4^t f_t(\mathbf x)=f(A_t\mathbf x),
\qquad |\det A_t|=2^t.
}
\tag{9}
\]

元の特別点を

\[
s=(1,1),\qquad f(s)=P(1)=2^u
\]

とします。

直接 \(A_t^{-1}s\) を取ると半整数になってしまいます。これは後述の通り避けられない障害です。

しかし

\[
x_t=\operatorname{adj}(A_t)s\in\mathbf Z^2
\]

とすると

\[
A_tx_t=(\det A_t)s=\pm2^ts.
\]

三次斉次性より

\[
4^t f_t(x_t)
=f(\pm2^ts)
=\pm2^{3t+u},
\]

したがって

\[
\boxed{f_t(x_t)=\pm2^{u+t}.}
\tag{10}
\]

しかも \(x_t\) の二座標の最大公約数には奇素因数がありません。実際、奇素数 \(p\) が両座標を割れば

\[
p\mid A_tx_t=(\det A_t)s
\]

となり、\(p\mid2^t\) という矛盾です。

従って

\[
x_t=2^r z_t,\qquad \gcd(z_{t,1},z_{t,2})=1
\]

と書けて

\[
\boxed{
f_t(z_t)=\pm2^E,\qquad
E=u+t-3r.
}
\tag{11}
\]

つまり終端形式は必ず **原始的な pure-\(2\) Thue–Mahler 解**を持ちます。

さらに \(P'(1)\) が奇数という条件も完全には失われません。

\[
\nabla f(1,1)
\]

の第一成分は \(P'(1)\) なので2進的に primitive です。(9) を微分して \(x_t\) に代入すると

\[
\nabla f_t(x_t)=A_t^T\nabla f(s).
\]

一方 \(x_t=2^rz_t\) なので左辺は \(2^{2r}\) の倍数です。adjugate をもう一度掛けると

\[
2^{2r}\mid 2^t\nabla f(s).
\]

\(\nabla f(s)\) の少なくとも一成分が奇数だから

\[
\boxed{2r\le t.}
\tag{12}
\]

したがって

\[
\boxed{
E\ge u+t-3\left\lfloor\frac t2\right\rfloor
\ge u-\left\lfloor\frac t2\right\rfloor.
}
\tag{13}
\]

これはかなり重要です。**\(P(1)\) と \(P'(1)\) は同じ整数点では保存されないが、「終端形式が巨大な pure-\(2\) Thue–Mahler 解を持つ」という形では強く保存されます。**

判別式を絶対有界にできれば終端形式は有限個になり、各固定既約三次形式について

\[
f_t(x,y)=\pm2^E,\qquad \gcd(x,y)=1
\]

は古典的な Thue–Mahler 方程式なので解は有限個です。従って \(E\)、そして (13) から \(u\) も有界になります。

これで

\[
\boxed{
\text{「}\mathcal R\text{ の一様上界」}
\Longrightarrow
\text{「終端形式有限個」}
\Longrightarrow
\text{「Thue--Mahler により }u\text{ 有界」}
}
\]

という非常に明確な有限化ルートができます。

---

## 6. 保存条件の厳密監査

| 条件 | 降下で保存? | 監査結果 |
|---|---:|---|
| 整数係数 | ✅ | 与えられた補題の \(4\mid c,d\) により保証 |
| \(\mathbf Q\)-既約性 | ✅ | 合理的な可逆変数変換と非零スカラー倍 |
| 正の判別式 | ✅ | \(\Disc/4>0\) |
| 三実根 | ✅ | 既約三次＋正判別式 |
| 三根がすべて負 | ❌ | 一般の projective \(\mathrm{GL}_2\) 変換で符号は保存されない |
| mod2 単根＋二重根 | ✅ | 補題の仮定通り |
| 同じ三次数体 | ✅ | 変数変換は \(\mathbf Q\) 上可逆 |
| 同じ cubic order | ❌ | むしろ各段階で index \(2\) overorder へ移る |
| 判別式の2進付値 | ✅ | 毎回ちょうど2減少 |
| 二項係数由来の形 | ❌ | 新形式を新しい \((n',j')\) に再構成できる保証なし |
| 全桁 Kummer 条件 | ❌ | 既存 GitHub の診断例どおり一般には保存されない |
| \(P(1)=2^u\) を同じ整数点で保持 | ❌ | 単根方向は降下格子から外れる |
| \(P'(1)\) 奇数を同じ点で保持 | ❌ | 同様 |
| \(2\)-冪値を取る原始整数点の存在 | ✅ | (9)–(13) の adjugate 構成で保存 |

特に \(P(1)\) が直接保存されない理由も明確です。mod \(2\) で \(s=(1,1)\) は

\[
f(s)\equiv0,\qquad f_X(s)=P'(1)\equiv1
\]

なので**単根方向**です。一方、正規化 \(f\bmod2=X^2Y\) のあとに行う \(X\mapsto2X\) は mod2 では \(X=0\)、つまり**二重根方向の格子**にしか像を持ちません。

したがって単根 \(s\) をそのまま整数点として逆送することは構造的に不可能です。これは「変数変換の選び方が悪い」のではありません。

---

## 現時点の研究結論

かなり整理できました。**判別式降下をそのまま反例の無限降下にする方針は、Kummer 保存のため成立していません。しかしその保存を要求する必要もありません。**

今回のルートでは、

\[
\boxed{
w\ {\rm odd}\Rightarrow79\,2^wM^3<2^u,
\qquad
w\ {\rm even}\Rightarrow71\,2^wM^3<2^u
}
\]

という強化が得られ、さらに降下後には必ず primitive な

\[
\boxed{f_t(x,y)=\pm2^E}
\]

が残ります。

そして一様有限化に本当に足りないものは、かなり明確に

\[
\boxed{
\frac{2^{u-w}}{M^3}\le B
}
\]

型の**絶対上界**です。これを全桁 Kummer 条件から出せれば、判別式降下 → 有限個の cubic orders → Thue–Mahler という形で一気に有限化へ接続できます。

なお \(316\) と \(568\) の下界だけは、小判別式全実三次数体の表の完全性に依存しています。局所型による \(148,196\) の排除自体は上の短い議論で独立に確認できますが、GitHubへ「証明済み」と入れるなら、**判別式 \(<568\) の全実三次数体を列挙する独立証明書**を付けるのが安全です。


## 回答 657cae35-d333-4a1d-9587-c3919d60df71

続けた。今回は判別式降下と全桁 Kummer 側が、かなり直接につながりました。特に「反例そのものを保存する降下」にこだわらなくても、**終端形式に必要な情報を十分保存して有限化へ持っていける**ことがかなり明確になっています。

### 1. 判別式がブロック変数だけに完全に潰れる

奇数 \(j\) とし、既存のブロック分解

\[
j=TSBg,\qquad y=TRCh,\qquad
j-1=RAa,\qquad y-1=SAb,
\]

\[
n-1=\delta _1RS,\qquad
n-2=2\delta _2ABC,\qquad M=\gamma T
\]

を判別式

\[
\Delta=\Disc(f)
=
\frac{108j^2y^2(j-1)(y-1)}
{M^4(n-1)^3(n-2)^2}
\]

へそのまま代入すると、巨大な因子が全部キャンセルして

\[
\boxed{
\Delta=
\frac{27\,ab\,g^2h^2}
{\gamma^4\delta_1^3\delta_2^2}
}
\tag{A}
\]

になります。

これは記号計算でも恒等的に再確認しました。

ここでの \(a,b,g,h\) は三次形式の係数ではなく、GitHub のブロック分解の変数です。

奇数 \(j\) では \(g,h\) は奇数で、

\[
v_2(a)+v_2(b)=w+1.
\]

そこで

\[
a_0=\frac a{2^{v_2(a)}},\qquad
b_0=\frac b{2^{v_2(b)}}
\]

とすると、判別式の奇数部分は厳密に

\[
\boxed{
D_0:=\frac{\Delta}{2^{w+1}}
=
\frac{27a_0b_0g^2h^2}
{\gamma^4\delta_1^3\delta_2^2}.
}
\tag{B}
\]

これはかなり重要です。**判別式降下の最後に残る奇数判別式が、全桁 Kummer の残余変数 \(a_0,b_0,g,h\) だけで書けた**ことになります。

---

### 2. 降下の終端は完全に二種類

\[
t=\left\lfloor\frac{w-1}{2}\right\rfloor
\]

回降下すると、

\[
\Delta_t=
\begin{cases}
4D_0,&w\ {\rm odd},\\[1mm]
8D_0,&w\ {\rm even}.
\end{cases}
\tag{C}
\]

つまり

\[
v_2(\Delta_t)=
\begin{cases}
2,&w\text{ odd},\\
3,&w\text{ even}.
\end{cases}
\]

終端を \(F=aX^3+bX^2Y+cXY^2+dY^3\) として単根を \([1:0]\) に正規化すると

\[
a,c,d\equiv0,\qquad b\equiv1\pmod2.
\]

対応する cubic order の mod \(2\) 代数は、乗法公式から

\[
\boxed{
R/2R\simeq
\mathbf F_2\times
\mathbf F_2[\varepsilon]/(\varepsilon^2).
}
\tag{D}
\]

したがって「単根＋二重根」は単なる多項式の見かけではなく、**order の局所型として最後まで保存**されています。

---

### 3. 79 と 71 の監査はかなり固まった

全実三次数体の小さい判別式は

\[
49,81,148,169,229,257,316,\ldots,564,568,\ldots
\]

と並びます。:chatgpt-content-reference{index="0"}

\(w\) 奇数の場合、終端の2進判別式指数は2です。最初の候補148の体は

\[
x^3-x^2-3x+1
\]

で、その整数環はこの生成元で monogenic、index \(1\) です。:chatgpt-content-reference{index="1"} ところが mod \(2\) では

\[
x^3+x^2+x+1=(x+1)^3,
\]

なので局所環であり、(D) の「単根＋二重根」型ではありません。

もう一つ \(4\cdot49=196\) の可能性がありますが、判別式49の体では \(2\) は inert、すなわち

\[
\mathcal O_L/2\mathcal O_L\simeq\mathbf F_8
\]

です。LMFDB でも \(p=2\) の cycle type は3です。:chatgpt-content-reference{index="2"} index \(2\) の suborder があれば \(\mathbf F_8\) 内に4元の単位的部分環が必要になりますが、有限体なのでそれは \(\mathbf F_4\) でなければならず、\(\mathbf F_8\) は \(\mathbf F_4\) を含みません。したがって196も不可能。

次の316は

\[
316=4\cdot79,
\qquad
x^3-x^2-4x+2,
\]

で、mod \(2\) は \(x^2(x+1)\)。要求する局所型と一致します。:chatgpt-content-reference{index="3"}

よって

\[
\boxed{w\text{ odd}\Rightarrow D_0\ge79.}
\tag{E}
\]

一方 \(w\) 偶数では終端指数が3。order の index の2進指数を \(s\) とすると field discriminant の指数は \(3-2s\)。数体判別式に \(v_2=1\) はないので \(s=0\)、つまり終端 order は2-maximalです。小判別式表で最初の \(v_2=3\) は

\[
568=8\cdot71,
\]

定義多項式も

\[
x^3-x^2-6x-2\equiv x^2(x+1)\pmod2.
\] :chatgpt-content-reference{index="4"}


したがって

\[
\boxed{w\text{ even}\Rightarrow D_0\ge71.}
\tag{F}
\]

外部依存は「全実三次数体の小判別式表の完全性」だけです。GitHub に定理として入れるなら Belabas/Llorente–Quer 等の表への明示的な引用か、PARI/Magma の独立列挙証明書を付けるのが安全です。:chatgpt-content-reference{index="5"}

---

### 4. \(284M^3<2^u\) を \(336M^3<2^u\) まで押せる

既存の

\[
ab<\frac{\delta BC}{2A},\qquad
gh<\frac{\delta A}{2T^2},
\qquad \delta=\delta_1\delta_2
\]

を (B) に入れると、補正項を捨てずに

\[
\boxed{
D_0<
\frac{27}{32}\,
\frac{2^{u-w}}{M^3}.
}
\tag{G}
\]

が得られます。

これと (E),(F) から

\[
\boxed{
\frac{2528}{27}\,2^wM^3<2^u
\qquad(w\text{ odd}),
}
\tag{H}
\]

\[
\boxed{
\frac{2272}{27}\,2^wM^3<2^u
\qquad(w\text{ even}).
}
\tag{I}
\]

特に \(w\ge2\)。最悪なのは偶数 \(w=2\) なので

\[
\frac{9088}{27}M^3<2^u,
\]

すなわち整数定数として

\[
\boxed{336M^3<2^u}
\tag{J}
\]

を得ます。

奇数 \(w\ge3\) ならさらに

\[
\boxed{749M^3<2^u}.
\]

なので、引継ぎの \(284M^3<2^u\) は奇数 \(j\) について確実に強化できます。

---

### 5. 一番大事な保存監査：\(P(1)\) は別の形で「完全保存」できる

前回は adjugate を使って弱い形で追いましたが、もっと強くできます。

ある降下段階で原始ベクトル \((x,y)\) が単根を持ち上げていて

\[
F_k(x,y)=2^E
\]

とします。単根を \([1:0]\) に持っていけば

\[
x\text{ odd},\qquad y\text{ even}.
\]

次の降下

\[
F_{k+1}(X,Y)=\frac{F_k(2X,Y)}4
\]

に対して、新しい点を

\[
(x,2y)
\]

とすれば

\[
F_{k+1}(x,2y)
=
\frac{F_k(2x,2y)}4
=
2F_k(x,y)
=
2^{E+1}.
\]

しかも \(x\) が奇数なので依然原始的です。

さらに

\[
\frac{\partial F_{k+1}}{\partial Y}(x,2y)
=
\frac14
\frac{\partial F_k}{\partial Y}(2x,2y)
=
\frac{\partial F_k}{\partial Y}(x,y),
\]

なので単根性も保存されます。

したがって帰納的に、奇数 \(j\) では開始点 \(f(1,1)=2^u\) から

\[
\boxed{
F_t(x_t,y_t)=2^{u+t},
\qquad
\gcd(x_t,y_t)=1,
}
\tag{K}
\]

を**正確に**得ます。

これはかなり大きな改善です。

つまり保存されないのは

> 「変換後も新しい \((n',j')\) から来た Erdős 699 の反例である」

という性質です。

一方、

> 「同じ全実三次数体の order の降下であり、終端形式が巨大な原始 pure-\(2\) 値を取る」

という性質は完全に保存できます。

---

### 6. これで一様有限化は「\(D_0\) の上界」だけに還元できる

ここから非常にきれいです。

仮に何らかの方法で

\[
\boxed{D_0\le B}
\tag{L}
\]

という絶対定数 \(B\) を証明できたとします。

すると (C) より

\[
\Disc(F_t)\le8B.
\]

有界な判別式を持つ既約整数 binary cubic form は \(\mathrm{GL}_2(\mathbf Z)\)-同値を除いて有限個しかありません。

その各形式について (K) は

\[
F_t(x,y)=2^E,\qquad \gcd(x,y)=1
\]

という \(S=\{2\}\) の Thue–Mahler 方程式です。固定した既約三次形式について原始解は有限個なので、\(E\) は有限集合に入ります。

ところが

\[
E=u+t\ge u.
\]

したがって \(u\) が有界になり、そこから \(M,n,j\) も有限になります。

つまり、

\[
\boxed{
D_0\text{ の絶対上界}
\Longrightarrow
\text{終端 cubic forms 有限}
\Longrightarrow
\text{Thue--Mahler}
\Longrightarrow
u\text{ 有界}
}
\tag{M}
\]

です。

これは「判別式降下を一様有限化へ接続する」という目的に対して、かなり明確な橋になっています。

---

### 7. 全桁 Kummer との接続も直接式になった

GitHub の dynamic product を

\[
\Pi=\Pi_T\Pi_R\Pi_S\Pi_A
\]

とします。既存結果では

\[
2^{e_2}\Pi\mid abgh.
\]

奇数 \(j\) では、今回

\[
e_2=v_2(abgh)=w+1
\]

が厳密なので

\[
\boxed{\Pi\mid a_0b_0gh.}
\]

(B) から、3の因子だけ除けば

\[
\boxed{\Pi_{(3')}\mid D_0.}
\tag{N}
\]

したがって

\[
\boxed{
\Pi_{(3')}
<
\frac{27}{32}
\frac{2^{u-w}}{M^3}.
}
\tag{O}
\]

これは全桁 Kummer の prefix forcing が作る素数冪を、**終端 cubic order の奇数判別式へ直接押し込む式**です。

以前の

\[
4T^2 2^{e_2}\Pi<\delta^2BC
\]

より、今回の目的には (O) の方が自然です。

したがって次の本命は、

\[
\Pi_{(3')}
\quad\text{または}\quad
a_0b_0g^2h^2
\]

が、全桁条件から無制限には増えられないことを示すことです。

---

### 8. \(w\) にも新しい上限が出る

\(2^w\mid j-1\) の場合を例に

\[
j-1=2^wm,\qquad r=u-w.
\]

\(T\mid j\) なので

\[
\gcd(m,T)=1.
\]

よって

\[
g_0:=\gcd(m,M)\mid\gamma,
\qquad g_0\in\{1,3\}.
\]

そして

\[
\frac{j-1}{n}
=
\frac{m/g_0}{2^rM/g_0}
\]

は既約分数です。分母を \(b\) とすると

\[
v_2(b)=r,\qquad
|bj-an|=b.
\]

つまり \(w\) が大きいこと自体が、\(j/n\) に非常に特殊な dyadic 有理近似を強制します。

GitHub の強化版有理近似不等式をこの分数へ入れ、\(y-1\) 側も対称に処理すると

\[
\boxed{
2^{2w-u}
<
\frac{5M}{6g_0^3},
\qquad g_0\mid\gamma.
}
\tag{P}
\]

が得られます。定数 \(5/6\) は \(u\ge51\) なら十分余裕を持った有理上界です。

例えば

\[
M=1\quad\Longrightarrow\quad
2^{2w-u}<1,
\]

なので

\[
\boxed{w\le\left\lfloor\frac{u-1}{2}\right\rfloor.}
\tag{Q}
\]

判別式の \(w\) と、GitHub の連分数・有理近似ルートがここで直接接続します。

---

現時点では **一様有限化そのものはまだ閉じていません**。ただ、欠けている命題はかなり絞れました。

今の形なら、最優先で狙うべきなのは

\[
\boxed{
D_0=
\frac{27a_0b_0g^2h^2}
{\gamma^4\delta_1^3\delta_2^2}
\ \text{の絶対上界}
}
\]

です。これが取れれば、Kummer 条件を変換後へ保存する必要はもうなく、(M) の Thue–Mahler ルートで有限化できます。

さらに、小判別式を順番に Thue–Mahler で排除する有限証明書もかなり有望です。診断として \(|x|,|y|\le300\) だけ調べると、判別式568の代表形式では見つかった最大指数が16、316では13で、必要な \(u+t\ge51\) からかなり遠いです。もちろんこれは探索であって証明ではありませんが、**316・568から順に厳密な Thue–Mahler 証明書で潰して、\(D_0\) の下限を一気に上げる**方向は実行価値があります。

