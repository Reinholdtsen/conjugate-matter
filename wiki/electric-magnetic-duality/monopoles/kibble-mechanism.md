---
title: "The Kibble mechanism"
weight: 30
status: established
description: "Causality limits how far a field can align at a symmetry-breaking transition, so at least about one defect forms per horizon volume; Kibble–Zurek dynamics and bubble nucleation only add more — a floor, not a ceiling."
provenance: [T]
sources:
  - "review/round3-adjudication.md 'Rulings' 3"
  - "review/round3-adjudication.md 'Rulings' 1"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3-adjudication.md 'Decisions' 3"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/step2a.out 'KIBBLE'"
  - "review/round3/referee/step4.out"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/broken-born-checkpoint-v2.md refs [28]–[29]"
  - "wiki/papers/broken-born-checkpoint-v2.md §14 item 12"
  - "wiki/papers/broken-born-checkpoint-v2.md §11.1"
  - "notes/closed-universe.md §9"
  - "review/wiki-build-flags.md flag 61"
  - "verify/closed_universe.py section F"
  - "verify/soliton_obituary.py 'Anchors'"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md ref [18]"
  - "review/v3-worklog.md 'Verified references for v3'"
  - "HANDOFF.md §2"
---

*The Kibble mechanism, proposed by Tom Kibble in 1976, is the standard account of how [topological defects](../../symmetry-breaking/topological-defects.md) such as [monopoles](_index.md), strings and domain walls form when the early universe cools through a symmetry-breaking transition. Regions farther apart than the horizon, the distance light has travelled since the Big Bang, have had no contact, so the field settles into unrelated vacuum states in different regions, and defects are left where those regions meet. This gives at least about one defect per horizon volume, and that count is a minimum: slow transitions (Kibble–Zurek dynamics) and first-order transitions, which proceed by bubbles, make more. In the program the count decided the fate of the withdrawn manuscript [#14](../../../notes/knot-dark-matter-standalone.md)'s model of a soliton dark-matter candidate, which had normalized it too low and treated it as an upper end; that error and its correction are recorded with #14's model.*

**Status:** Established — [T] — literature: the mechanism (Kibble 1976, reference [18] of the withdrawn [#14](../../dark-matter/candidates/soliton-candidate/_index.md)), the one-per-horizon normalization (Gangui, [astro-ph/0110285](https://arxiv.org/abs/astro-ph/0110285), which the round-3 referee cited and [the gate](../../method/verification/the-gate.md) uses as an anchor), and the floor, which the [checkpoint](../../history/documents/checkpoint.md) supports with Murayama–Shu [28S]. [Round 3](../../method/review/round-3/_index.md) upheld the floor as [ruling 3](../../method/review/round-3/rulings.md); the adjudicator did not re-run the referee's Kibble–Zurek integration. The program's own evaluation of the normalization, p ≈ 104 [V] ([#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates)), and #14's error belong to [Under review: the Kibble normalization](../../dark-matter/candidates/soliton-candidate/kibble-normalization.md); the value is gated in [`verify/soliton_obituary.py`](../../../verify/soliton_obituary.py) ([the soliton-obituary script](../../method/verification/soliton-obituary-script.md)). The explanations below are standard physics written from general knowledge [T]; references added from memory are marked †.

## Defects from a cooling field [T]

Above a symmetry-breaking temperature T_c the order parameter of a field theory, such as the adjoint scalar Φ of [the 't Hooft–Polyakov monopole](thooft-polyakov-monopole.md), averages to zero. Below T_c it takes a value on the vacuum manifold, the set of minima of its potential ([topological defects and the vacuum manifold](../../symmetry-breaking/topological-defects.md)). Nothing selects one point of that manifold over another, so the value is aligned only over a correlation length ξ, and regions farther apart than ξ settle at unrelated points.

Where regions with different vacuum values meet, the field interpolates between them. If the shape of the vacuum manifold M does not allow a smooth interpolation, the field is trapped away from its vacuum on a surface, a line or a point: a domain wall if M is in separate pieces (π₀), a string if it has loops that cannot be shrunk (π₁), a monopole if it has spheres that cannot be shrunk (π₂). The classification by these homotopy groups, and why a trapped configuration cannot unwind, are on [topological defects and the vacuum manifold](../../symmetry-breaking/topological-defects.md#the-classification-t). It is Kibble's: the round-3 audit summarizes the abstract of his 1976 paper as "formation of walls, strings or monopoles depends on homotopy groups" ([`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md), Step 1).

For monopoles of SU(2) → U(1) the vacuum manifold is a sphere. Where several domains meet, the directions they carry can wrap the sphere once, and a monopole or an antimonopole sits there; the fraction of meeting points at which this happens is a geometric number of order one [T]. The number density of monopoles is therefore of the order of one per correlation volume: n ~ ξ⁻³.

## The causal bound [T]

The correlation length cannot exceed the distance over which the field has been in causal contact. At the transition that distance is the horizon, of the order of the Hubble length H⁻¹ in the radiation era. So ξ ≲ H⁻¹ at T_c, and at least about one defect forms per Hubble volume:

```text
n ≳ H(T_c)³
```

The count is converted to a [yield](../../cosmology/early-universe/relic-yield-and-dilution.md#the-kibble-yield-t), the number per unit entropy n/s, because the yield stays constant as the universe expands once nothing creates or destroys the defects. In the radiation era the expansion rate and the entropy density are [T] ([the radiation era](../../cosmology/early-universe/radiation-era.md)):

```text
H = 1.66 √g* T²/M_Pl,        s = (2π²/45) g* T³
```

with g\* the number of relativistic degrees of freedom and M_Pl the [Planck mass](../../gravity/spin-2-fields/planck-units.md#one-convention-per-formula). One defect per H⁻³ at T_c then gives a yield proportional to the cube of T_c/M_Pl:

```text
n/s = p (T_c/M_Pl)³,        p = (1.66 √g*)³ · 45/(2π² g*)        (one defect per H⁻³)
```

The standard normalization in the literature is the one the round-3 referee took from Gangui ([astro-ph/0110285](https://arxiv.org/abs/astro-ph/0110285)): "about one monopole per Hubble volume ... n_monop/s ~ 100 (T_c/m_P)^3" (Step 1), with m_P the Planck mass, at g\* of order 100. Liveoak, Maharana and Wells describe the same count as the "minimal number density ... one per Hubble volume" (as the referee quotes them, Step 2).

Two choices move p. Which volume counts as one horizon (H⁻³, or the sphere (4π/3)H⁻³) is an order-one ambiguity in the estimate itself, and it changes the count by the ratio of the two volumes. Which Planck mass appears in H and in the yield (the Planck mass or the reduced Planck mass, which differ by a factor of √(8π)) is a convention: it changes the coefficient but not the physical count, provided the same one is used in both, while mixing the two between the yield and the formula for H does change the count. The program's record contains an instance of each ([how the program uses it](#how-the-program-uses-it)).

## A floor, not a ceiling [T]

The causal argument bounds the correlation length from above, so it bounds the number of defects from below. Real transitions correlate the field over less than a horizon, and so make more defects. Two mechanisms are standard.

### Continuous transitions: Kibble–Zurek

Zurek (1985†) applied the same reasoning to phase transitions in the laboratory and found that the dynamics of the transition, not causality alone, sets the correlation length. Near T_c the time the order parameter needs to relax to equilibrium grows without bound, the critical slowing down of a continuous transition. When that relaxation time exceeds the time left before the transition, the field can no longer follow the falling temperature, and its correlation length freezes at the value it has at that moment [T]. That value, ξ̂, is set by the cooling rate and by the critical exponents of the transition, and in the early universe, where the cooling time is the expansion time, it is much smaller than the horizon. The resulting count is Kibble–Zurek (KZ) production.

The round-3 referee took the cosmological estimate from Liveoak–Maharana–Wells (LMW), eq. 13: "Kibble-Zurek gives n ~ lambda H T_c^2, i.e. (M_Pl/T_c)^2 per horizon" (Step 2). Here λ is a coupling of the scalar sector, which the referee varied from 0.1 to 1 ([`review/round3/referee/step4.out`](../../../review/round3/referee/step4.out)). Since M_Pl is far larger than any transition temperature, this is many defects per horizon rather than one.

### First-order transitions: bubbles

A first-order transition proceeds by supercooling: the universe stays in the old phase below T_c, and bubbles of the new phase nucleate at random points and expand until they fill space. Inside each bubble the field takes its own vacuum value, independently of the other bubbles, so each bubble acts as a domain, and defects form where bubbles collide [T]. The nucleation rate per unit volume rises roughly exponentially in time, at a rate β, so β⁻¹ is the duration of the transition. With walls moving at a speed near that of light, the bubbles reach a size of order 1/β, and the number of domains per Hubble volume is of order (β/H)³ [T]. Fast transitions, β ≫ H, therefore make many more defects than one per horizon. The same bubble collisions source gravitational waves ([gravitational waves from phase transitions](../../cosmology/early-universe/phase-transition-gravitational-waves.md)).

### The literature

The checkpoint cites the floor to Murayama and Shu [28S], whose abstract, as ruling 3 quotes it, says that Kibble "drastically underestimates the production of topological defects" ([`review/round3-adjudication.md`](../../../review/round3-adjudication.md), 'Rulings' 3). Murayama and Shu, and Liveoak, Maharana and Wells [29S], use this production in hidden-sector models of topological dark matter ([topological dark matter in the literature](../../dark-matter/candidates/soliton-candidate/prior-art.md)).

What happens after formation is a separate question. Monopoles and antimonopoles can annihilate, which matters only if the initial yield is high enough, and [inflation](../../cosmology/early-universe/inflation-and-dilution.md) after the transition can dilute them; both belong to [the monopole problem](monopole-problem.md).

## How the program uses it

The Kibble count was the abundance estimate of #14's soliton model, and the error in it decided the model's fate. The full record is on [Under review: the Kibble normalization](../../dark-matter/candidates/soliton-candidate/kibble-normalization.md) and [overproduction at the benchmark](../../dark-matter/candidates/soliton-candidate/overproduction.md); this section summarizes it, and ends with the production question that the program's own order parameter raises.

### #14's normalization and direction

#14 v3 §3: "The Kibble mechanism [18] at a post-inflationary transition with T_c ~ v yields n/s ~ p (v/M_Pl)^3. One monopole per horizon volume with g\* = 100 gives p ~ 0.023; we take p = 1 as the upper end." Here v is the hidden symmetry-breaking scale. Round 3 found two errors in that sentence.

- **The value.** Ruling 1, upheld: "My code: p = 104.31 with M_Pl, 0.828 with the reduced M_Pl. v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³." In the formula of the previous section, 45/(2π² g\*) is what remains when the Friedmann prefactor is set to one; the referee's script prints "45/(2 pi^2 * 100) = 0.0228  <- equals n=(T^2/MPl)^3 i.e. H without 1.66 sqrt(g\*)" ([`review/round3/referee/step2a.out`](../../../review/round3/referee/step2a.out)). The checkpoint carries the corrected value: "One defect per Hubble volume gives p ≈ 104 [V], and that is the causal minimum; Kibble–Zurek and bubble-nucleation production only add to it [28S]" ([#11 §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates)).
- **The direction.** Ruling 3, upheld: "Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more". The referee judged #14's bracket from 0.023 to 1 unreasonable for that reason: p "should be >= ~25-100, not <= 1" (Step 2). The lower figure counts one defect per (4π/3)H⁻³: the referee's script prints "p(one per H^-3) = 104.31 ; p(one per (4pi/3)H^-3) = 24.90" at g\* = 100 (`step2a.out`). The adjudication and the gate use H⁻³.

The two Planck-mass values, 104.31 and 0.828, are the same count in two conventions; #14's reduced-Planck "factor of about 3" in its mass band came from changing the Planck mass without changing p, and ruling 2 found that "consistently normalized, the two conventions agree" ([Under review: the Kibble normalization](../../dark-matter/candidates/soliton-candidate/kibble-normalization.md)).

### The referee's estimates of the excess

The referee applied both mechanisms of the previous section at #14's parameters (Step 4(a)):

- **Bubbles.** [#14 §4](../../../notes/knot-dark-matter-standalone.md#4-observational-consistency) had considered a first-order transition with "f\*/H\* = 1-100". For it, "bubble counting gives p ~ 104 (beta/H)^3 = 1e2-1e8 (step4.out) - flatly inconsistent with "p = 1 as the upper end" of Sec. 3" (item 2). The script prints:

  ```text
  first-order with beta/H=1: p ~ 1.0e+02
  first-order with beta/H=10: p ~ 1.0e+05
  first-order with beta/H=100: p ~ 1.0e+08
  ```

- **Kibble–Zurek with annihilation.** Production by the LMW formula, followed by capture in the hidden plasma, leaves "Omega/Omega_DM = 1.1e12 - 2.2e12" at #14's benchmark; LMW's analytic eq. (25) "at these parameters: 1.2e9 - 2.2e11. Either way the annihilation does not rescue it" (item 3).

Ruling 3's evidence ends: "I did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction)." The wiki build's list of suspected source errors, item 21 of [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md), notes that the integration itself printed 1.1e12–2.2e12 and that the 1e9 lower end is the LMW analytic estimate's; the verdict, overproduction either way, is unaffected. The ruling is quoted here as written (flag 21, pending).

### The anchors in the gate

#14 v3's own check had reproduced its own number. Round-3 lesson 2: "An anchor must be independent of the paper. v3's Kibble anchor reproduced v2's own number and so tested nothing. The replacement anchors are the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume" ([independent anchors](../../method/verification/independent-anchors.md)). The gate now checks both literature values before the program's numbers; the relevant lines of the current run:

```text
== Anchors
PASS  Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl
PASS  one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)  [p = 104.31]

== Kibble normalization (ruling 1)
PASS  p = 104.31 with M_Pl  [104.3106]
PASS  p = 0.828 with reduced M_Pl  [0.8279]
PASS  v3's 0.0228 drops (1.66 sqrt(g*))^3 ~ 4.6e3  [4575.6]
```

### The √N floor

The [handoff](../../history/documents/handoff.md) had framed the relic question of its soliton candidate, #14's model, between a "Kibble ceiling" and a "√N floor" ([`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen), open item 2). [Round-3 Decision 3](../../method/review/round-3/decisions.md) dropped the calculation queued for it: "Its premise, Kibble as a ceiling, is inverted (ruling 3)" ([Under review: the √N topological floor (chat-only)](../../dark-matter/candidates/soliton-candidate/sqrt-n-floor.md)).

### The polarization's own defects (OP12)

The program's own symmetry breaking raises the same question. The polarization manifold Λ(4), the space of position/momentum splittings ([the Lagrangian Grassmannian](../../phase-space/modular-field/lagrangian-grassmannian.md)), has π₁(Λ(4)) = ℤ and π₂(Λ(4)) = ℤ₂ [T], with the maps behind them gated in [`verify/closed_universe.py`](../../../verify/closed_universe.py) section F ([the closed-universe script](../../method/verification/closed-universe-script.md#f-topology-of-the-polarization-manifold-8-checks)), for d = 4 and with the U(4) acting on the polarization global. [#11 §14 item 12](../../papers/broken-born-checkpoint-v2.md#14-open-problems) draws the consequence in this page's terms: "Selecting the polarization can then leave strings of τ (π₁; they exist on the light Maslov circle too) and, where the order parameter ranges over the whole manifold, point defects of the monopole type (π₂ = 0 on the circle). Whether a transition produced them, and their fate, are open [O]". Here τ is the program's dark-energy field, the angle around the Maslov circle of Λ(4) ([τ as the Maslov phase](../../phase-space/modular-field/maslov-phase.md)). The closed-universe note states the production question: "If a transition in the early universe selected the polarization, the ℤ₂ point defects and the τ-strings of §8 could form at it", and "Whether such a transition happened, what it left, and whether the point defects would pose a monopole problem of the program's own are not computed" ([`notes/closed-universe.md` §9 item 4](../../../notes/closed-universe.md#9-what-is-open); flag 61; [Open: point defects of the polarization (OP12)](../../symmetry-breaking/topological-defects.md#open-point-defects-of-the-polarization-op12)).

## References

- T. W. B. Kibble, "Topology of Cosmic Domains and Strings," J. Phys. A 9, 1387 (1976) — #14 [18], without a tag; the title is the v3 worklog's correction ('Verified references for v3'), and the round-3 audit checked the abstract.
- A. Gangui, [astro-ph/0110285](https://arxiv.org/abs/astro-ph/0110285) — the one-per-Hubble-volume normalization, cited by the round-3 referee and in the gate.
- H. Murayama, J. Shu, "Topological dark matter," Phys. Lett. B 686, 162 (2010), [arXiv:0905.1720](https://arxiv.org/abs/0905.1720) — #11 [28S].
- D. Liveoak, A. Maharana, J. D. Wells, "Dark monopoles, bounds on hidden sectors, and cosmological implications," [arXiv:2607.20843](https://arxiv.org/abs/2607.20843) (2026) — #11 [29S].

Added by the wiki from model memory (†):

- W. H. Zurek (1985)†: the freeze-out of the correlation length at a continuous transition.
- A. Vilenkin, E. P. S. Shellard, *Cosmic Strings and Other Topological Defects* (Cambridge University Press)†: textbook treatment of defect formation.

## Used by

- [Under review: the Kibble normalization](../../dark-matter/candidates/soliton-candidate/kibble-normalization.md) — #14's p = 0.023 and the corrected p ≈ 104.
- [Overproduction at the benchmark](../../dark-matter/candidates/soliton-candidate/overproduction.md) — the closing mass at minimum production.
- [The monopole problem](monopole-problem.md) — the production side of the monopole abundance.
- [Under review: the √N topological floor (chat-only)](../../dark-matter/candidates/soliton-candidate/sqrt-n-floor.md) — its queued calculation was dropped because its premise, Kibble as a ceiling, is inverted.
- [The soliton-obituary script](../../method/verification/soliton-obituary-script.md) — the one-per-Hubble-volume anchor.
- [Independent anchors](../../method/verification/independent-anchors.md) — v3's circular Kibble anchor and its replacement.
- [Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md) — the abundance estimate whose error decided the model's fate.
- [Benchmark-conditional arithmetic](../../dark-matter/candidates/soliton-candidate/benchmark-arithmetic.md) — a pure Kibble abundance closes at a single mass.
- [W′ overclosure: the minimal sector is excluded](../../dark-matter/candidates/soliton-candidate/w-prime-overclosure.md) — the transition at which the monopoles were to be made.
- [Open: the topological loophole](../../dark-matter/momentum-clumping/topological-loophole.md) — #14's model of the loophole's candidate took its abundance from the Kibble estimate.
- [Conjecture: conjugate monopoles explain the null result](../monopole-explanation.md) — at least about one monopole per causally connected region, which inflation dilutes in one of the standard histories set against the explanation.
- [Row 8: no monopoles of our sector](../../predictions/monopole-null.md) — the production of superheavy monopoles at a unification transition, which inflation, one of the standard histories under which the row's null is expected, would dilute ([#11 §11.1](../../papers/broken-born-checkpoint-v2.md#111-the-monopole-audit-revised-d)).
- [Open: point defects of the polarization (OP12)](../../symmetry-breaking/topological-defects.md#open-point-defects-of-the-polarization-op12) — whether a transition that selected the polarization produced point defects and τ-strings, and whether they would pose a monopole problem of the program's own, is not computed.

## Sources

- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Rulings' 1, 2 and 3, 'Lessons', 'Decisions' 3 — the corrected normalization, the floor and its evidence, the anchor lesson, the dropped √N floor.
- [`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 1, Step 2, Step 4(a), Step 4(c) — Kibble's abstract and Gangui's normalization; the floor and the Kibble–Zurek count; bubble counting and the integration; Murayama–Shu.
- [`review/round3/referee/step2a.out`](../../../review/round3/referee/step2a.out) (the Kibble block), [`review/round3/referee/step4.out`](../../../review/round3/referee/step4.out) — the computed p values and the first-order lines.
- [`wiki/papers/broken-born-checkpoint-v2.md` §12](../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates), refs [28]–[29] — p ≈ 104 [V] as the causal minimum, and the two live-searched references; [§14 item 12](../../papers/broken-born-checkpoint-v2.md#14-open-problems) — the polarization's defects, their production and fate open [O]; [§11.1](../../papers/broken-born-checkpoint-v2.md#111-the-monopole-audit-revised-d) — inflation as one of the standard histories.
- [`notes/closed-universe.md` §9 item 4](../../../notes/closed-universe.md#9-what-is-open), [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) flag 61, [`verify/closed_universe.py`](../../../verify/closed_universe.py) section F — the production question for the polarization's defects, not computed; the homotopy groups behind them.
- [`verify/soliton_obituary.py`](../../../verify/soliton_obituary.py) — the Friedmann and one-per-Hubble-volume anchors and p = 104.31.
- [`notes/knot-dark-matter-standalone.md` §3](../../../notes/knot-dark-matter-standalone.md#3-the-candidate), ref [18] — v3's p ~ 0.023 "as the upper end" (withdrawn), and the citation of Kibble 1976.
- [`review/v3-worklog.md`](../../../review/v3-worklog.md) 'Verified references for v3' — the corrected title of Kibble's paper.
- [`HANDOFF.md` §2](../../../HANDOFF.md#2-scientific-state-one-screen) — the "Kibble ceiling" of the superseded open item 2.
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 21 — the suspected misattribution in ruling 3's range.
