# チャット原文：整数方程式系導出

取得日：2026-09-21
チャットID：6ab016c9-24b8-83e9-9e68-586589abf2de
参照：https://chatgpt.com/c/6ab016c9-24b8-83e9-9e68-586589abf2de

以下は取得できたAI回答の原文を古い順に保存したもの。未検証の主張と後続回答による訂正を含む。


## 回答 39cae260-29ad-4b32-a857-e7455ff02b39

かなり使える構造が出ました。今回の係数ルートでは、一般の既約三次式の判別式下界を使わず、**同じ \((n,j)\) から4係数が生じることだけで、完全な整数復元系と大きな gcd の強制**まで持っていけます。現時点では無限範囲の完全排除までは閉じていませんが、残る核心をかなり狭くできます。

## 1. 正確な整数方程式系

\[
R(t):=P(1+t)=N+At+Bt^2+Ct^3
\]

と置きます。二項係数の factorial moment 恒等式

\[
F^{(m)}(1)=y(y-1)\cdots(y-m+1)\binom{n-m}{3-m}
\]

から、これは近似でなく厳密に

\[
\boxed{
N=\frac nK=2^{u-v},
\qquad
A=\frac{3y}{K},
}
\]

\[
\boxed{
B=\frac{3y(y-1)}{K(n-1)},
\qquad
C=\frac{y(y-1)(y-2)}{K(n-1)(n-2)}.
}
\tag{1}
\]

特に \(A\) は奇数なので

\[
s:=\frac A3=\frac yK\in\mathbf Z_{>0}
\]

は奇数です。また

\[
r:=N-s=\frac jK
\]

も正の奇数で、

\[
\boxed{r+s=N=2^{u-v},\qquad 0<r<s.}
\tag{2}
\]

したがって

\[
\boxed{n=KN,\qquad j=Kr,\qquad y=Ks}
\tag{3}
\]

と完全に復元できます。

ここで

\[
\boxed{U:=3s^2-NB=\frac{A^2-3NB}{3}}
\]

と置くと、(1)から

\[
\boxed{
U=\frac{3rs}{KN-1}>0.
}
\tag{4}
\]

さらに驚くほど単純に

\[
\boxed{A-B=KU.}
\tag{5}
\]

よって係数だけから

\[
\boxed{K=\frac{A-B}{U}\in\mathbf Z_{>0}}
\tag{6}
\]

まで復元できます。

次に

\[
\boxed{V:=sB-3NC=\frac{AB-9NC}{3}}
\]

と置くと

\[
\boxed{
V=\frac{2U(Ks-1)}{KN-2}>0
}
\tag{7}
\]

かつ

\[
\boxed{2(B-3C)=KV.}
\tag{8}
\]

したがって4係数は一般の三次整数多項式ではなく、必ず

\[
\boxed{
(A-B)(AB-9NC)
=
2(B-3C)(A^2-3NB)
}
\tag{9}
\]

を満たします。ただし、後で述べるように **(9)だけへ弱めてはいけません**。

逆シフトした元の \(P(z)\) の4係数も保持する必要があります：

\[
\boxed{
E_0=N-A+B-C>0,
}
\]

\[
E_1=A-2B+3C>0,\qquad
E_2=B-3C>0,\qquad
E_3=C>0.
\tag{10}
\]

特に

\[
E_0=
\frac{r(Kr-1)(Kr-2)}
{(KN-1)(KN-2)}
\in\mathbf Z_{>0}.
\tag{11}
\]

これは \(j\ge4\) を係数系の中に残す重要な復元条件です。

---

さらに中心変数へ移します。\(N=2a\) とし、

\[
d:=\frac{s-r}{2}
=\frac{n-2j}{2K},
\qquad
L:=Ka-1=\frac{n-2}{2}.
\]

すると \(a\) は2の冪、\(d\) は正の奇数で \(0<d<a\) です。

(4)は

\[
\boxed{
U(2L+1)=3(a^2-d^2).
}
\tag{12}
\]

また (7) と対称側を比較すると

\[
\boxed{L\mid Ud.}
\tag{13}
\]

ここが今回の一番重要な特殊構造です。

さらに (12) を mod \(N=2a\) で読むと

\[
\boxed{
U\equiv 3d^2\pmod N.
}
\tag{14}
\]

しかも

\[
\boxed{0<U<N.}
\tag{15}
\]

したがって \(U\) は単なる合同類ではなく、

