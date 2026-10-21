---
title: "Dirac quantization and the DSZ pairing"
weight: 10
status: established
description: "Dirac's condition e·g ~ 2π, the Dirac–Schwinger–Zwanziger pairing ⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ and mutual locality, the 2π-versus-4π normalization, and why a weakly coupled sector has strongly coupled monopoles."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §11.2"
  - "papers/broken-born-checkpoint-v2.md §11.3"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md ref [17]"
  - "notes/knot-dark-matter-standalone.md §2"
  - "review/round3-adjudication.md 'Rulings' 12"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "HANDOFF.md §2"
---

*Dirac quantization is the rule, found by Paul Dirac in 1931, that a magnetic monopole can exist in quantum mechanics only if the product of its magnetic charge g with any electric charge e is a whole-number multiple of a fixed constant: e·g ~ 2π in the normalization the checkpoint uses. Schwinger and Zwanziger extended the rule to dyons, particles that carry both kinds of charge, as the Dirac–Schwinger–Zwanziger (DSZ) pairing of two charges. Because the product is fixed, a small electric charge forces a large magnetic one, so a weakly coupled force has strongly coupled monopoles. The program builds its charge-lattice argument on the pairing, and the weak-to-strong consequence is one of the results that survived the retired soliton candidate.*

**Status:** Established — [T] — literature. The checkpoint cites Dirac 1931, Schwinger 1966 and Zwanziger 1968 together as [17†], from model memory, so the citation awaits [the † literature battery](/wiki/method/literature-battery). [The round-3 audit](/wiki/method/review/round-3/rulings) checked Dirac and Zwanziger, which the withdrawn [#14](/wiki/dark-matter/candidates/soliton-candidate) cited as its reference [7], and found that they support the antisymmetric pairing, with a normalization difference that ruling 12 accepted as minor.

## Key facts

- **Dirac's condition** ([#11](/wiki/history/documents/checkpoint) §11.2 [T]): "Dirac's condition e·g ~ 2π pins the magnetic coupling near 4π/e² ≈ 34 — the magnetic world is our strong-coupling mirror, heavy and bound" ([the magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family)). The figure depends on the normalization by a factor of 4: "1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn)" (`review/v3-worklog.md`, round-2 item R2, tagged [V]; no script in the current gate prints these two values).
- **The pairing** (#11 §11.3): "The Dirac–Schwinger–Zwanziger pairing ⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ is an antisymmetric integer form" [17†]. Each charge q = (e, g) lists a particle's electric and magnetic charge.

```text
⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ        mutual locality: ⟨q, q′⟩ = 0
```

- **Mutual locality** (#11 §11.3): "Mutual locality (which charges can share one Lagrangian) is ⟨q,q′⟩ = 0". The program reads these two facts as a symplectic structure on charge space with a Lagrangian sublattice ([the symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)); the round-3 audit called that reading "interpretation".
- **2π or 4π** (round-3 audit, Step 1, on #14's reference [7]): "Zwanziger's abstract states e_m g_n - g_m e_n in 4 pi Z; manuscript writes 2 pi Z (Dirac normalization). The 't Hooft-Polyakov monopole with doublets realises 2 pi, so the physics is fine; but [7] as cited states 4 pi." The audit also noted that the text named Schwinger without citing him. Ruling 12 accepted both points as minor ([round-3 rulings](/wiki/method/review/round-3/rulings)), and #11's [17†] now lists Schwinger 1966.
- **A weak force has strong monopoles** (#14 §2): the monopoles of a hidden SU(2) sector "carry magnetic charge g_m = 4 pi/g_d, the Dirac minimum relative to psi's charge g_d/2, so their mutual coupling is alpha_m = g_m^2/4pi = 1/alpha_W' [7]. Any weakly coupled hidden sector therefore has strongly coupled monopoles: the strong magnetic coupling is generic, not a hypothesis." Here g_d is the hidden gauge coupling and ψ a hidden fermion of charge g_d/2 ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)).

```text
α_W′ = g_d²/4π,    g_m = 4π/g_d,    α_m = g_m²/4π = 1/α_W′
```

- **What survives** (#11 §12): "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]" — listed among the survivors of [the soliton obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary), though the round-3 adjudication's own survivor list omits it.
- **Against which photon** (`HANDOFF.md` §2, under "Dead"): "α_d ≈ 34 via Dirac quantization against our photon (round-1 reviewer's valid kill: can't use our DSZ lattice and then deny coupling to our photon)." #14 v3 then applied the condition only within its hidden sector: "nothing is quantized against our gauge field" (#14 §2). See [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling). The checkpoint's figure for ordinary electromagnetism (§11.2) is a different statement and stands.

## Used by

- [The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice) — reads the DSZ pairing as a symplectic form on charge space.
- [The magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family) — Dirac's condition as the reason the magnetic counterparts are strongly coupled and unseen.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — the weak-to-strong result is among what survives.
- [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling) — the dead attempt to quantize a hidden sector's charges against our photon.

## Sources

- `papers/broken-born-checkpoint-v2.md` §11.2, §11.3, §12, ref [17] — Dirac's condition, the pairing and mutual locality, the surviving weak-to-strong result, and the citation (†).
- `review/round3/referee/audit-notes.md` Step 1 — the 2π-versus-4π normalization and the uncited Schwinger.
- `review/round3-adjudication.md` 'Rulings' 12 — both accepted as minor.
- `notes/knot-dark-matter-standalone.md` §2 — g_m = 4π/g_d and α_m = 1/α_W′, and "nothing is quantized against our gauge field" (withdrawn manuscript).
- `review/v3-worklog.md` 'Round-2 pending list' — the factor-of-4 convention spread, item R2 [V].
- `HANDOFF.md` §2 — the dead α_d ≈ 34 via our photon.
