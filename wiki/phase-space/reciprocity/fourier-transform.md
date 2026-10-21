---
title: "The Fourier transform as a phase-space rotation"
weight: 30
status: established
description: "The unitary map between position and momentum representations implements ρ (F² is parity); the waveform–spectrum picture and the time–bandwidth product."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md Appendix A"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §5"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §2"
  - "verify/toy_s5.py"
  - "verify/toy_gw.py"
  - "review/round4/referee/out_sec5_fix.txt line 1"
  - "review/round4/referee/audit-notes.md Step 2(d)"
  - "HANDOFF.md §4"
  - "popsci/universes-other-half.md 'Two descriptions of one thing'"
---

*The Fourier transform is the exact, reversible map that turns a quantum state's description in position into its description in momentum — the same operation that turns a sound's waveform into its spectrum. Neither description approximates the other; each contains the whole state. Applied once, the transform carries out [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), the quarter-turn ρ: (x, p) → (p, −x) of phase space; applied twice, it reflects x → −x; applied four times, it returns every state unchanged. The program takes the analogy literally: position and momentum are two descriptions of one state, and its [toy models](/wiki/symmetry-breaking/toy-models) use the transform to relate a vacuum in which a matter coupling is local in position to its mirror image, in which the coupling is local in momentum.*

