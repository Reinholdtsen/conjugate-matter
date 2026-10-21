---
title: "Row 3: the island discriminant"
weight: 40
status: alive
description: "The knee's tail tells particles from waves — a sharp cutoff for particle χ, a (v*/σ)⁴ power law for wave χ: a diagnostic salvaged from Debt 3, with open caveats on its particle side."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 3"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3b-wave-island.md 'Standing results after Chunks A+B'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure of Debt 3'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §7"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-program-v1.md §11"
  - "HANDOFF.md §2"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*The island discriminant is a proposed way to read from astronomical data whether dark matter is made of particles or of a classical wave field. The program's gated self-interaction weakens above the gate velocity v\* in both cases, but differently: for particles the cutoff is sharp, while for a wave field it falls off only as a power law, (v\*/σ)⁴, where σ is the velocity dispersion of the halo. The program calls the two regimes the particle island and the wave island, and the shape of the knee in the self-interaction strength, the subject of [row 1](/wiki/predictions/self-interaction-knee), would say which one dark matter occupies. The diagnostic came out of the calculation that killed velocity clumping (Debt 3). #11 counts it among its predictions not previously posed, and it selects a branch rather than killing the program. Its particle side assumes a sharp tail, which the program now treats as open.*

**Status:** Alive, as a diagnostic — [D] — a corollary of the wave-island condensation rate in calc note #3 (`notes/debt3b-wave-island.md`, where the rate is tagged [D, heuristic coefficients]), carried in #11 §9's wave-island result [D + T] and stated as row 3 of #11 §13; not machine-checked. Its particle side assumes a sharp tail, while the tail's shape is open [O] (#11 §14 item 4). No source records a test.

## The row

