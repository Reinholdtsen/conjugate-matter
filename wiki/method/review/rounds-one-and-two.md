---
title: "Review rounds 1 and 2"
weight: 50
status: record
description: "The two console reviews of #14 v1 and v2 (B / medium; B near B/C / medium), known only from the handoff's summary: the valid findings and where they went, the referees' own arithmetic errors, the pending list R1–R7 that v3 was cut from, and the unreconciled count of reviews."
sources:
  - "HANDOFF.md §6"
  - "HANDOFF.md §1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "review/v3-worklog.md 'Round-2 pending list', 'Findings neither referee raised', 'v3 as drafted (2026-10-19)', 'Round 3 outcome (2026-10-19)'"
  - "review/skeptic-review-console.html"
  - "review/round3-preregistration.md"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/wiki-build-flags.md item 35"
  - "review/wiki-build-flags.md item 60"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
---

*Review rounds 1 and 2 were the program's first two blind reviews, both of [#14](../../../notes/knot-dark-matter-standalone.md), the standalone manuscript proposing [superheavy hidden-sector solitons](../../dark-matter/candidates/soliton-candidate/obituary.md) as dark matter. Both ran through the [skeptic review console](skeptic-console.md): a fresh referee with web search and no code execution. Round 1 graded version 1 B, flawed but salvageable, with medium confidence, and every valid finding was folded into version 2; round 2 graded version 2 "B near B/C" and called the derivation of the hidden coupling numerology. Round 2's findings became the pending list R1–R7, from which version 3 was cut for [round 3](round-3/_index.md). The rounds are known only from the handoff's summary: the referees' reports and the full adjudications were never brought into the repository.*

**Status:** Record — untagged. The only account in the repository is the summary in [`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode), with mentions in [§1](../../../HANDOFF.md#1-what-this-project-is)–[§4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) and [§8](../../../HANDOFF.md#8-ranked-next-actions-queue); the full adjudications, "with executed arbitration code", exist only in the old chat ([`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact)). The pending list is moot for #14: v3 was cut from it, failed round 3 and was withdrawn, and #14's model, built with ordinary kinematics, failed on its recomputed abundance ([Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md)); the candidate it modeled, conjugate monopoles localized in momentum, is P.R.'s open conjecture.

## What survives of the record

Only a summary survives. The account of the rounds on this page comes from the handoff, which the author wrote when the project moved from claude.ai to Claude Code, and from the worklog that later used it. None of it can be checked against the reports from inside the repository. What exists and what does not:

| Item | Where it is |
| --- | --- |
| The verdicts, valid findings and referee errors | [`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode), "sufficient if those files are absent" ([§3](../../../HANDOFF.md#3-artifact-inventory-creation-order)) |
| The two referee reports | "two referee-report text files (round 1 and round 2 outputs of [#15](../../../review/skeptic-review-console.html))" that P.R. holds ([`HANDOFF.md` §3](../../../HANDOFF.md#3-artifact-inventory-creation-order)); "The round-2 referee report itself is not in the repo", and P.R. holds it ([`review/v3-worklog.md`](../../../review/v3-worklog.md)) |
| The full adjudications and their arbitration code | only in the chat: "Full adjudications of review rounds 1–2 with executed arbitration code (summarized in §6)" ([`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact)) |
| The pre-registrations | not in the repository; only their score survives, "2 for 2 on verdicts" |
| #14 v1, the manuscript of round 1 | not in the repository |
| #14 v2, the manuscript of round 2 | verbatim in [`review/skeptic-review-console.html`](../../../review/skeptic-review-console.html), and in git history |
| The dates of the rounds | not recorded |

## How the rounds were run

The referee was the console's: in the handoff's words for round 1, "fresh Sonnet, web search, blind", and for round 2, "same protocol, on v2". It received the manuscript and an adversarial prompt that asked it to grade the paper A (coherent speculative physics), B (flawed but salvageable) or C (confabulation), name the single weakest link, and check citations, theorems, consistency, arithmetic and omitted constraints. It could search the web but not run code ([the skeptic review console](skeptic-console.md)).

