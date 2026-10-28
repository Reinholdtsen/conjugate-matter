---
title: "Pre-registration and its calibration record"
weight: 30
status: method
description: "Write down and fix the expected verdict and weakest link before each review round (by a commit, or in round 5 by a recorded hash), keep them out of commit subjects, and score them afterwards: verdicts 2 for 2 in rounds 1–2, a miss in round 3, hits in rounds 4 and 5; the weakest link's location hit in rounds 4 and 5, with the severity of a defect, the number of small errors and the extent of prior art underestimated."
sources:
  - "review/momentum-gravity/README.md"
  - "review/momentum-gravity/preregistration-run2.md"
  - "review/momentum-gravity/preregistration-run3.md"
  - "review/momentum-gravity/preregistration-run4.md"
  - "notes/velocity-gated-gravity.md §11"
  - "notes/gate-mechanism.md §6"
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
  - "review/round5-preregistration.md"
  - "review/round5-adjudication.md 'Pre-registration scored'"
  - "notes/phase-space-diameter-worklog.md 'Status'"
  - "review/round3/referee/audit-notes.md Step 5"
  - "review/round5/referee-A/audit-notes.md"
  - "review/round5/referee-B/audit-notes.md"
  - "notes/toy-lagrangian.md 'Success criteria', 'Predictions', 'Assessment against the predictions'"
  - "review/wiki-build-flags.md item 35"
  - "review/closed-universe/preregistration.md"
  - "review/closed-universe/README.md"
  - "notes/closed-universe.md §10"
---

*Pre-registration is the practice of writing down the verdict a blind review is expected to return and the weakest point the referee is expected to find, and fixing that forecast before the referee is dispatched: in rounds 3 and 4 by committing it to the repository, in round 5 by keeping it outside the repository and recording its hash. Because the forecast is fixed in advance it cannot be adjusted to the outcome, and scoring it afterwards measures how well the author judges the author's own work. The record so far: the verdict was forecast correctly in rounds 1 and 2, missed in round 3 and forecast correctly in rounds 4 and 5; the location of the weakest link was forecast correctly in rounds 4 and 5, while the severity of the defect there in round 4, and the number of small errors and the extent of prior art in round 5, were underestimated. Since round 3 the forecast is kept out of the commit subject, because a referee subagent sees recent commit subjects.*

**Status:** Method, in force — untagged. It is a rule of root `CLAUDE.md` ('Method') and of `HANDOFF.md` §5. The scores are recorded in `review/round3-adjudication.md`, `review/round4-adjudication.md` and `review/round5-adjudication.md`, which bring the handoff's "2-for-2" up to date.

## What pre-registration is

In empirical science, pre-registration means recording the hypotheses and the analysis plan before the data are seen, so that the analysis cannot be fitted to the result [T]. The program applies the idea to its own [blind reviews](/wiki/method/review/review-protocol). The "data" is the referee's report, and what is registered is the author's forecast of it. The round-3 pre-registration opens: "Written and committed **before** the round-3 audit was dispatched, so the prediction cannot be fitted to the outcome."

The rule, in root `CLAUDE.md`:

> Pre-register the expected verdict and weakest link before each review round. Keep the prediction out of the commit subject: subagents see recent commit subjects in their git-status context, and round 3's auditor saw it.

The handoff's earlier form: "before each review round, the expected verdict and weakest link were written down in advance (scored 2-for-2 on verdicts). Continue the practice; it calibrates trust." (`HANDOFF.md` §5).

## Why the program uses it

Paul "cannot independently verify most of the technical physics and relies on the tags, the machine checks and pre-registration to tell sound results from confabulation" (root `CLAUDE.md`; [the collaboration](/wiki/method/collaboration)). The handoff records the request behind this: he "has asked for explicit legit-vs-hallucination calibration: keep the tier tags, keep machine-verifying, keep pre-registering, keep reporting negative results prominently" (`HANDOFF.md` §7).

