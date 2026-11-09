---
title: "The iron rule: no arithmetic by eyeball"
weight: 10
status: method
description: "Every asserted or disputed number gets executed code with printed output, kept in verify/; why the AI referees' unit errors in rounds 1 and 2 made it load-bearing, how it is applied, and where it stops."
sources:
  - "CLAUDE.md 'Method'"
  - "HANDOFF.md §5"
  - "HANDOFF.md §6"
  - "review/round3-preregistration.md"
  - "review/round3-adjudication.md header"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round4-adjudication.md header"
  - "review/round5-adjudication.md header"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "scripts/check.sh"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "review/wiki-build-checks/README.md"
  - "review/wiki-build-flags.md items 16, 28"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "verify/dual_sector.py docstring"
---

*The iron rule is the program's requirement that no number be accepted on inspection: every number a document asserts, and every number a reviewer disputes, is computed by code that is actually run and prints its result, and the code is kept in the repository's `verify/` folder. It was adopted after the first two blind reviews, in which AI referees working without code execution made three confident accusations of order-of-magnitude errors, all of which came from their own unit mistakes. The rule makes the arithmetic checkable by anyone who runs the scripts, and [the gate](the-gate.md) runs them before any work counts as finished. It does not make the physics right, which round 3 showed.*

**Status:** Method, in force — untagged — root [`CLAUDE.md`](../../../CLAUDE.md) ('Method') and [`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it); enforced by [the gate](the-gate.md).

## The rule

Root [`CLAUDE.md`](../../../CLAUDE.md), 'Method': "Iron rule: no arithmetic by eyeball. Every asserted or disputed number gets executed code with printed output, kept in `verify/`."

The [handoff](../../history/documents/handoff.md) stated it first, in its verification protocol: "**Iron rule:** no arithmetic by eyeball. Any disputed or asserted number gets executed code with printed output. This is load-bearing — see §6." ([`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it)). The repository version adds where the code lives.

Three parts of the wording matter:

- **"Asserted or disputed".** The rule covers the author's numbers and the reviewer's objections alike. A referee's claim that a number is wrong is settled by running code, not by a second reading.
- **"Executed code with printed output".** The record shows the value the code produced, so a reader can compare it with the document without rerunning anything, and a rerun can be compared with the record.
- **"No arithmetic by eyeball".** Estimates by inspection, including the author's, do not count. A number either has a script behind it or is not asserted.

## Why it was adopted

### Rounds 1 and 2