**Status:** Established — standard mathematics [T]; [#11](/wiki/history/documents/checkpoint) §3 cites Born for its role [1†, 2†] — the parity property F²ψ(x) = ψ(−x) was checked numerically by the referee of [review round 4](/wiki/method/review/round-4), and the toy-model uses are machine-checked [V] in `verify/toy_s5.py` and `verify/toy_gw.py` (see [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Definition

With ℏ = 1, as the toy-model checks set it, the momentum wavefunction ψ̃(p) and the position wavefunction ψ(x) are related by

```text
ψ̃(p) = (2π)^(−1/2) ∫ ψ(x) e^(−ipx) dx
ψ(x)  = (2π)^(−1/2) ∫ ψ̃(p) e^(+ipx) dp
```

[T]. `verify/toy_s5.py` writes the first line as "(2 pi)^-1/2 int psi(x) e^{-ipx} dx". With ℏ restored, px becomes px/ℏ and 2π becomes 2πℏ [T]. Each e^{ipx} is a plane wave of wavenumber p, and ψ̃(p) is its amplitude in the state.

The transform is unitary: it preserves the norm, ∫|ψ̃(p)|² dp = ∫|ψ(x)|² dx (the Parseval–Plancherel theorem), and inner products [T]. Every probability computed in one description is the same in the other, and no information is lost in either direction. The toy-model gate opens its matter-coupling checks with exactly this test: "Fourier pair is consistent (Parseval)".

## Why it is a rotation of phase space

Conjugating the position and momentum operators by the transform F exchanges them, with the sign of ρ [T]:

```text
F† x̂ F = p̂          F† p̂ F = −x̂
```

Here † is the Hermitian adjoint. F therefore implements ρ: (x, p) → (p, −x) on the operators of quantum kinematics, and it leaves [x̂, p̂] = iℏ unchanged ([the canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator)). In #11's words: "Quantum kinematics is exactly invariant under ρ: (x,p) → (p,−x); the Fourier transform implements it unitarily [1†, 2†]" (§3).

Two standard facts make the word "rotation" literal [T]:

- **The oscillator picture.** The harmonic-oscillator eigenstates |n⟩ (the Hermite functions) are eigenfunctions of F, with eigenvalues (−i)ⁿ. So F = e^{−iπN/2}, where N is the oscillator's number operator. Evolution under the oscillator Hamiltonian (x² + p²)/2 rotates phase space rigidly at unit rate, and a quarter of its period is, up to a constant phase, the Fourier transform. Replacing the angle π/2 by any angle α gives the fractional Fourier transforms e^{−iαN}, a continuous circle of phase-space rotations of which F is the quarter-turn.
- **The phase-space portrait.** The [Wigner function](/wiki/phase-space/reciprocity/wigner-function) draws a state on phase space, and under these operations it rotates rigidly. `verify/toy_s5.py` builds the transformed state's Wigner function exactly this way: "W_{F psi}(x, p) = W_psi(-p, x): rotation of the phase plane".

One consequence is that some states are their own transforms: the oscillator ground state, a Gaussian, has eigenvalue 1 [T]. A test of whether the two descriptions give different physics needs a state whose momentum profile differs from its position profile; the toy-model check uses "a non-self-dual state (two displaced squeezed Gaussians)" (`verify/toy_s5.py`).

## Twice is parity

Applying the transform twice reflects the wavefunction, and four times restores it [T]:

```text
F² ψ(x) = ψ(−x)          F⁴ = 1
```

This matches ρ² = −1, the phase-space parity (x, p) → (−x, −p) (#1 §2), and ρ⁴ = 1. The [lab notebook](/wiki/history/documents/lab-notebook) calls the group of the four powers of ρ "the ℤ₄ generated by the complex structure I" (#1 P3).

The round-4 referee checked the parity property numerically, on the toy note's test state, with a direct discrete transform: `max|F^2 psi(x) - psi(-x)| = 3.6082248765060084e-14` (`review/round4/referee/out_sec5_fix.txt`). The check came out of a debugging episode. The referee's first attempt at the toy note's combined map gave 23.27. The referee traced this to a normalization bug in its own fast-transform code, not an error in the manuscript, and replaced that code with a direct discrete transform; the corrected transform passed the parity test and reproduced the note's number (audit notes, Step 2(d)).

## Waveform and spectrum

Signal analysis uses the same pair. A sound recorded as pressure against time and as amplitude against frequency gives two complete descriptions, related by the Fourier transform [T]. The [popular article](/wiki/history/documents/popular-articles) #12 opens on this: "Every sound admits two complete descriptions", and position and momentum descriptions "are two complete readings of one underlying state, related by the same Fourier transform that relates a waveform to its spectrum" (#12, "Two descriptions of one thing"; a popular article, never a status source).

The program's version is [the conjugate universe](/wiki/program/conjugate-universe): founding supposition 2, "A coexisting conjugate universe", is "alive, transformed" into one state with two descriptions (#11 Appendix A, supposition 2).

### The time–bandwidth product

The Fourier pair sets a trade-off: a signal cannot be both short in time and narrow in frequency. For root-mean-square widths, the product of duration and angular bandwidth obeys the same inequality as position and momentum, Δx · Δp ≥ ℏ/2, with ℏ set to 1 [T]. The [uncertainty principle](/wiki/phase-space/reciprocity/canonical-commutator) is this trade-off applied to the wavefunction.

`HANDOFF.md` §4 ([the handoff document](/wiki/history/documents/handoff)) lists, among results that exist only in the old chat, a "Phase-space diameter relation: D_x · D_p = h · N^(1/3) per dimension (cosmic time–bandwidth theorem)", which it calls "Conjecture-tier; candidate for a future note". It applies the trade-off to the universe as a whole; it is chat-only and has no derivation in any document. See [the phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter).

## In the toy models

### Model I: the matter coupling

The toy-model note couples matter to the vacuum of [model I](/wiki/symmetry-breaking/toy-models/coset-model) through a functional of a state's Wigner function, I[W] = ∫_{L+} du (∫_{L−} dv W)², where L± are the two eigenlines of the real structure K ([the order parameter](/wiki/symmetry-breaking/order-parameter)). At H = 1 it is ∫|ψ(x)|⁴ dx in the vacuum +K_ref and ∫|ψ̃(p)|⁴ dp in −K_ref, where ψ̃ is the transform of ψ (§5). For the note's test state the two vacua give 0.4070 and 0.3600 (§5).

The transform and the vacuum flip act together: "The combined map (ψ → Fψ, K → −K) leaves I invariant" (§5). The gate checks it as "rho-covariance: I_{-K}[W_{F psi}] = I_{+K}[W_psi]", and the round-4 referee reproduced it independently: "combined map: I_-K[F psi] = int |F(F psi)|^4 = 0.406972" against I_{+K}[ψ] = 0.406972 (`review/round4/referee/out_sec5_fix.txt`). See [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).

### Model II: the Langmann–Szabo duality

In [the self-dual Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar), the position–momentum duality of Langmann and Szabo is itself a Fourier transform, taken on the noncommutative (Moyal) plane, whose two coordinates do not commute: [x₁, x₂] = iθ, with θ = 1 (toy-model note §3). The note implements

```text
D f(x) = (πθ)⁻¹ ∫ d²y e^(−i x̃·y) f(y)          x̃ = 2θ⁻¹x
```

"by direct numerical integration", and finds "D f_mn = (−1)^m f_mn for m, n < 4, to ≲ 10⁻¹¹. The opposite sign of the exponent gives (−1)^n." On the matrix base f_mn the transform is therefore parity acting on one index. The gate prints a maximum deviation of 1.4e-12 for this check, against an asserted tolerance of 1e-7 (`verify/toy_gw.py`). See [the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) and [noncommutative field theory and the Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory).

## Standard references

Added by the wiki from model memory (†); the program's documents do not cite them.

- D. Gabor (1946)†: the time–frequency uncertainty relation of signal analysis.
- V. Namias (1980)†: the fractional Fourier transform and its use in quantum mechanics.

## Used by

- [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) — the two vacua are related by ψ → Fψ together with K → −K.
- [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) — the Langmann–Szabo transform computed by direct Fourier integration.
- [The conjugate universe: one state, two descriptions](/wiki/program/conjugate-universe) — the momentum description of the one physical state.
- [Born's question](/wiki/program/borns-question) and [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking) — both start from #11 §3's statement that the transform implements ρ.
- [The phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter) — the time–bandwidth analogy at cosmic scale.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — the Fourier transform implements ρ unitarily [1†, 2†].
- `papers/broken-born-checkpoint-v2.md` Appendix A — supposition 2, one state with two descriptions.
- `papers/reciprocity-toy-models.md` §3, §5 — the Langmann–Szabo transform on the matrix base; the coupling I and the combined map (ψ → Fψ, K → −K).
- `verify/toy_s5.py` — the transform's convention, the Parseval check, the rotation of the Wigner function, the non-self-dual test state.
- `verify/toy_gw.py` — D f_mn = (−1)^m f_mn and its tolerance.
- `review/round4/referee/out_sec5_fix.txt` — the referee's numerical check of F²ψ(x) = ψ(−x) and of the combined map.
- `review/round4/referee/audit-notes.md` Step 2(d) — the referee's normalization episode.
- `HANDOFF.md` §4 — the chat-only "cosmic time–bandwidth theorem".
- `notes/broken-born-theory.md` §1, §2 — P3's ℤ₄; ρ² as the parity (x, p) → (−x, −p).
- `popsci/universes-other-half.md` "Two descriptions of one thing" — the waveform–spectrum framing (popular article; never a status source).
