---
title: "The twisted element ρ∘(K → −K)"
weight: 80
status: alive
description: "Within the full symmetry group the vacuum keeps an element that acts on H exactly as ρ does, so breaking ρ is physical only once matter couples to the sign of K."
sources:
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "review/round4-adjudication.md 'Rulings' F3"
  - "review/round4-adjudication.md 'Revisions' 2"
  - "review/round4/referee/audit-notes.md Step 2(a) F3"
  - "review/round4/referee/audit-notes.md Step 3 C1"
  - "review/round4/referee/out_sec5_fix.txt"
  - "review/round4/adjudicator/arb.out F3"
  - "verify/toy_coset.py 'round-4 F3'"
  - "verify/toy_s5.py part C"
  - "notes/toy-lagrangian.md 'Chunk 1 results (2026-10-19)'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions (written before construction)'"
---

*The twisted element is a combined operation in the coset toy model of broken reciprocity: apply Born reciprocity, the exchange of position and momentum, and at the same time reverse the sign of the real structure K, the field whose value marks which of two lines in the position–momentum plane counts as position. Reciprocity alone carries every vacuum of the model to a different one, which is the sense in which the vacuum breaks it. The combination carries the reference vacuum back to itself, and it acts on the model's metric H exactly as reciprocity does. So as long as nothing in the theory depends on the sign of K, the vacuum keeps a symmetry that cannot be told apart from reciprocity, and calling reciprocity broken is a choice of labels. The statement gains physical content once matter couples to the sign of K, which in the program is the role of postulate P4. The round-4 referee found the point, the adjudication upheld it, and [checkpoint #11](/wiki/history/documents/checkpoint) now states it in its postulate P2′.*

**Status:** Alive — no tag of its own: #11 states it in the v2.2 refinement of P2′, whose Goldstone-angle sentence is tagged [D][V] — upheld as round-4 finding F3 (`review/round4-adjudication.md`) and checked in [the gate](/wiki/method/verification/the-gate) (`verify/toy_coset.py`, "round-4 F3"; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Statement

The [toy-model note](/wiki/symmetry-breaking/toy-models) (`papers/reciprocity-toy-models.md`, version 2; "toy note" below) states the result in its section on model I:

> But the twisted element ρ∘(K → −K) maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does. Breaking ρ is physical only once a coupling odd in K is present (§5). (toy note §2)

Checkpoint #11 carries it into the program's postulates, in the v2.2 refinement of [P2′](/wiki/program/postulates/p2-prime): "the breaking of ρ is physical only once matter couples to the sign of K (P4): without such a coupling, a twisted element ρ∘(K → −K) leaves the vacuum invariant" (#11 §4).

The result belongs to [model I](/wiki/symmetry-breaking/toy-models/coset-model), the [coset sigma model](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models) built to show [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), ρ: (x, p) → (p, −x), broken by a vacuum.

## Model I and its two symmetries

Model I has a 1+1-dimensional base and a two-dimensional phase space ℝ², with the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω = [[0, 1], [−1, 0]] (toy note §1). Its two fields are:

- **H**, a positive symmetric symplectic matrix, the phase-space metric. It is written H(Z) for a point Z = X + iY of the [upper half-plane](/wiki/phase-space/modular-field/siegel-domain), and I ≡ ω⁻¹H squares to −1 (toy note §2).
- **K**, a real structure: K² = 1 and Kᵀ ω K = −ω, which for 2 × 2 matrices means "traceless with det K = −1" (toy note §1, §2). Its two eigenlines L+ (eigenvalue +1) and L− (eigenvalue −1) are the candidate position and momentum directions, and "Choosing K is choosing which line is 'position'" (toy note §1). K determines the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η = ωK, the program's [order parameter](/wiki/symmetry-breaking/order-parameter).

The Euclidean Lagrangian (toy note §2; [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)):

```text
L = (f_H²/8) Tr(H⁻¹∂H H⁻¹∂H) + (f_K²/4) Tr(H⁻¹ ∂Kᵀ H ∂K) + (λ/8) Tr(H⁻¹ Cᵀ H C),
    with C = KI + IK
```

The note lists two symmetries: "Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS, and the action is invariant (checked for generic symplectic S, so for ρ). There is a separate ℤ₂, K → −K." (toy note §2).

- Sp(2,ℝ) is the group of linear maps of the plane that preserve ω. The quarter turn ρ = [[0, 1], [−1, 0]] is one of its elements.
- The flip K → −K is a symmetry because the first term of L does not contain K and the other two contain it, or its derivative, exactly twice: the potential through C, which is linear in K.

