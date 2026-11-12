---
title: "Row 3: the island discriminant"
weight: 40
status: alive
description: "The knee's tail tells particles from waves — a sharp cutoff for particle χ, a (v*/σ)⁴ power law for wave χ: a diagnostic salvaged from the clumping problem, with open caveats on its particle side."
provenance: [D]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 3"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 4"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "notes/wave-island.md 'The rate'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "notes/wave-island.md 'Standing results after Chunks A+B'"
  - "notes/ufd-endpoint.md 'Verdict and closure of the clumping problem'"
  - "notes/stream-stability.md 'Consequences for the predictions table'"
  - "notes/x-classification.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.2, after the clumping notes)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-program-v1.md §11"
  - "HANDOFF.md §2"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
  - "review/wiki-build-flags.md items 19, 55"
  - "notes/gate-mechanism.md §3"
  - "notes/gate-mechanism.md §5"
---

*The island discriminant is a proposed way to read from astronomical data whether [dark matter](../dark-matter/_index.md) is made of particles or of a classical wave field. The program's gated self-interaction weakens above the gate velocity v\* in both cases, but differently: for particles the cutoff is sharp, while for a wave field it falls off only as a power law, (v\*/σ)⁴, where σ is the [velocity dispersion](../dark-matter/halo-astrophysics/velocity-dispersion.md#row-3-the-island-discriminant) of the halo. The program calls the two regimes [the particle island](../dark-matter/momentum-clumping/classicality-theorem.md#the-particle-island) and [the wave island](../dark-matter/momentum-clumping/wave-island/_index.md), and the shape of the knee in the self-interaction strength, the subject of [row 1](self-interaction-knee.md), would say which one dark matter occupies. The diagnostic came out of the calculations that tested [velocity clumping](../dark-matter/momentum-clumping/founding-image.md), the program's founding image and P.R.'s open conjecture ([the clumping problem](../history/main-problems.md)). [#11](../papers/broken-born-checkpoint-v2.md) counts it among its predictions not previously posed, and it selects a branch rather than killing the program. Its particle side assumes a sharp tail, which the program treats as open, and a note of 2026-10-28 makes whether the discriminant survives at all an open question.*

