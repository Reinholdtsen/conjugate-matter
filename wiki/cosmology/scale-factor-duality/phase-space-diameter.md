---
title: "The phase-space diameter relation (chat-only)"
weight: 70
status: conjecture
description: "D_x·D_p = h·N^{1/3} per dimension, a 'cosmic time–bandwidth theorem' whose rectangle is square at the bounce; chat-only, and queued for a note."
sources:
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "CLAUDE.md 'Since the handoff'"
---

*The phase-space diameter relation is a conjecture from the program's original chat sessions: the diameter of the universe in position space, multiplied by its diameter in momentum space, equals Planck's constant times a large number fixed by how many photons the universe contains. It is a cosmological counterpart of the time–bandwidth product of signal analysis, which says that a pulse cannot be both very short and very narrow in frequency. The relation exists only in the chat, as summarized by the [handoff document](/wiki/history/documents/handoff): no paper or note derives it and no script checks its numbers. A short note on it is in the current work queue.*

**Status:** Conjecture (chat-only) — untagged; the handoff calls it "Conjecture-tier" — no derivation in any document, no `verify/` script, absent from #11; queued as a note (root `CLAUDE.md`, current queue item 1). Listed on [conjectures](/wiki/status/conjectures).

## Statement

The whole record of the relation is one bullet of `HANDOFF.md` §4, "Results that exist only in the chat (not in any artifact)" (the heading's "only" is set in capitals in the source):

> Phase-space diameter relation: D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem); the constant = the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension); rectangle square (D_x = D_p in Planck units) exactly at the bounce; aspect ratio today ~10⁹² = a clock measuring distance from self-duality. Conjecture-tier; candidate for a future note.

The bullet makes four claims:

1. **The product.** The universe's extent in position, D_x, times its extent in momentum, D_p, equals Planck's constant h times N^{1/3}, along each of the three dimensions.
2. **The constant.** N is "the universe's photon count/entropy", given as ~10⁹⁰, so that the product is "~10³⁰ h per dimension".
3. **The square.** In Planck units the "rectangle" D_x × D_p is square, D_x = D_p, "exactly at the bounce".
4. **The clock.** Its "aspect ratio today ~10⁹²" is "a clock measuring distance from self-duality".

The handoff does not define D_x and D_p beyond their names, does not say what N counts beyond "photon count/entropy", and gives no derivation.

## Background: the time–bandwidth product [T]

A signal that lasts a time Δt and occupies a band of frequencies Δf cannot make both small: the product Δt·Δf has a lower bound of order one, reached by Gaussian pulses (Gabor 1946 †). The bound is a property of the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform), which relates a waveform to its spectrum. Stretching a pulse in time narrows its spectrum by the same factor, so the product is unchanged.

Quantum mechanics carries the same structure, because the Fourier transform also relates a particle's description in position to its description in momentum, as a rotation of phase space. The position–momentum version is the uncertainty principle, and the area of phase space one quantum state occupies is of order h per position–momentum pair ([the canonical commutator and the uncertainty principle](/wiki/phase-space/reciprocity/canonical-commutator)) [T]. A system of many quanta needs correspondingly many such cells.

## Reading the relation

The handoff's name for the relation, "cosmic time–bandwidth theorem", places it in this family: D_x plays the role of a duration, D_p of a bandwidth, and h·N^{1/3} the role of the bound, with N the universe's "photon count/entropy".

One feature of the form can be read from the bullet itself (the wiki's reading; the handoff gives no derivation): if N counts cells of phase space, a count N shared among three dimensions is N^{1/3} cells along each one, which is what "per dimension" suggests. The handoff itself joins its two figures with "i.e.": "~10⁹⁰, i.e. ~10³⁰ h per dimension".

The program's derived relation between the two descriptions is [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint): position-space scales grow with a while momentum-space scales shrink with ã. The handoff does not relate the diameter relation to it.

## At the bounce and today

**The square.** The handoff places the square rectangle "exactly at the bounce" but does not say which bounce. The only bounce elsewhere in the record is the [conjugate universe](/wiki/program/conjugate-universe)'s bounce at the far-future turnaround of our expansion ([the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)); the handoff's summary does not connect the two statements, and no document says how D_x and D_p evolve in time. The ambiguity is recorded for Paul's ruling in `review/wiki-build-flags.md` item 24.

**The clock.** "Self-duality" in the program refers to the [self-dual point](/wiki/phase-space/modular-field/modular-inversion) of the [modular field](/wiki/phase-space/modular-field/modular-field-z), Z = i, and the self-dual locus |Z| = 1 with which the documents identify a·ã = 1 (#11 §6, §10). The handoff's phrase "a clock measuring distance from self-duality" appears to read today's aspect ratio of ~10⁹² as a measure of how far the universe is from the square, self-dual configuration (the wiki's reading); the handoff does not say how the clock runs.

## What is missing

- **No derivation.** No paper, note or review document states the relation. #11 does not mention it, an absence rather than a conflict.
- **No numbers checked.** The figures ~10⁹⁰, ~10³⁰ and ~10⁹² appear only in the handoff's summary of the chat, and no `verify/` script executes them. [The iron rule](/wiki/method/verification/iron-rule) requires executed code with printed output before any of them is used.
- **No definitions.** D_x, D_p, N and "the bounce" are named but not defined.

## The queue

The handoff lists the relation under "Optional write-ups: phase-space diameter relation note (§4)" (§8 item 7). The root `CLAUDE.md` ("Since the handoff") moves it into current queue item 1, "HANDOFF §8 items 5–7: the partially-massless comparison, the † literature battery, the phase-space-diameter note"; the second of the three is described on [the † literature battery](/wiki/method/literature-battery). Until that note exists the relation stays a chat-only conjecture, with no derivation behind it. See [open problems and the queue](/wiki/status/open-problems).

## Sources

- `HANDOFF.md` §4 — the relation, its numbers and its tier (the only source)
- `HANDOFF.md` §8 item 7 — the optional write-up in the handoff's queue
- `CLAUDE.md` 'Since the handoff' — the note in current queue item 1
