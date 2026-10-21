---
title: "The compatibility theorem"
weight: 40
status: established
description: "Positive H compatible with both rigid ω and η are exactly diag(g, g⁻¹): Freidel–Leigh–Minic's statement, the program's block proof, battery test T1, and round 3's independent Gröbner re-derivation."
provenance: [T, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §5"
  - "notes/debt1a-geometric-core.md §A"
  - "verify/battery.py T1"
  - "review/round3/referee/audit-notes.md Step 3"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "CLAUDE.md 'Since the handoff'"
  - "HANDOFF.md §6"
---

*The compatibility theorem is a statement of linear algebra about metrics on phase space: if both the symplectic form ω and the neutral metric η are held fixed in their standard forms, the only positive metrics H compatible with both are block-diagonal, H = diag(g, g⁻¹), with the momentum block equal to the inverse of the position block. The statement is Freidel, Leigh and Minic's; the short block proof and its machine check are the program's, and an independent reviewer re-derived it in round 3. Its role in the program is negative: it showed that freezing both structures leaves the program with no content of its own — general relativity plus one bespoke dark-matter model — which forced the postulate change from P2 to P2′.*

**Status:** Established — literature [T] (Freidel–Leigh–Minic, #11 ref. [26S]), with the program's block proof machine-checked [V] (battery test T1; [the battery](/wiki/method/verification/battery)) — re-derived independently in round 3; the re-attribution from "derived here" was made in #11 v2.1.

## Key facts

- **Statement [T][V].** #11 §5: "Positive H satisfying both (η⁻¹H)² = 1 and (ω⁻¹H)² = −1 are exactly H = diag(g, g⁻¹), g ∈ Sym⁺(d)." In the language of [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures), the two conditions say J² = 1 and I² = −1.
- **Proof.** #11 §5, with the blocks of #5 §A:

  ```text
  H = [[A, C], [Cᵀ, B]]
  (2,1) blocks:     AC^T + CA = 0  and  CA − AC^T = 0,  hence  AC^T = 0
  positivity:       C = 0
  diagonal blocks:  B = A⁻¹
  ```

- **Attribution.** #11 §5 (v2.1): "It is the Born-geometry compatibility statement of Freidel, Leigh and Minic: writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]. The block proof and the machine check are this program's." Earlier documents (#5 "[D — rigorous]", #9 "[D]", #13 "[D — compatibility theorem]", #14) treat it as derived here; #11 and the root `CLAUDE.md` govern ([conflicts between sources](/wiki/history/documents/source-conflicts)).
- **Battery test T1.** At d = 4 the gate prints `PASS  T1a diag(g,g^-1) satisfies (eta^-1 H)^2=1 and (omega^-1 H)^2=-1`, `PASS  T1b generic H violates at least one condition`, and the two proof-block identities `(J^2)_21 = A C^T + C A` and `(I^2)_21 = C A - A C^T`.
- **Round 3's re-derivation.** The referee checked the block identities symbolically (sympy, d = 1, 2); at d = 2, where `sympy.solve returned 0 branches (solver failure, not a counterexample)`, a Gröbner basis proved C = 0 and B = A⁻¹; and the referee ran numerical families at d = 3, 4 (2000 trials per family); "perturbing diag by C of size 1e-4 gives residuals ~1e-3: the solution set is isolated as claimed." Verdict: `theorem TRUE; stated proof VALID (uses positivity where it is not needed; slightly weaker hypothesis suffices)`, and "it does not by itself establish any physics" (audit notes, Step 3). See [the round-3 rulings](/wiki/method/review/round-3/rulings).
- **The positivity step.** #11's proof uses positivity to get C = 0; round 3 found `Positivity is NOT needed for C=0 (only for g>0)`. #11 §5 records the refinement, so the proof stands and the step is redundant, not wrong.
- **Scope and history.** Proven for positive-definite (Euclidean) H only; the Lorentzian extension is [open](/wiki/phase-space/born-geometry/lorentzian-dressing). Round 1's referee "insinuated the compatibility theorem might be false (it is machine-verified)" (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)). Its consequences are [the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries) and, through them, [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem).

## Used by

- [Original P2: both structures rigid (superseded)](/wiki/program/postulates/original-p2) — the postulate the theorem showed to be too rigid.
- [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — content beyond general relativity requires η to be emergent.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — the repair the theorem forced.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — the theorem's solutions are the vacuum slice X = 0.
- [Two causal cones](/wiki/conjugate-relativity/two-causal-cones) — #13 builds its two light cones on H = diag(g, g⁻¹).

## Sources

- `CLAUDE.md` "Since the handoff" — the re-tag to [T] with the Freidel–Leigh–Minic credit.
- `papers/broken-born-checkpoint-v2.md` §5 — statement, proof, attribution and the positivity note.
- `review/round3-adjudication.md` "Rulings", "What survives v3" — verified, identified as Freidel–Leigh–Minic's result, kept "as [T], pending the FLM comparison".
- `review/round3/referee/audit-notes.md` Step 3 — the independent symbolic, Gröbner and numerical re-derivation.
- `notes/debt1a-geometric-core.md` §A — the original proof, tagged "[D — rigorous]" before the re-attribution.
- `verify/battery.py` T1 — both directions and the two proof-block identities.
- `HANDOFF.md` §6 — round 1's doubt, arbitrated by the machine check.
