---
title: "Obituary: velocity-space granularity in halos (old row 3)"
weight: 80
status: dead
description: "The lab notebook's flagship discriminant — O(10) macro-streams of width ~v* perturbing cold stellar streams — permanently withdrawn on both islands."
sources:
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure'"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/debt3b-wave-island.md 'Standing results'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §11 item 3"
  - "notes/broken-born-theory.md §12"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-program-v1.md §9"
---

*Velocity-space granularity was the [lab notebook](/wiki/history/documents/lab-notebook)'s prediction that the dark matter of a relaxed galaxy halo, such as the Milky Way's, is split into of order ten broad streams, each with its own velocity and coherent over kiloparsec distances, and that their gravity leaves correlated ripples along thin streams of stars. It was row 3 of the notebook's [prediction table](/wiki/predictions/table-history) and one of its three flagship discriminants. It rested on the [founding image](/wiki/dark-matter/momentum-clumping/founding-image) of velocity clumping, so when Debt 3 showed that clumping is impossible for particle dark matter and never mandatory for wave dark matter, the row was withdrawn permanently, on both islands. The current table's row 3 is a different prediction, [the island discriminant](/wiki/predictions/island-discriminant).*

**Status:** Dead — "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands" (`notes/debt3c-ufd-endpoint.md`); #11 §13 lists "velocity-space granularity in halos" under "Withdrawn with cause". Untagged in the sources. Killed with the founding image by Debt 3, whose summary is [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem). Home section: [momentum clumping](/wiki/dark-matter/momentum-clumping); listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

### The row as written

Row 3 of the lab notebook's prediction table (`notes/broken-born-theory.md` §9), in the notebook's columns:

| Column | Row 3 |
|---|---|
| Observable | "DM velocity-space structure in relaxed halos" |
| Standard expectation | "Smooth f(v) + sub-percent accretion streams" |
| Requirement of the framework | "Fragmentation into O(10) macro-streams of width ~v\*, coherent over kpc; long-wavelength correlated perturbations of cold stellar streams (GD-1, Pal 5) vs. ΛCDM's localized subhalo gaps" |
| Kill condition | "Gaia DR4/Rubin stream power spectra consistent with smooth-halo + point-subhalo model only" |

DM is dark matter, ΛCDM the standard cosmology with a cosmological constant and cold dark matter, and v\* the width of the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), about 120 km/s in the notebook. Gaia DR4 is the fourth data release (Data Release 4) of the Gaia astrometry mission, and Rubin is the Vera C. Rubin Observatory's survey [T].

### What it would have meant for observations

Cold stellar streams such as GD-1 and Pal 5 are thin trails of stars torn from star clusters by the Milky Way's tides. Their density along the trail is sensitive to the gravity of the dark matter they pass through [T] ([halo-substructure probes](/wiki/dark-matter/halo-astrophysics/halo-substructure)).

- **In the standard picture**, a small dark subhalo flying past a stream leaves a localized gap, so the stream's density fluctuations come from a population of compact, point-like perturbers [T].
- **In the notebook's picture**, the halo's dark matter would be organized into about ten macro-streams, each spread through space but narrow in velocity. Their gravity would vary smoothly over kiloparsecs, so the perturbations of a stellar stream would be correlated over long stretches, not localized.

A stream's power spectrum, the strength of its density fluctuations as a function of their wavelength along the stream, would separate the two: excess power at long wavelengths for macro-streams, a gap-dominated spectrum for subhalos. A spectrum fully explained by a smooth halo plus point subhalos would have killed the row.

### Its basis

