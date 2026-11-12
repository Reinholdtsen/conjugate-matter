---
title: "Open: polarization-genesis and the 5.4 : 1 ratio (OP7)"
weight: 50
status: open
description: "No candidate's abundance is explained: thermal freeze-out fails for a light gravity-only sector, so the ratio Ω_χ : Ω_b = 5.4 : 1 needs a mechanism — the program's analog of baryogenesis."
provenance: [O]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 7"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §8"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/wave-island.md 'Bonus: the relic-abundance problem solves itself'"
  - "notes/geometric-core.md §D"
  - "notes/geometric-core.md §F"
  - "notes/broken-born-program-v1.md §10"
  - "HANDOFF.md §2"
  - "CLAUDE.md 'Since the handoff'"
  - "review/wiki-build-flags.md item 18"
---

*Polarization-genesis is the program's name for a mechanism it does not yet have: the process that would set how much [dark matter](../_index.md) the early universe made compared with ordinary matter, whose densities stand in the observed ratio Ω_χ : Ω_b = 5.4 : 1. For particle χ the [lab notebook](../../history/documents/lab-notebook.md) argues that the standard route is closed: a light sector that interacts strongly with itself and touches ordinary matter only through gravity cannot get its abundance from [thermal freeze-out](thermal-freeze-out.md#particle-χ-the-route-the-notebook-closes), so the abundance has to come from an asymmetry, as the abundance of ordinary baryons does. The notebook sketched a mechanism in which heavy fields decay into both kinds of matter, with the split set by an angle of the vacuum's [polarization](../../phase-space/reciprocity/lagrangian-polarizations.md), and called it "a shape, not a mechanism". The problem is open and applies to all three [dark-matter candidates](_index.md).*

