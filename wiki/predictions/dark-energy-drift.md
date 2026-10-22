---
title: "Row 4: thawing dark energy, never phantom"
weight: 50
status: alive
description: "Thawing with w₀ > −1, wₐ < 0, never phantom, the drift persisting in DESI DR3: a constant −1 kills the τ sector, a robust intrinsic w < −1 kills the framework, and DR2 already leans against it."
provenance: [D, T]
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md ref [21]"
  - "review/round3-adjudication.md 'Rulings' item 11"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3)'"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "review/wiki-build-flags.md item 26"
  - "review/wiki-build-flags.md item 27"
  - "review/wiki-build-flags.md item 6"
  - "popsci/angle-of-the-mirror.md 'The referee is already on the field'"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*Row 4 is the program's prediction for how dark energy, the cause of the accelerating cosmic expansion, changes over time. The program identifies dark energy with [τ](/wiki/cosmology/dark-energy/tau-quintessence), the angle that locates the vacuum's choice of [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations) on a circle; τ has a periodic potential and starts near its maximum, a setup called hilltop [quintessence](/wiki/cosmology/dark-energy/quintessence). Such a field makes dark energy weaken slowly ("thaw") and keeps its equation of state w at or above −1, the value of a cosmological constant, so it can never enter the "[phantom](/wiki/cosmology/dark-energy/phantom-divide)" regime w < −1. The test is the [Dark Energy Spectroscopic Instrument (DESI)](/wiki/cosmology/dark-energy/desi). Its Data Release 3 (DR3), expected in late 2026, is the decisive one. Its Data Release 2 (DR2) already favours a phantom phase in the past, so the sector is under real pressure. Row 4 is one of the three rows [the checkpoint](/wiki/history/documents/checkpoint) names as the program's near-term falsification exposure.*

**Status:** Alive, under real pressure — [D + T] (#11 §10), with w ≥ −1 [D] and the thawing shape [T] in [the lab notebook](/wiki/history/documents/lab-notebook) (#1 §7) — DESI DR2's phantom crossing stands against the strict w ≥ −1 (#11 §10, accepted as [round-3 ruling 11](/wiki/method/review/round-3/rulings); root `CLAUDE.md`: "under real pressure ahead of DR3"); not machine-checked.

## The row

[Checkpoint #11](/wiki/history/documents/checkpoint) §13, row 4:

| Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- |
| Dark energy w(z) | w ≡ −1 | Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3 | DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) — DR2 already favors a crossing above z ≈ 0.4 (§10) |

"DR3+" means DR3 or a later release. #11 §15 lists the row, with rows 1 and 7, as near-term falsification exposure, and calls DESI's next release the program's "nearest trial".

## The observable

The equation of state w of a component of the universe is the ratio of its pressure to its energy density, p = wρ. Through the continuity equation ρ̇ = −3H(ρ + p), with H the expansion rate, it fixes how the component's density changes as space expands [T] ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence)). w(z) is that ratio for dark energy as a function of redshift z, which labels cosmic time by how much the universe has expanded since.

A drifting w is usually summarized by two numbers in the Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a), with a the scale factor, equal to 1 today [T]. w₀ is the present value, and a negative wₐ means that w has been rising toward the present ([the w₀–wₐ parametrization](/wiki/cosmology/dark-energy/quintessence)).

