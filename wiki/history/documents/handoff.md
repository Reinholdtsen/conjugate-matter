---
title: "The handoff document"
weight: 20
status: record
description: "HANDOFF.md, the transfer from claude.ai on 2026-10-19: what each of its sections records, what became of every alive, dead and open item and every queue entry, which parts are superseded, and the flags that concern it."
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
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "papers/phase-space-diameter.md header"
  - "papers/phase-space-diameter.md §3"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §6"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
  - "review/wiki-build-flags.md items 7, 16, 23, 24, 26, 27, 29, 35, 36"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §5"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "notes/closed-universe.md §2"
  - "verify/battery.py"
---

*`HANDOFF.md` is the note that carried the program from the claude.ai conversation where it was developed to Claude Code and this repository. It was prepared on 2026-10-19 so that a fresh session could continue without the original chat: it gives the scientific state on one screen, numbers the artifacts #1–#15, lists the results that exist only in the chat, and records the method, the review history, the working conventions and a ranked list of next actions. Much of it still stands, including its list of dead claims, which stays binding. Its [soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) and its work queue were superseded on 2026-10-19, the queue that replaced it was revised again on 2026-10-19, 2026-10-20 and 2026-10-26, several of its statuses have moved on, its chat-only diameter relation has since been written up in a note that withdraws one of the relation's four statements, and the root `CLAUDE.md` and [checkpoint #11](/wiki/history/documents/checkpoint) now rank above it.*

**Status:** Record, superseded in part — untagged (it marks machine-checked results with ✓ rather than [V]) — rank 5 in the wiki's precedence order, with its §2 soliton candidate and §8 queue superseded (`wiki/CLAUDE.md`; root `CLAUDE.md`, 'Since the handoff'). The file is unchanged since its import on 2026-10-19 (commit 8d588f6, as `import/HANDOFF.md`; moved to the root in 008c3ee).

## What the document is

The handoff states its purpose in its first line: "Everything a fresh Claude Code session needs to continue this project. Read this first; the artifacts listed in §3 travel with it. It is self-sufficient — nothing essential lives only in the originating chat session or in claude.ai memory." It mentions a second, running record kept in claude.ai's memory store, and says that if the store is visible, "it corroborates but adds nothing critical beyond this document". The footer dates it: "Handoff prepared 2026-10-19 from the originating claude.ai session."

The document is a snapshot. It was written at the move, when #11 was at version 2.0 and the soliton manuscript #14 at version 2, and before review round 3 had finished. Everything the repository has done since is measured against it: the root `CLAUDE.md` tells a fresh session to read the handoff first and then lists, under "Since the handoff", what has changed ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)).

## Its standing

The wiki ranks the handoff at position 5 of its precedence order, below the root `CLAUDE.md`, checkpoint #11, the toy-model note and the phase-space-diameter note, the review adjudications and #13, and above the notes and the popular articles (`wiki/CLAUDE.md`; [Documents](/wiki/history/documents#the-order-of-precedence)). Two parts are superseded by name: "its §2 soliton candidate and its §8 queue". Other statements have been overtaken by events, and the sections below say which.

One part outranks its position. The handoff's list of dead claims stays binding whatever happens later: "Claims listed as dead in HANDOFF §2 stay dead" (root `CLAUDE.md`, 'Method'), and the wiki's rule "Dead stays dead" names "`HANDOFF.md` §2" first among the places where claims were killed (`wiki/CLAUDE.md`).

## §1: what the project is

§1 names the project, the "Broken-Born program" (BBT, Broken-Born theory), "a speculative physics research program developed September–October 2026". It states the [hard core](/wiki/program/hard-core): "Born reciprocity — the (x,p) → (p,−x) symmetry of quantum kinematics — taken as exact and spontaneously broken, with only the symplectic form ω rigid (ℏ-rigidity) and the neutral metric η emergent as the order parameter." It fixes the roles: "Paul (P.R.) — conjecture, direction, veto; Claude — derivations, counterexamples, drafting, verification. Attribution in all papers follows this split" ([the collaboration](/wiki/method/collaboration)).

