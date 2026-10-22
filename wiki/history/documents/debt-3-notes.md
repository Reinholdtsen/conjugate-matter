---
title: "The Debt-3 calc notes (#2–#4)"
weight: 40
status: record
description: "debt3a (stream stability), debt3b (the wave island) and debt3c (the ultra-faint-dwarf endpoint): the three working notes that closed Debt 3 against the program, section by section, with where their results went and where they differ."
sources:
  - "notes/debt3a-stream-stability.md"
  - "notes/debt3b-wave-island.md"
  - "notes/debt3c-ufd-endpoint.md"
  - "papers/broken-born-checkpoint-v2.md §9"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3)'"
  - "notes/broken-born-program-v1.md §7"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "CLAUDE.md 'Layout'"
  - "wiki/CLAUDE.md 'The wiki is derivative'"
  - "review/wiki-build-flags.md items 16, 19"
---

*The Debt-3 calc notes are three short working notes, artifacts #2 to #4, that tested the program's founding image: dark matter clumping by velocity rather than in space. The first showed that dark matter made of particles cannot clump this way. The second found that dark matter light enough to behave as a wave can, but only as an option, except in one scenario where clumping becomes compulsory in the smallest galaxies. The third showed that this scenario would have drained those galaxies of their dark matter, which observation rules out. Together they closed Debt 3 with a negative result, which checkpoint #11 now reports as an obituary. The notes are final for their own scope; no script in the gate checks their numbers.*

