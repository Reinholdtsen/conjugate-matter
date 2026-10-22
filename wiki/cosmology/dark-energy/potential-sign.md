---
title: "Open: the sign of V(τ) and the turnaround"
weight: 90
status: open
description: "V₀[1 + cos(τ/f)] is never negative for V₀ > 0, yet the turnaround needs V < 0 and the cited fits use a negative minimum; none of #1, #9 and #11 discusses the conflict, which awaits Paul's ruling as flag 27, with an executed check kept outside the gate."
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 5"
  - "papers/broken-born-checkpoint-v2.md App. A item 7"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §12"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "HANDOFF.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "CLAUDE.md 'Since the handoff'"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
  - "popsci/angle-of-the-mirror.md 'The referee is already on the field'"
  - "review/wiki-build-flags.md item 27"
  - "review/wiki-build-checks/v_sign_check.py"
  - "review/wiki-build-checks/README.md"
---

*The sign problem is a conflict in the program's documents about the potential energy V(τ) of the [dark-energy field τ](/wiki/cosmology/dark-energy/tau-quintessence). They write it as V = V₀[1 + cos(τ/f)], and since a cosine never goes below −1, this potential is never negative when V₀ is positive. Yet the program's far-future [turnaround](/wiki/cosmology/scale-factor-duality/conjugate-bounce), in which our expansion halts and reverses, requires the potential to become negative, and the published fits the program cites for that event use potentials with a negative minimum. None of the three documents that write the potential discusses the conflict. It was found while this wiki was being built and is recorded, for Paul's ruling, as flag 27 in the build's list of suspected errors in the sources. Until he rules, the turnaround, its reading as the conjugate bounce, and the turnaround time in the [over-constraint](/wiki/cosmology/dark-energy/over-constraint) all rest on an unresolved point. This page records the conflict and does not choose a side.*

