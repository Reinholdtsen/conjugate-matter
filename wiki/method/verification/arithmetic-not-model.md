---
title: "Verification checks arithmetic, not the model"
weight: 20
status: method
description: "A script confirms the arithmetic of the model it encodes; the soliton manuscript's wrong input passed such a script, and only independent review caught it."
sources:
  - "papers/broken-born-checkpoint-v2.md §2"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3-preregistration.md"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md §6"
  - "CLAUDE.md 'Method'"
  - "review/round4-adjudication.md 'Rulings'"
---

*A verification script confirms that a calculation was carried out correctly for the inputs and formulas written into it; it cannot tell whether those inputs and formulas are the right physics. The program learned this from its soliton dark-matter manuscript: every number in it was computed and checked by a gated script, yet one input, the normalization of how many monopoles the early universe forms, was wrong, and only an independent review caught it. Checkpoint #11 has carried the caution since version 2.1, and the program's rule on independent anchors is the repair.*

**Status:** Method, in force since #11 v2.1 — untagged — #11 §2 and root `CLAUDE.md` ('Method'); round-3 ruling 13, "Upheld in substance".

## Key facts

- **The caution.** "A caution added in v2.1: a verification script confirms arithmetic, not the model it encodes — the §12 failure passed a script whose physics input was wrong, and was caught only by an independent review." (#11 §2). Root `CLAUDE.md`: "A verification check confirms arithmetic, not the model."
- **The claim that overstated.** The soliton manuscript (#14 v3) said: "All numerical statements in Secs. 2-4 were computed by executed code rather than by hand." (§6). The v3 worklog records that every number v3 quotes was "a gated check" in knot_numbers.py, a script since retired and kept in git history ([The soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).
- **What the referee found.** "Sec. 6 says all numbers were computed by executed code; the p error (a dropped prefactor of 4576) and the psi window (factor 3-10 in mass) indicate otherwise or a coding error." (round-3 audit notes, Step 4(a) item 9).
- **The ruling.** Ruling 13: "v3 §6 "all numbers computed by executed code" overstates" — "Upheld in substance" — "The code checked the arithmetic of a wrong model. See lesson 2." The wrong input was ruling 1's: "Kibble normalization: one defect per Hubble volume is p ≈ 104, not 0.023" — "My error came from misremembering the formula." See [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) and [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings).
- **The prediction it broke.** The round-3 pre-registration expected "zero surviving numerical indictments", because every number had been computed by knot_numbers.py. Outcome: "Three survive (p; the ψ window; ξ), plus the ε coefficient" — "Miss. All are wrong inputs or model choices in my scripts, not arithmetic slips". See [Pre-registration and its calibration record](/wiki/method/review/pre-registration).
- **The failure mode moved.** "In rounds 1–2 it was the referee's unaided arithmetic. In round 3 it is that the author's verification checks the author's model: a wrong physics input passes a gate that tests only arithmetic." (`review/round3-adjudication.md`; [The measured referee failure mode](/wiki/method/review/referee-failure-mode)).
- **The repair.** Lesson 2: "An anchor must be independent of the paper. v3's Kibble anchor reproduced v2's own number and so tested nothing." ([Independent anchors](/wiki/method/verification/independent-anchors)). Round 4 found a related gap, a stability check made only on a reduced model: "I checked the potential only at frozen H." ([The reduced-model stability rule](/wiki/method/verification/reduced-model-stability)).
- **What remains unchecked by any script.** #11 §2's plain-language passage: "What no machine can check is whether the algebra is attached to the right physics; that verdict belongs to expert readers and, ultimately, to data." ([Claim tiers and selection bias](/wiki/method/claim-tiers)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §2 — the v2.1 caution and the limit of Tier 1
- `review/round3-adjudication.md` 'Rulings' (1, 13), 'Pre-registration scored', 'Lessons (now in CLAUDE.md)' — the ruling, the missed prediction, the moved failure mode, the anchor lesson
- `review/round3/referee/audit-notes.md` Step 4(a) item 9 — the referee's finding
- `review/round3-preregistration.md` — the prediction of zero surviving numerical indictments
- `review/v3-worklog.md` 'v3 as drafted (2026-10-19)' and `notes/knot-dark-matter-standalone.md` §6 — the manuscript's claim that every number was computed
- Root `CLAUDE.md` 'Method' — the rule as now stated
- `review/round4-adjudication.md` 'Rulings' (F2) — the related round-4 gap
