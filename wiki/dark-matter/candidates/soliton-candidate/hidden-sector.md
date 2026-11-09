---
title: "Under review: the hidden SU(2) → U(1) proposal"
weight: 30
status: under-review
description: "An adjoint Higgs breaks SU(2)_d to U(1)_d, leaving W′±, a massless hidden photon, stable monopoles and a light Dirac doublet ψ: a standard prior-art model, under review as a program-native proposal."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/skeptic-review-console.html"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'New open items'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/round3-preregistration.md 'Predictions'"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "verify/soliton_obituary.py"
  - "HANDOFF.md §6"
  - "notes/literature-check.md §4"
  - "review/wiki-build-flags.md item 68"
---

*The hidden SU(2) → U(1) proposal was the particle content the soliton manuscript [#14](../../../../notes/knot-dark-matter-standalone.md) assumed for its dark sector: a hidden copy of a simple gauge force, SU(2)_d, whose Higgs field breaks it down to a single unbroken U(1)_d. The breaking leaves heavy charged W′± bosons, a massless hidden photon, and 't Hooft–Polyakov monopoles that are stable for topological reasons, which were the dark matter in #14's model. A light hidden fermion ψ was added because without it the W′± would overclose the universe. #14 identified this sector with the [momentum-polarized half](../../conjugate-matter/_index.md) of the program's matter, but nothing numerical in the proposal depended on that identification. As a model it is a standard hidden-sector monopole scenario already in the literature; as the program's own proposal it failed with #14's model.*

**Status:** Under review — the evidence below weighs against it, and its final status awaits review. What is under review is the sector as a program-native proposal, a part of #14's model, which round-3 Decision 2 retired ([round-3 decisions](../../../method/review/round-3/decisions.md)). #14 marked the sector "(postulated)" and listed "the identification of the SU(2)_d sector as the momentum-polarized matter sector" as "Conjectural" ([#14 §6](../../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria)). No `verify/` script checks the sector itself; the one result about it that stands, the exclusion of its minimal form, is [V], gated in [`verify/soliton_obituary.py`](../../../../verify/soliton_obituary.py) ([the soliton-obituary script](../../../method/verification/soliton-obituary-script.md)). Home section: [#14's soliton model](_index.md); listed in [claims under review](../../../status/under-review.md).

## What was claimed

### The sector

#14 v3 §2, "The sector (postulated).":

> The momentum-polarized matter sector contains a gauge group SU(2)_d with a real adjoint scalar Phi whose expectation value v breaks it to U(1)_d. U(1)_d stays unbroken, so the hidden photon is massless. The charged vectors W'+- have mass g_d v. The sector also contains at least one Dirac fermion psi in the doublet, with U(1)_d charges +-g_d/2 (Sec. 3 shows it is required).

The subscript d marks the hidden ("dark") sector, and g_d is its gauge coupling.

### What each piece is [T]

The content is the textbook case of an SU(2) gauge theory broken by an adjoint scalar, with a fermion doublet added; the explanation here is standard physics [T].

- **The gauge group and its scalar.** SU(2) has three gauge fields, one for each independent rotation of its internal space. The adjoint scalar Φ is a real three-component field that rotates like a vector in that space. Its potential is minimized when Φ has length v, so the vacuum picks a direction.
- **What breaks and what remains.** Rotations about the chosen direction leave Φ unchanged, so one U(1) subgroup survives: U(1)_d, whose gauge field stays massless and is the hidden photon. The other two gauge fields combine into the charged W′± and acquire mass g_d v by the [Higgs mechanism](../../../symmetry-breaking/goldstone-and-higgs.md).
- **Why there are monopoles.** The vacua, the directions Φ can point with length v, form a sphere, S² = SU(2)/U(1), the [vacuum manifold](../../../symmetry-breaking/topological-defects.md#the-vacuum-manifold-t). Far from a localized object, Φ can point radially outward in every direction, wrapping that sphere once, and no continuous change of the field can undo a wrapping. [#14 §3](../../../../notes/knot-dark-matter-standalone.md#3-the-candidate): "SU(2)_d -> U(1)_d has pi_2(SU(2)/U(1)) = pi_2(S^2) = Z and supports 't Hooft-Polyakov monopoles [15], stable by topological charge." The integer π₂ counts the wrappings ([the 't Hooft–Polyakov monopole](../../../electric-magnetic-duality/monopoles/thooft-polyakov-monopole.md)). Their mass is "M = 4 pi f v/g_d", with f between 1 and about 1.79 ([#14 §3](../../../../notes/knot-dark-matter-standalone.md#3-the-candidate); [overproduction at the benchmark](overproduction.md)).
- **The fermion doublet.** ψ transforms as a two-component doublet of SU(2)_d, so its two components carry U(1)_d charges +g_d/2 and −g_d/2, half the W′ charge. It gives the W′± something to decay into, and its charge g_d/2 is the smallest in the sector, which sets the monopoles' magnetic charge by [Dirac quantization](../../../electric-magnetic-duality/monopoles/dirac-quantization.md) ([the coupling α_d ≈ 34](alpha-d-coupling.md)).

### Why not a mirror copy of the Standard Model

The simplest hidden sector would be an exact copy of ours. [#14 §2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling) ruled that out:

> An exact mirror copy of the Standard Model cannot serve: the electroweak vacuum manifold is S^3, whose pi_2 vanishes, so it has no stable monopoles. The hidden gauge structure must therefore differ from ours.

In the Standard Model a Higgs doublet breaks SU(2) × U(1) to the U(1) of electromagnetism, and the vacua form a three-sphere. Any way of mapping a sphere surrounding a point into a three-sphere can be shrunk continuously to a single vacuum, so no configuration is topologically trapped [T]. The worklog drew the consequence for #14's coupling hypothesis: "An exact mirror copy of the SM has no stable monopoles (π₂(S³) = 0), so H relates couplings only, not gauge groups" ([`review/v3-worklog.md`](../../../../review/v3-worklog.md), 'v3 as drafted (2026-10-19)'; SM is the Standard Model).

### The identification and the separation

Two postulates tied this sector to the program. The first is the identification itself: the opening words of the sector's definition, "The momentum-polarized matter sector contains", place it in the mirror-polarized half of the program's matter content ([P4](../../../program/postulates/p4-polarized-matter.md)). [#14 §6](../../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) listed that identification as "Conjectural". The second is sector separation, also marked "(postulated)": "No field carries charge under both U(1)_d and our hypercharge" ([#14 §2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling)). How weakly the hidden photon may then mix with ours is [kinetic mixing between sectors](kinetic-mixing.md).

The manuscript described the sector with ordinary physics throughout. [#14 §1](../../../../notes/knot-dark-matter-standalone.md#1-framework): "Throughout, the hidden sector is described by ordinary relativistic quantum field theory. Whether the parent framework requires a different kinematics for momentum-polarized matter is an open question that this proposal does not use." The worklog's item O3 had found that #14 and the [conjugate-relativity](../../../conjugate-relativity/_index.md) paper [#13](../../../papers/conjugate-special-relativity.md) were never reconciled on this ([conflicts between sources](../../../history/documents/source-conflicts.md#conjugate-relativity)), and that #13 itself has "two different dual cones" ([the two dual cones](../../../conjugate-relativity/two-cones-inconsistency.md)); v3's decision was to "keep the dark sector in ordinary kinematics and say so explicitly". [#11](../../../papers/broken-born-checkpoint-v2.md) draws the consequence for the candidate the sector served: #14 "did not model the localization in momentum that v2.0 claimed" (§12), so that candidate is untested and is P.R.'s open conjecture ([Conjecture: magnetic monopoles abundant in momentum space](../momentum-space-monopoles.md)).

## How it got its content

### v2 named no group

v2 of #14 required only that "the dual sector contains a gauge group G broken to a subgroup H with pi_2(G/H) nonzero", supporting "monopole-class defects classified by pi_2, not knot solitons in the pi_3/Hopfion sense", and listed "the existence and group theory of the dual gauge sector" as conjectural ([`review/skeptic-review-console.html`](../../../../review/skeptic-review-console.html), which embeds v2). Round 2 asked for more: "name an explicit candidate group (dual SU(2)→U(1) suffices)" ([`HANDOFF.md` §6](../../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); [review rounds 1 and 2](../../../method/review/rounds-one-and-two.md)).

### The worklog's answer and its correction

The worklog's item R6 answered: "SU(2) → U(1) by an adjoint Higgs; π₂(SU(2)/U(1)) = ℤ ['t Hooft 1974; Polyakov 1974]. Hiramatsu et al. (JHEP 12 (2021) 122) study exactly this case with kinetic mixing." ([`review/v3-worklog.md`](../../../../review/v3-worklog.md), 'Round-2 pending list').

Its item O1 then computed what that minimal sector does in the early universe ('New open items'). With only the adjoint scalar, "W′± is the lightest dark-charged state, so it is stable", and because the monopoles need a hot hidden plasma to form, the W′± were thermal; their [relic density](../relic-abundance.md) exceeds the observed dark matter many times over. "The minimal model is excluded." The fix: "at least one light dark-charged fermion (a dark doublet) for W′± to decay into", and "R6 becomes "SU(2)_d → U(1)_d with at least one light dark doublet"." The surviving form of that result is [W′ overclosure: the minimal sector is excluded](w-prime-overclosure.md).

### v3

v3 recorded the result and the fix: "A negative result: the minimal model fails." and "The fix is the Dirac doublet psi: W'+ can decay to a psi pair." ([#14 §3](../../../../notes/knot-dark-matter-standalone.md#3-the-candidate)). ψ then became a relic of its own, with a mass window that round 3 overturned ([the ψ relic window](psi-relic-window.md)), and with ψ included the hidden sector's dark radiation required it to be [colder than ours](../../../cosmology/early-universe/hidden-sector-temperature.md), ξ < 0.77 in v3 ([the hidden sector's thermal history](hidden-thermal-history.md)). [#14 §6](../../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) lists among its "Requirements forced by consistency (not optional)": "(i) at least one hidden doublet fermion with mass between the MeV scale and ~0.1 TeV" and "(iii) an unbroken U(1)_d".

## How it was tested

Round 3's referee audited the proposal without access to the program ([review round 3](../../../method/review/round-3/_index.md)). Its conceptual audit asked whether the phase-space framework does any work, and answered no ([`review/round3/referee/audit-notes.md`](../../../../review/round3/referee/audit-notes.md), Step 4(d)):

> the hidden-sector content, sector separation, xi and m_psi are all postulated; Sec. 1 "Kinematics" says the hidden sector is ordinary relativistic QFT. The DM proposal is the standard hidden 't Hooft-Polyakov-monopole scenario (Baek-Ko-Park 2013; Khoze-Ro 2014; Murayama-Shu 2009; LMW 2026) with one coupling choice (alpha_d = alpha), and it stands or falls on that literature, independently of Born reciprocity.

QFT is quantum field theory, DM is dark matter, and LMW is Liveoak–Maharana–Wells. The referee listed Baek–Ko–Park and Khoze–Ro, "both: hidden SU(2)->U(1) monopoles + W' + dark photon", as uncited prior art (Step 4(c) item 10; [topological dark matter in the literature](prior-art.md)). The [pre-registration](../../../method/review/round-3/preregistration.md) had predicted the same weakness: "The candidate in §2–§4 is a standard hidden-sector monopole model."

The adjudication also accepted, as a to-do not individually re-checked, the referee's list of constraints the sector was never tested against: re-thermalization by ψ, limits on millicharged particles from supernova 1987A and from [nucleosynthesis](../../../cosmology/early-universe/big-bang-nucleosynthesis.md#nucleosynthesis-limits-on-a-millicharged-ψ), charged-subcomponent and cosmic-microwave-background bounds, dark acoustic oscillations, the Higgs portal, the [reheating](../../../cosmology/early-universe/inflation-and-dilution.md) mechanism for the temperature ratio, and collective magnetic-plasma effects ('Rulings', [omitted constraints](../../../method/review/round-3/rulings.md#omitted-constraints)). Strict sector separation (Decision 1) later closed the channels that depend on mixing; the rest were not pursued after #14's model was retired.

## The evidence against it as the program's proposal

The sector was not refuted. Its physics is the standard physics above, and its minimal form was excluded by the worklog's calculation (item O1). What the evidence weighs against is the claim that the program had selected it. Round-3 Decision 2, on the low-scale version of the same model: "Route (a), v ≲ 100 PeV, works, but it is Murayama–Shu's and Liveoak–Maharana–Wells's model. Nothing in it depends on Born reciprocity (the referee and the pre-registration agree), so claiming it would add no testable content and would misattribute it." The superheavy version failed on its abundance ([Obituary: #14's superheavy-soliton model](obituary.md)). #14 had said so: its charge-lattice motivation for the sector was used "only as motivation", and "No numerical result below depends on it" ([#14 §2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling)). This is the soliton episode's instance of [the 'framework does no work' critique](../../../program/framework-does-no-work.md).

## What stands

- **The exclusion of the minimal sector.** [#11](../../../history/documents/checkpoint.md) [§12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model): "The minimal adjoint-only SU(2) → U(1) hidden sector is excluded on its own terms: its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V]." The adjudication lists the same: "The statement that the minimal adjoint-only sector is excluded." The same exclusion is published for the minimal 't Hooft–Polyakov model, in a paper posted before #14 v3's calculation: "dark monopoles cannot constitute a sizeable fraction of dark matter" ([Brümmer, Ferrante, Fischer and Frigerio 2026](https://arxiv.org/abs/2509.21924) [S]; flag 68, pending). See [W′ overclosure](w-prime-overclosure.md#in-the-literature).
- **The Dirac relation.** "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]" ([#11 §12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model)).
- **The mixing literature.** "The kinetic-mixing literature points (a) and (c)" (adjudication, 'What survives v3'): mixing induced by gravity alone is tiny or absent, and while U(1)_d is unbroken a hidden monopole induces no visible magnetic flux ([kinetic mixing between sectors](kinetic-mixing.md)).
- **The monopole physics.** 't Hooft–Polyakov monopoles, their topology and their mass formula are established ([magnetic monopoles](../../../electric-magnetic-duality/monopoles/_index.md)).

## Sources

- [`CLAUDE.md`](../../../../CLAUDE.md) 'Since the handoff' — the hidden SU(2) → U(1) sector under review
- [`review/round3-adjudication.md`](../../../../review/round3-adjudication.md) 'Decisions' 2 — the retirement, which covers #14's model, and the misattribution argument; 'What survives v3' — the minimal-sector exclusion and the mixing points; 'Rulings' — the omitted constraints
- [`wiki/papers/broken-born-checkpoint-v2.md` §12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) — the survivors, with tags, and the localization in momentum #14 did not model; [§4](../../../../notes/knot-dark-matter-standalone.md#4-observational-consistency) — P4
- [`verify/soliton_obituary.py`](../../../../verify/soliton_obituary.py) — the gated minimal-sector exclusion
- [`review/round3/referee/audit-notes.md`](../../../../review/round3/referee/audit-notes.md) Step 4(d) — "the standard hidden 't Hooft-Polyakov-monopole scenario"; Step 4(c) item 10 — the uncited prior art
- [`review/round3-preregistration.md`](../../../../review/round3-preregistration.md) 'Predictions' — the expected weakness
- [`review/v3-worklog.md`](../../../../review/v3-worklog.md) 'Round-2 pending list' (R6), 'New open items' (O1, O3), 'v3 as drafted (2026-10-19)' — how the content was chosen and corrected
- [`notes/knot-dark-matter-standalone.md` §1](../../../../notes/knot-dark-matter-standalone.md#1-framework) — the ordinary kinematics; [§2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling) — the sector, the mirror-Standard-Model argument, sector separation; [§3](../../../../notes/knot-dark-matter-standalone.md#3-the-candidate) — the monopoles and the minimal model's failure; [§6](../../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) — "Conjectural" and the requirements
- [`review/skeptic-review-console.html`](../../../../review/skeptic-review-console.html) — v2's unnamed group
- [`HANDOFF.md` §6](../../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — round 2's request for an explicit group
- [`notes/literature-check.md` §4](../../../../notes/literature-check.md#4-monopoles-in-momentum-space-c2-and-the-null-result-c3-not-found); [`review/wiki-build-flags.md`](../../../../review/wiki-build-flags.md) item 68 — the minimal sector's exclusion, published by Brümmer et al.; pending
