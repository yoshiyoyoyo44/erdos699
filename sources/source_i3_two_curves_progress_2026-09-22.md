# Erdős 699・担当3「二つの楕円曲線」統合研究チェックポイント

**作成日:** 2026-09-22  
**固定参照コミット:** `0d2262f3beb7c5ce0535ce4fe998832d558ad965`  
**対象:** Erdős #699, 仮想反例の `i=3`・偶数 `j` 枝  
**状態:** **問題699全体も i=3 も未解決。** 本文は、この担当チャットで得た必要条件・新しい恒等式・楕円曲線制約・排除済み枝・訂正履歴を一つに統合した研究再開用チェックポイントである。GitHub には未反映。

---

## 0. この文書のラベル

- **[既存]** 固定参照コミット以前にリポジトリで証明・監査済み。
- **[新規・代数]** この担当チャットで、既存恒等式から直接導いた結果。外部定理を不要とするもの。
- **[新規・外部依存]** この担当チャットで導いたが、modularity / isogeny 分類 / Thue–Mahler / 数体データ等の外部入力を使うもの。
- **[監査要]** 数学的筋は通っているが、論文・repo へ入れる前に出典と局所条件を独立再監査すべき箇所。
- **[撤回]** 途中で誤りが判明し、後段で修正済みの主張。

---

# 1. 基本正規化と既存の土台

[既存] 偶数 `j` の仮想反例に対し

\[
n=\gamma T2^u,\qquad u\ge 51,\qquad v=v_2(j)\ge1,
\]
\[
x=2^v,\qquad G=u-4v\ge14.
\]

分岐は

\[
(\gamma,\delta_1,\delta_2)\in
\{(1,1,1),(1,1,3),(1,3,1),(3,1,1)\},
\]

\[
\delta=\delta_1\delta_2,\qquad c_0=\delta_1^2\delta_2.
\]

正の奇整数

\[
A,B,C,R,S,T,a,b,g_0,h_0
\]

を用い、`P=g_0h_0` とする。六ブロック表示は

\[
n-1=\delta_1RS,
\qquad
\frac{n-2}{2}=\delta_2ABC,
\]
\[
j=TSBxg_0,
\qquad
n-j=TRCxh_0,
\]
\[
j-1=RAa,
\qquad
n-j-1=SAb,
\]
\[
T^2x^2BCP-A^2ab=\delta_1.
\tag{1.1}
\]

また

\[
W_*:=\frac{\delta BC-Aab}{Tx^2}>0
\]

は奇数で

\[
AW_*+TBCP=\delta_1\gamma2^{u-2v-1},
\tag{1.2}
\]
\[
aBg_0+bCh_0=2xW_*.
\tag{1.3}
\]

素数台の分離として

\[
\gcd(W_*,TABC)=1,
\qquad
\gcd(W_*,P)\mid\delta_1\gamma,
\tag{1.4}
\]

したがって `p>=5, p|W_*` なら

\[
p\nmid abP.
\tag{1.5}
\]

---

# 2. 中心和と第二 Frey 曲線

[既存] 中心の整数

\[
B_G=\gamma c_0 2^{G-3},
\qquad 0<m<B_G,
\]

を用いると

\[
q=\frac{B_G-m}{T}=TPW_*,
\tag{2.1}
\]

従って

\[
\boxed{m+T^2PW_*=B_G.}
\tag{2.2}
\]

さらに

\[
d=\gcd(m,T^2PW_*)\mid\gamma c_0.
\]

\[
\alpha=\frac md,
\qquad
\beta=\frac{T^2PW_*}{d},
\qquad
\chi=\alpha+\beta=3^r2^{G-3},
\]

\[
0\le r\le2.
\tag{2.3}
\]

`alpha,beta,chi` は正の奇整数で対ごとに互いに素。

第二 Frey 曲線

\[
F:\quad y^2=X(X-\alpha)(X+\beta)
\tag{2.4}
\]

は full rational 2-torsion を持つ。

[既存] 適切な大域最小モデルで

\[
\Delta_{F,\min}=
\left(\frac{\alpha\beta\chi}{16}\right)^2,
\tag{2.5}
\]

\[
v_2(\Delta_{F,\min})=2G-14,
\tag{2.6}
\]

`F` は半安定、

\[
N_F=2\cdot 3^\epsilon R_F,
\qquad
R_F=\operatorname{rad}_{\ge5}(mTPW_*).
\tag{2.7}
\]

また

\[
R_F
=
\operatorname{rad}_{\ge5}(m)
\operatorname{rad}_{\ge5}(TP)
\operatorname{rad}_{\ge5}(W_*),
\tag{2.8}
\]

右辺三因子は対ごとに互いに素。

[既存] 公開曲線表と一般導手・判別式評価から

