---
title: "The maximum force c̃ = c⁴/G"
weight: 40
status: alive
description: "c̃ = ℏc/λ² with the Born length set to the Planck length gives c⁴/G ≈ 1.2×10⁴⁴ N, four times the literature's c⁴/4G — a factor #13 leaves open."
sources:
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md Abstract"
  - "papers/conjugate-special-relativity.md §2"
  - "papers/conjugate-special-relativity.md §4"
  - "papers/conjugate-special-relativity.md §7"
  - "notes/broken-born-theory.md §2"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "popsci/angle-of-the-mirror.md 'Dividends and daydreams'"
  - "popsci/universes-other-half.md 'A second speed of light'"
---

*The maximum force is the invariant speed of the momentum-space light cone: since a rate of change of momentum is a force, the dual cone's speed limit is a largest possible force, c̃ = ℏc/λ², where λ is a length that the paper #13 calls the Born length. Setting the Born length equal to the Planck length gives c̃ = c⁴/G, about 1.2 × 10⁴⁴ newtons, which #13 describes as "the scale black holes reach when they collide". The general-relativity literature already contains a conjectured maximum force, c⁴/4G; #13's value is larger by a factor of 4, and the factor is open. The result is alive but unreviewed: no review round has examined it, no script checks the number, and the checkpoint #11 does not mention it.*

