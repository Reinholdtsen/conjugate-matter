# Momentum gravity and a relative-velocity gate: the scope of the clumping obituary

*Working note, 2026-10-28. Status: computed. Four analyses were each checked by two independent verifiers, a
critic ruled on the tensions between them, and a final critic reran the disputed calculations. Results resting on
one agent are marked where they appear. The note has not been through a blind review round. Every number is
recomputed in `verify/velocity_gated_gravity.py` (§9's medium in `verify/gate_mechanism.py`), except the N-body
runs of §8, whose record is kept. The analyses,
verdicts, scripts and pre-registrations are in `review/momentum-gravity/`. The companion note
`notes/gate-mechanism.md` takes up a question this one raised: whether X exchange produces the program's gate at
all. Conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic).*

## 1. The question, the readings, the method

*In plain terms: the program buried its founding picture of dark matter, a halo breaking up into streams of
particles that share a velocity. Paul asked whether that burial was premature, and whether the program's
momentum gravity would show up as a correction to ordinary gravity that depends on how fast two bodies move
relative to each other. The question has two readings, one about the program as written and one about a new
model, and this note answers both.*

Paul's question (2026-10-26): "I think the obituary is premature. Would momentum gravity look like a perturbation
to regular gravity that depends on the relative velocity of two massive bodies?" The obituary is #11 §9, resting on
the clumping notes (#2–#4); the wiki records it at `dark-matter/momentum-clumping/founding-image`.

**Readings [assumption].**
- "Momentum gravity" as the program defines it: the massive momentum graviton X of #11 §7, between ordinary
  bodies (§2). Two further readings are checked: #13's dual kinematics, and the Siegel reading of flag 39.
- "A perturbation that depends on relative velocity", acting between all bodies: a universal gated term, tested
  against the Solar System and binary pulsars (§3).
- The same, acting only between dark-matter particles χ and at long range: a model the record does not contain,
  which the clumping problem never tested (§§5–9). The strength is ε ≡ G̃/G.

**Method** (run numbers as in the record, `review/momentum-gravity/README.md`; run 1 was lost to a memory
exhaustion before any agent finished).
- Run 2: four analyses (the program's momentum gravity, velocity clumping, tests with ordinary matter, tests in
  the dark sector); two verifiers per analysis, each working from the extracted claims only; a critic. Three
  verifiers were lost to a network error.
- Run 3: the three lost verifications; checks of the run-2 critic's own claims; an agent on the narrow-gate corner
  (§8); a final critic that reran the disputed calculations with its own code.
- Run 4: checks of the answer's numbers and scope before it went to Paul, and a blind second derivation of the
  gate question of `notes/gate-mechanism.md`.
- Two findings of §8 were noticed only while porting the record into `verify/`; they are marked there.
- Tally: 178 claim checks, 107 confirmed, 65 corrected, 3 refuted (§11), 3 unverifiable.
- Pre-registrations were sealed before each run and are scored in §11. Run 2's was not blind (§11).
- Gate conventions: the record's cross-section gate is e^{−v²/v*²} with v* ≈ 120 km/s; its amplitude gate is
  e^{−v²/v_a²} with v_a = √2 v* = 169.7 km/s. W(v/v*) below is the gate on the potential, in the convention each
  result names.

## 2. Between ordinary bodies, X is a short-range Yukawa term, not a velocity gate

*In plain terms: between two ordinary bodies the program's momentum graviton adds a second, short-range piece to
Newton's attraction, with a range below a few hundredths of a millimetre. Like every force carried by a field, it
depends on the bodies' relative velocity only through the corrections of relativity, which at galactic speeds are
parts in ten million and of the same size as ordinary gravity's own.*

**What the record gives** [V][S].
- V = −(Gm₁m₂/r)(1 + (4/3)e^{−r/λ_X}) in the aligned vacuum (background ratio u = 1), with λ_X < 37.7 μm if the
  Sun and planets are not screened (`papers/phase-space-diameter.md` §8.2; `verify/phase_space_diameter.py`).
- A search of the record finds no velocity dependence assigned to this term.

**Its velocity dependence is relativistic** [D][V; two verifiers by different methods].
- Single exchange of a massive spin-2 field between point sources carries the factor (3γ² − 1)/2, with
  γ = u₁·u₂ the relative Lorentz factor. The massless graviton carries 2γ² − 1. The graviton's factor reproduces
  the O(G) terms of the Einstein–Infeld–Hoffmann two-body Lagrangian of general relativity [T].
- At 120 km/s: 1 + 2.40×10⁻⁷ for X, against 1 + 3.20×10⁻⁷ for the graviton.
- X is not velocity-gated at any range.

**Two other readings of "momentum gravity"** [D; negligible either way].
- #13's kinematics, where the dual of velocity is force: corrections are γ̃ − 1 = (1/2)(F/c̃)², with c̃ = c⁴/G. For
  the Sun and Earth, F/c̃ = 2.93×10⁻²² and γ̃ − 1 = 4.3×10⁻⁴⁴. But #13 §5 identifies dual rest with free fall,
  which makes the correction zero for any freely falling pair; #13 §2 says a black-hole merger "operates at F ~ c̃
  by construction".
  The two sections disagree (flag 56).
- The Siegel reading (flag 39, open): Standard-Model matter has no linear X coupling. Its coupling sits in the
  mixed block, with relative size about vF/(c⁵/G) = 2.9×10⁻²⁶ for the Sun and Earth, a product of velocity and
  force.

**A potential in momentum differences exerts no force** [D][V].
- A potential U(p_a − p_b) that depends only on momenta contributes nothing to ṗ = −∂H/∂x, in any external
  potential. It changes only how velocity relates to momentum, which is inertia.
- It leaves relative momenta unchanged only in free space or a uniform field. In a harmonic core, the canonical map
  X = p/(mΩ), P = −mΩx turns it exactly into an ordinary attraction in position, for orbits that stay inside the
  core: the founding image's exchange of x and v, realized. The map preserves the energy, so the contact gate's
  shortfall (§4) is unchanged.

## 3. A universal relative-velocity gate between ordinary bodies is excluded

*In plain terms: corrections to Newton's law that depend on relative velocity are old (Tisserand applied a
Weber-type law to the planets in 1872 [S]) and are already tested, because general relativity has one. A gated
term would shift planetary perihelia, the Moon's orbit and binary pulsars. At gravitational strength it is
excluded by at least eight orders of magnitude.*

