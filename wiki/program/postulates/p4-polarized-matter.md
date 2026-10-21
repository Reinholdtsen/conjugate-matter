---
title: "P4: polarized matter and strict sector separation"
weight: 60
status: alive
description: "The Standard Model is x-polarized and conjugate matter χ is p-polarized; both couple universally to H and no gauge force crosses polarizations, taken strictly since v2.1 (gravity-induced mixing ε ≲ 10⁻¹³)."
provenance: [P]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §13 row 7"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/v3-worklog.md 'Round-2 pending list' R4"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-program-v1.md §2"
  - "papers/reciprocity-toy-models.md §5"
  - "review/round4-adjudication.md 'Rulings' F3"
  - "verify/toy_s5.py part C"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
---

*P4 is the program's axiom about matter: ordinary matter, the Standard Model, is x-polarized, with its fields organized around position, the variable in which its interactions are local, while a second kind, conjugate matter χ, is p-polarized, organized around momentum. Both kinds respond to the same gravity, so the equivalence principle holds across them, but no gauge force (the electromagnetic, weak or strong interaction) acts between the two kinds. Since checkpoint v2.1 the program reads this strictly: the only mixing allowed between the sectors is what gravity itself induces, which is zero or extremely small.*

**Status:** Alive — [P]; the gravity-only bound it quotes is from the literature [27S] — the strict reading is in force by decision (round-3 Decision 1, 2026-10-19), not by derivation.

## Key facts

- Statement (#11 §4):

  ```text
  P4  Matter comes in x-polarized (Standard Model) and p-polarized (χ)
      representations; both couple universally to H; gauge forces do not
      cross polarizations. [P; taken strictly since v2.1: no kinetic mixing
      between the sectors beyond what gravity induces, which vanishes if
      hidden charge conjugation is exact and otherwise first appears at
      six loops, ε ≲ 10⁻¹³ [27S].]
  ```

- The lab notebook's version (#1 §1) adds: "Both couple universally to H — the equivalence principle holds across polarizations. Gauge interactions do not connect the two representations." See [conjugate matter and the velocity gate](/wiki/dark-matter/conjugate-matter).
- Round-3 Decision 1 (`review/round3-adjudication.md`): "**Kinetic mixing: strict sector separation.** ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry." "It is the program's own postulate P4 ('gauge forces do not cross polarizations') taken at face value." It "costs nothing and closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector." See [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) and [round-3 decisions](/wiki/method/review/round-3/decisions).
- The reading of the bound is unresolved. The round-3 referee notes that Gherghetta et al. present the figure as a floor ("could be as large as ~1e-13"), consistent with "≲" only in the sense "up to" (audit notes, Step 1); #11's wording ε ≲ 10⁻¹³ stands. The zero case is also worded two ways: hidden charge conjugation "exact" (#11) or "a gauged symmetry" (Decision 1). The v3 worklog bears on the difference: "Quantum gravity forbids an exact global C", while "a gauged C … remains a loophole" (`review/v3-worklog.md` 'Round-2 pending list', item R4).
- The test that rests on it: [row 7](/wiki/predictions/direct-detection-null) of #11 §13 requires a "**Permanent null** (both dark-sector candidates SM-decoupled; P4 strict)", where SM-decoupled means decoupled from the Standard Model, and is killed by "Any confirmed non-gravitational DM–SM coupling" (DM: dark matter).
- In the toy models P4 is also what makes the breaking physical. Round-4 ruling F3: "Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K." A coupling built from (H, K) is local in x in one vacuum and local in p in the other (checked in `verify/toy_s5.py`, one of [the toy-model scripts](/wiki/method/verification/toy-model-scripts)), but "Nothing here forces that coupling" (toy note §5). See [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) and [the twisted element](/wiki/symmetry-breaking/twisted-element).
- The worklog calls P4 the lock that ties matter's choice of section to the sign of K: without it, "matter's choice of section and K's sign are independent orders", and "The lock is P4" (the worklog's wording for the coupling predates v2 of the toy note, which calls it (H, K)-built). #11 §14 item 11 lists "locality of matter beyond the weak (Yukawa-like) form, which in the toy reduces to P4" as still open [O]. See [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — the statement and its strict reading; §13 row 7; §14 item 11
- `review/round3-adjudication.md` 'Decisions' 1 — why strict separation was adopted
- `review/round3/referee/audit-notes.md` Step 1 — the referee's reading of the gravity-only bound
- `review/v3-worklog.md` 'Round-2 pending list', item R4 — exact versus gauged hidden charge conjugation
- `notes/broken-born-theory.md` §1 — the v0.1 statement, with the equivalence principle across polarizations
- `notes/broken-born-program-v1.md` §2 — the v1 statement, before the strict reading
- `papers/reciprocity-toy-models.md` §5 and `review/round4-adjudication.md` 'Rulings' F3 — P4-type coupling as what makes the breaking physical; `verify/toy_s5.py` part C — the gated check
- `notes/toy-lagrangian.md` 'Chunk 4 (in progress, 2026-10-19): S5' — the P4 lock
