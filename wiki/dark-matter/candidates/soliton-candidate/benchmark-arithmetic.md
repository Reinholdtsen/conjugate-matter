---
title: "Benchmark-conditional arithmetic"
weight: 110
status: record
description: "Numbers that survive as arithmetic though the benchmark is withdrawn: densities and spacing, a Coulomb σ_T/M ~ 10⁻²⁶ cm²/g, and a counterfactual flux 7.5 orders above the Parker bound that shows why sector separation is mandatory."
sources:
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Rulings' (omitted constraints)"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/step2a.out"
  - "review/round3/referee/step4.out"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/v3-worklog.md 'Verified references for v3'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "HANDOFF.md §6"
  - "review/wiki-build-flags.md item 33"
---

*Benchmark-conditional arithmetic is the set of numbers that #14 v3 computed at its benchmark monopole mass of 3×10¹³ GeV and that remain correct as arithmetic, although the benchmark itself is withdrawn. At that mass, monopoles making up all the [dark matter](/wiki/dark-matter) would be spaced about 420 m apart near the Sun; they would scatter off one another so weakly, [σ_T/M](/wiki/dark-matter/halo-astrophysics/transfer-cross-section#the-soliton-candidates-σ_tm) ~ 10⁻²⁶ cm²/g, that they would behave as collisionless cold dark matter; and if they carried magnetic charge under our own electromagnetism, their flux would exceed the Parker bound by 7.5 orders of magnitude. That last, counterfactual number is why the [hidden sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) has to be separate from ours. The [round-3](/wiki/method/review/round-3) referee recomputed each value from independently chosen constants and confirmed it.*

**Status:** Record — "The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′ overclosure" survives v3 (round-3 adjudication, 'What survives v3'), and the referee marked each value "CONFIRMED" (audit notes, Step 2). #14 §6 lists "the counterfactual flux numbers and cross-section of Sec. 4" as derived. Apart from the W′ overclosure, which has [its own page](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) and is gated, these values are not in [the current gate](/wiki/method/verification/the-gate): v3's own checks of them were retired with the paper.

## What the benchmark was

The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) needed one mass at which to evaluate its candidate. The v3 worklog's finding F1 showed that a pure [Kibble](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) abundance closes at a single mass, and Paul decided: "move the benchmark to M ≈ 3×10¹³, and keep 10¹⁶ with its ~10¹⁰ dilution as a stated alternative" (`review/v3-worklog.md`, 'Findings neither referee raised'). #14 §3: "We adopt the benchmark M = 3e13 GeV, which corresponds to v ~ (0.8-1.4)e12 GeV."

Round 3 withdrew it. Counted correctly, the Kibble mechanism overproduces monopoles of that mass 2.1×10³–1.2×10⁴ times [V] ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction); [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)). The numbers on this page do not depend on the abundance calculation. Each follows from the mass, the observed dark-matter density, a typical galactic speed and the coupling, so each remains a correct statement of what monopoles of 3×10¹³ GeV would be like if they were the dark matter.

## Number density and spacing

If objects of mass M make up all of the dark matter at mass density ρ, their number density is n = ρ/M, and the mean distance between neighbours is about n^(−1/3) [T]. #14 §3:

> Benchmark numbers (M = 3e13 GeV). The mean number density is n ~ 4.2e-20 /cm^3. At the local halo density (0.4 GeV/cm^3) there is one monopole per ~0.075 km^3, a mean spacing of about 420 m, drifting at ~1e-3 c.