The manuscript was #14, the proposal that dark matter consists of superheavy [topological solitons](../../symmetry-breaking/topological-defects.md#topological-and-non-topological-solitons-t), monopole-class defects of a hidden gauge sector identified with the momentum-polarized half of broken [Born reciprocity](../../phase-space/reciprocity/born-reciprocity.md) ([#14's soliton model (failed)](../../dark-matter/candidates/soliton-candidate/_index.md)). Round 1 reviewed version 1; round 2 reviewed version 2, which "incorporates all valid round-1 findings" ([`HANDOFF.md` §3](../../../HANDOFF.md#3-artifact-inventory-creation-order)).

## Round 1: #14 v1

**Verdict:** "**B / medium**".

**Valid findings**, "all incorporated in #14 v2" ([`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode)):

- **The coupling contradiction.** v1 fixed the hidden coupling α_d ≈ 34 by [Dirac quantization](../../electric-magnetic-duality/monopoles/dirac-quantization.md) against our own [charge lattice](../../electric-magnetic-duality/symplectic-charge-lattice.md), and also held that the hidden solitons do not couple to our photon. The handoff lists this among its failed claims as the "round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen); DSZ is the Dirac–Schwinger–Zwanziger charge pairing). v2 "restated" the coupling "as reciprocity-as-S conjecture", which round 2 then attacked. The coupling in its first form, via our photon, is under review ([Under review: the coupling α_d ≈ 34](../../dark-matter/candidates/soliton-candidate/alpha-d-coupling.md)).
- **An inverted citation.** The Preskill citation was "inverted (fixed)". v2 cites Preskill [8] for the finding that annihilation is inefficient for superheavy monopoles, "the historical overproduction problem" ([the monopole problem](../../electric-magnetic-duality/monopoles/monopole-problem.md)).
- **Kinetic mixing.** "kinetic mixing unaddressed (postulate + ε ≲ 10⁻⁵ exclusion added)". v2 added the sector-separation postulate and an exclusion condition for mixing above that level ([kinetic mixing between sectors](../../dark-matter/candidates/soliton-candidate/kinetic-mixing.md)).
- **A misnomer.** "'knots' → π₂ monopole-class (renamed)". v2 calls its objects "monopole-class defects classified by pi_2, not knot solitons in the pi_3/Hopfion sense".
- **[Gravitational-wave backgrounds](../../cosmology/early-universe/phase-transition-gravitational-waves.md)**, from a first-order hidden transition, were added.
- **The toy Lagrangian.** The referee's demand for an explicit model was "adopted as acceptance criterion [#1](../../../notes/broken-born-theory.md)". Both reviewers named it ([acceptance criterion 1](../../symmetry-breaking/toy-models/acceptance-criterion.md)).

**The referee's own errors**, "machine-arbitrated": "GeV→gram conversion off 10³; σ_T/M misread as σ_T (off ~10⁴³); insinuated the compatibility theorem might be false (it is machine-verified)" ([the compatibility theorem](../../phase-space/born-geometry/compatibility-theorem.md); [the verification battery](../verification/battery.md); [cross-sections per unit mass](../../dark-matter/halo-astrophysics/transfer-cross-section.md#per-unit-mass-t)).

## Round 2: #14 v2

**Verdict:** "**B near B/C / medium**". **Weakest link:** "the α_d derivation ("matrix coincidence ≠ physical identity" / "numerology")", that is, v2's claim that [the reciprocity map, acting as the modular S transformation](../../dark-matter/candidates/soliton-candidate/alpha-d-coupling.md#conjecture-reciprocity-acting-as-modular-s), fixes the hidden coupling to 1/(4α). The objection still stands. v2 had made that S-dual identification of the momentum-polarized sector its load-bearing conjecture, "load-bearing for alpha_d" (#14 v2 §6, embedded in [`review/skeptic-review-console.html`](../../../review/skeptic-review-console.html)), and [#11 §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) records it as related to P.R.'s [magnetic-mirror conjecture](../../electric-magnetic-duality/magnetic-identification.md), whose separate-photon form is #14 v2's. §11.4 lists the objection as open in either form of the conjecture: "the round-2 objection that a shared matrix is not a shared physics ("matrix coincidence ≠ physical identity"), since [[0,1],[−1,0]] is the canonical form of any two-dimensional symplectic pairing [T]".

**Valid findings**, "**PENDING for v3 of #14**" (capitals in the original). The worklog for v3 numbered them R1–R7 and settled each before v3 was drafted ([`review/v3-worklog.md`](../../../review/v3-worklog.md), 'Round-2 pending list'):

| # | The finding ([`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode)) | Status when v3 was cut | Evidence or decision (worklog) |
| --- | --- | --- | --- |
| R1 | the supersymmetry-exactness burden for Montonen–Olive duality: "either reciprocity supplies the rigidity or the dual sector is approximately" supersymmetric | ready | exact S-duality has been tested only in N = 4 super Yang–Mills theory and special finite N = 2 theories; without supersymmetry there is "no reason to think" it survives quantum corrections, "an expectation, not a no-go" ([S-duality and Montonen–Olive](../../electric-magnetic-duality/s-duality.md)) |
| R2 | the coupling convention and its running: "α at transition scale drags 34 toward ~6–8" | adjudicated [V] | "Convention: 1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn)"; the "toward ~6–8" is "not reproduced for the electromagnetic coupling"; present α_d "as free-but-strong" |
| R3 | the extended Parker bound ([Adams et al. 1993](https://doi.org/10.1103/PhysRevLett.70.2511)): "our-U(1) exclusion is ~7 orders, not 5" | ready, counterfactual only | "Excess at the 10¹⁶ benchmark: 6.98 orders [V]" ([monopole flux bounds](../../electric-magnetic-duality/monopoles/monopole-searches.md)) |
| R4 | gravity-induced kinetic mixing: the referee's mechanism had a formula that was "uncited and unverified", and v2's "forbidden to all orders" was "too strong either way" | ready; the question changes | "The referee is right that it exists, and it is negligible": ε = 0 if hidden charge conjugation is exact, otherwise ≲10⁻¹³ from pure gravity ([kinetic mixing between sectors](../../dark-matter/candidates/soliton-candidate/kinetic-mixing.md)) |
| R5 | the [entropy-dilution](../../cosmology/early-universe/inflation-and-dilution.md) caveat | adjudicated [V], "stronger than the referee said" | the mass window was not "Kibble-only" (finding F1 below) |
| R6 | name an explicit candidate group: "dual SU(2)→U(1) suffices" | ready | "SU(2) → U(1) by an adjoint Higgs", later extended to need "at least one light dark doublet" ([the hidden SU(2) → U(1) proposal](../../dark-matter/candidates/soliton-candidate/hidden-sector.md)) |
| R7 | the [bimetric cosmological-branch](../../gravity/spin-2-fields/bimetric-cosmology.md) instability: "mass hierarchy may evade" | ready, with a tension | the published escape assumes unequal [Planck masses](../../gravity/spin-2-fields/planck-units.md#two-metrics-two-planck-masses), while reciprocity forces equal ones; "v3: state this as an open consistency item, not as evaded" ([Open: stability at equal Planck masses](../../gravity/momentum-graviton/equal-planck-mass-stability.md)) |

**The referee's own errors**, "machine-arbitrated": it "fed ρ_DM = 1.26×10⁻³ GeV/cm³ instead of 1.26×10⁻⁶ (the manuscript's own number) — with the right input the closure lands within 3%", and it "conflated mean vs local density labels (manuscript's 1.3×10⁻²² mean and one-per-25-km³ local are both exactly right)". With round 1's errors these make up the evidence for [the measured failure mode](referee-failure-mode.md).

## From round 2 to version 3

Cutting v3 from the pending list turned up three findings "neither referee raised" ([`review/v3-worklog.md`](../../../review/v3-worklog.md)):

- **F1**, the mass window was not "Kibble-only": the [Kibble estimate](../../electric-magnetic-duality/monopoles/kibble-mechanism.md) fixes a single mass, and at the 10¹⁶ GeV benchmark the observed density needs [entropy dilution](../../cosmology/early-universe/relic-yield-and-dilution.md#entropy-dilution-t) of 1.3×10¹⁰. The benchmark moved to 3×10¹³ GeV ([overproduction at the benchmark](../../dark-matter/candidates/soliton-candidate/overproduction.md)).
- **F2**, v2 used the weak value of the coupling that sets the soliton mass in one section and the strong value in others; v3 reframed the coupling hypothesis and did not use S-duality to fix α_d ([F2, superseded](../../dark-matter/candidates/soliton-candidate/alpha-d-coupling.md#superseded-f2-which-coupling-sets-the-soliton-mass)). The decision behind that reframing is withdrawn, and F2's finding stands (flag 60 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). In the separate-photon form of P.R.'s magnetic-mirror conjecture [O], #14 v2's form ([#11 §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)), which coupling of the p-polarized sector is the S-image of ours, the elementary one or the magnetic one, is open, and F2's finding is that the choice decides whether the sector's solitons are heavy. Round 2's supersymmetry-exactness burden (R1 above), which the worklog expected to shrink if S no longer carried α_d, is among the conjecture's open items in [§11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23). #14 is withdrawn.
- **L1**, from the literature: with a massless dark photon, mixing gives the hidden monopoles no ordinary magnetic flux, so v2's mixing premise was wrong for its own setup.

v3 was drafted on 2026-10-19, with every number it quoted gated in a script. It was reviewed in [round 3](round-3/_index.md), the first round whose referee could execute code, and "failed blind review with **verdict C**" on a [wrong Kibble normalization](../../dark-matter/candidates/soliton-candidate/kibble-normalization.md). It was withdrawn. [Round-3 Decision 2](round-3/decisions.md) retired #14's model, which used ordinary kinematics, as a program-native proposal ([Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md); [the graveyard](../../status/graveyard.md)); the candidate it modeled, conjugate monopoles localized in momentum, is P.R.'s open conjecture.

## What the two rounds established

- **A measured failure mode.** Referees without code were "strong on structure, literature and logic; **unreliable on unaided arithmetic**" ([`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode)). This made [the iron rule](../verification/iron-rule.md) "load-bearing" and was "the main reason the project is moving" to Claude Code.
- **The gate to verdict A.** The handoff's open item 1, the toy Lagrangian, is the one "both reviewers independently named", and its queue calls it "the item both independent reviewers named as the gate to verdict A" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen), [§8](../../../HANDOFF.md#8-ranked-next-actions-queue)). The [toy models](../../symmetry-breaking/toy-models/_index.md) were built to meet it and reviewed in [round 4](round-4.md).
- **The common objection.** Round 3's adjudication: "Every referee across three rounds converges on 'the framework does no work'" ([the 'framework does no work' critique](../../program/framework-does-no-work.md)).
- **Pre-registration.** Both rounds were pre-registered and "scored 2 for 2 on verdicts" ([`review/round3-preregistration.md`](../../../review/round3-preregistration.md), citing [`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); on that pointer, see flag 35 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [pre-registration](pre-registration.md)).

## Unresolved: how many reviews returned B

[`HANDOFF.md` §1](../../../HANDOFF.md#1-what-this-project-is) says "Three blind AI reviews returned verdict B ("flawed but salvageable")". Its §6 records two completed rounds, "B / medium" and "B near B/C / medium", and a third, "Round 3 (incomplete)", that "died partway on a rate limit" before giving a verdict. No document reconciles the count ([conflicts between sources](../../history/documents/source-conflicts.md#method-and-records)).

## Sources

- [`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — both rounds: verdicts, valid findings, the referees' errors, the pending items, the failure mode
- [`review/v3-worklog.md`](../../../review/v3-worklog.md) 'Round-2 pending list', 'Findings neither referee raised', 'v3 as drafted (2026-10-19)', 'Round 3 outcome (2026-10-19)' — R1–R7 with their status and evidence; F1, F2, L1; the round-2 report not in the repository
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — the α_d inconsistency credited to round 1; the toy Lagrangian named by both reviewers
- [`HANDOFF.md` §3](../../../HANDOFF.md#3-artifact-inventory-creation-order), [§4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — the referee-report files P.R. holds; v2 incorporating round 1; the chat-only adjudications
- [`HANDOFF.md` §8](../../../HANDOFF.md#8-ranked-next-actions-queue) — the toy Lagrangian as the gate to verdict A
- [`HANDOFF.md` §1](../../../HANDOFF.md#1-what-this-project-is) — the unreconciled "Three blind AI reviews"
- [`review/skeptic-review-console.html`](../../../review/skeptic-review-console.html) — the referee set-up and #14 v2 as embedded, its §6 calling the S-dual identification "load-bearing for alpha_d"
- [`review/round3-preregistration.md`](../../../review/round3-preregistration.md) — "scored 2 for 2 on verdicts"
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Decisions' (4) — the referees' convergence on "the framework does no work"
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 35 — the round-3 file's pointer to [`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) for the 2-for-2 record, pending; item 60 — F2's finding
- [`wiki/papers/broken-born-checkpoint-v2.md` §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) — the magnetic-mirror conjecture [O] and #14 v2's related identification, F2's finding, and round 2's objection and supersymmetry burden, open
