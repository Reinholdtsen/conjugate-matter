---
title: "Double field theory and the generalized metric"
weight: 20
status: established
description: "String theory's doubled geometry: the O(d, d) generalized metric with its Kalb–Ramond B-field, and the section (strong) condition with its derivations — the contrast case for the program."
provenance: [T]
sources:
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-ii-X-classification.md §2"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §5"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "review/round3/referee/audit-notes.md Step 3"
---

*Double field theory is a formulation of string theory's low-energy fields on a doubled space, in which each ordinary coordinate has a partner "dual" coordinate. Its central object, the generalized metric, packages the spacetime metric together with an antisymmetric field, the Kalb–Ramond B-field, and its symmetry group O(d, d) is the group that preserves a neutral metric η. For the theory to be consistent, fields may depend on only half of the doubled coordinates — the section, or strong, condition. For the program it is the contrast case: doubling geometry with η gives a harmless antisymmetric partner field, doubling with the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω gives a second graviton, and holding ω rigid as well removes the B-field altogether.*

**Status:** Established — literature [T], with live-searched citations [S] (toy-model note §1; the worklog's section-condition search) — a mechanism that selects one section over its partner is open in the literature as well as in the program.

## Key facts

- **The η-only family.** Generalized metrics built from a metric and a B-field are compatible with η, and with ω only when the B-field vanishes. #11 §5, crediting Freidel, Leigh and Minic: "writing the η-compatible H in terms of (G, B), H is related to ω through a complex structure exactly when B vanishes [26S, §2.1]." Round 3's numerical check of this family: `eta residual <= 7e-14 but omega residual >= 0.28 (d=3), 1.48 (d=4)` (audit notes, Step 3). See [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem).
- **No B-field once ω is rigid [D — rigorous].** #5 §A, corollary 2: the off-diagonal block, double field theory's B-field, "is frozen out by the extra symplectic compatibility"; Born geometry with both structures rigid is "*stiffer* than" double field theory. See [the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries).
- **The partner's spin.** #6 §2: in double field theory "the doubled partner is the antisymmetric B-field, δB = dλ, a 2-form gauge theory — spin-wise harmless", whereas doubling with ω makes the partner of the metric a symmetric tensor — "the symplectic partner of the graviton is another graviton". See [the symplectic partner](/wiki/gravity/momentum-graviton/symplectic-partner).
- **A healthy precedent [T].** #5 §D: "the DFT precedent (graviton + B-field + dilaton, ghost-free) shows doubled-geometry kinetic operators can be healthy" — that is, double field theory's graviton, B-field and dilaton propagate without ghosts.
- **The section condition.** Toy-model note §1: "The section condition confines fields to a maximally isotropic subspace. It is imposed for closure of the gauge algebra [11], or derived from string consistency [12]. Those derivations leave the section undetermined within a family — a pair for d = 1, a continuous family for d > 1." The worklog's search ([S]) adds a derivation from worldsheet locality (arXiv:1502.08005 §6). Version 2 of the note restricted the worklog's unqualified "pair" to d = 1, after round 4. See [the section condition](/wiki/symmetry-breaking/section-condition).
- **Selection is claimed only in words.** The worklog (chunk 4, [S]): Freidel–Rudolph–Svoboda say the choice "might be subject to a dynamical selection rule"; Freidel–Leigh–Minic call it "a dynamical question"; and "Open: a mechanism that picks L over L̃." See [forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality).
- **References.** Toy-model note [11] C. Hull, B. Zwiebach, "Double field theory," JHEP 09 (2009) 099, arXiv:0904.4664; O. Hohm, C. Hull, B. Zwiebach, JHEP 07 (2010) 016, arXiv:1003.5027. [12] A. Betz, R. Blumenhagen, D. Lüst, F. Rennecke, JHEP 05 (2014) 044, arXiv:1402.1686.

## Used by

- [The section condition: what η fixes](/wiki/symmetry-breaking/section-condition) — the toy version of the condition, built from the vacuum's η.
- [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner) — the contrast between η-doubling and ω-doubling.
- [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content) — the precedent for healthy doubled kinetic terms.
- [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) — no known mechanism picks one section.

## Sources

- `notes/debt1a-geometric-core.md` §A, §D — corollary 2 (no Kalb–Ramond analog); the healthy precedent.
- `notes/debt1a-ii-X-classification.md` §2 — the B-field as a spin-harmless partner.
- `papers/broken-born-checkpoint-v2.md` §5 — the Freidel–Leigh–Minic statement in terms of (G, B).
- `papers/reciprocity-toy-models.md` §1, §5 — the section condition, its derivations, the d = 1 pair and the d > 1 family.
- `notes/toy-lagrangian.md` chunk 4 — the live-searched literature on deriving and selecting the section.
- `review/round3/referee/audit-notes.md` Step 3 — the η-only family checked numerically.
