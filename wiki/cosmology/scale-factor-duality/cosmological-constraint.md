---
title: "The cosmological constraint a·ã = 1"
weight: 20
status: alive
description: "ω-rigidity fixes the comoving phase-space cell, so our scale factor and the conjugate's are reciprocals: the one-cell form of the phase-space diameter relation, identified in the documents with the |Z| = 1 locus of the modular field (queried, flag 23; the diameter note reads it as det H = 1 on the slice X = 0), and the program's version of scale-factor duality."
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
  - "notes/geometric-core.md §A"
  - "notes/geometric-core.md §C"
  - "notes/geometric-core.md §F"
  - "notes/broken-born-program-v1.md §8"
  - "verify/battery.py T2"
  - "papers/phase-space-diameter.md §3"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §6"
  - "verify/phase_space_diameter.py 'Reciprocity on a rectangle; wave packets (note §5)'"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
  - "review/wiki-build-flags.md items 23, 25"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §7"
  - "review/wiki-build-flags.md items 27 (addendum), 49"
---

*The cosmological constraint is the relation a·ã = 1 between the scale factor a of our universe and the scale factor ã of its momentum-space description, the [conjugate universe](/wiki/program/conjugate-universe): as our universe expands, its momentum-space description contracts by exactly the same factor. It follows from the program's postulate that the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω, the structure that fixes the size of a cell of phase space and with it the value of Planck's constant, is rigid. A comoving cell therefore keeps its phase-space volume while position-space distances grow, which forces momentum-space distances to shrink; in signal terms, stretching a waveform compresses its spectrum. The relation is derived [D], and it turned one of the program's [founding suppositions](/wiki/program/founding-suppositions), that the conjugate universe shrinks as ours expands, into a theorem.*

