---
title: "The duality dictionary w_eff = −w̃"
weight: 30
status: alive
description: "With one shared lapse, a dual-frame fluid of equation of state w̃ contributes w_eff = −w̃: dual stiff ↦ Λ, dual Λ ↦ stiff, dual curvature ↦ negative dark radiation, dust ↦ dust."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 10"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md App. A item 8"
  - "notes/broken-born-theory.md §0"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-program-v1.md §8"
---

*The duality dictionary is the rule that translates energy in the conjugate, momentum-space description of the universe into the form in which it acts on our own expansion. Each kind of energy is labelled by its equation of state w, the ratio of its pressure to its energy density, and the rule is that conjugate-side energy with equation of state w̃ acts on us like energy with w = −w̃. Pure kinetic energy on the conjugate side therefore acts here like a cosmological constant, a conjugate cosmological constant acts like the stiffest possible fluid, and dust acts like dust. The rule is derived [D] from the cosmological constraint a·ã = 1, and it replaced an earlier heuristic that gave a different answer, a correction that #11 counts as one of the two that sharpened the program's hard core.*

**Status:** Alive — [D — corrected en route] (#11 §10) — derived in the lab notebook (#1 §6); no `verify/` script checks it.

## Key facts

- **Statement.** #11 §10: "**Dictionary [D — corrected en route]:** with one shared lapse, a dual-frame fluid contributes w_eff = −w̃ (superseding an earlier −2 − w̃; the constraint's Jacobian changed the answer — rigor's job)."
- **Derivation.** The [lab notebook](/wiki/history/documents/lab-notebook) (#1 §6) uses [the constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) and the Hamiltonian constraint of [minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology). A fluid comoving in the dual frame, with equation of state w̃, gives:

```text
ρ̃ ∝ ã^{−3(1+w̃)},     E = ρ̃ ã³ ∝ ã^{−3w̃} = a^{3w̃}
ρ_eff = E/a³ ∝ a^{−3(1−w̃)}     ⇒     w_eff = −w̃
```

- **The table.** #11 §10 summarizes the rule as "Dual stiff ↦ Λ; dual Λ ↦ stiff; dual curvature ↦ negative dark radiation; dust ↦ dust". The lab notebook's table (#1 §6), with its right-hand column renamed:

| Dual-frame content | Acts on our expansion as |
| --- | --- |
| Kinetic/stiff energy (w̃ = +1) | Cosmological constant (w = −1) |
| Cosmological constant (w̃ = −1) | Stiff fluid (w = +1, dies as a⁻⁶) |
| Spatial curvature (w̃ = −1/3) | Dark radiation (w = +1/3; closed dual space ⇒ negative ΔN_eff) |
| Dust (w̃ = 0) | Dust (w = 0) |

- **The dual gravity term.** "the dual Einstein term is an a⁻⁶ step in G_eff" (#11 §10). In #1 §6 it is the M̃²a⁻⁶ term of 3H²(M_P² + M̃²a⁻⁶) = ρ, an equation found only in the lab notebook and not machine-checked. Its test, together with the negative ΔN_eff of closed dual curvature, is [row 10](/wiki/predictions/early-universe-step), which #11 marks "Optional" and "Knob-bounded".
- **The correction.** The superseded heuristic w_eff = −2 − w̃ "identified densities across frames without the constraint's volume Jacobian" (#1 §6). With the corrected rule, "dust maps to dust — the w=−2 pathology is gone because it was an artifact" (#1 §6). The founding idea built on the heuristic is dead: [Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion). The documents name the cause differently — #1 the "volume Jacobian", #9 §8 the Lagrange multiplier, #11 "the constraint's Jacobian" — and #11's wording is the current one.
- **Its place in the program.** #11 §15: the hard core is "twice sharpened by forced corrections (P2′; the w-dictionary)"; see [the hard core](/wiki/program/hard-core). Founding supposition 8, "Synchronized, not causal; Fourier/holography", is "**alive** (the dictionary)" (#11 App. A item 8); see [the conjugate universe](/wiki/program/conjugate-universe).
- **An open link.** #1 §6 draws one more conclusion from the table: "the natural source of a near-constant dark energy is **kinetic energy in the dual frame**". The program implements dark energy as the potential energy of τ instead, and no document derives one from the other: [Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link).

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the current statement, its tag and the summary of the table
- `papers/broken-born-checkpoint-v2.md` §13 row 10 — the test of the dual gravity term
- `papers/broken-born-checkpoint-v2.md` §15, App. A item 8 — the forced correction; founding supposition 8
- `notes/broken-born-theory.md` §6 — the derivation, the table, the superseded heuristic and the kinetic-energy remark
- `notes/broken-born-theory.md` §0 — the correction announced at the head of the notebook
- `notes/broken-born-program-v1.md` §8 — v1's statement of the dictionary
