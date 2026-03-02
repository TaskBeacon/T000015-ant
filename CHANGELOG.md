# CHANGELOG

All notable development changes for `T000015-ant` are documented here.

## [1.1.2] - 2026-03-02

### Added
- Added full reference artifact bundle under `references/`:
  - `references.yaml`
  - `references.md`
  - `parameter_mapping.md`
  - `stimulus_mapping.md`
  - `task_logic_audit.md`
- Added ANT-specific simulation responder behavior in `responders/task_sampler.py`.

### Changed
- Updated `main.py` finalize flow so goodbye no longer terminates before save/close.
- Updated voice conversion call to list-based API (`["instruction_text"]`).
- Updated `config/config_scripted_sim.yaml` scripted responder key to valid task key (`f`).
- Updated `config/config_sampler_sim.yaml` to ANT-specific sampler kwargs.
- Updated `responders/__init__.py` to export `TaskSamplerResponder`.
- Rewrote `README.md` to current contract structure and added `### Controller Logic`.
- Updated `taskbeacon.yaml` release tag, evidence list, and maintainer metadata.

## [1.1.1] - 2026-02-18

### Changed
- Refactored responder context phase names in `src/run_trial.py` to task-specific labels.
- Updated stage comments in `src/run_trial.py` for cleaner auditability.

### Fixed
- Removed legacy generic stage comment patterns from runtime trial code.

## [1.1.0] - 2026-02-17

### Added
- Added mode-aware main flow for `human`, `qa`, and `sim`.
- Added split runtime configs for qa/scripted sim/sampler sim.
- Added task-local responder scaffold in `responders/task_sampler.py`.
- Added output scaffolding (`outputs/.gitkeep`) and standardized `.gitignore` rules.

### Changed
- Aligned trigger config to structured schema (`triggers.map`, `triggers.driver`, `triggers.policy`, `triggers.timing`).
- Added responder context injection via `set_trial_context(...)` in trial runtime.
