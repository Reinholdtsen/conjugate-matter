---
title: "The Siegel domain Sp(2d, ℝ)/U(d)"
weight: 10
status: established
description: "Symmetric complex matrices Z = X + iY with positive-definite Y, moved by fractional-linear (Möbius) maps: the space of all positive phase-space metrics compatible with a fixed symplectic form, its H_Z parametrization, and battery test T2."
provenance: [D, V]
sources:
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §D"
  - "notes/tuning-test.md §2"
  - "notes/tuning-test.md §3"
  - "verify/battery.py T2"
  - "HANDOFF.md §5"
  - "HANDOFF.md §8"
  - "notes/x-classification.md §1"
  - "notes/x-classification.md §3"
  - "wiki/papers/broken-born-checkpoint-v2.md §2"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/reciprocity-toy-models.md §2"
  - "wiki/papers/reciprocity-toy-models.md §4"
  - "verify/toy_coset.py"
  - "review/round3/referee/audit-notes.md Step 3"
  - "notes/broken-born-theory.md §2"
---

*The Siegel domain is the space of complex symmetric d × d matrices Z = X + iY whose imaginary part Y is positive definite. For a single coordinate (d = 1) it is the upper half of the complex plane; for larger d it is the matrix version of that half-plane. Each point Z names exactly one positive phase-space metric H_Z that is compatible with a fixed [symplectic form](../reciprocity/symplectic-form.md) ω, and every such metric has a point, so the domain is the space of all of them. The symplectic group moves its points by fractional-linear (Möbius) maps, the matrix versions of z → (αz + β)/(γz + δ). The program uses the domain as the arena of [the modular field](modular-field-z.md) once only ω is held rigid. The space and its parametrization are standard mathematics, and battery test T2 checks the parametrization's identities at one sampled point.*

