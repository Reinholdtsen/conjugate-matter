---
title: "Round-3 arbitration and the referee's constants"
weight: 40
status: record
description: "The adjudicator's re-derivation from independent anchors (p = 104.31; M* = 2.87–4.44×10¹² GeV; the ψ recount) and the referee's externally sourced constants."
provenance: [V]
sources:
  - "review/round3/adjudicator/round3_arb.out"
  - "review/round3/adjudicator/round3_arb.py"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3-adjudication.md 'Rulings'"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "verify/soliton_obituary.py"
  - "CLAUDE.md 'Layout'"
---

*The round-3 arbitration is the adjudicator's own recomputation of the numbers the referee disputed, run before ruling on its findings: a short script, `review/round3/adjudicator/round3_arb.py`, that rebuilds the Kibble normalization from the radiation-era expansion rate, the mass at which the monopole abundance closes, and the relic window of the light hidden fermion ψ. It confirmed the referee's central finding: one defect per Hubble volume gives p = 104.31, where v3 had used 0.0228. The referee, for its part, took every physical constant from outside sources (the Particle Data Group's 2024 review and Planck 2018) rather than from the manuscript, so its checks could not simply repeat the manuscript's inputs.*

**Status:** Record — p and the closing mass carry [V] in #11 §12, because `verify/soliton_obituary.py` recomputes them, and the ψ window, in the gate ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)); `round3_arb.py` itself sits in `review/` and the gate does not run it. `CLAUDE.md` 'Layout' says arbitration scripts go in `verify/`; no document resolves the difference.

## Key facts

- **The output** (`review/round3/adjudicator/round3_arb.out`, first six lines):

  ```text
  1.66 check: sqrt(8 pi^3/90) = 1.6602
  p, one defect per H^-3, non-reduced M_Pl: 104.31
  p, one defect per H^-3, reduced M_Pl:     0.828
  p used in v3 (45/(2 pi^2 g*)):             0.0228
  f=1.0: M* (Kibble minimum production) = 2.87e+12 GeV; v = 1.38e+11; 3e13 overproduced x1.2e+04
  f=1.787: M* (Kibble minimum production) = 4.44e+12 GeV; v = 1.20e+11; 3e13 overproduced x2.1e+03
  ```

- **The anchor and inputs.** The script's expansion rate is "H = 1.66 sqrt(g\*) T^2 / M_Pl (radiation era, non-reduced Planck mass)", with the coefficient checked as √(8π³/90) ([Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)); M_Pl = 1.22089×10¹⁹ GeV, s₀ = 2891.2 cm⁻³ and Ω h² = 0.120 for the dark matter; the monopole mass M = 4πf v/g_d with f = 1 to 1.787 ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)). Independent anchors of this kind are now a rule ([independent anchors](/wiki/method/verification/independent-anchors)).
- **Rulings 1 and 2.** One defect per Hubble volume gives p = 104.31 with the Planck mass and 0.828 with the reduced Planck mass, against v3's 0.0228 ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization); [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism)). At that minimum production the abundance closes at M\* = 2.87×10¹² GeV (f = 1) to 4.44×10¹² GeV (f = 1.787), and the 3×10¹³ GeV benchmark is overproduced ×1.2×10⁴ to ×2.1×10³ ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)).
- **Ruling 4, the ψ recount.** With "sigma v = pi alpha^2/m^2 exact s-wave" and both ψ and ψ̄ and both doublet members counted, 100% of the dark matter is reached at 146 GeV and 10% at 45 GeV for g\* = 80, and at 158 and 49 GeV for g\* = 106.75; v3's counting gives 297 / 92 GeV and 321 / 99 GeV ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window); [relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)).
- **Where referee and adjudicator differ.** The referee's own Boltzmann integration put the ψ window at 28–46 / 96–153 GeV; the adjudication: "We agree to within ×1.6", and the gate checks the adjudicator's numbers. The referee also gave an M\* variant for one defect per volume (4π/3)H⁻³, 4.11×10¹²–6.35×10¹² GeV; the adjudication and the gate use the H⁻³ convention. The adjudicator did not re-run the referee's Kibble–Zurek integration, and rulings 6 and 9 were accepted without re-checking ([round-3 rulings](/wiki/method/review/round-3/rulings)).
- **The referee's constants and its check of the manuscript's inputs** (audit notes, Step 2, verbatim; `PDG` is the Particle Data Group, `EW` its electroweak review, `MZ` the Z mass):

  ```text
  Own constants: alpha^-1=137.035999; alpha_hat(MZ)^-1 = 127.930 (PDG 2024 EW review); MPl=1.220890e19 (PDG 2024 astro);
  rho_c/h^2=1.053672e-5 GeV/cm^3; s0=2891.2/cm^3 (PDG 2024 astro); Omega_c h^2 = 0.120 (Planck 2018); N_eff 95% from Planck eq. 67b.
  Manuscript inputs checked: rho_DM = 1.264 keV/cm^3 (OK), s0 ~2.9e3 (OK), MPl 1.22e19 (OK); local 0.4 GeV/cm^3 (PDG canonical 0.3, x2-3).
  ```

  The one flagged input is the local dark-matter density, 0.4 GeV/cm³ against the Particle Data Group's canonical 0.3 ([benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)).

## Sources

- `review/round3/adjudicator/round3_arb.out` — the printed numbers
- `review/round3/adjudicator/round3_arb.py` — the anchor, the constants and the ψ counting
- `review/round3/referee/audit-notes.md` Step 2 — the referee's constants, its checks of the manuscript's inputs, and its own ψ window and M\* variant
- `review/round3-adjudication.md` 'Rulings' (1–4) — how the arbitration fed the rulings, and what was not re-run
- `papers/broken-born-checkpoint-v2.md` §12 — the corrected numbers as [V]
- `verify/soliton_obituary.py` — the gated recomputation
- `CLAUDE.md` 'Layout' — arbitration scripts belong in `verify/`