\[
\boxed{
U=\text{「}3d^2\bmod N\text{ の最小正剰余」}
}
\tag{16}
\]

そのものです。

加えて

\[
\boxed{\gcd(U,d)\mid3.}
\tag{17}
\]

これは (12) と \(\gcd(a,d)=1\) から従います。

---

## 2. 新しく得た「大きい middle gcd」の強制

\[
g:=\gcd(L,d)
=
\gcd\!\left(
\frac{n-2}{2},
\frac{n-2j}{2K}
\right).
\tag{18}
\]

\(L=g\ell,\ d=gt\)、\(\gcd(\ell,t)=1\) とします。

(13) と \(\gcd(\ell,t)=1\) より

\[
\boxed{\ell\mid U.}
\]

したがって

\[
U=\ell q,\qquad q\in\mathbf Z_{>0}.
\tag{19}
\]

よって

\[
\frac{L}{g}=\ell\le U,
\]

すなわち

\[
g\ge\frac LU.
\]

(12)を使えば

\[
\frac LU
=
\frac{L(2L+1)}{3(a^2-d^2)}
>
\frac{L(2L+1)}{3a^2}.
\]

\(L=(KN-2)/2,\ a=N/2\) を戻すと

\[
\boxed{
g\ge
\frac{2(KN-2)(KN-1)}{3N^2}.
}
\tag{20}
\]

これは漸近的に

\[
g\gtrsim \frac23K^2.
\]

実際 \(n=KN\ge12\) なら

\[
\boxed{g>\frac{K^2}{2}.}
\tag{21}
\]

反例ではもちろん \(n\gg12\) なので無条件に使えます。

これはかなり重要です。つまり係数構造だけで、

> \((n-2)/2\) の巨大な部分が \(n-2j\) にも同時に入らなければならない

ことが証明されます。

---

## 3. 判別式も特殊な形へ完全簡約できる

一般三次式の判別式下界ではなく、元の \((n,j)\) 構造を代入すると

\[
\boxed{
\operatorname{Disc}(P)
=
\frac{U^2(K^2U-3)}{L^2}.
}
\tag{22}
\]

この恒等式は今回、記号計算でも独立に確認しました。

根が相異なるので

\[
K^2U-3>0.
\]

さらに \(L=g\ell,\ U=\ell q\) とすると、(12)から

\[
\boxed{g^2\mid K^2U-3.}
\tag{23}
\]

したがって

\[
W:=\frac{K^2U-3}{g^2}\in\mathbf Z_{>0}.
\]

そして

\[
\boxed{
\operatorname{Disc}(P)=q^2W.
}
\tag{24}
\]

さらに完全に因数分解した整数系は

\[
\boxed{
W(2g\ell+1)
=
3(\ell^2-K^2t^2),
}
\tag{25}
\]

\[
L=g\ell,\qquad d=gt,\qquad U=\ell q,
\]

\[
\gcd(\ell,t)=1,\qquad
\gcd(g,U)\mid3,
\tag{26}
\]

です。

特に \(W>0\) なので

\[
\boxed{\ell>Kt.}
\tag{27}
\]

これは単なる「判別式が49以上」のような一般論より、かなり原問題寄りの Diophantine 系です。

---

## 4. 最も有望な補題

現時点で一番狙う価値があるのは、次です。

### Dyadic coefficient rigidity lemma — 未証明

\(a\) を2の冪、\(0<d<a\) を奇数、\(K\ge1\) とし、

\[
L=Ka-1,
\]

\[
0<U<2a,\qquad
U\equiv3d^2\pmod{2a},
\]

\[
U(2L+1)=3(a^2-d^2),
\]

\[
L\mid Ud
\]

を満たすとする。

このとき唯一の解は

\[
\boxed{K=1,\qquad d=a-1,\qquad U=3}
\tag{28}
\]

ではないか。

これが証明できれば、

\[
r=a-d=1,\qquad j=Kr=1
\]

となり \(j\ge4\) に反するので、**\(i=3\) は一気に完全排除**です。\(2^u\le C M^{3-\varepsilon}\) を経由する必要すらありません。

残っている一点は非常に明確で、

\[
\boxed{
L=Ka-1\mid Ud
\quad\text{と}\quad
U=\operatorname{leastres}_{2a}(3d^2)
}
\]

の組み合わせから、非退化な \(K^2U>3\) を排除することです。

ここまでの変換・整数性・分母・復元条件はすべて保持されています。

### 実行した計算

