---
title: "Row 6: the exactly massless graviton"
weight: 70
status: alive
description: "Graviton-mass bounds from gravitational waves apply to the reciprocity-even spin-2 combination, which is exactly massless, while the odd combination X is massive and short-range; killed by a nonzero mass attributed to the even eigenstate."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 6"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.5)'"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-program-v1.md §11"
  - "papers/conjugate-special-relativity.md §6"
  - "review/v3-worklog.md 'Round-2 pending list' R7"
  - "review/wiki-build-flags.md item 5"
  - "verify/battery.py T5"
---

*Row 6 is the program's prediction that the graviton, the quantum of gravitational waves, has exactly zero mass. The program's geometry carries two spin-2 fields, the ordinary metric and a partner describing momentum space, and Born reciprocity exchanges them. The combinations of definite mass are their sum, which the exchange leaves unchanged (reciprocity-even), and their difference, which changes sign (reciprocity-odd). The even combination is the ordinary graviton and is exactly massless; the odd one is the [momentum graviton X](/wiki/gravity/momentum-graviton), which is massive, so the force it carries has a finite range. Observations of gravitational waves set upper bounds on the graviton's mass, and in the program those bounds apply to the even combination, which meets them identically. A nonzero mass attributed to the even combination would kill the row; #11 does not count it among the program's near-term exposures.*

