---
title: "Obituary: superheavy conjugate solitons"
weight: 10
status: dead
description: "What #14 claimed, how it was built and tested, why the corrected Kibble count overproduces the benchmark 2.1×10³–1.2×10⁴ times, the verdict, and what survives."
provenance: [V]
sources:
  - "papers/broken-born-checkpoint-v2.md §12"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Verdict'"
  - "review/round3-adjudication.md 'Rulings' 13"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "notes/knot-dark-matter-standalone.md Abstract"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
  - "verify/soliton_obituary.py"
  - "HANDOFF.md §2"
---

*Superheavy conjugate solitons were the third dark-matter candidate of version 2.0 of the checkpoint: magnetic monopoles of a hidden gauge sector, with a benchmark mass of 3×10¹³ GeV in the final version, stable because their field configuration cannot unwind and dark because no force of ordinary matter acts on them. The proposal was written up as the manuscript #14 and reviewed blind three times. The third review re-ran every number in code and found that the count of monopoles formed in the early universe had been normalized too low; corrected, the benchmark mass is overproduced by a factor of 2.1×10³ to 1.2×10⁴, and only a much lighter version survives, which is an existing published scenario that does not depend on the program. The candidate was retired on 2026-10-19 and stays dead.*

**Status:** Dead — "Retired as a program-native candidate" on 2026-10-19 (#11 §12; round-3 Decision 2). The numbers that killed it are [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)); the literature on the surviving low-scale scenario is live-searched [28S, 29S]. Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate) among [the dark-sector candidates](/wiki/dark-matter/candidates). The rulings are in [round-3 verdict and rulings](/wiki/method/review/round-3/rulings) and [round-3 decisions](/wiki/method/review/round-3/decisions); listed in [the graveyard](/wiki/status/graveyard).

## Key facts

- **What was claimed** (#11 §12): "v2.0 listed topological solitons of a p-local gauge sector (§11) as a third candidate, stable by topological charge. It also claimed they slip through the Debt-3 loophole (§9), since topology, not collective dynamics, would localize them in momentum" ([the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)). #14 v3's abstract: "The candidate is stable by topology, dark by sector separation, effectively collisionless, and inaccessible to direct detection."
- **How it was built and tested** (#11 §12): "The candidate was developed into a standalone proposal, #14, now in `notes/`: superheavy 't Hooft–Polyakov monopoles of a hidden SU(2) → U(1) sector" ([the hidden sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). "It was reviewed blind three times. Round 3, with code execution, returned verdict C, and arbitration upheld the central finding."
- **Why it failed** (#11 §12): "The Kibble estimate n/s = p (T_c/M_Pl)³ had been normalized at p = 1 (#14 v2) and p ≈ 0.023 (#14 v3)." "One defect per Hubble volume gives p ≈ 104 [V], and that is the causal minimum; Kibble–Zurek and bubble-nucleation production only add to it [28S]." "At minimum production the abundance closes at M ≈ 2.9–4.4×10¹² GeV [V], and the v3 benchmark of 3×10¹³ GeV is overproduced by 2.1×10³–1.2×10⁴ [V]." See [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) and [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction).
- **Why there is no rescue** (#11 §12): "Hidden-sector monopoles avoid overclosing the universe only for symmetry-breaking scales ≲ 100 PeV, or with a period of early matter domination [29S]." "Superheavy masses survive only with a free dilution factor. That removes the mass prediction, which was the candidate's reason to exist." Decision 2 rejected that route, a dilution "of at least 10³–10⁴ (ruling 2), probably far more (ruling 3)", because "the program does not trade falsifiability for survival" ([inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution)).
- **The verdict** (#11 §12): "Retired as a program-native candidate. The framework is compatible with the prior-art PeV-scale scenario and adds nothing testable to it." `CLAUDE.md`: "The framework is merely compatible with known PeV-scale topological dark matter (prior art)" ([topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).
- **What survives** (#11 §12): "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]" ([Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization)); "The minimal adjoint-only SU(2) → U(1) hidden sector is excluded on its own terms: its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V]" ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)); and the Debt-3 loophole "remains untested, but has no candidate". The adjudication's list adds "The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′ overclosure" ([benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)) and "The kinetic-mixing literature points (a) and (c)" ([kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)), with the compatibility theorem kept "as [T]", since re-credited to Freidel–Leigh–Minic ([the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)).
- **#14's own self-assessment** (§5–§6). It listed seven exclusion conditions and three "Requirements forced by consistency": "(i) at least one hidden doublet fermion with mass between the MeV scale and ~0.1 TeV", "(ii) a hidden-to-visible temperature ratio xi < 0.77 after reheating" and "(iii) an unbroken U(1)_d". Rulings 4–6 later moved the edges of (i) and the bound in (ii) ([the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window), [thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)). Its statement "All numerical statements in Secs. 2-4 were computed by executed code" was ruled an overstatement, "Upheld in substance": "The code checked the arithmetic of a wrong model" (ruling 13; [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).
- **Superseded framings.** The handoff, written before round 3, called these solitons the "Current best DM candidate" (DM: dark matter) at "~10¹³–10¹⁷ GeV" (`HANDOFF.md` §2; [the handoff](/wiki/history/documents/handoff)). The popular articles still present a three-way dark-matter question that includes "topological knots" ([the popular articles](/wiki/history/documents/popular-articles)). Neither is a status source.

## Sources

- `CLAUDE.md` 'Since the handoff' — "dead as a program-native proposal"; "merely compatible"
- `papers/broken-born-checkpoint-v2.md` §12 — the obituary: claim, test, failure, verdict, survivors, and the [V] tags
- `review/round3-adjudication.md` 'Verdict', 'Rulings' 13, 'What survives v3', 'Decisions' 2 — the review record and the retirement
- `verify/soliton_obituary.py` — the gated numbers
- `HANDOFF.md` §2 — the superseded "Current best" framing
- `notes/knot-dark-matter-standalone.md` Abstract, §5, §6 — the withdrawn manuscript's claims, exclusion conditions and requirements
