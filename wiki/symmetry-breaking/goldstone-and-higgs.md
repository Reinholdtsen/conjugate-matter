---
title: "Goldstone modes and the Higgs mechanism"
weight: 20
status: established
description: "Massless modes of broken continuous symmetries, pseudo-Goldstones and Hessian rank; gauge fields that eat Goldstones and become massive; Stückelberg fields and inverse-Higgs constraints."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "verify/toy_coset.py 'Spectrum'"
---

*A Goldstone mode is a massless excitation that appears when a continuous symmetry of the laws is broken by the ground state: moving along the family of equally good ground states costs no energy, so waves of that motion carry no mass. If a small explicit term tilts the family, the mode acquires a small mass and is called a pseudo-Goldstone mode. When the broken symmetry is a gauge symmetry, the Higgs mechanism applies instead: the gauge field absorbs the would-be Goldstone modes as extra polarizations and becomes massive. The program uses all three ideas: the polarization angle is a Goldstone direction in its toy models, and its momentum graviton X gets its mass from a gravitational version of the Higgs mechanism.*

**Status:** Established — [T] — textbook field theory, explained here from general knowledge; the program's applications are the Hessian count of the coset toy model (`verify/toy_coset.py`) and the Debt-1 derivation of X's mass [D + T] (#11 §7.1).

## Key facts

- **Goldstone modes [T].** When a continuous symmetry is spontaneously broken, each flat direction of the vacuum manifold carries a massless mode (Goldstone's theorem, for internal symmetries of a Lorentz-invariant theory). At a vacuum the Hessian of the potential vanishes along those directions: its rank counts the massive modes and its null directions are the flat ones. See [Spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking).
- **The count in model I.** "The potential's Hessian has rank 1 at the vacuum. That leaves three Goldstone directions: the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)." (toy-model note §2). The worklog marks this "Spectrum [V]", and the gate prints the Hessian eigenvalues [0, 4, 0, 0] (`verify/toy_coset.py`; [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). The compact direction is the program's [polarization angle](/wiki/symmetry-breaking/goldstone-angle).
- **Pseudo-Goldstone modes [T].** A small explicit breaking tilts the vacuum manifold and gives the would-be Goldstone mode a small mass. The worklog's reading of model I with its ρ-preserving potential: the toy supports broken reciprocity in the form "a pseudo-Goldstone polarization angle with a ρ-symmetric potential", not "only ω rigid, nothing else" (worklog, 'Chunk 3 results').
- **A zero mode that no symmetry protects.** With the bounded potential V_b and H dynamical, one Hessian eigenvalue is 0; the toy-model note says this zero mode "is not symmetry-protected" (§4). The round-4 adjudication called it an exact symmetry; the note v2 outranks it ([The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential); [Conflicts between sources](/wiki/history/documents/source-conflicts)).
- **The Higgs mechanism and Stückelberg fields [T].** If the broken symmetry is a gauge symmetry, the would-be Goldstone modes are not physical massless particles; they become the extra polarizations of the gauge field, which becomes massive. Written with those modes kept explicit as Stückelberg fields, the massive theory keeps a gauge symmetry, and fixing the gauge removes them.
- **The gravitational Higgs mechanism of X [D + T].** "(iii) The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale." (#11 §7.1). The Debt-1 note: "the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a massive spin-2 with its five polarizations" [D — structural] (Chunk A-ii §3). See [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) and [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms).
- **What is eaten, and τ.** The later note words it differently: "the Higgsing of the dual diffeomorphisms eats the vector π_μ and the longitudinal scalar of the λ-gradient sector", and "τ is not eaten [D — leading order]" (Chunk A-iv §3); #11 §7.5 has "τ un-eaten (compact J-sector, not the Stückelberg sector)". The two wordings of what X eats are not reconciled, and #11 §7.1 follows the first ([τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten); the residual mixing is open problem 6, [Open: τ–Stückelberg mixing](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing)).
- **Inverse-Higgs constraints [T].** When spacetime symmetries break, some Goldstone fields can be written as derivatives of others and removed, so there can be fewer independent Goldstone modes than broken generators. The program expects this for its vacuum moduli: "Λ(d) σ-modes (10: τ plus nine, of which inverse-Higgs constraints likely eliminate most [O])" (Debt-1 Chunk A §D; [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content)).

## Used by

- [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) — the vacuum's polarization as a flat direction.
- [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua) — three Goldstone directions from a rank-1 Hessian.
- [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) — the pseudo-Goldstone angle and the unprotected zero mode.
- [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) — the Yukawa analogy: masses from a Higgs vacuum value.
- [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) — X becomes massive by absorbing the Goldstones of the broken dual diffeomorphisms.
- [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten) — τ survives as the light field.
- [Open: τ–Stückelberg mixing](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing) — residual mixing with the eaten modes.
- [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content) — the inverse-Higgs accounting of the nine heavy moduli.
- [Fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force) — τ as a derivatively coupled (pseudo-)Goldstone.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.1, §7.5 — X eats the Goldstones of the broken dual diffeomorphisms; τ un-eaten
- `papers/reciprocity-toy-models.md` §2, §4 — model I's rank-1 Hessian and three Goldstone directions; V_b's unprotected zero mode
- `notes/debt1a-ii-X-classification.md` §3 — the gravitational Higgs mechanism, mass M_X
- `notes/debt1a-iv-beta-coefficients.md` §3 — what is eaten; τ not eaten at leading order
- `notes/debt1a-geometric-core.md` §D — the Λ(d) σ-modes and inverse-Higgs constraints [O]
- `notes/toy-lagrangian.md` 'Chunk 3 results' — "a pseudo-Goldstone polarization angle with a ρ-symmetric potential"
- `verify/toy_coset.py` — the Hessian-rank check
