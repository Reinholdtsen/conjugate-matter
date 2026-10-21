---
title: "The soliton-obituary script"
weight: 80
status: method
description: "verify/soliton_obituary.py recomputes every number that the round-3 rulings and the #11 §12 obituary quote, after anchors independent of the manuscript; it replaced knot_numbers.py, which checked the withdrawn paper's own claims."
provenance: [V]
sources:
  - "verify/soliton_obituary.py"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md header"
  - "review/v3-worklog.md 'New open items (to compute before v3 states anything about them)'"
  - "CLAUDE.md 'Layout'"
---

*The soliton-obituary script, `verify/soliton_obituary.py`, recomputes every number in the record of why the program's superheavy-soliton dark-matter candidate failed: the corrected count of monopoles formed in the early universe, the mass at which their abundance would match the observed dark matter, the overproduction at the withdrawn manuscript's benchmark mass, and the other figures that review round 3 upheld. Before computing any of these it reproduces standard cosmology results that do not depend on the manuscript. It replaced an earlier script, knot_numbers.py, which had checked the manuscript's own claims and passed a wrong normalization. The candidate it documents is dead; the script keeps the record of that death reproducible.*

**Status:** Method — the numbers it gates carry [V] in #11 §12: "The [V] numbers here are gated in `verify/soliton_obituary.py`." — runs in [the gate](/wiki/method/verification/the-gate); it checks the record of a dead claim, [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary). The last recorded run ended "OK — every number the round-3 record quotes reproduces."

## Key facts

- **Purpose and model.** The docstring: "every number that review/round3-adjudication.md and the §12 obituary of papers/broken-born-checkpoint-v2.md (v2.1) quote for the withdrawn soliton candidate (#14 v3), recomputed and checked." Root `CLAUDE.md` lists it as "the round-3 record". It cites #11 v2.1; #11 is now v2.2, whose changes do not include §12. The model, from the docstring: `SU(2)_d -> U(1)_d by an adjoint Higgs with vev v; Dirac doublet psi of dark charge g_d/2 = e (hypothesis H); monopole mass M = 4 pi f v / g_d, f = 1 (BPS) to 1.787; T_c ~ v.` Abundances follow "Kibble with one defect per Hubble volume, the causal minimum", and the reference constants are those of the Particle Data Group and Planck 2018 (`Reference constants: PDG and Planck 2018 values.`), among them `M_PL = 1.22089e19` (GeV) and `S0 = 2891.2` (cm⁻³), with the dark-matter density built from Ωh² = 0.120. See [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector).
- **Anchors first.** "Anchors come first and are independent of the manuscript (a textbook identity; a published value)." They are the Friedmann coefficient 1.66, the Kibble count "n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)" with `[p = 104.31]`, a standard freeze-out relic ("Omega h^2 ~ 0.12 (within x2)", which passes inside a window and prints no value), and "one extra neutrino species at T_nu gives 1" for ΔN_eff. See [Independent anchors](/wiki/method/verification/independent-anchors).
- **Ruling 1, the Kibble normalization.** `p = 104.31 with M_Pl  [104.3106]`; `p = 0.828 with reduced M_Pl  [0.8279]`; `v3's 0.0228 drops (1.66 sqrt(g*))^3 ~ 4.6e3  [4575.6]`. See [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) and [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism).
- **Ruling 2, mass and overproduction.** `M* at minimum production = 2.9-4.4e12 GeV  [2.873e+12-4.441e+12]`; `the 3e13 benchmark is overproduced 2.1e3-1.2e4 times  [2.08e+03-1.19e+04]`; and "the two Planck conventions agree when p is normalized consistently". See [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction).
- **Rulings 4 and 5, the ψ relic window and dark radiation.** Ruling 4: `10% of the dark matter at 45-49 GeV  [45.2-48.8]`; `100% at 146-158 GeV  [146.4-158.0]`. See [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window). Ruling 5: `95% bound Delta N_eff < 0.286  [0.286]`; `xi < 0.760  [0.7601]`; and a knock-on check on the upper frequency of the gravitational-wave band, `knock-on: GW upper end 3.2e7 Hz at the withdrawn benchmark  [3.17e+07]`. See [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history).
- **The surviving exclusion.** Under the heading "Minimal adjoint-only sector (survives, benchmark-conditional)": `stable W'+- overclose by 1e16-1e17  [9.5e+15-2.0e+17]`. #11 §12 carries it as "its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V]". See [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure).
- **What it replaced.** Executed the day of the round-3 decisions: knot_numbers.py, which checked v3's claims, "was replaced by `verify/soliton_obituary.py`, which checks every number this record quotes, with independent anchors. The v3 checks are in history at 96f58da." And: "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything." (`review/round3-adjudication.md`, 'Decisions'). The old script's flaw, in lesson 2: "v3's Kibble anchor reproduced v2's own number and so tested nothing." Its freeze-out self-check gave "Ω h² = 0.108" (`review/v3-worklog.md`); that value belongs to the retired script.
- **Not gated.** The script has no checks for rulings 3 and 6–13. Ruling 3's Kibble–Zurek overproduction was not re-run by the adjudicator, and rulings 6 and 9 were "Accepted, not re-checked" (`review/round3-adjudication.md`, 'Rulings'; [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings)).

## Sources

- `verify/soliton_obituary.py` — the docstring, the model, the anchors and every check quoted above
- `review/round3-adjudication.md` 'Rulings', 'Lessons (now in CLAUDE.md)', 'Decisions' — the rulings it checks, the circular anchor, the replacement
- `papers/broken-born-checkpoint-v2.md` §12 — the obituary and its "Checks." line; header — the v2.2 change list
- `review/v3-worklog.md` 'New open items (to compute before v3 states anything about them)' — the retired script's freeze-out self-check
- Root `CLAUDE.md` 'Layout' — "the round-3 record"
