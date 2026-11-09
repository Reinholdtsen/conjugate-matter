---
title: "Open: Lorentzian dressing of the Euclidean skeleton (OP3)"
weight: 60
status: open
description: "The compatibility theorem and the X chain are proven for positive-definite H; extending them to spacetime signature, where the stabilizer becomes U(1, d−1), is open item 3."
provenance: [O]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 3"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §1"
  - "wiki/papers/broken-born-checkpoint-v2.md §6"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "notes/x-classification.md §1"
  - "notes/x-classification.md §2"
  - "notes/x-classification.md §3"
  - "notes/x-classification.md §5"
  - "notes/geometric-core.md §D"
  - "notes/tuning-test.md §2"
  - "notes/tuning-test.md §5"
  - "notes/beta-coefficients.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §10 item 2"
  - "notes/broken-born-program-v1.md §11"
  - "wiki/papers/conjugate-special-relativity.md preamble"
  - "wiki/papers/conjugate-special-relativity.md §1"
  - "wiki/papers/conjugate-special-relativity.md §2"
  - "HANDOFF.md §2"
---

*The Lorentzian dressing of the Euclidean skeleton is the open problem of carrying the program's main geometric results over from a positive-definite phase-space metric, the Euclidean case, to the Lorentzian signature of physical spacetime, in which time enters with the opposite sign to space. Those results, [the compatibility theorem](compatibility-theorem.md), the parametrization of [the Siegel domain](../modular-field/siegel-domain.md) and the chain of arguments that forces [the momentum graviton X](../../gravity/momentum-graviton/_index.md) to be massive, were proven in the Euclidean case. The extension is open problem 3 of the checkpoint [#11](../../papers/broken-born-checkpoint-v2.md). The change is not a formality: with a Lorentzian metric the group that leaves the vacuum fixed becomes non-compact, and the metric on the space of field values becomes indefinite, the situation in which some field components would carry kinetic energy of the wrong sign. The working notes expect the gauge symmetry and mass mechanism already in the chain to keep the theory healthy there, and list the extension as a check. Nothing has been computed, and the checkpoint counts it among the three items on which the word "theory" still waits.*

