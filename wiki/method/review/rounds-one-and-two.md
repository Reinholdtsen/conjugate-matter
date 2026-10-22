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
---

*Review rounds 1 and 2 were the program's first two blind reviews, both of #14, the standalone manuscript proposing [superheavy hidden-sector solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) as dark matter. Both ran through the [skeptic review console](/wiki/method/review/skeptic-console): a fresh referee with web search and no code execution. Round 1 graded version 1 B, flawed but salvageable, with medium confidence, and every valid finding was folded into version 2; round 2 graded version 2 "B near B/C" and called the derivation of the hidden coupling numerology. Round 2's findings became the pending list R1–R7, from which version 3 was cut for [round 3](/wiki/method/review/round-3). The rounds are known only from the handoff's summary: the referees' reports and the full adjudications were never brought into the repository.*

**Status:** Record — untagged. The only account in the repository is the summary in `HANDOFF.md` §6, with mentions in §1–§4 and §8; the full adjudications, "with executed arbitration code", exist only in the old chat (`HANDOFF.md` §4). The pending list is moot: v3 was cut from it, failed round 3 and was withdrawn, and the candidate is [retired](/wiki/dark-matter/candidates/soliton-candidate/obituary).

## What survives of the record

Only a summary survives. The account of the rounds on this page comes from the handoff, which the author wrote when the project moved from claude.ai to Claude Code, and from the worklog that later used it. None of it can be checked against the reports from inside the repository. What exists and what does not:

| Item | Where it is |
| --- | --- |
| The verdicts, valid findings and referee errors | `HANDOFF.md` §6, "sufficient if those files are absent" (§3) |
| The two referee reports | "two referee-report text files (round 1 and round 2 outputs of #15)" that Paul holds (`HANDOFF.md` §3); "The round-2 referee report itself is not in the repo. Paul holds it." (`review/v3-worklog.md`) |
| The full adjudications and their arbitration code | only in the chat: "Full adjudications of review rounds 1–2 with executed arbitration code (summarized in §6)" (`HANDOFF.md` §4) |
| The pre-registrations | not in the repository; only their score survives, "2 for 2 on verdicts" |
| #14 v1, the manuscript of round 1 | not in the repository |
| #14 v2, the manuscript of round 2 | verbatim in `review/skeptic-review-console.html`, and in git history |
| The dates of the rounds | not recorded |

## How the rounds were run

The referee was the console's: in the handoff's words for round 1, "fresh Sonnet, web search, blind", and for round 2, "same protocol, on v2". It received the manuscript and an adversarial prompt that asked it to grade the paper A (coherent speculative physics), B (flawed but salvageable) or C (confabulation), name the single weakest link, and check citations, theorems, consistency, arithmetic and omitted constraints. It could search the web but not run code ([the skeptic review console](/wiki/method/review/skeptic-console)).

The manuscript was #14, the proposal that dark matter consists of superheavy topological solitons, monopole-class defects of a hidden gauge sector identified with the momentum-polarized half of broken [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ([the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate)). Round 1 reviewed version 1; round 2 reviewed version 2, which "incorporates all valid round-1 findings" (`HANDOFF.md` §3).

## Round 1: #14 v1

**Verdict:** "**B / medium**".

**Valid findings**, "all incorporated in #14 v2" (`HANDOFF.md` §6):

- **The coupling contradiction.** v1 fixed the hidden coupling α_d ≈ 34 by [Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) against our own charge lattice, and also held that the hidden solitons do not couple to our photon. The handoff lists this among the dead claims as the "round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon" (`HANDOFF.md` §2; DSZ is the Dirac–Schwinger–Zwanziger charge pairing). v2 "restated" the coupling "as reciprocity-as-S conjecture", which round 2 then attacked ([obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).
- **An inverted citation.** The Preskill citation was "inverted (fixed)". v2 cites Preskill [8] for the finding that annihilation is inefficient for superheavy monopoles, "the historical overproduction problem" ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)).
- **Kinetic mixing.** "kinetic mixing unaddressed (postulate + ε ≲ 10⁻⁵ exclusion added)". v2 added the sector-separation postulate and an exclusion condition for mixing above that level ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).
- **A misnomer.** "'knots' → π₂ monopole-class (renamed)". v2 calls its objects "monopole-class defects classified by pi_2, not knot solitons in the pi_3/Hopfion sense".
- **[Gravitational-wave backgrounds](/wiki/cosmology/early-universe/phase-transition-gravitational-waves)**, from a first-order hidden transition, were added.
- **The toy Lagrangian.** The referee's demand for an explicit model was "adopted as acceptance criterion #1". Both reviewers named it ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)).

