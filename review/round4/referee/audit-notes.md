# Round 4 blind audit notes

Manuscript: round4/manuscript.md ("Spontaneous Breaking of Born Reciprocity in Two Toy Models")
Started 2026-10-19. Steps appended as completed.

## Step 1 — Citations (completed)

Method: INSPIRE API metadata for every ref (cites/*.json); arXiv e-print sources downloaded to dl/ and grepped for each attributed statement.

| Ref | Exists as cited? | Supports claim? |
|---|---|---|
| [1a] 1307.7080 PLB 730 302 | yes | yes: "both elements (eta,J) ... are dynamical. The solutions are labelled by bi-Lagrangians and spacetime is a derived dynamical concept" (main.tex l.395) |
| [1b] 1405.3949 IJMPD 23 1442006 | yes | yes: "we have to make eta dynamical" (l.232) |
| [1c] 1502.08005 JHEP06(2015)006 | yes | quote VERBATIM at FlatstringGM.tex l.141 ("if all probes agree ... broken Born duality --- there is a preferred choice of polarization, the space-time one"). grep "spontan" in [1a-c]: no symmetry-breaking analysis -> "no potential / no SSB analysis" consistent |
| [2] 1706.07089 JHEP11(2017)175 | yes | quote verbatim l.189, but the subject is "the kinematical structure of spacetime itself" (eta, omega), not literally "the choice"; acceptable paraphrase |
| [3] hep-th/0202039 PLB 533 168 | yes | yes (x<->p duality). NOTE: LS formulate it for a COMPLEX field in a magnetic field, with BOTH quartic vertices alpha Phi^+ Phi Phi^+ Phi and beta Phi^+ Phi^+ Phi Phi, as a single Fourier map Phi~(x)=sqrt|det B| Phi^(Bx), with theta -> theta~ = -B^-1 theta^-1 B^-1 (Prop. 1). The complex-field framing is LS's original |
| [4] hep-th/0402093 EPJC 35 277; hep-th/0401128 CMP 256 305 | yes | eq.(1) is the 4D form with prefactor pi^2 sqrt|det theta|; manuscript writes pi (2D adaptation) and attributes it to "[4, eq. 1]" without saying so (minor). Alternating sign: phi^(p_a)=int e^{(-1)^a i p_a x_a} phi(x_a), "a refers to the cyclic order in the star-product" -- CONFIRMED. GW state the real Omega=1 action "is invariant under the duality" -- the manuscript's "covariant only" is its own reinterpretation (assessed in step 2) |
| [5] hep-th/0612251 PLB 649 95 | yes | yes: "we compute the flow at the special LS dual point Omega=1, and check that the beta function vanishes at all orders" (l.124). This is the 4D model; model II is 2D |
| [6] 0709.3950 EPJC 53 459 | yes | non-constant vacua at Omega=1: yes (complex a f_{m0 n0}; real sum_k a_k f_kk, a_k^2=(mu^2 theta/4-2k-1)/(lambda theta)). "duality" appears only in the set-up (l.359-364): breaking not examined -- CONFIRMED. App. A matrix base matches manuscript's definitions (f00=2^{D/2}e^{-2H/theta}, a=(x1+ix2)/sqrt2, f_mn=(m!n!theta^{m+n})^{-1/2} abar^m*f00*a^n, H*f_mn=theta(m+1/2)f_mn) |
| [7] 0904.4664 JHEP09(2009)099; 1003.5027 JHEP07(2010)016 | yes | yes: HHZ "strong constraint ... equivalent to restriction ... to a maximally isotropic subspace"; closure of gauge transformations (l.721). HZ2009 uses the weak (L0-L0bar) constraint |
| [8] 1402.1686 JHEP05(2014)044 | yes | derived from CFT: yes (factorization of Virasoro-Shapiro amplitude). "selects a PAIR": OVERSTATED. BBLR eq. (micond)/(extcons): k_R = M k_L, M in O(d) -- a continuous family for d>=2; only for d=1, O(1)={+-1}, giving w=0 or p=0 (a pair). HHZ footnote: maximal isotropic subspaces "split into two classes", each an SO(D,D) orbit (continuum). So "every derivation selects the pair" is true only in d=1, where it is just the statement that R^{1,1} has two null lines |
| [9] PRL 17 1133; [10] CMP 31 259 | yes | yes |
| [11] hep-th/0312293 AHP 6 1025; hep-th/0405163 NPB 720 235 | yes, but first author of the second is A. Duncan (INSPIRE), not "N. Duncan"; erratum NPB 758 330 (2006) | yes: DNS abstract "(ii) the SO(1,N) symmetry is spontaneously broken. For D=2 this shows that the systems evade the Mermin-Wagner theorem." NOT APPLIED: model I's H-sector IS the SO(1,2)/SO(2) hyperbolic sigma model; Sec. 4's "In the exactly symmetric model the continuous breaking is forbidden [9,10]" ignores [11] for model I's own (non-amenable) Sp(2,R) |
| [12] PRB 16 1217 (1977) | yes (erratum PRB 17 1477) | abstract (INSPIRE/APS) treats hexagonal and cubic crystalline fields; no mention of the two-fold/Ising case. Full text paywalled -> specific claim UNVERIFIABLE |

URLs: https://inspirehep.net/api/literature?q=arxiv:<id> for each id above; sources https://arxiv.org/e-print/<id>; JKKN via q=doi:10.1103/PhysRevB.16.1217.

Omitted prior work found:
- Langmann, Szabo, Zarembo, "Exact solution of quantum field theory on noncommutative phase spaces", JHEP 01 (2004) 017, hep-th/0308043 -- exact solution of the complex model at a special self-dual point (U(infty) degeneracies); GW [4] themselves cite it as "closely related" to the Omega=1 model. Directly relevant to Sec. 4 restoration claim.
- L. Smolin, "Quantum reference frames and triality", arXiv:2007.05957 -- explicit cubic matrix model in which an extension of Born duality (triality) is spontaneously broken; partially undercuts "we found no explicit model".
- C.D. Fosco, G.A. Moreno, JHEP 11 (2007), arXiv:0710.0818 -- complex self-dual GW model, quantum effects around non-trivial (U(1)-breaking) minima; does not examine duality breaking (grep).
- V.E. Marotta, R.J. Szabo, Born sigma-models, arXiv:1910.09997 -- sigma models of Born geometry (polarization as target structure, not a field); relevant to "coset models of Born geometry".
- INSPIRE full-text searches 'fulltext:"Langmann-Szabo duality" and fulltext:"spontaneous"' (6 hits) and '"Born reciprocity" and "spontaneously broken"' (14 hits) found no prior explicit model with LS duality spontaneously broken by vacua.

## Step 2(a) — Model I (completed). Script: round4/ref_model1.py, output round4/out_model1.txt

CONFIRMED (sympy, generic symbolic S with det S=1, generic H, dH, K, dK):
- rho symplectic, rho^2=-1; H(Z) det 1; I^2=-1.
- all three terms Sp(2,R)-invariant: "transformed - original = 0" for H kinetic, K kinetic, potential; also invariant under K->-K.
- naive Tr(dK dK) at K0 = "2*db*dc" (indefinite); H-contracted at H=1 = "db**2 + dc**2"; random (H,dK) min ratio 0.0598 > 0 (positive definite).
- V(1,K) = "2*(b - c)**2" -> vacua K symmetric -> circle K(phi); V(1,K(phi)) = 0.
- rho^T H(Z) rho = H(-1/Z) (difference 0); fixed point Z=i gives H=1; rho^-1 K(phi) rho = K(phi+pi) = -K(phi).
- stabilizer: R(t)^-1 K0 R(t) = K0 only at t in {0, pi} -> {+-1}.
- Hessian of V at (1,K0) in (X,Y,b,c): rank 1, eigenvalues {3:1, 0:3} -> 3 flat directions.
- phi stiffness at H=1: (f_K^2/4)Tr(dK^T dK) = (1/2) f_K^2 (dphi)^2 -> matches (f_K^2/2)(dphi)^2.
- Sec. 4 potential at H=1: -mu[Tr(K K_ref)]^2 = -2mu(1+cos 2phi) (difference 0); rho-invariant for all K (difference 0).

DISCREPANT / NEW FINDINGS:
- (F1) The Sec. 4 rho-preserving potential is UNBOUNDED BELOW in model I. Along the lambda-flat family H=S(t)^T S(t), K=S(t)^-1 K0 S(t), S(t)=[[cosh t, sinh t],[sinh t, cosh t]] (symplectic: True): "lambda-term on family: 0", "V_mu on family: -4*mu*cosh(2*t)**2"; t=2: V/mu=-2982.96; t=4: V/mu=-8886112.5. Constant fields, so no kinetic cost.
- (F2) Consequently (H=1, K_ref) is a SADDLE, not a vacuum, once the potential is added: Hessian of V_lambda/8+V_mu at (1,K0) has eigenvalues [-3.3723, 0.0, 2.3723, 4.0] (lambda=mu=1); the negative mode persists for lambda=10 (-2.7797) and lambda=100 (-2.6785). The "two vacua K=+-K_ref" exist only if H is frozen at 1, which the manuscript asserts ("At H = 1 the polarization field is phi") but does not justify; H is a dynamical hyperbolic sigma field.
- (F3) The vacuum (1,K0) is invariant under the twisted element (rho, K->-K) -- "twisted rho on (1,K0): H -> [1,0,0,1], K -> [1,0,0,-1]". The model's full symmetry group is Sp(2,R) x Z2(K->-K) (both stated in Sec. 2); its stabilizer of the vacuum contains an element acting on H exactly as rho. Without matter couplings, "rho is broken" vs "K->-K is broken" is a labelling choice. (The Sec. 5 coupling I_K breaks K->-K explicitly, which removes the ambiguity -- but model I as defined has no matter.)
## Step 2(b) — Model II (completed). Scripts: ref_model2_base.py (out_model2_base.txt), ref_model2_vac.py (out_model2_vac.txt)

Independent anchors: differential Moyal product with "[x1,x2]_* = I" (theta=1); integral kernel sign fixed against the order-10 differential series (sigma=+1: |diff| 3.34e-09; sigma=-1: 1.77e-02); QM Weyl symbol of |m><n| from Hermite functions; GW eq.(1) definition read from source.

CONFIRMED:
- Laguerre form vs exact H-eigenrelations, m,n<=3: "True".
- f_mn*f_kl = delta_nk f_ml (exact Gaussian integrals, 20 index sets): max error 2.97e-140; f00*f00 - f00 = 0.
- Laguerre f_mn == Weyl symbol of |m><n| (independent QM construction): max error 5.63e-14 (m,n<=3).
- int f_mn = 2 pi theta delta_mn and orthogonality: errors 0.0 (exact).
- Duality, exact: with D_- f(x)=(pi theta)^-1 int e^{-i x~.y} f(y), x~=2 theta^-1 x, theta_12=theta: "D_minus f_mn / f_mn == (-1)^m for all m,n<=3: True" for theta = 1, 1/2, 3. The opposite sign of the exponent gives "(-1)^n: True". So D f_mn=(-1)^m f_mn is CONFIRMED for the manuscript's stated sign; the GW alternation = left parity on phi, right parity on the alternate factor.
  Novelty note: GW (hep-th/0401128) already say the duality is "manifest" in the matrix base; the explicit parity form follows from the classical parity-operator representation of Weyl symbols (Royer, PRA 15, 449 (1977), Crossref-verified to exist). Correct, but not a new structural fact.
- Quadratic form: off-diagonal max 0.0; diagonal/(8 pi) = m+n+1 for all m,n<=2 (exact).
- Real vs complex: Pi phi Hermitian? False; Tr phi^4 = 1230.31 vs Tr (Pi phi)^4 = 50.62; Tr (psi psi^+)^2 = 1230.31. Complex S[phi] = S[Pi phi] = S[U phi V^+] = 3539.2309815 (diagonal U,V); non-diagonal U gives 3657.12.
- Vacua: 6 random starts, N=8: all S_min = -2.5000000000, |offdiag| <= 7.7e-08, |phi_mm|^2 = [1.5 0.5 0 0]; beta scattered (0.33 ... 3.67). 200 extra restarts: lowest S = -2.49999999985 (no lower minimum).
- Flat phase: S = -2.500000000000 at 7 values of beta; duality maps beta -> beta+pi (all 7).
- Delta(beta) with D computed by direct 2D Fourier quadrature (not via Pi): Delta/Delta(0) = cos(beta) to 6 decimals at 9 angles; Delta(0) = +0.866025 = sqrt(3)/2 > 0 (beta=0 broader in position: <x^2>_vac=1.183 vs 0.317); zero at pi/2; Delta[D phi] = -Delta[phi] (0.66237 vs -0.66237). Sign convention CONFIRMED.

ADDITIONAL FINDING (supports the manuscript's real/complex distinction, but shows the "Goldstone angle" structure is model-specific):
- (F4) The real Omega=1 model (the GW model of [4]) has real diagonal vacua diag(+-a0, +-a1) (dGTW's sum_k a_k f_kk); for diagonal phi, Pi phi stays Hermitian, so the duality maps v+ = diag(a0,a1) to v- = diag(a0,-a1), classically degenerate (S_r = -2.5 both). But the fluctuation spectra differ: lowest Hessian eigenvalues v+: [2 2 2 4 4 4], v-: [0.5359 0.5359 2 2 2 4]; one-loop free energies differ by 2.634 (N=8). Complex model: max eigenvalue difference 0.0. So in the real model the polarization is a DISCRETE classical choice lifted explicitly at one loop -- not a Goldstone angle. The abstract's "in both models rho is one element of a continuous U(1), so the polarization is a Goldstone angle rather than a discrete choice" is true of the two models chosen, not of the GW model the duality literature is about.
## Step 2(d) — Sec. 5 (completed). Scripts: ref_sec5.py (out_sec5.txt), ref_sec5_fix.py (out_sec5_fix.txt)

CONFIRMED:
- eta = omega K(phi) symmetric, det -1; v(t)^T eta v(t) = sin(phi - 2t): zeros exactly at t = phi/2, phi/2+pi/2 (2 sign changes on [0,pi) for 3 random phi), = eigenlines of K (K e+ = e+, K e- = -e-). -eta has the same null lines; rho^-1 e+ is parallel to e- (cross = 0).
- Section condition, null coords: F(u),G(u) pair 0; F(w),G(w) pair 0; F(u),G(w) pair -F'G'; F(u)+G(w) with itself -2F'G' (box = 0); with -eta sign flips only.
- I_K, test state (hbar=1, unitary FT): I_(+K_ref) = 0.406972, I_(-K_ref) = 0.360047 -> quoted 0.4070 / 0.3600 CONFIRMED; reproduced independently from explicit Wigner-function marginals (0.406972 / 0.360047); int W = 1.0000, int W^2 = 0.1591549431 = 1/2pi.
- Combined map (psi -> F psi, K -> -K): I_-K[F psi] = 0.406972 = I_+K[psi]. (A first FFT-based attempt gave 23.27 -- my normalisation bug, fixed with a direct DFT; not a manuscript error.) K -> -K alone changes I by -0.046925.
- Rotation covariance (SO(2), H=1): I_{R K0 R^-1}[W_R] = 0.40673 vs 0.40697 (difference = interpolation error).

CAVEAT (F5): I_K is not defined by K alone. Same K0, eigenline parametrisation rescaled e+ -> 2 e1, e- -> e2/2 (du dv preserved): I = 0.813649 vs 0.406972. A scale on L+ (from H) is needed, so the coupling is covariant under the SO(2) stabilising H=1 (which contains rho), not under Sp(2,R). Calling it "K-covariant" overstates; it is (H,K)-covariant.
- "Locality" here is a quartic functional of a one-particle state, not an interacting field theory; the Yukawa analogy is heuristic. Claim correctly hedged in the text ("Nothing here forces matter to couple through K").
## Step 2(c) — Sec. 4 (completed). Scripts: ref_model2_quantum.py, ref_xy_mc.py, ref_xy_trap.py, ref_sec4_extra.py (outputs out_*.txt)

Model II restoration argument:
- Exact phase decoupling CONFIRMED and stronger than stated: S is invariant under independent diagonal U, V (N=10: S = 7638.11944458 at 5 random (U,V)); every condensed level's phase is an independent exact flat direction. So <Delta>=0 at any truncation follows from symmetry alone, and no beta-dependence can be generated at any loop order. The "tunnelling" caveat is only needed for the add-a-potential variant.
- Logical gap: <Delta>=0 at finite truncation holds for ANY symmetric finite system and is not by itself an argument against SSB; the operative point is that beta is one compact collective coordinate with O(1) action (no volume factor), so lim_{h->0} lim_{N->inf} <Delta>_h = 0. The manuscript's "nothing couples beta across space" gestures at this; the condensate is a localised lump (dGTW: "decays at infinity ... finite linear combination of Schwartz functions"), so a thermodynamic limit with an intensive order parameter never existed. Conclusion CONFIRMED in substance; argument should be restated.
- (F6) "Increasing the truncation adds only massive levels" omits mass renormalisation. One-loop: d^2 Tr((phi^+phi)^2)/dphi00 dconj(phi00) averaged = "4*G00 + 2*G01 + 2*G02 + 2*G10 + 2*G20" (N=3), i.e. 2 sum_k (G_0k + G_k0); with G_ij = 1/(i+j+1+M^2): T_0(N) - 2 ln N -> -0.8455 (N=10^5), i.e. the tadpole grows as 2 ln N. At fixed bare mu^2 the low-level condensate is destroyed at large N; mu^2 must be renormalised with N. Does not change the no-SSB conclusion.

Model I in 1+1, Monte Carlo (own checkerboard Metropolis, own seeds):
| Run | manuscript | referee |
|---|---|---|
| h=1, T=0.6, <|m|> L=16/32/64 | 0.954 all; U=0.667 | cold: 0.9541 / 0.9543 / 0.9542, U = 0.6666 / 0.6667 / 0.6667 ; hot L=16,32 identical |
| control T=3.0 | 0.078 -> 0.033 -> 0.014 | 0.0630+-0.0004 -> 0.0318+-0.0004 -> 0.0156+-0.0002 (m*L = 1.007, 1.018, 0.997) |
| h=0, T=0.6, <|M|> | 0.838 -> 0.798 -> 0.776, ratio 0.925 | 0.8371 -> 0.8040 -> 0.7673, ratio 0.9166 |
- Ordered phase with potential: CONFIRMED (0.954, Binder 2/3).
- Caveat: hot start at L=64 did not equilibrate in 6000 sweeps: <|m|> = 0.0593 (U=0.536); diagnostic runs: hot seeds 1064/77 E/site = -2.58524 / -2.61222 (<|m|> 0.0265 / 0.6052, winding ~0), cold E/site = -2.67587 (<|m|> 0.9541). Metastable domain stripes with higher energy; equilibrium is ordered. Manuscript does not state its start condition; results from a cold start alone would be partly by construction.
- Control: same magnitude and qualitative reading (disordered), CONFIRMED qualitatively; but the quoted sequence scales as L^-1.239 vs the 1/L expected and found (referee exponent -1.0069); quoted L=16 value is 1.238x the referee's (0.078 vs 0.0630+-0.0004). Minor: likely under-sampled; NOT REPRODUCED to the stated precision.
- h=0: decreasing with L, no true order: CONFIRMED. Values agree at L=16; L=32/64 differ by ~0.006-0.009 (3-4 binned sigma, binned errors likely underestimated for Metropolis autocorrelation at L=64). Ratio 0.926 (manuscript) / 0.917 (referee) vs spin-wave 0.936: both below spin-wave, as expected from stiffness renormalisation (referee fitted exponent -0.0628 vs bare -0.0477).
- Spin-wave formula CONFIRMED: lattice Gaussian sum gives M(64)/M(16) = 0.9359 vs closed form (64/16)^(-T/4piJ) = 0.9360.
- "Ising-class": data at a single T deep in the ordered phase establish order only, not universality class. Minor wording.
- Residual symmetry once the potential is added (sympy): S^-1 K_ref S = +K_ref -> S = diag(a, 1/a); = -K_ref -> S = [[0, -1/c],[c, 0]]. So the potential leaves a NON-COMPACT boost subgroup unbroken plus {+-1, +-rho} (Z4) in SO(2). Combined with F1/F2: in model I proper, the boost direction is where the potential runs away.
## Step 3 — Conceptual audit (completed). Extra script: ref_fix_potential.py (out_fix_potential.txt)

Internal consistency
- (C1) Sec. 2 lists K->-K as a symmetry, but the stabilizer is computed in Sp(2,R) only. In Sp(2,R) x Z2 the vacuum (1,K0) is fixed by (rho, K->-K) (F3). Sec. 2's "no vacuum is rho-invariant" is true for rho alone; "Born reciprocity is broken" in model I is a labelling choice until a K-odd coupling (Sec. 5's I_K: K->-K alone changes it by -0.046925) is added. On the H=1 circle rho and K->-K act identically (K(phi) -> K(phi+pi) = -K(phi)).
- (C2) Sec. 1 cites [11] ("non-amenable groups are an exception"); Sec. 4 then states "In the exactly symmetric model the continuous breaking is forbidden [9,10]". Model I's group Sp(2,R) is non-amenable and its H-sector is the SO(1,2)/SO(2) hyperbolic sigma model for which DNS [11] report spontaneous breaking in D=2 ("For D=2 this shows that the systems evade the Mermin-Wagner theorem"). The statement must be restricted to the compact SO(2) containing rho, with an argument.
- (C3) Sec. 4's potential is written for the full model but analysed at H=1; in the full model it is unbounded below (F1) and (1,K_ref) is a saddle (F2). The Monte Carlo is of the textbook XY + two-fold-field model with H frozen, not of model I. Sec. 6's "Ising-class breaking of rho in model I in 1+1" is therefore not established. A bounded variant exists: V' = -mu[Tr(K K_ref)]^2/(2 Tr(K^T K)) gives min V'/mu = -0.99999913, max = -1.26e-05 over 141227 hyperboloid samples, max |V'(rho K) - V'(K)| = 2.2e-16, and on the runaway family V'/mu = -1/2 - 1/(2 cosh 4t) -> -1/2. But it uses the Euclidean Tr(K^T K), which breaks the residual boosts explicitly; the vacuum analysis with H dynamical would have to be redone.

Is "spontaneous breaking" fair for model I in 1+1?
- With H frozen: yes, standard Ising-type SSB of the residual Z2 = <rho>/<rho^2> (the potential's SO(2) residue is {+-1, +-rho}, sympy). But the potential fixes the unordered axis pair by hand, so the vacuum chooses only which of two pre-set axes is "position". The manuscript says this in Sec. 6 ("rigid unordered pair of axes"); the abstract's "rho is spontaneously broken" should carry the qualifier and the frozen-H caveat. With H dynamical as written: not established (C3).

Model II
- Correct conclusion (no SSB), but the strongest reason is the exact U(1)^N x U(1)^N invariance (every condensate phase decoupled) plus the absence of a volume factor (the condensate is a localised Schwartz-class lump). "Classical breaking" of a zero-dimensional degeneracy is weak language. The tadpole grows as 2 ln N (F6), so "fixed mu^2" needs renormalisation.
- The structural claim "in both models rho is one element of a continuous U(1)" is true for the two models chosen; the real GW model, where the duality literature lives, has a discrete classical pair of duality-related vacua whose degeneracy is lifted at one loop (F4: free energies differ by 2.634 at N=8). The abstract's generalisation ("so the polarization is a Goldstone angle rather than a discrete choice") should be restricted.

Novelty claims
- "No explicit model": no prior explicit model with LS duality broken by vacua, or with eta=omega K as a dynamical order parameter, turned up in INSPIRE full-text searches (step 1). Smolin, arXiv:2007.05957, gives an explicit cubic matrix model in which an extension of Born duality (triality) is spontaneously broken; it must be cited and distinguished.
- "We compute the LS duality on the matrix base": correct (step 2b), but GW (hep-th/0401128) already state the duality is "manifest" in the matrix base, and the parity form follows from the parity-operator representation of Weyl symbols (Royer 1977). Present as a lemma.
- "Real covariant, complex symmetric": LS's original duality (Prop. 1) is formulated for complex fields; LSZ (hep-th/0308043) solve a closely related complex model exactly. Partly prior art; LSZ is the natural check for the restoration claim and is not cited.
- Coset models of Born geometry: Marotta-Szabo Born sigma-models (1910.09997) treat Born geometry as target structure, not as dynamical (H,K) fields; INSPIRE '"Born geometry" and coset and "order parameter"' returned 0. Model I appears new as a field theory, but it is a simple coset (vacuum manifold PSL(2,R)).

Matter locality (Sec. 5)
- Mostly hedged correctly ("A mechanism that forces such a coupling is not provided"). Over-reach: (i) "agrees with the DFT literature, where every derivation selects the pair [8]" -- BBLR give an O(d) family; a pair only for d=1; (ii) I_K needs H to normalise the measure on L+ (F5); (iii) "consistency confines matter" -- the section condition is imposed, not derived, in this paper.
## Step 4 — Verdict (completed)

GRADE: B (flawed but salvageable). Confidence ~0.75.
Reason: the algebra and numerics of Secs. 2, 3, 5 reproduce. But the paper's only claim of actual (quantum) spontaneous breaking -- Ising-class breaking of rho "in model I in 1+1" -- rests on a potential that is unbounded below in model I and on freezing H=1. In model I the vacuum also keeps an unbroken element acting on H exactly as rho. Both are repairable (bounded potential plus a K-odd coupling, or an honest restriction to a frozen-H toy), so B rather than C.

SINGLE WEAKEST LINK: Sec. 4's rho-preserving potential -mu[Tr(K K_ref)]^2. In model I it gives V = -4 mu cosh^2(2t) along the lambda-flat family, so (1, K_ref) is a saddle (Hessian eigenvalue -3.37). The Monte Carlo therefore tests a frozen-H XY model, not model I.

Indictments resting on executed code: all numerical/algebraic ones (F1-F6, MC control, hot-start trapping, residual symmetry). Citation and omission indictments rest on retrieved sources (INSPIRE API, arXiv e-print sources), none from memory.
