# Erdős 699 — i=3 担当2「非平方の中心方程式」全進捗まとめ

**作成日:** 2026-09-22  
**基準 GitHub commit:** `0d2262f3beb7c5ce0535ce4fe998832d558ad965`  
**対象 repo:** `yoshiyoyoyo44/erdos699`  
**状態:** i=3 も Erdős Problem 699 全体も未解決。  
**GitHub 未反映。**

## 0. この文書の目的
固定 commit に既にある結果と、このチャットで担当2として新たに導出した未コミット結果を統合する。
証明済み・監査訂正・有限実験・未監査を区別する。

## 1. 固定正規化
\[
n=\gamma T2^u,\quad u\ge51,\quad
v=v_2(j)\ge1,\quad x=2^v,\quad G=u-4v\ge14.
\]

\[
(\gamma,\delta_1,\delta_2)
=(1,1,1),(1,1,3),(1,3,1),(3,1,1).
\]

\[
\delta=\delta_1\delta_2,\qquad
c_0=\delta_1^2\delta_2,\qquad
P=g_0h_0.
\]

\[
n-1=\delta_1RS,\quad
\frac{n-2}{2}=\delta_2ABC,
\]

\[
j=TSBxg_0,\quad
n-j=TRCxh_0,
\]

\[
j-1=RAa,\quad
n-j-1=SAb.
\]

\[
T^2x^2BCP-A^2ab=\delta_1,
\]

\[
\delta_1S=Aa+TCxh_0,\qquad
\delta_1R=Ab+TBxg_0.
\]

既知：
\[
A,B,C\ge11,\qquad R,S>1.
\]

## 2. \(W_*\) と中心方程式
\[
W_*=rac{\delta BC-Aab}{Tx^2}>0
\]
は正の奇数で
\[
AW_*+TBCP=\delta_1\gamma2^{u-2v-1},
\]
\[
aBg_0+bCh_0=2xW_*,
\]
\[
\gcd(W_*,TABC)=1,\qquad
\gcd(W_*,P)\mid\delta_1\gamma.
\]

また \(p\ge5,\ p\mid W_*\) なら \(p\nmid abP\)。

中心側：
\[
B_G=\gamma c_0 2^{G-3},
\]
\[
0<m<B_G,\quad m\text{ odd},\quad \gcd(m,T)=1,
\]
\[
q=(B_G-m)/T=TPW_*,
\]
\[
m+T^2PW_*=B_G.
\]

正の奇数 \(Z,C_{\rm cen}\) が存在し
\[
\delta_2Z^2=m\gamma2^{u-1}+q,
\]
\[
\delta_1TC_{\rm cen}^2=
\delta_1\gamma2^{G-2+2v}+(n-1)Z.
\]

さらに
\[
q\equiv c_0T^2\pmod{16},\qquad
m\equiv-c_0T^3\pmod{16}.
\]

## 3. 担当2開始前に確立済みの主要結果

### 3.1 Effective gap
\[
abP^2<
\frac{\gamma\delta_1^3\delta_2^2}{16T^3}2^G.
\]

\[
Q=
\operatorname{rad}_{p\ge5}(ab)
\operatorname{rad}_{p\ge5}(\operatorname{cf}_3(P))^2.
\]

\[
u\le972Q\lceil\log_2(486Q)\rceil^2+124.
\]

従って
\[
u<\frac{6561}{4}2^G(G+10)^2+124.
\]

固定 \(G\) は effective finite だが global finite ではない。

### 3.2 第二 Frey
\[
d=\gcd(m,T^2PW_*)\mid\gamma c_0,
\]
\[
\alpha=m/d,\quad
\beta=T^2PW_*/d,\quad
\chi=\alpha+\beta=3^r2^{G-3}.
\]

\[
\Delta_{\min}=(\alpha\beta\chi/16)^2,\qquad
v_2(\Delta_{\min})=2G-14.
\]

\[
R_F=\operatorname{rad}_{p\ge5}(mTPW_*),\qquad
N_F=2\cdot3^\epsilon R_F.
\]

公開曲線表 completeness 依存で
\[
N_F>1000,\quad R_F>166,
\]
および \(mTPW_*\) に少なくとも13個の素因数。

