---
title: "The velocity gate"
weight: 10
status: alive
description: "The self-interaction amplitude depends on the incoming relative momentum through a gate F(k²/μ²), a variable no position-local mediator produces; from the v0.1 Gaussian postulate to the current form."
provenance: [D, O]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §11 item 2"
  - "notes/broken-born-theory.md 'Addendum (v0.3, overnight)'"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-theory.md §5.2"
  - "HANDOFF.md §2"
---

*The velocity gate is a factor in the self-interaction of [conjugate matter](/wiki/dark-matter/conjugate-matter) that switches the interaction off when two particles approach each other with a large relative velocity. A force carried through position space makes the scattering depend on how much momentum the two particles exchange; the gate makes it depend on their incoming relative momentum, a dependence that, according to [the checkpoint](/wiki/history/documents/checkpoint), no position-local carrier produces. In signal terms, an ordinary contact force acts where two waveforms overlap, and the gate acts where two spectra overlap. The program first postulated the gate as a Gaussian, then derived its mechanism from exchange of the momentum graviton X; its exact shape is still open.*

**Status:** Alive — [D] for the mechanism, [O] for the shape (`papers/broken-born-checkpoint-v2.md` §8) — derived structurally in the [Debt-1 calc notes](/wiki/history/documents/debt-1-notes); no `verify/` script covers it.

## Key facts

- **The amplitude.** The checkpoint (#11 §8) gives χ's nonrelativistic self-interaction amplitude as the formula below, "k the incoming *relative* momentum — the variable no x-local mediator produces, delivered by X-exchange between dual-stress bilinears, with μ the χ quantum's intrinsic momentum-fiber width [D — mechanism; shape [O]]". Here q is the momentum transfer and x-local means local in position.

```text
M(k, q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²)
```

- **The symbols.** The checkpoint leaves α̃, m_φ and F undefined. They come from [the lab notebook](/wiki/history/documents/lab-notebook) (#1 §3) and [v1](/wiki/history/documents/checkpoint) (#9 §6): the prefactor is a Yukawa amplitude with coupling α̃ and transfer-mediator mass m_φ, and F is the gate. "An x-local Yukawa is the limit μ → ∞" (#1 §3), the ordinary [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) case.
- **The v0.1 postulate (superseded).** The lab notebook wrote the gate as a Gaussian, M(k, q) = 4πα̃m_χ/(q² + m_φ²)·e^{−k²/μ²}, with "k = m_χv_rel/2 the incoming **relative** momentum. The Gaussian *gate* e^{−k²/μ²} is the new object: it is the imprint of momentum-space locality, and it depends on k, not q" (#1 §3). That a gate exists was a postulate [P]; deriving its shape was open [O] (#1 §3; §11 item 2).
- **From postulate to mechanism.** The v0.3 addendum identified the carrier: "the *mechanism* is X-exchange between χ dual-stress bilinears, which produces dependence on incoming relative momenta — the defining property of the gate; the shape awaits the X propagator" (#1). The derivation is on [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism), the coupling on [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress), and the open shape on [the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape).
- **Two conventions, not reconciled.** The lab notebook's e^{−k²/μ²} with k = m_χv_rel/2 and the Debt-1 note's overlap form e^{−(p₁−p₂)²/2μ²} (`notes/debt1a-ii-X-classification.md` §4) are not reconciled in any source.
- **What it predicts.** The gate makes self-scattering strong at low relative velocity and suppressed at high: [the gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law), tested by [row 1](/wiki/predictions/self-interaction-knee) and [row 2](/wiki/predictions/scattering-isotropy) of the predictions table. It is the program's [Debt 2](/wiki/history/debts); [the handoff](/wiki/history/documents/handoff) lists it among the live results (`HANDOFF.md` §2).
- **What it did not deliver.** The same gated attraction underlay the founding image of dark matter clumping by velocity (#1 §5.2), which the program's own calculation killed: see [the obituary](/wiki/dark-matter/momentum-clumping/founding-image).
- **A name collision.** "The gate" also names the build check `scripts/check.sh`; that is [a different page](/wiki/method/verification/the-gate).

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the current amplitude, the gate variable and the tags
- `HANDOFF.md` §2 — the gate among the live results
- `notes/debt1a-ii-X-classification.md` §4 — the overlap form e^{−(p₁−p₂)²/2μ²}
- `notes/broken-born-theory.md` §3 — the v0.1 Gaussian gate, k = m_χv_rel/2, the μ → ∞ Yukawa limit, the [P] and [O] tags
- `notes/broken-born-theory.md` §11 item 2 — the gate-shape derivation listed as open in v0.1
- `notes/broken-born-theory.md` 'Addendum (v0.3, overnight)' — the mechanism identified as X exchange
- `notes/broken-born-program-v1.md` §6 — v1's statement, with q the transfer
- `notes/broken-born-theory.md` §5.2 — the gated attraction in the founding image
