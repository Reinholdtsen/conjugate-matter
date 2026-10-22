---
title: "Row 10: an early step in G_eff"
weight: 110
status: alive
description: "Two optional early-universe imprints of the dual gravitational sector: an a⁻⁶ step in the effective gravitational coupling before nucleosynthesis, and negative dark radiation (ΔN_eff < 0) if the dual space is closed; their sizes are free parameters, so data bound them rather than kill the program."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 10"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "review/round3-adjudication.md 'Rulings' ruling 5"
  - "review/round3/referee/audit-notes.md Step 1, citation [23]"
  - "notes/knot-dark-matter-standalone.md §4"
  - "review/wiki-build-flags.md item 22"
  - "review/wiki-build-flags.md item 32"
  - "verify/soliton_obituary.py dark radiation"
---

*Row 10 describes two possible imprints of the program's dual, momentum-side gravitational sector on the early universe. The first is a step in the effective strength of gravity, G_eff: the dual sector adds to the square of the effective Planck mass a term that grows toward the past as the sixth inverse power of the cosmic scale factor, a⁻⁶, so it matters only at early times, before the light elements formed in Big Bang nucleosynthesis. The second is negative dark radiation: if the dual space is closed, its curvature acts on our expansion like radiation of negative energy, which lowers the effective number of neutrino species, N_eff. Both follow from the lab notebook's calculation with the [cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint) a·ã = 1. The step is optional and the dark radiation conditional on a closed dual space, and their sizes are free parameters (knobs), so a null result bounds the knobs rather than killing the program; #11 names the cosmic microwave background experiment CMB-S4 as the probe.*

**Status:** Alive, optional and knob-bounded — [D] (the lab notebook's minisuperspace calculation and dictionary, #1 §6; #11 §10's dictionary is [D — corrected en route]) — not machine-checked; no document compares either imprint with data.

## The row

