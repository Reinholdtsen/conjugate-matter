---
title: "The cosmological constraint a·ã = 1"
weight: 20
status: alive
description: "ω-rigidity fixes the comoving phase-space cell, so our scale factor and the conjugate's are reciprocals: the |Z| = 1 locus of the modular field, and the program's version of scale-factor duality."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md App. A item 6"
  - "notes/broken-born-theory.md §6"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/broken-born-program-v1.md §8"
  - "verify/battery.py T2"
---

*The cosmological constraint is the relation a·ã = 1 between the scale factor a of our universe and the scale factor ã of its momentum-space description: as our universe expands, its momentum-space description contracts by exactly the same factor. It follows from the program's postulate that the symplectic form ω, the structure that fixes the size of a cell of phase space and with it the value of Planck's constant, is rigid. A comoving cell therefore keeps its phase-space volume while position-space distances grow, which forces momentum-space distances to shrink; in signal terms, stretching a waveform compresses its spectrum. The relation is derived [D], and it turned one of the program's founding suppositions, that the conjugate universe shrinks as ours expands, into a theorem.*

**Status:** Alive — [D] (#11 §10) — derived in the lab notebook (#1 §6) and stated from ω-rigidity in #11; the modular parametrization it belongs to, including det H_Z = 1, is machine-checked ([the verification battery](/wiki/method/verification/battery), test T2), but the constraint itself is not.

## Key facts

- **Statement.** #11 §10: "**Constraint [D]:** ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run) — the |Z| = 1 self-dual locus."
- **Derivation.** #1 §6: "Rigidity of ω means the comoving phase-space cell has fixed volume: with x-space scale factor a and p-space scale factor ã, each mode occupies (aã)³ × (comoving cell) = ℏ³. Hence a ã = const ≡ 1. This is not an extra assumption; it is the statement that ℏ does not run." The [lab notebook](/wiki/history/documents/lab-notebook) derives it under the [original P2](/wiki/program/postulates/original-p2), which froze both ω and η. #11 states it from ω-rigidity alone, the rigidity that [P2′](/wiki/program/postulates/p2-prime) keeps: "Only ω is rigid (symplectic rigidity ≡ constancy of ℏ)" (#11 §4).
- **Geometry.** #11 §6: Born reciprocity acts on the modular field as "**ρ: Z → −Z⁻¹** (Möbius; d = 1 check), fixed point Z = i; at X = 0 it is scale-factor duality g → g⁻¹, and the cosmological constraint a·ã = 1 (§10) is the |Z| = 1 locus." Calc note #5 adds: "the minisuperspace duality was the shadow of this modular action" (§C). See [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion) and [the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z).
- **The name [T].** Scale-factor duality is the name string cosmology gives to a symmetry a → 1/a of its equations. In this program the corresponding map is the X = 0 form of modular inversion, g → g⁻¹ (#11 §6).
- **The geometric face of ℏ-rigidity.** Calc note #5 counts "unimodularity of H (det H = 1) as the geometric face of ℏ-rigidity" among the results of Debt 1 (§F). det H_Z = 1 is test T2 of [the battery](/wiki/method/verification/battery), and it passes.
- **A founding supposition promoted.** Founding supposition 6, "Conjugate universe shrinks as ours expands", is "**promoted to theorem** (a·ã = 1 from ℏ-rigidity; the |Z| = 1 locus)" (#11 App. A item 6). See [founding suppositions and their fates](/wiki/program/founding-suppositions) and [the conjugate universe](/wiki/program/conjugate-universe).
- **What it feeds.** The constraint is the input to [the duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary) and to [the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce), whose test is [row 5](/wiki/predictions/fate-of-expansion). The popular article #12 explains cosmological redshift through it, as the momentum spectrum contracting ([Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the current statement and its tag
- `papers/broken-born-checkpoint-v2.md` §6 — the |Z| = 1 locus and scale-factor duality g → g⁻¹
- `papers/broken-born-checkpoint-v2.md` §4 — P2′: "symplectic rigidity ≡ constancy of ℏ"
- `papers/broken-born-checkpoint-v2.md` App. A item 6 — founding supposition 6, "promoted to theorem"
- `notes/broken-born-theory.md` §6 — the derivation from a fixed phase-space cell
- `notes/debt1a-geometric-core.md` §C, §F — "the shadow of this modular action"; det H = 1 as the geometric face of ℏ-rigidity
- `notes/broken-born-program-v1.md` §8 — v1's statement: "Not an assumption — the statement that ℏ does not run"
- `verify/battery.py` T2 — det H_Z = 1 and the Siegel parametrization, executed
