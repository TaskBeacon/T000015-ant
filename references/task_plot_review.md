# Task Plot Review

## Evidence Match

- Pass: title and construct match ANT task metadata and logic.
- Pass: No cue, Center cue, Double cue, and Spatial cue rows represent the configured cue categories.
- Pass: No cue row correctly omits the cue phase.
- Pass: phase order matches implementation and README: Fixation -> optional Cue -> Flanker response -> Feedback -> ITI.
- Pass: timing labels match config: 500 ms fixation, 100 ms cue, 1000 ms response window, 500 ms feedback, 800-1200 ms ITI.
- Pass: response mapping is correct: F = left and J = right, based on the center arrow.
- Pass: flanker examples represent congruent and incongruent variants without expanding all 48 condition tokens.

## Visual Quality

- Pass: rows and arrows are readable at preview size.
- Pass: generated content stays below the header band.
- Pass: fixed title and Construct subtitle are centered.
- Pass: top-right TaskBeacon logo lockup is borderless and non-overlapping.
- Pass: no generated title, logo, watermark, people, devices, or decorative scene is present.

## README Embed

- Pass: `README.md` contains `## 2. Task Flow`.
- Pass: the section embeds `![Task Flow](task_flow.png)`.
- Pass: final image is saved as `task_flow.png`; raw timeline is saved as `references/task_plot_timeline_raw.png`.
