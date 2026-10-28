---
title: "Obituary: the square rectangle at the bounce"
weight: 80
status: dead
description: "The chat claim that the universe's position–momentum rectangle is square 'exactly at the bounce': for the radiation it is square only at 4.4×10¹⁴ T_P, before the radiation existed, and most elongated at the turnaround; the Hubble-sphere, two-region, squeezed-mode, string-cosmology and |Z| = 1 readings fail too, and the claim is withdrawn."
provenance: [D, V]
sources:
  - "papers/phase-space-diameter.md §6"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §8.4"
  - "papers/phase-space-diameter.md §9"
  - "verify/phase_space_diameter.py 'Where the radiation rectangle is square, lambda = l_P (note §6)'"
  - "review/round5-adjudication.md 'Rulings' R11, R14, R15"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
  - "review/round5/manuscript-v1.0.md §6"
  - "review/round5/referee-B/audit-notes.md §4.3, §4.5"
  - "review/round5/referee-A/audit-notes.md §4.3"
  - "CLAUDE.md 'Since the handoff'"
  - "HANDOFF.md §4"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "review/wiki-build-flags.md items 23, 24, 27"
  - "review/wiki-build-flags.md items 27 (addendum), 49, 50"
  - "notes/closed-universe.md §2"
  - "notes/closed-universe.md §7"
---

