# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| `conditions` | `task.conditions` | `['red_left', 'red_right', 'blue_left', 'blue_right']` | `W2086897159` | Simon conflict design contrasts stimulus color rule with irrelevant spatial location. | `implemented` | Four condition tokens encode congruent and incongruent pairings. |
| `response_mapping` | `task.left_key`, `task.right_key` | `f` for red, `j` for blue | `W2086897159` | Simon protocol requires color-based response while ignoring location. | `implemented` | Mapping is config-defined for localization/portability. |
| `total_blocks` | `task.total_blocks` | `3` (human), `1` (qa/sim) | `W2580218417` | Simon-type studies assess conflict processing across repeated trials/segments. | `inferred` | QA/sim reduce blocks for runtime smoke testing. |
| `trial_per_block` | `task.trial_per_block` | `60` (human), `16` (qa/sim) | `W2086897159` | Simon conflict metrics rely on repeated congruent/incongruent events. | `inferred` | Practical implementation target for stable behavioral estimates. |
| `fixation_duration` | `timing.fixation_duration` | `0.5` | `W2580218417` | Pre-target fixation stage is used before conflict stimulus onset. | `inferred` | Implemented as fixed pre-stimulus period. |
| `stim_duration` | `timing.stim_duration` | `1.0` | `W2086897159` | Conflict stimulus response window is bounded to enforce timely responses. | `inferred` | Timeout yields no-response feedback. |
| `feedback_duration` | `timing.feedback_duration` | `0.5` | `W2580218417` | Post-response outcome signal supports control adaptation analyses. | `inferred` | Feedback text depends on hit/miss state. |
| `iti_duration` | `timing.iti_duration` | `[0.8, 1.2]` | `W2086897159` | Variable inter-trial spacing reduces temporal predictability in conflict tasks. | `inferred` | Sampled per trial via `StimUnit.show(duration=[min,max])`. |
| `stim_onset` | `triggers.map.stim_onset` | `10` | `W2086897159` | Event markers are required for trial-aligned EEG conflict analyses. | `implemented` | Emitted at Simon stimulus onset. |
| `key_triggers` | `triggers.map.left_key_press`, `triggers.map.right_key_press` | `30`, `31` | `W2580218417` | Response-side markers support lateralized control analyses. | `implemented` | Sent on keypress if response occurs within window. |
| `feedback_triggers` | `triggers.map.feedback_correct_response`, `feedback_incorrect_response`, `feedback_no_response` | `51`, `52`, `53` | `W2580218417` | Outcome-class markers support post-conflict adaptation analyses. | `implemented` | Emitted at feedback onset by outcome type. |