一般 bound：
\[
G<\frac92R_F\lceil\log_2(6R_F)\rceil^2+52.
\]

### 3.3 平方枝排除
第一中心式を
\[
Y^2=A_o2^{u-1}+\delta_2q,\qquad
A_o=\delta_2\gamma m
\]
と書く。

全 \(G\ge14\) で
\[
\boxed{\delta_2q\text{ は平方でない}}.
\]

さらに
\[
\operatorname{sf}(\delta_2q)\equiv1\pmod8,
\qquad
\operatorname{sf}(\delta_2q)\ge17.
\]

先頭係数
\[
\mathcal A=\delta_2\gamma m2^{G-1}
\]
が平方なら
\[
G\text{ odd},\qquad
\gamma T\equiv7\pmod8,
\]
かつ
\[
2^umT^2<(\delta_2\gamma c_0^2)2^{2G-7}.
\]

分岐別に
\[
2G-u\ge13,11,7,13.
\]

従って
\[
G<(u+7)/2
\]
なら先頭係数も非平方。

特に \(T=1\)、より一般に \(T\) 平方なら先頭係数平方は不可能。

### 3.4 既存補助条件
\[
TZ^2-mABC=\gamma\delta_1^2 2^{G-3}.
\]

従って \(p\ge5,\ p\mid m\) なら
\[
\left(\frac{\gamma T2^{G-3}}p\right)=1.
\]

## 4. 監査済み失敗事項
旧 Pell recurrence の予想
\[
v_2(A_n)=3+v_2(3n+5),\qquad
v_2(B_n)=3+v_2(3n-5)
\]
は偽。

反例：
- \(A\): \(n=681\), actual 13, predicted 14.
- \(B\): \(n=343\), actual 16, predicted 13.

また既存 descent \((n,j)\mapsto(n/2,s/2)\) は第二条件を一般には保存しない。

固定された有限個の法だけでは、ある main branch に任意に大きい \(v\) の合同解が通る。
したがって moving modulus / global size / full-digit が必要。

## 5. このチャットで得た主要恒等式

置く
\[
H_1=\delta A-2T^2x^2P,\qquad
H_2=\delta A-T^2x^2P.
\]

### 5.1 三項平方恒等式
\[
\boxed{
\delta_2mA^2+T^3P^2
=
\gamma2^{G-3}H_1^2.
}
\]

### 5.2 第二恒等式
\[
\boxed{
\delta_2qA^2-T^2P^2
=
\gamma TP\,2^{u-2v-1}H_2.
}
\]

### 5.3 中心一次恒等式
\[
\boxed{
\delta_2AZ-TP
=
\gamma2^{u-2v-2}H_1.
}
\]

### 5.4 正確な2進付値
\[
v_2(\delta_2mA^2+T^3P^2)=G-3,
\]
\[
v_2(\delta_2qA^2-T^2P^2)=u-2v-1=G+2v-1,
\]
\[
v_2(\delta_2AZ-TP)=u-2v-2=G+2v-2.
\]

よって
\[
G=r_m+3,
\]
\[
v=(r_q-r_m-2)/2,
\]
\[
u=2r_q-r_m-1.
\]

## 6. \(W_*\) 側の moving 2-adic 条件
\(q=TPW_*\) を代入して
\[
\boxed{
\delta_2A^2W_*-TP
=
\gamma2^{u-2v-1}H_2.
}
\]

従って
\[
v_2(\delta_2A^2W_*-TP)=u-2v-1.
\]

すなわち
\[
\delta_2A^2W_*\equiv TP\pmod{2^{u-2v-1}}.
\]

さらに
\[
\boxed{
AW_*-Z=\gamma\delta_1 2^{u-2v-2}.
}
\]

## 7. 中心差の完全因数分解
置く
\[
D=\delta_1\gamma2^{u-2v-2},
\qquad
Q_2=ABC=\frac{n-2}{2\delta_2}.
\]

すると
\[
\boxed{D^2-Z^2=qQ_2}.
\]

さらに
\[
\boxed{D+Z=AW_*},
\]
\[
\boxed{D-Z=TBCP}.
\]

よって
\[
(D-Z)(D+Z)=qQ_2.
\]

また
\[
\boxed{\gcd(D-Z,D+Z)\mid3}.
\]

