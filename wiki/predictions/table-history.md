---
title: "History of the predictions table"
weight: 10
status: record
description: "From the lab notebook's ten rows through v1's ten to the checkpoint's eleven: renumbering, withdrawn rows, dropped details, and the per-sector parameter counts."
sources:
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-program-v1.md §0"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §12"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure of Debt 3'"
  - "notes/debt1a-iv-beta-coefficients.md §3"
---

*The predictions table is the program's list of observations that could kill it: for each observable it gives what standard physics expects, what the Broken-Born program requires, and the result that would end the claim. The table has had three versions: ten rows in [the lab notebook](/wiki/history/documents/lab-notebook) (#1 §9, v0.1), ten in the first consolidated paper (#9 §9, v1) and eleven in [the current checkpoint](/wiki/history/documents/checkpoint) (#11 §13). Between them, two rows were withdrawn when the program's own Debt-3 calculation killed velocity clumping, a diagnostic row took their place, the lead row softened from an exponential cliff to a knee, and the retired soliton candidate joined the list of withdrawn predictions. This page records those changes so that a row number in an older document can be read correctly.*

**Status:** Record — the tables themselves carry no provenance tags — #11 §13 is the current table; the tables of #1 §9 and #9 §9 are superseded and kept as the audit trail.

## Key facts

