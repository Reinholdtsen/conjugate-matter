---
title: "Review round 4"
weight: 70
status: record
description: "The blind review of the toy-model note on 2026-10-19/20: the forecast and its score; the referee's citation audit, re-derivations and Monte Carlo; findings F1–F6 and the other rulings; the six revisions applied in v2, where v2 departs from them, and the two lessons."
sources:
  - "review/round4-adjudication.md"
  - "review/round4-preregistration.md"
  - "review/round4/referee/audit-notes.md Step 1–Step 4"
  - "review/round4/adjudicator/arb.out"
  - "review/round4/adjudicator/ctrl.out"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "notes/toy-lagrangian.md 'Write-up and review (2026-10-19/20)'"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
  - "verify/toy_s4.py"
  - "verify/toy_s5.py"
  - "CLAUDE.md 'Since the handoff (2026-10-19)'"
  - "review/round3-adjudication.md 'Decisions'"
  - "HANDOFF.md §8"
  - "review/wiki-build-flags.md items 2, 10, 11, 12, 13"
---

*Review round 4 was the blind review of the toy-model note, `papers/reciprocity-toy-models.md`, which builds two explicit field theories in which Born reciprocity is a symmetry of the action and asks whether the lowest-energy state breaks it. A fresh referee that could execute code reproduced the note's algebra and most of its numerics, but found that the note's one claim of quantum symmetry breaking rested on a potential that is unbounded below once the field H is allowed to vary. It graded the note B, flawed but salvageable, and the author agreed; the pre-registered forecast had also been B, though it had placed the weakest link correctly and underestimated how serious it was. Every revision was accepted and applied in version 2 of the note on 2026-10-20, and the round added two rules to the project's method.*

**Status:** Record — untagged. The record is `review/round4-adjudication.md`, with the referee's notes, scripts and outputs in `review/round4/referee/` and the arbitration in `review/round4/adjudicator/`. The revisions were applied in commit 6606734 (toy note v2 and #11 v2.2). A round-5 review is optional, "but only before any external use" (root `CLAUDE.md`, 'Since the handoff').

## The manuscript under review

The note answers the program's first acceptance criterion: an explicit action in which [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), the phase-space map ρ: (x, p) → (p, −x), is a symmetry that the vacuum breaks, with the neutral metric η as the order parameter ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion)). The handoff called this "the item both independent reviewers named as the gate to verdict A" (`HANDOFF.md` §8 item 4), and round 3's fourth decision made it the next task, because "Every referee across three rounds converges on 'the framework does no work'" and "The toy action is the only item that can change that" ([the 'framework does no work' critique](/wiki/program/framework-does-no-work)).

The note studies two models ([toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models)):

- **Model I**, [a coset sigma model](/wiki/symmetry-breaking/toy-models/coset-model) of a phase-space metric H and a real structure K (K² = 1), with η = ωK. Its vacua break Sp(2,ℝ), the group containing ρ, and K is the order parameter.
- **Model II**, [the self-dual Grosse–Wulkenhaar model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar), a noncommutative scalar field theory with an exact position–momentum duality (the Langmann–Szabo duality).

