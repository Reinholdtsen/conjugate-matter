---
title: "The blind-review protocol and verdict scale"
weight: 10
status: method
description: "Five steps (citations, every number in code, an independent re-derivation, a conceptual audit, an A/B/C verdict with four lists and the weakest link) run by a fresh subagent given only the manuscript, then an adjudication finding by finding; the scale's glosses and the protocol's limits."
sources:
  - "review/round3-preregistration.md 'Protocol (HANDOFF §6, round 3)'"
  - "review/round4-preregistration.md"
  - "review/round3/referee/audit-notes.md Step 1–Step 5"
  - "review/round4/referee/audit-notes.md Step 1–Step 4"
  - "review/round3-adjudication.md 'Rulings', 'Decisions'"
  - "review/round4-adjudication.md 'Rulings', 'Revisions for v2 of the note'"
  - "review/skeptic-review-console.html SYSTEM"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "CLAUDE.md 'Layout', 'Since the handoff (2026-10-19)', 'Working with Paul'"
  - "HANDOFF.md §1"
  - "HANDOFF.md §6"
  - "HANDOFF.md §8"
  - "notes/knot-dark-matter-standalone.md (header)"
  - "papers/reciprocity-toy-models.md (header)"
  - "review/wiki-build-flags.md items 11, 33"
---

*The blind-review protocol is the fixed procedure the program uses to test a manuscript: a fresh AI subagent receives a copy of the manuscript and the protocol and nothing else, checks every citation against its source, re-runs every number in its own code, re-derives the mathematics independently, audits the argument for consistency and omitted constraints, and returns a grade of A, B or C with the single weakest link named. The author then rules on each finding, re-running disputed numbers in separate scripts, and scores the forecast that was committed before the referee was dispatched. The grade scale comes from the referee prompt of the [skeptic review console](/wiki/method/review/skeptic-console), the tool of rounds 1 and 2; rounds 3 and 4 ran the full five-step form with a referee that could execute code. The protocol's own stated limit is that the referee is the same model family as the author.*

**Status:** Method, in force — untagged. It is written into the pre-registrations of [round 3](/wiki/method/review/round-3/preregistration) (`review/round3-preregistration.md`) and [round 4](/wiki/method/review/round-4) (`review/round4-preregistration.md`), and both rounds ran under it. Its next use would be the optional round-5 review of the toy-model note, "but only before any external use" (root `CLAUDE.md`, 'Since the handoff').

## What the protocol is for

The program is a collaboration in which Paul supplies conjecture and direction and Claude supplies derivations, counterexamples, verification and drafting ([the collaboration](/wiki/method/collaboration)). #11 §2 names the risk this creates: "AI-generated physics has a known failure mode — fluent confabulation". Paul "cannot independently verify most of the technical physics and relies on the tags, the machine checks and pre-registration to tell sound results from confabulation" (root `CLAUDE.md`).

The machine checks of [verification](/wiki/method/verification) test the author's arithmetic, with the author's inputs. Blind review adds a reader who has none of the author's context and is asked to find what is wrong. #11 §2 records a case where only that reader could help: "a verification script confirms arithmetic, not the model it encodes — the §12 failure passed a script whose physics input was wrong, and was caught only by an independent review" ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

"Blind" goes further here than in journal peer review, where a double-blind referee is only not told who wrote the paper [T]. The referee is denied the whole project. In round 3 it "gets only a copy of the manuscript and the protocol below, with no repo, worklog or handoff context"; round 4's referee likewise received "only a copy of the manuscript, no repo context".

### The manuscript

A manuscript sent to review is written to stand alone. Both reviewed manuscripts, #14 (the [soliton dark-matter proposal](/wiki/dark-matter/candidates/soliton-candidate/obituary)) and the [toy-model note](/wiki/symmetry-breaking/toy-models), open with the same line: "Anonymous working manuscript submitted for adversarial review. The manuscript may contain errors or confabulations; the reviewer is asked to find them." Root `CLAUDE.md` calls this form "Blind-review format". Each pre-registration fixes the exact text by its commit: #14 v3 "as of commit 5dbaa82" for round 3, and the toy note "as committed with this file" for round 4, which the adjudication gives as "as of commit d9a06ac".

### The referee

Round 3's referee was "a fresh subagent with shell, Python (numpy/sympy/scipy) and web search". Round 4's was "a fresh subagent with shell, Python (numpy/sympy/scipy) and web", given "the same five-step protocol as round 3: citations, numbers, an independent re-derivation, a conceptual audit, and a verdict with four lists." Each referee left its notes, scripts and printed outputs, which are kept in `review/round3/referee/` and `review/round4/referee/`.

