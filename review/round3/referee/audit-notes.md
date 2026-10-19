# Round-3 blind audit notes

Working dir: round3/. Downloads in round3/dl/ (untrusted data, separate dirs). Scripts: cite_fetch.py, pdfgrep.py, and step*.py.
Raw INSPIRE metadata: dl/inspire.json. Abstracts via arXiv API (dl/arxiv_abs.xml); full texts via arXiv PDFs + pypdf.

## Step 1 - Citations

Method: INSPIRE API query per reference (script cite_fetch.py; output quoted in report), arXiv abstracts,
and full-text grep of the PDFs (pdfgrep.py) for the specific claim each reference is cited for.

Bibliographic metadata: ALL 23 references (37 individual items) resolve on INSPIRE with matching
authors / journal / volume / page / year / arXiv id. No fabricated or mis-numbered reference found.
(Kolb & Turner resolves as Front. Phys. 69 (1990), Addison-Wesley; PDG 2024 review confirmed as
"95. Magnetic Monopoles, revised March 2024 by D. Milstead and E.J. Weinberg", pdg.lbl.gov/2024/reviews/rpp2024-rev-mag-monopole-searches.pdf.)

Support for the specific claims:

- [1] Born 1938 / 1949: metadata OK (DOI 10.1098/rspa.1938.0060; 10.1103/RevModPhys.21.463). 1938 abstract does not
  state the rule; primary text paywalled. Secondary sources (Wikipedia "Born reciprocity") confirm x->p, p->-x.
  Fourier-transform statement is standard maths. PARTIALLY VERIFIED (primary text not read).
- [2] Boulanger et al.: abstract: "no consistent (ghost-free) coupling, with at most two derivatives ... that can mix the
  various gravitons". SUPPORTS "massless X coupled to gravity is excluded" (caveats: 2-derivative, local, ghost-free).
- [3] Hassan-Rosen x2: SUPPORTS ghost-free (bi)metric structure.
- [4] Comelli et al. (exponential Jeans-like instability in 2nd branch), Koennig et al. (instabilities for several classes),
  Lagos-Ferreira (generally exponential instabilities). SUPPORTS "find gradient or ghost instabilities", BUT
  slight over-generalisation: Koennig et al. abstract identifies a STABLE model (infinite-branch bigravity), and Lagos-Ferreira
  find stable scalar perturbations for a particular parameter choice. The "m ~ H0 and comparable Planck masses" premise is
  consistent with [5]'s framing ("Previous work has suggested ... generically plagued by instabilities").
- [5] Akrami et al.: SUPPORTS. Text p.7: "the alpha->0 limit brings bimetric theory arbitrarily close to GR even for ...
  m >> H0. The presence of heavy spin-2 fields ... is therefore not excluded as long as ... M_f is sufficiently small".
- [6] Higuchi: abstract "M^2 cannot be between 0 and 2/3 x (cosmological constant)"; with Lambda = 3H^2 this is m^2 >= 2H^2. SUPPORTS.
- [7] Dirac 1931; Zwanziger 1968: SUPPORTS the antisymmetric DSZ pairing. Minor normalization mismatch: Zwanziger's abstract
  states e_m g_n - g_m e_n in 4 pi Z; manuscript writes 2 pi Z (Dirac normalization). The 't Hooft-Polyakov monopole with
  doublets realises 2 pi, so the physics is fine; but [7] as cited states 4 pi. "Charge space is symplectic" is interpretation.
  Note the text says "Dirac-Schwinger-Zwanziger" but Schwinger is not cited.
- [8] Montonen-Olive, Osborn, Harvey: SUPPORTS. Harvey: "put to non-trivial tests in finite N = 4 Super Yang-Mills theory and
  special finite N = 2 theories"; "there is no reason to think that the duality of the spectrum should be maintained by
  quantum corrections" (for the non-SUSY BPS-limit theory).
- [9] Gherghetta et al.: SUPPORTS both parts. p.5: "If C_A and C_X are separately good symmetries ..., then kinetic mixing cannot be
  induced at any perturbative order"; abstract: "kinetic mixing through gravity alone, requires at least six loops and could be as
  large as ~1e-13" (conditional on C_X breaking and O(1) hidden Yukawa). Note: Gherghetta et al. present 1e-13 as a FLOOR
  ("minimum kinetic mixing in any theory with hidden gauge interactions and charge symmetry breaking"), consistent with "<~" only
  in the sense "up to".