**Status:** Alive — [D] ([#11](/wiki/history/documents/checkpoint) §10) — derived in the [lab notebook](/wiki/history/documents/lab-notebook) (#1 §6) and stated from ω-rigidity in #11; not machine-checked. The modular parametrization it belongs to, including det H_Z = 1, is checked numerically at one sampled point ([the verification battery](/wiki/method/verification/battery), test T2) and, for d = 1, symbolically at every Z ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)); the derivation of the constraint from ω-rigidity is not checked by any script, and its identification with the |Z| = 1 locus is structural and awaits a ruling (`review/wiki-build-flags.md` item 23).

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

**Comparison with standard cosmology [T].** In an ordinary expanding universe the physical momentum of a freely moving particle falls as 1/a, so the momentum scales of the universe shrink as its distances grow, and a cloud of free particles keeps its phase-space volume. The [popular article](/wiki/history/documents/popular-articles) #12, without naming the constraint, describes the same reciprocal scaling as the [redshift](/wiki/cosmology/scale-factor-duality/redshift#the-momentum-description-12s-reading) read in momentum variables: "every momentum in the universe is shrinking: the spectrum of the cosmos has been contracting since the beginning. That is not a second process running alongside expansion; it is expansion, read in the other variable." The checkpoint and the lab notebook state the constraint from ω-rigidity and do not discuss this correspondence; the gloss quoted is the popular article's.

The phase-space-diameter note does discuss it (`papers/phase-space-diameter.md` §3). It reads a·ã = 1 as the area statement for one cell of the radiation's phase space: "The rectangle's area is the number of occupied cells times the area of one; a·ã = 1 fixes only the second factor, and the first is the radiation's entropy, set at reheating. In general relativity the one-cell statement already holds, because a free particle's comoving momentum is conserved [T]. The diameter relation therefore holds in standard ΛCDM cosmology, with or without reciprocity, and cannot test the program." ΛCDM is the standard cosmological model of a cosmological constant plus cold dark matter. The many-cell statement is [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), D_x·D_p = κ h N_γ^{1/3} for the radiation of a fixed comoving region [D][V].

## From strict P2 to P2′

The notebook derived the constraint under the [original P2](/wiki/program/postulates/original-p2), which froze both ω and the [neutral metric η](/wiki/phase-space/born-geometry/born-structures). That postulate was given "triple duty", one of which was that "it enforces the cosmological constraint a ã = const" (#1 §1, which points to §7; the derivation is in §6, a pointer slip recorded in `review/wiki-build-flags.md` item 25).

The v0.3 addendum found that strict P2 makes the theory trivial and replaced it by P2′, under which only ω is rigid ([the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem)). The constraint survives the replacement, because its derivation uses only the rigidity of ω: η plays no role in fixing the cell volume. #11 states it on that basis: "ω-rigidity fixes the comoving phase-space cell". The same addendum lists, among the identifications of the [modular field](/wiki/phase-space/modular-field/modular-field-z) that P2′ introduces, "the cosmological constraint a·ã = 1 as the |Z| = 1 locus" (#1, v0.3 addendum), a reading queried in `review/wiki-build-flags.md` item 23 (below).

## The geometry: the |Z| = 1 locus

With only ω rigid, the generalized metric H ranges over the [Siegel domain](/wiki/phase-space/modular-field/siegel-domain), coordinatized by the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY with Im Z = Y the spacetime metric g. [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) acts on Z by inversion: #11 §6, "**ρ: Z → −Z⁻¹** (Möbius; d = 1 check), fixed point Z = i; at X = 0 it is scale-factor duality g → g⁻¹, and the cosmological constraint a·ã = 1 (§10) is the |Z| = 1 locus." See [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion).

[Calc note #5](/wiki/history/documents/field-equation-notes) puts the relation between the two pictures this way: "The cosmological constraint a·ã = 1 is the |Z| = 1 self-dual circle — the minisuperspace duality was the shadow of this modular action" (§C). In the half-plane picture (d = 1), inversion Z → −1/Z carries the unit semicircle |Z| = 1 onto itself and fixes only the point Z = i [T].

The documents identify a·ã = 1 with this circle without writing out how the two scale factors a and ã sit inside Z. The identification is a structural reading: calc note #5 tags its section "[D — structural; math facts standard]", and #11 §10 tags the constraint [D].

The identification is under query. An executed check made while this wiki was built reads the X = 0 slice (d = 1) with g = a² = Y and the momentum block of H, Y⁻¹, as ã²; on that reading a·ã = 1 holds along the whole slice, as the content of det H = 1, while |Z| = 1 meets the slice only at Z = i. Either the documents intend a different placement of a and ã inside Z, or the identification is a slip; the point is recorded for Paul's ruling in `review/wiki-build-flags.md` item 23, with the check in `review/wiki-build-checks/self_dual_locus.py`. The wiki quotes the documents' identification as they state it and does not correct it.

**The phase-space-diameter note's reading [D][V].** The note reads the three loci on Gaussian wave packets (`papers/phase-space-diameter.md` §5; [Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states)). A packet labelled by Z has position and momentum widths with Δx/Δp = 1/|Z|, so:

> - **|Z| = 1** is the set of states whose rectangle is square, Δx = Δp, including tilted ellipses with X ≠ 0;
> - **Z = i** is the one round state, unchanged by reciprocity;
> - **det H_Z = 1** holds at every Z, so the constraint a·ã = 1 holds everywhere on the slice X = 0, where H = diag(Y, Y⁻¹).

It sets this beside the record: "The program's checkpoint identifies a·ã = 1 with the circle |Z| = 1 [P1, §6, §10]. But a·ã = 1 holds along the whole slice, and the circle meets the slice only at Z = i; an internal audit of the record queries the identification on this ground [H2]. This note uses the slice: cosmic expansion moves along X = 0, and 'self-duality' means Z = i." In the note's citations P1 is #11 and H2 is `review/wiki-build-flags.md`. The round-5 adjudication recommends that Paul accept flag 23, saying that the note's §5 and §6 support it ('Recommendations to Paul'). The flag awaits his ruling, and #11's identification stands in the record as written. The note's §6 adds an inference, tagged [D, inference]: the identification, applied to the expanding universe, is the probable origin of the withdrawn chat claim that the universe's phase-space rectangle is square at a bounce. It also finds that on |Z| = 1 the position and momentum extents are equal at all times, which the measured aspect ratio of the universe's radiation contradicts [V] ([Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)).

**Unimodularity.** A second geometric fact expresses the same ℏ-rigidity. The [compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)'s first corollary is that "det H = 1 identically. The generalized metric is unimodular: phase-space volume is not a dynamical field. ℏ-rigidity is manifest in the geometry, not imposed on it." (#5 §A). Calc note #5 counts "unimodularity of H (det H = 1) as the geometric face of ℏ-rigidity" among the results of its night's work (§F), and #11 §5 lists "det H = 1 identically (ℏ-rigidity is *geometric*, and — machine-verified — persists across the whole modular family of §6)". See [the corollaries of the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-corollaries).

**The machine checks.** Test T2 of [the verification battery](/wiki/method/verification/battery) builds H_Z for one randomly drawn X and Y at d = 4 and prints `PASS  T2 det H_Z = 1  [det=1.000000000000]`. #11 §2 describes the check as "det H = 1 across the whole family"; the test evaluates one member of the family. For d = 1, `verify/phase_space_diameter.py` checks the identity symbolically for every Z and prints `PASS  det H_Z = 1 at every Z; on X = 0, H = diag(Y, 1/Y)` ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)). Both check the parametrization. Reading det H = 1 on the slice as a·ã = 1 is the note's (§5) and flag 23's, and no script derives the constraint from ω-rigidity.

## The name: scale-factor duality [T]

In string cosmology, scale-factor duality is a symmetry of the low-energy string equations for a homogeneous universe: a solution with scale factor a(t) maps to another solution with 1/a(t), together with a shift of the dilaton field (Veneziano 1991 †; Tseytlin 1991 †). It relates two different solutions. The program uses the name for the X = 0 form of modular inversion, g → g⁻¹ (#11 §6): if the metric is the unit metric scaled by a², its inverse is scaled by a⁻². The constraint a·ã = 1, by contrast, pairs the two scale factors of one state in its two descriptions (the wiki's reading of the difference; the documents use the name without comparing the two).

## What follows

- **The duality dictionary.** Because ã = 1/a at every moment, energy described in the conjugate frame can be translated into its effect on our expansion. The result is w_eff = −w̃: [the duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary).
- **The early-universe term.** Substituting ã = 1/a into a dual gravitational term gives the a⁻⁶ correction to the Friedmann equation behind [row 10](/wiki/predictions/early-universe-step) (#1 §6). No document derives that dual term from the geometric action (flag 49), and in a closed universe the constraint fixes the normalization a = R/λ but not the a⁻⁶ coefficient, since only the combinations vM̃²C³ and vM̃²k̃C are physical ([the dual frame](/wiki/cosmology/scale-factor-duality/closed-universe#the-dual-frame-what-closure-fixes-and-what-it-does-not)).
- **The bounce.** A maximum of a is a minimum of ã, so a far-future turnaround of our expansion is the conjugate universe's bounce: [the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce), tested on [row 5](/wiki/predictions/fate-of-expansion). With τ's potential as written the turnaround needs a closed universe (flag 27 addendum; [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe)).
- **A founding supposition promoted.** Founding supposition 6, "Conjugate universe shrinks as ours expands", is "**promoted to theorem** (a·ã = 1 from ℏ-rigidity; the |Z| = 1 locus)" (#11 App. A item 6); the |Z| = 1 reading is queried in flag 23 (above). See [founding suppositions and their fates](/wiki/program/founding-suppositions).
- **The phase-space diameter relation.** For the radiation of a fixed comoving region, the region's diameter times the radiation's momentum spread is fixed, D_x·D_p = κ h N_γ^{1/3} with κ = 1.708 [D][V]; a·ã = 1 is its one-cell form, which general relativity already satisfies, so the relation holds in standard cosmology and cannot test the program (`papers/phase-space-diameter.md` §3). The logarithm of the rectangle's aspect ratio, which grows as a², is the note's clock: the Siegel distance from the self-dual point Z = i (§5). See [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), which began as a chat-only conjecture, and its dead clause, [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce).

## Scope and caveats

- **Minisuperspace.** The derivation concerns a homogeneous universe with one scale factor per description. No document extends it to an inhomogeneous H.
- **Not machine-checked.** The constraint is derived [D] and no `verify/` script derives it. Only the unimodularity of the modular parametrization is checked: at one sampled point for d = 4 by the battery, and symbolically for d = 1 by `verify/phase_space_diameter.py`.
- **A structural geometry.** The |Z| = 1 reading is stated, not derived through an explicit map from (a, ã) to Z, and it is queried in `review/wiki-build-flags.md` item 23. The phase-space-diameter note reads a·ã = 1 as det H = 1 along the slice X = 0 and |Z| = 1 as the set of square rectangles (§5); the flag awaits Paul's ruling.
- **No test of the program.** In general relativity the one-cell statement already holds, so its many-cell form, the diameter relation, holds in standard cosmology (`papers/phase-space-diameter.md` §3).
- **Normalization.** The constant is set to 1 by choice; only its constancy is physical.

## History

- **Lab notebook, v0.1.** Derived in #1 §6 under strict P2, which #1 §1 credits with enforcing it.
- **Lab notebook, v0.3 addendum.** P2 replaced by P2′; the constraint appears "as the |Z| = 1 locus" of the modular field, a reading queried in flag 23 of `review/wiki-build-flags.md`.
- **Calc note #5** (§C, §F): "the minisuperspace duality was the shadow of this modular action"; det H = 1 as "the geometric face of ℏ-rigidity".
- **#9 §8**: "ω-rigidity fixes the comoving phase-space cell: a·ã = 1. Not an assumption — the statement that ℏ does not run; geometrically, the |Z| = 1 self-dual locus."
- **#11 §10** is the current statement, and App. A item 6 records the founding supposition's promotion.
- **The phase-space-diameter note, version 1.1 (2026-10-26)** (§3, §5): a·ã = 1 as the one-cell form of the diameter relation, which already holds in general relativity; |Z| = 1, Z = i and det H = 1 read as three distinct loci on wave packets.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the current statement, its tag and "one motion written twice"
- `papers/broken-born-checkpoint-v2.md` §6 — the |Z| = 1 locus and scale-factor duality g → g⁻¹
- `papers/broken-born-checkpoint-v2.md` §4 — P2′: "symplectic rigidity ≡ constancy of ℏ"
- `papers/broken-born-checkpoint-v2.md` §2, §5 — det H = 1 "across the whole family" and as a corollary of the compatibility theorem
- `papers/broken-born-checkpoint-v2.md` App. A item 6 — founding supposition 6, "promoted to theorem"
- `notes/broken-born-theory.md` §6 — the derivation from a fixed phase-space cell
- `notes/broken-born-theory.md` §1 — the original P2 and its "triple duty"
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight): axiom correction and the modular core' — P2′ and the |Z| = 1 locus
- `notes/geometric-core.md` §A, §C, §F — unimodularity; "the shadow of this modular action"; det H = 1 as the geometric face of ℏ-rigidity
- `notes/broken-born-program-v1.md` §8 — v1's statement: "Not an assumption — the statement that ℏ does not run"
- `verify/battery.py` T2 — det H_Z = 1 for one sampled member of the Siegel family, executed
- `papers/phase-space-diameter.md` §3 — a·ã = 1 as the one-cell statement of the diameter relation, and its holding in general relativity
- `papers/phase-space-diameter.md` §5 — the three loci |Z| = 1, Z = i and det H = 1 on wave packets, beside the record's identification
- `papers/phase-space-diameter.md` §6 — the |Z| = 1 identification as the likely origin of the withdrawn square [D, inference], and the measured aspect ratio against it
- `verify/phase_space_diameter.py` 'Reciprocity on a rectangle; wave packets (note §5)' — det H_Z = 1 at every Z for d = 1, symbolically
- `review/round5-adjudication.md` 'Recommendations to Paul' — the recommendation to accept flag 23
- `review/wiki-build-flags.md` items 23, 25 — the |Z| = 1 identification (awaiting Paul's ruling) and the §7 pointer slip
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — the redshift gloss (popular article; explanation only)
- `notes/closed-universe.md` §2, §7; `review/wiki-build-flags.md` item 27's addendum and item 49 — the turnaround in a closed universe, and the underived dual term with its physical combinations
