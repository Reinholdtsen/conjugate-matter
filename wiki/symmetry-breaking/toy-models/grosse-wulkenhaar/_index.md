---
title: "Model II: the self-dual Grosse–Wulkenhaar model"
weight: 40
status: hub
description: "A renormalizable noncommutative scalar field theory whose Ω = 1 point is self-dual under the Langmann–Szabo x ↔ p duality (a symmetry for complex fields, a covariance for real ones), tested first as the route in which a field's own vacuum might select x or p with no K put in by hand."
bookCollapseSection: true
---

*Model II is a scalar field theory on the noncommutative plane, whose two coordinates fail to commute as position and momentum do, taken at the parameter value Ω = 1 where the Langmann–Szabo duality maps the theory to itself. The duality is a Fourier transform: it exchanges a field's dependence on position with its dependence on momentum, as a waveform is exchanged with its spectrum. The model was tested first because its own vacuum might break that exchange symmetry with no extra structure put in by hand. For complex fields the vacua do break the duality classically, but the breaking does not survive quantization; for real fields the duality is not a symmetry at all, and a one-loop preference for the position-sharp vacuum remains a lead.*

**Stands:** [noncommutative field theory and the Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory) (literature), [the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base), [the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma), [complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields), [the complex-model vacua and Δ(β)](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua), [quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration) · **Died:** nothing yet · **Open:** [the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)

## Map

**Why this route came first.** In chunk 1 the worklog decided, as Claude's call under Paul's delegation, to "test the Grosse–Wulkenhaar Ω = 1 route first; keep the coset model as the η-implementation". The reason: "It is the one place where the toy could be both new and non-trivial: an interacting, renormalizable field whose own vacuum might select x or p, with no K put in by hand." A clash between recalled conventions for the duality stalled that chunk ("a recalled convention is wrong somewhere") and was settled in chunk 2 by direct numerical Fourier integration. The route then failed criterion S4, and the coset model's fallback, a ρ-preserving potential, became the S4 result ([model I](/wiki/symmetry-breaking/toy-models/coset-model)).

[Noncommutative field theory and the Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory) is the established background: the Moyal plane and its star product, the duality, and the Grosse–Wulkenhaar model, whose β-function vanishes to all orders at Ω = 1 in four dimensions.

[Model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base) sets up the computation: the oscillator basis f_mn, in which the Ω = 1 kinetic term is diagonal, with each formula checked against independent anchors, and the action for complex and real fields.

[The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) is the lemma the rest depends on: computed by direct Fourier integration, the duality multiplies f_mn by (−1)^m, which is left multiplication by parity.

[Complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields) draws the first consequence: for complex fields the duality is a symmetry, one element of a continuous group of phase rotations; for real fields it leads out of the field space, so the action is only covariant.

[Complex-model vacua and the polarization Δ(β)](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua) finds the classical vacua: two oscillator levels condense with a free relative phase β, the duality shifts β by π, and the vacuum's position-versus-momentum spread varies as cos β.

[Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration) shows why that classical breaking does not survive: β is an exact flat direction of a localized lump with no volume factor, so the quantum average of the polarization is zero, and criterion S4 fails for this route.

[Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead) closes the section with the real-field version, where two classically degenerate vacua split at one loop in favour of the position-sharp one: an explicit selection, recorded as a lead.

The first page is literature [T]; the rest are the program's computations, gated in `verify/toy_gw.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)) and reviewed in [review round 4](/wiki/method/review/round-4).

## Boundaries

- Model I, the coset route that meets the criterion, is [Model I: the coset sigma model](/wiki/symmetry-breaking/toy-models/coset-model).
- What the complex model's flat angle means for the program, together with model I's, is at [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).
- The phase-space tools the lemma relies on are [the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform) and [the Wigner function and Weyl symbols](/wiki/phase-space/reciprocity/wigner-function).
- The demand the route was tested against is [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion), through the [success criteria](/wiki/symmetry-breaking/toy-models/success-criteria).
