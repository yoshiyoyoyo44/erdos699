# Erdős Problem 699 — 2026-09-20 進捗総まとめ

## 0. 位置づけ

この文書は、Erdős Problem 699 のうち主に **i=3** に関して、2026-09-20 時点までの GitHub 既存成果と、このチャットで新たに得た進展を統合した引き継ぎメモである。

**重要:** i=3 全体も Problem 699 全体も未解決。以下では「既存 repo で確定」「このセッションで新たに導出」「撤回・要再監査」を区別する。

---

## 1. 既存 repo で確定している基盤

反例候補を仮定すると

\[
n=\gamma T2^u=TH,\qquad j=Tk,
\]

\[
Q_1=(n-1)/\delta_1=RS,\qquad Q=(n/2-1)/\delta_2=ABC,
\]

\[
(\gamma,\delta_1,\delta_2)\in\{(1,1,1),(1,1,3),(1,3,1),(3,1,1)\}.
\]

六ブロック \(A,B,C,R,S,T\) は奇数で pairwise coprime、また \(T\perp\gamma\delta_1\delta_2\)。

主要因子表示:

\[
k=SBg,\qquad j-1=RAa,\qquad H-k=RCh,\qquad n-j-1=SAb,
\]

\[
s=T^2gh,\qquad r_B=Tbh/2,\qquad r_C=Tag/2,
\]

\[
BCs-A^2ab=\delta_1.
\]

既存の重要結果:

- 反例なら \(u\ge49\)。
- 偶数 \(j\)、\(v=v_2(j)\) なら \(u\ge4v+14\)。
- \(A,B,C\ge11\)、\(R,S>1\)。
- 全平方枝は排除済み。
- 固定した \(w\)、固定した \(\lambda\)、固定 gap \(g=u-4v\) では候補有限。
- 全六ブロックに対する full-digit Kummer 条件が構成済み。
- 無限個の反例候補があるなら
  \[
  \frac{\min\{j,n/2-j\}}{n^{3/4}}\to\infty.
  \]
- exact center valuation:
  \[
  v_2(w-c_0)=4v+2,\qquad c_0=\delta_1^2\delta_2.
  \]

中心・添字側の整数:

\[
z^2=\delta_1^2+wQ,
\qquad
4c^2=n+2Q_1z,
\qquad c=n/2-j,
\]

\[
\rho=\frac{j(j-1)}{2Q_1},
\qquad
\rho(\rho-\delta_1)=\lambda Q.
\]

中心側には

\[
w=e_cf_c,
\qquad
Af_c-BCe_c=2\delta_1,
\qquad
\gcd(e_c,f_c)\mid\delta_1.
\]

また \(T\) は \(w-c_0\) の unitary divisor:

\[
T\mid w-c_0,
\qquad
\gcd\!\left(T,\frac{w-c_0}{T}\right)=1.
\]

---

## 2. 低次数の桁多項式ルートで得た進展

### 2.1 次数3

GitHub 既存成果で、末尾2・次数3の非自明な桁多項式を完全分類。例外族は整数値で共通素数3を強制されるため反例にならない。

### 2.2 次数4〜6でこのセッションに得たもの

このセッションでは次数4・5・6の桁多項式分類をかなり進めた。

- 次数4の 2+2 因子割当について、複数の枝が既知二次例外の合成へ落ちるか、整数値で \(2\bmod4\) に落ちる。
- 次数5では、主要な非自明族を導出し、resultant / 2進・3進条件から排除した枝がある。
- 次数6では、既知三次例外の二次合成や、新しい正係数六次族を導出し、後者は 3進 Kummer 障害で全整数値を排除した。

ただし、途中の \((2,2,2)\) balanced 枝では一度 \(B\mid J-1\) を落とした緩和系を解析していた。そこで得た「連続実数族」は **元の完全系の反例候補ではなく撤回**。その後、正しい系に戻して特殊枝を排除し、generic 枝を有理パラメータ化した。

この低次数分類は有用だが、**完全解決へ向けては有限次数を順に上げる戦略だけでは不十分**と判断し、以降は無限族全体を切る一様構造へ方針転換した。

---

## 3. このセッションで新たに得た「無限族向け」一様構造

### 3.1 中心側と添字側を結ぶ新合同式

添字側にも中心側と対応する全指数合同式を得た:

\[
\boxed{
4\lambda\equiv
-c_0\,j(j-1)\bigl(j(j-1)+2\bigr)
\pmod{n/2}
}
\]

これと \(u\ge4v+14\) を使うと、偶数 \(j\)、\(v=v_2(j)\ge2\) について

\[
\boxed{v_2(\lambda)=v-1}.
\]

中心側の既存 exact valuation

\[
v_2(w-c_0)=4v+2
\]

と合わせると、同じ \(v\) に対して中心側は4倍の2進精度、添字側は1倍の精度を持つ。

---

### 3.2 中心と添字を直接結ぶ積恒等式

