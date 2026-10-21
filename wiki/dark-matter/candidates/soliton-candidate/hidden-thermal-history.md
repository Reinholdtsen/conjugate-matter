---
title: "The hidden sector's thermal history"
weight: 100
status: record
description: "Dark radiation from the hidden photon (ΔN_eff = 0.86 at ξ = 1 for one light doublet), the bound ξ < 0.760, its inconsistent application in v3, and the gravitational-wave band a first-order transition would leave."
provenance: [V]
sources:
  - "review/round3-adjudication.md 'Rulings' 5"
  - "review/round3-adjudication.md 'Rulings' (omitted constraints)"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "verify/soliton_obituary.py"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/step2a.out"
  - "review/round3/referee/step4.out"
  - "review/round3/referee/step4c.out"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/v3-worklog.md 'New open items'"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §6"
---

*The hidden sector's thermal history is the record of how the soliton candidate's hidden sector would have evolved as the universe cooled, and of the constraints that evolution had to meet. Its massless hidden photon, together with any light hidden fermion ψ, is extra radiation, which measurements of the cosmic microwave background limit through the effective number of neutrino species, N_eff. A hidden sector as hot as ours would add about 0.86 to N_eff, which is excluded, so #14 required the hidden sector to start colder, by a temperature ratio ξ below 0.77 — corrected in round 3 to 0.760 — yet computed its relic abundances as if ξ were 1. A first-order hidden phase transition would also have left gravitational waves at about 10⁵–10⁷ Hz. These are requirements and predictions of a retired candidate, kept as record.*

**Status:** Record — requirements and predictions of a dead candidate. The corrected dark-radiation numbers (ruling 5, "Upheld (minor)") are [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)), as is the corrected upper end of the gravitational-wave band. The v3 worklog's earlier table is tagged `[NOTE-tier]`, with its 0.3 bound "from memory †". The gravitational-wave band died with the candidate ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## A sector with its own temperature

A hidden sector that exchanges no energy with ours after the universe is reheated evolves on its own [T]. Each sector conserves its own entropy as the universe expands, so each cools as the inverse of the scale factor, and their temperatures keep the ratio ξ = T_h/T that reheating left them with ([the radiation era](/wiki/cosmology/early-universe/radiation-era)). The ratio changes only when a species in one sector becomes non-relativistic and annihilates: its entropy passes to the lighter species of the same sector, which then cool more slowly than the other sector [T]. Our own sector does this many times, from the 106.75 relativistic degrees of freedom of the full Standard Model to the 10.75 left when the neutrinos decouple.

The soliton candidate's hidden sector ([the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)) has the same structure. Above the breaking scale v its plasma holds the SU(2)_d gauge fields, the adjoint scalar and the fermion doublet ψ. Below v the W′± and the scalar become heavy and disappear, ψ freezes out at its own mass, and in the end only the hidden photon is left. The photon is massless because U(1)_d is unbroken, which v3 lists as requirement (iii), "an unbroken U(1)_d" (#14 §6), so it stays radiation forever.

## Dark radiation

### N_eff [T]

