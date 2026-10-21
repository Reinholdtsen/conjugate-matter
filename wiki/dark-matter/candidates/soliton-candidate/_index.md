---
title: "The soliton candidate (retired)"
weight: 60
status: hub
description: "Superheavy 't Hooft–Polyakov monopoles of a hidden gauge sector, proposed as a third candidate in v2.0, written up as #14 (v1–v3), failed round 3 on its abundance arithmetic, and retired on 2026-10-19."
bookCollapseSection: true
---

*The soliton candidate was the proposal that dark matter consists of superheavy magnetic monopoles of a hidden gauge force: configurations of a hidden field that are topologically knotted and cannot unwind, so they would be stable without any further assumption. Version 2.0 of the checkpoint listed them as a third dark-matter candidate, and the idea was written up as a standalone manuscript, #14, for blind review. The third review recomputed every number with executed code and found that the estimate of how many monopoles the early universe forms had been too low by a factor of a hundred to several thousand; counted correctly, superheavy monopoles are made in far too great a number. The candidate was retired on 2026-10-19. This subsection records what was proposed, each component that failed and why, the results that survive, and the published scenario that the surviving low-mass version duplicates.*

**Stands:** [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction), [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure), and, as arithmetic conditional on the withdrawn benchmark, [benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic) and [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) · **Died:** [superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary), [the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector), [the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling), [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization), [the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor), [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window), [Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) · **Open:** nothing in this section

## Map

The record of the episode is the manuscript #14, `notes/knot-dark-matter-standalone.md`, in three versions, with checkpoint #11 §12 and the round-3 adjudication as its current summary.

- **Version 1** called the objects "knots". Round 1 of blind review graded it "B / medium" and renamed them "π₂ monopole-class" (`HANDOFF.md` §6).
- **Version 2**, "Superheavy Magnetic Solitons of a Spontaneously Broken Phase-Space Duality", set the hidden coupling by "the reciprocity map, acting as the modular S transformation", to "alpha_d = 1/(4 alpha) ~ 34", took the Kibble normalization at "p = O(1)" and used a benchmark "M = 1e16 GeV". It survives verbatim inside `review/skeptic-review-console.html`, the tool used for rounds 1 and 2. Round 2 graded it "B near B/C / medium" and left a pending list of seven items (`HANDOFF.md` §6).
- **Version 3** (commit 5dbaa82), "Dark Matter as Superheavy Monopoles of a Hidden Gauge Sector Selected by a Spontaneously Broken Phase-Space Duality", was cut from that list in `review/v3-worklog.md`, a chunked log of the round-2 items, new findings and Paul's decisions, which ends "This worklog is closed." v3 placed the monopole mass "at about 1e13 to 4e13 GeV with no dilution required". Round 3 graded it C on 2026-10-19. It was withdrawn the same day, moved from `papers/` to `notes/`, and given a banner: "Kept as the audit trail; not for circulation."

The pages below open with the death and the published scenario; the components follow, from the hidden sector and its coupling, through the abundance and the particles it forced, to the mixing with ordinary electromagnetism. Two pages are established literature ([prior art](/wiki/dark-matter/candidates/soliton-candidate/prior-art) and [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)), two are record, two are results that stand, and seven are obituaries.

[Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) comes first, because the death is the subject of the section: what #14 claimed, how it was tested, why the corrected count overproduces the benchmark 2.1×10³–1.2×10⁴ times, the verdict, and what survives.

[Topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art) is the established scenario the corrected candidate reduces to: hidden-sector monopoles as dark matter at low symmetry-breaking scales (Murayama–Shu; Liveoak–Maharana–Wells), with which the framework is "merely compatible".

[Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) is the sector #14 postulated: an adjoint Higgs field breaking SU(2)_d to U(1)_d, leaving heavy W′±, a massless hidden photon, stable monopoles, and a light fermion ψ. It is a standard model, dead as a program-native proposal.

[Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling) records the three attempts to fix the monopoles' coupling — Dirac quantization against our photon, reciprocity acting as modular S, and hypothesis H — and the factor-of-four convention spread.

[Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) is the error that killed the candidate: v3 used p ≈ 0.023 in the yield n/s = p (T_c/M_Pl)³, where one defect per Hubble volume, the causal minimum, gives p ≈ 104.

[Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) is the corrected result, which stands [V]: the abundance closes at M\* = 2.9–4.4×10¹² GeV, the 3×10¹³ GeV benchmark is overproduced 2.1×10³–1.2×10⁴ times, and realistic production adds more.

[Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) is a bound on the abundance that existed only in the claude.ai chat. It was dropped because its premise, the Kibble count as a ceiling, is inverted.

[W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) is a result that survives the candidate [V]: with no light charged fermion, the stable W′± overclose the universe by 10¹⁶–10¹⁷, which forced the addition of ψ.

[Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) is the mass range v3 allowed for ψ. Both edges were wrong: the upper by a miscount of states, the lower because MeV-scale ψ would freeze out during nucleosynthesis.

[The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) is record: the dark-radiation bound that requires a colder hidden sector, ξ < 0.760, its inconsistent use in v3, and the gravitational-wave band a first-order hidden transition would leave.

[Benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic) is record: densities, spacing, the self-interaction σ_T/M ~ 10⁻²⁶ cm²/g, and the counterfactual flux that shows why the hidden sector must be separate from ours.

[Kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) is the established literature on how a hidden photon can mix with ours: gravity-induced mixing and its protection, no visible magnetic flux while U(1)_d is unbroken, and the leakage channels that strict sector separation closes.

[Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) comes last: v3's dimension-5 estimate of the mixing, whose coefficient had no source. With it gone, the program took postulate P4 strictly.

## Boundaries

- General monopole physics is in [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles): [Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization), [the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole), [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism), [the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem) and [the flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches). The surviving claim that conjugate-sector monopoles, if they exist, gravitate is [conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles).
- The reviews are in [blind review](/wiki/method/review): [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two) and [review round 3](/wiki/method/review/round-3), with its [rulings](/wiki/method/review/round-3/rulings), [decisions and lessons](/wiki/method/review/round-3/decisions) and [arbitration](/wiki/method/review/round-3/arbitration). The numbers are checked by [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script).
- Early-universe background is in [early-universe cosmology](/wiki/cosmology/early-universe): [the radiation era](/wiki/cosmology/early-universe/radiation-era), [inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution) and [gravitational waves from phase transitions](/wiki/cosmology/early-universe/phase-transition-gravitational-waves).
- Strict sector separation is the postulate [P4](/wiki/program/postulates/p4-polarized-matter). The referees' consensus that "the framework does no work" is [its own page](/wiki/program/framework-does-no-work), and #14's acceptance criterion 1, the toy Lagrangian, is [acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion).
- The Debt-3 loophole the candidate once occupied is [the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole). Two open items raised during the episode sit with their subjects: [stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability) and [the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency).
- The two remaining candidates are in [dark-sector candidates](/wiki/dark-matter/candidates).
