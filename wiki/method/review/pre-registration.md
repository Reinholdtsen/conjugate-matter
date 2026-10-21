---
title: "Pre-registration and its calibration record"
weight: 30
status: method
description: "Write the expected verdict and weakest link before each round, keep them out of commit subjects, and score them afterwards: 2 for 2, then a miss in round 3, then a hit in round 4."
sources:
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "HANDOFF.md §5"
  - "review/round3-preregistration.md"
  - "review/round4-preregistration.md"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round3/referee/audit-notes.md Step 5"
---

*Pre-registration is the practice of writing down, and committing to the repository, the verdict a review is expected to return and the weakest point the referee is expected to find, before the referee is dispatched. Because the forecast is fixed in advance it cannot be adjusted to the outcome, and scoring it afterwards measures how well the author judges the author's own work. The record so far: the verdict was forecast correctly in rounds 1 and 2, missed in round 3 (B forecast, C returned) and forecast correctly in round 4; the location of the weakest link is now forecast better, and its severity is still underestimated. Since round 3 the forecast is kept out of the commit subject, because a referee subagent sees recent commit subjects.*

**Status:** Method, in force — untagged — a rule of `CLAUDE.md` 'Method' and `HANDOFF.md` §5; the scores are recorded in `review/round3-adjudication.md` and `review/round4-adjudication.md`, which supersede the handoff's "2-for-2".

## Key facts

- **The rule** (`CLAUDE.md`): "Pre-register the expected verdict and weakest link before each review round. Keep the prediction out of the commit subject: subagents see recent commit subjects in their git-status context, and round 3's auditor saw it." The handoff's version: "before each review round, the expected verdict and weakest link were written down in advance (scored 2-for-2 on verdicts). Continue the practice; it calibrates trust." In empirical science the same word means registering hypotheses and the analysis plan before the data are seen [T].
- **Why it matters here.** Paul "cannot independently verify most of the technical physics and relies on the tags, the machine checks and pre-registration to tell sound results from confabulation" (`CLAUDE.md`; [the collaboration](/wiki/method/collaboration)).
- **What a pre-registration contains** (rounds 3 and 4): the verdict with a confidence and the reasons it is not the grade above or the grade below; the single weakest link and ranked runners-up; the expected number of surviving numerical indictments and where they would most likely land; and whether the citations will resolve, with the likeliest over-cited reference. The toy-model work used the same practice for its success criteria ([S0–S5 and the pre-registered predictions](/wiki/symmetry-breaking/toy-models/success-criteria)).
- **Round 3, scored** ([round-3 pre-registration](/wiki/method/review/round-3/preregistration)): verdict B against C, "**Miss**: the first after 2 for 2"; weakest link "the framework does no work", the referee's second, "**Miss on #1** (hit on #2)"; zero surviving numerical indictments against "Three survive (p; the ψ window; ξ), plus the ε coefficient", a miss; all 23 citations resolve, a hit; a misattribution most likely in [5] or [11], a miss. "Calibration: my confidence in v3 was too high."
- **Round 4, scored** ([round 4](/wiki/method/review/round-4)): verdict B against B, "**Hit**"; weakest link, the rigid background K_ref, "**Partial**: right location, missed severity"; runners-up "Partial on all three"; at most one surviving numerical indictment, "**Hit on count, miss on location**" (the one survivor was the Monte Carlo control values); all 12 citations resolve, a hit.
- **Calibration across rounds** (`review/round4-adjudication.md`): "Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4)." "Weakest-link location has improved. Severity is still underestimated."
- **The leak.** Round 3's pre-registration was committed (cc05705) with a subject that stated the forecast verdict and weakest link. The referee's notes: "The harness auto-attached a git-status snapshot whose latest commit subject mentions a pre-registered expected verdict; it was not consulted for any finding." The adjudication: the verdict differed from the prediction, "which argues against anchoring. But the round was less blind than intended." ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions)). Round 4's pre-registration was committed "with a neutral subject" (d9a06ac, "Pre-register round 4; toy-model note for review").

## Sources

- `CLAUDE.md` 'Method (HANDOFF §5)' — the rule, including the commit-subject clause; Paul's reliance on it ('Working with Paul')
- `HANDOFF.md` §5 — the rule as handed over, with the superseded "2-for-2"
- `review/round3-preregistration.md`, `review/round4-preregistration.md` — the two pre-registrations in the repository
- `review/round3-adjudication.md` 'Pre-registration scored', 'Lessons (now in CLAUDE.md)' — round 3's score and the leak lesson
- `review/round4-adjudication.md` 'Pre-registration scored' — round 4's score and the calibration across rounds
- `review/round3/referee/audit-notes.md` Step 5 — the referee's reproducibility note on the leak
