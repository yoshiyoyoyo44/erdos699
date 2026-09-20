# Erdős 699 — Kummer 全桁条件の進展（2026-09-13）

**注意。これは Erdős Problem 699 の完全解決ではない。**
このファイルは、現在の GitHub HEAD に既にある結果以降に得た進展だけを記録する。
今後の研究方針や「次に試すこと」は記載しない。

## 1. 完全素数冪を剥がす quotient-lift 補題

\(p\ge 3\) を素数、\(q=p^e\) とする。
\[
n=qN+r,\qquad j=qJ+s,\qquad 0\le s\le r<p.
\]
このとき下位 \(e\) 個の \(p\) 進桁では繰り上がりが発生しないので、Kummer の定理から
\[
\boxed{
v_p\binom nj=v_p\binom NJ.
}
\tag{1}
\]
特に
\[
\boxed{
p\nmid\binom nj\iff p\nmid\binom NJ.
}
\tag{2}
\]

Lucas の定理で書けば
\[
\binom nj\equiv \binom rs\binom NJ\pmod p,
\]
かつ \(\binom rs\not\equiv0\pmod p\) である。

従って、既存の「完全素数冪 \(q\) に対する最下位の剰余条件」は、その後の全ての上位桁を \((N,J)\) に対する同じ無繰り上がり条件として再帰的に残す。

## 2. signed-deviation 形式

\(N=\sum_{\nu\ge0}n_\nu p^\nu\) を \(p\) 進展開とし、
\[
\mathcal D_p(N)=
\left\{
\sum_{\nu\ge0}d_\nu p^\nu:
d_\nu\in\{-n_\nu,-n_\nu+2,\ldots,n_\nu\}
\right\}
\]
と定義する。

\(0\le J\le N\)、\(D=N-2J\) とすると
\[
\boxed{
p\nmid\binom NJ
\iff
D\in\mathcal D_p(N).
}
\tag{3}
\]

証明は Lucas の条件 \(0\le j_\nu\le n_\nu\) に対し \(d_\nu=n_\nu-2j_\nu\) と置けばよい。逆向きは \(j_\nu=(n_\nu-d_\nu)/2\) で戻る。

## 3. \(T,R,S,A,B,C\) の全ブロックへの全桁条件

既存の記号
\[
n=HT,\qquad j=Tk,
\]
\[
Q_1=(n-1)/\delta_1=RS,\qquad
Q_2=(n-2)/(2\delta_2)=ABC
\]
を使う。共通の中心偏差を
\[
\Delta=n-2j
\]
とする。

各ブロックに属する完全素数冪 \(q=p^e\) について、全桁 Kummer 条件は
\[
\boxed{
\begin{array}{c|c}
q\text{ の所属} & \text{全桁 Kummer 条件}\\ \hline
T & \displaystyle \frac{\Delta}{q}\in\mathcal D_p(n/q)\\[5pt]
R & \displaystyle \frac{\Delta+1}{q}\in\mathcal D_p((n-1)/q)\\[5pt]
S & \displaystyle \frac{\Delta-1}{q}\in\mathcal D_p((n-1)/q)\\[5pt]
A & \displaystyle \frac{\Delta}{q}\in\mathcal D_p((n-2)/q)\\[5pt]
B & \displaystyle \frac{\Delta-2}{q}\in\mathcal D_p((n-2)/q)\\[5pt]
C & \displaystyle \frac{\Delta+2}{q}\in\mathcal D_p((n-2)/q).
\end{array}
}
\tag{4}
\]

従来の低位条件
\[
T,A\mid\Delta,\qquad
R\mid\Delta+1,\qquad
S\mid\Delta-1,\qquad
B\mid\Delta-2,\qquad
C\mid\Delta+2
\]
は、(4) の左辺が整数になる部分だけに相当する。

## 4. signed-digit set の最小正要素

\(N=\sum n_\nu p^\nu>0\) とする。

\(n_h\) が奇数となる最大の \(h\) が存在する場合、
\[
\boxed{
g_p(N)=p^h-(N\bmod p^h)
}
\tag{5}
\]
は \(\mathcal D_p(N)\) の最小の正整数である。

従って、(4) の各正の quotient deviation \(D_q\) に対し
\[
\boxed{D_q\ge g_p(N_q)}
\tag{6}
\]
が必要。

全ての \(p\) 進桁が偶数なら \(0\in\mathcal D_p(N)\)。さらに \(q=p^e\) が元の整数の完全 \(p\) 冪成分なら \(p\nmid N\) なので、最小の正要素は
\[
\boxed{2}.
\tag{7}
\]

## 5. 既存の緩和例に対する全桁排除

既存稿にある低位条件の緩和例
\[
(n,j)=(76672,26775),\qquad \Delta=23122
\]
は全桁条件では排除される。

### \(p=17\)

\(17\mid n-2\)、\(17\mid j\) なので B 型。
\[
N=\frac{n-2}{17}=4510,\qquad
J=\frac j{17}=1575.
\]
次の base-17 digit は
\[
J\bmod17=11,\qquad N\bmod17=5.
\]
従って \(11>5\) で Lucas/Kummer 条件に反し、
\[
17\mid\binom{76672}{26775}.
\]

### \(p=41\)

\(41\mid n-2\)、\(j\equiv2\pmod{41}\) なので C 型。
\[
N=\frac{n-2}{41}=1870,\qquad
J=\frac{j-2}{41}=653.
\]
中心偏差商は
\[
N-2J=\frac{\Delta+2}{41}=564.
\]
一方
\[
g_{41}(1870)=1492.
\]
従って \(564<1492\) で (6) に反する。

