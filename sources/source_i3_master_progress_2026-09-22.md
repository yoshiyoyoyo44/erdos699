# Erdős Problem 699 — i=3 Master Progress Note
## 2026-09-22 統合版

**固定参照コミット:** `0d2262f3beb7c5ce0535ce4fe998832d558ad965`

**現状:** 問題699全体も i=3 全体も未解決。本稿は、これまでに得た紙上証明、有限証明書、外部定理依存の結果、修正点、未解決点を重複なしで統合した研究再開用マスター記録。

---

# 1. 基本正規化

偶数 j の主要枝で

\[
n=\gamma T2^u,\qquad u\ge51,\qquad v=v_2(j)\ge1,
\]
\[
x=2^v,\qquad G=u-4v\ge14.
\]

\[
(\gamma,\delta_1,\delta_2)\in\{(1,1,1),(1,1,3),(1,3,1),(3,1,1)\},
\]
\[
c_0=\delta_1^2\delta_2,\qquad P=g_0h_0.
\]

六ブロック A,B,C,R,S,T は正の奇数で pairwise coprime、

\[
A,B,C\ge11,\qquad R,S>1,
\]
\[
\gcd(T,\gamma\delta_1\delta_2)=1.
\]

補助因子 a,b,g_0,h_0 は正の奇数。

基本分解:

\[
n-1=\delta_1RS,
\]
\[
\frac{n-2}{2}=\delta_2ABC,
\]
\[
j=TSBxg_0,
\]
\[
n-j=TRCxh_0,
\]
\[
j-1=RAa,
\]
\[
n-j-1=SAb.
\]

主要行列式:

\[
\boxed{T^2x^2BCP-A^2ab=\delta_1.}
\tag{1.1}
\]

線形恒等式:

\[
\boxed{\delta_1S=Aa+TCxh_0,}
\tag{1.2}
\]
\[
\boxed{\delta_1R=Ab+TBxg_0.}
\tag{1.3}
\]

---

# 2. W_* と中心系

\[
W_*:=\frac{\delta BC-Aab}{Tx^2},\qquad \delta=\delta_1\delta_2.
\]

既知:

\[
W_*>0,\qquad W_*\ \text{odd},
\]
\[
\gcd(W_*,TABC)=1,
\]
\[
\gcd(W_*,P)\mid\delta_1\gamma.
\]

p\ge5, p\mid W_* なら

\[
p\nmid abP.
\]

重要な和:

\[
\boxed{AW_*+TBCP=\delta_1\gamma2^{u-2v-1}.}
\tag{2.1}
\]

\[
\boxed{aBg_0+bCh_0=2xW_*.}
\tag{2.2}
\]

中心変数:

\[
B_G=\gamma c_0 2^{G-3},
\]
\[
0<m<B_G,\qquad m\ \text{odd},\qquad \gcd(m,T)=1,
\]
\[
q=\frac{B_G-m}{T}=TPW_*,
\]
\[
\boxed{m+T^2PW_*=B_G.}
\tag{2.3}
\]

中心平方:

\[
\boxed{\delta_2Z^2=m\gamma2^{u-1}+q,}
\tag{2.4}
\]
\[
\boxed{\delta_1TC_{\rm cen}^2=\delta_1\gamma2^{G-2+2v}+(n-1)Z.}
\tag{2.5}
\]

16進条件:

\[
q\equiv c_0T^2\pmod{16},\qquad m\equiv-c_0T^3\pmod{16}.
\]

---

# 3. Full-digit Kummer table

完全素数冪 p^e\parallel F に対して、対応 quotient addition は base p で carry-free。

| Block | 第1加数 | 第2加数 | 合計 |
|---|---|---|---|
| T | j/p^e | (n-j)/p^e | n/p^e |
| R | (j-1)/p^e | (n-j)/p^e | (n-1)/p^e |
| S | j/p^e | (n-j-1)/p^e | (n-1)/p^e |
| A | (j-1)/p^e | (n-j-1)/p^e | (n-2)/p^e |
| B | j/p^e | (n-j-2)/p^e | (n-2)/p^e |
| C | (j-2)/p^e | (n-j)/p^e | (n-2)/p^e |

v_2(j)\ge2 では全六ブロック合算で

\[
\boxed{\mathcal D\ge8\omega(T)+7\omega(Q_1)+6\omega(Q_2)-4,}
\tag{3.1}
\]

\[
Q_1=RS,\qquad Q_2=ABC.
\]

T=1 なら

\[
\boxed{\mathcal D\ge7\omega(Q_1)+6\omega(Q_2)-4.}
\tag{3.2}
\]

重要: この lower bound 単独では D の一様 upper bound がないため完全排除にはならない。

---

# 4. 第一Frey / cube-removal

5以上の導手量:

\[
\boxed{\mathcal Q=\operatorname{rad}_{p\ge5}(ab)\,\operatorname{rad}_{p\ge5}(\operatorname{cf}_3(P))^2.}
\tag{4.1}
\]

主 bound:

