# Spontaneous Breaking of Born Reciprocity: Two Toy Models

*Anonymous working manuscript submitted for adversarial review. The manuscript may contain errors or confabulations; the reviewer is asked to find them.*

## Abstract

Born reciprocity, the phase-space map ρ: (x, p) → (p, −x), is an exact symmetry of quantum kinematics but not of observed dynamics, which is local in position. A natural explanation is spontaneous breaking: a ρ-symmetric action whose vacuum selects a Lagrangian polarization, with the neutral metric η = ωK (K a real structure, K² = 1) as order parameter. The idea has been stated before, but we found no explicit model of ρ itself being spontaneously broken. We study two.

- **(I) A coset sigma model** of a phase-space metric H and a real structure K. Its vacua break Sp(2,ℝ) ∋ ρ to {±1}, and K is the order parameter.
  - Because the action is also invariant under K → −K, a twisted combination of ρ with that flip leaves the vacuum invariant. Breaking ρ becomes physical only once a coupling odd in K is present.
- **(II) The self-dual (Ω = 1) Grosse–Wulkenhaar model.** On the matrix base the Langmann–Szabo duality is left multiplication by parity, D f_mn = (−1)^m f_mn.
  - **Complex field:** this is a field symmetry. Once two oscillator levels condense, every classical vacuum breaks it, and the vacuum's position-versus-momentum sharpness varies as cos β along a flat direction.
  - **Real field:** the duality is only a covariance. The two vacua of opposite relative sign are classically degenerate but split at one loop, in favour of the vacuum that is sharper in position.

Where ρ sits inside a continuous U(1) — model I, and model II with complex fields — the polarization is a Goldstone angle. Consequences:

- In complex model II the breaking does not survive quantization: every condensate phase is an exact flat direction, and the condensate is a localized lump with no volume factor.
- In model I, a ρ-preserving potential that reduces the U(1) to a discrete group is needed. Its naive form is unbounded below once H is dynamical. A normalized form is bounded and stable. In the frozen-H reduction it gives an ordered ℤ₂ phase in 1+1 dimensions (Monte Carlo with error bars).

Finally, a section condition built from η confines matter fields to one of η's two null lines (for d = 1) without telling them apart. A coupling built from (H, K) makes interactions local in one and nonlocal in the other — the analogue of Yukawa-generated masses. A mechanism forcing such a coupling is not given.

## 1. Setting and prior work

Phase space ℝ² with symplectic form ω = [[0, 1], [−1, 0]]. ρ = [[0, 1], [−1, 0]] is symplectic and squares to −1. A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK. Its null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing which line is "position".

**Prior work.**

- *The idea.* Freidel, Leigh and Minic make η dynamical and describe spacetime as a choice of Lagrangian [1]. They write "if all probes agree on what we mean by space-time, then we have broken Born duality — there is a preferred choice of polarization" [1c], but give no potential for η and no symmetry-breaking analysis. Freidel, Rudolph and Svoboda suggest the choice "might be subject to a dynamical selection rule" [2]. Born sigma models choose the polarization by gauging [3].
- *Related spontaneous breaking.* Smolin breaks a triality down to Born duality, which stays unbroken [4].
- *An exactly x ↔ p symmetric interacting theory.* Langmann and Szabo found a duality of noncommutative scalar field theory that exchanges positions and momenta, formulated for complex fields [5]. The Grosse–Wulkenhaar model is invariant under it at Ω = 1 [6], with an all-orders vanishing β-function in 4D [7]. A closely related model is exactly solvable [8]. Non-constant vacua at Ω = 1 [9], and minima of the complex self-dual planar model [10], have been studied, but not their behaviour under the duality.
- *Double field theory.* The section condition confines fields to a maximally isotropic subspace. It is imposed for closure of the gauge algebra [11], or derived from string consistency [12]. Those derivations leave the section undetermined within a family — a pair for d = 1, a continuous family for d > 1.
- *Symmetry breaking in low dimension.* Continuous compact symmetries cannot break spontaneously in two dimensions [13, 14]. Non-compact hyperbolic models are an exception [15].

