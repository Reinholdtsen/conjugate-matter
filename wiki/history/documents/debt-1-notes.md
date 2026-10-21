---
title: "The Debt-1 calc notes (#5–#8)"
weight: 50
status: record
description: "debt1a (the geometric core), -ii (the classification of X), -iii (the tuning test) and -iv (the β coefficients): the structural settlement of Debt 1."
sources:
  - "notes/debt1a-geometric-core.md"
  - "notes/debt1a-ii-X-classification.md"
  - "notes/debt1a-iii-tuning-test.md"
  - "notes/debt1a-iv-beta-coefficients.md"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "HANDOFF.md §3"
  - "verify/battery.py"
---

*The Debt-1 calc notes are four working notes, artifacts #5 to #8, on the most severe of the lab notebook's open problems: what equations govern the geometry of momentum space. The first, written overnight, showed that the original axioms left the program with no content beyond general relativity and one model of self-interacting dark matter, repaired them, and gathered the geometry into a single modular field; it also found the mechanism of the velocity gate. The second showed that the field carrying momentum-space geometry must be a second graviton, and a massive one. The third tested whether that field can avoid the Boulware–Deser ghost, the instability that generic massive-graviton theories carry, and found that it can in the formulation the geometry favors. The fourth used Born reciprocity to fix the remaining coefficients and cancel the sector's vacuum energy. Together they closed Debt 1 in structure; their results are now stated in the checkpoint #11 §5–§7.*

**Status:** Record, final for its scope — the notes tag their own results ("[D — rigorous]", "[D — structural]", "[D + T]"); the seven-test battery T1–T7 in `verify/battery.py` checks the algebra #11 §2 calls Tier 1 [V] — superseded as reference by #11; `HANDOFF.md` §3 marks all four "final", and #8 "final — closes Debt 1 (structural)".

## Key facts

- **#5, debt1a: "Debt 1, Chunk A — the geometric core, linearized groundwork", subtitled "(plus an unplanned payment on Debt 2)".** "Overnight working note. Status: two rigorous results, one axiom correction forced, one mechanism identified, one decisive computation defined but not completed." Its sections give [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) (§A, "[D — rigorous]"), the inconsistency of the original P2 and its forced repair to [P2′](/wiki/program/postulates/p2-prime) (§B; [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)), [the modular field Z](/wiki/phase-space/modular-field/modular-field-z) (§C), and the gate's mechanism, X exchange (§E; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)).
- **#6, debt1a-ii: "The classification of X".** "X is forced to be a massive spin-2 field, with exactly one known consistent structure available, and the massless option excluded by theorem. One tuning question remains, now precisely posed." See [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry), [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms), [the symplectic partner of the graviton](/wiki/gravity/momentum-graviton/symplectic-partner) and [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain). It logged the X-condensate as "A new door, deliberately left closed today"; since #11 v2.0 it is [a dark-matter candidate](/wiki/dark-matter/candidates/x-condensate).
- **#7, debt1a-iii: "The tuning test".** "Status: computed. Outcome: conditional pass — the condition identified, both branches computed or classified, and the failure mode exhibited explicitly." The theory "fails in second-order (metric) variables and passes in first-order (frame) variables", and the picture that emerges is Hassan–Rosen bimetric gravity "with the second frame constrained to a compact moduli space Λ(d)" ([the tuning test](/wiki/gravity/tuning-test); [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)).
- **#8, debt1a-iv: "The β coefficients — closing the debt".** "Reciprocity fixes the potential's structure, cancels its vacuum energy by theorem, and cuts the free parameters from five to two. Debt 1 is structurally paid." See [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome), [the vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity) and [Born's answer](/wiki/gravity/momentum-graviton/borns-answer). Its residue, "none of it existential", became #11 §14 items 1, 3, 6, 5 and 2 ([the three debts](/wiki/history/debts)).
- **What the machine checks cover.** #11 §2's Tier 1, "explicit algebra", is the battery: the compatibility theorem in both directions with its proof's block identities, the Siegel parametrization, the anticommutator block structure, the linearized potential against the Fierz–Pauli form, the palindrome identity as exact integers, the binomial linearization coefficients, and p₄'s exclusion from the span of the elementary symmetric polynomials. All seven passed [V] ([the verification battery](/wiki/method/verification/battery)). Steps the notes state in words, such as the derivation of the palindrome from reciprocity and the count of five parameters reduced to two, are [D].
- **Re-tags and downgrades since.** The compatibility theorem, "[D — rigorous]" in #5, is [T][V] since #11 v2.1: the statement is Freidel, Leigh and Minic's, and the block proof and the machine check are the program's ([broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)). #8 called the interchange-symmetric branch "an ad hoc simplification" in the literature that "now has a reason to exist"; #11 §7.4 found that the partially-massless point lies inside that branch and downgraded the novelty claim to "requires detailed comparison with the PM and exchange-symmetric literature" (PM: partially massless; [the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison)).
- **Wording that differs between the notes.** #7 counts "three structural tests in a row" where #11 §15 counts "four consecutive consistency tests", and #11 governs. What X eats is "the four would-be Goldstones π_μ" in #6 but "the vector π_μ and the longitudinal scalar of the λ-gradient sector" in #8; #11 §7.1 follows #6, and no document reconciles the two ([the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs); [Conflicts between sources](/wiki/history/documents/source-conflicts)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §5 and §7 — the current statements of the notes' results and their tags; §2 — the battery's coverage; §15 — "four consecutive consistency tests"
- `HANDOFF.md` §3 rows 5–8 — the notes' standing
- `verify/battery.py` — tests T1–T7
- `notes/debt1a-geometric-core.md` — the compatibility theorem, P2 → P2′, the modular field and the gate's mechanism
- `notes/debt1a-ii-X-classification.md` — X as a massive spin-2 field
- `notes/debt1a-iii-tuning-test.md` — the tuning test and constrained bimetric gravity
- `notes/debt1a-iv-beta-coefficients.md` — the palindrome, the vacuum-energy identity, the parameter count and the residue of Debt 1
