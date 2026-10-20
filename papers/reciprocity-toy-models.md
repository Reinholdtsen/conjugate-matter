# Spontaneous Breaking of Born Reciprocity in Two Toy Models: the Polarization as a Goldstone Angle


> **Status (2026-10-20): round-4 review returned verdict B.** The §4 potential is unbounded below once H is dynamical, so the Monte Carlo is a frozen-H reduction; v2 with the accepted revisions is pending. See [review/round4-adjudication.md](../review/round4-adjudication.md).
*Anonymous working manuscript submitted for adversarial review. The manuscript may contain errors or confabulations; the reviewer is asked to find them.*

## Abstract

Born reciprocity, the phase-space map ρ: (x, p) → (p, −x), is an exact symmetry of quantum kinematics but not of observed dynamics, which is local in position. A natural explanation is spontaneous breaking: a ρ-symmetric action whose vacuum selects a Lagrangian polarization, with the neutral metric η = ωK (K a real structure, K² = 1) as order parameter. The idea has been stated before; we found no explicit model. We give two.

- **(I) A coset sigma model** of a phase-space metric H and a real structure K. Here ρ ∈ Sp(2,ℝ) is a symmetry, the vacua break Sp(2,ℝ) to {±1}, and K is the order parameter.
- **(II) The complex Grosse–Wulkenhaar model at its self-dual point Ω = 1.** We compute the Langmann–Szabo duality on the matrix base and find D f_mn = (−1)^m f_mn: left multiplication by parity.
  - It is a field symmetry of the complex model but not of the real one.
  - Once two oscillator levels condense, every classical vacuum breaks it. The vacuum's position-versus-momentum sharpness varies as cos β around a flat direction.

In both models ρ is one element of a continuous U(1), so the polarization is a Goldstone angle rather than a discrete choice. Consequences:

- In model II the breaking does not survive quantization, because the angle is a zero mode with no stiffness.
- In model I in 1+1 dimensions, ρ is spontaneously broken only after a ρ-preserving potential on the angle reduces the U(1) to a discrete group. Monte Carlo then shows an ordered Ising-class phase.
- Matter locality: a section condition built from η confines fields to one of η's two null lines (the eigenlines of K) but cannot tell them apart. A K-covariant coupling makes interactions local in one and nonlocal in the other, in the way a Yukawa coupling makes masses. A mechanism that forces such a coupling is not provided.

## 1. Setting and prior work

Phase space ℝ² with symplectic form ω = [[0, 1], [−1, 0]]. ρ = [[0, 1], [−1, 0]] is symplectic and squares to −1. A real structure K with K² = 1 and Kᵀ ω K = −ω defines a neutral metric η = ωK whose null lines are the two eigenlines L± of K, which are Lagrangian. Choosing K is choosing a polarization: which line is "position".

**Prior work.**

- *The idea.* Freidel, Leigh and Minic make η dynamical and describe spacetime as a choice of Lagrangian [1]. They also write "if all probes agree on what we mean by space-time, then we have broken Born duality — there is a preferred choice of polarization" [1c]. They give no potential for η and no symmetry-breaking analysis. Freidel, Rudolph and Svoboda suggest the choice "might be subject to a dynamical selection rule" [2].
- *An exactly x ↔ p symmetric interacting theory.* Langmann and Szabo found a duality of noncommutative scalar field theory exchanging positions and momenta [3]. Grosse and Wulkenhaar's renormalizable φ⁴ model is invariant under it at Ω = 1 [4], where its β-function vanishes to all orders [5]. Non-constant vacua at Ω = 1 were found by de Goursac, Tanasa and Wallet [6]. Whether they break the duality was not examined there.
- *Double field theory.* Its section condition confines fields to a maximally isotropic subspace. It is imposed for closure of the gauge algebra [7], or derived from string consistency [8]. Each derivation selects a pair of sections, not one.
- *Symmetry breaking in low dimension.* Continuous symmetries cannot break spontaneously in two dimensions [9, 10]. Non-amenable groups are an exception [11].

A literature search (INSPIRE full text and arXiv abstracts) found no explicit action with ρ spontaneously broken and η as order parameter.

## 2. Model I: a coset sigma model of (H, K)

**Fields** on a 1+1 dimensional base:

- H, a positive symmetric symplectic matrix, parametrized by the upper half-plane Z = X + iY via H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]], with I ≡ ω⁻¹H, I² = −1;
- K, a real structure as above. For 2 × 2 matrices this means traceless with det K = −1: the one-sheeted hyperboloid a² + bc = 1, which is two-dimensional de Sitter space.

