---
title: "Spontaneous symmetry breaking"
weight: 10
status: established
description: "A symmetric law with an asymmetric ground state: vacuum manifold and stabilizer, order parameter, why breaking needs infinitely many degrees of freedom, and spontaneous versus explicit breaking (spurions); the program's operational version is criteria S1–S3."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §4"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/debt1a-geometric-core.md §F"
  - "review/round4/referee/audit-notes.md 'Step 2(c)'"
  - "verify/toy_coset.py S2–S3"
---

*Spontaneous symmetry breaking is the situation in which the equations of a system are unchanged by some transformation but its lowest-energy state is not. A cooled magnet is the standard example: the laws governing its atoms treat every direction alike, yet the magnet ends up magnetized along one direction, and any other direction would have been an equally good ground state. The symmetry is not lost. It now relates the possible ground states to one another, and the system occupies one of them. The Broken-Born program uses this pattern for its hard core: it proposes that the exchange of position and momentum, an exact symmetry of quantum kinematics, is broken by the vacuum rather than by the laws. This page is the textbook background and the program's operational version of it; the program's own claims follow on the next pages of this section.*

**Status:** Established — [T] — standard field theory, explained here from general knowledge; the program applies it in [#11](/wiki/history/documents/checkpoint) §3 and turns it into the pass/fail criteria S1–S3 of its toy models, checked in `verify/toy_coset.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## The pattern

A symmetry of a physical system is a transformation that leaves its law unchanged. In field theory the law is an action S, a functional of the fields Φ, and a group G of transformations is a symmetry when [T]

```text
S[g·Φ] = S[Φ]          for every g in G
```

The ground state, or vacuum, Φ₀ is the configuration of least energy. If g·Φ₀ = Φ₀ for every g in G, the symmetry is unbroken. If some g moves the vacuum, g·Φ₀ is a different configuration with exactly the same energy, since S cannot tell the two apart. The symmetry is then spontaneously broken [T]: it still holds in the law, it is absent from the state, and what remains of it is a map from ground states to ground states.

In a ferromagnet the energy depends only on the relative orientation of neighbouring spins, so rotating every spin together changes nothing [T]. Below the Curie temperature the spins align, and the magnetization points along some direction. A rotation of the whole sample carries that state to another magnetized state of equal energy, pointing elsewhere. Which direction results is decided by small accidents of the sample's history, such as a stray field while it cooled, not by the laws.

The program's instance is stated in #11 §3: "Quantum kinematics is exactly invariant under ρ: (x,p) → (p,−x); the Fourier transform implements it unitarily [1†, 2†]", and "The program: ρ is exact and spontaneously broken." Here ρ is [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), the quarter-turn of the position–momentum plane that [the Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) carries out on wavefunctions, and the claim is the program's [hard core](/wiki/program/hard-core): the world's preference for position belongs to the vacuum, as a magnet's direction belongs to its state. The postulate that says so is [P5](/wiki/program/postulates/p5-spontaneous-selection): "The vacuum selects a polarization; ours is x-tilted; the mirror vacuum is equally lawful. [P]" (#11 §4).

## The vacuum manifold and the stabilizer

The vacua of a theory with a broken symmetry form a family, the vacuum manifold. The elements of G that leave a chosen vacuum Φ₀ fixed form a subgroup, its stabilizer (also called the unbroken or isotropy subgroup), and when every vacuum lies on the orbit of Φ₀ the vacuum manifold is the coset space G/G₀ [T]:

```text
G₀ = {g in G : g·Φ₀ = Φ₀}          vacuum manifold ≅ G/G₀
```

For a continuous group, each generator outside G₀ moves the vacuum along a direction that costs no energy, so the vacuum manifold has dimension dim G − dim G₀ [T]. Those flat directions carry the massless modes of [Goldstone's theorem](/wiki/symmetry-breaking/goldstone-and-higgs). For the magnet, G is the rotation group, G₀ the rotations about the magnetization axis, and the vacuum manifold the sphere of possible directions [T]. The construction, how the shape of the vacuum manifold decides which defects a transition can leave, and the program's own vacuum manifolds are on [topological defects and the vacuum manifold](/wiki/symmetry-breaking/topological-defects).

### A worked case: model I

The program's coset toy model ([model I](/wiki/symmetry-breaking/toy-models/coset-model)) shows these objects explicitly (toy-model note §2). Its two fields, on a 1+1-dimensional base, are H, a metric on the phase plane given by a point Z of the [upper half-plane](/wiki/phase-space/modular-field/siegel-domain), and K, a real structure with K² = 1 that marks which line of the phase plane counts as position ([the order parameter](/wiki/symmetry-breaking/order-parameter)). The symplectic group Sp(2, ℝ) of area-preserving linear maps of the phase plane ([the symplectic form](/wiki/phase-space/reciprocity/symplectic-form)) acts on both and leaves the action invariant. At H = 1 the vacua are a circle of real structures K(φ), and "The vacuum manifold is the upper half-plane times this circle"; "The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}" (toy-model note §2, whose model-I results are "All checked symbolically"). Every other element of the group moves the vacuum, ρ among them: "ρ acts as Z → −1/Z and K(φ) → K(φ + π) = −K(φ)" (§2). Within the model's full symmetry group, which adds the sign flip K → −K, the vacuum keeps the twisted element ρ∘(K → −K), so the breaking of ρ has physical consequences only once something couples to the sign of K ([the twisted element](/wiki/symmetry-breaking/twisted-element)). The full calculation is on [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua), and the vacuum manifold's topology and its other descriptions on [topological defects and the vacuum manifold](/wiki/symmetry-breaking/topological-defects#model-i-the-upper-half-plane-times-a-circle).

## The order parameter

An order parameter is a quantity that the broken symmetry changes and that takes a definite, nonzero value in a broken vacuum [T]. A magnet's magnetization is the standard example: it vanishes in the symmetric high-temperature phase, it points along a definite direction in the ordered phase, and a rotation turns it. Its value labels which vacuum the system is in, and the symmetry moves it around the vacuum manifold.

The program's order parameter is the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η, the structure on phase space that marks which directions count as position: "The neutral metric η is emergent — the order parameter" (#11 §4, P2′; [P2′](/wiki/program/postulates/p2-prime)). The toy-model work wrote the requirement as a test: "S3 — η as order parameter. A local operator built from η (equivalently the real structure K, with η = ωK) has a nonzero expectation value in each vacuum and is odd under ρ." (worklog, 'Success criteria'). In model I, "O = K₁₁ flips sign under ρ" (toy-model note §2). See [the order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter).

## The operational definition: criteria S1–S3

The referees' demand, in the worklog's quotation, was "an action in which ρ is a genuine Noether symmetry, spontaneously broken, with η the order parameter" (worklog, 'Success criteria'). Before building anything, the worklog turned each part of that sentence into a pass/fail test ([success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)):

- **S1, a symmetry and not a change of description.** "An explicit action S[fields] on which ρ acts as a symmetry: S is invariant, not merely related to its image by a unitary equivalence. Invariance is verified symbolically." The second clause matters. In ordinary quantum mechanics the Fourier transform implements ρ as a unitary equivalence: it rewrites the same physics in other variables, as a spectrum rewrites a waveform, and constrains nothing. Only a symmetry of an action can be spontaneously broken. See [unitary equivalence versus Noether symmetry](/wiki/phase-space/reciprocity/unitary-equivalence).
- **S2, degenerate vacua that ρ permutes.** "The minima of S form a set on which ρ acts without fixed points: no vacuum is ρ-invariant, and ρ maps each vacuum to another one. Verified."
- **S3, the order parameter.** Quoted in the previous section.

Model I passes all three, and the worklog records the result as "S1 pass [V]", "S2 pass [V]" and "S3 pass [V]", adding: "As predicted, S1–S3 come almost by construction. This is a coset model of Sp(2,R) → Z₂." ('Chunk 1 results'). The complex Grosse–Wulkenhaar model also passes S1–S3 ('Chunk 2 results'; [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)). The tests fix what "spontaneously broken" means in the program's documents; they do not by themselves show that the breaking survives quantum fluctuations, which is the next question.

## Breaking needs infinitely many degrees of freedom

A finite quantum system cannot break a symmetry spontaneously [T]. In a double-well potential the two states localized in the left and right wells have equal energy, but tunnelling connects them. The true ground state is their symmetric combination, which is unique and invariant. Only when the number of degrees of freedom is infinite does the tunnelling amplitude between macroscopically different states vanish, so that the system can stay in one of them [T].

The precise definition uses an order of limits [T]. Add a small explicit term h that favours one vacuum, take the system size to infinity, and only then let h go to zero. If the order parameter stays nonzero, the symmetry is spontaneously broken. Taken in the other order, the limits give zero by symmetry.

The toy models meet both parts of this:

- **Quantum mechanics is too small.** "In 0+1 dimensions (quantum mechanics), tunnelling restores any symmetry, so the toy starts in 1+1." (worklog, criterion S4).
- **A condensate without a volume factor.** In the complex Grosse–Wulkenhaar model the vacuum breaks the duality classically, but "At fixed μ² the condensate occupies finitely many levels: it is a localized lump, not an extended order. Nothing supplies a volume factor that could suppress fluctuations of β." (toy-model note §4), where β is the relative phase of the two condensed levels. The round-4 referee put the conclusion in exactly the order-of-limits form: "beta is one compact collective coordinate with O(1) action (no volume factor), so lim_{h->0} lim_{N->inf} <Delta>_h = 0" (audit notes, Step 2(c)), with N the truncation size and Δ the model's order parameter. See [quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration).
- **Dimension matters even at infinite size.** In two dimensions a compact continuous symmetry cannot break, while a discrete one can; see [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman).

## Spontaneous versus explicit breaking

Explicit breaking puts a non-invariant term into the law itself [T]. The would-be vacua are then no longer degenerate, and the term, not the state, determines which one is realized: a magnet cooled in an external field points along the field. A small explicit term tilts a vacuum manifold that would otherwise be flat, and the would-be massless modes acquire small masses ([pseudo-Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs)).

A spurion keeps symmetry arguments usable when the symmetry is broken explicitly [T]. The symmetry-breaking parameter is treated as if it were a field that transforms under G, which makes the action formally invariant again. The breaking then enters only through the spurion's fixed value, and the symmetry determines which terms that value can generate and at what order.

The record uses each of these ideas:

- **Explicit selection, not spontaneous.** In the real Grosse–Wulkenhaar model, two vacua of equal classical energy have different one-loop free energies, and the lower one is "the one sharper in position" (toy-model note §3). "This is explicit, not spontaneous selection, because the real model is not duality-symmetric: its field is real in position." (toy-model note §3). The root `CLAUDE.md` records it as a lead; see [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead).
- **Explicit and spontaneous together.** In model I the polarization angle is a flat direction of a continuous symmetry, and in 1+1 dimensions it cannot order. To get a definite polarization the note adds "a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" (toy-model note §4). The potential breaks the continuous symmetry explicitly. ρ remains a symmetry of the action, and the vacuum then breaks it spontaneously: the lattice simulation of [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) finds an ordered ℤ₂ phase ([Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)). #11 §4 names the price: "a rigid, unordered pair of axes, so more structure than ω alone, though less than a rigid η." See [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).
- **A background structure as the explicit breaking (v0.1, superseded).** [The lab notebook](/wiki/history/documents/lab-notebook) gave the potential of the dark-energy field τ ([τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence)) this kind of origin: "its existence comes from the explicit breaking of Grassmannian rotations by the rigid ω (P2) — the rigidity is the 'instanton' that tilts the circle. Its magnitude V₀ is a free parameter here. [P/O]" (#1 §3). The later record does not keep that origin. After [the original P2](/wiki/program/postulates/original-p2) was replaced, [the Debt-1 note](/wiki/history/documents/debt-1-notes) listed "the origin of τ's potential under P2′ (what explicitly breaks Λ(d) rotations — candidate: the section choice itself, or matter loops)" as open (#5 §F). The toy models then found that ω alone leaves the angle flat: "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]", so "A definite polarization needs a ρ-preserving potential on that angle" (#11 §4).
- **A spurion argument.** The notebook also argued that photon dispersion has no linear term: "Corrections to x-sector dispersion require insertions of the symmetry-breaking spurion ⟨J⟩. Under the residual ρ² (a phase-space parity), operators linear in energy are odd and forbidden" [D, schematic] (#1 §4). That argument rests on the discrete breaking pattern ℤ₄ → ℤ₂, which the Goldstone-angle picture has replaced; #11's prediction row 9 still cites it. See [the superseded breaking pattern](/wiki/symmetry-breaking/order-parameter#superseded-the-discrete-breaking-pattern) and [Row 9](/wiki/predictions/photon-dispersion).

## Standard references

Added by the wiki from model memory (†); the program's documents cite none of them for the general theory.

- Y. Nambu and G. Jona-Lasinio (1961)†: spontaneous breaking of a continuous symmetry in a relativistic field theory, by analogy with superconductivity.
- J. Goldstone (1961)†: the massless modes that accompany it.
- S. Coleman, *Aspects of Symmetry* (1985)†: lectures on spontaneous breaking, instantons and tunnelling.
- S. Weinberg, *The Quantum Theory of Fields*, vol. II (1996)†: the general theory of broken symmetries.

## Used by

- [The hard core](/wiki/program/hard-core) — Born reciprocity as an exact symmetry broken by the vacuum.
- [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection) — the selection postulate.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — η as the order parameter.
- [P3: a reciprocity-invariant action](/wiki/program/postulates/p3-reciprocity) — only a symmetry of an action can be spontaneously broken.
- [Mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking) — why some polarization must be selected.
- [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) — what carries the breaking.
- [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) — explicit breaking of the continuous rotation, spontaneous breaking of ρ.
- [The twisted element ρ∘(K → −K)](/wiki/symmetry-breaking/twisted-element) — the stabilizer of a vacuum within the full symmetry group.
- [Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) — "spontaneously broken" as part of the referees' demand.
- [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria) — S1–S3 as the operational definition.
- [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua) — a vacuum manifold and stabilizer computed explicitly.
- [Complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields) — a symmetry, not a covariance, is what a vacuum can break.
- [Complex-model vacua and the polarization Δ(β)](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua) — vacua that break the duality classically.
- [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration) — classical breaking with no volume factor, undone by quantization.
- [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead) — an explicit, not spontaneous, selection.
- [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) — the polarization choice breaks the dual diffeomorphisms spontaneously.
- [Row 9: no linear photon dispersion](/wiki/predictions/photon-dispersion) — the spurion argument under the residual ρ².

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — ρ exact in quantum kinematics; "ρ is exact and spontaneously broken"
- `papers/broken-born-checkpoint-v2.md` §4 — P2′ (η the order parameter) and P5; the v2.2 refinement ("a rigid, unordered pair of axes")
- `papers/reciprocity-toy-models.md` §2 — model I's symmetry group, vacua, stabilizer, order parameter and twisted element; §3 — explicit selection in the real model II; §4 — the ρ-preserving potential and the complex model's missing volume factor; §1 — the setting
- `notes/toy-lagrangian.md` 'Success criteria' — the referees' wording; S1–S3; tunnelling in 0+1
- `notes/toy-lagrangian.md` 'Chunk 1 results', 'Chunk 2 results' — S1–S3 passed in model I ("a coset model of Sp(2,R) → Z₂") and in the complex model II
- `review/round4/referee/audit-notes.md` Step 2(c) — the order-of-limits statement for model II
- `notes/broken-born-theory.md` §3 — v0.1's explicit-breaking origin of V(τ) (superseded); §4 — the spurion ⟨J⟩ and the ρ² argument
- `notes/debt1a-geometric-core.md` §F — the origin of τ's potential under P2′, listed as open
- `verify/toy_coset.py` — the S2 and S3 checks for model I, including the stabilizer {±1}
