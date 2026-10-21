---
title: "The order parameter: J, η and K"
weight: 50
status: alive
description: "Reciprocity is broken iff the vacuum carries a definite η: J = η⁻¹H in v0.1, η = HJ in P2′, η = ωK in the toy note; its vacuum manifold Λ(d), its checks in the toy models, the superseded ℤ₄ → ℤ₂ pattern and the unreconciled J/K naming."
provenance: [P]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §13 row 9"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §5"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.3)'"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Predictions'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "review/round4/referee/audit-notes.md 'Step 2(a)' F3"
  - "review/round4/referee/audit-notes.md 'Step 2(c)'"
  - "review/round4/referee/audit-notes.md 'Step 3'"
  - "verify/toy_coset.py S3"
  - "verify/toy_gw.py"
---

*An order parameter is the quantity that tells a broken-symmetry state from a symmetric one, as a magnet's magnetization does: it is zero while the symmetry is intact, and once the symmetry is broken it takes a definite value that the symmetry would change. In the Broken-Born program that role belongs to the neutral metric η, the structure on phase space that marks which directions count as position and which as momentum. Born reciprocity reverses the sign of η, so a vacuum that carries a definite η is not reciprocity-symmetric, and its mirror image carries −η. The program has written this order parameter in three notations over its history, using J, η and K, and the documents do not agree on which of J and K to call "the real structure". An early description of the breaking as a discrete pattern has been replaced by the Goldstone-angle picture.*

**Status:** Alive — [P] (P2′, #11 §4, where "the reading of η as the order parameter of broken reciprocity is this program's") — in the coset toy model the order parameter O = K₁₁ is checked to flip sign under ρ [V] (`verify/toy_coset.py`, S3; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)); the J/K naming is unresolved between #11 and the toy-model note.

## What an order parameter is

In [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking) the laws have a symmetry that the vacuum lacks. An order parameter is a quantity built from the fields that the broken symmetry changes, and whose value in a broken vacuum is definite [T]. It does three jobs at once. It distinguishes the broken phase from the symmetric one, it labels which of the equivalent vacua the system is in, and the symmetry moves it from one vacuum to another. A magnet's magnetization does all three: zero above the Curie temperature, pointing along a definite direction below it, and turned by a rotation.

The toy-model work wrote the requirement as a pass/fail test: "S3 — η as order parameter. A local operator built from η (equivalently the real structure K, with η = ωK) has a nonzero expectation value in each vacuum and is odd under ρ." (worklog, 'Success criteria'; [success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)).

## Three notations for one order parameter

The order parameter is built from the structures of Born geometry ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)): the symplectic form ω, behind the commutator [x, p] = iℏ; the neutral metric η, a symmetric pairing with as many positive as negative directions; and the positive generalized metric H. #11 §5 combines them into three linear maps:

```text
I = ω⁻¹H,   J = η⁻¹H,   K = η⁻¹ω;     I² = −1,   J² = K² = +1,   IJ = K        (#11 §5)
```

I squares to −1, so it is a complex structure, acting on phase space as multiplication by i does on complex numbers. J and K square to +1. Each such involution splits phase space into its +1 and −1 eigenspaces, which makes it a real structure [T]. The documents have written the order parameter with each of these at different times:

```text
J = η⁻¹H               the lab notebook v0.1 (#1 §2), with η rigid          superseded
η = HJ                 P2′ (#11 §4), the v0.3 addendum (#1), #5 §B
η = ωK,   K² = 1       the toy-model note §1, #11 §14 item 11
```