**Status:** Alive — [D] (#11 §7.5); [D + T] in calc note #8 (`notes/debt1a-iv-beta-coefficients.md` §3) — the parity follows from reciprocity acting on the two spin-2 frames as an exchange (#11 §7.3). No machine check covers the parity assignment; the identity V(1) = 2T used in reducing the gravity sector's parameters is machine-checked [V] (battery test T5).

## The row

[Checkpoint #11](/wiki/history/documents/checkpoint) §13, row 6:

| Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- |
| Gravitational waves | m_g = 0 | Massless eigenstate exactly massless (reciprocity-even) | Nonzero mass attributed to the even eigenstate |

m_g is the graviton mass. The standard expectation and the requirement agree on the number, zero. What the row adds is a claim about a theory with two spin-2 fields: that the combination whose mass the observations bound is massless exactly, as a consequence of reciprocity, and that it is the reciprocity-even one.

## The observable: the graviton mass [T]

In [general relativity](/wiki/gravity/spin-2-fields/general-relativity#the-gravitons-mass-t) the graviton is massless, and gravitational waves of every frequency travel at the speed of light. A graviton of mass m_g would obey the energy–momentum relation of a massive particle, E² = p²c² + m_g²c⁴, so its waves would travel slower than light, and the more slowly the lower their frequency [T]. The signal from a merging pair of black holes or neutron stars sweeps upward in frequency as the two bodies spiral together. A graviton mass would delay the low-frequency part of the signal relative to the high-frequency part and so change the signal's phase relative to the prediction of general relativity; the agreement of observed signals with that prediction bounds the mass [T]. A massive graviton would also give gravity a finite range, the Yukawa form set out on [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety#background-yukawa-forces-and-their-range-t) [T].

Calc note #7 §4 places the bound from gravitational-wave observations in the "m_g ≲ 10⁻²³ eV territory", with no reference. Two standard references, cited from memory and by no program document (†): C. M. Will, "Bounding the mass of the graviton using gravitational-wave observations of inspiralling compact binaries," Phys. Rev. D 57, 2061 (1998); B. P. Abbott et al. (the LIGO Scientific and Virgo Collaborations, LIGO being the Laser Interferometer Gravitational-Wave Observatory), "Tests of general relativity with GW150914," Phys. Rev. Lett. 116, 221101 (2016).

## The standard expectation

"m_g = 0" (#11 §13). General relativity has one spin-2 field, the metric, and its quantum is massless [T].

A theory with two interacting spin-2 fields, such as [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric#the-spectrum-t), has, about a common background, one massless and one massive spin-2 mode, and matter coupled to one of the metrics feels both modes in proportions set by the two Planck masses [T]. Calc note #7 §4 applied these "Standard bimetric facts" [T] to the program: "one massless combination (our graviton, coupling to SM stress) and one massive (X)", SM being the Standard Model. In such a theory a bound on the graviton mass needs an interpretation, because the waves detectors register are emitted and absorbed by ordinary matter, which couples to both modes. #7 §4 read the bound as a check on how the two modes mix; row 6 replaces that reading with a statement about the modes themselves (History, below).

## The Broken-Born requirement

### Two spin-2 frames

After [the tuning test](/wiki/gravity/tuning-test), the program's gravity sector is bimetric gravity written in frame variables: the frame e of the ordinary metric g, and a second frame f = E₀[J] built from the vacuum's polarization J and confined to the compact space Λ(4) ([constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric)). Why the second spin-2 field exists and must be massive is set out on [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain). In #11 §7.1's summary [D + T], X is "a second linearized-diff gauge field", a second massless graviton is excluded by the [multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go), and "The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale" ([the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)).

### Reciprocity exchanges the frames

#11 §7.3: "Reciprocity acts on the wedge sector as frame exchange, forcing **βₙ = β₄₋ₙ**." The βₙ are the five coefficients of the bimetric potential. Exchanging the frames reverses their order, so a potential that reciprocity leaves invariant reads the same in both directions ([the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome#how-reciprocity-acts-the-frame-exchange) [D]). With the requirement that the aligned vacuum be flat, which uses the identity V(1) = 2T checked in exact integers by battery test T5 ([the verification battery](/wiki/method/verification/battery)), two parameters remain. #11 §7.5 [D]: "Five βₙ → two parameters (M_X ∝ 2(β₁+β₂); one cubic shape)." Calc note #8 §3, the source of the count, writes the proportionality for the squared Fierz–Pauli mass, "m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**"; the difference is recorded in `review/wiki-build-flags.md` item 5, and this page quotes both as written. The reduction is on [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity#from-five-coefficients-to-two).

### The even and odd combinations

Calc note #8 §3 [D + T] assigns the parities:

> "the massless graviton is the reciprocity-**even** combination (e + f); X is reciprocity-**odd** (e − f). Reciprocity is a selection rule on vertices."

#11 §7.5 [D] carries the result as "Massless graviton = reciprocity-even" and "X = reciprocity-odd".

#8 states the result without the intermediate steps. The wiki's reading of them [T]: an exchange that leaves the quadratic part of the action unchanged commutes with its mass matrix, so the fields of definite mass can be chosen even or odd under it, and with two fields these are the sum and the difference. In bimetric gravity the potential is unchanged when both metrics undergo the same change of coordinates, so one combination of the fluctuations stays massless. About the point where the two metrics coincide, the massive mode is the difference of the two fluctuations, and the massless mode is their sum weighted by the squares of the two Planck masses. With equal Planck masses the weights are equal and the massless mode is the plain sum, which the exchange leaves unchanged. #8 §3 supplies the equal Planck masses: "With equal effective Planck masses (forced by the same symmetry)" ([equal Planck masses](/wiki/gravity/momentum-graviton/spectrum-and-parity#equal-planck-masses)).

```text
reciprocity:   e ↔ f
e + f   →    e + f        even    the massless graviton
e − f   →  −(e − f)       odd     X, mass M_X
```

### What the parity does to the bounds

The graviton-mass bounds from gravitational waves "apply to the even eigenstate, which is exactly massless" (#8 §3), and #11 §7.5 calls them "satisfied identically". The bound is met for every value of the program's two remaining parameters, because the even combination has no mass term for a bound to constrain. The odd combination carries the whole mass M_X, and no document gives M_X a value ([no value for M_X](/wiki/gravity/momentum-graviton/spectrum-and-parity#no-value-for-mx)). The requirement is a structural statement, not a fit to data.

### X: massive, short-range, felt by matter

The equal Planck masses have a second consequence. Matter coupled to g "sees both eigenstates with comparable strength; safety is by **range**, not decoupling" (#8 §3): X's force on ordinary matter has gravitational strength and is "Yukawa-cut at 1/M_X" (#11 §7.5; [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety#the-argument-step-by-step)). v1 wrote this into its row 6 as a second requirement, "massive X short-range" (#9 §9); #11 keeps it in §7.5 and not in the row.

[Conjugate special relativity](/wiki/conjugate-relativity) (#13 §6) adds that the massless graviton is common to both kinds of matter: "Shared: the time coordinate (in the 3+1 presentation used here) and the massless graviton, so both polarizations fall identically." The two polarizations of matter are those of postulate [P4](/wiki/program/postulates/p4-polarized-matter).

## What kills it

"Nonzero mass attributed to the even eigenstate" (#11 §13). In the wiki's reading, the test is a gravitational-wave observation that measures a graviton mass rather than bounding it, with the mass belonging to the long-range graviton that the program identifies with the even combination. The documents do not say how such an attribution would be made, or what a measured mass of the odd combination would imply. v1's wording was "Any nonzero graviton mass attributed to the even eigenstate" (#9 §9).

The row rests on the same step as [the palindrome](/wiki/gravity/palindromic-branch/palindrome) and [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity): reciprocity acting on the two frames as an exchange (#11 §7.3).

## The data situation

No observation has found a graviton mass, and the published limits are upper bounds [T]. The program's documents cite them only through calc note #7 §4's "m_g ≲ 10⁻²³ eV territory" and treat every such bound as met: "satisfied identically" (#11 §7.5). A tighter upper bound leaves the row where it is. #11 §15 names rows 1, 4 and 7 as the program's "genuine and near-term" falsification exposure; row 6 is not among them.

## Related open questions

- **Stability at equal Planck masses.** The heavy spin-2 fields shown to be linearly stable at late times in an expanding universe assume the second metric's Planck mass much smaller than the first. Reciprocity's equal Planck masses rule out "the M_f ≪ M_g escape", and "Whether a large mass alone is enough at M_f = M_g is open" (`review/v3-worklog.md`, item R7; [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability); [bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology)). The question concerns X's stability, not the mass of the even combination.
- **The selection rule.** #8 §3 calls reciprocity "a selection rule on vertices"; no document lists the vertices it allows or forbids ([a selection rule on vertices](/wiki/gravity/momentum-graviton/spectrum-and-parity#a-selection-rule-on-vertices)).

## History of the row

- **v0.1.** The lab notebook's table (#1 §9) has no graviton row; its ten rows are listed on [the history of the predictions table](/wiki/predictions/table-history).
- **The mixing-angle reading.** Calc note #7 §4 logged the graviton-mass bound as a check on how the two spin-2 modes mix: "safety requires the massless combination to dominate SM couplings — a parametric check to log, alongside graviton-mass bounds", quoted as "m_g ≲ 10⁻²³ eV territory" from gravitational-wave observations, "for the mixing angle". The notebook's v0.5 addendum listed graviton-mass and mixing parametrics against the gravitational-wave bounds among three logged checks. Calc note #8 §3 replaced that reading with the parity eigenstates; the record is on [Superseded: the graviton-mass bound as a mixing-angle check](/wiki/gravity/momentum-graviton/spectrum-and-parity#superseded-the-graviton-mass-bound-as-a-mixing-angle-check).
- **The parities.** The notebook's v0.6 addendum summarized #8: "Spectrum: massless graviton = reciprocity-even, X = reciprocity-odd", with the Standard Model safe "by Yukawa range" and the gravitational-wave bounds "satisfied identically by the massless eigenstate" ([the lab notebook](/wiki/history/documents/lab-notebook)).
- **v1.** #9 §9 made it row 6: requirement "Massless eigenstate exactly massless (reciprocity-even); massive X short-range", killed by "Any nonzero graviton mass attributed to the even eigenstate". #9 §5 item 6 states the spectrum in nearly the words of #11 §7.5.
- **#11.** v2.0 shortened the row to its current wording, dropping "massive X short-range" and "Any". v2.1 and v2.2 left it unchanged ([the history of the predictions table](/wiki/predictions/table-history#the-checkpoint-v20-eleven-rows)).

## Superseded: "not previously posed"

v1's assessment counted "even-eigenstate masslessness as a bimetric-parity statement" among its "novel predictions not previously posed" (#9 §11). #11 §15 names only "predictions not previously posed (rows 3, 11)", and row 6 is not among them. No document says why the claim was dropped. Calc note #7 §4 had already counted the existence of one massless combination among the "Standard bimetric facts" [T]; what the program adds is the parity assignment and the equal Planck masses [D + T] (#8 §3). The program's current list of what it has produced is on [Assessment: a live research program](/wiki/program/assessment#predictions-not-previously-posed-rows-3-and-11).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 6 — the row; §7.5 — the spectrum, the parities and "satisfied identically" [D]; §7.3 — the frame exchange and the palindrome; §7.1 — why X is massive [D + T]; §15 — the near-term rows and the rows not previously posed
- `notes/debt1a-iv-beta-coefficients.md` §3 — the parities, the equal Planck masses, safety by range and the bounds on the even eigenstate [D + T]
- `notes/debt1a-iii-tuning-test.md` §4 — "Standard bimetric facts" and the earlier mixing-angle reading of the bound
- `verify/battery.py` T5 — the identity V(1) = 2T in exact integers [V]
- `notes/broken-born-theory.md` 'Addendum (v0.5)', 'Addendum (v0.6)' — the logged check and the summary of the parities
- `notes/broken-born-program-v1.md` §5, §9, §11 — v1's spectrum, its row 6 and its novelty claim
- `papers/conjugate-special-relativity.md` §6 — the massless graviton shared by both polarizations
- `review/v3-worklog.md` 'Round-2 pending list', item R7 — the equal Planck masses and the open stability question
- `review/wiki-build-flags.md` item 5 — M_X versus M_X² in the parameter count
