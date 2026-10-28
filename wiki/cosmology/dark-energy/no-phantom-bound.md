---
title: "The no-phantom bound w ≥ −1"
weight: 60
status: alive
description: "τ is a canonical scalar, so the null energy condition holds and w ≥ −1 strictly: the framework's sharpest dark-energy commitment, which a robust intrinsic w < −1 would kill outright, and which DESI DR2's phantom crossing now puts under real pressure."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "review/round3-adjudication.md 'Rulings' 11"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3): resolution of open problem 3'"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "notes/knot-dark-matter-standalone.md §5"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
  - "popsci/angle-of-the-mirror.md 'The referee is already on the field'"
  - "notes/closed-universe.md §6"
  - "review/wiki-build-flags.md item 52"
---

*The no-phantom bound is the program's requirement that the dark-energy equation of state w never fall below −1, the value of a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant). It holds because the program's dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) is an ordinary (canonical) scalar field, whose energy density can fall or hold steady as space expands but never rise, while w < −1, the phantom regime, would make it rise. The bound makes the dark-energy sector a sharp test: a robust measurement of an intrinsic w < −1 would kill the program's framework outright. The second data release of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI) favours a phase with w < −1 at [redshifts](/wiki/cosmology/scale-factor-duality/redshift) above about 0.4, so the bound stands against the direct reading of current data and is under real pressure; it survives only because fits without a phantom phase remain compatible and because w is inferred rather than observed.*

**Status:** Alive, under real pressure — [D] in #1 §7 item 1, and part of [checkpoint #11](/wiki/history/documents/checkpoint) §10's [D + T] paragraph — not machine-checked; its test is [row 4](/wiki/predictions/dark-energy-drift), and DESI's Data Release 2 (DR2) leans against it ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing); root `CLAUDE.md`: "under real pressure ahead of DR3").

## The statement

#11 §10, in the paragraph tagged **Dark energy [D + T]**: τ is hilltop [quintessence](/wiki/cosmology/dark-energy/quintessence) on the [Maslov circle](/wiki/phase-space/modular-field/maslov-phase), with "strictly w ≥ −1". The [lab notebook](/wiki/history/documents/lab-notebook) states and tags the bound (#1 §7 item 1, transcribed from its LaTeX):

> **w ≥ −1 always.** τ is a canonical scalar; the null energy condition holds; phantom crossing is impossible. **[D]** Any robust measurement of w < −1 (as an intrinsic equation of state, not an artifact of an assumed ΛCDM background) falsifies this sector outright.

The [handoff](/wiki/history/documents/handoff) carries it among the live results as "thawing, w ≥ −1 always" (`HANDOFF.md` §2). The field is [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence).

## The derivation

The notebook's argument has three steps, each one sentence.

