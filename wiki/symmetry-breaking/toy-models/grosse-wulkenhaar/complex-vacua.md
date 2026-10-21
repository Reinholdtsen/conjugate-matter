---
title: "Complex-model vacua and the polarization Δ(β)"
weight: 50
status: alive
description: "Two oscillator levels condense with a free relative phase β that the duality shifts by π; the vacuum's position-versus-momentum spread varies as Δ(0) cos β, with Δ(0) > 0 (a sign first written reversed). Classical only."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §1"
  - "verify/toy_gw.py S2"
  - "verify/toy_gw.py 'S3/S5 start'"
  - "review/round4-adjudication.md 'Revisions' 3"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(b)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_model2_vac.txt"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "notes/toy-lagrangian.md chunk 2 as first committed (4923112)"
---

*The vacua of the complex [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) are its configurations of lowest action. At the parameters the toy-model note uses, μ² = 4 and λ = 1, the two lowest oscillator levels condense: the diagonal matrix entries φ₀₀ and φ₁₁ take fixed nonzero magnitudes, and their relative phase β is free, so the vacua form a circle. The duality shifts β by π, half-way round the circle, so it maps every vacuum to a different one and leaves none unchanged: classically, the vacuum breaks the exchange of position and momentum. The polarization Δ(β) measures how much broader the vacuum's profile is in position than in momentum. It varies as cos β, so the β = 0 vacuum is broad in position and narrow in momentum and the β = π vacuum is the reverse, as a narrow pulse has a broad spectrum and a broad pulse a narrow one. The sign was written reversed in the first draft and corrected the same day. The breaking is classical only: quantization restores the symmetry.*

**Status:** Alive, classical only — [V]: criteria S2 and S3 for this route, the vacua, the flat angle and the polarization, are gated in `verify/toy_gw.py` ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)); the referee of [review round 4](/wiki/method/review/round-4) reproduced them, including the sign of Δ(0), with an independent Fourier quadrature. The breaking does not survive quantization ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).

## The vacua

A vacuum is a configuration of least action: the classical ground state, about which the quantum theory is then built ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking)). For the complex field the action is ([the matrix base and the action](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/model-and-matrix-base))

```text
S[φ] = Σ_mn (m + n + 1 − μ²) |φ_mn|² + λ Tr((φ†φ)²)
```

with † the Hermitian adjoint, not the citation mark.

**They are diagonal.** The note: "Gradient descent from random starts always reaches a diagonal φ with |φ_mm|² = (1.5, 0.5, 0, …) and S_min = −2.5." (§3). For the real model the worklog gave the reason in chunk 1: the action depends on φ only through φ², and "With distinct level energies, every minimum is then diagonal". For the complex model the evidence is numerical.

**What a diagonal vacuum looks like.** For a diagonal φ with entries of magnitude q_m = |φ_mm|², the action separates into one term per level, Σ_m [(2m + 1 − μ²) q_m + λ q_m²]: a diagonal entry has n = m, so its quadratic coefficient m + n + 1 − μ² is 2m + 1 − μ², and Tr((φ†φ)²) = Σ_m q_m². Each term is a parabola in q_m. A level whose coefficient 2m + 1 − μ² is positive stays empty; a level whose coefficient is negative fills to the bottom of its parabola. That is the formula the gate checks:

```text
q_m = max(0, −(2m + 1 − μ²)/(2λ))            S_min = −Σ (2m + 1 − μ²)²/(4λ)   over the filled levels
```

At μ² = 4 and λ = 1 the gate prints "q = [1.5 0.5 0. ]" and "-2.5", in the section titled "mu2 = 4: levels 0 and 1 condense" (`verify/toy_gw.py`, S2). The worklog's form: "Every minimum found by descent from random starts is diagonal, with |φ_mm|² = q_m = max(0, −(2m+1−μ²)/(2λ))" and "S_min matches its exact value" ('Chunk 2 results').

On the plane, the vacuum is the profile φ(x) = φ₀₀ f₀₀(x) + φ₁₁ f₁₁(x). The diagonal functions are rotationally symmetric, so the vacuum is a round lump centred on the origin. It occupies two oscillator levels and decays away from the origin; it is not an order spread through space, which matters for its quantum fate ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration#step-2-no-volume-factor)).

**The checks [V].** The gate descends from six random starts at N = 8 and passes "every minimum found is diagonal", "with |phi_mm|^2 = q_m = max(0, -(2m+1-mu2)/(2 lam))" and "and S_min = -sum (2m+1-mu2)^2/(4 lam)". The round-4 referee ran its own descent: "6 random starts, N=8: all S_min = -2.5000000000, |offdiag| <= 7.7e-08, |phi_mm|^2 = [1.5 0.5 0 0]", and "200 extra restarts: lowest S = -2.49999999985 (no lower minimum)" (audit notes, Step 2(b)).

## The flat angle β

The magnitudes of φ₀₀ and φ₁₁ are fixed; their phases are not. Every diagonal unitary rephasing of rows and columns leaves the action unchanged ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)), so each condensed entry can take any phase at no cost. An overall phase does not change the shape of the profile, |φ(x)|², so for the questions asked here the vacua are labelled by the relative phase β of the two entries:

