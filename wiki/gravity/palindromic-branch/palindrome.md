---
title: "The palindrome βₙ = β₄₋ₙ"
weight: 10
status: alive
description: "On the broken vacuum reciprocity acts as the frame exchange 𝕏 → 𝕏⁻¹, forcing β₀ = β₄ and β₁ = β₃: the interchange-symmetric branch of bimetric gravity, its ℤ₂ read as Born reciprocity."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "HANDOFF.md §2"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
---

*The palindrome is the constraint βₙ = β₄₋ₙ on the five coefficients of the program's bimetric wedge potential: β₀ = β₄ and β₁ = β₃, with β₂ free. It follows because [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) acts on the broken vacuum as an exchange of the two frames, which reverses the order of the potential's terms, so a potential invariant under reciprocity must read the same in both directions. It places the program's gravity sector in the interchange-symmetric branch of bimetric gravity, whose ℤ₂ exchange symmetry the program reads as Born reciprocity. The derivation stands as a program result; it is not machine-checked, and the branch itself is not new to the literature.*

**Status:** Alive — [D] — derived in [#8](/wiki/history/documents/debt-1-notes) §1. The [checkpoint](/wiki/history/documents/checkpoint) tags its §7.3 [D][V], but the [V] there belongs to the integer identity on the next page (battery T5); the palindrome derivation itself has no machine check. The earlier claim that the branch had no prior motivation was downgraded in #11 §7.4.

## Key facts

- The potential acted on (#8 §1), for the program's frames (e, f = E₀[J]): V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏), 𝕏 = √(g⁻¹f), with the exchange identity Sₙ(g, f) = S₄₋ₙ(f, g); see [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) and [the frame tier](/wiki/gravity/tuning-test/frame-tier).
- The action of reciprocity (#8 §1): "Born reciprocity acts on the broken vacuum as the frame exchange (𝕏 → 𝕏⁻¹ in the aligned frame; the duality between the 'e-dynamical' and 'f-dynamical' presentations of the same physics)." On the modular field itself reciprocity acts as Z → −Z⁻¹ (#11 §6; [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)).
- The constraint [D] (#8 §1; #11 §7.3):

  ```text
  βₙ = β₄₋ₙ      (β₀ = β₄,  β₁ = β₃,  β₂ free)
  ```

- #8 §1 called this "exactly the 'interchange-symmetric branch' that has floated in the bimetric literature as an ad hoc simplification", which "now has a reason to exist: **its ℤ₂ is Born reciprocity.**" #11 §7.4 corrects the history: the interchange-symmetric choice appears in the partially massless literature, and at α = 1 the [partially massless point](/wiki/gravity/spin-2-fields/partially-massless-gravity) lies inside this branch. Whether reciprocity is the origin of the partially massless symmetry is open [O], as part of [open problem 2](/wiki/gravity/palindromic-branch/pm-comparison).
- Consequences: the palindrome removes two of the five βₙ (#8 §3; [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)), and at the aligned point it yields [the vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity).
- In the checkpoint's summary, the program's gravity sector is "the interchange-symmetric branch of Hassan–Rosen bimetric gravity" with the second frame confined to [Λ(4)](/wiki/phase-space/modular-field/lagrangian-grassmannian) (#11 §1); see [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric).

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.3, §7.4 — the constraint as currently stated; the literature position and the open question.
- `HANDOFF.md` §2 — the palindromic βₙ = β₄₋ₙ branch in the one-screen state.
- `notes/debt1a-iv-beta-coefficients.md` §1, §3 — the derivation and the parameter count.
- `notes/broken-born-theory.md` 'Addendum (v0.6)' — the result as first recorded, with the "previously ad hoc branch" wording that #11 §7.4 downgraded.
- `notes/broken-born-program-v1.md` §5 — v1's version, which called it the branch's "raison d'être" (superseded by #11).
