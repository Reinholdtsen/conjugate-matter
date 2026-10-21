---
title: "Two causal cones"
weight: 30
status: alive
description: "With H = diag(g, g⁻¹) each block defines a null cone: ours bounds |dx/dt| by c and the dual bounds |dp/dt| by c̃ — motion through momentum space is force; the dual cone belongs to the slaved geometry, modified by X at short range."
provenance: [D]
sources:
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md preamble"
  - "papers/conjugate-special-relativity.md §6"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "review/v3-worklog.md 'New open items'"
  - "HANDOFF.md §2"
---

*The two causal cones are the light cones of position space and of momentum space. In the program's broken vacuum the metric on phase space has one block for position and the inverse of that block for momentum, and each block defines its own cone of allowed motion: the familiar cone limits speed, |dx/dt| ≤ c, and its twin limits the rate of change of momentum, |dp/dt| ≤ c̃. A rate of change of momentum is a force, so the twin of the speed of light is a maximum force. This is the starting point of #13, the program's paper on the special relativity of the momentum polarization; it is alive but unreviewed, and #13 uses two different versions of the momentum cone in different sections, an inconsistency that is open.*

**Status:** Alive, unreviewed — [D — compatibility theorem] as #13 §1 tags the block form it starts from — no `verify/` script checks the cones; the block form is the compatibility theorem, which #11 v2.1 and later tag [T][V] (Freidel–Leigh–Minic, machine-checked in [the battery](/wiki/method/verification/battery), test T1); which momentum cone governs is [open](/wiki/conjugate-relativity/two-cones-inconsistency).

## Key facts

- **The block form.** #13 §1: "The broken vacuum equips phase space with H = diag(g, g⁻¹) [D — compatibility theorem]: position space carries the metric g and momentum space its inverse. Each metric defines a null cone." #11 §5 credits the theorem to Freidel, Leigh and Minic and tags it [T][V]; #11 governs ([The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)).
- **The two cones** (#13 §1), with λ the Born length and ε = ℏ/λ "its conjugate momentum scale":

  ```text
  ours:   |dx/dt| ≤ c
  dual:   |dp/dt| ≤ c̃ = ε/(λ/c) = ℏc/λ²
  ```

  The value of c̃ is on [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force); the template is the light cone of [special relativity](/wiki/conjugate-relativity/special-relativity).
- **Force as dual velocity.** #13 §1: "Motion through momentum space is what we call force." The dual cone's invariant speed is therefore a force.
- **The slaved dual cone.** #13 §1: "the dual cone is the causal structure of the *slaved* geometry g⁻¹; the independently dynamical part of momentum-space geometry is the massive field X, which modifies the dual cone only at short range in momentum [D — §7 of the checkpoint]." The slaving g̃ = g⁻¹ is a [corollary of the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-corollaries), and X is [the momentum graviton](/wiki/gravity/momentum-graviton). #11 §7 itself does not discuss a dual cone; it states X's couplings to Standard Model matter as "gravitational-strength and Yukawa-cut at 1/M_X" (§7.5; [Safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)).
- **Which dual cone.** This §1 cone is the 3+1 version: it lives in (t, p), with time shared and slope c̃. #13 §6 instead calls E = c|p| "the dual null cone", which belongs to the four-dimensional Born map; the v3 worklog asks to "fix #13's two cones and settle which construction governs" (`review/v3-worklog.md`, item O3; [Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).
- **Signature.** A light cone needs a metric of Lorentzian signature [T], while the compatibility theorem is proven for positive-definite H. #13's preamble: "The Euclidean/Lorentzian caveat of the main checkpoint is inherited throughout" ([Open: Lorentzian dressing of the Euclidean skeleton](/wiki/phase-space/born-geometry/lorentzian-dressing)).
- **Basis of the status.** #11 v2.2 does not mention the two cones; `HANDOFF.md` §2 lists the maximum force and dual special relativity among the alive results, without a machine-check mark.

## Sources

- `papers/conjugate-special-relativity.md` §1 — the block form, the two cones, force as motion through momentum space, the slaved dual cone; preamble for the inherited caveat; §6 for the second cone.
- `papers/broken-born-checkpoint-v2.md` §5 — the compatibility theorem as [T][V] and its attribution; §7.5 for the range of X.
- `review/v3-worklog.md` 'New open items' — item O3, the two dual cones.
- `HANDOFF.md` §2 — the alive listing.