[Checkpoint #11](/wiki/history/documents/checkpoint) §13, row 3:

| Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- |
| **Island discriminant** | (not previously posed) | Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave | Diagnostic — selects the branch (particle vs wave χ) |

Two columns differ from the other rows. There is no standard expectation, because the question had not been asked: v1 wrote "— (question not previously posed)" (#9 §9). And there is no kill condition. Whatever shape the tail has, the row assigns dark matter to one branch or the other; it is "Diagnostic, not a kill: identifies the branch" in v1's words (#9 §9).

## The two islands

The row's two branches are the two regimes that Debt 3 found for [conjugate matter χ](/wiki/dark-matter/conjugate-matter), separated by mass ([the Debt-3 calc notes](/wiki/history/documents/debt-3-notes)).

- **The particle island.** Heavy χ, of MeV to GeV mass, is a gas of classical particles. Its self-interaction acts collision by collision, through the two-body cross-section of [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law). This is the home of [the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) ([the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem#the-particle-island)).
- **The wave island.** Very light χ has so many quanta in each quantum state that the halo behaves as a classical wave field ([occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number)). After Debt 3, "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings" (`notes/debt3c-ufd-endpoint.md`; [the wave island](/wiki/dark-matter/momentum-clumping/wave-island)).

[The classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem) explains why there are two islands rather than one continuum of behaviour: satisfying the criterion for collective behaviour "at fixed σ₀/m forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ — collective momentum-space behavior and classical particles are mutually exclusive" (#11 §9 (i)), N_occ being the occupation number. The discriminant asks which of the two the data favour.

## The two laws

Calc note #3 states the discriminant as the first of two corollaries of its condensation rate, "before any numbers" (`notes/debt3b-wave-island.md`, 'The rate'; quotations from the Debt-3 notes on this page are transcribed from their LaTeX):

> "**Island discriminant.** The velocity suppression of self-interaction effects is e^{−v²/v\*²} on the particle island but (v\*/σ)⁴ on the wave island. The cliff's *sharpness* distinguishes the islands observationally."

### The particle side

On the particle island the suppression is the gate's own tail. The amplitude M(k,q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²) carries a gate factor F in the incoming relative momentum k (#11 §8; [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate#the-amplitude)), and the cross-section follows as σ_T(v) = σ₀F(v²/v\*²). Every collision faster than v\* is cut off by F itself. With the lab notebook's Gaussian gate the cutoff is e^{−v²/v\*²}, the form calc note #3 quotes; the [lab notebook](/wiki/history/documents/lab-notebook) called it "An exponential cliff, not a power-law tail" (#1 §5.1, transcribed from its LaTeX).

### The wave side

On the wave island two-body scattering is not the right observable, and the self-interaction acts through wave kinetics: waves scatter off one another with a rate multiplied by the occupation number, and power collects at low relative momenta ([wave kinetics](/wiki/dark-matter/wave-dark-matter/wave-kinetics)). Calc note #3 computed that rate for the gated attraction ([the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#the-rate)), tagged [D, heuristic coefficients]:

```text
Γ_self ≈ c · g²ρ² min(σ, v*)⁴ / (m³σ⁶),      c = O(5–15)
```

with g the gated coupling, ρ the halo's density, σ its velocity dispersion and m the χ mass. The two regimes: "Gate-open (σ ≲ v\*): Γ ≈ c g²ρ²/(m³σ²). Gate-narrow: suppressed by (v\*/σ)⁴ — **a power law, not an exponential**." In a halo hotter than the gate, the gate removes most scattering partners but leaves those moving within about v\* of each other, and that co-moving fraction shrinks only as a power of v\*/σ ([where the powers come from](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#where-the-powers-come-from), a reading the wiki gives and the note does not write out). The "self-interaction effects" on this side are of this kinetic kind: calc note #3 calls Γ_self "the analog of SIDM heat transport (kinetic relaxation redistributes energy through the halo)" ('What pins g? Two scenarios'), SIDM being [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter).

### Reading the knee

The two laws describe how the effects of self-interaction fall off above the gate velocity: steeply for particles, as a power law for waves. The row compresses this into "Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave". It reads the tail of the knee that [row 1](/wiki/predictions/self-interaction-knee) requires, an observable that row 1 states "across halo masses", that is, across halos of different internal speeds.

## Where it came from

The discriminant was salvaged from the calculation that killed velocity clumping, the program's founding image ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)).

1. **Calc note #2 (Debt 3a).** On the wave island "a cliff-analog survives as (v\*/σ)³ suppression rather than an exponential" (`notes/debt3a-stream-stability.md`, 'Consequences for the predictions table'), a first estimate.
2. **Calc note #3 (Debt 3b).** The rate above, with corollary 1. Its standing results: "Wave island: collective phenomena live but tunable, except Scenario A's mandatory UFD signature; cliff softens to (v\*/σ)⁴", UFD meaning ultra-faint dwarf.
3. **The v0.2 addendum.** With [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem), old rows 3 and 4 were withdrawn and "A new row replaces them: **cliff-sharpness island discriminant** — self-interaction suppression is e^{−v²/v\*²} for particle χ but (v\*/σ)⁴ for wave χ, so the measured shape of the SIDM knee identifies the island" (#1 'Addendum (v0.2, post Debt-3)', transcribed from its LaTeX).
4. **Calc note #4 (Debt 3c).** The closing note lists "the cliff-sharpness **island discriminant** (exponential vs (v\*/σ)⁴)" among what "remains distinctively BBT's own", BBT being Broken-Born Theory, the notes' name for the framework ('Verdict and closure of Debt 3').
5. **v1.** "Salvage: the **island discriminant** — self-interaction suppression is a sharp knee for particle χ but (v\*/σ)⁴ for wave χ, so the knee's *shape* identifies dark matter's fundamental nature" (#9 §7 item 3), and row 3 of v1's table.
6. **#11.** "Salvage: the **island discriminant** (knee shape: sharp cutoff ⇒ particle χ; (v\*/σ)⁴ ⇒ wave χ) and free relic abundance via misalignment on the wave island" (§9), and row 3 of §13.

The row took the place of the two withdrawn rows in the table's numbering; the renumbering is on [the history of the predictions table](/wiki/predictions/table-history).

## Its standing in the assessment

#11 §15 counts "predictions not previously posed (rows 3, 11)" among the program's progressive signs, in the vocabulary of [Lakatos's methodology](/wiki/method/lakatosian-methodology), and its plain-language passage lists "one new experimental question (the knee-shape discriminant)" among what the program has produced. v1's assessment had said the same: "plus one new experimental question (the knee-shape island discriminant)" (#9 §11). [The handoff](/wiki/history/documents/handoff) records it among the live results as "knee-tail shape = particle-vs-wave 'island discriminant' (new observable)" (`HANDOFF.md` §2). The popular article #12 states it in plain terms: "the sharpness of that knee differs according to whether dark matter is a gas of particles or a coherent quantum wave, so the knee's measured shape identifies which it is" ('Dark matter as the other polarization'; [the popular articles](/wiki/history/documents/popular-articles)).

The same §15 lists "gate tail not yet forced" among the degeneration risks. That item bears on this row's particle side (below).

## The data situation

No source records a measurement of the knee's tail, and no source names a survey or a set of halos that would read it. #11 §15 names rows 1, 4 and 7 as the near-term falsification exposure; row 3, a diagnostic, is not among them. In this wiki's reading, since the row reads the tail of row 1's knee, it has nothing to read until the knee itself is found.

## Caveats and open questions

- **The particle side assumes a sharp tail.** The e^{−v²/v\*²} of the Debt-3 notes is the lab notebook's postulated Gaussian gate. Calc note #6 then found that "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" (`notes/debt1a-ii-X-classification.md` §4), and the v0.4 addendum made the tail "Gaussian vs rational" (#1 'Addendum (v0.4)'). #11 §8 keeps that open: "tail (Gaussian vs rational) diagnoses the vertex completion". The gate's shape is item 4 of #11 §14 ([Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape#why-it-is-observable)). The row's "sharp ⇒ particle" holds for the Gaussian case. If the particle gate is rational, both branches have power-law tails, and no source compares the two power laws or says whether the discriminant survives.
- **Two different variables.** The particle law is written in the collision speed v, the wave law in the halo's dispersion σ. The sources do not convert one into the other or say how a measured knee would be compared with each.
- **An uncalibrated coefficient.** The rate's coefficient c is "heuristic at O(1)–O(10) level", awaiting calibration against Levkov–Panin–Tkachev numerics (calc note #3, header; [Open: calibration of the coefficient c](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#open-calibration-of-the-coefficient-c)); #11 §9 marks the coefficients [O].
- **Rows 1 and 2 in wave language.** Calc note #2 asked that "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)". The (v\*/σ)⁴ law answers this for the knee's tail only ([Open: rows 1 and 2 in wave language](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#open-rows-1-and-2-in-wave-language)).
- **The X-condensate.** #11 §12 gives [the X-condensate](/wiki/dark-matter/candidates/x-condensate) the handle "knee shape wave-like" and [χ particles](/wiki/dark-matter/candidates/chi-particles) "knee at v\*, sharp tail". The (v\*/σ)⁴ law was derived for wave χ; no document derives a knee for a condensate of X or relates it to wave χ.

## Where the row is used

Rows 1–3 are the discriminators of [row 11, particles or condensate](/wiki/predictions/dark-sector-microstructure): "Particles vs condensate, separable via rows 1–3 + coherence signatures" (#11 §13), which is open problem 9 of #11 §14. The companion rows are [row 1, the knee](/wiki/predictions/self-interaction-knee), whose tail this row reads, and [row 2, isotropy](/wiki/predictions/scattering-isotropy), which holds on the particle island.

## Superseded: the exponential and the cube

Two parts of the Debt-3 statement have been replaced.

- **"Exponential vs (v\*/σ)⁴".** The Debt-3 notes and the v0.2 addendum set an exponential particle side against the wave law and called the row the "cliff-sharpness" discriminant. Since the v0.4 addendum the particle side is a knee whose tail is open, and v1 and #11 write "sharp" instead of "exponential" (#9 §7; #11 §9, §13).
- **(v\*/σ)³.** Calc note #2's first estimate of the wave-side suppression was the third power. Calc notes #3 and #4, v1 and #11 use the fourth, and the fourth governs ([Superseded: the cubic suppression of Debt 3a](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#superseded-the-cubic-suppression-of-debt-3a)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 3 — the row; §9 — the salvage, the classicality theorem and the rate's tags; §8 — the open tail; §12 — the candidates' handles; §14 item 4 — the open gate shape; §15 — "not previously posed", the new experimental question and "gate tail not yet forced"
- `notes/debt3b-wave-island.md` 'The rate' — the rate, the (v\*/σ)⁴ suppression and corollary 1; 'What pins g? Two scenarios' — the rate as the analog of SIDM heat transport; 'Standing results after Chunks A+B' — "cliff softens to (v\*/σ)⁴"
- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — the surviving wave island and the discriminant among the surviving content
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — the first (v\*/σ)³ estimate and the rows 1–2 to-do
- `notes/debt1a-ii-X-classification.md` §4 — rational, power-law-tailed gates
- `notes/broken-born-theory.md` 'Addendum (v0.2, post Debt-3)' — the discriminant as the replacement row; 'Addendum (v0.4)' — the tail made open
- `notes/broken-born-program-v1.md` §7, §9, §11 — v1's salvage, row 3 and assessment
- `HANDOFF.md` §2 — "new observable"
- `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the popular statement
