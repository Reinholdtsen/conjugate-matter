---
title: "P2′: only the symplectic form is rigid"
weight: 40
status: alive
description: "The corrected postulate: only ω (the constancy of ℏ) is fixed and η = HJ is chosen by the vacuum; v2.2 adds that the polarization is a Goldstone angle needing a ρ-preserving potential and made physical only by a K-odd coupling."
provenance: [P]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §10"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 11"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §F"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.3)'"
  - "notes/broken-born-program-v1.md §2"
  - "wiki/papers/reciprocity-toy-models.md Abstract"
  - "wiki/papers/reciprocity-toy-models.md §1"
  - "wiki/papers/reciprocity-toy-models.md §2"
  - "wiki/papers/reciprocity-toy-models.md §4"
  - "wiki/papers/reciprocity-toy-models.md §6"
  - "notes/toy-lagrangian.md 'Chunk 2 results (2026-10-19): the Grosse–Wulkenhaar route'"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "review/round4-adjudication.md 'Rulings' F3"
  - "verify/toy_coset.py"
  - "verify/battery.py T2"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/dual-sector.md §8"
  - "review/wiki-build-flags.md item 70"
---

*P2′ is the program's corrected second axiom: of the structures on phase space, only the symplectic form ω is fixed in advance, and holding it fixed is the program's way of saying that Planck's constant does not change. The [neutral metric](../../phase-space/born-geometry/born-structures.md) η, which marks which directions count as position, is not part of the background. It is a property of the vacuum: the order parameter of the broken symmetry, the quantity whose value tells a vacuum from its mirror image, as the direction of magnetization tells a magnet pointing one way from one pointing the other. The original P2 had fixed η as well, and the nontriviality theorem showed that this left the program with no content of its own. [Checkpoint](../../history/documents/checkpoint.md) v2.2 added a refinement from the toy models: with only ω fixed, the polarization is a continuous angle. Two consequences follow. Pinning the angle to a definite value needs an additional potential, which brings back a little fixed structure, and the choice has physical consequences only once matter couples to it.*

**Status:** Alive — [P]; the correction from the original P2 is forced [D] by [the nontriviality theorem](nontriviality-theorem.md); the v2.2 Goldstone-angle sentence is [D][V], checked by the [toy-model scripts](../../method/verification/toy-model-scripts.md). The toy models show that the structure is consistent; they do not test the postulate.

## Statement

```text
P2′  Only ω is rigid (symplectic rigidity ≡ constancy of ℏ). The neutral
     metric η is emergent — the order parameter, η = HJ, with the real
     structure J chosen spontaneously.                                 [P]
```

