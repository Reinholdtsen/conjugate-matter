---
title: "DESI baryon acoustic oscillations"
weight: 30
status: established
description: "The Dark Energy Spectroscopic Instrument's baryon-acoustic-oscillation survey: the sound-horizon ruler, how distances become a fitted w(z) rather than an observed one, the data releases DR1–DR3, and the survey's role as the program's external clock."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md ref [21]"
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md App. A item 7"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §7"
  - "CLAUDE.md 'Since the handoff'"
---

*The Dark Energy Spectroscopic Instrument (DESI) is a survey that measures the redshifts of galaxies and quasars in order to map how the universe has expanded over a long span of its history. Its main tool is baryon acoustic oscillations (BAO): sound waves in the hot plasma of the early universe left a preferred separation between concentrations of matter, a fixed length that serves as a ruler at every later epoch. In Fourier terms the imprint is a single bump in the correlation between galaxy positions and a series of wiggles in its transform, the power spectrum. Measuring the ruler's apparent size at different redshifts gives distances, and the dark-energy equation of state is inferred from those distances by fitting a model; it is not observed directly. DESI's data releases are the external clock for the program's dark-energy sector, and its second release already leans against the program's requirement.*

**Status:** Established — [T] — survey physics, written here from general knowledge; the release the program cites is live-searched [21S] ([checkpoint #11](/wiki/history/documents/checkpoint) §10).

## The survey [T]

DESI is a spectroscopic survey: it records the spectra of galaxies and quasars and reads off their redshifts, z, the fractional stretching of their light by the expansion since it was emitted. A redshift and a position on the sky place an object in three dimensions, so the survey produces a map of the large-scale distribution of matter over a range of redshifts. The popular articles describe the scale as "tens of millions of galaxies" (#10, 'The referee is already on the field'; [the popular articles](/wiki/history/documents/popular-articles)).

The map is used to measure distances by a standard ruler, the baryon acoustic oscillation scale.

## The ruler: baryon acoustic oscillations [T]

### Sound in the early plasma

Before the universe was cool enough for neutral atoms to form, photons and baryons (ordinary matter) were held together by scattering as a single plasma with a high sound speed. A small excess of matter at one point drove a spherical sound wave outward through the plasma, while the [dark matter](/wiki/dark-matter), which does not feel the photon pressure, stayed behind at the centre. When the photons decoupled from the baryons, the wave stopped: the baryons were left in a thin shell at the distance the sound had travelled, the sound horizon r_d (Eisenstein and Hu †; Peebles and Yu †; Sunyaev and Zeldovich †).

Matter later fell into both the central excess and the shell. Summed over countless such sources, the result is a small excess in the number of galaxy pairs separated by r_d (Eisenstein et al. † and Cole et al. †, the first detections).

### The ruler in Fourier space

The imprint has a simple Fourier description. In the two-point correlation function of galaxy positions, the probability of finding two galaxies at separation r, it is a single bump at r = r_d. The power spectrum P(k) is the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of the correlation function, and the transform of a thin spherical shell of radius r_d is an oscillation in k of the form sin(k r_d)/(k r_d). The same length therefore appears as a bump in position space and as a series of wiggles in wavenumber, as an echo, a delayed copy of a signal, appears as a ripple in the signal's spectrum. Surveys fit either form.

### Calibration

The length r_d is fixed by early-universe physics: the sound speed of the plasma and the time at which it ended, which depend on the densities of baryons and of matter. Measurements of the cosmic microwave background (CMB), the light released at that time, determine those densities and so calibrate the ruler. A BAO survey can also be analysed without that calibration, in which case it measures distances in units of r_d [T].

## From the ruler to distances [T]

At redshift z the ruler is seen in two orientations.

- **Across the line of sight**, it subtends an angle θ = r_d/D_M(z), where D_M is the transverse comoving distance. The survey measures D_M/r_d.
- **Along the line of sight**, it spans a redshift interval Δz = r_d H(z)/c, where H(z) is the expansion rate at that redshift. The survey measures D_H/r_d, with D_H = c/H(z).

When the two directions cannot be separated, an average of them is quoted. Each redshift bin of the survey gives one or two such ratios.

## From distances to w(z) [T]

In a spatially flat universe the distances are integrals of the expansion history, D_M(z) = c∫dz′/H(z′) from 0 to z, and H(z) depends on the densities of matter and of dark energy. The dark-energy density in turn depends on its equation of state w(z) through the continuity equation ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence)). A measurement of distances therefore constrains w(z) only through a model:

1. choose a form for w(z), such as the w₀–wₐ form w(a) = w₀ + wₐ(1 − a) ([the CPL parametrization](/wiki/cosmology/dark-energy/cpl-parametrization));
2. compute the distances it predicts, together with the other parameters (the matter density, r_d);
3. fit to the BAO ratios, usually combined with the CMB, which fixes the early universe and r_d, and with supernova distances, which fix the shape of the expansion at low redshift.

The result is a posterior distribution for the parameters of the chosen form. Different forms and different combinations of data can give different preferred w(z), and the parameters are correlated with one another. #11 §10 makes the point that matters for the program: "w(z) is inferred from distances rather than observed, as [21S] also notes." What the latest release infers, and how strongly the inference holds across choices of form, is on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).

## The data releases

- **Data Release 1 (DR1).** The documents mention it only alongside the second: the [handoff](/wiki/history/documents/handoff) called the framework "Consistent with DESI DR1/DR2 drift hints" (`HANDOFF.md` §2), and the [lab notebook](/wiki/history/documents/lab-notebook) says hilltop and axion potentials "have been fit directly to DESI DR1/DR2 by the collaboration and others" (#1 §7 item 2). No DR1 paper is in #11's reference list.
- **Data Release 2 (DR2).** #11's reference [21][S]: DESI Collaboration (M. Abdul-Karim et al.), "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," arXiv:2503.14738 (2025). It is the release that reports a crossing of w = −1, below −1 above z ≃ 0.4 (#11 §10). The lab notebook's citation "DESI 2025" [T] (#1 §7 item 2) carries no arXiv number, and no document says whether it is the same paper.
- **Data Release 3 (DR3).** The handoff gives it as "DESI DR3 (three-year data, expected late 2026)" and calls it the "External clock" (`HANDOFF.md` §2). The "three-year" label is listed as a suspected slip in the source (`review/wiki-build-flags.md` item 26); the wiki quotes it as written. #11 §10: "DR3 is the decisive test (§13, row 4)."

## How the program uses the survey

The survey is the external test of the program's dark-energy sector. The sector's requirement, a thawing w(z) that never falls below −1, is [row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) of #11 §13, and its kill conditions are stated in terms of DESI: "DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) — DR2 already favors a crossing above z ≈ 0.4 (§10)" (#11 §13 row 4). #11 §15 names the survey as the program's nearest trial: "Its nearest trial is DESI's next release, and the current release already leans against its dark-energy prediction (§10)."

The reading of the survey has changed. Before the [round-3](/wiki/method/review/round-3) review the documents read DESI's results as support; since #11 v2.1 the second release is recorded as a phantom crossing that stands against the program's bound, and the root `CLAUDE.md` says "The dark-energy sector is under real pressure ahead of DR3" ('Since the handoff'). The earlier readings and the change are on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing#superseded-the-earlier-readings-of-desi); the bound is [the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound).

## Used by

- [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) — the release that put the dark-energy sector under pressure.
- [The no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) — "w(z) is inferred from distances rather than observed".
- [The dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint) — w₀ and wₐ, two of its three observables, measured from survey distances.
- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — the fits that compare τ-type models with the data.
- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — the test that Data Release 3 decides.
- [The turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce) — [founding supposition 7](/wiki/program/founding-suppositions) is "live at DESI DR3" (#11 App. A item 7).

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — inference from distances; DR2's crossing; DR3 as the decisive test
- `papers/broken-born-checkpoint-v2.md` ref [21] — DESI DR2 Results II (live-searched)
- `papers/broken-born-checkpoint-v2.md` §13 row 4 — the kill conditions in terms of DESI; §15 — "nearest trial" and "already leans against"; App. A item 7 — "live at DESI DR3"
- `HANDOFF.md` §2 — the earlier reading and the external clock
- `notes/broken-born-theory.md` §7 item 2 — fits of hilltop and axion potentials to DR1 and DR2; "DESI 2025"
- `CLAUDE.md` 'Since the handoff' — "under real pressure ahead of DR3"
