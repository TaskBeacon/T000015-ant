# T000006-mid Task Flow 重绘总结

## 目标

本次任务要求使用 `task-plot` 从零重绘 `T000006-mid` 的 task-flow 图，不沿用原始方案中的现成结果，并且所有输出都放在 `benchmark/` 下。

## 重绘结果

- 重新绘制后的图像为 `task_flow.png`。
- 时间线按条件拆分为 3 行，分别对应 `win`、`lose`、`neut`。
- 每条时间线都恢复为 5 个阶段：
  - `Cue`
  - `Anticipation`
  - `Target`
  - `Pre-Feedback`
  - `Feedback`
- `Target` 使用自适应时长，图中按 `40–370 ms` 表达。
- `Cue` 与 `Pre-Feedback` 阶段是根据源码中的 `show()` 调用重新补回的，不再沿用旧图的缺失结果。

## 验证结果

- `task_plot_spec.yaml` 与 `task_plot_spec.json` 已互相对齐，结构一致。
- YAML/JSON 载入后比对结果为 `True`。
- 结构校验结果为 `3` 条时间线、每条 `5` 个阶段。
- `task_flow.png` 已存在且已重新渲染。
- 最新布局反馈为 `layout pass 1: crop-only; left=0.058, right=0.067, blank=0.169`。
- 当前审计文件已写入最终哈希与不确定项说明。

## 产物

- `[task_flow.png](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000006-mid/task_flow.png)`
- `[task_plot_spec.yaml](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000006-mid/references/task_plot_spec.yaml)`
- `[task_plot_spec.json](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000006-mid/references/task_plot_spec.json)`
- `[task_plot_source_excerpt.md](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000006-mid/references/task_plot_source_excerpt.md)`
- `[task_plot_audit.md](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000006-mid/references/task_plot_audit.md)`

## 日志

- `[attempt1.log](/E:/xhmhc/TaskBeacon/benchmark/logs/task_plot_redo_T000006_mid_attempt1.log)`
- `[rerender.log](/E:/xhmhc/TaskBeacon/benchmark/logs/task_plot_redo_T000006_mid_rerender.log)`
- `[finalcheck.log](/E:/xhmhc/TaskBeacon/benchmark/logs/task_plot_redo_T000006_mid_finalcheck.log)`

## 结论

这次重绘已经补齐 `MID` 任务的试次级流程，且把条件、阶段、时长和反馈证据链统一到了同一份可审计的 `task-plot` 产物中。
