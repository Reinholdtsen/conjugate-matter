---
title: "Two gravitational charges and the conjugate field equations (chat-only)"
weight: 110
status: conjecture
description: "Results that exist only in the old chat: dual stress as a second gravitational charge, the slaved layer as algebraic, the dual Newtonian limit as the gate, and massive X waves with a frequency floor."
sources:
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "notes/geometric-core.md §A"
  - "notes/geometric-core.md §E"
  - "notes/x-classification.md §3"
  - "notes/x-classification.md §4"
  - "notes/tuning-test.md §4"
  - "notes/beta-coefficients.md §3"
  - "notes/beta-coefficients.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.5"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 4"
  - "wiki/papers/conjugate-special-relativity.md §1"
  - "wiki/papers/conjugate-special-relativity.md §4"
  - "wiki/papers/conjugate-special-relativity.md §5"
  - "wiki/papers/conjugate-special-relativity.md §6"
  - "verify/battery.py T1"
  - "CLAUDE.md 'Since the handoff'"
  - "wiki/papers/phase-space-diameter.md §1"
  - "wiki/papers/phase-space-diameter.md §6"
  - "wiki/papers/phase-space-diameter.md §8.2"
  - "wiki/papers/phase-space-diameter.md §9"
  - "review/round5-adjudication.md 'Verdict'"
  - "review/wiki-build-flags.md item 29"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
---

*Two results from the program's original claude.ai conversation are derived in no project document: a claim that gravity has two charges, and a comparison of the program's field equations with those of [general relativity](../spin-2-fields/general-relativity.md). The [handoff document](../../history/documents/handoff.md) lists them in its §4, among the results that exist only in the chat, so that they are not lost. The first says gravity has two independent charges: ordinary stress-energy is the source of the massless graviton, and [dual stress](../../dark-matter/conjugate-matter/dual-stress.md), which measures how energy is structured across momentum, is the source of the [momentum graviton X](_index.md). Whether a "dual equivalence principle" ties the second charge to the [invariant length](../../conjugate-relativity/invariant-length-shell.md) of [conjugate quanta](../../dark-matter/conjugate-matter/_index.md) is left as a question. The second compares the program's field equations with those of general relativity: the [slaved momentum metric](../../phase-space/born-geometry/compatibility-corollaries.md) is fixed algebraically, the momentum-side counterpart of the Newtonian limit is a [Yukawa form in momentum](../spin-2-fields/yukawa-forces.md#conjugate-special-relativity-a-range-in-momentum) that is [the dark-matter gate](../../dark-matter/conjugate-matter/velocity-gate.md), and X waves are massive, with five polarizations and a lowest frequency. Parts of both have counterparts in [the calc notes](../../history/documents/field-equation-notes.md) and the papers; the rest has none. Both are conjectures: no artifact derives them and no script checks them.*

**Status:** Conjecture (chat-only) — no tags in the source — recorded only in [`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact); no derivation in any artifact, no `verify/` script, not on the work queue. Listed in [Conjectures: P.R.'s, the record's, chat-only and popsci-only claims](../../status/conjectures.md).

## What the handoff records

[`HANDOFF.md`](../../../HANDOFF.md) was written to make the project self-sufficient outside the original conversation. Its §4 is headed "Results that exist only in the chat (not in any artifact)" (the handoff sets "only" in capitals) and lists six items in compressed form: [the phase-space diameter relation](../../cosmology/scale-factor-duality/phase-space-diameter.md) (since written up in a note of its own), [the √N topological floor](../../dark-matter/candidates/soliton-candidate/sqrt-n-floor.md), the two items on this page, [momentum-space black holes](../../conjugate-relativity/momentum-space-black-holes.md), and the full adjudications of review rounds 1 and 2, which are on [review rounds 1 and 2](../../method/review/rounds-one-and-two.md).

The handoff gives each of the two items here as a single line of notes. Those lines are the whole record: the reasoning behind them stayed in the chat. The wiki quotes them verbatim and then sets each part beside what the documents do contain.

## Two gravitational charges

### The claim

[`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact), verbatim:

> "**Two gravitational charges:** ordinary stress-energy (sources massless graviton) vs dual stress 'how energy is structured across momentum' (sources X); independent numbers; equivalence principle intact; whether invariant length λ and dual charge lock together = 'dual equivalence principle' open question."

### Background: the charge of gravity [T]

