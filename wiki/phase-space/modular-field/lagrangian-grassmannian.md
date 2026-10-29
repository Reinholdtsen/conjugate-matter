---
title: "The Lagrangian Grassmannian Λ(d)"
weight: 40
status: established
description: "The compact manifold U(d)/O(d) of all position/momentum splittings of phase space (dimension d(d+1)/2 = 10 at d = 4), its Maslov class π₁ = ℤ, its higher homotopy π₂ = π₃ = ℤ₂ at d = 4, its place as the Shilov boundary of the Siegel domain, and its role as the space of vacuum polarizations."
provenance: [T]
sources:
  - "notes/broken-born-theory.md §2"
  - "notes/geometric-core.md §B–§D"
  - "notes/tuning-test.md §4"
  - "notes/x-classification.md §3"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "verify/toy_coset.py"
  - "notes/broken-born-theory.md §8"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/broken-born-checkpoint-v2.md §14 item 12"
  - "notes/closed-universe.md §8"
  - "verify/closed_universe.py section F"
  - "review/wiki-build-flags.md flag 61"
---

*The Lagrangian Grassmannian Λ(d) is the space of all ways to split a 2d-dimensional phase space into a "position" half and a "momentum" half. Each [Lagrangian subspace](/wiki/phase-space/reciprocity/lagrangian-polarizations), a d-dimensional plane on which the symplectic form vanishes, is one point of it. For d = 1 it is the set of lines through the origin of the (x, p) plane, which is a circle; in general it is the compact manifold U(d)/O(d), of dimension 10 when d = 4. It contains a loop that cannot be shrunk to a point, the Maslov circle, so any angle measured around that loop is periodic. At d = 4 its topology also allows point defects and textures, and whether the early universe made any is an open question of the program. It also forms the distinguished (Shilov) boundary of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain). In the program it is the space of possible vacuum polarizations, and its circle direction carries the dark-energy field. The mathematics is standard.*

