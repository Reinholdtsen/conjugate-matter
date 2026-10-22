---
title: "The conjugate universe: one state, two descriptions"
weight: 40
status: alive
description: "The 'conjugate universe' is the momentum-space description of the one physical state, related to ours as a spectrum to its waveform and synchronized rather than causally linked; the popular articles' 'other observers' speculation, quarantined."
sources:
  - "papers/broken-born-checkpoint-v2.md App. A items 2, 4, 6–9"
  - "papers/broken-born-checkpoint-v2.md §6"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 rows 4–5"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §7"
  - "popsci/universes-other-half.md 'Two descriptions of one thing'"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
  - "popsci/universes-other-half.md 'The other observers'"
  - "popsci/angle-of-the-mirror.md 'Dividends and daydreams'"
---

*In the current program the conjugate universe is a second description of our universe rather than a second world: the description of the one physical state in momentum variables, related to the ordinary description as a sound's spectrum is related to its waveform. It began as one of the program's founding suppositions, a second universe organized around momentum and existing alongside ours. Two derived relations turned it into a second description. The constancy of Planck's constant fixes the size of a cell of phase space, so as our universe expands its momentum-space description contracts by the same factor; and a derived translation rule says how energy described on the momentum side acts on our expansion. The two descriptions are synchronized rather than causally linked, so an event in one is the same event read in the other, which is how the program reads its predicted far-future halt and reversal of our expansion as a bounce of the conjugate universe. The idea that observers might live in the momentum description appears only in the popular articles and has no status in the program.*