この補題について、\(N=2^h,\ h=3,\dots,22\) を**全ての奇数 \(r<N/2\)**について調べました。

ポイントは \(K\) に探索上限を置く必要がないことです。

\[
3r^2=mN+U,\qquad0<U<N
\]

とすると (4) から必ず

\[
\boxed{KU=3r-m.}
\tag{29}
\]

したがって各 \(r\) に対する \(K\) は一意に決まります。その候補について \(B,C\in\mathbf Z\) を厳密整数演算で確認しました。

結果、\(h=3,\ldots,22\) では

\[
\boxed{K=1,\qquad r=1}
\]

以外はありませんでした。

これは**計算結果であり一般証明ではありません**。全桁Kummer条件もこの探索では使用していません。

---

## 5. 弱めた係数条件には実際に無限族がある

ここは重要です。

任意の \(N=2^h,\ h\ge2\) に対し

\[
K=1,\qquad r=1,\qquad s=N-1
\]

とすると

\[
A=3(N-1),\qquad
B=3N-6,\qquad
C=N-3.
\]

したがって

\[
P(1+t)
=
N+3(N-1)t+(3N-6)t^2+(N-3)t^3
\]

は整数係数で、\(A\) は奇数、さらに今回の係数恒等式 (9) も満たします。

しかし

\[
N-A+B-C=0
\]

であり、

\[
K^2U-3=0,\qquad
\operatorname{Disc}(P)=0.
\]

つまりこれは

\[
j=1
\]

に対応する退化族です。

**元問題の反例ではありません。**

したがって、

> \(N=2^h\)、\(A\) 奇数、整数係数、係数恒等式 (9)

程度まで条件を弱めると、\(h\) を一様に抑える命題は偽です。

少なくとも

\[
P(0)>0,\qquad j\ge4,\qquad \operatorname{Disc}(P)>0
\]

あるいはそれと同値な復元条件を絶対に捨ててはいけません。

---

## 6. 全桁 Kummer 担当者に要求したい具体的条件

ここが一番直接的です。

係数側ではすでに

\[
\boxed{
g=
\gcd\!\left(
\frac{n-2}{2},
\frac{n-2j}{2K}
\right)
>
\frac{K^2}{2}
}
\tag{30}
\]

を証明できました。

したがって全桁 Kummer 側には、

\[
\boxed{
\gcd\!\left(
\frac{n-2}{2},
\frac{n-2j}{2K}
\right)
\le\frac{K^2}{2}
}
\tag{31}
\]

を反例候補について証明してほしいです。

これだけで即矛盾です。

完全素数冪で言い換えると、\(p^e\parallel(n-2)/2\) に対して全桁条件から

\[
j\bmod p^e\in\{0,1,2\}
\]

という all-or-nothing の分類を得た場合、

\[
p^e\mid g
\iff
j\equiv1\pmod{p^e}.
\]

したがって要求しているのは、

> **\(j\equiv1\) に割り当てられる完全素数冪ブロックの積が \(K^2/2\) を超えないこと**

です。

\(p=3\) の例外があるなら、それだけを別管理して構いません。

実は \(1/2\) は余裕を持った値です。係数側の真の下界は

\[
g\ge
\frac{2(KN-2)(KN-1)}{3N^2}
=
\frac23K^2-o(1).
\]

よって Kummer 側で任意の固定 \(\eta>0\) に対して

\[
g\le
\left(\frac23-\eta\right)K^2
\]

まで出せれば、大きい \(n\) を一様排除でき、残りは有限になります。

---

現状の一番大きい進展は、**問題を「一般三次式の判別式」から、2冪法での平方剰余 \(U\) と \(L\mid Ud\) の剛性問題へ落とせたこと**だと思います。特に

\[
U=\operatorname{leastres}_{2^{u-v}}(3d^2),
\qquad
Ka-1\mid Ud,
\qquad
\gcd(U,d)\mid3
\]

の3本を同時に使う方向が、今回の担当としては最も有望です。


## 回答 88fbf0f0-2f6a-425e-82c8-f8f729474605

続きです。まず重要な訂正があります。前回こちらが置いた \(j/K,\ y/K\in\mathbf Z\) は、**\(3\mid K\) の枝では一般には正しくありません**。3 の例外を保持した正規化に直すと、むしろ構造がきれいになりました。以下はその修正版です。GitHub の現行 i=3 稿とも突き合わせています。

## 1. 修正版の完全な整数系

