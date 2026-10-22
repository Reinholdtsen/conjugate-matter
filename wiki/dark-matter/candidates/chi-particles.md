---
title: "The χ-particle candidate"
weight: 20
status: alive
description: "Mirror-polarized particles with assumed stability that fall, orbit and lens like ordinary dark matter; their handles are the knee at v* with a sharp tail, isotropic scattering, and a permanent direct-detection null."
provenance: [D, O]
sources:
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md App. A item 4"
  - "notes/broken-born-theory.md §1"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §5.1"
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/broken-born-program-v1.md §9"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/wiki-build-flags.md item 17"
  - "review/wiki-build-flags.md item 19"
---

*The χ-particle candidate is the proposal that [dark matter](/wiki/dark-matter) consists of particles of [conjugate matter χ](/wiki/dark-matter/conjugate-matter): matter in the momentum-polarized representation, the mirror image of ordinary, position-polarized matter. χ gravitates exactly like ordinary matter, so it falls, orbits and bends light like standard cold dark matter, but no gauge force of ordinary matter acts on it. Its own self-interaction works only between particles with nearly equal velocities — the [velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate) — which predicts strong self-scattering in slow [dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies), none in fast galaxy clusters, and a knee in between. It is one of the program's two remaining [dark-matter candidates](/wiki/dark-matter/candidates); its stability is assumed rather than derived, and its abundance is unexplained.*

**Status:** Alive — one of two candidates; #11 §12 tags the pair "[D — framework; each candidate O]". Its gravitational behaviour is [D] (`notes/broken-born-theory.md` §4); its gate is "[D — mechanism; shape [O]]" (#11 §8). Nothing on this page is machine-checked.

## The candidate

