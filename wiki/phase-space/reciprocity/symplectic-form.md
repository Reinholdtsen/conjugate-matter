---
title: "The symplectic form and Sp(2d, ℝ)"
weight: 20
status: established
description: "The antisymmetric pairing ω of position and momentum, the group Sp(2d, ℝ) that preserves it with its rotations, boosts and squeezes, and ω's rigidity read as the constancy of ℏ."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §11"
  - "notes/geometric-core.md §A"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §C"
  - "notes/x-classification.md §1"
  - "wiki/papers/reciprocity-toy-models.md §1"
  - "wiki/papers/reciprocity-toy-models.md §2"
  - "wiki/papers/reciprocity-toy-models.md §4"
  - "review/round4-adjudication.md F1–F2"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "verify/toy_coset.py"
  - "verify/battery.py T2"
---

*The symplectic form ω is the antisymmetric pairing of positions with momenta that underlies Hamiltonian mechanics and the quantum commutator; in the plane of one position and one momentum it measures signed area. The symplectic group Sp(2d, ℝ) is the set of linear maps of phase space (d positions, d momenta) that preserve it. The group contains rotations of phase space — the quarter-turn [Born reciprocity](born-reciprocity.md) is one — together with stretches that lengthen one direction and shorten another, called boosts and squeezes. In the program ω is the one structure held fixed: its corrected postulate reads the rigidity of ω as the constancy of Planck's constant, and every other piece of phase-space geometry is allowed to vary.*

**Status:** Established — standard mathematics [T]; its rigidity in the program is a postulate [P] ([P2′](../../program/postulates/p2-prime.md), [#11](../../history/documents/checkpoint.md) [§4](../../papers/broken-born-checkpoint-v2.md#4-postulates)) — the toy model's invariance under a generic symplectic matrix is machine-checked [V] in [`verify/toy_coset.py`](../../../verify/toy_coset.py) (see [the toy-model scripts](../../method/verification/toy-model-scripts.md)).

## Definition

A symplectic form on phase space ℝ^{2d} is an antisymmetric, non-degenerate pairing ω(u, v) = uᵀωv of two phase-space vectors [T]. In the (x, p) block basis it takes the standard form

```text
ω = [[0, 1], [−1, 0]]          (d × d blocks)
ω(u, v) = u_x · v_p − u_p · v_x
```

where u = (u_x, u_p) splits a vector into its position and momentum parts. The [lab notebook](../../history/documents/lab-notebook.md) writes this form with d = 4 ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)); the [toy-model note](../../symmetry-breaking/toy-models/_index.md) uses d = 1, where the blocks are single numbers ([§1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)).

Three properties make ω the structure of mechanics [T]:

- **Antisymmetry.** ω(u, u) = 0, so ω measures oriented area rather than length. For d = 1, ω(u, v) is the signed area of the parallelogram spanned by u and v.
- **Non-degeneracy.** Only the zero vector pairs to zero with every vector. Each position direction is paired with its own momentum direction and with nothing else.
- **Dynamics.** Hamilton's equations use ω to turn the gradient of the energy into a velocity in phase space, and the Poisson bracket {x, p} = 1 is the same pairing written for functions.

Quantization turns the Poisson bracket into the commutator, so [x, p] = iℏ is the quantum form of ω ([the canonical commutator](canonical-commutator.md)).

## The symplectic group

A linear map S of phase space is symplectic when it preserves the pairing, ω(Su, Sv) = ω(u, v) for all u and v. In matrices:

```text
Sᵀ ω S = ω
```

These matrices form the group Sp(2d, ℝ) [T]. Three facts about it matter here [T]:

- **Volume.** Every symplectic matrix has det S = 1, so symplectic maps preserve phase-space volume. Hamiltonian time evolution is symplectic, so it preserves phase-space volume too: Liouville's theorem.
- **One degree of freedom.** For d = 1 the condition reduces to det S = 1, so Sp(2, ℝ) = SL(2, ℝ), the real 2 × 2 matrices of unit determinant. [`verify/toy_coset.py`](../../../verify/toy_coset.py) uses the generic element S = [[s₁, s₂], [s₃, (1 + s₂s₃)/s₁]], whose determinant is 1 by construction, and checks "generic S is symplectic".
- **Quantum implementation.** In quantum mechanics each symplectic map is carried out by a unitary operator, unique up to a phase (the metaplectic representation). For ρ that operator is the [Fourier transform](fourier-transform.md). Linear symplectic maps leave the commutator unchanged because they preserve ω, and the unitary operator that carries out each one is why they count, ordinarily, as changes of description; see [unitary equivalence versus Noether symmetry](unitary-equivalence.md).

## Rotations, boosts and squeezes

For d = 1 every element of Sp(2, ℝ) combines a rotation with a stretch [T]. Three one-parameter families appear in the toy-model note and its review:

