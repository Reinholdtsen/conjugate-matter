---
title: "Row 1: the knee in σ_T(v)"
weight: 20
status: alive
description: "Strong self-scattering in slow dwarfs, none in fast clusters, with a knee at v* ~ 10² km/s; killed by robust self-interaction at v ≫ v* or a knee excluded in the 150–400 km/s band."
provenance: [D, O]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 1"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-program-v1.md §9"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "papers/conjugate-special-relativity.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "review/wiki-build-flags.md item 17"
---

*Row 1 of [the predictions table](/wiki/predictions) tests how strongly dark matter scatters off itself as a function of the speed at which two particles collide. If dark matter is the program's [conjugate matter χ](/wiki/dark-matter/candidates/chi-particles) in particle form, its self-interaction passes through [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate): it is strong in slow collisions, as in [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies), and absent in fast ones, as in galaxy clusters, with a knee near the gate velocity v\* ~ 10² km/s between the two. Standard cold dark matter does not scatter at all, and the usual self-interacting models, in which a light particle carries the force, weaken gradually with speed, as a power law, rather than at a knee. Observations of halos across the range of masses, and so of internal speeds, can find the knee or exclude it. Row 1 is one of the three rows that [the checkpoint](/wiki/history/documents/checkpoint) names as the program's near-term falsification exposure.*