[Provenance tags](/wiki/method/provenance-tags) say where a claim came from, and [the gate](/wiki/method/verification/the-gate) says whether its arithmetic reproduces. Neither says whether the author's confidence in a manuscript is warranted. A scored forecast does. If the forecasts come out right, the author's self-assessment carries information. If they miss in a consistent direction, the author's confidence should be discounted in that direction. The adjudications draw exactly this kind of conclusion: "Calibration: my confidence in v3 was too high." (round 3), "Severity is still underestimated." (round 4), and "Still underestimated: the number of small errors in a long text, and the extent of prior art." (round 5).

## What a pre-registration contains

The pre-registrations in the repository, `review/round3-preregistration.md`, `review/round4-preregistration.md` and `review/round5-preregistration.md`, have the same parts:

- **The set-up:** the manuscript and the commit or hash that fixes its text, the auditor and its tools, and the protocol's stated limitation ("same model family as the author"). Round 5's adds that the program documents the manuscript cites "are unavailable to the referees, so the premises taken from them can be checked for consistent use only."
- **The verdict**, with a confidence, and the reasons it is neither the grade above nor the grade below. Round 4: "It is not C: every number was computed by gated code with independent anchors, and the claims are narrowly scoped, with limitations stated." and "It is not A: the significance is thin, and at least one argument is explicitly incomplete."
- **The single weakest link**, argued in a few lines, and the runners-up in order.
- **Arithmetic:** how many numerical indictments are expected to survive arbitration, and where one would most likely land.
- **Citations:** whether all references will resolve, and which one is likeliest to be cited for more than it says.
- **Novelty**, a part first forecast in round 5: whether the referees will find prior art beyond what the manuscript cites.

The toy-model work used the same discipline for a calculation rather than a review. Its worklog fixed the success criteria "before any construction", wrote predictions before construction, and assessed them afterwards ([success criteria S0–S5 and the pre-registered predictions](/wiki/symmetry-breaking/toy-models/success-criteria)).

## The record, round by round

### Rounds 1 and 2

