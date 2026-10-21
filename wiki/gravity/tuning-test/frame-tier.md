---
title: "The frame tier: the symplectic vielbein"
weight: 30
status: alive
description: "Wedge polynomials of the symplectic vielbein E (H = EᵀE) and the polarization frame E₀[J] are exactly the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic — selected, not derived."
provenance: [D, T]
sources:
  - "notes/debt1a-iii-tuning-test.md §3"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "papers/broken-born-checkpoint-v2.md §14 item 1"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §5"
---

*The frame tier is the reformulation that rescues the tuning test: the momentum graviton's mass term is built from frames (vielbeins), the first-order variables from which a metric is assembled as H = EᵀE, instead of from metrics. In frame variables the ghost-free spin-2 potentials are plain polynomials, wedge products of two frames in the form found by Hinterbichler and Rosen ([vielbein formulation](/wiki/gravity/spin-2-fields/vielbein-formulation)), and the program has a natural frame-level object, the symplectic vielbein E, which sits at the same first-order level as the polarization J. Coupling E linearly to the polarization frame E₀[J] lands exactly in the ghost-free class, with the Fierz–Pauli structure automatic. The claim is structural and rests on literature [D — structural, resting on T]; the class was selected by minimality and consistency rather than derived from the geometric action, which is an open problem.*

**Status:** Alive — [D — structural, resting on T] in calc note #7 (`notes/debt1a-iii-tuning-test.md` §3); part of [checkpoint #11](/wiki/history/documents/checkpoint) §7.2, which is tagged [D][V], but no battery test covers the frame tier. The derivation from S_H is [Open: deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction), item 1 of #11 §14.

## Key facts

- Calc note #7 §3 (see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)): "The rescue is not a tuning but a tier change. In vielbein variables the ghost-free potentials are polynomial — wedge products ε(e ∧ … ∧ f ∧ …) of two frames (Hinterbichler–Rosen) [T] — with no square roots and no tuning to miss."
- The program's frame-tier object (#7 §3): "the symplectic vielbein E, the coset representative with H = EᵀE", and "J and E live on the same geometric tier (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order." The connection is [the Born connection](/wiki/phase-space/born-geometry/born-connection).
- The landing (#7 §3): "The geometrically minimal coupling of the polarization to the modular sector is therefore E-linear — wedge polynomials of (E, E₀[J]) — which is precisely the Hinterbichler–Rosen class: ghost-free by construction, Fierz–Pauli automatic, dRGT structure inherited rather than tuned." dRGT is de Rham–Gabadadze–Tolley ([dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity)).
- #11 §7.2: "Frame-tier couplings — wedge polynomials of the symplectic vielbein E (H = EᵀE) with the polarization frame E₀[J] — are the Hinterbichler–Rosen class [12†], ghost-free by construction; J, E, and the Born connection share the first-order tier, so this is the geometrically minimal formulation." The † marks a citation from model memory, not yet checked against the source.
- What the frame tier yields, calc note #8 §1: "The Hinterbichler–Rosen sector for (e, f = E₀[J]) is V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏), 𝕏 = √(g⁻¹f), with the exchange identity Sₙ(g,f) = S₄₋ₙ(f,g)." This is the [Hassan–Rosen potential](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) that reciprocity then restricts ([The palindromic branch](/wiki/gravity/palindromic-branch)).
- Selected, not derived: #11 §14 item 1, "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]"; #8 §5, "the class was selected by minimality + consistency, not derived line-by-line".
- Verification scope: the battery's tests T3, T4 and T7 check the block algebra and the metric-tier failures ([The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)); the frame-tier claim has no test and stays [D — structural, resting on T]. Its place in the outcome is [The verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass).

## Sources

- `notes/debt1a-iii-tuning-test.md` §3 — the frame tier [D — structural, resting on T]
- `papers/broken-born-checkpoint-v2.md` §7.2 — the current statement and the [12†] citation; §14 item 1 for the open derivation
- `notes/debt1a-iv-beta-coefficients.md` §1 — the resulting wedge potential; §5 for "selected by minimality + consistency"