\[
\boxed{u\le972\mathcal Q\left\lceil\log_2(486\mathcal Q)\right\rceil^2+124.}
\tag{4.2}
\]

したがって

\[
\mathcal Q=o(u/(\log u)^2)
\]

は不可能。

さらに

\[
\boxed{abP^2<\kappa\frac{2^G}{T^3},\qquad \kappa=\frac{\gamma\delta_1^3\delta_2^2}{16}\le\frac{27}{16}.}
\tag{4.3}
\]

したがって

\[
\boxed{T<2^{(G+1)/3}.}
\tag{4.4}
\]

---

# 5. cube-blind support

\[
A_0=\operatorname{rad}_{p\ge5}(ab),
\]
\[
V=\operatorname{rad}_{p\ge5}(\operatorname{cf}_3(P)),
\]
\[
H=\prod_{\substack{p\ge5,\ p\mid P\\3\mid v_p(P)}}p.
\]

すると

\[
\operatorname{rad}_{p\ge5}(P)=VH,
\]
\[
\mathcal Q=A_0V^2.
\]

H^6\mid P^2 なので

\[
\boxed{H<\kappa^{1/6}2^{G/6}T^{-1/2}.}
\tag{5.1}
\]

第一Freyから完全に消える cube-support も G によって制約される。

---

# 6. 第二Frey: center gap curve

\[
m+T^2PW_*=\gamma c_0 2^{G-3}.
\]

primitive 化して full-2-torsion curve を構成。

\[
\boxed{v_2(\Delta_{F,\min})=2G-14.}
\tag{6.1}
\]

5以上導手:

\[
\boxed{R_F=\operatorname{rad}_{p\ge5}(mTPW_*).}
\tag{6.2}
\]

しかも

\[
R_F=\operatorname{rad}_{p\ge5}(m)\operatorname{rad}_{p\ge5}(TP)\operatorname{rad}_{p\ge5}(W_*),
\]

三因子は pairwise coprime。

一般 bound:

\[
\boxed{G<\frac92R_F\left\lceil\log_2(6R_F)\right\rceil^2+52.}
\tag{6.3}
\]

したがって R_F=o(G/(\log G)^2) は不可能。

外部完全曲線表に依存する追加排除:

\[
R_F>166,
\]

かつ mTPW_* は13以上の素因数を持つ。

---

# 7. direct n-1 curve

\[
E_1:\ y^2+xy=x^3+\frac n4x^2+\frac n{16}x.
\]

\[
\boxed{v_2(\Delta_{1,\min})=2u-8.}
\]

\[
\boxed{R_1=\operatorname{rad}_{p\ge5}(RST).}
\]

\[
\boxed{u<\frac92R_1\left\lceil\log_2(6R_1)\right\rceil^2+49.}
\tag{7.1}
\]

---

# 8. direct n-2 curve

\[
E_2:\ y^2+xy=x^3+\frac n8x^2+\frac n{32}x.
\]

\[
\boxed{v_2(\Delta_{2,\min})=2u-10.}
\]

\[
\boxed{R_2=\operatorname{rad}_{p\ge5}(ABCT).}
\]

\[
\boxed{u<\frac92R_2\left\lceil\log_2(6R_2)\right\rceil^2+50.}
\tag{8.1}
\]

---

# 9. J-split curve

\[
SBg_0+RCh_0=\gamma2^{u-v}.
\]

full-2-torsion Frey:

\[
\boxed{v_2(\Delta_{J,\min})=2(u-v)-8.}
\]

\[
\boxed{R_J=\operatorname{rad}_{p\ge5}(RSBCP).}
\]

\[
\boxed{u-v<\frac92R_J\left\lceil\log_2(6R_J)\right\rceil^2+49.}
\tag{9.1}
\]

P の cube-support も full radical として捕捉する。

---

# 10. block Frey

\[
AW_*+TBCP=\delta_1\gamma2^{u-2v-1}.
\]

\[
\boxed{v_2(\Delta_{\rm blk,\min})=u+G-10.}
\]

\[
\boxed{R_{\rm blk}=\operatorname{rad}_{p\ge5}(ABCTPW_*).}
\]

\[
\boxed{u+G<9R_{\rm blk}\left\lceil\log_2(6R_{\rm blk})\right\rceil^2+100.}
\tag{10.1}
\]

構造上 P,W_* を同一導手に入れるが、純粋 growth では direct n-2 がより強い。

---

# 11. split Frey: aBg_0+bCh_0

\[
aBg_0+bCh_0=2^{v+1}W_*.
\]

U=aBg_0, V=bCh_0 とし

\[
d=\gcd(U,V)\in\{1,3\}.
\]

primitive full-2-torsion curve E_\Sigma を作る。

v\ge3 では

\[
\boxed{v_2(\Delta_{\Sigma,\min})=2v-6.}
\tag{11.1}
\]

5以上導手:

\[
\boxed{R_\Sigma=\operatorname{rad}_{p\ge5}(abBCPW_*).}
\tag{11.2}
\]

