---
title: "Row 3: the island discriminant"
weight: 40
status: alive
description: "The knee's tail tells particles from waves — a sharp cutoff for particle χ, a (v*/σ)⁴ power law for wave χ: a diagnostic salvaged from Debt 3, with open caveats on its particle side."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 3"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3b-wave-island.md 'Standing results after Chunks A+B'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure of Debt 3'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3)'"
  - "notes/broken-born-program-v1.md §7"
---

*The island discriminant is a proposed way to read from astronomical data whether dark matter is made of particles or of a classical wave field. The program's gated self-interaction weakens above the gate velocity v\* in both cases, but differently: for particles the cutoff is sharp, while for a wave field it falls off only as a power law, (v\*/σ)⁴, where σ is the velocity dispersion of the halo. The program calls the two regimes the particle island and the wave island, and the shape of the knee in the scattering strength (the subject of [row 1](/wiki/predictions/self-interaction-knee)) would say which one dark matter occupies. The diagnostic came out of the calculation that killed velocity clumping (Debt 3); #11 counts it among its predictions not previously posed, and it selects a branch rather than killing the program.*

**Status:** Alive, as a diagnostic — [D] — a corollary of the wave-island condensation rate in calc note #3 (`notes/debt3b-wave-island.md`, where the rate is tagged [D, heuristic coefficients]), stated in #11 §9 and §13; not machine-checked. Its particle side assumes a Gaussian tail, which is now open [O] (#11 §14 item 4).

## Key facts

- **The row** ([checkpoint #11](/wiki/history/documents/checkpoint) §13). Observable: "**Island discriminant**". Standard expectation: "(not previously posed)". Requirement: "Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave". Role: "Diagnostic — selects the branch (particle vs wave χ)".
- **The two laws** (calc note #3, corollary 1): "The velocity suppression of self-interaction effects is e^{−v²/v\*²} on the particle island but (v\*/σ)⁴ on the wave island. The cliff's *sharpness* distinguishes the islands observationally."
- **Where (v\*/σ)⁴ comes from.** The [gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) on the wave island, displayed below with c = O(5–15), is suppressed when the gate is narrow "by (v\*/σ)⁴ — **a power law, not an exponential**" (calc note #3). #11 §9 tags this rate [D + T]: Bose-enhanced, in the style of Levkov, Panin and Tkachev [13†], with its coefficients [O]. Calc note #2's first estimate was a "(v\*/σ)³ suppression"; calc notes #3 and #4 and #11 use the fourth power.

```text
Γ_self ≈ c · g²ρ² min(σ, v*)⁴ / (m³σ⁶)
```

- **The two islands.** By the [classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem), collective behaviour needs "m ≲ 0.1 meV, where N_occ ~ 10²⁰" (#11 §9), so classical particle χ scatters but cannot clump collectively, and collective behaviour belongs to a wave field ([occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number)). After Debt 3, "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings" (calc note #4; [the wave island](/wiki/dark-matter/momentum-clumping/wave-island)).
- **Origin.** #11 §9: "Salvage: the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island." It took the place of the two withdrawn rows: "A new row replaces them: **cliff-sharpness island discriminant**" (#1 'Addendum (v0.2, post Debt-3)'). See [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem), [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image) and [the history of the table](/wiki/predictions/table-history).
- **Standing.** #11 §15 counts "predictions not previously posed (rows 3, 11)" among the program's progressive signs.
- **Open caveats.** The sharp particle-side cutoff e^{−v²/v\*²} is the Gaussian gate of v0.1; since addendum v0.4 the tail is "Gaussian vs rational", and the gate shape is #11 §14 item 4 [O] ([Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)). The sources do not ask whether a rational particle-side tail could resemble the wave-side power law. The two laws are also written in different variables: the collision speed v on the particle side, the halo dispersion σ on the wave side.
- **Use.** Rows 1–3 are the discriminators of [row 11](/wiki/predictions/dark-sector-microstructure), whose candidates #11 §12 lists with "knee at v\*, sharp tail" for [χ particles](/wiki/dark-matter/candidates/chi-particles) and "knee shape wave-like" for [the X-condensate](/wiki/dark-matter/candidates/x-condensate).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 3 — the row; §9 for the salvage, the rate's tags and the classicality theorem; §14 item 4 for the open gate shape; §15 for "not previously posed"
- `notes/debt3b-wave-island.md` 'The rate', 'Standing results after Chunks A+B' — the rate, the (v\*/σ)⁴ suppression and corollary 1 (the discriminant)
- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — the surviving wave island and the discriminant among the surviving content
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — the first (v\*/σ)³ estimate
- `notes/broken-born-theory.md` 'Addendum (v0.2, post Debt-3)' and `notes/broken-born-program-v1.md` §7 — the discriminant as the replacement row and as v1's salvage
