---
title: "The misalignment potential"
weight: 10
status: alive
description: "X's mass must come from an energy cost for misalignment between the polarization J and Z, measured by {J, I[Z]} = [[S, A], [A, S]] (battery T3), which vanishes only at X = 0 with g pinned — a two-tensor potential."
provenance: [D, V]
sources:
  - "notes/debt1a-iii-tuning-test.md §1"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "verify/battery.py T3"
  - "papers/broken-born-checkpoint-v2.md §4"
---

*The misalignment potential is the energy cost the program assigns to a mismatch between the polarization J that the vacuum has chosen and the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z. Geometry alone gives the momentum graviton X no potential ([shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)), so X's mass has to come from this term, which the calc notes also call the η-selection or Higgs sector. The natural measure of the mismatch is the anticommutator {J, I[Z]}, which is zero exactly where J and Z are compatible; its block form is derived [D — rigorous] and machine-checked [V]. Because the mismatch vanishes only at X = 0 with the metric pinned to a reference metric, the potential necessarily involves two tensors, like the potential of a massive-gravity theory.*

**Status:** Alive — [D][V] in [checkpoint #11](/wiki/history/documents/checkpoint) §7.2; [D — rigorous] in calc note #7 (`notes/debt1a-iii-tuning-test.md` §2) — the block structure is checked by test T3 of [the verification battery](/wiki/method/verification/battery) (`verify/battery.py`), which passes.

## Key facts

- The object, from calc note #7 §1 (see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)): "The X mass must come from the η-selection (Higgs) sector: a misalignment potential penalizing incompatibility between the polarization J and the modular field Z. The natural incompatibility measure is the anticommutator {J, I[Z]} (zero exactly on the compatible locus)."
- The computation, #7 §2 [D — rigorous], "in the vacuum frame (g₀ = 1), Euclidean skeleton", with the Siegel parametrization of I[Z]:

  ```text
  I[Z] = [[ −Y⁻¹X , −Y⁻¹ ], [ Y + XY⁻¹X , XY⁻¹ ]],    J₀ = [[0, 1], [1, 0]]

  {J₀, I[Z]} = [[S, A], [A, S]],    S = Y + XY⁻¹X − Y⁻¹,    A = [X, Y⁻¹]
  ```

- The machine check [V]: battery test T3 compares the four blocks numerically (d = 4, seed 0) and prints `PASS  T3 {J0,I[Z]} = [[S,A],[A,S]]`.
- The consequence, #7 §2: "The compatible locus is X = 0 and Y = Y⁻¹ (i.e. g pinned to the J-frame reference metric): the Higgs sector is inevitably a two-tensor potential V(g, X; reference) — a massive-gravity-type potential".
- #11 §7.2 [D][V]: "The Higgs sector is a misalignment potential in {J, I[Z]} = [[S,A],[A,S]], S = Y + XY⁻¹X − Y⁻¹, A = [X, Y⁻¹] (blocks machine-verified)."
- What the test then asks is whether a potential built from these blocks is ghost-free. Built from metrics it is not ([The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)); built from frames it is ([The frame tier](/wiki/gravity/tuning-test/frame-tier)). The mass it produces is the one described on [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs).
- Notation: J here is the real structure of postulate P2′, where η is the product of H and J (#11 §4); #11 §5 also writes J = η⁻¹H, and the toy-model note calls the real structure K. Which convention to use is unresolved across the documents ([The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter)).

## Sources

- `notes/debt1a-iii-tuning-test.md` §1 — the object to test; §2 for the block computation and the compatible locus [D — rigorous]
- `papers/broken-born-checkpoint-v2.md` §7.2 — the current statement [D][V]; §4 for J in postulate P2′
- `verify/battery.py` T3 — the machine check of the blocks
