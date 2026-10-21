---
title: "Obituary: superheavy conjugate solitons"
weight: 10
status: dead
description: "What #14 claimed, how it was built and tested in three blind reviews, why the corrected Kibble count overproduces the benchmark 2.1×10³–1.2×10⁴ times, the retirement decision, and what survives."
provenance: [V]
sources:
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Verdict'"
  - "review/round3-adjudication.md 'Rulings' 1–13"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Decisions' 1–3"
  - "review/round3-preregistration.md 'Protocol (HANDOFF §6, round 3)'"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/round3/referee/audit-notes.md Step 5"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/v3-worklog.md 'New open items'"
  - "review/v3-worklog.md 'Round 3 outcome (2026-10-19)'"
  - "review/skeptic-review-console.html"
  - "notes/knot-dark-matter-standalone.md Abstract"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
  - "verify/soliton_obituary.py"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §6"
  - "HANDOFF.md §8"
  - "popsci/angle-of-the-mirror.md 'Dividends and daydreams'"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*Superheavy conjugate solitons were the third dark-matter candidate of version 2.0 of the checkpoint: magnetic monopoles of a hidden gauge force, with a benchmark mass of 3×10¹³ GeV in the final version, stable because their field configuration cannot unwind and dark because no gauge force of ordinary matter acts on them. The proposal was written up as a standalone manuscript, #14, and reviewed blind three times. The third review re-ran every number in code and found that the count of monopoles formed in the early universe had been normalized far too low. Counted correctly, the benchmark mass is overproduced by a factor of 2.1×10³ to 1.2×10⁴, and the only version that survives is a much lighter one, which is an existing published scenario that does not depend on the program. The candidate was retired on 2026-10-19 and stays dead.*