```text
rotation   R(θ) = [[cos θ, sin θ], [−sin θ, cos θ]]     compact: the circle SO(2)
squeeze    diag(a, 1/a)                                  stretches x by a, compresses p by 1/a
boost      S(t) = [[cosh t, sinh t], [sinh t, cosh t]]   the same stretch along the diagonals x ± p
```

The boost matrix is the one the referee of [review round 4](../../method/review/round-4.md) used ("S(t)=[[cosh t, sinh t],[sinh t, cosh t]] (symplectic: True)", audit notes Step 2(a)). It stretches the direction (1, 1) by eᵗ and compresses (1, −1) by e⁻ᵗ [T], so a boost is a squeeze along the diagonals. The referee's notes call diag(a, 1/a) a boost as well (see flag 10 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)); this page follows the toy note, which calls it a squeeze.

The quarter-turn ρ = [[0, 1], [−1, 0]] is the rotation R(π/2). It "is symplectic and squares to −1" ([toy-model note §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)), and ρ² = −1 is the half-turn, the parity (x, p) → (−x, −p) ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)). The rotations form the compact subgroup SO(2), a circle. Squeezes and boosts are non-compact: their parameter runs to infinity [T].

### Why compactness matters

By the [Mermin–Wagner–Coleman theorem](../../symmetry-breaking/mermin-wagner-coleman.md), a continuous compact symmetry cannot break spontaneously in a two-dimensional system [T]. The toy-model note applies it to the rotations only: "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ. The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur [15]. Whether ρ's SO(2) stays unbroken in the full coupled model is open." ([§4](../../papers/reciprocity-toy-models.md#4-quantum-stability)). See [Open: does ρ's SO(2) break in the coupled model?](../../symmetry-breaking/toy-models/coset-model/so2-question.md)

The boosts are where the [first ρ-preserving potential](../../symmetry-breaking/toy-models/coset-model/naive-potential.md) of [model I](../../symmetry-breaking/toy-models/coset-model/_index.md), the toy note's [coset sigma model](../../symmetry-breaking/toy-models/coset-model/sigma-models.md), failed. "Along H = SᵀS, K = S⁻¹K_ref S with S a boost, the compatibility term stays zero while the potential reaches −8.9 × 10⁶ μ at boost parameter 4" ([toy-model note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability)). That naive potential is under review as a stabilizing potential ([Under review: the naive ρ-preserving potential](../../symmetry-breaking/toy-models/coset-model/naive-potential.md)). Its replacement, [the bounded potential V_b](../../symmetry-breaking/toy-models/coset-model/bounded-potential.md), penalizes boosts: "the boost family rises from −1 to −0.5" (round-4 adjudication, F2). Along the squeezes it keeps a flat direction: "The zero mode is the classical flat line H = diag(y, 1/y), K = K_ref. It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref. Boosts are penalized." ([toy-model note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability)). The round-4 adjudication had called this zero mode an exact symmetry; the toy note, which ranks above the adjudication, says it is not symmetry-protected (see flag 12 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [conflicts between sources](../../history/documents/source-conflicts.md#postulates-and-the-toy-models), entry C28).

The referee also worked out, with sympy, which maps of Sp(2, ℝ) the naive potential leaves unbroken. A conjugation S⁻¹K_ref S that returns +K_ref forces S = diag(a, 1/a); one that returns −K_ref forces S = [[0, −1/c], [c, 0]]. So the potential "leaves a non-compact boost subgroup unbroken plus {+-1, +-rho} (Z4) in SO(2)" (audit notes Step 2(c), capitals lowered here; its "boost subgroup" is the squeeze family diag(a, 1/a), see flag 10 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)): among the rotations only ±1 and ±ρ survive.

## How the toy models use the group

Model I, the coset sigma model of a phase-space metric H and a real structure K ([the order parameter](../../symmetry-breaking/order-parameter.md)), takes Sp(2, ℝ) as its symmetry group. Its metric field is itself a symplectic matrix: H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]] for Z = X + iY in the upper half-plane ([toy-model note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k); gate: "H(Z) is symplectic and I = w^-1 H squares to -1"). The group acts on both fields:

```text
H → Sᵀ H S        K → S⁻¹ K S
```

"Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS, and the action is invariant (checked for generic symplectic S, so for ρ)" (§2) [V]. The gate checks each of the three terms of the Lagrangian separately ("H kinetic term invariant under generic symplectic S", and likewise the K kinetic and potential terms), then ρ itself ("all three terms invariant under rho"). The vacua break the group: "the stabilizer of the vacuum (1, K0) in Sp(2,R) is {+1, -1} (so the orbit is 3-dimensional)". See [Model I: action and symmetries](../../symmetry-breaking/toy-models/coset-model/action-and-symmetries.md) and [the toy-model scripts](../../method/verification/toy-model-scripts.md).

