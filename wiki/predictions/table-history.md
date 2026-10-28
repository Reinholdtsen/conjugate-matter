---
title: "History of the predictions table"
weight: 10
status: record
description: "From the lab notebook's ten rows through v1's ten to the checkpoint's eleven: renumbering, withdrawn rows, dropped details, and the per-sector parameter counts."
sources:
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-program-v1.md §11"
  - "notes/broken-born-program-v1.md §0"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §12"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure of Debt 3'"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "HANDOFF.md §2"
  - "review/wiki-build-flags.md items 27, 32"
  - "review/wiki-build-flags.md items 27 (addendum), 46, 48, 49"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §4"
  - "notes/closed-universe.md §7"
---

*The predictions table is the program's list of observations that could kill it: for each observable it gives what standard physics expects, what the Comatter program requires, and the result that would end the claim. The table has appeared in three documents: ten rows in [the lab notebook](/wiki/history/documents/lab-notebook) (#1 §9, v0.1), ten in the first consolidated paper (#9 §9, v1) and eleven in [the current checkpoint](/wiki/history/documents/checkpoint) (#11 §13). Between them, two rows were withdrawn when the Debt-3 calculation [killed velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image), a diagnostic row took their place, the lead row softened from an exponential cliff to a knee, a graviton row and a dark-sector row were added, and the retired [soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) joined the list of withdrawn predictions. This page records those changes so that a row number in an older document can be read correctly.*

**Status:** Record — the tables themselves carry no [provenance tags](/wiki/method/provenance-tags) — #11 §13 is the current table; the tables of #1 §9 and #9 §9 are superseded and kept as the audit trail, and #11's own v2.0 table survives only in the repository's history.

## What the table is

Every version gives each row four entries: an observable, the standard expectation, the framework's requirement and a kill condition. The lab notebook introduces its table this way: "Each row states what standard theory (ΛCDM + GR + generic WIMP/Yukawa-SIDM alternatives) expects, what BBT requires, and what kills BBT" (#1 §9; quotations from #1 on this page are transcribed from its LaTeX where it writes mathematics). ΛCDM is the standard cosmology of a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant) plus cold dark matter, GR [general relativity](/wiki/gravity/spin-2-fields/general-relativity), WIMP a weakly interacting massive particle and SIDM [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter), here through a [Yukawa mediator](/wiki/gravity/spin-2-fields/yukawa-forces#the-standard-expectations-of-rows-1-and-2); BBT, Broken-Born Theory, is the notebook's name for the framework. #9 §9 and #11 §13 open with the plain-language line "A theory is its list of ways to die", to which #11 adds "updated".

Not every row has a kill condition. Some are diagnostics, which assign dark matter to one branch or another whatever the outcome, and some are long-horizon, with a parenthesis in place of a kill. The current table, with a page per row, is on [Predictions and kill conditions](/wiki/predictions).

## v0.1: the lab notebook's ten rows

#1 §9 had ten rows: σ_T(v) across halo masses, scattering anisotropy, [velocity-space structure in halos](/wiki/dark-matter/momentum-clumping/velocity-granularity), [dynamical friction in dwarf cores](/wiki/dark-matter/momentum-clumping/fornax-friction), dark energy w(z), the fate of the expansion, direct detection and colliders, [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles), photon dispersion and the early universe. Rows 1–4 belonged to [conjugate matter](/wiki/dark-matter/conjugate-matter), rows 5–6 to the dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence), rows 7–9 were permanent nulls, and row 10 covered the dual gravitational sector in the early universe.

