# Erdős Problem 699 — i=3 研究進捗総まとめ

更新日: 2026-09-18

## 0. 位置づけ

この文書は、Erdős Problem 699 のうち **i=3** に関する現時点の研究進捗を、GitHub リポジトリ `yoshiyoyoyo44/erdos699` の既存成果と、このチャットで新たに得た進展をまとめた引き継ぎ用ノートである。

**重要:** i=3 は未解決。Problem 699 全体も未解決。この文書は完全解決を主張しない。

保証レベルは以下で区別する。

- **[PROVED / repo]**: 既存 repo に証明または再生可能な検算がある。
- **[PROVED / session]**: このセッションで紙上導出がかなり明確で、既存式だけから従う。まだ repo に保存していない。
- **[COMPUTED]**: 整数演算などの有限検査で確認したが、証明書を repo に保存していない。
- **[WORKING]**: 有力な作業結果だが、定数処理や一般条件の再監査が必要。
- **[RETRACTED]**: 一度出したが、そのまま証明として使ってはいけない。

---

# 1. 既存の i=3 正規化と基盤

[PROVED / repo]

反例候補があると仮定して

\[
n=\gamma T2^u=TH,\qquad j=Tk,
\]

\[
Q_1=(n-1)/\delta_1=RS,\qquad Q_2=(n/2-1)/\delta_2=ABC,
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
T^2BCgh-A^2ab=\delta_1,
\]

\[
\delta_1R=Ab+TBg,\qquad \delta_1S=Aa+TCh.
\]

既存の基本下界:

\[
u\ge49,
\]

\[
A,B,C\ge11,
\]

偶数 \(j\) では

\[
u\ge4v_2(j)+14.
\]

また

\[
A>\frac{2T^2}{\delta},\qquad
B\ge\frac{T+1}{\delta},\qquad
C>\frac{4T}{\delta},\qquad \delta=\delta_1\delta_2.
\]

さらに

\[
R>\frac{3T^2+T}{\delta_1^2\delta_2},\qquad
S>\frac{6T^2}{\delta_1^2\delta_2}.
\]

既存の中心変数 \(c=n/2-j\)、および中心の整数 \(w\) には

\[
4c^4>wQQ_1^2
\]

や

\[
w\equiv\delta_1^2\delta_2(1-4c^4)\pmod{n/2}
\]

などの制約がある。

---

# 2. repo ですでに確定している i=3 の主成果

[PROVED / repo]

- 全平方枝 \(j(n-j)/(n-1)\) が平方になる場合は全 \(M\) で排除済み。
- \(u\le48\) の有限範囲を完全検証し、反例なら \(u\ge49\)。
- \(A,B,C\ge11\)。
- 任意の固定 \(F\) に対して \(\min(A,B,C)\le F\) の候補は有限。
- 固定した中心 \(w\)、固定した \(\lambda\)、固定した gap \(g=u-4v_2(j)\) などの有限性結果。
- 偶数 \(j\) について \(u\ge4v_2(j)+14\)。
- T-block を含む full-digit Kummer 条件が factor block 形式に展開されている。

T-block の carry-free 加法:

\[
USB g+URC h=UH
\]

ここで \(p^e\parallel T\)、\(U=T/p^e\)。

base-\(p\) 桁和で

\[
s_p(USB g)+s_p(URC h)=s_p(UH).
\]

動的 prefix forcing:

\[
\lambda_T=v_p(UH-1)>0
\]

なら

\[
p^{\lambda_T}\text{ は }g,h\text{ のちょうど一方を割る}.
\]

\[
\Pi_T:=\prod_{p^e\parallel T,\lambda_T>0}p^{\lambda_T}\mid gh.
\]

偶数 \(j\)、\(x=2^{v_2(j)}\) では

\[
2T^2x^2\Pi_T<\delta A.
\]

全ブロック積では

\[
4T^2 2^{e_2}\Pi<\delta^2BC,
\]

偶数 \(j\) なら \(e_2=2v_2(j)\)。

---

# 3. prime-power / digit-sum-4 枝の研究

## 3.1 基本設定

T-block の一つの素数冪枝:

\[
T=p^e,
\]

偶数 \(j\) で base-\(p\) 桁和4を仮定すると、スパース表示は

\[
2^u=1+p^r+p^\beta+p^{\beta+s}
\]

の形になる。

\[
a=r-\beta>0
\]

と置けば

