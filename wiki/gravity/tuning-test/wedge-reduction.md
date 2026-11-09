---
title: "Open: deriving the wedge sector from S_H (OP1)"
weight: 70
status: open
description: "The ghost-free class was selected by minimality and consistency, not derived line by line from the geometric action; with OP2 and OP3 it gates the word 'theory'."
provenance: [O]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 1"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md §2"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §5"
  - "notes/beta-coefficients.md §5"
  - "notes/tuning-test.md §1"
  - "notes/tuning-test.md §3"
  - "notes/x-classification.md §1"
  - "notes/x-classification.md §3"
  - "notes/geometric-core.md §B"
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §D"
  - "notes/geometric-core.md §F"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §10"
  - "notes/broken-born-program-v1.md §11"
  - "notes/knot-dark-matter-standalone.md §1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §8"
  - "CLAUDE.md 'Since the handoff'"
  - "review/wiki-build-flags.md item 7"
---

*This open problem asks for the [ghost-free](../spin-2-fields/ghosts.md) potential of the [momentum graviton X](../momentum-graviton/_index.md) to be derived from the program's geometric action instead of being chosen. [The tuning test](_index.md) found that wedge polynomials of the symplectic vielbein E and the polarization frame E₀[J] form a ghost-free class ([the frame tier](frame-tier.md)), and argued that this is the minimal way to couple the polarization to the geometry. That argument selects the class; it does not obtain it line by line from an action. The only geometric action written out, the [lab notebook](../../history/documents/lab-notebook.md)'s [S_H](geometric-action.md), predates the change of postulate that brought X into the theory. The problem is item 1 of the open problems in [checkpoint #11](../../history/documents/checkpoint.md) [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) [O], and one of the three items, with [the partially-massless comparison](../palindromic-branch/pm-comparison.md) and [the Lorentzian dressing](../../phase-space/born-geometry/lorentzian-dressing.md), on which [#11](../../papers/broken-born-checkpoint-v2.md) makes the word "theory" wait. Nothing has been computed toward it, and it is not on the current work queue.*

**Status:** Open — [O] — item 1 of [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems); also item (i) of the open residue in [calc note #8](../../history/documents/field-equation-notes.md) [§5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out) and the first half of open item 5 in [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen); no derivation exists. Listed in [open problems and the queue](../../status/open-problems.md).

## The open problem

[#11 §14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems), in full: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]."

The item was first stated by calc note [#8](../../../notes/beta-coefficients.md) ([the field-equation calc notes](../../history/documents/field-equation-notes.md)), in its close-out of [the field-equation problem](../../history/main-problems.md): "**The field-equation problem: solved in structure.** Open residue, none of it existential: (i) first-principles reduction of the symplectic-vielbein wedge sector from S_H (the class was selected by minimality + consistency, not derived line-by-line)" ([#8 §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)). The four other items of that residue became [#11 §14 items 3](../../papers/broken-born-checkpoint-v2.md#14-open-problems), 6, 5 and 2.

"The frame-tier wedge sector" is the potential that gives X its mass, written as wedge polynomials of the two frames, (E, E₀[J]) ([the frame tier](frame-tier.md)). "S_H" is the program's geometric action ([the geometric action S_H](geometric-action.md)). A first-principles reduction would start from the action and arrive at that potential, instead of selecting it.

## How the class was selected

Calc note [#7](../../../notes/tuning-test.md) reached the frame tier in two steps of different kinds ([#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t)):

- **The literature step [T].** "In vielbein variables the ghost-free potentials are polynomial — wedge products ε(e ∧ … ∧ f ∧ …) of two frames (Hinterbichler–Rosen) [T]". This is a result about which potentials are healthy ([the vielbein formulation](../spin-2-fields/vielbein-formulation.md)).
- **The program's step, by minimality.** "**J and E live on the same geometric tier** (first-order structures on the tangent, like the Born connection), while H = EᵀE is second-order. The geometrically minimal coupling of the polarization to the modular sector is therefore E-linear — wedge polynomials of (E, E₀[J])". This is a reason to expect the program's coupling to take that form, not a derivation that it does.

"Consistency" is the other half of #8's phrase. The coupling had to lie in the one known consistent structure for a massive spin-2 field, "Fierz–Pauli/dRGT/Hassan–Rosen" ([#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t), which drops the qualifier in [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)'s "exactly one known consistent structure"; see flag 7 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)), dRGT being de Rham–Gabadadze–Tolley ([the Fierz–Pauli mass term](../spin-2-fields/fierz-pauli.md); [dRGT massive gravity](../spin-2-fields/drgt-massive-gravity.md); [Hassan–Rosen bimetric gravity](../spin-2-fields/hassan-rosen-bimetric.md)), and the coupling built from metrics does not ([the metric tier fails twice](metric-tier-failures.md)). Minimality picked the frame-level coupling, and consistency required a ghost-free one; the frame tier satisfies both. OP1 asks for a derivation from the action in place of that choice.

## What a derivation would start from

- **The only action written out is superseded.** [The lab notebook](../../history/documents/lab-notebook.md)'s S_H = ½M_B² ∫_Σ √|H| R_B[H] was written "with ω, η frozen (P2)" ([#1 §3](../../../notes/broken-born-theory.md#3-action)). Under that postulate, "S_H is a functional of g alone: a pure metric theory. No momentum graviton" ([#5 §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural); [#11 §5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)), so that form contains no X to give a potential to.
- **After [P2′](../../program/postulates/p2-prime.md) the symbol stays, the action is not written.** The notes use S_H for an action built from ω and H: "Constant shifts of X are **exact symmetries** of any S_H built from (ω, H)" ([#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous)), and "the field equation for momentum-space geometry is the Re Z sector of S_H" ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)). No document writes this action out.
- **Where X's potential must come from.** The same paragraph of [#6 §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous) continues: "X has no potential and no non-derivative couplings from the geometric sector alone". X's mass comes from "the η-selection (Higgs) sector", in which the polarization J enters ([#7 §1](../../../notes/tuning-test.md#1-the-object-to-test); [the misalignment potential](misalignment-potential.md)), and the wedge sector involves J through E₀[J]. The documents do not say how the action from which the wedge sector is to be derived includes J.
- **The direct expansion was posed and not done.** Calc note #5 defined the decisive computation as "expand the generalized curvature scalar of (ω, H_Z) to quadratic order in X about X = 0 on the section, with ω-generalized diffeomorphisms as the gauge symmetry" ([#5 §D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial)). It was "Not completed tonight", and no later document reports it; calc notes #6 to #8 settled the character of X by symmetry and consistency arguments instead.
- **The connection under P2′.** The v0.1 action is built on the curvature of [the Born connection](../../phase-space/born-geometry/born-connection.md), which is unique for the full triple (ω, η, H). Whether ω and H alone fix a unique connection is open: "(5) connection uniqueness for the (ω, H)-only structure" ([#5 §F](../../../notes/geometric-core.md#f-status-after-tonight)). That item is not among #11's numbered open problems.

## Why it matters

**Selection against derivation.** [#11 §2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) warns of "the selection-versus-derivation bias", acknowledged "explicitly where it operates (§7.4)". [§7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) applies it to the novelty of [the vacuum-energy identity](../palindromic-branch/vacuum-energy-identity.md), which it downgrades pending a literature comparison. The parenthesis of [§14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems), "(class selected, not derived)", records the same distinction for the frame-tier class ([claim tiers and selection bias](../../method/claim-tiers.md)).

**What rests on the selected class.** The positive half of the tuning test, [the frame tier](frame-tier.md), and with it [the verdict: a conditional pass](conditional-pass.md). The potential that [reciprocity](../../phase-space/reciprocity/born-reciprocity.md) then restricts, [the palindromic branch](../palindromic-branch/_index.md), including [the palindrome βₙ = β₄₋ₙ](../palindromic-branch/palindrome.md) and [the vacuum-energy identity](../palindromic-branch/vacuum-energy-identity.md). The picture of [constrained bimetric gravity](constrained-bimetric.md), and the program's statement of [Born's answer](../momentum-graviton/borns-answer.md). All of these take the selected class as their starting point.

**The word "theory".** [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) ends: "That is a live research program; the word 'theory' still waits on items 1–3 above." Items 2 and 3 are [the partially-massless comparison (OP2)](../palindromic-branch/pm-comparison.md) and [the Lorentzian dressing of the Euclidean skeleton (OP3)](../../phase-space/born-geometry/lorentzian-dressing.md) ([the assessment](../../program/assessment.md)).

**How the notes ranked it.** Calc note #8 called the whole residue "none of it existential" ([#8 §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)), and #11 opens its list of open problems by saying that none of them is "any longer, about whether the structure can exist" ([#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems)). The item is ranked as unfinished work on a structure the notes consider settled, and at the same time as one of the three conditions for calling the program a theory.

## History of the item

- **Calc note [#8 §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)** lists it first in the open residue of the field-equation problem, and the lab notebook's v0.6 addendum repeats it: "Residual open items (none existential): first-principles wedge reduction from S_H; Lorentzian dressing; τ–Stückelberg mixing; dual-stress enhancement parametrics; literature check on the Λ = 0 observation" ([the lab notebook](../../history/documents/lab-notebook.md)).
- **The v1 program paper**, superseded by #11, makes it open problem 1 in nearly the same words as #8 ([#9 §10 item 1](../../../notes/broken-born-program-v1.md#10-open-problems)), and makes "theory" wait on it and the Lorentzian dressing: "The word 'theory' awaits items 1–2 of §10" ([#9 §11](../../../notes/broken-born-program-v1.md#11-assessment); [the checkpoint](../../history/documents/checkpoint.md)).
- **The handoff** pairs it with the Lorentzian dressing as open item 5: "First-principles wedge reduction from S_H; Lorentzian dressing of the Euclidean skeleton" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen); [the handoff](../../history/documents/handoff.md)).
- **The standalone manuscript [#14](../../../notes/knot-dark-matter-standalone.md)**, since withdrawn after its [round-3](../../method/review/round-3/_index.md) review for reasons unrelated to this item ([Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md)), put the caveat to its referees: "That the symmetry-breaking sector lands on the ghost-free potential is argued from a first-order (vielbein) formulation and is a structural claim, not a line-by-line derivation" ([#14 §1](../../../notes/knot-dark-matter-standalone.md#1-framework)).
- **Checkpoint #11** makes it [§14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems), and [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) adds the partially-massless comparison to the items on which "theory" waits.

No document reports work toward a derivation.

## The queue

The handoff's ranked queue of next actions did not include the item ([`HANDOFF.md` §8](../../../HANDOFF.md#8-ranked-next-actions-queue)). The current queue, in [`CLAUDE.md`](../../../CLAUDE.md) ('Since the handoff'), is the handoff's §8 items 5 and 6, namely the partially-massless comparison and [the † literature battery](../../method/literature-battery.md), followed by an optional round-6 review of [the toy-model note](../../symmetry-breaking/toy-models/_index.md) "but only before any external use"; item 7, [the phase-space-diameter note](../../cosmology/scale-factor-duality/phase-space-diameter.md), is done. This item is not on it ([open problems and the queue](../../status/open-problems.md)).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §14 item 1](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open problem [O], and the opening line of [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems); [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — "theory" waits on items 1–3; [§2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification), [§7.4](../../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade) — the selection-versus-derivation bias; [§7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — the one consistent structure for massive spin-2; [§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem) — S_H a functional of g alone under strict P2.
- [`notes/beta-coefficients.md` §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out) — the open residue of the field-equation problem, "none of it existential".
- [`notes/tuning-test.md` §1](../../../notes/tuning-test.md#1-the-object-to-test), [§3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — the η-selection sector; the frame-tier argument by minimality.
- [`notes/x-classification.md` §1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous), [§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — S_H built from (ω, H) gives X no potential; the health criterion.
- [`notes/geometric-core.md` §B](../../../notes/geometric-core.md#b-the-inconsistency-and-the-forced-repair-d--structural), [§C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard), [§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial), [§F](../../../notes/geometric-core.md#f-status-after-tonight) — S_H under strict P2; the Re Z sector of S_H; the expansion posed and not completed; connection uniqueness for (ω, H).
- [`notes/broken-born-theory.md` §3](../../../notes/broken-born-theory.md#3-action) — S_H written with ω and η frozen; 'Addendum (v0.6)' — the residual open items.
- [`notes/broken-born-program-v1.md` §10](../../../notes/broken-born-program-v1.md#10-open-problems), [§11](../../../notes/broken-born-program-v1.md#11-assessment) — the v1 listing and "theory" awaiting items 1–2.
- [`notes/knot-dark-matter-standalone.md` §1](../../../notes/knot-dark-matter-standalone.md#1-framework) — the caveat as stated in the withdrawn manuscript.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — open item 5; [§8](../../../HANDOFF.md#8-ranked-next-actions-queue) — the ranked queue at the handoff.
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the current queue.
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 7 — "the unique consistent structure" without the "known" of [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural); pending.
