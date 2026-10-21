---
title: "The hidden sector's thermal history"
weight: 100
status: record
description: "Dark radiation from the hidden photon (ΔN_eff = 0.86 at ξ = 1 for one light doublet), the bound ξ < 0.760, its inconsistent application in v3, and the gravitational-wave band a first-order transition would leave."
provenance: [V]
sources:
  - "review/round3-adjudication.md 'Rulings' 5"
  - "verify/soliton_obituary.py"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/v3-worklog.md 'New open items'"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3-preregistration.md 'Predictions'"
---

*The hidden sector's thermal history is the record of how #14's hidden sector would have evolved as the universe cooled, and of the constraints that evolution had to meet. Its massless hidden photon, together with any light ψ, is extra radiation, which measurements of the cosmic microwave background limit through the effective number of neutrino species, N_eff. A hidden sector as hot as ours would add about 0.86 to N_eff, which is excluded, so #14 required the hidden sector to start colder, by a temperature ratio ξ below 0.77 — corrected in round 3 to 0.760 — yet computed its relic abundances as if ξ were 1. A first-order hidden phase transition would also have left gravitational waves at about 10⁵–10⁷ Hz. These are requirements and predictions of a retired candidate, kept as record.*

**Status:** Record — requirements and predictions of a dead candidate. The corrected dark-radiation numbers (ruling 5, "Upheld (minor)") are [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)); the v3 worklog's table is tagged `[NOTE-tier]`, with its 0.3 bound "from memory †". The gravitational-wave band died with the candidate.

## Key facts

- **Dark radiation** (#14 §4): "Suppose the two sectors shared a temperature above v. The hidden sector - the SU(2)_d gauge fields, the adjoint scalar and one psi doublet - then contributes Delta N_eff ~ 0.86 after its heavy states disappear. That is excluded by Planck 2018 (N_eff = 2.99 +- 0.34 at 95%) [23]. The proposal therefore requires the hidden sector to have been reheated to xi < 0.77 of our temperature, an assumption about reheating that the framework does not fix." See [the radiation era](/wiki/cosmology/early-universe/radiation-era) and [inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution).
- **The worklog's table** (item O2), ΔN_eff at ξ = 1 and the ξ needed for ΔN_eff < 0.3: minimal sector 0.40, "< 0.93"; one light doublet 0.86, "< 0.77"; two light doublets 1.39, "< 0.68".
- **Ruling 5** (upheld, minor): "Using N_eff,SM = 3.044, the 95% bound is ΔN_eff < 0.286", where N_eff,SM is the Standard Model value; the bound becomes ξ < 0.760, "not 0.77". The gate's checks `95% bound Delta N_eff < 0.286  [0.286]` and `xi < 0.760  [0.7601]` pass. The referee computed ΔN_eff = 0.8567 for a shared temperature and verdict "minor DISCREPANCY (should be 0.76)" (audit notes, Step 2).
- **The knock-on on the monopole mass** (#14 §4): "A colder hidden sector lowers M\* by xi^(3/4), a factor of 0.8 at the bound". The referee: "0.822 (xi=0.77), 0.814 (xi=0.76)", confirmed.
- **Applied inconsistently** (Step 4(a) item 4): "the M\* band is quoted at xi=1 while xi<0.76 is required (the xi^(3/4) shift is stated, the band is not updated)". At ξ₀ = 0.76, ψ "below about 0.1 TeV" would be "~70-100%" of the dark matter ([the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)), while the W′ overclosure survives ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)). The round-3 pre-registration had named this as its second runner-up weakest link: "Thermal-history consistency. The W′ and ψ freeze-out are computed at ξ = 1, but dark radiation requires ξ < 0.77".
- **What a colder sector would need** (Step 4(c) items 7 and 9). Reheating "requires visible T_RH >~ v/xi = 1.06e12 - 1.90e12 GeV (step4c.out) and a two-field (or asymmetric) reheating mechanism for xi"; and a Higgs-portal coupling large enough to equilibrate the sectors "would set xi=1 -> Delta N = 0.86 (excluded)". The adjudication accepted "The reheating mechanism for ξ" as an unchecked to-do.
- **The gravitational-wave band** (#14 §4): "If the hidden transition is first order, it sources a stochastic gravitational-wave background with a present-day peak frequency of ~1e5 to 1e7 Hz for f\*/H\* = 1-100 ... A crossover transition leaves no such signal." The referee's range is 1.35×10⁵–2.47×10⁷ Hz, taking the transition temperature T\* = v; ruling 5's knock-on puts the upper end at 3.2×10⁷ Hz, taking T\* = v/ξ, and the gate's check of that upper end passes at 3.17×10⁷ Hz ([gravitational waves from phase transitions](/wiki/cosmology/early-universe/phase-transition-gravitational-waves)).

## Sources

- `review/round3-adjudication.md` 'Rulings' 5 — the corrected bound and its knock-on
- `verify/soliton_obituary.py` — the gated dark-radiation values
- `review/round3/referee/audit-notes.md` Step 2 — the referee's values; Step 4(a) — the inconsistency; Step 4(c) — reheating and the Higgs portal
- `review/round3-preregistration.md` 'Predictions' — the anticipated weakness
- `review/v3-worklog.md` 'New open items' — O2's table
- `notes/knot-dark-matter-standalone.md` §4 — dark radiation and the gravitational-wave band; §6 — requirement (ii)