**Status:** Record, final for its scope — the notes carry few tags of their own (3b's rate is "[D, heuristic coefficients]", and 3b and 3c cite their literature as [T]); #11 §9 tags the particle-island result [D] and the wave-island result [D + T] — no `verify/` script covers any Debt-3 number. The files are unchanged since their import on 2026-10-19 (commit 8d588f6; moved to `notes/` in 008c3ee).

## What the notes are

Debt 3 was open problem 3 of [the lab notebook](/wiki/history/documents/lab-notebook)'s list: "Stream-instability growth rate γ vs. orbital phase-mixing: determines whether Prediction 3's granularity survives in Milky-Way-like halos. [O]" (#1 §11). The notebook had predicted that the gated self-interaction of conjugate matter would make a halo fragment into streams in velocity space, and the growth rate of that instability was "the theory's most important undone calculation on the astrophysics side" (#1 §5.2). It was the first of [the three debts](/wiki/history/debts) to be settled.

The work was done in three chunks, each written up as a working note with a status line: Chunk A (`notes/debt3a-stream-stability.md`, #2), Chunk B (`notes/debt3b-wave-island.md`, #3) and Chunk C (`notes/debt3c-ufd-endpoint.md`, #4). The notes are undated. They follow v0.1 of the notebook, whose v0.2 addendum summarizes them, and precede the Debt-1 notes. They share the notebook's scattering benchmark, σ₀/m = 30 cm²/g with m_χ = 70 MeV and v\* = 120 km/s (3a; #1 §5.1), and its numbering of the predictions table, in which rows 3 and 4 are velocity granularity and Fornax friction ([the scattering benchmark](/wiki/dark-matter/conjugate-matter/benchmark)).

## Their standing

[The handoff](/wiki/history/documents/handoff) marks all three "final", and #4 "final — closes Debt 3 (negative)" (`HANDOFF.md` §3). The wiki's precedence order treats the calc notes as "final for their own scope" (`wiki/CLAUDE.md`), while the root `CLAUDE.md` files them under `notes/`, "the audit trail, superseded as reference but kept". The current statement of their results is #11 §9, "Obituary: the death of momentum clumping (Debt 3)" ([momentum clumping (Debt 3)](/wiki/dark-matter/momentum-clumping)).

## #2, debt3a: the particle island

"Debt 3, Chunk A: Linear stability of the conjugate sector's velocity-space fragmentation". Status: "calculation complete. Result: negative on the particle island, with a structural corollary."

- **Setup.** The nonrelativistic mean-field (Vlasov) limit of the gated interaction, with a single-particle energy that includes the gated attraction of co-moving neighbors, coupling g ≡ 4πα̃/m_φ² = √(πσ₀/m²) and the position range collapsed to contact. Linearizing about a homogeneous Maxwellian distribution gives "An eigenvalue problem (the 'potential' lives on momentum space), not a scalar dispersion relation." See [the gated Vlasov model](/wiki/dark-matter/momentum-clumping/gated-vlasov-model) and [Vlasov stability and Landau damping](/wiki/dark-matter/momentum-clumping/vlasov-stability).
- **Two limits.** For a broad gate, which the note assigns to the "dwarf regime", the static threshold is gn/(mσ²) ≥ 1; below it perturbations are Landau-damped, and "There is no race with orbital stirring below threshold — the flocking never starts." The notebook's framing of growth against phase-mixing was therefore misplaced ([superseded](/wiki/dark-matter/momentum-clumping/gated-vlasov-model#superseded-racing-stream-growth-against-orbital-stirring)). For a narrow gate, the Milky Way (MW) and cluster regime, only co-moving particles count, and the "Unified criterion" is ε_gate ≳ m · min(σ, v\*)².
- **The numbers.** At the benchmark, where "g is *spent* — no freedom remains", the ratio of the two sides is "∼ 10⁻²⁸" in a dwarf core and "∼ 10⁻³¹" in the local Milky Way halo: "**Fails by 28–31 orders of magnitude.**" Collisions do not help: "equilibrium is Maxwellian to one part in 10³⁰". See [the mean-field criterion and its 10²⁸–10³¹ shortfall](/wiki/dark-matter/momentum-clumping/instability-criterion).
- **The corollary.** Holding σ₀/m fixed and asking what mass would satisfy the criterion gives m_crit "≈ 10⁻¹³ GeV ∼ 0.1 meV for MW conditions", where the occupation per mode is N_occ "∼ 10²⁰ ≫ 1": "Collective velocity-space dynamics and classical-particle dark matter are mutually exclusive within this framework." See [the classicality theorem](/wiki/dark-matter/momentum-clumping/classicality-theorem) and [occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number). The corollary evaluates the broad-gate form at Milky Way conditions, which the note treats as narrow-gate; `review/wiki-build-flags.md` item 19 records this, with the conclusion unchanged.
- **Consequences.** On the particle island rows 1–2 "**survive** — they are collisional", and rows 3 and 4 are "**withdrawn**". On the wave island the collective sector "is reborn in field language", with "a cliff-analog" surviving "as (v\*/σ)³ suppression rather than an exponential". The next chunk is the wave-island rate.

## #3, debt3b: the wave island

"Debt 3, Chunk B: Gated condensation on the wave island". Status: "rate derived, environments evaluated, verdict reached. Coefficients heuristic at O(1)–O(10) level; calibration against Levkov–Panin–Tkachev (LPT) numerics is a flagged to-do."

- **Setup.** On the wave island, "m ≲ 0.1 meV", the halo is "an incoherent classical field", and relaxation runs by wave kinetics with Bose enhancement, the mechanism Levkov, Panin and Tkachev established for gravity ([wave kinetics and Bose-star formation](/wiki/dark-matter/wave-dark-matter/wave-kinetics); [the wave island](/wiki/dark-matter/momentum-clumping/wave-island)).
- **The rate [D, heuristic coefficients].** Γ_self ≈ c g²ρ² min(σ, v\*)⁴/(m³σ⁶) with c = O(5–15). With a narrow gate it is "suppressed by (v\*/σ)⁴ — **a power law, not an exponential**". Two corollaries follow: the **island discriminant**, "The cliff's *sharpness* distinguishes the islands observationally", and a **gravity floor**: the gated channel dominates the gravitational one above a coupling "∼ 10⁻³¹ GeV⁻² (MW numbers) — an easy floor", and for m ≫ 10⁻²⁰ eV "the gated channel is the only game" ([the gated condensation rate](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate); [row 3](/wiki/predictions/island-discriminant)).
- **Scenario A, the gated channel as the core-maker.** Fitting dwarf cores spends the coupling, and the ratio of the condensation rate to the orbital rate is then about 10⁻² in classical dwarf cores and the inner Milky Way, 4×10⁻⁵ at the solar circle and ∼0 in clusters, but "∼ 40" in ultra-faint dwarfs (UFDs). "In UFDs, condensation is then mandatory and halo-wide", and with an attractive interaction the condensate has a critical mass, M_crit ≈ 3.6 M_P/(m√g) [T], above which it collapses ([Obituary: Scenario A](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a); [attractive condensates](/wiki/dark-matter/wave-dark-matter/attractive-condensates)).
- **Scenario B, cores from elsewhere.** With the coupling free, the stream condition leaves a window X ∈ [5×10⁻¹¹, 1] at m = 0.1 meV with Milky Way numbers, "ten orders of magnitude": "**Verdict B: streams are *tunable*, not mandatory.**" The note calls this "a degeneration flag" in Lakatos's terms ([Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b); [Lakatos's methodology](/wiki/method/lakatosian-methodology)).
- **"Bonus: the relic debt closes itself".** A field this light is produced by misalignment, like an axion, so "Open problem #5 (cannibalism-safe relic abundance) is moot on the wave island"; "The 5.4:1 question remains" ([relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)). "Open problem #5" is item 5 of #1 §11, not of #11 §14.
- **Standing results.** "Row 3 as written (Gaia/GD-1 granularity in MW-like halos) is dead on both islands as a *mandatory* signature." Next: Chunk 3c, "Completes Debt 3", then Debt 1.

