---
title: "Quintessence and the equation of state"
weight: 10
status: established
description: "Dynamical dark energy from a slowly evolving scalar field: the equation of state w, thawing versus freezing, hilltop and axion-like potentials, a summary of the CPL w₀–wₐ parametrization, and recollapse when the vacuum energy turns negative."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "papers/broken-born-checkpoint-v2.md refs [19]–[21]"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-program-v1.md §8"
---

*Quintessence is dark energy made of a scalar field, a quantity with a single value at each point of space, whose energy density changes slowly as the universe expands instead of staying fixed as a cosmological constant's does. Its behaviour is summarized by the equation of state w, the ratio of pressure to energy density: a cosmological constant has w = −1 exactly, and a field whose energy is almost all potential energy comes close to that value. In a thawing model the expansion holds the field nearly still at early times and it starts to change late, so w begins near −1 and rises. The program's dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) is a model of this kind, with the periodic potential of an axion-like field, sitting near the potential's maximum.*

**Status:** Established — [T] — textbook cosmology, written here from general knowledge, with the literature it names marked †; the fits that [checkpoint #11](/wiki/history/documents/checkpoint) cites are live-searched [S] (#11 refs [19]–[21]).

## Dark energy and the equation of state

### Expansion and the Friedmann equation [T]

A spatially flat, homogeneous universe is described by a scale factor a(t), the factor by which distances between distant galaxies have grown. Its expansion rate H = ȧ/a is set by the total energy density ρ through the Friedmann equation, H² = ρ/(3M_P²), where M_P is the reduced Planck mass. Each component of the cosmic fluid obeys the continuity equation

```text
ρ̇ = −3H(ρ + p)
```

where p is its pressure. Writing the pressure as p = wρ defines the equation of state w. For constant w the continuity equation integrates to ρ ∝ a^{−3(1+w)}: matter (w = 0) dilutes as a⁻³, radiation (w = 1/3) as a⁻⁴, and a fluid with w = −1 does not dilute at all [T]. The background is on [Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology).

### Acceleration [T]

The second Friedmann equation gives the acceleration, ä/a = −(ρ + 3p)/(6M_P²). The expansion accelerates when ρ + 3p < 0, which for a single dominant component means w < −1/3. Dark energy is the name for whatever component makes the present expansion accelerate.

### The cosmological constant [T]

The simplest dark energy is a cosmological constant, an energy density of empty space that is the same everywhere and at all times. Its pressure is minus its energy density, w = −1 exactly, and ρ stays constant as space expands. The cosmological constant is the standard expectation in the program's [prediction table](/wiki/predictions): "w ≡ −1" (#11 §13 [row 4](/wiki/predictions/dark-energy-drift)). Why quantum vacuum energy does not produce a far larger value is a separate, unsolved question ([the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem)).

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

When V ≥ 0, w lies between −1 (all potential energy, φ̇ = 0) and +1 (all kinetic energy, the stiff fluid of [Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)). A field whose kinetic energy is small compared with its potential energy has w close to −1 and behaves almost like a cosmological constant. The combination ρ + p = φ̇² is never negative, which is why such a field never reaches w < −1 while its energy density is positive ([the phantom divide and the null energy condition](/wiki/cosmology/dark-energy/phantom-divide)).

The program writes the same structure for its field τ, S_τ = ∫√−g[½(∂τ)² − V(τ)] (#1 §3, transcribed from its LaTeX): a canonical kinetic term plus a potential.

### The field equation [T]

A uniform field obeys

```text
φ̈ + 3Hφ̇ + V′(φ) = 0
```

This is the equation of an oscillator whose restoring force is −V′ and whose damping coefficient is 3H, set by the expansion. While H is large compared with the field's natural rate of change, √|V″|, the damping dominates and the field barely moves: it is "frozen" by the expansion, with φ̇ ≈ 0 and w ≈ −1. As H falls, the damping weakens and the field begins to respond to the slope of its potential.

## Thawing and freezing [T]

The two regimes of the field equation give the standard classification of quintessence models (Caldwell and Linder †):

- **Thawing.** The field is frozen at early times, with w ≈ −1, and departs from it late, once H has fallen far enough. The equation of state rises away from −1 toward the present.
- **Freezing.** The field is already evolving at early times, with w > −1, and slows down as it approaches the asymptotic form of its potential, so w falls toward −1.

The lab notebook places the program's field in the first class: "Hilltop initial conditions give w ≈ −1 in the past, rising now: w₀ > −1, wₐ < 0, on the standard thawing corridor wₐ ≈ −1.5(1 + w₀)" (#1 §7 item 2; the [lab notebook](/wiki/history/documents/lab-notebook)). The quantities w₀ and wₐ are the two parameters of [the CPL parametrization](/wiki/cosmology/dark-energy/cpl-parametrization), summarized below.

## Hilltop and axion-like potentials [T]

### Hilltop quintessence

In a hilltop model the field begins near a maximum of its potential, where V′ ≈ 0 and V″ < 0 (Dutta and Scherrer †). Near the maximum the force −V′ points away from it, so a small displacement grows once the expansion damping weakens. Starting close to the top keeps w near −1 for a long time; how fast w then rises depends on how sharply curved the maximum is compared with the expansion rate. Hilltop models are thawing models.

### Axion-like fields

An axion-like field, or pseudo-Nambu–Goldstone field, is an angle: a field whose couplings are invariant under the shift φ → φ + constant, up to a small explicit breaking that leaves a periodic potential (Frieman, Hill, Stebbins and Waga †). The standard form is

```text
V(φ) = V₀[1 + cos(φ/f)]
```

with a period 2πf in φ. The shift symmetry keeps the field light, and its maximum at cos(φ/f) = 1 makes it a natural hilltop model. The general mechanism is on [Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs).

### The program's choice

#11 §10: "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology". In the program the period is not chosen: τ is an angle on a circle in the space of polarizations ([τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase)). The program's version is on [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence), and among the fits of this class of potential to data is an axion-quintessence analysis of data from the Dark Energy Spectroscopic Instrument (DESI), Ureña-López et al. [20S] ([DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi)).

## The w₀–wₐ parametrization [T]

Surveys summarize a changing w by the two-parameter Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a), with a = 1 today: w₀ is the present value, and a negative wₐ means that w has been rising as the universe expands (Chevallier and Polarski †; Linder †). A thawing field has w₀ > −1 and wₐ < 0, and thawing models lie near a line that the program calls the "thawing corridor wₐ ≈ −1.5(1 + w₀)" (#11 §10); no document gives a reference for it. Where the form comes from, its pivot version, what two numbers cannot represent, and how a CPL fit expresses the phantom crossing reported in DESI's second data release ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)) are on [the CPL parametrization](/wiki/cosmology/dark-energy/cpl-parametrization).

## Recollapse [T]

If the total energy density of a flat universe reaches zero, the Friedmann equation gives H = 0: the expansion halts. A negative potential energy can bring this about, because the potential term does not dilute while the matter density falls as a⁻³. Since the acceleration is negative at that moment, the universe then contracts. A field that settles into a negative minimum of its potential acts as a negative cosmological constant, an anti-de Sitter phase, and the contraction ends in collapse [T].

#11 §10 cites "high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]". The lab notebook gives a figure for one of those fits, a "93.8% preference for a future transition to anti-de Sitter space with eventual cosmological collapse" (Gialamas et al., arXiv:2506.21542; #1 §7 item 3). That figure appears only in #1, and no `verify/` script or later document checks it.

The program uses recollapse for its far-future turnaround ([the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)). Whether its own potential can go negative is unresolved: V₀[1 + cos(τ/f)] is never negative when V₀ > 0 ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); flag 27 in `review/wiki-build-flags.md`).

