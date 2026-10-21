---
title: "Unitary equivalence versus Noether symmetry"
weight: 50
status: established
description: "By the Stone–von Neumann theorem the irreducible representations of the canonical commutation relations are unitarily equivalent, so ρ is ordinarily a change of description; why the referees demanded an action in which it is a genuine symmetry."
provenance: [T]
sources:
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §6"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §3"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
---

*Unitary equivalence and Noether symmetry are the two different ways a map like [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) can relate to a physical theory. It can be a change of description, a unitary equivalence — the same physics written in other variables, as a Fourier transform rewrites a waveform as a spectrum — or it can be a symmetry of the dynamics: an operation that leaves a specific action unchanged, and therefore constrains what the theory can do (a Noether symmetry). In ordinary quantum mechanics ρ is the first kind, because the Stone–von Neumann theorem makes all the standard ways of representing the position–momentum commutation rules equivalent. The program needs the second kind, since only a symmetry of an action can be [spontaneously broken](/wiki/symmetry-breaking/spontaneous-symmetry-breaking). Its referees made exhibiting such an action [the first acceptance criterion](/wiki/symmetry-breaking/toy-models/acceptance-criterion) for anything it proposes, and [#11](/wiki/history/documents/checkpoint) records the criterion as met, in the referees' wording, by the [toy models](/wiki/symmetry-breaking/toy-models).*

**Status:** Established — the equivalence is textbook quantum mechanics [T], stated here from general knowledge; the program's claim that ρ is a symmetry of an underlying action is the postulate [P3](/wiki/program/postulates/p3-reciprocity) [P]. The distinction was raised by the referees and conceded in [#14](/wiki/dark-matter/candidates/soliton-candidate) §1; #11 §14 item 11 records the criterion as met in the referees' wording by the toy models, whose invariance is machine-checked [V] ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Two ways a map can be a symmetry

### A change of description

Two descriptions of a quantum system are unitarily equivalent when a unitary operator U carries the states and operators of one into those of the other [T]. Every probability and every expectation value comes out the same, so nothing observable tells the two apart: they are one theory in two coordinate systems. Rewriting a wavefunction ψ(x) as its momentum wavefunction ψ̃(p) is of this kind ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)).

### A symmetry of the dynamics

A Noether symmetry is a transformation of the fields that leaves a specific action S unchanged [T]. It constrains the dynamics. Terms that the transformation does not leave invariant cannot appear in the action, solutions map to solutions, and lowest-energy states map to lowest-energy states. For each continuous symmetry, Noether's theorem gives a conserved quantity [T].

Only a symmetry of this second kind can be spontaneously broken. The action has the symmetry, but its lowest-energy states do not; they form a family that the symmetry permutes, and the system settles in one member [T] ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)). The program's [hard core](/wiki/program/hard-core) claims that the world's preference for position is a choice of that kind, made by the vacuum. The withdrawn manuscript #14 states what that requires: "The framework's claim is that rho is a genuine symmetry of an underlying action, spontaneously broken" (#14 §1).

## The Stone–von Neumann theorem

The commutation relation [x̂, p̂] = iℏ could in principle be represented by operators on many different spaces of states. For finitely many degrees of freedom the Stone–von Neumann theorem settles the question: every irreducible representation of the relations, in their exponentiated (Weyl) form, is unitarily equivalent to the ordinary Schrödinger representation on wavefunctions ψ(x) [T]. The exponentiated form, built from the bounded operators e^{iax̂} and e^{ibp̂}, avoids the domain problems of the unbounded x̂ and p̂, for which the uniqueness can fail [T].

Applied to ρ, the theorem works as follows.

1. The pair (p̂, −x̂) obeys the same relation as (x̂, p̂), since [p̂, −x̂] = [x̂, p̂] = iℏ ([the canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator)).
2. By the theorem a unitary operator carries the first representation into the second. It is the Fourier transform: F† x̂ F = p̂ and F† p̂ F = −x̂ [T].
3. The same argument covers every linear map of phase space that preserves the symplectic form. Each is carried out by a unitary operator, unique up to a phase (the metaplectic representation) [T]; see [the symplectic form and Sp(2d, ℝ)](/wiki/phase-space/reciprocity/symplectic-form).

