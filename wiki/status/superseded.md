---
title: "Superseded statements"
weight: 50
status: record
description: "Statements replaced by corrected versions — the original P2, the exponential cliff, ℤ₄ → ℤ₂, the v0.1 action, 'Ising class', the handoff's soliton candidate and queue, and others — each with its replacement."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "CLAUDE.md 'Layout'"
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §5"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/round4-adjudication.md 'Revisions for v2 of the note'"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Decisions'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "HANDOFF.md §5"
  - "HANDOFF.md §6"
  - "HANDOFF.md §8"
  - "HANDOFF.md §9"
  - "notes/broken-born-theory.md §0–§10 and addenda v0.3–v0.6"
  - "notes/broken-born-program-v1.md §8–§11"
  - "notes/debt1a-geometric-core.md §D–§E"
  - "notes/debt1a-ii-X-classification.md §1, §4, §5"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "README.md"
---

*This register lists statements the program once made and later replaced with corrected versions. A superseded statement differs from a dead claim: the subject survives, but its earlier form is no longer the program's position, often because a calculation forced a repair. Each line names the old statement, its replacement and where the replacement is recorded. The older documents are kept as an audit trail and still contain the old forms; the lab notebook, for example, keeps its version-0.1 body with the corrections appended as addenda, so the old forms read there as if current.*

**Status:** Record, a register current to 2026-10-20 — no tags of its own; each replacement keeps the tag its source gives — the replacements are recorded in higher-precedence sources: checkpoint #11 v2.2, the toy-model note v2, the review adjudications and the root `CLAUDE.md`.

## Key facts