Both rounds of the [skeptic review console](/wiki/method/review/skeptic-console) on [#14](/wiki/dark-matter/candidates/soliton-candidate/obituary) were pre-registered. The round-3 pre-registration: "Rounds 1 and 2 were pre-registered the same way and scored 2 for 2 on verdicts (HANDOFF §6)." (On that pointer, see flag 35 in `review/wiki-build-flags.md`.) The referees returned "B / medium" and "B near B/C / medium" (`HANDOFF.md` §6). The forecasts themselves are not in the repository, and no document records how their weakest-link forecasts scored ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

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

In the arithmetic row, every number in v3 had passed a script, and three still fell, together with the coefficient in the estimate of the [kinetic-mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) parameter ε, because the scripts encoded wrong inputs or model choices: [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) p, [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) and the bound on the [temperature ratio](/wiki/cosmology/early-universe/hidden-sector-temperature#the-bound-on-ξ) ξ ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history); [round-3 rulings](/wiki/method/review/round-3/rulings)). The adjudication's conclusion: "Calibration: my confidence in v3 was too high. The failure mode has moved." ([the measured failure mode](/wiki/method/review/referee-failure-mode)). The adjudication does not score the list of runners-up.

### Round 4

The forecast for the [toy-model note](/wiki/symmetry-breaking/toy-models) ([review round 4](/wiki/method/review/round-4)): verdict B with medium confidence. The weakest link: "in 1+1, the 'spontaneous' breaking of ρ rests on an explicit, rigid background", the fixed pair of axes K_ref that the [ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) needs. Runners-up, in order: model II's [quantum-restoration argument](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration), the [real-versus-complex distinction](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields), and the weak form of [matter locality](/wiki/symmetry-breaking/matter-coupling). On arithmetic, "at most one surviving numerical indictment", most likely "a normalization or convention: the spin-wave exponent, the 8π(m+n+1) coefficient, or the Δ sign convention". On citations, "all 12 resolve", with [12] (José et al.) the likeliest over-cited.

The adjudication scored it (`review/round4-adjudication.md`, 'Pre-registration scored'):

| Prediction | Outcome | Score |
|---|---|---|
| Verdict B | B | **Hit** |
| Weakest link: §4's breaking rests on a rigid background (K_ref) | Same place, worse defect: the potential is unbounded below with H dynamical | **Partial**: right location, missed severity |
| Runner-ups: model II restoration argument; real-vs-complex; weak S5 by construction | Restoration conclusion confirmed but must be restated (F6, Langmann–Szabo–Zarembo); real-vs-complex confirmed and extended (F4); I_K needs H (F5) | Partial on all three |
| At most one surviving numerical indictment, likeliest a normalization or sign | One: the MC control values, a statistical problem. Every normalization and sign I listed was confirmed | **Hit on count, miss on location** |
| All 12 citations resolve; likeliest over-cited is [12] | All resolve; [12]'s specific claim is unverifiable; also [8] (d = 1 only) and [11] (author's initial) | **Hit** |

The table is quoted with one abbreviation spelled out (the Langmann–Szabo–Zarembo exact solution). In it, MC is Monte Carlo, and S5 is the toy work's success criterion on matter locality. The forecast found the right place and missed what was there: the potential at K_ref was not merely put in by hand, it was unbounded below once the field H could vary ([obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). The one surviving numerical indictment was statistical, Monte Carlo values quoted from fixed seeds without error bars ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)), and none of the normalizations or signs the author had worried about.

### Round 5

The forecast for the note on [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), the first round with two referees ([Round 5](/wiki/method/review/round-5)): verdict B from both, confidence medium. The weakest link: "the bound on X in §8.2. It inherits the program's own, unreviewed premise that X couples to ordinary matter at gravitational strength (equal Planck masses, α = 4/3), which the referee cannot check." The runners-up, in order: the obituary of §6, "square exactly at the bounce" ([Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)); "'The program fixes no λ' (§5) rests on documents the referee cannot see"; and that §8.4 and §8.5 "are conditional to the point of carrying no content". On arithmetic, "zero surviving numerical indictments", and if one survived, "a convention". On citations, "all literature citations resolve", with five named candidates for being cited for more than they say. A part new to the forecasts covered novelty: "no prior art for the self-dual length beyond what §4 and §7 already cite".

The adjudication scored it (`review/round5-adjudication.md`, 'Pre-registration scored'):

| Prediction | Outcome | Score |
|---|---|---|
| Verdict B from both | B and B, confidence 0.75 each | **Hit** |
| Weakest link: the bound in §8.2 inherits the unreviewed coupling premise (equal Planck masses, α = 4/3) | Both referees: §8.2's α = 4/3 omits the background ratio c | **Hit** on location and premise; the mechanism, a dropped parameter of the cited formula, was not foreseen |
| Runner-up 1: the obituary — a surviving reading, or the \|Z\| = 1 origin paragraph read as speculation | B: the survey of readings is incomplete and the apex is convention-dependent; none changes the withdrawal | **Partial** |
| Runner-up 2: "the program fixes no λ" rests on unavailable documents | Not raised | Miss |
| Runner-up 3: §8.4 and §8.5 conditional to the point of carrying no content | A: §8.4 in tension with §8.2 (through the value of c, not upheld); B: §8.4's step sits at the §6 epoch; §8.5 not attacked | **Partial** |
| Arithmetic: zero surviving numerical indictments; if one, a convention (κ, CKN factor, ±α₉₅ column, g_* at T_P, ħ against h cells) | Five minor ones survive (R3, R6, R7, R9, R12), four of them in conventions listed | **Miss on count; hit on kind** |
| Citations: all resolve; likeliest over-cited Ohsawa or de Gosson, Slepian, Egan–Lineweaver, the Mignemi sentence, the Lee interpolation | All resolve. Over-cited: Egan–Lineweaver (table), Mignemi, the Lee interpolation column; also Bhattacharyya et al. and Gabor, not foreseen | **Hit** on resolution; three of five predicted, two not |
| Novelty: no prior art for the self-dual length beyond what the note cites | Bambi–Urban and Bolen–Cavaglià (explicit), Sundrum and Kapner et al. (the test at the dark-energy length), Albrecht et al. (the e-fold clock), string cosmology (self-dual bounces) | **Miss** |

The table is quoted as written. In it, c is the ratio of the backgrounds of the two metrics of bimetric gravity, which version 1.1 of the note writes u; CKN is the Cohen–Kaplan–Nelson bound; `g_*` at T_P is the effective number of relativistic degrees of freedom at the Planck temperature; and A and B are the two referees. The forecast found the right place and the right premise, and missed what was wrong there: the cited coupling formula carries the background ratio, which the note had dropped ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)). It expected no surviving numerical indictment, and five minor ones survived, four of them in the conventions it had listed. Its novelty forecast missed: the referees found prior art for the self-dual length, for the test at the dark-energy length, for the reading of squeezing as an e-fold clock and for self-dual bounces.

