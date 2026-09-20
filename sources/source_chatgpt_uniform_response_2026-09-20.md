指定された commit `8072705f3ab9af92cbe076f7b1243617a31ad505` の `i3_mixed_parameter_bound_2026-09-20.md` と `i3_handoff_uniform_integration_2026-09-20.md` を基準に進めた。前者の \(D=w-4\lambda\) と明示的 bound、後者の降下候補
\[
Aq_0+BCTg_0h_0=\delta_1\gamma2^{u-1-2v}
\]
を確認している。チェックポイント自身も、固定 \(D\) の有限還元と「条件を保存する真の降下」を明確に区別している。 

今回、有限探索を使わずにいくつか新しい一様補題まで進んだ。以下は現時点で紙上証明できているもの。

### 1. 降下候補は、予想よりかなり多くの構造を保存する

\(g=2^vg_0,\ h=2^vh_0\) とし、

\[
N:=\delta_1\gamma2^{u-1-2v},\qquad
J:=BCTg_0h_0.
\]

既存の式から
\[
N-J=Aq_0>0.
\]

さらに、これは元の \(n,j\) だけを使って

\[
\boxed{
N=\frac{\delta_1n}{T2^{2v+1}},
\qquad
J=\frac{\delta_1j(n-j)}
{T2^{2v}(n-1)}
}
\tag{A}
\]

と書ける。

ここで予想外にきれいな恒等式が出る：

\[
\boxed{
N-2J=\frac{Z}{T2^{2v}}.
}
\tag{B}
\]

実際、
\[
1-\frac{2J}{N}
=
1-\frac{4j(n-j)}{n(n-1)}
=
\frac{(n-2j)^2-n}{n(n-1)}
\]
へ \(N\) の式を代入すればそのまま \(Z\) の定義になる。

既存成果から
\[
T\mid Z,\qquad v_2(Z)=2v+1,
\]
なので

\[
\boxed{N-2J\in2\mathbb Z_{>0},\qquad v_2(N-2J)=1.}
\]

したがって

\[
\boxed{J<N/2}.
\]

また \(J=BCTg_0h_0\) は奇数で、既存の \(B,C\ge11\) から

\[
\boxed{J\ge121}.
\]

よって

\[
\boxed{4\le J<N/2,\qquad J\text{ は奇数}.}
\tag{C}
\]

さらに \(\delta_1\gamma\in\{1,3\}\) なので

\[
\boxed{N=2^U\quad\text{または}\quad N=3\cdot2^U},
\qquad
U=u-1-2v.
\]

つまりこの写像は任意の反例候補を、

\[
\boxed{
\text{奇数部分 }1\text{ または }3,\quad T'=1,\quad J\text{ 奇数}
}
\]

というかなり特殊な領域に送る。

これは `i3_handoff_uniform_integration` で未確認だった「\(J\le N/2\) を保存できるか」という穴を埋めている。

ただし、**まだ真の反例→反例降下ではない**。残っている核心は

\[
N-1\mid3J(J-1),
\qquad
N-2\mid6J(J-1)(J-2)
\]

および対応する全桁Kummer条件の保存。この2つの新しい法 \(N-1,N-2\) は元の \(n-1,n-2\) の因子ではないので、今の恒等式だけから保存は出ていない。

したがって現時点で安全に言えるのは、

\[
\boxed{
\text{「範囲・偶奇・中心の2進構造を保存する降下」}
}
\]

まで。完全な反例降下とはまだ呼ばない。

---

### 2. \(D-c_0\) の \(T\)-進構造を正確に決定

\[
c_0=\delta_1^2\delta_2,\qquad
D=c_0+TE,\qquad
E=\frac{D-c_0}{T}.
\]

チェックポイントでは \(T\mid D-c_0\) まで証明されている。

これを mod \(T^2\) まで持ち上げると、新しく

\[
\boxed{
E\equiv-\frac{c_0}{2}(4k-H)\pmod T,
\qquad H=\gamma2^u,\quad j=Tk.
}
\tag{D}
\]

