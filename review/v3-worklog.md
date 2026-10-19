# v3 of #14 — worklog

Cutting v3 of [papers/knot-dark-matter-standalone.md](../papers/knot-dark-matter-standalone.md)
from the round-2 pending list (HANDOFF §6). State is saved here after each
chunk so any session can resume cold.

Evidence used so far:

- HANDOFF §6 summary of round 2. The round-2 referee report itself is not in
  the repo. Paul holds it.
- [verify/knot_numbers.py](../verify/knot_numbers.py): every number v2 quotes,
  recomputed. All reproduce (gated in `scripts/check.sh`). NOTE lines are
  adjudication inputs not yet quoted by the manuscript.
- Literature check of the cited and newly needed sources: dispatched
  2026-10-19, result pending.

## Round-2 pending list

| # | Item | Status | Evidence / decision |
|---|------|--------|---------------------|
| R1 | SUSY-exactness burden for Montonen–Olive | waiting on literature | Exact S-duality is an N=4 (and finite N=2) property; v3 must say whether reciprocity supplies the rigidity or the dual sector is approximately SUSY. |
| R2 | Coupling convention and running spread | **adjudicated** [V] | Convention: 1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn). Running: one-loop SM α_em gives 1/(4α_em) = 29.0 at 10¹¹, 28.8 at 3×10¹¹, 27.3 at 10¹⁶ GeV. The referee's "toward ~6–8" is **not reproduced** for the electromagnetic coupling; 6–8 appears only for 1/(4α₃) (7.9–8.2 at 10¹¹–3×10¹¹ GeV). The valid core stands: the number is convention-dependent by a factor of 4. v3: present α_d as free-but-strong, with the point-selecting hypothesis named as such. |
| R3 | Extended Parker bound (Adams et al. 1993) | arithmetic done [V], citation waiting | With F ≲ 10⁻¹⁶ (M/10¹⁷ GeV): excess 6.98 orders at M = 10¹⁶ (Parker: 4.98); 12.0 orders at M = 3×10¹³ (Parker: 7.5). The referee's "~7 orders" is right at the benchmark. |
| R4 | Gravity-induced kinetic mixing | waiting on literature | v2's "forbidden to all orders" is too strong either way. Candidate mechanism to check: for a non-abelian dual group, Φᵃ Fᵃ B / M is gauge invariant (dimension 5) and gives ε ~ ⟨Φ⟩/M. With ⟨Φ⟩ ~ Λ_c ≈ 3×10¹¹ GeV: ε ≈ 2.4×10⁻⁸ (M = M_Pl) to 1.2×10⁻⁷ (reduced M_Pl), against a threshold of 1.0×10⁻⁵ [V, NOTE line]. The operator's existence and genericness are [D], pending the literature. |
| R5 | Entropy-dilution caveat | **adjudicated** [V], stronger than the referee said | See finding F1. |
| R6 | Name an explicit candidate group | ready | SU(2) → U(1) by an adjoint Higgs; π₂(SU(2)/U(1)) = π₂(S²) = ℤ [T]. |
| R7 | Bimetric cosmological-branch instability | waiting on literature | Question: do the instability analyses assume a light second metric (spin-2 mass ~ H)? Is the heavy-mass regime known to be safe? Is the early universe still open? |

## New findings from the recomputation (not raised by either referee)

- **F1 — the mass window is not "Kibble-only"** [V]. Kibble with p = 1 closes
  at a single point, M* ≈ 3.0×10¹³ GeV. Below it, solitons are
  under-produced (×0.013 at 10¹³). Above it, the abundance scales as
  (M/M*)⁴, so the observed density needs entropy dilution of 1.3×10⁶ at
  10¹⁵, **1.3×10¹⁰ at the 10¹⁶ benchmark**, and 1.3×10¹⁴ at 10¹⁷.
  - v2 §3 calls 10¹³–10¹⁷ "the Kibble-only estimate". That is wrong. Only the
    lower end is Kibble-only; everything above needs dilution.
  - The horizon-counting p is ≈ 0.023 (g* = 100), which moves M* to
    ≈ 7.7×10¹³. Same conclusion.
  - v3 options: (a) move the benchmark to M ≈ 3×10¹³, where the flux excess
    over Parker grows to 7.5 orders and the spacing per soliton shrinks; or
    (b) keep 10¹⁶ and state the 10¹⁰ dilution as a requirement on the dual
    transition's history. Recommendation: (a), with (b) as a stated
    alternative.
- **F2 — which coupling sets the soliton mass** [D, numbers V]. v2 writes
  M ~ (4π/e_d²) Λ_c ~ 100 Λ_c. That factor is ~137 only if e_d²/4π ≈ 1/137.
  With e_d²/4π = α_d = 34 it is 0.029, so the solitons would not be heavy
  and the semiclassical formula would not apply. v2 uses the weak value in
  §3 and the strong value in §2 and §4.
  - The self-consistent reading: the dual sector's elementary coupling is
    weak (α_e,d), its solitons are heavy (M ≈ Λ_c/α_e,d), and the solitons
    themselves are strongly coupled (α_m ≈ 1/(4α_e,d) or 1/α_e,d, by the
    dual sector's own Dirac quantization).
  - Then α_d ≈ 34 is the solitons' coupling. It follows from α_e,d ≈ α, a
    mirror-coupling equality, with no need to act with S on our coupling.
  - This removes the contradiction between §2 and §3. It also moves the
    load-bearing conjecture from "reciprocity acts as S" to "α_e,d = α",
    or to α_e,d free.
  - New consequence to state: the dual sector's elementary charged states
    and its dark photon need a cosmological fate (stable lightest dark
    charge; dark radiation, i.e. ΔN_eff).
  - **Needs Paul's call** (it changes §2's framing).
- **F3 — self-interaction**: 3×10⁻³⁴ cm²/g corresponds to ln Λ ≈ 12. v3
  should state the Coulomb log; ln Λ = 10–30 gives 2.5–7.6×10⁻³⁴.
- **F4 — GW peak**: 10⁴–10⁷ Hz holds for f*/H* = 1. Fast transitions
  (f*/H* ~ 10–100) push it to ~10⁹ Hz. v3 should state the assumption.

## Next chunks

1. Fold in the literature report: R1, R3 citation, R4, R7, plus every v2
   reference.
2. Paul's call on F2 (framing of §2) and F1 (benchmark).
3. Draft v3. Then update `verify/knot_numbers.py` so every number v3 quotes
   is a gated check, and retire the v2 checks.
4. Pre-register the expected verdict and weakest link, then run the round-3
   audit on v3 (HANDOFF §8 item 2).