### The closed-universe investigation (not a review round)

The same practice was applied on 2026-10-27 to an investigation rather than a review. Before any agent was dispatched to work on Paul's question about a closed universe, the expected answers were written down as eleven predictions with confidences, P1–P11, and the file was "Kept out of every agent folder; never named in a prompt" (`review/closed-universe/preregistration.md`); its hash, SHA-256 `5b1fb2334c316d2780fd47f8aca49a26663b9214f5d2ac86b31ecb9a0fd3f564`, is recorded in `review/closed-universe/README.md`. The note scores it (`notes/closed-universe.md` §10; [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#record-of-the-investigation)):

- confirmed: P1 (a turnaround if and only if k = +1), P3 (size and timing, 8 of 8 matching histories), P9 (the radius–mass pairing), P10 (no over-constraint without Ω_k) and P11 (the Z₂ textures);
- confirmed and strengthened: P7 (reciprocity breaks globally) and P8 (nothing observable from the finite volume);
- P2, the data: the numbers confirmed, without the forecast anticipating that w₀wₐ+Ω_K is the wrong proxy; P4: mostly confirmed, having described the conjugate picture only as a lattice;
- partly wrong: P5, the pre-registered weakest link, since the normalization is a gauge choice and row 10's knob survives as a postulate; and P6, since the Higuchi bound holds during inflation and the gradient instability is the problem;
- the expected overall answer called closure "natural for the program"; it is not, since nothing derives it.

No review round followed; the note has not been reviewed.

### The momentum-gravity investigation (not a review round)

The investigation that answered Paul's question of 2026-10-26, whether the velocity-clumping obituary is premature, sealed an expected answer before each of its runs (`review/momentum-gravity/README.md`). The two notes score them (`notes/velocity-gated-gravity.md` §11; `notes/gate-mechanism.md` §6).

