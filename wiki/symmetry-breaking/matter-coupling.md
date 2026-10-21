---
title: "Locality from an (H, K)-built coupling"
weight: 100
status: alive
description: "The coupling I_K is local in x in one vacuum and local in p in the other, odd in K and (H, K)-covariant; locality then follows from the vacuum as fermion masses follow from a Higgs vacuum value — the weak form of criterion S5."
provenance: [V]
sources:
  - "papers/reciprocity-toy-models.md §5"
  - "review/round4-adjudication.md 'Rulings' F5"
  - "verify/toy_s5.py part C"
  - "notes/toy-lagrangian.md 'Chunk 4: S5'"
  - "notes/toy-lagrangian.md 'Success criteria'"
  - "review/round4-preregistration.md 'Predictions'"
  - "review/round4/referee/audit-notes.md Step 2(d)"
---

*This page is about one particular interaction for matter in the coset toy model, built from the metric H and the real structure K, that is local in position in one vacuum and local in momentum in the mirror vacuum. Evaluated on a single quantum state, it reduces to an integral over the state's position profile in the first vacuum and over its momentum profile, the Fourier transform of the position profile, in the second, so the same state gives different values in the two vacua. Because the interaction distinguishes K from −K, it also gives the breaking of reciprocity a physical effect. The arrangement parallels the Higgs mechanism, in which particle masses follow from the Higgs field's vacuum value once the particles' couplings to it are given; nothing in the toy forces matter to couple this way, which is why this is only the weak form of the locality criterion S5.*

**Status:** Alive — [V] (the worklog's "C [V], the weak form of S5" and "Weak form: passes [V].") — `verify/toy_s5.py` part C reproduces the numbers; round-4 finding F5 narrowed the coupling to (H, K)-covariant; the strong form is open.

## Key facts

- **The criterion it answers.** S5: "Matter coupled to the order parameter through ρ-symmetric couplings acquires, in the selected vacuum, interactions local in the selected Lagrangian (x) and nonlocal in its complement (p). In the ρ-image vacuum it is the other way round." (worklog, 'Success criteria'; [Success criteria S0–S5](/wiki/symmetry-breaking/toy-models/success-criteria)).
- **The coupling.** For a state's [Wigner function](/wiki/phase-space/reciprocity/wigner-function) W, integrated along K's eigenlines L± ([the section condition](/wiki/symmetry-breaking/section-condition)):

  ```text
  I[W] = ∫_{L+} du (∫_{L−} dv W)²
  ```

  "At H = 1, in the vacuum +K_ref it is ∫|ψ(x)|⁴ dx (local in x); in −K_ref it is ∫|ψ̃(p)|⁴ dp." (toy-model note §5).
- **The numbers [V].** "For ψ ∝ e^{−(x−1.3)²/0.7} + 0.6 e^{−(x+1.3)²/0.7}, the two vacua give 0.4070 and 0.3600." (§5). The gate prints 0.406972 and 0.360047 (`verify/toy_s5.py` part C; [The toy-model scripts](/wiki/method/verification/toy-model-scripts)).
- **Odd in K.** "I is odd in K, so it breaks the K → −K symmetry and makes the breaking of ρ physical (§2)." "The combined map (ψ → Fψ, K → −K) leaves I invariant. A K-blind interaction ∫W² shows no asymmetry." (§5; [the twisted element](/wiki/symmetry-breaking/twisted-element); [the Fourier transform](/wiki/phase-space/reciprocity/fourier-transform)).
- **It needs H as well as K (round-4 F5).** Upheld: "rescaling the eigenline coordinate by 2 doubles I (0.407 → 0.814)" (round-4 adjudication; [Review round 4](/wiki/method/review/round-4)). The note v2: "It is covariant under the SO(2) fixing H = 1, not under Sp(2,ℝ)." The worklog's earlier "ρ-covariant" is superseded by "(H, K)-covariant".
- **The weak form of S5 [V].** "Locality in the selected Lagrangian therefore follows from the vacuum once matter couples this way, as fermion masses follow from a Higgs vacuum value once Yukawa couplings are given. Nothing here forces that coupling." (§5). The worklog: "Weak form: passes [V]." See [Goldstone modes and the Higgs mechanism](/wiki/symmetry-breaking/goldstone-and-higgs).
- **Limits.** The round-4 pre-registration expected "The weak form of matter locality is close to true by construction." The referee: "'Locality' here is a quartic functional of a one-particle state, not an interacting field theory; the Yukawa analogy is heuristic." (audit notes, Step 2(d); [Pre-registration](/wiki/method/review/pre-registration)). The strong form, locality forced rather than chosen, is [Open: forced locality and the P4 lock](/wiki/symmetry-breaking/strong-locality).

## Sources

- `papers/reciprocity-toy-models.md` §5 — the coupling, its values in the two vacua, its K-oddness, the Yukawa analogy
- `review/round4-adjudication.md` 'Rulings' F5 — (H, K)-covariance, upheld
- `verify/toy_s5.py` part C — the gated reproduction of every number
- `notes/toy-lagrangian.md` 'Chunk 4: S5' — part C [V] and the S5 conclusion
- `notes/toy-lagrangian.md` 'Success criteria' — the wording of S5
- `review/round4-preregistration.md` 'Predictions' — the weak form expected to be close to true by construction
- `review/round4/referee/audit-notes.md` Step 2(d) — "the Yukawa analogy is heuristic"
