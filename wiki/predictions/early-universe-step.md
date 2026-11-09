---
title: "Row 10: an early step in G_eff"
weight: 110
status: alive
description: "Two optional early-universe imprints of the dual gravitational sector: an a⁻⁶ step in the effective gravitational coupling before nucleosynthesis, and negative dark radiation (ΔN_eff < 0) if the dual space is closed; their sizes are free parameters, so data bound them rather than kill the program."
provenance: [D]
sources:
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 10"
  - "wiki/papers/broken-born-checkpoint-v2.md §10"
  - "wiki/papers/broken-born-checkpoint-v2.md §15"
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
  - "wiki/papers/phase-space-diameter.md §8.4"
  - "verify/phase_space_diameter.py"
  - "notes/closed-universe.md §4"
  - "notes/closed-universe.md §7"
  - "notes/closed-universe.md §9"
  - "verify/closed_universe.py 'E. Momentum space and reciprocity'"
  - "review/wiki-build-flags.md items 48, 49"
  - "notes/dual-sector.md §4"
  - "notes/dual-sector.md §9"
  - "review/wiki-build-flags.md item 72"
---

*Row 10 describes two possible imprints of the program's dual, momentum-side gravitational sector on the early universe. The first is a step in the effective strength of gravity, G_eff: the dual sector adds to the square of the [effective Planck mass](../gravity/spin-2-fields/planck-units.md#an-effective-planck-mass) a term that grows toward the past as the sixth inverse power of the cosmic scale factor, a⁻⁶, so it matters only at early times, before the light elements formed in [Big Bang nucleosynthesis](../cosmology/early-universe/big-bang-nucleosynthesis.md). The second is negative dark radiation: if the dual space is closed, its curvature acts on our expansion like radiation of negative energy, which lowers the effective number of neutrino species, N_eff. Both follow from [the lab notebook](../history/documents/lab-notebook.md)'s calculation with the [cosmological constraint](../cosmology/scale-factor-duality/cosmological-constraint.md) a·ã = 1. The step is optional and the dark radiation conditional on a closed dual space, and their sizes are free parameters (knobs), so a null result bounds the knobs rather than killing the program; [#11](../papers/broken-born-checkpoint-v2.md) names the cosmic microwave background experiment CMB-S4 as the probe.*

**Status:** Alive, optional and knob-bounded — [D] (the lab notebook's minisuperspace calculation and dictionary, [#1 §6](../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary); [#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology)'s dictionary is [D — corrected en route]); the self-dual placement of the step, conditional, is [D][V] ([phase-space-diameter note §8.4](../papers/phase-space-diameter.md#84-the-early-universe-term-sits-at-the-self-dual-point-dv)) — no `verify/` script checks the row's equations, except that the exchange of the two kinetic terms under a → C/a at M̃ = M_P is gated in [`verify/phase_space_diameter.py`](../../verify/phase_space_diameter.py); no document compares either imprint with data. Two flags from the closed-universe note (2026-10-27, computed, not reviewed) bear on the row's foundations: the dual Einstein–Hilbert term behind the a⁻⁶ step is derived in no document, so the step tests a postulate (flag 49 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md)), and a closed universe does not close the dual space, so the negative ΔN_eff needs a postulate no document states (flag 48); see [what the row rests on](#what-the-row-rests-on).

## The row

[Checkpoint #11](../history/documents/checkpoint.md) [§13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions), row 10:

| Observable | Standard expectation | Program requirement | Killed by |
| --- | --- | --- | --- |
| Early universe | Standard G, N_eff | Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff | (Knob-bounded; CMB-S4 probes) |

G is Newton's constant and G_eff the effective gravitational coupling in the expansion equation. N_eff is the effective number of neutrino species and ΔN_eff its departure from the standard value. CMB-S4 is a proposed ground-based experiment on the cosmic microwave background (CMB) [T]; whether it is still going ahead is unchecked (flag 32 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md), a lead from model memory that the flags' audit left unclear). The kill column is a parenthesis: the row names no result that would end a claim.

## The observables [T]

Two measurements of the early universe bear on the row ([the radiation era: thermal history and N_eff](../cosmology/early-universe/radiation-era.md)):

- **The expansion rate during nucleosynthesis.** In the first minutes, the ratio of neutrons to protons freezes when the weak reactions that convert them become slower than the expansion. A faster expansion freezes it earlier, leaves more neutrons and so more helium. The primordial helium abundance therefore measures the expansion rate H during Big Bang nucleosynthesis (BBN), and H depends on both the radiation content and the strength of gravity [T] ([the expansion rate: radiation and gravity together](../cosmology/early-universe/big-bang-nucleosynthesis.md#the-expansion-rate-radiation-and-gravity-together)).
- **N_eff.** The radiation of the universe after electron–positron annihilation is photons and three neutrino species. N_eff measures the energy density of all light species other than photons, in units of one neutrino species; extra light particles raise it, and the [cosmic microwave background](../cosmology/early-universe/cosmic-microwave-background.md#n_eff) measures it through the expansion history before recombination [T].

## The standard expectation

"Standard G, N_eff" ([#11 §13](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)): Newton's constant has the same value in the early universe as now, and N_eff takes the value of the Standard Model's three neutrinos, a little above 3. The round-3 record uses 3.044 for it ([ruling 5](../method/review/round-3/rulings.md)) [T].

## The program's requirement

Both imprints come from the lab notebook's cosmology, which rests on two results of [scale-factor duality](../cosmology/scale-factor-duality/_index.md).

### The constraint a·ã = 1

The program describes the universe with two scale factors, a for position space and ã for momentum space. Rigidity of [the symplectic form](../phase-space/reciprocity/symplectic-form.md) fixes the volume of a comoving cell of [phase space](../phase-space/_index.md), so ([#1 §6](../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary), [D]): "each mode occupies (aã)³ × (comoving cell) = ℏ³", and a·ã = const ≡ 1, "the statement that ℏ does not run" ([the derivation](../cosmology/scale-factor-duality/cosmological-constraint.md#the-derivation)). ã is therefore not an independent variable: wherever it appears, it can be replaced by 1/a. Quotations from #1 on this page are transcribed from its LaTeX.

### The a⁻⁶ step in G_eff

The notebook adds the dual sector's own gravitational term to the minisuperspace description of the universe, in which gravity is reduced to the scale factor and the lapse ([#1 §6](../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary), [D]): "With one shared lapse N and dual Planck mass M̃, substituting ã = 1/a into the dual Einstein–Hilbert kinetic term" — the term ã(dã/dt)², which the substitution turns into ȧ²/a⁵ — "gives"

```text
3H²(M_P² + M̃² a⁻⁶) = ρ
```

where H is the expansion rate and ρ the energy density. Without the M̃ term this is the ordinary Friedmann equation. The steps are on [Friedmann cosmology and minisuperspace](../cosmology/scale-factor-duality/friedmann-cosmology.md#the-programs-extension-a-second-scale-factor).

What the term means, in the notebook's words: "The dual gravitational sector is **not** a new fluid and **not** a ghost — ã was never independent — but a stiff-like (a⁻⁶) modification of the effective Planck mass, relevant only at early times. It predicts a step in G_eff before BBN and, conditionally on its one knob, a spectral step in the primordial gravitational-wave background. **[D]**"

The wiki's reading of the equation: the bracket is an effective Planck mass squared, and the effective strength of gravity is inversely proportional to it. The dual term grows toward the past as a⁻⁶, so at early enough times it dominates the bracket and gravity is weaker than today; as a grows, M_P² takes over and the ordinary Friedmann equation returns. The passage between the two regimes is the "step". The notebook gives neither the step's size nor its time, beyond "before BBN"; M̃ is free. [#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology) keeps the result in one clause, "the dual Einstein term is an a⁻⁶ step in G_eff" ([the dual gravity term](../cosmology/scale-factor-duality/duality-dictionary.md#the-dual-gravity-term)).

"Not a ghost" is a [minisuperspace statement](../gravity/spin-2-fields/ghosts.md#the-lab-notebooks-minisuperspace-argument). The notebook records that "no Boulware–Deser sector arises in minisuperspace" [D] and that "The statement for full inhomogeneous H is open" [O] ([#1 §4](../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured)). That analysis predates the notebook's v0.4 addendum, after which the momentum-space partner of the metric is a massive spin-2 field ([the momentum graviton X](../gravity/momentum-graviton/_index.md)).

If reciprocity fixes M̃ = M_P, the step has a place [D][V]. With a·ã = C, the two kinetic terms M_P² aȧ² and M̃² C³ ȧ²/a⁵ are exchanged by a → C/a exactly when M̃ = M_P, and they are then equal at the fixed point a = √C, where a = ã, so the step "sits at the self-dual epoch". That epoch depends on the [Born length](../phase-space/reciprocity/born-length.md) λ and on the comoving unit: for λ = l_P and the radiation of today's observable universe it is the 10¹⁴ T_P of [the square at the bounce](../cosmology/scale-factor-duality/square-at-the-bounce.md), "which is not a bounce". Whatever the unit, it "must lie before" nucleosynthesis ([phase-space-diameter note §8.4](../papers/phase-space-diameter.md#84-the-early-universe-term-sits-at-the-self-dual-point-dv)). The exchange is gated in [`verify/phase_space_diameter.py`](../../verify/phase_space_diameter.py).

### Negative dark radiation from a closed dual space

The second imprint comes from the [duality dictionary](../cosmology/scale-factor-duality/duality-dictionary.md), which translates content of the dual frame into its effect on our expansion. The notebook's derivation ([#1 §6](../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary), [D]): a fluid comoving in the dual frame with [equation of state](../cosmology/dark-energy/quintessence.md#dark-energy-and-the-equation-of-state) w̃, the ratio of its pressure to its energy density in that frame, has density ρ̃ ∝ ã^{−3(1+w̃)} and energy E = ρ̃ã³ ∝ ã^{−3w̃} = a^{3w̃}; entering our expansion as ρ_eff = E/a³ ∝ a^{−3(1−w̃)}, it acts as a fluid with

```text
w_eff = −w̃
```

Spatial curvature behaves like a fluid with w̃ = −1/3 [T], so curvature of the dual space acts on our side as w = +1/3, the equation of state of radiation. The notebook's table: "Spatial curvature (w̃ = −1/3)" appears as "Dark radiation (w = +1/3; closed dual space ⇒ *negative* ΔN_eff)" ([the table](../cosmology/scale-factor-duality/duality-dictionary.md#the-table)). The sign comes from the curvature: in the Friedmann equation the curvature of a closed space enters with the opposite sign to an energy density, so read as a fluid it has negative energy density [T], and the dictionary carries that sign across. Extra radiation raises or lowers N_eff according to its sign, so a closed dual space gives ΔN_eff < 0. The table singles out the closed case, and no document discusses an open dual space ([row 10 on the radiation-era page](../cosmology/early-universe/radiation-era.md#row-10-negative-δn_eff-from-a-closed-dual-space)).

[#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology) keeps it as "dual curvature ↦ negative dark radiation", with the dictionary tagged "[D — corrected en route]" (as a map of fluid variables, the scale-factor duality of string cosmology with sources; flag 66 in [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md), pending): the rule w_eff = −w̃ superseded an earlier heuristic, −2 − w̃, which identified densities across the two frames without the constraint's volume factor ([Superseded: the earlier heuristic rule](../cosmology/scale-factor-duality/duality-dictionary.md#superseded-the-earlier-heuristic-rule)).

### Optional, and bounded by knobs

The notebook's parameter table counts the dual geometric sector separately ([#1 §10](../../notes/broken-born-theory.md#10-parameter-count)):

| Sector | Parameters | Phenomena covered |
| --- | --- | --- |
| Geometry | M̃, k̃ (2, optional) | Early-G step, ΔN_eff, a gravitational-wave step |

The last entry is paraphrased; the notebook abbreviates it. M̃ is the dual Planck mass. k̃ is not defined in the notebook; written beside the dual curvature, it reads as the curvature of the dual space (the wiki's reading). Both can be zero: with M̃ = 0 there is no step, and with a flat or open dual space no negative dark radiation. "Knob-bounded" means that measurements consistent with the standard values bound M̃ and k̃ rather than refute the program; v0.1 and v1 wrote "Bounds constrain knobs" ([#1 §9](../../notes/broken-born-theory.md#9-predictions); [#9 §9](../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions)).

## What the row rests on

The closed-universe note of 2026-10-27 examined both imprints while asking what a closed universe implies ([`notes/closed-universe.md` §4](../../notes/closed-universe.md#4-how-small-momentum-space-gets), [§7](../../notes/closed-universe.md#7-the-dual-frame-what-closure-fixes-and-what-it-does-not); [a closed Comatter universe](../cosmology/scale-factor-duality/closed-universe.md)). The note is computed and checked by independent agents and has not been reviewed; the two flags are pending.

**The dual term is not derived [O] (flag 49).** [#1 §6](../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary)'s minisuperspace equation, tagged [D], uses a dual Einstein–Hilbert term in ã with its own mass M̃, but [#1 §3](../../notes/broken-born-theory.md#3-action) reduces the geometric action S_H only for the ordinary metric's block, "[D, schematic]", and no document derives the dual term from S_H. [#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology)'s "the dual Einstein term is an a⁻⁶ step in G_eff" and this row's step rest on it, while [#11 §14 item 1](../papers/broken-born-checkpoint-v2.md#14-open-problems) lists only the wedge-sector reduction as open. "Until the term is derived, the a⁻⁶ step and every bound on the dual frame test a postulate." The flag's two auditors both confirm that no derivation exists, and both note that √|H| = 1 holds if |H| is the full 2d-dimensional determinant, which the record does not say. The note lists the derivation first among its open items ([§9](../papers/broken-born-checkpoint-v2.md#9-momentum-clumping-the-founding-image-tested)). A dual Einstein term is treated in the literature, in string theory's [doubled phase space](../dark-matter/conjugate-matter/dual-standard-model.md#what-dual-means-there), whose dual coordinate is not momentum but a coordinate with a momentum of its own: [Berglund, Hübsch and Minić 2019](https://arxiv.org/abs/1905.08269) (Phys. Lett. B) [S] integrate the doubled gravitational action over that coordinate, and "the curvature of the canonically conjugate dual space provides for a positive cosmological constant to leading order", the opposite assignment to [#11 §10](../papers/broken-born-checkpoint-v2.md#10-cosmology)'s "dual curvature ↦ negative dark radiation" ([`notes/dual-sector.md` §4](../../notes/dual-sector.md#4-what-their-dual-is), [§9](../../notes/dual-sector.md#9-other-overlaps); flag 72, pending).

**Only two combinations are physical [D][V].** Under the record's dictionary only vM̃²C³, the coefficient of the a⁻⁶ term, and vM̃²k̃C, the dual curvature, are physical, C being the comoving unit; so "M̃ = M_P" constrains nothing unless C is fixed (§7). With the record's normalization, C = 1, M̃ = M_P and λ = l_P, the a⁻⁶ term is below 10⁻¹⁹⁸ of the total after inflation for |Ω_k| ≤ 10⁻², where Ω_k is the curvature density of a closed universe (§7). The knob M̃ survives as a postulate (§10).

**A closed universe does not close the dual space [D][V] (flag 48).** The row's second imprint needs a closed dual space. Under the slaved block g̃ = g⁻¹ of the record's geometry, the momentum block of the generalized metric is the same at every momentum, for any X, so the momentum fibre is flat, k̃ = 0, and k = +1 does not induce k̃ = +1 (§4; [momentum fibers](../phase-space/reciprocity/momentum-fibers.md)). The effect therefore needs a separate postulate of a curved, compact momentum space, which no document states; the flag's audit adds that the record keeps k̃ as an optional knob rather than asserting a closed dual space, so the gap is the unstated postulate. This page's reading of k̃ as the curvature of the dual space, above, is the same reading.

**The symmetric reading is under review; its bounds stand [D][V].** The note tests the simplest such postulate, k̃ = k with vM̃² = M_P², in which one self-dual radius R_sd fixes both the a⁻⁶ term and the dual curvature. At |Ω_k| = 10⁻², Big Bang nucleosynthesis requires R_sd ≤ 1.568×10¹⁷ m and N_eff requires R_sd ≤ 3.029×10²⁵ m; the observed momentum range sets a minimum on R_sd, and the 6.8 TeV protons of the Large Hadron Collider (LHC), with N_eff and nucleosynthesis, then need a Born length λ ≤ 1.278×10⁻⁶ m, and with standard slow-roll inflation λ ≤ 1.986×10⁻⁴⁹ m; for λ = √(l_P c/H₀) the window is empty (§4). The reading also contradicts the record's k̃ = 0 and rests on the underived dual term. The note's verdict: the reading stands only if a compact momentum space is added deliberately (§4; [Under review: the symmetric reading](../cosmology/scale-factor-duality/closed-universe.md#under-review-the-symmetric-reading-dv)). The numbers are checked in section E of [`verify/closed_universe.py`](../../verify/closed_universe.py) ([the closed-universe script](../method/verification/closed-universe-script.md)).

None of this removes the row: "Optional a⁻⁶ G_eff step" remains a knob, and a postulated one, and "closed dual curvature ⇒ negative ΔN_eff" remains conditional, on a closed dual space that closure of our own space does not provide.

## What kills it

Nothing in the row: "(Knob-bounded; CMB-S4 probes)". A measurement of standard G and N_eff is consistent with the row at small M̃ and k̃, and the documents name no values of the knobs that the program expects, so a result within the standard values bounds the knobs without counting against the program. What the row looks for is a step in the expansion rate before nucleosynthesis or a negative ΔN_eff.

## The data situation

No program document compares either imprint with a measurement, and none computes the size of the step or of the negative ΔN_eff for any value of the knobs.

Apart from the notebook's ±0.03 for CMB-S4 (below), the N_eff figures in the record belong to [#14](../../notes/knot-dark-matter-standalone.md)'s failed soliton model, whose hidden photon would have added positive dark radiation ([Obituary: #14's superheavy-soliton model](../dark-matter/candidates/soliton-candidate/obituary.md)). The round-3 referee checked the [Planck 2018](https://arxiv.org/abs/1807.06209) interval against its source, Planck's combination of its own data with baryon-acoustic-oscillation measurements at 95% confidence: "N_eff = 2.99 +0.34 -0.33" ([`review/round3/referee/audit-notes.md`](../../review/round3/referee/audit-notes.md), Step 1, citation [23]; #14 had written "2.99 +- 0.34", [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 22). With the Standard Model value 3.044, ruling 5 put the 95% bound on extra radiation at ΔN_eff < 0.286, which [the gate](../method/verification/the-gate.md) checks ([the soliton-obituary script](../method/verification/soliton-obituary-script.md)):

```text
PASS  95% bound Delta N_eff < 0.286  [0.286]
```

These figures bound positive ΔN_eff for a different proposal; no document applies them to row 10.

#11 names CMB-S4 as the probe and gives no sensitivity. [#11 §15](../papers/broken-born-checkpoint-v2.md#15-assessment) names rows 1, 4 and 7 as the program's near-term falsification exposure; row 10 is not among them.

## Superseded: the spectral step and the ±0.03 target

The lab notebook's row 10 ([#1 §9](../../notes/broken-born-theory.md#9-predictions)) required an "a⁻⁶ step in G_eff; optional negative ΔN_eff from closed dual curvature", together with a conditional step in the spectrum of primordial gravitational waves, and its kill column read "(Bounds constrain knobs; CMB-S4 N_eff at ±0.03 probes the curvature term)". The ±0.03 figure appears only in #1, and no document or script checks it.

v1 ([#9 §9](../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions)) changed the row in three ways, and #11 kept v1's form:

- it dropped the spectral step in the gravitational-wave background;
- it dropped the ±0.03 target, reading "(Bounds constrain knobs; CMB-S4 probes)";
- it moved "optional" from the dark radiation to the step: "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff". v1's cosmology section calls the step "an optional early-universe fingerprint" ([#9 §8](../../notes/broken-born-program-v1.md#8-cosmology)).

#11 changed only the kill column's first words, from "Bounds constrain knobs" to "Knob-bounded". No document says why the spectral step and the target were dropped. The mechanism the notebook implies for the spectral step is discussed on [the dropped spectral step](../cosmology/early-universe/phase-transition-gravitational-waves.md#the-dropped-spectral-step-row-10), and the whole table's history on [the history of the predictions table](table-history.md).

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §13 row 10](../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the row; [§10](../papers/broken-born-checkpoint-v2.md#10-cosmology) — the dictionary [D — corrected en route] and "the dual Einstein term is an a⁻⁶ step in G_eff"; [§15](../papers/broken-born-checkpoint-v2.md#15-assessment) — the near-term rows
- [`notes/broken-born-theory.md` §6](../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary) — the constraint, the minisuperspace equation, the a⁻⁶ step and the dictionary table [D]; [§4](../../notes/broken-born-theory.md#4-consistency-with-everything-already-measured) — the minisuperspace ghost analysis; [§9](../../notes/broken-born-theory.md#9-predictions) — v0.1's row 10; [§10](../../notes/broken-born-theory.md#10-parameter-count) — the knobs M̃ and k̃. Quotations are transcribed from its LaTeX.
- [`notes/broken-born-program-v1.md` §8](../../notes/broken-born-program-v1.md#8-cosmology), [§9](../../notes/broken-born-program-v1.md#9-predictions-and-kill-conditions) — the step as "an optional early-universe fingerprint" and v1's row 10
- [`review/round3/referee/audit-notes.md`](../../review/round3/referee/audit-notes.md) Step 1, citation [23] — the Planck 2018 interval, checked against its source
- [`review/round3-adjudication.md`](../../review/round3-adjudication.md) 'Rulings', ruling 5 — the Standard Model value 3.044 and the bound ΔN_eff < 0.286
- [`verify/soliton_obituary.py`](../../verify/soliton_obituary.py), dark radiation — the gate's check of that bound
- [`notes/knot-dark-matter-standalone.md` §4](../../notes/knot-dark-matter-standalone.md#4-observational-consistency) — #14's dark radiation and its Planck interval (withdrawn manuscript)
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 22 — #14's symmetric interval against the source's asymmetric one; item 32 — CMB-S4's status, unchecked
- [`wiki/papers/phase-space-diameter.md` §8.4](../papers/phase-space-diameter.md#84-the-early-universe-term-sits-at-the-self-dual-point-dv) and [`verify/phase_space_diameter.py`](../../verify/phase_space_diameter.py) — the step at the self-dual epoch if reciprocity fixes M̃ = M_P, and the exchange of the two kinetic terms
- [`notes/closed-universe.md` §4](../../notes/closed-universe.md#4-how-small-momentum-space-gets) — the flat momentum fibre and the symmetric reading, under review, with the note's verdict; [§7](../../notes/closed-universe.md#7-the-dual-frame-what-closure-fixes-and-what-it-does-not) — the underived dual term, the two physical combinations and the record's normalization; [§9](../../notes/closed-universe.md#9-what-is-open) — the derivation, open; computed, not reviewed
- [`verify/closed_universe.py`](../../verify/closed_universe.py) section E — E1 (the flat fibre), E7 (the symmetric reading and its bounds), E9 (the a⁻⁶ term after inflation)
- [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) items 48 and 49 — the closed dual space and the underived dual term, with their audits; pending
- [`notes/dual-sector.md` §9](../../notes/dual-sector.md#9-other-overlaps) and [`review/wiki-build-flags.md`](../../review/wiki-build-flags.md) item 72 — a dual Einstein term in the literature, the dual space's curvature giving a positive cosmological constant (Berglund, Hübsch and Minić 2019); §4 — their dual space spanned by the doubled coordinate, not by momentum; searched and verified by independent agents, not reviewed; the flag pending
