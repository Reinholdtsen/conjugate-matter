---
title: "The handoff document"
weight: 20
status: record
description: "HANDOFF.md, the transfer from claude.ai on 2026-10-19: what each of its sections records, where every item of its lists and every queue entry stands now, which parts are superseded, and the flags that concern it."
sources:
  - "HANDOFF.md §1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §4"
  - "HANDOFF.md §5"
  - "HANDOFF.md §6"
  - "HANDOFF.md §7"
  - "HANDOFF.md §8"
  - "HANDOFF.md §9"
  - "HANDOFF.md Appendix A"
  - "CLAUDE.md 'Since the handoff'"
  - "CLAUDE.md 'Layout'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md §11.4"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/broken-born-checkpoint-v2.md App. A"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "papers/phase-space-diameter.md header"
  - "papers/phase-space-diameter.md §3"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §6"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
  - "review/round5-adjudication.md 'Pre-registration scored'"
  - "review/round5-preregistration.md"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "review/wiki-build-flags.md items 7, 16, 23, 24, 26, 27, 29, 35, 36"
  - "review/wiki-build-flags.md item 55"
  - "review/wiki-build-flags.md items 59, 60, 62, 63"
  - "notes/gate-mechanism.md §5"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "notes/closed-universe.md §2"
  - "verify/battery.py"
---

*`HANDOFF.md` is the note that carried the program from the claude.ai conversation where it was developed to Claude Code and this repository. It was prepared on 2026-10-19 so that a fresh session could continue without the original chat: it gives the scientific state on one screen, numbers the artifacts #1–#15, lists the results that exist only in the chat, and records the method, the review history, the working conventions and a ranked list of next actions. Much of it still stands. Of the four claims it lists as killed by the program's own calculations, three are P.R.'s open conjectures and the fourth is under review. Its superheavy [soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary), the model of manuscript #14, and its work queue were superseded on 2026-10-19, several of its statuses have moved on, its chat-only diameter relation has since been written up in a note that withdraws one of the relation's four statements, and the root `CLAUDE.md` and [checkpoint #11](/wiki/history/documents/checkpoint) now rank above it.*

**Status:** Record, superseded in part — untagged (it marks machine-checked results with ✓ rather than [V]) — rank 5 in the wiki's precedence order, with its §2 soliton candidate and §8 queue superseded (`wiki/CLAUDE.md`; root `CLAUDE.md`, 'Since the handoff'). The file was imported on 2026-10-19 (commit 8d588f6, as `import/HANDOFF.md`; moved to the root in 008c3ee). On 2026-10-28 the [three main problems](/wiki/history/main-problems) took their subject names in it, and its file names for the calc notes were updated (c12da1b). Two notes dated 2026-10-29 give the later standing of §1's founding intuition and of §2's list of failed claims (6cbaf24). Its account of the state at the move is otherwise as written.

## What the document is

The handoff states its purpose in its first line: "Everything a fresh Claude Code session needs to continue this project. Read this first; the artifacts listed in §3 travel with it. It is self-sufficient — nothing essential lives only in the originating chat session or in claude.ai memory." It mentions a second, running record kept in claude.ai's memory store, and says that if the store is visible, "it corroborates but adds nothing critical beyond this document". The footer dates it: "Handoff prepared 2026-10-19 from the originating claude.ai session."

The document is a snapshot. It was written at the move, when #11 was at version 2.0 and the soliton manuscript #14 at version 2, and before review round 3 had finished. Everything the repository has done since is measured against it: the root `CLAUDE.md` tells a fresh session to read the handoff first, and then lists, under "Since the handoff", what has changed ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)).

## Its standing

The wiki ranks the handoff at position 5 of its precedence order, below the root `CLAUDE.md`, checkpoint #11, the toy-model note and the phase-space-diameter note, the review adjudications and #13, and above the notes and the popular articles (`wiki/CLAUDE.md`; [Documents](/wiki/history/documents#the-order-of-precedence)). Two parts are superseded by name: "its §2 soliton candidate and its §8 queue". Later documents have superseded other statements, and the sections below say which.