## #4, debt3c: the ultra-faint-dwarf endpoint

"Debt 3, Chunk C: The ultra-faint-dwarf endpoint — closing Debt 3". Status: "complete. Verdict: Scenario A falsified; Debt 3 closed."

- **Sharpened inputs.** Segue 1 has "M(< 38 pc) ≈ 6×10⁵ M_⊙ ⇒ mean core density ρ ≈ 100 GeV/cm³ (not the conservative 20 used in 3b), σ ≈ 3.7 km/s, t_dyn ≈ 10 Myr". The rate ratio becomes "≈ 660", the condensation time "≈ 1.5×10⁴ yr", and over 10 Gyr "the system has ~6×10⁵ condensation times": "There is no timescale refuge."
- **The attractive endpoint.** Under the Scenario-A normalization, M_crit ≈ 2.9×10⁻³⁰ (m/eV)^{−7/4} M_⊙, which crosses the core mass of an ultra-faint dwarf at m ≈ 5×10⁻²¹ eV. For heavier fields, "the bulk of the wave island", the condensate reaches criticality almost at once and cycles through collapse, ejecting mass faster than the escape velocity: "**the condensate is a mass drain.**" Lighter fields are excluded independently, by ultra-faint-dwarf kinematics (Dalal and Kravtsov, "bound ≈ 3×10⁻¹⁹ eV; verify exact figure before publication") and the Lyman-α forest ([bounds on fuzzy dark matter](/wiki/dark-matter/wave-dark-matter/fuzzy-dark-matter-bounds)).
- **The data.** "Observed UFDs are the densest, most DM-dominated, oldest systems known", DM being dark matter; Segue 1 sits "in an intact, *dense* halo". No parameter direction rescues the scenario ([dwarf galaxies](/wiki/dark-matter/halo-astrophysics/dwarf-galaxies)).
- **The verdict.** "**Scenario A is falsified by the existence of ultra-faint dwarfs.**" With the other two chunks, Debt 3 closes: "**Nowhere in the viable parameter space of BBT is velocity-space clumping a mandatory phenomenon.** It is forbidden for classical-particle χ, fatal where it would have been mandatory (Scenario A), and merely optional elsewhere", BBT being the Broken-Born theory ([the net theorem](/wiki/dark-matter/momentum-clumping/net-theorem)). "Rows 3 and 4 of the predictions table are permanently withdrawn, on both islands. The Fornax mechanism goes with them" ([old row 3](/wiki/dark-matter/momentum-clumping/velocity-granularity); [old row 4](/wiki/dark-matter/momentum-clumping/fornax-friction)). "The surviving wave island is roughly 3×10⁻¹⁹ eV ≲ m ≲ 10⁻⁴ eV with Scenario-B couplings."
- **Next.** "Debt 1, Chunk 1a": linearize the geometric action "with ω, η frozen", importing the spectrum of linearized double field theory. The Debt-1 work that followed began instead by showing that with η frozen the program has no content of its own, and made η emergent ([the Debt-1 calc notes](/wiki/history/documents/debt-1-notes)).

## Where the results went

