---
title: "Dwarf galaxies: cores and ultra-faint dwarfs"
weight: 20
status: established
description: "The cusp–core problem and baryonic feedback in classical dwarfs; ultra-faint dwarfs as the densest, most dark-matter-dominated systems, with Segue 1's inputs as the program used them (uncited, to be source-checked)."
provenance: [T]
sources:
  - "notes/ufd-endpoint.md 'Sharpened input numbers'"
  - "notes/ufd-endpoint.md 'The data'"
  - "notes/ufd-endpoint.md 'The attractive endpoint: criticality and the drain'"
  - "notes/ufd-endpoint.md 'Verdict and closure of the clumping problem'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md 'Addendum (v0.2, after the clumping notes): resolution of open problem 3'"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §5"
  - "review/round3/referee/audit-notes.md Step 2"
---

*Dwarf galaxies are small, faint galaxies, many of them satellites of the Milky Way, whose mass is mostly dark matter. In many of the brighter, classical dwarfs the dark matter's central density is flatter than collisionless cold dark matter (CDM) predicts — the cusp–core problem — which a self-interaction of the dark matter, the wave nature of very light dark matter, or the gravitational stirring caused by gas that supernovae blow out of the center can explain. The ultra-faint dwarfs (UFDs) are fainter still, and they are the densest, oldest and most dark-matter-dominated systems known. In the Comatter program, the classical dwarfs fix the strength of [conjugate matter](/wiki/dark-matter/conjugate-matter)'s self-scattering, and the ultra-faint dwarfs, Segue 1 among them, falsified [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), one branch of the momentum-clumping test.*

**Status:** Established observational background — [T] — the Segue 1 numbers below are the program's own inputs, stated without a citation in any source and not checked by a `verify/` script; they are to be source-checked before external use.

## What dwarf galaxies are [T]

The Milky Way is surrounded by many satellite galaxies far smaller than itself. The brighter ones, the classical dwarfs such as the Fornax dwarf spheroidal, have been known for decades. The ultra-faint dwarfs, with far fewer stars, were found in deep imaging surveys of this century.