## 6. \(T=1\) での対称形

\(T=1\) とし
\[
n=2B,\qquad j=B-x,\qquad x>0
\]
と置く。

低位条件は
\[
Q_1\mid j(j-1),\qquad
Q_2\mid j(j-1)(j-2).
\tag{8}
\]

主枝 \(\delta_1=\delta_2=1\) では
\[
Q_1=2B-1,\qquad Q_2=B-1,
\]
よって
\[
\boxed{2B-1\mid(2x-1)(2x+1)}
\tag{9}
\]
\[
\boxed{B-1\mid x(x-1)(x+1)}.
\tag{10}
\]

## 7. \(T=1\) では全桁条件がブロック名に依存しない

### 7.1 \(q=p^e\Vert Q_2\)

低位条件から \(s=j\bmod q\in\{0,1,2\}\)。
\[
M=Q_2/q,\qquad
X=\frac{x-(1-s)}q.
\]
すると
\[
\frac{n-2}{q}=2\delta_2M,\qquad
\frac{j-s}{q}=\delta_2M-X.
\]
従って
\[
\boxed{
v_p\binom nj
=
v_p\binom{2\delta_2M}{\delta_2M-X}.
}
\tag{11}
\]
よって全桁 Kummer 条件は
\[
\boxed{2X\in\mathcal D_p(2\delta_2M)}.
\tag{12}
\]

\(s=0,1,2\)、すなわち A/B/C のどこに属したかは quotient 後には消える。

### 7.2 \(q=p^e\Vert Q_1\)

\[
s=j\bmod q\in\{0,1\},\qquad
\sigma=1-2s\in\{1,-1\},
\]
\[
M=Q_1/q,\qquad
X=\frac{2x-\sigma}{q}.
\]
すると
\[
X=\delta_1M-2J,\qquad
J=\frac{j-s}{q}.
\]
従って
\[
\boxed{
v_p\binom nj
=
v_p\binom{\delta_1M}{(\delta_1M-X)/2},
}
\tag{13}
\]
したがって
\[
\boxed{X\in\mathcal D_p(\delta_1M)}.
\tag{14}
\]

R/S のどちらに属したかも quotient 後には同じ対称形へ統一される。

## 8. \(T=1\) における三分岐から二分岐への圧縮

\(T=1\) で
\[
\boxed{
\rho=\frac{j(j-1)}{2Q_1}.
}
\tag{15}
\]
\(Q_1\) は奇数で \(Q_1\mid j(j-1)\) だから \(\rho\) は正整数。

関係式
\[
\delta_1Q_1=2\delta_2Q_2+1
\]
と \(Q_2\mid j(j-1)(j-2)\) を用いると
\[
\boxed{Q_2\mid\rho(\rho-\delta_1)}.
\tag{16}
\]

実際 mod \(Q_2\) で
\[
2\rho\equiv\delta_1j(j-1),
\]
よって
\[
4\rho(\rho-\delta_1)
\equiv
\delta_1^2j(j-1)(j-2)(j+1)
\equiv0\pmod{Q_2},
\]
かつ \(\gcd(4\delta_1,Q_2)=1\)。

従って \(Q_2\) の完全素数冪について、元の
\[
j\bmod q\in\{0,1,2\}
\]
という三分岐は、\(\rho\) では
\[
\boxed{\rho\bmod q\in\{0,\delta_1\}}
\tag{17}
\]
という二分岐へ圧縮される。

さらに
\[
\boxed{
z=\frac{\rho(\rho-\delta_1)}{Q_2}}
\tag{18}
\]
は正の偶数である。従って
\[
\boxed{\rho(\rho-\delta_1)\ge2Q_2}.
\tag{19}
\]

特に主枝 \(\delta_1=\delta_2=1\)、\(Q=Q_2\) では
\[
\boxed{\rho>\sqrt{2Q}}.
\tag{20}
\]

また
\[
j(j-1)=2\rho(2Q+1),
\]
なので
\[
\boxed{j>2^{5/4}Q^{3/4}}.
\tag{21}
\]
これは既存の \(j>2Q^{3/4}\) を定数の面で強化する。

## 9. 主枝 \(T=\delta_1=\delta_2=1\) の中心距離下界

\[
m=B-1=Q_2
\]
とする。\(n=2^u\) なので \(m\) は奇数。

(9),(10) から
\[
s=\frac{x(x^2-1)}m\in\mathbb Z_{>0},
\qquad
r=\frac{4x^2-1}{2m+1}\in\mathbb Z_{>0}.
\]
直接消去すると
\[
\boxed{2m(2s-xr)=x(r-3)}.
\tag{22}
\]

\(r=1\) なら (22) から \(m\mid x\) となるが \(0<x<m\) なので不可能。

\(r=3\) なら
\[
2(x^2-1)=3m,
\]
左辺が偶数、右辺が奇数で矛盾。

\(r\) は奇数なので \(r\ge5\)。従って (22) の左括弧は正整数で
\[
2m\le x(r-3)<xr.
\]
一方
\[
r=\frac{4x^2-1}{2m+1}<\frac{2x^2}{m}.
\]
よって
\[
2m<\frac{2x^3}{m},
\]
すなわち
\[
\boxed{x^3>m^2=(B-1)^2}.
\tag{23}
\]

従って主枝の候補は必ず
\[
\boxed{x>(B-1)^{2/3}}
\tag{24}
\]
を満たす。

これは有限探索ではなく、低位 Kummer 条件から従う一般的な必要条件である。

以上はすべて必要条件・排除補題であり、\(i=3\) 全体または Erdős 699 全体の完全証明を主張しない。
