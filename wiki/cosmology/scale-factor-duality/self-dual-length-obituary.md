---
title: "Obituary: the self-dual length as a program scale"
weight: 100
status: dead
description: "The self-dual length √(l_P L), 47–84 μm, tested as #13's Born length (a maximum force of 1.4×10⁻¹⁷ N, below the force inside a hydrogen atom) and as the range of the momentum graviton X in the aligned vacuum (excluded by torsion balances): both dead; the bound λ_X < 37.7 μm, M_X c² > 5.2 meV at background ratio u = 1 survives."
provenance: [D, V]
sources:
  - "papers/phase-space-diameter.md §8"
  - "papers/phase-space-diameter.md §8.1"
  - "papers/phase-space-diameter.md §8.2"
  - "papers/phase-space-diameter.md §8.5"
  - "papers/phase-space-diameter.md §8.6"
  - "papers/phase-space-diameter.md §9"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §7"
  - "papers/phase-space-diameter.md §1"
  - "verify/phase_space_diameter.py 'Consequences (note §8)'"
  - "review/round5-adjudication.md 'Rulings' R1, R12, R16"
  - "review/round5-adjudication.md 'Pre-registration scored'"
  - "review/round5-adjudication.md 'Lessons (into CLAUDE.md)'"
  - "review/round5-preregistration.md 'Predictions'"
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §2"
  - "CLAUDE.md 'Since the handoff'"
  - "CLAUDE.md 'Method'"
  - "review/wiki-build-flags.md item 39"
---

*This page records two uses of one length that the program's phase-space-diameter note tested and excluded. The [self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box), the range of scales from the Planck length to the size of the universe, is mapped onto itself by [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) for one reference length, √(l_P L), between 47 and 84 micrometres. The program has one exact reciprocity and so one [Born length](/wiki/phase-space/reciprocity/born-length), and a Born length enters it in two places: the [maximum force](/wiki/conjugate-relativity/maximum-force) of its dual special relativity, and the range of the massive [momentum graviton X](/wiki/gravity/momentum-graviton), whose force on ordinary matter has the strength of gravity. At the self-dual length the maximum force would be 1.4×10⁻¹⁷ newtons, which the electric force inside a hydrogen atom exceeds by a factor of 5.8×10⁹, and X would exert a gravitational-strength force at a range where laboratory torsion balances have looked for one and found none. Both uses are dead. The second leaves a bound: in the vacuum the program's own equations assume, X's range is below 37.7 micrometres.*

**Status:** Dead — [D][V] for the maximum force; [D][V] with live-searched measurements [S] for the range, in the aligned vacuum (bimetric background ratio u = 1) — `papers/phase-space-diameter.md` §8.1–§8.2 and §9, with every number printed by `verify/phase_space_diameter.py` ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)). The note was graded B by both referees of [round 5](/wiki/method/review/round-5), whose shared weakest link was the background ratio missing from the range argument; version 1.1 states it. Filed in [the graveyard](/wiki/status/graveyard).

## What was proposed

The self-dual length belongs to the literature. It is the cutoff of Cohen, Kaplan and Nelson's bound on field theory in a box the size of the universe, and the cell length of the Born-geometry papers of Freidel–Kowalski-Glikman–Leigh–Minic (FKGLM), who let it depend on the system under study ([the length in the literature](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box#the-length-in-the-literature-t)). The note asked whether the program could adopt it as a scale of its own, and its answer opens:

> "FKGLM let their reference length depend on the system under study. This program cannot: its reciprocity is one exact symmetry with one Born length. That length could enter in two places." (§8, plain-language passage)

The two identifications it tested:

1. **The Born length of the dual special relativity.** The program's paper on [conjugate special relativity](/wiki/conjugate-relativity), #13, bounds every rate of change of momentum by c̃ = ħc/λ² and sets λ equal to the Planck length "in one untagged sentence" (note §5; #13 §1). The candidate was λ = √(l_P L).
2. **The range of X.** X is a massive spin-2 field whose mass M_X is the program's polarization-breaking scale, "with no value in the record" (§8.2). The candidate was a range ħ/(M_X c) equal to √(l_P L).