**Status:** Open [O] — [#11 §14 item 7](../../papers/broken-born-checkpoint-v2.md#14-open-problems), "Polarization-genesis: Ω_χ : Ω_b = 5.4 : 1 [O]". The notebook's sketch is tagged "[O, sketched]" ([`notes/broken-born-theory.md` §8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched)). It qualifies all three candidates: [the χ-particle candidate](chi-particles.md), [the X-condensate candidate](x-condensate.md) and P.R.'s conjecture of [magnetic monopoles abundant in momentum space](momentum-space-monopoles.md). Nothing is calculated and nothing is machine-checked. Listed among [open problems](../../status/open-problems.md); not on the current queue in the root [`CLAUDE.md`](../../../CLAUDE.md).

## The question

Dark matter outweighs ordinary (baryonic) matter by a fixed factor. [Checkpoint #11](../../history/documents/checkpoint.md) writes the ratio Ω_χ : Ω_b = 5.4 : 1 ([§14 item 7](../../papers/broken-born-checkpoint-v2.md#14-open-problems)), the lab notebook Ω_χ/Ω_b = 5.4 ([#1 §5.3](../../../notes/broken-born-theory.md#53-relic-abundance-o)), and [the handoff](../../history/documents/handoff.md) "Ω_DM:Ω_b = 5.4:1" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)), where DM is dark matter. Ω_b is the density of baryons and Ω_χ that of the dark matter, each as a fraction of the critical density. The documents treat the value as an observational input and give no reference for it.

The question is what physics fixes the ratio. [#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) states its scope: "The 5.4 : 1 abundance question (polarization-genesis) applies to all three". The name follows baryogenesis, the process that set the excess of baryons over antibaryons; [#9](../../../notes/broken-born-program-v1.md) calls the problem "the program's baryogenesis analog [O]" ([#9 §10 item 6](../../../notes/broken-born-program-v1.md#10-open-problems)).

## Why the standard route fails for particle χ

The notebook states the argument in two sentences [O]:

> A sub-GeV, strongly self-coupled, gravitationally-only-connected sector cannot freeze out thermally without cannibalism problems; the abundance must be set asymmetrically — by *polarization-genesis* (§8). The observed Ω_χ/Ω_b = 5.4 is an input awaiting a mechanism, exactly as η_B awaited baryogenesis. ([#1 §5.3](../../../notes/broken-born-theory.md#53-relic-abundance-o))

On the wiki's reading, the three adjectives describe χ as the notebook had just fixed it. "Sub-GeV" and "strongly self-coupled" match its benchmark two subsections earlier: a mass m_χ ≈ 70 MeV × α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3} for a coupling α̃ of order one ("At α̃ ∼ 1 the Born approximation is marginal"), fixed by the cross-section per mass σ₀/m_χ ≈ 30 cm²/g that fits [dwarf-galaxy cores](../halo-astrophysics/dwarf-galaxies.md) ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d); [the scattering benchmark](../conjugate-matter/benchmark.md)). "Gravitationally-only-connected" is postulate [P4](../../program/postulates/p4-polarized-matter.md): no gauge force crosses from ordinary matter to χ, a statement #11 takes strictly ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)).

Why that combination rules out freeze-out is standard [T] ([relic abundance mechanisms](relic-abundance.md)). Thermal freeze-out sets the abundance by annihilation into lighter particles, at a rate fixed by the coupling to them. A sector connected to ours only by gravity cannot annihilate into ordinary particles at any useful rate, and if χ is the lightest state of its own sector it has nothing lighter to annihilate into. What remains are number-changing self-interactions, in which several χ particles scatter into fewer and the lost rest mass heats the survivors: cannibalism, whose outcome depends on the sector's self-coupling and its own initial temperature rather than on any coupling to ordinary matter. The notebook does not spell out which "cannibalism problems" it means; this is the standard picture.

The notebook's conclusion is that the abundance "must be set asymmetrically": by an excess of χ over its antiparticle, as the baryon density is set by an excess of baryons.

## The template: baryogenesis [T]

The baryon density is not a freeze-out relic. It is set by the baryon asymmetry η_B, a small excess of baryons over antibaryons that survived when the rest annihilated [T]. Producing such an excess requires the three Sakharov conditions: baryon-number violation, violation of C (charge conjugation) and of CP (charge conjugation and parity combined), and a departure from thermal equilibrium [T]. Asymmetric dark matter extends the idea to the dark sector, so that a shared origin of the two excesses can fix the ratio of the two densities [T]. The notebook's comparison, "exactly as η_B awaited baryogenesis", places the 5.4 : 1 ratio where η_B stood before a mechanism for it existed: an observed number with no derivation.

## The notebook's sketch [O, sketched]

[#1 §8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched) gives the only proposal in the record, in full:

> Why Ω_χ : Ω_b = 5.4 : 1? Sketch: at reheating, the heavy Grassmannian moduli (the nine non-Maslov directions) decay; their branching into x- versus p-polarized quanta is set by the vacuum tilt angle, Ω_χ/Ω_x^(0) ~ tan²θ_pol, after which baryogenesis processes the x-side. A relation between the observed ratio and a Grassmannian angle would be the theory's second nontrivial number. Status: a shape, not a mechanism — the same maturity baryogenesis had in 1966.

Its steps, with what the record supplies for each:

1. **The decaying fields.** The vacuum's polarization is a point of [the Lagrangian Grassmannian](../../phase-space/modular-field/lagrangian-grassmannian.md) Λ(4), the space of position/momentum splittings, which has "dimension d(d+1)/2 = 10 for d = 4" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core) [T]). One direction is the Maslov circle, whose angle τ is the dark-energy field ([τ as the Maslov phase](../../phase-space/modular-field/maslov-phase.md)); the other nine are the "non-Maslov directions". That τ "is the *lightest* modulus, with the other nine directions heavy, is assumed **[P]**" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)).
2. **Decay at reheating.** [Reheating](../../cosmology/early-universe/inflation-and-dilution.md) is the end of inflation, when the energy of the fields that drove it is converted into a hot plasma [T]. In the sketch the nine heavy moduli decay then, into quanta of both polarizations: x-polarized ordinary matter and p-polarized χ.
3. **The split.** The branching between the two is "set by the vacuum tilt angle", giving Ω_χ/Ω_x^(0) ~ tan²θ_pol. The notebook defines θ_pol only by that phrase; its postulate [P5](../../program/postulates/p5-spontaneous-selection.md) calls our vacuum "x-tilted" ([#1 §1](../../../notes/broken-born-theory.md#1-postulates)). It gives no amplitudes. A ratio of the form tan²θ is what a split by angle produces when the two channels receive amplitudes proportional to sin θ and cos θ, as when polarized light meets a polarizing beam splitter at angle θ and the two output intensities go as cos²θ and sin²θ [T]; that this is the intended reading is the wiki's inference, not the notebook's statement.
4. **Baryogenesis on the x-side.** Ω_x^(0) is not defined further. The superscript reads as the x-side share before "baryogenesis processes the x-side", but the notebook does not say how Ω_x^(0) becomes Ω_b, so the sketch does not by itself give Ω_χ : Ω_b.
5. **What it would buy.** A relation between the ratio and a Grassmannian angle "would be the theory's second nontrivial number". The notebook does not say which number is the first.

The sketch has no decay rates, no value for θ_pol and no number for the ratio, and no later document develops it. Its own verdict, "a shape, not a mechanism", is the status the wiki records.

## An unreconciled dependence

The sketch needs the nine heavy moduli to exist as fields and to decay. [Calc note #5](../../history/documents/field-equation-notes.md), written later, counts them in the field content of the broken vacuum and expects most of them to disappear: "Λ(d) σ-modes (10: τ plus nine, of which inverse-Higgs constraints likely eliminate most [O])" ([`notes/geometric-core.md` §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)). [Inverse-Higgs constraints](../../symmetry-breaking/inverse-higgs-constraints.md) are relations that make some would-be [Goldstone fields](../../symmetry-breaking/goldstone-and-higgs.md) derivatives of others, removing them as independent fields [T]. [#5](../../../notes/geometric-core.md) lists "(4) inverse-Higgs accounting of the nine heavy moduli" among the items "Now precisely open" ([§F](../../../notes/geometric-core.md#f-status-after-tonight)), and no later note returns to it. No document reconciles the sketch with #5's expectation ([Open: field content of the broken vacuum](../../phase-space/modular-field/field-content.md); [conflicts between sources](../../history/documents/source-conflicts.md#dark-matter)).

## Scope: the three candidates

- **Wave χ.** Very light χ on [the wave island](../momentum-clumping/wave-island/_index.md) gets its abundance by misalignment, like an [axion](../../cosmology/dark-energy/axion-like-fields.md#wave-χ-produced-like-an-axion). [Calc note #3](../../history/documents/clumping-notes.md): "Open problem #5 (cannibalism-safe relic abundance) is moot on the wave island: misalignment is the mechanism, and Ω_χ trades against (m, χᵢ) in the standard way. The 5.4:1 question remains (polarization-genesis), but the *production channel* is no longer exotic" ('Bonus'; [relic abundance by misalignment on the wave island](../momentum-clumping/wave-island/misalignment-relic.md)). The notebook's addendum v0.2 records "open problems 3 and 5 close (5 via misalignment production on the wave island)". That closes the production channel on the wave island only; the ratio itself stays open. "Open problem #5" here is item 5 of the notebook's list, not item 5 of [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems), which is [the dual-stress enhancement](../conjugate-matter/dual-stress-enhancement.md).
- **Particle χ.** The freeze-out argument above applies, and no mechanism is known.
- **The X-condensate.** No document discusses how it would be produced. [#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) applies the ratio question to it as to χ.
- **The conjugate monopoles.** P.R.'s conjecture, the third candidate ([Conjecture: magnetic monopoles abundant in momentum space](momentum-space-monopoles.md)). The record gives no mechanism and no number for how many form, and [#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) applies the ratio question to them as to the other two. [#14](../../../notes/knot-dark-matter-standalone.md)'s model of the candidate, with ordinary kinematics, failed on its count of how many monopoles the early universe makes ([Obituary: #14's superheavy-soliton model](soliton-candidate/obituary.md)).

#11 outranks the notebook, and it keeps the ratio open for all three candidates.

## History

- **The lab notebook (v0.1).** [§5.3](../../../notes/broken-born-theory.md#53-relic-abundance-o) states the problem and [§8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched) the sketch. Its list of open problems, "in order of severity", ranks "**Polarization-genesis** mechanism for 5.4 : 1. **[O]**" fourth and makes the fifth depend on it: "**Relic abundance** without cannibalism: needs the asymmetric mechanism of (4). **[O]**" ([#1 §11](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity)).
- **[The clumping problem](../../history/main-problems.md) (addendum v0.2).** The relic-abundance item closes on the wave island; polarization-genesis does not.
- **#9.** Open problem 6: "Polarization-genesis: the 5.4 : 1 ratio Ω_χ : Ω_b — the program's baryogenesis analog [O]" ([#9 §10](../../../notes/broken-born-program-v1.md#10-open-problems)).
- **The handoff.** Open item 7, "Polarization-genesis (the Ω_DM:Ω_b = 5.4:1 ratio)" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)).
- **#11.** [§14 item 7](../../papers/broken-born-checkpoint-v2.md#14-open-problems), and [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates)'s statement of its scope: "applies to all three". #11 v2.0 said of the third candidate that "the knot option inherits the monopole-abundance machinery of standard cosmology with inflationary dilution acting on both sectors at once".
- **Now.** The current queue in the root [`CLAUDE.md`](../../../CLAUDE.md) ('Since the handoff') does not include it.

## A date to check

The notebook's "the same maturity baryogenesis had in 1966" is not checked against a source. Sakharov's conditions are usually dated 1967 (from model memory, †); the register entry is on [references](../../references.md), and the discrepancy is [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 18, pending. The flags' audit rated the item unclear: no repository file dates Sakharov's conditions independently, so under the † rule the usual date stays unverified.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §14 item 7](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open problem; [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — it applies to all three candidates, and the failure of #14's model; §8 — the benchmark; [§4](../../../notes/knot-dark-matter-standalone.md#4-observational-consistency) — P4, taken strictly
- Git history: #11 v2.0 at commit 008c3ee, §12 — the knot option's abundance
- [`notes/broken-born-theory.md` §5.3](../../../notes/broken-born-theory.md#53-relic-abundance-o) — why freeze-out fails; [§8](../../../notes/broken-born-theory.md#8-polarization-genesis-o-sketched) — the sketch; [§11](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity) — items 4 and 5 of the notebook's open problems; [§2](../../../notes/broken-born-theory.md#2-kinematic-core) — the dimension of Λ(4) and the nine heavy directions [P]; [§5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d) — the benchmark; [§1](../../../notes/broken-born-theory.md#1-postulates) — P5, "x-tilted"; 'Addendum (v0.2)' — the wave-island closure
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'Bonus: the relic-abundance problem solves itself' — misalignment on the wave island; the ratio remains
- [`notes/geometric-core.md` §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) — the nine moduli, likely eliminated; [§F item 4](../../../notes/geometric-core.md#f-status-after-tonight) — "inverse-Higgs accounting of the nine heavy moduli", open
- [`notes/broken-born-program-v1.md` §10](../../../notes/broken-born-program-v1.md#10-open-problems) — "the program's baryogenesis analog"
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — open item 7
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the current queue
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 18 — the notebook's 1966 date for baryogenesis