## The five steps

The round-3 pre-registration writes the steps as follows (`review/round3-preregistration.md`, 'Protocol (HANDOFF §6, round 3)'):

1. "Verify every citation against INSPIRE, arXiv or the publisher, including that each one supports what it is cited for."
2. "Re-check every number in Secs. 2–4 in Python from independently chosen constants."
3. "Re-derive the compatibility theorem independently, symbolically (sympy) and with random numerical tests."
4. "Conceptual audit: internal consistency, omitted constraints (by literature search), and the kinetic-mixing claims."
5. "Verdict A/B/C with a confidence, four lists (verified / failed / unverifiable / omitted constraints), and the single weakest link."

Steps 2–4 name the parts of #14 v3 they apply to. Round 4 kept the five headings and applied them to the toy note's own content. Its referee's notes merge the numbers and the re-derivation into one Step 2 with four parts, (a) to (d), so the conceptual audit is its Step 3 and the verdict its Step 4.

### Step 1: citations

INSPIRE is the literature database of high-energy physics [T]. The step tests two things: that each reference exists as cited, and the stronger condition that it supports the use made of it. A real paper cited for something it does not say is a defect most readers would not catch.

Round 3's referee queried INSPIRE for each reference, read the arXiv abstracts, and searched the full texts "for the specific claim each reference is cited for" (`review/round3/referee/audit-notes.md`, Step 1). All 23 references (37 individual items) resolved "with matching authors / journal / volume / page / year / arXiv id. No fabricated or mis-numbered reference found." Round 4's referee downloaded each paper's arXiv source and searched it for the attributed statement; its table records, reference by reference, whether the paper exists as cited and whether it supports the claim.

The same step looks for prior work the manuscript should have cited. Round 4's referee found the Langmann–Szabo–Zarembo exact solution and Smolin's triality model, among others, and its full-text searches on INSPIRE found no earlier explicit model of the duality broken by vacua ([round 4](/wiki/method/review/round-4)); round 3's referee named four uncited papers on "the standard hidden 't Hooft-Polyakov-monopole scenario", which it judged #14 v3's proposal to be (Step 4(d)).

### Step 2: every number in code

"Independently chosen constants" means the referee takes its inputs from its own sources, not from the manuscript. Round 3's referee recorded its own: α⁻¹ = 137.035999; M_Pl = 1.220890e19 and the present entropy density s0 = 2891.2 per cm³, both from the Particle Data Group (PDG) 2024 review; and Ω_c h² = 0.120 from Planck 2018 (Step 2; [round-3 arbitration and the referee's constants](/wiki/method/review/round-3/arbitration)). Round 4's referee built independent anchors for the note's algebra, such as the sign of the star product's integral kernel, "fixed against the order-10 differential series", and the [Weyl symbol](/wiki/phase-space/reciprocity/wigner-function) of |m⟩⟨n| constructed from Hermite functions (Step 2(b)).

The adjudications count the result. Round 3: "Every one of its 16 numerical findings rests on executed code." Round 4: "All 9 of its numerical and algebraic indictments rest on executed code." The step exists because of [the measured failure mode](/wiki/method/review/referee-failure-mode) of rounds 1 and 2, in which referees without code made confident order-of-magnitude errors. It is the referee's form of [the iron rule](/wiki/method/verification/iron-rule).

### Step 3: an independent re-derivation

In round 3 the theorem was [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), the one theorem #14 stated. The referee checked the proof's block identities symbolically for d = 1, 2, proved the result at d = 2 with a Groebner basis when the symbolic solver returned nothing, and ran 2000 random trials per family at d = 3, 4 (Step 3). It found the theorem true and the stated proof valid, and identified it as "essentially the known Freidel-Leigh-Minic 'Born geometry' statement", uncited. The adjudication proposed that the theorem's "[D] derived here" tag "should become [T] with that citation", and #11 v2.1 made the change.

