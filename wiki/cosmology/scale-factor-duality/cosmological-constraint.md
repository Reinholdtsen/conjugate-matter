---
title: "The cosmological constraint a·ã = 1"
weight: 20
status: alive
description: "ω-rigidity fixes the comoving phase-space cell, so our scale factor and the conjugate's are reciprocals: the |Z| = 1 locus of the modular field, and the program's version of scale-factor duality."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md App. A item 6"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight): axiom correction and the modular core'"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/broken-born-program-v1.md §8"
  - "verify/battery.py T2"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*The cosmological constraint is the relation a·ã = 1 between the scale factor a of our universe and the scale factor ã of its momentum-space description, the [conjugate universe](/wiki/program/conjugate-universe): as our universe expands, its momentum-space description contracts by exactly the same factor. It follows from the program's postulate that the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, the structure that fixes the size of a cell of phase space and with it the value of Planck's constant, is rigid. A comoving cell therefore keeps its phase-space volume while position-space distances grow, which forces momentum-space distances to shrink; in signal terms, stretching a waveform compresses its spectrum. The relation is derived [D], and it turned one of the program's [founding suppositions](/wiki/program/founding-suppositions), that the conjugate universe shrinks as ours expands, into a theorem.*

**Status:** Alive — [D] (#11 §10) — derived in the [lab notebook](/wiki/history/documents/lab-notebook) (#1 §6) and stated from ω-rigidity in #11; not machine-checked. The modular parametrization it belongs to, including det H_Z = 1, is checked numerically at one sampled point ([the verification battery](/wiki/method/verification/battery), test T2); the constraint itself is not, and its identification with the |Z| = 1 locus is structural.

## Statement

#11 §10: "**Constraint [D]:** ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run) — the |Z| = 1 self-dual locus."

#11's plain-language opener to the same section describes the relation as "one motion written twice, like a number and its reciprocal".

## The ingredients

**Two scale factors.** In [Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) the scale factor a(t) multiplies every distance between comoving galaxies. The program describes the same universe a second time in momentum variables, the [conjugate universe](/wiki/program/conjugate-universe), and gives that description its own scale factor: "x-space scale factor a and p-space scale factor ã" (#1 §6). The scale factor ã multiplies momentum-space distances as a multiplies position-space ones.

**The phase-space cell [T].** Quantum mechanics divides phase space, the space of positions and momenta together, into cells: one quantum state occupies a cell of volume of order ℏ per position–momentum pair. That size comes from the canonical commutator [x, p] = iℏ ([the canonical commutator and the uncertainty principle](/wiki/phase-space/reciprocity/canonical-commutator)), and geometrically from the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, which measures areas in each position–momentum plane. A map that preserves ω preserves phase-space volume (Liouville's theorem) [T].

**ω-rigidity.** In the program ω is not a dynamical field. The current postulate is [P2′](/wiki/program/postulates/p2-prime): "Only ω is rigid (symplectic rigidity ≡ constancy of ℏ)" (#11 §4). A rigid ω means a fixed cell size, which is the same statement as a constant ℏ.

## The derivation

The [lab notebook](/wiki/history/documents/lab-notebook) gives the argument in three sentences (#1 §6): "Rigidity of ω means the comoving phase-space cell has fixed volume: with x-space scale factor a and p-space scale factor ã, each mode occupies (aã)³ × (comoving cell) = ℏ³." Hence

```text
a·ã = const ≡ 1
```

"This is not an extra assumption; it is the statement that ℏ does not run."

Step by step:

1. **A comoving cell.** Take a cell of phase space attached to the expansion: fixed comoving extent in position and fixed comoving extent in momentum.
2. **Its physical volume.** In three dimensions its physical position-space volume grows as a³ and its physical momentum-space volume as ã³, so its phase-space volume is (aã)³ times the comoving volume.
3. **Rigidity.** ω-rigidity fixes that volume: one mode occupies ℏ³, now and at every other time.
4. **The constraint.** The comoving cell is fixed by definition, so (aã)³ is constant, and so is a·ã. The constant is set to 1, a choice of normalization for ã.

The derivation is short because the content sits in the postulate. It needs no field equation and no dynamics of the conjugate side, so it holds at every moment of any homogeneous cosmology, which is what lets later results use it as an identity ([the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)).

**Comparison with standard cosmology [T].** In an ordinary expanding universe the physical momentum of a freely moving particle falls as 1/a, so the momentum scales of the universe shrink as its distances grow, and a cloud of free particles keeps its phase-space volume. The [popular article](/wiki/history/documents/popular-articles) #12 reads a·ã = 1 in these terms, as the redshift read in momentum variables: "every momentum in the universe is shrinking: the spectrum of the cosmos has been contracting since the beginning. That is not a second process running alongside expansion; it is expansion, read in the other variable." The technical documents state the constraint from ω-rigidity and do not discuss this correspondence; the gloss is the popular article's.

## From strict P2 to P2′

The notebook derived the constraint under the [original P2](/wiki/program/postulates/original-p2), which froze both ω and the neutral metric η. That postulate was given "triple duty", one of which was that "it enforces the cosmological constraint a ã = const" (#1 §1, which points to §7; the derivation is in §6, a pointer slip of the kind collected in `review/wiki-build-flags.md` item 10).

The v0.3 addendum found that strict P2 makes the theory trivial and replaced it by P2′, under which only ω is rigid ([the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)). The constraint survives the replacement, because its derivation uses only the rigidity of ω: η plays no role in fixing the cell volume. #11 states it on that basis: "ω-rigidity fixes the comoving phase-space cell". The same addendum lists, among the structures P2′ restores, "the cosmological constraint a·ã = 1 as the |Z| = 1 locus" (#1, v0.3 addendum).

## The geometry: the |Z| = 1 locus

With only ω rigid, the generalized metric H ranges over the Siegel domain, coordinatized by the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY with Im Z = Y the spacetime metric g. Born reciprocity acts on Z by inversion: #11 §6, "**ρ: Z → −Z⁻¹** (Möbius; d = 1 check), fixed point Z = i; at X = 0 it is scale-factor duality g → g⁻¹, and the cosmological constraint a·ã = 1 (§10) is the |Z| = 1 locus." See [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion).

Calc note #5 puts the relation between the two pictures this way: "The cosmological constraint a·ã = 1 is the |Z| = 1 self-dual circle — the minisuperspace duality was the shadow of this modular action" (§C). In the half-plane picture (d = 1), inversion Z → −1/Z carries the unit semicircle |Z| = 1 onto itself and fixes only the point Z = i [T].

The documents identify a·ã = 1 with this circle without writing out how the two scale factors a and ã sit inside Z. The identification is a structural reading: calc note #5 tags its section "[D — structural; math facts standard]", and #11 §10 tags the constraint [D].

**Unimodularity.** A second geometric fact carries the same content. The [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)'s first corollary is that "det H = 1 identically. The generalized metric is unimodular: phase-space volume is not a dynamical field. ℏ-rigidity is manifest in the geometry, not imposed on it." (#5 §A). Calc note #5 counts "unimodularity of H (det H = 1) as the geometric face of ℏ-rigidity" among the results of its night's work (§F), and #11 §5 lists "det H = 1 identically (ℏ-rigidity is *geometric*, and — machine-verified — persists across the whole modular family of §6)". See [the corollaries of the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-corollaries).

**The machine check.** Test T2 of [the verification battery](/wiki/method/verification/battery) builds H_Z for one randomly drawn X and Y at d = 4 and prints `PASS  T2 det H_Z = 1  [det=1.000000000000]`. #11 §2 describes the check as "det H = 1 across the whole family"; the test evaluates one member of the family. It checks the parametrization, not the cosmological constraint, which no script tests.

## The name: scale-factor duality [T]

In string cosmology, scale-factor duality is a symmetry of the low-energy string equations for a homogeneous universe: a solution with scale factor a(t) maps to another solution with 1/a(t), together with a shift of the dilaton field (Veneziano 1991 †; Tseytlin 1991 †). It relates two different solutions. The program uses the name for the X = 0 form of modular inversion, g → g⁻¹ (#11 §6): if the metric is the unit metric scaled by a², its inverse is scaled by a⁻². The constraint a·ã = 1, by contrast, pairs the two scale factors of one state in its two descriptions (the wiki's reading of the difference; the documents use the name without comparing the two).

## What follows

- **The duality dictionary.** Because ã = 1/a at every moment, energy described in the conjugate frame can be translated into its effect on our expansion. The result is w_eff = −w̃: [the duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary).
- **The early-universe term.** Substituting ã = 1/a into a dual gravitational term gives the a⁻⁶ correction to the Friedmann equation behind [row 10](/wiki/predictions/early-universe-step) (#1 §6).
- **The bounce.** A maximum of a is a minimum of ã, so a far-future turnaround of our expansion is the conjugate universe's bounce: [the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce), tested on [row 5](/wiki/predictions/fate-of-expansion).
- **A founding supposition promoted.** Founding supposition 6, "Conjugate universe shrinks as ours expands", is "**promoted to theorem** (a·ã = 1 from ℏ-rigidity; the |Z| = 1 locus)" (#11 App. A item 6). See [founding suppositions and their fates](/wiki/program/founding-suppositions).
- **A chat-only use.** The [phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter) speaks of "distance from self-duality"; it is a conjecture with no document behind it.

## Scope and caveats

- **Minisuperspace.** The derivation concerns a homogeneous universe with one scale factor per description. No document extends it to an inhomogeneous H.
- **Not machine-checked.** The constraint is derived [D] and no `verify/` script tests it. Only the unimodularity of the modular parametrization is checked, at one sampled point.
- **A structural geometry.** The |Z| = 1 reading is stated, not derived through an explicit map from (a, ã) to Z.
- **Normalization.** The constant is set to 1 by choice; only its constancy is physical.

## History

- **Lab notebook, v0.1.** Derived in #1 §6 under strict P2, which #1 §1 credits with enforcing it.
- **Lab notebook, v0.3 addendum.** P2 replaced by P2′; the constraint appears "as the |Z| = 1 locus" of the modular field.
- **Calc note #5** (§C, §F): "the minisuperspace duality was the shadow of this modular action"; det H = 1 as "the geometric face of ℏ-rigidity".
- **#9 §8**: "ω-rigidity fixes the comoving phase-space cell: a·ã = 1. Not an assumption — the statement that ℏ does not run; geometrically, the |Z| = 1 self-dual locus."
- **#11 §10** is the current statement, and App. A item 6 records the founding supposition's promotion.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the current statement, its tag and "one motion written twice"
- `papers/broken-born-checkpoint-v2.md` §6 — the |Z| = 1 locus and scale-factor duality g → g⁻¹
- `papers/broken-born-checkpoint-v2.md` §4 — P2′: "symplectic rigidity ≡ constancy of ℏ"
- `papers/broken-born-checkpoint-v2.md` §2, §5 — det H = 1 "across the whole family" and as a corollary of the compatibility theorem
- `papers/broken-born-checkpoint-v2.md` App. A item 6 — founding supposition 6, "promoted to theorem"
- `notes/broken-born-theory.md` §6 — the derivation from a fixed phase-space cell
- `notes/broken-born-theory.md` §1 — the original P2 and its "triple duty"
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight): axiom correction and the modular core' — P2′ and the |Z| = 1 locus
- `notes/debt1a-geometric-core.md` §A, §C, §F — unimodularity; "the shadow of this modular action"; det H = 1 as the geometric face of ℏ-rigidity
- `notes/broken-born-program-v1.md` §8 — v1's statement: "Not an assumption — the statement that ℏ does not run"
- `verify/battery.py` T2 — det H_Z = 1 for one sampled member of the Siegel family, executed
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — the redshift gloss (popular article; explanation only)
