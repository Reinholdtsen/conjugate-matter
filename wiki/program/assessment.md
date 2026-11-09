---
title: "Assessment: a live research program"
weight: 70
status: record
description: "The checkpoint's Lakatosian self-assessment: the hard core intact and twice sharpened, forced convergence and the other progressive signs, the degeneration risks, and near-term falsification exposure."
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 items 1–3"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 8"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §1"
  - "wiki/papers/broken-born-checkpoint-v2.md §2"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §8–§13"
  - "HANDOFF.md §1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/x-classification.md §5"
  - "notes/tuning-test.md §3, §5"
  - "notes/beta-coefficients.md §2"
  - "notes/wave-island.md 'What pins g?'"
  - "notes/broken-born-program-v1.md §10–§11"
  - "review/round3-adjudication.md 'Verdict'"
  - "review/round4-adjudication.md 'Verdict'"
  - "review/round5-adjudication.md 'Verdict'"
  - "verify/battery.py T4, T5, T7"
  - "verify/soliton_obituary.py"
  - "notes/closed-universe.md §2"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §5"
  - "review/wiki-build-flags.md items 27 (addendum), 46"
  - "review/wiki-build-flags.md item 55"
  - "review/wiki-build-flags.md item 63"
  - "notes/literature-check.md §5"
  - "notes/literature-check.md §6"
  - "review/wiki-build-flags.md items 66, 67"
---