\[
\boxed{\frac{2^u-1}{p^\beta}=1+p^a+p^s.}
\]

また

\[
\beta=v_p(2^u-1).
\]

---

## 3.2 v2(j)>=2 の quadratic-character obstruction

[PROVED / session]

\(v=v_2(j)\ge2\)、\(T=p^e\)、桁和4とする。

既存 sparse branch から \(r,s\) は奇数。任意の \(\ell\mid Q_1\) について \(p^m\equiv-1\pmod\ell\)（\(m\) odd）となるため

\[
\left(\frac p\ell\right)=\left(\frac{-1}{\ell}\right).
\]

\(p\equiv3\pmod4\) と quadratic reciprocity から

\[
\left(\frac\ell p\right)=1.
\]

ゆえに

\[
\left(\frac{Q_1}{p}\right)=1.
\]

ところが

\[
Q_1\equiv-\delta_1^{-1}\pmod p
\]

なので

\[
\left(\frac{-\delta_1}{p}\right)=1.
\]

\((-1/p)=-1\) より

\[
\boxed{\delta_1=3.}
\]

帰結:

- \(\gamma=3\) branch は \((\gamma,\delta_1,\delta_2)=(3,1,1)\) しかないため矛盾。
- \(\gamma=1\) なら \((1,3,1)\) に限られる。
- \(v=2\) だと \(p=3\) だが \(T\perp\delta_1=3\) に反する。

よって digit-sum-4 / prime-power の \(v\ge2\) は極めて細い Mersenne 型 branch に落ちる。

---

## 3.3 Mersenne congruences

[PROVED / session]

残存 Mersenne branch では

\[
p=2^v-1.
\]

スパース式から

\[
v-1\mid u-2.
\]

さらに \(b>0\) なら

\[
v\mid u,
\]

\(b=0\) なら

\[
v\mid u-1.
\]

したがって

\[
b>0\Rightarrow u\equiv2v\pmod{v(v-1)},
\]

\[
b=0\Rightarrow u\equiv v+1\pmod{v(v-1)}.
\]

---

# 4. v2(j)=1 の最後の digit-sum-4 枝

## 4.1 残存形

既存・セッション結果を統合すると、難しい枝は

\[
v_2(j)=1,
\]

\[
\gamma=1,
\]

\[
T=p^e,
\]

\[
p\equiv5\pmod8,
\]

\[
2^u=1+p^r+p^\beta+p^{\beta+s}.
\]

\[
a=r-\beta>0.
\]

そして

\[
\frac{2^u-1}{p^\beta}=1+p^a+p^s.
\]

---

## 4.2 exact beta formula

[PROVED / session]

\[
\operatorname{ord}_p(2)=4h,
\]

\(h\) odd、\(h\mid U_0\)、\(u=2^tU_0\) とする。

\[
2^{2h}\equiv-1\pmod p.
\]

よって

\[
\boxed{\beta=v_p(2^{2U_0}+1)}
\]

および LTE から

\[
\boxed{\beta=v_p(2^{2h}+1)+v_p(U_0/h)}.
\]

特に

\[
\boxed{p^\beta\mid2^{2U_0}+1}
\]

なので

\[
\boxed{p^\beta\le2^{2U_0}+1.}
\]

---

## 4.3 exact local valuations

[PROVED / session]

\[
C:=\frac{2^u-1}{p^\beta}=1+p^a+p^s.
\]

残存 branch では

\[
\boxed{v_3(C)=1+v_3(U_0)}.
\]

また \(p\ne5\) なら

\[
\boxed{v_5(C)=1+v_5(U_0)}.
\]

---

## 4.4 strong residue elimination

[PROVED / session]

\(p\ne5\) なら

\[
\boxed{p\equiv13\pmod{48}}.
\]

さらに mod 5 条件から

\[
p\equiv2\text{ or }3\pmod5.
\]

CRT で

\[
\boxed{p\equiv13\text{ or }157\pmod{240}.}
\]

さらに指数類:

- \(p\equiv157\pmod{240}\)（\(p\equiv2\pmod5\)）なら

\[
(a,s)\bmod4\in\{(0,3),(1,1),(3,0)\}.
\]

- \(p\equiv13\pmod{240}\)（\(p\equiv3\pmod5\)）なら

\[
(a,s)\bmod4\in\{(0,1),(1,0),(3,3)\}.
\]

---

## 4.5 p=5 branch

