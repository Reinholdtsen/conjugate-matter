---
title: "Goldstone modes and the Higgs mechanism"
weight: 20
status: established
description: "Massless modes of broken continuous symmetries and their count from the Hessian, pseudo-Goldstone modes and flat directions no symmetry protects; gauge fields that absorb Goldstones and become massive, Stückelberg fields, and inverse-Higgs constraints — with the program's uses in model I and in the momentum graviton X."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §14 item 6"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §5"
  - "notes/debt1a-ii-X-classification.md §1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-geometric-core.md §D"
  - "notes/debt1a-geometric-core.md §F"
  - "notes/broken-born-theory.md §4"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "review/round4-adjudication.md 'Rulings' F2"
  - "review/round4/referee/audit-notes.md 'Step 2(a)'"
  - "verify/toy_coset.py 'Spectrum'"
  - "verify/toy_s4.py"
---

*A Goldstone mode is a massless excitation that appears when a continuous symmetry of the laws is broken by the ground state. Moving along the family of equally good ground states costs no energy, so a slow, long-wavelength wave of that motion costs arbitrarily little, and the particle it describes has no mass. If a small explicit term tilts the family, the mode acquires a small mass and is called a pseudo-Goldstone mode. When the broken symmetry is a gauge symmetry, the Higgs mechanism applies instead: the gauge field absorbs the would-be Goldstone modes as extra polarizations and becomes massive. The program uses all three ideas. In its coset toy model the polarization angle is a Goldstone direction, which an added potential turns into a pseudo-Goldstone mode, and its momentum graviton X gets its mass from a gravitational version of the Higgs mechanism.*

**Status:** Established — [T] — textbook field theory, explained here from general knowledge; the program's applications are the Hessian count of the coset toy model [V] (`verify/toy_coset.py`; [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) and the [Debt-1](/wiki/history/debts) derivation of X's mass, tagged [D + T] in [#11](/wiki/history/documents/checkpoint) §7.1 and "[D — structural]" in its calc note.

## Goldstone's theorem

When a continuous global symmetry G is spontaneously broken to a subgroup G₀, the vacuum manifold G/G₀ has one flat direction for each broken generator ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)). Goldstone's theorem says that in a Lorentz-invariant field theory each of these directions carries a massless spin-0 particle [T].

The reason is clearest in terms of waves. A uniform shift of the whole system along the vacuum manifold costs no energy, because it only exchanges one vacuum for another. A shift that varies slowly in space, with wavelength λ, costs only gradient energy, which falls toward zero as λ grows. The frequency of such a wave therefore goes to zero with its wavenumber k, and with Lorentz invariance the frequency is c|k|, the dispersion of a massless particle [T]. Spin waves in a magnet and sound waves in a crystal are the condensed-matter counterparts; without Lorentz invariance their dispersion, and sometimes their number, can differ [T].

### Counting with the Hessian

Classically the count is a statement about the potential V at its minimum Φ₀ [T]. The matrix of second derivatives there, the Hessian, is the mass-squared matrix of small oscillations:

```text
M²ᵢⱼ = ∂²V/∂Φᵢ∂Φⱼ   at Φ = Φ₀

massive modes        = rank of M²
flat directions      = number of fields − rank of M²
Goldstone directions = dim G − dim G₀  (each one flat)
```

