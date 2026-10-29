---
title: "Conjecture: a long-range velocity-gated attraction among χ"
weight: 75
status: conjecture
description: "P.R.'s model of dark-matter particles attracting each other at long range only when they move at similar velocities: no field in the record carries it; at the record's gate width the Lyman-α forest allows ε < 0.057–0.106 while velocity-selected clumping needs ε > 1; it cannot make dwarf cores, so it would be decorative; narrow gates below about 30 km/s are a partly open corner."
provenance: [D, V]
sources:
  - "notes/velocity-gated-gravity.md §1"
  - "notes/velocity-gated-gravity.md §5"
  - "notes/velocity-gated-gravity.md §6"
  - "notes/velocity-gated-gravity.md §7"
  - "notes/velocity-gated-gravity.md §8"
  - "notes/velocity-gated-gravity.md §10"
  - "notes/velocity-gated-gravity.md §11"
  - "verify/velocity_gated_gravity.py 'E. The long-range chi-only gated attraction'"
  - "verify/velocity_gated_gravity.py 'F. Clumping thresholds'"
  - "verify/velocity_gated_gravity.py 'G. The low-v* corner'"
  - "verify/velocity_gated_gravity.py 'H. Cores'"
  - "review/momentum-gravity/README.md"
  - "notes/gate-mechanism.md §3"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "notes/broken-born-theory.md §5.2"
  - "notes/stream-stability.md 'Numbers at the scattering benchmark'"
---

*This is a model of dark matter that the program's record does not contain: dark-matter particles χ attract each other at long range, like gravity, but only when they move at similar velocities. P.R. proposed it on 2026-10-26, asking whether the obituary of the program's founding picture, a halo breaking up into streams of particles that share a velocity, was premature. A note of 2026-10-28 tests the model on its own terms. Nothing in the program supplies a field that could carry such a force. In an expanding universe the force switches off between particles a few megaparsecs apart, on the scales that the Lyman-α forest of distant quasar spectra measures, and the forest allows a force of at most six to eighteen percent of gravity, while making velocity-selected lumps needs more than gravity's full strength. At any strength the force could not make the cores of dwarf galaxies, the job the program introduced its gate for, so its strength would be a free number the program cannot predict. Only gates much narrower than the program's, below about 30 km/s, remain partly unexplored.*

