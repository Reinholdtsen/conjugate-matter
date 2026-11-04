---
title: "Obituary: #14's superheavy-soliton model"
weight: 10
status: dead
description: "#14's model of the third dark-matter candidate, superheavy monopoles of a hidden gauge sector with ordinary kinematics: what it claimed, three blind reviews, the corrected Kibble count that overproduces its benchmark 2.1×10³–1.2×10⁴ times, the decision that retired it, and what survives; the candidate it modeled is P.R.'s open conjecture."
provenance: [V]
sources:
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "papers/broken-born-checkpoint-v2.md §11.4"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/knot-dark-matter-standalone.md §1"
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
  - "popsci/angle-of-the-mirror.md 'Corollaries and daydreams'"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
  - "review/wiki-build-flags.md item 21"
  - "review/wiki-build-flags.md item 60"
---

*#14's superheavy-soliton model was the withdrawn manuscript #14's version of the third dark-matter candidate of version 2.0 of the checkpoint: [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles) of [a hidden gauge force](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector), with a benchmark mass of 3×10¹³ GeV in the final version, stable because their field configuration cannot unwind, dark because no gauge force of ordinary matter acts on them, and described throughout with the kinematics of ordinary particles moving in space. The manuscript was [reviewed blind](/wiki/method/review) three times. The third review re-ran every number in code and found that the count of monopoles formed in the early universe had been [normalized far too low](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization). Counted correctly, the benchmark mass is overproduced by a factor of 2.1×10³ to 1.2×10⁴, and the only version that survives is a much lighter one, which is an existing published scenario that does not depend on the program. The model failed on 2026-10-19 and was retired. It never treated the monopoles as localized in momentum, so the candidate it modeled was not tested: that candidate is P.R.'s open conjecture, [magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles).*

**Status:** Dead — #14's model failed round 3 (verdict C, 2026-10-19) and was "retired as a program-native proposal" by round-3 Decision 2. The numbers that failed it are [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)); the literature on the surviving low-scale scenario is live-searched [28S, 29S]. The candidate it modeled is P.R.'s open conjecture [O] ([Conjecture: magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles)). Home section: [#14's soliton model](/wiki/dark-matter/candidates/soliton-candidate) among [the dark-sector candidates](/wiki/dark-matter/candidates). The rulings are in [round-3 verdict and rulings](/wiki/method/review/round-3/rulings) and the retirement in [round-3 decisions](/wiki/method/review/round-3/decisions); listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

### The third candidate of checkpoint v2.0

Version 2.0 of [the checkpoint](/wiki/history/documents/checkpoint), #11, offered three answers to the question of what [dark matter](/wiki/dark-matter) is: particles of [conjugate matter χ](/wiki/dark-matter/candidates/chi-particles), [a coherent oscillation of the momentum graviton X](/wiki/dark-matter/candidates/x-condensate), and [topological solitons](/wiki/symmetry-breaking/topological-defects#topological-and-non-topological-solitons-t). #11 §12 records the third:

> v2.0 listed topological solitons of a p-local gauge sector (§11) as a third candidate, stable by topological charge. It also claimed they slip through the clumping loophole (§9), since topology, not collective dynamics, would localize them in momentum.

