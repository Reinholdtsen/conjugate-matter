---
title: "Conjectures: chat-only and popsci-only claims"
weight: 40
status: record
description: "The results that exist only in the old chat (HANDOFF §4), the claims found only in the popular articles, and the conjecture-tier statements inside the record, each linked to the page or section that holds it, with its relation to the record; the first chat-only item, the phase-space diameter relation, is now written up, and its square at the bounce is dead."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/phase-space-diameter.md §2"
  - "papers/phase-space-diameter.md §3"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §6"
  - "papers/phase-space-diameter.md §9"
  - "review/round5-adjudication.md 'Verdict'"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
  - "verify/phase_space_diameter.py"
  - "HANDOFF.md §4"
  - "HANDOFF.md §6"
  - "HANDOFF.md §8"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Decisions'"
  - "papers/broken-born-checkpoint-v2.md §2"
  - "papers/broken-born-checkpoint-v2.md §11.3"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13"
  - "papers/conjugate-special-relativity.md §3"
  - "papers/conjugate-special-relativity.md §5"
  - "papers/conjugate-special-relativity.md §6"
  - "notes/debt1a-geometric-core.md §A"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/toy-lagrangian.md 'Chunk 2 results (2026-10-19): the Grosse–Wulkenhaar route'"
  - "notes/toy-lagrangian.md 'Chunk 3 results (2026-10-19): S4, quantum stability'"
  - "popsci/universes-other-half.md"
  - "popsci/angle-of-the-mirror.md"
  - "review/wiki-build-flags.md items 23, 24, 29"
---

*This register collects the claims that are not part of the program's derived record. Some exist only in the original claude.ai conversation and are known from a list in [the handoff document](/wiki/history/documents/handoff); some appear only in the two [popular articles](/wiki/history/documents/popular-articles); and a few sit inside the record but are called conjectures by their own sources. No document in the repository derives them and no script checks them, so they are kept apart from the program's results. The exception is the first chat-only item, the phase-space diameter relation, which a note of 2026-10-26 derived and checked; it stays on the list with the statuses that note gives its parts. The popular article "The Universe's Other Half" presents the framework as if it were confirmed and never decides a claim's status. Each line says where the claim is recorded and how it stands against the record.*

**Status:** Record, a register current to 2026-10-26 — no provenance tags on the claims: `HANDOFF.md` §4 calls two of its items conjecture-tier, #13 §5 calls the dual second law "conjecture-tier", the toy-model worklog calls its [thawing](/wiki/cosmology/dark-energy/thawing-and-freezing) remark "a claim about the program, not verified here", and the popular articles tag nothing; the parts of the diameter relation now carry the tags of the note that wrote it up — no derivation or script in the repository supports these claims, except the diameter relation, now derived in `papers/phase-space-diameter.md` and gated in `verify/phase_space_diameter.py`; the chat-only list is `HANDOFF.md` §4, and the popsci-only claims are found only in `popsci/`.

A claim with a page of its own carries "(chat-only)" or "(popsci-only)" in its title. A smaller claim recorded on a page about another subject sits under a heading "Chat-only: …", "Popsci-only: …" or "Conjecture: …", and the register links that heading. Three claims, or parts of claims, have obituaries of their own and are also listed in [the graveyard](/wiki/status/graveyard): the √N topological floor, the diameter relation's square at the bounce, and the magnetic identification.

## Chat-only results (`HANDOFF.md` §4)

