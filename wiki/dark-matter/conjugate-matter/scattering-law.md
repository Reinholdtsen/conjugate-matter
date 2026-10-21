---
title: "The gated scattering law σ_T(v)"
weight: 40
status: alive
description: "σ_T(v) = σ₀F(v²/v*²): strong in slow dwarfs, off in fast clusters, isotropic below the gate; from v0.1's exponential cliff to the current knee, whose tail diagnoses the vertex."
provenance: [D, O]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §13 rows 1–3"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3b-wave-island.md 'The rate'"
---

*The gated scattering law gives the momentum-transfer cross-section σ_T of conjugate matter as a function of the relative velocity v of two colliding particles. Because [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) shuts the interaction off at large relative velocity, self-scattering is strong in dwarf galaxies, where dark matter moves slowly, and absent in galaxy clusters, where it moves fast; between the two, σ_T bends down at a knee at the gate velocity v\*. Below the knee the scattering is the same in every direction. The program first derived a sharp exponential cliff at v\*; it now claims only the knee, whose tail shape is open and diagnostic.*

**Status:** Alive — [D], with the shape [O] (`papers/broken-born-checkpoint-v2.md` §8) — derived in Born approximation in the lab notebook (#1 §5.1) and downgraded from cliff to knee in the Debt-1 notes; not machine-checked. The v0.1 exponential cliff is superseded.

## Key facts

- **The current law.** [The checkpoint](/wiki/history/documents/checkpoint) (#11 §8): "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking."
- **Row 1.** Against the standard expectation of cold dark matter (CDM) and of Yukawa [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) (SIDM), "CDM none; Yukawa SIDM power-law + Coulomb log", the requirement is "Knee at v\* ~ 10² km/s; zero cluster signal (particle χ)", killed by "Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band" (#11 §13). See [row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee).
- **Row 2, isotropy [D].** "Because the gate depends on k and the contact part is flat in q, scattering below v\* is isotropic; light-mediator Yukawa scattering is forward-peaked" ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §5.1). It assumes a heavy mediator. Row 2 is killed by "Morphology demanding forward peaking" (#11 §13); see [row 2](/wiki/predictions/scattering-isotropy).
- **Superseded: the v0.1 cliff [D].** "In Born approximation with a heavy transfer mediator (m_φ ≳ m_χ, contact-like in x)", #1 §5.1 derived the law below, with "An exponential cliff, not a power-law tail" and v0.1 row 1 reading "cliff at v\* ~ 120 km/s; **exactly zero in clusters forever**", killed by "Robust nonzero self-interaction at v > 3v\*" (#1 §9). These formulas appear only in #1 and are unverified; the checkpoint does not restate v\* ≡ √2μ/m_χ, though the conjugate-relativity paper uses it ([#13 §4](/wiki/conjugate-relativity/invariant-length-shell)).

```text
σ_T(v) = σ₀ e^{−v²/v*²},   v* ≡ √2 μ/m_χ,   σ₀ = 16πα̃²m_χ²/m_φ⁴
```

- **The downgrade.** When the gate's mechanism was derived, "row 1's 'exponential cliff' weakens to 'sharp knee at v\*, with the tail shape (Gaussian vs rational) a diagnostic of the vertex completion.' The knee's existence and location are robust; its steepness is model-internal information, not a guaranteed exponential" (`notes/debt1a-ii-X-classification.md` §4; #1 'Addendum (v0.4)'). The location moved from "v\* ~ 120 km/s" to "v\* ~ 10² km/s" and the kill condition from "v > 3v\*" to "v ≫ v\*". The tail is [the gate-shape problem](/wiki/dark-matter/conjugate-matter/gate-shape).
- **On the wave island.** For very light χ the suppression is "(v\*/σ)⁴ — **a power law, not an exponential**" (`notes/debt3b-wave-island.md`; Debt 3a's first estimate was (v\*/σ)³, and Debt 3c and the checkpoint use the fourth power), which makes the knee's shape the diagnostic of [row 3, the island discriminant](/wiki/predictions/island-discriminant). [Debt 3a](/wiki/history/documents/debt-3-notes) noted that "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)"; Debt 3b's (v\*/σ)⁴ law answers part of this, and no document restates isotropy for waves.

## Sources

- `papers/broken-born-checkpoint-v2.md` §8, §13 rows 1–3 — the current law; the requirements and kill conditions of rows 1–3
- `notes/debt1a-ii-X-classification.md` §4 and `notes/broken-born-theory.md` 'Addendum (v0.4)' — the downgrade from cliff to knee
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — rows 1–2 to be re-derived in wave language
- `notes/debt3b-wave-island.md` 'The rate' — the (v\*/σ)⁴ suppression on the wave island
- `notes/broken-born-theory.md` §5.1, §9 — the v0.1 cliff, σ₀, v\*, isotropy, the v0.1 row 1
