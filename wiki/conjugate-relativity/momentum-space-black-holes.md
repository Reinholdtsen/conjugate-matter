---
title: "Momentum-space black holes (chat-only)"
weight: 120
status: conjecture
description: "Velocity traps and horizons as maximum-force surfaces, with dual Hawking quanta huge in position space; chat-only, and partly in the popular article."
sources:
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "popsci/universes-other-half.md 'A second speed of light'"
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §2"
  - "papers/conjugate-special-relativity.md §7"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "CLAUDE.md 'Since the handoff'"
---

*Momentum-space black holes are a conjecture from the program's original claude.ai conversation. Read in the momentum description, the program's mirror description in which momentum plays the part of position, a black hole's horizon would be the surface at which hovering in place requires the [maximum force](/wiki/conjugate-relativity/maximum-force) of conjugate special relativity; and there may be mirror objects, regions trapped in momentum rather than in space, which the [handoff document](/wiki/history/documents/handoff) calls velocity traps. The handoff records the idea among the results that exist only in the chat, at conjecture tier, together with "dual Hawking quanta" that would be huge in position space. The [popular article #12](/wiki/history/documents/popular-articles) repeats part of it and adds that such a mirror object would look like compact dark matter. No document derives any of it, it appears in neither the [checkpoint #11](/wiki/history/documents/checkpoint) nor the paper on conjugate special relativity [#13](/wiki/conjugate-relativity), and it is not one of the program's [dark-matter candidates](/wiki/dark-matter/candidates). Its status is conjecture (chat-only).*

**Status:** Conjecture (chat-only), partly repeated in the popular article #12 — "Conjecture tier" in `HANDOFF.md` §4, which is not a house tag — no derivation in any artifact, no `verify/` script, not on the work queue. Listed in [Conjectures: chat-only and popsci-only claims](/wiki/status/conjectures).

## What the handoff records

The [handoff document](/wiki/history/documents/handoff) was written to make the project self-sufficient outside the original conversation. Its §4, "Results that exist only in the chat (not in any artifact)" (the handoff sets "only" in capitals), gives this item one line. Its parts, with the quoted words verbatim and the handoff's "dual ledger" rendered as the momentum description:

- "**Momentum-space black holes:** velocity traps";
- our horizon, read in the momentum description, is a "max-force surface (hovering at horizon requires F → c⁴/G)";
- "dual Hawking quanta are position-space-huge. Conjecture tier; partially in #12."

The line is the whole record: the reasoning behind it stayed in the chat. The handoff attaches its own tier, "Conjecture tier", which is not one of the program's tags ([provenance tags and citation marks](/wiki/method/provenance-tags)).

## Background [T]

### Horizons and hovering

In general relativity a black hole's event horizon bounds a region from which no signal, light included, can reach distant observers; for a non-rotating, uncharged black hole of mass M it lies at the Schwarzschild radius r_s = 2GM/c² [T] ([general relativity and the graviton](/wiki/gravity/spin-2-fields/general-relativity)). A body held at a fixed radius outside the horizon needs a force to stay there. Measured by the body itself, the acceleration it must sustain grows without bound as the horizon is approached; the force transmitted to it from far away, measured far away, stays finite [T]. The handoff does not say in which sense "hovering at horizon requires F → c⁴/G".

### Hawking radiation

Quantum theory assigns a black hole a temperature, inversely proportional to its mass, and the thermal emission at that temperature is Hawking radiation (S. W. Hawking, 1974–75†). The typical wavelength of the emitted quanta is set by the size of the horizon, which it exceeds by a numerical factor [T]. The handoff gives no reasoning for its statement that the dual quanta are "position-space-huge".

## The force in the conjecture

The force c⁴/G is the maximum force of [conjugate special relativity](/wiki/conjugate-relativity), #13's c̃, the bound on |dp/dt| set by the momentum-space light cone, evaluated with the Born length equal to the Planck length ([two causal cones](/wiki/conjugate-relativity/two-causal-cones); [the maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force)). The conjecture in the general-relativity literature is c⁴/4G (#13's reference [1]†), and #13 records the difference: "The factor of 4 is not fixed here [O]" (§1; [maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)). The handoff's line uses #13's value.

#13 itself mentions black holes only as the arena where forces approach c̃. Its §1 plain-language passage puts the maximum force at "about 10⁴⁴ newtons, the scale black holes reach when they collide"; its technical text cites "a companion maximum luminosity c⁵/4G approached by binary black-hole mergers" [1†]; and its §2 says a comparable-mass merger "operates at F ~ c̃ by construction", where any dual-kinematic corrections "would be order unity [O — flagged, not derived]" ([force boosts and force composition](/wiki/conjugate-relativity/force-boosts)). #13 says nothing about horizons, trapped regions in momentum or Hawking radiation.

## The popular version

The popular article #12 ("A second speed of light") restates the horizon reading in prose:

> "Black holes then take on a second role. In the position description, a horizon bounds a region from which there is no spatial exit. In the momentum description, the same horizon is the surface where remaining stationary would require force beyond the limit. The framework also permits, though it has not yet constructed, the mirror-image object: a trapped region in momentum rather than position, from which no attainable force can extract a captive."

In the wiki's reading, the mirror object corresponds to the handoff's "velocity traps": a region bounded in momentum, as a black hole's interior is bounded in position. #12 says the framework "has not yet constructed" it. #12 does not mention the dual Hawking quanta. It presents the framework as if confirmed and is never a source for status ([the popular articles](/wiki/history/documents/popular-articles)).

## Popsci-only: the mirror object as compact dark matter

#12 continues the passage above with a claim that appears in no other document, the handoff included:

> "Such an object would be opaque in the momentum description and transparent in ours — undetectable by light, evident only through its gravity, and therefore indistinguishable, to our instruments, from compact dark matter."

The program's dark-matter candidates are the two in #11 §12, χ particles and the X-condensate ([dark-sector candidates](/wiki/dark-matter/candidates); [the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles); [the X-condensate](/wiki/dark-matter/candidates/x-condensate)). Momentum-space black holes are not among them, and no document estimates their abundance, their formation or their gravitational signatures.

## Standing

- No artifact derives any part of the conjecture, and no `verify/` script checks it.
- It is not on the work queue. The handoff's queue (`HANDOFF.md` §8) held two chat-only results, the √N-floor estimate (item 3, since dropped) and an optional note on the phase-space diameter relation (item 7); the root `CLAUDE.md` ('Since the handoff') keeps only the diameter note ([the phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter)).
- It depends on #13's maximum force, which is itself unreviewed and unchecked by script, and which #11 v2.2 does not mention.
- The other chat-only items of `HANDOFF.md` §4 are on their own pages; the nearest in subject is [two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results).

## Sources

- `HANDOFF.md` §4 — the only record of the conjecture, verbatim; §8 for the queue's chat-only items.
- `popsci/universes-other-half.md` 'A second speed of light' — the horizon reading, the mirror object and the compact-dark-matter claim (not a status source).
- `papers/conjugate-special-relativity.md` §1 — the maximum force c̃ = c⁴/G, the literature's c⁴/4G and c⁵/4G, and the open factor of 4; §2 for black-hole mergers as the arena; §7 for the open list.
- `papers/broken-born-checkpoint-v2.md` §12 — the two dark-matter candidates.
- `CLAUDE.md` 'Since the handoff' — the current queue.