Its "Honest status" reads: "a Lakatosian research program, not a theory. Three blind AI reviews returned verdict B ("flawed but salvageable"). Zero fabricated citations across all checks. The founding intuition (dark matter clumping in momentum space) was falsified by the program's own calculations; the structural core survived four consecutive consistency tests by being forced onto unique consistent structures each time." The count of reviews disagrees with the handoff's own §6 (below). The "four consecutive consistency tests" is also #11 §15's count ([assessment](/wiki/program/assessment)). On "unique consistent structures", without the qualifier "known" that calc note #6 §3 keeps, see flag 7 in `review/wiki-build-flags.md`.

## §2: the scientific state on one screen

§2 sorts the program's results into alive, dead and open, and names an external clock. It is the part of the handoff the later record has changed most.

### Alive

The heading is "Alive (derived, machine-verified where marked ✓)". Its items, and where each stands now:

- **The compatibility theorem**, "ω,η both rigid ⇒ H = diag(g,g⁻¹), det H = 1, momentum metric slaved g̃ = g⁻¹ ✓". Still alive, but no longer the program's own: #11 v2.1 tags it [T][V], crediting the statement to Freidel, Leigh and Minic, with the block proof and the machine check the program's ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)).
- **The P2′ correction**, "strict rigidity trivializes the theory (nontriviality theorem); η must be emergent" ([P2′](/wiki/program/postulates/p2-prime); [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)). #11 v2.2 adds a refinement from the toy models: the polarization is a [Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).
- **The modular field**, "Z = X + iY on Siegel domain Sp(2d,R)/U(d); Im Z = metric, Re Z = X = momentum graviton; reciprocity = Z → −1/Z; a·ã = 1 is the |Z|=1 locus; dark energy τ = Maslov phase of the Shilov boundary Λ(4) ✓ (parametrization identities)" ([the modular field Z](/wiki/phase-space/modular-field/modular-field-z); [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase)). The identification of a·ã = 1 with the |Z| = 1 locus, which #11 §6 and §10 repeat, is queried in `review/wiki-build-flags.md` item 23.
- **X forced massive**, ending "Geometric sector = interchange-symmetric (palindromic βₙ = β₄₋ₙ) Hassan–Rosen bimetric, second frame confined to compact Λ(4)" ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain); [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)).
- **The [palindrome](/wiki/gravity/palindromic-branch/palindrome) and Λ theorem**, "V(1) = 2T exactly ⇒ flat aligned vacuum forces wedge-sector vacuum energy = 0 ✓ (integer identity [2,8,6] = 2·[1,4,3])", with the novelty already downgraded after a literature check, "Detailed comparison still to do" ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity); [Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison)). The comparison is first in the current queue.
- **The tuning test**: metric-tier potentials fail [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) (FP) ✓, and the frame tier "passes iff formulated in first-order variables" ([the tuning test](/wiki/gravity/tuning-test)).
- **Cosmology**: the dictionary w_eff = −w̃, [τ as hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence), "thawing, w ≥ −1 always, eventual negative V ⇒ turnaround = conjugate bounce (one event, two descriptions). Consistent with DESI DR1/DR2 drift hints." The last sentence is superseded: Data Release 2 (DR2) of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI) favors a phantom crossing, and the sector is "under real pressure" (root `CLAUDE.md`; [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)). DR1 is Data Release 1. Whether the potential can turn negative at all is unresolved (flag 27 in `review/wiki-build-flags.md`; [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)). The flag's addendum (2026-10-27) finds that "eventual negative V ⇒ turnaround" names the wrong cause: with the potential as written a closed universe turns around with V ≥ 0, and a flat or open one never does ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#the-turnaround-needs-k--1-dv)).
- **The dark-matter sector**: "gated self-interaction (gate = X-exchange; gate variable = incoming relative momentum; μ = χ's momentum-fiber width); knee at v\*; knee-tail shape = particle-vs-wave 'island discriminant' (new observable)" ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate); [row 3](/wiki/predictions/island-discriminant)). "Gate = X-exchange" is among the text flag 55 in `review/wiki-build-flags.md` lists as depending on #11 §8's tag: `notes/gate-mechanism.md` (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging #11 §7's X cannot produce the gate, and the flag proposes [P] for the gate and μ and [O] for the mechanism, pending Paul's ruling; #11 is unchanged ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The same note opens whether the island discriminant survives (`notes/gate-mechanism.md` §5).
- **The maximum force and dual special relativity**: "Maximum force c̃ = c⁴/G as the momentum-space light speed (matches Gibbons–Schiller maximum-force conjecture up to the factor 4)", with [force boosts](/wiki/conjugate-relativity/force-boosts), [force dilation](/wiki/conjugate-relativity/force-dilation), [the invariant length](/wiki/conjugate-relativity/invariant-length-shell) and [the equivalence principle](/wiki/conjugate-relativity/equivalence-principle) "as the dual relativity principle" ([the maximum force](/wiki/conjugate-relativity/maximum-force); [conjugate special relativity](/wiki/conjugate-relativity)). Neither item carries a ✓, and #13 has not been through review.
- **The charge lattice**: "DSZ pairing is symplectic; duality frame choice = Lagrangian polarization, same [[0,1],[−1,0]] generator as Born rotation and S-duality", DSZ being Dirac–Schwinger–Zwanziger ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). The same bullet names the "Current best DM candidate: superheavy (~10¹³–10¹⁷ GeV) topological solitons (π₂ monopole-class) of a separate, strongly coupled dual gauge sector — 'dark by sector separation,'" not magnetically charged under our photon, DM being dark matter. That candidate is dead ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

