# A closed Comatter universe: the size of position space and of momentum space

*Working note, 2026-10-27. Status: computed. The analyses' results were each checked by two independent verifiers and
a completeness critic. Four results are the critic's own and were checked by one agent only; they are
marked where they appear: the corridor fit (§2), the integrability result and Gr̃(2,5) (§5), and inflation's π/2
(§8). The note has not been through a blind review round. Every number is recomputed in
`verify/closed_universe.py`. The analyses, verdicts and scripts are in `review/closed-universe/`.
Conjecture and direction, P.R.; derivations, counterexamples, verification, drafting, Claude (Anthropic).*

## 1. The question, the reading, the method

*In plain terms: Paul asked what follows if the universe is closed — finite in volume, like the surface of a
balloon one dimension up — and specifically how large position space becomes and how small momentum space
becomes. The answer depends on what "generalized general relativity" means, and the reading used here is the
program's own gravity.*

Paul's question (2026-10-27): "Presumably a comatter universe is closed. Work out the cosmological consequences
wrt generalized general relativity. How small does momentum space get? How big does position space get?
Anything else of interest."

**Reading [assumption].**
- "Generalized general relativity" is taken to mean the program's gravity on the generalized metric H:
  - H = diag(g, g⁻¹) in the vacuum, with a·ã = 1 (#11 §5, §10);
  - the massive momentum graviton X in the palindromic Hassan–Rosen branch at background ratio u = 1
    (#11 §7; `papers/phase-space-diameter.md` §8.2);
  - τ with V = V₀[1 + cos(τ/f)] (#11 §10);
  - the dual-frame minisuperspace (#1 §6).
- "Closed" means spatial curvature k = +1, so Ω_k < 0.
- Not explored: Born's reciprocal relativity with a momentum space of fixed curvature radius. §5 gives the one
  result bearing on it.

**Method.**
- A pre-registration was sealed before dispatch; it is scored in §10.
- Five analyses: observations, dynamics, gravity sector, minisuperspace, momentum space.
- Two verifiers per analysis, each working from the extracted claims only.
- A critic that ruled on the tensions between analyses.
- Tally: 469 claim checks, 403 confirmed, 48 corrected, 2 refuted (§10), 16 not reached.
- Conventions: H₀ = 67.4 km/s/Mpc and Ω_m = 0.315. The curvature radius today is R₀ = c/(H₀√|Ω_k|).

## 2. The premise, and the turnaround it buys

*In plain terms: nothing in the program forces the universe to be closed. But the program's dark-energy
potential never goes negative, and with such a potential only a closed universe stops expanding and falls
back. The program's prediction that the expansion turns around therefore needs closure. Current data lean
mildly against closure.*

**Nothing derives closure** [S][D][V].
- No source derives a closed universe from Born reciprocity. Two independent searches of arXiv, INSPIRE and
  the web found none.
- Born 1938 goes the other way. It starts from Einstein's closed universe and gives momentum space a
  hypersphere to match, with the radius b fixed from the classical electron radius.
- The compactness of the polarization frame's moduli space does not bound the universe. On the β₁ > 0 branch
  the ratio y = Y/a stays in (0, 1] while Y grows with a [V].

**The turnaround needs k = +1** [D][V].
- With V ≥ 0, H² > 0 at every epoch when k ≤ 0, so flat and open universes expand forever (flag 27).
- In a closed universe the turnaround happens with V ≥ 0 throughout:
  - τ thaws and passes its potential minimum, at a = 1.34–18.5 in the histories recomputed;
  - it then oscillates as dust, with |⟨w⟩| ≤ 1.1×10⁻⁷ at the turnaround;
  - curvature then reverses the expansion.
- With τ frozen at the hilltop, there is no turnaround.
- #11 §10's "eventually goes negative" therefore names the wrong cause (flag 27 addendum).
- The record's identification of the turnaround with the conjugate bounce (row 5) exists only if k = +1.

**Size and timing** [D][V]:

```text
a_max   = (Ω_m + Ω_d)/|Ω_k|
t_turn  = (π/2)(Ω_m + Ω_d)|Ω_k|^(−3/2)/H₀
t_crunch = 2 t_turn
```

- Ω_d is τ's dust-like density, referred to today. It satisfies Ω_d ≥ Ω_DE,0, so a_max ≳ 1/|Ω_k|.
- The crunch is driven by τ's kinetic energy (w → 1). It is not the time-reverse of the bang.

**Conditions** [D][V]. The turnaround needs:
- a_max ≥ Ω_m/|Ω_k|;
- at H = 0, ρ_m + 2ρ_r + 4K − 2V ≥ 0, where K is τ's kinetic energy density.

Round-5 R11 states the existence result without these (flag 50).

**Prior art** [T]. Recollapse of a closed universe with oscillating quintessence is published: Barrow 1987 †;
Tipler et al., gr-qc/0003082, §7 [S]. The τ potential is the pseudo-Nambu–Goldstone potential of Frieman,
Hill, Stebbins and Waga 1995 (astro-ph/9505060) [S] (flag 54).

**The over-constraint moves** [D][V].
- At fixed (w₀, wₐ), t_turn ∝ |Ω_k|^{−3/2}, so Ω_k is a third input beside (f, τᵢ) (flag 46).
- Ω_k is measurable, but the data bound t_turn only from below (§3), so t_turn cannot test the count.

**Data.**
- Published values [S]:
  - DESI DR2 + CMB in ΛCDM+Ω_K: Ω_K = 0.0023 ± 0.0011 (arXiv:2503.14738, Table 5).
  - Exponential quintessence with free curvature: Ω_K = 0.003 ± 0.001 (Akrami, Alestas, Nesseris 2025,
    arXiv:2504.04226, abstract).
- The program's own model class, approximated by the thawing corridor wₐ = −s(1 + w₀) with w₀ ≥ −1
  [V; the critic's fit, one agent]:
  - Fitted to DESI DR2's distances plus DESI's compressed CMB prior, with Ω_K free.
  - The fit uses the background only, with no supernovae. It reproduces DR2's published flat w₀wₐ fit
    and its ΛCDM+Ω_K value.
  - Ω_K = +0.0025 ± 0.0012 for s = 1.5 and +0.00245 ± 0.00119 for s = 2.0.
  - The probability of closure is 0.017–0.020.
- The w₀wₐ+Ω_K family gives Ω_K = +0.00071 ± 0.00151 in the same fit, with probability of closure 0.32.
  - Its looser bound comes from the phantom crossing (w₀ + wₐ < −1 at w₀ > −1).
  - The program's w ≥ −1 forbids that crossing (flag 43), so w₀wₐ+Ω_K is not a proxy for the program's
    model.
- Curvature below |Ω_k| ≈ 10⁻⁴ is not measurable against cosmic variance [S: Leonard, Bull and Allison 2016,
  arXiv:1604.01410].
- A measured closed curvature with |Ω_k| > 10⁻⁴ would exclude eternal inflation in our past [S: Kleban and
  Schillo 2012, arXiv:1202.5037; Guth and Nomura 2012, arXiv:1203.6876].

**Result.** Closure is a requirement of the turnaround story, not a consequence of the program. In the
program's model class the data disfavour it at about 2σ.

## 3. How big position space gets

*In plain terms: a closed universe reaches a largest size and then recollapses. Measurements so far only say
the curvature is small, so they set a minimum on that largest size and no maximum: the flatter the universe,
the larger it grows before turning around.*

**Lower bounds only** [V]. |Ω_k| → 0 is the flat limit, so there is no upper bound. The bounds below are the
95% bound on |Ω_k| given closure: the posterior is treated as a Gaussian truncated to Ω_K < 0, with
a_max ≥ (Ω_m + Ω_DE,0)/|Ω_k|.

| Input | \|Ω_k\| | R₀ today | a_max | R_max | t_turn |
| --- | --- | --- | --- | --- | --- |
| DESI DR2 + CMB, ΛCDM+Ω_K | < 0.00113 | > 132.4 Gpc | > 886.9 | > 1.174×10⁵ Gpc = 2.242×10⁶⁵ l_P | > 6.015×10⁵ Gyr |
| Corridor + Ω_K fit (s = 1.5) | < 0.001207 | > 128.0 Gpc | > 829.5 | > 1.062×10⁵ Gpc | > 5.441×10⁵ Gyr |
| Cosmic-variance floor | = 10⁻⁴ | > 444.8 Gpc | > 10⁴ | > 4.448×10⁶ Gpc | > 2.279×10⁷ Gyr |

**A representative history** (|Ω_k| = 10⁻³, f = M̄_P, w₀ = −0.8) [V]:
- a_max = 1726 and t_turn = 1.24×10⁶ Gyr;
- R₀ = 140.7 Gpc and R_max = 2.43×10⁵ Gpc = 7.49×10³⁰ m;
- T_CMB at the turnaround is 1.58 mK.

Across |Ω_k| = 10⁻⁵–10⁻², f = 0.2–2 M̄_P and w₀ = −0.95 to −0.7:
- R_max runs from 4.54×10³ to 1.91×10¹⁰ Gpc;
- t_turn runs from about 2.3×10⁴ to 9.8×10¹⁰ Gyr.

**The smallest size** [D][V]. The closed universe's smallest radius is set before the hot big bang. An
inflationary de Sitter throat has radius c/H_inf = 2.67×10⁵ l_P for an inflation scale at the bound the diameter
note uses, E_inf < 1.39×10¹⁶ GeV (from r < 0.036).

## 4. How small momentum space gets

*In plain terms: momentum space does not close up. What closure does is make momenta discrete, as a string of
fixed length can only hold certain wavelengths. The spacing between allowed momenta, and the overall momentum
scale, are smallest at the turnaround and shrink further the flatter the universe is.*

There are three readings of the question. Only the second gives physical numbers.

1. **Shape: the momentum fibre stays flat** [D][V].
   - In the record's geometry the momentum block of H is Y⁻¹, the same at every p, for any X. So the fibre is
     flat ℝ³ (k̃ = 0), and k = +1 does not induce k̃ = +1.
   - The dictionary's "closed dual space ⇒ negative ΔN_eff" is therefore not a consequence of closure (flag 48).
   - Closure makes momenta discrete. On S³ the spectrum is √(ν² − 1)·ħ/R, so the spacing is of order ħ/R.
   - On the Poincaré dodecahedral space the lowest nontrivial scalar mode is ν = 13 [V; anchor: Aurich et al.
     2005].
2. **Scale: smallest at the turnaround** [V].
   - ã(turnaround)/ã(today) = 1/a_max.
   - At the 95% bound given closure (ΛCDM+Ω_K): 1/a_max < 1.128×10⁻³, the grain ħc/R_max < 5.446×10⁻³⁸ eV,
     and T_CMB at the turnaround < 3.073 mK.
   - For the corridor fit: < 1.206×10⁻³, < 6.022×10⁻³⁸ eV and < 3.286 mK.
   - At the cosmic-variance floor: 10⁻⁴, 1.438×10⁻³⁹ eV and 0.273 mK.
   - There is no lower bound. After the turnaround ã grows without bound into the crunch.
   - Absolute values of ã are a normalization: with k̃ = 0 the comoving unit C is a gauge choice.
3. **The conjugate picture** [D][V].
   - Read through ρ_λ, our position S³ of radius R becomes a momentum S³ of radius ħR/λ², which is largest at
     the turnaround.
   - Our discrete momenta become an unbounded position lattice of spacing λ²/R.

**A compact momentum space would be a new postulate** [D][V]. Its symmetric reading, k̃ = k with vM̃² = M_P²,
fixes the a⁻⁶ term and the dual curvature by a single self-dual radius R_sd. At |Ω_k| = 10⁻²:
- BBN requires R_sd ≤ 1.568×10¹⁷ m, and N_eff requires R_sd ≤ 3.029×10²⁵ m.
- The observed momentum range sets a minimum on R_sd. The LHC's 6.8 TeV protons together with N_eff and BBN
  then need λ ≤ 1.278×10⁻⁶ m.
- Adding standard slow-roll inflation needs λ ≤ 1.986×10⁻⁴⁹ m.
- For λ = √(l_P c/H₀) the window is empty.

The reading also contradicts the record's k̃ = 0, and it rests on the underived dual Einstein–Hilbert term
(§7). It is dead unless Paul adds a compact momentum space deliberately.

## 5. Reciprocity on a closed space

*In plain terms: on a finite space, position and momentum stop being interchangeable as wholes, because one
is continuous and the other discrete. Locally the exchange still holds to extraordinary accuracy. Closure
also leaves the program's position-like vacuum as the only one that can be laid consistently across the whole
universe.*

**The global Fourier map fails; the local one survives** [D][V].
- On S³ or a torus, position has a continuous spectrum and momentum a discrete one, so no unitary operator
  exchanges them.
- A wave packet of width σ is exchanged by the flat transform to relative accuracy (2/3)(σ/R)². That is
  3.5×10⁻⁵⁵ at σ = 1 m for |Ω_k| = 10⁻².
- #11 §3's "the Fourier transform implements it unitarily" needs that scope once closure is adopted (flag 47).

**Only the position polarization is integrable** [D][V; from the critic alone, not independently verified].
- The program's U(1) family of polarizations is L_θ = e^{θI}(vertical). This assumes the Levi-Civita
  splitting in which H = diag(g, g⁻¹).
- Every L_θ is Lagrangian. On T*S³, the component of [L_θ, L_θ] outside L_θ is ℓ²p·sin³θ/R², the curvature
  of S³ times sin³θ.
- So only θ = 0 (and θ = π, the same plane) is integrable. Every tilt, including the mirror momentum
  polarization θ = π/2, fails the Frobenius condition. On T³ every θ is integrable.
- The size of the effect is (L/R₀)² = 5.309×10⁻⁵⁵ at L = 1 m for |Ω_k| = 10⁻².
- Consequences:
  - Closure cuts the Born rotation's U(1) on integrable polarizations down to Z₂.
  - If the section condition (#1 §2) requires integrability, P5's mirror vacuum has no global realization in
    a closed universe.
  - The record does not state that requirement. If non-integrable polarization fields are allowed, the energy
    cost of the mirror is not computed [O].

**Compact phase spaces** [D][V; the Gr̃(2,5) construction is the critic's, one agent].
- No product X × M is symplectic when X is a k = +1 position space (S³ or any spherical space form) and M is
  any closed 3-manifold. In the product, H² comes from M alone, so [ω]³ would be a class pulled back from
  H⁶(M) = 0.
- So Born's position sphere times a momentum sphere cannot be a phase space.
- A non-product compact phase space exists: Gr̃(2,5) = SO(5)/(SO(2)×SO(3)), the Euclidean Snyder–de Sitter
  orbit. It is Kähler, and Born reciprocity is the inner SO(5) automorphism exchanging X and P [S: Mignemi and
  Štrajn 2015, arXiv:1501.01447; V].
- Its reciprocity length is λ = √(Rħ/κ). With κ = m_P·c this is √(R₀ l_P) = 1.489×10⁻⁴ m at |Ω_k| = 10⁻²,
  which the diameter note's two tests exclude.
- To meet the program's own Born-length bounds, the momentum-sphere radius κc must be at least:
  - 46.5 E_P today, from X's range of 37.7 μm;
  - 1.72×10¹¹ E_P today, from #13's maximum force;
  - 4.1×10⁴ and 1.5×10¹⁴ E_P respectively at the turnaround.

**Prior art on compact phase spaces and recollapse** [S, found by a verifier].
- Artigas, Mielczarek and Rovelli 2019 (arXiv:1904.11338): compactifying the minisuperspace phase space makes
  the universe recollapse. The paper cites Born reciprocity.
- Moffat 2004 (gr-qc/0401117) writes a closed momentum-space FRW metric following Born.
- Tseytlin 1992 (hep-th/9112004) bounds the size of a toroidal universe by duality.

## 6. The momentum graviton X in a closed universe

*In plain terms: the program's second, massive graviton X lives on a second metric f. If f is a dynamical
field with the same strength as ordinary gravity, it closes along with the universe and stays aligned with
it, and the turnaround is smooth. If f is a fixed background, a closed expanding universe is impossible, but
that reading contradicts the record elsewhere.*

**Hassan–Rosen with f dynamical** (palindromic βₙ = β₄₋ₙ, zero-vacuum branch β₀ = −4β₁ − 3β₂, M_f = M_g)
[D][V]:
- The algebraic equation for y = Y/a does not depend on k.
- f is closed with the same k. The SO(4)-invariant symmetric 2-tensors on S³ form a one-dimensional space;
  that unequal curvatures are inconsistent is [T: Comelli, Crisostomi, Nesti, Pilo 2012, arXiv:1111.1983].
- The exact relation on the branch:

  ```text
  3M̄²(H² + k/a²) = ρ + (M̄²M_X²/8)·(β₁/(β₁ + β₂))·(1 − y)⁴/y
  ```

- At leading order, 1 − y = 2(H² + k/a²)/M_X², which is 1.5×10⁻⁶¹ today at the smallest allowed
  M_X c² = 5.24 meV.
- M_X² = 4m²(β₁ + β₂), confirming flag 5.
- Every broken vacuum has Λ_g = −3m²(β₁ + β₂)(u − 1)² = 18m²u(β₁ + β₂)²/β₁.
- β₁ > 0 is required. For β₁ ≤ 0 the aligned branch is bounded, or ends at a broken vacuum with negative Λ_g
  and a Higuchi ghost (flag 51).
- The turnaround is regular: in a toy closed history, f's lapse passes smoothly through ȧ = 0 (a_max = 1.588667,
  lapse 1.226664 there).

**The early universe** [D][V].
- For H ≫ M_X the effective Planck mass is M_g², half its late value 2M_g², so G_eff = 2G_N. The halfway point is at T ≈ 1.55–1.58 TeV
  (H/M_X = 0.75–0.77) for the smallest M_X, scaling as √M_X. #11 §10 omits this step (flag 52).
- The Higuchi bound holds through the dressed mass, m_FP²(y) − 2(H² + k/a²) = −yρ_y/(3M_g²) > 0. The
  fixed-mass argument "trivially satisfied by a heavy X" does not (flag 53).
- Könnig's scalar gradient instability for w > −1/2 operates above about 1.3 TeV (H ≈ 0.5 M_X). It returns in
  the recollapse, and equal Planck masses close the usual escape from it.

**f frozen** [D][V].
- A frozen flat f cannot be written in k = +1 FRW form: the curvature component (X² + Ẏ²)sin²χ/X² never
  vanishes.
- A frozen scale (Ẏ = 0) makes the Bianchi constraint proportional to ȧ, so there is no expanding universe
  for any k.
- Every frozen f is the M_f → ∞ limit, which the record's equal Planck masses (`notes/beta-coefficients.md`
  §3) exclude.
- The record never defines E₀[J] beyond "the polarization frame" on compact moduli. Round-5 R1 holds that
  question open.

## 7. The dual frame: what closure fixes and what it does not

*In plain terms: the program's description in which momentum space expands while position space contracts
has its own gravity term, and that term is postulated rather than derived. With the record's normalization it
is negligible after inflation, and the universe never comes near the point where the two descriptions have
equal size.*

**The term is underived** [O] (flag 49). The dual Einstein–Hilbert term in ã (with its mass M̃) is used in #1
§6 under a [D] tag, but no document derives it from S_H. The a⁻⁶ step in G_eff (#11 §10, row 10) rests on it.

**Only two combinations are physical** [D][V]. Under the record's dictionary, only vM̃²C³ (the a⁻⁶ term) and
vM̃²k̃C (the dual curvature) are physical. So "M̃ = M_P" constrains nothing unless the comoving unit C is
fixed. Closure fixes the normalization a = R/λ but not the a⁻⁶ coefficient.

**With the record's normalization** (C = 1, M̃ = M_P, λ = l_P) [D][V]:
- The a⁻⁶ term is below 10⁻¹⁹⁸ of the total after inflation, for |Ω_k| ≤ 10⁻². At k̃ = 0 it is the only dual
  term.
- An inflationary throat has c/H_inf = 2.67×10⁵ l_P, so ã ≤ 3.75×10⁻⁶ there. The self-dual point a = ã is never
  reached after inflation begins.

**The radius–mass pairing** [D][V].
- Pairing the radius R with the total mass M = ρ·2π²R³/c² gives G·M/c² = (3π/4)R at H = 0.
- The aspect ratio at a turnaround spans 4/(3π) to 8/3 across conventions.
- This is the closed Friedmann equation at H = 0, with ħ cancelling. The obituary of "square exactly at the
  bounce" (`papers/phase-space-diameter.md` §6) stands.

## 8. Light, horizons and counts

*In plain terms: a closed universe can be crossed. Whether light circles it before the crunch depends on
inflation: with inflation, the whole sphere comes into causal contact well before the turnaround.*

- **Light** [V]. The conformal time from today to the turnaround is π + c·√|Ω_k|, with c = −1.98 to +0.62 in
  the four histories recomputed. Light emitted today therefore reaches our antipode near the turnaround.
- **Inflation** [D][V; the critic's, one agent]. A closed de Sitter phase starting at a throat adds π/2 of conformal time. With it the
  whole S³ is in causal contact by about a_max/2, and light circles the universe in every history.
- **Entropy bounds** [D][V, review record]. The Fischler–Susskind bound fails as the particle horizon reaches
  the antipode, at a ≈ a_max. Bousso's covariant bound holds.
- **Photons** [V]. The number of CMB photons in the whole universe is finite: n_γ·2π²R₀³ = 2.1×10⁹¹ at
  |Ω_k| = 10⁻² to 6.6×10⁹⁵ at 10⁻⁵. It is conserved after e± annihilation.
- **Topology** [D]. S³ carries two homotopy classes of polarization texture, [S³, Λ(4)] = Z₂, which follows
  from π₃(Λ(4)) = ℤ₂ [T][V]. The same manifold has π₁(Λ(4)) = ℤ [T][V] and π₂(Λ(4)) = ℤ₂ [T], so selecting
  the polarization can leave strings of the Maslov phase τ, which exist on the light Maslov circle too, and,
  where the order parameter ranges over the whole manifold, point defects, the monopole type. On the light
  circle alone π₂ = π₃ = 0, and neither the point defects nor the textures exist there. All of this assumes
  d = 4 and that the U(4) acting on the polarization is global, the verifiers' caveats (flag 61;
  `verify/closed_universe.py` section F). X's lowest tensor modes on S³ are the L = 2 (Bianchi IX) modes [D].

## 9. What is open

1. **Derive the dual Einstein–Hilbert term from S_H** [O]. Every bound on the dual frame, including #11 §10's
   a⁻⁶ step and row 10, currently tests a postulate (flag 49).
2. **Fit the program's model properly** [O]. The fit should use V₀[1 + cos(τ/f)] plus Ω_K against full CMB, BAO
   and supernova likelihoods (Cobaya/CAMB). It decides the premise: the background fit of §2 has no
   supernovae.
3. **The remaining calculations** [O]:
   - inflation and the bimetric sector together (G_eff = 2G_N during inflation, two light gravitons);
   - the energy splitting between the ±K_ref polarizations that closure induces;
   - perturbations, and X's L = 2 modes, through the recollapse.
4. **Defects of the polarization** [O]. If a transition in the early universe selected the polarization, the
   ℤ₂ point defects and the τ-strings of §8 could form at it; the gravity-sector analysis lists their fate as
   open (`review/closed-universe/analyses/gravity-sector.json`). Whether such a transition happened, what it
   left, and whether the point defects would pose a monopole problem of the program's own are not computed.
   They are defects of the program's own order parameter, unlike conjugate-sector solitons, whose existence
   depends on gauge content the record does not specify (flag 61; #11 §14 item 12).

## 10. Record of the investigation

**Refuted along the way.**
- *Light from the big bang never circles the universe in 6 histories.* Refuted: the grid sampled only two
  independent phases of τ's oscillation, not four. With eight phases, every history completes the circuit
  in some phase. The result is in any case moot once inflation is included (§8).
- *The Fischler–Susskind bound fails at a ≈ 4×10⁻¹⁷ during the collapse.* Refuted: it assumed a horizon of
  1 rad, but the horizon reaches the antipode at the turnaround (§8).

**Corrected.**
- *"A doubly compact reciprocal phase space must be torus-like."* Wrong: Gr̃(2,5) (§5).
- The w₀wₐ+Ω_K closed-side bounds first quoted for "how big" used the wrong model class (§2) and central
  rather than closure-conditional bounds (§3).

**Pre-registration** (`review/closed-universe/preregistration.md`, SHA-256 5b1fb233…, sealed before dispatch).
- Confirmed: P1 (turnaround iff k = +1), P3 (size and timing, 8 of 8 matching histories), P9 (the R–Mc
  pairing), P10 (no over-constraint without Ω_k) and P11 (Z₂ textures).
- Confirmed and strengthened: P7 (reciprocity breaks globally) and P8 (nothing observable from finite volume).
- P2: the numbers are confirmed. It did not anticipate that w₀wₐ+Ω_K is the wrong proxy.
- P4: mostly confirmed. It described the conjugate picture only as a lattice.
- Partly wrong:
  - P5, the pre-registered weakest link: the normalization is a gauge choice, and row 10's knob survives as a
    postulate.
  - P6: the Higuchi bound holds during inflation; the gradient instability is the problem.
- The expected overall answer called closure "natural for the program". It is not: nothing derives it.

## Sources

- #11 `papers/broken-born-checkpoint-v2.md` §3, §5, §7, §10, §13 row 5 and row 10
- `papers/phase-space-diameter.md` §6, §8.2, §8.4; `review/round5-adjudication.md` R1, R11
- #1 `notes/broken-born-theory.md` §2, §3, §6, §7
- `notes/geometric-core.md` Corollary 3; `notes/beta-coefficients.md` §3
- `review/wiki-build-flags.md` flags 5, 27 (addendum), 43, 45–54, 61
- `verify/closed_universe.py`; `review/closed-universe/`
