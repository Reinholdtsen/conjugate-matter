---
title: "The transfer cross-section σ_T"
weight: 15
status: established
description: "σ_T = ∫(1 − cos θ) dσ, which weights each collision by the forward momentum it removes: why it and not the total cross-section measures self-scattering in a halo, its quotation per unit mass in cm²/g, its speed dependence for contact and long-range forces, isotropic against forward-peaked scattering, related measures, and the program's uses."
provenance: [T]
sources:
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §13 rows 1–3"
  - "papers/broken-born-checkpoint-v2.md §14 items 4–5"
  - "notes/debt3a-stream-stability.md 'Setup'"
  - "notes/debt3a-stream-stability.md 'Numbers at the scattering benchmark'"
  - "notes/debt3a-stream-stability.md 'Consequences for the predictions table'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/knot-dark-matter-standalone.md §4"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/step2a.out"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/wiki-build-checks/audit/flag17_recompute.out sections 3, 5"
  - "HANDOFF.md §6"
---

*The transfer cross-section σ_T measures how strongly particles scatter off one another by counting each collision according to how much forward momentum it removes: σ_T = ∫(1 − cos θ) dσ, where θ is the angle through which the collision turns the particles' relative motion. A grazing collision, which barely bends their paths, counts for almost nothing, and a head-on rebound counts most. For dark matter that scatters off itself, σ_T, rather than the plain count of collisions, is the standard measure of how fast scattering moves momentum and heat through a halo. Because the motions of stars and gas reveal the mass density of dark matter but not the mass of its particles, observations constrain σ_T per unit mass, σ_T/m, quoted in cm²/g. How σ_T changes with the speed of a collision depends on the force: it stays constant for a short-range contact force, and it falls steeply with speed for a long-range force, whose scattering is concentrated at small angles. This page is the established quantity. The Broken-Born program states its dark-matter predictions in it: its own law, [the gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law), bends down at a knee near a gate velocity v\* and is isotropic below it, and the first three rows of [the predictions table](/wiki/predictions) are written in terms of it.*

**Status:** Established — [T] — standard scattering theory and halo astrophysics, written here from general knowledge, with the literature it names marked † (Chapman and Cowling †; Tulin, Yu and Zurek 2013 †; Tulin and Yu 2018 †; Kaplinghat, Tulin and Yu 2016 †; Kahlhoefer et al. 2014 †); the program's documents use σ_T without citing a source for it. No `verify/` script computes a transfer cross-section. Executed checks that are not part of `scripts/check.sh` exist for two sets of values: the withdrawn soliton candidate's σ_T/M, recomputed by the [round-3](/wiki/method/review/round-3) referee (`review/round3/referee/step2a.out`), and the lab notebook's v0.1 values above the gate, recomputed in [the audit of the wiki-build flags](/wiki/status/open-problems#pending-rulings) (`review/wiki-build-checks/audit/flag17_recompute.out`).

## The definition [T]

### The momentum one collision removes

A collision between two particles is simplest to describe in their centre-of-mass frame, where they approach each other with equal and opposite momenta of size k, the relative momentum of the pair. An elastic collision keeps that size and turns the direction through the scattering angle θ. Along the original line of approach each particle's momentum goes from k to k cos θ, so the collision removes k(1 − cos θ) of forward momentum: none at θ = 0, where the paths are unchanged, and the most at θ = π, where the particles rebound along the line they came in on.

The differential cross-section dσ/dΩ says how the collisions are distributed over directions, Ω being solid angle. Weighting each direction by the momentum a collision into it removes gives the transfer cross-section:

```text
σ_T = ∫ dΩ (1 − cos θ) dσ/dΩ
```

It is also called the momentum-transfer cross-section. A particle moving through a population of others, with number density n and relative speed v, loses forward momentum over its collisions at a rate proportional to n σ_T v. σ_T is therefore the cross-section of drag and of momentum relaxation, and in the kinetic theory of gases the same weighting governs diffusion (Chapman and Cowling †).

