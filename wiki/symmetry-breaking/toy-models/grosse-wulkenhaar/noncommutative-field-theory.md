---
title: "Noncommutative field theory and the Langmann–Szabo duality"
weight: 10
status: established
description: "The Moyal plane and star product, the Langmann–Szabo duality of noncommutative scalar field theory, and the Grosse–Wulkenhaar model at Ω = 1 with its all-orders vanishing β-function in 4D."
provenance: [T]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md refs [5]–[10]"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "review/round4/referee/audit-notes.md Step 1"
---

*Noncommutative field theory places fields on a plane whose two coordinates do not commute, [x₁, x₂] = iθ, the same kind of relation that position and momentum obey in quantum mechanics; the ordinary product of fields is replaced by the Moyal star product, which carries that relation. Langmann and Szabo found that scalar field theories of this kind have a duality exchanging positions and momenta, a Fourier transform of the field. Grosse and Wulkenhaar's model is invariant under it at the parameter value Ω = 1, where its β-function vanishes to all orders in four dimensions. This is the literature behind [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar): an interacting field theory with an exact exchange of position and momentum, which the program used to test whether a vacuum alone could break that exchange.*

**Status:** Established — literature [T]; the citations were retrieved [S] in the worklog's prior-art survey and checked against INSPIRE records and arXiv sources by the round-4 referee.

## Key facts

- **The Moyal plane.** Model II works on "the Moyal plane [x₁, x₂] = iθ (θ = 1)", with a matrix base f_mn taken from de Goursac–Tanasa–Wallet (App. A), in which the star product becomes matrix multiplication: f_mn ⋆ f_kl = δ_nk f_ml ([the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base)).
- **The Langmann–Szabo duality.** "Langmann and Szabo found a duality of noncommutative scalar field theory that exchanges positions and momenta, formulated for complex fields [5]." The round-4 referee found it formulated for a complex field in a magnetic field, as a single Fourier map, so the complex-field framing is Langmann and Szabo's original ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)).
- **The Grosse–Wulkenhaar model.** "The Grosse–Wulkenhaar model is invariant under it at Ω = 1 [6], with an all-orders vanishing β-function in 4D [7]" (Disertori–Gurau–Magnen–Rivasseau). Grosse and Wulkenhaar state that the real Ω = 1 action "is invariant under the duality", note that the duality is "manifest" in the matrix base, and alternate the sign of the Fourier exponent around the star-product vertex.
- **An exact solution.** "A closely related model is exactly solvable [8]" (Langmann–Szabo–Zarembo), which version 2 calls "the natural independent check" of its restoration argument and has not carried out ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).
- **Vacua studied, but not under the duality.** "Non-constant vacua at Ω = 1 [9], and minima of the complex self-dual planar model [10], have been studied, but not their behaviour under the duality." The worklog: de Goursac–Tanasa–Wallet "find non-constant vacua at Ω = 1 for μ² ≥ 4/θ", and "Stripe phases in this literature break translations, not x ↔ p."
- **Locality in this literature.** The worklog quotes Langmann and Szabo: at θ = 0 the position vertex is "fully local" and the momentum vertex non-local; "for non-singular θ, both vertex functions have the same non-local form". Its reading: "In that literature, locality in x arises only at the singular θ → 0 limit, not from a vacuum."
- **Dimension.** These results are for four dimensions; model II is two-dimensional, and version 2 uses "the two-dimensional form of [6, eq. 1]", whose four-dimensional original has the prefactor π² rather than π.

## Used by

- [Model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base) — the matrix base and the Ω = 1 kinetic form.
- [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) — the duality's explicit action on f_mn.
- [Complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields) — symmetry for complex fields, covariance for real ones.
- [Complex-model vacua and the polarization Δ(β)](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua) — the condensed vacua and their cos β polarization.
- [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration) — why the classical breaking does not survive.
- [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead) — the real model's one-loop split.

## Sources

- `papers/reciprocity-toy-models.md` §1, §3, §4, refs [5]–[10] — the literature as version 2 states it
- `review/round4/referee/audit-notes.md` Step 1 — the citation audit: the complex formulation, the four-dimensional form of eq. 1, "invariant under the duality", the alternating sign
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Chunk 2 results' — the prior-art survey [S], the vacua at μ² ≥ 4/θ, the locality quotation, the sources of the matrix base and the duality
