---
title: "The Mermin–Wagner–Coleman theorem"
weight: 30
status: established
description: "No spontaneous breaking of a compact continuous symmetry in two dimensions, and none at all in 0+1 because of tunnelling: the spin-wave reason, what escapes the theorem, why the toy models start in 1+1, and what the lattice runs show."
provenance: [T]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/reciprocity-toy-models.md refs [13]–[15], [17]"
  - "review/round4-adjudication.md 'Rulings' (Mermin–Wagner vs [11])"
  - "review/round4-adjudication.md 'Revisions' 1"
  - "review/round4/referee/audit-notes.md 'Step 1'"
  - "review/round4/referee/audit-notes.md 'Step 2(c)'"
  - "review/round4/referee/audit-notes.md 'Step 3'"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Predictions'"
  - "notes/toy-lagrangian.md 'Chunk 1 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/toy-lagrangian.md 'Assessment'"
  - "verify/toy_s4.py"
---

*The Mermin–Wagner–Coleman theorem says that in two dimensions a continuous symmetry of the compact kind, such as rotation through an angle, cannot be spontaneously broken. The two dimensions can be two of space at nonzero temperature, or one of space and one of time in a quantum field theory. Slow, long-wavelength wobbles of the would-be ordered direction cost so little energy that they grow without limit as the system gets larger, and they wash the order out. Discrete symmetries escape the theorem, as the two-dimensional Ising magnet shows, and so do some non-compact symmetries. With only a few degrees of freedom, as in ordinary quantum mechanics (0+1 dimensions), not even a discrete symmetry breaks, because tunnelling mixes the would-be ground states. These limits determined how the program's toy models were built: they start in 1+1 dimensions, and their compact polarization angle can order only after a potential reduces its symmetry to a discrete one.*

**Status:** Established — [T] — Mermin and Wagner (1966) and Coleman (1973), the toy-model note's references [13] and [14], which the [round-4](/wiki/method/review/round-4) referee found and checked against their statements; their reach in the toy models was fixed by the round-4 ruling that restricts the theorem to the compact SO(2) containing ρ (`review/round4-adjudication.md`); the lattice illustration is `verify/toy_s4.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## The theorem

Two results, from statistical mechanics and from field theory, make up the theorem [T]:

- **Mermin and Wagner (1966).** In the isotropic Heisenberg model with short-range interactions, in one or two dimensions, there is no spontaneous magnetization, and no sublattice magnetization, at any nonzero temperature. Hohenberg (1967)† proved the same for superfluid and superconducting order.
- **Coleman (1973).** His paper is titled "There are no Goldstone bosons in two dimensions". In a quantum field theory with one space and one time dimension, a continuous internal symmetry cannot be spontaneously broken. Breaking would require a massless Goldstone boson ([Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs)), and in two dimensions a massless scalar field fluctuates too strongly at long wavelengths to exist as one.

The two are one statement. A quantum field theory in n space dimensions at zero temperature becomes, after the rotation to imaginary time, a statistical system in n + 1 Euclidean dimensions [T]. A 1+1-dimensional field theory therefore corresponds to a two-dimensional classical system at nonzero temperature, with the quantum fluctuations playing the role of thermal ones. The program's [model I](/wiki/symmetry-breaking/toy-models/coset-model) is written this way, with a "Euclidean Lagrangian" (toy-model note §2), and its lattice version is simulated as a two-dimensional classical system, "On a square lattice (Euclidean 2D)" (`verify/toy_s4.py`, docstring).

The toy-model note states the theorem with its known exception: "Continuous compact symmetries cannot break spontaneously in two dimensions [13, 14]. Non-compact hyperbolic models are an exception [15]." (§1).

## Why: spin waves in two dimensions

The reason is clearest for planar spins, an angle θ at each lattice site with an energy that depends only on the angle differences of neighbours, the XY model [T]:

```text
E = −J Σ⟨ij⟩ cos(θᵢ − θⱼ)          ≈   (J/2) ∫ (∇θ)² d²x   at long wavelengths
```

