---
title: "Row 1: the knee in σ_T(v)"
weight: 20
status: alive
description: "Strong self-scattering in slow dwarfs, none in fast clusters, with a knee at v* ~ 10² km/s; killed by robust self-interaction at v ≫ v* or a knee excluded in the 150–400 km/s band."
provenance: [D, O]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 1"
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 4"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-program-v1.md §6"
  - "notes/broken-born-program-v1.md §9"
  - "notes/x-classification.md §4"
  - "notes/stream-stability.md 'Consequences for the predictions table'"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "wiki/papers/conjugate-special-relativity.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "review/wiki-build-flags.md items 17, 55"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §3"
  - "notes/gate-mechanism.md §5"
  - "notes/gate-mechanism.md §6"
  - "verify/gate_mechanism.py"
  - "notes/literature-check.md §3"
---

*Row 1 of [the predictions table](_index.md) tests how strongly dark matter scatters off itself as a function of the speed at which two particles collide. If dark matter is the program's [conjugate matter χ](../dark-matter/candidates/chi-particles.md) in particle form, its self-interaction passes through [the velocity gate](../dark-matter/conjugate-matter/velocity-gate.md): it is strong in slow collisions, as in [dwarf galaxies](../dark-matter/halo-astrophysics/dwarf-galaxies.md), and absent in fast ones, as in galaxy clusters, with a knee near the gate velocity v\* ~ 10² km/s between the two. Standard cold dark matter does not scatter at all, and the usual self-interacting models, in which a light particle carries the force, weaken gradually with speed, as a power law, rather than at a knee. Observations of halos across the range of masses, and so of internal speeds, can find the knee or exclude it. Row 1 is one of the three rows that [the checkpoint](../history/documents/checkpoint.md) names as the program's near-term falsification exposure.*

