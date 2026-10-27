---
title: "Constrained bimetric gravity"
weight: 50
status: alive
description: "The picture that emerges: Hassan–Rosen bimetric gravity with the second frame confined to the ten compact moduli of Λ(d), τ the light direction and X the massive spin-2."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §13 row 6"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iii-tuning-test.md §5"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §4"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/knot-dark-matter-standalone.md §1"
  - "HANDOFF.md §2"
  - "review/wiki-build-flags.md item 8"
---

*Constrained bimetric gravity is the picture of the program's gravity that [the tuning test](/wiki/gravity/tuning-test) leaves. [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) is a [ghost-free](/wiki/gravity/spin-2-fields/ghosts) theory of two interacting metrics, each with its own dynamics. In the program's version the second frame is not a free field: it is the polarization frame, built from the [polarization J](/wiki/symmetry-breaking/order-parameter), and J ranges only over the compact space [Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian) of splittings of phase space into position and momentum, which is ten-dimensional at d = 4. [Calc note #7](/wiki/history/documents/debt-1-notes) calls the result a predictive truncation of bimetric theory, with fewer free functions. In it the massless combination of the two spin-2 fields is the ordinary graviton, the massive one is the [momentum graviton X](/wiki/gravity/momentum-graviton), and the light direction of the compact space is the [dark-energy field τ](/wiki/phase-space/modular-field/maslov-phase). [Reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) then restricts the potential to its [palindromic branch](/wiki/gravity/palindromic-branch), and with the condition for a flat vacuum two free parameters remain. The picture is a structural derivation; the standard bimetric facts it uses come from the literature, and nothing in it is machine-checked.*

**Status:** Alive — [D — structural] in calc note #7 §4, with the standard bimetric facts [T] — not machine-checked; carried into the technical abstract (§1) and §7 of [checkpoint #11](/wiki/history/documents/checkpoint) with d = 4, as Λ(4).

## The claim

Calc note #7 ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)) heads its §4 "The picture that emerges: constrained bimetric gravity [D — structural]":

> J carries only the 10 compact moduli of U(d)/O(d) — not a full second metric. So the "second vielbein" E₀[J] is confined to a compact 10-dimensional moduli space. BBT's geometric sector is therefore

> **Hassan–Rosen bimetric gravity with the second frame constrained to a compact moduli space Λ(d)** — a *predictive truncation* of bimetric theory: fewer free functions, with the light direction of the compact space being τ (the dark-energy field) and the massive spin-2 being X.

BBT is Broken-Born theory, the program's earlier name. Checkpoint #11 states the current form in its technical abstract: a chain of structural results "forces X to be a **massive spin-2** field in the interchange-symmetric branch of Hassan–Rosen bimetric gravity [10†, 11†] with the second frame confined to Λ(4)" (#11 §1). The interchange-symmetric branch is the restriction that reciprocity adds afterwards ([the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome)).

## Bimetric gravity [T]

Hassan–Rosen bimetric gravity has two dynamical metrics, g and f, each with its own Einstein–Hilbert kinetic term. They interact through a potential that is a linear combination of the [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials) eₙ of the matrix √(g⁻¹f), with constant coefficients βₙ, the form that avoids the Boulware–Deser ghost ([Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric); [the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)). #11 cites the theory from model memory as [10†, 11†]. In the general theory the second metric is a full dynamical field in its own right, with its own value at each point, and the potential has five constant coefficients, β₀ to β₄.

#7 §4 takes over the theory's spectrum: "Standard bimetric facts then slot in [T]: one massless combination (our graviton, coupling to SM stress) and one massive (X)". SM is the Standard Model. The fluctuation of each metric is a mixture of the two mass eigenstates, one massless spin-2 field and one massive.

## Why the second frame is confined [D — structural]

The argument has three steps, each in the notes.

1. **The second frame is a polarization frame.** In the frame tier the passing potential is a wedge polynomial of the symplectic vielbein E and the polarization frame E₀[J] (#7 §3; [the frame tier](/wiki/gravity/tuning-test/frame-tier)). In calc note #8's notation the two frames of the bimetric potential are "(e, f = E₀[J])" (#8 §1). The second frame is a function of J alone.
2. **J lives on the Lagrangian Grassmannian.** Calc note #5: "The space of H-compatible real structures on (ℝ^{2d}, I) is {J} ≅ U(d)/O(d) = Λ(d), the Lagrangian Grassmannian" (#5 §B). The lab notebook gives its size: "compact, of dimension d(d+1)/2 = 10 for d=4" (#1 §2). A compact space is closed and bounded, like a circle or a sphere [T].
3. **So the second sector is truncated.** A free second metric is replaced by a frame that moves only over this compact space: "not a full second metric" (#7 §4). #7 calls this "a *predictive truncation* of bimetric theory: fewer free functions".

The notes write Λ(d). #11 writes Λ(4) where it confines the second frame (§1, §7) and Λ(d) for the Grassmannian in general (§1, §6). They agree at d = 4, the physical case ([the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian)).

## What fills the picture

- **The massless combination: the graviton.** It couples to the stress of Standard Model matter (#7 §4). Reciprocity later identifies it as the reciprocity-even combination, which is exactly massless (#8 §3; [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton); on the parity under #11 §6's Z → −Z⁻¹, see flag 39 in `review/wiki-build-flags.md`).
- **The massive combination: X.** The momentum graviton, the real part of [the modular field](/wiki/phase-space/modular-field/modular-field-z) Z, acquires its mass when the vacuum's choice of polarization breaks its gauge symmetry, with "M_X = the polarization-breaking scale" (#11 §7.1; [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).
- **The light direction: τ.** τ is [the Maslov phase](/wiki/phase-space/modular-field/maslov-phase), the angle along the one circle direction of Λ(d). It is not among the modes that X absorbs in acquiring its mass: "τ is a J-modulus on the compact Λ(d), a different sector with different origin; it survives as the light field" (#8 §3, [D — leading order]; [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten)). Calc note #6 had flagged this as a check still to be made (#6 §3).
- **The other nine directions.** That τ is the lightest modulus, "with the other nine directions heavy, is assumed [P]" (#1 §2). Calc note #5 expected [constraints of the inverse-Higgs type](/wiki/symmetry-breaking/inverse-higgs-constraints) to "likely eliminate most" of the nine [O] (#5 §D); no later document works this out ([Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content)).

## How far the truncation goes

Calc note #8 quantifies the truncation once reciprocity has acted (#8 §3, tagged [D + T]):

> **Parameter count:** five βₙ → palindrome (−2) → T = 0 (−1) → **two**: the Fierz–Pauli mass combination m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**, and one orthogonal shape parameter controlling cubic interactions. The "predictive truncation" of Chunk A-iii is now quantified: HR bimetric's five-function freedom collapses to two numbers.

HR is Hassan–Rosen, and Chunk A-iii is calc note #7; on "five-function freedom", see flag 8 in `review/wiki-build-flags.md`. The palindrome βₙ = β₄₋ₙ removes two coefficients, and the condition T = 0 from a flat aligned vacuum removes one more ([the palindrome](/wiki/gravity/palindromic-branch/palindrome); [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)). #11 §7.5 carries the count, "Five βₙ → two parameters", tagged [D] ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)).

## Superseded: safety through a dominant massless combination

#7 §4 went on to say how ordinary matter is protected from X: "safety requires the massless combination to dominate SM couplings — a parametric check to log", together with the bounds on a graviton mass from gravitational-wave observations, "m_g ≲ 10⁻²³ eV territory", read as a bound on the mixing angle.

Calc note #8 replaced this reading. "With equal effective Planck masses (forced by the same symmetry), SM matter — coupled to g — sees both eigenstates with comparable strength; safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X, and gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X" (#8 §3; [Yukawa forces](/wiki/gravity/spin-2-fields/yukawa-forces#the-momentum-graviton-x)). The graviton-mass bounds from gravitational waves apply to the reciprocity-even eigenstate, which is exactly massless, so they hold identically rather than constraining a mixing angle (#8 §3; #11 §7.5 and §13 row 6). The current argument is on [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety).

## Before the test: the conditional form

Calc note #6 had stated the picture with a condition attached (#6 §3):

> Restated as a selling line: **BBT's geometric sector is bimetric gravity with the second metric's kinetic structure and couplings dictated by modular (Siegel-domain) symmetry rather than chosen by hand** — *if* the dRGT tuning emerges from the symmetry.

dRGT is de Rham–Gabadadze–Tolley ([dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity)). The note adds that "bimetric gravity was the right neighborhood from the start; the modular structure explains *which* bimetric." The tuning test met the condition in frame variables, which is the sense of its conditional pass ([the verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass)). #7 §5 then records "the resulting physical picture (constrained HR bimetric with compact second sector)" as "sharper and more predictive than generic bimetric gravity".

## Scope and what is open

- **Structural, not computed.** The picture is [D — structural] and the bimetric facts [T]; no [battery](/wiki/method/verification/battery) test covers it. #11 cites the bimetric literature from model memory, pending the literature check ([Open: the † literature battery (OP10)](/wiki/method/literature-battery)).
- **The second frame is selected.** The frame-tier potential that defines the coupling was selected by minimality and consistency, not derived from the geometric action ([Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)). No document writes E₀[J] out explicitly.
- **Euclidean skeleton.** The Debt-1 results are derived for a positive-definite metric ([Open: Lorentzian dressing (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).
- **τ and the eaten modes.** Residual mixing of τ with the modes X absorbs is open problem 6, "τ–Stückelberg mixing matrix [O]" (#11 §14; [Open: τ–Stückelberg mixing (OP6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing)).
- **[Equal Planck masses](/wiki/gravity/spin-2-fields/planck-units#equal-planck-masses-in-the-bimetric-sector).** The symmetry that fixes the branch also forces "equal effective Planck masses" for the two metrics (#8 §3). The standalone manuscript #14, since withdrawn for unrelated reasons ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)), lists "the stability of a heavy spin-2 field at equal Planck masses" as "an open consistency condition" (#14 §1). #11 §14 does not list it ([Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)).

## History

- **Calc note #6 and the v0.4 addendum**: the conditional form, "bimetric gravity with structure dictated by modular symmetry" (notebook 'Addendum (v0.4)').
- **Calc note #7 and the v0.5 addendum**: "BBT's geometric sector is **Hassan–Rosen bimetric gravity with the second frame confined to the compact moduli space Λ(d)** — a predictive truncation of bimetric theory. One massless graviton (ours), one massive spin-2 (X), and the compact sector's light direction is τ" ([the lab notebook](/wiki/history/documents/lab-notebook)).
- **Calc note #8 and the v0.6 addendum**: the truncation quantified, and the picture folded into the program's answer to Born: X's "self-consistent dynamics is Hassan–Rosen bimetric gravity restricted to the reciprocity-symmetric branch with the second frame confined to the compact moduli space Λ(d)" (#8 §4; [Born's answer](/wiki/gravity/momentum-graviton/borns-answer)).
- **The v1 program paper and checkpoint #11** write Λ(4): "the reciprocity-symmetric branch of Hassan–Rosen bimetric with the second frame confined to the compact Λ(4)" (#9 §5) and "the reciprocity-symmetric branch of bimetric gravity with the second frame confined to compact Λ(4)" (#11 §7).
- **The handoff**: "Geometric sector = interchange-symmetric (palindromic βₙ = β₄₋ₙ) Hassan–Rosen bimetric, second frame confined to compact Λ(4)" (`HANDOFF.md` §2; [the handoff](/wiki/history/documents/handoff)).

## Sources

- `notes/debt1a-iii-tuning-test.md` §4 — the picture [D — structural], the bimetric facts [T] and the superseded safety reading; §3 — the polarization frame in the frame tier; §5 — "sharper and more predictive".
- `papers/broken-born-checkpoint-v2.md` §1, §7 — the current statement with Λ(4); §7.1 — M_X; §7.5 and §13 row 6 — the two parameters and the massless even eigenstate; §14 — open problem 6.
- `notes/debt1a-ii-X-classification.md` §3 — the conditional form before the test; τ un-eaten flagged.
- `notes/debt1a-iv-beta-coefficients.md` §1 — the two frames (e, f = E₀[J]); §3 — the parameter count, equal Planck masses, safety by range and τ not eaten; §4 — Born's answer with Λ(d).
- `notes/debt1a-geometric-core.md` §B — the space of real structures is Λ(d); §D — the ten σ-modes.
- `notes/broken-born-theory.md` §2 — Λ(d) compact, of dimension 10 for d = 4, and the nine heavy directions assumed; 'Addendum (v0.4)', 'Addendum (v0.5)', 'Addendum (v0.6)' — the notebook's statements.
- `notes/broken-born-program-v1.md` §5 — the v1 statement with Λ(4).
- `notes/knot-dark-matter-standalone.md` §1 — stability at equal Planck masses as an open condition.
- `HANDOFF.md` §2 — the handoff's one-screen statement.
- `review/wiki-build-flags.md` item 8 — "five-function" for five constant coefficients; awaiting Paul's ruling.