\[
R_F>166,
\tag{2.9}
\]

かつ

\[
G<\frac92R_F\left\lceil\log_2(6R_F)\right\rceil^2+52.
\tag{2.10}
\]

---

# 3. 第一楕円曲線と導手量 Q

[既存] 三次式から作る第一曲線 `E_D` の最適二次捻りでは、5以上の素数に対する導手量を

\[
Q=
\operatorname{rad}_{\ge5}(ab)
\operatorname{rad}_{\ge5}(\operatorname{cf}_3(P))^2
\tag{3.1}
\]

で支配できる。

ここで `cf_3` は各素数の指数を mod 3 で 0,1,2 に落とした 3-free 部分。

[既存]

\[
abP^2<
\kappa\frac{2^G}{T^3},
\qquad
\kappa=\frac{\gamma\delta_1^3\delta_2^2}{16}.
\tag{3.2}
\]

分岐別 `kappa` は

\[
\frac1{16},\frac9{16},\frac{27}{16},\frac3{16}.
\]

また

\[
u\le972Q\left\lceil\log_2(486Q)\right\rceil^2+124.
\tag{3.3}
\]

従って

\[
u<\frac{6561}{4}2^G(G+10)^2+124.
\tag{3.4}
\]

---

# 4. 新しい共通パラメータ lambda

[新規・代数] 定義

\[
e_c=\delta A-2T^2x^2P,
\qquad
\lambda:=\frac{e_c}{\delta A},
\qquad 0<\lambda<1.
\tag{4.1}
\]

また

\[
y:=1-\lambda.
\]

六ブロックから

\[
\boxed{
\lambda
=1-
\frac{4j(n-j)}{(n-1)(n-2)}
}
\tag{4.2}
\]

を得る。

`D=n-2j` とすると

\[
\boxed{
\lambda=
\frac{D^2-3n+2}{(n-1)(n-2)}.
}
\tag{4.3}
\]

これは中心 gap と二曲線をつなぐ基本パラメータ。

---

# 5. m/B_G と lambda の完全な関係

[新規・代数]

中心の

\[
w=(\delta A-2T^2x^2P)(\delta BC-2Aab)
=c_0+4Tx^4m
\]

を用いると

\[
\boxed{
\frac{m}{B_G}
=
\lambda^2-
\frac{2(1-\lambda)^2}{n}.
}
\tag{5.1}
\]

` t := m/B_G = alpha/chi ` と置けば

\[
\boxed{
t=
1-2y+\left(1-\frac2n\right)y^2.
}
\tag{5.2}
\]

従って `lambda -> t` は厳密単調増加。

---

# 6. abP^2 と中心比率の完全な1変数化

[新規・代数]

\[
\boxed{
abP^2
=
\frac{\kappa2^G}{T^3}
(1-\lambda)^2
\frac{(n-2)(1-\lambda)-4}{n}.
}
\tag{6.1}
\]

特に

\[
\boxed{
abP^2
<
\frac{\kappa2^G}{T^3}
(1-\lambda)^3.
}
\tag{6.2}
\]

(5.1) から `lambda > sqrt(m/B_G)` なので

\[
\boxed{
Q<
\frac{\kappa2^G}{T^3}
\left(1-\sqrt{\frac m{B_G}}\right)^3.
}
\tag{6.3}
\]

これは第一曲線の導手量 `Q` と第二曲線の中心分割 `m/B_G=alpha/chi` を直接結ぶ。

さらに

\[
\sigma_n(t):=
\sqrt{t+\frac{2(1-t)}n}
\]

とすれば

\[
1-\lambda
=
\frac{1-\sigma_n(t)}{1-2/n},
\]

従って (6.1) は `t` の明示関数として書ける。

---

# 7. 第一曲線から m/B_G への明示上限

[新規・代数 + 既存導手評価]

(3.3) より

\[
Q\ge
\frac{u-124}{972(G+10)^2}.
\tag{7.1}
\]

(6.3) と合わせて

\[
\boxed{
\frac m{B_G}
<
\left[
1-
\left(
\frac{(u-124)T^3}
{972\kappa2^G(G+10)^2}
\right)^{1/3}
\right]^2.
}
\tag{7.2}
\]

括弧内の立方根が 1 以上ならその枝は即排除。

---

# 8. Q > sqrt(u) の閾値

[新規・代数]

(3.3) から、`u>=2^40` なら

\[
\boxed{Q>\sqrt u.}
\tag{8.1}
\]

証明の核：もし `Q<=sqrt(u)` なら

\[
\lceil\log_2(486Q)\rceil<10+\frac12\log_2u,
\]

従って (3.3) を `sqrt(u)` で割ると `u=2^40` の時点で右辺比が 1 未満で、その後単調減少する。

