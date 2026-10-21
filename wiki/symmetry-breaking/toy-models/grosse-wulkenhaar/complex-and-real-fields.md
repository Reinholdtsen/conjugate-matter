---
title: "Complex versus real fields: symmetry versus covariance"
weight: 40
status: alive
description: "For complex fields the duality is a genuine symmetry inside a continuous U(1)^N × U(1)^N; for real fields it maps out of the field space, so the action is only covariant, and the vacua it relates need not stay degenerate."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md v1 (commit d9a06ac) Abstract, §3"
  - "verify/toy_gw.py S1"
  - "review/round4-adjudication.md 'Rulings' F4"
  - "review/round4-adjudication.md 'Revisions' 3"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_model2_vac.txt"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
---

*Whether the [Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory) is a symmetry of [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) depends on whether its field is complex or real. On the [matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base) the duality multiplies the rows of the field's matrix by alternating signs. A complex field is an arbitrary matrix, so the duality takes every allowed field to another allowed field with the same action: a genuine symmetry, and one element, the half-turn, of a continuous family of phase rotations that also leave the action unchanged. A real field is a Hermitian matrix, and the duality's image of a Hermitian matrix is in general not Hermitian, so the duality leads out of the space of real fields. The real action keeps its value only when it is rewritten in the new variable, which makes the duality a covariance of the real model, not a symmetry. The distinction decides what each version can show: a symmetry can be broken spontaneously and keeps the vacua it relates exactly degenerate, while without one a preference between vacua can arise explicitly, as it does in the real model at one loop.*