Every broken generator moves the vacuum along the vacuum manifold, so each gives a null direction of the Hessian [T]. The converse fails. A null direction that does not come from a broken symmetry is accidental, and nothing guarantees that it survives higher-order terms or quantum corrections [T]. The individual eigenvalues also depend on how the fields are parametrized; at a critical point the rank and the number of negative eigenvalues do not (Sylvester's law of inertia) [T]. The toy-model record shows both facts. For the same saddle of model I with its first, unbounded potential ([the naive potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), now dead), the [round-4](/wiki/method/review/round-4) referee reports the negative eigenvalue −3.3723 (`review/round4/referee/audit-notes.md`, Step 2(a)) and the adjudication −6.47, "in my coordinates" (`review/round4-adjudication.md`, F2); the values differ, and both are negative.

## The count in model I

The program's coset toy model ([model I](/wiki/symmetry-breaking/toy-models/coset-model)) is a field theory of a phase-space metric H and a real structure K on a 1+1-dimensional base, with the Euclidean Lagrangian (toy-model note §2)

```text
L = (f_H²/8) Tr(H⁻¹∂H H⁻¹∂H) + (f_K²/4) Tr(H⁻¹ ∂Kᵀ H ∂K) + (λ/8) Tr(H⁻¹ Cᵀ H C),   C = KI + IK
```

where I ≡ ω⁻¹H. "The potential vanishes exactly when K is compatible with H" (toy-model note §2), and at H = 1 [the gate](/wiki/method/verification/the-gate) checks that it is a sum of squares (`verify/toy_coset.py`). The compatible pairs, the vacua, form "the upper half-plane times a circle of K's, a 3-dimensional space" (worklog, 'Chunk 1 results'). The fields span four directions, two for H and two for K, whose target is "two-dimensional de Sitter space" (toy-model note §2). So at a vacuum the potential is flat along three directions and curves upward in one. The gate's spectrum section is headed "4 fields, 3-dim vacuum manifold", and its check reads:

```text
PASS  potential Hessian has rank 1: three flat directions (Goldstones), one massive  [[0, 4, 0, 0]]
```

The note states the result: "The potential's Hessian has rank 1 at the vacuum. That leaves three Goldstone directions: the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)." (toy-model note §2). [The Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian) Λ(d) is the space of possible position subspaces, a circle when d = 1. The worklog marks the result "Spectrum [V]" and identifies the compact direction: "The compact Goldstone is the rotation of K at fixed H: the Lagrangian Grassmannian Λ(1), which is the checkpoint's Maslov circle (the τ field of §10)." ('Chunk 1 results'). The round-4 referee, in other coordinates, found "rank 1, eigenvalues {3:1, 0:3} -> 3 flat directions" (audit notes, Step 2(a)): a different nonzero eigenvalue, the same rank.

Here every flat direction is a Goldstone direction. The stabilizer of a vacuum in [Sp(2, ℝ)](/wiki/phase-space/reciprocity/symplectic-form) is the discrete group {±1} (toy-model note §2), so the number of broken directions equals the dimension of the vacuum manifold. Their characters differ:

- **The compact angle φ** is the program's [polarization angle](/wiki/symmetry-breaking/goldstone-angle). At H = 1 its kinetic term is "(f_K²/4) Tr(dKᵀ dK) = (f_K²/2)(dφ)²", "an XY stiffness" (`verify/toy_s4.py`, docstring). In 1+1 dimensions this compact mode cannot order ([the Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)).
- **The two half-plane directions** belong to the H-sector, which round 4 identified as "a hyperbolic SO(1,2) model" that can break even in two dimensions (`review/round4-adjudication.md`, "Mermin–Wagner vs [11]"; [coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models)).

Details are on [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua).

## Pseudo-Goldstone modes

A small explicit breaking of the symmetry tilts the vacuum manifold [T]. The would-be Goldstone mode then moves in a shallow potential and acquires a small mass, which vanishes as the explicit breaking is switched off. The pions are the standard example: the chiral symmetry of the strong interaction is broken spontaneously, and the small quark masses break it explicitly, so the pions are light rather than massless [T]. A Goldstone mode couples through derivatives of its field, and a pseudo-Goldstone mode keeps that property apart from terms proportional to the explicit breaking [T].

The program meets the idea twice:

- **The polarization angle with a ρ-preserving potential.** To make the polarization definite, model I adds a potential that keeps ρ and reduces the continuous rotation of K to a discrete group. In its bounded form, at H = 1, "V_b = −(μ/2)(1 + cos 2φ)" (toy-model note §4), with its minima at the two vacua ±K_ref. The worklog draws the conclusion: the toy supports "broken reciprocity" in the form "a pseudo-Goldstone polarization angle with a ρ-symmetric potential", not "only ω rigid, nothing else" ('Chunk 3 results'). See [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) and [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).
- **The dark-energy field τ.** [The lab notebook](/wiki/history/documents/lab-notebook): "τ is a (pseudo-)Goldstone: derivatively coupled, no tree-level Yukawa to SM matter, safe from torsion-balance bounds despite being ultralight. [D]" (#1 §4), where SM is the Standard Model. See [fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force).

### A zero mode that no symmetry protects

With V_b and H dynamical, the reference vacuum is "a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236" (toy-model note §4; `verify/toy_coset.py`). The zero is the accidental kind described above: "The zero mode is the classical flat line H = diag(y, 1/y), K = K_ref. It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref. Boosts are penalized." (toy-model note §4). The round-4 adjudication worded it differently, as "the residual diagonal squeeze, which is an exact symmetry" (F2). The note v2 outranks the adjudication, and the wiki follows the note ([the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential); [conflicts between sources](/wiki/history/documents/source-conflicts#postulates-and-the-toy-models); see flag 12 in `review/wiki-build-flags.md`).

## The Higgs mechanism

When the broken symmetry is a local, gauge symmetry, the would-be Goldstone fields are not physical [T]. A gauge transformation can remove them, so they never appear as massless particles. Their degrees of freedom reappear as the longitudinal polarization of the gauge field, which becomes massive, with a mass set by the gauge coupling and the vacuum value of the field that breaks the symmetry. A massless gauge field carries only transverse polarizations; the massive one carries one more, and that one is the absorbed Goldstone mode. The W and Z bosons of the weak interaction get their masses this way, and inside a superconductor the photon does, which is why magnetic fields are expelled from it beyond a penetration depth [T].

### Stückelberg fields

The massive theory can be written with the absorbed mode kept in view, as a Stückelberg field [T]. For a vector field:

```text
mass term                 m² A_μ A^μ                          not gauge invariant
Stückelberg form          m² (A_μ + ∂_μπ)(A^μ + ∂^μπ)          invariant under A_μ → A_μ + ∂_μα,  π → π − α
unitary gauge             π = 0 returns the massive vector
```

The mass term looks as if it breaks the gauge symmetry; written with π it keeps it, and π is the Goldstone field the gauge field absorbs [T]. The same device works for a massive spin-2 field h_μν, whose mass term breaks the linearized diffeomorphisms δh_μν = ∂_μξ_ν + ∂_νξ_μ. Restoring them introduces a vector Stückelberg field π_μ through h_μν → h_μν + ∂_μπ_ν + ∂_νπ_μ, and π_μ can be split further into a transverse vector and the gradient of a scalar, the scalar carrying the longitudinal (helicity-zero) mode [T].

### Masses from a vacuum value

In the Standard Model a fermion gets its mass from a Yukawa coupling to the Higgs field: once the Higgs field takes its vacuum value, the coupling becomes a mass term, proportional to the coupling constant times that value [T]. The toy-model note uses this as its analogy for matter locality: locality in the selected position variable "follows from the vacuum once matter couples this way, as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling." (toy-model note §5). See [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).

## The gravitational Higgs mechanism of X

The program's [momentum graviton](/wiki/gravity/momentum-graviton) X = Re Z, the real part of the [modular field](/wiki/phase-space/modular-field/modular-field-z), gets its mass by this mechanism, with linearized diffeomorphisms in place of an internal gauge symmetry. #11 §7.1 gives the chain [D + T]:

1. "The rigid Sp(2d,ℝ) contains Z → Z + B (B symmetric): X is shift-symmetric — axion-like, never auxiliary." Constant shifts of X are exact symmetries, so "X has no potential and no non-derivative couplings from the geometric sector alone" (calc note [#6](/wiki/history/documents/debt-1-notes) §1), and "The mass cannot be written by hand (shift symmetry) — but it doesn't need to be." (#6 §3; [the shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)).
2. "Locally, dual diffeomorphisms act as δX_μν = ∂₍μλ_ν₎ — a second linearized-diff gauge field, because X is *symmetric*". Massless, X would be a second graviton, which "is excluded by the multi-graviton no-go [8†]" ([the multi-graviton no-go](/wiki/gravity/spin-2-fields/multi-graviton-no-go)); without the gauge symmetry, it is excluded "by Lorentz signature" (#11 §7.1; [dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms); [the forcing chain](/wiki/gravity/momentum-graviton/forcing-chain)).
3. "The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale."

The calc note gives the step in Higgs-mechanism terms, tagged "[D — structural]": "The vacuum ⟨Z⟩ = i·g sits at X = 0 and is *moved* by the shifts: the polarization selection (η-emergence) spontaneously breaks the local dual diffeomorphisms. Gravitational Higgs mechanism: the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a massive spin-2 with its five polarizations, mass M_X = the polarization-breaking scale." (#6 §3). The roles map onto the textbook case: X is the gauge field, λ_μ the gauge parameter, the vacuum's choice of polarization the symmetry-breaking vacuum value, and π_μ the absorbed Goldstone fields. See [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs).

Two consequences in the record:

- **What is eaten.** The later calc note words it differently: "the Higgsing of the dual diffeomorphisms eats the vector π_μ and the *longitudinal scalar of the λ-gradient sector*" (#8 §3). The sources do not reconcile the two wordings, and #11 §7.1 follows the first ([conflicts between sources](/wiki/history/documents/source-conflicts#gravity-and-symmetry-breaking)).
- **τ is not eaten.** #6 already set the dark-energy field apart: "The Λ(d) moduli, τ included, are not the eaten modes — they carry the compact phase directions, which constant shifts do not generate; verifying τ survives un-eaten is flagged [O]." (#6 §3). #8 settled it to leading order: "τ is not eaten [D — leading order]: … τ is a J-modulus on the compact Λ(d), a different sector with different origin; it survives as the light field. (Residual τ–Stückelberg mixing through the potential: logged, expected small by compactness.)" (#8 §3). #11 §7.5: "τ un-eaten (compact J-sector, not the Stückelberg sector)". The residual mixing is open problem 6, "τ–Stückelberg mixing matrix [O]" (#11 §14). See [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten) and [Open: τ–Stückelberg mixing](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing).

A massive X also has a finite range. #11 §7.5 gives its couplings to ordinary matter as of gravitational strength and "Yukawa-cut at 1/M_X", the range of a massive mediator ([fifth-force safety of X](/wiki/gravity/momentum-graviton/fifth-force-safety)).

## Inverse-Higgs constraints

When spacetime symmetries such as translations and rotations are broken, the count of one Goldstone mode per broken generator can fail [T]. Some of the would-be Goldstone fields are not independent: a constraint, the inverse-Higgs constraint, expresses them as derivatives of the others, and they drop out. The standard example is a flat membrane. It breaks the translation perpendicular to itself and the rotations that would tilt it; but a tilt is just the slope of the displacement, so the rotations' would-be Goldstones are derivatives of the translation's, and only the displacement remains as an independent mode [T].

The Debt-1 note expects this for the vacuum moduli of the broken geometry: "Field content on the broken vacuum: h_μν (10, graviton) ⊕ X_μν (10, momentum graviton) ⊕ Λ(d) σ-modes (10: τ plus nine, of which inverse-Higgs constraints likely eliminate most [O]) ⊕ matter." (#5 §D). Its closing list of open items includes "inverse-Higgs accounting of the nine heavy moduli" (#5 §F). #11 §14 does not carry the item; the wiki keeps it open. The nine heavy moduli also appear in the sketch of [polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis). See [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content).

## Standard references

Added by the wiki from model memory (†); the program's documents cite none of them for the general theory.

- J. Goldstone (1961)†; J. Goldstone, A. Salam and S. Weinberg (1962)†: the massless modes of a broken continuous symmetry.
- P. W. Anderson (1963)†: the photon mass in a superconductor. F. Englert and R. Brout (1964)†; P. W. Higgs (1964)†; G. S. Guralnik, C. R. Hagen and T. W. B. Kibble (1964)†: the mechanism in relativistic gauge theory.
- E. C. G. Stueckelberg (1938)†: the field that bears his name.
- N. Arkani-Hamed, H. Georgi and M. D. Schwartz (2003)†: Stückelberg fields for massive gravity.
- E. A. Ivanov and V. I. Ogievetsky (1975)†: the inverse Higgs phenomenon. I. Low and A. V. Manohar (2002)†: Goldstone counting when spacetime symmetries break.

## Used by

- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — the v2.2 refinement: the polarization is a Goldstone angle.
- [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) — the vacuum's polarization as a flat direction.
- [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) — the potential that turns the angle into a pseudo-Goldstone mode.
- [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua) — three Goldstone directions from a rank-1 Hessian.
- [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) — the pseudo-Goldstone angle and the unprotected zero mode.
- [Complex-model vacua and the polarization Δ(β)](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua) — the relative phase β as a flat direction.
- [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) — the Yukawa analogy: masses from a Higgs vacuum value.
- [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) — the weak form of locality as the Yukawa analogy, the strong form open.
- [Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) — locality beyond the weak (Yukawa-like) form as an open part.
- [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria) — criterion S5 written as the analogue of Yukawa-generated masses.
- [Dual diffeomorphisms: a second graviton](/wiki/gravity/momentum-graviton/dual-diffeomorphisms) — the would-be Goldstones become extra polarizations of X.
- [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) — the last link of the chain: X absorbs the would-be Goldstone modes.
- [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner) — mass, from the broken dual diffeomorphisms, as the only exit.
- [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs) — X becomes massive by absorbing the Goldstones of the broken dual diffeomorphisms.
- [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten) — τ survives as the light field.
- [Open: τ–Stückelberg mixing](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing) — residual mixing with the eaten modes.
- [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content) — the nine heavy moduli, of which inverse-Higgs constraints "likely eliminate most".
- [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase) — the Maslov phase as a (pseudo-)Goldstone mode of the vacuum.
- [Fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force) — τ as a derivatively coupled (pseudo-)Goldstone.

## Sources

- `papers/broken-born-checkpoint-v2.md` §7.1 — the chain: shift symmetry, dual diffeomorphisms, X eats the four Goldstones [D + T]; §7.5 — τ un-eaten; the Yukawa cut at 1/M_X; §14 item 6 — τ–Stückelberg mixing [O]
- `papers/reciprocity-toy-models.md` §2 — model I's Lagrangian, rank-1 Hessian and three Goldstone directions; §4 — V_b at H = 1, its Hessian with H dynamical and its unprotected zero mode; §5 — the Yukawa analogy
- `notes/debt1a-ii-X-classification.md` §1 — X has no potential from geometry; §3 — the gravitational Higgs mechanism, mass M_X, τ not among the eaten modes [D — structural]
- `notes/debt1a-iv-beta-coefficients.md` §3 — what is eaten; τ not eaten at leading order
- `notes/debt1a-geometric-core.md` §D — the Λ(d) σ-modes and inverse-Higgs constraints [O]; §F — "inverse-Higgs accounting of the nine heavy moduli" as open
- `notes/broken-born-theory.md` §4 — τ as a (pseudo-)Goldstone [D]
- `notes/toy-lagrangian.md` 'Chunk 1 results' — "Spectrum [V]" and the compact Goldstone as Λ(1); 'Chunk 3 results' — "a pseudo-Goldstone polarization angle with a ρ-symmetric potential"
- `review/round4-adjudication.md` 'Rulings' F2 — the zero mode called an exact symmetry; eigenvalues "in my coordinates"; "Mermin–Wagner vs [11]" — the hyperbolic H-sector
- `review/round4/referee/audit-notes.md` Step 2(a) — the referee's independent Hessian count
- `verify/toy_coset.py` — the Hessian-rank check and V_b's stability; `verify/toy_s4.py` — the docstring's XY stiffness of φ
