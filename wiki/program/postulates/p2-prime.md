---
title: "P2′: only the symplectic form is rigid"
weight: 40
status: alive
description: "The corrected postulate: only ω (the constancy of ℏ) is fixed and η = HJ is chosen by the vacuum; v2.2 adds that the polarization is a Goldstone angle needing a ρ-preserving potential and made physical only by a K-odd coupling."
provenance: [P]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.3)'"
  - "notes/broken-born-program-v1.md §2"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "notes/toy-lagrangian.md 'Chunk 2 results (2026-10-19): the Grosse–Wulkenhaar route'"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "review/round4-adjudication.md 'Rulings' F3"
  - "verify/toy_coset.py"
  - "verify/battery.py T2"
  - "CLAUDE.md 'Since the handoff'"
---

*P2′ is the program's corrected second axiom: of the structures on phase space, only the symplectic form ω is fixed in advance, and holding it fixed is the program's way of saying that Planck's constant does not change. The [neutral metric](/wiki/phase-space/born-geometry/born-structures) η, which marks which directions count as position, is not part of the background. It is a property of the vacuum: the order parameter of the broken symmetry, the quantity whose value tells a vacuum from its mirror image, as the direction of magnetization tells a magnet pointing one way from one pointing the other. The original P2 had fixed η as well, and the nontriviality theorem showed that this left the program with no content of its own. [Checkpoint](/wiki/history/documents/checkpoint) v2.2 added a refinement from the toy models: with only ω fixed, the polarization is a continuous angle. Two consequences follow. Pinning the angle to a definite value needs an additional potential, which brings back a little fixed structure, and the choice has physical consequences only once matter couples to it.*

**Status:** Alive — [P]; the correction from the original P2 is forced [D] by [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem); the v2.2 Goldstone-angle sentence is [D][V], checked by the [toy-model scripts](/wiki/method/verification/toy-model-scripts). The toy models show that the structure is consistent; they do not test the postulate.

## Statement

```text
P2′  Only ω is rigid (symplectic rigidity ≡ constancy of ℏ). The neutral
     metric η is emergent — the order parameter, η = HJ, with the real
     structure J chosen spontaneously.                                 [P]
```

This is #11 §4's text. Its bracket adds two things: "the correction from the original P2 is *forced*: a nontriviality theorem (§5) shows the theory has content beyond GR + SIDM iff η is emergent. [D]" (GR: [general relativity](/wiki/gravity/spin-2-fields/general-relativity); SIDM: [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter)), and a note on credit, below. Since v2.2 a refinement follows the statement, also below. The program paper v1 states the same axiom as "P2′ (Rigidity — corrected). Only ω is non-dynamical: symplectic rigidity is the constancy of ℏ. The neutral metric η is *not* fundamental; it is the order parameter, η = HJ, with the real structure J chosen spontaneously." (#9 §2).

The axiom has two halves: what is fixed (ω) and what is left to the vacuum (η). Both refer to the structures of [P1](/wiki/program/postulates/p1-arena).

## What is rigid: ω and the constancy of ℏ

A rigid, or non-dynamical, structure is fixed background: it has no equation of motion and takes the same value in every state of the theory [T]. P2′ as stated allows exactly one such structure, the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, the antisymmetric pairing of position with momentum behind the commutator [x, p] = iℏ ([the canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator)).

