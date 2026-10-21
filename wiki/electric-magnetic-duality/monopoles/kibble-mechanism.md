---
title: "The Kibble mechanism"
weight: 30
status: established
description: "Causality forces at least about one defect per horizon at a symmetry-breaking transition; Kibble–Zurek dynamics and bubble nucleation only add more — a floor, not a ceiling."
provenance: [T, V]
sources:
  - "review/round3-adjudication.md 'Rulings' 3"
  - "review/round3-adjudication.md 'Rulings' 1"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/step4.out"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md ref [28]"
  - "verify/soliton_obituary.py 'Anchors'"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md ref [18]"
---

*The Kibble mechanism, proposed by Tom Kibble in 1976, is the standard account of how topological defects such as monopoles, strings and domain walls form when the early universe cools through a symmetry-breaking transition. Regions farther apart than the horizon, the distance light has travelled since the Big Bang, have had no contact, so the field settles into unrelated vacuum states in different regions, and defects are left where those regions meet. This gives at least about one defect per horizon volume, and that count is a minimum: slow transitions (Kibble–Zurek dynamics) and first-order transitions, which proceed by bubbles, make more. In the program the count decided the fate of the soliton dark-matter candidate, whose manuscript had normalized it too low and treated it as an upper end.*

**Status:** Established — [T] for the mechanism and for the floor, which the checkpoint supports with Murayama–Shu [28S]; the one-defect-per-Hubble-volume yield p ≈ 104 is [V] (#11 §12), recomputed in `verify/soliton_obituary.py` against an independent anchor ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). Round 3 upheld the floor as [ruling 3](/wiki/method/review/round-3/rulings); the adjudicator did not re-run the referee's Kibble–Zurek integration.

## Key facts

- **The yield** ([#11](/wiki/history/documents/checkpoint) §12): "The Kibble estimate n/s = p (T_c/M_Pl)³", where n/s is the number of defects per unit entropy, T_c the transition temperature and M_Pl the Planck mass.
- **One defect per Hubble volume** (#11 §12): "gives p ≈ 104 [V], and that is the causal minimum". The gate's anchors (`verify/soliton_obituary.py`) are "Friedmann: H = 1.66 sqrt(g\*) T^2/M_Pl" and "one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)", and the gate prints p = 104.31. Normalized with the reduced Planck mass, the same count gives p = 0.828 (ruling 1).

```text
n/s = p (T_c/M_Pl)³
one defect per Hubble volume:   p = 104.31  (Planck mass M_Pl)
                                p = 0.828   (reduced Planck mass)
```

- **A floor, not a ceiling** (ruling 3, upheld): "Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more". The evidence is Murayama–Shu (arXiv:0905.1720), whose abstract, as the round-3 audit quotes it, says that the "Kibble mechanism drastically underestimates the production of topological defects" [28S].
- **How much more** (round-3 audit). For a second-order transition, Kibble–Zurek production gives n ~ λ H T_c², "i.e. (M_Pl/T_c)^2 per horizon" (Step 2). For a first-order transition, "bubble counting gives p ~ 104 (beta/H)^3 = 1e2-1e8" (Step 4(a), item 2); `review/round3/referee/step4.out` prints p ~ 10², 10⁵ and 10⁸ for β/H = 1, 10 and 100. The audit concluded that p "should be >= ~25-100, not <= 1" (Step 2); its table gives p = 24.9 when the horizon volume is taken as (4π/3)H⁻³ rather than H⁻³. The adjudication and the gate use H⁻³.
- **The program's error** (#14 §3; ruling 1). [#14](/wiki/dark-matter/candidates/soliton-candidate) v3 wrote that one monopole per horizon volume "gives p ~ 0.023; we take p = 1 as the upper end." Ruling 1: "v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³." See [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) and, for the consequence, [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction).
- **The anchor lesson** (round-3 lessons, item 2): "v3's Kibble anchor reproduced v2's own number and so tested nothing. The replacement anchors are the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume" ([independent anchors](/wiki/method/verification/independent-anchors)).
- **The original paper** (#14 [18]): T. W. B. Kibble, J. Phys. A 9, 1387 (1976), titled "Topology of Cosmic Domains and Strings" (the worklog's correction). The round-3 audit summarizes its abstract: "formation of walls, strings or monopoles depends on homotopy groups".

## Used by

- [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) — #14's p = 0.023 and the corrected p ≈ 104.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — the closing mass at minimum production.
- [Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) — dropped because its premise, Kibble as a ceiling, is inverted.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — the one-per-Hubble-volume anchor.

## Sources

- `review/round3-adjudication.md` 'Rulings' 1 and 3, 'Lessons' — the corrected normalization, the floor and its evidence, and the anchor lesson.
- `papers/broken-born-checkpoint-v2.md` §12, ref [28] — the yield, p ≈ 104 [V] as the causal minimum, and Murayama–Shu [S].
- `verify/soliton_obituary.py` — the Friedmann and one-per-Hubble-volume anchors and p = 104.31.
- `review/round3/referee/audit-notes.md` Step 2, Step 4(a), Step 4(c); `review/round3/referee/step4.out` — Kibble–Zurek and bubble counting, and the Murayama–Shu abstract.
- `notes/knot-dark-matter-standalone.md` §3, ref [18] — v3's p ~ 0.023 "as the upper end" (withdrawn), and the citation of Kibble 1976.
