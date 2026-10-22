---
title: "The popular articles (#10, #12)"
weight: 70
status: record
description: "'The Angle of the Mirror', a narrative of the first week, and 'The Universe's Other Half', written as if confirmed: what each says section by section, the claims found only in them, what the record has overtaken, and why neither is a status source."
sources:
  - "popsci/angle-of-the-mirror.md"
  - "popsci/universes-other-half.md"
  - "HANDOFF.md §3"
  - "HANDOFF.md §7"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §3"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §11"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/broken-born-checkpoint-v2.md App. A"
  - "papers/conjugate-special-relativity.md §1"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/wiki-build-flags.md item 6"
---

*The popular articles are two plain-language essays about the program, written on claude.ai for general readers. "The Angle of the Mirror" (#10) is a field report on the first week: the bet that Born's symmetry between position and momentum is exact but hidden, the two founding ideas the calculations killed, and the structure that survived. "The Universe's Other Half" (#12) is a tour of the whole framework written, in its own opening words, "as if it were confirmed. It is not." Neither has been revised since the import into this repository, so both still present the superheavy soliton candidate as alive and read the dark-energy data more favorably than the checkpoint now does, and #12 adds claims that no other document makes. They are kept for their exposition, and neither is ever a source for a claim's status.*

**Status:** Record, never a status source — untagged — rank 7, last, in the wiki's precedence order (`wiki/CLAUDE.md`); both files are unchanged since their import on 2026-10-19 (commit 8d588f6; moved to `popsci/` in 008c3ee).

## What the articles are

[The handoff](/wiki/history/documents/handoff) lists them among the artifacts: #10, "final (journey article)", is "Pop-sci #1: narrative of the program including the deaths", with a register note that Paul is to be called an independent developer and not retired; #12, "final (destination article)", is "Pop-sci #2: the framework presented as if confirmed; wave/spectrum analogy spine; includes magnetic identification, transparency argument, magnetic-quark/dual-superconductor section, dual SR, equivalence-principle unification. Register: serious-scientist plain language (see §7)" (`HANDOFF.md` §3). SR is special relativity. In the handoff's creation order #10 comes after the program v1.0 (#9) and #12 after checkpoint #11 v2.0. Both describe the dark-matter question as three-way, with topological knots as the third option, as #11 v2.0 did.

The articles carry no provenance tags and no references, and they are undated. Their register is the one `HANDOFF.md` §7 asks for in science writing, "serious scientist explaining abstract material in plain language", and #12's opening, the waveform and its spectrum, is the wave/Fourier analogy the program uses throughout.

## Why neither is a status source

The wiki's precedence order places the popular articles last and adds: "#12 presents the framework as if it were confirmed. It is never a source for a claim's status" (`wiki/CLAUDE.md`). #12 says the same of itself: "What follows presents the broken-Born framework as if it were confirmed. It is not. It is a speculative proposal awaiting expert review and observational tests, and it ends with the measurements that could refute it." #10 calls itself "unreviewed, unpublished, and wrong in whatever places expert scrutiny will eventually find."

Two further reasons follow from the dates. Both articles predate #11 v2.1, so they do not know of the soliton candidate's retirement or of the phantom crossing in the second data release of the Dark Energy Spectroscopic Instrument (DESI). And #12 goes beyond the technical record in several places, listed below. A claim found only in the articles is recorded as popsci-only, at conjecture tier or dead, on [chat-only and popsci-only conjectures](/wiki/status/conjectures).

## #10, "The Angle of the Mirror"

Subtitle: "What happened when an engineer's hunch and an AI's mathematics spent a week stress-testing an 88-year-old symmetry — and killed their own favorite idea". The article is the only narrative of the program's first week. It describes the staffing: "the intuition came from an independent developer with a physics-lab past, the derivations from an AI, and the referee's whistle from mathematics itself" ([the collaboration](/wiki/method/collaboration)).

- **Opening.** Born's 1938 observation, ending "the question spent eighty-eight years in a drawer" ([Born's question](/wiki/program/borns-question)). #11 v2.2 credits Freidel, Leigh and Minic with the idea that a preferred polarization breaks Born duality, so the question had not lain untouched ([broken Born duality](/wiki/phase-space/reciprocity/broken-born-duality)).
- **"The wager".** Born's symmetry is exact and "the universe is the magnet"; the hiding is mandatory because nothing is sharp in position and momentum at once; and conjugate matter, "polarized toward momentum the way we are polarized toward space", was first imagined "clumping not in space but in *speed*" ([the hard core](/wiki/program/hard-core); [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking)).
- **"The killing fields".** The founding image died: the collective pull "falls short of what flocking requires by a factor of ten to the thirtieth", and on the wave side the tiniest galaxies "should have converted their dark matter into escaping radiation", whereas "little Segue 1 has held its darkness for thirteen billion years" ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)). An earlier casualty, "that the conjugate universe's gravitational collapse is what powers our accelerating expansion", failed too ([Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)). "This one lost its two favorites in the first week". #11's audit records the second death as "dead twice (w = −2 falsified; corrected dictionary removed the mechanism)" (Appendix A item 9).
- **"What refused to die".** The partner of the metric is "*another graviton*", two interacting massless gravities are inconsistent, and the partner becomes massive when the vacuum picks its polarization ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain); [the symplectic partner of the graviton](/wiki/gravity/momentum-graviton/symplectic-partner)). The article's "forty-year asymmetry in theoretical physics" appears in no other document ([popsci-only](/wiki/gravity/momentum-graviton/symplectic-partner#popsci-only-a-forty-year-asymmetry)). Then the palindrome makes the partner's vacuum energy cancel, "Zero, by symmetry rather than by the fine-tuning such theories normally require", with the footnote that partially massless gravity sits in the same family and novelty "awaits a careful comparison" ([the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity); [Open: the partially-massless comparison](/wiki/gravity/palindromic-branch/pm-comparison)). The phrase "by symmetry rather than by the fine-tuning" is queried in `review/wiki-build-flags.md` item 6.
- **"The referee is already on the field".** Dark energy as "the orientation of the universe's broken symmetry, the angle of the mirror", with the slogan "dark matter is the mirror-world's stuff; dark energy is the angle of the mirror". The three outcomes of the next data release are "Three doors": "Constant kills the theory's heart. Phantom kills it outright. Continued weakening keeps it alive" ([τ: hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence); [row 4](/wiki/predictions/dark-energy-drift)). DESI is described as "having spent two years reporting tantalizing hints of exactly the required weakening".
- **"Dividends and daydreams".** The momentum-space speed limit is a force, "c⁴/G, about 10⁴⁴ newtons" ([the maximum force](/wiki/conjugate-relativity/maximum-force)); dark matter's identity "has narrowed to a three-way question", the third option being "topological knots"; and a paragraph of "licensed daydreaming" about observers made of conjugate matter ([the other observers, popsci-only](/wiki/program/conjugate-universe#popsci-only-the-other-observers)).
- **"The method is the message".** "Every load-bearing equation in this program has been verified by machine, independently of the AI that first derived it — seven checks, seven passes", followed by "What no machine can verify is whether correct algebra is attached to the right physics", and data "already executed two of the founding ideas".