しかも

\[
\boxed{R_\Sigma=\operatorname{rad}_{p\ge5}(ab)\operatorname{rad}_{p\ge5}(BCP)\operatorname{rad}_{p\ge5}(W_*),}
\tag{11.3}
\]

三 support は pairwise disjoint。

判別式下界:

\[
\boxed{|\Delta_{\Sigma,\min}|>2^{u+G/3-16}.}
\tag{11.4}
\]

\[
\boxed{u+\frac G3<18R_\Sigma\left\lceil\log_2(6R_\Sigma)\right\rceil^2+202\qquad(v\ge3).}
\tag{11.5}
\]

特に十分大きい u で

\[
R_\Sigma>\frac{u}{36(\log_2u+4)^2}.
\]

v=1,2 も一般2-adic conductor bound f_2\le8 により

\[
\boxed{u+\frac G3<2304R_\Sigma\left\lceil\log_2(768R_\Sigma)\right\rceil^2+202.}
\tag{11.6}
\]

---

# 12. center Vieta dictionary

第一中心平方:

\[
Z_*:=\delta_1\gamma2^{G-2+2v}.
\]

\[
\boxed{Z_*^2-Z^2=TABC\,P\,W_*.}
\]

\[
AW_*+TBCP=2Z_*.
\]

したがって

\[
\boxed{\{Z_*-Z,Z_*+Z\}=\{AW_*,TBCP\}.}
\tag{12.1}
\]

後の大小評価で AW_*>TBCP が分かるので

\[
\boxed{AW_*=Z_*+Z,\qquad TBCP=Z_*-Z.}
\tag{12.2}
\]

第二中心平方:

\[
J=SBg_0,\qquad K=RCh_0.
\]

\[
J+K=\gamma2^{u-v},\qquad K-J=2C_{\rm cen}.
\]

\[
\boxed{\{\gamma2^{u-v-1}-C_{\rm cen},\gamma2^{u-v-1}+C_{\rm cen}\}=\{SBg_0,RCh_0\}.}
\tag{12.3}
\]

\[
\boxed{2\delta_1C_{\rm cen}=A(bCh_0-aBg_0).}
\tag{12.4}
\]

よって bCh_0>aBg_0。

注意: center squares を block/J split と独立 constraint として二重計上しない。

---

# 13. square branch results

第一中心を

\[
Y^2=A_o2^{u-1}+\delta_2q,\qquad A_o=\delta_2\gamma m
\]

と書く。

\[
\boxed{\delta_2q\ \text{square}}
\]

の枝は全 G で一様排除。

従って

\[
\operatorname{sf}(\delta_2q)\equiv1\pmod8,\qquad \operatorname{sf}(\delta_2q)\ge17.
\]

leading coefficient A_o2^{G-1} が平方なら枝ごとに

\[
2G-u\ge13,11,7,13.
\]

特に

\[
G<\frac{u+7}{2}
\]

なら leading coefficient nonsquare。

T square、特に T=1 では leading coefficient square は不可能。

未解決: 両係数 nonsquare の中心枝。

---

# 14. G と block radicals

T<2^{(G+1)/3} と direct n-1/n-2 を組み合わせる。

\[
R_1=R_{RS}R_T,\qquad R_2=R_{ABC}R_T,
\]
\[
R_T\le T.
\]

固定 c<3 で

\[
G\le c\log_2u+O(1)
\]

なら R_{RS},R_{ABC} は polynomial speed で増大する必要がある。

明示例:

\[
u\ge2^{214},\qquad G\le2\log_2u
\]

なら

\[
R_{ABC}>u^{1/4},\qquad R_{RS}>u^{1/4}.
\]

---

# 15. fresh-support bridge

\[
F=\prod_{\substack{p\ge5\\p\mid BCW_*\\p\nmid abP}}p.
\]

\[
\boxed{R_\Sigma=A_0VH\,F.}
\tag{15.1}
\]

\[
\boxed{F=\frac{R_\Sigma}{H\sqrt{A_0\mathcal Q}}.}
\tag{15.2}
\]

v\ge3 で

\[
\boxed{\sqrt{A_0}F>\frac{uT^2}{52\,2^{2G/3}(\log_2u+4)^2}.}
\tag{15.3}
\]

さらに

\[
\boxed{F>\frac{uT^{7/2}}{67\,2^{7G/6}(\log_2u+4)^2}.}
\tag{15.4}
\]

したがって G\le c\log_2u, c<6/7 なら fresh support は polynomial speed で発散。

---

# 16. B/C cube-depth

p^e\parallel B, r=v_p(g_0) とする。

\[
\boxed{v_p(n-j-2)=e,}
\]
\[
\boxed{v_p(\delta_1R-Ab)=e+r,}
\]
\[
\boxed{v_p(A^2ab+\delta_1)=e+r.}
\tag{16.1}
\]

C側は対称。

第一Freyから p が消える条件 3\mid r は

\[
v_p(A^2ab+\delta_1)-e\equiv0\pmod3
\]