**The referee's own errors**, "machine-arbitrated": "GeV→gram conversion off 10³; σ_T/M misread as σ_T (off ~10⁴³); insinuated the compatibility theorem might be false (it is machine-verified)" ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem); [the verification battery](/wiki/method/verification/battery)).

## Round 2: #14 v2

**Verdict:** "**B near B/C / medium**". **Weakest link:** "the α_d derivation ("matrix coincidence ≠ physical identity" / "numerology")", that is, v2's claim that [the reciprocity map, acting as the modular S transformation](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#superseded-reciprocity-acting-as-modular-s), fixes the hidden coupling to 1/(4α).

**Valid findings**, "**PENDING for v3 of #14**" (capitals in the original). The worklog for v3 numbered them R1–R7 and settled each before v3 was drafted (`review/v3-worklog.md`, 'Round-2 pending list'):

| # | The finding (`HANDOFF.md` §6) | Status when v3 was cut | Evidence or decision (worklog) |
| --- | --- | --- | --- |
| R1 | the supersymmetry-exactness burden for Montonen–Olive duality: "either reciprocity supplies the rigidity or the dual sector is approximately" supersymmetric | ready | exact S-duality has been tested only in N = 4 super Yang–Mills theory and special finite N = 2 theories; without supersymmetry there is "no reason to think" it survives quantum corrections, "an expectation, not a no-go" ([S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality)) |
| R2 | the coupling convention and its running: "α at transition scale drags 34 toward ~6–8" | adjudicated [V] | "Convention: 1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn)"; the "toward ~6–8" is "not reproduced for the electromagnetic coupling"; present α_d "as free-but-strong" |
| R3 | the extended Parker bound (Adams et al. 1993): "our-U(1) exclusion is ~7 orders, not 5" | ready, counterfactual only | "Excess at the 10¹⁶ benchmark: 6.98 orders [V]" ([monopole flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches)) |
| R4 | gravity-induced kinetic mixing: the referee's mechanism had a formula that was "uncited and unverified", and v2's "forbidden to all orders" was "too strong either way" | ready; the question changes | "The referee is right that it exists, and it is negligible": ε = 0 if hidden charge conjugation is exact, otherwise ≲10⁻¹³ from pure gravity ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)) |
| R5 | the [entropy-dilution](/wiki/cosmology/early-universe/inflation-and-dilution) caveat | adjudicated [V], "stronger than the referee said" | the mass window was not "Kibble-only" (finding F1 below) |
| R6 | name an explicit candidate group: "dual SU(2)→U(1) suffices" | ready | "SU(2) → U(1) by an adjoint Higgs", later extended to need "at least one light dark doublet" ([the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)) |
| R7 | the [bimetric cosmological-branch](/wiki/gravity/spin-2-fields/bimetric-cosmology) instability: "mass hierarchy may evade" | ready, with a tension | the published escape assumes unequal Planck masses, while reciprocity forces equal ones; "v3: state this as an open consistency item, not as evaded" ([Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)) |

