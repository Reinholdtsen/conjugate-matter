---
title: "Open: one modular structure for both polarizations (OP8)"
weight: 80
status: open
description: "Are choosing 'space' and choosing 'electric' components of one enlarged modular structure, as T- and S-duality sit inside U-duality? The conjecture of §11.3; the item also asks for a test of P.R.'s magnetic-mirror conjecture (§11.4), which is what §11.3's conjecture would give if one vacuum event made both choices."
provenance: [O]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.3"
  - "papers/broken-born-checkpoint-v2.md §11.4"
  - "papers/broken-born-checkpoint-v2.md §14 item 8"
  - "papers/broken-born-checkpoint-v2.md §14 item 11"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/skeptic-review-console.html"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/wiki-build-flags.md flag 60"
  - "review/wiki-build-flags.md flag 28"
  - "review/wiki-build-flags.md flag 62"
  - "notes/literature-check.md §5"
---

*This open problem asks whether two choices the program treats in parallel are parts of one structure: the vacuum's choice of which phase-space directions count as position (postulate [P5](/wiki/program/postulates/p5-spontaneous-selection)), and the choice of which charges count as electric, which is a polarization of the charge lattice. Both choices are made with the same quarter-turn matrix, and [the checkpoint](/wiki/history/documents/checkpoint) conjectures that they are components of one larger "modular" structure, on the model of string theory, where T-duality and [S-duality](/wiki/electric-magnetic-duality/s-duality) are both contained in a larger U-duality. It is open problem 8 of the checkpoint, tagged [O]. The checkpoint also records P.R.'s [magnetic-mirror conjecture](/wiki/electric-magnetic-duality/magnetic-identification), which is what the unification conjecture would give if one vacuum event made both choices: each electrically charged particle of ours would have a magnetically charged analog in the momentum-polarized matter sector. The open problem asks for a test of that conjecture as well. The checkpoint does not say what the larger structure would be, no calculation toward it exists in the repository, and it is not in the current work queue. The [toy models](/wiki/symmetry-breaking/toy-models) that met the program's [first acceptance criterion](/wiki/symmetry-breaking/toy-models/acceptance-criterion) did not address the related demand that the [order parameter](/wiki/symmetry-breaking/order-parameter) also select the electric charges.*

**Status:** Open — [O]; the U-duality analogy it invokes is [T] — #11 §11.3, §11.4 and §14 item 8. Listed with the program's [open problems](/wiki/status/open-problems); it qualifies [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice). Nothing here is derived or machine-checked.

## The item and the conjecture