**Status:** Alive, partly prior art — [V]: the symmetry and covariance checks, criterion S1 for this route, are gated in `verify/toy_gw.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)), and the referee of [review round 4](/wiki/method/review/round-4) reproduced them with independent code. Grosse and Wulkenhaar call the real model invariant, and the complex formulation is Langmann and Szabo's original.

## Symmetry and covariance

A map of a theory can relate it to itself in two ways [T]:

- **A symmetry** maps the space of field configurations onto itself and leaves the action unchanged. Every quantity the theory computes is then unchanged as well, including the quantum corrections, and the vacua the map exchanges are exactly degenerate.
- **A covariance** carries the action into an action of the same form written in other variables, or at other parameter values. It relates two descriptions; it does not by itself make two configurations of one theory equivalent.

The program's first success criterion turns on the same distinction: "S is invariant, not merely related to its image by a unitary equivalence" (criterion S1, [success criteria](/wiki/symmetry-breaking/toy-models/success-criteria)), which is the referees' point that [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) in ordinary quantum mechanics is a change of description ([unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence)). A symmetry is also what [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking) needs: a symmetric law with an asymmetric vacuum. Grosse and Wulkenhaar call their model at general Ω "duality-covariant", in the sense that the duality carries it to the model at another value of Ω [T] ([noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory#the-self-dual-point)); at Ω = 1 the question is whether it maps the theory onto itself.

On the matrix base the duality is left multiplication by parity, Dφ = Πφ with Π = diag((−1)^m) ([the lemma](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma)), and the answer depends on the field space.

## Complex fields: a genuine symmetry

The complex field is an arbitrary matrix, with the action ([the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base))

```text
S[φ] = Σ_mn (m + n + 1 − μ²) |φ_mn|² + λ Tr((φ†φ)²)
```

where † is the Hermitian adjoint, not the citation mark. Πφ is again an arbitrary matrix, and the action does not change. The worklog: "Complex model: the duality is a genuine field symmetry, S[Πφ] = S[φ] [V]." ('Chunk 2 results'). The reason is short. Multiplying rows by signs leaves every |φ_mn|² unchanged, and (Πφ)†(Πφ) = φ†Π²φ = φ†φ, since Π is real and Π² = 1.

**A continuous family.** The same holds for any phases on the rows and columns. The note: "It satisfies S[UφV†] = S[φ] for all diagonal unitaries U, V. The duality Πφ is the α = π element of e^{−iαN}." (§3). Each diagonal unitary carries one phase per level, so the group is U(1)^N × U(1)^N for a truncation to N levels. Its one-parameter subgroup of left rotations e^{−iαN}, with N = diag(0, 1, 2, …) the level number, contains the duality at α = π, the half-turn. The duality is therefore one point on a circle of exact symmetries, which is why the complex model's vacua form a circle and the polarization is an angle on it ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua); [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

**The checks [V].** The gate's section "S1: is the duality a symmetry of the field space?" passes "complex model: S[Pi phi] = S[phi] (duality is a field symmetry)" and "complex model: S[U phi V^dag] = S[phi] for any diagonal unitaries U, V (a continuous U(1)^N x U(1)^N)", on random complex matrices with N = 8. The round-4 referee's values: S[φ] = S[Πφ] = S[UφV†] = 3539.2309815 for diagonal U and V, while "non-diagonal U gives 3657.12" (audit notes, Step 2(b)); a unitary that mixes levels is not a symmetry. At N = 10 it found "S = 7638.11944458 at 5 random (U,V)" (Step 2(c)). It also checked the consequence for the vacua: the Hessians at the duality-related vacua have identical spectra, "complex model: max |eig(v+) - eig(v-)| = 0.0" (`review/round4/referee/out_model2_vac.txt`).

## Real fields: only a covariance

A field that is real on the plane has a Hermitian matrix, and its quartic term is Tr φ⁴. The note:

> Πφ is not Hermitian, so the duality maps the real field space out of itself. The real action is only covariant: its quartic term is invariant in the alternating form Tr((ψψ†)²), ψ = Πφ. (§3)

**Why Πφ leaves the field space.** The adjoint of Πφ is φΠ, which equals Πφ only if φ commutes with Π, that is, only if φ has no entries linking an even level to an odd one. A general Hermitian matrix has such entries, so its image is not Hermitian.

**What the alternating form does.** With ψ = Πφ and φ Hermitian, ψ† = φΠ, and the product ψψ† = Πφ²Π. Squaring it and using Π² = 1 gives Πφ⁴Π, whose trace is Tr φ⁴. The quadratic term is unchanged as well, because |ψ_mn|² = |φ_mn|². Written in the variable ψ, with the legs of the quartic term alternating between ψ and ψ†, the real action therefore keeps its value and takes the form of the complex action. But ψ is not a real field, so the duality relates the real model to a description of it in other variables, not to itself. The plain quartic term in the image, Tr((Πφ)⁴), is a different number.

**The checks [V].** The gate passes three checks on random Hermitian matrices: "real model: Pi phi is not Hermitian, so the duality leaves the real field space"; "real model: Tr((Pi phi)^4) != Tr(phi^4); the real action is only covariant (alternating legs)"; and "real model: its quartic is invariant in the alternating form Tr((psi psi^dag)^2), psi = Pi phi". The referee's values for one configuration: Tr φ⁴ = 1230.31 against Tr (Πφ)⁴ = 50.62, while Tr (ψψ†)² = 1230.31 (audit notes, Step 2(b)).

### The vacua it does relate

On diagonal matrices the duality stays inside the real field space: a diagonal φ commutes with Π. The referee: "for diagonal phi, Pi phi stays Hermitian, so the duality maps v+ = diag(a0,a1) to v- = diag(a0,-a1), classically degenerate (S_r = -2.5 both). But the fluctuation spectra differ" (audit notes, Step 2(b)). The real model's vacua are diagonal, so the duality exchanges them, and their classical actions are equal. The fluctuations around a vacuum, however, are general Hermitian matrices, which the duality takes out of the field space; it does not carry the fluctuations around one vacuum into those around the other, and nothing requires the two spectra to agree. They do not. In the complex model the symmetry does carry them across, and the spectra agree ("max eigenvalue difference 0.0"). This difference is round-4 finding F4: the real model's two vacua split at one loop, in favour of the one sharper in position ([Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)).

## Two readings of one algebra

**Why chunk 1 looked contradictory.** Before the computation, conventions recalled from memory could not make the quartic term invariant, against Grosse and Wulkenhaar's stated invariance. Chunk 2 found the cause: "Grosse–Wulkenhaar's duality alternates the sign of the Fourier exponent around the ⋆-vertex" (worklog, 'Chunk 2 results'). In the matrix base the alternation is parity on the left index of one factor and on the right index of the next ([the lemma](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma#the-alternation-of-grosse-and-wulkenhaar)): precisely the alternating form Tr((ψψ†)²).

**Grosse and Wulkenhaar's reading.** They state that the real Ω = 1 action "is invariant under the duality". The round-4 referee found the statement and the alternating convention in their paper ("'a refers to the cyclic order in the star-product' -- CONFIRMED") and called the note's "covariant only" "its own reinterpretation" (audit notes, Step 1). Both readings describe the same algebra: the quartic term is unchanged when its legs are transformed alternately. They differ on whether that alternating assignment counts as a symmetry of a real field. The note's reading is that it does not. The duality, as a map of the field, is φ → Πφ, and it takes a real field out of the real field space; the alternation transforms alternate factors of the quartic term differently, which a map of the field, acting on every factor alike, does not do.

**Langmann and Szabo's reading.** Their original duality is formulated "for a complex field in a magnetic field" (audit notes, Step 1, capitals lowered), so the complex framing is theirs. The referee's novelty audit: "'Real covariant, complex symmetric': [Langmann and Szabo's] original duality (Prop. 1) is formulated for complex fields; [Langmann, Szabo and Zarembo] (hep-th/0308043) solve a closely related complex model exactly. Partly prior art" (Step 3, with the referee's abbreviations written out). The adjudication's revision 3 credits "Langmann–Szabo (the complex formulation)".

## Predicted as a weak point

The round-4 pre-registration named the distinction as its second runner-up weakest link: "The real-versus-complex distinction. Grosse–Wulkenhaar call the real model invariant, and a referee may read their alternating convention as a symmetry of the real model after all." (`review/round4-preregistration.md`; [pre-registration](/wiki/method/review/pre-registration)). The adjudication scored the outcome as "real-vs-complex confirmed and extended (F4)", and the three runner-up predictions together as "Partial on all three" ('Pre-registration scored').

## What round 4 changed

The distinction was already in the note's first version (commit d9a06ac), which called the real action "duality-*covariant*" (§3) and the duality "a field symmetry of the complex model but not of the real one" (Abstract). Round 4 confirmed it, credited it in part to Langmann and Szabo, and extended it with F4. It also narrowed a generalization built on the complex case. The first version's abstract said that "in both models" ρ is one element of a continuous U(1), "so the polarization is a Goldstone angle rather than a discrete choice"; the referee found this "true of the two models chosen, not of the [Grosse–Wulkenhaar] model the duality literature is about" (audit notes, Step 2(b)), and revision 3 reads "Restrict 'Goldstone angle' to the complex model." Version 2 states the scope: "Where ρ sits inside a continuous U(1) — model I, and model II with complex fields — the polarization is a Goldstone angle." (Abstract; [model I](/wiki/symmetry-breaking/toy-models/coset-model)).

## What follows

- **Complex fields.** The vacua form a circle of the phase β, the duality moves each vacuum half-way round it, and classically no vacuum is invariant ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)). Because the circle is generated by an exact symmetry and the condensate is a localized lump, quantization restores the symmetry ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).
- **Real fields.** The vacua are discrete, the duality exchanges them, and their degeneracy is lifted at one loop. The selection is "explicit, not spontaneous … because the real model is not duality-symmetric: its field is real in position" (§3; [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)).

## Sources

- `papers/reciprocity-toy-models.md` §3, Abstract — the complex and real cases, quoted above; the scope of the Goldstone-angle reading
- `papers/reciprocity-toy-models.md` version 1 (commit d9a06ac), Abstract, §3 — the distinction as first stated
- `verify/toy_gw.py` S1 — the five gated symmetry and covariance checks
- `review/round4-adjudication.md` 'Rulings' F4, 'Revisions' 3, 'Pre-registration scored' — the real model's split; the credit to Langmann–Szabo and the restriction of "Goldstone angle"; the scored prediction
- `review/round4-preregistration.md` 'Predictions' — the runner-up weakest link
- `review/round4/referee/audit-notes.md` Step 1, Step 2(b), Step 2(c), Step 3 — the alternating convention and "invariant" in Grosse–Wulkenhaar; the numerical values; the duality on diagonal vacua; the U(1)^N × U(1)^N check at N = 10; "Partly prior art"
- `review/round4/referee/out_model2_vac.txt` — the identical complex-model spectra
- `notes/toy-lagrangian.md` 'Chunk 2 results' — the resolution of the convention question and the two cases [V]