```text
φ_vac(β) = diag( √q₀, √q₁ e^{iβ}, 0, … )        S[φ_vac(β)] = S_min for every β
```

"The relative phase β of φ₀₀ and φ₁₁ is free." (§3). The worklog calls it "a flat direction (a Goldstone mode)" ('Chunk 2 results'; [Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs)). The descents land at scattered values: the gate prints the six phases as "betas [-1.61  1.4  -0.52  2.06 -2.28  0.64]" and passes "S is constant around the vacuum circle beta (Goldstone direction)"; the referee found "S = -2.500000000000 at 7 values of beta" (audit notes, Step 2(b)).

## The duality moves every vacuum

The duality is left multiplication by parity, Π = diag((−1)^m) ([the lemma](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma)). On the vacuum it leaves φ₀₀ alone and multiplies φ₁₁ by −1 = e^{iπ}:

```text
Π φ_vac(β) = φ_vac(β + π)
```

"The duality maps β → β + π, so no vacuum is invariant." (§3). A vacuum mapped to itself would need φ₁₁ = −φ₁₁, so invariance fails as soon as level 1 is occupied. The gate passes "the duality maps vacuum beta to vacuum beta + pi" and "no vacuum is duality-invariant once level 1 condenses (|phi_11| > 0)"; the referee found "duality maps beta -> beta+pi (all 7)". This is criterion S2 for this route, "no vacuum is ρ-invariant, and ρ maps each vacuum to another one" ([success criteria](/wiki/symmetry-breaking/toy-models/success-criteria)), with the duality in the role of ρ. Since Π is the α = π member of the continuous rotations e^{−iαN}, the duality is a half-turn of the vacuum circle, and the rest of the family turns it continuously.

## The polarization Δ(β)

An [order parameter](/wiki/symmetry-breaking/order-parameter) is a quantity that differs between the vacua and changes sign, or otherwise transforms, under the symmetry they break. For this route it is a comparison between the vacuum's profile and its image under the duality:

```text
Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual = Δ(0) cos β,        Δ(0) > 0
```

"Polarization: Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual equals Δ(0) cos β, with Δ(0) > 0. β = 0 is broader in position than in momentum; β = π is its image." (§3).

**What it measures.** ⟨x²⟩_vacuum is the second moment of the vacuum's profile on the plane, its spread in position. The dual profile is the duality's image, the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of the field read at p = x̃, so ⟨x²⟩_dual is the spread of the vacuum in momentum. Δ > 0 means the vacuum is broader in position than in momentum, and Δ < 0 the reverse. The trade-off between the two spreads is the waveform–spectrum relation: a narrow pulse has a broad spectrum. The worklog's reading: "β = 0 is broader in x than in p (Δ(0) = +10.88 > 0), β = π is its image (broader in p), β = ±π/2 is balanced." ('Chunk 2 results').

**Why a cosine.** The vacuum and its dual differ only in the sign of the level-1 component, so in the difference of their second moments the contributions of each level alone cancel, and only the interference between levels 0 and 1 is left. That term carries the factor cos β. The referee's output computes Δ(0) from this cross term alone ("grid Delta(0) from cross term", `review/round4/referee/out_model2_vac.txt`). Δ is odd under the duality, Δ(β + π) = −Δ(β), and the worklog takes it as the order parameter of criterion S3: "S3: the order parameter is the vacuum's x-versus-p polarization" (worklog, 'Chunk 2 results').

**The checks [V].** The gate's section "S3/S5 start: x-versus-p polarization of the vacuum profile" first checks that the dual profile computed by the grid Fourier transform agrees with the (−1)^m rule. It then passes "Delta(beta) = <x^2>_vacuum - <x^2>_dual is nonzero at beta = 0 and flips sign at beta = pi" with "Delta(0) = 10.8828", "Delta(beta) = Delta(0) cos(beta): the polarization is an angle on the Goldstone circle", and "Delta(0) > 0: the beta = 0 vacuum is broader in x than in p (quoted +10.88)".

The referee computed the dual "by direct 2D Fourier quadrature (not via Pi)", an independent route to the same quantity, and found "Delta/Delta(0) = cos(beta) to 6 decimals at 9 angles; Delta(0) = +0.866025 = sqrt(3)/2 > 0 (beta=0 broader in position: <x^2>_vac=1.183 vs 0.317); zero at pi/2; Delta[D phi] = -Delta[phi] (0.66237 vs -0.66237). Sign convention CONFIRMED." (audit notes, Step 2(b)).

**Two magnitudes, one sign.** The gate's Δ(0) is 10.8828 and the referee's is 0.866025. The two computations normalize ⟨x²⟩ differently: the gate's moment is the unnormalized integral of x²|φ|² over the plane (`verify/toy_gw.py`). No document reconciles the magnitudes, and the difference of normalization is the wiki's reading. The claim rests on the sign, which agrees.

