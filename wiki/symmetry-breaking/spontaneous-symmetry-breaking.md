---
title: "Spontaneous symmetry breaking"
weight: 10
status: established
description: "A symmetric law with an asymmetric ground state: order parameter, vacuum manifold and stabilizer, and the difference between spontaneous and explicit breaking (spurions)."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §3"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/broken-born-theory.md §3"
  - "verify/toy_coset.py S2–S3"
---

*Spontaneous symmetry breaking is the situation in which the equations of a system are unchanged by some transformation but its lowest-energy state is not. A cooled magnet is the standard example: the laws governing its atoms treat every direction alike, yet the magnet ends up magnetized along one direction, and any other direction would have been an equally good ground state. The Broken-Born program uses this pattern for its hard core, proposing that the position–momentum symmetry of quantum mechanics is exact in the laws and broken by the vacuum. This page is the textbook background; the program's use of it is on the pages that follow in this section.*

**Status:** Established — [T] — standard field theory, explained here from general knowledge; the program applies it in #11 §3 and turns it into the pass/fail criteria S1–S3 of its toy models, checked in `verify/toy_coset.py`.

## Key facts

- **The pattern [T].** A symmetry group G of the laws is spontaneously broken when the ground state is not invariant under G. G then maps each ground state to another one, and the ground states form a vacuum manifold, the orbit G/G₀, where the stabilizer G₀ is the subgroup that leaves a chosen ground state fixed. The program's instance: "The program: ρ is exact and spontaneously broken." (#11 §3; see [the hard core](/wiki/program/hard-core) and [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)).
- **The order parameter [T].** A quantity that transforms nontrivially under G and has a nonzero expectation value in a broken ground state, such as a magnet's magnetization. The toy-model work turned this into a test: "S3 — η as order parameter. A local operator built from η (equivalently the real structure K, with η = ωK) has a nonzero expectation value in each vacuum and is odd under ρ." (worklog, 'Success criteria'; see [the order parameter](/wiki/symmetry-breaking/order-parameter)).
- **A symmetry, not a change of description.** Criterion S1 asks for "An explicit action S[fields] on which ρ acts as a symmetry: S is invariant, not merely related to its image by a unitary equivalence." This is the distinction drawn at [Unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence).
- **Degenerate vacua.** Criterion S2: "The minima of S form a set on which ρ acts without fixed points: no vacuum is ρ-invariant, and ρ maps each vacuum to another one." (worklog, 'Success criteria').
- **A worked case.** In the coset toy model at H = 1 the vacua are K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]; "The vacuum manifold is the upper half-plane times this circle", and "The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}" (toy-model note §2, whose results are "All checked symbolically"). The gate's stabilizer check in `verify/toy_coset.py` adds "(so the orbit is 3-dimensional)" ([Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)).
- **Spontaneous versus explicit [T].** Explicit breaking puts a non-symmetric term into the laws themselves. A fixed background structure that does this can be treated as a spurion: a parameter that would restore the symmetry if it were allowed to transform along with the fields. The lab notebook (v0.1) gave τ's potential this kind of origin, "the explicit breaking of Grassmannian rotations by the rigid ω (P2)" [P/O], an origin lost when P2 was replaced ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). The real Grosse–Wulkenhaar model's one-loop vacuum preference is "explicit, not spontaneous selection, because the real model is not duality-symmetric" (toy-model note §3; [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)).
- **Dimension matters.** In 0+1 dimensions tunnelling restores any symmetry, and in 1+1 a compact continuous symmetry cannot break; see [The Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman).

## Used by

- [The hard core](/wiki/program/hard-core) — Born reciprocity as an exact symmetry broken by the vacuum.
- [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection) — the selection postulate.
- [Mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking) — why some polarization must be selected.
- [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) — what carries the breaking.
- [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria) — S1–S3 as the operational definition.
- [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua) — a vacuum manifold and stabilizer computed explicitly.
- [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead) — an explicit, not spontaneous, selection.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — the program's statement that ρ is exact and spontaneously broken
- `papers/reciprocity-toy-models.md` §1–§3 — the toy setting; model I's vacuum manifold and stabilizer; explicit selection in the real model II
- `notes/toy-lagrangian.md` 'Success criteria' — criteria S1–S3, the operational definition used by the toy models
- `notes/broken-born-theory.md` §3 — v0.1's explicit-breaking origin of V(τ) (superseded)
- `verify/toy_coset.py` — the S2 and S3 checks for model I
