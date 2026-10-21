---
title: "The vacuum-energy identity V(1) = 2T"
weight: 20
status: alive
description: "At the aligned point the integer identity [2,8,6] = 2·[1,4,3] gives V(1) = 2T, so a flat aligned vacuum forces T = 0 and V(1) = 0 (battery T5); it does not address matter-loop vacuum energy."
provenance: [D, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "verify/battery.py T5"
  - "verify/battery.py T6"
  - "HANDOFF.md §2"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
---

*The vacuum-energy identity is a four-line algebraic result about the program's [palindromic](/wiki/gravity/palindromic-branch/palindrome) bimetric potential: at the aligned point, where the two frames coincide, the potential's value V(1) is exactly twice its tadpole T, the coefficient of the term linear in a small departure from that point. A flat aligned vacuum requires V(1) = T, and the two conditions together force T = 0 and V(1) = 0, so the spin-2 interaction sector contributes no vacuum energy there. The integer arithmetic behind the identity is machine-checked. The identity does not address the vacuum energy of matter loops, and whether it is new is the subject of an open literature comparison.*

**Status:** Alive — [D][V] (#11 §7.3) — battery test T5 checks the integer identity and T6 the coefficients it uses, and both pass ([the verification battery](/wiki/method/verification/battery)). The novelty claim was downgraded in #11 §7.4 and waits on [the partially massless comparison](/wiki/gravity/palindromic-branch/pm-comparison); the scope is limited to the wedge sector (#11 §7.3).

## Key facts

- The tadpole, which the [checkpoint](/wiki/history/documents/checkpoint) uses without defining ([#8](/wiki/history/documents/debt-1-notes) §2): "At the aligned point 𝕏 = 1: eₙ(1) = C(4,n), and linearizing eₙ(1+δ) = C(4,n) + C(3,n−1)Tr δ gives the tadpole combination T = β₁ + 3β₂ + 3β₃ + β₄." See [elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials).
- Under [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome) (#8 §2, [D — rigorous, four lines]):

  ```text
  V(1) ∝ 2β₀ + 8β₁ + 6β₂,     T = β₀ + 4β₁ + 3β₂     ⟹     V(1) = 2T
  ```

- A flat aligned vacuum requires V(1) = T; with V(1) = 2T this gives "T = 0 and V(1) = 0 exactly" (#8 §2). In the checkpoint's words, "the wedge sector contributes zero cosmological constant, by symmetry" (#11 §7.3). The condition selects β₀ = −4β₁ − 3β₂ (#11 §7.4).
- Battery T5 [V] prints "V(1) - 2T = [0,0,0]" with V1 = [2, 8, 6] and T = [1, 4, 3], the coefficient vectors that #11 §7.3 writes as the integer identity [2,8,6] = 2·[1,4,3]. Battery T6 [V] confirms the coefficients C(3, n−1) = [0, 1, 3, 3, 1] (`verify/battery.py`).
- Scope (#11 §7.3): "this cancels the spin-2 interaction potential's vacuum contribution at the aligned point — it does **not** by itself address matter-loop vacuum energy, the 'old' cosmological-constant problem"; see [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem). With the spin-2 sector contributing nothing, "dark energy is left entirely to the τ sector" (#8 §2; [τ quintessence](/wiki/cosmology/dark-energy/tau-quintessence)).
- Names and novelty. The result was called the "vacuum-energy theorem" (#8 §2), the "four-line theorem" ([#1](/wiki/history/documents/lab-notebook) v0.6), the "palindrome theorem" and "Λ theorem" (#9 §5, §11; [HANDOFF](/wiki/history/documents/handoff) §2); #11 calls it an identity. #8 said that if the literature had not noticed it, "it is a standalone publishable observation", and #9 counted it among "two results that stand on their own". #11 §7.4 downgraded this to "requires detailed comparison with the PM and exchange-symmetric literature", PM being partially massless, and #11 §15 lists "one identity awaiting a novelty verdict" ([assessment](/wiki/program/assessment)).
- The partially massless point sits at Λ ≠ 0 and is "a *different* point of the same branch" from the one this identity selects (#11 §7.4); see [partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity).

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.3, §7.4, §15 — the identity as currently stated, its scope, the novelty downgrade and the self-assessment.
- `verify/battery.py` T5, T6 — the printed integer identity and coefficients.
- `HANDOFF.md` §2 — the "Λ theorem" and its novelty downgrade in the one-screen state.
- `notes/debt1a-iv-beta-coefficients.md` §2 — the four-line derivation and the definition of T.
- `notes/broken-born-theory.md` 'Addendum (v0.6)' — the result as first recorded (superseded as reference).
- `notes/broken-born-program-v1.md` §5, §11 — v1's "Λ theorem" and its "standalone" claim (superseded by #11).