この結果と (6.3) を合わせると、`m/B_G` が正の定数から離れない枝では `G` に追加下界が入る。

---

# 9. Q と R_F の直接的な弱い橋

[新規・代数]

` t=alpha/chi ` とすると

\[
\alpha\beta=\chi^2t(1-t).
\]

したがって

\[
R_F\le\alpha\beta=\chi^2t(1-t).
\tag{9.1}
\]

\[
\rho:=\frac{R_F}{\chi^2}
\]

とおけば

\[
t(1-t)\ge\rho,
\]

よって

\[
t\ge
\frac{1-\sqrt{1-4\rho}}2
\]

または対称側。

(6.3) から

\[
Q<
\frac{\kappa2^G}{T^3}
\left(
1-
\sqrt{
\frac{1-\sqrt{1-4R_F/\chi^2}}2
}
\right)^3.
\tag{9.2}
\]

ただし `R_F << chi^2` では弱い。

---

# 10. 第一・第二曲線の j-invariant の1変数リンク

[既存 + 新規・代数]

第一曲線の `j` 不変量を `j_E` と書く。
既存結果

\[
j_E-1728
=
\frac{1728(n-1)(n-2j)^2}
{n^2(j-1)(n-j-1)}>0.
\]

(4.3) を代入すると

\[
\boxed{
 j_E-1728
=
\frac{
6912[3n-2+\lambda(n-1)(n-2)]
}
{n^2[n-6-\lambda(n-2)]}.
}
\tag{10.1}
\]

さらに

\[
\boxed{
\frac{d}{d\lambda}(j_E-1728)
=
\frac{6912(n-2)^3}
{n^2[n-6-\lambda(n-2)]^2}>0.
}
\tag{10.2}
\]

第二曲線では `t=alpha/chi` として

\[
\boxed{
 j_F
=256\frac{(1-t+t^2)^3}{t^2(1-t)^2}.
}
\tag{10.3}
\]

また

\[
\boxed{
 j_F-1728
=64\frac{(t-2)^2(t+1)^2(2t-1)^2}{t^2(1-t)^2}.
}
\tag{10.4}
\]

従って

\[
\boxed{E\leftrightarrow\lambda\leftrightarrow t=\alpha/\chi\leftrightarrow F}
\]

という明示的な1変数リンクがある。

**重要:** これは isogeny を仮定しない。

---

# 11. 二曲線は Q-isogenous ではない

[新規・代数]

第一曲線 `E_D` は、元の irreducible cubic から構成されるため有理2-torsionを持たない。

第二曲線 `F` は

\[
X=0,\alpha,-\beta
\]

に full rational 2-torsion を持つ。

有理 isogeny class 内で rational 2-torsion の存在を最小次数 isogeny で追うと、`E_D` と `F` が Q-isogenous なら矛盾する。

従って

\[
\boxed{E_D\not\sim_{\mathbf Q}F.}
\tag{11.1}
\]

**結論:** 二曲線比較で「同じパラメータだから isogenous」などを使ってはいけない。

---

# 12. 第二曲線上の自然な twist point と障害

[新規・代数]

中心式から `H=n/2` と置くと

\[
X_0=\alpha H
\]

に対し

\[
X_0(X_0-\alpha)(X_0+\beta)
=
(\alpha\delta_2TZ)^2
\cdot
\frac{\gamma2^{u-1}ABC}{d}.
\tag{12.1}
\]

したがって `F` の twist

\[
D_0Y^2=X(X-\alpha)(X+\beta),
\qquad
D_0=\frac{\gamma2^{u-1}ABC}{d}
\tag{12.2}
\]

に明示点が存在する。

ただし twist squareclass に `ABC` が入り、これは `Q` と `R_F` だけでは制御されない。
これは 2-descent を二曲線で直結する際の構造的障害。

---

# 13. 新しい完全恒等式：ab と中心 q/m の橋

[新規・代数]

\[
\boxed{
T^2x^4q-c_0
=
Aab(\delta A-T^2x^2P).
}
\tag{13.1}
\]

既存の

\[
\delta A>2T^2x^2P
\]

より右辺は正。

また `B_G-m=Tq` と `8Tx^4B_G=c_0n` を使うと

\[
\boxed{
c_0(n-8)-8Tx^4m
=
8Aab(\delta A-T^2x^2P)>0.
}
\tag{13.2}
\]

これにより以前の合同式は正の完全恒等式へ昇格した。

---

# 14. ab 上で delta_2 q は全素数冪に対して平方

[新規・代数]

(13.1) を mod `ab` で見ると

\[
T^2x^4q\equiv c_0\pmod{ab}.
\]

よって

\[
\boxed{
(Tx^2)^2\delta_2q\equiv\delta^2\pmod{ab}.
}
\tag{14.1}
\]

