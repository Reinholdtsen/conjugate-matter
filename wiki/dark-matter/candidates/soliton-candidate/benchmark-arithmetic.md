---
title: "Benchmark-conditional arithmetic"
weight: 110
status: record
description: "Numbers that survive as arithmetic though the benchmark is withdrawn: densities and spacing, a Coulomb σ_T/M ~ 10⁻²⁶ cm²/g, and a counterfactual flux 7.5 orders above the Parker bound that shows why sector separation is mandatory."
sources:
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Verified references for v3'"
  - "HANDOFF.md §6"
---

*Benchmark-conditional arithmetic is the set of numbers that #14 v3 computed at its benchmark monopole mass of 3×10¹³ GeV and that remain correct as arithmetic, although the benchmark itself is withdrawn. At that mass, monopoles making up all the dark matter would be spaced about 420 m apart near the Sun; they would scatter off one another so weakly, σ_T/M ~ 10⁻²⁶ cm²/g, that they would behave as collisionless cold dark matter; and if they carried magnetic charge under our own electromagnetism, their flux would exceed the Parker bound by 7.5 orders of magnitude. That last, counterfactual number is why the hidden sector has to be separate from ours. The round-3 referee recomputed each value from independently chosen constants and confirmed it.*

**Status:** Record — "The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′ overclosure" survives v3 (round-3 adjudication, "What survives v3"), and the referee marked each value "CONFIRMED" (audit notes, Step 2). #14 §6 lists the "counterfactual flux numbers and cross-section of Sec. 4" as derived. Apart from the W′ overclosure, which has [its own page](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure), these values are not in the current gate.

## Key facts

- **Densities and spacing** (#14 §3): "The mean number density is n ~ 4.2e-20 /cm^3. At the local halo density (0.4 GeV/cm^3) there is one monopole per ~0.075 km^3, a mean spacing of about 420 m, drifting at ~1e-3 c." The referee: 4.215×10⁻²⁰ cm⁻³; "0.0750 km^3 / 421.7 m (0.3 GeV/cm^3: 0.100 km^3, 464 m)", noting that the canonical local density of the Particle Data Group is 0.3 GeV/cm³. The mean density used was 1.264 keV/cm³ (Step 2).
- **v2's numbers.** At v2's benchmark of 10¹⁶ GeV, the "manuscript's 1.3×10⁻²² mean and one-per-25-km³ local are both exactly right"; the round-2 referee had conflated the two (`HANDOFF.md` §6).
- **Self-interaction** (#14 §4): "sigma_T/M ~ 8 pi alpha_m^2 ln(Lambda)/((M/2)^2 M v^4) ~ 1e-26 cm^2/g at v ~ 1e-3 c and M = 3e13 GeV, for ln(Lambda) = 10-30. That is some twenty-six orders below astrophysical sensitivity. The candidate is effectively collisionless cold dark matter, so observed dwarf-galaxy cores must be attributed to baryonic feedback." The referee: "0.95e-26 - 2.9e-26 (manuscript formula); standard 4 pi a^2 lnL/(mu^2 v^4) gives half; ~25.7 orders below 1 cm^2/g", "CONFIRMED (factor-2 convention)". See [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) and [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies).
- **Caveats on "collisionless".** It "rests on two-body sigma_T only"; collective magnetic-plasma effects were left "Unevaluated, not an indictment" (Step 4(c) item 6). In round 1 the referee had "σ_T/M misread as σ_T (off ~10⁴³)" (`HANDOFF.md` §6).
- **The counterfactual flux** (#14 §4). If the monopoles carried magnetic charge under our electromagnetism, "The flux at dark-matter density would be F = n v/4 pi ~ 3e-8 /cm^2/s/sr." That exceeds the Parker bound (about 10⁻¹⁵ for M ≲ 10¹⁷ GeV) by 7.5 orders of magnitude, the direct-search limit of the Monopole, Astrophysics and Cosmic Ray Observatory (2.8×10⁻¹⁶ for m ≳ 10¹⁰ GeV) by eight, and the extended Parker bound, 10⁻¹⁶ (M/10¹⁷ GeV), by twelve; "Sector separation is therefore mandatory." The referee: F = 3.18×10⁻⁸ and excesses of 7.50, 8.06 and 12.03 orders, confirmed; with the galactic-acceleration velocity 0.058c instead, "F=1.84e-6; 9.3/9.8/13.8 orders", "conclusion strengthened" (Step 2). See [monopole flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches).
- **Round 2's correction.** The extended Parker bound "⇒ our-U(1) exclusion is ~7 orders, not 5" (`HANDOFF.md` §6). The v3 worklog (R3): "Excess at the 10¹⁶ benchmark: 6.98 orders [V]", with "Charge scaling: (g/g_D)⁻² at high mass, (g/g_D)⁻¹ at low mass [Kobayashi–Perri 2023, arXiv:2307.07553]". For the 10⁻¹⁵ Parker value it says to cite the Particle Data Group's 2024 review or Turner–Parker–Bogdan, Phys. Rev. D 26, 1296 (1982), "not Parker 1970 alone. That value holds for M ≲ 10¹⁷ GeV."
- **Why it does not apply.** Sector separation is postulate [P4](/wiki/program/postulates/p4-polarized-matter), taken strictly since round 3, and with the hidden photon massless, mixing gives the monopoles no visible magnetic flux ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)). The flux therefore stands only as the reason for the separation; the program's own monopole test is [row 8](/wiki/predictions/monopole-null).

## Sources

- `review/round3-adjudication.md` 'What survives v3' — the arithmetic survives
- `HANDOFF.md` §6 — v2's numbers and the round-1 and round-2 referee errors
- `review/round3/referee/audit-notes.md` Step 2 — every value recomputed; Step 4(c) — the plasma caveat
- `review/v3-worklog.md` 'Round-2 pending list' (R3) — the extended Parker bound and charge scaling; 'Verified references for v3' — how to cite the Parker value
- `notes/knot-dark-matter-standalone.md` §3 — densities and spacing; §4 — σ_T/M and the counterfactual flux