## 8. 中心から aggregate を再構成
\[
\boxed{A=\gcd(D+Z,Q_2)}.
\]

\[
\boxed{
W_*=(D+Z)/A,
}
\]
\[
\boxed{
BC=Q_2/A,
}
\]
\[
\boxed{
P=\frac{A(D-Z)}{TQ_2}
=\frac{qA}{T(D+Z)}.
}
\]

さらに
\[
\boxed{
ab=\frac{Tx^2(D-Z)-\delta_1}{A^2}.
}
\]

## 9. \(A\mid C_{\rm cen}\) と混合積
ブロック恒等式から
\[
\boxed{
2\delta_1C_{\rm cen}
=
A(bCh_0-aBg_0).
}
\]

よって
\[
A\mid C_{\rm cen}.
\]

\[
K=C_{\rm cen}/A.
\]

\[
\boxed{
U=xW_*-\delta_1K=aBg_0,
}
\]
\[
\boxed{
V=xW_*+\delta_1K=bCh_0.
}
\]

\[
\boxed{UV=abBCP}.
\]

さらに
\[
\gcd(K,BC)=1.
\]

したがって
\[
\boxed{
A=\gcd(C_{\rm cen},Q_2).
}
\]

## 10. 大素数配置の一意化
\[
\gcd(U,V)
\]
は \(p\ge5\) の素因数を持たない。

同様に
\[
\gcd(W_*,K)
\]
も \(p\ge5\) の素因数を持たない。

従って \(a,b,B,C,g_0,h_0\) の \(p\ge5\) 完全素数冪部分は中心データから一意。

3-free aggregate なら六個全部を gcd で一意復元できる。

## 11. primitive \(2\times2\) gcd table
\(p\ge5\) 部分で

\[
\begin{array}{c|cc}
 & q=TPW_* & Q_2=ABC\\ \hline
D+Z & W_* & A\\
D-Z & TP & BC
\end{array}
\]

が成立。

\[
g=\gcd_{\ge5}(q,Q_2)
\]
なら
\[
\boxed{
g=\gcd_{\ge5}(P,BC),
}
\]
\[
\boxed{
g^2\mid(D-Z)/T=BCP.
}
\]

従って
\[
g<
\sqrt{D/T}
=
\sqrt{\delta_1\gamma/T}\,
2^{(u-2v-2)/2}.
\]

## 12. \(T\) 平方のノルム型
\(T=t^2\) とする。

\[
M=t^3P.
\]

\[
d_m=
\begin{cases}
\gamma,&G\text{ odd},\\
2\gamma,&G\text{ even}.
\end{cases}
\]

すると
\[
\boxed{
M^2-d_mL_m^2=-\delta_2mA^2.
}
\]

したがって \(d_m\in\{1,2,3,6\}\)。
平方差、\(\mathbf Q(\sqrt2)\)、\(\mathbf Q(\sqrt3)\)、\(\mathbf Q(\sqrt6)\) に分かれる。

## 13. \(T\) 平方での平方自由核
\(T\) が平方なら \(m,q\) はともに非平方。

\[
a=\operatorname{sf}(m),\qquad
b=\operatorname{sf}(q)=\operatorname{sf}(PW_*).
\]

分岐別 mod8：
- \((1,1,1)\): \(a\equiv7,\ b\equiv1\).
- \((1,1,3)\): \(a\equiv5,\ b\equiv3\).
- \((1,3,1)\): \(a\equiv7,\ b\equiv1\).
- \((3,1,1)\): \(a\equiv7,\ b\equiv1\).

## 14. \(\gamma=3,T\) 平方の mod24 分類

### 14.1 3-free
\[
3\nmid mq
\]
なら
\[
\boxed{\operatorname{sf}(m)\equiv23\pmod{24}},
\]
\[
\boxed{\operatorname{sf}(q)\equiv1\pmod{24}},
\]
\[
\boxed{\operatorname{sf}(Z)\equiv23\pmod{24}}.
\]

以前候補に出した \((7,17)\) は監査で消えた。

### 14.2 3-divisible
\(3\mid m\) なら
\[
v_3(m)=1,\qquad
v_3(q)\ge3,\qquad
v_3(Z)=1,
\]
\[
3\mid P,\qquad3\mid W_*,
\]
\[
\{v_3(P),v_3(W_*)\}=\{1,\ge2\}.
\]