**Euclidean Lagrangian:**

L = (f_H²/8) Tr(H⁻¹∂H H⁻¹∂H) + (f_K²/4) Tr(H⁻¹ ∂Kᵀ H ∂K) + (λ/8) Tr(H⁻¹ Cᵀ H C), with C = KI + IK.

- The K kinetic term is contracted with H, which makes it positive definite. The naive Tr(∂K ∂K) is indefinite on K's target space (2 db dc at K₀ = diag(1, −1)) and would give a ghost.
- The potential vanishes exactly when K anticommutes with I, i.e. when K is compatible with H.

**Symmetry.** S ∈ Sp(2,ℝ) acts by H → SᵀHS, K → S⁻¹KS. All three terms are invariant for a generic symplectic S, hence for ρ, and also under K → −K.

**Vacua.**

- At H = 1, V = 0 exactly when K is symmetric. Then K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]], a circle.
- The vacuum manifold is the upper half-plane times this circle.
- ρ acts on H as Z → −1/Z (fixed point Z = i) and on K(φ) as K(φ) → K(φ + π) = −K(φ). No vacuum is ρ-invariant.
- The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}. Sp(2,ℝ) is broken to {1, ρ²}.
- The order parameter O = K₁₁ is +1 in (1, K₀) and −1 in its ρ-image.
- The potential's Hessian at the vacuum has rank 1 on the four field directions. That leaves three Goldstone directions: two non-compact (the half-plane) and one compact, the angle φ, which parametrizes the Lagrangian Grassmannian Λ(1).

All statements of this section are verified symbolically (`toy_coset.py`).

## 3. Model II: the self-dual Grosse–Wulkenhaar model

**Matrix base** of the Moyal plane [x₁, x₂] = iθ (θ = 1 below), as in [6, App. A]:

- f₀₀ = 2 e^{−x²/θ} and f_mn = (m! n! θ^{m+n})^{−1/2} ā^{⋆m} ⋆ f₀₀ ⋆ a^{⋆n};
- f_mn ⋆ f_kl = δ_nk f_ml, and H ⋆ f_mn = θ(m + ½) f_mn, f_mn ⋆ H = θ(n + ½) f_mn, with H = ½x².
- We use the explicit Laguerre form 2(−1)^m √(m!/n!) (√(2/θ))^{n−m} (x₁ + i x₂)^{n−m} L_m^{n−m}(2r²/θ) e^{−r²/θ} (n ≥ m). We check it exactly against the two H-eigen-relations for m, n ≤ 2, and numerically for orthogonality and ∫ f_mn = 2πθ δ_mn.

**The duality** [4, eq. 1]:

- φ̂(p) ↔ π√|det θ| φ(x), with p = x̃ = 2θ⁻¹x, where the sign of the Fourier exponent alternates around the ⋆-vertex.
- We implement D f(x) = (πθ)⁻¹ ∫ d²y e^{−i x̃·y} f(y) by direct numerical integration.
- **Result:** D f_mn = (−1)^m f_mn for all m, n < 4, to numerical precision (≲ 10⁻¹¹). The duality is left multiplication by the parity matrix Π = e^{−iπN}.
- The Ω = 1 quadratic form ∫ |∂φ|² + x̃²|φ|² is diagonal in the matrix base and equal to 8π(m + n + 1)|φ_mn|², computed with exact derivatives.

**Real versus complex fields.**

- For a real (Hermitian) φ, Πφ is not Hermitian, and Tr((Πφ)⁴) ≠ Tr φ⁴. The duality maps the real field space out of itself. The real action is duality-*covariant*: its quartic term is invariant in the alternating form Tr((ψψ†)²), ψ = Πφ, which is the alternation of [4].
- For a complex field, S[φ] = Σ_mn (m + n + 1 − μ²)|φ_mn|² + λ Tr((φ†φ)²) (units in which the kinetic coefficient is 1). It satisfies S[Πφ] = S[φ], and more generally S[UφV†] = S[φ] for all diagonal unitaries U, V. **The duality is the α = π element of the continuous left rotations e^{−iαN}.**

**Vacua of the complex model** (μ² = 4, λ = 1; levels 0 and 1 condense):

