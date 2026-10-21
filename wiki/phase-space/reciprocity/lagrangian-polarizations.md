---
title: "Lagrangian subspaces and polarizations"
weight: 60
status: established
description: "Maximal subspaces on which ω vanishes; choosing one is choosing which coordinates count as 'position', the choice the program says the vacuum makes."
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/reciprocity-toy-models.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §1"
  - "notes/debt1a-geometric-core.md §B"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "verify/toy_s5.py"
---

*A Lagrangian subspace of phase space is a set of directions, half the dimension of phase space, on which the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) vanishes. Choosing one, a polarization, is choosing which coordinates count as "position": the ordinary position axis is one Lagrangian subspace, the momentum axis is another, and there are infinitely many tilted ones in between. A quantum state can be written as a wavefunction over any of them. The program's postulates say that the vacuum carries one such choice, and that ours is tilted toward position.*

**Status:** Established — standard symplectic geometry [T] — the d = 1 statements the toy models rely on are checked in `verify/toy_s5.py` (see [the toy-model scripts](/wiki/method/verification/toy-model-scripts)); what the program does with the choice is its own claim.

## Key facts

- **Definition [T].** In phase space ℝ^{2d}, a Lagrangian subspace is a d-dimensional subspace on which ω vanishes. For d = 1 every line qualifies; the toy-model check reads "L+ and L- are Lagrangian (w vanishes on each line trivially in d = 1)" (`verify/toy_s5.py`).
- **The program's use.** #11 §3: "[x,p] = iℏ forbids joint locality, so any world with local physics must select a Lagrangian polarization." See [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking). P5 in the lab notebook: "The vacuum selects a Lagrangian polarization of 𝒫; ours is x-tilted. The choice is spontaneous: the mirror vacuum is an equally good solution." [P] (#1 §1; [P5](/wiki/program/postulates/p5-spontaneous-selection)).
- **Polarization from a real structure.** Toy-model note §1: "A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK. Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is 'position'." See [the order parameter](/wiki/symmetry-breaking/order-parameter) and [the section condition](/wiki/symmetry-breaking/section-condition).
- **The space of all choices.** "The space of Lagrangian polarizations of ℝ^{2d} is the Lagrangian Grassmannian Λ(d) ≅ U(d)/O(d), compact, of dimension d(d+1)/2 = 10 for d = 4." [T] (#1 §2) — see [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian).
- **When too much is frozen.** With both ω and η rigid, the compatible polarizations are "discrete — the 2^d coordinate-type splittings" (#5 §B), so no continuous family remains — the reason [original P2](/wiki/program/postulates/original-p2) was superseded.
- **Prior art and a second arena.** Freidel, Leigh and Minic "describe spacetime as a choice of Lagrangian" (toy-model note §1; [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)). In charge space, mutual locality picks out "a Lagrangian sublattice", and choosing a duality frame "is choosing a Lagrangian polarization of charge space" [D — structural; math T] (#11 §11.3; [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)).

## Used by

- [Mandatory breaking: the uncertainty argument](/wiki/symmetry-breaking/mandatory-breaking) — any world with local physics must select a polarization.
- [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection) — ours is x-tilted, the mirror vacuum equally lawful.
- [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) — choosing K is choosing which line is "position".
- [The section condition: what η fixes](/wiki/symmetry-breaking/section-condition) — matter confined to one Lagrangian null line.
- [Original P2 (superseded)](/wiki/program/postulates/original-p2) — rigid η leaves only discrete polarizations.
- [The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice) — a duality frame as a Lagrangian polarization of charge space.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — the mandatory selection of a Lagrangian polarization.
- `papers/broken-born-checkpoint-v2.md` §11 — Lagrangian sublattices and duality frames in charge space.
- `papers/reciprocity-toy-models.md` §1 — K's eigenlines as η's Lagrangian null lines; Freidel–Leigh–Minic's "choice of Lagrangian".
- `notes/broken-born-theory.md` §1, §2 — P5; Λ(d) ≅ U(d)/O(d) and its dimension.
- `notes/debt1a-geometric-core.md` §B — the discrete splittings under strict P2.
- `verify/toy_s5.py` — the d = 1 Lagrangian-line checks.
