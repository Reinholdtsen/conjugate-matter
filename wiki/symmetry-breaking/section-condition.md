---
title: "The section condition: what η fixes"
weight: 90
status: alive
description: "η's null lines are K's eigenlines; a section condition built from η confines matter to one of them but cannot tell which (a clean pair only for d = 1); the lab notebook's original section condition and its curved-background question."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §1"
  - "review/round4-adjudication.md 'Rulings' (DFT 'pair')"
  - "review/round4/referee/audit-notes.md Step 3"
  - "notes/toy-lagrangian.md 'Chunk 4: S5'"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §11 item 1"
  - "verify/toy_s5.py parts A–B"
---

*A section condition is a rule, taken from double field theory, that makes every field depend on only half of a doubled set of coordinates, so that physics lives on one "section" of the doubled space. In the program's toy model the neutral metric η, the order parameter of broken reciprocity, singles out exactly two lines in the position–momentum plane, its null lines, and a section condition built from η forces each matter field to depend on one of those lines only. The condition cannot say which of the two lines is position: the same fields pass whether it is built from η or from −η. So η fixes the pair of candidate directions, and the choice within the pair has to come from somewhere else.*

**Status:** Alive, for d = 1 — [V] (the worklog's parts A and B; `verify/toy_s5.py`) — the section condition itself is literature [T] and is imposed, not derived, in the toy; the lab notebook's question about curved backgrounds stays open [O] and is not tracked in #11 §14.

## Key facts

- **What η fixes [V].** "The null lines of η = ωK(φ) are exactly K's eigenlines L±, and the only ones. K → −K sends η → −η with the same null lines. ρ exchanges L+ and L−." (toy-model note §5; worklog part A [V]; `verify/toy_s5.py` part A). The lines are Lagrangian (§1; [Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations); [the order parameter](/wiki/symmetry-breaking/order-parameter)).
- **The condition [V].** For d = 1 the toy imposes

  ```text
  η^{AB} ∂_A f ∂_B g = 0,    η^{AB} ∂_A ∂_B f = 0
  ```

  "In null coordinates it is purely off-diagonal: fields on one null line pass; mixed fields fail; built from −η, the pairing only changes sign. So consistency confines matter to one null line without telling the two apart." (§5; worklog part B [V]; `verify/toy_s5.py` part B; [The toy-model scripts](/wiki/method/verification/toy-model-scripts)).
- **The pair, not the member.** "Mixing the two lines fails: η(dF(u), dG(v)) = −F′G′." "The section condition selects the unordered pair {L+, L−} and cannot tell position from momentum." (worklog, chunk 4, part B).
- **Only for d = 1.** "For d > 1 the analogous statement leaves a continuous family of sections [12]." (§5). The round-4 ruling on the "pair", upheld: "'Every derivation selects the pair' holds only for d = 1" — "For d > 1, Betz–Blumenhagen–Lüst–Rennecke's M ∈ O(d) gives a continuous family of sections." ([Review round 4](/wiki/method/review/round-4)).
- **Imposed, not derived.** In [double field theory](/wiki/phase-space/born-geometry/double-field-theory) the section condition "is imposed for closure of the gauge algebra [11], or derived from string consistency [12]" [T] (§1). The worklog's literature check found the dynamical choice of section "Claimed only in words", and lists as open "a mechanism that picks L over L̃". In the toy the condition is imposed: the round-4 referee notes that "the section condition is imposed, not derived, in this paper" (audit notes, Step 3).
- **The lab notebook's version (open [O]).** v0.1: "Field dependence is restricted to a Lagrangian leaf by a section condition, as in double field theory; consistency of the section condition on general backgrounds is open there and open here. [O]" (#1 §2). Its open problems keep "the section condition on curved backgrounds" open (#1 §11 item 1). The item does not appear among #11 §14's open problems: it was dropped, not resolved ([Open problems and the queue](/wiki/status/open-problems); [The lab notebook](/wiki/history/documents/lab-notebook)).
- **What follows.** Choosing the member of the pair takes a coupling that can tell K from −K ([Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling); [the twisted element](/wiki/symmetry-breaking/twisted-element)), and nothing yet forces matter to use one ([Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality)).

## Sources

- `papers/reciprocity-toy-models.md` §5 — what η fixes; the section condition; the d > 1 family
- `papers/reciprocity-toy-models.md` §1 — η = ωK and its Lagrangian null lines; the double-field-theory prior work
- `review/round4-adjudication.md` 'Rulings' — the "pair" holds only for d = 1
- `review/round4/referee/audit-notes.md` Step 3 — imposed, not derived
- `notes/toy-lagrangian.md` 'Chunk 4: S5' — parts A and B [V]; the section-selection literature
- `verify/toy_s5.py` — parts A and B
- `notes/broken-born-theory.md` §2, §11 item 1 — the v0.1 section condition and its curved-background question [O]
