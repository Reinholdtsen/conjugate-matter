---
title: "Superseded statements"
weight: 50
status: record
description: "Every statement the program replaced with a corrected version — the two superseded pages and the earlier forms recorded on the pages of the claims that replaced them — each linked and paired with its replacement."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "CLAUDE.md 'Layout'"
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §5"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-adjudication.md 'Revisions for v2 of the note (all accepted; applied 2026-10-20 in commit 6606734)'"
  - "review/round3-adjudication.md 'Decisions'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §5"
  - "HANDOFF.md §6"
  - "HANDOFF.md §8"
  - "HANDOFF.md §9"
  - "notes/broken-born-theory.md §0–§12 and addenda v0.2–v0.6"
  - "notes/broken-born-program-v1.md §2–§11"
  - "notes/debt1a-geometric-core.md §B–§F"
  - "notes/debt1a-ii-X-classification.md §1–§5"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/debt1a-iv-beta-coefficients.md §1–§3"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3c-ufd-endpoint.md"
  - "notes/toy-lagrangian.md 'Chunk 2 results (2026-10-19): the Grosse–Wulkenhaar route'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions (written before construction)'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/wiki-build-flags.md items 6, 10, 11, 17, 27, 33, 37, 38"
  - "notes/closed-universe.md §2"
  - "README.md"
---

*This register lists the statements the program once made and later replaced with corrected versions. A superseded statement differs from a dead claim: the subject survives, but its earlier form is no longer the program's position, often because a calculation or a review forced a repair. Each line names the old statement, what replaced it and where the replacement is recorded. The older documents are kept as an audit trail and still contain the old forms: the [lab notebook](/wiki/history/documents/lab-notebook), for example, keeps its version-0.1 body with the corrections appended as addenda, so the old forms read there as if they were current.*

