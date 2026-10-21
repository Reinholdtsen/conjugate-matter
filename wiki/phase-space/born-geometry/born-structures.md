---
title: "The structures ω, η, H and the split-quaternion algebra"
weight: 10
status: established
description: "I = ω⁻¹H, J = η⁻¹H, K = η⁻¹ω with I² = −1, J² = K² = +1, IJ = K: Freidel–Leigh–Minic's Born geometry, para-Hermitian geometry, and how ρ acts on the triple (it preserves ω and H and flips η)."
provenance: [T, D]
sources:
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md ref [3]"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-program-v1.md §3"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 3"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/debt1a-geometric-core.md §F"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/reciprocity-toy-models.md §1"
  - "verify/battery.py T1"
---

*Born geometry equips phase space with three structures: the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, the pairing behind the quantum commutator; a neutral metric η, a symmetric pairing with as many positive as negative directions, whose null directions mark out "position" and "momentum"; and a positive generalized metric H, a ruler on phase space. From the three one builds three operators, I, J and K, that multiply like the split quaternions: I squares to −1, while J and K square to +1. Freidel, Leigh and Minic named phase spaces with such a compatible triple Born geometries. The quarter-turn [ρ](/wiki/phase-space/reciprocity/born-reciprocity) preserves ω and H but reverses the sign of η, which is why the program treats η as the quantity whose vacuum value breaks the symmetry.*

**Status:** Established — the algebra is literature [T] (Freidel–Leigh–Minic, #11 ref. [3†]); the action of ρ on the triple is derived here [D] (#1 §2) — not machine-checked as an algebra; battery test T1 checks J² = 1 and I² = −1 on the compatible metrics ([the battery](/wiki/method/verification/battery)).

## Key facts

- **Standard forms.** In the (x, p) block basis, with d = 4 and "units chosen so a reference length λ and momentum ε = ℏ/λ are scaled out" (#1 §2):

  ```text
  ω = [[0, 1], [−1, 0]]     η = [[0, 1], [1, 0]]     H = [[1, 0], [0, 1]]
  ```

- **The algebra.** With ω and η standard, #11 §5 defines three operators and states their products:

  ```text
  I = ω⁻¹H     J = η⁻¹H     K = η⁻¹ω
  I² = −1      J² = K² = +1      IJ = K
  ```

  This is "a split-quaternion algebra (Born geometry [3†]; a unique compatible connection exists [7†])" (#11 §5). The connection is [the Born connection](/wiki/phase-space/born-geometry/born-connection).

- **The name.** #1 §2 [T]: "A compatible triple (ω, η, H) realizing this algebra is precisely a Born geometry in the sense of Freidel, Leigh & Minic." The round-3 referee located the term in arXiv:1502.08005, p. 11, where phase spaces with such I, J, K "were referred to as Born geometries", with I a complex structure when the B-field vanishes. The referee writes I = H⁻¹ω; this wiki follows #11, I = ω⁻¹H. The vanishing B-field is the content of [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem).
- **ρ on the triple [D].** #1 §2: the Born rotation "preserves ω (it is symplectic), preserves H (it is orthogonal), and flips the sign of η, hence flips J and K while preserving I." Under P2′ this "now reads correctly as the broken symmetry moving the order parameter" (#5 §B). ρ² preserves all three structures; the breaking pattern ℤ₄ → ℤ₂ that #1 drew from this is superseded by the Goldstone-angle picture of #11 v2.2 ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).
- **Which operator is "the real structure" (unreconciled).** The documents name it differently, and none reconciles the two:

  ```text
  #11 P2′:                                  η = HJ    "the real structure J"
  toy-model note §1, #11 §14 item 11:       η = ωK    K the real structure, K² = 1
  ```

  This page uses #11 §5's definitions above. [The order parameter](/wiki/symmetry-breaking/order-parameter) records both conventions.
- **η's null lines.** η is "a neutral (split-signature) metric" (#1 P1). In the toy model its null lines are the two eigenlines L± of K, which are Lagrangian (toy-model note §1) — see [Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations).
- **Literature.** #11 [3]† L. Freidel, R. G. Leigh, D. Minic, "Born reciprocity in string theory and the nature of spacetime," Phys. Lett. B 730, 302 (2014); "Quantum gravity, dynamical phase space and string theory," Int. J. Mod. Phys. D 23, 1442006 (2014). For the (ω, H)-only structure of P2′, #5 §F names the para-Hermitian literature (Svoboda; Marotta–Szabo) as "the nearest neighbor".

## Used by

- [P1: the phase-space arena](/wiki/program/postulates/p1-arena) — physics on phase space with ω and a positive generalized metric H.
- [P3: a reciprocity-invariant action](/wiki/program/postulates/p3-reciprocity) — the Born rotation generated by I = ω⁻¹H.
- [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) — η, J and K as the quantities ρ moves.
- [The hard core: spontaneously broken Born reciprocity](/wiki/program/hard-core) — ω rigid, η emergent.
- [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential) — the anticommutator of J with I[Z] measures misalignment.

## Sources

- `papers/broken-born-checkpoint-v2.md` §5 and ref. [3] — the algebra and its attribution.
- `papers/broken-born-checkpoint-v2.md` §4 — P2′ and P3 in terms of J and I.
- `notes/broken-born-theory.md` §1, §2 — the standard forms, the algebra tagged [T], ρ's action on the triple [D].
- `notes/broken-born-program-v1.md` §3 — the same algebra as "Born geometry in the sense of Freidel–Leigh–Minic [T]".
- `notes/debt1a-geometric-core.md` §B, §F — ρ moving the order parameter; the para-Hermitian neighbor.
- `papers/reciprocity-toy-models.md` §1 — K as the real structure, η = ωK, and its Lagrangian null lines.
- `review/round3/referee/audit-notes.md` Step 1, Step 3 — the Born-geometry passage in arXiv:1502.08005 and the referee's I = H⁻¹ω.
- `verify/battery.py` T1 — J² = 1 and I² = −1 on H = diag(g, g⁻¹).