\[
Z^2=\delta_1^2+wQ,
\qquad
R_0^2=\delta_1^2+4\lambda Q
\]

と置くと

\[
\boxed{
(w-4\lambda)Q
=(Z+2\rho-\delta_1)(Z-2\rho+\delta_1)
}.
\]

さらにブロック割当から

\[
\boxed{AC\mid Z-R_0},
\qquad
\boxed{B\mid Z+R_0}.
\]

したがって整数 \(u_0,v_0\) が存在して

\[
Z-R_0=ACu_0,
\qquad
Z+R_0=Bv_0,
\]

かつ

\[
\boxed{u_0v_0=w-4\lambda}.
\]

これは固定 \(w\)・固定 \(\lambda\) の有限性を別々に使うのではなく、両方を同時に扱える新しい構造。

---

### 3.3 添字側の積分解

既存の

\[
\rho=ABr_C,
\qquad Q=ABC,
\]

と \(Q\mid\rho(\rho-\delta_1)\) から

\[
E:=\frac{\rho-\delta_1}{C}\in\mathbb Z_{>0}
\]

と置けて

\[
\boxed{\lambda=r_CE},
\qquad
\gcd(r_C,E)\mid\delta_1.
\]

中心側の \(w=e_cf_c\) と対称な積分解になった。

---

### 3.4 新しい unitary-divisor 型量 q

\[
q:=\delta BC-Aab
\]

と置く。このとき

\[
\boxed{v_2(q)=2v}.
\]

さらに任意の \(p^e\parallel T\) に対して

\[
\boxed{v_p(q)=e}.
\]

したがって

\[
\boxed{
q=2^{2v}Tq_0,
\qquad q_0\text{ odd},
\qquad \gcd(T,q_0)=1.
}
\]

また \(g=2^vg_0,\ h=2^vh_0\) とすると

\[
\boxed{
Aq_0+BCTg_0h_0
=
\delta_1\gamma\,2^{u-1-2v}.
}
\tag{D1}
\]

右辺の奇数係数は許される分岐では1または3。

これは全反例候補を、指数が \(u-1-2v\) に下がった「1または3×2冪」の二項方程式へ送る一様な降下候補。

---

### 3.5 既存 unitary-divisor 量との第二の2冪方程式

既存の

\[
N_1:=ab+\delta_1\delta_2^2B^2C^2
\]

に対し

\[
\boxed{AN_1+q=\delta BC\,(n/2)}.
\]

ここから

\[
\boxed{v_2(N_1)=2v}.
\]

従って

\[
N_1=2^{2v}TN_0,
\qquad
\gcd(T,N_0)=1,
\qquad N_0\text{ odd}.
\]

さらに

\[
\boxed{\gcd(q_0,N_0)\mid3}.
\]

つまり同じ \(2^{2v}T\) が二つの独立した整数量に現れ、ほぼ互いに素な奇数商を持つ。

---

### 3.6 ロジスティック型降下候補

割り切る前の量

\[
\widehat H=\delta_1\gamma2^{u-1},
\qquad
\widehat k=BCTgh
\]

を取ると

\[
\boxed{\widehat H-\widehat k=A(q/T)}.
\]

しかも

\[
\boxed{
v_2(\widehat k)
=v_2(\widehat H-\widehat k)
=2v.
}
\]

比を元の \(n,j\) で書くと

\[
\boxed{
\frac{\widehat k}{\widehat H}
=
\frac{2j(n-j)}{n(n-1)}.
}
\]

したがって \(\theta=j/n\) に対して漸近的に

\[
\theta\mapsto2\theta(1-\theta)
\]

という logistic 型変換になる。

**未証明点:** この変換が full-digit Kummer 条件まで保存して「反例→反例」の真正な無限降下になることはまだ示せていない。既存 repo の旧降下案も、因子分割の再表現に留まり反復可能性は未証明だったため、ここが現在の核心。

---

## 4. 比 x,y,z の一様有理パラメータ化

既存の比

\[
x=\frac{s}{A},
\qquad y=\frac{r_B}{B},
\qquad z=\frac{r_C}{C},
\qquad \varepsilon=\frac{\delta_1}{Q}
\]

は

\[
x+y+z=\delta+\varepsilon,
\qquad
4yz=x(x-\varepsilon)
\]

を満たす。

\[
t=\frac{2y}{x}=\frac{Ab}{BTg}
\]

とすると

\[
\boxed{
x=
\frac{2t\delta+(2t+1)\varepsilon}{(t+1)^2}
}
\]

\[
\boxed{
y=
\frac{t\,[2t\delta+(2t+1)\varepsilon]}
{2(t+1)^2}
}
\]

\[
\boxed{
z=
\frac{2\delta-t\varepsilon}
{2(t+1)^2}
}.
\]

対称に

\[
t'=\frac{2z}{x}=\frac{Aa}{CTh}
\]

と置くと

