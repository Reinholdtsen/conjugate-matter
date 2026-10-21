---
title: "The symplectic form and Sp(2d, ℝ)"
weight: 20
status: established
description: "The antisymmetric pairing ω of position and momentum, the group Sp(2d, ℝ) that preserves it with its rotations, boosts and squeezes, and ω's rigidity read as the constancy of ℏ."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-ii-X-classification.md §1"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "review/round4-adjudication.md F1–F2"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "verify/toy_coset.py"
  - "verify/battery.py T2"
---

*The symplectic form ω is the antisymmetric pairing of positions with momenta that underlies Hamiltonian mechanics and the quantum commutator; in the plane of one position and one momentum it measures signed area. The symplectic group Sp(2d, ℝ) is the set of linear maps of phase space (d positions, d momenta) that preserve it. The group contains rotations of phase space — the quarter-turn [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) is one — together with stretches that lengthen one direction and shorten another, called boosts and squeezes. In the program ω is the one structure held fixed: its corrected postulate reads the rigidity of ω as the constancy of Planck's constant, and every other piece of phase-space geometry is allowed to vary.*

**Status:** Established — standard mathematics [T]; its rigidity in the program is a postulate [P] ([P2′](/wiki/program/postulates/p2-prime), [#11](/wiki/history/documents/checkpoint) §4) — the toy model's invariance under a generic symplectic matrix is machine-checked [V] in `verify/toy_coset.py` (see [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Definition

A symplectic form on phase space ℝ^{2d} is an antisymmetric, non-degenerate pairing ω(u, v) = uᵀωv of two phase-space vectors [T]. In the (x, p) block basis it takes the standard form

```text
ω = [[0, 1], [−1, 0]]          (d × d blocks)
ω(u, v) = u_x · v_p − u_p · v_x
```

where u = (u_x, u_p) splits a vector into its position and momentum parts. The [lab notebook](/wiki/history/documents/lab-notebook) writes this form with d = 4 (#1 §2); the [toy-model note](/wiki/symmetry-breaking/toy-models) uses d = 1, where the blocks are single numbers (§1).

Three properties make ω the structure of mechanics [T]:

- **Antisymmetry.** ω(u, u) = 0, so ω measures oriented area rather than length. For d = 1, ω(u, v) is the signed area of the parallelogram spanned by u and v.
- **Non-degeneracy.** Only the zero vector pairs to zero with every vector. Each position direction is paired with its own momentum direction and with nothing else.
- **Dynamics.** Hamilton's equations use ω to turn the gradient of the energy into a velocity in phase space, and the Poisson bracket {x, p} = 1 is the same pairing written for functions.

Quantization turns the Poisson bracket into the commutator, so [x, p] = iℏ is the quantum form of ω ([the canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator)).

## The symplectic group

A linear map S of phase space is symplectic when it preserves the pairing, ω(Su, Sv) = ω(u, v) for all u and v. In matrices:

```text
Sᵀ ω S = ω
```

These matrices form the group Sp(2d, ℝ) [T]. Three facts about it matter here [T]:

- **Volume.** Every symplectic matrix has det S = 1, so symplectic maps preserve phase-space volume. Hamiltonian time evolution is symplectic, so it preserves phase-space volume too: Liouville's theorem.
- **One degree of freedom.** For d = 1 the condition reduces to det S = 1, so Sp(2, ℝ) = SL(2, ℝ), the real 2 × 2 matrices of unit determinant. `verify/toy_coset.py` uses the generic element S = [[s₁, s₂], [s₃, (1 + s₂s₃)/s₁]], whose determinant is 1 by construction, and checks "generic S is symplectic".
- **Quantum implementation.** In quantum mechanics each symplectic map is carried out by a unitary operator, unique up to a phase (the metaplectic representation). For ρ that operator is the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform). Linear symplectic maps leave the commutator unchanged because they preserve ω, and the unitary operator that carries out each one is why they count, ordinarily, as changes of description; see [unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence).

## Rotations, boosts and squeezes

For d = 1 every element of Sp(2, ℝ) combines a rotation with a stretch [T]. Three one-parameter families appear in the toy-model note and its review:

```text
rotation   R(θ) = [[cos θ, sin θ], [−sin θ, cos θ]]     compact: the circle SO(2)
squeeze    diag(a, 1/a)                                  stretches x by a, compresses p by 1/a
boost      S(t) = [[cosh t, sinh t], [sinh t, cosh t]]   the same stretch along the diagonals x ± p
```

The boost matrix is the one the referee of [review round 4](/wiki/method/review/round-4) used ("S(t)=[[cosh t, sinh t],[sinh t, cosh t]] (symplectic: True)", audit notes Step 2(a)). It stretches the direction (1, 1) by eᵗ and compresses (1, −1) by e⁻ᵗ [T], so a boost is a squeeze along the diagonals. The referee's notes call diag(a, 1/a) a boost as well; this page follows the toy note, which calls it a squeeze.

The quarter-turn ρ = [[0, 1], [−1, 0]] is the rotation R(π/2). It "is symplectic and squares to −1" (toy-model note §1), and ρ² = −1 is the half-turn, the parity (x, p) → (−x, −p) (#1 §2). The rotations form the compact subgroup SO(2), a circle. Squeezes and boosts are non-compact: their parameter runs to infinity [T].

### Why compactness matters

By the [Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman), a continuous compact symmetry cannot break spontaneously in a two-dimensional system [T]. The toy-model note applies it to the rotations only: "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ. The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur [15]. Whether ρ's SO(2) stays unbroken in the full coupled model is open." (§4). See [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)

The boosts are where the [first ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) of [model I](/wiki/symmetry-breaking/toy-models/coset-model), the toy note's coset sigma model, failed. "Along H = SᵀS, K = S⁻¹K_ref S with S a boost, the compatibility term stays zero while the potential reaches −8.9 × 10⁶ μ at boost parameter 4" (toy-model note §4). That naive potential is dead as a stabilizing potential ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). Its replacement, [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential), penalizes boosts: "the boost family rises from −1 to −0.5" (round-4 adjudication, F2). Along the squeezes it keeps a flat direction: "The zero mode is the classical flat line H = diag(y, 1/y), K = K_ref. It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref. Boosts are penalized." (toy-model note §4). The round-4 adjudication had called this zero mode an exact symmetry; the toy note's v2, which ranks above the adjudication, says it is not symmetry-protected.

The referee also worked out, with sympy, which maps of Sp(2, ℝ) the naive potential leaves unbroken. A conjugation S⁻¹K_ref S that returns +K_ref forces S = diag(a, 1/a); one that returns −K_ref forces S = [[0, −1/c], [c, 0]]. So the potential "leaves a non-compact boost subgroup unbroken plus {+-1, +-rho} (Z4) in SO(2)" (audit notes Step 2(c), capitals lowered here): among the rotations only ±1 and ±ρ survive.

## How the toy models use the group

Model I, the coset sigma model of a phase-space metric H and a real structure K ([the order parameter](/wiki/symmetry-breaking/order-parameter)), takes Sp(2, ℝ) as its symmetry group. Its metric field is itself a symplectic matrix: H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]] for Z = X + iY in the upper half-plane (toy-model note §2; gate: "H(Z) is symplectic and I = w^-1 H squares to -1"). The group acts on both fields:

```text
H → Sᵀ H S        K → S⁻¹ K S
```

"Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS, and the action is invariant (checked for generic symplectic S, so for ρ)" (§2) [V]. The gate checks each of the three terms of the Lagrangian separately ("H kinetic term invariant under generic symplectic S", and likewise the K kinetic and potential terms), then ρ itself ("all three terms invariant under rho"). The vacua break the group: "the stabilizer of the vacuum (1, K0) in Sp(2,R) is {+1, -1} (so the orbit is 3-dimensional)". See [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) and [the toy-model scripts](/wiki/method/verification/toy-model-scripts).

## Rigidity: the one fixed structure

In the program's postulates ω is the only structure that does not vary. "**P2′** Only ω is rigid (symplectic rigidity ≡ constancy of ℏ). The neutral metric η is emergent — the order parameter" [P] (#11 §4; [P2′](/wiki/program/postulates/p2-prime); for η and the generalized metric H, see [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). [The calc note](/wiki/history/documents/debt-1-notes) that forced the change put it as "Freeze ω only — that is genuinely ℏ" (#5 §B). The lab notebook's gloss on the original postulate was "the symplectic structure *is* the constancy of ℏ — phase-space cells do not stretch" (#1 §1). The [original P2](/wiki/program/postulates/original-p2) froze the neutral metric η as well; the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) then left the program no content of its own ([the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)).

What a rigid ω leaves free:

- **The Siegel domain.** The positive generalized metrics H compatible with ω alone form the Siegel domain Sp(2d, ℝ)/U(d), coordinatized by a complex symmetric matrix Z = X + iY with Y > 0 (#5 §C; [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain)). For d = 1 it is the upper half-plane of model I.
- **Möbius maps.** Sp(2d, ℝ) acts on Z by fractional linear (Möbius) maps, and ρ acts as Z → −Z⁻¹ with fixed point Z = i [D] (#11 §6; [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)).
- **Shifts.** "The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric)" (#11 §7.1, tagged [D + T]), the Möbius action of the block matrix [[1, B], [0, 1]] (#6 §1). It shifts [the momentum graviton](/wiki/gravity/momentum-graviton) X = Re Z, so X "is shift-symmetric — axion-like, never auxiliary" ([shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)).
- **Unimodularity.** With η also rigid, det H = 1 follows (#5 §A; [the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries)). #11 §5 adds, calling it machine-verified, that it "persists across the whole modular family". Battery test T2 checks "det H_Z = 1" at one randomly sampled member of the family (d = 4), so the statement for the whole family is derived [D], not machine-verified ([the verification battery](/wiki/method/verification/battery)).

## A second symplectic space: charges

#11 §11.3 finds the same structure on electric and magnetic charges. The [Dirac–Schwinger–Zwanziger pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) ⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ "is an antisymmetric integer form: **the charge lattice is a symplectic space** [17†]" [D — structural; math T]. Duality frames are then [Lagrangian polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations) of charge space, and [S-duality](/wiki/electric-magnetic-duality/s-duality) is "generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹: the third appearance of one matrix in this program". See [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice).

## Standard references

Added by the wiki from model memory (†); the program's documents do not cite them.

- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (1978)†: symplectic forms, Hamiltonian flows, Liouville's theorem.
- G. B. Folland, *Harmonic Analysis in Phase Space* (1989)†: the symplectic group and the metaplectic representation.

The toy note's own references for the two-dimensional theorems are Mermin–Wagner [13] and Coleman [14], and for the hyperbolic exception Niedermaier–Seiler and Duncan–Niedermaier–Seiler [15]; the round-4 referee found all of them on INSPIRE and supporting the statements they are cited for (audit notes, Step 1, under the note's earlier numbering).

## Used by

- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — ω is the program's one rigid structure.
- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — Sp(2, ℝ) is the toy's symmetry group.
- [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) and [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) — boosts and squeezes as the test directions.
- [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question) — the compact rotations and the non-compact rest.
- [The Siegel domain Sp(2d, ℝ)/U(d)](/wiki/phase-space/modular-field/siegel-domain) — the metrics a rigid ω leaves free.
- [Shift symmetry: X is never auxiliary](/wiki/gravity/momentum-graviton/shift-symmetry) — the rigid group contains Z → Z + B.
- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — ω-rigidity fixes the comoving phase-space cell.
- [The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice) — the same structure on electric and magnetic charges.

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — P2′: symplectic rigidity ≡ constancy of ℏ.
- `papers/broken-born-checkpoint-v2.md` §5 — the compatibility theorem, with ω and η standard; unimodularity across the modular family.
- `papers/broken-born-checkpoint-v2.md` §6, §7.1 — ρ as Z → −Z⁻¹; the rigid group contains Z → Z + B.
- `papers/broken-born-checkpoint-v2.md` §11 — the charge lattice as a symplectic space.
- `papers/reciprocity-toy-models.md` §1, §2, §4 — ρ symplectic; the Sp(2, ℝ) action of model I; boosts, squeezes and the compact SO(2).
- `review/round4-adjudication.md` F1–F2 — the boost family and the bounded repair.
- `review/round4/referee/audit-notes.md` Step 1, Step 2(a), Step 2(c) — the two-dimensional references checked; the boost matrix; the residual symmetry of the naive potential.
- `notes/debt1a-geometric-core.md` §A–§C — det H = 1; "Freeze ω only"; the Siegel domain of ω-compatible metrics.
- `notes/debt1a-ii-X-classification.md` §1 — the Möbius subgroup Z → Z + B of the rigid group.
- `notes/broken-born-theory.md` §1, §2 — the original P2's gloss; the standard block form of ω; ρ² as parity.
- `verify/toy_coset.py` — invariance of model I under a generic symplectic S and under ρ; the vacuum's stabilizer.
- `verify/battery.py` T2 — det H_Z = 1 at one sampled member of the modular family.