- [10] Dim-5 operator Phi^a F^a B / M_*:
  - Baumgart et al. 0901.0283: DOES NOT SUPPORT. Its mixing is the renormalizable B_mu-nu b^mu-nu with a dark U(1) factor:
    "Since G_dark must contain a U(1) factor, the minimal choice is ... SU(2) x U(1)" (p.5). No adjoint dim-5 operator found
    (grep "dimension five/5", "non-renormalizable": no hits relevant).
  - Chen-Cline-Frey 0907.4746: SUPPORTS existence (eq. 1: sum_i (1/Lambda_i) Y_mu-nu B^mu-nu_a Delta^a_i) BUT "The dimension-5 operator (1)
    can be induced at one loop by a heavy particle X which carries both dark SU(2) charge and weak hypercharge" (p.3).
  - Bruemmer-Jaeckel 0902.3615: SUPPORTS chi = v/M (their eq. 25) for -(1/2M) Q^a G^a F, AND generates it from a loop of a field
    charged under BOTH groups: 1/M = e f h/(6 pi^2 m0) (eq. 28).
  - Gherghetta et al. Sec. 3.2.3 (non-Abelian dark sector, adjoint scalar): eps ~ g_X g' y_Sigma/(16 pi^2) <Sigma>/Lambda.
  => [10] is cited for more than it says: all sources that derive the operator obtain it from bi-charged states with a one-loop factor
     ~ g g' y/(16 pi^2), not an O(1) coefficient at M_Pl; and bi-charged states are what the manuscript's sector-separation postulate excludes.
- [11] Banks-Seiberg, Harlow-Ooguri: SUPPORTS "no exact global symmetries in quantum gravity".
- [12] Hiramatsu et al.: SUPPORTS (abstract): "The dark monopole ... does not induce the QED magnetic flux in the U(1) symmetric
  phase, even in the presence of the kinetic mixing."
- [13] Terning-Verhaaren: SUPPORTS (p.11): with a massive dark photon, "dark magnetic charges get an eps e/4pi coupling to the massless
  photon", and dark monopoles are confined by flux tubes.
- [14] Bruemmer-Jaeckel-Khoze: SUPPORTS (abstract): with CP violation, monopoles acquire hidden electric charge (Witten effect) and
  "quite generally they also acquire (small) electric charges under the visible electromagnetic gauge group". Also: "Both kinetic and
  magnetic mixing are naturally induced radiatively".
- [15] 't Hooft, Polyakov: SUPPORTS (abstract: monopole mass of order 137 M_W).
- [16] Prasad-Sommerfield, Bogomolny: SUPPORTS f = 1 (BPS). The value f ~ 1.79 at large self-coupling is NOT in [16] and is uncited
  (checked numerically in Step 2 instead).
- [17] Kolb & Turner (book): standard; not checked page-level.
- [18] Kibble 1976: SUPPORTS (abstract: formation of walls, strings or monopoles depends on homotopy groups).
- [19] Preskill 1979: abstract "density of such monopoles in the early universe is estimated to be unacceptably large". Consistent with
  "annihilation inefficient". SUPPORTS (abstract-level).
- [20] PDG 2024 (Milstead & Weinberg), eq. (95.9): Parker F < 1e-15 cm^-2 sr^-1 s^-1 for M <~ 1e17 GeV. SUPPORTS.
  TPB 1982 / Parker 1970: metadata OK. (TPB abstract quotes "F <~ 1e-16" as the "Parker limit" - different from the PDG 1e-15;
  the manuscript follows PDG; fine.)
  PDG eq. (95.8) also states that a Dirac-charge monopole of M >~ 1e11 GeV is accelerated by the Galactic field to
  v ~ 1e-3 c (1e17 GeV/M)^(1/2) - relevant to the counterfactual flux (Step 2).
