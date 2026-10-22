---
title: "Topological defects and the vacuum manifold"
weight: 15
status: established
description: "The vacua of a broken symmetry form the coset G/G₀, one flat direction per broken generator; its homotopy groups decide which defects can form (π₀ walls, π₁ strings, π₂ monopoles, π₃ textures) and why they cannot unwind; the program's vacuum manifolds, its retired π₂ candidate and the two meanings of 'soliton'."
provenance: [T]
sources:
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "verify/toy_coset.py S2"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/ref_xy_trap.py"
  - "review/round4/referee/out_xy_trap.txt"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14 item 8"
  - "notes/broken-born-theory.md §2"
  - "notes/debt1a-geometric-core.md §B"
  - "notes/broken-born-program-v1.md §4"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "review/skeptic-review-console.html '3. The candidate'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "review/v3-worklog.md 'Verified references for v3'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "HANDOFF.md §2"
  - "HANDOFF.md §6"
  - "notes/debt3b-wave-island.md 'Setup'"
  - "review/wiki-build-flags.md item 1"
  - "review/wiki-build-flags.md item 12"
---

*A topological defect is a wall, line or point where a field that has broken a symmetry is held out of its lowest-energy states, because the vacuum values it takes around that place cannot be joined smoothly across it: a domain wall between two regions that settled into different vacua, a string around which the field's vacuum value runs once round a loop, or a point-like monopole around which it covers a sphere. The set of lowest-energy states is the vacuum manifold. When a symmetry group G is spontaneously broken, the vacuum manifold is G/G₀, the group taken modulo the subgroup G₀ that leaves one vacuum in place. Its dimension counts the massless Goldstone modes, and its shape, measured by its homotopy groups, decides which defects a cooling universe can leave and why, once formed, they cannot decay on their own. In the Broken-Born program the vacuum manifold of the polarization, the Lagrangian Grassmannian Λ(d) of all possible choices of which phase-space directions count as position, contains a loop that cannot be shrunk, and the program takes the periodicity of its dark-energy field τ from that loop. The retired dark-matter candidate was a defect of the monopole kind in a hidden gauge sector; it died on the count of how many of them a transition makes, not on their stability. One open question, without a candidate, asks whether topology could keep a single object localized in momentum.*

**Status:** Established — [T] — standard field theory and topology, written here from general knowledge; references added from memory are marked †. The classification of defects by homotopy groups is Kibble's (1976), reference [18] of the withdrawn #14, whose abstract the [round-3](/wiki/method/review/round-3) audit checked. The program statements quoted here keep their own tags: Λ(d) ≅ U(d)/O(d) and π₁(Λ(d)) = ℤ are [T] and the periodicity of τ is [D] (#1 §2; restated in [#11](/wiki/history/documents/checkpoint) §6); model I's vacua, stabilizer and flat directions are [V], checked in `verify/toy_coset.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)); the π₂ monopoles of #14 were a dark-matter candidate that is dead ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## The vacuum manifold [T]

### Vacua as a coset

A symmetry of a field theory is a group G of transformations that leaves its action unchanged. If a vacuum Φ₀, a configuration of least energy, is moved by some element g of G, then g·Φ₀ is another vacuum of exactly the same energy, and the symmetry is spontaneously broken ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)). The elements that leave Φ₀ in place form a subgroup, its stabilizer G₀, also called the unbroken or isotropy subgroup. Applying every element of G to Φ₀ sweeps out its orbit, and two elements give the same vacuum exactly when they differ by an element of G₀. When every vacuum lies on that one orbit, the set of vacua is therefore the coset space

```text
G₀ = {g in G : g·Φ₀ = Φ₀}                the stabilizer of the vacuum Φ₀

