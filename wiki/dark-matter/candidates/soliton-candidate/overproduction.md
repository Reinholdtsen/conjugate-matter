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
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "notes/knot-dark-matter-standalone.md §3"
---

*Overproduction at the benchmark is the corrected abundance result that retired the soliton candidate. If one monopole forms per Hubble volume when the hidden symmetry breaks — the least that causality allows — the monopoles match the observed dark-matter density only for a mass M\* of 2.9–4.4×10¹² GeV, and heavier monopoles are overproduced in proportion to the fourth power of their mass. At #14 v3's benchmark of 3×10¹³ GeV they would exceed the observed density 2.1×10³ to 1.2×10⁴ times, and realistic production at the transition makes the excess larger still. The result stands and is checked by the program's verification gate; it is why a superheavy monopole could survive only with an arbitrary dilution factor, which would remove its mass prediction.*

**Status:** Alive — a standing result of round 3 (ruling 2, upheld), tagged [V] in #11 §12 and gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). The Kibble–Zurek figures are the referee's; ruling 3 upheld them, but the adjudicator "did not re-run the referee's Kibble–Zurek integration", so they are accepted, not verified.

## Key facts

- **The relation.** With the 't Hooft–Polyakov mass M = 4πf v/g_d ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)), T_c ~ v, and p = 104.31 for one defect per Hubble volume ([the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)), the script computes the mass at which the relic density equals the observed one; heavier masses are overproduced as (M/M\*)⁴ (#14 §3):

  ```text
  M* = r · (ρ_DM M_Pl³ / (r p s₀))^(1/4),   r = 4πf/g_d,   f = 1 to 1.787
  overproduction at mass M = (M/M*)⁴
  ```

- **The numbers** [V]. Ruling 2: "At minimum production M\* = 2.9–4.4×10¹² GeV. The 3×10¹³ benchmark is overproduced 2.1×10³–1.2×10⁴ times." #11 §12 carries both with [V] and adds: "Realistic production lowers the viable mass much further." Gate output: `M* at minimum production = 2.9-4.4e12 GeV  [2.873e+12-4.441e+12]` and `the 3e13 benchmark is overproduced 2.1e3-1.2e4 times  [2.08e+03-1.19e+04]`, both passing. The arbitration run gives "f=1.0: M\* (Kibble minimum production) = 2.87e+12 GeV; v = 1.38e+11; 3e13 overproduced x1.2e+04" and "f=1.787: ... = 4.44e+12 GeV; v = 1.20e+11; 3e13 overproduced x2.1e+03".
- **What v3 had claimed** (#14 §3): "This gives a Kibble-consistent mass M\* ~ (0.9-3.7)e13 GeV ... We adopt the benchmark M = 3e13 GeV"; the abstract placed the mass "at about 1e13 to 4e13 GeV with no dilution required". The referee: the band's "arithmetic reproduces, but rests on wrong p", and "The abstract's "no dilution required" fails at the benchmark" (Step 2; Step 4(a) item 1).
- **Realistic production only adds** (Step 4(a) item 3). Kibble–Zurek production followed by annihilation in the hidden plasma gives, at the benchmark, Ω/Ω_DM = 1.1×10¹²–2.2×10¹² in the referee's integration and 1.2×10⁹–2.2×10¹¹ in the Liveoak–Maharana–Wells analytic estimate: "Either way the annihilation does not rescue it." Starting from the Kibble minimum, annihilation "is irrelevant in that case and overproduction 4.9e3 - 9.8e4 (xi=0.76..0.5) stands." First-order bubble counting gives "p ~ 104 (beta/H)^3 = 1e2-1e8" (item 2). See [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) and [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art).
- **With the colder hidden sector** that dark radiation requires (Step 4(a) item 1): "Corrected Kibble-minimum M\* = 2.87e12-4.44e12 GeV (xi=1), 2.34e12-3.61e12 GeV (xi=0.76); benchmark 3e13 overproduced by 2.1e3-2.7e4" ([thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)). The referee's variant with one defect per (4π/3)H⁻³ gives 4.11×10¹²–6.35×10¹² GeV; the record uses one per H⁻³.
- **The earlier "point, not a window"** (superseded). The v3 worklog's F1 found that "Kibble with p = 1 closes at a single point, M\* ≈ 3.0×10¹³ GeV", with dilution "(M/M\*)⁴" above it, "1.3×10¹⁰ at the 10¹⁶ benchmark"; Paul then moved the benchmark to 3×10¹³ GeV (decided 2026-10-19). Those numbers rest on the wrong p. Against the corrected M\*, the referee's dilution at 10¹⁶ GeV is 2.6×10¹³ (Step 2).
- **The consequence** (Decision 2). Rescuing the superheavy candidate (route (b)) "restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass would then no longer be a prediction, and the program does not trade falsifiability for survival" ([inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution); [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — the [V] numbers
- `review/round3-adjudication.md` 'Rulings' 2–3 — the corrected mass and overproduction, and the Kibble–Zurek note; 'Decisions' 2 — route (b) rejected
- `verify/soliton_obituary.py` — the relation as coded and the gated values
- `review/round3/adjudicator/round3_arb.out` — the arbitration run
- `review/round3/referee/audit-notes.md` Step 2, Step 4(a) — the referee's recomputation, Kibble–Zurek and bubble counting, the colder-sector values
- `review/v3-worklog.md` 'Findings neither referee raised' — F1
- `notes/knot-dark-matter-standalone.md` §3 — v3's band, benchmark and (M/M\*)⁴ scaling