\[
\operatorname{sf}(m)\equiv
\operatorname{sf}(Z)\equiv15\pmod{24}.
\]

## 15. \(\gamma=1,T\) 平方, \(G\) odd の平方差分解
平方自由核
\[
s=\operatorname{sf}(\delta_2m)
\]
が
\[
s=s_-s_+
\]
に分かれ
\[
s_-\equiv-t^3P/\epsilon\pmod8,
\]
\[
s_+\equiv t^3P/\epsilon\pmod8.
\]

従って
\[
t^3P/\epsilon\equiv3,5\pmod8
\]
なら \(\operatorname{sf}(\delta_2m)\) は \(3,5\pmod8\) 型の素因数を少なくとも2個必要とする。

## 16. 第二中心からの quartic local obstruction
\(T=t^2,\gamma=1,\ p^e\mid m,\ p\ge5\)。

### \(G\) even
\[
y=t2^{u/2}
\]
とし \(r^2\equiv2\pmod{p^e}\)。
ある \(w\) が存在し
\[
w^2\equiv t(y+r(y^2-1))\pmod{p^e}.
\]

符号除去：
\[
\boxed{
w^4-2ty\,w^2
-t^2(y^2-2)(2y^2-1)
\equiv0\pmod{p^e}.
}
\]

### \(G\) odd
\[
y=t2^{(u-1)/2},\quad
s=2^{(G-3)/2}.
\]

\[
\boxed{
w^4
-2tsy\,w^2
-t^2s^2(y^2-1)(4y^2-1)
\equiv0\pmod{p^e}.
}
\]

具体的 forbidden residue classes は有限計算としてのみ報告。再利用前にスクリプト再検算推奨。

## 17. 純2冪 \(T=1,\gamma=1,G\) even
\(u\) も even。

\[
\delta_2=1,\qquad
Q_2=2^{u-1}-1.
\]

\(\delta_1\) は
- \(u\equiv0\pmod6\): \(\delta_1=1\).
- \(u\equiv2,4\pmod6\): \(\delta_1=3\).

\[
D=\delta_1 2^{u-2v-2}.
\]

\[
A=\gcd(D+Z,Q_2),
\]
\[
BC=\gcd(D-Z,Q_2).
\]

従って
\[
\gcd(D+Z,Q_2)\ge11,
\]
\[
\gcd(D-Z,Q_2)\ge121.
\]

## 18. 純2冪 \(\delta_1=3\) branch の3進分類

### \(3\nmid m\)
\[
m\equiv1\pmod3,\qquad
q\equiv2\pmod3.
\]

\[
\gcd(P,W_*)=1.
\]

さらに \(q=PW_*\) は少なくとも2個の distinct prime
\[
p\equiv3,5\pmod8
\]
を持つ。

### \(3\mid m\)
\[
\boxed{v_3(m)=2},
\]
\[
\boxed{v_3(q)\ge2}.
\]

つまり
\[
9\parallel m,\qquad9\mid q.
\]

\[
3\mid P,\qquad3\mid W_*,
\]
\[
\min(v_3(P),v_3(W_*))=1.
\]

\[
\boxed{
v_3(q)=2
\iff
v_3(Z)\ge2.
}
\]

\(v_3(q)\ge3\) なら \(v_3(Z)=1\) で、3進質量は \(P,W_*\) の片方に寄る。

## 19. 中心 sign pattern と A/B/C assignment
純2冪 even-\(G\) で
\[
j=Q_2+1-xC_{\rm cen}.
\]

\[
\boxed{A=\gcd(Q_2,xC_{\rm cen})},
\]
\[
\boxed{B=\gcd(Q_2,xC_{\rm cen}-1)},
\]
\[
\boxed{C=\gcd(Q_2,xC_{\rm cen}+1)}.
\]

完全 \(p^e\parallel Q_2\) は
\[
A: xC_{\rm cen}\equiv0,
\quad
B: xC_{\rm cen}\equiv1,
\quad
C: xC_{\rm cen}\equiv-1
\pmod{p^e}.
\]

## 20. Q₂ full-digit の統一形
\[
Q_2=qM.
\]