**The model** [D][V].
- V = −(Gm₁m₂/r)[1 + εW(|v₁ − v₂|/v_a)], treated as a Lagrangian potential so that the canonical momentum is
  handled correctly.
- Circular orbits obey ω²r³ = GM[1 + εK(u)] exactly, with K = W − uW′ and u the orbital speed over the gate width.
  The apsidal advance follows from the same averaging that reproduces general relativity's 6πGM/(c²a(1 − e²)) [T].
- For a gate wider than orbital speeds the term acts like a first post-Newtonian velocity term with c replaced by
  the gate width.

**Bounds** [D; data S; two verifiers].
- |ε| < 8.7×10⁻⁹ for a Gaussian gate of width 0.3–3000 km/s in the e^{−v²/v_a²} convention, which is
  v* = 0.2–2100 km/s in the record's. A Lorentzian gate: |ε| < 9.4×10⁻⁹ for 0.1–3000 km/s.
- At the record's gate width (v_a = 170 km/s): |ε| < 3.5×10⁻¹¹, from Mars's perihelion (EPM2011).
- Below about 0.3 km/s, ε ~ 1 is excluded only qualitatively: a body at rest at a pole would have vanishing
  inertia for ε ≈ 8×10⁻⁵ at v_a = 0.1 km/s. No sourced numerical bound exists there.
- Which velocities the gate sees inside a composite body matters. If it acts on constituents, internal motion
  suppresses it and what remains is a composition-dependent G, bounded by torsion balances and MICROSCOPE under
  model-dependent assumptions. A gate on the difference of momenta, |m₁v₁ − m₂v₂|, is not Galilean invariant.
- None of this touches a gate confined to χ, which is the next question.

