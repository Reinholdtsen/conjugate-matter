---
title: "The velocity-gated-gravity script"
weight: 120
status: method
description: "verify/velocity_gated_gravity.py recomputes the numbers of the momentum-gravity note: anchors independent of the investigation (CODATA, the Einstein–Infeld–Hoffmann and Darwin Lagrangians, textbook spin-2 numerators, Planck 2018's age, exact growth modes, a closed-form kernel, published torsion-balance ranges, Mercury's perihelion, the Plummer sphere), then regression checks in nine blocks, B to J; the N-body runs are read from their logs, not rerun."
provenance: [D, V]
sources:
  - "verify/velocity_gated_gravity.py"
  - "notes/velocity-gated-gravity.md header"
  - "notes/velocity-gated-gravity.md §1–§9"
  - "notes/velocity-gated-gravity.md §11"
  - "review/momentum-gravity/README.md"
  - "review/momentum-gravity/answer.md 'Candidate flags (for your ruling)'"
  - "review/momentum-gravity/scripts/corner/diagnostics_final.out"
  - "review/momentum-gravity/scripts/corner/injection_test.out"
  - "review/wiki-build-checks/stream_stability_check.py"
  - "scripts/check.sh"
  - "CLAUDE.md 'Layout'"
  - "CLAUDE.md 'Method (HANDOFF §5)'"
  - "review/wiki-build-flags.md items 16 (addendum), 39, 56, 57, 58"
---

*The velocity-gated-gravity script, `verify/velocity_gated_gravity.py`, recomputes the numbers of the note that answers Paul's question of 2026-10-26: whether the obituary of velocity clumping is premature, and whether the program's momentum gravity would look like a correction to ordinary gravity that depends on the relative velocity of two bodies. The investigation ran in scripts outside the repository; this file ports the ones it needs into one self-contained check that the gate runs. Before it computes anything from the investigation, it reproduces values that do not depend on it: CODATA 2018 constants, the two-body Lagrangians of general relativity and of electrodynamics at first order beyond Newton and Coulomb, the textbook numerators of massless and massive spin-2 exchange, the age of the universe and the epoch of matter–radiation equality published by Planck 2018, exact growing modes of density perturbations, a closed form of the gate's Fourier kernel, two published torsion-balance ranges, Mercury's perihelion advance in general relativity and the free-fall time of a Plummer sphere. Everything after these anchors is, in the docstring's words, a regression check: it reproduces the investigation's own numbers and is not independent of them. The simulations of the narrow-gate corner cannot be rerun here; their checks read the simulations' logs and recompute nothing.*

**Status:** Method, in force — the note says that "Every number is recomputed in `verify/velocity_gated_gravity.py` (§9's medium in `verify/gate_mechanism.py`), except the N-body runs of §8, whose record is kept" (note header), and its [V] tags rest on the script — ninth in the list of scripts that [the gate](/wiki/method/verification/the-gate), `scripts/check.sh`, runs. The run of 2026-10-28 recorded below printed 93 lines marked `PASS` and none marked `FAIL` (a count of its output lines), and the script ended "OK — every number of the velocity-gated-gravity investigation reproduces." The note itself has not been reviewed.

## What it checks, and for what

The note is `notes/velocity-gated-gravity.md`, of 2026-10-28. Its results are on these pages:

- [X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies): the momentum graviton X adds a short-range Yukawa term whose only velocity dependence is relativistic, and a relative-velocity gate acting between all bodies is excluded (note §§2–3; blocks B and C);
- [what the obituary covers](/wiki/dark-matter/momentum-clumping/founding-image#what-the-obituary-covers) and [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion): the obituary's three branches and calc note #2's shortfall (note §4; block D);
- [a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction), a model the record does not contain: its readings, the Lyman-α and Sagittarius bounds, the clumping thresholds, the cores and the narrow-gate corner (note §§5–8; blocks E to H);
- [what could carry a relative-velocity gate](/wiki/dark-matter/conjugate-matter/gate-carriers): finite spin, a tower of spins, a medium, continuous spin (note §9; block I).

Block J checks the Vainshtein radius of the phase-space-diameter note, which the investigation found computed with the formula for a massless mode (flag 57 in `review/wiki-build-flags.md`). The numbers the note computes carry [V] or [D][V]; the published figures it quotes carry [S].

The docstring states the scope, the anchors and the inputs:

```text
velocity_gated_gravity.py — every load-bearing number of the momentum-gravity
investigation (notes/velocity-gated-gravity.md), recomputed and checked. Paul's
question (2026-10-26): "I think the obituary is premature. Would momentum
gravity look like a perturbation to regular gravity that depends on the
relative velocity of two massive bodies?" The investigation ran outside the
repository in executed scripts; its record (analyses, verdicts, the critics'
rulings, every script beside its printed output) is review/momentum-gravity/.
This file ports the scripts it needs (it imports none of them) and is
self-contained. The ported source is named at each section as
scripts/<agent>/<file>, relative to review/momentum-gravity/. The numbers
checked are those of review/momentum-gravity/answer.md and of the final
critic's load-bearing list (run3/critic.json); where the two differ, the
critic's ruling and run 4's corrections (applied in answer.md) are used.

Exit code 1 if any check fails. Anchors come first and are independent of the
investigation: [...] Everything after the anchors is a regression check: it
reproduces the investigation's own numbers and is not independent of them.
Checks marked "record" read the record's printed output and recompute
nothing: they cover the 29 N-body runs of the low-v* corner, whose runs took
hours of CPU and whose snapshots (about 90 MB) were not kept, so they cannot
be rerun here.

Inputs: CODATA 2018. The record's hypothetical long-range attraction
U = -eps G m^2 W(|v - v'|/v*)/r with the amplitude gate W = exp(-s^2/2) (the
record's convention; the ordinary-matter analyses use exp(-v^2/v_a^2), and
v_a = sqrt2 v*); v* = 120 km/s; m_chi = 70 MeV and sigma_T/m = 30 cm^2/g at
30 km/s (calc note #2). Each data input (Planck 2018, DESI DR1 and eBOSS
Lyman-alpha compressions, planetary ephemerides, the double pulsar, Lee et al.
2020, Vasiliev-Belokurov 2020's Sagittarius, Enander-Mortsell 2013) is typed
in with its source where it is used; the record marks them [S] (live-searched
by its agents) unless a dagger is shown.
```

The docstring's lines are rewrapped here, the command that runs the script is left out, and the bracket stands for its list of anchors, set out below; its last two paragraphs, on two reduced ports and on what is not recomputed, are quoted under [what it does not recompute](#what-it-does-not-recompute). Each check prints `PASS` or `FAIL`, its label and, where there is one, the computed value in brackets; indented lines print intermediate values without a check, and bracketed times are the elapsed seconds. The failures are collected, and the script lists them and exits with code 1. Check labels carry a block letter and an item number (A1, B0, C2 and so on); a label marked "(record)" reads the investigation's printed output, and two labels are marked "(record, not adjudicated)". The docstring gives the runtime as about 35 s on the development machine, which has 8 gigabytes of memory, with a peak resident memory of about 175 megabytes; the run recorded below printed a wall time of 34.6 s.

The record convention matters throughout. The record's cross-section gate is e^{−v²/v\*²} with v\* ≈ 120 km/s, and its amplitude gate e^{−v²/v_a²} with v_a = √2 v\* = 169.7 km/s (note §1); the ordinary-matter analyses state their gate widths as v_a.

## The anchors

The rule behind them is root `CLAUDE.md`'s: "An anchor must be independent of the paper (a textbook identity, a published value). A check that reproduces the paper's own number is circular." ([independent anchors](/wiki/method/verification/independent-anchors)). The first block, headed "Anchors (independent of the investigation)", prints 14 `PASS` lines:

- **Constants (A1).** ħc and the Planck mass against CODATA 2018.
- **Two-body Lagrangians (A2).** The Fokker action of massless spin-2 exchange at order v² reproduces the order-G terms of the Einstein–Infeld–Hoffmann Lagrangian of [general relativity](/wiki/gravity/spin-2-fields/general-relativity) "(Landau-Lifshitz sec. 106) exactly", and spin-1 exchange reproduces the Darwin Lagrangian of electrodynamics (§65); the Yukawa propagator functions solve their equations.
- **Spin-2 numerators (A3).** The textbook de Donder numerator, normalized to its static value, is 2γ² − 1 = T₂(γ), and the [Fierz–Pauli](/wiki/gravity/spin-2-fields/fierz-pauli) one (3γ² − 1)/2 = P₂(γ), with γ the relative Lorentz factor; their static ratio is 4/3, the van Dam–Veltman–Zakharov factor, and 3/4 as γ → ∞. A second check contracts the stress tensors of point masses at five random pairs of velocities to 40 digits.
- **The cosmological background (A4).** The dark-tests background reproduces Planck 2018's age, 13.795 Gyr against the published 13.797 ± 0.023, and matter–radiation equality, z_eq = 3419 against 3402 ± 26; the Lyman-α background reproduces the Planck 2018 + BAO column's age, 13.80 Gyr against 13.787 ± 0.020, the published value marked † (BAO is baryon acoustic oscillations). A third line, the σ₈ normalization of the power spectrum (0.8111), labels itself "regression: normalization, not an anchor".
- **Growth (A5).** Both growth integrators reproduce the exact Einstein–de Sitter solution (3/5)(a/a_i) + (2/5)(a/a_i)^{−3/2} to 10⁻⁸, and the integrator of the cosmology code holds Mészáros's exact D = 1 + 3a/(2a_eq) to 10⁻⁹ from a = 10⁻⁶ to 1.
- **The gate kernel (A6).** R(y) = y∫₀^∞ sin(yt)e^{−t²/2}dt has the closed form √(π/2) y e^{−y²/2} erfi(y/√2); the critic's quadrature matches it at y = 0.3, 1, 1.08 and 3 to 10⁻⁸.
- **X's range (A7).** The torsion-balance interpolation reproduces Lee et al. 2020's published 38.6 μm (|α| = 1) and 30 μm (α = 8/3), as in [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script) ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)).
- **Planetary units (A8).** Mercury's perihelion advance in general relativity, 6πGM/(c²a(1 − e²)) per orbit, from the fact-sheet orbit: 43.0 arcsec per century against the textbook 42.98.
- **The N-body units (A9).** The central free-fall time of a Plummer sphere in N-body units, 1/√3 = 0.5774.