という深い p-adic lifting condition に翻訳できる。

ただし単一素数の no-carry だけでは r mod 3 は禁止できない。局所例 X=p^r,Y=1,N=p^r+1 は任意 r で carry-free。

---

# 17. W_* を消した Kummer-block bridge

\[
F_{BC}=\prod_{\substack{p\ge5\\p\mid BC\\p\nmid P}}p,
\]
\[
F_{RS}=\prod_{\substack{p\ge5\\p\mid RS\\p\nmid abP}}p,
\]
\[
R_A=\operatorname{rad}_{p\ge5}(A).
\]

\[
\boxed{R_AF_{BC}>\frac{uT A_0^{2/3}}{13\,2^{2G/3}(\log_2u+4)^2}.}
\tag{17.1}
\]

\[
\boxed{A_0^{1/3}F_{RS}>\frac{uT}{13\,2^{2G/3}(\log_2u+4)^2}.}
\tag{17.2}
\]

掛け合わせて A_0 を消去:

\[
\boxed{R_AF_{BC}F_{RS}^{2}>\left(\frac{uT}{13\,2^{2G/3}(\log_2u+4)^2}\right)^3.}
\tag{17.3}
\]

\[
M_K=\max\{R_A,F_{BC},F_{RS}\}
\]

なら

\[
\boxed{M_K>\frac{(uT)^{3/4}}{7\,2^{G/2}(\log_2u+4)^{3/2}}.}
\tag{17.4}
\]

W_*,m,P,ab が完全に消え、actual Kummer blocks だけが残る。

---

# 18. BC-W_* exact identity と complement variable

\[
\boxed{Tx^2AW_*-\delta_1=BC(\delta A-T^2x^2P).}
\tag{18.1}
\]

\[
K_*:=\delta A-T^2x^2P.
\]

既知の \delta A>2T^2x^2P から

\[
\boxed{K_*>T^2x^2P>0.}
\tag{18.2}
\]

したがって AW_*>TBCP。

---

# 19. complement Frey: u-G direction

\[
K_*+T^2x^2P=\delta A.
\]

primitive full-2-torsion curve を作ると v\ge2 で

\[
\boxed{v_2(\Delta_{K,\min})=4v-8=u-G-8.}
\tag{19.1}
\]

さらに

\[
\boxed{|\Delta_{K,\min}|>2^{3(u-G)-16}.}
\tag{19.2}
\]

\[
\boxed{R_K=\operatorname{rad}_{p\ge5}(ATPK_*).}
\tag{19.3}
\]

\[
\boxed{u-G<6R_K\left\lceil\log_2(6R_K)\right\rceil^2+68.}
\tag{19.4}
\]

したがって R_K=o((u-G)/(\log(u-G))^2) は不可能。

現在は G,u,u+G,u-G の4方向を Frey curves で測れる。

# 20. shifted transition lemma

R/S/A/B/C では

\[
n=p^eN+r,\qquad j=p^eJ+s,
\]

シフトを残す。

\[
D=s_p(N),\qquad a=s_p(J).
\]

q odd prime, K\ge1（q=3なら K\ge2）、p\equiv1 mod q^K とする。

\[
R=(D+r)\bmod q^K,
\]
\[
A=(a+s)\bmod q^K,
\]
\[
B=(D-a+r-s)\bmod q^K.
\]

もし

\[
q\mid\binom{D+r}{3}
\]

かつ

\[
\boxed{R<A\ \text{or}\ R<B,}
\tag{20.1}
\]

なら別素数 q の carry が生じ、反例ではない。

各 block shift:

\[
R:(1,1),\ S:(1,0),\ A:(2,1),\ B:(2,0),\ C:(2,2).
\]

修正履歴: T-block 用 shift-free transition を Q2 等へそのまま適用した初期議論は不十分。以後すべて shifted version で再検証。

---

# 21. finite lifting ladder

固定 H に対し D<H の全 shifted patterns を殺す witness q^K を集め lcm を L_H とする。

検証済み:

| H | L_H の十進桁数 | prime bases | shifted splits |
|---:|---:|---:|---:|
| 50 | 17 | 12 | 2,646 |
| 100 | 31 | 20 | 11,521 |
| 200 | 58 | 32 | 48,021 |
| 500 | 128 | 60 | 307,521 |
| 1000 | 221 | 94 | 1,240,021 |

特に

\[
L_{1000}\mid\operatorname{ord}_p(2),\ p\mid R,S
\]

なら

\[
\boxed{s_p((n-1)/p^e)\ge1001.}
\tag{21.1}
\]

また

\[
L_{1000}\mid\operatorname{ord}_p(2),\ p\mid A,B,C
\]

なら

\[
\boxed{s_p((n-2)/p^e)\ge1000.}
\tag{21.2}
\]

これは p,u の有限探索ではなく、小さい digit-pattern certificate を無限個の大きい primes に持ち上げる結果。

さらに最初に carry が起きる witness level を取れば

