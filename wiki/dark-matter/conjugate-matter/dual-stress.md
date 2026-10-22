---
title: "Dual stress T̃"
weight: 20
status: alive
description: "The momentum-side counterpart of stress-energy, built from momentum derivatives of the χ bilinear: the quantity X couples to."
provenance: [D]
sources:
  - "notes/debt1a-geometric-core.md §E"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §4"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "HANDOFF.md §4"
---

*The dual stress, written T̃, is the quantity through which matter couples to the [momentum graviton X](/wiki/gravity/momentum-graviton), in the way the stress-energy tensor is the quantity through which matter couples to the ordinary graviton. Stress-energy is built from derivatives of a matter field along spacetime and describes how energy and momentum are distributed in position; the dual stress is built from derivatives along the momentum directions and so reflects how the field is structured across momentum, the spectrum side of the same field. Exchange of X between the dual stresses of two particles of [conjugate matter](/wiki/dark-matter/conjugate-matter) produces [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate). The calc notes define the dual stress in words and give no formula for it. Why it is strong for conjugate matter and weak for ordinary matter is [an open problem](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).*

**Status:** Alive — [D — structural] (`notes/debt1a-geometric-core.md` §E) — a definition in words, with no explicit formula in any source; not machine-checked. Why it is enhanced for conjugate matter is [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).

## Definition

The dual stress enters in calc note #5, the first of [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes), in a section headed "Debt 2 — the mechanism, found [D — structural]":

> "Conjugate matter couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃ — moments involving momentum-derivatives of the χ bilinear. Exchange of X between two such bilinears yields a four-point amplitude that depends on the **incoming relative momenta** of the pair — the variable no x-local mediator can produce, and exactly the variable the gate was postulated in." (`notes/debt1a-geometric-core.md` §E)

The sentence has three parts.