## 2. Model I: a coset sigma model of (H, K)

**Fields** on a 1+1 dimensional base:

- H, a positive symmetric symplectic matrix, H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]] for Z = X + iY in the upper half-plane, with I ≡ ω⁻¹H, I² = −1;
- K, traceless with det K = −1. Its target is the one-sheeted hyperboloid a² + bc = 1, which is two-dimensional de Sitter space.

**Euclidean Lagrangian:**

L = (f_H²/8) Tr(H⁻¹∂H H⁻¹∂H) + (f_K²/4) Tr(H⁻¹ ∂Kᵀ H ∂K) + (λ/8) Tr(H⁻¹ Cᵀ H C), with C = KI + IK.

- The K kinetic term is contracted with H and is positive definite. The naive Tr(∂K ∂K) is indefinite on the hyperboloid (2 db dc at K₀ = diag(1, −1)).
- The potential vanishes exactly when K is compatible with H.

**Symmetries.** Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS, and the action is invariant (checked for generic symplectic S, so for ρ). There is a separate ℤ₂, K → −K.

**Vacua.**

- At H = 1 the vacua are K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]]. The vacuum manifold is the upper half-plane times this circle.
- ρ acts as Z → −1/Z and K(φ) → K(φ + π) = −K(φ). The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}, and O = K₁₁ flips sign under ρ.
- But the twisted element ρ∘(K → −K) maps (1, K₀) to itself. So within the full symmetry group, the vacuum keeps an element that acts on H exactly as ρ does. Breaking ρ is physical only once a coupling odd in K is present (§5).
- The potential's Hessian has rank 1 at the vacuum. That leaves three Goldstone directions: the two non-compact half-plane directions, and the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1).

All checked symbolically (`toy_coset.py`).

## 3. Model II: the self-dual Grosse–Wulkenhaar model

**Matrix base** of the Moyal plane [x₁, x₂] = iθ (θ = 1), as in [9, App. A]:

- f₀₀ = 2e^{−x²/θ}, f_mn = (m! n! θ^{m+n})^{−1/2} ā^{⋆m} ⋆ f₀₀ ⋆ a^{⋆n};
- f_mn ⋆ f_kl = δ_nk f_ml, and H ⋆ f_mn = θ(m + ½) f_mn, f_mn ⋆ H = θ(n + ½) f_mn, with H = ½x².
- The explicit Laguerre form 2(−1)^m √(m!/n!) (√(2/θ))^{n−m} (x₁ + i x₂)^{n−m} L_m^{n−m}(2r²/θ) e^{−r²/θ} (n ≥ m) is checked exactly against the H-eigen-relations, and numerically for orthogonality and ∫ f_mn = 2πθ δ_mn.

**Lemma (the duality on the matrix base).**

- With the two-dimensional form of [6, eq. 1] — p = x̃ = 2θ⁻¹x and normalization π√|det θ| (the cited equation is the 4D form, with π²) — we implement D f(x) = (πθ)⁻¹ ∫ d²y e^{−i x̃·y} f(y) by direct numerical integration.
- **Result:** D f_mn = (−1)^m f_mn for m, n < 4, to ≲ 10⁻¹¹. The opposite sign of the exponent gives (−1)^n.
- The duality is therefore parity acting on the left index for one factor and on the right for the next. That is the alternation of [6], and is consistent with the parity-operator form of Weyl symbols [16]. Grosse and Wulkenhaar already note that the duality is manifest in the matrix base [6b]; we record the explicit form because the rest of the analysis turns on it.
- The Ω = 1 quadratic form ∫ |∂φ|² + x̃²|φ|² equals 8π(m + n + 1)|φ_mn|², diagonal, computed with exact derivatives.

**Complex fields.**

