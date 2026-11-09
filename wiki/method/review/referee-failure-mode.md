---
title: "The measured referee failure mode"
weight: 40
status: record
description: "Rounds 1–2: referees strong on structure and literature and unreliable on unaided arithmetic (three confident order-of-magnitude indictments, none surviving); rounds 3–5: with code-executing referees, the failures were the author's: model inputs, reduced checks and a parameter dropped from a cited formula."
sources:
  - "HANDOFF.md §6"
  - "HANDOFF.md §5"
  - "HANDOFF.md §4"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/round3-preregistration.md"
  - "review/round3-adjudication.md 'Rulings', 'Pre-registration scored', 'Lessons (now in CLAUDE.md)'"
  - "review/round4-preregistration.md"
  - "review/round4-adjudication.md 'Rulings', 'Lessons (into CLAUDE.md)'"
  - "review/round4/referee/audit-notes.md Step 2(d)"
  - "review/round5-preregistration.md"
  - "review/round5-adjudication.md header, 'Rulings', 'Pre-registration scored', 'Lessons (into CLAUDE.md)'"
  - "wiki/papers/broken-born-checkpoint-v2.md §2"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "review/skeptic-review-console.html"
---

*The measured referee failure mode is the program's record of where its blind reviews have gone wrong, and on which side. In rounds 1 and 2 the referees, which could search the web but not run code, were reliable on structure, literature and logic and unreliable on arithmetic: their three confident order-of-magnitude indictments were all their own unit errors, and none survived. That finding made the iron rule load-bearing and was the main reason the project moved to Claude Code, where a referee can execute code. In round 3 the failure moved to the author's side: the author's scripts had checked the arithmetic of a model with a wrong physics input, so a check that tests only arithmetic passed it. Round 4's decisive defect was again on the author's side, in a check run on a reduced model, and so was round 5's major finding, a parameter dropped from a cited formula.*

**Status:** Record — untagged. The round-1–2 form is [`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode). The round-3 form, from [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Pre-registration scored', is the current lesson: "The failure mode has moved." The [iron rule](../verification/iron-rule.md) that the first produced stays in force (root [`CLAUDE.md`](../../../CLAUDE.md), 'Method'). The two lessons of round 4 ([`review/round4-adjudication.md`](../../../review/round4-adjudication.md)) and the two of round 5 ([`review/round5-adjudication.md`](../../../review/round5-adjudication.md)) are further instances on the author's side.

## What was measured

Rounds 1 and 2 used the [skeptic review console](skeptic-console.md): a fresh Claude model with web search and an adversarial prompt, but no code execution, so any arithmetic in its review was done unaided. Both rounds reviewed [#14](../../../notes/knot-dark-matter-standalone.md), the [soliton dark-matter manuscript](../../dark-matter/candidates/soliton-candidate/obituary.md) ([review rounds 1 and 2](rounds-one-and-two.md)). The handoff summarizes the result under the heading "Measured failure mode (both rounds + consistent)":

> fresh LLM referees are strong on structure, literature and logic; **unreliable on unaided arithmetic** (3 confident order-of-magnitude indictments, all reviewer unit errors, 0 surviving). Hence the iron rule. Claude Code's native execution removes this failure mode — that's the main reason the project is moving to you.

([`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); LLM is large language model.) The finding has two halves, and both are in the record.

**Strong on structure, literature and logic.** Round 1's valid findings were all incorporated into #14 v2. The first was a logical contradiction: the manuscript fixed the hidden coupling α_d ≈ 34 by [Dirac quantization](../../electric-magnetic-duality/monopoles/dirac-quantization.md) against our own [charge lattice](../../electric-magnetic-duality/symplectic-charge-lattice.md), then denied that the solitons couple to our photon. The handoff records it as "round-1 reviewer's valid kill" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen); [Under review: the coupling α_d ≈ 34](../../dark-matter/candidates/soliton-candidate/alpha-d-coupling.md)). Round 1 also found an inverted citation of Preskill and the missing treatment of [kinetic mixing](../../dark-matter/candidates/soliton-candidate/kinetic-mixing.md), and demanded the toy Lagrangian that became [acceptance criterion 1](../../symmetry-breaking/toy-models/acceptance-criterion.md). Round 2's valid findings included literature and consistency points: the supersymmetry burden of [Montonen–Olive duality](../../electric-magnetic-duality/s-duality.md), the extended [Parker bound](../../electric-magnetic-duality/monopoles/monopole-searches.md), a gravity-induced mixing channel, and the instability of the [bimetric cosmological branch](../../gravity/spin-2-fields/bimetric-cosmology.md).

**Unreliable on unaided arithmetic.** The handoff lists the referees' own errors, all "machine-arbitrated" by the author:

- round 1: "GeV→gram conversion off 10³; σ_T/M misread as σ_T (off ~10⁴³)". The second error read a [cross-section per unit mass](../../dark-matter/halo-astrophysics/transfer-cross-section.md#per-unit-mass-t) as a bare cross-section. Round 1 also "insinuated the compatibility theorem might be false (it is machine-verified)", a claim answered by [battery test T1](../verification/battery.md) ([the compatibility theorem](../../phase-space/born-geometry/compatibility-theorem.md)).
- round 2: it "fed ρ_DM = 1.26×10⁻³ GeV/cm³ instead of 1.26×10⁻⁶ (the manuscript's own number) — with the right input the closure lands within 3%", and it "conflated mean vs local density labels (manuscript's 1.3×10⁻²² mean and one-per-25-km³ local are both exactly right)". In v2's own text the inputs read "mean rho_DM = 1.26 keV/cm^3" and, at the benchmark, "mean number density n ~ 1.3e-22 /cm^3" and "one soliton per ~25 km^3" for the local halo.

The handoff counts three confident order-of-magnitude indictments among these and none surviving; it does not say which listed errors are the three. The executed arbitration code that settled them exists only in the old chat ([`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact)).

Round 2's quantitative claims held up only in part when the worklog for v3 checked them in code and in the literature. The referee had said that running the coupling to the transition scale "drags 34 toward ~6–8". The worklog's check: "The referee's 'toward ~6–8' is **not reproduced** for the electromagnetic coupling; 6–8 appears only for 1/(4α₃)", although "The valid core stands: the number is convention-dependent by a factor of 4." The referee's gravity-induced mixing channel came with a formula that was "uncited and unverified" ([`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode)); the literature check found that the channel "exists, and it is negligible" ([`review/v3-worklog.md`](../../../review/v3-worklog.md), R2 and R4).

## What the program did about it

**The iron rule.** "No arithmetic by eyeball. Any disputed or asserted number gets executed code with printed output. This is load-bearing — see §6." ([`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it); [the iron rule](../verification/iron-rule.md)). The rule applies to the author as well as to the referee.

**Referees that execute code.** The move to Claude Code made it possible to give the referee a shell and Python. Step 2 of the [blind-review protocol](review-protocol.md) re-checks every number "in Python from independently chosen constants". The round-3 pre-registration states what this does and does not change: "It removes the arithmetic failure mode of rounds 1–2, which had no code execution. It does not remove correlated blind spots."

**The effect.** In round 3, "Every one of its 16 numerical findings rests on executed code"; in round 4, "All 9 of its numerical and algebraic indictments rest on executed code"; in round 5, "Every numerical indictment rests on executed code." Where round 3's referee and adjudicator computed the same quantity separately, they agreed closely: on [the ψ relic window](../../dark-matter/candidates/soliton-candidate/psi-relic-window.md), "We agree to within ×1.6, and v3's 0.1–0.3 TeV was wrong" (ruling 4). The one round-3 finding that was overturned was a reading error, not an arithmetic one: the referee had missed a footnote in a cited paper (ruling 8). In round 4 the referee caught one arithmetic error of its own by running code: a first attempt at the matter-coupling integral gave 23.27, which it traced to its own normalization and recorded as "not a manuscript error" ([`review/round4/referee/audit-notes.md`](../../../review/round4/referee/audit-notes.md), Step 2(d)). No round-4 finding was overturned. In round 5 the one part not upheld was referee A's value of the background ratio, set from a·ã = 1: "The record's second frame is the polarization frame, not the slaved momentum block g̃ = g⁻¹ that carries ã, so that value does not follow." (ruling R1).

## Round 3: the failure moves to the author's side

The round-3 adjudication:

> Calibration: my confidence in v3 was too high. The failure mode has moved. In rounds 1–2 it was the referee's unaided arithmetic. In round 3 it is that **the author's verification checks the author's model**: a wrong physics input passes a gate that tests only arithmetic.

**The evidence.** The pre-registration had forecast "zero surviving numerical indictments", since "Every number was computed by" a gated script ([pre-registration](pre-registration.md)). The outcome: "Three survive (p; the ψ window; ξ), plus the ε coefficient", and "All are wrong inputs or model choices in my scripts, not arithmetic slips". The central one was the Kibble normalization p, the coefficient in the [Kibble estimate](../../electric-magnetic-duality/monopoles/kibble-mechanism.md) of the monopole abundance: one [defect](../../symmetry-breaking/topological-defects.md) per Hubble volume "is p ≈ 104, not 0.023". Ruling 1: "v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³. My error came from misremembering the formula." The gated check did not catch it, because its anchor was not independent of the manuscript: "v3's Kibble anchor reproduced v2's own number and so tested nothing" (lesson 2). Ruling 13 upheld, in substance, the referee's objection to v3's claim that all its numbers were computed by executed code: "The code checked the arithmetic of a wrong model." ([round-3 rulings](round-3/rulings.md); [Under review: the Kibble normalization](../../dark-matter/candidates/soliton-candidate/kibble-normalization.md)).

**The rules it produced.**

- [#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification), added in v2.1: "a verification script confirms arithmetic, not the model it encodes — the §12 failure passed a script whose physics input was wrong, and was caught only by an independent review" ([verification checks arithmetic, not the model](../verification/arithmetic-not-model.md)).
- Round 3's second lesson: "An anchor must be independent of the paper." The replacement anchors for the Kibble estimate are "the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume" ([independent anchors](../verification/independent-anchors.md)).

Both are in root [`CLAUDE.md`](../../../CLAUDE.md) ('Method'): "A verification check confirms arithmetic, not the model. An anchor must be independent of the paper (a textbook identity, a published value). A check that reproduces the paper's own number is circular. Round 3 caught a wrong Kibble normalization that a circular anchor had passed."

## Round 4: the same side again

The round-4 pre-registration argued against a C partly because "every number was computed by gated code with independent anchors". The decisive finding was nonetheless a defect the author's checks had missed. The note's ρ-preserving potential had been checked with the field H held fixed, and it is unbounded below once H varies: "I should have caught F1 myself: I checked the potential only at frozen H." ([review round 4](round-4.md); [Under review: the naive ρ-preserving potential](../../symmetry-breaking/toy-models/coset-model/naive-potential.md)). The one surviving numerical indictment was statistical. The Monte Carlo control values were reproducible because the seeds were fixed, and one of them was "a short-run fluctuation": "**Fixed seeds gave reproducibility, not accuracy; the numbers lacked error bars.**"

Each became a rule in root [`CLAUDE.md`](../../../CLAUDE.md): [the reduced-model stability rule](../verification/reduced-model-stability.md) and [the Monte Carlo error-bar rule](../verification/monte-carlo-error-bars.md). In the wiki's reading, like round 3's, both concern what a passing check does not establish: a reduced model's stability does not establish the full model's, and a reproducible number need not be accurate.

## The pattern across four rounds

| Round | Referee's tools | Where the surviving errors were | What caught them | Rules that followed |
| --- | --- | --- | --- | --- |
| 1–2 | web search, no code | the referees' own arithmetic: 3 indictments, 0 surviving | the author's machine arbitration | the iron rule; code execution for referees |
| 3 | shell, Python, web search | the author's model inputs: p, the ψ window, ξ, the ε coefficient | the referee's independent recomputation | verification checks arithmetic, not the model; independent anchors |
| 4 | shell, Python, web | the author's reduced-model check; fixed-seed Monte Carlo values | the referee's stability analysis and its own Monte Carlo | reduced-model stability; Monte Carlo error bars |

Once the referee could run code, the errors that survived were on the author's side. In the wiki's reading, each was a check that passed for a reason other than the claim being right.

Round 5, with two referees using shell, Python and web, falls on the same side. What survived was the author's: a parameter dropped from a cited formula (ruling R1) and five minor numerical findings, "four of them in conventions listed" in the forecast. Its two rules are on [its page](round-5.md#the-lessons).

## What it does not cover

- **Correlated blind spots.** The referees of rounds 3 to 5 are "the same model family as the author". Code execution removes the arithmetic failure mode, and "It does not remove correlated blind spots." (round-3 pre-registration).
- **Severity.** The calibration record shows the author locating the weakest link better but still underestimating it: "Weakest-link location has improved. Severity is still underestimated." ([`review/round4-adjudication.md`](../../../review/round4-adjudication.md); [pre-registration](pre-registration.md)). Round 5's adjudication: "Weakest-link location: hit in rounds 4 and 5." and "Still underestimated: the number of small errors in a long text, and the extent of prior art."
- **Whether the physics is right.** [#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification): "What no machine can check is whether the algebra is attached to the right physics; that verdict belongs to expert readers and, ultimately, to data."

## Sources

- [`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — the measured failure mode of rounds 1–2, the referees' valid findings and their errors
- [`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it), [§4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — the iron rule, "load-bearing — see §6"; the arbitration code that exists only in the chat
- [`review/v3-worklog.md`](../../../review/v3-worklog.md) 'Round-2 pending list' (R2, R4) — round 2's coupling-running and mixing claims checked in code and literature
- [`review/round3-preregistration.md`](../../../review/round3-preregistration.md) — what code execution removes and what it does not; the forecast of zero numerical indictments
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Rulings' (1, 4, 8, 13), 'Pre-registration scored', 'Lessons (now in CLAUDE.md)' — the shift to the author's side and the anchor lesson
- [`review/round4-preregistration.md`](../../../review/round4-preregistration.md), [`review/round4-adjudication.md`](../../../review/round4-adjudication.md) 'Rulings' (F1, the Monte Carlo control), 'Lessons (into CLAUDE.md)' — round 4's author-side findings and rules
- [`review/round4/referee/audit-notes.md`](../../../review/round4/referee/audit-notes.md) Step 2(d) — the referee's own normalization error, caught by its code
- [`review/round5-preregistration.md`](../../../review/round5-preregistration.md) — the same model family; [`review/round5-adjudication.md`](../../../review/round5-adjudication.md) header, 'Rulings' (R1), 'Pre-registration scored', 'Lessons (into CLAUDE.md)' — round 5's executed code, what survived and the calibration across rounds
- [`wiki/papers/broken-born-checkpoint-v2.md` §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) — "a verification script confirms arithmetic, not the model it encodes"; the limit of machine checks
- [`CLAUDE.md`](../../../CLAUDE.md) 'Method ([HANDOFF §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it))' — the rules as now in force
- [`review/skeptic-review-console.html`](../../../review/skeptic-review-console.html) — #14 v2's density inputs as the round-2 referee received them