- **Run 2, not blind.** Its pre-registration was written on 2026-10-26 in the session's state file, beside the agents' folders, and three agents read it: the program analyst, the clumping derivation verifier and the dark-tests analyst. "Their judgment-level text was not blind; their executed numbers were unaffected." It was moved out of reach on 2026-10-27 (`review/momentum-gravity/preregistration-run2.md`). Right: the obituary stands for the program as written; no gate between ordinary bodies, only O(v²/c²) structure; the gate is χ–χ at contact; a universal version is excluded; the long-range variant meets small-scale-structure limits, the Lyman-α forest binding at v\* = 120 km/s. Partly right: clumping needs G̃/G ≳ (σ/v\*)³, about 2 in the Milky Way and 580 in clusters, where the executed values are at least 28 and at least 693. Wrong: that Debt 3a's σ → v\* substitution is generous to the instability, since in the Milky Way it overstates the shortfall about 3× (flag 58). The weakest link: "the O(1) factors were indeed the weak point, off by more than an order of magnitude in the Milky Way", and Hubble-flow gating does not let the variant escape the cosmological bounds, since "the gate closes at a Hubble separation of exactly v\*, the forest's scale".
- **Run 3.** Written 2026-10-27 before launch and kept outside the agents' folder. Right: the run-2 force law judged neither Hamiltonian nor Lagrangian; the record and run-2 numbers reproduce; a source correction, the mapping of the Baryon Oscillation Spectroscopic Survey's limit; the ordinary-matter envelope below 10⁻⁸, with the literature-input corrections under 3×, except one coupling correction, for MICROSCOPE, which exceeded it; no clumping in the N-body, "and more strongly than predicted, none up to ε = 10". Mostly right: the theory items; the fiber-overlap gate is not confined to contact range by itself, and "what forbids a long-range version is relativistic factorization with finitely many fields of finite spin". Wrong: the Lyman-α bound (predicted 0.1–0.5, got 0.057–0.106, anchored on the run-2 critic's 0.34); the Sagittarius bound (predicted 1–3, got 0.2–2.5); the corner (predicted no robust exclusion, but ε ≈ 2 is excluded from 10 km/s up, and ε ≈ 3 at 5–30 km/s in one reading). Missed: continuous spin, the sign of the Lyman-α response in the record's reading, and the gate-mechanism flag. The weakest link named, the compressed likelihood's shape, "was a real problem, and the N-body held up. The failures were formula errors in two linear models, which were not named."
- **Run 4.** Written 2026-10-27 before the blind second derivation of the gate question and kept outside every agent folder. Right: the polynomial of degree two in s with velocity scale c; the record builds no fiber structure; #6 §4's "rational gates" are not a gate in k. Partly right: the verdict matched the hedged alternative ("unsupported" for the tag as written), not the first choice ("conditional"), which the derivation rules out; the tag matched only in its [P] branch, and not on the stated condition, since the derivation gives [P] to the gate itself, not to a fiber-resolving X. The weakest link named, the polarization, held up: it is Lorentz-invariant, and the scenario it guarded against, a ruling of [P] rather than [O], "partly happened, for a different reason". Missed: reading R1, in which the fiber overlap is an ordinary potential of range ~10 pm ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#what-flag-55-proposes)).

The SHA-256 hashes of the three files as committed are in `review/momentum-gravity/README.md`. No review round followed; neither note has been reviewed.

### Across rounds

The round-5 adjudication sums up the record:

- "Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4), hit (round 5)."
- "Weakest-link location: hit in rounds 4 and 5."
- "Still underestimated: the number of small errors in a long text, and the extent of prior art."

The round-4 adjudication's summary, a round earlier, had read "Weakest-link location has improved. Severity is still underestimated."

| Round | Manuscript | Forecast verdict | Referee's verdict | Verdict score |
|---|---|---|---|---|
| 1 | #14 v1 | not in the repository | B / medium | scored 2 for 2 with round 2 |
| 2 | #14 v2 | not in the repository | B near B/C / medium | scored 2 for 2 with round 1 |
| 3 | #14 v3 | B, medium | C, medium | Miss |
| 4 | toy-model note | B, medium | B, ~0.75 | Hit |
| 5 | phase-space-diameter note v1.0 | B from both, medium | B and B, 0.75 each | Hit |

In rounds 3 and 4 the referee found a more serious defect than the author had forecast: in round 3 in a different place, in round 4 in the forecast place. In round 5 the forecast named the place and the premise, and the defect was of a kind it had not foreseen, a parameter dropped from a cited formula. On arithmetic, rounds 3 and 4 expected no more than a slip in a normalization or an estimate, and the indictments that survived were of another kind: wrong model inputs in round 3, missing statistics in round 4. Round 5 expected none; those that survived were mostly of the kind it had listed, conventions, and more numerous than forecast.

## Keeping the forecast from the referee

Round 3's pre-registration was committed (cc05705) with a commit subject that stated the forecast. The referee subagent's environment attached a snapshot of `git status` with the latest commit subjects, though the referee read nothing in the repository itself. Its reproducibility note: "nothing under /home/paul/git was read. The harness auto-attached a git-status snapshot whose latest commit subject mentions a pre-registered expected verdict; it was not consulted for any finding." (`review/round3/referee/audit-notes.md`, Step 5).

The adjudication's first lesson weighs it: "The auditor says it did not use it, and its verdict differed from the prediction, which argues against anchoring. But the round was less blind than intended." ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions)). The commit-subject clause entered the rule in root `CLAUDE.md`. Round 4's pre-registration states that it follows it: "Per the round-3 lesson, the commit subject does not state the prediction." The adjudication confirms it was "committed before dispatch with a neutral subject", and the repository history shows that subject for d9a06ac: "Pre-register round 4; toy-model note for review".

Round 5's forecast was not committed at all. The pre-registration says it was "kept outside the repository, in the session scratchpad, until both referees had returned, so that neither could read it. It is not committed: this session has no commit authorization." Its hash and that of the manuscript copy "were written into `notes/phase-space-diameter-worklog.md` and into the session transcript before dispatch", and the adjudication records that the hash "matches the file". The hash fixes the forecast's content; the time at which it was fixed rests on the worklog's entry, "recorded before dispatch", and on the session transcript. The referees' notes state their isolation: "only manuscript.md and files created here were read" (referee A) and "I read only the manuscript copy and my own files" (referee B).

## What it does not do

- It does not make the review more independent. The referees are still "the same model family as the author" ([the review protocol](/wiki/method/review/review-protocol#limits)).
- The scoring is the author's. The labels Hit, Partial and Miss and the calibration statements are written in the adjudications, in the first person.
- The forecasts of rounds 1 and 2 cannot be re-examined, since only their score survives.

## Sources

- `CLAUDE.md` 'Method (HANDOFF §5)' — the rule, including the commit-subject clause; 'Working with Paul' — Paul's reliance on pre-registration
- `review/round3-preregistration.md`, `review/round4-preregistration.md` — the first two pre-registrations in the repository: forecasts, reasons and the neutral-subject statement
- `review/round3-adjudication.md` 'Pre-registration scored', 'Lessons (now in CLAUDE.md)' — round 3's scores, the calibration statement and the leak lesson
- `review/round4-adjudication.md` 'Pre-registration scored' — round 4's scores and its calibration across rounds
- `review/round5-preregistration.md` — round 5's forecast, its limitation, its novelty part, and its storage outside the repository
- `review/round5-adjudication.md` 'Pre-registration scored' — round 5's scores and the calibration across rounds; its header — the recorded hash "matches the file"
- `notes/phase-space-diameter-worklog.md` 'Status' — the hashes "recorded before dispatch" and the dispatch time
- `review/round5/referee-A/audit-notes.md` and `review/round5/referee-B/audit-notes.md` — the referees' statements of isolation
- `review/round3/referee/audit-notes.md` Step 5 — the referee's reproducibility note on the leak
- `HANDOFF.md` §5, §6, §7 — the rule as handed over, with the superseded "2-for-2"; the round-1 and round-2 verdicts; the request for explicit calibration
- `notes/toy-lagrangian.md` 'Success criteria (fixed 2026-10-19, before any construction)', 'Predictions (written before construction)' — the same discipline applied to the toy-model calculation
- `review/wiki-build-flags.md` item 35 — the round-3 file's pointer to `HANDOFF.md` §6 for the 2-for-2 record, awaiting a ruling
- `review/closed-universe/preregistration.md`, `review/closed-universe/README.md` and `notes/closed-universe.md` §10 — the closed-universe investigation's sealed forecast, its hash and its scoring
- `review/momentum-gravity/README.md`, `review/momentum-gravity/preregistration-run2.md`, `review/momentum-gravity/preregistration-run3.md`, `review/momentum-gravity/preregistration-run4.md`, `notes/velocity-gated-gravity.md` §11 and `notes/gate-mechanism.md` §6 — the momentum-gravity investigation's three pre-registrations, the run-2 blindness failure, and the scores
