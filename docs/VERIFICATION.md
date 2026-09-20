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
python -X utf8 scripts/audit_i3_irreducible_cubic_and_rational_gaps.py
python -X utf8 scripts/audit_i3_dyadic_denominators_and_continued_fractions.py
python -X utf8 scripts/audit_i3_mixed_parameter_bound.py
```

出力は[検算結果](../data/results/)へ保存されます。標準出力にも確認項目を表示します。

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

初期のCRT証明書と、$43\le u\le48$の拡張は次のとおりです。

```text
python scripts/replay_certificate.py i3_original_replay.json i3_u42.json
python scripts/replay_certificate.py i3_u43_to_u48.json --primes prime_certificates_u48.json --output verification_u48.json
```

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
