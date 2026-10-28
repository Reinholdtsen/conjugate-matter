---
title: "P4: polarized matter and strict sector separation"
weight: 60
status: alive
description: "The Standard Model is x-polarized and conjugate matter χ is p-polarized; both couple universally to H and no gauge force crosses polarizations, taken strictly since v2.1 (gravity-induced mixing ε ≲ 10⁻¹³)."
provenance: [P]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13 row 7"
  - "papers/broken-born-checkpoint-v2.md §14"
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
  - "notes/debt1a-geometric-core.md §E"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §6"
  - "review/round4-adjudication.md 'Rulings' F3, F5"
  - "verify/toy_s5.py part C"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §3"
---

*P4 is the program's axiom about matter. Ordinary matter, the Standard Model, is x-polarized: its fields are organized around position, the variable in which its interactions are local. A second kind, conjugate matter χ, is p-polarized, organized around momentum. Both kinds respond to the same gravity, so the [equivalence principle](/wiki/gravity/spin-2-fields/equivalence-principle) holds across them, but no gauge force (the electromagnetic, weak or strong interaction) acts between them. Since [checkpoint](/wiki/history/documents/checkpoint) v2.1 the program reads the last clause strictly: the only mixing allowed between the two sectors is what gravity itself induces, which is zero or extremely small. P4 is the basis of the program's prediction that dark-matter direct-detection experiments will see nothing, and in the toy models it is also what gives the vacuum's choice of polarization a physical effect.*

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

This is #11 §4's text. The [lab notebook](/wiki/history/documents/lab-notebook)'s version spells out what universal coupling means:

> **P4 (Polarized matter, universal gravity).** Matter comes in two representations: x-polarized fields (the Standard Model) and p-polarized fields (χ, conjugate matter). Both couple universally to H — the equivalence principle holds across polarizations. Gauge interactions do not connect the two representations. **[P]** (#1 §1)

The program paper v1 states the first three clauses as #11 does, without the strict-reading bracket (#9 §2); kinetic mixing appears nowhere in it. The axiom makes three claims, taken in turn below: two kinds of matter, one gravity for both, and no gauge force between them.

## Two polarizations of matter

A polarization is a choice of which half of the phase-space directions count as position: a Lagrangian subspace for the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω ([Lagrangian polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)). An x-polarized field is written as a function of position, and its interactions are local in x, as the known interactions are ("x-local interactions", #11 §3). A p-polarized field is written as a function of momentum, and its interactions are local in p. The two descriptions are related as a waveform and its spectrum are related by the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform), which implements the Born rotation ρ ([Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)). The [toy-model](/wiki/symmetry-breaking/toy-models) worklog puts the pair in exactly these terms: "x-polarized matter, and its ρ-image, p-polarized matter" ('Chunk 4').

- **The x-polarized sector** is the Standard Model. In the lab notebook's action it is untouched: "S_x is the Standard Model minimally coupled to g. Nothing is modified. **[P4]**" (#1 §3), where g is the spacetime metric.
- **The p-polarized sector** is conjugate matter χ ([conjugate matter and the velocity gate](/wiki/dark-matter/conjugate-matter)). In the current program χ is one of the two remaining [dark-matter candidates](/wiki/dark-matter/candidates), "p-polarized matter field" in #11 §12's table ([the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles)). Its distinctive property is a self-interaction that depends on relative momentum, the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate).

## One gravity for both

"Both couple universally to H" is the [equivalence principle](/wiki/gravity/spin-2-fields/equivalence-principle) extended across the two polarizations: H is the [generalized metric](/wiki/phase-space/born-geometry/born-structures) of [P1](/wiki/program/postulates/p1-arena), which contains the spacetime metric g, and both kinds of matter couple to it in the same way. The lab notebook draws the observational consequence: "χ couples to g universally: it falls, orbits, and lenses like ordinary dark matter. Bullet Cluster lensing-centroid behavior is automatic" [D] (#1 §4). #11 §8 keeps it: "χ propagates on g (equivalence principle; Bullet-Cluster-safe)" ([the Bullet Cluster](/wiki/dark-matter/halo-astrophysics/bullet-cluster)).

Universal coupling to H also supplies the gate's mechanism. The [Debt-1 note](/wiki/history/documents/debt-1-notes): "Conjugate matter couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃". Exchange of the [momentum graviton](/wiki/gravity/momentum-graviton) X between two such bilinears "yields a four-point amplitude that depends on the **incoming relative momenta** of the pair — the variable no x-local mediator can produce" (#5 §E; [dual stress](/wiki/dark-matter/conjugate-matter/dual-stress); [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). `notes/gate-mechanism.md` (2026-10-28; two derivations, the second blind; not reviewed) finds that this exchange cannot produce the gate: with #11 §7's X every on-shell vertex depends only on the momentum transfer, and no χχX vertex or formula for T̃ exists in the record (§§2–3). Flag 55 in `review/wiki-build-flags.md` proposes [P] for the gate and μ and [O] for the mechanism, pending Paul's ruling ([exchanging X cannot produce the gate](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). And because everything couples to H, conjugate-sector objects gravitate even if nothing else of theirs is visible: "by P4, conjugate-sector solitons gravitate" (#11 §11.1; [conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)).

## No gauge force between them

### Kinetic mixing

The third clause, "gauge forces do not cross polarizations", says that no particle feels both the Standard Model's forces and the conjugate sector's. Even without such particles, two sectors with separate abelian gauge forces can be linked by kinetic mixing: a term in the action that couples the field strength of our photon to that of a hidden photon, with a small coefficient ε [T] ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)). Its effect is that particles charged only under the hidden force acquire a small charge under ours, "visible electric charge ~ epsilon e" in the [withdrawn manuscript #14](/wiki/dark-matter/candidates/soliton-candidate)'s words (#14 §2(c)). Mixing is therefore a channel through which a hidden sector becomes visible.

### The strict reading (since v2.1)

Since v2.1 (2026-10-19) #11 takes P4 to exclude kinetic mixing "beyond what gravity induces", and gives the gravitational amount from Gherghetta, Kersten, Olive and Pospelov [27S]: it "vanishes if hidden charge conjugation is exact and otherwise first appears at six loops, ε ≲ 10⁻¹³" (#11 §4). The round-3 referee checked the paper and quoted it (audit notes, Step 1):

- "If C_A and C_X are separately good symmetries ..., then kinetic mixing cannot be induced at any perturbative order" (p. 5), which is the source of the zero;
- "kinetic mixing through gravity alone, requires at least six loops and could be as large as ~1e-13" (abstract), conditional, in the referee's summary, "on C_X breaking and O(1) hidden Yukawa".

`CLAUDE.md` lists the reading among the changes since [the handoff](/wiki/history/documents/handoff): "Strict sector separation (P4 at face value) is in force."

### Why it was adopted: round-3 Decision 1

The strict reading was a decision, not a derivation. On 2026-10-19, after the [round-3 review](/wiki/method/review/round-3) of the soliton manuscript #14, Paul delegated a set of decisions to Claude, keeping the veto (`review/round3-adjudication.md`, 'Decisions'). The first:

> **Kinetic mixing: strict sector separation.** ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry.
> - It is the program's own postulate P4 ("gauge forces do not cross polarizations") taken at face value.
> - The alternative rested on an unsupported coefficient. The dimension-5 "O(1) at the Planck scale" estimate (ruling 7) has no source. The sources generate that operator only from bi-charged states, which P4 forbids.
> - It costs nothing and closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector.

The three channels belonged to #14's hidden sector. ψ was its light hidden-charged fermion, which mixing would have given a small electric charge; ruling 9 accepted, without re-checking, that with mixing and a physical hidden θ angle the monopoles would carry "visible electric charge ~ εθ/2π · e (Witten effect)" ([the Witten effect](/wiki/electric-magnetic-duality/monopoles/witten-effect)); and the referee listed "Re-thermalization by ψ at ε ~ 1e-7–1e-6" among the constraints #14 had omitted, accepted as a to-do and not individually re-checked (`review/round3-adjudication.md`, 'Rulings'). Ruling 7 upheld the referee's finding that the dimension-5 operator's "O(1) coefficient at the Planck scale" is unsupported, since "the literature generates it at one loop from bi-charged states, which sector separation forbids" ([obituary of Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator)). Decision 2 retired the soliton candidate the same day ([its obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary)), so the three channels no longer threaten a live candidate, but the strict reading stays as P4's reading. See [round-3 decisions](/wiki/method/review/round-3/decisions).

### How the record reached it

- **Lab notebook and v1.** P4 states that gauge interactions do not connect the representations; neither document discusses kinetic mixing (#1 §1; #9 §2).
- **Review round 1** found "kinetic mixing unaddressed" in #14, and v2 of the manuscript added a postulate with an "ε ≲ 10⁻⁵ exclusion" (`HANDOFF.md` §6). That bound belonged to the withdrawn manuscript's own postulate and is not the gravity-only figure in P4.
- **Review round 2** disputed gravity-induced mixing: the referee claimed "a graviton-loop mixing mechanism needing no bi-charged matter", and the handoff's summary of the adjudication adds that "its formula was uncited and unverified — v2's 'forbidden to all orders' is too strong either way; soften and resolve by literature" (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)). The handoff listed "UV stability of sector separation / kinetic mixing" as open item 3 (`HANDOFF.md` §2).
- **The v3 worklog** resolved it from the literature (item R4): "Pure gravity: ε = 0 if dark charge conjugation C is exact. Otherwise it needs at least 6 loops and gives ≲10⁻¹³ [Gherghetta–Kersten–Olive–Pospelov, PRD 100, 095001 (2019)]. The referee is right that it exists, and it is negligible." #14 v3 §2(a) carried this into the manuscript.
- **Round 3** upheld ruling 7 and accepted ruling 9, as above, and **Decision 1** adopted strict separation. #11 v2.1 wrote it into P4, and kinetic mixing does not appear among #11 §14's open problems.

### How to read the bound and the zero

- **A ceiling or a floor.** #11 writes ε ≲ 10⁻¹³. The round-3 referee notes that Gherghetta et al. present the figure as a floor, the "minimum kinetic mixing in any theory with hidden gauge interactions and charge symmetry breaking", which is "consistent with '<~' only in the sense 'up to'" (audit notes, Step 1). #11's wording stands; the reading is unresolved in the record.
- **Exact or gauged.** #11 says the mixing vanishes "if hidden charge conjugation is exact"; Decision 1 says "zero if hidden charge conjugation is a gauged symmetry". The v3 worklog bears on the difference: "Quantum gravity forbids an exact global C [Banks–Seiberg 2011; Harlow–Ooguri 2021]; a gauged C (O(2)/O(3)-type) remains a loophole [Obied–Parikh, preprint]" (R4), and #14 v3 §2(b) says a discrete symmetry acting as hidden charge conjugation forbids the dimension-5 operator "only if that symmetry is gauged, since quantum gravity is believed to admit no exact global symmetries". #11 outranks the adjudication in the precedence list, so its wording is the current statement.

## What P4 does in the program

- **A permanent null.** Row 7 of #11 §13 predicts a "**Permanent null** (both dark-sector candidates SM-decoupled; P4 strict)" in direct-detection and collider searches, where SM-decoupled means decoupled from the Standard Model. It is killed by "Any confirmed non-gravitational DM–SM coupling", DM being dark matter ([row 7](/wiki/predictions/direct-detection-null)).
- **The gate and the equivalence principle**, as above: χ falls and lenses like ordinary matter, and its self-interaction runs through X exchange (not derived, according to flag 55 in `review/wiki-build-flags.md`, pending Paul's ruling; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)).
- **What strict P4 excludes in the popular article.** The popular article #12 calls the momentum-polarized sector "the magnetic side of electromagnetism", dark because [Dirac's condition](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) makes its coupling strong, and argues that such a sector would be transparent to light (#12, 'Dark matter as the other polarization'). Neither is a program claim. The magnetic identification conflicts with strict P4 and row 7 and is treated as dead ([its obituary](/wiki/electric-magnetic-duality/magnetic-identification)); the transparency argument is quarantined as popsci-only ([the popular articles](/wiki/history/documents/popular-articles)).

## P4 in the toy models: what makes the breaking physical

The [coset toy model](/wiki/symmetry-breaking/toy-models/coset-model) showed that an action symmetric under ρ is not enough for the breaking of ρ to have physical content. Its vacuum keeps a twisted element, ρ combined with the flip K → −K of the real structure K, so "Breaking ρ is physical only once a coupling odd in K is present" (toy note §2; [the twisted element](/wiki/symmetry-breaking/twisted-element)). [Round-4](/wiki/method/review/round-4) ruling F3 named the remedy: "Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K" (`review/round4-adjudication.md`).

The toy-model note builds such a coupling from a state's [Wigner function](/wiki/phase-space/reciprocity/wigner-function) W (toy note §5; [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)):

```text
I[W] = ∫_{L+} du ( ∫_{L−} dv W )²                                   (toy note §5)
```

where L+ and L− are the two eigenlines of K, the null lines of η = ωK. At H = 1 it becomes "in the vacuum +K_ref ... ∫|ψ(x)|⁴ dx (local in x); in −K_ref it is ∫|ψ̃(p)|⁴ dp". For a test state ψ ∝ e^{−(x−1.3)²/0.7} + 0.6 e^{−(x+1.3)²/0.7}, "the two vacua give 0.4070 and 0.3600. **I is odd in K**, so it breaks the K → −K symmetry and makes the breaking of ρ physical" (on "odd in K", see flag 2 in `review/wiki-build-flags.md`). The combined map (ψ → Fψ, K → −K) leaves I invariant, and a K-blind interaction ∫W² shows no asymmetry. The coupling "needs H as well as K" and is covariant only under the SO(2) that fixes H = 1 (toy note §5). [The gate](/wiki/method/verification/the-gate) checks these statements (`verify/toy_s5.py`, part C; its output prints the two values, 0.4070 vs 0.3600; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

The note draws the analogy and the limit in two sentences: "Locality in the selected Lagrangian therefore follows from the vacuum once matter couples this way, as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling." (toy note §5).

The worklog states the role of P4 more directly. The section condition built from η confines matter to one null line but "cannot tell position from momentum", so "Without that lock, matter's choice of section and K's sign are independent orders", and "**The lock is P4** (x-polarized matter, and its ρ-image, p-polarized matter)" ('Chunk 4'; [the section condition](/wiki/symmetry-breaking/section-condition)). In the toy, then, the program's account of why forces fade with distance "amounts to this: our matter is the x-polarized species. The explanatory gain is that x-locality comes packaged with a p-local mirror sector, the program's dark-matter claim. It does not derive x-locality from nothing." The worklog calls the coupling "ρ-covariant"; v2 of the note restates it as built from (H, K) and covariant under SO(2) only, after round-4 ruling F5.

## The strong form of locality

What the toy models leave open is the strong form of the locality claim: that the vacuum forces matter to be local in the selected polarization, rather than matter being postulated to couple that way.

- #11 §14 item 11 lists as still open [O] "locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4".
- The toy-model note lists "a mechanism forcing the (H, K)-coupling of matter" under "Not shown" (§6).
- `CLAUDE.md` names "the strong form of matter locality" as one of the toy work's open ends. The worklog adds that the strong form is "also open in the literature" ('Chunk 4').

See [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) and [open problems](/wiki/status/open-problems).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — the statement and its strict reading; §8 — χ on g; §11.1 — conjugate solitons gravitate by P4; §12 — χ as a candidate; §13 row 7 — the permanent null; §14 — the open problems, with forced locality in item 11 and no kinetic-mixing item
- `CLAUDE.md` 'Since the handoff' — strict separation in force; the strong form of matter locality as an open end
- `review/round3-adjudication.md` 'Decisions' 1 — why strict separation was adopted; 'Rulings' 7, 9 — the dimension-5 coefficient and the Witten-effect charge
- `review/round3/referee/audit-notes.md` Step 1 — the referee's quotations of Gherghetta et al. and its reading of the bound
- `review/v3-worklog.md` 'Round-2 pending list', item R4 — the literature resolution; exact versus gauged hidden charge conjugation
- `notes/knot-dark-matter-standalone.md` §2 — the withdrawn manuscript's kinetic-mixing points (a)–(c)
- `HANDOFF.md` §2, §6 — review rounds 1–2 on kinetic mixing, and open item 3
- `notes/broken-born-theory.md` §1 — the v0.1 statement, with the equivalence principle across polarizations; §3 — the untouched Standard Model sector; §4 — χ falls, orbits and lenses
- `notes/broken-born-program-v1.md` §2 — the v1 statement, before the strict reading
- `notes/debt1a-geometric-core.md` §E — universal coupling to H and the gate as X exchange
- `papers/reciprocity-toy-models.md` §5 and `review/round4-adjudication.md` 'Rulings' F3 — P4-type coupling as what makes the breaking physical; F5 — the coupling needs H; toy note §6 — what is not shown; `verify/toy_s5.py` part C — the gated check
- `notes/toy-lagrangian.md` 'Chunk 4 (in progress, 2026-10-19): S5' — the P4 lock
- `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the magnetic identification and the transparency argument (popular article; not a status source)
- `notes/gate-mechanism.md` §2 and `review/wiki-build-flags.md` item 55 — exchanging #11 §7's X cannot produce the gate; the proposed tags [P] for the gate and μ, [O] for the mechanism; awaiting Paul's ruling
