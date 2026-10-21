---
title: "The Debt-3 calc notes (#2–#4)"
weight: 40
status: record
description: "debt3a (stream stability), debt3b (the wave island) and debt3c (the ultra-faint-dwarf endpoint): final for their scope, with no verify/ coverage."
sources:
  - "notes/debt3a-stream-stability.md"
  - "notes/debt3b-wave-island.md"
  - "notes/debt3c-ufd-endpoint.md"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "CLAUDE.md 'Layout'"
---

*The Debt-3 calc notes are three short working notes, artifacts #2 to #4, that tested the program's founding image: dark matter clumping by velocity rather than in space. The first showed that particle dark matter cannot clump this way. The second found that dark matter light enough to behave as a wave can, but only as an option, except in one scenario where clumping becomes compulsory in the smallest galaxies. The third showed that this scenario would have drained those galaxies of their dark matter, which observation rules out. Together they closed Debt 3 with a negative result, which the checkpoint #11 now reports as an obituary. The notes are final for their own scope, and no script checks their numbers.*

**Status:** Record, final for its scope — the notes carry few tags of their own (3b's rate is "[D, heuristic coefficients]"); #11 §9 tags the particle-island result [D] and the wave-island result [D + T] — no `verify/` script covers any Debt-3 number.

## Key facts

- **#2, debt3a: "Debt 3, Chunk A: Linear stability of the conjugate sector's velocity-space fragmentation."** "Result: negative on the particle island, with a structural corollary." The mean-field criterion "Fails by 28–31 orders of magnitude" at the scattering benchmark ([the criterion and its shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion)), and the corollary is [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem): "Collective velocity-space dynamics and classical-particle dark matter are mutually exclusive within this framework." The setup is [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model).
- **#3, debt3b: "Debt 3, Chunk B: Gated condensation on the wave island."** "Status: rate derived, environments evaluated, verdict reached. Coefficients heuristic at O(1)–O(10) level; calibration against Levkov–Panin–Tkachev (LPT) numerics is a flagged to-do." It derives [the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate), finds the island discriminant (suppression e^{−v²/v\*²} on the particle island, (v\*/σ)⁴ on the wave island; [row 3](/wiki/predictions/island-discriminant)), and splits [the wave island](/wiki/dark-matter/momentum-clumping/wave-island) into [Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a), mandatory condensation in ultra-faint dwarfs, and [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b): "streams are tunable, not mandatory". Misalignment supplies the relic abundance ([misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)).
- **#4, debt3c: "Debt 3, Chunk C: The ultra-faint-dwarf endpoint — closing Debt 3."** "Status: complete. Verdict: Scenario A falsified; Debt 3 closed." Its conclusion is [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem): "Nowhere in the viable parameter space of BBT is velocity-space clumping a mandatory phenomenon" (BBT: the Broken-Born framework). "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands" ([old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity); [old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction)), and "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings."
- **Standing.** `HANDOFF.md` §3 marks all three "final", and #4 "final — closes Debt 3 (negative)". The root `CLAUDE.md` places them with the notes, "the audit trail, superseded as reference but kept", and #11 §9 is the current summary ([Momentum clumping (Debt 3)](/wiki/dark-matter/momentum-clumping); [the three debts](/wiki/history/debts)).
- **No machine check.** `HANDOFF.md` §2 marks "criterion fails by 10²⁸–10³¹ ✓" as machine-verified, but no `verify/` script computes it and #11 §9 tags the result [D]. The wiki follows #11; whatever check existed is in the old chat ([the iron rule](/wiki/method/verification/iron-rule)).
- **Where the three differ.** 3a gives the wave-island suppression as (v\*/σ)³, while 3b, 3c and #11 give (v\*/σ)⁴. The wave island's upper edge is "≲ meV" in 3a, "≲ 0.1 meV" in 3b and 10⁻⁴ eV in 3c, the final note. The notes number the predictions rows as #1 §9 does, so their "rows 3 and 4" are the old rows, not #11 §13's. Unresolved: Scenario B's fuzzy-dark-matter option at m ∼ 10⁻²² eV (3b) lies below 3c's lower edge of 3×10⁻¹⁹ eV, and neither note addresses it ([Conflicts between sources](/wiki/history/documents/source-conflicts)).
- **The plan they ended on.** 3b and 3c close by planning "Debt 1, Chunk 1a", a linearization with ω and η frozen. The Debt-1 work that followed made η emergent instead ([the Debt-1 notes](/wiki/history/documents/debt-1-notes)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §9 — the current summary and its tags
- `HANDOFF.md` §3 rows 2–4 — the notes' standing; §2 — the ✓ on 10²⁸–10³¹
- `CLAUDE.md` 'Layout' — the notes as the audit trail
- `notes/debt3a-stream-stability.md` — the particle island and the classicality theorem
- `notes/debt3b-wave-island.md` — the condensation rate, the island discriminant and Scenarios A and B
- `notes/debt3c-ufd-endpoint.md` — the endpoint, the verdict and the net theorem
