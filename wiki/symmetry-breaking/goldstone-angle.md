---
title: "The polarization as a Goldstone angle"
weight: 60
status: alive
description: "Where ρ sits inside a continuous U(1) (model I and the complex model II), the x-sharp and p-sharp vacua are joined by a flat direction, so a definite polarization needs a ρ-preserving potential; in model I the angle is τ's circle (consistency only), and the worklog's τ-drift and 3+1 remarks are uncomputed conjectures."
provenance: [D, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §6"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/toy-lagrangian.md 'Assessment'"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §4"
  - "review/round4-adjudication.md 'Revisions' 3"
  - "review/round4/referee/audit-notes.md 'Step 2(b)'"
  - "review/round4/referee/audit-notes.md 'Step 3'"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "verify/toy_s4.py"
---

*Born reciprocity is a quarter turn of the position–momentum plane, the operation the Fourier transform performs when it turns a waveform into its spectrum. In the program's toy models this exchange is one member of a continuous family of symmetries, so the vacuum's polarization, which fixes the direction that counts as position, is an angle that can turn smoothly rather than a switch with two settings. Turning that angle costs no energy, which makes it a Goldstone direction: the position-sharp and momentum-sharp vacua lie on one continuous family. This finding, recorded in #11 v2.2, is why a definite polarization needs an added potential on the angle. In the coset model the angle is the same circle that the program identifies with its dark-energy field τ, which shows that the structures fit together but does not test the cosmology. It is evidence from two toy models, not a theorem.*

**Status:** Alive — [D][V] (#11 §4, P2′ refinement; #11 §10, "Toy-model support (v2.2) [D][V]") — machine-checked in the toy models (`verify/toy_coset.py`, `verify/toy_gw.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)); the link to τ is consistency only, and two worklog remarks, the drift of τ as a turning angle and continuous breaking in 3+1, are uncomputed conjectures.

## The finding

The toy-model worklog states the result in its second chunk, after both models had been built:

> **The structural finding, common to both toys.**
> - At the self-dual point, Born reciprocity is never the whole symmetry. It is one element of a continuous U(1):
>   - the coset model: the U(1) stabilizer of H that rotates K;
>   - Grosse–Wulkenhaar: the left phase rotations e^{−iαN}, with the duality at α = π.
> - So "which polarization" is an angle on a Goldstone circle, not a discrete choice. The x-sharp and p-sharp vacua are joined by a flat direction.
>
> (worklog, 'Chunk 2 results')

and adds: "This is model-level evidence from two toys, not a theorem." The program's documents record it in two places, both tagged [D][V]:

- **In the postulates.** #11's refinement of [P2′](/wiki/program/postulates/p2-prime): "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]." (#11 §4).
- **In the cosmology.** "Toy-model support (v2.2) [D][V]: in an explicit ρ-symmetric coset model of (H, K), and in the complex self-dual Grosse–Wulkenhaar model, ρ sits inside a continuous U(1), so the polarization is a Goldstone angle." (#11 §10).

A Goldstone direction is a direction along the family of equivalent vacua, along which the potential is flat ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)). The finding qualifies the program's argument that some polarization must be selected ([mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking)): what is selected is a point on a circle. The worklog lists it first among the "Findings that were not predicted" ('Assessment').

## Model I: the rotations that keep H fixed

The coset sigma model ([model I](/wiki/symmetry-breaking/toy-models/coset-model)) has two fields on a 1+1-dimensional base, a phase-space metric H and a real structure K, and its action is invariant under the whole symplectic group Sp(2, ℝ) (toy-model note §2). On H, ρ acts as the inversion Z → −1/Z of the upper half-plane, whose fixed point Z = i is H = 1 (`verify/toy_coset.py`). The symplectic maps that keep H = 1 fixed are the rotations of the phase plane, the group SO(2) ≅ U(1) [T]; in the gate's stabilizer computation, keeping H = 1 fixed is the condition SᵀS = 1, together with det S = 1. ρ = [[0, 1], [−1, 0]] is the quarter turn in this group. This is the worklog's "U(1) stabilizer of H that rotates K".

The vacua at H = 1 form a circle on which the potential vanishes:

```text
K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]                      (toy-model note §2)

ρ:  K(φ) → K(φ + π) = −K(φ)
```

The gate checks that the potential vanishes on the whole circle, and that ρ maps "the vacuum (1, K(phi)) to (1, -K(phi)) = (1, K(phi + pi))" (`verify/toy_coset.py`). Each K(φ) has two eigenlines, which are the candidate position and momentum lines ([the order parameter](/wiki/symmetry-breaking/order-parameter)). At φ = 0, K = K₀ = diag(1, −1), whose +1 eigenline is the x axis; at φ = π, K = −K₀, whose +1 eigenline is the p axis. The worklog's names for the two vacua ±K_ref are "'x is position' and 'p is position'" ('Chunk 3 results'). In between, the pair of lines turns in the phase plane, and every intermediate vacuum has the same energy: the x-sharp and p-sharp vacua are joined by a flat direction.

The Hessian confirms that the circle is flat. "The potential's Hessian has rank 1 at the vacuum. That leaves three Goldstone directions: the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)." (toy-model note §2; checked in `verify/toy_coset.py`; see [the count in model I](/wiki/symmetry-breaking/goldstone-and-higgs#the-count-in-model-i)). The polarization angle is the compact one.

The rotations of the phase plane also have a familiar action on wavefunctions [T]. A rotation by an angle α acts on a state, up to a phase, as the fractional Fourier transform of that angle: at α = 0 the state is unchanged, at a quarter turn it becomes its ordinary Fourier transform, the momentum wavefunction, and the intermediate angles interpolate continuously between a waveform and its spectrum. Model I itself contains no wavefunctions; matter enters the toy only in §5 of the note, where ρ acts on a state as ψ → Fψ, F the Fourier transform. The continuous family that contains ρ is, in that language, the family of fractional Fourier transforms that contains F ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform)).

## Model II: the left phase rotations

The second toy is the self-dual Grosse–Wulkenhaar model with complex fields ([model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)), a field theory on a noncommutative plane written in its matrix base. In units where the kinetic coefficient is 1 its action is (toy-model note §3)

```text
S[φ] = Σ_mn (m + n + 1 − μ²)|φ_mn|² + λ Tr((φ†φ)²)
```

"It satisfies S[UφV†] = S[φ] for all diagonal unitaries U, V. The duality Πφ is the α = π element of e^{−iαN}." Here the duality is the program's ρ in this model: on the matrix base it acts as D f_mn = (−1)^m f_mn, left multiplication by parity ([the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma)). The left phase rotation e^{−iαN} multiplies row m of the matrix φ_mn by the phase e^{−iαm}; at α = π the phases are (−1)^m and the rotation is the duality.

The vacua at μ² = 4, λ = 1 have two condensed levels: "Gradient descent from random starts always reaches a diagonal φ with |φ_mm|² = (1.5, 0.5, 0, …) and S_min = −2.5. The relative phase β of φ₀₀ and φ₁₁ is free. The duality maps β → β + π, so no vacuum is invariant." (toy-model note §3). The phase β is the flat direction, and the vacuum's position-versus-momentum polarization varies along it as a cosine:

```text
Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual = Δ(0) cos β,    Δ(0) > 0              (toy-model note §3)
```

"β = 0 is broader in position than in momentum; β = π is its image." The worklog adds that β = ±π/2 "is balanced" ('Chunk 2 results'). Here the flat direction literally carries the vacuum from one polarization through the balanced point to the other ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)). The gate prints Δ(0) = 10.8828 and checks "Delta(beta) = Delta(0) cos(beta): the polarization is an angle on the Goldstone circle" (`verify/toy_gw.py`). The round-4 referee reproduced the cosine with an independent Fourier quadrature, "to 6 decimals at 9 angles", and the same sign of Δ(0); its value, +0.866025, differs from the gate's, and the documents do not compare the two normalizations (audit notes, Step 2(b)).

