---
title: "Open: one modular structure for both polarizations (OP8)"
weight: 80
status: open
description: "Are choosing 'space' and choosing 'electric' components of one enlarged modular structure, as T- and S-duality sit inside U-duality? The conjecture of §11.3."
provenance: [O]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.3"
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
---

*This open problem asks whether two choices the program treats in parallel are parts of one structure: the vacuum's choice of which phase-space directions count as position (postulate [P5](/wiki/program/postulates/p5-spontaneous-selection)), and the choice of which charges count as electric, which is a polarization of the charge lattice. Both choices are made with the same quarter-turn matrix, and [the checkpoint](/wiki/history/documents/checkpoint) conjectures that they are components of one larger "modular" structure, on the model of string theory, where T-duality and [S-duality](/wiki/electric-magnetic-duality/s-duality) are both contained in a larger U-duality. It is open problem 8 of the checkpoint, tagged [O]. The checkpoint does not say what the larger structure would be, no calculation toward it exists in the repository, and it is not in the current work queue. The [toy models](/wiki/symmetry-breaking/toy-models) that met the program's [first acceptance criterion](/wiki/symmetry-breaking/toy-models/acceptance-criterion) did not address the related demand that the [order parameter](/wiki/symmetry-breaking/order-parameter) also select the electric charges.*

**Status:** Open — [O]; the U-duality analogy it invokes is [T] — #11 §11.3 and §14 item 8. Listed with the program's [open problems](/wiki/status/open-problems); it qualifies [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice). Nothing here is derived or machine-checked.

## The item and the conjecture

