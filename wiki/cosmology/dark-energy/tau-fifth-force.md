---
title: "Fifth-force safety of τ"
weight: 50
status: alive
description: "As a pseudo-Goldstone field, τ couples derivatively, with no tree-level Yukawa coupling to Standard Model matter, so torsion-balance bounds are safe despite its tiny mass: a lab-notebook argument that no later document restates or revisits."
provenance: [D]
sources:
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §14 item 6"
  - "notes/broken-born-program-v1.md §10"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/beta-coefficients.md §3"
---

*Fifth-force safety is the requirement that a new light field not produce a detectable extra force between ordinary bodies. The program's dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) is extremely light, so if it coupled to ordinary matter through its value, as the gravitational potential does, it would add a long-range force of the kind that torsion-balance experiments search for. The [lab notebook](/wiki/history/documents/lab-notebook) argues that τ is an approximate [Goldstone field](/wiki/symmetry-breaking/goldstone-and-higgs), one whose couplings are fixed by a symmetry under shifting its value, so it couples to matter only through its rate of change, which produces no such static force between ordinary bodies. The argument appears only in the lab notebook, in its first version; the current checkpoint does not restate it, and no script checks it.*

**Status:** Alive — [D] (#1 §4) — argued in the lab notebook only; [checkpoint #11](/wiki/history/documents/checkpoint) does not restate it, the notebook names no experiment and cites no bound, and no `verify/` script checks it.

## The statement

The [lab notebook](/wiki/history/documents/lab-notebook)'s section "Consistency with everything already measured" (#1 §4) lists, beside the claims that [general relativity](/wiki/gravity/spin-2-fields/general-relativity) and the Standard Model (SM) are untouched:

> **Fifth forces.** τ is a (pseudo-)Goldstone: derivatively coupled, no tree-level Yukawa to SM matter, safe from torsion-balance bounds despite being ultralight. **[D]**

τ is the program's dark-energy field, the angle around the [Maslov circle](/wiki/phase-space/modular-field/maslov-phase) of the space of polarizations ([τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)). The statement has three parts: τ is a [pseudo-Goldstone field](/wiki/cosmology/dark-energy/axion-like-fields#τ-an-axion-like-dark-energy-field); therefore its couplings to ordinary matter are derivative, with no [Yukawa coupling](/wiki/gravity/spin-2-fields/yukawa-forces#the-field-τ-no-coupling-so-no-yukawa-force) at tree level; therefore it does not produce the static force that torsion balances test, however light it is. The sections below take them in reverse order.

## Fifth forces and how they are tested [T]

A scalar field φ of mass m that couples to ordinary matter through its value, by a term proportional to φ times the matter's mass density, is exchanged between any two bodies. The result is an extra static potential of Yukawa form, proportional to e^{−r/λ}/r, added to Newton's 1/r, with a range λ = ħ/(mc) set by the mass and a strength set by the coupling. If the coupling differs between materials, the extra force also violates the [universality of free fall](/wiki/gravity/spin-2-fields/equivalence-principle#the-weak-form-universality-of-free-fall-t) [T].

Torsion balances measure such forces: a suspended pendulum with test masses of different shapes or compositions responds to a force that does not follow Newton's law or that depends on composition, and the experiments constrain the strength of a Yukawa term over ranges from below a millimetre to astronomical scales (Adelberger, Heckel and Nelson †, a review). #1 names no experiment and cites no bound.

A field that is still evolving on cosmological time scales today must be extremely light, with a range at least comparable to the size of the observable universe [T]; #1 calls τ "ultralight". For a field that light, a coupling to mass density of gravitational strength would act as an additional component of gravity at every scale tested, and the tests leave room only for a very weak one. This is the general problem of couplings between [quintessence](/wiki/cosmology/dark-energy/quintessence) and ordinary matter (Carroll †).

## Why a shift symmetry removes the force [T]

### Derivative couplings

If the action is unchanged when τ is shifted by a constant, τ → τ + c, then no term can contain τ itself, only its derivatives ∂_μτ [T]. A mass term, a potential and a coupling of the form τ × (mass density) are all excluded. The leading interactions with matter take the form

```text
(1/F) ∂_μτ J^μ
```

with F a constant of the dimension of mass and J^μ a current built from the matter fields.

### No static force between ordinary bodies

Two cases cover the standard examples [T].

- If J^μ is a conserved current, such as a particle-number current, the coupling can be integrated by parts into −(1/F) τ ∂_μJ^μ, which vanishes. The coupling has no effect at all.
- If J^μ is an axial current, as for the axion, the coupling is to the spin of the matter particles. Exchange of the field then produces forces that depend on the spins of the sources (Moody and Wilczek †), which cancel between ordinary, unpolarized bodies.

In neither case is there a static attraction between unpolarized masses proportional to their mass or composition, which is what torsion balances test. This is the standard reason axion-like fields escape fifth-force bounds however light they are [T]. The general account of Goldstone modes is on [Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs).

## Why "pseudo"-Goldstone [T]

τ is not an exact Goldstone field, because it has a potential. Its potential, V(τ) = V₀[1 + cos(τ/f)] (#1 §3), is invariant only under shifts by whole periods, τ → τ + 2πf, not under arbitrary constant shifts. The continuous shift symmetry is therefore broken explicitly, by a small amount set by V₀, and τ is a pseudo-Goldstone field: light, with couplings that are derivative up to effects of that breaking ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)). The notebook's claim is limited accordingly to "no tree-level Yukawa"; it does not estimate couplings induced at loop level through the potential.

The later documents keep the pseudo-Goldstone picture, and the toy models are consistent with it. Version 2.2 of the checkpoint finds from the [toy models](/wiki/symmetry-breaking/toy-models) that the polarization is a Goldstone angle, and adds: "A definite polarization needs a ρ-preserving potential on that angle" (#11 §4, the [P2′](/wiki/program/postulates/p2-prime) refinement, [D][V]; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle); [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential)). The toy-model worklog notes that in 3+1 dimensions the [coset model](/wiki/symmetry-breaking/toy-models/coset-model) "can break the continuous U(1) itself, with τ an exactly massless Goldstone", and that since τ has a potential, "the explicit breaking is in the program anyway"; it summarizes the result as "a pseudo-Goldstone polarization angle with a ρ-symmetric potential" (`notes/toy-lagrangian.md`, 'Chunk 3 results').

## Scope

- **One source.** The argument is in the notebook's v0.1 only (#1 §4). #11 does not restate it, and the [handoff](/wiki/history/documents/handoff) does not list it among the live results.
- **No numbers.** #1 gives no mass for τ, no value of the coupling scale and no experimental bound; the claim is structural.
- **The v0.1 matter coupling.** In the notebook's action the Standard Model couples to the metric alone: "S_x is the Standard Model minimally coupled to g. Nothing is modified." (#1 §3, transcribed from its LaTeX). τ does not appear in S_x, and #1 does not write out the derivative coupling that §4 describes.
- **The v2.2 matter coupling.** Since v2.2 the breaking of reciprocity "is physical only once matter couples to the sign of K (P4)" (#11 §4; [P4](/wiki/program/postulates/p4-polarized-matter)), and the toy note builds such a coupling from the fields (H, K) ([locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)). No document revisits the fifth-force argument in that picture.
- **Not machine-checked.** No `verify/` script tests it.

## A related open problem

τ's mixing with the modes that the [momentum graviton X](/wiki/gravity/momentum-graviton) absorbs when it becomes massive has not been computed: "τ–Stückelberg mixing matrix [O]" (#11 §14 item 6). [Calc note #8](/wiki/history/documents/field-equation-notes) logged it as "expected small by compactness" (`notes/beta-coefficients.md` §3), and #9 repeats the expectation (§10 item 5). See [Open: τ–Stückelberg mixing (OP6)](/wiki/gravity/momentum-graviton/tau-stuckelberg-mixing) and [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten).

## Compare: X is safe by range

The momentum graviton X is protected differently. It couples to ordinary matter at gravitational strength, but it is massive, so its force is cut off beyond a range of order 1/M_X: in #11's words, "SM couplings gravitational-strength and Yukawa-cut at 1/M_X" (#11 §7.5). τ's protection is the reverse case: its range is unlimited, and the derivative form of its coupling removes the static force. See [safety by range: X and ordinary matter](/wiki/gravity/momentum-graviton/fifth-force-safety).

## Sources

- `notes/broken-born-theory.md` §4 — the statement and its tag (the only source for the claim); §3 — the potential, and the Standard Model coupled to g alone
- `papers/broken-born-checkpoint-v2.md` §4 — the P2′ refinement: the polarization as a Goldstone angle that needs a ρ-preserving potential, and matter coupling to the sign of K; §7.5 — X's Yukawa cut; §14 item 6 — τ–Stückelberg mixing, open
- `notes/toy-lagrangian.md` 'Chunk 3 results' — τ as a Goldstone in 3+1, "a pseudo-Goldstone polarization angle with a ρ-symmetric potential"
- `notes/beta-coefficients.md` §3 — the residual mixing "expected small by compactness"
- `notes/broken-born-program-v1.md` §10 item 5 — the same expectation in v1
