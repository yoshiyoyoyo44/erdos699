# 検算コード

[入口](../README.md) · **[実行方法](../docs/VERIFICATION.md)** · [証明ノート](../research/README.md)

リポジトリのルートから `python scripts/audit_i3_mixed_parameter_bound.py` で実行します。

| 名前 | 役割 |
|---|---|
| `audit_*.py` | 恒等式・不等式・保存された計算の検算 |
| `replay_*.py` | 有限証明書の再生 |
| `certify_*.py`、`make_*.py` | 証明書・計算入力の生成 |
| `explore_*.py` | 探索用。証明の保証範囲は各ノートを参照 |
| [check_repository.py](check_repository.py) | リンク・構文・原本保存と、代表的な動作の確認 |
| [repo_paths.py](repo_paths.py) | 証明書やログに記録された旧ファイル名を新配置へ対応 |
| [package_results.py](package_results.py) | 現在の構成をSHA-256付きのZIPにする |

最初に実行するものは[検算の案内](../docs/VERIFICATION.md)で選べます。
全スクリプトをまとめて走らせる必要はありません。
`run_magma_*.py`は指定した入力を外部のMagma計算サービスへ送るためのものです。
保存済みの応答を検算するだけなら実行は不要です。