が出る。

証明は短い。\(Z=Tz,\rho=Tr\) とし
\[
Q=\frac{TH/2-1}{\delta_2}
\]
を
\[
DQ=Z^2-(2\rho-\delta_1)^2
\]
へ代入し mod \(T^2\) で比較する。さらに
\[
r=\rho/T\equiv\delta_1k/2\pmod T
\]
を使えば (D)。

\(\gcd(T,2c_0)=1\) なので直ちに

\[
\boxed{
\gcd\!\left(T,\frac{D-c_0}{T}\right)
=
\gcd(T,4k-H).
}
\tag{E}
\]

これは \(D\) に関して、既存の単なる
\[
D\equiv c_0\pmod T
\]
より一段強い。

比較として同じ計算から

\[
\boxed{
\frac{w-c_0}{T}\equiv\frac{c_0H}{2}\pmod T,
\qquad
\frac{\lambda}{T}\equiv\frac{c_0k}{2}\pmod T.
}
\tag{F}
\]

最初の式は既存の
\[
\gcd\!\left(T,\frac{w-c_0}{T}\right)=1
\]
を即座に説明する。

つまり \(w-c_0\) では \(T\) は常に unitary だが、\(D-c_0\) で unitary 性が壊れる量は**正確に**

\[
4k-H=\frac{4j-n}{T}
\]

で測られる。

これは固定 \(D\) の有限化とは独立した、全指数に対する局所構造。

---

### 3. \(D=\ell m\) の二因子の共通部分に一様な制約

\[
d:=Z-R_0=AC\ell,\qquad
s:=Z+R_0=Bm,\qquad D=\ell m.
\]

直接計算すると

\[
d=
\frac{\delta_1}{2(n-1)}
\left(
2j^2-4jn+2j+n^2+n-2
\right),
\]

\[
s=
\frac{\delta_1}{2(n-1)}
\left(
6j^2-4jn-2j+n^2-3n+2
\right).
\]

この2つには単純な一次関係がある：

\[
\boxed{
s-3d=\delta_1(4j-n-4).
}
\tag{G}
\]

さらに residue allocation から

\[
\boxed{\gcd(\ell,B)=1,\qquad \gcd(m,AC)=1.}
\tag{H}
\]

従って

\[
g:=\gcd(|\ell|,m)=\gcd(|d|,s).
\]

\(g_0=g/\gcd(g,\delta_1)\) とする。(G) より

\[
4j\equiv n+4\pmod{g_0}.
\]

一方 \(g_0\mid d\)。上の \(d\) の二次式へこの合同式を戻すと

\[
\boxed{
g_0\mid n^2-12n+16=(n-6)^2-20.
}
\tag{I}
\]

そして \(D=\ell m\) だから当然

\[
\boxed{g^2\mid D.}
\tag{J}
\]

つまり \(D\) の二つの因子の大きな共通部分は自由ではなく、

\[
\boxed{
g/\gcd(g,\delta_1)
\mid (n-6)^2-20
}
\]

を満たさなければならない。

特に \(p\ne5\) が
\[
p\mid g,\qquad p\nmid\delta_1
\]
なら

\[
(n-6)^2\equiv20\pmod p
\]

なので

\[
\boxed{\left(\frac5p\right)=1},
\]

従って

\[
\boxed{p\equiv\pm1\pmod5}.
\tag{K}
\]

つまり \(D\asymp n\) を \(\ell,m\) の巨大な共通因子で実現しようとすると、その共通部分は、3の例外と5を除き**全て \(\mathbf Q(\sqrt5)\) で split する素数**だけからできなければならない。

これも固定 \(D\) の議論ではない。

---

### 4. 個々の \(\ell,m\) にも一様な平方剰余条件

さらに上の二次式の判別式は

\[
\Delta_-=
4(2n^2-6n+5),
\]

\[
\Delta_+=
-4(2n^2-22n+11).
\]

