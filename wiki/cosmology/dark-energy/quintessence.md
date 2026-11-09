---
title: "Quintessence and the equation of state"
weight: 10
status: established
description: "Dynamical dark energy from a slowly evolving scalar field: the equation of state w and the field equation, short summaries of thawing versus freezing, hilltop and axion-like potentials and the CPL w₀–wₐ parametrization, the program's choice of potential, and recollapse when the vacuum energy turns negative or, with positive energy, in a closed universe."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §10"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 4"
  - "wiki/papers/broken-born-checkpoint-v2.md refs [19]–[21]"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-program-v1.md §8"
  - "review/wiki-build-flags.md items 27, 43"
  - "review/wiki-build-flags.md items 45, 50, 54"
  - "notes/closed-universe.md §2"
---

*Quintessence is dark energy made of a scalar field, a quantity with a single value at each point of space, whose energy density changes slowly as the universe expands instead of staying fixed as a [cosmological constant](cosmological-constant.md)'s does. Its behaviour is summarized by the equation of state w, the ratio of pressure to energy density: a cosmological constant has w = −1 exactly, and a field whose energy is almost all potential energy comes close to that value. In a [thawing model](thawing-and-freezing.md) the expansion holds the field nearly still at early times and it starts to change late, so w begins near −1 and rises. The program's dark-energy field [τ](tau-quintessence.md) is a model of this kind, with the periodic potential of an [axion-like field](axion-like-fields.md), sitting near the potential's maximum.*

