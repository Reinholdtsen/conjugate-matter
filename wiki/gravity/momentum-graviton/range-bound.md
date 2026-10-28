---
title: "The laboratory bound on X's range"
weight: 95
status: alive
description: "In the program's aligned bimetric vacuum (background ratio u = 1) X acts on ordinary matter with Yukawa strength α = 4/3, and torsion balances then require λ_X < 37.7 μm, M_X c² > 5.2 meV; why the couplings single out that vacuum, what it leaves open, how the bound moves with u, and its caveats."
provenance: [D, V, S]
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/phase-space-diameter.md §8.2"
  - "papers/phase-space-diameter.md §8"
  - "papers/phase-space-diameter.md §8.1"
  - "papers/phase-space-diameter.md §1"
  - "papers/phase-space-diameter.md §7"
  - "papers/phase-space-diameter.md §8.6"
  - "papers/phase-space-diameter.md §9"
  - "papers/phase-space-diameter.md 'References'"
  - "review/round5-adjudication.md 'Verdict'"
  - "review/round5-adjudication.md 'Rulings' R1, R12, R16"
  - "review/round5-adjudication.md 'Pre-registration scored'"
  - "review/round5-adjudication.md 'Revisions for v1.1'"
  - "review/round5-preregistration.md 'Predictions'"
  - "review/round5/manuscript-v1.0.md §8.2"
  - "verify/phase_space_diameter.py 'Consequences (note §8)'"
  - "review/round5/adjudicator/arb.out A1/B1, B9"
  - "review/round5/adjudicator/arb.py"
  - "review/round5/referee-A/scripts/lee_interp.py"
  - "review/round5/referee-A/outputs/lee_interp.txt"
  - "review/round5/referee-B/outputs/torsion_interp.txt"
  - "review/round5/referee-B/audit-notes.md §4.5"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "review/v3-worklog.md 'Round-2 pending list' R7"
  - "review/wiki-build-flags.md item 39"
  - "notes/closed-universe.md §6"
  - "review/wiki-build-flags.md item 51"
---

*The laboratory bound on X's range is an upper limit on the distance over which the program's [momentum graviton X](/wiki/gravity/momentum-graviton) can pull on ordinary matter: 37.7 micrometres, which puts X's mass above 5.2 meV. X is a massive spin-2 field, so the force it adds to gravity between two bodies is a [Yukawa force](/wiki/gravity/spin-2-fields/yukawa-forces), which dies away beyond a range set by the field's mass. Its strength depends on the Planck masses of the program's two spin-2 frames, which [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) makes equal, and on the ratio of the two frames' backgrounds, which is one in the aligned vacuum the program's own equations assume. In that vacuum the extra force is 4/3 as strong as gravity at short distances, and torsion balances, which have looked for such a force between test masses tens of micrometres apart and found none, exclude it at ranges above 37.7 micrometres. The same data exclude a range set by the self-dual length of about 50 micrometres. The bound is the one new number of the [phase-space-diameter note](/wiki/cosmology/scale-factor-duality/phase-space-diameter) (§8.2); before it, no document put a number on X's mass, and none gives it a value. It is machine-checked, it was revised after a blind review, and it holds only for the aligned vacuum, whose persistence as the universe expands is open.*

**Status:** Alive — [D][V][S] in the phase-space-diameter note v1.1 §8.2, whose summary table tags the bound itself [V][S]; the premise u = 1 is [D][V] and its persistence as the universe expands [O]; the caveats are [T][O]. Every number the note gives for the bound is recomputed by `verify/phase_space_diameter.py` ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)); the further values quoted here from the round-5 records come from the review's own scripts, which are outside the gate. The note received verdict B in [review round 5](/wiki/method/review/round-5), whose referees found the background ratio missing from the bound's first version; v1.1 states it.

## The bound

The phase-space-diameter note §8.2, for the aligned vacuum [V]:

```text
λ_X < 37.7 μm,     M_X c² > ħc/(37.7 μm) = 5.2 meV
```

