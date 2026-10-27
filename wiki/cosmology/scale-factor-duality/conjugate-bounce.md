---
title: "The turnaround as the conjugate bounce"
weight: 50
status: alive
description: "If V(τ) goes negative our expansion halts and reverses; by a·ã = 1 the same event is the conjugate universe's bounce — one event, two descriptions."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 rows 4–5"
  - "papers/broken-born-checkpoint-v2.md App. A item 7"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
  - "review/wiki-build-flags.md items 24, 27"
  - "papers/phase-space-diameter.md §6"
  - "verify/phase_space_diameter.py 'Where the radiation rectangle is square, lambda = l_P (note §6)'"
  - "review/round5-adjudication.md 'Rulings' R11"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
---

*The turnaround is a far-future event the program predicts: our universe stops expanding and begins to contract, which happens if the potential energy of the [dark-energy field τ](/wiki/cosmology/dark-energy/tau-quintessence) becomes negative. Because our scale factor and that of the [conjugate universe](/wiki/program/conjugate-universe) are reciprocals ([the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint)), the moment our universe is largest is the moment its momentum-space description is smallest, so the same event, read in momentum variables, is a contracting universe reaching its minimum size and rebounding. The program states this as one event with two descriptions, not as two linked events. It is a long-horizon prediction whose near-term proxy is the [dark-energy drift](/wiki/predictions/dark-energy-drift) that survey data are testing now, and whether τ's potential, as the documents write it, can become negative at all is an unresolved conflict in the sources.*