- **The form.** Every version gives each row an observable, a standard expectation, the framework's requirement and a kill condition. #9 §9 and #11 §13 open with "A theory is its list of ways to die"; #11 adds "updated". The current table is on [Predictions and kill conditions](/wiki/predictions).
- **v0.1** (#1 §9) had ten rows: σ_T(v), scattering anisotropy, velocity-space structure in halos, dynamical friction in dwarf cores, dark energy w(z), the fate of the expansion, direct detection and colliders, magnetic monopoles, photon dispersion and the early universe. "Rows 1, 3, and 7 are the flagship discriminants: no mainstream framework predicts an exponential scattering cliff, gravitationally-detectable macro-granularity of the local velocity distribution, *and* a guaranteed-null direct-detection program."
- **Debt 3 removed two rows.** After [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem), "Rows 3–4 are struck from §9 permanently" and "A new row replaces them: **cliff-sharpness island discriminant**" (#1 'Addendum (v0.2, post Debt-3)'). Calc note #4 closes Debt 3 with "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." The obituaries are [velocity-space granularity in halos (old row 3)](/wiki/dark-matter/momentum-clumping/velocity-granularity) and [Fornax friction suppression (old row 4)](/wiki/dark-matter/momentum-clumping/fornax-friction).
- **Row 1 softened.** Addendum v0.4 amends row 1: "the exponential cliff weakens to a sharp knee at v\* with tail shape (Gaussian vs rational) diagnosing the vertex completion; the knee's existence and location remain the robust prediction." The requirement "cliff at v\* ~ 120 km/s" became "Knee at v\* ~ 10² km/s", and the kill condition "v > 3v\*" became "v ≫ v\*" ([row 1](/wiki/predictions/self-interaction-knee)).
- **v1** (#9 §9) had ten rows: the island discriminant as row 3, dark energy and the fate of the expansion moved to rows 4 and 5, a new row 6 on gravitational waves, and rows 7–10 as before. Below the table: "Withdrawn with cause, permanently: velocity-space granularity in halos; Fornax friction suppression (rows 3–4 of earlier versions; obituary in §7)."
- **#11** (§13) has eleven rows. It adds row 11, "Dark-sector microstructure" ([particles or condensate](/wiki/predictions/dark-sector-microstructure)). Row 4 now records that the second data release of the Dark Energy Spectroscopic Instrument "already favors a crossing above z ≈ 0.4 (§10)"; row 7 now rests on both dark-sector candidates being decoupled from the Standard Model, with P4 taken strictly; row 8 is limited to monopoles "(ours)". The withdrawn list adds "superheavy-soliton dark matter (obituary §12)", the candidate retired in v2.1 ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).
- **Dropped details.** Between v0.1 and v1, row 10 lost its conditional step in the primordial gravitational-wave spectrum and its "CMB-S4 N_eff at ±0.03" probe of the curvature term, CMB-S4 being a cosmic microwave background experiment ([row 10](/wiki/predictions/early-universe-step)). Between v1 and #11, row 1 lost "tail shape = vertex diagnostic", row 2 "(halo relaxation morphology)", row 5 "after V(τ) < 0" and row 6 "massive X short-range". Whether the potential as written can go negative is an open point of [row 5](/wiki/predictions/fate-of-expansion).
- **Numbering.** The Debt-3 calc notes and #1 §9 use v0.1's numbers, in which row 3 is granularity, row 4 Fornax friction, row 5 dark energy and row 6 the fate of the expansion. This wiki uses #11's numbers and calls the withdrawn rows "old row 3" and "old row 4".

| Observable | v0.1 (#1 §9) | v1 (#9 §9) | #11 §13 |
|---|---|---|---|
| σ_T(v) across halo masses | 1 (cliff) | 1 (knee) | [1](/wiki/predictions/self-interaction-knee) |
| Scattering anisotropy | 2 | 2 | [2](/wiki/predictions/scattering-isotropy) |
| Velocity-space structure in relaxed halos | 3 | withdrawn | withdrawn |
| Dynamical friction in dwarf cores | 4 | withdrawn | withdrawn |
| Island discriminant | none (added by the v0.2 addendum, unnumbered) | 3 | [3](/wiki/predictions/island-discriminant) |
| Dark energy w(z) | 5 | 4 | [4](/wiki/predictions/dark-energy-drift) |
| Fate of expansion | 6 | 5 | [5](/wiki/predictions/fate-of-expansion) |
| Gravitational waves | none | 6 | [6](/wiki/predictions/massless-graviton) |
| Direct detection and colliders | 7 | 7 | [7](/wiki/predictions/direct-detection-null) |
| Magnetic monopoles | 8 | 8 | [8](/wiki/predictions/monopole-null) (ours) |
| Photon dispersion | 9 | 9 | [9](/wiki/predictions/photon-dispersion) |
| Early universe | 10 | 10 | [10](/wiki/predictions/early-universe-step) |
| Dark-sector microstructure | none | none | [11](/wiki/predictions/dark-sector-microstructure) |
| Superheavy-soliton dark matter | none | none | listed as withdrawn |

**Parameter count** (#1 §10; superseded). The lab notebook counted two parameters per sector against the phenomena each sector covers:

| Sector | Parameters | Phenomena covered |
|---|---|---|
| Conjugate matter | σ₀/m, v\* (2) | dwarf cores, the low-surface-brightness/group knee, cluster nulls, stream granularity scale, friction suppression (≥5) |
| Dark energy | f, τᵢ (2; V₀ fixed by Ω_DE) | w₀, wₐ, t_turn (3) |
| Geometry | M̃, k̃ (2, optional) | early-G step, ΔN_eff, gravitational-wave step |

#1 §12 sums this up as "Two parameters per sector, kill conditions in every row of §9", and v1's plain-language abstract as "two free parameters per sector, kill conditions on every claim" (#9 §0). The count predates the momentum graviton X, whose five βₙ coefficients reduce to two (calc note #8 §3; [spectrum and parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)). #11 keeps the [dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint), two parameters for three observables (§10), but has no full parameter table. Two of the five conjugate-matter phenomena, stream granularity and friction suppression, belonged to the withdrawn rows.

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 — the current eleven-row table and the withdrawn list; §15 for the exposure rows
- `notes/broken-born-program-v1.md` §9 — v1's ten rows and its withdrawn list; §0 for "two free parameters per sector"
- `notes/broken-born-theory.md` §9, §10, §12 — v0.1's ten rows, its flagships, its parameter table and summary
- `notes/broken-born-theory.md` 'Addendum (v0.2, post Debt-3)', 'Addendum (v0.4)' — the withdrawal of rows 3–4, the island-discriminant row, and the cliff-to-knee amendment
- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — rows 3 and 4 withdrawn on both islands
- `notes/debt1a-iv-beta-coefficients.md` §3 — the five-to-two reduction of the βₙ that postdates the v0.1 count