- In units where the kinetic coefficient is 1, S[φ] = Σ_mn (m + n + 1 − μ²)|φ_mn|² + λ Tr((φ†φ)²).
- It satisfies S[UφV†] = S[φ] for all diagonal unitaries U, V. The duality Πφ is the α = π element of e^{−iαN}.
- **Vacua** (μ² = 4, λ = 1):
  - Gradient descent from random starts always reaches a diagonal φ with |φ_mm|² = (1.5, 0.5, 0, …) and S_min = −2.5.
  - The relative phase β of φ₀₀ and φ₁₁ is free. The duality maps β → β + π, so no vacuum is invariant.
- **Polarization:** Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual equals Δ(0) cos β, with Δ(0) > 0. β = 0 is broader in position than in momentum; β = π is its image.

**Real fields.**

- Πφ is not Hermitian, so the duality maps the real field space out of itself. The real action is only covariant: its quartic term is invariant in the alternating form Tr((ψψ†)²), ψ = Πφ.
- The vacua are diag(±√q₀, ±√q₁). Up to the global sign, the two relative signs are classically degenerate (S = −2.5) but have different fluctuation spectra.
- Their one-loop Gaussian free energies differ by F(+) − F(−) = 2.634. The value is the same at truncations N = 6, 8, 10, because the sign-dependent term involves only the modes coupling levels 0 and 1.
- **The preferred vacuum, diag(a₀, −a₁), is the β = π configuration, the one sharper in position.**
- This is explicit, not spontaneous selection, because the real model is not duality-symmetric: its field is real in position. It holds at fixed bare μ², and is not followed through renormalization (§4).

All in `toy_gw.py`.

## 4. Quantum stability

**Model II, complex fields: restoration.**

- Every condensate phase is an exact flat direction, by the U(1)^N × U(1)^N symmetry.
- At fixed μ² the condensate occupies finitely many levels: it is a localized lump, not an extended order. Nothing supplies a volume factor that could suppress fluctuations of β.
- So the quantum measure is uniform in β at every truncation, and ⟨Δ⟩ = 0. The classical breaking of §3 does not survive quantization.
- Two caveats.
  - The bare μ² is itself renormalized. The level-0 tadpole grows as ln N (it is a harmonic sum), so fixed bare μ² is not a consistent large-N limit.
  - Whether a potential on β could be stabilized by the massive tower is argued against, not proven.
- The exact solution of the related model [8] is the natural independent check. We have not carried it out.

**Model I: the ρ-preserving potential.**

- In 1+1 the compact angle φ cannot order: Mermin–Wagner [13, 14] applies to the compact SO(2) containing ρ.
- The non-compact half-plane sector is a hyperbolic model, where symmetry breaking in 2D does occur [15]. Whether ρ's SO(2) stays unbroken in the full coupled model is open.
- To get a definite polarization we add a potential that is invariant under ρ and under K → −K, and reduces the U(1) to a discrete group.
- **The naive choice −μ[Tr(K K_ref)]² is unbounded below once H is dynamical.** Along H = SᵀS, K = S⁻¹K_ref S with S a boost, the compatibility term stays zero while the potential reaches −8.9 × 10⁶ μ at boost parameter 4. The point (1, K_ref) is a saddle (Hessian eigenvalue −6.47 at λ = μ = 1).
- **The normalized form V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK) is bounded**, −μ ≤ V_b ≤ 0 by Cauchy–Schwarz, since Tr K_refᵀK_ref = 2.
  - It is ρ- and flip-invariant.
  - With H dynamical, (1, K_ref) is a stable minimum: Hessian eigenvalues 0, 0.764, 2, 5.236.
  - The zero mode is the classical flat line H = diag(y, 1/y), K = K_ref. It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref. Boosts are penalized.
  - Vacuum manifold: {diag(y, 1/y)} × {±K_ref}.
- At H = 1, V_b = −(μ/2)(1 + cos 2φ).

**Monte Carlo of the frozen-H reduction.**

- We simulate the lattice model E = −J Σ cos(φ_i − φ_j) − h Σ cos 2φ_i: model I's polarization angle at H = 1, with V_b up to a constant and normalization. H is not simulated.
- Checkerboard Metropolis, cold start (φ = 0), L = 16, 32, 64. Means ± standard errors over four independent seeds. Order parameter for ρ: m = ⟨cos φ⟩.