`HANDOFF.md` §4 is headed "Results that exist only in the chat (not in any artifact)", with "only" in capitals in the original. It lists six items, given here in its order. Items 3 and 4 share a page, [Two gravitational charges and the conjugate field equations (chat-only)](/wiki/gravity/momentum-graviton/chat-only-results), which sets each part beside what the documents contain. Item 1, the phase-space diameter relation, is no longer chat-only: the phase-space-diameter note (`papers/phase-space-diameter.md`, version 1.1 of 2026-10-26, graded B by both referees of [review round 5](/wiki/method/review/round-5)) derived and checked it, and each of its parts now has the status the note gives it; one part is dead. None of the six items is on the current work queue ([open problems and the queue](/wiki/status/open-problems#the-work-queue)).

1. **The phase-space diameter relation.** [The phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), with the bullet itself under [Chat-only: the original statement](/wiki/cosmology/scale-factor-duality/phase-space-diameter#chat-only-the-original-statement) — the handoff's bullet makes four claims: the diameter of the universe in position space times its diameter in momentum space equals h · N^(1/3) per dimension, a "cosmic time–bandwidth theorem"; N is "the universe's photon count/entropy (~10⁹⁰, i.e. ~10³⁰ h per dimension)"; the rectangle is "square (D_x = D_p in Planck units) exactly at the bounce"; and its "aspect ratio today ~10⁹²" is "a clock measuring distance from self-duality". The handoff called it "Conjecture-tier; candidate for a future note". The note finds that the bullet defines none of its terms and that its numbers fit one reading, the radiation of today's observable universe (§2). Status: written up; three of the four parts stand as the note corrects them, and one is dead.
   - **The product: alive, as standard physics.** For blackbody radiation filling a sphere, D_x·D_p = κ h N_γ^{1/3} with κ = 1.708, an identity of blackbody statistics [D][V], constant for a fixed comoving region of the radiation [T] (note §3). It holds in standard cosmology with or without reciprocity, so it cannot test the program, and the program's [constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) fixes the area of one phase-space cell, not the number of cells [D].
   - **The constant: corrected.** The chat's ~10⁹⁰ is the radiation entropy, S = 1.01×10⁹⁰ k_B, beside a photon count N_γ = 1.43×10⁸⁹ [V]. It is not the entropy of the universe, which black holes and the cosmic event horizon dominate [T][S] (note §3, §9).
   - **The square: dead.** [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce). In the reading the chat's numbers fit, the rectangle is square only at about 10¹⁴ times the Planck temperature, before the radiation existed, and at the program's [turnaround](/wiki/cosmology/scale-factor-duality/conjugate-bounce) it is at its most elongated; no reading makes it square at a bounce, and the note withdraws the claim [D][V] (§1, §6). Flag 24 in `review/wiki-build-flags.md` asks which bounce was meant; it still awaits Paul's ruling, and the round-5 adjudication recommends accepting it. The note's inference about the claim's origin, tagged [D, inference], is the record's identification of a·ã = 1 with the circle |Z| = 1 (flag 23), which the measured aspect ratio excludes.
   - **The clock: alive, as a reparametrization.** In Planck units the aspect ratio is 5.2×10⁹² today and grows as a²; its logarithm, 213.5 per axis, is the distance on the Siegel half-plane from the self-dual point Z = i [D][V] ([Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states)). In the note's words, "It reparametrizes ln a and adds no dynamics" (§5). Read as one perturbation mode's squeezing, an aspect ratio of 10⁹² is a squeezing of r = 105.9, inside the literature's 100–120 for today's largest scales, but that mode was round before it left the Hubble radius, not at a bounce ([squeezed cosmological perturbations](/wiki/cosmology/early-universe/squeezed-perturbations); note §6).
2. **The √N topological floor.** [Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) — the argument that the Kibble mechanism leaves a net topological charge that annihilation cannot remove, which would bound the soliton candidate's relic abundance between a "Kibble ceiling" and a √N floor. Status: dead. Round-3 ruling 3 showed that Kibble's count is a minimum, not a ceiling, and Decision 3 dropped the planned calculation: "Its premise, Kibble as a ceiling, is inverted (ruling 3)", and "Under decision 2 it has no candidate left to serve."
3. **Two gravitational charges.** [Two gravitational charges](/wiki/gravity/momentum-graviton/chat-only-results#two-gravitational-charges) — ordinary stress-energy is the source of the massless graviton, and dual stress, "how energy is structured across momentum", is the source of the [momentum graviton X](/wiki/gravity/momentum-graviton); the two are "independent numbers", the [equivalence principle](/wiki/gravity/spin-2-fields/equivalence-principle) is "intact", and whether the invariant length λ and the dual charge lock together is left as a "dual equivalence principle" question. Status: conjecture. The coupling of conjugate matter to X through its dual stress is documented (calc note #5 §E; calc note #8 §4); the independence of the two charges and the dual equivalence principle are not.
   - [Chat-only: dual stress as a second gravitational charge](/wiki/dark-matter/conjugate-matter/dual-stress#chat-only-dual-stress-as-a-second-gravitational-charge) — the same claim, recorded on the page of [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress).
4. **The field equations compared with general relativity.** [The field equations compared with general relativity](/wiki/gravity/momentum-graviton/chat-only-results#the-field-equations-compared-with-general-relativity) — three claims, each recorded on the page it bears on. Status: conjecture.
   - [Chat-only: the slaved layer is algebraic](/wiki/phase-space/born-geometry/compatibility-corollaries#chat-only-the-slaved-layer-is-algebraic) — the momentum metric g̃ = g⁻¹ has no field equation of its own, so "Einstein's equation does double duty". The slaving itself is documented (calc note #5 §A; #11 §5); the comparison is not.
   - [Chat-only: the gate as a dual Newtonian limit](/wiki/dark-matter/conjugate-matter/gate-mechanism#chat-only-the-gate-as-a-dual-newtonian-limit) — "dual Newtonian limit = Yukawa in momentum = the gate". No document derives a [Yukawa form in momentum](/wiki/gravity/spin-2-fields/yukawa-forces#conjugate-special-relativity-a-range-in-momentum); #13 cites #11 §7 for the momentum reading, which #11 §7 does not contain (flag 29 in `review/wiki-build-flags.md`).
   - [Chat-only: massive X waves](/wiki/phase-space/modular-field/field-content#chat-only-massive-x-waves) — "X-waves massive, 5 polarizations, frequency floor". The massive spin-2 nature and the five polarizations are in calc note #6; the frequency floor is in no document.
5. **Momentum-space black holes.** [Momentum-space black holes (chat-only)](/wiki/conjugate-relativity/momentum-space-black-holes) — "velocity traps"; a black hole's horizon, read in the momentum description, is a maximum-force surface, since "hovering at horizon requires F → c⁴/G"; and "dual Hawking quanta are position-space-huge". "Conjecture tier; partially in #12". Status: conjecture. #12's addition is listed with the popsci-only claims below.
6. **The full adjudications of review rounds 1 and 2.** "Full adjudications of review rounds 1–2 with executed arbitration code (summarized in §6)". They are not in the repository; only the handoff's summary of the verdicts and rulings survives ([what survives of the record](/wiki/method/review/rounds-one-and-two#what-survives-of-the-record)). This is a missing record, not a claim.

## Popsci-only claims (#10, #12)

The popular articles are "The Angle of the Mirror" (#10) and "The Universe's Other Half" (#12), described on [the popular articles (#10, #12)](/wiki/history/documents/popular-articles). Neither has been revised since its import into the repository, and #12 opens: "What follows presents the broken-Born framework as if it were confirmed. It is not." Each claim below is found, in the form given, only in the articles; the status given is the one the record gives the subject.

### The research program

- [Popsci-only: the other observers](/wiki/program/conjugate-universe#popsci-only-the-other-observers) — if the momentum-polarized sector includes complex structures, "a possibility the framework permits but does not require", observers there would perceive the world through momentum: "Their sky would be a map of velocities", and "Each polarization is the other's dark sector" (#12). #10 calls its version "licensed daydreaming". Neither #11 nor #13 states or analyses the idea; it is speculation with no status in the record.
- [Popsci-only: "a single assumption"](/wiki/program/hard-core#popsci-only-a-single-assumption) — #12: "The framework rests on a single assumption — the position–momentum symmetry is exact and spontaneously broken". #11 formalizes [the hard core](/wiki/program/hard-core) as five postulates and, since v2.2, adds that a definite polarization needs a ρ-preserving potential. #12's closing list of what the assumption buys is set item by item against the record on [the popular articles](/wiki/history/documents/popular-articles#what-one-assumption-purchases-against-the-record).
- The machine-verification claim — #10: "Every load-bearing equation in this program has been verified by machine, independently of the AI that first derived it — seven checks, seven passes". In #11 §2 the battery covers the explicit algebra of Tier 1, and "a verification script confirms arithmetic, not the model it encodes" ([what the record has overtaken](/wiki/history/documents/popular-articles#what-the-record-has-overtaken); [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

### Gravity

- [Popsci-only: a forty-year asymmetry](/wiki/gravity/momentum-graviton/symplectic-partner#popsci-only-a-forty-year-asymmetry) — #10 says that the graviton's symplectic partner being another graviton "explains a forty-year asymmetry in theoretical physics", between string theory's doubled geometry and Born's. No technical document dates the asymmetry; #11 §7 says only that "the symplectic version stalled since Born".

### Dark matter

- [Popsci-only: the favoured corner of the three-way question](/wiki/dark-matter/candidates/soliton-candidate/obituary#popsci-only-the-favoured-corner-of-the-three-way-question) — #12: "Three independent requirements — thirteen-billion-year stability, the strong coupling Dirac's condition demands, and transparency to light — select the same corner of the three-way question", the corner of the topological knots; #10 also presents the knots as a live option. The candidate was retired on 2026-10-19 (#11 §12; round-3 Decision 2) and is recorded as dead in [the graveyard](/wiki/status/graveyard).

### Electric–magnetic duality

- [Obituary: the magnetic identification (popsci-only)](/wiki/electric-magnetic-duality/magnetic-identification) — #12: "The momentum-polarized sector is the magnetic side of electromagnetism", dark because Dirac's condition makes its coupling strong, "about 34, against our 1/137". Status: dead. It was never a program claim, and it conflicts with the dead fixing of α_d ≈ 34 by Dirac quantization against our photon, with strict P4 and with prediction row 7. Two further passages of #12 belong to it:
  - [the transparency argument](/wiki/electric-magnetic-duality/magnetic-identification#the-transparency-argument) — "Uniform media do not scatter light; they refract it", so that a magnetically charged dark sector would leave effects "some forty orders of magnitude below the sharpest astronomical measurements"; the argument assumes the dead premise, uses the retired candidate's mass, and no script checks it;
  - [the popular article's extension](/wiki/electric-magnetic-duality/magnetic-mirror-family#the-popular-articles-extension) of [the magnetic mirror-family](/wiki/electric-magnetic-duality/magnetic-mirror-family) — "the momentum polarization carries the entire magnetic mirror-family"; no program document makes the claim.
- [Popsci-only: "inside every proton"](/wiki/electric-magnetic-duality/dual-superconductor#popsci-only-inside-every-proton) — #12, from [the dual-superconductor](/wiki/electric-magnetic-duality/dual-superconductor) picture of confinement: "If that picture is correct, magnetic analogs of quarks are not hypothetical inhabitants of a hidden sector; their condensed form is at work inside every proton." The sentence is conditional, and the passage goes on to place the magnetic family's free spectrum in the momentum-polarized sector, which is the dead identification above.

### Conjugate special relativity

- [Popsci-only: the unqualified popular statement](/wiki/conjugate-relativity/force-dilation#popsci-only-the-unqualified-popular-statement) — #12: "Clocks subjected to sustained force run slow, by the same square-root formula that governs fast clocks, with force in place of velocity." It drops #13 §3's restriction of [force dilation](/wiki/conjugate-relativity/force-dilation) to conjugate-polarized systems and its open question of which clocks respond ([Open: which clocks respond](/wiki/conjugate-relativity/force-dilation#open-which-clocks-respond)); #13 governs.
- [Popsci-only: the mirror object as compact dark matter](/wiki/conjugate-relativity/momentum-space-black-holes#popsci-only-the-mirror-object-as-compact-dark-matter) — #12 says that a trap in momentum would be "undetectable by light, evident only through its gravity, and therefore indistinguishable, to our instruments, from compact dark matter". No document derives momentum-space black holes as dark matter or estimates their abundance; the program's candidates are the two of #11 §12, χ particles and the X-condensate ([dark-sector candidates](/wiki/dark-matter/candidates)).

### Predictions

- [Popsci-only: "constant is impossible"](/wiki/predictions/dark-energy-drift#popsci-only-constant-is-impossible) — #12: "Decreasing is required; phantom is impossible; constant is impossible", and "The framework survives only the first outcome" of the coming data. In #11 §13 row 4 a constant −1 in the third data release or later kills only the τ sector, and #10 agrees: "Constant kills the theory's heart. Phantom kills it outright."

## Conjecture-tier statements inside the record

These statements are in the repository's documents but are not derived there, and their own sources mark them as conjectures. Each is recorded on the page of the claim it qualifies.

- [Conjecture: the dual second law](/wiki/conjugate-relativity/dual-inertia#conjecture-the-dual-second-law) — #13 §5 makes the invariant length λ_χ "the measure of resistance to force-*change*" and tags the statement "[conjecture-tier; the full dual dynamics awaits the formalization of §6]". The dual dynamics waits on [the four-dimensional Born map](/wiki/conjugate-relativity/four-dimensional-born-map), which is open.
- [Conjecture: the thawing of dark energy as a drifting polarization angle](/wiki/symmetry-breaking/goldstone-angle#conjecture-the-thawing-of-dark-energy-as-a-drifting-polarization-angle) — the toy-model worklog: "It also means the present-day thawing of τ would be a slow drift of the polarization angle. That is a claim about the program, not verified here." No document computes the drift; the program's dark-energy prediction is [row 4](/wiki/predictions/dark-energy-drift).
- [Conjecture: continuous breaking in 3+1 dimensions](/wiki/symmetry-breaking/goldstone-angle#conjecture-continuous-breaking-in-31-dimensions) — the worklog notes that in 3+1 dimensions the Coleman–Mermin–Wagner theorem does not apply, so the self-dual coset model "can break the continuous U(1) itself, with τ an exactly massless Goldstone". Nothing computes it, and the toy-model note lists "anything beyond d = 1" as not shown.
- The unification of #11 §11.3 — "Conjecture [O]: the phase-space polarization (P5) and the charge-lattice polarization are components of one enlarged modular structure". It is registered as an open problem, [OP8](/wiki/electric-magnetic-duality/unified-modular-structure), in [open problems and the queue](/wiki/status/open-problems).

## Sources

- `CLAUDE.md` "Since the handoff" — the phase-space-diameter note done and its results; the current queue.
- `papers/phase-space-diameter.md` §2, §3, §5, §6, §9 — the relation's terms, unstated in the handoff; the identity, its values and what N counts; the clock as a distance from Z = i; the obituary of the square and the squeezed-mode reading; the status of each part.
- `review/round5-adjudication.md` "Verdict", "Recommendations to Paul" — verdict B from both referees; the note's support for flags 23 and 24.
- `verify/phase_space_diameter.py` — the relation's gated numbers.
- `HANDOFF.md` §4, §6, §8 — the chat-only list; the summary of rounds 1–2; the note as an optional write-up.
- `review/round3-adjudication.md` "Rulings" 3, "Decisions" 2–3 — the √N floor's premise inverted and the item dropped; the soliton candidate retired.
- `papers/broken-born-checkpoint-v2.md` §2, §5, §7, §11.3, §12, §13 — the battery's scope; the slaved momentum metric; the Yukawa cut at 1/M_X; the unification conjecture; the two candidates; row 4.
- `papers/conjugate-special-relativity.md` §3, §5, §6 — force dilation and its open clause; the conjecture-tier dual second law; "Yukawa-cut in momentum".
- `notes/debt1a-geometric-core.md` §A, §E; `notes/debt1a-ii-X-classification.md` §3 — the slaved momentum metric; dual stress as the source of X; a massive X with five polarizations.
- `notes/toy-lagrangian.md` "Chunk 2 results", "Chunk 3 results" — the two worklog conjectures.
- `popsci/universes-other-half.md` — #12, cited by section heading.
- `popsci/angle-of-the-mirror.md` — #10, cited by section heading.
- `review/wiki-build-flags.md` items 23, 24, 29 — the identification of a·ã = 1 with |Z| = 1; which bounce the diameter relation meant; the momentum reading of X's range.