## Rigidity: the one fixed structure

In the program's postulates ω is the only structure that does not vary. "**P2′** Only ω is rigid (symplectic rigidity ≡ constancy of ℏ). The neutral metric η is emergent — the order parameter" [P] ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates); [P2′](../../program/postulates/p2-prime.md); for η and the generalized metric H, see [the structures ω, η, H](../born-geometry/born-structures.md)). [The calc note](../../history/documents/field-equation-notes.md) that forced the change put it as "Freeze ω only — that is genuinely ℏ" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). The lab notebook's gloss on the original postulate was "the symplectic structure *is* the constancy of ℏ — phase-space cells do not stretch" ([#1 §1](../../../notes/broken-born-theory.md#1-postulates)). The [original P2](../../program/postulates/original-p2.md) froze the neutral metric η as well; the [compatibility theorem](../born-geometry/compatibility-theorem.md) then left the program no content of its own ([the nontriviality theorem](../../program/postulates/nontriviality-theorem.md)).

What a rigid ω leaves free:

- **The Siegel domain.** The positive generalized metrics H compatible with ω alone form the Siegel domain Sp(2d, ℝ)/U(d), coordinatized by a complex symmetric matrix Z = X + iY with Y > 0 ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard); [the Siegel domain](../modular-field/siegel-domain.md)). For d = 1 it is the upper half-plane of model I.
- **Möbius maps.** Sp(2d, ℝ) acts on Z by fractional linear (Möbius) maps, and ρ acts as Z → −Z⁻¹ with fixed point Z = i [D] ([#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field); [reciprocity as modular inversion](../modular-field/modular-inversion.md)).
- **Shifts.** "The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric)" ([#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t), tagged [D + T]), the Möbius action of the block matrix [[1, B], [0, 1]] ([#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous)). It shifts [the momentum graviton](../../gravity/momentum-graviton/_index.md) X = Re Z, so X "is shift-symmetric — axion-like, never auxiliary" ([shift symmetry](../../gravity/momentum-graviton/shift-symmetry.md)).
- **Unimodularity.** With η also rigid, det H = 1 follows ([#5 §A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous); [the corollaries](../born-geometry/compatibility-corollaries.md)). [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) adds, calling it machine-verified, that it "persists across the whole modular family". Battery test T2 checks "det H_Z = 1" at one randomly sampled member of the family (d = 4), so the statement for the whole family is derived [D], not machine-verified ([the verification battery](../../method/verification/battery.md)).

## A second symplectic space: charges

[#11 §11.3](../../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) finds the same structure on electric and magnetic charges. The [Dirac–Schwinger–Zwanziger pairing](../../electric-magnetic-duality/monopoles/dirac-quantization.md) ⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ "is an antisymmetric integer form: **the charge lattice is a symplectic space** [17†]" [D — structural; math T]. Duality frames are then [Lagrangian polarizations](lagrangian-polarizations.md) of charge space, and [S-duality](../../electric-magnetic-duality/s-duality.md) is "generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹: the third appearance of one matrix in this program". See [the symplectic charge lattice](../../electric-magnetic-duality/symplectic-charge-lattice.md). That electric–magnetic duality is a case of Born reciprocity, in the phase space of the electromagnetic field, is a published remark (flag 67 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending).

## Standard references

Added by the wiki from model memory (†); the program's documents do not cite them.

- V. I. Arnold, *Mathematical Methods of Classical Mechanics* (1978)†: symplectic forms, Hamiltonian flows, Liouville's theorem.
- G. B. Folland, *Harmonic Analysis in Phase Space* (1989)†: the symplectic group and the metaplectic representation.

The toy note's own references for the two-dimensional theorems are Mermin–Wagner [13] and Coleman [14], and for the hyperbolic exception Niedermaier–Seiler and Duncan–Niedermaier–Seiler [15]; the round-4 referee found all of them on INSPIRE and supporting the statements they are cited for (audit notes, Step 1, under the note's earlier numbering).

## Used by

- [The hard core: spontaneously broken Born reciprocity](../../program/hard-core.md) — ω is the one structure the laws fix.
- [P1: the phase-space arena](../../program/postulates/p1-arena.md) — physics on phase space with a symplectic form ω.
- [P2′: only the symplectic form is rigid](../../program/postulates/p2-prime.md) — ω is the program's one rigid structure.
- [P3: a reciprocity-invariant action](../../program/postulates/p3-reciprocity.md) — the Born rotation generated by I = ω⁻¹H.
- [P4: polarized matter and strict sector separation](../../program/postulates/p4-polarized-matter.md) and [P5: the vacuum selects a polarization](../../program/postulates/p5-spontaneous-selection.md) — a polarization is a Lagrangian subspace for ω.
- [The nontriviality theorem](../../program/postulates/nontriviality-theorem.md) — the program has content only with ω alone rigid.
- [The conjugate universe: one state, two descriptions](../../program/conjugate-universe.md) and [the cosmological constraint a·ã = 1](../../cosmology/scale-factor-duality/cosmological-constraint.md) — ω-rigidity fixes the comoving phase-space cell.
- [The Siegel domain Sp(2d, ℝ)/U(d)](../modular-field/siegel-domain.md) and [the modular field Z = X + iY](../modular-field/modular-field-z.md) — the metrics a rigid ω leaves free.
- [Shift symmetry: X is never auxiliary](../../gravity/momentum-graviton/shift-symmetry.md) — the rigid group contains Z → Z + B.
- [The symplectic partner of the graviton is another graviton](../../gravity/momentum-graviton/symplectic-partner.md) — the antisymmetric pairing ω gives the metric a symmetric partner.
- [The geometric action S_H and the v0.1 action (superseded)](../../gravity/tuning-test/geometric-action.md) — written with ω and η frozen.
- [τ: hilltop quintessence on the Maslov circle](../../cosmology/dark-energy/tau-quintessence.md) — τ exists only once ω alone is rigid.
- [Acceptance criterion 1](../../symmetry-breaking/toy-models/acceptance-criterion.md) and [model I: action and symmetries](../../symmetry-breaking/toy-models/coset-model/action-and-symmetries.md) — Sp(2, ℝ) is the toy's symmetry group.
- [Model I vacua](../../symmetry-breaking/toy-models/coset-model/vacua.md) — a symplectic map carries the circle of vacua at H = 1 onto the circle at any H.
- [Under review: the naive ρ-preserving potential](../../symmetry-breaking/toy-models/coset-model/naive-potential.md) and [the bounded potential V_b](../../symmetry-breaking/toy-models/coset-model/bounded-potential.md) — boosts and squeezes as the test directions.
- [Open: does ρ's SO(2) break in the coupled model?](../../symmetry-breaking/toy-models/coset-model/so2-question.md) — the compact rotations and the non-compact rest.
- [The twisted element ρ∘(K → −K)](../../symmetry-breaking/twisted-element.md) — model I on the phase plane with the standard ω.
- [The duality on the matrix base](../../symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma.md) — the Langmann–Szabo kernel is built from the symplectic product.
- [The symplectic charge lattice](../../electric-magnetic-duality/symplectic-charge-lattice.md) and [Open: one modular structure for both polarizations (OP8)](../../electric-magnetic-duality/unified-modular-structure.md) — the same structure on electric and magnetic charges.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — P2′: symplectic rigidity ≡ constancy of ℏ.
- [`wiki/papers/broken-born-checkpoint-v2.md` §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) — the compatibility theorem, with ω and η standard; unimodularity across the modular family.
- [`wiki/papers/broken-born-checkpoint-v2.md` §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field), [§7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — ρ as Z → −Z⁻¹; the rigid group contains Z → Z + B.
- [`wiki/papers/broken-born-checkpoint-v2.md` §11](../../papers/broken-born-checkpoint-v2.md#11-polarized-charge-lattices-monopoles-duality-frames-and-the-recurring-matrix) — the charge lattice as a symplectic space.
- [`wiki/papers/reciprocity-toy-models.md` §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work), [§2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k), [§4](../../papers/reciprocity-toy-models.md#4-quantum-stability) — ρ symplectic; the Sp(2, ℝ) action of model I; boosts, squeezes and the compact SO(2).
- [`review/round4-adjudication.md`](../../../review/round4-adjudication.md) F1–F2 — the boost family and the bounded repair.
- [`review/round4/referee/audit-notes.md`](../../../review/round4/referee/audit-notes.md) Step 1, Step 2(a), Step 2(c) — the two-dimensional references checked; the boost matrix; the residual symmetry of the naive potential.
- [`notes/geometric-core.md` §A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous)–[§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — det H = 1; "Freeze ω only"; the Siegel domain of ω-compatible metrics.
- [`notes/x-classification.md` §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous) — the Möbius subgroup Z → Z + B of the rigid group.
- [`notes/broken-born-theory.md` §1](../../../notes/broken-born-theory.md#1-postulates), [§2](../../../notes/broken-born-theory.md#2-kinematic-core) — the original P2's gloss; the standard block form of ω; ρ² as parity.
- [`verify/toy_coset.py`](../../../verify/toy_coset.py) — invariance of model I under a generic symplectic S and under ρ; the vacuum's stabilizer.
- [`verify/battery.py`](../../../verify/battery.py) T2 — det H_Z = 1 at one sampled member of the modular family.
