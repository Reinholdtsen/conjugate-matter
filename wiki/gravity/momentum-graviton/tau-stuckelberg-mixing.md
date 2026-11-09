---
title: "Open: τ–Stückelberg mixing (OP6)"
weight: 70
status: open
description: "How strongly the dark-energy field τ mixes, through the potential, with the Stückelberg modes that X absorbs: logged in calc note #8 as expected small by compactness, never computed."
provenance: [O]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 6"
  - "notes/beta-coefficients.md §3"
  - "notes/beta-coefficients.md §5"
  - "notes/beta-coefficients.md §1"
  - "notes/x-classification.md §3"
  - "notes/tuning-test.md §3"
  - "notes/tuning-test.md §4"
  - "notes/tuning-test.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.5"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-program-v1.md §10"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §8"
  - "CLAUDE.md 'Since the handoff'"
---

*This open problem asks how strongly the [dark-energy field τ](../../cosmology/dark-energy/tau-quintessence.md) mixes with the [Stückelberg modes](../../symmetry-breaking/goldstone-and-higgs.md), the would-be Goldstone fields that the [momentum graviton X](_index.md) absorbs when it becomes massive. Two fields mix when the quadratic part of a theory contains a term coupling them, so that neither has a definite mass on its own. The program's leading-order result is that τ is not among the absorbed modes and stays light ([τ is not eaten](tau-not-eaten.md)). [Calc note #8](../../history/documents/field-equation-notes.md) logged a residual mixing through the potential and expected it to be small "by compactness"; no document computes it. It is item 6 of the open problems in [checkpoint #11](../../history/documents/checkpoint.md) [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) [O].*

