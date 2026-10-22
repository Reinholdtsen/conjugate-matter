---
title: "Pre-registration and its calibration record"
weight: 30
status: method
description: "Write down and commit the expected verdict and weakest link before each review round, keep them out of commit subjects, and score them afterwards: verdicts 2 for 2 in rounds 1–2, a miss in round 3, a hit in round 4; the weakest link's location forecast better, its severity still underestimated."
sources:
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "CLAUDE.md 'Working with Paul'"
  - "HANDOFF.md §5"
  - "HANDOFF.md §6"
  - "HANDOFF.md §7"
  - "review/round3-preregistration.md"
  - "review/round4-preregistration.md"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round3/referee/audit-notes.md Step 5"
  - "notes/toy-lagrangian.md 'Success criteria', 'Predictions', 'Assessment against the predictions'"
  - "review/wiki-build-flags.md item 35"
---

*Pre-registration is the practice of writing down, and committing to the repository, the verdict a blind review is expected to return and the weakest point the referee is expected to find, before the referee is dispatched. Because the forecast is fixed in advance it cannot be adjusted to the outcome, and scoring it afterwards measures how well the author judges the author's own work. The record so far: the verdict was forecast correctly in rounds 1 and 2, missed in round 3 and forecast correctly in round 4; the location of the weakest link is now forecast better, and its severity is still underestimated. Since round 3 the forecast is kept out of the commit subject, because a referee subagent sees recent commit subjects.*

**Status:** Method, in force — untagged. It is a rule of root `CLAUDE.md` ('Method') and of `HANDOFF.md` §5. The scores are recorded in `review/round3-adjudication.md` and `review/round4-adjudication.md`, which bring the handoff's "2-for-2" up to date.

## What pre-registration is

In empirical science, pre-registration means recording the hypotheses and the analysis plan before the data are seen, so that the analysis cannot be fitted to the result [T]. The program applies the idea to its own [blind reviews](/wiki/method/review/review-protocol). The "data" is the referee's report, and what is registered is the author's forecast of it. The round-3 pre-registration opens: "Written and committed **before** the round-3 audit was dispatched, so the prediction cannot be fitted to the outcome."

The rule, in root `CLAUDE.md`:

> Pre-register the expected verdict and weakest link before each review round. Keep the prediction out of the commit subject: subagents see recent commit subjects in their git-status context, and round 3's auditor saw it.

The handoff's earlier form: "before each review round, the expected verdict and weakest link were written down in advance (scored 2-for-2 on verdicts). Continue the practice; it calibrates trust." (`HANDOFF.md` §5).

## Why the program uses it

Paul "cannot independently verify most of the technical physics and relies on the tags, the machine checks and pre-registration to tell sound results from confabulation" (root `CLAUDE.md`; [the collaboration](/wiki/method/collaboration)). The handoff records the request behind this: he "has asked for explicit legit-vs-hallucination calibration: keep the tier tags, keep machine-verifying, keep pre-registering, keep reporting negative results prominently" (`HANDOFF.md` §7).

[Provenance tags](/wiki/method/provenance-tags) say where a claim came from, and [the gate](/wiki/method/verification/the-gate) says whether its arithmetic reproduces. Neither says whether the author's confidence in a manuscript is warranted. A scored forecast does. If the forecasts come out right, the author's self-assessment carries information. If they miss in a consistent direction, the author's confidence should be discounted in that direction. The adjudications draw exactly this kind of conclusion: "Calibration: my confidence in v3 was too high." (round 3), and "Severity is still underestimated." (round 4).

## What a pre-registration contains

The two pre-registrations in the repository, `review/round3-preregistration.md` and `review/round4-preregistration.md`, have the same parts:

- **The set-up:** the manuscript and the commit that fixes its text, the auditor and its tools, and the protocol's stated limitation ("same model family as the author").
- **The verdict**, with a confidence, and the reasons it is neither the grade above nor the grade below. Round 4: "It is not C: every number was computed by gated code with independent anchors, and the claims are narrowly scoped, with limitations stated." and "It is not A: the significance is thin, and at least one argument is explicitly incomplete."
- **The single weakest link**, argued in a few lines, and the runners-up in order.
- **Arithmetic:** how many numerical indictments are expected to survive arbitration, and where one would most likely land.
- **Citations:** whether all references will resolve, and which one is likeliest to be cited for more than it says.

