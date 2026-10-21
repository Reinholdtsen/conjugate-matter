---
title: "Model I vacua, the order parameter and the Goldstone spectrum"
weight: 30
status: alive
description: "The vacua are the compatible pairs, the upper half-plane times a circle K(φ); ρ maps K(φ) to −K(φ), the stabilizer is {±1}, O = K₁₁ flips sign, and three of the four field directions are flat, the compact one parametrizing Λ(1) (criteria S2 and S3)."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "verify/toy_coset.py S2"
  - "verify/toy_coset.py S3"
  - "verify/toy_coset.py 'Spectrum'"
  - "review/round4/referee/audit-notes.md Step 2(a)"
  - "review/round4/referee/audit-notes.md Step 2(d)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_model1.txt"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
---

*The vacua of [model I](/wiki/symmetry-breaking/toy-models/coset-model) are its lowest-energy configurations: constant fields H and K that are compatible, so that the potential vanishes. They form a three-dimensional family, the upper half-plane of metrics times a circle of real structures, and [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ carries each vacuum to a different one, so no vacuum is symmetric (criterion S2). The entry K₁₁ of the real structure takes opposite signs in a vacuum and in its image, which makes it an order parameter (criterion S3). Three of the four directions in which the fields can vary are flat. One of them is the polarization angle: moving along it turns the line of the phase plane that counts as position, at no cost in energy. [Checkpoint #11](/wiki/history/documents/checkpoint) identifies that circle with the one on which its dark-energy field τ lives, as a matter of consistency, not as a test.*

**Status:** Alive — [V] (the worklog records "S2 pass [V]", "S3 pass [V]" and "Spectrum [V]"; checked in `verify/toy_coset.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — confirmed by the round-4 referee; what the breaking means physically is qualified by [the twisted element](/wiki/symmetry-breaking/twisted-element).

## The vacua are the compatible pairs

For constant fields both kinetic terms of [model I's Lagrangian](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) vanish, and what remains is the compatibility potential (λ/8) Tr(H⁻¹ Cᵀ H C), with C = KI + IK and I = ω⁻¹H. It is never negative and is zero exactly when K is compatible with H. Hence the worklog's statement: "The vacua are the compatible pairs (H, K)" ('Chunk 1 results').

### At H = 1: a circle of real structures

At the metric H = 1 the potential is zero exactly when K is symmetric ("|C|^2 = 2 (b - c)^2", `verify/toy_coset.py`). A real structure that is traceless, symmetric and of determinant −1 is a reflection of the plane [T], and these form a circle (toy-model note §2):

```text
K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]
```

The gate checks that "K(phi) is a compatible real structure for every phi" and that "V vanishes on the circle K(phi) at H = 1". K(φ) leaves the line at angle φ/2 in place and reverses the perpendicular line [T], so its eigenlines are L+ at angle φ/2 and L− at φ/2 + π/2. These are the null lines of η = ωK(φ) that the referee found: for v(t) = (cos t, sin t), "v(t)^T eta v(t) = sin(phi - 2t): zeros exactly at t = phi/2, phi/2+pi/2" (`review/round4/referee/audit-notes.md`, Step 2(d)). At φ = 0, K(0) = K₀ = diag(1, −1), and L+ is the x-axis.

As φ goes once around its circle, L+ makes a half-turn and passes through every line through the origin exactly once. The circle of vacua at H = 1 is therefore the set of all possible position axes [T].

### The whole vacuum manifold

"The vacuum manifold is the upper half-plane times this circle." (note §2); the worklog calls it "a 3-dimensional space" ('Chunk 1 results'). Every metric H has its own circle of compatible real structures. Because the action is Sp(2, ℝ)-invariant, a symplectic map that carries the metric 1 to H carries the circle at H = 1 onto the circle at H [T].

## How ρ acts (criterion S2)

Criterion S2 asks that "The minima of S form a set on which ρ acts without fixed points: no vacuum is ρ-invariant, and ρ maps each vacuum to another one." (worklog, 'Success criteria'; [success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)). Version 2: "ρ acts as Z → −1/Z and K(φ) → K(φ + π) = −K(φ)." (§2). The two halves of that statement:

- **On the metric**, ρ is the inversion Z → −1/Z of the upper half-plane, whose only fixed point is Z = i, the metric H = 1 ([reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)). The gate: "rho acts on Z as Z -> -1/Z with fixed point Z = i".
- **On the real structure** at H = 1, ρ shifts the angle by π. The eigenline L+ turns by a quarter-turn onto the old L−: "ρ exchanges L+ and L−" (note §5). The gate: "rho maps the vacuum (1, K(phi)) to (1, -K(phi)) = (1, K(phi + pi))".

A vacuum left in place by ρ would need H = 1, the only fixed metric, together with a K(φ) that ρ leaves unchanged; but ρ turns every K(φ) into −K(φ). The gate's check reads: "no vacuum is rho-invariant: at H = 1 a compatible K with rho^-1 K rho = K must vanish". The referee confirmed each piece with sympy: "rho^T H(Z) rho = H(-1/Z) (difference 0); fixed point Z=i gives H=1; rho^-1 K(phi) rho = K(phi+pi) = -K(phi)" (Step 2(a)).

So the action is symmetric under ρ and none of its vacua is: ρ is [spontaneously broken](/wiki/symmetry-breaking/spontaneous-symmetry-breaking).

## The breaking pattern

"The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}" (note §2). The referee's route to it: a symplectic S that keeps H = 1 must satisfy SᵀS = 1, so it is a rotation R(t), and "R(t)^-1 K0 R(t) = K0 only at t in {0, pi} -> {+-1}" (Step 2(a)). The gate solves the same conditions and passes "the stabilizer of the vacuum (1, K0) in Sp(2,R) is {+1, -1} (so the orbit is 3-dimensional)".

Neither element changes the fields: −1 sends H to (−1)ᵀH(−1) = H and K to K [T]. And −1 = ρ², the half-turn. The worklog writes the pattern as "Only {±1} leaves a vacuum fixed, so Sp(2,R) → Z₂ = {1, ρ²}" ('Chunk 1 results'). Every other element of the group moves the vacuum, and the orbit of (1, K₀) is three-dimensional like the group itself: in the referee's words model I is "a simple coset" (Step 3; [coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models)).

## The order parameter (criterion S3)

Criterion S3: "A local operator built from η (equivalently the real structure K, with η = ωK) has a nonzero expectation value in each vacuum and is odd under ρ." (worklog, 'Success criteria'). Model I's choice is the simplest entry of K: "O = K₁₁ is +1 in (1, K₀) and −1 in its ρ-image" ('Chunk 1 results'); "O = K₁₁ flips sign under ρ" (note §2). The gate: "O = K_11 takes +1 in (1, K0) and -1 in its rho-image (1, -K0)".

On the circle at H = 1, O = K₁₁(φ) = cos φ, and ρ, which shifts φ by π, reverses its sign. The [lattice simulation](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) measures this quantity averaged over the lattice, "m = ⟨cos φ⟩", which the note calls the "Order parameter for ρ" (§4). Because O is built from K, it is built from η = ωK, the program's [order parameter](/wiki/symmetry-breaking/order-parameter).

O is odd under the flip K → −K as well. Without a coupling to matter, "'rho is broken' vs 'K->-K is broken' is a labelling choice" (referee, Step 2(a)); see [the twisted element](#the-twisted-element) below.

## The spectrum: three flat directions and one massive

At a vacuum the fields can vary in four directions: two for the metric (X and Y) and two along the hyperboloid of K. Version 2: "The potential's Hessian has rank 1 at the vacuum. That leaves three Goldstone directions: the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)." (§2). The worklog: "the potential's Hessian has rank 1, giving three Goldstone modes and one massive mode" ('Chunk 1 results').

The count is the standard one [T]. Sp(2, ℝ) is three-dimensional and the unbroken group {±1} is discrete, so there are three [Goldstone directions](/wiki/symmetry-breaking/goldstone-and-higgs), the dimension of the vacuum manifold. The one massive direction is the one along which K stops being compatible with H, since that is what the potential measures.

The machine checks assert the rank. In its coordinates (x, y, u, t) the gate prints the eigenvalues [0, 4, 0, 0] and passes "potential Hessian has rank 1: three flat directions (Goldstones), one massive" (`verify/toy_coset.py`). The referee, in coordinates (X, Y, b, c), found "rank 1, eigenvalues {3:1, 0:3} -> 3 flat directions" (Step 2(a); `review/round4/referee/out_model1.txt`). The nonzero eigenvalue depends on the coordinates; the numbers of zero, positive and negative eigenvalues do not [T].

### The compact direction is Λ(1)

The two half-plane directions are non-compact: Z can run off towards the edge of the half-plane without end. The angle φ is compact: it returns to itself after one turn. The set of Lagrangian lines of the phase plane, which for d = 1 is every line through the origin, is the Lagrangian Grassmannian Λ(1), a circle [T] ([the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian)). φ fixes which line is L+, so it parametrizes Λ(1).

The worklog: "The compact Goldstone is the rotation of K at fixed H: the Lagrangian Grassmannian Λ(1), which is the checkpoint's Maslov circle (the τ field of §10)." ('Chunk 1 results'). The rotations of the phase plane keep H = 1 and turn K around the circle, and ρ is the quarter-turn among them [T]. So, in the worklog's words, Born reciprocity "is one element of a continuous U(1)": in the coset model, "the U(1) stabilizer of H that rotates K" ('Chunk 2 results'). Checkpoint #11 states the same in its refinement of [P2′](/wiki/program/postulates/p2-prime): "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (§4; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

## What follows

### The twisted element

The vacuum is not fixed by ρ, but it is fixed by ρ combined with the flip: "But the twisted element ρ∘(K → −K) maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does. Breaking ρ is physical only once a coupling odd in K is present (§5)." (note §2). This is round-4 finding F3, upheld, and the gate passes "round-4 F3: the twisted rho (rho composed with K -> -K) fixes (1, K_ref)". On the circle at H = 1, ρ and the flip act identically, both sending K(φ) to K(φ + π) = −K(φ) (referee, Step 3, point C1). The coupling that makes the breaking physical is the matter coupling of [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling), which the program attributes to [P4](/wiki/program/postulates/p4-polarized-matter). See [the twisted element](/wiki/symmetry-breaking/twisted-element).

### The angle cannot order by itself in 1+1 dimensions

"In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ." (note §4; [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). Quantum fluctuations along the flat circle would wash out a definite polarization. The note therefore adds "a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" (§4). Its first form, the [naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), proved unbounded below once H moves; the repair is [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential). Where such a potential comes from is [open](/wiki/symmetry-breaking/rho-preserving-potential), and so is whether the coupled model, with H free, orders the compact SO(2) without one ([Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).

### The bridge to τ: consistency only

Checkpoint #11 uses the compact direction in its cosmology: "In the coset model that angle parametrizes Λ(1): it is τ's circle. A definite polarization requires the ρ-preserving potential this section posits." It adds: "None of this tests the cosmology; it only shows the structure is consistent." (§10, "Toy-model support (v2.2) [D][V]"; [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase); [τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). The note is as careful: "Motivation, not result. In a parent framework the polarization angle is identified with a dark-energy field. The Goldstone structure here is consistent with that, but untested by it." (§6). The worklog's further remark that "both toys support §10's identification" goes beyond this: only the coset model's circle is Λ(1) ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

## History

The worklog recorded the vacua, the order parameter and the spectrum on 2026-10-19 as passes of criteria S2 and S3: "As predicted, S1–S3 come almost by construction." Its S2 entry did not contain the twisted element, which the round-4 referee found and version 2 added (revision 2 of `review/round4-adjudication.md`). The referee reproduced the rest — the action of ρ, the stabilizer, the order parameter and the rank-1 Hessian — under its own conventions (Step 2(a)).

## Sources

- `papers/reciprocity-toy-models.md` §2 — the vacua, the action of ρ, the stabilizer, the order parameter, the spectrum and the twisted element, quoted above
- `papers/reciprocity-toy-models.md` §4, §5, §6 — the compact angle and Mermin–Wagner; m = ⟨cos φ⟩; ρ exchanging L+ and L−; "Motivation, not result"
- `verify/toy_coset.py` S2, S3, 'Spectrum' — the gated checks
- `review/round4/referee/audit-notes.md` Step 2(a), Step 2(d), Step 3 — the referee's independent confirmation, the null lines of η, point C1 and the "simple coset" remark
- `review/round4/referee/out_model1.txt` — the referee's printed stabilizer and Hessian
- `notes/toy-lagrangian.md` 'Success criteria', 'Chunk 1 results', 'Chunk 2 results' — criteria S2 and S3; the S2, S3 and spectrum passes [V]; the Maslov-circle remark; ρ inside a continuous U(1)
- `papers/broken-born-checkpoint-v2.md` §4, §10 — the P2′ refinement [D][V]; the toy-model support for τ's circle [D][V], and its limits
- `review/round4-adjudication.md` 'Revisions' 2 — the twisted element added in version 2