Radiation in the early universe beyond the photons is measured as N_eff, the number of neutrino species at the standard neutrino temperature that would carry the same energy density [T]. The Standard Model value is about 3.044 (the round-3 adjudication's value; Planck 2018 uses 3.046). Any extra light species raises it. For a species with g internal states at temperature T_x, the excess is

```text
ΔN_eff = (4/7) · g · (T_x/T_ν)⁴
```

for bosons [T]; the 4/7 converts to neutrino units, since one neutrino species with its antineutrino counts as 7/4 bosonic states. `verify/soliton_obituary.py` codes this formula and anchors it on a textbook case before using it: "Delta N_eff: one extra neutrino species at T_nu gives 1". The measurement #14 cites is Planck 2018, eq. (67b): "N_eff = 2.99 +0.34 -0.33" at 95% confidence (audit notes, Step 1).

### #14's requirement

#14 §4:

> Dark radiation. The hidden photon is radiation. Suppose the two sectors shared a temperature above v. The hidden sector - the SU(2)_d gauge fields, the adjoint scalar and one psi doublet - then contributes Delta N_eff ~ 0.86 after its heavy states disappear. That is excluded by Planck 2018 (N_eff = 2.99 +- 0.34 at 95%) [23]. The proposal therefore requires the hidden sector to have been reheated to xi < 0.77 of our temperature, an assumption about reheating that the framework does not fix.

The calculation follows the two sectors separately. The worklog's setup: "the two sectors at temperature ratio ξ at high T, then separately entropy-conserving, ending with only the dark photon relativistic" (`review/v3-worklog.md`, 'New open items', O2). As the gate's script codes it, the hidden photon's temperature relative to the neutrinos is

```text
T_h/T_ν = ξ · (10.75/106.75)^(1/3) · ((9 + 7/8·8)/2)^(1/3)
ΔN_eff  = (4/7) · 2 · (T_h/T_ν)⁴
```

The first factor after ξ is the visible sector's entropy transfer from above v down to neutrino decoupling, which heats the neutrinos relative to an isolated sector. The second is the hidden sector's own: 9 + 7/8·8 states above v, which the referee writes as "g_h(high)=16.0", collapsing into the hidden photon's 2 polarizations, "g_h(late)=2.0" (`step2a.out`). The 9 and the 8 are the bosons (the gauge fields and the adjoint scalar) and the fermions (one ψ doublet, weighted by 7/8) of the content #14 names [T]. The script evaluates ΔN_eff at ξ = 1 and uses its ξ⁴ dependence to find the bound on ξ. At ξ = 1 the referee's code gives "T_h/T_nu = 0.9305, DeltaN_eff = 0.8567", confirming #14's 0.86 (Step 2).

### The worklog's table and the corrected bound

The worklog had computed three versions of the hidden content (O2, tagged `[NOTE-tier]`):

| Dark sector content | ΔN_eff at ξ = 1 | ξ needed for ΔN_eff < 0.3 |
| --- | --- | --- |
| Minimal | 0.40 | < 0.93 |
| One light doublet | 0.86 | < 0.77 |
| Two light doublets | 1.39 | < 0.68 |

"The 0.3 bound is an approximate Planck 2018 value, from memory †." Round 3 replaced it with the measured interval. Ruling 5, "Upheld (minor)": "ξ bound 0.760, not 0.77", because "Using N_eff,SM = 3.044, the 95% bound is ΔN_eff < 0.286", where N_eff,SM is the Standard Model value. The script takes the upper end of Planck's 95% interval and subtracts the Standard Model value, `bound = 2.99 + 0.34 - 3.044`, and its two checks pass:

```text
PASS  95% bound Delta N_eff < 0.286  [0.286]
PASS  xi < 0.760  [0.7601]
```

The referee's table (Step 2) gives the spread over conventions: "0.760 (N_SM=3.044), 0.759 (3.046); 0.769 only if DeltaN<0.30", with the verdict "minor DISCREPANCY (should be 0.76)". v3's 0.77 is the remembered 0.3 bound carried through.

## Requirement (ii) and its knock-on

v3 made the colder sector the second of its "Requirements forced by consistency (not optional)": "(ii) a hidden-to-visible temperature ratio xi < 0.77 after reheating", and listed "the colder reheating of the hidden sector" among its conjectural claims (#14 §6). The worklog had called it a choice of a free parameter: "v3 requirement: the dark sector reheated ~25–30% colder than ours. ξ is a free parameter of the framework."

A colder hidden sector also changes the monopole count, since the hidden transition then happens when our plasma is hotter. #14 §4: "A colder hidden sector lowers M\* by xi^(3/4), a factor of 0.8 at the bound - smaller than the factor-of-four spread already in the band above." The referee confirmed the factor, "0.822 (xi=0.77), 0.814 (xi=0.76)" (Step 2). After the Kibble correction, the referee's minimum-production mass shifts accordingly: "M\* = 2.87e12-4.44e12 GeV (xi=1), 2.34e12-3.61e12 GeV (xi=0.76)" (Step 4(a) item 1; [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)).

## Applied inconsistently

v3 required ξ < 0.77 but computed everything else at ξ = 1. The worklog had said so for the W′ relic ("Computed at ξ = 1 only"), and the round-3 [pre-registration](/wiki/method/review/round-3/preregistration) named it the second runner-up weakest link: "Thermal-history consistency. The W′ and ψ freeze-out are computed at ξ = 1, but dark radiation requires ξ < 0.77, and Kibble production with a colder hidden sector is treated only by the ξ^(3/4) scaling."

The referee recomputed at the required ratio (Step 4(a) item 4):

> Colder hidden sector: W' overclosure survives (xi=0.76: 9.9e15 - 2.9e16, step4b.out); the M\* band is quoted at xi=1 while xi<0.76 is required (the xi^(3/4) shift is stated, the band is not updated). psi window computed with hidden temperature (step2c_thr.out): 10% DM at 35 GeV (xi0=0.76) - the manuscript's "below about 0.1 TeV" would make psi ~70-100% of DM (step2c_psi.out: 73.1% at 100 GeV, xi0=0.76).

DM is dark matter. The W′ result survives the change ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)); the ψ window does not ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)).

