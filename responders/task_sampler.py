from __future__ import annotations

from typing import Any

from psyflow.sim.contracts import Action, Feedback, Observation, SessionInfo


class TaskSamplerResponder:
    """Task-specific sampler responder for ANT."""

    def __init__(
        self,
        *,
        left_key: str = "f",
        right_key: str = "j",
        p_correct_congruent: float = 0.90,
        p_correct_incongruent: float = 0.78,
        p_miss: float = 0.05,
        rt_congruent_mean_s: float = 0.42,
        rt_incongruent_mean_s: float = 0.50,
        rt_sd_s: float = 0.08,
        rt_min_s: float = 0.15,
        continue_rt_s: float = 0.25,
    ):
        self.left_key = str(left_key)
        self.right_key = str(right_key)
        self.p_correct_congruent = float(p_correct_congruent)
        self.p_correct_incongruent = float(p_correct_incongruent)
        self.p_miss = float(p_miss)
        self.rt_congruent_mean_s = float(rt_congruent_mean_s)
        self.rt_incongruent_mean_s = float(rt_incongruent_mean_s)
        self.rt_sd_s = max(1e-6, float(rt_sd_s))
        self.rt_min_s = max(0.0, float(rt_min_s))
        self.continue_rt_s = float(continue_rt_s)
        self._rng: Any = None

    def start_session(self, session: SessionInfo, rng: Any) -> None:
        self._rng = rng

    def _pick_key(self, valid_keys: list[str], preferred: str | None = None) -> str | None:
        if not valid_keys:
            return None
        if preferred and preferred in valid_keys:
            return preferred
        return valid_keys[0]

    def _sample_rt(self, mean_s: float) -> float:
        if self._rng is None:
            return max(self.rt_min_s, mean_s)
        return max(self.rt_min_s, float(self._rng.gauss(mean_s, self.rt_sd_s)))

    def _deadline(self, obs: Observation) -> float | None:
        if obs.deadline_s is not None:
            return float(obs.deadline_s)
        if obs.response_window_s is not None:
            return float(obs.response_window_s)
        return None

    def _infer_correct_key(self, obs: Observation) -> str:
        condition = str(obs.condition_id or "").strip().lower()
        if condition.endswith("_left"):
            return self.left_key
        if condition.endswith("_right"):
            return self.right_key

        factors = dict(obs.task_factors or {})
        direction = str(factors.get("target_direction", "")).strip().lower()
        if direction == "left":
            return self.left_key
        return self.right_key

    def _is_incongruent(self, obs: Observation) -> bool:
        condition = str(obs.condition_id or "").strip().lower()
        if "incongruent" in condition:
            return True
        factors = dict(obs.task_factors or {})
        return str(factors.get("flanker_type", "")).strip().lower() == "incongruent"

    def act(self, obs: Observation) -> Action:
        if isinstance(obs, dict):
            obs = Observation.from_dict(obs)
        valid_keys = list(obs.valid_keys or [])
        phase = str(obs.phase or "").strip().lower()

        if phase in ("instruction_text", "block", "block_feedback", "goodbye"):
            key = self._pick_key(valid_keys)
            if key is None:
                return Action(key=None, rt_s=None, meta={"source": "task_sampler", "reason": "no_valid_key"})
            return Action(key=key, rt_s=max(0.01, self.continue_rt_s), meta={"source": "task_sampler", "phase": phase})

        if phase not in ("stimulus", "flanker_response") or self._rng is None:
            return Action(key=None, rt_s=None, meta={"source": "task_sampler", "phase": phase, "reason": "withhold"})

        if float(self._rng.random()) < self.p_miss:
            return Action(key=None, rt_s=None, meta={"source": "task_sampler", "outcome": "miss"})

        correct_key = self._infer_correct_key(obs)
        incongruent = self._is_incongruent(obs)
        p_correct = self.p_correct_incongruent if incongruent else self.p_correct_congruent

        if float(self._rng.random()) <= p_correct:
            key = self._pick_key(valid_keys, preferred=correct_key)
            outcome = "correct"
        else:
            alt_keys = [k for k in valid_keys if k != correct_key]
            key = self._pick_key(alt_keys)
            outcome = "error"
            if key is None:
                return Action(key=None, rt_s=None, meta={"source": "task_sampler", "outcome": "miss"})

        mean_s = self.rt_incongruent_mean_s if incongruent else self.rt_congruent_mean_s
        rt_s = self._sample_rt(mean_s)
        deadline = self._deadline(obs)
        if deadline is not None and rt_s > deadline:
            return Action(key=None, rt_s=None, meta={"source": "task_sampler", "outcome": "late"})

        return Action(key=key, rt_s=rt_s, meta={"source": "task_sampler", "outcome": outcome})

    def on_feedback(self, fb: Feedback) -> None:
        return None

    def end_session(self) -> None:
        return None
