# A closed Comatter universe — answer (2026-10-27)

Question (Paul): "Presumably a comatter universe is closed. Work out the cosmological consequences wrt
generalized general relativity. How small does momentum space get? How big does position space get?
Anything else of interest."

## Reading used (an assumption, flagged)

- "Generalized GR" = the program's gravity on the generalized metric H: H = diag(g, g⁻¹), a·ã = 1, massive
  X in the palindromic Hassan–Rosen branch at u = 1, τ with V = V₀[1 + cos(τ/f)], the dual-frame minisuperspace.
- "Closed" = k = +1.
- Not explored: Born's reciprocal relativity with a momentum space of fixed curvature radius (with #13's kinematics).
  The one result on it is below (Gr̃(2,5)).

## Evidence

- Workflow 1: five analysts (observations, dynamics, gravity sector, minisuperspace, momentum space), each with
  executed scripts and printed outputs.
- Workflow 2: ten verifiers, two lenses per analysis, plus a completeness critic. 469 claim checks: 403
  confirmed, 48 corrected, 2 refuted, 16 unreachable (arXiv rate limits). The two refutations are C23 (dynamics)
  and C37 (momentum space), described under "Anything else".
- My own checks: I reran the critic's fit and answer-number scripts (identical output), scored P3 against the
  grid, and read Akrami–Alestas–Nesseris's abstract (arXiv:2504.04226) myself.
- Single-agent results, reproduced but not independently verified: the corridor+Ω_K fit, the T*S³
  integrability result, the Gr̃(2,5) construction, and inflation's π/2 for light travel.
- Citations new from verifiers are [S] by that verifier. Of them I checked only Akrami et al.

## 1. The premise

- **Nothing derives closure.** [S][D][V]
  - No source derives closure from reciprocity (two novelty searches).
  - Born 1938 goes the other way: it takes Einstein's closed universe and transfers it to a momentum
    hypersphere.
  - The compact moduli of the polarization frame do not bound the universe: y = Y/a ∈ (0, 1] while Y grows.
- **The record needs it.** [D][V]
  - With V₀[1 + cos] ≥ 0, flat and open universes never turn around.
  - So row 5 ("turnaround = conjugate bounce") exists only if k = +1. This is R11 applied.
