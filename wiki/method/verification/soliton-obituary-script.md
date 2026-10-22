---
title: "The soliton-obituary script"
weight: 80
status: method
description: "verify/soliton_obituary.py recomputes the adjudicator's figures for round-3 rulings 1, 2, 4 and 5 and every [V] number of the #11 §12 obituary, after four anchors independent of the manuscript; it replaced knot_numbers.py, which checked the withdrawn paper's own claims."
provenance: [V]
sources:
  - "verify/soliton_obituary.py"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Decisions'"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md header"
  - "review/v3-worklog.md 'New open items (to compute before v3 states anything about them)'"
  - "CLAUDE.md 'Layout'"
  - "review/wiki-build-flags.md items 21, 22, 33, 34"
---

*The soliton-obituary script, `verify/soliton_obituary.py`, recomputes the numbers in the record of why the program's superheavy-soliton dark-matter candidate failed: the corrected count of monopoles formed in the early universe, the mass at which their abundance would match the observed dark matter, the overproduction at the withdrawn manuscript's benchmark mass, the corrected relic window of the hidden sector's light fermion, the dark-radiation bound, and the exclusion of the minimal hidden sector. Before computing any of these it reproduces standard cosmology results that do not depend on the manuscript. It replaced an earlier script, knot_numbers.py, which had checked the manuscript's own claims and had passed a wrong normalization. The candidate it documents is dead; the script keeps the arithmetic of that death reproducible.*

**Status:** Method, in force — the numbers it gates carry [V] in #11 §12: "The [V] numbers here are gated in `verify/soliton_obituary.py`." — runs second in [the gate](/wiki/method/verification/the-gate). It checks the record of a dead claim, [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary). In the run of 2026-10-21 every check passed and the script ended "OK — every number the round-3 record quotes reproduces."

## What it is

The docstring: "every number that review/round3-adjudication.md and the §12 obituary of papers/broken-born-checkpoint-v2.md (v2.1) quote for the withdrawn soliton candidate (#14 v3), recomputed and checked." Root `CLAUDE.md` lists it as "the round-3 record". It cites #11 v2.1; #11 is now v2.2, whose changes do not touch §12 (#11 header).

