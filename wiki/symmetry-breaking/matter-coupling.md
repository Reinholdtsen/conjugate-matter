---
title: "Locality from an (H, K)-built coupling"
weight: 100
status: alive
description: "The coupling I_K is local in x in one vacuum and local in p in the other, dependent on the sign of K and (H, K)-covariant; locality then follows from the vacuum as fermion masses follow from a Higgs vacuum value — the weak form of criterion S5."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §5"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §6"
  - "verify/toy_s5.py part C"
  - "review/round4-adjudication.md 'Rulings' F3"
  - "review/round4-adjudication.md 'Rulings' F5"
  - "review/round4-adjudication.md 'Revisions' 5"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 2(d)"
  - "review/round4/referee/out_sec5.txt"
  - "review/round4/referee/out_sec5_fix.txt"
  - "review/round4/adjudicator/arb.py F5"
  - "review/round4/adjudicator/arb.out F5"
  - "notes/toy-lagrangian.md 'Success criteria (fixed 2026-10-19, before any construction)'"
  - "notes/toy-lagrangian.md 'Predictions (written before construction)'"
  - "notes/toy-lagrangian.md 'Chunk 4 (in progress, 2026-10-19): S5'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions (written before construction)'"
  - "verify/toy_coset.py"
---

*The coupling I_K is a particular interaction for matter in the coset toy model of broken reciprocity. It is built from the model's two fields, the metric H and the real structure K, and it is local in position in one vacuum and local in momentum in the mirror vacuum. Evaluated on a single quantum state, it reduces in the first vacuum to an integral over the state's position profile, its waveform, and in the second to the same integral over its momentum profile, the spectrum of that waveform, so one state can give different values in the two vacua. Because the interaction depends on the sign of K, it also gives the breaking of reciprocity a physical effect. The arrangement parallels the Standard Model's fermion masses, which follow from the Higgs field's vacuum value once the fermions' Yukawa couplings to it are given. Nothing in the toy requires matter to couple this way, which is why this is only the weak form of the locality criterion S5.*