Block F opens with checks it labels "F1 anchors" (the Jeans limit of its eigenvalue problem, and the gate set to 1), and block G with "G5 anchors" and "G7 anchors" (the corner's own printed responses reproduced). These test the ports against limits or against the record; they are not independent of the investigation in the sense of the rule above.

## The checks, block by block

The block headers name the investigation's scripts each block ports, as paths under `review/momentum-gravity/scripts/`.

### B. X between ordinary bodies (8 checks)

- B0: at order v², exchange of X, a massive spin-2 field, gives a Yukawa term with relativistic O(v²/c²) terms, "no gate"; V = −(Gm₁m₂/r)(1 + α e^{−r/λ_X}) with α = 4u²/3 = 4/3 in the aligned vacuum u = 1 gives the unscreened λ_X < 37.7 μm and M_X c² > 5.2 meV, "recomputed here; also gated in `verify/phase_space_diameter.py`", and 57.0 μm at u = 0.5, 30.8 μm at u = 1.5.
- B1: X's velocity factor (3γ² − 1)/2 − 1 = 2.40×10⁻⁷ at 120 km/s, against the graviton's 2γ² − 1 − 1 = 3.20×10⁻⁷; both grow monotonically with relative velocity, "no velocity gate at any range"; u₁·u₂ = γ_rel depends on the relative velocity.
- B2: #13's dual kinematics for the Sun and Earth, F/c̃ = 2.93×10⁻²² and γ̃ − 1 = 4.28×10⁻⁴⁴ — the label notes that the answer's "(F/c~)^2 ~ 4e-44" is γ̃ − 1, and (F/c̃)² itself 8.56×10⁻⁴⁴ — "or zero if free fall is dual rest (#13 sec. 5)", the conflict of flag 56 ([dual inertia](/wiki/conjugate-relativity/dual-inertia)); the Siegel reading of flag 39, vF/(c⁵/G) = 2.91×10⁻²⁶ for the Sun and Earth, and the Siegel generalized metric for d = 2, symplectic with determinant 1 and its part linear in X in the mixed blocks only.

These are the numbers of [X between ordinary bodies](/wiki/gravity/momentum-graviton/ordinary-bodies).

### C. A universal relative-velocity gate between ordinary bodies (10 checks)

- C0: e^{−v²/v_a²} equals the record's amplitude gate iff v_a = √2 v\*, so the scan v_a = 0.3–3000 km/s is v\* = 0.21–2121 km/s, "'0.2-2100' in the record's convention".
- C1: the double pulsar's mass-bias factor, 2.4666 (Kramer et al. 2021 §VI.2.1), turns their 1.3×10⁻⁴ into |δω̇/ω̇| < 5.27×10⁻⁵.
- C2: at v_a = 120 km/s Mars's perihelion binds, 1.82×10⁻¹¹ (Earth 4.04×10⁻¹¹, Mercury 6.37×10⁻¹¹); the interim figure "2e-11 from Mercury" is the INPOP15a ephemeris's one-standard-deviation anomalous advance at v_a = 120 km/s, giving 2.5×10⁻¹¹ and 1.7×10⁻¹¹ in the ordinary-tests convention; at the record's v\* = 120 km/s (v_a = 170 km/s), |ε| < 3.5×10⁻¹¹ from Mars (Lorentzian gate 3.64×10⁻¹¹). The note records the correction: the bound at the record's gate width is 3.5×10⁻¹¹ from Mars, "not 2×10⁻¹¹ from Mercury, which used the other gate convention" (§11).
- C3: the Gaussian envelope over v_a = 0.3–3000 km/s, |ε| < 8.65×10⁻⁹ ("8.7e-9"), weakest at 3000 km/s and set by the double pulsar; the Lorentzian envelope over 0.1–3000 km/s, |ε| < 9.42×10⁻⁹; and the leading order as u → 0, δω̇/ω̇_GR = −(2/3)(c/v_a)²ε, which gives 7.92×10⁻⁹ at 3000 km/s from the double-pulsar limit.
- C4: below v_a ≈ 0.3 km/s there is no numerical bound — the Gaussian envelope's weakest point on 0.1–0.3 km/s is ε < 0.615, at v_a = 0.176 km/s, set by Eros — only a qualitative exclusion: a body at rest at a pole has inertia m(1 − 2GMε/(Rv_a²)), which vanishes at ε = 7.97×10⁻⁵ for v_a = 0.1 km/s.

### D. The obituary's scope: calc note #2's shortfall (4 checks)

- D1: "Calc note #2's record logic", ported from the wiki build's recomputation `review/wiki-build-checks/stream_stability_check.py`: g = 2.48×10³ GeV⁻², and the contact gate's collective pull over m·min(σ, v\*)² is 3.9×10⁻²⁸ in a dwarf core and 2.9×10⁻³¹ in the Milky Way. A second D1 line prints the logarithms, −27.41 and −30.54, and notes that "'falls short by 10^28-10^31' quotes the ratios' printed exponents e-28 and e-31; the shortfall factors are 2.6e27 and 3.5e30".
- D2: the linearized threshold, g·n·Λ_g(σ/v\*)/(m σ²) = 3.27×10⁻²⁸ in the dwarf core and 8.7×10⁻³¹ in the Milky Way.
- D3: for a gate narrower than the dispersion the linearized criterion is g·n·Λ_g ≥ m σ², and #2's form overstates the Milky Way shortfall by 3.04 ("about 3x") at r = 155/120; "the verdict is unchanged".

Block D puts calc note #2's arithmetic in the gate for the first time. Flag 16 in `review/wiki-build-flags.md` had recorded that `HANDOFF.md` §2 marks the shortfall ✓ with no script behind it; its addendum of 2026-10-28 says that this section "now ports 3a's arithmetic into the gate and reproduces both ratios, with the linearized values beside them (flag 58). The ✓ is now backed by a script; #11 §9's tag [D] is unchanged until Paul rules." The addendum adds: "'10²⁸–10³¹' quotes the ratios' exponents; the shortfall factors are 2.6×10²⁷ and 3.5×10³⁰." D3 is labelled with flag 58. The pages are [the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion) and [what the obituary covers](/wiki/dark-matter/momentum-clumping/founding-image#what-the-obituary-covers).

### E. The long-range attraction among χ (18 checks)

The block's header names the model, U = −εGm²W(|v − v′|/v\*)/r among χ only, and the scripts it ports, among them the final critic's Hamiltonian system and the Sagittarius bound. Its checks:

- **Kernels (E1).** At the pivot of the Dark Energy Spectroscopic Instrument's (DESI's) Lyman-α data, y = 1.08: R = 0.803130, the density kernel of the run-2 agent (the script's "round-2 agent"), and R₁ = 0.311446, the force law's, "2.58x smaller"; R_v = 0.536423 and B = −0.938630; four identities among the kernels to 10⁻⁸; the pivot k = 0.009 s/km at z = 3 is 0.6898 Mpc⁻¹, and y_p = 1.0800 at v\* = 120 km/s, "the gate in velocity units is v\* at every epoch".
- **The response at the pivot (E2).** At ε = 0.1: in the record's (Hamiltonian) reading T_m² = 0.9478 and Δn = −0.0603, "a suppression"; in the force law 1.0356 and +0.0637; the superseded systems give 0.9862 (a transcription by the run-2 critic) and 1.0784 (the run-2 agent's hybrid).
- **The Lyman-α bound (E3).** From DESI's compressed Data Release 1 (DR1) parameters at Δχ² = 3.84: ε < 0.0570 (matter ratio) and 0.1063 (gas ratio) in the record's reading, 0.0585 and 0.1755 in the force law. The superseded numbers are traced to their flawed systems: the hybrid's 0.028, and the run-2 critic's 0.358/0.305, "the '0.34' that counted -H A_delta twice". A "(record)" line compares the second independent derivation's outputs, 0.0572/0.1069 and 0.0585/0.1760, with this port: largest difference 0.61%.
- **The eBOSS compression (E4).** In the record's reading χ² falls from 26.31 at ε = 0 to 1.90 at ε = 0.0535, with an upper bound of 0.0741, "(not evidence: the data sit 4.90 sigma from Planck [S, arXiv:2311.16377])"; a step test gives T_m² = 0.947755 with 8000 and 16000 steps of the fourth-order Runge–Kutta integrator.
- **Where linear theory fails (E5).** The record's reading becomes singular where 1 + κB = 0: min B = −1.0712 at y = 1.41, so at ε = 2.248 (z = 50), 2.236 (z = 10) and 2.293 (z = 3), "linear theory fails above eps ~ 2.2".
- **Hubble-flow gating (E6).** The gate radius v\*/H₀ = 1.781 Mpc today; the comoving gate radius peaks at 2.028 Mpc at z = 0.631, where the expansion turns from deceleration to acceleration.
- **The Sagittarius stream (E7).** The gate average in closed form, 0.06136, against quadrature and a Monte Carlo of 20 independent runs of 2×10⁵ pairs, 0.06143 ± 0.00008. A "(record)" line finds that a Monte Carlo value in the record, 0.06150 ± 0.00004, sits 3.3 standard deviations from the closed form on its own 10-run error bar but 2.2 on the exact variance: "its error bar came out low, the closed form stands" ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars)). Then the bounds: ⟨W⟩ = 0.0656 at V = 311.1 km/s, so Kesden and Kamionkowski's 10% gives ε < 1.52 in the force-law mapping; ε < 0.20–0.37 in the record's reading, "order of magnitude"; ε < 0.36–2.46 over three toy Milky Way potentials, three host dispersions and four orbit weightings; and so the quoted range, "of order 1 (0.2-2.5)".
- **Too small for clumping (E8).** Clumping needs ε > 1 at every gate width (F2), so the allowed strength is at least 5.7× too small in the force law and 9.4× in the record's reading; ε = 4/3 exceeds the record-reading gas bound 12.5×.