\[
q^K\le D+r\le H+2.
\]

したがって

\[
\boxed{L_H\mid\operatorname{lcm}(1,2,\dots,H+2),}
\tag{21.3}
\]

\[
\boxed{\log L_H=O(H).}
\tag{21.4}
\]

---

# 22. multiscale smoothness sieve

\[
L_M=\operatorname{lcm}(1,3,5,\dots,M).
\]

代表的 barrier:

\[
315\mid\operatorname{ord}_p(2)
\]

なら

\[
D\ge11\ (R/S),\qquad D\ge10\ (A/B/C).
\]

\[
45045\mid\operatorname{ord}_p(2)
\]

なら

\[
D\ge17\ (R/S),\qquad \boxed{D\ge16\ (A/B/C)}.
\]

\[
4512611027925\mid\operatorname{ord}_p(2)
\]

なら

\[
D\ge41\ (R/S),\qquad D\ge40\ (A/B/C).
\]

訂正: 以前の Q2 で D\ge18 は shift を無視していた。正しくは D\ge16。

---

# 23. T=1, gamma=1: 全約数 Zsigmondy

\[
n=2^u.
\]

m>6、各 d\mid m, d>2,d\ne6 に primitive prime p_d を選べる:

\[
\operatorname{ord}_{p_d}(2)=d.
\]

異なる d は異なる prime。

\[
\Pi(m)=\prod_{\substack{d\mid m\\d>2,d\ne6}}p_d.
\]

p_d>d と全約数積公式から

\[
\boxed{\Pi(m)>\frac{m^{\tau(m)/2}}{12}.}
\tag{23.1}
\]

Q1 側 primitive primes は A_0,V,H,F_{RS} のどこか。
Q2 側は R_A,V,H,F_{BC} のどこか。

\[
\boxed{\Pi(u)\Pi(u-1)\mid A_0VH\,R_AF_{BC}F_{RS}.}
\tag{23.2}
\]

A_0VH<\kappa2^G なので

\[
\boxed{R_AF_{BC}F_{RS}>\frac{u^{\tau(u)/2}(u-1)^{\tau(u-1)/2}}{243\,2^G}.}
\tag{23.3}
\]

---

# 24. side-separated primitive support

Q1側:

\[
\boxed{F_{RS}>\frac{u^{\tau(u)/2}}{12\kappa\,2^G}.}
\tag{24.1}
\]

Q2側:

\[
\boxed{R_AF_{BC}>\frac{(u-1)^{\tau(u-1)/2}}{12\sqrt\kappa\,2^{G/2}}.}
\tag{24.2}
\]

Q2 は auxiliary absorption が P だけなので gap cost が 2^{G/2} しかない。

\[
M_K=\max\{R_A,F_{BC},F_{RS}\}.
\]

特に

\[
G=(1+o(1))\log_2u
\]

なら

\[
\boxed{M_K\ge u^{3/4-o(1)}.}
\tag{24.3}
\]

以前の u^{2/3-o(1)} を改善。

---

# 25. primitive order から exact digit residue

\[
\lambda_d=\operatorname{lcm}(d,2).
\]

Q1, d\mid u:

\[
\boxed{D_{1,d}=s_{p_d}((n-1)/p_d^{e_d})\equiv2^u-1\pmod{\lambda_d}.}
\tag{25.1}
\]

Q2, d\mid u-1:

\[
\boxed{D_{2,d}=s_{p_d}((n-2)/p_d^{e_d})\equiv2(2^{u-1}-1)\pmod{\lambda_d}.}
\tag{25.2}
\]

finite lifting の smoothness 条件なしで成立。

---

# 26. exponent の 2-adic part

2^a\mid u, a\ge2 なら order 2^a primitive prime が Q1 に入り

\[
D\equiv-1\pmod{2^a}.
\]

したがって

\[
\boxed{D\ge2^a-1.}
\tag{26.1}
\]

2^a\mid u-1 なら Q2 側で

\[
\boxed{D\ge2^a-2.}
\tag{26.2}
\]

---

# 27. odd-prime cofactor formula

\[
u=\ell t,\qquad \ell\ \text{odd prime}
\]

なら order \ell primitive prime で

\[
\boxed{D_{1,\ell}\equiv2^t-1\pmod{2\ell}.}
\tag{27.1}
\]

\[
u-1=\ell t
\]

なら

\[
\boxed{D_{2,\ell}\equiv2(2^t-1)\pmod{2\ell}.}
\tag{27.2}
\]

---

# 28. divisor-count 最小ケース

常に

\[
\tau(u)+\tau(u-1)\ge6.
\]

和=6 の場合、u\ge51 では奇数側=奇素数、偶数側=2\ell。

u が奇素数なら

\[
\boxed{\mathcal D\ge2u+1.}
\tag{28.1}
\]

u=2\ell なら

\[
\boxed{\mathcal D\ge u+3.}
\tag{28.2}
\]

一様に

\[
\boxed{\tau(u)+\tau(u-1)=6\Longrightarrow\mathcal D\ge u+3.}
\tag{28.3}
\]