In [general relativity](../spin-2-fields/general-relativity.md) the source of gravity is the stress-energy tensor T_μν, which records the density and flow of energy and momentum; for slow bodies it reduces to mass, the charge of Newtonian gravity [T]. The equivalence principle states that this gravitational charge equals the inertial mass, the resistance to acceleration, for every body, so that all bodies fall alike; general relativity builds it in by coupling all matter to the same metric g [T].

### What the documents contain

- **Dual stress as X's source.** Calc note [#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) [D — structural] defines the quantity that the chat calls the second charge: "Conjugate matter couples to H universally (P4); its coupling to the X-block is through the **dual stress** T̃ — moments involving momentum-derivatives of the χ bilinear." In that note, exchange of X between two such bilinears is the dark-matter gate ([dual stress T̃](../../dark-matter/conjugate-matter/dual-stress.md); [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md); not derived, according to flag 55, pending). Calc note [#8 §4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born) summarizes X as "coupled to conjugate matter through the dual stress (the gate) and to ordinary matter only at gravitational strength and short range".
- **Ordinary matter and X.** The chat line pairs ordinary stress-energy with the massless graviton. In the documented account ordinary matter also couples to X: Standard Model matter, coupled to g, "sees both eigenstates with comparable strength" ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)), and [#11](../../history/documents/checkpoint.md) [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) states its couplings to X as "gravitational-strength and Yukawa-cut at 1/M_X" ([safety by range](fifth-force-safety.md)). No document relates the chat's one-charge-per-field assignment to this.
- **[The equivalence principle](../spin-2-fields/equivalence-principle.md).** The documents keep it for both kinds of matter. Under postulate [P4](../../program/postulates/p4-polarized-matter.md) both "couple universally to H" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)); conjugate matter "propagates on g (equivalence principle; Bullet-Cluster-safe)" ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate); [the Bullet Cluster](../../dark-matter/halo-astrophysics/bullet-cluster.md)); and the paper on conjugate special relativity, [#13](../../conjugate-relativity/_index.md), lists in its §6 the massless graviton as shared by both polarizations, "so both polarizations fall identically". [#13 §5](../../papers/conjugate-special-relativity.md#5-inertia-dualized) adds a reading of its own: "the dual principle of relativity — equivalence of all force-free frames — is the equivalence principle" [D — structural] ([the equivalence principle as dual relativity](../../conjugate-relativity/equivalence-principle.md)). The chat's "equivalence principle intact" agrees with these, but the argument behind it, given two charges, is not written down.
- **The phrase "independent numbers".** No document says whether, or why, the dual charge of a body is independent of its mass-energy.

### The open question: a dual equivalence principle

The name is modelled on the ordinary equivalence principle, which locks a body's gravitational charge to its inertial mass. #13 supplies the quantity that plays the part of mass for conjugate quanta: "conjugate quanta are characterized by an irreducible extent λ_χ as ours are by mass" ([§4](../../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell), [D — structural]; [the invariant-length shell](../../conjugate-relativity/invariant-length-shell.md)), and "The dual second law, structurally, makes λ_χ the measure of resistance to force-*change*" ([§5](../../papers/conjugate-special-relativity.md#5-inertia-dualized), tagged "conjecture-tier" there; [dual inertia](../../conjugate-relativity/dual-inertia.md)). The chat's question is whether the dual charge is locked to λ in the same way. Neither the handoff nor any document goes further than posing it.

## The field equations compared with general relativity

### The claim

[`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact), verbatim (GR is general relativity):

> "**GR-vs-conjugate equation comparison:** slaved layer g̃ = g⁻¹ is algebraic (Einstein's equation does double duty); dual Newtonian limit = Yukawa in momentum = the gate; X-waves massive, 5 polarizations, frequency floor."

### The slaved layer is algebraic

Einstein's equation is a differential equation for the metric g. The momentum metric g̃ does not get one of its own: it is fixed point by point by g, so once Einstein's equation determines g, g̃ is determined too. That is the natural reading of "does double duty"; the handoff does not spell it out.

The documented counterpart is corollary 3 of [the compatibility theorem](../../phase-space/born-geometry/compatibility-theorem.md), in calc note [#5 §A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous) [D — rigorous]: "**The momentum metric is slaved: g̃ = g⁻¹ pointwise.** No independent momentum-space geometry survives." [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) lists "g̃ = g⁻¹ slaved" among the corollaries of the theorem, which it tags [T][V], the [V] being battery test T1 ([corollaries: unimodularity, no B-field, slaved momentum metric](../../phase-space/born-geometry/compatibility-corollaries.md); [the verification battery](../../method/verification/battery.md)). The theorem holds when the [neutral metric η](../../symmetry-breaking/order-parameter.md) is rigid. With η emergent, the independent part of momentum-space geometry is X = Re Z ([the modular field Z](../../phase-space/modular-field/modular-field-z.md); [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)), and [#13 §1](../../papers/conjugate-special-relativity.md#1-two-causal-cones) separates the two layers in the same way: "the dual cone is the causal structure of the *slaved* geometry g⁻¹; the independently dynamical part of momentum-space geometry is the massive field X". The phrase "Einstein's equation does double duty" appears in no document.

### The dual Newtonian limit and the gate

In general relativity the Newtonian limit is the regime of weak fields and slow sources, in which Einstein's equation reduces to Poisson's equation for a potential falling as 1/r [T]. The chat line asserts a counterpart on the momentum side: the corresponding limit gives a Yukawa form in momentum, and that form is [the velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md), the factor that switches conjugate matter's self-interaction off except between particles of nearly equal velocity.

The documented counterpart is the gate's mechanism, not its form. Calc note [#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) found that "Exchange of X between two such bilinears yields a four-point amplitude that depends on the **incoming relative momenta** of the pair", and [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) states the mechanism as "delivered by X-exchange between dual-stress bilinears" [D — mechanism; shape [O]]. That documented counterpart is itself disputed: [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate, and flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism ([the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). The shape is open: item 4 of [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems), Gaussian against rational ([Open: the gate shape](../../dark-matter/conjugate-matter/gate-shape.md)). No document derives a Yukawa form in momentum or describes the gate as a Newtonian limit.

The nearest documented statements are in #13, which says X "modifies the dual cone only at short range in momentum [D — [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) of the checkpoint]" (§1) and "dual-geometric effects are Yukawa-cut in momentum [D — [checkpoint §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)]" (§6) ([two causal cones](../../conjugate-relativity/two-causal-cones.md)). The checkpoint section it cites says "Yukawa-cut at 1/M_X", of the couplings of ordinary matter ([#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d)). The wiki follows #11's wording, and the reading in momentum remains chat-only ([conflicts between sources](../../history/documents/source-conflicts.md); see flag 29 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).

### Massive X waves: five polarizations and a frequency floor

Gravitational waves in general relativity are massless, travel at the speed of light and have two polarizations [T]. A massive spin-2 field has five, 2s + 1 for spin s = 2 [T]. Its waves obey the dispersion relation of a massive field, ω² = k² + M² in units where ℏ = c = 1, so no wave of the field oscillates with angular frequency below M: the frequency floor [T].

The documented part: calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) [D — structural] has X become "a **massive spin-2** with its five polarizations" ([the gravitational Higgs mechanism](gravitational-higgs.md)), and [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) [D + T] has it emerge "massive". The frequency floor appears in no document outside the handoff's line ([Open: field content of the broken vacuum](../../phase-space/modular-field/field-content.md) records the same). For X the floor would sit at its mass M_X, for which no document gives a value ([spectrum, parameters and reciprocity parity](spectrum-and-parity.md)); the phase-space-diameter note bounds it from below, M_X c² > 5.2 meV, in the program's aligned vacuum ([`wiki/papers/phase-space-diameter.md` §8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs); [the laboratory bound on X's range](range-bound.md)).

## What has a documented counterpart

| Part of the chat claims | Documented counterpart | Tag there |
| --- | --- | --- |
| Dual stress couples conjugate matter to X | [#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural); [#8 §4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born) | [D — structural] (#5) |
| Ordinary stress-energy sources the massless graviton | general relativity; [#7 §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural)'s "our graviton, coupling to SM stress" (SM: Standard Model). [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) adds that such matter also sees X | [T]; [D + T] (#8) |
| The two charges are independent numbers | none | — |
| The equivalence principle survives | [#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) (P4), [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate); [#13 §5](../../papers/conjugate-special-relativity.md#5-inertia-dualized), [§6](../../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) | [P]; [D — structural] ([#13 §5](../../papers/conjugate-special-relativity.md#5-inertia-dualized)) |
| A dual equivalence principle | none; posed as a question | — |
| The slaved layer g̃ = g⁻¹ | [#5 §A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous) corollary 3; [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) | [D — rigorous] (#5); the theorem [T][V] (#11) |
| Einstein's equation does double duty | none | — |
| The gate as a dual Newtonian limit | the gate as X exchange: [#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural); [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) | [D — mechanism; shape [O]] (#11); not derived according to flag 55, pending |
| Yukawa in momentum | [#13 §1](../../papers/conjugate-special-relativity.md#1-two-causal-cones), [§6](../../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open), citing [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton), which says "Yukawa-cut at 1/M_X" | [D — [checkpoint §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)] (#13) |
| X waves massive, with five polarizations | [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural); [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) | [D — structural] (#6); [D + T] (#11) |
| A frequency floor | none | — |

## Standing

Both items are conjectures in the wiki's sense: claims that no artifact derives. The handoff attaches no tier to either line, unlike the neighbouring diameter relation and momentum-space black holes, which it calls conjecture-tier. Neither item is queued for a write-up. The handoff's queue ([`HANDOFF.md` §8](../../../HANDOFF.md#8-ranked-next-actions-queue)) held two of the chat-only results: item 3, the "√N-floor freeze-out estimate", and item 7, an optional note on the phase-space diameter relation. The root [`CLAUDE.md`](../../../CLAUDE.md) ("Since the handoff") drops item 3 and records item 7 as done. The phase-space-diameter note ([`wiki/papers/phase-space-diameter.md`](../../papers/phase-space-diameter.md), round-5 verdict B) wrote the relation up, found it to be an identity of standard physics that cannot test the program, and withdrew its clause "square exactly at the bounce", which is under review ([the phase-space diameter relation](../../cosmology/scale-factor-duality/phase-space-diameter.md); [Under review: the square rectangle at the bounce](../../cosmology/scale-factor-duality/square-at-the-bounce.md)). No chat-only result is on the current queue, whose first item is the partially-massless comparison and the † literature battery.

## Sources

- [`HANDOFF.md` §4](../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — the only record of both results, verbatim; [§8](../../../HANDOFF.md#8-ranked-next-actions-queue) — the queue, whose chat-only entries are item 3 (the √N-floor estimate, since dropped) and item 7 (the diameter note, since done)
- [`wiki/papers/phase-space-diameter.md` §1](../../papers/phase-space-diameter.md#1-two-abstracts), [§6](../../papers/phase-space-diameter.md#6-where-the-rectangle-is-square), [§9](../../papers/phase-space-diameter.md#9-summary) — the diameter relation written up: an identity of standard physics, and "square exactly at the bounce" withdrawn; [§8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs) — the conditional lower bound on M_X
- [`review/round5-adjudication.md`](../../../review/round5-adjudication.md) 'Verdict' — verdict B on the diameter note
- [`notes/geometric-core.md` §A](../../../notes/geometric-core.md#a-the-compatibility-theorem-d--rigorous) — the slaved momentum metric (corollary 3); [§E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) — the dual stress and the gate as X exchange
- [`notes/x-classification.md` §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — massive X with five polarizations; [§4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — the gate from integrating out massive X
- [`notes/tuning-test.md` §4](../../../notes/tuning-test.md#4-the-picture-that-emerges-constrained-bimetric-gravity-d--structural) — the massless combination coupling to Standard Model stress
- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — ordinary matter sees both eigenstates; [§4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born) — X's couplings to conjugate and ordinary matter
- [`wiki/papers/broken-born-checkpoint-v2.md` §4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — P4; [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) — the slaved metric among the theorem's corollaries; [§6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — X = Re Z; [§7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — X massive; [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) — "Yukawa-cut at 1/M_X"; [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the gate mechanism; [§14 item 4](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the gate shape [O]
- [`wiki/papers/conjugate-special-relativity.md` §1](../../papers/conjugate-special-relativity.md#1-two-causal-cones), [§6](../../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) — the slaved dual cone and the reading "in momentum"; [§4](../../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) — the invariant length λ_χ; [§5](../../papers/conjugate-special-relativity.md#5-inertia-dualized) — λ_χ as resistance to force-change and the equivalence principle as dual relativity
- [`verify/battery.py`](../../../verify/battery.py) T1 — the machine check of the compatibility theorem
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the current queue; "square exactly at the bounce" under review
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 29 — #13's citation of [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) for X's effect being in momentum, which #11 does not state (pending)
- [`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate) and [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 55 — exchanging [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate; the proposed tags [P] for the gate and μ, [O] for the mechanism (pending)
