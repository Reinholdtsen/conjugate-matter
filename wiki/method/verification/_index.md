---
title: "Verification"
weight: 70
status: hub
description: "Rules for checking numbers and the gate that enforces them: the iron rule, its limit, independent anchors, the reduced-model and error-bar lessons, and the verify/ scripts run by scripts/check.sh."
bookCollapseSection: true
---

*Verification, in this program, means recomputing the numbers that the documents assert with scripts kept in the repository's `verify/` folder, under the rule that every asserted or disputed number gets executed code, and running those scripts together in one gate, `scripts/check.sh`, which must pass before work counts as finished. Each script prints a pass or a fail for every check, with the measured value where there is one. The rules behind the scripts were learned from specific failures: AI referees made confident arithmetic errors, a script confirmed the arithmetic of a wrong physical input, a stability check covered only a frozen version of a model, and simulation numbers came without error bars. A passing script shows that the arithmetic is right for the model it encodes, not that the model describes nature.*

**Method pages only:** this section holds rules and the scripts that apply them, all in force, and makes no physics claims; what stands, what died and what is open is registered in [claims that stand](/wiki/status/alive), [the graveyard](/wiki/status/graveyard) and [open problems and the queue](/wiki/status/open-problems).

## Map

The rules come first, in the order the program learned them, each with the episode that produced it and its applications since, the wiki build's executed checks among them. The gate and the scripts it runs follow. None of these pages states physics: each script page says what it checks, what it does not, and which topic pages carry the claims.

- [The iron rule: no arithmetic by eyeball](/wiki/method/verification/iron-rule) is the founding rule: every asserted or disputed number gets executed code with printed output. It came from review rounds 1 and 2, whose referees, working without code execution, made three confident order-of-magnitude accusations that were all their own unit errors. The page follows the rule into the scripts, the referees' and adjudicators' practice, the drafting of the [soliton manuscript](/wiki/dark-matter/candidates/soliton-candidate/obituary), and the wiki build.
- [Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model) is the iron rule's limit, learned in round 3: every number of the soliton manuscript was computed by a gated script, and its Kibble normalization was still wrong. All four surviving indictments were inputs or model choices, not arithmetic slips.
- [Independent anchors](/wiki/method/verification/independent-anchors) is round 3's repair: a script first tests its formulas on a textbook identity or a published value. The page quotes the circular anchor from the retired script and lists the anchors each current script uses, and why parity checks are not anchors.
- [The reduced-model stability rule](/wiki/method/verification/reduced-model-stability) is round 4's first lesson: the coset toy's first potential had been checked only with H frozen and is unbounded below once H moves, so its vacuum was a saddle. The repair is checked over all fields, the texts name the simulation a reduction, and the zero mode's status is disputed between the sources (flag 12).
- [The Monte Carlo error-bar rule](/wiki/method/verification/monte-carlo-error-bars) is round 4's second lesson: a fixed-seed control value was a short-run fluctuation. The lattice script now averages four independent seeds, and two of its checks are stated in units of the error bar.
- [The gate: scripts/check.sh](/wiki/method/verification/the-gate) is the definition of done: how it runs, what each script gates, what is not gated, how its script list grew from the battery alone to six scripts and the wiki check, and a recorded run.
- [The verification battery T1–T7](/wiki/method/verification/battery) checks the Tier-1 algebra of checkpoint #11, test by test: what is drawn, what is asserted with what tolerance, which claim it gates, and its recorded output.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) recomputes the numbers of the record of the retired soliton candidate after four anchors. Its docstring claims every number of that record; the page states which numbers the script does not check (flag 33 in `review/wiki-build-flags.md`).
- [The toy-model scripts](/wiki/method/verification/toy-model-scripts) check the toy-model note's criteria S1–S5: the coset sigma model, the self-dual Grosse–Wulkenhaar model, the lattice Monte Carlo and matter locality, each with its method, its limits and its recorded output.

## Boundaries

- What the review rounds found, and the referees' and adjudicators' own scripts, are in [blind review](/wiki/method/review), notably [Review round 3](/wiki/method/review/round-3) and [Review round 4](/wiki/method/review/round-4).
- The claims each script checks are stated on their topic pages, for example [the compatibility theorem](/wiki/phase-space/born-geometry/compatibility-theorem), [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) and [the toy models](/wiki/symmetry-breaking/toy-models).
- The [V] tag that a machine check earns is defined on [Provenance tags and citation marks](/wiki/method/provenance-tags), and the tier it belongs to on [Claim tiers and selection bias](/wiki/method/claim-tiers).
- Suspected errors in the source documents found while building this wiki, with their executed checks, are recorded in `review/wiki-build-flags.md` and `review/wiki-build-checks/`, outside the gate; the pages quote the sources faithfully and point to the flags.
