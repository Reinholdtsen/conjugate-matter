---
title: "The magnetic mirror-family"
weight: 40
status: established
description: "Founding supposition 11 absorbed as established physics: Dirac's condition pins the magnetic coupling near 4π/e² ≈ 34 (a figure that depends on the charge convention by a factor of 4), so the magnetic world is our strong-coupling mirror, hidden by its own structure."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.2"
  - "papers/broken-born-checkpoint-v2.md App. A item 11"
  - "papers/broken-born-checkpoint-v2.md §11 (italic opening)"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md refs [17]–[18]"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/round3/referee/step2a.out"
  - "review/round3-adjudication.md 'Rulings' 12"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*The magnetic mirror-family is the idea that every electrically charged particle, quarks included, has a magnetic counterpart. It entered the program as P.R.'s [founding supposition 11](/wiki/program/founding-suppositions), and [the checkpoint](/wiki/history/documents/checkpoint) records it as established physics: [Montonen–Olive duality](/wiki/electric-magnetic-duality/s-duality), Seiberg's magnetic quarks and the [dual-superconductor](/wiki/electric-magnetic-duality/dual-superconductor) picture of quark confinement already contain it. [Dirac's condition](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) accounts for why the counterparts are not seen: a weak electric coupling forces a strong magnetic one, so magnetic particles are heavy and tightly bound. The checkpoint's figure for the magnetic coupling of our electromagnetism, about 34, is not the hidden-sector coupling [α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling) that died with the soliton candidate. The program's own addition is the observation that choosing which particles count as electric is a choice of polarization, which has its own page.*

**Status:** Established — [T] — "alive as established physics" (#11 App. A item 11). The physics is #11 §11.2, tagged [T] and cited as [17†-adjacent; 18†] and 't Hooft–Mandelstam†, all from model memory and due [the † literature battery](/wiki/method/literature-battery). The factor-of-four convention spread is marked [V] in the v3 worklog (item R2); the round-3 referee's script prints the two values for the hidden sector (`review/round3/referee/step2a.out`), and no script in the current gate checks them.

## The supposition and its fate

Founding supposition 11, as #11's audit of P.R.'s founding suppositions records it ([#11](/wiki/history/documents/checkpoint) App. A item 11; [founding suppositions and their fates](/wiki/program/founding-suppositions)):

> A full magnetic mirror-family, quarks included — **alive as established physics** (Montonen–Olive, Seiberg, dual superconductor), absorbed as §11 with the polarization identification as the program-native addition.

The supposition was one of P.R.'s founding conjectures. The audit found that the physics literature already contains it, in three forms, and it moved from the program's claims to its background. Section 11 of the checkpoint, where it was absorbed, first appeared in v2.0; [the handoff](/wiki/history/documents/handoff) lists "charge-lattice §11" among v2.0's additions (`HANDOFF.md` §3).

## The dual spectrum in the literature [T]

#11 §11.2, under the heading "The full dual spectrum [T]":

> The conjecture that every electrically charged particle has a magnetic counterpart is Montonen–Olive duality [17†-adjacent; 18†], exact in maximally supersymmetric Yang–Mills; "magnetic quarks" is standard vocabulary via Seiberg duality [18†]; and the dual-superconductor picture of confinement — chromomagnetic monopole condensation squeezing color-electric flux into strings — is the leading mechanism for why free quarks are never seen [T, 't Hooft–Mandelstam†].

The three results, each with its own page:

- **Montonen–Olive duality** (1977). In a gauge theory with [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles), the electrically charged particles and the monopoles can exchange roles under a duality that also exchanges weak and strong coupling; exact in the maximally supersymmetric theory ([S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality)).
- **Magnetic quarks.** Seiberg's dualities of supersymmetric versions of quantum chromodynamics give the long-distance physics of a theory with quarks an equivalent description in terms of "magnetic quarks" (same page).
- **The dual superconductor.** A condensate of magnetic monopoles in the vacuum of the strong interaction confines quarks by squeezing the color-electric field into strings ([the dual superconductor](/wiki/electric-magnetic-duality/dual-superconductor)).

The checkpoint's italic opening to §11 dates the idea: "proposed in 1977, named in 1994". The label "17†-adjacent" is the checkpoint's own; reference [17] is the Dirac–Schwinger–Zwanziger trio, and #11 does not say what the qualifier means.

## Why the mirror is not seen

### Dirac's condition forces a strong magnetic coupling [T]

The strength of a force between two charges q is measured by a dimensionless coupling, q²/4π in natural units; for the electron's charge e this is the fine-structure constant α = e²/4π ≈ 1/137 [T]. A magnetic charge g has a magnetic coupling g²/4π in the same way.

Dirac showed that quantum mechanics allows a magnetic charge g alongside an electric charge e only if the product e·g is a whole-number multiple of a fixed constant ([Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization), where DSZ is Dirac–Schwinger–Zwanziger). Since e·g is fixed, g is proportional to 1/e, and the magnetic coupling is proportional to 1/α. A weak electric force forces a strong magnetic one.

#11 §11.2 draws the consequence for our electromagnetism:

> Non-observation is structural: Dirac's condition e·g ~ 2π pins the magnetic coupling near 4π/e² ≈ 34 — the magnetic world is our strong-coupling mirror, heavy and bound.

"Heavy" follows because a monopole that arises as a soliton of a broken gauge symmetry has a mass of the symmetry-breaking scale multiplied by 4π/g, which is large when the gauge coupling g is small: the ['t Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole) has M = 4πf v/g for scale v and an order-one factor f [T] ([#14](/wiki/dark-matter/candidates/soliton-candidate) §3 gives the formula for the hidden sector). "Bound" refers to the strength of the magnetic interaction: at a coupling far above one, opposite magnetic charges attract strongly and bind [T]. If magnetic counterparts exist, their absence from experiments follows from the structure of the theory itself, which is what #11 means by "structural".

### The convention behind 34

The figure 34 depends on how Dirac's condition is normalized. Round 2 of the soliton manuscript's review asked about it ([review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)), and the v3 worklog adjudicated it as item R2, marked [V] (`review/v3-worklog.md`, 'Round-2 pending list'):

> Convention: 1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn). One-loop SM running of α_em gives 1/(4α_em) = 29.0 at 10¹¹, 28.8 at 3×10¹¹ and 27.3 at 10¹⁶ GeV. The referee's "toward ~6–8" is **not reproduced** for the electromagnetic coupling; 6–8 appears only for 1/(4α₃). The valid core stands: the number is convention-dependent by a factor of 4.

SM is the Standard Model, and α₃ the strong-force coupling. The item was written for the hidden sector of the soliton manuscript, but its arithmetic concerns α itself: writing Dirac's condition with 2πn or with 4πn changes the smallest magnetic charge by a factor of two and the magnetic coupling by four [T], and the coupling also changes slowly with the energy at which α is evaluated. The round-3 referee's script prints the same two values, "alpha_m = g_m^2/4pi = 34.259" and "alpha_m = 1/alpha = 137.036" (`review/round3/referee/step2a.out`). Ruling 12 of round 3 accepted the related point that Zwanziger's paper states the pairing in 4πℤ where the manuscripts write 2πℤ ([round-3 rulings](/wiki/method/review/round-3/rulings)). The figure should not be quoted without its normalization.

Quoted as #11 writes it, the expression 4π/e² stands beside the condition e·g ~ 2π. With α = e²/4π [T], 4π/e² is 1/α, which R2 pairs with eg = 4πn and the value 137.04, while R2 pairs the value 34.26 with 1/(4α) and eg = 2πn. Whether #11's e means the smallest charge, as here, or twice it, as for the gauge coupling g_d of #14 (whose smallest charge is g_d/2, so that its monopoles have g_m = 4π/g_d, #14 §2), is queried in this wiki's list of suspected source errors (`review/wiki-build-flags.md`); the statement above is #11's, unchanged.

### Not the dead α_d ≈ 34

Two different claims carry the number 34, and only one of them is dead.

- **This page's 34** is a property of our own electromagnetism: the magnetic coupling that Dirac's condition imposes on any monopole of our U(1), given our electric charge (#11 §11.2 [T]). It is established physics and alive.
- **The dead α_d ≈ 34** was the coupling the soliton candidate assigned to the monopoles of a hidden gauge sector. Its first derivation applied Dirac's condition against our photon, which the handoff lists among the dead claims: "α_d ≈ 34 via Dirac quantization against our photon (round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon)" (`HANDOFF.md` §2). Its later forms, reciprocity acting on the coupling as modular S and #14's hypothesis H, are superseded or dead with the candidate ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).

What carries over from the general mechanism is #11 §12's surviving statement: "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]."

## The same explanatory shape as the hidden metric

#11 §11.2 ends with a comparison: "*Same explanatory shape as §7: the duality is genuine, and its structure hides its second half.*"

In §7 the duality is [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), and its second half is the second metric of phase space, the [momentum graviton X](/wiki/gravity/momentum-graviton). When the vacuum selects a polarization, X absorbs the [Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs) of the broken dual diffeomorphisms and becomes massive, with "M_X = the polarization-breaking scale" (#11 §7.1). #11 states the result: "Momentum space gravitates, massively and invisibly to everything not polarized its way — which is simultaneously why the symmetry is real and why its second metric was never seen" (§7).

The parallel is structural, and #11 does not develop it further:

| | electric–magnetic duality (§11.2) | Born reciprocity (§7) |
| --- | --- | --- |
| the duality | electric ↔ magnetic | position ↔ momentum |
| the hidden half | magnetic particles | the second metric X |
| what hides it | the strong magnetic coupling forced by Dirac's condition | the mass X acquires when the polarization is chosen |
| status | [T] | [D + T] |

## What the program adds

The supposition's fate names "the polarization identification as the program-native addition". It is the observation of #11 §11.3 that the Dirac–Schwinger–Zwanziger (DSZ) pairing makes the space of charges symplectic, so that choosing which particles count as electric is choosing a [Lagrangian polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations) of that space, as the vacuum chooses which phase-space directions count as position [D — structural; math T] ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). Whether the two choices are one structure is open ([open problem 8](/wiki/electric-magnetic-duality/unified-modular-structure)).

## The popular article's extension

[The popular article #12](/wiki/history/documents/popular-articles) takes the family a step further than the record: "The framework's addition is the free spectrum: the momentum polarization carries the entire magnetic mirror-family — a matter sector as structured as our own, every member heavy and strongly bound by Dirac's condition, of which only the topologically protected knots survive the age of the universe as free relics." No program document makes this claim. It identifies the momentum-polarized sector with the magnetic side of our electromagnetism, which conflicts with the strict separation of the two sectors' forces, and it is recorded as dead ([Obituary: the magnetic identification (popsci-only)](/wiki/electric-magnetic-duality/magnetic-identification)). The knots it names are the retired soliton candidate ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## Standard references

As #11 cites them, all from model memory (†):

- [17]† P. A. M. Dirac, Proc. R. Soc. Lond. A 133, 60 (1931); J. Schwinger, Phys. Rev. 144, 1087 (1966); D. Zwanziger, Phys. Rev. 176, 1489 (1968).
- [18]† C. Montonen, D. Olive, "Magnetic monopoles as gauge particles?" Phys. Lett. B 72, 117 (1977); N. Seiberg, "Electric–magnetic duality in supersymmetric non-abelian gauge theories," Nucl. Phys. B 435, 129 (1995), hep-th/9411149.
- 't Hooft–Mandelstam†, named in §11.2 with no entry in the reference list.

## Used by

- [The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice) — the "polarization identification", the program-native addition to founding supposition 11.
- [Founding suppositions and their fates](/wiki/program/founding-suppositions) — item 11.
- [Obituary: the magnetic identification (popsci-only)](/wiki/electric-magnetic-duality/magnetic-identification) — the established family of our own electromagnetism, against #12's relocation of it.

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.2 — the dual spectrum and Dirac's condition [T]; §11 italic opening — "proposed in 1977, named in 1994"; App. A item 11 — the fate of the supposition; §7 — the hidden second metric; §12 — "A weakly coupled hidden sector always has strongly coupled monopoles"; refs [17]–[18].
- `review/v3-worklog.md` 'Round-2 pending list' (R2) — the factor-of-4 convention spread and the running [V].
- `review/round3/referee/step2a.out` — the referee's printed 34.259 and 137.036.
- `review/round3-adjudication.md` 'Rulings' 12 — Zwanziger's 4π against the manuscripts' 2π, accepted as minor.
- `notes/knot-dark-matter-standalone.md` §2, §3 — g_m = 4π/g_d against the charge g_d/2; the monopole mass (withdrawn manuscript).
- `HANDOFF.md` §2 — the dead α_d ≈ 34, a different claim; §3 — §11 added in v2.0.
- `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the popular extension (not a status source).