A/B/C のどの block でも、適切な \(E\) により
\[
\boxed{(M-E)+(M+E)=2M}
\]
が base \(p\) で carry-free。

## 21. Q₂ 素数 mod24 と digit-sum 下限
\(p\mid Q_2\) なら
\[
p\equiv1,7,17,23\pmod{24}.
\]

完全 \(q=p^e\parallel Q_2\) に対して
\[
p\equiv1\pmod{24}
\Rightarrow
s_p(2Q_2/q)\ge14,
\]

\[
p\equiv7\pmod{24}
\Rightarrow
s_p(2Q_2/q)\ge8,
\]

\[
p\equiv17\pmod{24}
\Rightarrow
s_p(2Q_2/q)\ge6.
\]

## 22. B/C digit sum 4 の pure-prime-power theorem
もし
\[
q=p^e\parallel B,\qquad
s_p((n-2)/q)=4
\]
なら
\[
\boxed{B=p^e}.
\]

同様に
\[
\boxed{C=p^e}.
\]

さらに \(v\ge2\) なら
\[
v_2(p+1)=v.
\]

## 23. Q₂ digit-sum 4 の完全排除
仮に
\[
s_p(2Q_2/p^e)=4.
\]

必要条件から
\[
p\equiv23\pmod{24}.
\]

sparse summand の mod \(p+1\) 解析により
\[
\frac{p+1}{2}\mid Q_2-1
\]
または
\[
\frac{p+1}{2}\mid Q_2+1.
\]

しかし
\[
(p+1)/2\equiv0\pmod{12},
\]
\[
Q_2-1=2(2^{u-2}-1)
\]
は2進付値1、
\[
Q_2+1=2^{u-1}
\]
は2冪。

両方不可能。

従って
\[
\boxed{
\forall p^e\parallel Q_2,\quad
s_p(2Q_2/p^e)\ge6.
}
\]

最終下限：
- \(p\equiv1\pmod{24}\): \(\ge14\)
- \(p\equiv7\pmod{24}\): \(\ge8\)
- \(p\equiv17,23\pmod{24}\): \(\ge6\)

また
\[
\omega(Q_2)\ge3
\]
なので digit-sum 合計は最低18。

## 24. Q₁ full-digit 最小値5
\[
Q_1=(2^u-1)/\delta_1=RS.
\]

既存：
\[
s_\ell((2^u-1)/\ell^f)\ge5.
\]

\(v\ge2\) で等号5なら
\[
v_2(\ell+1)=v.
\]

## 25. \(v\ge3\): Q₁ digit-sum 5 は Mersenne 素数だけ
digit sum \(3+2\) の sparse 解析から
\[
\ell+1\mid2^u.
\]

従って
\[
\boxed{\ell=2^v-1}.
\]

さらに
\[
\boxed{\ell=2^v-1\text{ is prime}},
\]
\[
\boxed{v\text{ is prime}},
\]
\[
\boxed{v\mid u},
\]
\[
\boxed{v\mid G}.
\]

R,S は coprime なので digit-sum 5 exception は高々1個。

従って
\[
2^v-1\text{ composite}
\quad\text{or}\quad
v\nmid G
\]
なら
\[
\boxed{
\forall\ell\mid Q_1,\quad
s_\ell((2^u-1)/\ell^{v_\ell(Q_1)})\ge7.
}
\]

## 26. 残る Q₁ Mersenne 例外
R-block なら
\[
\boxed{
UCh_0'
=
\frac{\ell^r+1}{\ell+1},
\qquad
r\ge3\text{ odd}.
}
\]

S-block なら
\[
\boxed{
UBg_0'
=
\frac{\ell^r+1}{\ell+1},
\qquad
r\ge3\text{ odd}.
}
\]

## 27. 未監査/保留
このチャット初期の square-root split による
\[
Vz_+-Uz_-=2^{G/2+v}
\]
や
\[
V\mu_+-U\mu_-=\delta_1 2^{(G-1)/2}
\]
の方向は、factor assignment と lower bounds の完全再監査が未完。

論文用には現時点で未採用。

## 28. 外部依存の整理
一般証明に使っていない：
- Magma
- Sage
- PARI
- Siegel
- Mordell–Weil
- fixed-coefficient Pell 一般解分類
- 旧 Pell 2進付値予想

