---
title: "The radiation era: thermal history and N_eff"
weight: 10
status: established
description: "The expansion rate H = 1.66√g* T²/M_Pl, entropy density and yields Y = n/s, and the effective number of relativistic species with its nucleosynthesis and cosmic-microwave-background bounds."
provenance: [T]
sources:
  - "verify/soliton_obituary.py 'Anchors'"
  - "verify/soliton_obituary.py 'Dark radiation (ruling 5)'"
  - "review/round3-adjudication.md 'Rulings' 1"
  - "review/round3-adjudication.md 'Rulings' 5"
  - "review/round3/referee/audit-notes.md Step 2"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13 row 10"
  - "notes/broken-born-theory.md §9"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
---

*The radiation era is the early period in which the universe's energy was dominated by radiation and other particles moving at nearly the speed of light, so that the temperature alone set how fast the universe expanded. Three standard quantities describe it: the expansion rate as a function of temperature; the entropy density, which falls as the volume grows, so that the ratio of a relic's number density to it stays fixed once the relic is no longer made or destroyed; and N_eff, the effective number of light neutrino-like species, which nucleosynthesis and the cosmic microwave background both measure. The program used these quantities twice: in its optional prediction of fewer effective species from the conjugate sector, and in the review that retired its soliton dark-matter candidate, whose central error was a dropped factor of the radiation-era expansion rate.*

**Status:** Established — [T] — textbook thermal history, written here from general knowledge; the Friedmann coefficient 1.66 and the bound on extra species are anchors and checks [V] in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).

## Key facts

- **Expansion rate [T][V].** During radiation domination H = 1.66√g\* T²/M_Pl, with g\* the effective number of relativistic degrees of freedom and M_Pl the Planck mass. The script takes M_Pl = 1.22089e19 GeV and the reduced value 2.43536e18 GeV, and its anchor "Friedmann: H = 1.66 sqrt(g\*) T^2/M_Pl" passes. The coefficient comes from the [Friedmann equation](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) with the energy density of radiation.
- **Entropy and yields [T].** While the plasma stays in equilibrium, the entropy in a comoving volume is conserved, so a relic's yield Y = n/s, its number density divided by the entropy density, is constant once the relic freezes out. The script's present entropy density is s₀ = 2891.2 cm⁻³, the value the round-3 referee took from the Particle Data Group's 2024 tables (`review/round3/referee/audit-notes.md` Step 2).
- **Where the program met it.** The Kibble estimate of defect production is a yield, n/s = p (T_c/M_Pl)³ (#11 §12). One defect per Hubble volume gives p ≈ 104 [V] (the script prints "p = 104.31 with M_Pl" and 0.828 with the reduced Planck mass), and #14 v3's 0.0228 "drops (1.66√g\*)³ ≈ 4.6×10³" (round-3 ruling 1). See [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) and [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism).
- **N_eff [T].** N_eff measures the energy density of light species other than photons, in units of one neutrino species. The Standard Model value used in round 3 is 3.044 (ruling 5); the referee also gives results for 3.046. One extra neutrino species at the neutrino temperature adds ΔN_eff = 1, an anchor of the script.
- **The bound the program uses [T][V].** The script's inputs are Planck 2018's N_eff = 2.99 ± 0.34 at 95% (the value #14 §4 cites) and the Standard Model's 3.044; it prints "95% bound Delta N_eff < 0.286" (ruling 5). Both Big Bang nucleosynthesis and the cosmic microwave background (CMB) constrain N_eff.
- **The program's uses.** Row 10 predicts "closed dual curvature ⇒ negative ΔN_eff", with "CMB-S4 probes" (#11 §13 row 10); the lab notebook's "CMB-S4 N_eff at ±0.03" (#1 §9 row 10) was dropped from #11. See [row 10: an early step in G_eff](/wiki/predictions/early-universe-step). The retired candidate's hidden sector, had it shared our temperature, would have contributed "Delta N_eff ~ 0.86" (#14 §4; the referee's code gives 0.8567), which forced a colder hidden sector, ξ < 0.760 [V] (ruling 5); see [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history).

## Used by

- [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step) — negative ΔN_eff from closed dual curvature.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — the dark-radiation bound and ξ < 0.760.
- [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) — the dropped (1.66√g\*)³.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — yields at minimum production.

## Sources

- `verify/soliton_obituary.py` 'Anchors', 'Dark radiation (ruling 5)' — the Friedmann coefficient, the one-species anchor, the constants and the ΔN_eff bound, all executed
- `review/round3-adjudication.md` 'Rulings' 1, 5 — the dropped factor; the Standard Model's 3.044 and ΔN_eff < 0.286
- `review/round3/referee/audit-notes.md` Step 2 — the referee's constants and recomputations
- `papers/broken-born-checkpoint-v2.md` §12, §13 row 10 — the Kibble yield in the soliton obituary; the program's ΔN_eff prediction
- `notes/broken-born-theory.md` §9 row 10 — the dropped ±0.03 target
- `notes/knot-dark-matter-standalone.md` §3, §4 — the withdrawn candidate's yield and dark radiation (withdrawn; its body numbers are superseded)