Rotating every angle by the same amount costs nothing, so the ordered state is a continuous family. A wave of θ with wavenumber k costs energy proportional to Jk², and at temperature T each such mode carries, by equipartition, a mean-square amplitude proportional to T/(Jk²) [T]. Adding up the modes in two dimensions gives

```text
⟨θ²⟩ = (T/J) ∫ d²k/(2π)² 1/k²  ≈  (T/2πJ) ln(L/a)          L the system size, a the lattice spacing
⟨cos θ⟩ ≈ exp(−⟨θ²⟩/2)  ≈  (L/a)^(−T/4πJ)                    [T]
```

The fluctuations of the angle grow logarithmically with the size of the system, so the magnetization falls as a power of L and vanishes in an infinite system at any T > 0, though only slowly. In three dimensions the corresponding integral of 1/k² converges at small k, the fluctuations stay finite and order survives [T]. Coleman's argument rests on the same integral: the propagator of a massless scalar in two dimensions diverges logarithmically at long wavelengths [T].

This decay law is the "spin-wave" estimate the toy-model note compares its lattice data with, written as a ratio between two lattice sizes: "(64/16)^{−T/4πJ} = 0.936" for the run at T = 0.6 (toy-model note §4). The round-4 referee checked the closed form against a direct lattice sum: "lattice Gaussian sum gives M(64)/M(16) = 0.9359 vs closed form (64/16)^(-T/4piJ) = 0.9360" (audit notes, Step 2(c)).

The absence of true order does not mean disorder. At low temperature the two-dimensional XY model has quasi-long-range order, with correlations that decay as a power of distance rather than exponentially, and a transition to the disordered phase driven by the unbinding of vortices, the Berezinskii–Kosterlitz–Thouless (BKT) transition [T]. The note's potential-free lattice run, below, shows the magnetization's slow fall with system size.

## What the theorem does not rule out

- **Discrete symmetries.** In the two-dimensional Ising model, reversing a domain of spins costs energy proportional to the length of its boundary, so large reversed domains are suppressed and the model orders below a nonzero temperature [T]. The worklog: "In 1+1, a discrete symmetry can break (as in the 2D Ising model)." (criterion S4).
- **Symmetry-breaking fields.** A term that depends on the angle itself, such as −h cos 2θ, removes the continuous symmetry and leaves a discrete one, which can order. The toy-model note cites José, Kadanoff, Kirkpatrick and Nelson [17] for symmetry-breaking fields in the planar model as background only: "the ordered phase used here is established by our own Monte Carlo, not by appeal to this reference". The round-4 referee found that the paper's abstract treats hexagonal and cubic fields, with "no mention of the two-fold/Ising case", and could not check the full text (audit notes, Step 1).
- **Non-compact symmetries.** Sigma models whose target is a hyperbolic space, with a non-compact symmetry group SO(1,N), can break that symmetry even in two dimensions. The abstract of Duncan, Niedermaier and Seiler, as quoted by the round-4 referee: "(ii) the SO(1,N) symmetry is spontaneously broken. For D=2 this shows that the systems evade the Mermin-Wagner theorem." (audit notes, Step 1). The worklog had first posed the exception in terms of non-amenable groups, groups that admit no invariant way of averaging over their elements, unlike compact groups [T] ('Success criteria'). See [coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models).
- **Long-range interactions, and more dimensions.** The theorem assumes short-range interactions, and it constrains two dimensions or fewer [T].

## Tunnelling in 0+1 dimensions

Ordinary quantum mechanics, a field theory in 0+1 dimensions with finitely many degrees of freedom, cannot break even a discrete symmetry [T]. In a symmetric double-well potential the states localized in either well are not stationary, because tunnelling connects them. The ground state is their symmetric combination, unique and invariant, separated from the antisymmetric one by a small but nonzero splitting. A symmetry breaks only when the number of degrees of freedom is infinite and the tunnelling amplitude between the candidate vacua vanishes ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)).