In this model the Goldstone angle is a classical statement only. "In complex model II the breaking does not survive quantization: every condensate phase is an exact flat direction, and the condensate is a localized lump with no volume factor." (toy-model note, Abstract). The quantum measure is uniform in β and ⟨Δ⟩ = 0 (§4; [quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).

## Scope: where the finding holds

The worklog wrote the finding for every self-dual point ("At every self-dual point, ρ sits inside a continuous U(1)", 'Assessment'). The real Grosse–Wulkenhaar model, the version the duality literature studies, does not fit it. There "the duality is only a covariance", not a symmetry of the field space, and the vacua are discrete: "The vacua are diag(±√q₀, ±√q₁). Up to the global sign, the two relative signs are classically degenerate (S = −2.5) but have different fluctuation spectra." (toy-model note, Abstract and §3). One loop lifts the degeneracy explicitly, in favour of the vacuum sharper in position ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields); [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)). The round-4 referee drew the consequence that in the real model the polarization is a discrete classical choice, lifted explicitly at one loop, not a Goldstone angle (audit notes, Step 2(b), F4), and that the general claim "is true for the two models chosen" (Step 3). Revision 3 of the adjudication: "Restrict 'Goldstone angle' to the complex model."

The note v2 states the scope accordingly: "Where ρ sits inside a continuous U(1) — model I, and model II with complex fields — the polarization is a Goldstone angle." (Abstract), and "In model I and complex model II, ρ sits inside a continuous U(1), so the polarization is a Goldstone angle." (§6). Both models have d = 1 on a 1+1-dimensional base, and "anything beyond d = 1" is listed as not shown (§6).

