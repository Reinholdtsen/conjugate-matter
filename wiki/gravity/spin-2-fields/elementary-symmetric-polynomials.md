---
title: "Elementary symmetric polynomials"
weight: 60
status: established
description: "eₙ of the eigenvalues of √(g⁻¹f), power sums and Newton's identities: the building blocks of the bimetric potential, its linearization coefficients C(3, n−1) (battery T6) and the span test T7."
provenance: [T, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §7.2"
  - "verify/battery.py T6"
  - "verify/battery.py T7"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/debt1a-iii-tuning-test.md §2"
---

*The elementary symmetric polynomials of a list of numbers are the sums of all products of distinct entries taken n at a time: e₁ is the sum, e₂ the sum of all pairwise products, and so on up to the product of all the entries, with e₀ = 1. Applied to the eigenvalues of the matrix √(g⁻¹f), they are the building blocks of the ghost-free bimetric potential, which is linear in them. Power sums, such as p₄, the sum of fourth powers, can be written in terms of the eₙ by Newton's identities, but only as nonlinear polynomials. The program's verification battery checks two facts of this algebra: the linear coefficients of the eₙ near the identity matrix (test T6), and that p₄ is not a linear combination of the eₙ (test T7).*

**Status:** Established — [T] for the algebra; [V] for battery tests T6 and T7, which pass in the last recorded gate run ([the verification battery](/wiki/method/verification/battery)).

## Key facts

- Definition [T]: eₙ is the sum over all products of n distinct eigenvalues, with e₀ = 1; this is the function `en` in `verify/battery.py`. For the 4 × 4 matrices of the program there are five, e₀ to e₄, one for each coefficient βₙ of the [Hassan–Rosen potential](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric).
- At the identity matrix ([#8](/wiki/history/documents/debt-1-notes) §2, part of the [D — rigorous, four lines] derivation): eₙ(1) = C(4, n), and "linearizing eₙ(1+δ) = C(4,n) + C(3,n−1)Tr δ".
- Battery T6 [V]: for one random small symmetric δ, the linear coefficients come out [0.0, 1.0, 3.0, 3.0, 1.0], matching C(3, n−1) = [0, 1, 3, 3, 1] (`verify/battery.py` T6).
- These coefficients give the tadpole of the bimetric potential at the aligned point, T = β₁ + 3β₂ + 3β₃ + β₄ (#8 §2), the input to [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity).
- Power sums [T]: pₖ is the sum of the k-th powers of the eigenvalues, and Newton's identities express it through e₁ to eₖ, nonlinearly. #7 §2: "Tr(g²) = p₄ of the square-root eigenvalues is a *nonlinear* polynomial in the eₙ, hence outside the family."
- Battery T7 [V]: a least-squares fit of p₄ against e₀ to e₄, over 300 random samples with eigenvalues drawn between 0.5 and 2.0, leaves an rms residual of 3.2853 (`verify/battery.py` T7), which the [checkpoint](/wiki/history/documents/checkpoint) quotes as 3.29 (#11 §2). See [the metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures).
- What T7 does not show: #11 §7.2 says the metric-tier structure Tr(g²) + Tr(g⁻²) is "provably outside the linear-in-eₙ span (T7)", but T7 tests p₄ alone, numerically. The [V] covers p₄; the statement about Tr(g²) + Tr(g⁻²) rests on the derivation [D].

## Used by

- [The vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity) — eₙ(1) = C(4, n) and the tadpole coefficients.
- [The metric tier fails twice](/wiki/gravity/tuning-test/metric-tier-failures) — battery T7, the span test.

## Sources

- `papers/broken-born-checkpoint-v2.md` §2, §7.2 — the battery's Tier-1 list ("rms residual 3.29"); the claim that the metric-tier structure lies outside the span.
- `verify/battery.py` T6, T7 — the definition of eₙ used, the printed coefficients and the printed residual.
- `notes/debt1a-iv-beta-coefficients.md` §2 — eₙ(1) = C(4, n), the linearization and the tadpole.
- `notes/debt1a-iii-tuning-test.md` §2 — p₄ as a nonlinear polynomial in the eₙ.