**Status:** Alive, with near-term falsification exposure ([#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment)) — [the scattering law](../dark-matter/conjugate-matter/scattering-law.md) behind it is [D] for [the gate mechanism](../dark-matter/conjugate-matter/gate-mechanism.md) and [O] for the shape of the knee's tail ([#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)) — derived in [the lab notebook](../history/documents/lab-notebook.md) and [the field-equation calc notes](../history/documents/field-equation-notes.md) and not machine-checked; the tail is [open problem 4](../dark-matter/conjugate-matter/gate-shape.md) of [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems), and no source sets a measurement in the 150–400 km/s band against the knee, while two published fits bear on the row's zero cluster signal ([the data situation](#the-data-situation); flag 69, pending). The row is among the text that depends on the mechanism's tag: [`notes/gate-mechanism.md`](../../notes/gate-mechanism.md) (2026-10-28; two derivations, the second blind; not reviewed) finds that exchanging [#11 §7](../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton)'s X cannot produce the gate, and flag 55 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) (pending) proposes [P] for the gate and μ and [O] for the mechanism, which [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) tags [D] ([the gate mechanism](../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). [`verify/gate_mechanism.py`](../../verify/gate_mechanism.py) reruns the note's arithmetic and algebra, on which the [V] of its tag below rests, and does not test its physics ([the gate-mechanism script](../method/verification/gate-mechanism-script.md)).

## The row

[Checkpoint #11](../history/documents/checkpoint.md) [§13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions), row 1:

| Observable | Standard expectation | Program requirement | Killed by |
| --- | --- | --- | --- |
| σ_T(v) across halo masses | CDM none; Yukawa SIDM power-law + Coulomb log | Knee at v\* ~ 10² km/s; zero cluster signal (particle χ) | Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band |

CDM is cold dark matter and SIDM self-interacting dark matter. [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) lists the row, with rows 4 and 7, as near-term falsification exposure.

## The observable

σ_T is the momentum-transfer cross-section, the measure of self-scattering that weights each collision by the fraction of forward momentum it removes, so that grazing collisions count for little and head-on rebounds most. It is quoted per unit mass, σ_T/m, in cm²/g [T] ([the transfer cross-section σ_T](../dark-matter/halo-astrophysics/transfer-cross-section.md)). v is the relative velocity of a colliding pair.

"Across halo masses" names how the velocity dependence is reached. Heavier halos have faster internal motions, so a set of halos of different masses samples σ_T at different speeds: dwarf galaxies at tens of km/s, galaxy clusters at thousands, with large spirals and small groups between [T]. A cross-section that falls with speed separates the two ends, and the shape of the fall is the observable ([why velocity dependence matters](../dark-matter/halo-astrophysics/self-interacting-dark-matter.md#why-velocity-dependence-matters-t)).

## The standard expectation

The row sets two standard models against the program.

- **Cold dark matter: none.** CDM does not scatter off itself, so σ_T = 0 at every speed.
- **Yukawa SIDM: a power law with a Coulomb logarithm.** When a [light mediator](../gravity/spin-2-fields/yukawa-forces.md#the-light-mediator-limit-forward-peaking-and-the-coulomb-logarithm) of mass m_φ carries the force, the Born amplitude goes as 1/(q² + m_φ²), with q the momentum transfer; small-angle collisions dominate, and the transfer cross-section falls smoothly as speed rises. The [lab notebook](../history/documents/lab-notebook.md) states it: "Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction" ([#1 §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d)). The logarithm comes from the small-angle cutoff that the mediator mass supplies [T] ([contact and Yukawa forces](../dark-matter/halo-astrophysics/self-interacting-dark-matter.md#contact-and-yukawa-forces)).

The lab notebook's version of the column read "Constant (CDM: 0) or power-law v⁻⁴ln tail (Yukawa SIDM)" ([#1 §9](../../notes/broken-born-theory.md#9-predictions)).

[`notes/gate-mechanism.md`](../../notes/gate-mechanism.md) (2026-10-28, not reviewed) places calc note [#6](../../notes/x-classification.md)'s rational gates in this column. "The rationality of tree amplitudes sits in the transfer: the propagator 1/(q² + M_X²) and form factors in t. Integrated over angle these give a light mediator's knee in σ_T(v) with a power-law tail. That is [#11 §13 row 1](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)'s 'standard expectation' column, not a gate in k" (§3; both derivations) [D][V]. On that reading the rational branch of [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)'s "tail (Gaussian vs rational)" is this column's expectation rather than a program-specific gate; the program's requirement rests on a gate in the incoming relative momentum k, whose derivation flag 55 disputes.

## The program's requirement

### The law behind it

[#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) states the law the row tests:

> "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking."

```text
σ_T(v) = σ₀ · F(v²/v*²)
```

σ₀ is the cross-section below the gate, F the gate function, and v\* the gate velocity. The chain that produces it runs through four pages:

1. **The amplitude.** Conjugate matter scatters with "M(k,q) = 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²), k the incoming *relative* momentum — the variable no x-local mediator produces" ([#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)), where x-local means local in position and μ is the momentum width of a χ quantum ([the velocity gate: the amplitude](../dark-matter/conjugate-matter/velocity-gate.md#the-amplitude)).
2. **The mechanism.** In [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) the gate comes from exchange of the massive [momentum graviton X](../gravity/momentum-graviton/_index.md) between two χ quanta, which can exchange X only where their momentum-space wavepackets overlap [D — mechanism] ([the derivation as the sources give it](../dark-matter/conjugate-matter/gate-mechanism.md#the-derivation-as-the-sources-give-it)). Not derived, according to flag 55 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) (pending): exchanging the X of [#11 §7](../papers/broken-born-checkpoint-v2.md#7-the-massive-momentum-graviton) gives a dependence on k with the speed of light as its velocity scale, 2.4×10⁻⁷ at 120 km/s where the gate is 0.61 ([`notes/gate-mechanism.md` §2](../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate); [the gate mechanism](../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)). The note does not refute the gate; it proposes returning it to a postulate [P] ([§5](../../notes/gate-mechanism.md#5-what-follows-for-the-record)).
3. **The cross-section.** In the Born approximation the gate in k becomes a gate in the collision speed, σ_T(v) = σ₀F(v²/v\*²) ([the gated scattering law](../dark-matter/conjugate-matter/scattering-law.md#the-law)).
4. **The strength.** σ₀ is fitted to the cores of dwarf galaxies ([the scattering benchmark](../dark-matter/conjugate-matter/benchmark.md#the-relation)).

### The knee and its location

The knee exists because the gate depends on k, whatever the function F: below v\* pairs pass through the gate and scatter with σ₀, above it they do not. Calc note #6 separated what is robust from what is not: "The knee's existence and location are robust; its steepness is model-internal information, not a guaranteed exponential" ([`notes/x-classification.md` §4](../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)).

The location comes from the core fit. The lab notebook: "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" ([#1 §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d)), a value it gives without a citation ([where the input comes from](../dark-matter/conjugate-matter/benchmark.md#where-the-input-comes-from)). #11's row states the location less precisely, as "v\* ~ 10² km/s". The checkpoint's benchmark mass for particle χ follows from the same input: m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3} ([#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)).

The gate velocity is defined in the lab notebook as v\* ≡ √2μ/m_χ ([#1 §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d)), and [conjugate special relativity](../conjugate-relativity/_index.md) ([#13 §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell)) repeats it as v\* = √2 μ/m_χ; #11 does not restate it. It belongs to the notebook's postulated gate e^{−k²/μ²} with k = m_χv_rel/2. Calc note #6's overlap form is written e^{−(p₁−p₂)²/2μ²}, and the two are not reconciled in any source ([two conventions, not reconciled](../dark-matter/conjugate-matter/velocity-gate.md#two-conventions-not-reconciled)). [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 17 records a suspected factor of √2 in μ between them: with #6's [fiber width](../phase-space/reciprocity/momentum-fibers.md#quanta-with-a-width-along-the-fiber) the knee would sit at v\* = μ/m_χ rather than at #1's √2μ/m_χ. The flag (pending) notes that no stated number changes; its audit found the factor present only if #6's form is read as the gate on the amplitude, and rated the flag as depending on that convention ([two conventions](../dark-matter/conjugate-matter/velocity-gate.md#two-conventions-not-reconciled)). This page quotes the sources as written.

### Zero cluster signal, for particles

In clusters the collision speeds are far above v\*, so the gate is closed and the requirement is no measurable self-scattering. #11 attaches the qualifier "(particle χ)". For the wave branch of χ, [calc note #3](../history/documents/clumping-notes.md) gives a power-law suppression above the gate, (v\*/σ)⁴ with σ the halo's [velocity dispersion](../dark-matter/halo-astrophysics/velocity-dispersion.md), instead of a closed gate; telling the two apart is [row 3, the island discriminant](island-discriminant.md). The gravitational side of cluster collisions is separate: χ "propagates on g (equivalence principle; Bullet-Cluster-safe)" ([#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)), so its mass moves with the galaxies as ordinary dark matter does ([the equivalence principle](../gravity/spin-2-fields/equivalence-principle.md); [the Bullet Cluster](../dark-matter/halo-astrophysics/bullet-cluster.md#lensing-one-gravity-for-both-kinds-of-matter)).

## What kills it

The row has two kill conditions.

- **"Robust self-interaction at v ≫ v\*".** A confirmed nonzero self-scattering at speeds far above the knee, as in galaxy clusters, contradicts a closed gate. The row does not say how large a remainder counts as robust. That matters because the knee's tail is open: a Gaussian gate leaves essentially nothing above the knee, while a rational gate leaves a power-law remainder ([why the gate shape is observable](../dark-matter/conjugate-matter/gate-shape.md#why-it-is-observable)).
- **"Knee excluded in the 150–400 km/s band".** The lab notebook named the band where the program and Yukawa SIDM separate most: "The discriminating band is v ~ 150–400 km/s (large spirals, small groups), where the two shapes diverge by orders of magnitude" ([#1 §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d)). Halo data in that band that exclude a knee end the claim. The v0.1 wording was "cliff-shape excluded in the 150–400 km/s band" ([#1 §9](../../notes/broken-born-theory.md#9-predictions)).

A dwarf-galaxy core is not itself a test. It is the input that fixes σ₀; the knee and its absence in clusters are the predictions.

## The data situation

No source sets a measurement in the 150–400 km/s band against the knee. At cluster speeds, two published fits bear on the row's "zero cluster signal (particle χ)" ([`notes/literature-check.md` §3](../../notes/literature-check.md#3-dark-matter-is-conjugate-matter-c1-the-identification-is-published); flag 69, pending). [Kaplinghat, Tulin and Yu 2016](https://arxiv.org/abs/1508.03339) "prefer a mildly velocity-dependent cross section", from about 2 cm²/g on galaxy scales to about 0.1 cm²/g on cluster scales, and [Sagunski et al. 2021](https://arxiv.org/abs/2006.12515) find "a mild preference for a nonzero cross section compared with cold collisionless dark matter" in groups and clusters, with 0.19 ± 0.09 cm²/g in clusters and an upper limit of 0.35 cm²/g at 95% confidence [S]. Both favour a nonzero value at cluster speeds, where row 1 gives particle χ none, and the first also a cross-section that falls with velocity, as the knee does, which the second finds consistent with its data. Neither is the robust self-interaction at v ≫ v\* that kills the row. [#11 §8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) leaves the gate's tail open, Gaussian or rational; one judge of the literature check reads a rational tail as softening the conflict with the two fits, and whether it could match them was not assessed. The pattern itself, strong scattering in dwarfs and weak in clusters, also has a published mechanism besides the Yukawa power law of the standard expectation: resonant self-interaction ([Chu, Garcia-Cely and Murayama 2019](https://arxiv.org/abs/1810.04709) [S]), which flag 69 suggests adding to the row's standard expectation. The verifier of the literature check who labeled it related concludes that the knee alone does not single out the gate, and that the knee's origin and tail shape are what was not found ([`notes/literature-check.md` §3](../../notes/literature-check.md#3-dark-matter-is-conjugate-matter-c1-the-identification-is-published)). [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) calls the exposure near-term without naming the observations that will decide it. The documents use the data only at the input end: the dwarf-core value σ₀/m_χ ≈ 30 cm²/g, stated without a citation ([#1 §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d)), and the standard observation that many dwarfs show flat cores where CDM predicts cusps [T] ([the cusp–core problem](../dark-matter/halo-astrophysics/dwarf-galaxies.md#the-cuspcore-problem-t)).

The popular article [#12](../../popsci/universes-other-half.md) describes the smoothing of dwarf cusps and the shut-off in cluster collisions in the present tense, as if observed ('Dark matter as the other polarization'). In the program's documents the core fit is the input and the knee is a prediction ([the popular articles](../history/documents/popular-articles.md)).

## What is open

- **The tail.** Whether F is Gaussian or rational is item 4 of [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems) [O]; [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) lists "gate tail not yet forced" among the program's degeneration risks ([Open: the gate shape (OP4)](../dark-matter/conjugate-matter/gate-shape.md)). The existence and location of the knee do not depend on it; its steepness, and so the strength of the first kill condition, does.
- **The strength.** Why σ₀ can be as large as dwarf cores require while ordinary matter couples to X only at gravitational strength is item 5 of [#11 §14](../papers/broken-born-checkpoint-v2.md#14-open-problems) ([Open: the dual-stress enhancement (OP5)](../dark-matter/conjugate-matter/dual-stress-enhancement.md)).
- **The wave branch.** For χ as a classical wave, calc note [#2](../../notes/stream-stability.md) found that "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)" ([`notes/stream-stability.md`](../../notes/stream-stability.md), 'Consequences for the predictions table'). The power-law suppression of row 3 answers this only for the knee's tail ([Open: rows 1 and 2 in wave language](../dark-matter/momentum-clumping/wave-island/condensation-rate.md#open-rows-1-and-2-in-wave-language)).
- **The √2 in v\*.** [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 17, above.
- **The mechanism.** Flag 55 proposes that the mechanism is open [O] ([`notes/gate-mechanism.md` §5](../../notes/gate-mechanism.md#5-what-follows-for-the-record)). Among the questions that would then be open: whether the program keeps the gate as a postulate, or rewrites χ's self-interaction as the note's reading R1, a position-local potential "of range ~10 pm, which is ordinary short-range self-interacting dark matter with power-law tails and would remove the program-specific content of rows 1–3" ([§5](../../notes/gate-mechanism.md#5-what-follows-for-the-record); [the fiber overlap, read two ways](../dark-matter/conjugate-matter/gate-mechanism.md#the-fiber-overlap-read-two-ways)). Reading R1 is the note's reconstruction of [#6 §4](../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)'s fiber overlap, not a statement of the record.

Row 1 feeds two other rows. Its tail is what [row 3](island-discriminant.md) reads, and rows 1–3 together are the discriminators of [row 11, particles or condensate](dark-sector-microstructure.md). In [#11 §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model)'s candidate table, [χ particles](../dark-matter/candidates/chi-particles.md) carry "knee at v\*, sharp tail" and [the X-condensate](../dark-matter/candidates/x-condensate.md) "knee shape wave-like"; the third candidate, P.R.'s conjecture of [magnetic monopoles abundant in momentum space](../dark-matter/candidates/momentum-space-monopoles.md), is listed as "untested" ([#11 §12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model)). The companion signature of the same law is [row 2, isotropic scattering below the gate](scattering-isotropy.md).

## Superseded: the exponential cliff of v0.1

The lab notebook's row 1 was sharper ([#1 §9](../../notes/broken-born-theory.md#9-predictions)):

| | [#1 §9](../../notes/broken-born-theory.md#9-predictions) (v0.1) | [#11 §13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) (current) |
| --- | --- | --- |
| Requirement | "σ₀ e^{−v²/v\*²}: cliff at v\* ∼ 120 km/s; **exactly zero in clusters forever**" | "Knee at v\* ~ 10² km/s; zero cluster signal (particle χ)" |
| Killed by | "Robust nonzero self-interaction at v > 3v\*; or cliff-shape excluded in the 150–400 km/s band" | "Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band" |

The cliff rested on the postulated Gaussian gate. With it the notebook predicted "σ_T/m (300 km/s) ≈ 6×10⁻² cm²/g" and "σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0" ([#1 §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d)), numbers that hold only if the tail is Gaussian and that no script checks ([the v0.1 predictions from the benchmark](../dark-matter/conjugate-matter/benchmark.md#superseded-the-v01-predictions-from-the-benchmark)).

Calc note #6 derived the gate from X exchange (not derived, according to flag 55 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md), pending; [the gate mechanism](../dark-matter/conjugate-matter/gate-mechanism.md#exchanging-x-cannot-produce-the-gate)) and found that "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" (§4). The lab notebook's v0.4 addendum amended the row: "the exponential cliff weakens to a *sharp knee at v_\* with tail shape (Gaussian vs rational) diagnosing the vertex completion*; the knee's existence and location remain the robust prediction" (#1 'Addendum (v0.4)'). v1 already reads "Knee at v\* ~ 10² km/s; tail shape = vertex diagnostic; zero cluster signal (particle χ)" ([#9 §9](../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions)), and #11 drops the middle clause from the table while keeping it in [§8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate). The downgrade is told step by step on [the gated scattering law](../dark-matter/conjugate-matter/scattering-law.md#the-downgrade-to-a-knee), and the renumbering of the whole table on [the history of the predictions table](table-history.md).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §13 row 1](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the row; [§8](../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — the law, the amplitude, the tags and the benchmark mass; [§12](../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates-and-the-failure-of-one-model) — the candidates' handles; [§14 item 4](../papers/broken-born-checkpoint-v2.md#14-open-problems) — the open gate shape; [§15](../papers/broken-born-checkpoint-v2.md#15-assessment) — the near-term exposure and "gate tail not yet forced"
- [`notes/x-classification.md` §4](../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — the downgrade from cliff to knee and its reason
- [`notes/broken-born-theory.md`](../../notes/broken-born-theory.md) 'Addendum (v0.4)' — the amended row
- [`notes/broken-born-program-v1.md` §6](../../notes/broken-born-program-v1.md#6-conjugate-matter-and-the-gate-the-gate-problem-mechanism-found), [§9](../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions) — v1's law and its row 1, already a knee
- [`notes/stream-stability.md`](../../notes/stream-stability.md) 'Consequences for the predictions table' — rows 1–2 to be re-derived in wave language
- [`notes/broken-born-theory.md` §5.1](../../notes/broken-born-theory.md#51-the-scattering-law-d) — the core-fit input, v\* ≡ √2μ/m_χ, the Yukawa v⁻⁴ tail, the 150–400 km/s band and the v0.1 numbers; [§9](../../notes/broken-born-theory.md#9-predictions) — the v0.1 row 1 and standard expectation
- [`wiki/papers/conjugate-special-relativity.md` §4](../papers/conjugate-special-relativity.md#4-invariants-the-mass-shell-and-the-length-shell) — v\* = √2 μ/m_χ restated
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 17 — the suspected √2 in μ between the two gate conventions, pending; item 55 — the gate's mechanism not derived, pending
- [`notes/gate-mechanism.md` §2](../../notes/gate-mechanism.md#2-exchanging-the-x-of-7-cannot-produce-the-gate) — exchanging X gives no gate; [§3](../../notes/gate-mechanism.md#3-the-fiber-overlap-read-two-ways) — the rational gates are the standard-expectation column; reading R1; [§5](../../notes/gate-mechanism.md#5-what-follows-for-the-record) — the proposed tags, rows 1–3 among the dependent text, what becomes open; [§6](../../notes/gate-mechanism.md#6-record) — what the script tests
- [`verify/gate_mechanism.py`](../../verify/gate_mechanism.py) — reruns the note's arithmetic and algebra ([the gate-mechanism script](../method/verification/gate-mechanism-script.md))
- [`popsci/universes-other-half.md`](../../popsci/universes-other-half.md) 'Dark matter as the other polarization' — the knee and core smoothing in the present tense (popular article)
- [`notes/literature-check.md` §3](../../notes/literature-check.md#3-dark-matter-is-conjugate-matter-c1-the-identification-is-published) — two fits of the self-interaction across halo masses, with their numbers; [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 69
