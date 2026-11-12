---
title: "Under review: the coupling α_d ≈ 34"
weight: 40
status: under-review
description: "Three attempts to fix the hidden monopoles' coupling — Dirac quantization against our photon (in the handoff, round 1's 'valid kill') and hypothesis H, both under review, and reciprocity acting as modular S (called numerology in round 2; part of P.R.'s open magnetic-mirror conjecture) — F2's finding on which coupling sets the soliton mass, and the factor-of-four convention spread."
sources:
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "review/skeptic-review-console.html"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md Abstract"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3/referee/step2a.out"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/round3-adjudication.md 'Rulings' 12"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "wiki/papers/broken-born-checkpoint-v2.md §11"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "CLAUDE.md 'Since the handoff'"
  - "verify/soliton_obituary.py"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
  - "review/wiki-build-flags.md item 28"
  - "review/wiki-build-flags.md item 60"
---

*α_d ≈ 34 was the strength [#14](../../../../notes/knot-dark-matter-standalone.md)'s soliton model assigned to the interaction between its hidden [monopoles](../../../electric-magnetic-duality/monopoles/_index.md): 1/(4α), the reciprocal of four times the fine-structure constant α ≈ 1/137 of ordinary electromagnetism. The program tried three ways to fix that value. The first applied Dirac's charge-quantization condition using our photon's charge, which contradicted the claim that the monopoles do not couple to our photon. The second had [Born reciprocity](../../../phase-space/reciprocity/born-reciprocity.md) act on gauge couplings as the [modular S transformation](../../../electric-magnetic-duality/modular-group.md#the-generators-s-and-t) of [electric–magnetic duality](../../../electric-magnetic-duality/_index.md); a referee called it numerology. The identification it rested on, the momentum-polarized sector as the image of ours under the exchange of electric and magnetic charge, is one form of P.R.'s open [magnetic-mirror conjecture](../../../electric-magnetic-duality/magnetic-identification.md), that each electrically charged particle has a magnetically charged analog in the momentum-polarized sector. The third assumed that the smallest hidden charge equals the electron's; it was motivated but not derived. The number itself shifts by a factor of four with the convention used. What stands is a general fact: a weakly coupled force always has strongly coupled monopoles.*

**Status:** Under review — the evidence below weighs against it, and its final status awaits review. This covers the first form, "α_d ≈ 34 via our photon" (root [`CLAUDE.md`](../../../../CLAUDE.md), 'Since the handoff'), and hypothesis H, the third, which is under review with that coupling ([hypothesis H](#hypothesis-h)); the second is part of an open conjecture. Round 1 found the first inconsistent ([the handoff](../../../history/documents/handoff.md) calls it the "round-1 reviewer's valid kill"); H was part of #14 v3, which was withdrawn on 2026-10-19 (round-3 Decision 2; [round-3 decisions](../../../method/review/round-3/decisions.md)). The second is the separate-photon form of P.R.'s magnetic-mirror conjecture [O] ([#11 §11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)), which is #14 v2's form: the p-polarized sector's own gauge field has a coupling that is "the S-image of ours", and whether that is the sector's elementary coupling or its magnetic one is open ([Conjecture: the momentum sector as the magnetic mirror](../../../electric-magnetic-duality/magnetic-identification.md#separate-photon)). It is folded below as a conjecture. The decision to adopt the reading proposed in the v3 worklog's item F2 is withdrawn, F2's finding stands ([below](#superseded-f2-which-coupling-sets-the-soliton-mass); flag 60 in [`review/wiki-build-flags.md`](../../../../review/wiki-build-flags.md)), and #14 is withdrawn. The round-3 referee confirmed the arithmetic of hypothesis H with executed code; the convention spread is marked [V] in the v3 worklog, and the current gate, [`verify/soliton_obituary.py`](../../../../verify/soliton_obituary.py), does not re-check it. The surviving Dirac relation is [T]. Home section: [#14's soliton model](_index.md); listed in [claims under review](../../../status/under-review.md).

## The couplings and Dirac's condition

### Electric and magnetic couplings [T]

A gauge force's strength is measured by a dimensionless coupling, α = q²/4π for a charge q in units with ħ = c = 1; for ordinary electromagnetism α ≈ 1/137, the fine-structure constant [T]. A magnetic charge g has a magnetic coupling g²/4π in the same way. Dirac showed that if a magnetic monopole and an electric charge exist in the same gauge theory, quantum mechanics requires their charges to satisfy q·g = 2πn for an integer n, in the normalization the program's documents use ([Dirac quantization and the DSZ pairing](../../../electric-magnetic-duality/monopoles/dirac-quantization.md)) [T]. The smallest electric charge therefore fixes the smallest magnetic charge, and a small electric charge forces a large magnetic one.

### The relation in #14

#14 v3 applied this inside its [hidden sector](hidden-sector.md) ([§2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling), "Coupling."):

> The hidden sector is weakly coupled in its electric description, with alpha_W' = g_d^2/4pi. Its monopoles carry magnetic charge g_m = 4 pi/g_d, the Dirac minimum relative to psi's charge g_d/2, so their mutual coupling is alpha_m = g_m^2/4pi = 1/alpha_W' [7]. Any weakly coupled hidden sector therefore has strongly coupled monopoles: the strong magnetic coupling is generic, not a hypothesis.

Here g_d is the gauge coupling of the hidden SU(2)_d, α_W′ the coupling of its heavy charged vector bosons W′±, and ψ the light hidden fermion, whose charge g_d/2 is the smallest hidden charge ([the hidden SU(2) → U(1) proposal](hidden-sector.md)). With q = g_d/2 and n = 1, Dirac's condition gives g_m = 4π/g_d, and then α_m = (4π/g_d)²/4π = 4π/g_d² = 1/α_W′. The product α_m·α_W′ = 1 holds whatever g_d is; the referee's script checks it, "check alpha_m * alpha_W' = 1.000000 (should be 1)" ([`review/round3/referee/step2a.out`](../../../../review/round3/referee/step2a.out)). The question the three attempts below tried to answer is which value g_d takes.

The monopoles' coupling has carried several names: α_d in the handoff and v2, α_m in v3, and α_d again in the worklog's F2 (where α_e,d denotes the hidden electric coupling). On this page α_d ≈ 34 means the monopoles' mutual coupling.

## Attempt 1: Dirac quantization against our photon

The first version of #14 fixed the hidden monopoles' coupling with Dirac's condition applied to our electron's charge. The handoff lists the result among its failed claims ([`HANDOFF.md` §2](../../../../HANDOFF.md#2-scientific-state-one-screen)):

> α_d ≈ 34 via Dirac quantization against our photon (round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon).

The DSZ (Dirac–Schwinger–Zwanziger) lattice is the lattice of electric and magnetic charges of one gauge theory, on which Dirac's condition holds pairwise ([the symplectic charge lattice](../../../electric-magnetic-duality/symplectic-charge-lattice.md)). Dirac's argument applies only to charges that couple to the same gauge field. Quantizing the monopoles' charge against the electron's therefore makes them magnetic charges of our electromagnetism, which contradicts the candidate's defining claim that they are dark because they do not couple to our photon. Round 1 found the contradiction and the handoff calls it valid (§6). v3 later stated the opposite explicitly: "nothing is quantized against our gauge field" ([#14 §2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling), "What is not asserted.").

## Conjecture: reciprocity acting as modular S

This form is the separate-photon form of P.R.'s magnetic-mirror conjecture, open [O] ([#11 §11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23); [below](#the-separate-photon-form)). Within #14, hypothesis H took its place.

v2 replaced the Dirac argument with a conjecture. The handoff: "Restated in v2 as reciprocity-acts-as-modular-S on the coupling — explicitly the load-bearing conjecture; without it α_d is a free strong coupling" (§2).

### The conjecture as v2 stated it

Electric–magnetic duality exchanges a theory's electric and magnetic descriptions. Its generator S acts on the complexified coupling τ_c by τ_c → −1/τ_c, and [#11](../../../history/documents/checkpoint.md) [§11.3](../../../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) notes that S is generated by the same matrix [[0,1],[−1,0]] as Born's ρ and the program's [inversion Z → −Z⁻¹](../../../phase-space/modular-field/modular-inversion.md) [T] ([S-duality and Montonen–Olive](../../../electric-magnetic-duality/s-duality.md)). v2 conjectured that the two dualities are the same event. Its §2, embedded verbatim in [`review/skeptic-review-console.html`](../../../../review/skeptic-review-console.html):

> Conjecture (the identification). The two polarization choices are made by the same vacuum event, and the momentum-polarized matter sector is the S-dual image of the electric sector: a distinct gauge structure whose complexified coupling is fixed by the reciprocity map, acting as the modular S transformation, to the image of ours - alpha_d = 1/(4 alpha) ~ 34, quoted in the Dirac normalization (the Schwinger convention shifts this by the standard factor of four).

v2 stated the stakes: "This identification is the manuscript's load-bearing conjecture: if reciprocity does not act on gauge couplings as S, the value alpha_d ~ 34 loses its derivation and becomes a free parameter (the candidate survives, but loses predictivity)."

### Round 2's verdict

Round 2 graded v2 "B near B/C / medium" with "weakest link = the α_d derivation ("matrix coincidence ≠ physical identity" / "numerology")" ([`HANDOFF.md` §6](../../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); [review rounds 1 and 2](../../../method/review/rounds-one-and-two.md)). That two dualities are represented by the same matrix does not show that one acts on the other's coupling. Round 2 also raised the exactness burden, which the worklog answered as item R1: "Exact S-duality has been tested only in N=4 SYM and special finite N=2 theories. For non-SUSY theories there is "no reason to think" it survives quantum corrections, and the bosonic spectrum mismatches (W spin 1, monopole spin 0). That is an expectation, not a no-go" ([`review/v3-worklog.md`](../../../../review/v3-worklog.md), 'Round-2 pending list'). SYM is super Yang–Mills, and SUSY is supersymmetry.

### Why it was set aside

The worklog's finding [F2](#superseded-f2-which-coupling-sets-the-soliton-mass) showed that v2 used both a weak and a strong value of the dual coupling, and it proposed a reading in which α_d ≈ 34 "does not need S acting on our coupling" ([`review/v3-worklog.md`](../../../../review/v3-worklog.md), 'Findings neither referee raised'). #14 v3 adopted that reading and did not use S-duality to fix α_d. The decision to adopt it is withdrawn, and the finding stands ([#11 §11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23); flag 60). v3 kept the charge-lattice correspondence only "as motivation" and added that "Exact electric-magnetic duality is also not assumed" ([#14 §2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling)). No [round-3 ruling](../../../method/review/round-3/rulings.md) addresses the conjecture.

### The separate-photon form

[#11 §11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) states P.R.'s magnetic-mirror conjecture [O]: "momentum matter is similar to position matter, each electrically charged x-polarized particle having a magnetically charged p-polarized analog". x-polarized matter is ours, made of fields local in position, and p-polarized matter is the conjugate sector's, local in momentum ([P4: polarized matter and strict sector separation](../../../program/postulates/p4-polarized-matter.md)). #11 places v2's conjecture beside it: "#14 v2 stated a related identification, "the momentum-polarized matter sector is the S-dual image of the electric sector", with reciprocity acting on gauge couplings as S; it called that identification load-bearing for its dual coupling α_d, and a full mirror spectrum appeared there only as something the sector "may carry"." It adds that "F2's finding, that #14 v2 used both a weak and a strong value of the dual coupling, stands", and #14 is withdrawn (§12; [F2](#superseded-f2-which-coupling-sets-the-soliton-mass)).

v2's form is the conjecture's separate-photon form: "The analogs are magnetic under the p-polarized sector's own gauge field, whose coupling is the S-image of ours. Whether that is the sector's elementary coupling or its magnetic one is open; F2's finding is that the choice decides whether the sector's solitons are heavy. This form is consistent with P4 and leaves the absence of our own monopoles to §11.1" (§11.4). Round 2's objections stay open. Among what stays open in either form, #11 lists "the round-2 objection that a shared matrix is not a shared physics ("matrix coincidence ≠ physical identity")" and "round 2's burden that exact S-duality is established only with extended supersymmetry, so either reciprocity supplies the rigidity or the dual sector is approximately supersymmetric" ([round 2's verdict](#round-2s-verdict)), together with the factor-of-four spread of the dual coupling ([below](#superseded-the-convention-and-running-spread)). The worklog ties the burden's size to whether S carries α_d: "If F2 is adopted, S no longer carries α_d, and the burden shrinks to the §2 "full mirror spectrum" remark" ([`review/v3-worklog.md`](../../../../review/v3-worklog.md), 'Round-2 pending list', R1). In the separate-photon form the sector's coupling is the S-image of ours (§11.4), and the root [`CLAUDE.md`](../../../../CLAUDE.md) lists among that form's open items the burden, "which returns with the withdrawal of F2's decision" ('Open from the monopole discussion'). The conjecture, its two forms and what it needs are on [Conjecture: the momentum sector as the magnetic mirror](../../../electric-magnetic-duality/magnetic-identification.md).

## Superseded: F2, which coupling sets the soliton mass

The worklog found an inconsistency in v2 that neither referee had raised ([`review/v3-worklog.md`](../../../../review/v3-worklog.md), 'Findings neither referee raised', F2, tagged [D, numbers V]):

> v2 writes M ~ (4π/e_d²) Λ_c ~ 100 Λ_c. That factor is ~137 only if e_d²/4π ≈ 1/137. With e_d²/4π = α_d = 34 it is 0.029, so the solitons would not be heavy. v2 uses the weak value in §3 and the strong value in §2 and §4.

A soliton's mass is the symmetry-breaking scale enhanced by the inverse of the elementary coupling [T] ([the 't Hooft–Polyakov monopole](../../../electric-magnetic-duality/monopoles/thooft-polyakov-monopole.md)), so a heavy soliton needs a weak elementary coupling. v2 had used one number for two different couplings. The worklog's resolution:

- "the dual sector's elementary coupling α_e,d is weak, its solitons are heavy (M ≈ Λ_c/α_e,d), and the solitons themselves are strongly coupled (α_m ≈ 1/(4α_e,d) or 1/α_e,d)";
- "Then α_d ≈ 34 follows from α_e,d ≈ α, a mirror-coupling equality, and does not need S acting on our coupling."

#14 v3 adopted the reading: "the load-bearing conjecture becomes α_e,d = α (or α_e,d free and weak), and S-duality is no longer what fixes α_d." That equality became hypothesis H. The decision to adopt the reading is withdrawn ([`review/v3-worklog.md`](../../../../review/v3-worklog.md), F2; [#11 §11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)).

F2's finding is not refuted, and it stands: v2 used both a weak and a strong value of the dual coupling, and the choice decides whether the solitons are heavy ([#11 §11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)). In the separate-photon form of P.R.'s magnetic-mirror conjecture the coupling of the p-polarized sector's own gauge field is the S-image of ours, and which coupling that is, the sector's elementary one or its magnetic one, is open ([§11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23); [the separate-photon form](#the-separate-photon-form)). #14 is withdrawn.

## Attempt 3: hypothesis H

### The statement

#14 v3 §2:

> The proposal's single coupling hypothesis (H): the smallest hidden charge equals ours, (g_d/2)^2/4pi = alpha. The motivation is that reciprocity exchanges the two polarizations; if it acts on gauge couplings at all, the minimal action is to equate the elementary charges of the two sectors. Under H, alpha_W' = 4 alpha ~ 1/34 and alpha_m = 1/(4 alpha) ~ 34.

The arithmetic follows from the Dirac relation above: if (g_d/2)²/4π = α, then α_W′ = g_d²/4π = 4α, and α_m = 1/α_W′ = 1/(4α). The worklog explains why H matches ψ's charge rather than the W′ charge: the light doublet "makes ψ's charge g_d/2 the smallest dark charge. H matches *that* charge to ours, so α_W′ = 4α ≈ 1/34 and the monopoles' coupling is α_m = 1/α_W′ = 1/(4α) ≈ 34 exactly, by Dirac quantization relative to ψ" ('v3 as drafted (2026-10-19)'). It also records a limit on what H can mean: an exact mirror copy of the Standard Model has no stable monopoles, "so H relates couplings only, not gauge groups". (H here is unrelated to the [generalized metric](../../../phase-space/born-geometry/born-structures.md) H of phase space.)

H fixed g_d, and through it the monopole mass M = 4πf v/g_d ≈ (21–37) v, the W′ mass g_d v, the ψ annihilation cross-section and the monopoles' self-interaction; the gate script still states it as part of the model it checks ("Dirac doublet psi of dark charge g_d/2 = e (hypothesis H)").

### What round 3 found

The referee confirmed the arithmetic with executed code: "alpha_W' under H | 4 alpha ~ 1/34 | 1/34.259 | CONFIRMED" and "alpha_m | ~34 | 34.259 | CONFIRMED" ([`review/round3/referee/audit-notes.md`](../../../../review/round3/referee/audit-notes.md), Step 2), with "gd = 0.60564" (`step2a.out`). It also found a variant the manuscript had not considered: matching ψ's charge to e/3, the smallest charge in the Standard Model, "gives alpha_m = 308 (step2a.out), and the framework gives no way to choose" (Step 4(d)).

The conceptual audit placed H at the centre of the referee's second finding, "the framework does no work": "hypothesis H is motivated, not derived (acceptance criterion 1 concedes this)", and "Even the one structural input H only sets M/v = 21-37 and alpha_m = 34" (Step 4(d); [the 'framework does no work' critique](../../../program/framework-does-no-work.md)). The [pre-registration](../../../method/review/round-3/preregistration.md) had expected this: "Hypothesis H's motivation ("the minimal action is to equate the elementary charges") is one sentence."

### Hypothesis H

[#14 §6](../../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) listed "hypothesis H" as "Conjectural", and its [acceptance criterion 1](../../../symmetry-breaking/toy-models/acceptance-criterion.md) asked for an action from which H could be derived: "deriving hypothesis H from that action would make the coupling a prediction". H was part of #14 v3, whose model failed in round 3 ([Obituary: #14's superheavy-soliton model](obituary.md)). H is absent from both lists of what survives, in [#11 §12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) and in the round-3 adjudication, and no ruling addresses it by itself. It is under review with the coupling.

## Superseded: the convention and running spread

Round 2 asked how much the number 34 depends on conventions. The worklog's item R2, "**adjudicated** [V]" ([`review/v3-worklog.md`](../../../../review/v3-worklog.md), 'Round-2 pending list'):

> Convention: 1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn). One-loop SM running of α_em gives 1/(4α_em) = 29.0 at 10¹¹, 28.8 at 3×10¹¹ and 27.3 at 10¹⁶ GeV. The referee's "toward ~6–8" is **not reproduced** for the electromagnetic coupling; 6–8 appears only for 1/(4α₃). The valid core stands: the number is convention-dependent by a factor of 4. v3: present α_d as free-but-strong.

SM is the Standard Model, and α₃ the strong-force coupling. The spread has two sources [T]. The first is normalization: whether Dirac's condition is written q·g = 2πn or 4πn changes the minimal magnetic charge by a factor of two and the coupling by four. The referee also flagged it in #14's citation of Zwanziger, whose abstract "states e_m g_n - g_m e_n in 4 pi Z; manuscript writes 2 pi Z (Dirac normalization). The 't Hooft-Polyakov monopole with doublets realises 2 pi, so the physics is fine" (Step 1; [ruling 12](../../../method/review/round-3/rulings.md#ruling-12-minor-citation-issues), accepted). The second is the energy scale: α grows slowly with energy, so matching the two sectors' charges at the transition scale rather than at low energy lowers 1/(4α).

v3 carried both into its text: "Matching the W' charge to ours instead of psi's gives alpha_m ~ 137. Matching at 1e12 GeV instead of at low energy gives about 29, from one-loop Standard Model running of alpha." The referee confirmed both: "137.036" for the W′-charge variant, and "28.61 (MSbar 127.930), 28.86 (128.95)" for running to 10¹² GeV (Step 2). The drafting check had corrected the second figure before v3 was written: "the coupling matched at 10¹² GeV is ≈ 29 (not 28)" (worklog, 'v3 as drafted (2026-10-19)').

Within #14 the spread is that of a number with no role there: without H, nothing in #14 fixes α_d. The spread is an open item of P.R.'s magnetic-mirror conjecture, whose separate-photon form takes the dual coupling to be the S-image of ours: [#11 §11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) lists "the dual coupling's factor-of-4 convention spread, 1/(4α) or 1/α ([`review/v3-worklog.md`](../../../../review/v3-worklog.md) R2 [V]; the formula printed beside 34 in §11.2 is flag 28)" among what stays open in either form ([what it needs](../../../electric-magnetic-duality/magnetic-identification.md#what-it-needs)).

## What stands

The general relation survives #14's model. [#11 §12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates), under "What survives": "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]." In #14's words, "the strong magnetic coupling is generic, not a hypothesis." The first and third attempts to fix the value 34 for a hidden sector, Dirac quantization against our photon and hypothesis H, are under review ([attempt 1](#attempt-1-dirac-quantization-against-our-photon); [hypothesis H](#hypothesis-h)). The second, reciprocity acting as modular S, is the separate-photon form of P.R.'s open magnetic-mirror conjecture ([above](#conjecture-reciprocity-acting-as-modular-s)). Two things about the value stay open there: whether the S-image of our coupling is the sector's elementary coupling or its magnetic one, and the factor-of-four convention, 1/(4α) or 1/α ([#11 §11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23); [the convention and running spread](#superseded-the-convention-and-running-spread)).

For ordinary electromagnetism the same arithmetic is established physics and untouched. [#11 §11.2](../../../papers/broken-born-checkpoint-v2.md#112-the-full-dual-spectrum-t) [T]: "Dirac's condition e·g ~ 2π pins the magnetic coupling near 4π/e² ≈ 34 — the magnetic world is our strong-coupling mirror, heavy and bound" ([the magnetic mirror-family](../../../electric-magnetic-duality/magnetic-mirror-family.md)). That value concerns the magnetic charges of our own electromagnetism, not a hidden sector. Flag 28 in [`review/wiki-build-flags.md`](../../../../review/wiki-build-flags.md) finds the number right and the formula beside it suspect: with α = e²/4π, 4π/e² is 1/α, while a coupling near 34 is 1/(4α), as in the Dirac relation above.

The [popular article](../../../history/documents/popular-articles.md) [#12](../../../../popsci/universes-other-half.md) uses the same comparison, "about 34, against our 1/137", for the claim that the momentum-polarized sector is "the magnetic side of electromagnetism". #11 records that reading as the shared-photon form of P.R.'s magnetic-mirror conjecture, open, in which the analogs "carry magnetic charge of our photon" ([§11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23); [Conjecture: the momentum sector as the magnetic mirror](../../../electric-magnetic-duality/magnetic-identification.md#shared-photon)). That reading does not repeat the first attempt, which took Dirac's condition against our photon while denying the coupling to it: a separate photon, as in #14 v2 and v3, and an accepted coupling, as in #12, are the two ways out of that inconsistency (flag 60). #12 is never a source for a claim's status.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — what survives; [§11.2](../../../papers/broken-born-checkpoint-v2.md#112-the-full-dual-spectrum-t) — the ordinary-electromagnetism statement; [§11.3](../../../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) — the shared matrix; [§11.4](../../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) — P.R.'s magnetic-mirror conjecture [O], its two forms, what stays open in either, and F2's finding
- [`CLAUDE.md`](../../../../CLAUDE.md) 'Since the handoff' — the conjecture and F2's finding; "α_d ≈ 34 via our photon" under review, and hypothesis H "under review with that coupling"; 'Open from the monopole discussion' — the supersymmetry burden among the separate-photon form's open items
- [`HANDOFF.md` §2](../../../../HANDOFF.md#2-scientific-state-one-screen) — the first two attempts; [§6](../../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — round 1's finding and round 2's verdict
- [`review/v3-worklog.md`](../../../../review/v3-worklog.md) 'Round-2 pending list' (R1, R2), 'Findings neither referee raised' (F2), 'v3 as drafted (2026-10-19)' — the exactness burden, the convention spread, the mass argument, the withdrawn decision and the finding that stands, and how H was matched
- [`review/wiki-build-flags.md`](../../../../review/wiki-build-flags.md) item 60 — F2's finding, and the two ways out of round 1's inconsistency
- [`notes/knot-dark-matter-standalone.md` §2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling) — the Dirac relation, hypothesis H, "What is not asserted"; [§6](../../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) — H as "Conjectural" and acceptance criterion 1; Abstract — the coupling as v3 states it
- [`review/round3/referee/audit-notes.md`](../../../../review/round3/referee/audit-notes.md) Step 1 — the 2π versus 4π normalization; Step 2 — the confirmed arithmetic and variants; Step 4(d) — the e/3 variant and "motivated, not derived"
- [`review/round3/referee/step2a.out`](../../../../review/round3/referee/step2a.out) — the referee's printed couplings
- [`review/round3-preregistration.md`](../../../../review/round3-preregistration.md) 'Predictions' — H's one-sentence motivation
- [`review/round3-adjudication.md`](../../../../review/round3-adjudication.md) 'Rulings' 12 — the normalization accepted; 'Decisions' 2 — covers #14's model, which used ordinary kinematics
- [`verify/soliton_obituary.py`](../../../../verify/soliton_obituary.py) — H as part of the checked model
- [`review/skeptic-review-console.html`](../../../../review/skeptic-review-console.html) — #14 v2's modular-S conjecture, verbatim
- [`popsci/universes-other-half.md`](../../../../popsci/universes-other-half.md) 'Dark matter as the other polarization' — the popular echo, the shared-photon reading (never a status source)
- [`review/wiki-build-flags.md`](../../../../review/wiki-build-flags.md) item 28 — the formula [#11 §11.2](../../../papers/broken-born-checkpoint-v2.md#112-the-full-dual-spectrum-t) writes beside the value 34