The row rested on §5.2 of the notebook, tagged "[D at mean-field level; O beyond]": with an attractive gated interaction, "a smooth Maxwellian f(v) is unstable to fragmentation into **discrete velocity streams of width Δv ~ v\***, each spatially delocalized and internally coherent across kiloparsecs". The notebook saw this as "the Jeans problem *with the roles of x and v exchanged*" ([the Jeans instability](/wiki/dark-matter/momentum-clumping/vlasov-stability#the-static-threshold-and-the-jeans-instability); [the founding image](/wiki/dark-matter/momentum-clumping/founding-image)).

### Its standing

The notebook ranked it among its strongest predictions: "Rows 1, 3, and 7 are the flagship discriminants: no mainstream framework predicts an exponential scattering cliff, gravitationally-detectable macro-granularity of the local velocity distribution, *and* a guaranteed-null direct-detection program." (§9). Its one-paragraph summary lists "velocity-space granularity" among the dark sector's signatures (§12), and its parameter count credits the conjugate-matter parameters σ₀/m and v\* with the "stream granularity scale" (§10).

## How it was tested

The notebook named the missing step and tied it to this row. Open problem 3: "Stream-instability growth rate γ vs. orbital phase-mixing: determines whether Prediction 3's granularity survives in Milky-Way-like halos." (§11). Debt 3 computed it, first for classical particles and then for wave dark matter ([the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)).

## Why it failed

### Particle island: no streams form

For dark-matter particles of MeV to GeV mass, [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) for streams fails at the [scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) by a ratio of about 10⁻³¹ in the Milky Way's halo near the Sun and 10⁻²⁸ in dwarf cores (3a). Below threshold the velocity distribution is stable, and collisions only drive it toward a Maxwellian. 3a withdrew the row on this island: "Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**, and with them the mechanism-level linkage claimed between them." (3a, 'Consequences for the predictions table').

### Wave island: never mandatory

Collective behaviour survives only for very light, wave-like dark matter, on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) ([the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem)). There 3b asked whether the gated [condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) beats orbital stirring in each environment.

- **Under [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)**, where the coupling is fixed by dwarf cores, streams lose in Milky-Way-like halos. 3b's table gives the ratio of condensation rate to stirring rate R_X as "~10⁻²" in the Milky Way's inner 1 kpc and "~4×10⁻⁵" at the solar circle, and its verdict is "streams lose everywhere by 10²–10⁴ — *except ultra-faint dwarfs*". The granularity the row predicted, in the Milky Way, does not form. 3b kept a "surviving descendant of old rows 3–4", a signature confined to ultra-faint dwarf galaxies, and 3c showed that this endpoint drains those galaxies of dark matter, which observation excludes.
- **Under [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b)**, where the coupling is free, streams are possible across a window ten orders of magnitude wide but are not required: "streams are *tunable*, not mandatory". 3b: "on this branch the granularity prediction is no longer a novel *requirement* of the program, only an option — a degeneration flag."

3b's interim standing: "Row 3 as written (Gaia/GD-1 granularity in MW-like halos) is dead on both islands as a *mandatory* signature." (MW: Milky Way.)

### The permanent withdrawal

3c closed Debt 3: "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands." The notebook's addendum: "Rows 3–4 are struck from §9 permanently" (`notes/broken-born-theory.md`, 'Addendum (v0.2)').

## What survives

Nothing of the row as a prediction. Under Scenario B, velocity granularity in a halo remains allowed at a tunable strength, which #11 §15 counts among the program's [degeneration risks](/wiki/method/lakatosian-methodology), not among its predictions. Stellar-stream gaps remain a standard probe of dark-matter substructure, with no program-specific signal attached ([halo-substructure probes](/wiki/dark-matter/halo-astrophysics/halo-substructure)).

The row's number went to a new prediction. The notebook's addendum: "A new row replaces them: **cliff-sharpness island discriminant**". In #9 and #11, row 3 is [the island discriminant](/wiki/predictions/island-discriminant), which the checkpoint lists as "(not previously posed)" (#11 §13). It is part of Debt 3's salvage (#11 §9).

## In the later tables

- #9 §9: "Withdrawn with cause, permanently: velocity-space granularity in halos; Fornax friction suppression (rows 3–4 of earlier versions; obituary in §7)."
- #11 §13: "Withdrawn with cause: velocity-space granularity in halos; Fornax friction suppression (obituary §9); superheavy-soliton dark matter (obituary §12)." The last item is [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary).

The calc notes 3a–3c number the rows as the notebook does. Since #9 and #11 reuse the numbers for other rows, this wiki calls the notebook's row "old row 3" ([history of the predictions table](/wiki/predictions/table-history)). Its companion is [old row 4, Fornax friction suppression](/wiki/dark-matter/momentum-clumping/fornax-friction).

## Sources

- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — the permanent withdrawal
- `papers/broken-born-checkpoint-v2.md` §13 — "Withdrawn with cause" and the new row 3; §9 — the obituary and the salvage
- `notes/debt3a-stream-stability.md` 'Numbers at the scattering benchmark', 'Consequences for the predictions table' — the shortfall and the withdrawal on the particle island
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — the environment table, the descendant and the degeneration flag; 'Standing results after Chunks A+B' — dead on both islands as a mandatory signature
- `notes/broken-born-theory.md` §9 — the row as written and its flagship status; §5.2 — its basis; §10 — the parameter count; §11 item 3 — the open problem; §12 — the summary; 'Addendum (v0.2)' — the strike and the replacement row
- `notes/broken-born-program-v1.md` §9 — the withdrawal in v1's renumbered table