よって、ブロック由来の自明な場合も含めて、\(\ell\) の各奇素因数 \(p\) には原則として

\[
\boxed{
2n^2-6n+5
\text{ が mod }p\text{ で平方}
}
\tag{L}
\]

が必要。

\(m\) の各奇素因数には

\[
\boxed{
-(2n^2-22n+11)
\text{ が mod }p\text{ で平方}
}
\tag{M}
\]

が必要になる。

\(p\mid Q\) ではそれぞれ自動的に
\[
1,\quad25
\]
となり、\(p\mid Q_1\) では
\[
1,\quad9
\]
となるので既存ブロックとも整合する。

したがってこれは「Qの素因数だけを言い換えた条件」ではなく、**\(D\) が新しく持ち込む素因数にも同じ平方剰余制約を延長する**もの。

ただし、ここから全 \(\ell,m\) を排除する quadratic-reciprocity の閉じた矛盾まではまだ得られていない。

---

### 5. 補助的に得た、C因子のBと対称な上限

これはCodex側の「因子の大きさ」と少し重なるので主ルートにはしていないが、証明できる。

\[
\boxed{
L_C:=
\frac{\delta_1(n-j)(2n-j-2)}
{(n-1)C^2}\in\mathbb Z_{>0}.
}
\]

\(C\mid n-j\) かつ \(C\mid2n-j-2\)、また mod \(Q_1\) では

\[
(n-j)(2n-j-2)
\equiv j(j-1)
\]

だから整数性が従う。

さらに既存の \(B\) の商と全く同じ2進計算で

\[
\boxed{\chi_vT\mid L_C}.
\]

従って

\[
\boxed{
C^2\le
\frac{\delta_1(n-j)(2n-j-2)}
{\chi_vT(n-1)}.
}
\tag{N}
\]

これは checkpoint の

\[
B^2\le
\frac{\delta_1j(j+n-2)}
{\chi_vT(n-1)}
\]

の完全な C-side analogue。

ただ、これだけを既存の \(A,B,C\) の大きさと組み合わせても、現時点では \(D\) の一様上限までは出ない。主に
\[
\chi_vT\ll\sqrt n
\]
型の、既存の \(u\ge4v+14\) より弱い領域へ戻ってしまう。

---

## 現時点の評価

一番価値があるのは (B) と (E) だと思う。

降下については、

\[
(n,j)\mapsto(N,J)
\]

が

\[
N\in\{2^U,3\cdot2^U\},\qquad
J\text{ odd},\qquad
4\le J<N/2,
\]

さらに

\[
N-2J=\frac{Z}{T2^{2v}},\qquad v_2(N-2J)=1
\]

まで**本当に保存する**ことが分かった。

一方、反復に必要な \(N-1,N-2\) のKummer条件はまだ保存できていない。ここを無視して「無限降下完成」とするのは不可。

\(D\to\infty\) については、今回

\[
D=\ell m
\]

の共通部分を

\[
g^2\mid D,\qquad
g/\gcd(g,\delta_1)\mid(n-6)^2-20
\]

まで押し込めた。したがって、大きな \(D\) が

1. \(\ell,m\) の大きな共通部分から来るなら、その素数はほぼ全部 \(p\equiv\pm1\pmod5\)；
2. 共通部分が小さいなら、\(\ell/g,m/g\) という二つの大きな互いに素な因子が残り、それぞれ (L),(M) の別々の平方剰余条件を満たす、

という**一様な二分**が得られた。

ここから quadratic reciprocity だけで両ケースを完全に矛盾へ持っていくところまでは、今回まだ届いていない。なので、Problem 699 や \(i=3\) の完全解決は主張しない。

ただ、固定 \(D\)・固定gap・有限合同の延長ではなく、今回はちゃんと **\(D\) が無限に成長する場合にも残る条件**が増えている。特に (B) は「指数が減るだけだった変換」を、かなり真の降下に近づける新しい保存則になっている。