**Status:** Alive, as a diagnostic — [D] — a corollary of the wave-island [condensation rate](../dark-matter/momentum-clumping/wave-island/condensation-rate.md) in [calc note #3](../history/documents/clumping-notes.md) ([`notes/wave-island.md`](../../notes/wave-island.md), where the rate is tagged [D, heuristic coefficients]), carried in [#11 §9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)'s wave-island result [D + T] and stated as row 3 of [#11 §13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions); not machine-checked. Its particle side assumes a sharp tail, while the tail's shape is open [O] ([#11 §14 item 4](../papers/broken-born-checkpoint-v2.md#14-open-problems)). No source records a test. [`notes/gate-mechanism.md`](../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging [#11 §7](../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate, whose mechanism [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) tags [D — mechanism; shape [O]], and flag 55 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md), pending, proposes [P] for the gate and μ and [O] for the mechanism ([the gate mechanism](../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). The flag adds: "It also opens whether row 3's island discriminant survives" ([below](#caveats-and-open-questions)).

## The row

[Checkpoint #11](../history/documents/checkpoint.md) [§13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions), row 3:

| Observable | Standard expectation | Program requirement | Killed by |
| --- | --- | --- | --- |
| **Island discriminant** | (not previously posed) | Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave | Diagnostic — selects the branch (particle vs wave χ) |

Two columns differ from the other rows. There is no standard expectation, because the question had not been asked: v1 wrote "— (question not previously posed)" ([#9 §9](../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions)). And there is no kill condition. Whatever shape the tail has, the row assigns dark matter to one branch or the other; it is "Diagnostic, not a kill: identifies the branch" in v1's words ([#9 §9](../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions)).

## The two islands

The row's two branches are the two regimes that the clumping problem found for [conjugate matter χ](../dark-matter/conjugate-matter/_index.md), separated by mass ([the clumping calc notes](../history/documents/clumping-notes.md)).

- **The particle island.** Heavy χ, of MeV to GeV mass, is a gas of classical particles. Its self-interaction acts collision by collision, through the two-body cross-section of [the gated scattering law](../dark-matter/conjugate-matter/scattering-law.md). This is the home of [the χ-particle candidate](../dark-matter/candidates/chi-particles.md) ([the particle island](../dark-matter/momentum-clumping/classicality-theorem.md#the-particle-island)).
- **The wave island.** Very light χ has so many quanta in each quantum state that the halo behaves as a classical wave field ([occupation number](../dark-matter/wave-dark-matter/occupation-number.md)). After the clumping problem, "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings" ([`notes/ufd-endpoint.md`](../../notes/ufd-endpoint.md); [the wave island](../dark-matter/momentum-clumping/wave-island/_index.md)).

[The classicality theorem](../dark-matter/momentum-clumping/classicality-theorem.md) explains why there are two islands rather than one continuum of behaviour: satisfying the criterion for collective behaviour "at fixed σ₀/m forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ — collective momentum-space behavior and classical particles are mutually exclusive" ([#11 §9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) (i)), N_occ being the occupation number. Flag 19 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) notes that calc note [#2](../../notes/stream-stability.md) evaluates this corollary with its broad-gate formula at Milky Way conditions, which it treats elsewhere as narrow-gate; N_occ ≫ 1 either way, so the conclusion stands. The discriminant asks which of the two the data favour.

## The two laws

Calc note [#3](../../notes/wave-island.md) states the discriminant as the first of two corollaries of its condensation rate, "before any numbers" ([`notes/wave-island.md`](../../notes/wave-island.md), 'The rate'; quotations from the clumping notes on this page are transcribed from their LaTeX):

> "**Island discriminant.** The velocity suppression of self-interaction effects is e^{−v²/v\*²} on the particle island but (v\*/σ)⁴ on the wave island. The cliff's *sharpness* distinguishes the islands observationally."

### The particle side

On the particle island the suppression is the gate's own tail. The amplitude M(k,q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²) carries a gate factor F in the incoming relative momentum k ([#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate); [the velocity gate](../dark-matter/conjugate-matter/velocity-gate.md#the-amplitude)), and the [transfer cross-section](../dark-matter/halo-astrophysics/transfer-cross-section.md) follows as σ_T(v) = σ₀F(v²/v\*²). Every collision faster than v\* is cut off by F itself. With the lab notebook's Gaussian gate the cutoff is e^{−v²/v\*²}, the form calc note #3 quotes; the [lab notebook](../history/documents/lab-notebook.md) called it "An exponential cliff, not a power-law tail" ([#1 §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d), transcribed from its LaTeX).

### The wave side

On the wave island two-body scattering is not the right observable, and the self-interaction acts through wave kinetics: waves scatter off one another with a rate multiplied by the occupation number, and power collects at low relative momenta ([wave kinetics](../dark-matter/wave-dark-matter/wave-kinetics.md)). Calc note #3 computed that rate for the gated attraction ([the gated condensation rate](../dark-matter/momentum-clumping/wave-island/condensation-rate.md#the-rate)), tagged [D, heuristic coefficients]:

```text
Γ_self ≈ c · g²ρ² min(σ, v*)⁴ / (m³σ⁶),      c = O(5–15)
```

with g the gated coupling, ρ the halo's density, σ its velocity dispersion and m the χ mass. The two regimes: "Gate-open (σ ≲ v\*): Γ ≈ c g²ρ²/(m³σ²). Gate-narrow: suppressed by (v\*/σ)⁴ — **a power law, not an exponential**." In a halo hotter than the gate, the gate removes most scattering partners but leaves those moving within about v\* of each other, and that co-moving fraction shrinks only as a power of v\*/σ ([where the powers come from](../dark-matter/momentum-clumping/wave-island/condensation-rate.md#where-the-powers-come-from), a reading the wiki gives and the note does not write out). The "self-interaction effects" on this side are of this kinetic kind: calc note #3 calls Γ_self "the analog of SIDM heat transport (kinetic relaxation redistributes energy through the halo)" ('What pins g? Two scenarios'), SIDM being [self-interacting dark matter](../dark-matter/halo-astrophysics/self-interacting-dark-matter.md).

### Reading the knee

The two laws describe how the effects of self-interaction fall off above the gate velocity: steeply for particles, as a power law for waves. The row compresses this into "Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave". It reads the tail of the knee that [row 1](self-interaction-knee.md) requires, an observable that row 1 states "across halo masses", that is, across halos of different internal speeds.

## Where it came from

The discriminant was salvaged from the calculations that tested velocity clumping, the program's founding image and P.R.'s open conjecture [O] ([#11 §9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested); [Conjecture: velocity clumping, the founding image](../dark-matter/momentum-clumping/founding-image.md)).

1. **Calc note #2.** On the wave island "a cliff-analog survives as (v\*/σ)³ suppression rather than an exponential" ([`notes/stream-stability.md`](../../notes/stream-stability.md), 'Consequences for the predictions table'), a first estimate.
2. **Calc note #3.** The rate above, with corollary 1. Its standing results: "Wave island: collective phenomena live but tunable, except Scenario A's mandatory UFD signature; cliff softens to (v\*/σ)⁴", UFD meaning [ultra-faint dwarf](../dark-matter/halo-astrophysics/dwarf-galaxies.md). Scenario A, "the committed-wave case" of [#11 §9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)'s wave-island result, is under review ([Under review: Scenario A and the ultra-faint-dwarf endpoint](../dark-matter/momentum-clumping/wave-island/scenario-a.md)).
3. **The v0.2 addendum.** With [the net theorem](../dark-matter/momentum-clumping/net-theorem.md), old rows 3 and 4 were withdrawn ([velocity-space granularity in halos](../dark-matter/momentum-clumping/velocity-granularity.md) and [Fornax friction suppression](../dark-matter/momentum-clumping/fornax-friction.md), both under review) and "A new row replaces them: **cliff-sharpness island discriminant** — self-interaction suppression is e^{−v²/v\*²} for particle χ but (v\*/σ)⁴ for wave χ, so the measured shape of the SIDM knee identifies the island" (#1 'Addendum (v0.2, after the clumping notes)', transcribed from its LaTeX).
4. **Calc note [#4](../../notes/ufd-endpoint.md).** The closing note lists "the cliff-sharpness **island discriminant** (exponential vs (v\*/σ)⁴)" among what "remains distinctively BBT's own", BBT being Broken-Born theory, the program's earlier name ('Verdict and closure of the clumping problem').
5. **v1.** "Salvage: the **island discriminant** — self-interaction suppression is a sharp knee for particle χ but (v\*/σ)⁴ for wave χ, so the knee's *shape* identifies dark matter's fundamental nature" ([#9 §7 item 3](../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative)), and row 3 of v1's table.
6. **#11.** "Salvage: the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island" ([§9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)), and row 3 of [§13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions).

The row took the place of the two withdrawn rows in the table's numbering; the renumbering is on [the history of the predictions table](table-history.md).

## Its standing in the assessment

[#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) counts "predictions not previously posed (rows 3, 11)" among the program's progressive signs, in the vocabulary of [Lakatos's methodology](../method/lakatosian-methodology.md), and its plain-language passage lists "one new experimental question (the knee-shape discriminant)" among what the program has produced. v1's assessment had said the same: "plus one new experimental question (the knee-shape island discriminant)" ([#9 §11](../../notes/broken-born-program-v1.md#11-assessment)). [The handoff](../history/documents/handoff.md) records it among the live results as "knee-tail shape = particle-vs-wave 'island discriminant' (new observable)" ([`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen)). The popular article [#12](../../popsci/universes-other-half.md) states it in plain terms: "the sharpness of that knee differs according to whether dark matter is a gas of particles or a coherent quantum wave, so the knee's measured shape identifies which it is" ('Dark matter as the other polarization'; [the popular articles](../history/documents/popular-articles.md)).

The same §15 lists "gate tail not yet forced" among the degeneration risks. That item bears on this row's particle side (below).

## The data situation

No source records a measurement of the knee's tail, and no source names a survey or a set of halos that would read it. [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) names rows 1, 4 and 7 as the near-term falsification exposure; row 3, a diagnostic, is not among them. In this wiki's reading, since the row reads the tail of row 1's knee, it has nothing to read until the knee itself is found.

## Caveats and open questions

- **The particle side assumes a sharp tail.** The e^{−v²/v\*²} of the clumping notes is the lab notebook's postulated Gaussian gate. [Calc note #6](../history/documents/field-equation-notes.md) then found that "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" ([`notes/x-classification.md` §4](../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)), and the v0.4 addendum made the tail "Gaussian vs rational" (#1 'Addendum (v0.4)'). [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) keeps that open: "tail (Gaussian vs rational) diagnoses the vertex completion". The gate's shape is item 4 of [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems) ([Open: the gate shape (OP4)](../dark-matter/conjugate-matter/gate-shape.md#why-it-is-observable)). The row's "sharp ⇒ particle" holds for the Gaussian case. If the particle gate is rational, both branches have power-law tails, and no source compares the two power laws or says whether the discriminant survives.
- **Whether the discriminant survives.** [`notes/gate-mechanism.md`](../../notes/gate-mechanism.md) lists it as open [O]: "Row 3's island discriminant reads a sharp tail as particle χ and a (v\*/σ)⁴ tail as wave χ. Under reading R1 the particle tail is a power law, the same functional class as the wave island's. Whether the discriminant survives is open" ([§5](../../notes/gate-mechanism.md#5-what-follows-for-the-record)). Reading R1 is the note's reconstruction of [#6 §4](../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)'s fiber overlap as an ordinary position-local potential of range ħ/μ, whose cross-section tails are power laws even for Gaussian profiles ([§3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural); one derivation; [the fiber overlap, read two ways](../dark-matter/conjugate-matter/gate-mechanism.md#the-fiber-overlap-read-two-ways)). The other reading, R2, a pair-channel interaction, falls faster than any power of k but contains no X ([§3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural); one derivation). The note also places the record's rational gates in [row 1](self-interaction-knee.md)'s standard-expectation column, a light mediator's knee with a power-law tail ([§3](../../notes/x-classification.md#3-the-mass-mechanism-and-the-endpoint-d--structural)). Flag 55 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) is pending.
- **Two different variables.** The particle law is written in the collision speed v, the wave law in the halo's dispersion σ. The sources do not convert one into the other or say how a measured knee would be compared with each.
- **An uncalibrated coefficient.** The rate's coefficient c is "heuristic at O(1)–O(10) level", awaiting calibration against Levkov–Panin–Tkachev numerics (calc note #3, header; [Open: calibration of the coefficient c](../dark-matter/momentum-clumping/wave-island/condensation-rate.md#open-calibration-of-the-coefficient-c)); [#11 §9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) marks the coefficients [O].
- **Rows 1 and 2 in wave language.** Calc note #2 asked that "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)". The (v\*/σ)⁴ law answers this for the knee's tail only ([Open: rows 1 and 2 in wave language](../dark-matter/momentum-clumping/wave-island/condensation-rate.md#open-rows-1-and-2-in-wave-language)).
- **The X-condensate.** [#11 §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) gives [the X-condensate](../dark-matter/candidates/x-condensate.md) the handle "knee shape wave-like" and [χ particles](../dark-matter/candidates/chi-particles.md) "knee at v\*, sharp tail". The (v\*/σ)⁴ law was derived for wave χ; no document derives a knee for a condensate of X or relates it to wave χ.

## Where the row is used

Rows 1–3 are the discriminators of [row 11, particles or condensate](dark-sector-microstructure.md): "Particles vs condensate, separable via rows 1–3 + coherence signatures" ([#11 §13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)), which is open problem 9 of [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems). The companion rows are [row 1, the knee](self-interaction-knee.md), whose tail this row reads, and [row 2, isotropy](scattering-isotropy.md), which holds on the particle island.

## Superseded: the exponential and the cube

Two parts of the clumping statement have been replaced.

- **"Exponential vs (v\*/σ)⁴".** The clumping notes and the v0.2 addendum set an exponential particle side against the wave law and called the row the "cliff-sharpness" discriminant. Since the v0.4 addendum the particle side has been a knee whose tail is open. Both v1 and #11 write "sharp" instead of "exponential" ([#9 §7](../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative); [#11 §9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested), [§13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)).
- **(v\*/σ)³.** Calc note #2's first estimate of the wave-side suppression was the third power. Calc notes #3 and #4, v1 and #11 use the fourth, and the fourth governs ([Superseded: the cubic suppression of calc note #2](../dark-matter/momentum-clumping/wave-island/condensation-rate.md#superseded-the-cubic-suppression-of-calc-note-2)).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §13 row 3](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the row; [§9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the salvage, the classicality theorem and the rate's tags, the founding image as P.R.'s open conjecture, and Scenario A, "the committed-wave case", under review; [§8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the open tail and the mechanism's tag; [§12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — the candidates' handles; [§14 item 4](../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open gate shape; [§15](../papers/broken-born-checkpoint-v2.md#15-assessment) — "not previously posed", the new experimental question and "gate tail not yet forced"; [§13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the withdrawn rows, under review
- [`notes/wave-island.md`](../../notes/wave-island.md) 'The rate' — the rate, the (v\*/σ)⁴ suppression and corollary 1; 'What pins g? Two scenarios' — the rate as the analog of SIDM heat transport; 'Standing results after Chunks A+B' — "cliff softens to (v\*/σ)⁴"
- [`notes/ufd-endpoint.md`](../../notes/ufd-endpoint.md) 'Verdict and closure of the clumping problem' — the surviving wave island and the discriminant among the surviving content
- [`notes/stream-stability.md`](../../notes/stream-stability.md) 'Consequences for the predictions table' — the first (v\*/σ)³ estimate and the rows 1–2 to-do
- [`notes/x-classification.md` §4](../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — rational, power-law-tailed gates
- [`notes/broken-born-theory.md`](../../notes/broken-born-theory.md) 'Addendum (v0.2, after the clumping notes)' — the discriminant as the replacement row; 'Addendum (v0.4)' — the tail made open
- [`notes/broken-born-program-v1.md` §7](../../notes/broken-born-program-v1.md#7-the-death-of-momentum-clumping-the-clumping-problem-closed-negative), [§9](../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions), [§11](../../notes/broken-born-program-v1.md#11-assessment) — v1's salvage, row 3 and assessment
- [`HANDOFF.md` §2](../../HANDOFF.md#2-scientific-state-one-screen) — "new observable"
- [`popsci/universes-other-half.md`](../../popsci/universes-other-half.md) 'Dark matter as the other polarization' — the popular statement
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 19 — the regime in which calc note #2 evaluates the classicality corollary; conclusion unchanged; item 55 — the gate's mechanism not derived, and whether row 3 survives; pending
- [`notes/gate-mechanism.md` §5](../../notes/gate-mechanism.md#5-what-follows-for-the-record) — whether the discriminant survives under reading R1, open; [§3](../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways) — readings R1 and R2 and their tails, the rational gates as the standard expectation