The gate checks both: "all three terms invariant under rho" and "all three terms invariant under K -> -K" (`verify/toy_coset.py`). The [round-4](/wiki/method/review/round-4) referee states the consequence: "The model's full symmetry group is Sp(2,R) x Z2(K->-K) (both stated in Sec. 2)" (`review/round4/referee/audit-notes.md`, Step 2(a); "audit notes" below).

## What ρ does to the vacuum

The potential vanishes exactly when K is compatible with H. At H = 1 the vacua form a circle,

```text
K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]                        (toy note §2)
```

and the whole [vacuum manifold](/wiki/symmetry-breaking/topological-defects#the-vacuum-manifold-t) is "the upper half-plane times this circle" (toy note §2; [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). The reference vacuum is (H, K) = (1, K₀), the point φ = 0, with K₀ = diag(1, −1). Its eigenline L+ is the x-axis and L− the p-axis.

ρ acts on the two fields separately (toy note §2):

- on H as the Möbius map Z → −1/Z, whose fixed point Z = i is the metric H = 1 ([reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)), so H = 1 stays where it is;
- on the circle of K's as "K(φ) → K(φ + π) = −K(φ)".

So ρ carries (1, K₀) to (1, −K₀), a different vacuum, and the gate confirms that "no vacuum is rho-invariant". Within Sp(2,ℝ), "The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}, and O = K₁₁ flips sign under ρ" (toy note §2). The stabilizer is the set of symmetries that leave a vacuum unchanged ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)) [T]; here it holds only the identity and −1 = ρ². The local quantity O = K₁₁ takes the value +1 in (1, K₀) and −1 in its image under ρ. The worklog of the toy work (`notes/toy-lagrangian.md`; "worklog" below) records the pattern as "Sp(2,R) → Z₂ = {1, ρ²}" ('Chunk 1 results'). These facts are criteria S2 and S3 of the toy work, scored as passed [V] ([success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)).

## The twisted element fixes the vacuum

The flip undoes what ρ does to K, and it does not act on H. Composing the two:

```text
(1, K₀)  ──ρ──▶  (1, −K₀)  ──(K → −K)──▶  (1, K₀)
```

The twisted element ρ∘(K → −K) therefore maps the reference vacuum to itself, and since the flip leaves H alone, it acts on H exactly as ρ does. Three scripts check it:

- the round-4 referee: "twisted rho on (1,K0): H -> [1,0,0,1], K -> [1,0,0,-1]" (audit notes, Step 2(a), F3);
- the adjudicator: "H -> [1. 0. 0. 1.]  K -> [ 1. -0. -0. -1.]  fixed: True" (`review/round4/adjudicator/arb.out`);
- the gate: "round-4 F3: the twisted rho (rho composed with K -> -K) fixes (1, K_ref)" (`verify/toy_coset.py`, where K_ref = diag(1, −1)).

The referee adds that on the circle of vacua at H = 1, "rho and K->-K act identically (K(phi) -> K(phi+pi) = -K(phi))" (audit notes, Step 3, C1), so their composition leaves each vacuum of that circle in place, not only (1, K₀).

The stabilizer therefore depends on which group it is computed in. In Sp(2,ℝ) alone it is {±1}, and both elements act trivially on every field configuration, while ρ acts on the metric field as Z → −1/Z. In the full group Sp(2,ℝ) × ℤ₂, in the referee's words, "its stabilizer of the vacuum contains an element acting on H exactly as rho" (audit notes, F3).

## Why the breaking needs a coupling odd in K

The referee's reading of model I without matter: "Without matter couplings, 'rho is broken' vs 'K->-K is broken' is a labelling choice." (audit notes, F3). One description says that the vacuum breaks ρ; the other says that it breaks the flip and keeps the twisted element, which does to H everything ρ does. Both describe the same vacuum, and nothing in model I distinguishes them, because "model I as defined has no matter" (audit notes, F3).

The ambiguity goes away when the theory contains a term that depends on the sign of K: such a term breaks the flip explicitly, so the flip, and with it the twisted element, is no longer a symmetry. The referee: "The Sec. 5 coupling I_K breaks K->-K explicitly, which removes the ambiguity -- but model I as defined has no matter." (audit notes, F3). The adjudication upheld the finding, with this evidence:

> `arb.py`: (1, K₀) is mapped to itself. Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K. This sharpens the S5 conclusion rather than contradicting it. (`review/round4-adjudication.md`, F3)

