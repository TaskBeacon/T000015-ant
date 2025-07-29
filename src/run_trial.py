from psyflow import StimUnit
from functools import partial

def run_trial(
    win,
    kb,
    settings,
    condition: str,
    stim_bank: dict,
    trigger_sender=None,
):
    """
    Runs a single trial of the Attention Network Test.

    Args:
        win: The PsychoPy window object.
        kb: The keyboard handler.
        settings: The task settings object.
        condition (str): A string defining the current trial's type.
        stim_bank: The stimulus bank containing all visual stimuli.
        trigger_sender: The object responsible for sending EEG/fMRI triggers.

    Returns:
        dict: A dictionary containing all data recorded for this trial.
    """
    trial_data = {"condition": condition}
    make_unit = partial(StimUnit, win=win, kb=kb, triggersender=trigger_sender)

    # --- 1. Determine trial properties from condition string ---
    parts = condition.split('_')
    target_direction = parts[-1]
    target_position = parts[-2]
    flanker_type = parts[-3]
    cue_type = '_'.join(parts[:-3])

    correct_response = settings.left_key if target_direction == 'left' else settings.right_key
    stim_name = f"{flanker_type}_{target_position}_{target_direction}"
    
    trial_data.update({
        "cue_type": cue_type,
        "flanker_type": flanker_type,
        "target_position": target_position,
        "target_direction": target_direction,
        "correct_response": correct_response
    })

    # --- 2. Fixation ---
    make_unit(unit_label='fixation') \
        .add_stim(stim_bank.get("fixation")) \
        .show(duration=settings.fixation_duration, onset_trigger=settings.triggers.get("fixation_onset")) \
        .to_dict(trial_data)

    # --- 3. Cue ---
    if cue_type != 'no_cue':
        if cue_type == 'center_cue':
            make_unit(unit_label='cue') \
                .add_stim(stim_bank.get("cue_center")) \
                .show(duration=settings.cue_duration, onset_trigger=settings.triggers.get("center_cue_onset")) \
                .to_dict(trial_data)
        elif cue_type == 'double_cue':
            make_unit(unit_label='cue') \
                .add_stim(stim_bank.get("cue_up")) \
                .add_stim(stim_bank.get("cue_down")) \
                .show(duration=settings.cue_duration, onset_trigger=settings.triggers.get("double_cue_onset")) \
                .to_dict(trial_data)
        elif cue_type.startswith('spatial_cue'):
            cue_pos = cue_type.split('_')[-1]
            make_unit(unit_label='cue') \
                .add_stim(stim_bank.get(f"cue_{cue_pos}")) \
                .show(duration=settings.cue_duration, onset_trigger=settings.triggers.get(f"spatial_cue_{cue_pos}_onset")) \
                .to_dict(trial_data)

    # --- 4. Flanker Stimulus & Response ---
    stim_unit = make_unit(unit_label="stimulus") \
        .add_stim(stim_bank.get(stim_name))
    
    # Determine stimulus onset trigger
    cue_code = {"no_cue": 1, "center_cue": 2, "double_cue": 3, "spatial_cue_up": 4, "spatial_cue_down": 4}[cue_type]
    flanker_code = 1 if flanker_type == 'congruent' else 2
    pos_code = 1 if target_position == 'up' else 2
    dir_code = 1 if target_direction == 'left' else 2
    stim_trigger = settings.triggers.get(f"stim_{cue_code}{flanker_code}{pos_code}{dir_code}")

    stim_unit.capture_response(
        keys=settings.key_list,
        correct_keys=correct_response,
        duration=settings.stim_duration,
        response_trigger={settings.left_key: settings.triggers.get("left_key_press"),settings.right_key: settings.triggers.get("right_key_press")},
        onset_trigger=stim_trigger,
        terminate_on_response=True
    )
    stim_unit.to_dict(trial_data)

    # --- 5. Determine Accuracy and Feedback ---
    response = stim_unit.get_state("response", False)
    hit = stim_unit.get_state("hit", False)

    if response and hit:
        feedback_stim = stim_bank.get("correct_feedback")
        feedback_trigger = settings.triggers.get("feedback_correct_response")
    elif response and not hit:
        feedback_stim = stim_bank.get("incorrect_feedback")
        feedback_trigger = settings.triggers.get("feedback_incorrect_response")
    else:
        feedback_stim = stim_bank.get("no_response_feedback")
        feedback_trigger = settings.triggers.get("feedback_no_response")

    # --- 6. Feedback ---
    make_unit(unit_label="feedback") \
        .add_stim(feedback_stim) \
        .show(duration=settings.feedback_duration, onset_trigger=feedback_trigger) \
        .to_dict(trial_data)

    # --- 7. Inter-Trial Interval (ITI) ---
    make_unit(unit_label='iti').show(duration=settings.iti_duration).to_dict(trial_data)

    return trial_data
