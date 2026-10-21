---
title: "Notation"
weight: 140
status: record
description: "The symbols used across the program's documents: what each means, where it is defined and which wiki page explains it; the symbols that carry several meanings (ρ, ω, τ, μ, H, K, f, Λ and others); and the conventions the wiki follows."
sources:
  - "papers/broken-born-checkpoint-v2.md §3–§14"
  - "papers/reciprocity-toy-models.md §1–§5"
  - "papers/conjugate-special-relativity.md §1–§5"
  - "notes/broken-born-theory.md §1–§8"
  - "notes/debt1a-geometric-core.md §A–§E"
  - "notes/debt1a-ii-X-classification.md §1–§4"
  - "notes/debt1a-iii-tuning-test.md §2–§4"
  - "notes/debt1a-iv-beta-coefficients.md §1–§3"
  - "notes/debt3a-stream-stability.md Setup, Limit 2, Corollary"
  - "notes/debt3b-wave-island.md The rate, Scenario A, Scenario B"
  - "notes/debt3c-ufd-endpoint.md Sharpened input numbers, The attractive endpoint"
  - "notes/knot-dark-matter-standalone.md §2–§4"
  - "notes/toy-lagrangian.md Chunk 2, S5"
  - "review/v3-worklog.md R7, F2, O1"
  - "review/round3/referee/audit-notes.md Steps 2–4"
  - "review/round3/referee/step2a.py constants"
  - "review/round3/referee/step2b.py docstring"
  - "review/round4/referee/audit-notes.md Steps 2–3"
  - "review/round4-adjudication.md F1–F2"
  - "HANDOFF.md §3–§5"
  - "verify/toy_coset.py K0, Kref"
  - "verify/toy_gw.py Pi"
---

*This page lists the mathematical symbols in the Broken-Born program's documents, each with its meaning, the document that defines it and the wiki page that explains it. The program's central objects keep one meaning throughout the current documents: the reciprocity map ρ, the symplectic form ω, the neutral metric η, the generalized metric H, the modular field Z and the dark-energy field τ. Many other letters are reused from one document to the next. The letter μ, for example, is a width in momentum in the dark-matter sector and a coupling constant in the toy models. Those reuses are gathered in the Collisions section near the end.*

**Status:** Record. A register compiled from the documents; it adds no results and carries no provenance tags of its own. Each entry names the document that defines the symbol, and where an entry and its document differ, the document governs.

## Key facts

- **Documents.** References such as "#11 §5" use the artifact numbers of `HANDOFF.md` §3: #1 is the lab notebook, #2–#4 the Debt-3 calc notes, #5–#8 the Debt-1 calc notes, #11 the checkpoint, #13 conjugate special relativity and #14 the withdrawn soliton manuscript. "The toy note" is `papers/reciprocity-toy-models.md` and "the worklog" its working record `notes/toy-lagrangian.md`. [Documents](/wiki/history/documents) maps every number to its file.
- **Writing.** The wiki writes mathematics in Unicode as the checkpoint does: H = diag(g, g⁻¹), Z → −Z⁻¹, βₙ = β₄₋ₙ, w ≥ −1. Display equations go in `text` blocks. The lab notebook, the calc notes and #13 write their formulas in LaTeX; the wiki transcribes them.
- **The three products of the structures.** With ω and η in standard form, #11 §5 defines three products of ω, η and H that obey a split-quaternion algebra. The lab notebook (#1 §2) uses the same definitions. See [The structures ω, η, H and the split-quaternion algebra](/wiki/phase-space/born-geometry/born-structures).

  ```text
  I = ω⁻¹H,   J = η⁻¹H,   K = η⁻¹ω        I² = −1,   J² = K² = +1,   IJ = K
  ```

- **"The real structure" is named two ways.** #11's postulate P2′ builds the order parameter from H and J, "with the real structure J chosen spontaneously". The toy note and #11 §14 item 11 build it from ω and K, with K the real structure. No document reconciles the two namings.

  ```text
  η = HJ     #11 §4, postulate P2′ (J the real structure)
  η = ωK     toy note §1; #11 §14 item 11 (K the real structure)
  ```

  The wiki quotes each formula with its source and does not choose between them; [The order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter) sets the versions side by side.