従って `p^e|ab, p>=5` なら

\[
\boxed{\delta_2q\text{ は mod }p^e\text{ で平方}.}
\tag{14.2}
\]

既存の

\[
D_q:=\operatorname{sf}(\delta_2q)\equiv1\pmod8,
\qquad D_q\ge17
\]

と合わせると

\[
\boxed{
 p\mid ab,\,p\ge5
\Longrightarrow
\left(\frac{D_q}{p}\right)=1.
}
\tag{14.3}
\]

---

# 15. ab-m 共有素数の完全 endpoint collapse

[新規・代数]

(13.2) から `p>=5, p|ab` なら

\[
\boxed{
\min(v_p(ab),v_p(m))
=
\min(v_p(ab),v_p(n-8)).
}
\tag{15.1}
\]

特に

\[
\boxed{
\operatorname{rad}_{\ge5}\gcd(ab,m)
=
\operatorname{rad}_{\ge5}\gcd(ab,n-8).
}
\tag{15.2}
\]

`p^s|gcd(ab,m)` なら

\[
\boxed{n\equiv8\pmod{p^s}.}
\tag{15.3}
\]

さらに `p` は `a,b` のちょうど一方を割る。

- `p|a` なら `(n,j)≡(8,1) mod p^s`
- `p|b` なら `(n,j)≡(8,7) mod p^s`

中心変数について

\[
Z\equiv\frac{\delta_1}{Tx^2}\pmod{p^s},
\tag{15.4}
\]

\[
C_{\rm cen}\equiv\pm\frac3{Tx}\pmod{p^s}.
\tag{15.5}
\]

そして **二つの中心平方条件はこの mod `p^s` で恒等的に成立する。**

したがって shared prime を中心の局所平方条件だけで排除する戦略には本質的 no-go がある。

---

# 16. P-channel の endpoint collapse

[新規・代数]

`p^e|P` なら、5以上では `g_0,h_0` の一方だけを割る。

- `p^e|g_0` なら `j≡0 mod p^e`
- `p^e|h_0` なら `n-j≡0 mod p^e`

中心量は

\[
Z\equiv
\delta_1\gamma2^{G+2v-2}
\pmod{p^e},
\tag{16.1}
\]

\[
C_{\rm cen}\equiv
\pm\gamma2^{G+3v-1}
\pmod{p^e}.
\tag{16.2}
\]

ここでも二つの中心平方条件は恒等的に成立。

**結論:** `Q` と第二 residual support を同じ大素数が支える二つの共有 channel は、中心平方式が局所的に退化する点そのもの。

---

# 17. exact common-support formula

[新規・代数]

\[
A_5=\operatorname{rad}_{\ge5}(ab),
\qquad
C_5=\operatorname{rad}_{\ge5}(\operatorname{cf}_3(P)).
\]

第一導手は

\[
Q=A_5C_5^2.
\]

第二側 `R_F` との共有素数について

\[
\boxed{
\gcd(Q,R_F)
=
C_5\cdot\gcd(A_5,n-8).
}
\tag{17.1}
\]

ここで gcd の `C_5` は squarefree で一度だけ現れる。

`ab-m` 共有素数 `p>=5, p!=7` は `n(n-1)(n-2)` の素因数ではないため、元の Kummer no-shared-prime 条件がその素数に直接作用しない。

---

# 18. 三つの平方類制約

[新規・代数]

5以上の各素数冪に対し：

### (a) `p^e|m`

既存恒等式

\[
TZ^2-mABC=\gamma\delta_1^22^{G-3}
\]

から

\[
\boxed{
\gamma T2^{G-3}
\text{ は mod }p^e\text{ で平方}.
}
\tag{18.1}
\]

### (b) `p^e|TP`

(1.1) から

\[
\boxed{
-\delta_1ab
\text{ は mod }p^e\text{ で平方}.
}
\tag{18.2}
\]

### (c) `p^e|W_*`

既存の

\[
r^2\equiv-\delta AP
\pmod{2^{v+1}W_*}
\]

と (1.2) を合わせると

\[
\boxed{
-\delta_1\gamma Tab2^{G-1}
\text{ は mod }p^e\text{ で平方}.
}
\tag{18.3}
\]

三つの平方類は積関係を持ち、`W_*` 側は `m` 側と `TP` 側の積 squareclass と一致する。

また `p^e|ab` では

\[
\boxed{\delta_2TPW_*\text{ は mod }p^e\text{ で平方}.}
\tag{18.4}
\]

---

# 19. 二つの大域ノルム方程式

[新規・代数]

\[
\delta_2q=D_qY_q^2,
\qquad
D_q=\operatorname{sf}(\delta_2q).
\]

(13.1) から

