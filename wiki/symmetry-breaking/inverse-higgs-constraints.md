---
title: "Inverse-Higgs constraints"
weight: 25
status: established
description: "When spacetime symmetries break, some would-be Goldstone fields are fixed as derivatives of others and drop out, leaving fewer Goldstone modes than broken generators: the count by local transformations, the membrane, the commutator criterion, the dilaton, removed fields that are redundant or massive — and calc note #5's expectation, never worked out, that such constraints remove most of the nine non-Maslov moduli of Λ(d)."
provenance: [T]
sources:
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §8"
  - "notes/debt1a-ii-X-classification.md §3"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "HANDOFF.md §2"
---

*An inverse-Higgs constraint is a relation that fixes one would-be [Goldstone field](/wiki/symmetry-breaking/goldstone-and-higgs) as a derivative of another, so that the first drops out of the theory as an independent field. Such relations arise when the symmetries broken by the ground state act on space and time themselves, as translations, rotations and boosts do. A flat membrane is the standard example. It breaks the translation perpendicular to itself and the rotations that would tilt it, but its local tilt is set by the slope of its local displacement, so the displacement is its only massless field. In a relativistic theory each broken generator of an internal symmetry brings its own massless Goldstone mode; when spacetime symmetries break, there can be fewer modes than broken generators. The program's record mentions the idea in a single document: [calc note #5](/wiki/history/documents/debt-1-notes) expects such constraints to remove most of the nine directions, besides that of the dark-energy field [τ](/wiki/phase-space/modular-field/maslov-phase), in which the vacuum's [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations) can vary. No document works this out, and the question is [open](/wiki/phase-space/modular-field/field-content).*

**Status:** Established — [T] — textbook field theory, explained here from general knowledge, with the literature it names marked † (Ivanov and Ogievetsky 1975 †; Low and Manohar 2002 †); no `verify/` script checks it. The program's only use is an expectation in calc note #5 §D, tagged [O] and never worked out ([Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content)).

## Goldstone counting [T]

### One mode per broken generator

