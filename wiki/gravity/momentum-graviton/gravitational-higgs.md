---
title: "The gravitational Higgs mechanism"
weight: 50
status: alive
description: "The polarization choice spontaneously breaks the dual diffeomorphisms; X eats the would-be Goldstones and becomes a massive spin-2 with five polarizations, its mass the polarization-breaking scale."
provenance: [D]
sources:
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §4"
  - "notes/debt1a-iii-tuning-test.md §1"
  - "notes/debt1a-iii-tuning-test.md §2"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/broken-born-checkpoint-v2.md ref [9]"
  - "papers/broken-born-checkpoint-v2.md ref [10]"
  - "papers/broken-born-checkpoint-v2.md ref [11]"
  - "notes/debt1a-geometric-core.md §C"
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
---

*The gravitational Higgs mechanism is how the [momentum graviton X](/wiki/gravity/momentum-graviton) acquires its mass in this program. The vacuum value of the [modular field](/wiki/phase-space/modular-field/modular-field-z), ⟨Z⟩ = i·g, sits at X = 0, and the local shifts of X, the [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms), move it away from there. So when the vacuum selects a [polarization](/wiki/phase-space/reciprocity/lagrangian-polarizations), a split of phase space into position and momentum, those gauge symmetries are broken spontaneously. In the ordinary [Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs), a gauge field absorbs the would-be massless modes of a broken symmetry and becomes massive; here X absorbs the would-be Goldstone modes of the broken dual diffeomorphisms and becomes a massive spin-2 field with five polarizations. Its mass M_X is the scale of the polarization breaking, and no document gives it a value. The mechanism is a structural derivation [D — structural]; whether the mass term it produces is free of [ghosts](/wiki/gravity/spin-2-fields/ghosts) was a separate question, [the tuning test](/wiki/gravity/tuning-test).*

**Status:** Alive — [D — structural] in [calc note #6](/wiki/history/documents/debt-1-notes) (`notes/debt1a-ii-X-classification.md` §3); step (iii) of [checkpoint #11](/wiki/history/documents/checkpoint) §7.1's chain, tagged [D + T] — not machine-checked; M_X has no value in any source. Whether the mass term is ghost-free is the tuning test, a conditional pass.

## The statement

Calc note #6 ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)), in its section "The mass mechanism and the endpoint [D — structural]":

> The mass cannot be written by hand (shift symmetry) — but it doesn't need to be. The vacuum ⟨Z⟩ = i·g sits at X = 0 and is *moved* by the shifts: the polarization selection (η-emergence) **spontaneously breaks the local dual diffeomorphisms**. Gravitational Higgs mechanism: the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a **massive spin-2** with its five polarizations, mass M_X = the polarization-breaking scale.

The checkpoint, step (iii) of its chain (#11 §7.1): "The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale. The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†]." dRGT is de Rham–Gabadadze–Tolley, and the † marks citations from model memory, not yet checked against the source.

## Background: the Higgs mechanism [T]

### Broken symmetries and Goldstone modes

When the lowest-energy state of a system does not share a continuous symmetry of its laws, the symmetry is spontaneously broken, and the vacuum is one of a family of equally good states related by the symmetry. Moving along that family costs no energy, so for a global symmetry each broken direction carries a massless excitation, a Goldstone mode [T] ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)).

### Broken gauge symmetries

If the broken symmetry is a gauge symmetry, a redundancy of the description rather than a map between distinct states, the would-be Goldstone modes are not physical particles. They become the extra polarization states that a massive gauge field needs, and the gauge field becomes massive, with a mass set by the scale of the breaking [T]. The W and Z bosons of the electroweak theory are the standard example. Written with the would-be Goldstone modes kept as explicit fields, called [Stückelberg fields](/wiki/symmetry-breaking/stuckelberg-fields), the massive theory keeps a gauge symmetry, and fixing the gauge removes them again [T] ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)).

### The gravitational version