\[
\boxed{
N_{\mathbf Q(\sqrt{D_q})/\mathbf Q}
\left(
\delta+Tx^2Y_q\sqrt{D_q}
\right)
=
-\delta_2Aab(\delta A-T^2x^2P).
}
\tag{19.1}
\]

一方

\[
\gamma T2^{G-3}=D_mY_m^2,
\]

とおくと

\[
\boxed{
N_{\mathbf Q(\sqrt{D_m})/\mathbf Q}
(TZ+\delta_1Y_m\sqrt{D_m})
=mTABC.
}
\tag{19.2}
\]

共有素数では局所平方条件が退化するため、今後はこれら大域 norm factorization と六ブロック互いに素性を同時に使う必要がある。

`T=1` では

\[
D_m\in\{1,2,3,6\}
\]

に固定される。

---

# 20. mod 3 rational-isogeny branch の分類

[新規・外部依存 / 監査要]

第二曲線の 3-division polynomial を

\[
\psi_3(X)=
3X^4+4(\beta-\alpha)X^3
-6\alpha\beta X^2
-\alpha^2\beta^2
\tag{20.1}
\]

と計算。

`F[3]` が reducible、すなわち rational 3-isogeny があるなら `psi_3` は有理根を持つ。

パラメータ化すると、`G>=14` で候補は最終的に

\[
(G,r;\{\alpha,\beta\})
=(16,1;\{11,24565\})
\tag{20.2}
\]

または

\[
(19,2;\{33275,556549\}).
\tag{20.3}
\]

法16中心条件と既存の「`delta_2 q` は非平方」を使って両方排除。

従って

\[
\boxed{\bar\rho_{F,3}\text{ は既約}.}
\tag{20.4}
\]

---

# 21. mod 3 image は GL_2(F_3)

[新規・外部依存 / 監査要]

既約性に加え、mod 3 residual level に 5以上の素数が少なくとも一つ残ることを modularity / low-level cusp-space の消滅から示す。

その素数の inertia image は非自明 transvection を含む。

既約 subgroup of `GL_2(F_3)` が transvection を含み、determinant が cyclotomic で全射なら

\[
\boxed{
\operatorname{im}\bar\rho_{F,3}
=\mathrm{GL}_2(\mathbf F_3).
}
\tag{21.1}
\]

---

# 22. cube-free residual level L_3

[新規・外部依存]

\[
L_3=
\operatorname{rad}_{\ge5}
\left(
\operatorname{cf}_3(mT^2PW_*)
\right).
\tag{22.1}
\]

mod 3 level lowering により、5以上で指数が3の倍数の素数は residual level から消える。

第一曲線と合わせると、中心積の 3-free support

\[
S_{\rm cen}:=
\operatorname{rad}_{\ge5}
\left(
\operatorname{cf}_3(mTPW_*)
\right)
\]

について

\[
\boxed{S_{\rm cen}\mid\operatorname{rad}(QL_3),}
\tag{22.2}
\]

したがって

\[
\boxed{S_{\rm cen}\le QL_3.}
\tag{22.3}
\]

二曲線を同時に使うことで、`T,P` の mod 3 指数混合による取り逃しを防げる。

---

# 23. 固定 L_3 support なら G は有効有限

[新規・外部依存]

\[
\alpha=AX^3,
\qquad
\beta=BY^3
\]

と 3-free parts を分離すると

\[
\boxed{
AX^3+BY^3=3^r2^{G-3}.
}
\tag{23.1}
\]

固定 `L_3=L` なら `(A,B,r)` は高々

\[
7\cdot4^{\omega(L)}
\tag{23.2}
\]

通り。

`A=B=1` の可約ケースは `G>=14` で初等的に排除。

それ以外は irreducible cubic Thue–Mahler equation。

従って Thue–Mahler の有効解法により

\[
\boxed{L_3=L\Longrightarrow G\le G_{\max}(L)}
\tag{23.3}
\]

となる計算可能な上限が存在。

さらに有限素数集合 `S` を固定して

\[
\operatorname{Supp}(L_3)\subseteq S
\]

だけでも有限個の Thue–Mahler に落ちるため `G` は有効有界。

**重要帰結:** 新しい巨大素数をすべて「3乗指数だけ」で投入して `G->infty` とする逃げ道はない。

---

# 24. exponent gcd の原始性

[新規・代数]

\[
H:=\gcd_{p\mid\alpha\beta}v_p(\alpha\beta).
\]

すると

\[
\boxed{H=1.}
\tag{24.1}
\]

### `2|H` の排除

`alpha,beta` が両方平方なら、奇数平方は mod 8 で1なので

\[
\alpha+\beta\equiv2\pmod8,
\]

`3^r2^{G-3}` (`G-3>=11`) に反する。

### `3|H` の排除

`alpha=A^3, beta=B^3` なら

