---
title: "S-duality and Montonen–Olive"
weight: 20
status: established
description: "Electric–magnetic duality as strong–weak duality, exact only in maximally supersymmetric Yang–Mills; Seiberg's magnetic quarks; T-, S- and U-duality in string theory; and the exactness burden on any use the program makes of it."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §11.2"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.3"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.4"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §11 (italic opening)"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [18]"
  - "CLAUDE.md 'Since the handoff'"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/wiki-build-flags.md flag 60"
  - "review/v3-worklog.md 'Verified references for v3'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md ref [8]"
  - "HANDOFF.md §6"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*S-duality is the proposed equivalence between a gauge theory at coupling g and a theory at a coupling of order 1/g in which electrically charged particles and [magnetic monopoles](monopoles/_index.md) exchange roles, so that a strongly coupled theory has a weakly coupled description. It grows out of a symmetry of Maxwell's equations in empty space, which are unchanged when the electric and magnetic fields are exchanged. Montonen and Olive proposed the quantum version in 1977. [The checkpoint](../history/documents/checkpoint.md) records it as exact in maximally supersymmetric Yang–Mills theory, one of the few theories in which it has passed non-trivial tests, and Seiberg's related dualities supply the "magnetic quarks" of a dual description. In string theory S-duality sits with T-duality inside a larger U-duality. The program uses S-duality as a structural comparison, because it acts on the coupling through the same matrix as [Born reciprocity](../phase-space/reciprocity/born-reciprocity.md), and in one form of P.R.'s open [magnetic-mirror conjecture](magnetic-identification.md) the program's momentum-polarized matter has a gauge field of its own whose coupling is the image of ours under S. The duality carries a standing caution: outside special supersymmetric theories it is an expectation, not an established symmetry.*