No program document before the note mentions the length (the wiki's search of the record); the note raised both identifications and excluded both.

## How it was tested

### As the Born length: the maximum force [D][V]

The bound c̃ = ħc/λ² (#13 §1) evaluated at the two lengths (§8.1):

```text
λ = l_P:          c̃ = c⁴/G = 1.21×10⁴⁴ N
λ = √(l_P L):     c̃ = (c⁴/G)(l_P/L) = 1.4×10⁻¹⁷ N    (L = c/H₀)
                                     1.2×10⁻¹⁷ N    (L = L_Λ)
```

Ordinary forces exceed the second value by large factors: the Coulomb force in the hydrogen ground state, 8.24×10⁻⁸ N, by 5.8×10⁹, and the weight of a kilogram by 6.9×10¹⁷ (§8.1). In #13 forces do not simply add. Its composition law,

```text
F₁ ⊕ F₂ = (F₁ + F₂)/(1 + F₁F₂/c̃²)        (#13 §2)
```

combines forces as special relativity combines velocities, so that no combination passes c̃ ([force composition](/wiki/conjugate-relativity/force-boosts#force-composition-d)). With c̃ near 10⁻¹⁷ N the law "would cap every force near 10⁻¹⁷ N", and the note concludes: "The self-dual length cannot be that Born length." (§8.1)

The note also sets out where a Born length comes from in the literature (§8.1). In the metastring theory of Freidel, Leigh and Minic, ħ = λε and Newton's constant is G_N = ρα′ = ρλ/ε, with ρ set by the dimension and the compactification, so λ² = ħG_N/ρ is the Planck length squared up to ρ [S: Freidel–Leigh–Minic 2015]. A maximal force from Born reciprocity is itself in the literature: Low's reciprocal relativity bounds forces by a constant b [S: Low 2006]. #13 cites Gibbons's maximum-tension conjecture and Caianiello's maximal acceleration for the idea, from model memory (†) ([maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)). The root `CLAUDE.md` lists Low 2006 among the leads of the note's literature sweep, not queued, as prior art for #13's maximum force.

### As the range of X: torsion balances [D][V][S]

**The coupling.** Reciprocity forces the two spin-2 frames of the program to have equal Planck masses ([equal Planck masses](/wiki/gravity/momentum-graviton/spectrum-and-parity#equal-planck-masses)), so ordinary matter, coupled to the metric g, feels X at gravitational strength. It is safe only because X's force is cut off beyond ħ/(M_X c) (§8.2; [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)). In [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) with matter on g, the potential between two masses is Newton's with a [Yukawa](/wiki/gravity/spin-2-fields/yukawa-forces) term added (§8.2):

```text
V(r) = −(G m₁ m₂ / r) (1 + α e^(−r/λ_X)),        α = (4/3) (M_f u / M_g)²
```

Here u is the ratio of the two frames' backgrounds, f̄ = u²ḡ (written c in the cited papers), and the 4/3 comes from the massive field's extra polarizations [S: Lüben, Mörtsell and Schmidt-May 2020, eq. 9; Enander–Mörtsell 2013, eq. 4.1; V]. Equal Planck masses give α = 4/3 only if u = 1. The program's vacuum is the aligned point, u = 1, where its vacuum-energy identity holds; the argument for that vacuum and the questions it leaves open are on [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound).

**Screening.** A massive graviton's extra force is suppressed near a body, inside its Vainshtein radius, by the field's nonlinear self-interaction [T]. For a range of order 50 μm, laboratory test masses are far outside their Vainshtein radii, "about 10⁻¹² m for a kilogram", so the force is unscreened [D][V] (§8.2).

**The measurement.** Torsion-balance tests of the inverse-square law limit "any gravitational-strength Yukawa interactions to ranges <38.6 μm" at 95% confidence [S: Lee et al. 2020]. X's Yukawa force is attractive, so the note uses the one-sided +α₉₅ column of the experiment's exclusion table, which at α = 4/3 gives λ_X < 37.7 μm [S: Lee 2020 thesis, Table 11.4; V] (§8.2).

**The verdict.** The self-dual length, 47.1 μm for the Hubble radius and 84.0 μm for the particle horizon, lies above that limit, so in the aligned vacuum it is excluded. It would be allowed only for u < 0.67 (47.1 μm) or u < 0.30 (84.0 μm) [V] (§8.2). The test is an old one: "a gravitational-strength modification of gravity at the dark-energy length was proposed to address the cosmological-constant problem [S: Sundrum 2004], and torsion balances were aimed 'below the dark-energy length scale' to look for it [S: Kapner et al. 2007]" (§8.2).

## Why it failed

The note's summary table (§9):

| Identification | Status | Tag |
| --- | --- | --- |
| λ = √(l_P L) as the dual-relativity Born length | excluded: c̃ = 10⁻¹⁷ N | [D][V] |
| λ = √(l_P L) as X's range | excluded by torsion balances in the aligned vacuum; allowed only for background ratio u < 0.67 | [D][V][S] |

The two failures are independent. The first follows from #13's own formula and ordinary forces, from the force inside a hydrogen atom to the weight of a kilogram. The second follows from the bimetric coupling at u = 1 and a published torsion-balance limit.

## What survives

- **A bound on X's range.** In the aligned vacuum (u = 1, α = 4/3), λ_X < 37.7 μm and M_X c² > ħc/(37.7 μm) = 5.2 meV [V][S]. For other background ratios the limit moves: 57.0 μm at u = 0.5, 42.5 μm at u = 0.8, 30.8 μm at u = 1.5 [V]. "The polarization-breaking scale lies at least 2.3 times above the dark-energy scale of 2.24 meV." (§8.2) The record's statement that gravitational-strength short-range forces are "experimentally unconstrained down to far below any plausible M_X" (calc note #8 §3) "is consistent with the bound but gave no number" (§8.2). The bound, its premise and its caveats are on [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound).
- **Its premise.** The note's summary lists "The program's vacuum has u = 1" as "the only proportional vacuum with zero wedge vacuum energy; persistence under expansion open" [D][V][O] (§9). How reciprocity's action as the exchange of the two frames relates to its action Z → −Z⁻¹ on the modular field is open in the record (§8.2; flag 39 in `review/wiki-build-flags.md`). The bound also assumes that X adds the only Yukawa term (§8.2).
- **#13's choice of the Planck length.** The program's action singles out no Born length [D] (§5), and #13's λ = l_P remains "an untagged choice" (§9). At that value the cosmic box is far from self-dual: "A = L/l_P = 8.5×10⁶⁰ for the Hubble radius, and the cosmological-constant problem is the size of that number squared" (§8.1; [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem)).
- **The self-dual box itself**, as a restatement of published results and of the Friedmann equation: [the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box).
- **The test.** "The bound of §8.2 tightens with every improvement in short-range gravity tests." (§8.6)

## Open: a lever arm

The note keeps one consequence of the Born length open [O] (§8.5). The program identifies its dark-energy field τ with the angle of the vacuum's polarization ([τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)), and in its coset toy model the polarization angle and the squeeze along the slice are separate flat directions ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). "Whether matter's polarization follows the vacuum's as τ drifts is not settled." If it does, a rotation of the polarization by θ displaces a particle of momentum p by θλ²p/ħ [V]:

```text
displacement per radian, an electron at the Bohr momentum:
  λ = l_P:             4.9×10⁻⁶⁰ m
  λ = √(l_P c/H₀):     42 m
```

The note concludes: "A cosmological drift of τ would then be harmless only for a Born length near the Planck length." (§8.5) The item turns on a question the record leaves open, whether matter's polarization follows the vacuum's. A related reading, τ's present-day thawing as a slow drift of the polarization angle, is recorded as a conjecture of the toy-model worklog ([the thawing of dark energy as a drifting polarization angle](/wiki/symmetry-breaking/goldstone-angle#conjecture-the-thawing-of-dark-energy-as-a-drifting-polarization-angle)). The program's open items are collected in [open problems and the queue](/wiki/status/open-problems).

## Where it is filed

- Home section: [Scale-factor duality](/wiki/cosmology/scale-factor-duality), beside [the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box).
- The calculations that killed it: `papers/phase-space-diameter.md` §8.1–§8.2, gated in `verify/phase_space_diameter.py` ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)); the review that repaired the range argument: [round 5](/wiki/method/review/round-5), ruling R1.
- The pages it concerns: [the Born length λ](/wiki/phase-space/reciprocity/born-length), [the maximum force](/wiki/conjugate-relativity/maximum-force), [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound).
- The register of dead claims: [the graveyard](/wiki/status/graveyard).
- How the program treats dead claims: [negative results and dead claims](/wiki/method/negative-results).

## History

- **2026-10-26, version 1.0 of the note.** Both identifications were raised and excluded, with the range bound resting on "α = 4/3 at equal Planck masses" (round-5 ruling R1).
- **The pre-registration.** It named the bound in §8.2 as the weakest link, because it "inherits the program's own, unreviewed premise that X couples to ordinary matter at gravitational strength (equal Planck masses, α = 4/3)" (`review/round5-preregistration.md`).
- **Round 5.** Both referees found that the cited coupling formula carries the background ratio and that the note had dropped it. Ruling R1: "Upheld in substance; referee A's value of c not upheld". Referee A had set the ratio from a·ã = 1, which gave α ~ 10⁻¹⁸⁶; the adjudicator ruled that "The record's second frame is the polarization frame, not the slaved momentum block g̃ = g⁻¹ that carries ã, so that value does not follow." The adjudication scored the pre-registered weakest link a hit "on location and premise; the mechanism, a dropped parameter of the cited formula, was not foreseen". Ruling R12 asked the note to say which column of the exclusion table it uses, and R16 added the caveats.
- **Version 1.1** (2026-10-26). It states u = 1 and the argument for it, gives the bound as a function of u, names the column (the attractive, one-sided limit, "which is the more conservative", ruling R12), and adds the caveats. The adjudication carried a method rule into the root `CLAUDE.md`: "When a result rests on a formula from the literature, carry every parameter the cited formula has and state what fixes each one."

## Sources

- `papers/phase-space-diameter.md` §8 — the plain-language passage: one exact reciprocity with one Born length, and the two places it could enter
- `papers/phase-space-diameter.md` §8.1 — the maximum force at the self-dual length, the forces it is compared with, the composition law, the metastring and Low 2006; A = L/l_P at λ = l_P
- `papers/phase-space-diameter.md` §8.2 — the coupling with its background ratio u, the screening estimate, the torsion-balance limit and its column, the bound as a function of u, Sundrum 2004 and Kapner et al. 2007, the caveats
- `papers/phase-space-diameter.md` §8.5 — the lever arm [O]; §8.6 — what would test the bound
- `papers/phase-space-diameter.md` §9 — the summary table and its tags
- `papers/phase-space-diameter.md` §5, §7 — the program fixes no λ; the self-dual length
- `papers/phase-space-diameter.md` §1 — the abstracts
- `verify/phase_space_diameter.py` — section "Consequences (note §8)"
- `review/round5-adjudication.md` 'Rulings' R1, R12, R16 — the background ratio, the column, the caveats; 'Pre-registration scored'; 'Lessons (into CLAUDE.md)'
- `review/round5-preregistration.md` 'Predictions' — the weakest link named before the review
- `papers/conjugate-special-relativity.md` §1, §2 — c̃ = ħc/λ², the Planck identification and the composition law
- `CLAUDE.md` 'Since the handoff' — the result and the leads; 'Method' — the rule from round 5
- `review/wiki-build-flags.md` item 39 — the two actions of reciprocity on the spin-2 sector, awaiting Paul's ruling
