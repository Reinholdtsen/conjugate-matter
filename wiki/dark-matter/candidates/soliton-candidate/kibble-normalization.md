---
title: "Obituary: the Kibble normalization"
weight: 50
status: dead
description: "v3's yield n/s ~ p(T_c/M_Pl)³ with p = 0.023 dropped the factor (1.66√g*)³; one defect per Hubble volume gives p ≈ 104, the causal minimum, and the reduced-Planck 'factor of 3' was an artefact."
provenance: [V]
sources:
  - "review/round3-adjudication.md 'Rulings' 1–3"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "verify/soliton_obituary.py"
  - "review/round3/adjudicator/round3_arb.out"
  - "review/round3/adjudicator/round3_arb.py"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 5"
  - "review/round3/referee/step2a.out"
  - "review/round3/referee/step4.out"
  - "review/round3/referee/step4d.out"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "review/skeptic-review-console.html"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3-adjudication.md 'Rulings' 13"
---

*The Kibble normalization is the number p in the estimate of how many monopoles a symmetry-breaking phase transition in the early universe leaves behind: the yield n/s = p (T_c/M_Pl)³, the number of monopoles per unit entropy, where T_c is the transition temperature and M_Pl the Planck mass. Version 3 of the soliton manuscript #14 used p ≈ 0.023 and treated p = 1 as an upper end. The round-3 referee showed that 0.023 is what the formula gives when the expansion rate of the universe is written without its numerical prefactor; with the prefactor, one monopole per Hubble volume gives p ≈ 104. Because causality requires at least about that many, the value is a minimum, not a maximum. The correction moved the mass at which the monopoles would make up all the dark matter from v3's (0.9–3.7)×10¹³ GeV down to 2.9–4.4×10¹² GeV, and the candidate was retired.*

**Status:** Dead — v3's value. The corrected p = 104.31 is [V] (#11 §12, "p ≈ 104 [V]") and gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). Round-3 ruling 1 upheld the finding, and the adjudicator's evidence ends "My error came from misremembering the formula" ([round-3 verdict and rulings](/wiki/method/review/round-3/rulings)). Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); listed in [the graveyard](/wiki/status/graveyard).

## The quantity being normalized

### The yield

A relic is counted by its yield, the number density n divided by the entropy density s [T]. Expansion dilutes both in the same way, so the yield stays fixed once nothing creates or destroys the particles, and today's density follows from the present entropy density s₀ ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)). For monopoles formed at a transition, the yield is set at the transition and, if annihilation is negligible, carried unchanged to the present.

### One defect per horizon

[The Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) estimates how many defects form [T]. When the universe cools through the transition temperature T_c, the field picks a vacuum state independently in regions that have not been in causal contact, and the regions' choices do not match where they meet. A monopole is left wherever the mismatch wraps around a point. Causal contact reaches no farther than about the Hubble length H⁻¹, so the field cannot be aligned over larger distances, and at least about one defect forms per Hubble volume [T]. The round-3 referee's source for the normalization is Gangui (astro-ph/0110285): "about one monopole per Hubble volume ... n_monop/s ~ 100 (T_c/m_P)^3" (`review/round3/referee/audit-notes.md`, Step 1).

### The prefactor

In the radiation era the Hubble rate is H = 1.66 √g\* T²/M_Pl, with g\* the number of relativistic degrees of freedom, and the entropy density is s = (2π²/45) g\* T³ [T] ([the radiation era](/wiki/cosmology/early-universe/radiation-era)). One defect per Hubble volume means n ≈ H³ at T_c. The arbitration script `review/round3/adjudicator/round3_arb.py` codes the resulting normalization as the cube of the Friedmann prefactor times 45/(2π² g\*); in the notation of #11 §12:

```text
n/s = p (T_c/M_Pl)³                       H = 1.66 √g* T²/M_Pl,   s = (2π²/45) g* T³
one defect per H⁻³:   p = (1.66 √g*)³ · 45/(2π² g*)
```

Its output at g\* = 100 (`round3_arb.out`):

```text
1.66 check: sqrt(8 pi^3/90) = 1.6602
p, one defect per H^-3, non-reduced M_Pl: 104.31
p, one defect per H^-3, reduced M_Pl:     0.828
p used in v3 (45/(2 pi^2 g*)):             0.0228
```

