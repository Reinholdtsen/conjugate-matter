---
title: "Unitary equivalence versus Noether symmetry"
weight: 50
status: established
description: "By the Stone–von Neumann theorem the irreducible representations of the canonical commutation relations are unitarily equivalent, so ρ is ordinarily a change of description; why the referees demanded an action in which it is a genuine symmetry."
provenance: [T]
sources:
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 11"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/reciprocity-toy-models.md §1"
  - "wiki/papers/reciprocity-toy-models.md §2"
  - "wiki/papers/reciprocity-toy-models.md §3"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "wiki/papers/phase-space-diameter.md §5"
  - "verify/phase_space_diameter.py"
---

*Unitary equivalence and Noether symmetry are the two different ways a map like [Born reciprocity](born-reciprocity.md) can relate to a physical theory. It can be a change of description, a unitary equivalence — the same physics written in other variables, as a Fourier transform rewrites a waveform as a spectrum — or it can be a symmetry of the dynamics: an operation that leaves a specific action unchanged, and therefore constrains what the theory can do (a Noether symmetry). In ordinary quantum mechanics ρ is the first kind, because the Stone–von Neumann theorem makes all the standard ways of representing the position–momentum commutation rules equivalent. The program needs the second kind, since only a symmetry of an action can be [spontaneously broken](../../symmetry-breaking/spontaneous-symmetry-breaking.md). Its referees made exhibiting such an action [the first acceptance criterion](../../symmetry-breaking/toy-models/acceptance-criterion.md) for anything it proposes, and [#11](../../history/documents/checkpoint.md) records the criterion as met, in the referees' wording, by the [toy models](../../symmetry-breaking/toy-models/_index.md).*

**Status:** Established — the equivalence is textbook quantum mechanics [T], stated here from general knowledge; the program's claim that ρ is a symmetry of an underlying action is the postulate [P3](../../program/postulates/p3-reciprocity.md) [P]. The distinction was raised by the referees and conceded in [a withdrawn paper on monopole dark matter, §1](../../../notes/knot-dark-matter-standalone.md#1-framework); [#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) records the criterion as met in the referees' wording by the toy models, whose invariance is machine-checked [V] ([the toy-model scripts](../../method/verification/toy-model-scripts.md)).

## Two ways a map can be a symmetry

### A change of description

Two descriptions of a quantum system are unitarily equivalent when a unitary operator U carries the states and operators of one into those of the other [T]. Every probability and every expectation value comes out the same, so nothing observable tells the two apart: they are one theory in two coordinate systems. Rewriting a wavefunction ψ(x) as its momentum wavefunction ψ̃(p) is of this kind ([the Fourier transform as a phase-space rotation](fourier-transform.md)).

### A symmetry of the dynamics

A Noether symmetry is a transformation of the fields that leaves a specific action S unchanged [T]. It constrains the dynamics. Terms that the transformation does not leave invariant cannot appear in the action, solutions map to solutions, and lowest-energy states map to lowest-energy states. For each continuous symmetry, Noether's theorem gives a conserved quantity [T].

Only a symmetry of this second kind can be spontaneously broken. The action has the symmetry, but its lowest-energy states do not; they form a family that the symmetry permutes, and the system settles in one member [T] ([spontaneous symmetry breaking](../../symmetry-breaking/spontaneous-symmetry-breaking.md)). The program's [hard core](../../program/hard-core.md) claims that the world's preference for position is a choice of that kind, made by the vacuum. The withdrawn paper states what that requires: "The framework's claim is that rho is a genuine symmetry of an underlying action, spontaneously broken" ([its §1](../../../notes/knot-dark-matter-standalone.md#1-framework)).

## The Stone–von Neumann theorem

The commutation relation [x̂, p̂] = iℏ could in principle be represented by operators on many different spaces of states. For finitely many degrees of freedom the Stone–von Neumann theorem settles the question: every irreducible representation of the relations, in their exponentiated (Weyl) form, is unitarily equivalent to the ordinary Schrödinger representation on wavefunctions ψ(x) [T]. The exponentiated form, built from the bounded operators e^{iax̂} and e^{ibp̂}, avoids the domain problems of the unbounded x̂ and p̂, for which the uniqueness can fail [T].

Applied to ρ, the theorem works as follows.

1. The pair (p̂, −x̂) obeys the same relation as (x̂, p̂), since [p̂, −x̂] = [x̂, p̂] = iℏ ([the canonical commutator](canonical-commutator.md)).
2. By the theorem a unitary operator carries the first representation into the second. It is the Fourier transform: F† x̂ F = p̂ and F† p̂ F = −x̂ [T].
3. The same argument covers every linear map of phase space that preserves the symplectic form. Each is carried out by a unitary operator, unique up to a phase (the metaplectic representation) [T]; see [the symplectic form and Sp(2d, ℝ)](symplectic-form.md). On Gaussian wave packets these operators act by Möbius maps of the packet's complex shape parameter Z, the Fourier transform as Z → −1/Z ([Gaussian wave packets on the Siegel half-plane](../modular-field/gaussian-states.md)).

So in quantum mechanics with finitely many degrees of freedom, ρ and every other linear symplectic map is a change of description. This holds for the whole family of quarter-turns, one for each choice of reference length: [the phase-space-diameter note's script](../../method/verification/phase-space-diameter-script.md) checks that the map with [Born length](born-length.md) λ is symplectic for every λ [T][V], and that two such maps differ by a squeeze [D][V] ([`wiki/papers/phase-space-diameter.md` §5](../../papers/phase-space-diameter.md#5-what-reciprocity-adds-invariant-area-inverted-shape)).

The theorem does not extend to infinitely many degrees of freedom. Quantum field theories admit unitarily inequivalent representations of the commutation relations, and distinct vacua of a spontaneously broken symmetry live in such inequivalent representations [T]. The toy models are field theories: the worklog's criterion for quantum stability starts them in 1+1 dimensions, because "In 0+1 dimensions (quantum mechanics), tunnelling restores any symmetry" ([`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md), "Success criteria", S4).

## Why ρ is ordinarily only a change of description

The withdrawn paper conceded the point at its outset: "We note at the outset a distinction the proposal must eventually discharge: as usually encountered, rho is a unitary equivalence between representations of the canonical commutation relations, not a Noether symmetry of a specified action. The framework's claim is that rho is a genuine symmetry of an underlying action, spontaneously broken; the emergent structure eta below is the proposed order parameter, and the exhibition of a toy action realizing this is stated in Sec. 6 as the proposal's first acceptance criterion." ([its §1](../../../notes/knot-dark-matter-standalone.md#1-framework)).

The order parameter it names is the [neutral metric](../born-geometry/born-structures.md) η ([the order parameter](../../symmetry-breaking/order-parameter.md)). The program postulates the second kind of symmetry: "**P3** The action is invariant under the Born rotation generated by I = ω⁻¹H. [P]" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates); [P3](../../program/postulates/p3-reciprocity.md)).

## The referees' demand

The demand came out of the [blind reviews](../../method/review/_index.md) of that paper:

- **Round 1.** The referee's "toy-Lagrangian demand" was "adopted as acceptance criterion [#1](../../../notes/broken-born-theory.md)" ([`HANDOFF.md` §6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode)). [The handoff](../../history/documents/handoff.md)'s first open item adds that "both reviewers independently named it" ([§2](../../../HANDOFF.md#2-scientific-state-one-screen)). See [review rounds 1 and 2](../../method/review/rounds-one-and-two.md).
- **The withdrawn paper** states the criterion: "(1) exhibition of an action - a toy model suffices - in which rho is a genuine Noether symmetry, spontaneously broken, with eta the order parameter selecting both the position polarization and the hidden sector's electric description" ([its §6](../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria)). Its "hidden sector" is the separate copy of electromagnetism in which it placed its monopoles.
- **[Round 3](../../method/review/round-3/_index.md).** The referees' shared verdict became the program's main critique ([the 'framework does no work' critique](../../program/framework-does-no-work.md)), and the adjudication made the toy Lagrangian the next task, as the one item that could answer it: "Every referee across three rounds converges on 'the framework does no work'. The toy action is the only item that can change that, and it is acceptance criterion 1 for anything the program proposes." ([`review/round3-adjudication.md`](../../../review/round3-adjudication.md), decision 4; [round-3 decisions](../../method/review/round-3/decisions.md)).

The worklog fixed its success criteria before building anything, and the first of them is this page's distinction: "**S1 — symmetry of an action.** An explicit action S[fields] on which ρ acts as a symmetry: S is invariant, not merely related to its image by a unitary equivalence. Invariance is verified symbolically." ([`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md), "Success criteria"; [success criteria S0–S5](../../symmetry-breaking/toy-models/success-criteria.md)).

## The answer so far

[#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) records the criterion as "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential":

- "ρ is a symmetry of an explicit action, and η = ωK is the order parameter;"
- "the vacuum is stable with H dynamical;"
- "there is an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo)."

Still open there [O]: "a Monte Carlo with H dynamical; a derivation of the potential; locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4." See [acceptance criterion 1](../../symmetry-breaking/toy-models/acceptance-criterion.md) and [Open: a Monte Carlo with H dynamical](../../symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo.md). #11 does not qualify the second point; the toy note does. Its stable minimum keeps one flat direction, the squeeze line, and "It is not symmetry-protected" ([§4](../../papers/reciprocity-toy-models.md#4-quantum-stability); [the symplectic form and Sp(2d, ℝ)](symplectic-form.md#rotations-boosts-and-squeezes)).

The invariance is machine-checked. In [model I](../../symmetry-breaking/toy-models/coset-model/_index.md), the coset model of (H, K), "Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS, and the action is invariant (checked for generic symplectic S, so for ρ)" ([toy-model note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)), and [the gate](../../method/verification/the-gate.md) prints "all three terms invariant under rho" [V] ([Model I: action and symmetries](../../symmetry-breaking/toy-models/coset-model/action-and-symmetries.md)).

"Met" leaves two things uncovered, one clause of the referees' wording and the round-3 critique:

- **The electric sublattice.** The withdrawn paper's criterion and the handoff's open item required η to select "the hidden sector's electric description" (the paper's separate copy of electromagnetism; the handoff says "the electric sublattice") as well. The worklog's criteria and [#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) omit that clause. The root [`CLAUDE.md`](../../../CLAUDE.md) calls the toy Lagrangian "done to the referees' wording", and the clause remains unaddressed. [#11 §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) lists it first among what stays open for P.R.'s magnetic-mirror conjecture: "a mechanism by which one order parameter makes both choices (the electric-sublattice clause of acceptance criterion 1, never attempted; the toy models of §14 item 11 contain no gauge field)" ([what the conjecture needs](../../electric-magnetic-duality/magnetic-identification.md#what-it-needs)).
- **The round-3 critique.** The worklog's assessment: "The round-3 critique ('the framework does no work') is only partly answered. The toy makes the program's structures cohere (η as order parameter; τ as the polarization angle), but matter's x-locality still enters through the P4-type coupling." ([`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md), "Assessment against the predictions"; [Open: forced locality and the P4 lock](../../symmetry-breaking/strong-locality.md)).

## Symmetry, covariance and the twisted element

Model II shows the same distinction between its complex and real versions. In [the self-dual Grosse–Wulkenhaar model](../../symmetry-breaking/toy-models/grosse-wulkenhaar/_index.md) the position–momentum duality of [Langmann and Szabo](../../symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory.md) acts on the field φ through a matrix Π ([toy-model note §3](../../papers/reciprocity-toy-models.md#3-model-ii-the-self-dual-grossewulkenhaar-model)):

- **Complex fields: a symmetry.** The action satisfies S[Πφ] = S[φ], and "The duality Πφ is the α = π element of e^{−iαN}" (§3); the gate prints "complex model: S[Pi phi] = S[phi] (duality is a field symmetry)".
- **Real fields: a covariance.** "Πφ is not Hermitian, so the duality maps the real field space out of itself. The real action is only covariant: its quartic term is invariant in the alternating form Tr((ψψ†)²), ψ = Πφ." (§3; here † is the Hermitian adjoint, not the citation mark). Grosse and Wulkenhaar themselves describe the real action at Ω = 1 as invariant under the duality; "covariant only" is the toy note's reading (the referee of [review round 4](../../method/review/round-4.md), audit notes Step 1).

See [complex versus real fields: symmetry versus covariance](../../symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields.md).

Even a symmetry of the action does not by itself make the breaking of ρ physical. Model I has a second symmetry, K → −K, and "the twisted element ρ∘(K → −K) maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does. Breaking ρ is physical only once a coupling odd in K is present" ([toy-model note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)). See [the twisted element](../../symmetry-breaking/twisted-element.md).

## Standard references

Added by the wiki from model memory (†); the program's documents do not cite them.

- M. H. Stone (1930)† and J. von Neumann (1931)†: uniqueness of the representation of the canonical commutation relations.
- E. Noether (1918)†: symmetries of an action and conserved quantities.
- G. B. Folland, *Harmonic Analysis in Phase Space* (1989)†: the metaplectic representation.

## Used by

- [Acceptance criterion 1: the toy Lagrangian](../../symmetry-breaking/toy-models/acceptance-criterion.md) — the demand this distinction produced.
- [Success criteria S0–S5](../../symmetry-breaking/toy-models/success-criteria.md) — criterion S1 is the distinction itself.
- [P3: a reciprocity-invariant action](../../program/postulates/p3-reciprocity.md) — the program postulates a symmetry of the action, not a change of description.
- [Mandatory breaking: the uncertainty argument](../../symmetry-breaking/mandatory-breaking.md) — a vacuum can break only a symmetry of an action, not a change of description.
- [Model I: action and symmetries](../../symmetry-breaking/toy-models/coset-model/action-and-symmetries.md) — an explicit action invariant under ρ.
- [Complex versus real fields: symmetry versus covariance](../../symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields.md) — the distinction realized in model II.
- [The twisted element ρ∘(K → −K)](../../symmetry-breaking/twisted-element.md) — what a symmetry of the action still leaves open.
- [The 'framework does no work' critique](../../program/framework-does-no-work.md) — why the referees asked for the action.

## Sources

- [`CLAUDE.md`](../../../CLAUDE.md) "Since the handoff" — the toy Lagrangian "done to the referees' wording".
- [`wiki/papers/broken-born-checkpoint-v2.md` §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the criterion met in the referees' wording, and what remains open.
- [`wiki/papers/broken-born-checkpoint-v2.md` §11.4](../../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) — the electric-sublattice clause as the first open item of the magnetic-mirror conjecture [O].
- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — P3, the postulated symmetry of the action.
- [`wiki/papers/reciprocity-toy-models.md` §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)–[§3](../../papers/reciprocity-toy-models.md#3-model-ii-the-self-dual-grossewulkenhaar-model) — the explicit ρ-invariant action, the twisted element, symmetry versus covariance.
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) "Decisions" — decision 4: the toy Lagrangian as the next task.
- [`review/round4/referee/audit-notes.md`](../../../review/round4/referee/audit-notes.md) Step 1 — Grosse–Wulkenhaar's own wording on the real action.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen), [§6](../../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — the open item with the electric-sublattice clause; round 1 and the adoption of acceptance criterion 1.
- [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) "Success criteria", "Assessment against the predictions" — criterion S1; the 0+1 remark under S4; the partial answer to round 3.
- [`notes/knot-dark-matter-standalone.md` §1](../../../notes/knot-dark-matter-standalone.md#1-framework), [§6](../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) — the concession and the criterion as the withdrawn paper stated them.
- [`verify/toy_coset.py`](../../../verify/toy_coset.py), [`verify/toy_gw.py`](../../../verify/toy_gw.py) — the invariance checks for model I and the complex model II.
- [`wiki/papers/phase-space-diameter.md` §5](../../papers/phase-space-diameter.md#5-what-reciprocity-adds-invariant-area-inverted-shape) — the Möbius action on Gaussian packets [S]; the map with Born length λ symplectic for every λ [T][V], and two such maps differing by a squeeze [D][V], both checked in [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py).
