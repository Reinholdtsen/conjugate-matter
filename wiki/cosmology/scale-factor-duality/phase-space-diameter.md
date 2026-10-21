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

*The phase-space diameter relation is a conjecture from the program's original chat sessions: the diameter of the universe in position space, multiplied by its diameter in momentum space, equals Planck's constant times a large number fixed by how many photons the universe contains. It is a cosmological counterpart of the time–bandwidth product of signal analysis, which says that a pulse cannot be both very short and very narrow in frequency. The relation exists only in the chat, as summarized by the handoff document: no paper or note derives it and no script checks its numbers. A short note on it is in the current work queue.*

**Status:** Conjecture (chat-only) — untagged; the handoff calls it "Conjecture-tier" — no derivation in any document, no `verify/` script, absent from #11; queued as a note (root `CLAUDE.md`, current queue item 1). Listed on [conjectures](/wiki/status/conjectures).

## Key facts

- **Statement.** `HANDOFF.md` §4: "D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem); the constant = the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension)".
- **At the bounce.** "rectangle square (D_x = D_p in Planck units) exactly at the bounce" (`HANDOFF.md` §4). The bounce is [the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce).
- **Today.** "aspect ratio today ~10⁹² = a clock measuring distance from self-duality" (`HANDOFF.md` §4). The reciprocal relation between the two descriptions is [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint).
- **Its tier and the queue.** "Conjecture-tier; candidate for a future note" (`HANDOFF.md` §4). The handoff's queue lists it under "Optional write-ups: phase-space diameter relation note (§4)" (§8 item 7); the root `CLAUDE.md` moves it into current queue item 1, with the partially-massless comparison and the † literature battery. See [open problems and the queue](/wiki/status/open-problems).
- **What is missing.** No document derives the relation, #11 does not mention it, and no `verify/` script executes its numbers (~10⁹⁰, ~10³⁰, ~10⁹²), which [the iron rule](/wiki/method/verification/iron-rule) requires before any use.
- **The analogy [T].** A signal's duration and its bandwidth cannot both be made arbitrarily small: their product has a lower bound, the signal-analysis form of the uncertainty principle. Its phase-space form is [the canonical commutator and the uncertainty principle](/wiki/phase-space/reciprocity/canonical-commutator), and the Fourier transform that relates the position and momentum descriptions is [a rotation of phase space](/wiki/phase-space/reciprocity/fourier-transform).

## Sources

- `HANDOFF.md` §4 — the relation, its numbers and its tier (the only source)
- `HANDOFF.md` §8 item 7 — the optional write-up in the handoff's queue
- `CLAUDE.md` 'Since the handoff' — the note in current queue item 1