[WORKING / partially checked]

\(p=5\) では

\[
\operatorname{ord}_5(2)=4,
\]

\[
\boxed{\beta=1+v_5(U_0)}.
\]

さらに parity から \(\beta\) odd、\(a,s\) even。

この枝は有限探索と BBM を組み合わせて完全排除できるという作業結果が出たが、BBM 定数処理の一部をその後再監査したため、**repo に正式保存するまでは完全排除として固定しない**。

安全に維持できるのは exact beta と parity 制約。

---

# 5. BBM / p-adic logarithm 関連の扱い

## 5.1 参照定理

Bennett–Bugeaud–Mignotte,
“Perfect powers with few binary digits and related Diophantine problems, II”
の Theorem 6 / 7 を参照。

Theorem 6 の形自体は原論文で確認済み。

## 5.2 要注意・撤回済み

[RETRACTED]

以下を **確定結果として使ってはいけない**:

- 初期の \(t\le12\) の導出。
- 後に一度「修正済み」とした \(t\le12\) の一部。
- Theorem 7 を用いた \(B\le20\)、\(B\le6\) などの強い境界。

理由: Theorem 7 の条件 (2.3) およびパラメータ被覆を十分厳密に扱えていない箇所があった。

[WORKING]

- Theorem 6 を安全側に使うことで \(B\) を有限範囲へ圧縮できる可能性は高い。
- 符号付き \(\alpha_1=-2^{d/2}\) は定理上 admissible で、定数改善に使える。
- ただし最終的な数値境界は、区間演算の完全証明書を作るまで未確定。

---

# 6. 一般 T に対する新しい low-digit-sum 定理

ここからが、このチャットで得た最も重要な一般化。

## 6.1 digit sum 4 または 6 の素因数は高々1個

[PROVED / session]

偶数 \(j\)、\(v=v_2(j)\ge2\)。\(p^e\parallel T\)、\(U=T/p^e\)。

\[
X=Uk,\qquad Y=U(H-k).
\]

carry-free なので

\[
s_p(X)+s_p(Y)=s_p(UH).
\]

### digit sum 4

既存 repo で、桁和4なら各 summand が桁和2、\(p\equiv3\pmod4\)、かつ他の全素因数 \(\ell\mid U\) に対して

\[
\left(\frac\ell p\right)=1.
\]

よって2つの素数が同時に桁和4を取ることは quadratic reciprocity に反する。

### digit sum 6

桁和6なら summand の桁和分解は \((2,4)\) または \((4,2)\)。

桁和2側は

\[
p^a(p^r+1)
\]

型。

\(v\ge2\) なので \(r\) odd、\(p\equiv3\pmod4\)。

他の \(\ell\mid U\) について

\[
p^r\equiv-1\pmod\ell
\]

より

\[
\left(\frac\ell p\right)=1.
\]

したがって digit sum 4 と6を合わせて

\[
\boxed{
\#\{p\mid T:s_p(\gamma2^uT/p^{v_p(T)})\le6\}\le1
\qquad(v_2(j)\ge2).
}
\]

これは有限探索ではない一般結果。

---

## 6.2 v2(j)=1 の digit sum 6

[PROVED / session]

\(v_2(j)=1\)、\(\omega(T)\ge2\) では既存結果により桁和4は不可能。

桁和6の素数 \(p\) があるなら \(p\equiv3\pmod4\)。桁和2側の指数は今度は even となり、他の全 \(\ell\mid U\) について

\[
4\mid\operatorname{ord}_\ell(p),
\]

従って

\[
\ell\equiv1\pmod4.
\]

よって桁和6の素数も高々1個。

---

# 7. 一般 2-adic digit-sum lower bound

[PROVED / session]

\(v=v_2(j)\ge1\)、\(p^e\parallel T\)。

\[
X=Uk,\qquad Y=U(H-k)
\]

では

\[
v_2(X)=v_2(Y)=v.
\]

任意の整数 \(Z\) について

\[
Z\equiv s_p(Z)\pmod{p-1}.
\]

\[
m_p:=\min\{v,v_2(p-1)\}
\]

とすると

\[
2^{m_p}\mid s_p(X),\qquad 2^{m_p}\mid s_p(Y).
\]

両者正なので

\[
\boxed{
s_p\!\left(\gamma2^uT/p^{v_p(T)}\right)
\ge
2^{1+\min(v_2(j),v_2(p-1))}.
}
\]

