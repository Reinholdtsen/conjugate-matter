---
title: "The toy-model scripts"
weight: 90
status: method
description: "toy_coset, toy_gw, toy_s4 and toy_s5: what each checks for the toy-model note, their anchors and tolerances, and the vacuous checks caught before commit."
provenance: [D, V]
sources:
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "verify/toy_s4.py"
  - "verify/toy_s5.py"
  - "notes/toy-lagrangian.md 'Write-up and review (2026-10-19/20)'"
  - "notes/toy-lagrangian.md 'Chunk 2 results (2026-10-19): the Grosse–Wulkenhaar route'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "papers/reciprocity-toy-models.md §2–§6"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "review/round4-adjudication.md 'Rulings'"
---

*The toy-model scripts are four programs in `verify/` that recompute the results of the toy-model note, which studies two explicit field theories in which the exchange of position and momentum is an exact symmetry that the vacuum breaks. `toy_coset.py` checks the coset sigma model, `toy_gw.py` the self-dual Grosse–Wulkenhaar model, `toy_s4.py` runs the lattice Monte Carlo, and `toy_s5.py` checks the criterion that matter interactions become local in position. They were written with the models on 2026-10-19, extended with the round-4 review's corrections, and run in the gate. Their checks are symbolic identities, numerical tests against anchors taken from the cited literature, and seeded simulations with error bars.*

**Status:** Method — #11 tags the toy results these scripts gate [D][V] (§4, P2′ refinement; §10, toy-model support) — run in [the gate](/wiki/method/verification/the-gate); the last recorded run passed every check in all four.

## Key facts

- **`verify/toy_coset.py`, model I** ([Model I: the coset sigma model](/wiki/symmetry-breaking/toy-models/coset-model)). A classical check of criteria S1–S3 and of the potential. Its action: `L = (f_H^2/8) Tr(H^-1 dH H^-1 dH) + (f_K^2/4) Tr(H^-1 dK^T H dK) + V`. Among its checks: `all three terms invariant under rho`; `no vacuum is rho-invariant: at H = 1 a compatible K with rho^-1 K rho = K must vanish`; `O = K_11 takes +1 in (1, K0) and -1 in its rho-image (1, -K0)`; the saddle of the naive potential and the stable minimum of the bounded one with H dynamical; and `round-4 F3: the twisted rho (rho composed with K -> -K) fixes (1, K_ref)`. It ends "OK — the coset baseline meets S1-S3 classically." See [action and symmetries](/wiki/symmetry-breaking/toy-models/coset-model/action-and-symmetries), [vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua), [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential) and [the twisted element](/wiki/symmetry-breaking/twisted-element).
- **`verify/toy_gw.py`, model II** ([Model II: the self-dual Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)). "Inputs taken from the sources, not from memory." It checks the matrix base against the literature, then the duality lemma, `D f_mn = (-1)^m f_mn for all m, n < 4: the duality is left multiplication by parity  [max dev 1.4e-12]`; the complex field's symmetry against the real field's covariance; the complex vacua and their polarization `[Delta(0) = 10.8828]`; the real model's one-loop split, `F(+) - F(-) = 2.634 at N = 8 (matching the round-4 referee)`; and the logarithmic tadpole of round-4 finding F6. It ends "OK — Grosse-Wulkenhaar route checks pass." See [the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma), [complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields), [complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua) and [Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead).
- **`verify/toy_s4.py`, criterion S4.** A Metropolis simulation of the lattice energy E = −J Σ cos(φ_i − φ_j) − h Σ cos 2φ_i. The docstring: `This is the FROZEN-H reduction of the coset toy (H = 1 held fixed)`, and "All runs use a cold start (phi = 0). Error bars: standard error over 4 independent seeds." It ends "OK — S4: rho is spontaneously broken in 1+1 (frozen-H reduction) only with the rho-preserving potential." See [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo), [The reduced-model stability rule](/wiki/method/verification/reduced-model-stability) and [The Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars).
- **`verify/toy_s5.py`, criterion S5.** Part A, what the vacuum's η fixes (its null lines); part B, the section condition built from η, which "cannot tell L+ from L-"; part C, an interaction built from K, local in x in one vacuum and in p in the other: `the two vacua give different physics for the same state  [0.4070 vs 0.3600]`, and `I_K is not K-covariant alone: rescaling the L+ coordinate by 2 doubles it (it needs H)  [0.4070 -> 0.8139]`. It ends "OK — S5 (weak form) and the section-condition structure check out." See [the section condition](/wiki/symmetry-breaking/section-condition), [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling) and [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality).
- **Lessons from writing them.** "Two checks were vacuous on the first draft (an always-true term; a condition multiplied by 0) and were replaced by real tests before commit." (worklog, chunk 4). "Two drafting errors were caught by gated checks along the way: a hard-coded `True`, and citation regexes matching matrix entries." (worklog, 'Write-up and review'). When a check on the model II kinetic form failed, the fix was not a looser tolerance: "A first check used finite-difference derivatives and failed at the 0.3% level. The fix was exact derivatives, not a looser tolerance." (worklog, chunk 2).
- **Tolerances against quoted precision.** Some assertions are looser than the precision the note quotes: the note gives the duality lemma "to ≲ 10⁻¹¹" (§3), while the script asserts a deviation below 1e-7 and prints 1.4e-12; the split 2.634 is asserted at N = 8, while its sign is asserted at N = 6, 8 and 10 and the run prints 2.634 at each.
- **Wording lags.** The `toy_s4.py` docstring still calls the naive potential "The tau-type potential"; it notes that the energy it simulates "equals the bounded V_b at H = 1 up to a constant and a factor".
- **Not checked by any script.** The note lists as not shown "a Monte Carlo of model I with H dynamical", "a derivation of the ρ-preserving potential" and "anything beyond d = 1", among others (§6). The note's argument that the complex model's breaking does not survive quantization is analytic (§4): the gate checks its premise, `complex model: S[U phi V^dag] = S[phi] for any diagonal unitaries U, V (a continuous U(1)^N x U(1)^N)`, not its conclusion. See [Acceptance criterion 1: the toy Lagrangian](/wiki/symmetry-breaking/toy-models/acceptance-criterion) and [Quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration).

## Sources

- `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py`, `verify/toy_s5.py` — docstrings, checks and final lines
- `notes/toy-lagrangian.md` 'Chunk 2 results', 'Chunk 4 (in progress, 2026-10-19): S5', 'Write-up and review (2026-10-19/20)' — the tolerance fix, the vacuous checks, the drafting errors
- `papers/reciprocity-toy-models.md` §2–§6 — the results the scripts check, and what is not shown
- `papers/broken-born-checkpoint-v2.md` §4, §10 — the [D][V] tags on the toy results
- `review/round4-adjudication.md` 'Rulings' — the round-4 findings that the scripts now carry
