---
title: "Round-3 pre-registration"
weight: 10
status: record
description: "The forecast committed before the round-3 referee was dispatched — verdict B, weakest link 'the framework does no work', no surviving numerical indictment, all 23 citations resolving — how each part scored, and the commit subject that leaked it."
sources:
  - "review/round3-preregistration.md"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3/referee/audit-notes.md Step 5"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/v3-worklog.md 'New open items'"
  - "review/v3-worklog.md 'Next chunks'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
  - "HANDOFF.md §5"
  - "HANDOFF.md §6"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "CLAUDE.md 'Working with Paul'"
  - "review/round4-preregistration.md"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/skeptic-review-console.html SYSTEM"
---

*The round-3 pre-registration is the forecast of the third blind review of the soliton dark-matter manuscript #14, written into `review/round3-preregistration.md` and committed on 2026-10-19 before the referee was dispatched, so that the forecast could not be fitted to the outcome. It predicted that the referee would grade version 3 B ("flawed but salvageable") with medium confidence, that the weakest link it named would be "the framework does no work", that no numerical indictment would survive, and that all 23 citations would resolve. The referee graded the manuscript C. The adjudication scored the verdict a miss, the first after two hits; the weakest link a miss on the referee's first choice and a hit on its second; the arithmetic a miss; and the citations a hit. The commit that recorded the forecast also stated it in its subject line, which the referee's environment displayed, so the round was less blind than intended, and forecasts have been kept out of commit subjects since.*

**Status:** Record — untagged. The forecast is `review/round3-preregistration.md` as committed (cc05705); its scoring is the adjudication's 'Pre-registration scored', reproduced below against the referee's grade ([round-3 verdict and rulings](/wiki/method/review/round-3/rulings)). The lesson about the commit subject is part of the pre-registration rule in the root `CLAUDE.md`, 'Method' ([pre-registration and its calibration record](/wiki/method/review/pre-registration)).

## What was pre-registered, and why

A pre-registration, in this program, is a forecast of a review's outcome, written down and committed before the referee starts, and scored against the outcome afterwards ([pre-registration](/wiki/method/review/pre-registration)). The root `CLAUDE.md` makes it a rule: "Pre-register the expected verdict and weakest link before each review round." The round-3 file states its purpose in its first sentence: "Written and committed **before** the round-3 audit was dispatched, so the prediction cannot be fitted to the outcome."

