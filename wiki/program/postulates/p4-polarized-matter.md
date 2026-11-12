---
title: "P4: polarized matter and strict sector separation"
weight: 60
status: alive
description: "The Standard Model is x-polarized and conjugate matter χ is p-polarized; both couple universally to H and no gauge force crosses polarizations, taken strictly (gravity-induced mixing ε ≲ 10⁻¹³)."
provenance: [P]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 7"
  - "wiki/papers/broken-born-checkpoint-v2.md §14"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Rulings' 7, 9"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/v3-worklog.md 'Round-2 pending list' R4"
  - "notes/knot-dark-matter-standalone.md §2"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-program-v1.md §2"
  - "notes/geometric-core.md §E"
  - "wiki/papers/reciprocity-toy-models.md §5"
  - "wiki/papers/reciprocity-toy-models.md §6"
  - "review/round4-adjudication.md 'Rulings' F3, F5"
  - "verify/toy_s5.py part C"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §3"
  - "review/wiki-build-flags.md item 60"
  - "review/wiki-build-flags.md item 62"
  - "review/wiki-build-flags.md item 63"
---

*P4 is the program's axiom about matter. Ordinary matter, the Standard Model, is x-polarized: its fields are organized around position, the variable in which its interactions are local. A second kind, conjugate matter χ, is p-polarized, organized around momentum. Both kinds respond to the same gravity, so the [equivalence principle](../../gravity/spin-2-fields/equivalence-principle.md) holds across them, but no gauge force (the electromagnetic, weak or strong interaction) acts between them. The [checkpoint](../../history/documents/checkpoint.md) reads the last clause strictly: the only mixing allowed between the two sectors is what gravity itself induces, which is zero or extremely small. P4 is the basis of the program's prediction that dark-matter direct-detection experiments will see nothing, and in the toy models it is also what gives the vacuum's choice of polarization a physical effect. One form of P.R.'s open [magnetic-mirror conjecture](../../electric-magnetic-duality/magnetic-identification.md), in which the momentum sector carries magnetic charge of our own photon, would need P4 restated.*

**Status:** Alive — [P]; the gravity-only bound it quotes is from the literature [27S] — the strict reading is in force by decision (round-3 Decision 1, 2026-10-19), not by derivation.

## Statement

```text
P4  Matter comes in x-polarized (Standard Model) and p-polarized (χ)
    representations; both couple universally to H; gauge forces do not
    cross polarizations. [P; taken strictly since v2.1: no kinetic mixing
    between the sectors beyond what gravity induces, which vanishes if
    hidden charge conjugation is exact and otherwise first appears at
    six loops, ε ≲ 10⁻¹³ [27S].]
```