Here λ_X = ħ/(M_X c) is the range of X's force, the reduced Compton wavelength of its quanta, and M_X is X's mass. [Checkpoint #11](/wiki/history/documents/checkpoint) identifies M_X with the polarization-breaking scale and gives it no value (#11 §7; [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)). The bound combines three things, taken in turn below: the strength of X's force on ordinary matter, the premise that fixes that strength, and the torsion-balance data.

## The strength of X's force

### The Yukawa form [T]

Ordinary matter couples to the metric g. In [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) with matter on g, the potential between two masses m₁ and m₂ a distance r apart, to first order in the fields, is (note §8.2, citing Lüben, Mörtsell and Schmidt-May 2020, eq. 9 [S], and Enander and Mörtsell 2013, eq. 4.1 [S]):

```text
V(r) = −(G m₁ m₂ / r) · (1 + α e^(−r/λ_X))
α    = (4/3) (M_f u / M_g)²
```

- **M_g and M_f** are the Planck masses of the two metrics g and f, the coefficients of their Einstein–Hilbert terms ([two metrics, two Planck masses](/wiki/gravity/spin-2-fields/planck-units#two-metrics-two-planck-masses)).
- **u** is the ratio of the two backgrounds about which the fields are expanded, f̄ = u²ḡ. The cited papers write it c, as do the [Hassan–Rosen page](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric#the-spectrum-t) and the round-5 records; the note writes u to keep it apart from the speed of light, and so do the verify script's labels and this page.
- **The 4/3** "comes from the massive field's extra polarizations" (note §8.2). Between two static bodies, a massless graviton's exchange carries the tensor factor 1 − 1/2 and a massive spin-2 field's carries 1 − 1/3, because the massive field's helicity-zero polarization also couples to the trace of the source's stress-energy [T]; their ratio is 4/3, which the script checks. This is the van Dam–Veltman–Zakharov factor of [a massive spin-2 mediator](/wiki/gravity/spin-2-fields/yukawa-forces#a-massive-spin-2-mediator), and the five polarizations are those of [the Fierz–Pauli field](/wiki/gravity/spin-2-fields/fierz-pauli).

The term with α is the force of the massive field, X; the 1 is the massless graviton's. X's force is attractive, as the exchange of any spin-2 field between masses is.

### What fixes the strength

"Only the product M_f u is fixed by the theory, so equal Planck masses give α = 4/3 only if u = 1" (note §8.2). Reciprocity, acting on the spin-2 sector as the exchange of the two frames, sets M_f = M_g ([calc note #8](/wiki/history/documents/debt-1-notes) §3; [equal Planck masses](/wiki/gravity/momentum-graviton/spectrum-and-parity#equal-planck-masses)). That leaves α = (4/3)u², and the bound depends on the value of u in the program's vacuum.

## The premise: the aligned vacuum, u = 1

### The program's vacuum

The program's second frame is the polarization frame f = E₀[J], built from the polarization J that the vacuum selects ([constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)). Its vacuum is the aligned point 𝕏 = √(g⁻¹f) = 1, where g⁻¹f is the unit matrix, the two frames coincide, and [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity#the-potential-and-the-aligned-point) holds (#8 §1–§2). At that point the two backgrounds are equal, u = 1 (note §8.2).

### Why that vacuum and no other [D][V]

The program's couplings single out the aligned vacuum (note §8.2). They obey [the palindrome](/wiki/gravity/palindromic-branch/palindrome) βₙ = β₄₋ₙ, and with them the proportional backgrounds solve

```text
u (u − 1) (u + 1) (β₁u² + (3β₂ − β₀)u + β₁) = 0
```

The root u = 1 is the aligned vacuum. On the program's flat branch, β₀ = −4β₁ − 3β₂, where the aligned vacuum is flat and its wedge vacuum energy vanishes ([the four lines](/wiki/gravity/palindromic-branch/vacuum-energy-identity#the-four-lines)), the other solutions are a pair (u, 1/u) that breaks the frame exchange. Such a pair exists only for β₁ < 0 < |β₁| < β₂, and there the bimetric vacuum energy is of the order of the spin-2 mass squared, "some 10⁶¹ times H₀² for M_X c² ≥ 5 meV", H₀ being today's Hubble rate. The round-5 arbitration script gives an example: at β₁ = −1, β₂ = 2 the pair sits at u = 0.127 and u = 7.873, where the g-metric's vacuum energy is −1.14 and −70.9 in units of 2(β₁ + β₂), the combination to which the squared spin-2 mass is proportional (`review/round5/adjudicator/arb.out`, A1/B1; ruling R1). Only the aligned vacuum is compatible with the observed [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant). The note states when the broken vacua exist but not that the branch needs β₁ > 0; the closed-universe note of 2026-10-27 finds that it does: for β₁ = 0 the aligned branch is bounded, and for β₁ < 0 it ends at a broken vacuum with negative Λ_g and violates the Higuchi bound, every broken vacuum having Λ_g = −3m²(β₁ + β₂)(u − 1)² (flag 51 in `review/wiki-build-flags.md`; [the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe#β--0-is-required-dv)). The note's summary table records the premise as "the only proportional vacuum with zero wedge vacuum energy; persistence under expansion open" [D][V][O] (§9).

### What a·ã = 1 does not fix

The program's cosmology has its own reciprocal pair, the scale factor a and its momentum-space counterpart ã, tied by [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint). That pair belongs to a different object. "The second frame is not the slaved momentum block g̃ = g⁻¹ that carries ã, so a·ã = 1 does not fix u" (note §8.2; [the slaved momentum metric](/wiki/phase-space/born-geometry/compatibility-corollaries#corollary-3-the-slaved-momentum-metric)). In round 5, referee A had set u from it, u = ã/a today, which gave α ~ 10⁻¹⁸⁶ and no laboratory bound at all; the adjudication did not uphold that value, for this reason (ruling R1; `review/round5/referee-A/outputs/lee_interp.txt`).

### Unscreened at these ranges [D][V]

In massive gravity the nonlinear self-interactions of the helicity-zero polarization suppress the extra force inside a distance around each source called its Vainshtein radius; outside it, the potential above holds [T]. "For a range of order 50 μm, laboratory test masses are far outside their Vainshtein radii (about 10⁻¹² m for a kilogram), so the force is unscreened" (note §8.2).

### Open: two points the premise leaves [O]

The note leaves two points open (§8.2):

- **Persistence.** "Whether the aligned point persists as the universe expands is not settled, since E₀[J] lies on a compact moduli space" (here the note cites calc note #7 §4) "and so, on this note's reading, carries no scale of its own." Calc note #7 §4 says that E₀[J] is confined to a compact moduli space, [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian); that the space therefore carries no scale is the note's reading, not #7's. The root `CLAUDE.md` lists the question among the leads of the note's literature sweep, not on the work queue ('Since the handoff'). The closed-universe note, taking f as a dynamical field at equal Planck masses, finds the ratio of the two scale factors within 1 − y = 1.5×10⁻⁶¹ of alignment today at the smallest allowed M_X, and finds that a frozen f admits no expanding universe and contradicts the record's equal Planck masses; it leaves the definition of E₀[J] open, as ruling R1 does ([the momentum graviton in a closed universe](/wiki/gravity/momentum-graviton/closed-universe)).
- **Which action of reciprocity.** "How reciprocity's action as this frame exchange relates to its action Z → −Z⁻¹ on the modular field is open in the record" ([reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion); [two actions of reciprocity](/wiki/gravity/momentum-graviton/spectrum-and-parity#two-actions-of-reciprocity); flag 39 in `review/wiki-build-flags.md`, awaiting Paul's ruling). Ruling R1 records the same open question and adds that "v1.1 says so rather than ruling the identification out".

## The data: torsion balances

### The experiment

A torsion balance measures the tiny torque that nearby masses exert on a pendulum hung from a thin fibre, and it is how the inverse-square law is tested in the laboratory at short separations [T] ([how experiments test it](/wiki/gravity/spin-2-fields/yukawa-forces#how-experiments-test-it)). The note uses the experiment of Lee, Adelberger, Cook, Fleischer and Heckel, "New test of the gravitational 1/r² law at separations down to 52 μm" (2020) [S]. Its authors limit "any gravitational-strength Yukawa interactions to ranges <38.6 μm" at 95% confidence, and they draw the conclusion for a "heavy graviton" of bimetric gravity, citing Aoki and Mukohyama 2016 [S]: its mass "must be greater than 5.1 meV" (note §8.2). The script checks that 5.1 meV is ħc/(38.6 μm).

### Which column of the table

The experiment's exclusion table, in Lee's thesis (Table 11.4) [S], gives at each range the largest Yukawa strength the data allow at 95% confidence. It has a column for an attractive term, +α₉₅, which is a one-sided limit, and a column for a term of either sign, |α₉₅|, which is two-sided (referee A's transcription also carries the repulsive column, −α₉₅; `review/round5/referee-A/scripts/lee_interp.py`). "X's Yukawa force is attractive, so the relevant limit is the one-sided +α₉₅ column", which at α = 4/3 gives λ_X < 37.7 μm (note §8.2). It is also the more conservative of the two (ruling R12). The two-sided column reproduces the published limits, 38.6 μm at |α| = 1 and 30 μm at α = 8/3, "and so checks the transcription and the interpolation"; at α = 4/3 it gives the stronger 35.8 μm (note §8.2).

The two columns at three strengths, from the round-5 arbitration (`review/round5/adjudicator/arb.out`, B9):

| α | one-sided +α₉₅ | two-sided \|α₉₅\| |
| --- | --- | --- |
| 1 | 40.66 μm | 38.63 μm |
| 4/3 | 37.68 μm | 35.79 μm |
| 8/3 | 31.69 μm | 30.23 μm |

The 38.63 and 30.23 μm are the published 38.6 and 30 μm; the 37.68 μm is the note's 37.7 μm.

## How the bound moves with u

"For another background ratio the limit is the table's value at α = (4/3)u²: 57.0 μm at u = 0.5, 42.5 μm at u = 0.8, 30.8 μm at u = 1.5" [V] (note §8.2). The round-5 arbitration tabulates it, in the one-sided column, with the corresponding mass (`review/round5/adjudicator/arb.out`, A1/B1):

| u | α = (4/3)u² | λ_X below | M_X c² above |
| --- | --- | --- | --- |
| 0.50 | 0.333 | 57.0 μm | 3.46 meV |
| 0.67 | 0.599 | 47.2 μm | 4.18 meV |
| 0.80 | 0.853 | 42.5 μm | 4.64 meV |
| 1.00 | 1.333 | 37.7 μm | 5.24 meV |
| 1.25 | 2.083 | 33.6 μm | 5.87 meV |
| 1.50 | 3.000 | 30.8 μm | 6.40 meV |

The note quotes the u = 1 row as 37.7 μm and 5.2 meV. A smaller background ratio weakens X's coupling to ordinary matter and lets its range be longer; a larger one strengthens it.

## What follows

### X at the self-dual length is excluded

The self-dual length √(l_P L), with l_P the Planck length and L a cosmological length, is the one Born length for which the Fourier box [l_P, L] × [ħ/L, ħ/l_P] maps onto itself under reciprocity: 47–84 μm for L between the Hubble radius and the particle horizon ([the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box)). "In the aligned vacuum an X set by the self-dual length, at 47–84 μm, is excluded; it would survive only for u < 0.67 (47.1 μm) or u < 0.30 (84.0 μm)" [V] (note §8.2). In the aligned vacuum the identification of that length with X's range is dead. Its use as the Born length of the program's dual special relativity is dead whatever u is, because of the maximum force it would give (§8.1; [Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)).

### X's mass lies above the dark-energy scale

The note draws a second consequence, which holds in the aligned vacuum: "The polarization-breaking scale lies at least 2.3 times above the dark-energy scale of 2.24 meV" (note §8.2), the dark-energy scale being the fourth root of the dark-energy density (§7). The script computes the factor from the bound at α = 4/3.

### The test is an old one

"A gravitational-strength modification of gravity at the dark-energy length was proposed to address the cosmological-constant problem [S: Sundrum 2004], and torsion balances were aimed 'below the dark-energy length scale' to look for it [S: Kapner et al. 2007]" (note §8.2; [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem)). The bound "tightens with every improvement in short-range gravity tests" (§8.6).

### The record's range argument, with a number

Calc note #8 §3 had said that "gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X" ([safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)). The note finds that statement "consistent with the bound but gave no number" (§8.2). The bound is the number, for the aligned vacuum.

## Caveats [T][O]

The note lists three (§8.2), accepted from both referees in round 5 (ruling R16):

- **Vacuum energy.** "In bigravity a spin-2 field far heavier than H₀ at equal Planck masses needs the potential's vacuum energy, of order M_X²M_P², cancelled"; in the program the cancellation is the vacuum-energy identity of [the palindrome](/wiki/gravity/palindromic-branch/palindrome) at the aligned point ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)).
- **The early universe.** "Bimetric cosmologies are unstable while H exceeds the spin-2 mass" [S: Lüben et al. 2020], "so the early universe is a separate question, open in the record" ([bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology); [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability); `review/v3-worklog.md` item R7).
- **One Yukawa term.** "The bound assumes that X adds the only Yukawa term; other light fields of the program could add attractive or repulsive ones."

## In review

[Round 5](/wiki/method/review/round-5) reviewed version 1.0 of the note, blind, with two referees.

- **The prediction.** The pre-registration named this bound as the weakest link: it "inherits the program's own, unreviewed premise that X couples to ordinary matter at gravitational strength (equal Planck masses, α = 4/3)" (`review/round5-preregistration.md`, 'Predictions').
- **The finding.** Both referees found the gap there. Version 1.0 wrote α = (4/3)(M_f/M_g)² and "At equal Planck masses α = +4/3" (`review/round5/manuscript-v1.0.md` §8.2), which drops the background ratio that both cited formulas carry, so the bound held only for u = 1, which the note did not state (ruling R1). The adjudication upheld the finding in substance and scored the prediction a hit "on location and premise; the mechanism, a dropped parameter of the cited formula, was not foreseen". Referee A's value of u was not upheld (above).
- **The repair.** Version 1.1 states u and the argument for u = 1, gives the bound as a function of u and the values below which X at the self-dual length survives, says which column it uses and why, records the two open points and that the second frame is not the slaved momentum block, adds the caveats, and carries the condition u = 1 into its abstracts, the opening of §8 and the summary (revision 1 of 'Revisions for v1.1'). The root `CLAUDE.md` took the lesson into its method: "When a result rests on a formula from the literature, carry every parameter the cited formula has and state what fixes each one."
- **Other checks.** Referee B found no stronger constraint at these ranges: a 2026 review (arXiv:2605.18212) names the 2020 limits of the University of Washington and of the Huazhong University of Science and Technology as still the tightest (`review/round5/referee-B/audit-notes.md` §4.5). Referee B's own interpolation of the thesis table gives 37.68 μm on logarithmic axes and 38.08 μm on linear ones at α = 4/3 in the one-sided column (`review/round5/referee-B/outputs/torsion_interp.txt`).

The verdict on the note as a whole was B from both referees, confidence 0.75 ('Verdict').

## Verification

`verify/phase_space_diameter.py` recomputes every number the note gives for the bound and runs in [the gate](/wiki/method/verification/the-gate) ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)). It codes the rows of Table 11.4 that bracket the crossings and interpolates between neighbouring rows on logarithmic axes. The rows of the u table above that the note does not quote (u = 0.67 and 1.25), the masses in that table, the two-column table and the roots u = 0.127 and 7.873 of the broken-vacuum example come from the round-5 arbitration script `review/round5/adjudicator/arb.py` (output in `review/round5/adjudicator/arb.out`), and the interpolation comparison from referee B's script; neither is part of the gate. The gate's own output, below, includes four of the two-column table's six values (38.63, 30.23, 37.68 and 35.79 μm), and its first sampled coupling is the example's β₁ = −1, β₂ = 2, whose two vacuum energies, −1.143 and −70.857, it prints. The gate script's output for this section:

```text
PASS  anchor: the interpolation reproduces Lee et al.'s published 38.6 um (|alpha| = 1) and 30 um (alpha = 8/3)  [38.63, 30.23 um]
PASS  attractive Yukawa with alpha = 4/3 (one-sided +alpha95): lambda_X < 37.7 um, M_X c^2 > 5.2 meV  [37.68 um, 5.237 meV]
PASS  Lee et al.'s 5.1 meV is hbar c/38.6 um
PASS  the two-sided |alpha95| column gives the stronger 35.8 um at alpha = 4/3  [35.79 um]
PASS  for background ratio u (alpha = 4u^2/3; c in the cited papers): 57.0 um at u = 0.5, 42.5 at 0.8, 30.8 at 1.5  [[56.98, 42.53, 30.83]]
PASS  X at the self-dual length survives only for u < 0.67 (47.1 um) or u < 0.30 (84.0 um)  [[0.6717, 0.3017]]
PASS  proportional backgrounds of the palindromic theory: u(u - 1)(u + 1)(beta1 u^2 + (3 beta2 - beta0) u + beta1) = 0
PASS  on the flat branch the symmetry-breaking pair (u, 1/u) exists only for beta1 < 0 < |beta1| < beta2 (sampled), with vacuum energy of order the spin-2 mass squared  [[[-1.143, -70.857], [-1.387, -934.613], [-0.632, -5.128]]]
PASS  so X at the self-dual length (47-84 um) is excluded, and M_X exceeds the dark-energy scale by 2.3x
PASS  (arithmetic of the cited propagators) the 4/3: massive (1 - 1/3) over massless (1 - 1/2) tensor structure
PASS  Vainshtein radius of a 1 kg test mass for a 50 um range: about 1e-12 m  [1.95e-12 m]
```

What these checks cover:

- **The anchor is independent of the note.** The interpolation must reproduce the two limits Lee et al. published, which no program document produced ([independent anchors](/wiki/method/verification/independent-anchors)). Both columns come from the same table, so the anchor on the two-sided column checks the transcription and the method used for the one-sided column that gives the bound (ruling R12).
- **The broken vacua are sampled.** The check that the pair (u, 1/u) exists only for β₁ < 0 < |β₁| < β₂ evaluates sampled couplings; the factorization above it is exact (symbolic).
- **Arithmetic, not the model.** The coupling formula and its 4/3 come from the cited papers, and the premise u = 1 from the program's record; the script checks the arithmetic that connects them to the bound, not the physics behind them ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

## Sources

- `CLAUDE.md` 'Since the handoff' — the bound as recorded after the note: in the aligned bimetric vacuum, u = 1, X's range is below 37.7 μm and M_X c² > 5.2 meV; the persistence of the aligned vacuum as an open lead; 'Method' — the lesson on carrying every parameter of a cited formula
- `papers/phase-space-diameter.md` §8.2 — the coupling, the premise and its argument, the open points, the screening estimate, the data, the bound and its dependence on u, what follows, the caveats [D][V][S]; §8 — the plain-language summary; §8.1 — the self-dual length excluded as the dual-relativity Born length; §1 — the abstracts; §7 — the self-dual length and the dark-energy scale; §8.6 — what would test it; §9 — the summary table and its tags; 'References' — Lee et al. 2020 and the thesis, Aoki–Mukohyama 2016, Lüben–Mörtsell–Schmidt-May 2020, Enander–Mörtsell 2013, Sundrum 2004, Kapner et al. 2007, all [S]
- `review/round5-adjudication.md` 'Verdict', 'Rulings' R1, R12, R16, 'Pre-registration scored', 'Revisions for v1.1' — the dropped background ratio, the argument for u = 1, referee A's value not upheld, the column wording, the caveats, the score and the repair
- `review/round5-preregistration.md` 'Predictions' — the weakest link predicted
- `review/round5/manuscript-v1.0.md` §8.2 — the reviewed version's coupling, α = (4/3)(M_f/M_g)², without the background ratio
- `verify/phase_space_diameter.py` 'Consequences (note §8)' — every number on this page recomputed [V]
- `review/round5/adjudicator/arb.out` A1/B1, B9 (from `review/round5/adjudicator/arb.py`) — the broken vacua at β₁ = −1, β₂ = 2; the bound as a function of u; the two columns at three strengths
- `review/round5/referee-A/scripts/lee_interp.py`; `review/round5/referee-A/outputs/lee_interp.txt` — the three columns of Table 11.4 as transcribed by referee A; the bound at referee A's u = ã/a, "no laboratory bound"
- `review/round5/referee-B/audit-notes.md` §4.5; `review/round5/referee-B/outputs/torsion_interp.txt` — no stronger constraint at these ranges; the bound under logarithmic and linear interpolation
- `notes/debt1a-iv-beta-coefficients.md` §1–§2 — the second frame f = E₀[J], the aligned point and the vacuum-energy identity; §3 — equal Planck masses and the range argument [D + T]
- `notes/debt1a-iii-tuning-test.md` §4 — E₀[J] confined to a compact moduli space (that it carries no scale of its own is the note's reading)
- `papers/broken-born-checkpoint-v2.md` §7.5 — X's couplings "gravitational-strength and Yukawa-cut at 1/M_X" [D]
- `review/v3-worklog.md` 'Round-2 pending list' item R7 — the early-universe stability of a heavy spin-2 field at equal Planck masses, open
- `review/wiki-build-flags.md` item 39 — the frame exchange and Z → −Z⁻¹ give the graviton different parities; awaiting Paul's ruling
- `notes/closed-universe.md` §6; `review/wiki-build-flags.md` item 51 — β₁ > 0 required on the branch, the alignment today with f dynamical, and the frozen reading