- [21] MACRO final: Table 2: "<= 2.8e-16 for m >~ 1e10 GeV, beta > 1e-4"; global 1.4e-16. SUPPORTS the 2.8e-16 figure exactly.
- [22] Adams et al. 1993: abstract "F <= 1e-16 (m/1e17 GeV) cm^-2 s^-1 sr^-1". SUPPORTS exactly.
  (PDG eq. 95.10 adds a +3e-6 term inside the bracket - negligible here.)
- [23] Planck 2018 VI, eq. (67b) p.50: "N_eff = 2.99 +0.34 -0.33 (95%, TT,TE,EE+lowE+lensing+BAO)". SUPPORTS.
  Planck uses N_eff,SM = 3.046 (text p.49).

Uncited claims / prior art that should be cited:
- The compatibility theorem is the known "Born geometry" structure of Freidel-Leigh-Minic: 1502.08005 (JHEP 06 (2015) 006), p.11:
  "If, in addition, we assume that B vanishes we have that I is a complex structure and that JK = -KJ. Phase space geometries
  that have I,J,K satisfying these conditions were referred to as Born geometries". Not cited.
- f ~ 1.79 for lambda -> infinity (uncited; checked numerically in Step 2).
- "thawing, never-phantom dark energy, currently consistent with hints of weakening dark energy in recent BAO data": uncited.
- Prior hidden-monopole DM literature not cited (see Step 4c).
- Kibble "one per horizon" normalisation: Gangui astro-ph/0110285 p.14: "about one monopole per Hubble volume ...
  n_monop/s ~ 100 (T_c/m_P)^3" (used in Step 2 against the manuscript's p ~ 0.023).

## Step 2 - Numbers (all from executed code; outputs in step2a.out, step2b.out, step2b_inf.out, ggww.out, step2c.out, step2c_psi.out, step2c_thr.out)

Own constants: alpha^-1=137.035999; alpha_hat(MZ)^-1 = 127.930 (PDG 2024 EW review); MPl=1.220890e19 (PDG 2024 astro);
rho_c/h^2=1.053672e-5 GeV/cm^3; s0=2891.2/cm^3 (PDG 2024 astro); Omega_c h^2 = 0.120 (Planck 2018); N_eff 95% from Planck eq. 67b.
Manuscript inputs checked: rho_DM = 1.264 keV/cm^3 (OK), s0 ~2.9e3 (OK), MPl 1.22e19 (OK); local 0.4 GeV/cm^3 (PDG canonical 0.3, x2-3).

