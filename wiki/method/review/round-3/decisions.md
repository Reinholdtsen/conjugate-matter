---
title: "Round-3 decisions and lessons"
weight: 30
status: record
description: "Decision 1 strict sector separation, Decision 2 retire the soliton (routes a, b and c), Decision 3 drop the √N floor, Decision 4 the toy Lagrangian next; the blindness leak and the independent-anchor lesson."
sources:
  - "review/round3-adjudication.md 'Decisions'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "papers/broken-born-checkpoint-v2.md header"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "review/round3/referee/audit-notes.md Step 1"
  - "CLAUDE.md 'Since the handoff (2026-10-19)'"
---

*After the round-3 rulings, four decisions set the program's next steps. Paul delegated them on 2026-10-19, Claude made them, and Paul keeps the veto. They took the postulate that gauge forces do not cross between the two polarizations at face value, retired the soliton dark-matter candidate rather than keep it alive with a free dilution factor, dropped a queued calculation whose premise the review had inverted, and made the toy Lagrangian the next task. The round also produced two lessons, now in `CLAUDE.md`: keep the forecast out of the commit subject, and check numbers against anchors that are independent of the paper.*

**Status:** Record, in force — untagged — `review/round3-adjudication.md` 'Decisions' and 'Lessons'; executed in #11 v2.1 (2026-10-19), and Decision 4 in the toy-model note reviewed in [round 4](/wiki/method/review/round-4).

## Key facts

- **The delegation.** "Paul delegated these on 2026-10-19 ('You make the decisions for me and give rational'). Claude made them. Paul keeps the veto." ([the collaboration](/wiki/method/collaboration))
- **Decision 1: strict sector separation.** "ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry." It is "the program's own postulate P4 ('gauge forces do not cross polarizations') taken at face value" ([P4](/wiki/program/postulates/p4-polarized-matter)). The alternative "rested on an unsupported coefficient" (ruling 7), and strict separation "closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector" ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)). Unresolved reading: #11 P4 and this decision write ε ≲ 10⁻¹³, while the round-3 referee notes that Gherghetta et al. present 10⁻¹³ as a floor, the "minimum kinetic mixing in any theory with hidden gauge interactions and charge symmetry breaking", consistent with "≲" only in the sense "up to"; no document reconciles the two readings.
- **Decision 2: the soliton candidate retired** "as a program-native proposal (route c)" ([the obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary)):
  - route (a), v ≲ 100 PeV, "works, but it is Murayama–Shu's and Liveoak–Maharana–Wells's model"; "claiming it would add no testable content and would misattribute it" ([topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art));
  - route (b), superheavy plus a named dilution, "restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3)", and "the program does not trade falsifiability for survival";
  - route (c), retirement, follows "the Debt 3 obituary: a dead claim is reported prominently and stays dead" ([the momentum-clumping obituary](/wiki/dark-matter/momentum-clumping/founding-image); [negative results](/wiki/method/negative-results)). The trilemma "becomes two program-native candidates (gated χ particles; the X-condensate)" ([χ particles](/wiki/dark-matter/candidates/chi-particles); [the X-condensate](/wiki/dark-matter/candidates/x-condensate)).
- **Decision 3: the √N floor dropped** (`HANDOFF.md` §8 item 3): "Its premise, Kibble as a ceiling, is inverted (ruling 3)", and "Under decision 2 it has no candidate left to serve." ([Obituary: the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor))
- **Decision 4: the toy Lagrangian next**, after one short cleanup. "Every referee across three rounds converges on 'the framework does no work'. The toy action is the only item that can change that, and it is acceptance criterion 1 for anything the program proposes." "Candidate-level work is downstream of it." The cleanup: amend #11 with the soliton obituary, check the Freidel–Leigh–Minic prior art and re-tag the compatibility theorem, and give §10 the DESI DR2 phantom-crossing nuance (ruling 11). #11 v2.1 did all three ([acceptance criterion 1](/wiki/symmetry-breaking/toy-models/acceptance-criterion); [the 'framework does no work' critique](/wiki/program/framework-does-no-work); [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).
- **Executed the same day.** v3 "moved to `notes/` with a withdrawal banner", and the gate's script for v3's claims, knot_numbers.py, "was replaced by `verify/soliton_obituary.py`, which checks every number this record quotes, with independent anchors". "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything." ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script))
- **Lesson 1, the blindness leak.** "Keep the prediction out of the pre-registration commit subject. The auditor's auto-attached git status showed it." The verdict differed from the prediction, "which argues against anchoring. But the round was less blind than intended." ([round-3 pre-registration](/wiki/method/review/round-3/preregistration); [pre-registration](/wiki/method/review/pre-registration))
- **Lesson 2, independent anchors.** "An anchor must be independent of the paper. v3's Kibble anchor reproduced v2's own number and so tested nothing. The replacement anchors are the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume." ([independent anchors](/wiki/method/verification/independent-anchors))

## Sources

- `review/round3-adjudication.md` 'Decisions' — the delegation, Decisions 1–4, routes (a)–(c) and the same-day execution
- `review/round3-adjudication.md` 'Lessons (now in CLAUDE.md)' — the two lessons
- `papers/broken-born-checkpoint-v2.md` header, §4, §12 — the v2.1 amendments that executed the cleanup; P4 strict; the obituary
- `review/round3/referee/audit-notes.md` Step 1 — the referee's reading of Gherghetta et al.'s 10⁻¹³ as a floor
- `CLAUDE.md` 'Since the handoff (2026-10-19)' — strict P4 in force; the soliton candidate dead