- Gradient descent from six random starts always ends at a diagonal φ with |φ_mm|² = q_m = max(0, −(2m + 1 − μ²)/(2λ)) = (1.5, 0.5, 0, …), and S_min = −Σ(2m + 1 − μ²)²/(4λ) = −2.5.
- The relative phase β of φ₀₀ and φ₁₁ is free: S is constant around the circle.
- The duality maps β → β + π, so no vacuum is invariant once level 1 condenses.

**Order parameter: the vacuum's polarization.**

- Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual is the second moment of the vacuum profile minus that of its dual (momentum-space) profile.
- Numerically, Δ(β) = Δ(0) cos β with Δ(0) > 0 in our conventions.
  - β = 0: the vacuum is broader in position than in momentum.
  - β = π: its image under the duality, broader in momentum.
  - β = ±π/2: balanced.
- Δ is odd under the duality.

All statements of this section are computed in `toy_gw.py`.

## 4. Quantum stability

**Model II: restoration.**

- β is the orbit of an exact continuous symmetry.
- Because the condensate occupies finitely many levels at fixed μ², nothing couples β across space.
- So the quantum measure is uniform in β at every truncation, and ⟨Δ⟩ = 0 exactly. Increasing the truncation adds only massive levels.
- A potential on β would not help either. The order-parameter sector stays finite-dimensional, so the system tunnels between minima. This last step is argued, not proven: we assume integrating out the massive tower does not make the barrier grow with truncation.
- **The classical breaking of §3 does not survive quantization.**

**Model I in 1+1 dimensions: breaking with a ρ-preserving potential.**

- At H = 1 the polarization field is φ, with XY stiffness (f_K²/2)(∂φ)².
- In the exactly symmetric model the continuous breaking is forbidden [9, 10].
- The potential −μ[Tr(K K_ref)]² = −2μ(1 + cos 2φ) is invariant under ρ (φ → φ + π). It reduces the U(1) to a discrete group, leaving two vacua K = ±K_ref exchanged by ρ. This is the two-fold anisotropic planar model, whose ordered phase is Ising-like [12].
- We simulate the lattice version E = −J Σ cos(φ_i − φ_j) − h Σ cos 2φ_i with checkerboard Metropolis, fixed seeds, and L = 16, 32, 64. The order parameter for ρ is m = ⟨cos φ⟩.

| Run | ⟨\|m\|⟩ or ⟨\|M\|⟩ at L = 16, 32, 64 | Reading |
|---|---|---|
| With the potential (J = h = 1), T = 0.6 | ⟨\|m\|⟩ = 0.954 at all three sizes; Binder cumulant 0.667 | Ordered |
| Control, T = 3.0 | ⟨\|m\|⟩ = 0.078 → 0.033 → 0.014 | Disordered |
| Exactly symmetric (h = 0), T = 0.6 | ⟨\|M\|⟩ = \|⟨e^{iφ}⟩\| = 0.838 → 0.798 → 0.776, ratio 0.925 vs. spin-wave estimate (64/16)^{−T/4πJ} = 0.936 | No true order |

(`toy_s4.py`.) In three or more dimensions the continuous breaking is allowed. There the angle is a massless Goldstone mode unless a potential is added.

## 5. Matter and locality

**What η fixes.**

- The null lines of η = ωK(φ) are exactly K's eigenlines L±, for every φ, and they are the only ones.
- K → −K sends η → −η with the same null lines. ρ exchanges L+ and L−.

**The section condition** η^{AB} ∂_A f ∂_B g = 0, η^{AB} ∂_A ∂_B f = 0. In null coordinates (u, v) it is purely off-diagonal:

- fields on one null line pass, F(u) and G(u), or likewise in v;
- mixed fields fail, since η(dF(u), dG(v)) = −F′G′, and F(u) + G(v) fails against itself;
- built from −η, the pairing only changes sign.

So consistency confines matter to a single Lagrangian null line but cannot say which one. This agrees with the double-field-theory literature, where every derivation selects the pair [8].

**A K-covariant coupling** (the weak form of locality).

- For a state with Wigner function W, define I_K[W] = ∫_{L+} du (∫_{L−} dv W)².
- In the vacuum +K_ref (L+ the x-axis) this is ∫|ψ(x)|⁴ dx, an interaction local in x and independent of p. In −K_ref it is ∫|ψ̃(p)|⁴ dp.
- For the test state ψ ∝ e^{−(x−1.3)²/0.7} + 0.6 e^{−(x+1.3)²/0.7}, the two vacua give 0.4070 and 0.3600.
- The combined map (ψ → Fψ, K → −K) leaves I invariant.
- A K-blind phase-space interaction ∫W² (= 1/2π for pure states) shows no asymmetry.

