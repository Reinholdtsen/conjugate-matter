---
title: "Verification"
weight: 70
status: hub
description: "Rules for checking numbers and the gate that enforces them: the iron rule, independent anchors, the reduced-model and error-bar lessons, and the verify/ scripts run by scripts/check.sh."
bookCollapseSection: true
---

*Verification, in this program, means recomputing the numbers that the documents assert with scripts kept in the repository's `verify/` folder, under the rule that every asserted or disputed number gets executed code, and running those scripts together in one gate, `scripts/check.sh`, which must pass before work counts as finished. Each script prints a pass or a fail for every check, with the measured value where there is one. The rules behind the scripts were learned from specific failures: AI referees made confident arithmetic errors, a script confirmed the arithmetic of a wrong physical input, a stability check covered only a frozen version of a model, and simulation numbers came without error bars. A passing script shows that the arithmetic is right for the model it encodes, not that the model describes nature.*

**Stands:** [the iron rule](/wiki/method/verification/iron-rule), [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model), [independent anchors](/wiki/method/verification/independent-anchors), [the reduced-model stability rule](/wiki/method/verification/reduced-model-stability), [the Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars), [the gate](/wiki/method/verification/the-gate) and the scripts it runs ([the battery](/wiki/method/verification/battery), [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script), [the toy-model scripts](/wiki/method/verification/toy-model-scripts)) — rules and tools in force · **Died:** nothing in this section (the script that checked the withdrawn soliton manuscript was retired; see [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)) · **Open:** nothing in this section

## Map

The rules come first, in the order the program learned them; the gate and the scripts it runs follow. None of these pages states physics: each script page says what it checks and links the topic pages that carry the claims.

- [The iron rule: no arithmetic by eyeball](/wiki/method/verification/iron-rule) is the founding rule: every asserted or disputed number gets executed code with printed output, kept in `verify/`. It came from review rounds 1 and 2, whose AI referees were reliable on structure and unreliable on unaided arithmetic.
- [Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model) is the limit of the iron rule, learned in round 3: the soliton manuscript's numbers were all computed and gated, and one physical input was still wrong.
- [Independent anchors](/wiki/method/verification/independent-anchors) is round 3's repair: a script must first reproduce a textbook identity or a published value, because a check that reproduces the paper's own number is circular.
- [The reduced-model stability rule](/wiki/method/verification/reduced-model-stability) is the first lesson of round 4: a model simplified by freezing fields needs a stability check with all fields free, and the text must say it is a reduction.
- [The Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars) is round 4's second lesson: simulation numbers need error bars from independent runs, because a fixed seed makes a number reproducible, not accurate.
- [The gate: scripts/check.sh](/wiki/method/verification/the-gate) is the definition of done. It runs every script below, then the wiki's own check, and records which claims are gated and which are not.
- [The verification battery T1–T7](/wiki/method/verification/battery) checks the Tier-1 algebra of checkpoint #11: the compatibility theorem, the modular-field parametrization and the algebra of the momentum graviton's potential.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) recomputes every number in the record of the retired soliton candidate, after anchors that are independent of the manuscript.
- [The toy-model scripts](/wiki/method/verification/toy-model-scripts) check the toy-model note: the coset sigma model, the self-dual Grosse–Wulkenhaar model, the lattice Monte Carlo and the matter-locality criterion.

## Boundaries

- What the review rounds found, and the referees' and adjudicators' own scripts, are in [blind review](/wiki/method/review), notably [Review round 3](/wiki/method/review/round-3) and [Review round 4](/wiki/method/review/round-4).
- The claims each script checks are stated on their topic pages, for example [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) and [the toy models](/wiki/symmetry-breaking/toy-models).
- The [V] tag that a machine check earns is defined on [Provenance tags and citation marks](/wiki/method/provenance-tags), and the tier it belongs to on [Claim tiers and selection bias](/wiki/method/claim-tiers).
