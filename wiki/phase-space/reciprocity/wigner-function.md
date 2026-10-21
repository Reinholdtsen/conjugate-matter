---
title: "The Wigner function and Weyl symbols"
weight: 70
status: established
description: "Phase-space representations of quantum states: the Wigner function, its marginals, Royer's parity-operator form and ∫W² = 1/2π, as the toy-model checks use them."
sources:
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md ref [16]"
  - "verify/toy_s5.py"
  - "verify/toy_gw.py"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/audit-notes.md Step 2(d)"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
---

*The Wigner function is a way of drawing a quantum state as a distribution over phase space, with position on one axis and momentum on the other. Adding it up over all momenta gives the probability of each position, and adding it up over all positions gives the probability of each momentum, so one picture holds both descriptions of the state; unlike a true probability it can be negative. Weyl symbols extend the same idea from states to operators. The program uses the Wigner function in its toy-model note to build a matter coupling that reads one axis of phase space as "position", and to check that a coupling blind to that choice treats both axes alike.*

**Status:** Established — standard quantum mechanics [T]; Royer's parity-operator paper is the toy note's ref. [16] — the marginals and ∫W² = 1/2π are checked numerically in `verify/toy_s5.py` as anchors for the toy computation, and the round-4 referee reproduced them independently (see [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Key facts

- **Definition.** As `verify/toy_s5.py` implements it, with ℏ = 1:

  ```text
  W(x, p) = (1/π) ∫ ψ*(x+y) ψ(x−y) e^{2ipy} dy
  ```

- **Marginals [T].** Integrating W over p gives |ψ(x)|², and over x gives |ψ̃(p)|², the squared momentum wavefunction; both pass in the gate (`Wigner marginal over p is |psi(x)|^2`, `Wigner marginal over x is |psi~(p)|^2`). The [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) relates ψ and ψ̃.
- **∫W² = 1/2π for a pure state [T].** The worklog uses it as the K-blind control: "The K-blind interaction ∫W² (= 1/2π for pure states) shows no asymmetry" between the two vacua (`notes/toy-lagrangian.md`, chunk 4). The round-4 referee reproduced `int W = 1.0000, int W^2 = 0.1591549431 = 1/2pi`.
- **The coupling built on it.** Toy-model note §5: "I[W] = ∫_{L+} du (∫_{L−} dv W)² of a state's Wigner function needs H as well as K", and at H = 1 it is ∫|ψ(x)|⁴ dx in the vacuum +K_ref and ∫|ψ̃(p)|⁴ dp in −K_ref. For the note's test state the two vacua give 0.4070 and 0.3600. See [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).
- **Royer's parity form.** A. Royer, "Wigner function as the expectation value of a parity operator," Phys. Rev. A 15, 449 (1977) (toy-model note ref. [16]). The note calls the matrix-base form of the Langmann–Szabo duality "consistent with the parity-operator form of Weyl symbols [16]" (§3); round 4 asked for the credit and confirmed the paper exists. See [the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma).
- **Weyl symbols in model II.** The functions f_mn of the Moyal-plane matrix base are Weyl symbols of oscillator operators; the round-4 referee checked the Laguerre form of f_mn against the Weyl symbol of the oscillator operator |m⟩⟨n|, built independently, to a maximum error of 5.63e-14 for m, n ≤ 3 — see [model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base).

## Used by

- [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) — the coupling I_K is a functional of the Wigner function.
- [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) — parity on Weyl symbols, credited to Royer.
- [Model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base) — the matrix base of Weyl symbols.

## Sources

- `papers/reciprocity-toy-models.md` §5 — the coupling I[W], its values in the two vacua, the K-blind control.
- `papers/reciprocity-toy-models.md` §3 and ref. [16] — the parity-operator form of Weyl symbols (Royer).
- `verify/toy_s5.py` — the Wigner function as implemented, the marginal checks, ∫W² = 1/(2π).
- `verify/toy_gw.py` — the matrix-base functions and the duality as parity.
- `review/round4/referee/audit-notes.md` Step 2(b), Step 2(d) — independent checks of the Weyl symbols, ∫W and ∫W², and Royer's paper.
- `notes/toy-lagrangian.md` chunk 4 — ∫W² = 1/2π as the K-blind control.