| Run | Values at L = 16, 32, 64 | Reading |
|---|---|---|
| With the potential (J = h = 1), T = 0.6 | ⟨\|m\|⟩ = 0.954 ± 0.0001 at every size; Binder cumulant 0.667 | Ordered ℤ₂ phase |
| Control, T = 3.0 | ⟨\|m\|⟩ = 0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004 | Scales as 1/L: disordered |
| No potential (h = 0), T = 0.6 | ⟨\|M\|⟩ = \|⟨e^{iφ}⟩\| = 0.8369 ± 0.0007, 0.8025 ± 0.0039, 0.7736 ± 0.0038; ratio 0.924 vs spin-wave (64/16)^{−T/4πJ} = 0.936 | No true order |

(`toy_s4.py`.)

- We call the first row an ordered ℤ₂ phase. We did not measure critical exponents. Symmetry-breaking fields in the planar model are treated generally in [17]; the ordered phase at these parameters is established by the simulation itself.
- Hot starts at L = 64 coarsen slowly through metastable domains, so ordered-phase values are reported from cold starts.

## 5. Matter and locality

**What η fixes.**

- The null lines of η = ωK(φ) are exactly K's eigenlines L±, and the only ones.
- K → −K sends η → −η with the same null lines. ρ exchanges L+ and L−.

**The section condition** η^{AB} ∂_A f ∂_B g = 0, η^{AB} ∂_A ∂_B f = 0 (d = 1). In null coordinates it is purely off-diagonal:

- fields on one null line pass; mixed fields fail;
- built from −η, the pairing only changes sign.

So consistency confines matter to one null line without telling the two apart. For d > 1 the analogous statement leaves a continuous family of sections [12].

**A coupling built from (H, K).**

- I[W] = ∫_{L+} du (∫_{L−} dv W)² of a state's Wigner function needs H as well as K: rescaling the coordinate along L+ by 2 doubles it. It is covariant under the SO(2) fixing H = 1, not under Sp(2,ℝ).
- At H = 1, in the vacuum +K_ref it is ∫|ψ(x)|⁴ dx (local in x); in −K_ref it is ∫|ψ̃(p)|⁴ dp.
- For ψ ∝ e^{−(x−1.3)²/0.7} + 0.6 e^{−(x+1.3)²/0.7}, the two vacua give 0.4070 and 0.3600. **I is odd in K**, so it breaks the K → −K symmetry and makes the breaking of ρ physical (§2).
- The combined map (ψ → Fψ, K → −K) leaves I invariant. A K-blind interaction ∫W² shows no asymmetry.

(`toy_s5.py`.) Locality in the selected Lagrangian therefore follows from the vacuum once matter couples this way, as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling.

## 6. Summary and limitations

**Shown** (each by executed code):

- Model I: an explicit Sp(2,ℝ) ∋ ρ symmetric action with η = ωK as order parameter, including the twisted-ρ caveat.
- Model I: the instability of the naive ρ-preserving potential, and a bounded, stable replacement.
- Model I: an ordered ℤ₂ phase in the frozen-H reduction in 1+1.
- Model II: the explicit matrix-base form of the duality.
- Model II: complex fields — classical breaking along a flat polarization angle, and restoration under quantization.
- Model II: real fields — discrete vacua whose classical degeneracy is lifted at one loop in favour of the position-sharp one.
- In model I and complex model II, ρ sits inside a continuous U(1), so the polarization is a Goldstone angle.

**Not shown:**

- a Monte Carlo of model I with H dynamical;
- whether ρ's SO(2) breaks in the coupled model without a potential;
- a derivation of the ρ-preserving potential, which introduces a rigid, unordered pair of axes;
- the large-N, renormalized fate of the real model's one-loop selection;
- a mechanism forcing the (H, K)-coupling of matter;
- anything beyond d = 1.