The first two [blind reviews](../review/_index.md) were of manuscript [#14](../../../notes/knot-dark-matter-standalone.md), the [soliton dark-matter proposal](../../dark-matter/candidates/soliton-candidate/obituary.md), by fresh large language model (LLM) referees with web search and no code execution ("Round 1 (fresh Sonnet, web search, blind)", [`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); the [round-3 pre-registration](../review/round-3/preregistration.md) describes the "arithmetic failure mode of rounds 1–2, which had no code execution"). The referees' own errors, each settled by executed code ("machine-arbitrated"):

- round 1: a "GeV→gram conversion off 10³"; "σ_T/M misread as σ_T (off ~10⁴³)"; and the referee "insinuated the compatibility theorem might be false (it is machine-verified)";
- round 2: the referee "fed ρ_DM = 1.26×10⁻³ GeV/cm³ instead of 1.26×10⁻⁶ (the manuscript's own number) — with the right input the closure lands within 3%", and "conflated mean vs local density labels".

See [Review rounds 1 and 2](../review/rounds-one-and-two.md).

### The measured failure mode

[`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) drew the conclusion: "fresh LLM referees are strong on structure, literature and logic; **unreliable on unaided arithmetic** (3 confident order-of-magnitude indictments, all reviewer unit errors, 0 surviving). Hence the iron rule." See [The measured referee failure mode](../review/referee-failure-mode.md).

The same section gives the rule's practical consequence for the project: "Claude Code's native execution removes this failure mode — that's the main reason the project is moving to you." That was the main reason for the move from the chat to this repository on 2026-10-19 ([the collaboration](../collaboration.md)).

## How it is applied

### The scripts and the gate

Every number a current document asserts is meant to have a check in a script in `verify/`: the [Tier-1](../claim-tiers.md#tier-1-explicit-algebra) algebra of [#11](../../history/documents/checkpoint.md) in [the battery](battery.md), the numbers [#11](../../papers/broken-born-checkpoint-v2.md) gives for [#14's failed model](../../dark-matter/candidates/soliton-candidate/obituary.md) in [the soliton-obituary script](soliton-obituary-script.md), the [toy-model note](../../symmetry-breaking/toy-models/_index.md)'s results in [the toy-model scripts](toy-model-scripts.md), and the numbers of the later notes in [the phase-space-diameter script](phase-space-diameter-script.md), [the closed-universe script](closed-universe-script.md), [the velocity-gated-gravity script](velocity-gated-gravity-script.md) and [the gate-mechanism script](gate-mechanism-script.md); the literature-check note's two tables, its pre-registration score and the counts it states for the citation screen, the code checks, the panel's label changes, the workflows, the verdicts of the two reviews of its write-up and of the two checks that followed them, and the second review's findings by reviewer, are recomputed in [the literature-check script](literature-check-script.md), which also checks the algebra behind flag 66 (its section G); the note's other counts, among them the queries that did not run, are not. The dual-sector note's dates are checked against its record, and the counts it states for its workflows, its two sweeps and its panel's verdicts, with the pre-registration's score, are recomputed in [the dual-sector script](dual-sector-script.md), which also finds the note's quotations again, checks its citations and, in its section F, computes the bracket of the doubled phase space. [`scripts/check.sh`](../../../scripts/check.sh) runs all twelve scripts and fails if any check fails. Each check prints its measured value, which is the "printed output" the rule asks for.

### Referees and adjudicators

Since the move, the referees have executed code as well. Round 3: "Every one of its 16 numerical findings rests on executed code"; round 4: "All 9 of its numerical and algebraic indictments rest on executed code"; round 5: "Every numerical indictment rests on executed code" (adjudication headers). The adjudicator answers in the same way, with arbitration scripts kept beside the rulings ([`review/round3/adjudicator/round3_arb.py`](../../../review/round3/adjudicator/round3_arb.py), [`review/round4/adjudicator/arb.py`](../../../review/round4/adjudicator/arb.py), [`review/round4/adjudicator/ctrl.py`](../../../review/round4/adjudicator/ctrl.py), [`review/round5/adjudicator/arb.py`](../../../review/round5/adjudicator/arb.py)).

### Drafting

The rule also corrects the author before a reviewer sees the text. When v3 of #14 was drafted, every number it quoted was a gated check, and "Two planned figures were corrected by that check before the text was written: the coupling matched at 10¹² GeV is ≈ 29 (not 28), and the minimal model overcloses by 10¹⁶–10¹⁷ (not 10¹⁵–10¹⁷)." ([`review/v3-worklog.md`](../../../review/v3-worklog.md), 'v3 as drafted').

### The wiki

The wiki applies the rule to itself: "Every number on a page is copied from a source document or a `verify/` output, and the page names that source. Nothing is computed, rounded or converted by eye (the iron rule). A number the sources do not contain does not appear." ([`wiki/CLAUDE.md`](../../CLAUDE.md)).

The wiki build is the rule's latest application. When its verifiers suspected an arithmetic error in a source document, they did not correct the page by inspection; they wrote a script, ran it, and kept it with its output in [`review/wiki-build-checks/`](../../../review/wiki-build-checks/), "so that every flag that rests on arithmetic has executed code beside it" (README). For example, [#11 §11.2](../../papers/broken-born-checkpoint-v2.md#112-the-full-dual-spectrum-t) says [Dirac's condition](../../electric-magnetic-duality/monopoles/dirac-quantization.md) "pins the magnetic coupling near 4π/e² ≈ 34"; the last two lines that `dirac_coupling_check.py` prints are

```text
4π/e² = 137.036   (= 1/alpha)
π/e²  = 34.259   (= 1/(4 alpha))
```

Flag 28 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) reads it as: "The number 34 is right; the formula written beside it is not." The pages quote the source as written and point to the flag; the scripts are evidence for the flag and are not part of the gate.

## Where it stops

- **Arithmetic, not physics.** Round 3 found a wrong physical input in a manuscript every number of which had been computed by a gated script: "The failure mode has moved. In rounds 1–2 it was the referee's unaided arithmetic. In round 3 it is that **the author's verification checks the author's model**: a wrong physics input passes a gate that tests only arithmetic." ([`review/round3-adjudication.md`](../../../review/round3-adjudication.md), 'Pre-registration scored'). See [Verification checks arithmetic, not the model](arithmetic-not-model.md) and [Independent anchors](independent-anchors.md).
- **Statistics.** A simulation's number can be computed exactly and still be a fluctuation; round 4 added the [error-bar rule](monte-carlo-error-bars.md).
- **Numbers without a script.** Not every number in the record has one. [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) marks the clumping figure "criterion fails by 10²⁸–10³¹" with ✓, and until 2026-10-28 no script in `verify/` computed it (flag 16). Section D of [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) now reproduces [#2](../../../notes/stream-stability.md)'s two ratios; flag 16's addendum: "The ✓ is now backed by a script"; [#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)'s tag is [D] ([the velocity-gated-gravity script](velocity-gated-gravity-script.md)). The rest of the clumping problem, including the classicality numbers, the wave-island rate and the ultra-faint-dwarf endpoint, has no script. The gate page lists the other gaps ([what is not gated](the-gate.md#what-is-not-gated)).
- **"Kept in `verify/`."** The adjudicators' arbitration scripts are kept in `review/`, beside the rulings, and the gate does not run them; their corrected results are carried into `verify/` instead. The root [`CLAUDE.md`](../../../CLAUDE.md)'s layout and the header of [`scripts/check.sh`](../../../scripts/check.sh) say that arbitration scripts go in `verify/` (flag 38 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).

## Sources

- Root [`CLAUDE.md`](../../../CLAUDE.md) 'Method' — the rule as now stated
- [`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it) — the rule at the handoff; [§6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — rounds 1 and 2, the referees' errors, the measured failure mode, the move to Claude Code
- [`review/round3-preregistration.md`](../../../review/round3-preregistration.md) — the rounds without code execution
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) header and 'Pre-registration scored'; [`review/round4-adjudication.md`](../../../review/round4-adjudication.md) and [`review/round5-adjudication.md`](../../../review/round5-adjudication.md) headers — referees' findings resting on executed code; the moved failure mode
- [`review/round3/adjudicator/round3_arb.py`](../../../review/round3/adjudicator/round3_arb.py), [`review/round4/adjudicator/arb.py`](../../../review/round4/adjudicator/arb.py), [`review/round4/adjudicator/ctrl.py`](../../../review/round4/adjudicator/ctrl.py), [`review/round5/adjudicator/arb.py`](../../../review/round5/adjudicator/arb.py) — the arbitration scripts kept beside the rulings
- [`review/v3-worklog.md`](../../../review/v3-worklog.md) 'v3 as drafted (2026-10-19)' — the two figures corrected before the text was written
- [`scripts/check.sh`](../../../scripts/check.sh) — the gate that runs the scripts
- [`wiki/CLAUDE.md`](../../CLAUDE.md) 'The wiki is derivative' — the rule applied to the wiki
- [`review/wiki-build-checks/README.md`](../../../review/wiki-build-checks/README.md), `dirac_coupling_check.out`; [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) items 16, 28 — the wiki build's executed checks; the check mark without a script, and item 16's addendum of 2026-10-28
- [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) section D — calc note #2's shortfall, gated since 2026-10-28
- [`verify/dual_sector.py`](../../../verify/dual_sector.py) docstring — what the dual-sector script checks: quotations, citations, dates, counts and, in section F, the doubled bracket