**Status:** Conjecture, outside the record, and decorative where tested — P.R.'s model, which "the record does not contain, which the clumping problem never tested", with no carrier in the record (`notes/velocity-gated-gravity.md` §§1, 5). The note (2026-10-28; computed, each analysis checked by two independent verifiers, a critic and a final critic; not reviewed) tags its results [D], [D][V] and [D; derived twice independently] with observational inputs [S], as given below; the narrow-gate N-body runs and the corrected proxies each rest on one agent, one statistic of the runs is not adjudicated, and two findings of the runs were noticed only while the record was ported into `verify/` (§8). Every number except the N-body runs is recomputed in sections E–H of `verify/velocity_gated_gravity.py` ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)); the N-body record is in `review/momentum-gravity/scripts/corner/`. It does not reopen [the founding image's obituary](/wiki/dark-matter/momentum-clumping/founding-image#what-the-obituary-covers), which covers the program's own contact-range interaction; listed in [conjectures](/wiki/status/conjectures).

## The model

[D] (§5).

```text
U = −G̃ m_χ² W(|v − v′|/v*) / |x − x′|,     ε ≡ G̃/G
```

acting among χ only and added to gravity, with W the gate, v\* its width and ε the strength relative to gravity. The program's own gate acts only on contact, through scattering, and leaves χ's gravity ungated ([the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)); this model gates a long-range attraction instead.

- **What it amplifies.** In mean field it is a Jeans-type amplifier of spatial clumping among co-moving particles ([the Jeans instability](/wiki/dark-matter/momentum-clumping/vlasov-stability#the-static-threshold-and-the-jeans-instability)). Gravity and the gated term both scale as 1/k² with the wavenumber k, so the gate rescales the Jeans wavenumber by the top eigenvalue Λ of an operator on velocity space.
- **What it does not make.** Streams spread through space, the founding image's structures, are exactly neutral in mean-field dynamics in a homogeneous medium (k = 0). In a cored halo the harmonic potential interconverts velocity and position structure, and above threshold the gate-only velocity-dipole modes (m = ±1) grow. The modes the gate adds are spatial lumps carried by a velocity-selected population of width about √(σv\*), with σ the halo's [velocity dispersion](/wiki/dark-matter/halo-astrophysics/velocity-dispersion).

## No carrier in the record

[D][V] (§5).

- X, the program's only long-range candidate beyond gravity, is massive: λ_X < 37.7 μm at u = 1, unscreened ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound); [X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies)). #11 §8's m_φ, the mass of the carrier of the momentum transfer in the program's amplitude, is a free scale with no field behind it.
- Gating χ's own gravity is outside the record by postulate: "χ propagates on g (equivalence principle; Bullet-Cluster-safe)" (#11 §8). It is observationally untested. Lensing and dynamical masses both see χ through ungated gravity, and χ re-virialized in a weaker force stays bound (one agent). An earlier ruling in the investigation that observation excludes it is withdrawn (§11).
- Whether any local field could carry such a force is taken up on [what could carry a relative-velocity gate](/wiki/dark-matter/conjugate-matter/gate-carriers): no field of finite spin can, and the one exotic framework with the right shape has a threshold that depends on distance (§9). Whether the program's own contact gate can come from X at all is the subject of flag 55 ([the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The gate-mechanism note adds that, in a model with the gate inserted by hand around a separate potential, a fiber-overlap gate is not tied to contact range; what makes the record's gate contact-range is X's mass (one derivation; `notes/gate-mechanism.md` §3).

## Three readings of a velocity-dependent potential

[D] (§5). A potential that depends on velocity has more than one classical meaning:

- **Hamiltonian:** the gate acts on canonical momentum. This is the record's reading: the lab notebook writes the energy ε(p; f), a different ε from the strength, and the anomalous velocity ẋ ⊃ ∇ₚε (#1 §5.2; [the founding image](/wiki/dark-matter/momentum-clumping/founding-image#the-picture)).
- **Lagrangian:** the gate acts on velocity.
- **Force at fixed velocity:** −∇ₓU with ẋ = v. This is neither Hamiltonian nor Lagrangian; the note reports it only as one edge of a bracket.

Two caveats travel with the record's reading:

- [O]: whether the Hamiltonian reading is the right classical limit for a long-range gate. In it the kinematic and canonical velocity dispersions decouple, by up to 11.5× in the N-body runs below, and its linear theory loses meaning above ε ≈ 2.2 (2.24–2.29 at z = 50, 10 and 3), where the effective inverse inertia changes sign.
- In the Hamiltonian reading, gating on peculiar velocities alone is pathological (one agent; not rechecked). The gate is therefore taken on the full relative velocity, Hubble flow included.

## Hubble-flow gating

[D][V] (§6). Two χ a proper distance s apart in the Hubble flow move apart at Hs, so the gate closes at s_c = v\*/H(z): 1.78 Mpc comoving today, at most 2.03 Mpc near z = 0.63. In velocity units the gate scale is v\* at every epoch, an exact identity. At the pivot of the Lyman-α measurement of the Dark Energy Spectroscopic Instrument ([DESI](/wiki/cosmology/dark-energy/desi)), at z = 3, k_p·s_c = 1.08. The model changes the background expansion by nothing at order ε.

## What observations allow

### The Lyman-α forest

[D; derived twice independently; DESI and Planck inputs S] (§6). The forest is the series of absorption lines that intergalactic hydrogen imprints on the spectra of distant quasars; it measures the matter power spectrum on small scales [T] ([bounds from the Lyman-α forest](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds#bounds-from-the-lyman-α-forest-t)).

- **The data.** The compressed constraint of DESI's first data release at the pivot: Δ² = 0.379 ± 0.032, n = −2.309 ± 0.019.
- **The bound in the record's reading:** ε < 0.057 (matter ratio) to 0.106 (gas ratio) at v\* = 120 km/s.
- **In the force-at-fixed-velocity reading:** ε < 0.0585 to 0.176. Its density kernel is R₁(y) = ∫₀¹R(yμ)dμ, which at the pivot is 0.311, not the 0.803 of R.
- **The sign.** In the record's reading the force lowers the power at the pivot: T² = 0.948 at ε = 0.1 and v\* = 120 km/s.
- **An older data set.** The compressed data of eBOSS, the extended Baryon Oscillation Spectroscopic Survey, prefer ε ≈ 0.05 formally: χ² falls from 26.3 to 1.9 at ε = 0.0535. "This is not evidence. Those data sit 4.9σ from Planck, any suppression near the pivot relieves that tension, the compression assumes a ΛCDM spectrum shape, and DESI agrees with Planck."
- **Estimates, not likelihoods.** In the record's reading the response is a dip at the pivot and a rise at smaller scales, a shape a compressed (Δ², n) fit cannot represent. A full one-dimensional power-spectrum likelihood is open.
- **A limit that does not transfer.** The full-shape limit of the Baryon Oscillation Spectroscopic Survey on long-range dark-matter forces, β < 0.0048, is set by the background modification of the scalar model, which the gated model lacks (one agent's reading of the sources).

### The Sagittarius stream

[D; S] (§6). The Sagittarius dwarf galaxy is being torn apart by the Milky Way, and its leading and trailing tails would be asymmetric if dark matter felt a force that stars do not [T] ([cold stellar streams](/wiki/dark-matter/halo-astrophysics/halo-substructure#cold-stellar-streams-t)). The asymmetry limit (Kesden and Kamionkowski, a 10% level stated without a confidence level and disputed by Keselman, Nusser and Peebles) gives ε ≲ O(1): 0.2–2.5 at v\* = 120 km/s, depending on how the gate is averaged over the orbit and on the reading. It never beats the Lyman-α forest in the record's reading.

## What clumping needs

[D][V] (§7).

- **The threshold.** Velocity-selected modes need ε > 1/Λ_g(σ/v\*), with Λ_g the top eigenvalue of the gate-only operator. This exceeds 1 at every σ/v\*, tending to 1 as σ/v\* → 0 (1.000003 at σ/v\* = 10⁻³), and is at least 4.24 wherever σ ≥ v\*. It equals 4/3 at σ/v\* = 0.333.
- **Against the bounds.** At v\* = 120 km/s the allowed strength is at least 9.4× too small in the record's reading and 5.7× in the force-at-fixed-velocity reading.
- **In real halos.** The local model's own thresholds at v\* = 120 km/s are at least 28.1 in the Milky Way (the longest mode that fits; 161 at the solar circle's own scale; none at all once the halo re-virializes) and at least 693 in clusters (the crossover 1/Λ_g at σ/v\* = 8.33). These exceed the Lyman-α bound (gas, record's reading) by 264 and 6.5×10³, and the loosest Sagittarius bound by 11.4.
- **Validity.** Both thresholds lie beyond the local model's validity, which ends near ε ≈ 1.5 in the Milky Way and 133 in clusters. The note: "Treat them as indicative."
- **At gravitational strength.** A gravitational-strength gate (ε = 1, or 4/3) adds no velocity-selected instability anywhere.

The investigation's run-2 pre-registration expected G̃/G ≳ (σ/v\*)³, about 2 in the Milky Way and 580 in clusters; the executed values are at least 28 and at least 693 (§11). It was right that the long-range variant meets small-scale-structure limits, the Lyman-α forest binding at v\* = 120 km/s; its weakest link, the O(1) factors, "were indeed the weak point, off by more than an order of magnitude in the Milky Way", and Hubble-flow gating does not let the variant escape the cosmological bounds, since "the gate closes at a Hubble separation of exactly v\*, the forest's scale" (§11).

## Cores: why the force would be decorative

[D, three independent recomputations] (§7).

- A gravitational-strength 1/r force scatters χ at σ_T/m = 2.4×10⁻⁶² cm²/g at 30 km/s (Born approximation, ln Λ = 68.7 at b = 1 kpc), where σ_T/m is the [transfer cross-section](/wiki/dark-matter/halo-astrophysics/transfer-cross-section) per mass.
- Making [dwarf-galaxy cores](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) by scattering would need G̃/G ≈ 3.6×10³¹ ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark) is 30 cm²/g).
- So the force cannot make cores. Its strength would be a free parameter and any clumping optional: "decorative" in [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem)'s own word (§7).

## Narrow gates: the corner

Where the gate is narrower than about 30 km/s, comparable to the velocity spread of a dwarf galaxy, the local model fails and no bound existed. Simulations found no velocity-selected structure up to ten times gravity's strength, and corrected estimates from small-scale cosmology exclude twice gravity's strength for gates from 10 km/s up, and three times it from 5 to 30 km/s in one of the two readings (§8, plain-language passage). Two of the findings below were noticed only while the record was ported into `verify/`, not by an agent of the investigation, and are marked so (§1, §8).

### N-body runs

[D, executed; one agent; isolated cored halo] (§8).

- **The runs.** Direct-summation runs of a Plummer χ halo, N = 2000 (five more runs at N = 1000 test the resolution), three realizations per case and an ε = 0 control, with the gated term switched on slowly; the record's reading, with one case (three realizations) in the force-at-fixed-velocity reading for comparison. 29 runs.
- **Energy.** In the record's reading, energy is conserved after the switch-on to 1.8×10⁻⁵ in 23 of the 26 runs; three runs at ε = 10 exceed it, the largest reaching 5.4×10⁻⁵. The record says 1.8×10⁻⁵ for all. This was noticed while porting the record into `verify/`, not by an agent. The force-at-fixed-velocity reading is not Hamiltonian and conserves no energy.
- **The result.** At ε = 1, 3 and 10, with the gate as wide as the dispersion or 2.5× wider: no velocity-selected clumps, streams or coherent flows beyond the control over 43 central free-fall times, 0.1–0.6 Gyr in a dwarf. At ε = 10, ξ_u05 = −0.0069 ± 0.0063 over the three realizations, against +0.2339 for an injected population of clumps holding 2% of the mass.
- **Sensitivity.** The runs detect clumps holding 2% of the mass, and streams from 5%.
- **What the record's reading does instead.** It reorganizes the halo: canonical momenta narrow, so the gate opens further, the kinematic dispersion becomes up to 11.5 times the canonical one, and the halo's half-mass radius changes by a factor 0.685–1.647.
- **Not adjudicated**, and noticed while porting the record into `verify/`, not by an agent. In all seven gated cases at N = 2000 the close-pair statistic ξ_u1 exceeds the control, by +0.0073 to +0.0231 (1.7–3.5σ on three seeds). In the injection test, clumps holding 2% of the mass raise ξ_u1 from +0.0146 to +0.0409 in one snapshot, a change comparable to that offset, so ξ_u1 alone cannot exclude them. The null rests on ξ_u05, which the same injection raises from +0.0852 to +0.2339, and on the stream statistics. The corner agent and the final critic read the runs as a null; "nothing in the record separates the uniform ξ_u1 offset from the halo's reorganization."
- **Not rerun by the gate.** The runs' snapshots, about 90 megabytes, are not kept. Their logs, diagnostics and injection test are in `review/momentum-gravity/scripts/corner/`, and the script checks its quoted numbers against those logs ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script)).

### Observational proxies

[D; estimates, not likelihoods; the final critic's rerun, one agent] (§8). The corner agent's linear proxies used the two flawed systems of run 2 (below); the final critic reran them with corrected formulas, "the edges in v\* moved, and the map stands".

- ε ≈ 2 is excluded from v\* = 10 km/s up in both readings, by the reionization optical depth and dwarf central densities. In the record's reading ε = 2 lies close to where its linear theory loses meaning (ε ≈ 2.2), so the force-at-fixed-velocity reading carries this exclusion more safely; the note marks this an inference. The optical depth measures how much of the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background) was scattered by electrons freed when the first stars ionized the gas; earlier structure raises it [T].
- ε ≈ 3 is excluded at v\* = 5–30 km/s in the force-at-fixed-velocity reading: the dwarf density proxy rises ×9.54 and the optical depth to 0.099 at v\* = 5 km/s, against Planck's 0.054 ± 0.007. The record's reading gives no number there, because its linear theory has lost meaning.
- ε ≈ 1 is in tension above v\* ≈ 20–30 km/s and disfavoured from 3–5 km/s up, from the optical depth, dwarf densities, small-scale Lyman-α data, and the heating of Segue 1 if early χ clumps survive ([Segue 1](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies#segue-1-the-test-case)).

### Not computed

From §8:

- gates below 3 km/s, where clumping would need ε of about 4–10, beyond the model's validity;
- gates narrower than the dispersion in the record's reading;
- instabilities slower than 43 free-fall times, or below the N = 2000 relaxation floor;
- the satellite-count proxy, which was not rerun with the corrected formulas.

"Whatever the corner holds, it needs a second gate scale 4–40× below the record's 120 km/s, and the cores of §7 still need 3.6×10³¹" (§8).

## What is open

From the note's §10 [O]:

- a full Lyman-α likelihood, with hydrodynamics, for the long-range variant;
- a nonlinear cosmological simulation of the narrow-gate corner, including whether early χ clumps survive in ultra-faint dwarfs;
- slow collisionless instabilities beyond the N-body's window, and gates narrower than the dispersion;
- whether the uniform ξ_u1 offset in the gated N-body runs is the halo's reorganization or a weak velocity-selected signal;
- whether the Hamiltonian reading is the right classical limit for a long-range gate;
- the observational status of gated χ–χ gravity: χ against stars in streams or merging clusters;
- how the Sagittarius asymmetry weights the orbit, and the status of the 10% level;
- whether "premature" rests on a particular observation (§4).

On the last, the note records that cold dark matter already contains about 10¹⁴ fine-grained streams near the Sun (Vogelsberger and White), while the founding image predicted about ten broad ones, so only streams of that kind would test it [T][S] (§4). All of these are on [open problems and the queue](/wiki/status/open-problems).

## Corrections along the way

The note lists what was refuted or corrected before its answer went to Paul (§11). Those that bear on this model:

- **Refuted:** that every ε > 0 raises the Lyman-α power and deepens the eBOSS tension. It holds only for the force at fixed velocity; in the record's reading the power falls.
- **Refuted:** that the full-shape limit β < 0.0048 maps onto ε. It does not transfer (one agent's reading of the sources, §6).
- **Refuted:** that at strong coupling the clumping model has no purely growing mode past a certain threshold. The gate-only sector develops its own; the rate dips rather than saturating.
- **Corrected:** the run-2 Lyman-α bound used the wrong force-law kernel, R in place of R₁, a factor 2.58 at the pivot; both verifiers found it independently. The run-2 critic's record-reading bound, ε < 0.34, counted the Hubble term on the anomalous velocity twice; the bound is 0.057–0.106.
- **Withdrawn:** "gated χ–χ gravity is excluded by observation".
- **Corrected:** the Sagittarius bound is O(1), not a sharp 1.5; the N-body's energy conservation was recorded as 1.8×10⁻⁵, and three runs at ε = 10 exceed it, one reaching 5.4×10⁻⁵.

The run-3 pre-registration predicted a Lyman-α bound of 0.1–0.5, anchored on the run-2 critic's 0.34, and got 0.057–0.106; predicted a Sagittarius bound of 1–3 and got 0.2–2.5; and predicted no robust exclusion in the corner, where ε ≈ 2 is excluded from 10 km/s up, and ε ≈ 3 at 5–30 km/s in one reading. It was right that the N-body would find no clumping, "and more strongly than predicted, none up to ε = 10" (§11; [pre-registration](/wiki/method/review/pre-registration)).

## Sources

- `notes/velocity-gated-gravity.md` (2026-10-28, not reviewed) §1 — the question, the readings and ε; §5 — the model, no carrier, the three readings; §6 — Hubble-flow gating, the Lyman-α forest, the Sagittarius stream; §7 — the thresholds and the cores; §8 — the corner: N-body, proxies, what was not computed; §10 — what is open; §11 — refuted, corrected and withdrawn, and the pre-registrations scored; §4 — fine-grained streams and the scope of the obituary
- `verify/velocity_gated_gravity.py` — section E, the long-range χ-only attraction; F, the clumping thresholds; G, the low-v\* corner, including the checks of the N-body record; H, the cores ([the velocity-gated-gravity script](/wiki/method/verification/velocity-gated-gravity-script))
- `review/momentum-gravity/README.md` — the runs, the corner agent and the final critic; `review/momentum-gravity/scripts/corner/` holds the N-body logs, diagnostics and injection test
- `notes/gate-mechanism.md` §3 — the range of a fiber gate (one derivation)
- `papers/broken-born-checkpoint-v2.md` §8 — "χ propagates on g (equivalence principle; Bullet-Cluster-safe)" and the free scale m_φ; §9 — the net theorem's "decorative"
- `notes/broken-born-theory.md` §5.2 — the energy ε(p; f) and the anomalous velocity, the record's reading
- `notes/stream-stability.md` 'Numbers at the scattering benchmark' — the contact-range obituary this model is set against