## What follows: a definite polarization needs a potential

A Goldstone angle is not pinned. The worklog's first consequence: "(i) P5's 'the vacuum selects a polarization; ours is x-tilted' needs explicit breaking of that U(1) — a potential on the circle — to make the selection definite." ('Chunk 2 results'; [P5](/wiki/program/postulates/p5-spontaneous-selection)). In 1+1 dimensions there is a second reason: "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ." (toy-model note §4; [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)).

Model I therefore adds "a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" (toy-model note §4):

- The first form, −μ[Tr(K K_ref)]², "is unbounded below once H is dynamical" ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)).
- The bounded form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) satisfies "−μ ≤ V_b ≤ 0", and "With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236." At H = 1, "V_b = −(μ/2)(1 + cos 2φ)", which is lowest at the two vacua ±K_ref ([the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)).

With the potential the angle is no longer exactly flat: it is a pseudo-Goldstone mode ([pseudo-Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs#pseudo-goldstone-modes)). The worklog's verdict on what the toy supports: "a pseudo-Goldstone polarization angle with a ρ-symmetric potential", not "only ω rigid, nothing else" ('Chunk 3 results'). On the lattice, with H frozen at 1, the potential produces an ordered ℤ₂ phase, "⟨|m|⟩ = 0.954 ± 0.0001 at every size", while without it the magnetization falls with system size, "No true order" (toy-model note §4; `verify/toy_s4.py`; [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)). The round-4 referee found the residual symmetry inside the rotations to be the discrete group {±1, ±ρ} (audit notes, Step 3; see [the superseded discrete pattern](/wiki/symmetry-breaking/order-parameter#superseded-the-discrete-breaking-pattern)).

#11 records the price: "A definite polarization needs a ρ-preserving potential on that angle — a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η." (§4). V_b contains K_ref only through the square [Tr(K K_ref)]², so K_ref and −K_ref give the same potential: it fixes a pair of axes without saying which is position. #11 §10 adds: "A definite polarization requires the ρ-preserving potential this section posits. That potential must be bounded with all fields dynamical — the round-4 review found the naive form unbounded once H moves". Where the potential comes from is open ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)), and even a definite angle breaks ρ physically only once matter couples to the sign of K ([the twisted element](/wiki/symmetry-breaking/twisted-element)).

## The coset angle is τ's circle

In model I the compact Goldstone direction is the program's own polarization circle. The worklog: "The compact Goldstone is the rotation of K at fixed H: the Lagrangian Grassmannian Λ(1), which is the checkpoint's Maslov circle (the τ field of §10)." ('Chunk 1 results'). In the program, the space of possible polarizations is [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) Λ(d) = U(d)/O(d), and "the dark-energy field τ is the Maslov phase of the boundary variable, its periodicity a fact of topology (π₁(U(d)/O(d)) = ℤ)" (#11 §6; [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)). The lab notebook defined τ as "a compact, 2πf-periodic modulus of the vacuum" (#1 §2). In d = 1, Λ(1) is a circle, and the toy's angle φ parametrizes it.

#11 §10 states the connection and its limit together: "In the coset model that angle parametrizes Λ(1): it is τ's circle." and "None of this tests the cosmology; it only shows the structure is consistent." The note, written for blind review without naming the program, puts it as "Motivation, not result. In a parent framework the polarization angle is identified with a dark-energy field. The Goldstone structure here is consistent with that, but untested by it." (§6). Only the coset circle is Λ(1); the model-II angle β is the relative phase of two condensed levels. In the program τ has a potential of its own, "hilltop quintessence on the Maslov circle" (#11 §10; [τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence)), and the lab notebook calls τ "a (pseudo-)Goldstone" [D] (#1 §4).

## Conjecture: the thawing of τ as a drift of the polarization angle

The worklog drew two further consequences for the program, beyond what the note and #11 claim ('Chunk 2 results'):

- "(ii) In the coset toy, the circle is the Lagrangian Grassmannian Λ(1), the checkpoint's τ. So both toys support §10's identification of the dark-energy field with the polarization angle, and say the polarization is set by where τ sits on its potential."
- "(iii) It also means the present-day thawing of τ would be a slow drift of the polarization angle. That is a claim about the program, not verified here."

The first sentence of (ii) is the identification above. The rest overstates: only the coset circle is Λ(1), and #11 §10 claims consistency, not support. (iii) is a conjecture: no document computes the drift, and the worklog itself marks it unverified. The program's dark-energy prediction is [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift); the polarization-angle reading of that drift appears only in the worklog.

## Conjecture: continuous breaking in 3+1 dimensions

The worklog's remark on the program's own dimension ('Chunk 3 results'):

> In 3+1, the program's actual dimension, Coleman–Mermin–Wagner does not apply. There the self-dual coset model can break the continuous U(1) itself, with τ an exactly massless Goldstone. §10's τ has a potential, so the explicit breaking is in the program anyway.

The assessment repeats it as unpredicted finding 3: "In 1+1, 'only ω rigid' is not enough for a definite polarization. A ρ-preserving potential on the polarization circle is required. In 3+1 the continuous breaking is allowed, and §10's potential supplies the explicit breaking anyway." ('Assessment'). The first sentence is the scope of the theorem, which constrains two dimensions or fewer [T] ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). That the coset model does break the U(1) in 3+1 is not computed anywhere in the record, and the note v2 covers only 1+1 with d = 1. The remark's last sentence notes that τ has a potential in the program anyway; with it, τ is the "(pseudo-)Goldstone" of the lab notebook (#1 §4) rather than an exactly massless mode ([fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force)).

## Open: what the toy models leave undecided

- **The coupled model without a potential.** "whether ρ's SO(2) breaks in the coupled model without a potential" (toy-model note §6), since the hyperbolic H-sector can break in two dimensions; see [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question).
- **H dynamical on the lattice.** "a Monte Carlo with H dynamical" (#11 §14 item 11 [O]); the ordered phase is shown only in [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction).
- **The potential's origin.** "a derivation of the potential" (#11 §14 item 11 [O]); "a derivation of the ρ-preserving potential, which introduces a rigid, unordered pair of axes" (toy-model note §6).
- **More dimensions.** "anything beyond d = 1" (toy-model note §6).

These are registered in [open problems](/wiki/status/open-problems).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — the P2′ refinement: a Goldstone angle [D][V]; the potential as "a rigid, unordered pair of axes"
- `papers/broken-born-checkpoint-v2.md` §10 — 'Toy-model support (v2.2)' [D][V]: τ's circle, the bounded potential, consistency only; τ as hilltop quintessence; §6 — τ as the Maslov phase; §14 item 11 — what remains open
- `papers/reciprocity-toy-models.md` Abstract, §6 — the scope (model I and complex model II), the restoration, "Motivation, not result", what is not shown; §2 — model I's vacuum circle, ρ's action, three Goldstone directions; §3 — model II's action, U(1) phases, vacua, Δ(β), the real model's discrete vacua; §4 — Mermin–Wagner for the compact SO(2), the naive and bounded potentials, the Monte Carlo; §5 — ρ on matter states as ψ → Fψ
- `notes/toy-lagrangian.md` 'Chunk 2 results' — the structural finding and consequences (i)–(iii); 'Chunk 1 results' — the compact Goldstone as Λ(1), the Maslov circle; 'Chunk 3 results' — the pseudo-Goldstone verdict, the vacua ±K_ref, the 3+1 remark; 'Assessment' — the findings that were not predicted
- `notes/broken-born-theory.md` §2 — τ as a compact, periodic modulus; §4 — τ as a (pseudo-)Goldstone
- `review/round4-adjudication.md` 'Revisions' 3 — "Goldstone angle" restricted to the complex model
- `review/round4/referee/audit-notes.md` Step 2(b) — the independent reproduction of Δ(β); F4, the real model's discrete choice; Step 3 — "true for the two models chosen"; the residual group {±1, ±ρ}
- `verify/toy_coset.py` — the vacuum circle, ρ's action and the flat directions of model I; `verify/toy_gw.py` — the U(1) phases, the flat β and Δ(β) = Δ(0) cos β; `verify/toy_s4.py` — the lattice runs with and without the potential
