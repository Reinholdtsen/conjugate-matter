---
title: "The polarization as a Goldstone angle"
weight: 60
status: alive
description: "Where ρ sits inside a continuous U(1) (model I and the complex model II), the x-sharp and p-sharp vacua are joined by a flat direction; the consequences for P5 and τ, and the worklog's 3+1 remark."
provenance: [D, V]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/reciprocity-toy-models.md Abstract"
  - "papers/reciprocity-toy-models.md §2"
  - "papers/reciprocity-toy-models.md §3"
  - "papers/reciprocity-toy-models.md §6"
  - "notes/toy-lagrangian.md 'Chunk 2 results'"
  - "notes/toy-lagrangian.md 'Chunk 3 results'"
  - "notes/toy-lagrangian.md 'Assessment'"
  - "review/round4-adjudication.md 'Revisions' 3"
  - "verify/toy_coset.py"
  - "verify/toy_gw.py"
---

*Born reciprocity is a quarter turn of the position–momentum plane, the operation the Fourier transform performs when it turns a waveform into its spectrum. In the program's toy models this exchange is one member of a continuous family of symmetry transformations, so the vacuum's polarization, which fixes the direction that counts as position, is an angle that can rotate smoothly rather than a switch with two settings. Rotating that angle costs no energy, which makes it a Goldstone direction, and the position-sharp and momentum-sharp vacua lie on one continuous family. This finding, recorded in #11 v2.2, is why a definite polarization needs an added potential on the angle; in the coset model the angle is the same circle the program identifies with its dark-energy field τ. It is evidence from two toy models, not a theorem.*

**Status:** Alive — [D][V] (#11 §4, P2′ refinement; #11 §10, "Toy-model support (v2.2) [D][V]") — machine-checked in the toy models (`verify/toy_coset.py`, `verify/toy_gw.py`; [The toy-model scripts](/wiki/method/verification/toy-model-scripts)); the consequences for τ are consistency only, and the 3+1 remark is an uncomputed worklog conjecture.

## Key facts

- **The structural finding.** "At the self-dual point, Born reciprocity is never the whole symmetry. It is one element of a continuous U(1): the coset model: the U(1) stabilizer of H that rotates K; Grosse–Wulkenhaar: the left phase rotations e^{−iαN}, with the duality at α = π." "So 'which polarization' is an angle on a Goldstone circle, not a discrete choice. The x-sharp and p-sharp vacua are joined by a flat direction." "This is model-level evidence from two toys, not a theorem." (worklog, 'Chunk 2 results'; see [Goldstone modes](/wiki/symmetry-breaking/goldstone-and-higgs), [model I](/wiki/symmetry-breaking/toy-models/coset-model) and [model II](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar)).
- **Scope.** The note v2: "In model I and complex model II, ρ sits inside a continuous U(1), so the polarization is a Goldstone angle." (§6). The real model II is different: its vacua are "diag(±√q₀, ±√q₁)", discrete, and there the duality is "only a covariance" (§3, Abstract; [Complex versus real fields](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-and-real-fields)). Within model II, round-4 revision 3 reads: "Restrict 'Goldstone angle' to the complex model."
- **In the postulates [D][V].** "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]." (#11 §4; [P2′](/wiki/program/postulates/p2-prime)). It is the first of the v2.2 qualifications of [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking).
- **Model I's angle is τ's circle.** The compact flat direction is "the compact angle φ, which parametrizes the Lagrangian Grassmannian Λ(1)" (toy-model note §2; [Model I vacua](/wiki/symmetry-breaking/toy-models/coset-model/vacua)). #11 §10: "In the coset model that angle parametrizes Λ(1): it is τ's circle." and "None of this tests the cosmology; it only shows the structure is consistent." See [The Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian), [τ as the Maslov phase](/wiki/phase-space/modular-field/maslov-phase) and [τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence).
- **Complex model II.** Along the flat phase β the vacuum's polarization is "Δ(β) = ⟨x²⟩_vacuum − ⟨x²⟩_dual equals Δ(0) cos β" (§3; [Complex-model vacua](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/complex-vacua)), but "the breaking does not survive quantization: every condensate phase is an exact flat direction, and the condensate is a localized lump with no volume factor" (Abstract; [Quantum restoration](/wiki/symmetry-breaking/toy-models/grosse-wulkenhaar/quantum-restoration)).
- **Consequences for P5 and τ (worklog; conjecture).** "(i) P5's 'the vacuum selects a polarization; ours is x-tilted' needs explicit breaking of that U(1) — a potential on the circle — to make the selection definite." "(ii) In the coset toy, the circle is the Lagrangian Grassmannian Λ(1), the checkpoint's τ." "(iii) It also means the present-day thawing of τ would be a slow drift of the polarization angle. That is a claim about the program, not verified here." (worklog, 'Chunk 2 results'). The worklog's added remark that both toys support §10 overstates: only the coset circle is Λ(1). The note calls the link to a dark-energy field "Motivation, not result" (§6). See [P5](/wiki/program/postulates/p5-spontaneous-selection), [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential) and [Row 4](/wiki/predictions/dark-energy-drift).
- **The 3+1 remark (worklog only; uncomputed).** "In 3+1, the program's actual dimension, Coleman–Mermin–Wagner does not apply. There the self-dual coset model can break the continuous U(1) itself, with τ an exactly massless Goldstone. §10's τ has a potential, so the explicit breaking is in the program anyway." (worklog, 'Chunk 3 results'; finding 3 of 'Assessment'). The note covers only 1+1 with d = 1 ([The Mermin–Wagner–Coleman theorem](/wiki/symmetry-breaking/mermin-wagner-coleman)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — the P2′ refinement: a Goldstone angle [D][V]
- `papers/broken-born-checkpoint-v2.md` §10 — 'Toy-model support (v2.2)': τ's circle, consistency only
- `papers/reciprocity-toy-models.md` Abstract, §2, §3, §6 — the scope (model I and complex model II), Λ(1), Δ(β), restoration
- `notes/toy-lagrangian.md` 'Chunk 2 results' — the structural finding and consequences (i)–(iii)
- `notes/toy-lagrangian.md` 'Chunk 3 results', 'Assessment' — the 3+1 remark; unpredicted finding 1
- `review/round4-adjudication.md` 'Revisions' 3 — "Goldstone angle" restricted to the complex model II
- `verify/toy_coset.py`, `verify/toy_gw.py` — the flat directions in each model