| Claim | Manuscript | Mine (code) | Verdict |
|---|---|---|---|
| alpha_W' under H | 4 alpha ~ 1/34 | 1/34.259 | CONFIRMED |
| alpha_m | ~34 | 34.259 | CONFIRMED |
| W'-charge variant | ~137 | 137.036 | CONFIRMED |
| running to 1e12 GeV | ~29 | 28.61 (MSbar 127.930), 28.86 (128.95) | CONFIRMED |
| (extra) psi matched to e/3 | not considered | 308.3 | missing variant |
| f at large lambda | ~1.79 | 1.7867 (own BVP; BPS check E=1 with tail) | CONFIRMED |
| M = (21-37) v | | 20.75 - 37.07 | CONFIRMED |
| v at 3e13 | (0.8-1.4)e12 | 8.09e11 - 1.446e12 | CONFIRMED |
| m_W' | (5-9)e11 | 4.90e11 - 8.76e11 | CONFIRMED |
| W' overclosure | 1e16-1e17 (coef x10 bracket) | c=1..10: 9.4e15-1.95e17; with c=6.67 (W+W- -> gg at threshold, own detailed balance of hep-ph/9405359 eq. 5.15; scalar check gives textbook 2.000): 1.3e16-4.0e16 | CONFIRMED (bracket reasonable) |
| Kibble p for one per horizon | 0.023 | 104.3 (n=H^-3), 24.9 ((4pi/3)H^-3); 0.0228 = 45/(2pi^2 100) i.e. H^3 without (1.66 sqrt g*)^3 = 4576 | DISCREPANT (factor ~1e3-5e3) |
| M* band (manuscript inputs) | (0.9-3.7)e13 | 0.918e13 - 3.644e13 | arithmetic reproduces, but rests on wrong p |
| M* band with correct p | | 2.87e12 - 4.44e12 (H^-3); 4.11e12 - 6.35e12 ((4pi/3)H^-3) | DISCREPANT |
| benchmark 3e13 "no dilution" | | overproduced by (M/M*)^4 = 2.1e3 - 1.2e4 (Kibble minimum) | DISCREPANT |
| reduced-Planck factor | ~3 lower | 3.350 | arithmetic OK, but it is a convention artefact, not a physical spread (p must be recomputed consistently) |
| dilution at 1e16 | ~1e10 | 1.24e10 (vs M*=3e13); 2.6e13 vs corrected M* | arithmetic OK, input M* wrong |
| xi^(3/4) at bound | 0.8 | 0.822 (xi=0.77), 0.814 (xi=0.76) | CONFIRMED |
| psi window: <10% DM | m_psi < 0.1-0.3 TeV | 10% at 28.3 GeV (xi0=1), 34.9 GeV (xi0=0.76), 45.9 GeV (xi0=0.5) | DISCREPANT (factor 3-10 in mass) |
| psi = all DM | 0.3-1 TeV | 96 GeV (xi0=1), 118 GeV (0.76), 153 GeV (0.5) | DISCREPANT |
|   (psi code validated: standard 100 GeV WIMP 2.2e-26 -> Omega h^2 = 0.1145; single Dirac visible-like 0.0285; two species + hidden reheating of gamma' by psi annihilation, T_h/T -> 1.85 at freeze-out) | | | |
| mean n at 3e13 | 4.2e-20 | 4.215e-20 | CONFIRMED |
| local volume / spacing | 0.075 km^3 / 420 m | 0.0750 km^3 / 421.7 m (0.3 GeV/cm^3: 0.100 km^3, 464 m) | CONFIRMED |
| counterfactual flux | 3e-8 | 3.18e-8 (v=1e-3c) | CONFIRMED |
| excess over Parker / MACRO / ext. Parker | 7.5 / 8 / 12 orders | 7.50 / 8.06 / 12.03 | CONFIRMED |
| (extra) PDG eq. 95.8 galactic acceleration v=0.058c | not used | F=1.84e-6; 9.3/9.8/13.8 orders | conclusion strengthened |
| eps ~ v/M_* | 1e-7 - 1e-6 | 6.6e-8 - 5.9e-7 | CONFIRMED as arithmetic (order of magnitude) |
| eps with one-loop UV factor g_d g' y/16pi^2 | not considered | 1.37e-3 x -> 9e-11 - 8e-10 | the cited sources' own estimate is 3 orders smaller |
| Delta N_eff (shared T) | 0.86 | 0.8567 | CONFIRMED |
| xi bound | < 0.77 | 0.760 (N_SM=3.044), 0.759 (3.046); 0.769 only if DeltaN<0.30 | minor DISCREPANCY (should be 0.76) |
| sigma_T/M | ~1e-26 cm^2/g | 0.95e-26 - 2.9e-26 (manuscript formula); standard 4 pi a^2 lnL/(mu^2 v^4) gives half; ~25.7 orders below 1 cm^2/g | CONFIRMED (factor-2 convention) |
| GW peak | 1e5 - 1e7 Hz | 1.35e5 - 2.47e7 Hz | CONFIRMED |

Brackets: annihilation coefficient factor-10 bracket - reasonable (my W'W'->g'g' threshold coefficient 6.67 pi a^2/m^2 lies inside 1-10; extra channels h'h', g'h' push up).
f in [1, 1.79] - correct physical range (BPS to lambda->inf). p in [0.023, 1] - NOT reasonable: Kibble's one-per-horizon is a causal LOWER bound
(Gangui astro-ph/0110285: n/s ~ 100 (T_c/m_P)^3; LMW 2607.20843 Sec. III: "minimal number density ... one per Hubble volume";
Kibble-Zurek gives n ~ lambda H T_c^2, i.e. (M_Pl/T_c)^2 per horizon), so p should be >= ~25-100, not <= 1.

## Step 3 - Compatibility theorem (step3.py -> step3.out; step3_groebner.py; step3_diag.py)

Setup: omega=[[0,1],[-1,0]], eta=[[0,1],[1,0]] (d x d blocks), H=[[A,C],[C^T,B]], A,B symmetric, C general.
Symbolic (sympy, d=1,2; diagonal identities also d=3):
- "(2,1) block of (eta^-1 H)^2 - 1 == A C^T + C A : True" and "(2,1) block of (omega^-1 H)^2 + 1 == C A - A C^T : True" (d=1,2).
  Sum = 2CA, difference = 2AC^T: True. So the manuscript's block equations are exactly right.
- With C=0 the remaining equations reduce to BA=1 and AB=1: True.
- d=1 full solve: single branch C=0, A=1/b0, B=b0.
- d=2: sympy.solve returned 0 branches (solver failure, not a counterexample); Groebner basis instead:
  with t*det(A)-1 adjoined, normal forms of c0..c3 and of all entries of BA-1 are 0 => algebraic proof C=0, B=A^-1.
  WITHOUT the invertibility/positivity assumption, c0 is still in the ideal (True) and 1 is not (solutions exist).
- Diagonal blocks (d=1,2,3): E1+E2 = 2 (C^T)^2 and E1-E2 = 2(BA-1): True. Hence BA=1 follows from the diagonal blocks alone,
  A is automatically invertible, and CA=0 then gives C=0. Positivity is NOT needed for C=0 (only for g>0).
Numerical (d=3,4; 2000 trials per family):
- diag(g,g^-1): max residuals 4.7e-15 (d=3), 8.4e-15 (d=4); det H = 1.
- generic SPD H with C!=0: min over trials of max residual = 21.0 (d=3), 83.5 (d=4): always violates at least one.
- eta-only family (O(d,d) generalized metric with B-field): eta residual <= 7e-14 but omega residual >= 0.28 (d=3), 1.48 (d=4).
- omega-only family (Siegel, X != 0): omega residual <= 3e-14 but eta residual >= 0.52 (d=3), 1.87 (d=4).
- perturbing diag by C of size 1e-4 gives residuals ~1e-3: the solution set is isolated as claimed.
VERDICT: theorem TRUE; stated proof VALID (uses positivity where it is not needed; slightly weaker hypothesis suffices).
It is essentially the known Freidel-Leigh-Minic "Born geometry" statement (B-field vanishes <=> I = H^-1 omega compatible),
uncited (1502.08005 p.11). It is a pointwise linear-algebra fact; it does not by itself establish any physics
(the identification of a dynamical H, a rigid eta, and a second spin-2 field X is assumed, not derived).

## Step 4 - Conceptual audit (code: step4.py -> step4.out; step4b.py -> step4b.out; step4c.out)

### 4(a) Internal consistency
1. Kibble normalisation vs "upper end": p = 0.023 is the H^3 abundance with the 1.66 sqrt(g*) factor dropped (step2a.out:
   "45/(2 pi^2 * 100) = 0.0228"). One per Hubble volume is p = 104.3 and is a causal LOWER bound. Corrected Kibble-minimum
   M* = 2.87e12-4.44e12 GeV (xi=1), 2.34e12-3.61e12 GeV (xi=0.76); benchmark 3e13 overproduced by 2.1e3-2.7e4 (step4b.out).
   The abstract's "no dilution required" fails at the benchmark.
2. Sec. 4 GW paragraph contemplates a first-order transition with f*/H* = 1-100; bubble counting gives p ~ 104 (beta/H)^3 = 1e2-1e8
   (step4.out) - flatly inconsistent with "p = 1 as the upper end" of Sec. 3.
3. Second-order (Kibble-Zurek) production n ~ lambda H T_c^2 (LMW 2607.20843 eq. 13) followed by diffusive + radiative capture
   (LMW eqs. 16,18,28) at the manuscript's own parameters (h=20.75, e_psi=0.303, b_psi=0.183, b_W'=0.548): Y_final ~ 1.7e-11 - 3.2e-11,
   Omega/Omega_DM = 1.1e12 - 2.2e12 (step4.out). LMW analytic eq. (25) at these parameters: 1.2e9 - 2.2e11. Either way the
   annihilation does not rescue it. Kibble-minimum initial Y (7e-20 - 1.4e-18) is far BELOW the annihilation attractor, so annihilation
   is irrelevant in that case and overproduction 4.9e3 - 9.8e4 (xi=0.76..0.5) stands.
   => Acceptance criterion 3 is not open: the "strong-coupling" regime alpha_m = 34 is exactly the Dirac-monopole case of
   Preskill 1979 (h = 2 pi/e); its modern hidden-sector version (LMW 2026) excludes v >~ 100 PeV for hidden monopoles.
