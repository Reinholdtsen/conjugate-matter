---
title: "Mandatory breaking: the uncertainty argument"
weight: 40
status: alive
description: "Because [x, p] = iℏ rules out joint locality, any world with local physics must select a Lagrangian polarization ('the magnet must point'); the argument requires some polarization but not which one, and v2.2's toy models qualify it."
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §5"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "review/round4/referee/audit-notes.md 'Step 2(a)' F3"
  - "notes/broken-born-program-v1.md §1"
  - "notes/knot-dark-matter-standalone.md §1"
  - "CLAUDE.md 'Since the handoff'"
  - "popsci/angle-of-the-mirror.md 'The wager'"
  - "popsci/universes-other-half.md 'An asymmetry that cannot be avoided'"
---

*Mandatory breaking is the program's argument that Born reciprocity, the exchange of position and momentum, cannot remain unbroken in any world that contains local physics. The uncertainty principle rules out anything being sharp in both position and momentum at once, much as a waveform and its spectrum cannot both be narrow. A world whose interactions are local must therefore be local in one variable at the cost of the other; in [#11](/wiki/history/documents/checkpoint)'s phrase, "the magnet must point". The argument is why the program treats the breaking as forced rather than optional, while leaving open which of the two variables ends up as position. Since v2.2 it carries qualifications from the toy models: the polarization is a continuous angle, a definite polarization needs an added potential, and the breaking has physical effect only once matter couples to the sign of the order parameter.*

**Status:** Alive — untagged in #11 §3 (part of the [hard core](/wiki/program/hard-core), whose postulates are [P]) — a qualitative argument, not derived from a model and not machine-checked; its v2.2 qualifications come from the toy models and carry [D][V] where #11 §4 tags them ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Statement

