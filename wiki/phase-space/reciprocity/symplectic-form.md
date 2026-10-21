---
title: "The symplectic form and Sp(2d, ℝ)"
weight: 20
status: established
description: "The antisymmetric pairing ω of position and momentum, the group Sp(2d, ℝ) that preserves it with its rotations, boosts and squeezes, and ω's rigidity read as the constancy of ℏ."
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "notes/debt1a-geometric-core.md §A"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "notes/broken-born-theory.md §2"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-ii-X-classification.md §1"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "verify/toy_coset.py"
---

*The symplectic form ω is the antisymmetric pairing of positions with momenta that underlies Hamiltonian mechanics and the quantum commutator, and the symplectic group Sp(2d, ℝ) is the set of linear maps of phase space (d positions, d momenta) that preserve it. The group contains rotations of phase space — the quarter-turn [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) is one — together with boosts and squeezes. In the program ω is the one structure held fixed: its corrected postulate reads the rigidity of ω as the constancy of Planck's constant, and every other piece of phase-space geometry is allowed to vary.*

**Status:** Established — standard mathematics [T]; its rigidity in the program is a postulate [P] (P2′, #11 §4) — the toy model's invariance under a generic symplectic matrix is machine-checked [V] in `verify/toy_coset.py` (see [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Key facts

- **Standard form.** In the (x, p) block basis ω = [[0, 1], [−1, 0]], in d × d blocks (#1 §2, with d = 4; the toy-model note §1, with d = 1). A matrix S is symplectic when Sᵀ ω S = ω [T]; these matrices form Sp(2d, ℝ). The quantum version of the pairing is [the canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator).
- **Rotations, boosts, squeezes.** ρ = [[0, 1], [−1, 0]] "is symplectic and squares to −1" (toy-model note §1); it lies in the compact SO(2) of rotations, to which "Mermin–Wagner [13, 14] applies" in 1+1 dimensions (§4; [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). The non-compact directions are boosts and squeezes. Along a boost family "H = SᵀS, K = S⁻¹K_ref S" the naive potential is unbounded below ([obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)); for [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) the squeeze line H = diag(y, 1/y) is a zero mode and "Boosts are penalized" (§4).
- **The toy's symmetry group.** "Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS, and the action is invariant (checked for generic symplectic S, so for ρ)" (toy-model note §2; [model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)).
- **Rigidity as the constancy of ℏ.** P2′: "Only ω is rigid (symplectic rigidity ≡ constancy of ℏ)." [P] (#11 §4); #5 §B: "Freeze ω only — that is genuinely ℏ". See [P2′](/wiki/program/postulates/p2-prime). The [original P2](/wiki/program/postulates/original-p2) froze the neutral metric η as well and was superseded.
- **What a rigid ω leaves.** The positive metrics compatible with ω alone form the Siegel domain Sp(2d,ℝ)/U(d) (#5 §C; [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)). The rigid group "contains Z → Z + B (B symmetric)", which makes the momentum graviton shift-symmetric (#11 §7.1; [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)). With η also rigid, det H = 1 follows (#5 §A; [corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries)).
- **A second symplectic space.** #11 §11.3, on the Dirac–Schwinger–Zwanziger pairing of electric and magnetic charges: "the charge lattice is a symplectic space" [D — structural; math T] — see [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice).

## Used by

- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — ω is the program's one rigid structure.
- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — Sp(2, ℝ) is the toy's symmetry group.
- [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) and [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) — boosts and squeezes as the test directions.
- [Shift symmetry: X is never auxiliary](/wiki/gravity/momentum-graviton/shift-symmetry) — the rigid group contains Z → Z + B.
- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — ω-rigidity fixes the comoving phase-space cell.
- [The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice) — the same structure on electric and magnetic charges.

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — P2′: symplectic rigidity ≡ constancy of ℏ.
- `papers/broken-born-checkpoint-v2.md` §5 — ω in standard form; the compatibility theorem it enters.
- `papers/broken-born-checkpoint-v2.md` §11 — the charge lattice as a symplectic space.
- `papers/reciprocity-toy-models.md` §1, §2, §4 — ρ symplectic; the Sp(2, ℝ) action of model I; boosts, squeezes and the compact SO(2).
- `notes/broken-born-theory.md` §2 — the standard block form of ω.
- `notes/debt1a-geometric-core.md` §A–§C — det H = 1; "Freeze ω only"; the Siegel domain of ω-compatible metrics.
- `notes/debt1a-ii-X-classification.md` §1 — the Möbius subgroup Z → Z + B of the rigid group.
- `verify/toy_coset.py` — invariance of model I under a generic symplectic S and under ρ.