The candidate was a superheavy ['t Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole) of a hidden gauge sector, proposed as dark matter in manuscript #14 ([the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate)). [Review round 3](/wiki/method/review/round-3) found its abundance estimate misnormalized, and the program retired it on 2026-10-19 ([round-3 decisions](/wiki/method/review/round-3/decisions)). The script is the machine check behind the obituary: it does not test whether the candidate could be revived, only that the numbers the obituary and the rulings state follow from their inputs.

## The model and the constants

The docstring states the model, unchanged from the withdrawn manuscript:

```text
SU(2)_d -> U(1)_d by an adjoint Higgs with vev v; Dirac
doublet psi of dark charge g_d/2 = e (hypothesis H); monopole mass
M = 4 pi f v / g_d, f = 1 (BPS) to 1.787; T_c ~ v. Kibble with one defect per
Hubble volume, the causal minimum. Freeze-out: s-wave, Kolb & Turner eqs.
5.43-5.45. Reference constants: PDG and Planck 2018 values.
```

That is a hidden SU(2) broken to U(1) by a Higgs field in the adjoint representation ([the hidden sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)); a light fermion doublet ψ whose charge equals ours (hypothesis H); a monopole mass set by the vacuum value v, with f between 1 at the Bogomolny–Prasad–Sommerfield (BPS) limit and 1.787; a transition temperature of order v; and monopoles formed by [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) at its minimum rate. The constants in the code include the Planck mass `M_PL = 1.22089e19` and the reduced Planck mass `M_PL_RED = 2.43536e18` (GeV), the present entropy density `S0 = 2891.2` (cm⁻³), the dark-matter density built from Ωh² = 0.120, the fine-structure constant `1/137.035999`, `GSTAR = 100.0` at the transition, and the withdrawn benchmark `M_BENCH = 3e13` (GeV). The docstring names their origin as Particle Data Group (PDG) and Planck 2018 values; the predecessor script's docstring had added that they were "from model memory except the N_eff bound (Planck 2018 VI, live-checked)" (knot_numbers.py at commit 96f58da). Flag 34 in `review/wiki-build-flags.md` notes that the current docstring drops that caveat, although the values are still typed in rather than retrieved.

Two helper functions carry most of the physics. The relic density after freeze-out of an s-wave annihilator of mass m, cross-section σ₀, g internal states and g\* relativistic species is computed by iterating the freeze-out point x_f, and the extra radiation of a species with g_eff effective states at temperature ratio r:

```text
x_f = ln(0.038 g M_Pl m σ₀ / √g*) − ½ ln x_f
Ω h² = 1.07×10⁹ x_f / (√g* M_Pl σ₀)
ΔN_eff = (4/7) g_eff r⁴
```

Both are textbook formulas [T], and both are tested by the anchors before they are used.

## The anchors

"Anchors come first and are independent of the manuscript (a textbook identity; a published value)." There are four, and each tests a formula that the later checks reuse:

- **The Friedmann coefficient.** The check passes when √(8π³/90), rounded to two decimals, equals 1.66, the coefficient of the radiation-era expansion rate H = 1.66 √g\* T²/M_Pl [T]. The script's Hubble coefficient, from which the Kibble normalization p is built, is this number times √g\*.
- **One defect per Hubble volume.** The check passes when the computed p lies between 50 and 200, against the published estimate "n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)"; it prints `[p = 104.31]`. This is the anchor that replaced the circular one ([independent anchors](/wiki/method/verification/independent-anchors)).
- **A standard relic.** The check passes when the freeze-out function, for 100 GeV and σv = 2.2×10⁻²⁶ cm³/s, gives Ωh² between 0.06 and 0.24 ("within x2" of 0.12). It prints no value. It anchors the function used for the ψ window and the W′ overclosure.
- **One extra neutrino species.** The check passes when the dark-radiation function gives ΔN_eff = 1 for one extra neutrino species at the neutrino temperature, to 10⁻¹². It anchors the function used for the ξ bound.

The two window anchors test order of magnitude. The precision comes from the later checks, which compare the same code's output with the figures the record states. The mass formula M\* and the gravitational-wave frequency formula have no separate anchor; they are checked only against the record's figures.

## The rulings it checks

Each block below is the script's output; the [rulings page](/wiki/method/review/round-3/rulings) gives each ruling in full.

### Ruling 1: the Kibble normalization

```text
PASS  p = 104.31 with M_Pl  [104.3106]
PASS  p = 0.828 with reduced M_Pl  [0.8279]
PASS  v3's 0.0228 drops (1.66 sqrt(g*))^3 ~ 4.6e3  [4575.6]
```

The yield of one defect per Hubble volume is n/s = p (T_c/M_Pl)³. The script computes p in both Planck-mass conventions and checks that v3's value equals the correct one divided by (1.66 √g\*)³: the dropped factor. The ruling: "Kibble normalization: one defect per Hubble volume is p ≈ 104, not 0.023", upheld, with "My error came from misremembering the formula." See [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization).

### Ruling 2: the mass and the overproduction

```text
PASS  M* at minimum production = 2.9-4.4e12 GeV  [2.873e+12-4.441e+12]
PASS  the two Planck conventions agree when p is normalized consistently
PASS  the 3e13 benchmark is overproduced 2.1e3-1.2e4 times  [2.08e+03-1.19e+04]
```

The dark charge is fixed by hypothesis H, g_d = 2√(4πα); the ratio r = M/v = 4πf/g_d is evaluated at f = 1 and 1.787. The mass at which the Kibble abundance equals the observed density is computed as M\* = r (ρ_DM M_Pl³/(r p s₀))^{1/4}, and the overproduction at the benchmark as (3×10¹³ GeV/M\*)⁴, the fourth-power scaling of the abundance with mass in that formula. The second check computes M\* at r = 20 in both conventions and requires agreement to 1%, which settles the ruling's point that the manuscript's "reduced-Planck factor of 3" "was not a convention spread". See [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction).

### Ruling 4: the ψ relic window

```text
== psi relic window (ruling 4): psi, psi-bar, both doublet members; sigma v = pi alpha^2/m^2
PASS  10% of the dark matter at 45-49 GeV  [45.2-48.8]
PASS  100% at 146-158 GeV  [146.4-158.0]
```

The script finds, by bisection, the ψ mass at which four times the single-species relic density (ψ, ψ̄ and both doublet members, the factor v3 omitted) equals 0.012 and 0.12, with the exactly known s-wave σv = πα²/m² and g\* = 80 and 106.75 for the two ends. The ruling: "My recount: 10% of the DM at 45–49 GeV, 100% at 146–158 GeV" (DM is dark matter), against v3's "0.1–0.3 TeV". The referee's own Boltzmann integration, "28–46 / 96–153 GeV", is quoted in the ruling and not checked here. See [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window).

### Ruling 5: dark radiation

```text
PASS  95% bound Delta N_eff < 0.286  [0.286]
PASS  xi < 0.760  [0.7601]
PASS  knock-on: GW upper end 3.2e7 Hz at the withdrawn benchmark  [3.17e+07]
```

The bound is formed in the code as 2.99 + 0.34 − 3.044, Planck's upper value less the Standard Model's N_eff of 3.044. Flag 22 in `review/wiki-build-flags.md` notes that the Planck interval is asymmetric (+0.34/−0.33) and that only the +0.34 side enters, so nothing changes. The temperature ratio ξ of the hidden sector to ours is then bounded through a factor that follows both sectors separately at constant entropy until only the dark photon is relativistic, the setup of the worklog's item O2. The third line is a knock-on: the upper end of the gravitational-wave band (the script's label abbreviates gravitational waves) at the withdrawn benchmark, computed with the new ξ bound. See [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history).

