---
title: "Row 5: the fate of the expansion"
weight: 60
status: alive
description: "Eternal de Sitter versus a turnaround that is the conjugate bounce: a long-horizon prediction whose near-term proxy is row 4; whether V(τ) goes negative, as the turnaround needs, is unresolved (flag 27)."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 5"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md App. A item 7"
  - "papers/broken-born-checkpoint-v2.md App. A item 9"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §12"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "HANDOFF.md §2"
  - "CLAUDE.md 'Since the handoff'"
  - "review/wiki-build-flags.md item 27"
  - "review/wiki-build-flags.md item 23"
  - "review/wiki-build-checks/v_sign_check.out"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
  - "popsci/angle-of-the-mirror.md 'The referee is already on the field'"
---

*Row 5 is the program's prediction for the far future of the cosmic expansion. With a constant dark energy, standard cosmology expands forever toward an empty de Sitter universe. In the program, the expansion halts and reverses once the potential energy V(τ) of the dark-energy field τ becomes negative. Through the [cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint) a·ã = 1, which ties our scale factor a to the scale factor ã of the conjugate description, the same event is the conjugate universe's bounce: "our maximum is their minimum". The turnaround lies beyond any near-term observation, so #11 names [row 4](/wiki/predictions/dark-energy-drift) as its near-term test. Whether the potential as the documents write it can go negative at all is unresolved: as written, it never does.*