- **Reused letters.** Where a page uses a symbol that has several meanings (ρ as a density, H as the Hubble rate, μ as a coupling), it names the meaning in words at first use.
- **GW** on the wiki means Grosse–Wulkenhaar, the second toy model. Some documents use the same letters for gravitational waves (#1 §9, #11 §7.5, `review/round3-adjudication.md` ruling 5); the wiki always writes gravitational waves out.
- **†** marks a reference cited from model memory. The toy note also writes † for the Hermitian adjoint inside formulas (φ†φ, UφV†). Outside a formula, † on the wiki is always the citation mark; see [Provenance tags and citation marks](/wiki/method/provenance-tags).
- Terms in words are on the [Glossary](/wiki/glossary), and works cited on [References](/wiki/references).

## Phase space and Born geometry

- **ρ** — Born reciprocity, the Born rotation (x, p) → (p, −x). As a matrix it is [[0, 1], [−1, 0]], symplectic, and squares to −1 (toy note §1). On the modular field it acts as Z → −Z⁻¹. — #11 §3, §6; toy note §1 — [Born reciprocity ρ](/wiki/phase-space/reciprocity/born-reciprocity)
- **ρ²** — the phase-space parity (x, p) → (−x, −p), which preserves ω, η and H. In the lab notebook the vacuum keeps the residual group ℤ₂ = {1, ρ²} of the ℤ₄ that ρ generates; that breaking pattern, ℤ₄ → ℤ₂, is superseded by the Goldstone picture. — #1 §2 — [The order parameter](/wiki/symmetry-breaking/order-parameter)
- **R** — the matrix [[0, 1], [−1, 0]] by which ρ acts on tangent vectors in #1; it preserves ω and H and flips the sign of η. — #1 §2 — [The structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)
- **ρ∘(K → −K)** — the twisted element: ρ combined with the flip K → −K. It maps model I's vacuum (1, K₀) to itself. — toy note §2 — [The twisted element](/wiki/symmetry-breaking/twisted-element)
- **[x, p] = iℏ** — the canonical commutator; #11 §3 reads it as ruling out joint locality in x and p. — #11 §3 — [The canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator)
- **ℏ** — Planck's constant; its constancy is read as the rigidity of ω ("symplectic rigidity ≡ constancy of ℏ"). — #11 §4 — [The symplectic form](/wiki/phase-space/reciprocity/symplectic-form)
- **d** — the number of position coordinates: d = 4 physically, d = 1 in the toy models. — #1 §2; toy note §1 — [Phase-space geometry](/wiki/phase-space)
- **ω** — the symplectic form, [[0, 1], [−1, 0]] in d × d blocks; rigid under P2′. — #11 §4; #1 §2; toy note §1 — [The symplectic form and Sp(2d, ℝ)](/wiki/phase-space/reciprocity/symplectic-form)
- **Sp(2d, ℝ)** — the group of linear maps that preserve ω; Sp(2, ℝ) in the toy models, where it contains ρ. — #11 §1, §6; toy note §2 — [The symplectic form and Sp(2d, ℝ)](/wiki/phase-space/reciprocity/symplectic-form)
- **η** — the neutral (split-signature) metric, [[0, 1], [1, 0]] in the standard frame. Under P2′ it is emergent and serves as the order parameter. — #1 §1–§2; #11 §4 — [The structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)
- **H** — the positive generalized (phase-space) metric of postulate P1. — #11 §4 — [P1: the phase-space arena](/wiki/program/postulates/p1-arena)
- **I** — I = ω⁻¹H, a complex structure (I² = −1); P3 makes the action invariant under the Born rotation it generates. — #11 §4–§5 — [P3: a reciprocity-invariant action](/wiki/program/postulates/p3-reciprocity)
- **J** — J = η⁻¹H, a real structure (J² = +1). In #1 it is the order parameter ("Reciprocity is broken iff ⟨J⟩ ≠ 0 in the vacuum"); in #11's P2′ the vacuum chooses it, and η is built from H and J (Key facts). — #11 §4–§5; #1 §2 — [The order parameter](/wiki/symmetry-breaking/order-parameter)
- **K** — K = η⁻¹ω (K² = +1). In the toy note K is a real structure with Kᵀ ω K = −ω that defines η = ωK; in model I it is traceless with det K = −1. — #11 §5; toy note §1–§2 — [The order parameter](/wiki/symmetry-breaking/order-parameter)
- **L±; L, L̃** — the two eigenlines of K, which are η's null lines and are Lagrangian; ρ exchanges them. The worklog writes them L and L̃, following Freidel–Leigh–Minic: L = ker(η + ω), L̃ = ker(η − ω). — toy note §1, §5; `notes/toy-lagrangian.md` — [The section condition](/wiki/symmetry-breaking/section-condition)
- **g** — the spacetime metric; Im Z = g. — #11 §6 — [The modular field Z](/wiki/phase-space/modular-field/modular-field-z)
- **g̃** — the momentum-space metric; slaved to g̃ = g⁻¹ when ω and η are both rigid. — #5 §A; #11 §5 — [Corollaries of the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-corollaries)
- **diag(g, g⁻¹); Sym⁺(d)** — the only positive H compatible with both rigid ω and rigid η; Sym⁺(d) is the set of positive symmetric d × d matrices g. — #11 §5 — [The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)
- **A, B, C** — the blocks of H = [[A, C], [Cᵀ, B]] in the proof of the compatibility theorem. — #5 §A; #11 §5 — [The compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem)
- **R_B[H]** — the curvature of the Born connection. — #1 §2 — [The Born connection](/wiki/phase-space/born-geometry/born-connection)
- **U(1, d−1)** — the stabilizer when g has Lorentzian signature (written U(1,3) in #9). — #6 §3; #9 §10 — [Open: Lorentzian dressing of the Euclidean skeleton](/wiki/phase-space/born-geometry/lorentzian-dressing)

## The modular field and the dark-energy field

- **Z = X + iY** — the modular field: a complex symmetric matrix with Y > 0, the coordinate on the Siegel domain Sp(2d, ℝ)/U(d). — #5 §C; #11 §6 — [The modular field Z = X + iY](/wiki/phase-space/modular-field/modular-field-z)
- **H_Z** — the generalized metric in Siegel form, [[Y + XY⁻¹X, XY⁻¹], [Y⁻¹X, Y⁻¹]]. For d = 1 the toy note writes H(Z) = [[Y + X²/Y, X/Y], [X/Y, 1/Y]]. — #5 §C; toy note §2 — [The Siegel domain](/wiki/phase-space/modular-field/siegel-domain)
- **X** — Re Z, the momentum graviton. — #5 §C; #11 §6 — [The momentum graviton X](/wiki/gravity/momentum-graviton)
- **Y** — Im Z, equal to the metric g. — #5 §C — [The modular field Z](/wiki/phase-space/modular-field/modular-field-z)
- **⟨Z⟩ = i·g** — the vacuum, which sits at X = 0. — #6 §3 — [The modular field Z](/wiki/phase-space/modular-field/modular-field-z)
- **Z → −Z⁻¹; Z = i; |Z| = 1** — ρ acting as Möbius inversion; its fixed point, the self-dual point; and the self-dual circle, which is the cosmological constraint a·ã = 1. — #5 §C; #11 §6 — [Reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)
- **Z → Z + B** — the shift symmetry (B symmetric) contained in the rigid Sp(2d, ℝ). — #6 §1; #11 §7.1 — [Shift symmetry](/wiki/gravity/momentum-graviton/shift-symmetry)
- **I[Z]** — the complex structure on the Siegel family; battery test T2 checks I[Z]² = −1. — #7 §2; #11 §6 — [The Siegel domain](/wiki/phase-space/modular-field/siegel-domain); [The verification battery T1–T7](/wiki/method/verification/battery)
- **Λ(d)** — the Lagrangian Grassmannian U(d)/O(d): compact, of dimension d(d+1)/2 = 10 for d = 4, and the Shilov boundary of the Siegel domain. Λ(4) is the physical case; Λ(1) is the circle that model I's compact Goldstone angle parametrizes. — #1 §2; #11 §6; toy note §2 — [The Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian)
- **π₁(U(d)/O(d)) = ℤ** — the fundamental group of Λ(d), generated by the Maslov circle. — #1 §2; #11 §6 — [The Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian)
- **σ-modes** — the ten moduli of Λ(d): τ plus nine others, which #1 §2 assumes heavy [P] and #5 expects inverse-Higgs constraints to eliminate in part [O]. — #5 §D; #1 §2 — [Open: field content of the broken vacuum](/wiki/phase-space/modular-field/field-content)
- **τ** — the dark-energy field: the Maslov phase τ ≡ f·arg det² of the boundary variable, periodic with period 2πf. — #1 §2; #11 §6 — [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase)
- **f, τᵢ, V₀** — τ's period scale, its initial value and the amplitude of its potential. — #1 §2–§3, §7 — [The dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)
- **V(τ) = V₀[1 + cos(τ/f)]** — τ's potential. As written it cannot be negative for V₀ > 0, yet the same documents need V < 0 for the turnaround (#1 §7: "A cosine potential is negative over half its range"); no document resolves the conflict. — #1 §3; #11 §10 — [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence); [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)
- **θ_pol** — the vacuum tilt angle in the lab notebook's sketch Ω_χ/Ω_x^(0) ~ tan²θ_pol. — #1 §8 — [Open: polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis)

## Gravity and the bimetric potential

- **h** — the metric perturbation, Y = 1 + h. — #7 §2 — [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures)
- **λ_μ; δX_μν = ∂₍μλ_ν₎** — the dual-diffeomorphism parameters and the gauge transformation they generate on X. — #6 §2; #11 §7.1 — [Dual diffeomorphisms](/wiki/gravity/momentum-graviton/dual-diffeomorphisms)
- **π_μ** — the four would-be Goldstones of the broken dual diffeomorphisms, eaten by X. — #6 §3; #8 §3 — [The gravitational Higgs mechanism](/wiki/gravity/momentum-graviton/gravitational-higgs)
- **M_X** — the mass of X, "the polarization-breaking scale"; M_X ∝ 2(β₁ + β₂). — #6 §3; #11 §7.1, §7.5 — [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)
- **J₀** — the vacuum polarization [[0, 1], [1, 0]] used in the tuning test. — #7 §2 — [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential)
- **{J, I[Z]} = [[S, A], [A, S]]** — the anticommutator that measures misalignment between J and Z, with S = Y + XY⁻¹X − Y⁻¹ and A = [X, Y⁻¹]. — #7 §2; #11 §7.2 — [The misalignment potential](/wiki/gravity/tuning-test/misalignment-potential)
- **E; E₀[J]** — the symplectic vielbein, with H = EᵀE, and the polarization frame. — #7 §3; #11 §7.2 — [The frame tier](/wiki/gravity/tuning-test/frame-tier)
- **e, f** — the two frames of the bimetric sector, with f = E₀[J]. — #8 §1 — [Vielbein formulation and wedge potentials](/wiki/gravity/spin-2-fields/vielbein-formulation)
- **𝕏 = √(g⁻¹f)** — the frame ratio in the bimetric potential. — #8 §1 — [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)
- **βₙ (n = 0…4)** — the coefficients of the potential V = 2m²M² Σₙ₌₀⁴ βₙ eₙ(𝕏). — #8 §1 — [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)
- **Sₙ(g, f) = S₄₋ₙ(f, g)** — the exchange identity of the potential's terms. — #8 §1 — [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric)
- **eₙ; p₄** — the elementary symmetric polynomials of the eigenvalues of √(g⁻¹f), and the fourth power sum of the same eigenvalues (battery test T7). — #7 §2; #8 §1 — [Elementary symmetric polynomials](/wiki/gravity/spin-2-fields/elementary-symmetric-polynomials); [The verification battery T1–T7](/wiki/method/verification/battery)
- **βₙ = β₄₋ₙ** — the palindrome: β₀ = β₄, β₁ = β₃, β₂ free. — #8 §1; #11 §7.3 — [The palindrome](/wiki/gravity/palindromic-branch/palindrome)
- **T; V(1)** — the tadpole combination T = β₁ + 3β₂ + 3β₃ + β₄, and the potential at the aligned point 𝕏 = 1. Under the palindrome V(1) = 2T. — #8 §2; #11 §7.3 — [The vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)
- **Λ_wedge** — the vacuum energy of the wedge sector. — `HANDOFF.md` §3 — [The vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity)
- **m_FP²; m_g** — the Fierz–Pauli mass combination, m_FP² ∝ β₁ + 2β₂ + β₃ = 2(β₁+β₂), and the graviton mass. — #8 §3; #7 §4 — [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity); [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton)
- **α (partially massless point)** — the parameter in the partially-massless point β₀ = 3α⁻²β₂, β₁ = β₃ = 0, β₄ = 3α²β₂; at α = 1 the point lies inside the palindromic branch. — #11 §7.4 — [Partially massless gravity](/wiki/gravity/spin-2-fields/partially-massless-gravity)
- **M_f, M_g** — the Planck masses of the two metrics. — `review/v3-worklog.md` R7 — [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)
- **S = S_H + S_τ + S_x + S_p + S_mix; M_B** — the lab notebook's action and its parts, with S_H = ½M_B²∫√|H| R_B[H] over the section and M_B the Born mass scale. — #1 §3 — [The geometric action S_H and the v0.1 action (superseded)](/wiki/gravity/tuning-test/geometric-action)

## Cosmology

- **a, ã** — our scale factor and the conjugate one, with a·ã = 1. — #1 §6; #11 §10 — [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint)
- **N (lapse); H (Hubble rate)** — the one lapse shared by the two frames in #1's minisuperspace, and the Hubble rate. — #1 §6 — [Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)
- **M̃; k̃** — the dual Planck mass and the dual curvature parameter, the optional geometric parameters of #1's count. — #1 §6, §10 — [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step)
- **G; G_eff** — Newton's constant, and the effective gravitational coupling, which the dual Einstein term changes by an a⁻⁶ step at early times. — #1 §6; #11 §10 — [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step)
- **w, w̃, w_eff** — the equation of state of a fluid in our frame, of a fluid in the dual frame, and the effective value the dual fluid contributes to ours: w_eff = −w̃, superseding the earlier −2 − w̃. — #1 §6; #11 §10 — [The duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary); [Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)
- **w₀, wₐ** — the Chevallier–Polarski–Linder (CPL) parameters of the dark-energy equation of state; the thawing corridor is wₐ ≈ −1.5(1 + w₀). — #1 §7; #11 §10 — [Quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence)
- **t_turn** — the time of the turnaround. — #1 §7 — [The dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)
- **z** — redshift. The Dark Energy Spectroscopic Instrument's second data release (DESI DR2) favors a phantom crossing above z ≃ 0.4 in #11's quotation (z ≈ 0.4 in `CLAUDE.md`). — #11 §10 — [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)
- **Ω_DE, Ω_b, Ω_χ, Ω_x^(0), Ω_DM** — density fractions of dark energy, baryons, conjugate matter, x-polarized matter before baryogenesis, and dark matter. The abundance question is Ω_χ : Ω_b = 5.4 : 1. — #1 §7–§8; #11 §14 — [Open: polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis)
- **N_eff; ΔN_eff** — the effective number of relativistic species and its excess. The round-3 referee used N_eff,SM = 3.044 (Bennett et al. 2021) or 3.046 (Planck's value) for the Standard Model value. — #1 §6; #14 §4; `review/round3/referee/step2a.py` — [The radiation era](/wiki/cosmology/early-universe/radiation-era)
- **D_x, D_p, N** — the universe's spatial and momentum diameters and its photon count, in the chat-only relation D_x·D_p = h·N^{1/3} per dimension. — `HANDOFF.md` §4 — [The phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter)

## Conjugate matter, the gate and momentum clumping

- **χ** — conjugate (p-polarized) matter, a complex scalar or Dirac fermion. — #1 §3; #11 §8 — [Conjugate matter and the velocity gate](/wiki/dark-matter/conjugate-matter)
- **m_χ, m_φ, α̃** — the χ mass, the mediator mass and the gate coupling. — #1 §3 — [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)
- **M(k, q)** — the nonrelativistic self-interaction amplitude, 4πα̃m_χ/(q² + m_φ²)·F(k²/μ²). — #11 §8 — [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)
- **k; q** — the incoming relative momentum k = m_χv_rel/2, which is the gate variable, and the momentum transfer. — #1 §3 — [The velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate)
- **F(k²/μ²)** — the gate form factor, whose shape (Gaussian or rational) is open. — #11 §8 — [Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)
- **μ** — the gate width in momentum, identified as the χ quantum's intrinsic momentum-fiber width; #13 reads it as μ ~ ℏ/λ_χ. — #11 §8; #6 §4; #13 §4 — [The gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism)
- **T̃** — the dual stress, built from momentum derivatives of the χ bilinear; X couples to it. — #5 §E — [Dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress)
- **σ_T(v); σ₀** — the transfer cross-section, σ_T(v) = σ₀F(v²/v*²), and its low-velocity value. — #11 §8 — [The gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)
- **v\*** — the knee velocity, the gate scale in relative velocity. #1 §5.1 defines v* ≡ √2μ/m_χ and #13 §4 repeats it; #11 does not restate the relation. — #11 §8; #1 §5.1 — [Row 1: the knee in σ_T(v)](/wiki/predictions/self-interaction-knee)
- **σ** — the velocity dispersion of a halo. — #2 — [The gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)
- **g; G** — the gated contact coupling g ≡ 4πα̃/m_φ² = √(πσ₀/m²), and the Gaussian gate G, with G(0) = 1. — #2 — [The gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)
- **ε(p; f); ε_int, ε_gate** — a particle's energy including the gated mean field, and the interaction energies compared with kinetic energy in the stability criterion. — #1 §5.2; #2 — [The gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model)
- **n_gate** — the density of co-movers, the particles within the gate: n_gate ≈ n(v*/σ)³/(2π)^{3/2}. — #2 — [The mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)
- **S ≡ σ₀/m; m_crit** — the cross-section per mass held fixed in the classicality argument, and the classicality threshold m_crit ≈ 10⁻¹³ GeV ~ 0.1 meV for Milky Way conditions. — #2 — [The classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem)
- **N_occ; λ_dB** — the occupation number N_occ = nλ_dB³ = ρ/(m⁴σ³) and the de Broglie wavelength. — #2; #3 — [Occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number)
- **Γ_self; c** — the gated wave-kinetic condensation rate, Γ_self ≈ c·g²ρ²min(σ, v*)⁴/(m³σ⁶) (written Γ_cond in #2), with coefficient c = O(5–15). — #3; #11 §9 — [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate)
- **Γ_gr** — the gravitational condensation rate, which always runs. — #3 — [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate)
- **Ω; t_dyn, t_age** — the orbital stirring rate Ω = 1/t_dyn, the dynamical time and the age of a system. — #3 — [The gated condensation rate Γ_self](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate)
- **R_X; κ** — the stream-to-stirring ratio Γ_self(X)/Ω_X in an environment X, and the Scenario-A normalization Γ_self(dwarf)·t_age = κ. — #3 — [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)
- **X (mean-field parameter)** — X ≡ gn/(mσ²), the mean-field parameter of #2, used in Scenario B. — #3 — [Scenario B: tunable streams](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b)
- **M_crit; M_core; τ_cond; R** — the critical mass of an attractive condensate, an ultra-faint dwarf's core mass, the condensation time τ_cond = t_dyn/R, and Segue 1's rate ratio R. — #3; #4; #11 §9 — [Attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates); [Obituary: Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)
- **γ** — the growth rate of the stream instability that #1 left to be computed. — #1 §5.2 — [Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)
- **χᵢ** — the initial field amplitude that sets the relic abundance by misalignment. — #3 — [Relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)

## Electric–magnetic duality

- **⟨q, q′⟩ = e₁g₂ − e₂g₁ ∈ 2πℤ** — the Dirac–Schwinger–Zwanziger (DSZ) pairing of two charges, each with an electric part e and a magnetic part g; an antisymmetric integer form, so the charge lattice is a symplectic space. — #11 §11.3 — [Dirac quantization and the DSZ pairing](/wiki/electric-magnetic-duality/monopoles/dirac-quantization); [The symplectic charge lattice](/wiki/electric-magnetic-duality/symplectic-charge-lattice)
- **e, g; e·g ~ 2π** — electric and magnetic charge, and Dirac's condition, which pins the magnetic coupling near 4π/e² ≈ 34. — #11 §11.2 — [The magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family)
- **τ_c** — the complexified gauge coupling, on which S-duality acts as τ_c → −1/τ_c. — #11 §11.3 — [S-duality and Montonen–Olive](/wiki/electric-magnetic-duality/s-duality)

## Conjugate special relativity

- **λ; ε** — the Born length and its conjugate momentum scale ε = ℏ/λ; at the Planck value λ² = ℏG/c³. — #13 §1 — [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force)
- **c̃** — the invariant speed of the momentum polarization, a maximum force: c̃ = ℏc/λ² = c⁴/G. — #13 §1 — [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force)
- **ds̃²; F; γ̃; φ** — the dual interval ds̃² = c̃²dt² − dp², the dual boost parameter F (a force), the dual Lorentz factor γ̃ = (1 − F²/c̃²)^{−1/2}, and the dual rapidity, with F = c̃ tanh φ. — #13 §2 — [Force boosts and force composition](/wiki/conjugate-relativity/force-boosts)
- **F₁ ⊕ F₂** — force composition, (F₁ + F₂)/(1 + F₁F₂/c̃²). — #13 §2 — [Force boosts and force composition](/wiki/conjugate-relativity/force-boosts)
- **τ̃** — the dual proper time, dτ̃ = dt√(1 − F²/c̃²). — #13 §3 — [Force dilation](/wiki/conjugate-relativity/force-dilation)
- **λ_χ** — the invariant length of a conjugate quantum, on the shell x_μx^μ = λ_χ². — #13 §4 — [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell)
- **l_P; E_Planck** — the Planck length and the Planck energy; the dual rest-energy relation E = λc̃ gives E_Planck at λ = l_P. — #13 §4 — [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell)

## Toy models

Model I is the coset sigma model of (H, K); model II is the self-dual Grosse–Wulkenhaar (GW) model.

- **f_H, f_K, λ** — the couplings in model I's Euclidean Lagrangian, L = (f_H²/8) Tr(H⁻¹∂H H⁻¹∂H) + (f_K²/4) Tr(H⁻¹ ∂Kᵀ H ∂K) + (λ/8) Tr(H⁻¹ Cᵀ H C). — toy note §2 — [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)
- **C** — the combination of K and I in model I's potential term (λ/8) Tr(H⁻¹ Cᵀ H C), displayed below; the potential vanishes exactly when K is compatible with H. — toy note §2 — [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)

  ```text
  C = KI + IK
  ```

- **S** — an element of Sp(2, ℝ), acting as H → SᵀHS, K → S⁻¹KS. — toy note §2 — [Model I: action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries)
- **K(φ); φ** — the circle of model I vacua at H = 1, K(φ) = [[cos φ, sin φ], [sin φ, −cos φ]], and the polarization angle φ. — toy note §2 — [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)
- **K₀; K_ref** — a reference vacuum (toy note §2) and the reference axes of the ρ-preserving potential (§4); `verify/toy_coset.py` sets both to diag(1, −1). — toy note §2, §4 — [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua); [The toy-model scripts](/wiki/method/verification/toy-model-scripts)
- **O = K₁₁** — model I's order parameter, which flips sign under ρ. — toy note §2 — [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)
- **μ; V_μ; V_b** — the coupling of the ρ-preserving potential; the naive potential −μ[Tr(K K_ref)]² (V_μ in the round-4 records), unbounded below once H is dynamical; and the bounded form V_b = −μ[Tr(K K_ref)]²/(2 Tr KᵀK) (V′ in the round-4 referee's notes). — toy note §4; `review/round4-adjudication.md` F1–F2 — [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential); [The bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)
- **V_λ** — the compatibility term of model I's potential, written λV_λ + V_μ in the round-4 records. — `review/round4-adjudication.md` F2 — [Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential)
- **E, J, h, T, L** — the frozen-H lattice model E = −J Σ cos(φ_i − φ_j) − h Σ cos 2φ_i, simulated at temperature T with lattice size L = 16, 32, 64. — toy note §4 — [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)
- **m; M; U** — the ρ-odd order parameter m = ⟨cos φ⟩; the U(1) order parameter of the run without potential, ⟨|M|⟩ = |⟨e^{iφ}⟩|; and the Binder cumulant (U in the round-4 referee's notes). — toy note §4; `review/round4/referee/audit-notes.md` — [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)
- **ℤ₂** — in the toy note, model I's separate symmetry K → −K (§2); and, in "ordered ℤ₂ phase", the discrete order the frozen-H Monte Carlo finds, with an order parameter m = ⟨cos φ⟩ that is odd under ρ (§4). — toy note §2, §4 — [The twisted element](/wiki/symmetry-breaking/twisted-element); [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo)
- **θ; ⋆** — the Moyal noncommutativity [x₁, x₂] = iθ (θ = 1 in the note) and the star product. — toy note §3 — [Noncommutative field theory and the Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)
- **Ω** — the Grosse–Wulkenhaar model's parameter; at Ω = 1, the self-dual point, the model is invariant under the Langmann–Szabo duality. — toy note §1 — [Noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)
- **f_mn; H = ½x²** — the matrix base of the Moyal plane, with f_mn ⋆ f_kl = δ_nk f_ml, and the oscillator H = ½x² whose eigen-relations it satisfies. — toy note §3 — [Model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base)
- **x̃; D** — the dual coordinate x̃ = 2θ⁻¹x and the Langmann–Szabo duality transform D f(x) = (πθ)⁻¹ ∫ d²y e^{−i x̃·y} f(y), which acts on the matrix base as D f_mn = (−1)^m f_mn (written D₋ in the round-4 referee's notes). — toy note §3 — [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma)
- **Π; N** — parity on the matrix base, Π = e^{−iπN} in the worklog and diag((−1)^m) in `verify/toy_gw.py`; the duality acts on a field as Πφ, the α = π element of e^{−iαN}. — toy note §3; `notes/toy-lagrangian.md` — [The duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma)
- **μ², λ, φ_mn** — the mass parameter, the quartic coupling and the field components in S[φ] = Σ_mn (m + n + 1 − μ²)|φ_mn|² + λ Tr((φ†φ)²). — toy note §3 — [Model II: the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base)
- **β; Δ(β)** — the relative phase of φ₀₀ and φ₁₁ in a complex vacuum, and the polarization Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual = Δ(0) cos β. — toy note §3 — [Complex-model vacua and the polarization Δ(β)](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)
- **ψ = Πφ** — the alternating form in which the real model's quartic term Tr((ψψ†)²) is invariant. — toy note §3 — [Complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)
- **q₀, q₁; F(±)** — the occupations in the real vacua diag(±√q₀, ±√q₁), and the one-loop Gaussian free energies of the two relative signs, with F(+) − F(−) = 2.634. — toy note §3 — [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)
- **N; U(1)^N × U(1)^N** — the truncation (number of matrix levels), and the symmetry under which every condensate phase of the complex model is a flat direction. — toy note §3–§4 — [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)
- **G_ij** — the propagator 1/(i + j + 1 + M²) in the round-4 referee's tadpole check. — `review/round4/referee/audit-notes.md` — [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)
- **W; I[W]** — the Wigner function of a state, and the (H, K)-built coupling I[W] = ∫_{L+} du (∫_{L−} dv W)², called I_K in the round-4 records. — toy note §5 — [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)
- **ψ(x), ψ̃(p); F** — a state's wavefunction and its momentum representation, and the Fourier transform in the combined map (ψ → Fψ, K → −K). — toy note §5 — [Locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)
- **η with indices** — η written with phase-space indices in the section condition, displayed below (d = 1). — toy note §5 — [The section condition](/wiki/symmetry-breaking/section-condition)

  ```text
  η^{AB} ∂_A f ∂_B g = 0,     η^{AB} ∂_A ∂_B f = 0
  ```

## The retired soliton candidate

These symbols belong to #14, withdrawn after the round-3 review. The candidate is dead (see [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)), and #14's body numbers are superseded by the round-3 rulings.

- **SU(2)_d → U(1)_d; Φ, v** — the hidden gauge group, broken by a real adjoint scalar Φ with expectation value v. — #14 §2 — [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)
- **W′±; ψ; γ′** — the charged hidden vectors, of mass g_d v; the hidden Dirac doublet, with U(1)_d charges ±g_d/2; and the hidden photon (γ′ in the round-3 audit). — #14 §2; `review/round3/referee/audit-notes.md` — [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure); [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)
- **g_d; g_m** — the hidden gauge coupling and the monopoles' magnetic charge, g_m = 4π/g_d. — #14 §2 — [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)
- **α_W′; α_m** — α_W′ = g_d²/4π, and the monopoles' mutual coupling α_m = g_m²/4π = 1/α_W′. — #14 §2 — [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)
- **α_d; α_e,d** — the dark coupling, "α_d ≈ 34" in `HANDOFF.md` §2 (dead as derived from Dirac quantization against our photon), and the worklog's mirror electric coupling. — `HANDOFF.md` §2, §6; `review/v3-worklog.md` F2 — [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)
- **H (hypothesis H)** — #14's coupling hypothesis that the smallest hidden charge equals ours, (g_d/2)²/4π = α. — #14 §2 — [Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)
- **M = 4πf v/g_d; f** — the monopole mass, with f = 1 in the Bogomolny–Prasad–Sommerfield limit and about 1.79 at large scalar self-coupling (1.787 in `verify/soliton_obituary.py`). — #14 §3 — [The 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)
- **n/s = p(T_c/M_Pl)³; p; T_c** — the Kibble yield, its normalization and the transition temperature. — #14 §3; #11 §12 — [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)
- **M\*** — the monopole mass at which the Kibble abundance matches the observed dark-matter density. — #14 §3; `review/round3-adjudication.md` ruling 2 — [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)
- **M_\*** — the scale suppressing the dimension-five operator Φ^a F^a B/M_\*. — #14 §2(b) — [Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator)
- **ε** — kinetic mixing between the field strengths of our photon and the hidden one; gravity alone gives ε ≲ 10⁻¹³. — #11 §4; #14 §2 — [Kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)
- **C** — hidden charge conjugation; if it is exact, gravity induces no mixing. — #14 §2; #11 §4 — [Kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)
- **θ_d; q_vis** — the hidden theta angle, and the visible electric charge it gives a monopole through the Witten effect when ε ≠ 0. — `review/round3/referee/audit-notes.md` 4(a) — [Kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)
- **ξ** — the hidden-to-visible temperature ratio. — #14 §4 — [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)
- **g\*; s₀; Y** — the relativistic degrees of freedom, the entropy density today, and the yield Y = n/s (with Y_eq and the freeze-in yield Y_FI in the round-3 audit). — #14 §3; `review/round3/referee/audit-notes.md` — [The radiation era](/wiki/cosmology/early-universe/radiation-era)
- **σ_T/M; F** — the monopoles' transfer cross-section per mass, and the flux they would have had as monopoles of our U(1). — #14 §4 — [Benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)
- **λ_p** — the Higgs-portal coupling in the round-3 audit's list of omitted constraints. — `review/round3/referee/audit-notes.md` 4(c) — [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings)

## Labels and marks

- **P1–P5; P2; P2′** — the postulates; P2 is the superseded original, P2′ its repair. — #11 §4 — [Postulates P1–P5](/wiki/program/postulates)
- **#1–#15** — the artifact numbers of `HANDOFF.md` §3. — [Documents](/wiki/history/documents)
- **T1–T7** — the seven tests of the verification battery. — `HANDOFF.md` §5; `verify/battery.py` — [The verification battery T1–T7](/wiki/method/verification/battery)
- **S0–S5** — the toy models' success criteria, fixed before construction. — `notes/toy-lagrangian.md` — [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)
- **`OP1`–`OP11`** — the wiki's names for the open problems of #11 §14, items 1–11. — #11 §14 — [Open problems and the queue](/wiki/status/open-problems)
- **R1–R7; F1, F2, L1, O1–O3** — the round-2 pending items, and the v3 worklog's own findings, literature point and open items. — `review/v3-worklog.md` — [Review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)
- **F1–F6; C1–C3** — round 4's numbered findings and the referee's conceptual points. — `review/round4-adjudication.md`; `review/round4/referee/audit-notes.md` — [Review round 4](/wiki/method/review/round-4)
- **Rulings 1–13; Decisions 1–4** — round 3's rulings and the decisions taken after it. — `review/round3-adjudication.md` — [Round-3 rulings](/wiki/method/review/round-3/rulings); [Round-3 decisions](/wiki/method/review/round-3/decisions)
- **Rows 1–11** — the rows of #11 §13's predictions table. The Debt-3 notes and #1 §9 number an older table, whose rows 3 and 4 are withdrawn. — #11 §13 — [Predictions and kill conditions](/wiki/predictions); [History of the predictions table](/wiki/predictions/table-history); [Obituary: velocity-space granularity in halos (old row 3)](/wiki/dark-matter/momentum-clumping/velocity-granularity); [Obituary: Fornax friction suppression (old row 4)](/wiki/dark-matter/momentum-clumping/fornax-friction)
- **[D] [T] [P] [O] [V]; † [S]; ✓; conjecture-tier; `[NOTE-tier]`** — the provenance tags (derived here, literature, postulate, open, machine-verified), the citation marks (from model memory, live-searched), the handoff's machine-check mark, #13's label for a conjecture, and the v3 worklog's label for a result its script printed only as a note line, an adjudication input the manuscript did not yet quote. In #1, [T] meant "theorem — established in the literature, cited". — #11 header; #1 §0; `HANDOFF.md` §2; #13 §5; `review/v3-worklog.md` O2 — [Provenance tags and citation marks](/wiki/method/provenance-tags)

## Collisions

Each symbol below means different things in different documents. A page that uses one names its meaning in words at first use.

- **ρ** — the Born rotation (#11 §3); an energy density in Γ_self and N_occ (#2, #3; #11 §9) and ρ_DM (#14 §3).
- **ω** — the symplectic form; a frequency in the Vlasov response, δf ∝ e^{i(k·x − ωt)} (#2); ω_p, the monopoles' magnetic plasma frequency (round-3 audit 4(c)).
- **η** — the neutral metric; η_B, the baryon asymmetry (#1 §5.3).
- **τ** — the dark-energy field; τ_c, the complexified gauge coupling (#11 §11.3); τ_cond, the condensation time (#4); τ̃, the dual proper time (#13 §3).
- **μ** — the gate width (#11 §8); the coupling of model I's ρ-preserving potential (toy note §4); μ², the mass parameter of model II (toy note §3); a parameter proportional to λ/g² in the round-3 referee's monopole profile (`review/round3/referee/step2b.py`); and a spacetime index (X_μν, λ_μ).
- **H** — the generalized metric; the Hubble rate (#1 §6; #14 §1); the oscillator ½x² of model II (toy note §3); the scalar profile H(ξ) of the round-3 referee's monopole; hypothesis H (#14 §2).
- **K** — K = η⁻¹ω; the gauge profile K(ξ) of the same monopole calculation (`review/round3/referee/step2b.py`).
- **f** — τ's period scale (#1 §2); the second frame or metric (#8 §1); the monopole mass factor (#14 §3); a distribution function (#2; f̄ in #1 §5.2); model I's couplings f_H, f_K and model II's matrix base f_mn (toy note); test functions in the section condition (toy note §5).
- **Λ** — the Lagrangian Grassmannian Λ(d); the cosmological constant (#11 §7.4, §10); a factor #3 leaves undefined in Γ_gr; the scale Λ_c of #14 v2 (`review/v3-worklog.md` F2); Λ_wedge (`HANDOFF.md` §3); the Coulomb logarithm ln(Λ) (#14 §4).
- **σ** — the velocity dispersion (#2); σ_T(v) and σ₀ (#11 §8); σ_scat (#3); σ_T/M (#14 §4); the σ-modes of Λ(d) (#5 §D); σv, an annihilation cross-section (`review/v3-worklog.md` O1; `review/round3-adjudication.md` ruling 4).
- **ε** — the momentum scale ε = ℏ/λ (#1 §2; #13 §1); kinetic mixing (#11 §4; #14 §2); the expansion parameter of battery test T4 (`verify/battery.py`); a particle's energy ε(p; f) (#1 §5.2); ε_int and ε_gate (#2).
- **θ** — the Moyal parameter (toy note §3); θ_d, the hidden theta angle (round-3 audit); θ_pol, the polarization tilt (#1 §8).
- **Ω** — the Grosse–Wulkenhaar parameter (toy note); the stirring rate 1/t_dyn (#3); the density fractions Ω_χ, Ω_b, Ω_DE, Ω_DM, Ω_x^(0) and Ωh².
- **φ** — model I's polarization angle (toy note §2, §4); the dual rapidity (#13 §2); the field components φ_mn (toy note §3); m_φ, the gate mediator's mass (#1 §3).
- **Φ** — the hidden adjoint scalar (#14 §2); Φ_grav, the gravitational potential (#2).
- **β** — the relative phase of model II's vacuum (toy note §3); the bimetric coefficients βₙ (#8; #11 §7.3); β/H, the bubble-counting parameter in the round-3 audit's p ~ 104 (β/H)³; the β-function (toy note §1).
- **α** — α̃, the gate coupling (#1 §3); the fine-structure constant (#14 §2); α_d (`HANDOFF.md`); α_W′ and α_m (#14 §2); α_e,d (`review/v3-worklog.md` F2); the partially-massless mass-ratio parameter (#11 §7.4); the phase α in e^{−iαN} (toy note §3).
- **κ** — the Scenario-A normalization (#3); the annihilation coefficient κ = 1–10 (`review/v3-worklog.md` O1).
- **λ** — the Born length (#13 §1) and λ_χ (#13 §4); the dual-diffeomorphism parameters λ_μ (#6 §2); the couplings of model I and model II (toy note); the scalar self-coupling, the λ of the Kibble–Zurek estimate n ~ λHT_c², and the Higgs portal λ_p in the round-3 audit; λ_dB (#2).
- **ξ** — the hidden-to-visible temperature ratio (#14 §4); the p⁴ dispersion coefficient (#1 §4); the radial variable of the round-3 referee's monopole profile.
- **ψ** — the hidden Dirac doublet (#14 §2); a wavefunction (toy note §5); the alternating form ψ = Πφ (toy note §3).
- **χ** — conjugate matter (#11 §8); a kinetic-mixing parameter in Brümmer and Jaeckel's notation (round-3 audit); χᵢ, an initial field amplitude (#3).
- **γ** — the stream-instability growth rate (#1 §5.2); γ̃, the dual Lorentz factor (#13 §2); Euler's constant (`verify/toy_gw.py`); γ′, the hidden photon (round-3 audit).
- **A, B, C** — the proof blocks (#5 §A); A = [X, Y⁻¹] (#7 §2); B in the shift Z → Z + B (#6 §1) and the antisymmetric Kalb–Ramond B-field of double field theory (#6 §2); C, the combination of K and I in model I's potential (toy note §2); C, hidden charge conjugation (#14 §2); C, the lowest referee grade (see the [Glossary](/wiki/glossary)).
- **c** — the speed of light; Γ_self's coefficient (#3); the annihilation coefficient in the round-3 audit.
- **E** — the symplectic vielbein (#7 §3); an energy (#13 §4); the lattice energy (toy note §4); the residual matrices E1, E2 of the round-3 referee's compatibility check.
- **F** — the gate form factor (#11 §8); a force and the dual-boost parameter (#13 §2); the monopole flux (#14 §4); the free energies F(±) (toy note §3); the Fourier transform (toy note §5). The labels F1–F6 (round 4) and F1, F2 (the v3 worklog) name different findings.
- **g** — the metric (#11 §6); the gated contact coupling (#2, #3); a magnetic charge (#11 §11.3); g\*, relativistic degrees of freedom (#14 §3); g_d, the hidden coupling (#14 §2); a test function (toy note §5).
- **G** — Newton's constant (#3; #13 §1); the Gaussian gate (#2); G_eff (#1 §6); the propagator G_ij (round-4 referee notes).
- **h** — the metric perturbation (#7 §2); Planck's constant h in the chat-only relation of `HANDOFF.md` §4; the two-fold field of the lattice model (toy note §4); a monopole's magnetic charge in Liveoak–Maharana–Wells's notation (round-3 audit); h in Ωh².
- **I** — I = ω⁻¹H (#11 §5), written H⁻¹ω where the round-3 audit restates Freidel–Leigh–Minic; the matter coupling I[W] (toy note §5).
- **J** — J = η⁻¹H (#11 §5); the lattice coupling (toy note §4).
- **k** — the gate variable (#1 §3); a wavevector (#2); k = 4πf/g_d in the round-3 referee's mass relation (`review/round3/referee/step2a.py`); k̃, the dual curvature parameter (#1 §10).
- **L** — the eigenlines L±, L and L̃ (toy note; worklog); the lattice size (toy note §4); model I's Lagrangian (toy note §2).
- **M, m** — M_X, M_B, M_P (M_Pl), M̃, M_f, M_g, M\*, M_\*, M_core and M_crit, which differs from the classicality threshold m_crit; the amplitude M(k, q) (#11 §8); the monopole mass M (#14 §3); the Monte Carlo's U(1) order parameter M and its ρ-odd order parameter m (toy note §4); m_χ, m_φ, m_FP², m_g, m_W′ and m_ψ; m and n as matrix indices (toy note §3).
- **N** — the occupation number N_occ (#2); the lapse (#1 §6); the photon count (`HANDOFF.md` §4); the truncation level (toy note); N_eff; the level-number operator in e^{−iαN} (toy note §3); the N = 4 of super-Yang–Mills theory (#14 §2).
- **p** — momentum; the Kibble normalization (#14 §3; #11 §12); p₄, a power sum (#7 §2).
- **q** — the momentum transfer (#1 §3); a charge in ⟨q, q′⟩ (#11 §11.3); the occupations q₀, q₁ (toy note §3); q_vis (round-3 audit).
- **R** — the rotation matrix (#1 §2); R_B[H] (#1 §2); R_X (#3); Segue 1's ratio R (#4); the worklog labels R1–R7.
- **S** — the action and its parts (#1 §3); the block S (#7 §2); S ≡ σ₀/m (#2); a symplectic matrix, or the boost S(t) of the round-4 records (toy note §2, §4); the terms Sₙ (#8 §1); the criteria S0–S5; S-duality (#11 §11.3).
- **T** — the tadpole (#8 §2); temperatures (the Monte Carlo's T, T_c, and T_d and T_RH in the round-3 audit); the battery tests T1–T7; T̃, the dual stress (#5 §E); T-duality (#11 §11.3).
- **U** — the stabilizer U(1, d−1) (#6 §3); the Binder cumulant (round-4 referee notes); U-duality (#11 §11.3).
- **X** — the momentum graviton (#5 §C); the mean-field parameter X ≡ gn/(mσ²) and the environment label in R_X (#3); a heavy particle charged under both groups, in the Chen–Cline–Frey wording quoted in `review/round3-adjudication.md` ruling 7.
- **Y** — Im Z (#5 §C); the yield n/s and its forms Y_eq and Y_FI (round-3 audit).
- **†** — the citation mark; the Hermitian adjoint in the toy note.
- **GW** — Grosse–Wulkenhaar on the wiki; gravitational waves in several documents, written out on the wiki.

## Sources

- `papers/broken-born-checkpoint-v2.md` §3–§14 — the current symbols for the program, from ρ and the three structures through the modular field, the bimetric potential, the gate, cosmology and the charge lattice
- `papers/reciprocity-toy-models.md` §1–§5 — the toy models' symbols, including K as the real structure with η = ωK
- `papers/conjugate-special-relativity.md` §1–§5 — c̃, λ, λ_χ and the dual kinematics
- `notes/broken-born-theory.md` §0–§8 — the lab notebook's original definitions: R, ρ², J as order parameter, τ, the action, χ and the gate variables, the cosmology
- `notes/debt1a-geometric-core.md`, `notes/debt1a-ii-X-classification.md`, `notes/debt1a-iii-tuning-test.md`, `notes/debt1a-iv-beta-coefficients.md` — H_Z, the shift symmetry, π_μ, the misalignment blocks, E, 𝕏, βₙ and T
- `notes/debt3a-stream-stability.md`, `notes/debt3b-wave-island.md`, `notes/debt3c-ufd-endpoint.md` — the momentum-clumping symbols: g, G, n_gate, N_occ, Γ_self, R_X, κ, M_crit
- `notes/knot-dark-matter-standalone.md` §2–§4 — the retired candidate's hidden-sector symbols
- `notes/toy-lagrangian.md` — Π, L and L̃, S0–S5
- `review/v3-worklog.md` R7, F2, O1 — M_f, M_g, α_e,d, κ
- `review/round3/referee/audit-notes.md`, `review/round3/referee/step2a.py`, `review/round3/referee/step2b.py` — the round-3 referee's notation (γ′, θ_d, q_vis, Y, λ_p, the monopole profile) and N_eff,SM
- `review/round4/referee/audit-notes.md`, `review/round4-adjudication.md` — V_μ, V_λ, V′, D₋, G_ij, U
- `HANDOFF.md` §2–§5 — the artifact numbers, Λ_wedge, α_d, the chat-only D_x, D_p, N, and the battery labels
- `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/battery.py`, `verify/soliton_obituary.py` — K₀ and K_ref, Π, the T4 expansion parameter, the value of f