Of the four claims §2 lists as killed by the program's own calculations, #11 v2.4 lists conjugate collapse powering our expansion and the conjugate-monopole explanation of the null result as P.R.'s open conjectures, and v2.5 lists momentum clumping, the founding image, the same way ([below](#the-list-of-failed-claims)). The fourth, [α_d ≈ 34 against our photon](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling), is under review ([negative results and dead claims](/wiki/method/negative-results); [claims under review](/wiki/status/under-review)).

## §1: what the project is

§1 names the project, the "Broken-Born program" (BBT, Broken-Born theory, the program's earlier name), "a speculative physics research program developed September–October 2026". It states the [hard core](/wiki/program/hard-core): "Born reciprocity — the (x,p) → (p,−x) symmetry of quantum kinematics — taken as exact and spontaneously broken, with only the symplectic form ω rigid (ℏ-rigidity) and the neutral metric η emergent as the order parameter." It fixes the roles: P.R. supplies conjecture and direction and holds a veto, Claude supplies derivations, counterexamples, drafting and verification, and "Attribution in all papers follows this split" ([the collaboration](/wiki/method/collaboration)).

Its "Honest status" reads: "a Lakatosian research program, not a theory. Three blind AI reviews returned verdict B ("flawed but salvageable"). Zero fabricated citations across all checks." It reports the founding intuition, dark matter clumping in momentum space, as falsified by the program's own calculations, and goes on: "the structural core survived four consecutive consistency tests by being forced onto unique consistent structures each time." The founding intuition is P.R.'s open conjecture, with those calculations standing (#11 §9; [Conjecture: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)). The count of reviews disagrees with the handoff's own §6 (below). The "four consecutive consistency tests" is also #11 §15's count ([assessment](/wiki/program/assessment)). On "unique consistent structures", without the qualifier "known" that calc note #6 §3 keeps, see flag 7 in `review/wiki-build-flags.md`.

## §2: the scientific state on one screen

§2 sorts the program's results into three lists, alive, failed and open, and names an external clock. It is the part of the handoff that later documents have changed most.

### Alive

The heading is "Alive (derived, machine-verified where marked ✓)". Its items, and where each stands now:

- **The compatibility theorem**, "ω,η both rigid ⇒ H = diag(g,g⁻¹), det H = 1, momentum metric slaved g̃ = g⁻¹ ✓". Still alive, but no longer the program's own: #11 v2.1 tags it [T][V], crediting the statement to Freidel, Leigh and Minic, with the block proof and the machine check the program's ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)).
- **The P2′ correction**, "strict rigidity trivializes the theory (nontriviality theorem); η must be emergent" ([P2′](/wiki/program/postulates/p2-prime); [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)). #11 v2.2 adds a refinement from the toy models: the polarization is a [Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).
- **The modular field**, "Z = X + iY on Siegel domain Sp(2d,R)/U(d); Im Z = metric, Re Z = X = momentum graviton; reciprocity = Z → −1/Z; a·ã = 1 is the |Z|=1 locus; dark energy τ = Maslov phase of the Shilov boundary Λ(4) ✓ (parametrization identities)" ([the modular field Z](/wiki/phase-space/modular-field/modular-field-z); [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)). The identification of a·ã = 1 with the |Z| = 1 locus, which #11 §6 and §10 repeat, is queried in `review/wiki-build-flags.md` item 23.
- **X forced massive**, ending "Geometric sector = interchange-symmetric (palindromic βₙ = β₄₋ₙ) Hassan–Rosen bimetric, second frame confined to compact Λ(4)" ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain); [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)).
- **The [palindrome](/wiki/gravity/palindromic-branch/palindrome) and Λ theorem**, "V(1) = 2T exactly ⇒ flat aligned vacuum forces wedge-sector vacuum energy = 0 ✓ (integer identity [2,8,6] = 2·[1,4,3])", with the novelty already downgraded after a literature check, "Detailed comparison still to do" ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity); [Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison)). The comparison is first in the current queue.
- **The tuning test**: metric-tier potentials fail [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) (FP) ✓, and the frame tier "passes iff formulated in first-order variables" ([the tuning test](/wiki/gravity/tuning-test)).
- **Cosmology**: the [dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary) w_eff = −w̃ (w is a fluid's [equation of state](/wiki/cosmology/dark-energy/quintessence#dark-energy-and-the-equation-of-state), the ratio of its pressure to its energy density, which is −1 for a cosmological constant; a fluid with w̃ in the conjugate frame acts on our expansion like one with w_eff in ours), [τ as hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence), "thawing, w ≥ −1 always, eventual negative V ⇒ turnaround = conjugate bounce (one event, two descriptions). Consistent with DESI DR1/DR2 drift hints." The last sentence is superseded: Data Release 2 (DR2) of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI) favors a phantom crossing, and the sector is "under real pressure" (root `CLAUDE.md`; [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)). DR1 is Data Release 1. Whether the potential can turn negative at all is unresolved (flag 27 in `review/wiki-build-flags.md`; [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)). The flag's addendum (2026-10-27) finds that "eventual negative V ⇒ turnaround" names the wrong cause: with the potential as written a closed universe turns around with V ≥ 0, and a flat or open one never does ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#the-turnaround-needs-k--1-dv)).
- **The dark-matter sector**: "gated self-interaction (gate = X-exchange; gate variable = incoming relative momentum; μ = χ's momentum-fiber width); knee at v\*; knee-tail shape = particle-vs-wave 'island discriminant' (new observable)" ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate); [row 3](/wiki/predictions/island-discriminant)). "Gate = X-exchange" is among the text flag 55 in `review/wiki-build-flags.md` lists as depending on #11 §8's tag: `notes/gate-mechanism.md` (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging #11 §7's X cannot produce the gate, and the flag, pending, proposes [P] for the gate and μ and [O] for the mechanism; #11 §8's tag is [D — mechanism; shape [O]] ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The same note opens whether the island discriminant survives (`notes/gate-mechanism.md` §5).
- **The maximum force and dual special relativity**: "Maximum force c̃ = c⁴/G as the momentum-space light speed (matches Gibbons–Schiller maximum-force conjecture up to the factor 4)", with [force boosts](/wiki/conjugate-relativity/force-boosts), [force dilation](/wiki/conjugate-relativity/force-dilation), [the invariant length](/wiki/conjugate-relativity/invariant-length-shell) and [the equivalence principle](/wiki/conjugate-relativity/equivalence-principle) "as the dual relativity principle" ([the maximum force](/wiki/conjugate-relativity/maximum-force); [conjugate special relativity](/wiki/conjugate-relativity)). Neither item carries a ✓, and #13 has not been through review.
- **The charge lattice**: "DSZ pairing is symplectic; duality frame choice = Lagrangian polarization, same [[0,1],[−1,0]] generator as Born rotation and S-duality", DSZ being Dirac–Schwinger–Zwanziger ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). The same bullet names the "Current best DM candidate: superheavy (~10¹³–10¹⁷ GeV) topological solitons (π₂ monopole-class) of a separate, strongly coupled dual gauge sector — 'dark by sector separation,'" not magnetically charged under our photon, DM being dark matter. That candidate is #14's model, which, built with ordinary kinematics, failed on its recomputed abundance in review round 3 ([Obituary: #14's superheavy-soliton model](/wiki/dark-matter/candidates/soliton-candidate/obituary)). The candidate it modeled, conjugate monopoles localized in momentum, is P.R.'s open conjecture; #14's model did not treat localization in momentum, so the candidate itself has not been tested (#11 §12; [Conjecture: magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles)).