\[
(A+B)(A^2-AB+B^2)=3^r2^k.
\]

第二因子は奇数で `<=9`。正の互いに素な奇数 `A,B` では `k>=11` と両立しない。

### `ell>=5 | H` の排除

`alpha=A^ell, beta=B^ell` なら

\[
A^\ell+B^\ell=(A+B)R_\ell,
\]

`R_ell` は奇数で `R_ell|3^r`, よって `R_ell<=9`。

非自明 `max(A,B)>=3` なら

\[
R_\ell\ge\frac{3^{\ell-1}}2>9.
\]

矛盾。

---

# 25. 5以上の指数 gcd h_5

定義

\[
h_5=
\gcd_{p\ge5,\,p\mid\alpha\beta}
v_p(\alpha\beta).
\tag{25.1}
\]

[新規・代数] `H=1` から、`h_5>1` なら

\[
\boxed{r=0,\qquad3\mid\alpha\beta,}
\tag{25.2}
\]

\[
\boxed{\gcd(h_5,v_3(\alpha\beta))=1.}
\tag{25.3}
\]

また parity から

\[
\boxed{2\nmid h_5.}
\tag{25.4}
\]

---

# 26. 3 | h_5 の完全排除

[新規・代数 + 一部外部依存]

`3|h_5` なら、順序を除き

\[
\alpha=3^\nu A^3,
\qquad
\beta=B^3,
\qquad
\nu\in\{1,2\},
\]

かつ

\[
B^3+3^\nu A^3=2^k,
\qquad k=G-3\ge11.
\tag{26.1}
\]

### `nu=1`

\[
B^3+3A^3=2^k
\]

は Tzanakis の完全解により `k>=11` では不可能。**外部依存。**

### `nu=2`

\[
B^3+9A^3=2^k.
\]

mod 9 から `3|k`。

`z=2^{k/3}` として

\[
z^3-B^3=9A^3.
\]

因数分解と LTE で

\[
z-B=3X^3,
\qquad
z^2+zB+B^2=3Y^3.
\]

Eisenstein 整数 `Z[omega]` で

\[
z-B\omega
=\eta(1-\omega)(a+b\omega)^3.
\]

parity により `eta=±omega^2`。
実係数から

\[
2^{k/3}
=|(a-2b)(a+b)(2a-b)|.
\]

三因子は pairwise coprime で積が2冪なので、奇数因子二つは `±1`、残る偶数因子の絶対値は2。

従って `z=2`、しかし `k>=12` なら `z>=16`。矛盾。

ゆえに

\[
\boxed{3\nmid h_5.}
\tag{26.2}
\]

---

# 27. residual irreducibility と supersingular 制約

[新規・外部依存 / 監査要]

full rational 2-torsion と rational isogeny graph の分類を組み合わせると、第二曲線の residual representation は少なくとも

\[
\boxed{\bar\rho_{F,\ell}\text{ は全素数 }\ell\ge5\text{ で既約}}
\tag{27.1}
\]

とした。

**注意:** 特に `ell=5,7` の isogeny-graph 排除は、repo 化前に原典で再確認すること。

`ell|h_5` とする。level lowering 後の level は 3 または6。

- `ell|alpha beta` なら multiplicative + Serre weight 2 となるが、level 3/6 に weight-2 cusp form がなく矛盾。
- `ell` で good ordinary でも weight 2 で同じ矛盾。

従って

\[
\boxed{\ell\nmid\alpha\beta,}
\tag{27.2}
\]

\[
\boxed{F\bmod\ell\text{ は supersingular}.}
\tag{27.3}
\]

full rational 2-torsion は good reduction で injective なので

\[
4\mid\#F(\mathbf F_\ell).
\]

`ell>3` supersingular なら `a_ell=0`, よって

\[
\#F(\mathbf F_\ell)=\ell+1.
\]

したがって

\[
\boxed{\ell\equiv3\pmod4.}
\tag{27.4}
\]

従って

\[
\boxed{5\nmid h_5.}
\tag{27.5}
\]

---

# 28. 7 | h_5 の mod 7 modular reduction

[新規・外部依存 / 監査要]

`7|h_5` を仮定。

mod 7 representation は supersingular weight 8。

2 が residual level から消える `k≡4 mod 7` の場合、weight 8 level 3 の唯一の newform の `a_2=6` が multiplicative level-lowering congruence `±3 mod 7` と合わず排除。

従って residual level は6。

weight 8 level 6 の unique newform `6.8.a.a` に落ちる。

補助素数

\[
29,43,71,113,127
\]

で exact trace sieve を行い、最終的に

\[
\boxed{
\alpha=9A^7,
\qquad
\beta=B^7,
\qquad
k=G-3\equiv10\pmod{14}.
}
\tag{28.1}
\]

従って

