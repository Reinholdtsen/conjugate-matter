---
title: "DESI DR2's phantom crossing"
weight: 70
status: record
description: "DESI DR2 favours w > −1 at low redshift and a crossing to w < −1 above z ≃ 0.4 in every dataset combination, against the framework's strict w ≥ −1; the sector survives on non-phantom fits compatible at ~2σ and on w(z) being inferred, and DR3 decides."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md ref [21]"
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "review/round3-adjudication.md 'Rulings' 11"
  - "review/round3-adjudication.md 'Decisions' 4"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(c) item 11"
  - "HANDOFF.md §2"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-theory.md §7"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §5"
  - "popsci/angle-of-the-mirror.md 'The referee is already on the field'"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*DESI DR2's phantom crossing is the finding, reported in 2025 from the second data release (Data Release 2, DR2) of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI), that the dark-energy equation of state favoured by the data lies above −1 at low redshift and crosses below −1, into the [phantom regime](/wiki/cosmology/dark-energy/phantom-divide), at redshifts above about 0.4, in every combination of datasets analysed. The program [requires dark energy never to be phantom](/wiki/cosmology/dark-energy/no-phantom-bound), so its requirement stands against the direct reading of these data, and its dark-energy sector is under real pressure. The sector survives on two stated points: fits without a phantom phase remain compatible at about two standard deviations, and the equation of state is inferred from distance measurements rather than observed. The third data release is the decisive test.*

**Status:** Record — the measurement is cited [21S] in [checkpoint #11](/wiki/history/documents/checkpoint) §10, "Under pressure (v2.1)" — raised by the [round-3](/wiki/method/review/round-3) referee, accepted as ruling 11 and written into #11 v2.1; per the root `CLAUDE.md` the dark-energy sector is "under real pressure ahead of DR3", DESI's Data Release 3.

## What DESI reported

#11 §10 quotes the DR2 paper directly. In every dataset combination

> "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4"

and this preference

> "is thus rather independent of parametrization choices made in the analysis" [21S].

The paper is #11's reference [21][S]: DESI Collaboration (M. Abdul-Karim et al.), "DESI DR2 Results II: Measurements of Baryon Acoustic Oscillations and Cosmological Constraints," arXiv:2503.14738 (2025).

Three terms in the quotation need a gloss.

- **w(z)** is the dark-energy equation of state, pressure over energy density, as a function of redshift z ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence)). A cosmological constant has w = −1 at every z.
- **A phantom crossing** is a passage of w(z) through −1. Below −1 the dark-energy density grows as space expands, which an ordinary scalar field cannot do ([the phantom divide and the null energy condition](/wiki/cosmology/dark-energy/phantom-divide)). In the reported shape, w was below −1 at earlier times, above z ≃ 0.4, and is above −1 at later times.
- **The favoured w(z)** is the best-fitting curve of a fitted model. The survey measures distances with the baryon-acoustic-oscillation ruler, and w(z) follows only after a form for it is chosen and fitted together with other data ([DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi)). #11's "in every dataset combination" and the paper's "rather independent of parametrization choices" say that the shape does not hinge on one particular choice of data or of form; the most common two-parameter form, and how a crossing appears in it, are described on [the CPL parametrization](/wiki/cosmology/dark-energy/cpl-parametrization#a-phantom-crossing-in-the-w₀wₐ-plane-t).

## What it means for the program

The program's dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) is a canonical scalar, and the program requires "strictly w ≥ −1" (#11 §10; [the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound)). The phase that DR2 favours above z ≃ 0.4 is the phase the bound excludes. #11 §10 draws the consequence in its "Under pressure (v2.1)" paragraph:

> The framework's strict w ≥ −1 therefore stands against the direct reading of the data. It survives on two points: non-phantom quintessence fits remain compatible [19S], and w(z) is inferred from distances rather than observed, as [21S] also notes. DR3 is the decisive test (§13, row 4).

The two points are these.

1. **Non-phantom fits remain compatible.** Fits of quintessence models that never cross −1 are still acceptable: #11 §10 gives the current state as "compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ)" [19S, 20S, 21S], and cites the survival point to [19S], Gialamas et al., "Quintessence and phantoms in light of DESI 2025," arXiv:2506.21542.
2. **w(z) is inferred.** A fitted phantom phase can arise without any component that is intrinsically phantom ([the phantom divide](/wiki/cosmology/dark-energy/phantom-divide)). The program's kill condition counts only "robust intrinsic w < −1" (#11 §13 row 4), and the [lab notebook](/wiki/history/documents/lab-notebook) spelled out the distinction: w < −1 "as an intrinsic equation of state, not an artifact of an assumed ΛCDM background" (#1 §7 item 1), ΛCDM being the standard model of a cosmological constant plus cold [dark matter](/wiki/dark-matter).

