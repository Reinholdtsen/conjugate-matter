---
title: "Constrained bimetric gravity"
weight: 50
status: alive
description: "The picture that emerges: Hassan–Rosen bimetric gravity with the second frame confined to the ten compact moduli of Λ(d), τ the light direction and X the massive spin-2."
provenance: [D]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §1"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.5"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 6"
  - "wiki/papers/broken-born-checkpoint-v2.md §14"
  - "notes/tuning-test.md §4"
  - "notes/tuning-test.md §3"
  - "notes/tuning-test.md §5"
  - "notes/x-classification.md §3"
  - "notes/beta-coefficients.md §1"
  - "notes/beta-coefficients.md §3"
  - "notes/beta-coefficients.md §4"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §D"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/knot-dark-matter-standalone.md §1"
  - "HANDOFF.md §2"
  - "review/wiki-build-flags.md item 8"
  - "notes/closed-universe.md §6"
  - "review/round5-adjudication.md 'Rulings' R1"
---

*Constrained bimetric gravity is the picture of the program's gravity that [the tuning test](_index.md) leaves. [Hassan–Rosen bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md) is a [ghost-free](../spin-2-fields/ghosts.md) theory of two interacting metrics, each with its own dynamics. In the program's version the second frame is not a free field: it is the polarization frame, built from the [polarization J](../../symmetry-breaking/order-parameter.md), and J ranges only over the compact space [Λ(d)](../../phase-space/modular-field/lagrangian-grassmannian.md) of splittings of phase space into position and momentum, which is ten-dimensional at d = 4. [Calc note #7](../../history/documents/field-equation-notes.md) calls the result a predictive truncation of bimetric theory, with fewer free functions. In it the massless combination of the two spin-2 fields is the ordinary graviton, the massive one is the [momentum graviton X](../momentum-graviton/_index.md), and the light direction of the compact space is the [dark-energy field τ](../../phase-space/modular-field/maslov-phase.md). [Reciprocity](../../phase-space/reciprocity/born-reciprocity.md) then restricts the potential to its [palindromic branch](../palindromic-branch/_index.md), and with the condition for a flat vacuum two free parameters remain. The picture is a structural derivation; the standard bimetric facts it uses come from the literature, and nothing in it is machine-checked.*

**Status:** Alive — [D — structural] in calc note [#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural), with the standard bimetric facts [T] — not machine-checked; carried into the technical abstract ([§1](../../../notes/tuning-test.md#1-the-object-to-test)) and §7 of [checkpoint #11](../../history/documents/checkpoint.md) with d = 4, as Λ(4).

## The claim

Calc note #7 ([the field-equation calc notes](../../history/documents/field-equation-notes.md)) heads its §4 "The picture that emerges: constrained bimetric gravity [D — structural]":

> J carries only the 10 compact moduli of U(d)/O(d) — not a full second metric. So the "second vielbein" E₀[J] is confined to a compact 10-dimensional moduli space. BBT's geometric sector is therefore

> **Hassan–Rosen bimetric gravity with the second frame constrained to a compact moduli space Λ(d)** — a *predictive truncation* of bimetric theory: fewer free functions, with the light direction of the compact space being τ (the dark-energy field) and the massive spin-2 being X.

BBT is Broken-Born theory, the program's earlier name. Checkpoint [#11](../../papers/broken-born-checkpoint-v2.md) states the current form in its technical abstract: a chain of structural results "forces X to be a **massive spin-2** field in the interchange-symmetric branch of Hassan–Rosen bimetric gravity [10†, 11†] with the second frame confined to Λ(4)" ([#11 §1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts)). The interchange-symmetric branch is the restriction that reciprocity adds afterwards ([the palindrome βₙ = β₄₋ₙ](../palindromic-branch/palindrome.md)).

## Bimetric gravity [T]

Hassan–Rosen bimetric gravity has two dynamical metrics, g and f, each with its own Einstein–Hilbert kinetic term. They interact through a potential that is a linear combination of the [elementary symmetric polynomials](../spin-2-fields/elementary-symmetric-polynomials.md) eₙ of the matrix √(g⁻¹f), with constant coefficients βₙ, the form that avoids the Boulware–Deser ghost ([Hassan–Rosen bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md); [the Fierz–Pauli mass term and the Boulware–Deser ghost](../spin-2-fields/fierz-pauli.md)). #11 cites the theory from model memory as [10†, 11†]. In the general theory the second metric is a full dynamical field in its own right, with its own value at each point, and the potential has five constant coefficients, β₀ to β₄.

[#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) takes over the theory's spectrum: "Standard bimetric facts then slot in [T]: one massless combination (our graviton, coupling to SM stress) and one massive (X)". SM is the Standard Model. The fluctuation of each metric is a mixture of the two mass eigenstates, one massless spin-2 field and one massive.

## Why the second frame is confined [D — structural]

The argument has three steps, each in the notes.

1. **The second frame is a polarization frame.** In the frame tier the passing potential is a wedge polynomial of the symplectic vielbein E and the polarization frame E₀[J] ([#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t); [the frame tier](frame-tier.md)). In calc note [#8](../../../notes/beta-coefficients.md)'s notation the two frames of the bimetric potential are "(e, f = E₀[J])" ([#8 §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d)). The second frame is a function of J alone.
2. **J lives on the Lagrangian Grassmannian.** Calc note [#5](../../../notes/geometric-core.md): "The space of H-compatible real structures on (ℝ^{2d}, I) is {J} ≅ U(d)/O(d) = Λ(d), the Lagrangian Grassmannian" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). The lab notebook gives its size: "compact, of dimension d(d+1)/2 = 10 for d=4" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)). A compact space is closed and bounded, like a circle or a sphere [T].
3. **So the second sector is truncated.** A free second metric is replaced by a frame that moves only over this compact space: "not a full second metric" ([#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural)). #7 calls this "a *predictive truncation* of bimetric theory: fewer free functions".

The notes write Λ(d). #11 writes Λ(4) where it confines the second frame ([§1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts), [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)) and Λ(d) for the Grassmannian in general ([§1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts), [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)). They agree at d = 4, the physical case ([the Lagrangian Grassmannian Λ(d)](../../phase-space/modular-field/lagrangian-grassmannian.md)).

## What fills the picture

- **The massless combination: the graviton.** It couples to the stress of Standard Model matter ([#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural)). Reciprocity later identifies it as the reciprocity-even combination, which is exactly massless ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t); [Row 6: the exactly massless graviton](../../predictions/massless-graviton.md); on the parity under [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)'s Z → −Z⁻¹, see flag 39 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).
- **The massive combination: X.** The momentum graviton, the real part of [the modular field](../../phase-space/modular-field/modular-field-z.md) Z, acquires its mass when the vacuum's choice of polarization breaks its gauge symmetry, with "M_X = the polarization-breaking scale" ([#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t); [the gravitational Higgs mechanism](../momentum-graviton/gravitational-higgs.md)).
- **The light direction: τ.** τ is [the Maslov phase](../../phase-space/modular-field/maslov-phase.md), the angle along the one circle direction of Λ(d). It is not among the modes that X absorbs in acquiring its mass: "τ is a J-modulus on the compact Λ(d), a different sector with different origin; it survives as the light field" ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t), [D — leading order]; [τ is not eaten](../momentum-graviton/tau-not-eaten.md)). Calc note [#6](../../../notes/x-classification.md) had flagged this as a check still to be made ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)).
- **The other nine directions.** That τ is the lightest modulus, "with the other nine directions heavy, is assumed [P]" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)). Calc note #5 expected [constraints of the inverse-Higgs type](../../symmetry-breaking/inverse-higgs-constraints.md) to "likely eliminate most" of the nine [O] ([#5 §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)); no later document works this out ([Open: field content of the broken vacuum](../../phase-space/modular-field/field-content.md)).

## How far the truncation goes

Calc note #8 quantifies the truncation once reciprocity has acted ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t), tagged [D + T]):

> **Parameter count:** five βₙ → palindrome (−2) → T = 0 (−1) → **two**: the Fierz–Pauli mass combination m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**, and one orthogonal shape parameter controlling cubic interactions. The "predictive truncation" of Chunk A-iii is now quantified: HR bimetric's five-function freedom collapses to two numbers.

HR is Hassan–Rosen, and Chunk A-iii is calc note #7; on "five-function freedom", see flag 8 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md). The palindrome βₙ = β₄₋ₙ removes two coefficients, and the condition T = 0 from a flat aligned vacuum removes one more ([the palindrome](../palindromic-branch/palindrome.md); [the vacuum-energy identity](../palindromic-branch/vacuum-energy-identity.md)). [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) carries the count, "Five βₙ → two parameters", tagged [D] ([spectrum, parameters and reciprocity parity](../momentum-graviton/spectrum-and-parity.md)).

## Superseded: safety through a dominant massless combination

[#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) went on to say how ordinary matter is protected from X: "safety requires the massless combination to dominate SM couplings — a parametric check to log", together with the bounds on a graviton mass from gravitational-wave observations, "m_g ≲ 10⁻²³ eV territory", read as a bound on the mixing angle.

Calc note #8 replaced this reading. "With equal effective Planck masses (forced by the same symmetry), SM matter — coupled to g — sees both eigenstates with comparable strength; safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X, and gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X" ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t); [Yukawa forces](../spin-2-fields/yukawa-forces.md#the-momentum-graviton-x)). The graviton-mass bounds from gravitational waves apply to the reciprocity-even eigenstate, which is exactly massless, so they hold identically rather than constraining a mixing angle ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t); [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) and [§13 row 6](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)). The current argument is on [safety by range](../momentum-graviton/fifth-force-safety.md).

## Before the test: the conditional form

Calc note #6 had stated the picture with a condition attached ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)):

> Restated as a selling line: **BBT's geometric sector is bimetric gravity with the second metric's kinetic structure and couplings dictated by modular (Siegel-domain) symmetry rather than chosen by hand** — *if* the dRGT tuning emerges from the symmetry.

dRGT is de Rham–Gabadadze–Tolley ([dRGT massive gravity](../spin-2-fields/drgt-massive-gravity.md)). The note adds that "bimetric gravity was the right neighborhood from the start; the modular structure explains *which* bimetric." The tuning test met the condition in frame variables, which is the sense of its conditional pass ([the verdict: a conditional pass](conditional-pass.md)). [#7 §5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem) then records "the resulting physical picture (constrained HR bimetric with compact second sector)" as "sharper and more predictive than generic bimetric gravity".

## Scope and what is open

- **Structural, not computed.** The picture is [D — structural] and the bimetric facts [T]; no [battery](../../method/verification/battery.md) test covers it. #11 cites the bimetric literature from model memory, pending the literature check ([Open: the † literature battery (OP10)](../../method/literature-battery.md)).
- **The second frame is selected.** The frame-tier potential that defines the coupling was selected by minimality and consistency, not derived from the geometric action ([Open: deriving the wedge sector from S_H (OP1)](wedge-reduction.md)). No document writes E₀[J] out explicitly. Whether it is a frozen background is unsettled as well: the record never defines it "beyond 'the polarization frame' on compact moduli", and the closed-universe note, which takes f as dynamical at equal Planck masses, finds that a frozen f contradicts them, while round-5 ruling R1 holds the question open ([`notes/closed-universe.md` §6](../../../notes/closed-universe.md#6-the-momentum-graviton-x-in-a-closed-universe); [if f were frozen](../momentum-graviton/closed-universe.md#if-f-were-frozen-dv)).
- **Euclidean skeleton.** The field-equation results are derived for a positive-definite metric ([Open: Lorentzian dressing (OP3)](../../phase-space/born-geometry/lorentzian-dressing.md)).
- **τ and the eaten modes.** Residual mixing of τ with the modes X absorbs is open problem 6, "τ–Stückelberg mixing matrix [O]" ([#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems); [Open: τ–Stückelberg mixing (OP6)](../momentum-graviton/tau-stuckelberg-mixing.md)).
- **[Equal Planck masses](../spin-2-fields/planck-units.md#equal-planck-masses-in-the-bimetric-sector).** The symmetry that fixes the branch also forces "equal effective Planck masses" for the two metrics ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)). The standalone manuscript [#14](../../../notes/knot-dark-matter-standalone.md), since withdrawn for unrelated reasons ([Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md)), lists "the stability of a heavy spin-2 field at equal Planck masses" as "an open consistency condition" ([#14 §1](../../../notes/knot-dark-matter-standalone.md#1-framework)). [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) does not list it ([Open: stability at equal Planck masses](../momentum-graviton/equal-planck-mass-stability.md)).

## History

- **Calc note #6 and the v0.4 addendum**: the conditional form, "bimetric gravity with structure dictated by modular symmetry" (notebook 'Addendum (v0.4)').
- **Calc note #7 and the v0.5 addendum**: "BBT's geometric sector is **Hassan–Rosen bimetric gravity with the second frame confined to the compact moduli space Λ(d)** — a predictive truncation of bimetric theory. One massless graviton (ours), one massive spin-2 (X), and the compact sector's light direction is τ" ([the lab notebook](../../history/documents/lab-notebook.md)).
- **Calc note #8 and the v0.6 addendum**: the truncation quantified, and the picture folded into the program's answer to Born: X's "self-consistent dynamics is Hassan–Rosen bimetric gravity restricted to the reciprocity-symmetric branch with the second frame confined to the compact moduli space Λ(d)" ([#8 §4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born); [Born's answer](../momentum-graviton/borns-answer.md)).
- **The v1 program paper and checkpoint #11** write Λ(4): "the reciprocity-symmetric branch of Hassan–Rosen bimetric with the second frame confined to the compact Λ(4)" ([#9 §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved)) and "the reciprocity-symmetric branch of bimetric gravity with the second frame confined to compact Λ(4)" ([#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)).
- **The handoff**: "Geometric sector = interchange-symmetric (palindromic βₙ = β₄₋ₙ) Hassan–Rosen bimetric, second frame confined to compact Λ(4)" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen); [the handoff](../../history/documents/handoff.md)).

## Sources

- [`notes/tuning-test.md` §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) — the picture [D — structural], the bimetric facts [T] and the superseded safety reading; [§3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — the polarization frame in the frame tier; [§5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem) — "sharper and more predictive".
- [`wiki/papers/broken-born-checkpoint-v2.md` §1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts), [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) — the current statement with Λ(4); [§7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — M_X; [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) and [§13 row 6](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the two parameters and the massless even eigenstate; [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — open problem 6.
- [`notes/x-classification.md` §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — the conditional form before the test; τ un-eaten flagged.
- [`notes/beta-coefficients.md` §1](../../../notes/beta-coefficients.md#1-what-reciprocity-does-to-the-wedge-potential-d) — the two frames (e, f = E₀[J]); [§3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — the parameter count, equal Planck masses, safety by range and τ not eaten; [§4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born) — Born's answer with Λ(d).
- [`notes/geometric-core.md` §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural) — the space of real structures is Λ(d); [§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) — the ten σ-modes.
- [`notes/broken-born-theory.md` §2](../../../notes/broken-born-theory.md#2-kinematic-core) — Λ(d) compact, of dimension 10 for d = 4, and the nine heavy directions assumed; 'Addendum (v0.4)', 'Addendum (v0.5)', 'Addendum (v0.6)' — the notebook's statements.
- [`notes/broken-born-program-v1.md` §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) — the v1 statement with Λ(4).
- [`notes/knot-dark-matter-standalone.md` §1](../../../notes/knot-dark-matter-standalone.md#1-framework) — stability at equal Planck masses as an open condition.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — the handoff's one-screen statement.
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 8 — "five-function" for five constant coefficients; pending.
- [`notes/closed-universe.md` §6](../../../notes/closed-universe.md#6-the-momentum-graviton-x-in-a-closed-universe) and [`review/round5-adjudication.md`](../../../review/round5-adjudication.md) 'Rulings' R1 — f taken as dynamical, a frozen f against the record's equal Planck masses, and E₀[J] left undefined.