\[
\boxed{B^7+9A^7=2^k,\qquad k\equiv10\pmod{14}.}
\tag{28.2}
\]

これは

\[
B^7+9A^7=8Z^7,
\qquad
Z=2^{2m+1}
\]

という固定次数7曲線へ落ちる。

---

# 29. 7 | h_5 の完全排除：pure septic unit descent

[新規・外部依存]

`rho^7=3`, `K=Q(rho)` とする。

LMFDB 数体データを外部入力として

\[
\mathcal O_K=\mathbf Z[\rho]
\]

および unit rank 3、基本単数

\[
\varepsilon_1=\rho^4+\rho+1,
\]
\[
\varepsilon_2=
\rho^6-\rho^5-\rho^4+2\rho^3+\rho^2-2\rho+1,
\]
\[
\varepsilon_3=
\rho^6-\rho^5+\rho^4-\rho^3+\rho^2-2
\]

を使う。

\[
\xi=B+A\rho^2
\]

なら

\[
N_{K/\mathbf Q}(\xi)=B^7+9A^7=2^k.
\tag{29.1}
\]

\[
\pi=1-\rho,
\qquad N(\pi)=-2.
\]

`A,B` が奇数なので mod 2 で `xi≡1+rho^2`。
`x^7+1` の mod 2 分解から、`xi` を割る2上の素イデアルは `(pi)` のみ。

従って

\[
\boxed{
B+A\rho^2
=\varepsilon(1-\rho)^k
}
\tag{29.2}
\]

となる unit `epsilon` が存在。

`k≡10 mod 14` を使い unit exponents を mod 7 で落とす。

mod 2 の有限環で 343 unit classes を調べると許されるのは

\[
\boxed{
(n_1,n_2,n_3)
\equiv
(i,2i,6-2i)
\pmod7,
\quad i=0,\ldots,6.
}
\tag{29.3}
\]

つまり 343 -> 7。

次に mod 4 で

\[
\Lambda(c_0+c_1\rho+\cdots+c_6\rho^6)
:=c_1+c_3+c_5+c_6\pmod4
\tag{29.4}
\]

と置く。

7個の基本 residue 全てで

\[
\Lambda=2\pmod4.
\]

さらに基本単数の指数を 7 ずつずらしても `Lambda` は不変。
符号を変えても `2 -> -2 = 2 mod4`。

一方左辺 `B+A rho^2` は `rho,rho^3,rho^5,rho^6` の係数が0なので

\[
\Lambda(B+A\rho^2)=0.
\]

矛盾。

従って

\[
\boxed{7\nmid h_5.}
\tag{29.5}
\]

**重要:** この排除は `h_5=7` だけでなく `7|h_5` の全体を排除する。

---

# 30. 現在の h_5 の最終状態

ここまでで

\[
2\nmid h_5,
\qquad
3\nmid h_5,
\qquad
5\nmid h_5,
\qquad
7\nmid h_5.
\]

さらに全素因数は `3 mod 4`。

従って

\[
\boxed{
h_5>1
\Longrightarrow
p\mid h_5\Rightarrow p\ge11,\ p\equiv3\pmod4.
}
\tag{30.1}
\]

したがって

\[
\boxed{h_5>1\Longrightarrow h_5\ge11.}
\tag{30.2}
\]

また

\[
R_F^{h_5}\le\alpha\beta
\le\frac{(\alpha+\beta)^2}{4}
=2^{2G-8}.
\tag{30.3}
\]

`R_F>166` と `h_5>=11` から

\[
\boxed{h_5>1\Longrightarrow G\ge45.}
\tag{30.4}
\]

従って

\[
\boxed{14\le G\le44\Longrightarrow h_5=1.}
\tag{30.5}
\]

---

# 31. 訂正・撤回履歴

## 31.1 [撤回] mod 23 で指数 gcd を直接排除

途中で

> `23` は Mazur prime-isogeny list 外なので、`23|h_5` は level 1/2 weight 2 に落ちて矛盾

としたが、**誤り**。

`23\nmid alpha beta` の good supersingular case では Serre weight 24 があり得るため、weight 2 固定はできない。

この主張は撤回。

後により正しい一般結果：`ell|h_5` なら good supersingular を強制し、full 2-torsion から `ell≡3 mod4` を得る、へ置換した。

## 31.2 [撤回] `abP^2 < delta d beta /(2T^3)`

途中コメントで `W_*/P` 下界からこの形を書いたが、`ab` 因子を落としていた。
正しく直接従うのは `P^2` に対する上界であり、この誤式は最終結果では使用していない。

## 31.3 [訂正] h_5=7 枝での mod 7 residue

一度 `(A,B)` の mod7 候補を誤って記した。
固定曲線

\[
B^7+9A^7=8Z^7
\]

を mod49 で再計算すると

