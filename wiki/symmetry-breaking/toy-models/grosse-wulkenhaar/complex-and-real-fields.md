---
title: "Complex versus real fields: symmetry versus covariance"
weight: 40
status: alive
description: "For complex fields the duality is a genuine symmetry inside a continuous U(1)^N × U(1)^N; for real fields it maps out of the field space, so the action is only covariant."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §3"
  - "verify/toy_gw.py S1"
  - "review/round4-adjudication.md 'Revisions' 3"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
---

*Whether the Langmann–Szabo duality is a symmetry of [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) depends on whether its field is complex or real. For a complex field the duality maps every allowed field to another allowed field with the same action, so it is a genuine symmetry, and it is one element, rotation angle π, of a continuous family of phase rotations. For a real field the duality's image of a real configuration is no longer real, so the duality leads out of the space of fields; the action is only covariant, carried into an equivalent action written in new variables rather than into itself. The distinction matters for what follows: a symmetry can be spontaneously broken, while a covariance allows only an explicit selection between vacua.*

**Status:** Alive, partly prior art — [V] (`verify/toy_gw.py`, the S1 checks; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — reproduced by the round-4 referee; Grosse and Wulkenhaar call the real model invariant, and the complex framing is Langmann and Szabo's original.

## Key facts

- **Complex fields [V].** The duality "is a genuine field symmetry, S[Πφ] = S[φ]" (worklog). "It satisfies S[UφV†] = S[φ] for all diagonal unitaries U, V. The duality Πφ is the α = π element of e^{−iαN}." Here † is the Hermitian adjoint, not the citation mark.
- **Real fields [V].** "Πφ is not Hermitian, so the duality maps the real field space out of itself. The real action is only covariant: its quartic term is invariant in the alternating form Tr((ψψ†)²), ψ = Πφ." The referee's values: Tr φ⁴ = 1230.31 against Tr (Πφ)⁴ = 50.62, while Tr (ψψ†)² = 1230.31.
- **Why it looked contradictory.** "Grosse–Wulkenhaar's duality alternates the sign of the Fourier exponent around the ⋆-vertex" (worklog), which the referee confirmed in Grosse and Wulkenhaar's paper ("a refers to the cyclic order in the star-product"); the alternation is what [the matrix-base lemma](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) makes explicit.
- **Prior art.** Grosse and Wulkenhaar state that the real Ω = 1 action "is invariant under the duality"; the referee called the note's "covariant only" its "own reinterpretation", and found the duality formulated for complex fields in Langmann and Szabo's original paper. The referee's verdict: "Partly prior art" ([noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)).
- **Predicted as a weak point.** The round-4 pre-registration named the distinction a runner-up weakest link: "Grosse–Wulkenhaar call the real model invariant, and a referee may read their alternating convention as a symmetry of the real model after all." The outcome: "real-vs-complex confirmed and extended (F4)".
- **A continuous symmetry.** In the complex model the referee found S[φ] = S[Πφ] = S[UφV†] = 3539.2309815 for diagonal U, V, while a non-diagonal U gives 3657.12. So the duality sits inside a continuous U(1), and the polarization is a Goldstone angle, a reading round 4 restricted to the complex model (revision 3; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).
- **The two outcomes.** The complex model has a flat polarization angle whose classical breaking is undone by quantization ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua); [quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)); the real model has discrete vacua whose degeneracy is lifted explicitly at one loop ([the real model's lead](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)). Compare the distinction between a symmetry and a change of description at [unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence).

## Sources

- `papers/reciprocity-toy-models.md` §3 — the complex and real cases, quoted above
- `verify/toy_gw.py` S1 — the gated symmetry and covariance checks
- `review/round4-adjudication.md` 'Revisions' 3, 'Pre-registration scored' — the restriction of "Goldstone angle"; the scored prediction
- `review/round4-preregistration.md` 'Predictions' — the runner-up weakest link
- `review/round4/referee/audit-notes.md` Step 1, Step 2(b), Step 3 — the source check of the alternation and of "invariant"; the numerical values; "Partly prior art"
- `notes/toy-lagrangian.md` 'Chunk 2 results' — the resolution of the convention question [V]
