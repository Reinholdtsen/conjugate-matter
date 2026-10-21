---
title: "Quantum restoration in the complex model"
weight: 60
status: alive
description: "Every condensate phase is an exact flat direction and the condensate is a localized lump with no volume factor, so ⟨Δ⟩ = 0 and the classical breaking does not survive; the tadpole grows with the truncation (ln N or 2 ln N, unreconciled), and the exact-solution check is not done."
provenance: [D]
sources:
  - "papers/reciprocity-toy-models.md §4"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §6"
  - "papers/reciprocity-toy-models.md v1 (commit d9a06ac) §4"
  - "verify/toy_gw.py S1"
  - "verify/toy_gw.py 'Tadpole'"
  - "review/round4-adjudication.md 'Rulings' F6"
  - "review/round4-adjudication.md 'Revisions' 4"
  - "review/round4-adjudication.md 'Pre-registration scored'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 1"
  - "review/round4/referee/audit-notes.md Step 2(c)"
  - "review/round4/referee/audit-notes.md Step 3"
  - "review/round4/referee/out_model2_quantum.txt"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/toy-lagrangian.md 'Assessment against the predictions'"
  - "notes/toy-lagrangian.md 'Write-up and review'"
---

*Quantum restoration is the result that the classical breaking found in the complex [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar) does not survive quantization. The vacua form a circle labelled by the relative phase β of two condensed oscillator levels, and an exact symmetry turns the circle at no cost in action, so the quantum theory weights every value of β equally. A spontaneous choice can still survive in a system large enough that a vanishingly small bias, acting over its whole volume, pins it. This condensate occupies two oscillator levels and is a localized lump, so it supplies no such volume factor. The quantum average of the polarization is therefore zero, and criterion S4, survival of the breaking under quantum fluctuations ([success criteria](/wiki/symmetry-breaking/toy-models/success-criteria)), fails for this route. Round 4 confirmed the conclusion, asked for the argument to be restated on these two grounds, and added that the bare mass must be renormalized as the truncation grows. The comparison with an exactly solved related model, the natural independent check, has not been made.*

**Status:** Alive, a negative result — tagged [D] in the worklog ("S4 fails, by an exact argument [D]"). Its premise, the exact phase symmetry, is gated in `verify/toy_gw.py`, as is the logarithmic tadpole ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)). The referee of [review round 4](/wiki/method/review/round-4) confirmed the conclusion "in substance" and found the phase decoupling "stronger than stated"; version 2 restates the argument. One step is "argued against, not proven", and the exact-solution comparison is open.

## The claim

The [toy-model note](/wiki/symmetry-breaking/toy-models), version 2 (§4):

> **Model II, complex fields: restoration.**
> - Every condensate phase is an exact flat direction, by the U(1)^N × U(1)^N symmetry.
> - At fixed μ² the condensate occupies finitely many levels: it is a localized lump, not an extended order. Nothing supplies a volume factor that could suppress fluctuations of β.
> - So the quantum measure is uniform in β at every truncation, and ⟨Δ⟩ = 0. The classical breaking of §3 does not survive quantization.

Here β is the relative phase of the condensed entries φ₀₀ and φ₁₁, and Δ(β) = Δ(0) cos β is the vacuum's polarization, its spread in position minus its spread in momentum ([complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)). N is the number of oscillator levels kept. The argument has three steps.

## Step 1: every condensate phase is an exact flat direction

The complex action is unchanged when the rows and columns of the field's matrix are multiplied by arbitrary phases: "S[UφV†] = S[φ] for all diagonal unitaries U, V" (§3; † is the Hermitian adjoint here, not the citation mark). On a diagonal vacuum this rotates the phase of each condensed entry independently at no cost, so each phase is a flat direction, and β is one of them ([complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)). The gate checks the premise: "complex model: S[U phi V^dag] = S[phi] for any diagonal unitaries U, V (a continuous U(1)^N x U(1)^N)".

Flatness here is exact, not an accident of the classical action. A symmetry of the action, with an integration measure that the symmetry also leaves unchanged, is a symmetry of the quantum theory, so no quantum correction can produce a potential for β [T]. The round-4 referee: "Exact phase decoupling CONFIRMED and stronger than stated: S is invariant under independent diagonal U, V (N=10: S = 7638.11944458 at 5 random (U,V)); every condensed level's phase is an independent exact flat direction. So <Delta>=0 at any truncation follows from symmetry alone, and no beta-dependence can be generated at any loop order." (audit notes, Step 2(c)).