The two values of p for one defect per Hubble volume describe the same count. The reduced Planck mass M̄_Pl = M_Pl/√(8π) [T] is the other common convention, and the Friedmann prefactor changes with it, so p does too. The referee's check: "n/s = 0.828 (T/MPl_red)^3 ; check = 104.31*(MPl_red/MPl)^3 = 0.828" (`step4d.out`).

## What v2 and v3 used

- **#14 v2** wrote the yield as "n/s ~ p (Lambda_c/M_Pl)^3 with p = O(1)", with Λ_c the transition scale (`review/skeptic-review-console.html`, which embeds v2). #11 §12 records it as "normalized at p = 1 (#14 v2)".
- **#14 v3** (§3): "The Kibble mechanism [18] at a post-inflationary transition with T_c ~ v yields n/s ~ p (v/M_Pl)^3. One monopole per horizon volume with g\* = 100 gives p ~ 0.023; we take p = 1 as the upper end." Here v is the symmetry-breaking scale of the hidden sector, so T_c ~ v.
- **The v3 worklog**, whose finding F1 preceded v3, used the same value: "The horizon-counting p is ≈ 0.023" (`review/v3-worklog.md`, 'Findings neither referee raised').

v3 thus bracketed p between 0.023 and 1, and took the larger value to be the upper end of the abundance.

## Why it failed

### The dropped factor

The referee recomputed the one-per-horizon normalization from independently chosen constants and found 104.3 where v3 had 0.023: "0.0228 = 45/(2pi^2 100) i.e. H^3 without (1.66 sqrt g\*)^3 = 4576", verdict "DISCREPANT (factor ~1e3-5e3)" (`review/round3/referee/audit-notes.md`, Step 2). In the formula above, 45/(2π² g\*) is what remains when the Friedmann prefactor 1.66 √g\* is set to one, that is, when H is written as T²/M_Pl. The referee's script prints it directly: "45/(2 pi^2 * 100) = 0.0228 <- equals n=(T^2/MPl)^3 i.e. H without 1.66 sqrt(g\*)" and "missing factor (1.66 sqrt(100))^3 = 4575.6" (`step2a.out`).

Ruling 1, upheld: "My code: p = 104.31 with M_Pl, 0.828 with the reduced M_Pl. v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³. My error came from misremembering the formula." #11 §12 carries the corrected value: "One defect per Hubble volume gives p ≈ 104 [V], and that is the causal minimum".

### A floor, not a ceiling

The second error was the direction. One defect per Hubble volume is the least a transition can produce, because the field cannot be correlated beyond the causal horizon [T]; any slower or more violent transition makes more. Ruling 3, upheld: "Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more". The referee judged v3's bracket p ∈ [0.023, 1] unreasonable for that reason: one per horizon is a causal lower bound, so p "should be >= ~25-100, not <= 1" (Step 2). The lower figure, 25, counts one defect per (4π/3)H⁻³ rather than per H⁻³ ("p(one per (4pi/3)H^-3) = 24.90", `step2a.out`); the record uses H⁻³.

Two mechanisms add to the floor [T]:

- **Kibble–Zurek dynamics.** Near a continuous transition the field's response slows, and the correlation length freezes at a value well below the horizon, so many defects form per Hubble volume. The referee took the count from Liveoak–Maharana–Wells, eq. 13: "Kibble-Zurek gives n ~ lambda H T_c^2, i.e. (M_Pl/T_c)^2 per horizon" (Step 2).
- **Bubble nucleation.** A first-order transition proceeds by bubbles of the new phase, and defects form where bubbles meet. The referee's estimate: "bubble counting gives p ~ 104 (beta/H)^3 = 1e2-1e8", where β/H is the nucleation rate in Hubble units, taken from 1 to 100 (`step4.out`). v3 itself considered a first-order transition, in §4, with "f\*/H\* = 1-100", so the referee called its bracket "flatly inconsistent with "p = 1 as the upper end" of Sec. 3" (Step 4(a) item 2).

