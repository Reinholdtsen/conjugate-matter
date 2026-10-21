---
title: "Overproduction at the benchmark"
weight: 60
status: alive
description: "Correctly counted, the abundance closes at M* = 2.9–4.4×10¹² GeV, the 3×10¹³ GeV benchmark is overproduced 2.1×10³–1.2×10⁴ times, and Kibble–Zurek production only adds to it."
provenance: [V]
sources:
  - "review/round3-adjudication.md 'Rulings' 2–3"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "verify/soliton_obituary.py"
  - "review/round3/adjudicator/round3_arb.out"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/step2a.out"
  - "review/round3/referee/step4.out"
  - "review/round3/referee/step4b.out"
  - "review/round3-adjudication.md 'Verdict'"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md Abstract"
  - "notes/knot-dark-matter-standalone.md §3"
---

*Overproduction at the benchmark is the corrected abundance result that retired the soliton candidate. If one monopole forms per Hubble volume when the hidden symmetry breaks, the least that causality allows, the monopoles match the observed dark-matter density only for a mass M\* of 2.9–4.4×10¹² GeV. Heavier monopoles are overproduced in proportion to the fourth power of their mass, because a heavier monopole forms at a higher temperature, where more of them form per unit entropy. At the benchmark of #14 v3, 3×10¹³ GeV, they would exceed the observed density 2.1×10³ to 1.2×10⁴ times, and realistic production at the transition makes the excess larger still. The result stands and is checked by the program's verification gate. It is why a superheavy monopole could survive only with an arbitrary dilution factor, which would remove its mass prediction.*

**Status:** Alive — a standing result of round 3 (ruling 2, upheld), tagged [V] in #11 §12 and gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). It is a result about #14 v3's model and benchmark, which are withdrawn. The Kibble–Zurek figures are the referee's; ruling 3 upheld the point they support, but the adjudicator "did not re-run the referee's Kibble–Zurek integration", so they are accepted, not verified.

## Statement

#11 §12, in its account of why the [soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) failed:

> At minimum production the abundance closes at M ≈ 2.9–4.4×10¹² GeV [V], and the v3 benchmark of 3×10¹³ GeV is overproduced by 2.1×10³–1.2×10⁴ [V]. Realistic production lowers the viable mass much further.

Round-3 ruling 2, upheld: "At minimum production M\* = 2.9–4.4×10¹² GeV. The 3×10¹³ benchmark is overproduced 2.1×10³–1.2×10⁴ times." "Minimum production" means one monopole per Hubble volume at the transition, the causal floor of [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism).

## The model behind the number

The result is computed in #14 v3's own model, as the gate script states ("Model (as in v3)"). Four ingredients enter.

**The monopole mass.** A hidden SU(2) gauge group broken to U(1) by an adjoint scalar with vacuum value v has 't Hooft–Polyakov monopoles of mass M = 4πf v/g_d, where g_d is the hidden gauge coupling [T] ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole); [the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). #14 §3: "The factor f is 1 in the BPS limit [16] and rises to about 1.79 at large scalar self-coupling." The Bogomolny–Prasad–Sommerfield (BPS) limit is that of vanishing scalar self-coupling [T]. The script takes f = 1 to 1.787. The referee confirmed the upper value, 1.7867, with its own numerical solution of the monopole equations, and noted that it is not in the cited BPS references and is uncited (`review/round3/referee/audit-notes.md`, Steps 1 and 2).

**The coupling.** Under #14's hypothesis H, the smallest hidden charge equals the electron's, which fixes g_d ([the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)). The referee's script prints "gd = 0.60564" and "4 pi/g_d = 20.749;  4 pi f_inf/g_d = 37.072  -> M = (20.7 - 37.1) v" (`step2a.out`); #14 §3 writes "M ~ (21-37) v". The whole spread in M\* below comes from f.