**Status:** Established — [T] — textbook cosmology, written here from general knowledge, with the literature it names marked †; the fits that [checkpoint #11](../../history/documents/checkpoint.md) cites are live-searched [S] ([#11](../../papers/broken-born-checkpoint-v2.md) refs [19]–[21]).

## Dark energy and the equation of state

### Expansion and the Friedmann equation [T]

A spatially flat, homogeneous universe is described by a scale factor a(t), the factor by which distances between distant galaxies have grown. Its expansion rate H = ȧ/a is set by the total energy density ρ through the Friedmann equation, H² = ρ/(3M_P²), where M_P is the [reduced Planck mass](../../gravity/spin-2-fields/planck-units.md#two-conventions-for-the-planck-mass-t). Each component of the cosmic fluid obeys the continuity equation

```text
ρ̇ = −3H(ρ + p)
```

where p is its pressure. Writing the pressure as p = wρ defines the equation of state w. For constant w the continuity equation integrates to ρ ∝ a^{−3(1+w)}: matter (w = 0) dilutes as a⁻³, radiation (w = 1/3) as a⁻⁴, and a fluid with w = −1 does not dilute at all [T]. The background is on [Friedmann cosmology and minisuperspace](../scale-factor-duality/friedmann-cosmology.md).

### Acceleration [T]

The second Friedmann equation gives the acceleration, ä/a = −(ρ + 3p)/(6M_P²). The expansion accelerates when ρ + 3p < 0, which for a single dominant component means w < −1/3. Dark energy is the name for whatever component makes the present expansion accelerate.

### The cosmological constant [T]

The simplest dark energy is a cosmological constant Λ, an energy density of empty space that is the same everywhere and at all times: its pressure is minus its density, so w = −1 exactly and ρ stays constant as space expands. It is the standard expectation of the program's [prediction table](../../predictions/_index.md), "w ≡ −1" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) [row 4](../../predictions/dark-energy-drift.md)). Its own page, [the cosmological constant Λ](cosmological-constant.md), covers the rest, from the [de Sitter](de-sitter-space.md) future to [the cosmological-constant problem](../../gravity/spin-2-fields/cosmological-constant-problem.md).

## A scalar field as dark energy

### Energy density and pressure [T]

Quintessence replaces the constant by a scalar field φ (Ratra and Peebles †; Wetterich †). For a field that is uniform in space, the energy density and the pressure are

```text
ρ = ½φ̇² + V(φ)
p = ½φ̇² − V(φ)
```

with V the field's potential energy density, so that

```text
w = (½φ̇² − V) / (½φ̇² + V)
```

When V ≥ 0, w lies between −1 (all potential energy, φ̇ = 0) and +1 (all kinetic energy, the stiff fluid of [Friedmann cosmology](../scale-factor-duality/friedmann-cosmology.md)). A field whose kinetic energy is small compared with its potential energy has w close to −1 and behaves almost like a cosmological constant. The combination ρ + p = φ̇² is never negative, which is why such a field never reaches w < −1 while its energy density is positive ([the phantom divide and the null energy condition](phantom-divide.md)).

The program writes the same structure for its field τ, S_τ = ∫√−g[½(∂τ)² − V(τ)] ([#1 §3](../../../notes/broken-born-theory.md#3-action), transcribed from its LaTeX): a canonical kinetic term plus a potential.

### The field equation [T]

A uniform field obeys

```text
φ̈ + 3Hφ̇ + V′(φ) = 0
```

This is the equation of an oscillator whose restoring force is −V′ and whose damping coefficient is 3H, set by the expansion. While H is large compared with the field's natural rate of change, √|V″|, the damping dominates and the field barely moves: it is "frozen" by the expansion, with φ̇ ≈ 0 and w ≈ −1. As H falls, the damping weakens and the field begins to respond to the slope of its potential.

## Thawing and freezing [T]

The two regimes of the field equation divide quintessence models into two classes (Caldwell and Linder †). A thawing field is frozen at early times, with w ≈ −1, and departs from −1 late, once H has fallen far enough, so w rises toward the present. A freezing field is already evolving at early times, with w > −1, and slows down, so w falls toward −1. The [lab notebook](../../history/documents/lab-notebook.md) places the program's field in the first class: "Hilltop initial conditions give w ≈ −1 in the past, rising now" ([#1 §7 item 2](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround)). The classes are set out on [thawing and freezing quintessence](thawing-and-freezing.md): why a thawing field's initial velocity drops out, hilltop models, where each class lies in the plane of the two numbers w₀ and wₐ [summarized below](#the-wwₐ-parametrization-t) (w₀ is the value of w today, and wₐ measures how fast w has changed as the universe expanded), the program's thawing corridor, and how the second data release of the Dark Energy Spectroscopic Instrument bears on the class.

## Hilltop and axion-like potentials [T]

### Hilltop quintessence

In a hilltop model the field begins near a maximum of its potential, where V′ ≈ 0 and V″ < 0 (Dutta and Scherrer †), and a small displacement from the top grows once the expansion damping weakens. Hilltop models are thawing models; how fast w rises depends on the curvature of the maximum compared with the expansion rate ([hilltop models](thawing-and-freezing.md#hilltop-models)).

### Axion-like fields

An axion-like field, or pseudo-Nambu–Goldstone field, is an angle: its couplings are invariant under the shift φ → φ + constant, up to a small explicit breaking that leaves the periodic potential V(φ) = V₀[1 + cos(φ/f)], with period 2πf in φ (Frieman, Hill, Stebbins and Waga 1995, [astro-ph/9505060](https://arxiv.org/abs/astro-ph/9505060), which the closed-universe note cites as retrieved [S]; flag 54). The shift symmetry keeps the field light, and the maximum at cos(φ/f) = 1 makes it a natural hilltop model. The mechanism, the axion itself, axion-like dark matter and dark energy, and the program's uses of the idea are on [axion-like fields and pseudo-Goldstone bosons](axion-like-fields.md).

### The program's choice

[#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology): "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology". In the program the period is not chosen: τ is an angle on a circle in the space of polarizations ([τ as the Maslov phase of the boundary](../../phase-space/modular-field/maslov-phase.md)). The program's version is on [τ: hilltop quintessence on the Maslov circle](tau-quintessence.md), and among the fits of this class of potential to data is an axion-quintessence analysis of data from the Dark Energy Spectroscopic Instrument (DESI), Ureña-López et al. [20S] ([DESI baryon acoustic oscillations](desi.md)).

## The w₀–wₐ parametrization [T]

Surveys summarize a changing w by the two-parameter Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a), with a = 1 today: w₀ is the present value, and a negative wₐ means that w has been rising as the universe expands (Chevallier and Polarski †; Linder †). A thawing field has w₀ > −1 and wₐ < 0, and thawing models lie near a line that the program calls the "thawing corridor wₐ ≈ −1.5(1 + w₀)" ([#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology)); no document gives a reference for it. Where the form comes from, its pivot version, what two numbers cannot represent, and how a CPL fit expresses the phantom crossing reported in DESI's second data release ([DESI DR2's phantom crossing](desi-dr2-phantom-crossing.md)) are on [the CPL parametrization](cpl-parametrization.md). That page also reports flag 43 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md): the corridor itself lies in the region of the w₀–wₐ plane in which a CPL line passes below −1 in the past, the region of the release's fits, and what separates it from the release's crossing is the slope, not the region ([the corridor and DR2's crossing](cpl-parametrization.md#the-corridor-and-dr2s-crossing)).

## Recollapse [T]

If the total energy density of a flat universe reaches zero, the Friedmann equation gives H = 0: the expansion halts. A negative potential energy can bring this about, because the potential term does not dilute while the matter density falls as a⁻³. Since the acceleration is negative at that moment, the universe then contracts. A field that settles into a negative minimum of its potential acts as a [negative cosmological constant](cosmological-constant.md#a-negative-λ-turnaround-and-collapse-t), an anti-de Sitter phase, and the contraction ends in collapse [T].

[#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) cites "high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]". The lab notebook gives a figure for one of those fits, a "93.8% preference for a future transition to anti-de Sitter space with eventual cosmological collapse" (Gialamas et al., [arXiv:2506.21542](https://arxiv.org/abs/2506.21542); [#1 §7 item 3](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround)). That figure appears only in #1. The closed-universe investigation checked the paper: it fits a quartic potential V₀ + m²φ²/2 + λφ⁴/4 in a flat universe with the sign of the vacuum energy left free, and 93.8% is the posterior probability that the vacuum energy is negative, 12.2% for a future transition plus 81.6% for a vacuum already negative today. "Future transition … collapse" is the paper's own abstract wording; the description of the fitted potential is not. Of the three works #11 cites for the clause, only [19] supports it: [20] fits V₀[1 + cos] with null spatial curvature and mentions no anti-de Sitter phase or collapse (flag 45 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).

**Recollapse with positive energy [T].** In a closed universe, one with positive spatial curvature, the curvature term enters the Friedmann equation with the sign opposite to an energy density, H² = ρ/(3M_P²) − k/a², so the expansion can halt with every density positive. A quintessence field that has passed its minimum and oscillates about it averages to pressure-free matter, and a closed universe filled with matter recollapses. Recollapse of a closed universe with oscillating quintessence is published (Barrow 1987 †; Tipler et al., [gr-qc/0003082](https://arxiv.org/abs/gr-qc/0003082), §7 [S]; [`notes/closed-universe.md` §2](../../../notes/closed-universe.md#2-the-premise-and-the-turnaround-it-buys); flag 50).

The program uses recollapse for its far-future turnaround ([the turnaround as the conjugate bounce](../scale-factor-duality/conjugate-bounce.md)). Whether its own potential can go negative is unresolved: V₀[1 + cos(τ/f)] is never negative when V₀ > 0 ([Open: the sign of V(τ) and the turnaround](potential-sign.md); flag 27 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). The flag's addendum (2026-10-27) finds that with this potential the program's turnaround is the closed, positive-energy kind: flat and open universes never turn around, and a closed one does ([a closed Comatter universe](../scale-factor-duality/closed-universe.md)). Neither cited fit bears on that recollapse (flag 45).

## Fits to current data [S]

[#11 §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) summarizes the fits of quintessence models to recent data: "compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ)". The works it cites, all retrieved by live search:

- [19][S] I. D. Gialamas, G. Hütsi, M. Raidal, J. Urrutia, M. Vasar, H. Veermäe, "Quintessence and phantoms in light of DESI 2025," [arXiv:2506.21542](https://arxiv.org/abs/2506.21542).
- [20][S] L. A. Ureña-López et al. (DESI), axion-quintessence analysis of DESI data, [arXiv:2503.20178](https://arxiv.org/abs/2503.20178). #11 gives a description, not the paper's title.
- [21][S] DESI Collaboration (M. Abdul-Karim et al.), "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," [arXiv:2503.14738](https://arxiv.org/abs/2503.14738) (2025).

The earlier documents cite the first two as [T]: [#1 §7](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround) tags them [T], and [#9 §8](../../../notes/broken-born-program-v1.md#8-cosmology) adds "[T — refresh citations before publication]". The survey itself is described on [DESI baryon acoustic oscillations](desi.md).

## Used by

- [τ: hilltop quintessence on the Maslov circle](tau-quintessence.md) — τ is a thawing hilltop field with an axion-like potential.
- [Fifth-force safety of τ](tau-fifth-force.md) — the shift symmetry of an axion-like field.
- [The no-phantom bound w ≥ −1](no-phantom-bound.md) — ρ + p = φ̇² ≥ 0 for a canonical scalar.
- [The dark-energy over-constraint](over-constraint.md) — in a thawing model the field's initial velocity is not a separate parameter.
- [Open: the sign of V(τ) and the turnaround](potential-sign.md) — recollapse in a flat or open universe needs negative vacuum energy.
- [The turnaround as the conjugate bounce](../scale-factor-duality/conjugate-bounce.md) — recollapse once the vacuum energy is negative, or with positive energy in a closed universe.
- [Open: dual kinetic energy versus τ's potential](../scale-factor-duality/dual-kinetic-link.md) — hilltop quintessence as the explanation the program implements.
- [DESI DR2's phantom crossing](desi-dr2-phantom-crossing.md) — the equation of state w(z) that the release fits, with z the [redshift](../scale-factor-duality/redshift.md), the stretching of light by the expansion of the universe since the light was emitted (larger z means earlier).
- [τ as the Maslov phase of the boundary](../../phase-space/modular-field/maslov-phase.md) — τ's periodic potential, compared with quintessence in general.
- [Row 4: thawing dark energy, never phantom](../../predictions/dark-energy-drift.md) — the equation of state and the thawing class that row 4 tests.
- [Row 5: the fate of the expansion](../../predictions/fate-of-expansion.md) — recollapse when the vacuum energy turns negative, or with positive energy in a closed universe.
- [A closed Comatter universe](../scale-factor-duality/closed-universe.md) — recollapse of a closed universe with oscillating quintessence.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) — the program's potential, the thawing corridor, the state of the fits and the negative-minimum fits; [§13 row 4](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) for the standard expectation w ≡ −1
- [`wiki/papers/broken-born-checkpoint-v2.md`](../../papers/broken-born-checkpoint-v2.md) refs [19]–[21] — the cited fits and the DESI release (live-searched)
- [`notes/broken-born-theory.md` §3](../../../notes/broken-born-theory.md#3-action) — the action S_τ with a canonical kinetic term
- [`notes/broken-born-theory.md` §7 items 2–3](../../../notes/broken-born-theory.md#7-cosmology-ii-dark-energy-its-drift-and-the-turnaround) — hilltop initial conditions and τ's thawing shape, the fits with a negative minimum and the 93.8% figure (#1 only)
- [`notes/broken-born-program-v1.md` §8](../../../notes/broken-born-program-v1.md#8-cosmology) — the same fits, marked "[T — refresh citations before publication]"
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 27 — the potential as written cannot turn negative; item 43 — the corridor in the region of the release's fits, separated from its crossing by the slope
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 27 (addendum) and [`notes/closed-universe.md` §2](../../../notes/closed-universe.md#2-the-premise-and-the-turnaround-it-buys) — the closed turnaround with V ≥ 0, its prior art and the potential's source; items 45, 50 and 54 — the 93.8% figure and the compound citation, the published recollapse, Frieman et al. retrieved [S]