[Checkpoint #11](/wiki/history/documents/checkpoint) §13, row 10:

| Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- |
| Early universe | Standard G, N_eff | Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff | (Knob-bounded; CMB-S4 probes) |

G is Newton's constant and G_eff the effective gravitational coupling in the expansion equation. N_eff is the effective number of neutrino species and ΔN_eff its departure from the standard value. CMB-S4 is a proposed ground-based experiment on the cosmic microwave background (CMB) [T]; whether it is still going ahead is unchecked (flag 32 in `review/wiki-build-flags.md`). The kill column is a parenthesis: the row names no result that would end a claim.

## The observables [T]

Two measurements of the early universe bear on the row ([the radiation era: thermal history and N_eff](/wiki/cosmology/early-universe/radiation-era)):

- **The expansion rate during nucleosynthesis.** In the first minutes, the ratio of neutrons to protons freezes when the weak reactions that convert them become slower than the expansion. A faster expansion freezes it earlier, leaves more neutrons and so more helium. The primordial helium abundance therefore measures the expansion rate H during Big Bang nucleosynthesis (BBN), and H depends on both the radiation content and the strength of gravity [T] ([how N_eff is measured](/wiki/cosmology/early-universe/radiation-era#how-neff-is-measured-t)).
- **N_eff.** The radiation of the universe after electron–positron annihilation is photons and three neutrino species. N_eff measures the energy density of all light species other than photons, in units of one neutrino species; extra light particles raise it, and the [cosmic microwave background](/wiki/cosmology/early-universe/radiation-era#how-neff-is-measured-t) measures it through the expansion history before recombination [T].

## The standard expectation

"Standard G, N_eff" (#11 §13): Newton's constant has the same value in the early universe as now, and N_eff takes the value of the Standard Model's three neutrinos, a little above 3. The round-3 record uses 3.044 for it (ruling 5) [T].

## The Broken-Born requirement

Both imprints come from the lab notebook's cosmology, which rests on two results of [scale-factor duality](/wiki/cosmology/scale-factor-duality).

### The constraint a·ã = 1

The program describes the universe with two scale factors, a for position space and ã for momentum space. Rigidity of the symplectic form fixes the volume of a comoving cell of phase space, so (#1 §6, [D]): "each mode occupies (aã)³ × (comoving cell) = ℏ³", and a·ã = const ≡ 1, "the statement that ℏ does not run" ([the derivation](/wiki/cosmology/scale-factor-duality/cosmological-constraint#the-derivation)). ã is therefore not an independent variable: wherever it appears, it can be replaced by 1/a. Quotations from #1 on this page are transcribed from its LaTeX.

### The a⁻⁶ step in G_eff

The notebook adds the dual sector's own gravitational term to the minisuperspace description of the universe, in which gravity is reduced to the scale factor and the lapse (#1 §6, [D]): "With one shared lapse N and dual Planck mass M̃, substituting ã = 1/a into the dual Einstein–Hilbert kinetic term" — the term ã(dã/dt)², which the substitution turns into ȧ²/a⁵ — "gives"

```text
3H²(M_P² + M̃² a⁻⁶) = ρ
```

where H is the expansion rate and ρ the energy density. Without the M̃ term this is the ordinary Friedmann equation. The steps are on [Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#the-programs-extension-a-second-scale-factor).

What the term means, in the notebook's words: "The dual gravitational sector is **not** a new fluid and **not** a ghost — ã was never independent — but a stiff-like (a⁻⁶) modification of the effective Planck mass, relevant only at early times. It predicts a step in G_eff before BBN and, conditionally on its one knob, a spectral step in the primordial gravitational-wave background. **[D]**"

The wiki's reading of the equation: the bracket is an effective Planck mass squared, and the effective strength of gravity is inversely proportional to it. The dual term grows toward the past as a⁻⁶, so at early enough times it dominates the bracket and gravity is weaker than today; as a grows, M_P² takes over and the ordinary Friedmann equation returns. The passage between the two regimes is the "step". The notebook gives neither the step's size nor its time, beyond "before BBN"; M̃ is free. #11 §10 keeps the result in one clause, "the dual Einstein term is an a⁻⁶ step in G_eff" ([the dual gravity term](/wiki/cosmology/scale-factor-duality/duality-dictionary#the-dual-gravity-term)).

"Not a ghost" is a minisuperspace statement. The notebook records that "no Boulware–Deser sector arises in minisuperspace" [D] and that "The statement for full inhomogeneous H is open" [O] (#1 §4). That accounting predates the notebook's v0.4 addendum, after which the momentum-space partner of the metric is a massive spin-2 field ([the momentum graviton X](/wiki/gravity/momentum-graviton)).

### Negative dark radiation from a closed dual space

The second imprint comes from the [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary), which translates content of the dual frame into its effect on our expansion. The notebook's derivation (#1 §6, [D]): a fluid comoving in the dual frame with equation of state w̃ has density ρ̃ ∝ ã^{−3(1+w̃)} and energy E = ρ̃ã³ ∝ ã^{−3w̃} = a^{3w̃}; entering our expansion as ρ_eff = E/a³ ∝ a^{−3(1−w̃)}, it acts as a fluid with

```text
w_eff = −w̃
```

Spatial curvature behaves like a fluid with w̃ = −1/3 [T], so curvature of the dual space acts on our side as w = +1/3, the equation of state of radiation. The notebook's table: "Spatial curvature (w̃ = −1/3)" appears as "Dark radiation (w = +1/3; closed dual space ⇒ *negative* ΔN_eff)" ([the table](/wiki/cosmology/scale-factor-duality/duality-dictionary#the-table)). The sign comes from the curvature: in the Friedmann equation the curvature of a closed space enters with the opposite sign to an energy density, so read as a fluid it has negative energy density [T], and the dictionary carries that sign across. Extra radiation raises or lowers N_eff according to its sign, so a closed dual space gives ΔN_eff < 0. The table singles out the closed case, and no document discusses an open dual space ([row 10 on the radiation-era page](/wiki/cosmology/early-universe/radiation-era#row-10-negative-δneff-from-a-closed-dual-space)).

#11 §10 keeps it as "dual curvature ↦ negative dark radiation", with the dictionary tagged "[D — corrected en route]": the rule w_eff = −w̃ superseded an earlier heuristic, −2 − w̃, which identified densities across the two frames without the constraint's volume factor ([Superseded: the earlier heuristic rule](/wiki/cosmology/scale-factor-duality/duality-dictionary#superseded-the-earlier-heuristic-rule)).

### Optional, and bounded by knobs

The notebook's parameter table counts the dual geometric sector separately (#1 §10):

| Sector | Parameters | Phenomena covered |
| --- | --- | --- |
| Geometry | M̃, k̃ (2, optional) | Early-G step, ΔN_eff, a gravitational-wave step |

The last entry is paraphrased; the notebook abbreviates it. M̃ is the dual Planck mass. k̃ is not defined in the notebook; written beside the dual curvature, it reads as the curvature of the dual space (the wiki's reading). Both can be zero: with M̃ = 0 there is no step, and with a flat or open dual space no negative dark radiation. "Knob-bounded" means that measurements consistent with the standard values bound M̃ and k̃ rather than refute the program; v0.1 and v1 wrote "Bounds constrain knobs" (#1 §9; #9 §9).

## What kills it

Nothing in the row: "(Knob-bounded; CMB-S4 probes)". A measurement of standard G and N_eff is consistent with the row at small M̃ and k̃, and the documents name no values of the knobs that the program expects, so a result within the standard values bounds the knobs without counting against the program. What the row looks for is a step in the expansion rate before nucleosynthesis or a negative ΔN_eff.

## The data situation

No program document compares either imprint with a measurement, and none computes the size of the step or of the negative ΔN_eff for any value of the knobs.

Apart from the notebook's ±0.03 for CMB-S4 (below), the N_eff figures in the record belong to the retired soliton candidate, whose hidden photon would have added positive dark radiation ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). The round-3 referee checked the Planck 2018 interval against its source, Planck's combination of its own data with baryon-acoustic-oscillation measurements at 95% confidence: "N_eff = 2.99 +0.34 -0.33" (`review/round3/referee/audit-notes.md`, Step 1, citation [23]; #14 had written "2.99 +- 0.34", `review/wiki-build-flags.md` item 22). With the Standard Model value 3.044, ruling 5 put the 95% bound on extra radiation at ΔN_eff < 0.286, which the gate checks:

```text
PASS  95% bound Delta N_eff < 0.286  [0.286]
```

These figures bound positive ΔN_eff for a different proposal; no document applies them to row 10.

#11 names CMB-S4 as the probe and gives no sensitivity. #11 §15 names rows 1, 4 and 7 as the program's near-term falsification exposure; row 10 is not among them.

## Superseded: the spectral step and the ±0.03 target

The lab notebook's row 10 (#1 §9) required an "a⁻⁶ step in G_eff; optional negative ΔN_eff from closed dual curvature", together with a conditional step in the spectrum of primordial gravitational waves, and its kill column read "(Bounds constrain knobs; CMB-S4 N_eff at ±0.03 probes the curvature term)". The ±0.03 figure appears only in #1, and no document or script checks it.

v1 (#9 §9) changed the row in three ways, and #11 kept v1's form:

- it dropped the spectral step in the gravitational-wave background;
- it dropped the ±0.03 target, reading "(Bounds constrain knobs; CMB-S4 probes)";
- it moved "optional" from the dark radiation to the step: "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff". v1's cosmology section calls the step "an optional early-universe fingerprint" (#9 §8).

#11 changed only the kill column's first words, from "Bounds constrain knobs" to "Knob-bounded". No document says why the spectral step and the target were dropped. The mechanism the notebook implies for the spectral step is discussed on [the dropped spectral step](/wiki/cosmology/early-universe/phase-transition-gravitational-waves#the-dropped-spectral-step-row-10), and the whole table's history on [the history of the predictions table](/wiki/predictions/table-history).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 10 — the row; §10 — the dictionary [D — corrected en route] and "the dual Einstein term is an a⁻⁶ step in G_eff"; §15 — the near-term rows
- `notes/broken-born-theory.md` §6 — the constraint, the minisuperspace equation, the a⁻⁶ step and the dictionary table [D]; §4 — the minisuperspace ghost accounting; §9 — v0.1's row 10; §10 — the knobs M̃ and k̃. Quotations are transcribed from its LaTeX.
- `notes/broken-born-program-v1.md` §8, §9 — the step as "an optional early-universe fingerprint" and v1's row 10
- `review/round3/referee/audit-notes.md` Step 1, citation [23] — the Planck 2018 interval, checked against its source
- `review/round3-adjudication.md` 'Rulings', ruling 5 — the Standard Model value 3.044 and the bound ΔN_eff < 0.286
- `verify/soliton_obituary.py`, dark radiation — the gate's check of that bound
- `notes/knot-dark-matter-standalone.md` §4 — #14's dark radiation and its Planck interval (withdrawn manuscript)
- `review/wiki-build-flags.md` item 22 — #14's symmetric interval against the source's asymmetric one; item 32 — CMB-S4's status, unchecked
