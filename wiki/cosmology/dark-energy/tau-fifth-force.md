---
title: "Fifth-force safety of τ"
weight: 50
status: alive
description: "As a pseudo-Goldstone field, τ couples derivatively, with no tree-level Yukawa coupling to Standard Model matter, so torsion-balance bounds are safe despite its tiny mass."
provenance: [D]
sources:
  - "notes/broken-born-theory.md §4"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §14 item 6"
  - "notes/broken-born-program-v1.md §10"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
---

*Fifth-force safety is the requirement that a new light field not produce a detectable extra force between ordinary bodies. The dark-energy field τ is extremely light, so if it coupled to ordinary matter through its value, as the gravitational field does, it would produce a long-range force of the kind that torsion-balance experiments search for. The lab notebook argues that τ is an approximate Goldstone field, one whose couplings are fixed by a symmetry under shifting its value, so it couples to matter only through its rate of change, which produces no such static force. The argument appears only in the lab notebook; the current checkpoint does not restate it.*

**Status:** Alive — [D] (#1 §4) — argued in the lab notebook only; #11 does not restate it, and no script checks it.

## Key facts

- **Statement.** #1 §4: "**Fifth forces.** τ is a (pseudo-)Goldstone: derivatively coupled, no tree-level Yukawa to SM matter, safe from torsion-balance bounds despite being ultralight. **[D]**" Here SM means the Standard Model, and τ is the program's dark-energy field ([τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)).
- **Why a derivative coupling is safe [T].** If the couplings are invariant under τ → τ + constant, τ can enter them only through its gradient ∂τ, never through its value. Such couplings do not produce the static Yukawa attraction between unpolarized bodies that torsion balances test; this is the standard protection of axion-like fields.
- **Pseudo-Goldstone [T].** τ's potential V₀[1 + cos(τ/f)] breaks the shift symmetry explicitly, which makes τ a pseudo-Goldstone field rather than an exact one. Since v2.2 the polarization is a Goldstone angle, and "A definite polarization needs a ρ-preserving potential on that angle" (#11 §4, the P2′ refinement, [D][V]); the toy worklog's summary is "a pseudo-Goldstone polarization angle with a ρ-symmetric potential" (`notes/toy-lagrangian.md`, 'Chunk 3 results'). See [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and [Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs).
- **A related open problem.** τ's mixing with the eaten Stückelberg modes of the momentum graviton is open: "τ–Stückelberg mixing matrix [O]" (#11 §14 item 6), "expected small by compactness" (#9 §10 item 5). See [Open: τ–Stückelberg mixing (open problem 6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing).
- **Compare X.** The momentum graviton X is protected differently, by its short range: [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety).

## Sources

- `notes/broken-born-theory.md` §4 — the statement and its tag (the only source)
- `papers/broken-born-checkpoint-v2.md` §4 — the P2′ refinement: the polarization as a Goldstone angle that needs a ρ-preserving potential
- `papers/broken-born-checkpoint-v2.md` §14 item 6 — τ–Stückelberg mixing, open
- `notes/broken-born-program-v1.md` §10 item 5 — "expected small by compactness"
- `notes/toy-lagrangian.md` 'Chunk 3 results' — "a pseudo-Goldstone polarization angle with a ρ-symmetric potential"
