---
title: "Open: the dual-stress enhancement (OP5)"
weight: 70
status: open
description: "Why σ₀ can be nuclear-scale while Standard Model couplings to X stay gravitational: the main open quantitative item of the conjugate sector."
provenance: [O]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §14 item 5"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §4"
  - "notes/debt1a-iv-beta-coefficients.md §5"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-program-v1.md §10 item 4"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "HANDOFF.md §2"
  - "CLAUDE.md 'Since the handoff'"
---

*The dual-stress enhancement is the unexplained gap between how strongly [conjugate matter](/wiki/dark-matter/conjugate-matter) scatters off itself and how weakly ordinary matter couples to the same carrier. In the program both kinds of matter couple to the [momentum graviton X](/wiki/gravity/momentum-graviton): conjugate matter through its [dual stress](/wiki/dark-matter/conjugate-matter/dual-stress), ordinary matter through the spacetime metric. Fitting the flat cores of [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) needs a self-scattering cross-section that [the checkpoint](/wiki/history/documents/checkpoint) calls nuclear-scale, while ordinary matter must feel X only at gravitational strength. Something must make conjugate matter's coupling far more effective than ordinary matter's; what it is, and by how much, has not been worked out. The checkpoint calls it the main open quantitative item of the conjugate sector.*

**Status:** Open — [O] (`papers/broken-born-checkpoint-v2.md` §14 item 5) — the checkpoint calls it the "Main open quantitative item" (§8); no calculation exists and no source states the size of the gap. It qualifies [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism), which explains the gate's dependence on relative momentum but not its strength. It is listed in [open problems](/wiki/status/open-problems) and is not on the current work queue.

## The question

The checkpoint, #11, states it twice:

> "Main open quantitative item: the dual-stress enhancement (nuclear-scale σ₀ with gravitational SM couplings) [O]." (#11 §8)

> "Dual-stress enhancement parametrics [O]." (#11 §14 item 5)

SM is the Standard Model, ordinary matter. σ₀ is the low-velocity cross-section of [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law), σ_T(v) = σ₀F(v²/v\*²). "Parametrics" means how the size of the effect depends on the parameters of the theory; no source names which parameters.

The item was first logged in calc note #8, the last of [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes), at the end of its argument that ordinary matter is safe from X:

> "[Parametrics of the χ dual-stress enhancement — why σ₀ can be nuclear-scale while SM couplings stay gravitational — logged as the main open quantitative item.]" (`notes/debt1a-iv-beta-coefficients.md` §3)

The same note's close-out lists it among the open residue of Debt 1 as "(iv) dual-stress enhancement parametrics (gate strength vs gravitational SM coupling)" (§5).

## The strong side: σ₀

Conjugate matter's self-interaction is the gated amplitude M(k, q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²) (#11 §8; [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)). Its low-velocity cross-section is fixed by the cores of dwarf galaxies: "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §5.1). The lab notebook writes the cross-section as σ₀ = 16πα̃²m_χ²/m_φ⁴ and takes α̃ ~ 1 at [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark), where "the Born approximation is marginal" (#1 §5.1). A coupling of order one is a strong coupling.

#11 §8 calls this σ₀ "nuclear-scale", comparable to the cross-sections of nuclear physics [T]. The lab notebook states the core-fitting value without a citation; how self-scattering turns a dark-matter cusp into a core is the established physics of [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) [T].

## The weak side: ordinary matter

Ordinary matter couples to the metric g, and once [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) forces the two spin-2 frames to have equal Planck masses, the metric contains the massless graviton and X in comparable proportions. Calc note #8 draws the consequence:

> "With equal effective Planck masses (forced by the same symmetry), SM matter — coupled to g — sees both eigenstates with comparable strength; safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X, and gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X." (`notes/debt1a-iv-beta-coefficients.md` §3)

#11 §7.5 carries it as "SM couplings gravitational-strength and Yukawa-cut at 1/M_X". A gravitational-strength coupling is suppressed by the Planck mass, which makes it extremely weak for elementary particles [T]. The full argument is on [safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety). Calc note #8's summary has X coupled "to conjugate matter through the dual stress (the gate) and to ordinary matter only at gravitational strength and short range" (§4).

## Why the two must be reconciled

Both sides run through the same field. In the program's mechanism, conjugate matter scatters off itself by exchanging X between the dual stresses of two particles, and integrating out the massive X leaves the contact interaction of the gate ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). Ordinary matter exchanges the same X at gravitational strength. The fitted σ₀ requires X's coupling to conjugate matter's dual stress to be strong; the safety argument has X's coupling to ordinary matter gravitational. The open item is the account of that difference: v1 words it as "why σ₀ can be nuclear-scale while SM–X couplings stay gravitational" (#9 §6).

The word "enhancement" comes from the earlier calc notes, which attributed ordinary matter's weak coupling to its dual stress. Calc note #5: X "couples to x-polarized matter only through its (suppressed) dual stress" (§E). Calc note #6: "couplings to x-polarized (SM) matter run through the SM's dual stress, which is unenhanced" (§4). Conjugate matter's dual stress, by contrast, would have to be enhanced. Calc note #8 replaced the suppressed coupling with the range argument, in which ordinary matter couples to X through g at gravitational strength, so the contrast is now between conjugate matter's dual-stress coupling and ordinary matter's gravitational one.

## What the sources leave open

- **The size of the gap.** No source states how many orders of magnitude separate the two strengths. The wiki adds no estimate.
- **The parameters.** No source names the parameters the enhancement depends on. The amplitude's α̃ and m_φ are not related to M_X, the mass of X, in any document; the benchmark's choice m_φ ~ m_χ was made in v0.1, before X was identified as the carrier (#1 §5.1; [conflicts between sources](/wiki/history/documents/source-conflicts)).
- **A mechanism.** No source proposes one. The explicit form of the dual stress, which a mechanism would need, is itself not written down (`notes/debt1a-geometric-core.md` §E; [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress)).

Until the item is resolved, the strength of the gate is an input fitted to dwarf cores rather than an output of the X-exchange mechanism. The mechanism accounts for the gate's dependence on relative momentum, which is what [row 1](/wiki/predictions/self-interaction-knee) and [row 2](/wiki/predictions/scattering-isotropy) of [the predictions table](/wiki/predictions) test; the strength enters row 1 only as the fitted σ₀.

## History

1. **Calc note #8** logged it in §3 and listed it as residue (iv) of Debt 1 in §5 ([the three debts](/wiki/history/debts)).
2. **The lab notebook's v0.6 addendum** lists "dual-stress enhancement parametrics" among the "Residual open items (none existential)" (#1 'Addendum (v0.6)').
3. **v1** called it "The main open quantitative item" in its section on the gate (#9 §6) and listed it as item 4 of its open problems: "Dual-stress enhancement parametrics: σ₀ nuclear-scale with gravitational SM couplings [O]" (#9 §10).
4. **[The handoff](/wiki/history/documents/handoff)** lists it with [the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape) among the open items: "Gate shape (X propagator on momentum fibers); dual-stress enhancement parametrics" (`HANDOFF.md` §2, Open 6).
5. **The checkpoint** keeps it as the "Main open quantitative item" (§8) and item 5 of its open problems (§14).

The current queue, in the root `CLAUDE.md` ("Since the handoff"), does not include it.

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the open item and its tag; §14 item 5 — the open-problem entry; §7.5 — ordinary matter's couplings gravitational-strength and Yukawa-cut
- `CLAUDE.md` 'Since the handoff' — the current queue
- `HANDOFF.md` §2 — the item in the handoff's open list
- `notes/debt1a-iv-beta-coefficients.md` §3 — where the item was logged; safety by range; §4 — X's couplings to both kinds of matter; §5 — residue (iv)
- `notes/debt1a-ii-X-classification.md` §4 — ordinary matter's dual stress as unenhanced
- `notes/debt1a-geometric-core.md` §E — ordinary matter's dual stress as suppressed; the dual stress defined in words
- `notes/broken-born-program-v1.md` §6 — v1's statement of the item; §10 item 4 — v1's open-problem entry
- `notes/broken-born-theory.md` §5.1 — the dwarf-core value of σ₀/m, σ₀ in terms of α̃ and m_φ, the Born caveat; 'Addendum (v0.6)' — the item among the residual open items