The referee recomputed with its own constants (mean dark-matter density "rho_DM mean = 1.2644e-06 GeV/cm^3 = 1.264 keV/cm^3", from Planck 2018's Ω_c h² = 0.120) and checked both local densities (`review/round3/referee/step2a.out`):

```text
mean n = 4.215e-20 /cm^3
rho_loc=0.4: n = 1.333e-14/cm^3, volume per monopole = 0.0750 km^3, spacing n^-1/3 = 421.7 m
rho_loc=0.3: n = 1.000e-14/cm^3, volume per monopole = 0.1000 km^3, spacing n^-1/3 = 464.2 m
```

The audit table marks the mean density and the local volume and spacing "CONFIRMED". The last line uses 0.3 GeV/cm³, which the referee notes is the canonical local density of the Particle Data Group, against #14's 0.4 (Step 2). The drift speed of ~10⁻³ c is the typical speed of matter bound in the Galaxy's [halo](/wiki/dark-matter/halo-astrophysics) [T].

### The earlier benchmark

v2 of #14 had used 10¹⁶ GeV. The [round-2](/wiki/method/review/rounds-one-and-two) referee disputed its densities, and [the handoff](/wiki/history/documents/handoff) records the arbitration (`HANDOFF.md` §6): the referee "fed ρ_DM = 1.26×10⁻³ GeV/cm³ instead of 1.26×10⁻⁶ (the manuscript's own number) — with the right input the closure lands within 3%; conflated mean vs local density labels (manuscript's 1.3×10⁻²² mean and one-per-25-km³ local are both exactly right)." Those numbers belong to the 10¹⁶ GeV benchmark and moved when the benchmark did.

## Self-interaction

### The cross-section

Two monopoles interact through the massless hidden photon with the strong magnetic coupling α_m ~ 34 ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)), a long-range force with the Coulomb form. For such a force the quantity that measures how much scattering changes a particle's motion is the transfer cross-section, σ_T = ∫(1 − cos θ) dσ, which weights each deflection by the momentum it transfers [T]. For a Coulomb force it grows without bound at small angles until the force is screened at large distances, and the cutoff leaves a factor ln Λ, the Coulomb logarithm [T]; #14 takes ln Λ = 10–30. The standard result is

```text
σ_T ≈ 4π α² ln Λ / (μ² v⁴)
```

with μ the reduced mass (M/2 for two equal masses) and v the relative speed [T]. Halo astrophysics constrains σ_T per unit mass, σ_T/M, because the scattering rate per particle is n σ_T v = ρ (σ_T/M) v; cross-sections of order 1 cm²/g produce observable effects ([self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter)) [T].

#14 §4:

> Self-interaction. Monopole-monopole scattering through the hidden photon is Rutherford-like at alpha_m ~ 34 but suppressed by the mass: sigma_T/M ~ 8 pi alpha_m^2 ln(Lambda)/((M/2)^2 M v^4) ~ 1e-26 cm^2/g at v ~ 1e-3 c and M = 3e13 GeV, for ln(Lambda) = 10-30. That is some twenty-six orders below astrophysical sensitivity. The candidate is effectively collisionless cold dark matter, so observed dwarf-galaxy cores must be attributed to baryonic feedback.

The suppression is visible in the formula: σ_T/M falls as the cube of the mass, so even a coupling of 34 cannot make objects of 3×10¹³ GeV scatter appreciably.

### The referee's check

The referee evaluated both the manuscript's formula and the standard one (`step2a.out`):

```text
lnL=10: manuscript formula sigma_T/M = 9.545e-27 cm^2/g ; standard 4pi a^2 lnL/(mu^2 v^4): 4.773e-27 cm^2/g
lnL=30: manuscript formula sigma_T/M = 2.864e-26 cm^2/g ; standard 4pi a^2 lnL/(mu^2 v^4): 1.432e-26 cm^2/g
orders below 1 cm^2/g: 25.7
```

Verdict: "CONFIRMED (factor-2 convention)". #14's 8π is twice the standard 4π; at twenty-six orders of magnitude below sensitivity the factor does not matter.

### What follows, and the caveat

The candidate would have been collisionless cold dark matter. Dwarf-galaxy cores could then not come from dark-matter self-interaction ([dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies)), which #14 made exclusion condition 5: "Demonstration that dwarf cores require dark-sector self-interaction (this candidate cannot supply it)" (§5).

The referee qualified "collisionless" (Step 4(c) item 6). A medium of long-range charges oscillates collectively at its plasma frequency ω_p, and collective instabilities can act on timescales of order 1/ω_p, independently of two-body collisions [T]. The referee's estimates of 1/ω_p for the monopoles (`step4.out`):

```text
local 0.4 GeV/cm3: omega_p = 1.84e-09 s^-1, 1/omega_p = 1.72e+01 yr
cluster ~1e-2 GeV/cm3: omega_p = 2.91e-10 s^-1, 1/omega_p = 1.09e+02 yr
cosmic mean: omega_p = 3.28e-12 s^-1, 1/omega_p = 9.67e+03 yr
```

