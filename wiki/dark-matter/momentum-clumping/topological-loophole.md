---
title: "Open: the topological loophole"
weight: 100
status: open
description: "Single topological objects might still localize in momentum; the logical loophole is untested and, since the soliton candidate's retirement, has no candidate."
sources:
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14 item 8"
  - "papers/broken-born-checkpoint-v2.md App. A item 3"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions'"
  - "HANDOFF.md §2"
  - "notes/broken-born-program-v1.md §7"
  - "verify/soliton_obituary.py"
---

*The topological loophole is the route that [the clumping problem](/wiki/history/main-problems) leaves open for localization in momentum space: not a collective clumping of many particles, which [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem) rules out as a requirement, but a single object, such as a [topological soliton](/wiki/symmetry-breaking/topological-defects#topological-and-non-topological-solitons-t), whose own structure would localize it in momentum. The clumping problem's calculations cover collective dynamics only, so they do not test this case. The candidate that occupied the loophole, [superheavy solitons of a hidden gauge sector](/wiki/dark-matter/candidates/soliton-candidate), was retired on 2026-10-19 after failing review on its abundance arithmetic, so the loophole is logically open but has no candidate. [The checkpoint](/wiki/history/documents/checkpoint) does not say consistently whether it remains a work item.*

**Status:** Open — untested, without a candidate, and with no tag in the sources. #11 §12 says it "remains untested, but has no candidate"; #11 §14 item 8 says the "p-localization items are closed by the §12 obituary". The checkpoint does not reconcile the two. Listed among [open problems](/wiki/status/open-problems); it qualifies the death of [velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image).

## The statement

#11 App. A audits P.R.'s [founding suppositions](/wiki/program/founding-suppositions). Item 3, "Matter clumps in momentum space", is "**dead as dynamics** (§9); **loophole**: topological p-localization of individual solitons untested, and its candidate is retired (§12)".

The current wording, in #11 §12's list of what survives the soliton obituary: "The clumping loophole — topological momentum-space localization of individual objects — remains untested, but has no candidate."

"p-localization" means localization in momentum p: an object whose momentum-space profile is narrow, as an ordinary particle's position-space profile is narrow.

## Why the clumping problem leaves it open

The clumping problem asked whether many dark-matter particles, or a dark-matter wave field, would gather collectively into narrow ranges of velocity. Its three calculations are a mean-field stability analysis for classical particles ([the mean-field criterion](/wiki/dark-matter/momentum-clumping/instability-criterion)) and a wave-kinetic [condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate) with its endpoints ([the wave island](/wiki/dark-matter/momentum-clumping/wave-island)). Each treats the dark matter as a gas or a field whose structure comes from the interactions among its parts. [The net theorem](/wiki/dark-matter/momentum-clumping/net-theorem) is correspondingly a statement about collective dynamics.

A topological soliton is a different kind of object. It is a localized configuration of a field that cannot decay to the vacuum, because it carries a conserved topological charge, an integer that no continuous change of the field can alter [T]. Its shape is set by its own field equations, not by an instability of a surrounding gas. If such an object lived in a sector polarized toward momentum, its localization would be in momentum. The v2.0 candidate's claim was of this kind: its solitons "slip through the clumping loophole (§9), since topology, not collective dynamics, would localize them in momentum" (#11 §12). Nothing in the clumping problem addresses that case. #11 §9's opening passage records the outcome of the clumping problem as leaving "one loophole for individual knots, whose candidate has since been retired (§12)".

## The candidate that occupied it

In version 2.0 of the checkpoint, the program listed three [dark-sector candidates](/wiki/dark-matter/candidates): [χ particles](/wiki/dark-matter/candidates/chi-particles), a condensate of the [momentum graviton](/wiki/gravity/momentum-graviton), and "topological solitons of a p-local gauge sector (§11) as a third candidate, stable by topological charge" (#11 §12). The candidate was developed into a standalone proposal: superheavy ['t Hooft–Polyakov monopoles](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole) of a hidden SU(2) → U(1) sector ([the hidden sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)).

Its abundance followed from the [Kibble estimate](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) of how many defects a cosmological phase transition leaves. [The round-3 blind review](/wiki/method/review/round-3) recomputed it with code: [the normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) had been set too low, at minimum production the v3 benchmark is [overproduced](/wiki/dark-matter/candidates/soliton-candidate/overproduction) by 2.1×10³–1.2×10⁴ [V] (gated in `verify/soliton_obituary.py`; [the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)), and viable abundances need either lower masses, where the scenario is prior art, or a free [dilution factor](/wiki/cosmology/early-universe/relic-yield-and-dilution#entropy-dilution-t) that removes the mass prediction (#11 §12; [the soliton obituary](/wiki/dark-matter/candidates/soliton-candidate/obituary)). Verdict: "Retired as a program-native candidate." The root `CLAUDE.md` records the consequence: "The superheavy soliton candidate in HANDOFF §2 is **dead** as a program-native proposal. The framework is merely compatible with known PeV-scale topological dark matter (prior art)." ([prior art](/wiki/dark-matter/candidates/soliton-candidate/prior-art)). The round-3 adjudication cited the clumping obituary as a precedent for the retirement (`review/round3-adjudication.md`, 'Decisions').

The retirement removed the loophole's only occupant. It did not test the loophole: the soliton failed on its abundance, not on whether topology localizes it in momentum.

## Unresolved: open or closed

The checkpoint describes the loophole in two ways:

- #11 §12: "The clumping loophole — topological momentum-space localization of individual objects — remains untested, but has no candidate."
- #11 §14 item 8, on the charge-lattice open problem, ends: "(The soliton-spectrum and p-localization items are closed by the §12 obituary.)"

#11 does not reconcile them. Read together, they say that the logical loophole is untested and that there is no candidate and no work item for it. That reading follows the conflict register's ruling ([conflicts between sources](/wiki/history/documents/source-conflicts)); this page does not decide whether the loophole is still a live question. No current queue item addresses it: the root `CLAUDE.md`'s queue lists [the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison), [the † literature battery](/wiki/method/literature-battery) and an optional round-6 review of [the toy-model note](/wiki/symmetry-breaking/toy-models).

## What remains open

- **Whether any program-native object is localized in momentum by topology.** No candidate exists, and no calculation has been made.
- **The other dark-sector candidates.** The two remaining candidates, χ particles and [the X-condensate](/wiki/dark-matter/candidates/x-condensate), are not topological objects, and the sources do not connect either one to the loophole.

## History

- **#9.** The first consolidation states the clumping problem's three results without mentioning a loophole (`notes/broken-born-program-v1.md` §7).
- **v2.0 and [the handoff](/wiki/history/documents/handoff).** The soliton candidate was added, and v2.0 also claimed that it slips through the loophole. The handoff, written while the candidate was alive, lists among the dead: "Loophole: *topological* p-localization of individual solitons untouched." (`HANDOFF.md` §2).
- **v2.1, 2026-10-19.** The candidate was retired after round 3, and #11 §12 and App. A took their present wording: untested, no candidate. #11 outranks the handoff, so "untouched" is superseded by "untested, but has no candidate".

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — the candidate's use of the loophole, its retirement and the current wording; §14 item 8 — "closed by the §12 obituary"; App. A item 3 — the loophole in the founding-supposition audit; §9 — the opening passage
- `CLAUDE.md` 'Since the handoff' — the soliton candidate dead as a program-native proposal; the current queue
- `review/round3-adjudication.md` 'Decisions' — the retirement and the clumping precedent
- `HANDOFF.md` §2 — the earlier "untouched"
- `notes/broken-born-program-v1.md` §7 — the clumping problem without a loophole
- `verify/soliton_obituary.py` — the gated overproduction factor