In round 4 the referee rebuilt [model I's symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) with "generic symbolic S with det S=1, generic H, dH, K, dK", confirmed model II's [matrix-base identities](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) against an independent quantum-mechanical construction, and confirmed the note's sign convention for [the polarization Δ](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua) (Step 2(a), 2(b)).

### Step 4: conceptual audit

The audit asks whether the argument holds together and what the manuscript leaves out. In round 3 it included the question "Does the phase-space framework do any work?", answered "No.", with the reason that "Even the one structural input H only sets M/v = 21-37 and alpha_m = 34; replacing e by e/3 … gives alpha_m = 308 …, and the framework gives no way to choose" (Step 4(d); [the 'framework does no work' critique](/wiki/program/framework-does-no-work)). Its list of omitted constraints was accepted as a to-do. In round 4 the audit asked "Is 'spontaneous breaking' fair for model I in 1+1?" and assessed each of the note's novelty claims.

### Step 5: the verdict

The verdict is a grade, a confidence, four lists and one weakest link. Round 3's referee returned C with medium confidence ("high confidence in each individual finding; medium on the B/C boundary") and named "the Kibble abundance / mass determination" as the weakest link, with the framework doing no work second. Round 4's returned "B (flawed but salvageable). Confidence ~0.75", with the weakest link "Sec. 4's rho-preserving potential -mu[Tr(K K_ref)]^2."

## The verdict scale

The scale is defined in the console's referee prompt (`review/skeptic-review-console.html`, the constant `SYSTEM`): "(A) coherent speculative physics that uses established results correctly, (B) flawed but containing salvageable ideas, or (C) confabulation." The prompt ends by asking for a line of the form `VERDICT: [A/B/C], CONFIDENCE: [low/medium/high]` "and one sentence on what would change your verdict."

The later records gloss the grades in their own words. B is "flawed but salvageable" in `HANDOFF.md` §1 and both pre-registrations. C is "confabulation" in the console's prompt and "fundamentally flawed" in the round-3 referee's verdict. The two glosses of C differ, and both are on record.

The records also show where the B/C line falls in practice. Each pre-registration argues its forecast from both sides. Round 4: "It is not C: every number was computed by gated code with independent anchors, and the claims are narrowly scoped, with limitations stated" and "It is not A: the significance is thin, and at least one argument is explicitly incomplete." The referees give their reasons in the same terms. Round 4's: the defects are "repairable (bounded potential plus a K-odd coupling, or an honest restriction to a frozen-H toy), so B rather than C." Round 3's: "Salvage = a different model (v <~ 1e8 GeV, or explicit dilution), which already exists in the literature." Read together (the wiki's reading), B has meant defects that can be repaired within the manuscript's own proposal, and C a proposal whose only salvage is a different model.

No round has returned A. The handoff calls the toy Lagrangian "the item both independent reviewers named as the gate to verdict A" (`HANDOFF.md` §8 item 4; [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)).

| Round | Manuscript | Referee's tools | Verdict and confidence |
| --- | --- | --- | --- |
| 1 | #14 v1 | web search, no code | "B / medium" |
| 2 | #14 v2 | web search, no code | "B near B/C / medium" |
| 3 | #14 v3 | shell, Python, web search | C, medium |
| 4 | toy-model note | shell, Python, web | B, ~0.75 |

Rounds 1 and 2 are known only from the handoff's summary ([rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

## After the referee: adjudication

The author answers the review in an adjudication (`review/round3-adjudication.md`, `review/round4-adjudication.md`): a table with one row per finding, its ruling, and the evidence for the ruling. The rulings so far use these labels:

- **Upheld**, with qualifiers when they apply: "Upheld (minor)", "Upheld in substance", "Upheld (abstract level)", "Upheld (literature)", and "Upheld, with a consequence the referee did not draw";
- **Accepted**, "Accepted, not re-checked" (the adjudicator did not reproduce the finding) and "Accepted, as citations and reframing";
- **Overturned**.

Disputed numbers are re-run in arbitration scripts of the adjudicator's own: `review/round3/adjudicator/round3_arb.py`, and in round 4 `arb.py` for F1–F5 and `ctrl.py` for the Monte Carlo control run, with their printed outputs beside them. These scripts sit in `review/`, outside the gate, although the root `CLAUDE.md` says of `verify/` that "arbitration and audit scripts go here"; no document says which governs ([conflicts between sources](/wiki/history/documents/source-conflicts#method-and-records)). Corrected numbers go into [the gate](/wiki/method/verification/the-gate): round 3's corrected inputs "now live in `verify/soliton_obituary.py`" ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)), which does not check every number the round-3 record quotes (flag 33 in `review/wiki-build-flags.md`), and round 4's findings are checked in the toy scripts ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

An adjudication does not defer to the referee. Round 3's referee claimed that a paper #14 cited, Baumgart et al., does not contain the [adjoint kinetic-mixing operator](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator). The adjudicator found the operator in a footnote, quoted it verbatim, and ruled the finding "**Overturned**": "The referee missed the footnote." (ruling 8; [round-3 rulings](/wiki/method/review/round-3/rulings)).