The notebook singled out three rows: "Rows 1, 3, and 7 are the flagship discriminants: no mainstream framework predicts an exponential scattering cliff, gravitationally-detectable macro-granularity of the local velocity distribution, *and* a guaranteed-null direct-detection program" (#1 §9). Its one-paragraph summary claimed "kill conditions in every row of §9" (#1 §12).

Two of the three flagships rested on assumptions the program later tested. Row 1's cliff came from a Gaussian gate that was a postulate, and row 3's granularity, with row 4's friction suppression, from the expectation that the gated attraction would act collectively on a halo ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)).

## Debt 3: two rows withdrawn, one added

[Debt 3](/wiki/history/debts) tested the collective behaviour behind rows 3 and 4 and found it nowhere required ([the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem)). The withdrawal came in three steps, through [the Debt-3 calc notes](/wiki/history/documents/debt-3-notes).

1. **Calc note #2.** On [the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem#the-particle-island), "Rows 3 (velocity granularity) and 4 (condensed cores / Fornax friction suppression) are **withdrawn**, and with them the mechanism-level linkage claimed between them" (`notes/debt3a-stream-stability.md`, 'Consequences for the predictions table'). Rows 1–2 "**survive** — they are collisional".
2. **Calc note #3.** On the wave island the coupling could be fixed by dwarf-galaxy cores, and then "The surviving descendant of old rows 3–4" was a signature in [ultra-faint dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) (`notes/debt3b-wave-island.md`, 'What pins g? Two scenarios'). That scenario failed against the observed ultra-faint dwarfs ([Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)).
3. **Calc note #4.** "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them." (`notes/debt3c-ufd-endpoint.md`, 'Verdict and closure of Debt 3').

The lab notebook's v0.2 addendum records the result: "Rows 3–4 are struck from §9 permanently" and "A new row replaces them: **cliff-sharpness island discriminant**" (#1 'Addendum (v0.2, post Debt-3)'). It also lists what was left: "rows 1–2 (cliff, isotropy), the island discriminant, row 5 (thawing, no-phantom, DESI DR3), rows 7–9 (permanent nulls), and the geometric core awaiting Debt 1", DESI DR3 being Data Release 3 of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi).

The two withdrawn rows have obituaries beside the claims they tested: [Obituary: velocity-space granularity in halos (old row 3)](/wiki/dark-matter/momentum-clumping/velocity-granularity) and [Obituary: Fornax friction suppression (old row 4)](/wiki/dark-matter/momentum-clumping/fornax-friction). Both are indexed in [the graveyard](/wiki/status/graveyard). The new row became [row 3, the island discriminant](/wiki/predictions/island-discriminant).

## Debt 1: the cliff becomes a knee, and a graviton row

Two results of [Debt 1](/wiki/history/debts) changed the table.

- **Row 1 softened.** [Calc note #6](/wiki/history/documents/debt-1-notes) [derived the gate](/wiki/dark-matter/conjugate-matter/gate-mechanism) from exchange of [the momentum graviton X](/wiki/gravity/momentum-graviton) and found that generic vertices give power-law-tailed gates, which turned the cliff into a knee (`notes/debt1a-ii-X-classification.md` §4). Addendum v0.4 amends row 1: "the exponential cliff weakens to a *sharp knee at v\* with tail shape (Gaussian vs rational) diagnosing the vertex completion*; the knee's existence and location remain the robust prediction" (#1 'Addendum (v0.4)'). The requirement "cliff at v\* ~ 120 km/s" became "Knee at v\* ~ 10² km/s", and the kill condition "v > 3v\*" became "v ≫ v\*" ([row 1](/wiki/predictions/self-interaction-knee#superseded-the-exponential-cliff-of-v01)).
- **A graviton row.** Calc note #8 fixed the spectrum of the geometric sector. Addendum v0.6 gives the spectrum as "massless graviton = reciprocity-even, X = reciprocity-odd", with the Standard Model safe by the Yukawa range of X and the bounds from gravitational waves "satisfied identically by the massless eigenstate" (#1 'Addendum (v0.6)'; on the parities under #11 §6's Z → −Z⁻¹, see flag 39 in `review/wiki-build-flags.md`). v1 made this its new row 6 ([row 6, the exactly massless graviton](/wiki/predictions/massless-graviton); [spectrum and parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)).

## v1: ten rows again

#9 §9 had ten rows: the island discriminant as row 3, dark energy and the fate of the expansion moved to rows 4 and 5, the new row 6 on gravitational waves, and rows 7–10 as before. Below the table: "Withdrawn with cause, permanently: velocity-space granularity in halos; Fornax friction suppression (rows 3–4 of earlier versions; obituary in §7)."

Besides the renumbering, v1 reworded most surviving rows. The changes of substance:

- **Row 1**: "Knee at v\* ~ 10² km/s; tail shape = vertex diagnostic; zero cluster signal (particle χ)".
- **Row 3**: "Knee sharpness: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ", marked "(Diagnostic, not a kill: identifies the branch)", with the standard expectation "— (question not previously posed)".
- **Row 5**: v0.1's "Turnaround after V(τ)<0; AdS transition preferred by current quintessence fits", AdS being [anti-de Sitter](/wiki/cosmology/dark-energy/de-sitter-space#anti-de-sitter-space-t), became "Turnaround after V(τ) < 0 = conjugate bounce" ([row 5](/wiki/predictions/fate-of-expansion)).
- **Row 7**: v0.1's "χ has no non-gravitational SM coupling" became "χ (or X-condensate) has no non-gravitational SM coupling", SM being the Standard Model, the first trace of a second dark-matter candidate ([row 7](/wiki/predictions/direct-detection-null)).
- **Row 8**: v0.1's "Permanent null (p-polarized solitons)" lost its parenthesis ([row 8](/wiki/predictions/monopole-null)).
- **Row 10**: v0.1 read "a⁻⁶ step in G_eff; optional negative ΔN_eff from closed dual curvature" plus a conditional step in the primordial gravitational-wave spectrum, with the probe "CMB-S4 N_eff at ±0.03 probes the curvature term". v1 reads "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff" and "(Bounds constrain knobs; CMB-S4 probes)". CMB-S4 is a proposed [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#row-10s-probe-cmb-s4) experiment, whose current status is unchecked (flag 32 in `review/wiki-build-flags.md`; [row 10](/wiki/predictions/early-universe-step)). The closed-universe note of 2026-10-27 finds that a closed universe does not close momentum space in the record's geometry, so the closed dual curvature needs a separate postulate (flag 48), and that the dual Einstein–Hilbert term behind the a⁻⁶ step is derived in no document (flag 49) ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#the-dual-frame-what-closure-fixes-and-what-it-does-not)).

## The checkpoint, v2.0: eleven rows

#11 v2.0 added [row 11](/wiki/predictions/dark-sector-microstructure), "Dark-sector microstructure", a diagnostic with the standard expectation "(not previously posed)". In v2.0 the program had three dark-matter candidates, which [the handoff](/wiki/history/documents/handoff) calls a trilemma ("Dark-sector trilemma discrimination: particles vs X-condensate vs solitons", `HANDOFF.md` §2), and the v2.0 table carried all three. As imported into the repository (commit 8d588f6), row 11 required "Particles / condensate / knots separable via rows 1–3 + compact-object lensing + coherence signatures"; row 7's null covered "all three trilemma candidates SM-decoupled"; and row 3 was a diagnostic that "selects the branch, incl. trilemma row". Row 8 became "Magnetic monopoles (ours)".

v2.0 also shortened the wording and dropped four details that v1 had carried: row 1 lost "tail shape = vertex diagnostic", row 2 "(halo relaxation morphology)", row 5 "after V(τ) < 0" and row 6 "massive X short-range". The first survives in #11 §8's statement of [the scattering law](/wiki/dark-matter/conjugate-matter/scattering-law): "tail (Gaussian vs rational) diagnoses the vertex completion". The third matters because whether the potential as written can go negative at all is unresolved ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); `review/wiki-build-flags.md` item 27). The flag's addendum (2026-10-27) finds that with that potential the turnaround happens only in a closed universe, so the dropped clause names the wrong cause ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#the-turnaround-needs-k--1-dv)).

## The checkpoint, v2.1: after round 3

The [round-3](/wiki/method/review/round-3) review retired the third candidate, superheavy [topological solitons](/wiki/symmetry-breaking/topological-defects#topological-and-non-topological-solitons-t), and found DESI's second data release against the dark-energy row. #11 v2.1 (2026-10-19, commit e1c1f67) changed five entries of the table:

| Row | v2.0 | v2.1 |
| --- | --- | --- |
| 3, killed by | "Diagnostic — selects the branch, incl. trilemma row" | "Diagnostic — selects the branch (particle vs wave χ)" |
| 4, killed by | ends "robust intrinsic w < −1 (kills outright)" | adds "— DR2 already favors a crossing above z ≈ 0.4 (§10)" |
| 7, requirement | "(all three trilemma candidates SM-decoupled)" | "(both dark-sector candidates SM-decoupled; P4 strict)" |
| 11, requirement | "Particles / condensate / knots separable via rows 1–3 + compact-object lensing + coherence signatures" | "Particles vs condensate, separable via rows 1–3 + coherence signatures" |
| Withdrawn | two items | adds "superheavy-soliton dark matter (obituary §12)" |

DR2 is Data Release 2. The DR2 clause puts the dark-energy sector under real pressure ([row 4](/wiki/predictions/dark-energy-drift); root `CLAUDE.md`, 'Since the handoff'). The soliton candidate's obituary is [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary). "P4 strict" refers to strict sector separation under [postulate P4](/wiki/program/postulates/p4-polarized-matter). #11 v2.2 (2026-10-20) left §13 unchanged.

The current list of withdrawn predictions (#11 §13): "Withdrawn with cause: velocity-space granularity in halos; Fornax friction suppression (obituary §9); superheavy-soliton dark matter (obituary §12)."

## Exposure and novelty over time

The rows the documents single out have changed with the table.

| Document | Rows singled out | As |
| --- | --- | --- |
| #1 §9 (v0.1) | 1, 3, 7 | "the flagship discriminants" |
| #9 §11 (v1) | 1, 4, 7 | near-term falsification exposure |
| #11 §15 | 1, 4, 7 | near-term falsification exposure |
| #11 §15 | 3, 11 | "predictions not previously posed" |

The v0.1 flagship row 3 is dead, and the cliff of flagship row 1 is now a knee. v1 lists among its progressive signs "novel predictions not previously posed (island discriminant; knee shape; even-eigenstate masslessness as a bimetric-parity statement)" (#9 §11). The program's overall standing is on [Assessment: a live research program](/wiki/program/assessment).

## Numbering

The Debt-3 calc notes and #1 §9 use v0.1's numbers, in which row 3 is granularity, row 4 Fornax friction, row 5 dark energy and row 6 the fate of the expansion. v1 and #11 share one numbering. This wiki uses #11's numbers and calls the withdrawn rows "old row 3" and "old row 4".

| Observable | v0.1 (#1 §9) | v1 (#9 §9) | #11 §13 |
|---|---|---|---|
| σ_T(v) across halo masses | 1 (cliff) | 1 (knee) | [1](/wiki/predictions/self-interaction-knee) |
| Scattering anisotropy | 2 | 2 | [2](/wiki/predictions/scattering-isotropy) |
| Velocity-space structure in relaxed halos | 3 | withdrawn | withdrawn ([obituary](/wiki/dark-matter/momentum-clumping/velocity-granularity)) |
| Dynamical friction in dwarf cores | 4 | withdrawn | withdrawn ([obituary](/wiki/dark-matter/momentum-clumping/fornax-friction)) |
| Island discriminant | none (added by the v0.2 addendum, unnumbered) | 3 | [3](/wiki/predictions/island-discriminant) |
| Dark energy w(z) | 5 | 4 | [4](/wiki/predictions/dark-energy-drift) |
| Fate of expansion | 6 | 5 | [5](/wiki/predictions/fate-of-expansion) |
| Gravitational waves | none | 6 | [6](/wiki/predictions/massless-graviton) |
| Direct detection and colliders | 7 | 7 | [7](/wiki/predictions/direct-detection-null) |
| Magnetic monopoles | 8 | 8 | [8](/wiki/predictions/monopole-null) (ours) |
| Photon dispersion | 9 | 9 | [9](/wiki/predictions/photon-dispersion) |
| Early universe | 10 | 10 | [10](/wiki/predictions/early-universe-step) |
| Dark-sector microstructure | none | none | [11](/wiki/predictions/dark-sector-microstructure) |
| Superheavy-soliton dark matter | none | none | withdrawn in v2.1 ([obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary)) |

## Superseded: the parameter count

The lab notebook paired its table with a count of two parameters per sector against the phenomena each sector covers (#1 §10):

| Sector | Parameters | Phenomena covered |
|---|---|---|
| Conjugate matter | σ₀/m, v\* (2) | dwarf cores, the low-surface-brightness/group knee, cluster nulls, stream granularity scale, friction suppression (≥5) |
| Dark energy | f, τᵢ (2; V₀ fixed by Ω_DE) | w₀, wₐ, t_turn (3) |
| Geometry | M̃, k̃ (2, optional) | early-G step, ΔN_eff, gravitational-wave step |

#1 §12 sums this up as "Two parameters per sector, kill conditions in every row of §9", and v1's plain-language abstract as "two free parameters per sector, kill conditions on every claim" (#9 §0). Two of the five conjugate-matter phenomena, stream granularity and friction suppression, belonged to the withdrawn rows. The count also predates the momentum graviton X, whose five βₙ coefficients reduce to two (calc note #8 §3; #11 §7.5; [spectrum and parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)). #11 keeps only the dark-energy row of the count, as the [dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint), two parameters for three observables (§10), and has no full parameter table. In a closed universe, the only kind that turns around with the potential as written, t_turn also depends on the curvature, so the dark-energy row gains a third input (flag 46).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 — the current eleven-row table and the withdrawn list; §15 — the exposure rows and the rows not previously posed; §12 — the two remaining candidates; §7.5 — five βₙ to two parameters; header — the v2.1 and v2.2 change notes. #11 v2.0's table is quoted from the repository's history (commit 8d588f6, the imported text; commit e1c1f67, the v2.1 amendment).
- `notes/broken-born-program-v1.md` §9 — v1's ten rows and its withdrawn list; §11 — its exposure rows and novel predictions; §0 — "two free parameters per sector"
- `notes/broken-born-theory.md` §9, §10, §12 — v0.1's ten rows, its flagships, its parameter table and summary
- `notes/broken-born-theory.md` 'Addendum (v0.2, post Debt-3)', 'Addendum (v0.4)', 'Addendum (v0.6)' — the withdrawal of rows 3–4 and the island-discriminant row; the cliff-to-knee amendment; the spectrum behind the graviton row
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table', `notes/debt3b-wave-island.md` 'What pins g? Two scenarios', `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — the withdrawal of rows 3 and 4, step by step
- `notes/debt1a-ii-X-classification.md` §4 — the downgrade from cliff to knee
- `notes/debt1a-iv-beta-coefficients.md` §3 — the five-to-two reduction of the βₙ that postdates the v0.1 count
- `HANDOFF.md` §2 — the dark-sector trilemma
- `review/wiki-build-flags.md` item 32 — CMB-S4's status, unchecked; item 27 — the sign of the potential, which bears on row 5's dropped "after V(τ) < 0", with its addendum; items 46, 48 and 49 — the over-constraint moved to Ω_k, the closed dual curvature and the underived dual term
- `notes/closed-universe.md` §2 — the closed turnaround and the over-constraint; §4 — the flat momentum fibre; §7 — the dual Einstein–Hilbert term