> The program: ρ is exact and spontaneously broken. The breaking is *mandatory*: [x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization. The magnet must point. (#11 §3)

The sentence carries no tag. It joins three ideas: [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ: (x, p) → (p, −x) as an exact symmetry; the [canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator) [x, p] = iℏ and the uncertainty principle it implies; and a [Lagrangian polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations), a choice of which phase-space variables count as position. The last clause is the analogy of [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking): the laws of a magnet single out no direction, but a cooled magnet is magnetized along some direction all the same.

## The argument, step by step

The checkpoint gives the argument in one sentence. Spelled out, it runs in five steps; the premises are from #11 §3 and the [v1 paper](/wiki/history/documents/checkpoint)'s version of the same passage (#9 §1).

1. **The symmetry is exact in the kinematics.** "Quantum kinematics is exactly invariant under ρ: (x,p) → (p,−x); the Fourier transform implements it unitarily [1†, 2†]." (#11 §3). The commutator does not distinguish the two variables: with x′ = p and p′ = −x, [x′, p′] = [p, −x] = [x, p] = iℏ [T], which the v1 paper puts as "the canonical commutator is blind to it" (#9 §1). See [the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform).
2. **The asymmetry is in the dynamics.** "The asymmetry is dynamical: x-local interactions, the momentum-space mass shell, and general relativity's flat momentum fibers" (#11 §3). In the v1 paper's words, "Hamiltonians are p²/2m + V(x), interactions are local in x" (#9 §1). This is [Born's question](/wiki/program/borns-question): why physics uses only half of a symmetry its kinematics has.
3. **Nothing is sharp in both variables.** For every state Δx · Δp ≥ ℏ/2 [T]. The momentum wavefunction is the Fourier transform of the position wavefunction, and a function and its Fourier transform cannot both be narrow, the same trade-off as a signal's duration against its bandwidth [T]. "Joint locality" is locality in both variables at once; the v1 paper: "nothing can be local in both variables at once" (#9 §1).
4. **Local physics singles out one variable.** An interaction is local in x when it couples a field only at coinciding positions, as a contact term ∫|ψ(x)|⁴ dx does; written in momentum, the same term couples all momenta together [T]. The toy models give a worked pair. One coupling built from the vacuum's structures becomes "∫|ψ(x)|⁴ dx (local in x)" in one vacuum and "∫|ψ̃(p)|⁴ dp" in its mirror image (toy-model note §5; [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)). An interaction can be local in one variable or in the other, not in both.
5. **So a polarization must be selected.** A world with local interactions has to treat one Lagrangian subspace, one maximal set of mutually commuting variables, as position. Since the laws do not distinguish the candidates, the selection belongs to the state: "The magnet must point."

The argument is qualitative. Its premise, that the world's physics is local, is an observation, and its conclusion that the selection belongs to the vacuum rather than to the laws is the program's reading (below). No model derives it and no script checks it.

## What the argument requires, and what it leaves open

**Some polarization, not a particular one.** The argument rules out the symmetric option; it does not say which variable is sharp. The postulate [P5](/wiki/program/postulates/p5-spontaneous-selection) leaves that to the vacuum: "P5 The vacuum selects a polarization; ours is x-tilted; the mirror vacuum is equally lawful. [P]" (#11 §4). Why our vacuum is x-tilted is not answered by the argument.

**A symmetry of an action, first.** A vacuum can break only a symmetry that the dynamics has. In ordinary quantum mechanics ρ is a change of description, a unitary equivalence, not a symmetry of an action ([unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence)). The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) states the argument with that condition attached: "The breaking, if the symmetry exists, is compulsory in one respect: the uncertainty principle forbids states symmetric between the variables, so some polarization must be selected; which one is the spontaneous datum." (#14 §1). The toy models supply explicit actions in which ρ is a symmetry, and #11 §14 item 11 records the referees' criterion as met in their wording ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)).

**Spontaneous, as the program's reading.** That a preferred polarization breaks Born duality is not new, and #11 §3 says so since v2.2: "the idea that a preferred polarization breaks Born duality is Freidel, Leigh and Minic's — 'if all probes agree on what we mean by space-time, then we have broken Born duality — there is a preferred choice of polarization, the space-time one' [26S, p. 3]. They treat the breaking as kinematical and call the choice 'a dynamical question'. This program's addition is to read it as *spontaneous* breaking, with η as the order parameter". The worklog's literature check had found the quotation and required the credit: "#11 §3 must cite FLM for the idea. What is the program's own: the order-parameter (spontaneous) formulation and its consequences." ('Chunk 4'; FLM is Freidel–Leigh–Minic). Freidel, Rudolph and Svoboda suggest the choice "might be subject to a dynamical selection rule" (toy-model note §1). See [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality) and [the order parameter](/wiki/symmetry-breaking/order-parameter).

## Qualifications from the toy models (v2.2)

The toy models are two explicit field theories with ρ as an exact symmetry, built to see what form the breaking takes ([toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models)). They are in d = 1, phase space ℝ², on a 1+1-dimensional base. #11 v2.2 records what they found as a refinement of its postulate [P2′](/wiki/program/postulates/p2-prime):

> *Refinement (v2.2, from the toy models):* with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]. Two things follow. A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η. And the breaking of ρ is physical only once matter couples to the sign of K (P4): without such a coupling, a twisted element ρ∘(K → −K) leaves the vacuum invariant (`papers/reciprocity-toy-models.md` §2, §4). (#11 §4)

Each part changes what "the magnet must point" can mean.

1. **The magnet is a planar one.** The selection is an angle on a circle, not a choice between two settings: "The x-sharp and p-sharp vacua are joined by a flat direction" (worklog, 'Chunk 2 results'). The breaking is like that of a planar magnet, whose direction can turn continuously, rather than an up-or-down Ising spin. See [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).
2. **Pointing needs a potential.** In 1+1 dimensions a compact continuous angle cannot order ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). [Model I](/wiki/symmetry-breaking/toy-models/coset-model) orders only after "a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" is added; with it the [lattice simulation](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) of [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) finds an ordered ℤ₂ phase (toy-model note §4). #11 §10: "A definite polarization requires the ρ-preserving potential this section posits." The potential is not derived ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)).
3. **Pointing is physical only through matter.** Model I has a second symmetry, K → −K, and the combined element ρ∘(K → −K) leaves the vacuum unchanged. Until matter couples to the sign of K, which of the two symmetries one calls broken is, in the [round-4](/wiki/method/review/round-4) referee's words, "a labelling choice" (`review/round4/referee/audit-notes.md`, Step 2(a), F3). See [the twisted element](/wiki/symmetry-breaking/twisted-element) and [P4](/wiki/program/postulates/p4-polarized-matter).
4. **Quantization can undo it.** In the complex [Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar), "the breaking does not survive quantization: every condensate phase is an exact flat direction, and the condensate is a localized lump with no volume factor" (toy-model note, Abstract; [quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).

The qualifications narrow the claim; none of them removes it. In model I with [the bounded potential](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential), #11 §14 item 11 records that "ρ is a symmetry of an explicit action, and η = ωK is the order parameter", that "the vacuum is stable with H dynamical", and that "there is an ordered ℤ₂ phase in 1+1 in the frozen-H reduction (Monte Carlo)". The root `CLAUDE.md` calls the toy Lagrangian "done to the referees' wording".

## Open: locality is assumed, not derived

The argument runs from locality to a selected polarization. The toy models test the converse direction, from a selected polarization to local matter, and find only a weak form of it. A matter coupling built from H and K makes interactions local in x in one vacuum and in p in the other, "the analogue of Yukawa-generated masses. A mechanism forcing such a coupling is not given." (toy-model note, Abstract; [Yukawa-generated masses](/wiki/gravity/spin-2-fields/yukawa-forces#a-name-collision-the-yukawa-coupling)). The worklog's conclusion on that test:

- "**Strong form (locality forced, not chosen): not achieved.** It is also open in the literature."
- "So in the toy, the program's explanation of 'forces fade with distance' amounts to this: our matter is the x-polarized species. The explanatory gain is that x-locality comes packaged with a p-local mirror sector, the program's dark-matter claim. It does not derive x-locality from nothing." ('Chunk 4')

#11 §14 item 11 lists "locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4" as still open [O], with "a Monte Carlo with H dynamical" and "a derivation of the potential". See [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) and [open problems](/wiki/status/open-problems).

## Wordings in other documents

- **The v1 paper (#9 §1, superseded as reference by #11).** "The uncertainty principle guarantees the breaking is mandatory, not optional: nothing can be local in both variables at once, so any universe with local physics must pick a polarization. The choice is the magnet's direction."
- **The withdrawn manuscript (#14 §1).** The conditional form quoted above, "if the symmetry exists".
- **The popular articles.** #10: "The uncertainty principle forbids anything from being sharp in position and momentum at once, so any universe with local physics — atoms, chemistry, us — must choose which half of the symmetry to build on." ('The wager'). #12: "The settling was compulsory, since the uncertainty principle allows no symmetric option; the particular outcome was not." ('An asymmetry that cannot be avoided'). #12 presents the framework as if it were confirmed and omits the v2.2 qualifications: the Goldstone angle, the potential, the coupling to the sign of K and the quantum restoration in the complex model. It is never a source for the claim's status ([the popular articles](/wiki/history/documents/popular-articles)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — the argument, untagged; ρ exact in the kinematics; the dynamical asymmetry; the Freidel–Leigh–Minic attribution [26S]
- `papers/broken-born-checkpoint-v2.md` §4 — P5; the v2.2 refinement of P2′; §10 — "A definite polarization requires the ρ-preserving potential this section posits"; §14 item 11 — what the toy shows and what is still open
- `papers/reciprocity-toy-models.md` Abstract — the restoration in the complex model II; matter locality only in the Yukawa-like form; §1 — Freidel–Rudolph–Svoboda; §4 — the ρ-preserving potential and the ordered phase; §5 — the coupling that is local in x in one vacuum and in p in the other
- `notes/toy-lagrangian.md` 'Chunk 2 results' — the x-sharp and p-sharp vacua joined by a flat direction; 'Chunk 4 (in progress, 2026-10-19): S5' — the credit to Freidel–Leigh–Minic; the strong form not achieved
- `review/round4/referee/audit-notes.md` Step 2(a), F3 — without a K-odd coupling, "a labelling choice"
- `CLAUDE.md` 'Since the handoff' — the toy Lagrangian "done to the referees' wording"
- `notes/broken-born-program-v1.md` §1 — the v1.0 wording (superseded as reference)
- `notes/knot-dark-matter-standalone.md` §1 — the conditional wording (withdrawn manuscript)
- `popsci/angle-of-the-mirror.md` 'The wager'; `popsci/universes-other-half.md` 'An asymmetry that cannot be avoided' — the plain-language versions, without the v2.2 qualifications (never a status source)