4. Colder hidden sector: W' overclosure survives (xi=0.76: 9.9e15 - 2.9e16, step4b.out); the M* band is quoted at xi=1 while xi<0.76 is required
   (the xi^(3/4) shift is stated, the band is not updated). psi window computed with hidden temperature (step2c_thr.out): 10% DM at 35 GeV
   (xi0=0.76) - the manuscript's "below about 0.1 TeV" would make psi ~70-100% of DM (step2c_psi.out: 73.1% at 100 GeV, xi0=0.76).
5. Requirement (ii) xi<0.77 vs the psi millicharge: with eps = 1e-6 the SM freeze-in of psi reaches equilibrium for all m_psi <= 30 GeV
   (Y_FI/Y_eq = 4.9e3 (3 MeV) ... 1.1 (30 GeV)); with eps=1e-7 for m_psi <~ 0.3 GeV (Y_FI/Y_eq = 49 (3 MeV), 4.5 (30 MeV), 1.0 (0.3 GeV),
   0.12 (3 GeV)) [s-channel only, conservative]. psi then shares it with gamma' (alpha_d = alpha). The hidden sector is re-thermalised
   below v and the reheating ratio xi is no longer the operative variable. Delta N_eff is then set by decoupling at T_d ~ m_psi/4
   (Adshead et al. 2206.13530 eq. 2.17-2.19): T_d < 0.2 GeV -> Delta N >= 0.61 (excluded); T_d = 0.2-30 GeV -> 0.065-0.11 (gamma' only)
   up to 0.48-0.83 if the psi entropy is dumped after decoupling (step4.out).
6. Sec. 2(a) vs 2(b): (a) says gravity-only mixing is <~1e-13; (b) assumes an O(1) Planck-suppressed coefficient. All sources that
   derive the operator get it at one loop from fields charged under BOTH groups (Chen-Cline-Frey p.3; Bruemmer-Jaeckel eq. 28;
   Gherghetta et al. eq. 14), i.e. eps ~ g_d g' y/(16 pi^2) v/Lambda = 9e-11 - 8e-10 (step2a.out) - and such fields are exactly what the
   sector-separation postulate excludes. The eps ~ 1e-7-1e-6 window therefore contradicts the manuscript's own postulate.
7. Sec. 2(c)(ii) gives the DM itself a visible electric charge under CP violation, yet Sec. 2(c) concludes "the decisive constraints act on psi,
   not on the dark matter itself" and exclusion condition 1 treats any DM-SM coupling as fatal. Hidden theta is physical (psi massive) and
   generically O(1): q_vis ~ chi theta_d/(2 pi) (BJK eq. 3.19) = 1.6e-8 e (chi=1e-7, theta=1) to 1.6e-7 e (chi=1e-6) (step4b.out).
   Phenomenologically tiny at M=3e13 GeV, but it makes exclusion condition 1 self-triggering in the eps != 0 branch.
8. "above the MeV scale, so that psi has annihilated before nucleosynthesis": hidden freeze-out T_h ~ m/20 occurs at T_vis ~ 0.08 MeV for
   m_psi = 1 MeV, 0.24 MeV for 3 MeV, 0.71 MeV for 10 MeV (step4.out) - i.e. during BBN. Needs m_psi >~ 20-30 MeV. (Moot: excluded anyway, below.)
9. Sec. 6 says all numbers were computed by executed code; the p error (a dropped prefactor of 4576) and the psi window (factor 3-10 in mass)
   indicate otherwise or a coding error.

### 4(b) Kinetic mixing claims vs literature
- (a) gravity-only: SUPPORTED by Gherghetta et al. (C exact -> no mixing at any perturbative order; C broken -> >= six loops, up to ~1e-13).
  Caveat: the manuscript does not say whether hidden C is broken in its SU(2)+adjoint+doublet sector.
- (b) dim-5 Phi^a F^a B / M_*: gauge invariant, eps = v/M SUPPORTED (Bruemmer-Jaeckel eq. 25; CCF eq. 1). The O(1)-at-M_Pl coefficient is NOT
  supported: cited sources generate it at one loop from bi-charged states (see 4a.6). Baumgart et al. [10a] does not discuss this operator
  at all (uses renormalizable U(1)_dark x U(1)_Y mixing). Gauged-vs-global discrete symmetry statement consistent with [11].
- (c) unbroken U(1)_d => no visible magnetic flux: SUPPORTED (BJ p.5: "hidden monopoles are invisible to ordinary electrically charged matter";
  Hiramatsu et al. abstract). Massive dark photon needed for visible magnetic minicharge: SUPPORTED (Terning-Verhaaren p.11).
- CP-violating magnetic mixing: SUPPORTED (BJK abstract & eq. 2.7: hidden monopole gets visible electric charge -theta_12/2pi), but its size
  and its consequence for the DM are not addressed (4a.7).

### 4(c) Omitted constraints (literature verified on INSPIRE/arXiv)
1. Kibble-Zurek / first-order overproduction + hidden-plasma annihilation: Murayama & Shu, PLB 686 (2010) 162, arXiv:0905.1720
   ("Kibble mechanism drastically underestimates the production of topological defects ... dark matter of mass 1-10 PeV");
   Liveoak, Maharana & Wells, arXiv:2607.20843 ("for symmetry-breaking scales >~ 100 PeV, the monopole abundance is unacceptably high").
   My own integration: overclosure 1e12 at the benchmark (4a.3). FATAL to the stated mass prediction.
2. psi re-thermalisation and Delta N_eff: Vogel & Redondo JCAP 02 (2014) 029, arXiv:1311.2600 (Planck-2013-era: "disfavors MCPs with masses
   between 14 MeV < m_f < 390 MeV for a wide range of minicharges eps > 1e-7"; BBN: "exclude MCPs with m_f < 16 MeV for eps > 1.4e-8");
   Adshead, Ralegankar & Shelton arXiv:2206.13530 (thermalisation threshold m_th = 4 T_d; current N_eff). Mine: 4a.5.
3. SN1987A: Chang, Essig & McDermott, arXiv:1803.00993: "For a millicharged particle, we exclude charges between 1e-9 - few x 1e-6 ...
   for masses <~ 200 MeV" - covers the whole stated charge range for m_psi = 1-200 MeV.
4. Charged-DM subcomponent bounds: Stebbins & Krnjaic, JCAP 12 (2019) 003 (q/e <~ 1e-13+-1 m/GeV, weakened by f^-1/2 for f >~ 0.13);
   McDermott, Yu & Zurek, PRD 83 (2011) 063509 (recombination: eps < 1e-6 at 1 GeV for all DM); disk evacuation (Chuzhoy & Kolb, JCAP 07 (2009) 014)
   vs SN-shock-accelerated flux (Dunsky, Hall & Harigaya, JCAP 07 (2019) 015) - terrestrial direct detection of psi is non-trivial and unevaluated.
   CMB DM-baryon: Planck limits vanish below 0.4% interacting fraction (Boddy et al. 1808.00001); psi up to 10% is not automatically safe.
5. Dark acoustic oscillations of the psi component: psi kinetically coupled to the gamma' bath until z = 2.7e3 (30 MeV), 7.0e4 (0.3 GeV),
   2.2e6 (3 GeV), 6.9e7 (30 GeV) for Delta N = 0.286 (step4.out). For sub-GeV psi this approaches recombination; Cyr-Racine et al. 1310.3278:
   "at most ~5% of all DM can be very strongly interacting with DR". Not addressed.
6. Monopole collective (plasma) effects: magnetic plasma frequency 1/omega_p = 17 yr (local), 109 yr (1e-2 GeV/cm^3), 9.7e3 yr (cosmic mean)
   (step4.out) - far shorter than dynamical times; Lasenby 2007.00667 shows such instabilities can matter "many orders of magnitude below"
   two-body bounds (he gives no constraint). "Effectively collisionless" rests on two-body sigma_T only. Unevaluated, not an indictment.
7. Higgs portal lambda_p |H|^2 Tr Phi^2 (allowed by every stated symmetry): EW naturalness needs lambda_p <= 2.4e-20 - 7.5e-21; equilibration at
   T~v for lambda_p >~ 5e-2 (rough 2->2 estimate) would set xi=1 -> Delta N = 0.86 (excluded). Technically natural to set small, but unstated.
8. Hidden theta / Witten effect (4a.7): monopoles are hidden dyons; visible charge ~1e-8-1e-7 e for eps~1e-7-1e-6.
9. Reheating: requires visible T_RH >~ v/xi = 1.06e12 - 1.90e12 GeV (step4c.out) and a two-field (or asymmetric) reheating mechanism for xi;
   a separately reheated hidden sector can carry dark-radiation isocurvature (conditional; not computed). No CMB-scale monopole isocurvature
   expected from post-inflation production (inference, not computed).
10. Prior art not cited: Baek, Ko & Park JCAP 10 (2014) 067 [1311.1035]; Khoze & Ro JHEP 10 (2014) 061 [1406.2291] (both: hidden SU(2)->U(1)
    monopoles + W' + dark photon); Murayama-Shu; LMW; Freidel-Leigh-Minic (Born geometry, for Sec. 1).
11. Dark-energy aside: DESI DR2 (2503.14738) "the favored w(z) shows a phase of w > -1 at low redshifts and a phantom crossing to w < -1 above
    redshifts z ~ 0.4"; NEC-respecting models "can somewhat outperform LCDM" but are disfavoured relative to w0wa. "Never-phantom ... consistent
    with hints" is at best partially true; the DESI-preferred solution is phantom-crossing, which exclusion condition 6 says would kill the framework.

### 4(d) Does the phase-space framework do any work?
No. Sec. 2 itself: "We use this only as motivation ... No numerical result below depends on it." The compatibility theorem (true) is never
used after Sec. 1; hypothesis H is motivated, not derived (acceptance criterion 1 concedes this); the hidden-sector content, sector
separation, xi and m_psi are all postulated; Sec. 1 "Kinematics" says the hidden sector is ordinary relativistic QFT. The DM proposal is the
standard hidden 't Hooft-Polyakov-monopole scenario (Baek-Ko-Park 2013; Khoze-Ro 2014; Murayama-Shu 2009; LMW 2026) with one coupling choice
(alpha_d = alpha), and it stands or falls on that literature, independently of Born reciprocity. Even the one structural input H only sets
M/v = 21-37 and alpha_m = 34; replacing e by e/3 (the smallest SM charge) gives alpha_m = 308 (step2a.out), and the framework gives no way to choose.

## Step 5 - Verdict

GRADE: C (fundamentally flawed), confidence MEDIUM (high confidence in each individual finding; medium on the B/C boundary).
Reason: the headline result (M ~ 1e13-4e13 GeV "with no dilution required") is wrong on two independent counts (Kibble normalisation,
step2a.out; neglect of Kibble-Zurek / bubble overproduction with hidden-plasma annihilation, step4.out, LMW 2607.20843, Murayama-Shu 0905.1720),
every downstream number (v, m_W', psi window, GW band, eps) hangs on it, and the "selected by phase-space duality" claim does no work.
Salvage = a different model (v <~ 1e8 GeV, or explicit dilution), which already exists in the literature.

Single weakest link: the Kibble abundance / mass determination (p=0.023 instead of >= 25-104; Kibble treated as an upper end when it is
the causal minimum; KZ production and alpha_m=34 Preskill-type annihilation not computed although the literature already has it).
Second: the framework does no work.

Reproducibility note (blindness): nothing under /home/paul/git was read. The harness auto-attached a git-status snapshot whose
latest commit subject mentions a pre-registered expected verdict; it was not consulted for any finding.
Notes from extra.: p ~ 1 is (to 17%) the REDUCED-Planck normalisation of one-per-horizon (0.828, step4d.out); the manuscript's
"reduced-Planck convention lowers it by ~3" variant (2.74e12) is in fact the physically correct Kibble minimum (2.87e12).