## Step 2: no volume factor

That the average vanishes at any finite truncation is not yet an argument against breaking. In any finite system with a symmetry, the exact quantum average of an [order parameter](/wiki/symmetry-breaking/order-parameter) that the symmetry reverses is zero [T]. [Spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking) is defined by an order of limits [T]: add a small field h that favours one vacuum, take the size of the system to infinity, and only then remove the field. In an extended order the field acts over the whole volume, its effect grows with the volume, and the chosen vacuum survives as h → 0. The referee stated the operative point in these terms:

```text
β is one compact collective coordinate with an action of order one (no volume factor), so

    lim_{h→0} lim_{N→∞} ⟨Δ⟩_h = 0
```

("Logical gap: <Delta>=0 at finite truncation holds for any symmetric finite system and is not by itself an argument against" spontaneous breaking; "the operative point is that beta is one compact collective coordinate with O(1) action (no volume factor), so lim_{h->0} lim_{N->inf} <Delta>_h = 0", audit notes, Step 2(c), with "any" lowered from capitals.)

The condensate is a lump, not an order spread through space. At fixed μ² only the levels with negative quadratic coefficient condense, finitely many of them, and the vacuum profile is a finite sum of oscillator functions that decays away from the origin. The referee cites de Goursac, Tanasa and Wallet's description of such vacua, "decays at infinity ... finite linear combination of Schwartz functions", and concludes that "a thermodynamic limit with an intensive order parameter never existed" (Step 2(c)). The worklog's form of the step: "β has no stiffness. The condensate occupies finitely many oscillator levels at fixed μ², so nothing couples β across space." ('Chunk 3 results').

## Step 3: the quantum average of Δ vanishes

The quantum theory weights field configurations by their action, and the weight does not depend on β. Over a uniform circle the average of cos β is zero, so

```text
⟨Δ⟩ = Δ(0) ⟨cos β⟩ = 0
```

"So the quantum measure is uniform in β at every truncation, and ⟨Δ⟩ = 0. The classical breaking of §3 does not survive quantization." (§4). The quantum ground state is spread evenly over the circle of classical vacua, and the duality, which shifts β by π, maps it to itself.

The worklog's verdict on the route: "**Net: chunk 2's classical breaking of the duality does not survive quantization.** The route gives a polarized classical vacuum and no quantum symmetry breaking." ('Chunk 3 results'). Its scorecard records S4 as a "fail for both exactly self-dual versions in 1+1 / at fixed μ²", and its assessment: "The [Grosse–Wulkenhaar] route fails S4 outright: zero mode, no stiffness." ('Assessment against the predictions'; [success criteria](/wiki/symmetry-breaking/toy-models/success-criteria)).

## Why round 4 asked for a restatement

The first version of the note (commit d9a06ac, §4) argued that β "is the orbit of an exact continuous symmetry", that "nothing couples β across space", and that therefore "⟨Δ⟩ = 0 exactly" at every truncation. The referee confirmed the conclusion and moved its weight onto the two steps above: "Correct conclusion (no [spontaneous symmetry breaking]), but the strongest reason is the exact U(1)^N x U(1)^N invariance (every condensate phase decoupled) plus the absence of a volume factor (the condensate is a localised Schwartz-class lump)." (audit notes, Step 3). "Conclusion CONFIRMED in substance; argument should be restated." (Step 2(c)).

The adjudication's revision 4: "restate the restoration argument (exact independence of the condensate phases, no volume factor), add the 2 ln N mass renormalization, and compare with Langmann–Szabo–Zarembo." Version 2 restated the argument and added the mass renormalization, with the coefficient written ln N (caveat 1); it did not make the comparison (the open section below).

The pre-registration had named this argument the first runner-up weakest link: "Model II's quantum-restoration argument. The tunnelling step is argued, not proven, and a referee may raise large-N matrix-model transitions or noncommutative nonlocality as ways around 'nothing couples β across space'." (`review/round4-preregistration.md`; [pre-registration](/wiki/method/review/pre-registration)). The adjudication scored the outcome "Restoration conclusion confirmed but must be restated (F6, [Langmann–Szabo–Zarembo])", one of three runner-ups scored "Partial on all three" ('Pre-registration scored').

