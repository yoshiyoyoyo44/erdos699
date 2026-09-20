# Erdős Problem 699

二項係数どうしの共通素因数を調べる研究記録です。**問題全体は未解決です。**

> 任意の整数 $1\le i<j\le n/2$ に対して、
> $\binom ni$ と $\binom nj$ は素数 $p\ge i$ を共有するか？

[元の問題文](https://www.erdosproblems.com/699) · [形式的な定式化](https://github.com/google-deepmind/formal-conjectures/blob/main/FormalConjectures/ErdosProblems/699.lean)

## まず読む

| 知りたいこと | 読むページ |
|---|---|
| どこまで解けて、何が残っているか | **[現在地](docs/STATUS.md)** |
| 証明をどの順に読めばよいか | **[読む順序・分野別の案内](docs/READING_GUIDE.md)** |
| 各補題の詳しい結論と根拠 | [成果の詳細一覧](docs/RESULTS_CATALOG.md) |
| 計算を再現する方法 | **[検算の案内](docs/VERIFICATION.md)** |

## 現在地

このリポジトリに記録した証明・有限証明書による範囲です。根拠と依存関係は[現在地](docs/STATUS.md)にまとめています。

| 範囲 | 状況 |
|---|---|
| $i=1,2$ | 成立 |
| $i\ge120$、および $i=96,97,100,101$ | 全ての $n,j$ で成立 |
| $i=119$ | $n\le10^{87}$ で成立。それより先は未解決 |
| $i=3$ | 必要条件・部分領域の排除を研究中。一般の場合は未解決 |
| その他の $3\le i\le119$ | 上記の解決済み添字を除き未解決 |

## 最新の研究 — 2026年9月21日

[追加資料を統合](research/i3/i3_cubic_discriminant_and_cf_tail_2026-09-21.md)し、
全実三次数体の判別式下界49による必要条件の強化と、連分数末尾の制約を記録しました。
原文の交差積を最大公約数に訂正して結論を補証しています。
増大する全領域の排除にはまだ至っていません。

## ファイルの場所

| フォルダ | 内容 |
|---|---|
| [research](research/README.md) | 分野別の証明・研究ノート |
| [scripts](scripts/README.md) | Pythonの検算器・証明書の生成器 |
| [data](data/README.md) | 有限証明書、計算ケース、検算結果 |
| [magma](magma/README.md) | Magmaへの入力と保存した応答 |
| [formal](formal/README.md) | Leanで確認した三つの代数恒等式 |
| [sources](sources/README.md) | 添付・外部回答の原文 |
| [archive](archive/README.md) | 過去の進捗一覧、ZIP、旧ファイル名の対応表 |

2026年9月21日に構成を整理しました。証明の主張は変更せず、添付原本・証明書・計算ログは元のバイト列を保存しています。
