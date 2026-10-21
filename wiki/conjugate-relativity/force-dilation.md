---
title: "Force dilation"
weight: 60
status: alive
description: "dτ̃ = dt√(1 − F²/c̃²): sustained force dilates the internal evolution of conjugate-polarized systems and contracts a forced system's momentum spread; which clocks respond is open."
provenance: [D, O]
sources:
  - "papers/conjugate-special-relativity.md §3"
  - "papers/conjugate-special-relativity.md §2"
  - "papers/conjugate-special-relativity.md §7"
  - "papers/conjugate-special-relativity.md Abstract"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "HANDOFF.md §2"
  - "popsci/universes-other-half.md 'A second speed of light'"
---

*Force dilation is the momentum-space counterpart of time dilation. In [special relativity](/wiki/conjugate-relativity/special-relativity) a fast-moving clock runs slow; in the dual kinematics of [#13](/wiki/conjugate-relativity), a system under a large sustained force evolves slowly, by the same square-root formula with force in place of velocity and the [maximum force c̃](/wiki/conjugate-relativity/maximum-force) in place of the speed of light. Its mirror is a contraction of the range of momenta a forced system spans, in place of the contraction of its length. #13 restricts the effect to systems of the conjugate (momentum) [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations), leaves open which physical clocks respond, and states that both effects are unmeasurably small below the forces of black-hole mergers. The result is alive but unreviewed: #13 tags it as derived, but no review round or script has checked it, and the [checkpoint #11](/wiki/history/documents/checkpoint) does not mention it.*

**Status:** Alive, unreviewed — [D — structural; which physical clocks respond is polarization-dependent, O], as #13 §3 tags it; force dilation is on #13 §7's fixed [D] list, the contraction of momentum spread is untagged — no blind review round has examined #13, no `verify/` script checks the formula or the sizes quoted, and #11 v2.2 does not mention it. The clock-response question is open and is missing from #13 §7's open list.

## The dual proper time

#13 §3: "The dual proper time of a trajectory p(t) is"

```text
dτ̃ = dt √(1 − (1/c̃²)|dp/dt|²) = dt √(1 − F²/c̃²)
```

The template is the proper time of [special relativity](/wiki/conjugate-relativity/special-relativity), dτ = dt√(1 − v²/c²), the time read by a clock that moves at speed v = |dx/dt| [T]. The transcription replaces the velocity dx/dt by the rate of change of momentum dp/dt, which is the force F, and c by c̃ ([The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force)). The formula has the form of the dual interval along the trajectory divided by c̃, dτ̃ = ds̃/c̃ with ds̃² = c̃²dt² − dp² ([Force boosts and force composition](/wiki/conjugate-relativity/force-boosts)), as the template's proper time is ds/c; #13 writes the result without that intermediate step.

Read as #13 reads it, a system under a constant force F advances its dual proper time more slowly than the coordinate time t, by the dual Lorentz factor: dτ̃ = dt/γ̃ with γ̃ = (1 − F²/c̃²)^{−1/2}. The slowing depends only on the size of the force, |dp/dt|, and not on how the force changes, as time dilation in the template depends on speed and not on acceleration [T]. At F = 0 the two times agree; as F approaches c̃ the dual proper time stops advancing. The plain passage of §3 puts it as "hard-pushed clocks run slow — a system under enormous force ages more slowly than an unforced one, by the same square-root formula with force replacing velocity."

## What it dilates: conjugate-polarized systems

The technical statement is narrower than the plain passage. #13 §3:

> "so sustained force dilates the internal evolution of (conjugate-polarized) systems as sustained velocity dilates ours [D — structural; which physical clocks respond is polarization-dependent, O]."

The parenthesis restricts the effect to matter of the other polarization. Postulate [P4](/wiki/program/postulates/p4-polarized-matter) sorts matter into two kinds: "Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H; gauge forces do not cross polarizations" [P] (#11 §4). Ordinary matter is x-polarized, and its clocks are slowed by velocity in the usual way. #13's claim is that p-polarized systems, the program's [conjugate matter](/wiki/dark-matter/conjugate-matter), are slowed by sustained force in the same way. The Abstract's shorter phrase is "force-dilation of clocks", and §7 lists "force dilation" among its fixed [D] results without the qualifier.

## Open: which clocks respond

The second half of #13 §3's tag is open: "which physical clocks respond is polarization-dependent, O". #13 does not say which physical systems would show force dilation, whether any x-polarized system would, or how the dependence on polarization would be decided. Nothing has been computed. The question is absent from the lists that would schedule it: #13 §7's own open list ("the factor 4; the 4D covariant construction; dual dynamics; whether merger-band gravitational-wave data can bound dual-kinematic corrections"), #11 §14's open problems, and the current queue in `CLAUDE.md`. The program's other open items are collected in [Open problems and the queue](/wiki/status/open-problems).

## The mirror: contraction of momentum spread

#13 §3, untagged:

> "The mirror of length contraction: a forced system's extent *in momentum* — its momentum spread — contracts by γ̃ in the force direction."

In the template, a rod moving at velocity v is shorter along its motion by the factor γ than in its own rest frame, and its transverse size is unchanged [T]. The transcription replaces the rod's extent in position by a system's extent in momentum, the range of momenta it spans, and the velocity by the force: a system under the force F has its momentum spread along F reduced by the factor γ̃. The claim is not on §7's fixed list and carries no tag of its own. #13 states it in one sentence and does not discuss how a momentum spread would be measured.

## Size of the effects

#13 §3 closes: "Both effects are unmeasurably small below merger-scale forces (§2)." The factor that governs both is γ̃ − 1 ≈ ½(F/c̃)², and §2 evaluates it for "the strongest sustained macroscopic force in nature — on a kilogram at a neutron-star surface, ~10¹² N", giving "~ 10⁻⁶⁵" ([Force boosts and force composition](/wiki/conjugate-relativity/force-boosts#the-galilean-limit-why-force-looks-additive)). The plain passage of §3 states the threshold as "Below 10⁴³ newtons the effect is utterly negligible, which is why nobody has noticed." Only comparable-mass black-hole mergers, which #13 places at F ~ c̃, would bring the factor near 1 ([Open: merger-band corrections](/wiki/conjugate-relativity/force-boosts#open-merger-band-corrections)). No `verify/` script reproduces any of these figures ([the iron rule](/wiki/method/verification/iron-rule)).

## Popsci-only: the unqualified popular statement

The popular article #12 ('A second speed of light') says "Clocks subjected to sustained force run slow, by the same square-root formula that governs fast clocks, with force in place of velocity." It drops both the restriction to conjugate-polarized systems and the open question of which clocks respond, and so states more than #13 does. #13 governs; #12 presents the framework as if it were confirmed and is never a source for status ([The popular articles (#10, #12)](/wiki/history/documents/popular-articles)).

## Standing

`HANDOFF.md` §2 lists "force dilation" under dual special relativity among the alive results, without a machine-check mark. #13 tags the dual proper time [D — structural] and lists force dilation among its fixed results, but no blind review round has examined #13, no `verify/` script checks the formula or the numbers, and #11 v2.2 does not mention force dilation. The result is alive and unreviewed, and its physical scope, which clocks respond, is open ([Conjugate special relativity](/wiki/conjugate-relativity)).

## Sources

- `papers/conjugate-special-relativity.md` §3 — the dual proper time, its scope and open clock question, momentum-spread contraction, the size of both effects; §2 for the neutron-star estimate and the merger arena; §7 for the fixed and open lists; Abstract for "force-dilation of clocks".
- `papers/broken-born-checkpoint-v2.md` §4 — postulate P4, the two polarizations of matter.
- `HANDOFF.md` §2 — the alive listing.
- `popsci/universes-other-half.md` 'A second speed of light' — the unqualified popular statement (not a status source).