- The pages with the status superseded are [the original P2](/wiki/program/postulates/original-p2) and [the geometric action S_H and the v0.1 action](/wiki/gravity/tuning-test/geometric-action). The other superseded statements are earlier forms recorded on the pages of the claims that replaced them.
- The largest repair is P2 → P2′. With both ω and η frozen there is no Grassmannian, no Maslov circle and no dark-energy field, and the [nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) makes the correction "forced" (#11 §4–§5).
- The documents succeed one another: the lab notebook #1 (version 0.1 with addenda v0.2–v0.6), then the program v1.0 (#9), then checkpoint #11, whose v2.2 "Supersedes v2.1, v2.0 and v1.0". The notes are "superseded as reference but kept" (root `CLAUDE.md`).
- The root `CLAUDE.md` supersedes two parts of `HANDOFF.md`: the §2 soliton candidate, now dead, and the §8 queue.
- Superseded is not dead. The heuristic w_eff = −2 − w̃ was superseded by w_eff = −w̃, and the claim that rested on it, that conjugate collapse powers our expansion, died ([obituary](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)). Conversely, the naive toy potential was replaced by a bounded one but is recorded as dead, in [the graveyard](/wiki/status/graveyard).

## Superseded statements by section

### The research program

- [Original P2: both structures rigid (superseded)](/wiki/program/postulates/original-p2) — "ω and η are non-dynamical; only H carries degrees of freedom" (#1 §1) → [P2′](/wiki/program/postulates/p2-prime): only ω is rigid, and η is emergent as the order parameter (#11 §4; #1 addendum v0.3).
- P2's "triple duty" (#1 §1): removing the would-be second graviton, enforcing a·ã = const, and supplying τ's potential → the second graviton returned as the massive X ([Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain); #1 addendum v0.4); a·ã = 1 now follows from ω-rigidity alone ([The cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint); #11 §10); the origin of the potential is open ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)).

### Phase-space geometry

- The compatibility theorem as "derived here" — tagged "[D — rigorous]" in calc note #5, [D] in #9 and "[D — compatibility theorem]" in #13, and presented as derived in #11 v2.0 → [T][V] since #11 v2.1 (§5): the statement is Freidel, Leigh and Minic's, and the block proof and the machine check are the program's. See [The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem).

### Spontaneous breaking of reciprocity

- The breaking pattern ℤ₄ → ℤ₂ = {1, ρ²}, with J = η⁻¹H as the order parameter [D] (#1 §2) → with only ω rigid, ρ sits inside a continuous U(1) and the polarization is a [Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) [D][V] (#11 §4, v2.2). Prediction row 9 still calls the zero linear term in photon dispersion "ρ²-protected" (#11 §13), an argument written out only in #1 §4. See [The order parameter](/wiki/symmetry-breaking/order-parameter) and [Row 9](/wiki/predictions/photon-dispersion).
- "Ising class" (the toy-model note's v1 and its worklog) → an "ordered ℤ₂ phase" in the frozen-H reduction (note v2 §4; round-4 revision 1). See [The frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction).
- The v1 Monte Carlo control values at T = 3, quoted without error bars as 0.078 / 0.033 / 0.014 → 0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004, from four independent seeds (note v2 §4). The round-4 ruling: "Fixed seeds gave reproducibility, not accuracy; the numbers lacked error bars." See [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo).
- The note's v1 statement of Mermin–Wagner → restricted to the compact SO(2) containing ρ, since the hyperbolic H-sector can break in two dimensions (round-4 ruling; note v2 §4). See [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)
- "Every derivation selects the pair" of sections (v1) → true only for d = 1; for d > 1 the literature gives a continuous family (round-4 ruling; note v2 §5). See [The section condition](/wiki/symmetry-breaking/section-condition).
- The matter coupling I_K as a function of K → it needs H as well as K and is covariant only under the SO(2) fixing H = 1, so v2 calls it (H, K)-built (round-4 finding F5; note v2 §5). See [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).
- "Increasing the truncation adds only massive levels" (v1) → the restoration argument restated with the mass renormalization of the bare μ² (round-4 finding F6, accepted, not re-checked; note v2 §4). The adjudication writes the tadpole's growth as 2 ln N, and the note as ln N, "a harmonic sum"; the two sources do not reconcile the coefficient. See [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration).

### Gravity

- [The geometric action S_H and the v0.1 action (superseded)](/wiki/gravity/tuning-test/geometric-action) — S = S_H + S_τ + S_x[SM; g] + S_p[χ; g, g̃] + S_mix, with S_x the unmodified Standard Model and S_H = ½M_B² ∫ √|H| R_B[H] built with ω and η frozen (#1 §3) → P2′ unfroze η (#11 §4), and the ghost-free structure now comes from the frame tier (#11 §7.2). Deriving the wedge sector from S_H is open item 1 ([Open: deriving the wedge sector](/wiki/gravity/tuning-test/wedge-reduction)).
- The v0.1 ghost analysis, "There is no second independent metric" (#1 §4) → reversed when calc note #6 showed X to be a second graviton (#1 addendum v0.4); ghost-freedom now comes from the frame tier (#1 addendum v0.5; #11 §7.2). See [The frame tier](/wiki/gravity/tuning-test/frame-tier).
- The three-way classification of X as healthy, auxiliary or ghost (calc note #5 §D) → resolved by calc note #6: X is a "massive spin-2, conditionally healthy", and "auxiliary X" is "off the table at the fundamental level" by shift symmetry (#6 §1, §5). See [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) and [Shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry).
- The novelty of the vacuum-energy identity — "that previously ad hoc branch" given "its reason to exist" (#1 addendum v0.6), and "at least two results that stand on their own" (#9 §11) → downgraded "from 'likely standalone result' to 'requires detailed comparison with the PM and exchange-symmetric literature'" (#11 §7.4; PM is partially massless). #11 §15 now counts "one identity awaiting a novelty verdict". See [Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison).

### Dark matter

- The Gaussian gate e^{−k²/μ²}, postulated with "support set by a scale μ of the g̃ sector" (#1 §3) → a gate F(k²/μ²) delivered by X-exchange, with μ the χ quantum's momentum-fiber width and the shape open [D — mechanism; shape [O]] (#11 §8). On the way, calc note #5 had "μ ↔ (M_X, M_B) parametrically" (§E); calc note #6 replaced it with the fiber width (§4). See [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) and [The gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism).
- The exponential cliff σ_T(v) = σ₀e^{−v²/v\*²}, "exactly zero in clusters forever" (#1 §5.1, §9 row 1) → a knee at v\* whose tail shape is open (#1 addendum v0.4; #11 §8, §13 row 1). See [The gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law) and [Row 1](/wiki/predictions/self-interaction-knee).
- The wave-side suppression (v\*/σ)³ (calc note #2) → (v\*/σ)⁴ (calc notes #3 and #4; #11 §9). See [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate).
- The X-condensate as dark matter, "[O — direction, deliberately unopened]" (#9 §10 item 7) → one of the two remaining candidates (#11 §12). See [The X-condensate candidate](/wiki/dark-matter/candidates/x-condensate).
- Reciprocity acting as modular S on the hidden coupling, the "load-bearing conjecture" behind α_d ≈ 34 in #14 v2 (`HANDOFF.md` §2) → Paul's decision of 2026-10-19 that "S-duality is no longer what fixes α_d" (`review/v3-worklog.md`); the candidate that needed the coupling is dead. See [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling).
- Superheavy solitons as the handoff's "current best" dark-matter candidate (`HANDOFF.md` §2) → dead as a program-native proposal (root `CLAUDE.md`; #11 §12). See [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary).
- The three-way candidate question of #11 v2.0 (`HANDOFF.md` §2, open item 8: particles, X-condensate or solitons) → two candidates since v2.1 (#11 §12). See [Dark-sector candidates](/wiki/dark-matter/candidates).

### Cosmology

- The dictionary w_eff = −2 − w̃, a heuristic of the development discussion → w_eff = −w̃; "the constraint's Jacobian changed the answer" (#11 §10; #1 §0, §6). The claim built on the old form is dead. See [The duality dictionary w_eff = −w̃](/wiki/cosmology/scale-factor-duality/duality-dictionary).
- The reading of the dark-energy survey data: the handoff called the framework consistent with the drift hints of the Dark Energy Spectroscopic Instrument's first two data releases (`HANDOFF.md` §2), and #11 §10's italic opener says its hints "are exactly the required drift" (#9 §8 has the same reading) → "under real pressure" ahead of the third data release (root `CLAUDE.md`; #11 §10, "Under pressure (v2.1)"). The italic opener of #11 §10 was not updated and still carries the older wording. See [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).

### Predictions

- The predictions tables of #1 §9 (ten rows; rows 1, 3 and 7 "the flagship discriminants") and #9 §9 (ten rows) → #11 §13 (eleven rows). Old rows 3 and 4 are dead, as obituaries in [the graveyard](/wiki/status/graveyard). See [History of the predictions table](/wiki/predictions/table-history).
- The parameter count of #1 §10, two parameters per sector → in the X sector, five βₙ reduce to two (calc note #8 §3; #11 §7.5). #11 has no full parameter table. See [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity).

### Method and review

- [T] as "theorem — established in the literature, cited" (#1 §0) → [T] as "established literature", with [V], [S] and † added (#11 header). See [Provenance tags and citation marks](/wiki/method/provenance-tags).
- Pre-registration "scored 2-for-2 on verdicts" (`HANDOFF.md` §5) → rounds 1–2 hit, round 3 missed, round 4 hit (`review/round4-adjudication.md`, "Pre-registration scored"). See [Pre-registration and its calibration record](/wiki/method/review/pre-registration).
- "Round 3 (incomplete)" (`HANDOFF.md` §6), with its partial finding "citations and core numbers check out so far" → completed with verdict C (`review/round3-adjudication.md`; root `CLAUDE.md`). See [Review round 3](/wiki/method/review/round-3).
- The gate's check of #14 v3, knot_numbers.py, which tested v3's own claims → `verify/soliton_obituary.py`, which "checks every number this record quotes, with independent anchors" (`review/round3-adjudication.md`). See [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script).

### History and documents

- `HANDOFF.md` §3's statuses — #11 as v2.0, the current reference with 25 references; #14 as v2, the current blind-review manuscript → #11 v2.2; #14 v3, withdrawn after failing round-3 review (root `CLAUDE.md`, "Layout"). See [The handoff document](/wiki/history/documents/handoff).
- `HANDOFF.md` §3's read order, #11 → #14 → `HANDOFF.md` §6 → calc notes → the root `CLAUDE.md`'s #11 → `HANDOFF.md` §6 → `review/round3-adjudication.md` → calc notes "only as a task needs them". See [CLAUDE.md and the README](/wiki/history/documents/project-instructions).
- `HANDOFF.md` §8's ranked queue → the root `CLAUDE.md` queue; see [Open problems and the queue](/wiki/status/open-problems).
- `HANDOFF.md` §9's suggested repository layout → the actual layout recorded in the root `CLAUDE.md`, "Layout".
- The `README.md` tagline, "Physics hypothesis explaining dark matter and missing magnetic monopoles", does not match the current record: the monopole explanation is dead (#11 §11.1), the dark-matter candidates are open (#11 §12), and the root `CLAUDE.md` calls the program "a Lakatosian research program, not a theory".

## Sources

- `CLAUDE.md` "Since the handoff", "Layout" — the soliton candidate dead; the current queue, read order and layout.
- `papers/broken-born-checkpoint-v2.md` header, §4, §5, §7.4, §8, §10, §12, §13, §15 — the current forms and their version notes.
- `papers/reciprocity-toy-models.md` §4, §5 — the toy-model note's v2 wording.
- `review/round4-adjudication.md` "Rulings", "Pre-registration scored", "Revisions for v2 of the note" — the corrections to the note's v1; the calibration record.
- `review/round3-adjudication.md` "Decisions" — the retired candidate; the replacement gate script.
- `HANDOFF.md` §2, §3, §5, §6, §8, §9 — the handoff's statements that later sources replaced.
- `notes/broken-born-theory.md` §0–§10 and addenda v0.3–v0.6 — the version-0.1 forms and their corrections.
- `notes/broken-born-program-v1.md` §8–§11 — v1.0's forms.
- `notes/debt1a-geometric-core.md` §D–§E, `notes/debt1a-ii-X-classification.md` §1, §4, §5 — the classification of X and the gate scale.
- `notes/debt3a-stream-stability.md` — the original (v\*/σ)³ suppression.
- `review/v3-worklog.md` "Findings neither referee raised" — the decision that S-duality no longer fixes α_d.
- `README.md` — the tagline.
