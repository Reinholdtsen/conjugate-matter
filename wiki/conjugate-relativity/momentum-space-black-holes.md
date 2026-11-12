---
title: "Momentum-space black holes (chat-only)"
weight: 120
status: conjecture
description: "Velocity traps and horizons as maximum-force surfaces, with dual Hawking quanta huge in position space; chat-only, and partly in the popular article."
sources:
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "popsci/universes-other-half.md 'A second speed of light'"
  - "wiki/papers/conjugate-special-relativity.md §1"
  - "wiki/papers/conjugate-special-relativity.md §2"
  - "wiki/papers/conjugate-special-relativity.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "CLAUDE.md 'Since the handoff'"
  - "wiki/papers/phase-space-diameter.md §8.1"
  - "wiki/papers/phase-space-diameter.md §9"
  - "verify/phase_space_diameter.py"
  - "review/wiki-build-flags.md item 56"
  - "notes/velocity-gated-gravity.md §2"
---

*Momentum-space black holes are a conjecture from the program's original claude.ai conversation. Read in the momentum description, the program's mirror description in which momentum plays the part of position, a black hole's horizon would be the surface at which hovering in place requires the [maximum force](maximum-force.md) of conjugate special relativity; and there may be mirror objects, regions trapped in momentum rather than in space, which the [handoff document](../history/documents/handoff.md) calls velocity traps. The handoff records the idea among the results that exist only in the chat, at conjecture tier, together with "dual Hawking quanta" that would be huge in position space. The [popular article #12](../history/documents/popular-articles.md) repeats part of it and adds that such a mirror object would look like compact dark matter. No document derives any of it, it appears in neither the [checkpoint #11](../history/documents/checkpoint.md) nor the paper on conjugate special relativity [#13](_index.md), and it is not one of the program's [dark-matter candidates](../dark-matter/candidates/_index.md). Its status is conjecture (chat-only).*