**Status:** Alive, long horizon — [D] for the bounce identity, [T] for the cited fits (#1 §7 item 3; [#11](/wiki/history/documents/checkpoint) §10) — it follows from [the cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint) by identity and is not machine-checked; tested only in the long run ([row 5](/wiki/predictions/fate-of-expansion)). Its premise, a negative V(τ), conflicts with the potential as written, and no document resolves the conflict ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); flag 27 in `review/wiki-build-flags.md`).

## Statement

#11 §10: "The turnaround is the conjugate bounce by constraint identity."

The [handoff](/wiki/history/documents/handoff) gives the chain in one line: "eventual negative V ⇒ turnaround = conjugate bounce (one event, two descriptions)" (`HANDOFF.md` §2).

The [lab notebook](/wiki/history/documents/lab-notebook)'s version, with its [D] tag (#1 §7 item 3): the same event, "read through aã = 1, is the conjugate frame's bounce: our maximum is their minimum. One event, [two descriptions] — now as a constraint identity rather than a metaphor." (The notebook writes "two ledgers"; the brackets give the wiki's wording.)

## How a turnaround happens [T]

In [Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) the square of the expansion rate is proportional to the total energy density, H² ∝ ρ. Matter and radiation thin as the universe grows. If the vacuum energy, the part that does not thin, is positive, it eventually dominates and the expansion continues forever, approaching an empty, exponentially expanding [de Sitter](/wiki/cosmology/dark-energy/de-sitter-space) universe. That is the standard expectation with a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant#toward-de-sitter-space).

If the vacuum energy is negative, the total density falls as matter thins until it reaches zero. At that moment H = 0: the scale factor a has reached its maximum. The acceleration is then negative, so the universe begins to contract. A spacetime whose vacuum energy is negative is anti-de Sitter, so this sequence is described as a transition to anti-de Sitter space followed by collapse. The general physics of a field-driven recollapse is on [quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence).

In the program the vacuum energy is the potential energy V(τ) of the dark-energy field τ ([τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)). The lab notebook states the mechanism: once τ is past V = 0, "the effective vacuum energy is negative, expansion halts, and slow contraction begins" (#1 §7 item 3).

## The identity [D]

The [cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint) a·ã = 1 holds at every moment, so ã = 1/a. Two consequences follow without any dynamics of the conjugate side:

- **Our maximum is their minimum.** ã is smallest exactly when a is largest.
- **Our contraction is their re-expansion.** Before the turnaround a grows and ã shrinks: the conjugate description contracts. After it, a shrinks and ã grows: the conjugate description expands again. Read in momentum variables, the turnaround is a contracting universe reaching a minimum size and rebounding, which is a bounce.

This is why #11 calls it an identity: the bounce is not a second event caused by the first, but the same event in the other description, in the way that a pulse whose duration first grows and then shrinks has its narrowest spectrum at the moment of its longest duration. The [popular article](/wiki/history/documents/popular-articles) #12 puts it the same way: "The eventual reversal, likewise, is one event with two readings: in the position description, an expanding universe turning around; in the momentum description, a contracting one reaching minimum and rebounding." The [conjugate universe](/wiki/program/conjugate-universe) page sets out the two-description reading in general.

What the identity does not supply is the turnaround itself. That depends on the sign of τ's potential.

## The unresolved premise: the sign of V(τ)

The documents write τ's potential as

```text
V(τ) = V₀[1 + cos(τ/f)]
```

(#1 §3; #9 §8; #11 §10). Because cos(τ/f) ≥ −1, this V is never negative when V₀ > 0 [T]. The same documents require it to go negative:

- #1 §7 item 3: "A cosine potential is negative over half its range."
- #11 §10's plain-language opener: dark energy "eventually goes negative — at which point our expansion halts and reverses".
- #9 §9 row 5: "Turnaround after V(τ) < 0 = conjugate bounce"; #1 §9 row 6 has the same requirement.
- The fits the documents cite use potentials "possessing a negative minimum" (#1 §7 item 3).

No document reconciles the two statements. The register of [conflicts between sources](/wiki/history/documents/source-conflicts#cosmology) lists it as unresolved, and `review/wiki-build-flags.md` item 27 records it with an executed check, `review/wiki-build-checks/v_sign_check.py`, which prints the potential's minimum as 0; which statement the documents should carry awaits Paul's ruling. This page states the conflict and does not resolve it; the open problem has its own page, [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign). Everything on this page that depends on the turnaround happening, including the timing below, rests on that unresolved point.

The phase-space-diameter note restates the conflict with one qualification from its round-5 review: the potential "is never negative for V₀ > 0, and so, in the spatially flat universe the program's cosmology assumes, produces no turnaround as written (a closed universe can turn around without negative energy)" (`papers/phase-space-diameter.md` §6; `review/round5-adjudication.md` ruling R11, which cites #11 §10 for the flatness).

## The supporting fits [T]

#11 §10 cites "high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]". The lab notebook quotes a figure from the first of these: quintessence fits to the 2025 data of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI) "with a potential possessing a negative minimum find a **93.8% preference for a future transition to anti-de Sitter space with eventual cosmological collapse**" (Gialamas, Hütsi, Raidal, Urrutia, Vasar, Veermäe 2025, arXiv:2506.21542; #11's ref [19][S], "Quintessence and phantoms in light of DESI 2025").

Three cautions go with the figure:

- The 93.8% figure appears only in #1 and has not been rechecked against the paper.
- #9 §8 cites the same fits with the tag "[T — refresh citations before publication]"; #11 marks the reference [S], retrieved by live search.
- The fits use a potential with a negative minimum, which the program's potential as written does not have (the conflict above).

## The test: row 5

#11 §13 row 5: observable "Fate of expansion"; standard expectation "Eternal de Sitter"; requirement "Turnaround = conjugate bounce"; killed by "(Long horizon; near-term test is row 4)". See [row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion).

The near-term proxy is [row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift), the drift of dark energy's equation of state that DESI measures. #11 §13 adds to row 4 that "DR2 already favors a crossing above z ≈ 0.4", against the framework's [strict w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).

**Founding supposition 7.** "Our expansion reverses at their bounce" is "**alive, corrected**: one event, [two descriptions]; live at DESI DR3" (#11 App. A item 7, with the wiki's wording in brackets), where DESI DR3 is the survey's third data release (Data Release 3). The correction is the one this page describes: the two events became one. See [founding suppositions and their fates](/wiki/program/founding-suppositions).

## Timing

The turnaround time t_turn is the third of three observables, (w₀, wₐ, t_turn), that #11 §10 says are fixed by two parameters (f, τᵢ): "one over-constraint". The lab notebook adds that V₀ is "fixed by Ω_DE" (#1 §7 item 4). No document computes t_turn. See [the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint).

## The diameter relation's square

The chat-only form of the [phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter) stated that a position–momentum "rectangle", the extent of the universe's contents in position against their extent in momentum, is square "exactly at the bounce" (`HANDOFF.md` §4). The handoff's summary did not say which bounce it meant, and `review/wiki-build-flags.md` item 24 recorded the ambiguity.

The phase-space-diameter note answers the question for this bounce (`papers/phase-space-diameter.md` §6). The rectangle's aspect ratio grows as the square of the scale factor, so it is largest where a is: "If the expansion turns around, the turnaround is the moment of greatest elongation, not a square; for the Hubble box H → 0 there, and A → ∞" [D]. The radiation's rectangle would have been square only at 4.4×10¹⁴ times the Planck temperature, before the radiation existed [V] ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)). No reading the note tested puts a square rectangle at any bounce, and the claim is withdrawn: [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce). The identity on this page is not affected, since it concerns the two scale factors and not the rectangle's shape (the wiki's reading). Flag 24 awaits Paul's ruling; the round-5 adjudication recommends accepting it ('Recommendations to Paul').

## History

- **Lab notebook, v0.1** (#1 §7 item 3; §9 row 6). The identity [D], the fits [T], and the row "Turnaround after V(τ)<0; AdS transition preferred by current quintessence fits", where AdS is anti-de Sitter.
- **#9 §8, §9 row 5.** "The turnaround is the conjugate bounce by the constraint identity: one event, [two descriptions]"; the row reads "Turnaround after V(τ) < 0 = conjugate bounce".
- **`HANDOFF.md` §2.** "eventual negative V ⇒ turnaround = conjugate bounce (one event, two descriptions)".
- **#11 §10, §13 row 5.** The current statement. The row drops "after V(τ) < 0".
- **The phase-space-diameter note, version 1.1 (2026-10-26), §6.** The diameter relation's rectangle is at its most elongated at a turnaround, and its chat-only square "at the bounce" is withdrawn; the conflict over V(τ) is restated for the spatially flat universe (round-5 ruling R11).

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the statement, the potential, "eventually goes negative" and the cited fits
- `papers/broken-born-checkpoint-v2.md` §13 rows 4–5 — the prediction, its horizon and its near-term proxy
- `papers/broken-born-checkpoint-v2.md` App. A item 7 — founding supposition 7, "alive, corrected"
- `HANDOFF.md` §2 — "one event, two descriptions"
- `notes/broken-born-theory.md` §7 items 3–4 — the identity, "our maximum is their minimum", the trigger, the 93.8% figure; V₀ fixed by Ω_DE
- `notes/broken-born-theory.md` §3 — the potential V₀[1 + cos(τ/f)]
- `notes/broken-born-theory.md` §9 row 6 — the v0.1 form of the prediction
- `notes/broken-born-program-v1.md` §8, §9 row 5 — "Turnaround after V(τ) < 0 = conjugate bounce"
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — "one event with two readings" (popular article; explanation only)
- `review/wiki-build-flags.md` items 24 and 27 — the bounce the chat-only relation means, and the sign of V(τ), with the executed check `review/wiki-build-checks/v_sign_check.py`; both await Paul's ruling
- `papers/phase-space-diameter.md` §6 — the rectangle most elongated at a turnaround; the square withdrawn; the conflict over V(τ) in a spatially flat universe
- `verify/phase_space_diameter.py` 'Where the radiation rectangle is square, lambda = l_P (note §6)' — the epoch of the square, and the aspect ratio's maximum at a turnaround
- `review/round5-adjudication.md` 'Rulings' R11, 'Recommendations to Paul' — the flatness qualification; the recommendation to accept flag 24