## What a colder hidden sector would need

### A reheating mechanism

At the end of inflation the energy of the inflaton field is converted into hot particles, which reheats the universe [T] ([inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution)). A single inflaton that decays equally into both sectors gives them equal temperatures; a colder hidden sector needs a decay that favours ours, or a separate field for each sector [T]. #14 §3 adds the ordering condition for the monopoles themselves: "Inflation must precede the hidden transition, and v must lie below the reheating temperature." The referee (Step 4(c) item 9):

> Reheating: requires visible T_RH >~ v/xi = 1.06e12 - 1.90e12 GeV (step4c.out) and a two-field (or asymmetric) reheating mechanism for xi; a separately reheated hidden sector can carry dark-radiation isocurvature (conditional; not computed).

### No portal that re-equilibrates the sectors

Any coupling that lets the two plasmas exchange energy pulls ξ back toward 1. The referee named two (Step 4(c) item 7 and Step 4(a) item 5).

- **The Higgs portal.** The operator λ_p |H|² Tr Φ², which couples the hidden scalar to our Higgs field H, is "allowed by every stated symmetry". Keeping the electroweak scale natural "needs lambda_p <= 2.4e-20 - 7.5e-21", while "equilibration at T~v for lambda_p >~ 5e-2 (rough 2->2 estimate) would set xi=1 -> Delta N = 0.86 (excluded). Technically natural to set small, but unstated."
- **A millicharged ψ.** If the photons mix kinetically, ψ carries a small visible charge and the Standard Model plasma produces it directly: "with eps = 1e-6 the SM freeze-in of psi reaches equilibrium for all m_psi <= 30 GeV", where SM is the Standard Model; then "The hidden sector is re-thermalised below v and the reheating ratio xi is no longer the operative variable." ΔN_eff is then set by when the hidden photon decouples: "T_d < 0.2 GeV -> Delta N >= 0.61 (excluded); T_d = 0.2-30 GeV -> 0.065-0.11 (gamma' only) up to 0.48-0.83 if the psi entropy is dumped after decoupling (step4.out)." Decision 1, strict sector separation, closed this channel ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).

The adjudication accepted "The reheating mechanism for ξ", "The Higgs portal" and "Re-thermalization by ψ at ε ~ 1e-7–1e-6" as items for a to-do list, "not individually re-checked" ([round-3 verdict and rulings](/wiki/method/review/round-3/rulings)).

## The gravitational-wave band (died with the candidate)

A first-order phase transition proceeds by bubbles of the new phase that nucleate, expand and collide; the collisions and the sound waves they set up in the plasma radiate gravitational waves [T] ([gravitational waves from phase transitions](/wiki/cosmology/early-universe/phase-transition-gravitational-waves)). The characteristic frequency at the transition is set by the inverse duration of the transition, and the signal today is that frequency redshifted by the expansion since then. #14 §4:

> Phase-transition signatures. If the hidden transition is first order, it sources a stochastic gravitational-wave background with a present-day peak frequency of ~1e5 to 1e7 Hz for f\*/H\* = 1-100. That is above the LIGO band, in the unconstrained ultra-high-frequency window targeted by proposed detectors. The amplitude is suppressed by the hidden sector's share of the energy density at the transition, which is small for xi < 0.77. A crossover transition leaves no such signal.

LIGO is the Laser Interferometer Gravitational-Wave Observatory. Here f\*/H\* is the ratio of the characteristic frequency at the transition to the Hubble rate then. The referee evaluated the standard redshift formula (`step2a.out`):

```text
f0 = 1.65e-5 Hz (f*/H*) (T*/100 GeV) (g*/100)^(1/6)
```

