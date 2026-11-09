---
title: "Open: the gate shape (OP4)"
weight: 60
status: open
description: "Whether the gate cuts off as a Gaussian or with a power-law tail depends, in #11 §14, on the X propagator on the momentum fibers; the answer is now observable in the knee's tail."
provenance: [O]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 4"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 rows 1 and 3"
  - "wiki/papers/broken-born-checkpoint-v2.md References [26]"
  - "notes/geometric-core.md §E"
  - "notes/geometric-core.md §D"
  - "notes/x-classification.md §4"
  - "notes/x-classification.md §5"
  - "notes/x-classification.md §1"
  - "notes/beta-coefficients.md §5"
  - "notes/broken-born-program-v1.md §10 item 3"
  - "notes/broken-born-theory.md §11 item 2"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/wave-island.md 'The rate'"
  - "HANDOFF.md §2"
  - "CLAUDE.md 'Since the handoff'"
  - "review/wiki-build-flags.md items 17, 55"
  - "review/wiki-build-checks/gate_conventions.py"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §3"
  - "notes/gate-mechanism.md §5"
  - "notes/gate-mechanism.md §6"
  - "verify/gate_mechanism.py"
---

*The gate shape is the exact form of the function F that turns off the self-interaction of [conjugate matter](_index.md) at large relative velocity. A Gaussian F falls off faster than any power of the velocity; a rational F, a ratio of polynomials, falls off as a power law. In the record, which one holds depends on how the [momentum graviton X](../../gravity/momentum-graviton/_index.md) propagates along the momentum directions of phase space, and on the profile of a single conjugate quantum along those directions; neither has been computed. The question is open, and it is observable: [#11](../../papers/broken-born-checkpoint-v2.md) writes the tail of the knee in the self-interaction cross-section with the same letter F. The checkpoint counts the tail, not yet forced by any derivation, among the program's risks of degeneration. A note of 2026-10-28 goes further: it finds that exchanging X cannot produce the gate at all, that the propagator along the momentum directions has no meaning in the program's construction of X, and that the choice between Gaussian and rational is not a choice between two kinds of gate (flag 55, pending).*

**Status:** Open — [O] ([`wiki/papers/broken-born-checkpoint-v2.md` §14 item 4](../../papers/broken-born-checkpoint-v2.md#14-open-problems)) — the record holds no calculation of it; [#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment) lists "gate tail not yet forced" among the degeneration risks. It qualifies [the velocity gate](velocity-gate.md), whose mechanism is [D] in [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) and whose shape is this item. [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate, and flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism ([the gate mechanism](gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). The note also finds that this item, as worded, does not cover the gap ([below](#what-the-gate-mechanism-note-adds)). [`verify/gate_mechanism.py`](../../../verify/gate_mechanism.py) reruns the note's arithmetic and algebra, on which the [V] of its tags below rests, and does not test its physics ([the gate-mechanism script](../../method/verification/gate-mechanism-script.md)). It is listed in [open problems](../../status/open-problems.md) and is not on the current work queue.

## The question

[The checkpoint](../../history/documents/checkpoint.md), #11, lists it as item 4 of its open problems:

> "Gate shape (X propagator on momentum fibers; Gaussian vs rational — now observable) [O]." ([#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems))

The gate is the factor F in conjugate matter's self-interaction amplitude, M(k, q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²), where k is the incoming relative momentum of the pair and μ the momentum width of a χ quantum ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)). #11 tags the claim "[D — mechanism; shape [O]]": exchange of X over the overlap of two quanta's momentum-space wavepackets explains why the interaction depends on k ([the gate mechanism](gate-mechanism.md)), but not what function of k/μ it is. That the mechanism explains even the dependence on k is disputed (not derived, according to flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending; [the gate mechanism](gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). In the [transfer cross-section](../halo-astrophysics/transfer-cross-section.md) #11 writes the same letter as the tail of [the gated scattering law](scattering-law.md), σ_T(v) = σ₀F(v²/v\*²), whose "tail (Gaussian vs rational) diagnoses the vertex completion" ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)).

The first consolidation, v1, words the item as "Gate shape: the X propagator on momentum fibers; Gaussian vs rational tail (now doubly motivated — it is observable) [O]" ([#9 §10 item 3](../../../notes/broken-born-program-v1.md#10-open-problems)), and [the handoff](../../history/documents/handoff.md) as "Gate shape (X propagator on momentum fibers)" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen), Open 6).

## Background: Gaussian and power-law tails [T]

The two candidates differ in how fast the gate dies away once the relative momentum exceeds μ.

- A **Gaussian**, e^{−x²}, falls faster than any power of x. Beyond a few widths it is negligible.
- A **rational function**, a ratio of polynomials such as 1/(1 + x²)ⁿ, falls as a fixed power of x at large x. Its tail stays measurable much further out.

Both shapes occur in scattering off extended objects. The form factor of an object is the [Fourier transform](../../phase-space/reciprocity/fourier-transform.md) of its density profile: a Gaussian profile gives a Gaussian form factor, while a profile with an exponential edge gives a rational one, which is how the proton's charge form factor is usually described [T]. A propagator, such as 1/(q² + M²) for a field of mass M, is itself a rational function, and tree-level amplitudes, built from propagators and polynomial vertices, are rational functions of the momenta [T]. A Gaussian cannot come out of such an amplitude unless it is put in through the external states.

## Where the shape is decided

The calc notes locate the shape in two places.

- **The X propagator on the [momentum fibers](../../phase-space/reciprocity/momentum-fibers.md#the-x-propagator-on-the-fibers-op4).** [Calc note #5](../../history/documents/field-equation-notes.md), which first identified the gate's carrier as X: "The gate *shape* is the X propagator's structure on the momentum fibers — open [O], and downstream of the §D classification (outcome 2 gives it most cheaply)" ([`notes/geometric-core.md` §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural)). The momentum fibers are the momentum directions of phase space attached to each point of spacetime. Outcome 2 was an auxiliary X with no derivatives, which would have given a contact, momentum-structured interaction directly; calc note [#6](../../../notes/x-classification.md) excluded it, because constant shifts of X are exact symmetries, so "X appears only through derivatives, so it propagates or it doesn't exist" ([§1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous); [shift symmetry](../../gravity/momentum-graviton/shift-symmetry.md)). That route is closed, and X is a propagating massive field whose propagator on the fibers no document writes down.
- **The fiber profile and the vertex.** Calc note #6 gives the two candidates: "Wavepacket overlap of Gaussian profiles gives exactly e^{−(p₁−p₂)²/2μ²} — the postulated gate, with **μ = the χ quantum's own p-width**, a physical identification the EFT lacked. *However*: tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" ([`notes/x-classification.md` §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)). EFT is effective field theory, here [the lab notebook](../../history/documents/lab-notebook.md)'s v0.1 amplitude. The note's closing list of open items ties the Gaussian case to the metastring, the framework of Freidel, Leigh and Minic's "Metastring theory and modular space-time", which #11 cites as ref. [26][S] ([Born structures](../../phase-space/born-geometry/born-structures.md)): "gate-shape completion (Gaussian fiber profile — ties to the metastring's modular vertex structure)" ([§5](../../papers/broken-born-checkpoint-v2.md#5-the-kinematic-core-and-the-compatibility-theorem)). Calc note #6 gives no reference for the vertex structure ([references](../../references.md)).

Calc note #6 writes its Gaussian in the momenta p₁ and p₂ of the two quanta, while the lab notebook's postulated gate, e^{−k²/μ²}, is written in the incoming relative momentum k = m_χv_rel/2, with v_rel the pair's relative velocity ([#1 §3](../../../notes/broken-born-theory.md#3-action)); no source converts one exponent into the other ([two conventions, not reconciled](velocity-gate.md#two-conventions-not-reconciled)). [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 17 records a suspected factor of √2 in μ between the two forms: with p₁ − p₂ = 2k, #6's fiber width would put the knee at v\* = μ/m_χ rather than at the lab notebook's v\* ≡ √2μ/m_χ ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)). The flag, pending, notes that no stated number changes; its executed check is [`review/wiki-build-checks/gate_conventions.py`](../../../review/wiki-build-checks/gate_conventions.py). This page quotes both forms as written. The suspected factor concerns the width of the Gaussian form, not the choice between Gaussian and rational tails that this page is about.

A resolution would therefore need the χ–X vertex, the X propagator along the fibers and the χ quantum's profile there. [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) and [#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) call the missing piece "the vertex completion".

## What the gate-mechanism note adds

[`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28, not reviewed) takes up the mechanism this item presupposes and finds that it does not deliver the gate (flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending). Four of its findings bear on the shape question.

- **The item does not cover the gap.** "§14 item 4 does not cover the gap. It treats the mechanism as settled, presupposes an X propagator on the fibers that §7 does not have, and its Gaussian-against-rational split is not a dichotomy of gates in k (§3)" (§5).
- **No propagator on the fibers.** The [section condition](../../symmetry-breaking/section-condition.md) "makes H_Z, and with it X, depend on x only. The fiber metric is constant along each fiber, so 'X propagator on momentum fibers' has no meaning within §7" (§3) [D, record audit]. No χχX vertex, χ fiber profile, formula for the dual stress or overlap integral exists in the record either (§3).
- **What the rational gates are.** "The rationality of tree amplitudes sits in the transfer: the propagator 1/(q² + M_X²) and form factors in t. Integrated over angle these give a light mediator's knee in σ_T(v) with a power-law tail. That is [#11 §13 row 1](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)'s 'standard expectation' column, not a gate in k" (§3; both derivations) [D][V]. Exchanging X itself gives, at fixed transfer, an amplitude that depends on k only as a polynomial of degree at most two in k², with no denominator in k (§2) [D][V].
- **Neither tail comes from X as written.** Read as an exact amplitude with a t-channel pole, [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)'s form h(t)F(k²/μ²) "needs every spin": the Gaussian and the rational F both have nonzero Legendre coefficients at every order computed, l = 0–6; the first derivation reaches the same from the other side, through a tower of spins ([§2](../../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification)) [D][V][T]. In the note's two reconstructions of [#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)'s fiber overlap, reading R1 is an ordinary short-range potential whose cross-section tails are power laws even for Gaussian profiles, "contrary to [#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)" (one derivation), and reading R2, a pair-channel interaction, falls faster than any power of k but has no X pole (one derivation) (§3). Both readings are the note's reconstruction; the theorems about each are derived ([the fiber overlap, read two ways](gate-mechanism.md#the-fiber-overlap-read-two-ways)).

The note's open items that would replace this one, if the flag is accepted, include whether the program keeps the gate as a postulate or rewrites χ's self-interaction as reading R1's position-local potential "of range ~10 pm, which is ordinary short-range self-interacting dark matter with power-law tails and would remove the program-specific content of rows 1–3"; whether any construction tied to the program's geometry yields a pair-channel form factor for χχ; and, if a Gaussian form factor in s is kept, "whether microcausality and unitarity are acceptable at the nonlocality scale ħ/μ ≈ 10 pm" (§5) [O].

## Why it is observable

Before the record gave the gate a mechanism, the lab notebook took the shape as Gaussian and drew from it an exponential cliff in the cross-section. Calc note #6 weakened the cliff to a knee: "The knee's existence and location are robust; its steepness is model-internal information, not a guaranteed exponential" ([§4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)). Calc note [#8](../../../notes/beta-coefficients.md)'s close-out of the gate problem then lists the shape as "shape completion open (Gaussian vs rational tail — now also an observable discriminant)" ([`notes/beta-coefficients.md` §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out)).

The tail is measurable in the velocity dependence of dark-matter self-scattering:

- **[Row 1](../../predictions/self-interaction-knee.md)** requires a knee at "v\* ~ 10² km/s" and is killed by "Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)). A Gaussian tail makes self-interaction above the knee negligible; a rational tail leaves a power-law remainder. The kill condition does not say how large a remainder counts as robust. Two published fits mildly prefer a nonzero cross-section at cluster speeds, which the literature-check note does not count as robust (flag 69 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending).
- **[Row 3, the island discriminant](../../predictions/island-discriminant.md)** reads the tail as "Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)). The (v\*/σ)⁴ law, with σ the halo's [velocity dispersion](../halo-astrophysics/velocity-dispersion.md#row-3-the-island-discriminant), is the suppression of [the gated condensation rate](../momentum-clumping/wave-island/condensation-rate.md) when χ is a classical wave ([`notes/wave-island.md`](../../../notes/wave-island.md), 'The rate').
- In #11's comparison of the dark-matter candidates, [χ particles](../candidates/chi-particles.md) have "knee at v\*, sharp tail" and [the X-condensate](../candidates/x-condensate.md) "knee shape wave-like" ([#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model)).

Row 3's particle side assumes a sharp tail, which is the Gaussian case of this open problem. Calc note #6 calls the rational gates power-law-tailed, and the wave-island law is also a power law. No source compares the two power laws or says whether the discriminant survives a rational tail for particles. [`notes/gate-mechanism.md` §5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record) lists the question as open [O]: "Under reading R1 the particle tail is a power law, the same functional class as the wave island's. Whether the discriminant survives is open."

## What depends on it

- **The lab notebook's numbers above the gate.** "σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0" and "Cluster self-interaction is *identically zero at any future sensitivity*" ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)) were computed from the Gaussian. They hold only if the tail is Gaussian ([the scattering benchmark](benchmark.md)).
- **The particle side of the island discriminant**, as above.
- **The steepness of the knee in row 1.** The existence and location of the knee do not depend on the shape; how sharply the cross-section falls beyond it does.

The emphasis has moved since v0.1. The lab notebook's open-problem list read: "The σ(v) *cliff* is robust to the exact shape; the sub-v\* profile is not" ([#1 §11 item 2](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity)). Since the v0.4 downgrade the knee has been the robust part, and the steepness of the fall beyond it, which v0.1 took as given, has been part of the open question.

## History

1. **v0.1.** The lab notebook postulated the Gaussian e^{−k²/μ²} and listed its derivation as open problem 2: "obtain e^{−k²/μ²} (or its true form) from S_H + S_mix rather than postulating it" ([#1 §11 item 2](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity)), where S_H is the geometric action and S_mix a mixing term the notebook does not write out ([the lab notebook](../../history/documents/lab-notebook.md)).
2. **v0.3 and calc note [#5](../../../notes/geometric-core.md).** The notebook's addendum names the mechanism as X exchange; "the shape awaits the X propagator" (#1 'Addendum (v0.3, overnight)'), and [#5 §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) made the shape the propagator's structure on the fibers.
3. **v0.4 and calc note #6.** μ became the χ quantum's fiber width, "with a Gaussian gate iff the fiber profile is Gaussian" (#1 'Addendum (v0.4)'), and the cliff became a knee whose tail is a diagnostic.
4. **Calc note #8 and v1.** #8 closed the gate problem as "mechanism found", with the shape open, "now also an observable discriminant" ([#8 §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out); [the three main problems](../../history/main-problems.md)); v1 listed it as item 3 of its open problems, "now doubly motivated — it is observable" ([#9 §10](../../../notes/broken-born-program-v1.md#10-open-problems)).
5. **The checkpoint.** #11 lists it as item 4 of [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) and as a degeneration risk in [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment).
6. **The gate-mechanism note (2026-10-28).** It finds that exchanging [#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate and that this item does not cover the gap; flag 55, pending, proposes [P] for the gate and μ and [O] for the mechanism ([above](#what-the-gate-mechanism-note-adds)).

The current queue, in the root [`CLAUDE.md`](../../../CLAUDE.md) ("Since the handoff"), holds [the partially-massless comparison](../../gravity/palindromic-branch/pm-comparison.md) and [the literature battery](../../method/literature-battery.md), then an optional review round of [the toy-model note](../../symmetry-breaking/toy-models/_index.md). The gate shape is not on it.

## Its weight in the assessment

#11's assessment, framed in the terms of Lakatos's methodology of research programs ([Lakatosian methodology](../../method/lakatosian-methodology.md)), sorts the program's features into progressive signs and degeneration risks. Among the risks it lists "gate tail not yet forced" ([#11 §15](../../papers/broken-born-checkpoint-v2.md#15-assessment); [the assessment](../../program/assessment.md)). The same section counts the knee-shape discriminant among the program's new experimental questions, so the item sits on both sides: the tail is an observable the program proposes, and the program has not yet derived what it should be.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §14 item 4](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open item; [§15](../../papers/broken-born-checkpoint-v2.md#15-assessment) — the degeneration risk and the knee-shape discriminant; [§8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the tail as a vertex diagnostic; [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) — the candidates' handles; [§13 rows 1](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) and 3 — the knee and the island discriminant; References [26] — the metastring paper
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the current queue
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — the item in the handoff's open list
- [`notes/broken-born-program-v1.md` §10 item 3](../../../notes/broken-born-program-v1.md#10-open-problems) — v1's wording of the item
- [`notes/geometric-core.md` §E](../../../notes/geometric-core.md#e-the-gate-problem--the-mechanism-found-d--structural) — the shape as the X propagator's structure on the fibers; [§D](../../../notes/geometric-core.md#d-quadratic-spectrum-and-the-ghost-question-partial) — the auxiliary outcome
- [`notes/x-classification.md` §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — Gaussian versus rational gates, the knee; [§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — the metastring tie; [§1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous) — the auxiliary route closed
- [`notes/beta-coefficients.md` §5](../../../notes/beta-coefficients.md#5-what-remains-honest-close-out) — the shape as an observable discriminant
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'The rate' — the (v\*/σ)⁴ suppression on the wave island
- [`notes/broken-born-theory.md` §11 item 2](../../../notes/broken-born-theory.md#11-open-problems-in-order-of-severity) — the v0.1 open problem; [§3](../../../notes/broken-born-theory.md#3-action) — the postulated gate in the relative momentum k; [§5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d) — the Gaussian-tail cluster numbers and the definition of v\*; 'Addendum (v0.3, overnight)', 'Addendum (v0.4)' — the mechanism and the fiber width
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 17 — the suspected √2 in μ between the two gate conventions, pending; check in [`review/wiki-build-checks/gate_conventions.py`](../../../review/wiki-build-checks/gate_conventions.py); item 55 — the mechanism not derived, pending
- [`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate) — the polynomial in k², the exact-amplitude form needs every spin; [§3](../../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways) — the record audit, no propagator on the fibers, what the rational gates are, readings R1 and R2 and their tails; [§5](../../../notes/gate-mechanism.md#5-what-follows-for-the-record) — §14 item 4 does not cover the gap, and what becomes open; [§6](../../../notes/gate-mechanism.md#6-record) — what the script tests
- [`verify/gate_mechanism.py`](../../../verify/gate_mechanism.py) — reruns the note's arithmetic and algebra ([the gate-mechanism script](../../method/verification/gate-mechanism-script.md))