The toy-model work used the same discipline for a calculation rather than a review. Its worklog fixed the success criteria "before any construction", wrote predictions before construction, and assessed them afterwards ([success criteria S0–S5 and the pre-registered predictions](/wiki/symmetry-breaking/toy-models/success-criteria)).

## The record, round by round

### Rounds 1 and 2

Both rounds of the [skeptic review console](/wiki/method/review/skeptic-console) on #14 were pre-registered. The round-3 pre-registration: "Rounds 1 and 2 were pre-registered the same way and scored 2 for 2 on verdicts (HANDOFF §6)." (On that pointer, see flag 35 in `review/wiki-build-flags.md`.) The referees returned "B / medium" and "B near B/C / medium" (`HANDOFF.md` §6). The forecasts themselves are not in the repository, and no document records how their weakest-link forecasts scored ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

### Round 3

The forecast for #14 v3 ([round-3 pre-registration](/wiki/method/review/round-3/preregistration)): verdict B with medium confidence; "Weakest link: the framework does no work", with three ranked runners-up; on arithmetic, "zero surviving numerical indictments", since every number had been computed by a gated script, `knot_numbers.py` (since replaced; its last version is in the repository history at 96f58da); and "all 23 resolve" for the citations, with "[5] on heavy-spin-2 stability or [11] on global symmetries" as the likeliest over-citations.

The adjudication scored it (`review/round3-adjudication.md`, 'Pre-registration scored'):

| Prediction | Outcome | Score |
|---|---|---|
| Verdict B | C | **Miss**: the first after 2 for 2 |
| Weakest link: "the framework does no work" | The referee's #2; its #1 was the abundance normalization | **Miss on #1** (hit on #2) |
| Zero surviving numerical indictments | Three survive (p; the ψ window; ξ), plus the ε coefficient | **Miss**. All are wrong inputs or model choices in my scripts, not arithmetic slips |
| All 23 citations resolve | All exist | **Hit** |
| A misattribution most likely in [5] or [11] | The referee's one misattribution claim (Baumgart) was itself wrong; [4] was flagged as over-generalized | Miss |

In the arithmetic row, every number in v3 had passed a script, and three still fell, together with the coefficient in the estimate of the kinetic-mixing parameter ε, because the scripts encoded wrong inputs or model choices: the Kibble normalization p, the ψ relic window and the bound on the temperature ratio ξ ([round-3 rulings](/wiki/method/review/round-3/rulings)). The adjudication's conclusion: "Calibration: my confidence in v3 was too high. The failure mode has moved." ([the measured failure mode](/wiki/method/review/referee-failure-mode)). The adjudication does not score the list of runners-up.

### Round 4

The forecast for the toy-model note ([review round 4](/wiki/method/review/round-4)): verdict B with medium confidence. The weakest link: "in 1+1, the 'spontaneous' breaking of ρ rests on an explicit, rigid background", the fixed pair of axes K_ref that the ρ-preserving potential needs. Runners-up, in order: model II's quantum-restoration argument, the real-versus-complex distinction, and the weak form of matter locality. On arithmetic, "at most one surviving numerical indictment", most likely "a normalization or convention: the spin-wave exponent, the 8π(m+n+1) coefficient, or the Δ sign convention". On citations, "all 12 resolve", with [12] (José et al.) the likeliest over-cited.

The adjudication scored it (`review/round4-adjudication.md`, 'Pre-registration scored'):

| Prediction | Outcome | Score |
|---|---|---|
| Verdict B | B | **Hit** |
| Weakest link: §4's breaking rests on a rigid background (K_ref) | Same place, worse defect: the potential is unbounded below with H dynamical | **Partial**: right location, missed severity |
| Runner-ups: model II restoration argument; real-vs-complex; weak S5 by construction | Restoration conclusion confirmed but must be restated (F6, Langmann–Szabo–Zarembo); real-vs-complex confirmed and extended (F4); I_K needs H (F5) | Partial on all three |
| At most one surviving numerical indictment, likeliest a normalization or sign | One: the MC control values, a statistical problem. Every normalization and sign I listed was confirmed | **Hit on count, miss on location** |
| All 12 citations resolve; likeliest over-cited is [12] | All resolve; [12]'s specific claim is unverifiable; also [8] (d = 1 only) and [11] (author's initial) | **Hit** |

