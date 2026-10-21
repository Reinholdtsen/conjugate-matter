---
title: "Assessment: a live research program"
weight: 70
status: record
description: "The checkpoint's Lakatosian self-assessment: the hard core intact and twice sharpened, forced convergence and the other progressive signs, the degeneration risks, and near-term falsification exposure."
sources:
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md §14 items 1–3"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §8–§13"
  - "HANDOFF.md §1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/debt1a-iii-tuning-test.md §3, §5"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/debt3b-wave-island.md 'What pins g?'"
  - "notes/broken-born-program-v1.md §10–§11"
  - "review/round3-adjudication.md 'Verdict'"
  - "review/round4-adjudication.md 'Verdict'"
  - "verify/battery.py T4, T5, T7"
---

*The assessment is the checkpoint's own judgement of where the program stands, written in the terms of Imre Lakatos's account of research programmes: a hard core that is kept fixed, auxiliary claims that may be revised, and the question of whether the program keeps producing new predictions (progressive) or only accommodates its failures (degenerating). Checkpoint #11 v2.2 finds the hard core intact and sharpened twice by corrections the program's own mathematics forced. It lists the signs of progress and the risks of degeneration side by side, it names three predictions that observations could falsify soon, and it notes that the current dark-energy data already lean against one of them. Its verdict is that this is a live research program, and that the word "theory" waits on three open problems.*

**Status:** Record — untagged: a self-assessment, not a derivation. It is #11 §15, as amended in v2.1 after the round-3 review, and it supersedes the v1 assessment (#9 §11). The numbers it rests on are tagged and checked in the sections they come from.

## What the assessment is