The lab notebook's v0.2 addendum recorded the outcome first: "Debt 3 is paid, and the answer went against the theory", with rows 3–4 struck and the island discriminant added (#1). The program v1.0 restated it in its §7, "(Debt 3: closed, negative)", and #11 §9 carries it as an obituary, with the particle-island result tagged [D], the wave-island result [D + T] and the net theorem stated as "forbidden (particles), fatal (committed wave), decorative (free wave)". The founding image is dead ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)), and its two predictions have their own obituaries in [the graveyard](/wiki/status/graveyard). The salvage is [row 3, the island discriminant](/wiki/predictions/island-discriminant), and the quarantined remainder is [Scenario B](/wiki/dark-matter/momentum-clumping/wave-island/scenario-b).

The handoff lists the result as dead and marks its central number machine-verified: "impossible for particle DM (criterion fails by 10²⁸–10³¹ ✓)" (`HANDOFF.md` §2). No `verify/` script computes it, and #11 §9 tags it [D]; the wiki follows #11 (`review/wiki-build-flags.md` item 16). A recomputation made while building the wiki, `review/wiki-build-checks/debt3a_check.py`, reproduces the shortfall but is not part of the gate.

## Where the notes differ

- **The power of the wave-island suppression.** 3a estimated "(v\*/σ)³"; 3b, 3c and #11 have (v\*/σ)⁴, and the fourth power governs ([the cubic suppression, superseded](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#superseded-the-cubic-suppression-of-debt-3a)).
- **The wave island's upper edge.** 3a's consequences give "m_χ ≲ meV", while its corollary and 3b's setup give 0.1 meV; 3c and the notebook's addendum write 10⁻⁴ eV.
- **The occupation number.** 3b writes N_occ = ρ/(m⁴σ³) in its setup and a "peak occupation N_occ ≈ (2π)^{3/2}ρ/(m⁴σ³)" in its rate, and does not reconcile the two ([occupation number](/wiki/dark-matter/wave-dark-matter/occupation-number)).
- **Scenario B's fuzzy end.** 3b's first source of cores, "fuzzy-end quantum pressure at m ∼ 10⁻²² eV", lies below the lower edge of the wave island that 3c sets, 3×10⁻¹⁹ eV. Neither note addresses it.
- **The exponential cliff.** The notes were written before the Debt-1 notes softened the cliff into a knee, so they still speak of an exponential suppression on the particle island ([the gated scattering law](/wiki/dark-matter/conjugate-matter/scattering-law)).
- **Numbering.** "Rows 3 and 4" are the notebook's old rows, and "Open problem #5" is the notebook's item 5; #9 and #11 number both lists differently ([history of the predictions table](/wiki/predictions/table-history)).

The unreconciled points are listed on [conflicts between sources](/wiki/history/documents/source-conflicts).

## What they left open

- **The coefficient c.** 3b's calibration against Levkov–Panin–Tkachev numerics was "a flagged to-do"; #9 §10 lists "LPT coefficient calibration" and #11 §9 writes "coefficients [O]" ([calibration of c](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#open-calibration-of-the-coefficient-c)).
- **Rows 1 and 2 in wave language.** 3a: "Rows 1–2 must be re-derived in wave language" ([rows 1 and 2 in wave language](/wiki/dark-matter/momentum-clumping/wave-island/condensation-rate#open-rows-1-and-2-in-wave-language)).
- **The exact light-mass bound**, which 3c asks to be verified before publication.
- **The topological loophole**, not raised in the notes: #11 §9 and the handoff leave untouched the localization in momentum of individual topological objects, which no candidate now serves ([Open: the topological loophole](/wiki/dark-matter/momentum-clumping/topological-loophole)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §9 — the current summary and its tags
- `notes/debt3a-stream-stability.md` — the particle island, the criterion and its shortfall, the classicality corollary
- `notes/debt3b-wave-island.md` — the condensation rate, the island discriminant, Scenarios A and B, the misalignment bonus
- `notes/debt3c-ufd-endpoint.md` — the Segue 1 endpoint, the verdict and the net theorem
- `notes/broken-born-theory.md` §11 — Debt 3 as open problem 3; §5.2 — the founding image; 'Addendum (v0.2, post Debt-3)' — the first summary
- `notes/broken-born-program-v1.md` §7 — "(Debt 3: closed, negative)"
- `HANDOFF.md` §3 rows 2–4 — the notes' standing; §2 — the ✓ on 10²⁸–10³¹
- `CLAUDE.md` 'Layout' and `wiki/CLAUDE.md` 'The wiki is derivative' — their place among the documents
- `review/wiki-build-flags.md` items 16 and 19 — the ✓ without a script, and the regime of the classicality corollary