This is [#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)'s text. Its bracket adds two things: "the correction from the original P2 is *forced*: a nontriviality theorem (§5) shows the theory has content beyond GR + SIDM iff η is emergent. [D]" (GR: [general relativity](../../gravity/spin-2-fields/general-relativity.md); SIDM: [self-interacting dark matter](../../dark-matter/halo-astrophysics/self-interacting-dark-matter.md)), and a note on credit, below. A refinement follows the statement, also below. The program paper v1 states the same axiom as "P2′ (Rigidity — corrected). Only ω is non-dynamical: symplectic rigidity is the constancy of ℏ. The neutral metric η is *not* fundamental; it is the order parameter, η = HJ, with the real structure J chosen spontaneously." ([#9 §2](../../../notes/broken-born-program-v1.md#2-postulates--including-the-one-the-mathematics-rejected)).

The axiom has two halves: what is fixed (ω) and what is left to the vacuum (η). Both refer to the structures of [P1](p1-arena.md).

## What is rigid: ω and the constancy of ℏ

A rigid, or non-dynamical, structure is fixed background: it has no equation of motion and takes the same value in every state of the theory [T]. P2′ as stated allows exactly one such structure, the [symplectic form](../../phase-space/reciprocity/symplectic-form.md) ω, the antisymmetric pairing of position with momentum behind the commutator [x, p] = iℏ ([the canonical commutator](../../phase-space/reciprocity/canonical-commutator.md)).

The physical reading is the one the original P2 already gave ω: "the symplectic structure *is* the constancy of ℏ — phase-space cells do not stretch" ([#1 §1](../../../notes/broken-born-theory.md#1-postulates)). Holding ω fixed holds the size of a phase-space cell fixed, which is the statement that ℏ does not change ([#1 §6](../../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary)). The repair keeps exactly this part of the old axiom: "Freeze ω only — that is genuinely ℏ" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). Two consequences in the record follow from ω alone:

- **Unimodularity.** The compatibility theorem's [corollary det H = 1](../../phase-space/born-geometry/compatibility-corollaries.md) is, in the [field-equation note](../../history/documents/field-equation-notes.md)'s words, "the geometric face of ℏ-rigidity" ([#5 §F](../../../notes/geometric-core.md#f-status-after-tonight)). [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) adds that det H = 1 "persists across the whole modular family of §6" and marks this as machine-verified; the battery's test T2 checks det H_Z = 1 for one randomly sampled member of the family ([`verify/battery.py`](../../../verify/battery.py); [the verification battery](../../method/verification/battery.md)), so the statement for the whole family is [D], not [V].
- **The cosmological constraint.** "ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run)" [D] ([#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology)), where a and ã are the scale factors of position space and momentum space ([the cosmological constraint a·ã = 1](../../cosmology/scale-factor-duality/cosmological-constraint.md)).

## What is emergent: η as the order parameter

### The construction

The field-equation note gives the repair in one sentence: "the fundamental pair is (ω, H); the derived complex structure is I = ω⁻¹H; the vacuum spontaneously selects a real structure J (an involution anticommuting with I), and η ≡ HJ" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). In order:

1. The fundamental structures are ω, which is rigid, and the generalized metric H, which is dynamical.
2. From them comes the complex structure I = ω⁻¹H, with I² = −1, a quarter-turn of phase space.
3. The vacuum selects a real structure J: a linear map with J² = 1 (an involution [T]) that anticommutes with I.
4. The neutral metric is then defined from the vacuum's choice, η ≡ HJ.

So η is no longer an input. It is built from the dynamical H and the vacuum's J, and it differs from one vacuum to another.

### Why η is an order parameter

In [spontaneous symmetry breaking](../../symmetry-breaking/spontaneous-symmetry-breaking.md) the laws are symmetric but the ground state is not, and an order parameter is a quantity that the symmetry would change and that takes a definite value in the ground state, as magnetization does in a magnet [T]. At the standard forms of the structures, the [Born rotation](../../phase-space/reciprocity/born-reciprocity.md) ρ: (x, p) → (p, −x) leaves ω and H alone but not η. The [lab notebook](../../history/documents/lab-notebook.md) found that it "preserves ω (it is symplectic), preserves H (it is orthogonal), and **flips the sign of η**, hence flips J and K while preserving I. **[D]**" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)). A vacuum with a definite η is therefore carried by ρ to a different vacuum, with −η. Under P2′ the field-equation note reads the sign flip this way: "the earlier observation that reciprocity flips η now reads correctly as *the broken symmetry moving the order parameter*" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). The note calls the assignment "philosophically right" as well, since η "is the structure that says which directions are position", and on this reading the vacuum state, not the background, fixes those directions ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). See [the order parameter](../../symmetry-breaking/order-parameter.md).

### The space of vacua

The choices of J form a familiar manifold:

```text
{J} ≅ U(d)/O(d) = Λ(d)                                              (#5 §B)
```

"the Lagrangian Grassmannian — π₁ = ℤ, Maslov circle intact, τ restored" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). [The Lagrangian Grassmannian](../../phase-space/modular-field/lagrangian-grassmannian.md) Λ(d) is the space of all [Lagrangian subspaces](../../phase-space/reciprocity/lagrangian-polarizations.md), all possible choices of "position" directions. It is compact, of dimension d(d+1)/2, which is 10 for d = 4 ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core) [T]). Its non-contractible loop, the Maslov circle, carries the program's dark-energy field τ ([τ as the Maslov phase](../../phase-space/modular-field/maslov-phase.md)). The metric opens up at the same time: with only ω rigid, "H ranges over Sp(2d,ℝ)/U(d): Z = X + iY" ([#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)), [the Siegel domain](../../phase-space/modular-field/siegel-domain.md), whose real part X is the [momentum graviton](../../gravity/momentum-graviton/_index.md) ([the modular field Z = X + iY](../../phase-space/modular-field/modular-field-z.md)).

## Why the correction was forced

