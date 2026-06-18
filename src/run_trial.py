from functools import partial

from psyflow import StimUnit, set_trial_context, next_trial_id

# trial stages use task-specific phase labels via set_trial_context(...)


def run_trial(
    win,
    kb,
    settings,
    condition: str,
    stim_bank: dict,
    trigger_runtime=None,
    block_id=None,
    block_idx=None,
):
    """Run one ANT trial."""
    trial_id = next_trial_id()
    trial_data = {"condition": condition}
    make_unit = partial(StimUnit, win=win, kb=kb, runtime=trigger_runtime)

    parts = condition.split("_")
    target_direction = parts[-1]
    target_position = parts[-2]
    flanker_type = parts[-3]
    cue_type = "_".join(parts[:-3])

    correct_response = settings.left_key if target_direction == "left" else settings.right_key
    stim_name = f"{flanker_type}_{target_position}_{target_direction}"

    trial_data.update(
        {
            "cue_type": cue_type,
            "flanker_type": flanker_type,
            "target_position": target_position,
            "target_direction": target_direction,
            "correct_response": correct_response,
        }
    )

    # phase: pre_cue_fixation
    fix_unit = make_unit(unit_label="fixation").add_stim(stim_bank.get("fixation"))
    set_trial_context(
        fix_unit,
        trial_id=trial_id,
        phase="pre_cue_fixation",
        deadline_s=settings.fixation_duration,
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=str(condition),
        task_factors={"condition": str(condition), "stage": "pre_cue_fixation", "block_idx": block_idx},
        stim_id="fixation",
    )
    fix_unit.show(duration=settings.fixation_duration, onset_trigger=settings.triggers.get("fixation_onset")).to_dict(trial_data)

    # phase: cue_signal
    if cue_type != "no_cue":
        if cue_type == "center_cue":
            cue_unit = make_unit(unit_label="cue").add_stim(stim_bank.get("cue_center"))
            set_trial_context(
                cue_unit,
                trial_id=trial_id,
                phase="cue_signal",
                deadline_s=settings.cue_duration,
                valid_keys=list(settings.key_list),
                block_id=block_id,
                condition_id=str(condition),
                task_factors={"condition": str(condition), "stage": "cue_signal", "cue_type": cue_type, "block_idx": block_idx},
                stim_id="cue_center",
            )
            cue_unit.show(duration=settings.cue_duration, onset_trigger=settings.triggers.get("center_cue_onset")).to_dict(trial_data)
        elif cue_type == "double_cue":
            cue_unit = make_unit(unit_label="cue").add_stim(stim_bank.get("cue_up")).add_stim(stim_bank.get("cue_down"))
            set_trial_context(
                cue_unit,
                trial_id=trial_id,
                phase="cue_signal",
                deadline_s=settings.cue_duration,
                valid_keys=list(settings.key_list),
                block_id=block_id,
                condition_id=str(condition),
                task_factors={"condition": str(condition), "stage": "cue_signal", "cue_type": cue_type, "block_idx": block_idx},
                stim_id="cue_double",
            )
            cue_unit.show(duration=settings.cue_duration, onset_trigger=settings.triggers.get("double_cue_onset")).to_dict(trial_data)
        elif cue_type.startswith("spatial_cue"):
            cue_pos = cue_type.split("_")[-1]
            cue_name = f"cue_{cue_pos}"
            cue_unit = make_unit(unit_label="cue").add_stim(stim_bank.get(cue_name))
            set_trial_context(
                cue_unit,
                trial_id=trial_id,
                phase="cue_signal",
                deadline_s=settings.cue_duration,
                valid_keys=list(settings.key_list),
                block_id=block_id,
                condition_id=str(condition),
                task_factors={"condition": str(condition), "stage": "cue_signal", "cue_type": cue_type, "block_idx": block_idx},
                stim_id=cue_name,
            )
            cue_unit.show(
                duration=settings.cue_duration,
                onset_trigger=settings.triggers.get(f"spatial_cue_{cue_pos}_onset"),
            ).to_dict(trial_data)

    # phase: flanker_response
    stim_unit = make_unit(unit_label="stimulus").add_stim(stim_bank.get(stim_name))

    cue_code = {"no_cue": 1, "center_cue": 2, "double_cue": 3, "spatial_cue_up": 4, "spatial_cue_down": 4}[cue_type]
    flanker_code = 1 if flanker_type == "congruent" else 2
    pos_code = 1 if target_position == "up" else 2
    dir_code = 1 if target_direction == "left" else 2
    stim_trigger = settings.triggers.get(f"stim_{cue_code}{flanker_code}{pos_code}{dir_code}")

    set_trial_context(
        stim_unit,
        trial_id=trial_id,
        phase="flanker_response",
        deadline_s=settings.stim_duration,
        valid_keys=list(settings.key_list),
        block_id=block_id,
        condition_id=str(condition),
        task_factors={
            "condition": str(condition),
            "stage": "flanker_response",
            "cue_type": cue_type,
            "flanker_type": flanker_type,
            "target_position": target_position,
            "target_direction": target_direction,
            "block_idx": block_idx,
        },
        stim_id=stim_name,
    )
    stim_unit.capture_response(
        keys=settings.key_list,
        correct_keys=correct_response,
        duration=settings.stim_duration,
        response_trigger={
            settings.left_key: settings.triggers.get("left_key_press"),
            settings.right_key: settings.triggers.get("right_key_press"),
        },
        onset_trigger=stim_trigger,
        terminate_on_response=True,
    )
    stim_unit.to_dict(trial_data)

    # outcome display
    response = stim_unit.get_state("response", False)
    hit = stim_unit.get_state("hit", False)

    if response and hit:
        feedback_stim = stim_bank.get("correct_feedback")
        feedback_stim_id = "correct_feedback"
        feedback_trigger = settings.triggers.get("feedback_correct_response")
    elif response and not hit:
        feedback_stim = stim_bank.get("incorrect_feedback")
        feedback_stim_id = "incorrect_feedback"
        feedback_trigger = settings.triggers.get("feedback_incorrect_response")
    else:
        feedback_stim = stim_bank.get("no_response_feedback")
        feedback_stim_id = "no_response_feedback"
        feedback_trigger = settings.triggers.get("feedback_no_response")

    feedback_unit = make_unit(unit_label="feedback").add_stim(feedback_stim)
    set_trial_context(
        feedback_unit,
        trial_id=trial_id,
        phase="feedback",
        deadline_s=settings.feedback_duration,
        valid_keys=[],
        block_id=block_id,
        condition_id=str(condition),
        task_factors={
            "condition": str(condition),
            "stage": "feedback",
            "cue_type": cue_type,
            "flanker_type": flanker_type,
            "target_position": target_position,
            "target_direction": target_direction,
            "hit": bool(hit),
            "response_made": bool(response),
            "block_idx": block_idx,
        },
        stim_id=feedback_stim_id,
    )
    feedback_unit.show(
        duration=settings.feedback_duration,
        onset_trigger=feedback_trigger,
    ).to_dict(trial_data)

    iti_unit = make_unit(unit_label="iti")
    set_trial_context(
        iti_unit,
        trial_id=trial_id,
        phase="iti",
        deadline_s=settings.iti_duration,
        valid_keys=[],
        block_id=block_id,
        condition_id=str(condition),
        task_factors={
            "condition": str(condition),
            "stage": "iti",
            "cue_type": cue_type,
            "flanker_type": flanker_type,
            "target_position": target_position,
            "target_direction": target_direction,
            "block_idx": block_idx,
        },
        stim_id="blank_iti",
    )
    iti_unit.show(duration=settings.iti_duration).to_dict(trial_data)
    return trial_data