### Dead

"Dead (killed by own calculations — keep dead)":

- **Dark matter clumping in momentum space** "as dynamics: impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓), fatal where mandatory on the wave island (ultra-faint dwarfs would be drained; Segue 1 intact), tunable elsewhere. Rows withdrawn permanently." See [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image). When the handoff was written, no `verify/` script computed the 10²⁸–10³¹ that the ✓ marks, and #11 §9 tags it [D] (`review/wiki-build-flags.md` item 16; [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)). Since 2026-10-28 section D of `verify/velocity_gated_gravity.py` reproduces both ratios; the flag's addendum reads "The ✓ is now backed by a script; #11 §9's tag [D] is unchanged until Paul rules" ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)). The bullet adds: "Loophole: *topological* p-localization of individual solitons untouched" ([Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).
- **"Conjugate collapse powers our expansion"**: "first version gave w = −2 (falsified); corrected dictionary removed the mechanism (dual dust ↦ dust)" ([Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)).
- **Conjugate monopoles as the explanation of our monopole non-detection**: "(wrong duality; inflation suffices). As ontology they're alive (the soliton candidate)." See [Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation). The ontology is still alive, but no longer through the soliton candidate ([conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)).
- **α_d ≈ 34 via [Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) against our photon**: "round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon", with the v2 restatement, "reciprocity-acts-as-modular-S on the coupling — explicitly the load-bearing conjecture" ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).

All of them stay dead, and each is indexed in [the graveyard](/wiki/status/graveyard).

### Open

"Open (the real frontier)" lists items 1–8. Their fates:

| Handoff item | What became of it |
| --- | --- |
| 1. Toy Lagrangian, "η the order parameter also selecting the electric sublattice (acceptance criterion #1; both reviewers independently named it)" | met in the referees' wording by the toy-model note v2 (#11 §14 item 11); the electric-sublattice clause is not addressed ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion); [the clause](/wiki/electric-magnetic-duality/unified-modular-structure#open-the-electric-sublattice-clause)) |
| 2. Strong-coupling relic freeze-out at α_d ~ 34 against "the √N topological-charge floor" | dropped with the soliton candidate (round-3 Decision 3; [Obituary: the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)) |
| 3. "UV stability of sector separation / kinetic mixing" | answered in the record's terms by strict P4 (Decision 1; [P4](/wiki/program/postulates/p4-polarized-matter)); #11 §14 lists no kinetic-mixing item |
| 4. "PM-point comparison and the Λ=0 novelty audit", PM being [partially massless](/wiki/gravity/spin-2-fields/partially-massless-gravity) | #11 §14 item 2, first in the current queue ([Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison)) |
| 5. Wedge reduction from S_H; Lorentzian dressing | #11 §14 items 1 and 3 ([the wedge reduction](/wiki/gravity/tuning-test/wedge-reduction); [Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing)) |
| 6. Gate shape; dual-stress enhancement | #11 §14 items 4 and 5 ([the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape); [the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement)) |
| 7. Polarization-genesis, "the Ω_DM:Ω_b = 5.4:1 ratio" | #11 §14 item 7 ([polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis)) |
| 8. "Dark-sector trilemma discrimination: particles vs X-condensate vs solitons" | now a two-way question, #11 §14 item 9 ([row 11](/wiki/predictions/dark-sector-microstructure)) |

