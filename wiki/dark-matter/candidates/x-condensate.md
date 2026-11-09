---
title: "The X-condensate candidate"
weight: 40
status: alive
description: "A coherent oscillation of the massive momentum graviton, protected by its mass, that would unify dark matter with the geometry; one of #11's three dark-matter candidates."
provenance: [D, O]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §13"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 9"
  - "notes/x-classification.md §4"
  - "notes/x-classification.md §5"
  - "notes/geometric-core.md §C"
  - "notes/beta-coefficients.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-program-v1.md §10"
  - "HANDOFF.md §2"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/wiki-build-flags.md item 5"
  - "review/wiki-build-flags.md item 20"
  - "review/wiki-build-flags.md item 63"
  - "popsci/angle-of-the-mirror.md 'Corollaries and daydreams'"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*The X-condensate candidate is the proposal that [dark matter](../_index.md) is a coherent, spatially uniform oscillation of X, the program's [momentum graviton](../../gravity/momentum-graviton/_index.md): the massive spin-2 field that the broken [reciprocity](../../phase-space/reciprocity/born-reciprocity.md) adds to gravity. If it holds, dark matter and the hidden half of the geometry are one field rather than two separate things. The idea was logged during the work on [the field-equation problem](../../history/main-problems.md) as a direction deliberately left unopened. It is one of the checkpoint's three dark-matter candidates, with [the χ-particle candidate](chi-particles.md) and P.R.'s conjecture of [magnetic monopoles abundant in momentum space](momentum-space-monopoles.md). The record holds its profile and its history, not a calculation; like the χ-particle candidate, its abundance is unexplained.*

