# Parameter Mapping

## Mapping Table

| Parameter ID | Config Path | Implemented Value | Source Paper ID | Evidence (quote/figure/table) | Decision Type | Notes |
|---|---|---|---|---|---|---|
| `cue_conditions` | `task.conditions` prefix set (`no_cue`, `center_cue`, `double_cue`, `spatial_cue_*`) | 4 cue categories represented | `FAN2002` | ANT compares no-cue, center-cue, double-cue, and spatial-cue conditions. | `direct` | Spatial cue includes upper/lower cue location variants. |
| `flanker_conditions` | `task.conditions` middle token (`congruent` / `incongruent`) | Congruent and incongruent flanker arrays | `ERIKSEN1974` | Flanker interference manipulation is based on target-flanker compatibility. | `direct` | Used for executive-control effect. |
| `target_location` | `task.conditions` token (`up` / `down`) | Upper and lower target rows | `FAN2002` | ANT presents targets at upper/lower positions with cue manipulations. | `direct` | Supports orienting and spatial cueing logic. |
| `response_mapping` | `task.left_key`, `task.right_key` | `left->f`, `right->j` | `FAN2002` | Central arrow direction is mapped to binary motor response. | `adapted` | Keyboard keys adapted for this implementation. |
| `human_block_volume` | `task.total_blocks`, `task.trial_per_block` | `4 x 96` (384 trials) | `FAN2002` | Canonical ANT uses repeated balanced cue x flanker combinations. | `adapted` | QA/sim reduced for smoke profile. |
| `cue_duration` | `timing.cue_duration` | `0.1 s` | `FAN2005` | Brief cue presentation precedes target onset in ANT timing. | `direct` | Applied to center/double/spatial cue displays. |
| `fixation_duration` | `timing.fixation_duration` | `0.5 s` | `FAN2002` | Fixation period anchors each trial before cue/target. | `adapted` | Fixed duration in this implementation. |
| `stim_duration` | `timing.stim_duration` | `1.0 s` | `FAN2002` | ANT target response window is bounded to classify misses/errors. | `adapted` | Trial ends on response or timeout. |
| `iti_range` | `timing.iti_duration` | `[0.8, 1.2] s` | `FAN2005` | Jittered intervals reduce fixed temporal expectation. | `inferred` | Configured as uniform random range. |
| `trigger_cue_onset` | `triggers.map.center_cue_onset`, `double_cue_onset`, `spatial_cue_*_onset` | `11`, `12`, `13`, `14` | `FAN2005` | Cue type is a core ANT factor for alerting/orienting contrasts. | `adapted` | Cue-side markers separated for spatial cue. |
| `trigger_stim_onset` | `triggers.map.stim_*` | `21`..`58` family | `FAN2002` | Cue x flanker x position x direction combinations must be recoverable from events. | `adapted` | Encoded as compact digit scheme in config. |
| `trigger_response` | `triggers.map.left_key_press`, `right_key_press` | `201`, `202` | `ERIKSEN1974` | Correct side response is central behavioral outcome. | `direct` | Used for RT and accuracy extraction. |