## Caveat 1: the bare mass runs with the truncation

"The bare μ² is itself renormalized. The level-0 tadpole grows as ln N (it is a harmonic sum), so fixed bare μ² is not a consistent large-N limit." (§4).

**What a tadpole is** [T]. At one loop, the quartic interaction corrects the mass of a mode by a diagram in which the vertex closes on itself: the mode's mass term picks up the sum of the fluctuations of all the modes it couples to, each weighted by its propagator. In two-dimensional φ⁴ theory this sum diverges logarithmically with the cutoff, and the divergence is absorbed into the bare mass, which must then change with the cutoff. Here the truncation N plays the cutoff. The adjudication: "2D φ⁴ needs mass renormalization." ('Rulings' F6).

**The finding (F6).** The referee's objection was to a sentence of the first version, "Increasing the truncation adds only massive levels" ([superseded](#superseded-increasing-the-truncation-adds-only-massive-levels) below): "'Increasing the truncation adds only massive levels' omits mass renormalisation. … At fixed bare mu^2 the low-level condensate is destroyed at large N; mu^2 must be renormalised with N. Does not change the no-[breaking] conclusion." (audit notes, Step 2(c)). The adjudication ruled it "**Accepted, not re-checked**": "The no-breaking conclusion is unaffected; the argument must be restated." ('Rulings' F6).

**The checks.** The gate's section "Mass renormalization: the tadpole grows logarithmically with the truncation (round-4 F6)" checks the growth of a harmonic sum: "sum_{k<N} 1/(k+1) - ln N -> Euler's gamma (the level-0 tadpole with G_0k = 1/(k+1) is ~ ln N)", printing "[0.62638 0.57772 0.57722]" for N = 10, 1000 and 100000 and asserting agreement with Euler's γ = 0.5772156649 to 1e-4 at the largest N. The referee's own computation took the one-loop average of the second derivative of the quartic term with respect to φ₀₀, "4*G00 + 2*G01 + 2*G02 + 2*G10 + 2*G20" at N = 3, "i.e. 2 sum_k (G_0k + G_k0)", with propagators G_ij = 1/(i + j + 1 + M²), and found "T_0(N) - 2 ln N -> -0.8455 (N=10^5), i.e. the tadpole grows as 2 ln N" (audit notes, Step 2(c)). Its output defines T₀(N) = Σ_k [G₀ₖ + Gₖ₀] at M² = 1 and lists T₀ − 2 ln N from N = 10 to 10⁵ (`review/round4/referee/out_model2_quantum.txt`).

### The coefficient: ln N or 2 ln N

The sources disagree on the coefficient, and no document reconciles them:

- **ln N**: version 2 of the note ("grows as ln N (it is a harmonic sum)"), the worklog ("the restoration argument restated, with the ln N tadpole", 'Write-up and review') and the gate, which sums one series, Σ_{k<N} 1/(k+1), with G₀ₖ = 1/(k+1).
- **2 ln N**: the referee and the adjudication (F6, "the 2 ln N mass renormalization"; revision 4), from T₀(N) = Σ_k (G₀ₖ + Gₖ₀), a sum of two series.

The two use different definitions of the level-0 tadpole. Version 2 is the higher-ranked statement, and both agree that the growth is logarithmic and that the conclusion stands ([source conflicts](/wiki/history/documents/source-conflicts)).

## Caveat 2: a potential on β is argued against, not proven

"Whether a potential on β could be stabilized by the massive tower is argued against, not proven." (§4). The worklog's version of the step: "Even a potential on β cannot rescue it. The order-parameter sector stays finite-dimensional, so the system tunnels between the two vacua. This last step is argued, not proven: integrating out the massive tower is assumed not to make the barrier grow with N." ('Chunk 3 results').

