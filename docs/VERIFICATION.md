# 検算の案内

[入口](../README.md) · [現在地](STATUS.md) · [コード一覧](../scripts/README.md) · [データの場所](../data/README.md)

以下のコマンドは**リポジトリのルート**で実行します。Pythonのassertを使うため、`python -O`は使わないでください。
各ノートの検算はその主張に対応するもので、全てを一度に実行する必要はありません。

## 必要なもの

- Python。既存の記録ではPython 3.14.3を使用。
- 代数の検算にはSymPy。既存の記録ではSymPy 1.14.0を使用。
- 一部の証明書の**再生成**にはNumPy。標準ライブラリだけで動く再生器とは区別します。
- 保存済みMagma応答のローカル検算には、Magmaへの再送信は不要です。

必要に応じて `python -m pip install sympy` で導入できます。

## 最新の結果を短く検算する

```text
python -X utf8 scripts/audit_i3_gap_square_obstructions.py
python -X utf8 scripts/audit_i3_growing_gap_frey.py
python -X utf8 scripts/audit_i3_new_chat_and_effective_gap.py
python -X utf8 scripts/audit_i3_twist_and_kummer_support.py
python -X utf8 scripts/audit_i3_discriminant_support.py
python -X utf8 scripts/audit_i3_chat_integration.py
python -X utf8 scripts/audit_i3_thue_mahler_table.py
python -X utf8 scripts/replay_i3_cubic_discriminant_minima.py
python -X utf8 scripts/audit_i3_cubic_discriminant_and_cf_tail.py
python -X utf8 scripts/audit_i3_irreducible_cubic_and_rational_gaps.py
python -X utf8 scripts/audit_i3_dyadic_denominators_and_continued_fractions.py
python -X utf8 scripts/audit_i3_mixed_parameter_bound.py
```

出力は[検算結果](../data/results/)へ保存されます。標準出力にも確認項目を表示します。

指数差の平方枝の検算は、5恒等式、四分岐の定数証明書、256件の法16の条件、317件の平方差の人工的な診断を確認します。
全ての $G$ に対する排除は[続稿の一般証明](../research/i3/i3_gap_square_obstructions_2026-09-21.md)によります。
新たな外部表や高さ定理は不要ですが、既存の正規化の証明依存は引き継ぎます。

増大する指数差の検算は、14恒等式、2,471個の人工的な曲線診断、保存済みの全曲線表1,813,534行を確認します。
106個の根がない証明書と92個の根の分解を保存し、残る三つの和も全分岐で排除します。
素数の積に対する増大評価と閾値は[第二のFrey曲線の稿](../research/i3/i3_growing_gap_and_auxiliary_frey_2026-09-21.md)に証明しています。
表の完全性は外部計算、増大評価はvon Känelの一般定理に依存し、人工的な曲線は元の反例候補ではありません。

新チャットの統合と指数差の検算は、14恒等式、1,440件の局所合同式診断、四分岐の係数と $u=2^{42}$ の閾値を確認します。
診断例は二つの入力合同式を満たす人工的な局所データであり、元の反例候補ではありません。
固定した指数差 $G$ からの明示的上限の一般証明は[統合稿](../research/i3/i3_new_chat_integration_and_effective_gap_2026-09-21.md)にあります。

二次捻りとKummer補助因子の検算は、8恒等式と6剰余類の最小化・最適性を記号計算し、
9,000組の局所付値と256通りの符号を補助診断します。
3乗因子を除去した曲線のモデル、2進条件の保存、Kummerの四つの商との正確な対応が対象です。
一般証明は[続稿](../research/i3/i3_quadratic_twist_and_kummer_support_2026-09-21.md)にあります。

判別式の素因数を扱う検算は、14恒等式、整数系と局所付値の診断、公開曲線全リストの1,813,534行を確認します。
保存したgzip原本は約13.7MBで、展開後のSHA-256も照合します。外部への問い合わせは不要です。
素数集合の被覆、最大2進付値48・51、1728からの最小の隔たりを整数・分数で再計算します。
全曲線がリストに含まれるという完全性は、[証明ノート](../research/i3/i3_discriminant_support_and_elliptic_curve_2026-09-21.md)に明記した外部計算に依存します。
同稿第6.3節では、別の証明済み定理である von Känel の判別式・導手評価から $u$ の明示的上限を導きます。
検算器は $u\ge2^{40}\Rightarrow R>u^{1/4}$ の閾値に用いる定数比較を分数で確認します。一般の不等式の証明はノートに記載しています。