The change from the first line to the second is the program's main axiom correction: η moved from fixed background to vacuum property. The third line is the toy models' notation, with the real structure named K. This page writes K for the real structure, as the toy-model note does, and uses J only when quoting P2′ or the notebook. Which operator deserves the name is not settled ([below](#notation-which-operator-is-the-real-structure)).

## η as the program's order parameter

### The postulate

The current postulate makes η the order parameter [P]:

> **P2′** Only ω is rigid (symplectic rigidity ≡ constancy of ℏ). The neutral metric η is emergent — the order parameter, η = HJ, with the real structure J chosen spontaneously. (#11 §4)

#11 adds that the correction from [the original P2](/wiki/program/postulates/original-p2), which had fixed η too, is "forced: a nontriviality theorem (§5) shows the theory has content beyond GR + SIDM iff η is emergent. [D]" (GR is general relativity, SIDM self-interacting dark matter; [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)). On credit: "That η should be dynamical rather than fixed was argued independently in metastring theory [26S]; the reading of η as the order parameter of broken reciprocity is this program's." (#11 §4; [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)). The lab notebook's v0.3 addendum, which recorded the change in the axiom list, puts it as "η is emergent — the order parameter itself, η = HJ, with the real structure J chosen spontaneously from U(d)/O(d) = Λ(d)" (#1). See [P2′](/wiki/program/postulates/p2-prime).

The Debt-1 note gives the construction step by step: "the fundamental pair is (ω, H); the derived complex structure is I = ω⁻¹H; the vacuum spontaneously selects a real structure J (an involution anticommuting with I), and η ≡ HJ." (#5 §B). It also gives the reason for the assignment: "η is the structure that says which directions are position — of course that is what the vacuum decides, not the background."

### Why η qualifies: reciprocity reverses it

The lab notebook found how the [Born rotation](/wiki/phase-space/reciprocity/born-reciprocity) ρ: (x, p) → (p, −x) acts on the three structures in their standard forms. ρ acts on vectors by R = [[0, 1], [−1, 0]], and "R preserves ω (it is symplectic), preserves H (it is orthogonal), and flips the sign of η, hence flips J and K while preserving I. [D]" (#1 §2). A quarter turn preserves oriented area and length, so it keeps ω and H = 1. It exchanges the position and momentum axes and reverses one of them, which reverses the sign of the symmetric pairing η [T].

So η satisfies the definition. A vacuum with a definite η is carried by ρ to a different vacuum, with −η. Under P2′ the Debt-1 note reads the old observation in exactly these terms: "the earlier observation that reciprocity flips η now reads correctly as *the broken symmetry moving the order parameter*" (#5 §B).

### What η marks: its null lines

A neutral metric has null directions, vectors of zero length, and those are what make η a marker of "position". The toy-model note, in d = 1: "A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK. Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is 'position'." (§1). A Lagrangian line is a possible set of position coordinates ([Lagrangian polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)). Two further facts locate the information η carries: "The null lines of η = ωK(φ) are exactly K's eigenlines L±, and the only ones", and "K → −K sends η → −η with the same null lines. ρ exchanges L+ and L−." (§5). So η and −η single out the same pair of lines, and the sign, the choice between K and −K, says which line of the pair is position. What this means for matter fields is on [the section condition](/wiki/symmetry-breaking/section-condition).

In the language of waves: the position line and the momentum line carry the two descriptions of a state, related as a waveform and its spectrum, and the sign of the order parameter says which of the two counts as position.

## The vacuum manifold of the order parameter

The values the order parameter can take form a manifold. Under P2′, "The space of H-compatible real structures on (ℝ^{2d}, I) is {J} ≅ U(d)/O(d) = Λ(d), the Lagrangian Grassmannian — π₁ = ℤ, Maslov circle intact, τ restored" (#5 §B). [The Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) Λ(d) is the space of all Lagrangian subspaces of phase space, all possible choices of position. It is compact, of dimension d(d+1)/2, which is 10 for d = 4 (#1 §2 [T]). Its non-contractible loop, the Maslov circle, carries the program's dark-energy field τ ([τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)).

In the toy models, with d = 1, the space is a circle. The coset model's vacua at H = 1 are

```text
K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]                     (toy-model note §2)
```

with "The vacuum manifold is the upper half-plane times this circle" once H is allowed to move. ρ acts on the circle as "K(φ) → K(φ + π) = −K(φ)" (toy-model note §2): a half-turn of the order parameter's angle. That the order parameter lives on a continuous circle, so that the polarization is an angle rather than a choice between two settings, is [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).

## The order parameter in the toy models

### Model I: O = K₁₁

In the coset sigma model of H and K ([model I](/wiki/symmetry-breaking/toy-models/coset-model)), "O = K₁₁ flips sign under ρ" (toy-model note §2). The worklog records "S3 pass [V]: O = K₁₁ is +1 in (1, K₀) and −1 in its ρ-image" ('Chunk 1 results'), and the gate runs the check:

```text
PASS  O = K_11 takes +1 in (1, K0) and -1 in its rho-image (1, -K0)
```

(`verify/toy_coset.py`; [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). On the vacuum circle the (1,1) entry of K(φ) is cos φ, and the lattice simulation of the polarization angle uses the same quantity: "Order parameter for ρ: m = ⟨cos φ⟩" (toy-model note §4). With the ρ-preserving potential, at T = 0.6, it takes "⟨|m|⟩ = 0.954 ± 0.0001 at every size", an ordered ℤ₂ phase of the frozen-H reduction ([Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)).

O is odd under ρ, and it is odd under the sign flip K → −K as well, which model I also has as a symmetry. The round-4 referee: "On the H=1 circle rho and K->-K act identically (K(phi) -> K(phi+pi) = -K(phi))" (audit notes, Step 3). A nonzero ⟨O⟩ shows that the vacuum is invariant under neither operation, but it is invariant under their combination, the twisted element ρ∘(K → −K) (toy-model note §2). Without a coupling that is odd in K, whether one calls ρ or the flip the broken symmetry is "a labelling choice" (audit notes, Step 2(a), F3). This is [the twisted element](/wiki/symmetry-breaking/twisted-element), and the reason #11 §4 says the breaking of ρ "is physical only once matter couples to the sign of K".

### Model II: the vacuum's position-versus-momentum spread

The worklog's second route looked for "a field theory on phase space whose own vacuum breaks x ↔ p, with no separate K field" ('Predictions'). In the complex Grosse–Wulkenhaar model ([model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)) the order parameter is built from the vacuum's own profile: "the order parameter is the vacuum's x-versus-p polarization, Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual = Δ(0) cos β", and "It is odd under the duality: Δ(β + π) = −Δ(β)." ('Chunk 2 results'; `verify/toy_gw.py`). Here β is the relative phase of the condensate. Classically every vacuum has a definite Δ; quantum mechanically the phase β is uniformly distributed and ⟨Δ⟩ = 0, so the order parameter vanishes ([quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration); [complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)).

### Where it stands

#11 §14 item 11 records the toy result in the toy notation: "ρ is a symmetry of an explicit action, and η = ωK is the order parameter" in the coset model with a bounded ρ-preserving potential ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)). For d > 1 and for the program's 3+1-dimensional base, η as order parameter remains the postulate P2′.

## Superseded: the discrete breaking pattern

The lab notebook's first version described the breaking as a pattern of finite groups. Its postulate P3 called ρ "the ℤ₄ generated by the complex structure I" (#1 §1). With η rigid, the order parameter was "J = η⁻¹H — equivalently, the choice of which Lagrangian splitting H aligns with. Reciprocity is broken iff ⟨J⟩ ≠ 0 in the vacuum." (#1 §2). Then:

```text
ρ²: (x,p) → (−x,−p) preserves all three structures. The breaking pattern is ℤ₄ → ℤ₂:

        ℤ₄  —⟨J⟩→  ℤ₂ = {1, ρ²}                                      [D]   (#1 §2)
```

The four powers of ρ form the group ℤ₄, since ρ² = −1 and ρ⁴ = 1 [T]. ρ² is the phase-space parity (x, p) → (−x, −p): it reverses η twice and so leaves it unchanged, while ρ and ρ³ reverse it. The vacuum would keep {1, ρ²} and break the quarter turns.

**Why it is superseded.** The pattern assumed the rigid η of the original P2. #11 v2.2 replaces the discrete picture: "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (#11 §4). The Goldstone-angle picture governs ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

**What remains of it.**

- For ρ alone the stabilizer is unchanged. In model I, "Only {±1} leaves a vacuum fixed, so Sp(2,R) → Z₂ = {1, ρ²}" (worklog, 'Chunk 1 results'); ρ² = −1, since ρ "squares to −1" (toy-model note §1).
- In the frozen-H reduction with the ρ-preserving potential, the residual symmetry inside the rotations is discrete again. Examining the note's first version, the round-4 referee found "the potential's SO(2) residue is {+-1, +-rho}" and described the ordered phase as "standard Ising-type" spontaneous symmetry breaking "of the residual Z2 = <rho>/<rho^2>" (audit notes, Step 3; Step 2(c)). {±1, ±ρ} is the four-element group generated by ρ, and {±1} = {1, ρ²} is the notebook's ℤ₂. The discreteness now comes from an added potential, "a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η" (#11 §4), whose origin is open ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)).
- One prediction still cites ρ². #11's photon-dispersion row requires "Linear exactly zero (ρ²-protected); quadratic suppressed" (§13 row 9). #11 does not restate the argument; it exists only in the notebook, under the old pattern: "Corrections to x-sector dispersion require insertions of the symmetry-breaking spurion ⟨J⟩. Under the residual ρ² (a phase-space parity), operators linear in energy are odd and forbidden" [D, schematic] (#1 §4). See [Row 9: photon dispersion](/wiki/predictions/photon-dispersion).

## Notation: which operator is "the real structure"

The documents give the name to different operators, and none reconciles them:

- #11 §4 (P2′) names J: η = HJ, "with the real structure J chosen spontaneously", as do the Debt-1 note (#5 §B) and the notebook's v0.3 addendum.
- #11 §5 defines both, J = η⁻¹H and K = η⁻¹ω.
- The toy-model note names K: "η = ωK (K a real structure, K² = 1)" (Abstract), with Kᵀ ω K = −ω (§1); #11 §14 item 11 follows it with "η = ωK is the order parameter".
- The notebook's v0.1 calls J = η⁻¹H the order parameter (#1 §2).

In #11 §5's algebra both J and K square to +1, so each is a real structure in the sense above; the documents differ in which one they name as the structure the vacuum chooses. This page uses the toy-model note's K; [Born structures](/wiki/phase-space/born-geometry/born-structures) uses #11 §5's definitions. The conflict is listed among the unresolved ones on [conflicts between sources](/wiki/history/documents/source-conflicts), and both conventions are on [notation](/wiki/notation).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — P2′: η emergent as the order parameter [P]; the forced correction; the credit to metastring theory; the v2.2 refinement
- `papers/broken-born-checkpoint-v2.md` §5 — the definitions of I, J, K and their algebra
- `papers/broken-born-checkpoint-v2.md` §13 row 9 — the remaining reliance on ρ²
- `papers/broken-born-checkpoint-v2.md` §14 item 11 — "η = ωK is the order parameter" in the toy
- `papers/reciprocity-toy-models.md` §1 — K, η = ωK and its null lines; ρ squares to −1; §2 — the vacuum circle, ρ's action on it, O = K₁₁; §4 — m = ⟨cos φ⟩ and the ordered phase; §5 — η's null lines and their exchange; Abstract — "K a real structure"
- `notes/debt1a-geometric-core.md` §B — the forced repair: J selected from Λ(d), η ≡ HJ, ρ moving the order parameter
- `notes/broken-born-theory.md` §1 — P3 as the ℤ₄ generated by I; §2 — v0.1: J = η⁻¹H, ρ's action on the three structures [D], the ℤ₄ → ℤ₂ pattern (superseded), Λ(d)'s dimension; §4 — the ρ² argument behind row 9; 'Addendum (v0.3)' — η emergent, "the order parameter itself"
- `notes/toy-lagrangian.md` 'Success criteria' — S3; 'Predictions' — the route with no separate K field; 'Chunk 1 results' — S3 pass [V], the stabilizer {±1}; 'Chunk 2 results' — Δ(β) as model II's order parameter
- `review/round4/referee/audit-notes.md` Step 3 — ρ and K → −K act identically on the circle; the residual {±1, ±ρ} and its Ising-type breaking; Step 2(c) — the residual symmetry found with sympy; Step 2(a), F3 — "a labelling choice"
- `verify/toy_coset.py` — the S3 check of O = K₁₁; `verify/toy_gw.py` — Δ(β) = Δ(0) cos β