\[
P(1+t)=N+At+Bt^2+Ct^3,\qquad N=2^{u-v}=:2^h
\]

とし、

\[
a:=2^{h-1},\qquad N=2a.
\]

元の \(F\) の factorial moment をそのまま使うと

\[
\boxed{
A=\frac{3y}{K},\qquad
B=\frac{3y(y-1)}{K(n-1)},\qquad
C=\frac{y(y-1)(y-2)}{K(n-1)(n-2)}
}
\tag{1}
\]

で、すべて整数、\(A\) は奇数です。

3 の例外を

\[
\varepsilon:=\gcd(K,3)\in\{1,3\},\qquad K=\varepsilon k
\]

として吸収します。さらに

\[
d:=A-3a>0,\qquad e:=\frac{\varepsilon d}{3}.
\]

\(j<n/2\) と \(A\) 奇数から \(e\) は正の奇数です。すると **\(n,j,y\) が完全に復元**され、

\[
\boxed{
n=2\varepsilon ka,\qquad
j=k(\varepsilon a-e),\qquad
y=k(\varepsilon a+e),
}
\tag{2}
\]

\[
\boxed{0<e<\varepsilon a.}
\tag{3}
\]

ここで

\[
L:=\varepsilon ka-1=\frac{n-2}{2},\qquad m:=2L+1=n-1.
\]

元の \(P(z)\) を

\[
P(z)=c_0+c_1z+c_2z^2+c_3z^3,\qquad c_i\in\mathbf Z_{>0}
\]

とします。

中心二係数の和

\[
q:=c_1+c_2=A-B
\]

には

\[
\boxed{
q=\frac{3jy}{K(n-1)}
=\frac{3k(\varepsilon^2a^2-e^2)}
{\varepsilon(2L+1)}.
}
\tag{4}
\]

したがって

\[
\boxed{
(2L+1)q=\frac3\varepsilon k(\varepsilon^2a^2-e^2).
}
\tag{5}
\]

\(\gcd(k,2L+1)=1\) なので

\[
\boxed{k\mid q.}
\tag{6}
\]

さらに

\[
\boxed{
c_1=\frac{q(L-ke)}{2L},\qquad
c_2=\frac{q(L+ke)}{2L}.
}
\tag{7}
\]

2進部分は自動的に整合するので、この二係数の整数性はちょうど

\[
\boxed{L\mid qe}
\tag{8}
\]

に等価です。

そして

\[
z:=c_2-c_1=\frac{qke}{L}\in\mathbf Z.
\tag{9}
\]

端の二係数については

\[
c_0+c_3=2a-q
\]

および

\[
2A-3N=z+3(c_3-c_0)
\]

から

\[
\boxed{
c_3-c_0=\frac{2d-z}{3}.
}
\tag{10}
\]

したがって、中央二係数まで整数になった後に残る端点の整数性は

\[
\boxed{3\mid 2d-z}
\tag{11}
\]

です。これは実際に落としてはいけない条件です。

---

### gcd まで消去した系

\[
g:=\gcd(L,e),\qquad L=g\ell,\qquad e=gt,\qquad(\ell,t)=1
\tag{12}
\]

と置きます。(8) より \(\ell\mid q\)。また (6) と \((k,\ell)=1\) から

\[
\boxed{q=k\ell s}
\tag{13}
\]

となる正整数 \(s\) が存在します。しかも \(s\) は奇数です。

このとき

\[
\boxed{z=k^2st.}
\tag{14}
\]

また

\[
j-1=L-ke=g(\ell-kt)
\]

なので

\[
\boxed{\ell>kt.}
\tag{15}
\]

(5) をこの変数に代入すると、ある \(w\in\mathbf Z_{>0}\) が存在して

\[
\boxed{
g^2w+3=\varepsilon k^2\ell s,
}
\tag{16}
\]

\[
\boxed{
w(2g\ell+1)=3(\ell^2-k^2t^2).
}
\tag{17}
\]

これが今のところ一番小さい「係数構造を全部残した」整数系です。

さらに power-of-two 条件は

\[
\boxed{
g\ell+1=\varepsilon k\,2^{h-1}.
}
\tag{18}
\]

端係数の条件 (11) は

\[
\boxed{
3\mid \frac{6gt}{\varepsilon}-k^2st.
}
\tag{19}
\]

特に \(\varepsilon=1\)、すなわち \(3\nmid K\) なら

\[
\boxed{3\mid st.}
\tag{20}
\]

