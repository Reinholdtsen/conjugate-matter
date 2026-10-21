---
title: "Open: τ–Stückelberg mixing (OP6)"
weight: 70
status: open
description: "How strongly the dark-energy field τ mixes, through the potential, with the Stückelberg modes that X absorbs: logged in calc note #8 as expected small by compactness, never computed."
provenance: [O]
sources:
  - "papers/broken-born-checkpoint-v2.md §14 item 6"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/debt1a-iv-beta-coefficients.md §1"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-iii-tuning-test.md §3"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/debt1a-iii-tuning-test.md §5"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-program-v1.md §10"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §8"
  - "CLAUDE.md 'Since the handoff'"
---

*This open problem asks how strongly the dark-energy field τ mixes with the Stückelberg modes, the would-be Goldstone fields that the [momentum graviton X](/wiki/gravity/momentum-graviton) absorbs when it becomes massive. Two fields mix when the quadratic part of a theory contains a term coupling them, so that neither has a definite mass on its own. The program's leading-order result is that τ is not among the absorbed modes and stays light ([τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten)). Calc note #8 logged a residual mixing through the potential and expected it to be small because τ lives on a compact space; no document computes it. It is item 6 of the open problems in [checkpoint #11](/wiki/history/documents/checkpoint) §14 [O].*

**Status:** Open — [O] — item 6 of #11 §14; logged in calc note #8 (`notes/debt1a-iv-beta-coefficients.md` §3 and §5) with an expectation but no calculation; no `verify/` script; not on the current work queue. Listed in [Open problems and the queue](/wiki/status/open-problems).

## The question

#11 §14, item 6, in full: "τ–Stückelberg mixing matrix [O]."

The item asks for a matrix: the quadratic couplings between τ and the modes that X absorbs, and from them the combinations of fields that have definite masses. Its origin is a parenthesis at the end of calc note #8's derivation that τ is not eaten (§3; see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)):

```text
(Residual τ–Stückelberg mixing through the potential: logged, expected small by compactness.)
```

The question qualifies the leading-order result [τ is not eaten](/wiki/gravity/momentum-graviton/tau-not-eaten) [D — leading order], and through it the role that calc note #7 gives τ in [constrained bimetric gravity](/wiki/gravity/tuning-test/constrained-bimetric): "the light direction of the compact space being τ (the dark-energy field) and the massive spin-2 being X" (§4).

## Background: Stückelberg fields and mixing [T]

When a gauge symmetry is broken spontaneously, its would-be Goldstone fields do not appear as massless particles. They become extra polarization states of the gauge field, which becomes massive: the Higgs mechanism ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)) [T]. The Stückelberg description keeps those fields in view. The massive field is written as a gauge field combined with the would-be Goldstone fields, now called Stückelberg fields, so that the gauge symmetry stays manifest. Choosing the unitary gauge sets the Stückelberg fields to zero, and they survive only as the massive field's extra polarizations; they are then said to be "eaten" [T].

For a massive spin-2 field the Stückelberg fields are a vector and a scalar. Of its five polarization states, the two of helicity ±2 belong to the tensor itself, the two of helicity ±1 to the vector and the one of helicity 0 to the scalar [T] (Arkani-Hamed, Georgi and Schwartz 2003 †; the review by Hinterbichler 2012 †).

Two fields mix when the quadratic part of the Lagrangian contains a term proportional to their product. Neither field then has a definite mass. The states of definite mass are combinations of the two, found by diagonalizing the matrix of quadratic couplings; that matrix, or the rotation that diagonalizes it, is the mixing matrix. When the off-diagonal entries are small compared with the difference of the diagonal ones, each mass state is mostly one of the original fields [T].

## The two sectors

### The modes X absorbs

X becomes massive through [the gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs). Its local shifts δX_μν = ∂₍μλ_ν₎ form a second copy of linearized diffeomorphisms ([dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms)), and the vacuum's choice of polarization breaks them. Calc note #6 §3 [D — structural]: "the four would-be Goldstones π_μ of the broken λ-gauge are eaten; X becomes a **massive spin-2** with its five polarizations". Calc note #8 §3 words it differently: the Higgsing "eats the vector π_μ and the *longitudinal scalar of the λ-gradient sector*". No document reconciles the two wordings, and #11 §7.1 follows #6 ("X eats the four Goldstones"). Either way, these are the Stückelberg modes of the item.

### τ