**Status:** Conjecture (chat-only), partly repeated in the popular article [#12](../../popsci/universes-other-half.md) — "Conjecture tier" in [`HANDOFF.md` §4](../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact), which is not a house tag — no derivation in any artifact, no `verify/` script, not on the work queue. Listed in [Conjectures: P.R.'s, the record's, chat-only and popsci-only claims](../status/conjectures.md).

## What the handoff records

The [handoff document](../history/documents/handoff.md) was written to make the project self-sufficient outside the original conversation. Its §4, "Results that exist only in the chat (not in any artifact)" (the handoff sets "only" in capitals), gives this item one line. Its parts, with the quoted words verbatim and the handoff's "dual description" written as the momentum description:

- "**Momentum-space black holes:** velocity traps";
- our horizon, read in the momentum description, is a "max-force surface (hovering at horizon requires F → c⁴/G)";
- "dual Hawking quanta are position-space-huge. Conjecture tier; partially in #12."

The line is the whole record: the reasoning behind it stayed in the chat. The handoff attaches its own tier, "Conjecture tier", which is not one of the program's tags ([provenance tags and citation marks](../method/provenance-tags.md)).

## Background [T]

### Horizons and hovering

In general relativity a black hole's event horizon bounds a region from which no signal, light included, can reach distant observers; for a non-rotating, uncharged black hole of mass M it lies at the Schwarzschild radius r_s = 2GM/c² [T] ([general relativity and the graviton](../gravity/spin-2-fields/general-relativity.md)). A body held at a fixed radius outside the horizon needs a force to stay there. Measured by the body itself, the acceleration it must sustain grows without bound as the horizon is approached; the force transmitted to it from far away, measured far away, stays finite [T]. The handoff does not say in which sense "hovering at horizon requires F → c⁴/G".

### Hawking radiation

Quantum theory assigns a black hole a temperature, inversely proportional to its mass, and the thermal emission at that temperature is Hawking radiation (S. W. Hawking, 1974–75†). The typical wavelength of the emitted quanta is set by the size of the horizon, which it exceeds by a numerical factor [T]. The handoff gives no reasoning for its statement that the dual quanta are "position-space-huge".

## The force in the conjecture

The force c⁴/G is the maximum force of [conjugate special relativity](_index.md), [#13](../papers/conjugate-special-relativity.md)'s c̃, the bound on |dp/dt| set by the momentum-space light cone, evaluated with the [Born length](../phase-space/reciprocity/born-length.md) equal to the [Planck length](../gravity/spin-2-fields/planck-units.md#the-born-length-at-the-planck-length) ([two causal cones](two-causal-cones.md); [the maximum force c̃ = c⁴/G](maximum-force.md)). The conjecture in the general-relativity literature is c⁴/4G (#13's reference [1]†), and #13 records the difference: "The factor of 4 is not fixed here [O]" ([§1](../papers/conjugate-special-relativity.md#1-two-causal-cones); [maximum force and maximal acceleration in the literature](maximum-force-conjectures.md)). The handoff's line uses #13's value.

#13 itself mentions black holes only as the arena where forces approach c̃. Its §1 plain-language passage puts the maximum force at "about 10⁴⁴ newtons, the scale black holes reach when they collide"; its technical text cites "a companion maximum luminosity c⁵/4G approached by binary black-hole mergers" [1†]; and its §2 says a comparable-mass merger "operates at F ~ c̃ by construction", where any dual-kinematic corrections "would be order unity [O — flagged, not derived]" ([force boosts and force composition](force-boosts.md)); [#13 §5](../papers/conjugate-special-relativity.md#5-inertia-dualized)'s identification of dual rest with free fall gives the opposite answer for freely falling holes (flag 56 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md), pending). #13 says nothing about horizons, trapped regions in momentum or Hawking radiation.

## The popular version

The popular article #12 ("A second speed of light") restates the horizon reading in prose:

> "Black holes then take on a second role. In the position description, a horizon bounds a region from which there is no spatial exit. In the momentum description, the same horizon is the surface where remaining stationary would require force beyond the limit. The framework also permits, though it has not yet constructed, the mirror-image object: a trapped region in momentum rather than position, from which no attainable force can extract a captive."

In the wiki's reading, the mirror object corresponds to the handoff's "velocity traps": a region bounded in momentum, as a black hole's interior is bounded in position. #12 says the framework "has not yet constructed" it. #12 does not mention the dual Hawking quanta. It presents the framework as if confirmed and is never a source for status ([the popular articles](../history/documents/popular-articles.md)).

## Popsci-only: the mirror object as compact dark matter

#12 continues the passage above with a claim that appears in no other document, the handoff included:

> "Such an object would be opaque in the momentum description and transparent in ours — undetectable by light, evident only through its gravity, and therefore indistinguishable, to our instruments, from compact dark matter."

The program's dark-matter candidates are the three in [#11 §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates): χ particles, the X-condensate and P.R.'s conjecture of conjugate monopoles localized in momentum ([dark-sector candidates](../dark-matter/candidates/_index.md); [the χ-particle candidate](../dark-matter/candidates/chi-particles.md); [the X-condensate](../dark-matter/candidates/x-condensate.md); [Conjecture: magnetic monopoles abundant in momentum space](../dark-matter/candidates/momentum-space-monopoles.md)). Momentum-space black holes are not among them, and no document estimates their abundance, their formation or their gravitational signatures.

## Standing

- No artifact derives any part of the conjecture, and no `verify/` script checks it.
- It is not on the work queue. The handoff's queue ([`HANDOFF.md` §8](../../HANDOFF.md#8-ranked-next-actions-queue)) held two chat-only results, an estimate for the withdrawn paper on monopole dark matter (item 3, dropped from the current queue) and an optional note on the phase-space diameter relation (item 7). The diameter note is done ([`wiki/papers/phase-space-diameter.md`](../papers/phase-space-diameter.md); root [`CLAUDE.md`](../../CLAUDE.md), 'Since the handoff'): it finds the relation to be standard physics that cannot test the program, and it withdraws the claim of a rectangle square "exactly at the bounce", which is under review ([the phase-space diameter relation](../cosmology/scale-factor-duality/phase-space-diameter.md); [Under review: the square rectangle at the bounce](../cosmology/scale-factor-duality/square-at-the-bounce.md)). The current queue holds no chat-only result.
- It depends on #13's maximum force, which no review round has examined and which #11 does not mention. The arithmetic of c⁴/G, 1.21 × 10⁴⁴ N, is computed by [`verify/phase_space_diameter.py`](../../verify/phase_space_diameter.py) ([diameter note §8.1](../papers/phase-space-diameter.md#81-not-the-born-length-of-the-dual-special-relativity-dv); [the phase-space-diameter script](../method/verification/phase-space-diameter-script.md)); the identification of the Born length with the Planck length that gives the value is untagged in #13 ([the maximum force c̃ = c⁴/G](maximum-force.md)).
- The other chat-only items of [`HANDOFF.md` §4](../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) are on their own pages; the nearest in subject is [two gravitational charges and the conjugate field equations (chat-only)](../gravity/momentum-graviton/chat-only-results.md).

## Sources

- [`HANDOFF.md` §4](../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — the only record of the conjecture, verbatim; [§8](../../HANDOFF.md#8-ranked-next-actions-queue) for the queue's chat-only items.
- [`popsci/universes-other-half.md`](../../popsci/universes-other-half.md) 'A second speed of light' — the horizon reading, the mirror object and the compact-dark-matter claim (not a status source).
- [`wiki/papers/conjugate-special-relativity.md` §1](../papers/conjugate-special-relativity.md#1-two-causal-cones) — the maximum force c̃ = c⁴/G, the literature's c⁴/4G and c⁵/4G, and the open factor of 4; [§2](../papers/conjugate-special-relativity.md#2-force-boosts) for black-hole mergers as the arena; [§7](../papers/conjugate-special-relativity.md#7-summary-of-tethers) for the open list.
- [`wiki/papers/broken-born-checkpoint-v2.md` §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — the three dark-matter candidates, the third as P.R.'s conjecture.
- [`CLAUDE.md`](../../CLAUDE.md) 'Since the handoff' — the current queue; the diameter note done; the square at the bounce under review.
- [`wiki/papers/phase-space-diameter.md` §8.1](../papers/phase-space-diameter.md#81-not-the-born-length-of-the-dual-special-relativity-dv) — c⁴/G = 1.21 × 10⁴⁴ N at λ = l_P [V]; [§9](../papers/phase-space-diameter.md#9-summary) — the diameter relation's status and the withdrawn square.
- [`verify/phase_space_diameter.py`](../../verify/phase_space_diameter.py) — the computation of c⁴/G.
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 56 — [#13 §2](../papers/conjugate-special-relativity.md#2-force-boosts) against [§5](../papers/conjugate-special-relativity.md#5-inertia-dualized) on gravitating pairs (low), pending; [`notes/velocity-gated-gravity.md` §2](../../notes/velocity-gated-gravity.md#2-between-ordinary-bodies-x-is-a-short-range-yukawa-term-not-a-velocity-gate) — the two answers for the Sun and Earth
