Use case: infographic-diagram
Asset type: TaskBeacon task flow diagram
Primary request: Create a clean, publication-ready task flow diagram as a timeline collection for the behavioral task described below.

Task: Attention Network Test (ANT)
Construct: alerting / orienting / executive control
Rows/conditions:
- No cue: fixation directly precedes target.
- Center cue: center * cue precedes target.
- Double cue: upper and lower * cues precede target.
- Spatial cue: upper or lower * cue precedes target location.

Timeline phases:
- No cue: Fixation (500 ms; no scored response; +) -> Flanker response (1000 ms; F = left, J = right; respond to center arrow; examples <<<<< or >><>>) -> Feedback (500 ms; no response; correct / incorrect / no response) -> ITI (800-1200 ms; no response; blank screen)
- Center cue: Fixation (500 ms; no scored response; +) -> Cue (100 ms; no response; center *) -> Flanker response (1000 ms; F = left, J = right; respond to center arrow; congruent or incongruent arrows) -> Feedback (500 ms; no response; correct / incorrect / no response) -> ITI (800-1200 ms; no response; blank screen)
- Double cue: Fixation (500 ms; no scored response; +) -> Cue (100 ms; no response; upper * and lower *) -> Flanker response (1000 ms; F = left, J = right; respond to center arrow; target row up or down) -> Feedback (500 ms; no response; correct / incorrect / no response) -> ITI (800-1200 ms; no response; blank screen)
- Spatial cue: Fixation (500 ms; no scored response; +) -> Cue (100 ms; no response; upper or lower *) -> Flanker response (1000 ms; F = left, J = right; respond to center arrow at cued/uncued row) -> Feedback (500 ms; no response; correct / incorrect / no response) -> ITI (800-1200 ms; no response; blank screen)

Visual requirements:
- White background, landscape orientation, crisp dark text, restrained condition accent colors.
- One horizontal row per condition or representative trial type.
- Each row contains 3-7 participant-screen snapshots connected by a subtle arrow.
- Each screen snapshot shows the visible stimulus or feedback, not internal variable names.
- Use gray participant-screen boxes, thin black arrows, consistent row spacing, and subtle row separators.
- Place timing labels under each screen in compact text.
- Place condition labels at the left of each row.
- Use short labels only; avoid paragraphs inside the image.
- Make all text legible at normal document preview size.
- Leave a clean blank header band across the top 15-18% of the image. This band is reserved for a fixed title, `Construct: ...` subtitle, and TaskBeacon logo lockup that will be added after generation.

Accuracy constraints:
- Do not invent phases, stimuli, condition names, keys, rewards, or timings.
- Do not add people, lab equipment, decorative scenes, logos, or unrelated icons.
- Do not draw the task title, construct subtitle, any logo, watermark, brand mark, or `TaskBeacon` text inside the generated image.
- Draw only the timeline content below the blank header band.
- If a detail is unknown, omit it rather than guessing.
- Preserve these exact terms where used: No cue, Center cue, Double cue, Spatial cue, Fixation, Cue, Flanker response, Feedback, ITI, F = left, J = right, center arrow, 500 ms, 100 ms, 1000 ms, 800-1200 ms, correct, incorrect, no response, <<<<<, >><>>, <<><<.
- Collapse equivalent flanker and target-location variants into compact examples; do not draw all 48 condition tokens.

Style:
TaskBeacon scientific infographic style: clean vector-like raster image, organized spacing, gray screen boxes, restrained color accents, and a blank header-safe area.