## Fits to current data [S]

#11 §10 summarizes the fits of quintessence models to recent data: "compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ)". The works it cites, all retrieved by live search:

- [19][S] I. D. Gialamas, G. Hütsi, M. Raidal, J. Urrutia, M. Vasar, H. Veermäe, "Quintessence and phantoms in light of DESI 2025," arXiv:2506.21542.
- [20][S] L. A. Ureña-López et al. (DESI), axion-quintessence analysis of DESI data, arXiv:2503.20178. #11 gives a description, not the paper's title.
- [21][S] DESI Collaboration (M. Abdul-Karim et al.), "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," arXiv:2503.14738 (2025).

The earlier documents cite the first two as [T]: #1 §7 tags them [T], and #9 §8 adds "[T — refresh citations before publication]". The survey itself is described on [DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi).

## Used by

- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — τ is a thawing hilltop field with an axion-like potential.
- [Fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force) — the shift symmetry of an axion-like field.
- [The no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) — ρ + p = φ̇² ≥ 0 for a canonical scalar.
- [The dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint) — in a thawing model the field's initial velocity is not a separate parameter.
- [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign) — recollapse needs negative vacuum energy.
- [The turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce) — recollapse once the vacuum energy is negative.
- [Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link) — hilltop quintessence as the explanation the program implements.
- [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) — the equation of state w(z) that the release fits.
- [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase) — τ's periodic potential, compared with quintessence in general.
- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — the equation of state and the thawing class that row 4 tests.
- [Row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion) — recollapse when the vacuum energy turns negative.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the program's potential, the thawing corridor, the state of the fits and the negative-minimum fits; §13 row 4 for the standard expectation w ≡ −1
- `papers/broken-born-checkpoint-v2.md` refs [19]–[21] — the cited fits and the DESI release (live-searched)
- `notes/broken-born-theory.md` §3 — the action S_τ with a canonical kinetic term
- `notes/broken-born-theory.md` §7 items 2–3 — hilltop initial conditions, "the standard thawing corridor", the fits with a negative minimum and the 93.8% figure (#1 only)
- `notes/broken-born-program-v1.md` §8 — the same fits, marked "[T — refresh citations before publication]"