\[
\boxed{tt'=1-\frac{\delta_1}{BCs}<1}.
\]

また \(j<n/2\) から \(y>z\)、既存の \(\delta A>2s\) と合わせて

\[
\boxed{t>1>t'>0}.
\]

この一様パラメータ化は、有限係数分類を使わず無限族全体を1変数で圧縮する重要候補。

---

## 5. 指数とともに増大する2進合同式

上の比表示から、次の恒等式を得た:

\[
\boxed{
\delta_1R^2Ch-Bg=AbH
}
\]

\[
\boxed{
\delta_1S^2Bg-Ch=AaH
},
\qquad H=\gamma2^u.
\]

\(g=2^vg_0,\ h=2^vh_0\) とすれば

\[
\boxed{
Bg_0\equiv\delta_1R^2Ch_0
\pmod{2^{u-v}}
}
\]

\[
\boxed{
Ch_0\equiv\delta_1S^2Bg_0
\pmod{2^{u-v}}
}.
\]

固定した mod 8,16 などではなく、法そのものが \(2^{u-v}\) と指数に応じて発散する。

既存 repo では、固定有限個の合同式では一般 gap を排除できない無限局所解があることが証明されているため、この「指数依存の高精度合同式」は完全解決に向けて重要。

---

## 6. 三次 Bernstein / Krawtchouk 型整数成分

全反例で次の4つは正整数になる:

\[
X_3=\frac{j(j-1)(j-2)}{Q_1Q},
\]

\[
X_2=\frac{3j(j-1)(n-j)}{Q_1Q},
\]

\[
X_1=\frac{3j(n-j)(n-j-1)}{Q_1Q},
\]

\[
X_0=\frac{(n-j)(n-j-1)(n-j-2)}{Q_1Q}.
\]

和は

\[
\boxed{X_0+X_1+X_2+X_3=2\delta n}.
\]

偶数 \(j\)、\(v=v_2(j)\) なら exact valuation:

\[
\boxed{v_2(X_0)=v_2(X_3)=v+1},
\]

\[
\boxed{v_2(X_1)=v_2(X_2)=2v}.
\]

交代和

\[
K=X_0-X_1+X_2-X_3
\]

は

\[
K=
\frac{4\delta c(4c^2-3n+2)}{(n-1)(n-2)}
\]

で、

\[
\boxed{v_2(K)=v+2}.
\]

さらに \(T\mid K\)。したがって新しい一様下界

\[
\boxed{
c^3>
\frac{2^{v-2}T}{\delta}(n-1)(n-2)
}
\]

を得る。

これは有限探索に依存しない。

---

## 7. gap に関する無限族の圧縮

既存 exact-gap 理論と上の新しいサイズ評価から、固定した

\[
d=u-4v
\]

ごとの候補は有限。

従って無限個の偶数 \(j\) 反例候補が存在するなら

\[
\boxed{u-4v_2(j)\to\infty}.
\]

既存の端点有限性と合わせると、無限列なら同時に

\[
\boxed{
\frac{\min\{j,n/2-j\}}{n^{3/4}}\to\infty
}
\]

も必要。

つまり無限族の逃げ道は、gap も中心距離・添字距離も同時に巨大化する領域へ押し込められている。

---

## 8. 修正・撤回しておく点

1. 次数6 balanced \((2,2,2)\) 解析の途中で、\(B\mid J-1\) を落とした緩和系を一時解析していた。その「連続実数族」は元の反例系ではない。撤回。
2. その後、正しい完全系へ戻して特殊枝を排除し、generic 枝を有理パラメータ化したが、完全分類は未完了。
3. \(v_2(w-c_0)=4v+2\) はこのセッションでも再導出したが、GitHub の exact-gap 稿ですでに証明済み。新規結果として数えない。
4. 過去の BBM / p-adic logarithm を用いた一部の数値上界は repo 自身で撤回・要再監査になっているため、完全解決の根拠として使わない。
5. GitHub への書き込みは接続権限403のため、このセッションでは直接反映できなかった。

---

## 9. 現在地

2026-09-20 の最重要な変化は、研究方針を

> 低次数・有限候補を順番に潰す

から

> 反例が存在すると仮定したとき全指数で必ず成立する、高精度2進合同・unitary divisor・有理比圧縮・降下構造を使って無限族そのものを潰す

へ切り替えたこと。

現時点では完全解決ではないが、特に

\[
Aq_0+BCTg_0h_0=\delta_1\gamma2^{u-1-2v},
\]

\[
q=2^{2v}Tq_0,
\]

\[
t>1>t',\qquad tt'=1-\frac{\delta_1}{BCs},
\]

\[
Bg_0\equiv\delta_1R^2Ch_0\pmod{2^{u-v}},
\]

\[
Ch_0\equiv\delta_1S^2Bg_0\pmod{2^{u-v}}
\]

の5本が、完全解決へ向けた現在の主要な新しい道具。