So in quantum mechanics with finitely many degrees of freedom, ρ and every other linear symplectic map is a change of description.

The theorem does not extend to infinitely many degrees of freedom. Quantum field theories admit unitarily inequivalent representations of the commutation relations, and distinct vacua of a spontaneously broken symmetry live in such inequivalent representations [T]. The toy models are field theories: the worklog's criterion for quantum stability starts them in 1+1 dimensions, because "In 0+1 dimensions (quantum mechanics), tunnelling restores any symmetry" (`notes/toy-lagrangian.md`, "Success criteria", S4).

## Why ρ is ordinarily only a change of description

#14 conceded the point at its outset: "We note at the outset a distinction the proposal must eventually discharge: as usually encountered, rho is a unitary equivalence between representations of the canonical commutation relations, not a Noether symmetry of a specified action. The framework's claim is that rho is a genuine symmetry of an underlying action, spontaneously broken; the emergent structure eta below is the proposed order parameter, and the exhibition of a toy action realizing this is stated in Sec. 6 as the proposal's first acceptance criterion." (#14 §1).

The order parameter #14 names is the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η ([the order parameter](/wiki/symmetry-breaking/order-parameter)). The program postulates the second kind of symmetry: "**P3** The action is invariant under the Born rotation generated by I = ω⁻¹H. [P]" (#11 §4; [P3](/wiki/program/postulates/p3-reciprocity)).

## The referees' demand

The demand came out of the blind reviews of #14:

- **Round 1.** The referee's "toy-Lagrangian demand" was "adopted as acceptance criterion #1" (`HANDOFF.md` §6). [The handoff](/wiki/history/documents/handoff)'s first open item adds that "both reviewers independently named it" (§2). See [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two).
- **#14** states the criterion so that failure would be checkable: "(1) exhibition of an action - a toy model suffices - in which rho is a genuine Noether symmetry, spontaneously broken, with eta the order parameter selecting both the position polarization and the hidden sector's electric description; deriving hypothesis H from that action would make the coupling a prediction" (#14 §6).
- **Round 3.** The referees' shared verdict became the program's main critique ([the 'framework does no work' critique](/wiki/program/framework-does-no-work)), and the adjudication made the toy Lagrangian the next task, as the one item that could answer it: "Every referee across three rounds converges on 'the framework does no work'. The toy action is the only item that can change that, and it is acceptance criterion 1 for anything the program proposes." (`review/round3-adjudication.md`, decision 4; [round-3 decisions](/wiki/method/review/round-3/decisions)).

The worklog fixed its success criteria before building anything, and the first of them is this page's distinction: "**S1 — symmetry of an action.** An explicit action S[fields] on which ρ acts as a symmetry: S is invariant, not merely related to its image by a unitary equivalence. Invariance is verified symbolically." (`notes/toy-lagrangian.md`, "Success criteria"; [success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)).

## The answer so far

#11 §14 item 11 records the criterion as "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential":

- "ρ is a symmetry of an explicit action, and η = ωK is the order parameter;"
- "the vacuum is stable with H dynamical;"
- "there is an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo)."

Still open there [O]: "a Monte Carlo with H dynamical; a derivation of the potential; locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4." See [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion). #11 does not qualify the second point; the toy note does. Its stable minimum keeps one flat direction, the squeeze line, and "It is not symmetry-protected" (§4; [the symplectic form and Sp(2d, ℝ)](/wiki/phase-space/reciprocity/symplectic-form#rotations-boosts-and-squeezes)).

The invariance is machine-checked. In [model I](/wiki/symmetry-breaking/toy-models/coset-model), the coset model of (H, K), "Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS, and the action is invariant (checked for generic symplectic S, so for ρ)" (toy-model note §2), and the gate prints "all three terms invariant under rho" [V] ([Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)).

Two parts of the referees' wording are not covered by "met":

