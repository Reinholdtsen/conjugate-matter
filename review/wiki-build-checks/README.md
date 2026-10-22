# Executed checks behind `review/wiki-build-flags.md`

These scripts were written by the wiki depth-pass verifiers (2026-10-21) in the session
scratchpad and copied here with their printed output (`*.out`), so that every flag that
rests on arithmetic has executed code beside it. They are evidence for a ruling, not part of
the gate: none is wired into `scripts/check.sh`. A ruling that accepts a flag should move
the relevant check into `verify/`, with an anchor independent of the paper.

Run one with `cd review/wiki-build-checks && ../../.venv/bin/python <script>.py`.

| Script | Flag | What it prints |
| --- | --- | --- |
| `verifier_null_lagrangians.py` | 1 | ω and η vanish (~1e-16) on continuous families V ⊕ V^⊥ at d = 2, 3; det² is constant (±1) on each family |
| `zero_locus.py` | 3 | {J₀, I[Z]} ≈ 2e-15 at a point with X ≠ 0 |
| `s_expansion.py` | 4 | S − (2εh + ε²x²) is O(ε²) with coefficient |h²|; adding −ε²h² makes the residual O(ε³) |
| `sqrt_eig_check.py` | 14 | p₄ of the eigenvalues of √(g⁻¹f) equals Tr(g⁻²); of √(f⁻¹g), Tr(g²) |
| `squeeze_check.py` | 12 | V_b changes under the squeeze diag(a, 1/a) off the line K = K_ref (sympy) |
| `jk_check.py` | — | η = HJ and η = ωK are the same matrix under #11 §5's algebra; the J/K clash (inventory conflict C27) is a naming one |
| `gate_conventions.py` | 17 | the two gate forms differ by √2 in μ |
| `self_dual_locus.py` | 23 | a·ã = 1 on the whole axis X = 0; |Z| = 1 only at Z = i; also the dictionary w_eff = −w̃ |
| `v_sign_check.py` | 27 | V₀[1 + cos(τ/f)] has minimum 0; a turnaround needs V < 0 |
| `dirac_coupling_check.py` | 28 | 4π/e² = 1/α ≈ 137; g²/4π = 1/(4α) ≈ 34.26 |
| `quadratic_gap.py` | 31 | a lead: with a † Fermi-LAT bound, ~8 orders in scale, ~16 in effect size |
| `debt3a_check.py` | — | recomputes Debt 3a's mean-field shortfall (ratios ~4e-28, ~3e-31) and the classicality bound; HANDOFF §2 marks the 10²⁸–10³¹ figure ✓, but no `verify/` script gates it |