## What the breaking amounts to

Classically, every vacuum of the complex model breaks the duality, and the vacuum's polarization labels which one has been chosen. The assessment of the toy work lists it as an unpredicted finding, in terms of the [Langmann–Szabo duality](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory): "The self-dual complex Grosse–Wulkenhaar vacua break the Langmann–Szabo duality classically, as a cos β polarization (new as far as the S0 search found). The breaking does not survive quantization." (worklog, 'Assessment against the predictions').

Two qualifications came from round 4. The referee called the wording weak: "'Classical breaking' of a zero-dimensional degeneracy is weak language." (audit notes, Step 3). The vacuum is a single lump, so its degeneracy is that of one collective coordinate, not of an extended order. And the breaking does not survive quantization: β costs no action and nothing pins it, so the quantum average of Δ is zero ([quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).

## Novelty and prior work

The worklog claimed priority within the limits of its prior-art survey, criterion S0 ([success criteria](/wiki/symmetry-breaking/toy-models/success-criteria)): "This is, as far as the S0 search found, the first explicit statement that the self-dual Grosse–Wulkenhaar vacua break the Langmann–Szabo duality — in the complex model, not the real one." ('Chunk 2 results'). The note's first version already cited de Goursac, Tanasa and Wallet for the non-constant vacua, and the round-4 referee confirmed that they do not examine the duality: "breaking not examined -- CONFIRMED". The referee also found a paper the first version had missed, Fosco and Moreno, on "quantum effects around non-trivial (U(1)-breaking) minima; does not examine duality breaking (grep)" (audit notes, Step 1). Its full-text searches found "no prior explicit model with [Langmann–Szabo] duality spontaneously broken by vacua" (Step 1). Version 2 credits both papers and confines the claim to what they did not do: "Non-constant vacua at Ω = 1 [9], and minima of the complex self-dual planar model [10], have been studied, but not their behaviour under the duality." (§1; [noncommutative field theory](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/noncommutative-field-theory)).

## Restricted to the complex model

The flat angle exists because the complex model's duality sits inside a continuous symmetry. The real model has no such circle: its vacua are discrete, diag(±√q₀, ±√q₁), and the duality exchanges the two relative signs, which correspond to β = 0 and β = π. Round 4's revision 3 accordingly restricts the Goldstone-angle reading: "Restrict 'Goldstone angle' to the complex model." ([the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). In the real model the two vacua split at one loop, in favour of β = π, the vacuum sharper in position, and the sign of Δ(0) on this page is what identifies it ([Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)).

## Superseded: the reversed sign of the polarization

**The first statement.** The worklog's chunk 2, as first committed (4923112), read: "β = 0 is sharp in x, β = π is sharp in p, β = ±π/2 is balanced."

**The correction.** The line now reads: "β = 0 is broader in x than in p (Δ(0) = +10.88 > 0), β = π is its image (broader in p), β = ±π/2 is balanced. *Corrected 2026-10-19: the first version of this line had the sign reversed.*" ('Chunk 2 results'). The correction was committed the same day, with the round-4 pre-registration (d9a06ac). The computed sign is the gate's: "Delta(0) > 0: the beta = 0 vacuum is broader in x than in p".

**The check.** The [pre-registration](/wiki/method/review/pre-registration) named this sign as a likely place for a surviving error: "the Δ sign convention, which I reversed once myself while drafting" (`review/round4-preregistration.md`). The referee confirmed the corrected sign by an independent Fourier quadrature ("Sign convention CONFIRMED"), and the adjudication scored the prediction: "Every normalization and sign I listed was confirmed" ('Pre-registration scored').

The sign matters downstream. The real model's one-loop preference is for the β = π vacuum, and the corrected sign makes that the vacuum sharper in position (`verify/toy_gw.py`: "diag(a0, -a1) is the beta = pi vacuum, i.e. the one sharper in x (Delta(pi) = -Delta(0) < 0)").

## Sources

- `papers/reciprocity-toy-models.md` §3, §1 — the vacua, the flat angle and the polarization, quoted above; the prior work on these vacua
- `verify/toy_gw.py` S2, 'S3/S5 start' — the gated vacuum, phase and polarization checks, including Δ(0), and the moment as computed
- `review/round4/referee/audit-notes.md` Step 1, Step 2(b), Step 3 — the prior work checked for duality breaking; the independent reproduction, the extra restarts, the referee's Δ(0) and sign confirmation; "weak language"
- `review/round4/referee/out_model2_vac.txt` — the referee's printed vacua, phases and Δ(β), including the cross-term evaluation
- `review/round4-adjudication.md` 'Revisions' 3, 'Pre-registration scored' — the restriction to the complex model; the confirmed sign
- `review/round4-preregistration.md` 'Predictions' — the sign convention as a predicted error site
- `notes/toy-lagrangian.md` 'Chunk 2 results', 'Assessment against the predictions' — the occupation formula, the corrected sign line, the novelty statement, the unpredicted finding
- `notes/toy-lagrangian.md` as first committed (4923112) — the reversed line
