---
title: "The Fourier transform as a phase-space rotation"
weight: 30
status: established
description: "The unitary map between position and momentum representations implements ρ (F² is parity); the waveform–spectrum picture and the time–bandwidth product."
sources:
  - "papers/broken-born-checkpoint-v2.md §3"
  - "popsci/universes-other-half.md 'Two descriptions of one thing'"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §3"
  - "notes/broken-born-theory.md §2"
  - "review/round4/referee/out_sec5_fix.txt line 1"
  - "HANDOFF.md §4"
  - "papers/broken-born-checkpoint-v2.md Appendix A"
---

*The Fourier transform is the exact, reversible map that turns a quantum state's description in position into its description in momentum — the same operation that turns a sound's waveform into its spectrum. Neither description approximates the other; each contains the whole state. Applied once, the transform carries out [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), the quarter-turn ρ: (x, p) → (p, −x) of phase space; applied twice, it reflects x → −x. The program takes the analogy literally: position and momentum are two descriptions of one state, and its toy models use the transform to relate a vacuum that is sharp in position to its image that is sharp in momentum.*

**Status:** Established — standard mathematics [T]; #11 §3 cites Born for its role [1†, 2†] — the parity property F²ψ(x) = ψ(−x) was checked numerically by the round-4 referee, and the toy-model uses are machine-checked in `verify/toy_s5.py` and `verify/toy_gw.py` (see [the toy-model scripts](/wiki/method/verification/toy-model-scripts)).

## Key facts

- **It implements ρ.** #11 §3: "Quantum kinematics is exactly invariant under ρ: (x,p) → (p,−x); the Fourier transform implements it unitarily [1†, 2†]."
- **Twice is parity.** F²ψ(x) = ψ(−x) [T], matching ρ²: (x, p) → (−x, −p) (#1 §2). The round-4 referee checked it on the toy note's test state with a direct discrete transform: `max|F^2 psi(x) - psi(-x)| = 3.6082248765060084e-14` (`review/round4/referee/out_sec5_fix.txt`).
- **Waveform and spectrum.** The popular article #12 puts it this way: "Every sound admits two complete descriptions"; position and momentum descriptions "are two complete readings of one underlying state, related by the same Fourier transform that relates a waveform to its spectrum." The program's version is [the conjugate universe](/wiki/program/conjugate-universe): one state, two descriptions (#11 Appendix A, supposition 2).
- **Time–bandwidth product.** In signal analysis the same Fourier pair sets a trade-off: a signal cannot be both short in time and narrow in frequency [T]. This is the classical counterpart of [the uncertainty principle](/wiki/phase-space/reciprocity/canonical-commutator). `HANDOFF.md` §4 records a chat-only conjecture that applies it to the universe as a whole, a "cosmic time–bandwidth theorem" — see [the phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter).
- **In the matter coupling.** The toy note's coupling I_K is ∫|ψ(x)|⁴ dx in one vacuum and ∫|ψ̃(p)|⁴ dp in the other, with ψ̃ the transform of ψ, and "The combined map (ψ → Fψ, K → −K) leaves I invariant" (§5) — see [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling).
- **In model II.** The Langmann–Szabo duality is a Fourier transform on the noncommutative plane, D f(x) = (πθ)⁻¹ ∫ d²y e^{−i x̃·y} f(y), and on the matrix base it is parity: D f_mn = (−1)^m f_mn (toy-model note §3) — see [the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma).

## Used by

- [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) — the two vacua are related by ψ → Fψ together with K → −K.
- [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma) — the Langmann–Szabo transform computed by direct Fourier integration.
- [The conjugate universe: one state, two descriptions](/wiki/program/conjugate-universe) — the momentum description of the one physical state.
- [The phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter) — the time–bandwidth analogy at cosmic scale.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3 — the Fourier transform implements ρ unitarily [1†, 2†].
- `papers/broken-born-checkpoint-v2.md` Appendix A — supposition 2, one state with two descriptions.
- `papers/reciprocity-toy-models.md` §3, §5 — the Langmann–Szabo transform on the matrix base; the combined map (ψ → Fψ, K → −K).
- `notes/broken-born-theory.md` §2 — ρ² as the parity (x, p) → (−x, −p).
- `review/round4/referee/out_sec5_fix.txt` — the referee's numerical check of F²ψ(x) = ψ(−x).
- `HANDOFF.md` §4 — the chat-only "cosmic time–bandwidth theorem".
- `popsci/universes-other-half.md` "Two descriptions of one thing" — the waveform–spectrum framing (popular article; never a status source).
