---
title: "The gate-mechanism script"
weight: 130
status: method
description: "verify/gate_mechanism.py recomputes the algebra and numbers of the gate-mechanism note: anchors independent of both derivations (CODATA, on-shell kinematics, the Fierz–Pauli numerator and its helicity sum, Legendre and Chebyshev identities, the zero-range s-wave), then the t-channel exchange of X, the Dirac case, the numbers at μc = 20 keV, the two readings of the fiber overlap, the polarization under boosts, run 3's checks, and the two derivations side by side; it reruns their arithmetic and algebra and does not test their physics."
provenance: [D, V]
sources:
  - "verify/gate_mechanism.py"
  - "notes/gate-mechanism.md header"
  - "notes/gate-mechanism.md §1–§5"
  - "notes/gate-mechanism.md §6"
  - "notes/velocity-gated-gravity.md §9"
  - "review/momentum-gravity/README.md"
  - "review/momentum-gravity/answer.md 'Candidate flags (for your ruling)'"
  - "scripts/check.sh"
  - "CLAUDE.md 'Layout'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "review/wiki-build-flags.md items 17, 55"
---

*The gate-mechanism script, `verify/gate_mechanism.py`, recomputes the algebra and the numbers of the note that asks whether exchanging the program's momentum graviton X can produce the velocity gate of its dark matter, the factor that switches the dark matter's self-interaction off when two particles move at very different velocities. Two derivations answered the question, the second blind; both ran in scripts outside the repository, and this file ports them into one self-contained check that the gate runs. Before it computes anything from the derivations, it checks identities that do not depend on them: CODATA 2018 constants, the kinematics of particles on their mass shell, the textbook numerator of a massive spin-2 field and its decomposition into five polarization states, Legendre and Chebyshev polynomial identities, and the scattering of a zero-range interaction. Everything after these anchors is, in the docstring's words, a regression check of the derivations' own numbers and algebra. The note states its limit plainly: the script reruns the arithmetic and algebra of the two derivations and does not test their physics.*

**Status:** Method, in force — the note says that "Every number and algebraic result is recomputed in `verify/gate_mechanism.py`" (note header), and its [V] tags rest on the script — tenth and last in the list of scripts that [the gate](/wiki/method/verification/the-gate), `scripts/check.sh`, runs. The run of 2026-10-28 recorded below printed 83 lines marked `PASS` and none marked `FAIL` (a count of its output lines), and the script ended "OK — every result of the gate-mechanism derivation reproduces." The note has not been reviewed, and its result is proposed to Paul as flag 55 in `review/wiki-build-flags.md`, awaiting his ruling.

## What it checks, and for what

The note is `notes/gate-mechanism.md`, of 2026-10-28. Checkpoint #11 §8 says that χ's velocity gate is "delivered by X-exchange between dual-stress bilinears" and tags it "[D — mechanism; shape [O]]". The note finds that exchanging #11 §7's X cannot produce the gate, and that #6 §4's fiber overlap, written out, is either an ordinary short-range potential or a pair interaction that contains no X. Its results are on [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism), in the sections [exchanging X cannot produce the gate](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate) and [the fiber overlap, read two ways](/wiki/dark-matter/conjugate-matter/gate-mechanism#the-fiber-overlap-read-two-ways); the spin-J and medium results it shares with the momentum-gravity note are on [what could carry a relative-velocity gate](/wiki/dark-matter/conjugate-matter/gate-carriers). The note's tags are [D][V] for the derived results the script reruns; the proposed tags [P] for the gate and [O] for its mechanism are flag 55's, pending Paul's ruling, and #11 is unchanged.

The docstring states the question, the two derivations, the anchors and the inputs:

```text
gate_mechanism.py — every result of the gate-mechanism derivation
(notes/gate-mechanism.md), recomputed and checked. The question: can
exchanging the momentum graviton X that #11 §7 constructs produce the
dark-matter velocity gate of #11 §8, which #11 tags "[D — mechanism; shape
[O]]"? Two derivations answered it, both executed outside the repository and
kept in review/momentum-gravity/:
  - run 3's theory verifier: run3/verify-critic-theory.json, scripts in
    scripts/verify-critic-theory/ (v1-v7);
  - run 4's blind second derivation: run4/gate-derivation.json (claims
    C1-C19), scripts in scripts/derivation-gate-mechanism/ (gate_tchannel.py,
    gate_fermion.py, gate_numbers.py, fiber_overlap.py,
    polarization_lorentz.py).
This file ports their computations (it imports none of them) and is
self-contained. The ported source is named at each section. Check names carry
the claim id: C1-C19 for run 4, T-numbers, c1 and 'gate-range' for run 3.

Exit code 1 if any check fails. Anchors come first and are independent of
both derivations: [...] Everything after the anchors is a regression check:
it reproduces the derivations' own numbers and algebra and is not
independent of them. Section H sets the two derivations side by side wherever
both computed the same quantity.

Inputs: the record's benchmark (#1 s5.1, #11 s8): m_chi c^2 = 70 MeV, v* ~ 120
km/s, mu = m_chi v*/sqrt2 ~ 20 keV. The two derivations take different
primaries. Run 4 takes mu c = 20 keV, so v* = 121.1 km/s and hbar/mu = 9.87
pm; run 3 takes v* = 120 km/s, so mu c = 19.813 keV and hbar/mu = 9.96 pm.
Each is checked in its own convention. Gate convention (run 4): amplitude
exp(-k^2/mu^2) with k = m v_rel/2, i.e. exp(-v^2/v_a^2) with v_a = sqrt2 v* =
2 mu c/m; cross-section exp(-v^2/v*^2). Amplitude algebra in hbar = c = 1,
metric (+,-,-,-). CODATA 2018 G = 6.67430e-11 is typed in for run 3's
alpha_G.

Runtime is about 8 s and peak memory about 135 MB (the sympy contractions of
B and the integrals of E dominate). The record's scripts were rerun once
while porting; their outputs matched the stored .out files byte for byte.
```

