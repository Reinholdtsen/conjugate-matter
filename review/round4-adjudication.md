# Round 4 — adjudication

- **Manuscript:** `papers/reciprocity-toy-models.md` (the toy-model note), as
  of commit d9a06ac.
- **Pre-registration:** [round4-preregistration.md](round4-preregistration.md),
  committed before dispatch with a neutral subject.
- **Referee:** a blind subagent with Python and web. Its notes and scripts
  are in [round4/referee/](round4/referee/), with the verdict in
  `audit-notes.md`. It was interrupted once by a rate limit and resumed from
  its own transcript. All 9 of its numerical and algebraic indictments rest
  on executed code.
- **My arbitration:** [round4/adjudicator/](round4/adjudicator/).
  `arb.py` covers F1–F5; `ctrl.py` covers the control run and is run from
  the repo root. Outputs are in the `.out` files.

## Verdict

**Referee: B (flawed but salvageable), confidence ~0.75. I agree.**

- The algebra and numerics of §§2, 3 and 5 reproduced under the referee's
  own conventions and code.
- The only claim of actual quantum symmetry breaking (§4, model I in 1+1)
  rests on a potential that is unbounded below once H is dynamical.
- It is repairable.

## Rulings

| # | Finding | Ruling | Evidence |
|---|---|---|---|
| F1 | The §4 potential −μ[Tr(K K_ref)]² is unbounded below in model I | **Upheld** | `arb.py`: along H = SᵀS, K = S⁻¹K₀S (S a boost), the λ-term is ~0 while V_μ = −4, −56.6, −2983, −8.9×10⁶ at t = 0, 1, 2, 4. |
| F2 | So (1, K_ref) is a saddle, and the Monte Carlo simulates a frozen-H reduction, not model I | **Upheld** | The Hessian of λV_λ + V_μ at (1, K₀) has a negative eigenvalue at λ = 1, 10, 100 (−6.47, −4.40, −4.04 in my coordinates). The referee's bounded variant −μ[Tr(K K_ref)]²/(2Tr KᵀK) gives eigenvalues [0, 0.764, 2, 5.236]. Its zero mode is the residual diagonal squeeze, which is an exact symmetry, and the boost family rises from −1 to −0.5. **This is the repair.** I should have caught F1 myself: I checked the potential only at frozen H. |
| F3 | The twisted ρ, ρ∘(K → −K), fixes the vacuum | **Upheld** | `arb.py`: (1, K₀) is mapped to itself. Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K. This sharpens the S5 conclusion rather than contradicting it. |
| F4 | In the real Grosse–Wulkenhaar model the polarization is a discrete choice, lifted at one loop | **Upheld, with a consequence the referee did not draw** | `arb.py`, N = 8: diag(a₀, +a₁) and diag(a₀, −a₁) have equal classical action (−2.5) but different Hessian spectra (lowest [2, 4, 4, 4] vs [1.07, 1.07, 2, 4]; the referee's normalization is half of mine), and F(+) − F(−) = 2.634, exactly the referee's number. **The lower free energy belongs to diag(a₀, −a₁), the β = π vacuum, which is the one sharper in position** (Δ(π) = −Δ(0) < 0). The real model therefore selects the position-sharp polarization at one loop. This is explicit, not spontaneous: the real model is not duality-symmetric, because the field is real in x. It is recorded as a lead, not a result: truncation dependence and its interpretation are unchecked. |
| F5 | I_K needs H as well as K; it is covariant only under the SO(2) fixing H = 1 | **Upheld** | `arb.py`: rescaling the eigenline coordinate by 2 doubles I (0.407 → 0.814). |
| F6 | "Increasing the truncation adds only massive levels" ignores the 2 ln N mass renormalization | **Accepted, not re-checked** | 2D φ⁴ needs mass renormalization. The no-breaking conclusion is unaffected; the argument must be restated. |
| MC control | Quoted 0.078 / 0.033 / 0.014 at T = 3 do not match the referee's 0.0630 / 0.0318 / 0.0156 | **Upheld** | `ctrl.py`: my L = 16 value from seed 116 was a short-run fluctuation. Other seeds give 0.063–0.069, and long runs give 0.0653 / 0.0325 / 0.0164, clean 1/L. **Fixed seeds gave reproducibility, not accuracy; the numbers lacked error bars.** The ordered-phase values (0.954) and the h = 0 decay agree with the referee to about 1%. |
| MC start | Hot starts at L = 64 trap in metastable domains; start conditions not stated | **Accepted** | Cold starts are standard for ordered-phase measurements, but they must be stated. |
| DFT "pair" | "Every derivation selects the pair" holds only for d = 1 | **Upheld** | For d > 1, Betz–Blumenhagen–Lüst–Rennecke's M ∈ O(d) gives a continuous family of sections. |
| Mermin–Wagner vs [11] | The model I H-sector is a hyperbolic SO(1,2) model, which by Duncan–Niedermaier–Seiler can break in 2D | **Upheld (literature)** | The Mermin–Wagner statement must be restricted to the compact SO(2) containing ρ. Whether that SO(2) is broken in the coupled model is open. |
| Citations | A. Duncan, not N.; DNS erratum (NPB 758, 330 (2006)); GW eq. 1 is the 4D form (π²); [5] is about 4D; [12]'s two-fold claim cannot be checked (paywalled) | **Accepted** | — |
| Omitted prior work | Langmann–Szabo–Zarembo exact solution (hep-th/0308043); Smolin 2007.05957; Marotta–Szabo; Fosco–Moreno (0710.0818); GW 0401128 ("manifest" in the matrix base); Royer (parity-operator form of Weyl symbols) | **Accepted, as citations and reframing** | Smolin breaks a triality *down to* Born duality, leaving it unbroken, so it does not contradict "no model breaks ρ itself". It still has to be cited. |

## Pre-registration scored

| Prediction | Outcome | Score |
|---|---|---|
| Verdict B | B | **Hit** |
| Weakest link: §4's breaking rests on a rigid background (K_ref) | Same place, worse defect: the potential is unbounded below with H dynamical | **Partial**: right location, missed severity |
| Runner-ups: model II restoration argument; real-vs-complex; weak S5 by construction | Restoration conclusion confirmed but must be restated (F6, LSZ); real-vs-complex confirmed and extended (F4); I_K needs H (F5) | Partial on all three |
| At most one surviving numerical indictment, likeliest a normalization or sign | One: the MC control values, a statistical problem. Every normalization and sign I listed was confirmed | **Hit on count, miss on location** |
| All 12 citations resolve; likeliest over-cited is [12] | All resolve; [12]'s specific claim is unverifiable; also [8] (d = 1 only) and [11] (author's initial) | **Hit** |