**Motivation, not result.** In a parent framework the polarization angle is identified with a dark-energy field. The Goldstone structure here is consistent with that, but untested by it.

## References

[1] L. Freidel, R. G. Leigh, D. Minic: (a) "Born reciprocity in string theory and the nature of spacetime," Phys. Lett. B 730, 302 (2014), arXiv:1307.7080; (b) "Quantum gravity, dynamical phase space and string theory," Int. J. Mod. Phys. D 23, 1442006 (2014), arXiv:1405.3949; (c) "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005.
[2] L. Freidel, F. J. Rudolph, D. Svoboda, "Generalised kinematics for double field theory," JHEP 11 (2017) 175, arXiv:1706.07089.
[3] V. E. Marotta, R. J. Szabo, "Born sigma-models for para-Hermitian manifolds and generalized T-duality," Rev. Math. Phys. 33, 2150031 (2021), arXiv:1910.09997.
[4] L. Smolin, "Quantum reference frames and triality," arXiv:2007.05957.
[5] E. Langmann, R. J. Szabo, "Duality in scalar field theory on noncommutative phase spaces," Phys. Lett. B 533, 168 (2002), hep-th/0202039.
[6] H. Grosse, R. Wulkenhaar: (a) "The β-function in duality-covariant noncommutative φ⁴-theory," Eur. Phys. J. C 35, 277 (2004), hep-th/0402093; (b) "Renormalisation of φ⁴-theory on noncommutative ℝ⁴ in the matrix base," Commun. Math. Phys. 256, 305 (2005), hep-th/0401128.
[7] M. Disertori, R. Gurau, J. Magnen, V. Rivasseau, "Vanishing of beta function of non-commutative φ⁴₄ theory to all orders," Phys. Lett. B 649, 95 (2007), hep-th/0612251.
[8] E. Langmann, R. J. Szabo, K. Zarembo, "Exact solution of quantum field theory on noncommutative phase spaces," JHEP 01 (2004) 017, hep-th/0308043.
[9] A. de Goursac, A. Tanasa, J.-C. Wallet, "Vacuum configurations for renormalizable non-commutative scalar models," Eur. Phys. J. C 53, 459 (2008), arXiv:0709.3950.
[10] C. D. Fosco, G. A. Moreno, "One-loop effects in a self-dual planar noncommutative theory," JHEP 11 (2007) 046, arXiv:0710.0818.
[11] C. Hull, B. Zwiebach, "Double field theory," JHEP 09 (2009) 099, arXiv:0904.4664; O. Hohm, C. Hull, B. Zwiebach, "Background independent action for double field theory," JHEP 07 (2010) 016, arXiv:1003.5027.
[12] A. Betz, R. Blumenhagen, D. Lüst, F. Rennecke, "A note on the CFT origin of the strong constraint of DFT," JHEP 05 (2014) 044, arXiv:1402.1686.
[13] N. D. Mermin, H. Wagner, Phys. Rev. Lett. 17, 1133 (1966).
[14] S. Coleman, "There are no Goldstone bosons in two dimensions," Commun. Math. Phys. 31, 259 (1973).
[15] M. Niedermaier, E. Seiler, Ann. Henri Poincaré 6, 1025 (2005), hep-th/0312293; A. Duncan, M. Niedermaier, E. Seiler, "Vacuum orbit and spontaneous symmetry breaking in hyperbolic sigma models," Nucl. Phys. B 720, 235 (2005), erratum Nucl. Phys. B 758, 330 (2006), hep-th/0405163.
[16] A. Royer, "Wigner function as the expectation value of a parity operator," Phys. Rev. A 15, 449 (1977).
[17] J. V. José, L. P. Kadanoff, S. Kirkpatrick, D. R. Nelson, "Renormalization, vortices, and symmetry-breaking perturbations in the two-dimensional planar model," Phys. Rev. B 16, 1217 (1977). (Background on symmetry-breaking fields in the planar model; the ordered phase used here is established by our own Monte Carlo, not by appeal to this reference.)