The worklog applies this directly: "In 0+1 dimensions (quantum mechanics), tunnelling restores any symmetry, so the toy starts in 1+1." (criterion S4). The same consideration returns in the complex Grosse–Wulkenhaar model ([model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)), whose condensate occupies finitely many levels. There the polarization angle β "has no stiffness", and "Even a potential on β cannot rescue it. The order-parameter sector stays finite-dimensional, so the system tunnels between the two vacua. This last step is argued, not proven: integrating out the massive tower is assumed not to make the barrier grow with N." (worklog, 'Chunk 3 results'). The round-4 referee added that without a potential no tunnelling argument is needed: an exact symmetry makes every condensate phase a flat direction, so the vanishing of the [order parameter](/wiki/symmetry-breaking/order-parameter) "at any truncation follows from symmetry alone", and "The 'tunnelling' caveat is only needed for the add-a-potential variant." (audit notes, Step 2(c)). See [quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration).

## How the theorem shaped the toy models

### Criterion S4

The worklog fixed its quantum-stability test before building anything: "S4 — quantum stability. The breaking survives quantum fluctuations in the stated dimension." Its sub-points are the two limits above: tunnelling in 0+1, so "the toy starts in 1+1", and "In 1+1, a discrete symmetry can break (as in the 2D Ising model). A continuous compact one cannot (Coleman–Mermin–Wagner), though there is a claimed exception for non-amenable groups, to be checked." ('Success criteria'; [success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)). The prediction written alongside: "S4 will pass only for a discrete reduction (the symmetry group cut down to the group generated by ρ) or via the non-amenability exception. The continuous U(1) of phase-space rotations that contains ρ would be restored in 1+1." ('Predictions'). The worklog later scored it a hit: model I passed S4 only with a ρ-preserving potential (after round 4, a pass for the frozen-H reduction only; see below), the Grosse–Wulkenhaar route failed it outright, and the non-amenability route was "not needed, not tested" ('Assessment').

### Model I: the restriction to the compact SO(2)

Model I's symmetry group [Sp(2, ℝ)](/wiki/phase-space/reciprocity/symplectic-form) contains two kinds of directions. The rotations of the phase plane that leave H = 1 fixed form the compact group SO(2), and [ρ](/wiki/phase-space/reciprocity/born-reciprocity), a quarter turn, is one of them; they turn the vacuum K(φ) around its circle ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). The remaining directions move H through the [upper half-plane](/wiki/phase-space/modular-field/siegel-domain) and are non-compact.

The worklog first applied the theorem to the whole continuous breaking: "The breaking is continuous, so in 1+1 the compact circle mode should restore ⟨K⟩ (Coleman–Mermin–Wagner) unless the non-amenable directions change that." ('Chunk 1 results'). The note's first version stated that in the exactly symmetric model "the continuous breaking is forbidden" (as quoted in the referee's audit notes, Step 3). The round-4 referee objected that model I's H-sector is the hyperbolic sigma model for which Duncan, Niedermaier and Seiler report breaking in two dimensions, and the adjudication upheld the point as a literature ruling: "The model I H-sector is a hyperbolic SO(1,2) model, which by Duncan–Niedermaier–Seiler can break in 2D" — "The Mermin–Wagner statement must be restricted to the compact SO(2) containing ρ. Whether that SO(2) is broken in the coupled model is open." (`review/round4-adjudication.md`, "Mermin–Wagner vs [11]"; [11] is the hyperbolic-model reference in the note's first numbering, [15] in version 2). Revision 1 required the restriction, the citation for the hyperbolic H-sector and a note of the open question.

The note v2 states the result accordingly: "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ." and "The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur [15]. Whether ρ's SO(2) stays unbroken in the full coupled model is open." (§4). Its list of what is not shown includes "whether ρ's SO(2) breaks in the coupled model without a potential" (§6). See [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question).

### The lattice test