The reviewed text was the note "as of commit d9a06ac", committed with the pre-registration. Its title then was "Spontaneous Breaking of Born Reciprocity in Two Toy Models". Two of its claims matter below. Its §6 claimed an "Ising-class breaking of rho in model I in 1+1", from a Monte Carlo simulation in 1+1 dimensions with a ρ-preserving potential added. Its abstract generalized: "in both models rho is one element of a continuous U(1), so the polarization is a Goldstone angle rather than a discrete choice" (both quoted in the referee's notes, Step 3).

## The forecast

The pre-registration (`review/round4-preregistration.md`) was committed before dispatch "with a neutral subject" ([pre-registration](/wiki/method/review/pre-registration)). It forecast:

- **Verdict B**, medium confidence. "It is not C: every number was computed by gated code with independent anchors, and the claims are narrowly scoped, with limitations stated." "It is not A: the significance is thin, and at least one argument is explicitly incomplete."
- **Weakest link:** "in 1+1, the 'spontaneous' breaking of ρ rests on an explicit, rigid background." The ρ-preserving potential needs a fixed unordered pair of axes K_ref, so "A referee can reasonably call model I's 1+1 result an ordinary Z₂ breaking of an explicitly chosen axis pair."
- **Runners-up**, in order: model II's quantum-restoration argument, whose tunnelling step "is argued, not proven"; the real-versus-complex distinction; and that "The weak form of matter locality is close to true by construction."
- **Arithmetic:** "at most one surviving numerical indictment", likeliest in "the spin-wave exponent, the 8π(m+n+1) coefficient, or the Δ sign convention, which I reversed once myself while drafting."
- **Citations:** "all 12 resolve", with [12] (José et al.) the likeliest cited for more than it says.

## What the referee did

The referee was "a blind subagent with Python and web", working under the same five steps as round 3 ([the blind-review protocol](/wiki/method/review/review-protocol)). It started on 2026-10-19 and "was interrupted once by a rate limit and resumed from its own transcript." Its notes number the steps differently from the protocol: Step 1 citations, Step 2 numbers and re-derivation in four parts (a)–(d), Step 3 the conceptual audit, Step 4 the verdict.

### Citations

The referee pulled metadata for every reference from the INSPIRE database and downloaded each paper's arXiv source to search it for the attributed statement (Step 1). All 12 references resolve. Its table flags five problems: the double-field-theory reference [8] supports a pair of sections only for d = 1; the second Duncan–Niedermaier–Seiler paper has first author A. Duncan, not N. Duncan, and an erratum; Grosse–Wulkenhaar's eq. (1) is the four-dimensional form with prefactor π², which the note adapted to two dimensions without saying so; [5] concerns the four-dimensional model; and [12]'s specific claim is unverifiable, the full text being paywalled.

It also found prior work the note did not cite:

- Langmann, Szabo and Zarembo's exact solution of a closely related complex model at a self-dual point, "Directly relevant to Sec. 4 restoration claim";
- Smolin's "Quantum reference frames and triality", an explicit cubic matrix model in which an extension of Born duality, a triality, is spontaneously broken;
- Fosco and Moreno on the complex self-dual Grosse–Wulkenhaar model, which "does not examine duality breaking";
- Marotta and Szabo's Born sigma-models, which treat Born geometry as target structure rather than as a field.

Full-text searches on INSPIRE "found no prior explicit model with" the Langmann–Szabo duality "spontaneously broken by vacua". The referee's novelty verdict: "Model I appears new as a field theory, but it is a simple coset", with vacuum manifold `PSL(2,R)`.

### Re-derivation and numbers

The referee rebuilt both models in its own code (Step 2(a)–(d)). Most of the note reproduced:

- **Model I:** ρ is symplectic with ρ² = −1; all three terms of the action are Sp(2,ℝ)-invariant and invariant under K → −K; the vacua at H = 1 form a circle K(φ); the stabilizer of a vacuum in the rotations is {±1}; the Hessian of the action's potential at the vacuum has rank 1, leaving 3 flat directions ([model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)).
- **Model II:** the matrix-base functions f_mn multiply as f_mn ∗ f_kl = δ_nk f_ml, match the Weyl symbols of |m⟩⟨n| built independently from Hermite functions, and carry the duality as D f_mn = (−1)^m f_mn for the note's stated sign; the quadratic form is diagonal with entries 8π(m + n + 1); the vacua have S_min = −2.5; and the polarization obeys Δ(β)/Δ(0) = cos β "to 6 decimals at 9 angles", with the sign convention confirmed ([the duality on the matrix base](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/matrix-base-lemma); [complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)).
- **Matter coupling (§5):** I = 0.406972 and 0.360047 in the two vacua, matching the quoted 0.4070 and 0.3600. A first attempt with a fast Fourier transform gave 23.27, which the referee traced to its own normalization and corrected with a direct discrete transform: "not a manuscript error".
- **Monte Carlo (§4):** with its own lattice code and seeds, the referee reproduced the ordered phase with the potential (⟨|m|⟩ = 0.9541, 0.9543, 0.9542 at L = 16, 32, 64, Binder cumulant 2/3), the slow decay without it, and the spin-wave formula (0.9359 against the closed form's 0.9360).

The new findings it reported are taken up one by one under [the rulings](#the-rulings).

### Conceptual audit

The audit (Step 3) asked whether "spontaneous breaking" was a fair description of model I in 1+1. With H frozen, yes: an Ising-type breaking of the residual ℤ₂, though "the potential fixes the unordered axis pair by hand, so the vacuum chooses only which of two pre-set axes is 'position'." With H dynamical, as the action is written, "not established". It found the note's model II conclusion correct, and named as "the strongest reason" for it "the exact U(1)^N x U(1)^N invariance (every condensate phase decoupled) plus the absence of a volume factor". On matter locality it found the text "Mostly hedged correctly", with three over-reaches, the last that "the section condition is imposed, not derived, in this paper."

### Verdict

"B (flawed but salvageable). Confidence ~0.75." The reason: "the algebra and numerics of Secs. 2, 3, 5 reproduce. But the paper's only claim of actual (quantum) spontaneous breaking … rests on a potential that is unbounded below in model I and on freezing H=1. In model I the vacuum also keeps an unbroken element acting on H exactly as rho. Both are repairable …, so B rather than C." The single weakest link: "Sec. 4's rho-preserving potential -mu[Tr(K K_ref)]^2." The evidence statement: the numerical and algebraic indictments all rest on executed code; "Citation and omission indictments rest on retrieved sources (INSPIRE API, arXiv e-print sources), none from memory." (Step 4).

## The rulings

The adjudication: "**Referee: B (flawed but salvageable), confidence ~0.75. I agree.**" It adds that "The algebra and numerics of §§2, 3 and 5 reproduced under the referee's own conventions and code", that the only claim of quantum symmetry breaking "rests on a potential that is unbounded below once H is dynamical", and "It is repairable." The arbitration scripts are `review/round4/adjudicator/arb.py` (F1–F5) and `ctrl.py` (the control run), with outputs `arb.out` and `ctrl.out`.

### F1 and F2: the potential runs away when H moves

To pick a definite polarization in model I, the note added a potential −μ[Tr(K K_ref)]². It keeps ρ and K → −K and favours K = ±K_ref, two vacua in place of a circle. The note had checked it only at H = 1.

The referee followed a family of constant fields along which the compatibility term stays zero: H = SᵀS and K = S⁻¹K₀S, with S(t) = [[cosh t, sinh t], [sinh t, cosh t]] (Step 2(a)). The adjudicator's script follows the same family (`arb.out`):

```text
t = 0, 1, 2, 4:   V_mu = −4, −56.6, −2983, −8.9×10⁶      (λ-term ~0 throughout)
```

The referee's closed form along the family is −4μ cosh²(2t). Constant fields cost no kinetic energy, so the potential is unbounded below: ruling F1, "**Upheld**".

It follows that (1, K_ref), the note's vacuum, is a saddle point (F2, "**Upheld**"). The Hessian of the full potential at (1, K₀) has a negative eigenvalue at every compatibility coupling tried: −6.47, −4.40 and −4.04 at λ = 1, 10 and 100 "in my coordinates" (the adjudicator's, which are those of `verify/toy_coset.py`); the referee, in its own coordinates and normalization, found −3.3723, −2.7797 and −2.6785. The note's two vacua K = ±K_ref exist only if H is held at 1. The Monte Carlo had therefore simulated a frozen-H reduction of model I, not model I ([the frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction)).

The repair came from the referee. Dividing by 2 Tr KᵀK, a measure of the size of K, bounds the potential:

```text
V_b = −μ[Tr(K K_ref)]² / (2 Tr KᵀK)
```

The referee sampled it at 141227 points of the hyperboloid and found it between −0.99999913 and −1.26e-05 (in units of μ), and ρ-invariant. With H dynamical, the adjudicator's Hessian at (1, K₀) has eigenvalues [0, 0.764, 2, 5.236], and along the runaway family V_b now rises from −1 to −0.5. The ruling: "**This is the repair.** I should have caught F1 myself: I checked the potential only at frozen H." ([obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), listed in [the graveyard](/wiki/status/graveyard); [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)).

**The zero mode: a conflict between the sources.** The adjudication's F2 ruling calls the zero eigenvalue "the residual diagonal squeeze, which is an exact symmetry". Version 2 of the note says "It is not symmetry-protected, because V_b breaks the squeeze away from K = ±K_ref" (§4). Version 2 ranks higher, and the wiki follows it; a symbolic check made during the wiki build found V_b not squeeze-invariant off K = ±K_ref (flag 12 in `review/wiki-build-flags.md`).

**Two families called "boost".** The runaway family above uses the hyperbolic matrices [[cosh t, sinh t], [sinh t, cosh t]]. The referee's notes also call the diagonal squeezes diag(a, 1/a), which leave K_ref fixed, a "non-compact boost subgroup" (Step 2(c), capitals lowered). Version 2 calls the first family boosts and the second the squeeze; the double usage in the referee's notes is flag 10 in `review/wiki-build-flags.md`.

### F3: the twisted ρ

The action of model I is invariant under Sp(2,ℝ) and, separately, under the flip K → −K. The referee showed that the combination ρ∘(K → −K) leaves the vacuum (1, K₀) unchanged; the adjudicator's script confirms it ("fixed: True"). Without matter, saying that ρ is broken or that K → −K is broken is then "a labelling choice", in the referee's words. The ruling, "**Upheld**": "Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K. This sharpens the S5 conclusion rather than contradicting it." ([the twisted element ρ∘(K → −K)](/wiki/symmetry-breaking/twisted-element); [P4](/wiki/program/postulates/p4-polarized-matter)).

Version 2 states the caveat in its abstract and §2. Its §5 then says "**I is odd in K**, so it breaks the K → −K symmetry". Flag 2 in `review/wiki-build-flags.md` notes that I ≥ 0, so the two values show only that I is not invariant under K → −K; the requirement as the adjudication words it is unaffected.

### F4: the real model's one-loop preference

The note distinguishes complex fields, for which the Langmann–Szabo duality is a symmetry of model II, from real fields, for which it is only a covariance ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)). The referee looked at the real model, the one the duality literature studies. Its vacua are diagonal, diag(±a₀, ±a₁), and the duality maps diag(a₀, a₁) to diag(a₀, −a₁). The two have equal classical action (−2.5) but different fluctuation spectra, so their one-loop free energies differ. The polarization in the real model is therefore a discrete choice lifted at one loop, not a Goldstone angle, and the abstract's generalization is true "of the two models chosen, not of the GW model the duality literature is about" (Step 3; GW is Grosse–Wulkenhaar).