例: \(v_2(j)\ge4\) なら

- \(p\equiv3\pmod4\): 下界4
- \(p\equiv5\pmod8\): 下界8
- \(p\equiv9\pmod{16}\): 下界16
- \(p\equiv1\pmod{16}\): 下界32

---

# 8. weighted digit-sum lower bound

[PROVED / session]

\(v_2(j)\ge2\) では、digit sum \(\le6\) の素数は高々1個。

したがって

\[
\boxed{
\sum_{p\mid T}s_p\!\left(\gamma2^uT/p^{v_p(T)}\right)
\ge8\omega(T)-4.
}
\]

さらに \(v_2(p-1)\ge3\) の素数について一般2-adic下界を追加すると

\[
\boxed{
\sum_{p\mid T}s_p(UH)
\ge
8\omega(T)-4+
\sum_{\substack{p\mid T\\v_2(p-1)\ge3}}
\left(2^{1+\min(v,v_2(p-1))}-8\right).
}
\]

これは今後、一般 \(T\) の size inequality と結ぶための重要な weighted bound。

---

# 9. p+1 / alternating digit-sum 補題

[PROVED / session]

base-\(p\) 交代桁和

\[
A_p(Z)=\sum_i(-1)^id_i
\]

を用いると

\[
Z\equiv A_p(Z)\pmod{p+1},
\]

\[
|A_p(Z)|\le s_p(Z).
\]

\[
w=v_2(p+1),\qquad v=v_2(Z)
\]

とする。

### Case w>v

\[
\boxed{s_p(Z)\ge2^v.}
\]

### Case w<=v

\[
\boxed{
p+1\mid Z
\quad\text{または}\quad
s_p(Z)\ge2^w.
}
\]

T-block の \(X,Y\) に適用する。

\[
\gcd(X,Y)=U2^v\varepsilon,
\qquad \varepsilon\in\{1,3\}.
\]

\[
m=(p+1)/2^w.
\]

もし

\[
m\nmid U\varepsilon
\]

なら両方を \(p+1\) が割ることはできないので

\[
\boxed{s_p(UH)\ge2^w+2.}
\]

---

# 10. T の最小素因数に対する Mersenne 型分類

[PROVED / session]

\(p\) を \(T\) の最小素因数とする。

\[
m=\frac{p+1}{2^{v_2(p+1)}}<p.
\]

もし低桁和条件から

\[
m\mid U\varepsilon
\]

が必要なら、\(U\) の素因数は全て \(p\) より大きいので

\[
m\mid\varepsilon.
\]

\(\varepsilon\in\{1,3\}\) だから

\[
\boxed{m=1\text{ or }3.}
\]

すなわち

\[
\boxed{
p=2^w-1
\quad\text{or}\quad
p=3\cdot2^w-1,
\qquad w=v_2(p+1).
}
\]

これは低桁和8以下の \(p\equiv7\pmod8\) branch に特に強く効く。

---

# 11. digit-sum-8 の分類

## 11.1 基本

\(v=v_2(j)\ge3\) とする。

一般2-adic桁和下界から

\[
s_p(UH)=8
\]

なら

\[
v_2(p-1)\le2.
\]

従って

\[
\boxed{p\not\equiv1\pmod8.}
\]

候補は

\[
p\equiv3,5,7\pmod8.
\]

---

## 11.2 p≡5 mod8

[PROVED / session]

\(p\equiv1\pmod4\) なので各 summand の桁和は4の倍数。

総桁和8なら

\[
\boxed{(s_p(X),s_p(Y))=(4,4).}
\]

つまり必ず balanced。

---

## 11.3 p≡7 mod8, unbalanced

[PROVED / session]

桁和8が \((2,6)\) または \((6,2)\) なら、桁和2側は

\[
p^a(p^r+1)
\]

で、\(r\) odd。

他の任意の \(\ell\mid U\) に対して

\[
\boxed{\left(\frac\ell p\right)=1.}
\]

---

## 11.4 p≡7 mod8, balanced

[PROVED / session]

balanced \((4,4)\) なら \(w=v_2(p+1)\le v\)。

交代桁和の絶対値は高々4で、\(2^w\mid A_p(X),A_p(Y)\)、\(w\ge3\) だから

\[
A_p(X)=A_p(Y)=0.
\]

従って

\[
\boxed{p+1\mid X,Y.}
\]

