---
title: "The Wigner function and Weyl symbols"
weight: 70
status: established
description: "Phase-space representations of quantum states: the Wigner function, its marginals, Royer's parity-operator form and ∫W² = 1/2π, as the toy-model checks use them."
provenance: [T]
sources:
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md ref [16]"
  - "verify/toy_s5.py"
  - "verify/toy_gw.py"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/audit-notes.md Step 2(d)"
  - "review/round4/referee/out_sec5.txt"
  - "review/round4/referee/out_sec5_fix.txt"
  - "review/round4-adjudication.md F5"
  - "review/round4-adjudication.md 'Revisions for v2 of the note'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "notes/toy-lagrangian.md 'Write-up and review (2026-10-19/20)'"
---

*The Wigner function is a way of drawing a quantum state as a distribution over phase space, with position on one axis and momentum on the other. Adding it up over all momenta gives the probability of each position, and adding it up over all positions gives the probability of each momentum, so one picture holds both descriptions of the state; unlike a true probability, it can be negative. Weyl symbols extend the same idea from states to operators, turning each operator into a function on phase space. The program's toy-model note uses the Wigner function to build a matter coupling that reads one axis of phase space as "position", and to check that a coupling blind to that choice treats both axes alike.*

**Status:** Established — standard quantum mechanics [T]; Royer's parity-operator paper is the toy note's ref. [16] — the marginals and ∫W² = 1/2π are machine-checked [V] in `verify/toy_s5.py` as anchors for the toy computation, and the round-4 referee reproduced them independently (see [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Definition

For a pure state ψ in one dimension, with ℏ = 1, the Wigner function is

```text
W(x, p) = (1/π) ∫ ψ*(x + y) ψ(x − y) e^(2ipy) dy
```

This is the form `verify/toy_s5.py` implements ("W(x, p) = (1/pi) int psi*(x+y) psi(x-y) e^{2ipy} dy"); with ℏ restored, 1/π becomes 1/(πℏ) and the exponent becomes 2ipy/ℏ [T] (Wigner 1932†). The integrand compares the wavefunction at two points placed symmetrically about x, and the Fourier transform over their separation 2y reads off the momentum content at x. W is real, and its integral over all of phase space is 1 [T]; the round-4 referee found "int W = 1.0000" for the toy note's test state (audit notes, Step 2(d)).

## Marginals: both descriptions in one picture

Integrating out either variable leaves the probability distribution of the other [T]:

```text
∫ W(x, p) dp = |ψ(x)|²          ∫ W(x, p) dx = |ψ̃(p)|²
```

where ψ̃ is the momentum wavefunction, the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of ψ. Both pass in the gate: "Wigner marginal over p is |psi(x)|^2" and "Wigner marginal over x is |psi~(p)|^2" (`verify/toy_s5.py`). More generally, integrating W along all the lines parallel to a chosen direction gives the probability distribution of the coordinate measured across those lines, a rotated position [T]. The position and momentum descriptions are two of these projections of one function.

### Not a probability

W can be negative [T], so it is a quasi-probability distribution: its marginals are probabilities, but W itself is not. Negative regions mark interference, the features of a quantum state that no classical distribution over (x, p) reproduces.

### How it moves under ρ

When a linear symplectic map S of phase space is carried out on states by its unitary operator, the state's Wigner function is carried along by the map, W(z) → W(S⁻¹z) [T]; for a rotation it turns rigidly, and for a squeeze it stretches one way and shrinks the other, keeping its area. For the quarter-turn [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), carried out on states by the Fourier transform, the toy-model script builds the transformed Wigner function this way: "W_{F psi}(x, p) = W_psi(-p, x): rotation of the phase plane" (`verify/toy_s5.py`).

## ∫W² = 1/2π: a quantity blind to the axes

For any pure state, with ℏ = 1,

```text
∫∫ W(x, p)² dx dp = 1/2π
```

[T]; with ℏ restored it is 1/(2πℏ). It is a special case of Moyal's identity: the overlap ∫∫ W_ψ W_φ dx dp equals |⟨ψ|φ⟩|²/(2πℏ) [T]. Because the integral of W² does not change when W is rotated or squeezed, it cannot tell which axis is position.

That makes it the toy's control. The worklog: "The K-blind interaction ∫W² (= 1/2π for pure states) shows no asymmetry" between the two vacua (`notes/toy-lagrangian.md`, chunk 4). The gate's check reads "a K-blind phase-space interaction int W^2 (= 1/(2 pi) for pure states) shows no asymmetry", and the round-4 referee reproduced "int W = 1.0000, int W^2 = 0.1591549431 = 1/2pi" (audit notes, Step 2(d); the output file `review/round4/referee/out_sec5.txt` prints more digits).

## The coupling built on it

The toy-model note's matter coupling is a functional of the Wigner function that does depend on the axes. Its definition, with L+ and L− the two eigenlines of the real structure K (the program's polarization, [Lagrangian subspaces and polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)):

```text
I[W] = ∫_{L+} du ( ∫_{L−} dv W )²
```

The inner integral, along L−, gives the marginal distribution of the coordinate u along L+; the outer integral squares that distribution and adds it up.

- **In the two vacua.** "At H = 1, in the vacuum +K_ref it is ∫|ψ(x)|⁴ dx (local in x); in −K_ref it is ∫|ψ̃(p)|⁴ dp." (toy-model note §5). ∫|ψ(x)|⁴ dx has the form that a contact interaction, one acting only when two particles are at the same point, takes in a mean-field treatment [T], which is one way to read "local in x".
- **The numbers.** "For ψ ∝ e^{−(x−1.3)²/0.7} + 0.6 e^{−(x+1.3)²/0.7}, the two vacua give 0.4070 and 0.3600." (§5). The referee reproduced them, from the wavefunction directly and from the Wigner marginals, as 0.406972 and 0.360047 (`review/round4/referee/out_sec5.txt`).
- **Odd in K.** "**I is odd in K**, so it breaks the K → −K symmetry and makes the breaking of ρ physical (§2)." Flipping K alone changes it: "K->-K alone: I_-K[psi] - I_+K[psi] = -0.046925" (`review/round4/referee/out_sec5_fix.txt`). The combined map (ψ → Fψ, K → −K) leaves it invariant (§5).
- **It needs H.** "I[W] = ∫_{L+} du (∫_{L−} dv W)² of a state's Wigner function needs H as well as K: rescaling the coordinate along L+ by 2 doubles it. It is covariant under the SO(2) fixing H = 1, not under Sp(2,ℝ)." (§5). The round-4 adjudication upheld this as finding F5 ("rescaling the eigenline coordinate by 2 doubles I (0.407 → 0.814)"); the gate prints "0.4070 -> 0.8139". Earlier wordings called the coupling "ρ-covariant" or "K-covariant"; v2 calls it (H, K)-built.
- **What "locality" means here.** The referee's caveat: "'Locality' here is a quartic functional of a one-particle state, not an interacting field theory; the Yukawa analogy is heuristic." (audit notes, Step 2(d)).

See [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).

## Weyl symbols

The Weyl correspondence assigns to each operator Â a function A(x, p) on phase space, its Weyl symbol [T] (Weyl 1927†). The expectation value of Â in a state is the phase-space average of its symbol, weighted by the state's Wigner function, ⟨Â⟩ = ∫∫ A(x, p) W(x, p) dx dp; the Wigner function is itself, up to a constant factor, the Weyl symbol of the state's density operator |ψ⟩⟨ψ| [T]. Operator products become the Moyal (star) product of symbols [T] (Groenewold 1946†, Moyal 1949†).

### The Moyal plane and model II

Model II, the self-dual Grosse–Wulkenhaar model, lives on a noncommutative plane whose two coordinates obey [x₁, x₂] = iθ with θ = 1 (toy-model note §3). The plane is a phase space with θ in the role of ℏ, and its fields are functions multiplied with the star product [T]. The note's basis of functions is the matrix base f_mn, with f₀₀ = 2e^{−x²/θ} and f_mn ⋆ f_kl = δ_nk f_ml (§3). These functions are the Weyl symbols of the oscillator operators |m⟩⟨n| [T]. The round-4 referee checked the note's explicit Laguerre form of f_mn against the "Weyl symbol of |m><n|", built independently from the quantum-mechanical oscillator states: "max error 5.63e-14 (m,n<=3)" (audit notes, Step 2(b)). See [model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base).

## Royer's parity form

A. Royer showed that the Wigner function at a phase-space point is an expectation value of a parity operator, the reflection x → −x, p → −p moved so that it reflects about that point [T]: "Wigner function as the expectation value of a parity operator," Phys. Rev. A 15, 449 (1977) (the toy note's ref. [16]). The definition above shows the simplest case. At the origin, W(0, 0) = (1/π) ∫ ψ\*(y) ψ(−y) dy, which is 1/π times the expectation value of the parity operator. A state odd under x → −x therefore has a negative Wigner function at the origin [T].

The toy note uses the parity form to read its lemma on the matrix base. On the base f_mn, the Langmann–Szabo duality acts as D f_mn = (−1)^m f_mn: "parity acting on the left index for one factor and on the right for the next. That is the alternation of [6], and is consistent with the parity-operator form of Weyl symbols [16]." (§3). The credit came from round 4. The referee noted that the explicit parity form follows from the parity-operator representation of Weyl symbols (Royer 1977, which it confirmed exists) and called the lemma "Correct, but not a new structural fact" (audit notes, Step 2(b)). The adjudication's revision 3 asked v2 to present the result as a lemma, "crediting Grosse–Wulkenhaar (manifest in the matrix base), Royer (the parity form) and Langmann–Szabo (the complex formulation)". The worklog records the five references added in v2, Royer's among them, as "all retrieved". See [the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma).

## Standard references

Added by the wiki from model memory (†), except Royer, which the toy note cites as retrieved.

- E. Wigner (1932)†: the Wigner function.
- H. Weyl (1927)†: the Weyl correspondence between operators and phase-space functions.
- H. J. Groenewold (1946)† and J. E. Moyal (1949)†: the star product and phase-space quantum mechanics.
- A. Royer, Phys. Rev. A 15, 449 (1977): the parity-operator form (toy note ref. [16]).

## Used by

- [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) — the coupling I is a functional of the Wigner function.
- [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) — parity on Weyl symbols, credited to Royer.
- [Model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base) — the matrix base of Weyl symbols.
- [The twisted element ρ∘(K → −K)](/wiki/symmetry-breaking/twisted-element) — the K-odd coupling that makes breaking ρ physical.

## Sources

- `papers/reciprocity-toy-models.md` §5 — the coupling I[W], its values in the two vacua, its dependence on H, the K-blind control.
- `papers/reciprocity-toy-models.md` §3 and ref. [16] — the matrix base; the parity-operator form of Weyl symbols (Royer).
- `review/round4-adjudication.md` F5, "Revisions for v2 of the note" — the coupling needs H; the credit to Royer.
- `verify/toy_s5.py` — the Wigner function as implemented, the marginal checks, ∫W² = 1/(2π), the rotation under ρ.
- `verify/toy_gw.py` — the matrix-base functions and the duality as parity.
- `review/round4/referee/audit-notes.md` Step 2(b), Step 2(d) — independent checks of the Weyl symbols, ∫W and ∫W², the coupling's values; the referee's caveat on "locality"; Royer's paper.
- `review/round4/referee/out_sec5.txt`, `review/round4/referee/out_sec5_fix.txt` — the referee's printed values.
- `notes/toy-lagrangian.md` chunk 4, "Write-up and review" — ∫W² = 1/2π as the K-blind control; the v2 references "all retrieved".
