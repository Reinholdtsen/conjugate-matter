---
title: "Toy models of broken reciprocity"
weight: 120
status: hub
description: "Two explicit field theories built to meet acceptance criterion 1, a coset sigma model and the self-dual Grosse–Wulkenhaar model, with the criteria fixed in advance, the results, and the two documents (the toy-model note v2 and its worklog)."
bookCollapseSection: true
---

*A toy model is a small, fully specified field theory built to test one idea in isolation. The idea tested here is the program's [hard core](/wiki/program/hard-core): that [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), the exchange of position and momentum, is an exact symmetry of the equations that the lowest-energy state does not share. Two models were built and tested on 19–20 October 2026, a sigma model of phase-space structures (model I) and a scalar field theory on a noncommutative plane (model II). Together they answer the referees' acceptance criterion 1, which checkpoint #11 now records as met in the referees' wording, with stated open ends.*

**Stands:** [acceptance criterion 1, met in the referees' wording](/wiki/symmetry-breaking/toy-models/acceptance-criterion), [model I's action](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) and [vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua), [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential), [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) and [its ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo), [the duality lemma](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma), [complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields), [the complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua), [quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration) · **Died:** [the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) · **Open:** [whether ρ's SO(2) breaks in the coupled model](/wiki/symmetry-breaking/toy-models/coset-model/so2-question), [the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)

## Map

The work is recorded in two documents. `papers/reciprocity-toy-models.md` (version 2, commit 6606734, 2026-10-20) is the current reference. It is written as an anonymous manuscript for blind review, so it carries no provenance tags, and its † marks are Hermitian adjoints (φ†φ), not citation marks. `notes/toy-lagrangian.md` is the dated worklog: the criteria, four chunks of results, the assessment against the predictions, and the write-up. Where the two differ, version 2 governs; several of the worklog's numbers and wordings predate the round-4 review.

[Acceptance criterion 1: the toy Lagrangian](/wiki/symmetry-breaking/toy-models/acceptance-criterion) comes first because it is the demand the models answer: an action in which ρ is a genuine Noether symmetry, spontaneously broken, with the neutral metric η as order parameter. The page records the verdict, what remains open, and a clause of the demand that nothing yet addresses.

[Success criteria S0–S5 and the pre-registered predictions](/wiki/symmetry-breaking/toy-models/success-criteria) are the pass/fail tests written down before either model was built, with the forecasts scored against them. They are method, not physics, and they define what the later pages mean by "pass".

[Model I: the coset sigma model](/wiki/symmetry-breaking/toy-models/coset-model) is a field theory of a phase-space metric H and a real structure K, and it is the model that meets the criterion. Its subsection runs from the sigma-model background through the action, the vacua, the failed and the repaired potentials and the lattice simulation, to the open question about ρ's SO(2).

[Model II: the self-dual Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) was tested first, as the route in which a field's own vacuum might select position or momentum with no K put in by hand. For complex fields its classical breaking does not survive quantization, so the route fails the quantum-stability test; the real-field version leaves a one-loop lead.

Each model's subsection opens with one page of established physics, [coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models) and [noncommutative field theory and the Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory), both literature [T]. Every other page in this section is the program's own work, checked by the gated scripts described at [the toy-model scripts](/wiki/method/verification/toy-model-scripts) and graded B in [review round 4](/wiki/method/review/round-4).

## Boundaries

- The general lessons drawn from the toys sit at the root of [Spontaneous breaking of reciprocity](/wiki/symmetry-breaking): [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle), [the twisted element ρ∘(K → −K)](/wiki/symmetry-breaking/twisted-element), [the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) (open), [the section condition](/wiki/symmetry-breaking/section-condition), [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) and [forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) (open). This section holds the calculations behind them.
- The theorem that limits ordering in two dimensions is [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman).
- The objection the models were built to answer is [the 'framework does no work' critique](/wiki/program/framework-does-no-work), and the postulates they refine are [P2′](/wiki/program/postulates/p2-prime) and [P5](/wiki/program/postulates/p5-spontaneous-selection).
- The blind review that graded the toy-model note is [review round 4](/wiki/method/review/round-4), and the scripts that check it are described at [the toy-model scripts](/wiki/method/verification/toy-model-scripts).
