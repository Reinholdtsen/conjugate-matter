---
title: "Obituary: the √N topological floor (chat-only)"
weight: 70
status: dead
description: "A chat-only bound on the relic abundance between a 'Kibble ceiling' and a √N net-charge floor, dropped because its premise is inverted and no candidate is left; the strong-coupling annihilation question it addressed."
sources:
  - "review/round3-adjudication.md 'Decisions' 3"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/round3-adjudication.md 'Rulings' 3"
  - "review/round3-adjudication.md 'Rulings' 10"
  - "CLAUDE.md 'Since the handoff'"
  - "papers/broken-born-checkpoint-v2.md §12"
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

*The √N topological floor was an argument, made only in the claude.ai chat that preceded this repository, about how many of the soliton candidate's monopoles could survive annihilation in the early universe. A monopole and an antimonopole that meet can annihilate, and at the hidden sector's strong magnetic coupling, about 34, that annihilation might have been fast enough to deplete them. The floor argument held that the Kibble mechanism leaves a net topological charge that annihilation cannot remove, so the surviving abundance would lie between a Kibble "ceiling" and that floor. It was never written into any document. In round 3 the referee showed that Kibble's count is a minimum, not a ceiling, and that annihilation at this coupling has already been worked out for hidden sectors; with the soliton candidate retired, the planned calculation was dropped.*

**Status:** Dead (chat-only) — dropped by round-3 Decision 3: "Its premise, Kibble as a ceiling, is inverted (ruling 3)." "Under decision 2 it has no candidate left to serve." The [project instructions](/wiki/history/documents/project-instructions) record the same: "HANDOFF §8 queue item 3 is dropped." The argument was never written up and never machine-checked; no number belongs to it. Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); the decision is in [round-3 decisions](/wiki/method/review/round-3/decisions) and the rulings behind it in [round-3 verdict and rulings](/wiki/method/review/round-3/rulings); listed in [the graveyard](/wiki/status/graveyard) and among [conjectures](/wiki/status/conjectures).

## What was claimed

### The question: annihilation at strong coupling

A monopole and an antimonopole carry opposite topological charge, and when they meet they can annihilate into lighter particles [T]. After a phase transition has formed monopoles, annihilation is the only process that lowers their number, so a relic calculation follows how fast the pairs find each other as the universe cools ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)). For superheavy monopoles in our own plasma the classic analysis, Preskill 1979 (#14's [19]), found annihilation too slow to matter, which is why grand-unification monopoles would be overproduced: [the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem) [T].

The soliton candidate's monopoles were ['t Hooft–Polyakov monopoles](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole) of a hidden gauge sector ([the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)), and their mutual magnetic coupling is strong: α_m = 1/α_W′, the inverse of the sector's weak electric coupling, by [Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) (#14 §2). Under the manuscript's hypothesis H it is "1/(4 alpha) ~ 34" ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)). The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) (v3, §3) named what this changes:

> The classic relic analysis [19] found monopole-antimonopole annihilation inefficient for superheavy monopoles in our plasma. Here annihilation runs through the hidden plasma (psi and hidden photons) at alpha_m ~ 34, where Sommerfeld enhancement and rapid bound-state formation may matter. Whether the Kibble abundance survives requires a dedicated strong-coupling freeze-out calculation in that plasma, not performed here (acceptance criterion 3). Inflation must precede the hidden transition, and v must lie below the reheating temperature.

Both effects belong to attractive long-range forces [T]. Sommerfeld enhancement is the focusing of the two particles' relative wavefunction by their mutual attraction: at low relative velocity the wave piles up at short distance, and the annihilation rate rises above its short-distance value by a factor that grows with the ratio of the coupling to the velocity. Bound-state formation is a second route: an attracting pair radiates, drops into a bound orbit and then annihilates. At a coupling of about 34 both could be large, and the worry was that annihilation would remove too many monopoles to leave the observed dark-matter density. The handoff calls it the "Sommerfeld catastrophe" (§4) and "Sommerfeld probably fatal" (§8 item 3).

#14 made the calculation acceptance criterion 3, "the strong-coupling relic freeze-out calculation of Sec. 3, in the hidden plasma" (§6), and exclusion condition 4, "A strong-coupling relic calculation showing that monopole annihilation in the hidden plasma at alpha_m ~ 34 cannot leave the observed abundance" (§5). The v3 worklog had already noted that the classic result could not simply be carried over: "Preskill (verified from the scan): annihilation cannot reduce n/T³ below ~10⁻¹⁰ at m ≈ 10¹⁶ GeV. For a hidden sector the rate runs through the dark plasma, so it has to be recomputed (acceptance criterion 3), not carried over" ('Findings neither referee raised', F1).

### The floor argument

[The handoff](/wiki/history/documents/handoff) lists the question as open item 2 of its scientific state (§2), together with the chat's answer to it:

> Strong-coupling relic freeze-out at α_d ~ 34: Sommerfeld-enhanced annihilation vs. the √N topological-charge floor (Kibble leaves a net-charge residue annihilation cannot remove — chat-only idea, not yet in any paper; this bounds the relic abundance between Kibble ceiling and √N floor)

The argument has two edges.

- **The ceiling.** The [Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) estimates the number of monopoles a transition forms, written n/s = p (T_c/M_Pl)³ for the number per unit entropy, with T_c the transition temperature, M_Pl the Planck mass and p a normalization. [Checkpoint #11](/wiki/history/documents/checkpoint) §12 records that this estimate "had been normalized at p = 1 (#14 v2) and p ≈ 0.023 (#14 v3)", and v3 still says "we take p = 1 as the upper end" (§3). Read that way, Kibble's count bounds the abundance from above, before any annihilation.
- **The floor.** Annihilation removes monopole–antimonopole pairs, so it cannot change the net topological charge, the number of monopoles minus antimonopoles. Whatever net charge the Kibble mechanism leaves behind therefore survives, and bounds the abundance from below.

The handoff gives no formula for the floor. The name points to the standard random-walk estimate [T]: N defects formed with independent random charges leave a net charge of order √N. That reading is the wiki's, from the name alone; no source writes the estimate out. The handoff's list of results that exist only in the chat names the idea as "**√N topological floor** argument against the Sommerfeld catastrophe (open item #2 above)" (§4): whatever the annihilation rate, some monopoles would be left.

### The planned calculation

The handoff's ranked queue made the estimate its third item, after cutting v3 of #14 and re-running the blind audit (§8):

> **√N-floor freeze-out estimate** (open item #2) — resolves "Sommerfeld probably fatal" into a number; Preskill-style kinetic calculation; decides whether the soliton candidate's abundance window exists.

v3, written next, kept the strong-coupling question as acceptance criterion 3 and exclusion condition 4, but neither it nor any other document contains the floor argument, and no document records the calculation.

## How it was tested

The floor itself was never tested. [Round 3](/wiki/method/review/round-3) of blind review tested the two things it rested on, the Kibble normalization read as an upper end and the open status of strong-coupling annihilation, with executed code and the literature (`review/round3/referee/audit-notes.md`).

On the normalization, the referee's numerical table (Step 2) gives one monopole per Hubble volume as p = 104.3, and the note on its brackets rejects v3's range p ∈ [0.023, 1] as not reasonable, because "Kibble's one-per-horizon is a causal lower bound" (the referee sets "lower" in capitals). The note gives three supports: Gangui (astro-ph/0110285), "n/s ~ 100 (T_c/m_P)^3"; the hidden-monopole paper of [Liveoak–Maharana–Wells](/wiki/dark-matter/candidates/soliton-candidate/prior-art) (LMW, 2026, which #11 cites as [29S]), "minimal number density ... one per Hubble volume"; and Kibble–Zurek production, "n ~ lambda H T_c^2, i.e. (M_Pl/T_c)^2 per horizon". Its conclusion: "p should be >= ~25-100, not <= 1." The corrected count is on [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization).

On annihilation, the referee integrated the hidden-sector relic with the capture rates of the Liveoak–Maharana–Wells paper at the manuscript's own parameters (Step 4(a) item 3). Starting from Kibble–Zurek production, in which the correlation length at the transition is set by how fast the transition is crossed and is far shorter than the horizon, the final abundance is "Omega/Omega_DM = 1.1e12 - 2.2e12", and the paper's analytic formula gives "1.2e9 - 2.2e11" times the observed density: "Either way the annihilation does not rescue it." Starting from the Kibble minimum instead, the initial yield of monopoles per unit entropy ("Kibble-minimum initial Y (7e-20 - 1.4e-18)") lies "far" below the annihilation attractor, "so annihilation is irrelevant in that case and overproduction 4.9e3 - 9.8e4 (xi=0.76..0.5) stands." The attractor is the final abundance that annihilation drives every sufficiently large initial abundance toward [T]; an initial abundance already below it is left unchanged. The referee concluded:

> => Acceptance criterion 3 is not open: the "strong-coupling" regime alpha_m = 34 is exactly the Dirac-monopole case of Preskill 1979 (h = 2 pi/e); its modern hidden-sector version (LMW 2026) excludes v >~ 100 PeV for hidden monopoles.

A monopole with the minimal Dirac charge h = 2π/e relative to an electric charge e has the magnetic coupling 1/(4α) when e²/4π = α. Hypothesis H sets the hidden sector's smallest charge equal to the electron's, so the hidden monopoles have the coupling of a Dirac monopole of our own electromagnetism, the case Preskill treated. That is the sense in which the strong-coupling regime was not new (the wiki's gloss of the referee's parenthesis).

## Why it was dropped

### The premise is inverted

Ruling 3, upheld: "Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more." The adjudication's evidence is the literature: Murayama–Shu, arXiv:0905.1720, abstract: Kibble "drastically underestimates the production of topological defects"; Liveoak–Maharana–Wells, arXiv:2607.20843, abstract: hidden monopoles overclose for breaking scales ≳ 100 PeV unless diluted.

The physics behind the ruling is standard [T]. At a symmetry-breaking transition the direction the field picks in its vacuum manifold is uncorrelated beyond some correlation length, and causality keeps that length below the horizon. Where uncorrelated domains meet, a defect is trapped with a probability of order one, so a transition forms at least about one defect per horizon volume. Real transitions have correlation lengths well below the horizon, and a first-order transition forms defects where its bubbles meet, so both add to Kibble's count. The referee's own figure for bubble counting, for the first-order transitions #14 contemplated, is "p ~ 104 (beta/H)^3 = 1e2-1e8" (Step 4(a) item 2), against v3's "p = 1 as the upper end".

With Kibble's count a minimum, the window had no upper edge. The candidate's problem became the opposite of the one the floor was meant to answer: not too few monopoles after annihilation, but too many, which annihilation cannot remove ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)).

### The annihilation case was already worked out

Ruling 10, "**Upheld** (abstract level)": "Annihilation at α_m ≈ 34 is Preskill's Dirac case, already done for hidden sectors", with the evidence "LMW 2026 as in #3". The adjudicator checked the Liveoak–Maharana–Wells result at the level of its abstract and did not re-run the referee's integration (ruling 3: "I did not re-run the referee's Kibble–Zurek integration (1e9–1e12 overproduction)"; flag 21 in `review/wiki-build-flags.md` notes that the lower end of that range is the analytic estimate quoted above, not the integration). The published scenario is on [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art).

### No candidate left

Decision 2 retired the soliton candidate as a program-native proposal ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). Decision 3 followed:

> **HANDOFF §8 queue item 3 (the "√N floor"): dropped.**
> - Its premise, Kibble as a ceiling, is inverted (ruling 3).
> - Under decision 2 it has no candidate left to serve.

## What survives

Nothing of the floor. The strong-coupling annihilation it was meant to bound has already been treated in the literature (Preskill 1979; Liveoak–Maharana–Wells 2026), and in the program's own record the question lapsed with the candidate. The handoff's open item 2 and queue item 3 are superseded; the current queue is the one in the project instructions' 'Since the handoff' section, which opens with the handoff's items 5–7 ([open problems](/wiki/status/open-problems)).

The other results of the handoff's chat-only list (§4) have their own pages: [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), [momentum-space black holes](/wiki/conjugate-relativity/momentum-space-black-holes), and the two gravitational charges and the equation comparison on [the momentum graviton's chat-only results](/wiki/gravity/momentum-graviton/chat-only-results). All are registered in [conjectures](/wiki/status/conjectures).

## Record

1. **The claude.ai chat**, before the move to this repository: the floor argument is made and not written down (`HANDOFF.md` §4).
2. **The handoff**: open item 2 of the scientific state (§2) and queue item 3 (§8).
3. **v3 of #14** (2026-10-19): the strong-coupling calculation is acceptance criterion 3 and exclusion condition 4; there is no floor.
4. **Round 3** (2026-10-19, verdict C): the referee finds Kibble's count a causal lower bound and criterion 3 not open; rulings 3 and 10 uphold both.
5. **Decision 3** (2026-10-19): the queue item is dropped, as the project instructions record under 'Since the handoff'.

## Sources

- `review/round3-adjudication.md` 'Decisions' 3 — dropped; 'Decisions' 2 — the candidate retired; 'Rulings' 3 and 10 — the inverted premise and the solved annihilation case
- `CLAUDE.md` 'Since the handoff' — "HANDOFF §8 queue item 3 is dropped"
- `papers/broken-born-checkpoint-v2.md` §12 — the p = 1 and p ≈ 0.023 normalizations
- `HANDOFF.md` §2 — the idea, as open item 2; §4 — its chat-only status; §8 — queue item 3
- `review/round3/referee/audit-notes.md` Step 2 — the bracket of p judged; Step 4(a) items 2 and 3 — bubble counting, the relic integration, and "Acceptance criterion 3 is not open"
- `review/v3-worklog.md` 'Findings neither referee raised' (F1) — Preskill's bound, to be recomputed for a hidden sector
- `notes/knot-dark-matter-standalone.md` §2 — α_m = 1/α_W′ and hypothesis H; §3 — the strong-coupling question and "p = 1 as the upper end"; §5 — exclusion condition 4; §6 — acceptance criterion 3
- `review/wiki-build-flags.md` item 21 — the source of the lower end of ruling 3's range
