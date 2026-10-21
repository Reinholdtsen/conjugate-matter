---
title: "Dual diffeomorphisms: a second graviton"
weight: 20
status: alive
description: "Local shifts δX_μν = ∂₍μλ_ν₎ form a second copy of linearized diffeomorphisms because X is symmetric, which makes X a second graviton."
provenance: [D, T]
sources:
  - "notes/debt1a-ii-X-classification.md §2"
  - "notes/debt1a-ii-X-classification.md §3"
  - "papers/broken-born-checkpoint-v2.md §7.1"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
---

*Dual diffeomorphisms are the local form of the momentum graviton's [shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry): X may be shifted by the symmetrized derivative of an arbitrary vector field λ_μ(x), δX_μν = ∂₍μλ_ν₎. The metric fluctuation of linearized [general relativity](/wiki/gravity/spin-2-fields/general-relativity) has exactly this gauge redundancy, so X, a symmetric tensor with the same redundancy, is a second graviton-like gauge field. That identification drives the rest of the chain in [checkpoint #11](/wiki/history/documents/checkpoint) §7.1: a second interacting massless graviton is excluded by a theorem, so X has to become massive. The result is derived and rests on standard linearized gravity [D + T].*

**Status:** Alive — [D + T] in calc note #6 (`notes/debt1a-ii-X-classification.md` §2) and in #11 §7.1 — a structural argument, not machine-checked.

## Key facts

- Calc note #6 §2 [D + T] (see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)): "The local version of these shifts sits inside the ω-generalized diffeomorphisms: dual-diffeomorphism parameters λ_μ(x) act as δX_μν = ∂_(μ λ_ν) — because X is symmetric, this is a second copy of linearized diffeomorphisms, making X a second graviton-like gauge field."
- #11 §7.1, step (ii): "Locally, dual diffeomorphisms act as δX_μν = ∂₍μλ_ν₎ — a second linearized-diff gauge field, because X is symmetric".
- The contrast case is [double field theory](/wiki/phase-space/born-geometry/double-field-theory), where, in #6 §2's words, "the doubled partner is the antisymmetric B-field, δB = dλ, a 2-form gauge theory — spin-wise harmless." The program's reading of this contrast is [The symplectic partner of the graviton is another graviton](/wiki/gravity/momentum-graviton/symplectic-partner).
- Two facts then close the massless option (#6 §2). With the gauge invariance, X is a second massless spin-2 field, and the [multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go) excludes interacting massless gravitons [T]. Without it, the signature obstruction leaves a Lorentz-covariant symmetric tensor no ghost-free two-derivative kinetic term ([The Fierz–Pauli mass term and the Boulware–Deser ghost](/wiki/gravity/spin-2-fields/fierz-pauli)) [T — standard]. The assembled argument is [Why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain).
- The vacuum breaks these gauge symmetries (#6 §3): "The vacuum ⟨Z⟩ = i·g sits at X = 0 and is moved by the shifts: the polarization selection (η-emergence) spontaneously breaks the local dual diffeomorphisms." This is [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs).
- The lab notebook's v0.4 addendum records the same step: "Its local gauge structure δX_μν = ∂_(μλ_ν) makes it a second graviton".

## Sources

- `notes/debt1a-ii-X-classification.md` §2 — the derivation [D + T]; §3 for the breaking by the vacuum
- `papers/broken-born-checkpoint-v2.md` §7.1 — the current statement, step (ii) of the chain
- `notes/broken-born-theory.md` 'Addendum (v0.4)' — the lab notebook's record