**Status:** Alive — one of three candidates; [#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) tags the table of candidates "[D — framework; each candidate O]". The field it is made of is derived ([D + T], [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t)); that the dark matter is made of it is open. Its lineage, [bigravity dark matter](bigravity-dark-matter.md), is cited from model memory [23†]; flag 20 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) suspects that #11's entry for it pairs one paper's title with another's arXiv number. Nothing on this page is machine-checked.

## The candidate

[Checkpoint #11](../../history/documents/checkpoint.md) [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) lists three candidates for dark matter, each with its origin, what makes it stable, and the observable that would single it out. The second row:

| Candidate | Origin | Stability | Distinctive handle |
|---|---|---|---|
| **X-condensate** | oscillating massive spin-2 (bigravity-DM lineage [23†]) | m_X-protected | unifies dark sector with geometry; coherent-field signatures; knee shape wave-like |

DM there is dark matter. The tag "[D — framework; each candidate O]" says that the framework producing the candidates is derived and each candidate is open. The other rows are [χ particles](chi-particles.md) and P.R.'s [conjugate monopoles](momentum-space-monopoles.md), and "The 5.4 : 1 abundance question (polarization-genesis) applies to all three" ([#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model)). Those two are conjugate matter, P.R.'s core conjecture ([#11 App. A item 4](../../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates)); the X-condensate is the one candidate made of the geometry instead.

## What X is

The program's geometry lives in one field on phase space, the [modular field](../../phase-space/modular-field/modular-field-z.md) Z = X + iY. Its imaginary part is the spacetime metric, Im Z = Y = g. Its real part is "Re Z = X, a *new symmetric tensor*: the momentum graviton. It is exactly the fluctuation that breaks η-compatibility — i.e., the local wobble of the emergent polarization" ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard)). X is the field that measures how the split of phase space into position and momentum varies from place to place.

The field-equation problem established what kind of field X is ([why X must be massive](../../gravity/momentum-graviton/forcing-chain.md)). In #11's summary [D + T]: X is [shift-symmetric](../../gravity/momentum-graviton/shift-symmetry.md) and so "never auxiliary"; its local symmetry makes it "a second linearized-diff gauge field", that is, a second graviton; a second massless graviton is excluded by [the multi-graviton no-go](../../gravity/spin-2-fields/multi-graviton-no-go.md) [8†]; and "The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale" ([#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t); [the gravitational Higgs mechanism](../../gravity/momentum-graviton/gravitational-higgs.md)). X is therefore a massive spin-2 field with five polarizations, governed by [Hassan–Rosen bimetric gravity](../../gravity/spin-2-fields/hassan-rosen-bimetric.md) restricted to the [palindromic branch](../../gravity/palindromic-branch/palindrome.md).

The properties that matter for a dark-matter candidate are in [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) [D]:

- **Mass.** "Five βₙ → two parameters (M_X ∝ 2(β₁+β₂); one cubic shape)". No document gives a value for M_X. [Calc note #8](../../history/documents/field-equation-notes.md) [§3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t), the source of the count, writes the proportionality for the squared [Fierz–Pauli](../../gravity/spin-2-fields/fierz-pauli.md) mass, "m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**"; the difference is recorded in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 5, and this page quotes both as written ([spectrum, parameters and reciprocity parity](../../gravity/momentum-graviton/spectrum-and-parity.md)).
- **Parity.** The massless graviton is "reciprocity-even" and X is "reciprocity-odd"; "Reciprocity is a selection rule on vertices" ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t); on the parities under [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)'s Z → −Z⁻¹, see flag 39 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).
- **Couplings to ordinary matter.** "SM couplings gravitational-strength and Yukawa-cut at 1/M_X" (SM is the Standard Model; [Yukawa forces](../../gravity/spin-2-fields/yukawa-forces.md#the-momentum-graviton-x)). With [equal effective Planck masses](../../gravity/spin-2-fields/planck-units.md#equal-planck-masses-in-the-bimetric-sector), "SM matter — coupled to g — sees both eigenstates with comparable strength; safety is by **range**, not decoupling" ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t); [safety by range](../../gravity/momentum-graviton/fifth-force-safety.md)).

## What "condensate" means here

Calc note [#6](../../../notes/x-classification.md) states the idea in one sentence: "homogeneous oscillations of a massive spin-2 X are themselves a dark-matter candidate (cf. bigravity dark matter)" ([#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)). A scalar field that oscillates uniformly through space at a frequency set by its mass behaves, averaged over the oscillation, as pressureless matter, its energy diluting with the cube of the scale factor like cold dark matter [T]; for a light scalar this is [the misalignment mechanism](../wave-dark-matter/misalignment-mechanism.md). The uniform mode of a spin-2 field is a tensor and singles out directions in space; that case and its literature are on [bigravity dark matter](bigravity-dark-matter.md). Such a state is coherent: the field moves in phase everywhere, like a single standing wave, rather than as a gas of independent quanta [T].

The program's record does not go further. No document computes how the oscillation would be produced in the early universe, its amplitude, or its energy density.

## The three handles

The last column of the table names three distinguishing features. #11 states them and does not derive them; what the record says about each:

- **"unifies dark sector with geometry".** Calc note #6: "BBT may not need χ as a separate field — X-condensate dark matter would unify the geometric sector with the dark sector" ([#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade); BBT is Broken-Born theory, the program's earlier name). [#9](../../../notes/broken-born-program-v1.md) phrased it as "potentially eliminating χ and unifying the dark sector with the geometry" ([#9 §10 item 7](../../../notes/broken-born-program-v1.md#10-open-problems)). If the candidate holds, the dark matter is a state of the geometric field X, not a separate matter field.
- **"coherent-field signatures".** Not specified further in any document. [Row 11](../../predictions/dark-sector-microstructure.md) relies on "coherence signatures", with rows 1–3, to separate particles from a condensate.
- **"knee shape wave-like".** #11 gives no derivation for this entry. In [the predictions table](../../predictions/_index.md) the wave-like tail of [the self-interaction knee](../conjugate-matter/scattering-law.md) is "(v\*/σ)⁴", derived for wave χ on [the wave island](../momentum-clumping/wave-island/_index.md) ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested); [row 3](../../predictions/island-discriminant.md)). No document derives a knee for a condensate of X or relates it to wave χ.

The stability entry, "m_X-protected", is likewise stated without an argument. No document computes a lifetime for the oscillation.

## Its tests

- **[Row 7](../../predictions/direct-detection-null.md): a permanent null.** "**Permanent null** (both dark-sector candidates SM-decoupled; P4 strict)", killed by "Any confirmed non-gravitational DM–SM coupling" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)). The row says "both" although [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) lists three candidates; flag 63 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending, proposes wording that counts all three. X does couple to ordinary matter, at gravitational strength and with a range cut off at 1/M_X ([#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d)); the null concerns couplings other than gravity.
- **[Row 11](../../predictions/dark-sector-microstructure.md): particles or condensate.** "Particles vs condensate, separable via rows 1–3 + coherence signatures", marked "Diagnostic" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)); flag 63 proposes adding the conjugate monopoles to the row. How to make the separation is open: "Discriminating the three dark-sector candidates (§12) [O]" ([#11 §14 item 9](../../papers/broken-born-checkpoint-v2.md#14-open-problems)).

## What is open

- **Abundance.** "The 5.4 : 1 abundance question (polarization-genesis) applies to all three" ([#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model); [Open: polarization-genesis and the 5.4 : 1 ratio](polarization-genesis.md)).
- **Telling it from the other candidates.** [#11 §14 item 9](../../papers/broken-born-checkpoint-v2.md#14-open-problems), above.
- **Cosmological stability of X.** Reciprocity forces equal effective Planck masses, which "rules out the M_f ≪ M_g escape" in which a heavy spin-2 field has been shown linearly stable at late times ([bimetric cosmology and its instabilities](../../gravity/spin-2-fields/bimetric-cosmology.md)); whether "a large mass alone is enough at M_f = M_g is open" ([`review/v3-worklog.md`](../../../review/v3-worklog.md), item R7; [Open: stability at equal Planck masses](../../gravity/momentum-graviton/equal-planck-mass-stability.md)). The question concerns X itself, and through it this candidate.
- **No calculation yet.** Production, amplitude, lifetime and the coherence signatures are all uncomputed.

## Not the same condensate

The word "condensate" appears twice in the dark-matter record. On the wave island of the clumping problem, very light χ can condense into Bose stars ([wave kinetics and Bose-star formation](../wave-dark-matter/wave-kinetics.md)). Those are condensates of the matter field χ. The X-condensate is a state of the geometric field X. No document relates the two.

## History

- **A door left closed (calc note #6).** "A new door, deliberately left closed today: homogeneous oscillations of a massive spin-2 X are themselves a dark-matter candidate (cf. bigravity dark matter). BBT may not need χ as a separate field — X-condensate dark matter would unify the geometric sector with the dark sector. Logged as an open direction, not pursued. [O]" ([#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)). [#6 §5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) lists "X-condensate dark matter (§4)" among what is "Also now open".
- **[The lab notebook](../../history/documents/lab-notebook.md).** Addendum v0.4 records "A new open direction: massive-X condensate as the dark matter itself (bigravity-DM-style), potentially unifying the dark sector with the geometry."
- **#9.** Open problem 7: "X-condensate as the dark matter itself (bigravity-DM-style), potentially eliminating χ and unifying the dark sector with the geometry [O — direction, deliberately unopened]" ([#9 §10](../../../notes/broken-born-program-v1.md#10-open-problems)). Its row 7 already covers it: "χ (or X-condensate) has no non-gravitational SM coupling" ([#9 §9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions)).
- **The first version of #11, and the handoff.** The candidate became one row of a three-way choice with χ particles and [superheavy solitons](soliton-candidate/obituary.md). [The handoff](../../history/documents/handoff.md), [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen), lists "Dark-sector trilemma discrimination: particles vs X-condensate vs solitons" as open item 8.
- **[#14](../../../notes/knot-dark-matter-standalone.md)'s model of the third candidate.** #14's model, built with ordinary kinematics, failed on its recomputed abundance in [round 3](../../method/review/round-3/_index.md) ([`review/round3-adjudication.md`](../../../review/round3-adjudication.md), [Decision 2](../../method/review/round-3/decisions.md#decision-2-14s-model-retired); [Obituary: #14's superheavy-soliton model](soliton-candidate/obituary.md)). #14's model did not treat localization in momentum, so the candidate itself has not been tested: conjugate monopoles localized in momentum are P.R.'s open conjecture, and [#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) lists them with χ particles and the X-condensate as the three candidates ([Conjecture: magnetic monopoles abundant in momentum space](momentum-space-monopoles.md)).
- **The popular articles.** Both predate the failure of #14's model (2026-10-19) and describe the three-way question. [#10](../../../popsci/angle-of-the-mirror.md) lists "a condensate of the twin-graviton field itself" ('Corollaries and daydreams'); [#12](../../../popsci/universes-other-half.md) writes "a condensate of the massive geometric field itself, in which case dark matter and the hidden geometry are one substance" ('Dark matter as the other polarization'). Neither is a source for the candidate's status ([the popular articles](../../history/documents/popular-articles.md)).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) — the candidate profile and its tag; [§7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — X forced massive; [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) — mass, parity and couplings; [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the wave-island tail; [§13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — rows 3, 7 and 11; [§14 item 9](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — discriminating the three candidates; [App. A item 4](../../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates) — the two candidates that are conjugate matter
- [`notes/x-classification.md` §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — the door "deliberately left closed"; [§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — listed as open
- [`notes/geometric-core.md` §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — X as Re Z, "the local wobble of the emergent polarization"
- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — m_FP², equal Planck masses, safety by range
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.4)' — the open direction
- [`notes/broken-born-program-v1.md` §10](../../../notes/broken-born-program-v1.md#10-open-problems) — open problem 7 of #9; [§9](../../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions) — row 7 of #9
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — open item 8, the trilemma (superseded)
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Decisions' 2 — covers #14's model, which used ordinary kinematics
- [`review/v3-worklog.md`](../../../review/v3-worklog.md) 'Round-2 pending list' — R7, stability at equal Planck masses
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 5 — M_X versus m_FP²; item 20 — the title and arXiv number of reference [23]; item 63 — rows 7 and 11 name two candidates, pending
- [`popsci/angle-of-the-mirror.md`](../../../popsci/angle-of-the-mirror.md) 'Corollaries and daydreams'; [`popsci/universes-other-half.md`](../../../popsci/universes-other-half.md) 'Dark matter as the other polarization' — the three-way framing