**Status:** Open — untagged; not among [checkpoint #11](/wiki/history/documents/checkpoint) §14's open problems and not on the current queue — the conflict was found when the sources were read side by side for this wiki, and no document resolves it; an executed check made for this wiki and kept outside [the gate](/wiki/method/verification/the-gate), `review/wiki-build-checks/v_sign_check.py`, prints the potential's minimum as 0, and the point awaits Paul's ruling (flag 27 in `review/wiki-build-flags.md`). It qualifies [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence). Listed on [open problems and the queue](/wiki/status/open-problems) and [conflicts between sources](/wiki/history/documents/source-conflicts#cosmology) (entry C20).

## The conflict in one line

The three documents that write τ's potential, #1, #9 and #11, write a function that is never negative for V₀ > 0, and every document that describes the turnaround needs that function to become negative.

## The potential as written

The [lab notebook](/wiki/history/documents/lab-notebook) introduces the potential with τ's action (#1 §3, transcribed from its LaTeX):

```text
V(τ) = V₀ [1 + cos(τ/f)]
```

"The potential's *periodicity* is forced by the Maslov topology **[D]**; [...] Its *magnitude* V₀ is a free parameter here. **[P/O]**" The later documents keep the same form: #9 §8 writes "V = V₀[1 + cos(τ/f)]" with "V₀ fixed by Ω_DE", and #11 §10 writes "V = V₀[1 + cos(τ/f)], periodicity by topology".

Because cos(τ/f) ≥ −1, the bracket 1 + cos(τ/f) is never negative, so V ≥ 0 everywhere whenever V₀ > 0 [T]. Its lowest value is zero, reached where cos(τ/f) = −1, not a negative value. The documents do not state the sign of V₀; they fix V₀ by the measured dark-energy density (#1 §7 item 4; #9 §8).

## Statements that need V < 0

A turnaround needs the total vacuum energy to become negative: only then does the expansion rate reach zero and the expansion reverse ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence#recollapse-t)). The documents say so directly.

| Document | Statement |
| --- | --- |
| #1 §7 item 3 (v0.1) | "A cosine potential is negative over half its range. Once τ rolls past V = 0, the effective vacuum energy is negative, expansion halts, and slow contraction begins." |
| #1 §9 row 6 (v0.1) | "Turnaround after V(τ)<0; AdS transition preferred by current quintessence fits" (AdS: [anti-de Sitter](/wiki/cosmology/dark-energy/de-sitter-space#anti-de-sitter-space-t)) |
| #1 §12 (v0.1) | τ is "destined to go negative (turnaround = the conjugate bounce, by constraint)" |
| #9 §8, italic passage (v1) | dark energy "eventually goes negative — at which point our expansion halts and reverses" |
| #9 §9 row 5 (v1) | "Turnaround after V(τ) < 0 = conjugate bounce" |
| `HANDOFF.md` §2 ([the handoff](/wiki/history/documents/handoff)) | "eventual negative V ⇒ turnaround = conjugate bounce" |
| #11 §10, italic passage | dark energy "eventually goes negative — at which point our expansion halts and reverses" |

#1 quotes are transcribed from its LaTeX. #11's technical text does not repeat the requirement in words; it states "The turnaround is the conjugate bounce by constraint identity" (§10) and sets row 5 as "Turnaround = conjugate bounce" (§13), both of which presuppose a turnaround.

The notebook's sentence "A cosine potential is negative over half its range" is true of a bare cosine, V₀cos(τ/f). The potential the same notebook writes in §3 has 1 added inside the bracket, which raises the cosine so that its minimum is zero. The documents do not comment on the difference.

## The cited fits

The fits the program cites for a future collapse use a different kind of potential. #11 §10 cites "high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]". The notebook describes one of them, Gialamas, Hütsi, Raidal, Urrutia, Vasar and Veermäe (arXiv:2506.21542, #11's [19S]), as fits "with a potential possessing a negative minimum" and gives "a **93.8% preference for a future transition to anti-de Sitter space with eventual cosmological collapse**" (#1 §7 item 3). The 93.8% figure appears only in #1, and no `verify/` script or later document checks it.

A potential with a negative minimum lets the field settle where the vacuum energy is negative, which is what produces the anti-de Sitter phase and the collapse [T]. The program's potential as written has its minimum at zero.

## What depends on it

- **The turnaround as the conjugate bounce.** The identity that our turnaround is the [conjugate universe](/wiki/program/conjugate-universe)'s bounce, through [the constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint), presupposes a turnaround ([the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)).
- **Row 5.** The prediction "Turnaround = conjugate bounce", with the standard expectation "Eternal de Sitter" (#11 §13; [row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion)).
- **Founding supposition 7.** "Our expansion reverses at their bounce — **alive, corrected**", "live at DESI DR3" (#11 App. A item 7), DESI being the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) and DR3 its Data Release 3 ([founding suppositions and their fates](/wiki/program/founding-suppositions)).
- **The third leg of the over-constraint.** The turnaround time t_turn is one of the three observables counted against two parameters ([the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)).
- **The popular accounts of the ending.** #12: "The orientation's energy landscape dips below zero, and once the stored energy goes negative, the cosmic push becomes a pull" ('Dark energy as the orientation of the split'); #10: "a weakening that eventually goes negative means our expansion one day stalls and reverses" ('The referee is already on the field'). See [the popular articles](/wiki/history/documents/popular-articles).

In this wiki's reading, the near-term test does not depend on it. [Row 4](/wiki/predictions/dark-energy-drift) concerns the thawing drift near the potential's maximum and the bound w ≥ −1, which holds for any potential while τ's energy density is positive, because V cancels from ρ + p ([the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound)); neither involves the potential's lowest value. That near-term test is itself under real pressure from DESI's Data Release 2 ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).

## What the sources do not say

- None of #1, #9 and #11 notices the conflict, and the handoff repeats the requirement without comment ("eventual negative V ⇒ turnaround", `HANDOFF.md` §2). None of the three states the sign of V₀, adds a constant to the potential, or replaces the cosine form. The conflict was first written down during this wiki's build, as flag 27 in `review/wiki-build-flags.md`.
- The [toy models](/wiki/symmetry-breaking/toy-models) do not bear on it. Their [ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) at H = 1, "V_b = −(μ/2)(1 + cos 2φ)" (toy note §4; [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)), is a cosine on the same circle, but it belongs to a model without gravity, where adding a constant to the potential changes nothing [T]. No document relates it to the sign of V(τ).
- #11 §14 does not list it, and the current queue in the root `CLAUDE.md` does not include it.
- No `verify/` script evaluates V(τ) or the turnaround; the check made for this wiki sits outside [the gate](/wiki/method/verification/the-gate) (below).

## What would settle it

The question is arithmetic about the documents' own formula, combined with what the turnaround needs, so it falls under [the iron rule](/wiki/method/verification/iron-rule), which asks for an executed check with printed output. One was made while this wiki was built: `review/wiki-build-checks/v_sign_check.py` samples one period of the documents' form and of a bare cosine, and prints (`review/wiki-build-checks/v_sign_check.out`):

```text
V0[1+cos]: min V/V0 = 0.0 at tau/f = 3.1415926535897927
V0[1+cos]: fraction of period with V < 0 = 0.0
V0 cos   : fraction of period with V < 0 = 0.49999750001249993
```

The point is item 27 of `review/wiki-build-flags.md`, which names two ways out: "Either the potential carries a negative offset not written down, or the turnaround needs another mechanism." Which statement the documents should carry awaits Paul's ruling, and the check is evidence for that ruling, not part of the gate. The README beside it says the scripts there are "evidence for a ruling, not part of the gate: none is wired into `scripts/check.sh`", and that "A ruling that accepts a flag should move the relevant check into `verify/`, with an anchor independent of the paper" (`review/wiki-build-checks/README.md`). Until Paul rules, no `verify/` script evaluates V(τ), and the turnaround, its identification with the conjugate bounce and the t_turn leg of the over-constraint rest on an unresolved point. This page records the conflict and does not choose a side.

## The claim it qualifies

The potential belongs to [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence). Where that potential comes from is a separate open problem: [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the potential, "eventually goes negative" (italic passage), the turnaround as the conjugate bounce, and the negative-minimum fits; §13 row 5 — the prediction; App. A item 7 — founding supposition 7
- `notes/broken-born-theory.md` §3 — the potential and its v0.1 tags
- `notes/broken-born-theory.md` §7 items 3–4 — "negative over half its range"; the fits with a negative minimum and the 93.8% figure (#1 only); V₀ fixed by Ω_DE
- `notes/broken-born-theory.md` §9 row 6, §12 — the turnaround after V(τ) < 0, in v0.1
- `notes/broken-born-program-v1.md` §8, §9 row 5 — the same potential, "eventually goes negative", and "Turnaround after V(τ) < 0"
- `HANDOFF.md` §2 — "eventual negative V ⇒ turnaround"
- `papers/reciprocity-toy-models.md` §4 — the toy models' bounded potential at H = 1
- `CLAUDE.md` 'Since the handoff' — the current queue, which does not include the point
- `review/wiki-build-flags.md` item 27 — the conflict, recorded for Paul's ruling; `review/wiki-build-checks/v_sign_check.py` and `review/wiki-build-checks/v_sign_check.out` — the executed check and its output (outside `verify/`); `review/wiki-build-checks/README.md` — the checks are evidence for a ruling, not part of the gate
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split', `popsci/angle-of-the-mirror.md` 'The referee is already on the field' — the popular accounts of the reversal
