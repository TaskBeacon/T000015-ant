# Task Logic Audit

## 1. Paradigm Intent

- Task: Attention Network Test (ANT)
- Primary construct: Efficiency of alerting, orienting, and executive-control attentional networks
- Manipulated factors:
  - Cue type (`no_cue`, `center_cue`, `double_cue`, `spatial_cue`)
  - Flanker congruency (`congruent`, `incongruent`)
  - Target position (`up`, `down`)
  - Target direction (`left`, `right`)
- Dependent measures:
  - RT and accuracy by condition
  - Derived network effects:
    - Alerting: `RT(no_cue) - RT(double_cue)`
    - Orienting: `RT(center_cue) - RT(spatial_cue)`
    - Executive control: `RT(incongruent) - RT(congruent)`
- Key citations:
  - `FAN2002`
  - `ERIKSEN1974`
  - `POSNER1990`
  - `FAN2005`

## 2. Block/Trial Workflow

### Block Structure

- Total blocks: 4 (human), 1 (qa/sim)
- Trials per block: 96 (human), 40 (qa/sim)
- Randomization/counterbalancing:
  - `BlockUnit.generate_conditions()` samples from pre-enumerated balanced condition list.
- Condition generation method:
  - Built-in PsyFlow condition generation.
- Runtime-generated trial values:
  - ITI sampled from configured range `[0.8, 1.2]`.

### Trial State Machine

1. State name: `pre_cue_fixation`
   - Onset trigger: `fixation_onset`
   - Stimuli shown: fixation cross
   - Timeout: auto-advance after `fixation_duration`
   - Next state: optional `cue_signal` or direct `flanker_response`

2. State name: `cue_signal` (optional)
   - Onset trigger: cue-specific trigger (`center_cue_onset`, `double_cue_onset`, or spatial cue onset)
   - Stimuli shown: cue marker(s) according to condition
   - Timeout: auto-advance after `cue_duration`
   - Next state: `flanker_response`

3. State name: `flanker_response`
   - Onset trigger: condition-encoded `stim_*` trigger
   - Stimuli shown: one 5-arrow flanker array (upper or lower position)
   - Valid keys: `task.key_list`
   - Timeout: miss if no response by `stim_duration`
   - Next state: `feedback`

4. State name: `feedback`
   - Onset trigger: `feedback_correct_response` / `feedback_incorrect_response` / `feedback_no_response`
   - Stimuli shown: outcome message
   - Timeout: auto-advance after `feedback_duration`
   - Next state: `iti`

5. State name: `iti`
   - Onset trigger: none
   - Stimuli shown: blank interval
   - Timeout: auto-advance after sampled ITI
   - Next state: next trial

## 3. Condition Semantics

- Condition naming rule:
  - `<cue_type>_<flanker_type>_<target_position>_<target_direction>`
  - Examples:
    - `no_cue_congruent_up_left`
    - `center_cue_incongruent_down_right`
    - `spatial_cue_up_congruent_down_left`

- Semantic interpretation:
  - `cue_type`: warning/orienting cue manipulation
  - `flanker_type`: compatibility/conflict manipulation
  - `target_position`: upper/lower row display
  - `target_direction`: expected response side

Participant-facing text/stimuli source:

- Source: `config/*.yaml` `stimuli`.
- Why appropriate: text and cue wording remain localization-portable without editing runtime code.
- Localization strategy: replace participant-facing strings in config while preserving `run_trial.py` control flow.

## 4. Response and Scoring Rules

- Response mapping:
  - Target left arrow -> `task.left_key` (`f`)
  - Target right arrow -> `task.right_key` (`j`)
- Response key source: config (`task.left_key`, `task.right_key`, `task.key_list`).
- Missing-response policy:
  - No key in response window -> no-response feedback.
- Correctness logic:
  - `StimUnit.capture_response(..., correct_keys=...)` computes `hit`.
- Reward/penalty updates:
  - No monetary scoring.
- Running metrics:
  - Block-level accuracy displayed in break screen.
  - Network-effect computation is expected in offline analysis from exported trial data.

## 5. Stimulus Layout Plan

- Screen: fixation
  - Stimulus IDs: `fixation`
  - Layout: center
  - Rationale: stabilize gaze before cue/target sequence.

- Screen: cue
  - Stimulus IDs: `cue_center`, `cue_up`, `cue_down`
  - Layout: explicit positions `center`, `y=+3`, `y=-3`
  - Rationale: implement alerting vs orienting manipulations.

- Screen: flanker stimulus
  - Stimulus IDs: congruent/incongruent row strings
  - Layout: top (`y=+3`) or bottom (`y=-3`) according to condition
  - Rationale: preserve target-location factor while keeping central arrow embedded in flankers.

- Screen: feedback and transitions
  - Stimulus IDs: feedback text, block break, instruction, goodbye
  - Layout: centered text/textbox with config-defined font/size
  - Rationale: consistent readability and localization control.

## 6. Trigger Plan

- Experiment boundary:
  - `exp_onset`, `exp_end`
- Block boundary:
  - `block_onset`, `block_end`
- Fixation and cue:
  - `fixation_onset`
  - `center_cue_onset`, `double_cue_onset`, `spatial_cue_up_onset`, `spatial_cue_down_onset`
- Target onset:
  - `stim_1111` ... `stim_4222` condition-encoded family
- Response:
  - `left_key_press`, `right_key_press`
- Outcome:
  - `feedback_correct_response`, `feedback_incorrect_response`, `feedback_no_response`

## 7. Architecture Decisions (Auditability)

- `main.py` style: single mode-aware flow (`human`, `qa`, `sim`) with shared setup path.
- `utils.py` used: no custom task helper required.
- Custom controller used: no.
- Why PsyFlow-native path is sufficient:
  - ANT flow maps cleanly to built-in `BlockUnit` condition generation and `StimUnit` phase orchestration.
- Legacy/backward-compatibility fallback logic required: no.

## 8. Inference Log

- Decision: use 5-arrow text arrays (`<<<<<`, `>><>>`, etc.) for flankers.
  - Why inference was required: source papers specify flanker compatibility concept; concrete glyph rendering is implementation-specific.
  - Citation-supported rationale: `ERIKSEN1974` compatibility/conflict logic preserved.

- Decision: keep cue duration `0.1 s` and fixed fixation `0.5 s`.
  - Why inference was required: ANT timing variants exist across studies.
  - Citation-supported rationale: `FAN2002`/`FAN2005` support brief cue then target sequence with bounded response windows.

- Decision: QA/sim profiles shortened relative to full human run.
  - Why inference was required: development gates need fast mechanism-complete execution.
  - Citation-supported rationale: preserves same condition semantics while reducing runtime volume.