### Against the total cross-section

The total cross-section, σ_tot = ∫ dΩ dσ/dΩ, counts every collision once, however little it changes. The two measures differ according to how the scattering is spread over angle:

- **Isotropic scattering**, equally likely in every direction. The cos θ term averages to zero over the sphere, and σ_T equals σ_tot.
- **Forward-peaked scattering**, concentrated at small θ. Most collisions are grazing and remove little momentum, so σ_T is much smaller than σ_tot.
- **A long-range force.** For the Coulomb force the Rutherford cross-section grows as 1/sin⁴(θ/2) toward small angles, and σ_tot is infinite: a particle passing at any distance is deflected a little. The weight 1 − cos θ = 2 sin²(θ/2) cancels two of those powers. Cut off at a smallest angle, σ_tot grows as the inverse square of that angle and σ_T only as its logarithm. A real force is cut off at large distances, by screening in a plasma or by the mass of the particle that carries it, which sets the smallest angle; σ_T is then finite and carries the logarithm of the cutoff, the Coulomb logarithm ln Λ.

In each case σ_T counts the collisions that change the motion, while σ_tot can be dominated by collisions that change almost nothing.

### Related measures

- **The viscosity cross-section**, σ_V = ∫ dΩ sin²θ dσ/dΩ, gives little weight to both forward and backward scattering. In the kinetic theory of gases this weighting governs viscosity and heat conduction, while the weight 1 − cos θ governs diffusion (Chapman and Cowling †). Studies of self-interacting dark matter use both measures (Tulin and Yu 2018 †).
- **Identical particles.** When the two colliding particles are identical, a deflection through θ and one through π − θ produce the same final state, and dσ/dΩ is symmetric under θ → π − θ. The cos θ term then averages to zero for any angular distribution, so σ_T as defined equals σ_tot. A backward rebound, which for identical particles is a grazing collision with the labels exchanged, receives the largest weight. For identical particles the literature therefore uses σ_V, or a transfer cross-section weighted by 1 − |cos θ| (Tulin and Yu 2018 †).
- **For isotropic scattering** each of these measures is a fixed multiple of σ_tot. The choice then changes the normalization of a cross-section, not its dependence on speed.

The program's documents call σ_T "the momentum-transfer cross-section" (#1 §5.1) and do not discuss the variants.

## Per unit mass [T]

The rate at which one particle scatters, counted by σ_T, is Γ = n σ_T v. Dark matter is observed only through its gravity, which measures the mass density ρ = nm and the speeds of the matter in a halo, not the mass m of one particle. In those terms

```text
Γ = ρ (σ_T/m) v
```

so observations constrain the cross-section per unit mass, σ_T/m, and not σ_T itself. The customary unit is cm²/g.

The rate is what changes a halo of [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter) (SIDM): collisions carry heat into the colder center and turn a central cusp of density into a core, which needs only about one scattering per particle over the halo's age ([what self-scattering does to a halo](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#what-self-scattering-does-to-a-halo-t)). [Debt 3a](/wiki/history/documents/debt-3-notes) contrasts that requirement with the one for collective effects: "scattering fits only need Γt ∼ 1 over Gyr, which is ~30 orders cheaper" (`notes/debt3a-stream-stability.md`, 'Numbers at the scattering benchmark').

Reading a cross-section per unit mass as a bare cross-section is a large error. [The handoff](/wiki/history/documents/handoff) lists among the errors of the program's first blind-review referee "σ_T/M misread as σ_T (off ~10⁴³)" (`HANDOFF.md` §6), M being the mass of the soliton candidate ([the measured referee failure mode](/wiki/method/review/referee-failure-mode)).

### Averaged over speeds

Within a halo, pairs of particles meet at a spread of relative speeds set by the halo's velocity dispersion, so what the halo responds to is the rate averaged over that spread, ρ⟨σ_T v⟩/m. When σ_T depends on speed, a fit to one halo's structure measures this average, which is often reported as a cross-section at a speed characteristic of the halo [T].