**Status:** Established — [T] — the checkpoint cites Montonen–Olive 1977 and Seiberg 1995 as [18†], from model memory, so the citations await [the † literature battery](../method/literature-battery.md). [The round-3 audit](../method/review/round-3/rulings.md) checked the citations of the withdrawn [#14](../dark-matter/candidates/soliton-candidate/_index.md) to Montonen–Olive, Osborn 1979 and Harvey ([hep-th/9603086](https://arxiv.org/abs/hep-th/9603086)) and found that they support the exactness caveat (Step 1). The explanations below that go beyond the documents are textbook physics [T], and the references they add are marked †.

## Duality in Maxwell's equations [T]

Without charges, Maxwell's equations keep their form when the fields are exchanged as E → B, B → −E (units with c = 1). The exchange is a quarter-turn in the plane of (E, B), and applying it twice reverses both fields:

```text
(E, B) → (B, −E) → (−E, −B)
```

Electric charges spoil the symmetry, because Gauss's law for E has a source and Gauss's law for B does not. Adding magnetic charges and currents restores it, with the electric and magnetic sources exchanged together with the fields. A particle carrying magnetic charge alone is a magnetic monopole ([magnetic monopoles](monopoles/_index.md)).

In quantum mechanics the two kinds of charge are not independent. Dirac showed in 1931 that a monopole of charge g can coexist with an electric charge e only if their product is quantized; the checkpoint writes the condition e·g ~ 2π ([#11 §11.2](../papers/broken-born-checkpoint-v2.md#112-the-full-dual-spectrum-t); [Dirac quantization and the DSZ pairing](monopoles/dirac-quantization.md), where DSZ is Dirac–Schwinger–Zwanziger). A small electric charge therefore forces a large magnetic one. Exchanging the electric and magnetic descriptions of a theory exchanges weak coupling with strong coupling, which is why the quantum form of the duality is also called strong–weak duality. [#11 §11.1](../papers/broken-born-checkpoint-v2.md#111-the-monopole-audit-revised-d) abbreviates it as "electric–magnetic (E↔B, g → 1/g)".

## The coupling and the generator S [T]

A gauge theory's coupling g and its vacuum angle θ combine into the complexified coupling τ_c = θ/2π + 4πi/g² [T]; the notation is #11's, and τ_c is unrelated to the dark-energy field τ ([notation](../notation.md)). Duality transformations act on τ_c through [the modular group SL(2, ℤ)](modular-group.md), generated by T: τ_c → τ_c + 1, the shift of θ by 2π, and S = [[0, 1], [−1, 0]]: τ_c → −1/τ_c, the exchange of electric and magnetic charges [T]. At θ = 0, S sends τ_c = 4πi/g² to ig²/4π, the same form with g replaced by 4π/g [T]. [#11 §11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) states the action the program uses: "S-duality acts on the complexified coupling by τ_c → −1/τ_c, generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹". The matrix is also the quarter-turn of the Maxwell exchange above and of Born reciprocity, (x, p) → (p, −x); the program's use of the coincidence is the subject of [the symplectic charge lattice](symplectic-charge-lattice.md).

## Montonen–Olive duality [T]

The simplest gauge theory with monopoles has an SU(2) symmetry broken to U(1) by a Higgs field in the adjoint representation. Its spectrum contains electrically charged vector bosons W± of mass g·v, where v is the symmetry-breaking scale, and magnetically charged ['t Hooft–Polyakov monopoles](monopoles/thooft-polyakov-monopole.md) of mass M = 4πf v/g, with f = 1 in the Bogomolny–Prasad–Sommerfield (BPS) limit of a vanishing Higgs self-coupling ([#14 §2](../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling), [§3](../../notes/knot-dark-matter-standalone.md#3-the-candidate) give both formulas for the [hidden sector](../dark-matter/candidates/soliton-candidate/hidden-sector.md)). In that limit the exchange g → 4π/g turns the W mass into the monopole mass and back [T].

Montonen and Olive took the symmetry of the mass spectrum as a sign of an exact duality: a dual theory, at coupling 4π/g, in which the monopoles are the elementary gauge particles and the W bosons are the solitons. Their title states the conjecture as a question, "Magnetic monopoles as gauge particles?" (#11 ref [18]†).

The proposal has a defect in the bosonic theory, which the v3 worklog states: "the bosonic spectrum mismatches (W spin 1, monopole spin 0)". The W is a vector particle and the monopole is not, so the two cannot be exchanged by an exact symmetry. In N = 4 super Yang–Mills theory (SYM), which has the most supersymmetry (SUSY) a four-dimensional gauge theory without gravity can have, the monopoles come in multiplets that include spin 1, so the mismatch disappears; #14 cites Osborn 1979 for this setting (#14 ref [8]). The checkpoint's summary is that Montonen–Olive duality is "exact in maximally supersymmetric Yang–Mills" ([#11 §11.2](../papers/broken-born-checkpoint-v2.md#112-the-full-dual-spectrum-t) [T]).

How well tested the exactness is depends on the theory. Harvey's lectures, as the round-3 referee quoted them after checking the source: the duality has been "put to non-trivial tests in finite N = 4 Super Yang-Mills theory and special finite N = 2 theories", while for the non-supersymmetric theory "there is no reason to think that the duality of the spectrum should be maintained by quantum corrections" ([`review/round3/referee/audit-notes.md`](../../review/round3/referee/audit-notes.md), Step 1).

## Seiberg duality and magnetic quarks [T]

Seiberg found a related equivalence in N = 1 supersymmetric versions of quantum chromodynamics (QCD), the theory of quarks and gluons. A theory with a given number of colors and quark flavors has, at long distances, the same physics as a second gauge theory with a different number of colors, whose charged matter fields are called "magnetic quarks" [T, Seiberg 1995 [18†]]. In part of the range of flavors, the second description is weakly coupled where the first is strongly coupled. The equivalence holds for the long-distance limit of the two theories, not at every scale [T].

#11 cites it for the vocabulary: "magnetic quarks" is "standard vocabulary via Seiberg duality [18†]" ([§11.2](../papers/broken-born-checkpoint-v2.md#112-the-full-dual-spectrum-t)). The checkpoint's italic opening dates the idea "proposed in 1977, named in 1994"; its reference list dates Seiberg's paper 1995, the journal year, while the preprint number [hep-th/9411149](https://arxiv.org/abs/hep-th/9411149) dates from November 1994 [T]. The popular article [#12](../../popsci/universes-other-half.md) says that "'magnetic quark' has been standard vocabulary in field theory since the 1990s" ([the popular articles](../history/documents/popular-articles.md)).

## T-, S- and U-duality in string theory [T]

String theory has dualities of two kinds [T]:

- **T-duality** relates a closed string theory on a circle of radius R to the same or a related theory on a circle of radius 1/R in string units. A closed string on a circle carries two whole numbers, its momentum around the circle, as a wave on a ring does, and the number of times it winds; T-duality exchanges them. The doubled geometry that makes the exchange manifest is the subject of [double field theory](../phase-space/born-geometry/double-field-theory.md).
- **S-duality** in string theory relates strong and weak string coupling, and in some compactifications reduces to Montonen–Olive duality of the four-dimensional gauge theory.

Hull and Townsend (1995)† proposed that in the type II superstrings on a torus both are parts of a single larger discrete symmetry, U-duality. [#11 §11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t) describes the situation as "T- and S-duality cohabiting inside U-duality in string theory [T]", and uses it as the model for its conjecture that the program's two polarization choices are parts of one structure ([open problem 8](unified-modular-structure.md); OP8 is item 8 of [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems)).

## The exactness burden

Any argument that needs S-duality as an exact symmetry outside supersymmetric theories inherits the caution above. The burden arose in the program through the soliton manuscript #14, whose second version fixed the hidden sector's coupling by a conjectured action of reciprocity as the modular S map ([Under review: the coupling α_d ≈ 34](../dark-matter/candidates/soliton-candidate/alpha-d-coupling.md)).

- **Round 2 posed it.** Among the valid hits pending for v3: "SUSY-exactness burden for Montonen–Olive (either reciprocity supplies the rigidity or the dual sector is approximately SUSY)" ([`HANDOFF.md` §6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode); [review rounds 1 and 2](../method/review/rounds-one-and-two.md)).
- **The worklog answered it** as item R1, marked "ready": "Exact S-duality has been tested only in N=4 SYM and special finite N=2 theories. For non-SUSY theories there is "no reason to think" it survives quantum corrections, and the bosonic spectrum mismatches (W spin 1, monopole spin 0). That is an expectation, not a no-go [Harvey [hep-th/9603086](https://arxiv.org/abs/hep-th/9603086); Osborn 1979]. v3 must state it. If F2 is adopted, S no longer carries α_d, and the burden shrinks to the §2 "full mirror spectrum" remark." ([`review/v3-worklog.md`](../../review/v3-worklog.md), 'Round-2 pending list').
- **F2's reading.** Finding F2 showed that #14 v2 used both a weak and a strong value of the dual coupling, and proposed a reading that separated the hidden sector's weak elementary coupling from its monopoles' strong coupling. #14 v3 adopted the reading: "S-duality is no longer what fixes α_d" ('Findings neither referee raised'). The decision to adopt it is withdrawn, and the finding stands ([#11 §11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)).
- **v3 stated it.** "Exact electric-magnetic duality is also not assumed. It has been tested non-trivially only in N=4 super-Yang-Mills and certain finite N=2 theories, and there is no reason to expect it to survive quantum corrections in a non-supersymmetric theory [8]. Nothing here requires it: the monopole physics used is semiclassical, at alpha_W' ~ 1/34." ([#14 §2](../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling)). The manuscript was withdrawn after round 3 over its abundance arithmetic ([Obituary: #14's superheavy-soliton model](../dark-matter/candidates/soliton-candidate/obituary.md)).
- **The checkpoint today** cites Montonen–Olive as literature for the [magnetic mirror-family](magnetic-mirror-family.md), stating exactness only for maximally supersymmetric Yang–Mills ([§11.2](../papers/broken-born-checkpoint-v2.md#112-the-full-dual-spectrum-t)). It uses S for its action on τ_c ([§11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t)) and in the separate-photon form of P.R.'s magnetic-mirror conjecture [O]. That form is #14 v2's, whose S-dual identification #11 calls a related one: the analogs are magnetic under the momentum-polarized sector's own gauge field, "whose coupling is the S-image of ours", and "Whether that is the sector's elementary coupling or its magnetic one is open" ([§11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23); [Conjecture: the momentum sector as the magnetic mirror](magnetic-identification.md)). F2's finding stands (flag 60 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md)), and #14 is withdrawn. The burden stands: §11.4 lists among what stays open in either form "round 2's burden that exact S-duality is established only with extended supersymmetry, so either reciprocity supplies the rigidity or the dual sector is approximately supersymmetric", citing R1, which ties the burden's size to whether S carries α_d. The root [`CLAUDE.md`](../../CLAUDE.md) lists the burden among the items open from the monopole discussion.

## How the program uses it

- **As established physics behind [founding supposition 11](../program/founding-suppositions.md).** P.R.'s supposition of "A full magnetic mirror-family, quarks included" is "alive as established physics (Montonen–Olive, Seiberg, dual superconductor)" ([#11 App. A item 11](../papers/broken-born-checkpoint-v2.md#appendix-a-audit-of-founding-suppositions-pr-with-fates); [the dual superconductor](dual-superconductor.md)).
- **As the third appearance of one matrix.** S's matrix is the matrix of ρ and of the modular inversion Z → −Z⁻¹ ([reciprocity as modular inversion](../phase-space/modular-field/modular-inversion.md)); #11 calls this "the third appearance of one matrix in this program" ([the symplectic charge lattice](symplectic-charge-lattice.md)); that electric–magnetic duality is a case of Born reciprocity, in the phase space of the electromagnetic field, is a published remark (flag 67 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md), pending).
- **As the model for open problem 8.** The U-duality inclusion is the analogy for one enlarged structure containing both polarization choices ([open problem 8](unified-modular-structure.md)).
- **In P.R.'s magnetic-mirror conjecture** [O]: "momentum matter is similar to position matter, each electrically charged x-polarized particle having a magnetically charged p-polarized analog" ([#11 §11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)). In its separate-photon form, #14 v2's, the analogs are magnetic under the momentum-polarized sector's own gauge field, "whose coupling is the S-image of ours" ([separate photon](magnetic-identification.md#separate-photon)).
- **In the first ground against P.R.'s explanation of the missing monopoles.** [#11 §11.1](../papers/broken-born-checkpoint-v2.md#111-the-monopole-audit-revised-d) sets against that explanation the point that electric–magnetic duality, not Born reciprocity, is the duality that relates magnetic charges to electric ones, a ground that, in #11's words, "only the shared-photon form of §11.4 contests". The explanation is P.R.'s open conjecture [O], since "neither ground given against it kills it" ([§11.1](../papers/broken-born-checkpoint-v2.md#111-the-monopole-audit-revised-d); [Conjecture: conjugate monopoles explain the null result](monopole-explanation.md)).

## Standard references

As the documents cite them:

- C. Montonen, D. Olive, "Magnetic monopoles as gauge particles?" Phys. Lett. B 72, 117 (1977) — #11 [18]†; #14 [8].
- N. Seiberg, "Electric–magnetic duality in supersymmetric non-abelian gauge theories," Nucl. Phys. B 435, 129 (1995), [hep-th/9411149](https://arxiv.org/abs/hep-th/9411149) — #11 [18]†.
- H. Osborn, Phys. Lett. B 83, 321 (1979) — #14 [8].
- J. A. Harvey, "Magnetic monopoles, duality and supersymmetry," [hep-th/9603086](https://arxiv.org/abs/hep-th/9603086) — #14 [8]; conference proceedings, not a journal article ([`review/v3-worklog.md`](../../review/v3-worklog.md), 'Verified references for v3').

Added by the wiki from model memory (†); the program's documents do not cite them:

- A. Sen (1994)†: evidence for S-duality in N = 4 theory from bound states of monopoles.
- N. Seiberg and E. Witten (1994)†: the exact low-energy solution of N = 2 Yang–Mills theory, with monopole condensation after a breaking to N = 1.
- C. M. Hull and P. K. Townsend (1995)†: U-duality.

## Used by

- [The symplectic charge lattice](symplectic-charge-lattice.md) — τ_c → −1/τ_c as the third appearance of the matrix [[0,1],[−1,0]].
- [Reciprocity as modular inversion Z → −Z⁻¹](../phase-space/modular-field/modular-inversion.md) — the same matrix generates S on the coupling.
- [P3: a reciprocity-invariant action](../program/postulates/p3-reciprocity.md) — the recurring matrix.
- [Open: one modular structure for both polarizations (OP8)](unified-modular-structure.md) — the U-duality analogy.
- [The magnetic mirror-family](magnetic-mirror-family.md) — Montonen–Olive duality as the established form of founding supposition 11.
- [Conjecture: conjugate monopoles explain the null result](monopole-explanation.md) — electric–magnetic duality as the relevant duality, the first ground given against the explanation.
- [Row 8: no monopoles of our sector](../predictions/monopole-null.md) — electric–magnetic duality, not Born reciprocity, relates magnetic charges to electric ones.
- [Founding suppositions and their fates](../program/founding-suppositions.md) — item 11, "alive as established physics (Montonen–Olive, Seiberg, dual superconductor)".
- [Assessment: a live research program](../program/assessment.md) — S generated by the same matrix as reciprocity, in the charge-lattice unification.
- [Conjecture: the momentum sector as the magnetic mirror](magnetic-identification.md) — in the separate-photon form, the momentum-polarized sector's coupling as the S-image of ours.
- [Under review: the coupling α_d ≈ 34](../dark-matter/candidates/soliton-candidate/alpha-d-coupling.md) — #14 v2's conjecture that reciprocity acts on the coupling as S, which #14 v3 set aside under F2's reading.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §11.2](../papers/broken-born-checkpoint-v2.md#112-the-full-dual-spectrum-t), [§11.3](../papers/broken-born-checkpoint-v2.md#113-the-identification-d--structural-math-t), ref [18] — the statement [T], the action on τ_c, the U-duality analogy, and the citations (†); [§11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23) — P.R.'s magnetic-mirror conjecture, its separate-photon form, and the exactness burden among what stays open [O]; [§11.1](../papers/broken-born-checkpoint-v2.md#111-the-monopole-audit-revised-d) — the first ground of the audit, contested only by [§11.4](../papers/broken-born-checkpoint-v2.md#114-the-magnetic-mirror-conjecture-o-pr-v23)'s shared-photon form, and not held to kill the explanation; [§11](../papers/broken-born-checkpoint-v2.md#11-polarized-charge-lattices-monopoles-duality-frames-and-the-recurring-matrix) italic opening — "proposed in 1977, named in 1994".
- [`CLAUDE.md`](../../CLAUDE.md) 'Since the handoff' — the burden among the items open from the monopole discussion.
- [`review/v3-worklog.md`](../../review/v3-worklog.md) 'Round-2 pending list' (R1), 'Findings neither referee raised' (F2), 'Verified references for v3' — the exactness burden, F2's finding and the reading #14 v3 adopted, Harvey as proceedings.
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) flag 60 — #14 v2's identification, and F2's finding.
- [`review/round3/referee/audit-notes.md`](../../review/round3/referee/audit-notes.md) Step 1 — Harvey's wording, checked against the source.
- [`notes/knot-dark-matter-standalone.md` §2](../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling), [§3](../../notes/knot-dark-matter-standalone.md#3-the-candidate), ref [8] — "Exact electric-magnetic duality is also not assumed"; the W′ and monopole masses; Montonen–Olive, Osborn and Harvey as cited (withdrawn manuscript).
- [`HANDOFF.md` §6](../../HANDOFF.md#6-review-history-and-the-measured-failure-mode) — the round-2 framing of the burden.
- [`popsci/universes-other-half.md`](../../popsci/universes-other-half.md) 'Dark matter as the other polarization' — "magnetic quark" since the 1990s (not a status source).
