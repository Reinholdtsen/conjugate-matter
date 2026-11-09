---
title: "Under review: velocity-space granularity in halos (old row 3)"
weight: 80
status: under-review
description: "The lab notebook's flagship discriminant — O(10) macro-streams of width ~v* perturbing cold stellar streams — withdrawn on both islands, 'permanently' in calc note #4's words, and under review."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "notes/ufd-endpoint.md 'Verdict and closure'"
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "notes/stream-stability.md 'Consequences for the predictions table'"
  - "notes/stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/wave-island.md 'Standing results'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §5.2"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §11 item 3"
  - "notes/broken-born-theory.md §12"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-program-v1.md §9"
---

*Velocity-space granularity was the [lab notebook](../../history/documents/lab-notebook.md)'s prediction that the dark matter of a relaxed galaxy halo, such as the Milky Way's, is split into of order ten broad streams, each with its own velocity and coherent over kiloparsec distances, and that their gravity leaves correlated ripples along thin streams of stars. It was row 3 of the notebook's [prediction table](../../predictions/table-history.md) and one of its three flagship discriminants. It rested on the [founding image](founding-image.md) of velocity clumping. The calculations of [the clumping problem](../../history/main-problems.md) used the program's contact-range interaction, which acts only over microscopic distances. They found that the criterion for clumping fails for particle dark matter ("forbidden (particles)", in [the net theorem](net-theorem.md)'s words) and that clumping is never mandatory for wave dark matter, so the row was withdrawn on both islands, the two mass ranges in which dark matter behaves as particles or as a wave. The founding image itself is P.R.'s open conjecture. The current table's row 3 is a different prediction, [the island discriminant](../../predictions/island-discriminant.md).*

**Status:** Under review — the evidence below weighs against it, and its final status awaits review. "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands" ([`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md); row 4 is [Fornax friction suppression](fornax-friction.md)); [#11](../../history/documents/checkpoint.md) [§13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) lists "velocity-space granularity in halos" among the rows withdrawn and under review. Untagged in the sources. It was withdrawn on the results of the clumping problem, which tested the founding image, P.R.'s open conjecture ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)); [the net theorem](net-theorem.md) summarizes those results. Home section: [momentum clumping](_index.md); listed in [claims under review](../../status/under-review.md).

## What was claimed

### The row as written

Row 3 of the lab notebook's prediction table ([`notes/broken-born-theory.md` §9](../../../notes/broken-born-theory.md#9-predictions)), in the notebook's columns:

| Column | Row 3 |
|---|---|
| Observable | "DM velocity-space structure in relaxed halos" |
| Standard expectation | "Smooth f(v) + sub-percent accretion streams" |
| Requirement of the framework | "Fragmentation into O(10) macro-streams of width ~v\*, coherent over kpc; long-wavelength correlated perturbations of cold stellar streams (GD-1, Pal 5) vs. ΛCDM's localized subhalo gaps" |
| Kill condition | "Gaia DR4/Rubin stream power spectra consistent with smooth-halo + point-subhalo model only" |

DM is dark matter, ΛCDM the [standard cosmology](../../cosmology/_index.md) with a [cosmological constant](../../cosmology/dark-energy/cosmological-constant.md) and cold dark matter, and v\* the width of the [velocity gate](../conjugate-matter/velocity-gate.md), about 120 km/s in the notebook. Gaia DR4 is the fourth data release (Data Release 4) of the Gaia astrometry mission, and Rubin is the Vera C. Rubin Observatory's survey [T].

### What it would have meant for observations

Cold stellar streams such as GD-1 and Pal 5 are thin trails of stars torn from star clusters by the Milky Way's tides. Their density along the trail is sensitive to the gravity of the dark matter they pass through [T] ([halo-substructure probes](../halo-astrophysics/halo-substructure.md)).

- **In the standard picture**, a small dark subhalo flying past a stream leaves a localized gap, so the stream's density fluctuations come from a population of compact, point-like perturbers [T].
- **In the notebook's picture**, the halo's dark matter would be organized into about ten macro-streams, each spread through space but narrow in velocity. Their gravity would vary smoothly over kiloparsecs, so the perturbations of a stellar stream would be correlated over long stretches, not localized.

A stream's power spectrum, the strength of its density fluctuations as a function of their wavelength along the stream, would separate the two: excess power at long wavelengths for macro-streams, a gap-dominated spectrum for subhalos. A spectrum fully explained by a smooth halo plus point subhalos would have killed the row.

### Its basis

The row rested on [§5.2](../../../notes/broken-born-theory.md#52-collective-behavior-clumping-in-momentum-space-d-at-mean-field-level-o-beyond) of the notebook, tagged "[D at mean-field level; O beyond]": with an attractive gated interaction, "a smooth Maxwellian f(v) is unstable to fragmentation into **discrete velocity streams of width Δv ~ v\***, each spatially delocalized and internally coherent across kiloparsecs". The notebook saw this as "the Jeans problem *with the roles of x and v exchanged*" ([the Jeans instability](vlasov-stability.md#the-static-threshold-and-the-jeans-instability); [the founding image](founding-image.md)).

### Its standing

The notebook ranked it among its strongest predictions: "Rows 1, 3, and 7 are the flagship discriminants: no mainstream framework predicts an exponential scattering cliff, gravitationally-detectable macro-granularity of the local velocity distribution, *and* a guaranteed-null direct-detection program." (§9). Its one-paragraph summary lists "velocity-space granularity" among the dark sector's signatures (§12), and its parameter count credits the conjugate-matter parameters σ₀/m and v\* with the "stream granularity scale" (§10).

## How it was tested

The notebook named the missing step and tied it to this row. Open problem 3: "Stream-instability growth rate γ vs. orbital phase-mixing: determines whether Prediction 3's granularity survives in Milky-Way-like halos." (§11). The clumping problem computed it, first for classical particles and then for wave dark matter ([the gated Vlasov model](gated-vlasov-model.md)).

## The evidence against it

### Particle island: no streams form

For dark-matter particles of MeV to GeV mass, [the mean-field criterion](instability-criterion.md) for streams fails at the [scattering benchmark](../conjugate-matter/benchmark.md) by a ratio of about 10⁻³¹ in the Milky Way's halo near the Sun and 10⁻²⁸ in dwarf cores ([#2](../../history/documents/clumping-notes.md)). Below threshold the velocity distribution is stable, and collisions only drive it toward a Maxwellian. [#2](../../../notes/stream-stability.md) withdrew the row on this island: "Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**, and with them the mechanism-level linkage claimed between them." (#2, 'Consequences for the predictions table').

### Wave island: never mandatory

Collective behaviour survives only for very light, wave-like dark matter, on the [wave island](wave-island/_index.md) ([the classicality theorem](classicality-theorem.md)). There [#3](../../../notes/wave-island.md) asked whether the gated [condensation rate](wave-island/condensation-rate.md) beats orbital stirring in each environment.

- **Under [Scenario A](wave-island/scenario-a.md)**, where the coupling is fixed by dwarf cores, streams lose in Milky-Way-like halos. #3's table gives the ratio of condensation rate to stirring rate R_X as "~10⁻²" in the Milky Way's inner 1 kpc and "~4×10⁻⁵" at the solar circle, and its verdict is "streams lose everywhere by 10²–10⁴ — *except ultra-faint dwarfs*". The granularity the row predicted, in the Milky Way, does not form. #3 kept a "surviving descendant of old rows 3–4", a signature confined to [ultra-faint dwarf galaxies](../halo-astrophysics/dwarf-galaxies.md), and [#4](../../../notes/ufd-endpoint.md) showed that this endpoint drains those galaxies of dark matter, which observation excludes (Scenario A is under review).
- **Under [Scenario B](wave-island/scenario-b.md)**, where the coupling is free, streams are possible across a window ten orders of magnitude wide but are not required: "streams are *tunable*, not mandatory". #3: "on this branch the granularity prediction is no longer a novel *requirement* of the program, only an option — a degeneration flag."

#3's interim standing: row 3 as written, the Gaia/GD-1 granularity in Milky-Way-like halos, fails on both islands as a *mandatory* signature.

### The withdrawal

#4 closed the clumping problem. In its words, rows 3 and 4 of the predictions table "are permanently withdrawn, on both islands". The notebook's addendum: "Rows 3–4 are struck from §9 permanently" ([`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md), 'Addendum (v0.2)').

## What stands

The row is withdrawn as a prediction and is under review. Under Scenario B, velocity granularity in a halo remains allowed at a tunable strength, which [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) counts among the program's [degeneration risks](../../method/lakatosian-methodology.md), not among its predictions. Stellar-stream gaps remain a standard probe of dark-matter substructure, with no program-specific signal attached ([halo-substructure probes](../halo-astrophysics/halo-substructure.md)).

The row's number went to a new prediction. The notebook's addendum: "A new row replaces them: **cliff-sharpness island discriminant**". In [#9](../../../notes/broken-born-program-v1.md) and #11, row 3 is [the island discriminant](../../predictions/island-discriminant.md), which the checkpoint lists as "(not previously posed)" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)). It is part of the clumping problem's salvage ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)).

## In the later tables

- [#9 §9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions) lists the row, with Fornax friction suppression, as "Withdrawn with cause, permanently" (rows 3–4 of earlier versions; the cause is in [#9 §7](../../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative)).
- [#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) lists the same two rows as withdrawn and under review. Its one withdrawal with cause is [#14's superheavy-soliton model](../candidates/soliton-candidate/obituary.md).

The calc notes #2–#4 number the rows as the notebook does. Since #9 and #11 reuse the numbers for other rows, this wiki calls the notebook's row "old row 3" ([history of the predictions table](../../predictions/table-history.md)). Its companion is [old row 4, Fornax friction suppression](fornax-friction.md).

## Sources

- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — velocity-space granularity in halos under review
- [`notes/ufd-endpoint.md`](../../../notes/ufd-endpoint.md) 'Verdict and closure of the clumping problem' — the withdrawal, "permanently withdrawn" in its words
- [`wiki/papers/broken-born-checkpoint-v2.md` §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the row, withdrawn and under review, and the new row 3; [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the tests and the salvage, and the founding image as P.R.'s open conjecture
- [`notes/stream-stability.md`](../../../notes/stream-stability.md) 'Numbers at the scattering benchmark', 'Consequences for the predictions table' — the shortfall and the withdrawal on the particle island
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'What pins g? Two scenarios' — the environment table, the descendant and the degeneration flag; 'Standing results after Chunks A+B' — the note's interim standing on row 3
- [`notes/broken-born-theory.md` §9](../../../notes/broken-born-theory.md#9-predictions) — the row as written and its flagship status; [§5.2](../../../notes/broken-born-theory.md#52-collective-behavior-clumping-in-momentum-space-d-at-mean-field-level-o-beyond) — its basis; [§10](../../../notes/broken-born-theory.md#10-parameter-count) — the parameter count; [§11 item 3](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity) — the open problem; [§12](../../../notes/broken-born-theory.md#12-one-paragraph-summary) — the summary; 'Addendum (v0.2)' — the strike and the replacement row
- [`notes/broken-born-program-v1.md` §9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions) — the withdrawal in v1's renumbered table
