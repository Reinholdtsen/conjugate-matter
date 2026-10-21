---
title: "The mean-field criterion and its 10²⁸–10³¹ shortfall"
weight: 40
status: alive
description: "Streams need g·n_gate ≳ m·min(σ, v*)²; at the scattering benchmark the interaction falls short by 10²⁸ in dwarf cores and 10³¹ in the Milky Way, and the H-theorem closes the collisional route."
provenance: [D]
sources:
  - "notes/debt3a-stream-stability.md 'Limit 1 (broad gate)'"
  - "notes/debt3a-stream-stability.md 'Limit 2 (narrow gate)'"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
---

*The mean-field criterion is the condition under which a gas of dark-matter particles with the gated attraction would break up into velocity streams on its own: the attraction energy among particles that share a velocity has to match the kinetic energy of their random motion. Debt 3 derived it in two limits of the [gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) and evaluated it at the scattering benchmark, where the coupling is already fixed by fitting the cores of dwarf galaxies. There the attraction falls short by a factor of about 10²⁸ in dwarf-galaxy cores and 10³¹ in the Milky Way's halo near the Sun, and collisions cannot make up the difference, because they only drive the gas toward a smooth thermal distribution. This result rules out [velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image) for particle dark matter; the result itself stands.*

**Status:** Alive — [D] (#11 §9 (i)), derived in `notes/debt3a-stream-stability.md`. Mean-field only: the general eigenvalue problem is bracketed by two limits, not solved. No `verify/` script checks the numbers, although the handoff marks them ✓; any check exists only in the old chat.

## Key facts

- **Broad gate** (μ ≫ mσ; dwarf regime), by "standard plasma-function algebra" ([Vlasov stability](/wiki/dark-matter/momentum-clumping/vlasov-stability)):

  ```text
  g n/(m σ²) ≥ 1,   i.e.   ε_int ≡ g n ≥ mσ²
  ```

  "Below threshold: Landau-damped, stable."
- **Narrow gate** (μ ≪ mσ; Milky Way and cluster regime): only co-movers count, n → n_gate ≈ n(v\*/σ)³/(2π)^{3/2}, and σ → v\*, giving g n_gate/(m v\*²) ≥ O(1).
- **Unified criterion** (3a): ε_gate ≳ m·min(σ, v\*)². #11 §9 writes it as g·n_gate ≥ m·min(σ,v\*)².
- **The benchmark** (3a; [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)): "The dwarf-core fit fixes σ₀/m = 30 cm²/g, hence g is spent — no freedom remains. With m_χ = 70 MeV, v\* = 120 km/s":
  - dwarf core (ρ ~ 1 GeV/cm³, σ ~ 30 km/s): ε_gate ~ 3×10⁻³⁷ GeV against m·min(σ,v\*)² ~ 7×10⁻¹⁰ GeV, ratio ~10⁻²⁸;
  - Milky Way halo, local (ρ ~ 0.4, σ ~ 155 km/s): ~3×10⁻³⁹ GeV against ~10⁻⁸ GeV, ratio ~10⁻³¹.
- **Robustness** (3a): "Fails by 28–31 orders of magnitude. Robust to every dropped O(1): halos are dilute, the force is contact-range, and a mean-field instability needs interaction energy density competitive with kinetic — scattering fits only need Γt ~ 1 over Gyr, which is ~30 orders cheaper."
- **The collisional route** (3a): "The H-theorem closes the collisional back door: gated collisions still maximize entropy; equilibrium is Maxwellian to one part in 10³⁰." The note states this in one sentence, without a separate derivation.
- **What follows.** Meeting the criterion at fixed σ₀/m requires a mass so small that dark matter is a wave ([the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem)); for particle dark matter, the [net theorem](/wiki/dark-matter/momentum-clumping/net-theorem) records clumping as forbidden.
- **Verification record.** The handoff writes "criterion fails by 10²⁸–10³¹ ✓", where ✓ marks a machine check, but no `verify/` script covers any Debt-3 number; #11 §9's tag [D] governs ([the iron rule](/wiki/method/verification/iron-rule)).

## Sources

- `notes/debt3a-stream-stability.md` 'Limit 1 — broad gate', 'Limit 2 — narrow gate' — the two thresholds and the unified criterion
- `notes/debt3a-stream-stability.md` 'Numbers at the scattering benchmark' — the shortfall table, robustness, the H-theorem
- `papers/broken-born-checkpoint-v2.md` §9 (i) — the current statement and its tag
- `HANDOFF.md` §2 — the ✓ with no script behind it
- `notes/broken-born-theory.md` 'Addendum (v0.2)' — the notebook's summary of the result
