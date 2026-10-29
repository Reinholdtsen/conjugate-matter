---
title: "Open: the topological loophole"
weight: 100
status: open
description: "Single topological objects might still localize in momentum; the logical loophole is untested and, since the soliton candidate's retirement, has no candidate; since v2.3 the shared-photon form of P.R.'s magnetic-mirror conjecture needs p-localization again."
sources:
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14 item 8"
  - "papers/broken-born-checkpoint-v2.md §11.4"
  - "review/wiki-build-flags.md item 60"
  - "papers/broken-born-checkpoint-v2.md App. A item 3"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3-adjudication.md 'Decisions'"
  - "HANDOFF.md §2"
  - "notes/broken-born-program-v1.md §7"
  - "verify/soliton_obituary.py"
---

*The topological loophole is the route that [the clumping problem](/wiki/history/main-problems) leaves open for localization in momentum space: not a collective clumping of many particles, which [the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem) rules out as a requirement, but a single object, such as a [topological soliton](/wiki/symmetry-breaking/topological-defects#topological-and-non-topological-solitons-t), whose own structure would localize it in momentum. The clumping problem's calculations cover collective dynamics only, so they do not test this case. The candidate that occupied the loophole, [superheavy solitons of a hidden gauge sector](/wiki/dark-matter/candidates/soliton-candidate), was retired on 2026-10-19 after failing review on its abundance arithmetic, so the loophole is logically open but has no candidate. [The checkpoint](/wiki/history/documents/checkpoint) does not say consistently whether it remains a work item. Since the checkpoint's version 2.3, one form of P.R.'s [magnetic-mirror conjecture](/wiki/electric-magnetic-duality/magnetic-identification#shared-photon) needs localization in momentum again: the form in which magnetically charged partners of our charged particles carry magnetic charge of our own photon.*

**Status:** Open — untested and without a candidate; the sources tag it only through #11 §11.4's quotation of v2.0, "p-local solitons are p-localized" [O]. #11 §12 says it "remains untested, but has no candidate"; #11 §14 item 8 records that "v2.1 closed the soliton-spectrum and p-localization items with the §12 obituary; §11.4's shared-photon form needs p-localization again" (v2.3). The checkpoint does not reconcile the two. Listed among [open problems](/wiki/status/open-problems); it qualifies the death of [velocity clumping](/wiki/dark-matter/momentum-clumping/founding-image).

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
- #11 §14 item 8, on the charge-lattice open problem, reads in v2.3: "8. Charge-lattice polarization: formalize §11.3's unification, and test P.R.'s magnetic-mirror conjecture (§11.4) [O]. (v2.1 closed the soliton-spectrum and p-localization items with the §12 obituary; §11.4's shared-photon form needs p-localization again.)" In v2.1 and v2.2 it ended: "(The soliton-spectrum and p-localization items are closed by the §12 obituary.)"

#11 does not reconcile them. Read together on the v2.1 wording, they said that the logical loophole is untested and that there is no candidate and no work item for it. That reading follows the conflict register's ruling ([conflicts between sources](/wiki/history/documents/source-conflicts)).

v2.3 keeps §12's wording and ties p-localization to the shared-photon form of P.R.'s magnetic-mirror conjecture, in which the momentum-polarized analogs of our electrically charged particles carry magnetic charge of our photon ([shared photon](/wiki/electric-magnetic-duality/magnetic-identification#shared-photon)). #11 §11.4: "Localized in position at dark-matter density, such objects would exceed the Parker bound at #14's benchmark masses (#14 v2 and v3 §4; not gated). Something must therefore hide them, and neither option has been computed: p-localization, open since v2.0 ("p-local solitons are p-localized" [O]), with the spread in the objects' field profile rather than their quantum state, wider than detectors and than the coherence length of galactic magnetic fields, and decoupled from the photon–baryon plasma before recombination (†); or binding into magnetically neutral composites ("heavy and bound", §11.2)." The Parker bound caps the flux of free magnetic charges by the survival of the Galaxy's magnetic field [T] ([monopole flux bounds](/wiki/electric-magnetic-duality/monopoles/monopole-searches)). This page does not decide whether the loophole is still a live question. No current queue item addresses it: the root `CLAUDE.md`'s queue lists [the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison), [the † literature battery](/wiki/method/literature-battery) and an optional round-6 review of [the toy-model note](/wiki/symmetry-breaking/toy-models).

## What remains open

- **Whether any program-native object is localized in momentum by topology.** No candidate exists, and no calculation has been made.
- **p-localization for the shared-photon form.** That form of the magnetic-mirror conjecture needs its analogs hidden, by p-localization, with the spread in the objects' field profile rather than their quantum state, or by binding into magnetically neutral composites; neither option has been computed (#11 §11.4; [what it needs](/wiki/electric-magnetic-duality/magnetic-identification#what-it-needs)).
- **The other dark-sector candidates.** The two remaining candidates, χ particles and [the X-condensate](/wiki/dark-matter/candidates/x-condensate), are not topological objects, and the sources do not connect either one to the loophole.

## History

- **#9.** The first consolidation states the clumping problem's three results without mentioning a loophole (`notes/broken-born-program-v1.md` §7).
- **v2.0 and [the handoff](/wiki/history/documents/handoff).** The soliton candidate was added, and v2.0 also claimed that it slips through the loophole. The handoff, written while the candidate was alive, lists among the dead: "Loophole: *topological* p-localization of individual solitons untouched." (`HANDOFF.md` §2).
- **v2.1, 2026-10-19.** The candidate was retired after round 3, and #11 §12 and App. A took their present wording: untested, no candidate. #11 outranks the handoff, so "untouched" is superseded by "untested, but has no candidate".
- **v2.3, 2026-10-29.** §14 item 8's parenthetical became "v2.1 closed the soliton-spectrum and p-localization items with the §12 obituary; §11.4's shared-photon form needs p-localization again", when #11 recorded P.R.'s magnetic-mirror conjecture on Paul's ruling on flag 60 (`review/wiki-build-flags.md`). §12 and App. A item 3 are unchanged.

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — the candidate's use of the loophole, its retirement and the current wording; §14 item 8 — "closed" in v2.1, and p-localization needed again by §11.4's shared-photon form (v2.3); §11.4 — the shared-photon form, the Parker bound and p-localization "open since v2.0" [O]; App. A item 3 — the loophole in the founding-supposition audit; §9 — the opening passage
- `review/wiki-build-flags.md` item 60 — the ruling behind §11.4
- `CLAUDE.md` 'Since the handoff' — the soliton candidate dead as a program-native proposal; the current queue
- `review/round3-adjudication.md` 'Decisions' — the retirement and the clumping precedent
- `HANDOFF.md` §2 — the earlier "untouched"
- `notes/broken-born-program-v1.md` §7 — the clumping problem without a loophole
- `verify/soliton_obituary.py` — the gated overproduction factor