No survey observes w directly. DESI measures distances with the baryon-acoustic-oscillation ruler, the imprint of sound waves in the early plasma on the clustering of galaxies, and w(z) follows only after a form for it is chosen and fitted together with other data ([from distances to w(z)](/wiki/cosmology/dark-energy/desi#from-distances-to-wz-t)). That step matters for the kill condition below.

## The standard expectation

"w ≡ −1": a cosmological constant, an energy density of empty space that does not change as the universe expands. It is the dark energy of the standard cosmological model, ΛCDM, a cosmological constant plus cold dark matter [T] ([the cosmological constant](/wiki/cosmology/dark-energy/quintessence#the-cosmological-constant-t)).

## The Broken-Born requirement

### The field

#11 §10, tagged [D + T]:

> "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1; thawing corridor wₐ ≈ −1.5(1 + w₀); two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint."

τ is the angle that locates the vacuum's polarization on the Maslov circle, a circle in the space of ways to split phase space into position and momentum halves ([τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase)). Because τ lives on a circle, its potential is periodic; the cosine form, with amplitude V₀ and angular scale f, is the standard potential of an axion-like field [T]. τᵢ is the field's initial value. The field and its action are on [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence). The requirement has three parts, each with its own derivation.

### Thawing

A field that starts near the top of its potential is held almost still while the expansion rate is high, so its w is close to −1 in the past. As the expansion slows, the field moves off the hilltop, its kinetic energy grows, and w rises [T]. The [lab notebook](/wiki/history/documents/lab-notebook) applies this to τ (#1 §7 item 2, transcribed from its LaTeX):

> "**Thawing shape.** Hilltop initial conditions give w ≈ −1 in the past, rising now: w₀ > −1, wₐ < 0, on the standard thawing corridor wₐ ≈ −1.5(1 + w₀)." **[T]**

[The tag](/wiki/method/provenance-tags) is [T]: thawing is a property of hilltop fields in general, not a result of the program ([how τ behaves](/wiki/cosmology/dark-energy/tau-quintessence#how-τ-behaves-thawing-from-the-hilltop)). The corridor is a line in the (w₀, wₐ) plane near which thawing models lie; neither #1 nor #11 cites a source for it.

### Never phantom

The lab notebook's argument, tagged [D] (#1 §7 item 1, transcribed from its LaTeX):

> "**w ≥ −1 always.** τ is a canonical scalar; the null energy condition holds; phantom crossing is impossible. **[D]** Any robust measurement of w < −1 (as an intrinsic equation of state, not an artifact of an assumed ΛCDM background) falsifies this sector outright."

The steps are short. τ has a kinetic term of the standard sign, so for a uniform field the energy density is ρ = ½τ̇² + V and the pressure p = ½τ̇² − V. Then ρ + p = τ̇² ≥ 0, which is the null energy condition, and with ρ > 0 it gives w ≥ −1 [T]. The potential cancels from ρ + p, so no choice of V breaks the null energy condition; the step from it to w ≥ −1 uses ρ > 0, which holds for the positive dark-energy density observed today [T]. Below −1, dark energy would grow as space expands, which τ cannot do ([the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound#the-derivation); [the phantom divide and the null energy condition](/wiki/cosmology/dark-energy/phantom-divide)). The bound applies to τ as the whole of dark energy, a premise #11 supports with its [vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity): "§7.3 guarantees the wedge sector contributes nothing that competes with τ" (#11 §10). Flag 6 in `review/wiki-build-flags.md` notes that the identity holds for a flat aligned vacuum, which is itself one condition on the gravity sector's coefficients, so it is not a consequence of symmetry alone.

### The drift persists

"Drift persists in DESI DR3" asks that the next release keep seeing w above −1 and rising, rather than settling on a constant. The sector's two remaining parameters connect the row to the next one. With V₀ fixed by the measured dark-energy density, w₀ and wₐ fix f and τᵢ, and the turnaround time t_turn of [row 5](/wiki/predictions/fate-of-expansion) is then determined: "one over-constraint" ([the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)). No document computes that relation, and whether t_turn exists at all for the potential as written is unresolved (`review/wiki-build-flags.md` item 27; [the over-constraint's reach](/wiki/cosmology/dark-energy/over-constraint#its-reach)).

## What kills it

### Two kill conditions

- **"DR3+ constant −1 (kills τ-sector)".** If DR3 or a later release converges on a constant w = −1, the thawing drift the row requires is absent, and the τ sector dies. v0.1 wrote "DR3+ converging on constant −1" (#1 §9).
- **"Robust intrinsic w < −1 (kills outright)".** A phantom equation of state, established as a property of dark energy itself, contradicts the no-phantom bound. "Intrinsic" excludes a w below −1 that appears only because the background model assumed in the fit is wrong: #1 §7 item 1 counts only w < −1 "as an intrinsic equation of state, not an artifact of an assumed ΛCDM background".

The documents differ on how much the second condition kills. #1 §7 item 1 says "falsifies this sector outright"; #11's row sets "kills outright" against "kills τ-sector"; and [the handoff](/wiki/history/documents/handoff) spells it out as the whole framework. No document states why the scope is wider than the sector ([how much a violation kills](/wiki/cosmology/dark-energy/no-phantom-bound#how-much-a-violation-kills)).

### Three outcomes

The handoff states the test as three outcomes of the next release (`HANDOFF.md` §2, "External clock"):

| Outcome of DR3 | Consequence |
| --- | --- |
| Robust constant w = −1 | kills the τ sector |
| Robust intrinsic w < −1 | kills the framework outright |
| Continued thawing drift | keeps it alive, "shared with other dynamical-DE models" |

DE is dark energy. The third outcome is not specific to the program: other models of dynamical dark energy survive it too. The handoff dates DR3 as "three-year data, expected late 2026"; `review/wiki-build-flags.md` item 26 records that DR2 already covers three years of operations, and this page quotes the handoff as written. The journey article #10 calls the outcomes "Three doors": "Constant kills the theory's heart. Phantom kills it outright. Continued weakening keeps it alive" ('The referee is already on the field'; [the popular articles](/wiki/history/documents/popular-articles)).

## The data situation: under real pressure

DESI's second data release reports, in #11's quotation (§10, from [21S]), that in every dataset combination

> "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4"

and that this preference "is thus rather independent of parametrization choices made in the analysis". [21S] is DESI Collaboration (M. Abdul-Karim et al.), "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," arXiv:2503.14738 (2025).

The favoured curve contains both behaviours the row distinguishes. Its low-redshift phase, w above −1 and weakening dark energy, is what the row requires. Its phase above z ≃ 0.4, w below −1, is what the row excludes. #11 §10, in the paragraph "Under pressure (v2.1)":

> "The framework's strict w ≥ −1 therefore stands against the direct reading of the data. It survives on two points: non-phantom quintessence fits remain compatible [19S], and w(z) is inferred from distances rather than observed, as [21S] also notes. DR3 is the decisive test (§13, row 4)."

The first point rests on fits without a phantom phase, "non-phantom compatible at ~2σ" (#11 §10), citing Gialamas et al., "Quintessence and phantoms in light of DESI 2025," arXiv:2506.21542 [19S]. The second is the distinction the kill condition already draws between a fitted and an intrinsic w < −1. In this wiki's reading, both points concern whether the data meet the kill condition; neither is evidence for the bound.

The finding reached the program through the [round-3](/wiki/method/review/round-3) review, which accepted it as ruling 11 ([round-3 rulings](/wiki/method/review/round-3/rulings)), and #11 v2.1 (2026-10-19) added the "Under pressure" paragraph to §10 and the DR2 clause to this row. #11 §15 lists "DESI DR2's phantom crossing against §10's strict w ≥ −1" among the program's degeneration risks. The root `CLAUDE.md`, which ranks first among the sources, states the position: "DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The dark-energy sector is under real pressure ahead of DR3."

The full record, including an italic passage of #11 §10 that still reads DESI's hints as "exactly the required drift" and is unreconciled with the paragraph above, is on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing#an-unreconciled-sentence-in-11-10).

## What the row does not depend on

- **The sign of the potential.** The far-future turnaround of [row 5](/wiki/predictions/fate-of-expansion) needs V(τ) to become negative, which the potential as written never does for V₀ > 0 (`review/wiki-build-flags.md` item 27; [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)). In this wiki's reading that conflict does not touch row 4: thawing concerns the field near the potential's maximum, and the null energy condition behind w ≥ −1 holds for any V (the bound itself also needs a positive energy density, which today's dark energy has).
- **The potential's origin.** Where τ's potential comes from is open ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). [The toy models](/wiki/symmetry-breaking/toy-models) show the structure is consistent, and #11 §10 adds: "None of this tests the cosmology".

## Superseded: DESI read as support

Before round 3 the documents read DESI's results as confirmation of the drift. The lab notebook called thawing "the *sign pattern DESI reports*" (#1 §7 item 2). The handoff called the sector "Consistent with DESI DR1/DR2 drift hints" (`HANDOFF.md` §2), DR1 being Data Release 1. v1 (#9 §8), the journey article #10 and the italic passage of #11 §10 describe DESI's hints as exactly the drift the sector requires. The technical record of #11 §10 and the root `CLAUDE.md` replace those readings; what they left out is the phantom phase at higher redshift. The list is on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing#superseded-the-earlier-readings-of-desi).

## Popsci-only: "constant is impossible"

The destination article #12 states the requirement more strongly than the record: "Decreasing is required; phantom is impossible; constant is impossible", and of the next data releases, "The framework survives only the first outcome" ('Dark energy as the orientation of the split'). In #11's row a constant −1 kills only the τ sector, and #10 agrees ("Constant kills the theory's heart. Phantom kills it outright."). The popular articles are never a source for a claim's status ([Conjectures: chat-only and popsci-only claims](/wiki/status/conjectures)).

## History of the row

| Version | Row | Requirement | Killed by |
| --- | --- | --- | --- |
| v0.1 (#1 §9, transcribed from its LaTeX) | 5 | "Thawing drift, w₀ > −1, wₐ<0 on the thawing corridor; **never** w<−1; drift persists in DESI DR3" | "DR3+ converging on constant −1 (kills τ-sector) or robust intrinsic phantom (kills outright)" |
| v1 (#9 §9) | 4 | "Thawing drift, w₀ > −1, wₐ < 0, on the thawing corridor; **never phantom**; drift persists in DESI DR3" | "DR3+ converging on constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright)" |
| #11 §13 | 4 | "Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3" | as above, with "— DR2 already favors a crossing above z ≈ 0.4 (§10)" since v2.1 |

The row moved from 5 to 4 when the two clumping rows were withdrawn after [Debt 3](/wiki/history/debts) ([the history of the predictions table](/wiki/predictions/table-history)); the lab notebook's v0.2 addendum lists it as "row 5 (thawing, no-phantom, DESI DR3)" among the program's distinctive, still-live content. The only change of substance is v2.1's clause on DR2.

## Sources

- `CLAUDE.md` 'Since the handoff' — "under real pressure ahead of DR3"
- `papers/broken-born-checkpoint-v2.md` §13 row 4 — the row; §10 — the field, its tags and the "Under pressure (v2.1)" paragraph; §15 — the exposure, "nearest trial" and the degeneration risk; header — the v2.1 change note; ref [21] — DESI DR2 Results II
- `review/round3-adjudication.md` 'Rulings' item 11 — the DR2 finding, accepted
- `HANDOFF.md` §2 — the external clock and the three outcomes; its "consistent" reading is superseded
- `notes/broken-born-theory.md` §7 items 1–2 — the no-phantom argument [D] and the thawing shape [T]; §3 — τ's action; §9 — the v0.1 row 5; 'Addendum (v0.2, post Debt-3)' — the row among the live content
- `notes/broken-born-program-v1.md` §8, §9 — v1's reading of DESI (superseded) and its row 4
- `review/wiki-build-flags.md` item 26 — DR3 as "three-year data"; item 27 — the potential's sign, which bears on row 5 and on t_turn; item 6 — the vacuum-energy identity's dependence on the flatness condition
- `popsci/angle-of-the-mirror.md` 'The referee is already on the field' and `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — "three doors" and the popsci-only "constant is impossible"; not status sources