和=7 の場合、可能性は偶数側=2\ell、奇数側=q^2。

\[
\boxed{\tau(u)+\tau(u-1)=7\Longrightarrow\mathcal D\ge2\sqrt u+1.}
\tag{28.4}
\]

ゆえに

\[
\boxed{\mathcal D<2\sqrt u+1\Longrightarrow\tau(u)+\tau(u-1)\ge8.}
\tag{28.5}
\]

---

# 29. low-digit + low-gap dichotomy

(23.3) と (28.5) より

\[
\boxed{\mathcal D<2\sqrt u+1\Longrightarrow R_AF_{BC}F_{RS}>\frac{(u-1)^4}{243\,2^G}.}
\tag{29.1}
\]

したがって

\[
\boxed{M_K>\frac{(u-1)^{4/3}}{243^{1/3}2^{G/3}}.}
\tag{29.2}
\]

特に

\[
G=(1+o(1))\log_2u
\]

なら

\[
\boxed{\mathcal D<2\sqrt u+1\Longrightarrow M_K\ge u^{1-o(1)}.}
\tag{29.3}
\]

つまり

\[
\boxed{\mathcal D\ge2\sqrt u+1\quad\text{or}\quad M_K\ge u^{1-o(1)}.}
\tag{29.4}
\]

actual Kummer blocks だけについての強い dichotomy。

---

# 30. support-digit conservation law

finite lifting certificate (H,L_H) を使うと

\[
\boxed{B_K>\frac{(u-1)^{(\tau(u)+\tau(u-1))/2}}{243\,2^G[L_H(u-1)]^{\mathcal D/(2H)}},}
\tag{30.1}
\]

\[
B_K=R_AF_{BC}F_{RS}.
\]

対数形:

\[
\boxed{\log_2B_K+G+\frac{\mathcal D}{2H}\log_2(L_H(u-1))>\frac{\tau(u)+\tau(u-1)}2\log_2(u-1)-\log_2243.}
\tag{30.2}
\]

ただし最新の強い読み: smooth primitive primes も support には残るので、support lower bounds と digit penalties は either/or ではなく同時に成立する。

---

# 31. prime-exponent special branches

T=gamma=1。

u-1=m が奇素数なら ABC=2^m-1 の全 prime p で ord_p(2)=m、よって p\ge2m+1=2u-1。

A,B,C は nontrivial pairwise coprime なので

\[
\boxed{\operatorname{rad}(ABC)\ge(2u-1)^3.}
\tag{31.1}
\]

u が奇素数なら

\[
\boxed{\operatorname{rad}(RS)\ge(2u+1)^2.}
\tag{31.2}
\]

さらに u-1=m prime, p^e\parallel ABC なら

\[
\boxed{s_p((n-2)/p^e)\ge2u,}
\tag{31.3}
\]

\[
\boxed{p^e\le\frac{2^{u-1}-1}{u}.}
\tag{31.4}
\]

u prime でも Q1 側に同様の bound。

---

# 32. fixed congruence route の限界

任意の固定 modulus L に対して、principal branch などで arbitrarily large v の congruence-compatible residues を作れる。

したがって fixed congruence accumulation だけでは growing G branch は排除できない。

最終解には moving primes / global support / elliptic curves / all-digit structure が必要。

---

# 33. descent の限界

simple descent は full-digit Kummer 条件を一般に保存しない。

既存稿で explicit finite counterexample と infinite family を確認済み。

低位 divisibility + one-prime all-digit だけから descent 後の full-digit preservation を仮定してはいけない。

---

# 34. cubic digit classification

非負係数 cubic digit polynomial の非自明例外族を完全分類。

唯一の非自明族:

\[
F_h=216h^3X^3+162h^2X^2+27hX+2,
\]

\[
J_h=72h^3X^3+78h^2X^2+23hX+2
\]

および補数。

この族は3進条件で全て排除。

次数3以下では末尾0,1,2の digit-polynomial 法がかなり強く使える。

---

# 35. digit polynomial -> prime-size upper bound

n の base-p expansion:

\[
n=F(p),\qquad H=s_p(n),\qquad m=\deg F.
\]

既存条件の下で

\[
\boxed{p\le6H(H+1)(H+2)^{2m+2}+2.}
\tag{35.1}
\]

適用条件:
- terminal digit 0 or 1
- terminal digit 2 で非零桁位置の v_2(r) が一定
- または m\le2 なら terminal digit 2 でも無条件

m\approx\log n/\log p を代入すると概念的に

\[
\log p\lesssim\sqrt{\log n\,\log H}
\]

型が期待できる。

未完成: actual moving block primes 全体へ積み上げて support lower bounds と衝突させる最終段階。

---

# 36. complete prime-power size bounds

Q2 complete prime power q について

\[
\boxed{q^2<2\delta_1\frac{(n-2)^2}{n-1}<2\delta_1n.}
\tag{36.1}
\]

したがって q<\sqrt{6n}。

