---
title: "The measured referee failure mode"
weight: 40
status: record
description: "Rounds 1–2: referees strong on structure and literature and unreliable on unaided arithmetic; round 3: the author's verification checks the author's model."
sources:
  - "HANDOFF.md §6"
  - "HANDOFF.md §5"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-preregistration.md"
  - "review/round4-adjudication.md 'Rulings'"
  - "papers/broken-born-checkpoint-v2.md §2"
---

*The measured referee failure mode is the program's record of where its reviews have gone wrong, and on which side. In rounds 1 and 2 the referees, which could search the web but not run code, were reliable on structure, literature and logic and unreliable on arithmetic: their three confident order-of-magnitude indictments were all their own unit errors, and none survived. That finding made the iron rule load-bearing and was the main reason the project moved to Claude Code, where a referee can execute code. In round 3 the failure moved to the author's side: the author's scripts had checked the arithmetic of a model with a wrong physics input, so a gate that tests only arithmetic passed it.*

**Status:** Record — untagged — the round-1–2 form is `HANDOFF.md` §6; the round-3 form, from `review/round3-adjudication.md` 'Pre-registration scored', is the current lesson. The second extends the first and does not replace it.

## Key facts

- **Rounds 1–2** (`HANDOFF.md` §6, "Measured failure mode (both rounds + consistent)"): fresh large-language-model referees are "strong on structure, literature and logic; **unreliable on unaided arithmetic** (3 confident order-of-magnitude indictments, all reviewer unit errors, 0 surviving). Hence the iron rule. Claude Code's native execution removes this failure mode — that's the main reason the project is moving to you."
- **The referees' errors**, as the handoff lists them ([rounds 1 and 2](/wiki/method/review/rounds-one-and-two)): in round 1, "GeV→gram conversion off 10³; σ_T/M misread as σ_T (off ~10⁴³)", and the insinuation that the compatibility theorem might be false; in round 2, "fed ρ_DM = 1.26×10⁻³ GeV/cm³ instead of 1.26×10⁻⁶ (the manuscript's own number) — with the right input the closure lands within 3%", and "conflated mean vs local density labels". All were "machine-arbitrated".
- **What followed.** The handoff makes [the iron rule](/wiki/method/verification/iron-rule) "load-bearing — see §6", and [the review protocol](/wiki/method/review/review-protocol) gives the referee code execution: "It removes the arithmetic failure mode of rounds 1–2, which had no code execution. It does not remove correlated blind spots." (round-3 pre-registration).
- **Round 3** (`review/round3-adjudication.md`): "Calibration: my confidence in v3 was too high. The failure mode has moved. In rounds 1–2 it was the referee's unaided arithmetic. In round 3 it is that **the author's verification checks the author's model**: a wrong physics input passes a gate that tests only arithmetic."
- **The evidence.** The pre-registration expected zero surviving numerical indictments; "Three survive (p; the ψ window; ξ), plus the ε coefficient", and "All are wrong inputs or model choices in my scripts, not arithmetic slips". Ruling 13 upheld in substance that #14's claim of "all numbers computed by executed code" overstated: "The code checked the arithmetic of a wrong model." ([round-3 rulings](/wiki/method/review/round-3/rulings); [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization))
- **The rules it produced.** #11 §2 (v2.1): "a verification script confirms arithmetic, not the model it encodes — the §12 failure passed a script whose physics input was wrong, and was caught only by an independent review" ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)); and round 3's second lesson, that an anchor must be independent of the paper ([independent anchors](/wiki/method/verification/independent-anchors)).
- **Round 4.** The decisive finding was again a defect the author's checks had missed: "I should have caught F1 myself: I checked the potential only at frozen H." It became [the reduced-model stability rule](/wiki/method/verification/reduced-model-stability). The one surviving numerical indictment was statistical: Monte Carlo control values computed with fixed seeds and quoted without error bars ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars); [round 4](/wiki/method/review/round-4)).

## Sources

- `HANDOFF.md` §6 — the measured failure mode of rounds 1–2 and the referees' errors
- `HANDOFF.md` §5 — the iron rule, "load-bearing — see §6"
- `review/round3-preregistration.md` — what code execution removes and what it does not
- `review/round3-adjudication.md` 'Pre-registration scored', 'Rulings' (13) — the shift to the author's side
- `papers/broken-born-checkpoint-v2.md` §2 — "a verification script confirms arithmetic, not the model it encodes"
- `review/round4-adjudication.md` 'Rulings' (F2, the Monte Carlo control) — round 4's author-side findings