The same structure holds for a spin-2 field. A massless spin-2 field has the gauge symmetry of linearized coordinate changes, δh_μν = ∂₍μξ_ν₎ ([general relativity and the graviton](/wiki/gravity/spin-2-fields/general-relativity)). A mass term breaks that symmetry. In the standard Stückelberg treatment of massive gravity the symmetry is restored by writing h_μν + ∂₍μA_ν₎ in place of h_μν, with a new vector field A_μ that shifts under the gauge transformation, and the vector in turn carries a scalar, its longitudinal part ∂_μφ [T] (Arkani-Hamed, Georgi and Schwartz 2003 †; Hinterbichler 2012 †). These fields play the part of the would-be Goldstone modes, and a massive spin-2 field carries five polarizations [T], the number #6 gives for X. The Stückelberg language is the documents' too: #11 calls the absorbed modes "the Stückelberg sector" (§7.5).

## How the program gets there

The argument as calc note #6 §3 gives it, step by step.

### Step 1: no mass term by hand

[Shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry): constant shifts X → X + B are exact symmetries of any geometric action built from the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω and the metric H, so that action contains no term in X without derivatives, including a mass term. "The mass cannot be written by hand (shift symmetry) — but it doesn't need to be."

### Step 2: the vacuum sits at X = 0