[Goldstone's theorem](/wiki/symmetry-breaking/goldstone-and-higgs#goldstones-theorem) counts massless modes by counting broken generators, the independent directions in which the transformations of a symmetry group can move the vacuum. When a continuous group G is broken to a subgroup G₀, the ground states form the vacuum manifold G/G₀, with one flat direction for each generator outside G₀ ([the vacuum manifold](/wiki/symmetry-breaking/topological-defects#the-vacuum-manifold-t)). A Goldstone mode is a slow wave along such a direction: a broken symmetry transformation whose size varies gently from place to place, applied to the vacuum. An internal symmetry acts on the fields at each point and leaves the points themselves where they are. For such a symmetry, different broken generators produce different waves, and a relativistic theory has one massless mode for each broken generator [T].

### Spacetime symmetries

A symmetry that moves the points of space and time behaves differently [T]. A rotation about the origin displaces each point by an amount that grows with the point's distance from the origin, so in any small region it acts like a translation whose size depends on where the region is. Made local, a broken rotation can then produce the same deformation of the vacuum as a broken translation of suitably varying size. Two generators whose local transformations produce the same deformations describe one mode, not two. Low and Manohar (2002 †) stated the count in this form: the independent Goldstone modes correspond to the independent deformations that local broken transformations produce, and for spacetime symmetries there can be fewer of these than broken generators.

An inverse-Higgs constraint is the same reduction written as an equation between fields. It expresses the would-be Goldstone field of one broken generator through derivatives of the Goldstone field of another, so that only the second remains an independent field (Ivanov and Ogievetsky 1975 †).

A crystal shows the reduction in condensed matter. It breaks translations and rotations, and its massless modes are its sound waves, the acoustic phonons, one branch for each broken translation; the broken rotations add none [T].

### A different reduction

A ferromagnet also has fewer massless modes than broken generators, for another reason [T]. Its ground state breaks the internal rotations of its spins about the two axes perpendicular to the magnetization, and it has a single spin-wave mode. The commutator of the two broken generators is the total spin along the magnetization, which is nonzero in the ground state, so the two act as one conjugate pair, like a position and its momentum, rather than as two independent modes. That reduction occurs only without Lorentz invariance, involves no broken spacetime symmetry, and is not an inverse-Higgs constraint.

## The membrane [T]

The example is a flat membrane lying in the plane y = 0 of three-dimensional space, such as a [domain wall](/wiki/symmetry-breaking/topological-defects#the-classification-t), the surface where two regions in different ground states meet. The laws are taken to be relativistic, with the speed of light set to 1. They are invariant under every translation, rotation and boost; the membrane is not:

```text
unbroken   translations along x and z, and in time
           the rotation about y, the membrane's normal
           boosts along x and z
broken     the translation along y
           the rotations about x and about z, which tilt the membrane
           the boost along y, which sets the membrane moving
```

Each broken transformation carries the membrane to another solution of the same equations, and each result is a displacement in y:

```text
membrane at rest                          y = 0
translated by a                           y = a
rotated about z by a small angle θ        y = θ·x
boosted along y to a small velocity v     y = v·t
general slow deformation                  y = π(t, x, z)
```

A tilt is a displacement that grows along the membrane, and a uniform motion is one that grows in time. A rotation or boost whose size varies slowly from place to place therefore produces a deformation that some displacement field π already describes. The membrane has one Goldstone field, its displacement π, a field on the membrane's own two space dimensions and time. The would-be Goldstone fields of the broken rotations are the slopes ∂ₓπ and ∂_zπ, which set the local tilt, and that of the broken boost is the velocity ∂ₜπ [T]. The massless excitations are ripples, waves of π travelling along the sheet.

The broken rotations and boost leave no fields of their own, but they still act on π, and the action must be invariant under them. At lowest order in derivatives this fixes the action up to one constant, the tension T, the membrane's energy per unit area: the action is −T times the spacetime volume of the membrane's history, the three-dimensional surface it sweeps out in spacetime [T]:

```text
S = −T ∫ dt dx dz √(1 − (∂ₜπ)² + (∂ₓπ)² + (∂_zπ)²)
```

For a membrane at rest the square root is the area element of the surface y = π(x, z), so the energy is T times the area. To second order in π the action is that of a free massless field, so the ripples travel at the speed of light. The higher terms of the square root are fixed by the broken symmetries, which act on π nonlinearly: the change in π depends on π itself. Tilting the whole membrane by a small angle θ about the z axis changes π by

```text
δπ = θ·x + θ·π·∂ₓπ
```

where the first term is the tilt and the second comes from relabelling the points of the tilted membrane [T]. The action is the membrane version of the Nambu–Goto action of a relativistic string [T].

## The commutator criterion [T]

Ivanov and Ogievetsky (1975 †) stated when a field can be removed, in the language of the coset construction, the standard way of writing theories of Goldstone fields (Coleman, Wess and Zumino 1969 †; Callan, Coleman, Wess and Zumino 1969 †), which Volkov (1973 †) extended to spacetime symmetries. In that construction the Goldstone fields are coordinates on the coset space G/G₀, the space of group elements taken up to the stabilizer ([coset targets](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models#coset-targets)). At each point of spacetime the fields are the parameters of a group element built from the broken generators; for spacetime symmetries the translations P_μ are included, with the coordinates x^μ as their parameters. Differentiating that group element and expanding the result in the generators gives combinations of the fields and their derivatives, the covariant derivatives ∇_μπ, which transform simply under every symmetry. Invariant actions are built from them [T].

The commutator of two generators measures how much the order of the two transformations matters; it vanishes when the order makes no difference. Here X and X′ are broken generators, with Goldstone fields π and π′. If the commutator of a translation with X′ contains X, the covariant derivative of π contains π′ itself, with no derivative on it:

```text
condition      [P_μ, X′] contains X                  (X and X′ both broken)
consequence    ∇_μπ = ∂_μπ + c·π′_μ + …              (c a nonzero constant; schematic)
constraint     ∇_μπ = 0, solved for π′_μ as a function of ∂_μπ
```

Because ∇_μπ transforms covariantly, setting it to zero is consistent with every symmetry, and π′ is then no longer an independent field [T]. The generators of an internal symmetry commute with the translations, so for an internal symmetry the condition is never met, and the count of one mode per broken generator stands.

The membrane meets the condition. A translation along x, rotated by a small angle θ about the z axis, becomes partly a translation along y, so the commutator of P_x with that rotation is proportional to P_y, the broken translation, and the rotation's field is fixed by ∂ₓπ. In the same way the commutator of the time translation with the boost along y is proportional to P_y, and the boost's field is fixed by ∂ₜπ [T].

The name reflects a comparison with the Higgs mechanism in its [Stückelberg form](/wiki/symmetry-breaking/stuckelberg-fields), in which a gauge field and the gradient of a Goldstone field appear together as A_μ + ∂_μπ, and the Goldstone field is absorbed into the gauge field. In ∇_μπ = ∂_μπ + c·π′_μ the field π′_μ stands where the gauge field stood, and the elimination runs the other way: π′_μ is removed in favour of the gradient of π [T].

## The dilaton [T]

A conformal theory is invariant under the transformations that preserve angles but not necessarily lengths [T]. Besides translations and Lorentz transformations, these are the dilatations x^μ → λx^μ, generated by D, and the special conformal transformations, generated by K_μ, which rescale lengths by a factor that varies from point to point. If a field that rescales under dilatations takes a nonzero vacuum value, that value sets a scale. D and K_μ are then broken, and the translations and Lorentz transformations are not.

The would-be Goldstone fields are the dilaton σ, for D, and a vector ξ_μ, for K_μ. The commutator of a translation with a special conformal transformation contains the dilatation, so by the criterion ξ_μ is fixed by the gradient of the dilaton, proportional to ∂_μσ at lowest order, and the dilaton is the only Goldstone mode [T]. The local picture gives the same answer. A special conformal transformation acts on a constant vacuum value as a dilatation whose size grows linearly with position, so a slowly varying one produces deformations that a position-dependent dilatation already produces (Low and Manohar 2002 †).

## Redundant fields and massive fields [T]

The criterion shows that a field can be removed without breaking any symmetry. It does not say what the removed field was physically, and that depends on the system [T]. In the membrane it was redundant: the tilts are slopes of the displacement and never had separate fluctuations. In other systems the field that a constraint removes corresponds to a massive mode of the full theory. The constrained theory then describes the system only at energies below that mass, and in such cases integrating the massive mode out at those energies gives the same theory as imposing the constraint [T].

## How the program uses it

### Absorbed or constrained

Two ways in which would-be Goldstone fields can fail to appear as independent massless fields occur in the record, applied to different fields.

- **Absorbed.** The choice of polarization breaks the [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms), the local shifts of the [momentum graviton](/wiki/gravity/momentum-graviton) X, which are a gauge symmetry. X absorbs their would-be Goldstone modes and becomes massive ([checkpoint #11](/wiki/history/documents/checkpoint) §7.1, [D + T]). That is a Higgs mechanism, with X in the role of the gauge field ([the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).
- **Constrained, by expectation [O].** The moduli of the vacuum's polarization are not among the absorbed modes: "The Λ(d) moduli, τ included, are not the eaten modes — they carry the compact phase directions, which constant shifts do not generate" (calc note #6 §3; [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten)). For the nine besides τ, calc note #5, written before #6, had named the other mechanism, expecting inverse-Higgs constraints to eliminate most of them.

### The expectation [O]

Calc note #5, in its section "Quadratic spectrum and the ghost question [partial]", lists the fields that the program's geometry leaves on the broken vacuum (§D):

> Field content on the broken vacuum: h_μν (10, graviton) ⊕ X_μν (10, momentum graviton) ⊕ Λ(d) σ-modes (10: τ plus nine, of which inverse-Higgs constraints likely eliminate most [O]) ⊕ matter.

Under [P2′](/wiki/program/postulates/p2-prime), the postulate that only the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) is rigid, the vacuum selects a [real structure J](/wiki/symmetry-breaking/order-parameter), the operator that marks which directions of phase space count as position, and the possible choices form [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian#the-space-of-vacuum-polarizations) Λ(d) (#5 §B). The [lab notebook](/wiki/history/documents/lab-notebook) calls Λ(d) the vacuum manifold and gives its dimension as "d(d+1)/2 = 10 for d = 4" (#1 §2). The σ-modes are the fluctuations of the polarization along it. One direction is the Maslov circle, whose angle is τ; the other nine are, in the notebook's words, "the nine non-Maslov directions" (#1 §8). Calc note #5's closing list of what is "Now precisely open" includes "(4) inverse-Higgs accounting of the nine heavy moduli" (§F).

These two passages are the record's only mentions of inverse-Higgs constraints. They give no argument for the expectation: they name no broken generators and no commutators of the kind the criterion requires, and, beyond calling the nine "heavy" (§F), they do not say whether an eliminated modulus would be redundant or massive. No later document returns to the question. #11 §14 does not list it, nor does [the handoff](/wiki/history/documents/handoff)'s open list (`HANDOFF.md` §2), and no document closes it. The wiki keeps it open at [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content), registered under [open problems](/wiki/status/open-problems#phase-space-geometry).

### What else the record says about the nine

- **Heavy, by assumption.** "that τ is the *lightest* modulus, with the other nine directions heavy, is assumed **[P]**" (#1 §2), and calc note #5 calls them "the nine heavy moduli" (§F). No document derives a mass for any of them.
- **Needed by polarization-genesis.** The lab notebook's sketch of [polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis), tagged "[O, sketched]", has "the heavy Grassmannian moduli (the nine non-Maslov directions)" decay at reheating (#1 §8), so it needs the nine to exist as fields. Calc note #5, written later, expects most of them to be eliminated, and no document reconciles the two ([conflicts between sources](/wiki/history/documents/source-conflicts#dark-matter)).

The rest of what the documents say about the ten moduli, including the toy model's single circle, is on [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content).

## Standard references

Added by the wiki from model memory (†); the program's documents cite none of them.

- E. A. Ivanov and V. I. Ogievetsky (1975)†: the inverse Higgs phenomenon and the commutator criterion.
- I. Low and A. V. Manohar (2002)†: the count of Goldstone modes by local transformations when spacetime symmetries break, with examples of broken Poincaré and conformal invariance.
- S. Coleman, J. Wess and B. Zumino (1969)†; C. G. Callan, S. Coleman, J. Wess and B. Zumino (1969)†: the coset construction for internal symmetries. D. V. Volkov (1973)†: its extension to spacetime symmetries.

## Used by

- [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content) — the nine non-Maslov moduli, of which calc note #5 expects inverse-Higgs constraints to "likely eliminate most" [O].
- [Open: polarization-genesis (OP7)](/wiki/dark-matter/candidates/polarization-genesis) — a sketch that needs the same nine moduli to exist and decay.
- [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase) — τ, the modulus that calc note #5 counts apart from the nine.
- [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten) — the nine moduli, left open beside τ.
- [Constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric) — the nine directions besides τ in the compact moduli space.

## Sources

- `notes/debt1a-geometric-core.md` §D — the field content of the broken vacuum and the expectation that inverse-Higgs constraints "likely eliminate most" of the nine [O]; §F item 4 — the "inverse-Higgs accounting of the nine heavy moduli", left open; §B — the vacuum's real structures form Λ(d)
- `notes/broken-born-theory.md` §2 — Λ(d) as the vacuum manifold, of dimension 10 at d = 4; τ the lightest modulus and the other nine heavy, assumed [P]; §8 — "the nine non-Maslov directions" in the polarization-genesis sketch [O, sketched]
- `notes/debt1a-ii-X-classification.md` §3 — the Λ(d) moduli are not the eaten modes
- `papers/broken-born-checkpoint-v2.md` §7.1 — the polarization choice breaks the dual diffeomorphisms, and X absorbs their would-be Goldstone modes [D + T]; §14 — the current open list, which does not carry the item
- `HANDOFF.md` §2 — the handoff's open list, which does not carry it either
