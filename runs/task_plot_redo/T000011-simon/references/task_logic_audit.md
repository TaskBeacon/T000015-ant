# Task Logic Audit

## 1. Paradigm Intent

- Task: Simon task (color-based response with irrelevant spatial location).
- Primary construct: Cognitive control under stimulus-response conflict (Simon effect).
- Manipulated factors: Congruency between stimulus location and response side.
- Dependent measures: Reaction time, hit/miss, error rate, congruent vs incongruent performance gap.
- Key citations:
  - W2086897159
  - W2580218417
  - W2132894889

## 2. Block/Trial Workflow

### Block Structure

- Total blocks: 3 (human profile); 1 in QA/sim profiles.
- Trials per block: 60 (human profile); 16 in QA/sim profiles.
- Randomization/counterbalancing: Conditions generated with default `BlockUnit.generate_conditions()` randomization.
- Condition weight policy:
  - `task.condition_weights` is not defined.
  - Runtime resolution through `TaskSettings.resolve_condition_weights()` is not used.
  - Generation uses even/default condition sampling over configured labels.
- Condition generation method:
  - Built-in `BlockUnit.generate_conditions(...)`.
  - No custom generator required because condition labels directly map to concrete stimuli.
  - Data shape passed to `run_trial.py`: condition token string (e.g., `red_left`).
- Runtime-generated trial values (if any):
  - ITI is sampled from configured range `[0.8, 1.2]` per trial.
  - No additional stochastic trial metadata is generated in custom code.

### Trial State Machine

1. State name: `pre_stim_fixation`
   - Onset trigger: `fixation_onset`.
   - Stimuli shown: `fixation` (`+`).
   - Valid keys: `task.key_list` (responses are ignored for correctness here).
   - Timeout behavior: fixed duration (`fixation_duration`).
   - Next state: `simon_response`.
2. State name: `simon_response`
   - Onset trigger: `stim_onset`.
   - Stimuli shown: one of `red_left`, `red_right`, `blue_left`, `blue_right`.
   - Valid keys: `f`, `j`.
   - Timeout behavior: closes at response or `stim_duration` timeout.
   - Next state: `feedback`.
3. State name: `feedback`
   - Onset trigger: one of `feedback_correct_response`, `feedback_incorrect_response`, `feedback_no_response`.
   - Stimuli shown: `correct_feedback` or `incorrect_feedback` or `no_response_feedback`.
   - Valid keys: none.
   - Timeout behavior: fixed duration (`feedback_duration`).
   - Next state: `iti`.
4. State name: `iti`
   - Onset trigger: none.
   - Stimuli shown: blank frame.
   - Valid keys: none.
   - Timeout behavior: duration sampled from `iti_duration` range.
   - Next state: next trial or block end.

## 3. Condition Semantics

- Condition ID: `red_left`
- Participant-facing meaning: Red target appears left; response by color rule is `f`.
- Concrete stimulus realization (visual/audio): Red circle at left screen position.
- Outcome rules: Correct if key is `f`; otherwise incorrect/no response.

- Condition ID: `red_right`
- Participant-facing meaning: Red target appears right; response by color rule is still `f`.
- Concrete stimulus realization (visual/audio): Red circle at right screen position.
- Outcome rules: Correct if key is `f`; otherwise incorrect/no response.

- Condition ID: `blue_left`
- Participant-facing meaning: Blue target appears left; response by color rule is `j`.
- Concrete stimulus realization (visual/audio): Blue circle at left screen position.
- Outcome rules: Correct if key is `j`; otherwise incorrect/no response.

- Condition ID: `blue_right`
- Participant-facing meaning: Blue target appears right; response by color rule is `j`.
- Concrete stimulus realization (visual/audio): Blue circle at right screen position.
- Outcome rules: Correct if key is `j`; otherwise incorrect/no response.

Also document where participant-facing condition text/stimuli are defined:

- Participant-facing text source (config stimuli / code formatting / generated assets): `config/*.yaml` under `stimuli`.
- Why this source is appropriate for auditability: Rule instructions and feedback strings are declarative and version-traceable.
- Localization strategy (how language variants are swapped via config without code edits): Replace text values in config stimuli and keep stimulus IDs stable.

## 4. Response and Scoring Rules

- Response mapping: `f` for red, `j` for blue, regardless of location.
- Response key source (config field vs code constant): Config fields `task.left_key` and `task.right_key`.
- If code-defined, why config-driven mapping is not sufficient: Not applicable.
- Missing-response policy: If no key before deadline, classify as no-response and show `no_response_feedback`.
- Correctness logic: `stim_color == red -> left_key`, `stim_color == blue -> right_key`.
- Reward/penalty updates: None.
- Running metrics: Block accuracy computed after each block in `main.py` and shown in `block_break` stimulus.

## 5. Stimulus Layout Plan

For every screen with multiple simultaneous options/stimuli:

- Screen name: Not applicable (single target stimulus shown per response phase).
- Stimulus IDs shown together: One target circle per trial; one feedback text per feedback phase.
- Layout anchors (`pos`): Target circles at `[-3,0]` or `[3,0]`; fixation centered.
- Size/spacing (`height`, width, wrap): Circle radius `1.5`; instruction textbox uses centered layout (`size: [20,5]`, `letterHeight: 0.78`).
- Readability/overlap checks: Single-item trial displays avoid overlap.
- Rationale: Simon paradigm isolates location-response conflict with minimal visual clutter.

## 6. Trigger Plan

Map each phase/state to trigger code and semantics.

- Experiment: `exp_onset` (98), `exp_end` (99)
- Block: `block_onset` (100), `block_end` (101)
- Trial fixation: `fixation_onset` (1)
- Trial stimulus onset: `stim_onset` (10)
- Keypress: `left_key_press` (30), `right_key_press` (31)
- Feedback by outcome: `feedback_correct_response` (51), `feedback_incorrect_response` (52), `feedback_no_response` (53)
- `feedback_onset` is reserved in config but not separately emitted in current runtime.

## 7. Architecture Decisions (Auditability)

- `main.py` runtime flow style (simple single flow / helper-heavy / why): Simple single flow with explicit mode branching (`human|qa|sim`).
- `utils.py` used? (yes/no): No.
- If yes, exact purpose (adaptive controller / sequence generation / asset pool / other): Not applicable.
- Custom controller used? (yes/no): No.
- If yes, why PsyFlow-native path is insufficient: Not applicable.
- Legacy/backward-compatibility fallback logic required? (yes/no): No.
- If yes, scope and removal plan: Not applicable.

## 8. Inference Log

List any inferred decisions not directly specified by references:

- Decision: Use 3 blocks × 60 trials in human profile.
- Why inference was required: Selected papers motivate Simon conflict design but do not enforce one fixed block/trial count for all deployments.
- Citation-supported rationale: Repeated congruent/incongruent sampling is required for stable conflict estimates.

- Decision: Use ITI range `[0.8, 1.2]` seconds.
- Why inference was required: Timing values vary across Simon implementations.
- Citation-supported rationale: Jittered inter-trial spacing is commonly used to reduce temporal predictability in conflict tasks.

## Contract Note

- Participant-facing labels/instructions/options are config-defined.
- `src/run_trial.py` does not hardcode localization text shown to participants.