[#11](/wiki/history/documents/checkpoint) §14 item 8: "Charge-lattice polarization: formalize §11.3's unification [O]. (The soliton-spectrum and p-localization items are closed by the §12 obituary.)"

The unification it refers to ends #11 §11.3:

> Conjecture [O]: the phase-space polarization (P5) and the charge-lattice polarization are components of one enlarged modular structure — the BBT-native analog of T- and S-duality cohabiting inside U-duality in string theory [T].

BBT is the Broken-Born program's name for itself. OP8 is the wiki's label for this item.

## The two polarizations

### On phase space

Postulate P5: "The vacuum selects a polarization; ours is x-tilted; the mirror vacuum is equally lawful." [P] (#11 §4; [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection)). A polarization is a choice of Lagrangian subspace, the half of phase space that counts as position ([Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)). Since v2.2 the choice is a continuous angle: with only the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) rigid, ρ "sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (#11 §4; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)).

The structure the conjecture calls "modular" on this side is the program's modular field. With only ω rigid, the phase-space metric ranges over the [Siegel domain](/wiki/phase-space/modular-field/siegel-domain) Sp(2d,ℝ)/U(d), parametrized by Z = X + iY; reciprocity acts as "ρ: Z → −Z⁻¹ (Möbius; d = 1 check), fixed point Z = i"; and "Λ(d) is the Shilov boundary of the Siegel domain [T]", where Λ(d) is the space of polarizations and the dark-energy field τ is a phase on it (#11 §6; [the modular field Z](/wiki/phase-space/modular-field/modular-field-z); [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion); [the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian)).

### On charge space

The [Dirac–Schwinger–Zwanziger pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) makes the lattice of electric and magnetic charges a symplectic space; mutually local charges form a Lagrangian sublattice; and "Choosing a duality frame — which particles are "electric" (fundamental) versus "magnetic" (solitonic) — is choosing a Lagrangian polarization of charge space" (#11 §11.3; [the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)). The "modular" structure on this side is the action of duality on the complexified coupling: "S-duality acts on the complexified coupling by τ_c → −1/τ_c, generated by the same [[0,1],[−1,0]] rotation as Born's ρ and our Z → −Z⁻¹" ([S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality)).

### What the conjecture adds

#11 §11.3 establishes, as a structural observation [D — structural; math T], that the two choices are the same kind of operation and share a generator. The conjecture goes further: that they are not two copies of one operation but two components of a single structure. The checkpoint does not name the enlarged structure or say how the components would combine.

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

On the natural reading of the analogy, the program's ρ, a position–momentum exchange like T-duality's momentum–winding exchange, and the charge-lattice S are the two parts, and the conjecture asks for the program's counterpart of U; #11 does not spell out the correspondence. The comparison with T-duality has a further echo in the record: #11 §7.1 contrasts the partner field of its own doubled phase-space geometry, the symmetric [momentum graviton](/wiki/gravity/momentum-graviton), with the antisymmetric B-field of string theory's doubled geometry, [double field theory](/wiki/phase-space/born-geometry/double-field-theory) [T].

## The earlier, stronger form

The soliton manuscript's v2 ([#14](/wiki/dark-matter/candidates/soliton-candidate)) had stated the unification as a physical identification, with a number attached. Its §2, preserved verbatim in `review/skeptic-review-console.html`:

> Conjecture (the identification). The two polarization choices are made by the same vacuum event, and the momentum-polarized matter sector is the S-dual image of the electric sector: a distinct gauge structure whose complexified coupling is fixed by the reciprocity map, acting as the modular S transformation, to the image of ours - alpha_d = 1/(4 alpha) ~ 34, quoted in the Dirac normalization (the Schwinger convention shifts this by the standard factor of four).

That version made reciprocity act on gauge couplings. [Round 2](/wiki/method/review/rounds-one-and-two) judged its derivation of the coupling "numerology", with "matrix coincidence ≠ physical identity" (`HANDOFF.md` §6). The worklog's finding F2 then showed that the strong monopole coupling did not need it, and Paul decided on 2026-10-19 that "S-duality is no longer what fixes α_d" (`review/v3-worklog.md`, 'Findings neither referee raised'). v3 kept the correspondence "only as motivation", and the manuscript was later withdrawn ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)). The conjecture of #11 §11.3 makes no claim about couplings or about a hidden sector.

## Open: the electric-sublattice clause

Two older wordings of the program's first acceptance criterion tied the order parameter to this conjecture.

- [The handoff](/wiki/history/documents/handoff)'s first open item: "Toy Lagrangian in which ρ is a genuine Noether symmetry, spontaneously broken, η the order parameter also selecting the electric sublattice (acceptance criterion #1; both reviewers independently named it)" (`HANDOFF.md` §2).
- #14's criterion (1): "exhibition of an action - a toy model suffices - in which rho is a genuine Noether symmetry, spontaneously broken, with eta the order parameter selecting both the position polarization and the hidden sector's electric description; deriving hypothesis H from that action would make the coupling a prediction" (#14 §6; [#14](/wiki/dark-matter/candidates/soliton-candidate)).

#11 §14 item 11 declares the toy-Lagrangian criterion "Met in the referees' wording" by the [coset model](/wiki/symmetry-breaking/toy-models/coset-model), and the root `CLAUDE.md` says it is "done to the referees' wording". The toy models contain no gauge field and no charge lattice, and nothing in the repository addresses the clause ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)). An order parameter that selected both polarizations would be one concrete form of the conjecture.

## The closed sub-items (unresolved)

The parenthesis of item 8 says that "The soliton-spectrum and p-localization items are closed by the §12 obituary". The soliton spectrum was the retired candidate's. On p-localization, #11 §12 says that "The Debt-3 loophole — topological momentum-space localization of individual objects — remains untested, but has no candidate". The checkpoint does not reconcile "closed" with "untested" ([Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).

## Where it stands

- **Counted as progress.** #11 §15 lists "the §11.3 unification generating new questions" among the program's progressive signs, and "one structural unification (polarization of phase space and of charge space as one move)" among what it has produced ([the program's self-assessment](/wiki/program/assessment)).
- **Not queued.** The current queue in the root `CLAUDE.md` is the [partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison), the [† literature battery](/wiki/method/literature-battery) and the phase-space-diameter note (`HANDOFF.md` §8 items 5–7), then an optional round-5 review of the toy note. Item 8 is not on it.
- **No calculation.** Nothing in `papers/`, `notes/` or `verify/` works toward the enlarged structure.
- **The caution on record.** Round 2's weakest link was a coupling derived from the shared matrix, which the referee called "matrix coincidence ≠ physical identity" (`HANDOFF.md` §6). The conjecture asks for a structure behind the coincidence; it is stated, not derived.

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.3 — the conjecture [O] and the U-duality analogy [T]; §14 item 8 — the open item and its "closed" parenthesis; §14 item 11 — the toy criterion as met; §4 — P5 and the Goldstone angle; §6 — the modular field; §7.1 — the contrast with double field theory; §12 — the loophole's wording; §15 — the assessment.
- `CLAUDE.md` 'Since the handoff' — the current queue; the toy Lagrangian "done to the referees' wording".
- `HANDOFF.md` §2 — the electric-sublattice clause in the first open item; §6 — round 2's caution.
- `notes/knot-dark-matter-standalone.md` §2, §6 — "only as motivation"; acceptance criterion (1) with the electric description (withdrawn manuscript).
- `review/skeptic-review-console.html` — #14 v2's identification conjecture, verbatim.
- `review/v3-worklog.md` 'Findings neither referee raised' (F2) — S no longer fixes α_d.