**Status:** Record, a register current to 2026-10-21 — no tags of its own; each replacement keeps the tag its source gives — the replacements are recorded in higher-precedence sources: [checkpoint #11](/wiki/history/documents/checkpoint) v2.2, the toy-model note v2, the review adjudications and the root `CLAUDE.md`.

Two pages have the status superseded. Every other entry is an earlier form recorded on the page of the claim that replaced it, under a heading "Superseded: …" that this register links; the few recorded in a page's body without such a heading are marked "in the body". The documents themselves succeed one another: the lab notebook #1 (version 0.1 with addenda v0.2–v0.6), then the program v1.0 (#9), then checkpoint #11, whose v2.2 "Supersedes v2.1, v2.0 and v1.0". The notes are "superseded as reference but kept" (root `CLAUDE.md`).

Superseded is not dead. The heuristic w_eff = −2 − w̃ was superseded by w_eff = −w̃, and the claim that rested on it, that conjugate collapse powers our expansion, died ([Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)). The naive toy potential, by contrast, was replaced by a bounded one but is recorded as dead in [the graveyard](/wiki/status/graveyard).

## Superseded pages

- [Original P2: both structures rigid (superseded)](/wiki/program/postulates/original-p2) — the lab notebook's second axiom made both the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω and the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η non-dynamical, leaving the degrees of freedom to H alone (#1 §1) → [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime), with η emergent as the order parameter (#11 §4; #1 addendum v0.3). #11 calls the correction forced: by [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) the theory has content beyond general relativity plus self-interacting dark matter if and only if η is emergent. Of the "triple duty" #1 §1 gave P2, the second graviton it was to remove returned as the massive X, the cosmological constraint a·ã = 1 survives from the rigidity of ω alone (#11 §10), and the origin of the dark-energy potential became an open problem; the first and the last are listed below.
- [The geometric action S_H and the v0.1 action (superseded)](/wiki/gravity/tuning-test/geometric-action) — the notebook's complete action S = S_H + S_τ + S_x + S_p + S_mix, its Einstein-like S_H written with ω and η frozen (#1 §3), and the argument that no second independent metric, and so no [ghost](/wiki/gravity/spin-2-fields/ghosts#the-lab-notebooks-minisuperspace-argument), can arise (#1 §4) → P2′ unfroze η, X was found to be a second graviton (#1 addendum v0.4), and ghost freedom now comes from [the frame tier](/wiki/gravity/tuning-test/frame-tier) (#11 §7.2). #11 writes no full action; deriving the wedge sector from S_H is [OP1](/wiki/gravity/tuning-test/wedge-reduction).

## Superseded statements by section

### The research program

- [Superseded: the v0.1 arena with three structures](/wiki/program/postulates/p1-arena#superseded-the-v01-arena-with-three-structures) — the notebook's P1 put three structures on phase space, ω, η and H (#1 §1) → #9 §2 and #11 §4 list only ω and H; η survives as a property of the vacuum.
- [Superseded: the v1 assessment](/wiki/program/assessment#superseded-the-v1-assessment) — #9 §11 counted "at least two results that stand on their own regardless of its fate", one sharpening of the hard core and two degeneration risks → #11 §15 counts one standing observation and "one identity awaiting a novelty verdict", two sharpenings, and adds to the risks three demotions and the second data release of the Dark Energy Spectroscopic Instrument (DESI).

### Phase-space geometry

- [Superseded: the three-way classification of X](/wiki/phase-space/modular-field/field-content#superseded-the-three-way-classification-of-x) — calc note #5 §D posed the nature of the [momentum graviton X](/wiki/gravity/momentum-graviton) as a computation with three outcomes, healthy, auxiliary or ghost → calc note #6 answered in other terms, "massive spin-2, conditionally healthy", with the shift symmetry removing the auxiliary outcome; the curvature expansion itself is reported in no document. The same history from the side of the forcing chain is listed under gravity.
- The compatibility theorem as "derived here" (in the body of [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)) — tagged "[D — rigorous]" in calc note #5 and presented as derived in #11 v2.0 → since #11 v2.1 the statement is Freidel, Leigh and Minic's [T], and the block proof and its machine check [V] are the program's (#11 §5).

### Spontaneous breaking of reciprocity

- [Superseded: the discrete breaking pattern](/wiki/symmetry-breaking/order-parameter#superseded-the-discrete-breaking-pattern) — ℤ₄ → ℤ₂ = {1, ρ²}, with J = η⁻¹H as the order parameter [D] (#1 §2) → "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (#11 §4). Prediction row 9 still calls the absent linear term in photon dispersion "ρ²-protected", an argument written out only in #1 §4.
- [Superseded: the rigid symplectic form as the source of the tilt](/wiki/symmetry-breaking/rho-preserving-potential#superseded-the-rigid-symplectic-form-as-the-source-of-the-tilt) — the notebook's account of the dark-energy potential: its "existence comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2)" (#1 §3) → under P2′, ω alone leaves the polarization a Goldstone angle, a definite polarization needs "more structure than ω alone" (#11 §4), and where that structure comes from is [open](/wiki/symmetry-breaking/rho-preserving-potential). The same statement is recorded on τ's page, listed under cosmology.
- [Superseded: a coupling built from K alone](/wiki/symmetry-breaking/matter-coupling#superseded-a-coupling-built-from-k-alone) — the worklog's "The ρ-covariant interaction I_K[W]" and the reviewed note's "K-covariant" coupling → round-4 finding F5 showed that it needs H as well, and v2 calls it "A coupling built from (H, K)", covariant under the SO(2) fixing H = 1 (note §5). `verify/toy_s5.py` still says "built from K" (flag 10 in `review/wiki-build-flags.md`).
- [Superseded: every derivation selects the pair](/wiki/symmetry-breaking/section-condition#superseded-every-derivation-selects-the-pair) — the worklog's literature summary and the reviewed note's agreement with the double-field-theory literature, "where every derivation selects the pair" of null sections → restricted to d = 1 by the round-4 ruling and revision 5; for d > 1 the section condition leaves "a continuous family of sections" (note v2 §5).
- [Superseded: the worklog's first verdict](/wiki/symmetry-breaking/toy-models/acceptance-criterion#superseded-the-worklogs-first-verdict) — acceptance criterion 1 "Met, in the referees' wording, by the coset toy plus a τ-type potential", the breaking "(Ising class in 1+1, Monte Carlo verified)" → met "by the coset model of (H, K) with a bounded ρ-preserving potential", with "an ordered ℤ₂ phase in 1+1 in the frozen-H reduction" (#11 §14 item 11). The τ-type potential is unbounded below with H dynamical ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)).
- [Superseded: Ising-class breaking in model I](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction#superseded-ising-class-breaking-in-model-i) — the note's first version claimed Ising-class breaking of ρ in model I in 1+1 → round 4 narrowed the claim from model I to the frozen-H reduction, since the simulation never let H move, and from a universality class to order: "ordered Z₂ phase", not "Ising class" (revision 1; note v2 §4).
- [Superseded: the first version's control values](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo#superseded-the-first-versions-control-values) — the high-temperature control "0.078 → 0.033 → 0.014", from fixed seeds and without error bars → the four-seed means 0.0653 ± 0.0043, 0.0338 ± 0.0013 and 0.0155 ± 0.0004 (note v2 §4). The round-4 ruling: "Fixed seeds gave reproducibility, not accuracy; the numbers lacked error bars."
- [Superseded: the first version's unrestricted theorem](/wiki/symmetry-breaking/toy-models/coset-model/so2-question#superseded-the-first-versions-unrestricted-theorem) — the note's first version applied the two-dimensional no-breaking theorem to all of model I's continuous breaking, ignoring the exception for its non-amenable Sp(2,ℝ) → restricted to the compact SO(2) that contains ρ (round-4 ruling; note v2 §4); whether the coupled model breaks that SO(2) is [open](/wiki/symmetry-breaking/toy-models/coset-model/so2-question).
- [Superseded: the reversed sign of the polarization](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua#superseded-the-reversed-sign-of-the-polarization) — the worklog's first version of a line in its chunk 2 had the sign of the polarization reversed → corrected on 2026-10-19 to "β = 0 is broader in x than in p (Δ(0) = +10.88 > 0)", a sign the round-4 referee confirmed independently.
- [Superseded: "Increasing the truncation adds only massive levels"](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration#superseded-increasing-the-truncation-adds-only-massive-levels) — the note's first argument for restoration in the complex model → v2 rests it on the exact independence of the condensate phases and adds the caveat that the bare μ² is renormalized and that fixed bare μ² "is not a consistent large-N limit" (round-4 finding F6, accepted, not re-checked). The tadpole's coefficient, ln N or 2 ln N, is flag 11.

### Gravity

- [Superseded: no second graviton under the original P2](/wiki/gravity/momentum-graviton/forcing-chain#superseded-no-second-graviton-under-the-original-p2) — #1 §4: "There is no second independent metric" → reversed by the v0.4 addendum once calc note #6 showed X to be a second graviton; ghost freedom now comes from the frame tier, "ghost-free by construction" (#11 §7.2).
- [Superseded: the three-way classification of X](/wiki/gravity/momentum-graviton/forcing-chain#superseded-the-three-way-classification-of-x) — X as healthy, auxiliary or ghost, "the single most important remaining calculation" of calc note #5 §D → calc note #6 §5: "Not healthy-by-default, not auxiliary, not necessarily ghost: *massive spin-2, conditionally healthy*"; whether X carries a ghost became the condition that [the tuning test](/wiki/gravity/tuning-test) examined.
- [Superseded: earlier forms of the safety argument](/wiki/gravity/momentum-graviton/fifth-force-safety#superseded-earlier-forms-of-the-safety-argument) — calc notes #5 and #6 combined X's short range with a weak coupling of ordinary matter to X through its dual stress, and calc note #7 required the massless combination to dominate the couplings of ordinary matter → calc note #8 §3: safety by range alone, with couplings of gravitational strength "Yukawa-cut at 1/M_X" (#11 §7.5; [Yukawa forces](/wiki/gravity/spin-2-fields/yukawa-forces#the-momentum-graviton-x)).
- [Superseded: safety through a dominant massless combination](/wiki/gravity/tuning-test/constrained-bimetric#superseded-safety-through-a-dominant-massless-combination) — the same replacement, recorded on [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric): "safety is by range, not decoupling" (#8 §3).
- [Superseded: the graviton-mass bound as a mixing-angle check](/wiki/gravity/momentum-graviton/spectrum-and-parity#superseded-the-graviton-mass-bound-as-a-mixing-angle-check) — calc note #7 §4 read the gravitational-wave bounds on a graviton mass as a check on the mixing angle → calc note #8 §3: the bounds "apply to the even eigenstate, which is exactly massless", so they hold identically (#11 §7.5; row 6).
- [Superseded: earlier forms of the answer](/wiki/gravity/momentum-graviton/borns-answer#superseded-earlier-forms-of-the-answer) — Born's answer stated more strongly: its vacuum energy "zero by theorem" (#1 addendum v0.6), Debt 1 called closed without qualification (#1 addendum v0.6; #9 §5), and "theory" the defensible word after a pass (calc note #6 §5) → #11: "its wedge vacuum energy zero by identity", the open items of §14, and "theory" waiting on OP1–OP3.
- [Superseded: the v1 count of two standalone results](/wiki/gravity/momentum-graviton/symplectic-partner#superseded-the-v1-count-of-two-standalone-results) — #9 §11's "at least two results that stand on their own regardless of its fate" → #11 §15 keeps the symplectic-partner observation and counts the vacuum-energy identity as "one identity awaiting a novelty verdict".
- [Superseded: an ad hoc branch given a reason to exist](/wiki/gravity/palindromic-branch/palindrome#superseded-an-ad-hoc-branch-given-a-reason-to-exist) — calc note #8 §1, #1 addendum v0.6 and #9 §5: reciprocity gave the interchange-symmetric branch of bimetric gravity its "reason to exist" → #11 §7.4: the branch "appears in the partially-massless (PM) bimetric literature", and whether reciprocity is the origin of the PM symmetry is [OP2](/wiki/gravity/palindromic-branch/pm-comparison).
- [Superseded: the standalone-result claim](/wiki/gravity/palindromic-branch/pm-comparison#superseded-the-standalone-result-claim) — calc note #8 §2 expected the vacuum-energy identity, if unnoticed in the literature, to be "a standalone publishable observation", and #9 §5 "a standalone result" → #11 §7.4 downgraded the novelty claim from "likely standalone result" to "requires detailed comparison with the PM and exchange-symmetric literature".
- [Superseded: the cancellation framed as a cosmological-constant result](/wiki/gravity/spin-2-fields/cosmological-constant-problem#superseded-the-cancellation-framed-as-a-cosmological-constant-result) — "A cosmological-constant cancellation for free, from symmetry" (#9 §5) and "by symmetry rather than tuning" (#1 addendum v0.6, queried by flag 6) → #11: the cancellation concerns the wedge sector at the aligned point and does not by itself address matter-loop vacuum energy (§7.3), and its novelty awaits comparison (§7.4).
- [Superseded: a pass as the threshold for "theory"](/wiki/gravity/tuning-test/conditional-pass#superseded-a-pass-as-the-threshold-for-theory) — calc note #6 §5: "Pass ⇒ the geometric core stands and 'theory' becomes the defensible word" → #9 §11: "The word 'theory' awaits items 1–2 of §10"; #11 §15: it "still waits on items 1–3" (OP1–OP3). The tuning test's pass stands.

### Dark matter

- [Superseded: the Gaussian gate of v0.1](/wiki/dark-matter/conjugate-matter/velocity-gate#superseded-the-gaussian-gate-of-v01) — the gate e^{−k²/μ²}, its existence a postulate [P] and its Gaussian form underived (#1 §3) → the mechanism is X exchange (addendum v0.3), μ is the χ quantum's [momentum-fiber width](/wiki/phase-space/reciprocity/momentum-fibers#quanta-with-a-width-along-the-fiber) (addendum v0.4), and the gate is an unspecified F(k²/μ²), tagged [D — mechanism; shape [O]] (#9 §6; #11 §8). The two conventions for the gate's exponent are flag 17.
- [Superseded: earlier forms of the mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#superseded-earlier-forms-of-the-mechanism) — μ as a scale of the momentum-space metric (#1 §3), then tied to the masses M_X and M_B "parametrically" (calc note #5 §E), and an auxiliary X delivering the gate directly (#5 §D) → μ as the χ quantum's own width (calc note #6 §4), and a contact operator obtained by integrating out a massive, propagating X.
- [Superseded: the exponential cliff of v0.1](/wiki/dark-matter/conjugate-matter/scattering-law#superseded-the-exponential-cliff-of-v01) — σ_T(v) = σ₀e^{−v²/v\*²}, "An exponential cliff, not a power-law tail" (#1 §5.1) → a knee at v\* whose tail shape is open (#1 addendum v0.4; #11 §8, §13 row 1).
- [Superseded: the v0.1 predictions from the benchmark](/wiki/dark-matter/conjugate-matter/benchmark#superseded-the-v01-predictions-from-the-benchmark) — cross-sections above the gate computed from the cliff, a cluster self-interaction "identically zero at any future sensitivity", and two parameters covering five phenomena (#1 §5.1, §10) → #11 row 1 keeps "zero cluster signal (particle χ)" with no number; the numbers hold only for a Gaussian tail, and two of the five phenomena died.
- [Superseded: the cubic suppression of Debt 3a](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#superseded-the-cubic-suppression-of-debt-3a) — "(v\*/σ)³ suppression rather than an exponential" (calc note #2) → (v\*/σ)⁴ (calc notes #3 and #4; #11 §9).
- [Superseded: racing stream growth against orbital stirring](/wiki/dark-matter/momentum-clumping/gated-vlasov-model#superseded-racing-stream-growth-against-orbital-stirring) — the notebook's stream growth rate against orbital phase-mixing, "the theory's most important undone calculation on the astrophysics side" (#1 §5.2) → calc note #2: below the instability threshold there is no growth to race, "the flocking never starts", and the benchmark misses the threshold by 28–31 orders of magnitude.
- [Superseded: Debt 3b's ultra-faint-dwarf row](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies#superseded-debt-3bs-ultra-faint-dwarf-row) — calc note #3 entered ultra-faint dwarfs with a density of 20 GeV/cm³ and a [velocity dispersion](/wiki/dark-matter/halo-astrophysics/velocity-dispersion#the-values-in-the-programs-notes) of 3 km/s → calc note #4 used Segue 1's values, ρ ≈ 100 GeV/cm³ and σ ≈ 3.7 km/s, calling the earlier density "the conservative 20 used in 3b".
- [Superseded: reciprocity acting as modular S](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#superseded-reciprocity-acting-as-modular-s) — #14 v2's "load-bearing conjecture" that reciprocity acts on the hidden coupling as the [modular S transformation](/wiki/electric-magnetic-duality/modular-group#the-coupling-conjecture-of-the-soliton-manuscript), fixing α_d ≈ 34 → Paul's decision of 2026-10-19 that "S-duality is no longer what fixes α_d" (`review/v3-worklog.md`); the candidate that needed the coupling is dead ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).
- [Superseded: F2, which coupling sets the soliton mass](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#superseded-f2-which-coupling-sets-the-soliton-mass) — the worklog's resolution of v2's two couplings, a weak elementary coupling α_e,d ≈ α with heavy, strongly coupled solitons, adopted on 2026-10-19 as hypothesis H → not refuted, but superseded because hypothesis H died with the candidate.
- [Superseded: the convention and running spread](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling#superseded-the-convention-and-running-spread) — the worklog's adjudication that the value 34 depends on a convention by a factor of 4 and is lower when the couplings are matched at a higher energy (item R2) → with hypothesis H dead, nothing in the program fixes α_d, and the spread bears on no current claim.
- [Superseded: the "point, not a window" of the v3 worklog](/wiki/dark-matter/candidates/soliton-candidate/overproduction#superseded-the-point-not-a-window-of-the-v3-worklog) — worklog finding F1: the Kibble estimate with p = 1 closes "at a single point, M\* ≈ 3.0×10¹³ GeV", and v3 moved its benchmark there: "This is a point, not a window." → the (M/M\*)⁴ scaling of the [dilution](/wiki/cosmology/early-universe/relic-yield-and-dilution#how-much-dilution-a-relic-needs) survives, but the numbers rest on a wrong normalization ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)); the record cites only the gated values.
- [Superseded: the handoff's "current best" candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary#superseded-the-handoffs-current-best-candidate) — `HANDOFF.md` §2's best dark-matter candidate, superheavy [topological solitons](/wiki/symmetry-breaking/topological-defects#topological-and-non-topological-solitons-t) of a separate, strongly coupled dual gauge sector, with its open items and queue items 1–3 → dead as a program-native proposal (root `CLAUDE.md`; #11 §12; round-3 Decision 2); queue items 1 and 2 were done and item 3 was dropped.
- The X-condensate as a direction (in the body of [the X-condensate candidate](/wiki/dark-matter/candidates/x-condensate)) — "[O — direction, deliberately unopened]" (#9 §10 item 7) → one of the two remaining candidates (#11 §12).

### Cosmology

- [Superseded: the earlier heuristic rule](/wiki/cosmology/scale-factor-duality/duality-dictionary#superseded-the-earlier-heuristic-rule) — w_eff = −2 − w̃, a heuristic of the development discussion that identified densities across frames "without the constraint's volume Jacobian" → w_eff = −w̃ (#1 §0, §6; #11 §10). The claim built on the old rule is dead.
- [Superseded: the potential's origin in the rigid ω](/wiki/cosmology/dark-energy/tau-quintessence#superseded-the-potentials-origin-in-the-rigid-ω) — the same attribution of the potential of the dark-energy field τ to the rigid ω (#1 §3), summed up in #1 §12 as a single spontaneously broken symmetry "with a rigid symplectic form as its explicit tilt" → the potential's periodicity [D] stands, and its origin is open (calc note #5 §F; #11 §4; root `CLAUDE.md`).
- [Superseded: the earlier readings of DESI](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing#superseded-the-earlier-readings-of-desi) — #1, #9, `HANDOFF.md` §2, #14 v3, both popular articles and the italic passage of #11 §10 read the instrument's results as support for the drift → "under real pressure" (root `CLAUDE.md`; #11 §10, "Under pressure (v2.1)"; round-3 ruling 11), since its second data release favours a phantom crossing above z ≈ 0.4. The italic passage of #11 §10 was not updated.

### Predictions

- [Superseded: the exponential cliff of v0.1](/wiki/predictions/self-interaction-knee#superseded-the-exponential-cliff-of-v01) — row 1 as a cliff, "exactly zero in clusters forever" (#1 §9) → "Knee at v\* ~ 10² km/s; zero cluster signal (particle χ)" (#11 §13).
- [Superseded: the exponential and the cube](/wiki/predictions/island-discriminant#superseded-the-exponential-and-the-cube) — row 3's "exponential" particle side, and calc note #2's (v\*/σ)³ for the wave side → "sharp" against (v\*/σ)⁴ (#9 §7; #11 §9, §13).
- [Superseded: DESI read as support](/wiki/predictions/dark-energy-drift#superseded-desi-read-as-support) — row 4's side of the same change: the documents read the survey's hints as confirmation of the drift → the technical record of #11 §10 and the root `CLAUDE.md`.
- [Superseded: "after V(τ) < 0"](/wiki/predictions/fate-of-expansion#superseded-after-vτ--0) — row 5's "Turnaround after V(τ) < 0 = conjugate bounce" (#9 §9) → "Turnaround = conjugate bounce" (#11 §13); no document says why the clause was dropped, and the sign of V is flag 27, whose addendum (2026-10-27) finds the turnaround with V ≥ 0 in a closed universe ([a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe)).
- [Superseded: "not previously posed"](/wiki/predictions/massless-graviton#superseded-not-previously-posed) — #9 §11 counted the masslessness of the even eigenstate among its "novel predictions not previously posed" → #11 §15 names only rows 3 and 11; no document says why.
- [Superseded: earlier forms of the row](/wiki/predictions/direct-detection-null#superseded-earlier-forms-of-the-row) — row 7's permanent null, first for χ (#1 §9), then for χ or the X-condensate (#9 §9), then for all three candidates of #11 v2.0 → for "both dark-sector candidates", with P4 strict (#11 v2.1, v2.2).
- [Superseded: the spectral step and the ±0.03 target](/wiki/predictions/early-universe-step#superseded-the-spectral-step-and-the-003-target) — #1's row 10, with a step in the gravitational-wave spectrum and a target of ±0.03 in N_eff for the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#row-10s-probe-cmb-s4) experiment CMB-S4 → v1 dropped both (#9 §9), and #11 kept v1's form; no document says why.
- [Superseded: the three-way question](/wiki/predictions/dark-sector-microstructure#superseded-the-three-way-question) — particles, X-condensate or solitons (#11 v2.0; `HANDOFF.md` §2 item 8) → two candidates since #11 v2.1, after round-3 Decision 2 ([dark-sector candidates](/wiki/dark-matter/candidates)).
- [Superseded: the parameter count](/wiki/predictions/table-history#superseded-the-parameter-count) — #1 §10's two parameters per sector → #11 keeps only the dark-energy row, as the [over-constraint](/wiki/cosmology/dark-energy/over-constraint), and has no full parameter table; in the X sector five βₙ reduce to two (calc note #8 §3; #11 §7.5).
- The predictions tables (in the body of [history of the predictions table](/wiki/predictions/table-history)) — the ten rows of #1 §9, with rows 1, 3 and 7 "the flagship discriminants", and the ten of #9 §9 → the eleven of #11 §13; old rows 3 and 4 are dead, as obituaries in [the graveyard](/wiki/status/graveyard).

### Method and review

- [T] as "theorem — established in the literature, cited" (#1 §0) → [T] as "established literature", with [V], [S] and † added (#11 header); in the body of [provenance tags and citation marks](/wiki/method/provenance-tags).
- The pre-registration record "scored 2-for-2 on verdicts" (`HANDOFF.md` §5) → rounds 1–2 hit, round 3 missed and round 4 hit (`review/round4-adjudication.md`, "Pre-registration scored"); in the body of [pre-registration and its calibration record](/wiki/method/review/pre-registration).
- "Round 3 (incomplete)" (`HANDOFF.md` §6), with its partial finding "citations and core numbers check out so far" → completed with verdict C (`review/round3-adjudication.md`; root `CLAUDE.md`); in the body of [Review round 3](/wiki/method/review/round-3).
- The gate's check of #14, `knot_numbers.py`, written to recompute the numbers of v2 and then v3 → `verify/soliton_obituary.py`, which "checks every number this record quotes, with independent anchors" (`review/round3-adjudication.md`) (flag 33 in `review/wiki-build-flags.md`: its checks cover less than this; see [what it does not check](/wiki/method/verification/soliton-obituary-script#what-it-does-not-check)); in the body of [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script).

### History and documents

- `HANDOFF.md` §3's statuses, #11 as v2.0, the current reference, and #14 as v2, the current blind-review manuscript → #11 v2.2, and #14 v3, withdrawn after failing the round-3 review (root `CLAUDE.md`, "Layout"); in the body of [the handoff document](/wiki/history/documents/handoff).
- `HANDOFF.md` §3's read order, #11 → #14 → `HANDOFF.md` §6 → calc notes → the root `CLAUDE.md`'s #11 → `HANDOFF.md` §6 → `review/round3-adjudication.md` → calc notes "only as a task needs them"; in the body of [CLAUDE.md and the README](/wiki/history/documents/project-instructions).
- `HANDOFF.md` §8's ranked queue → the root `CLAUDE.md`'s queue, on [open problems and the queue](/wiki/status/open-problems#the-work-queue).
- `HANDOFF.md` §9's suggested repository layout → the layout recorded in the root `CLAUDE.md`, "Layout".
- The root `CLAUDE.md`'s "#11 is now v2.1" → v2.2, as a later bullet of the same section says (flag 38).
- The `README.md` tagline, "Physics hypothesis explaining dark matter and missing magnetic monopoles" → not rewritten, but overtaken by the record: the monopole explanation is dead (#11 §11.1), the dark-matter candidates are open (#11 §12), and the root `CLAUDE.md` calls the program "a Lakatosian research program, not a theory" (flag 37).

## Sources

- `CLAUDE.md` "Since the handoff", "Layout" — the soliton candidate dead; the current queue, read order and layout; "#11 is now v2.1".
- `papers/broken-born-checkpoint-v2.md` header, §4, §5, §7, §8, §10, §12, §13, §14, §15 — the current forms and their version notes.
- `papers/reciprocity-toy-models.md` §1, §4, §5 — the toy-model note's v2 wording.
- `review/round4-adjudication.md` "Rulings", "Pre-registration scored", "Revisions for v2 of the note" — the corrections to the note's first version; the calibration record.
- `review/round3-adjudication.md` "Decisions" — the retired candidate; the replacement gate script.
- `HANDOFF.md` §2, §3, §5, §6, §8, §9 — the handoff's statements that later sources replaced.
- `notes/broken-born-theory.md` §0–§12 and addenda v0.2–v0.6 — the version-0.1 forms and their corrections.
- `notes/broken-born-program-v1.md` §2–§11 — v1.0's forms.
- `notes/debt1a-geometric-core.md` §B–§F, `notes/debt1a-ii-X-classification.md` §1–§5, `notes/debt1a-iii-tuning-test.md` §4, `notes/debt1a-iv-beta-coefficients.md` §1–§3 — the classification of X, the gate scale, the safety argument and the novelty claims.
- `notes/debt3a-stream-stability.md`, `notes/debt3b-wave-island.md`, `notes/debt3c-ufd-endpoint.md` — the cubic suppression, the race against stirring, the ultra-faint-dwarf row.
- `notes/toy-lagrangian.md` "Chunk 2 results", "Assessment against the predictions" — the reversed sign; the first verdict.
- `review/v3-worklog.md` "Findings neither referee raised", "Round-2 pending list" — F1, F2 and R2; the decision that S-duality no longer fixes α_d.
- `review/wiki-build-flags.md` items 6, 10, 11, 17, 27, 33, 37, 38 — the flagged statements named above; item 27's addendum and `notes/closed-universe.md` §2 — the turnaround in a closed universe.
- `README.md` — the tagline.
