---
title: "Verification checks arithmetic, not the model"
weight: 20
status: method
description: "A script confirms the arithmetic of the model it encodes; the soliton manuscript's wrong Kibble input passed such a script and only independent review caught it. The limit as it applies to every script in the gate."
sources:
  - "papers/broken-born-checkpoint-v2.md §2"
  - "CLAUDE.md 'Method'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3-preregistration.md 'Protocol (HANDOFF §6, round 3)'"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/wiki-build-flags.md items 3, 4, 11, 14, 33"
---

*A verification script confirms that a calculation was carried out correctly for the inputs and formulas written into it; it cannot tell whether those inputs and formulas are the right physics. The program learned this from its soliton dark-matter manuscript: every number in it was computed and checked by a gated script, yet one formula, the normalization of how many monopoles the early universe forms, was wrong, and only an independent review caught it. Checkpoint #11 has carried the caution since version 2.1, the rule on independent anchors is the repair, and every script page in this section states what its checks leave to the derivation.*

**Status:** Method, in force since #11 v2.1 — untagged — #11 §2 and root `CLAUDE.md` ('Method'); round-3 ruling 13, "Upheld in substance".

## The principle

[Checkpoint #11](/wiki/history/documents/checkpoint) §2: "A caution added in v2.1: a verification script confirms arithmetic, not the model it encodes — the §12 failure passed a script whose physics input was wrong, and was caught only by an independent review." Root `CLAUDE.md` opens its rule on anchors with the same point: "A verification check confirms arithmetic, not the model."

A script encodes a model: its inputs, its formulas, the approximations chosen. When every check passes, the outputs follow from those choices without arithmetic error. Whether the choices are correct is a separate question, and a check that compares the script's output with the paper's figure cannot answer it, because the paper and the script share the choices. #11 §2's plain-language passage puts it as "What no machine can check is whether the algebra is attached to the right physics; that verdict belongs to expert readers and, ultimately, to data." That is why #11's [claim tiers](/wiki/method/claim-tiers) put machine-checked algebra in Tier 1 and keep novel structural physics in Tier 3 at an "honest prior per claim ~50–80%".

## The episode: round 3

### A manuscript computed throughout

The [soliton manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary), #14 v3, stated its own standard: "All numerical statements in Secs. 2-4 were computed by executed code rather than by hand." (§6). The worklog confirms it: "Every number it quotes is a gated check" in knot_numbers.py, the script then in the gate (`review/v3-worklog.md`, 'v3 as drafted'). The [iron rule](/wiki/method/verification/iron-rule) had been followed to the letter.

The round-3 pre-registration predicted "zero surviving numerical indictments", on the ground that every number had been computed by that script ([round 3's pre-registration](/wiki/method/review/round-3/preregistration)).

### What the referee found

The referee, a fresh agent with code execution, recomputed the numbers "from independently chosen constants", as the round-3 protocol asked (`review/round3-preregistration.md`), and found the Kibble normalization wrong: "p = 0.023 is the H^3 abundance with the 1.66 sqrt(g\*) factor dropped". Its conceptual audit added: "Sec. 6 says all numbers were computed by executed code; the p error (a dropped prefactor of 4576) and the psi window (factor 3-10 in mass) indicate otherwise or a coding error." (`review/round3/referee/audit-notes.md`, Step 4(a), items 1 and 9).

The adjudication showed it was neither: the code had computed the formula it was given. Ruling 1: "Kibble normalization: one defect per Hubble volume is p ≈ 104, not 0.023", upheld, with "My error came from misremembering the formula." Ruling 13: "v3 §6 "all numbers computed by executed code" overstates", "Upheld in substance": "The code checked the arithmetic of a wrong model. See lesson 2." ([Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings); [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)).

### What survived, and what kind of error each was

The pre-registration was scored a miss: "Three survive (p; the ψ window; ξ), plus the ε coefficient", "**Miss**. All are wrong inputs or model choices in my scripts, not arithmetic slips". Each is a choice the script took as given:

- **p**, a misremembered formula: the yield of one defect per Hubble volume without the factor (1.66 √g\*)³ (ruling 1).
- **The ψ window**, a counting choice: "v3 omitted ψ̄ and the second doublet member (a factor of 4), and bracketed an exactly known s-wave σv up to ×10" (ruling 4; [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)).
- **ξ**, an input value: "Using N_eff,SM = 3.044, the 95% bound is ΔN_eff < 0.286" (ruling 5; SM is the Standard Model).
- **The ε coefficient**, an assumed coupling: the "O(1) coefficient at the Planck scale" for the kinetic-mixing operator "is unsupported" (ruling 7; [the dimension-5 operator](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator)).

No arithmetic slip survived. The consequence was still fatal to the candidate ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

### The failure mode moved

The adjudication's calibration note: "The failure mode has moved. In rounds 1–2 it was the referee's unaided arithmetic. In round 3 it is that **the author's verification checks the author's model**: a wrong physics input passes a gate that tests only arithmetic." (`review/round3-adjudication.md`; [The measured referee failure mode](/wiki/method/review/referee-failure-mode)).

## What changed

- **The caution in #11.** Version 2.1 of #11 added the §2 sentence quoted above.
- **Independent anchors.** Lesson 2: "An anchor must be independent of the paper. v3's Kibble anchor reproduced v2's own number and so tested nothing." A script now tests its formulas on cases known from outside the paper before it computes the paper's numbers ([Independent anchors](/wiki/method/verification/independent-anchors)).
- **A new script.** knot_numbers.py was replaced by `verify/soliton_obituary.py`, which checks the corrected record after four such anchors ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).
- **The same limit in other forms.** Round 4 found two relatives of it. A stability check had covered only part of the model: "I should have caught F1 myself: I checked the potential only at frozen H." ([the reduced-model stability rule](/wiki/method/verification/reduced-model-stability)). And a simulation number, computed correctly, was a short-run fluctuation ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)). In each case the code did what it was written to do.