The question is what happens if the circle is tilted by a potential that leaves a few discrete minima, as [model I](/wiki/symmetry-breaking/toy-models/coset-model)'s potential does. A finite system tunnels through a barrier of finite height, so a choice among discrete minima survives only if the barrier grows without bound [T]. This is the reason the success criteria start in 1+1 dimensions: "In 0+1 dimensions (quantum mechanics), tunnelling restores any symmetry" (worklog, 'Success criteria'). The unproven assumption is that the massive levels above the condensate, once integrated out, do not make the barrier grow with N. The referee: "The 'tunnelling' caveat is only needed for the add-a-potential variant." (audit notes, Step 2(c)). The exactly symmetric model needs no such step.

## What it means for the route

Model II was tried first because its own vacuum might select position or momentum "with no K put in by hand" (worklog, 'Chunk 1 results'). The complex model does select classically and loses the selection under quantization; the real model is not duality-symmetric, and its selection at one loop is explicit ([Open: the real model's one-loop preference](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/real-model-lead)). The S4 result therefore came from the fallback named in chunk 1, "Discrete reduction by a τ-type potential" in model I. Its first form, the [naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential), died in round 4; its repair, [the bounded potential V_b](/wiki/symmetry-breaking/toy-models/coset-model/bounded-potential), orders in the [frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction). The note's abstract states the general lesson for model II: "In complex model II the breaking does not survive quantization: every condensate phase is an exact flat direction, and the condensate is a localized lump with no volume factor." See also [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking).

## Open: the comparison with the exact solution

"The exact solution of the related model [8] is the natural independent check. We have not carried it out." (§4). Ref. [8] is Langmann, Szabo and Zarembo, "Exact solution of quantum field theory on noncommutative phase spaces" (hep-th/0308043). The round-4 referee found it as omitted prior work: an "exact solution of the complex model at a special self-dual point (U(infty) degeneracies)", "Directly relevant to Sec. 4 restoration claim" (audit notes, Step 1). Revision 4 asked for the comparison; version 2 cites the paper and reports the comparison as not done. The item is tracked with the other open ends at [open problems](/wiki/status/open-problems).

## Superseded: "Increasing the truncation adds only massive levels"

**The earlier statement.** The first version of the note (§4): "Increasing the truncation adds only massive levels" (quoted in round-4 finding F6). The worklog's form: "Raising N adds only massive levels; the condensate does not grow." ('Chunk 3 results').

**What replaced it.** Version 2's restated argument, which rests on the exact independence of the condensate phases and the absence of a volume factor, and adds the caveat that the bare μ² is renormalized and fixed bare μ² "is not a consistent large-N limit" (§4).

**Why.** The added levels are not inert. Through the tadpole they shift the effective mass of the lowest level by an amount that grows with N, and from this the referee concluded that at fixed bare μ² "the low-level condensate is destroyed at large N" (audit notes, Step 2(c)). The adjudication accepted the finding without re-checking it and ruled that the no-breaking conclusion is unaffected ('Rulings' F6). The register of [superseded statements](/wiki/status/superseded) lists the change.

## Sources

- `papers/reciprocity-toy-models.md` §4, Abstract, §6 — the restoration argument and its two caveats, quoted above; the uncompleted exact-solution check
- `papers/reciprocity-toy-models.md` version 1 (commit d9a06ac) §4 — the argument as first stated, with "Increasing the truncation adds only massive levels"
- `verify/toy_gw.py` S1, 'Tadpole' — the gated phase symmetry; the harmonic-sum check of the tadpole's growth
- `review/round4-adjudication.md` 'Rulings' F6, 'Revisions' 4, 'Pre-registration scored' — F6 accepted, not re-checked; the requested restatement and comparison; the scored runner-up
- `review/round4-preregistration.md` 'Predictions' — the restoration argument as the first runner-up weakest link
- `review/round4/referee/audit-notes.md` Step 1, Step 2(c), Step 3 — the Langmann–Szabo–Zarembo paper; "stronger than stated", the logical gap, the 2 ln N tadpole; the strongest reasons for the conclusion
- `review/round4/referee/out_model2_quantum.txt` — the referee's tadpole sums and the N = 10 phase-invariance check
- `notes/toy-lagrangian.md` 'Chunk 3 results', 'Assessment against the predictions', 'Write-up and review' — the original argument [D], its superseded "only massive levels" step and the argued tunnelling step; the S4 scorecard; the ln N restatement