UV stands for ultraviolet, that is, high-energy physics.

### The external clock

"DESI DR3 (three-year data, expected late 2026). Kill conditions: robust constant w = −1 kills the τ sector; robust intrinsic w < −1 kills the framework outright; continued thawing drift keeps it alive (shared with other dynamical-DE models)", DE being dark energy and DR3 Data Release 3. The kill conditions match #11's row 4 ([row 4](/wiki/predictions/dark-energy-drift)). The label "three-year data" is queried in `review/wiki-build-flags.md` item 26, since DR2 already covers three years of operations; the wiki quotes it as written.

## §3: the artifact inventory

§3, "Artifact inventory (creation order)", lists the artifacts #1–#15 with file, status and a description. Its numbers #1–#15 are the ones the wiki and the root `CLAUDE.md` use; the folders and current standing of each are on [Documents](/wiki/history/documents). Some statuses have changed since:

- #11, "**v2.0 — CURRENT REFERENCE for the full program**", is now v2.2 ([the checkpoint](/wiki/history/documents/checkpoint)).
- #14, "**v2 — CURRENT blind-review manuscript**", with "Round-2 findings" not yet incorporated "(pending v3 — list in §6)", went to v3 and was withdrawn after round 3 ([the soliton candidate (retired)](/wiki/dark-matter/candidates/soliton-candidate)).
- #5's description, "gate mechanism = X-exchange (finds the gate's mechanism)", is among the text that flag 55 lists as depending on #11 §8's tag; the flag proposes that the mechanism is not derived, pending Paul's ruling ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate); [the field-equation calc notes](/wiki/history/documents/field-equation-notes)).
- #15, the skeptic console, "tool, current", was used for rounds 1–2 only; rounds 3 and 4 used blind subagents with code execution ([the skeptic review console](/wiki/method/review/skeptic-console)).

§3 also records that "Paul also holds two referee-report text files (round 1 and round 2 outputs of #15)", whose content §6 summarizes "which is sufficient if those files are absent". The repository holds no copy of them. Its recommended read order, "#11 → #14 → §6 of this handoff → calc notes (#2–#8) only as needed per task", was replaced by the root `CLAUDE.md`'s, which drops #14 and adds the round-3 adjudication.

## §4: results that exist only in the chat

The section heading, with its capitals set in lower case here, is "Results that exist only in the chat (not in any artifact)". These are the program's chat-only results, kept at conjecture tier except where a later document changed their standing: the first has since been written up in a note, and the second was dropped with the soliton candidate ([chat-only and popsci-only conjectures](/wiki/status/conjectures)):

