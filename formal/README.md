# Leanで確認した範囲

[入口](../README.md) · [検算の案内](../docs/VERIFICATION.md)

[AlgebraCertificates.lean](AlgebraCertificates.lean)は**三つの代数恒等式**を確認するファイルです。
問題699全体、その後の全ての数学的議論、有限証明書の再生器を形式化したものではありません。

保存した実行環境はLean 4.33.0-rc1、Mathlib v4.33.0-rc1
（Mathlibコミット `79d0395a1825a6264ad5d269e35e60537518955e`）。
[既存の実行記録](../data/results/verification_lean.txt)も保存しています。

対応するMathlibプロジェクトから、実際の絶対パスを指定して実行します。

```text
lake env lean /absolute/path/to/erdos699/formal/AlgebraCertificates.lean
```
