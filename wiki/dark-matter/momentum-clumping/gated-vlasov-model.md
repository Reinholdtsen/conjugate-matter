---
title: "The gated Vlasov model"
weight: 30
status: method
description: "The mean-field setup Debt 3 used: a Gaussian gate on a contact interaction, with linear response as an eigenproblem on momentum space bracketed by two solvable limits; the retired 'γ vs Ω' framing."
sources:
  - "notes/debt3a-stream-stability.md 'Setup'"
  - "notes/debt3a-stream-stability.md 'Limit 1 (broad gate)'"
  - "notes/debt3a-stream-stability.md 'Limit 2 (narrow gate)'"
  - "notes/debt3b-wave-island.md 'Setup'"
  - "notes/broken-born-theory.md §11 item 3"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
---

*The gated Vlasov model is the simplified description of dark matter that Debt 3 used to test [velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image). Dark matter is treated as a smooth gas in position and momentum; besides gravity, each particle feels an attraction only from neighbours whose momentum lies within a narrow window around its own, the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate), and the attraction's range in space is shrunk to a point. Whether a small ripple in this gas grows then becomes an eigenvalue problem on momentum space, which the calculation brackets between a broad-gate limit and a narrow-gate limit rather than solving in general. The model also retired the earlier plan to race the growth of streams against orbital stirring, because below the threshold there is no growth to race.*

**Status:** Method — the setup of `notes/debt3a-stream-stability.md`, which carries no tag of its own; it rests on standard [Vlasov stability theory](/wiki/dark-matter/momentum-clumping/vlasov-stability). Its Gaussian gate is an assumption, since the gate shape is open (#11 §14 item 4). The earlier "γ vs Ω" framing is superseded.

## Key facts

- **Single-particle energy** (3a, Setup), with G "the Gaussian gate, G(0)=1, attractive sign, and the x-range collapsed to contact (range 1/m_φ, microscopic)":

  ```text
  ε(x, p) = p²/2m + mΦ_grav(x) − g ∫d³p′ G((p − p′)/μ) f(x, p′),
  g ≡ 4πα̃/m_φ² = √(πσ₀/m²)
  ```

- **Linear response** about "a homogeneous Maxwellian f₀(p) of dispersion σ", with perturbations δf ∝ e^{i(k·x − ωt)}:

  ```text
  δε(p) = g ∫d³p′ G(p − p′) [k·∇_{p′} f₀ / (ω − k·v′)] δε(p′)
  ```

  "An eigenvalue problem (the "potential" lives on momentum space), not a scalar dispersion relation. Two solvable limits bracket it."
- **The two limits.** Broad gate (μ ≫ mσ; the dwarf regime): "G → 1, δε constant, scalar relation." Narrow gate (μ ≪ mσ; the Milky Way and cluster regime): "Patch modes: δε supported on a momentum ball of radius ~μ." Their thresholds are on [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) page.
- **Conventions carried to the wave island** (3b, Setup): "Same conventions as Chunk A: σ₀ ≡ g²m²/π, gate width v\* in relative velocity", used for [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate).
- **The Gaussian assumption.** #11 §8 derives the gate's mechanism, X exchange over overlapping momentum-space wavepackets, but tags its shape [O]; #11 §14 item 4 leaves "Gaussian vs rational" open ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism), [the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)).
- **Superseded: the "γ vs Ω" framing.** The notebook listed the "Stream-instability growth rate γ vs. orbital phase-mixing" as open [O] (`notes/broken-born-theory.md` §11 item 3). 3a retired it: below threshold the perturbation is Landau-damped, and "The earlier "γ vs Ω" framing presumed growth exists; it exists only above this line." The comparison returns on the wave island as Γ_self against the stirring rate Ω = 1/t_dyn (3b).
- **Symbol collisions.** Here g is a coupling in GeV⁻², not the metric; G is the gate, not Newton's constant; ω and k are a frequency and a wavevector, not the symplectic form and the gate variable ([notation](/wiki/notation)).

## Sources

- `notes/debt3a-stream-stability.md` 'Setup' — the energy, the linearization and the eigenvalue problem
- `notes/debt3a-stream-stability.md` 'Limit 1 — broad gate' and 'Limit 2 — narrow gate' — the bracketing limits; the retirement of "γ vs Ω"
- `notes/debt3b-wave-island.md` 'Setup' — the conventions carried to the wave island
- `papers/broken-born-checkpoint-v2.md` §8, §14 item 4 — the gate's mechanism and its open shape
- `notes/broken-born-theory.md` §11 item 3 — the original "γ vs. orbital phase-mixing" problem
