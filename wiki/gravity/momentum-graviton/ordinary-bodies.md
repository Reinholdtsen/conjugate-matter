---
title: "X between ordinary bodies: a Yukawa term, not a velocity gate"
weight: 97
status: alive
description: "Between two ordinary bodies, in the aligned vacuum (u = 1) and unscreened, the momentum graviton X adds a Yukawa term of range below 37.7 μm whose dependence on relative velocity is the O(v²/c²) spin-2 factor, 1 + 2.40×10⁻⁷ at 120 km/s, not a gate; #13's dual kinematics and the Siegel reading give negligible corrections; a potential in momentum differences exerts no force; and a relative-velocity gate acting between all bodies is bounded to |ε| < 8.7×10⁻⁹."
provenance: [D, V]
sources:
  - "notes/velocity-gated-gravity.md header"
  - "notes/velocity-gated-gravity.md §1"
  - "notes/velocity-gated-gravity.md §2"
  - "notes/velocity-gated-gravity.md §3"
  - "notes/velocity-gated-gravity.md §10"
  - "notes/velocity-gated-gravity.md §11"
  - "verify/velocity_gated_gravity.py 'B. X between ordinary bodies'"
  - "verify/velocity_gated_gravity.py 'C. A universal relative-velocity gate between ordinary bodies'"
  - "verify/velocity_gated_gravity.py 'Anchors (independent of the investigation)'"
  - "review/wiki-build-flags.md items 39, 56, 57"
  - "wiki/papers/phase-space-diameter.md §8.2"
  - "wiki/papers/conjugate-special-relativity.md §2"
  - "wiki/papers/conjugate-special-relativity.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "review/momentum-gravity/README.md"
---

*The [momentum graviton X](_index.md) is the program's second spin-2 field, the massive partner of the ordinary graviton. P.R.'s question is whether this "momentum gravity" would show up between two massive bodies as a correction to ordinary gravity that depends on their relative velocity. The answer, worked out in a note of 2026-10-28, is no. Between two ordinary bodies X adds a second, short-range piece to Newton's attraction, with a range below a few hundredths of a millimetre. Like every force carried by a field, it depends on the bodies' relative velocity only through the corrections of relativity, which at galactic speeds are parts in ten million and of the same size as ordinary gravity's own. A correction gated in relative velocity and acting between all bodies would shift planetary orbits and binary pulsars, and at gravitational strength such a term is excluded by at least eight orders of magnitude.*