### The surviving exclusion: stable W′± overclose

```text
== Minimal adjoint-only sector (survives, benchmark-conditional)
PASS  stable W'+- overclose by 1e16-1e17  [9.5e+15-2.0e+17]
```

In the minimal sector with only the adjoint Higgs, the charged gauge bosons W′± are the lightest dark-charged states and therefore stable. The script takes their mass as α_W M_bench/f with α_W = g_d²/4π, σv = κπα_W²/m² with the annihilation coefficient κ = 1 and 10, three internal states and g\* = 106.75 + 9, and reports twice the single-species relic density over 0.12, over the four combinations of f and κ. The check passes when the smallest and largest round to 10¹⁶ and 10¹⁷. #11 §12 carries it as "its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V]". See [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure).

## What it does not check

The docstring says "every number" the adjudication and the obituary quote, and the closing line says "every number the round-3 record quotes reproduces"; the adjudication's header and its 'Decisions' make the same claim. The checks cover every number #11 §12 tags [V], and the figures the adjudicator computed for rulings 1, 2, 4 and 5. Flag 33 in `review/wiki-build-flags.md` records the difference. Numbers the record quotes from other sources have no check:

- **Referee figures and literature.** Ruling 3's Kibble–Zurek overproduction is the referee's; the adjudicator "did not re-run the referee's Kibble–Zurek integration" (and flag 21 records that the ruling's "1e9" lower end is the Liveoak–Maharana–Wells (LMW) analytic estimate, not the integration). Ruling 4's referee range and the literature bounds of §12 ("≲ 100 PeV" [29S]) are quoted, not computed.
- **Rulings accepted without re-checking.** Rulings 6 and 9 were "Accepted, not re-checked"; rulings 7, 8 and 10–13 rest on literature and reading.
- **The benchmark arithmetic.** 'What survives v3' keeps "The benchmark-conditional arithmetic: flux, densities, σ_T/M, W′ overclosure". Only the last is here; the others' checks were retired with knot_numbers.py ([benchmark arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)).
- **The physics.** A pass shows that the corrected record is internally consistent arithmetic on the stated model. That the model's inputs are the right ones is what round 3 showed a script cannot establish ([Verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

## Where it came from

knot_numbers.py was written to recompute every number of #14 v2, then of v3; at v3 its anchor list included a Kibble check that reproduced v2's own number, and its p was 0.023 ([independent anchors](/wiki/method/verification/independent-anchors#the-circular-anchor-of-round-3)). After round 3 its inputs were corrected, which made the gate fail on v3's claims until v3 was withdrawn ([the gate](/wiki/method/verification/the-gate#how-the-script-list-grew)). The same day it was replaced. The adjudication's 'Decisions' records that knot_numbers.py, which checked v3's claims, "was replaced by `verify/soliton_obituary.py`, which checks every number this record quotes, with independent anchors. The v3 checks are in history at 96f58da." And: "This retires the checks of a withdrawn paper. It does not loosen the gate: the gate verifies what current documents claim, and v3 no longer claims anything."

Two of the four anchors were already in knot_numbers.py before round 3. The worklog records that it "checks its freeze-out formula on a standard relic first: 100 GeV with σv = 2.2×10⁻²⁶ cm³/s gives Ω h² = 0.108", and that for dark radiation "one extra neutrino species at T_ν gives ΔN_eff = 1.000" (`review/v3-worklog.md`, items O1 and O2). The value 0.108 belongs to that script's run; the current script prints no value for this anchor. The other two, the Friedmann coefficient and Gangui's estimate, are round-3 lesson 2's replacement anchors.

## The recorded output

The script's lines from the run of `scripts/check.sh` on 2026-10-21:

```text
== Anchors
PASS  Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl
PASS  one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)  [p = 104.31]
PASS  freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)
PASS  Delta N_eff: one extra neutrino species at T_nu gives 1

== Kibble normalization (ruling 1)
PASS  p = 104.31 with M_Pl  [104.3106]
PASS  p = 0.828 with reduced M_Pl  [0.8279]
PASS  v3's 0.0228 drops (1.66 sqrt(g*))^3 ~ 4.6e3  [4575.6]

== Mass and overproduction (ruling 2)
PASS  M* at minimum production = 2.9-4.4e12 GeV  [2.873e+12-4.441e+12]
PASS  the two Planck conventions agree when p is normalized consistently
PASS  the 3e13 benchmark is overproduced 2.1e3-1.2e4 times  [2.08e+03-1.19e+04]

== psi relic window (ruling 4): psi, psi-bar, both doublet members; sigma v = pi alpha^2/m^2
PASS  10% of the dark matter at 45-49 GeV  [45.2-48.8]
PASS  100% at 146-158 GeV  [146.4-158.0]

== Dark radiation (ruling 5)
PASS  95% bound Delta N_eff < 0.286  [0.286]
PASS  xi < 0.760  [0.7601]
PASS  knock-on: GW upper end 3.2e7 Hz at the withdrawn benchmark  [3.17e+07]

== Minimal adjoint-only sector (survives, benchmark-conditional)
PASS  stable W'+- overclose by 1e16-1e17  [9.5e+15-2.0e+17]

OK — every number the round-3 record quotes reproduces.
```

## Sources

- `verify/soliton_obituary.py` — the docstring, the model, the constants, the anchors and every check described above
- `review/round3-adjudication.md` 'Rulings' (1–13), 'Lessons (now in CLAUDE.md)' (lesson 2), 'What survives v3', 'Decisions' — the rulings it checks and those it does not; the replacement anchors; the retired benchmark checks; the replacement of knot_numbers.py
- `papers/broken-born-checkpoint-v2.md` §12 — the obituary, its [V] numbers and its 'Checks.' line; header — the v2.2 change list
- `review/v3-worklog.md` 'New open items (to compute before v3 states anything about them)' (O1, O2) — the predecessor's freeze-out and ΔN_eff self-checks, κ, the entropy-conserving setup
- Root `CLAUDE.md` 'Layout' — "the round-3 record"
- `review/wiki-build-flags.md` items 21, 22, 33, 34 — ruling 3's attribution; the Planck interval; the claimed coverage; the constants' origin
- Git history: knot_numbers.py at commits 5dbaa82 and 96f58da — the predecessor and its docstring
