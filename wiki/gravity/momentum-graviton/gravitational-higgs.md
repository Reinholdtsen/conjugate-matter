---
title: "The gravitational Higgs mechanism"
weight: 50
status: alive
description: "The polarization choice spontaneously breaks the dual diffeomorphisms; X eats the would-be Goldstones and becomes a massive spin-2 with five polarizations, its mass the polarization-breaking scale."
provenance: [D]
sources:
  - "notes/x-classification.md §3"
  - "notes/x-classification.md §1"
  - "notes/x-classification.md §2"
  - "notes/x-classification.md §4"
  - "notes/x-classification.md §5"
  - "notes/beta-coefficients.md §3"
  - "notes/beta-coefficients.md §4"
  - "notes/tuning-test.md §1"
  - "notes/tuning-test.md §2"
  - "notes/tuning-test.md §3"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.5"
  - "wiki/papers/broken-born-checkpoint-v2.md §7"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §14"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [9]"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [10]"
  - "wiki/papers/broken-born-checkpoint-v2.md ref [11]"
  - "notes/geometric-core.md §C"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §6"
  - "HANDOFF.md §2"
  - "popsci/angle-of-the-mirror.md 'What refused to die'"
  - "popsci/universes-other-half.md 'The second geometry, and why it has never been seen'"
  - "review/wiki-build-flags.md items 3, 5, 7"
  - "review/wiki-build-checks/zero_locus.out"
  - "wiki/papers/phase-space-diameter.md §8.2"
  - "wiki/papers/phase-space-diameter.md §9"
  - "verify/phase_space_diameter.py 'Consequences (note §8)'"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
---

*The gravitational Higgs mechanism is how the [momentum graviton X](_index.md) acquires its mass in this program. The vacuum value of the [modular field](../../phase-space/modular-field/modular-field-z.md), ⟨Z⟩ = i·g, sits at X = 0, and the local shifts of X, the [dual diffeomorphisms](dual-diffeomorphisms.md), move it away from there. So when the vacuum selects a [polarization](../../phase-space/reciprocity/lagrangian-polarizations.md), a split of phase space into position and momentum, those gauge symmetries are broken spontaneously. In the ordinary [Higgs mechanism](../../symmetry-breaking/goldstone-and-higgs.md), a gauge field absorbs the would-be massless modes of a broken symmetry and becomes massive; here X absorbs the would-be Goldstone modes of the broken dual diffeomorphisms and becomes a massive spin-2 field with five polarizations. Its mass M_X is the scale of the polarization breaking, and no document gives it a value. The mechanism is a structural derivation [D — structural]; whether the mass term it produces is free of [ghosts](../spin-2-fields/ghosts.md) was a separate question, [the tuning test](../tuning-test/_index.md).*

