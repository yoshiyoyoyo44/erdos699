# 2026年9月26日の添付原本

[現在地](../../../docs/STATUS.md) · [統合・追加研究](../../../research/general/weighted_cover_and_integration_2026-09-26.md)

受領した5ファイルは名前のアップロード番号だけを外し、内容のバイト列を保存した。
[import_manifest.json](import_manifest.json) が各原本のサイズとSHA-256を記録する。

| 添付原本 | 展開先・内容 |
|---|---|
| [5添字の報告](erdos699_five_indices_complete_2026-09-26.md) | $i=95,99,103,107,119$ の全範囲排除 |
| [5添字のZIP](erdos699_five_indices_complete_2026-09-26.zip) | [報告・証明書・検証器](erdos699_five_indices_complete_2026-09-26/) |
| [因子分配の報告](erdos699_coupled_factor_constraints_2026-09-26.md) | 行・列・対角線、二因子の行列式、素数個数の下限 |
| [因子分配のZIP](erdos699_coupled_factor_constraints_2026-09-26.zip) | [報告と前段3層](erdos699_coupled_factor_constraints_2026-09-26/) |
| [$i=3$ の研究索引](erdos699_i3_research_index_2026-09-25.md) | 参照先3本文は未添付。索引の強い次数評価を検証済みの一般定理とは扱わない |

5添字ZIP内の `previous_research.zip` は、上の因子分配ZIPとSHA-256が一致する。
同梱マニフェスト114項目を照合し、6監査を一時コピーで再実行した。
結果は[今回の再生記録](../../../data/results/verification_september26_attachments.json)に保存している。
原本内の `verification.json` を書き換えていない。

原本内の「未解決113個」「未解決108個」や既解決範囲は執筆時点の記述であり、今回の追加研究後の現在地ではない。
Pythonの相対パスや数式表記も原文のまま保存した。
現在の実行入口は `scripts/replay_september26_attachments.py`。