**The referee's own errors**, "machine-arbitrated": it "fed ρ_DM = 1.26×10⁻³ GeV/cm³ instead of 1.26×10⁻⁶ (the manuscript's own number) — with the right input the closure lands within 3%", and it "conflated mean vs local density labels (manuscript's 1.3×10⁻²² mean and one-per-25-km³ local are both exactly right)". With round 1's errors these make up the evidence for [the measured failure mode](/wiki/method/review/referee-failure-mode).

## From round 2 to version 3

Cutting v3 from the pending list turned up three findings "neither referee raised" (`review/v3-worklog.md`):

- **F1**, the mass window was not "Kibble-only": the [Kibble estimate](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) fixes a single mass, and at the 10¹⁶ GeV benchmark the observed density needs entropy dilution of 1.3×10¹⁰. The benchmark moved to 3×10¹³ GeV ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)).
- **F2**, v2 used the weak value of the coupling that sets the soliton mass in one section and the strong value in others; v3 reframed the coupling hypothesis ([F2, superseded](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#superseded-f2-which-coupling-sets-the-soliton-mass)).
- **L1**, from the literature: with a massless dark photon, mixing gives the hidden monopoles no ordinary magnetic flux, so v2's mixing premise was wrong for its own setup.

v3 was drafted on 2026-10-19, with every number it quoted gated in a script. It was reviewed in [round 3](/wiki/method/review/round-3), the first round whose referee could execute code, and "failed blind review with **verdict C**" on a [wrong Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization). It was withdrawn, and the soliton candidate was retired as a program-native proposal ([obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary); [the graveyard](/wiki/status/graveyard)).

## What the two rounds established

- **A measured failure mode.** Referees without code were "strong on structure, literature and logic; **unreliable on unaided arithmetic**" (`HANDOFF.md` §6). This made [the iron rule](/wiki/method/verification/iron-rule) "load-bearing" and was "the main reason the project is moving" to Claude Code.
- **The gate to verdict A.** The handoff's open item 1, the toy Lagrangian, is the one "both reviewers independently named", and its queue calls it "the item both independent reviewers named as the gate to verdict A" (`HANDOFF.md` §2, §8). The [toy models](/wiki/symmetry-breaking/toy-models) were built to meet it and reviewed in [round 4](/wiki/method/review/round-4).
- **The common objection.** Round 3's adjudication: "Every referee across three rounds converges on 'the framework does no work'" ([the 'framework does no work' critique](/wiki/program/framework-does-no-work)).
- **Pre-registration.** Both rounds were pre-registered and "scored 2 for 2 on verdicts" (`review/round3-preregistration.md`, citing `HANDOFF.md` §6; on that pointer, see flag 35 in `review/wiki-build-flags.md`; [pre-registration](/wiki/method/review/pre-registration)).

## Unresolved: how many reviews returned B

`HANDOFF.md` §1 says "Three blind AI reviews returned verdict B ("flawed but salvageable")". Its §6 records two completed rounds with verdict B, and a third, "Round 3 (incomplete)", that "died partway on a rate limit" before giving a verdict. No document reconciles the count ([conflicts between sources](/wiki/history/documents/source-conflicts#method-and-records)).

## Sources

- `HANDOFF.md` §6 — both rounds: verdicts, valid findings, the referees' errors, the pending items, the failure mode
- `review/v3-worklog.md` 'Round-2 pending list', 'Findings neither referee raised', 'v3 as drafted (2026-10-19)', 'Round 3 outcome (2026-10-19)' — R1–R7 with their status and evidence; F1, F2, L1; the round-2 report not in the repository
- `HANDOFF.md` §2 — the α_d kill credited to round 1; the toy Lagrangian named by both reviewers
- `HANDOFF.md` §3, §4 — the referee-report files Paul holds; v2 incorporating round 1; the chat-only adjudications
- `HANDOFF.md` §8 — the toy Lagrangian as the gate to verdict A
- `HANDOFF.md` §1 — the unreconciled "Three blind AI reviews"
- `review/skeptic-review-console.html` — the referee set-up and #14 v2 as embedded
- `review/round3-preregistration.md` — "scored 2 for 2 on verdicts"
- `review/round3-adjudication.md` 'Decisions' (4) — the referees' convergence on "the framework does no work"
- `review/wiki-build-flags.md` item 35 — the round-3 file's pointer to `HANDOFF.md` §6 for the 2-for-2 record, awaiting a ruling