Q1 complete prime powers には O(n^{2/3}) の明示上界。

単独では polynomial-in-u radical lower bound と直接矛盾しないが prime distribution を制約する。

---

# 37. D=n-2j identity

\[
D=n-2j.
\]

\[
\boxed{D^2+n(n-2)=4RSATx^2W_*.}
\tag{37.1}
\]

p\ge5,p\mid W_* で

\[
\left(\frac{-n(n-2)}p\right)=1.
\]

ただし既存平方類条件と同値で独立 constraint ではない。

---

# 38. 独立ではない結果の整理

二重計上しないもの:

1. 第一 center square と block split
2. 第二 center square と J-split
3. p\mid BCP の一部統一 Legendre 条件
4. beta-side center Legendre 条件
5. D^2+n(n-2) 由来の一部 W_* Legendre 条件

式変形・辞書としては有用。

---

# 39. 外部依存

1. Bang-Zsigmondy theorem: primitive prime divisor existence
2. von Känel 型 discriminant-conductor bound
3. von Känel-Matschke public complete elliptic-curve tables: small conductor exclusions

一般 growth bounds と外部 table completeness 依存の有限排除は分離して扱う。

---

# 40. computational certificates

一般命題へ持ち上がる有限証明書:

1. shifted transition H=50,100,200,500,1000
2. L_1000: 221 decimal digits, 94 odd prime bases
3. 1,240,021 shifted splits verified by integer arithmetic
4. multiscale odd-LCM smoothness barriers
5. cubic digit classification symbolic checks

これらは u や p を有限範囲で探索したのではなく、固定有限 patterns を証明書化したもの。

---

# 41. 主要修正履歴

**修正1**: T-block shift-free transition を Q2/R/S/A/B/C に直接使わない。shifted lemma を使用。

**修正2**: 45045 | ord_p(2) の Q2 digit barrier は D>=18 ではなく D>=16。R/S は D>=17。

**修正3**: center square と block/J split を独立条件として二重計上しない。

**修正4**: support-digit conservation を exclusive either/or と読むのは弱い。primitive support lower bounds と digit penalties は同時成立。

---

# 42. 現在の最強 picture

反例は同時に次を満たす必要がある:

- 第一Frey: \mathcal Q \not=o(u/\log^2u)
- center Frey: R_F \not=o(G/\log^2G)
- direct n-1: R_1 \not=o(u/\log^2u)
- direct n-2: R_2 \not=o(u/\log^2u)
- J-split: R_J \not=o((u-v)/\log^2(u-v))
- split Frey: R_\Sigma \not=o(u/\log^2u)
- complement Frey: R_K \not=o((u-G)/\log^2(u-G))
- pure-power cyclotomic support: actual Kummer blocks の support が divisor structure に応じて巨大化
- smooth primitive orders / large 2-adic exponent: full-digit complexity が巨大化

---

# 43. pure-power low-gap の現在最強結論

T=gamma=1,

\[
G=(1+o(1))\log_2u.
\]

side-separated primitive support から

\[
\boxed{M_K\ge u^{3/4-o(1)}.}
\]

さらに

\[
\mathcal D<2\sqrt u+1
\]

なら

\[
\boxed{M_K\ge u^{1-o(1)}.}
\]

したがって

\[
\boxed{\mathcal D\ge2\sqrt u+1\quad\text{or}\quad M_K\ge u^{1-o(1)}.}
\]

これは actual Kummer blocks A / BC / RS に対する現時点で最も強い圧縮の一つ。

---

# 44. 残っている本質的障害

巨大 radical 自体は contradiction ではない。Q1,Q2 は ~2^u なので polynomial-in-u radical はサイズ上は入る。

最終解へ必要なもの:

1. actual Kummer block radical M_K の global upper bound
2. full-digit no-carry と M_K growth の incompatible prime-distribution theorem
3. digit-polynomial prime-size bound を moving block primes 全体へ拡張
4. smooth/rough/order residues を全 support にわたり一斉に使う global sieve
5. center both-nonsquare branch の一様排除
6. full-digit を保存する新しい descent 構造

---

# 45. 次の最優先研究

## Priority 1: actual moving Kummer prime size vs digit height

既存

\[
p\le6H(H+1)(H+2)^{2m+2}+2
\]

と

\[
m\approx\frac{\log n}{\log p}
\]

を結合し、actual block primes の積 / radical upper bound を作る。

目標形:

\[
\log p\lesssim\sqrt{\log n\,\log H}.
\]

## Priority 2: Q2 side-separated support

Q2 auxiliary absorption は P だけで

\[
P<\sqrt\kappa2^{G/2}.
\]

R_AF_BC 側が特に強い。A/B/C の full-digit 条件を一体化する。

## Priority 3: center both-nonsquare branch

square branches は大きく排除済み。両係数 nonsquare が主要未解決枝。

## Priority 4: finite lifting の一般 H theorem 化

\[
L_H\mid\operatorname{lcm}(1,\dots,H+2),\qquad \log L_H=O(H).
\]

