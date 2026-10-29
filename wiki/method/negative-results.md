---
title: "Negative results and dead claims"
weight: 60
status: method
description: "The program's rule on negative results and dead claims: why #11 counts negative results as its most reliable Tier-3 items, the deaths in the record, how a death is reported, the rescue the program declined, and what a death leaves standing."
sources:
  - "CLAUDE.md 'Method'"
  - "CLAUDE.md 'Since the handoff'"
  - "HANDOFF.md §7"
  - "HANDOFF.md §2"
  - "papers/broken-born-checkpoint-v2.md §1"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md §11.4"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md Appendix A"
  - "notes/ufd-endpoint.md 'Verdict and closure of the clumping problem'"
  - "notes/knot-dark-matter-standalone.md banner"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round4-adjudication.md 'Rulings'"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "verify/velocity_gated_gravity.py 'D. The obituary's scope'"
  - "notes/velocity-gated-gravity.md §4"
  - "notes/velocity-gated-gravity.md §7"
  - "review/wiki-build-flags.md items 59, 60, 62"
---

*The program's rule on negative results is that a claim killed by calculation or by review is reported in an obituary of its own and is not revived. [Checkpoint #11](/wiki/history/documents/checkpoint) ranks such negative results as the most reliable of its new structural results. [The founding image](/wiki/dark-matter/momentum-clumping/founding-image) of the program, dark matter clumping in velocity rather than in space, is one of the dead claims, and so is a later dark-matter candidate, [superheavy solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) of a hidden gauge sector. The wiki gives every dead claim its own obituary page and lists them all in [the graveyard](/wiki/status/graveyard).*

**Status:** Method, in force — untagged — root `CLAUDE.md` ('Method') and `HANDOFF.md` §7; applied in #11 §9 and §12 and in round-3 Decision 2 (`review/round3-adjudication.md`).

## The rule

The root `CLAUDE.md`: "Report negative results prominently. Claims listed as dead in HANDOFF §2 stay dead." `HANDOFF.md` §7 makes it part of Paul's [calibration request](/wiki/method/collaboration#the-calibration), "keep reporting negative results prominently. Honest obituaries are part of the deliverable." The rule has two halves. The first is about visibility: a failure is reported where a reader will see it, not in a footnote. The second is about permanence: once a claim is dead, later work does not bring it back under a new parameter or a new name.

## Why negative results count as the most reliable

#11's methodological preface ranks them first among the program's new structural results (Tier 3): "Negative results (§9, §7.1, and the §12 obituary) are the most reliable Tier-3 items, since the program's incentive gradient ran against them." (#11 §2). The three named are [the death of momentum clumping](/wiki/dark-matter/momentum-clumping) (§9), the exclusions in [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) (§7.1), and [the soliton obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary) (§12). The tiers, and what "incentive gradient" means, are on [Claim tiers and selection bias](/wiki/method/claim-tiers#negative-results-the-most-reliable-tier-3-items).

## The deaths in the record

### Dead at the handoff

`HANDOFF.md` §2 lists them under "Dead (killed by own calculations — keep dead)":

