# T000011-simon 源摘录

## 1. README 关键点

- 任务名称是 Simon Task，目标是根据颜色作答、忽略左右位置。
- 任务说明中明确列出四个条件 token：`red_left`、`red_right`、`blue_left`、`blue_right`。
- `Trial-Level Flow` 的四个阶段分别是 `pre_stim_fixation`、`simon_response`、`feedback`、`iti`。

## 2. 配置关键点

- `task.conditions` 列出四个条件 token。
- `fixation_duration = 0.5 s`
- `stim_duration = 1.0 s`
- `feedback_duration = 0.5 s`
- `iti_duration = [0.8, 1.2] s`
- `fixation` 是白色 `+`。
- 四个刺激分别是左/右位置的红色或蓝色圆圈。
- 反馈文本分别是 `正确`、`错误`、`未反应`。
- `instruction_text`、`block_break`、`good_bye` 也在配置中定义，但本次图按试次级流程绘制，不纳入条件时间线。

## 3. run_trial.py 关键点

```python
set_trial_context(
    fixation_unit,
    phase="pre_stim_fixation",
    deadline_s=settings.fixation_duration,
    valid_keys=list(settings.key_list),
    stim_id="fixation",
)
fixation_unit.show(duration=settings.fixation_duration, onset_trigger=settings.triggers.get("fixation_onset"))
```

```python
set_trial_context(
    stim_unit,
    phase="simon_response",
    deadline_s=settings.stim_duration,
    valid_keys=list(settings.key_list),
    stim_id=str(condition),
)
stim_unit.capture_response(
    keys=settings.key_list,
    correct_keys=correct_response,
    duration=settings.stim_duration,
)
```

```python
if response and hit:
    feedback_stim = stim_bank.get("correct_feedback")
elif response and not hit:
    feedback_stim = stim_bank.get("incorrect_feedback")
else:
    feedback_stim = stim_bank.get("no_response_feedback")

make_unit(unit_label="feedback").add_stim(feedback_stim).show(duration=settings.feedback_duration)
make_unit(unit_label="iti").show(duration=settings.iti_duration)
```

- `pre_stim_fixation` 是试次开始前的中央注视阶段。
- `simon_response` 是颜色作答阶段，位置只是干扰项。
- `feedback` 由正确/错误/未反应三种结果分支决定。
- `iti` 是反馈之后的空白间隔。

## 4. 绘图映射

- 四个条件各保留一条时间线。
- 每条时间线都包含四个阶段：`Fixation`、`Simon Response`、`Feedback`、`ITI`。
- `Simon Response` 阶段用红/蓝圆圈加左右位置来区分条件。
- `Feedback` 阶段用中文反馈图资源呈现三种结果。
- `ITI` 阶段用空白画面表示。