with T\* the visible temperature at the transition. Taking T\* = v at the benchmark, f\*/H\* = 1 and 100, and g\* = 106.75 or 122.75, it found "1.35e5 - 2.47e7 Hz", "CONFIRMED" (Step 2). Ruling 5 carried the corrected ξ into the band, and the upper end becomes 3.2×10⁷ Hz. The script takes T\* = v/ξ, the visible temperature at which the colder hidden plasma reaches v. The gate's check of that upper end ("knock-on: ... upper end 3.2e7 Hz at the withdrawn benchmark") passes, printing `3.17e+07`. The record follows the adjudication and the gate, not the referee's T\* = v figure ([conflicts between sources](/wiki/history/documents/source-conflicts)).

The band was conditional twice over: on a first-order transition, and on the hidden sector carrying enough energy for the amplitude to matter. It also sat badly with the manuscript's own abundance count. The referee notes that #14's gravitational-wave paragraph "contemplates a first-order transition with f\*/H\* = 1-100", and that "bubble counting gives p ~ 104 (beta/H)^3 = 1e2-1e8 (step4.out) - flatly inconsistent with "p = 1 as the upper end" of Sec. 3" (Step 4(a) item 2). A first-order transition forms monopoles where bubbles meet, so it would have made far more of them than v3 counted ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)). The band was a prediction of the soliton candidate, and it died with it.

## Scope: ordinary kinematics

All of this treats the hidden sector with ordinary relativistic quantum field theory: "Throughout, the hidden sector is described by ordinary relativistic quantum field theory" (#14 §1). The worklog recorded that the dark-radiation calculation depends on that choice (O3): "v3 decision: keep the dark sector in ordinary kinematics and say so explicitly. L1 and O2 both rest on that." (L1 is the worklog's finding that mixing gives the monopoles no visible magnetic flux.) Whether the hidden photon is massless in the ordinary sense, or has zero invariant length in the sense of [conjugate special relativity](/wiki/conjugate-relativity) (#13), "is part of #13's open "dual dynamics" item" ([the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).

## Where the numbers stand

| Item | Value | Status |
| --- | --- | --- |
| ΔN_eff for a shared temperature (one ψ doublet) | 0.86 | computed inside the gated ξ check, not checked on its own; referee 0.8567 |
| 95% bound on ΔN_eff | 0.286 | [V], gated (ruling 5) |
| Bound on ξ | < 0.760 | [V], gated (ruling 5); v3's 0.77 superseded |
| Worklog table (three contents) | 0.40, 0.86, 1.39 | `[NOTE-tier]`, 0.3 bound † |
| Factor on M\* | ξ^(3/4): 0.822 (ξ = 0.77), 0.814 (ξ = 0.76) | referee, not gated |
| Visible reheating temperature | ≳ v/ξ = 1.06e12–1.90e12 GeV | referee's estimate, not re-checked |
| Gravitational-wave band | 10⁵–10⁷ Hz; upper end 3.2×10⁷ Hz at T\* = v/ξ | upper end [V], gated; dead with the candidate |

## Sources

- `review/round3-adjudication.md` 'Rulings' 5 — the corrected bound and its knock-on on the band; the omitted-constraints list — reheating, the Higgs portal and re-thermalization as unchecked to-dos; 'Decisions' 1 — the millicharge channel closed
- `verify/soliton_obituary.py` — the ΔN_eff formula and its anchor, the gated bound and ξ, and the band's upper end
- `review/round3/referee/audit-notes.md` Step 1 — Planck's eq. (67b); Step 2 — the referee's values; Step 4(a) items 1, 2, 4 and 5 — M\* at ξ = 0.76, bubble counting, the inconsistency, re-thermalization; Step 4(c) items 7 and 9 — the Higgs portal and reheating
- `review/round3/referee/step2a.out` — the dark-radiation degrees of freedom and the frequency formula; `review/round3/referee/step4.out`, `review/round3/referee/step4c.out` — the decoupling and reheating values quoted
- `review/round3-preregistration.md` 'Predictions' — the anticipated weakness
- `review/v3-worklog.md` 'New open items' — O2's setup and table, O1's "Computed at ξ = 1 only", O3 on kinematics
- `notes/knot-dark-matter-standalone.md` §1 — ordinary kinematics; §3 — the reheating condition; §4 — dark radiation and the gravitational-wave band; §6 — requirements (ii) and (iii)