- **Momentum-space clumping as dynamics.** The founding image was tested three ways in [the clumping problem](/wiki/history/main-problems). For particle dark matter the [mean-field instability criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) "fails by 10²⁸–10³¹ at the scattering benchmark" (#11 §9 [D]). On the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), the one branch where clumping became mandatory (Scenario A) predicted that [ultra-faint dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) would be drained of dark matter, and it was "**falsified** by observed UFD density and longevity" (UFD: ultra-faint dwarf). Elsewhere the effect is "tunable across ~10 orders: optional, never required" (#11 §9). The closing calc note's verdict, BBT being Broken-Born theory, the program's earlier name: "Nowhere in the viable parameter space of BBT is velocity-space clumping a mandatory phenomenon." (`notes/ufd-endpoint.md`). See [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image) and [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a). The handoff marks the 10²⁸–10³¹ shortfall as machine-verified; until 2026-10-28 no `verify/` script checked it (flag 16 in `review/wiki-build-flags.md`), and section D of `verify/velocity_gated_gravity.py` now reproduces it, with #11 §9's tag [D] unchanged until Paul rules. The obituary covers the program's contact-range interaction: it says clumping is required nowhere, not that it cannot happen; the momentum-gravity note of 2026-10-28 (computed, not reviewed) tests a long-range variant, which the record does not contain, and finds it decorative ([what the obituary covers](/wiki/dark-matter/momentum-clumping/founding-image#what-the-obituary-covers); [Conjecture: a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction)).
- **"Conjugate collapse powers our expansion".** "first version gave w = −2 (falsified); corrected dictionary removed the mechanism (dual dust ↦ dust)" (`HANDOFF.md` §2). #11 records the supposition as "dead twice" (Appendix A item 9). See [its obituary](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion).
- **Conjugate monopoles as the explanation of our monopole non-detection.** "wrong duality; inflation suffices" (`HANDOFF.md` §2). #11 v2.3 states the grounds as they now stand (flag 59 in `review/wiki-build-flags.md`, accepted 2026-10-29): only the [shared-photon form](/wiki/electric-magnetic-duality/magnetic-identification#shared-photon) of P.R.'s magnetic-mirror conjecture, in which momentum-polarized analogs carry magnetic charge of our own photon, contests the duality ground, and that form needs [P4](/wiki/program/postulates/p4-polarized-matter), the postulate that gauge forces do not cross polarizations, restated (#11 §11.4); and the null result is expected under several standard histories, inflation after a unification transition among them, so it lends the program no support (#11 §11.1). The claim stays dead. Whether the shared-photon form, with P4 restated, would reopen it is flag 62, pending Paul's ruling; v2.3 leaves it dead, since the root `CLAUDE.md` keeps claims listed dead in `HANDOFF.md` §2 dead and this one is listed there (flag 62). See [its obituary](/wiki/electric-magnetic-duality/monopole-explanation).
- **α_d ≈ 34 via [Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) against our photon.** Killed by the [round-1](/wiki/method/review/rounds-one-and-two) referee: one "can't use our DSZ lattice and then deny coupling to our photon" (`HANDOFF.md` §2), DSZ being the Dirac–Schwinger–Zwanziger [charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice). See [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling).

### Killed by review since the handoff

- **Superheavy solitons.** `HANDOFF.md` §2 still lists them as the current best dark-matter candidate; the root `CLAUDE.md` overrides it: "The superheavy soliton candidate in HANDOFF §2 is **dead** as a program-native proposal." [Round 3](/wiki/method/review/round-3) found the [Kibble estimate](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) of [defect](/wiki/symmetry-breaking/topological-defects) production misnormalized: one defect per Hubble volume gives "p ≈ 104 [V]" against the 0.023 that #14 v3 had used, at minimum production the abundance closes at "M ≈ 2.9–4.4×10¹² GeV [V]", and the v3 benchmark "is overproduced by 2.1×10³–1.2×10⁴ [V]" (#11 §12; [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). Several of #14's subsidiary claims died with it; the graveyard lists them.
- **The naive potential of the first toy model.** [Round 4](/wiki/method/review/round-4) found that the potential version 1 of the [toy-model note](/wiki/symmetry-breaking/toy-models) used to pin the polarization "is unbounded below in model I" once the field H is dynamical (ruling F1), so its vacuum (1, K_ref) is a saddle of the full model and the [Monte Carlo](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) had simulated a [frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) (ruling F2) (`review/round4-adjudication.md`; [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)). Version 2 replaced it with a [bounded potential](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential).

## How a death is reported

- **In the abstract.** #11's plain-language abstract reports both deaths: following the idea "killed its most cherished consequence — dark matter clumping in velocity instead of space", and the third candidate "was worked out, failed its own abundance arithmetic, and is retired" (#11 §1).
- **In the assessment.** #11 §15 opens its assessment with the death of the founding image ([Assessment: a live research program](/wiki/program/assessment)).
- **In a section of its own.** #11 §9 is titled "Obituary: the death of momentum clumping". The §12 obituary is laid out as "What was claimed", "What was built and how it was tested", "Why it failed", "Verdict", "What survives" and "Checks", the last pointing to the script that gates its numbers.
- **In the predictions table.** #11 §13 ends: "Withdrawn with cause: velocity-space granularity in halos; Fornax friction suppression (obituary §9); superheavy-soliton dark matter (obituary §12)." See [Obituary: velocity-space granularity in halos](/wiki/dark-matter/momentum-clumping/velocity-granularity), [Obituary: Fornax friction suppression](/wiki/dark-matter/momentum-clumping/fornax-friction) and [History of the predictions table](/wiki/predictions/table-history).
- **Against the founding suppositions.** #11's Appendix A gives each of Paul's eleven founding suppositions its fate, including "dead as dynamics" (item 3) and "dead twice" (item 9) ([Founding suppositions and their fates](/wiki/program/founding-suppositions)).
- **In the files.** The withdrawn manuscript #14 v3 was moved from `papers/` to `notes/` with a banner: "Kept as the audit trail; not for circulation." Its gated checks were replaced by `verify/soliton_obituary.py`, which checks the numbers of the obituary; the adjudication notes that this "does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything" ('Decisions'; [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).

## Dead stays dead: the rescue that was declined

After round 3, the soliton candidate could have been kept by adding a free [dilution factor](/wiki/cosmology/early-universe/relic-yield-and-dilution#entropy-dilution-t). Decision 2 rejected that route: it would restore the mass "only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3)", and the mass "would then no longer be a prediction". It cited the clumping obituary as the precedent for keeping a dead claim dead (`review/round3-adjudication.md`, 'Decisions'; [Round-3 decisions and lessons](/wiki/method/review/round-3/decisions)). In the terms of [Lakatos's methodology](/wiki/method/lakatosian-methodology), a free parameter added to save a claim is an ad hoc adjustment (the wiki's reading). Decision 3 followed: the queued "√N floor" calculation was dropped, because its premise was inverted and "it has no candidate left to serve" ([Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)).

The clumping rows were withdrawn on the same terms: "Rows withdrawn permanently." (`HANDOFF.md` §2); "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands." (`notes/ufd-endpoint.md`).

## What a death leaves standing

An obituary states its scope, so that the parts that survive are not lost with the claim.

- **After the clumping problem.** The salvage was "the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island" (#11 §9; [Row 3: the island discriminant](/wiki/predictions/island-discriminant)).
- **After the solitons.** #11 §12: "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]"; the [minimal adjoint-only hidden sector](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) "is excluded on its own terms" [V]; and the clumping loophole "remains untested, but has no candidate" ([Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)). The [V] numbers are recomputed in the gate by [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script).
- **A split verdict.** Founding supposition 5, that monopoles live in the conjugate space, died as an explanation and survives as [ontology](/wiki/electric-magnetic-duality/conjugate-monopoles): "as explanation, dead (wrong duality, which only §11.4's shared-photon form contests, and that form needs P4 restated; the null result is expected under several standard histories, so it lends no support — v2.3, flag 59); as ontology, alive and consequence-bearing" (#11 Appendix A item 5). Until v2.3 the parenthesis read "(wrong duality; inflation suffices)". Since v2.3 the item's ontology half, joined with item 11, is P.R.'s [magnetic-mirror conjecture](/wiki/electric-magnetic-duality/magnetic-identification) (§11.4) [O].

## Negative results about the method

The adjudications also record the author's misses. The round-3 adjudication scored its pre-registration as a miss on the verdict, "the first after 2 for 2", and wrote: "Calibration: my confidence in v3 was too high." It upheld the referee's finding that v3's statement "all numbers computed by executed code" overstated what the code showed: "The code checked the arithmetic of a wrong model" (ruling 13). In round 4 the adjudicator wrote of the unbounded potential: "I should have caught F1 myself: I checked the potential only at frozen H." The calibration record is kept on [pre-registration](/wiki/method/review/pre-registration), and the other two misses became rules: [Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model) and [the reduced-model stability rule](/wiki/method/verification/reduced-model-stability).

## In the wiki

"Dead stays dead" is one of the wiki's own rules: claims killed in `HANDOFF.md` §2, #11 §9 and §12, and the adjudications "are reported as dead, prominently, on their own pages" (`wiki/CLAUDE.md`). Each such page has status `dead` and a title beginning "Obituary:", follows the order of #11's obituary (what was claimed, how it was tested, why it failed, what survives), and links the claim's home section, the ruling that killed it and [the graveyard](/wiki/status/graveyard).

The rule covers claims that the record killed. One obituary rested on the wiki's own reading instead: the page on #12's magnetic identification recorded it as dead although no review or document had killed it. Flag 60 found that such a verdict adds a result, which the wiki does not do; Paul accepted the flag on 2026-10-29, and the page became a conjecture page ([Conjecture: the momentum sector as the magnetic mirror](/wiki/electric-magnetic-duality/magnetic-identification)).

## Sources

- Root `CLAUDE.md` 'Method' — the rule; 'Since the handoff' — the soliton candidate declared dead
- `HANDOFF.md` §7 — the rule in Paul's calibration request; §2 — the dead list at the handoff and the withdrawn rows
- `papers/broken-born-checkpoint-v2.md` §1 — the deaths in the abstract; §2 — negative results as the most reliable Tier-3 items; §9 and §12 — the two obituaries, their numbers and survivors; §11.1 — the dead monopole explanation's grounds as v2.3 states them; §11.4 — the magnetic-mirror conjecture [O]; §13 — "Withdrawn with cause"; §15 — the assessment's opening; Appendix A — the fates of the founding suppositions
- `review/wiki-build-flags.md` items 59 and 60 — the restated grounds, and the reversal of the wiki's obituary of the magnetic identification, both accepted on 2026-10-29; item 62 — whether the shared-photon form would reopen the dead explanation, pending, and why v2.3 leaves it dead
- `notes/ufd-endpoint.md` 'Verdict and closure of the clumping problem' — the net theorem and the permanent withdrawal
- `review/round3-adjudication.md` 'Rulings' 13, 'Pre-registration scored', 'Decisions' — the overstated verification, the calibration miss, Decisions 2 and 3, the withdrawal of v3
- `notes/knot-dark-matter-standalone.md` — the withdrawal banner
- `review/round4-adjudication.md` 'Rulings' F1–F2 — the naive potential
- `review/wiki-build-flags.md` item 16 — the handoff's unscripted ✓ on the clumping shortfall, and its addendum of 2026-10-28
- `verify/velocity_gated_gravity.py` section D — the shortfall, gated since 2026-10-28
- `notes/velocity-gated-gravity.md` §§4, 7 — what the obituary covers; the long-range variant decorative
- `wiki/CLAUDE.md` 'The wiki is derivative' — dead stays dead in the wiki
