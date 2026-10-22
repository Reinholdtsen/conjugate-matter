---
title: "The gated scattering law σ_T(v)"
weight: 40
status: alive
description: "σ_T(v) = σ₀F(v²/v*²): strong in slow dwarfs, off in fast clusters, isotropic below the gate; from v0.1's exponential cliff to the current knee, whose tail diagnoses the vertex."
provenance: [D, O]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §13 rows 1–3"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-program-v1.md §9"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3c-ufd-endpoint.md 'Verdict and closure of Debt 3'"
  - "popsci/universes-other-half.md"
  - "papers/conjugate-special-relativity.md §4"
  - "review/wiki-build-flags.md item 17"
---

*The gated scattering law gives the [momentum-transfer cross-section σ_T](/wiki/dark-matter/halo-astrophysics/transfer-cross-section) of [conjugate matter](/wiki/dark-matter/conjugate-matter), the measure of how strongly its particles scatter off one another, as a function of the relative velocity v of a colliding pair. Because [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) turns the interaction off at large relative velocity, self-scattering is strong in [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies), where dark matter moves at tens of kilometres per second, and absent in galaxy clusters, where it moves at thousands; between the two, σ_T bends down at a knee near the gate velocity v\*. Below the knee the scattering goes equally in all directions, unlike the forward-peaked scattering of the usual models with a light force carrier. The lab notebook first derived a sharp exponential cliff at v\*; once the gate's mechanism was found, the program kept only the knee, and the shape of its tail became an open question that observations could answer.*

