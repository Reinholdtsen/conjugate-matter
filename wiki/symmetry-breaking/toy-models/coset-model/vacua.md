---
title: "Model I vacua, the order parameter and the Goldstone spectrum"
weight: 30
status: alive
description: "Vacua K(φ) on a circle times the half-plane; ρ maps K(φ) to −K(φ), the stabilizer is {±1}, O = K₁₁ flips sign, and three flat directions remain, the compact one parametrizing Λ(1)."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §2"
  - "verify/toy_coset.py S2"
  - "verify/toy_coset.py S3"
  - "verify/toy_coset.py 'Spectrum'"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "papers/broken-born-checkpoint-v2.md §10"
---

*The vacua of model I are its lowest-energy configurations: constant fields H and K that are compatible, so that the potential vanishes. They form a three-dimensional family, the upper half-plane of metrics times a circle of real structures, and [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) carries each vacuum to a different one, so no vacuum is symmetric (criterion S2). The entry K₁₁ of the real structure takes opposite signs in a vacuum and in its image, which makes it an order parameter (criterion S3). The circle is the polarization angle: moving along it rotates which line of the phase plane counts as position, at no cost in energy, and checkpoint #11 identifies it with the circle of its dark-energy field τ.*

**Status:** Alive — [V] (criteria S2 and S3 and the spectrum, in `verify/toy_coset.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — confirmed by the round-4 referee; what the breaking means physically is qualified by [the twisted element](/wiki/symmetry-breaking/twisted-element).

## Key facts

- **The vacuum circle.** "At H = 1 the vacua are K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]. The vacuum manifold is the upper half-plane times this circle." The worklog: "a 3-dimensional space".
- **How ρ acts.** "ρ acts as Z → −1/Z and K(φ) → K(φ + π) = −K(φ)" ([reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)). The gate adds that Z = i is the fixed point on the half-plane and that "no vacuum is ρ-invariant".
- **Breaking pattern.** "The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}", with K₀ = diag(1, −1). The worklog writes the pattern as "Sp(2,R) → Z₂ = {1, ρ²}" ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)).
- **Order parameter [V].** "O = K₁₁ is +1 in (1, K₀) and −1 in its ρ-image" (worklog, criterion S3); version 2: "O = K₁₁ flips sign under ρ". K carries the program's order parameter η = ωK ([the order parameter](/wiki/symmetry-breaking/order-parameter)).
- **Spectrum [V].** "The potential's Hessian has rank 1 at the vacuum. That leaves three Goldstone directions: the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)." ([Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs); [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian))
- **The bridge to τ.** The worklog calls the compact Goldstone "the checkpoint's Maslov circle (the τ field of §10)". #11 §10: "In the coset model that angle parametrizes Λ(1): it is τ's circle", adding "None of this tests the cosmology; it only shows the structure is consistent." ([τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase); [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle))
- **Caveat.** "But the twisted element ρ∘(K → −K) maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does. Breaking ρ is physical only once a coupling odd in K is present" ([the twisted element](/wiki/symmetry-breaking/twisted-element); [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)).
- **Why a potential follows.** "In 1+1 the compact angle φ cannot order" ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)), so "To get a definite polarization we add a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" (version 2, §4): the [bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential). Its origin is [open](/wiki/symmetry-breaking/rho-preserving-potential), and so is [whether the coupled model orders ρ's SO(2) without it](/wiki/symmetry-breaking/toy-models/coset-model/so2-question).

## Sources

- `papers/reciprocity-toy-models.md` §2 — the vacua, the action of ρ, the stabilizer, the order parameter, the spectrum and the twisted element, quoted above
- `verify/toy_coset.py` S2, S3, 'Spectrum' — the gated checks
- `review/round4/referee/audit-notes.md` Step 2(a) — the referee's independent confirmation
- `notes/toy-lagrangian.md` 'Chunk 1 results' — the S2, S3 and spectrum passes [V], and the Maslov-circle remark
- `papers/broken-born-checkpoint-v2.md` §10 — the toy-model support for τ's circle [D][V], and its limits
