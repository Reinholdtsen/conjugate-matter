---
title: "The nontriviality theorem"
weight: 30
status: alive
description: "The program has content beyond general relativity plus self-interacting dark matter if and only if η is emergent: under strict P2 the action S_H depends on g alone and the dark-energy sector disappears."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/broken-born-theory.md 'Addendum (v0.3)'"
  - "notes/broken-born-program-v1.md §2–§3"
---

*The nontriviality theorem states that the Broken-Born program predicts anything beyond general relativity plus one model of self-interacting dark matter only if the neutral metric η, the structure that marks which directions count as position, is chosen by the vacuum rather than fixed in advance. It is the argument that forced the program to change its second axiom. With η fixed, the vacuum can pick among only a discrete set of position–momentum splittings, so the circle on which the program's dark-energy field lives does not exist, and the geometric action depends only on the ordinary spacetime metric. The result stands as a derived structural result of the program, and it is the reason the [original P2](/wiki/program/postulates/original-p2) was replaced by [P2′](/wiki/program/postulates/p2-prime).*

**Status:** Alive — [D] in #11 §4; the note that derived it tags its section "[D — structural]" — not machine-checked itself; its input, [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), is [T][V] (battery test T1, [the verification battery](/wiki/method/verification/battery)).

## Key facts

- #11 §4 (under P2′): "the correction from the original P2 is *forced*: a nontriviality theorem (§5) shows the theory has content beyond GR + SIDM iff η is emergent. [D]" GR + SIDM is general relativity plus self-interacting dark matter.
- #11 §5: "Under strict P2 the compatible polarizations are discrete, so no Grassmannian, no Maslov circle, no dark-energy field, and S_H is a functional of g alone: **nontriviality theorem** — the program has content iff η is emergent. Hence P2 → P2′."
- Where it was derived (#5 §B, "[D — structural]"): "**Program-nontriviality theorem:** BBT has content beyond GR + SIDM **iff** η is emergent. P2 → P2′ is not optional." BBT is the Broken-Born program.
- The input (#11 §5, [T][V]): "Positive H satisfying both (η⁻¹H)² = 1 and (ω⁻¹H)² = −1 are exactly H = diag(g, g⁻¹), g ∈ Sym⁺(d)." The statement is credited to Freidel, Leigh and Minic since v2.1; the block proof and the machine check are the program's.
- What strict P2 removes: the [Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) and its Maslov circle, hence [τ](/wiki/phase-space/modular-field/maslov-phase), the dark-energy field; and the momentum graviton, "hence no geometric origin for the χ gate either" (#5 §B). What is left is Branch R, the [original P2](/wiki/program/postulates/original-p2)'s reduced theory.
- What P2′ restores (#5 §B): the vacuum's choices form "{J} ≅ U(d)/O(d) = Λ(d), the Lagrangian Grassmannian — π₁ = ℤ, Maslov circle intact, τ restored".
- Caveats in the record: the result is called a theorem inside a section tagged [D — structural]; and the v1 paper's pointers for it are circular (#9 §2 cites "the theorems of §3 and §5", and §3 cites "the nontriviality theorem of §2").

## Sources

- `papers/broken-born-checkpoint-v2.md` §4–§5 — the current statement, tagged [D]
- `notes/debt1a-geometric-core.md` §B — the derivation ("[D — structural]"), Branch R and the repair
- `notes/broken-born-theory.md` 'Addendum (v0.3)' — the axiom correction as first recorded
- `notes/broken-born-program-v1.md` §2–§3 — the v1 statement (superseded by #11)
