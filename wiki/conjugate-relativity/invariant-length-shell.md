---
title: "The invariant-length shell and Planck closure"
weight: 70
status: alive
description: "The Born image of the mass shell is x_μx^μ = λ_χ², an irreducible extent for conjugate quanta; E = λc̃ returns the Planck energy at λ = l_P, and μ ~ ℏ/λ_χ reads the gate scale as a dual-relativistic invariant."
provenance: [D]
sources:
  - "wiki/papers/conjugate-special-relativity.md §4"
  - "wiki/papers/conjugate-special-relativity.md §1"
  - "wiki/papers/conjugate-special-relativity.md §5"
  - "wiki/papers/conjugate-special-relativity.md §6"
  - "wiki/papers/conjugate-special-relativity.md §7"
  - "wiki/papers/conjugate-special-relativity.md References [3]–[4]"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 1"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 items 4, 10"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §3"
  - "notes/x-classification.md §4"
  - "review/v3-worklog.md 'New open items'"
  - "review/wiki-build-flags.md item 17"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §3"
  - "review/round3/referee/audit-notes.md Step 1"
  - "CLAUDE.md 'Since the handoff'"
  - "popsci/universes-other-half.md 'A second speed of light'"
---

*The invariant-length shell is the [momentum polarization](../phase-space/reciprocity/lagrangian-polarizations.md)'s counterpart of the [mass shell](special-relativity.md). Every observer assigns an ordinary particle the same mass; [#13](_index.md), the paper on conjugate special relativity, proposes that every observer of the mirror polarization assigns a conjugate particle the same size, an irreducible length λ_χ, and obtains this by applying [Born's exchange of position and momentum](../phase-space/reciprocity/born-reciprocity.md) to the mass shell. Two consequences are drawn. A length times the [maximum force](maximum-force.md) is an energy, and at the [Planck length](../gravity/spin-2-fields/planck-units.md#planck-closure) it equals the Planck energy exactly, a result [#13](../papers/conjugate-special-relativity.md) calls closure at the self-dual point. And a fixed size in position fixes a width in momentum, as a short pulse fixes a broad spectrum; #13 identifies that width with the momentum scale of the dark-matter [velocity gate](../dark-matter/conjugate-matter/velocity-gate.md), which makes the [knee in dark-matter self-interaction](../predictions/self-interaction-knee.md) a dual-relativistic invariant. The shell is alive but unreviewed: #13 tags it as derived, but no review round or script has checked it, and the [checkpoint #11](../history/documents/checkpoint.md) does not mention it. Its description of dark-matter quanta by a length has not been reconciled with the checkpoint's ordinary treatment of them, which governs by the wiki's order of precedence.*

**Status:** Alive, unreviewed — the shell [D — structural], citing Born [3†, 4†]; Planck closure [D]; the gate-scale reading [D — structural] (all [#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell)). The tags are #13's own: no review round has covered #13, no `verify/` script checks the closure, and [#11](../history/documents/checkpoint.md) does not mention any of it. The λ_χ description of conjugate quanta is unreconciled with [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate), which governs for the χ candidate.

## The template: the mass shell [T]

In [special relativity](special-relativity.md) a particle's energy E and momentum **p** form a four-vector, p^μ = (E/c, **p**). Its square under the Minkowski metric, p_μp^μ = E²/c² − **p**², has the same value in every inertial frame, because Lorentz boosts preserve it, and that value is m²c², with m the particle's mass [T]. For a given mass the condition p_μp^μ = m²c² picks out a hyperboloid in four-momentum space, the mass shell. A boost moves a free particle along its shell, never off it, so the mass is the one label all inertial observers agree on. At rest **p** = 0, and the condition gives the rest energy E = mc² [T].

#13 transcribes this structure into the momentum polarization. Its §1 gives momentum space a light cone of its own, whose invariant "speed" is a force ([two causal cones](two-causal-cones.md); [the maximum force c̃ = c⁴/G](maximum-force.md)), and its §2 gives the transformations that preserve it ([force boosts](force-boosts.md)). [§4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell), the subject of this page, asks what plays the part of mass.

## The shell

### The Born image of the mass shell

[Born reciprocity ρ](../phase-space/reciprocity/born-reciprocity.md) is the exchange (x, p) → (p, −x) of position and momentum. [#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) applies it to the mass shell:

> "Our invariant hypersurface is the mass shell, p_μp^μ = m²c². Its Born image is a position-space hyperboloid,"

```text
x_μx^μ = λ_χ²
```

> "an **invariant-length shell**: conjugate quanta are characterized by an irreducible extent λ_χ as ours are by mass [D — structural; this recovers Born's 1938–49 program of a self-dual physics with both m and λ fundamental [3†, 4†]]."

The mass shell constrains momentum; its image constrains position. A conjugate quantum, a particle of the p-polarized matter of postulate [P4](../program/postulates/p4-polarized-matter.md), would be labelled by an extent λ_χ on which all observers of its polarization agree, as an ordinary particle is labelled by its mass. [#13 §7](../papers/conjugate-special-relativity.md#7-summary-of-tethers) lists the "invariant-length shell" among the "Kinematic structure fixed [D]". The step uses no action: the shell is the image of a known structure under ρ, and the qualifier "structural" in the tag is #13's.

### What #13 leaves unspecified

- **The letter λ.** In [#13 §1](../papers/conjugate-special-relativity.md#1-two-causal-cones), λ is the [Born length](../phase-space/reciprocity/born-length.md), the length that sets the maximum force. In [§4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell), λ_χ is the extent of a conjugate quantum, and the closure below uses a plain λ for a length. [`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen) writes "invariant length λ".
- **Which presentation.** The shell is written with four-vectors, like the mass shell, whose time component is the energy [T]. [#13's §1](../papers/conjugate-special-relativity.md#1-two-causal-cones)–[§3](../papers/conjugate-special-relativity.md#3-force-dilation-and-its-mirror) work in a 3+1 presentation, in which only space and momentum trade places and time is shared, and [§6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) lists the construction that also exchanges time and energy as open. #13 does not say which of the two the shell belongs to ([Open: the two dual cones](two-cones-inconsistency.md); [Open: the four-dimensional Born map and dual dynamics](four-dimensional-born-map.md)).

### Born's program [3†, 4†]

[#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell)'s plain-language passage: "This was Born's original hope in 1938: a physics with a fundamental mass and a fundamental length on equal footing." The references are [3]† M. Born, "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 (1938), and [4]† M. Born, "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 (1949), both cited from model memory; they are #11's references [1]† and [2]† ([Born's question](../program/borns-question.md)). [#13 §7](../papers/conjugate-special-relativity.md#7-summary-of-tethers) counts "Born's self-dual program [3†, 4†]" among its literature tethers.

The [round-3](../method/review/round-3/_index.md) referee checked the same two papers in another manuscript's reference list and found the metadata correct, but "1938 abstract does not state the rule; primary text paywalled" ([`review/round3/referee/audit-notes.md`](../../review/round3/referee/audit-notes.md), Step 1). Whether Born's papers express the hope in these terms is part of [the † literature battery](../method/literature-battery.md), #11's open problem 10 (OP10) and item 1 of the current queue.

## Planck closure

### The dual rest energy

The ordinary rest energy is mass times the square of the invariant speed. [#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) gives a dual counterpart: "The dual rest-energy relation is E = λ c̃ (length × maximum force)." A length times a force has the units of an energy [T]. Here c̃ is the invariant "speed" of the dual cone, which has the units of force because a trajectory's rate of motion through momentum space, dp/dt, is a force. #13 states the relation without a derivation.

### At the Planck length

Two inputs come from [#13 §1](../papers/conjugate-special-relativity.md#1-two-causal-cones). The maximum force is c̃ = ℏc/λ², with λ the Born length, and "The only length the gravitational sector supplies is the Planck length, λ² = ℏG/c³", which gives c̃ = c⁴/G. The Planck energy is √(ℏc⁵/G), one of the Planck units built from ℏ, c and G [T] ([maximum force and maximal acceleration in the literature](maximum-force-conjectures.md)). [#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) then evaluates the dual rest energy at the Planck length:

> "At λ = l_P: E = l_P · c⁴/G = √(ℏc⁵/G) — the Planck energy, exactly [D]. The dual E = mc² returns the right corner of physics."

```text
E = λ c̃,   c̃ = c⁴/G,   λ = l_P   ⟹   E = l_P · c⁴/G = √(ℏc⁵/G) = E_Planck
```

The bullet is headed "Closure at the self-dual point". #13 does not define the self-dual point; the bullet evaluates the relation at λ = l_P, the value [§1](../papers/conjugate-special-relativity.md#1-two-causal-cones) gave the Born length. [#13 §7](../papers/conjugate-special-relativity.md#7-summary-of-tethers) lists "E(l_P) = E_Planck" among its "Numerical anchors". No `verify/` script checks it, although the project's rule asks for executed code behind every asserted number ([the iron rule](../method/verification/iron-rule.md)).

## The gate scale as a dual-relativistic invariant

### Width in position, width in momentum [T]

A waveform confined to a short interval has a broad spectrum, and the product of the two widths has a lower bound: the time–bandwidth relation of Fourier analysis. In quantum mechanics momentum is ℏ times the wavenumber, so a state confined to a region of size L has a momentum spread of order ℏ/L, [the uncertainty relation](../phase-space/reciprocity/canonical-commutator.md) [T] ([the Fourier transform](../phase-space/reciprocity/fourier-transform.md)).

### The reading

[#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell), the second of its two anchors:

> "The conjugate quantum's invariant extent fixes its intrinsic momentum-space width μ ~ ℏ/λ_χ — which is precisely the gate scale of the dark-matter sector, v\* = √2 μ/m_χ. The knee in the dark-matter self-interaction curve is, in this reading, a *dual-relativistic invariant of the dark sector* made visible in galactic dynamics [D — structural]."

The chain has four links:

1. λ_χ is the conjugate quantum's invariant extent (the shell above).
2. Its intrinsic momentum width is μ ~ ℏ/λ_χ, the reciprocal relation between widths.
3. μ is the momentum scale of the [velocity gate](../dark-matter/conjugate-matter/velocity-gate.md). In [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) the self-interaction of [conjugate matter](../dark-matter/conjugate-matter/_index.md) carries a gate F(k²/μ²) in the incoming relative momentum k, "with μ the χ quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]"; [calc note #6](../history/documents/field-equation-notes.md) [§4](../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) identifies μ as "the χ quantum's own p-width" ([the gate mechanism](../dark-matter/conjugate-matter/gate-mechanism.md)). The tag on the mechanism is disputed: [`notes/gate-mechanism.md`](../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging [#11 §7](../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate, and flag 55 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism ([the gate mechanism](../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). On this link of the chain the note adds: "[#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) identifies μ with ħ/λ_χ, an extent in position. Standard form-factor physics turns that into a form factor in the transfer q at scale μ, not a gate in k [T]" (§3).
4. The knee in the cross-section sits at the gate velocity v\* = √2 μ/m_χ, so it inherits the invariance of λ_χ ([Row 1: the knee in σ_T(v)](../predictions/self-interaction-knee.md)). The √2 depends on the gate convention; see flag 17 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md), described below.

The relation μ ~ ℏ/λ_χ appears only in #13, and #13 gives no value for λ_χ.

### Where v\* comes from

The formula v\* ≡ √2 μ/m_χ is the definition in [the lab notebook](../history/documents/lab-notebook.md) [#1](../../notes/broken-born-theory.md) ([§5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d)), written for its Gaussian gate ([the gated scattering law](../dark-matter/conjugate-matter/scattering-law.md)); #1 is superseded as a reference. #11 keeps a "robust knee at v\*" with the shape of the gate open ([Open: the gate shape (OP4)](../dark-matter/conjugate-matter/gate-shape.md)), and its prediction row 1 requires a "Knee at v\* ~ 10² km/s", but it does not restate the formula.

The two sources of the chain use different gate conventions. #1 writes its gate as e^{−k²/μ²} in the relative momentum k ([§3](../../notes/broken-born-theory.md#3-action)) and defines v\* from it ([§5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d)); calc note [#6 §4](../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) writes the overlap form e^{−(p₁−p₂)²/2μ²} in the momenta p₁ and p₂ of the two quanta and reads μ as the [fiber width](../phase-space/reciprocity/momentum-fibers.md#quanta-with-a-width-along-the-fiber). [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 17 records a suspected factor of √2 in μ between them: [#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) takes μ as #6's fiber width but uses #1's v\*, and in #6's convention the knee would sit at v\* = μ/m_χ. The flag, pending, notes that no stated number changes, with an executed check in [`review/wiki-build-checks/gate_conventions.py`](../../review/wiki-build-checks/gate_conventions.py). The flags' audit found the √2 present only if #6's form is read as the gate on the amplitude; #6 does not say. Read as the factor on the rate, it equals [#1 §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d)'s with #1's own μ, which #1's v0.4 addendum, [#8](../../notes/beta-coefficients.md), [#9](../../notes/broken-born-program-v1.md), [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) and the handoff identify with the fiber width, so [#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) is consistent under that convention, and the audit rated the flag as depending on it. This page quotes #13 as written.

### A length and a mass

The formula for v\* needs a mass. #13 labels the conjugate quantum by λ_χ "as ours are by mass" and, in the same bullet, divides by m_χ. It does not say how the two labels are related in the dual kinematics, which leads to the open question below.

## Open: the invariant length against the checkpoint's kinematics

The checkpoint describes the χ particles of conjugate matter in ordinary kinematics. In [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate), "χ propagates on g (equivalence principle; Bullet-Cluster-safe)" ([the equivalence principle](../gravity/spin-2-fields/equivalence-principle.md); [the Bullet Cluster](../dark-matter/halo-astrophysics/bullet-cluster.md)) and has a mass m_χ, and [#11 §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) lists [χ particles](../dark-matter/candidates/chi-particles.md) on those terms, as one of its three dark-matter candidates. The [withdrawn soliton manuscript](../dark-matter/candidates/soliton-candidate/obituary.md) [#14](../../notes/knot-dark-matter-standalone.md) did the same. The v3 worklog, comparing the two papers while #14 was being revised, recorded the mismatch as item O3:

> "#14 describes the dark sector entirely in our kinematics: GeV masses, 10⁻³ c drift, an ordinary massless dark photon moving at c. [#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) labels conjugate quanta by an invariant length λ instead of a mass, and a λ = 0 quantum would sit on the dual null cone with |dp/dt| = c̃. The papers were never reconciled."

The decision for #14's v3 was to "keep the dark sector in ordinary kinematics and say so explicitly"; #14 was later withdrawn on other grounds ([Obituary: #14's superheavy-soliton model](../dark-matter/candidates/soliton-candidate/obituary.md)). The worklog leaves one question to the dual dynamics:

> Whether the dark photon is m = 0, λ = 0, or both is part of #13's open "dual dynamics" item.

No document has reconciled the two descriptions since. By the wiki's order of precedence #11 governs for the χ candidate, and #13's reading stays an alternative ([conflicts between sources](../history/documents/source-conflicts.md)). The item is not among [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems)'s open problems or on the current queue; the worklog's instruction to settle #13's cones first is on [Open: the two dual cones](two-cones-inconsistency.md). The program's other open items are collected in [open problems and the queue](../status/open-problems.md).

The record holds a related gap. #11's third dark-matter candidate, [conjugate monopoles localized in momentum](../dark-matter/candidates/momentum-space-monopoles.md), P.R.'s open conjecture, has not been tested: #14's model "used ordinary kinematics throughout" ([#11 §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates)) and did not treat localization in momentum. The root [`CLAUDE.md`](../../CLAUDE.md) lists "the kinematics of momentum-polarized matter, never modeled" among the open items of the monopole discussion, not queued. Neither document relates that gap to #13's dual kinematics.

## λ_χ in the dual dynamics

- **The dual second law.** [#13 §5](../papers/conjugate-special-relativity.md#5-inertia-dualized): "The dual second law, structurally, makes λ_χ the measure of resistance to force-*change* [conjecture-tier; the full dual dynamics awaits the formalization of §6]." This would give λ_χ the role mass plays in Newton's second law ([dual inertia: the dual second law](dual-inertia.md#conjecture-the-dual-second-law)).
- **A chat-only question.** [`HANDOFF.md` §4](../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact), among the results that exist only in the original chat, ends its entry on two gravitational charges with "whether invariant length λ and dual charge lock together = 'dual equivalence principle' open question" ([two gravitational charges and the conjugate field equations (chat-only)](../gravity/momentum-graviton/chat-only-results.md)).

## The popular version

The popular article [#12](../../popsci/universes-other-half.md) ("A second speed of light") states the shell and the closure as settled: "particles of the other polarization carry an unchangeable size as ours carry an unchangeable mass, realizing Born's original 1938 ambition of a physics with a fundamental mass and a fundamental length on equal footing", and "the Planck length times c⁴/G is exactly the Planck energy". #12 presents the framework as if confirmed and is never a source for status ([the popular articles](../history/documents/popular-articles.md)).

## Basis of the status

- [`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen) lists "invariant length λ, Planck closure E = l_P·c⁴/G = E_Planck" among the alive results, without the ✓ it uses for machine-verified items, and the root [`CLAUDE.md`](../../CLAUDE.md) lists #13 as a current reference.
- #13 has not been revised in substance since its import on 2026-10-19, and no review round has covered it ([conjugate special relativity](_index.md)).
- #11 mentions neither the shell nor the closure.

## Sources

- [`wiki/papers/conjugate-special-relativity.md` §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) — the shell, Born's program, Planck closure and the gate-scale reading; [§1](../papers/conjugate-special-relativity.md#1-two-causal-cones) for c̃ = ℏc/λ² and λ² = ℏG/c³; [§5](../papers/conjugate-special-relativity.md#5-inertia-dualized) for λ_χ in the dual second law; [§6](../papers/conjugate-special-relativity.md#6-what-is-shared-what-is-broken-what-is-open) for the 3+1 presentation and the open four-dimensional map; [§7](../papers/conjugate-special-relativity.md#7-summary-of-tethers) for the fixed list and the anchor; References [3]†–[4]† for Born.
- [`wiki/papers/broken-born-checkpoint-v2.md` §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the gate F(k²/μ²), μ as the fiber width, the knee and χ on g; [§4](../papers/broken-born-checkpoint-v2.md#4-postulates) for P4; [§12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) for the χ candidate and for #14's ordinary kinematics, which left the third candidate untested; §13 row 1 for the knee; §14 items 4 and 10 for the gate shape and the literature battery.
- [`review/v3-worklog.md`](../../review/v3-worklog.md) 'New open items' — item O3: the unreconciled kinematics and the dark-photon question.
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 17 — the suspected √2 in μ between #1's and #6's gate conventions; check in [`review/wiki-build-checks/gate_conventions.py`](../../review/wiki-build-checks/gate_conventions.py).
- [`notes/gate-mechanism.md` §3](../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways) and [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 55 — μ ~ ℏ/λ_χ gives a form factor in q, not a gate in k; the mechanism's tag disputed (flag 55, pending).
- [`notes/broken-born-theory.md` §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d) — the definition v\* ≡ √2 μ/m_χ; [§3](../../notes/broken-born-theory.md#3-action) for the gate e^{−k²/μ²} (superseded as a reference).
- [`notes/x-classification.md` §4](../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — μ as the χ quantum's own momentum width.
- [`review/round3/referee/audit-notes.md`](../../review/round3/referee/audit-notes.md) Step 1 — the metadata check on Born 1938 and 1949.
- [`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen) — the alive listing; [§4](../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) for the chat-only "dual equivalence principle"; [§8 item 6](../../HANDOFF.md#8-ranked-next-actions-queue) for the † check of #13's references.
- [`CLAUDE.md`](../../CLAUDE.md) 'Since the handoff' — #13 as a current reference; the † battery in the queue; the kinematics of momentum-polarized matter, never modeled (not queued).
- [`popsci/universes-other-half.md`](../../popsci/universes-other-half.md) 'A second speed of light' — the popular statement (not a status source).