[The original P2](original-p2.md) held η fixed as well. [The compatibility theorem](../../phase-space/born-geometry/compatibility-theorem.md) [T][V] then allows only H = diag(g, g⁻¹), and the theory reduces to "GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural), "Branch R"), where w is dark energy's [equation of state](../../cosmology/dark-energy/quintessence.md#dark-energy-and-the-equation-of-state), its pressure divided by its energy density, and −1 is the value for a [cosmological constant](../../cosmology/dark-energy/cosmological-constant.md). [The nontriviality theorem](nontriviality-theorem.md) states the general point: the program has content beyond that "iff η is emergent". The lab notebook's v0.3 addendum records the change: "P2 is therefore replaced by P2′".

## Precedent and credit

[#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates): "That η should be dynamical rather than fixed was argued independently in metastring theory [26S]; the reading of η as the order parameter of broken reciprocity is this program's." The toy-model note's survey of prior work says the same in more detail: "Freidel, Leigh and Minic make η dynamical and describe spacetime as a choice of Lagrangian [1]", and they describe a preferred polarization as breaking Born duality, "but give no potential for η and no symmetry-breaking analysis" ([toy note §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)). See [broken Born duality](../../phase-space/reciprocity/broken-born-duality.md).

More of P2′'s setting is in the same authors' papers [S], with no potential and no order parameter ([`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); flag 70, pending):

- **η = HJ.** The structure is theirs from 2013: both elements (η, J) "of the chiral structure are dynamical" ([Freidel, Leigh and Minic 2014, Phys. Lett. B](https://arxiv.org/abs/1307.7080), posted in 2013).
- **The space of choices.** [Freidel, Leigh and Minic 2016](https://arxiv.org/abs/1606.01829) (§2) name U(d)/O(d), the space of vacua above, as a space of choices of η: it "represents the choice of inequivalent lifts" η "that preserve the symplectic structure and the vacuum state".
- **A breaking in the vacuum.** A later paper of theirs, [Freidel, Kowalski-Glikman, Leigh and Minic 2021](https://arxiv.org/abs/2104.00802), places a symmetry breaking tied to the choice of polarization in the vacuum, for a dual Lorentz symmetry of their doubled phase space that is not ρ ([broken Born duality, its neighbours](../../phase-space/reciprocity/broken-born-duality.md#neighbours-in-the-literature)).

What was not found in their papers is P2′'s first half, the rigidity of ω alone. They put the rigidity of quantum theory in the flatness of η, "the rigidity of the quantum theory is encoded into the flatness of the polarization metric" η ([Freidel, Leigh and Minic 2015](https://arxiv.org/abs/1502.08005), §1), and [Minic 2020](https://arxiv.org/abs/2003.00318) (§2.2) makes all three structures dynamical.

## The v2.2 refinement

Checkpoint v2.2 (2026-10-20) appended to P2′ what the [toy models](../../symmetry-breaking/toy-models/_index.md) had found:

> *Refinement (v2.2, from the toy models):* with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]. Two things follow. A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η. And the breaking of ρ is physical only once matter couples to the sign of K (P4): without such a coupling, a twisted element ρ∘(K → −K) leaves the vacuum invariant. ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates))

The toy models work with phase space ℝ² (d = 1) and fields on a 1+1-dimensional base. In the toy-model note the order parameter is written with a real structure K, η = ωK, with K² = 1 and Kᵀ ω K = −ω ([toy note §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)); the naming question is below.

### The polarization is a Goldstone angle [D][V]

A Goldstone direction is a direction along the [vacuum manifold](../../symmetry-breaking/topological-defects.md#the-vacuum-manifold-t) of a broken continuous symmetry: moving along it costs no energy [T] ([Goldstone modes and the Higgs mechanism](../../symmetry-breaking/goldstone-and-higgs.md)). In the [coset toy model](../../symmetry-breaking/toy-models/coset-model/_index.md) (model I) the vacua at H = 1 are

```text
K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]                            (toy note §2)
```

a whole circle of them, and "ρ acts as Z → −1/Z and K(φ) → K(φ + π) = −K(φ)" ([toy note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)). So ρ moves each vacuum by π along a continuous circle of vacua. The worklog names the continuous group: "the U(1) stabilizer of H that rotates K", and in the complex [Grosse–Wulkenhaar model](../../symmetry-breaking/toy-models/grosse-wulkenhaar/_index.md), the other toy, "the left phase rotations e^{−iαN}, with the duality at α = π" (worklog, 'Chunk 2 results'). The potential's Hessian at the vacuum has rank 1, leaving three Goldstone directions: two non-compact directions of the upper half-plane and "the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)" ([toy note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k); checked in [`verify/toy_coset.py`](../../../verify/toy_coset.py)). [#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) draws the link to [dark energy](../../cosmology/dark-energy/tau-quintessence.md): "In the coset model that angle parametrizes Λ(1): it is τ's circle", and adds "None of this tests the cosmology; it only shows the structure is consistent." See [the polarization as a Goldstone angle](../../symmetry-breaking/goldstone-angle.md).

### A definite polarization needs a ρ-preserving potential

A Goldstone angle is not pinned to any value, and in 1+1 dimensions it cannot order at all: "Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability); [the Mermin–Wagner–Coleman theorem](../../symmetry-breaking/mermin-wagner-coleman.md)). To obtain a definite polarization the toy adds "a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability)).

- The first form tried, −μ[Tr(K K_ref)]², is "unbounded below once H is dynamical": along a family of boosts it reaches "−8.9 × 10⁶ μ at boost parameter 4", and the reference vacuum is a saddle ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability); [Under review: the naive ρ-preserving potential](../../symmetry-breaking/toy-models/coset-model/naive-potential.md)).
- The normalized form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) is bounded, "−μ ≤ V_b ≤ 0 by Cauchy–Schwarz", and with H dynamical the reference vacuum is "a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236". The zero mode is a flat line that "is not symmetry-protected" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability); [the bounded potential V_b](../../symmetry-breaking/toy-models/coset-model/bounded-potential.md)).
- At H = 1, V_b = −(μ/2)(1 + cos 2φ), and with H dynamical the vacuum manifold is "{diag(y, 1/y)} × {±K_ref}" ([toy note §4](../../papers/reciprocity-toy-models.md#4-quantum-stability)). The two signs ±K_ref are the vacua that ρ exchanges, since ρ sends K to −K at H = 1 ([toy note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)).

This is what #11 means by "a rigid, unordered pair of axes". V_b contains K_ref only inside the square [Tr(K K_ref)]², so K_ref and −K_ref define the same potential. The potential fixes the pair of axes along which K_ref points, but not which of the two is position; the worklog writes "a rigid, unordered pair of axes (K_ref up to sign)" ('Chunk 3 results'). That places the structure a definite polarization needs between two extremes: more than ω alone, which fixes no axes, and less than a rigid η, which would also fix which axis is position. The worklog draws the same conclusion: the toy supports "broken reciprocity" in the form "a pseudo-Goldstone polarization angle with a ρ-symmetric potential", not "only ω rigid, nothing else" ('Chunk 3 results').

### The breaking is physical only through the sign of K

Model I has a second symmetry besides Sp(2, ℝ): "There is a separate ℤ₂, K → −K" ([toy note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)). Combined with ρ it gives the twisted element ρ∘(K → −K), which "maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does" ([toy note §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)). [Round-4](../../method/review/round-4.md) ruling F3 upheld this and checked it ([`review/round4-adjudication.md`](../../../review/round4-adjudication.md); [`verify/toy_coset.py`](../../../verify/toy_coset.py), "round-4 F3"). The consequence, in the ruling's words: "Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K." That is why the refinement points to [P4](p4-polarized-matter.md). See [the twisted element](../../symmetry-breaking/twisted-element.md) and [locality from an (H, K)-built coupling](../../symmetry-breaking/matter-coupling.md).

## Notation: J or K

The sources do not agree on which real structure to name. [#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) names J as "the real structure J chosen spontaneously", with η = HJ, as in the field-equation note and the lab notebook's v0.3 addendum. [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) defines both, J = η⁻¹H and K = η⁻¹ω. The toy-model note and [#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) call K the real structure, with η = ωK, "K a real structure, K² = 1" (toy note abstract) and Kᵀ ω K = −ω ([toy note §1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work)). The lab notebook's v0.1 called J = η⁻¹H the order parameter ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)). No source reconciles the names; this page quotes each in its own notation. The [order-parameter](../../symmetry-breaking/order-parameter.md) page writes K for the real structure, as the toy-model note does.

## Open: the extra structure the refinement needs

The refinement says what a definite polarization needs; it does not say where that comes from.

- **The potential's origin.** No derivation of the ρ-preserving potential exists. [#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) lists "a derivation of the potential" as still open [O], the toy-model note lists "a derivation of the ρ-preserving potential, which introduces a rigid, unordered pair of axes" under "Not shown" ([§6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations)), and [`CLAUDE.md`](../../../CLAUDE.md) names it as an open end. Before the toy models, the field-equation note had listed "the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" as open ([#5 §F](../../../notes/geometric-core.md#f-status-after-tonight)). The lab notebook's v0.1 had attributed the potential's existence to "the explicit breaking of Grassmannian rotations by the rigid ω (P2)" ([#1 §3](../../../notes/broken-born-theory.md#3-action)); the current position is the refinement's, that ω alone leaves the angle free and a definite polarization needs "more structure than ω alone" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)). See [Open: the origin of the ρ-preserving potential](../../symmetry-breaking/rho-preserving-potential.md).
- **The unreduced model.** [The ordered phase](../../symmetry-breaking/toy-models/coset-model/monte-carlo.md) has been simulated only with [H frozen](../../symmetry-breaking/toy-models/coset-model/frozen-h-reduction.md); "a Monte Carlo with H dynamical" is open ([#11 §14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems); [Open: a Monte Carlo with H dynamical](../../symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo.md)). So is "whether ρ's SO(2) breaks in the coupled model without a potential" ([toy note §6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations); [Open: does ρ's SO(2) break in the coupled model?](../../symmetry-breaking/toy-models/coset-model/so2-question.md)).
- **Beyond the toy.** Everything above is for d = 1; "anything beyond d = 1" is listed as not shown ([toy note §6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations)).

These items are registered in [open problems](../../status/open-problems.md).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — the statement, the forced correction, the credit and the v2.2 refinement; [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) — the definitions of J and K and the det H = 1 corollary; [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — the Siegel domain under P2′; [§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) — τ's circle and "None of this tests the cosmology"; [§14 item 11](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — what is still open
- [`notes/geometric-core.md` §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural) — the repair as derived: the pair (ω, H), the real structure J, Λ(d), and the order-parameter reading; [§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — the modular field; [§F](../../../notes/geometric-core.md#f-status-after-tonight) — unimodularity as the face of ℏ-rigidity, and the potential's origin as open
- [`notes/broken-born-theory.md` §1](../../../notes/broken-born-theory.md#1-postulates) — the original P2's reading of ω; [§2](../../../notes/broken-born-theory.md#2-kinematic-core) — how ρ acts on ω, η and H, and the dimension of Λ(d); [§3](../../../notes/broken-born-theory.md#3-action) — the v0.1 attribution of the potential to the rigid ω; 'Addendum (v0.3)' — the axiom correction as first recorded
- [`notes/broken-born-program-v1.md` §2](../../../notes/broken-born-program-v1.md#2-postulates--including-the-one-the-mathematics-rejected) — the v1 statement
- [`wiki/papers/reciprocity-toy-models.md`](../../papers/reciprocity-toy-models.md) Abstract, [§1](../../papers/reciprocity-toy-models.md#1-setting-and-prior-work) — K, η = ωK and the prior work; [§2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k) — model I's vacua, Goldstone directions and twisted element; [§4](../../papers/reciprocity-toy-models.md#4-quantum-stability) — Mermin–Wagner, the naive and bounded potentials; [§6](../../papers/reciprocity-toy-models.md#6-summary-and-limitations) — what is not shown
- [`notes/toy-lagrangian.md`](../../../notes/toy-lagrangian.md) 'Chunk 2 results' — the continuous U(1) in both toys; 'Chunk 3 results' — the rigid, unordered pair of axes
- [`review/round4-adjudication.md`](../../../review/round4-adjudication.md) 'Rulings' F3 — the twisted element and the K-odd coupling
- [`verify/toy_coset.py`](../../../verify/toy_coset.py) — the Goldstone count, V_b's stability and the twisted-element check; [`verify/battery.py`](../../../verify/battery.py) T2 — det H_Z = 1 for a sampled Z
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the derivation of the ρ-preserving potential as an open end
- [`notes/dual-sector.md` §8](../../../notes/dual-sector.md#8-the-vacuum-and-the-choice-of-polarization); [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 70 — η = HJ (2013) and U(d)/O(d) as the space of choices of η (2016) in Freidel, Leigh and Minic; a breaking tied to the polarization in the vacuum, for another symmetry; quantum rigidity in the flatness of η, not in ω alone; pending
