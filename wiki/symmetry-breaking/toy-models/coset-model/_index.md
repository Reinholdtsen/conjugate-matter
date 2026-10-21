---
title: "Model I: the coset sigma model"
weight: 30
status: hub
description: "A 1+1-dimensional sigma model of a phase-space metric H and a real structure K, invariant under Sp(2, ℝ) ∋ ρ, whose vacua break ρ with K as order parameter."
bookCollapseSection: true
---

*Model I is a field theory on a two-dimensional base, one space and one time direction, whose two fields are geometric structures on the phase plane of a particle moving in one dimension: a metric H, and a real structure K whose two eigenlines are the candidate "position" and "momentum" axes. Its equations are unchanged by every area-preserving linear map of the phase plane, [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ among them, but its lowest-energy states are not: ρ carries each vacuum to a different one, and the entry K₁₁ changes sign. With a bounded potential added on the polarization angle, it is the model with which the program meets [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion); its lattice result holds for the reduction with H held fixed.*

**Stands:** [coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models) (literature), [the action and its symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries), [the vacua, order parameter and Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua), [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential), [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction), [the ordered ℤ₂ phase in the Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) · **Died:** [the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) · **Open:** [whether ρ's SO(2) breaks in the coupled model](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)

## Map

[Coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models) is the established physics the model is built from: fields valued in a curved target space, why an indefinite target metric means a ghost, and why non-compact (hyperbolic) models can order in two dimensions where compact ones cannot. It comes first because every later page uses it.

[Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) gives the Euclidean Lagrangian and the check of criterion S1: the action is invariant under Sp(2, ℝ), hence under ρ, and under a separate flip K → −K.

[Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua) finds the lowest-energy states (criteria S2 and S3): the upper half-plane times a circle of K's, which ρ maps to other vacua, with O = K₁₁ changing sign and three flat directions, one of them the polarization angle.

[Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) records the first potential added to make the polarization definite, −μ[Tr(K K_ref)]², and how round 4 showed it to be unbounded below once H is dynamical. It sits before its repair, so the repair reads as the answer to a measured failure.

[The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) is that repair: a normalized form that stays between −μ and 0 and leaves the vacuum stable with all fields dynamical.

[The frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) states the scope of the lattice result: with H held at 1, model I becomes a two-dimensional spin model of the polarization angle, and what is established holds for that reduction only.

[Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) is the numerical evidence for criterion S4 in the reduction, with error bars from independent seeds, a high-temperature control and the potential-free comparison.

[Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question) closes the subsection with the question the reduction leaves: whether the full model, whose H-sector is a hyperbolic sigma model, orders ρ's compact SO(2) without a potential.

Only the first page is literature [T]. The rest are the program's claims, from `papers/reciprocity-toy-models.md` §2 and §4, checked in `verify/toy_coset.py` and `verify/toy_s4.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Boundaries

- Model II, the noncommutative route, is [Model II: the self-dual Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar).
- What model I's results mean for the program is at the root of [Spontaneous breaking of reciprocity](/wiki/symmetry-breaking): [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle), [the twisted element ρ∘(K → −K)](/wiki/symmetry-breaking/twisted-element), [the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) (open), [the section condition](/wiki/symmetry-breaking/section-condition) and [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).
- The phase-space structures themselves are defined in [Born geometry](/wiki/phase-space/born-geometry), and the circle the polarization angle runs over is [the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian).
- The review that found the unbounded potential is [review round 4](/wiki/method/review/round-4).
