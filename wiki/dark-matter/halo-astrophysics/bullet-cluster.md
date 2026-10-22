---
title: "The Bullet Cluster"
weight: 25
status: established
description: "Two galaxy clusters seen after a collision, whose lensing mass moved on with the galaxies while the X-ray-emitting gas was slowed: evidence for a separate, nearly collisionless dark matter and a limit on self-scattering at cluster speeds; the program's χ is 'Bullet-Cluster-safe' through universal gravity and a gate closed at cluster speeds, with no number compared."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13 row 1"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §6"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt3b-wave-island.md 'The rate'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "popsci/universes-other-half.md 'Dark matter as the other polarization'"
---

*The Bullet Cluster is a pair of galaxy clusters seen shortly after the smaller one passed through the larger. A cluster has three components: its galaxies; hot, thin gas between them, which emits X-rays and outweighs the stars; and dark matter, which outweighs both. In the collision the two gas clouds struck each other and were slowed, while the galaxies passed through. The total mass, mapped by the way the clusters' gravity bends light from more distant galaxies, moved on with the galaxies and not with the gas. The observation is widely cited as direct evidence that most of a cluster's mass is a separate, nearly collisionless dark matter, and it limits how strongly dark matter can scatter off itself at the speeds of cluster collisions. The Broken-Born program calls its [conjugate matter](/wiki/dark-matter/conjugate-matter) "Bullet-Cluster-safe": it gravitates and bends light as ordinary matter does, and its self-interaction is switched off at cluster speeds by [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate). The program's documents quote no number for the limit and do not compare the gate with it.*

