---
title: "Open: the four-dimensional Born map and dual dynamics"
weight: 110
status: open
description: "The fully covariant construction that swaps time and energy, the natural home of #13's kinematics and a prerequisite for writing the dual field equations."
provenance: [O]
sources:
  - "wiki/papers/conjugate-special-relativity.md §6"
  - "wiki/papers/conjugate-special-relativity.md §7"
  - "wiki/papers/conjugate-special-relativity.md §1"
  - "wiki/papers/conjugate-special-relativity.md §2"
  - "wiki/papers/conjugate-special-relativity.md §3"
  - "wiki/papers/conjugate-special-relativity.md §4"
  - "wiki/papers/conjugate-special-relativity.md §5"
  - "review/v3-worklog.md 'New open items'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §14"
  - "CLAUDE.md 'Since the handoff'"
---

*The four-dimensional Born map is the version of [Born's reciprocity transformation](../phase-space/reciprocity/born-reciprocity.md) that exchanges time with energy as well as position with momentum. [#13](_index.md), the paper on the special relativity of the [momentum polarization](../phase-space/reciprocity/lagrangian-polarizations.md), names it as the fully covariant construction in which its kinematics belongs, and it has not been built. [#13](../papers/conjugate-special-relativity.md) itself works in a 3+1 presentation, in which space and momentum trade places while time is shared by both polarizations. The map is also a prerequisite for the dual dynamics, the field equations of the momentum polarization ("their Maxwell, their field theory"), which do not exist: only the dual kinematics has been written, and the [dual second law](dual-inertia.md#conjecture-the-dual-second-law) that #13 sketches is marked conjecture-tier until it is. Both items are open in [#13 §7](../papers/conjugate-special-relativity.md#7-summary-of-tethers), and neither is on the [checkpoint #11](../history/documents/checkpoint.md)'s [list of open problems](../status/open-problems.md) or on the current queue.*

**Status:** Open — [O] — [#13 §6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) and [§7](../papers/conjugate-special-relativity.md#7-summary-of-tethers); nothing computed, no `verify/` script; not in [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems) or the current queue in [`CLAUDE.md`](../../CLAUDE.md). #13 is unreviewed and not mentioned in [#11](../history/documents/checkpoint.md). Listed in [Open problems and the queue](../status/open-problems.md).

## The open items

[#13 §6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) ends its account of what the two polarizations share with what is missing:

> "Open [O]: the fully covariant construction with the four-dimensional Born map (t ↔ E), in which the dual "time" direction is our energy axis — the natural home of this paper's kinematics and a required step before the dual dynamics (their Maxwell, their field theory) can be written."

[#13 §7](../papers/conjugate-special-relativity.md#7-summary-of-tethers)'s list of open items repeats both: "the 4D covariant construction; dual dynamics". Two items are named, and the first is a prerequisite for the second.

## Background: time, energy and the 3+1 split [T]

- **Four-vectors.** Special relativity combines time and space into the four-vector x^μ = (ct, **x**), and energy and momentum into p^μ = (E/c, **p**). Lorentz boosts mix the time component with the space components, and the energy component with the momentum components ([special relativity: the template](special-relativity.md)).
- **Two conjugate pairs.** In quantum mechanics momentum generates translations in space, and energy generates translations in time. Both pairs are related by Fourier transformation: a wave packet's extent and its momentum spread are reciprocal, as a pulse's duration and its frequency bandwidth are, with E = ℏω ([the Fourier transform](../phase-space/reciprocity/fourier-transform.md)).
- **The 3+1 split.** Phase space, the arena of Hamiltonian mechanics, has position and momentum as its coordinates; time is not one of them but the parameter along which states evolve. A formulation that singles out time this way is a 3+1 split: three dimensions of space and one of time, treated differently.

[Born reciprocity ρ](../phase-space/reciprocity/born-reciprocity.md), the exchange (x, p) → (p, −x), acts on phase space. Applied to spatial position and momentum only, it leaves time alone; extended to four-vectors, it would exchange the time component with the energy component as well. That extension, t ↔ E, is the map of the open item.

## What #13 uses instead: the 3+1 presentation

[#13 §6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open)'s plain-language passage states the choice: "the tidiest version of this construction treats space and momentum as partners while leaving time alone; the fully four-dimensional version, in which energy and time also trade places, is deeper and not yet built." Its technical text calls the shared time a structure common to both polarizations: "Shared: the time coordinate (in the 3+1 presentation used here)".

The kinematics of [#13's §1](../papers/conjugate-special-relativity.md#1-two-causal-cones)–[§3](../papers/conjugate-special-relativity.md#3-force-dilation-and-its-mirror) and [§5](../papers/conjugate-special-relativity.md#5-inertia-dualized) is written in that presentation. Each result takes derivatives with respect to the shared t:

- the dual cone |dp/dt| ≤ c̃ of §1 ([two causal cones](two-causal-cones.md));
- the dual interval ds̃² = c̃²dt² − d**p**² on (t, **p**) and the force boosts of §2 ([force boosts and force composition](force-boosts.md));
- the dual proper time dτ̃ = dt√(1 − F²/c̃²) of §3 ([force dilation](force-dilation.md));
- the dual-inertial condition dp/dt = 0 of §5 ([dual inertia: free fall as rest](dual-inertia.md)).

#13 does not work out what these results become under the four-dimensional map. It says only that, there, "the dual "time" direction is our energy axis".

## Where #13 already reaches for it

[#13 §6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open)'s photon-dispersion argument treats light's relation E = c|p| as "the dual null cone". The v3 worklog (item O3) places that cone in this construction: it "belongs to the 4D Born map (t ↔ E): a cone in (E, p) with slope c. Under the 4D map, anything on our light cone is automatically dual-null." [#13 §1](../papers/conjugate-special-relativity.md#1-two-causal-cones) uses a different cone, in (t, p) with slope c̃, and the worklog asks to settle which construction governs ([Open: the two dual cones](two-cones-inconsistency.md)).

[#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell)'s invariant-length shell, x_μx^μ = λ_χ², is written with four-vectors, as the mass shell it mirrors is; #13 does not say which construction it belongs to ([the invariant-length shell](invariant-length-shell.md)).

## Dual dynamics

### What is missing

#13 is a paper on kinematics: cones, boosts, proper time and invariants. Its "dual dynamics (their Maxwell, their field theory)" are the field equations that would govern the momentum polarization in that kinematics, its counterparts of Maxwell's equations and of field theory in general. #13 does not define the term further, and no document writes such equations.

### What waits on it

- **The dual laws of motion.** [#13 §5](../papers/conjugate-special-relativity.md#5-inertia-dualized): "The dual second law, structurally, makes λ_χ the measure of resistance to force-*change* [conjecture-tier; the full dual dynamics awaits the formalization of §6]" ([dual inertia: the dual second law](dual-inertia.md#conjecture-the-dual-second-law)).
- **The dark photon.** The worklog's item O3 assigns one question to this item:

  > Whether the dark photon is m = 0, λ = 0, or both is part of #13's open "dual dynamics" item.

  In ordinary kinematics a massless photon has m = 0; in #13's dual kinematics a quantum is labelled by an invariant length λ, and the two readings make different quanta dual-null ([Open: the two dual cones](two-cones-inconsistency.md)).

[#13 §7](../papers/conjugate-special-relativity.md#7-summary-of-tethers)'s open list has two further items, which it does not tie to the dual dynamics: "the factor 4" of the maximum force ([the maximum force c̃ = c⁴/G](maximum-force.md)) and "whether merger-band gravitational-wave data can bound dual-kinematic corrections" ([force boosts and force composition](force-boosts.md)).

### What the program has instead

The program is not without dynamics for the momentum side. The checkpoint gives momentum-space geometry its own dynamical field, the massive spin-2 field X in a [bimetric](../gravity/spin-2-fields/hassan-rosen-bimetric.md) sector ([#11 §7](../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton); [the momentum graviton X](../gravity/momentum-graviton/_index.md)), and [#13 §1](../papers/conjugate-special-relativity.md#1-two-causal-cones) refers to it: "the independently dynamical part of momentum-space geometry is the massive field X". The checkpoint treats conjugate matter χ in ordinary kinematics, with a mass m_χ and a scattering amplitude gated in relative momentum ([#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate); [conjugate matter and the velocity gate](../dark-matter/conjugate-matter/_index.md)). Neither is written in #13's dual kinematics.

[The handoff](../history/documents/handoff.md) records, among the results that exist only in the original chat, a comparison of [general relativity](../gravity/spin-2-fields/general-relativity.md)'s field equations with the program's: "slaved layer g̃ = g⁻¹ is algebraic (Einstein's equation does double duty); dual Newtonian limit = Yukawa in momentum = the gate; X-waves massive, 5 polarizations, frequency floor" ([`HANDOFF.md` §4](../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact)). No artifact derives it ([two gravitational charges and the conjugate field equations (chat-only)](../gravity/momentum-graviton/chat-only-results.md); [a range in momentum](../gravity/spin-2-fields/yukawa-forces.md#conjugate-special-relativity-a-range-in-momentum)).

## Not scheduled

Neither item is among [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems)'s twelve open problems, which do not mention #13, or on the current queue in [`CLAUDE.md`](../../CLAUDE.md) ('Since the handoff'). The handoff's open list ([`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen)) and its queue ([§8](../../HANDOFF.md#8-ranked-next-actions-queue)) do not name them either; the queue's only #13 item is the source check of its † references, item 6 ([the † literature battery](../method/literature-battery.md)). The [two-cones problem](two-cones-inconsistency.md), which depends on this construction, is likewise unscheduled.

## Sources

- [`wiki/papers/conjugate-special-relativity.md` §6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) — the open item, the 3+1 presentation, the shared time and the photon-dispersion argument; [§7](../papers/conjugate-special-relativity.md#7-summary-of-tethers) for the open list; [§1](../papers/conjugate-special-relativity.md#1-two-causal-cones)–[§3](../papers/conjugate-special-relativity.md#3-force-dilation-and-its-mirror) and [§5](../papers/conjugate-special-relativity.md#5-inertia-dualized) for the 3+1 kinematics; [§4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) for the four-vector shell; [§5](../papers/conjugate-special-relativity.md#5-inertia-dualized) for the dual second law that waits on it.
- [`review/v3-worklog.md`](../../review/v3-worklog.md) 'New open items' — item O3: the §6 cone belongs to the four-dimensional map; the dark-photon question.
- [`wiki/papers/broken-born-checkpoint-v2.md` §7](../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) — the dynamics of X; [§8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) for χ in ordinary kinematics; [§14](../papers/broken-born-checkpoint-v2.md#14-open-problems) for the open problems, which do not include it.
- [`HANDOFF.md` §4](../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — the chat-only comparison of field equations; [§2](../../HANDOFF.md#2-scientific-state-one-screen) and [§8](../../HANDOFF.md#8-ranked-next-actions-queue) for the open list and the queue, which do not include it.
- [`CLAUDE.md`](../../CLAUDE.md) 'Since the handoff' — the current queue.