**Status:** Open — [O] — item 6 of [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems); logged in calc note [#8](../../../notes/beta-coefficients.md) ([`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) and [§5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)) with an expectation but no calculation; no `verify/` script; not on the current work queue. Listed in [Open problems and the queue](../../status/open-problems.md).

## The question

[#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems), item 6, in full: "τ–Stückelberg mixing matrix [O]."

The item asks for a matrix: the quadratic couplings between τ and the modes that X absorbs, and from them the combinations of fields that have definite masses. Its origin is a parenthesis at the end of calc note #8's derivation that τ is not eaten ([§3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t); see [The field-equation calc notes](../../history/documents/field-equation-notes.md)):

```text
(Residual τ–Stückelberg mixing through the potential: logged, expected small by compactness.)
```

The question qualifies the leading-order result [τ is not eaten](tau-not-eaten.md) [D — leading order], and through it the role that calc note [#7](../../../notes/tuning-test.md) gives τ in [constrained bimetric gravity](../tuning-test/constrained-bimetric.md): "the light direction of the compact space being τ (the dark-energy field) and the massive spin-2 being X" ([§4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural)).

## Background: Stückelberg fields and mixing [T]

When a gauge symmetry is broken spontaneously, its would-be Goldstone fields do not appear as massless particles. They become extra polarization states of the gauge field, which becomes massive: the Higgs mechanism ([Goldstone modes and the Higgs mechanism](../../symmetry-breaking/goldstone-and-higgs.md)) [T]. The [Stückelberg description](../../symmetry-breaking/stuckelberg-fields.md) keeps those fields in view. The massive field is written as a gauge field combined with the would-be Goldstone fields, now called Stückelberg fields, so that the gauge symmetry stays manifest. Choosing the unitary gauge sets the Stückelberg fields to zero, and they survive only as the massive field's extra polarizations; they are then said to be "eaten" [T].

For a massive spin-2 field the Stückelberg fields are a vector and a scalar. Of its five polarization states, the two of helicity ±2 belong to the tensor itself, the two of helicity ±1 to the vector and the one of helicity 0 to the scalar [T] (Arkani-Hamed, Georgi and Schwartz †; the review of massive gravity by Hinterbichler †).

Two fields mix when the quadratic part of the Lagrangian contains a term proportional to their product. Neither field then has a definite mass. The states of definite mass are combinations of the two, found by diagonalizing the matrix of quadratic couplings; that matrix, or the rotation that diagonalizes it, is the mixing matrix. When the off-diagonal entries are small compared with the difference of the diagonal ones, each mass state is mostly one of the original fields [T].

## The two sectors

### The modes X absorbs

X becomes massive through [the gravitational Higgs mechanism](gravitational-higgs.md). Its local shifts δX_μν = ∂₍μλ_ν₎ form a second copy of linearized diffeomorphisms ([dual diffeomorphisms](dual-diffeomorphisms.md)), and the vacuum's choice of polarization breaks them. Calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) [D — structural]: "the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a **massive spin-2** with its five polarizations". Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) words it differently: the Higgsing "eats the vector π_μ and the *longitudinal scalar of the λ-gradient sector*". No document reconciles the two wordings, and [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) follows #6 ("X eats the four Goldstones"). Either way, these are the Stückelberg modes of the item.

### τ

τ is the dark-energy field. It is a coordinate on [the Lagrangian Grassmannian Λ(d)](../../phase-space/modular-field/lagrangian-grassmannian.md), the compact space of possible [polarizations J](../../symmetry-breaking/order-parameter.md), and specifically its [Maslov phase](../../phase-space/modular-field/maslov-phase.md): "the dark-energy field τ is the Maslov phase of the boundary variable, its periodicity a fact of topology (π₁(U(d)/O(d)) = ℤ)" ([#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)). Its dynamics as [dark energy](../../cosmology/dark-energy/_index.md) are on [τ: hilltop quintessence on the Maslov circle](../../cosmology/dark-energy/tau-quintessence.md).

The leading-order argument separates τ from the absorbed modes by where each comes from. Calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural): "The Λ(d) moduli, τ included, are not the eaten modes — they carry the compact phase directions, which constant shifts do not generate". Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t): "τ is a J-modulus on the compact Λ(d), a different sector with different origin; it survives as the light field." [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) [D]: "τ un-eaten (compact J-sector, not the Stückelberg sector)."

### Where the sectors meet

#8 says the residual mixing arises "through the potential". The potential that gives X its mass is, in the field-equation notes, a [wedge polynomial](../spin-2-fields/vielbein-formulation.md) of two frames: the symplectic vielbein E and the polarization frame E₀[J] ([#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t); [the frame tier](../tuning-test/frame-tier.md)), written for the frames e and f = E₀[J] as V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏) ([#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d); [Hassan–Rosen bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md)). The second frame depends on J, and τ is one of J's moduli, so the potential involves both sectors. The notes write no formula for the mixing.

## What the leading-order result leaves open

#8 tags its result "[D — leading order]" and does not say what the expansion is in. "Residual" mixing is what lies beyond that order. The two documents that state an expectation, [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) and the superseded v1 paper, give the same one, "expected small by compactness", and neither gives the argument. The compactness meant is presumably that of Λ(d), which [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) calls compact in the same paragraph and on which τ is an angle; the absorbed modes come from the shifts of X, which do not generate the compact directions ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). How that difference would make the mixing small is not written down anywhere, and no document says what a large mixing would change.

## History of the item

- **Calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)** first raised τ's survival as a question: "verifying τ survives un-eaten is flagged [O]."
- **Calc note [#7 §5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem)** listed "(ii) τ-not-eaten verification" among the remaining items of [the field-equation problem](../../history/main-problems.md), with the note that "Items (ii)–(iv) are checks; item (i) is the substance."
- **Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)** derived "τ is not eaten [D — leading order]" and logged the residual mixing. Its close-out ([§5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)) lists "(iii) τ–Stückelberg mixing matrix" among the "Open residue, none of it existential" of the field-equation problem ([The three main problems](../../history/main-problems.md)).
- **The lab notebook's v0.6 addendum** carries the same list of "Residual open items (none existential)", including "τ–Stückelberg mixing" ([the lab notebook](../../history/documents/lab-notebook.md)).
- **The v1 paper ([#9](../../../notes/broken-born-program-v1.md)) [§10](../../../notes/broken-born-program-v1.md#10-open-problems), item 5**: "τ–Stückelberg mixing matrix; expected small by compactness [O]."
- **[#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems), item 6** keeps the item and drops the expectation: "τ–Stückelberg mixing matrix [O]."
- **The handoff's list of open problems** ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)) does not include it ([the handoff document](../../history/documents/handoff.md)).

## Priority

[#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) says "the word 'theory' still waits on items 1–3" of [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems): [deriving the wedge sector from S_H](../tuning-test/wedge-reduction.md), [the partially-massless comparison](../palindromic-branch/pm-comparison.md) and [the Lorentzian dressing](../../phase-space/born-geometry/lorentzian-dressing.md). Item 6 is not among them. The current queue in the root [`CLAUDE.md`](../../../CLAUDE.md) ("Since the handoff") is [`HANDOFF.md` §8 items 5–6](../../../HANDOFF.md#8-ranked-next-actions-queue) (the partially-massless comparison and [the † literature battery](../../method/literature-battery.md)), then an optional round-6 review of the [toy-model note](../../symmetry-breaking/toy-models/_index.md); item 7, [the phase-space-diameter note](../../cosmology/scale-factor-duality/phase-space-diameter.md), is done. The mixing matrix is not on the queue.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §14 item 6](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open problem as currently listed; [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) — τ un-eaten, "not the Stückelberg sector"; [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — τ as the Maslov phase; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — which items gate "theory"
- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — τ not eaten at leading order and the logged residual mixing; [§5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out) — the open residue of the field-equation problem; [§1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) — the potential for the frames e and f = E₀[J]
- [`notes/x-classification.md` §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — the eaten Goldstones, τ's survival first flagged [O]
- [`notes/tuning-test.md` §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — wedge polynomials of (E, E₀[J]); [§4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) — τ as the light direction of the compact space; [§5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem) — τ-not-eaten listed as a check
- [`notes/broken-born-program-v1.md` §10](../../../notes/broken-born-program-v1.md#10-open-problems) — the superseded v1 listing, "expected small by compactness"
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.6)' — the lab notebook's list of residual open items
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — the handoff's open list, which omits the item; [§8](../../../HANDOFF.md#8-ranked-next-actions-queue) — the queue items the root [`CLAUDE.md`](../../../CLAUDE.md) adopts
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the current queue