(`toy_s5.py`.) So locality in the selected Lagrangian follows from the vacuum value of K once matter couples to K this way, just as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces matter to couple through K rather than in a K-blind way.

## 6. Summary and limitations

**Established here** (each by executed code):

- an explicit action (model I) with ρ as a symmetry, a vacuum manifold on which ρ acts without fixed points, and η = ωK as order parameter;
- the matrix-base form of the Langmann–Szabo duality, D f_mn = (−1)^m f_mn;
- the distinction between the real model (covariant only) and the complex model (symmetric);
- classical breaking of the duality by the self-dual complex vacua, with a cos β polarization;
- the structural fact that in both models ρ sits inside a continuous U(1), so the polarization is a Goldstone angle;
- quantum restoration in model II;
- Ising-class breaking of ρ in model I in 1+1, once a ρ-preserving potential is added.

**Not established:**

- a mechanism that forces matter to couple to the order parameter (only the weak, Yukawa-like form of locality is shown);
- a derivation of the ρ-preserving potential, which introduces a rigid unordered pair of axes;
- the tunnelling step in model II's restoration argument, which is argued, not proven;
- anything beyond d = 1 (two-dimensional phase space).

**Motivation, not result.** In a parent framework the polarization angle is identified with a dark-energy field. The Goldstone structure found here is consistent with that, but nothing in this note tests it.

## References

[1] L. Freidel, R. G. Leigh, D. Minic: (a) "Born reciprocity in string theory and the nature of spacetime," Phys. Lett. B 730, 302 (2014), arXiv:1307.7080; (b) "Quantum gravity, dynamical phase space and string theory," Int. J. Mod. Phys. D 23, 1442006 (2014), arXiv:1405.3949; (c) "Metastring theory and modular space-time," JHEP 06 (2015) 006, arXiv:1502.08005.
[2] L. Freidel, F. J. Rudolph, D. Svoboda, "Generalised kinematics for double field theory," JHEP 11 (2017) 175, arXiv:1706.07089.
[3] E. Langmann, R. J. Szabo, "Duality in scalar field theory on noncommutative phase spaces," Phys. Lett. B 533, 168 (2002), hep-th/0202039.
[4] H. Grosse, R. Wulkenhaar, "The β-function in duality-covariant noncommutative φ⁴-theory," Eur. Phys. J. C 35, 277 (2004), hep-th/0402093; "Renormalisation of φ⁴-theory on noncommutative ℝ⁴ in the matrix base," Commun. Math. Phys. 256, 305 (2005), hep-th/0401128.
[5] M. Disertori, R. Gurau, J. Magnen, V. Rivasseau, "Vanishing of beta function of non-commutative φ⁴₄ theory to all orders," Phys. Lett. B 649, 95 (2007), hep-th/0612251.
[6] A. de Goursac, A. Tanasa, J.-C. Wallet, "Vacuum configurations for renormalizable non-commutative scalar models," Eur. Phys. J. C 53, 459 (2008), arXiv:0709.3950.
[7] C. Hull, B. Zwiebach, "Double field theory," JHEP 09 (2009) 099, arXiv:0904.4664; O. Hohm, C. Hull, B. Zwiebach, "Background independent action for double field theory," JHEP 07 (2010) 016, arXiv:1003.5027.
[8] A. Betz, R. Blumenhagen, D. Lüst, F. Rennecke, "A note on the CFT origin of the strong constraint of DFT," JHEP 05 (2014) 044, arXiv:1402.1686.
[9] N. D. Mermin, H. Wagner, Phys. Rev. Lett. 17, 1133 (1966).
[10] S. Coleman, "There are no Goldstone bosons in two dimensions," Commun. Math. Phys. 31, 259 (1973).
[11] M. Niedermaier, E. Seiler, Ann. Henri Poincaré 6, 1025 (2005), hep-th/0312293; N. Duncan, M. Niedermaier, E. Seiler, Nucl. Phys. B 720, 235 (2005), hep-th/0405163.
[12] J. V. José, L. P. Kadanoff, S. Kirkpatrick, D. R. Nelson, "Renormalization, vortices, and symmetry-breaking perturbations in the two-dimensional planar model," Phys. Rev. B 16, 1217 (1977).