Lakatos judged a body of research over time rather than one hypothesis at a time. A programme keeps a hard core fixed and revises the auxiliary claims around it; it is progressive while its revisions lead to new predictions, and degenerating while its revisions only absorb failures after the fact ([Lakatos's methodology](/wiki/method/lakatosian-methodology)). #11 §15 sorts the program's record under four headings in those terms: the hard core, progressive signs, degeneration risks and falsification exposure. The status line the project gives itself follows from it: "a Lakatosian research program, not a theory" (`HANDOFF.md` §1; root `CLAUDE.md`).

The assessment sits beside a calibration in #11's methodological preface. Novel structural claims (Tier 3) carry an "honest prior per claim ~50–80% pending expert review", and "Negative results (§9, §7.1, and the §12 obituary) are the most reliable Tier-3 items, since the program's incentive gradient ran against them" (#11 §2; [claim tiers and selection bias](/wiki/method/claim-tiers)).

## The hard core: intact, twice sharpened

"**hard core** (spontaneously broken reciprocity, ω-only rigidity) intact, twice sharpened by forced corrections (P2′; the w-dictionary)" (#11 §15; [the hard core](/wiki/program/hard-core)). Both corrections came from the program's own derivations rather than from data:

- **P2′.** The first rigidity postulate fixed both the symplectic form ω and the neutral metric η. With both fixed, the program reduced to general relativity plus one model of self-interacting dark matter, with no dark-energy field. The [nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) [D] showed that the program has content only if η is emergent, which forced [P2′](/wiki/program/postulates/p2-prime): only ω is rigid.
- **The w-dictionary.** An early heuristic rule for how energy in the conjugate description acts on our expansion, w_eff = −2 − w̃, was replaced by the derived rule w_eff = −w̃ [D — corrected en route]: "the constraint's Jacobian changed the answer — rigor's job" (#11 §10; [the duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary)).

## Progressive signs

#11 §15: "forced convergence onto consistency islands; predictions not previously posed (rows 3, 11); an unsolicited identity (§7.3); one over-constraint (DE sector); the §11.3 unification generating new questions." DE is dark energy.

### Forced convergence onto consistency islands

The claim is that each structural test that could have killed the program's geometric sector instead forced it onto the one consistent structure available at that point. A consistency island, in the Debt-1 note's usage, is "the unique known consistent structure" at such a junction; the term is unrelated to the particle and wave islands of Debt 3. #11 §15 counts "four consecutive consistency tests" without naming them. The documents give the chain in three versions:

- The Debt-1 note that first made the point counted three: "three structural tests in a row (multi-graviton no-go, signature obstruction, tuning test) could each have killed the geometric sector outright; each instead forced it into the unique known consistent structure at that junction. Repeated forced convergence onto consistency islands is the opposite of degeneration" (`notes/debt1a-iii-tuning-test.md` §5).
- The v1 assessment named four: "no-go → Higgs → HR class → palindrome" (#9 §11), HR being Hassan–Rosen.
- #11's technical abstract lists "a chain of structural results (a compatibility theorem [T][V]; the multi-graviton no-go [8†]; a signature obstruction; an explicit tuning test [V])" that forces the momentum graviton X to be a massive spin-2 field (#11 §1).

The count of four is #11's, as in `HANDOFF.md` §1, and #11 governs. The steps of the v1 chain, as #11 §7 records them:

1. **The no-go.** X, the symmetric partner of the metric, transforms as a second graviton, and two interacting massless gravitons are inconsistent, so "Massless X is excluded by the multi-graviton no-go [8†]" ([the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go)); an ungauged X is excluded by Lorentz signature, the "signature obstruction".
2. **The Higgs mechanism.** "The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive" ([the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).
3. **The Hassan–Rosen class.** "The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†]", dRGT being de Rham–Gabadadze–Tolley. The [tuning test](/wiki/gravity/tuning-test), tagged [D][V] in #11 §7.2, found the program's natural metric-tier mass terms outside that structure in two independent ways, each checked numerically: a linearized mass term whose limit, 66.58 for the battery's test matrix, differs from the Fierz–Pauli form's 63.72 (test T4), and a nonlinear term outside the allowed span, with rms residual 3.29 (test T7; [the verification battery](/wiki/method/verification/battery)). The frame-tier couplings belong to the Hinterbichler–Rosen class, "ghost-free by construction", which the calc note tags "[D — structural, resting on T]" (`notes/debt1a-iii-tuning-test.md` §3).
4. **The palindrome.** "Reciprocity acts on the wedge sector as frame exchange, forcing βₙ = β₄₋ₙ" ([the palindrome](/wiki/gravity/palindromic-branch/palindrome)), which yields the identity below.

### Predictions not previously posed: rows 3 and 11

Two rows of #11's predictions table have "(not previously posed)" in the column for the standard expectation (#11 §13). [Row 3, the island discriminant](/wiki/predictions/island-discriminant): the shape of the knee in dark matter's self-interaction cross-section, "sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave". [Row 11, dark-sector microstructure](/wiki/predictions/dark-sector-microstructure): "Particles vs condensate, separable via rows 1–3 + coherence signatures". Both are diagnostics rather than kill conditions: they would tell the program's options apart, not refute it.

### An unsolicited identity (§7.3)

The palindrome was imposed by reciprocity, not chosen to cancel anything, and the cancellation followed from it. At the aligned point, where the two frames coincide, the wedge potential's value V(1) and its tadpole T, the coefficient of its term linear in a small departure from that point, are fixed combinations of the coefficients βₙ. Under the palindrome one is exactly twice the other, while a flat vacuum requires the potential's contribution to the metric's field equation to vanish, which reads V(1) = T (`notes/debt1a-iv-beta-coefficients.md` §2, "[D — rigorous, four lines]"):

```text
βₙ = β₄₋ₙ:     V(1) ∝ 2β₀ + 8β₁ + 6β₂,     T = β₀ + 4β₁ + 3β₂     ⇒     V(1) = 2T
flat aligned vacuum:     V(1) = T     ⇒     T = 0   and   V(1) = 0
```

#11 §7.3 tags it [D][V]: "V(1) = 2T exactly (integer identity: [2,8,6] = 2·[1,4,3])", so the wedge sector "contributes zero cosmological constant, by symmetry". The battery checks the integers: "T5 V(1) - 2T = [0,0,0]  [V1=[2, 8, 6] T=[1, 4, 3]]" (`verify/battery.py`, test T5). Its scope, as #11 states it: it "does not by itself address matter-loop vacuum energy, the 'old' cosmological-constant problem" ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)). Whether it is new is the open comparison below.

### One over-constraint in the dark-energy sector

The dark-energy field τ has "two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint" (#11 §10): once two of the observables are measured, the third is predicted ([the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)). The third observable, the turnaround time, assumes that τ's potential goes negative, a point the documents leave unresolved ([Open: the sign of V(τ)](/wiki/cosmology/dark-energy/potential-sign)).

### The charge-lattice unification

#11 §11.3 [D — structural; math T] identifies the choice of which charges count as electric with a choice of Lagrangian polarization of the charge lattice, generated by the same matrix [[0,1],[−1,0]] as reciprocity ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). The new question it generates is #11 §14 item 8, whether the two polarizations are parts of one modular structure [O] ([Open: one modular structure for both polarizations](/wiki/electric-magnetic-duality/unified-modular-structure)).

## Degeneration risks

#11 §15: "tunable wave-island collective sector (quarantined); gate tail not yet forced; the novelty demotion of §7.4 as a standing caution, joined in v2.1 by the §12 soliton obituary and the §5 re-attribution of the compatibility theorem; DESI DR2's phantom crossing against §10's strict w ≥ −1." DESI DR2 is Data Release 2 of the Dark Energy Spectroscopic Instrument.

- **The tunable wave-island sector.** On the wave side of Debt 3, with the coupling left free, velocity streams are "tunable across ~10 orders: optional, never required" (#11 §9). Streams that are permitted but not required are no longer a prediction, and the calc note recorded this when it found them: "on this branch the granularity prediction is no longer a novel requirement of the program, only an option — a degeneration flag" (`notes/debt3b-wave-island.md`, 'What pins g?'). The branch is quarantined ([Scenario B: tunable streams](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b)).
- **The gate tail.** The dark-matter self-interaction has a "robust knee at v\*", but its "tail (Gaussian vs rational) diagnoses the vertex completion" (#11 §8), and no derivation yet fixes it ([Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)).
- **Three demotions.** In each, a result the program had claimed as its own was downgraded, withdrawn or credited to earlier work:
  - §7.4: a live literature search found the interchange-symmetric bimetric potentials charted, with the partially massless (PM) point inside the palindromic branch, so the novelty of the vacuum-energy identity was "downgraded from 'likely standalone result' to 'requires detailed comparison with the PM and exchange-symmetric literature'" ([Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison));
  - §12: the superheavy soliton candidate was retired after round 3 found its abundance misnormalized; the v3 benchmark of 3×10¹³ GeV "is overproduced by 2.1×10³–1.2×10⁴ [V]" ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary));
  - §5: the compatibility theorem, presented in v2.0 as derived here, is the Born-geometry statement of Freidel, Leigh and Minic, and is now tagged [T][V] ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)).
- **DESI DR2 against w ≥ −1.** The framework requires w ≥ −1 strictly, while DR2 reports that in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4" [21S]. #11 §10 records that the framework survives on two points: non-phantom quintessence fits remain compatible [19S], and w(z) is inferred from distances rather than observed ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)). The root `CLAUDE.md`: "The dark-energy sector is under real pressure ahead of DR3", DESI's next data release, Data Release 3.

## Falsification exposure

"genuine and near-term (rows 1, 4, 7)" (#11 §15). The three rows of #11 §13, with their kill conditions:

| Row | The program requires | Killed by |
| --- | --- | --- |
| [1: the knee](/wiki/predictions/self-interaction-knee) | a knee in σ_T(v) at v\* ~ 10² km/s, and zero self-interaction signal in clusters for particle χ | robust self-interaction at v ≫ v\*, or the knee excluded in the 150–400 km/s band |
| [4: dark energy](/wiki/predictions/dark-energy-drift) | thawing, w₀ > −1, wₐ < 0, never phantom; the drift persists in DESI Data Release 3 | a constant w = −1 in Data Release 3 or later (kills the τ sector); a robust intrinsic w < −1 (kills the framework outright) |
| [7: direct detection](/wiki/predictions/direct-detection-null) | a permanent null, since both dark-sector candidates are decoupled from the Standard Model under strict P4 | any confirmed non-gravitational coupling of dark matter to the Standard Model |

The handoff names DESI's Data Release 3 as the external clock, "three-year data, expected late 2026" (`HANDOFF.md` §2).

## What the program has produced

#11 §15's plain-language passage counts the output: "one observation that stands regardless of its fate (the symplectic partner of the graviton is another graviton — why string theory's doubling works and Born's stalled), one identity awaiting a novelty verdict, one new experimental question (the knee-shape discriminant), one structural unification (polarization of phase space and of charge space as one move), and a two-way question about dark matter's nature with named discriminators; a third option, superheavy knots, was tested and retired." The entries are [the symplectic partner of the graviton](/wiki/gravity/momentum-graviton/symplectic-partner), the vacuum-energy identity, row 3, the charge-lattice identification, and [the two dark-sector candidates](/wiki/dark-matter/candidates) with row 11. The same passage records that the founding image, dark matter clumping in velocity, was killed by the program's own calculations ([Obituary: velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image)).

## The verdict, and what "theory" waits on

"That is a live research program; the word 'theory' still waits on items 1–3 above" (#11 §15). The three items of #11 §14, all open [O]:

1. [the first-principles reduction of the frame-tier wedge sector](/wiki/gravity/tuning-test/wedge-reduction) from the geometric action ("class selected, not derived");
2. [the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison), the novelty audit of the vacuum-energy identity;
3. [the Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing) of the "Euclidean-rigorous skeleton".

The threshold has moved twice. The Debt-1 note on the classification of X made "theory" depend on the tuning test: "Pass ⇒ the geometric core stands and 'theory' becomes the defensible word" (`notes/debt1a-ii-X-classification.md` §5). After the conditional pass, the v1 paper said "The word 'theory' awaits items 1–2 of §10", the wedge reduction and the Lorentzian dressing (#9 §11). #11 inserts the partially-massless comparison, the open item that §7.4's novelty downgrade created. Of the three, only the comparison is in the current work queue, where it comes first (root `CLAUDE.md`).

## The record since the handoff

- **The handoff's status line predates the last two reviews.** `HANDOFF.md` §1's "Honest status" says "Three blind AI reviews returned verdict B ('flawed but salvageable')". Its own §6 records two completed rounds, with verdicts B and "B near B/C", and a third that was incomplete at the handoff; the handoff does not reconcile the two.
- **Round 3** returned verdict C on the soliton manuscript #14 v3, which was withdrawn (`review/round3-adjudication.md`, 'Verdict').
- **Round 4** returned verdict B on the toy-model note, whose version 2 applies the accepted revisions (`review/round4-adjudication.md`, 'Verdict'). See [blind review](/wiki/method/review).
- **#11 §15 itself** was amended in v2.1 (commit e1c1f67): the soliton obituary, the re-attribution of the compatibility theorem and DESI DR2 joined the degeneration risks; the plain-language count's "three-way question about dark matter's nature" became the two-way question with the third option retired; and the sentence that the current DESI release "already leans against its dark-energy prediction" was added.

## Superseded: the v1 assessment

The v1 paper's assessment (#9 §11) is the earlier form of this page's subject, superseded by #11 §15. Its criterion: "Programs that keep predicting novel facts are progressive; programs that only redescribe are degenerating." It differed from the current assessment in four places:

- **The hard core** was "intact and sharpened by the P2 → P2′ correction": one sharpening, where #11 counts two.
- **Standalone results.** v1 claimed "at least two results that stand on their own regardless of its fate", the symplectic-partner observation and "the palindrome theorem cancelling the symmetric-bimetric vacuum energy". After the §7.4 literature search #11 counts one observation, plus "one identity awaiting a novelty verdict".
- **Progressive signs** included "novel predictions not previously posed (island discriminant; knee shape; even-eigenstate masslessness as a bimetric-parity statement); an unsolicited theorem (Λ_wedge = 0)". #11 renames the theorem an identity and adds the charge-lattice unification.
- **Degeneration risks** were two, the tunable wave-island sector and the unforced gate tail. #11 adds the three demotions and DESI DR2.

v1's verdict: "The word 'theory' awaits items 1–2 of §10; the phrase 'research program,' used precisely, is earned now."

## Sources

- `papers/broken-born-checkpoint-v2.md` §15 — the assessment, current through v2.2; §14 items 1–3 — what "theory" waits on; §1 — the chain of structural results; §2 — the tiers and the reliability of negative results; §7 — the forcing chain, the tuning test, the identity and the novelty downgrade; §8–§13 — the gate tail, the wave-island sector, the over-constraint, the charge-lattice unification, the soliton obituary and the predictions table
- `HANDOFF.md` §1 — "a Lakatosian research program, not a theory", the four consistency tests and the pre-round-3 "Honest status"; §2 — the external clock; §6 — the review rounds as of the handoff
- root `CLAUDE.md` 'Since the handoff' — the pressure on the dark-energy sector and the current queue
- `notes/debt1a-iii-tuning-test.md` §5 — forced convergence as first stated, with three tests; §3 — the frame tier as a structural argument; `notes/debt1a-ii-X-classification.md` §5 — the first threshold for "theory"; `notes/debt1a-iv-beta-coefficients.md` §2 — the four-line derivation of V(1) = 2T
- `notes/debt3b-wave-island.md` 'What pins g?' — the degeneration flag on the wave island
- `notes/broken-born-program-v1.md` §10–§11 — the v1 open problems and assessment, superseded by #11 §15
- `review/round3-adjudication.md` 'Verdict' and `review/round4-adjudication.md` 'Verdict' — the review verdicts since the handoff
- `verify/battery.py` T4, T5, T7 — the machine checks of the tuning test and the integer identity