**Status:** Open [O] — [#11 §14 item 3](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — nothing computed; first flagged in calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) and carried by [#7](../../../notes/tuning-test.md), [#8](../../../notes/beta-coefficients.md), [#9](../../../notes/broken-born-program-v1.md), [#13](../../papers/conjugate-special-relativity.md) and [the handoff](../../history/documents/handoff.md)'s open list ([open problems and the queue](../../status/open-problems.md)).

## The open item

Checkpoint [#11](../../history/documents/checkpoint.md) [§14 item 3](../../papers/broken-born-checkpoint-v2.md#14-open-problems) reads in full: "Lorentzian dressing of the Euclidean-rigorous skeleton [O]." #11 does not define the phrase. Calc note [#6](../../history/documents/field-equation-notes.md) [§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) does: "The chain of §1–§3 is the Euclidean-rigorous skeleton; the Lorentzian dressing rides on the same FP/HR machinery it lands on." FP is Fierz–Pauli and HR is Hassan–Rosen, the theories of massive and bimetric gravity in which the chain ends. The three steps of that chain ([why X must be massive](../../gravity/momentum-graviton/forcing-chain.md)):

1. **The shift symmetry** [D — rigorous] ([#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous)). The rigid [symplectic group](../reciprocity/symplectic-form.md) contains Z → Z + B, so constant shifts of X are exact symmetries and X is "axion-like" ([shift symmetry](../../gravity/momentum-graviton/shift-symmetry.md)).
2. **The gauge structure and the no-go** [D + T] ([#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)). Dual diffeomorphisms act as δX_μν = ∂₍μλ_ν₎, a second copy of linearized diffeomorphisms, and a second massless graviton that couples to the first is excluded by the multi-graviton no-go ([dual diffeomorphisms](../../gravity/momentum-graviton/dual-diffeomorphisms.md); [the multi-graviton no-go theorem](../../gravity/spin-2-fields/multi-graviton-no-go.md)).
3. **The mass mechanism** [D — structural] ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). The vacuum's choice of polarization breaks the dual diffeomorphisms spontaneously, and X absorbs the four would-be [Goldstone modes](../../symmetry-breaking/goldstone-and-higgs.md) and becomes a massive spin-2 field ([the gravitational Higgs mechanism](../../gravity/momentum-graviton/gravitational-higgs.md)).

The same note names the geometric inputs that share the restriction: "the compatibility theorem and Siegel parametrization were derived for positive H" ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)).

## Euclidean and Lorentzian signature [T]

The signature of a metric counts its positive and negative directions. A positive-definite metric, all of whose directions have positive length, is called Euclidean (or Riemannian). A spacetime metric is Lorentzian: the time direction has the opposite sign to the three space directions. Only an indefinite metric has nonzero vectors of zero length, so of the two only a Lorentzian metric has light cones.

The program's results assume the Euclidean case at the start. The compatibility theorem is a statement about positive H with g ∈ Sym⁺(d), and the Siegel domain requires "Z = X + iY (symmetric; Y > 0)" ([#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)), where Y = Im Z is identified with the metric g. A Lorentzian g lies outside both settings.

## What changes in Lorentzian signature

[#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) states the caveat as first recorded:

> … the compatibility theorem and Siegel parametrization were derived for positive H. Lorentzian g makes the stabilizer U(1, d−1) and the invariant target metric indefinite — which is precisely the regime where the gauge+mass structure above is not a luxury but the only path to health. The chain of §1–§3 is the Euclidean-rigorous skeleton; the Lorentzian dressing rides on the same FP/HR machinery it lands on.

**The stabilizer.** The symplectic group Sp(2d, ℝ) acts on the Siegel domain, and the subgroup that leaves one point fixed is its stabilizer. For positive H that subgroup is a copy of the compact unitary group U(d), which is why the domain is the quotient Sp(2d, ℝ)/U(d) [T]. With a Lorentzian g, #6 records the stabilizer as U(1, d−1), the group that preserves a Hermitian form with one sign opposite to the rest, which is non-compact [T]. At d = 4 it is U(1,3) ([#9 §10 item 2](../../../notes/broken-born-program-v1.md#10-open-problems)).

**The target metric.** A field that takes values in a curved space, such as Z in the Siegel domain, has a kinetic term weighted by a metric on that space, the target metric [T]. Calc note [#5](../../../notes/geometric-core.md) counts among the good signs that "the Siegel target metric Tr(Y⁻¹dZ Y⁻¹dZ̄) is positive-definite" ([#5 §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)). With a Lorentzian g it becomes indefinite ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)), and a direction of negative norm gives its field component a kinetic term of the wrong sign, a [ghost](../../gravity/spin-2-fields/ghosts.md) [T].

**Why the gauge and mass structure matters there.** [#6 §2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t) explains, tagged [T — standard], [why a symmetric tensor needs its gauge symmetry](../../gravity/spin-2-fields/signature-obstruction.md): "Without the gauge invariance, no ghost-free two-derivative kinetic term for a Lorentz-covariant symmetric tensor exists (mixed time–space components enter with the wrong sign under any invariant contraction; this is why the Fierz–Pauli structure and its accidental gauge symmetry exist at all)." The gauge symmetry of step 2 and the Fierz–Pauli structure of step 3 are the standard means of removing such components ([the Fierz–Pauli mass term and the Boulware–Deser ghost](../../gravity/spin-2-fields/fierz-pauli.md); [Hassan–Rosen bimetric gravity](../../gravity/spin-2-fields/hassan-rosen-bimetric.md)). This is the sense of "not a luxury but the only path to health".

## Where signature already enters

The chain uses Lorentzian signature at one point already. [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t): "Massless X is excluded by the multi-graviton no-go [8†]; ungauged X by Lorentz signature." The second clause is the wrong-sign argument quoted above, and #11's abstract counts "a signature obstruction" among the structural results that force X to be massive ([#11 §1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts)).

## What the extension would have to cover

The sources name these pieces as proven or computed in the Euclidean setting:

- the compatibility theorem and the Siegel parametrization ([#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural));
- the chain of [#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous)–[§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural), summarized above;
- the tuning test's block computations, done "in the vacuum frame (g₀ = 1), Euclidean skeleton" ([#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous); [the tuning test](../../gravity/tuning-test/_index.md));
- the kinematics of [conjugate special relativity](../../conjugate-relativity/_index.md). #13's preamble: "The Euclidean/Lorentzian caveat of the main checkpoint is inherited throughout." #13 does not say which of its statements depend on the caveat. Its constructions are null cones and the dual interval ds̃² = c̃²dt² − dp² ([#13 §1](../../papers/conjugate-special-relativity.md#1-two-causal-cones)–[§2](../../papers/conjugate-special-relativity.md#2-force-boosts); [two causal cones](../../conjugate-relativity/two-causal-cones.md)), and null cones exist only for an indefinite metric. On [#13 §1](../../papers/conjugate-special-relativity.md#1-two-causal-cones)'s tag for its cones, "[D — compatibility theorem]", see flag 30 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md).

No document spells out the computation that would close the item. #6 expects the dressing to ride on "the same FP/HR machinery it lands on", and the v1 program paper words the item as "Lorentzian dressing of the Euclidean-rigorous skeleton (stabilizer U(1,3); the FP/HR machinery is exactly the tool it lands on) [O]" ([#9 §10 item 2](../../../notes/broken-born-program-v1.md#10-open-problems)).

## History and how the documents rank it

The item was first flagged in [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) and listed again in that note's §5 ("Lorentzian-signature dressing (§3)"). Every later document carries it, and none reports a computation:

- **A check, not the substance.** Calc note #7 lists "(iii) Lorentzian dressing of the Euclidean skeleton" among the remaining [the field-equation problem](../../history/main-problems.md) items and ranks it: "Items (ii)–(iv) are checks; item (i) is the substance" ([#7 §5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem)). The [notebook](../../history/documents/lab-notebook.md)'s v0.5 addendum calls the same three items "logged checks".
- **None of it existential.** Calc note #8 closes the field-equation problem as "solved in structure" with an "Open residue, none of it existential", item (ii) being the Lorentzian dressing ([#8 §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)); the notebook's v0.6 addendum repeats "Residual open items (none existential)".
- **The open lists.** [#9 §10 item 2](../../../notes/broken-born-program-v1.md#10-open-problems); the handoff's open item 5, "First-principles wedge reduction from S_H; Lorentzian dressing of the Euclidean skeleton" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)); [#11 §14 item 3](../../papers/broken-born-checkpoint-v2.md#14-open-problems).
- **What "theory" waits on.** [#9 §11](../../../notes/broken-born-program-v1.md#11-assessment): "The word 'theory' awaits items 1–2 of §10", where item 2 is this one. [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment): "That is a live research program; the word 'theory' still waits on items 1–3 above", the other two being [the wedge-sector derivation (OP1)](../../gravity/tuning-test/wedge-reduction.md) and [the partially-massless comparison (OP2)](../../gravity/palindromic-branch/pm-comparison.md) ([the assessment](../../program/assessment.md)).

The two rankings are consistent as written: the notes do not expect the extension to threaten the structure, and #11 still withholds the word "theory" until it is done. The plain-language opening of [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) says that none of the unfinished list is "any longer, about whether the structure can exist."

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §14 item 3](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open item; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — "theory" waits on items 1–3.
- [`wiki/papers/broken-born-checkpoint-v2.md` §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t), [§1](../../papers/broken-born-checkpoint-v2.md#1-two-abstracts) — the signature obstruction in the X chain; "a signature obstruction" in the abstract.
- [`wiki/papers/broken-born-checkpoint-v2.md` §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field) — the Siegel domain's Y > 0.
- [`wiki/papers/conjugate-special-relativity.md`](../../papers/conjugate-special-relativity.md) preamble, [§1](../../papers/conjugate-special-relativity.md#1-two-causal-cones), [§2](../../papers/conjugate-special-relativity.md#2-force-boosts) — #13 inherits the caveat; its null cones and dual interval.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — open item 5.
- [`notes/x-classification.md` §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous)–[§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural), [§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — the chain, the caveat, U(1, d−1), the definition of the Euclidean-rigorous skeleton; the item listed as open.
- [`notes/geometric-core.md` §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) — the positive-definite Siegel target metric.
- [`notes/tuning-test.md` §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous), [§5](../../../notes/tuning-test.md#5-status-of-the-field-equation-problem) — the Euclidean frame of the tuning test; the dressing as a check.
- [`notes/beta-coefficients.md` §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out) — the residue, "none of it existential".
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.5)', 'Addendum (v0.6)' — the logged checks; "none existential".
- [`notes/broken-born-program-v1.md` §10 item 2](../../../notes/broken-born-program-v1.md#10-open-problems), [§11](../../../notes/broken-born-program-v1.md#11-assessment) — the stabilizer U(1,3) at d = 4; "theory" awaits items 1–2.