ここまで全て**証明済みの恒等式・整数性**です。

---

## 2. 新しい強い2進合同式

(5) を法 \(a=2^{h-1}\) で読むと

\[
q\equiv\frac3\varepsilon ke^2\pmod a.
\]

\(v_2(k)=v\) なので、既存範囲では \(h-1>v\) を使って

\[
\ell s\equiv\frac3\varepsilon e^2
\pmod{2^{h-1-v}}.
\]

一方 (18) より

\[
g\ell\equiv-1\pmod{2^{h-1}},
\]

したがって \(e=gt\) を代入すると

\[
\boxed{
\varepsilon\ell^3s
\equiv3t^2
\pmod{2^{h-1-v}}.
}
\tag{21}
\]

前回の途中計算で得ていた法 \(2^{h-1-2v}\) より **さらに一段強く、\(2^{h-1-v}\) まで保持できます**。

特に指数が十分大きければ mod \(8\) で

\[
\boxed{\varepsilon\ell s\equiv3\pmod8.}
\tag{22}
\]

ただし、mod \(8\) 単独では有限化できません。重要なのは (21) が「実際の小さい正整数 \(t\)」を右辺に持つことです。

## 3. 証明できた新補題：中心 \(j=n/2\) からの三次ギャップ

これは今回かなり有用です。

Krawtchouk 型の直接計算で

\[
6F(-1)
=(2j-n)\bigl((n-2j)^2-3n+2\bigr).
\]

従って

\[
\boxed{
P(-1)=
\frac{(2j-n)((n-2j)^2-3n+2)}
{K(n-1)(n-2)}.
}
\tag{23}
\]

他方、シフト表示から

\[
P(-1)=N-2A+4B-8C.
\]

\(N=2^h\) は4の倍数、\(A\) は奇数なので

\[
\boxed{v_2(P(-1))=1.}
\tag{24}
\]

したがって \(P(-1)\neq0\)、かつ

\[
|P(-1)|\ge2.
\]

ここで

\[
D:=n-2j>0.
\]

もし \(D^2<3n-2\) なら \(P(-1)>0\) ですが、

\[
D(3n-2-D^2)
\le
\frac{2(3n-2)^{3/2}}{3\sqrt3}
<2n^{3/2}.
\]

したがって \(n\ge8\) なら

\[
0<P(-1)
<
\frac{2n^{3/2}}{K(n-1)(n-2)}
<2,
\]

これは正の偶整数であることに反します。等号 \(D^2=3n-2\) も (24) に反するので、

\[
\boxed{(n-2j)^2>3n-2,\qquad P(-1)<0.}
\tag{25}
\]

さらに \(-P(-1)\ge2\) から

\[
D(D^2-3n+2)\ge2K(n-1)(n-2).
\]

左辺は \(D^3\) より小さいので、

\[
\boxed{
(n-2j)^3>2K(n-1)(n-2).
}
\tag{26}
\]

これは完全に証明できています。

\(D=2ke\) を代入すると、

\[
\boxed{
e^3>
\frac{\varepsilon L(2L+1)}{2k^2}.
}
\tag{27}
\]

漸近的には

\[
\boxed{e>\varepsilon\,a^{2/3}(1+o(1)).}
\tag{28}
\]

つまり反例候補は中心 \(j=n/2\) に \(n^{2/3}\) より近づけません。

端 \(j=0\) 側も \(c_0=P(0)\ge1\) から、\(f:=\varepsilon a-e=j/k\) と置けば

\[
\boxed{
f^3>
\frac{2\varepsilon L(2L+1)}{k^2}.
}
\tag{29}
\]

従って

\[
\varepsilon a-e\gg\varepsilon a^{2/3}.
\]

つまり今回の係数系だけで、\(e\) は区間

\[
\text{おおよそ}\quad
\varepsilon a^{2/3}
<
e
<
\varepsilon a-O(a^{2/3})
\]

の内部に強制されます。

## 4. さらに「四係数由来」だけの Hessian 整数三つ

これは一般三次式の判別式下界とは別の情報です。

\[
H_0:=c_1^2-3c_0c_2,\qquad
H_1:=c_1c_2-9c_0c_3,\qquad
H_2:=c_2^2-3c_1c_3
\]

とすると、直接展開で

\[
\boxed{
H_0=
\frac{9j^2y(j-1)}
{K^2(n-2)(n-1)^2}>0,
}
\]