- **In the program's own model class the data disfavour closure at about 2σ.**
  - Corridor+Ω_K fit (DESI DR2 BAO plus DESI's compressed CMB prior): Ω_K = +0.0025 ± 0.0012, P(closed) =
    0.017–0.020. [V; background only, no SNe, calibrated against two published DR2 results]
  - It matches:
    - DESI DR2+CMB in ΛCDM+Ω_K: 0.0023 ± 0.0011. [S]
    - Exponential quintessence+Ω_K: 0.003 ± 0.001 (Akrami, Alestas, Nesseris 2025). [S]
  - The looser w₀wₐ+Ω_K result (P(closed) = 0.32) needs a phantom crossing, which w ≥ −1 forbids. It is not the
    program's model (flag 43).
- Curvature below |Ω_k| ≈ 10⁻⁴ cannot be measured (cosmic variance). [S]
- A measured closed |Ω_k| above 10⁻⁴ would falsify eternal inflation (Kleban–Schillo; Guth–Nomura). [S]

**Net:** closure is a requirement of the turnaround story, not a consequence of the program, and the current
data lean against it at about 2σ.

## 2. How big does position space get

- **Formula.** [V, two independent integrators]
  - a_max = (Ω_m + Ω_d)/|Ω_k|, good to 9×10⁻⁷.
  - Here Ω_d ≥ Ω_DE,0, so a_max ≳ 1/|Ω_k|, and up to 145× that for slowly thawing τ.
  - t_turn = (π/2)(Ω_m + Ω_d)|Ω_k|^{−3/2}/H₀, and t_crunch = 2 t_turn.
- **Lower bounds only.** |Ω_k| → 0 is the flat limit, so there is no upper bound. At 95% given closure:

  | Data | R₀ (curvature radius today) | a_max | R_max | t_turn |
  |---|---|---|---|---|
  | ΛCDM+Ω_K | > 132 Gpc | > 887 | > 1.2×10⁵ Gpc (2.2×10⁶⁵ l_P) | > 6.0×10⁵ Gyr |
  | Corridor+Ω_K | > 128 Gpc | > 827 | > 1.1×10⁵ Gpc | > 5.4×10⁵ Gyr |
  | Floor (\|Ω_k\| = 10⁻⁴) | > 445 Gpc | > 10⁴ | > 4.4×10⁶ Gpc | > 2.3×10⁷ Gyr |

  [V]
- **Grid example** (|Ω_k| = 10⁻³, f = M̄_P, w₀ = −0.8): a_max = 1726, t_turn = 1.24×10⁶ Gyr,
  R_max = 2.43×10⁵ Gpc = 7.5×10³⁰ m. Over the whole grid, R_max runs from 4.5×10³ to 1.9×10¹⁰ Gpc. [V]
- **Smallest size:** an inflationary throat, c/H_inf = 2.67×10⁵ l_P at the bound inflation scale. [D][V]

## 3. How small does momentum space get

Three readings answer different questions; only the second gives physical numbers.

1. **Shape: momentum space never closes.**
   - In the record's geometry the momentum fibre stays flat ℝ³ (k̃ = 0): its metric Y⁻¹ does not depend on p,
     for any X. [D][V]
   - Closure only makes momenta discrete. On S³ the spectrum is √(ν² − 1)ħ/R and the grain is ħ/R. On the
     dodecahedral space the lowest scalar mode is ν = 13. [D][V]
2. **Scale: smallest at the turnaround.** [V]
   - ã(turn)/ã(today) = 1/a_max < 1.1×10⁻³ (95% given closure).
   - The grain is ħc/R_max < 5.4×10⁻³⁸ eV.
   - The CMB temperature at the turnaround is below 3.1 mK.
   - There is no lower bound: these limits tighten without end as |Ω_k| → 0.
   - After the turnaround ã grows without bound into the crunch.
   - Absolute values of ã are a normalization: at k̃ = 0 the constant C is gauge, so only ratios are physical.
3. **Conjugate (ρ_λ) picture.** Our position S³ maps to a momentum S³ of radius ħR/λ², which is largest at the
   turnaround. Our momenta map to an unbounded lattice of spacing λ²/R. [D][V]

A compact momentum space would need a new postulate (k̃ ≠ 0). Its symmetric version, k̃ = k:

- survives N_eff, BBN and the observed momentum range only for λ ≲ 1.3 μm (LHC protons);
- never survives together with standard inflation, which would need λ ≤ 2×10⁻⁴⁹ m.

So that branch is dead unless you add it deliberately. [D][V]

## 4. Anything else of interest

**Turnaround and crunch** [V]
- The turnaround needs no negative energy:
  - τ thaws, passes its minimum at a = 1.3–19, and then oscillates as dust (|⟨w⟩| ≤ 1.1×10⁻⁷);
  - curvature then reverses the expansion;
  - a τ frozen at the hilltop never turns around.
- The record's "V eventually goes negative" as the cause of the turnaround is wrong.
- The crunch is driven by τ's kinetic energy (w = 1). It is not the time-reverse of the bang.

**Over-constraint** [V]
- It does not fail outright; it moves.
- t_turn ∝ |Ω_k|^{−3/2} at fixed (w₀, wₐ), so Ω_k is a third input.
- With t_turn > 5×10⁵ Gyr, the turnaround time can never test the count.

**Bimetric sector, with f dynamical** [D][V]
- f is closed with the same k.
- The aligned vacuum persists: 1 − y = 2(H² + k/a²)/M_X², which is 1.5×10⁻⁶¹ today and about 10⁻⁷⁰ at the
  turnaround.
- f's lapse is regular through ȧ = 0.
- β₁ > 0 is required. The record never states this.
- G_eff = 2G_N above about 1.5 TeV.
- Könnig's gradient instability operates for w > −1/2 above about 1.3 TeV and returns in the recollapse.
- The Higuchi bound holds through the dressed mass.
- If f is frozen, closure is excluded. But a frozen f contradicts M_f = M_g, and the record never defines
  E₀[J] (round-5 R1, open).

**Reciprocity breaks globally**
- The Fourier form of ρ fails on S³. Locally the error is (2/3)(σ/R)², about 10⁻⁵⁵ at 1 m. [D][V]
- Stronger (critic, single agent): on T*S³ only the exact x-polarization is integrable. Every tilt, including
  the mirror p-polarization, fails Frobenius by sin³θ × curvature. [D][V]
- Closure therefore cuts the Born U(1) on integrable polarizations down to Z₂.
- Consequence: if polarizations must be integrable, P5's mirror vacuum is unavailable globally. The record's
  section condition presupposes integrability without stating it. The energy cost of a non-integrable mirror
  is not computed. [O]

**Phase space cannot be "sphere × sphere"** [D][V]
- No product of a k = +1 position space with any closed 3-manifold is symplectic.
- A non-product option exists: Gr̃(2,5), the Euclidean Snyder–de Sitter orbit. It is compact, symplectic and
  exactly Born-reciprocal.
- Its Born length is √(R l_P), at least 149 μm, which the diameter note's tests exclude.
- To meet the program's bounds it needs a momentum-sphere radius of at least 46 E_P (from X's range) or
  1.7×10¹¹ E_P (from #13's maximum force), growing ∝ R.

**Light and causality** [V]
- Light emitted today reaches our antipode at t/t_turn = 0.96–1.13.
- With an inflationary throat, the whole S³ is in causal contact by a ≈ a_max/2.
- The Fischler–Susskind entropy bound fails near the antipode, at a ≈ a_max. Bousso's covariant bound holds.
- Two claims did not survive:
  - The momentum-space analysis placed the Fischler–Susskind failure at a ≈ 4×10⁻¹⁷. That is refuted: it
    assumed a 1 rad horizon.
  - The dynamics analysis said that in 6 histories light from the bang never completes the circuit. That is
    refuted: the analysis sampled two independent phases, not four.

**Counts and topology** [D][V]
- S³ carries two classes of polarization texture: [S³, Λ(4)] = Z₂.
- The lowest tensor modes of X are the ten L = 2 (Bianchi IX) modes.
- The universe holds a finite number of photons, 2.1×10⁹¹–6.6×10⁹⁵, conserved after e± annihilation.

**Prior art the record lacks**
- The τ potential is Frieman–Hill–Stebbins–Waga 1995's PNGB potential. The wiki cites it (†); #1 and #11
  do not. [S]
- Closed recollapse with oscillating quintessence is published (Barrow 1987; Tipler et al.), so the turnaround
  should be tagged [T]. [S]
- Artigas, Mielczarek and Rovelli 2019: compactifying the minisuperspace phase space makes the universe
  recollapse, and the paper cites Born reciprocity. This bears directly on "how big". [S, verifier]
- Moffat 2004 writes a closed momentum-space FRW metric following Born. [S, verifier]
- Tseytlin 1992 bounds cosmic size by duality. [S, verifier]

## 5. Record errors found (candidates for wiki-build flags)

1. **The 93.8% figure.**
   - #1's description of [19S] is wrong. [19S] fits a Higgs-like quartic in flat FRW, and 93.8% is the
     posterior probability of a negative vacuum energy (12.2% future transition + 81.6% already AdS).
   - #11's compound citation [19S, 20S, 21S] is a miscitation: [20S] fits V₀[1 + cos] with null curvature and
     mentions no AdS or collapse.
2. **Turnaround cause.** #11 §10 and HANDOFF §2 attribute the turnaround to V going negative. Under V ≥ 0 a
   closed universe turns around anyway.
3. **Over-constraint.** In a closed universe it moves to Ω_k (#11 §10, #1 §7.4).
4. **Corridor convention.** w_a ≈ −1.5(1 + w₀) holds only for a least-squares CPL fit with f ≥ M̄_P. The
   convention is unstated.
5. **"ρ implemented unitarily by Fourier" (#11 §3 and wiki pages).** It is true on ℝ^d only, and needs scoping
   if closure is adopted.
6. **Dual curvature k̃ (#1 §6, §9, §10; #11 §13 row 10).**
   - "Closed dual space ⇒ negative ΔN_eff" is not a consequence of k = +1.
   - It needs a compact-momentum postulate.
7. **Missing derivation.** No document derives the dual Einstein–Hilbert term (ãȧ̃², M̃) from S_H, yet #1 §6's
   equation is tagged [D].
8. **R11** omits two conditions: a_max ≥ Ω_m/|Ω_k|, and ρ_m + 2ρ_r + 4K − 2V ≥ 0 at H = 0.
9. **Bimetric statements.**
   - β₁ > 0 is required but never stated.
   - #11 §10 omits the doubling G_eff = 2G_N for H ≫ M_X.
   - "Higuchi trivially satisfied by a heavy X" is right in conclusion and incomplete in reasoning.

## 6. Pre-registration score (sealed, sha256 5b1fb233…)

- **P1, P3, P9, P10, P11: confirmed.** P3 holds in 8 of 8 matching grid histories (a_max 1098–9076,
  t_turn 7.9×10⁵–6.5×10⁶ Gyr, R_max ≥ 1.5×10⁵ Gpc).
- **P2: numbers confirmed.** I did not foresee that w₀wₐ+Ω_K is the wrong proxy, or that in the program's class
  closure sits about 2σ out rather than within 1σ.
- **P4: mostly right.**
  - "No edge to momentum space" holds.
  - The bounds hold: ≤ 1.1×10⁻³ and ≤ 3.1 mK.
  - I described the conjugate picture only as a lattice. It is also a momentum S³ of radius ħR/λ².
- **P5 (weakest link): partly wrong.**
  - The normalization a = R/λ is gauge at k̃ = 0.
  - Row 10's knob is not removed; it survives as an independent postulate.
  - The dual terms are negligible after inflation (≤ 10⁻¹⁹⁸), as predicted.
- **P6: partly wrong.**
  - The Higuchi bound holds during inflation via the dressed mass.
  - The real problem is the Könnig gradient instability.
  - There is no snag at the turnaround (I gave the snag 0.3).
- **P7, P8: confirmed and strengthened.**
  - Closure breaks global reciprocity through integrability as well as through spectra.
  - I did not foresee the non-product Gr̃(2,5).
- **Expected overall answer:**
  - "Closure is natural for the program" was wrong: nothing derives it.
  - The rest stands: it is needed for row 5, it is lower bounds only, it is about 2σ against, and only global
    reciprocity breaks.

## 7. Gaps, ranked

1. **(High) Derive the dual Einstein–Hilbert term from S_H.** Every dual-frame statement, including #11 §10's
   a⁻⁶ step and row 10, currently tests a postulate.
2. **(High) Fit the actual model** (V₀[1 + cos] + Ω_K) to CMB, BAO and SNe with Cobaya/CAMB. This decides the
   premise.
3. **(Medium)** Inflation and the bimetric sector together. The ±K_ref splitting induced by closure.
   Perturbations and X's L = 2 modes through the collapse.

## Files

- `w1/*.json`: analyst results.
- `w2/*.json`: verifier verdicts.
- `w2/critic.json`: rulings, gaps and load-bearing answers.
- `critic/*.py` and `*.out`: the critic's scripts, including the fit (`f_corridor_curvature_fit`) and the
  answer numbers (`g_answer_numbers`).
- `dynamics/grid.csv`: the 96 histories.