The docstring's lines are rewrapped here, the command that runs the script is left out, and the bracket stands for its list of anchors, set out below. Each check prints `PASS` or `FAIL`, its label and, where there is one, the computed value or expression in brackets; indented lines print a table without a check, and bracketed times are elapsed seconds. The failures are collected, and the script lists them and exits with code 1. Most labels carry the claim number of run 4's derivation (C1–C19); run 3's carry its own names. The algebra runs in sympy, the numerical integrals in mpmath and numpy.

The two derivations read the record's benchmark differently, and the script checks each in its own convention: run 4 takes μc = 20 keV, so v\* = 121.1 km/s and ħ/μ = 9.87 pm; run 3 takes v\* = 120 km/s, so μc = 19.813 keV and ħ/μ = 9.96 pm. The note's §1 gives the difference as 0.95%, and block H checks it.

## The anchors

The rule behind them is root `CLAUDE.md`'s: "An anchor must be independent of the paper (a textbook identity, a published value)." ([independent anchors](/wiki/method/verification/independent-anchors)). The block headed "A. Anchors (independent of both derivations)" prints 12 `PASS` lines:

- **Constants.** ħc = 197.3269804 MeV fm and 1 MeV/c² = 1.78266192×10⁻²⁷ g, both from the constants that the International System of Units fixes exactly, in CODATA 2018.
- **On-shell kinematics.** For particles on their mass shell, p·p′ = m² − t/2 and ((p + p′)/2)² = m² − t/4, in sympy. This is the identity behind the note's first result, that a vertex depends only on the transfer.
- **The massive spin-2 numerator.** The [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) numerator is symmetric, transverse and traceless on shell, a projector of rank 5, and not transverse off shell; it equals the sum over five explicitly built helicity tensors, at rest and after a boost; at rest the residue factorizes as (2/3)|a|²|b|²P₂(cos θ_ab). The van Dam–Veltman–Zakharov factor: between static sources the massive and massless numerators are 2/3 and 1/2, ratio 4/3; the citation, van Dam–Veltman–Zakharov (1970), is marked † in the label.
- **Polynomial identities.** The Legendre polynomials P₀ to P₈ from sympy, Bonnet's recursion and the generating function agree, with their orthogonality; the spherical-harmonic addition theorem for J = 0–6, which is why "a spin-J pole's residue, the polarization sum between two vertices, is proportional to P_J of the cosine"; the closed-form Legendre expansions of e^{az} and of 1/(α − z) against quadrature; and Chebyshev's min-max property against brute force: the monic quadratic of least maximum on [−1, 1] has maximum 1/2, and among quadratics with P(0) = 1 the least maximum on [1, 4] is 9/41.
- **The zero-range s-wave.** f = −1/(1/a + ik) gives σ = 4πa²/(1 + k²a²), obeys the optical theorem and saturates the unitarity limit 4π/k² as a → ∞.

## The checks, block by block

### B. t-channel exchange of one massive spin-2 X (19 checks)

A port of run 4's `gate_tchannel.py`, claims C1–C7. In the centre-of-mass frame s − u = 8k² + 4m² − q² at fixed transfer q, with k the incoming relative momentum.

