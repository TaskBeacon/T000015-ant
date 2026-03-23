# T000004-flanker 任务流程图重绘报告

## 目标

基于 `README.md`、`config/config.yaml` 和 `src/run_trial.py` 从头重绘 Flanker 任务流程图，不沿用原始 `task_flow.png` 和 `references/` 中的既有结果，所有输出均放在 `benchmark/` 下。

## 结果

- 最终任务流程图：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\task_flow.png`
- 规范文件：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\references\task_plot_spec.yaml`
- 规范 JSON：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\references\task_plot_spec.json`
- 源证据摘录：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\references\task_plot_source_excerpt.md`
- 审计记录：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000004-flanker\references\task_plot_audit.md`

## 关键修正

- 4 条条件时间线均已保留，分别对应 `congruent_left`、`congruent_right`、`incongruent_left`、`incongruent_right`。
- 将响应阶段标签从过于简略的 `Flanker` 改为 `Flanker Response`。
- 补回了初版遗漏的 `ITI` 空白间隔阶段，并与 `config/config.yaml` 中的 `iti_duration` 保持一致。
- `ITI` 阶段使用文本注释作为最后手段，避免它在图上被误看成真实刺激。

## 校验结果

- `task_plot_contract` 结构校验通过。
- 本地布局 QA 通过，未触发额外布局调整。
- 最终布局记录：`layout pass 1: no adjustment needed; left=0.055, right=0.055, blank=0.162`

## 日志

- 初次生成日志：`E:\xhmhc\TaskBeacon\benchmark\logs\task_plot_redo_T000004_flanker_attempt1.log`
- 重新渲染日志：`E:\xhmhc\TaskBeacon\benchmark\logs\task_plot_redo_T000004_flanker_attempt2.log`

## 结论

这次重绘结果已完成，图、规范、审计和总结都已写入 `benchmark/`，可以直接纳入后续 validation pipeline。