Each adjudication then scores the pre-registered forecast ([pre-registration](/wiki/method/review/pre-registration)), states the round's lessons, which go into `CLAUDE.md`, and records what follows. In round 3 that was four decisions: [strict sector separation](/wiki/program/postulates/p4-polarized-matter), the retirement of the soliton candidate, dropping the [√N floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor), and the toy Lagrangian as the next task ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions)). Paul had delegated them ("You make the decisions for me and give rational"): "Claude made them. Paul keeps the veto." In round 4 it was six revisions to the note, "all accepted; applied 2026-10-20 in commit 6606734".

## Limits

- **The referee is the same model family as the author.** The round-3 pre-registration states the limit "up front": "the auditor is the same model family as the author. It removes the arithmetic failure mode of rounds 1–2, which had no code execution. It does not remove correlated blind spots." Round 4's repeats "same model family as the author". #11 §2 places the final check elsewhere: "What no machine can check is whether the algebra is attached to the right physics; that verdict belongs to expert readers and, ultimately, to data."
- **Blindness depends on the referee's environment.** In round 3 the harness attached a git-status snapshot "whose latest commit subject mentions a pre-registered expected verdict". The referee reported that "it was not consulted for any finding", but "the round was less blind than intended" (round-3 lesson 1). Forecasts are now kept out of commit subjects ([pre-registration](/wiki/method/review/pre-registration#keeping-the-forecast-from-the-referee)).
- **Long audits can break off.** The first round-3 dispatch "died partway on a rate limit" (`HANDOFF.md` §6). Round 4's referee "was interrupted once by a rate limit and resumed from its own transcript."
- **Findings accepted without re-checking rest on the referee alone.** Examples are round 3's [Witten-effect charge](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#ii-the-witten-effect) (ruling 9) and round 4's mass renormalization (F6), whose coefficient the later sources state differently ([round 4](/wiki/method/review/round-4#f6-the-truncation-argument); flag 11 in `review/wiki-build-flags.md`).

## History

Rounds 1 and 2 ran through the [skeptic review console](/wiki/method/review/skeptic-console), a browser page whose referee could search the web but not execute code. Their record is the summary in `HANDOFF.md` §6.

The five-step form was planned in the claude.ai period. The handoff describes "an execution-verified blind audit agent (fresh context, shell+Python+web, 5-step protocol …)" dispatched on 2026-10-17, which "died partway on a rate limit after reporting 'most citations and core numbers checked; several omitted-constraint literature checks remaining.'" Its queue made the re-run item 2, after cutting v3 of #14 (`HANDOFF.md` §8), and suggested doing it "natively" in Claude Code. The round-3 pre-registration copies that plan under the heading "Protocol (HANDOFF §6, round 3)", and the round ran to completion on 2026-10-19 ([review round 3](/wiki/method/review/round-3)). Round 4 reused the protocol on the toy-model note on 2026-10-19 and 2026-10-20 ([review round 4](/wiki/method/review/round-4)).

## Sources

- `review/round3-preregistration.md` 'Protocol (HANDOFF §6, round 3)' — the five steps, the referee's set-up and the stated limitation
- `review/round4-preregistration.md` — the protocol reused for the toy-model note; the not-A and not-C arguments
- `review/round3/referee/audit-notes.md` Step 1–Step 5 — the protocol as executed: the citation method, the referee's constants, the re-derivation, "Does the phase-space framework do any work?", the verdict and the reproducibility note
- `review/round4/referee/audit-notes.md` Step 1–Step 4 — the round-4 execution, its anchors and its verdict
- `review/round3-adjudication.md` 'Rulings', 'Lessons (now in CLAUDE.md)', 'Decisions' — the ruling labels, the overturned finding, the delegated decisions
- `review/round4-adjudication.md` 'Rulings', 'Revisions for v2 of the note' — the arbitration scripts and the revisions
- `review/skeptic-review-console.html` — the A/B/C scale in the referee prompt
- `papers/broken-born-checkpoint-v2.md` §2 — fluent confabulation; a script confirms arithmetic, not the model
- `CLAUDE.md` 'Layout', 'Since the handoff (2026-10-19)', 'Working with Paul' — the blind-review format, where arbitration scripts go, round 5 optional, Paul's reliance on the checks
- `HANDOFF.md` §1, §6, §8 — the "flawed but salvageable" gloss, the first round-3 dispatch, the queue item and the gate to verdict A
- `notes/knot-dark-matter-standalone.md`, `papers/reciprocity-toy-models.md` (header lines) — the anonymous-manuscript line
- `review/wiki-build-flags.md` items 11, 33 — the tadpole coefficient in dispute; what `verify/soliton_obituary.py` checks against what it claims