**Status:** Alive, unreviewed — the boxed value carries no tag (#13 §7 lists it under "Numerical anchors"), the identification of the Born length with the Planck length carries none either, and the factor of 4 is [O] — listed alive in `HANDOFF.md` §2 without a machine-check mark; absent from #11 v2.2; never through a blind review round; no `verify/` script reproduces 1.2 × 10⁴⁴ N ([the iron rule](/wiki/method/verification/iron-rule)).

## The result

#13 §1, boxed:

```text
c̃ = c⁴/G ≈ 1.2 × 10⁴⁴ N
```

The Abstract gives the same value: "a maximum force, c̃ = ℏc/λ², equal to c⁴/G ≈ 1.2 × 10⁴⁴ N at the Planck value of the Born length." c̃ is the invariant speed of the dual cone of [Two causal cones](/wiki/conjugate-relativity/two-causal-cones), the bound |dp/dt| ≤ c̃ on how fast any trajectory can move through momentum space. Since dp/dt is a force, c̃ plays for forces the part that the speed of light c plays for velocities ([Special relativity: the template](/wiki/conjugate-relativity/special-relativity)).

## The Born length

The formula c̃ = ℏc/λ² contains one free length. #13 §1: "λ is the Born length and ε = ℏ/λ its conjugate momentum scale", and c̃ = ε/(λ/c), one unit of momentum ε per light-crossing time λ/c. The term "Born length" occurs in no other document of the program. The pair of symbols does: #1 §2 writes the standard phase-space structures in units in which "a reference length λ and momentum ε = ℏ/λ are scaled out", without naming λ or fixing its value. A length of this kind is needed whenever position and momentum are placed in one geometry, since the two have different units; ℏ converts the length λ into the momentum ε. Born's own program aimed at a physics with a fundamental mass and a fundamental length on equal footing (#13 §4, citing [3]†, [4]†; [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell)).

## The Planck identification, step by step

#13 fixes λ in one sentence and gives the step no tag: "The only length the gravitational sector supplies is the Planck length, λ² = ℏG/c³, giving" the boxed value. The steps are:

1. **The bound.** c̃ = ℏc/λ² (#13 §1).
2. **The identification.** λ is set equal to the Planck length l_P, the length built from ℏ, G and c, so λ² = ℏG/c³ ([Maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)). #13 offers no argument for the step beyond the sentence quoted.
3. **The substitution.** Putting λ² = ℏG/c³ into ℏc/λ² cancels ℏ and leaves c⁴/G, the boxed form. The result contains only c and G. c⁴/G is the Planck energy divided by the Planck length, the quantity known as the Planck force [T].
4. **The number.** #13 gives c⁴/G ≈ 1.2 × 10⁴⁴ N. No `verify/` script computes it; the iron rule asks for executed code with printed output for every asserted number, and this one is still owed (#13 §7 lists it among the "Numerical anchors").

Because the Born length enters squared, the value of c̃ depends directly on the identification in step 2: a different length would give a different maximum force. #13 states no alternative.

## The reason offered

#13 §1 presents its contribution as an explanation rather than a new value: "The framework's contribution is a reason: a maximum force is the statement that nothing outruns light in the momentum polarization." The plain passage of §1 puts it as "If position and momentum are true equals, there must be a second limit of the same kind governing motion through momentum space." The limit is the speed of the second light cone, the cone of the momentum block g⁻¹ of the phase-space metric. #13 §1 adds that this cone is the causal structure of the slaved geometry, modified at short range by the massive field X ([Two causal cones](/wiki/conjugate-relativity/two-causal-cones#the-slaved-dual-cone-and-x)).

## Comparison with the literature

#13 §1 sets its value beside the general-relativity literature:

> "A maximum force c⁴/4G was conjectured within general relativity as the "maximum tension principle" [1†], with a companion maximum luminosity c⁵/4G approached by binary black-hole mergers; a maximal *acceleration* from a phase-space metric is older still [2†]."

Both values are numbers times c⁴/G, the one force that c and G can form ([Maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)); #13's number is 1 and the conjecture's is 1/4. #13 notes "the conjecture's contested status" in that literature [T]. The documents describe the match in three ways:

- #13 §1: "The factor of 4 is not fixed here [O]".
- `HANDOFF.md` §2: c̃ "matches Gibbons–Schiller maximum-force conjecture up to the factor 4".
- The popular articles: "General relativity already contains a conjectured maximum force of exactly that form" (#10, 'Dividends and daydreams'), and "A maximum force of exactly this form was conjectured within general relativity two decades ago" (#12, 'A second speed of light').

#13's [O] governs. The popular articles are never a source for a claim's status ([The popular articles (#10, #12)](/wiki/history/documents/popular-articles)).

## Open: the factor of 4

#13 leaves the factor of 4 between c⁴/G and c⁴/4G open [O] (§1) and puts "the factor 4" first among §7's open items. Nothing has been computed on it. #13 does not say what would fix the factor, and no other document takes it up: it is not among #11 §14's open problems, the current queue in `CLAUDE.md` or `HANDOFF.md` §8. The item is listed in [Open problems and the queue](/wiki/status/open-problems).

## Where forces approach c̃

#13's plain passage for §1 places the limit at "about 10⁴⁴ newtons, the scale black holes reach when they collide". §2 names comparable-mass black-hole mergers as the one natural process that "operates at F ~ c̃ by construction", and so the one arena where dual-kinematic corrections could be of order unity, flagged and not derived ([Force boosts and force composition](/wiki/conjugate-relativity/force-boosts)). Every other force in nature lies far below the limit, which #13 gives as the reason force looks exactly additive.

A conjecture from the original chat reads a black hole's horizon in the momentum description as a maximum-force surface: "hovering at horizon requires F → c⁴/G" (`HANDOFF.md` §4, conjecture tier; [Momentum-space black holes (chat-only)](/wiki/conjugate-relativity/momentum-space-black-holes)).

## Planck closure

#13 §4 multiplies the maximum force by a length: "The dual rest-energy relation is E = λ c̃ (length × maximum force). At λ = l_P: E = l_P · c⁴/G = √(ℏc⁵/G) — the Planck energy, exactly [D]." It is the dual counterpart of E = mc² and the second of #13's numerical anchors ([The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell)).

## Standing

`HANDOFF.md` §2 lists "Maximum force c̃ = c⁴/G as the momentum-space light speed (matches Gibbons–Schiller maximum-force conjecture up to the factor 4)" among the alive results, without the ✓ that marks a machine-checked item. #11 v2.2 mentions neither the maximum force nor #13's dual kinematics, and no blind review round has examined #13. The value is therefore alive and unreviewed, and its number is unscripted ([Conjugate special relativity](/wiki/conjugate-relativity)).

## Sources

- `papers/conjugate-special-relativity.md` §1 — the Born length, the Planck identification, the boxed value, the reason, the literature and the open factor of 4; Abstract for "at the Planck value of the Born length"; §2 for the merger arena; §4 for Planck closure; §7 for the numerical anchors and the open list.
- `notes/broken-born-theory.md` §2 — the reference length λ and momentum ε = ℏ/λ.
- `HANDOFF.md` §2 — the alive listing, "up to the factor 4"; §4 for the chat-only horizon reading.
- `popsci/angle-of-the-mirror.md` 'Dividends and daydreams' and `popsci/universes-other-half.md` 'A second speed of light' — "of exactly that form" and "of exactly this form" (not a status source).