**Status:** Alive — [D], with the shape [O] (`papers/broken-born-checkpoint-v2.md` §8) — derived in the Born approximation in the lab notebook (#1 §5.1) and downgraded from cliff to knee in calc note #6 §4 ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)); not machine-checked. The v0.1 exponential cliff is superseded. The law is tested by [row 1](/wiki/predictions/self-interaction-knee) and [row 2](/wiki/predictions/scattering-isotropy) of [the predictions table](/wiki/predictions) and read by [row 3](/wiki/predictions/island-discriminant).

## The law

[The checkpoint](/wiki/history/documents/checkpoint), #11, states it in one sentence of §8:

> "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking."

```text
σ_T(v) = σ₀ · F(v²/v*²)
```

- **σ₀** is the cross-section at low velocity, below the gate. Its value is fixed by the cores of dwarf galaxies at [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark).
- **F** is the gate function of the amplitude M(k, q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²), now written in the relative velocity. Its shape is open ([Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape)).
- **v\*** is the gate velocity, where the knee sits. [The lab notebook](/wiki/history/documents/lab-notebook) defines it as v\* ≡ √2μ/m_χ, with μ the gate's momentum scale and m_χ the mass of a χ particle (#1 §5.1). #11 does not restate the definition; the paper on [conjugate special relativity](/wiki/conjugate-relativity) uses it (#13 §4; [the invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell)). The definition belongs to v0.1's gate e^{−k²/μ²}; a suspected factor of √2 in μ between that gate and calc note #6's overlap form, which matters once μ is read as the fiber width, is recorded for a ruling in `review/wiki-build-flags.md` item 17 ([two conventions](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)). The flag notes that no stated number changes; this page quotes the sources as written.

Three claims are packed into the sentence: a knee whose existence and location are robust; a tail whose shape is open and diagnostic; and isotropy below the gate.

## Background: the transfer cross-section [T]

Dark-matter self-scattering is measured by the momentum-transfer cross-section,

```text
σ_T = ∫ dΩ (1 − cos θ) dσ/dΩ
```

which weights each collision by the fraction of forward momentum it removes. A grazing collision at small angle θ counts for little and a head-on rebound counts fully. This is the quantity that controls how fast scattering carries heat through a halo, and it is quoted per unit mass, σ_T/m, usually in cm²/g [T]. In the Born approximation the differential cross-section dσ/dΩ is proportional to the square of the amplitude [T].

For [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) (SIDM) with a light mediator, the [Yukawa factor](/wiki/gravity/spin-2-fields/yukawa-forces#the-same-law-in-momentum-t) 1/(q² + m_φ²) is large at small transfer q, so scattering is concentrated at small angles, forward-peaked, and the cross-section falls as the velocity rises: "Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction" (#1 §5.1). For cold dark matter (CDM) there is no self-scattering at all. These are the two standard expectations against which [row 1](/wiki/predictions/self-interaction-knee) is set: "CDM none; Yukawa SIDM power-law + Coulomb log" (#11 §13).

## How the lab notebook derived it

The law first appears in the lab notebook's v0.1, as a boxed result of §5.1, tagged [D]:

> "In Born approximation with a heavy transfer mediator (m_φ ≳ m_χ, contact-like in x), the momentum-transfer cross-section from the boxed amplitude is"

```text
σ_T(v) = σ₀ e^{−v²/v*²},   v* ≡ √2 μ/m_χ,   σ₀ = 16πα̃²m_χ²/m_φ⁴
```

The boxed amplitude is the v0.1 one, with the Gaussian gate e^{−k²/μ²} and k = m_χv_rel/2 (#1 §3). The notebook gives the result without intermediate steps. Two features of it can be read off the amplitude [T]:

- **The flat part.** For slow particles the transfer q is at most 2k = m_χv, far below m_χ; with m_φ ≳ m_χ the factor 1/(q² + m_φ²) is then nearly the constant 1/m_φ². The interaction is contact-like in position, and the amplitude depends on the scattering angle only weakly, through q; the gate depends on k, which the collision energy fixes, not on the angle. σ₀ collects the constants, including 1/m_φ⁴ from the squared propagator.
- **The gate, squared.** The cross-section involves the square of the amplitude, so the gate enters squared. The definition v\* ≡ √2μ/m_χ is the one for which the squared Gaussian gate, e^{−2k²/μ²} with k = m_χv/2, reads e^{−v²/v\*²}.

The notebook adds a caveat on the Born approximation at the benchmark coupling: "At α̃ ~ 1 the Born approximation is marginal (expect O(1) corrections); the *shape* claims above survive because they follow from the k- vs q-dependence, not from the coupling strength" (#1 §5.1).

## The two signatures

The lab notebook lists "Two structural signatures" that distinguish the law "from *every* x-local mediator model" (#1 §5.1), x-local meaning local in position:

1. "**An exponential cliff, not a power-law tail.** Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction; BBT falls off a cliff at v\*. The discriminating band is v ~ 150–400 km/s (large spirals, small groups), where the two shapes diverge by orders of magnitude." BBT is the notebook's name for the framework, Broken-Born Theory.
2. "**Isotropy inside the gate.** Because the gate depends on k and the contact part is flat in q, scattering below v\* is isotropic; light-mediator Yukawa scattering is forward-peaked. Energy- vs momentum-transport efficiencies differ, which feeds into halo relaxation morphology."

The first signature was weakened when the gate's mechanism was derived (below); the band of 150–400 km/s survives in the kill condition of row 1. The second survives unchanged as [row 2](/wiki/predictions/scattering-isotropy). Its argument assumes a heavy mediator, since "the contact part is flat in q" only when m_φ is large compared with the transfers.

## The downgrade to a knee

Calc note #6 derived the gate from exchange of the [momentum graviton X](/wiki/gravity/momentum-graviton) over the overlap of the χ quanta's momentum-space wavepackets ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). A Gaussian gate then requires a Gaussian profile, and generic vertices give rational, power-law-tailed gates. The note draws the consequence for the scattering law, a downgrade of the flagship row:

> "**row 1's 'exponential cliff' weakens to 'sharp knee at v\*, with the tail shape (Gaussian vs rational) a diagnostic of the vertex completion.'** The knee's existence and location are robust; its steepness is model-internal information, not a guaranteed exponential." (`notes/debt1a-ii-X-classification.md` §4; the note writes v_\* for v\*)

The lab notebook's v0.4 addendum records the amendment: "the exponential cliff weakens to a *sharp knee at v_\* with tail shape (Gaussian vs rational) diagnosing the vertex completion*; the knee's existence and location remain the robust prediction" (#1 'Addendum (v0.4)'). The knee's existence follows from the gate depending on k, whatever F is; the location is set by μ. What changed is that the steepness, which v0.1 took from the assumed Gaussian, is no longer a prediction.

Row 1 changed with it, from the lab notebook's table (#1 §9) to v1 (#9 §9) and the checkpoint (#11 §13):

| | #1 §9 (v0.1) | #11 §13 |
| --- | --- | --- |
| Requirement | "σ₀ e^{−v²/v\*²}: cliff at v\* ∼ 120 km/s; **exactly zero in clusters forever**" | "Knee at v\* ~ 10² km/s; zero cluster signal (particle χ)" |
| Killed by | "Robust nonzero self-interaction at v > 3v\*; or cliff-shape excluded in the 150–400 km/s band" | "Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band" |

v1 (#9 §9) already reads "Knee at v\* ~ 10² km/s; tail shape = vertex diagnostic; zero cluster signal (particle χ)". The history of the whole table is on [the history of the predictions table](/wiki/predictions/table-history).

## The tests

The checkpoint's predictions table (#11 §13) has three rows on this law:

- **Row 1, the knee.** "σ_T(v) across halo masses": requirement "Knee at v\* ~ 10² km/s; zero cluster signal (particle χ)"; killed by "Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band". #11 §15 lists row 1, with rows 4 and 7, as the program's near-term falsification exposure. See [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee).
- **Row 2, isotropy [D].** "Scattering anisotropy": standard expectation "Forward-peaked (light mediators)"; requirement "Isotropic below the gate"; killed by "Morphology demanding forward peaking". See [Row 2: isotropic scattering below the gate](/wiki/predictions/scattering-isotropy).
- **Row 3, the island discriminant.** "Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave", a diagnostic that selects between particle and wave χ rather than a kill condition. See [Row 3: the island discriminant](/wiki/predictions/island-discriminant).

In #11's comparison of the two remaining dark-matter candidates, [χ particles](/wiki/dark-matter/candidates/chi-particles) carry "knee at v\*, sharp tail; isotropic scattering; permanent direct-detection null", and [the X-condensate](/wiki/dark-matter/candidates/x-condensate) carries "knee shape wave-like" (#11 §12). The popular article #12 describes the knee and the smoothing of dwarf-galaxy cusps in the present tense, as if observed; in the program's documents the core fit is the input that fixes σ₀, and the knee is a prediction ([the popular articles](/wiki/history/documents/popular-articles)).

## On the wave island

The law above is a two-body cross-section for classical particles. The Debt-3 calculations found that collective effects of the gated attraction can exist only if χ is light enough to behave as a classical wave, on what the notes call the [wave island](/wiki/dark-matter/momentum-clumping/wave-island) ([the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem)). There the velocity dependence takes a different form.

- **Calc note #2** (Debt 3a, the first of [the Debt-3 calc notes](/wiki/history/documents/debt-3-notes)): on the particle island, "Rows 1–2 (exponential cliff, isotropy) **survive** — they are collisional"; on the wave island, "a cliff-analog survives as (v\*/σ)³ suppression rather than an exponential. Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)" (`notes/debt3a-stream-stability.md`). Here σ is the velocity dispersion of the halo.
- **Calc note #3** (Debt 3b): the [gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate), when the gate is narrow, is "suppressed by (v\*/σ)⁴ — **a power law, not an exponential**", and "The velocity suppression of self-interaction effects is e^{−v²/v\*²} on the particle island but (v\*/σ)⁴ on the wave island. The cliff's *sharpness* distinguishes the islands observationally" (`notes/debt3b-wave-island.md`, 'The rate').
- **Calc note #4** (Debt 3c) lists among what remains "distinctively BBT's own" "the exponential cliff + in-gate isotropy (particle island)" and "the cliff-sharpness **island discriminant** (exponential vs (v\*/σ)⁴)" (`notes/debt3c-ufd-endpoint.md`).

The Debt-3 notes were written before the Debt-1 notes and so still speak of an exponential cliff. The fourth power of calc notes #3 and #4 is the one #11 uses; calc note #2's third power was a first estimate ([conflicts between sources](/wiki/history/documents/source-conflicts)). The re-derivation of rows 1–2 in wave language that calc note #2 called for is answered only in part by the (v\*/σ)⁴ law; no document restates isotropy for waves. That to-do belongs with [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate).

## What is open

- **The tail.** Whether F is Gaussian or rational is item 4 of #11 §14; #11 §15 counts "gate tail not yet forced" among the program's [degeneration risks](/wiki/program/assessment). See [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape).
- **The particle side of the discriminant.** Row 3 reads a sharp tail as particle χ. Calc note #6 calls the rational gates power-law-tailed, and the wave-island suppression is also a power law; no source compares the two or says whether the discriminant survives a rational tail for particles.
- **The strength.** Why σ₀ is as large as dwarf cores require while ordinary matter couples to X only at gravitational strength is [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).

## Superseded: the exponential cliff of v0.1

In v0.1 the law was σ_T(v) = σ₀e^{−v²/v\*²}, "An exponential cliff, not a power-law tail" (#1 §5.1). It rested on the postulated Gaussian gate, and the lab notebook drew its sharpest predictions from it:

- the v0.1 row 1, "cliff at v\* ∼ 120 km/s; **exactly zero in clusters forever**", killed by "Robust nonzero self-interaction at v > 3v\*" (#1 §9);
- "Rows 1, 3, and 7 are the flagship discriminants: no mainstream framework predicts an exponential scattering cliff, gravitationally-detectable macro-granularity of the local velocity distribution, *and* a guaranteed-null direct-detection program" (#1 §9). Row 3 of that table, velocity-space granularity, has since died ([Obituary: velocity-space granularity in halos](/wiki/dark-matter/momentum-clumping/velocity-granularity));
- the benchmark numbers above the gate, "σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0" and "Cluster self-interaction is *identically zero at any future sensitivity*" (#1 §5.1), on [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark).

The v0.4 downgrade replaced the cliff with the knee. Numbers computed from the exponential hold only if the gate's tail is Gaussian, and none of them has been machine-checked. The cliff's formulas, v\* ≡ √2μ/m_χ and σ₀ = 16πα̃²m_χ²/m_φ⁴, come from the lab notebook and are not restated in #11; #13 §4 uses the definition of v\*, with μ read as the fiber width (flag 17 in `review/wiki-build-flags.md`).

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — the current law; §13 rows 1–3 — the requirements and kill conditions; §12 — the candidates' handles; §15 — "gate tail not yet forced", falsification exposure
- `notes/broken-born-program-v1.md` §6, §9 — v1's law and its row 1 with the knee
- `notes/debt1a-ii-X-classification.md` §4 and `notes/broken-born-theory.md` 'Addendum (v0.4)' — the downgrade from cliff to knee
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — rows 1–2 survive on the particle island, to be re-derived in wave language; the (v\*/σ)³ estimate
- `notes/debt3b-wave-island.md` 'The rate' — the (v\*/σ)⁴ suppression and the island discriminant
- `notes/debt3c-ufd-endpoint.md` 'Verdict and closure of Debt 3' — what remains distinctive after Debt 3
- `notes/broken-born-theory.md` §5.1 — the v0.1 law, σ₀, v\*, the two signatures, the Born caveat, the cluster numbers; §9 — the v0.1 row 1 and the flagship discriminants; §3 — the v0.1 amplitude and k = m_χv_rel/2
- `papers/conjugate-special-relativity.md` §4 — v\* = √2 μ/m_χ with μ read as the fiber width
- `review/wiki-build-flags.md` item 17 — the suspected √2 in μ between the two gate conventions, awaiting a ruling
- `popsci/universes-other-half.md` — the knee and core smoothing in the present tense
