---
title: "Maximum force and maximal acceleration in the literature"
weight: 20
status: established
description: "Gibbons and Schiller's conjectured maximum force c⁴/4G with its luminosity companion c⁵/4G, Caianiello's maximal acceleration from a phase-space metric, and the Planck length and energy that #13 uses."
provenance: [T]
sources:
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §7"
  - "papers/conjugate-special-relativity.md References [1]–[2]"
  - "papers/conjugate-special-relativity.md §4"
  - "HANDOFF.md §2"
  - "HANDOFF.md §8 item 6"
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §14 item 10"
---

*The maximum-force conjecture is a proposal within [general relativity](/wiki/gravity/spin-2-fields/general-relativity) that no force can exceed c⁴/4G, a combination of the speed of light c and Newton's constant G; Gibbons named it the maximum tension principle, and Schiller took a principle of maximum force as the starting point for deriving general relativity. An older and separate proposal, Caianiello's, is a maximal acceleration obtained from a metric on [phase space](/wiki/phase-space). Both are proposals rather than settled results, and #13, the program's paper on [conjugate special relativity](/wiki/conjugate-relativity), notes that the maximum-force conjecture is contested. They matter to the program because #13's maximum force, c̃ = c⁴/G, has the same form up to a factor of 4, and #13 offers a reason for such a limit. This page covers the literature; the Planck units it is written in are on [their own page](/wiki/gravity/spin-2-fields/planck-units), and #13's own claim is on [the maximum force page](/wiki/conjugate-relativity/maximum-force).*

**Status:** Established as literature: the proposals are published, not settled, and the maximum-force conjecture is contested — [T], with both citations marked † (from model memory, not yet checked against the papers) — #13 notes the maximum-force conjecture's contested status [T] without citing the dispute; the † references wait on [the literature battery](/wiki/method/literature-battery). #13's use of the conjecture is its own, unreviewed and not machine-checked, and [#11](/wiki/history/documents/checkpoint) v2.2 does not mention it.

## Why c⁴/G is a force [T]

The speed of light c and Newton's constant G can be combined into exactly one quantity with the dimensions of a force, c⁴/G, and exactly one with the dimensions of a power, c⁵/G [T]. A bound on force built from classical gravity alone is therefore a pure number times c⁴/G, and a bound on luminosity a pure number times c⁵/G; the proposals in the literature, and #13's, differ in that number. Planck's constant ℏ does not enter either combination, so a limit of this kind is a statement about classical gravity.

## The maximum tension principle [1†]

#13 §1 introduces the literature in one sentence: "A maximum force c⁴/4G was conjectured within general relativity as the "maximum tension principle" [1†], with a companion maximum luminosity c⁵/4G approached by binary black-hole mergers". Reference [1]† gives two papers:

- G. W. Gibbons, "The maximum tension principle in general relativity," Found. Phys. 32, 1891 (2002), hep-th/0210109;
- C. Schiller, "General relativity and cosmology derived from principle of maximum force," Int. J. Theor. Phys. 44, 1629 (2005).

As the two titles say, Gibbons stated the bound as a principle within general relativity, a limit on the tension or force that general relativity allows, and Schiller reversed the direction, taking a maximum force as the postulate from which general relativity and cosmology are to be derived [T]. The companion bound c⁵/4G is a limit on power, the luminosity of any source; #13 describes it as "approached by binary black-hole mergers", that is, by the power two black holes radiate in gravitational waves in their final orbits and merger. The same mergers are the one natural process #13 places near its own limit ([Force boosts and force composition](/wiki/conjugate-relativity/force-boosts)).

**Contested.** #13 §1 notes "the conjecture's contested status" in the general-relativity literature and tags the remark [T]. It cites no paper on either side of the dispute, and the wiki adds none. The conjecture is therefore recorded here as a proposal, not as a result of general relativity.

## Maximal acceleration [2†]

#13 §1 adds that "a maximal *acceleration* from a phase-space metric is older still [2†]". Reference [2]†: E. R. Caianiello, "Is there a maximal acceleration?" Lett. Nuovo Cim. 32, 65 (1981).