**Status:** Established — standard mathematics [T] ([#1](/wiki/history/documents/lab-notebook) §2 tags the definition, the dimension and π₁ = ℤ [T]; [#11](/wiki/history/documents/checkpoint) §6 tags the Shilov-boundary statement [T]; [calc note #5](/wiki/history/documents/field-equation-notes) marks it "[standard]"). At d = 4, π₁(Λ(4)) = ℤ and π₃(Λ(4)) = ℤ₂ are machine-checked [V] in `verify/closed_universe.py` section F, where π₂(Λ(4)) = ℤ₂ [T] follows by exactness ([the closed-universe script](/wiki/method/verification/closed-universe-script#f-topology-of-the-polarization-manifold-8-checks)); the rest is not machine-checked as such. Its d = 1 case, Λ(1), is the compact [Goldstone direction](/wiki/symmetry-breaking/goldstone-and-higgs) of the [toy model](/wiki/symmetry-breaking/toy-models/coset-model) checked in `verify/toy_coset.py`.

## What it is

### Lagrangian subspaces

Phase space ℝ^{2d} carries the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, which pairs each position with its momentum: with ω = [[0, 1], [−1, 0]] in the (x, p) block basis, ω((x, p), (x′, p′)) = x·p′ − p·x′ [T]. A Lagrangian subspace is a d-dimensional subspace on which ω vanishes identically; d is the largest dimension for which that is possible [T]. The position plane {p = 0} and the momentum plane {x = 0} are Lagrangian. So is the graph p = Ax of any real symmetric d × d matrix A, and these graphs are all the Lagrangian subspaces that meet the momentum plane only at the origin [T].

Choosing one Lagrangian subspace to call "position" is choosing a polarization: it fixes which coordinates a wavefunction is written in, as a waveform is written as a function of time and its spectrum as a function of frequency ([the Fourier transform](/wiki/phase-space/reciprocity/fourier-transform); [Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)). The [toy-model note](/wiki/symmetry-breaking/toy-models) states the d = 1 case: the null lines of a neutral metric "are Lagrangian. Choosing K is choosing which line is 'position'" (§1).

### The space of them: U(d)/O(d)

Lagrangian subspaces form a manifold, the Lagrangian Grassmannian. #1 §2: "The space of Lagrangian polarizations of ℝ^{2d} is the Lagrangian Grassmannian Λ(d) ≅ U(d)/O(d), compact, of dimension d(d+1)/2 = 10 for d = 4. **[T]**"

The form U(d)/O(d) comes from a symmetry argument [T]. Phase space can be identified with ℂ^d, positions as real parts and momenta as imaginary parts. The unitary group U(d) then acts by maps that preserve both ω and the unit metric, and it carries the position plane ℝ^d onto every Lagrangian subspace. The unitary maps that carry the position plane onto itself are the real orthogonal matrices, O(d). Each Lagrangian subspace is therefore a unitary matrix taken up to an orthogonal factor on the right: Λ(d) = U(d)/O(d). Its dimension is dim U(d) − dim O(d) = d² − d(d − 1)/2 = d(d + 1)/2, the number of independent entries of a symmetric d × d matrix, as the graph picture suggests. It is compact because U(d) is.

For d = 1, U(1)/O(1) is the circle of unit complex numbers e^{iθ} with e^{iθ} and −e^{iθ} identified: the lines through the origin of the plane, a line at angle θ being the same line as at θ + π [T].

The notes write Λ(d) with d = 4 the physical case, and #11 writes Λ(4) when it means that case (§7: the second frame "confined to compact Λ(4)"). The two agree.

## The Maslov class

#1 §2: "Its fundamental group is π₁(Λ(d)) = ℤ, generated by the **Maslov circle** via the map det²: U(d)/O(d) → U(1). **[T]**"

What this says [T]. A unitary matrix U has a determinant det U of modulus 1. Multiplying U on the right by an orthogonal matrix O describes the same Lagrangian subspace but multiplies det U by det O = ±1. So det U is not a function on Λ(d), while its square det² U is. The map det² sends each Lagrangian subspace to a point of the unit circle. Along a closed loop of Lagrangian subspaces, the number of times det² winds around the circle is an integer, the Maslov index of the loop (Maslov 1965 †; Arnold 1967 †). Loops with different counts [cannot be deformed into each other](/wiki/symmetry-breaking/topological-defects#homotopy-groups-t), loops with the same count can be, and every integer occurs, so π₁(Λ(d)) = ℤ. A loop that winds once is a Maslov circle.

For d = 1, the line at angle θ is U = e^{iθ} applied to the x-axis, and det² U = e^{2iθ}. Turning the line through a half-turn brings it back to itself and carries e^{2iθ} once around the circle: the half-turn of a line is the generating loop [T].

The remaining directions of Λ(d) leave det² unchanged. The points with a given value of det² form a copy of SU(d)/SO(d) [T], and moving within such a set changes the polarization without moving around the circle. At d = 4 these are the directions that #1 calls "the nine non-Maslov directions" (§8), beside the one circle direction.

An angle measured around the Maslov circle is periodic because of this topology, whatever dynamics act on it. The program uses exactly this for the dark-energy field: [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase). #1 §2 tags that periodicity "[D]": "Periodicity is topology".

## Higher homotopy at d = 4

The closed-universe investigation computed the first three homotopy groups of Λ(4) = U(4)/O(4) (`notes/closed-universe.md` §8; flag 61 in `review/wiki-build-flags.md`):

```text
π₁(Λ(4)) = ℤ      [T][V]    the Maslov class
π₂(Λ(4)) = ℤ₂     [T]       by exactness
π₃(Λ(4)) = ℤ₂     [T][V]
```

They are Bott periodicity's stable values for U/O, the values the homotopy groups of U(d)/O(d) take when d is large [T]. Section F of `verify/closed_universe.py` derives them from the fibration O(4) → U(4) → U(4)/O(4) [T]. Its check F1 finds the image of π₃(SO(4)) in π₃(U(4)) = ℤ to be 2ℤ, by a winding-number integral anchored on two literature values, so π₃(Λ(4)) = ℤ₂; check F2 finds det² winding once on a loop that closes in Λ(4), so π₁(Λ(4)) = ℤ. π₂ follows by exactness from standard inputs, and check F3 "confirms an input rather than testing one". Check F4 matches the three groups to Bott periodicity's table ([the closed-universe script](/wiki/method/verification/closed-universe-script#f-topology-of-the-polarization-manifold-8-checks)).

In the classification of defects, π₁ allows strings, π₂ point defects of the monopole type and π₃ textures [T] ([the classification](/wiki/symmetry-breaking/topological-defects#the-classification-t)). On the light Maslov circle alone π₂ = π₃ = 0. Strings around which τ winds exist there too, but the point defects and the textures need the order parameter to range over the whole manifold (`notes/closed-universe.md` §8). On a closed universe, whose space is a 3-sphere, the classes of polarization texture are [S³, Λ(4)] = Z₂ [D], argued from π₃ and not computed (check F4; [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#light-horizons-and-counts)). All of this assumes d = 4 and that the U(4) acting on the polarization is global, the closed-universe verifiers' caveats. Whether a transition produced such defects is open problem 12 of #11 (§14 item 12; [Open: point defects of the polarization (OP12)](/wiki/symmetry-breaking/topological-defects#open-point-defects-of-the-polarization-op12)).

## The boundary of the Siegel domain

The Siegel domain of complex symmetric matrices Z = X + iY with Y > 0 can be mapped by the Cayley transform W = (Z − i)(Z + i)⁻¹ onto a bounded domain, the "Siegel disk" of complex symmetric W with 1 − W̄W positive definite [T]. A bounded domain has a distinguished part of its boundary, its Shilov boundary: the smallest closed part of the boundary on which every function holomorphic inside and continuous up to the edge reaches its largest absolute value [T]. For the unit disk (d = 1) it is the whole circle. For a product of two disks it is the torus of pairs of boundary points, smaller than the full boundary. For the Siegel disk it is the set of symmetric unitary matrices [T] (Hua 1963 †).

That set is Λ(d) [T]. Every symmetric unitary matrix can be written as W = UUᵀ with U unitary, and two unitary matrices give the same W exactly when they differ by an orthogonal factor on the right, so the symmetric unitary matrices are U(d)/O(d). On them det W = det(U)², so the Maslov map det² of the previous section is the determinant of the boundary point. In the original half-space picture the real symmetric matrices, the limit Y → 0, form a dense part of this boundary: one chart of Λ(d) whose points, like the graphs of the first section, are labelled by real symmetric matrices. The remaining Lagrangian subspaces are limits at infinity [T].

The program's statements are brief. Calc note #5: "**Λ(d) is the Shilov boundary of the Siegel domain** [standard]" (§C). #11 §6: "**Λ(d) is the Shilov boundary** of the Siegel domain [T]". Neither document gives a reference. The program reads the boundary as the place where the dark-energy field lives ([τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)).

## The space of vacuum polarizations

### Lost under strict P2, restored under P2′

Under the [original P2](/wiki/program/postulates/original-p2), which froze both ω and the neutral metric η, calc note #5 found: "The space of polarizations compatible with both structures (ω-Lagrangian *and* η-null) is **discrete** — the 2^d coordinate-type splittings, GL(d)-rigid. No Lagrangian Grassmannian, no Maslov circle, **no τ field**" (§B; on "discrete", see flag 1 in `review/wiki-build-flags.md`). This is part of the [nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) that forced the repair.

Under [P2′](/wiki/program/postulates/p2-prime), only ω is rigid, and "the vacuum spontaneously selects a real structure J (an involution anticommuting with I), and η ≡ HJ. The space of H-compatible real structures on (ℝ^{2d}, I) is {J} ≅ U(d)/O(d) = Λ(d), the Lagrangian Grassmannian — π₁ = ℤ, Maslov circle intact, τ restored" (#5 §B; #11 §4 writes P2′ with the same η = HJ). Here I = ω⁻¹H is the complex structure of [Born geometry](/wiki/phase-space/born-geometry/born-structures). The identification is standard [T]: such a J is fixed by its +1 eigenspace, which is a Lagrangian subspace, and every Lagrangian subspace arises this way. Choosing J is choosing which directions count as position, and the possible choices are the points of Λ(d). In the language of [spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking), Λ(d) is the vacuum manifold of the polarization.

A note on letters. This page follows #5 and #11's P2′ in calling the vacuum's real structure J, with η = HJ. The toy-model note calls it K, with η = ωK (§1), and so does #11 §14 item 11. No document reconciles the two namings; see [the order parameter](/wiki/symmetry-breaking/order-parameter) and [notation](/wiki/notation).

### Ten compact moduli

At d = 4 the polarization has ten directions in which to vary. Calc note #7 makes this the basis of [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric): "J carries only the 10 compact moduli of U(d)/O(d) — not a full second metric. So the 'second vielbein' E₀[J] is confined to a compact 10-dimensional moduli space" (§4). Calc note #5 counts the same ten as "Λ(d) σ-modes (10: τ plus nine, of which inverse-Higgs constraints likely eliminate most [O])" (§D; [inverse-Higgs constraints](/wiki/symmetry-breaking/inverse-higgs-constraints)); whether they survive is [open](/wiki/phase-space/modular-field/field-content). The lab notebook assumes that τ, the circle direction, is the light one: "that τ is the *lightest* modulus, with the other nine directions heavy, is assumed **[P]**" (#1 §2). Calc note #6 adds that none of the ten is absorbed when X acquires its mass: "The Λ(d) moduli, τ included, are not the eaten modes — they carry the compact phase directions, which constant shifts do not generate" (§3, a section tagged [D — structural], which flags the check for τ as [O]; [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten)).

### The toy model's Λ(1)

In the d = 1 coset model of the toy-model note, the vacua at H = 1 are the real structures K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]], a circle of them (§2). "The potential's Hessian has rank 1 at the vacuum. That leaves three Goldstone directions: the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)" (§2). The gate prints `PASS  potential Hessian has rank 1: three flat directions (Goldstones), one massive  [[0, 4, 0, 0]]` (`verify/toy_coset.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)). The worklog: "The compact Goldstone is the rotation of K at fixed H: the Lagrangian Grassmannian Λ(1), which is the checkpoint's Maslov circle (the τ field of §10)" ('Chunk 1 results'). #11 §10: "In the coset model that angle parametrizes Λ(1): it is τ's circle." See [model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua) and [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle). Because Λ(1) is a single circle, the toy has no counterpart of the nine other directions.

## Standard references

- V. P. Maslov, *Theory of Perturbations and Asymptotic Methods* (1965) † — the index that bears his name.
- V. I. Arnold, "Characteristic class entering in quantization conditions", Functional Analysis and Its Applications (1967) † — the Lagrangian Grassmannian as U(d)/O(d), its fundamental group ℤ and the det² description of the Maslov class.
- L. K. Hua, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains* (English translation 1963) † — the Shilov boundaries of the classical domains.

The program's documents cite none of these; they tag the facts [T] or "[standard]".

## Used by

- [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase) and [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — the dark-energy field is the angle around the Maslov circle.
- [The Siegel domain](/wiki/phase-space/modular-field/siegel-domain) — Λ(d) is its Shilov boundary.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — no Grassmannian in the rigid version, τ on its boundary in the free one.
- [The hard core: spontaneously broken Born reciprocity](/wiki/program/hard-core) and [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — the vacuum's real structure ranges over Λ(d) once only ω is rigid.
- [Original P2](/wiki/program/postulates/original-p2) and [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — under strict P2 the polarizations form what #5 calls a discrete set (see flag 1 in `review/wiki-build-flags.md`), with no Grassmannian and no τ.
- [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection) — the possible choices of polarization.
- [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) — the manifold of values the order parameter can take.
- [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua), [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) — Λ(1) as the toy's compact Goldstone direction.
- [Constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric), [Born's answer](/wiki/gravity/momentum-graviton/borns-answer) and [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) — the second frame confined to the compact Λ(4).
- [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten) and [Open: τ–Stückelberg mixing (OP6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing) — τ as a compact modulus, not a Stückelberg mode.
- [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content) — the fate of the nine non-Maslov directions.
- [Open: polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis) — the lab notebook's sketch, in which the nine heavy directions decay at reheating.
- [Open: one modular structure for both polarizations (OP8)](/wiki/electric-magnetic-duality/unified-modular-structure) — the space of phase-space polarizations in the conjectured structure.
- [Open: point defects of the polarization (OP12)](/wiki/symmetry-breaking/topological-defects#open-point-defects-of-the-polarization-op12) — π₂(Λ(4)) = ℤ₂ and the Maslov loop allow point defects and τ-strings, whose production is open.
- [A closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe) — two classes of polarization texture on S³, [S³, Λ(4)] = Z₂ [D].

## Sources

- `notes/broken-born-theory.md` §2 — definition, dimension and π₁ = ℤ, tagged [T]; τ the lightest modulus [P]; periodicity "is topology [D]".
- `papers/broken-born-checkpoint-v2.md` §6 — Λ(d) as the Shilov boundary [T].
- `papers/broken-born-checkpoint-v2.md` §4, §7, §10, §14 item 11 — P2′ with the real structure J; Λ(4) as the physical case; Λ(1) as τ's circle in the coset model; η = ωK in the toy-model item.
- `papers/broken-born-checkpoint-v2.md` §14 item 12 — the polarization's defects, π₁ = ℤ and π₂ = ℤ₂ [T] with the maps behind them gated, their production open [O].
- `notes/closed-universe.md` §8 — π₁, π₂ and π₃ of Λ(4) with their tags, the textures on S³ [D], and the light-circle caveat; `verify/closed_universe.py` section F — checks F1–F4; `review/wiki-build-flags.md` flag 61 — how the groups reached the record.
- `notes/geometric-core.md` §B–§D — the discrete polarizations under strict P2; {J} ≅ U(d)/O(d) = Λ(d) under P2′; the boundary fact "[standard]"; the ten σ-modes.
- `notes/tuning-test.md` §4 — the ten compact moduli carried by J.
- `notes/x-classification.md` §3 — the Λ(d) moduli are not the eaten modes.
- `notes/broken-born-theory.md` §8 — "the nine non-Maslov directions".
- `papers/reciprocity-toy-models.md` §1, §2 — Lagrangian null lines; Λ(1) in model I's Goldstone spectrum.
- `notes/toy-lagrangian.md` 'Chunk 1 results' — the compact Goldstone as the checkpoint's Maslov circle.
- `verify/toy_coset.py` — the rank-1 Hessian: three flat directions, one massive.