The physical reading is the one the original P2 already gave ω: "the symplectic structure *is* the constancy of ℏ — phase-space cells do not stretch" (#1 §1). Holding ω fixed holds the size of a phase-space cell fixed, which is the statement that ℏ does not change (#1 §6). The repair keeps exactly this part of the old axiom: "Freeze ω only — that is genuinely ℏ" (#5 §B). Two consequences in the record follow from ω alone:

- **Unimodularity.** The compatibility theorem's [corollary det H = 1](/wiki/phase-space/born-geometry/compatibility-corollaries) is, in the [Debt-1 note](/wiki/history/documents/debt-1-notes)'s words, "the geometric face of ℏ-rigidity" (#5 §F). #11 §5 adds that det H = 1 "persists across the whole modular family of §6" and marks this as machine-verified; the battery's test T2 checks det H_Z = 1 for one randomly sampled member of the family (`verify/battery.py`; [the verification battery](/wiki/method/verification/battery)), so the statement for the whole family is [D], not [V].
- **The cosmological constraint.** "ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run)" [D] (#11 §10), where a and ã are the scale factors of position space and momentum space ([the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint)).

## What is emergent: η as the order parameter

### The construction

The Debt-1 note gives the repair in one sentence: "the fundamental pair is (ω, H); the derived complex structure is I = ω⁻¹H; the vacuum spontaneously selects a real structure J (an involution anticommuting with I), and η ≡ HJ" (#5 §B). In order:

1. The fundamental structures are ω, which is rigid, and the generalized metric H, which is dynamical.
2. From them comes the complex structure I = ω⁻¹H, with I² = −1, a quarter-turn of phase space.
3. The vacuum selects a real structure J: a linear map with J² = 1 (an involution [T]) that anticommutes with I.
4. The neutral metric is then defined from the vacuum's choice, η ≡ HJ.

So η is no longer an input. It is built from the dynamical H and the vacuum's J, and it differs from one vacuum to another.

### Why η is an order parameter

In [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking) the laws are symmetric but the ground state is not, and an order parameter is a quantity that the symmetry would change and that takes a definite value in the ground state, as magnetization does in a magnet [T]. At the standard forms of the structures, the [Born rotation](/wiki/phase-space/reciprocity/born-reciprocity) ρ: (x, p) → (p, −x) leaves ω and H alone but not η. The [lab notebook](/wiki/history/documents/lab-notebook) found that it "preserves ω (it is symplectic), preserves H (it is orthogonal), and **flips the sign of η**, hence flips J and K while preserving I. **[D]**" (#1 §2). A vacuum with a definite η is therefore carried by ρ to a different vacuum, with −η. Under P2′ the Debt-1 note reads the sign flip this way: "the earlier observation that reciprocity flips η now reads correctly as *the broken symmetry moving the order parameter*" (#5 §B). The note calls the assignment "philosophically right" as well, since η "is the structure that says which directions are position", and on this reading the vacuum state, not the background, fixes those directions (#5 §B). See [the order parameter](/wiki/symmetry-breaking/order-parameter).

### The space of vacua

The choices of J form a familiar manifold:

```text
{J} ≅ U(d)/O(d) = Λ(d)                                              (#5 §B)
```

"the Lagrangian Grassmannian — π₁ = ℤ, Maslov circle intact, τ restored" (#5 §B). [The Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) Λ(d) is the space of all [Lagrangian subspaces](/wiki/phase-space/reciprocity/lagrangian-polarizations), all possible choices of "position" directions. It is compact, of dimension d(d+1)/2, which is 10 for d = 4 (#1 §2 [T]). Its non-contractible loop, the Maslov circle, carries the program's dark-energy field τ ([τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)). The metric opens up at the same time: with only ω rigid, "H ranges over Sp(2d,ℝ)/U(d): Z = X + iY" (#11 §6), [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain), whose real part X is the [momentum graviton](/wiki/gravity/momentum-graviton) ([the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z)).

## Why the correction was forced

[The original P2](/wiki/program/postulates/original-p2) held η fixed as well. [The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) [T][V] then allows only H = diag(g, g⁻¹), and the theory reduces to "GR + one bespoke SIDM model, with w ≡ −1 and the gate unexplained" (#5 §B, "Branch R"). [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) states the general point: the program has content beyond that "iff η is emergent". The lab notebook's v0.3 addendum records the change: "P2 is therefore replaced by P2′".

## Precedent and credit

#11 §4: "That η should be dynamical rather than fixed was argued independently in metastring theory [26S]; the reading of η as the order parameter of broken reciprocity is this program's." The toy-model note's survey of prior work says the same in more detail: "Freidel, Leigh and Minic make η dynamical and describe spacetime as a choice of Lagrangian [1]", and they describe a preferred polarization as breaking Born duality, "but give no potential for η and no symmetry-breaking analysis" (toy note §1). See [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality).

## The v2.2 refinement

Checkpoint v2.2 (2026-10-20) appended to P2′ what the [toy models](/wiki/symmetry-breaking/toy-models) had found:

> *Refinement (v2.2, from the toy models):* with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]. Two things follow. A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η. And the breaking of ρ is physical only once matter couples to the sign of K (P4): without such a coupling, a twisted element ρ∘(K → −K) leaves the vacuum invariant. (#11 §4)

The toy models work with phase space ℝ² (d = 1) and fields on a 1+1-dimensional base. In the toy-model note the order parameter is written with a real structure K, η = ωK, with K² = 1 and Kᵀ ω K = −ω (toy note §1); the naming question is below.

### The polarization is a Goldstone angle [D][V]

A Goldstone direction is a direction along the [vacuum manifold](/wiki/symmetry-breaking/topological-defects#the-vacuum-manifold-t) of a broken continuous symmetry: moving along it costs no energy [T] ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)). In the [coset toy model](/wiki/symmetry-breaking/toy-models/coset-model) (model I) the vacua at H = 1 are

```text
K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]                            (toy note §2)
```

a whole circle of them, and "ρ acts as Z → −1/Z and K(φ) → K(φ + π) = −K(φ)" (toy note §2). So ρ moves each vacuum by π along a continuous circle of vacua. The worklog names the continuous group: "the U(1) stabilizer of H that rotates K", and in the complex [Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar), the other toy, "the left phase rotations e^{−iαN}, with the duality at α = π" (worklog, 'Chunk 2 results'). The potential's Hessian at the vacuum has rank 1, leaving three Goldstone directions: two non-compact directions of the upper half-plane and "the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)" (toy note §2; checked in `verify/toy_coset.py`). #11 §10 draws the link to [dark energy](/wiki/cosmology/dark-energy/tau-quintessence): "In the coset model that angle parametrizes Λ(1): it is τ's circle", and adds "None of this tests the cosmology; it only shows the structure is consistent." See [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).

### A definite polarization needs a ρ-preserving potential

A Goldstone angle is not pinned to any value, and in 1+1 dimensions it cannot order at all: "Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ" (toy note §4; [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). To obtain a definite polarization the toy adds "a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" (toy note §4).

- The first form tried, −μ[Tr(K K_ref)]², is "unbounded below once H is dynamical": along a family of boosts it reaches "−8.9 × 10⁶ μ at boost parameter 4", and the reference vacuum is a saddle (toy note §4; [obituary of the naive potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)).
- The normalized form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) is bounded, "−μ ≤ V_b ≤ 0 by Cauchy–Schwarz", and with H dynamical the reference vacuum is "a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236". The zero mode is a flat line that "is not symmetry-protected" (toy note §4; [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)).
- At H = 1, V_b = −(μ/2)(1 + cos 2φ), and with H dynamical the vacuum manifold is "{diag(y, 1/y)} × {±K_ref}" (toy note §4). The two signs ±K_ref are the vacua that ρ exchanges, since ρ sends K to −K at H = 1 (toy note §2).

This is what #11 means by "a rigid, unordered pair of axes". V_b contains K_ref only inside the square [Tr(K K_ref)]², so K_ref and −K_ref define the same potential. The potential fixes the pair of axes along which K_ref points, but not which of the two is position; the worklog calls the price "a rigid, unordered pair of axes (K_ref up to sign)" ('Chunk 3 results'). That places the structure a definite polarization needs between two extremes: more than ω alone, which fixes no axes, and less than a rigid η, which would also fix which axis is position. The worklog draws the same conclusion: the toy supports "broken reciprocity" in the form "a pseudo-Goldstone polarization angle with a ρ-symmetric potential", not "only ω rigid, nothing else" ('Chunk 3 results').

### The breaking is physical only through the sign of K

Model I has a second symmetry besides Sp(2, ℝ): "There is a separate ℤ₂, K → −K" (toy note §2). Combined with ρ it gives the twisted element ρ∘(K → −K), which "maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does" (toy note §2). [Round-4](/wiki/method/review/round-4) ruling F3 upheld this and checked it (`review/round4-adjudication.md`; `verify/toy_coset.py`, "round-4 F3"). The consequence, in the ruling's words: "Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K." That is why the refinement points to [P4](/wiki/program/postulates/p4-polarized-matter). See [the twisted element](/wiki/symmetry-breaking/twisted-element) and [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).

## Notation: J or K

The sources do not agree on which real structure to name. #11 §4 names J as "the real structure J chosen spontaneously", with η = HJ, as in the Debt-1 note and the lab notebook's v0.3 addendum. #11 §5 defines both, J = η⁻¹H and K = η⁻¹ω. The toy-model note and #11 §14 item 11 call K the real structure, with η = ωK, "K a real structure, K² = 1" (toy note abstract) and Kᵀ ω K = −ω (toy note §1). The lab notebook's v0.1 called J = η⁻¹H the order parameter (#1 §2). No source reconciles the names; this page quotes each in its own notation. The [order-parameter](/wiki/symmetry-breaking/order-parameter) page writes K for the real structure, as the toy-model note does.

## Open: the extra structure the refinement needs

The refinement says what a definite polarization needs; it does not say where that comes from.

- **The potential's origin.** No derivation of the ρ-preserving potential exists. #11 §14 item 11 lists "a derivation of the potential" as still open [O], the toy-model note lists "a derivation of the ρ-preserving potential, which introduces a rigid, unordered pair of axes" under "Not shown" (§6), and `CLAUDE.md` names it as an open end. Before the toy models, the Debt-1 note had listed "the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" as open (#5 §F). The lab notebook's v0.1 had attributed the potential's existence to "the explicit breaking of Grassmannian rotations by the rigid ω (P2)" (#1 §3); the current position is the refinement's, that ω alone leaves the angle free and a definite polarization needs "more structure than ω alone" (#11 §4). See [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).
- **The unreduced model.** [The ordered phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) has been simulated only with [H frozen](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction); "a Monte Carlo with H dynamical" is open (#11 §14 item 11; [Open: a Monte Carlo with H dynamical](/wiki/symmetry-breaking/toy-models/coset-model/dynamical-h-monte-carlo)). So is "whether ρ's SO(2) breaks in the coupled model without a potential" (toy note §6; [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).
- **Beyond the toy.** Everything above is for d = 1; "anything beyond d = 1" is listed as not shown (toy note §6).

These items are registered in [open problems](/wiki/status/open-problems).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — the statement, the forced correction, the credit and the v2.2 refinement; §5 — the definitions of J and K and the det H = 1 corollary; §6 — the Siegel domain under P2′; §10 — τ's circle and "None of this tests the cosmology"; §14 item 11 — what is still open
- `notes/debt1a-geometric-core.md` §B — the repair as derived: the pair (ω, H), the real structure J, Λ(d), and the order-parameter reading; §C — the modular field; §F — unimodularity as the face of ℏ-rigidity, and the potential's origin as open
- `notes/broken-born-theory.md` §1 — the original P2's reading of ω; §2 — how ρ acts on ω, η and H, and the dimension of Λ(d); §3 — the v0.1 attribution of the potential to the rigid ω; 'Addendum (v0.3)' — the axiom correction as first recorded
- `notes/broken-born-program-v1.md` §2 — the v1 statement
- `papers/reciprocity-toy-models.md` Abstract, §1 — K, η = ωK and the prior work; §2 — model I's vacua, Goldstone directions and twisted element; §4 — Mermin–Wagner, the naive and bounded potentials; §6 — what is not shown
- `notes/toy-lagrangian.md` 'Chunk 2 results' — the continuous U(1) in both toys; 'Chunk 3 results' — the rigid, unordered pair of axes
- `review/round4-adjudication.md` 'Rulings' F3 — the twisted element and the K-odd coupling
- `verify/toy_coset.py` — the Goldstone count, V_b's stability and the twisted-element check; `verify/battery.py` T2 — det H_Z = 1 for a sampled Z
- `CLAUDE.md` 'Since the handoff' — the derivation of the ρ-preserving potential as an open end