Since the compact angle cannot order on its own in 1+1, the note adds "a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group" (§4; [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). The simulated model keeps only the polarization angle, with H frozen at 1 ([the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction)):

```text
E = −J Σ cos(φ_i − φ_j) − h Σ cos 2φ_i                        (toy-model note §4)
```

"model I's polarization angle at H = 1, with V_b up to a constant and normalization. H is not simulated." With h = 0 this is the XY model above, with its continuous symmetry. With h > 0 a general shift of φ changes the energy, but the shift φ → φ + π does not, and that shift is how ρ acts on the angle (toy-model note §2). Runs used "Checkerboard Metropolis, cold start (φ = 0), L = 16, 32, 64. Means ± standard errors over four independent seeds. Order parameter for ρ: m = ⟨cos φ⟩." (§4):

| Run | Values at L = 16, 32, 64 | Reading |
|---|---|---|
| With the potential (J = h = 1), T = 0.6 | ⟨\|m\|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667 | Ordered ℤ₂ phase |
| Control, T = 3.0 | ⟨\|m\|⟩ = 0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004 | Scales as 1/L: disordered |
| No potential (h = 0), T = 0.6 | ⟨\|M\|⟩ = \|⟨e^{iφ}⟩\| = 0.8369 ± 0.0007, 0.8025 ± 0.0039, 0.7736 ± 0.0038; ratio 0.924 vs spin-wave (64/16)^{−T/4πJ} = 0.936 | No true order |

(toy-model note §4; reproduced by `verify/toy_s4.py`; [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo). On "± 0.0001 at every size", see flag 13 in `review/wiki-build-flags.md`.)

The three rows are the theorem and its exception seen on the lattice:

- **With the potential**, the symmetry left is discrete, and it breaks: the order parameter does not fall with size, and the Binder cumulant sits at the ordered-phase value ([the gate](/wiki/method/verification/the-gate)'s check reads "Binder cumulant near 2/3 (an ordered Z2 phase)").
- **The control** tests the method. Every run starts ordered, and at high temperature "the sampler does leave it when the phase is disordered" (worklog, 'Chunk 3 results'); a finite disordered lattice still shows a small |m|, which falls as 1/L [T].
- **Without the potential**, the U(1) magnetization falls with every doubling of L, as the spin-wave law requires, and the ratio between L = 64 and L = 16 is a little below the bare spin-wave value. The round-4 referee, whose own runs gave a ratio of 0.917, read such a shortfall as "as expected from stiffness renormalisation" (audit notes, Step 2(c)): at nonzero temperature the effective stiffness is smaller than J, so the decay is faster [T].

The ordered row belongs to the frozen-H reduction, not to model I with H dynamical; "a Monte Carlo of model I with H dynamical" is listed as not shown (§6). Two run details matter for the reading: "Hot starts at L = 64 coarsen slowly through metastable domains, so ordered-phase values are reported from cold starts." (§4), and the error bars come from four independent seeds, not from one fixed seed ([Monte Carlo error bars](/wiki/method/verification/monte-carlo-error-bars)).

## The program's dimension, 3+1

The worklog adds a remark about the program's own dimension: "In 3+1, the program's actual dimension, Coleman–Mermin–Wagner does not apply. There the self-dual coset model can break the continuous U(1) itself, with τ an exactly massless Goldstone. §10's τ has a potential, so the explicit breaking is in the program anyway." ('Chunk 3 results'). The first sentence is the theorem's scope: four Euclidean dimensions are more than two [T]. The rest is not computed anywhere in the record, and the note v2 covers only 1+1 with d = 1 ("anything beyond d = 1" is not shown, §6). The remark is recorded with its status on [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle#conjecture-continuous-breaking-in-31-dimensions).

## References

The toy-model note's references, as it gives them; the note marks none, and the round-4 referee found [13]–[15] and checked that they support the statements they are cited for (audit notes, Step 1, under the note's first numbering):

- [13] N. D. Mermin, H. Wagner, Phys. Rev. Lett. 17, 1133 (1966).
- [14] S. Coleman, "There are no Goldstone bosons in two dimensions," Commun. Math. Phys. 31, 259 (1973).
- [15] M. Niedermaier, E. Seiler, Ann. Henri Poincaré 6, 1025 (2005), hep-th/0312293; A. Duncan, M. Niedermaier, E. Seiler, "Vacuum orbit and spontaneous symmetry breaking in hyperbolic sigma models," Nucl. Phys. B 720, 235 (2005), erratum Nucl. Phys. B 758, 330 (2006), hep-th/0405163. Round 4 corrected the first author's initial to A. Duncan and added the erratum.
- [17] J. V. José, L. P. Kadanoff, S. Kirkpatrick, D. R. Nelson, "Renormalization, vortices, and symmetry-breaking perturbations in the two-dimensional planar model," Phys. Rev. B 16, 1217 (1977), cited as background only.

Added by the wiki from model memory (†):

- P. C. Hohenberg (1967)†: the theorem for superfluid and superconducting order.
- R. Peierls (1936)† and L. Onsager (1944)†: order in the two-dimensional Ising model.
- V. L. Berezinskii (1971)†; J. M. Kosterlitz and D. J. Thouless (1973)†: quasi-long-range order and the vortex-unbinding transition.

## Used by

- [The hard core](/wiki/program/hard-core) — in the toy, a definite polarization in 1+1 needs a potential.
- [P2′: only the symplectic form is rigid](/wiki/program/postulates/p2-prime) — the compact polarization angle cannot order in 1+1.
- [P5: the vacuum selects a polarization](/wiki/program/postulates/p5-spontaneous-selection) — in the toy, the selected angle cannot order by itself in 1+1.
- [Mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking) — "the magnet must point" only with a potential in 1+1.
- [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria) — why criterion S4 is posed in 1+1.
- [Acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion) — the ordered ℤ₂ phase that meets it.
- [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) — why a definite polarization needs a potential in 1+1, and the 3+1 remark.
- [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) — the potential that reduces the symmetry to a discrete group.
- [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality) — a spontaneous selection of the pair of lines placed in 3+1, where the theorem does not apply.
- [Model I vacua, the order parameter and the Goldstone spectrum](/wiki/symmetry-breaking/toy-models/coset-model/vacua) — the compact angle cannot order by itself.
- [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential) — why model I needed a potential at all.
- [The frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) — what the 1+1 result establishes.
- [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) — the h = 0 run as the theorem's lattice check.
- [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question) — the theorem's reach in model I.
- [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration) — a finite-dimensional order-parameter sector, as in 0+1.
- [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase) and [τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence) — the toy's polarization angle, τ's circle, cannot order in 1+1 without a potential.

## Sources

- `papers/reciprocity-toy-models.md` §1 — the statement and the hyperbolic exception; §4 — the restriction to the compact SO(2), the potential, the lattice model and the three runs; §6 — what is not shown; refs [13]–[15], [17]; §2 — the Euclidean Lagrangian and ρ's action on the angle
- `review/round4-adjudication.md` 'Rulings' (Mermin–Wagner vs [11]) — the restriction, upheld from the literature; 'Revisions' 1 — the revision that applied it
- `review/round4/referee/audit-notes.md` Step 1 — the references found and checked, the Duncan–Niedermaier–Seiler abstract, the limits of [17]; Step 2(c) — the spin-wave closed form against a lattice sum, the stiffness-renormalisation reading, the tunnelling caveat; Step 3 — the first version's wording
- `notes/toy-lagrangian.md` 'Success criteria', 'Predictions' — criterion S4 and its prediction; 'Chunk 1 results' — the theorem first applied to the whole breaking; 'Chunk 3 results' — the Grosse–Wulkenhaar restoration and the 3+1 remark; 'Assessment' — the prediction scored
- `verify/toy_s4.py` — the lattice runs with and without the potential, and the high-temperature control