外部依存がある既存結果：
第二 Frey の曲線表ベースの
\[
N_F>1000,\quad R_F>166
\]
および13素因数以上。

finite residue-class lists は再検算推奨。

## 29. 現在の strongest picture
特に
\[
T=1,\quad\gamma=1,\quad G\text{ even}
\]
では：

1. \(\delta_2=1\).
2. 中心解から \(j\) が一意。
3. \(A,B,C\) の full prime-power assignment が \(xC_{\rm cen}\equiv0,\pm1\) で一意。
4. \(A,P,W_*,BC,ab,U,V\) まで中心から復元。
5. \(p\ge5\) の \(a,b,B,C,g_0,h_0\) の左右配置も一意。
6. Q₂ full prime-power quotient digit sum はすべて \(\ge6\).
7. mod24 により一部は \(\ge8,\ge14\).
8. Q₁ digit sum 5 を取れるのは \(v\ge3\) なら高々1個。
9. その例外は \(\ell=2^v-1\) Mersenne prime で \(v\mid G\).
10. 残る例外は cyclotomic 型
\[
(\ell^r+1)/(\ell+1),\quad r\ge3\text{ odd}.
\]

## 30. 最優先未解決点

### 30.1 純2冪 even-\(G\) の Mersenne 例外を潰す
残る
\[
\ell=2^v-1,\qquad v\mid G,
\]
\[
\frac{\ell^r+1}{\ell+1}
\]
を既存 size bound
\[
abP^2<
\frac{\gamma\delta_1^3\delta_2^2}{16T^3}2^G
\]
と組み合わせる。

cyclotomic 因子は概ね
\[
\ell^{r-1}\asymp2^{v(r-1)}.
\]

\(r\) と \(G/v\) の直接制約が狙える。

### 30.2 高 digit-sum branch に uniform upper bound
Q₂ は最低6、Q₁ はほぼ最低7まで押し上げたが、大きい digit sum を global contradiction にする uniform upper bound はまだない。

### 30.3 \(\gamma=3,T\) square の二重ノルムをさらに結合
3-free:
\[
(\operatorname{sf}(m),\operatorname{sf}(q),\operatorname{sf}(Z))
\equiv(23,1,23)\pmod{24}.
\]

3-divisible も3進分配が強く固定。
第一・第二 Frey conductor と結ぶ価値が高い。

### 30.4 center-only conductor bounds
中心解から
\[
ab,P,W_*
\]
が復元できるので、第一 curve の \(Q\) と第二 curve の \(R_F\) を中心候補から直接計算可能。

## 31. Overclaim 禁止
- i=3 は未解決。
- Problem 699 全体も未解決。
- fixed \(G\) finite を global finite と言わない。
- fixed coefficient Pell/Siegel を moving coefficient に拡張しない。
- failed Pell valuation conjecture を再利用しない。
- finite residue checks を一般定理と混同しない。
- 未監査 square-root split を確定結果として使わない。

## 32. 固定 commit で参照すべき既存ファイル
- `docs/STATUS.md`
- `research/i3/i3_new_chat_integration_and_effective_gap_2026-09-21.md`
- `research/i3/i3_growing_gap_and_auxiliary_frey_2026-09-21.md`
- `research/i3/i3_gap_square_obstructions_2026-09-21.md`
- `research/i3/i3_exact_gap_and_g9_continuation.md`
- `research/i3/i3_digit_reciprocity_and_W_continuation.md`
- `sources/source_i3_full_digit_kummer_2026-09-14.md`
- `sources/source_pure_power_i3_continuation_2026-09-14.md`
- `research/i3/i3_gap13_and_descent_continuation.md`

## 33. 一行要約
担当2で、両非平方中心式を exact 2-adic valuation・primitive factorization・center reconstruction・full-digit Kummer に結合し、特に純2冪 even-\(G\) では Q₂ の最小 digit-sum 4 を完全排除し、Q₁ の最小5も Mersenne prime 1個の例外にまで縮小した。

**次の最優先:**  
\[
\ell=2^v-1,\qquad
\frac{\ell^r+1}{\ell+1}
\]
という最後の Mersenne/cyclotomic 低桁枝を size bound と結合して潰す。