## The limit in the current scripts

The pages for the scripts in [the gate](/wiki/method/verification/the-gate) each end with what the script does not check, because a passing check is easily read as covering more than it does. Examples:

- **The battery.** Tests T3, T4 and T7 check algebra on random samples. During the wiki build, verifiers found suspected errors in statements written next to that algebra in calc note #7: a zero set larger than stated (flag 3), a second-order term missing from an expansion (flag 4), and a notational slip about which trace a power sum gives (flag 14). The tests pass, because they test the algebra as written and not those statements ([the verification battery](/wiki/method/verification/battery)).
- **The toy-model scripts.** The check labelled with round-4 finding F6 tests a harmonic series against Euler's constant. It does not settle whether the tadpole grows as ln N or 2 ln N, on which the toy note and the adjudication differ (flag 11; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).
- **The soliton-obituary script.** Its docstring says it checks "every number" of the round-3 record; its checks cover the obituary's [V] numbers and the adjudicator's own figures, not the referee's or the literature's (flag 33 in `review/wiki-build-flags.md`).

These flags are suspected errors in the source documents, quoted faithfully on the pages that carry the statements and awaiting Paul's ruling (`review/wiki-build-flags.md`).

## Sources

- `papers/broken-born-checkpoint-v2.md` §2 — the v2.1 caution; the plain-language limit of Tier 1; the tiers
- Root `CLAUDE.md` 'Method' — the rule as now stated
- `review/round3-adjudication.md` 'Rulings' (1, 4, 5, 7, 13), 'Pre-registration scored', 'Lessons (now in CLAUDE.md)' — the ruling, the missed prediction, the moved failure mode, the anchor lesson
- `review/round3/referee/audit-notes.md` Step 4(a) items 1 and 9 — the referee's finding and its reading of §6
- `review/round3-preregistration.md` 'Protocol' — independently chosen constants; 'Predictions' — zero surviving numerical indictments
- `review/v3-worklog.md` 'v3 as drafted (2026-10-19)' and `notes/knot-dark-matter-standalone.md` §6 — the manuscript computed throughout
- `review/round4-adjudication.md` 'Rulings' (F1, F2, and the Monte Carlo control, "MC control") — the round-4 relatives
- `review/wiki-build-flags.md` items 3, 4, 11, 14 — suspected source errors beside passing checks; item 33 — the soliton script's claimed coverage