よって

\[
\boxed{
\frac{p+1}{2^{v_2(p+1)}}\mid U\varepsilon.
}
\]

最小素因数なら前節の Mersenne 型分類へ落ちる。

---

# 12. digit-sum-8 balanced から中心 c への divisibility

ここはこのセッションで得た重要な「digit sum -> center」の橋。

[PROVED / session, but manuscript 前に再監査推奨]

\[
c=n/2-j.
\]

balanced \((4,4)\) で \(p\equiv5\) または \(7\pmod8\) の場合、base-\(p\) の parity split / alternating digit argument から

\[
X\equiv Y\pmod{p^2-1}.
\]

ところが

\[
X-Y
=U(2k-H)
=-\frac{2c}{p^e}.
\]

したがって

\[
\boxed{
\frac{p^2-1}{2}\mid\frac{c}{p^e}.
}
\]

これは初めて

\[
\text{low digit sum}\to\text{中心 }c\text{ の巨大な明示因子}
\]

を与える。

今後はこれを

\[
4c^4>wQQ_1^2
\]

や

\[
w\equiv\delta_1^2\delta_2(1-4c^4)\pmod{n/2}
\]

と結合するのが有力。

---

# 13. pure-power Mersenne / digit-sum-8 branch

[PROVED / session, local branch]

\(T=p^e\)、\(p=2^w-1\)、digit sum 8 の Mersenne 側。

center-side congruence から

\[
\gamma2^{u-w-2}\equiv1\pmod{2^{w-1}-1}.
\]

\(\gamma=3\) は不可能。

従って

\[
\boxed{\gamma=1.}
\]

また \(2\) の mod \(2^{w-1}-1\) order は \(w-1\) なので

\[
\boxed{u\equiv3\pmod{w-1}.}
\]

さらに units digit から

\[
u\bmod w\in\{0,1,2\}.
\]

CRT で

\[
\boxed{
u\equiv3w,\quad2w+1,\quad w+2
\pmod{w(w-1)}.
}
\]

既存 \(u\ge4v+14\)、\(v\ge w\) を合わせると

\[
\boxed{u\ge w^2+2.}
\]

---

# 14. 「digit sum -> Pi_T」は直接には成立しない

[IMPORTANT NEGATIVE RESULT]

桁和が大きいことだけから \(\Pi_T\) が大きいとは言えない。

理由:

\[
\lambda_T=v_p(UH-1)
\]

は base-\(p\) の最下位 prefix が1になることに依存し、総桁和の大きさだけでは下から制御できない。

したがって今後は

\[
\text{digit sum}
\to p\pm1\text{ / order / center divisibility}
\]

を使う方が有望。

---

# 15. 有限計算について

[COMPUTED / not yet archived]

このセッション中に、prime-power digit-sum-4 branch について複数の有限 modular scan を行った。

ただし一部の走査では後から「\(B\equiv B_0\pmod p\) の複数代表を全て見る必要がある」というバグを発見し修正した。

そのため、有限探索の数値境界は **repo に証明書として保存するまでは主定理に使わない**。

安全に引き継ぐべきなのは、有限探索そのものより、上記の一般合同式・桁和補題・quadratic reciprocity 構造。

---

# 16. 撤回・要再監査リスト

次の主張は、今後のAIが誤って前提にしないこと。

1. **BBM だけで \(t\le12\) が確定** — そのままでは不可。
2. **Theorem 7 で \(B\le20\)** — 未確定。
3. **Theorem 7 で \(B\le6\)** — 未確定。
4. **Mersenne v>=2 digit-sum-4 を完全排除** — 中間の BBM/Hensel 定数処理を再監査するまで確定扱いしない。
5. **p=5 branch 完全排除** — 有力な有限化＋探索結果はあるが、BBM 定数監査が必要。
6. `i3_all_square_branches.md` は \(T\) や \(n\) が平方という意味ではない。対象は
   \[
   L=j(n-j)/(n-1)
   \]
   が整数平方となる branch。

---

# 17. 現在もっとも信頼できる新成果

優先順でまとめる。

### A. digit sum <=6 は高々1素数

\[
\boxed{
\#\{p\mid T:s_p(\gamma2^uT/p^{v_p(T)})\le6\}\le1
\quad(v_2(j)\ge2).
}
\]

### B. 一般2-adic digit-sum lower bound

