---
title: "Conjectures: chat-only and popsci-only claims"
weight: 40
status: record
description: "Results that exist only in the old chat and claims found only in the popular articles, quarantined, each with its relation to the record."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Decisions'"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/conjugate-special-relativity.md §5"
  - "papers/conjugate-special-relativity.md §6"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "popsci/universes-other-half.md"
  - "popsci/angle-of-the-mirror.md"
---

*This register collects claims that are not part of the program's derived record: results that exist only in the original claude.ai conversation, and claims that appear only in the two popular articles. They are kept apart because no document in the repository derives them and no script checks them. The popular article "The Universe's Other Half" also presents the framework as if it were confirmed, so it never decides a claim's status. Each line says how the claim relates to the record.*

**Status:** Record, a register current to 2026-10-20 — no provenance tags: `HANDOFF.md` §4 calls the phase-space diameter relation and the momentum-space black holes conjecture-tier, and the popular articles tag nothing — no derivation or script in the repository supports these claims; the chat-only list is `HANDOFF.md` §4, and the popsci-only claims are found only in `popsci/`.

## Key facts

- `HANDOFF.md` §4 lists the results that exist only in the chat, "not in any artifact": the phase-space diameter relation, the √N topological floor, two gravitational charges, a comparison of the general-relativity and conjugate field equations, momentum-space black holes, and the full adjudications of review rounds 1–2.
- A note on the phase-space diameter relation is in the current work queue (root `CLAUDE.md`, queue item 1).
- The √N floor is dead: it was dropped because its premise is inverted and its candidate is retired (round-3 Decision 3).
- #12 opens: "What follows presents the broken-Born framework as if it were confirmed. It is not." By the wiki's precedence rules it is never a source for a claim's status.
- Popsci-only claims conflict with the record in places: the magnetic identification contradicts strict sector separation and is dead, and "constant is impossible" contradicts #11's prediction row 4.
- The record has a few conjecture-tier statements of its own, outside these two lists; they are noted at the end.

## Chat-only results (`HANDOFF.md` §4)

### Gravity

- [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results) — ordinary stress-energy sources the massless graviton and dual stress, "how energy is structured across momentum", sources X; the slaved layer g̃ = g⁻¹ is algebraic; the dual Newtonian limit is "Yukawa in momentum = the gate"; X waves are massive, with five polarizations and a frequency floor. Status: conjecture. #13 §6 cites the checkpoint for dual effects "Yukawa-cut in momentum", while #11 §7.5 states the cut as "Yukawa-cut at 1/M_X"; the momentum reading appears only in the chat results.

### Cosmology

- [The phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter) — D_x · D_p = h · N^(1/3) per dimension, a "cosmic time–bandwidth theorem" whose rectangle is square at the bounce; "Conjecture-tier; candidate for a future note" (`HANDOFF.md` §4). Status: conjecture; the note is in the current queue.

### Conjugate special relativity

- [Momentum-space black holes (chat-only)](/wiki/conjugate-relativity/momentum-space-black-holes) — velocity traps; a horizon read in the momentum description is a maximum-force surface, since hovering there requires F → c⁴/G; "Conjecture tier; partially in #12". Status: conjecture. #12 says the framework "also permits, though it has not yet constructed" the mirror-image object.

### Dark matter

- [Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) — a bound on the soliton relic abundance between a Kibble ceiling and a √N net-charge floor. Status: dead. Ruling 3 of round 3 inverted its premise (Kibble production is a floor, not a ceiling), and Decision 3 dropped it.

### Review history

- The full adjudications of review rounds 1–2, with executed arbitration code — not in the repository; `HANDOFF.md` §6 summarizes their verdicts and rulings. See [Review rounds 1 and 2](/wiki/method/review/rounds-one-and-two).

## Popsci-only claims (#10, #12)

### Electric–magnetic duality

- [Obituary: the magnetic identification (popsci-only)](/wiki/electric-magnetic-duality/magnetic-identification) — #12: "The momentum-polarized sector is the magnetic side of electromagnetism", with a magnetic coupling "about 34, against our 1/137". Status: dead. It was never a program claim. `HANDOFF.md` §2 describes the soliton candidate as "dark by sector separation" and not magnetically charged under our photon, and strict P4 and prediction row 7 exclude a dark sector charged under our photon.

### Predictions

- "Constant is impossible" — #12: "Decreasing is required; phantom is impossible; constant is impossible", and #10: "frozen forbidden". The record differs: in #11 §13 row 4 a constant w = −1 in DR3 or later data (Data Release 3) kills the τ sector, not the framework, and #10 itself says "Constant kills the theory's heart. Phantom kills it outright." See [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift).

### The research program

- The other observers — if the momentum-polarized sector includes complex structures, observers there would see a sky of velocities: "Each polarization is the other's dark sector" (#12). The article calls it "a possibility the framework permits but does not require", and #10 calls its version "licensed daydreaming". Status: speculation, untested. See [The conjugate universe: one state, two descriptions](/wiki/program/conjugate-universe).

### The popular articles themselves

- The transparency argument — #12 argues that a sparse dark sector of very heavy magnetic objects would refract rather than scatter light, leaving effects "some forty orders of magnitude below the sharpest astronomical measurements". No script checks the figure, the argument assumes a dark sector magnetically charged under our electromagnetism, which strict P4 excludes, and the candidate it supported is retired. See [The popular articles (#10, #12)](/wiki/history/documents/popular-articles).
- "What one assumption purchases" — #12's closing summary, which says the framework "rests on a single assumption" where #11 states five postulates; its items are mapped to their current status on [The popular articles (#10, #12)](/wiki/history/documents/popular-articles).

## Conjecture-tier statements inside the record

These are in the repository's documents but are not derived there; each is recorded on the page of the claim it qualifies.

- The dual second law — #13 §5 makes λ_χ "the measure of resistance to force-change" and tags it "[conjecture-tier; the full dual dynamics awaits the formalization of §6]"; on [Dual inertia: free fall as rest](/wiki/conjugate-relativity/dual-inertia).
- Continuous breaking in 3+1 — the toy-model worklog notes that in 3+1 dimensions the Coleman–Mermin–Wagner theorem does not apply, so the self-dual coset model "can break the continuous U(1) itself, with τ an exactly massless Goldstone"; not computed, and the toy-model note lists "anything beyond d = 1" as not shown. On [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).

## Sources

- `CLAUDE.md` "Since the handoff" — the phase-space-diameter note in the current queue.
- `papers/broken-born-checkpoint-v2.md` §7.5, §13 — the Yukawa cut at 1/M_X; prediction row 4.
- `review/round3-adjudication.md` "Rulings" 3, "Decisions" 3 — the √N floor's premise inverted, and the item dropped.
- `papers/conjugate-special-relativity.md` §5, §6 — the conjecture-tier dual second law; "Yukawa-cut in momentum".
- `HANDOFF.md` §2, §4, §6, §8 — the chat-only list, the soliton candidate's charge, the round 1–2 summaries, the queued note.
- `notes/toy-lagrangian.md` "Chunk 3 results (2026-10-19): S4, quantum stability" — the 3+1 remark.
- `popsci/universes-other-half.md` — the "as if confirmed" preface, the magnetic identification, "constant is impossible", the transparency argument, the other observers, "What one assumption purchases".
- `popsci/angle-of-the-mirror.md` "The referee is already on the field", "Dividends and daydreams" — "frozen forbidden" and "Constant kills the theory's heart"; "licensed daydreaming".