**The transition temperature.** The hidden transition happens at T_c ~ v (#14 §3).

**The yield.** The number of monopoles per unit entropy is n/s = p (T_c/M_Pl)³, with p = 104.31 for one defect per Hubble volume and M_Pl the (non-reduced) Planck mass ([the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)).

The observational inputs are the mean dark-matter density, the present entropy density s₀ and M_Pl. #14 §3 quotes "mean rho_DM = 1.26 keV/cm^3, s_0 ~ 2.9e3 /cm^3 and M_Pl = 1.22e19 GeV"; the script's constants are `RHO_DM = 0.120*1.05371e-5` (GeV cm⁻³), `S0 = 2891.2` (cm⁻³) and `M_PL = 1.22089e19` (GeV), "PDG and Planck 2018 values" (Particle Data Group).

## The relation

Today's monopole density is the mass times the number density, M·(n/s)·s₀, and the yield depends on the mass through v = M/r, with r = 4πf/g_d. Setting the monopole density equal to the observed one and solving for M gives the closing mass in the form the script codes (the algebra is the wiki's reading; the formula is the script's):

```text
M* = r · (ρ_DM M_Pl³ / (r p s₀))^(1/4),     r = 4πf/g_d,   f = 1 to 1.787
overproduction at mass M = (M/M*)⁴
```

The fourth power has a plain origin. At fixed r and p the density of monopoles today is proportional to M times v³, and v is proportional to M, so it grows as M⁴. #14 §3 states the scaling: "Heavier monopoles are over-produced as (M/M\*)^4 and need that much entropy dilution". A heavier monopole means a higher transition temperature, where a Hubble volume contains less entropy, and so more monopoles per unit entropy, each of them heavier.

## The numbers [V]

The gate's output (`verify/soliton_obituary.py`, section "Mass and overproduction (ruling 2)"):

```text
PASS  M* at minimum production = 2.9-4.4e12 GeV  [2.873e+12-4.441e+12]
PASS  the two Planck conventions agree when p is normalized consistently
PASS  the 3e13 benchmark is overproduced 2.1e3-1.2e4 times  [2.08e+03-1.19e+04]
```

The adjudicator's arbitration run gives the two ends separately (`review/round3/adjudicator/round3_arb.out`):

```text
f=1.0: M* (Kibble minimum production) = 2.87e+12 GeV; v = 1.38e+11; 3e13 overproduced x1.2e+04
f=1.787: M* (Kibble minimum production) = 4.44e+12 GeV; v = 1.20e+11; 3e13 overproduced x2.1e+03
```

The smaller f gives the lighter M\* and therefore the larger overproduction at a fixed benchmark. The middle line of the gate's output is the check that the result does not depend on whether M_Pl or the reduced Planck mass is used, once p is normalized in the same convention.

## What v3 had claimed

#14 v3 §3: "This gives a Kibble-consistent mass M\* ~ (0.9-3.7)e13 GeV; the reduced-Planck convention lowers it by a factor of about 3. We adopt the benchmark M = 3e13 GeV, which corresponds to v ~ (0.8-1.4)e12 GeV." Its abstract placed the mass "at about 1e13 to 4e13 GeV with no dilution required".

The referee reproduced v3's band from v3's own inputs, "0.918e13 - 3.644e13", and recorded that the "arithmetic reproduces, but rests on wrong p" (Step 2). With p for one defect per Hubble volume the band becomes "2.87e12 - 4.44e12 (H^-3)", and the benchmark is "overproduced by (M/M\*)^4 = 2.1e3 - 1.2e4 (Kibble minimum)". The referee's conclusion: "The abstract's "no dilution required" fails at the benchmark" (Step 4(a) item 1). The adjudication's verdict names the same failure: "The headline result ("1e13–4e13 GeV, no dilution required") rests on a wrong Kibble normalization."

## With the colder hidden sector

The hidden photon is radiation, and the bound on extra radiation requires the hidden sector to be colder than ours by a ratio ξ < 0.760 (ruling 5; [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)). v3 stated that a colder sector lowers M\* by ξ^{3/4} but quoted its band at ξ = 1 (Step 4(a) item 4). The referee recomputed both (Step 4(a) item 1): "Corrected Kibble-minimum M\* = 2.87e12-4.44e12 GeV (xi=1), 2.34e12-3.61e12 GeV (xi=0.76); benchmark 3e13 overproduced by 2.1e3-2.7e4" (`step4b.out`). A colder hidden sector makes the overproduction worse, not better. The record quotes the ξ = 1 values.

## Realistic production only adds

One defect per Hubble volume is the floor; ruling 3 (upheld): "Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more". The referee estimated both mechanisms at v3's parameters (Step 4(a) items 2–3; `step4.out`):

- **Kibble–Zurek production with annihilation.** Production near a continuous transition, "n ~ lambda H T_c^2 (LMW 2607.20843 eq. 13)", followed by monopole–antimonopole capture in the hidden plasma, using the capture rates of Liveoak–Maharana–Wells (LMW). The referee's integration leaves "Omega/Omega_DM = 1.1e12 - 2.2e12" at the benchmark, and LMW's analytic estimate (their eq. 25) gives "1.2e9 - 2.2e11". "Either way the annihilation does not rescue it."
- **The Kibble minimum with annihilation.** Starting from one defect per Hubble volume, the initial yield, "Kibble-minimum initial Y (7e-20 - 1.4e-18)", lies far below the level at which annihilation acts, so annihilation "is irrelevant in that case and overproduction 4.9e3 - 9.8e4 (xi=0.76..0.5) stands."
- **A first-order transition.** Bubble counting gives "p ~ 104 (beta/H)^3 = 1e2-1e8", where β/H is the bubble nucleation rate in Hubble units.

The adjudicator "did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction)" (ruling 3). The literature agrees on the direction: Murayama and Shu, Kibble "drastically underestimates the production of topological defects" ([topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).

## The count per Hubble volume: a convention

"One defect per Hubble volume" can mean one per H⁻³ or one per (4π/3)H⁻³. The referee computed both: "2.87e12 - 4.44e12 (H^-3); 4.11e12 - 6.35e12 ((4pi/3)H^-3)" (Step 2). The adjudication and the gate use H⁻³. The (4π/3)H⁻³ variant was not adopted, and with either convention the benchmark is overproduced.

## Superseded: the "point, not a window" of the v3 worklog

Before round 3, the v3 worklog had already found that the Kibble estimate fixes one mass rather than a range. Finding F1 (`review/v3-worklog.md`, 'Findings neither referee raised'):

> Kibble with p = 1 closes at a single point, M\* ≈ 3.0×10¹³ GeV. Below it, solitons are under-produced (×0.013 at 10¹³). Above it, the abundance scales as (M/M\*)⁴, so the observed density needs entropy dilution of 1.3×10⁶ at 10¹⁵, **1.3×10¹⁰ at the 10¹⁶ benchmark**, and 1.3×10¹⁴ at 10¹⁷.

F1 also recorded that annihilation would not help at the old benchmark: "Preskill (verified from the scan): annihilation cannot reduce n/T³ below ~10⁻¹⁰ at m ≈ 10¹⁶ GeV." Paul then decided, on 2026-10-19, to "move the benchmark to M ≈ 3×10¹³, and keep 10¹⁶ with its ~10¹⁰ dilution as a stated alternative". v3 kept the conclusion as "This is a point, not a window."

The conclusion that heavier masses need dilution in proportion to (M/M\*)⁴ survives. The numbers do not: they rest on p = 1 (or, in the worklog's aside, p ≈ 0.023), and the worklog's stage values were never reconciled with v3's. Against the corrected M\*, the referee found the dilution needed at 10¹⁶ GeV to be "2.6e13 vs corrected M\*" rather than ~10¹⁰ (Step 2). The record cites only the gated values.

## What follows

A monopole heavier than M\* can still be the dark matter if a late epoch dilutes the monopoles after they form, as reheating after a period of early matter domination would ([inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution)). Round 3's Decision 2 rejected that route for the program: it "restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass would then no longer be a prediction, and the program does not trade falsifiability for survival." #11 §12: "Superheavy masses survive only with a free dilution factor. That removes the mass prediction, which was the candidate's reason to exist." The lighter version, at symmetry-breaking scales up to about 100 PeV, is published prior art ([topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)), and the candidate was retired ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — the [V] numbers and the dilution argument
- `review/round3-adjudication.md` 'Verdict', 'Rulings' 2–3 — the corrected mass and overproduction, the floor and the unchecked Kibble–Zurek figures; 'Decisions' 2 — route (b) rejected
- `verify/soliton_obituary.py` — the model, the relation as coded and the gated values
- `review/round3/adjudicator/round3_arb.out` — the arbitration run
- `review/round3/referee/audit-notes.md` Steps 1–2 — the factor f, v3's band reproduced and corrected, the volume convention, the dilution at 10¹⁶ GeV; Step 4(a) — Kibble–Zurek and bubble counting, the colder-sector values
- `review/round3/referee/step2a.out`, `review/round3/referee/step4.out`, `review/round3/referee/step4b.out` — the referee's printed values
- `review/v3-worklog.md` 'Findings neither referee raised' — F1 and Paul's decision; 'v3 as drafted (2026-10-19)' — the mass relation and benchmark
- `notes/knot-dark-matter-standalone.md` Abstract, §3 — v3's band, benchmark and (M/M\*)⁴ scaling