*The assessment is the [checkpoint](../history/documents/checkpoint.md)'s own judgement of where the program stands, written in the terms of Imre Lakatos's account of research programmes: a hard core that is kept fixed, auxiliary claims that may be revised, and the question of whether the program keeps producing new predictions (progressive) or only accommodates its failures (degenerating). Checkpoint [#11](../papers/broken-born-checkpoint-v2.md) finds the hard core intact and sharpened twice by corrections that later derivations forced. It lists the signs of progress and the risks of degeneration side by side, it names three predictions that observations could falsify soon, and it notes that the current dark-energy data already lean against one of them. Its verdict is that this is a live research program, and that the word "theory" waits on three [open problems](../status/open-problems.md).*

**Status:** Record — untagged: a self-assessment, not a derivation. It is [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment), and it supersedes the v1 assessment ([#9 §11](../../notes/broken-born-program-v1.md#11-assessment)). The numbers it rests on carry the tags of the sections they come from; only those tagged [V] are machine-checked.

## What the assessment is

Lakatos judged a body of research over time rather than one hypothesis at a time. A programme keeps a hard core fixed and revises the auxiliary claims around it; it is progressive while its revisions lead to new predictions, and degenerating while its revisions only absorb failures after the fact [T] ([Lakatos's methodology](../method/lakatosian-methodology.md)). [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) sorts the program's record under four headings in those terms: the hard core, progressive signs, degeneration risks and falsification exposure. The status line the project gives itself follows from it: "a Lakatosian research program, not a theory" ([`HANDOFF.md` §1](../../HANDOFF.md#1-what-this-project-is); root [`CLAUDE.md`](../../CLAUDE.md)).

The assessment sits beside a calibration in #11's methodological preface. Novel structural claims (Tier 3) carry an "honest prior per claim ~50–80% pending expert review", and "Negative results (§9, §7.1, and the failure of [#14](../../notes/knot-dark-matter-standalone.md)'s model in §12) are the most reliable Tier-3 items, since the program's incentive gradient ran against them" ([#11 §2](../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification); [claim tiers and selection bias](../method/claim-tiers.md)).

## The hard core: intact, twice sharpened

"**hard core** (spontaneously broken reciprocity, ω-only rigidity) intact, twice sharpened by forced corrections (P2′; the w-dictionary)" ([#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment); [the hard core](hard-core.md)). In the w-dictionary, w is a fluid's [equation of state](../cosmology/dark-energy/quintessence.md#dark-energy-and-the-equation-of-state), the ratio of its pressure to its energy density. Both corrections came from derivations rather than from data:

- **P2′.** The first rigidity postulate fixed both the [symplectic form](../phase-space/reciprocity/symplectic-form.md) ω and the [neutral metric](../phase-space/born-geometry/born-structures.md) η. With both fixed, the program reduced to [general relativity](../gravity/spin-2-fields/general-relativity.md) plus one model of [self-interacting dark matter](../dark-matter/halo-astrophysics/self-interacting-dark-matter.md), with no [dark-energy field](../cosmology/dark-energy/tau-quintessence.md). The [nontriviality theorem](postulates/nontriviality-theorem.md) [D] showed that the program has content only if η is emergent, which forced [P2′](postulates/p2-prime.md): only ω is rigid.
- **The w-dictionary.** An early heuristic rule for how energy in the [conjugate description](conjugate-universe.md) acts on our expansion, w_eff = −2 − w̃, was replaced by the derived rule w_eff = −w̃ [D — corrected en route]: "the constraint's Jacobian changed the answer" ([#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology); [the duality dictionary](../cosmology/scale-factor-duality/duality-dictionary.md)). As a map of fluid variables, the derived rule is the scale-factor duality of string cosmology with sources; its derivation from a·ã = 1 is the program's (flag 66, pending).

## Progressive signs

[#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment): "forced convergence onto consistency islands; predictions not previously posed (rows 3, 11); an unsolicited identity (§7.3); one over-constraint (DE sector); the §11.3 unification generating new questions." DE is dark energy.

### Forced convergence onto consistency islands

The claim is that each structural test that could have killed the program's geometric sector instead forced it onto the one consistent structure available at that point. A consistency island, in the [field-equation note](../history/documents/field-equation-notes.md)'s usage, is "the unique known consistent structure" at such a junction; the term is unrelated to the particle and [wave islands](../dark-matter/momentum-clumping/wave-island/_index.md) of [the clumping problem](../dark-matter/momentum-clumping/_index.md). [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) counts "four consecutive consistency tests" without naming them. The documents give the chain in three versions:

- The field-equation note that first made the point counted three: "three structural tests in a row (multi-graviton no-go, signature obstruction, tuning test) could each have killed the geometric sector outright; each instead forced it into the unique known consistent structure at that junction. Repeated forced convergence onto consistency islands is the opposite of degeneration" ([`notes/tuning-test.md` §5](../../notes/tuning-test.md#5-status-of-the-field-equation-problem)).
- The v1 assessment named four: "no-go → Higgs → HR class → palindrome" ([#9 §11](../../notes/broken-born-program-v1.md#11-assessment)), HR being Hassan–Rosen.
- #11's technical abstract lists a chain of structural results, "a compatibility theorem [T][V]; the multi-graviton no-go [8†]; a signature obstruction; an explicit tuning test [V]", that forces the [momentum graviton X](../gravity/momentum-graviton/_index.md) to be a massive spin-2 field ([#11 §1](../papers/broken-born-checkpoint-v2.md#1-two-abstracts)).

The count of four is #11's, as in [`HANDOFF.md` §1](../../HANDOFF.md#1-what-this-project-is), and #11 governs. The steps of the v1 chain, as [#11 §7](../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) records them:

1. **The no-go.** X, the symmetric partner of the metric, transforms as a second graviton, and two interacting massless gravitons are inconsistent, so "Massless X is excluded by the multi-graviton no-go [8†]" ([the multi-graviton no-go theorem](../gravity/spin-2-fields/multi-graviton-no-go.md)); an ungauged X is excluded by [Lorentz signature](../gravity/spin-2-fields/signature-obstruction.md), the "signature obstruction".
2. **The Higgs mechanism.** "The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive" ([the gravitational Higgs mechanism](../gravity/momentum-graviton/gravitational-higgs.md)).
3. **The Hassan–Rosen class.** "The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†]" (on the qualifier "known" that calc note [#6 §3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) has and this sentence drops, see flag 7 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md)), dRGT being [de Rham–Gabadadze–Tolley](../gravity/spin-2-fields/drgt-massive-gravity.md) ([the Fierz–Pauli mass term](../gravity/spin-2-fields/fierz-pauli.md); [Hassan–Rosen bimetric gravity](../gravity/spin-2-fields/hassan-rosen-bimetric.md)). The [tuning test](../gravity/tuning-test/_index.md), tagged [D][V] in [#11 §7.2](../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv), found the program's natural metric-tier mass terms outside that structure in two independent ways, each checked numerically: a linearized mass term whose limit, 66.58 for the battery's test matrix, differs from the Fierz–Pauli form's 63.72 (test T4), and a nonlinear term outside the allowed span, with rms residual 3.29 (test T7; [the verification battery](../method/verification/battery.md)). The [frame-tier](../gravity/tuning-test/frame-tier.md) couplings belong to the Hinterbichler–Rosen class, "ghost-free by construction", which the calc note tags "[D — structural, resting on T]" ([`notes/tuning-test.md` §3](../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t)).
4. **The palindrome.** "Reciprocity acts on the wedge sector as frame exchange, forcing βₙ = β₄₋ₙ" ([the palindrome](../gravity/palindromic-branch/palindrome.md)), which yields the identity below.

### Predictions not previously posed: rows 3 and 11

Two rows of #11's predictions table have "(not previously posed)" in the column for the standard expectation ([#11 §13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)). [Row 3, the island discriminant](../predictions/island-discriminant.md): the shape of the knee in dark matter's self-interaction cross-section, "sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave". [Row 11, dark-sector microstructure](../predictions/dark-sector-microstructure.md): "Particles vs condensate, separable via rows 1–3 + coherence signatures". Both are diagnostics rather than kill conditions: they would tell the program's options apart, not refute it.

### An unsolicited identity (§7.3)

The palindrome was imposed by [reciprocity](../phase-space/reciprocity/born-reciprocity.md), not chosen to cancel anything, and the cancellation followed from it together with the requirement of a flat vacuum, itself one condition on the βₙ (flag 6 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md)). At the aligned point, where the two frames coincide, the wedge potential's value V(1) and its tadpole T, the coefficient of its term linear in a small departure from that point, are fixed combinations of the coefficients βₙ. Under the palindrome one is exactly twice the other, while a flat vacuum requires the potential's contribution to the metric's field equation to vanish, which reads V(1) = T ([`notes/beta-coefficients.md` §2](../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines), "[D — rigorous, four lines]"):

```text
βₙ = β₄₋ₙ:     V(1) ∝ 2β₀ + 8β₁ + 6β₂,     T = β₀ + 4β₁ + 3β₂     ⇒     V(1) = 2T
flat aligned vacuum:     V(1) = T     ⇒     T = 0   and   V(1) = 0
```

[#11 §7.3](../papers/broken-born-checkpoint-v2.md#73-palindrome-and-the-vacuum-energy-identity-dv) tags it [D][V]: "V(1) = 2T exactly (integer identity: [2,8,6] = 2·[1,4,3])", so the wedge sector "contributes zero cosmological constant, by symmetry" (on "by symmetry", see flag 6 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md)). The battery checks the integers: "T5 V(1) - 2T = [0,0,0]  [V1=[2, 8, 6] T=[1, 4, 3]]" ([`verify/battery.py`](../../verify/battery.py), test T5). Its scope, as #11 states it: it "does not by itself address matter-loop vacuum energy, the 'old' cosmological-constant problem" ([the vacuum-energy identity](../gravity/palindromic-branch/vacuum-energy-identity.md)). Whether it is new is the open comparison below.

### One over-constraint in the dark-energy sector

The dark-energy field τ has "two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint" ([#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology)), where w₀ is the value of w today and wₐ measures how fast w has changed as the universe expanded (a negative wₐ means that w has been rising; [the CPL form](../cosmology/dark-energy/cpl-parametrization.md#what-w-and-wₐ-mean)). Once two of the observables are measured, the third is predicted ([the dark-energy over-constraint](../cosmology/dark-energy/over-constraint.md)). The third observable, the turnaround time, assumes in the documents' account that τ's potential goes negative, a point they leave unresolved (see flag 27 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md); [Open: the sign of V(τ)](../cosmology/dark-energy/potential-sign.md)). The closed-universe note of 2026-10-27, not reviewed, finds that with the potential as written only a closed universe turns around; there t_turn ∝ |Ω_k|^{−3/2} at fixed (w₀, wₐ), so the curvature is a third input and the over-constraint moves to (f, τᵢ, Ω_k) rather than vanishing, and since the data bound t_turn only from below, the turnaround time cannot test the count (flag 27 addendum; flag 46; [a closed Comatter universe](../cosmology/scale-factor-duality/closed-universe.md#the-over-constraint-moves-dv)).

### The charge-lattice unification

[#11 §11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) [D — structural; math T] identifies the choice of which charges count as electric with a choice of [Lagrangian polarization](../phase-space/reciprocity/lagrangian-polarizations.md) of the charge lattice, and notes that [S-duality](../electric-magnetic-duality/s-duality.md) is generated by the same matrix [[0,1],[−1,0]] as reciprocity ([the symplectic charge lattice](../electric-magnetic-duality/symplectic-charge-lattice.md)). The new question it generates is [#11 §14 item 8](../papers/broken-born-checkpoint-v2.md#14-open-problems), whether the two polarizations are parts of one modular structure [O] ([Open: one modular structure for both polarizations](../electric-magnetic-duality/unified-modular-structure.md)). The item also asks for a test of P.R.'s [magnetic-mirror conjecture](../electric-magnetic-duality/magnetic-identification.md) ([§11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)), that each electrically charged particle has a magnetically charged analog in the momentum polarization.

## Degeneration risks

[#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment): "tunable wave-island collective sector (quarantined); gate tail not yet forced; the novelty demotion of §7.4 as a standing caution", joined by "the failure of #14's soliton model (§12) and the §5 re-attribution of the compatibility theorem; DESI DR2's phantom crossing against §10's strict w ≥ −1." DESI DR2 is Data Release 2 of the [Dark Energy Spectroscopic Instrument](../cosmology/dark-energy/desi.md).

- **The tunable wave-island sector.** On the wave side of the clumping problem, with the coupling left free, velocity streams are "tunable across ~10 orders: optional, never required" ([#11 §9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)). Streams that are permitted but not required are no longer a prediction, as the calc note records: "on this branch the granularity prediction is no longer a novel requirement of the program, only an option — a degeneration flag" ([`notes/wave-island.md`](../../notes/wave-island.md), 'What pins g?'); the granularity prediction is old row 3, [under review](../dark-matter/momentum-clumping/velocity-granularity.md). The branch is quarantined ([Scenario B: tunable streams](../dark-matter/momentum-clumping/wave-island/scenario-b.md)).
- **The gate tail.** The dark-matter self-interaction has a "robust knee at v\*", but its "tail (Gaussian vs rational) diagnoses the vertex completion" ([#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)), and no derivation yet fixes it ([Open: the gate shape](../dark-matter/conjugate-matter/gate-shape.md)).
- **Three demotions.** In each, a result the program had claimed as its own was downgraded, withdrawn or credited to earlier work:
  - §7.4: a live literature search found the interchange-symmetric bimetric potentials charted, with the partially massless (PM) point inside the palindromic branch, so the novelty of the vacuum-energy identity was "downgraded from 'likely standalone result' to 'requires detailed comparison with the PM and exchange-symmetric literature'" ([Open: the partially-massless comparison](../gravity/palindromic-branch/pm-comparison.md));
  - §12: #14's model of the third dark-matter candidate, superheavy solitons described with ordinary kinematics, failed after [round 3](../method/review/round-3/_index.md) found its abundance misnormalized ([Under review: the Kibble normalization](../dark-matter/candidates/soliton-candidate/kibble-normalization.md)); the v3 benchmark of 3×10¹³ GeV "is overproduced by 2.1×10³–1.2×10⁴ [V]" (checked in [`verify/soliton_obituary.py`](../../verify/soliton_obituary.py), see [the soliton-obituary script](../method/verification/soliton-obituary-script.md); [Obituary: #14's superheavy-soliton model](../dark-matter/candidates/soliton-candidate/obituary.md)). The candidate it modeled, conjugate monopoles localized in momentum, is P.R.'s open conjecture ([Conjecture: magnetic monopoles abundant in momentum space](../dark-matter/candidates/momentum-space-monopoles.md));
  - §5: the compatibility theorem, presented in v2.0 as derived here, is the Born-geometry statement of Freidel, Leigh and Minic, and is tagged [T][V] ([the compatibility theorem](../phase-space/born-geometry/compatibility-theorem.md)).
- **DESI DR2 against w ≥ −1.** The framework requires [w ≥ −1](../cosmology/dark-energy/no-phantom-bound.md) strictly, while DR2 reports that in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4" [21S] (z is the [redshift](../cosmology/scale-factor-duality/redshift.md), the stretching of light by the expansion of the universe since the light was emitted; larger z means earlier). [#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology) records that the framework survives on two points: non-phantom [quintessence](../cosmology/dark-energy/quintessence.md) fits remain compatible [19S], and w(z) is inferred from distances rather than observed ([DESI DR2's phantom crossing](../cosmology/dark-energy/desi-dr2-phantom-crossing.md)). The root [`CLAUDE.md`](../../CLAUDE.md): "The dark-energy sector is under real pressure ahead of DR3", DESI's next data release, Data Release 3.

## Falsification exposure

"genuine and near-term (rows 1, 4, 7)" ([#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment)). The three rows of [#11 §13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions), with their kill conditions:

| Row | The program requires | Killed by |
| --- | --- | --- |
| [1: the knee](../predictions/self-interaction-knee.md) | a knee in σ_T(v) at v\* ~ 10² km/s, and zero self-interaction signal in clusters for particle χ | robust self-interaction at v ≫ v\*, or the knee excluded in the 150–400 km/s band |
| [4: dark energy](../predictions/dark-energy-drift.md) | [thawing](../cosmology/dark-energy/thawing-and-freezing.md), w₀ > −1, wₐ < 0, never phantom; the drift persists in DESI Data Release 3 | a constant w = −1 in Data Release 3 or later (kills τ-sector); a robust intrinsic w < −1 (kills outright) |
| [7: direct detection](../predictions/direct-detection-null.md) | a permanent null, since "both dark-sector candidates" are decoupled from the Standard Model under strict [P4](postulates/p4-polarized-matter.md), a wording that names two while §12 lists three (flag 63 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md), pending, proposes wording for three) | any confirmed non-gravitational coupling of dark matter to the Standard Model |

[The handoff](../history/documents/handoff.md) names DESI's Data Release 3 as the external clock, "three-year data, expected late 2026" ([`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen); on "three-year data", see flag 26 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md); the date is the handoff's own and is unverified, [the data releases](../cosmology/dark-energy/desi.md#the-data-releases)).

## What the program has produced

[#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment)'s plain-language passage counts the output: "one observation that stands regardless of its fate (the symplectic partner of the graviton is another graviton — why string theory's doubling works and Born's stalled), one identity awaiting a novelty verdict, one new experimental question (the knee-shape discriminant), one structural unification (polarization of phase space and of charge space as one move), and a three-way question about dark matter's nature with named discriminators; #14's superheavy-knot model of the third option was tested and failed, and the option itself is P.R.'s open conjecture." The entries are [the symplectic partner of the graviton](../gravity/momentum-graviton/symplectic-partner.md), the vacuum-energy identity, row 3, the charge-lattice identification, whose bridge between the two dualities is a published remark (flag 67, pending), and [the dark-sector candidates](../dark-matter/candidates/_index.md) with row 11, which names two of the three (flag 63, pending). The same passage records that the founding image, dark matter clumping in velocity, "failed the program's own calculations for particle dark matter and, where it would have been mandatory for wave dark matter, the test of the faintest dwarf galaxies; P.R. holds it open as his conjecture" ([Conjecture: velocity clumping, the founding image](../dark-matter/momentum-clumping/founding-image.md)).

## The verdict, and what "theory" waits on

"That is a live research program; the word 'theory' still waits on items 1–3 above" ([#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment)). The three items of [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems), all open [O]:

1. [the first-principles reduction of the frame-tier wedge sector](../gravity/tuning-test/wedge-reduction.md) from the [geometric action](../gravity/tuning-test/geometric-action.md) ("class selected, not derived");
2. [the partially-massless comparison](../gravity/palindromic-branch/pm-comparison.md), the novelty audit of the vacuum-energy identity;
3. [the Lorentzian dressing](../phase-space/born-geometry/lorentzian-dressing.md) of the "Euclidean-rigorous skeleton".

The threshold has moved twice. The field-equation note on the classification of X made "theory" depend on the tuning test: "Pass ⇒ the geometric core stands and 'theory' becomes the defensible word" ([`notes/x-classification.md` §5](../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk)). After the [conditional pass](../gravity/tuning-test/conditional-pass.md), the v1 paper said "The word 'theory' awaits items 1–2 of §10", the wedge reduction and the Lorentzian dressing ([#9 §11](../../notes/broken-born-program-v1.md#11-assessment)). #11 inserts the partially-massless comparison, the open item that [§7.4](../papers/broken-born-checkpoint-v2.md#74-literature-position-updated-by-this-sessions-search--honesty-upgrade)'s novelty downgrade created. Of the three, only the comparison is in the current work queue, where it comes first (root [`CLAUDE.md`](../../CLAUDE.md)).

## Later results

- **The handoff's status line predates the reviews below.** [`HANDOFF.md` §1](../../HANDOFF.md#1-what-this-project-is)'s "Honest status" says "Three blind AI reviews returned verdict B ('flawed but salvageable')". Its own [§6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) records two completed rounds, with verdicts B and "B near B/C", and a third that was incomplete at the handoff; the handoff does not reconcile the two.
- **[Round 3](../method/review/round-3/_index.md)** returned verdict C on the soliton manuscript #14 v3, which was withdrawn ([`review/round3-adjudication.md`](../../review/round3-adjudication.md), 'Verdict').
- **[Round 4](../method/review/round-4.md)** returned verdict B on the [toy-model note](../symmetry-breaking/toy-models/_index.md), whose version 2 applies the accepted revisions ([`review/round4-adjudication.md`](../../review/round4-adjudication.md), 'Verdict'), except revision 4's comparison with an exactly solved related model, which it has not carried out (flag 42 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md)).
- **[Round 5](../method/review/round-5.md)** returned verdict B on [the phase-space-diameter note](../cosmology/scale-factor-duality/phase-space-diameter.md) ([`review/round5-adjudication.md`](../../review/round5-adjudication.md), 'Verdict'). See [blind review](../method/review/_index.md).
- **The closed universe.** [`notes/closed-universe.md`](../../notes/closed-universe.md) (2026-10-27, not reviewed) finds that with τ's potential as written only a closed universe turns around, and that in the program's model class the data disfavour closure at about 2σ, in one agent's background fit without supernovae ([what the data say](../cosmology/scale-factor-duality/closed-universe.md#what-the-data-say)).
- **The gate's mechanism.** [`notes/gate-mechanism.md`](../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging [#11 §7](../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce [the velocity gate](../dark-matter/conjugate-matter/velocity-gate.md) on dark matter's self-interaction. Flag 55 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) (pending) proposes [P] for the gate and its momentum width μ and [O] for the mechanism ([what flag 55 proposes](../dark-matter/conjugate-matter/gate-mechanism.md#what-flag-55-proposes)).

## Superseded: the v1 assessment

The v1 paper's assessment ([#9 §11](../../notes/broken-born-program-v1.md#11-assessment)) is the earlier form of this page's subject, superseded by [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment). Its criterion: "Programs that keep predicting novel facts are progressive; programs that only redescribe are degenerating." It differed from the current assessment in four places:

- **The hard core** was "intact and sharpened by the P2 → P2′ correction": one sharpening, where #11 counts two.
- **Standalone results.** v1 claimed "at least two results that stand on their own regardless of its fate", the symplectic-partner observation and "the palindrome theorem cancelling the symmetric-bimetric vacuum energy". After the §7.4 literature search #11 counts one observation, plus "one identity awaiting a novelty verdict".
- **Progressive signs** included "novel predictions not previously posed (island discriminant; knee shape; even-eigenstate masslessness as a bimetric-parity statement); an unsolicited theorem (Λ_wedge = 0)". #11 renames the theorem an identity and adds the charge-lattice unification.
- **Degeneration risks** were two, the tunable wave-island sector and the unforced gate tail. #11 adds the three demotions and DESI DR2.

v1's verdict: "The word 'theory' awaits items 1–2 of §10; the phrase 'research program,' used precisely, is earned now."

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §15](../papers/broken-born-checkpoint-v2.md#15-assessment) — the assessment; [§14 items 1–3](../papers/broken-born-checkpoint-v2.md#14-open-problems) — what "theory" waits on; [§14 item 8](../papers/broken-born-checkpoint-v2.md#14-open-problems) and [§11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) — the question the charge-lattice unification generates, with the magnetic-mirror conjecture; [§1](../papers/broken-born-checkpoint-v2.md#1-two-abstracts) — the chain of structural results; [§2](../papers/broken-born-checkpoint-v2.md#2-methodological-preface-provenance-and-verification) — the tiers and the reliability of negative results; [§7](../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) — the forcing chain, the tuning test, the identity and the novelty downgrade; [§8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)–[§13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the gate tail, the wave-island sector, the over-constraint, the charge-lattice unification, the three candidates and #14's failed model, and the predictions table
- [`HANDOFF.md` §1](../../HANDOFF.md#1-what-this-project-is) — "a Lakatosian research program, not a theory", the four consistency tests and the pre-round-3 "Honest status"; [§2](../../HANDOFF.md#2-scientific-state-one-screen) — the external clock; [§6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — the review rounds as of the handoff
- root [`CLAUDE.md`](../../CLAUDE.md) 'Since the handoff' — the pressure on the dark-energy sector and the current queue
- [`notes/tuning-test.md` §5](../../notes/tuning-test.md#5-status-of-the-field-equation-problem) — forced convergence as first stated, with three tests; [§3](../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — the frame tier as a structural argument; [`notes/x-classification.md` §5](../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — the first threshold for "theory"; [`notes/beta-coefficients.md` §2](../../notes/beta-coefficients.md#2-the-vacuum-energy-theorem-d--rigorous-four-lines) — the four-line derivation of V(1) = 2T
- [`notes/wave-island.md`](../../notes/wave-island.md) 'What pins g?' — the degeneration flag on the wave island
- [`notes/broken-born-program-v1.md` §10](../../notes/broken-born-program-v1.md#10-open-problems)–[§11](../../notes/broken-born-program-v1.md#11-assessment) — the v1 open problems and assessment, superseded by [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment)
- [`review/round3-adjudication.md`](../../review/round3-adjudication.md) 'Verdict', [`review/round4-adjudication.md`](../../review/round4-adjudication.md) 'Verdict' and [`review/round5-adjudication.md`](../../review/round5-adjudication.md) 'Verdict' — the review verdicts since the handoff
- [`verify/battery.py`](../../verify/battery.py) T4, T5, T7 — the machine checks of the tuning test and the integer identity
- [`verify/soliton_obituary.py`](../../verify/soliton_obituary.py) — the [V] numbers of #14's failed model
- [`notes/closed-universe.md` §2](../../notes/closed-universe.md#2-the-premise-and-the-turnaround-it-buys); [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 27's addendum and item 46 — the closed turnaround, the data on closure and the over-constraint moved to Ω_k
- [`notes/gate-mechanism.md` §2](../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate), [§5](../../notes/gate-mechanism.md#5-what-follows-for-the-record); [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 55 — exchanging X cannot produce the gate, and the proposed tags; pending
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 63 — rows 7 and 11 worded for two candidates; pending
- [`notes/literature-check.md` §5](../../notes/literature-check.md#5-the-magnetic-mirror-c4-partly-anticipated), [§6](../../notes/literature-check.md#6-conjugate-collapse-drives-our-acceleration-c5-partly-anticipated); [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) items 66, 67 — the w-dictionary as scale-factor duality with sources, as a map of fluid variables, and the bridge between the two dualities as a published remark; pending
