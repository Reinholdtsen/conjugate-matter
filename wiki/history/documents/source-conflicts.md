---
title: "Conflicts between sources"
weight: 80
status: record
description: "Where documents disagree, how the precedence order resolves each case, and the conflicts no document settles."
sources:
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md"
  - "papers/reciprocity-toy-models.md"
  - "review/round4-adjudication.md"
  - "review/round3-adjudication.md"
  - "review/round3/referee/audit-notes.md"
  - "review/v3-worklog.md 'New open items'"
  - "papers/conjugate-special-relativity.md"
  - "HANDOFF.md"
  - "notes/broken-born-theory.md"
  - "notes/broken-born-program-v1.md"
  - "notes/debt1a-ii-X-classification.md"
  - "notes/debt1a-iv-beta-coefficients.md"
  - "notes/debt3a-stream-stability.md"
  - "notes/debt3b-wave-island.md"
  - "notes/debt3c-ufd-endpoint.md"
  - "notes/toy-lagrangian.md"
  - "popsci/angle-of-the-mirror.md"
  - "popsci/universes-other-half.md"
  - "verify/battery.py"
  - "verify/toy_gw.py"
  - "scripts/check.sh"
---

*The program's documents were written over several weeks, and the later ones correct, re-tag or retire what the earlier ones said, so the same question can get different answers in different files. This page collects those disagreements. Most are settled by a fixed order of precedence in which the most current document wins. The rest are cases where documents of equal rank disagree, or where no document addresses the point; for those the wiki reports both readings and does not choose.*

**Status:** Record, current to 2026-10-20 — untagged — the precedence order is set in `wiki/CLAUDE.md`, with the root `CLAUDE.md` "Since the handoff" first; each ruling below names the document that decides it.

## Key facts

- **The order of precedence**, most current first: the root `CLAUDE.md` "Since the handoff" ([CLAUDE.md and the README](/wiki/history/documents/project-instructions)); checkpoint #11 v2.2 and the toy-model note v2; the round-4 and round-3 adjudications; #13; `HANDOFF.md`, whose §2 soliton candidate and §8 queue are superseded; the notes, with the calc notes #2–#8 final for their own scope, #1 and #9 superseded as reference and #14 withdrawn; and last the popular articles, never a source for a claim's status. The documents themselves are described under [Documents](/wiki/history/documents).
- **Dead stays dead.** Claims killed in `HANDOFF.md` §2, #11 §9 and §12, and the adjudications are reported as dead whatever an earlier or popular document says ([the graveyard](/wiki/status/graveyard)).
- **Tags follow the highest-ranked source and are never upgraded.** Where an older document marks a number machine-checked but no `verify/` script computes it, the wiki uses the tag #11 gives ([provenance tags](/wiki/method/provenance-tags)).
- **Inconsistencies inside a top-ranked document are flagged, not copied.** #11 and the root `CLAUDE.md` each contain a few statements that other parts of the same document, or the files themselves, contradict; the wiki follows the more current statement and records the lapse here and on the affected page.
- **"Unresolved"** means that two documents of equal rank disagree, or that no document settles the point. Those cases are listed first, and each affected page states both readings.

## Unresolved