## #12, "The Universe's Other Half"

Subtitle: "One broken symmetry as the common origin of dark matter, dark energy, and the fate of the cosmos". The article is built on one analogy, set out in its first section: a sound can be described as a waveform or as a spectrum, the two are related by the Fourier transform, and quantum mechanics says the same of position and momentum.

- **"Two descriptions of one thing".** The waveform and the spectrum, and Born's question ([the Fourier transform as a phase-space rotation](/wiki/phase-space/reciprocity/fourier-transform); [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity)).
- **"An asymmetry that cannot be avoided".** The uncertainty principle forces a choice, and the vacuum is "the frozen state", like a crystal that has settled on axes ([spontaneous symmetry breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking); [mandatory breaking](/wiki/symmetry-breaking/mandatory-breaking)).
- **"The second geometry, and why it has never been seen".** The counterpart of the metric is "in effect a second copy of gravity", two interacting massless gravities are inconsistent by "a theorem of field theory, proved in 2000", and the second field becomes massive "like the Higgs mechanism"; the graviton "remains exactly massless, in agreement with gravitational-wave observations" ([the multi-graviton no-go theorem](/wiki/gravity/spin-2-fields/multi-graviton-no-go); [row 6](/wiki/predictions/massless-graviton)). The cancellation of the field's vacuum energy is set against estimates that "exceed the measured value by some hundred and twenty orders of magnitude", and its novelty is called "an unresolved question" ([the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem)).
- **"Dark matter as the other polarization".** Momentum-polarized matter gravitates like ordinary matter and self-interacts only at nearly equal velocities, with a knee whose sharpness tells particles from waves ([the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles); [the velocity gate](/wiki/dark-matter/conjugate-matter/velocity-gate); [row 3](/wiki/predictions/island-discriminant)). The three candidates follow, the third being topological solitons that "cannot decay for the same reason a knot cannot untie". The section then adds what #12 alone claims: that "The momentum-polarized sector is the magnetic side of electromagnetism", with a magnetic coupling "about 34, against our 1/137"; that the momentum polarization carries "the entire magnetic mirror-family"; and the transparency argument, "Uniform media do not scatter light; they refract it", with the solitons "around 10¹⁶ times the proton's" in mass and the residual effects on light "some forty orders of magnitude below the sharpest astronomical measurements" ([Obituary: the magnetic identification](/wiki/electric-magnetic-duality/magnetic-identification); [the transparency argument](/wiki/electric-magnetic-duality/magnetic-identification#the-transparency-argument); [the magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family); [the dual superconductor](/wiki/electric-magnetic-duality/dual-superconductor#popsci-only-inside-every-proton)). It concludes that three requirements "select the same corner of the three-way question", the knots ([popsci-only](/wiki/dark-matter/candidates/soliton-candidate/obituary#popsci-only-the-favoured-corner-of-the-three-way-question)).
- **"Dark energy as the orientation of the split".** Dark energy as the energy of the orientation's displacement: "Decreasing is required; phantom is impossible; constant is impossible." The framework "survives only the first outcome" of the coming data, a continued weakening ([popsci-only: constant is impossible](/wiki/predictions/dark-energy-drift#popsci-only-constant-is-impossible)). The turnaround is "one event with two readings" ([the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)).
- **"A second speed of light".** c⁴/G, "roughly 10⁴⁴ newtons", as a maximum force; force composition and force dilation, with corrections "of order 10⁻⁶⁵" for a kilogram at a neutron star's surface; the invariant length and the Planck closure; and "his two relativity principles are one principle, read in the two descriptions" ([conjugate special relativity](/wiki/conjugate-relativity); [force dilation, popsci-only statement](/wiki/conjugate-relativity/force-dilation#popsci-only-the-unqualified-popular-statement); [the equivalence principle as dual relativity](/wiki/conjugate-relativity/equivalence-principle)). The mirror object, a trap in momentum, would be "indistinguishable, to our instruments, from compact dark matter" ([popsci-only](/wiki/conjugate-relativity/momentum-space-black-holes#popsci-only-the-mirror-object-as-compact-dark-matter)).
- **"The other observers".** "Each polarization is the other's dark sector" ([popsci-only](/wiki/program/conjugate-universe#popsci-only-the-other-observers)).
- **"What one assumption purchases".** "The framework rests on a single assumption", followed by a list of what it buys; the record rests on postulates P1–P5 ([popsci-only: "a single assumption"](/wiki/program/hard-core#popsci-only-a-single-assumption)). The list, item by item, is set against the record below.

## What the record has overtaken

- **The soliton candidate.** Both articles present the knots as live, and #12 as the favored corner. The candidate was retired on 2026-10-19 (#11 §12; root `CLAUDE.md`; [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).
- **The reading of DESI.** #10's "exactly the required weakening" and #12's "the required behavior" are superseded by DESI Data Release 2's phantom crossing above z ≈ 0.4, which puts the sector "under real pressure" (root `CLAUDE.md`; [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).
- **What the machine verified.** #10's "Every load-bearing equation in this program has been verified by machine" goes beyond #11 §2, where the battery covers the explicit algebra of Tier 1 and "a verification script confirms arithmetic, not the model it encodes" ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).
- **The kill conditions.** #12's "constant is impossible", and its statement that the framework "survives only the first outcome", go beyond #11 row 4, where a robust constant w = −1 kills only the τ sector. #10's "Constant kills the theory's heart" agrees with #11.
- **The magnetic identification.** #12's claim conflicts with the dead "α_d ≈ 34 via Dirac quantization against our photon" (`HANDOFF.md` §2), with strict sector separation under P4, and with #11's row 7. The 34 itself depends on a convention by a factor of 4: "1/(4α) = 34.26 (eg = 2πn) vs 1/α = 137.04 (eg = 4πn)" (`review/v3-worklog.md`, R2 [V]). It is treated as dead.
- **"Eighty-eight years in a drawer".** Superseded in its implication by #11 §3's credit to Freidel, Leigh and Minic.
- **"Proved in 2000".** #11 cites the no-go theorem as a 2001 journal paper with a 2000 preprint number; the years refer to the same work.

These cases are also listed on [conflicts between sources](/wiki/history/documents/source-conflicts).

## "What one assumption purchases", against the record

| #12's item | The record |
| --- | --- |
| "The primacy of space over momentum: a property of the frozen vacuum" | [the hard core](/wiki/program/hard-core), qualified in v2.2: the polarization is [a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle) and needs a ρ-preserving potential |
| "The century-long invisibility of the symmetry: the mass of the second gravitational field" | [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain) |
| "The quietness of empty space, at least as concerns that field: the palindromic cancellation" | [the vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity), novelty awaiting comparison |
| "Dark matter: the other polarization of matter" with a measurable knee | [the χ-particle candidate](/wiki/dark-matter/candidates/chi-particles), one of two candidates |
| "Dark energy: the vacuum orientation's displacement, obligated to decrease" | [τ as hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence) and [the no-phantom bound](/wiki/cosmology/dark-energy/no-phantom-bound), under pressure from the data |
| "A candidate origin for the conjectured maximum force" | #13, where the value c̃ = c⁴/G carries no tag (§7 lists it among the "Numerical anchors") and "The factor of 4 is not fixed here [O]" ([the maximum force](/wiki/conjugate-relativity/maximum-force)) |
| "A candidate identity for dark matter's charge: the magnetic half of electromagnetism's own duality" | popsci-only and dead ([obituary](/wiki/electric-magnetic-duality/magnetic-identification)) |
| "a revised ending for the universe" | [the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce), a long-horizon prediction whose premise, a negative V(τ), is unresolved |

## What the wiki takes from them

The articles are sources for their own wording and for the exposition the program found to work. The waveform and spectrum of #12's opening are the analogy the wiki's voice rules recommend, since the Fourier transform implements ρ. #10 is the only account of the order in which the first week's ideas died. Where an article states a result, the wiki cites the technical document that derives it, and where only an article states it, the wiki labels the claim popsci-only and takes its status from the record.

## Sources

- `wiki/CLAUDE.md` 'The wiki is derivative' — the articles' rank, last, and #12 "never a source for a claim's status"
- `popsci/angle-of-the-mirror.md` — #10, cited by section heading
- `popsci/universes-other-half.md` — #12, cited by section heading
- `HANDOFF.md` §3 rows 10 and 12 — the articles' standing and #12's contents; §7 — the register for science writing; §2 — the dead α_d ≈ 34
- `papers/broken-born-checkpoint-v2.md` §2 — what the battery checks; §3 — the Freidel–Leigh–Minic credit; §4 — P4 strict; §10 — the pressure from DR2; §12 — the soliton obituary; §13 row 4 — the constant-w kill condition; App. A item 9 — the second death
- `papers/conjugate-special-relativity.md` §1 — the factor of 4 [O]
- `review/v3-worklog.md` 'Round-2 pending list', R2 — the convention behind "34"
- `review/wiki-build-flags.md` item 6 — "by symmetry rather than tuning"
