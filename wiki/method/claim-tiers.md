---
title: "Claim tiers and selection bias"
weight: 40
status: method
description: "Tier 1 machine-checked algebra, Tier 2 literature, Tier 3 novel structural physics at a stated prior of ~50–80% per claim; negative results as the most reliable Tier-3 items; and the selection-versus-derivation bias, acknowledged where it operates."
sources:
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §7.1–§7.4"
  - "papers/broken-born-checkpoint-v2.md §14 item 1"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-program-v1.md §10"
  - "notes/debt1a-iii-tuning-test.md §3, §5"
  - "notes/debt1a-ii-X-classification.md §3"
  - "HANDOFF.md §1"
  - "HANDOFF.md §5"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round4-adjudication.md 'Rulings'"
  - "review/wiki-build-flags.md items 7, 36"
  - "verify/battery.py"
---

*The claim tiers are [checkpoint #11](/wiki/history/documents/checkpoint)'s ranking of its own statements by how much trust each deserves. Tier 1 is explicit algebra checked by machine; Tier 2 is established literature, correct at the level of well-worn results; Tier 3 is the program's new structural physics, which #11 rates as plausible, at a prior of ~50–80% per claim pending expert review. Within Tier 3, #11 counts its negative results as the most reliable items. Alongside the tiers it names one specific risk, the selection-versus-derivation bias, which the wiki reads as presenting a structure that was chosen from the known consistent options as though the program's premises had forced it. The tiers and the bias check are part of #11's methodological preface, §2.*

**Status:** Method — Tier 1 is the [V] tier; the tiers themselves carry no tag — #11 §2 ("Methodological preface: provenance and verification"); Tier 1's tests run in the gate (`verify/battery.py`; [the verification battery](/wiki/method/verification/battery)).

## Tags and tiers

[Provenance tags](/wiki/method/provenance-tags) say where a claim comes from: derived here, taken from the literature, postulated, open, or machine-checked. The tiers answer a different question, how far a claim of each kind can be trusted. #11 §2 sets them out in one paragraph that begins "Claims are stratified." The sections below take the tiers in order, from most to least secure.

## Tier 1: explicit algebra

"Tier 1 (explicit algebra): verified this session by an independent numerical/exact-integer battery — seven tests covering the compatibility theorem (both directions, including the proof's individual block identities), the Siegel parametrization (I[Z]² = −1, H > 0, det H = 1 across the whole family), the anticommutator block structure, the linearized potential (Tr(S²)/ε² → 4Tr(h²) to six digits, visibly ≠ the Fierz–Pauli form), the palindrome identity as exact integers, the binomial linearization coefficients, and the exclusion of p₄ from the linear span of elementary symmetric polynomials (rms residual 3.29). All seven passed [V]." (#11 §2).

The seven tests are T1–T7 of `verify/battery.py`, which [the gate](/wiki/method/verification/the-gate) runs before any work counts as finished. Its current output includes "T4 parity: 66.58 vs 63.72 as quoted" (on where these two figures are printed, see flag 36 in `review/wiki-build-flags.md`), the linearized potential's limit against the Fierz–Pauli form for the test matrix, "T5 V(1) - 2T = [0,0,0]", and "T7 p4 outside span of e_n (rms residual nonzero)  [rms=3.2853]". The tests and what each establishes are on [The verification battery T1–T7](/wiki/method/verification/battery).

#11 §2 defines Tier 1 by this battery. Later machine-checked items, the numbers of the soliton obituary (§12, `verify/soliton_obituary.py`; [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)) and the toy-model results (§4, the [toy-model scripts](/wiki/method/verification/toy-model-scripts)), carry [V], but §2 does not place them in Tier 1; it counts the §12 obituary among the most reliable Tier-3 items (below).

### What Tier 1 does not cover

The plain-language passage of #11 §2 draws the line: "What no machine can check is whether the algebra is attached to the right physics; that verdict belongs to expert readers and, ultimately, to data." v2.1 added a caution after review round 3: "a verification script confirms arithmetic, not the model it encodes — the §12 failure passed a script whose physics input was wrong, and was caught only by an independent review." The script had reproduced a [misremembered normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) of the Kibble estimate of defect production; round 3's adjudication puts it as "the author's verification checks the author's model" ('Pre-registration scored'). Round 4 found the same pattern in another form: [a potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) checked "only at frozen H" was unbounded below once H was dynamical ('Rulings' F2). Both lessons are now rules: [Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model), [independent anchors](/wiki/method/verification/independent-anchors) and [the reduced-model stability rule](/wiki/method/verification/reduced-model-stability).

## Tier 2: literature

"Tier 2 (literature): correct at the level of well-worn results; exact numbers, conventions, and attributions are flagged † pending source checks." (#11 §2). The † mark means a reference was recalled from model memory; checking every such reference against its source is the open [literature battery](/wiki/method/literature-battery), #11 §14 item 10.

In the wiki's reading, the qualification has bitten in the program's record at one of the levels it names, attribution. The compatibility theorem, presented as derived in v2.0, was found to be a literature result and re-tagged in v2.1 ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)). v2.2 credited Freidel, Leigh and Minic with the idea that a preferred polarization breaks Born duality (#11 §3; [broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)).

## Tier 3: novel structural physics

"Tier 3 (novel structural physics): plausibility-tier reasoning; honest prior per claim ~50–80% pending expert review; the selection-versus-derivation bias is acknowledged explicitly where it operates (§7.4)." (#11 §2).

In the wiki's reading, Tier 3 is the program's own structural argument wherever it goes beyond the battery's algebra and beyond cited literature: the reading of [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) as [spontaneously broken](/wiki/program/hard-core), the identification of [the momentum graviton](/wiki/gravity/momentum-graviton), the [gated dark-matter sector](/wiki/dark-matter/conjugate-matter), the [dark-energy identification](/wiki/cosmology/dark-energy/tau-quintessence) and the [charge-lattice unification](/wiki/electric-magnetic-duality/symplectic-charge-lattice). The figure ~50–80% is a stated prior for each claim taken singly. #11 gives no derivation of it; it is a self-assessment that waits on expert readers. The four review rounds in the record were by AI referees ([blind review](/wiki/method/review)), so that expert review has not yet happened.

### Negative results: the most reliable Tier-3 items

"Negative results (§9, §7.1, and the §12 obituary) are the most reliable Tier-3 items, since the program's incentive gradient ran against them." (#11 §2). In the wiki's reading of "incentive gradient": a program looking for support for its own ideas is more likely to err toward a positive result than toward a negative one, so a calculation that came out against the program's interest is less likely to reflect that error. The three are [the death of momentum clumping](/wiki/dark-matter/momentum-clumping) (§9), the exclusions of massless and ungauged X in [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) (§7.1), and [the soliton obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary) (§12). The rule that follows is on [Negative results and dead claims](/wiki/method/negative-results).

## The selection-versus-derivation bias

#11 does not define the term; in the wiki's reading, the bias is the gap between finding a structure and choosing it. Where the program needs a consistent structure at some step and the literature offers one, the program may adopt it and then describe the result as forced, when its own premises have only selected it from the known options. The check is to say which steps are selections. #11 states that the bias "is acknowledged explicitly where it operates (§7.4)".

### Where it operates

- **The frame tier.** The [tuning test](/wiki/gravity/tuning-test) found that couplings written in the metric fail the [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) condition and couplings written in frame (vielbein) variables pass. The passing class is the Hinterbichler–Rosen class of [wedge-product potentials](/wiki/gravity/spin-2-fields/vielbein-formulation), "ghost-free by construction", and the calc note tags the step "[D — structural, resting on T]" (`notes/debt1a-iii-tuning-test.md` §3; [the frame tier](/wiki/gravity/tuning-test/frame-tier)). The program did not derive that its geometric action reduces to this class. #11 §14 item 1 records it: "First-principles reduction of the frame-tier wedge sector from S_H (class selected, not derived) [O]." The v1 paper had said the class "was selected by minimality + consistency, not derived line-by-line" (#9 §10 item 1). See [Open: deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction).
- **"Unique" and "unique known".** The forcing chain of #11 §7.1 ends: "The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen", dRGT being [de Rham–Gabadadze–Tolley](/wiki/gravity/spin-2-fields/drgt-massive-gravity). Calc note #6 had written "Massive spin-2 coupled to gravity has exactly one known consistent structure" (`notes/debt1a-ii-X-classification.md` §3), and the Debt-1 note that first described the pattern says each test "forced it into the unique known consistent structure at that junction" (`notes/debt1a-iii-tuning-test.md` §5). `HANDOFF.md` §1 says the structural core was "forced onto unique consistent structures each time", and #11 §15 that each test "forced the theory onto the unique consistent structure available". The dropped qualifier is recorded as flag 7 in `review/wiki-build-flags.md`; the wiki quotes each wording as written.

### The novelty downgrade of §7.4

After the [palindrome](/wiki/gravity/palindromic-branch/palindrome) identity of #11 §7.3 was derived, a literature search found that the [partially-massless](/wiki/gravity/spin-2-fields/partially-massless-gravity) (PM) parameter point of bimetric gravity lies inside the program's [palindromic branch](/wiki/gravity/palindromic-branch), and that an exchange-symmetric cancellation of vacuum energy has a precedent by a different mechanism. #11 downgraded the identity's novelty "from "likely standalone result" to "requires detailed comparison with the PM and exchange-symmetric literature," queued as an open item", and names the downgrade as the bias check of §2 (#11 §7.4). See [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity) and [Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison). #11 §15 keeps "the novelty demotion of §7.4 as a standing caution" among its degeneration risks ([Assessment: a live research program](/wiki/program/assessment)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §2 — the three tiers, the ranking of negative results, the v2.1 caution; §3 — the v2.2 credit to Freidel, Leigh and Minic; §7.1–§7.4 — the forcing chain, the tuning test, the identity and the novelty downgrade; §14 item 1 — "class selected, not derived"; §15 — the standing caution
- `verify/battery.py` (output in the gate) — Tier 1's seven tests
- `review/round3-adjudication.md` 'Pre-registration scored' and `review/round4-adjudication.md` 'Rulings' F2 — the two ways a checked script missed the physics
- `notes/debt1a-iii-tuning-test.md` §3, §5 and `notes/debt1a-ii-X-classification.md` §3 — the frame tier as a selected class; "unique known"
- `notes/broken-born-program-v1.md` §10 item 1 — the v1 wording of the selection
- `HANDOFF.md` §1, §5 — "unique consistent structures"; the battery as handed over
- `review/wiki-build-flags.md` item 7 — the dropped qualifier; item 36 — where the parity figures are printed
