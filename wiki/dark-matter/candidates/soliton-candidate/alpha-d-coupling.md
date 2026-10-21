---
title: "Obituary: the coupling α_d ≈ 34"
weight: 40
status: dead
description: "Three attempts to fix the hidden coupling — Dirac quantization against our photon (round 1's valid kill), reciprocity acting as modular S (numerology), and hypothesis H — and the factor-of-four convention spread."
sources:
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "review/skeptic-review-console.html"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "papers/broken-born-checkpoint-v2.md §12"
---

*α_d ≈ 34 was the strength the soliton candidate assigned to the coupling between its hidden monopoles — 1/(4α), the reciprocal of four times the fine-structure constant — and the program tried three ways to fix that value. The first applied Dirac's charge-quantization condition using our photon's charge, which contradicted the claim that the monopoles do not couple to our photon. The second had Born reciprocity act on couplings as the modular S transformation of electric–magnetic duality; a referee called it numerology. The third assumed that the smallest hidden charge equals the electron's; it was motivated but not derived, and it fell with the candidate. What survives is a general fact: a weakly coupled force always has strongly coupled monopoles.*

**Status:** Dead in all three forms. The first was killed in round 1 (the handoff calls it the "round-1 reviewer's valid kill"); the second was set aside when Paul decided on 2026-10-19 that "S-duality is no longer what fixes α_d" (v3 worklog, F2); the third, hypothesis H, was part of #14 v3, which was withdrawn on 2026-10-19 (round-3 Decision 2). The convention spread is marked [V] in the v3 worklog; the current gate, `verify/soliton_obituary.py`, does not re-check it. Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); listed in [the graveyard](/wiki/status/graveyard).

## Key facts

- **Attempt 1: Dirac quantization against our photon** (dead). The handoff's list of dead claims: "α_d ≈ 34 via Dirac quantization against our photon (round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon)" (`HANDOFF.md` §2). The DSZ (Dirac–Schwinger–Zwanziger) lattice is the lattice of our electric and magnetic charges ([Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization)).
- **Attempt 2: reciprocity as modular S** (set aside). "Restated in v2 as reciprocity-acts-as-modular-S on the coupling — explicitly the load-bearing conjecture; without it α_d is a free strong coupling" (`HANDOFF.md` §2). v2 fixed the coupling "by the reciprocity map, acting as the modular S transformation, to the image of ours - alpha_d = 1/(4 alpha) ~ 34" (`review/skeptic-review-console.html`, which embeds v2). Round 2's weakest link was "the α_d derivation ("matrix coincidence ≠ physical identity" / "numerology")" (`HANDOFF.md` §6; [S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality), [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). No ruling addresses it and #11 v2.2 does not mention it; Paul's F2 decision is the operative record.
- **F2: which coupling sets the mass** [D, numbers V] (v3 worklog): "v2 writes M ~ (4π/e_d²) Λ_c ~ 100 Λ_c. That factor is ~137 only if e_d²/4π ≈ 1/137. With e_d²/4π = α_d = 34 it is 0.029, so the solitons would not be heavy." The consistent reading: the hidden sector's elementary coupling is weak, its solitons are heavy, and the solitons themselves are strongly coupled.
- **Attempt 3: hypothesis H** (dead with the candidate; #14 §6 "Conjectural"). #14 §2: "The proposal's single coupling hypothesis (H): the smallest hidden charge equals ours, (g_d/2)^2/4pi = alpha. ... Under H, alpha_W' = 4 alpha ~ 1/34 and alpha_m = 1/(4 alpha) ~ 34." The round-3 referee confirmed the arithmetic (α_W′ = "1/34.259", α_m = "34.259"; audit notes, Step 2) and noted that matching ψ's charge to e/3, the smallest Standard Model charge, instead "gives alpha_m = 308 ... and the framework gives no way to choose" (Step 4(d)).
- **The convention spread** [V] (v3 worklog, R2): "1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn). One-loop [Standard Model] running of α_em gives 1/(4α_em) = 29.0 at 10¹¹, 28.8 at 3×10¹¹ and 27.3 at 10¹⁶ GeV. The referee's "toward ~6–8" is **not reproduced** for the electromagnetic coupling; 6–8 appears only for 1/(4α₃). The valid core stands: the number is convention-dependent by a factor of 4."
- **What survives.** "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]" (#11 §12); in #14's words, "the strong magnetic coupling is generic, not a hypothesis." For ordinary electromagnetism, #11 §11.2's [T] statement that "Dirac's condition e·g ~ 2π pins the magnetic coupling near 4π/e² ≈ 34" is untouched ([the magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family)).
- **A popular-article echo.** #12 sets the magnetic coupling at "about 34, against our 1/137". That comparison depends on the factor-of-four convention, and the identification it serves is dead ([Obituary: the magnetic identification](/wiki/electric-magnetic-duality/magnetic-identification)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — what survives; §11 — the ordinary-electromagnetism statement
- `HANDOFF.md` §2 — the first two attempts and their status; §6 — round 2's verdict on the second
- `review/round3/referee/audit-notes.md` Step 2, Step 4(d) — the confirmed arithmetic and the e/3 variant
- `review/v3-worklog.md` 'Findings neither referee raised' (F2), 'Round-2 pending list' (R2), 'v3 as drafted (2026-10-19)' — the decision, the mass argument and the convention spread
- `notes/knot-dark-matter-standalone.md` §2 — hypothesis H and the Dirac relation; §6 — H as "Conjectural"
- `review/skeptic-review-console.html` — #14 v2's wording of the modular-S coupling