**Status:** Established — standard mathematics ([calc note #5](../../history/documents/field-equation-notes.md) heads its section "[D — structural; math facts standard]"); the parametrization identities are machine-checked [V] at one sampled point at d = 4 (battery test T2; [the verification battery](../../method/verification/battery.md)) and symbolically at d = 1 ([`verify/toy_coset.py`](../../../verify/toy_coset.py)).

## What the domain is

### The upper half-plane (d = 1)

With one coordinate the domain is the upper half-plane, the complex numbers z = x + iy with y > 0. The real 2 × 2 matrices of unit determinant, the group SL(2, ℝ), act on it by fractional-linear maps [T]:

```text
z → (α z + β) / (γ z + δ),        [[α, β], [γ, δ]] ∈ SL(2, ℝ)
```

Each such map sends the half-plane onto itself, and any point can be carried to any other. The maps that leave the point z = i fixed are the rotations [[cos θ, sin θ], [−sin θ, cos θ]], which form the circle group SO(2) ≅ U(1). The half-plane is therefore the coset space SL(2, ℝ)/SO(2): a point of the half-plane is a group element up to a rotation [T]. In two dimensions SL(2, ℝ) is the same group as Sp(2, ℝ), the linear maps of the (x, p) plane that preserve the area form ω.

### The matrix version (general d)

For d coordinates, z becomes a complex symmetric d × d matrix Z = X + iY, with X and Y real symmetric and Y positive definite (Y > 0). This is Siegel's upper half-space [T] (Siegel 1943 †). A symplectic matrix written in d × d blocks, S = [[A, B], [C, D]], acts by the matrix form of the same map:

```text
Z → (A Z + B)(C Z + D)⁻¹
```

Sp(2d, ℝ) reaches every point, and the elements that fix the base point Z = i·1 (i times the unit matrix) form the unitary group U(d), sitting inside Sp(2d, ℝ) as the symplectic maps that are also rotations. Hence the name Sp(2d, ℝ)/U(d) [T]. X and Y each have d(d + 1)/2 independent entries, ten each at d = 4, the counts calc note [#5](../../../notes/geometric-core.md) gives for the metric and for X ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)).

Two kinds of map recur in the program's documents:

- the translations [[1, B], [0, 1]], with B real symmetric, act as Z → Z + B: they shift X and leave Y alone ([#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous));
- the quarter-turn [[0, 1], [−1, 0]] acts as Z → −Z⁻¹, which is how [Born reciprocity](../reciprocity/born-reciprocity.md) acts on the modular field ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard); [#11](../../history/documents/checkpoint.md) [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field); [modular inversion](modular-inversion.md)).

Together with the linear changes Z → AZAᵀ (A invertible), these two kinds generate the whole action [T]. One convention needs care [T]: the [toy-model note](../../symmetry-breaking/toy-models/_index.md) lets a symplectic S act on a metric by congruence, H → SᵀHS ([§2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)), and in that convention the map induced on Z is the fractional-linear map of Sᵀ, so Z → Z + B comes from [[1, 0], [B, 1]]. For ρ the two readings agree, because ρᵀ = −ρ and S and −S induce the same map.

### The domain as a space of phase-space metrics

The program meets the domain from the other side, as a space of metrics. The symplectic form is fixed as ω = [[0, 1], [−1, 0]] in d × d blocks, in the (x, p) basis of the [lab notebook](../../history/documents/lab-notebook.md), [#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core). A positive symmetric matrix H on phase space is compatible with ω when I = ω⁻¹H squares to −1, so that I is a complex structure (see [the structures ω, η, H](../born-geometry/born-structures.md)). For a symmetric H this is the same as H itself being a symplectic matrix [T]; [model I](../../symmetry-breaking/toy-models/coset-model/_index.md) of the toy-model note takes H to be "a positive symmetric symplectic matrix" with I² = −1 ([§2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)). Calc note #5: "positive H compatible with ω alone form the **Siegel domain** Sp(2d,ℝ)/U(d), coordinatized by a complex symmetric matrix" ([§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)):

```text
Z = X + iY,   Y > 0

H_Z = [[ Y + XY⁻¹X ,  XY⁻¹ ],
       [ Y⁻¹X      ,  Y⁻¹  ]]
```

[#11](../../papers/broken-born-checkpoint-v2.md) calls H_Z "the standard generalized metric" ([§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)). Its complex structure, in what calc note [#7](../../../notes/tuning-test.md) calls "the verified Siegel parametrization" ([§2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous)), is

```text
I[Z] = ω⁻¹ H_Z = [[ −Y⁻¹X     ,  −Y⁻¹  ],
                  [ Y + XY⁻¹X ,  XY⁻¹  ]]
```

The upper-left block of H_Z measures position directions, the lower-right block measures momentum directions, and the off-diagonal blocks XY⁻¹ and Y⁻¹X couple the two. At X = 0 the coupling vanishes and H = diag(Y, Y⁻¹): position metric Y, momentum metric Y⁻¹. That is exactly the form diag(g, g⁻¹) which [the compatibility theorem](../born-geometry/compatibility-theorem.md) allows when the [neutral metric η](../born-geometry/born-structures.md) is held rigid as well. A point with X ≠ 0 is compatible with ω but mixes the position and momentum directions.

### Why the identities hold [T]

A standard factorization shows at once why H_Z has the properties the battery tests:

```text
H_Z = Lᵀ · diag(Y, Y⁻¹) · L,        L = [[ 1 , 0 ],
                                          [ X , 1 ]]
```

Both L and diag(Y, Y⁻¹) are symplectic, so H_Z is symplectic and I[Z]² = −1. diag(Y, Y⁻¹) is positive definite because Y is, so H_Z is positive definite. And det H_Z = det Y · det Y⁻¹ = 1. Taking square roots of the diagonal factor writes H_Z = EᵀE with E symplectic, which is one choice of what calc note #7 calls "the symplectic vielbein E, the coset representative with H = EᵀE" ([§3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t)). The factorization is textbook algebra; the program's documents do not use it.

## How the program uses it

### The arena of the modular field

Under the corrected postulate [P2′](../../program/postulates/p2-prime.md), only ω is rigid. The metric H may then be any ω-compatible positive metric, that is, any point of the Siegel domain, and its coordinates X and Y become fields on spacetime. [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field): "With only ω rigid, H ranges over Sp(2d,ℝ)/U(d): Z = X + iY (symmetric; Y > 0), H_Z the standard generalized metric (I[Z]² = −1 machine-verified [V])." The physical readings, Im Z = g the metric and Re Z = X the [momentum graviton](../../gravity/momentum-graviton/_index.md), are the program's claims and are set out on [the modular field Z = X + iY](modular-field-z.md). Under the [original P2](../../program/postulates/original-p2.md), with η rigid too, only the slice X = 0 would remain.

### Its symmetries as field symmetries

- **Translations.** "The Möbius action of the rigid Sp(2d,ℝ) contains the subgroup [[1, B], [0, 1]], B symmetric, acting as Z → Z + B: X → X + B, Y → Y" ([#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous), a section tagged [D — rigorous]). Constant shifts of X are therefore exact symmetries of any action built from (ω, H): X is "axion-like", never auxiliary ([shift symmetry](../../gravity/momentum-graviton/shift-symmetry.md)).
- **Inversion.** Reciprocity acts as Z → −Z⁻¹ with fixed point Z = i ([modular inversion](modular-inversion.md)).

### The target metric

A field with values in the domain needs a kinetic term, and the natural one comes from the domain's invariant metric [T] (Siegel 1943 †):

```text
ds² = Tr( Y⁻¹ dZ  Y⁻¹ dZ̄ )
```

It is unchanged by every map of the Sp(2d, ℝ) action [T]. For d = 1 it is the hyperbolic metric (dx² + dy²)/y² of the upper half-plane. Calc note #5 counts its positivity among the good signs for a healthy kinetic term: "the Siegel target metric Tr(Y⁻¹dZ Y⁻¹dZ̄) is positive-definite" ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial); see [the field content of the broken vacuum](field-content.md)). That positivity belongs to positive (Euclidean) H. With a Lorentzian metric, calc note #6 records "the stabilizer U(1, d−1) and the invariant target metric indefinite" ([§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)); the extension to spacetime signature is open item 3 ([Open: Lorentzian dressing](../born-geometry/lorentzian-dressing.md)).

### The toy model's H-sector (d = 1)

Model I of the toy-model note takes "H, a positive symmetric symplectic matrix, H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]] for Z = X + iY in the upper half-plane, with I ≡ ω⁻¹H, I² = −1" ([§2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k)): the d = 1 case of H_Z. [`verify/toy_coset.py`](../../../verify/toy_coset.py) checks the d = 1 parametrization symbolically, for symbolic X and Y ([the toy-model scripts](../../method/verification/toy-model-scripts.md)): `PASS  H(Z) is symplectic and I = w^-1 H squares to -1`. The model's [vacuum manifold](../../symmetry-breaking/topological-defects.md#the-vacuum-manifold-t) is "the upper half-plane times this circle" of real structures, and the two half-plane directions are two of its three [Goldstone directions](../../symmetry-breaking/goldstone-and-higgs.md) (§2). The half-plane sector is non-compact: "The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur" (§4; [coset and hyperbolic sigma models](../../symmetry-breaking/toy-models/coset-model/sigma-models.md); [model I: action and symmetries](../../symmetry-breaking/toy-models/coset-model/action-and-symmetries.md)). [The handoff](../../history/documents/handoff.md)'s queue had proposed starting the toy "on the Siegel disk", the bounded form of the domain described next ([`HANDOFF.md` §8 item 4](../../../HANDOFF.md#8-ranked-next-actions-queue)).

## The boundary of the domain

The domain is unbounded, but the Cayley transform W = (Z − i)(Z + i)⁻¹ maps it onto a bounded domain, the "Siegel disk" of complex symmetric matrices W with 1 − W̄W positive definite; the point Z = i goes to the center W = 0 [T]. For d = 1 this is the familiar map of the upper half-plane onto the unit disk.

A bounded domain has a distinguished part of its boundary, its Shilov boundary: the smallest closed part of the boundary on which every function that is holomorphic inside and continuous up to the edge reaches its largest absolute value [T]. For the Siegel disk it is the set of symmetric unitary matrices, which is the [Lagrangian Grassmannian](lagrangian-grassmannian.md) Λ(d) [T] (Hua 1963 †; the construction is on [that page](lagrangian-grassmannian.md#the-boundary-of-the-siegel-domain)). [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field): "**Λ(d) is the Shilov boundary** of the Siegel domain [T]". In the upper-half-space picture the real symmetric matrices, the limit Y → 0, make up a dense part of that boundary [T]. The program places the dark-energy field there ([τ as the Maslov phase of the boundary](maslov-phase.md)).

## Battery test T2

**What it computes.** [`verify/battery.py`](../../../verify/battery.py), the battery of [`HANDOFF.md` Appendix A](../../../HANDOFF.md#appendix-a--machine-verification-battery-re-run-first), works at d = 4 with numpy's random seed 0. It draws one random symmetric X and one positive-definite Y, builds H_Z and I[Z] = ω⁻¹H_Z, and checks four properties. The gate prints:

```text
PASS  T2 I[Z]^2 = -1
PASS  T2 H_Z symmetric
PASS  T2 det H_Z = 1  [det=1.000000000000]
PASS  T2 H_Z positive definite
```

[`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it) describes the test as "T2 Siegel parametrization (I[Z]² = −1, H ≻ 0, det H = 1 off-vacuum)": the sampled point has X ≠ 0, away from the vacuum slice.

**What it shows, and what it does not.**

- It checks one sampled member of the family. [#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) describes the battery as covering "the Siegel parametrization (I[Z]² = −1, H > 0, det H = 1 across the whole family)", and [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) says det H = 1 "machine-verified — persists across the whole modular family of §6". That the identities hold for every Z is the algebra above ([T]; [D] in the program's tagging), not a machine result. The symbolic check in [`verify/toy_coset.py`](../../../verify/toy_coset.py) holds for all X and Y at once, but only at d = 1.
- It confirms a matrix identity, not the program's reading of Y as the spacetime metric ([verification confirms arithmetic, not the model](../../method/verification/arithmetic-not-model.md)).

**Round 3's independent check.** The [round-3](../../method/review/round-3/_index.md) blind audit re-derived the compatibility theorem with its own code and tested an "omega-only family (Siegel, X != 0)" in 2000 random trials at each of d = 3 and d = 4: "omega residual <= 3e-14 but eta residual >= 0.52 (d=3), 1.87 (d=4)" ([`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 3). Every sampled member is compatible with ω to rounding error, and every one misses compatibility with η by a finite margin. The Siegel family is strictly larger than the compatibility theorem's solution set, which is its X = 0 slice ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)). The audit's scripts sit in [`review/round3/referee/`](../../../review/round3/referee/) and are not part of [the gate](../../method/verification/the-gate.md).

## Standard references

- C. L. Siegel, "Symplectic geometry", American Journal of Mathematics (1943) † — the upper half-space, the symplectic group's action on it and its invariant metric.
- L. K. Hua, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains* (English translation 1963) † — the bounded realizations of these domains and their Shilov boundaries.

The program's documents cite no reference for these facts: #5 marks them "[standard]", and #11 tags the boundary statement [T].

## Used by

- [P1: the phase-space arena](../../program/postulates/p1-arena.md) and [P2′: only the symplectic form is rigid](../../program/postulates/p2-prime.md) — with only ω fixed, H ranges over the Siegel domain.
- [P3: a reciprocity-invariant action](../../program/postulates/p3-reciprocity.md) — ρ acts on the domain by modular inversion.
- [The nontriviality theorem](../../program/postulates/nontriviality-theorem.md) — under P2′ the metric opens up into the domain.
- [The modular field Z = X + iY](modular-field-z.md) — the program's field takes values in this space.
- [Reciprocity as modular inversion Z → −Z⁻¹](modular-inversion.md) — ρ as a Möbius map.
- [The Lagrangian Grassmannian Λ(d)](lagrangian-grassmannian.md) and [τ as the Maslov phase of the boundary](maslov-phase.md) — the domain's Shilov boundary and the field placed on it.
- [Corollaries: unimodularity, no B-field, slaved momentum metric](../born-geometry/compatibility-corollaries.md) — det H = 1 and its persistence across the family.
- [Open: field content of the broken vacuum](field-content.md) — the positive target metric as a sign of health.
- [Open: Lorentzian dressing (OP3)](../born-geometry/lorentzian-dressing.md) — the indefinite target metric at Lorentzian signature.
- [Shift symmetry: X is never auxiliary](../../gravity/momentum-graviton/shift-symmetry.md) — the translations Z → Z + B.
- [Why X must be massive](../../gravity/momentum-graviton/forcing-chain.md) and [the symplectic partner of the graviton](../../gravity/momentum-graviton/symplectic-partner.md) — X and g as the two halves of H_Z.
- [τ is not eaten](../../gravity/momentum-graviton/tau-not-eaten.md) — the absorbed modes move X through the non-compact domain, τ through the compact Λ(d).
- [The misalignment potential](../../gravity/tuning-test/misalignment-potential.md) — built from I[Z] (battery test T3).
- [The frame tier](../../gravity/tuning-test/frame-tier.md) — the symplectic vielbein E with H = EᵀE.
- [Constrained bimetric gravity](../../gravity/tuning-test/constrained-bimetric.md) — couplings dictated by modular (Siegel-domain) symmetry.
- [The cosmological constraint a·ã = 1](../../cosmology/scale-factor-duality/cosmological-constraint.md) — the |Z| = 1 locus in the domain, identified with a·ã = 1 (see flag 23 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).
- [Model I: action and symmetries](../../symmetry-breaking/toy-models/coset-model/action-and-symmetries.md) — the d = 1 domain as the toy's H-sector.
- [Model I vacua](../../symmetry-breaking/toy-models/coset-model/vacua.md), [the frozen-H reduction](../../symmetry-breaking/toy-models/coset-model/frozen-h-reduction.md) and [Open: does ρ's SO(2) break in the coupled model?](../../symmetry-breaking/toy-models/coset-model/so2-question.md) — the upper half-plane as the toy's space of metrics, with Z = i fixed by ρ.
- [Open: one modular structure for both polarizations (OP8)](../../electric-magnetic-duality/unified-modular-structure.md) — the phase-space side of the conjectured structure.

## Sources

- [`notes/geometric-core.md` §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — the Siegel domain of ω-compatible metrics and H_Z; "[D — structural; math facts standard]"; the boundary fact "[standard]".
- [`notes/geometric-core.md` §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) — the positive Siegel target metric.
- [`notes/tuning-test.md` §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous), [§3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — I[Z] in "the verified Siegel parametrization"; the symplectic vielbein H = EᵀE.
- [`verify/battery.py`](../../../verify/battery.py) T2 — the four identities at one sampled point (d = 4, seed 0).
- [`HANDOFF.md` §5](../../../HANDOFF.md#5-verification-protocol-the-method--keep-using-it), [§8](../../../HANDOFF.md#8-ranked-next-actions-queue) — T2 described as an off-vacuum check; the toy queued "on the Siegel disk".
- [`notes/x-classification.md` §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous), [§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — the translations Z → Z + B; the Lorentzian stabilizer U(1, d−1) and the indefinite target metric.
- [`wiki/papers/broken-born-checkpoint-v2.md` §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — "the standard generalized metric"; Λ(d) as the Shilov boundary [T].
- [`wiki/papers/broken-born-checkpoint-v2.md` §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification), [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) — the battery's description of T2; det H = 1 "across the whole modular family".
- [`wiki/papers/reciprocity-toy-models.md` §2](../../papers/reciprocity-toy-models.md#2-model-i-a-coset-sigma-model-of-h-k), [§4](../../papers/reciprocity-toy-models.md#4-quantum-stability) — the d = 1 case in model I; the hyperbolic half-plane sector.
- [`verify/toy_coset.py`](../../../verify/toy_coset.py) — the symbolic d = 1 anchor "H(Z) is symplectic and I = w^-1 H squares to -1".
- [`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 3 — the ω-only family, checked by independent code.
- [`notes/broken-born-theory.md` §2](../../../notes/broken-born-theory.md#2-kinematic-core) — the (x, p) block basis in which ω is fixed.