- **The electric sublattice.** #14's criterion and the handoff's open item required η to select "the hidden sector's electric description" (or "the electric sublattice") as well. The worklog's criteria and #11 §14 item 11 omit that clause. The root `CLAUDE.md` calls the toy Lagrangian "done to the referees' wording", and the clause remains unaddressed.
- **The round-3 critique.** The worklog's own assessment: "The round-3 critique ('the framework does no work') is only partly answered. The toy makes the program's structures cohere (η as order parameter; τ as the polarization angle), but matter's x-locality still enters through the P4-type coupling." (`notes/toy-lagrangian.md`, "Assessment against the predictions"; [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality)).

## Symmetry, covariance and the twisted element

Model II shows the same distinction between its complex and real versions. In [the self-dual Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) the position–momentum duality of [Langmann and Szabo](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory) acts on the field φ through a matrix Π (toy-model note §3):

- **Complex fields: a symmetry.** The action satisfies S[Πφ] = S[φ], and "The duality Πφ is the α = π element of e^{−iαN}" (§3); the gate prints "complex model: S[Pi phi] = S[phi] (duality is a field symmetry)".
- **Real fields: a covariance.** "Πφ is not Hermitian, so the duality maps the real field space out of itself. The real action is only covariant: its quartic term is invariant in the alternating form Tr((ψψ†)²), ψ = Πφ." (§3; here † is the Hermitian adjoint, not the citation mark). Grosse and Wulkenhaar themselves describe the real action at Ω = 1 as invariant under the duality; "covariant only" is the toy note's reading (the referee of [review round 4](/wiki/method/review/round-4), audit notes Step 1).

See [complex versus real fields: symmetry versus covariance](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields).

Even a symmetry of the action does not by itself make the breaking of ρ physical. Model I has a second symmetry, K → −K, and "the twisted element ρ∘(K → −K) maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does. Breaking ρ is physical only once a coupling odd in K is present" (toy-model note §2). See [the twisted element](/wiki/symmetry-breaking/twisted-element).

## Standard references

Added by the wiki from model memory (†); the program's documents do not cite them.

- M. H. Stone (1930)† and J. von Neumann (1931)†: uniqueness of the representation of the canonical commutation relations.
- E. Noether (1918)†: symmetries of an action and conserved quantities.
- G. B. Folland, *Harmonic Analysis in Phase Space* (1989)†: the metaplectic representation.

## Used by

- [Acceptance criterion 1: the toy Lagrangian](/wiki/symmetry-breaking/toy-models/acceptance-criterion) — the demand this distinction produced.
- [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria) — criterion S1 is the distinction itself.
- [P3: a reciprocity-invariant action](/wiki/program/postulates/p3-reciprocity) — the program postulates a symmetry of the action, not a change of description.
- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — an explicit action invariant under ρ.
- [Complex versus real fields: symmetry versus covariance](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields) — the distinction realized in model II.
- [The twisted element ρ∘(K → −K)](/wiki/symmetry-breaking/twisted-element) — what a symmetry of the action still leaves open.
- [The 'framework does no work' critique](/wiki/program/framework-does-no-work) — why the referees asked for the action.

## Sources

- `CLAUDE.md` "Since the handoff" — the toy Lagrangian "done to the referees' wording".
- `papers/broken-born-checkpoint-v2.md` §14 item 11 — the criterion met in the referees' wording, and what remains open.
- `papers/broken-born-checkpoint-v2.md` §4 — P3, the postulated symmetry of the action.
- `papers/reciprocity-toy-models.md` §1–§3 — the explicit ρ-invariant action, the twisted element, symmetry versus covariance.
- `review/round3-adjudication.md` "Decisions" — decision 4: the toy Lagrangian as the next task.
- `review/round4/referee/audit-notes.md` Step 1 — Grosse–Wulkenhaar's own wording on the real action.
- `HANDOFF.md` §2, §6 — the open item with the electric-sublattice clause; round 1 and the adoption of acceptance criterion 1.
- `notes/toy-lagrangian.md` "Success criteria", "Assessment against the predictions" — criterion S1; the 0+1 remark under S4; the partial answer to round 3.
- `notes/knot-dark-matter-standalone.md` §1, §6 — the concession and the criterion as #14 stated them (withdrawn paper).
- `verify/toy_coset.py`, `verify/toy_gw.py` — the invariance checks for model I and the complex model II.