As usually summarized (†, from model memory; #13 states none of it), Caianiello joined a particle's velocities (for a particle of given mass, equivalently its momenta) to its spacetime coordinates and gave the combined space a single line element, so that position and velocity enter one geometry, as Born's reciprocity puts position and momentum into one phase space ([Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)). Requiring that line element to remain real bounds the particle's proper acceleration, in the way the Minkowski interval bounds speed ([Special relativity: the template](/wiki/conjugate-relativity/special-relativity)). The bound so obtained involves ℏ and depends on the particle's mass; it is not a single universal force. #13 does not state how its maximum force relates to Caianiello's acceleration.

## Planck units [T]

The Planck length l_P = √(ℏG/c³) and the Planck energy E_Planck = √(ℏc⁵/G) are built from ℏ, c and G; their ratio is c⁴/G, the Planck force, which contains no ℏ, as the section above requires of any force built from c and G [T]. #13 sets its Born length equal to the Planck length, written λ² = ℏG/c³, which turns c̃ = ℏc/λ² into c⁴/G (§1; [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force)), and obtains the Planck energy as "E = l_P · c⁴/G = √(ℏc⁵/G)" (§4; [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell)). The units, the Planck mass and its two conventions are on [Planck units and the two Planck masses](/wiki/gravity/spin-2-fields/planck-units).

## What #13 takes from this literature

- **The form of the limit.** #13's value c̃ = c⁴/G has the same form as the conjecture's c⁴/4G and is larger by a factor of 4. #13 §1: "The factor of 4 is not fixed here [O]"; §7 lists "the factor 4" among its open items. `HANDOFF.md` §2 says c̃ "matches Gibbons–Schiller maximum-force conjecture up to the factor 4".
- **A reason for the limit.** #13 §1: "The framework's contribution is a reason: a maximum force is the statement that nothing outruns light in the momentum polarization." In #13 the limit is the invariant speed of a second light cone, the one of momentum space ([Two causal cones](/wiki/conjugate-relativity/two-causal-cones)).
- **Literature tethers.** #13 §7 lists "maximum-tension conjecture [1†], maximal acceleration [2†], Born's self-dual program [3†, 4†]" as the work it ties itself to.

These uses are #13's claims, not results of the literature. #13 was never put through a [blind review](/wiki/method/review) round, no `verify/` script checks its numbers, and #11 v2.2 mentions neither the maximum force nor the conjecture.

## Verification still to do

All four of #13's references are marked †: cited from model memory and to be checked against the sources before any external use. `HANDOFF.md` §8 item 6 asks for "every † reference in #11 and #13 source-checked"; in `CLAUDE.md`'s current queue the † literature battery is part of item 1. #11 §14 item 10 (OP10) carries the same task for #11's own references, "Literature battery completion; every † reference source-checked [O]" ([Open: the † literature battery (OP10)](/wiki/method/literature-battery)). #13's [3]† and [4]† (Born, 1938 and 1949) are #11's [1]† and [2]†; [1] and [2], the two references on this page, appear in no other document's reference list; `HANDOFF.md` §2 names the "Gibbons–Schiller maximum-force conjecture" without a citation.

## Used by

- [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force) — #13's value, c⁴/G, set against the conjecture's c⁴/4G.
- [Force boosts and force composition](/wiki/conjugate-relativity/force-boosts) — black-hole mergers, which approach the companion luminosity, as the one arena near the limit.
- [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell) — the Planck energy as the Planck length times c⁴/G.
- [Momentum-space black holes (chat-only)](/wiki/conjugate-relativity/momentum-space-black-holes) — a horizon read as a maximum-force surface.
- [Open: the † literature battery (OP10)](/wiki/method/literature-battery) — the source check of references [1]† and [2]†, not yet done.

## Sources

- `papers/conjugate-special-relativity.md` §1 — the conjectures as #13 cites them, their contested status [T] and #13's reason; §7 for the literature tethers and the open factor 4; References [1]†–[2]† for the citations.
- `papers/conjugate-special-relativity.md` §4 — the Planck energy as l_P · c⁴/G.
- `HANDOFF.md` §2 — "up to the factor 4"; §8 item 6 for the literature battery.
- `CLAUDE.md` 'Since the handoff' — the battery as part of item 1 of the current queue.
- `papers/broken-born-checkpoint-v2.md` §14 item 10 — the battery for #11's references (OP10).
