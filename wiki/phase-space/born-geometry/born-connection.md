---
title: "The Born connection"
weight: 30
status: established
description: "The unique connection compatible with (ω, η, H) (Freidel–Rudolph–Svoboda) and its curvature R_B[H]; whether it stays unique when only (ω, H) are fundamental is open."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [7]"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.2"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 1"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §11 item 1"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-program-v1.md §3"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §D"
  - "notes/geometric-core.md §F"
  - "notes/tuning-test.md §3"
  - "wiki/papers/reciprocity-toy-models.md ref [2]"
---

*The Born connection is the connection of a Born geometry, phase space with the three compatible structures ω, η and H of [Born geometry](born-structures.md): the rule for comparing vectors at neighbouring points that respects all three structures. A connection defines how fields are differentiated, and its curvature is what the field equations of a geometry are built from. Freidel, Rudolph and Svoboda showed that a Born geometry has exactly one connection compatible with all three under the conditions of their theorem, so its curvature R_B[H] is well defined. The program's first action for the phase-space metric was built on that curvature. In the current reference the connection appears in a citation and in the argument that frames, not metrics, are the natural variables for the mass term of [the momentum graviton](../../gravity/momentum-graviton/_index.md). Under the corrected postulate only ω and H are fundamental, and whether a unique compatible connection still exists then has not been shown.*

