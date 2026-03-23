# T000009-prl Task Flow 重绘总结

## 目标

本次任务要求使用 `task-plot` 从零重绘 `T000009-prl` 的 task-flow 图，不沿用原始方案中的现成结果，并且所有输出都放在 `benchmark/` 下。

## 重绘结果

- 重新绘制后的图像为 `task_flow.png`。
- 时间线按条件拆分为 2 行，分别对应 `AB` 和 `BA`。
- 每条时间线都保留 4 个阶段：
  - `Fixation`
  - `Choice`
  - `Blank`
  - `Feedback`
- `Choice` 阶段使用本次在 `references/` 下生成的组合图来表示左右刺激顺序：
  - `choice_pair_AB.png`
  - `choice_pair_BA.png`
- `Blank` 阶段用空文本占位方式表达真正的空白屏幕，避免渲染成 `[text]`。
- `Feedback` 阶段改用 ASCII 文本表达，避免中文或负号在图中被字体处理成乱码。

## 验证结果

- `task_plot_spec.yaml` 与 `task_plot_spec.json` 已互相对齐，结构一致。
- YAML/JSON 载入后比对结果为 `True`。
- 结构校验结果为 `2` 条时间线、每条 `4` 个阶段。
- `task_flow.png` 已重新渲染并与更新后的规范一致。
- 最新布局反馈为 `layout pass 1: crop-only; left=0.052, right=0.060, blank=0.164`。
- `README.md` 的 `Task Flow` 预览位已保持为 `![Task Flow](task_flow.png)`。

## 产物

- `[task_flow.png](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000009-prl/task_flow.png)`
- `[task_plot_spec.yaml](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000009-prl/references/task_plot_spec.yaml)`
- `[task_plot_spec.json](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000009-prl/references/task_plot_spec.json)`
- `[task_plot_source_excerpt.md](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000009-prl/references/task_plot_source_excerpt.md)`
- `[task_plot_audit.md](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000009-prl/references/task_plot_audit.md)`
- `[choice_pair_AB.png](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000009-prl/references/choice_pair_AB.png)`
- `[choice_pair_BA.png](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000009-prl/references/choice_pair_BA.png)`

## 日志

- `[attempt1.log](/E:/xhmhc/TaskBeacon/benchmark/logs/task_plot_redo_T000009_prl_attempt1.log)`
- `[rerender.log](/E:/xhmhc/TaskBeacon/benchmark/logs/task_plot_redo_T000009_prl_rerender.log)`
- `[finalcheck.log](/E:/xhmhc/TaskBeacon/benchmark/logs/task_plot_redo_T000009_prl_finalcheck.log)`

## 结论

这次重绘补齐了 `PRL` 任务的试次级流程，并把条件差异、空白间隔和反馈阶段统一到了同一份可审计的 `task-plot` 产物中。