The table is quoted with one abbreviation spelled out (the Langmann–Szabo–Zarembo exact solution). In it, MC is Monte Carlo, and S5 is the toy work's success criterion on matter locality. The forecast found the right place and missed what was there: the potential at K_ref was not merely put in by hand, it was unbounded below once the field H could vary ([obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). The one surviving numerical indictment was statistical, Monte Carlo values quoted from fixed seeds without error bars ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)), and none of the normalizations or signs the author had worried about.

### Across rounds

The round-4 adjudication sums up the record:

- "Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4)."
- "Weakest-link location has improved. Severity is still underestimated."

| Round | Manuscript | Forecast verdict | Referee's verdict | Verdict score |
|---|---|---|---|---|
| 1 | #14 v1 | not in the repository | B / medium | scored 2 for 2 with round 2 |
| 2 | #14 v2 | not in the repository | B near B/C / medium | scored 2 for 2 with round 1 |
| 3 | #14 v3 | B, medium | C, medium | Miss |
| 4 | toy-model note | B, medium | B, ~0.75 | Hit |

In both scored rounds the referee found a more serious defect than the author had forecast: in round 3 in a different place, in round 4 in the forecast place. In both, the arithmetic forecast expected no more than a slip in a normalization or an estimate, and the indictments that survived were of another kind: wrong model inputs in round 3, missing statistics in round 4.

## Keeping the forecast from the referee

Round 3's pre-registration was committed (cc05705) with a commit subject that stated the forecast. The referee subagent's environment attached a snapshot of `git status` with the latest commit subjects, though the referee read nothing in the repository itself. Its reproducibility note: "nothing under /home/paul/git was read. The harness auto-attached a git-status snapshot whose latest commit subject mentions a pre-registered expected verdict; it was not consulted for any finding." (`review/round3/referee/audit-notes.md`, Step 5).

The adjudication's first lesson weighs it: "The auditor says it did not use it, and its verdict differed from the prediction, which argues against anchoring. But the round was less blind than intended." ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions)). The commit-subject clause entered the rule in root `CLAUDE.md`. Round 4's pre-registration states that it follows it: "Per the round-3 lesson, the commit subject does not state the prediction." The adjudication confirms it was "committed before dispatch with a neutral subject", and the repository history shows that subject for d9a06ac: "Pre-register round 4; toy-model note for review".

## What it does not do

- It does not make the review more independent. The referee is still "the same model family as the author" ([the review protocol](/wiki/method/review/review-protocol#limits)).
- The scoring is the author's. The labels Hit, Partial and Miss and the calibration statements are written in the adjudications, in the first person.
- The forecasts of rounds 1 and 2 cannot be re-examined, since only their score survives.

## Sources

- `CLAUDE.md` 'Method (HANDOFF §5)' — the rule, including the commit-subject clause; 'Working with Paul' — Paul's reliance on pre-registration
- `review/round3-preregistration.md`, `review/round4-preregistration.md` — the two pre-registrations in the repository: forecasts, reasons and the neutral-subject statement
- `review/round3-adjudication.md` 'Pre-registration scored', 'Lessons (now in CLAUDE.md)' — round 3's scores, the calibration statement and the leak lesson
- `review/round4-adjudication.md` 'Pre-registration scored' — round 4's scores and the calibration across rounds
- `review/round3/referee/audit-notes.md` Step 5 — the referee's reproducibility note on the leak
- `HANDOFF.md` §5, §6, §7 — the rule as handed over, with the superseded "2-for-2"; the round-1 and round-2 verdicts; the request for explicit calibration
- `notes/toy-lagrangian.md` 'Success criteria (fixed 2026-10-19, before any construction)', 'Predictions (written before construction)' — the same discipline applied to the toy-model calculation
- `review/wiki-build-flags.md` item 35 — the round-3 file's pointer to `HANDOFF.md` §6 for the 2-for-2 record, awaiting a ruling