**Status:** Alive, transformed — the fate [#11](/wiki/history/documents/checkpoint) Appendix A gives founding supposition 2, without a tag. The relations that carry it, the cosmological constraint a·ã = 1 and the corrected duality dictionary, are derived [D] (#11 §10; first derived in the [lab notebook](/wiki/history/documents/lab-notebook), #1 §6) and are not machine-checked. The "other observers" speculation is popsci-only and has no status.

## What the phrase means now

The conjugate universe entered the program as founding supposition 2, P.R.'s "A coexisting conjugate universe". The checkpoint's audit gives its fate as "alive, transformed: one state, two ledgers" (#11 App. A item 2). The wiki writes "two descriptions" for #11's "two ledgers", as [the handoff](/wiki/history/documents/handoff) does ("one event, two descriptions", `HANDOFF.md` §2). What was imagined as a second universe existing beside ours is now the same physical state described in momentum variables instead of position variables.

A companion supposition says how the two are related. Founding supposition 8, "Synchronized, not causal; Fourier/holography", has the fate "alive (the dictionary); holographic tie loosened, echoed in τ's boundary residence" (#11 App. A item 8). Both fates rest on the cosmology of #11 §10, described below. The audit as a whole is on [founding suppositions and their fates](/wiki/program/founding-suppositions).

## Two descriptions of one state

For a single particle the idea is standard quantum mechanics [T]. The particle's state can be written as a wavefunction of position or as a wavefunction of momentum, and the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform) converts one into the other exactly. The popular article #12 states the picture the program builds on: "A particle's description in terms of position and its description in terms of momentum are two complete readings of one underlying state, related by the same Fourier transform that relates a waveform to its spectrum." Neither reading is more real than the other, as neither the waveform nor the spectrum of a chord is the more real recording.

The program applies the same reading to cosmology. The lab notebook describes the universe with two scale factors, "x-space scale factor a and p-space scale factor ã" (#1 §6): a measures how distances in position space grow, and ã how the corresponding scales in momentum space change. The "conjugate universe" is the universe described by ã.

## One motion read in two variables

The two scale factors are not independent. The lab notebook derives the relation from the rigidity of the [symplectic form](/wiki/phase-space/reciprocity/symplectic-form), which in the program's [hard core](/wiki/program/hard-core) is the statement that Planck's constant does not change: "Rigidity of ω means the comoving phase-space cell has fixed volume: with x-space scale factor a and p-space scale factor ã, each mode occupies (aã)³ × (comoving cell) = ℏ³" (#1 §6). Hence:

```text
(a·ã)³ × (comoving cell) = ℏ³      ⇒      a·ã = const ≡ 1
```

"This is not an extra assumption; it is the statement that ℏ does not run" (#1 §6). #11 §10 states the result as derived: "ω-rigidity fixes the comoving phase-space cell: a·ã = 1 (ℏ does not run) — the |Z| = 1 self-dual locus" [D]. The last phrase places the relation in the [modular field](/wiki/phase-space/modular-field/modular-field-z) Z = X + iY, on which [reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) acts as Z → −Z⁻¹; "at X = 0 it is scale-factor duality g → g⁻¹, and the cosmological constraint a·ã = 1 (§10) is the |Z| = 1 locus" (#11 §6; [reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion)). The identification of a·ã = 1 with the |Z| = 1 locus is queried in flag 23 of `review/wiki-build-flags.md`. The full treatment is on [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint).

The relation turned founding supposition 6, "Conjugate universe shrinks as ours expands", into a theorem: "promoted to theorem (a·ã = 1 from ℏ-rigidity; the |Z| = 1 locus)" (#11 App. A item 6; on the |Z| = 1 locus, see flag 23 in `review/wiki-build-flags.md`). In signal terms it is the familiar trade between a waveform and its spectrum: stretching a signal in time compresses its spectrum by the same factor [T]. #12 glosses it with the cosmological redshift: "Cosmic expansion stretches every wavelength — the redshift — which, read in the momentum description, means every momentum in the universe is shrinking … That is not a second process running alongside expansion; it is expansion, read in the other variable." The gloss is the popular article's; the derived statement is a·ã = 1.

## Synchronized, not causal: the duality dictionary

Because ã = 1/a holds at every moment, the momentum description does not evolve on its own: a change seen in one description is the same change seen in the other, which is the sense of "synchronized, not causal". What remains to be specified is how energy described on the momentum side shows up in ours. That rule is the [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary), and it is what the audit means by "alive (the dictionary)" for supposition 8.

A fluid with equation of state w, the ratio of its pressure to its energy density, dilutes in an expanding universe as ρ ∝ a^(−3(1+w)) [T] ([Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)). The lab notebook applies this to a fluid at rest in the momentum-space frame, with equation of state w̃, and translates its energy into our frame through the constraint (#1 §6):

```text
ρ̃ ∝ ã^(−3(1+w̃))                       a fluid in the dual frame
E = ρ̃ ã³ ∝ ã^(−3w̃) = a^(3w̃)            its energy, using ã = 1/a
ρ_eff = E / a³ ∝ a^(−3(1−w̃))           as it enters our Hamiltonian constraint
⇒   w_eff = −w̃
```

#11 §10 tags the result "[D — corrected en route]": "with one shared lapse, a dual-frame fluid contributes w_eff = −w̃", superseding an earlier −2 − w̃ because "the constraint's Jacobian changed the answer". The lab notebook describes the error in the earlier heuristic as having "identified densities across frames without the constraint's volume Jacobian" (#1 §6). The translations, with the equations of state from the notebook's table:

| Dual-frame content | Equation of state w̃ | Acts on our expansion as | w_eff |
| --- | --- | --- | --- |
| kinetic or stiff energy | +1 | a cosmological constant | −1 |
| a cosmological constant | −1 | a stiff fluid, dying as a⁻⁶ | +1 |
| spatial curvature | −1/3 | dark radiation, negative for a closed dual space | +1/3 |
| dust | 0 | dust | 0 |

#11 §10 adds that "the dual Einstein term is an a⁻⁶ step in G_eff", an optional early-universe signature ([row 10](/wiki/predictions/early-universe-step)). #11 §15 counts the corrected dictionary as one of the two forced corrections that sharpened the hard core ([assessment](/wiki/program/assessment)).

## One event, two descriptions: the turnaround

Founding supposition 7, "Our expansion reverses at their bounce", has the fate "alive, corrected: one event, [two descriptions]; live at DESI DR3" (#11 App. A item 7, with the wiki's wording in brackets), where DESI DR3 is Data Release 3 of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi). The program predicts that our expansion eventually halts and reverses if the potential energy of the dark-energy field τ ([hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)) becomes negative. Through a·ã = 1 that moment, the largest our universe gets, is the moment the momentum description is smallest, so the same event, read in momentum variables, is a contracting universe reaching its minimum and rebounding. The lab notebook: "the same event, read through aã = 1, is the conjugate frame's bounce: our maximum is their minimum. One event, [two descriptions] — now as a constraint identity rather than a metaphor. [D]" (#1 §7). #11 §10: "The turnaround is the conjugate bounce by constraint identity." The page for the claim is [the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce).

Two qualifications go with it:

- **The sign of the potential.** The documents write τ's potential as V = V₀[1 + cos(τ/f)], which is never negative for V₀ > 0, while the turnaround needs it to go negative. No document resolves the conflict (see flag 27 in `review/wiki-build-flags.md`; [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)).
- **The horizon.** [Row 5](/wiki/predictions/fate-of-expansion) of #11's predictions table, "Turnaround = conjugate bounce", is "(Long horizon; near-term test is row 4)". [Row 4](/wiki/predictions/dark-energy-drift) is the thawing drift of dark energy that DESI is testing; Data Release 2 already "favors a crossing above z ≈ 0.4", against the framework's strict [w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) (#11 §13; [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).

## What died: collapse as the source of acceleration

Founding supposition 9, "Their collapse is our acceleration", gave the conjugate universe a causal role: its gravitational collapse would drive our accelerating expansion. Its fate is "dead twice (w = −2 falsified; corrected dictionary removed the mechanism)" (#11 App. A item 9). The handoff gives the two deaths: "first version gave w = −2 (falsified); corrected dictionary removed the mechanism (dual dust ↦ dust)" (`HANDOFF.md` §2). Under the derived rule, collapsing dust on the momentum side acts on our expansion as ordinary dust, which decelerates it; in the lab notebook's words, "dual matter no longer masquerades as exotic energy (dust maps to dust — the w=−2 pathology is gone because it was an artifact)" (#1 §6). The claim stays dead: [Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion).

## Holography: a loosened tie

The second half of supposition 8 linked the two descriptions holographically. In physics, holography is the encoding of the physics of a region in degrees of freedom on its boundary [T]. The audit records that tie as "loosened, echoed in τ's boundary residence" (#11 App. A item 8): the dark-energy field τ lives on a boundary, since "Λ(d) is the Shilov boundary of the Siegel domain [T]; the dark-energy field τ is the Maslov phase of the boundary variable" (#11 §6; [τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase)). No document in the repository develops the holographic tie further.

## What remains open

- **The turnaround's premise.** The sign of V(τ), above.
- **What sources dark energy.** The dictionary maps dual kinetic energy to a cosmological constant, so the lab notebook named "kinetic energy in the dual frame" the natural source of a near-constant dark energy (#1 §6), and then identified dark energy with the potential energy of τ (#1 §7). No document derives the second from the first ([Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link)).

## Popsci-only: the other observers

The popular article #12 offers a speculation in its section 'The other observers': "If the momentum-polarized sector includes complex structures — a possibility the framework permits but does not require — observers there would perceive the world through momentum rather than position. Their sky would be a map of velocities." It ends: "Each polarization is the other's dark sector." #10 gives the same picture as "one paragraph of licensed daydreaming", in which beings of conjugate matter "would see motion rather than place", and closes: "We are each other's dark sector — which was, give or take the mathematics, the engineer's hunch on day one."

Neither #11 nor [#13](/wiki/conjugate-relativity) states or analyses the idea, and the popular articles are never a source for a claim's status, so it has none. The nearest entries in the record concern how conjugate matter is arranged: it clusters in position like any dark matter ("x-clumping", #11 App. A item 4; [conjugate matter and the velocity gate](/wiki/dark-matter/conjugate-matter)), and momentum-space clumping is dead as dynamics ([Obituary: velocity clumping, the founding image](/wiki/dark-matter/momentum-clumping/founding-image)). The speculation is listed with the other popsci-only claims in [conjectures](/wiki/status/conjectures), and the articles are described on [the popular articles](/wiki/history/documents/popular-articles).

## Sources

- `papers/broken-born-checkpoint-v2.md` App. A items 2, 4, 6–9 — the founding suppositions behind the idea and their fates
- `papers/broken-born-checkpoint-v2.md` §10 — the constraint a·ã = 1, the corrected dictionary and the turnaround as the conjugate bounce; §6 — the |Z| = 1 locus and τ on the Shilov boundary; §13 rows 4–5 — the near-term test and the long horizon
- `HANDOFF.md` §2 — "one event, two descriptions"; the two deaths of the collapse mechanism
- `notes/broken-born-theory.md` §6 — the derivations of a·ã = 1 and w_eff = −w̃, and the dictionary table; §7 — the turnaround read through a·ã = 1 (lab notebook, superseded as reference; the results are carried by #11 §10)
- `popsci/universes-other-half.md` 'Two descriptions of one thing', 'Dark energy as the orientation of the split' — the waveform–spectrum picture and the redshift gloss; 'The other observers' — the popsci-only speculation (popular article; not a status source)
- `popsci/angle-of-the-mirror.md` 'Dividends and daydreams' — the same speculation, offered as daydreaming (popular article)
