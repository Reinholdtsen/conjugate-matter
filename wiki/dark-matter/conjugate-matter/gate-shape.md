---
title: "Open: the gate shape (OP4)"
weight: 60
status: open
description: "Whether the gate cuts off as a Gaussian or with a power-law tail depends on the X propagator on the momentum fibers; the answer is now observable in the knee's tail."
provenance: [O]
sources:
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13 rows 1 and 3"
  - "papers/broken-born-checkpoint-v2.md References [26]"
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
---

*The gate shape is the exact form of the function F that turns off the self-interaction of [conjugate matter](/wiki/dark-matter/conjugate-matter) at large relative velocity. A Gaussian F falls off faster than any power of the velocity; a rational F, a ratio of polynomials, falls off as a power law. Which one holds depends on how the [momentum graviton X](/wiki/gravity/momentum-graviton) propagates along the momentum directions of phase space, and on the profile of a single conjugate quantum along those directions; neither has been computed. The question is open, and it is observable: the tail of the knee in the self-interaction cross-section is the same function. The checkpoint counts the tail, not yet forced by any derivation, among the program's risks of degeneration. A note of 2026-10-28 goes further: it finds that exchanging X cannot produce the gate at all, that the propagator along the momentum directions has no meaning in the program's construction of X, and that the choice between Gaussian and rational is not a choice between two kinds of gate; this awaits Paul's ruling.*

**Status:** Open — [O] (`papers/broken-born-checkpoint-v2.md` §14 item 4) — no calculation exists; #11 §15 lists "gate tail not yet forced" among the degeneration risks. It qualifies [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), whose mechanism is [D] in #11 §8 and whose shape is this item. `notes/gate-mechanism.md` (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging #11 §7's X cannot produce the gate, and flag 55 in `review/wiki-build-flags.md` proposes [P] for the gate and μ and [O] for the mechanism, pending Paul's ruling; #11 is unchanged ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The note also finds that this item, as worded, does not cover the gap ([below](#what-the-gate-mechanism-note-adds)). It is listed in [open problems](/wiki/status/open-problems) and is not on the current work queue.

## The question

[The checkpoint](/wiki/history/documents/checkpoint), #11, lists it as item 4 of its open problems:

> "Gate shape (X propagator on momentum fibers; Gaussian vs rational — now observable) [O]." (#11 §14)

The gate is the factor F in conjugate matter's self-interaction amplitude, M(k, q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²), where k is the incoming relative momentum of the pair and μ the momentum width of a χ quantum (#11 §8). #11 tags the claim "[D — mechanism; shape [O]]": exchange of X over the overlap of two quanta's momentum-space wavepackets explains why the interaction depends on k ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)), but not what function of k/μ it is. That the mechanism explains even the dependence on k is disputed (not derived, according to flag 55 in `review/wiki-build-flags.md`, pending Paul's ruling; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). In the [transfer cross-section](/wiki/dark-matter/halo-astrophysics/transfer-cross-section) the same function appears as the tail of [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law), σ_T(v) = σ₀F(v²/v\*²), whose "tail (Gaussian vs rational) diagnoses the vertex completion" (#11 §8).

The first consolidation, v1, words the item as "Gate shape: the X propagator on momentum fibers; Gaussian vs rational tail (now doubly motivated — it is observable) [O]" (#9 §10 item 3), and [the handoff](/wiki/history/documents/handoff) as "Gate shape (X propagator on momentum fibers)" (`HANDOFF.md` §2, Open 6).

## Background: Gaussian and power-law tails [T]

The two candidates differ in how fast the gate dies away once the relative momentum exceeds μ.

- A **Gaussian**, e^{−x²}, falls faster than any power of x. Beyond a few widths it is negligible.
- A **rational function**, a ratio of polynomials such as 1/(1 + x²)ⁿ, falls as a fixed power of x at large x. Its tail stays measurable much further out.

Both shapes occur in scattering off extended objects. The form factor of an object is the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of its density profile: a Gaussian profile gives a Gaussian form factor, while a profile with an exponential edge gives a rational one, which is how the proton's charge form factor is usually described [T]. A propagator, such as 1/(q² + M²) for a field of mass M, is itself a rational function, and tree-level amplitudes, built from propagators and polynomial vertices, are rational functions of the momenta [T]. A Gaussian cannot come out of such an amplitude unless it is put in through the external states.

## Where the shape is decided

The calc notes locate the shape in two places.

- **The X propagator on the [momentum fibers](/wiki/phase-space/reciprocity/momentum-fibers#the-x-propagator-on-the-fibers-op4).** [Calc note #5](/wiki/history/documents/field-equation-notes), which first identified the gate's carrier as X: "The gate *shape* is the X propagator's structure on the momentum fibers — open [O], and downstream of the §D classification (outcome 2 gives it most cheaply)" (`notes/geometric-core.md` §E). The momentum fibers are the momentum directions of phase space attached to each point of spacetime. Outcome 2 was an auxiliary X with no derivatives, which would have given a contact, momentum-structured interaction directly; calc note #6 excluded it, because constant shifts of X are exact symmetries, so "X appears only through derivatives, so it propagates or it doesn't exist" (§1; [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)). That route is closed, and X is a propagating massive field whose propagator on the fibers no document writes down.
- **The fiber profile and the vertex.** Calc note #6 gives the two candidates: "Wavepacket overlap of Gaussian profiles gives exactly e^{−(p₁−p₂)²/2μ²} — the postulated gate, with **μ = the χ quantum's own p-width**, a physical identification the EFT lacked. *However*: tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" (`notes/x-classification.md` §4). EFT is effective field theory, here [the lab notebook](/wiki/history/documents/lab-notebook)'s v0.1 amplitude. The note's closing list of open items ties the Gaussian case to the metastring, the framework of Freidel, Leigh and Minic's "Metastring theory and modular space-time", which #11 cites as ref. [26][S] ([Born structures](/wiki/phase-space/born-geometry/born-structures)): "gate-shape completion (Gaussian fiber profile — ties to the metastring's modular vertex structure)" (§5). Calc note #6 gives no reference for the vertex structure ([references](/wiki/references)).

Calc note #6 writes its Gaussian in the momenta p₁ and p₂ of the two quanta, while the lab notebook's postulated gate, e^{−k²/μ²}, is written in the incoming relative momentum k = m_χv_rel/2, with v_rel the pair's relative velocity (#1 §3); no source converts one exponent into the other ([two conventions, not reconciled](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)). `review/wiki-build-flags.md` item 17 records a suspected factor of √2 in μ between the two forms: with p₁ − p₂ = 2k, #6's fiber width would put the knee at v\* = μ/m_χ rather than at the lab notebook's v\* ≡ √2μ/m_χ (#1 §5.1). The flag notes that no stated number changes; its executed check is `review/wiki-build-checks/gate_conventions.py`, and it awaits Paul's ruling. This page quotes both forms as written. The suspected factor concerns the width of the Gaussian form, not the choice between Gaussian and rational tails that this page is about.

A resolution would therefore need the χ–X vertex, the X propagator along the fibers and the χ quantum's profile there. #11 §8 and #6 §4 call the missing piece "the vertex completion".

## What the gate-mechanism note adds

`notes/gate-mechanism.md` (2026-10-28, not reviewed) takes up the mechanism this item presupposes and finds that it does not deliver the gate (flag 55 in `review/wiki-build-flags.md`, awaiting Paul's ruling). Four of its findings bear on the shape question.

- **The item does not cover the gap.** "§14 item 4 does not cover the gap. It treats the mechanism as settled, presupposes an X propagator on the fibers that §7 does not have, and its Gaussian-against-rational split is not a dichotomy of gates in k (§3)" (§5).
- **No propagator on the fibers.** The [section condition](/wiki/symmetry-breaking/section-condition) "makes H_Z, and with it X, depend on x only. The fiber metric is constant along each fiber, so 'X propagator on momentum fibers' has no meaning within §7" (§3) [D, record audit]. No χχX vertex, χ fiber profile, formula for the dual stress or overlap integral exists in the record either (§3).
- **What the rational gates are.** "The rationality of tree amplitudes sits in the transfer: the propagator 1/(q² + M_X²) and form factors in t. Integrated over angle these give a light mediator's knee in σ_T(v) with a power-law tail. That is #11 §13 row 1's 'standard expectation' column, not a gate in k" (§3; both derivations) [D][V]. Exchanging X itself gives, at fixed transfer, an amplitude that depends on k only as a polynomial of degree at most two in k², with no denominator in k (§2) [D][V].
- **Neither tail comes from X as written.** Read as an exact amplitude with a t-channel pole, #11 §8's form h(t)F(k²/μ²) "needs every spin": the Gaussian and the rational F both have nonzero Legendre coefficients at every order computed, l = 0–6; the first derivation reaches the same from the other side, through a tower of spins (§2) [D][V][T]. In the note's two reconstructions of #6 §4's fiber overlap, reading R1 is an ordinary short-range potential whose cross-section tails are power laws even for Gaussian profiles, "contrary to #6 §4" (one derivation), and reading R2, a pair-channel interaction, falls faster than any power of k but has no X pole (one derivation) (§3). Both readings are the note's reconstruction; the theorems about each are derived ([the fiber overlap, read two ways](/wiki/dark-matter/conjugate-matter/gate-mechanism#the-fiber-overlap-read-two-ways)).

The note's open items that replace this one, if Paul accepts the flag, include whether the program keeps the gate as a postulate or rewrites χ's self-interaction as reading R1's position-local potential "of range ~10 pm, which is ordinary short-range self-interacting dark matter with power-law tails and would remove the program-specific content of rows 1–3"; whether any construction tied to the program's geometry yields a pair-channel form factor for χχ; and, if a Gaussian form factor in s is kept, "whether microcausality and unitarity are acceptable at the nonlocality scale ħ/μ ≈ 10 pm" (§5) [O].

## Why it is observable

Before the gate's mechanism was derived, the lab notebook took the shape as Gaussian and drew from it an exponential cliff in the cross-section. Calc note #6 weakened the cliff to a knee: "The knee's existence and location are robust; its steepness is model-internal information, not a guaranteed exponential" (§4). Calc note #8's close-out of the gate problem then lists the shape as "shape completion open (Gaussian vs rational tail — now also an observable discriminant)" (`notes/beta-coefficients.md` §5).

The tail is measurable in the velocity dependence of dark-matter self-scattering:

- **[Row 1](/wiki/predictions/self-interaction-knee)** requires a knee at "v\* ~ 10² km/s" and is killed by "Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band" (#11 §13). A Gaussian tail makes self-interaction above the knee negligible; a rational tail leaves a power-law remainder. The kill condition does not say how large a remainder counts as robust.
- **[Row 3, the island discriminant](/wiki/predictions/island-discriminant)** reads the tail as "Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave" (#11 §13). The (v\*/σ)⁴ law, with σ the halo's [velocity dispersion](/wiki/dark-matter/halo-astrophysics/velocity-dispersion#row-3-the-island-discriminant), is the suppression of [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) when χ is a classical wave (`notes/wave-island.md`, 'The rate').
- In #11's comparison of the two dark-matter candidates, [χ particles](/wiki/dark-matter/candidates/chi-particles) have "knee at v\*, sharp tail" and [the X-condensate](/wiki/dark-matter/candidates/x-condensate) "knee shape wave-like" (#11 §12).

Row 3's particle side assumes a sharp tail, which is the Gaussian case of this open problem. Calc note #6 calls the rational gates power-law-tailed, and the wave-island law is also a power law. No source compares the two power laws or says whether the discriminant survives a rational tail for particles. `notes/gate-mechanism.md` §5 lists the question as open [O]: "Under reading R1 the particle tail is a power law, the same functional class as the wave island's. Whether the discriminant survives is open."

## What depends on it

- **The lab notebook's numbers above the gate.** "σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0" and "Cluster self-interaction is *identically zero at any future sensitivity*" (#1 §5.1) were computed from the Gaussian. They hold only if the tail is Gaussian ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)).
- **The particle side of the island discriminant**, as above.
- **The steepness of the knee in row 1.** The existence and location of the knee do not depend on the shape; how sharply the cross-section falls beyond it does.

The emphasis has moved since v0.1. The lab notebook's open-problem list read: "The σ(v) *cliff* is robust to the exact shape; the sub-v\* profile is not" (#1 §11 item 2). Since the v0.4 downgrade the knee is the robust part, and the steepness of the fall beyond it, which v0.1 took as given, is part of the open question.

## History

1. **v0.1.** The lab notebook postulated the Gaussian e^{−k²/μ²} and listed its derivation as open problem 2: "obtain e^{−k²/μ²} (or its true form) from S_H + S_mix rather than postulating it" (#1 §11 item 2), where S_H is the geometric action and S_mix a mixing term the notebook does not write out ([the lab notebook](/wiki/history/documents/lab-notebook)).
2. **v0.3 and calc note #5.** The mechanism was identified as X exchange; "the shape awaits the X propagator" (#1 'Addendum (v0.3, overnight)'), and #5 §E made the shape the propagator's structure on the fibers.
3. **v0.4 and calc note #6.** μ became the χ quantum's fiber width, "with a Gaussian gate iff the fiber profile is Gaussian" (#1 'Addendum (v0.4)'), and the cliff became a knee whose tail is a diagnostic.
4. **Calc note #8 and v1.** The gate problem closed with the mechanism found and the shape open, "now also an observable discriminant" (#8 §5; [the three main problems](/wiki/history/main-problems)); v1 listed it as item 3 of its open problems, "now doubly motivated — it is observable" (#9 §10).
5. **The checkpoint.** #11 lists it as item 4 of §14 and as a degeneration risk in §15.
6. **The gate-mechanism note (2026-10-28).** It finds that exchanging #11 §7's X cannot produce the gate and that this item does not cover the gap; flag 55 proposes [P] for the gate and μ and [O] for the mechanism. #11 is unchanged until Paul rules ([above](#what-the-gate-mechanism-note-adds)).

The current queue, in the root `CLAUDE.md` ("Since the handoff"), holds [the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison) and [the literature battery](/wiki/method/literature-battery), then an optional review round of [the toy-model note](/wiki/symmetry-breaking/toy-models). The gate shape is not on it.

## Its weight in the assessment

#11's assessment, framed in the terms of Lakatos's methodology of research programs ([Lakatosian methodology](/wiki/method/lakatosian-methodology)), sorts the program's features into progressive signs and degeneration risks. Among the risks it lists "gate tail not yet forced" (#11 §15; [the assessment](/wiki/program/assessment)). The same section counts the knee-shape discriminant among the program's new experimental questions, so the item sits on both sides: the tail is an observable the program proposes, and the program has not yet derived what it should be.

## Sources

- `papers/broken-born-checkpoint-v2.md` §14 item 4 — the open item; §15 — the degeneration risk and the knee-shape discriminant; §8 — the tail as a vertex diagnostic; §12 — the candidates' handles; §13 rows 1 and 3 — the knee and the island discriminant; References [26] — the metastring paper
- `CLAUDE.md` 'Since the handoff' — the current queue
- `HANDOFF.md` §2 — the item in the handoff's open list
- `notes/broken-born-program-v1.md` §10 item 3 — v1's wording of the item
- `notes/geometric-core.md` §E — the shape as the X propagator's structure on the fibers; §D — the auxiliary outcome
- `notes/x-classification.md` §4 — Gaussian versus rational gates, the knee; §5 — the metastring tie; §1 — the auxiliary route closed
- `notes/beta-coefficients.md` §5 — the shape as an observable discriminant
- `notes/wave-island.md` 'The rate' — the (v\*/σ)⁴ suppression on the wave island
- `notes/broken-born-theory.md` §11 item 2 — the v0.1 open problem; §3 — the postulated gate in the relative momentum k; §5.1 — the Gaussian-tail cluster numbers and the definition of v\*; 'Addendum (v0.3, overnight)', 'Addendum (v0.4)' — the mechanism and the fiber width
- `review/wiki-build-flags.md` item 17 — the suspected √2 in μ between the two gate conventions, awaiting a ruling; check in `review/wiki-build-checks/gate_conventions.py`; item 55 — the mechanism not derived, awaiting a ruling
- `notes/gate-mechanism.md` §2 — the polynomial in k², the exact-amplitude form needs every spin; §3 — the record audit, no propagator on the fibers, what the rational gates are, readings R1 and R2 and their tails; §5 — §14 item 4 does not cover the gap, and what becomes open
