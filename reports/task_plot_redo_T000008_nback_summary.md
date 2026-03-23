# T000008-nback Task Flow 重绘总结

## 目标

本次任务要求使用 `task-plot` 从零重绘 `T000008-nback` 的 task-flow 图，不沿用原始方案中的现成结果，并且所有输出都放在 `benchmark/` 下。

## 重绘结果

- 重新绘制后的图像为 `task_flow.png`。
- 时间线按条件逻辑折叠为 1 条代表性时间线，条件标签为 `Match`，`Nomatch` 作为等价变体注记保留。
- 每个试次保留 2 个阶段：
  - `Probe`
  - `ITI`
- `Probe` 使用示例数字 `5`，更贴近真实运行时的数字刺激。
- `ITI` 使用不可见占位图元表示空屏，避免渲染成 `[text]` 占位。

## 验证结果

- `task_plot_spec.yaml` 与 `task_plot_spec.json` 已互相对齐，结构一致。
- YAML/JSON 载入后比对结果为 `True`。
- 结构校验结果为 `1` 条时间线、`2` 个阶段。
- `task_flow.png` 已重新渲染并与更新后的规格一致。
- 最新布局反馈为 `layout pass 1: crop-only; left=0.052, right=0.053, blank=0.177`。
- `README.md` 的 `Task Flow` 预览位已保持为 `![Task Flow](task_flow.png)`。

## 产物

- `[task_flow.png](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000008-nback/task_flow.png)`
- `[task_plot_spec.yaml](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000008-nback/references/task_plot_spec.yaml)`
- `[task_plot_spec.json](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000008-nback/references/task_plot_spec.json)`
- `[task_plot_source_excerpt.md](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000008-nback/references/task_plot_source_excerpt.md)`
- `[task_plot_audit.md](/E:/xhmhc/TaskBeacon/benchmark/runs/task_plot_redo/T000008-nback/references/task_plot_audit.md)`

## 日志

- `[attempt1.log](/E:/xhmhc/TaskBeacon/benchmark/logs/task_plot_redo_T000008_nback_attempt1.log)`
- `[rerender.log](/E:/xhmhc/TaskBeacon/benchmark/logs/task_plot_redo_T000008_nback_rerender.log)`
- `[finalcheck.log](/E:/xhmhc/TaskBeacon/benchmark/logs/task_plot_redo_T000008_nback_finalcheck.log)`

## 结论

这次重绘把 `N-Back` 任务的试次级流程压缩成一个更准确的代表性时间线，并把数字刺激与空屏呈现修正为更接近真实运行状态的示意。
