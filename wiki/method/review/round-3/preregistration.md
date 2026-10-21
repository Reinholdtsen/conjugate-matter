---
title: "Round-3 pre-registration"
weight: 10
status: record
description: "Predicted verdict B with 'the framework does no work' as the weakest link and zero surviving numerical indictments — and the commit subject that leaked it."
sources:
  - "review/round3-preregistration.md"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3/referee/audit-notes.md Step 5"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
---

*The round-3 pre-registration is the forecast of the round-3 review, written and committed on 2026-10-19 before the referee was dispatched (`review/round3-preregistration.md`, commit cc05705). It predicted verdict B with medium confidence, named "the framework does no work" as the weakest link, expected no numerical indictment to survive, and expected all 23 citations to resolve. The referee returned C, so the verdict forecast missed for the first time after two hits; of the forecasts, only "all 23 resolve" was scored a hit outright. The commit's subject line also stated the forecast, and the referee's environment displayed it, which made the round less blind than intended.*

**Status:** Record — untagged — scored in `review/round3-adjudication.md` 'Pre-registration scored' ([verdict and rulings](/wiki/method/review/round-3/rulings)); the leak became the commit-subject clause of [pre-registration](/wiki/method/review/pre-registration) in `CLAUDE.md` 'Method'.

## Key facts

- **The set-up.** Manuscript: #14 v3, "as of commit 5dbaa82" (cited at its old path in papers/; now `notes/knot-dark-matter-standalone.md`, withdrawn). Auditor: "a fresh subagent with shell, Python (numpy/sympy/scipy) and web search", given "only a copy of the manuscript and the protocol" ([the review protocol](/wiki/method/review/review-protocol)). Limitation: "the auditor is the same model family as the author. It removes the arithmetic failure mode of rounds 1–2, which had no code execution. It does not remove correlated blind spots."
- **Verdict: B** ("flawed but salvageable"), confidence medium. "It is not A: the toy action (acceptance criterion 1) does not exist, and two of v3's own exclusion tests (the millicharged ψ window and the strong-coupling relic) are stated but not evaluated." "It is not C: v3 removes v2's known internal contradictions (§2 vs §3 coupling; the ε·g premise; the 'Kibble-only' window)."
- **Weakest link: "the framework does no work."** "The candidate in §2–§4 is a standard hidden-sector monopole model. Nothing numerical depends on Born reciprocity, the compatibility theorem or the polarization identification." ([the 'framework does no work' critique](/wiki/program/framework-does-no-work))
- **Runners-up**, in order: the unevaluated millicharge bounds on ψ "at ε ~ 10⁻⁷–10⁻⁶, MeV–0.1 TeV"; thermal-history consistency (freeze-out "computed at ξ = 1, but dark radiation requires ξ < 0.77"; [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)); and "the strong-coupling annihilation at α_m ≈ 34 (criterion 3)".
- **Arithmetic and citations.** "Zero surviving numerical indictments. Every number was computed by" the gate's script for v3 (`knot_numbers.py`, since retired; [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). Citations: "all 23 resolve", with the likeliest problems the two references not live-checked, "or a reference cited for slightly more than it says, such as [5] on heavy-spin-2 stability or [11] on global symmetries."
- **The score** (adjudication): verdict "**Miss**: the first after 2 for 2"; weakest link "**Miss on #1** (hit on #2)", since the referee's first was "the abundance normalization"; arithmetic a miss, with "Three survive (p; the ψ window; ξ), plus the ε coefficient"; citations "**Hit**"; the misattribution forecast a miss, since "The referee's one misattribution claim (Baumgart) was itself wrong; [4] was flagged as over-generalized."
- **The leak.** The commit's subject named the expected verdict and weakest link. The referee: "The harness auto-attached a git-status snapshot whose latest commit subject mentions a pre-registered expected verdict; it was not consulted for any finding." The adjudication's lesson 1: "Keep the prediction out of the pre-registration commit subject"; the verdict differed from the prediction, "which argues against anchoring. But the round was less blind than intended." ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions))

## Sources

- `review/round3-preregistration.md` — the forecast, the protocol and the stated limitation
- `review/round3-adjudication.md` 'Pre-registration scored', 'Lessons (now in CLAUDE.md)' — the score and the leak lesson
- `review/round3/referee/audit-notes.md` Step 5 — the referee's reproducibility note on the commit subject
- `CLAUDE.md` 'Method (HANDOFF §5)' — the rule as it now stands
