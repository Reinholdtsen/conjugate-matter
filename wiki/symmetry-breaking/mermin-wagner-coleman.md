---
title: "The Mermin–Wagner–Coleman theorem"
weight: 30
status: established
description: "No spontaneous breaking of a compact continuous symmetry in two dimensions, and none at all in 0+1 because of tunnelling: why the toy models start in 1+1 and what they can order."
provenance: [T]
sources:
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md refs [13]–[15]"
  - "review/round4-adjudication.md 'Rulings' (Mermin–Wagner vs [11])"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "verify/toy_s4.py"
---

*The Mermin–Wagner–Coleman theorem says that in two dimensions (one space and one time, or a two-dimensional system at nonzero temperature) a continuous symmetry of the compact kind, such as rotation through an angle, cannot be spontaneously broken: slow, long-wavelength wobbles of the would-be ordered direction grow without limit and wash the order out. Discrete symmetries escape the theorem, as the two-dimensional Ising magnet shows, and so do some non-compact symmetries. With only a few degrees of freedom (0+1 dimensions, ordinary quantum mechanics), not even a discrete symmetry breaks, because tunnelling mixes the would-be ground states. These limits decided how the program's toy models were built: they start in 1+1 dimensions, and their compact polarization angle can order only after a potential reduces its symmetry to a discrete one.*

**Status:** Established — [T] — Mermin and Wagner [13] and Coleman [14] as cited in the toy-model note; its scope in the toy models was fixed by the round-4 ruling that restricts it to the compact SO(2) containing ρ (`review/round4-adjudication.md`).

## Key facts

- **The theorem [T].** Mermin and Wagner (Phys. Rev. Lett. 17, 1133 (1966)) showed that isotropic spin models with short-range interactions in one or two dimensions have no spontaneous magnetization at nonzero temperature; Coleman's field-theory version is titled "There are no Goldstone bosons in two dimensions" (Commun. Math. Phys. 31, 259 (1973)). In two dimensions the fluctuations of a would-be [Goldstone mode](/wiki/symmetry-breaking/goldstone-and-higgs) diverge logarithmically at long wavelengths and destroy the order.
- **As the toy-model note states it.** "Continuous compact symmetries cannot break spontaneously in two dimensions [13, 14]. Non-compact hyperbolic models are an exception [15]." (§1; see [Coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models)).
- **Why the toys start in 1+1.** Criterion S4: "In 0+1 dimensions (quantum mechanics), tunnelling restores any symmetry, so the toy starts in 1+1. In 1+1, a discrete symmetry can break (as in the 2D Ising model). A continuous compact one cannot (Coleman–Mermin–Wagner)" (worklog, 'Success criteria'; [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)).
- **Restricted to the compact SO(2) (round 4).** The referee found that model I's H-sector "is a hyperbolic SO(1,2) model, which by Duncan–Niedermaier–Seiler can break in 2D"; the ruling, upheld: "The Mermin–Wagner statement must be restricted to the compact SO(2) containing ρ. Whether that SO(2) is broken in the coupled model is open." The note v2: "In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ." (§4; [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).
- **The lattice control without a potential.** In the frozen-H reduction with no potential (h = 0, T = 0.6), ⟨|M|⟩ = 0.8369 ± 0.0007, 0.8025 ± 0.0039, 0.7736 ± 0.0038 at L = 16, 32, 64; "ratio 0.924 vs spin-wave (64/16)^{−T/4πJ} = 0.936"; reading: "No true order" (toy-model note §4; `verify/toy_s4.py`; [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)).
- **With the potential, a discrete symmetry orders.** With the ρ-preserving potential (J = h = 1, T = 0.6): "⟨|m|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667", read as an "Ordered ℤ₂ phase" (§4) of [the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction), not of model I with H dynamical.
- **In 3+1 (worklog only, uncomputed).** "In 3+1, the program's actual dimension, Coleman–Mermin–Wagner does not apply." (worklog, 'Chunk 3 results'). The note v2 covers only 1+1 with d = 1; see [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).

## Used by

- [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria) — why criterion S4 is posed in 1+1.
- [The polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) — why a definite polarization needs a potential in 1+1, and the 3+1 remark.
- [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) — the potential that reduces the symmetry to a discrete group.
- [The frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction) — what the 1+1 result establishes.
- [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo) — the h = 0 run as the theorem's lattice check.
- [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question) — the theorem's reach in model I.

## Sources

- `papers/reciprocity-toy-models.md` §1, §4, refs [13]–[15] — the statement, its restriction to the compact SO(2), the hyperbolic exception, the Monte Carlo
- `review/round4-adjudication.md` 'Rulings' (Mermin–Wagner vs [11]) — the restriction, upheld from the literature
- `notes/toy-lagrangian.md` 'Success criteria' — tunnelling in 0+1; the 2D Ising contrast
- `notes/toy-lagrangian.md` 'Chunk 3 results' — the 3+1 remark
- `verify/toy_s4.py` — the lattice runs with and without the potential
