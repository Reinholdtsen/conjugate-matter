---
title: "DESI baryon acoustic oscillations"
weight: 30
status: established
description: "The Dark Energy Spectroscopic Instrument's baryon-acoustic-oscillation survey, its data releases DR1–DR3, and how w(z) is inferred from distances rather than observed."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md ref [21]"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §7"
  - "CLAUDE.md 'Since the handoff'"
---

*The Dark Energy Spectroscopic Instrument (DESI) is a survey that measures the redshifts of galaxies and quasars in order to map how the universe has expanded over a long span of its history. Its main tool is baryon acoustic oscillations (BAO): sound waves in the hot plasma of the early universe left a preferred separation between concentrations of matter, a fixed length that serves as a ruler at every later epoch. In Fourier terms the imprint is a single bump in the correlation between galaxy positions and a series of wiggles in its transform, the power spectrum. Measuring the ruler's apparent size at different redshifts gives distances, and the dark-energy equation of state is inferred from those distances by fitting a model; it is not observed directly. DESI's data releases are the external clock for the program's dark-energy sector.*

**Status:** Established — [T] — survey physics, written here from general knowledge; the release the program cites is live-searched [21S] (#11 §10).

## Key facts

- **The ruler [T].** The preferred separation is the sound horizon, the distance a sound wave in the photon–baryon plasma could travel before the plasma released its light. Its length is set by early-universe physics and can be calibrated with the cosmic microwave background (CMB); the survey measures it in galaxy clustering both across and along the line of sight.
- **From distances to w(z) [T].** BAO distances, combined with the CMB and with supernova distances, constrain the expansion history, and a dark-energy model, such as the w₀–wₐ form described on [quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence), is then fitted to them. #11 §10: "w(z) is inferred from distances rather than observed, as [21S] also notes."
- **Data Release 2 [S].** DESI Collaboration (M. Abdul-Karim et al.), "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," arXiv:2503.14738 (2025), #11 ref [21S]. What it means for the program is on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).
- **Earlier readings, superseded.** Before the crossing in Data Release 2 was taken into account, the handoff called the framework "Consistent with DESI DR1/DR2 drift hints" (`HANDOFF.md` §2), DR1 being Data Release 1, and the lab notebook wrote that hilltop and axion potentials "have been fit directly to DESI DR1/DR2 by the collaboration and others" (#1 §7 item 2). The current reading is that the dark-energy sector is "under real pressure" (root `CLAUDE.md`).
- **Data Release 3.** The handoff gives DR3 as "expected late 2026" and calls it the "External clock" (`HANDOFF.md` §2); #11 §10: "DR3 is the decisive test (§13, row 4)". See [row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift).

## Used by

- [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) — the release that put the dark-energy sector under pressure.
- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — the fits that compare τ-type models with the data.
- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — the test that Data Release 3 decides.
- [The turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce) — founding supposition 7 is "live at DESI DR3".

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — inference from distances; DR3 as the decisive test
- `papers/broken-born-checkpoint-v2.md` ref [21] — DESI DR2 Results II (live-searched)
- `HANDOFF.md` §2 — the earlier reading and the external clock
- `notes/broken-born-theory.md` §7 item 2 — fits of hilltop and axion potentials to DR1 and DR2
- `CLAUDE.md` 'Since the handoff' — "under real pressure ahead of DR3"
