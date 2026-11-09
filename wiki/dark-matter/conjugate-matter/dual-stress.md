---
title: "Dual stress T̃"
weight: 20
status: alive
description: "The momentum-side counterpart of stress-energy, built from momentum derivatives of the χ bilinear: the quantity X couples to."
provenance: [D]
sources:
  - "notes/geometric-core.md §E"
  - "notes/geometric-core.md §C"
  - "notes/x-classification.md §4"
  - "notes/beta-coefficients.md §3"
  - "notes/beta-coefficients.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "HANDOFF.md §4"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §3"
  - "notes/gate-mechanism.md §5"
  - "notes/gate-mechanism.md §6"
  - "verify/gate_mechanism.py"
---

*The dual stress, written T̃, is the quantity through which matter couples to the [momentum graviton X](../../gravity/momentum-graviton/_index.md), in the way the stress-energy tensor is the quantity through which matter couples to the ordinary graviton. Stress-energy is built from derivatives of a matter field along spacetime and describes how energy and momentum are distributed in position; the dual stress is built from derivatives along the momentum directions and so reflects how the field is structured across momentum, the spectrum side of the same field. The calc notes say that exchange of X between the dual stresses of two particles of [conjugate matter](_index.md) produces [the velocity gate](velocity-gate.md); a note of 2026-10-28 finds that it cannot (flag 55, pending). The calc notes define the dual stress in words and give no formula for it. Why it is strong for conjugate matter and weak for ordinary matter is [an open problem](dual-stress-enhancement.md).*