certificate 依存を減らして一般定理化。

---

# 46. 研究上の禁止事項

1. necessary condition を sufficient と呼ばない。
2. fixed-G finite を global finite と呼ばない。
3. fixed coefficient Pell/Siegel を moving coefficient 全体へ拡張しない。
4. fixed congruence accumulation だけで growing branch が消えたと主張しない。
5. center square と block/J split を二重計上しない。
6. finite table completeness 依存と一般数学証明を分離する。
7. computational certificate と一般 proof を区別する。
8. i=3 完全解決は全枝が閉じるまで言わない。

---

# 47. 主な生成済み研究ファイル

- `i3_third_frey_block_bridge_2026-09-21.md`
- `i3_split_frey_support_2026-09-21.md`
- `i3_fresh_support_bridge_2026-09-21.md`
- `i3_kummer_block_bridge_2026-09-22.md`
- `i3_cyclotomic_kummer_bridge_2026-09-22.md`
- `i3_complementary_frey_and_shifted_transition_2026-09-22.md`
- `i3_shifted_transition_L31_certificate.json`
- `i3_multiscale_cyclotomic_digit_sieve_2026-09-22.md`
- `i3_multiscale_shifted_transition_certificates.json`
- `i3_finite_lifting_ladder_2026-09-22.md`
- `i3_finite_lifting_moduli_H1000.json`
- `verify_i3_shifted_finite_lifting.py`
- `i3_support_digit_conservation_2026-09-22.md`
- `i3_side_separated_cyclotomic_support_2026-09-22.md`

GitHub repo の重要既存ファイル:

- `research/i3/i3_new_chat_integration_and_effective_gap_2026-09-21.md`
- `research/i3/i3_growing_gap_and_auxiliary_frey_2026-09-21.md`
- `research/i3/i3_gap_square_obstructions_2026-09-21.md`
- `research/i3/i3_global_digit_constraints_2026-09-19.md`
- `research/i3/i3_digit_reciprocity_and_W_continuation.md`
- `research/i3/i3_gap13_and_descent_continuation.md`
- `research/i3/i3_quadratic_twist_and_kummer_support_2026-09-21.md`
- `research/i3/i3_exact_gap_and_g9_continuation.md`
- `research/i3/i3_discriminant_support_and_elliptic_curve_2026-09-21.md`
- `research/i3/i3_cross_modulus_and_digit_height_2026-09-20.md`
- `research/i3/i3_cubic_digit_classification_2026-09-20.md`
- `research/i3/i3_prime_neighbor_powers_2026-09-20.md`
- `research/i3/i3_complement_digit_bounds_2026-09-20.md`
- `research/i3/i3_four_chat_integration_2026-09-21.md`
- `research/i3/i3_descent_kummer_obstruction_2026-09-20.md`
- `research/i3/i3_mixed_parameter_bound_2026-09-20.md`
- `research/i3/i3_finite_prime_obstruction_2026-09-20.md`
- `research/i3/i3_integrated_digits_and_center.md`

---

# 48. 最終ステータス表

| 項目 | 状態 |
|---|---|
| 六ブロック分解 | 紙上証明済み |
| full-digit Kummer table | 紙上証明済み |
| 第一Frey / cube-removal | 紙上証明済み + von Känel依存 |
| center gap Frey | 紙上証明済み |
| small conductor curve-table exclusion | 外部完全表依存 |
| direct n-1 / n-2 Frey | 紙上証明済み |
| J-split Frey | 紙上証明済み |
| block Frey | 紙上証明済み |
| split Frey | 紙上証明済み |
| split v=1,2 extension | 一般2-adic conductor bound依存 |
| complement Frey | 紙上導出済み、独立再監査推奨 |
| center Vieta dictionary | 紙上証明済み |
| delta_2 q square branch | 一様排除済み |
| fixed congruence obstruction | 証明済み |
| simple descent preservation failure | 証明済み |
| shifted transition lemma | 紙上証明済み |
| H=1000 finite lifting | 整数証明書あり |
| multiscale smoothness sieve | 整数証明書あり |
| all-divisor Zsigmondy support | Bang-Zsigmondy依存 |
| side-separated support bounds | 紙上導出済み |
| divisor-count low-digit dichotomy | 紙上導出済み |
| low-gap M_K >= u^(3/4-o(1)) | 紙上導出済み |
| low-digit + low-gap M_K >= u^(1-o(1)) | 紙上導出済み |
| center both-nonsquare | 未解決 |
| actual support の最終 upper bound | 未解決 |
| i=3 complete solution | **未解決** |

---

# 49. 一文で現在地

**現在の i=3 研究は、補助変数・固定合同・単純 descent への主要な逃げ道をかなり除去し、反例が存在するなら gap、複数Frey導手、actual Kummer block support、full-digit complexity、cyclotomic order のすべてを同時に巨大化させなければならない段階まで圧縮されている。最終障害は、その巨大 actual block support と full-digit no-carry を大域的に衝突させることである。**
