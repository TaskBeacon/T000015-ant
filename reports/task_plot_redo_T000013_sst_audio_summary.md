# T000013 SST-Audio 绘图总结

已按 `task-plot` 从零重绘 `T000013-sst-audio` 的 task-flow 图，并推送到远程分支 `codex/task-plot-redo-T000013-sst-audio`。

## 结果

- 最终图已更新到 [task_flow.png](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000013-sst-audio/task_flow.png)
- 绘图规范已保存为 [task_plot_spec.yaml](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000013-sst-audio/references/task_plot_spec.yaml) 和 [task_plot_spec.json](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000013-sst-audio/references/task_plot_spec.json)
- 源证据摘录已更新为 [task_plot_source_excerpt.md](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000013-sst-audio/references/task_plot_source_excerpt.md)
- 审计记录已更新为 [task_plot_audit.md](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000013-sst-audio/references/task_plot_audit.md)

## 关键修正

- 补回了 go 试次的 `no_response_feedback` 分支。
- 将 stop cue 改为更短的 `Beep` 注释，避免长文本在窄屏中截断。
- 将图中阶段标签压缩为更短但仍清晰的中文/英文混合显示，减少重叠。
- 反馈屏使用了从配置读取的中文原文生成的图像资源，避免乱码。

## 验证结论

- `yaml/json` 结构一致
- `task_plot_contract` 校验通过
- `README.md` 的 Task Flow 预览位存在
- 最终重绘后的图像可读，反馈分支和 stop cue 均已显示
