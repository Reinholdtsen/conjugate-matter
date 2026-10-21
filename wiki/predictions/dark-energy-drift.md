---
title: "Row 4: thawing dark energy, never phantom"
weight: 50
status: alive
description: "Thawing with w₀ > −1, wₐ < 0, never phantom, the drift persisting in DESI DR3: a constant −1 kills the τ sector, a robust intrinsic w < −1 kills the framework, and DR2 already leans against it."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Rulings' item 11"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "popsci/angle-of-the-mirror.md 'The referee is already on the field'"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*Row 4 is the program's prediction for how dark energy, the cause of the accelerating cosmic expansion, changes over time. The program identifies dark energy with [τ](/wiki/cosmology/dark-energy/tau-quintessence), the angle that locates the vacuum's choice of polarization on a circle; τ has a periodic potential and starts near its maximum, a setup called hilltop quintessence. Such a field makes dark energy weaken slowly ("thaw") and keeps its equation of state w at or above −1, the value of a cosmological constant, so it can never enter the "phantom" regime w < −1. The test is the Dark Energy Spectroscopic Instrument (DESI): its Data Release 3 (DR3), expected in late 2026, is the decisive one, and its Data Release 2 (DR2) already favors a phantom phase in the past, so the sector is under real pressure.*

**Status:** Alive, under pressure — [D + T] (#11 §10), with w ≥ −1 [D] in the lab notebook (#1 §7) — DESI DR2's phantom crossing stands against the strict w ≥ −1 (#11 §10; accepted as round-3 ruling 11; root `CLAUDE.md`: "under real pressure ahead of DR3"); not machine-checked.

## Key facts

- **The row** ([checkpoint #11](/wiki/history/documents/checkpoint) §13). Observable: "Dark energy w(z)". Standard expectation: "w ≡ −1". Requirement: "Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3". Killed by: "DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) — DR2 already favors a crossing above z ≈ 0.4 (§10)". Here w(z) is dark energy's equation of state as a function of redshift z, and w₀, wₐ describe its present value and its evolution ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence)).
- **The model** (#11 §10, [D + T]): "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1 + w₀); two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint." See [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase) and [the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint).
- **Why never phantom** ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §7 item 1, [D]): "τ is a canonical scalar; the null energy condition holds; phantom crossing is impossible. Any robust measurement of w < −1 (as an intrinsic equation of state, not an artifact of an assumed ΛCDM background) falsifies this sector outright." See [the no-phantom bound](/wiki/cosmology/dark-energy/no-phantom-bound) and [the phantom divide](/wiki/cosmology/dark-energy/phantom-divide).
- **Under pressure** (#11 §10, added in v2.1). DESI DR2 reports that in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4", and that this preference "is thus rather independent of parametrization choices made in the analysis" [21S]. "The framework's strict w ≥ −1 therefore stands against the direct reading of the data. It survives on two points: non-phantom quintessence fits remain compatible [19S], and w(z) is inferred from distances rather than observed, as [21S] also notes." See [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) and [DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi).
- **Three outcomes** (`HANDOFF.md` §2, "External clock"): DR3 is "three-year data, expected late 2026"; "robust constant w = −1 kills the τ sector; robust intrinsic w < −1 kills the framework outright; continued thawing drift keeps it alive", a survival shared with other models of dynamical dark energy. The journey article (#10) calls these "Three doors".
- **Superseded readings.** `HANDOFF.md` §2 called the sector consistent with the drift hints of DESI's first two data releases, and v1 (#9 §8), the journey article (#10) and the italic opening of #11 §10 itself describe DESI's hints as exactly the drift the sector requires. The technical record of #11 §10 and the root `CLAUDE.md` replace those readings.
- **Popsci-only: "constant is impossible".** The destination article (#12) states "Decreasing is required; phantom is impossible; constant is impossible" and "The framework survives only the first outcome." The record differs: in #11's row a constant −1 kills only the τ sector, and #10 agrees ("Constant kills the theory's heart. Phantom kills it outright."). The popular articles are never a source for a claim's status ([Conjectures: chat-only and popsci-only claims](/wiki/status/conjectures)).
- **Exposure.** #11 §15 lists "DESI DR2's phantom crossing against §10's strict w ≥ −1" among the degeneration risks, and includes row 4 in the near-term falsification exposure (rows 1, 4, 7). The long-horizon consequence is [row 5, the fate of the expansion](/wiki/predictions/fate-of-expansion).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 4 — the row; §10 for the model, its tags and the "Under pressure (v2.1)" paragraph; §15 for the exposure and the degeneration risk
- `CLAUDE.md` 'Since the handoff' — "under real pressure ahead of DR3"
- `review/round3-adjudication.md` 'Rulings' item 11 — the DR2 finding, accepted
- `HANDOFF.md` §2 — the external clock and the three outcomes; its "consistent" reading is superseded
- `notes/broken-born-theory.md` §7 — the no-phantom argument [D] and the thawing shape
- `notes/broken-born-program-v1.md` §8, §9 — v1's reading of DESI (superseded) and its row 4
- `popsci/angle-of-the-mirror.md` 'The referee is already on the field' and `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — "three doors" and the popsci-only "constant is impossible"; not status sources
