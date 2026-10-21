---
title: "Vielbein formulation and wedge potentials"
weight: 70
status: established
description: "First-order (frame) variables for gravity, and Hinterbichler–Rosen's interacting spin-2 potentials written as wedge products of frames, ghost-free by construction."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md ref [12]"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §5"
---

*In the vielbein, or frame, formulation of gravity the basic variable is a frame field e, a set of local reference axes at each point, from which the metric is built as a quadratic expression. The program calls frames first-order variables and metrics, being quadratic in frames, second-order. Hinterbichler and Rosen showed that potentials coupling two spin-2 fields can be written as wedge products of their two frames, polynomials with no matrix square roots, and that these are free of the Boulware–Deser ghost by construction. The program's [tuning test](/wiki/gravity/tuning-test) passed only in this form: the potential that gives the [momentum graviton X](/wiki/gravity/momentum-graviton) its mass is ghost-free when written with frames, and not when written with metrics.*

**Status:** Established — [T] — Hinterbichler–Rosen is cited in the [checkpoint](/wiki/history/documents/checkpoint) as [12†], from model memory. [#7](/wiki/history/documents/debt-1-notes) §3 tags the program's use "[D — structural, resting on T]"; that the program's potential lies in this class is not machine-checked, and was selected rather than derived.

## Key facts

- #7 §3 [T]: "In vielbein variables the ghost-free potentials are polynomial — wedge products ε(e ∧ … ∧ f ∧ …) of two frames (Hinterbichler–Rosen) [T] — with no square roots and no tuning to miss."
- Reference [12†] (#11): K. Hinterbichler, R. A. Rosen, "Interacting spin-2 fields," JHEP 1207, 047 (2012), arXiv:1203.5783.
- The program's frame (#7 §3): "the symplectic vielbein E, the coset representative with H = EᵀE"; "J and E live on the same geometric tier (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order." See [the frame tier](/wiki/gravity/tuning-test/frame-tier) and [the Born connection](/wiki/phase-space/born-geometry/born-connection).
- The checkpoint (#11 §7.2): "Frame-tier couplings — wedge polynomials of the symplectic vielbein E (H = EᵀE) with the polarization frame E₀[J] — are the Hinterbichler–Rosen class [12†], ghost-free by construction".
- The class is "ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned" (#7 §3); see [the Fierz–Pauli mass term](/wiki/gravity/spin-2-fields/fierz-pauli) and [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity).
- #8 §1 writes the program's wedge sector for the frames (e, f = E₀[J]) as the [Hassan–Rosen potential](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric), which is where reciprocity then acts ([the palindrome](/wiki/gravity/palindromic-branch/palindrome)).
- Open: "the class was selected by minimality + consistency, not derived line-by-line" (#8 §5); see [deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction).

## Used by

- [The frame tier: the symplectic vielbein](/wiki/gravity/tuning-test/frame-tier) — the formulation in which the potential passes.
- [The verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass) — the theory passes iff written in first-order variables.
- [Open: deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction) — the class was selected, not derived.
- [The palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) — reciprocity acting on the wedge sector.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.2, ref [12] — the frame-tier couplings as the Hinterbichler–Rosen class; the citation, marked †.
- `notes/debt1a-iii-tuning-test.md` §3 — wedge potentials, the symplectic vielbein and the first-order tier.
- `notes/debt1a-iv-beta-coefficients.md` §1, §5 — the wedge sector as a Hassan–Rosen potential; the class selected, not derived.
