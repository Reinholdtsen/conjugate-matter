---
title: "Stückelberg fields"
weight: 22
status: established
description: "Fields that restore the gauge symmetry a mass term breaks: A_μ + ∂_μπ for a massive vector, the phase of the Higgs field in the Higgs mechanism, h_μν + ∂_μπ_ν + ∂_νπ_μ for spin 2 with its helicity-1 and helicity-0 parts, what the form shows about the massless limit, the Fierz–Pauli weight and the van Dam–Veltman–Zakharov discontinuity, and the program's use: the modes the momentum graviton X absorbs, which #11 calls the Stückelberg sector, with τ outside it and their mixing open (OP6)."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §7.1"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.2"
  - "wiki/papers/broken-born-checkpoint-v2.md §7.5"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 6"
  - "notes/x-classification.md §3"
  - "notes/x-classification.md §5"
  - "notes/beta-coefficients.md §3"
  - "notes/beta-coefficients.md §5"
  - "notes/broken-born-program-v1.md §5"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "verify/battery.py T4"
---

*Stückelberg fields are extra fields written into a theory of a massive gauge field so that the gauge symmetry its mass term breaks holds again. For a vector field A_μ the mass term m²A_μA^μ changes when A_μ is shifted by the gradient of a function; written in terms of the combination A_μ + ∂_μπ, where π is a new scalar field that shifts back by the same function, it does not. Setting π to zero, the choice called the unitary gauge, returns the original theory, so the construction changes the description and not the physics. The new fields are the would-be Goldstone modes of the [Higgs mechanism](goldstone-and-higgs.md#the-higgs-mechanism) written out as fields: the extra polarizations that a gauge field absorbs, or "eats", when it becomes massive. A massive spin-2 field needs a vector of them, and the vector's gradient part carries the polarization of helicity zero, the one with no spin along the direction of motion. In the Comatter program the [momentum graviton X](../gravity/momentum-graviton/_index.md) becomes massive by absorbing the would-be Goldstone modes of its broken [dual diffeomorphisms](../gravity/momentum-graviton/dual-diffeomorphisms.md) (the local shifts of X), and [checkpoint #11](../history/documents/checkpoint.md) calls these modes "the Stückelberg sector". The [dark-energy field τ](../cosmology/dark-energy/tau-quintessence.md) lies outside that sector at leading order; how strongly the two mix has not been computed and is [open problem 6 (OP6)](../gravity/momentum-graviton/tau-stuckelberg-mixing.md).*

**Status:** Established — [T] — textbook field theory, written here from general knowledge, with the literature it names marked † (among them Stueckelberg 1938 †; Arkani-Hamed, Georgi and Schwartz 2003 †; Hinterbichler 2012 †); no `verify/` script checks it. The program's use is part of the structural derivation of X's mass, "[D — structural]" in [calc note #6](../history/documents/field-equation-notes.md) [§3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) and [D + T] in [#11 §7.1](../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t), with τ's exclusion "[D — leading order]" in calc note [#8 §3](../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) and [D] in [#11 §7.5](../papers/broken-born-checkpoint-v2.md#75-spectrum-d); no document writes X's Stückelberg fields out explicitly. The τ–Stückelberg mixing matrix is open [O] ([#11 §14 item 6](../papers/broken-born-checkpoint-v2.md#14-open-problems)).

## A mass term breaks a gauge symmetry [T]

A gauge symmetry is a redundancy in the description of a field: two configurations related by a gauge transformation describe the same physical state. For the vector field A_μ of electromagnetism the transformation is A_μ → A_μ + ∂_μα, with α any function of spacetime, and the field strength F_μν = ∂_μA_ν − ∂_νA_μ, from which the kinetic term is built, does not change under it. The symmetry does physical work. Of the four components of A_μ, the symmetry and the constraint that comes with it remove two, so a massless vector field carries two polarizations, both transverse to its direction of motion [T].

A mass term, proportional to m²A_μA^μ, is not invariant: under the transformation it changes by terms in ∂_μα. The massive vector field, often called a Proca field, has no gauge symmetry and carries three polarizations, the two transverse ones and a longitudinal one, polarized along the direction of motion [T]. The limit m → 0 is therefore not smooth in this form: a polarization present at every nonzero mass is absent at zero mass, and the massive theory as written does not show what becomes of it.

The same holds for spin 2. The massless graviton of [general relativity](../gravity/spin-2-fields/general-relativity.md#linearized-gravity-and-the-graviton-t) has the gauge symmetry of linearized diffeomorphisms, the linear form of a change of coordinates, δh_μν = ∂_μξ_ν + ∂_νξ_μ, and two polarizations. [The Fierz–Pauli mass term](../gravity/spin-2-fields/fierz-pauli.md) breaks that symmetry, and the massive field carries five polarizations [T].

## The vector case [T]

### The construction

Stueckelberg (1938 †) restored the symmetry of the massive vector by adding a scalar field π that shifts under the gauge transformation, and writing the mass term in terms of A_μ + ∂_μπ:

```text
massless vector     F_μν = ∂_μA_ν − ∂_νA_μ             unchanged by A_μ → A_μ + ∂_μα
mass term           m² A_μ A^μ                          changed by it
Stückelberg form    m² (A_μ + ∂_μπ)(A^μ + ∂^μπ)         unchanged by A_μ → A_μ + ∂_μα,  π → π − α
unitary gauge       π = 0 gives back the mass term m² A_μ A^μ
```

The combination A_μ + ∂_μπ is unchanged because the shift of A_μ and the shift of ∂_μπ cancel; π is the Stückelberg field. The new theory has one more field and one more gauge symmetry than the old, and the two additions offset each other. Any configuration can be brought to π = 0 by the transformation with α = π, and in that gauge the Stückelberg theory is the massive vector theory term by term. The gauge π = 0 is called the unitary gauge, because in it only the physical polarizations appear [T].

### What the form shows

The construction changes no prediction. Its use is that it shows how the massive theory behaves at energies well above m [T]. With π rescaled to φ = mπ, and up to the overall normalization of the mass term,

```text
m² (A_μ + ∂_μπ)(A^μ + ∂^μπ) = m² A_μA^μ + 2m A^μ∂_μφ + ∂_μφ ∂^μφ        φ = mπ
```

The last term is the kinetic term of a scalar field, and the middle one couples the scalar to A_μ with a strength proportional to m. As m → 0 the coupling vanishes, and the theory separates into a massless vector with two polarizations and a massless scalar with one: three polarizations, the same number as at nonzero mass. At energies far above m the longitudinal polarization of the massive vector behaves as the scalar φ, and the amplitudes for producing it approach those for producing φ, a statement known as the Goldstone boson equivalence theorem [T].

The scalar's coupling to matter vanishes for a different reason. If A_μ couples to a conserved current J^μ, the substitution adds a coupling of ∂_μφ to J^μ, which is a total derivative and drops out. φ then decouples from the current, and the massless limit of a massive vector coupled to a conserved current is smooth [T].

### The Higgs mechanism in this form

In the abelian Higgs model, a complex scalar field Φ, charged under A_μ, has a nonzero vacuum value of magnitude v ([the Higgs mechanism](goldstone-and-higgs.md#the-higgs-mechanism)). Written in terms of a magnitude v + h and a phase θ, the field transforms under the gauge symmetry by a shift of θ, and in the kinetic term of Φ the phase appears only in the combination A_μ − ∂_μθ/g, with g the gauge coupling. At h = 0 that kinetic term is a mass term for A_μ in Stückelberg form, with π = −θ/g and a mass proportional to gv [T]. The Stückelberg field is the phase of the Higgs field, the would-be [Goldstone mode](goldstone-and-higgs.md#goldstones-theorem) of the broken symmetry. The unitary gauge is the gauge in which the phase is zero, and what remains of Φ is the radial mode h, the Higgs boson. With the radial mode held fixed, the abelian Higgs model is the Stückelberg theory [T].

This is the sense of "eaten": in unitary gauge the would-be Goldstone mode no longer appears as a field, and its degree of freedom is the longitudinal polarization of the massive vector [T]. The Stückelberg form and the Higgs mechanism answer different questions. The Stückelberg form takes the mass as given and rewrites the theory so that its gauge symmetry is visible; the Higgs mechanism supplies a vacuum value that produces the mass [T].

## A massive spin-2 field [T]

### The Stückelberg vector

The [Fierz–Pauli](../gravity/spin-2-fields/fierz-pauli.md) theory of a massive spin-2 field h_μν keeps the gauge-invariant kinetic term of the massless graviton and breaks the linearized diffeomorphisms only through its mass term. A vector Stückelberg field π_μ restores the symmetry, and π_μ in turn contains a scalar (Arkani-Hamed, Georgi and Schwartz 2003 †; Hinterbichler 2012 †):

```text
symmetry of the massless field     δh_μν = ∂_μξ_ν + ∂_νξ_μ
Stückelberg vector                 h_μν → h_μν + ∂_μπ_ν + ∂_νπ_μ       restored, with π_μ → π_μ − ξ_μ
vector and scalar                  π_μ = A_μ + ∂_μφ                     new symmetry A_μ → A_μ + ∂_μΛ,  φ → φ − Λ
together                           h_μν → h_μν + ∂_μA_ν + ∂_νA_μ + 2∂_μ∂_νφ
unitary gauge                      π_μ = 0 gives back the Fierz–Pauli theory
```

Only the mass term changes under the substitution, because the kinetic term is gauge invariant. In four dimensions the four components of π_μ match the four gauge parameters ξ_μ: one would-be Goldstone field for each broken direction of the symmetry. Splitting π_μ into A_μ and the gradient of φ adds a second gauge symmetry, of the vector kind, under which A_μ behaves as the gauge field of the previous section and φ as its Stückelberg field. Fixing that symmetry by ∂^μA_μ = 0 makes A_μ transverse, and the split is then the decomposition of π_μ into a transverse vector and a gradient, the gradient being its longitudinal part [T].

### Five polarizations as 2 + 2 + 1

At energies far above m, with each field rescaled by the power of m that gives it a standard kinetic term, the five polarizations of the massive field separate by helicity, the component of spin along the direction of motion [T]:

- h_μν carries helicity ±2, the two polarizations of a massless graviton;
- A_μ carries helicity ±1, the two of a massless vector;
- φ carries helicity 0.

The helicity-0 scalar φ is the polarization behind the features that separate massive from massless gravity in the next three subsections: the [ghost](../gravity/spin-2-fields/ghosts.md) of a mass term without the Fierz–Pauli weight, the van Dam–Veltman–Zakharov discontinuity, and strong coupling at high energy [T]. [Partially massless gravity](../gravity/spin-2-fields/partially-massless-gravity.md) is the case in which an extra gauge symmetry removes this polarization on a de Sitter background [T].

### The Fierz–Pauli weight

A general mass term for h_μν has the form m²(h_μνh^μν − a h²), where h = h^μ_μ is the trace and a is a relative weight; the Fierz–Pauli term has a = 1 ([the Fierz–Pauli weight](../gravity/spin-2-fields/fierz-pauli.md#the-fierzpauli-weight-t)). After the substitution, the terms that contain φ alone are, with □ = ∂_μ∂^μ the wave operator,

```text
terms in φ alone  ∝  m² [ (∂_μ∂_νφ)(∂^μ∂^νφ) − a (□φ)² ]  =  m² (1 − a) (□φ)²  +  a total derivative
```

For a = 1 they are a total derivative and drop out of the equations of motion. For any other weight φ has a kinetic term with four derivatives, and a field with such a kinetic term propagates an additional mode with negative energy, a ghost: the same extra mode that the Fierz–Pauli page describes through the time components of h_μν [T]. With a = 1 the terms that couple A_μ to φ also cancel, up to a total derivative [T].

In this notation the metric-built mass term that the program's [tuning test](../gravity/tuning-test/_index.md) found, a "quadratic mass m²Tr(h²) with no −(Tr h)²" ([#11 §7.2](../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv)), has a = 0, Tr(h²) being h_μνh^μν and (Tr h)² being h². Battery test T4 checks that comparison numerically [V] ([the metric tier fails twice](../gravity/tuning-test/metric-tier-failures.md); [the verification battery](../method/verification/battery.md)).

### Mixing and the van Dam–Veltman–Zakharov discontinuity

A quadratic term that couples two different fields is called a mixing: neither field then describes a particle of definite mass by itself, and the particles are combinations of the two [T]. With the Fierz–Pauli weight, φ still enters the mass term through a mixing with h_μν, proportional to m²h^μν(∂_μ∂_νφ − η_μν□φ), where η_μν is the Minkowski metric (unrelated to the program's neutral metric η). This two-derivative term is φ's only kinetic term. With φ rescaled by m², the mixing no longer depends on m and survives the limit m → 0.

A field redefinition that shifts h_μν by a term proportional to φη_μν removes the mixing and gives φ a kinetic term of its own. Matter couples to h_μν through its stress-energy tensor T^μν, so the shift leaves φ coupled to the trace T^μ_μ, with a strength that does not vanish as m → 0 [T]. The exchange of φ adds to the force between two bodies, and the force mediated by a massive spin-2 field does not approach that of the massless graviton as the mass goes to zero: the van Dam–Veltman–Zakharov discontinuity (van Dam and Veltman 1970 †; Zakharov 1970 †; [a massive spin-2 mediator](../gravity/spin-2-fields/yukawa-forces.md#a-massive-spin-2-mediator)). The vector A_μ couples to a conserved T^μν only through a total derivative and decouples, as φ does in the vector case [T].

### The high-energy limit

The Stückelberg fields also show at what energy a massive gauge field with no further fields stops being predictive. Their interactions carry derivatives, so in scattering amplitudes they grow with energy. For a massive non-abelian vector field, and for a massive spin-2 field, they become strong at a finite energy set by the mass and the coupling, which for a spin-2 field much lighter than the Planck mass lies far below the Planck mass. Above that energy the theory needs completing: it is an effective theory, valid only below it [T] (Arkani-Hamed, Georgi and Schwartz 2003 †). Letting m go to zero and the Planck mass grow without bound together, in a way that keeps the helicity-0 scalar's leading interactions, isolates those interactions; this is the decoupling limit [T]. De Rham and Gabadadze (2010 †) worked in it, where a ghost shows up as self-interactions of φ with too many derivatives, and chose the coefficients of the potential so that those interactions cancel ([dRGT massive gravity](../gravity/spin-2-fields/drgt-massive-gravity.md)).

## Two metrics [T]

Beyond linear order the mass term of massive gravity compares the dynamical metric g_μν with a second, reference metric f_μν ([the dRGT potential](../gravity/spin-2-fields/drgt-massive-gravity.md#the-potential-t)). A fixed f_μν does not transform under a change of coordinates, so the mass term breaks the invariance under such changes. Arkani-Hamed, Georgi and Schwartz (2003 †) restored it with four scalar Stückelberg fields Π^a, one per spacetime dimension, by writing the reference metric as f_ab(Π)∂_μΠ^a∂_νΠ^b, which transforms as a metric. The unitary gauge is Π^a = x^a, and writing Π^a = x^a − π^a gives back, at linear order, the vector π_μ of the linear theory [T].

When the second metric is dynamical, as in [Hassan–Rosen bimetric gravity](../gravity/spin-2-fields/hassan-rosen-bimetric.md), each metric alone would have its own invariance under changes of coordinates. The interaction potential is invariant only under changes applied to both metrics at once, so it breaks the two invariances to their common part, and the four scalars can be introduced in the same way. About proportional backgrounds, the massless combination of the two metrics keeps the common invariance, and the massive combination absorbs the Stückelberg fields of the broken one [T] ([the bimetric spectrum](../gravity/spin-2-fields/hassan-rosen-bimetric.md#the-spectrum-t)).

## How the program uses them

### The modes X absorbs

The program's momentum graviton X = Re Z, the real part of the [modular field](../phase-space/modular-field/modular-field-z.md), is a symmetric tensor field with a local symmetry of the graviton's kind: "Locally, dual diffeomorphisms act as δX_μν = ∂₍μλ_ν₎ — a second linearized-diff gauge field, because X is *symmetric*" ([#11 §7.1](../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) (ii)). A massless X would be a second graviton, which [the multi-graviton no-go theorem](../gravity/spin-2-fields/multi-graviton-no-go.md) excludes, so X must be massive ([why X must be massive](../gravity/momentum-graviton/forcing-chain.md)). The mass comes from the vacuum, which breaks the dual diffeomorphisms when it selects a [polarization](../phase-space/reciprocity/lagrangian-polarizations.md), a split of phase space into position and momentum: "X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale" ([#11 §7.1](../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) (iii), in a chain tagged [D + T]). Calc note [#6](../../notes/x-classification.md), in a section tagged [D — structural], names the absorbed fields:

> Gravitational Higgs mechanism: the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a **massive spin-2** with its five polarizations, mass M_X = the polarization-breaking scale.

([#6 §3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural); [the gravitational Higgs mechanism](../gravity/momentum-graviton/gravitational-higgs.md).) In the construction above (the wiki's reading of [#6 §2](../../notes/x-classification.md#2-the-gauge-structure-and-the-no-go-d--t)–[§3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)), X stands where h_μν stands, the gauge parameter λ_μ where ξ_μ stands, and π_μ is the Stückelberg vector; λ_μ has four components in four dimensions, the four of #6's count. [#11 §7.5](../papers/broken-born-checkpoint-v2.md#75-spectrum-d) calls the absorbed modes "the Stückelberg sector", in "τ un-eaten (compact J-sector, not the Stückelberg sector)" [D]. The [v1 paper](../history/documents/checkpoint.md) ([#9 §5 item 6](../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved)) and the v0.6 addendum of [the lab notebook](../history/documents/lab-notebook.md) use the same phrase.

### Two wordings, and no explicit form

Calc note #8 describes the absorbed modes differently: "the Higgsing of the dual diffeomorphisms eats the vector π_μ and the *longitudinal scalar of the λ-gradient sector*" ([#8 §3](../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)). [#11 §7.1](../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) follows #6. No document reconciles the two wordings or relates either to the standard split of π_μ into a vector A_μ and the gradient of a scalar φ described above ([conflicts between sources](../history/documents/source-conflicts.md#gravity-and-symmetry-breaking)).

No document writes X's mass term with its Stückelberg fields explicit. The number of absorbed modes is stated, not derived from an action, and #6's own summary lists "the eaten modes counted" ([§5](../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk); [scope of the gravitational Higgs mechanism](../gravity/momentum-graviton/gravitational-higgs.md#scope-and-caveats)). The mechanism also belongs to what #6 calls "the Euclidean-rigorous skeleton" ([§3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)), derived for positive-definite metrics; its extension to the Lorentzian signature of spacetime is [open problem 3 (OP3)](../phase-space/born-geometry/lorentzian-dressing.md).

### τ is outside the Stückelberg sector

τ is a coordinate on [the Lagrangian Grassmannian](../phase-space/modular-field/lagrangian-grassmannian.md) Λ(d), the compact space of polarizations: its [Maslov phase](../phase-space/modular-field/maslov-phase.md). Calc note #6 set it apart from the absorbed modes: "The Λ(d) moduli, τ included, are not the eaten modes — they carry the compact phase directions, which constant shifts do not generate; verifying τ survives un-eaten is flagged [O]." ([#6 §3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). Calc note #8 settled the point at leading order: "τ is a J-modulus on the compact Λ(d), a different sector with different origin; it survives as the light field." ([#8 §3](../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t), [D — leading order]).

In the terms of this page, the fields a gauge field absorbs are those that shift under its own broken gauge transformations [T], here the local shifts of X. τ lies in directions that, in #6's words, constant shifts do not generate, so it is not among those fields and can be involved only through mixing. Applying the rule to τ is the wiki's reading; the claim itself carries #8's tag, [D — leading order]. See [τ is not eaten](../gravity/momentum-graviton/tau-not-eaten.md).

### The mixing left open

Through the potential, τ and the Stückelberg fields can still mix. Calc note #8 records it in a parenthesis: "(Residual τ–Stückelberg mixing through the potential: logged, expected small by compactness.)" ([§3](../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t)), and its close-out lists "(iii) τ–Stückelberg mixing matrix" in the "Open residue, none of it existential" of [the field-equation problem](../history/main-problems.md) ([§5](../../notes/beta-coefficients.md#5-what-remains-honest-close-out)). No document computes the mixing or develops the compactness argument behind the expectation. [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems) keeps the item without the expectation, as item 6: "τ–Stückelberg mixing matrix [O]." The documents do not define the matrix. In standard usage a mixing matrix is the matrix of quadratic couplings between the fields, here τ and the Stückelberg fields, or the rotation that diagonalizes it; from either follow the combinations of fields that have definite masses [T]. See [Open: τ–Stückelberg mixing (OP6)](../gravity/momentum-graviton/tau-stuckelberg-mixing.md).

## What is open

- **τ–Stückelberg mixing.** [OP6](../gravity/momentum-graviton/tau-stuckelberg-mixing.md), item 6 of [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems) [O]; not on the current work queue ([open problems and the queue](../status/open-problems.md)).
- **What X absorbs.** The wordings of [#6 §3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) and [#8 §3](../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) stand unreconciled ([conflicts between sources](../history/documents/source-conflicts.md#gravity-and-symmetry-breaking)).
- **An explicit form.** No document writes X's Stückelberg fields out, so the count of absorbed modes and τ's exclusion rest on structural arguments rather than on an action ([the gravitational Higgs mechanism](../gravity/momentum-graviton/gravitational-higgs.md#scope-and-caveats); [τ is not eaten](../gravity/momentum-graviton/tau-not-eaten.md)).
- **Lorentzian signature.** The mechanism is derived on the Euclidean skeleton ([OP3](../phase-space/born-geometry/lorentzian-dressing.md)).

## Used by

- [The gravitational Higgs mechanism](../gravity/momentum-graviton/gravitational-higgs.md) — X absorbs the would-be Goldstone modes π_μ of the broken dual diffeomorphisms.
- [Dual diffeomorphisms: a second graviton](../gravity/momentum-graviton/dual-diffeomorphisms.md) — the broken gauge symmetry whose would-be Goldstone modes become polarizations of X.
- [Why X must be massive](../gravity/momentum-graviton/forcing-chain.md) — the exit from the chain: X absorbs the would-be Goldstone modes.
- [τ is not eaten](../gravity/momentum-graviton/tau-not-eaten.md) — τ lies in the compact J-sector, "not the Stückelberg sector".
- [Open: τ–Stückelberg mixing (OP6)](../gravity/momentum-graviton/tau-stuckelberg-mixing.md) — the matrix of τ's quadratic couplings to the absorbed modes.
- [τ: hilltop quintessence on the Maslov circle](../cosmology/dark-energy/tau-quintessence.md) — τ survives X's mass mechanism as a light field.
- [τ as the Maslov phase of the boundary](../phase-space/modular-field/maslov-phase.md) — the Maslov phase is not among the absorbed modes.
- [Constrained bimetric gravity](../gravity/tuning-test/constrained-bimetric.md) — τ the light direction of the compact space, X the massive spin-2, their residual mixing open.

## Standard references

Added by the wiki from model memory (†); the program's documents cite none of them.

- E. C. G. Stueckelberg (1938)†: the scalar field that restores the gauge symmetry of a massive vector field.
- N. Arkani-Hamed, H. Georgi, M. D. Schwartz, "Effective field theory for massive gravitons and gravity in theory space," Annals of Physics 305, 96 (2003), [hep-th/0210184](https://arxiv.org/abs/hep-th/0210184)†: Stückelberg fields for massive gravity, the four scalars, and the high-energy behaviour of the helicity-0 mode.
- K. Hinterbichler, "Theoretical aspects of massive gravity," Rev. Mod. Phys. 84, 671 (2012), [arXiv:1105.3735](https://arxiv.org/abs/1105.3735)†: a review, including the Stückelberg form of the Fierz–Pauli theory and its helicity decomposition.
- H. van Dam, M. Veltman, Nucl. Phys. B (1970)†; V. I. Zakharov, JETP Lett. (1970)†: the discontinuity of massive spin-2 exchange.
- C. de Rham, G. Gabadadze (2010)†: the potential built in the limit that isolates the helicity-0 mode.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §7.1](../papers/broken-born-checkpoint-v2.md#71-the-chain-d--t) — the chain: dual diffeomorphisms as a second linearized-diff gauge field, "X eats the four Goldstones" [D + T]; [§7.2](../papers/broken-born-checkpoint-v2.md#72-the-tuning-test-dv) — the metric-tier "quadratic mass m²Tr(h²) with no −(Tr h)²"; [§7.5](../papers/broken-born-checkpoint-v2.md#75-spectrum-d) — "not the Stückelberg sector" [D]; [§14 item 6](../papers/broken-born-checkpoint-v2.md#14-open-problems) — "τ–Stückelberg mixing matrix [O]"
- [`notes/x-classification.md` §3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural) — the four would-be Goldstones π_μ eaten, the five polarizations, τ not among the eaten modes, its verification flagged [O], the Euclidean-rigorous skeleton [D — structural]; [§5](../../notes/x-classification.md#5-the-field-equation-problem-after-this-chunk) — "the eaten modes counted"
- [`notes/beta-coefficients.md` §3](../../notes/beta-coefficients.md#3-spectrum-parameters-selection-structure-d--t) — the second wording of the absorbed modes, τ not eaten [D — leading order], the residual τ–Stückelberg mixing logged; [§5](../../notes/beta-coefficients.md#5-what-remains-honest-close-out) — the mixing matrix in the field-equation problem's open residue
- [`notes/broken-born-program-v1.md` §5 item 6](../../notes/broken-born-program-v1.md#5-the-second-graviton-and-its-mass-the-field-equation-problem-solved) — "not the Stückelberg sector" (superseded as reference)
- [`notes/broken-born-theory.md`](../../notes/broken-born-theory.md) 'Addendum (v0.6)' — "not the Stückelberg sector"
- [`verify/battery.py`](../../verify/battery.py) T4 — the metric-tier mass term compared with the Fierz–Pauli form