Calibration across rounds:

- Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4).
- Weakest-link location has improved. Severity is still underestimated.

## Lessons (into CLAUDE.md)

1. When numerics run on a reduced model (some fields frozen), check the
   stability of the unreduced model — boundedness, and the Hessian with all
   fields dynamical — and state the reduction in the text.
2. Monte Carlo numbers need error bars from independent runs. A fixed seed
   makes a number reproducible, not accurate.

## Revisions for v2 of the note (all accepted; applied 2026-10-20 in commit 6606734)

1. **§4:**
   - Use the bounded potential. Show it is stable with H dynamical (local
     minimum up to the exact residual squeeze).
   - Present the Monte Carlo as the frozen-H reduction, explicitly.
   - Restrict Mermin–Wagner to the compact SO(2); cite DNS for the
     hyperbolic H-sector, noting the open question.
   - Say "ordered Z₂ phase", not "Ising class".
   - Give start conditions, equilibration checks, and error bars from
     independent seeds; rerun the control.
2. **§2/§6:** state the twisted ρ (F3). Breaking ρ is physical only with a
   K-odd coupling.
3. **§3:**
   - Present the matrix-base duality as a lemma, crediting
     Grosse–Wulkenhaar (manifest in the matrix base), Royer (the parity
     form) and Langmann–Szabo (the complex formulation).
   - Restrict "Goldstone angle" to the complex model.
   - Add F4 (the real model's discrete, one-loop-lifted vacua) as a lead.
4. **§4, model II:** restate the restoration argument (exact independence of
   the condensate phases, no volume factor), add the 2 ln N mass
   renormalization, and compare with Langmann–Szabo–Zarembo.
5. **§5:** restrict the section "pair" to d = 1. Call I_K (H, K)-covariant,
   covariant under SO(2) only.
6. **References:** apply the fixes above; add LSZ, Smolin, Marotta–Szabo,
   Fosco–Moreno and Royer. Every new citation is to be retrieved, not
   recalled.