**Status:** Alive, long horizon — the bounce identity [D], the supporting fits [T] — it follows from the constraint a·ã = 1 [D] (#11 §10) and is not machine-checked. Its premise, a negative V(τ), conflicts with the potential as written, V = V₀[1 + cos(τ/f)], which has minimum zero for V₀ > 0; the conflict is recorded for Paul's ruling (`review/wiki-build-flags.md` item 27; [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)).

## The row

[Checkpoint #11](/wiki/history/documents/checkpoint) §13, row 5:

| Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- |
| Fate of expansion | Eternal de Sitter | Turnaround = conjugate bounce | (Long horizon; near-term test is row 4) |

The row is the long-run consequence of the dark-energy field whose present behaviour row 4 tests. Its kill column is a parenthesis: it names no observation that would end the claim.

## The observable

The fate of the expansion is whether the scale factor a(t), the factor by which cosmic distances have grown, increases forever or reaches a maximum and then decreases. In [Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) the square of the expansion rate H is proportional to the total energy density. The expansion halts at the moment the total density reaches zero, and reverses if the acceleration there is negative [T] ([how a turnaround happens](/wiki/cosmology/scale-factor-duality/conjugate-bounce#how-a-turnaround-happens-t)). The time of that moment is the turnaround time t_turn, which the documents count as an observable of the dark-energy sector (#11 §10) without computing it.

## The standard expectation

"Eternal de Sitter." With a positive cosmological constant, matter and radiation thin out as space grows while the vacuum energy does not, so the vacuum energy comes to dominate and the universe approaches de Sitter space, expanding exponentially forever [T]. A turnaround requires the vacuum energy to be negative, so that the total density can fall to zero as matter thins; a field that settles where its potential is negative acts as a negative cosmological constant, an anti-de Sitter phase, and the universe then collapses [T] ([recollapse](/wiki/cosmology/dark-energy/quintessence#recollapse-t)).

## The Broken-Born requirement

### The turnaround

The [lab notebook](/wiki/history/documents/lab-notebook) states the mechanism for the program's dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) (#1 §7 item 3; quotations from #1 on this page are transcribed from its LaTeX):

> "**The turnaround.** A cosine potential is negative over half its range. Once τ rolls past V = 0, the effective vacuum energy is negative, expansion halts, and slow contraction begins."

τ thaws from the top of its potential, which is the behaviour row 4 tests; the turnaround would come later in the same motion, once the potential has fallen below zero. The [handoff](/wiki/history/documents/handoff) gives the chain in one line: "eventual negative V ⇒ turnaround = conjugate bounce (one event, two descriptions)" (`HANDOFF.md` §2).

### The identity

The second half of the requirement rests on the cosmological constraint. #11 §10:

> "**Constraint [D]:** ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run) — the |Z| = 1 self-dual locus."

The derivation is the lab notebook's (#1 §6): with a the scale factor of position space and ã that of momentum space, "each mode occupies (aã)³ × (comoving cell) = ℏ³", so a·ã is constant, set to 1. The symplectic form ω measures phase-space area, and its rigidity is the constancy of ℏ ([the derivation](/wiki/cosmology/scale-factor-duality/cosmological-constraint#the-derivation)). The constraint's further identification with the |Z| = 1 locus of the modular field is queried in `review/wiki-build-flags.md` item 23; the turnaround uses only a·ã = 1.

Since ã = 1/a at every moment, the largest a is the smallest ã. Before the turnaround a grows and ã shrinks; after it, a shrinks and ã grows. Read in momentum variables, the turnaround is a contracting universe reaching a minimum and rebounding, which is a bounce. The lab notebook, tagged [D] (#1 §7 item 3):

> "In BBT the same event, read through aã = 1, is the conjugate frame's bounce: our maximum is their minimum. One event, [two descriptions] — now as a constraint identity rather than a metaphor. **[D]**"

BBT is the notebook's name for the framework, Broken-Born Theory, and the brackets replace its "two ledgers". #11 §10: "The turnaround is the conjugate bounce by constraint identity." The bounce is not a second event caused by the first; it is the same event in the other description, as a pulse whose duration grows and then shrinks has its narrowest spectrum at the moment of its longest duration. The full argument is on [the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce#the-identity-d), and the two-description reading in general on [the conjugate universe](/wiki/program/conjugate-universe#one-event-two-descriptions-the-turnaround).

The identity supplies no turnaround of its own. If a never reaches a maximum, there is no bounce to identify it with; everything turns on the sign of V(τ).

### The supporting fits

#11 §10 cites the data for a future collapse [T]: "high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]". The lab notebook quotes a figure from the first of these, fits to the 2025 data of the Dark Energy Spectroscopic Instrument (DESI) "with a potential possessing a negative minimum find a **93.8% preference for a future transition to anti-de Sitter space with eventual cosmological collapse**" (Gialamas, Hütsi, Raidal, Urrutia, Vasar, Veermäe 2025, arXiv:2506.21542; #11's [19S], "Quintessence and phantoms in light of DESI 2025"). Three cautions apply:

- the 93.8% figure appears only in #1, and no later document or `verify/` script checks it;
- #9 §8 cites the same fits with "[T — refresh citations before publication]", while #11 marks them [S];
- the fits assume a potential with a negative minimum, which the program's potential as written does not have (next section).

## The unresolved premise: the sign of V(τ)

The three documents that write τ's potential, #1 §3, #9 §8 and #11 §10, give it the same form:

```text
V(τ) = V₀[1 + cos(τ/f)]
```

Since cos(τ/f) ≥ −1, the bracket is never negative, so for V₀ > 0 the potential's lowest value is zero, not a negative number [T]. The turnaround needs V < 0, and the documents say so: "A cosine potential is negative over half its range" (#1 §7 item 3); dark energy "eventually goes negative" (#11 §10 and #9 §8, italic passages); "Turnaround after V(τ) < 0 = conjugate bounce" (#9 §9 row 5); τ is "destined to go negative" (#1 §12).

`review/wiki-build-flags.md` item 27 records the conflict: the turnaround "needs V < 0, but the stated potential V = V₀[1 + cos(τ/f)] has minimum 0 for V₀ > 0. #1 §7 says 'a cosine potential is negative over half its range', which is true of V₀cos(τ/f) but not of V₀[1 + cos(τ/f)]. Either the potential carries a negative offset not written down, or the turnaround needs another mechanism." The flag's executed check prints `V0[1+cos]: min V/V0 = 0.0` and `V0[1+cos]: fraction of period with V < 0 = 0.0` (`review/wiki-build-checks/v_sign_check.out`). The flag awaits Paul's ruling. This page quotes the sources as written and does not choose between the two readings; the open problem is [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign).

What rests on the point:

- **This row**, and the identity above, which presuppose a turnaround.
- **The third leg of the over-constraint.** #11 §10 counts "two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint", with V₀ "fixed by Ω_DE" (#1 §7 item 4). For the potential as written, t_turn is not defined ([the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint#its-reach)).
- **Founding supposition 7**, below.

The popular articles state the negative potential without qualification: "The orientation's energy landscape dips below zero, and once the stored energy goes negative, the cosmic push becomes a pull" (#12, 'Dark energy as the orientation of the split'); "a weakening that eventually goes negative means our expansion one day stalls and reverses" (#10, 'The referee is already on the field'). They are not sources for the claim's status ([the popular articles](/wiki/history/documents/popular-articles)).

## What kills it

The row has no kill condition of its own: "(Long horizon; near-term test is row 4)". A turnaround, if it happens, lies in the far future; v0.1 already wrote "— (long-horizon; the near-term test is row 5)", row 5 being the dark-energy row under the old numbering (#1 §9).

The near-term test is indirect. The turnaround is the end point of τ's motion, and [row 4](/wiki/predictions/dark-energy-drift) tests that motion now: a constant w = −1 in DESI's Data Release 3 (DR3) or later "kills τ-sector", and a robust intrinsic w < −1 "kills outright" (#11 §13). In the wiki's reading, either outcome removes the field whose potential would produce the turnaround. In principle the over-constraint adds a second link: once w₀ and wₐ are measured, f and τᵢ are fixed and t_turn follows, but no document computes that relation, and for the potential as written t_turn is not defined.

## The data situation

No observation bears on the turnaround directly. The cited fits prefer a future collapse only within models whose potential has a negative minimum. The proxy, row 4, is under real pressure: DESI's Data Release 2 (DR2) favours a phantom crossing above z ≈ 0.4, "against the framework's strict w ≥ −1", and "The dark-energy sector is under real pressure ahead of DR3" (root `CLAUDE.md`, 'Since the handoff'; [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).

## Founding supposition 7

#11's audit of Paul's founding suppositions records item 7, "Our expansion reverses at their bounce", as "**alive, corrected**: one event, [two descriptions]; live at DESI DR3" (#11 App. A item 7, with the brackets replacing "two ledgers"). The correction is the identity: the supposition as worded has two linked events, and the constraint makes them one. "Live at DESI DR3" refers to the proxy, row 4 ([founding suppositions](/wiki/program/founding-suppositions#7-our-expansion-reverses-at-their-bounce)).

The row is distinct from a dead neighbour. Founding supposition 9, "Their collapse is our acceleration", is "**dead twice**" (#11 App. A item 9): the conjugate side's collapse does not power our expansion ([Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)). Row 5 claims only that our future turnaround and the conjugate bounce are one event.

## Superseded: "after V(τ) < 0"

| Version | Row | Requirement |
| --- | --- | --- |
| v0.1 (#1 §9) | 6 | "Turnaround after V(τ)<0; AdS transition preferred by current quintessence fits" |
| v1 (#9 §9) | 5 | "Turnaround after V(τ) < 0 = conjugate bounce" |
| #11 §13 | 5 | "Turnaround = conjugate bounce" |

AdS is anti-de Sitter. v0.1 stated the turnaround and the supporting fits but not the bounce in the row; v1 joined them; #11 drops "after V(τ) < 0". No document says why the clause was dropped, and #11 §10's italic passage still says dark energy "eventually goes negative". The renumbering of the whole table is on [the history of the predictions table](/wiki/predictions/table-history).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 5 — the row; §10 — the constraint, the potential, the bounce identity, the fits and the italic "eventually goes negative"; App. A items 7 and 9 — founding suppositions 7 and 9
- `CLAUDE.md` 'Since the handoff' — the dark-energy sector under real pressure
- `notes/broken-born-theory.md` §6 — the derivation of a·ã = 1; §7 items 3–4 — the turnaround mechanism, the identity [D], the 93.8% figure [T], V₀ fixed by Ω_DE; §3 — the written potential; §9 — the v0.1 row 6; §12 — "destined to go negative"
- `notes/broken-born-program-v1.md` §8, §9 — the same potential, "eventually goes negative", and "Turnaround after V(τ) < 0"
- `HANDOFF.md` §2 — "eventual negative V ⇒ turnaround = conjugate bounce"
- `review/wiki-build-flags.md` item 27 and `review/wiki-build-checks/v_sign_check.out` — the sign conflict and its executed check, awaiting a ruling; item 23 — the |Z| = 1 identification queried
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' and `popsci/angle-of-the-mirror.md` 'The referee is already on the field' — the negative potential stated without qualification; not status sources