**Status:** Alive — [D — structural] in [calc note #6](../../history/documents/field-equation-notes.md) ([`notes/x-classification.md` §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)); step (iii) of [checkpoint #11](../../history/documents/checkpoint.md) [§7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t)'s chain, tagged [D + T] — not machine-checked; M_X has no value in any source. Whether the mass term is ghost-free is the tuning test, a conditional pass.

## The statement

Calc note [#6](../../../notes/x-classification.md) ([the field-equation calc notes](../../history/documents/field-equation-notes.md)), in its section "The mass mechanism and the endpoint [D — structural]":

> The mass cannot be written by hand (shift symmetry) — but it doesn't need to be. The vacuum ⟨Z⟩ = i·g sits at X = 0 and is *moved* by the shifts: the polarization selection (η-emergence) **spontaneously breaks the local dual diffeomorphisms**. Gravitational Higgs mechanism: the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a **massive spin-2** with its five polarizations, mass M_X = the polarization-breaking scale.

The checkpoint, step (iii) of its chain ([#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t)): "The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale. The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†]." dRGT is de Rham–Gabadadze–Tolley, and the † marks citations from model memory, not yet checked against the source.

## Background: the Higgs mechanism [T]

### Broken symmetries and Goldstone modes

When the lowest-energy state of a system does not share a continuous symmetry of its laws, the symmetry is spontaneously broken, and the vacuum is one of a family of equally good states related by the symmetry. Moving along that family costs no energy, so for a global symmetry each broken direction carries a massless excitation, a Goldstone mode [T] ([spontaneous symmetry breaking](../../symmetry-breaking/spontaneous-symmetry-breaking.md)).

### Broken gauge symmetries

If the broken symmetry is a gauge symmetry, a redundancy of the description rather than a map between distinct states, the would-be Goldstone modes are not physical particles. They become the extra polarization states that a massive gauge field needs, and the gauge field becomes massive, with a mass set by the scale of the breaking [T]. The W and Z bosons of the electroweak theory are the standard example. Written with the would-be Goldstone modes kept as explicit fields, called [Stückelberg fields](../../symmetry-breaking/stuckelberg-fields.md), the massive theory keeps a gauge symmetry, and fixing the gauge removes them again [T] ([Goldstone modes and the Higgs mechanism](../../symmetry-breaking/goldstone-and-higgs.md)).

### The gravitational version

The same structure holds for a spin-2 field. A massless spin-2 field has the gauge symmetry of linearized coordinate changes, δh_μν = ∂₍μξ_ν₎ ([general relativity and the graviton](../spin-2-fields/general-relativity.md)). A mass term breaks that symmetry. In the standard Stückelberg treatment of massive gravity the symmetry is restored by writing h_μν + ∂₍μA_ν₎ in place of h_μν, with a new vector field A_μ that shifts under the gauge transformation, and the vector in turn carries a scalar, its longitudinal part ∂_μφ [T] (Arkani-Hamed, Georgi and Schwartz 2003 †; Hinterbichler 2012 †). These fields play the part of the would-be Goldstone modes, and a massive spin-2 field carries five polarizations [T], the number #6 gives for X. The Stückelberg language is the documents' too: #11 calls the absorbed modes "the Stückelberg sector" ([§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d)).

## How the program gets there

The argument as calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) gives it, step by step.

### Step 1: no mass term by hand

[Shift symmetry](shift-symmetry.md): constant shifts X → X + B are exact symmetries of any geometric action built from the [symplectic form](../../phase-space/reciprocity/symplectic-form.md) ω and the metric H, so that action contains no term in X without derivatives, including a mass term. "The mass cannot be written by hand (shift symmetry) — but it doesn't need to be."

### Step 2: the vacuum sits at X = 0

"The vacuum ⟨Z⟩ = i·g sits at X = 0". On that slice the phase-space metric is diag(g, g⁻¹), the form that is also compatible with the [neutral metric η](../../phase-space/born-geometry/born-structures.md) the vacuum has selected ([#5 §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard); [the modular field](../../phase-space/modular-field/modular-field-z.md)). Under the corrected postulate [P2′](../../program/postulates/p2-prime.md), η is not fixed in advance: "η is emergent — the order parameter, η = HJ, with the real structure J chosen spontaneously" [P] ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)), and the choice is postulate [P5](../../program/postulates/p5-spontaneous-selection.md), "The vacuum selects a polarization".

### Step 3: the shifts move the vacuum

"…and is *moved* by the shifts". A dual diffeomorphism changes X by ∂₍μλ_ν₎ and so carries the configuration off the slice X = 0, away from compatibility with the selected η. The vacuum is therefore not invariant under the dual diffeomorphisms: "the polarization selection (η-emergence) **spontaneously breaks the local dual diffeomorphisms**". In the tuning test the energy cost of moving away from compatibility comes from a misalignment potential: "The X mass must come from the η-selection (Higgs) sector: a misalignment potential penalizing incompatibility between the polarization J and the modular field Z" ([#7 §1](../../../notes/tuning-test.md#1-the-object-to-test); [the misalignment potential](../tuning-test/misalignment-potential.md)). Calc note #7 found "The compatible locus is X = 0 *and* Y = Y⁻¹", the metric pinned to a reference set by the polarization, so that "the Higgs sector is inevitably a *two-tensor* potential V(g, X; reference) — a massive-gravity-type potential, confirming the structural landing point of Chunk A-ii from the opposite direction" ([§2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous)). Chunk A-ii is calc note #6.

Flag 3 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) finds the zero set of #7's first invariant, built from the anticommutator {J₀, I[Z]}, larger than #7 states. It is the set on which X and Y commute and X² + Y² = 1, which contains points with X ≠ 0, and an executed check finds the anticommutator zero to rounding at such a point ([`review/wiki-build-checks/zero_locus.out`](../../../review/wiki-build-checks/zero_locus.out)). The flag adds that at quadratic order x is a flat direction, consistent with battery test T4: the quadratic mass that the class Tr({J, I}²) gives is a mass for the metric fluctuation h ([#7 §2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous)). The quadratic mass for X that #7 reports comes from its second invariant, built from [J, I] + 2K ([the metric tier fails twice](../tuning-test/metric-tier-failures.md#a-second-invariant-the-same-defect)). The flag is pending; it asks whether the degeneracy is intended and whether it affects the claims about the vacuum.

### Step 4: the would-be Goldstone modes are absorbed

Because the broken symmetry is a gauge symmetry, the would-be Goldstone modes are absorbed rather than left as massless particles: "the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a **massive spin-2** with its five polarizations". The gauge parameter λ_μ has four components in four dimensions, and #6 counts four would-be Goldstones π_μ. Calc note [#8](../../../notes/beta-coefficients.md) words the absorbed modes differently (below).

### Step 5: the mass scale

"…mass M_X = the polarization-breaking scale." As in the ordinary mechanism, the mass of the field that absorbs the modes is set by the scale at which the symmetry breaks [T]. No document gives a value for that scale. Once [reciprocity](../../phase-space/reciprocity/born-reciprocity.md)'s [palindrome](../palindromic-branch/palindrome.md) and a flat aligned vacuum have fixed three of the potential's five coefficients, M_X is one of the two free parameters left ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)). Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) writes the Fierz–Pauli mass combination as "m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**", and [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) writes "M_X ∝ 2(β₁+β₂)" (flag 5 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) suspects that #11 means M_X², a question of notation only; [spectrum, parameters and reciprocity parity](spectrum-and-parity.md)). The βₙ are the coefficients of the [Hassan–Rosen potential](../spin-2-fields/hassan-rosen-bimetric.md).

## Which massive spin-2: the consistency condition

A massive spin-2 field coupled to gravity is consistent only with a special mass term. [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural): "Massive spin-2 coupled to gravity has exactly one known consistent structure: the Fierz–Pauli tuning at quadratic order completed by a dRGT/Hassan–Rosen-class potential [T: HR 2011]", HR being Hassan–Rosen. [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) words it without "known": "The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen" (see flag 7 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [the Fierz–Pauli mass term and the Boulware–Deser ghost](../spin-2-fields/fierz-pauli.md); [dRGT massive gravity](../spin-2-fields/drgt-massive-gravity.md)).

The Higgs mechanism fixes that X is massive, not which mass term it gets. #6 therefore lands on a condition:

> **X is a massive spin-2 field. The geometric sector is healthy iff the potential generated by the η-selection lands in the Hassan–Rosen class; a generic potential reintroduces the Boulware–Deser ghost.**

It restates the result: "BBT's geometric sector is bimetric gravity with the second metric's kinetic structure and couplings dictated by modular (Siegel-domain) symmetry rather than chosen by hand — *if* the dRGT tuning emerges from the symmetry" (BBT, Broken-Born theory, the program's earlier name). The tuning test examined the condition: misalignment potentials built from the metric fail it, and potentials built from frames pass it, "a conditional pass with the condition being the formulation the geometry already prefers" ([#7 §3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t); [the verdict: a conditional pass](../tuning-test/conditional-pass.md)). The passing class was selected, not derived from the geometric action, which is open item 1 of [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) ([Open: deriving the wedge sector from S_H (OP1)](../tuning-test/wedge-reduction.md)).

## What X absorbs: two unreconciled wordings

The documents describe the absorbed modes in two ways.

- Calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural): "the four would-be Goldstones π_μ of the broken λ-gauge are eaten". [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) follows it ("X eats the four Goldstones"), as do the [lab notebook](../../history/documents/lab-notebook.md)'s v0.4 addendum and [#9 §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved).
- Calc note [#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t): "the Higgsing of the dual diffeomorphisms eats the vector π_μ and the *longitudinal scalar of the λ-gradient sector*".

No document reconciles the two wordings or relates them to the standard Stückelberg decomposition described above ([conflicts between sources](../../history/documents/source-conflicts.md)). Both exclude the [dark-energy field τ](../../cosmology/dark-energy/tau-quintessence.md): #6 says "The Λ(d) moduli, τ included, are not the eaten modes", and #8 that τ "survives as the light field" ([τ is not eaten](tau-not-eaten.md)).

## What follows

- **τ stays light.** "τ is a J-modulus on the compact Λ(d), a different sector with different origin; it survives as the light field" ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t), [D — leading order]). How much τ still mixes with the absorbed modes through the potential is open item 6 ([Open: τ–Stückelberg mixing (OP6)](tau-stuckelberg-mixing.md)).
- **The spin-2 spectrum.** One exactly massless graviton, even under reciprocity, and the massive X, odd under it ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t); [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d); [spectrum, parameters and reciprocity parity](spectrum-and-parity.md); on the parities under [#11 §6](../../papers/broken-born-checkpoint-v2.md#6-the-modular-field)'s Z → −Z⁻¹, see flag 39 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).
- **A short range.** A massive field mediates a force [cut off](../spin-2-fields/yukawa-forces.md#the-range) beyond a distance of order 1/M_X [T]. [#11 §7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d): "SM couplings gravitational-strength and Yukawa-cut at 1/M_X", SM being the Standard Model ([safety by range](fifth-force-safety.md)).
- **The dark-matter gate.** "Integrating out massive X between χ bilinears gives the contact four-χ operator" ([#6 §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)), the program's mechanism for the [velocity gate](../../dark-matter/conjugate-matter/velocity-gate.md) of [conjugate matter](../../dark-matter/conjugate-matter/_index.md) ([the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md)) (not derived, according to flag 55 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), pending; [the gate mechanism](../../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). [`notes/gate-mechanism.md`](../../../notes/gate-mechanism.md) (2026-10-28, not reviewed) finds that exchanging the massive X that this mechanism produces gives a velocity dependence with the speed of light as its scale, not a gate ([§2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate)).
- **A dark-matter candidate.** [#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) lists the stability of [the X-condensate candidate](../../dark-matter/candidates/x-condensate.md), an oscillating massive X, as "m_X-protected".
- **Born's answer.** "a reciprocity-odd massive spin-2, its mass born of the polarization choice" ([#11 §7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton); [Born's answer](borns-answer.md)).

## Scope and caveats

- **Structural.** The mechanism is argued from the symmetry: no document writes a Lagrangian for X with the would-be Goldstone modes as explicit fields, and the number of absorbed modes is stated, not derived from an action. Calc note #6's own summary lists it as "the mass mechanism identified (Higgsed dual diffs), the eaten modes counted" ([§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk)).
- **Not machine-checked.** The battery tests behind [#11 §7.2](../../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv)'s [V], T3, T4 and T7, check the misalignment potential's blocks and its two metric-tier failures ([the verification battery](../../method/verification/battery.md)); no test checks the Higgs mechanism itself.
- **No value for M_X.** The sources fix no value for the mass or for the breaking scale. The one number in the record is a lower bound, conditional on the program's aligned vacuum, in which the ratio of the two frames' backgrounds is u = 1. There, with the equal Planck masses that reciprocity forces ([#8 §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)), X's force on ordinary matter has Yukawa strength α = 4/3, and torsion balances require λ_X < 37.7 μm, M_X c² > 5.2 meV, with λ_X = ħ/(M_X c) the force's range; "The polarization-breaking scale lies at least 2.3 times above the dark-energy scale of 2.24 meV" ([phase-space-diameter note](../../cosmology/scale-factor-duality/phase-space-diameter.md) [§8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs); the bound tagged [V][S] in its summary, [§9](../../papers/phase-space-diameter.md#9-summary); [the laboratory bound on X's range](range-bound.md)). Whether the aligned vacuum persists as the universe expands is open [O].
- **Positive metrics.** The mechanism is §3 of the chain that #6 calls "the Euclidean-rigorous skeleton" ([§3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)); the extension to the Lorentzian signature of spacetime is open item 3 ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](../../phase-space/born-geometry/lorentzian-dressing.md)).
- **The withdrawn manuscript's own wording.** [#14](../../dark-matter/candidates/soliton-candidate/_index.md) [§1](../../../notes/knot-dark-matter-standalone.md#1-framework) states the limits: "That the symmetry-breaking sector lands on the ghost-free potential is argued from a first-order (vielbein) formulation and is a structural claim, not a line-by-line derivation. Cosmological stability is a further, open check." Its §6 lists "the ghost-free landing of the mass mechanism and its cosmological stability at equal Planck masses" as conjectural. The stability question is [Open: stability at equal Planck masses](equal-planck-mass-stability.md), which [#11 §14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) does not list.
- **Literature citations.** [9†], [10†] and [11†] are memory citations, due a source check in [the literature battery](../../method/literature-battery.md).

## The name

The label "gravitational Higgs" is used in calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural), in the v1 paper ("X eats the four Goldstones (gravitational Higgs)", [#9 §5 item 3](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved)) and in the withdrawn soliton manuscript ("X absorbs the Goldstones and acquires mass M_X (gravitational Higgs)", [#14 §1](../../../notes/knot-dark-matter-standalone.md#1-framework); [#14's soliton model](../../dark-matter/candidates/soliton-candidate/_index.md)). [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) describes the mechanism without the label. Other documents speak of "Higgsed dual diffeomorphisms" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen)) and "the Higgsing of dual diffeomorphisms when the vacuum selects a polarization" ([#8 §4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born)). The [popular articles](../../history/documents/popular-articles.md) state the comparison in everyday terms: "the way particles gain mass from the Higgs" ([#10](../../../popsci/angle-of-the-mirror.md), 'What refused to die') and "The resolution operates like the Higgs mechanism" ([#12](../../../popsci/universes-other-half.md), 'The second geometry, and why it has never been seen').

## History

- **Before.** Calc note #5 left open what X is and had no mass mechanism; it posed the healthy, auxiliary or ghost question ([why X must be massive](forcing-chain.md#superseded-the-three-way-classification-of-x)).
- **Found.** Calc note [#6 §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural), after the no-go of [§2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t) required a mass. The lab notebook's v0.4 addendum: "The only exit: the polarization selection (η-emergence) spontaneously breaks the dual diffeomorphisms, X eats the four Goldstones and becomes a **massive spin-2** with M_X = the polarization-breaking scale" ([the lab notebook](../../history/documents/lab-notebook.md)).
- **Its potential.** Calc note #7 identified the Higgs sector with the misalignment potential and ran the tuning test; calc note #8 constrained the potential's coefficients by reciprocity and a flat aligned vacuum, leaving M_X as one of two free parameters. The v0.6 addendum's summary: "its mass from the Higgsing of dual diffeomorphisms by the polarization choice".
- **The papers.** [#9 §5 item 3](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved), headed "The mass [D]", with "The unique consistent home for a massive spin-2 coupled to gravity is the Fierz–Pauli/dRGT/Hassan–Rosen structure [T]" (see flag 7 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)). [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) (iii) is the current statement, inside a chain tagged [D + T].

## References

As #11 cites them, all from model memory (†):

- [9]† C. de Rham, G. Gabadadze, A. J. Tolley, "Resummation of massive gravity," Phys. Rev. Lett. 106, 231101 (2011), [arXiv:1011.1232](https://arxiv.org/abs/1011.1232).
- [10]† S. F. Hassan, R. A. Rosen, "Resolving the ghost problem in non-linear massive gravity," Phys. Rev. Lett. 108, 041101 (2012), [arXiv:1106.3344](https://arxiv.org/abs/1106.3344).
- [11]† S. F. Hassan, R. A. Rosen, "Bimetric gravity from ghost-free massive gravity," JHEP 1202, 126 (2012), [arXiv:1109.3515](https://arxiv.org/abs/1109.3515).

Added here for the Stückelberg background, also from memory (†), and cited by no project document:

- N. Arkani-Hamed, H. Georgi, M. D. Schwartz, "Effective field theory for massive gravitons and gravity in theory space," Annals of Physics 305, 96 (2003), [hep-th/0210184](https://arxiv.org/abs/hep-th/0210184) †.
- K. Hinterbichler, "Theoretical aspects of massive gravity," Rev. Mod. Phys. 84, 671 (2012), [arXiv:1105.3735](https://arxiv.org/abs/1105.3735) †.

## Sources

- [`notes/x-classification.md` §3](../../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — the mechanism [D — structural], the classification and the Euclidean-rigorous skeleton; [§1](../../../notes/x-classification.md#1-the-shift-symmetry-d--rigorous) — the shift symmetry; [§2](../../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t) — the no-go that requires a mass; [§4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — the gate from integrating out massive X; [§5](../../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — "the eaten modes counted".
- [`notes/beta-coefficients.md` §3](../../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — the second wording of the absorbed modes; M_X as the Fierz–Pauli mass combination; [§4](../../../notes/beta-coefficients.md#4-the-field-equation-problem-the-answer-to-born) — "the Higgsing of dual diffeomorphisms".
- [`notes/tuning-test.md` §1](../../../notes/tuning-test.md#1-the-object-to-test), [§2](../../../notes/tuning-test.md#2-explicit-computation-metric-tier-d--rigorous), [§3](../../../notes/tuning-test.md#3-the-frame-tier-d--structural-resting-on-t) — the Higgs sector as the misalignment potential, its compatible locus, the verdict.
- [`wiki/papers/broken-born-checkpoint-v2.md` §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — the current statement, step (iii); [§7.5](../../papers/broken-born-checkpoint-v2.md#75-spectrum-d) — M_X ∝ 2(β₁+β₂), the Stückelberg sector, the Yukawa range; [§7](../../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) — Born's answer; [§4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — P2′ and P5; [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) — the X-condensate; [§14](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — open items 1, 3 and 6; refs [9]–[11].
- [`notes/geometric-core.md` §C](../../../notes/geometric-core.md#c-the-modular-field-d--structural-math-facts-standard) — the vacuum slice X = 0.
- [`notes/broken-born-theory.md`](../../../notes/broken-born-theory.md) 'Addendum (v0.4)', 'Addendum (v0.6)' — the lab notebook's record.
- [`notes/broken-born-program-v1.md` §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) — the v1 statement, "(gravitational Higgs)".
- [`notes/knot-dark-matter-standalone.md` §1](../../../notes/knot-dark-matter-standalone.md#1-framework), [§6](../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) — the withdrawn manuscript's summary and its list of conjectural claims.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — "Higgsed dual diffeomorphisms".
- [`popsci/angle-of-the-mirror.md`](../../../popsci/angle-of-the-mirror.md) 'What refused to die' and [`popsci/universes-other-half.md`](../../../popsci/universes-other-half.md) 'The second geometry, and why it has never been seen' — the popular articles' comparison with the Higgs mechanism.
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 3 — the larger zero set of #7's first invariant and the flat direction of x at quadratic order; item 5 — M_X versus M_X²; item 7 — the qualifier "known" that [#11 §7.1](../../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) and [#9 §5](../../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) drop. All pending.
- [`review/wiki-build-checks/zero_locus.py`](../../../review/wiki-build-checks/zero_locus.py) and [`review/wiki-build-checks/zero_locus.out`](../../../review/wiki-build-checks/zero_locus.out) — the anticommutator {J₀, I[Z]} evaluated at a point with X ≠ 0.
- [`wiki/papers/phase-space-diameter.md` §8.2](../../papers/phase-space-diameter.md#82-not-the-range-of-the-momentum-graviton-and-a-bound-on-it-dvs) — the conditional lower bound on M_X and on the polarization-breaking scale, in the aligned vacuum [D][V][S]; [§9](../../papers/phase-space-diameter.md#9-summary) — the bound tagged [V][S].
- [`verify/phase_space_diameter.py`](../../../verify/phase_space_diameter.py) 'Consequences (note §8)' — the bound and the factor 2.3 recomputed [V].
- [`notes/gate-mechanism.md` §2](../../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate) and [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 55 — exchanging the massive X cannot produce the gate (flag 55, pending).