## 4. What the obituary covers

*In plain terms: the obituary tested the program's own dark-matter interaction, which acts only on contact, and
found that it cannot make the halo break up into velocity streams where it would need to. Paul's picture, a
long-range attraction gated in relative velocity, is a different model, and the obituary does not cover it. The
obituary's own scope is narrower than "impossible": it shows that clumping is required nowhere.*

**The program's interaction is contact-range** [D, record].
- Calc note #2: "the x-range collapsed to contact (range 1/m_φ, microscopic)", and "the force is contact-range" is one
  of its robustness reasons.
- The record's only relative-velocity gate is χ–χ scattering, σ_T(v) = σ₀F(v²/v*²) (#11 §8): a velocity-dependent
  self-interaction where χ distributions overlap, not a change to the 1/r law. χ gravity is ungated: "χ propagates
  on g (equivalence principle; Bullet-Cluster-safe)".

**The three branches** [D, record; reproduced].
- Particle χ: the collective pull falls short of the instability threshold by 10²⁸–10³¹ (#11 §9). The wiki
  build's recomputation from 3a's inputs (`review/wiki-build-checks/stream_stability_check.py`) gives ratios of 3.9×10⁻²⁸
  in a dwarf core and 2.9×10⁻³¹ in the Milky Way. "10²⁸–10³¹" quotes their exponents; the shortfall factors are
  2.6×10²⁷ and 3.5×10³⁰. A linearized calculation gives 3.3×10⁻²⁸ and 8.7×10⁻³¹ [D, two verifiers].
- Wave χ whose gate also makes dwarf cores (Scenario A): clumping is mandatory in ultra-faint dwarfs and would
  drain them, which observation excludes (#4).
- Wave χ with a free coupling (Scenario B): streams can form, but their strength is tunable over about ten orders,
  so they predict nothing (#3).
- So the obituary says velocity clumping is required nowhere. It does not say clumping cannot happen.

**Calc note #2's criterion for narrow gates** [D][V] (flag 58).
- 3a writes the threshold as g·n_gate ≥ m·min(σ, v*)². Its substitution σ → v* is the threshold of a cold stream
  that already exists, not of a smooth halo.
- Linearized, the threshold keeps the halo's dispersion: g·n·Λ_g ≥ m·σ², with Λ_g the gate's eigenvalue (§7).
- In the Milky Way 3a's form overstates the shortfall about 3× (2.9×10⁻³¹ against the linearized 8.7×10⁻³¹), the
  non-conservative direction for an obituary. In the dwarf core and the cluster it errs the other way. The
  verdict is unchanged. Both verifiers confirm the σ point, and both found the analysis's statement of the
  direction at the Milky Way wrong.

**If "premature" means "velocity structure is observed"** [T][S].
- Cold dark matter already contains about 10¹⁴ fine-grained streams near the Sun (Vogelsberger and White). The
  founding image predicted about ten broad ones, so only streams of that kind would test it.

## 5. The long-range variant: a velocity-gated attraction among χ

*In plain terms: this section sets up Paul's model. Dark-matter particles attract each other at long range, like
gravity, but only when they move at similar velocities. Nothing in the program supplies a field that could carry
such a force, so the model is tested as a hypothesis in its own right.*

**The model** [D].
- U = −G̃m_χ²W(|v − v′|/v*)/|x − x′| among χ only, added to gravity, with ε = G̃/G.
- In mean field it is a Jeans-type amplifier of spatial clumping among co-moving particles. Gravity and the gated
  term both scale as 1/k², so the gate rescales the Jeans wavenumber by the top eigenvalue Λ of an operator on
  velocity space.
- Streams spread through space, the founding image's structures, are exactly neutral in mean-field dynamics in a
  homogeneous medium (k = 0). In a cored halo the harmonic potential interconverts velocity and position
  structure, and above threshold the gate-only velocity-dipole modes (m = ±1) grow. The modes the gate adds are
  spatial lumps carried by a velocity-selected population of width about √(σv*).

**No carrier in the record** [D][V].
- X is massive: λ_X < 37.7 μm at u = 1, unscreened. #11 §8's m_φ is a free scale with no field behind it.
- Gating χ's own gravity is outside the record by postulate: "χ propagates on g (equivalence principle;
  Bullet-Cluster-safe)". It is observationally untested. Lensing and dynamical masses both see χ through ungated
  gravity, and χ re-virialized in a weaker force stays bound (one agent). An earlier ruling that observation
  excludes it is withdrawn (§11).
- §9 takes up whether any local field could carry the force.

**Three readings of a velocity-dependent potential** [D].
- Hamiltonian: the gate acts on canonical momentum. This is the record's reading: the lab notebook writes the
  energy ε(p; f) and the anomalous velocity ẋ ⊃ ∇ₚε (#1 §5.2).
- Lagrangian: the gate acts on velocity.
- Force at fixed velocity: −∇ₓU with ẋ = v. This is neither Hamiltonian nor Lagrangian; it is reported only as one
  edge of a bracket.
- Open [O]: whether the Hamiltonian reading is the right classical limit for a long-range gate. In it the kinematic
  and canonical velocity dispersions decouple, by up to 11.5× in the N-body of §8, and its linear theory loses
  meaning above ε ≈ 2.2 (2.24–2.29 at z = 50, 10 and 3), where the effective inverse inertia changes sign.
- In the Hamiltonian reading, gating on peculiar velocities alone is pathological (one agent; not rechecked). The
  gate is therefore taken on the full relative velocity, Hubble flow included.

## 6. What observations allow at the record's gate width

*In plain terms: in an expanding universe, two particles a few megaparsecs apart recede from each other at more
than v*, so the gate closes at that distance. That distance, expressed as a velocity, is exactly v* at every epoch,
and it falls on the scales that the Lyman-α forest of distant quasar spectra measures. The forest allows a force
of at most six to eighteen percent of gravity, while clumping needs more than gravity's full strength.*

**Hubble-flow gating** [D][V].
- Two χ a proper distance s apart in the Hubble flow move apart at Hs, so the gate closes at s_c = v*/H(z):
  1.78 Mpc comoving today, at most 2.03 Mpc near z = 0.63.
- In velocity units the gate scale is v* at every epoch, an exact identity. At DESI's Lyman-α pivot (z = 3),
  k_p·s_c = 1.08.
- The model changes the background expansion by nothing at order ε.

**The Lyman-α forest** [D; derived twice independently; DESI and Planck inputs S].
- Compressed DESI DR1 constraint at the pivot: Δ² = 0.379 ± 0.032, n = −2.309 ± 0.019.
- Record's reading: ε < 0.057 (matter ratio) to 0.106 (gas ratio) at v* = 120 km/s.
- Force at fixed velocity: ε < 0.0585 to 0.176. Its density kernel is R₁(y) = ∫₀¹R(yμ)dμ, which at the pivot is
  0.311, not the 0.803 of R (§11).
- In the record's reading the force lowers the power at the pivot: T² = 0.948 at ε = 0.1 and v* = 120 km/s.
- Older eBOSS compressed data then prefer ε ≈ 0.05 formally: χ² falls from 26.3 to 1.9 at ε = 0.0535. This is not
  evidence. Those data sit 4.9σ from Planck, any suppression near the pivot relieves that tension, the
  compression assumes a ΛCDM spectrum shape, and DESI agrees with Planck.
- These are estimates, not likelihoods. In the record's reading the response is a dip at the pivot and a rise at
  smaller scales, a shape a compressed (Δ², n) fit cannot represent. A full one-dimensional power-spectrum
  likelihood is open.
- The BOSS full-shape limit on long-range dark-matter forces (β < 0.0048) does not transfer. It is set by the
  background modification of the scalar model, which the gated model lacks (one agent's reading of the sources).

**The Sagittarius stream** [D; S].
- The leading/trailing asymmetry limit (Kesden and Kamionkowski, a 10% level stated without a confidence level and
  disputed by Keselman, Nusser and Peebles) gives ε ≲ O(1): 0.2–2.5 at v* = 120 km/s, depending on how the gate
  is averaged over the orbit and on the reading.
- It never beats the Lyman-α forest in the record's reading.

## 7. What clumping needs, and why the variant is decorative

*In plain terms: for velocity-selected lumps to grow, the gated attraction must be stronger than gravity, and in
the Milky Way and in clusters many times stronger. Observations allow at most six to eighteen percent. And at any strength the force
could not do the job the program introduced the gate for, making the cores of dwarf galaxies, so its strength
would be a free number the program cannot predict.*

**The threshold** [D][V].
- Velocity-selected modes need ε > 1/Λ_g(σ/v*). This exceeds 1 at every σ/v*, tending to 1 as σ/v* → 0 (1.000003
  at σ/v* = 10⁻³), and is at least 4.24 wherever σ ≥ v*. It equals 4/3 at σ/v* = 0.333.
- So at v* = 120 km/s the allowed strength is at least 9.4× too small in the record's reading and 5.7× in the
  force-at-fixed-velocity reading.
- The local model's own thresholds at v* = 120 km/s: at least 28.1 in the Milky Way (the longest mode that fits;
  161 at the solar circle's own scale; none at all once the halo re-virializes), and at least 693 in clusters (the
  crossover 1/Λ_g at σ/v* = 8.33). These exceed the Lyman-α bound (gas, record's reading) by 264 and 6.5×10³, and
  the loosest Sagittarius bound by 11.4.
- Both thresholds lie beyond the local model's validity, which ends near ε ≈ 1.5 in the Milky Way and 133 in
  clusters. Treat them as indicative.
- A gravitational-strength gate (ε = 1, or 4/3) adds no velocity-selected instability anywhere.

**Cores** [D, three independent recomputations].
- A gravitational-strength 1/r force scatters χ at σ_T/m = 2.4×10⁻⁶² cm²/g at 30 km/s (Born, ln Λ = 68.7 at
  b = 1 kpc).
- Making dwarf cores by scattering would need G̃/G ≈ 3.6×10³¹.
- So the force cannot make cores. Its strength would be a free parameter and any clumping optional: "decorative" in
  the net theorem's own word.

## 8. Narrow gates: the corner

*In plain terms: where the gate is narrower than about 30 km/s, comparable to the velocity spread of a dwarf
galaxy, the local model fails and no bound existed. A set of simulations found no velocity-selected structure up to
ten times gravity's strength. Corrected estimates from small-scale cosmology exclude twice gravity's strength for
gates from 10 km/s up, and three times it from 5 to 30 km/s in one of the two readings.*

**N-body** [D, executed; one agent; isolated cored halo].
- Direct-summation runs of a Plummer χ halo, N = 2000 (five more runs at N = 1000 test the resolution), three
  realizations per case and an ε = 0 control, the gated
  term switched on slowly; the record's reading, with one case (three realizations) in the
  force-at-fixed-velocity reading for comparison. 29 runs.
- In the record's reading, energy is conserved after the switch-on to 1.8×10⁻⁵ in 23 of the 26 runs; three runs
  at ε = 10 exceed it, the largest reaching 5.4×10⁻⁵. The record says 1.8×10⁻⁵ for all. This was noticed while
  porting the record into `verify/`, not by an agent. The force-at-fixed-velocity reading is not Hamiltonian and
  conserves no energy.
- At ε = 1, 3 and 10, with the gate as wide as the dispersion or 2.5× wider: no velocity-selected clumps, streams
  or coherent flows beyond the control over 43 central free-fall times, 0.1–0.6 Gyr in a dwarf. At ε = 10,
  ξ_u05 = −0.0069 ± 0.0063 over the three realizations, against +0.2339 for an injected population of clumps
  holding 2% of the mass.
- The runs detect clumps holding 2% of the mass, and streams from 5%.
- The record's reading reorganizes the halo instead: canonical momenta narrow, so the gate opens further, the
  kinematic dispersion becomes up to 11.5 times the canonical one, and the halo's half-mass radius changes by a
  factor 0.685–1.647.
- Not adjudicated, and noticed while porting the record into `verify/`, not by an agent: in all seven gated cases
  at N = 2000 the close-pair statistic ξ_u1 exceeds the control, by +0.0073 to +0.0231 (1.7–3.5σ on three seeds).
  In the injection test, clumps holding 2% of the mass raise ξ_u1 from +0.0146 to +0.0409 in one snapshot, a
  change comparable to that offset, so ξ_u1 alone cannot exclude them. The null rests on ξ_u05, which the same
  injection raises from +0.0852 to +0.2339, and on the stream statistics. The corner agent and the final critic
  read the runs as a null; nothing in the record separates the uniform ξ_u1 offset from the halo's
  reorganization.
- The N-body is not rerun by the gate: its snapshots (90 MB) are not kept. Its logs, diagnostics and injection test
  are in `review/momentum-gravity/scripts/corner/`.

**Observational proxies, rerun with corrected formulas** [D; estimates, not likelihoods; the final critic's
rerun, one agent].
- The corner agent's linear proxies used the two flawed systems of §11. The final critic reran them; the edges in
  v* moved, and the map stands.
- ε ≈ 2 is excluded from v* = 10 km/s up in both readings, by the reionization optical depth and dwarf central
  densities. In the record's reading ε = 2 lies close to where its linear theory loses meaning (ε ≈ 2.2), so the
  force-at-fixed-velocity reading carries this exclusion more safely [inference].
- ε ≈ 3 is excluded at v* = 5–30 km/s in the force-at-fixed-velocity reading: the dwarf density proxy rises ×9.54
  and the optical depth to 0.099 at v* = 5 km/s, against Planck's 0.054 ± 0.007. The record's reading gives no
  number there, because its linear theory has lost meaning (§5).
- ε ≈ 1 is in tension above v* ≈ 20–30 km/s and disfavoured from 3–5 km/s up, from the optical depth, dwarf
  densities, small-scale Lyman-α, and the heating of Segue 1 if early χ clumps survive.

**Not computed.**
- Gates below 3 km/s, where clumping would need ε of about 4–10, beyond the model's validity.
- Gates narrower than the dispersion in the record's reading.
- Instabilities slower than 43 free-fall times, or below the N = 2000 relaxation floor.
- The satellite-count proxy, which was not rerun with the corrected formulas.
- Whatever the corner holds, it needs a second gate scale 4–40× below the record's 120 km/s, and the cores of §7
  still need 3.6×10³¹.

## 9. Could any field carry a relative-velocity gate?

*In plain terms: when a force is carried by a field of definite spin, its dependence on the bodies' relative
velocity is a polynomial that grows with speed, with the speed of light as its scale. Switching a long-range force
off above 120 km/s would need fields of every spin with huge cancellations, or a medium, which makes the force
depend on motion through the medium rather than on the bodies' relative velocity. One known exotic framework has
the right shape, but its threshold depends on distance.*

**Finite spin** [D][V; two derivations].
- At tree level, exchange of a spin-J field between spinless point sources has a pole residue that is a degree-J
  polynomial in γ: P_J(γ) if massive, T_J(γ) if massless. The (v/c)² coefficients are J(J + 1)/4 and J²/2.
- Every such residue increases with velocity, so no single spin gives a gate. An order-one rise at 120 km/s needs
  J ≈ 3533 (massless) to 4996 (massive).
- Derivative couplings, form factors of composite sources, loops, nonlocal form factors in the transfer, and the
  record's spin-0 fields (τ and the other moduli) add no gate. Loops bring other functions of γ, all with velocity
  scale c. `notes/gate-mechanism.md` §2 gives the same result for the record's own X.

**No-go theorems** [T][S].
- Massless fields of spin 3 or more give no macroscopic force (Weinberg 1964, abstract read; Porrati 2008).
- Finitely many massive fields of spin above 2 cannot couple causally to gravitons (Afkhami-Jeddi, Kundu and Tajdini
  2019).

**A tower of spins** [D][V; one derivation].
- A tower can build only gates that are entire functions of γ, and only through cancelling terms. For the Gaussian
  gate at v* = 120 km/s the largest single-spin term is about 10^5421169 times the net (x = c²/v*² = 6.24×10⁶).
  Rational gates are impossible.

**A medium** [D][V; one derivation].
- A mediator propagating through a medium at speed c_s gives dependence on each body's velocity relative to the
  medium. Two co-moving bodies side by side feel 1/√(1 − V²/c_s²) times the static force: 1.155 at V/c_s = 0.5.
  This is a preferred-frame effect, not dependence on relative velocity.

**Continuous spin** [T][S, read twice: by the run-3 theory verifier, and by the drafting session on 2026-10-27,
whose fetch is in the session transcript, not the record; numbers D].
- A massless continuous-spin particle has infinitely many helicities and lies outside the theorems above.
  Schuster, Toro and Zhou (JHEP 04 (2023) 010, eq. 129) give, for a scalar current,
  L_int ≈ (g²/4πr)[1 − (ρ²r²/32)(|v_ij| − v_ij·r̂)² + …]. The correction depends only on the relative velocity and
  vanishes for co-moving bodies and for motion along the line joining them: the shape of Paul's question.
- But it matters when ρvr ~ ħc, so its threshold velocity falls with distance; it is not a fixed v*. A 120 km/s
  threshold at 1 kpc needs ρ = 1.6×10⁻²³ eV.
- It is worked out only for a scalar current. No gravitational (tensor) version exists, and the record has no such
  field.

## 10. Open

*In plain terms: what this investigation did not settle.*

- A full Lyman-α likelihood, with hydrodynamics, for the long-range variant (§6).
- A nonlinear cosmological simulation of the narrow-gate corner, including whether early χ clumps survive in
  ultra-faint dwarfs (§8).
- Slow collisionless instabilities beyond the N-body's window, and gates narrower than the dispersion (§8).
- Whether the uniform ξ_u1 offset in the gated N-body runs is the halo's reorganization or a weak
  velocity-selected signal (§8).
- Whether the Hamiltonian reading is the right classical limit for a long-range gate (§5).
- The observational status of gated χ–χ gravity: χ against stars in streams or merging clusters (§5).
- Whether the program's bimetric branch has Vainshtein screening at all (flag 57).
- Whether #11 §8's gate can be produced by X at all (`notes/gate-mechanism.md`).
- How the Sagittarius asymmetry weights the orbit, and the status of the 10% level (§6).
- A sourced numerical bound on a universal gate below about 0.3 km/s (§3).
- Whether "premature" rests on a particular observation (§4).

## 11. Record

*In plain terms: what was refuted or corrected along the way, how the sealed expectations scored, and what went
wrong in the process.*

**Refuted.**
- That every ε > 0 raises the Lyman-α power and deepens the eBOSS tension. It holds only for the force at fixed
  velocity; in the record's reading the power falls (§6).
- That the BOSS full-shape limit β < 0.0048 maps onto ε. It does not transfer (§6).
- That at strong coupling the clumping model has no purely growing mode past a certain threshold. The gate-only
  sector develops its own; the rate dips rather than saturating.

**Corrected, and withdrawn** [the main ones].
- The run-2 Lyman-α bound used the wrong force-law kernel, R in place of R₁, a factor 2.58 at the pivot. Both
  verifiers found it independently.
- The run-2 critic's record-reading bound, ε < 0.34, counted the Hubble term on the anomalous velocity twice. The
  bound is 0.057–0.106.
- Withdrawn: "gated χ–χ gravity is excluded by observation" (§5).
- The ordinary-matter bound at the record's gate width is 3.5×10⁻¹¹ from Mars, not 2×10⁻¹¹ from Mercury, which used
  the other gate convention.
- The Sagittarius bound is O(1), not a sharp 1.5.
- The diameter note's Vainshtein radius uses the formula for a massless mode (flag 57).
- The N-body's energy conservation was recorded as 1.8×10⁻⁵; three runs at ε = 10 exceed it, one reaching
  5.4×10⁻⁵ (§8).
- The answer's "(F/c̃)² ≈ 4×10⁻⁴⁴" is γ̃ − 1 = (F/c̃)²/2 (§2).

**Pre-registrations, scored.**
- Run 2 (not blind: three agents read it).
  - Right: the obituary stands for the program as written; no gate between ordinary bodies, only O(v²/c²)
    structure; the gate is χ–χ at contact; a universal version is excluded; the long-range variant meets
    small-scale-structure limits (the Lyman-α forest binds at v* = 120 km/s).
  - Partly right: clumping needs G̃/G ≳ (σ/v*)³, about 2 in the Milky Way and 580 in clusters. Executed: at least 28
    and at least 693 in the local model.
  - Wrong: that calc note #2's σ → v* substitution is generous to the instability. In the Milky Way it overstates the
    shortfall about 3×.
  - Weakest link: the O(1) factors were indeed the weak point, off by more than an order of magnitude in the Milky
    Way. Hubble-flow gating does not let the variant escape the cosmological bounds: the gate closes at a Hubble
    separation of exactly v*, the forest's scale.
- Run 3.
  - Right: the run-2 force law would be judged neither Hamiltonian nor Lagrangian; the record and run-2 numbers
    reproduce; a source correction (the BOSS mapping); the ordinary-matter envelope below 10⁻⁸, with the
    literature-input corrections under 3× (one coupling correction, for MICROSCOPE, exceeded it); no clumping in
    the N-body, and more strongly than predicted, none up to ε = 10.
  - Mostly right: the theory items. The fiber-overlap gate is not confined to contact range by itself (§9 and
    `notes/gate-mechanism.md` §3); what forbids a long-range version is relativistic factorization with finitely
    many fields of finite spin.
  - Wrong: the Lyman-α bound (predicted 0.1–0.5, got 0.057–0.106, anchored on the run-2 critic's 0.34); the
    Sagittarius bound (predicted 1–3, got 0.2–2.5); the corner (predicted no robust exclusion, but ε ≈ 2 is
    excluded from 10 km/s up, and ε ≈ 3 at 5–30 km/s in one reading).
  - Missed: continuous spin; the sign of the Lyman-α response in the record's reading; the gate-mechanism flag.
  - Weakest link: the compressed likelihood's shape was a real problem, and the N-body held up. The failures were
    formula errors in two linear models, which were not named.

**Process.**
- Run 1 was lost when the machine ran out of memory.
- Three run-2 verifiers were lost to a network error and redone in run 3.
- The run-2 pre-registration sat beside the agents' folders, and three agents read it. Their judgment-level
  text was not blind; their executed numbers were unaffected. Later pre-registrations were kept out of reach.

## Sources

- #11 `papers/broken-born-checkpoint-v2.md` §§7–9, 12, 13; #1 `notes/broken-born-theory.md` §5.2; #2–#4
  `notes/stream-stability.md`, `notes/wave-island.md`, `notes/ufd-endpoint.md`; #13
  `papers/conjugate-special-relativity.md` §§2, 5; `papers/phase-space-diameter.md` §8.2; HANDOFF §4.
- `review/momentum-gravity/`: the analyses, verdicts and critics' rulings, with the scripts named there.
- Einstein, Infeld and Hoffmann 1938; Fierz–Pauli propagator [T].
- Weinberg, Phys. Rev. 135, B1049 (1964) [S, abstract]; Porrati 2008 [S]; Afkhami-Jeddi, Kundu and Tajdini, JHEP 04
  (2019) 056 [S]; Schuster, Toro and Zhou, JHEP 04 (2023) 010, arXiv:2303.04816 [S].
- DESI DR1 Lyman-α compressed parameters; eBOSS compressed parameters and their 4.9σ tension with Planck
  (arXiv:2311.16377); Planck 2018 optical depth; BOSS full-shape bounds on long-range dark-matter forces
  (arXiv:2204.08484, 2309.11496) [S].
- Kesden and Kamionkowski 2006; Keselman, Nusser and Peebles [S].
- Mars perihelion (EPM2011), lunar laser ranging, binary pulsars [S]; Vogelsberger and White, fine-grained streams
  [S].
- Enander and Mörtsell, Vainshtein radii in bimetric gravity, eqs. 38–43 [S, read by the run-3 critic-numbers
  verifier and by the drafting session on 2026-10-27].
