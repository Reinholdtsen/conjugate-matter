---
title: "Curved momentum space"
weight: 80
status: established
description: "Snyder's quantized space-time, momenta on a curved group manifold in 2+1 gravity, and relative locality: the literature in which momentum space has geometry; with the soccer-ball (extensivity) problem, open here."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md refs [4]–[6]"
  - "notes/broken-born-theory.md §11 item 6"
  - "notes/broken-born-program-v1.md §1"
  - "notes/broken-born-program-v1.md §10"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "notes/broken-born-theory.md §3"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/knot-dark-matter-standalone.md §1"
---

*Curved momentum space is the idea, developed in a line of quantum-gravity research, that the space of momenta can carry a geometry of its own instead of being flat. Snyder used it in 1947 to build a quantized space-time; in quantum gravity with two space dimensions, which can be solved exactly, the momenta of a particle live on a curved space; and "relative locality" made the geometry of momentum space a principle. [General relativity](/wiki/gravity/spin-2-fields/general-relativity) curves space-time but leaves momentum space flat, which the program counts as an assumption rather than a measurement; its own version of momentum-space geometry is [the momentum graviton X](/wiki/gravity/momentum-graviton). One known difficulty of the idea, the soccer-ball problem, was listed as open in the [lab notebook](/wiki/history/documents/lab-notebook) and never resolved.*