The coupling the note supplies is I_K, a functional of a matter state's [Wigner function](/wiki/phase-space/reciprocity/wigner-function) built from H and K ([Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)): "**I is odd in K**, so it breaks the K → −K symmetry and makes the breaking of ρ physical (§2)." (toy note §5; see flag 2 in `review/wiki-build-flags.md`). It has the two properties the argument needs:

- **Flipping K alone changes it.** For the note's test state the referee found "K->-K alone: I_-K[psi] - I_+K[psi] = -0.046925 (nonzero: K->-K alone is not a symmetry of I)" (`review/round4/referee/out_sec5_fix.txt`).
- **ρ applied to K and to the state together leaves it unchanged.** ρ acts on states by the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) F and on K by K → −K (`verify/toy_s5.py`: "rho acts on states by the Fourier transform: psi -> psi~, and on K by K -> -K"), and "The combined map (ψ → Fψ, K → −K) leaves I invariant" (toy note §5).

So I keeps ρ and breaks the flip. The adjudication's last sentence refers to criterion S5, the requirement that the vacuum's choice make matter's interactions local in position in one vacuum and in momentum in the other: the coupling that delivers the weak form of S5 is the same one that gives the breaking of ρ its physical content.

## Where the program puts the coupling: P4

In the program the coupling of matter to the sign of K is the job of postulate [P4](/wiki/program/postulates/p4-polarized-matter): "Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations" (#11 §4), with ordinary matter in the first and its ρ-image in the second. #11's P2′ refinement names P4 for this role, and the adjudication's example is "P4-type matter through I_K". So the breaking of reciprocity that the program's [hard core](/wiki/program/hard-core) asserts is, in the toy, physical only together with a matter sector that couples to K's sign.

That coupling has to be put in. "Nothing here forces that coupling" (toy note §5), and the worklog's analysis of locality concludes that matter's section "is locked to K's sign only through the K-covariant coupling" and that "The lock is P4" ('Chunk 4'). Whether anything forces the lock is [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality).

## How it was found

The toy work's first pass did not contain the point. The worklog scored criterion S2 on ρ alone ("No vacuum is ρ-invariant"; "Only {±1} leaves a vacuum fixed, so Sp(2,R) → Z₂ = {1, ρ²}", 'Chunk 1 results'), and neither S2 nor its verdict on [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) mentions the twisted element ('Assessment against the predictions'). The first version of the note listed the flip among the symmetries but, as the referee put it, "the stabilizer is computed in Sp(2,R) only"; its "no vacuum is rho-invariant" "is true for rho alone; 'Born reciprocity is broken' in model I is a labelling choice until a K-odd coupling (Sec. 5's I_K: K->-K alone changes it by -0.046925) is added" (audit notes, Step 3, C1).

The blind referee of [review round 4](/wiki/method/review/round-4) found the twisted element while re-deriving model I (finding F3, audit notes, Step 2(a)) and returned to it in the conceptual audit (C1). The adjudication upheld F3, and its revision 2 asked version 2 to "state the twisted ρ (F3). Breaking ρ is physical only with a K-odd coupling." Version 2 states it in the abstract ("a twisted combination of ρ with that flip leaves the vacuum invariant. Breaking ρ becomes physical only once a coupling odd in K is present"), in §2, and in its list of results ("including the twisted-ρ caveat", §6). #11 v2.2 states it in P2′, and the gate checks it.

## Sources

- `papers/reciprocity-toy-models.md` §2 — model I's fields, action, symmetries, vacua, stabilizer and the twisted element; Abstract, §6 — the twisted-ρ caveat in the summary; §1 — the real structure K and η = ωK; §5 — the coupling I_K ("odd in K" in the note's words) and its invariance under the combined map
- `papers/broken-born-checkpoint-v2.md` §4 — the statement in the P2′ refinement; P4
- `review/round4-adjudication.md` 'Rulings' F3, 'Revisions' 2 — the finding upheld, "This sharpens the S5 conclusion", and the revision
- `review/round4/referee/audit-notes.md` Step 2(a) F3, Step 3 C1 — the referee's finding, the "labelling choice" reading, the full group Sp(2,R) × Z₂, and the stabilizer computed in Sp(2,R) only
- `review/round4/referee/out_sec5_fix.txt` — the flip alone changes I by −0.046925
- `review/round4/adjudicator/arb.out` — the arbitration check of F3
- `verify/toy_coset.py` — the gated checks of the symmetries, the vacua, the stabilizer and "round-4 F3"; `verify/toy_s5.py` part C — how ρ acts on states and on K
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Assessment against the predictions' — criterion S2 and the verdict, without the twisted element; 'Chunk 4' — the K-covariant lock and "The lock is P4"
