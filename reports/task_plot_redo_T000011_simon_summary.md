# T000011-simon 任务流程图重绘总结

## 结论

已按 `task-plot` 从头重绘 `T000011-simon` 的任务流程图，输出都放在 `benchmark/runs/task_plot_redo/T000011-simon/` 下。

## 最终产物

- 流程图：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\task_flow.png`
- 规格文件：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\references\task_plot_spec.yaml`
- 规格文件 JSON：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\references\task_plot_spec.json`
- 源摘录：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\references\task_plot_source_excerpt.md`
- 反馈图资源：`E:\xhmhc\TaskBeacon\benchmark\runs\task_plot_redo\T000011-simon\references\feedback_outcomes_text.png`

## 本次修正

- 把自动折叠成单条代表线的结果，手工展开为 4 条条件时间线。
- 每条时间线保留 4 个阶段：`Fixation`、`Simon Response`、`Feedback`、`ITI`。
- `Simon Response` 阶段改成条件专属的左右位置红/蓝圆圈，避免被概括成通用圆圈。
- `Feedback` 阶段改成中文反馈图资源，确保 `正确 / 错误 / 未反应` 可读。
- `ITI` 阶段改成空白间隔，不再显示占位文字。

## 验证结果

- `task_plot_contract` 通过。
- 布局反馈结果为 `layout pass 1: crop-only; left=0.064, right=0.076, blank=0.189`。
- 最终图已经确认显示 4 条时间线，没有再被折叠成单条代表图。
- `README.md` 的 `## 2. Task Flow` 预览位已更新为 `![Task Flow](task_flow.png)`。

## 日志

- 初次自动生成日志：`E:\xhmhc\TaskBeacon\benchmark\logs\task_plot_redo_T000011_simon_attempt1.log`
- 最终重渲染日志：`E:\xhmhc\TaskBeacon\benchmark\logs\task_plot_redo_T000011_simon_rerender.log`

