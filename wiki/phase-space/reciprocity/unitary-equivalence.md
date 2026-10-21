---
title: "Unitary equivalence versus Noether symmetry"
weight: 50
status: established
description: "By the Stone–von Neumann theorem the irreducible representations of the canonical commutation relations are unitarily equivalent, so ρ is ordinarily a change of description; why the referees demanded an action in which it is a genuine symmetry."
sources:
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §6"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §3"
  - "HANDOFF.md §6"
  - "review/round3-adjudication.md 'Decisions'"
---

*A map like [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) can relate to a physical theory in two different ways. It can be a change of description — the same physics written in other variables, as a Fourier transform rewrites a waveform as a spectrum — or it can be a symmetry of the dynamics: an operation that leaves a specific action unchanged and therefore constrains what the theory can do (a Noether symmetry). In ordinary quantum mechanics ρ is the first kind, because all the standard ways of representing the position–momentum commutation rules are equivalent. The program needs the second kind, and its referees made exhibiting such an action the first acceptance criterion for anything it proposes; the toy models were built to meet it.*

**Status:** Established — the equivalence is textbook quantum mechanics [T], stated here from general knowledge — the distinction was raised by the referees and conceded in #14 §1; #11 §14 item 11 records the criterion as met in the referees' wording by the toy models.

## Key facts

- **The theorem [T].** By the Stone–von Neumann theorem, for finitely many degrees of freedom the irreducible representations of the canonical commutation relations (in their exponentiated, Weyl form) are all unitarily equivalent. Since ρ leaves [the canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator) unchanged, it maps one such representation to another, and the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) is the unitary that relates them.
- **The concession.** #14 §1: "as usually encountered, rho is a unitary equivalence between representations of the canonical commutation relations, not a Noether symmetry of a specified action. The framework's claim is that rho is a genuine symmetry of an underlying action, spontaneously broken".
- **The demand.** Round 1's referee asked for a toy Lagrangian, which was "adopted as acceptance criterion #1"; the handoff records that "both reviewers independently named it" (`HANDOFF.md` §6, §2; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)). #14 §6 states it as "exhibition of an action - a toy model suffices - in which rho is a genuine Noether symmetry, spontaneously broken, with eta the order parameter selecting both the position polarization and the hidden sector's electric description". After round 3 it became the next task, because it is "the only item that can change" the referees' verdict that the framework does no work (round-3 adjudication, decision 4; [the 'framework does no work' critique](/wiki/program/framework-does-no-work)).
- **The answer so far.** #11 §14 item 11: "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential … ρ is a symmetry of an explicit action, and η = ωK is the order parameter". The clause about the hidden sector's electric description is not addressed — see [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion).
- **Symmetry versus covariance, in a model.** In the self-dual Grosse–Wulkenhaar model the duality is a genuine field symmetry for complex fields, while for real fields "the duality is only a covariance" (toy-model note, abstract and §3) — see [complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields).
- **What a symmetry of the action still leaves open.** In model I, "a twisted combination of ρ with that flip leaves the vacuum invariant. Breaking ρ becomes physical only once a coupling odd in K is present" (toy-model note abstract, §2) — see [the twisted element](/wiki/symmetry-breaking/twisted-element).

## Used by

- [Acceptance criterion 1: the toy Lagrangian](/wiki/symmetry-breaking/toy-models/acceptance-criterion) — the demand this distinction produced.
- [P3: a reciprocity-invariant action](/wiki/program/postulates/p3-reciprocity) — the program postulates a symmetry of the action, not a change of description.
- [Complex versus real fields: symmetry versus covariance](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields) — the distinction realized in model II.
- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — an explicit action invariant under ρ.
- [The 'framework does no work' critique](/wiki/program/framework-does-no-work) — why the referees asked for the action.

## Sources

- `papers/broken-born-checkpoint-v2.md` §14 item 11 — the criterion met in the referees' wording, and what remains open.
- `papers/broken-born-checkpoint-v2.md` §4 — P3, the postulated symmetry of the action.
- `papers/reciprocity-toy-models.md` §1–§3 — the explicit ρ-invariant action, the twisted element, symmetry versus covariance.
- `review/round3-adjudication.md` "Decisions" — decision 4: the toy Lagrangian as the next task.
- `HANDOFF.md` §6 — round 1 and the adoption of acceptance criterion 1.
- `notes/knot-dark-matter-standalone.md` §1, §6 — the concession and the criterion as #14 stated them (withdrawn paper).