**Status:** Dead — "Retired as a program-native candidate" on 2026-10-19 (#11 §12; round-3 Decision 2). The numbers that killed it are [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)); the literature on the surviving low-scale scenario is live-searched [28S, 29S]. Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate) among [the dark-sector candidates](/wiki/dark-matter/candidates). The rulings are in [round-3 verdict and rulings](/wiki/method/review/round-3/rulings) and the retirement in [round-3 decisions](/wiki/method/review/round-3/decisions); listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

### The third candidate of checkpoint v2.0

Version 2.0 of [the checkpoint](/wiki/history/documents/checkpoint), #11, offered three answers to the question of what dark matter is: particles of [conjugate matter χ](/wiki/dark-matter/candidates/chi-particles), [a coherent oscillation of the momentum graviton X](/wiki/dark-matter/candidates/x-condensate), and topological solitons. #11 §12 records the third:

> v2.0 listed topological solitons of a p-local gauge sector (§11) as a third candidate, stable by topological charge. It also claimed they slip through the Debt-3 loophole (§9), since topology, not collective dynamics, would localize them in momentum.

A p-local gauge sector is a gauge force of the momentum-polarized matter, the mirror half of the program's matter content under postulate [P4](/wiki/program/postulates/p4-polarized-matter). A soliton is a localized, finite-energy configuration of a field. It is stable by topological charge when the field far from its core wraps the space of vacuum states a whole number of times, and no smooth change of the field can alter that integer [T] ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)). The second claim concerned [Debt 3](/wiki/history/debts), which had shown that momentum-space clumping by collective dynamics is "nowhere mandatory": forbidden for particles, fatal where it would have been required of wave dark matter, and optional otherwise (#11 §9); a soliton localized in momentum by its own topology would have escaped that result ([the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).

When the candidate was retired, the adjudication named the two claims on which it had "earned its place in the checkpoint's trilemma": "topology makes it stable for free, and the mass came out of the abundance with no free dilution" (`review/round3-adjudication.md`, Decision 2). The review removed the second.

### The manuscript #14 in three versions

The candidate was developed into a standalone manuscript, #14, written to be reviewed without context and now kept as `notes/knot-dark-matter-standalone.md`. #11 §12: "superheavy 't Hooft–Polyakov monopoles of a hidden SU(2) → U(1) sector" ([the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). It went through three versions, and each fixed the monopoles' coupling and abundance differently.

| Version | How the coupling was fixed | Kibble normalization p | Mass claim | Review |
|---|---|---|---|---|
| v1 | Dirac quantization against our photon (`HANDOFF.md` §2) | not in the repository | not in the repository | round 1: "B / medium" |
| v2 | "the reciprocity map, acting as the modular S transformation", giving "alpha_d = 1/(4 alpha) ~ 34" | "p = O(1)" | "Benchmark M = 1e16 GeV"; "the window M ~ 1e13 to 1e17 GeV is the Kibble-only estimate" | round 2: "B near B/C / medium" |
| v3 | hypothesis H: "(g_d/2)^2/4pi = alpha" | "p ~ 0.023; we take p = 1 as the upper end" | "at about 1e13 to 4e13 GeV with no dilution required"; benchmark "M = 3e13 GeV" | round 3: C |

v1 is not in the repository and is known from the handoff's summary; v2 is in git history and verbatim inside `review/skeptic-review-console.html`, the tool used for the first two rounds; v3 is the withdrawn file (`HANDOFF.md` §3, §6; `review/v3-worklog.md`). The coupling's history is [the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling), and the normalization's is [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization).

v3's abstract states the final proposal: "We propose that dark matter consists of superheavy 't Hooft-Polyakov monopoles of a hidden SU(2) gauge sector broken to U(1). The hidden sector is identified with the momentum-polarized half of a spontaneously broken Born reciprocity." Its summary of the candidate: "The candidate is stable by topology, dark by sector separation, effectively collisionless, and inaccessible to direct detection." Here [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) is the symmetry (x, p) → (p, −x) whose spontaneous breaking is the program's [hard core](/wiki/program/hard-core), and sector separation is the postulate that no field carries charge under both the hidden force and ours.

## How it was tested

### Rounds 1 and 2: blind review without code

The first two reviews ran through [the skeptic console](/wiki/method/review/skeptic-console), a browser page that "sends #14 verbatim to a fresh Claude (claude-sonnet-4-6, web search on, adversarial referee prompt)" (`HANDOFF.md` §3). Round 1 graded v1 "B / medium". Its valid findings were folded into v2: the contradiction in fixing the coupling against our photon, an inverted citation of Preskill, the missing treatment of kinetic mixing, a renaming ("knots" became "π₂ monopole-class"), gravitational-wave backgrounds and the demand for a toy Lagrangian as acceptance criterion 1. Round 2 graded v2 "B near B/C / medium", named the coupling derivation as the weakest link, and left seven items pending for v3 (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

Neither referee could execute code. Their own arithmetic produced three confident order-of-magnitude indictments, all of them unit errors by the referee, so the handoff concluded that such referees are "unreliable on unaided arithmetic" ([the referee failure mode](/wiki/method/review/referee-failure-mode)). That was the reason for the program's [iron rule](/wiki/method/verification/iron-rule): every asserted number gets executed code.

### The v3 worklog

v3 was cut from the round-2 list in `review/v3-worklog.md`, a chunked log of the seven pending items (R1–R7), findings neither referee had raised (F1, F2, L1) and new open items (O1–O3), with Paul's decisions recorded as they were made. Two of its findings changed the candidate. F1 found that the Kibble estimate fixes a single mass rather than a window ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction#superseded-the-point-not-a-window-of-the-v3-worklog)), so the benchmark moved from 10¹⁶ to 3×10¹³ GeV. O1 found that the minimal hidden sector, with only the symmetry-breaking scalar, leaves stable heavy charged vector bosons that overclose the universe, so a light hidden fermion ψ was added ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)). Every number v3 quotes was gated in a script, `knot_numbers.py`, since replaced.

### Round 3: blind review with code execution

Before the third review, the expected outcome was committed in `review/round3-preregistration.md` ([the round-3 pre-registration](/wiki/method/review/round-3/preregistration)): verdict B, "confidence medium"; weakest link "the framework does no work"; and on arithmetic, "zero surviving numerical indictments". The referee was "a fresh subagent with shell, Python (numpy/sympy/scipy) and web search", given "only a copy of the manuscript and the protocol", with five steps: verify every citation, re-check every number "from independently chosen constants", re-derive the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), audit the concepts and omitted constraints, and give a verdict with its single weakest link.

The adjudication records the outcome: "**Referee: C (fundamentally flawed), medium confidence. I agree for v3 as written.**" and "Every one of its 16 numerical findings rests on executed code." The referee's single weakest link was "the Kibble abundance / mass determination", with "the framework does no work" second (`review/round3/referee/audit-notes.md`, Step 5). The adjudicator checked the central finding with an arbitration script of its own ([round-3 arbitration](/wiki/method/review/round-3/arbitration)) and ruled on thirteen findings ([review round 3](/wiki/method/review/round-3)).

## Why it failed

### The count of monopoles was normalized too low

A symmetry-breaking transition in the early universe leaves topological defects behind. The standard estimate of how many is [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism): regions farther apart than the horizon cannot coordinate their choice of vacuum, so at least about one defect forms per horizon volume [T]. The manuscript wrote the yield, the number of monopoles per unit entropy, as n/s = p (T_c/M_Pl)³, with T_c the transition temperature and M_Pl the Planck mass. #11 §12:

> The Kibble estimate n/s = p (T_c/M_Pl)³ had been normalized at p = 1 (#14 v2) and p ≈ 0.023 (#14 v3).
>
> One defect per Hubble volume gives p ≈ 104 [V], and that is the causal minimum; Kibble–Zurek and bubble-nucleation production only add to it [28S].

v3's value had dropped the numerical prefactor of the expansion rate, a factor of about 4.6×10³ (ruling 1, upheld). The adjudicator, who had drafted v3, noted: "My error came from misremembering the formula." The derivation, the reduced-Planck convention and why the manuscript's own check passed are on [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization).

### The benchmark is overproduced

A larger yield means more monopoles per unit entropy, so the mass at which they make up exactly the observed dark matter falls. #11 §12: "At minimum production the abundance closes at M ≈ 2.9–4.4×10¹² GeV [V], and the v3 benchmark of 3×10¹³ GeV is overproduced by 2.1×10³–1.2×10⁴ [V]. Realistic production lowers the viable mass much further." Ruling 2 (upheld) adds that the manuscript's reduced-Planck "factor of about 3" was not a spread at all: "consistently normalized, the two conventions agree." The relation and its inputs are on [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction).

### Realistic production makes it worse

One defect per horizon volume is a floor. Slow (Kibble–Zurek) dynamics at a continuous transition and bubble collisions at a first-order one both make more defects (ruling 3, upheld). The referee integrated Kibble–Zurek production followed by annihilation in the hidden plasma and found the benchmark still overproduced; the adjudicator records that it "did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction)", so those figures are accepted, not verified.

### Where hidden monopoles can be the dark matter

#11 §12 states where the published literature allows hidden-sector monopoles to make up the dark matter:

> Hidden-sector monopoles avoid overclosing the universe only for symmetry-breaking scales ≲ 100 PeV, or with a period of early matter domination [29S].
>
> Below that scale, annihilation in the hidden plasma sets the abundance. That is the established topological-dark-matter scenario [28S, 29S], and nothing in it depends on Born reciprocity.
>
> Superheavy masses survive only with a free dilution factor. That removes the mass prediction, which was the candidate's reason to exist.

The low-scale scenario is [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art); dilution by a late epoch is described in [inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution).

### The other rulings

The abundance finding was decisive, and most of the remaining rulings fell on the hidden sector v3 had built around the candidate (`review/round3-adjudication.md`, 'Rulings'):

| Ruling | Finding | Outcome | Page |
|---|---|---|---|
| 4 | the ψ relic window is too high | upheld | [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) |
| 5 | the hidden temperature bound is ξ < 0.760, not 0.77 | upheld (minor) | [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) |
| 6 | MeV-scale ψ freezes out during nucleosynthesis | accepted, not re-checked | [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) |
| 7 | the "O(1) coefficient at the Planck scale" of the dimension-5 mixing operator is unsupported | upheld | [Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) |
| 8 | Baumgart et al. lack the adjoint operator | overturned | [Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) |
| 9 | with mixing and a hidden θ, the monopoles carry a small visible electric charge | accepted, not re-checked | [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) |
| 10 | annihilation at α_m ≈ 34 "is Preskill's Dirac case, already done for hidden sectors" | upheld (abstract level) | [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art) |
| 11 | the Dark Energy Spectroscopic Instrument's Data Release 2 (DESI DR2) best fit crosses into phantom above z ≈ 0.4 | accepted | [the DR2 phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) |
| 12 | minor citation issues | accepted | [review round 3](/wiki/method/review/round-3) |
| 13 | v3 §6's "all numbers computed by executed code" overstates | upheld in substance | [#14's self-assessment](#14s-self-assessment) below |

### The pre-registration, scored

The adjudication scored its own predictions: verdict B against outcome C, "**Miss**: the first after 2 for 2"; the weakest link, "**Miss on #1** (hit on #2)"; zero surviving numerical indictments, a miss, since "Three survive (p; the ψ window; ξ), plus the ε coefficient", all of them "wrong inputs or model choices in my scripts, not arithmetic slips"; and all 23 citations resolving, a hit. It drew the lesson that the failure mode had moved: in rounds 1 and 2 it was the referee's unaided arithmetic, and "In round 3 it is that **the author's verification checks the author's model**: a wrong physics input passes a gate that tests only arithmetic." That lesson is [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model), and its companion, that a check must rest on an anchor independent of the paper, is [independent anchors](/wiki/method/verification/independent-anchors).

## The decision

Paul delegated the follow-up decisions on 2026-10-19; Claude made them, and Paul keeps the veto (`review/round3-adjudication.md`, 'Decisions'). Decision 2 set out three routes:

- **Route (a)**, claim the low-scale model: "Route (a), v ≲ 100 PeV, works, but it is Murayama–Shu's and Liveoak–Maharana–Wells's model. Nothing in it depends on Born reciprocity (the referee and the pre-registration agree), so claiming it would add no testable content and would misattribute it."
- **Route (b)**, keep the superheavy mass and name a dilution mechanism: rejected, because it "restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass would then no longer be a prediction, and the program does not trade falsifiability for survival."
- **Route (c)**, retire: chosen. "The soliton candidate: retired as a program-native proposal (route c). The surviving version is noted as prior art (route a)."

The decision cites the program's precedent, the obituary of momentum clumping: "a dead claim is reported prominently and stays dead" ([momentum clumping](/wiki/dark-matter/momentum-clumping)). Its consequence: "the trilemma becomes two program-native candidates (gated χ particles; the X-condensate), plus the remark that the framework is compatible with known PeV-scale topological dark matter."

The same day, v3 was moved from `papers/` to `notes/` with a banner, "Kept as the audit trail; not for circulation", and the script `knot_numbers.py`, which had checked v3's own claims, was replaced by `verify/soliton_obituary.py`, which checks the corrected record against independent anchors. The adjudication adds: "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything." ([the gate](/wiki/method/verification/the-gate)). Decision 3 dropped the handoff's queued "√N floor" calculation, whose premise was inverted and which had no candidate left to serve ([the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)).

**The verdict** (#11 §12): "Retired as a program-native candidate. The framework is compatible with the prior-art PeV-scale scenario and adds nothing testable to it." The root `CLAUDE.md` records the candidate as "**dead** as a program-native proposal" and adds: "The framework is merely compatible with known PeV-scale topological dark matter (prior art)." #11 v2.1's abstract summarizes the episode: the candidate "was retired after an execution-verified review found its abundance estimate misnormalized (§12), leaving two candidates: particles and a condensate", and its predictions table lists "superheavy-soliton dark matter (obituary §12)" under "Withdrawn with cause" (§13).

## What survives

#11 §12 lists three survivors:

- "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]." If the smallest hidden electric charge is weak, [Dirac's quantization condition](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) forces the magnetic charge to be large, so the monopoles' mutual coupling is strong ([the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#what-survives)).
- "The minimal adjoint-only SU(2) → U(1) hidden sector is excluded on its own terms: its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V]" ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)).
- "The Debt-3 loophole — topological momentum-space localization of individual objects — remains untested, but has no candidate."

The adjudication's own list, "What survives v3", overlaps: "The compatibility theorem (as [T], pending the FLM comparison)", since credited to Freidel–Leigh–Minic (FLM) in #11 §5; "The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′ overclosure" ([benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)); "The kinetic-mixing literature points (a) and (c)" ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)); and "The statement that the minimal adjoint-only sector is excluded." The two lists differ. #11 §12 adds the Dirac result and the loophole; of the adjudication's other items, #11 carries the compatibility theorem in §5 and gravity-induced mixing in P4 (§4), and does not restate the benchmark-conditional arithmetic or point (c). The corrected abundance itself also stands as a result, [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction).

Two further points are untouched. The ontology of conjugate monopoles is alive: "by P4, conjugate-sector solitons gravitate", while "Their candidacy as the dark matter itself is retired in v2.1 (§12)" (#11 §11.1; [conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)). And the decision on kinetic mixing that came out of the same review, strict sector separation (Decision 1), is now part of postulate P4.

The loophole is worded two ways in #11. §12 says it "remains untested, but has no candidate"; §14 item 8 says "The soliton-spectrum and p-localization items are closed by the §12 obituary." The sources do not reconcile the two; [the conflicts register](/wiki/history/documents/source-conflicts) reads them together as a loophole that is logically untested with no candidate or work item attached.

## #14's self-assessment

v3 ended with an assessment of its own claims (§5–§6), which round 3 tested.

**Seven exclusion conditions** (§5), each a finding that would have killed the proposal: a confirmed non-gravitational coupling between the dominant dark matter and the Standard Model; a confirmed monopole flux of our electromagnetism at dark-matter abundance; exclusion of the millicharged ψ window; a strong-coupling relic calculation that cannot leave the observed abundance; a demonstration that dwarf-galaxy cores require dark-sector self-interaction; a robust measurement of constant w = −1 or intrinsic w < −1; and internal failures, among them "instability of a heavy spin-2 field at equal Planck masses" ([stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)).

**Claim categories** (§6). "Derived within the framework or by standard methods" included "the failure of the adjoint-only model and the psi relic window" and "the Kibble-consistent mass". "Conjectural" included "hypothesis H", "the identification of the SU(2)_d sector as the momentum-polarized matter sector" and "the colder reheating of the hidden sector". The Kibble-consistent mass and the ψ window were both overturned.

**Three "Requirements forced by consistency (not optional)"**: "(i) at least one hidden doublet fermion with mass between the MeV scale and ~0.1 TeV"; "(ii) a hidden-to-visible temperature ratio xi < 0.77 after reheating"; "(iii) an unbroken U(1)_d". Rulings 4 and 6 moved both edges of (i), and ruling 5 tightened (ii) to ξ < 0.760.

**Three acceptance criteria** (§6). (1), an action in which ρ is "a genuine Noether symmetry, spontaneously broken", is "Met in the referees' wording" by the toy models (#11 §14 item 11), which do not address its second half, η selecting "the hidden sector's electric description" ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)). (2), a gauged hidden charge conjugation or a surviving millicharged-ψ window, concerned the ψ-millicharge channel, one of the three that Decision 1, strict sector separation, closes. (3), "the strong-coupling relic freeze-out calculation", was ruled already done in the literature (ruling 10, upheld at abstract level).

**Its claim about its own numbers.** §6 opened: "All numerical statements in Secs. 2-4 were computed by executed code rather than by hand." Ruling 13 found this "Upheld in substance": "The code checked the arithmetic of a wrong model."

## Superseded: the handoff's "current best" candidate

`HANDOFF.md`, written before round 3, listed among the live results the "Current best DM candidate: superheavy (~10¹³–10¹⁷ GeV) topological solitons (π₂ monopole-class) of a separate, strongly coupled dual gauge sector" (§2; DM is dark matter), dark by sector separation and not magnetically charged under our photon. Its open items included "Strong-coupling relic freeze-out at α_d ~ 34" (item 2) and "Dark-sector trilemma discrimination: particles vs X-condensate vs solitons" (item 8), and its queue served the candidate in items 1–3: cut v3, re-run the audit, and the "√N-floor freeze-out estimate" (§8). Items 1 and 2 were done; item 3 was dropped by Decision 3. The handoff's §2 soliton candidate and its §8 queue are superseded by #11 §12, the adjudication and the root `CLAUDE.md` ([the handoff](/wiki/history/documents/handoff)).

## Popsci-only: the favoured corner of the three-way question

[The popular articles](/wiki/history/documents/popular-articles) still present the candidate as live. #10 describes "a three-way question with named experimental discriminators", the third being "topological knots — the conjugate sector's monopoles, unable to untie, which would explain dark matter's thirteen-billion-year stability for free". #12 goes further and states that "Three independent requirements — thirteen-billion-year stability, the strong coupling Dirac's condition demands, and transparency to light — select the same corner of the three-way question." Its figures, "around 10¹⁶ times the proton's" and "roughly one object per twenty-five cubic kilometers of local space", are those of v2's benchmark, "one soliton per ~25 km^3" (`review/skeptic-review-console.html`). The popular articles are never a source for a claim's status.

## Sources

- `CLAUDE.md` 'Since the handoff' — "dead as a program-native proposal"; "merely compatible"
- `papers/broken-born-checkpoint-v2.md` §12 — the obituary: claim, test, failure, verdict, survivors, and the [V] tags; §1 — the technical abstract; §9 — Debt 3's net theorem; §11.1 — conjugate monopoles as ontology; §13 — "Withdrawn with cause"; §14 item 8 — the loophole "closed"
- `review/round3-adjudication.md` 'Verdict', 'Rulings' 1–13, 'Pre-registration scored', 'What survives v3', 'Decisions' 1–3 — the review record and the retirement
- `review/round3-preregistration.md` 'Protocol (HANDOFF §6, round 3)', 'Predictions' — the referee's brief and the predicted outcome
- `review/round3/referee/audit-notes.md` Step 5 — the referee's weakest links
- `verify/soliton_obituary.py` — the gated numbers
- `review/v3-worklog.md` 'Findings neither referee raised', 'New open items', 'Round 3 outcome (2026-10-19)' — how v3 was cut, and its closure
- `HANDOFF.md` §2, §8 — the superseded "Current best" framing and queue; §3 — the console; §6 — rounds 1 and 2
- `notes/knot-dark-matter-standalone.md` Abstract, §5, §6 — the withdrawn manuscript's claims, exclusion conditions, requirements and acceptance criteria
- `review/skeptic-review-console.html` — #14 v2, verbatim
- `popsci/angle-of-the-mirror.md` 'Dividends and daydreams'; `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the popular framings