This is [#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)'s text. The [lab notebook](../../history/documents/lab-notebook.md)'s version spells out what universal coupling means:

> **P4 (Polarized matter, universal gravity).** Matter comes in two representations: x-polarized fields (the Standard Model) and p-polarized fields (χ, conjugate matter). Both couple universally to H — the equivalence principle holds across polarizations. Gauge interactions do not connect the two representations. **[P]** ([#1 §1](../../../notes/broken-born-theory.md#1-postulates))

The program paper v1 states the first three clauses as #11 does, without the strict-reading bracket ([#9 §2](../../../notes/broken-born-program-v1.md#2-postulates--including-the-one-the-mathematics-rejected)); kinetic mixing appears nowhere in it. The axiom makes three claims, taken in turn below: two kinds of matter, one gravity for both, and no gauge force between them.

## Two polarizations of matter

A polarization is a choice of which half of the phase-space directions count as position: a Lagrangian subspace for the [symplectic form](../../phase-space/reciprocity/symplectic-form.md) ω ([Lagrangian polarizations](../../phase-space/reciprocity/lagrangian-polarizations.md)). An x-polarized field is written as a function of position, and its interactions are local in x, as the known interactions are ("x-local interactions", [#11 §3](../../papers/broken-born-checkpoint-v2.md#3-the-question)). A p-polarized field is written as a function of momentum, and its interactions are local in p. The two descriptions are related as a waveform and its spectrum are related by the [Fourier transform](../../phase-space/reciprocity/fourier-transform.md), which implements the Born rotation ρ ([Born reciprocity](../../phase-space/reciprocity/born-reciprocity.md)). The [toy-model](../../symmetry-breaking/toy-models/_index.md) worklog puts the pair in exactly these terms: "x-polarized matter, and its ρ-image, p-polarized matter" ('Chunk 4').

- **The x-polarized sector** is the Standard Model. In the lab notebook's action it is untouched: "S_x is the Standard Model minimally coupled to g. Nothing is modified. **[P4]**" ([#1 §3](../../../notes/broken-born-theory.md#3-action)), where g is the spacetime metric.
- **The p-polarized sector** is conjugate matter χ ([conjugate matter and the velocity gate](../../dark-matter/conjugate-matter/_index.md)). In the current program χ is one of the three [dark-matter candidates](../../dark-matter/candidates/_index.md) of [#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates), "p-polarized matter field" in its table ([the χ-particle candidate](../../dark-matter/candidates/chi-particles.md)); the third, P.R.'s conjecture, is "magnetically charged topological solitons of the p-polarized sector, localized in momentum" ([Conjecture: magnetic monopoles abundant in momentum space](../../dark-matter/candidates/momentum-space-monopoles.md)). χ's distinctive property is a self-interaction that depends on relative momentum, the [velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md).

## One gravity for both

"Both couple universally to H" is the [equivalence principle](../../gravity/spin-2-fields/equivalence-principle.md) extended across the two polarizations: H is the [generalized metric](../../phase-space/born-geometry/born-structures.md) of [P1](p1-arena.md), which contains the spacetime metric g, and both kinds of matter couple to it in the same way. The lab notebook draws the observational consequence: "χ couples to g universally: it falls, orbits, and lenses like ordinary dark matter. Bullet Cluster lensing-centroid behavior is automatic" [D] ([#1 §4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured)). [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) keeps it: "χ propagates on g (equivalence principle; Bullet-Cluster-safe)" ([the Bullet Cluster](../../dark-matter/halo-astrophysics/bullet-cluster.md)).

In the record, universal coupling to H also supplies the gate's mechanism. The [field-equation note](../../history/documents/field-equation-notes.md): "Conjugate matter couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃". Exchange of the [momentum graviton](../../gravity/momentum-graviton/_index.md) X between two such bilinears "yields a four-point amplitude that depends on the **incoming relative momenta** of the pair — the variable no x-local mediator can produce" ([#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural); [dual stress](../../dark-matter/conjugate-matter/dual-stress.md); [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md)). [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that this exchange cannot produce the gate: with [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X every on-shell vertex depends only on the momentum transfer, and no χχX vertex or formula for T̃ exists in the record (§§2–3). Flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism ([exchanging X cannot produce the gate](../../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). And because everything couples to H, conjugate-sector objects gravitate even if nothing else of theirs is visible: "by P4, conjugate-sector solitons gravitate" ([#11 §11.1](../../papers/broken-born-checkpoint-v2.md#111-the-monopole-audit-revised-d); [conjugate monopoles as ontology](../../electric-magnetic-duality/conjugate-monopoles.md)).

## No gauge force between them

### Kinetic mixing

The third clause, "gauge forces do not cross polarizations", says that no particle feels both the Standard Model's forces and the conjugate sector's. Even without such particles, two sectors with separate abelian gauge forces can be linked by kinetic mixing: a term in the action that couples the field strength of our photon to that of another sector's photon, with a small coefficient ε [T] ([kinetic mixing between sectors](../../dark-matter/candidates/soliton-candidate/kinetic-mixing.md)). Its effect is that particles charged only under the other force acquire a small electric charge, of order ε times ours [T]. Mixing is therefore a channel through which matter that otherwise interacts with ours only through gravity becomes visible.

### The strict reading

#11 takes P4 to exclude kinetic mixing "beyond what gravity induces". The gravitational amount it gives, from Gherghetta, Kersten, Olive and Pospelov [27S], "vanishes if hidden charge conjugation is exact and otherwise first appears at six loops, ε ≲ 10⁻¹³" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)); hidden charge conjugation is the charge conjugation of the other sector. The round-3 referee checked the paper and quoted it (audit notes, Step 1):

- "If C_A and C_X are separately good symmetries ..., then kinetic mixing cannot be induced at any perturbative order" (p. 5), which is the source of the zero;
- "kinetic mixing through gravity alone, requires at least six loops and could be as large as ~1e-13" (abstract), conditional, in the referee's summary, "on C_X breaking and O(1) hidden Yukawa".

[`CLAUDE.md`](../../../CLAUDE.md) lists the reading among the changes since [the handoff](../../history/documents/handoff.md): "Strict sector separation (P4 at face value) is in force."

### Why it was adopted: round-3 Decision 1

The strict reading is a decision, not a derivation. It is the first of the decisions recorded on 2026-10-19, after the [round-3 review](../../method/review/round-3/_index.md) of [a withdrawn paper on monopole dark matter](../../../notes/knot-dark-matter-standalone.md) ([`review/round3-adjudication.md`](../../../review/round3-adjudication.md), 'Decisions'). It takes P4 ("gauge forces do not cross polarizations") at face value, with "ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry". The alternative "rested on an unsupported coefficient", an estimate that "has no source": "The sources generate that operator only from bi-charged states, which P4 forbids." Strict separation also closed failure channels of the paper's own model. The reading is P4's. See [round-3 decisions](../../method/review/round-3/decisions.md).

### How the record reached it

- **Lab notebook and v1.** P4 states that gauge interactions do not connect the representations; neither document discusses kinetic mixing ([#1 §1](../../../notes/broken-born-theory.md#1-postulates); [#9 §2](../../../notes/broken-born-program-v1.md#2-postulates--including-the-one-the-mathematics-rejected)).
- **Review round 1** found "kinetic mixing unaddressed" in the withdrawn paper, and the paper's v2 added a postulate with an "ε ≲ 10⁻⁵ exclusion" ([`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode)). That bound belonged to the paper's own postulate and is not the gravity-only figure in P4.
- **Review round 2** disputed gravity-induced mixing: the referee claimed "a graviton-loop mixing mechanism needing no bi-charged matter", and the handoff's summary of the adjudication adds that "its formula was uncited and unverified — v2's 'forbidden to all orders' is too strong either way; soften and resolve by literature" ([`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); [review rounds 1 and 2](../../method/review/rounds-one-and-two.md)). The handoff listed "UV stability of sector separation / kinetic mixing" as open item 3 ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)).
- **The v3 worklog** resolved it from the literature (item R4): "Pure gravity: ε = 0 if dark charge conjugation C is exact. Otherwise it needs at least 6 loops and gives ≲10⁻¹³ [Gherghetta–Kersten–Olive–Pospelov, PRD 100, 095001 (2019)]. The referee is right that it exists, and it is negligible." The paper's v3 carried this into its §2(a).
- **Round 3**: **Decision 1** adopted strict separation. #11 v2.1 wrote it into P4, and kinetic mixing does not appear among [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems)'s open problems.

### How to read the bound and the zero

- **A ceiling or a floor.** #11 writes ε ≲ 10⁻¹³. The round-3 referee notes that Gherghetta et al. present the figure as a floor, the "minimum kinetic mixing in any theory with hidden gauge interactions and charge symmetry breaking", which is "consistent with '<~' only in the sense 'up to'" (audit notes, Step 1). #11's wording stands; the reading is unresolved in the record.
- **Exact or gauged.** #11 says the mixing vanishes "if hidden charge conjugation is exact"; Decision 1 says "zero if hidden charge conjugation is a gauged symmetry". The v3 worklog bears on the difference: "Quantum gravity forbids an exact global C [Banks–Seiberg 2011; Harlow–Ooguri 2021]; a gauged C (O(2)/O(3)-type) remains a loophole [Obied–Parikh, preprint]" (R4), and the withdrawn paper's v3 (§2(b)) says a discrete symmetry acting as the other sector's charge conjugation forbids a mixing operator "only if that symmetry is gauged, since quantum gravity is believed to admit no exact global symmetries". #11 outranks the adjudication in the precedence list, so its wording is the current statement.

## What P4 does in the program

- **A permanent null.** Row 7 of [#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) predicts a "**Permanent null** (both dark-sector candidates SM-decoupled; P4 strict)" in direct-detection and collider searches, where SM-decoupled means decoupled from the Standard Model. It is killed by "Any confirmed non-gravitational DM–SM coupling", DM being dark matter ([row 7](../../predictions/direct-detection-null.md)). The row's wording counts two candidates, while [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) lists three; flag 63 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes "**Permanent null** (all dark-sector candidates SM-decoupled under P4 strict; for the third candidate's shared-photon form, a null of position-space searches, flag 60)".
- **The gate and the equivalence principle**, as above: χ falls and lenses like ordinary matter, and its self-interaction runs through X exchange (not derived, according to flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending; [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)).
- **P4 and the magnetic-mirror conjecture.** P.R.'s magnetic-mirror conjecture, open in [#11 §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) [O], gives each electrically charged x-polarized particle "a magnetically charged p-polarized analog". In its separate-photon form the analogs are magnetic under the p-polarized sector's own gauge field, and the form "is consistent with P4". In its shared-photon form, the popular article [#12](../../../popsci/universes-other-half.md)'s reading, the momentum-polarized sector is "the magnetic side of electromagnetism" (#12, 'Dark matter as the other polarization'): the analogs carry magnetic charge of our photon, so one gauge field would act in both sectors. Of that form [#11 §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) says: "P4 as written excludes this form ("gauge forces do not cross polarizations", in the program since #1), so it needs P4 restated." The no-crossing clause dates from the lab notebook's version 0.1, "Gauge interactions do not connect the two representations" ([#1 §1](../../../notes/broken-born-theory.md#1-postulates)); round-3 Decision 1 added the strict reading; both are postulates [P] (flag 60 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The shared-photon form also conflicts with the basis of row 7 outright, and the row's observable null survives only if the momentum sector is spread in position, which no document analyzes (flag 60; [the shared-photon form](../../electric-magnetic-duality/magnetic-identification.md#shared-photon)). The shared-photon form is also the setting of P.R.'s explanation of the monopole null result, open [O]: in [#11 §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)'s words it "requires P4 restated" and conditions that would hide the analogs, "none of them yet computed" (flag 62; [Conjecture: conjugate monopoles explain the null result](../../electric-magnetic-duality/monopole-explanation.md)). #12's further argument, that such a sector would be transparent to light, remains popsci-only ([the transparency argument](../../electric-magnetic-duality/magnetic-identification.md#popsci-only-the-transparency-argument); [the popular articles](../../history/documents/popular-articles.md)).

## P4 in the toy models: what makes the breaking physical

The [coset toy model](../../symmetry-breaking/toy-models/coset-model/_index.md) showed that an action symmetric under ρ is not enough for the breaking of ρ to have physical content. Its vacuum keeps a twisted element, ρ combined with the flip K → −K of the real structure K, so "Breaking ρ is physical only once a coupling odd in K is present" ([toy note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k); [the twisted element](../../symmetry-breaking/twisted-element.md)). [Round-4](../../method/review/round-4.md) ruling F3 named the remedy: "Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K" ([`review/round4-adjudication.md`](../../../review/round4-adjudication.md)).

The toy-model note builds such a coupling from a state's [Wigner function](../../phase-space/reciprocity/wigner-function.md) W ([toy note §5](../../papers/reciprocity-toy-models.md#5-matter-and-locality); [locality from an (H, K)-built coupling](../../symmetry-breaking/matter-coupling.md)):

```text
I[W] = ∫_{L+} du ( ∫_{L−} dv W )²                                   (toy note §5)
```

where L+ and L− are the two eigenlines of K, the null lines of η = ωK. At H = 1 it becomes "in the vacuum +K_ref ... ∫|ψ(x)|⁴ dx (local in x); in −K_ref it is ∫|ψ̃(p)|⁴ dp". For a test state ψ ∝ e^{−(x−1.3)²/0.7} + 0.6 e^{−(x+1.3)²/0.7}, "the two vacua give 0.4070 and 0.3600. **I is odd in K**, so it breaks the K → −K symmetry and makes the breaking of ρ physical" (on "odd in K", see flag 2 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The combined map (ψ → Fψ, K → −K) leaves I invariant, and a K-blind interaction ∫W² shows no asymmetry. The coupling "needs H as well as K" and is covariant only under the SO(2) that fixes H = 1 ([toy note §5](../../papers/reciprocity-toy-models.md#5-matter-and-locality)). [The gate](../../method/verification/the-gate.md) checks these statements ([`verify/toy_s5.py`](../../../verify/toy_s5.py), part C; its output prints the two values, 0.4070 vs 0.3600; [the toy-model scripts](../../method/verification/toy-model-scripts.md)).

The note draws the analogy and the limit in two sentences: "Locality in the selected Lagrangian therefore follows from the vacuum once matter couples this way, as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling." ([toy note §5](../../papers/reciprocity-toy-models.md#5-matter-and-locality)).

The worklog states the role of P4 more directly. The section condition built from η confines matter to one null line but "cannot tell position from momentum", so "Without that lock, matter's choice of section and K's sign are independent orders", and "**The lock is P4** (x-polarized matter, and its ρ-image, p-polarized matter)" ('Chunk 4'; [the section condition](../../symmetry-breaking/section-condition.md)). In the toy, then, the program's account of why forces fade with distance "amounts to this: our matter is the x-polarized species. The explanatory gain is that x-locality comes packaged with a p-local mirror sector, the program's dark-matter claim. It does not derive x-locality from nothing." The worklog calls the coupling "ρ-covariant"; version 2 of the note restates it as built from (H, K) and covariant under SO(2) only, after round-4 ruling F5.

## The strong form of locality

What the toy models leave open is the strong form of the locality claim: that the vacuum forces matter to be local in the selected polarization, rather than matter being postulated to couple that way.

- [#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) lists as still open [O] "locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4".
- The toy-model note lists "a mechanism forcing the (H, K)-coupling of matter" under "Not shown" ([§6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations)).
- [`CLAUDE.md`](../../../CLAUDE.md) names "the strong form of matter locality" as one of the toy work's open ends. The worklog adds that the strong form is "also open in the literature" ('Chunk 4').

See [Open: forced locality and the P4 lock](../../symmetry-breaking/strong-locality.md) and [open problems](../../status/open-problems.md).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — the statement and its strict reading; [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — χ on g; [§11.1](../../papers/broken-born-checkpoint-v2.md#111-the-monopole-audit-revised-d) — conjugate solitons gravitate by P4; [§11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) — the magnetic-mirror conjecture [O], whose shared-photon form P4 as written excludes and which is the setting of the open explanation of the monopole null result; [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — χ as a candidate; [§13 row 7](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the permanent null; [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open problems, with forced locality in item 11 and no kinetic-mixing item
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — strict separation in force; the strong form of matter locality as an open end
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Decisions' 1 — why strict separation was adopted; 'Rulings' 7, 9 — the dimension-5 coefficient and the Witten-effect charge
- [`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 1 — the referee's quotations of Gherghetta et al. and its reading of the bound
- [`review/v3-worklog.md`](../../../review/v3-worklog.md) 'Round-2 pending list', item R4 — the literature resolution; exact versus gauged hidden charge conjugation
- [`notes/knot-dark-matter-standalone.md` §2](../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling) — the withdrawn manuscript's kinetic-mixing points (a)–(c)
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen), [§6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — review rounds 1–2 on kinetic mixing, and open item 3
- [`notes/broken-born-theory.md` §1](../../../notes/broken-born-theory.md#1-postulates) — the v0.1 statement, with the equivalence principle across polarizations; [§3](../../../notes/broken-born-theory.md#3-action) — the untouched Standard Model sector; [§4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured) — χ falls, orbits and lenses
- [`notes/broken-born-program-v1.md` §2](../../../notes/broken-born-program-v1.md#2-postulates--including-the-one-the-mathematics-rejected) — the v1 statement, before the strict reading
- [`notes/geometric-core.md` §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) — universal coupling to H and the gate as X exchange
- [`wiki/papers/reciprocity-toy-models.md` §5](../../papers/reciprocity-toy-models.md#5-matter-and-locality) and [`review/round4-adjudication.md`](../../../review/round4-adjudication.md) 'Rulings' F3 — P4-type coupling as what makes the breaking physical; F5 — the coupling needs H; [toy note §6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations) — what is not shown; [`verify/toy_s5.py`](../../../verify/toy_s5.py) part C — the gated check
- [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) 'Chunk 4 (in progress, 2026-10-19): S5' — the P4 lock
- [`popsci/universes-other-half.md`](../../../popsci/universes-other-half.md) 'Dark matter as the other polarization' — the magnetic identification and the transparency argument (popular article; not a status source)
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 60 — the history of P4's no-crossing clause and its strict reading, and the shared-photon form's conflicts. Item 62 — the explanation of the monopole null result as open in that form's setting. Item 63 — row 7 still worded for two candidates, with the proposed wording; pending
- [`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate) and [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 55 — exchanging [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate; the proposed tags [P] for the gate and μ, [O] for the mechanism; pending