4チャットの統合検算は15恒等式、2,000件の原始点輸送、6通りの座標変換を確認します。
Thue–Mahler表の検算は保存した原本を使い、全33,456点の原始性・値、2冪値の最大指数28、
独立な239,190組の列挙から得た268形式の表への整数可逆変換を確認します。
**掲載解の完全性は von Känel–Matschke のTheorem Eに依存**し、このPython検算だけでは再証明していません。
詳細は[終端形式の排除](../research/i3/i3_terminal_thue_mahler_2026-09-21.md)を参照してください。

小判別式の再生は、65,790組の係数を生成器とは別に全列挙し、74組の簡約形と一致することを確認します。
判別式の2進付値を下げる恒等式も検算します。数体の外部表やMagmaは使いません。
その[証明ノート](../research/i3/i3_cubic_discriminant_minima_2026-09-21.md)に、有限範囲の完全性と一様な上限 $M^3<2^u/284$ の根拠があります。
証明書を再生成する場合は `python scripts/certify_i3_cubic_discriminant_minima.py` を実行します。

## 主な証明書を再生する

| 対象 | コマンド | 読む証明 |
|---|---|---|
| 大きい添字の基盤 | `python scripts/replay_large_indices.py` | [判別式](../research/general/discriminant_continuation.md) |
| 区間ごとの改善 | `python scripts/replay_interval_indices.py` | [区間評価](../research/general/interval_valuation_continuation.md) |
| 臨界添字 | `python scripts/replay_critical_indices.py` | [臨界添字](../research/general/critical_indices_and_handoff_integration.md) |
| $i=119$の有限範囲 | `python scripts/replay_i119_finite.py` | [有限範囲](../research/i119/i119_a100_continuation.md) |
| $i=3$の指数差 | `python scripts/replay_i3_gap13.py` | [指数差の証明](../research/i3/i3_gap13_and_descent_continuation.md) |
| 素数の直後の冪 | `python scripts/replay_i3_prime_neighbor_powers.py` | [特殊な冪の族](../research/i3/i3_prime_neighbor_powers_2026-09-20.md) |

詳細な実行の組み合わせや外部定理への依存は、それぞれの証明ノートにあります。

初期のCRT証明書と、$u\le50$ までの拡張は次のとおりです。

```text
python scripts/replay_certificate.py i3_original_replay.json i3_u42.json
python scripts/replay_certificate.py i3_u43_to_u48.json --primes prime_certificates_u48.json --output verification_u48.json
python scripts/replay_certificate.py i3_u49_to_u50.json --primes prime_certificates_u50.json --output verification_u50.json
```

最後のコマンドは新しい $284M^3<2^u$ を使う $u=49,50$ の証明書です。
14,194個の奇数部分の被覆、164個のCRT候補の排除、43,353個の素数を標準Pythonだけで確認します。
上限の数学的根拠は[小判別式の証明ノート](../research/i3/i3_cubic_discriminant_minima_2026-09-21.md)とその再生器で確認します。
CRT証明書の再生成は `python scripts/extend_i3_cubic_minima_certificate.py` です。

データの旧ファイル名はそのまま指定できます。[参照先の解決](../scripts/repo_paths.py)で新しい保存場所へ対応させています。
明示的な相対パスはリポジトリのルート基準、絶対パスはそのまま使います。

## MagmaとLean

```text
python scripts/audit_i3_center_curve.py
python scripts/audit_i3_fixed_blocks.py
```

これは保存された入力・応答・点・逆変換の確認です。整数点のリストの完全性は、ノートに記載したMagmaの証明計算への依存が残ります。
[Magmaの入力と応答](../magma/README.md)から対応をたどれます。

Leanについては[形式化の範囲と環境](../formal/README.md)を参照してください。

## リポジトリ構成を確認する

```text
python scripts/check_repository.py
python scripts/check_repository.py --smoke
```

文書リンク、Pythonの構文、移動前後の原本・証明書・ログのSHA-256を確認します。
`--smoke`は一時的なコピーで代表的な検算器を実行し、保存済みの結果を上書きしません。
今回の整理に必要な確認であり、全数学的成果の再監査ではありません。

## 現在の構成でZIPを作る

```text
python scripts/package_results.py
```

Git管理下のファイルをフォルダ構成ごと `dist/erdos699-current.zip` に保存し、ZIP内の `SHA256.json` と照合します。
[過去のZIP](../archive/README.md)は当時の配布物として保存し、このコマンドでは上書きしません。