These are "far shorter than dynamical times; Lasenby 2007.00667 shows such instabilities can matter "many orders of magnitude below" two-body bounds (he gives no constraint). "Effectively collisionless" rests on two-body sigma_T only. Unevaluated, not an indictment." The adjudication listed "Collective magnetic-plasma effects" among the [omitted constraints](/wiki/method/review/round-3/rulings#collective-magnetic-plasma-effects) accepted as a to-do and not re-checked.

In round 1 the referee had misread this quantity: "σ_T/M misread as σ_T (off ~10⁴³)" (`HANDOFF.md` §6), among the referee errors of rounds 1–2 that machine arbitration overturned ([referee failure mode](/wiki/method/review/referee-failure-mode)).

## The counterfactual flux

### Why it was computed

The candidate's monopoles carry magnetic charge under the hidden U(1)_d only. #14 §4 computed what would follow if they were instead magnetic under our electromagnetism:

> Not monopoles of our U(1). If these objects carried magnetic charge under our electromagnetism, they would be classic monopoles and excluded. The flux at dark-matter density would be F = n v/4 pi ~ 3e-8 /cm^2/s/sr. That exceeds the Parker bound (~1e-15 for M <~ 1e17 GeV) [20] by 7.5 orders of magnitude, the MACRO limit for m >~ 1e10 GeV (2.8e-16) [21] by eight, and the extended Parker bound 1e-16 (M/1e17 GeV) [22] by twelve. Sector separation is therefore mandatory. Sec. 2(c) shows it is not undone by kinetic mixing while U(1)_d is unbroken.

For an isotropic population of number density n moving at speed v, the number crossing unit area per unit time per unit solid angle is F = n v/4π [T]. The three limits are explained on [monopole flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches): the Parker bound requires that monopoles accelerated by the Galaxy's magnetic field not drain the field faster than it regenerates; the extended Parker bound applies the same argument to the weaker seed field of the young Galaxy and is proportional to the monopole mass, so it tightens for lighter monopoles; MACRO, the Monopole, Astrophysics and Cosmic Ray Observatory, searched for them directly [T]. The round-3 referee found each figure supported by its source: the Particle Data Group's 2024 review, eq. (95.9), for the Parker bound; MACRO's Table 2, "<= 2.8e-16 for m >~ 1e10 GeV, beta > 1e-4"; and the abstract of Adams et al. 1993, "F <= 1e-16 (m/1e17 GeV) cm^-2 s^-1 sr^-1" (Step 1).

### The numbers

The referee's recomputation (`step2a.out`) at #14's speed and at the speed the Galactic field would give a heavy monopole:

```text
v=1e-3 c (1.000e-03 c): F = 3.181e-08 /cm^2/s/sr ; log10 excess: Parker 7.50, MACRO(2.8e-16) 8.06, ext.Parker 12.03 (PDG form 12.02)
v=PDG eq.95.8 v_mag=1e-3c(1e17/M)^0.5 (5.774e-02 c): F = 1.836e-06 /cm^2/s/sr ; log10 excess: Parker 9.26, MACRO(2.8e-16) 9.82, ext.Parker 13.79 (PDG form 13.78)
```

The first line confirms #14's 7.5, 8 and 12 orders. The second uses eq. (95.8) of the Particle Data Group (PDG) review, by which a Dirac-charge monopole heavier than about 10¹¹ GeV is accelerated by the Galactic field to v ~ 10⁻³ c (10¹⁷ GeV/M)^(1/2) (Step 1); the faster speed raises the flux, "conclusion strengthened" (Step 2). The extended bound gives the largest excess because it tightens as the mass falls, and the benchmark lies far below 10¹⁷ GeV.

### Corrections along the way

- **The extended bound** (round 2). The handoff records the round-2 finding: "extended Parker bound (Adams et al. 1993: F ≲ 10⁻¹⁶(m/10¹⁷ GeV) ⇒ our-U(1) exclusion is ~7 orders, not 5 — cite it)" (`HANDOFF.md` §6). That was at v2's 10¹⁶ GeV benchmark; the worklog's item R3 confirms "Excess at the 10¹⁶ benchmark: 6.98 orders [V]" and adds: "Others quote a 1.2×10⁻¹⁶ prefactor, and PDG 2024 Eq. 95.10 adds a low-mass floor." The referee judged the added term "negligible here" (Step 1).
- **Charge scaling.** Worklog R3: "Charge scaling: (g/g_D)⁻² at high mass, (g/g_D)⁻¹ at low mass [Kobayashi–Perri 2023, arXiv:2307.07553]", with g the monopole's magnetic charge and g_D the Dirac charge.
- **Which MACRO row.** When the benchmark moved, so did the applicable limit: "At 3×10¹³, the counterfactual MACRO limit is ≤ 2.8×10⁻¹⁶ (m ≳ 10¹⁰ GeV row), not 1.4×10⁻¹⁶ (m ≳ 10¹⁶ GeV row)" (worklog F1). The referee calls 1.4×10⁻¹⁶ the "global" figure.
- **How to cite the Parker value.** "For the 10⁻¹⁵ Parker value, cite PDG 2024 or Turner–Parker–Bogdan, PRD 26, 1296 (1982), not Parker 1970 alone. That value holds for M ≲ 10¹⁷ GeV" (worklog, 'Verified references for v3'). The Turner–Parker–Bogdan abstract quotes a different "Parker limit", F ≲ 10⁻¹⁶; the referee: "the manuscript follows PDG; fine" (Step 1).

### Why the counterfactual does not arise

Two facts keep these monopoles from being monopoles of our electromagnetism. The program's postulate [P4](/wiki/program/postulates/p4-polarized-matter) says that "gauge forces do not cross polarizations", and since v2.1 it has been taken strictly, allowing no kinetic mixing beyond what gravity induces ([#11](/wiki/history/documents/checkpoint) §4; [round-3 Decision 1](/wiki/method/review/round-3/decisions#decision-1-strict-sector-separation)). And even with some mixing, an unbroken hidden U(1) gives the monopoles no visible magnetic flux: the worklog's finding L1, from Hiramatsu et al., that kinetic mixing "does not induce the QED magnetic flux in the U(1) symmetric phase", where QED is quantum electrodynamics ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).

