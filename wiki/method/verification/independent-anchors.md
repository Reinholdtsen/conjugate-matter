---
title: "Independent anchors"
weight: 30
status: method
description: "An anchor must come from outside the paper — a textbook identity or a published value; a check that reproduces the paper's own number is circular, as v3's Kibble anchor was."
sources:
  - "CLAUDE.md 'Method'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3-adjudication.md 'Rulings'"
  - "verify/soliton_obituary.py"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "verify/toy_s5.py"
  - "verify/battery.py"
  - "review/v3-worklog.md 'New open items (to compute before v3 states anything about them)'"
---

*An anchor is a check that a verification script must pass against something known independently of the paper being checked, such as a textbook identity or a published value, before its own numbers are trusted. A check that only reproduces the paper's own figure is circular: if the paper's formula is wrong, the check repeats the error and passes. Review round 3 found such a case, a wrong normalization of the monopole count in the soliton manuscript that had passed because its anchor reproduced the previous draft's number. The rule has been part of the program's method since, and the soliton-obituary script and two of the toy-model scripts now open with anchor checks taken from textbooks or from the cited literature.*

**Status:** Method, in force (a round-3 lesson, now in root `CLAUDE.md`) — untagged — applied in `verify/soliton_obituary.py`, `verify/toy_coset.py` and `verify/toy_gw.py`, which print their anchor checks first.

## Key facts

- **The rule.** "A verification check confirms arithmetic, not the model. An anchor must be independent of the paper (a textbook identity, a published value). A check that reproduces the paper's own number is circular. Round 3 caught a wrong Kibble normalization that a circular anchor had passed." (root `CLAUDE.md`).
- **The lesson it came from.** Round-3 lesson 2: "An anchor must be independent of the paper. v3's Kibble anchor reproduced v2's own number and so tested nothing. The replacement anchors are the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume." The wrong number was ruling 1's normalization p ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization); [Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).
- **The soliton-obituary anchors.** `verify/soliton_obituary.py`: "Anchors come first and are independent of the manuscript (a textbook identity; a published value)." Its anchor checks print `Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl`; `one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)  [p = 104.31]`; `freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)`; and `Delta N_eff: one extra neutrino species at T_nu gives 1`. The freeze-out anchor passes inside a window and prints no value. See [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script).
- **The toy-model anchors.** `verify/toy_coset.py` opens with `H(Z) is symplectic and I = w^-1 H squares to -1` and `rho is symplectic and is the quarter turn: rho^2 = -1`. `verify/toy_gw.py` takes its inputs "from the sources, not from memory" (the matrix base of de Goursac–Tanasa–Wallet, arXiv:0709.3950, and the duality of Grosse–Wulkenhaar, hep-th/0402093), checks the explicit Laguerre form of the basis functions against the source's defining properties "so it is not taken on trust", and prints `f_00 = 2 exp(-x^2/theta) as in 0709.3950 (A.2)` and `anchor: D f_00 = f_00 (the normalization pi sqrt|det theta|)`. `verify/toy_s5.py` checks textbook identities (Parseval's theorem; the marginals of the Wigner function) before computing its interaction values. See [The toy-model scripts](/wiki/method/verification/toy-model-scripts).
- **What is not an anchor.** Checks marked "quoted:" in the toy scripts, and the "parity" checks of `verify/battery.py`, compare the code's output with the figures the documents print. battery.py's docstring: "a parity failure means this environment no longer reproduces the numbers the papers cite." Such checks show that the documents print what the code computes; they are reproductions, not independent anchors ([The verification battery T1–T7](/wiki/method/verification/battery)).
- **The retired script's self-check.** knot_numbers.py, the script that checked the withdrawn manuscript, tested "its freeze-out formula on a standard relic first: 100 GeV with σv = 2.2×10⁻²⁶ cm³/s gives Ω h² = 0.108" (`review/v3-worklog.md`). The value 0.108 belongs to that retired script, not to the current one. The circular anchor was the Kibble one (lesson 2, above).

## Sources

- Root `CLAUDE.md` 'Method' — the rule
- `review/round3-adjudication.md` 'Lessons (now in CLAUDE.md)' (lesson 2) and 'Rulings' (ruling 1) — the circular anchor and its replacement
- `verify/soliton_obituary.py` — the soliton anchors
- `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s5.py` — the toy-model anchors and identity checks
- `verify/battery.py` — parity checks, which are reproductions
- `review/v3-worklog.md` 'New open items (to compute before v3 states anything about them)' — the retired script's freeze-out self-check