- **"couples to H universally (P4)"**. H is the [generalized metric](/wiki/phase-space/born-geometry/born-structures) on phase space. Postulate [P4](/wiki/program/postulates/p4-polarized-matter) says matter comes in "x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H" ([#11](/wiki/history/documents/checkpoint) §4). χ is [conjugate matter](/wiki/dark-matter/conjugate-matter), the representation polarized toward momentum; the Standard Model (SM) is ordinary matter, polarized toward position.
- **"the X-block"**. Calc note #5 writes H through the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY, with Y = g the spacetime metric and X the momentum graviton (§C):

  ```text
  H_Z = [ Y + X Y⁻¹ X    X Y⁻¹ ]
        [ Y⁻¹ X          Y⁻¹   ]
  ```

  At X = 0 the off-diagonal blocks vanish and H reduces to diag(g, g⁻¹). The "X-block" is the part of H that X carries, and the dual stress is what χ couples to there. The note does not say which entries of H_Z it has in mind.
- **"moments involving momentum-derivatives of the χ bilinear"**. A bilinear is a product of the field with its conjugate, such as χ\*χ for a complex scalar [T]; ordinary stress-energy is such a bilinear with two spacetime derivatives (below). The dual stress is built instead from derivatives with respect to momentum, along the momentum fiber, the momentum directions of phase space attached to each point of spacetime. The note uses the word "moments" and specifies neither which moments nor their weights. No later document writes T̃ out.

## Background: stress-energy as the charge of gravity [T]

The stress-energy tensor T_μν of a matter field collects its energy density, its momentum density and its internal stresses. For a free complex scalar field it is a bilinear in first derivatives of the field, of the form ∂_μχ\*∂_νχ plus terms fixed by the metric [T]. It is the source in Einstein's equation, and at linear order the graviton h_μν couples to matter through the product h_μν T^μν, with a strength set by the Planck mass [T]. Every form of energy enters T_μν in the same way, which is the universality of gravity, [the equivalence principle](/wiki/gravity/spin-2-fields/general-relativity#the-equivalence-principle-and-rindler-frames-t) [T].

The name "dual stress" places T̃ in the same role for X: the quantity of matter that X couples to. Where T_μν records how a field's energy is arranged in position, T̃ is built from its structure across momentum, as a signal's spectrum describes it across frequency rather than time. The calc notes go no further than this analogy and the words quoted above; they give T̃ no index structure, no normalization and no conservation law.

## What the coupling produces: the gate

A coupling of X to a bilinear in χ gives a vertex with two χ lines and one X line. Joining two such vertices by an X propagator gives an amplitude with four χ lines: two particles in, two out [T]. Calc note #5 states the result of that exchange: a four-point amplitude "that depends on the **incoming relative momenta** of the pair" (§E), which is the variable of the velocity gate. [The lab notebook](/wiki/history/documents/lab-notebook)'s v0.3 addendum records the same step: "the *mechanism* is X-exchange between χ dual-stress bilinears, which produces dependence on incoming relative momenta — the defining property of the gate" (#1 'Addendum (v0.3, overnight)').

Calc note #6 completed the mechanism by integrating out the massive X and attributing the momentum dependence to the χ quantum's width μ along the momentum fiber ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). The checkpoint carries the outcome: the gate is "delivered by X-exchange between dual-stress bilinears" (#11 §8), and v1 has the same words (#9 §6). Calc note #8's summary of the momentum graviton couples X "to conjugate matter through the dual stress (the gate) and to ordinary matter only at gravitational strength and short range" (`notes/debt1a-iv-beta-coefficients.md` §4).

The derivation is structural. No source writes the vertex, the X propagator on the momentum fibers or the four-point amplitude explicitly, and no `verify/` script checks any part of it.

## Ordinary matter's dual stress

Ordinary matter is polarized toward position, and the calc notes first used its dual stress to explain why it shows no sign of X. The argument changed across the notes.

- **Calc note #5 §E [O]:** "SM safety: X is massive and couples to x-polarized matter only through its (suppressed) dual stress; short-range, fifth-force-safe — to be verified when the propagator exists [O]."
- **Calc note #6 §4:** "Massive X ⇒ short-ranged, safe; couplings to x-polarized (SM) matter run through the SM's dual stress, which is unenhanced. [Consistency preserved; quantify with the propagator later.]"
- **Calc note #8 §3 [D + T]:** the coupling of ordinary matter to X runs through the metric g, which contains both spin-2 eigenstates once [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) forces equal Planck masses: "SM matter — coupled to g — sees both eigenstates with comparable strength; safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X".

In #8's form, the current one, the dual stress no longer carries the argument; ordinary matter feels X at gravitational strength and is protected by X's short range. The full argument and its history are on [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety).

## What is open

- **No formula.** T̃ is defined only in words (#5 §E). Its explicit form waits on the same calculation as [the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape): #5 §E places the shape in "the X propagator's structure on the momentum fibers — open [O]".
- **The enhancement.** Calc note #8 logs the strength of the coupling as the main open quantitative item: "[Parametrics of the χ dual-stress enhancement — why σ₀ can be nuclear-scale while SM couplings stay gravitational — logged as the main open quantitative item.]" (§3). #11 §8 calls it the "Main open quantitative item" and §14 lists it as item 5; see [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).

## Chat-only: dual stress as a second gravitational charge

[The handoff](/wiki/history/documents/handoff) records a reading of the dual stress that exists only in the original conversation, among its "Results that exist only in the chat" (the handoff sets "only" in capitals):

> "**Two gravitational charges:** ordinary stress-energy (sources massless graviton) vs dual stress "how energy is structured across momentum" (sources X); independent numbers; equivalence principle intact; whether invariant length λ and dual charge lock together = "dual equivalence principle" open question." (`HANDOFF.md` §4)

The documented part is the coupling of conjugate matter to X through T̃ (#5 §E; #8 §4). The rest, that the two charges are independent numbers and that a "dual equivalence principle" might tie the second to the invariant length of [conjugate special relativity](/wiki/conjugate-relativity), is derived in no document. Its status is conjecture. The page [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results) separates the documented and undocumented parts.

## Where it comes from

Calc note #5 is subtitled "(plus an unplanned payment on Debt 2)": the dual stress appeared while the note was working on the geometric core, as the coupling through which the newly identified X could carry the gate ([the three debts](/wiki/history/debts)). The lab notebook's v0.3 addendum, which reports calc note #5, took it up. Calc note #6 used the term for ordinary matter's "unenhanced" coupling, and #8 for the open enhancement and in its summary of X. v1 (#9 §6) and #11 §8 keep only the phrase "dual-stress bilinears" in the statement of the gate, and "dual-stress enhancement" among the open problems.

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the gate delivered by X exchange between dual-stress bilinears; the enhancement as the main open quantitative item; §4 — P4, universal coupling to H
- `notes/broken-born-program-v1.md` §6 — v1's statement of the gate
- `notes/debt1a-geometric-core.md` §E — the definition, the four-point amplitude, the first statement of ordinary-matter safety; §C — H in terms of Z = X + iY
- `notes/debt1a-ii-X-classification.md` §4 — ordinary matter's dual stress as unenhanced
- `notes/debt1a-iv-beta-coefficients.md` §3 — safety by range; the enhancement logged as the main open quantitative item; §4 — X coupled to conjugate matter through the dual stress
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)' — X exchange between dual-stress bilinears as the gate's mechanism
- `HANDOFF.md` §4 — the chat-only "two gravitational charges"