*This page records a dead claim: that the "rectangle" the universe occupies in position and momentum, its extent in position against its extent in momentum, is square "exactly at the bounce". The claim is one clause of the chat-only form of [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), and the summary that records it does not say which bounce it means. The phase-space-diameter note of 2026-10-26 tested every reading it found. For the universe's radiation, the rectangle's length divided by its width, in Planck units, grows as the square of the scale factor: it is about 5×10⁹² today, and it would have been one only at about 10¹⁴ times the Planck temperature, in an epoch before the radiation existed. At the far-future turnaround that the program reads as the [conjugate universe's bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce), the rectangle would be at its most elongated. The other readings fail as well, and the note withdraws the claim. The area relation, and the reading of the aspect ratio as a clock, survive.*

**Status:** Dead (withdrawn) — [D][V] for the withdrawal (`papers/phase-space-diameter.md` §6, §9) — every number the note computes for it is checked by [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script), and the survey of readings went through [round 5](/wiki/method/review/round-5) of blind review, in which referee B added readings that did not change the withdrawal (rulings R14 and R15); listed in [the graveyard](/wiki/status/graveyard). Flag 24 in `review/wiki-build-flags.md`, which recorded that the claim names no bounce, awaits Paul's ruling.

## What was claimed

The claim is the third clause of one bullet of the [handoff document](/wiki/history/documents/handoff), `HANDOFF.md` §4, among the results that exist only in the chat: "rectangle square (D_x = D_p in Planck units) exactly at the bounce". The whole bullet is quoted on the diameter relation's page ([Chat-only: the original statement](/wiki/cosmology/scale-factor-duality/phase-space-diameter#chat-only-the-original-statement)). D_x is the universe's extent in position and D_p its extent in momentum; the bullet's other clauses give their product, h·N^{1/3} per dimension, and read the "aspect ratio today ~10⁹²" as "a clock measuring distance from self-duality".

The bullet defines none of D_x, D_p, N or "the bounce" (note §2). Flag 24 in `review/wiki-build-flags.md` recorded that it does not say which bounce it means, and that if the bounce is the turnaround, the rectangle would be most elongated there; the flag's audit confirmed the point by one independent check.

## What "square" means

"Planck units" means a Born length λ = l_P, the reference length that the program's [dual special relativity](/wiki/conjugate-relativity) takes in #13 §1 ([the Born length](/wiki/phase-space/reciprocity/born-length)). The aspect ratio is then A = (D_x/l_P)/(D_p/m_P c), with m_P the Planck mass, and the rectangle is square when A = 1 (note §6). Born reciprocity keeps a rectangle's area and inverts its aspect ratio, and every rectangle is square for exactly one choice of λ, so "square" says something only once λ is fixed (note §5; [the aspect ratio](/wiki/cosmology/scale-factor-duality/phase-space-diameter#the-aspect-ratio-a-clock-and-a-distance-from-self-duality)). The program's action fixes no Born length; λ = l_P is #13's untagged choice (note §5, §9).

## How it was tested

The note computed the aspect ratio's history for the reading the chat's own numbers fit, the radiation of today's observable universe; for the Hubble-sphere reading; for a two-region reading; for a squeezed mode; and for the record's |Z| = 1 geometry, at every event the record or the literature could mean by "the bounce", including the self-dual bounces of string cosmology (note §6, obituary). The numbers are checked by `verify/phase_space_diameter.py`, section 'Where the radiation rectangle is square, lambda = l_P (note §6)'. Referee B of round 5 found readings missing from version 1.0: the squeezed mode, the early-universe step of the note's §8.4 at the epoch of the square, the convention dependence of the |Z| = 1 geometry and the infinite elongation of the Hubble rectangle at a true bounce (ruling R14), and the self-dual bounces of string cosmology (ruling R15). Version 1.1 adds them, and none changes the withdrawal.

### The radiation of today's observable universe

This is the reading the chat's numbers fit (note §2–§3). For the radiation filling today's observable universe, in Planck units (note §6) [V]:

- today A₀ = 5.2×10⁹² (log₁₀ A₀ = 92.72), matching the chat's "~10⁹²"; ln A₀ = 213.5, so the radiation is 106.7 e-folds of expansion past the moment it would have been square;
- run back with D_x ∝ a and D_p ∝ 1/a, so that A ∝ a², the rectangle is square at a/a₀ = 4.4×10⁻⁴⁷, where T = 4.4×10¹⁴ T_P, T_P being the Planck temperature; counting the Standard Model's g_s = 106.75, its relativistic degrees of freedom counted for entropy, moves this to a/a₀ = 2.5×10⁻⁴⁷ and T = 2.5×10¹⁴ T_P;
- in closed form [D][V], at the square both sides equal √(2πκ) N_γ^{1/6} = 3.28 N_γ^{1/6} in Planck units, and T_sq = 0.61 N_γ^{1/6} T_P, where κ = 1.708 is the relation's coefficient and N_γ the photon count. "A region of N cells can be square only when its quanta carry about N^{1/6} ≈ 10¹⁵ Planck momenta";
- at T = T_P the rectangle is still long by A = 6.4×10²⁸ (Standard Model counting).

**That epoch is not a physical one [T][V].** "Above the Planck temperature there is no tested physics" (note §6). In inflationary cosmology the radiation did not exist then either: it was created at [reheating](/wiki/cosmology/early-universe/inflation-and-dilution#reheating-t), at a temperature no higher than about 5.7×10¹⁵ GeV. That limit assumes instantaneous reheating at the energy scale of inflation allowed by a tensor-to-scalar ratio of primordial perturbations below 0.036 [S: BICEP/Keck 2021], E_inf < 1.39×10¹⁶ GeV [S: Soman et al. 2025]. At reheating A = 2.9×10³⁵, and "Since its creation the radiation rectangle has never been within 35 orders of magnitude of square" (note §6). The note sets beside this the trans-Planckian censorship conjecture, under which no mode may be stretched from below the Planck length to beyond the Hubble radius [S: Bedroya–Vafa 2020], as "a separate constraint of the same kind on how far a mode's cell can move from the self-dual point during accelerated expansion".

### The Hubble sphere

Drawn around the Hubble sphere instead, with D_x = 2c/H for the Hubble rate H, the rectangle is square in the radiation era at T = 0.28 T_P, when the Hubble radius is 0.75 l_P and the sphere holds about 0.45 quanta of all Standard Model species [D][V]. "At the Planck time every scale is Planckian, so this is dimensional analysis rather than a result" (note §6). In this reading the area is not conserved: it grows as N_H^{1/3}, from below one to N_H = 4.4×10⁸⁷ photons today, when the aspect ratio is 1.6×10⁹². At a true bounce, where H = 0, the Hubble rectangle is infinitely elongated.

### Two regions

The chat's four clauses can each be made true by reading the first two, the area and N ~ 10⁹⁰, as statements about today's observable universe, and the last two, the square and the clock, as statements about one Hubble patch (note §6) [D][V]. They then describe different objects. When a Hubble patch was square, at T = 0.28 T_P, today's observable universe was a region about 10³⁰ l_P across made of about 6×10⁸⁹ such patches, and its own rectangle was long by about 8×10²⁹.

### A squeezed mode

Read as the Wigner ellipse of one perturbation mode ([the Wigner function](/wiki/phase-space/reciprocity/wigner-function)), an aspect ratio of 10⁹² is a squeezing of r = 105.9, inside the literature's 100–120 for today's largest scales, and the chat's clock is then the mode's squeezing (note §6) [D][V]; see [squeezed cosmological perturbations](/wiki/cosmology/early-universe/squeezed-perturbations). That reading fits the fourth clause of the claim and not the third: the mode was round before it left the Hubble radius during inflation, which is not a bounce.

### Self-dual bounces in string cosmology

String cosmology has bounces at self-dual points, "the most natural source of the phrase" (note §6) [T][V]. Its [scale-factor duality](/wiki/cosmology/scale-factor-duality/cosmological-constraint#the-name-scale-factor-duality-t) maps a(t) to a⁻¹(−t), and the big bang becomes "an instant of maximal curvature" between the two branches [S: Veneziano 1991; Gasperini–Veneziano 1993]; in string-gas cosmology the temperature is symmetric under R → 1/R about the self-dual radius [S: Brandenberger–Vafa 1989; Brandenberger 2008]. There the self-dual point is in string units, for a compact radius or for the scale factor itself, not for the radiation rectangle in Planck units. At a string-scale bounce, k_BT = 10¹⁷ GeV, the observable universe's radiation rectangle would still be long by A = 9.5×10³².

### At the turnaround

A ∝ a² is largest where a is (note §6) [D]. If the expansion turns around, the turnaround is the moment of greatest elongation, not a square; for the Hubble box H → 0 there, and A → ∞. The program reads that turnaround, through ã = 1/a, as the conjugate description's bounce ([#11](/wiki/history/documents/checkpoint) §10; [the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)). The note also records the premise problem of that page: the potential the program writes for its dark-energy field, V₀[1 + cos(τ/f)], is never negative for V₀ > 0, and so, in the spatially flat universe the program's cosmology assumes, it produces no turnaround as written; a closed universe can turn around without negative energy (note §6; round-5 ruling R11). The record leaves this unresolved: flag 27 in `review/wiki-build-flags.md`, and [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign). The flag's addendum (2026-10-27) finds that with this potential the turnaround needs a closed universe. Ruling R11's statement is true but omits two conditions, a_max ≥ Ω_m/|Ω_k| and, at H = 0, ρ_m + 2ρ_r + 4K − 2V ≥ 0, with K τ's kinetic energy density, and the mechanism is published (Barrow 1987 †; Tipler et al. [S]) (flag 50; [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#the-conditions-dv)). The closed-universe note also finds the turnaround's aspect ratio, pairing the radius with the total mass, to be the closed Friedmann equation at H = 0, and the obituary stands ([the radius–mass pairing](/wiki/cosmology/scale-factor-duality/closed-universe#the-dual-frame-what-closure-fixes-and-what-it-does-not)).

### The early-universe step

The note's §8.4 finds a related epoch [D][V]. If reciprocity fixes the dual Planck mass M̃ to equal M_P, the optional a⁻⁶ step in the Friedmann equation, the subject of [row 10](/wiki/predictions/early-universe-step) and a term derived in no document (flag 49), sits at the self-dual epoch, which depends on λ and on the comoving scale reciprocity treats as unit. For λ = l_P and the radiation of today's observable universe it is the 10¹⁴ T_P of the square, "which is not a bounce (H² > 0 throughout)". Ruling R14 lists this among the readings version 1.0 had missed. The closed-universe note adds that only vM̃²C³ and vM̃²k̃C are physical, so "M̃ = M_P" constrains nothing unless the comoving unit C is fixed, and that with the record's normalization the self-dual point a = ã is never reached after inflation begins ([the dual frame](/wiki/cosmology/scale-factor-duality/closed-universe#the-dual-frame-what-closure-fixes-and-what-it-does-not)).

### The record's |Z| = 1 geometry

One reading reproduces the claim exactly, and the note tests it as the claim's probable origin: the record's identification of a·ã = 1 with the circle |Z| = 1 of the [modular field](/wiki/phase-space/modular-field/modular-field-z). It is set out in the section on where the claim probably came from, below. The identification fails under either convention for how the scale factor sits in Z (ruling R14).

## Why it failed

The note's verdict (§6, obituary):

- In the reading the numbers fit, the rectangle is square only at about 10¹⁴ T_P, before the radiation existed; since reheating it has been elongated by at least 10³⁵.
- At the program's turnaround it is at its most elongated.
- In the Hubble reading it is square at the Planck time, a statement about the Planck time, not about any bounce.
- A squeezed mode matches the number 10⁹² but was round before it left the Hubble radius, not at a bounce.
- At a string-scale bounce the rectangle is still long by 10³³.
- The record's |Z| = 1 geometry, which would make the claim exact, contradicts the measured aspect ratio.

In the note's plain-language summary: "No reading puts a square rectangle of 10⁹⁰ cells at any bounce, so the early-chat claim is withdrawn" (§6). The root `CLAUDE.md` records the outcome in 'Since the handoff': "'square exactly at the bounce' is withdrawn (obituary in §6)".

## Where the claim probably came from

This section is the note's inference, tagged [D, inference] (§6). "The record holds no transcript of the chat."

**The reading that reproduces the claim.** #11 identifies the cosmological constraint a·ã = 1 with the circle |Z| = 1 (#11 §6, §10). Along that circle, written Z = tanh s + i sech s, Im Z peaks at Z = i. With the record's a² = Im Z, the peak is the maximum of a, the turnaround, and the phase-space metric H is round there. With the wave-packet convention of the note's §5, in which Im Z falls as a⁻², the same point is a minimum of a, a literal bounce. Under that identification "square exactly at the bounce" and "a clock measuring distance from self-duality" both follow, with the bounce at the turnaround.

**Why the reading fails [V].** "The identification fails in two ways" (note §6):

1. On |Z| = 1 the position and momentum extents are equal at all times (H_xx = H_pp = 1/Y), which contradicts the measured aspect ratio of 10⁹².
2. If the 10⁹² is read instead as the squeeze of H along the circle, it requires X ≈ 1 today: a homogeneous [momentum graviton](/wiki/gravity/momentum-graviton) whose energy density, of order M̄_P² M_X² X² with M̄_P the reduced Planck mass and M_X the graviton's mass, exceeds the critical density by a factor of order (M_X/H₀)² ≈ 10⁶¹ for the smallest M_X allowed by the note's §8.2. The script prints 1.3×10⁶¹ for M_X c² = 5.2 meV, the smallest mass that [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound) allows in the program's aligned vacuum.

**The flag.** The identification is the one that flag 23 in `review/wiki-build-flags.md` queries: on the vacuum slice X = 0, a·ã = 1 holds along the whole imaginary axis, as the content of det H = 1, while |Z| = 1 meets that axis only at Z = i ([the |Z| = 1 locus](/wiki/cosmology/scale-factor-duality/cosmological-constraint#the-geometry-the-z--1-locus)). For wave packets the note reads |Z| = 1 as the set of square rectangles and Z = i as the self-dual point ([Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states)). The round-5 adjudication recommends that Paul accept flags 23 and 24, since "a·ã = 1 is det H = 1 on the whole slice X = 0; |Z| = 1 is the locus of square rectangles; Z = i is the self-dual point; and the diameter relation's square is not at the turnaround" ('Recommendations to Paul'). Both flags await his ruling, and the wiki does not rule on them.

## What survives

- **The area relation**, as standard physics (note §3): the radiation of a fixed comoving region keeps D_x·D_p = κ h N_γ^{1/3}. See [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter).
- **The aspect ratio as a clock** of e-folds and as a distance on the Siegel half-plane (note §5), today 213.5 per axis from the self-dual point in Planck units. See [the aspect ratio](/wiki/cosmology/scale-factor-duality/phase-space-diameter#the-aspect-ratio-a-clock-and-a-distance-from-self-duality) and [Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states).
- **The turnaround as the conjugate bounce** is a separate claim, not touched by this obituary: it concerns the two scale factors, not the rectangle's shape (the wiki's reading), and its status comes from #11 §10 and flag 27 ([the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)).

## Where it is filed

- Home of the claim: [the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter), in [scale-factor duality](/wiki/cosmology/scale-factor-duality).
- The calculation that killed it: `papers/phase-space-diameter.md` §6, checked by `verify/phase_space_diameter.py` ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)).
- The review: [round 5](/wiki/method/review/round-5), rulings R11, R14 and R15.
- The register of dead claims: [the graveyard](/wiki/status/graveyard).
- The flags: items 23, 24 and 27 in `review/wiki-build-flags.md`, awaiting Paul's ruling.
- How the program treats dead claims: [negative results and dead claims](/wiki/method/negative-results).

## History

- **Chat era, before 2026-10-19.** The claim, as one clause of the diameter relation.
- **`HANDOFF.md` §4 (2026-10-19).** Recorded among the chat-only results, "Conjecture-tier; candidate for a future note".
- **Wiki build (2026-10-21 to 2026-10-22).** Flag 24 records that the claim names no bounce and that the rectangle would be most elongated at the turnaround; the audit confirmed it.
- **The note, version 1.0 (2026-10-26).** The obituary in §6, with the radiation, Hubble-sphere, two-region and |Z| = 1 readings (`review/round5/manuscript-v1.0.md` §6).
- **Round 5 and version 1.1 (2026-10-26).** Referee B added the squeezed mode, the §8.4 step, the convention dependence of the |Z| = 1 geometry and the infinite Hubble elongation at a true bounce (R14) and the string-cosmology bounces (R15); referee A added the flatness qualification on the turnaround (R11). The withdrawal stands.

## Sources

- `papers/phase-space-diameter.md` §6 — every reading, its numbers, the obituary and the probable origin [D, inference]
- `papers/phase-space-diameter.md` §5 — what "square" and "self-dual" mean for a rectangle and for wave packets; the program's free Born length
- `papers/phase-space-diameter.md` §8.4 — the a⁻⁶ step's self-dual epoch, which is the square and not a bounce
- `papers/phase-space-diameter.md` §9 — the summary row "withdrawn" and its tags
- `verify/phase_space_diameter.py` 'Where the radiation rectangle is square, lambda = l_P (note §6)' — the numbers of every reading
- `review/round5-adjudication.md` 'Rulings' R11, R14, R15 — the flatness qualification; the readings and prior art added in review, none of which changes the withdrawal
- `review/round5-adjudication.md` 'Recommendations to Paul' — the recommendation on flags 23 and 24
- `review/round5/manuscript-v1.0.md` §6 — the reviewed version 1.0 and the four readings it tested
- `review/round5/referee-B/audit-notes.md` §4.3, §4.5, `review/round5/referee-A/audit-notes.md` §4.3 — which referee raised which reading: referee B the squeezed mode, the §8.4 step, the Hubble rectangle at a true bounce and the |Z| = 1 convention (§4.3) and the string-cosmology bounces (§4.5); referee A the flatness qualification
- `CLAUDE.md` 'Since the handoff' — the claim withdrawn
- `HANDOFF.md` §4 — the claim as recorded
- `papers/broken-born-checkpoint-v2.md` §6, §10 — a·ã = 1 as the |Z| = 1 locus, and the turnaround read as the conjugate bounce
- `review/wiki-build-flags.md` items 23, 24, 27 — the |Z| = 1 identification, the unnamed bounce, and the sign of V(τ); all await Paul's ruling; item 27's addendum and items 49 and 50 — the turnaround in a closed universe, the underived dual term, and R11's omitted conditions and prior art
- `notes/closed-universe.md` §2 — the turnaround's conditions and prior art; §7 — the dual frame and the radius–mass pairing