**Status:** Established — literature [T] ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)), cited from model memory as [#11](../../papers/broken-born-checkpoint-v2.md) ref. [7]† and not yet checked against the source ([the † literature battery](../../method/literature-battery.md)) — not machine-checked. Uniqueness for the (ω, H)-only structure of P2′ is open [O] ([#5 §F item 5](../../../notes/geometric-core.md#f-status-after-tonight)); it is recorded below and is not among #11's numbered open problems.

## What a connection is [T]

Vectors at different points of a curved space live in different tangent spaces, and comparing them needs a rule. A connection ∇ supplies it: it defines the covariant derivative of a field and parallel transport along a curve. A connection is *compatible* with a structure S, such as a metric or a [symplectic form](../reciprocity/symplectic-form.md), when ∇S = 0, which means that parallel transport preserves S. Its *torsion* measures the failure of infinitesimal parallelograms to close, and its *curvature* measures how a vector rotates when transported around a small loop.

Compatibility alone does not fix a connection. The standard uniqueness statement is the Levi-Civita theorem: a metric has exactly one compatible connection with zero torsion. [General relativity](../../gravity/spin-2-fields/general-relativity.md)'s Einstein–Hilbert action, the integral of √|g| R over spacetime, is built from that connection's curvature scalar R.

A Born geometry carries three structures, and a connection on it has to preserve ω, η and H at once. Whether any connection does so, and what further condition makes one unique, as zero torsion does for a single metric, is the question Freidel, Rudolph and Svoboda answered.

## The theorem [T]

The lab notebook ([#1](../../history/documents/lab-notebook.md) [§2](../../../notes/broken-born-theory.md#2-kinematic-core)) states the result and what follows from it:

> A theorem of Freidel, Rudolph & Svoboda (2018) establishes the existence and uniqueness of a connection compatible with the full triple (ω,η,H) — the *Born connection*. **[T]** Its curvature R_B[H] is therefore well-defined, and a diffeomorphism-style invariant action for H can be written.

Checkpoint [#11](../../history/documents/checkpoint.md) [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) cites it in one clause, "a unique compatible connection exists [7†]", and the v1 program paper as "[T: Freidel–Rudolph–Svoboda 2018]" ([#9 §3](../../../notes/broken-born-program-v1.md#3-the-kinematic-core-and-the-compatibility-theorem)). None of the documents states the theorem's hypotheses beyond compatibility with the full triple; in particular they do not say which condition on the torsion makes the connection unique.

**The reference.** #11 [7]† L. Freidel, F. J. Rudolph, D. Svoboda, "A unique connection for Born geometry," Commun. Math. Phys. (2019), [arXiv:1806.05992](https://arxiv.org/abs/1806.05992). The lab notebook and #9 date the result 2018, #11 dates it 2019. No document reconciles the years; the difference is probably an arXiv year against a journal year, and it is left to the † literature battery ([conflicts between sources](../../history/documents/source-conflicts.md)). The [toy-model note](../../symmetry-breaking/toy-models/_index.md)'s ref. [2], [arXiv:1706.07089](https://arxiv.org/abs/1706.07089), is a different paper by the same authors, "Generalised kinematics for double field theory".

## How the program used it

### The lab notebook's geometric action (v0.1, superseded)

The notebook wrote an Einstein-like action for the phase-space metric from the Born curvature ([#1 §3](../../../notes/broken-born-theory.md#3-action)):

```text
S_H = ½ M_B² ∫_Σ √|H| R_B[H]        over the section Σ, with ω, η frozen (P2)
```

"On the x-tilted vacuum, H decomposes into a spacetime metric g_μν(x) and a momentum-space metric g̃^μν; the g-block reproduces the Einstein–Hilbert action with M_P fixed by M_B and the section volume. [D, schematic]" ([#1 §3](../../../notes/broken-born-theory.md#3-action)). The section Σ comes from [a section condition](../../symmetry-breaking/section-condition.md) borrowed from [double field theory](double-field-theory.md): "Field dependence is restricted to a Lagrangian leaf by a section condition, as in double field theory; consistency of the section condition on general backgrounds is open there and open here. [O]" ([#1 §2](../../../notes/broken-born-theory.md#2-kinematic-core)).

The notebook's first open problem records how far this went: "The field equation for H beyond minisuperspace — the question Born left open in 1938. The action exists (Born connection [T]), but solutions, the section condition on curved backgrounds, and the full ghost analysis do not. [O]" ([#1 §11 item 1](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity)).

[The compatibility theorem](compatibility-theorem.md) then emptied the action of new content. With ω and η both rigid, H = diag(g, g⁻¹), and "S_H is a functional of g alone: a pure metric theory" (calc note [#5](../../history/documents/field-equation-notes.md) [§B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). That finding forced the change from [the original P2](../../program/postulates/original-p2.md) to [P2′](../../program/postulates/p2-prime.md). The superseded action is recorded on [the geometric action S_H](../../gravity/tuning-test/geometric-action.md).

### After P2′

With [the modular field Z = X + iY](../modular-field/modular-field-z.md) in place, calc note #5 restated the field-equation problem as "the field equation for momentum-space geometry is the Re Z sector of S_H" ([§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)) and posed the decisive computation: "expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry" ([§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)). The field-equation notes then settled the character of X by symmetry arguments and [the tuning test](../../gravity/tuning-test/_index.md) instead ([why X must be massive](../../gravity/momentum-graviton/forcing-chain.md)), and the step back from the frame-tier potential to S_H has not been made. #11 lists it as open problem 1: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]" ([Open: deriving the wedge sector from S_H](../../gravity/tuning-test/wedge-reduction.md)).

### The first-order tier

The connection's remaining role in #11 is in an argument about variables. A [vielbein](../../gravity/spin-2-fields/vielbein-formulation.md), or frame, E is a square root of the metric, H = EᵀE. Calc note [#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) sorts the program's objects by how they enter: "J and E live on the same geometric tier (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order." The tuning test fails for potentials built from metrics and passes for potentials built from frames, and the shared tier is the reason given for preferring the frame formulation ([#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv)): "J, E, and the Born connection share the first-order tier, so this is the geometrically minimal formulation." The notebook's v0.5 addendum says the same. See [the frame tier](../../gravity/tuning-test/frame-tier.md).

## Open: connection uniqueness under P2′

Under [P2′](../../program/postulates/p2-prime.md) only ω and H are fundamental. η is not a background structure: "the vacuum spontaneously selects a real structure J (an involution anticommuting with I), and η ≡ HJ" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural)). Freidel, Rudolph and Svoboda's theorem covers the full triple (ω, η, H). Whether ω and H alone determine a unique compatible connection is item 5 of calc note #5's list of what is "Now precisely open":

> (5) connection uniqueness for the (ω, H)-only structure ([Freidel–Rudolph–Svoboda] proved it for the full triple; the para-Hermitian literature — Svoboda, Marotta–Szabo — is the nearest neighbor).

The question bears on the computation [#5 §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) posed, which is phrased in terms of "the generalized curvature scalar of (ω, H_Z)", a curvature for exactly the (ω, H) structure. The item is not carried into [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) and no later document reports work on it. It is open [O] ([open problems](../../status/open-problems.md)). The para-Hermitian literature it points to is described on [the structures ω, η, H](born-structures.md).

## Used by

- [The geometric action S_H and the v0.1 action (superseded)](../../gravity/tuning-test/geometric-action.md) — an action for H written from R_B[H].
- [The section condition: what η fixes](../../symmetry-breaking/section-condition.md) — the v0.1 action, built from the connection's curvature, integrated over a section.
- [The modular field Z = X + iY](../modular-field/modular-field-z.md) — S_H presupposes a connection whose uniqueness is proved only for the full triple.
- [The frame tier: the symplectic vielbein](../../gravity/tuning-test/frame-tier.md) — the polarization, the vielbein and the connection on one first-order tier.
- [The verdict: a conditional pass](../../gravity/tuning-test/conditional-pass.md) — the shared first-order tier is part of the case for frames.
- [Open: deriving the wedge sector from S_H](../../gravity/tuning-test/wedge-reduction.md) — the reduction from the curvature action to the frame-tier potential.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) and ref. [7] — "a unique compatible connection exists [7†]"; the reference and its 2019 date.
- [`wiki/papers/broken-born-checkpoint-v2.md` §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv), [§14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the first-order tier shared with the vielbein; the wedge sector not derived from S_H.
- [`wiki/papers/reciprocity-toy-models.md`](../../papers/reciprocity-toy-models.md) ref. [2] — the other Freidel–Rudolph–Svoboda paper.
- [`notes/geometric-core.md` §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural), [§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard), [§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial), [§F](../../../notes/geometric-core.md#f-status-after-tonight) — S_H reduced to g under strict P2; η ≡ HJ under P2′; the curvature of (ω, H_Z); item 5, connection uniqueness for (ω, H) alone.
- [`notes/tuning-test.md` §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — J, E and the Born connection on the first-order tier.
- [`notes/broken-born-theory.md` §2](../../../notes/broken-born-theory.md#2-kinematic-core), [§3](../../../notes/broken-born-theory.md#3-action), [§11 item 1](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity) — the theorem as #1 states it, with R_B[H] and the 2018 date; S_H; the field equation for H as open; 'Addendum (v0.5)' — the first-order tier.
- [`notes/broken-born-program-v1.md` §3](../../../notes/broken-born-program-v1.md#3-the-kinematic-core-and-the-compatibility-theorem) — the same attribution, dated 2018.