[Checkpoint #11](/wiki/history/documents/checkpoint) §12 answers the question it poses in plain terms, "what is dark matter, fundamentally?", with a table of two candidates, each described by its origin, what makes it stable, and the observable that would single it out. The χ row reads:

| Candidate | Origin | Stability | Distinctive handle |
|---|---|---|---|
| **χ particles** (§8) | p-polarized matter field | assumed | knee at v\*, sharp tail; isotropic scattering; permanent direct-detection null |

The tag on the table, "[D — framework; each candidate O]", separates two things. The framework that produces χ, a second matter representation coupled to gravity and to nothing else of ours, is derived from [the postulates](/wiki/program/postulates). Whether dark matter is in fact made of χ is open. The other row is [the X-condensate](/wiki/dark-matter/candidates/x-condensate), and both share the open question of [the 5.4 : 1 abundance ratio](/wiki/dark-matter/candidates/polarization-genesis).

## The field χ

χ is introduced by postulate [P4](/wiki/program/postulates/p4-polarized-matter): "Matter comes in x-polarized (Standard Model) and p-polarized (χ) representations; both couple universally to H; gauge forces do not cross polarizations" [P]. Here H is [the generalized metric](/wiki/phase-space/born-geometry/born-structures) on phase space, and a polarization is the choice of which half of phase-space coordinates counts as position ([Lagrangian polarizations](/wiki/phase-space/reciprocity/lagrangian-polarizations)). Ordinary matter is local in position; χ is matter organized the other way round, local in momentum, hence "conjugate matter" ([conjugate matter and the velocity gate](/wiki/dark-matter/conjugate-matter)).

Since v2.1 of #11, P4 is "taken strictly": "no kinetic mixing between the sectors beyond what gravity induces, which vanishes if hidden charge conjugation is exact and otherwise first appears at six loops, ε ≲ 10⁻¹³ [27S]" (#11 §4; [round-3 Decision 1](/wiki/method/review/round-3/decisions)). No Standard Model (SM) force reaches χ.

[The lab notebook](/wiki/history/documents/lab-notebook) leaves the spin open: "χ (take a complex scalar or Dirac fermion; nothing below depends on spin) propagates on g — it gravitates exactly like ordinary matter — but its self-interaction is routed through the g̃ block" (#1 §3). On the program's vacuum, H splits into a spacetime metric g and a momentum-space metric g̃ (#1 §3). χ moves on the first and interacts with itself through the second.

## How χ gravitates [D]

P4 couples both kinds of matter universally to H, and on the vacuum that means to the same spacetime metric g. In the notebook's form of the postulate, "the equivalence principle holds across polarizations" (#1 §1, P4). χ therefore follows the same free-fall trajectories as ordinary matter, and its energy curves spacetime in the same way. The notebook draws the consequence [D]: "χ couples to g universally: it falls, orbits, and lenses like ordinary dark matter. Bullet Cluster lensing-centroid behavior is automatic (and see Prediction 1 for the scattering side)" (#1 §4).

The Bullet Cluster is a collision of two galaxy clusters in which the mass seen by gravitational lensing sits with the galaxies, offset from the hot gas that collided and slowed [T]. The dark matter passed through with little scattering. For χ the lensing half is the gravitational coupling above; the scattering half is the gate, which is closed at cluster speeds (next section). #11 §8 keeps both: "χ propagates on g (equivalence principle; Bullet-Cluster-safe)". The established background is on [self-interacting dark matter](/wiki/dark-matter/halo-astrophysics/self-interacting-dark-matter).

## How χ scatters off itself: the gate and the knee

The self-interaction is where χ differs from cold dark matter. #11 §8 gives its nonrelativistic amplitude [D — mechanism; shape [O]]:

```text
M(k, q) = 4πα̃ m_χ / (q² + m_φ²) · F(k²/μ²)
```

Here q is the momentum transfer, k "the incoming *relative* momentum", α̃ the coupling, m_χ the χ mass and m_φ the mass of the exchanged field. The first factor is an ordinary exchange amplitude in the transfer q, contact-like in position when the mediator is heavy (m_φ ≳ m_χ, #1 §5.1). The second, the gate F, cuts the interaction off once the two particles move too fast relative to each other. Its argument, the relative momentum k, is "the variable no x-local mediator produces" (#11 §8). The scale μ is "the χ quantum's intrinsic momentum-fiber width" ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)).

The mechanism is exchange of [the momentum graviton X](/wiki/gravity/momentum-graviton) "between dual-stress bilinears" (#11 §8). [Calc note #6](/wiki/history/documents/debt-1-notes) explains why it depends on k: momentum-polarized quanta are extended along the momentum fiber with width μ, "and they exchange X only over their fiber overlap" (#6 §4; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)). Two particles with very different velocities have wavepackets that do not overlap in momentum, much as two signals in separate frequency bands share no spectral overlap.

The consequence for the momentum-transfer cross-section is "σ_T(v) = σ₀F(v²/v\*²): robust knee at v\*" (#11 §8; [the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)). Below the knee velocity v\*, χ scatters with cross-section σ₀; above it, scattering is suppressed. The shape of the tail above the knee, "(Gaussian vs rational)", "diagnoses the vertex completion", and the scattering is "isotropic below the gate versus Yukawa forward-peaking". The benchmark, set by fitting the cores of dwarf galaxies (#1 §5.1), is "m_χ ≈ 70 MeV·α̃^{2/3}(σ₀/m ÷ 30 cm²g⁻¹)^{−1/3}" ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)). Why σ₀ can be nuclear-scale while χ's couplings to ordinary matter stay gravitational is open: "Main open quantitative item: the dual-stress enhancement (nuclear-scale σ₀ with gravitational SM couplings) [O]" (#11 §8; [the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement)).

## Handles and tests

Each entry in the table's last column is a row of #11 §13, [the predictions table](/wiki/predictions):

| Row | Requirement | Killed by |
|---|---|---|
| [1](/wiki/predictions/self-interaction-knee), σ_T(v) across halo masses | "Knee at v\* ~ 10² km/s; zero cluster signal (particle χ)" | "Robust self-interaction at v ≫ v\*; knee excluded in the 150–400 km/s band" |
| [2](/wiki/predictions/scattering-isotropy), scattering anisotropy | "Isotropic below the gate" | "Morphology demanding forward peaking" |
| [3](/wiki/predictions/island-discriminant), island discriminant | "Knee tail: sharp ⇒ particle; (v\*/σ)⁴ ⇒ wave" | "Diagnostic — selects the branch (particle vs wave χ)" |
| [7](/wiki/predictions/direct-detection-null), direct detection and colliders | "**Permanent null** (both dark-sector candidates SM-decoupled; P4 strict)" | "Any confirmed non-gravitational DM–SM coupling" |

DM is dark matter. Rows 1 and 2 are the gate seen in halo dynamics: strong scattering in dwarf galaxies, where velocities are low, and none in clusters, where they are high. Row 7 follows from strict P4: with no gauge force crossing polarizations, a detector built of ordinary matter can register χ only through gravity. #11 §15 counts rows 1 and 7 among the program's near-term falsification exposure.

## Particle χ and wave χ

The table's "sharp tail" fixes which kind of χ the candidate is. Debt 3 found that χ behaves in one of two regimes, set by its mass ([momentum clumping](/wiki/dark-matter/momentum-clumping)). Heavy χ is a gas of classical particles, the particle island; very light χ has so many particles per quantum state that it acts as a classical wave, the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), "3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV" in the notebook's addendum v0.2. The [classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem) separates them: collective momentum-space behaviour "forces m ≲ 0.1 meV, where N_occ ~ 10²⁰ — collective momentum-space behavior and classical particles are mutually exclusive" (#11 §9; flag 19 in `review/wiki-build-flags.md` queries the gate regime in which that bound was evaluated, and finds the conclusion unchanged).

The two regimes give different knees. For particle χ the tail is the gate's own cutoff; for wave χ the suppression is "(v\*/σ)⁴" (#11 §9; [row 3](/wiki/predictions/island-discriminant)). The candidate row of #11 §12 lists the sharp tail, so it describes particle χ, and row 1's "zero cluster signal" is also stated for "particle χ". The wave branch survives in the record with free couplings; its "tunable wave-island collective sector" is "quarantined" as a degeneration risk (#11 §15; [Scenario B: tunable streams](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b)), and the branch's relic abundance comes from misalignment ([relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)). #11 §12's other row, the X-condensate, carries "knee shape wave-like". No document relates wave χ to the X-condensate.

## What the candidate no longer claims

χ clusters in position, as cold dark matter does, not in velocity. The program's founding image was dark matter clumping in momentum space; Debt 3 tested it and found it "nowhere mandatory — forbidden (particles), fatal (committed wave), decorative (free wave)" (#11 §9; [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)). Founding supposition 4, "Dark matter is conjugate matter", is "**alive, modified**: x-clumping, gated self-force; now one of two remaining candidates (§12)" (#11 App. A item 4; [founding suppositions](/wiki/program/founding-suppositions)).

## What is open

- **Stability.** The table's entry is "assumed". No document derives why χ does not decay.
- **Abundance.** "The 5.4 : 1 abundance question (polarization-genesis) applies to both" (#11 §12). The notebook argues that particle χ cannot get its abundance from thermal freeze-out (#1 §5.3; [Open: polarization-genesis and the 5.4 : 1 ratio](/wiki/dark-matter/candidates/polarization-genesis); [relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)).
- **The gate's shape.** "Gate shape (X propagator on momentum fibers; Gaussian vs rational — now observable) [O]" (#11 §14 item 4; [Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)).
- **The size of σ₀.** "Dual-stress enhancement parametrics [O]" (#11 §14 item 5).
- **Telling χ from the X-condensate.** [Row 11](/wiki/predictions/dark-sector-microstructure): "Particles vs condensate, separable via rows 1–3 + coherence signatures", open as #11 §14 item 9.

## History

- **The lab notebook, v0.1.** χ enters with P4 and a Gaussian gate e^{−k²/μ²}, postulated [P] (#1 §3). The scattering law falls "off a cliff at v\*", and cluster self-interaction is "identically zero at any future sensitivity" (#1 §5.1). "Rows 1, 3, and 7 are the flagship discriminants" (#1 §9), with row 3 then velocity-space granularity.
- **Debt 3 (addendum v0.2).** Collective clumping fails, old rows 3 and 4 are withdrawn, and the island discriminant replaces them.
- **[Debt 1](/wiki/history/debts) (addenda v0.3 and v0.4).** The gate's mechanism becomes X-exchange, μ becomes the fiber width (flag 17 in `review/wiki-build-flags.md` records a suspected factor of √2 in μ between #6's overlap form and v0.1's e^{−k²/μ²}), and "the exponential cliff weakens to a sharp knee at v\* with tail shape (Gaussian vs rational) diagnosing the vertex completion" (#1 v0.4; #6 §4).
- **#9.** Row 7's null covers "χ (or X-condensate)" (#9 §9).
- **#11 v2.0 and v2.1.** χ particles become one of three candidates, then one of two after the soliton candidate was retired on 2026-10-19 (round-3 Decision 2: "the trilemma becomes two program-native candidates (gated χ particles; the X-condensate)"; [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). P4 is taken strictly from v2.1.

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — the candidate profile and its tag; §8 — the amplitude, the gate, the knee, the benchmark and the open enhancement; §4 — P4, strict since v2.1; §9 — the particle and wave islands, the net theorem; §13 — rows 1, 2, 3, 7 and 11; §14 items 4, 5, 7, 9; §15 — quarantine and falsification exposure; App. A item 4 — the fate of founding supposition 4
- `notes/broken-born-theory.md` §1 — P4 in the notebook's form; §3 — the χ field and the original gate; §4 — the equivalence principle and lensing [D]; §5.1 — the cliff; §5.3 — why particle χ cannot freeze out [O]; §9 — the flagship rows; 'Addendum (v0.2)' — the wave island; 'Addendum (v0.4)' — cliff to knee
- `notes/debt1a-ii-X-classification.md` §4 — exchange over the fiber overlap, and the downgrade from cliff to knee
- `notes/broken-born-program-v1.md` §9 — row 7 in #9
- `review/round3-adjudication.md` 'Decisions' 1 — strict sector separation; 'Decisions' 2 — three candidates become two
- `review/wiki-build-flags.md` item 17 — the suspected √2 in μ between the two gate conventions; item 19 — the regime of the classicality bound