The literature supports the floor. Murayama and Shu, as ruling 3 quotes their abstract: Kibble "drastically underestimates the production of topological defects" ([topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).

## The reduced-Planck "factor of 3" was an artefact

v3 reported a spread in its mass band from the choice of Planck mass: the mass "M\* ~ (0.9-3.7)e13 GeV; the reduced-Planck convention lowers it by a factor of about 3" (#14 §3). v2 had said the same: "the reduced-Planck convention shifts both downward by a factor ~3".

The referee reproduced the factor and identified it as an artefact: "reduced-Planck factor | ~3 lower | 3.350 | arithmetic OK, but it is a convention artefact, not a physical spread (p must be recomputed consistently)" (Step 2). v3 had swapped M_Pl for the reduced value while holding p fixed. Since n/s = p (T_c/M_Pl)³, that raises the yield, and the closing mass M\* scales as (M_Pl³/p)^{1/4}, so it falls by the factor the referee printed, "reduced-Planck 'convention' factor (MPl/MPl_red)^(3/4) = 3.350" (`step2a.out`). But p belongs to the convention: with M̄_Pl the same physical count is p = 0.828, and with that value the shift disappears. Ruling 2: "The "reduced-Planck factor of 3" was not a convention spread: consistently normalized, the two conventions agree." The gate checks exactly this: `the two Planck conventions agree when p is normalized consistently`.

The referee added a reading of v3's lowered edge (Step 5): "p ~ 1 is (to 17%) the REDUCED-Planck normalisation of one-per-horizon (0.828, step4d.out)". v3's reduced-Planck variant therefore came close to the right answer: its lower edge, 2.74×10¹² GeV, sits beside the corrected Kibble minimum, 2.87×10¹² GeV ("manuscript band lower edge /3.35 = 2.740e+12 GeV vs corrected Kibble-minimum lower edge 2.873e12", `step4d.out`).

## Why the manuscript's own check missed it

Every number in v3 was gated in a script, `knot_numbers.py`, and v3 §6 claimed that "All numerical statements in Secs. 2-4 were computed by executed code rather than by hand." The script reproduced the wrong p without complaint. Round-3 lesson 2: "An anchor must be independent of the paper. v3's Kibble anchor reproduced v2's own number and so tested nothing. The replacement anchors are the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume." Ruling 13 states the general point: "The code checked the arithmetic of a wrong model." Both are now method: [independent anchors](/wiki/method/verification/independent-anchors) and [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model).

## The corrected value in the gate

`verify/soliton_obituary.py` replaced the old script on 2026-10-19. It checks its two anchors first, a textbook identity and a published value, and only then the ruling's numbers. Current output:

```text
== Anchors
PASS  Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl
PASS  one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)  [p = 104.31]

== Kibble normalization (ruling 1)
PASS  p = 104.31 with M_Pl  [104.3106]
PASS  p = 0.828 with reduced M_Pl  [0.8279]
PASS  v3's 0.0228 drops (1.66 sqrt(g*))^3 ~ 4.6e3  [4575.6]
```

The Gangui paper is the script's anchor; #11's reference list does not cite it.

## What followed

With p = 104.31 the abundance closes at M\* = 2.9–4.4×10¹² GeV, and v3's benchmark of 3×10¹³ GeV is overproduced 2.1×10³–1.2×10⁴ times (ruling 2; [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)). The referee's verdict named this as the single weakest link: "the Kibble abundance / mass determination (p=0.023 instead of >= 25-104; Kibble treated as an upper end when it is the causal minimum ...)" (Step 5). The banner on the withdrawn manuscript states the consequence: "So the mass band, the benchmark's "no dilution required" and the ψ relic window are wrong." The candidate was retired ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — p = 1 (v2), p ≈ 0.023 (v3), p ≈ 104 [V], "the causal minimum"
- `review/round3-adjudication.md` 'Rulings' 1–3 — the finding, the correction, the convention and the floor; 'Rulings' 13 and 'Lessons (now in CLAUDE.md)' — the circular anchor
- `verify/soliton_obituary.py` — the anchors and the gated values
- `review/round3/adjudicator/round3_arb.py` and `review/round3/adjudicator/round3_arb.out` — the arbitration run
- `review/round3/referee/audit-notes.md` Step 1 — the Gangui normalization; Step 2 — the recomputation and the bracket; Step 4(a) — bubble counting against v3 §4; Step 5 — the weakest link and the reduced-Planck reading
- `review/round3/referee/step2a.out`, `review/round3/referee/step4.out`, `review/round3/referee/step4d.out` — the referee's printed values
- `notes/knot-dark-matter-standalone.md` §3 — v3's normalization and "factor of about 3"; §4 — the first-order transition; banner — the consequence
- `review/skeptic-review-console.html` — v2's p = O(1)
- `review/v3-worklog.md` 'Findings neither referee raised' — F1's use of 0.023