Halos of different mass have different internal speeds. The [Debt-3 notes](/wiki/history/documents/debt-3-notes) model a classical dwarf core with velocity dispersion 30 km/s and a galaxy cluster with 1000 km/s (`notes/debt3b-wave-island.md`, 'What pins g? Two scenarios'). A set of halos from dwarf galaxies to clusters therefore samples σ_T/m over a range of speeds, and fits of such sets have been used to infer σ_T/m as a function of the collision speed (Kaplinghat, Tulin and Yu 2016 †). This is the sense of "across halo masses" in [row 1](/wiki/predictions/self-interaction-knee). No program document cites such a fit.

## Speed dependence [T]

### What sets it

How σ_T changes with speed follows from how the force depends on the momentum transfer q, the change in either particle's momentum. A collision with relative momentum k turned through θ transfers q = 2k sin(θ/2), from zero for a grazing collision to 2k for a head-on rebound. In the Born approximation, the first-order treatment of a weak interaction, the scattering amplitude is proportional to the Fourier transform of the potential at wavenumber q. A collision thus reads the potential's spectrum at the wavenumbers it transfers, and a faster collision reaches further out in that spectrum.

For a force carried by a mediator particle of mass m_φ, the potential is of Yukawa form and its spectrum is proportional to 1/(q² + m_φ²). Two limits bracket the behaviour ([contact and Yukawa forces](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#contact-and-yukawa-forces)):

- **A contact force**, with m_φ large compared with the transfers. The spectrum is flat over the wavenumbers a collision reaches, the amplitude is the same at every angle, the scattering is isotropic, and σ_T does not depend on speed.
- **A light mediator**, with m_φ small compared with the transfers. The spectrum approaches the Coulomb form 1/q², and the scattering is forward-peaked. At a fixed angle the transfer grows in proportion to the speed, so the amplitude falls as v⁻² and the differential cross-section as v⁻⁴. Integrated with the weight 1 − cos θ, σ_T falls as v⁻⁴ multiplied by a Coulomb logarithm, whose cutoff the mediator mass supplies. [The lab notebook](/wiki/history/documents/lab-notebook) states this standard behaviour as "Yukawa SIDM falls as v⁻⁴ with a Coulomb-log correction" (#1 §5.1).

For a pure Coulomb force with coupling α between particles of reduced mass m_r, the standard result in natural units is

```text
σ_T ≈ 4π α² ln Λ / (m_r² v⁴)
```

the form the round-3 referee used as "standard 4 pi a^2 lnL/(mu^2 v^4)", mu being the reduced mass (`review/round3/referee/audit-notes.md`, Step 2; evaluated in `review/round3/referee/step2a.out`).

At stronger coupling the Born approximation fails, and σ_T(v) passes through resonant and classical regimes with a more complicated dependence on speed (Tulin, Yu and Zurek 2013 †; [the Born regime and beyond](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#the-born-regime-and-beyond)).

### Why it is observable

A cross-section large enough to make cores in slow dwarf galaxies would, if it kept that size at all speeds, also scatter strongly in fast galaxy clusters, where collisions such as [the Bullet Cluster](/wiki/dark-matter/halo-astrophysics/bullet-cluster) limit it. A σ_T that falls with speed can meet both conditions, and the shape of the fall distinguishes the models ([why velocity dependence matters](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter#why-velocity-dependence-matters-t)). The lab notebook places the band where its own law and the Yukawa form separate most at "v ∼ 150–400 km/s (large spirals, small groups)" (#1 §5.1).

## The angular pattern [T]

σ_T compresses an angular distribution into one number, and two distributions with the same σ_T can still act differently on a halo.

- **Relaxation.** Isotropic and forward-peaked scattering move energy and momentum through a halo with different efficiencies. The lab notebook: "Energy- vs momentum-transport efficiencies differ, which feeds into halo relaxation morphology" (#1 §5.1). Halo relaxation morphology, the structure a halo settles into as scattering redistributes heat, is the observable named in the notebook's version of [row 2](/wiki/predictions/scattering-isotropy), "Scattering anisotropy (via halo relaxation morphology)" (#1 §9).
- **Collisions of halos.** When two halos collide, rare scatterings through large angles knock particles out, while frequent scatterings through small angles, as with a light mediator, act as a drag that slows a halo without removing much of it. An offset or a loss of mass measured in a merging cluster therefore translates into σ_T/m differently for the two patterns (Kahlhoefer et al. 2014 †; [the limit on self-scattering](/wiki/dark-matter/halo-astrophysics/bullet-cluster#the-limit-on-self-scattering-t)).

## How the program uses it

### The gated law σ_T(v)

[Conjugate matter χ](/wiki/dark-matter/conjugate-matter), whose particles are one of the program's two remaining dark-matter candidates ([the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles)), scatters off itself through the amplitude

```text
M(k, q) = 4πα̃ m_χ / (q² + m_φ²) · F(k²/μ²)        (#11 §8)
```

a Yukawa factor in the transfer q multiplied by a gate F in the incoming relative momentum k, which [the checkpoint](/wiki/history/documents/checkpoint) calls "the variable no x-local mediator produces" (#11 §8), x-local meaning local in position ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate#the-amplitude)). Its speed dependence therefore comes from the gate, not from the range of transfers a collision reaches. #11 states the consequence in σ_T:

> "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*; tail (Gaussian vs rational) diagnoses the vertex completion; isotropic below the gate versus Yukawa forward-peaking." (#11 §8)

The amplitude is tagged [D — mechanism; shape [O]]. In the terms of this page, the lab notebook took the mediator to be heavy, "m_φ ≳ m_χ, contact-like in x" (#1 §5.1), so below the gate the scattering is the contact case, flat in speed and isotropic, and above it the gate, not the mediator, cuts σ_T off. The audit of the wiki-build flags computed the Born σ_T with the full Yukawa factor kept and no gate, and found that at the benchmark masses its change between zero speed and the gate velocity is negligible: "the v-dependence of sigma_T is the gate's alone" (`review/wiki-build-checks/audit/flag17_recompute.out`, section 3; an audit check, not part of `scripts/check.sh`). The notebook's v0.1 law, with a Gaussian gate, was σ_T(v) = σ₀e^{−v²/v\*²}, "An exponential cliff, not a power-law tail" (#1 §5.1). Its v0.4 addendum weakened the cliff to a knee whose tail, Gaussian or rational, is open (#1 'Addendum (v0.4)'). The law and its history are on [the gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law), the superseded cliff on [Superseded: the exponential cliff of v0.1](/wiki/dark-matter/conjugate-matter/scattering-law#superseded-the-exponential-cliff-of-v01), and the open tail on [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape).

### Three rows of the predictions table

The first three rows of #11 §13 are stated in σ_T:

| Row | Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- | --- |
| [1](/wiki/predictions/self-interaction-knee) | σ_T(v) across halo masses | CDM none; Yukawa SIDM power-law + Coulomb log | Knee at v\* ~ 10² km/s; zero cluster signal (particle χ) | Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band |
| [2](/wiki/predictions/scattering-isotropy) | Scattering anisotropy | Forward-peaked (light mediators) | Isotropic below the gate | Morphology demanding forward peaking |
| [3](/wiki/predictions/island-discriminant) | Island discriminant | (not previously posed) | Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave | Diagnostic — selects the branch (particle vs wave χ) |

CDM is cold dark matter, which does not scatter off itself, and σ in row 3 is the velocity dispersion of a halo, not a cross-section. Row 1's standard expectations are cold dark matter's zero and the light-mediator case above, a v⁻⁴ fall with a Coulomb logarithm. The lab notebook's version of the row, with the same observable, also listed the contact case: "Constant (CDM: 0) or power-law v⁻⁴ln tail (Yukawa SIDM)" (#1 §9). Row 2 sets the isotropy of the contact case below the gate against the forward peaking of a light mediator. Row 3 reads the shape of σ_T's fall above the knee.

### The scattering benchmark

The program fixes the strength of the law from the cores of dwarf galaxies: "Fitting dwarf-scale cores wants σ₀/m_χ ≈ 30 cm²/g at v ≲ v\* ≈ 120 km/s" (#1 §5.1), a value stated without a citation. #11 §8 carries it in the benchmark mass m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3} ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)). Debt 3a writes the coupling through σ₀, g ≡ 4πα̃/m_φ² = √(πσ₀/m²) ('Setup'; [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)), and concludes that the core fit leaves it "*spent* — no freedom remains" ('Numbers at the scattering benchmark'). Why σ₀ can be as large as the fit requires is item 5 of #11 §14 ([Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement)).

The notebook's v0.1 values above the gate, "σ_T/m (300 km/s) ≈ 6×10⁻² cm²/g, σ_T/m (1500 km/s) ≈ 30 e^{−156} ≈ 0" (#1 §5.1), were computed from the Gaussian gate. They hold only if the tail is Gaussian, and they are superseded ([the v0.1 predictions from the benchmark](/wiki/dark-matter/conjugate-matter/benchmark#superseded-the-v01-predictions-from-the-benchmark)). No `verify/` script checks them; the flags' audit recomputed both from the notebook's formula 30·exp(−(v/v\*)²), which confirms the arithmetic, not the model (`review/wiki-build-checks/audit/flag17_recompute.out`, section 5; [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

### Where σ_T is not the observable

The law is a two-body cross-section, and it applies while χ is a gas of classical particles, on [the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem#the-particle-island). For χ light enough to act as a classical wave, Debt 3a found that "Rows 1–2 must be re-derived in wave language (two-body Born scattering is no longer the right observable)" ('Consequences for the predictions table'). On [the wave island](/wiki/dark-matter/momentum-clumping/wave-island) the role of σ_T passes to [the gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate), which Debt 3b calls "the analog of SIDM heat transport (kinetic relaxation redistributes energy through the halo)" (`notes/debt3b-wave-island.md`, 'What pins g? Two scenarios'). The re-derivation is answered only for the knee's tail ([Open: rows 1 and 2 in wave language](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#open-rows-1-and-2-in-wave-language)).

### The soliton candidate's σ_T/M

The withdrawn soliton manuscript #14 estimated the self-scattering of its superheavy monopoles as a Coulomb-type σ_T, the long-range case above (#14 §4):

> Self-interaction. Monopole-monopole scattering through the hidden photon is Rutherford-like at alpha_m ~ 34 but suppressed by the mass: sigma_T/M ~ 8 pi alpha_m^2 ln(Lambda)/((M/2)^2 M v^4) ~ 1e-26 cm^2/g at v ~ 1e-3 c and M = 3e13 GeV, for ln(Lambda) = 10-30. That is some twenty-six orders below astrophysical sensitivity. The candidate is effectively collisionless cold dark matter, so observed dwarf-galaxy cores must be attributed to baryonic feedback.

M/2 is the reduced mass of two monopoles, so σ_T/M falls as the cube of the mass. The round-3 referee recomputed the value as "0.95e-26 - 2.9e-26 (manuscript formula)", found that the "standard 4 pi a^2 lnL/(mu^2 v^4) gives half", counted "~25.7 orders below 1 cm^2/g", and confirmed it up to a "factor-2 convention" (`review/round3/referee/audit-notes.md`, Step 2). The round-3 adjudication keeps "The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′ overclosure" among what survives the withdrawn paper ('What survives v3'). The candidate itself was retired on other grounds ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary); [benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic#the-cross-section)).

## References

The program's documents cite no source for the transfer cross-section. Added by the wiki from model memory (†):

- S. Chapman, T. G. Cowling, *The Mathematical Theory of Non-uniform Gases* (Cambridge University Press)†: the transport cross-sections of the kinetic theory of gases, with the weighting 1 − cos θ for diffusion and sin²θ for viscosity and heat conduction.
- S. Tulin, H.-B. Yu, K. M. Zurek, "Beyond collisionless dark matter: particle physics dynamics for dark matter halo structure," Phys. Rev. D (2013)†: σ_T for Yukawa forces in the Born, resonant and classical regimes.
- S. Tulin, H.-B. Yu, "Dark matter self-interactions and small scale structure," Phys. Rep. (2018)†: a review, including the viscosity cross-section and the treatment of identical particles.
- M. Kaplinghat, S. Tulin, H.-B. Yu, "Dark matter halos as particle colliders: unified solution to small-scale structure puzzles from dwarfs to clusters," Phys. Rev. Lett. (2016)†: the cross-section per unit mass inferred across halo masses.
- F. Kahlhoefer, K. Schmidt-Hoberg, M. T. Frandsen, S. Sarkar, "Colliding clusters and dark matter self-interactions," Mon. Not. R. Astron. Soc. (2014)†: rare large-angle and frequent small-angle scattering in cluster collisions.

## Used by

- [The gated scattering law σ_T(v)](/wiki/dark-matter/conjugate-matter/scattering-law) — the program's σ_T, with a knee at v\* and isotropy below it.
- [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee) — σ_T across halo masses, against the standard expectations of cold dark matter and Yukawa SIDM.
- [Row 2: isotropic scattering below the gate](/wiki/predictions/scattering-isotropy) — the angular pattern behind σ_T.
- [Row 3: the island discriminant](/wiki/predictions/island-discriminant) — the shape of the fall above the knee.
- [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) — a speed dependence through the relative momentum k, not through the range of q.
- [The scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) — σ₀/m fixed by the cores of dwarf galaxies.
- [Open: the gate shape (OP4)](/wiki/dark-matter/conjugate-matter/gate-shape) — the tail of σ_T(v) above the knee.
- [Open: the dual-stress enhancement (OP5)](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement) — the size of σ₀.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) — its distinctive handles are stated in σ_T.
- [The gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) — its coupling g written through σ₀.
- [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) — the wave-island analog, where σ_T is not the observable.
- [Benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic) — the withdrawn monopoles' σ_T/M ~ 10⁻²⁶ cm²/g.

## Sources

- `notes/broken-born-theory.md` §5.1 — "the momentum-transfer cross-section", the v0.1 law and its heavy mediator, Yukawa SIDM's v⁻⁴ fall with a Coulomb log, the transport remark, the 150–400 km/s band, the dwarf-core value and the v0.1 values above the gate; §9 — the v0.1 row 1; 'Addendum (v0.4)' — the cliff weakened to a knee
- `papers/broken-born-checkpoint-v2.md` §8 — the amplitude, its tag, the gated σ_T(v) and the benchmark mass; §13 rows 1–3 — the rows stated in σ_T; §14 items 4–5 — the open gate shape and the dual-stress enhancement
- `notes/debt3a-stream-stability.md` 'Setup' — g written through σ₀; 'Numbers at the scattering benchmark' — Γt ∼ 1 and the "spent" coupling; 'Consequences for the predictions table' — two-body Born scattering not the observable on the wave island
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' — the dwarf and cluster dispersions; Γ_self as the analog of SIDM heat transport
- `notes/knot-dark-matter-standalone.md` §4 — the soliton candidate's σ_T/M
- `review/round3/referee/audit-notes.md` Step 2 and `review/round3/referee/step2a.out` — the recomputed σ_T/M and the standard Coulomb formula
- `review/round3-adjudication.md` 'What survives v3' — the benchmark-conditional arithmetic survives
- `review/wiki-build-checks/audit/flag17_recompute.out` sections 3 and 5 — the Born σ_T without a gate is flat in speed at the benchmark; the v0.1 values above the gate recomputed (an audit check, not part of `scripts/check.sh`)
- `HANDOFF.md` §6 — the round-1 referee's misreading of σ_T/M as σ_T