In this wiki's reading, both points concern whether the data meet the kill condition; neither is evidence for the bound. The weakening at low redshift, "a phase of w > −1", is the behaviour the program requires; the phantom phase at higher redshift is the behaviour it excludes; and the favoured w(z) contains both.

## How it entered the record

The finding entered the program through the review of a different manuscript.

- **The claim reviewed.** The [soliton manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary) #14 v3, since withdrawn, said in passing: "The parent framework's cosmological sector separately predicts thawing, never-phantom dark energy, currently consistent with hints of weakening dark energy in recent baryon-acoustic-oscillation data" (§4). Its exclusion condition 6 read: "Robust dark-energy measurement of constant w = -1 or intrinsic w < -1 (kills the parent framework's cosmological sector)" (§5).
- **The referee.** The [round-3](/wiki/method/review/round-3) referee, a [blind subagent](/wiki/method/review/review-protocol) with web access, listed the sentence as uncited (`review/round3/referee/audit-notes.md` Step 1) and added a "Dark-energy aside" (Step 4(c) item 11). It quoted DR2, "the favored w(z) shows a phase of w > -1 at low redshifts and a phantom crossing to w < -1 above redshifts z ~ 0.4", and concluded: "'Never-phantom ... consistent with hints' is at best partially true; the DESI-preferred solution is phantom-crossing, which exclusion condition 6 says would kill the framework."
- **The ruling.** The adjudication's table records the finding as ruling 11, "DESI DR2's best fit crosses into phantom (w < −1) above z ≈ 0.4", rules it **Accepted**, and gives as evidence: "The parent framework's 'never phantom' needs the checkpoint's own nuance: non-phantom fits remain compatible at ~2σ." ([round-3 rulings](/wiki/method/review/round-3/rulings)).
- **The decision.** Decision 4 scheduled a cleanup before further work, including: "give §10 the DESI DR2 phantom-crossing nuance (ruling 11)" ([round-3 decisions](/wiki/method/review/round-3/decisions)). Paul delegated the round-3 decisions to Claude on 2026-10-19 and keeps the veto (`review/round3-adjudication.md`, 'Decisions').
- **The amendment.** #11 v2.1, dated 2026-10-19, records the change in its header: "§10 records DESI DR2's phantom crossing". It added the "Under pressure (v2.1)" paragraph to §10, the clause "DR2 already favors a crossing above z ≈ 0.4 (§10)" to row 4 of §13, and the crossing to the degeneration risks of §15. The commit that made v2.1 (e1c1f67) also re-marked reference [21] from † to [S] and gave its full title.
- **The project instructions.** The root `CLAUDE.md` lists the change among the events since the handoff ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)).

## Where it stands

The root `CLAUDE.md`, which ranks first among the sources, states the position plainly: "DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The dark-energy sector is under real pressure ahead of DR3." ('Since the handoff').

#11 §15 says the same in its assessment: the program's "nearest trial is DESI's next release, and the current release already leans against its dark-energy prediction (§10)", and it lists "DESI DR2's phantom crossing against §10's strict w ≥ −1" among the program's degeneration risks, in the vocabulary of [Lakatos's methodology of research programmes](/wiki/method/lakatosian-methodology). The overall assessment is on [assessment: a live research program](/wiki/program/assessment).

## An unreconciled sentence in #11 §10

#11 §10 opens, like every section of the checkpoint, with an italic plain-language passage. That passage still ends: "The sky is voting now: DESI's hints of weakening dark energy are exactly the required drift." The same sentence stood in v2.0, and the v2.1 amendment added the "Under pressure" paragraph below it without changing it.

Within #11 the two passages disagree: the italic one reads the data as the required drift, the technical one as a phantom crossing that stands against the bound. #11 does not reconcile them, and no later document edits the italic passage. This wiki takes the sector's status from the root `CLAUDE.md`, which ranks above #11, and from #11's technical paragraph, both of which say "under pressure"; it records the italic sentence as an unresolved inconsistency inside #11 ([conflicts between sources](/wiki/history/documents/source-conflicts)).

## Data Release 3: three outcomes