**Status:** Alive — [V] (the worklog's "C [V], the weak form of S5" and "Weak form: passes [V].") — `verify/toy_s5.py` part C reproduces every number ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)), and the round-4 referee reproduced them independently; round-4 finding F5 narrowed the description to a coupling built from H as well as K. The strong form is [open](/wiki/symmetry-breaking/strong-locality).

## The criterion it answers

Before building anything, the toy work fixed its pass/fail criteria ([success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)). S1–S3 encode the referees' demand for an action in which [ρ](/wiki/phase-space/reciprocity/born-reciprocity) is a symmetry that the vacuum breaks; S5 asks that the vacuum's choice matter for matter:

> Matter coupled to the order parameter through ρ-symmetric couplings acquires, in the selected vacuum, interactions local in the selected Lagrangian (x) and nonlocal in its complement (p). In the ρ-image vacuum it is the other way round. (worklog, 'Success criteria')

The worklog (`notes/toy-lagrangian.md`) calls this "the analogue of a Yukawa coupling giving masses through a vacuum expectation value", and "the content of the program's claim that 'forces fade with distance, never with velocity difference' because the vacuum is polarized". A pass "requires an explicit computation, e.g. of a two-point function or an effective interaction, showing the anisotropy". S5 belongs to the second tier of criteria, "what would answer round 3", the critique that the framework does no work ([the 'framework does no work' critique](/wiki/program/framework-does-no-work)). The expectation written down beforehand was guarded: "S5 is the real test, and I expect it not to pass at the first attempt. The likely outcome is that locality has to be defined relative to K by hand." ('Predictions').

## The ingredients

- **Two mirror vacua.** In [model I](/wiki/symmetry-breaking/toy-models/coset-model) the fields are a phase-space metric H and a real structure K, and at H = 1 the vacua are the real structures K(φ) ([Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). The computation uses the two vacua +K_ref and −K_ref, with K_ref = diag(1, −1) (`verify/toy_coset.py`), the minima of the toy's ρ-preserving potential ([the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential)). [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) ρ exchanges them.
- **Two lines.** L+ and L− are the eigenlines of K, with eigenvalues +1 and −1; they are also the null lines of the neutral metric η = ωK ([the section condition](/wiki/symmetry-breaking/section-condition)). A phase-space point is written ξ = u e+ + v e−, so u is the coordinate along L+ and v along L− (`verify/toy_s5.py`). In the vacuum +K_ref, L+ is the x-axis; in −K_ref it is the p-axis (script: "at K = +K_ref, L+ = x-axis; at K = -K_ref, L+ = p-axis").
- **A state and its portrait.** Matter enters as a one-particle state ψ, drawn on phase space by its [Wigner function](/wiki/phase-space/reciprocity/wigner-function) W(x, p). The marginals of W are probability densities [T]: integrating over p gives |ψ(x)|², and integrating over x gives |ψ̃(p)|², where ψ̃ is the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) of ψ. The gate checks both marginals ("Wigner marginal over p is |psi(x)|^2", "Wigner marginal over x is |psi~(p)|^2").

## The coupling

```text
I[W] = ∫_{L+} du ( ∫_{L−} dv W )²                               (toy note §5)
```

Read from the inside out: integrating W along L− gives the probability density of the coordinate u, the state's profile along L+; the coupling squares that profile and integrates it along L+. The [toy-model note](/wiki/symmetry-breaking/toy-models) (`papers/reciprocity-toy-models.md`, version 2; "toy note" below) writes it I[W], or I; the worklog and the round-4 adjudication write I_K, a name that records its dependence on K.

In the two vacua, at H = 1, it becomes (toy note §5):

```text
vacuum +K_ref:   I = ∫ |ψ(x)|⁴ dx        local in x
vacuum −K_ref:   I = ∫ |ψ̃(p)|⁴ dp       local in p
```

In +K_ref the inner integral runs over p and returns |ψ(x)|²; in −K_ref it runs over x and returns |ψ̃(p)|². The same functional of the same state is the fourth-power integral of the waveform in one vacuum and of its spectrum in the other.

The word "local" has a concrete reading. ∫|ψ(x)|⁴ dx is the form a contact interaction, one that acts only when two particles are at the same point, takes in a mean-field treatment [T]; in the vacuum +K_ref the coupling acts like such an interaction in position, and in −K_ref like one in momentum. The note's abstract: "A coupling built from (H, K) makes interactions local in one and nonlocal in the other — the analogue of Yukawa-generated masses."

A state that is its own Fourier transform up to a phase, such as the oscillator ground state, gives the same value in both vacua [T]. The test therefore needs a state whose waveform and spectrum differ in shape; the script uses "a non-self-dual state (two displaced squeezed Gaussians)" (`verify/toy_s5.py`).

## The numbers [V]

The test state, with ℏ = 1 (toy note §5):

```text
ψ ∝ e^{−(x−1.3)²/0.7} + 0.6 e^{−(x+1.3)²/0.7}
```

| Value of I | Toy note §5 | Gate, `verify/toy_s5.py` | Round-4 referee |
|---|---|---|---|
| vacuum +K_ref, ∫\|ψ(x)\|⁴ dx | 0.4070 | 0.406972 | 0.406972 |
| vacuum −K_ref, ∫\|ψ̃(p)\|⁴ dp | 0.3600 | 0.360047 | 0.360047 |

The gate asserts that the two values differ (`abs(Ix - Ip) > 0.05*max(Ix, Ip)`, printed as "the two vacua give different physics for the same state  [0.4070 vs 0.3600]") and that they match the values the note quotes ("quoted: 0.4070 vs 0.3600"). It also checks the Fourier pair for consistency (Parseval) and both Wigner marginals. The referee reproduced the values "independently from explicit Wigner-function marginals", with the normalizations "int W = 1.0000, int W^2 = 0.1591549431 = 1/2pi" (`review/round4/referee/audit-notes.md`, Step 2(d); "audit notes" below; the printed values are in `review/round4/referee/out_sec5.txt`).

That file also prints "I_(-K)[F psi] = int |F(F psi)|^4 = 23.273691", which the referee traced to its own normalization error, "not a manuscript error"; the corrected run is in `review/round4/referee/out_sec5_fix.txt` (audit notes, Step 2(d)). On the program's side, the worklog records that two checks of this chunk "were vacuous on the first draft (an always-true term; a condition multiplied by 0) and were replaced by real tests before commit" ('Chunk 4').

## How it behaves under the symmetries

### Flipping K alone changes it

"**I is odd in K**, so it breaks the K → −K symmetry and makes the breaking of ρ physical (§2)." (toy note §5). For the test state the referee found "K->-K alone: I_-K[psi] - I_+K[psi] = -0.046925 (nonzero: K->-K alone is not a symmetry of I)" (`out_sec5_fix.txt`). This is the property that [the twisted element](/wiki/symmetry-breaking/twisted-element) calls for. Model I without matter is symmetric under K → −K as well as under ρ, so its vacuum keeps the combination ρ∘(K → −K), which acts on H exactly as ρ does, and calling ρ broken is a labelling choice. A coupling that depends on the sign of K removes that symmetry. The round-4 adjudication named this coupling as the example: "Breaking ρ means something physically only once a coupling odd in K breaks the K → −K symmetry, for example P4-type matter through I_K. This sharpens the S5 conclusion rather than contradicting it." (`review/round4-adjudication.md`, F3).

### Applying ρ to the state and to K together leaves it unchanged

ρ acts on states by the Fourier transform and on K by K → −K (script: "rho acts on states by the Fourier transform: psi -> psi~, and on K by K -> -K"). "The combined map (ψ → Fψ, K → −K) leaves I invariant." (toy note §5). Under F the Wigner function turns rigidly through a quarter turn of phase space, W_{Fψ}(x, p) = W_ψ(−p, x) (script; [T]), so the momentum profile of Fψ is the position profile of ψ reflected, and the fourth-power integral is unchanged. The gate checks "rho-covariance: I_{-K}[W_{F psi}] = I_{+K}[W_psi]", and the referee found "I_-K[F psi] = int |F(F psi)|^4 = 0.406972", equal to I_{+K}[ψ] (`out_sec5_fix.txt`). The coupling is therefore one of the "ρ-symmetric couplings" that S5 asks for.

### A coupling blind to K shows nothing

"A K-blind interaction ∫W² shows no asymmetry." (toy note §5). For a pure state ∫W² = 1/2π whichever axes are used [T], so it cannot depend on the vacuum. The gate checks that it is the same for ψ and Fψ and equals 1/(2π) ("a K-blind phase-space interaction int W^2 (= 1/(2 pi) for pure states) shows no asymmetry"). This is the control: the asymmetry between the vacua comes from the coupling's dependence on K, not from the state.

## It needs H as well as K (round-4 F5)

The note's statement (toy note §5): "I[W] = ∫_{L+} du (∫_{L−} dv W)² of a state's Wigner function needs H as well as K: rescaling the coordinate along L+ by 2 doubles it. It is covariant under the SO(2) fixing H = 1, not under Sp(2,ℝ)."

The reason is that K fixes the two lines but not a unit of length along them. The integral needs coordinates u and v, and K alone does not fix them. The referee kept K and the area element and changed the coordinates, "eigenline parametrisation rescaled e+ -> 2 e1, e- -> e2/2 (du dv preserved)", and the value went from 0.406972 to 0.813649 (audit notes, Step 2(d)). The adjudicator's script states the mechanism in a comment, `density along L+ in the rescaled coordinate u' = u/s is s*rho(s u'), so I scales by s` (`review/round4/adjudicator/arb.py`), and prints "scale s=2.0: I = 0.813944" (`arb.out`). The gate's check reads "I_K is not K-covariant alone: rescaling the L+ coordinate by 2 doubles it (it needs H)  [0.4070 -> 0.8139]". The adjudication writes the result as "(0.407 → 0.814)". The three scripts print slightly different doubled values; the gate asserts only that the ratio is 2 within its tolerance (`abs(I_s2/Ix - 2) < 1e-3`).

The missing scale comes from the metric: "A scale on L+ (from H) is needed" (audit notes, Step 2(d)). Rotations that keep H = 1 preserve it, and the referee checked one: "I_{R K0 R^-1}[W_R] = 0.40673 vs 0.40697 (difference = interpolation error)". That rotation group is "the SO(2) stabilising H=1 (which contains rho)". Other elements of Sp(2,ℝ), such as the squeeze in the referee's test, change the scale, and I changes with them. The referee's conclusion: "Calling it 'K-covariant' overstates; it is (H,K)-covariant." The adjudication upheld this as F5, and its revision 5 asked version 2 to "Call I_K (H, K)-covariant, covariant under SO(2) only." ([review round 4](/wiki/method/review/round-4)).

## The weak form of S5 [V]

The note's conclusion:

> Locality in the selected Lagrangian therefore follows from the vacuum once matter couples this way, as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling. (toy note §5)

The worklog's: "**Weak form: passes [V].** A ρ-covariant coupling of matter to K makes interactions local in L+ in one vacuum and in L− in the other. This works as a Yukawa coupling does." ('Chunk 4', S5 conclusion).

The analogy is the textbook one [T] ([Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs)). In the Standard Model a fermion's mass is proportional to the product of its Yukawa coupling to the Higgs field and the Higgs field's vacuum value. The vacuum supplies the scale; the Yukawa couplings are free parameters, one for each fermion, and they are inputs to the theory, not consequences of the vacuum. In the toy the vacuum supplies the sign of K, which fixes which line is L+, and the coupling I makes matter's interaction follow that line. As with the Yukawa couplings, the coupling is chosen.

The forecasts written before construction expected this outcome. The worklog's own prediction ("locality has to be defined relative to K by hand") was scored against the result "Weak form only; the strong form is open here and in the literature": "Hit" ('Assessment against the predictions'). The round-4 [pre-registration](/wiki/method/review/pre-registration) named, among its runner-up weakest links, "The weak form of matter locality is close to true by construction." (`review/round4-preregistration.md`). The adjudication scored the runner-ups "Partial on all three", with "I_K needs H (F5)" as the finding at this one.

## Limits

- **A functional of one state, not a field theory.** "'Locality' here is a quartic functional of a one-particle state, not an interacting field theory; the Yukawa analogy is heuristic. Claim correctly hedged in the text" (audit notes, Step 2(d)).
- **Chosen, not forced.** "Nothing here forces that coupling" (toy note §5), and "a mechanism forcing the (H, K)-coupling of matter" is listed under "Not shown" (§6). The strong form, "locality forced, not chosen" (worklog), is [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality). In the program the coupling is supplied by postulate [P4](/wiki/program/postulates/p4-polarized-matter).
- **Scope.** The values are computed at H = 1, in the phase-space plane (d = 1); "anything beyond d = 1" is not shown (§6).

## Superseded: a coupling built from K alone

Before round 4 the coupling was described as a function of K. The worklog called it "The ρ-covariant interaction I_K[W]" ('Chunk 4', part C) and, in its conclusion, "the K-covariant coupling"; the version of the note sent to review called it K-covariant, which the referee judged an overstatement (audit notes, Step 2(d), quoted above). Finding F5 showed that the coupling needs H as well, and version 2 calls it "A coupling built from (H, K)", "covariant under the SO(2) fixing H = 1, not under Sp(2,ℝ)" (§5). Its covariance under ρ itself is unaffected, since ρ lies in that SO(2). The gate's section heading still reads "a rho-covariant interaction built from K", a wording lag; the gate's checks include the F5 rescaling. The change is listed at [Superseded statements](/wiki/status/superseded).

## Sources

- `papers/reciprocity-toy-models.md` §5 — the coupling, its form in the two vacua, the test state and its values, its dependence on the sign of K, the combined map, the K-blind control, the need for H and the Yukawa analogy; Abstract — "local in one and nonlocal in the other"; §6 — the forcing mechanism and d > 1 not shown
- `verify/toy_s5.py` part C — the gated reproduction of every number, the Wigner marginals and the F5 rescaling; `verify/toy_coset.py` — K_ref = diag(1, −1)
- `review/round4/referee/audit-notes.md` Step 2(d) — the independent reproduction, the rescaling and rotation checks, F5, and "the Yukawa analogy is heuristic"; `review/round4/referee/out_sec5.txt`, `out_sec5_fix.txt` — the referee's printed values
- `review/round4-adjudication.md` 'Rulings' F3, F5, 'Revisions' 5, 'Pre-registration scored' — the coupling as the example of a K-odd coupling, (H, K)-covariance upheld, the scoring of the runner-up forecast
- `review/round4/adjudicator/arb.py`, `review/round4/adjudicator/arb.out` — the rescaling mechanism and the doubled value
- `review/round4-preregistration.md` 'Predictions' — "close to true by construction"
- `notes/toy-lagrangian.md` 'Success criteria', 'Predictions', 'Chunk 4', 'Assessment against the predictions' — the wording of S5, the forecast, part C [V] and the S5 conclusion, the score
