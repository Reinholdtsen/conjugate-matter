---
title: "The Bullet Cluster"
weight: 25
status: established
description: "Two galaxy clusters seen after a collision, whose lensing mass moved on with the galaxies while the X-ray-emitting gas was slowed: evidence for a separate, nearly collisionless dark matter and a limit on self-scattering at cluster speeds; the program's χ is 'Bullet-Cluster-safe' through universal gravity and a gate closed at cluster speeds, with no number compared."
provenance: [T]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §8"
  - "wiki/papers/broken-born-checkpoint-v2.md §4"
  - "wiki/papers/broken-born-checkpoint-v2.md §9"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 1"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §6"
  - "notes/x-classification.md §4"
  - "notes/wave-island.md 'The rate'"
  - "notes/wave-island.md 'What pins g? Two scenarios'"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
  - "notes/literature-check.md §3"
  - "review/wiki-build-flags.md item 69"
---

*The Bullet Cluster is a pair of galaxy clusters seen shortly after the smaller one passed through the larger. A cluster has three components: its galaxies; hot, thin gas between them, which emits X-rays and outweighs the stars; and dark matter, which outweighs both. In the collision the two gas clouds struck each other and were slowed, while the galaxies passed through. The total mass, mapped by the way the clusters' gravity bends light from more distant galaxies, moved on with the galaxies and not with the gas. The observation is widely cited as direct evidence that most of a cluster's mass is a separate, nearly collisionless dark matter, and it limits how strongly dark matter can [scatter off itself](self-interacting-dark-matter.md) at the speeds of cluster collisions. The Comatter program calls its [conjugate matter](../conjugate-matter/_index.md) "Bullet-Cluster-safe": it gravitates and bends light as ordinary matter does, and its self-interaction is switched off at cluster speeds by [the velocity gate](../conjugate-matter/velocity-gate.md). The program's documents quote no number for the limit and do not compare the gate with it.*

**Status:** Established — [T] — observational astrophysics written here from general knowledge, with the literature it names marked † (Markevitch et al. 2004 †; Clowe et al. 2006 †; Randall et al. 2008 †; Kahlhoefer et al. 2014 †); the program's documents cite no paper for it and quote no number from it. The program's uses are the lab notebook's lensing statement ([#1 §4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured)), tagged [D], the clause "Bullet-Cluster-safe" in [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate), and row 1's requirement of "zero cluster signal (particle χ)" ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)); no `verify/` script checks any of them.

## What was observed [T]

### Three components in a collision

A galaxy cluster is the largest kind of gravitationally bound system. Most of its ordinary matter is not in its galaxies but in gas between them, hot enough to shine in X-rays, and most of its mass is dark matter, detected by its gravity alone. In a collision of two clusters the three components behave differently:

- **Galaxies** are small compared with the distances between them, so the galaxies of one cluster pass between those of the other almost without colliding.
- **Gas** fills the volume of each cluster, so the two gas clouds cannot pass through each other. Each is slowed by the pressure of the gas it runs into and falls behind its galaxies.
- **Dark matter** passes through as the galaxies do if its particles do not scatter off one another. If they do scatter, it is slowed or partly scattered out, as the gas is, though more weakly.

### The system

The Bullet Cluster consists of two clusters, one smaller than the other, seen shortly after the smaller passed through the larger. The collision runs nearly in the plane of the sky, across the line of sight, so the separation of the components is visible. X-ray images show the gas of both clusters lying between the two groups of galaxies. The smaller cluster's gas forms a cloud shaped like a bullet, which gave the system its name. A bow shock, a front of compressed hot gas, lies ahead of it.

Gravitational lensing maps the total mass, ordinary and dark. The gravity of the clusters bends light from galaxies far behind them, which distorts their apparent shapes slightly and in a coherent pattern; from the pattern the projected mass can be reconstructed. In the Bullet Cluster the lensing map has two mass concentrations, one at each group of galaxies, and both are offset from the gas (Clowe et al. 2006 †).

## What it shows [T]

### Dark matter as a separate component

The gas holds most of the ordinary mass. If the ordinary matter were all of the mass, the lensing map would peak on the gas. It peaks instead on the galaxies, which hold a smaller part of the ordinary mass. Most of the mass is therefore something other than the ordinary matter, and it passed through the collision as the galaxies did. Clowe and collaborators titled their paper "A direct empirical proof of the existence of dark matter" (2006 †). The observation is also widely cited as a difficulty for theories that replace dark matter with a modification of gravity, since in those theories the gravitational field is set by the visible matter.

