---
title: "The Siegel domain Sp(2d, ℝ)/U(d)"
weight: 10
status: established
description: "Symmetric complex matrices Z = X + iY with positive-definite Y, moved by fractional-linear (Möbius) maps: the space of all positive phase-space metrics compatible with a fixed symplectic form, its H_Z parametrization, and battery test T2."
provenance: [D, V]
sources:
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "verify/battery.py T2"
  - "HANDOFF.md §5"
  - "HANDOFF.md §8"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "verify/toy_coset.py"
  - "review/round3/referee/audit-notes.md Step 3"
---

*The Siegel domain is the space of complex symmetric d × d matrices Z = X + iY whose imaginary part Y is positive definite. For a single coordinate (d = 1) it is the upper half of the complex plane; for larger d it is the matrix version of that half-plane. Each point Z names exactly one positive phase-space metric H_Z that is compatible with a fixed [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, and every such metric has a point, so the domain is the space of all of them. The symplectic group moves its points by fractional-linear (Möbius) maps, the matrix versions of z → (αz + β)/(γz + δ). The program uses the domain as the arena of [the modular field](/wiki/phase-space/modular-field/modular-field-z) once only ω is held rigid. The space and its parametrization are standard mathematics, and battery test T2 checks the parametrization's identities at one sampled point.*

**Status:** Established — standard mathematics (calc note #5 heads its section "[D — structural; math facts standard]"); the parametrization identities are machine-checked [V] at one sampled point at d = 4 (battery test T2; [the verification battery](/wiki/method/verification/battery)) and symbolically at d = 1 (`verify/toy_coset.py`).

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

Sp(2d, ℝ) reaches every point, and the elements that fix the base point Z = i·1 (i times the unit matrix) form the unitary group U(d), sitting inside Sp(2d, ℝ) as the symplectic maps that are also rotations. Hence the name Sp(2d, ℝ)/U(d) [T]. X and Y each have d(d + 1)/2 independent entries, ten each at d = 4, the counts calc note #5 gives for the metric and for X (§D).

Two kinds of map recur in the program's documents:

- the translations [[1, B], [0, 1]], with B real symmetric, act as Z → Z + B: they shift X and leave Y alone (#6 §1);
- the quarter-turn [[0, 1], [−1, 0]] acts as Z → −Z⁻¹, which is how [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) acts on the modular field (#5 §C; #11 §6; [modular inversion](/wiki/phase-space/modular-field/modular-inversion)).

Together with the linear changes Z → AZAᵀ (A invertible), these two kinds generate the whole action [T]. One convention needs care [T]: the toy-model note lets a symplectic S act on a metric by congruence, H → SᵀHS (§2), and in that convention the map induced on Z is the fractional-linear map of Sᵀ, so Z → Z + B comes from [[1, 0], [B, 1]]. For ρ the two readings agree, because ρᵀ = −ρ and S and −S induce the same map.

### The domain as a space of phase-space metrics

The program meets the domain from the other side, as a space of metrics. The symplectic form is fixed as ω = [[0, 1], [−1, 0]] in d × d blocks, in the (x, p) basis of #1 §2. A positive symmetric matrix H on phase space is compatible with ω when I = ω⁻¹H squares to −1, so that I is a complex structure (see [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). For a symmetric H this is the same as H itself being a symplectic matrix [T]; model I of the toy-model note takes H to be "a positive symmetric symplectic matrix" with I² = −1 (§2). Calc note #5: "positive H compatible with ω alone form the **Siegel domain** Sp(2d,ℝ)/U(d), coordinatized by a complex symmetric matrix" (§C):

```text
Z = X + iY,   Y > 0

H_Z = [[ Y + XY⁻¹X ,  XY⁻¹ ],
       [ Y⁻¹X      ,  Y⁻¹  ]]
```

#11 calls H_Z "the standard generalized metric" (§6). Its complex structure, in what calc note #7 calls "the verified Siegel parametrization" (§2), is

```text
I[Z] = ω⁻¹ H_Z = [[ −Y⁻¹X     ,  −Y⁻¹  ],
                  [ Y + XY⁻¹X ,  XY⁻¹  ]]
```

The upper-left block of H_Z measures position directions, the lower-right block measures momentum directions, and the off-diagonal blocks XY⁻¹ and Y⁻¹X couple the two. At X = 0 the coupling vanishes and H = diag(Y, Y⁻¹): position metric Y, momentum metric Y⁻¹. That is exactly the form diag(g, g⁻¹) which [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) allows when the [neutral metric η](/wiki/phase-space/born-geometry/born-structures) is held rigid as well. A point with X ≠ 0 is compatible with ω but mixes the position and momentum directions.

### Why the identities hold [T]

A standard factorization shows at once why H_Z has the properties the battery tests:

```text
H_Z = Lᵀ · diag(Y, Y⁻¹) · L,        L = [[ 1 , 0 ],
                                          [ X , 1 ]]
```

Both L and diag(Y, Y⁻¹) are symplectic, so H_Z is symplectic and I[Z]² = −1. diag(Y, Y⁻¹) is positive definite because Y is, so H_Z is positive definite. And det H_Z = det Y · det Y⁻¹ = 1. Taking square roots of the diagonal factor writes H_Z = EᵀE with E symplectic, which is one choice of what calc note #7 calls "the symplectic vielbein E, the coset representative with H = EᵀE" (§3). The factorization is textbook algebra; the program's documents do not use it.

## How the program uses it

### The arena of the modular field

Under the corrected postulate [P2′](/wiki/program/postulates/p2-prime), only ω is rigid. The metric H may then be any ω-compatible positive metric, that is, any point of the Siegel domain, and its coordinates X and Y become fields on spacetime. #11 §6: "With only ω rigid, H ranges over Sp(2d,ℝ)/U(d): Z = X + iY (symmetric; Y > 0), H_Z the standard generalized metric (I[Z]² = −1 machine-verified [V])." The physical readings, Im Z = g the metric and Re Z = X the momentum graviton, are the program's claims and are set out on [the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z). Under the [original P2](/wiki/program/postulates/original-p2), with η rigid too, only the slice X = 0 would remain.

### Its symmetries as field symmetries

- **Translations.** "The Möbius action of the rigid Sp(2d,ℝ) contains the subgroup [[1, B], [0, 1]], B symmetric, acting as Z → Z + B: X → X + B, Y → Y" (#6 §1, a section tagged [D — rigorous]). Constant shifts of X are therefore exact symmetries of any action built from (ω, H): X is "axion-like", never auxiliary ([shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)).
- **Inversion.** Reciprocity acts as Z → −Z⁻¹ with fixed point Z = i ([modular inversion](/wiki/phase-space/modular-field/modular-inversion)).

### The target metric

A field with values in the domain needs a kinetic term, and the natural one comes from the domain's invariant metric [T] (Siegel 1943 †):

```text
ds² = Tr( Y⁻¹ dZ  Y⁻¹ dZ̄ )
```

It is unchanged by every map of the Sp(2d, ℝ) action [T]. For d = 1 it is the hyperbolic metric (dx² + dy²)/y² of the upper half-plane. Calc note #5 counts its positivity among the good signs for a healthy kinetic term: "the Siegel target metric Tr(Y⁻¹dZ Y⁻¹dZ̄) is positive-definite" (§D; see [the field content of the broken vacuum](/wiki/phase-space/modular-field/field-content)). That positivity belongs to positive (Euclidean) H. With a Lorentzian metric, calc note #6 records "the stabilizer U(1, d−1) and the invariant target metric indefinite" (§3); the extension to spacetime signature is open item 3 ([Open: Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing)).

### The toy model's H-sector (d = 1)

Model I of the toy-model note takes "H, a positive symmetric symplectic matrix, H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]] for Z = X + iY in the upper half-plane, with I ≡ ω⁻¹H, I² = −1" (§2): the d = 1 case of H_Z. `verify/toy_coset.py` checks the d = 1 parametrization symbolically, for symbolic X and Y: `PASS  H(Z) is symplectic and I = w^-1 H squares to -1`. The model's vacuum manifold is "the upper half-plane times this circle" of real structures, and the two half-plane directions are two of its three [Goldstone directions](/wiki/symmetry-breaking/goldstone-and-higgs) (§2). The half-plane sector is non-compact: "The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur" (§4; [coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models); [model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)). The handoff's queue had proposed starting the toy "on the Siegel disk", the bounded form of the domain described next (`HANDOFF.md` §8 item 4).

## The boundary of the domain

The domain is unbounded, but the Cayley transform W = (Z − i)(Z + i)⁻¹ maps it onto a bounded domain, the "Siegel disk" of complex symmetric matrices W with 1 − W̄W positive definite; the point Z = i goes to the center W = 0 [T]. For d = 1 this is the familiar map of the upper half-plane onto the unit disk.

A bounded domain has a distinguished part of its boundary, its Shilov boundary: the smallest closed part of the boundary on which every function that is holomorphic inside and continuous up to the edge reaches its largest absolute value [T]. For the Siegel disk it is the set of symmetric unitary matrices, which is the [Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) Λ(d) [T] (Hua 1963 †; the construction is on [that page](/wiki/phase-space/modular-field/lagrangian-grassmannian#the-boundary-of-the-siegel-domain)). #11 §6: "**Λ(d) is the Shilov boundary** of the Siegel domain [T]". In the upper-half-space picture the real symmetric matrices, the limit Y → 0, make up a dense part of that boundary [T]. The program places the dark-energy field there ([τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase)).

## Battery test T2

**What it computes.** `verify/battery.py`, the battery of `HANDOFF.md` Appendix A, works at d = 4 with numpy's random seed 0. It draws one random symmetric X and one positive-definite Y, builds H_Z and I[Z] = ω⁻¹H_Z, and checks four properties. The gate prints:

```text
PASS  T2 I[Z]^2 = -1
PASS  T2 H_Z symmetric
PASS  T2 det H_Z = 1  [det=1.000000000000]
PASS  T2 H_Z positive definite
```

`HANDOFF.md` §5 describes the test as "T2 Siegel parametrization (I[Z]² = −1, H ≻ 0, det H = 1 off-vacuum)": the sampled point has X ≠ 0, away from the vacuum slice.

**What it shows, and what it does not.**

- It checks one sampled member of the family. #11 §2 describes the battery as covering "the Siegel parametrization (I[Z]² = −1, H > 0, det H = 1 across the whole family)", and #11 §5 says det H = 1 "machine-verified — persists across the whole modular family of §6". That the identities hold for every Z is the algebra above ([T]; [D] in the program's tagging), not a machine result. The symbolic check in `verify/toy_coset.py` holds for all X and Y at once, but only at d = 1.
- It confirms a matrix identity, not the program's reading of Y as the spacetime metric ([verification confirms arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

**Round 3's independent check.** The round-3 blind audit re-derived the compatibility theorem with its own code and tested an "omega-only family (Siegel, X != 0)" in 2000 random trials at each of d = 3 and d = 4: "omega residual <= 3e-14 but eta residual >= 0.52 (d=3), 1.87 (d=4)" (`review/round3/referee/audit-notes.md` Step 3). Every sampled member is compatible with ω to rounding error, and every one misses compatibility with η by a finite margin. The Siegel family is strictly larger than the compatibility theorem's solution set, which is its X = 0 slice (#5 §C). The audit's scripts sit in `review/round3/referee/` and are not part of the gate.

## Used by

- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — the program's field takes values in this space.
- [Reciprocity as modular inversion Z → −Z⁻¹](/wiki/phase-space/modular-field/modular-inversion) — ρ as a Möbius map.
- [The Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian) and [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase) — the domain's Shilov boundary and the field placed on it.
- [Shift symmetry: X is never auxiliary](/wiki/gravity/momentum-graviton/shift-symmetry) — the translations Z → Z + B.
- [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential) — built from I[Z] (battery test T3).
- [The frame tier](/wiki/gravity/tuning-test/frame-tier) — the symplectic vielbein E with H = EᵀE.
- [Corollaries: unimodularity, no B-field, slaved momentum metric](/wiki/phase-space/born-geometry/compatibility-corollaries) — det H = 1 and its persistence across the family.
- [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries) — the d = 1 domain as the toy's H-sector.
- [Open: Lorentzian dressing (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing) — the indefinite target metric at Lorentzian signature.

## Standard references

- C. L. Siegel, "Symplectic geometry", American Journal of Mathematics (1943) † — the upper half-space, the symplectic group's action on it and its invariant metric.
- L. K. Hua, *Harmonic Analysis of Functions of Several Complex Variables in the Classical Domains* (English translation 1963) † — the bounded realizations of these domains and their Shilov boundaries.

The program's documents cite no reference for these facts: #5 marks them "[standard]", and #11 tags the boundary statement [T].

## Sources

- `notes/debt1a-geometric-core.md` §C — the Siegel domain of ω-compatible metrics and H_Z; "[D — structural; math facts standard]"; the boundary fact "[standard]".
- `notes/debt1a-geometric-core.md` §D — the positive Siegel target metric.
- `notes/debt1a-iii-tuning-test.md` §2, §3 — I[Z] in "the verified Siegel parametrization"; the symplectic vielbein H = EᵀE.
- `verify/battery.py` T2 — the four identities at one sampled point (d = 4, seed 0).
- `HANDOFF.md` §5, §8 — T2 described as an off-vacuum check; the toy queued "on the Siegel disk".
- `notes/debt1a-ii-X-classification.md` §1, §3 — the translations Z → Z + B; the Lorentzian stabilizer U(1, d−1) and the indefinite target metric.
- `papers/broken-born-checkpoint-v2.md` §6 — "the standard generalized metric"; Λ(d) as the Shilov boundary [T].
- `papers/broken-born-checkpoint-v2.md` §2, §5 — the battery's description of T2; det H = 1 "across the whole modular family".
- `papers/reciprocity-toy-models.md` §2, §4 — the d = 1 case in model I; the hyperbolic half-plane sector.
- `verify/toy_coset.py` — the symbolic d = 1 anchor "H(Z) is symplectic and I = w^-1 H squares to -1".
- `review/round3/referee/audit-notes.md` Step 3 — the ω-only family, checked by independent code.