The ruling, "**Upheld, with a consequence the referee did not draw**". At N = 8 the lowest Hessian eigenvalues are [2, 4, 4, 4] for diag(a₀, +a₁) and [1.07, 1.07, 2, 4] for diag(a₀, −a₁) ("the referee's normalization is half of mine"), and "F(+) − F(−) = 2.634, exactly the referee's number." The consequence: "**The lower free energy belongs to diag(a₀, −a₁), the β = π vacuum, which is the one sharper in position** (Δ(π) = −Δ(0) < 0)." The selection is "explicit, not spontaneous: the real model is not duality-symmetric, because the field is real in x", and "It is recorded as a lead, not a result: truncation dependence and its interpretation are unchecked."

Version 2 reports the same 2.634 "at truncations N = 6, 8, 10, because the sign-dependent term involves only the modes coupling levels 0 and 1" (§3), and the gate prints 2.634 at all three (`verify/toy_gw.py`). The large-N, renormalized fate is still listed as not shown ([Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)).

### F5: the matter coupling needs H

The note's matter coupling is a functional of a state's Wigner function, I[W] = ∫_{L+} du (∫_{L−} dv W)², integrated along the two eigenlines L± of K. The referee found that I is not defined by K alone: rescaling the coordinate along L+ by 2 changes it, at fixed K, from 0.406972 to 0.813649 (Step 2(d)). The adjudicator's ruling, "**Upheld**", quotes "0.407 → 0.814", and the gate prints "0.4070 -> 0.8139" (`verify/toy_s5.py`). A scale along L+ has to come from H, so the coupling is covariant under the SO(2) that fixes H = 1, which contains ρ, and not under all of Sp(2,ℝ): "(H, K)-covariant", not "K-covariant" ([locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)).