**Status:** Established — literature [T] (#9 §1), cited in [#11](/wiki/history/documents/checkpoint) from model memory [4†–6†] and not yet source-checked ([the † literature battery](/wiki/method/literature-battery)) — the soccer-ball problem, folded in below, is open [O] (#1 §11 item 6) and absent from #11's open list.

## What curved momentum space means

In ordinary physics momentum space is flat [T]. A particle's momentum is a vector, the momenta of independent particles add as vectors, and the total momentum of a body is the sum of its parts. The relativistic energy–momentum relation, the mass shell, is a hyperboloid drawn in this flat space.

In a curved momentum space the set of possible momenta is a curved manifold [T]. Two consequences follow. The mass shell becomes a statement about distance in a curved geometry, and the momenta of two particles no longer combine by simple addition but by a nonlinear composition rule, as displacements on a sphere do not simply add [T]. The size of the departure is set by a curvature scale, a momentum or mass that the literature usually places near the [Planck scale](/wiki/gravity/spin-2-fields/planck-units#the-scale-of-quantum-gravity-t) [T]. For momenta far below that scale the geometry looks flat and the ordinary rules return.

## The lineage #11 cites

#11 §3 names three steps, all cited from model memory:

- **Snyder.** [4]† H. S. Snyder, "Quantized space-time," Phys. Rev. 71, 38 (1947). Snyder made the space-time coordinates non-commuting while keeping Lorentz invariance, by taking momentum space to be a space of constant curvature [T].
- **Gravity in 2+1 dimensions.** [5]† H.-J. Matschull, M. Welling, "Quantum mechanics of a point particle in 2+1 dimensional gravity," Class. Quantum Grav. 15, 2981 (1998), gr-qc/9708054. With two space dimensions, gravity has no propagating waves and can be solved exactly; the momenta of a point particle take values in a group manifold, which is curved [T]. #11's wording: "the one exactly solved quantum gravity (2+1d, where momenta live on a curved group manifold [5†])". The v1 paper states the same result as [T] without a reference (#9 §1).
- **Relative locality.** [6]† G. Amelino-Camelia, L. Freidel, J. Kowalski-Glikman, L. Smolin, "The principle of relative locality," Phys. Rev. D 84, 084010 (2011), arXiv:1101.0931. It takes momentum space as the primary arena; its geometry fixes how momenta compose, and whether two events coincide can then depend on the observer [T].

None of the three has been checked against its source; they are part of [the † literature battery](/wiki/method/literature-battery) (OP10).

## The program's framing

#11 §3 cites the lineage to make one point about [Born's question](/wiki/program/borns-question): that the asymmetry between position and momentum lives in the dynamics. Among the dynamical sources of the asymmetry it lists "general relativity's flat momentum fibers — the last an architectural assumption, not a measurement, and false in the one exactly solved quantum gravity (2+1d, where momenta live on a curved group manifold [5†]; curved momentum space has an independent lineage from Snyder [4†] through relative locality [6†])." The v1 paper says the same, tagged [T]: general relativity "curves x-space while leaving momentum fibers flat — an assumption of the formalism, not a measurement, and one that is *false* in the one exactly solved quantum gravity (2+1 dimensions, where momentum space is a curved group manifold) [T]" (#9 §1).

The point is negative: flat momentum space is not forced by any measurement. It does not by itself say what geometry momentum space has.

## The program's own momentum-space geometry

The program's answer comes from its phase-space geometry rather than from the Snyder lineage.

1. **Two metrics in one.** The generalized metric H on phase space ([the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)) contains both: "On the x-tilted vacuum, H decomposes into a spacetime metric g_μν(x) and a momentum-space metric g̃^μν" (#1 §3).
2. **In the vacuum the momentum metric is not independent.** With the neutral metric held rigid (the [original P2](/wiki/program/postulates/original-p2)), or under [P2′](/wiki/program/postulates/p2-prime) on the vacuum slice X = 0, which #11 §6 identifies with the η-compatible locus, the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) forces H = diag(g, g⁻¹), and "The momentum metric is slaved: g̃ = g⁻¹ pointwise. No independent momentum-space geometry survives." ([#5](/wiki/history/documents/debt-1-notes) §A; [the corollaries](/wiki/phase-space/born-geometry/compatibility-corollaries)).
3. **Off the vacuum it lives in X.** Once only ω is rigid, the metric becomes the [modular field Z](/wiki/phase-space/modular-field/modular-field-z) = X + iY, and "any independent momentum-space geometry resides in the fluctuation X" ([#14](/wiki/dark-matter/candidates/soliton-candidate) §1, the withdrawn manuscript). The calc note: "Born's debt, restated exactly: *the field equation for momentum-space geometry is the Re Z sector of S_H.*" (#5 §C).
4. **Born's answer.** #11 §7: "momentum-space geometry is dynamical — a reciprocity-odd massive spin-2, its mass born of the polarization choice … Momentum space gravitates, massively and invisibly to everything not polarized its way". See [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer).

The program's momentum geometry is thus a dynamical metric on momentum space, short-ranged because X is massive. No document compares it in detail with the Snyder or relative-locality constructions; the one place they meet is the open problem below.

## Open: extensivity (the soccer-ball problem)

**The problem in general [T].** If momenta compose nonlinearly, with corrections set by a Planck-scale momentum, the corrections are negligible for an elementary particle but not for the total momentum of a macroscopic body. A kicked ball can carry more momentum than the Planck scale. If the deformed rules applied to such a total, everyday bodies would show large departures from ordinary momentum addition, and they do not. Any theory with curved momentum space has to explain why the curvature does not show up for macroscopic momenta.

**As the program states it.** The lab notebook's sixth open problem: "**Extensivity (the soccer ball)**: why macroscopic momenta don't probe g̃ curvature; patched by standard coproduct rescaling, which is ad hoc here as everywhere. **[O]**" (#1 §11 item 6). Here g̃ is the program's momentum-space metric. The "coproduct" is the rule, in the algebraic description of deformed symmetries, that combines the momenta of subsystems; rescaling it makes the effective curvature scale grow with the number of constituents, so a body of many particles behaves classically [T]. #1 calls the patch ad hoc in every theory that uses it, the program's included.

**Fate.** The item was dropped from later open-problem lists without a resolution. It is absent from #9 §10 and from #11 §14, and no document returns to it. Its status is therefore still open [O], on the lab notebook's authority. It qualifies the program's claim that momentum-space geometry is dynamical ([Born's answer](/wiki/gravity/momentum-graviton/borns-answer)); whether it arises for the massive, short-ranged X in the same form as for Snyder-type models is not analysed anywhere. See [open problems and the queue](/wiki/status/open-problems).

## Standard references

#11's three references, [4]†, [5]† and [6]†, are listed above. One more is added by the wiki from model memory (†):

- G. Amelino-Camelia, L. Freidel, J. Kowalski-Glikman, L. Smolin, "Relative locality and the soccer ball problem" (2011)†.

## Used by

- [Born's question](/wiki/program/borns-question) — general relativity's flat momentum fibers as one source of the asymmetry.
- [Born's answer: momentum space gravitates](/wiki/gravity/momentum-graviton/borns-answer) — the program's dynamical momentum-space geometry.
- [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z) — X as the carrier of independent momentum-space geometry.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 and refs [4]–[6] — the lineage Snyder → 2+1 gravity → relative locality, all †.
- `papers/broken-born-checkpoint-v2.md` §7 — Born's answer: momentum-space geometry as a massive spin-2 field.
- `papers/broken-born-checkpoint-v2.md` §14 — the current open-problem list, which does not carry extensivity.
- `notes/debt1a-geometric-core.md` §A, §C — g̃ = g⁻¹ slaved; momentum-space geometry as the Re Z sector.
- `notes/broken-born-program-v1.md` §1, §10 — the 2+1 statement tagged [T]; v1's open-problem list, without extensivity.
- `notes/broken-born-theory.md` §3, §11 item 6 — H split into g and g̃; the soccer-ball problem as #1 stated it.
- `notes/knot-dark-matter-standalone.md` §1 — independent momentum-space geometry resides in X (withdrawn paper).