**Status:** Alive, with near-term falsification exposure (#11 §15) — [the scattering law](/wiki/dark-matter/conjugate-matter/scattering-law) behind it is [D] for [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism) and [O] for the shape of the knee's tail (#11 §8) — derived in [the lab notebook](/wiki/history/documents/lab-notebook) and [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes) and not machine-checked; the tail is [open problem 4](/wiki/dark-matter/conjugate-matter/gate-shape) of #11 §14, and no source records a measurement that tests the knee.

## The row

[Checkpoint #11](/wiki/history/documents/checkpoint) §13, row 1:

| Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- |
| σ_T(v) across halo masses | CDM none; Yukawa SIDM power-law + Coulomb log | Knee at v\* ~ 10² km/s; zero cluster signal (particle χ) | Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band |

CDM is cold dark matter and SIDM self-interacting dark matter. #11 §15 lists the row among those of "genuine and near-term" falsification exposure, with rows 4 and 7.

## The observable

σ_T is the momentum-transfer cross-section, the measure of self-scattering that weights each collision by the fraction of forward momentum it removes, so that grazing collisions count for little and head-on rebounds most. It is quoted per unit mass, σ_T/m, in cm²/g [T] ([the transfer cross-section](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#the-transfer-cross-section-t)). v is the relative velocity of a colliding pair.

"Across halo masses" names how the velocity dependence is reached. Heavier halos have faster internal motions, so a set of halos of different masses samples σ_T at different speeds: dwarf galaxies at tens of km/s, galaxy clusters at thousands, with large spirals and small groups between [T]. A cross-section that falls with speed separates the two ends, and the shape of the fall is the observable ([why velocity dependence matters](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#why-velocity-dependence-matters-t)).

## The standard expectation

The row sets two standard models against the program.

- **Cold dark matter: none.** CDM does not scatter off itself, so σ_T = 0 at every speed.
- **Yukawa SIDM: a power law with a Coulomb logarithm.** When a light mediator of mass m_φ carries the force, the Born amplitude goes as 1/(q² + m_φ²), with q the momentum transfer; small-angle collisions dominate, and the transfer cross-section falls smoothly as speed rises. The [lab notebook](/wiki/history/documents/lab-notebook) states it: "Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction" (#1 §5.1). The logarithm comes from the small-angle cutoff that the mediator mass supplies [T] ([contact and Yukawa forces](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#contact-and-yukawa-forces)).

The lab notebook's version of the column read "Constant (CDM: 0) or power-law v⁻⁴ln tail (Yukawa SIDM)" (#1 §9).

## The Broken-Born requirement

### The law behind it

#11 §8 states the law the row tests:

> "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking."

```text
σ_T(v) = σ₀ · F(v²/v*²)
```

σ₀ is the cross-section below the gate, F the gate function, and v\* the gate velocity. The chain that produces it runs through four pages:

1. **The amplitude.** Conjugate matter scatters with "M(k,q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²), k the incoming *relative* momentum — the variable no x-local mediator produces" (#11 §8), where x-local means local in position and μ is the momentum width of a χ quantum ([the velocity gate: the amplitude](/wiki/dark-matter/conjugate-matter/velocity-gate#the-amplitude)).
2. **The mechanism.** The gate comes from exchange of the massive [momentum graviton X](/wiki/gravity/momentum-graviton) between two χ quanta, which can exchange X only where their momentum-space wavepackets overlap [D — mechanism] ([the derivation as the sources give it](/wiki/dark-matter/conjugate-matter/gate-mechanism#the-derivation-as-the-sources-give-it)).
3. **The cross-section.** In the Born approximation the gate in k becomes a gate in the collision speed, σ_T(v) = σ₀F(v²/v\*²) ([the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law#the-law)).
4. **The strength.** σ₀ is fitted to the cores of dwarf galaxies ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark#the-relation)).

### The knee and its location

The knee exists because the gate depends on k, whatever the function F: below v\* pairs pass through the gate and scatter with σ₀, above it they do not. Calc note #6 separated what is robust from what is not: "The knee's existence and location are robust; its steepness is model-internal information, not a guaranteed exponential" (`notes/debt1a-ii-X-classification.md` §4).

The location comes from the core fit. The lab notebook: "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" (#1 §5.1), a value it gives without a citation ([where the input comes from](/wiki/dark-matter/conjugate-matter/benchmark#where-the-input-comes-from)). #11's row states the location less precisely, as "v\* ~ 10² km/s". The checkpoint's benchmark mass for particle χ follows from the same input: m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3} (#11 §8).

The gate velocity is defined in the lab notebook as v\* ≡ √2μ/m_χ (#1 §5.1), and [conjugate special relativity](/wiki/conjugate-relativity) (#13 §4) repeats it as v\* = √2 μ/m_χ; #11 does not restate it. It belongs to the notebook's postulated gate e^{−k²/μ²} with k = m_χv_rel/2. Calc note #6's overlap form is written e^{−(p₁−p₂)²/2μ²}, and the two are not reconciled in any source ([two conventions, not reconciled](/wiki/dark-matter/conjugate-matter/velocity-gate#two-conventions-not-reconciled)). `review/wiki-build-flags.md` item 17 records a suspected factor of √2 in μ between them: with #6's fiber width the knee would sit at v\* = μ/m_χ rather than at #1's √2μ/m_χ. The flag notes that no stated number changes, and it awaits Paul's ruling; this page quotes the sources as written.

### Zero cluster signal, for particles

In clusters the collision speeds are far above v\*, so the gate is closed and the requirement is no measurable self-scattering. #11 attaches the qualifier "(particle χ)". For the wave branch of χ, [calc note #3](/wiki/history/documents/debt-3-notes) gives a power-law suppression above the gate, (v\*/σ)⁴ with σ the halo's velocity dispersion, instead of a closed gate; telling the two apart is [row 3, the island discriminant](/wiki/predictions/island-discriminant). The gravitational side of cluster collisions is separate: χ "propagates on g (equivalence principle; Bullet-Cluster-safe)" (#11 §8), so its mass moves with the galaxies as ordinary dark matter does ([the Bullet Cluster](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#the-bullet-cluster-t)).

## What kills it

The row has two kill conditions.

- **"Robust self-interaction at v ≫ v\*".** A confirmed nonzero self-scattering at speeds far above the knee, as in galaxy clusters, contradicts a closed gate. The row does not say how large a remainder counts as robust. That matters because the knee's tail is open: a Gaussian gate leaves essentially nothing above the knee, while a rational gate leaves a power-law remainder ([why the gate shape is observable](/wiki/dark-matter/conjugate-matter/gate-shape#why-it-is-observable)).
- **"Knee excluded in the 150–400 km/s band".** The lab notebook named the band where the program and Yukawa SIDM separate most: "The discriminating band is v ~ 150–400 km/s (large spirals, small groups), where the two shapes diverge by orders of magnitude" (#1 §5.1). Halo data in that band that exclude a knee end the claim. The v0.1 wording was "cliff-shape excluded in the 150–400 km/s band" (#1 §9).

A dwarf-galaxy core is not itself a test. It is the input that fixes σ₀; the knee and its absence in clusters are the predictions.

## The data situation

No source records a measurement that tests the knee, either in the 150–400 km/s band or as a bound on cluster self-scattering set against the program's gate. #11 §15 calls the exposure "genuine and near-term" without naming the observations that will decide it. The documents use the data only at the input end: the dwarf-core value σ₀/m_χ ≈ 30 cm²/g, stated without a citation (#1 §5.1), and the standard observation that many dwarfs show flat cores where CDM predicts cusps [T] ([the cusp–core problem](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies#the-cuspcore-problem-t)).

The popular article #12 describes the smoothing of dwarf cusps and the shut-off in cluster collisions in the present tense, as if observed ('Dark matter as the other polarization'). In the program's documents the core fit is the input and the knee is a prediction ([the popular articles](/wiki/history/documents/popular-articles)).

## What is open

- **The tail.** Whether F is Gaussian or rational is item 4 of #11 §14 [O]; #11 §15 lists "gate tail not yet forced" among the program's degeneration risks ([Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape)). The existence and location of the knee do not depend on it; its steepness, and so the strength of the first kill condition, does.
- **The strength.** Why σ₀ can be as large as dwarf cores require while ordinary matter couples to X only at gravitational strength is item 5 of #11 §14 ([Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement)).
- **The wave branch.** For χ as a classical wave, calc note #2 found that "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)" (`notes/debt3a-stream-stability.md`, 'Consequences for the predictions table'). The power-law suppression of row 3 answers this only for the knee's tail ([Open: rows 1 and 2 in wave language](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#open-rows-1-and-2-in-wave-language)).
- **The √2 in v\*.** `review/wiki-build-flags.md` item 17, above.

Row 1 feeds two other rows. Its tail is what [row 3](/wiki/predictions/island-discriminant) reads, and rows 1–3 together are the discriminators of [row 11, particles or condensate](/wiki/predictions/dark-sector-microstructure). In #11's comparison of the remaining candidates, [χ particles](/wiki/dark-matter/candidates/chi-particles) carry "knee at v\*, sharp tail" and [the X-condensate](/wiki/dark-matter/candidates/x-condensate) "knee shape wave-like" (#11 §12). The companion signature of the same law is [row 2, isotropic scattering below the gate](/wiki/predictions/scattering-isotropy).

## Superseded: the exponential cliff of v0.1

The lab notebook's row 1 was sharper (#1 §9):

| | #1 §9 (v0.1) | #11 §13 (current) |
| --- | --- | --- |
| Requirement | "σ₀ e^{−v²/v\*²}: cliff at v\* ∼ 120 km/s; **exactly zero in clusters forever**" | "Knee at v\* ~ 10² km/s; zero cluster signal (particle χ)" |
| Killed by | "Robust nonzero self-interaction at v > 3v\*; or cliff-shape excluded in the 150–400 km/s band" | "Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band" |

The cliff rested on the postulated Gaussian gate. With it the notebook predicted "σ_T/m (300 km/s) ≈ 6×10⁻² cm²/g" and "σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0" (#1 §5.1), numbers that hold only if the tail is Gaussian and that no script checks ([the v0.1 predictions from the benchmark](/wiki/dark-matter/conjugate-matter/benchmark#superseded-the-v01-predictions-from-the-benchmark)).

Calc note #6 derived the gate from X exchange and found that "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" (§4). The lab notebook's v0.4 addendum amended the row: "the exponential cliff weakens to a *sharp knee at v_\* with tail shape (Gaussian vs rational) diagnosing the vertex completion*; the knee's existence and location remain the robust prediction" (#1 'Addendum (v0.4)'). v1 already reads "Knee at v\* ~ 10² km/s; tail shape = vertex diagnostic; zero cluster signal (particle χ)" (#9 §9), and #11 drops the middle clause from the table while keeping it in §8. The downgrade is told step by step on [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law#the-downgrade-to-a-knee), and the renumbering of the whole table on [the history of the predictions table](/wiki/predictions/table-history).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 1 — the row; §8 — the law, the amplitude, the tags and the benchmark mass; §12 — the candidates' handles; §14 item 4 — the open gate shape; §15 — the near-term exposure and "gate tail not yet forced"
- `notes/debt1a-ii-X-classification.md` §4 — the downgrade from cliff to knee and its reason
- `notes/broken-born-theory.md` 'Addendum (v0.4)' — the amended row
- `notes/broken-born-program-v1.md` §6, §9 — v1's law and its row 1, already a knee
- `notes/debt3a-stream-stability.md` 'Consequences for the predictions table' — rows 1–2 to be re-derived in wave language
- `notes/broken-born-theory.md` §5.1 — the core-fit input, v\* ≡ √2μ/m_χ, the Yukawa v⁻⁴ tail, the 150–400 km/s band and the v0.1 numbers; §9 — the v0.1 row 1 and standard expectation
- `papers/conjugate-special-relativity.md` §4 — v\* = √2 μ/m_χ restated
- `review/wiki-build-flags.md` item 17 — the suspected √2 in μ between the two gate conventions, awaiting a ruling
- `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the knee and core smoothing in the present tense (popular article)
