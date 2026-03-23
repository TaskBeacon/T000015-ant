# T000014 Stroop 任务流程图重绘总结

已按 `task-plot` 从零重绘 `T000014-stroop` 的 task-flow 图，并将结果放在 `benchmark/runs/task_plot_redo/T000014-stroop/` 下。

## 结果

- 最终图：[task_flow.png](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000014-stroop/task_flow.png)
- 绘图规范：[task_plot_spec.yaml](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000014-stroop/references/task_plot_spec.yaml) / [task_plot_spec.json](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000014-stroop/references/task_plot_spec.json)
- 源证据摘录：[task_plot_source_excerpt.md](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000014-stroop/references/task_plot_source_excerpt.md)
- 审计记录：[task_plot_audit.md](E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000014-stroop/references/task_plot_audit.md)

## 关键修正

- 从 4 个条件重新建立了 4 条时间线，没有沿用自动折叠的代表性方案。
- 每条时间线恢复为 4 个阶段：`Fixation`、`Stroop Response`、`Feedback`、`ITI`。
- `Feedback` 阶段使用了独立中文图片资源，避免文本渲染出现问号。
- `auto_width` 打开后，右侧空白明显减少，图面更紧凑。

## 验证结果

- `task_plot_contract` 通过
- `yaml/json` 一致
- `README.md` 中的 Task Flow 预览位已更新
- 最终图像可读，反馈和 ITI 均符合预期