- **The phase-space diameter relation**, "D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem)", with the rectangle "square … exactly at the bounce" and "Conjecture-tier; candidate for a future note". The note was written on 2026-10-26: `papers/phase-space-diameter.md` v1.1, round-5 verdict B ([the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter); [Round 5](/wiki/method/review/round-5)). For blackbody radiation in a sphere the product is an identity, D_x·D_p = κ h N_γ^{1/3} with κ = 1.708 [D][V], constant for a fixed comoving region [T]; the bullet's "~10⁹⁰" is the radiation's entropy, 1.01×10⁹⁰ k_B, beside a photon count of 1.43×10⁸⁹ [V]; and the relation holds in standard cosmology, so it cannot test the program. "Square exactly at the bounce" is withdrawn: in Planck units the radiation's rectangle is square only at about 10¹⁴ T_P, before the radiation existed, and most elongated at a turnaround ([Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)). What survives of the bullet is the area relation, as standard physics, and the aspect ratio as a clock of e-folds and a distance on the Siegel half-plane. Which bounce is meant is queried in `review/wiki-build-flags.md` item 24. The note traces the claim's likeliest origin, by its own tag an inference, to #11's identification of a·ã = 1 with |Z| = 1, the subject of item 23; the round-5 adjudication recommends accepting both flags, which await Paul's ruling.
- **The √N topological floor**, dropped with the soliton candidate ([obituary](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)).
- **Two gravitational charges** and the **comparison of the conjugate field equations with [general relativity](/wiki/gravity/spin-2-fields/general-relativity) (GR)**, including "dual Newtonian limit = Yukawa in momentum = the gate" ([two gravitational charges and the conjugate field equations](/wiki/gravity/momentum-graviton/chat-only-results); [a range in momentum](/wiki/gravity/spin-2-fields/yukawa-forces#conjugate-special-relativity-a-range-in-momentum)). The reading of X's range "in momentum" also appears in #13, which cites #11 §7 for it; #11 §7 does not make it (`review/wiki-build-flags.md` item 29).
- **Momentum-space black holes**, "Conjecture tier; partially in #12" ([momentum-space black holes](/wiki/conjugate-relativity/momentum-space-black-holes)).
- **"Full adjudications of review rounds 1–2 with executed arbitration code (summarized in §6)"**. Only the summary survives ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

## §5: the verification protocol

§5, "the method — keep using it", sets out the tags [D], [T], [P], [O] and [V] with the citation marks † and [S] ([provenance tags](/wiki/method/provenance-tags)); the iron rule, "no arithmetic by eyeball. Any disputed or asserted number gets executed code with printed output. This is load-bearing — see §6" ([the iron rule](/wiki/method/verification/iron-rule)); pre-registration of the expected verdict and weakest link, "(scored 2-for-2 on verdicts)" ([pre-registration](/wiki/method/review/pre-registration)); and the seven-test battery, "(all passed ✓)", with its expected outputs, among them "66.58 vs 63.72 at seed 0" for T4 and "lstsq rms ≈ 3.29" for T7 ([the verification battery](/wiki/method/verification/battery)).

Two later documents cite other sections for these records: the round-3 pre-registration cites §6 for the 2-for-2 record (flag 35 in `review/wiki-build-flags.md`), and the docstring of `verify/battery.py` and #11 §7.2 place the T4 figures in #11 §2, which does not print them (flag 36).

The root `CLAUDE.md` carries the section forward under the heading "Method (HANDOFF §5)" and has added the lessons of rounds 3 and 4. The pre-registration record did not stay at 2-for-2: round 3 scored "**Miss**: the first after 2 for 2" on the verdict, and round 4 a "**Hit**" (`review/round3-adjudication.md`, `review/round4-adjudication.md`, 'Pre-registration scored').

## §6: review history and the measured failure mode

§6 is the only surviving account of the first two blind reviews of #14. Round 1, "(fresh Sonnet, web search, blind)", returned "**B / medium**"; round 2, on v2, "**B near B/C / medium**", with the weakest link "the α_d derivation". Each round's valid findings and the referee's own arithmetic errors are listed, the round-2 findings as pending for v3 ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

From both rounds it draws the "Measured failure mode": "fresh LLM referees are strong on structure, literature and logic; **unreliable on unaided arithmetic** (3 confident order-of-magnitude indictments, all reviewer unit errors, 0 surviving). Hence the iron rule." LLM stands for large language model. It adds that Claude Code's execution tools remove this failure mode, "that's the main reason the project is moving to you". Round 3 moved the failure mode to the author's side: "the author's verification checks the author's model" (`review/round3-adjudication.md`; [the measured referee failure mode](/wiki/method/review/referee-failure-mode)).

Round 3 is recorded as "(incomplete)": an execution-verified audit dispatched on 2026-10-17 "died partway on a rate limit". The handoff's "Suggested first task in Claude Code" was to re-run it, and its footer asks that the partial finding be treated "as unconfirmed until re-run". Both were done on 2026-10-19, and round 3 returned verdict C on #14 v3 ([review round 3](/wiki/method/review/round-3)).

## §7: working conventions

§7 records Paul's background and preferences: "Paul is an independent developer (Stanford Ginzton Lab research past in scanning acoustic microscopy — Fourier-domain physics, the origin of his intuition)", with the explicit instruction never to describe him as retired; the calibration he asked for ("keep the tier tags, keep machine-verifying, keep pre-registering, keep reporting negative results prominently. Honest obituaries are part of the deliverable"); the chunked work pattern resumed with "go"; the prose register for science writing; the house pattern for papers; the attribution line; and "simple bullets over prose paragraphs for working communication". The root `CLAUDE.md` 'Working with Paul' carries all of it forward ([the collaboration](/wiki/method/collaboration)). The wiki's own voice rules come from the same register.

## §8: the ranked queue

| Handoff item (§8) | What became of it |
| --- | --- |
| 1. "Cut v3 of `knot-dark-matter-standalone.md`" with the §6 pending list | done 2026-10-19 (commit 5dbaa82) |
| 2. "Re-run the execution-verified blind audit on v3" | done 2026-10-19: round 3, verdict C, and #14 withdrawn |
| 3. "√N-floor freeze-out estimate" | dropped by round-3 Decision 3 |
| 4. "Toy Lagrangian (acceptance criterion #1)", "Hardest; highest value. Start in 0+1 or 1+1 dimensions on the Siegel disk." | done to the referees' wording on 2026-10-20 ([toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models)) |
| 5. "PM-point comparison" (partially massless) | first in the current queue |
| 6. "Literature battery completion: every † reference in #11 and #13 source-checked; resolve the gravity-induced kinetic mixing question" | second in the current queue; Born's two papers were retrieved for the diameter note ([Open: the † literature battery](/wiki/method/literature-battery)) |
| 7. "Optional write-ups: phase-space diameter relation note (§4); LaTeX/arXiv shaping only after 1–5" | the diameter note done on 2026-10-26, version 1.1 after round 5 ([Round 5](/wiki/method/review/round-5)); the current queue names only items 5–6, so the shaping for arXiv is not in it |

The root `CLAUDE.md` records the decisions: "HANDOFF §8 queue item 3 is dropped. The current queue, in order: 1. HANDOFF §8 items 5–6: the partially-massless comparison and the † literature battery (Born 1938 and 1949 were retrieved for the diameter note; see its §4). 2. Optional: a round-6 review of the toy note, but only before any external use." It also records that "The phase-space-diameter note (HANDOFF §8 item 7) is done". From 2026-10-20 to 2026-10-26 the first item had read "HANDOFF §8 items 5–7", and the optional review was numbered round 5, the number the diameter note's review then took. "Reasons for the queue are in the round-3 adjudication's 'Decisions' section" ([round-3 decisions and lessons](/wiki/method/review/round-3/decisions); [open problems and the queue](/wiki/status/open-problems)).

## §9 and Appendix A

§9, "Repo suggestion (optional)", proposed folders for papers, popular articles, notes, review material and verification scripts, with `HANDOFF.md` at the root and `CLAUDE.md` pointing at it. The repository follows it, with #9 placed in `notes/` and #14 moved there after its withdrawal ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)).

Appendix A, "machine-verification battery (re-run first)", is the Python code of tests T1–T7 with the expected results: "T1–T3 all True; T4 converges to 4Tr(h²) and visibly ≠ FP; T5 = [0,0,0]; T6 = [0,1,3,3,1]; T7 rms ≈ 3.3." `verify/battery.py` is that code turned into assertions, with the same computations, seeds and random-number order, and it is the first script the gate runs ([the verification battery](/wiki/method/verification/battery); [the gate](/wiki/method/verification/the-gate)). The handoff's Appendix A is distinct from #11's Appendix A, which is the [audit of founding suppositions](/wiki/program/founding-suppositions).

## What is superseded or unresolved

Superseded by later documents:

- **The soliton candidate** (§2) and **the queue** (§8), by name (`wiki/CLAUDE.md`; root `CLAUDE.md`, 'Since the handoff'; #11 §12).
- **The reading of DESI** (§2), by DR2's phantom crossing (#11 §10, "Under pressure (v2.1)").
- **The statuses of #11, #14 and #15** (§3), **round 3 as incomplete** (§6), **the 2-for-2 pre-registration record** (§5) and **the read order** (§3), as above.
- **The tag of the compatibility theorem**: the handoff lists it as derived and machine-verified; #11 since v2.1 tags the statement [T].
- **The diameter relation's standing** (§4), by the phase-space-diameter note of 2026-10-26: no longer a conjecture but standard physics, with its "square exactly at the bounce" withdrawn ([Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)).

Unresolved inside the document: §1's "Three blind AI reviews returned verdict B" against §6's two completed rounds, B and "B near B/C", and an incomplete third. No document reconciles the count ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two#unresolved-how-many-reviews-returned-b); [conflicts between sources](/wiki/history/documents/source-conflicts#method-and-records)).

Flagged in `review/wiki-build-flags.md`, quoted here as written: item 7, "unique consistent structures" without "known"; item 16, the ✓ on "fails by 10²⁸–10³¹" without a script, now backed by `verify/velocity_gated_gravity.py` (addendum of 2026-10-28); item 55, "gate = X-exchange" in §2 and #5's "finds the gate's mechanism" in §3, which the gate-mechanism note finds not derived; item 23, a·ã = 1 as the |Z| = 1 locus; item 24, which bounce the diameter relation means, on which the diameter note's §6 tests every reading it records; item 26, "three-year data"; item 27, the negative V that the turnaround needs, against the potential V₀[1 + cos(τ/f)] of #11 §10, whose minimum is 0 for V₀ > 0, with its addendum of 2026-10-27 on the closed turnaround; item 29, the reading of X's range in momentum, documented only in the chat.

## Sources

- `HANDOFF.md` §1–§9 and Appendix A — the document itself; its first line, purpose and footer
- `CLAUDE.md` 'Since the handoff' — which parts are dead, dropped or replaced, the diameter note done, and the current queue; 'Layout' — the replacement read order; 'Method (HANDOFF §5)' — the method carried forward
- `papers/phase-space-diameter.md` header — version 1.1 and its round-5 verdict; §3 — the identity, κ, the radiation's entropy and photon count; §5 — the clock and the Siegel distance; §6 — the withdrawal, its obituary and the claim's likeliest origin, tagged "[D, inference]"
- `review/round5-adjudication.md` 'Recommendations to Paul' — accepting flags 23 and 24 recommended
- `wiki/CLAUDE.md` 'The wiki is derivative' — the handoff's rank, its superseded parts and the dead-stays-dead rule
- `papers/broken-born-checkpoint-v2.md` §5 — the re-tagged compatibility theorem; §10 — "Under pressure (v2.1)"; §12 — the soliton obituary and the two remaining candidates; §14 — the open items the handoff's list became
- `review/round3-adjudication.md` 'Pre-registration scored' and 'Decisions' — round 3's completion, the moved failure mode and the queue decisions; `review/round4-adjudication.md` 'Pre-registration scored' — the round-4 hit
- `review/wiki-build-flags.md` items 7, 16, 23, 24, 26, 27, 29 and 55 — the flags that concern statements in the handoff, items 16 and 27 with their addenda; items 35 and 36 — two later documents' pointers to sections that do not hold the records the handoff's §5 holds
- `notes/closed-universe.md` §2 — the turnaround in a closed universe with V ≥ 0
- `verify/battery.py` — Appendix A as assertions
- `notes/gate-mechanism.md` §5 — the text that depends on #11 §8's tag, including §2's "gate = X-exchange" and §3's "finds the gate's mechanism"
- `verify/velocity_gated_gravity.py` section D — the script now behind the ✓ on the clumping shortfall
