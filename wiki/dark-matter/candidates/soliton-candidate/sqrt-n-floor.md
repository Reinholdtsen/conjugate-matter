---
title: "Under review: the √N topological floor (chat-only)"
weight: 70
status: under-review
description: "A chat-only bound on the relic abundance between a 'Kibble ceiling' and a √N net-charge floor, whose queued calculation was dropped because its premise is inverted and, with #14's model retired, no candidate was left for it; the strong-coupling annihilation question it addressed."
sources:
  - "review/round3-adjudication.md 'Decisions' 3"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/round3-adjudication.md 'Rulings' 3"
  - "review/round3-adjudication.md 'Rulings' 10"
  - "CLAUDE.md 'Since the handoff'"
  - "wiki/papers/broken-born-checkpoint-v2.md §12"
  - "wiki/papers/phase-space-diameter.md §3"
  - "wiki/papers/phase-space-diameter.md §6"
  - "wiki/papers/phase-space-diameter.md §9"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "HANDOFF.md §8"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/wiki-build-flags.md item 21"
---

*The √N topological floor was an argument, made only in the claude.ai chat that preceded this repository, about how many of the monopoles of [#14](../../../../notes/knot-dark-matter-standalone.md)'s soliton model could survive annihilation in the early universe. A monopole and an antimonopole that meet can annihilate, and at the strong magnetic coupling of the model's [hidden sector](hidden-sector.md), [about 34](alpha-d-coupling.md), that annihilation might have been fast enough to deplete them. The floor argument held that the Kibble mechanism leaves a net topological charge that annihilation cannot remove, so the surviving abundance would lie between a Kibble "ceiling" and that floor. It was never written up: only [the handoff](../../../history/documents/handoff.md) records it, without a formula. In round 3 the referee showed that Kibble's count is a minimum, not a ceiling, and that annihilation at this coupling has already been worked out for hidden sectors; with #14's model retired, the planned calculation was dropped.*

**Status:** Under review — the evidence below weighs against it, and its final status awaits review. Chat-only. Round-3 Decision 3 dropped the calculation queued for it: "Its premise, Kibble as a ceiling, is inverted (ruling 3)." "Under decision 2 it has no candidate left to serve" (the candidate meant is #14's model, which Decision 2 covers). The [project instructions](../../../history/documents/project-instructions.md) record the same: "[HANDOFF §8](../../../../HANDOFF.md#8-ranked-next-actions-queue) queue item 3 is dropped." The argument was never written up and never machine-checked; no number belongs to it. Home section: [#14's soliton model](_index.md); the decision is in [round-3 decisions](../../../method/review/round-3/decisions.md) and the rulings behind it in [round-3 verdict and rulings](../../../method/review/round-3/rulings.md); listed in [claims under review](../../../status/under-review.md) and among [conjectures](../../../status/conjectures.md).

## What was claimed

### The question: annihilation at strong coupling

A monopole and an antimonopole carry opposite topological charge, and when they meet they can annihilate into lighter particles [T]. After a phase transition has formed monopoles, annihilation is the only process that lowers their number, so a relic calculation follows how fast the pairs find each other as the universe cools ([relic abundance mechanisms](../relic-abundance.md)). For superheavy monopoles in our own plasma the classic analysis, Preskill 1979 (#14's [19]), found annihilation too slow to matter, which is why grand-unification monopoles would be overproduced: [the monopole problem](../../../electric-magnetic-duality/monopoles/monopole-problem.md) [T].

The monopoles of #14's model were ['t Hooft–Polyakov monopoles](../../../electric-magnetic-duality/monopoles/thooft-polyakov-monopole.md) of a hidden gauge sector ([the hidden SU(2) → U(1) proposal](hidden-sector.md)), and their mutual magnetic coupling is strong: α_m = 1/α_W′, the inverse of the sector's weak electric coupling, by [Dirac quantization](../../../electric-magnetic-duality/monopoles/dirac-quantization.md) ([#14 §2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling)). Under the manuscript's hypothesis H it is "1/(4 alpha) ~ 34" ([Under review: the coupling α_d ≈ 34](alpha-d-coupling.md)). The withdrawn manuscript [#14](_index.md) (v3, §3) named what this changes:

> The classic relic analysis [19] found monopole-antimonopole annihilation inefficient for superheavy monopoles in our plasma. Here annihilation runs through the hidden plasma (psi and hidden photons) at alpha_m ~ 34, where Sommerfeld enhancement and rapid bound-state formation may matter. Whether the Kibble abundance survives requires a dedicated strong-coupling freeze-out calculation in that plasma, not performed here (acceptance criterion 3). Inflation must precede the hidden transition, and v must lie below the reheating temperature.

Both effects belong to attractive long-range forces [T]. Sommerfeld enhancement is the focusing of the two particles' relative wavefunction by their mutual attraction: at low relative velocity the wave piles up at short distance, and the annihilation rate rises above its short-distance value by a factor that grows with the ratio of the coupling to the velocity. Bound-state formation is a second route: an attracting pair radiates, drops into a bound orbit and then annihilates. At a coupling of about 34 both could be large, and the worry was that annihilation would remove too many monopoles to leave the observed dark-matter density. The handoff calls it the "Sommerfeld catastrophe" (§4) and "Sommerfeld probably fatal" (§8 item 3).

#14 made the calculation acceptance criterion 3, "the strong-coupling relic freeze-out calculation of Sec. 3, in the hidden plasma" ([§6](../../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria); [freeze-out of defects](../thermal-freeze-out.md#other-freeze-outs-in-the-record)), and exclusion condition 4, "A strong-coupling relic calculation showing that monopole annihilation in the hidden plasma at alpha_m ~ 34 cannot leave the observed abundance" ([§5](../../../../notes/knot-dark-matter-standalone.md#5-exclusion-conditions)). The v3 worklog had already noted that the classic result could not simply be carried over: "Preskill (verified from the scan): annihilation cannot reduce n/T³ below ~10⁻¹⁰ at m ≈ 10¹⁶ GeV. For a hidden sector the rate runs through the dark plasma, so it has to be recomputed (acceptance criterion 3), not carried over" ('Findings neither referee raised', F1).

### The floor argument

[The handoff](../../../history/documents/handoff.md) lists the question as open item 2 of its scientific state (§2), together with the chat's answer to it:

> Strong-coupling relic freeze-out at α_d ~ 34: Sommerfeld-enhanced annihilation vs. the √N topological-charge floor (Kibble leaves a net-charge residue annihilation cannot remove — chat-only idea, not yet in any paper; this bounds the relic abundance between Kibble ceiling and √N floor)

The argument has two edges.

- **The ceiling.** The [Kibble mechanism](../../../electric-magnetic-duality/monopoles/kibble-mechanism.md) estimates the number of monopoles a transition forms, written n/s = p (T_c/M_Pl)³ for the [number per unit entropy](../../../cosmology/early-universe/relic-yield-and-dilution.md#the-kibble-yield-t), with T_c the transition temperature, M_Pl the [Planck mass](../../../gravity/spin-2-fields/planck-units.md) and p a normalization ([Under review: the Kibble normalization](kibble-normalization.md)). [Checkpoint #11](../../../history/documents/checkpoint.md) [§12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) records that this estimate "had been normalized at p = 1 (#14 v2) and p ≈ 0.023 (#14 v3)", and v3 still says "we take p = 1 as the upper end" (§3). Read that way, Kibble's count bounds the abundance from above, before any annihilation.
- **The floor.** Annihilation removes monopole–antimonopole pairs, so it cannot change the net topological charge, the number of monopoles minus antimonopoles. Whatever net charge the Kibble mechanism leaves behind therefore survives, and bounds the abundance from below.

The handoff gives no formula for the floor. The name points to the standard random-walk estimate [T]: N [defects](../../../symmetry-breaking/topological-defects.md) formed with independent random charges leave a net charge of order √N. That reading is the wiki's, from the name alone; no source writes the estimate out. The handoff's list of results that exist only in the chat names the idea as "**√N topological floor** argument against the Sommerfeld catastrophe (open item [#2](../../../../notes/stream-stability.md) above)" (§4): whatever the annihilation rate, some monopoles would be left.

### The planned calculation

The handoff's ranked queue made the estimate its third item, after cutting v3 of #14 and re-running the blind audit (§8):

> **√N-floor freeze-out estimate** (open item #2) — resolves "Sommerfeld probably fatal" into a number; Preskill-style kinetic calculation; decides whether the soliton candidate's abundance window exists.

v3, written next, kept the strong-coupling question as acceptance criterion 3 and exclusion condition 4, but neither it nor any later document sets out the floor argument, and no document records the calculation.

## How it was tested

The floor itself was never tested. [Round 3](../../../method/review/round-3/_index.md) of blind review tested the two things it rested on, the Kibble normalization read as an upper end and the open status of strong-coupling annihilation, with executed code and the literature ([`review/round3/referee/audit-notes.md`](../../../../review/round3/referee/audit-notes.md)).

On the normalization, the referee's numerical table (Step 2) gives one monopole per Hubble volume as p = 104.3, and the note on its brackets rejects v3's range p ∈ [0.023, 1] as not reasonable, because "Kibble's one-per-horizon is a causal lower bound" (the referee sets "lower" in capitals). The note gives three supports: Gangui ([astro-ph/0110285](https://arxiv.org/abs/astro-ph/0110285)), "n/s ~ 100 (T_c/m_P)^3"; the hidden-monopole paper of [Liveoak–Maharana–Wells](prior-art.md) (LMW, 2026, which [#11](../../../papers/broken-born-checkpoint-v2.md) cites as [29S]), "minimal number density ... one per Hubble volume"; and Kibble–Zurek production, "n ~ lambda H T_c^2, i.e. (M_Pl/T_c)^2 per horizon". Its conclusion: "p should be >= ~25-100, not <= 1." The corrected count is on [Under review: the Kibble normalization](kibble-normalization.md).

On annihilation, the referee integrated the hidden-sector relic with the capture rates of the Liveoak–Maharana–Wells paper at the manuscript's own parameters (Step 4(a) item 3). Starting from Kibble–Zurek production, in which the correlation length at the transition is set by how fast the transition is crossed and is far shorter than the horizon, the final abundance is "Omega/Omega_DM = 1.1e12 - 2.2e12", and the paper's analytic formula gives "1.2e9 - 2.2e11" times the observed density: "Either way the annihilation does not rescue it." Starting from the Kibble minimum instead, the initial yield of monopoles per unit entropy ("Kibble-minimum initial Y (7e-20 - 1.4e-18)") lies "far" below the annihilation attractor, "so annihilation is irrelevant in that case and overproduction 4.9e3 - 9.8e4 (xi=0.76..0.5) stands." The attractor is the final abundance that annihilation drives every sufficiently large initial abundance toward [T]; an initial abundance already below it is left unchanged. The referee concluded:

> => Acceptance criterion 3 is not open: the "strong-coupling" regime alpha_m = 34 is exactly the Dirac-monopole case of Preskill 1979 (h = 2 pi/e); its modern hidden-sector version (LMW 2026) excludes v >~ 100 PeV for hidden monopoles.

A monopole with the minimal Dirac charge h = 2π/e relative to an electric charge e has the magnetic coupling 1/(4α) when e²/4π = α. Hypothesis H sets the hidden sector's smallest charge equal to the electron's, so the hidden monopoles have the coupling of a Dirac monopole of our own electromagnetism, the case Preskill treated. That is the sense in which the strong-coupling regime was not new (the wiki's gloss of the referee's parenthesis).

## Why it was dropped

### The premise is inverted

Ruling 3, upheld: "Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more." The adjudication's evidence is the literature: Murayama–Shu, [arXiv:0905.1720](https://arxiv.org/abs/0905.1720), abstract: Kibble "drastically underestimates the production of topological defects"; Liveoak–Maharana–Wells, [arXiv:2607.20843](https://arxiv.org/abs/2607.20843), abstract: hidden monopoles overclose for breaking scales ≳ 100 PeV unless diluted.

The physics behind the ruling is standard [T]. At a symmetry-breaking transition the direction the field picks in its vacuum manifold is uncorrelated beyond some correlation length, and causality keeps that length below the horizon. Where uncorrelated domains meet, a defect is trapped with a probability of order one, so a transition forms at least about one defect per horizon volume. Real transitions have correlation lengths well below the horizon, and a first-order transition forms defects where its bubbles meet, so both add to Kibble's count. The referee's own figure for bubble counting, for the first-order transitions #14 contemplated, is "p ~ 104 (beta/H)^3 = 1e2-1e8" (Step 4(a) item 2), against v3's "p = 1 as the upper end".

With Kibble's count a minimum, the window had no upper edge. The model's problem became the opposite of the one the floor was meant to answer: not too few monopoles after annihilation, but too many, which annihilation cannot remove ([overproduction at the benchmark](overproduction.md)).

### The annihilation case was already worked out

Ruling 10, "**Upheld** (abstract level)": "Annihilation at α_m ≈ 34 is Preskill's Dirac case, already done for hidden sectors", with the evidence "LMW 2026 as in [#3](../../../../notes/wave-island.md)". The adjudicator checked the Liveoak–Maharana–Wells result at the level of its abstract and did not re-run the referee's integration (ruling 3: "I did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction)"; flag 21 in [`review/wiki-build-flags.md`](../../../../review/wiki-build-flags.md) notes that the lower end of that range is the analytic estimate quoted above, not the integration). The published scenario is on [topological dark matter in the literature](prior-art.md).

### No candidate left

Decision 2 retired #14's model as a program-native proposal ([Obituary: #14's superheavy-soliton model](obituary.md)). Decision 3 followed:

> **[HANDOFF §8](../../../../HANDOFF.md#8-ranked-next-actions-queue) queue item 3 (the "√N floor"): dropped.**
> - Its premise, Kibble as a ceiling, is inverted (ruling 3).
> - Under decision 2 it has no candidate left to serve.

The candidate meant is #14's model, which Decision 2 covers: it used ordinary kinematics, and the floor concerned its monopoles. The candidate itself, conjugate monopoles localized in momentum, is P.R.'s open conjecture; it was never modeled, and no document applies the floor to it ([Conjecture: magnetic monopoles abundant in momentum space](../momentum-space-monopoles.md)).

## What stands

No source lists anything of the floor among the survivors of v3, and none tests or refutes its own step, that annihilation cannot remove net topological charge: Decision 3 dropped the queued estimate for its inverted premise and for want of a candidate, without a calculation of the floor. The strong-coupling annihilation it was meant to bound has already been treated in the literature (Preskill 1979; Liveoak–Maharana–Wells 2026), and in the program's record the question lapsed with #14's model. The handoff's open item 2 and queue item 3 are superseded; the current queue is the one in the project instructions' 'Since the handoff' section, which opens with the handoff's items 5–6 ([open problems](../../../status/open-problems.md)).

The other results of the handoff's chat-only list (§4) have their own pages: [the phase-space diameter relation](../../../cosmology/scale-factor-duality/phase-space-diameter.md), [momentum-space black holes](../../../conjugate-relativity/momentum-space-black-holes.md), and the two gravitational charges and the equation comparison on [the momentum graviton's chat-only results](../../../gravity/momentum-graviton/chat-only-results.md). The diameter relation has been written up and tested in the phase-space-diameter note ([`wiki/papers/phase-space-diameter.md`](../../../papers/phase-space-diameter.md)): its corrected form is an identity of blackbody statistics [D][V], standard physics that cannot test the program, and its claim that the universe's position–momentum rectangle is square "exactly at the bounce" is withdrawn [D][V] and under review (§9) ([Under review: the square rectangle at the bounce](../../../cosmology/scale-factor-duality/square-at-the-bounce.md)). The others are still chat-only and are registered in [conjectures](../../../status/conjectures.md).

## Record

1. **The claude.ai chat**, before the move to this repository: the floor argument is made and not written down ([`HANDOFF.md` §4](../../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact)).
2. **The handoff**: open item 2 of the scientific state (§2) and queue item 3 (§8).
3. **v3 of #14** (2026-10-19): the strong-coupling calculation is acceptance criterion 3 and exclusion condition 4; there is no floor.
4. **Round 3** (2026-10-19, verdict C): the referee finds Kibble's count a causal lower bound and criterion 3 not open; rulings 3 and 10 uphold both.
5. **Decision 3** (2026-10-19): the queue item is dropped, as the project instructions record under 'Since the handoff'.

## Sources

- [`review/round3-adjudication.md`](../../../../review/round3-adjudication.md) 'Decisions' 3 — dropped; 'Decisions' 2 — the retirement, which covers #14's model; 'Rulings' 3 and 10 — the inverted premise and the solved annihilation case
- [`CLAUDE.md`](../../../../CLAUDE.md) 'Since the handoff' — "[HANDOFF §8](../../../../HANDOFF.md#8-ranked-next-actions-queue) queue item 3 is dropped"; the √N floor under review
- [`wiki/papers/broken-born-checkpoint-v2.md` §12](../../../papers/broken-born-checkpoint-v2.md#12-the-dark-sector-question-three-candidates) — the p = 1 and p ≈ 0.023 normalizations; the candidate as P.R.'s conjecture
- [`wiki/papers/phase-space-diameter.md` §3](../../../papers/phase-space-diameter.md#3-the-conserved-area-a-cosmological-timebandwidth-relation) — the diameter relation as an identity of blackbody statistics that cannot test the program; [§6](../../../papers/phase-space-diameter.md#6-where-the-rectangle-is-square) — the withdrawal of "square exactly at the bounce", under review; [§9](../../../papers/phase-space-diameter.md#9-summary) — the summary table
- [`HANDOFF.md` §2](../../../../HANDOFF.md#2-scientific-state-one-screen) — the idea, as open item 2; [§4](../../../../HANDOFF.md#4-results-that-exist-only-in-the-chat-not-in-any-artifact) — its chat-only status; [§8](../../../../HANDOFF.md#8-ranked-next-actions-queue) — queue item 3
- [`review/round3/referee/audit-notes.md`](../../../../review/round3/referee/audit-notes.md) Step 2 — the bracket of p judged; Step 4(a) items 2 and 3 — bubble counting, the relic integration, and "Acceptance criterion 3 is not open"
- [`review/v3-worklog.md`](../../../../review/v3-worklog.md) 'Findings neither referee raised' (F1) — Preskill's bound, to be recomputed for a hidden sector
- [`notes/knot-dark-matter-standalone.md` §2](../../../../notes/knot-dark-matter-standalone.md#2-the-hidden-sector-and-its-coupling) — α_m = 1/α_W′ and hypothesis H; [§3](../../../../notes/knot-dark-matter-standalone.md#3-the-candidate) — the strong-coupling question and "p = 1 as the upper end"; [§5](../../../../notes/knot-dark-matter-standalone.md#5-exclusion-conditions) — exclusion condition 4; [§6](../../../../notes/knot-dark-matter-standalone.md#6-status-of-claims-and-acceptance-criteria) — acceptance criterion 3
- [`review/wiki-build-flags.md`](../../../../review/wiki-build-flags.md) item 21 — the source of the lower end of ruling 3's range