These are the numbers of [a long-range velocity-gated attraction among χ](/wiki/dark-matter/momentum-clumping/long-range-gated-attraction); the note calls the Lyman-α figures "estimates, not likelihoods" (§6).

### F. Clumping thresholds (8 checks)

- F1: the anchors named above, and the gate-only top eigenvalue in closed form, Λ_g = [1/2 + r² + √(1 + 4r²)/2]^{−3/2}, against the Nyström operator: 1.4928686×10⁻¹ in the Milky Way (r = 155/120) and 1.4435026×10⁻³ in a cluster (r = 1000/120).
- F2: velocity-selected clumping needs ε > 1/Λ_g(σ/v\*), which increases with r and has minimum 1.000003 over r in [10⁻³, 10], "so eps > 1 everywhere" (the note: tending to 1 as σ/v\* → 0, §7); 1/Λ_g(1) = φ³ = 4.236, so ε ≥ 4.24 wherever σ ≥ v\*; 1/Λ_g = 4/3 at r = 0.33282.
- F3: in the Milky Way (σ = 155 km/s) the threshold is 28.07 at the core margin, 127.5 at 2π² and 161.2 at the solar circle's scale, and none once the halo re-virializes; in clusters (σ = 1000 km/s) the velocity-selection crossover is 692.8, and the instability threshold 152.2 (the interim's "at least 152") or 798.8 re-virialized.
- F4: the margins over the allowed ε at v\* = 120 km/s: 264 (Milky Way), 6.52×10³ (clusters) and 11.4 (the loosest Sagittarius mapping).
- F5: the local model holds only for ε < (1 + r²)^{5/2}/(4.5r²): 1.549 in the Milky Way and 133.3 in clusters, so the thresholds lie beyond it; 1.257 at r = 1 and 3.106 at r = 2.
- F6: for gates as wide as the dispersion (r = 1), the crossover 4.24 and the re-virialized threshold 9.785, "('clumping would need eps of about 4 to 10' below 3 km/s)", both beyond the model's validity.

### G. The narrow-gate corner (18 checks)

The block header names its record, `corner/runs/log_*.txt`, `diagnostics_final.out`, `injection_test.out` and `summary_numbers.out`, and the two scripts it ports. Nine of its lines read the record:

- G1 (record): 29 run logs in 10 cases — ε = 0 (the control), 1, 3 and 10 in the record's (Hamiltonian) reading, plus ε = 3 in the force law; a gate as wide as the dispersion or 2.5 times wider; three seeds per case, two for the N = 1000 control; the note describes the runs as N = 2000, with five more runs at N = 1000 that test the resolution (§8). After the switch-on the Hamiltonian runs conserve energy to max |ΔE/E| = 5.4×10⁻⁵, 23 of the 26 within the corner agent's stated 1.8×10⁻⁵, the three exceptions at ε = 10 (1.86×10⁻⁵, 2.94×10⁻⁵, 5.37×10⁻⁵); the force-law runs drift 2.0–3.8%, "as a non-conservative force should". That three runs exceed the stated 1.8×10⁻⁵ "was noticed while porting the record into `verify/`, not by an agent" (note §8).
- G2 (record): at ε = 10 with the gate as wide as the dispersion, N = 2000, ξ_u05 = −0.0069 ± 0.0063, "no velocity-selected clumping".
- G3 (record): injected clumps holding 2% of the mass raise Ξ(v\*/2) from +0.0852 to +0.2339; a 2% stream does not register and a 5% stream does; the record's reading separates the kinematic from the canonical dispersion by up to 11.5×.
- G3 (record, not adjudicated): in all seven gated cases at N = 2000, ξ_u1 exceeds the control by +0.0073 to +0.0231, 1.7–3.5σ on three seeds, while the halo's half-mass radius changes by a factor 0.685–1.647; and injected 2% clumps raise ξ_u1 from +0.0146 to +0.0409 in one snapshot, a change comparable to that offset, so "the null rests on Xi(v\*/2)", which they raise from +0.0852 to +0.2339. This too was noticed while porting the record into `verify/`, not by an agent, and the note leaves the offset unadjudicated: "nothing in the record separates the uniform ξ_u1 offset from the halo's reorganization" (§8).

The rest recompute:

- G4: the post-ramp window of 25 units is 43.3 central free-fall times, which is 0.117–0.643 Gyr in dwarfs ("0.1-0.6 Gyr"); the corner needs a second gate scale 4 to 40 times below the record's 120 km/s.
- G5: the corner's kernels at y = 1, and its printed Lyman-α responses reproduced.
- G6: at ε = 1 the Lyman-α response goes beyond the 5.3-keV warm-dark-matter template at 0.1 s/km from v\* = 3 km/s in the record's reading and 5 km/s in the force law.
- G7: ΛCDM's reionization optical depth in the proxy, 0.0575, and the corner's printed proxies reproduced; ε = 3 in the force law gives a density proxy ×9.54 and τ = 0.099 at v\* = 5 km/s, "6.4 sigma above Planck's 0.054 +- 0.007", and ×366 with τ = 0.582 at 30 km/s, "excluded at 5-30 km/s (the record's reading is singular there, E5)"; ε = 2 at v\* = 10 km/s gives τ = 0.078 (3.4σ) in both readings, "excluded from 10 km/s up"; ε = 1 gives τ = 0.073, 2.7σ high, at v\* = 30 km/s (record's reading) and 20 km/s (force law).
- G8: the heating of Segue 1 at z_min = 87.7 (limit 7.88 solar masses): at ε = 1 the moment is 39 (record's reading) and 12.5 (force law) at v\* = 5 km/s, above the limit, and 7.6 and 2.49 at 3 km/s, below it.
- G9: the corner's integrator reproduces its systems' analytic growth exponents in the uniform Einstein–de Sitter limit, labelled "(implementation check, not independent of the model)".

The N-body runs rest on one agent (note §8: "[D, executed; one agent; isolated cored halo]"); the final critic reran the linear proxies of G5–G8 with corrected formulas, a rerun by one agent (note §8: "the final critic's rerun, one agent").

### H. Cores (3 checks)

- H1: a gravitational-strength 1/r force between χ scatters at σ_T/m = 2.37×10⁻⁶² cm²/g at 30 km/s (Born approximation, ln Λ = 68.67 at b = 1 kpc), so making [dwarf-galaxy](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies) cores (30 cm²/g) needs G̃/G = 3.56×10³¹ ("3.6e31").
- H2: the exact Born transfer cross-section of a screened 1/r potential equals its numerical integral and needs G̃/G = 3.5588×10³¹; the classical routes give 3.30×10³¹ and 2.37×10³¹, "so '3.6e31' is the Born value"; the Sommerfeld parameter at that strength is 1.17×10⁻⁵, so Born is the right regime.

### I. Carriers (7 checks)

- I1: exchange of spin J between point sources has a residue that is a degree-J polynomial in γ = u₁·u₂, the Legendre P_J for a massive field and the Chebyshev T_J for a massless one (J = 0–4); the (v/c)² coefficients are J(J + 1)/4 and J²/2 (J = 0–8), and all roots lie in [−1, 1], so "for any finite spin, exchange makes the force grow with relative velocity".
- I2: an order-one effect at 120 km/s needs J = 4996.0 (massive) or 3533.1 (massless).
- I3: an infinite tower of spins reproduces the Gaussian gate only through a largest term 10^5421169 times the net force at v\* = 120 km/s (x = c²/v\*² = 6.24×10⁶). The note marks the tower "[D][V; one derivation]" (§9).
- I4: continuous-spin exchange (Schuster, Toro and Zhou 2023, eq. 129 [S]) matters when ρvr/(ħc) ~ 1: ρ = 1.598×10⁻²³ eV for 120 km/s at 1 kpc, ten times smaller at 10 kpc; its correction depends only on the relative velocity and vanishes for bodies moving together and for motion along the line joining them.
- I5: non-relativistically the record's gate on the incoming relative momentum survives at long range, the quantum expectation matching the classical gated value to 5×10⁻⁵ at 100 ħ/μ, with ħ/μ = 1.0×10⁻¹¹ m: "the gate is contact-range because X is massive".

The page is [what could carry a relative-velocity gate](/wiki/dark-matter/conjugate-matter/gate-carriers); I5 bears on [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism).

### J. The Vainshtein radius (3 checks)

The block header names flag 57 in `review/wiki-build-flags.md`.

- J1: in r_V³ = K r_S λ², the program's palindromic vacuum gives K = 1 (Enander and Mörtsell's eq. 40) and 15 (eq. 41); the form that assumes one mode massless (eq. 43), used at `verify/phase_space_diameter.py` line 383, gives K = 2, and in the palindromic vacuum it would make X massless.
- J2: for 1 kg at λ_X = 50 μm, r_V = 1.55×10⁻¹² m (eq. 40), 3.82×10⁻¹² m (eq. 41) and 1.95×10⁻¹² m (eq. 43); under eq. 41 the rounding check at line 384 of that script would fail; laboratory masses stay unscreened.
- J3: if this branch screens at all, which is open, the Sun's Vainshtein radius covers Saturn for λ > 1.024 pc (eq. 40) or 0.264 pc (eq. 41), and the windows open at about 0.3–9 pc and close at Enander and Mörtsell's 4.4 kpc.

Flag 57's audit: "the source equations were read twice [S]: by the run-3 critic-numbers verifier, and by the drafting session (its fetch is in the session transcript, not the record). The final critic adopted the verifier's ruling without rechecking them." The note cites the equations "[S, read by the run-3 critic-numbers verifier and by the drafting session on 2026-10-27]". The flag places the 4.4 kpc edge at the edge of Enander and Mörtsell's linear-theory lensing window [T][S]. The check that the flag concerns is described on [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script).

## What it does not recompute

The docstring says what was not ported:

```text
Two ports are reduced, without changing any printed digit: the critic's
kernel table (critic3/c1) is built only on its nodes up to y = 3 (the v* =
120 km/s runs never leave y < 1.2; the code refuses y in (3, 300]), and the
corner's kernels (corner/linear_corner.py) evaluate sin and cos once per
node. Not recomputed: the N-body runs (see above); the satellite-count proxy
corner/sat_proxy.py (the critic did not rerun it either); the superseded
round-2 analyses except where a superseded number is quoted.
```

- **The N-body runs.** The 29 runs of the narrow-gate corner took hours and their snapshots, about 90 megabytes, were not kept (`review/momentum-gravity/README.md`, 'Not kept'). The checks marked "(record)" in block G read the runs' logs and the diagnostics, injection and summary outputs in `review/momentum-gravity/scripts/corner/`, and recompute nothing. They confirm that the note quotes the record correctly, not that the simulations are right; the runs rest on one agent, and the offset in ξ_u1 is not adjudicated.
- **The satellite-count proxy.** It was not rerun with the corrected formulas (note §8, 'Not computed'), and the script does not port it.
- **The literature and the inputs.** Published values are typed in: Planck 2018, the DESI DR1 and eBOSS Lyman-α compressions, the planetary ephemerides, the double pulsar, Lee et al. 2020, the Sagittarius model of Vasiliev and Belokurov 2020 and Enander and Mörtsell 2013. Whether the cited works say what the note quotes rests on retrieval ([S]), not on the script; for the Vainshtein formulas the equations were read twice, by the run-3 critic-numbers verifier and by the drafting session, whose fetch is in the session transcript, not the record (block J).
- **The models.** The long-range attraction is a hypothesis outside the record, tested in three readings; the Lyman-α bounds and the corner's proxies are "estimates, not likelihoods" (note §§6, 8), and a full Lyman-α likelihood is open (§10). Whether the Hamiltonian reading is the right classical limit is open [O] (§5). The script checks arithmetic, not the model ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).
- **Single-derivation results.** The note marks the tower of spins and the medium "[one derivation]" (§9), and the pathology of gating on peculiar velocities alone in the Hamiltonian reading "(one agent; not rechecked)" (§5); the last is not among the script's checks.
- **The rest of the clumping problem.** Block D covers calc note #2's shortfall only. The numbers of calc note #3 and #4, and the classicality corollary's mass and occupation number, have no check in `verify/`.

## The recorded output

The run of 2026-10-28:

```text
== Anchors (independent of the investigation)
PASS  A1: CODATA 2018 hbar c = 197.3269804 MeV fm  [1.9732698034e-07 eV m]
PASS  A1: CODATA 2018 Planck mass 2.176434e-8 kg  [2.176434e-08]
PASS  A2: Fokker action: massless spin-2 exchange at O(v^2) reproduces the O(G) terms of the Einstein-Infeld-Hoffmann Lagrangian (G m1 m2/r)[1 + 3/2(v1^2 + v2^2) - 7/2 v1.v2 - 1/2 (n.v1)(n.v2)] (Landau-Lifshitz sec. 106) exactly; spin 1 reproduces the Darwin Lagrangian (LL sec. 65); Y = e^(-Mr)/4pi r, Z = e^(-Mr)/8pi M solve their equations
PASS  A3: textbook numerators normalized to their static value: de Donder (massless) (gamma^2 - 1/2)/(1/2) = 2 gamma^2 - 1 = T_2(gamma); Fierz-Pauli (gamma^2 - 1/3)/(2/3) = (3 gamma^2 - 1)/2 = P_2(gamma); static ratio massive/massless 4/3 (vDVZ), 3/4 as gamma -> infinity
PASS  A3: point-mass stress tensors: T1.T2 - c T1 T2 = m1 m2 ((u1.u2)^2 - c) at five random velocity pairs (40 digits)
PASS  A4: Planck 2018 LCDM (TT,TE,EE+lowE+lensing): the dark-tests background (massless neutrinos) gives age 13.795 Gyr (published 13.797 +- 0.023) and z_eq = 3419 (3402 +- 26, within 1 sigma); the derivation verifier's (one massive neutrino) gives 13.797 Gyr  [13.7952, 3418.8; 13.7966]
PASS  A4: Planck 2018 + BAO column (the Lyman-alpha background, h = 0.6766, omega_c = 0.11933, omega_b = 0.02242, massless neutrinos): age 13.80 Gyr, within 1 sigma of the published 13.787 +- 0.020 (dagger)  [13.8041 Gyr]
PASS  A4: sigma8 normalization of the EH98 no-wiggle P(k) returns 0.8111 (regression: normalization, not an anchor)  [0.81110]
PASS  A5: Meszaros (matter + smooth radiation): D = 1 + 3a/(2 a_eq) is exact; the cosmo.py integrator holds it to 1e-9 from a = 1e-6 to 1  [max deviation 4.4e-12]
PASS  A6: gate kernel R(y) = y Int_0^inf sin(yt) e^(-t^2/2) dt = sqrt(pi/2) y e^(-y^2/2) erfi(y/sqrt2) (closed form): the critic's quadrature matches it at y = 0.3, 1, 1.08, 3 to 1e-8, inside the 6 decimals its kernels are quoted to  [7.5e-11, 8.3e-10, 9.7e-10, 7.5e-09]
      [8.5 s]
PASS  A5: Einstein-de Sitter: from delta = 1, delta' = 0 at a_i the exact solution is (3/5)(a/a_i) + (2/5)(a/a_i)^(-3/2); both growth integrators (critic's and corner's) reproduce it at a = 1 to 1e-8  [-1.6e-11, 6.5e-12]
PASS  A7: the range interpolation reproduces Lee et al. 2020's published 38.6 um (|alpha| = 1) and 30 um (alpha = 8/3)  [38.63, 30.23 um]
PASS  A8: GR perihelion advance of Mercury 6 pi G M/(c^2 a (1 - e^2)) per orbit from the fact-sheet a, e, P: 43.0 arcsec/cy (textbook 42.98)  [42.979 arcsec/cy]
PASS  A9: Plummer sphere in N-body units: central free-fall time 1/sqrt(4 pi G rho0) = 1/sqrt3 = 0.5774
      [10.6 s]

== B. X between ordinary bodies (ports of verify/phase_space_diameter.py's range, verify-program-derivation/v1_spin2_fokker.py, critic3/c4_numbers.py (d), verify-critic-theory/v4_force_dual.py)
PASS  B0: X (massive spin 2, Fierz-Pauli) at O(v^2): alpha G m1 m2 e^(-Mr)/r [1 + v1^2 + v2^2 - 5/2 v1.v2 - 1/2 (n.v1)(n.v2)] - (alpha G m1 m2 M/2) e^(-Mr)(n.v1)(n.v2): a Yukawa with relativistic O(v^2/c^2) terms, no gate
PASS  B0: V = -(G m1 m2/r)(1 + alpha e^(-r/lambda_X)), alpha = 4u^2/3 = 4/3 at the aligned vacuum u = 1: unscreened lambda_X < 37.7 um, M_X c^2 > 5.2 meV (recomputed here; also gated in verify/phase_space_diameter.py); 57.0 um at u = 0.5, 30.8 um at u = 1.5  [37.68 um, 5.237 meV; 56.98, 30.83 um]
PASS  B1: X's velocity factor (3 gamma^2 - 1)/2 - 1 = 2.40e-7 at 120 km/s; graviton 2 gamma^2 - 1 - 1 = 3.20e-7 (critic: 2.403e-07, 3.204e-07)  [2.4033e-07, 3.2044e-07]
PASS  B1: both factors grow monotonically with relative velocity (d/dgamma > 0 for gamma > 1): no velocity gate at any range
PASS  B1: u1.u2 = gamma_rel = 1 + |v1 - v2|^2/2 + O(v^4): the factor depends on the relative velocity
PASS  B2: #13's dual kinematics, Sun-Earth: F/c~ = 2.93e-22, gamma~ - 1 = 4.28e-44 (the answer's '(F/c~)^2 ~ 4e-44'; (F/c~)^2 itself is 8.56e-44 = 2(gamma~ - 1)), or zero if free fall is dual rest (#13 sec. 5)  [F/c~ = 2.9263e-22, gamma~-1 = 4.2816e-44]
PASS  B2: Siegel reading (flag 39): the X-linear term sits in the mixed blocks with size X (v/c)(F/c~) = vF/(c^5/G) = 2.91e-26 ~ 3e-26 for Sun-Earth  [2.9073e-26]
PASS  B2: Siegel generalized metric (d = 2): symplectic, det 1, and its part linear in X lies only in the mixed blocks
      [12.6 s]

== C. A universal relative-velocity gate between ordinary bodies (ports of verify-ordinary-tests-numbers/vot_bounds_lib.py, vot_bounds.py, vot_topend.py; critic3/c4_numbers.py (e, g); verify-critic-numbers/u4)
PASS  C0: exp(-v^2/v_a^2) equals the record's amplitude gate exp(-v^2/(2 v*^2)) iff v_a = sqrt2 v*: v_a = 169.7 km/s at v* = 120; the scan v_a = 0.3-3000 km/s is v* = 0.21-2121 km/s ('0.2-2100' in the record's convention)
PASS  C1: double-pulsar mass-bias factor (masses from omega-dot and Shapiro s, Kramer et al. 2021 sec. VI.2.1) 2.4666, so |d omega-dot/omega-dot| < 5.27e-5 from their 1.3e-4  [2.4666, 5.270e-05]
PASS  C2: at v_a = 120 km/s Mars's perihelion binds: 1.82e-11 (Earth 4.04e-11, Mercury 6.37e-11)  [1.817e-11]
PASS  C2: the interim's '2e-11 from Mercury' is INPOP15a's 1-sigma anomalous advance (3.1 mas/cy, criterion 1; 2.075 mas/cy, mean) at v_a = 120 km/s: eps < 2.5e-11 and 1.7e-11, in the ordinary-tests convention (verify-program-numbers/n6_mercury_bound.py)  [2.469e-11, 1.653e-11]
PASS  C2: at the record's v* = 120 km/s (v_a = 170): |eps| < 3.5e-11 from Mars's perihelion (Gaussian; Lorentzian 3.64e-11)  [3.497e-11, 3.641e-11]
PASS  C3: Gaussian gate, envelope over v_a = 0.3-3000 km/s: |eps| < 8.65e-9 ('8.7e-9'), weakest at the 3000 km/s end, set by the double pulsar  [8.652e-09 at 3000 km/s (double pulsar)]
PASS  C3: Lorentzian gate, envelope over v_a = 0.1-3000 km/s: |eps| < 9.42e-9 ('9.4e-9'), double pulsar at 3000 km/s  [9.418e-09 (double pulsar)]
PASS  C3: leading order u -> 0: d omega-dot/omega-dot_GR = -(2/3)(c/v_a)^2 eps (Mercury at v_a = 30000 km/s: -66.574), so the double-pulsar limit gives 5.27e-5 (3/2)(v_a/c)^2 = 7.92e-9 at 3000 km/s (critic c4 (e))  [-66.5741]
PASS  C4: below v_a ~ 0.3 km/s there is no numerical bound: the Gaussian envelope's weakest point on 0.1-0.3 km/s is eps < 0.615 (Eros)  [0.615 at 0.176 km/s]
PASS  C4: qualitative exclusion there: a body at rest at the pole has inertia m(1 - 2 G M eps/(R v_a^2)), which vanishes at eps = 7.97e-5 for v_a = 0.1 km/s  [7.9738e-05]
      [13.6 s]

== D. The obituary's scope: calc note #2's shortfall (ports of review/wiki-build-checks/stream_stability_check.py and verify-clumping-numbers/v09_units.py)
PASS  D1: calc note #2's record logic (stream_stability_check.py, the critic's run c3): g = 2.48e3 GeV^-2; the contact gate's collective pull over m min(sigma, v*)^2 is 3.9e-28 (dwarf core) and 2.9e-31 (MW)  [2483; 3.8878e-28, 2.8637e-31]
PASS  D1: so the pull is 10^-27.4 (dwarf core) to 10^-30.5 (MW) of threshold ('falls short by 10^28-10^31' quotes the ratios' printed exponents e-28 and e-31; the shortfall factors are 2.6e27 and 3.5e30)  [log10 = -27.41, -30.54]
PASS  D2: linearized (clumping C6, CODATA): g n Lambda_g(sigma/v*)/(m sigma^2) = 3.27e-28 (dwarf core), 8.7e-31 (MW)  [3.2733e-28, 8.6968e-31]
PASS  D3 (flag 58): for a gate narrower than the dispersion the linearized criterion is g n Lambda_g >= m sigma^2; 3a's form g n (v*/sigma)^3 (2 pi)^(-3/2) >= m v*^2 overstates the MW shortfall by (2 pi)^(3/2) r Lambda_g(r) = 3.04 ('about 3x') at r = 155/120; the verdict is unchanged  [3.0370]
      [13.6 s]

== E. The long-range chi-only gated attraction U = -eps G m^2 W(|v - v'|/v*)/r (ports of critic3/c1_hamiltonian_system.py, critic3/c4_numbers.py (c), dark-tests/r_gate.py, verify-dark-tests-derivation/v3_misc.py, verify-critic-numbers/u7_sgr_bound.py)
PASS  E1: kernels at the DESI pivot y = 1.08, by quadrature of their definitions: R = 0.803130 (the round-2 agent's density kernel), R1 = 0.311446 (the force law's), 2.58x smaller; R_v = 0.536423, B = -0.938630  [R 0.803130, R1 0.311446, J -0.455263, R_v 0.536423, B -0.938630]
PASS  E1: kernel identities R1 - yJ = R, R_v - B = -3yJ, R1 = Int_0^1 R(y mu) dmu, R_v = 3 Int mu^2 R(y mu) dmu, to 1e-8  [6.5e-10, 1.7e-09, 1.1e-16, 1.4e-09]
PASS  E1: pivot k = 0.009 s/km at z = 3 is 0.6898/Mpc; y_p = k_p v*/(aH) = 1.0800 at v* = 120 (the gate in velocity units is v* at every epoch)  [0.68979, 1.080000]
      agent: eps = 0.1: T_m^2 = 1.0784, dn_m = +0.1310 | T_b^2 = 1.0248, dn_b = +0.0459;  eps = 1: T_m^2 = 2.1307, dn_m = +1.3150
      F    : eps = 0.1: T_m^2 = 1.0356, dn_m = +0.0637 | T_b^2 = 1.0111, dn_b = +0.0211;  eps = 1: T_m^2 = 1.4259, dn_m = +0.6549
      H    : eps = 0.1: T_m^2 = 0.9478, dn_m = -0.0603 | T_b^2 = 0.9796, dn_b = -0.0331;  eps = 1: T_m^2 = 0.5296, dn_m = -0.8718
      c4b  : eps = 0.1: T_m^2 = 0.9862, dn_m = +0.0048 | T_b^2 = 0.9926, dn_b = -0.0091;  eps = 1: T_m^2 = 0.7330, dn_m = -0.4306
PASS  E2: DESI pivot, v* = 120 km/s, z = 3, eps = 0.1: record's reading (H) T_m^2 = 0.9478, dn = -0.0603 (a suppression); force law 1.0356, +0.0637; c4b's transcription 0.9862, +0.0048; round-2 agent's hybrid 1.0784, +0.1310  [H 0.947755]
PASS  E3: compressed DESI DR1, v* = 120 km/s, delta chi^2 = 3.84 with baseline errors: record's reading eps < 0.0570 (matter ratio) / 0.1063 (gas ratio) -> 'eps < 0.06 to 0.11'  [0.05700 / 0.10625]
PASS  E3: force-law reading eps < 0.0585 / 0.1755 -> the bracket '0.06-0.18' (critic: 0.0585/0.176)  [0.05845 / 0.17553]
PASS  E3: the superseded numbers come from the flawed systems: the round-2 agent's hybrid gives 0.028 (matter; the interim's '0.03'); c4b's system gives 0.358/0.305 with baseline errors, 0.354/0.299 with DESI errors only (c4b printed 0.3405/0.2959: the '0.34' that counted -H A_delta twice)  [agent 0.0285; c4b 0.3583/0.3052, DESI-only 0.3537/0.2994]
PASS  E3 (record): the second, independent derivation (VDD v3_lya_withbase.out: H 0.0572/0.1069, force law 0.0585/0.1760) and this port round alike to the quoted 0.06/0.11 (H) and 0.06/0.18 (force law)  [largest difference 0.61%]
PASS  E4: eBOSS compression in the record's reading: chi^2 falls from 26.31 (eps = 0) to 1.90 at eps = 0.0535 (upper bound 0.0741); delta chi^2 = 24.4, 4.94 'sigma' for one parameter (not evidence: the data sit 4.90 sigma from Planck [S, arXiv:2311.16377])  [26.308 -> 1.895 at 0.05345; bound 0.07408]
PASS  E4: step test: T_m^2(eps = 0.1, H) is 0.947755 with 8000 and 16000 RK4 steps  [0.9477547, 0.9477547]
PASS  E5: the record's reading becomes singular where 1 + kappa B = 0: min B = -1.0712 at y = 1.41, so eps = 2/(1.0712 Omega_c) = 2.248 (z = 50, Omega_c = 0.8305), 2.236 (z = 10, 0.835), 2.293 (z = 3, 0.8143): linear theory fails above eps ~ 2.2  [-1.07117 at y = 1.412; Omega_c(10) on the dark-tests background 0.8388 gives 2.226]
PASS  E6: Hubble gate radius r_gate = v*/H0 = 1.781 Mpc for v* = 120 km/s (proper, today); the comoving gate radius peaks at 2.028 Mpc at z = 0.631, where the expansion turns from deceleration to acceleration ((2 Omega_L/Omega_m)^(1/3) - 1 = 0.631)  [1781.473 kpc; 2.0277 Mpc at z = 0.631]
PASS  E7: gate average closed form (0.06136 at V = 317.6, sigma_rel = 120) against quadrature (1e-9) and a Monte Carlo of 20 independent runs of 2e5 pairs (pull < 3 sigma)  [MC 0.06143 +- 0.00008]
PASS  E7 (record): u7's MC '0.06150 +- 0.00004' is 3.3 sigma from the closed form on its own 10-run error bar, but 2.2 sigma on the exact variance (sigma of a 4e6-pair mean = 6.1e-5): its error bar came out low, the closed form stands  [pull 2.19]
PASS  E7: Sgr, force-law mapping: <W> = 0.0656 at V = 311.1 km/s, so KK's 10% gives eps < 1.52 (round 2's '1.5')  [0.06565]
PASS  E7: Sgr, record's reading (VDD D14, order of magnitude): the satellite chi's inverse mass shifts by eta_perp = +0.27..+0.30 eps and eta_par = -0.44..-0.49 eps (host truncated at 200-300 kpc), so eps < 0.1/|eta| = 0.20-0.37  [+0.2712 +0.3035; -0.4379 -0.4900]
PASS  E7: Sgr, three toy Milky-Way potentials x three host dispersions x four orbit weightings (VCN u7, 3-Gyr orbits): eps < 0.36-2.46; with VDD's 0.20 the quoted range is 'of order 1 (0.2-2.5)'  [<W> in [0.0406, 0.2781]]
PASS  E8: clumping needs eps > 1 at every gate width (F2), so the allowed strength is at least 1/0.1755 = 5.7x ('6x') too small, 1/0.1063 = 9.4x ('9x') in the record's reading; eps = 4/3 exceeds the record-reading gas bound 12.5x  [5.70, 9.41, 12.55]
      [22.4 s]

== F. Clumping thresholds (ports of verify-critic-numbers/u2_c5_static_thresholds.py, u10_crossover_43.py, critic3/c4_numbers.py (a, b), corner/local_compare.py)
PASS  F1 anchors: gt = 0 gives Lambda_0 = 1 (Jeans criterion); r -> 0 gives 1 + gt (gate = 1): 3.9991 at r = 0.01, gt = 3; the secular root equals the dense eigenvalue to 1e-12
PASS  F1: the gate-only top eigenvalue Lambda_g = [1/2 + r^2 + sqrt(1 + 4r^2)/2]^(-3/2) matches the Nystrom operator: 1.4928686e-01 (MW, r = 155/120), 1.4435026e-03 (cluster, r = 1000/120); Lambda_0(1.2917, 10) = 2.30511  [1.4928686e-01, 1.4435026e-03]
PASS  F2: velocity-selected clumping needs eps > 1/Lambda_g(sigma/v*): increasing in r, min over r in [1e-3, 10] = 1.000003 (so eps > 1 everywhere); 1/Lambda_g(1) = phi^3 = 4.236 (so eps >= 4.24 wherever sigma >= v*); 1/Lambda_g = 4/3 at r = 0.33282  [min 1.0000030; 4.236068]
PASS  F3: Milky Way (sigma = 155, v* = 120, r = 1.2917, <W> = 0.1107): threshold 28.07 at the core margin Q = pi^2/2, 127.5 at 2 pi^2, 161.2 at the solar-circle (lambda_J/R0)^2 = 24.771 ('28-161'); none (inf) once the halo re-virializes ('at least 28, or none')  [28.0749, 127.52, 161.25]
PASS  F3: clusters (sigma = 1000, r = 8.333): velocity-selection crossover 692.8 ('at least 690'); the instability threshold at Q = (pi/3)^2 is 152.2 (the interim's 'at least 152'), 798.8 re-virialized  [692.7594; 152.223 / 798.804]
PASS  F4: margins at v* = 120 over the allowed eps: 28.07/0.1063 = 264 (MW), 692.8/0.1063 = 6.52e3 (clusters), 28.07/2.46 = 11.4 (loosest Sgr mapping)  [264.2, 6520, 11.41]
PASS  F5: the local model holds only for eps < (1 + r^2)^(5/2)/(4.5 r^2): 1.549 (MW), 133.3 (clusters), so the thresholds 28 and 690 lie beyond it; 1.257 at r = 1, 3.106 at r = 2
PASS  F6: gates as wide as the dispersion (r = 1): crossover 4.24, re-virialized threshold 9.785 at Q = (pi/3)^2 ('clumping would need eps of about 4 to 10' below 3 km/s), both beyond the model's validity (1.257)  [9.7845]
      [23.7 s]

== G. The low-v* corner (record: corner/runs/log_*.txt, diagnostics_final.out, injection_test.out, summary_numbers.out; recomputed: ports of corner/phys_scales.py and critic3/c2_corner_recheck.py)
PASS  G1 (record): 29 run logs: eps = 0 (control), 1, 3, 10 in the record's (Hamiltonian) reading plus eps = 3 in the force law; gate as wide as (r_g = 1) or 2.5x wider than (r_g = 0.4) the dispersion; three seeds per case, two for the N = 1000 control  [10 cases]
PASS  G1 (record): after the ramp the Hamiltonian runs conserve energy to max|dE/E| = 5.4e-5 (23 of the 26 within the corner's stated 1.8e-5; the three eps = 10 exceptions are 1.86e-5, 2.94e-5, 5.37e-5); the force-law runs drift 2.0-3.8%, as a non-conservative force should  [H max 5.37e-05; F [0.0198, 0.0221, 0.0376]]
PASS  G2 (record): eps = 10, gate = dispersion, N = 2000: post-ramp xi_u05 = -0.0069 +- 0.0063 (no velocity-selected clumping)
PASS  G3 (record): sensitivity: injected clumps holding 2% of the mass raise Xi(v*/2) from +0.0852 to +0.2339; a 2% stream does not register (Xi(v*/2) +0.0396, S2 +0.088 within the control errors); a 5% stream does (S1 +0.8181)
PASS  G3 (record): the record's reading separates kinematic from canonical dispersion by up to 11.5x (eps = 10, r_g = 1)
PASS  G3 (record, not adjudicated): in all 7 gated N = 2000 cases xi_u1 exceeds the control by +0.0073 to +0.0231, 1.7-3.5 sigma on three seeds, while the halo's r50 changes by a factor 0.685-1.647  [pulls 2.08, 1.70, 2.98, 2.67, 3.45, 2.45, 1.65]
PASS  G3 (record, not adjudicated): injected 2% clumps raise xi_u1 = Xi(v*) from +0.0146 to +0.0409 in one snapshot, a change comparable to that offset; the null rests on Xi(v*/2), which they raise from +0.0852 to +0.2339
PASS  G4: the runs' post-ramp window of 25 units is 25/0.5774 = 43.3 central free-fall times; dwarf t_ff = 14.96, 8.66 Myr (classical dSph, Read-Walker-Steger 2019) and 2.71 Myr (Segue 1, Simon et al. 2011), so 43 t_ff = 0.117-0.643 Gyr ('0.1-0.6 Gyr')
PASS  G4: the corner needs a second gate scale 120/30 = 4 to 120/3 = 40 times below the record's 120 km/s
      [23.7 s]
PASS  G5: corner kernels at y = 1 (c4b's printout): R = 0.72478, R_v = 0.47699, R_a = -0.87168, J_W = -0.44956
PASS  G5 anchors: the corner's printed Lyman-alpha responses reproduce (z = 4.2, k = 0.05/0.1/0.2 s/km, v* = 10, eps = 1): H 0.927/0.754/0.932, K4 1.2/1.92/6.91
PASS  G6: eps = 1, Lyman-alpha against the 5.3-keV WDM template at 0.1 s/km: beyond it from v* = 3 km/s (record's reading, T^2 = 0.939) and 5 km/s (force law, 1.08); the force law passes at 3 km/s (1.03)
      eps = 1, v* = 10, K4: density proxy 1e9 Msun x2.17, tau(ii) = 0.068
      eps = 1, v* = 20, H : density proxy 1e9 Msun x2.14, tau(ii) = 0.071
      eps = 3, v* =  5, Fc: density proxy 1e9 Msun x9.54, tau(ii) = 0.099
      eps = 3, v* = 30, Fc: density proxy 1e9 Msun x366, tau(ii) = 0.582
      eps = 2, v* = 10, Hc: density proxy 1e9 Msun x4.39, tau(ii) = 0.078
      eps = 2, v* = 10, Fc: density proxy 1e9 Msun x3.59, tau(ii) = 0.078
      eps = 1, v* = 30, Hc: density proxy 1e9 Msun x2.27, tau(ii) = 0.073
      eps = 1, v* = 20, Fc: density proxy 1e9 Msun x2.82, tau(ii) = 0.073
PASS  G7 anchors: LCDM tau(ii) = 0.0575; the corner's K4 (eps = 1, v* = 10: x2.17, tau 0.068) and H (eps = 1, v* = 20: x2.14, tau 0.071) reproduce
PASS  G7: eps = 3, force law (fixed-velocity reading): at v* = 5 km/s the 1e9-Msun density proxy is x9.54 and tau(ii) = 0.099 (6.4 sigma above Planck's 0.054 +- 0.007); at 30 km/s x366, tau 0.582: excluded at 5-30 km/s (the record's reading is singular there, E5)  [9.5427, 0.0988]
PASS  G7: eps = 2 at v* = 10 km/s: tau(ii) = 0.078 (3.4 sigma) in both readings, density x4.39 (record's) and x3.59 (force law): excluded from 10 km/s up
PASS  G7: eps = 1: tau(ii) = 0.073, 2.7 sigma high, at v* = 30 (record's reading) and 20 km/s (force law); dwarf densities x2.27 and x2.82 ('x2.3-2.8')
PASS  G8: Segue 1 heating moment at z_min = 87.7 (limit 7.88 Msun): the corner's anchors 1.05e3 (H) and 742 (K4) at v* = 10 reproduce; eps = 1 at v* = 5 gives 39 (record's reading) and 12.5 (force law), above the limit; at v* = 3, 7.6 and 2.49, below it  [1.05e+03, 742, 39, 12.5, 7.6, 2.49]
PASS  G9: the corner's integrator in the Einstein-de Sitter uniform limit reproduces its systems' analytic growth exponents (force law 1.73205, 3.00000; record's reading 1.88600, 3.63104 at eps = 1, 3) to 1e-4 (implementation check, not independent of the model)  [1.73205, 3.00000, 1.88600, 3.63104]
      [34.0 s]

== H. Cores (ports of verify-dark-tests-derivation/v3_misc.py K16, verify-dark-tests-numbers/vscatter.py, verify-critic-numbers/u5_c6C_born.py)
PASS  H1: a gravitational-strength 1/r chi-chi force scatters at sigma_T/m = 2.37e-62 cm^2/g at 30 km/s (Born, ln Lambda = 68.67 at b = 1 kpc; eta = 3.29e-37); dwarf cores (30 cm^2/g) need G~/G = 3.56e31 ('3.6e31')  [2.3688e-62, 3.5588e+31]
PASS  H2: the exact Born transfer cross-section of a screened 1/r potential, (2 pi al^2/mu^2 v^4)[ln(1 + 4k^2b^2) - 4k^2b^2/(1 + 4k^2b^2)], equals its numerical q-integral; it needs G~/G = 3.5588e31 (b = 1 kpc); the classical routes give 3.30e31 (self-consistent log) and 2.37e31 (ln N = 155.1), so '3.6e31' is the Born value  [3.55877e+31, 3.2990e+31, 2.3680e+31]
PASS  H2: Born is the right regime: the Sommerfeld parameter G~ m^2/(hbar v) at G~/G = 3.56e31, 30 km/s is 1.17e-5
      [34.1 s]

== I. Carriers (ports of verify-critic-theory/v1_spinJ_residues.py, v2_tower_gate.py, v3_gate_range.py, v7_misc_numbers.py; critic3/c4_numbers.py (f))
PASS  I1: spin-J exchange between point sources: the residue is the traceless projection, a degree-J polynomial in gamma = u1.u2: Legendre P_J (massive, 3 states orthogonal to q) and Chebyshev T_J (massless, 2 helicities), J = 0-4  [max deviation 2.8e-15]
PASS  I1: (v/c)^2 coefficients J(J + 1)/4 (massive) and J^2/2 (massless), J = 0-8; all roots lie in [-1, 1], so every residue grows with gamma > 1: for any finite spin, exchange makes the force grow with relative velocity
PASS  I2: an O(1) effect at 120 km/s needs J = 4996.0 (massive, J(J + 1)/4 (v/c)^2 = 1) or 3533.1 (massless): 'spin 3500-5000'; there P_4996(gamma*) - 1 = 1.28, T_3533(gamma*) - 1 = 1.18  [4996.04, 3533.09]
PASS  I3: an infinite spin tower: exp(-x(gamma - 1)) = e^x Sum (2J + 1)(-1)^J i_J(x) P_J(gamma) (checked at x = 5); its largest term (2J + 1) e^(2x)/(2x) e^(-J(J+1)/2x) (exact to 3e-4 in log10 at x = 320-3000) is 10^5421169 times the net force at v* = 120 km/s (x = c^2/v*^2 = 6.24e6)  [log10 = 5421168.812; 2.7e-04, 9.0e-05, 3.0e-05]
PASS  I4: continuous-spin exchange (Schuster-Toro-Zhou 2023, eq. 129 [S]): the correction matters when rho v r/(hbar c) ~ 1: rho = 1.598e-23 eV for 120 km/s at 1 kpc, ten times smaller at 10 kpc (the switch-on velocity falls with distance)
PASS  I4: eq. 129's correction (|v_i - v_j| - (v_i - v_j).r^)^2 depends only on the relative velocity, vanishes for bodies moving together and for relative motion along r^
PASS  I5: the record's gate on the incoming relative momentum survives at long range non-relativistically: at 100 hbar/mu the quantum expectation matches the classical gated value to 5e-5 (1.000051); hbar/mu = 1.0e-11 m (mu c = 19.8 keV): the gate is contact-range because X is massive  [1.0000509]
      [34.4 s]

== J. Flag 57: the Vainshtein radius (port of verify-critic-numbers/u6_c6E_vainshtein.py)
PASS  J1: in r_V^3 = K r_S lambda^2 at c = 1: the palindromic vacuum (beta3 = beta1, so m1 = m2 for any beta1, beta2) gives K = 1 (eq. 40) and 15 (eq. 41); the m1 = 0 form (eq. 43, used at verify/phase_space_diameter.py:383) gives K = 2, and m1 = 0 = m2 there would make X massless  [{'40': 1, '41': 15, '43': 2}]
PASS  J2: a 1 kg mass with lambda_X = 50 um: r_V = 1.55e-12 m (eq. 40), 3.82e-12 m (eq. 41) ('1.5-3.8e-12 m'), 1.95e-12 m (eq. 43); under eq. 41 round(log10 r_V) = -11, so the rounding check at verify/phase_space_diameter.py:384 would fail; lab masses stay unscreened  [1.549e-12, 3.819e-12, 1.951e-12]
PASS  J3: if this branch screens at all (open), the Sun's Vainshtein radius covers Saturn for lambda > 1.024 pc (eq. 40) or 0.264 pc (eq. 41), Pluto for 8.560 or 2.210 pc: the windows open at ~0.3-9 pc and close at Enander-Mortsell's 4.4 kpc (their published linear-theory lensing window, 4.4 kpc-4.4 Mpc at u ~ 1 [T][S])

wall time 34.6 s

OK — every number of the velocity-gated-gravity investigation reproduces.
```

## Sources

- `verify/velocity_gated_gravity.py` — the docstring with its scope, anchors, inputs, reduced ports and what is not recomputed; every check and label; its output — the 93 `PASS` lines of the run recorded above
- `notes/velocity-gated-gravity.md` header — "Every number is recomputed in `verify/velocity_gated_gravity.py` (§9's medium in `verify/gate_mechanism.py`), except the N-body runs of §8, whose record is kept"; §1 — the gate conventions; §§2–9 — the numbers the script reproduces, the one-agent and one-derivation marks, the unadjudicated ξ_u1 offset and what was not computed; §11 — the corrected and withdrawn numbers
- `review/momentum-gravity/README.md` — the record, the scripts beside their outputs, and what was not kept (the N-body snapshots); `review/momentum-gravity/scripts/corner/diagnostics_final.out` and `review/momentum-gravity/scripts/corner/injection_test.out` — two of the outputs block G reads
- `review/momentum-gravity/answer.md` — the answer as given to Paul, whose numbers the script checks
- `review/wiki-build-checks/stream_stability_check.py` — the wiki build's recomputation that block D ports
- `scripts/check.sh` — the script's place in the gate
- `CLAUDE.md` 'Layout' — the script listed with the momentum-gravity notes; 'Method (HANDOFF §5)' — the anchor rule
- `review/wiki-build-flags.md` items 16 (addendum), 39, 56, 57, 58 — the clumping check mark now backed by block D; the Siegel reading; #13's dual rest; the Vainshtein formula; calc note #2's narrow-gate criterion