A dwarf's mass is measured from the motions of its stars. Spectra give each member star's velocity along the line of sight; their spread is the [velocity dispersion](/wiki/dark-matter/halo-astrophysics/velocity-dispersion#measuring-σ-in-a-dwarf-galaxy) σ, and a stellar system of size R in equilibrium has a mass of order σ²R/G inside R, with G Newton's constant. Comparing that mass with the light of the stars gives the mass-to-light ratio, M/L. In dwarf galaxies M/L is far larger than the stars can supply, and the difference is dark matter.

## The cusp–core problem [T]

Simulations of collisionless cold dark matter produce halos whose density keeps rising toward the center, a cusp. Observations of many dwarfs indicate instead a central region of nearly constant density, a core: the rotation curves of gas-rich dwarfs rise more slowly than a cusp would make them, and the stellar kinematics of several dwarf spheroidals favor cores, though how well they do so is debated. The explanations fall into two families.

- **Dark-matter physics.** If dark matter scatters off itself, collisions carry heat into the cold center and flatten it ([self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter)). If dark matter is a very light wave, the wave's resistance to compression, its quantum pressure, gives each halo a coherent central core ([bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds)).
- **Baryonic feedback.** Supernovae repeatedly blow gas out of a dwarf's center. Each outflow changes the central gravitational potential faster than the dark-matter orbits can follow, and the repeated changes transfer energy to the dark matter, which spreads out into a core. This requires no new dark-matter physics.

The survival of globular clusters far from the center of the Fornax dwarf, which [dynamical friction](/wiki/dark-matter/halo-astrophysics/halo-substructure) would drag inward in a cuspy halo, is often cited as indirect evidence for a core.

## The classical dwarfs in the program

### The core-fitting value

The program fixes the strength of conjugate matter's self-scattering with the classical dwarfs. [The lab notebook](/wiki/history/documents/lab-notebook): "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" (#1 §5.1), a value stated without a citation. Calc note #2 draws the consequence: "The dwarf-core fit fixes σ₀/m = 30 cm²/g, hence g is *determined* — no freedom remains" (`notes/stream-stability.md`, 'Numbers at the scattering benchmark'). [The checkpoint](/wiki/history/documents/checkpoint)'s benchmark mass, m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3} (#11 §8), carries the same value; see [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark).

### A dwarf core as a test environment

The [clumping notes](/wiki/history/documents/clumping-notes) use a classical dwarf core as one of their test environments. Calc note #2's "Dwarf core (ρ ∼ 1 GeV/cm³, σ∼30 km/s)" is where the ratio of the two sides of the mean-field [instability criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) is "∼10⁻²⁸". Calc note #3's environment table has the row "Classical dwarf core (1, 30)", with ρ in GeV/cm³ and σ in km/s, t_dyn = 0.1 Gyr and stream-to-stirring ratio R_X ~ 10⁻² (`notes/wave-island.md`, 'What pins g? Two scenarios'). Under Scenario A, the same cores fix the coupling: "Fitting classical-dwarf cores means Γ_self(dwarf) · t_age = κ ∼ 1".

### Where each branch gets its cores

Each of the program's dark-matter options needs the dwarf cores to come from somewhere, and the record gives a different source for each:

| Option | Status | Origin of dwarf cores |
|---|---|---|
| χ particles ([particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem)) | alive | gated self-scattering, at the core-fitting value above ([χ particles](/wiki/dark-matter/candidates/chi-particles)) |
| Wave χ, [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) | dead | the gated condensation channel, as "the core-maker" (calc note #3) |
| Wave χ, [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b) | alive, quarantined | "fuzzy-end quantum pressure at m ∼ 10⁻²² eV, or baryonic feedback" (calc note #3) |
| Superheavy solitons ([retired](/wiki/dark-matter/candidates/soliton-candidate/obituary)) | dead | baryonic feedback, since the candidate was "effectively collisionless cold dark matter" (#14 §4) |

Two entries need comment. Scenario B's fuzzy option lies below the lower edge of the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) that calc note #4 later set, 3×10⁻¹⁹ eV; neither note addresses the difference ([bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds)). The soliton manuscript #14, now withdrawn, estimated the [monopoles](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)' self-interaction at [σ_T/M](/wiki/dark-matter/halo-astrophysics/transfer-cross-section#the-soliton-candidates-σ_tm) ∼ 10⁻²⁶ cm²/g and concluded: "The candidate is effectively collisionless cold dark matter, so observed dwarf-galaxy cores must be attributed to baryonic feedback" (`notes/knot-dark-matter-standalone.md` §4). It listed the opposite finding among its exclusion conditions: "Demonstration that dwarf cores require dark-sector self-interaction (this candidate cannot supply it)" (§5). The [round-3](/wiki/method/review/round-3) referee's audit reproduced the self-interaction estimate, up to a factor-2 convention (`review/round3/referee/audit-notes.md`, Step 2). The candidate was retired for other reasons ([the soliton obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## Ultra-faint dwarfs [T]

The ultra-faint dwarfs are the faintest galaxies known. Their stars are old, their sizes and velocity dispersions are small, and their mass-to-light ratios are very large. In the notes' words, with DM for dark matter: "Observed UFDs are the densest, most DM-dominated, oldest systems known" (`notes/ufd-endpoint.md`, 'The data'). The notes use "a UFD escape velocity of ~10 km/s" and "the UFD core mass (~10⁶ M_⊙)" ('The attractive endpoint: criticality and the drain').

Those properties make them sensitive tests of dark-matter physics. Their potential wells are shallow, so anything that gives dark matter a speed above the escape velocity removes it. Their stellar populations are compact and kinematically cold, so anything that heats stars over billions of years shows in their sizes. And they have existed for most of the age of the universe, so slow processes have had time to act. The program met both kinds of test in the ultra-faint dwarfs: the drain of Scenario A's Branch (i), and the stellar heating behind the bound that closed Branch (ii) ([bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds)).

## Segue 1, the test case

Calc note #4 chose Segue 1 as the test system and gave its inputs ('Sharpened input numbers'):

> Segue 1: M(< 38 pc) ≈ 6×10⁵ M_⊙ ⇒ mean core density ρ ≈ 100 GeV/cm³ (not the conservative 20 used in #3), σ ≈ 3.7 km/s, t_dyn ≈ 10 Myr.

and its character ('The data'): "Segue 1 has M/L ~ 10³ and a ~13 Gyr stellar population sitting in an intact, *dense* halo". No source cites a measurement for any of these numbers, and no `verify/` script checks them.

With these inputs, calc note #4 reruns calc note #3's ratio of [condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) to orbital stirring, normalized to the dwarf cores (κ = 1):

```text
R_Segue1 = κ (t_dyn/t_age)(ρ/ρ_d)²(σ_d/σ)² ≈ 10⁻³ · 10⁴ · 66 ≈ 660
```

where ρ_d and σ_d are the classical dwarf core's values. The condensation time is "τ_cond = t_dyn/R ≈ 1.5×10⁴ yr. Over a 10 Gyr lifetime the system has ~6×10⁵ condensation times." The checkpoint quotes "Segue 1: rate ratio ~660; condensation ~10⁴ yr" (#11 §9). The computation and its robustness checks belong to [the Scenario A obituary](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a).

## What the ultra-faint dwarfs decided

Under Scenario A, condensation would be mandatory in ultra-faint dwarfs, and the condensate of an [attractive self-interaction](/wiki/dark-matter/wave-dark-matter/attractive-condensates) would cycle through collapses that eject dark matter faster than the escape velocity. Calc note #4's prediction for that branch: "UFDs today should be low-density, inflated, or gone." Segue 1's dense, intact halo and old stars contradict it: "Branch (i) predicts the opposite of what is observed" ('The data'), and "Scenario A is falsified by the existence of ultra-faint dwarfs" ('Verdict and closure of the clumping problem'). The checkpoint records it as "**falsified** by observed UFD density and longevity" (#11 §9), and the lab notebook's addendum v0.2 as "falsified by the observed density and longevity of Segue 1-class systems". The obituary is [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a); the claim is in [the graveyard](/wiki/status/graveyard).

## Superseded: calc note #3's ultra-faint-dwarf row

Calc note #3's environment table first entered the ultra-faint dwarfs as "Ultra-faint dwarf (20, 3)" — ρ = 20 GeV/cm³, σ = 3 km/s — with t_dyn = 0.01 Gyr and a ratio R_X ∼ 40 ('What pins g? Two scenarios'). Calc note #4 replaced that row with Segue 1's values, calling the earlier density "the conservative 20 used in 3b": ρ ≈ 100 GeV/cm³, σ ≈ 3.7 km/s, t_dyn ≈ 10 Myr, and a ratio of about 660. The checkpoint's "~10⁴ yr" for the condensation time is a rounding of calc note #4's 1.5×10⁴ yr, not a different value.

## References

The program's documents cite no source for the cusp–core problem, baryonic feedback, the ultra-faint dwarfs or Segue 1. Added by the wiki from model memory (†):

- B. Moore, Nature (1994)†; R. A. Flores, J. R. Primack, Astrophys. J. Lett. (1994)†: the cusp–core problem in dwarf rotation curves.
- J. F. Navarro, C. S. Frenk, S. D. M. White, "A universal density profile from hierarchical clustering," Astrophys. J. (1997)†: the cuspy profile of simulated halos.
- A. Pontzen, F. Governato, "How supernova feedback turns dark matter cusps into cores," Mon. Not. R. Astron. Soc. (2012)†.
- J. S. Bullock, M. Boylan-Kolchin, "Small-scale challenges to the ΛCDM paradigm," Annu. Rev. Astron. Astrophys. (2017)†: a review.
- V. Belokurov et al., Astrophys. J. (2007)†: the discovery of Segue 1; J. D. Simon et al., "A complete spectroscopic survey of the Milky Way satellite Segue 1: the darkest galaxy," Astrophys. J. (2011)†.
- J. D. Simon, "The faintest galaxies," Annu. Rev. Astron. Astrophys. (2019)†: a review of the ultra-faint dwarfs.

## Used by

- [The scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) — the dwarf-core fit fixes σ₀/m.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) — its dwarf cores come from gated self-scattering at the core-fitting value.
- [The mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion) — the coupling fixed by the dwarf-core fit, and a classical dwarf core as one of its two test environments.
- [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement) — the cross-section the dwarf cores require is the one it must explain.
- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — Segue 1's survival falsifies Scenario A.
- [Scenario B: tunable streams](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b) — cores attributed to fuzzy quantum pressure or baryonic feedback.
- [The net theorem](/wiki/dark-matter/momentum-clumping/net-theorem) — "fatal where it would have been mandatory" rests on the ultra-faint dwarfs.
- [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) — strong self-scattering in slow dwarfs.

## Sources

- `papers/broken-born-checkpoint-v2.md` §8, §9 — the benchmark mass; Segue 1's rate ratio and condensation time; the checkpoint's statement of the falsification
- `notes/ufd-endpoint.md` 'Sharpened input numbers', 'The data', 'The attractive endpoint: criticality and the drain', 'Verdict and closure of the clumping problem' — Segue 1's inputs and ratio, the ultra-faint dwarfs' escape velocity and core mass, the falsification
- `notes/wave-island.md` 'What pins g? Two scenarios' — the classical-dwarf and superseded ultra-faint environment rows; Scenario A's normalization; Scenario B's other origins of cores
- `notes/stream-stability.md` 'Numbers at the scattering benchmark' — the coupling determined by the dwarf-core fit; the dwarf core as a test environment
- `notes/broken-born-theory.md` §5.1, 'Addendum (v0.2, after the clumping notes): resolution of open problem 3' — the dwarf-core value of σ₀/m; the falsification as the lab notebook records it
- `notes/knot-dark-matter-standalone.md` §4, §5 — the withdrawn soliton manuscript: cores from baryonic feedback; exclusion condition 5
- `review/round3/referee/audit-notes.md` Step 2 — the self-interaction estimate reproduced up to a factor-2 convention