- C1: at one vertex the only invariant is t, the squared momentum transfer.
- C2: at fixed q the t-channel numerator is a polynomial of degree 4 in k (2 in k²), "no denominator in k, so no tail", of the form A(t) + B(t)(s − u) + C(t)(s − u)² with C = F₁².
- C3: the residue at t = M_X² does not depend on F₂, F₃, F₄; it is (2/3)F₁²(4m² − M_X²)²P₂(z_t); the rest is a polynomial contact term.
- C4: the minimal vertex is conserved; with it the forward ratio is N_min(k, 0)/N_min(0, 0) = 1 + 6k²/m² + 6k⁴/m⁴, "its k-scale is m/sqrt6, a relative speed of order c".
- C5: at q = 0 the coefficients of k² and k⁴, 64F₁²m² and 64F₁², are non-negative, so "the forward numerator never decreases with k^2 except toward one zero"; for minimal coupling the k-scale squared is m²/6.
- C6: the forward u-channel term is rational in k with scale M_X/2, and in the forward direction t plus u gives (M² + 2k²)/(M² + 4k²) → 1/2 (the label's "spin-0 forward t + u"): "the u-channel halves the forward amplitude, it does not gate it"; the s-channel residue is the d-wave (32/3)G₁²k⁴P₂(cos θ) and vanishes at threshold, "an anti-gate".
- C7: the Legendre coefficients of e^{−z} and of 1/(2 − z) are nonzero for l = 0–6: "a non-polynomial residue F(s) needs every spin".

### C. Dirac χ (3 checks)

A port of `gate_fermion.py`. All 12 printed rows of the fermion amplitudes reproduce; the spin-preserving amplitudes give the same coefficient as scalar χ, 6.00; and the spin-flip amplitude, "printed in gate_fermion.out, not in C4's text", has coefficient 2.0000, "also of order one: the k-scale is m in every helicity channel". The note marks the Dirac case "one derivation" (§2).

### D. Numbers at μc = 20 keV (13 checks)

A port of `gate_numbers.py`, in run 4's convention:

- C19: μ/m = 2.8571×10⁻⁴, v\* = 121.1 km/s and v_a = 171.3 km/s; C9/C11: ħ/(μc) = 9.87 pm, "the range of the R1 potential, the nonlocality of R2"; C6: ħ/(M_X c) = 4.93 pm at M_X = 2μ; C5: (m/μ)² = 1.225×10⁷.
- C4: a table of X's forward k-dependence beside the gate at v = 50, 120, 171.3, 300 and 1500 km/s reproduces; X's k-dependence is 2.4×10⁻⁷ at 120 km/s and 3.8×10⁻⁵ at 1500 km/s, "where the gate exp(-k^2/mu^2) falls from 0.61 to 5e-34"; it reaches order one at 0.816c, 1429 times v_a, or at 0.661c read relativistically.
- C5: no quadratic P with P(0) = 1 stays below 0.90324 in magnitude on x ∈ [1, 76.7], the range from v_a to 1500 km/s, by Chebyshev's bound, which convex minimization confirms; the record's random search found nothing better than 0.90378; over that range the Gaussian gate falls from 3.679×10⁻¹ to 5.050×10⁻³⁴.
- C19: the contact Born benchmark, σ₀/m = 32.01 cm²/g at 70 MeV, or m = 71.5 MeV for 30 cm²/g. The note counts this among what does not change: "The benchmark arithmetic is contact Born physics and needs no mechanism" (§5; [the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)).
- C8: a zero-energy state with 1/a = μ gives σ/m = 9.803×10⁷ cm²/g at 70 MeV, 3.27×10⁶ times 30 cm²/g.
- C14: a preferred-frame vertex suppresses a pair moving at V by e^{−m²V²/μ²}: 2.559×10⁻¹, 4.705×10⁻⁶ and 4.899×10⁻²² at V = 100, 300 and 600 km/s.

### E. The fiber overlap in field-theory terms (9 checks)

A port of `fiber_overlap.py`, claims C1 and C9–C11, the two readings of [#6 §4's fiber overlap](/wiki/dark-matter/conjugate-matter/gate-mechanism#the-fiber-overlap-read-two-ways):

- C1/C9: a bilinear's fiber coordinate is the average momentum, and with momentum conserved the fiber separation of the two bilinears is a momentum transfer.
- C9, reading R1: its Born amplitude for identical χ is S(q) + S(q_u), which at q → 0 is 1 + e^{−2k²/μ²} and tends to 1, not 0, at large k ("#6's exp(-(p1 - p2)^2/2mu^2) is only the exchange term's forward value"); as an operator it is local in position, a Gaussian of width 1/μ; a one-dimensional quadrature confirms the operator identity for two pairs of wavepackets; and the overlap of two packets is a property of the states.
- C11, reading R2: the pair bilinear depends on the pair's relative momentum, and the separable amplitude |g(k)|² on shell is the gate.
- C10: the tails — R2 falls faster than any power; R1 with Gaussian profiles has the power-law tails 2πμ⁴/k⁴ (identical χ) and 2πμ²/k² (distinct species); a Yukawa force π ln k/k⁴; at k = 10μ, R2 gives 1.159×10⁻⁸⁶ against R1's 6.252×10⁻⁴.

The note calls the two readings "this note's reconstruction; the theorems about each are derived" (§3), and marks them "one derivation".

### F. The vacuum polarization under boosts (5 checks)

A port of `polarization_lorentz.py`, claims C13 and C14. With Lorentzian g, the blocks ω, η, K, J and H are all invariant under the boost L = diag(Λ, Λ^{−T}), with residuals at or below 10⁻¹⁵, and H is not positive definite; the Born rotation ρ flips K and J and commutes with L, "the vacuum breaks rho, not Lorentz symmetry"; with positive-definite H, as [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem) assumes, J and H are not Lorentz-invariant (2.5 and 2.9). C14 checks the Galilean identity Σ|mV + k_i|² = 4m²V² + 4k², behind the preferred-frame factor of block D. The note marks these "one derivation" (§4).

### G. Run 3's theory verifier (14 checks)

Ports of run 3's `v3_gate_range.py`, `v6_medium_mediator.py`, the J = 2 parts of `v1_spinJ_residues.py` and T3 of `v7_misc_numbers.py`:

- **Gate range (a)–(d).** With the gate inserted by hand around a separate potential, all 72 printed ratios reproduce; the quantum expectation matches the classical gated value within 3.4×10⁻³ at 3–10 ħ/μ, 7×10⁻⁴ at 30, 5×10⁻⁵ at 100 and below 10⁻⁵ from 300 on, so "non-relativistically the gate is not tied to contact range"; at 1000 ħ/μ the gate survives; on a Coulomb potential the smoothed potential times r is erf(rμ/ħ); in run 3's convention μc = 19.813 keV and ħ/μ = 9.960×10⁻¹² m, and the mean χ spacing, 4.121×10⁻³ m in a dwarf core and 5.593×10⁻³ m locally, is far above ħ/μ. The note marks the range result "one derivation, the first" (§3).
- **A medium (T6).** The fields of a source moving through a mediator of speed c_s solve the wave equation; two bodies at zero relative velocity, side by side, feel 1.155, 2.294 and 7.089 times the static force at V/c_s = 1/2, 9/10 and 99/100; above c_s the trailing body feels twice the static force and the others none: "the dependence is on velocity through the medium, not between the bodies".
- **X's own residue (c1).** P₂(γ) = 2.315350 times static at γ = 1.37 for the massive field, T₂(γ) = 2.753800 for the massless one; at 120 km/s P₂(γ) − 1 = 2.40332×10⁻⁷ and T₂(γ) − 1 = 3.20443×10⁻⁷.
- **Loops (T3).** For gravitational-strength exchange between 70 MeV χ, α_G = 3.287×10⁻⁴¹ and the Bohr-type velocity 9.855×10⁻³³ m/s: "loops bring no scale near v\* either".

### H. The two derivations side by side (8 checks)

Where both derivations computed the same quantity: run 4's forward numerator is exactly run 3's spin-2 residue P₂(γ) with γ = 1 + 2k²/m² (H1), and run 4's pole variable tends to γ (H2); X's velocity dependence at 120 km/s, 2.4033×10⁻⁷ and 2.40332×10⁻⁷, agrees to the quoted digits (H3); both give the van Dam–Veltman–Zakharov ratio 4/3 (H4); the nonlocality ħ/μ, 9.87 pm and 9.960 pm, differs by 0.95%, the ratio of the two readings of μ (H5), and (mc/μ)² likewise (H6); both find that spin-2 exchange grows with relative velocity and never gates (H7); and both find that a preferred frame gives dependence on velocity through that frame, not on relative velocity (H8).

## What it does not recompute

- **The physics.** The note: "Neither derivation's own results were checked by a further agent. `verify/gate_mechanism.py` reruns their arithmetic and algebra; it does not test their physics" (§6). The checks show that each derivation's algebra and numbers follow from its own setup ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).
- **One-derivation results.** The central result, that an on-shell vertex depends only on t and that single exchange of a finite-spin carrier gives a residue polynomial in the pair's velocity with velocity scale c, rests on both derivations (§6). The note marks the results that only one of them computed "one derivation": among them the fiber weight w(m² − t/4), the Dirac case, the polynomial bound, the u and s channels, the resonance, the readings R1 and R2, the polarization and the preferred frame (run 4), and the gate's range and the medium (run 3).
- **The setup's caveats.** From the second derivation: "the main theorem is tree level on a flat background with the Fierz–Pauli numerator. Hassan–Rosen nonlinearities and vDVZ subtleties change the t-dependence and normalization, not the degree in s. The Lorentzian check transplants the program's block structures to Lorentzian g; the record's theorems assume positive H (OP3). Cross-section normalizations use unit couplings; only shapes and tail laws are compared" (§6; vDVZ is van Dam–Veltman–Zakharov).
- **The record audit.** The note's finding that no χχX vertex, X propagator on the fibers, χ fiber profile, formula for the dual stress, overlap integral or verify script exists in the record (§3) was made by searching the record, not computed, and is not a check here.
- **The readings themselves.** Which of R1 and R2, if either, the record intended is not a computation; the script checks the algebra of each.
- **Inputs.** The record's μ ≈ 20 keV and v\* ≈ 120 km/s are not exactly consistent; the script checks each derivation in its own convention and does not decide between them. Flag 17's question of a √2 between the two gate conventions "is untouched by anything here" (§1). The resonant self-interacting dark matter the note compares with is cited from model memory (†).

## The recorded output

The run of 2026-10-28:

```text
== A. Anchors (independent of both derivations)
PASS  CODATA 2018: hbar c = 197.3269804 MeV fm, from the exact h, c and e  [197.3269804593]
PASS  CODATA 2018: 1 MeV/c^2 = 1.78266192e-27 g, from the exact e and c  [1.78266192163e-27]
PASS  on shell (p^2 = p'^2 = m^2), for any 3-momenta: p.p' = m^2 - t/2, i.e. -t = 2 m^2 (gamma - 1) with gamma = p.p'/m^2; and ((p + p')/2)^2 = m^2 - t/4 (sympy)
PASS  Fierz-Pauli numerator 1/2(G G + G G) - 1/3 G G, G = eta - l l/M^2, on shell l^2 = M^2: symmetric, transverse (l^mu P = 0) and traceless (eta^{mu nu} P = 0), a projector (P.P = P) of rank P^{mn}_{mn} = 5; off shell it is not transverse  [3.6e-15, 8.9e-16, 2.0e-14; rank 5.000000000000; off shell 4.48]
PASS  the sum over the five helicity tensors eps(+-2) = e+-e+-, eps(+-1) = (e+-e0 + e0e+-)/sqrt2, eps(0) = (e+e- + e-e+ + 2e0e0)/sqrt6 equals the Fierz-Pauli numerator, at rest and after a boost; they are orthonormal  [3.3e-16, 4.4e-16]
PASS  spin-2 residue factorization at rest: sum_lambda (a.eps.a)(b.eps.b)* = (2/3)|a|^2|b|^2 P_2(cos theta_ab)  [-0.049724064834 vs -0.049724064834]
PASS  van Dam-Veltman-Zakharov (1970) †: between static sources the massive (Fierz-Pauli) and massless (de Donder) numerators are 2/3 and 1/2, ratio 4/3  [0.666666666666667, 0.500000000000000]
PASS  Legendre P_0..P_8: sympy's legendre = Bonnet's recursion = coefficients of (1 - 2xt + t^2)^(-1/2); int P_i P_j = 2 delta_ij/(2i + 1) for i, j <= 6
PASS  addition theorem (textbook): sum_m Y_Jm(n1) Y_Jm(n2)* = (2J+1)/(4 pi) P_J(n1.n2), J = 0..6 (mpmath): a spin-J pole's residue, the polarization sum between two vertices, is proportional to P_J of the cosine  [max deviation 3.8e-18]
PASS  Legendre coefficients in closed form (generating function e^{az} = sum (2l+1) i_l(a) P_l(z); Neumann 1/(alpha - z) = sum (2l+1) Q_l(alpha) P_l(z)), against quadrature at a = 0.7, alpha = 3, l = 0..6  [9.9e-32, 5.2e-34]
PASS  Chebyshev min-max property, brute force: the monic quadratic of least sup norm on [-1, 1] has norm 2^(1-n) = 1/2 (T_2/2); with P(0) = 1, min over degree-2 P of max_[1,4]|P| = 1/T_2(5/3) = 9/41  [0.500000000, 0.219512195 (9/41 = 0.219512195)]
PASS  zero-range s-wave: f = -1/(1/a + ik) gives sigma = 4 pi a^2/(1 + k^2 a^2), obeys the optical theorem Im f = k|f|^2, and saturates the unitarity limit 4 pi/k^2 as a -> oo
      [0.8 s]

== B. t-channel exchange of one massive spin-2 X, general vertex (port of derivation-gate-mechanism/gate_tchannel.py; claims C1-C7)
PASS  kinematics (CM, equal masses): s = 4k^2 + 4m^2, t = -q^2, u = q^2 - 4k^2, so s - u = 8k^2 + 4m^2 - q^2 at fixed q  [s - u = 8*k**2 + 4*m**2 - q**2]
PASS  C1: at one vertex, p1^2 = p3^2 = m^2, p1.p3 = m^2 - t/2 and P.l = 0: the vertex's only invariant is t
PASS  C2: at fixed transfer q the t-channel numerator N_t(k, q) is a polynomial in k of degree 4 (2 in k^2), lowest power k^0: no denominator in k, so no tail  [degree 4]
PASS  C2: N_t = A(t) + B(t)(s - u) + C(t)(s - u)^2 with C = F1^2, B = 2 F2^2 q^2 (M^2 + q^2)/M^2, and A the printed degree-8 polynomial in q over 3M^4  [C = F1**2, B = 2*F2**2*q**2*(M**2 + q**2)/M**2]
PASS  C3: the residue at t = M_X^2 does not depend on F2, F3, F4  [[0, 0, 0]]
PASS  C3: residue = (2/3) F1^2 (4m^2 - M_X^2)^2 P_2(z_t), z_t = (s - u)/(4m^2 - M_X^2)
PASS  C3: the non-pole remainder is a polynomial in (k, q) over 3 M_X^4: degree 2 in k for constant F_i, degree 4 for F_i = a_i + b_i t (a contact term, quadratic in s)  [{'const': (3*M**4, True, 2), 'linear': (3*M**4, True, 4)}]
PASS  C4: the minimal vertex <p_out|T^{mu nu}|p_in> = 1/2 P P - 1/2 l l + (t/2) eta is conserved: l_mu V^{mu nu} = 0
PASS  C4: minimal-coupling numerator N_min = (s - u)^2/4 + t^2/4 + 2m^2 t - (2m^2 + t)^2/3
PASS  C4: N_min(0, 0) = 8m^4/3, and the forward ratio N_min(k, 0)/N_min(0, 0) = 1 + 6k^2/m^2 + 6k^4/m^4: its k-scale is m/sqrt6, a relative speed of order c  [6*k**4/m**4 + 6*k**2/m**2 + 1]
PASS  C4: at k = 0 the transfer dependence is N_min(0, q)/N_min(0, 0) = 1 - q^2/m^2 + q^4/(16 m^4)  [1 - q**2/m**2 + q**4/(16*m**4)]
PASS  C5: at q = 0, N_t = n0 + n1 k^2 + n2 k^4 with n1 = 64 F1^2 m^2 >= 0, n2 = 64 F1^2 >= 0 and n0 = 4m^4 (2F1 - F4)(4F1 + F4)/3: the forward numerator never decreases with k^2 except toward one zero  [n0 = 4*m**4*(2*F1 - F4)*(4*F1 + F4)/3, n1 = 64*F1**2*m**2, n2 = 64*F1**2]
PASS  C5: k-scale^2 = n0/n1 = m^2 (2F1 - F4)(4F1 + F4)/(48 F1^2); for minimal coupling (F1 = 1/2, F4 = t/2m^2 = 0 at q = 0) it is m^2/6  [m**2*(2*F1 - F4)*(4*F1 + F4)/(48*F1**2); minimal m**2/6]
PASS  C6: forward u-channel (identical chi, minimal coupling): u - M_X^2 = -(M_X^2 + 4k^2), so the term is rational in k with scale M_X/2; its series -8m^4/(3M^2) + k^2(-8m^2/(3M^2) + 32m^4/(3M^4)) + ... reproduces
PASS  C6: spin-0 forward t + u: A(k)/A(0) = (M^2 + 2k^2)/(M^2 + 4k^2) -> 1/2: the u-channel halves the forward amplitude, it does not gate it  [(M**2 + 2*k**2)/(M**2 + 4*k**2), limit 1/2]
PASS  C6: s-channel (chi chibar) residue at s = M_X^2 is (32/3) G1^2 k^4 P_2(cos theta) = 16 G1^2 k^4 (3c^2 - 1)/3: d-wave, independent of G2-G4  [16*G1**2*k**4*(3*c**2 - 1)/3]
PASS  C6: with the pole just below threshold (M_X^2 = 4(m^2 - delta)) the s-channel term G1^2 k^4 (4c^2 - 4/3)/(delta + k^2) -> 0 as k -> 0: it vanishes at threshold (an anti-gate)
PASS  C7: Legendre coefficients of exp(-z), l = 0-6: 1.17520, -1.10364, 0.357814, -0.0704556, 0.00996513, -0.00109959, 9.94543e-5, all nonzero, = (2l+1) i_l(-1)  [1.1752, -1.10364, 0.357814, -0.0704556, 0.00996513, -0.00109959, 9.94543e-05]
PASS  C7: Legendre coefficients of 1/(2 - z), l = 0-6: 0.549306, 0.295837, 0.105919, 0.0340978, 0.0104497, 0.00311274, 0.000910235, all nonzero, = (2l+1) Q_l(2): a non-polynomial residue F(s) needs every spin  [0.549306, 0.295837, 0.105919, 0.0340978, 0.0104497, 0.00311274, 0.000910235]
      [3.4 s]

== C. Dirac chi (port of derivation-gate-mechanism/gate_fermion.py; claim C4)
PASS  C4: Dirac chi, with and without a magnetic-type structure (kappa = 0, 0.7): all 12 printed rows of |A(k0)| and (|A(k)|/|A(k0)| - 1)/((k^2 - k0^2)/m^2) reproduce (q/m = 2e-3 and 0.1)  [[]]
PASS  C4: Dirac chi gives the same coefficient as scalar chi, 6.00 (6.0006 at k/m = 0.01, q/m = 2e-3, where |A(k)|/|A(k0)| - 1 = 5.9142e-4): at q/m = 2e-3 all four spin-preserving rows (uuuu, udud; kappa = 0, 0.7) equal scalar chi's N_min ratio at the same (k, k0, q), 6.0000, 6.0006, 6.0054, 6.0600, to 4 decimals  [scalar 6.0000, 6.0006, 6.0054, 6.0600; at q/m = 0.1 scalar 5.9969, 6.1748, 6.4713, Dirac 6.00-6.04, 6.18-6.21, 6.47-6.51]
PASS  C4, spin-flip channel (printed in gate_fermion.out, not in C4's text): the uudd amplitude, 1e-6 of the others at q/m = 2e-3, has coefficient 2.0000 (1.9906 at q/m = 0.1), also of order one: the k-scale is m in every helicity channel  [1.999996-1.999996]

== D. Numbers in run 4's convention, mu c = 20 keV (port of derivation-gate-mechanism/gate_numbers.py; claims C4, C5, C6, C8, C9, C14, C19)
PASS  C19: mu/m = 2.8571e-4; v* = sqrt2 (mu/m) c = 121.1 km/s; v_a = sqrt2 v* = 2 (mu/m) c = 171.3 km/s  [2.8571e-04, 121.1344, 171.3100 km/s]
PASS  C9/C11: hbar/(mu c) = 9866 fm = 9.87 pm (the range of the R1 potential, the nonlocality of R2)  [9866.35 fm]
PASS  C6: hbar/(M_X c) at M_X = 2 mu = 40 keV is 4.93 pm  [4.9332 pm]
PASS  C5: (m/mu)^2 = 1.225e7: a k-scale mu in the degree-2 numerator needs n0 cancelled to (mu/m)^2 = 1/(1.2e7)  [1.225000e+07]
      v =     50 km/s: k/m = 8.3391e-05, X: N(k)/N(0) - 1 = 4.1724e-08, gate exp(-k^2/mu^2) = 9.1834e-01, sigma gate = 8.4335e-01
      v =    120 km/s: k/m = 2.0014e-04, X: N(k)/N(0) - 1 = 2.4033e-07, gate exp(-k^2/mu^2) = 6.1221e-01, sigma gate = 3.7480e-01
      v =  171.3 km/s: k/m = 2.8570e-04, X: N(k)/N(0) - 1 = 4.8974e-07, gate exp(-k^2/mu^2) = 3.6792e-01, sigma gate = 1.3537e-01
      v =    300 km/s: k/m = 5.0035e-04, X: N(k)/N(0) - 1 = 1.5021e-06, gate exp(-k^2/mu^2) = 4.6573e-02, sigma gate = 2.1690e-03
      v =   1500 km/s: k/m = 2.5017e-03, X: N(k)/N(0) - 1 = 3.7552e-05, gate exp(-k^2/mu^2) = 5.0498e-34, sigma gate = 2.5501e-67
PASS  C4: the table of k/m, X's forward k-dependence 6k^2/m^2 + 6k^4/m^4, the amplitude gate exp(-k^2/mu^2) and the cross-section gate exp(-v^2/v*^2) at v = 50, 120, 171.3, 300, 1500 km/s reproduces (k = m v/2)  [[]]
PASS  C4: X's k-dependence is 2.4e-7 at 120 km/s and 3.8e-5 at 1500 km/s, where the gate exp(-k^2/mu^2) falls from 0.61 to 5e-34
PASS  C4: X's k-dependence reaches order one (6k^2/m^2 = 1) at v_rel = 2c/sqrt6 = 244780 km/s = 0.816c, 1429 times v_a (with k = m v/2)  [244779.52 km/s; read relativistically (gamma = 1 + 2k^2/m^2 = 4/3) the relative speed is 0.661c]
PASS  C5: on x in [1, 76.7] (v_a to 1500 km/s) the Chebyshev bound is 1/T_2(1.02643) = 0.90324; P* attains it (max|P*| = 0.90324 on a 200001-point grid, P*(0) = 1) and equioscillates (+, -, + at x = 1, mid, 76.7), so by de la Vallee Poussin no degree-2 P with P(0) = 1 stays below 0.903 in magnitude  [0.90324327; alternation [0.903243, -0.903243, 0.903243]]
PASS  C5: brute force agrees: convex minimization gives 0.90324; the record's random search (2e5 trials, seed 0) best max|P| = 0.90378, never below the bound  [0.90324327, 0.90378149]
PASS  C5: over the same range the Gaussian amplitude gate falls from 3.679e-1 to 5.050e-34
PASS  C19: contact Born benchmark sigma0 = 16 pi alpha~^2 m^2/m_phi^4 (alpha~ = 1, m_phi = m) = 3.9944e-24 cm^2: sigma0/m = 32.01 cm^2/g at 70 MeV, m = 71.5 MeV for 30 cm^2/g  [3.994356e-24 cm^2, 32.0096 cm^2/g, 71.529 MeV]
PASS  C8: a zero-energy state with 1/a = mu gives sigma(k -> 0) = 4 pi a^2 = 1.2233e-17 cm^2, sigma/m = 9.803e7 cm^2/g at 70 MeV, 3.27e6 times 30 cm^2/g  [1.22327e-17 cm^2, 9.80293e+07 cm^2/g]
PASS  C14: a preferred-frame vertex suppresses a pair moving at V by exp(-m^2 V^2/mu^2) = exp(-2V^2/v*^2): 2.559e-1, 4.705e-6, 4.899e-22 at V = 100, 300, 600 km/s  [2.5589e-01, 4.7046e-06, 4.8989e-22]
      [3.5 s]

== E. #6 s4's fiber overlap in field-theory terms (port of derivation-gate-mechanism/fiber_overlap.py; claims C1, C9-C11)
PASS  C1/C9: a bilinear's fiber coordinate is the average momentum; with k1 + k2 = k3 + k4 the fiber separation of the two bilinears is k1 - k4 (pairing 1->3, 2->4) or k1 - k3 (pairing 1->4, 2->3): a momentum transfer
PASS  C9: in the CM frame |k1 - k3|^2 = q^2, |k1 - k4|^2 = 4k^2 - q^2 (= q_u^2), |k1 - k2|^2 = 4k^2  [[q**2, 4*k**2 - q**2, 4*k**2]]
PASS  C9: R1's Born amplitude for identical chi is S(q) + S(q_u); at q -> 0 it is 1 + exp(-2k^2/mu^2) (#6's exp(-(p1 - p2)^2/2mu^2) is only the exchange term's forward value) and it tends to 1, not 0, at large k  [1 + exp(-2*k**2/mu**2); k -> oo: 1]
PASS  C9: as an operator R1 is x-local: (p, p') -> (P, Delta) has |Jacobian| = 1, the P integral gives 2 pi delta(y + y'), and St(y) = int dDelta e^{i Delta y} S(Delta) = sqrt(2 pi) mu exp(-mu^2 y^2/2), so V(r) = 2 pi St(r), a Gaussian of width 1/mu in position  [St = sqrt(2)*sqrt(pi)*mu*exp(-mu**2*y**2/2)]
PASS  C9: 1D quadrature for two wavepacket pairs: the phase-space overlap equals 2 pi times the exchange integral of V: 5.57550319 = 5.57550319 and 7.35636496 = 7.35636496 (imaginary parts < 1e-15)  [5.5755031948 vs 5.5755031948; 7.3563649581 vs 7.3563649581]
PASS  C9: the packet overlap (the mu -> 0 limit) is a state property: |<1|2>|^2 = 0.367879 at dp = 1 and at dx = 2 (sigma_x = 1), 0.778801 at dx = 1, 0.018316 at dp = 2, = exp(-dp^2/(4 sp^2) - dx^2/(4 sx^2))  [['0.367879', '0.778801', '0.367879', '0.018316']]
PASS  C11: R2's pair bilinear psi(x + y/2) psi(x - y/2) on plane waves has phase i(k_a + k_b) x + i(k_a - k_b) y/2: the vertex sees the pair's relative momentum (k_a - k_b)/2, and the separable amplitude g(k) g*(k') = |g(k)|^2 on shell is the gate
PASS  C10: tails: the pair-channel gate R2 falls faster than any power (k^n sigma -> 0, n = 2, 4, 8); R1 with Gaussian profiles has power-law tails, k^4 sigma_V -> 2 pi mu^4 (identical chi), k^2 sigma_T -> 2 pi mu^2 (distinct species); Yukawa k^4 sigma_T/ln k -> pi  [[0, 0, 0], 2*pi*mu**4, 2*pi*mu**2, pi]
PASS  C10: the table at k/mu = 0.5, 2, 5, 10 reproduces (R2 sigma_V, R1 identical sigma_V, R1 distinct sigma_T, Yukawa M_X = 2 mu sigma_T); at k = 10 mu R2 gives 1.159e-86 against R1's 6.252e-4  [[]]
      [5.1 s]

== F. The vacuum polarization under Lorentz transformations; a preferred frame (port of derivation-gate-mechanism/polarization_lorentz.py; claims C13, C14)
PASS  C13: the boost-rotation Lam (seed 1) is Lorentz (|Lam^T g Lam - g| < 1e-15; printed 4.4e-16); the algebra I^2 = -1, J^2 = 1, K^2 = 1, IJ = K holds for Lorentzian and Euclidean g  [4.44e-16]
PASS  C13: with Lorentzian g, omega, eta, K, J and H are all invariant under L = diag(Lam, Lam^-T) (residuals <= 1e-15; printed 2.5e-16, 2.5e-16, 3.2e-16, 8.9e-16, 7.8e-16), and H is not positive definite  [2.5e-16, 2.5e-16, 3.2e-16, 8.9e-16, 7.8e-16]
PASS  C13: the Born rotation rho = I flips K and J (rho K rho^-1 = -K, rho J rho^-1 = -J), preserves omega, and commutes with L (printed 8.9e-16): the vacuum breaks rho, not Lorentz symmetry  [0.0e+00, 0.0e+00, 0.0e+00; 8.9e-16]
PASS  C13: with positive-definite H (Euclidean g, as the compatibility theorem assumes) J and H are not Lorentz-invariant: |L J L^-1 - J| = 2.5, |L^T H L - H| = 2.9, |L rho L^-1 - rho| = 2.5; omega, eta, K still are  [2.5e-16, 2.5e-16, 3.2e-16, 2.5e+00, 2.9e+00]
PASS  C14: Galilean identity sum_i |mV + k_i|^2 = 4m^2 V^2 + 2|k|^2 + 2|k'|^2 (sympy) = 4m^2V^2 + 4k^2 for |k| = |k'|; numeric (seed 1) 4.5805875967 = 4.5805875967; so a per-leg profile exp(-|p_u|^2/4mu^2) gives exp(-k^2/mu^2) exp(-m^2V^2/mu^2)  [4.580587596682, 4.580587596682]

== G. Run 3's theory verifier (ports of verify-critic-theory/v3_gate_range.py, v6_medium_mediator.py; the J = 2 parts of v1_spinJ_residues.py; T3 of v7_misc_numbers.py)
PASS  gate-range (a): Gaussian sandwich symbol: [sqrt(F(p+a) F(p-a))]^2/[F(p) exp(-a^2/mu^2)]^2 = 1 in 1D and 3D, so W_A(x,p) = F(p) x (V smoothed by a Gaussian of width ~hbar/mu)
PASS  gate-range (b): all 72 printed ratios quantum/classical-gated and quantum/ungated reproduce (Gaussian and Lorentzian gates; V = exp(-|x|/300) and 1/sqrt(x^2 + 1); x0 = 3-1000 hbar/mu; p0 = 0, 1, 2 mu)  [[]]
PASS  gate-range (b): Gaussian gate, V = 1/sqrt(x^2 + 1): quantum/classical-gated = 0.996653, 1.003152, 1.000725, 1.000051, 1.000006, 1.000001 at x0 = 3, 10, 30, 100, 300, 1000 hbar/mu: non-relativistically the gate is not tied to contact range
PASS  gate-range (b): quantum equals the classical gated value within 3.4e-3 at 3-10 hbar/mu (worst 3.35e-3), 7e-4 at 30, 5e-5 at 100 (worst 5.1e-5, '1.000051'), and below 1e-5 from 300 on  [3: 3.35e-03, 10: 3.15e-03, 30: 7.25e-04, 100: 5.09e-05, 300: 5.57e-06, 1000: 2.78e-06]
PASS  gate-range (b): the gate survives at 1000 hbar/mu: quantum/ungated = 0.99313, 0.37039, 0.01921 at p0 = 0, 1, 2 mu (Gaussian; = the closed-form packet average exp(-p0^2/(1 + 2 sp^2))/sqrt(1 + 2 sp^2), sp = 1/12) and 0.99320, 0.50172, 0.20061 (Lorentzian)  [0.993127, 0.370390, 0.019214]
PASS  gate-range (c): 3D Gaussian gate on Coulomb V: the smoothed potential times r equals erf(r mu/hbar) at r = 0.5, 1, 2, 3, 10 hbar/mu (0.9999779095 at 3) to 10 digits  [2.9e-27]
PASS  gate-range (d): with v* = 120 km/s, mu c = m v*/sqrt2 = 19.813 keV, hbar/mu = 9.960e-12 m, x = c^2/v*^2 = 6.2414e6 = (mc/mu)^2/2  [19.81270 keV, 9.95962e-12 m, 6.241355e+06]
PASS  gate-range (d): mean chi spacing n^(-1/3) = 4.121e-3 m in a dwarf core (1 GeV/cm^3, n = 14.29/cm^3) and 5.593e-3 m locally (0.4 GeV/cm^3, n = 5.71/cm^3), far above hbar/mu
PASS  T6: a source moving at V through a mediator of speed c_s: the Heaviside ellipsoid 1/(4 pi sqrt(xi^2 + (1 - V^2/c_s^2) rho^2)) (V < c_s) and the Mach-cone field 1/(2 pi sqrt(xi^2 - (V^2/c_s^2 - 1) rho^2)) (V > c_s) solve the wave equation away from the source; V -> 0 gives Coulomb
PASS  T6: two bodies at zero relative velocity, both moving at V: side by side the force is 1/sqrt(1 - V^2/c_s^2) times static, 2 sqrt3/3 = 1.155, 10 sqrt19/19 = 2.294, 100 sqrt199/199 = 7.089 at V/c_s = 1/2, 9/10, 99/100; in line it is unchanged below c_s  [[2*sqrt(3)/3, 10*sqrt(19)/19, 100*sqrt(199)/199]]
PASS  T6: above c_s the trailing body feels twice the static force (2, for any V > c_s) while the side-by-side and leading bodies, outside the cone, feel none: action and reaction are unequal, so the dependence is on velocity through the medium, not between the bodies  [2]
PASS  c1 (J = 2, X's own residue): Fierz-Pauli contracted with point sources u1, u2 and an on-shell complex q orthogonal to both gives P_2(gamma) = (3 gamma^2 - 1)/2 = 2.315350 times static at gamma = 1.37; de Donder and the massless helicity sum give T_2(gamma) = 2 gamma^2 - 1 = 2.753800; static ratio massive/massless = 4/3  [2.3153500000, 2.7538000000, 2.7538000000]
PASS  c1 (J = 2): the (v/c)^2 coefficients are J(J+1)/4 = 3/2 (massive X) and J^2/2 = 2 (massless graviton); at v_rel = 120 km/s P_2(gamma) - 1 = 2.40332e-7 and T_2(gamma) - 1 = 3.20443e-7  [2.403324506e-7, 3.204432675e-7]
PASS  T3: for gravitational-strength exchange between 70 MeV chi, alpha_G = G m^2/(hbar c) = 3.287e-41 and the Bohr-type velocity alpha_G c = 9.855e-33 m/s: loops bring no scale near v* either  [3.287327e-41, 9.855159e-33 m/s]
      [6.7 s]

== H. The two derivations side by side (quantities both computed)
PASS  H1: run 4's forward numerator N_min(k,0)/N_min(0,0) = 1 + 6k^2/m^2 + 6k^4/m^4 is exactly run 3's spin-2 residue P_2(gamma) with gamma = p1.p2/m^2 = 1 + 2k^2/m^2  [gamma = 2*k**2/m**2 + 1]
PASS  H2: s - u = 4 p1.p2 + t, so run 4's pole variable z_t = (s - u)/(4m^2 - M_X^2) at t = M_X^2 is (4m^2 gamma + M_X^2)/(4m^2 - M_X^2) -> gamma as M_X/m -> 0: run 4's residue P_2(z_t) becomes run 3's P_2(gamma)
PASS  H3: X's velocity dependence at 120 km/s: run 4 (forward numerator, k = m v/2) 2.4033e-7 and run 3 (P_2(gamma) - 1, relativistic gamma) 2.40332e-7 agree to the quoted digits (they differ at O(v^4/c^4))  [2.40332422e-07 vs 2.40332450e-07, relative difference 1.2e-07]
PASS  H4: vDVZ in both: run 4's N_min(0,0) = 8m^4/3 against the massless (de Donder) numerator 2m^4 for the same vertices is 4/3, run 3's static ratio massive/massless 1.333333  [massless 2*m**4]
PASS  H5: the gate's nonlocality hbar/mu: run 4 9.87 pm (mu c = 20 keV), run 3 9.960 pm (v* = 120 km/s); they differ by 0.95%, exactly the ratio of the two readings of the record's mu = m v*/sqrt2 ~ 20 keV (121.1/120 km/s)  [9.8663 vs 9.9596 pm, ratio 1.009454]
PASS  H6: (m c/mu)^2: run 4 1.225e7 (mu c = 20 keV), run 3 2x = 2 c^2/v*^2 = 1.248e7 (v* = 120 km/s): the same quantity in the two conventions, ratio (121.1/120)^2 = 1.019  [1.22500e+07, 1.24827e+07]
PASS  H7: both find that spin-2 exchange grows with relative velocity and never gates: run 4's forward coefficients n1 = 64 F1^2 m^2, n2 = 64 F1^2 are >= 0 for real F1; run 3's P_2'(gamma) = 3 gamma > 0 for gamma >= 1
PASS  H8: both find a preferred frame (medium, slow mediator, or Lorentz-violating vertex) gives dependence on velocity through that frame at zero relative velocity, not on relative velocity: run 4's factor at k = 0, V = 300 km/s is exp(-m^2V^2/mu^2) = 4.7e-6; run 3's side-by-side force at V = c_s/2 is 1.155 times static

wall time 6.7 s

OK — every result of the gate-mechanism derivation reproduces.
```

## Sources

- `verify/gate_mechanism.py` — the docstring with its question, the two derivations, anchors, inputs and runtime; every check and label; its output — the 83 `PASS` lines of the run recorded above
- `notes/gate-mechanism.md` header — "Every number and algebraic result is recomputed in `verify/gate_mechanism.py`", the note's status and flag 55; §1 — the two conventions and flag 17; §§2–5 — the results the script reruns and their one-derivation marks; §6 — the two derivations, "it does not test their physics", and the second derivation's caveats
- `notes/velocity-gated-gravity.md` §9 — the spin-J residues and the medium, shared with block G
- `review/momentum-gravity/README.md` — the record: run 3's theory verifier and run 4's blind derivation, with their scripts
- `scripts/check.sh` — the script's place in the gate
- `CLAUDE.md` 'Layout' — the script listed with the momentum-gravity notes; 'Method (HANDOFF §5)' — the anchor rule
- `review/wiki-build-flags.md` items 17 and 55 — the √2 between the gate conventions; the mechanism not derived, with its audit, awaiting Paul's ruling