\[
B\equiv-A,
\qquad
Z\equiv A\pmod7.
\]

`Z=2^{odd}` より正しい候補は

\[
(A,B,Z)\equiv
(1,6,1),(2,5,2),(4,3,4)\pmod7.
\]

この旧誤合同は pure septic unit descent には使用していない。

---

# 32. 現在の「何が本当に残っているか」

## 32.1 i=3 全体

**未解決。**

## 32.2 第二曲線 exponent gcd branch

- `h_5=1`：当然まだ残る。これが主要な一般枝。
- `h_5>1`：
  - `2,3,5,7` は割れない。
  - 全素因数は `>=11` かつ `3 mod 4`。
  - `G>=45`。
  - 各 `ell|h_5` で `F mod ell` は supersingular。

次の最小候補は

\[
\boxed{11\mid h_5.}
\]

## 32.3 shared large-prime branch

第一曲線 `Q` と第二側 residual support が同じ大素数を共有する経路は本質的に

1. `P`-channel
2. `ab-m` channel (`n≡8` endpoint)

の二つ。

しかしその素数では中心二平方条件が自動的に成立し、局所平方条件による排除は効かない。

## 32.4 残る高速無限枝

固定した cube-free support `L_3` では `G` は有効有限。
したがって無限反例列があるなら、新しい large prime が 3-free support に次々出現する必要がある。

第一曲線側でも `Q` は増大する必要がある。

従って二曲線を同時に見た残存枝は

> 第一曲線の導手と第二曲線の residual support の両方に moving large primes を供給し続ける枝

に限定される。

---

# 33. 次にやるべき研究タスク（優先順）

## A. `11 | h_5` branch

一般形は

\[
B^{11}+3^sA^{11}=2^k,
\qquad 1\le s\le10,
\]

型。

候補方針：

1. mod 11 residual representation の level/weight を確定。
2. weight 12, level 3/6 側の newforms と比較。
3. auxiliary-prime Kraus sieve で `(s,k mod M, orientation)` を圧縮。
4. 固定 generalized Fermat curve に落ちれば `Q(3^{1/11})` の unit descent を検討。

## B. `h_5=1` の一般枝

exponent gcd に頼れない本命。

- `L_3` と `Q` の large-prime escape を同時に追う。
- `lambda` / `t=alpha/chi` の1変数リンクを使って導手高さを同時評価。
- `P`-channel と `ab-m` channel の共有素数を、局所平方ではなく大域 norm / Kummer / digit conditions で攻める。

## C. T=1 を優先

`T=1` では

\[
D_m\in\{1,2,3,6\}
\]

となり、第二 norm field が固定小二次体になる。

全桁 Kummer と `L_3`, `Q` を同時に入れる価値が高い。

## D. formal audit

repo へ入れる前に特に再監査すべき外部依存：

1. mod 3 rational-isogeny candidate classification の細部。
2. `bar rho_{F,3}=GL_2(F_3)` の residual conductor / weight 条件。
3. `ell=5,7` における full rational 2-torsion と rational ell-isogeny の両立不能の原典。
4. weight 8 level 3/6 newform の一意性と使用した Fourier coefficients。
5. `Q(3^{1/7})` の integral basis と fundamental units の LMFDB データを Sage/Magma/Pari で独立再計算。

---

# 34. 参照すべき固定コミット内ファイル

最低限：

- `docs/STATUS.md`
- `research/i3/i3_new_chat_integration_and_effective_gap_2026-09-21.md`
- `research/i3/i3_growing_gap_and_auxiliary_frey_2026-09-21.md`
- `research/i3/i3_gap_square_obstructions_2026-09-21.md`
- `research/i3/i3_quadratic_twist_and_kummer_support_2026-09-21.md`
- `research/i3/i3_discriminant_support_and_elliptic_curve_2026-09-21.md`
- `research/i3/i3_digit_reciprocity_and_W_continuation.md`
- `research/i3/i3_exact_gap_and_g9_continuation.md`
- `research/i3/i3_integrated_digits_and_center.md`
- `research/i3/i3_four_chat_integration_2026-09-21.md`

固定参照：

`0d2262f3beb7c5ce0535ce4fe998832d558ad965`

---

# 35. 一行で現在地

担当3で得た最も重要な構造は、

\[
E\leftrightarrow\lambda\leftrightarrow\alpha/\chi\leftrightarrow F
\]

という二曲線の明示的1変数リンク、共有導手素数での endpoint collapse、固定 residual support の有効有限性、そして第二曲線の5以上の指数 gcd に対する

\[
\boxed{
7\nmid h_5,
\qquad
h_5>1\Rightarrow h_5\ge11,\ G\ge45
}
\]

までの排除である。

**ただし問題699全体も i=3 全体も未解決。**