vacuum manifold = {g·Φ₀ : g in G} ≅ G/G₀
```

Five standard examples [T]:

- **A magnet.** G is the rotation group SO(3), G₀ the rotations SO(2) about the magnetization axis, and the vacuum manifold SO(3)/SO(2) the sphere S² of directions in which the magnetization can point.
- **A real field with two minima.** A potential such as λ(φ² − v²)² is unchanged by φ → −φ and has the two minima φ = ±v. The reflection moves each of them, G₀ contains only the identity, and the vacuum manifold is two points.
- **A complex field with a circle of minima.** A potential that depends on |φ| alone and is least at |φ| = v is unchanged by the phase rotations U(1). Every rotation other than the identity moves a vacuum v·e^{iα}, and the vacuum manifold is the circle S¹ of phases α.
- **SU(2) broken to U(1) by an adjoint scalar.** The scalar is a three-component vector whose minima lie on a sphere; the rotations about the vacuum's axis form the unbroken U(1), and the vacuum manifold is SU(2)/U(1) = S² ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)).
- **The electroweak theory.** The Higgs doublet has two complex components, four real ones, and its minima form the 3-sphere S³ in that four-dimensional space. SU(2) × U(1) breaks to the U(1) of electromagnetism, and S³ is the vacuum manifold.

### Dimension and flat directions

For a continuous group, each generator outside G₀ moves the vacuum along a direction that costs no energy, so the vacuum manifold has dimension dim G − dim G₀ [T]. These flat directions carry the massless modes of [Goldstone's theorem](/wiki/symmetry-breaking/goldstone-and-higgs#goldstones-theorem), one for each broken generator of a global symmetry. When the broken symmetry is a gauge symmetry, the gauge fields absorb those modes and become massive ([the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs#the-higgs-mechanism)), but the vacuum manifold keeps its shape, and the defects below exist for gauge and global symmetries alike [T].

### Flat directions that no symmetry generates

A potential can also be flat along a direction that no symmetry generates. The set of vacua is then larger than one orbit, and the extra direction is accidental: it is flat in the classical theory, and quantum corrections, which respect only the symmetries, are not bound to keep it flat [T] ([a zero mode that no symmetry protects](/wiki/symmetry-breaking/goldstone-and-higgs#a-zero-mode-that-no-symmetry-protects)). Model I with its bounded potential has such a direction ([below](#with-the-bounded-potential-two-vacua)).

## Homotopy groups [T]

Which defects a vacuum manifold M allows depends on which closed shapes drawn in M can be shrunk to a point without leaving M. The homotopy groups πₖ(M) record the answer:

- **π₀(M)** counts the separate pieces of M. Two points form two pieces; a circle is one.
- **π₁(M)**, the fundamental group, classifies closed loops in M up to continuous deformation. On the circle S¹ a loop is labelled by its winding number, the net number of times it goes round, so π₁(S¹) = ℤ. On the sphere S² every loop can be slid off to one side and shrunk, so π₁(S²) = 0.
- **π₂(M)** classifies the ways of mapping a sphere into M. A map of S² onto itself that covers it once cannot be shrunk; π₂(S²) = ℤ, the integer counting how many times the sphere is covered. In S³ there is room to slide any sphere off and shrink it: π₂(S³) = 0.
- **π₃(M)** classifies maps of the 3-sphere into M. π₃(S³) = ℤ, and also π₃(S²) = ℤ: for a map of S³ to S², the curves that land on two different points of S² are closed loops, and the integer, the Hopf invariant, counts how many times they are linked.

A product of spaces has the homotopy groups of its factors, and a space that can be shrunk to a point within itself, such as a line, a disk or the upper half-plane, has none [T].

## The classification [T]

Below a symmetry-breaking transition the field settles at some point of M in each region, and regions that have not been in contact settle at unrelated points ([the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism#defects-from-a-cooling-field-t)). Far from any defect the field lies in M. Follow it over a closed surface, a closed loop or a pair of points that encloses some region: if the values it takes there form a shape in M that cannot be shrunk, the field cannot be in a vacuum everywhere inside, and the region holds a defect.

| Homotopy group | The field around the defect | Defect | In three space dimensions | Example |
| --- | --- | --- | --- | --- |
| π₀(M) ≠ 0 | different vacua on the two sides | domain wall | a surface | the real field with two minima |
| π₁(M) ≠ 0 | winds around a loop of M | string | a line | the phase of a complex field |
| π₂(M) ≠ 0 | covers a sphere of M | monopole | a point | SU(2) → U(1), M = S² |
| π₃(M) ≠ 0 | covers M over a whole region | texture | not localized | M = S³ |

The round-3 audit summarizes the abstract of Kibble's 1976 paper, #14's reference [18], as "formation of walls, strings or monopoles depends on homotopy groups" (`review/round3/referee/audit-notes.md`, Step 1).

The pattern is a count of dimensions [T]. In D space dimensions, a defect classified by πₖ(M) has dimension D − k − 1. In three dimensions walls are surfaces, strings are lines and monopoles are points. In two, walls are lines and the π₁ defects are points, the vortices whose unbinding drives the Berezinskii–Kosterlitz–Thouless transition of the two-dimensional XY model ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman#why-spin-waves-in-two-dimensions)). When k equals D, the field covers M across a whole region and the object has no core: the texture of the table's last row.

For a symmetry group G that is connected and simply connected, meaning that every loop in it can be shrunk, the groups of the vacuum manifold are fixed by the unbroken subgroup [T] (Mermin 1979 †):

```text
π₁(G/G₀) = π₀(G₀)          π₂(G/G₀) = π₁(G₀)
```

A loop of U(1) that winds once cannot be shrunk, π₁(U(1)) = ℤ, so breaking such a group to a subgroup that keeps a U(1) produces monopoles; this is why every grand unified theory predicts them ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole#why-it-is-stable-winding-t)). Breaking it to a discrete subgroup of more than one element produces strings. A connected group always has a connected vacuum manifold, so domain walls need a broken discrete symmetry, or a symmetry group in separate pieces [T].

What a defect does after it forms depends on its kind [T]. Stable domain walls stretched across the universe would come to dominate its energy density, the domain-wall problem (Zel'dovich, Kobzarev and Okun 1974 †). Superheavy monopoles from a grand unified transition would overclose it, which is [the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem). A network of cosmic strings instead settles into a state in which it keeps a fixed fraction of the total density (Vilenkin and Shellard †).

## Why a defect cannot unwind, and what can remove it [T]

Take a monopole of SU(2) → U(1) as the example. Far from it the scalar field lies on the sphere of vacua, so over a large sphere drawn around the monopole the field's direction defines a map from that sphere to the sphere of vacua, and the map has a class in π₂(S²) = ℤ: the number of times it covers the sphere of vacua. A continuous change of the field cannot change an integer, and the field evolves continuously in time, so the class is conserved. In the hedgehog, the simplest configuration of class one, the field points radially outward at every point of the large sphere. At the centre no direction is continuous with all of these, so the field leaves the vacuum manifold there, Φ = 0, and that costs energy: the defect has a core, whose size is set by the masses of the theory, and it has a mass. The same argument with a loop in place of the sphere applies to strings, and with a pair of points on either side to walls.

Topology fixes the class, not the number of defects or their size:

- **Annihilation.** A defect and its antidefect carry opposite classes, and only the total is conserved, so a monopole and an antimonopole that meet can annihilate ([annihilation is not enough](/wiki/electric-magnetic-duality/monopoles/monopole-problem#annihilation-is-not-enough-t)). A closed loop of string, or a closed bubble of wall, has total class zero and can shrink and disappear.
- **Collapse.** A texture has no core where the field must leave M. In a theory of scalar fields whose energy has only terms with up to two derivatives, a static configuration in three space dimensions lowers its energy by shrinking (Derrick 1964 †), so a texture collapses; at zero size the field leaves the vacuum manifold at one point and the winding is undone (Turok 1989 †). Stable π₃ objects need terms with more derivatives. Such a term stabilizes the knotted Hopf solitons classified by π₃(S²) = ℤ (Faddeev and Niemi 1997 †). Monopoles avoid the collapse because the energy of the gauge field rises as the core shrinks.
- **Finite energy.** In a gauge theory the gauge field cancels the scalar field's gradient energy far from the core, so a gauge string has a finite energy per unit length and a gauge monopole a finite mass. For global defects that energy grows with the size of the region, logarithmically for a string and linearly for a monopole.

## Topological and non-topological solitons [T]

A soliton, in field theory, is a localized lump of field energy that keeps its shape and moves like a particle. A topological soliton keeps its shape because it carries a conserved winding: the defects above, and the Hopf solitons. A non-topological soliton carries no winding; a balance of forces holds it together, and a conserved number of quanta keeps it from dispersing. A Bose star is of the second kind: a self-gravitating lump of a wave field in which gravity balances the gradient energy of the wave ([Bose stars](/wiki/dark-matter/wave-dark-matter/wave-kinetics#bose-stars-t)). The program's documents use the word in both senses ([below](#two-meanings-of-soliton-and-the-name-knots)).

## The program's vacuum manifolds

### The polarization's vacuum manifold and its Maslov loop

The program's order parameter is the [neutral metric](/wiki/phase-space/born-geometry/born-structures) η, the structure on phase space that marks which directions count as position ([the order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter)). Under [P2′](/wiki/program/postulates/p2-prime), with only the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form) ω rigid, the values the order parameter can take form a space of the coset kind. [Calc note #5](/wiki/history/documents/debt-1-notes) §B: "The space of H-compatible real structures on (ℝ^{2d}, I) is {J} ≅ U(d)/O(d) = Λ(d), the Lagrangian Grassmannian — π₁ = ℤ, Maslov circle intact, τ restored" (transcribed from its LaTeX). The [lab notebook](/wiki/history/documents/lab-notebook) heads its paragraph on this space "The vacuum manifold and the Maslov circle" and writes (#1 §2, transcribed from its LaTeX):

> The space of Lagrangian polarizations of ℝ^{2d} is the Lagrangian Grassmannian Λ(d) ≅ U(d)/O(d), compact, of dimension d(d+1)/2 = 10 for d=4. **[T]** Its fundamental group is π₁(Λ(d)) = ℤ, generated by the **Maslov circle** via the map det²: U(d)/O(d) → U(1). **[T]**

In the terms of this page, G is the unitary group U(d), the transformations of phase space that preserve both ω and a fixed metric, which carry the position plane onto every Lagrangian subspace; G₀ is the orthogonal group O(d), which carries it onto itself ([the space of them: U(d)/O(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian#the-space-of-them-udod)). The loop that cannot be shrunk is the Maslov class: along a closed path of polarizations, det² winds around a circle a whole number of times ([the Maslov class](/wiki/phase-space/modular-field/lagrangian-grassmannian#the-maslov-class)). #1 §2 calls the angle around that circle, τ ≡ f · arg det²(·), "a compact, 2πf-periodic modulus of the vacuum", and adds: "Periodicity is topology **[D]**; that τ is the *lightest* modulus, with the other nine directions heavy, is assumed **[P]**." (transcribed from its LaTeX).

The program uses the loop for one purpose, the periodicity of its dark-energy field. #11 §6: "the dark-energy field τ is the Maslov phase of the boundary variable, its periodicity a fact of topology (π₁(U(d)/O(d)) = ℤ)"; [the v1 paper](/wiki/history/documents/checkpoint) adds "not a modeling choice" (#9 §4). The construction is on [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase#why-the-period-is-topology), and τ's cosmology on [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence).

### Strict P2: no Maslov loop

Under the original postulate P2, with η held rigid as well as ω, the loop is lost. #11 §5: "Under strict P2 the compatible polarizations are discrete, so no Grassmannian, no Maslov circle, no dark-energy field". Flag 1 in `review/wiki-build-flags.md` finds "discrete" wrong for d ≥ 2: the polarizations compatible with both structures form continuous families, but det² is constant on each family, so there is still no Maslov circle and no τ; the audit confirmed the flag with two independent checks. The loss of the loop is part of the argument of [the nontriviality theorem](/wiki/program/postulates/nontriviality-theorem), by which the program has content only if η is emergent.

### Model I: the upper half-plane times a circle

[Model I](/wiki/symmetry-breaking/toy-models/coset-model), the coset toy model, makes each object of the first section explicit at d = 1 (toy-model note §2). Its fields on a 1+1-dimensional base are a metric H on the phase plane, given by a point Z = X + iY of the upper half-plane, and a real structure K, with K² = 1, that marks which line of the plane counts as position. The symplectic group Sp(2, ℝ) acts on both, and "the action is invariant". The vacua are the compatible pairs (H, K); at H = 1 they form the circle

```text
K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]                     (toy-model note §2)
```

and "The vacuum manifold is the upper half-plane times this circle" (§2), "a 3-dimensional space" (worklog, 'Chunk 1 results'). "The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}" (§2), with K₀ = diag(1, −1); [the gate](/wiki/method/verification/the-gate) checks it and adds "(so the orbit is 3-dimensional)" (`verify/toy_coset.py`). The worklog states the pattern in this page's terms: "Only {±1} leaves a vacuum fixed, so Sp(2,R) → Z₂ = {1, ρ²}", and "This is a coset model of Sp(2,R) → Z₂." ('Chunk 1 results'). The full calculation is on [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua).

The [round-4](/wiki/method/review/round-4) referee's novelty search names the same space as a group: "Model I appears new as a field theory, but it is a simple coset (vacuum manifold PSL(2,R))" (`review/round4/referee/audit-notes.md`, Step 3). The two descriptions agree [T]. Sp(2, ℝ) is the group SL(2, ℝ) of real linear maps of the plane with unit determinant; dividing it by the stabilizer {±1} gives PSL(2, ℝ), which has the dimension of the group, since the stabilizer is discrete; and as a space PSL(2, ℝ) is the upper half-plane times a circle.

The dimension count is the one of the first section: the group is three-dimensional and the stabilizer discrete, so three directions are flat, "the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)" (§2; [the spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua#the-spectrum-three-flat-directions-and-one-massive)). The upper half-plane, the [Siegel domain](/wiki/phase-space/modular-field/siegel-domain) at d = 1, can be shrunk to a point within itself, so the loops of this vacuum manifold that cannot be shrunk are those of the circle factor [T]. That circle is Λ(1), and its loop is the d = 1 case of the Maslov class: the worklog calls the compact Goldstone direction "the Lagrangian Grassmannian Λ(1), which is the checkpoint's Maslov circle (the τ field of §10)" ('Chunk 1 results').

The model has one more symmetry, the flip K → −K, and within the full group the reference vacuum keeps an element: "the twisted element ρ∘(K → −K) maps (1, K₀) to itself" (§2). The breaking of ρ therefore has physical consequences only once something couples to the sign of K ([the twisted element](/wiki/symmetry-breaking/twisted-element)).

### With the bounded potential: two vacua

The toy-model note: "In 1+1 the compact angle φ cannot order" (§4; [the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)). To get a definite polarization it adds "a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" (§4). With its bounded form, [V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential), and H dynamical: "Vacuum manifold: {diag(y, 1/y)} × {±K_ref}." (§4). Its two factors are of the two kinds described in the first section.

- **The line diag(y, 1/y)** is a flat direction that no symmetry generates: "The zero mode is the classical flat line H = diag(y, 1/y), K = K_ref. It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref." (§4). The round-4 adjudication had called the zero mode an exact squeeze symmetry; flag 12 in `review/wiki-build-flags.md`, which the flag audit confirmed, finds the note's wording the accurate one ([the vacuum manifold and the zero mode](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential#the-vacuum-manifold-and-the-zero-mode)).
- **The pair ±K_ref** is a vacuum manifold in two pieces, which ρ exchanges, since ρ sends K(φ) to K(φ + π) = −K(φ) at H = 1 (§2). The worklog: "Then ρ breaks as a Z₂ (Ising class), with vacua ±K_ref: "x is position" and "p is position"." ('Chunk 3 results').

The lattice simulation of [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction), in which H is held at 1 and only the angle φ varies, has the two vacua ±K_ref, and its hot starts trapped. Version 2 of the note: "Hot starts at L = 64 coarsen slowly through metastable domains, so ordered-phase values are reported from cold starts." (§4). The round-4 referee's reading of the trapped runs was "Metastable domain stripes with higher energy; equilibrium is ordered." (`review/round4/referee/audit-notes.md`, Step 2(c)). Its diagnostic script also measured the net number of times the angle φ turns through a full circle along each direction of the periodic lattice (`review/round4/referee/ref_xy_trap.py`), a winding of the π₁ kind, and printed (`review/round4/referee/out_xy_trap.txt`):

```text
L=64 hot seed=1064: E/site=-2.58524  <|m|>=0.0265  winding (x,y)=(+0.02,-0.00)
L=64 hot seed=77: E/site=-2.61222  <|m|>=0.6052  winding (x,y)=(+0.00,+0.08)
L=64 cold seed=1065: E/site=-2.67587  <|m|>=0.9541  winding (x,y)=(-0.00,+0.00)
```

The audit notes summarize the windings as "winding ~0". In the terms of this page, the stripes are domain walls between the two vacua, defects of the π₀ kind, and not windings of the angle ([Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo#start-conditions-hot-starts-trap)).

## Defects in the program

### The retired monopole candidate

Version 2.0 of the checkpoint listed "topological solitons of a p-local gauge sector (§11) as a third candidate, stable by topological charge" (#11 §12). The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) made them monopoles of a hidden SU(2) broken to U(1), with the vacuum manifold of the fourth example above: "SU(2)_d -> U(1)_d has pi_2(SU(2)/U(1)) = pi_2(S^2) = Z and supports 't Hooft-Polyakov monopoles [15], stable by topological charge." (#14 §3; [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). It used the electroweak example to rule out a copy of our own sector (#14 §2):

> An exact mirror copy of the Standard Model cannot serve: the electroweak vacuum manifold is S^3, whose pi_2 vanishes, so it has no stable monopoles. The hidden gauge structure must therefore differ from ours.

The v3 worklog records the same, "π₂(S³) = 0" (`review/v3-worklog.md`, 'v3 as drafted (2026-10-19)').

The topology was not what failed. The candidate died on its abundance: the count of monopoles that [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) gives at formation had been normalized too low, and counted correctly the superheavy monopoles are overproduced ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization); [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). At low breaking scales the scenario is published work, "the established topological-dark-matter scenario [28S, 29S], and nothing in it depends on Born reciprocity" (#11 §12; [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).

Because only the total topological charge is conserved, monopoles and antimonopoles can annihilate in pairs. A chat-only argument held that the net charge left at formation survives annihilation and bounds the relic abundance from below, the "√N topological-charge floor" (`HANDOFF.md` §2, open item 2). It was dropped after round 3 because its premise, Kibble's count as a ceiling, is inverted ([Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor)).

### Two meanings of "soliton", and the name "knots"

"Soliton" has two meanings in the record. In the Debt-3 notes it is the core of a Bose star, a non-topological soliton: "Bose condensation of virialized wave DM into solitons" (#3, 'Setup'; DM is dark matter; [the wave island](/wiki/dark-matter/momentum-clumping/wave-island)). In #14 and #11 §12 it is a topological defect, the monopole above.

The candidate also changed names. Among the round-1 findings incorporated in #14 v2 is a renaming, "'knots' → π₂ monopole-class (renamed)" (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)). #14 v2 states the distinction in the terms of the table above: "monopole-class defects classified by pi_2, not knot solitons in the pi_3/Hopfion sense" (§3, as embedded in `review/skeptic-review-console.html`). The [handoff](/wiki/history/documents/handoff) names the candidate "topological solitons (π₂ monopole-class)" (§2). #11 keeps "knots" in its plain-language passages, "topological knots, heavy defects of a hidden gauge sector" (§12) and "one loophole for individual knots" (§9); in both, the objects are the π₂ monopoles.

### The topological loophole

[Debt 3](/wiki/history/debts) found collective clumping in momentum space nowhere mandatory ([the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem)), but its calculations treat a gas of particles or a wave field, not single objects. A topological soliton's shape is set by its own field equations, and its winding keeps it from decaying; v2.0 claimed that its candidate's solitons "slip through the Debt-3 loophole (§9), since topology, not collective dynamics, would localize them in momentum" (#11 §12). With the candidate retired, #11 §12 lists: "The Debt-3 loophole — topological momentum-space localization of individual objects — remains untested, but has no candidate." See [Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole), and [conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles) for what such objects would be if the momentum-polarized sector has them.

## What the record leaves open

- **The loophole.** The one registered open item that turns on topology is the Debt-3 loophole above, listed in [open problems and the queue](/wiki/status/open-problems). #11 §14 item 8 calls the p-localization items "closed by the §12 obituary", and the checkpoint does not reconcile the two wordings.
- **Defects of the program's own breaking.** No document asks whether the vacuum's selection of a polarization, if it happened as the early universe cooled, would leave defects. The topological facts that would bear on the question are in the record for other purposes: the loop of Λ(d), for the periodicity of τ, and the two vacua ±K_ref of the 1+1-dimensional toy model, for its ℤ₂ order. The wiki records the absence and draws no conclusion from it.

## References

From the record:

- T. W. B. Kibble, "Topology of Cosmic Domains and Strings", J. Phys. A 9, 1387 (1976) — #14 [18], without a tag; the title is the v3 worklog's correction ('Verified references for v3'), and the round-3 audit checked the abstract.

Added by the wiki from model memory (†):

- N. D. Mermin, "The topological theory of defects in ordered media," Reviews of Modern Physics (1979)†: the homotopy classification of defects, with the rules for G/G₀.
- A. Vilenkin, E. P. S. Shellard, *Cosmic Strings and Other Topological Defects* (Cambridge University Press)†: defects in cosmology, string networks and the domain-wall problem.
- N. Manton, P. Sutcliffe, *Topological Solitons* (Cambridge University Press)†: monopoles, Hopf solitons and Derrick's theorem.
- G. H. Derrick (1964)†: no stable static solitons of scalar fields with two-derivative terms in three space dimensions.
- Ya. B. Zel'dovich, I. Yu. Kobzarev, L. B. Okun (1974)†: the cosmological domain-wall problem.
- N. Turok (1989)†: the collapse and unwinding of global textures.
- L. Faddeev, A. J. Niemi (1997)†: stable knotted solitons, labelled by the Hopf invariant.

## Used by

- [The Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) — which defects a cooling field leaves, by the homotopy groups of its vacuum manifold.
- [The 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole) — the case π₂(S²) = ℤ.
- [Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs) — one flat direction of the vacuum manifold for each broken generator.
- [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) — its values form Λ(d).
- [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase) — the periodicity of τ from π₁(Λ(d)) = ℤ.
- [The nontriviality theorem](/wiki/program/postulates/nontriviality-theorem) — under strict P2 the Maslov loop is lost.
- [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua) — the upper half-plane times a circle, and the stabilizer {±1}.
- [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) — the vacuum manifold {diag(y, 1/y)} × {±K_ref}.
- [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) — hot starts trapped by domain stripes.
- [The twisted element ρ∘(K → −K)](/wiki/symmetry-breaking/twisted-element) — the stabilizer of a vacuum within the full symmetry group.
- [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) — π₂(S²) = ℤ for the hidden sector, π₂(S³) = 0 against a mirror Standard Model.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — the π₂ candidate, dead on its abundance.
- [Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) — a conserved net topological charge as a floor on the relic abundance.
- [Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole) — localization in momentum by topology.
- [Topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art) — defects of a hidden sector as relics.
- [Conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles) — topological solitons of the momentum-polarized sector, if it has them.

## Sources

- `papers/reciprocity-toy-models.md` §2 — model I's symmetry, vacua, vacuum manifold, stabilizer, twisted element and three flat directions; §4 — the potential that reduces the U(1) to a discrete group, the vacuum manifold {diag(y, 1/y)} × {±K_ref} and its unprotected zero mode, and the metastable domains of hot starts
- `notes/toy-lagrangian.md` 'Chunk 1 results' — "a 3-dimensional space", "Sp(2,R) → Z₂", the compact Goldstone direction as Λ(1); 'Chunk 3 results' — ρ breaks "as a Z₂ (Ising class), with vacua ±K_ref"
- `verify/toy_coset.py` — the stabilizer {±1} and the three-dimensional orbit
- `review/round4/referee/audit-notes.md` Step 2(c) — "Metastable domain stripes", "winding ~0"; Step 3 — "a simple coset (vacuum manifold PSL(2,R))"
- `review/round4/referee/ref_xy_trap.py`, `review/round4/referee/out_xy_trap.txt` — the winding measurement and its output
- `papers/broken-born-checkpoint-v2.md` §5 — no Maslov circle under strict P2; §6 — the periodicity of τ "a fact of topology"; §9 — "one loophole for individual knots"; §12 — the topological candidate, its retirement, the published scenario and the loophole; §14 item 8 — "closed by the §12 obituary"
- `notes/broken-born-theory.md` §2 — Λ(d) under the heading "The vacuum manifold and the Maslov circle", its dimension and π₁ = ℤ [T], the periodicity [D], τ the lightest modulus [P]
- `notes/debt1a-geometric-core.md` §B — Λ(d) restored under P2′, "π₁ = ℤ, Maslov circle intact"
- `notes/broken-born-program-v1.md` §4 — the periodicity "not a modeling choice"
- `notes/knot-dark-matter-standalone.md` §2, §3 — the electroweak S³ with vanishing π₂, and π₂(S²) = ℤ for the hidden sector (withdrawn manuscript; the topology is not what failed)
- `review/skeptic-review-console.html` — #14 v2 §3 as embedded: "not knot solitons in the pi_3/Hopfion sense"
- `review/v3-worklog.md` 'v3 as drafted (2026-10-19)' — "π₂(S³) = 0"; 'Verified references for v3' — the title of Kibble's paper
- `review/round3/referee/audit-notes.md` Step 1 — Kibble's abstract
- `HANDOFF.md` §2 — "π₂ monopole-class" and the √N floor; §6 — the renaming of the "knots"
- `notes/debt3b-wave-island.md` 'Setup' — "soliton" as the core of a Bose star
- `review/wiki-build-flags.md` item 1 — the compatible polarizations under strict P2 are not discrete for d ≥ 2, and the conclusion survives; item 12 — the zero mode is not an exact symmetry
