---
title: "Row 9: no linear photon dispersion"
weight: 100
status: alive
description: "The linear Planck-scale term is exactly zero (ρ²-protected in the lab notebook's argument) and the quadratic one suppressed; Fermi Large Area Telescope bounds from gamma-ray bursts, and #13's joint-cone reading of them."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 9"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §9"
  - "papers/conjugate-special-relativity.md §6"
  - "review/v3-worklog.md 'New open items' O3"
  - "papers/reciprocity-toy-models.md §2"
  - "verify/toy_coset.py anchors"
---

*Row 9 predicts that the speed of light in vacuum has no correction proportional to a photon's energy. Some approaches to quantum gravity predict such a linear correction, suppressed only by the Planck scale; it would make high-energy photons from a distant gamma-ray burst arrive measurably earlier or later than low-energy photons emitted with them, and burst observations with the Fermi Large Area Telescope exclude it [T]. In the program the linear term is exactly zero, protected by the residual symmetry ρ², the half-turn (x, p) → (−x, −p) of [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), and the leading allowed correction is quadratic and strongly suppressed. The protection argument exists only in the lab notebook, which made it before the polarization became a Goldstone angle, and no later document restates it.*

**Status:** Alive — the protection argument [D, schematic] and the observational bound [T] both come from the lab notebook (#1 §4), and #11's row cites the ρ² protection without restating the argument — not machine-checked; no source gives a reference for the bound.

## Key facts

- **The row** ([checkpoint #11](/wiki/history/documents/checkpoint) §13). Observable: "Photon dispersion". Standard expectation: none in general relativity (GR), and a linear term in some quantum-gravity models. Requirement: "Linear exactly zero (ρ²-protected); quadratic suppressed". Killed by: "Confirmed linear-in-E dispersion".
- **The argument** ([the lab notebook](/wiki/history/documents/lab-notebook), #1 §4, [D, schematic]): "Corrections to x-sector dispersion require insertions of the symmetry-breaking spurion ⟨J⟩. Under the residual ρ² (a phase-space parity), operators linear in energy are odd and forbidden; the leading allowed corrections are quadratic", of the form below, "and gravitationally suppressed".

```text
E² = p² + m² + ξ p⁴/M_B²
```

- **The bound** (#1 §4, [T], no reference given): bounds from gamma-ray bursts observed by the Fermi Large Area Telescope "exclude linear Planck-scale dispersion; quadratic effects at M_B ~ M_P sit ~10 orders below current sensitivity. Consistent." The "~10 orders" figure is unverified.
- **Where ρ² comes from.** In #1 §2 [D], "ρ²: (x,p) → (−x,−p) preserves *all three* structures. The breaking pattern is ℤ₄ → ℤ₂", the unbroken group being ℤ₂ = {1, ρ²} ([the order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter)). That pattern was derived under the [original P2](/wiki/program/postulates/original-p2), in which ω and η are both rigid. Since v2.2, with only ω rigid ([P2′](/wiki/program/postulates/p2-prime)), "ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (#11 §4; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle), checked by [the toy-model scripts](/wiki/method/verification/toy-model-scripts)). The Goldstone picture governs, and the row's rationale exists only in #1; no current document restates it in that picture. The toy-model note's coset model has "The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}" (`papers/reciprocity-toy-models.md` §2), and ρ² = −1 is one of the anchors of `verify/toy_coset.py`; no document applies either statement to row 9.
- **#13's joint reading.** [Conjugate special relativity](/wiki/conjugate-relativity) (#13 §6) adds that since "our massless dispersion E = c|p| *is* the dual null cone", the same photon-dispersion bounds "constrain both cones at once" [T] ([two causal cones](/wiki/conjugate-relativity/two-causal-cones)).
- **That reading is unsettled.** The v3 worklog (item O3) notes that #13 §1 uses a dual cone in (t, p) with slope c̃, while §6's statement "belongs to the 4D Born map (t ↔ E): a cone in (E, p) with slope c", and asks to "fix #13's two cones and settle which construction governs" ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).
- **Wording across versions.** v0.1: "Linear term exactly zero (protected by ρ²); quadratic allowed, gravitationally suppressed", killed by "Any confirmed linear-in-E dispersion" (#1 §9). v1: "Linear term exactly zero (protected by ρ²); quadratic allowed, suppressed", killed by "Confirmed linear-in-E dispersion" (#9 §9). See [the history of the table](/wiki/predictions/table-history).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 9 — the row; §4 for P2′'s Goldstone-angle refinement [D][V]
- `notes/broken-born-theory.md` §4 — the protection argument [D, schematic] and the bound [T]; §2 for the breaking pattern ℤ₄ → ℤ₂ [D]; §9 for v0.1's row 9
- `notes/broken-born-program-v1.md` §9 — v1's row 9
- `papers/conjugate-special-relativity.md` §6 — the joint test of both cones
- `review/v3-worklog.md` 'New open items', item O3 — the two dual cones, unsettled
- `papers/reciprocity-toy-models.md` §2 and `verify/toy_coset.py` — the coset model's stabilizer {±1} and the check ρ² = −1