**Status:** Established — [T] — observational astrophysics written here from general knowledge, with the literature it names marked † (Markevitch et al. 2004 †; Clowe et al. 2006 †; Randall et al. 2008 †; Kahlhoefer et al. 2014 †); the program's documents cite no paper for it and quote no number from it. The program's uses are the lab notebook's lensing statement (#1 §4), tagged [D], the clause "Bullet-Cluster-safe" in #11 §8, and row 1's requirement of "zero cluster signal (particle χ)" (#11 §13); no `verify/` script checks any of them.

## What was observed [T]

### Three components in a collision

A galaxy cluster is the largest kind of gravitationally bound system. Most of its ordinary matter is not in its galaxies but in gas between them, hot enough to shine in X-rays, and most of its mass is dark matter, detected by its gravity alone. In a collision of two clusters the three components behave differently:

- **Galaxies** are small compared with the distances between them, so the galaxies of one cluster pass between those of the other almost without colliding.
- **Gas** fills the volume of each cluster, so the two gas clouds cannot pass through each other. Each is slowed by the pressure of the gas it runs into and falls behind its galaxies.
- **Dark matter** passes through as the galaxies do if its particles do not scatter off one another. If they do scatter, it is slowed or partly scattered out, as the gas is, though more weakly.

### The system

The Bullet Cluster consists of two clusters, one smaller than the other, seen shortly after the smaller passed through the larger. The collision runs nearly in the plane of the sky, across the line of sight, so the separation of the components is visible. X-ray images show the gas of both clusters lying between the two groups of galaxies. The smaller cluster's gas forms a cloud shaped like a bullet, with a bow shock, a front of compressed hot gas, ahead of it, which gave the system its name.

Gravitational lensing maps the total mass, ordinary and dark. The gravity of the clusters bends light from galaxies far behind them, which distorts their apparent shapes slightly and in a coherent pattern; from the pattern the projected mass can be reconstructed. In the Bullet Cluster the lensing map has two mass concentrations, one at each group of galaxies, and both are offset from the gas (Clowe et al. 2006 †).

## What it shows [T]

### Dark matter as a separate component

The gas holds most of the ordinary mass. If the ordinary matter were all of the mass, the lensing map would peak on the gas. It peaks instead on the galaxies, which hold a smaller part of the ordinary mass. Most of the mass is therefore something other than the ordinary matter, and it passed through the collision as the galaxies did. Clowe and collaborators titled their paper "A direct empirical proof of the existence of dark matter" (2006 †). The observation is also widely cited as a difficulty for theories that replace dark matter with a modification of gravity, since in those theories the gravitational field is set by the visible matter.

### The limit on self-scattering [T]

If dark-matter particles scatter off one another, the two dark-matter halos interacted during the collision. Three consequences have been used to bound the scattering, each expressed as a cross-section per unit mass (Markevitch et al. 2004 †; Randall et al. 2008 †):

- **Offset.** Scattering would slow the smaller cluster's dark matter relative to its galaxies and displace its mass peak toward the gas. The lensing peak and the galaxies coincide within the errors of the measurement.
- **Mass loss.** Particles scattered through large angles would leave the smaller cluster, which would lower its ratio of mass to light compared with the larger cluster's. No such deficit is seen.
- **Survival.** A dark-matter particle of the smaller cluster that crosses the larger one passes through a column of dark matter of surface density Σ, its mass per unit area on the sky. The expected number of scatterings on the way is τ = (σ/m)·Σ, with σ/m the cross-section per unit mass. The smaller cluster kept its dark matter, so τ cannot be large, which bounds σ/m.

The bounds hold at the relative speed of this collision, far above the internal speeds of dwarf galaxies. A cross-section that falls with speed can be small here and still large in dwarfs, so a self-interaction strong enough to make the cores of dwarf galaxies can meet the cluster limits by weakening at cluster speeds ([why velocity dependence matters](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#why-velocity-dependence-matters-t)). How an offset or a loss of mass translates into [the transfer cross-section](/wiki/dark-matter/halo-astrophysics/transfer-cross-section) per unit mass, σ_T/m, also depends on the angular pattern of the scattering: rare scatterings through large angles remove particles, while frequent scatterings through small angles, as with a light mediator, act on a halo as a drag (Kahlhoefer et al. 2014 †; [the angular pattern](/wiki/dark-matter/halo-astrophysics/transfer-cross-section#the-angular-pattern-t)).

No program document quotes a value of these limits, and this page gives none.

## How the program meets it

The program's documents treat the observation in two halves, as the lab notebook first did: the lensing, which follows from how conjugate matter gravitates, and the scattering, which is the subject of the predictions table's [row 1](/wiki/predictions/self-interaction-knee).

### Lensing: one gravity for both kinds of matter

The program's postulate [P4](/wiki/program/postulates/p4-polarized-matter) [P] reads: "Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H; gauge forces do not cross polarizations" (#11 §4). H is the [generalized metric](/wiki/phase-space/born-geometry/born-structures) on phase space, and on the program's vacuum it contains the spacetime metric g, so conjugate matter χ couples to g in the same way as ordinary matter ([one gravity for both](/wiki/program/postulates/p4-polarized-matter#one-gravity-for-both)). It therefore falls, orbits and bends light like any other mass, as general relativity requires of everything that couples to the metric ([minimal coupling and free fall](/wiki/gravity/spin-2-fields/general-relativity#minimal-coupling-and-free-fall-t); [the equivalence principle](/wiki/gravity/spin-2-fields/equivalence-principle)).

[The lab notebook](/wiki/history/documents/lab-notebook) draws the consequence for the Bullet Cluster, tagged [D] (#1 §4, transcribed from its LaTeX):

> "χ couples to g universally: it falls, orbits, and lenses like ordinary dark matter. Bullet Cluster lensing-centroid behavior is automatic (and see Prediction 1 for the scattering side)."

[The checkpoint](/wiki/history/documents/checkpoint) keeps it in one clause: "χ propagates on g (equivalence principle; Bullet-Cluster-safe)" (#11 §8). The first consolidation, v1, has the same clause with a comma for the semicolon (#9 §6), and the plain-language passage of #11 §8 says that conjugate matter "falls and bends light like everything else". The notebook's Prediction 1 is the first form of today's row 1.

### Scattering: the gate closed at cluster speeds

χ's self-interaction passes through a gate in the relative momentum of a colliding pair, and it is suppressed once two particles approach each other faster than the gate velocity v\* ([the gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law)). Cluster collisions are far above v\*. The plain-language passage of #11 §8 calls the result "self-interaction strong in cold dwarf galaxies, off in hot clusters", and row 1 of the predictions table makes it a requirement (#11 §13):

| Observable | Broken-Born requirement | Killed by |
| --- | --- | --- |
| σ_T(v) across halo masses | Knee at v\* ~ 10² km/s; zero cluster signal (particle χ) | Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band |

A merging cluster such as this one is therefore a place where particle χ must show no self-scattering, and a robust self-interaction measured at cluster speeds would kill the row ([zero cluster signal, for particles](/wiki/predictions/self-interaction-knee#zero-cluster-signal-for-particles)). The program's notes model a galaxy cluster with velocity dispersion 1000 km/s, against 30 km/s for the core of a classical dwarf galaxy (`notes/debt3b-wave-island.md`, 'What pins g? Two scenarios').

How much self-interaction remains above the knee depends on the gate's tail, which is open:

- **The v0.1 numbers.** The notebook's first gate was a postulated Gaussian. With it the notebook computed "σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0" and stated that "Cluster self-interaction is *identically zero at any future sensitivity* — a sharper statement than any Yukawa model can make, and a standing kill condition" (#1 §5.1). Its row 1 required "**exactly zero in clusters forever**", killed by "Robust nonzero self-interaction at v > 3v\*" (#1 §9). These statements are superseded ([the v0.1 predictions from the benchmark](/wiki/dark-matter/conjugate-matter/benchmark#superseded-the-v01-predictions-from-the-benchmark)).
- **The knee.** [Calc note #6](/wiki/history/documents/debt-1-notes) found that "tree-level exchange with generic vertices yields rational (power-law-tailed) gates; the Gaussian requires the Gaussian fiber profile" (`notes/debt1a-ii-X-classification.md` §4). The lab notebook's v0.4 addendum amended row 1 accordingly: "the exponential cliff weakens to a sharp knee at v\* with tail shape (Gaussian vs rational) diagnosing the vertex completion" (#1 'Addendum (v0.4)', italics dropped and v_\* written v\*). A Gaussian tail makes self-interaction above the knee negligible; a rational tail leaves a power-law remainder ([why the gate shape is observable](/wiki/dark-matter/conjugate-matter/gate-shape#why-it-is-observable)).
- **No comparison.** No source evaluates that remainder at cluster speeds or sets it against the Bullet Cluster limit, and the kill condition does not say how large a remainder counts as robust.

### Particles, waves and the other candidate

Row 1 attaches the qualifier "(particle χ)". If χ is light enough to behave as a classical wave, the Debt-3 notes find that "The velocity suppression of self-interaction effects is e^{−v²/v\*²} on the particle island but (v\*/σ)⁴ on the wave island", with σ here the halo's velocity dispersion, not a cross-section (`notes/debt3b-wave-island.md`, 'The rate', transcribed from its LaTeX; #11 §9). Telling the two apart is [row 3, the island discriminant](/wiki/predictions/island-discriminant). Debt 3b's table of environments lists a cluster as "(0.03, 1000)", density in GeV/cm³ and dispersion in km/s, with a ratio of the wave-island rate to the orbital rate of "∼ 0" under [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), which has since been falsified. No source treats a cluster collision for wave χ, and none discusses the Bullet Cluster for the program's other candidate, [the X-condensate](/wiki/dark-matter/candidates/x-condensate) (#11 §12).

### The popular account

The popular article #12 describes the requirement in the present tense, as if observed: "In galaxy-cluster collisions, at thousands of kilometers per second, the interaction shuts off and the dark matter passes through undisturbed — the behavior demanded by the Bullet Cluster" ('Dark matter as the other polarization'). In the program's documents this is row 1's requirement for particle χ, and no measurement of the gate is recorded ([the popular articles](/wiki/history/documents/popular-articles)).

## References

The program's documents cite no source for the Bullet Cluster. Added by the wiki from model memory (†):

- M. Markevitch et al., Astrophys. J. (2004)†: limits on dark-matter self-interaction from the Bullet Cluster's offset, mass-to-light ratios and survival.
- D. Clowe et al., "A direct empirical proof of the existence of dark matter," Astrophys. J. Lett. (2006)†: the lensing map and its offset from the gas.
- S. W. Randall et al., Astrophys. J. (2008)†: limits on self-interaction from simulations of the collision.
- F. Kahlhoefer, K. Schmidt-Hoberg, M. T. Frandsen, S. Sarkar, "Colliding clusters and dark matter self-interactions," Mon. Not. R. Astron. Soc. (2014)†: how the angular pattern of the scattering changes what merging clusters constrain.

## Used by

- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) — "Bullet-Cluster-safe": lensing from universal gravity, no scattering at cluster speeds.
- [P4: polarized matter and strict sector separation](/wiki/program/postulates/p4-polarized-matter) — universal coupling to H makes χ lens like ordinary dark matter.
- [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) — closed at cluster speeds; #11 §8's sentence on the gate opens with the clause.
- [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) — "zero cluster signal (particle χ)".
- [The scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) — the superseded v0.1 value at 1500 km/s.
- [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape) — how much self-interaction survives above the knee.
- [Row 7: a permanent null in direct detection](/wiki/predictions/direct-detection-null) — the same clauses of P4 make dark matter gravitate like ordinary matter.
- [The equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle) — both kinds of matter fall alike.
- [The gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) — χ falls in ordinary gravity like everything else.
- [Founding suppositions and their fates](/wiki/program/founding-suppositions) — supposition 4: χ clusters in position, with a gated self-force.
- [Conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles) — whatever the conjugate sector contains gravitates.
- [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell) — #11 §8 describes χ in ordinary kinematics.

## Sources

- `papers/broken-born-checkpoint-v2.md` §8 — "Bullet-Cluster-safe", the plain-language passage on lensing and on the gate in dwarfs and clusters; §4 — P4; §9 — the (v\*/σ)⁴ suppression on the wave island; §12 — the two remaining candidates; §13 row 1 — zero cluster signal for particle χ
- `notes/broken-born-theory.md` §4 — the lensing statement [D]; §5.1 — the v0.1 value at 1500 km/s and "identically zero at any future sensitivity"; §9 — the v0.1 row 1; 'Addendum (v0.4)' — the cliff weakened to a knee
- `notes/broken-born-program-v1.md` §6 — the same clause in v1
- `notes/debt1a-ii-X-classification.md` §4 — rational, power-law-tailed gates
- `notes/debt3b-wave-island.md` 'The rate' — the island discriminant; 'What pins g? Two scenarios' — the cluster and dwarf environments
- `popsci/universes-other-half.md` 'Dark matter as the other polarization' — the popular account (not a status source)