### The limit on self-scattering [T]

If dark-matter particles scatter off one another, the two dark-matter halos interacted during the collision. Three consequences have been used to bound the scattering, each expressed as a cross-section per unit mass (Markevitch et al. 2004 †; Randall et al. 2008 †):

- **Offset.** Scattering would slow the smaller cluster's dark matter relative to its galaxies and displace its mass peak toward the gas. The lensing peak and the galaxies coincide within the errors of the measurement.
- **Mass loss.** Particles scattered through large angles would leave the smaller cluster, which would lower its ratio of mass to light compared with the larger cluster's. No such deficit is seen.
- **Survival.** A dark-matter particle of the smaller cluster that crosses the larger one passes through a column of dark matter of surface density Σ, its mass per unit area on the sky. The expected number of scatterings on the way, the scattering depth, is (σ/m)·Σ, with σ/m the cross-section per unit mass. The smaller cluster kept its dark matter, so the scattering depth cannot be large, which bounds σ/m.

The bounds hold at the relative speed of this collision, far above the internal speeds of [dwarf galaxies](dwarf-galaxies.md). A cross-section that falls with speed can be small here and still large in dwarfs, so a self-interaction strong enough to make the cores of dwarf galaxies can meet the cluster limits by weakening at cluster speeds ([why velocity dependence matters](self-interacting-dark-matter.md#why-velocity-dependence-matters-t)). How an offset or a loss of mass translates into [the transfer cross-section](transfer-cross-section.md) per unit mass, σ_T/m, also depends on the angular pattern of the scattering: rare scatterings through large angles remove particles, while frequent scatterings through small angles, as with a light mediator, act on a halo as a drag (Kahlhoefer et al. 2014 †; [the angular pattern](transfer-cross-section.md#the-angular-pattern-t)).

No program document quotes a value of these limits, and this page gives none.

## How the program treats it

The program's documents treat the observation in two halves, as the lab notebook first did: the lensing, which follows from how conjugate matter gravitates, and the scattering, which is the subject of the predictions table's [row 1](../../predictions/self-interaction-knee.md).

### Lensing: one gravity for both kinds of matter

The program's postulate [P4](../../program/postulates/p4-polarized-matter.md) [P] reads: "Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H; gauge forces do not cross polarizations" ([#11 §4](../../papers/broken-born-checkpoint-v2.md#4-postulates)). H is the [generalized metric](../../phase-space/born-geometry/born-structures.md) on phase space, and on the program's vacuum it contains the spacetime metric g, so conjugate matter χ couples to g in the same way as ordinary matter ([one gravity for both](../../program/postulates/p4-polarized-matter.md#one-gravity-for-both)). It therefore falls, orbits and bends light like any other mass, as general relativity requires of everything that couples to the metric ([minimal coupling and free fall](../../gravity/spin-2-fields/general-relativity.md#minimal-coupling-and-free-fall-t); [the equivalence principle](../../gravity/spin-2-fields/equivalence-principle.md)).

[The lab notebook](../../history/documents/lab-notebook.md) draws the consequence for the Bullet Cluster, tagged [D] ([#1 §4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured), transcribed from its LaTeX):

> "χ couples to g universally: it falls, orbits, and lenses like ordinary dark matter. Bullet Cluster lensing-centroid behavior is automatic (and see Prediction 1 for the scattering side)."

[The checkpoint](../../history/documents/checkpoint.md) keeps it in one clause: "χ propagates on g (equivalence principle; Bullet-Cluster-safe)" ([#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)). The first consolidation, v1, has the same clause ([#9 §6](../../../notes/broken-born-program-v1.md#6-conjugate-matter-and-the-gate-the-gate-problem-mechanism-found)), and the plain-language passage of [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) says that conjugate matter "falls and bends light like everything else". The notebook's Prediction 1 is the first form of today's row 1.

### Scattering: the gate closed at cluster speeds

χ's self-interaction passes through a gate in the relative momentum of a colliding pair, and it is suppressed once two particles approach each other faster than the gate velocity v\* ([the gated scattering law σ_T(v)](../conjugate-matter/scattering-law.md)). Cluster collisions are far above v\*. The plain-language passage of [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) calls the result "self-interaction strong in cold dwarf galaxies, off in hot clusters", and row 1 of the predictions table makes it a requirement ([#11 §13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)):

| Observable | Program requirement | Killed by |
| --- | --- | --- |
| σ_T(v) across halo masses | Knee at v\* ~ 10² km/s; zero cluster signal (particle χ) | Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band |

A merging cluster such as this one is therefore a place where particle χ must show no self-scattering, and a robust self-interaction measured at cluster speeds would kill the row ([zero cluster signal, for particles](../../predictions/self-interaction-knee.md#zero-cluster-signal-for-particles)). Two published fits mildly prefer a nonzero cross-section at cluster speeds: about 0.1 cm²/g on cluster scales ([Kaplinghat, Tulin and Yu 2016](https://arxiv.org/abs/1508.03339)) and 0.19 ± 0.09 cm²/g in clusters, with an upper limit of 0.35 cm²/g at 95% confidence ([Sagunski et al. 2021](https://arxiv.org/abs/2006.12515)) [S]. Neither is the robust self-interaction that kills the row ([the data situation](../../predictions/self-interaction-knee.md#the-data-situation); flag 69, pending). The program's notes model a galaxy cluster with [velocity dispersion](velocity-dispersion.md#the-values-in-the-programs-notes) 1000 km/s, against 30 km/s for the core of a classical dwarf galaxy ([`notes/wave-island.md`](../../../notes/wave-island.md), 'What pins g? Two scenarios').

How much self-interaction remains above the knee depends on the gate's tail, which is open:

- **The v0.1 numbers.** The notebook's first gate was a postulated Gaussian. With it the notebook computed "σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0" and stated that "Cluster self-interaction is *identically zero at any future sensitivity* — a sharper statement than any Yukawa model can make, and a standing kill condition" ([#1 §5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d)). Its row 1 required "**exactly zero in clusters forever**", killed by "Robust nonzero self-interaction at v > 3v\*" ([#1 §9](../../../notes/broken-born-theory.md#9-predictions)). These statements are superseded ([the v0.1 predictions from the benchmark](../conjugate-matter/benchmark.md#superseded-the-v01-predictions-from-the-benchmark)).
- **The knee.** [Calc note #6](../../history/documents/field-equation-notes.md) found that "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" ([`notes/x-classification.md` §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade)). The lab notebook's v0.4 addendum amended row 1 accordingly: "the exponential cliff weakens to a sharp knee at v\* with tail shape (Gaussian vs rational) diagnosing the vertex completion" (#1 'Addendum (v0.4)', italics dropped and v_\* written v\*). A Gaussian tail makes self-interaction far above the knee negligible; a rational tail leaves a power-law remainder ([why the gate shape is observable](../conjugate-matter/gate-shape.md#why-it-is-observable)).
- **No comparison.** No source evaluates that remainder at cluster speeds or sets it against the Bullet Cluster limit, and the kill condition does not say how large a remainder counts as robust.

### Particles, waves and the other candidates

Row 1 attaches the qualifier "(particle χ)". If χ is light enough to behave as a classical wave (the regime called [the wave island](../momentum-clumping/wave-island/_index.md)), [the clumping notes](../../history/documents/clumping-notes.md) find that "The velocity suppression of self-interaction effects is e^{−v²/v\*²} on the particle island but (v\*/σ)⁴ on the wave island", with σ here the halo's velocity dispersion, not a cross-section ([`notes/wave-island.md`](../../../notes/wave-island.md), 'The rate', transcribed from its LaTeX). [#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) keeps the (v\*/σ)⁴ law for wave χ and writes the particle side as a "sharp cutoff". Telling the two apart is [row 3, the island discriminant](../../predictions/island-discriminant.md). Calc note [#3](../../../notes/wave-island.md)'s table of environments lists a cluster as "(0.03, 1000)", density in GeV/cm³ and dispersion in km/s, with a ratio of [the gated condensation rate](../momentum-clumping/wave-island/condensation-rate.md) to the orbital rate of "∼ 0" under [Scenario A](../momentum-clumping/wave-island/scenario-a.md), whose prediction for the ultra-faint dwarfs the data contradict; Scenario A is under review ([#11 §9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)). No source treats a cluster collision for wave χ, and none discusses the Bullet Cluster for the program's other candidates, [the X-condensate](../candidates/x-condensate.md) and P.R.'s conjecture of [magnetic monopoles abundant in momentum space](../candidates/momentum-space-monopoles.md) ([#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates)).

### The popular account

The popular article [#12](../../../popsci/universes-other-half.md) describes the requirement in the present tense, as if observed: "In galaxy-cluster collisions, at thousands of kilometers per second, the interaction shuts off and the dark matter passes through undisturbed — the behavior demanded by the Bullet Cluster" ('Dark matter as the other polarization'). In the program's documents this is row 1's requirement for particle χ, and no measurement of the gate is recorded ([the popular articles](../../history/documents/popular-articles.md)).

## References

The program's documents cite no source for the Bullet Cluster. Added by the wiki from model memory (†):

- M. Markevitch et al., Astrophys. J. (2004)†: limits on dark-matter self-interaction from the Bullet Cluster's offset, mass-to-light ratios and survival.
- D. Clowe et al., "A direct empirical proof of the existence of dark matter," Astrophys. J. Lett. (2006)†: the lensing map and its offset from the gas.
- S. W. Randall et al., Astrophys. J. (2008)†: limits on self-interaction from simulations of the collision.
- F. Kahlhoefer, K. Schmidt-Hoberg, M. T. Frandsen, S. Sarkar, "Colliding clusters and dark matter self-interactions," Mon. Not. R. Astron. Soc. (2014)†: how the angular pattern of the scattering changes what merging clusters constrain.

## Used by

- [The χ-particle candidate](../candidates/chi-particles.md) — "Bullet-Cluster-safe": lensing from universal gravity, no scattering at cluster speeds.
- [P4: polarized matter and strict sector separation](../../program/postulates/p4-polarized-matter.md) — universal coupling to H makes χ lens like ordinary dark matter.
- [The velocity gate](../conjugate-matter/velocity-gate.md) — closed at cluster speeds; [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate)'s sentence on the gate opens with the clause.
- [Row 1: the knee in σ_T(v)](../../predictions/self-interaction-knee.md) — "zero cluster signal (particle χ)".
- [The scattering benchmark](../conjugate-matter/benchmark.md) — the superseded v0.1 value at 1500 km/s.
- [Open: the gate shape (OP4)](../conjugate-matter/gate-shape.md) — how much self-interaction survives above the knee.
- [Row 7: a permanent null in direct detection](../../predictions/direct-detection-null.md) — the same clauses of P4 make dark matter gravitate like ordinary matter.
- [The equivalence principle as dual relativity](../../conjugate-relativity/equivalence-principle.md) — both kinds of matter fall alike.
- [The gated Vlasov model](../momentum-clumping/gated-vlasov-model.md) — χ falls in ordinary gravity like everything else.
- [Founding suppositions and their fates](../../program/founding-suppositions.md) — supposition 4: χ clusters in position, with a gated self-force.
- [Conjugate monopoles as ontology](../../electric-magnetic-duality/conjugate-monopoles.md) — whatever the conjugate sector contains gravitates.
- [The invariant-length shell and Planck closure](../../conjugate-relativity/invariant-length-shell.md) — [#11 §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) describes χ in ordinary kinematics.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §8](../../papers/broken-born-checkpoint-v2.md#8-conjugate-matter-and-the-gate) — "Bullet-Cluster-safe", the plain-language passage on lensing and on the gate in dwarfs and clusters; [§4](../../papers/broken-born-checkpoint-v2.md#4-postulates) — P4; [§9](../../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested) — the (v\*/σ)⁴ suppression on the wave island and the "sharp cutoff" for particles; Scenario A under review; [§12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — the three candidates; [§13 row 1](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — zero cluster signal for particle χ
- [`notes/broken-born-theory.md` §4](../../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured) — the lensing statement [D]; [§5.1](../../../notes/broken-born-theory.md#51-the-scattering-law-d) — the v0.1 value at 1500 km/s and "identically zero at any future sensitivity"; [§9](../../../notes/broken-born-theory.md#9-predictions) — the v0.1 row 1; 'Addendum (v0.4)' — the cliff weakened to a knee
- [`notes/broken-born-program-v1.md` §6](../../../notes/broken-born-program-v1.md#6-conjugate-matter-and-the-gate-the-gate-problem-mechanism-found) — the same clause in v1
- [`notes/x-classification.md` §4](../../../notes/x-classification.md#4-consequences-downstream-d--structural-with-one-honest-downgrade) — rational, power-law-tailed gates
- [`notes/wave-island.md`](../../../notes/wave-island.md) 'The rate' — the island discriminant; 'What pins g? Two scenarios' — the cluster and dwarf environments
- [`popsci/universes-other-half.md`](../../../popsci/universes-other-half.md) 'Dark matter as the other polarization' — the popular account (not a status source)
- [`notes/literature-check.md` §3](../../../notes/literature-check.md#3-dark-matter-is-conjugate-matter-c1-the-identification-is-published); [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 69 — two fits that mildly prefer a nonzero cross-section at cluster speeds; pending