A p-local gauge sector is a gauge force of the [momentum-polarized matter](/wiki/dark-matter/conjugate-matter), the mirror half of the program's matter content under postulate [P4](/wiki/program/postulates/p4-polarized-matter). A soliton is a localized, finite-energy configuration of a field. It is stable by topological charge when the field far from its core wraps the space of vacuum states a whole number of times, and no smooth change of the field can alter that integer [T] ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)). The second claim concerned the calculations of [the clumping problem](/wiki/history/main-problems). They had tested momentum-space clumping by collective dynamics under the program's [contact-range interaction](/wiki/dark-matter/momentum-clumping/founding-image#the-scope-of-the-tests), which acts only over microscopic distances. #11 §9 states their net theorem: "velocity-space clumping is nowhere mandatory — forbidden (particles), fatal (committed wave), decorative (free wave)" ([the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem)); the committed-wave case, Scenario A, is under review ([Under review: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)). A soliton localized in momentum by its own topology would have escaped that result ([the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)). The results of those calculations stand, and the founding image itself is P.R.'s open conjecture [O] ([Conjecture: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)).

That candidate is the third row of #11 §12's table, P.R.'s conjecture [O]: "magnetically charged topological solitons of the p-polarized sector, localized in momentum (§11, §11.4)" ([Conjecture: magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles)). This page is the obituary of #14's model of it, not of the candidate.

When #14's model was retired, the adjudication named the two claims on which the candidate had "earned its place in the checkpoint's trilemma": "topology makes it stable for free, and the mass came out of the abundance with no free dilution" (`review/round3-adjudication.md`, Decision 2). The review removed the second, which was the model's.

### The manuscript #14 in three versions

The candidate was developed into a standalone manuscript, #14, written to be reviewed without context and now kept as `notes/knot-dark-matter-standalone.md`. #11 §12: "superheavy 't Hooft–Polyakov monopoles of a hidden SU(2) → U(1) sector" ([the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). It went through three versions, and each fixed the monopoles' coupling and abundance differently.

| Version | How the coupling was fixed | Kibble normalization p | Mass claim | Review |
|---|---|---|---|---|
| v1 | [Dirac quantization against our photon](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#attempt-1-dirac-quantization-against-our-photon) (`HANDOFF.md` §2) | not in the repository | not in the repository | round 1: "B / medium" |
| v2 | "the reciprocity map, acting as the modular S transformation", giving "alpha_d = 1/(4 alpha) ~ 34" | "p = O(1)" | "Benchmark M = 1e16 GeV"; "the window M ~ 1e13 to 1e17 GeV is the Kibble-only estimate" | round 2: "B near B/C / medium" |
| v3 | [hypothesis H](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#attempt-3-hypothesis-h): "(g_d/2)^2/4pi = alpha" | "p ~ 0.023; we take p = 1 as the upper end" | "at about 1e13 to 4e13 GeV with no dilution required"; benchmark "M = 3e13 GeV" | round 3: C |

v1 is not in the repository and is known from the handoff's summary; v2 is in git history and verbatim inside `review/skeptic-review-console.html`, the tool used for the first two rounds; v3 is the withdrawn file (`HANDOFF.md` §3, §6; `review/v3-worklog.md`). The coupling's history is [the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling), and the normalization's is [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization).

v3's abstract states the final proposal: "We propose that dark matter consists of superheavy 't Hooft-Polyakov monopoles of a hidden SU(2) gauge sector broken to U(1). The hidden sector is identified with the momentum-polarized half of a spontaneously broken Born reciprocity." Its summary of the candidate: "The candidate is stable by topology, dark by sector separation, effectively collisionless, and inaccessible to direct detection." Here [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) is the symmetry (x, p) → (p, −x) whose spontaneous breaking is the program's [hard core](/wiki/program/hard-core), and sector separation is the postulate that no field carries charge under both the hidden force and ours.

#14 used ordinary kinematics throughout (#11 §12), and v3 says so in its framework section:

> Kinematics. Throughout, the hidden sector is described by ordinary relativistic quantum field theory. Whether the parent framework requires a different kinematics for momentum-polarized matter is an open question that this proposal does not use. (#14 §1)

Its monopoles were therefore localized in position, like ordinary particles. #11 §12: "It did not model the localization in momentum that v2.0 claimed."

## How it was tested

### Rounds 1 and 2: blind review without code

The first two reviews ran through [the skeptic console](/wiki/method/review/skeptic-console), a browser page that "sends #14 verbatim to a fresh Claude (claude-sonnet-4-6, web search on, adversarial referee prompt)" (`HANDOFF.md` §3). Round 1 graded v1 "B / medium". Its valid findings were folded into v2: the contradiction in fixing the coupling against our photon, an inverted citation of Preskill, the missing treatment of kinetic mixing, a renaming ("knots" became "π₂ monopole-class"), [gravitational-wave backgrounds](/wiki/cosmology/early-universe/phase-transition-gravitational-waves) and the demand for a toy Lagrangian as [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion). Round 2 graded v2 "B near B/C / medium", named the coupling derivation as the weakest link, and left seven items pending for v3 (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

Neither referee could execute code. Their own arithmetic produced three confident order-of-magnitude indictments, all of them unit errors by the referee, so the handoff concluded that such referees are "unreliable on unaided arithmetic" ([the referee failure mode](/wiki/method/review/referee-failure-mode)). That was the reason for the program's [iron rule](/wiki/method/verification/iron-rule): every asserted number gets executed code.

### The v3 worklog

v3 was cut from the round-2 list in `review/v3-worklog.md`, a chunked log of the seven pending items (R1–R7), findings neither referee had raised (F1, F2, L1) and new open items (O1–O3), with the decisions recorded as they were made. Two of its findings changed the model. F1 found that the Kibble estimate fixes a single mass rather than a window ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction#superseded-the-point-not-a-window-of-the-v3-worklog)), so the benchmark moved from 10¹⁶ to 3×10¹³ GeV. O1 found that the minimal hidden sector, with only the symmetry-breaking scalar, leaves stable heavy charged vector bosons that overclose the universe, so a light hidden fermion ψ was added ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)). Every number v3 quotes was gated in a script, `knot_numbers.py`, since replaced.

### Round 3: blind review with code execution

Before the third review, the expected outcome was committed in `review/round3-preregistration.md` ([the round-3 pre-registration](/wiki/method/review/round-3/preregistration)): verdict B, "confidence medium"; weakest link "the framework does no work"; and on arithmetic, "zero surviving numerical indictments". The referee was "a fresh subagent with shell, Python (numpy/sympy/scipy) and web search", given "only a copy of the manuscript and the protocol", with five steps: verify every citation, re-check every number "from independently chosen constants", re-derive the [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), audit the concepts and omitted constraints, and give a verdict with its single weakest link.

The adjudication records the outcome: "**Referee: C (fundamentally flawed), medium confidence. I agree for v3 as written.**" and "Every one of its 16 numerical findings rests on executed code." The referee's single weakest link was "the Kibble abundance / mass determination", with "the framework does no work" second (`review/round3/referee/audit-notes.md`, Step 5). The adjudicator checked the central finding with an arbitration script of its own ([round-3 arbitration](/wiki/method/review/round-3/arbitration)) and ruled on thirteen findings ([review round 3](/wiki/method/review/round-3)).

## Why it failed

### The count of monopoles was normalized too low

A symmetry-breaking transition in the early universe leaves topological defects behind. The standard estimate of how many is [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism): regions farther apart than the horizon cannot coordinate their choice of vacuum, so at least about one defect forms per horizon volume [T]. The manuscript wrote the [yield](/wiki/cosmology/early-universe/relic-yield-and-dilution#the-kibble-yield-t), the number of monopoles per unit entropy, as n/s = p (T_c/M_Pl)³, with T_c the transition temperature and M_Pl the [Planck mass](/wiki/gravity/spin-2-fields/planck-units). #11 §12:

> The Kibble estimate n/s = p (T_c/M_Pl)³ had been normalized at p = 1 (#14 v2) and p ≈ 0.023 (#14 v3).
>
> One defect per Hubble volume gives p ≈ 104 [V], and that is the causal minimum; Kibble–Zurek and bubble-nucleation production only add to it [28S].

v3's value had dropped the numerical prefactor of the expansion rate, a factor of about 4.6×10³ (ruling 1, upheld). The adjudicator, who had drafted v3, noted: "My error came from misremembering the formula." The derivation, the reduced-Planck convention and why the manuscript's own check passed are on [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization).

### The benchmark is overproduced

A larger yield means more monopoles per unit entropy, so the mass at which they make up exactly the observed dark matter falls. #11 §12: "At minimum production the abundance closes at M ≈ 2.9–4.4×10¹² GeV [V], and the v3 benchmark of 3×10¹³ GeV is overproduced by 2.1×10³–1.2×10⁴ [V]. Realistic production lowers the viable mass much further." Ruling 2 (upheld) adds that the manuscript's reduced-Planck "factor of about 3" was not a spread at all: "consistently normalized, the two conventions agree." The relation and its inputs are on [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction).

### Realistic production makes it worse

One defect per horizon volume is a floor. Slow (Kibble–Zurek) dynamics at a continuous transition and bubble collisions at a first-order one both make more defects (ruling 3, upheld). The referee integrated Kibble–Zurek production followed by annihilation in the hidden plasma and found the benchmark still overproduced; the adjudicator records that it "did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction)", so those figures are accepted, not verified. Flag 21 in `review/wiki-build-flags.md` notes that the lower end of that range comes from an analytic estimate in the literature, not from the referee's integration.

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
| 5 | the [hidden temperature](/wiki/cosmology/early-universe/hidden-sector-temperature#the-bound-on-ξ) bound is ξ < 0.760, not 0.77 | upheld (minor) | [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) |
| 6 | MeV-scale ψ [freezes out](/wiki/dark-matter/candidates/thermal-freeze-out#the-hidden-sector-of-14s-model) during [nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#the-ψ-relic-windows-lower-edge) | accepted, not re-checked | [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) |
| 7 | the "O(1) coefficient at the Planck scale" of the dimension-5 mixing operator is unsupported | upheld | [Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) |
| 8 | Baumgart et al. lack the adjoint operator | overturned | [Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) |
| 9 | with mixing and a hidden θ, the monopoles carry a small visible electric charge | accepted, not re-checked | [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) |
| 10 | annihilation at α_m ≈ 34 "is Preskill's Dirac case, already done for hidden sectors" | upheld (abstract level) | [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art) |
| 11 | the Dark Energy Spectroscopic Instrument's Data Release 2 (DESI DR2) best fit crosses into phantom above [redshift](/wiki/cosmology/scale-factor-duality/redshift) z ≈ 0.4, z being the stretching of light by the expansion of the universe since the light was emitted (larger z means earlier) | accepted | [the DR2 phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) |
| 12 | minor citation issues | accepted | [round-3 rulings](/wiki/method/review/round-3/rulings#ruling-12-minor-citation-issues) |
| 13 | v3 §6's "all numbers computed by executed code" overstates | upheld in substance | [#14's self-assessment](#14s-self-assessment) below |

### The pre-registration, scored

The adjudication scored the pre-registered predictions: verdict B against outcome C, "**Miss**: the first after 2 for 2"; the weakest link, "**Miss on #1** (hit on #2)"; zero surviving numerical indictments, a miss, since "Three survive (p; the ψ window; ξ), plus the ε coefficient", all of them "wrong inputs or model choices in my scripts, not arithmetic slips"; and all 23 citations resolving, a hit. It drew the lesson that the failure mode had moved: in rounds 1 and 2 it was the referee's unaided arithmetic, and "In round 3 it is that **the author's verification checks the author's model**: a wrong physics input passes a gate that tests only arithmetic." That lesson is [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model), and its companion, that a check must rest on an anchor independent of the paper, is [independent anchors](/wiki/method/verification/independent-anchors).

## The decision

The decisions of 2026-10-19 that followed the review are in `review/round3-adjudication.md`, 'Decisions'. Decision 2 set out three routes:

- **Route (a)**, claim the low-scale model: "Route (a), v ≲ 100 PeV, works, but it is Murayama–Shu's and Liveoak–Maharana–Wells's model. Nothing in it depends on Born reciprocity (the referee and the pre-registration agree), so claiming it would add no testable content and would misattribute it."
- **Route (b)**, keep the superheavy mass and name a dilution mechanism: rejected, because it "restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass would then no longer be a prediction".
- **Route (c)**, retire: chosen. "The soliton candidate: retired as a program-native proposal (route c). The surviving version is noted as prior art (route a)."

The decision's consequence: "the trilemma becomes two program-native candidates (gated χ particles; the X-condensate), plus the remark that the framework is compatible with known PeV-scale topological dark matter." The decision covers #14's model, which used ordinary kinematics; the candidate it modeled, conjugate monopoles localized in momentum, is P.R.'s open conjecture.

The same day, v3 was moved from `papers/` to `notes/` with a banner, "Kept as the audit trail; not for circulation", and the script `knot_numbers.py`, which had checked v3's own claims, was replaced by `verify/soliton_obituary.py`, which checks the corrected record against independent anchors. The adjudication adds: "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything." ([the gate](/wiki/method/verification/the-gate)). Decision 3 dropped the handoff's queued "√N floor" calculation: "Its premise, Kibble as a ceiling, is inverted (ruling 3)", and "Under decision 2 it has no candidate left to serve" (the candidate meant is #14's model, which Decision 2 covers; [the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)).

**The verdict.** #11 §12:

> #14's model fails as a program-native proposal: with ordinary kinematics it is either overproduced or the prior-art PeV-scale scenario, to which the framework adds nothing testable.

Its technical abstract says that "#14's model of it, superheavy solitons of a hidden gauge sector with ordinary kinematics, failed after an execution-verified review found its abundance estimate misnormalized (§12)", and its [predictions table](/wiki/predictions) lists the model under "Withdrawn with cause" (§13). The root `CLAUDE.md` adds: "The framework is merely compatible with known PeV-scale topological dark matter (prior art)."

**The model's parts.** Six of the model's components are under review ([claims under review](/wiki/status/under-review)): [the hidden SU(2) → U(1) sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector), [α_d ≈ 34 via our photon](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling), [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization), [the √N floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor), [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) and [the dimension-five operator](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator). Hypothesis H, the third way #14 fixed α_d ≈ 34, is under review with that coupling ([hypothesis H](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#attempt-3-hypothesis-h)). The model's own outputs and claims, such as its headline mass band, fell with the model ([parts of #14's soliton model](/wiki/status/graveyard#parts-of-14s-soliton-model)).

## What survives

#11 §12 lists three survivors:

- "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]." If the smallest hidden electric charge is weak, [Dirac's quantization condition](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) forces the magnetic charge to be large, so the monopoles' mutual coupling is strong ([the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#what-stands)).
- "The minimal adjoint-only SU(2) → U(1) hidden sector is excluded on its own terms: its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V]" ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)). The same exclusion was published first, independently, for the minimal model ([in the literature](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure#in-the-literature); flag 68 in `review/wiki-build-flags.md`, pending).
- "The clumping loophole — topological momentum-space localization of individual objects — remains untested; its candidate is P.R.'s conjecture of conjugate monopoles (table above)."

The adjudication's own list, "What survives v3", overlaps: "The compatibility theorem (as [T], pending the FLM comparison)", since credited to [Freidel–Leigh–Minic](/wiki/phase-space/reciprocity/broken-born-duality) (FLM) in #11 §5; "The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′ overclosure" ([benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)); "The kinetic-mixing literature points (a) and (c)" ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)); and "The statement that the minimal adjoint-only sector is excluded." The two lists differ. #11 §12 adds the Dirac result and the loophole; of the adjudication's other items, #11 carries the compatibility theorem in §5 and gravity-induced mixing in P4 (§4), and does not restate the benchmark-conditional arithmetic or point (c). The corrected abundance itself also stands as a result, [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction).

Two further points are untouched. The ontology of conjugate monopoles is alive: "by P4, conjugate-sector solitons gravitate", and "P.R. conjectures that they are abundant in momentum space"; their candidacy as the dark matter is open (§12): #14's model of it failed, and "the candidate itself was never modeled" (#11 §11.1; [conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)). And the decision on kinetic mixing that came out of the same review, strict sector separation (Decision 1), is part of postulate P4.

The identification that #14 v2 made its load-bearing conjecture, the momentum-polarized sector as the [S-dual](/wiki/electric-magnetic-duality/s-duality) image of the electric sector, its image under the exchange of electric and magnetic charge, is related to P.R.'s magnetic-mirror conjecture, open [O] (#11 §11.4): "momentum matter is similar to position matter, each electrically charged x-polarized particle having a magnetically charged p-polarized analog". #14 v2's identification is the conjecture's separate-photon form, in which the analogs are magnetic under the momentum-polarized sector's own gauge field. The worklog's finding F2, that #14 v2 used both a weak and a strong value of the dual coupling, stands (#11 §11.4; flag 60), and #14 is withdrawn ([Conjecture: the momentum sector as the magnetic mirror](/wiki/electric-magnetic-duality/magnetic-identification)).

The loophole has open work items: #11 §14 item 8 lists the soliton spectrum and p-localization as open, since the third candidate of §12 and §11.4's shared-photon form need p-localization, "p-local solitons are p-localized" [O] ([shared photon](/wiki/electric-magnetic-duality/magnetic-identification#shared-photon)).

## What the model did not test

#14 described its hidden sector with ordinary kinematics (#14 §1), so it did not test v2.0's claim that topology would localize the candidate's solitons in momentum. #11 states the consequence in §12's plain-language passage: "The model never treated the defects as localized in momentum, so the candidate itself has not been tested." The candidate is therefore outside this obituary. It is the third row of §12's table, P.R.'s conjecture, with the handle "untested: p-localization open (§14 item 8); #14's model, with ordinary kinematics, failed (below)". What it needs, beginning with a derivation that the sector's solitons are localized in momentum, is on [Conjecture: magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles).

## #14's self-assessment

v3 ended with an assessment of its own claims (§5–§6), which round 3 tested.

**Seven exclusion conditions** (§5), each a finding that would have killed the proposal: a confirmed non-gravitational coupling between the dominant dark matter and the Standard Model; a confirmed monopole flux of our electromagnetism at dark-matter abundance; exclusion of the millicharged ψ window; a strong-coupling relic calculation that cannot leave the observed abundance; a demonstration that [dwarf-galaxy cores](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) require dark-sector self-interaction; a robust measurement of constant w = −1 or [intrinsic w < −1](/wiki/cosmology/dark-energy/no-phantom-bound), where w is dark energy's [equation of state](/wiki/cosmology/dark-energy/quintessence#dark-energy-and-the-equation-of-state), its pressure divided by its energy density, and −1 is its value for a cosmological constant; and internal failures, among them "instability of a heavy spin-2 field at equal Planck masses" ([stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)).

**Claim categories** (§6). "Derived within the framework or by standard methods" included "the failure of the adjoint-only model and the psi relic window" and "the Kibble-consistent mass". "Conjectural" included "hypothesis H", "the identification of the SU(2)_d sector as the momentum-polarized matter sector" and "the colder reheating of the hidden sector". Round 3 overturned both the Kibble-consistent mass and the ψ window.

**Three "Requirements forced by consistency (not optional)"**: "(i) at least one hidden doublet fermion with mass between the MeV scale and ~0.1 TeV"; "(ii) a hidden-to-visible temperature ratio xi < 0.77 after reheating"; "(iii) an unbroken U(1)_d". Rulings 4 and 6 moved both edges of (i), and ruling 5 tightened (ii) to ξ < 0.760.

**Three acceptance criteria** (§6). (1), an action in which ρ is "a genuine Noether symmetry, spontaneously broken", is "Met in the referees' wording" by the toy models (#11 §14 item 11), which do not address its second half, η selecting "the hidden sector's electric description" ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)). (2), a gauged hidden charge conjugation or a surviving millicharged-ψ window, concerned the ψ-millicharge channel, one of the three that Decision 1, strict sector separation, closes. (3), "the strong-coupling relic freeze-out calculation", was ruled already done in the literature (ruling 10, upheld at abstract level).

**Its claim about its own numbers.** §6 opened: "All numerical statements in Secs. 2-4 were computed by executed code rather than by hand." Ruling 13 found this "Upheld in substance": "The code checked the arithmetic of a wrong model."

## Superseded: the handoff's "current best" candidate

`HANDOFF.md`, written before round 3, listed among the live results the "Current best DM candidate: superheavy (~10¹³–10¹⁷ GeV) topological solitons (π₂ monopole-class) of a separate, strongly coupled dual gauge sector" (§2; DM is dark matter), dark by sector separation and not magnetically charged under our photon. Its open items included "Strong-coupling relic freeze-out at α_d ~ 34" (item 2) and "Dark-sector trilemma discrimination: particles vs X-condensate vs solitons" (item 8), and its queue served the candidate in items 1–3: cut v3, re-run the audit, and the "√N-floor freeze-out estimate" (§8). Items 1 and 2 were done; item 3 was dropped by Decision 3. The handoff's §2 soliton candidate and its §8 queue are superseded by #11 §12, the adjudication and the root `CLAUDE.md` ([the handoff](/wiki/history/documents/handoff)).

## Popsci-only: the favoured corner of the three-way question

[The popular articles](/wiki/history/documents/popular-articles) still present the candidate in its superheavy form, #14's, as live. #10 describes "a three-way question with named experimental discriminators", the third being "topological knots — the conjugate sector's monopoles, unable to untie, which would explain dark matter's thirteen-billion-year stability for free". #12 goes further and states that "Three independent requirements — thirteen-billion-year stability, the strong coupling Dirac's condition demands, and transparency to light — select the same corner of the three-way question." Its figures, "around 10¹⁶ times the proton's" and "roughly one object per twenty-five cubic kilometers of local space", are those of v2's benchmark, "one soliton per ~25 km^3" (`review/skeptic-review-console.html`). The popular articles are never a source for a claim's status.

## Sources

- `CLAUDE.md` 'Since the handoff' — #14's model; "merely compatible"; six of its components under review, and hypothesis H under review with the coupling α_d ≈ 34
- `papers/broken-born-checkpoint-v2.md` §12 — #14's model of the third candidate: claim, ordinary kinematics, test, failure, verdict, survivors, and the [V] tags; the candidate's row, P.R.'s conjecture; §1 — the technical abstract; §9 — the clumping problem's net theorem, and the founding image as P.R.'s open conjecture; §11.1 — conjugate monopoles as ontology, and the candidacy open; §11.4 — the magnetic-mirror conjecture, #14 v2's related identification, and F2's finding; §13 — "Withdrawn with cause"; §14 item 8 — p-localization, open
- `review/round3-adjudication.md` 'Verdict', 'Rulings' 1–13, 'Pre-registration scored', 'What survives v3', 'Decisions' 1–3 — the review record, and the retirement, which covers #14's model
- `review/round3-preregistration.md` 'Protocol (HANDOFF §6, round 3)', 'Predictions' — the referee's brief and the predicted outcome
- `review/round3/referee/audit-notes.md` Step 5 — the referee's weakest links
- `verify/soliton_obituary.py` — the gated numbers
- `review/v3-worklog.md` 'Findings neither referee raised', 'New open items', 'Round 3 outcome (2026-10-19)' — how v3 was cut, and its closure
- `HANDOFF.md` §2, §8 — the superseded "Current best" framing and queue; §3 — the console; §6 — rounds 1 and 2
- `notes/knot-dark-matter-standalone.md` Abstract, §1, §5, §6 — the withdrawn manuscript's claims, its ordinary kinematics, exclusion conditions, requirements and acceptance criteria
- `review/skeptic-review-console.html` — #14 v2, verbatim
- `popsci/angle-of-the-mirror.md` 'Corollaries and daydreams'; `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the popular framings
- `review/wiki-build-flags.md` item 21 — the source of the lower end of ruling 3's Kibble–Zurek range; item 60 — the identification as P.R.'s conjecture, and F2's finding