\[
\boxed{
s_p(\gamma2^uT/p^{v_p(T)})
\ge2^{1+\min(v_2(j),v_2(p-1))}.
}
\]

### C. weighted sum lower bound

\[
\boxed{
\sum_{p\mid T}s_p(UH)
\ge8\omega(T)-4+
\sum_{v_2(p-1)\ge3}
(2^{1+\min(v,v_2(p-1))}-8).
}
\]

### D. p+1 alternating-digit forcing

低桁和なら

\[
\frac{p+1}{2^{v_2(p+1)}}\mid U\varepsilon
\]

が頻繁に強制され、最小素因数では

\[
\boxed{p=2^w-1\text{ or }3\cdot2^w-1.}
\]

### E. digit-sum-8 balanced -> center divisibility

\[
\boxed{
\frac{p^2-1}{2}\mid\frac c{p^e}.
}
\]

### F. prime-power digit-sum-4 の clean residue theorem

\[
\boxed{p\ne5\Rightarrow p\equiv13\text{ or }157\pmod{240}.}
\]

---

# 18. i=3 を完全に閉じるために残っている大物

1. **一般 non-square branch** 全体。
2. odd \(j\) branch。
3. \(T=1\) branch の完全処理。
4. multi-prime \(T\) で digit sum 8 以上が多数出る場合を global size contradiction へ変換すること。
5. prime-power digit-sum-4 の最後の枝を完全に閉じること。
6. weighted digit-sum lower bound と
   \[
   4T^2 2^{2v}\Pi<\delta^2BC
   \]
   の間を、\(\Pi\) を経由せず center/order/size でつなぐこと。

---

# 19. 次に最も有望な研究方向

## Direction 1 — center divisibility を使う

新しい

\[
\frac{p^2-1}{2}\mid\frac c{p^e}
\]

を

\[
4c^4>wQQ_1^2
\]

および

\[
w\equiv\delta_1^2\delta_2(1-4c^4)\pmod{n/2}
\]

に入れ、digit-sum-8 balanced branch を一般 \(T\) で排除する。

## Direction 2 — multiple low-digit primes の incompatibility

- digit sum4/6 は高々1個。
- digit sum8 は residue class と balanced/unbalanced に分類。
- 最小素因数は Mersenne / 3×Mersenne 型へ落ちる。

これらを複数素因数間の reciprocity / order 条件で衝突させる。

## Direction 3 — weighted digit-sum lower bound を size へ変換

直接 \(\Pi_T\) へは行かない。

代わりに

- \(p-1\), \(p+1\) の巨大因子
- \(p^2-1\mid c\)
- sparse polynomial divisibility
- center curve

を使う。

## Direction 4 — prime-power digit-sum-4 最終枝

clean に残っている条件:

\[
p=5\text{ または }p\equiv13,157\pmod{240},
\]

\[
\beta=v_p(2^{2U_0}+1),
\]

\[
v_3(C)=1+v_3(U_0),
\]

\[
v_5(C)=1+v_5(U_0)\quad(p\ne5).
\]

この枝は BBM 定数に依存しすぎず、local valuation + order + finite certificates で閉じる方が安全。

---

# 20. repo で参照すべき主ファイル

- `STATUS_AND_DIRECTIONS.md`
- `i3_digit_reciprocity_and_W_continuation.md`
- `source_i3_full_digit_kummer_2026-09-14.md`
- `i3_integrated_digits_and_center.md`
- `i3_nonsquare_merged_continuation.md`
- `i3_boundary_and_fixed_blocks.md`
- `i3_direct_center_and_endpoint_curves.md`
- `i3_exact_gap_and_g9_continuation.md`
- `i3_gap13_and_descent_continuation.md`
- `i3_all_square_branches.md`

---

# 21. 最終ステータス

**i=3 はまだ未解決。**

しかしこのセッションで、特に一般 \(T\) に対して

\[
\boxed{\text{桁和4/6の希少性}}
\]

\[
\boxed{\text{2-adic桁和下界}}
\]

\[
\boxed{\text{p+1 alternating-digit forcing}}
\]

\[
\boxed{\text{digit-sum-8 balanced }\Rightarrow (p^2-1)/2\mid c/p^e}
\]

という、既存の有限 gap 排除とは別方向の一般構造が得られた。

現時点で最も有望なのは、digit-sum-8 の center divisibility を既存の center equation と結び、一般 \(T\) の balanced branch を消すこと。

