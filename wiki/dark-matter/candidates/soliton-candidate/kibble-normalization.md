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
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 5"
  - "notes/knot-dark-matter-standalone.md §3"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
---

*The Kibble normalization is the number p in the estimate of how many monopoles a symmetry-breaking phase transition leaves behind: the yield n/s = p (T_c/M_Pl)³, the number of monopoles per unit entropy, where T_c is the transition temperature and M_Pl the Planck mass. Version 3 of #14 used p ≈ 0.023 and treated p = 1 as an upper end. The round-3 referee showed that 0.023 is what the formula gives when the expansion rate of the universe is written without its numerical prefactor; with the prefactor, one monopole per Hubble volume gives p ≈ 104, and because causality requires at least about that many, the value is a minimum rather than a maximum. The correction moved the mass at which the monopoles would make up all the dark matter from v3's (0.9–3.7)×10¹³ GeV down to 2.9–4.4×10¹² GeV, and the candidate was retired.*

**Status:** Dead — v3's value. The corrected p = 104.31 is [V] (#11 §12, "p ≈ 104 [V]") and gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). Round-3 ruling 1 upheld the finding, and the author's note on it reads "My error came from misremembering the formula" ([round-3 verdict and rulings](/wiki/method/review/round-3/rulings)). Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); listed in [the graveyard](/wiki/status/graveyard).

## Key facts

- **What v3 wrote** (#14 §3): "The Kibble mechanism [18] at a post-inflationary transition with T_c ~ v yields n/s ~ p (v/M_Pl)^3. One monopole per horizon volume with g\* = 100 gives p ~ 0.023; we take p = 1 as the upper end." #11 §12 records the history: the estimate "had been normalized at p = 1 (#14 v2) and p ≈ 0.023 (#14 v3)." The v3 worklog's F1 had used the same value: "The horizon-counting p is ≈ 0.023".
- **The dropped factor.** The referee: "0.0228 = 45/(2pi^2 100) i.e. H^3 without (1.66 sqrt g\*)^3 = 4576", verdict "DISCREPANT (factor ~1e3-5e3)" (audit notes, Step 2). Ruling 1, upheld: "My code: p = 104.31 with M_Pl, 0.828 with the reduced M_Pl. v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³." In the notation of the arbitration run:

  ```text
  n/s = p (T_c/M_Pl)³          H = 1.66 √g* T²/M_Pl
  one defect per H⁻³:   p = 104.31 (M_Pl),   p = 0.828 (reduced M_Pl)
  used in v3:           p = 45/(2π² g*) = 0.0228
  ```

- **The gate's check.** `verify/soliton_obituary.py` reproduces it after two independent anchors, `Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl` and `one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)`. Current output: `p = 104.31 with M_Pl  [104.3106]`, `p = 0.828 with reduced M_Pl  [0.8279]`, `v3's 0.0228 drops (1.66 sqrt(g*))^3 ~ 4.6e3  [4575.6]` — all pass.
- **A floor, not a ceiling** (ruling 3, upheld): "Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more". The referee called one defect per horizon a causal lower bound, so that p "should be >= ~25-100, not <= 1" (Step 2, brackets). See [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism); the consequences are [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction).
- **The reduced-Planck "factor of 3"** was an artefact. #14 §3: "the reduced-Planck convention lowers it by a factor of about 3". The referee found the factor, 3.350, to be "a convention artefact, not a physical spread", and ruling 2 agreed: "consistently normalized, the two conventions agree." The referee added that "p ~ 1 is (to 17%) the REDUCED-Planck normalisation of one-per-horizon", so v3's lowered edge, 2.74×10¹² GeV, "is in fact the physically correct Kibble minimum (2.87e12)" (Step 5). The gate checks that `the two Planck conventions agree when p is normalized consistently`.
- **Why v3's own check missed it** (round-3 lesson 2): "v3's Kibble anchor reproduced v2's own number and so tested nothing. The replacement anchors are the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume" ([independent anchors](/wiki/method/verification/independent-anchors)). Ruling 13: "The code checked the arithmetic of a wrong model" ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — p = 1 (v2), p ≈ 0.023 (v3), p ≈ 104 [V]
- `review/round3-adjudication.md` 'Rulings' 1–3 — the finding, the correction and the floor; 'Lessons (now in CLAUDE.md)' — the circular anchor
- `verify/soliton_obituary.py` — the anchors and the gated values
- `review/round3/adjudicator/round3_arb.out` — the arbitration run
- `review/round3/referee/audit-notes.md` Step 2, Step 5 — the referee's derivation and the reduced-Planck reading
- `review/v3-worklog.md` 'Findings neither referee raised' — F1's use of 0.023
- `notes/knot-dark-matter-standalone.md` §3 — v3's normalization