\[
\boxed{
H_1=
\frac{18jy(j-1)(y-1)}
{K^2(n-2)(n-1)^2}>0,
}
\]

\[
\boxed{
H_2=
\frac{9jy^2(y-1)}
{K^2(n-2)(n-1)^2}>0.
}
\tag{30}
\]

左辺が係数の整数式なので、

\[
\boxed{H_0,H_1,H_2\in\mathbf Z_{>0}.}
\]

そして三つの和は非常に単純で、

\[
\boxed{
H_0+H_1+H_2
=A^2-3NB
=\frac{9jy}{K^2(n-1)}.
}
\tag{31}
\]

しかも

\[
\boxed{
K(H_0+H_1+H_2)=3q.
}
\tag{32}
\]

さらに

\[
\boxed{
H_1^2-4H_0H_2=-3\Disc(P).
}
\tag{33}
\]

つまり判別式そのものが、「三つの正整数 \(H_0,H_1,H_2\) の二次式」として拘束されます。

縮約変数ではさらに

\[
\boxed{
\Disc(P)=\frac{s^2w}{\varepsilon^2}.
}
\tag{34}
\]

これはかなり使いやすい形です。特に平方因子 \(s^2\) と残余 \(w\) が、係数構造から自然に分離します。

## 5. 現時点で最も有望な有限化補題

今は次を狙うのが最短だと考えています。

**候補補題。** 全桁 Kummer 条件を満たす反例では、ある絶対定数 \(C,\eta>0,\alpha\) に対して

\[
\boxed{
n-2j\le C K^\alpha n^{\,2/3-\eta}.
}
\tag{35}
\]

これが得られれば、証明済みの (26)

\[
n-2j>
\{2K(n-1)(n-2)\}^{1/3}
\asymp K^{1/3}n^{2/3}
\]

と比較して

\[
n^\eta\ll K^{\alpha-1/3}.
\tag{36}
\]

したがって \(K=2^vM\) と既存の \(u,v\) 関係を入れれば、**指数に対する真の上界**になります。

これは単に

\[
g\ll K^{2-\eta}
\]

のような gcd 上界を要求するより強いです。後者だけでは \(K\) を制限しても \(u\) が自由に伸びる余地が残ります。

## 6. 全桁 Kummer 担当へ今要求したい、さらに具体的な形

抽象的な (35) より、実装しやすい形があります。

今回の

\[
\boxed{
g=\gcd(L,e)
=\gcd\!\left(\frac{n-2}{2},\,j-1\right)
}
\tag{37}
\]

は、3 の例外を除けば \(Q_2\) の「\(j\equiv1\) 完全素数冪ブロック」そのものです。

一方

\[
\ell=L/g
\]

は \(j\equiv0,2\) 側です。また

\[
e=gt,\qquad
j-1=g(\ell-kt).
\]

従って全桁担当には、

\[
\boxed{
t=\frac{e}{\gcd((n-2)/2,j-1)}
}
\tag{38}
\]

に対する power-saving 上界、あるいは直接

\[
\boxed{
\varepsilon\ell^3s\equiv3t^2
\pmod{2^{u-2v-1}}
}
\tag{39}
\]

を、\(Q_2\) の全完全素数冪の \(0,1,2\) 配置と同時に満たせないという命題を要求したいです。

ここで \(h=u-v\) なので (39) の法は \(2^{h-1-v}=2^{u-2v-1}\) です。

**これが今の最重要インターフェースです。**

---

結論として、今回の進展は「一般三次式の判別式」からさらに離れて、

\[
\boxed{
\begin{gathered}
g\ell+1=\varepsilon k2^{h-1},\\
g^2w+3=\varepsilon k^2\ell s,\\
w(2g\ell+1)=3(\ell^2-k^2t^2),\\
\varepsilon\ell^3s\equiv3t^2\pmod{2^{h-1-v}},\\
3\mid 6gt/\varepsilon-k^2st
\end{gathered}}
\tag{40}
\]

という**復元可能な正整数系**まで落とせたことです。

まだ (40) 単独から \(u\) の一様上界を証明できてはいません。次に攻める一点は、(17) を \(\ell-kt\) と \(\ell+kt\) に分解して \(Q_1\) の二ブロックと同定し、(39) の巨大な2進法と **\(Q_1,Q_2\) の両方の完全素数冪配置を同時に衝突させること**です。そこが閉じれば、有限探索延長ではなく無限範囲そのものを落とせます。

