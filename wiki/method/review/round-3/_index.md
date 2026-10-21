---
title: "Review round 3"
weight: 60
status: hub
description: "The execution-verified blind audit of #14 v3 on 2026-10-19: verdict C, thirteen rulings, the decisions that retired the soliton candidate, and the lessons now in CLAUDE.md."
bookCollapseSection: true
---

*Review round 3 was the blind audit of version 3 of #14, the standalone proposal that dark matter consists of superheavy 't Hooft–Polyakov monopoles of a hidden gauge sector, run on 2026-10-19 by a fresh subagent that could execute code. The referee checked every citation against its source, re-ran every number in its own scripts and re-derived the compatibility theorem, and graded the manuscript C, fundamentally flawed: the count of monopoles formed in the early universe, on which the predicted mass rested, used a wrong normalization of the Kibble estimate. The author's adjudication agreed, upheld the central findings, and retired the soliton candidate. The round also wrote two lessons into the project's method.*

**Stands:** the records — [the pre-registration](/wiki/method/review/round-3/preregistration), [the verdict, rulings and citation audit](/wiki/method/review/round-3/rulings), [the decisions and lessons](/wiki/method/review/round-3/decisions), [the arbitration and the referee's constants](/wiki/method/review/round-3/arbitration) · **Died:** nothing in this section; the round's casualties have obituaries in the soliton-candidate section: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary), [the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization), [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window), [Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) and [the √N floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) · **Open:** nothing in this section

## Map

Round 3 was planned in the claude.ai era. A first attempt, dispatched from claude.ai on 2026-10-17, "died partway on a rate limit after reporting 'most citations and core numbers checked; several omitted-constraint literature checks remaining'" (`HANDOFF.md` §6, which still calls the round incomplete). After the move to Claude Code, v3 was cut from [round 2's pending list](/wiki/method/review/rounds-one-and-two) and the round ran to completion under [the five-step protocol](/wiki/method/review/review-protocol). The pages follow the round in order.

- [Round-3 pre-registration](/wiki/method/review/round-3/preregistration) comes first because it was committed before the referee was dispatched: verdict B, the weakest link "the framework does no work", and no surviving numerical indictment expected. Its commit subject also leaked the forecast to the referee's environment.
- [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings) is what the referee found and how each of its thirteen findings was ruled: the grade C, the Kibble normalization, the overproduced benchmark, the ψ window, the one overturned citation complaint, the omitted constraints accepted as a to-do, and all 23 references resolving.
- [Round-3 decisions and lessons](/wiki/method/review/round-3/decisions) is what the program did next: strict sector separation, the retirement of the soliton candidate, the dropped √N floor and the toy Lagrangian as the next task, plus the two lessons now in `CLAUDE.md`.
- [Round-3 arbitration and the referee's constants](/wiki/method/review/round-3/arbitration) is the numerical evidence behind the rulings: the adjudicator's own recomputation of the Kibble normalization, the closing mass and the ψ window, and the externally sourced constants the referee used.

The round's files are `review/round3-preregistration.md`, `review/round3-adjudication.md`, the referee's notes, scripts and outputs in `review/round3/referee/`, and the adjudicator's script and output in `review/round3/adjudicator/`. The manuscript is `notes/knot-dark-matter-standalone.md` (v3, withdrawn; the round's files cite it at its old path in `papers/`).

## Boundaries

- The physics the round tested and killed is in [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate): the [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction), the [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) that survives, the [hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) and the published [topological dark matter](/wiki/dark-matter/candidates/soliton-candidate/prior-art) that the candidate's viable low-mass version reproduces. The general monopole physics, such as [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism), is in [monopoles](/wiki/electric-magnetic-duality/monopoles).
- The theorem the referee re-derived is [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), re-tagged [T] with credit to Freidel–Leigh–Minic after the round.
- The script that now gates the round's corrected numbers is [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script).
- Strict sector separation as a postulate is [P4](/wiki/program/postulates/p4-polarized-matter); the toy Lagrangian the round set as the next task is in [toy models of broken reciprocity](/wiki/symmetry-breaking/toy-models); the referees' shared objection is [the 'framework does no work' critique](/wiki/program/framework-does-no-work).