### The list of failed claims

The second list, headed "Dead", names four claims as killed by the program's own calculations. Each is given here as the handoff states it, with where it stands now:

- **Dark matter clumping in momentum space** "as dynamics: impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓), fatal where mandatory on the wave island (ultra-faint dwarfs would be drained; Segue 1 intact), tunable elsewhere. Rows withdrawn permanently." The founding image is P.R.'s open conjecture [O], and the calculations that tested it stand; Scenario A, the wave-island case where clumping is mandatory, and the withdrawn rows on [velocity-space granularity](/wiki/dark-matter/momentum-clumping/velocity-granularity) and [Fornax friction](/wiki/dark-matter/momentum-clumping/fornax-friction) are under review (#11 §9, §13, Appendix A item 3; [Conjecture: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image); [Under review: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)). When the handoff was written, no `verify/` script computed the 10²⁸–10³¹ that the ✓ marks, and #11 §9's tag is [D] (`review/wiki-build-flags.md` item 16; [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)). Since 2026-10-28 section D of `verify/velocity_gated_gravity.py` has reproduced both ratios, so the ✓ is now backed by a script (the flag's addendum; [the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)). The bullet adds: "Loophole: *topological* p-localization of individual solitons untouched" ([Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)); the loophole's candidate is P.R.'s conjecture of conjugate monopoles localized in momentum (#11 §12).
- **"Conjugate collapse powers our expansion"**: "first version gave w = −2 (falsified); corrected dictionary removed the mechanism (dual dust ↦ dust)". It is P.R.'s open conjecture [O]: the two versions the handoff names failed, and "the corrected dictionary's dual stiff ↦ Λ leaves a route, a conjugate universe kinetic-dominated as it contracts acting on ours as a cosmological constant" (#11 Appendix A item 9; §10). What the corrected dictionary removed is the dust version ([Conjecture: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)).
- **Conjugate monopoles as the explanation of our monopole non-detection**: "(wrong duality; inflation suffices). As ontology they're alive (the soliton candidate)." The ontology is alive. The soliton candidate the handoff tied it to was #14's model, which failed; the ontology carries P.R.'s conjecture that such monopoles are abundant in momentum space, and their candidacy as the dark matter is open (§11.1, §12; [conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)). The explanation is P.R.'s open conjecture [O] in the setting of the [shared-photon form](/wiki/electric-magnetic-duality/magnetic-identification#shared-photon) of his magnetic-mirror conjecture, in which momentum-polarized analogs carry magnetic charge of our own photon (flag 62 in `review/wiki-build-flags.md`). Two grounds weigh against it, and neither kills it. The first, wrong duality, is contested only by the shared-photon form, and that form needs [P4](/wiki/program/postulates/p4-polarized-matter), the postulate that gauge forces do not cross polarizations, restated, and conditions that hide the analogs, none of them yet computed (#11 §11.1, §11.4). On the second, the null result is expected under several standard histories, inflation after a unification transition among them, so it lends the explanation no support, and inflation is the standard account, not an observed epoch (#11 §11.1; flag 59; [Conjecture: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation)).
- **α_d ≈ 34 via [Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) against our photon**: "round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon", with the v2 restatement, "reciprocity-acts-as-modular-S on the coupling — explicitly the load-bearing conjecture" ([Under review: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)). The claim is under review. Round 1 found an inconsistency in it: Dirac's condition taken against our photon while coupling to it was denied (flag 60). v2's load-bearing conjecture, the momentum-polarized sector as the S-dual image of the electric sector, is what #11 §11.4 records as #14 v2's "related identification" beside P.R.'s magnetic-mirror conjecture [O], and v2's form, magnetic under the sector's own gauge field, is the conjecture's separate-photon form ([Conjecture: the momentum sector as the magnetic mirror](/wiki/electric-magnetic-duality/magnetic-identification)).

The first three are listed with [the conjectures](/wiki/status/conjectures), and the fourth in [claims under review](/wiki/status/under-review).

### Open

"Open (the real frontier)" lists items 1–8. Their fates:

| Handoff item | What became of it |
| --- | --- |
| 1. Toy Lagrangian, "η the order parameter also selecting the electric sublattice (acceptance criterion #1; both reviewers independently named it)" | met in the referees' wording by version 2 of the toy-model note (#11 §14 item 11); the electric-sublattice clause is not addressed, and #11 §11.4 lists it first among what the magnetic-mirror conjecture needs, "never attempted" ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion); [the clause](/wiki/electric-magnetic-duality/unified-modular-structure#open-the-electric-sublattice-clause)) |
| 2. Strong-coupling relic freeze-out at α_d ~ 34 against "the √N topological-charge floor" | dropped after #14's model failed (round-3 Decision 3; [Under review: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)) |
| 3. "UV stability of sector separation / kinetic mixing" | answered in the record's terms by strict P4 (Decision 1; [P4](/wiki/program/postulates/p4-polarized-matter)); #11 §14 lists no kinetic-mixing item |
| 4. "PM-point comparison and the Λ=0 novelty audit", PM being [partially massless](/wiki/gravity/spin-2-fields/partially-massless-gravity) | #11 §14 item 2, first in the current queue ([Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison)) |
| 5. Wedge reduction from S_H; Lorentzian dressing | #11 §14 items 1 and 3 ([the wedge reduction](/wiki/gravity/tuning-test/wedge-reduction); [Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing)) |
| 6. Gate shape; dual-stress enhancement | #11 §14 items 4 and 5 ([the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape); [the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement)) |
| 7. Polarization-genesis, "the Ω_DM:Ω_b = 5.4:1 ratio" | #11 §14 item 7 ([polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis)) |
| 8. "Dark-sector trilemma discrimination: particles vs X-condensate vs solitons" | two-way in #11 v2.1 to v2.3, and three-way from v2.4, "Discriminating the three dark-sector candidates (§12) [O]" (§14 item 9), the third being P.R.'s conjecture of conjugate monopoles localized in momentum ([Conjecture: magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles)); prediction [row 11](/wiki/predictions/dark-sector-microstructure) names two of them, "Particles vs condensate", and flag 63 in `review/wiki-build-flags.md`, pending, proposes new wording |

UV stands for ultraviolet, that is, high-energy physics.

### The external clock

"DESI DR3 (three-year data, expected late 2026). Kill conditions: robust constant w = −1 kills the τ sector; robust intrinsic w < −1 kills the framework outright; continued thawing drift keeps it alive (shared with other dynamical-DE models)", DE being dark energy and DR3 Data Release 3. The kill conditions follow #11's row 4, which writes "kills τ-sector" and "kills outright" ([row 4](/wiki/predictions/dark-energy-drift)); "the framework" is the handoff's reading of the second. The label "three-year data" is queried in `review/wiki-build-flags.md` item 26, since DR2 already covers three years of operations; the wiki quotes it as written. The date is the handoff's own and is unverified ([the data releases](/wiki/cosmology/dark-energy/desi#the-data-releases)).

## §3: the artifact inventory

§3, "Artifact inventory (creation order)", lists the artifacts #1–#15 with file, status and a description. Its numbers #1–#15 are the ones the wiki and the root `CLAUDE.md` use; the folders and current standing of each are on [Documents](/wiki/history/documents). Some statuses have changed since:

- #11, "**v2.0 — CURRENT REFERENCE for the full program**", is now v2.5 ([the checkpoint](/wiki/history/documents/checkpoint)).
- #14, "**v2 — CURRENT blind-review manuscript**", with "Round-2 findings" not yet incorporated "(pending v3 — list in §6)", went to v3 and was withdrawn after round 3 ([#14's soliton model (failed)](/wiki/dark-matter/candidates/soliton-candidate)).
- #5's description, "gate mechanism = X-exchange (finds the gate's mechanism)", is among the text that flag 55 lists as depending on #11 §8's tag; the flag, pending, proposes that the mechanism is not derived ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate); [the field-equation calc notes](/wiki/history/documents/field-equation-notes)).
- #15, the skeptic console, "tool, current", was used for rounds 1–2 only; rounds 3 to 5 used blind subagents with code execution ([the skeptic review console](/wiki/method/review/skeptic-console)).

§3 also records that P.R. holds two referee-report text files, the round 1 and round 2 outputs of #15, whose content §6 summarizes "which is sufficient if those files are absent". The repository holds no copy of them. Its recommended read order, "#11 → #14 → §6 of this handoff → calc notes (#2–#8) only as needed per task", was replaced by the root `CLAUDE.md`'s, which drops #14 and adds the round-3 adjudication.

## §4: results that exist only in the chat

The section heading, with its capitals set in lower case here, is "Results that exist only in the chat (not in any artifact)". These are the program's chat-only results, kept at conjecture tier except where a later document changed their standing: the first has since been written up in a note, and the second was dropped after #14's model failed ([chat-only and popsci-only conjectures](/wiki/status/conjectures)):

- **The phase-space diameter relation**, "D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem)", with the rectangle "square … exactly at the bounce" and "Conjecture-tier; candidate for a future note". The note was written on 2026-10-26: `papers/phase-space-diameter.md` v1.1, round-5 verdict B, and v1.2 since 2026-10-29 ([the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter); [Round 5](/wiki/method/review/round-5)). For blackbody radiation in a sphere the product is an identity, D_x·D_p = κ h N_γ^{1/3} with κ = 1.708 [D][V], constant for a fixed comoving region [T]; the bullet's "~10⁹⁰" is the radiation's entropy, 1.01×10⁹⁰ k_B, beside a photon count of 1.43×10⁸⁹ [V]; and the relation holds in standard cosmology, so it cannot test the program. "Square exactly at the bounce" is withdrawn: in Planck units the radiation's rectangle is square only at about 10¹⁴ T_P, before the radiation existed, and most elongated at a turnaround. The claim is under review, and the withdrawal's results stand ([Under review: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)). What stands of the bullet is the area relation, as standard physics, and the aspect ratio as a clock of e-folds and a distance on the Siegel half-plane. Which bounce is meant is queried in `review/wiki-build-flags.md` item 24. The note traces the claim's likeliest origin, by its own tag an inference, to #11's identification of a·ã = 1 with |Z| = 1, the subject of item 23; the round-5 adjudication recommends accepting both flags, which are pending.
- **The √N topological floor**, whose queued calculation was dropped after #14's model failed; the argument is under review ([Under review: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)).
- **Two gravitational charges** and the **comparison of the conjugate field equations with [general relativity](/wiki/gravity/spin-2-fields/general-relativity) (GR)**, including "dual Newtonian limit = Yukawa in momentum = the gate" ([two gravitational charges and the conjugate field equations](/wiki/gravity/momentum-graviton/chat-only-results); [a range in momentum](/wiki/gravity/spin-2-fields/yukawa-forces#conjugate-special-relativity-a-range-in-momentum)). The reading of X's range "in momentum" also appears in #13, which cites #11 §7 for it; #11 §7 does not make it (`review/wiki-build-flags.md` item 29).
- **Momentum-space black holes**, "Conjecture tier; partially in #12" ([momentum-space black holes](/wiki/conjugate-relativity/momentum-space-black-holes)).
- **"Full adjudications of review rounds 1–2 with executed arbitration code (summarized in §6)"**. Only the summary survives ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

## §5: the verification protocol

§5, "the method — keep using it", sets out the tags [D], [T], [P], [O] and [V] with the citation marks † and [S] ([provenance tags](/wiki/method/provenance-tags)); the iron rule, "no arithmetic by eyeball. Any disputed or asserted number gets executed code with printed output. This is load-bearing — see §6" ([the iron rule](/wiki/method/verification/iron-rule)); pre-registration of the expected verdict and weakest link, "(scored 2-for-2 on verdicts)" ([pre-registration](/wiki/method/review/pre-registration)); and the seven-test battery, "(all passed ✓)", with its expected outputs, among them "66.58 vs 63.72 at seed 0" for T4 and "lstsq rms ≈ 3.29" for T7 ([the verification battery](/wiki/method/verification/battery)).

Two later documents cite other sections for these records: the round-3 pre-registration cites §6 for the 2-for-2 record (flag 35 in `review/wiki-build-flags.md`), and the docstring of `verify/battery.py` and #11 §7.2 place the T4 figures in #11 §2, which does not print them (flag 36).

The root `CLAUDE.md` carries the section forward under the heading "Method (HANDOFF §5)" and has added the lessons of rounds 3, 4 and 5. The pre-registration record did not stay at 2-for-2: round 3 scored "**Miss**: the first after 2 for 2" on the verdict, and rounds 4 and 5 a "**Hit**" (`review/round3-adjudication.md`, `review/round4-adjudication.md`, `review/round5-adjudication.md`, 'Pre-registration scored').

## §6: review history and the measured failure mode

§6 is the only surviving account of the first two blind reviews of #14. Round 1, "(fresh Sonnet, web search, blind)", returned "**B / medium**"; round 2, on v2, "**B near B/C / medium**", with the weakest link "the α_d derivation". Each round's valid findings and the referee's own arithmetic errors are listed, the round-2 findings as pending for v3 ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

From both rounds it draws the "Measured failure mode": "fresh LLM referees are strong on structure, literature and logic; **unreliable on unaided arithmetic** (3 confident order-of-magnitude indictments, all reviewer unit errors, 0 surviving). Hence the iron rule." LLM stands for large language model. It adds that Claude Code's execution tools remove this failure mode, "that's the main reason the project is moving to you". Round 3 moved the failure mode to the author's side: "the author's verification checks the author's model" (`review/round3-adjudication.md`; [the measured referee failure mode](/wiki/method/review/referee-failure-mode)).

Round 3 is recorded as "(incomplete)": an execution-verified audit dispatched on 2026-10-17 "died partway on a rate limit". The handoff's "Suggested first task in Claude Code" was to re-run it, and its footer asks that the partial finding be treated "as unconfirmed until re-run". Both were done on 2026-10-19, and round 3 returned verdict C on #14 v3 ([review round 3](/wiki/method/review/round-3)).

## §7: working conventions

§7 records P.R.'s background as an independent developer with a research past at the Stanford Ginzton Lab in scanning acoustic microscopy, Fourier-domain physics, the origin of his intuition; the calibration he relies on, since he cannot independently verify most of the technical physics ("keep the tier tags, keep machine-verifying, keep pre-registering, keep reporting negative results prominently"); the chunked work pattern; the prose register for science writing; the house pattern for papers; the attribution line; and the format of working communication. The root `CLAUDE.md` 'Working with Paul' carries all of it forward ([the collaboration](/wiki/method/collaboration)). The wiki's own voice rules come from the same register.

## §8: the ranked queue

| Handoff item (§8) | What became of it |
| --- | --- |
| 1. "Cut v3 of `knot-dark-matter-standalone.md`" with the §6 pending list | done 2026-10-19 (commit 5dbaa82) |
| 2. "Re-run the execution-verified blind audit on v3" | done 2026-10-19: round 3, verdict C, and #14 withdrawn |
| 3. "√N-floor freeze-out estimate" | dropped by round-3 Decision 3 |
| 4. "Toy Lagrangian (acceptance criterion #1)", "Hardest; highest value. Start in 0+1 or 1+1 dimensions on the Siegel disk." | done to the referees' wording on 2026-10-20 ([toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models)) |
| 5. "PM-point comparison" (partially massless) | first in the current queue |
| 6. "Literature battery completion: every † reference in #11 and #13 source-checked; resolve the gravity-induced kinetic mixing question" | second in the current queue; Born's two papers were retrieved for the diameter note ([Open: the † literature battery](/wiki/method/literature-battery)) |
| 7. "Optional write-ups: phase-space diameter relation note (§4); LaTeX/arXiv shaping only after 1–5" | the diameter note done on 2026-10-26, version 1.1 after round 5, version 1.2 since 2026-10-29 ([Round 5](/wiki/method/review/round-5)); the current queue names only items 5–6, so the shaping for arXiv is not in it |

The root `CLAUDE.md` records the decisions: "HANDOFF §8 queue item 3 is dropped. The current queue, in order: 1. HANDOFF §8 items 5–6: the partially-massless comparison and the † literature battery (Born 1938 and 1949 were retrieved for the diameter note; see its §4). 2. Optional: a round-6 review of the toy note, but only before any external use." It also records that "The phase-space-diameter note (HANDOFF §8 item 7) is done". "Reasons for the queue are in the round-3 adjudication's 'Decisions' section" ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions); [open problems and the queue](/wiki/status/open-problems)).

## §9 and Appendix A

§9, "Repo suggestion (optional)", proposed folders for papers, popular articles, notes, review material and verification scripts, with `HANDOFF.md` at the root and `CLAUDE.md` pointing at it. The repository follows it, with #9 placed in `notes/` and #14 moved there after its withdrawal ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)).

Appendix A, "machine-verification battery (re-run first)", is the Python code of tests T1–T7 with the expected results: "T1–T3 all True; T4 converges to 4Tr(h²) and visibly ≠ FP; T5 = [0,0,0]; T6 = [0,1,3,3,1]; T7 rms ≈ 3.3." `verify/battery.py` is that code turned into assertions, with the same computations, seeds and random-number order, and it is the first script the gate runs ([the verification battery](/wiki/method/verification/battery); [the gate](/wiki/method/verification/the-gate)). The handoff's Appendix A is distinct from #11's Appendix A, which is the [audit of founding suppositions](/wiki/program/founding-suppositions).

## What is superseded or unresolved

Superseded by later documents:

- **The soliton candidate** (§2), which is #14's model, and **the queue** (§8), by name (`wiki/CLAUDE.md`; root `CLAUDE.md`, 'Since the handoff'; #11 §12).
- **The reading of DESI** (§2), by DR2's phantom crossing (#11 §10, "Under pressure (v2.1)").
- **The statuses of #11, #14 and #15** (§3), **round 3 as incomplete** (§6), **the 2-for-2 pre-registration record** (§5) and **the read order** (§3), as above.
- **The tag of the compatibility theorem**: the handoff lists it as derived and machine-verified; #11 has tagged the statement [T] since v2.1.
- **The diameter relation's standing** (§4), by the phase-space-diameter note of 2026-10-26: no longer a conjecture but standard physics, with its "square exactly at the bounce" withdrawn, the claim under review ([Under review: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)).
- **The grounds against the monopole explanation** (§2), "(wrong duality; inflation suffices)", by #11 §11.1 (flag 59), and its status (flag 62): open, P.R.'s conjecture.
- **The status of collapse-powered expansion** (§2), by #11 §10 and Appendix A item 9: open, P.R.'s conjecture, with the two versions the handoff names failed.
- **The status of momentum clumping as dynamics** (§2), by #11 §9 and Appendix A item 3: open, P.R.'s conjecture, with the calculations that tested it standing.
- **The status of α_d ≈ 34 against our photon** (§2): under review (root `CLAUDE.md`, 'Since the handoff').

Unresolved inside the document: §1's "Three blind AI reviews returned verdict B" against §6's two completed rounds, B and "B near B/C", and an incomplete third. No document reconciles the count ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two#unresolved-how-many-reviews-returned-b); [conflicts between sources](/wiki/history/documents/source-conflicts#method-and-records)).

Flagged in `review/wiki-build-flags.md`, quoted here as written: item 7, "unique consistent structures" without "known"; item 16, the ✓ on "fails by 10²⁸–10³¹" without a script, now backed by `verify/velocity_gated_gravity.py` (addendum of 2026-10-28); item 55, "gate = X-exchange" in §2 and #5's "finds the gate's mechanism" in §3, which the gate-mechanism note finds not derived; item 23, a·ã = 1 as the |Z| = 1 locus; item 24, which bounce the diameter relation means, on which the diameter note's §6 tests every reading it records; item 26, "three-year data"; item 27, the negative V that the turnaround needs, against the potential V₀[1 + cos(τ/f)] of #11 §10, whose minimum is 0 for V₀ > 0, with its addendum of 2026-10-27 on the closed turnaround; item 29, the reading of X's range in momentum, documented only in the chat; item 59, that §2's "inflation suffices", a ground against the monopole explanation, shows the explanation unnecessary, not false (applied to #11, not to the handoff); item 62, the explanation in the setting of the shared-photon form.

## Sources

- `HANDOFF.md` §1–§9 and Appendix A — the document itself; its first line, purpose and footer; the notes in §1 and §2 dated 2026-10-29; its earlier wording is in its history (`git log -- HANDOFF.md`: 8d588f6, 008c3ee, c12da1b, 6cbaf24)
- `CLAUDE.md` — the instruction to read the handoff first; 'Since the handoff' — which parts are dropped or replaced, #14's model, P.R.'s open conjectures and the claims under review, the diameter note done, and the current queue; 'Layout' — the replacement read order; 'Method (HANDOFF §5)' — the method carried forward
- `papers/phase-space-diameter.md` header — version 1.1 and its round-5 verdict, and version 1.2 of 2026-10-29; §3 — the identity, κ, the radiation's entropy and photon count; §5 — the clock and the Siegel distance; §6 — the withdrawal and the claim's likeliest origin, tagged "[D, inference]"
- `review/round5-adjudication.md` 'Recommendations to Paul' — accepting flags 23 and 24 recommended
- `wiki/CLAUDE.md` 'The wiki is derivative' — the handoff's rank and its superseded parts
- `papers/broken-born-checkpoint-v2.md` §5 — the re-tagged compatibility theorem; §10 — "Under pressure (v2.1)", and founding supposition 9 as P.R.'s conjecture; §11.1 — the grounds against the monopole explanation, and the explanation as P.R.'s open conjecture; §11.4 — P.R.'s magnetic-mirror conjecture [O] in its separate-photon and shared-photon forms, #14 v2's related identification, which v2 called load-bearing for its dual coupling, and the electric-sublattice clause as the conjecture's first open item; §12 — the three candidates and the failure of #14's model; §14 — the open items the handoff's list became; Appendix A item 9 — the route through dual stiff ↦ Λ, and its two failed versions; §9, §13 and Appendix A item 3 — momentum clumping as P.R.'s open conjecture, with Scenario A and the withdrawn rows under review
- `review/round3-adjudication.md` 'Pre-registration scored' and 'Decisions' — round 3's completion, the moved failure mode and the queue decisions; `review/round4-adjudication.md` 'Pre-registration scored' — the round-4 hit; `review/round5-adjudication.md` 'Pre-registration scored' — the round-5 hit; `review/round5-preregistration.md` — round 5's referees
- `review/wiki-build-flags.md` items 7, 16, 23, 24, 26, 27, 29, 55 and 59 — the flags that concern statements in the handoff, items 16 and 27 with their addenda; item 60 — the α_d kill as an inconsistency that the magnetic-mirror conjecture does not repeat; item 62 — the explanation in the setting of the conjecture's shared-photon form; item 63 — row 11 naming two of the three candidates, pending; items 35 and 36 — two later documents' pointers to sections that do not hold the records the handoff's §5 holds
- `notes/closed-universe.md` §2 — the turnaround in a closed universe with V ≥ 0
- `verify/battery.py` — Appendix A as assertions
- `notes/gate-mechanism.md` §5 — the text that depends on #11 §8's tag, including §2's "gate = X-exchange" and §3's "finds the gate's mechanism"
- `verify/velocity_gated_gravity.py` section D — the script now behind the ✓ on the clumping shortfall