- **The sign of τ's potential.** #11 §10, #9 and #1 write V = V₀[1 + cos(τ/f)], which is non-negative for V₀ > 0. Yet the same documents need V < 0 for the turnaround: τ's energy "eventually goes negative" (#11 §10), "A cosine potential is negative over half its range" (#1 §7), "Turnaround after V(τ) < 0" (#9 §9 row 5), and the quintessence fits they cite use a negative minimum. No document settles it; it needs an executed check. → [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign).
- **The momentum-localization loophole, inside #11.** §12 says the Debt-3 loophole "remains untested, but has no candidate"; §14 item 8 says the p-localization items "are closed by the §12 obituary". Read together: the loophole is untested, and it has no candidate and no work item. → [Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole).
- **"Empty set" or "measure zero".** #11 §11.1 says "true but irrelevant" is "the empty set"; #11 Appendix A item 5 quotes P.R.'s "true-but-irrelevant is measure zero". The verdict is the same either way: as an explanation of the missing monopoles the idea is dead. → [Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation).
- **Which structure is "the real structure".** #11's P2′ writes η as the matrix product H J, "with the real structure J chosen spontaneously", and #11 §5 defines J = η⁻¹H and K = η⁻¹ω; the toy-model note calls K "a real structure" with η = ωK, and #11 §14 item 11 makes "η = ωK" the order parameter. → [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter); [Notation](/wiki/notation).
- **The tadpole coefficient in the complex Grosse–Wulkenhaar model.** The round-4 adjudication (finding F6 and revision 4) says "2 ln N"; the toy-model note v2 says the level-0 tadpole "grows as ln N (it is a harmonic sum)", as do `verify/toy_gw.py` and the worklog. No document reconciles the two; the note v2 is the higher-ranked statement. → [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration).
- **The reading of the kinetic-mixing bound.** #11's P4 writes "ε ≲ 10⁻¹³ [27S]". The round-3 referee's notes quote Gherghetta et al. as "could be as large as ~1e-13" and read the number as a floor, the minimum mixing once hidden charge conjugation is broken. #11's wording stands; the reading is flagged. → [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter).
- **Arbitration scripts outside the gate.** The root `CLAUDE.md` says arbitration scripts go in `verify/`, but `review/round3/adjudicator/round3_arb.py`, `review/round4/adjudicator/arb.py` and `review/round4/adjudicator/ctrl.py` sit in `review/`, and `scripts/check.sh` does not run them. → [The gate](/wiki/method/verification/the-gate).
- **Dark energy as dual kinetic energy or as τ's potential.** #1 §6 finds "the natural source of a near-constant dark energy is kinetic energy in the dual frame"; #1 §7 then implements dark energy as τ's hilltop potential. No document derives the link between the two (an inference from reading #1). → [Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link).
- **The gate's exponent.** #1 postulates the Gaussian gate e^{−k²/μ²} with "k = m_χ v_rel/2 the incoming relative momentum"; calc note #6 derives the overlap e^{−(p₁−p₂)²/2μ²}. The two conventions are not reconciled. → [The gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism).
- **What X eats.** Calc note #6: "the four would-be Goldstones π_μ of the broken λ-gauge are eaten"; calc note #8: "the vector π_μ and the longitudinal scalar of the λ-gradient sector". #11 §7.1 follows #6. → [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs).
- **Two dual cones in #13, and its dark-sector kinematics.** As `review/v3-worklog.md` O3 records, #13 §1 uses a cone in (t, p) with slope c̃, while #13 §6 says "our massless dispersion E = c|p| *is* the dual null cone", a cone in (E, p) with slope c that belongs to the four-dimensional Born map. Paul raised it on 2026-10-19, and no queue or open-item list schedules it. #13 §4 also labels conjugate quanta by an invariant length rather than a mass, while #14 used ordinary kinematics: "The papers were never reconciled." → [Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency); [Open: the four-dimensional Born map and dual dynamics](/wiki/conjugate-relativity/four-dimensional-born-map).
- **The fuzzy end of Scenario B.** Calc note 3b lets the cores come from "fuzzy-end quantum pressure at m ∼ 10⁻²² eV", below 3c's lower edge of the surviving wave island, 3×10⁻¹⁹ eV. Neither note addresses this. → [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b).
- **The occupation number's normalization.** Calc note 3b writes N_occ = ρ/(m⁴σ³) in its setup and N_occ ≈ (2π)^{3/2}ρ/(m⁴σ³) in its rate derivation, and does not reconcile the two. → [Occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number).
- **The Freidel–Rudolph–Svoboda year.** #1 and #9 date the connection theorem 2018; #11's reference [7]† gives "(2019), arXiv:1806.05992". It may be an arXiv year against a journal year; the check is left to the † literature battery. → [References](/wiki/references); [Open: the † literature battery](/wiki/method/literature-battery).
- **The handoff's review count.** `HANDOFF.md` §1 says "Three blind AI reviews returned verdict B"; its §6 records two completed rounds and an incomplete third. → [The handoff document](/wiki/history/documents/handoff).

## Resolved, by subject

### Status changes since the handoff

- **The soliton candidate.** `HANDOFF.md` §2 calls superheavy solitons the "Current best" dark-matter candidate, its §8 items 1–3 serve it, and #10 and #12 present the knots as live. The root `CLAUDE.md`, #11 §12 and round-3 Decision 2 outrank all of these: dead. → [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary).
- **Conjugate monopoles.** `HANDOFF.md` §2 ties their ontology to the soliton candidate ("As ontology they're alive (the soliton candidate)"). The ontology stands (#11 §11.1); the dark-matter candidacy is retired. → [Conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles).
- **The handoff's open items.** Item 1, the toy Lagrangian, is met in the referees' wording; item 2, the √N floor, was dropped (round-3 Decision 3); item 3, kinetic mixing, is closed by strict P4 (Decision 1); item 8's three-way question is now two-way (#11 §12). → [Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion); [Obituary: the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor); [Dark-sector candidates](/wiki/dark-matter/candidates).
- **The electric-sublattice clause.** `HANDOFF.md` §2 asks for η as "the order parameter also selecting the electric sublattice"; #11 §14 item 11 and the toy work's criteria omit the clause and declare the criterion met. The root `CLAUDE.md`'s wording governs ("done to the referees' wording"), and the clause is recorded as unaddressed. → [Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion).

### Tags and attribution

- **The compatibility theorem.** #1 v0.3, #5 ("[D — rigorous]"), #9, `HANDOFF.md` §2, #13 ("[D — compatibility theorem]") and #14 treat it as derived in the program. #11 since v2.1 and the root `CLAUDE.md` tag it [T][V], with the statement credited to Freidel, Leigh and Minic; the block proof and the machine check stay the program's. The round-3 audit adds that positivity is not needed for C = 0, so that step of #11 §5's proof is redundant, not wrong. → [The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem).
- **The ✓ on 10²⁸–10³¹.** `HANDOFF.md` §2 marks the clumping shortfall machine-verified, but no `verify/` script computes it and #11 §9 tags it [D]. → [The mean-field criterion and its shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion).
- **Statements phrased as if machine-checked.** #11 §7.2 calls Tr(g²) + Tr(g⁻²) "provably outside the linear-in-eₙ span", where the battery's T7 tests p₄ numerically; #11 §2's "det H = 1 across the whole family" rests on T2, which checks one randomly drawn member (`verify/battery.py`). The wiki tags such steps [D]. → [The verification battery](/wiki/method/verification/battery).

### Gravity and dark matter

- **Cliff to knee.** #1's exponential cliff (v\* ∼ 120 km/s, killed by self-interaction at v > 3v\*) became #11's knee (v\* ∼ 10² km/s, killed by "Robust self-interaction at v ≫ v\*"), with the tail shape open (#11 §8, §13). → [The gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law); [Row 1](/wiki/predictions/self-interaction-knee).
- **The wave-island suppression.** Calc note 3a has (v\*/σ)³; 3b, 3c and #11 have (v\*/σ)⁴. → [Row 3: the island discriminant](/wiki/predictions/island-discriminant).
- **Row numbers.** In #1 §9 and the Debt-3 notes, rows 3 and 4 are velocity granularity and Fornax friction; in #9 and #11 they are the island discriminant and dark energy. The wiki uses #11's numbering and calls the withdrawn rows "old row 3" and "old row 4". → [History of the predictions table](/wiki/predictions/table-history).
- **How many structural tests.** Calc note #7 counts "three structural tests in a row"; #11 §15 counts "four consecutive consistency tests", and #11 governs. → [Assessment](/wiki/program/assessment).

### Dark energy

- **The reading of DESI.** `HANDOFF.md` §2 says "Consistent with DESI DR1/DR2 drift hints" (Data Release 1 and Data Release 2 of the Dark Energy Spectroscopic Instrument); #9 calls the hints "exactly the drift this sector requires", and #10 "exactly the required weakening"; #11 §10's own plain-language opener still says "exactly the required drift". The root `CLAUDE.md`, #11 §10's "Under pressure (v2.1)" paragraph and round-3 ruling 11 record Data Release 2's phantom crossing above z ≈ 0.4: the sector is under pressure. → [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).
- **Why the dictionary changed.** #9 credits "the Lagrange-multiplier bookkeeping", #11 "the constraint's Jacobian", #1 the constraint's "volume Jacobian"; the result, w_eff = −w̃, is the same, and the wiki uses #11's wording. → [The duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary).
- **Constant dark energy.** #12 calls it "impossible"; #11 row 4 says a constant w = −1 kills only the τ sector, and #10 ("Constant kills the theory's heart") agrees with #11. → [Row 4](/wiki/predictions/dark-energy-drift).

### The toy models

- **The naive potential.** The worklog's S4 pass used −μ[Tr(K K_ref)]², which round 4 found unbounded below once H is dynamical (findings F1 and F2); the note v2 uses the bounded V_b. → [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential); [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential).
- **V_b's zero mode.** The round-4 adjudication calls it "the residual diagonal squeeze, which is an exact symmetry"; the note v2 says it "is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref". The note v2 (rank 2) outranks the adjudication (rank 3). → [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential).
- **"Ising class".** The worklog calls the Monte Carlo phase "Ising class", and the note v1 "Ising-class"; #11 §14 item 11 says "an ordered ℤ₂ phase in 1+1 in the frozen-H reduction", as the note v2 does. → [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo).

### The popular articles

- **"As if confirmed".** #12 "presents the broken-Born framework as if it were confirmed" and is never a status source; its "single assumption" yields to #11's postulates P1–P5. → [The popular articles](/wiki/history/documents/popular-articles).
- **The magnetic identification.** #12's "about 34, against our 1/137" conflicts with the dead α_d ≈ 34 via Dirac quantization against our photon, with #14's "dark by sector separation", and with strict P4 and #11 row 7; it is treated as dead. → [Obituary: the magnetic identification](/wiki/electric-magnetic-duality/magnetic-identification).
- **"Eighty-eight years in a drawer"** (#10). #11 v2.2 credits Freidel, Leigh and Minic for "broken Born duality", and v2.1 credits them for the compatibility statement. → [Broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality).

## Sources

- `wiki/CLAUDE.md` 'The wiki is derivative' — the precedence order and the dead-stays-dead rule
- `CLAUDE.md` 'Since the handoff' — the top-ranked rulings
- `papers/broken-born-checkpoint-v2.md` and `papers/reciprocity-toy-models.md` — the rank-2 statements, including the internal inconsistencies listed above
- `review/round4-adjudication.md`, `review/round3-adjudication.md` and `review/round3/referee/audit-notes.md` — the review rulings and decisions
- `papers/conjugate-special-relativity.md` and `review/v3-worklog.md` 'New open items' — the two dual cones and the dark-sector kinematics
- `HANDOFF.md` — the superseded state of 2026-10-19
- `notes/broken-born-theory.md`, `notes/broken-born-program-v1.md`, the calc notes and `notes/toy-lagrangian.md` — the earlier statements
- `popsci/angle-of-the-mirror.md`, `popsci/universes-other-half.md` — the popular framing
- `verify/battery.py`, `verify/toy_gw.py`, `scripts/check.sh` — what the gate does and does not check
