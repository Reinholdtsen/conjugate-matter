---
title: "τ as the Maslov phase of the boundary"
weight: 50
status: alive
description: "The dark-energy field τ ≡ f·arg det² is the phase of Z's boundary value on Λ(d); its 2πf periodicity is topology, and its lightness among the ten moduli is postulated."
provenance: [D, T, P]
sources:
  - "papers/broken-born-checkpoint-v2.md §6"
  - "notes/broken-born-theory.md §2"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/broken-born-program-v1.md §4"
  - "notes/debt1a-geometric-core.md §B"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §7"
---

*The program's dark-energy field τ is an angle: the phase of a determinant built from the boundary value of [the modular field](/wiki/phase-space/modular-field/modular-field-z), measured around the Maslov circle of [the Lagrangian Grassmannian](/wiki/phase-space/modular-field/lagrangian-grassmannian), which forms the boundary of the Siegel domain. Because that circle cannot be shrunk to a point, τ is periodic, with period 2πf, as a matter of topology rather than of modeling choice. Of the ten directions of the Grassmannian at d = 4, τ is assumed to be the only light one. The identification is derived [D], the topology is literature [T], and the lightness is a postulate [P]; τ's behavior as dark energy is worked out in the cosmology section.*

**Status:** Alive — the identification is derived [D] (#11 §6); the Shilov boundary and π₁ = ℤ are literature [T]; the periodicity is [D] and τ's lightness [P] (#1 §2) — nothing here is machine-checked.

## Key facts

- **Definition.** #1 §2:

  ```text
  τ ≡ f · arg det²(·)
  ```

  "is a compact, 2πf-periodic modulus of the vacuum. This field is promoted below to the dark-energy field. Periodicity is topology [D]; that τ is the *lightest* modulus, with the other nine directions heavy, is assumed [P]."
- **The identification.** #11 §6: "**Λ(d) is the Shilov boundary** of the Siegel domain [T]; the dark-energy field τ is the Maslov phase of the boundary variable, its periodicity a fact of topology (π₁(U(d)/O(d)) = ℤ)." #9 §4 adds: "not a modeling choice".
- **Two wordings.** #5 §C describes τ as "arg det of the boundary variable" and "the phase of Z's boundary value", without the square or the scale f of #1's definition; the documents do not reconcile the two forms.
- **Restored by P2′.** Under strict P2 there is "No Lagrangian Grassmannian, no Maslov circle, **no τ field**" (#5 §B); with only ω rigid, the Grassmannian, the Maslov circle and τ are restored. See [original P2](/wiki/program/postulates/original-p2) and [P2′](/wiki/program/postulates/p2-prime).
- **Its dynamics, elsewhere.** #11 §10 makes τ "hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology" ([τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence)). The sign of that potential is unresolved across the documents ([the sign of V(τ)](/wiki/cosmology/dark-energy/potential-sign)), and its origin is open ([the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). τ survives X's Higgs mechanism: "τ un-eaten (compact J-sector, not the Stückelberg sector)" (#11 §7.5; [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten)). Its test is [row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift).
- **Toy support, consistency only.** #11 §10 (v2.2): "In the coset model that angle parametrizes Λ(1): it is τ's circle. A definite polarization requires the ρ-preserving potential this section posits." And: "None of this tests the cosmology; it only shows the structure is consistent." See [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle).

## Sources

- `papers/broken-born-checkpoint-v2.md` §6 — the identification and the topological periodicity.
- `papers/broken-born-checkpoint-v2.md` §10 — τ as hilltop quintessence; the toy-model support and its limit.
- `papers/broken-born-checkpoint-v2.md` §7 — τ un-eaten by the Higgs mechanism.
- `notes/broken-born-theory.md` §2 — the definition τ ≡ f·arg det², with the [D] and [P] tags.
- `notes/debt1a-geometric-core.md` §B, §C — τ lost under strict P2 and restored; τ as the phase of Z's boundary value.
- `notes/broken-born-program-v1.md` §4 — "not a modeling choice".