[#11](/wiki/history/documents/checkpoint) §14 item 8: "Charge-lattice polarization: formalize §11.3's unification, and test P.R.'s magnetic-mirror conjecture (§11.4) [O]." It adds that the soliton-spectrum and p-localization items are open, "since the third candidate of §12 and §11.4's shared-photon form need p-localization: "p-local solitons are p-localized" [O]" ([the sub-items](#the-sub-items-the-soliton-spectrum-and-p-localization)).

The unification it refers to ends #11 §11.3:

> Conjecture [O]: the phase-space polarization (P5) and the charge-lattice polarization are components of one enlarged modular structure — the BBT-native analog of T- and S-duality cohabiting inside U-duality in string theory [T].

BBT, Broken-Born theory, is the program's earlier name. OP8 is the wiki's label for this item.

### The magnetic-mirror conjecture

#11 §11.4, "The magnetic-mirror conjecture [O]", ties P.R.'s conjecture to this one:

> P.R.'s conjecture: momentum matter is similar to position matter, each electrically charged x-polarized particle having a magnetically charged p-polarized analog. It joins founding suppositions 5 and 11 (Appendix A), and it is what §11.3's conjecture would give if one vacuum event selected both the position polarization and the electric sublattice.

It has two forms. In the separate-photon form the analogs are magnetic under the momentum-polarized sector's own gauge field; in the shared-photon form they carry magnetic charge of our photon. Both, and what each needs, are on [Conjecture: the momentum sector as the magnetic mirror](/wiki/electric-magnetic-duality/magnetic-identification).

## The two polarizations

### On phase space

Postulate P5: "The vacuum selects a polarization; ours is x-tilted; the mirror vacuum is equally lawful." [P] (#11 §4; [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection)). A polarization is a choice of Lagrangian subspace, the half of phase space that counts as position ([Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)). The choice is a continuous angle: with only the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) rigid, ρ "sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (#11 §4; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

The structure the conjecture calls "modular" on this side is the program's modular field. With only ω rigid, the phase-space metric ranges over the [Siegel domain](/wiki/phase-space/modular-field/siegel-domain) Sp(2d,ℝ)/U(d), parametrized by Z = X + iY; reciprocity acts as "ρ: Z → −Z⁻¹ (Möbius; d = 1 check), fixed point Z = i"; and "Λ(d) is the Shilov boundary of the Siegel domain [T]", where Λ(d) is the space of polarizations and the dark-energy field τ is a phase on it (#11 §6; [the modular field Z](/wiki/phase-space/modular-field/modular-field-z); [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion); [the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian)).

### On charge space

The [Dirac–Schwinger–Zwanziger pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) makes the lattice of electric and magnetic charges a symplectic space; mutually local charges form a Lagrangian sublattice; and "Choosing a duality frame — which particles are "electric" (fundamental) versus "magnetic" (solitonic) — is choosing a Lagrangian polarization of charge space" (#11 §11.3; [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). The "modular" structure on this side is the action of duality on the complexified coupling, the action of [the modular group SL(2, ℤ)](/wiki/electric-magnetic-duality/modular-group#the-complexified-coupling-t): "S-duality acts on the complexified coupling by τ_c → −1/τ_c, generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹" ([S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality)).

### What the conjecture adds

#11 §11.3 establishes, as a structural observation [D — structural; math T], that the two choices are the same kind of operation and share a generator. The conjecture goes further: that they are not two copies of one operation but two components of a single structure. The checkpoint does not name the enlarged structure or say how the components would combine. §11.4 records a conjecture that would follow from it, but no mechanism: "a mechanism by which one order parameter makes both choices" heads its list of what stays open (the electric-sublattice clause, below).

| | phase space | charge space |
| --- | --- | --- |
| what is chosen | which directions are "position" | which charges are "electric" |
| who chooses | the vacuum (P5) [P] | the description (a duality frame) [T] |
| the modular action | ρ: Z → −Z⁻¹ on the Siegel domain | S: τ_c → −1/τ_c on the coupling |
| status of the choice in the program | spontaneous, a Goldstone angle [D][V] | not modelled |

## The model: T and S inside U [T]

In string theory two dualities of different origin are parts of one symmetry group [T]:

- **T-duality** relates a string theory on a circle of radius R to a theory on a circle of radius 1/R in string units. It exchanges the string's momentum around the circle with the number of times the string winds around it, in the way a waveform and its spectrum exchange roles.
- **S-duality** relates strong and weak string coupling, and contains the Montonen–Olive duality of gauge theories as a special case ([S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality)).
- **U-duality**, proposed by Hull and Townsend (1995)†, is a larger discrete symmetry of the type II superstrings on a torus that contains both.

On the natural reading of the analogy, the program's ρ, a position–momentum exchange like T-duality's momentum–winding exchange, and the charge-lattice S are the two parts, and the conjecture asks for the program's counterpart of U; #11 does not spell out the correspondence. The comparison with T-duality has a further echo in the record: #11 §7.1 contrasts the partner field of its own doubled phase-space geometry, the symmetric [momentum graviton](/wiki/gravity/momentum-graviton), with the antisymmetric [B-field](/wiki/phase-space/born-geometry/kalb-ramond-field#set-against-the-momentum-graviton) of string theory's doubled geometry, [double field theory](/wiki/phase-space/born-geometry/double-field-theory) [T].

## The earlier, stronger form

The soliton manuscript's v2 ([#14](/wiki/dark-matter/candidates/soliton-candidate)) had stated the unification as a physical identification, with a number attached. Its §2, preserved verbatim in `review/skeptic-review-console.html`:

> Conjecture (the identification). The two polarization choices are made by the same vacuum event, and the momentum-polarized matter sector is the S-dual image of the electric sector: a distinct gauge structure whose complexified coupling is fixed by the reciprocity map, acting as the modular S transformation, to the image of ours - alpha_d = 1/(4 alpha) ~ 34, quoted in the Dirac normalization (the Schwinger convention shifts this by the standard factor of four).

That version made reciprocity act on gauge couplings. [Round 2](/wiki/method/review/rounds-one-and-two) judged its derivation of the coupling "numerology", with "matrix coincidence ≠ physical identity" (`HANDOFF.md` §6). The worklog's finding F2 then showed that v2 used both a weak and a strong value of the dual coupling, and proposed a reading in which the strong monopole coupling did not need S acting on our coupling. #14 v3 adopted the reading: "S-duality is no longer what fixes α_d" (`review/v3-worklog.md`, 'Findings neither referee raised'). v3 kept the correspondence "only as motivation", and the manuscript was later withdrawn ([Under review: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).

The decision to adopt that reading is withdrawn, and F2's finding stands (flag 60 in `review/wiki-build-flags.md`). #11 records P.R.'s magnetic-mirror conjecture (§11.4 [O]), and says that #14 v2 "stated a related identification". #14 v2 called that identification load-bearing for its dual coupling α_d, and a full mirror spectrum appeared there only as something the sector "may carry". #14 v2's version is the conjecture's separate-photon form: "The analogs are magnetic under the p-polarized sector's own gauge field, whose coupling is the S-image of ours. Whether that is the sector's elementary coupling or its magnetic one is open; F2's finding is that the choice decides whether the sector's solitons are heavy." #14 is withdrawn (§12). The conjecture of #11 §11.3 makes no claim about couplings or about a hidden sector; the separate-photon form of §11.4 does. §11.4 lists round 2's supersymmetry-exactness burden ([the exactness burden](/wiki/electric-magnetic-duality/s-duality#the-exactness-burden)), with the dual coupling's factor-of-4 convention spread, among what stays open in either form (the formula printed beside 34 in §11.2 is flag 28).

## Open: the electric-sublattice clause

Two older wordings of the program's first acceptance criterion tied the order parameter to this conjecture.

- [The handoff](/wiki/history/documents/handoff)'s first open item: "Toy Lagrangian in which ρ is a genuine Noether symmetry, spontaneously broken, η the order parameter also selecting the electric sublattice (acceptance criterion #1; both reviewers independently named it)" (`HANDOFF.md` §2).
- #14's criterion (1): "exhibition of an action - a toy model suffices - in which rho is a genuine Noether symmetry, spontaneously broken, with eta the order parameter selecting both the position polarization and the hidden sector's electric description; deriving hypothesis H from that action would make the coupling a prediction" (#14 §6; [#14](/wiki/dark-matter/candidates/soliton-candidate)).

#11 §14 item 11 declares the toy-Lagrangian criterion "Met in the referees' wording" by the [coset model](/wiki/symmetry-breaking/toy-models/coset-model), and the root `CLAUDE.md` says it is "done to the referees' wording". The toy models contain no gauge field and no charge lattice, and nothing in the repository addresses the clause ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)). An order parameter that selected both polarizations would be one concrete form of the conjecture.

#11 §11.4 lists the clause first among what stays open in either form of the magnetic-mirror conjecture: "a mechanism by which one order parameter makes both choices (the electric-sublattice clause of acceptance criterion 1, never attempted; the toy models of §14 item 11 contain no gauge field)". The root `CLAUDE.md` lists the same mechanism among the items "Open from the monopole discussion, not queued".

## The sub-items: the soliton spectrum and p-localization

The soliton spectrum is an item of the candidate that #14 modeled, and it is open with that candidate, P.R.'s conjecture of [magnetic monopoles abundant in momentum space](/wiki/dark-matter/candidates/momentum-space-monopoles). On p-localization, #11 §12 says: "The clumping loophole — topological momentum-space localization of individual objects — remains untested; its candidate is P.R.'s conjecture of conjugate monopoles (table above)". §12 and §14 item 8 both call the item open ([Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).

The shared-photon form needs p-localization, or another way to hide its analogs. #11 §11.4: "Something must therefore hide them, and neither option has been computed": p-localization ("p-local solitons are p-localized" [O]), "with the spread in the objects' field profile rather than their quantum state, wider than detectors and than the coherence length of galactic magnetic fields, and decoupled from the photon–baryon plasma before recombination (†)"; or "binding into magnetically neutral composites ("heavy and bound", §11.2)" ([shared photon](/wiki/electric-magnetic-duality/magnetic-identification#shared-photon)).

## In the literature

The bridge the conjecture builds on, that electric–magnetic duality is a case of Born reciprocity, is a published remark, made for the phase space of the electromagnetic field, whose conjugate pair is B and D, not for the position and momentum of matter. Gibbons and Herdeiro 2001 write that "electric-magnetic duality is a special case of Born-Reciprocity", "a transformation which acts as a rotation in phase space", and Russo and Townsend 2025 call the Z₂ that remains of the duality group of self-dual nonlinear electrodynamics in the quantum theory "an example of Born-reciprocity" [S]. Berglund, Hübsch and Minic 2021 make two gauge groups of a string theory, one built on ordinary and one on dual coordinates of its extra dimensions, each other's electric–magnetic duals through the metric of Born geometry, for gauge groups only, the two being "physically indistinguishable"; each group has visible fields and a dark counterpart in the same group, so their dark sector is not the electric–magnetic dual of ours; Freidel, Leigh and Minic 2014 (Phys. Lett. B), the first paper of #11's [3]†, tie the Dirac–Schwinger–Zwanziger pairing of worldsheet dyons, which carry momentum and dual momentum, to the diffeomorphism constraint; and other work casts S-duality as a canonical transformation, as T-duality or as a Fourier transform (Lozano 1995; Harvey, Moore and Strominger 1995; Kapustin and Witten 2007; Galakhov, Mironov and Morozov 2014) [S]. The conjecture itself, one enlarged modular structure in which one vacuum event selects both polarizations, was not found ([the literature check](/wiki/method/literature-check); flag 67, pending).

## Where it stands

- **Counted as progress.** #11 §15 lists "the §11.3 unification generating new questions" among the program's progressive signs, and "one structural unification (polarization of phase space and of charge space as one move)" among what it has produced ([the program's self-assessment](/wiki/program/assessment)).
- **Not queued.** The current queue in the root `CLAUDE.md` is the [partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison) and the [† literature battery](/wiki/method/literature-battery) (`HANDOFF.md` §8 items 5–6), then an optional round-6 review of the toy note. Item 8 is not on it. The same file lists the magnetic-mirror conjecture's open items under "Open from the monopole discussion, not queued": for the third dark-matter candidate and the explanation of the monopole null result, p-localization and the kinematics of momentum-polarized matter, never modeled; the mechanism; for the separate-photon form, which coupling of the momentum-polarized sector is the S-image of ours, and round 2's supersymmetry burden; for the shared-photon form, p-localization in the field profile and the momentum width that would hide the analogs from detectors, from the Parker bound and from the plasma before recombination, or their binding into magnetically neutral composites, or screening by a magnetic condensate; and the dual coupling's convention. The explanation of the null result is P.R.'s open conjecture, in the shared-photon form's setting (flag 62; [Conjecture: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation)).
- **No calculation.** Nothing in `papers/`, `notes/` or `verify/` works toward the enlarged structure or tests the magnetic-mirror conjecture.
- **The caution on record.** Round 2's weakest link was a coupling derived from the shared matrix, which the referee called "matrix coincidence ≠ physical identity" (`HANDOFF.md` §6). The conjecture asks for a structure behind the coincidence; it is stated, not derived. §11.4 keeps the objection open in either form, since [[0,1],[−1,0]] "is the canonical form of any two-dimensional symplectic pairing [T]".

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.3 — the conjecture [O] and the U-duality analogy [T]; §11.4 — P.R.'s magnetic-mirror conjecture, what §11.3's conjecture would give if one vacuum event made both choices, with its two forms and what stays open [O]; §14 item 8 — the open item and its sub-items; §14 item 11 — the toy criterion as met; §4 — P5 and the Goldstone angle; §6 — the modular field; §7.1 — the contrast with double field theory; §12 — the loophole and its candidate; §15 — the assessment.
- `CLAUDE.md` 'Since the handoff' — the current queue; the toy Lagrangian "done to the referees' wording"; the items open from the monopole discussion.
- `HANDOFF.md` §2 — the electric-sublattice clause in the first open item; §6 — round 2's caution.
- `notes/knot-dark-matter-standalone.md` §2, §6 — "only as motivation"; acceptance criterion (1) with the electric description (withdrawn manuscript).
- `review/skeptic-review-console.html` — #14 v2's identification conjecture, verbatim.
- `review/v3-worklog.md` 'Findings neither referee raised' (F2) — the finding that v2 used two values of the dual coupling, and the reading #14 v3 adopted.
- `review/wiki-build-flags.md` flag 60 — #14 v2's identification, and F2's finding; flag 28 — the formula printed beside 34 in §11.2; flag 62 — the explanation of the null result open, in the shared-photon form's setting.
- `notes/literature-check.md` §5 — the published remarks on the two dualities; `review/wiki-build-flags.md` item 67
