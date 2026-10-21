---
title: "P1: the phase-space arena"
weight: 10
status: alive
description: "Physics lives on phase space with a symplectic form ω and a positive generalized metric H; the lab notebook's version also listed η as a structure."
provenance: [P]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
---

*P1 is the program's first axiom: physics is formulated on phase space, the space whose points are a position together with a momentum, rather than on spacetime alone. The axiom gives phase space two structures. The symplectic form ω is the antisymmetric pairing of position with momentum that quantum mechanics fixes through Planck's constant; the generalized metric H is a positive measure of distance that treats both kinds of coordinate together. The lab notebook's first version of P1 also listed a third structure, the neutral metric η; the current version lists only ω and H, and P2′ makes η a property of the vacuum.*

**Status:** Alive — [P] — a postulate of #11 §4; postulates are assumed, not derived or machine-checked.

## Key facts

- Current statement (#11 §4):

  ```text
  P1  Physics on phase space with symplectic form ω and positive
      generalized metric H.                                        [P]
  ```

- Lab-notebook statement (#1 §1, v0.1): "P1 (Arena). Physics is formulated on phase space 𝒫 carrying a *Born geometry*: a symplectic form ω, a neutral (split-signature) metric η, and a positive generalized metric H, mutually compatible". See [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures) and [the symplectic form](/wiki/phase-space/reciprocity/symplectic-form).
- Standard forms (#1 §2), on flat phase space ℝ²ᵈ with d = 4, in the (x, p) block basis, "units chosen so a reference length λ and momentum ε = ℏ/λ are scaled out":

  ```text
  ω = [[0, 1], [−1, 0]]     η = [[0, 1], [1, 0]]     H = [[1, 0], [0, 1]]
  ```

- From P1's two structures the program builds I = ω⁻¹H. A positive H is compatible with ω when (ω⁻¹H)² = −1, so that I is a complex structure (#11 §5); [P3](/wiki/program/postulates/p3-reciprocity) states the symmetry in terms of I.
- Under the [original P2](/wiki/program/postulates/original-p2), which also fixed η, the allowed H are exactly diag(g, g⁻¹) ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), [T][V]).
- Under [P2′](/wiki/program/postulates/p2-prime), with only ω rigid, "H ranges over Sp(2d,ℝ)/U(d): Z = X + iY (symmetric; Y > 0)", with "I[Z]² = −1 machine-verified [V]" (#11 §6; battery test T2, [the verification battery](/wiki/method/verification/battery)). See [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain) and [the modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — the current statement; §5–§6 — what H can be under P2 and under P2′
- `notes/broken-born-theory.md` §1 — the v0.1 statement, with η; §2 — the standard forms