"The vacuum ⟨Z⟩ = i·g sits at X = 0". On that slice the phase-space metric is diag(g, g⁻¹), the form that is also compatible with the [neutral metric η](/wiki/phase-space/born-geometry/born-structures) the vacuum has selected (#5 §C; [the modular field](/wiki/phase-space/modular-field/modular-field-z)). Under the corrected postulate [P2′](/wiki/program/postulates/p2-prime), η is not fixed in advance: "η is emergent — the order parameter, η = HJ, with the real structure J chosen spontaneously" [P] (#11 §4), and the choice is postulate [P5](/wiki/program/postulates/p5-spontaneous-selection), "The vacuum selects a polarization".

### Step 3: the shifts move the vacuum

"…and is *moved* by the shifts". A dual diffeomorphism changes X by ∂₍μλ_ν₎ and so carries the configuration off the slice X = 0, away from compatibility with the selected η. The vacuum is therefore not invariant under the dual diffeomorphisms: "the polarization selection (η-emergence) **spontaneously breaks the local dual diffeomorphisms**". In the tuning test the energy cost of moving away from compatibility comes from a misalignment potential: "The X mass must come from the η-selection (Higgs) sector: a misalignment potential penalizing incompatibility between the polarization J and the modular field Z" (#7 §1; [the misalignment potential](/wiki/gravity/tuning-test/misalignment-potential)). Calc note #7 found "The compatible locus is X = 0 *and* Y = Y⁻¹", the metric pinned to a reference set by the polarization, so that "the Higgs sector is inevitably a *two-tensor* potential V(g, X; reference) — a massive-gravity-type potential, confirming the structural landing point of Chunk A-ii from the opposite direction" (§2). Chunk A-ii is calc note #6.

Flag 3 in `review/wiki-build-flags.md` finds the zero set of #7's first invariant, built from the anticommutator {J₀, I[Z]}, larger than #7 states. It is the set on which X and Y commute and X² + Y² = 1, which contains points with X ≠ 0, and an executed check finds the anticommutator zero to rounding at such a point (`review/wiki-build-checks/zero_locus.out`). The flag adds that at quadratic order x is a flat direction, consistent with battery test T4: the quadratic mass that the class Tr({J, I}²) gives is a mass for the metric fluctuation h (#7 §2). The quadratic mass for X that #7 reports comes from its second invariant, built from [J, I] + 2K ([the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures#a-second-invariant-the-same-defect)). The flag awaits Paul's ruling on whether the degeneracy is intended and whether it affects the claims about the vacuum.

### Step 4: the would-be Goldstone modes are absorbed

Because the broken symmetry is a gauge symmetry, the would-be Goldstone modes are absorbed rather than left as massless particles: "the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a **massive spin-2** with its five polarizations". The gauge parameter λ_μ has four components in four dimensions, and #6 counts four would-be Goldstones π_μ. Calc note #8 words the absorbed modes differently (below).

### Step 5: the mass scale

"…mass M_X = the polarization-breaking scale." As in the ordinary mechanism, the mass of the field that absorbs the modes is set by the scale at which the symmetry breaks [T]. No document gives a value for that scale. Once [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)'s [palindrome](/wiki/gravity/palindromic-branch/palindrome) and a flat aligned vacuum have fixed three of the potential's five coefficients, M_X is one of the two free parameters left (#8 §3). Calc note #8 §3 writes the Fierz–Pauli mass combination as "m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), i.e. **M_X**", and #11 §7.5 writes "M_X ∝ 2(β₁+β₂)" (flag 5 in `review/wiki-build-flags.md` suspects that #11 means M_X², a question of notation only; [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)). The βₙ are the coefficients of the [Hassan–Rosen potential](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric).

## Which massive spin-2: the consistency condition

A massive spin-2 field coupled to gravity is consistent only with a special mass term. #6 §3: "Massive spin-2 coupled to gravity has exactly one known consistent structure: the Fierz–Pauli tuning at quadratic order completed by a dRGT/Hassan–Rosen-class potential [T: HR 2011]", HR being Hassan–Rosen. #11 §7.1 words it without "known": "The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen" (see flag 7 in `review/wiki-build-flags.md`; [the Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli); [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity)).

The Higgs mechanism fixes that X is massive, not which mass term it gets. #6 therefore lands on a condition:

> **X is a massive spin-2 field. The geometric sector is healthy iff the potential generated by the η-selection lands in the Hassan–Rosen class; a generic potential reintroduces the Boulware–Deser ghost.**

It restates the result: "BBT's geometric sector is bimetric gravity with the second metric's kinetic structure and couplings dictated by modular (Siegel-domain) symmetry rather than chosen by hand — *if* the dRGT tuning emerges from the symmetry" (BBT, the Broken-Born program). The tuning test examined the condition: misalignment potentials built from the metric fail it, and potentials built from frames pass it, "a conditional pass with the condition being the formulation the geometry already prefers" (#7 §3; [the verdict: a conditional pass](/wiki/gravity/tuning-test/conditional-pass)). The passing class was selected, not derived from the geometric action, which is open item 1 of #11 §14 ([Open: deriving the wedge sector from S_H (OP1)](/wiki/gravity/tuning-test/wedge-reduction)).

## What X absorbs: two unreconciled wordings

The documents describe the absorbed modes in two ways.

- Calc note #6 §3: "the four would-be Goldstones π_μ of the broken λ-gauge are eaten". #11 §7.1 follows it ("X eats the four Goldstones"), as do the [lab notebook](/wiki/history/documents/lab-notebook)'s v0.4 addendum and #9 §5.
- Calc note #8 §3: "the Higgsing of the dual diffeomorphisms eats the vector π_μ and the *longitudinal scalar of the λ-gradient sector*".

No document reconciles the two wordings or relates them to the standard Stückelberg decomposition described above ([conflicts between sources](/wiki/history/documents/source-conflicts)). Both exclude the [dark-energy field τ](/wiki/cosmology/dark-energy/tau-quintessence): #6 says "The Λ(d) moduli, τ included, are not the eaten modes", and #8 that τ "survives as the light field" ([τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten)).

## What follows

- **τ stays light.** "τ is a J-modulus on the compact Λ(d), a different sector with different origin; it survives as the light field" (#8 §3, [D — leading order]). How much τ still mixes with the absorbed modes through the potential is open item 6 ([Open: τ–Stückelberg mixing (OP6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing)).
- **The spin-2 spectrum.** One exactly massless graviton, even under reciprocity, and the massive X, odd under it (#8 §3; #11 §7.5; [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity); on the parities under #11 §6's Z → −Z⁻¹, see flag 39 in `review/wiki-build-flags.md`).
- **A short range.** A massive field mediates a force [cut off](/wiki/gravity/spin-2-fields/yukawa-forces#the-range) beyond a distance of order 1/M_X [T]. #11 §7.5: "SM couplings gravitational-strength and Yukawa-cut at 1/M_X", SM being the Standard Model ([safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)).
- **The dark-matter gate.** "Integrating out massive X between χ bilinears gives the contact four-χ operator" (#6 §4), the program's mechanism for the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) of [conjugate matter](/wiki/dark-matter/conjugate-matter) ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)).
- **A dark-matter candidate.** #11 §12 lists the stability of [the X-condensate candidate](/wiki/dark-matter/candidates/x-condensate), an oscillating massive X, as "m_X-protected".
- **Born's answer.** "a reciprocity-odd massive spin-2, its mass born of the polarization choice" (#11 §7; [Born's answer](/wiki/gravity/momentum-graviton/borns-answer)).

## Scope and caveats

- **Structural.** The mechanism is argued from the symmetry: no document writes a Lagrangian for X with the would-be Goldstone modes as explicit fields, and the number of absorbed modes is stated, not derived from an action. Calc note #6's own summary lists it as "the mass mechanism identified (Higgsed dual diffs), the eaten modes counted" (§5).
- **Not machine-checked.** The battery tests behind #11 §7.2's [V], T3, T4 and T7, check the misalignment potential's blocks and its two metric-tier failures ([the verification battery](/wiki/method/verification/battery)); no test checks the Higgs mechanism itself.
- **No value for M_X.** The sources fix no number for the mass or for the breaking scale.
- **Positive metrics.** The mechanism is §3 of the chain that #6 calls "the Euclidean-rigorous skeleton" (§3); the extension to the Lorentzian signature of spacetime is open item 3 ([Open: Lorentzian dressing of the Euclidean skeleton (OP3)](/wiki/phase-space/born-geometry/lorentzian-dressing)).
- **The withdrawn manuscript's own wording.** [#14](/wiki/dark-matter/candidates/soliton-candidate) §1 states the limits: "That the symmetry-breaking sector lands on the ghost-free potential is argued from a first-order (vielbein) formulation and is a structural claim, not a line-by-line derivation. Cosmological stability is a further, open check." Its §6 lists "the ghost-free landing of the mass mechanism and its cosmological stability at equal Planck masses" as conjectural. The stability question is [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability), which #11 §14 does not list.
- **Literature citations.** [9†], [10†] and [11†] are memory citations, due a source check in [the literature battery](/wiki/method/literature-battery).

## The name

The label "gravitational Higgs" is used in calc note #6 §3, in the v1 paper ("X eats the four Goldstones (gravitational Higgs)", #9 §5 item 3) and in the withdrawn soliton manuscript ("X absorbs the Goldstones and acquires mass M_X (gravitational Higgs)", #14 §1; [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate)). #11 §7.1 describes the mechanism without the label. Other documents speak of "Higgsed dual diffeomorphisms" (`HANDOFF.md` §2) and "the Higgsing of dual diffeomorphisms when the vacuum selects a polarization" (#8 §4). The [popular articles](/wiki/history/documents/popular-articles) state the comparison in everyday terms: "the way particles gain mass from the Higgs" (#10, 'What refused to die') and "The resolution operates like the Higgs mechanism" (#12, 'The second geometry, and why it has never been seen').

## History

- **Before.** Calc note #5 left open what X is and had no mass mechanism; it posed the healthy, auxiliary or ghost question ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain#superseded-the-three-way-classification-of-x)).
- **Found.** Calc note #6 §3, after the no-go of §2 required a mass. The lab notebook's v0.4 addendum: "The only exit: the polarization selection (η-emergence) spontaneously breaks the dual diffeomorphisms, X eats the four Goldstones and becomes a **massive spin-2** with M_X = the polarization-breaking scale" ([the lab notebook](/wiki/history/documents/lab-notebook)).
- **Its potential.** Calc note #7 identified the Higgs sector with the misalignment potential and ran the tuning test; calc note #8 constrained the potential's coefficients by reciprocity and a flat aligned vacuum, leaving M_X as one of two free parameters. The v0.6 addendum's summary: "its mass from the Higgsing of dual diffeomorphisms by the polarization choice".
- **The papers.** #9 §5 item 3, headed "The mass [D]", with "The unique consistent home for a massive spin-2 coupled to gravity is the Fierz–Pauli/dRGT/Hassan–Rosen structure [T]" (see flag 7 in `review/wiki-build-flags.md`). #11 §7.1 (iii) is the current statement, inside a chain tagged [D + T].

## References

As #11 cites them, all from model memory (†):

- [9]† C. de Rham, G. Gabadadze, A. J. Tolley, "Resummation of massive gravity," Phys. Rev. Lett. 106, 231101 (2011), arXiv:1011.1232.
- [10]† S. F. Hassan, R. A. Rosen, "Resolving the ghost problem in non-linear massive gravity," Phys. Rev. Lett. 108, 041101 (2012), arXiv:1106.3344.
- [11]† S. F. Hassan, R. A. Rosen, "Bimetric gravity from ghost-free massive gravity," JHEP 1202, 126 (2012), arXiv:1109.3515.

Added here for the Stückelberg background, also from memory (†), and cited by no project document:

- N. Arkani-Hamed, H. Georgi, M. D. Schwartz, "Effective field theory for massive gravitons and gravity in theory space," Annals of Physics 305, 96 (2003), hep-th/0210184 †.
- K. Hinterbichler, "Theoretical aspects of massive gravity," Rev. Mod. Phys. 84, 671 (2012), arXiv:1105.3735 †.

## Sources

- `notes/debt1a-ii-X-classification.md` §3 — the mechanism [D — structural], the classification and the Euclidean-rigorous skeleton; §1 — the shift symmetry; §2 — the no-go that requires a mass; §4 — the gate from integrating out massive X; §5 — "the eaten modes counted".
- `notes/debt1a-iv-beta-coefficients.md` §3 — the second wording of the absorbed modes; M_X as the Fierz–Pauli mass combination; §4 — "the Higgsing of dual diffeomorphisms".
- `notes/debt1a-iii-tuning-test.md` §1, §2, §3 — the Higgs sector as the misalignment potential, its compatible locus, the verdict.
- `papers/broken-born-checkpoint-v2.md` §7.1 — the current statement, step (iii); §7.5 — M_X ∝ 2(β₁+β₂), the Stückelberg sector, the Yukawa range; §7 — Born's answer; §4 — P2′ and P5; §12 — the X-condensate; §14 — open items 1, 3 and 6; refs [9]–[11].
- `notes/debt1a-geometric-core.md` §C — the vacuum slice X = 0.
- `notes/broken-born-theory.md` 'Addendum (v0.4)', 'Addendum (v0.6)' — the lab notebook's record.
- `notes/broken-born-program-v1.md` §5 — the v1 statement, "(gravitational Higgs)".
- `notes/knot-dark-matter-standalone.md` §1, §6 — the withdrawn manuscript's summary and its list of conjectural claims.
- `HANDOFF.md` §2 — "Higgsed dual diffeomorphisms".
- `popsci/angle-of-the-mirror.md` 'What refused to die' and `popsci/universes-other-half.md` 'The second geometry, and why it has never been seen' — the popular articles' comparison with the Higgs mechanism.
- `review/wiki-build-flags.md` item 3 — the larger zero set of #7's first invariant and the flat direction of x at quadratic order; item 5 — M_X versus M_X²; item 7 — the qualifier "known" that #11 §7.1 and #9 §5 drop. All await Paul's ruling.
- `review/wiki-build-checks/zero_locus.py` and `review/wiki-build-checks/zero_locus.out` — the anticommutator {J₀, I[Z]} evaluated at a point with X ≠ 0.