The flux numbers therefore enter v3 only as the reason for separation. Worklog L1: "Parker and MACRO stay in v3 only as the reason sector separation is needed: they show what would happen if these objects were monopoles of our U(1)." #14 made a real flux exclusion condition 2: "Any confirmed magnetic-monopole flux of our U(1) at dark-matter abundance." The program's own monopole prediction is [row 8](/wiki/predictions/monopole-null).

## Status of the numbers

| Quantity | #14 v3 | Referee (Step 2) | Verdict |
| --- | --- | --- | --- |
| Mean number density | ~4.2e-20 cm⁻³ | 4.215e-20 | confirmed |
| Volume per monopole, spacing (0.4 GeV/cm³) | ~0.075 km³, ~420 m | 0.0750 km³, 421.7 m | confirmed |
| σ_T/M | ~10⁻²⁶ cm²/g | 0.95e-26 – 2.9e-26 | confirmed (factor-2 convention) |
| Counterfactual flux | ~3e-8 cm⁻² s⁻¹ sr⁻¹ | 3.18e-8 | confirmed |
| Excess over Parker, MACRO, extended Parker | 7.5, 8, 12 orders | 7.50, 8.06, 12.03 | confirmed |

The adjudication's 'What survives v3' keeps "The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′ overclosure". When v3 was drafted, each of these numbers was a gated check in the predecessor script `knot_numbers.py`, last in history at 96f58da ("Every number it quotes is a gated check", worklog 'v3 as drafted'). That script was replaced by `verify/soliton_obituary.py`, which checks the corrected record and, among these, only the W′ overclosure; its docstring claims wider coverage (flag 33 in `review/wiki-build-flags.md`). The adjudication on the replacement: "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything" ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script); [round-3 decisions](/wiki/method/review/round-3/decisions)). The arithmetic stands on the referee's recomputation and the benchmark stays withdrawn ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## Sources

- `review/round3-adjudication.md` 'What survives v3' — the arithmetic survives; the omitted-constraints list — collective plasma effects; 'Decisions', "Executed the same day" — the predecessor script retired
- `review/round3/referee/audit-notes.md` Step 1 — the flux bounds checked against their sources, PDG eq. (95.8); Step 2 — every value recomputed; Step 4(c) item 6 — the plasma caveat
- `review/round3/referee/step2a.out` — the density, cross-section and flux lines quoted; `review/round3/referee/step4.out` — the plasma frequencies
- `notes/knot-dark-matter-standalone.md` §3 — the benchmark, densities and spacing; §4 — σ_T/M and the counterfactual flux; §5 — exclusion conditions 2 and 5; §6 — listed as derived
- `review/v3-worklog.md` 'Findings neither referee raised' (F1, L1) — the benchmark decision, the MACRO row, the flux as the reason for separation; 'Round-2 pending list' (R3) — the extended Parker bound and charge scaling; 'Verified references for v3' — how to cite the Parker value; 'v3 as drafted (2026-10-19)' — the predecessor gate
- `papers/broken-born-checkpoint-v2.md` §4 — P4 taken strictly
- `HANDOFF.md` §6 — v2's numbers and the round-1 and round-2 referee errors
- `review/wiki-build-flags.md` item 33 — the gate script's claimed coverage against what it checks