### F6: the truncation argument

For complex model II the note had argued that the classical breaking does not survive quantization, and that "Increasing the truncation adds only massive levels." The referee (Step 2(c)): that sentence "omits mass renormalisation". At one loop the level-0 tadpole grows with the truncation N, so "At fixed bare mu^2 the low-level condensate is destroyed at large N; mu^2 must be renormalised with N." It "Does not change the no-SSB conclusion", the conclusion that there is no spontaneous symmetry breaking. The ruling, "**Accepted, not re-checked**": "2D φ⁴ needs mass renormalization. The no-breaking conclusion is unaffected; the argument must be restated." The referee also found the restoration "stronger than stated": the action is invariant under independent diagonal unitaries, so every condensate phase is an exact flat direction at any truncation ([quantum restoration in the complex model](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).

The sources disagree on the coefficient of the growth, and none reconciles them (flag 11 in `review/wiki-build-flags.md`):

- **2 ln N**: the referee, from the sum 2 Σ_k (G_0k + G_k0), with "T_0(N) - 2 ln N -> -0.8455 (N=10^5)"; and the adjudication, whose revision 4 asks for "the 2 ln N mass renormalization".
- **ln N**: version 2, "The level-0 tadpole grows as ln N (it is a harmonic sum)" (§4); the toy worklog ("the ln N tadpole"); and the gate, which checks a single harmonic series, "sum_{k<N} 1/(k+1) - ln N -> Euler's gamma" (`verify/toy_gw.py`).

Both agree that the growth is logarithmic and that the conclusion stands ([the coefficient: ln N or 2 ln N](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration#the-coefficient-ln-n-or-2-ln-n)).

### The Monte Carlo control and start conditions

The note's Monte Carlo of the frozen-H reduction included a control at high temperature, T = 3, where the system should be disordered and ⟨|m|⟩ should fall as 1/L. The note quoted 0.078, 0.033, 0.014 at L = 16, 32, 64. The referee found 0.0630 ± 0.0004, 0.0318 ± 0.0004, 0.0156 ± 0.0002, a clean 1/L; the quoted sequence scales as L^−1.239 instead (Step 2(c)).

The adjudicator re-ran the control (`ctrl.out`). The quoted L = 16 value came from one seed:

```text
L = 16, T = 3, seed 116:  ⟨|m|⟩ = 0.0777
seeds 1, 2, 3:            0.0687, 0.0639, 0.0626
long runs:               0.0653 (L = 16, 40000 sweeps), 0.0325 (L = 32), 0.0164 (L = 64)
```

The ruling, "**Upheld**": "my L = 16 value from seed 116 was a short-run fluctuation. … **Fixed seeds gave reproducibility, not accuracy; the numbers lacked error bars.**" The ordered-phase value (0.954) and the decay without the potential agreed with the referee "to about 1%".

The referee also found that hot starts (random initial angles) at L = 64 did not equilibrate in 6000 sweeps, giving ⟨|m|⟩ = 0.0593 in metastable domains of higher energy. It noted that the manuscript did not state its start condition, and that "results from a cold start alone would be partly by construction." Ruled "**Accepted**": "Cold starts are standard for ordered-phase measurements, but they must be stated."

Version 2 states the method: "Checkerboard Metropolis, cold start (φ = 0), L = 16, 32, 64. Means ± standard errors over four independent seeds." Its control row reads 0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004, as the gate prints (`verify/toy_s4.py`). Its ordered-phase row gives "0.954 ± 0.0001 at every size", where the gate prints ± 0.0000 at L = 64 (flag 13 in `review/wiki-build-flags.md`). See [Monte Carlo: an ordered ℤ₂ phase](/wiki/symmetry-breaking/toy-models/coset-model/monte-carlo).

### Scope: the section pair and Mermin–Wagner

- **The double-field-theory "pair"** ("**Upheld**"). The note said every derivation of the section condition "selects the pair" of null lines. That holds only for d = 1: "For d > 1, Betz–Blumenhagen–Lüst–Rennecke's M ∈ O(d) gives a continuous family of sections." ([the section condition](/wiki/symmetry-breaking/section-condition)).
- **Mermin–Wagner** ("**Upheld (literature)**"). The note invoked the theorem that continuous compact symmetries cannot break in two dimensions ([Mermin–Wagner–Coleman](/wiki/symmetry-breaking/mermin-wagner-coleman)). But model I's H-sector "is a hyperbolic SO(1,2) model, which by Duncan–Niedermaier–Seiler can break in 2D". The statement "must be restricted to the compact SO(2) containing ρ", and "Whether that SO(2) is broken in the coupled model is open." ([coset and hyperbolic sigma models](/wiki/symmetry-breaking/toy-models/coset-model/sigma-models); [Open: does ρ's SO(2) break in the coupled model?](/wiki/symmetry-breaking/toy-models/coset-model/so2-question)).

### Citations and prior work

The citation fixes were "**Accepted**". The omitted prior work was "**Accepted, as citations and reframing**": the Langmann–Szabo–Zarembo exact solution, Smolin's triality paper, Marotta–Szabo, Fosco–Moreno, Grosse–Wulkenhaar's statement that the duality is "manifest" in the matrix base, and Royer's parity-operator form of Weyl symbols. On Smolin: "Smolin breaks a triality *down to* Born duality, leaving it unbroken, so it does not contradict 'no model breaks ρ itself'. It still has to be cited."

## The forecast scored

The adjudication scores the pre-registration ([pre-registration](/wiki/method/review/pre-registration#round-4)):

- verdict B against B: "**Hit**";
- weakest link: "Same place, worse defect: the potential is unbounded below with H dynamical", "**Partial**: right location, missed severity";
- runners-up: "Partial on all three";
- arithmetic: "One: the MC control values, a statistical problem. Every normalization and sign I listed was confirmed", "**Hit on count, miss on location**" (MC is Monte Carlo);
- citations: "**Hit**", with [12]'s claim unverifiable and two further issues, in [8] and [11].

Across the rounds: "Verdicts: 2/2 (rounds 1–2), miss (round 3), hit (round 4)." "Weakest-link location has improved. Severity is still underestimated."

## The lessons

Both went into root `CLAUDE.md` ('Method'):

1. "When numerics run on a reduced model (some fields frozen), check the stability of the unreduced model — boundedness, and the Hessian with all fields dynamical — and state the reduction in the text." ([the reduced-model stability rule](/wiki/method/verification/reduced-model-stability))
2. "Monte Carlo numbers need error bars from independent runs. A fixed seed makes a number reproducible, not accurate." ([the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars))

Both were defects in the author's own checks: the potential had been checked only on the reduced model, and the control values were reproducible but not accurate ([the measured failure mode](/wiki/method/review/referee-failure-mode)).

## The revisions and version 2

The adjudication lists six revisions, "all accepted; applied 2026-10-20 in commit 6606734":

1. **§4, model I:** use the bounded potential and show it stable with H dynamical; present the Monte Carlo "as the frozen-H reduction, explicitly"; restrict Mermin–Wagner to the compact SO(2) and cite Duncan–Niedermaier–Seiler for the hyperbolic H-sector; say "ordered Z₂ phase", not "Ising class"; give start conditions, equilibration checks and error bars from independent seeds, and rerun the control.
2. **§2/§6:** state the twisted ρ. "Breaking ρ is physical only with a K-odd coupling."
3. **§3:** present the matrix-base duality as a lemma, crediting Grosse–Wulkenhaar, Royer and Langmann–Szabo; restrict "Goldstone angle" to the complex model; add F4 as a lead.
4. **§4, model II:** restate the restoration argument, add the mass renormalization, and compare with Langmann–Szabo–Zarembo.
5. **§5:** restrict the section "pair" to d = 1, and call I_K (H, K)-covariant.
6. **References:** apply the fixes and add the five new references. "Every new citation is to be retrieved, not recalled."

Version 2 departs from the list in three places:

- the zero mode, "not symmetry-protected" where the adjudication said "exact" (flag 12);
- the tadpole, ln N where the adjudication said 2 ln N (flag 11);
- the Langmann–Szabo–Zarembo comparison, of which v2 says: "The exact solution of the related model [8] is the natural independent check. We have not carried it out." (§4).

The toy worklog records the outcome and the decision on a further round: "No round 5 for now. v2 fixes and narrows claims rather than adding new ones; the real-model lead is labelled as a lead." (`notes/toy-lagrangian.md`, 'Write-up and review'). #11 v2.2 §14 item 11 records the criterion as "Met in the referees' wording by the coset model of (H, K) with a bounded ρ-preserving potential", ending "Round-4 blind review: verdict B; v2 applies the accepted revisions."

## The round's files and the gate

The record of the round is `review/round4-preregistration.md`, `review/round4-adjudication.md`, the referee's notes, scripts and outputs in `review/round4/referee/`, and the adjudicator's scripts and outputs in `review/round4/adjudicator/`. The arbitration scripts stay in `review/` and are not run by the gate. Each finding has a check in the gate's toy scripts ([the toy-model scripts](/wiki/method/verification/toy-model-scripts); [the gate](/wiki/method/verification/the-gate)):

| Finding | Check | Script |
| --- | --- | --- |
| F1, F2 | the saddle eigenvalue −6.47; V_b stable with eigenvalues 0, 0.764, 2, 5.236; −8.9e6 at boost t = 4 | `verify/toy_coset.py` |
| F3 | "round-4 F3: the twisted rho (rho composed with K -> -K) fixes (1, K_ref)" | `verify/toy_coset.py` |
| F4 | F(+) − F(−) = 2.634 at N = 6, 8, 10 | `verify/toy_gw.py` |
| F5 | I_K doubles under the rescaling | `verify/toy_s5.py` |
| F6 | the harmonic sum against Euler's γ | `verify/toy_gw.py` |
| control | 0.0653 ± 0.0043, 0.0338 ± 0.0013, 0.0155 ± 0.0004 | `verify/toy_s4.py` |

## What remains open

- **The open ends of the toy work**, listed in root `CLAUDE.md`: a Monte Carlo with H dynamical; a derivation of the ρ-preserving potential; the strong form of matter locality; and "the real Grosse–Wulkenhaar model's one-loop preference for the position-sharp vacuum, a lead." ([Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential); [strong locality](/wiki/symmetry-breaking/strong-locality); [open problems and the queue](/wiki/status/open-problems)).
- **Whether ρ's SO(2) breaks** in the coupled model, raised by the Mermin–Wagner ruling.
- **The Langmann–Szabo–Zarembo comparison**, asked for by revision 4 and not carried out.
- **A round-5 review**, optional, "but only before any external use" (root `CLAUDE.md`).

## Sources

- `review/round4-adjudication.md` — the verdict, rulings F1–F6 and the rest, the scoring, the lessons and the revisions
- `review/round4-preregistration.md` — the forecast and the neutral commit subject
- `review/round4/referee/audit-notes.md` Step 1–Step 4 — the citation audit, omitted prior work, confirmations, findings, conceptual audit and verdict
- `review/round4/adjudicator/arb.out`, `review/round4/adjudicator/ctrl.out` — the arbitration numbers
- `papers/reciprocity-toy-models.md` Abstract, §3, §4, §5, §6 — version 2: the zero mode, the ln N tadpole, the F4 truncations, the Monte Carlo method and values, the uncompleted comparison, "odd in K"
- `papers/broken-born-checkpoint-v2.md` §14 item 11 — the criterion met in the referees' wording; the round's outcome
- `notes/toy-lagrangian.md` 'Write-up and review (2026-10-19/20)' — the revisions as applied; no round 5 for now
- `verify/toy_coset.py`, `verify/toy_gw.py`, `verify/toy_s4.py`, `verify/toy_s5.py` — the gated checks of the findings
- `CLAUDE.md` 'Since the handoff (2026-10-19)', 'Method (HANDOFF §5)' — the open ends, round 5 optional, the two lessons
- `review/round3-adjudication.md` 'Decisions' (4) — why the toy Lagrangian came next
- `HANDOFF.md` §8 item 4 — the toy Lagrangian as the gate to verdict A
- `review/wiki-build-flags.md` items 2, 10, 11, 12, 13 — suspected source errors bearing on this round
