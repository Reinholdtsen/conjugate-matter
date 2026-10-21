---
title: "Dwarf galaxies: cores and ultra-faint dwarfs"
weight: 20
status: established
description: "The cusp–core problem and baryonic feedback in classical dwarfs; ultra-faint dwarfs as the densest, most dark-matter-dominated systems, with Segue 1's inputs as the program used them (uncited, to be source-checked)."
provenance: [T]
sources:
  - "notes/debt3c-ufd-endpoint.md 'Sharpened input numbers'"
  - "notes/debt3c-ufd-endpoint.md 'The data'"
  - "notes/debt3c-ufd-endpoint.md 'The attractive endpoint: criticality and the drain'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure of Debt 3'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/broken-born-theory.md §5.1"
  - "papers/broken-born-checkpoint-v2.md §9"
---

*Dwarf galaxies are small, faint galaxies, many of them satellites of the Milky Way, whose mass is mostly dark matter. In many of the brighter, classical dwarfs the dark matter's central density is flatter than collisionless cold dark matter (CDM) predicts — the cusp–core problem — which a self-interaction of the dark matter, or the gravitational stirring caused by gas that supernovae blow out of the center, can explain. The ultra-faint dwarfs (UFDs) are fainter still, and they are the densest, oldest and most dark-matter-dominated systems known. In the program, the classical dwarfs fix the strength of conjugate matter's self-scattering, and the ultra-faint dwarfs, Segue 1 among them, falsified [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), one branch of the momentum-clumping test.*

**Status:** Established observational background — [T] — the Segue 1 numbers below are the program's own inputs, stated without a citation in any source and not checked by a `verify/` script; they are to be source-checked before external use.

## Key facts

- **The cusp–core problem [T].** Simulations of collisionless cold dark matter give halo densities that keep rising toward the center (a cusp); the rotation curves and stellar motions of many dwarfs instead indicate a nearly constant central density (a core). The explanations divide into dark-matter physics — self-interaction or wave pressure — and baryonic feedback.
- **Classical dwarf cores, as the program used them.** [The lab notebook](/wiki/history/documents/lab-notebook) takes the core-fitting value to be "σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" (#1 §5.1), which sets [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark). The [Debt-3 notes](/wiki/history/documents/debt-3-notes) model a "Classical dwarf core (1, 30)", with ρ in GeV/cm³ and σ in km/s, and t_dyn = 0.1 Gyr (`notes/debt3b-wave-island.md`).
- **Cores from elsewhere.** [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b) lets "cores come from elsewhere (fuzzy-end quantum pressure at m ~ 10⁻²² eV, or baryonic feedback)" (`notes/debt3b-wave-island.md`).
- **Ultra-faint dwarfs.** In the notes' words, with DM for dark matter: "Observed UFDs are the densest, most DM-dominated, oldest systems known" (`notes/debt3c-ufd-endpoint.md`, 'The data'). The notes use "a UFD escape velocity of ~10 km/s" and "the UFD core mass (~10⁶ M_⊙)" ('The attractive endpoint').
- **Segue 1, the test case.** "Segue 1: M(< 38 pc) ≈ 6×10⁵ M_⊙ ⇒ mean core density ρ ≈ 100 GeV/cm³ (not the conservative 20 used in 3b), σ ≈ 3.7 km/s, t_dyn ≈ 10 Myr" ('Sharpened input numbers'); "Segue 1 has M/L ~ 10³ and a ~13 Gyr stellar population sitting in an intact, *dense* halo" ('The data'). No source cites a measurement for these numbers.
- **A superseded input.** Debt 3b's ultra-faint row, "Ultra-faint dwarf (20, 3)" with t_dyn = 0.01 Gyr, is replaced by Debt 3c's Segue 1 values.
- **What they decided.** Under Scenario A, condensation would be mandatory in ultra-faint dwarfs and would drain their dark matter; "Scenario A is falsified by the existence of ultra-faint dwarfs" (Debt 3c) — see [the Scenario A obituary](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a). [The checkpoint](/wiki/history/documents/checkpoint) records it as "falsified by observed UFD density and longevity" (#11 §9).

## Used by

- [The scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) — the dwarf-core fit fixes σ₀/m.
- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — Segue 1's survival falsifies Scenario A.
- [Scenario B: tunable streams](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b) — cores attributed to fuzzy quantum pressure or baryonic feedback.
- [The net theorem](/wiki/dark-matter/momentum-clumping/net-theorem) — "fatal where it would have been mandatory" rests on the ultra-faint dwarfs.
- [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) — strong self-scattering in slow dwarfs.

## Sources

- `papers/broken-born-checkpoint-v2.md` §9 — the checkpoint's statement of the falsification
- `notes/debt3c-ufd-endpoint.md` 'Sharpened input numbers', 'The data', 'The attractive endpoint: criticality and the drain', 'Verdict and closure of Debt 3' — Segue 1's inputs, the ultra-faint dwarfs' escape velocity and core mass, the falsification
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — the classical-dwarf and superseded ultra-faint environment rows; Scenario B's other origins of cores
- `notes/broken-born-theory.md` §5.1 — the dwarf-core value of σ₀/m
