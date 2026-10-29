# The clumping problem, Chunk C: The ultra-faint-dwarf endpoint — closing the clumping problem

*Working note. Status: complete. Verdict: Scenario A falsified; the clumping problem closed.*

## The question

Chunk 3b left Scenario A (gated channel = the core-maker) with one mandatory prediction: halo-wide condensation in ultra-faint dwarfs (UFDs), R ≡ Γ_self·t_dyn ≫ 1. This chunk follows that condensation to its endpoint and tests it against real UFDs.

## Sharpened input numbers

Segue 1: M(< 38 pc) ≈ 6×10⁵ M_⊙ ⇒ mean core density ρ ≈ 100 GeV/cm³ (not the conservative 20 used in 3b), σ ≈ 3.7 km/s, t_dyn ≈ 10 Myr. Rerunning the 3b ratio with the dwarf-core normalization (κ = 1):

$$
R_{\rm Segue\,1} = \kappa\,\frac{t_{\rm dyn}}{t_{\rm age}}\left(\frac{\rho}{\rho_d}\right)^2\left(\frac{\sigma_d}{\sigma}\right)^2 \approx 10^{-3}\cdot 10^4 \cdot 66 \approx \mathbf{660}.
$$

Condensation time τ_cond = t_dyn/R ≈ 1.5×10⁴ yr. Over a 10 Gyr lifetime the system has ~6×10⁵ condensation times. Even granting the soliton-growth slowdown seen in LPT-type kinetics (t^{1/2} growth, factor ~10²–10³ in effective rate), the core is processed through the condensate many times over. There is no timescale refuge.

## The attractive endpoint: criticality and the drain

Under the Scenario-A normalization (which pins g²/m³, hence pins M_crit as a function of m alone):

$$
M_{\rm crit} = \frac{3.6\,M_P}{m\sqrt{g}} \;\approx\; 2.9\times10^{-30}\, \left(\frac{m}{\mathrm{eV}}\right)^{-7/4} M_\odot .
$$

This crosses the UFD core mass (~10⁶ M_⊙) at m ≈ 5×10⁻²¹ eV. Two branches:

**Branch (i), m ≳ 10⁻²⁰ eV (the bulk of the wave island):** M_crit ≪ M_core — often absurdly so (10⁻⁷ M_⊙ at 10⁻¹³ eV). The condensate reaches criticality almost immediately and enters the known attractive-collapse cycle: grow to M_crit → collapse → eject an O(0.1–1) fraction as fast/relativistic waves (bosenova; LPT 2017-type result [T]) → remnant regrows. Ejecta velocities are set by the dense collapse stage and vastly exceed a UFD escape velocity of ~10 km/s: **the condensate is a mass drain.** The UFD converts its cold dark matter into escaping radiation at a rate bounded below by the self-regulated relaxation rate. Even if heating and expansion throttle Γ down to ~1/t_age (the gravothermal self-limit), an O(1) fraction of the core mass is processed *and removed* within the lifetime — unlike SIDM, where relaxation is elastic and mass stays. Prediction of Branch (i): UFDs today should be low-density, inflated, or gone.

**Branch (ii), m ≲ 5×10⁻²¹ eV:** M_crit ≳ M_core; the condensate grows as a stable soliton — ordinary fuzzy-DM phenomenology with an attractive perturbation. But this mass range is independently excluded: UFD sizes and stellar kinematics (granule-heating arguments, Dalal & Kravtsov 2022 [T — bound ≈ 3×10⁻¹⁹ eV; verify exact figure before publication]) and Lyman-α forest limits already forbid wave DM this light.

## The data

Observed UFDs are the densest, most DM-dominated, oldest systems known — Segue 1 has M/L ~ 10³ and a ~13 Gyr stellar population sitting in an intact, *dense* halo. Branch (i) predicts the opposite of what is observed; Branch (ii) is excluded before we arrive. Robustness checks: shrinking v* makes it worse (σ⁻⁶ leverage boosts R to ~10⁵); growing v* leaves R unchanged; κ < 1 is by definition Scenario B. No parameter direction rescues it.

## Verdict and closure of the clumping problem

**Scenario A is falsified by the existence of ultra-faint dwarfs.** Combined with the chunk-A theorem (no collective behavior on the particle island) and the chunk-B Scenario-B verdict (tunable, never mandatory, on the wave island), the clumping problem closes with a clean, honest result:

> **Nowhere in the viable parameter space of BBT is velocity-space clumping a mandatory phenomenon.** It is forbidden for classical-particle χ, fatal where it would have been mandatory (Scenario A), and merely optional elsewhere (Scenario B, ten tunable orders of magnitude — a degeneration flag, not a prediction).

Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them. What remains distinctively BBT's own: the exponential cliff + in-gate isotropy (particle island), the cliff-sharpness **island discriminant** (exponential vs (v*/σ)⁴), the dark-energy sector (thawing, no-phantom, turnaround — live at DESI DR3), and the permanent nulls (direct detection, monopoles, linear dispersion). The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings.

## Next: the field-equation problem, Chunk 1a

Linearize S_H on the broken vacuum. Sub-plan: (1a-i) mode content at quadratic order on flat background, importing the known linearized-DFT spectrum [T: graviton + two-form + dilaton]; (1a-ii) ghost check of the quadratic action with ω, η frozen; (1a-iii) extract the dynamical equation for the g̃-block — the field-equation problem, first direct step. This is the heaviest chunk; expect subdivision.