1. **τ is a canonical scalar.** Its action is S_τ = ∫√−g[½(∂τ)² − V(τ)] (#1 §3, transcribed from its LaTeX): a kinetic term of the standard sign plus a potential, with no coupling to curvature and no second field.
2. **The null energy condition holds.** For such a field, uniform in space, the energy density is ρ = ½τ̇² + V and the pressure p = ½τ̇² − V, so ρ + p = τ̇², which cannot be negative. More generally, for any light-like vector k the stress-energy contracts to a square, T_μν k^μ k^ν = (k^μ ∂_μτ)² ≥ 0, which is the null energy condition [T] ([the phantom divide and the null energy condition](/wiki/cosmology/dark-energy/phantom-divide)).
3. **No phantom phase, no crossing.** With ρ > 0, ρ + p ≥ 0 means w = p/ρ ≥ −1. Equivalently, from the continuity equation ρ̇ = −3H(ρ + p), τ's energy density never grows while the universe expands. A w(z) that dips below −1 at any epoch is therefore impossible for τ, and so is a crossing of −1 in either direction.

Step 2 is textbook physics [T]; the program's contribution is the premise, that dark energy is the canonical scalar τ, and #1 tags the result [D]. The derivation is short, and its key step does not depend on the shape of the potential: no choice of V can make τ violate the null energy condition, because V cancels from ρ + p. Turning that into w ≥ −1 needs ρ > 0, as step 3 states. It does rely on τ being the whole of dark energy. #11 supports that premise with the [vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity): "§7.3 guarantees the wedge sector contributes nothing that competes with τ" (#11 §10). Flag 52 in `review/wiki-build-flags.md` finds that the guarantee holds for the dark-energy density but follows from the exact (1 − y)⁴/y relation on the bimetric branch rather than from §7.3's aligned-point identity alone ([the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe#the-branch-relation-dv)).

## What counts as a violation

The bound concerns the equation of state of τ itself. A survey does not measure that directly; it measures distances and fits a model of w(z) to them ([DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi)). A fitted w below −1 can arise without any intrinsically phantom component, for example when the assumed background model is wrong ([the phantom divide](/wiki/cosmology/dark-energy/phantom-divide#intrinsic-against-inferred)). The documents draw the line accordingly.

- #1 §7 item 1 counts only a w < −1 "as an intrinsic equation of state, not an artifact of an assumed ΛCDM background", ΛCDM being the standard model of a cosmological constant plus cold [dark matter](/wiki/dark-matter).
- #11's kill condition is a "robust intrinsic w < −1" (§13 row 4).
- #11 §10 adds, of the current data, that "w(z) is inferred from distances rather than observed".

## The kill condition

Row 4 of #11's [prediction table](/wiki/predictions) ([row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift)):

| Observable | Standard expectation | Program requirement | Killed by |
| --- | --- | --- | --- |
| Dark energy w(z) | w ≡ −1 | Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3 | DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) — DR2 already favors a crossing above z ≈ 0.4 (§10) |

DR3 is DESI's Data Release 3. The no-phantom bound is the second kill condition; the first, a constant w = −1, tests the [thawing drift](/wiki/cosmology/dark-energy/thawing-and-freezing) ([τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)).

### How much a violation kills

The documents differ on the scope of the second kill.

| Document | What a robust intrinsic w < −1 kills |
| --- | --- |
| #1 §7 item 1 (v0.1) | "falsifies this sector outright" |
| #1 §9 row 5 (v0.1) | "robust intrinsic phantom (kills outright)" |
| #9 §9 row 4 (v1) | "robust intrinsic w < −1 (kills outright)" |
| `HANDOFF.md` §2 | "robust intrinsic w < −1 kills the framework outright" |
| #14 §5, exclusion condition 6 (withdrawn) | "kills the parent framework's cosmological sector" |
| #11 §13 row 4 (current) | "robust intrinsic w < −1 (kills outright)" |

#11 ranks above the others. Its row 4 sets "kills outright" against "kills τ-sector" for a constant −1, which reads as more than the sector, and the handoff spells it out as the whole framework; #1 §7 item 1 and the withdrawn #14 confine the kill to the sector. No document states why the scope is wider than the sector. The register of [conflicts between sources](/wiki/history/documents/source-conflicts#dark-energy) lists the disagreement as settled by precedence in #11's favour.

## Under pressure

DESI's DR2 reports that in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4" [21S] (#11 §10). The preferred w(z) thus contains the phase the bound excludes. #11 §10, "Under pressure (v2.1)":

> The framework's strict w ≥ −1 therefore stands against the direct reading of the data. It survives on two points: non-phantom quintessence fits remain compatible [19S], and w(z) is inferred from distances rather than observed, as [21S] also notes. DR3 is the decisive test (§13, row 4).

The fits without a phantom phase are "non-phantom compatible at ~2σ" (#11 §10). The root `CLAUDE.md` states the position: "DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The dark-energy sector is under real pressure ahead of DR3." #11 §15 lists "DESI DR2's phantom crossing against §10's strict w ≥ −1" among the program's degeneration risks.

The bound is alive because the data do not yet meet the kill condition: the crossing is a preference of fitted models, not a robust measurement of an intrinsic w < −1. If DR3 confirms an intrinsic phantom phase, the bound fails and, by #11's row 4, the kill is outright. How the finding entered the program, and the italic passage of #11 §10 that still reads DESI's hints as "exactly the required drift", are on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).

## The popular gloss

Both popular articles explain the bound through the sign of kinetic energy ([the popular articles](/wiki/history/documents/popular-articles)). #12: phantom behaviour "would require the orientation's kinetic energy to be negative, and kinetic energy is the square of a rate of change; a square of a real quantity cannot be negative" ('Dark energy as the orientation of the split'). #10: dark energy "can never strengthen past the constant line, because exceeding it would require negative kinetic energy, a square of a real number coming out below zero" ('The referee is already on the field'). These are explanations of step 2 above, not sources for the bound's status.

## History

- **v0.1 (#1 §7 item 1; §9 row 5).** The bound is derived [D] and made a kill condition, with the intrinsic-versus-artifact qualification.
- **v0.2.** After [Debt 3](/wiki/history/debts), the notebook lists "row 5 (thawing, no-phantom, DESI DR3)" among the program's distinctive, still-live content.
- **v1 (#9 §8; §9 row 4).** "Strictly w ≥ −1", and the requirement "**never phantom**", with the kill "robust intrinsic w < −1 (kills outright)".
- **#11 v2.0.** §10 "strictly w ≥ −1"; row 4 as in v1.
- **Round 3.** The [soliton manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary) #14 v3, since withdrawn, described the parent framework as predicting "thawing, never-phantom dark energy, currently consistent with hints of weakening dark energy in recent baryon-acoustic-oscillation data" (§4). The [round-3](/wiki/method/review/round-3) referee found the DESI-preferred solution phantom-crossing, and ruling 11 accepted it: "The parent framework's 'never phantom' needs the checkpoint's own nuance: non-phantom fits remain compatible at ~2σ." ([round-3 rulings](/wiki/method/review/round-3/rulings)).
- **#11 v2.1 (2026-10-19).** §10 gains the "Under pressure (v2.1)" paragraph, row 4 the clause "DR2 already favors a crossing above z ≈ 0.4 (§10)", and §15 the degeneration risk. The bound itself is unchanged.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — "strictly w ≥ −1" and the "Under pressure (v2.1)" paragraph
- `CLAUDE.md` 'Since the handoff' — "under real pressure ahead of DR3"
- `papers/broken-born-checkpoint-v2.md` §13 row 4 — the requirement and the kill conditions
- `papers/broken-born-checkpoint-v2.md` §15 — DR2's crossing among the degeneration risks
- `review/round3-adjudication.md` 'Rulings' 11 — the finding accepted
- `HANDOFF.md` §2 — "w ≥ −1 always"; "kills the framework outright"
- `notes/broken-born-theory.md` §3 — the canonical action; §7 item 1 — the derivation [D] and the intrinsic-versus-artifact qualification; §9 row 5 — the v0.1 kill condition; 'Addendum (v0.2)' — row 5 among the live content
- `notes/broken-born-program-v1.md` §8, §9 row 4 — v1's "Strictly w ≥ −1" and kill condition
- `notes/knot-dark-matter-standalone.md` §5 — exclusion condition 6 (withdrawn manuscript)
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split', `popsci/angle-of-the-mirror.md` 'The referee is already on the field' — the plain-language gloss (popular articles)
- `notes/closed-universe.md` §6; `review/wiki-build-flags.md` item 52 — where the wedge sector's guarantee comes from