**Status:** Alive — computed, not reviewed — [D][V] for the velocity factor (two verifiers by different methods), [V][S] for the potential and its range, [D; data S; two verifiers] for the bounds on a universal gate, and [D; negligible either way] for the two other readings, as [`notes/velocity-gated-gravity.md`](../../../notes/velocity-gated-gravity.md) §§2–3 tags them. Every number is recomputed in sections B and C of [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) ([the velocity-gated-gravity script](../../method/verification/velocity-gated-gravity-script.md)); the note has not been through a blind review round. Flag 56 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), on [#13](../../papers/conjugate-special-relativity.md)'s two answers for gravitating pairs, is pending.

## The question

P.R.'s question is whether momentum gravity would look like a perturbation to regular gravity that depends on the relative velocity of two massive bodies ([`notes/velocity-gated-gravity.md` §1](../../../notes/velocity-gated-gravity.md#1-the-question-the-readings-the-method)). It bears on the program's founding picture of dark matter, P.R.'s open conjecture [O] ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested); [Conjecture: velocity clumping, the founding image](../../dark-matter/momentum-clumping/founding-image.md)), and the note's results are evidence about [the scope of the tests](../../dark-matter/momentum-clumping/founding-image.md#the-scope-of-the-tests) of that picture. The note reads the question three ways [assumption]:

- "momentum gravity" as the program defines it, the massive X of [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton), acting between ordinary bodies, with two further readings checked: #13's dual kinematics and the Siegel reading of flag 39 (this page);
- a perturbation that depends on relative velocity and acts between all bodies, tested against the Solar System and binary pulsars (this page, [the last section](#a-universal-relative-velocity-gate-is-excluded));
- the same, acting only between dark-matter particles χ and at long range, a model the record does not contain ([Conjecture: a long-range velocity-gated attraction among χ](../../dark-matter/momentum-clumping/long-range-gated-attraction.md)).

The strength of a gated term relative to gravity is ε ≡ G̃/G. The note's gate conventions (§1): the record's cross-section gate is e^{−v²/v\*²} with v\* ≈ 120 km/s, and its amplitude gate is e^{−v²/v_a²} with v_a = √2 v\* = 169.7 km/s ([the velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md)).

## The potential between two bodies

The record gives X's contribution as a [Yukawa term](../spin-2-fields/yukawa-forces.md#fifth-forces-a-yukawa-term-beside-gravity-t) beside Newton's potential [V][S] (§2):

```text
V = −(G m₁ m₂ / r) · (1 + (4/3) e^{−r/λ_X})
```

in the aligned vacuum (background ratio u = 1), with λ_X < 37.7 μm if the Sun and planets are not screened ([the laboratory bound on X's range](range-bound.md); [`wiki/papers/phase-space-diameter.md` §8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs)). A search of the record finds no velocity dependence assigned to this term ([§2](../../papers/phase-space-diameter.md#2-three-meanings-of-size-in-momentum-space)).

## Its velocity dependence is relativistic

[D][V; two verifiers by different methods] (§2).

- **The factor.** Single exchange of a massive spin-2 field between point sources carries the factor (3γ² − 1)/2, with γ = u₁·u₂ the relative Lorentz factor of the two bodies. The massless graviton carries 2γ² − 1. The graviton's factor reproduces the O(G) terms of the Einstein–Infeld–Hoffmann two-body Lagrangian of [general relativity](../spin-2-fields/general-relativity.md) [T]. (3γ² − 1)/2 is the Legendre polynomial P₂(γ), and 2γ² − 1 the Chebyshev polynomial T₂(γ); the static ratio of the two numerators, massive to massless, is 4/3, the van Dam–Veltman–Zakharov factor ([`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py), anchor A3; [Fierz–Pauli theory](../spin-2-fields/fierz-pauli.md)).
- **The size.** At 120 km/s the factor is 1 + 2.40×10⁻⁷ for X, against 1 + 3.20×10⁻⁷ for the graviton (§2).
- **No gate.** Both factors grow monotonically with relative velocity (check B1): X's dependence on relative velocity is this O(v²/c²) spin-2 factor, not a gate, and X is not velocity-gated at any range (§2).

At order v² the script writes X's interaction out in full (check B0, in units with c = 1, α the strength and M the mass of X):

```text
α G m1 m2 e^(-Mr)/r [1 + v1^2 + v2^2 - 5/2 v1.v2 - 1/2 (n.v1)(n.v2)] - (α G m1 m2 M/2) e^(-Mr)(n.v1)(n.v2)
```

"a Yukawa with relativistic O(v^2/c^2) terms, no gate". Its anchor is the massless case, where the same construction reproduces the order-G terms of the Einstein–Infeld–Hoffmann Lagrangian as Landau and Lifshitz give it (anchor A2). The [gate-mechanism note](../../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate) reaches the same factor from the other side, as the forward amplitude of X exchange between two χ: N(k,0)/N(0,0) = 1 + 6k²/m² + 6k⁴/m⁴, which is P₂(γ) ([`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate)). Why no field of finite spin does better is on [what could carry a relative-velocity gate](../../dark-matter/conjugate-matter/gate-carriers.md).

## Two other readings of momentum gravity

[D; negligible either way] (§2).

- **#13's dual kinematics.** In [conjugate special relativity](../../conjugate-relativity/_index.md), the dual of velocity is force, and corrections are γ̃ − 1 = (1/2)(F/c̃)², with c̃ = c⁴/G the [maximum force](../../conjugate-relativity/maximum-force.md). For the Sun and Earth, F/c̃ = 2.93×10⁻²² and γ̃ − 1 = 4.3×10⁻⁴⁴. But [#13 §5](../../papers/conjugate-special-relativity.md#5-inertia-dualized) identifies dual rest with free fall ([dual inertia: free fall as rest](../../conjugate-relativity/dual-inertia.md)), which makes the correction zero for any freely falling pair, while [#13 §2](../../papers/conjugate-special-relativity.md#2-force-boosts) says a black-hole merger "operates at F ~ c̃ by construction" ([Open: merger-band corrections](../../conjugate-relativity/force-boosts.md#open-merger-band-corrections)). The two sections disagree: flag 56 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), rated low, "raised by 1 agent (the run-3 theory verifier), upheld by the final critic". For the Sun and Earth the two readings give 4.3×10⁻⁴⁴ and 0; "both are negligible, but the paper gives two answers" (flag 56).
- **The Siegel reading.** Under the reading of flag 39, in which reciprocity acts on the spin-2 sector through [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)'s map on the [modular field](../../phase-space/modular-field/modular-inversion.md) (open), Standard-Model matter has no linear X coupling. Its coupling sits in the mixed block of the generalized metric, with relative size about vF/(c⁵/G) = 2.9×10⁻²⁶ for the Sun and Earth, a product of velocity and force ([§2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification)).

The answer as first given wrote "(F/c̃)² ≈ 4×10⁻⁴⁴"; the note corrects it to γ̃ − 1 = (F/c̃)²/2 (§11), and the script prints (F/c̃)² = 8.56×10⁻⁴⁴ = 2(γ̃ − 1) (check B2).

## A potential in momentum differences exerts no force

[D][V] (§2). The founding image imagines an attraction between particles close in momentum rather than in position. The note checks what such a term does:

- A potential U(p_a − p_b) that depends only on momenta contributes nothing to ṗ = −∂H/∂x, in any external potential. It changes only how velocity relates to momentum, which is inertia.
- It leaves relative momenta unchanged only in free space or a uniform field. In a harmonic core, the canonical map X = p/(mΩ), P = −mΩx (here X and P are new canonical coordinates, not the field X) turns it exactly into an ordinary attraction in position, for orbits that stay inside the core: "the founding image's exchange of x and v, realized". In signal terms the map is a quarter-turn of phase space, the rotation that takes a waveform to its spectrum ([the Fourier transform](../../phase-space/reciprocity/fourier-transform.md)) [T].
- The map preserves the energy, so the contact gate's shortfall is unchanged ([the mean-field criterion](../../dark-matter/momentum-clumping/instability-criterion.md)).

## A universal relative-velocity gate is excluded

Corrections to Newton's law that depend on relative velocity are old, and they are already tested, because general relativity has one; Tisserand applied a Weber-type law, a force depending on relative velocity, to the planets in 1872 [S]. A gated term acting between all bodies would shift planetary perihelia, the Moon's orbit and binary pulsars, and at gravitational strength it is excluded by at least eight orders of magnitude (§3, plain-language passage).

**The model** [D][V] (§3).

- V = −(Gm₁m₂/r)[1 + εW(|v₁ − v₂|/v_a)], treated as a Lagrangian potential so that the canonical momentum is handled correctly.
- Circular orbits obey ω²r³ = G·M[1 + εK(u)] exactly, with K = W − uW′ and u the orbital speed over the gate width. The apsidal advance follows from the same averaging that reproduces general relativity's 6πG·M/(c²a(1 − e²)) [T]; the script's anchor reproduces Mercury's 43.0 arcsec per century from it (anchor A8).
- For a gate wider than orbital speeds the term acts like a first post-Newtonian velocity term with c replaced by the gate width.

**The bounds** [D; data S; two verifiers] (§3).

| Gate | Range of widths | Bound | Set by |
| --- | --- | --- | --- |
| Gaussian, e^{−v²/v_a²} | v_a = 0.3–3000 km/s, which is v\* = 0.2–2100 km/s in the record's convention | \|ε\| < 8.7×10⁻⁹ | the double pulsar, at the 3000 km/s end (check C3) |
| Lorentzian | 0.1–3000 km/s | \|ε\| < 9.4×10⁻⁹ | the double pulsar, at 3000 km/s (check C3) |
| Gaussian, the record's width | v_a = 170 km/s (v\* = 120 km/s) | \|ε\| < 3.5×10⁻¹¹ | Mars's perihelion, EPM2011 ephemeris |

- **The record's width.** An interim bound of 2×10⁻¹¹ from Mercury used the other gate convention; the note corrects it to 3.5×10⁻¹¹ from Mars (§11; check C2).
- **Below about 0.3 km/s,** ε ~ 1 is excluded only qualitatively: a body at rest at a pole would have vanishing inertia for ε ≈ 8×10⁻⁵ at v_a = 0.1 km/s. No sourced numerical bound exists there (§3).
- **Composite bodies.** Which velocities the gate sees inside a composite body matters. If it acts on constituents, internal motion suppresses it, and what remains is a composition-dependent G, bounded by torsion balances and the MICROSCOPE satellite under model-dependent assumptions ([the equivalence principle](../spin-2-fields/equivalence-principle.md)). A gate on the difference of momenta, |m₁v₁ − m₂v₂|, is not Galilean invariant (§3).
- **Scope.** "None of this touches a gate confined to χ, which is the next question" (§3): [Conjecture: a long-range velocity-gated attraction among χ](../../dark-matter/momentum-clumping/long-range-gated-attraction.md).

The investigation's run-2 pre-registration expected this result: "no gate between ordinary bodies, only O(v²/c²) structure; the gate is χ–χ at contact; a universal version is excluded" (§11). That pre-registration was not blind: three agents read it, so their judgment-level text was not blind, while their executed numbers were unaffected (§11; [`review/momentum-gravity/README.md`](../../../review/momentum-gravity/README.md)).

## What is open

From the note's §10 [O]:

- a sourced numerical bound on a universal gate below about 0.3 km/s;
- whether the program's bimetric branch has Vainshtein screening at all, the nonlinear suppression of a massive graviton's extra force near a body [T]. The bound λ_X < 37.7 μm assumes the Sun and planets are not screened, and the diameter note's Vainshtein radius uses the formula for a massless mode (flag 57 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [unscreened at these ranges](range-bound.md#unscreened-at-these-ranges-dv)).

Both are on [open problems and the queue](../../status/open-problems.md).

## Sources

- [`notes/velocity-gated-gravity.md`](../../../notes/velocity-gated-gravity.md) (2026-10-28, not reviewed) header — the note's status, computed and not through a blind review round; [§1](../../../notes/velocity-gated-gravity.md#1-the-question-the-readings-the-method) — the question, its readings and the gate conventions; [§2](../../../notes/velocity-gated-gravity.md#2-between-ordinary-bodies-x-is-a-short-range-yukawa-term-not-a-velocity-gate) — the potential, the relativistic factor, the two other readings and the potential in momentum differences; [§3](../../../notes/velocity-gated-gravity.md#3-a-universal-relative-velocity-gate-between-ordinary-bodies-is-excluded) — the universal gate, its model and bounds; [§10](../../../notes/velocity-gated-gravity.md#10-open) — what is open; [§11](../../../notes/velocity-gated-gravity.md#11-record) — the corrections and the run-2 pre-registration scored
- [`verify/velocity_gated_gravity.py`](../../../verify/velocity_gated_gravity.py) — anchors A2, A3, A8; section B, X between ordinary bodies; section C, the universal gate ([the velocity-gated-gravity script](../../method/verification/velocity-gated-gravity-script.md))
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 56 — [#13 §2](../../papers/conjugate-special-relativity.md#2-force-boosts) against [§5](../../papers/conjugate-special-relativity.md#5-inertia-dualized) on gravitating pairs; item 57 — the Vainshtein formula; item 39 — the two actions of reciprocity on the spin-2 sector; all pending
- [`wiki/papers/phase-space-diameter.md` §8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs) — the potential in the aligned vacuum and λ_X < 37.7 μm
- [`wiki/papers/conjugate-special-relativity.md` §2](../../papers/conjugate-special-relativity.md#2-force-boosts) — the merger arena, "operates at F ~ c̃ by construction"; [§5](../../papers/conjugate-special-relativity.md#5-inertia-dualized) — dual rest as free fall
- [`wiki/papers/broken-born-checkpoint-v2.md` §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) — X as one massive spin-2 field; [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the founding image, P.R.'s open conjecture
- [`review/momentum-gravity/README.md`](../../../review/momentum-gravity/README.md) — the investigation's runs and the blindness of its pre-registrations