τ is the dark-energy field. It is a coordinate on [the Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian), the compact space of possible polarizations J, and specifically its [Maslov phase](/wiki/phase-space/modular-field/maslov-phase): "the dark-energy field τ is the Maslov phase of the boundary variable, its periodicity a fact of topology (π₁(U(d)/O(d)) = ℤ)" (#11 §6). Its dynamics as dark energy are on [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence).

The leading-order argument separates τ from the absorbed modes by where each comes from. Calc note #6 §3: "The Λ(d) moduli, τ included, are not the eaten modes — they carry the compact phase directions, which constant shifts do not generate". Calc note #8 §3: "τ is a J-modulus on the compact Λ(d), a different sector with different origin; it survives as the light field." #11 §7.5 [D]: "τ un-eaten (compact J-sector, not the Stückelberg sector)."

### Where the sectors meet

#8 says the residual mixing arises "through the potential". The potential that gives X its mass is, in the Debt-1 notes, a wedge polynomial of two frames: the symplectic vielbein E and the polarization frame E₀[J] (#7 §3; [the frame tier](/wiki/gravity/tuning-test/frame-tier)), written for the frames e and f = E₀[J] as V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏) (#8 §1; [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)). The second frame depends on J, and τ is one of J's moduli, so the potential involves both sectors. The notes write no formula for the mixing.

## What the leading-order result leaves open

#8 tags its result "[D — leading order]" and does not say what the expansion is in. "Residual" mixing is what lies beyond that order. The two documents that state an expectation, #8 §3 and the superseded v1 paper, give the same one, "expected small by compactness", and neither gives the argument. The compactness in question is that of Λ(d), on which τ is an angle; the absorbed modes come from the shifts of X, which do not generate the compact directions (#6 §3). How that difference would make the mixing small is not written down anywhere, and no document says what a large mixing would change.

## History of the item

- **Calc note #6 §3** first raised τ's survival as a question: "verifying τ survives un-eaten is flagged [O]."
- **Calc note #7 §5** listed "(ii) τ-not-eaten verification" among the remaining items of Debt 1, with the note that "Items (ii)–(iv) are checks; item (i) is the substance."
- **Calc note #8 §3** derived "τ is not eaten [D — leading order]" and logged the residual mixing. Its close-out (§5) lists "(iii) τ–Stückelberg mixing matrix" among the "Open residue, none of it existential" of Debt 1 ([The three debts](/wiki/history/debts)).
- **The lab notebook's v0.6 addendum** carries the same list of "Residual open items (none existential)", including "τ–Stückelberg mixing" ([the lab notebook](/wiki/history/documents/lab-notebook)).
- **The v1 paper (#9) §10, item 5**: "τ–Stückelberg mixing matrix; expected small by compactness [O]."
- **#11 §14, item 6** keeps the item and drops the expectation: "τ–Stückelberg mixing matrix [O]."
- **The handoff's list of open problems** (`HANDOFF.md` §2) does not include it ([the handoff document](/wiki/history/documents/handoff)).

## Priority

#11 §15 says "the word 'theory' still waits on items 1–3" of §14: [deriving the wedge sector from S_H](/wiki/gravity/tuning-test/wedge-reduction), [the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison) and [the Lorentzian dressing](/wiki/phase-space/born-geometry/lorentzian-dressing). Item 6 is not among them. The current queue in the root `CLAUDE.md` ("Since the handoff") is `HANDOFF.md` §8 items 5–7 (the partially-massless comparison, the † literature battery and the phase-space-diameter note), then an optional round-5 review of the toy-model note; the mixing matrix is not on it.

## Sources

- `papers/broken-born-checkpoint-v2.md` §14 item 6 — the open problem as currently listed; §7.5 — τ un-eaten, "not the Stückelberg sector"; §6 — τ as the Maslov phase; §15 — which items gate "theory"
- `notes/debt1a-iv-beta-coefficients.md` §3 — τ not eaten at leading order and the logged residual mixing; §5 — the open residue of Debt 1; §1 — the potential for the frames e and f = E₀[J]
- `notes/debt1a-ii-X-classification.md` §3 — the eaten Goldstones, τ's survival first flagged [O]
- `notes/debt1a-iii-tuning-test.md` §3 — wedge polynomials of (E, E₀[J]); §4 — τ as the light direction of the compact space; §5 — τ-not-eaten listed as a check
- `notes/broken-born-program-v1.md` §10 — the superseded v1 listing, "expected small by compactness"
- `notes/broken-born-theory.md` 'Addendum (v0.6)' — the lab notebook's list of residual open items
- `HANDOFF.md` §2 — the handoff's open list, which omits the item; §8 — the queue items the root `CLAUDE.md` adopts
- `CLAUDE.md` 'Since the handoff' — the current queue