**Status:** Alive — [D — structural] ([`notes/geometric-core.md` §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural)) — a definition in words, with no explicit formula in any source; the definition is not machine-checked. The gate it is said to deliver is disputed: [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate, and flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism; [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) tags the mechanism [D] ([the gate mechanism](gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). [`verify/gate_mechanism.py`](../../../verify/gate_mechanism.py) reruns the note's arithmetic and algebra, on which the [V] of its tag below rests, and does not test its physics ([the gate-mechanism script](../../method/verification/gate-mechanism-script.md)). Why it is enhanced for conjugate matter is [Open: the dual-stress enhancement (OP5)](dual-stress-enhancement.md).

## Definition

The dual stress enters in calc note [#5](../../../notes/geometric-core.md), the first of [the field-equation calc notes](../../history/documents/field-equation-notes.md), in a section headed "The gate problem — the mechanism, found [D — structural]":

> "Conjugate matter couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃ — moments involving momentum-derivatives of the χ bilinear. Exchange of X between two such bilinears yields a four-point amplitude that depends on the **incoming relative momenta** of the pair — the variable no x-local mediator can produce, and exactly the variable the gate was postulated in." ([`notes/geometric-core.md` §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural))

The sentence has three parts.

- **"couples to H universally (P4)"**. H is the [generalized metric](../../phase-space/born-geometry/born-structures.md) on phase space. Postulate [P4](../../program/postulates/p4-polarized-matter.md) says matter comes in "x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H" ([#11](../../history/documents/checkpoint.md) [§4](../../papers/broken-born-checkpoint-v2.md#4-postulates)). χ is [conjugate matter](_index.md), the representation polarized toward momentum; the Standard Model (SM) is ordinary matter, polarized toward position.
- **"the X-block"**. Calc note #5 writes H through the [modular field](../../phase-space/modular-field/modular-field-z.md) Z = X + iY, with Y = g the spacetime metric and X the momentum graviton ([§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)):

  ```text
  H_Z = [ Y + X Y⁻¹ X    X Y⁻¹ ]
        [ Y⁻¹ X          Y⁻¹   ]
  ```

  At X = 0 the off-diagonal blocks vanish and H reduces to diag(g, g⁻¹). The "X-block" is the part of H that X carries, and the dual stress is what χ couples to there. The note does not say which entries of H_Z it has in mind.
- **"moments involving momentum-derivatives of the χ bilinear"**. A bilinear is a product of the field with its conjugate, such as χ\*χ for a complex scalar [T]; ordinary stress-energy is such a bilinear with two spacetime derivatives (below). The dual stress is built instead from derivatives with respect to momentum, along the [momentum fiber](../../phase-space/reciprocity/momentum-fibers.md#the-dual-stress-derivatives-along-the-fiber), the momentum directions of phase space attached to each point of spacetime. The note uses the word "moments" and specifies neither which moments nor their weights. No later document writes T̃ out.

## Background: stress-energy as the charge of gravity [T]

The stress-energy tensor T_μν of a matter field collects its energy density, its momentum density and its internal stresses. For a free complex scalar field it is a bilinear in first derivatives of the field, of the form ∂_μχ\*∂_νχ plus terms fixed by the metric [T]. It is the source in Einstein's equation, and at linear order the graviton h_μν couples to matter through the product h_μν T^μν, with a strength set by the [Planck mass](../../gravity/spin-2-fields/planck-units.md#the-coupling-of-a-spin-2-field) [T]. Every form of energy enters T_μν in the same way, which is the universality of gravity, [the equivalence principle](../../gravity/spin-2-fields/equivalence-principle.md#how-general-relativity-builds-it-in-t) [T].

The name "dual stress" places T̃ in the same role for X: the quantity of matter that X couples to. Where T_μν records how a field's energy is arranged in position, T̃ is built from its structure across momentum, as a signal's spectrum describes it across frequency rather than time. The calc notes go no further than this analogy and the words quoted above; they give T̃ no index structure, no normalization and no conservation law.

## What the coupling produces: the gate

A coupling of X to a bilinear in χ gives a vertex with two χ lines and one X line. Joining two such vertices by an X propagator gives an amplitude with four χ lines: two particles in, two out [T]. Calc note #5 states the result of that exchange: a four-point amplitude "that depends on the **incoming relative momenta** of the pair" ([§E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural)), which is the variable of the velocity gate. [The lab notebook](../../history/documents/lab-notebook.md)'s v0.3 addendum records the same step: "the *mechanism* is X-exchange between χ dual-stress bilinears, which produces dependence on incoming relative momenta — the defining property of the gate" ([#1](../../../notes/broken-born-theory.md) 'Addendum (v0.3, overnight)').

Calc note [#6](../../../notes/x-classification.md) completed the mechanism by integrating out the massive X and attributing the momentum dependence to the χ quantum's width μ along the momentum fiber ([the gate mechanism](gate-mechanism.md)). The checkpoint carries the outcome: the gate is "delivered by X-exchange between dual-stress bilinears" ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)), and v1 has the same words ([#9 §6](../../../notes/broken-born-program-v1.md#6-conjugate-matter-and-the-gate-the-gate-problem-mechanism-found)). Calc note [#8](../../../notes/beta-coefficients.md)'s summary of the momentum graviton couples X "to conjugate matter through the dual stress (the gate) and to ordinary matter only at gravitational strength and short range" ([`notes/beta-coefficients.md` §4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born)).

The derivation is structural. No source writes the vertex, the X propagator on the momentum fibers or the four-point amplitude explicitly, and no `verify/` script checks any part of it.

### What the gate-mechanism note finds

[`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28, not reviewed) audits the record for the pieces this mechanism needs and finds none of them: "No χχX vertex, X propagator on the fibers, χ fiber profile, formula for the dual stress T̃, overlap integral or verify script exists" ([§3](../../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways)) [D, record audit]. It adds that the section condition makes H_Z, and with it X, depend on position only, so "X propagator on momentum fibers" has no meaning within [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) ([§3](../../papers/broken-born-checkpoint-v2.md#3-the-question)). Writing the most general vertex instead, it finds that for on-shell χ any χ–χ–X vertex depends only on the transfer t, local, derivative and form-factor vertices alike; a nonlocal dual stress weighted along the fiber becomes a function of t as well, because the fiber coordinate of a χ\*χ bilinear is the average momentum (one derivation) ([§2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification)) [D][V]. Exchange of X then gives an amplitude whose dependence on the incoming relative momentum is a polynomial with the speed of light as its velocity scale, not a gate ([§2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification)). Flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism, and the note lists "the wiki's gate-mechanism, gate-shape and dual-stress pages" among the text that depends on the tag (§5). [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)'s "delivered by X-exchange between dual-stress bilinears" stands in the record ([the gate mechanism](gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). The strength of the coupling, the enhancement below, "stays open whatever the mechanism" ([§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)).

## Ordinary matter's dual stress

Ordinary matter is polarized toward position, and the calc notes first used its dual stress to explain why it shows no sign of X. The argument changed across the notes.

- **Calc note [#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) [O]:** "SM safety: X is massive and couples to x-polarized matter only through its (suppressed) dual stress; short-range, fifth-force-safe — to be verified when the propagator exists [O]."
- **Calc note [#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade):** "Massive X ⇒ short-ranged, safe; couplings to x-polarized (SM) matter run through the SM's dual stress, which is unenhanced. [Consistency preserved; quantify with the propagator later.]"
- **Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) [D + T]:** the coupling of ordinary matter to X runs through the metric g, which contains both spin-2 eigenstates once [reciprocity](../../phase-space/reciprocity/born-reciprocity.md) forces equal Planck masses: "SM matter — coupled to g — sees both eigenstates with comparable strength; safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X" ([Yukawa forces](../../gravity/spin-2-fields/yukawa-forces.md#the-momentum-graviton-x)).

In #8's form, the current one, the dual stress no longer carries the argument; ordinary matter feels X at gravitational strength and is protected by X's short range. The full argument and its history are on [safety by range](../../gravity/momentum-graviton/fifth-force-safety.md).

## What is open

- **No formula.** T̃ is defined only in words ([#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural)). Its explicit form waits on the same calculation as [the gate shape](gate-shape.md): [#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) places the shape in "the X propagator's structure on the momentum fibers — open [O]". [`notes/gate-mechanism.md` §3](../../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways) finds that the section condition gives that propagator no meaning within [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) (flag 55).
- **The enhancement.** Calc note #8 logs the strength of the coupling as the main open quantitative item: "[Parametrics of the χ dual-stress enhancement — why σ₀ can be nuclear-scale while SM couplings stay gravitational — logged as the main open quantitative item.]" ([§3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)). [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) calls it the "Main open quantitative item" and [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) lists it as item 5; see [Open: the dual-stress enhancement (OP5)](dual-stress-enhancement.md).

## Chat-only: dual stress as a second gravitational charge

[The handoff](../../history/documents/handoff.md) records a reading of the dual stress that exists only in the original conversation, among its "Results that exist only in the chat" (the handoff sets "only" in capitals):

> "**Two gravitational charges:** ordinary stress-energy (sources massless graviton) vs dual stress "how energy is structured across momentum" (sources X); independent numbers; equivalence principle intact; whether invariant length λ and dual charge lock together = "dual equivalence principle" open question." ([`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact))

The documented part is the coupling of conjugate matter to X through T̃ ([#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural); [#8 §4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born)). The rest, that the two charges are independent numbers and that a "dual equivalence principle" might tie the second to the invariant length of [conjugate special relativity](../../conjugate-relativity/_index.md), is derived in no document. Its status is conjecture. The page [Two gravitational charges and the conjugate field equations (chat-only)](../../gravity/momentum-graviton/chat-only-results.md) separates the documented and undocumented parts.

## Where it comes from

Calc note #5 is subtitled "(plus an unplanned result on the gate problem)": the dual stress appeared while the note was working on the geometric core, as the coupling through which the newly identified X could carry the gate ([the three main problems](../../history/main-problems.md)). The lab notebook's v0.3 addendum, which reports calc note #5, took it up. Calc note #6 used the term for ordinary matter's "unenhanced" coupling, and #8 for the open enhancement and in its summary of X. v1 ([#9 §6](../../../notes/broken-born-program-v1.md#6-conjugate-matter-and-the-gate-the-gate-problem-mechanism-found)) and [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) keep only the phrase "dual-stress bilinears" in the statement of the gate, and "dual-stress enhancement" among the open problems.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the gate delivered by X exchange between dual-stress bilinears; the enhancement as the main open quantitative item; [§4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — P4, universal coupling to H
- [`notes/broken-born-program-v1.md` §6](../../../notes/broken-born-program-v1.md#6-conjugate-matter-and-the-gate-the-gate-problem-mechanism-found) — v1's statement of the gate
- [`notes/geometric-core.md` §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) — the definition, the four-point amplitude, the first statement of ordinary-matter safety; [§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — H in terms of Z = X + iY
- [`notes/x-classification.md` §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — ordinary matter's dual stress as unenhanced
- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — safety by range; the enhancement logged as the main open quantitative item; [§4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born) — X coupled to conjugate matter through the dual stress
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.3, overnight)' — X exchange between dual-stress bilinears as the gate's mechanism
- [`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — the chat-only "two gravitational charges"
- [`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate) — every on-shell vertex depends only on the transfer, the fiber-weighted dual stress included; [§3](../../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways) — the record audit: no formula for T̃, no χχX vertex, X depends on position only; [§5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record) — the proposed tags and the pages that depend on them; [§6](../../../notes/gate-mechanism.md#6-record) — what the script tests
- [`verify/gate_mechanism.py`](../../../verify/gate_mechanism.py) — reruns the note's arithmetic and algebra ([the gate-mechanism script](../../method/verification/gate-mechanism-script.md))
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 55 — the mechanism not derived, pending
