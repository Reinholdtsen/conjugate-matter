---
title: "P5: the vacuum selects a polarization"
weight: 70
status: alive
description: "Our vacuum is x-tilted and the mirror vacuum is equally lawful; Freidel–Leigh–Minic stated the preferred-polarization idea, and the toy models add that selection needs a potential."
provenance: [P]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "notes/broken-born-theory.md §1"
  - "notes/debt1a-geometric-core.md §B"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §4"
  - "verify/toy_s4.py"
  - "CLAUDE.md 'Since the handoff'"
  - "popsci/universes-other-half.md 'An asymmetry that cannot be avoided'"
---

*P5 is the program's axiom of spontaneous breaking: the vacuum of the universe selects a polarization, a choice of which half of the phase-space coordinates count as position, and ours is the one organized around position in the ordinary sense ("x-tilted"). The mirror choice, a vacuum organized around momentum, satisfies the same laws equally well. Which one occurs is a property of the state, not of the laws, as the axes of an ice crystal are a property of the crystal rather than of the laws governing water. Freidel, Leigh and Minic had already described a preferred polarization as breaking Born's symmetry; the program's addition is to treat the choice as spontaneous symmetry breaking. The toy models qualify the axiom: with only the symplectic form fixed the choice is a continuous angle, like an ice axis that could point anywhere, and a definite polarization needs an additional potential.*

**Status:** Alive — [P] — a postulate of #11 §4. The toy models show a consistent realization, not a test: in model I with a bounded ρ-preserving potential, the frozen-H reduction has an ordered ℤ₂ phase in 1+1 dimensions (Monte Carlo, `verify/toy_s4.py`, [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Key facts

- Statement (#11 §4):

  ```text
  P5  The vacuum selects a polarization; ours is x-tilted; the mirror
      vacuum is equally lawful.                                      [P]
  ```

- Lab-notebook statement (#1 §1, v0.1): "**P5 (Spontaneous breaking).** The vacuum selects a Lagrangian polarization of 𝒫; ours is x-tilted. The choice is spontaneous: the mirror vacuum is an equally good solution. **[P]**" See [Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations).
- Why some choice is claimed necessary (#11 §3): "[x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization." See [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking). That ours is the x-tilted vacuum is part of the postulate, not derived.
- Credit (#11 §3, since v2.2): Freidel, Leigh and Minic wrote "if all probes agree on what we mean by space-time, then we have broken Born duality — there is a preferred choice of polarization, the space-time one" [26S, p. 3]; "They treat the breaking as kinematical and call the choice 'a dynamical question'." See [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality).
- The space of choices: under [P2′](/wiki/program/postulates/p2-prime) the vacuum's choice ranges over Λ(d) ≅ U(d)/O(d), [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) (#5 §B). With only ω rigid, "ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (#11 §4). See [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).
- Selection needs a potential (toy note §4): "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ." "To get a definite polarization we add a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group." With it, the frozen-H Monte Carlo gives "⟨|m|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667": an ordered ℤ₂ phase. See [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman), [the Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) and [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).
- A lead on position over momentum (toy note §3; listed in `CLAUDE.md` as an open end): in the real Grosse–Wulkenhaar model the two sign-vacua are classically degenerate but split at one loop, F(+) − F(−) = 2.634, and "The preferred vacuum, diag(a₀, −a₁), is the β = π configuration, the one sharper in position." The note adds: "This is explicit, not spontaneous selection, because the real model is not duality-symmetric". See [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — the statement and the Goldstone-angle refinement; §3 — mandatory breaking and the Freidel–Leigh–Minic credit
- `notes/broken-born-theory.md` §1 — the v0.1 statement
- `notes/debt1a-geometric-core.md` §B — the space of choices Λ(d) under P2′
- `papers/reciprocity-toy-models.md` §3–§4 — the potential, the ordered ℤ₂ phase and the real-model lead
- `verify/toy_s4.py` — the Monte Carlo numbers, gated
- `CLAUDE.md` 'Since the handoff' — the real-model preference listed as a lead
- `popsci/universes-other-half.md` 'An asymmetry that cannot be avoided' — the ice-crystal picture (popular article; not a status source)