The [handoff](/wiki/history/documents/handoff) names the next release as the program's external clock: "DESI DR3 (three-year data, expected late 2026). Kill conditions: robust constant w = −1 kills the τ sector; robust intrinsic w < −1 kills the framework outright; continued thawing drift keeps it alive (shared with other dynamical-DE models)" (`HANDOFF.md` §2), DE being dark energy. The "three-year" label is listed as a suspected slip in the source (`review/wiki-build-flags.md` item 26); the wiki quotes it as written. #11's row 4 states the first two kill conditions as "kills τ-sector" and "kills outright" ([row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift)).

| Outcome of Data Release 3 | Consequence (HANDOFF §2) |
| --- | --- |
| Robust constant w = −1 | kills the τ sector |
| Robust intrinsic w < −1 | kills the framework outright |
| Continued thawing drift | keeps it alive, shared with other models of dynamical dark energy |

The journey article #10 calls these "Three doors": "Constant kills the theory's heart. Phantom kills it outright. Continued weakening keeps it alive — shared credit with other dynamical-dark-energy models, but alive" ('The referee is already on the field'; [the popular articles](/wiki/history/documents/popular-articles)). The other popular article, #12, says instead that the framework "survives only the first outcome" (a strengthening of the weakening trend), so that a constant would also be fatal; the row-4 page records that popsci-only reading against #11's.

The withdrawn #14 gave a third reading: both robust outcomes kill "the parent framework's cosmological sector" (§5, exclusion condition 6). #11 ranks above it; its row 4 has the phantom outcome kill "outright", against "kills τ-sector" for a constant, and the handoff reads that as the whole framework.

## Superseded: the earlier readings of DESI

Before round 3, the documents that comment on DESI's results all read them as support for the dark-energy sector. Each of these readings is superseded by #11 §10's "Under pressure (v2.1)" paragraph, ruling 11 and the root `CLAUDE.md`.

| Document | Its reading |
| --- | --- |
| Lab notebook #1 §7 item 2 (v0.1) | thawing "is the *sign pattern DESI reports*" |
| #9 §8, italic passage (v1) | "the DESI survey's hints of weakening dark energy are exactly the drift this sector requires" |
| `HANDOFF.md` §2 | "Consistent with DESI DR1/DR2 drift hints." (DR1 is Data Release 1) |
| #14 v3 §4 (withdrawn) | "currently consistent with hints of weakening dark energy in recent baryon-acoustic-oscillation data" |
| #10, 'The referee is already on the field' | "having spent two years reporting tantalizing hints of exactly the required weakening" |
| #12, 'Dark energy as the orientation of the split' | "reported statistically suggestive evidence that dark energy is weakening — the required behavior — though the case is not yet decisive" |
| #11 §10, italic passage | "exactly the required drift" (unreconciled inside #11; see above) |

What the earlier readings described, weakening dark energy at low redshift, is still part of what DR2 reports. What they omit is the phantom phase above z ≃ 0.4, which is the part that bears on the program's bound. The lab notebook ([the lab notebook](/wiki/history/documents/lab-notebook)) and #9 ([the checkpoint](/wiki/history/documents/checkpoint)) are kept as the audit trail and were never edited; the superseded statements are also listed on [superseded statements](/wiki/status/superseded).

## Sources

- `CLAUDE.md` 'Since the handoff' — the current status: "under real pressure ahead of DR3"
- `papers/broken-born-checkpoint-v2.md` §10 — the "Under pressure (v2.1)" paragraph quoting DESI DR2, and the italic passage; header — the v2.1 change note
- `papers/broken-born-checkpoint-v2.md` ref [21] — DESI DR2 Results II (live-searched)
- `papers/broken-born-checkpoint-v2.md` §13 row 4 — the kill conditions and the DR2 clause
- `papers/broken-born-checkpoint-v2.md` §15 — "already leans against"; the degeneration risk
- `review/round3-adjudication.md` 'Rulings' 11, 'Decisions' 4 — the finding accepted, and §10 amended
- `review/round3/referee/audit-notes.md` Step 1, Step 4(c) item 11 — the referee's finding
- `HANDOFF.md` §2 — the superseded reading and the external clock with its three outcomes
- `notes/broken-born-program-v1.md` §8, `notes/broken-born-theory.md` §7 — earlier readings, superseded
- `notes/knot-dark-matter-standalone.md` §4, §5 — the reviewed sentence and exclusion condition 6 (withdrawn manuscript)
- `popsci/angle-of-the-mirror.md` 'The referee is already on the field', `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — "Three doors" and the popular readings (popular articles)
