---
title: "Quintessence and the equation of state"
weight: 10
status: established
description: "Dynamical dark energy from a slowly evolving scalar field: the equation of state w, thawing versus freezing, hilltop and axion-like potentials, the CPL w₀–wₐ parametrization, and recollapse when the vacuum energy turns negative."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md refs [19]–[21]"
  - "notes/broken-born-theory.md §7"
---

*Quintessence is dark energy made of a scalar field, a quantity with a single value at each point of space, whose energy density changes slowly as the universe expands instead of staying fixed as a cosmological constant's does. Its behaviour is summarized by the equation of state w, the ratio of pressure to energy density: a cosmological constant has w = −1 exactly, and a field whose energy is mostly potential energy comes close to that value. In a thawing model the expansion holds the field nearly still at early times and it starts to change late, so w begins near −1 and rises. The program's dark-energy field τ is a model of this kind, with the periodic potential of an axion-like field.*

**Status:** Established — [T] — textbook cosmology, written here from general knowledge; the fits #11 cites are live-searched [S] (#11 refs [19]–[21]).

## Key facts

- **The equation of state [T].** For a uniform scalar field φ with potential V, the energy density is ρ = ½φ̇² + V and the pressure is p = ½φ̇² − V, so w = p/ρ. When V ≥ 0, w lies between −1 (all potential energy) and +1 (all kinetic energy, the stiff fluid of [Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)).
- **Thawing and freezing [T].** In a thawing model the expansion rate holds the field nearly fixed at early times, with w ≈ −1, and the field departs from it late; in a freezing model the field evolves early and slows toward w = −1 (the classification of Caldwell and Linder †). The lab notebook's version: "Hilltop initial conditions give w ≈ −1 in the past, rising now" (#1 §7 item 2).
- **Hilltop and axion-like potentials [T].** A hilltop model starts near a maximum of its potential. An axion-like, or pseudo-Nambu–Goldstone, field has a periodic potential of the form V₀[1 + cos(φ/f)]. The program's choice is "V = V₀[1 + cos(τ/f)]" (#11 §10); see [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence).
- **The w₀–wₐ parametrization [T].** The Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a) summarizes a drifting w by its present value w₀ and its slope wₐ; a thawing field has w₀ > −1 and wₐ < 0. The program uses the "thawing corridor wₐ ≈ −1.5(1 + w₀)" (#11 §10), which #1 §7 item 2 calls "the standard thawing corridor".
- **Recollapse [T].** If the total vacuum energy becomes negative, the expansion of a flat universe halts and reverses; a field that settles toward a negative minimum of its potential produces an anti-de Sitter phase and collapse. #11 §10 cites "high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]". Whether the program's own potential can go negative is open: [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign).
- **Fits to current data [S].** #11 §10: "compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ)". The works cited are Gialamas, Hütsi, Raidal, Urrutia, Vasar and Veermäe, "Quintessence and phantoms in light of DESI 2025," arXiv:2506.21542 [19S], and Ureña-López et al. (DESI), an axion-quintessence analysis of DESI data, arXiv:2503.20178 [20S]. DESI is the Dark Energy Spectroscopic Instrument ([DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi)).

## Used by

- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — τ is a thawing hilltop field with an axion-like potential.
- [The no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) — w ≥ −1 for a canonical scalar.
- [The dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint) — w₀, wₐ and the turnaround time as functions of the model's free numbers.
- [The turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce) — recollapse once the vacuum energy is negative.
- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — the w₀–wₐ test.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the program's potential, the thawing corridor and the state of the fits
- `papers/broken-born-checkpoint-v2.md` refs [19]–[21] — the cited fits and the DESI release (live-searched)
- `notes/broken-born-theory.md` §7 items 2–3 — hilltop initial conditions, "the standard thawing corridor", the negative-minimum fits