The purpose is calibration. Paul "cannot independently verify most of the technical physics and relies on the tags, the machine checks and pre-registration to tell sound results from confabulation" (root `CLAUDE.md`, 'Working with Paul'). A forecast scored afterwards measures how well the author judges its own work before an outside reader has seen it ([the calibration](/wiki/method/collaboration#the-calibration)). The handoff's record for the earlier rounds: "before each review round, the expected verdict and weakest link were written down in advance (scored 2-for-2 on verdicts)" (`HANDOFF.md` §5); the round-3 file repeats it, "Rounds 1 and 2 were pre-registered the same way and scored 2 for 2 on verdicts" ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

The forecast was the step the v3 worklog had planned after cutting the new version: "Pre-register the expected verdict and weakest link, then run the round-3 audit on v3 (HANDOFF §8 item 2)" ('Next chunks'). The adjudication records it as "commit cc05705, made before dispatch".

## The set-up

The file fixes three things before the forecast itself.

- **The manuscript.** #14 v3, "as of commit 5dbaa82", then in `papers/` and now `notes/knot-dark-matter-standalone.md`, withdrawn. It proposed that dark matter consists of "superheavy 't Hooft-Polyakov monopoles of a hidden SU(2) gauge sector broken to U(1)", with a benchmark mass of 3×10¹³ GeV ([the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate)).
- **The auditor.** "A fresh subagent with shell, Python (numpy/sympy/scipy) and web search. It gets only a copy of the manuscript and the protocol below, with no repo, worklog or handoff context."
- **The limitation**, "stated up front": "the auditor is the same model family as the author. It removes the arithmetic failure mode of rounds 1–2, which had no code execution. It does not remove correlated blind spots." The failure mode is the one the handoff had measured: referees without code made confident order-of-magnitude errors in their own arithmetic ([the measured referee failure mode](/wiki/method/review/referee-failure-mode)).

The protocol is the five steps planned in the claude.ai period, under the heading "Protocol (HANDOFF §6, round 3)": verify every citation, "including that each one supports what it is cited for"; "Re-check every number in Secs. 2–4 in Python from independently chosen constants"; re-derive the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) "symbolically (sympy) and with random numerical tests"; audit "internal consistency, omitted constraints (by literature search), and the kinetic-mixing claims"; and return a "Verdict A/B/C with a confidence, four lists (verified / failed / unverifiable / omitted constraints), and the single weakest link" ([the five steps](/wiki/method/review/review-protocol#the-five-steps)). A first dispatch of the same protocol, from claude.ai on 2026-10-17, had "died partway on a rate limit" (`HANDOFF.md` §6; [review round 3](/wiki/method/review/round-3)).

## The forecast

### Verdict: B, with medium confidence

The file argues the grade from both sides.

- "It is not A: the toy action (acceptance criterion 1) does not exist, and two of v3's own exclusion tests (the millicharged ψ window and the strong-coupling relic) are stated but not evaluated." The toy action is an explicit action in which reciprocity is a genuine symmetry, spontaneously broken, which #14 itself set as its first acceptance criterion ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)). The two tests are #14's exclusion conditions 3 and 4: "Exclusion of the millicharged psi window" and "A strong-coupling relic calculation showing that monopole annihilation in the hidden plasma at alpha_m ~ 34 cannot leave the observed abundance" (§5).
- "It is not C: v3 removes v2's known internal contradictions (§2 vs §3 coupling; the ε·g premise; the "Kibble-only" window)." Each was a finding of the v3 worklog. The worklog's F2 found that "v2 uses the weak value in §3 and the strong value in §2 and §4" for the hidden coupling ([F2](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#superseded-f2-which-coupling-sets-the-soliton-mass)); its L1 found v2's premise, "mixing ε gives the solitons magnetic charge εg under our photon", "wrong for its own setup" ([no visible magnetic flux](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#c-no-visible-magnetic-flux-while-u1d-is-unbroken)); and its F1 found that "the mass window is not "Kibble-only"" ([the point, not a window](/wiki/dark-matter/candidates/soliton-candidate/overproduction#superseded-the-point-not-a-window-of-the-v3-worklog)).

On the program's scale, from the console's referee prompt, B is "flawed but containing salvageable ideas" and C "confabulation" ([the verdict scale](/wiki/method/review/review-protocol#the-verdict-scale)).

### Weakest link: "the framework does no work"

> - The candidate in §2–§4 is a standard hidden-sector monopole model.
> - Nothing numerical depends on Born reciprocity, the compatibility theorem or the polarization identification. Hypothesis H's motivation ("the minimal action is to equate the elementary charges") is one sentence.
> - Expect the auditor to say the dark-matter proposal stands or falls independently of the phase-space framework.

The objection is that a proposal made under the program's name owes nothing to the program's [hard core](/wiki/program/hard-core), spontaneously broken [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ([the 'framework does no work' critique](/wiki/program/framework-does-no-work)). #14 v3 conceded part of it in its own text: the charge-lattice motivation is used "only as motivation ... No numerical result below depends on it" (§2). Hypothesis H was its single coupling assumption, that the smallest hidden charge equals the electron's ([hypothesis H](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#attempt-3-hypothesis-h)).

### Runner-up weakest links

In order:

1. "The unevaluated millicharge bounds on ψ at ε ~ 10⁻⁷–10⁻⁶, MeV–0.1 TeV. They might already exclude part of the window." ψ is the light hidden fermion v3 added so that the hidden W′± bosons could decay; with [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) of strength ε it carries a small visible charge.
2. "Thermal-history consistency. The W′ and ψ freeze-out are computed at ξ = 1, but dark radiation requires ξ < 0.77, and Kibble production with a colder hidden sector is treated only by the ξ^(3/4) scaling." ξ is the ratio of the hidden sector's temperature to ours ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)).
3. "The strong-coupling annihilation at α_m ≈ 34 (criterion 3)." α_m is the monopoles' mutual magnetic coupling, and criterion 3 is #14's request for "the strong-coupling relic freeze-out calculation of Sec. 3, in the hidden plasma" (§6).

### Arithmetic: "zero surviving numerical indictments"

An indictment, here, is a referee's finding that a stated number is wrong. The file expected none to survive: "Every number was computed by" the script then in the gate for v3, `knot_numbers.py`, since replaced. "If one does land, the most likely place is the order-of-magnitude freeze-out or ΔN_eff estimates, where the inputs (κ, g\*, f) are bracketed rather than derived." κ is the coefficient of the W′ annihilation cross-section, bracketed over 1–10; g\* the number of relativistic degrees of freedom; and f the factor in the monopole mass, between 1 and 1.787 (`review/v3-worklog.md`, 'New open items', O1).

### Citations: "all 23 resolve"

> Citations: all 23 resolve. The likeliest problems are the two not live-checked (Kolb & Turner; Hiramatsu et al.'s journal reference), or a reference cited for slightly more than it says, such as [5] on heavy-spin-2 stability or [11] on global symmetries.

The two had been left unchecked in the worklog: "Kolb & Turner, *The Early Universe* (a textbook, cited for the freeze-out formula); the JHEP reference for Hiramatsu et al., which was taken from its DOI. Round 3 should confirm both" ('v3 as drafted (2026-10-19)').

## How it scored

The adjudication's table, in full:

| Prediction | Outcome | Score |
| --- | --- | --- |
| Verdict B | C | **Miss**: the first after 2 for 2 |
| Weakest link: "the framework does no work" | The referee's #2; its #1 was the abundance normalization | **Miss on #1** (hit on #2) |
| Zero surviving numerical indictments | Three survive (p; the ψ window; ξ), plus the ε coefficient | **Miss**. All are wrong inputs or model choices in my scripts, not arithmetic slips |
| All 23 citations resolve | All exist | **Hit** |
| A misattribution most likely in [5] or [11] | The referee's one misattribution claim (Baumgart) was itself wrong; [4] was flagged as over-generalized | Miss |

### The verdict

The referee's grade line reads `GRADE: C (fundamentally flawed), confidence MEDIUM (high confidence in each individual finding; medium on the B/C boundary)`. The forecast had argued against C from the contradictions v3 removed. The referee's C rested on something the forecast had not listed among its risks: the abundance normalization, the count of monopoles formed in the early universe, which was too low by a factor of about 4.6×10³ and on which the predicted mass depended ([the verdict](/wiki/method/review/round-3/rulings#the-verdict); [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)). The thermal-history runner-up touched Kibble production only through the ξ^(3/4) scaling. The referee's salvage was "a different model (v <~ 1e8 GeV, or explicit dilution), which already exists in the literature": in the wiki's reading of the scale, a proposal whose only repair is a different model is what has separated C from B ([the verdict scale](/wiki/method/review/review-protocol#the-verdict-scale)).

### The weakest link

The referee named "the Kibble abundance / mass determination (p=0.023 instead of >= 25-104; Kibble treated as an upper end when it is the causal minimum; KZ production and alpha_m=34 Preskill-type annihilation not computed although the literature already has it)" first, where KZ is Kibble–Zurek, and "the framework does no work" second (Step 5). Its conceptual audit answered the forecast's third bullet in nearly the forecast's words: the proposal "stands or falls on that literature, independently of Born reciprocity" (Step 4(d)).

### The arithmetic

Three numbers survived as indictments, plus the coefficient of ε: the Kibble normalization p (ruling 1), [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) (ruling 4), the bound on ξ (ruling 5) and [the Planck-scale coefficient of the mixing operator](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) (ruling 7) ([the rulings](/wiki/method/review/round-3/rulings#the-rulings)). The adjudication's comment: "All are wrong inputs or model choices in my scripts, not arithmetic slips". In the wiki's reading, two of the three fell where the forecast had said one most likely would, in a freeze-out estimate (the ψ window) and a ΔN_eff estimate (ξ); the one that decided the verdict, p, did not. The adjudication scored the row as a whole, a miss.

### The citations

The referee's result, with its capitals lowered: "all 23 references (37 individual items) resolve on INSPIRE with matching authors / journal / volume / page / year / arXiv id. No fabricated or mis-numbered reference found." Both references not checked live resolved; Kolb and Turner, a textbook, was "not checked page-level". The two references the forecast named as most likely to be over-cited were not: the referee marked [5] and [11] as supporting their claims. Its misattribution claim fell on [10], on Baumgart et al., and the adjudicator overturned it (ruling 8); [4] was the reference "flagged as over-generalized" ([the citation audit](/wiki/method/review/round-3/rulings#the-citation-audit)).

### The runner-ups

The adjudication scores no runner-up. The record shows where each went.

- **The millicharge bounds.** The referee's literature check found that supernova SN1987A limits exclude millicharges "between 1e-9 - few x 1e-6 ... for masses <~ 200 MeV", a band that "covers the whole stated charge range for m_psi = 1-200 MeV" (Step 4(c) item 3). The adjudication accepted the bounds "as a to-do; not individually re-checked", and Decision 1, strict sector separation, closed the channel ([omitted constraints](/wiki/method/review/round-3/rulings#supernova-sn1987a-and-nucleosynthesis-limits)).
- **Thermal-history consistency.** The referee found the inconsistency the forecast described: "the M\* band is quoted at xi=1 while xi<0.76 is required (the xi^(3/4) shift is stated, the band is not updated)" (Step 4(a) item 4). Ruling 5 corrected the bound itself to ξ < 0.760.
- **Strong-coupling annihilation.** Ruling 10, upheld at the level of the abstracts: "Annihilation at α_m ≈ 34 is Preskill's Dirac case, already done for hidden sectors". The referee: "Acceptance criterion 3 is not open" (Step 4(a) item 3).

### Calibration

The adjudication's conclusion:

> Calibration: my confidence in v3 was too high. The failure mode has moved. In rounds 1–2 it was the referee's unaided arithmetic. In round 3 it is that **the author's verification checks the author's model**: a wrong physics input passes a gate that tests only arithmetic.

That conclusion became the rule that a verification check confirms arithmetic, not the model ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)). The next round's adjudication carried the record forward: "Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4)" (`review/round4-adjudication.md`; [review round 4](/wiki/method/review/round-4)).

## The leak

The forecast was committed before dispatch, as the rule required. The commit's subject line stated it as well; the repository's history keeps the subject under cc05705, and it names the expected verdict and the weakest link. The harness that launched the referee attached a snapshot of the repository's git status, recent commit subjects included, to the referee's context. The referee's reproducibility note (Step 5):

> Reproducibility note (blindness): nothing under /home/paul/git was read. The harness auto-attached a git-status snapshot whose latest commit subject mentions a pre-registered expected verdict; it was not consulted for any finding.

The risk is anchoring: a referee who knows the grade the author expects may be drawn toward it [T]. The adjudication weighed it in lesson 1:

> Keep the prediction out of the pre-registration commit subject. The auditor's auto-attached git status showed it. The auditor says it did not use it, and its verdict differed from the prediction, which argues against anchoring. But the round was less blind than intended.

The rule in the root `CLAUDE.md` now carries the lesson: "Keep the prediction out of the commit subject: subagents see recent commit subjects in their git-status context, and round 3's auditor saw it." Round 4 applied it. Its pre-registration says "Per the round-3 lesson, the commit subject does not state the prediction", and its adjudication records the file as "committed before dispatch with a neutral subject" ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions#lesson-1-keep-the-forecast-out-of-the-commit-subject)).

## Sources

- `review/round3-preregistration.md` — the set-up, the protocol, the forecast and the stated limitation
- `review/round3-adjudication.md` 'Pre-registration scored' — the table and the calibration paragraph; 'Lessons (now in CLAUDE.md)' — lesson 1; 'Rulings' — rulings 1, 4, 5, 7, 8 and 10 as the score cites them
- `review/round3/referee/audit-notes.md` Step 1 — the citation result; Step 4(a) items 3–4 and Step 4(c) item 3 — what became of the runner-ups; Step 4(d) — the framework does no work; Step 5 — the grade, the weakest links and the reproducibility note
- `review/v3-worklog.md` 'Findings neither referee raised' (F1, F2, L1) — the contradictions v3 removed; 'New open items' (O1) — the bracketed inputs; 'Next chunks' — the plan; 'v3 as drafted (2026-10-19)' — the two references not checked live
- `notes/knot-dark-matter-standalone.md` §2 — "only as motivation"; §5 — exclusion conditions 3 and 4; §6 — acceptance criterion 3
- `HANDOFF.md` §5 — pre-registration and the 2-for-2 record; §6 — the first round-3 dispatch
- `CLAUDE.md` 'Method (HANDOFF §5)' — the rule as it now stands; 'Working with Paul' — what pre-registration is for
- `review/round4-preregistration.md`, `review/round4-adjudication.md` 'Pre-registration scored' — the lesson applied, and the record across rounds
- `review/skeptic-review-console.html` — the A/B/C scale in the referee prompt
