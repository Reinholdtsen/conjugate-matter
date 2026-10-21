---
title: "The duality dictionary w_eff = −w̃"
weight: 30
status: alive
description: "With one shared lapse, a dual-frame fluid of equation of state w̃ contributes w_eff = −w̃: dual stiff ↦ Λ, dual Λ ↦ stiff, dual curvature ↦ negative dark radiation, dust ↦ dust."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 10"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md App. A item 8"
  - "papers/broken-born-checkpoint-v2.md App. A item 9"
  - "HANDOFF.md §2"
  - "notes/broken-born-theory.md §0"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §8"
---

*The duality dictionary is the rule that translates energy in the conjugate, momentum-space description of the universe ([the conjugate universe](/wiki/program/conjugate-universe)) into the form in which it acts on our own expansion. Each kind of energy is labelled by its equation of state w, the ratio of its pressure to its energy density, and the rule is that conjugate-side energy with equation of state w̃ acts on us like energy with w = −w̃. Pure kinetic energy on the conjugate side therefore acts here like a cosmological constant, a conjugate cosmological constant acts like the stiffest possible fluid, and dust acts like dust. The rule is derived [D] from [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint), and it replaced an earlier heuristic that gave a different answer, a correction that #11 counts as one of the two that sharpened the program's [hard core](/wiki/program/hard-core).*

**Status:** Alive — [D — corrected en route] (#11 §10) — derived in the [lab notebook](/wiki/history/documents/lab-notebook) (#1 §6); no `verify/` script checks it. The earlier rule w_eff = −2 − w̃ is superseded (below).

## Statement

#11 §10: "**Dictionary [D — corrected en route]:** with one shared lapse, a dual-frame fluid contributes w_eff = −w̃ (superseding an earlier −2 − w̃; the constraint's Jacobian changed the answer — rigor's job). Dual stiff ↦ Λ; dual Λ ↦ stiff; dual curvature ↦ negative dark radiation; dust ↦ dust; the dual Einstein term is an a⁻⁶ step in G_eff."

## The ingredients

The derivation combines three pieces of [Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology) with one result of the program.

- **Equation of state [T].** A fluid with pressure p = wρ thins as ρ ∝ a^{−3(1+w)} in a universe with scale factor a. Read backwards, the power of a with which an energy density falls identifies its w.
- **The Hamiltonian constraint [T].** In minisuperspace the lapse N is a Lagrange multiplier, and varying it gives one equation, the Friedmann equation, in which each kind of content enters through its energy per comoving volume.
- **One shared lapse.** The program describes the conjugate side with the same time coordinate, so the same N multiplies both descriptions and there is one constraint, not two. Energy described in the conjugate frame enters our Friedmann equation directly.
- **The constraint a·ã = 1 [D].** The conjugate scale factor is the reciprocal of ours at every moment ([the cosmological constraint](/wiki/cosmology/scale-factor-duality/cosmological-constraint)).

## The derivation

The [lab notebook](/wiki/history/documents/lab-notebook) (#1 §6) considers "A fluid comoving in the dual frame with equation of state w̃" and follows its energy across the constraint:

```text
ρ̃ ∝ ã^{−3(1+w̃)}                        the fluid thins in its own frame
E = ρ̃ ã³ ∝ ã^{−3w̃} = a^{3w̃}             its energy per dual comoving volume, using ã = 1/a
ρ_eff = E/a³ ∝ a^{−3(1−w̃)}              entered in our constraint per our comoving volume
⇒   w_eff = −w̃
```

Each line has a plain reading:

1. In the conjugate frame the fluid is an ordinary fluid and thins with ã by the usual rule.
2. The energy it holds in a comoving cell of the dual frame is its density times that cell's volume, ã³. Substituting ã = 1/a turns a power of ã into the opposite power of a.
3. Our Hamiltonian constraint takes energy per our comoving volume, a³, so the effective density on our side is E/a³: "Entering our Hamiltonian constraint as ρ_eff = E/a³" (#1 §6).
4. Matching a^{−3(1−w̃)} to the standard form a^{−3(1+w_eff)} gives w_eff = −w̃.

The factor ã³ in step 2 is the volume Jacobian of the constraint: it converts a density measured in the dual frame's volume into an energy before that energy is spread over ours. Leaving it out gives the superseded rule (below). The derivation is algebraic and does not use any field equation of the conjugate side.

## The table

The lab notebook's table (#1 §6), with its right-hand column renamed. The notebook heads that column "Appears on our books as"; the table below heads it *Acts on our expansion as*.

| Dual-frame content | Acts on our expansion as |
| --- | --- |
| Kinetic/stiff energy (w̃ = +1) | Cosmological constant (w = −1) |
| Cosmological constant (w̃ = −1) | Stiff fluid (w = +1, dies as a⁻⁶) |
| Spatial curvature (w̃ = −1/3) | Dark radiation (w = +1/3; closed dual space ⇒ negative ΔN_eff) |
| Dust (w̃ = 0) | Dust (w = 0) |

Each entry follows from E ∝ a^{3w̃}:

- **Dual stiff ↦ Λ.** A stiff fluid thins fastest in its own frame, as ã⁻⁶, so as ã shrinks its density grows; the dual comoving volume shrinks at the same time, and its energy E grows as a³. Spread over our volume, which also grows as a³, the effective density stays constant: a cosmological constant. A uniform scalar field whose energy is all kinetic is a stiff fluid [T], which is why the notebook labels this row "Kinetic/stiff energy".
- **Dual Λ ↦ stiff.** A constant dual density held in a shrinking dual volume gives an energy falling as a⁻³, and an effective density falling as a⁻⁶: a stiff fluid on our side, which matters only at early times.
- **Dual curvature ↦ dark radiation.** Curvature acts like a fluid with w = −1/3, so on our side it acts like radiation, w = +1/3. Extra radiation that is not photons or known neutrinos is called dark radiation, and it is measured by the shift ΔN_eff in the effective number of neutrino species N_eff ([the radiation era](/wiki/cosmology/early-universe/radiation-era)) [T]. A closed space has curvature energy of negative sign [T], so a closed dual space appears as negative dark radiation, "closed dual space ⇒ *negative* ΔN_eff" (#1 §6).
- **Dust ↦ dust.** Dust has w̃ = 0, so its energy E is constant: a fixed amount of matter. Spread over our volume, it thins as a⁻³, like ordinary matter.

The notebook draws the consequence: "dual *matter* no longer masquerades as exotic energy (dust maps to dust — the w=−2 pathology is gone because it was an artifact)" (#1 §6).

## The dual gravity term

The last clause of #11's statement, "the dual Einstein term is an a⁻⁶ step in G_eff", concerns the gravitational sector of the conjugate side rather than a fluid in it. The lab notebook substitutes ã = 1/a into the dual Einstein–Hilbert kinetic term, with the shared lapse and a dual Planck mass M̃, and obtains (#1 §6, [D])

```text
3H²(M_P² + M̃²a⁻⁶) = ρ
```

The dual term multiplies H² alongside M_P², so it changes the effective Planck mass and with it the effective strength of gravity G_eff, and it scales as a⁻⁶, like the stiff fluid of the table's second row. In #1 §6's words, it is "**not** a new fluid and **not** a ghost — ã was never independent — but a stiff-like (a⁻⁶) modification of the effective Planck mass, relevant only at early times". The steps are on [Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#the-programs-extension-a-second-scale-factor).

The test of this term, together with the negative ΔN_eff of closed dual curvature, is [row 10](/wiki/predictions/early-universe-step): "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff", "(Knob-bounded; CMB-S4 probes)" (#11 §13), where CMB-S4 is a planned fourth-stage survey of the cosmic microwave background. The equation appears only in the lab notebook and has not been machine-checked. The notebook's row also predicted, "conditionally on its one knob", a spectral step in the primordial gravitational-wave background and a CMB-S4 sensitivity to N_eff at "±0.03" (#1 §6, §9 row 10); #11 drops both.

## Superseded: the earlier heuristic rule

The development discussion on claude.ai used a different rule, w_eff = −2 − w̃. The lab notebook announces the replacement at its head: "the duality dictionary for cosmological fluids is w_eff = −w̃, not w_eff = −2 − w̃. The correction is what makes the dark-energy sector work. Rigor changed an answer; that is the point of rigor." (#1 §0). In §6 it gives the reason: the derived rule "**supersedes** the heuristic w_eff = −2 − w̃ used earlier in the development (which identified densities across frames without the constraint's volume Jacobian)".

**How the heuristic arises** (the wiki's reading; no document writes the step out). Identifying densities across frames means setting ρ_eff = ρ̃, skipping step 2 of the derivation. Then ρ_eff ∝ ã^{−3(1+w̃)} = a^{3(1+w̃)}, and matching this to a^{−3(1+w_eff)} gives w_eff = −2 − w̃. For dual dust, w̃ = 0, the heuristic gives w = −2.

**What it cost.** Collapsing conjugate matter, read through the heuristic, acted on our expansion like dark energy with w = −2. That was the basis of the founding idea that the conjugate universe's collapse drives our acceleration. The idea died twice: "first version gave w = −2 (falsified); corrected dictionary removed the mechanism (dual dust ↦ dust)" (`HANDOFF.md` §2). See [Obituary: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion).

**What the documents call the cause.** #1 §6 names the "volume Jacobian"; #9 §8 attributes the change to the handling of the Lagrange multiplier (the lapse); #11 §10 names "the constraint's Jacobian". The result is the same in all three, and #11's wording is the current one.

## Its place in the program

- **A forced correction.** #11 §15: the hard core is "twice sharpened by forced corrections (P2′; the w-dictionary)", the other correction being [P2′](/wiki/program/postulates/p2-prime). See [the hard core](/wiki/program/hard-core) and [assessment](/wiki/program/assessment).
- **Synchronized, not causal.** Founding supposition 8, "Synchronized, not causal; Fourier/holography", is "**alive** (the dictionary)" (#11 App. A item 8). Because ã = 1/a holds at every moment, the dictionary is a translation between two descriptions of one state, not a force one universe exerts on the other. See [the conjugate universe](/wiki/program/conjugate-universe) and [founding suppositions and their fates](/wiki/program/founding-suppositions).
- **A motivation for dark energy.** From the first row of the table the notebook concludes that "the natural source of a near-constant dark energy is **kinetic energy in the dual frame**" (#1 §6). The program then identifies dark energy with the potential energy of the field τ ([τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)), and no document derives one from the other: [Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link).

## Scope and caveats

- **Minisuperspace.** The dictionary is derived for homogeneous fluids in a homogeneous universe. #1 §4's ghost accounting is likewise a minisuperspace statement, and it records that "The statement for full inhomogeneous H is open" [O].
- **Not machine-checked.** The derivation and the a⁻⁶ equation appear only in the lab notebook. #11 §10 and #9 §8 restate the result without the derivation, and no `verify/` script checks it.

## History

- **Chat era.** The heuristic −2 − w̃ and the collapse-powered acceleration it supported; both appear in the documents only as superseded or dead.
- **Lab notebook, v0.1** (#1 §0, §6): the corrected rule, its table and the dark-energy motivation.
- **#9 §8**: "With one shared lapse, a dual-frame fluid contributes w_eff = −w̃", tagged "[D — corrected en route]".
- **`HANDOFF.md` §2**: "duality dictionary w_eff = −w̃ (corrected from an earlier wrong −2−w̃)".
- **#11 §10** is the current statement; §15 counts it among the forced corrections.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the current statement, its tag and the summary of the table
- `papers/broken-born-checkpoint-v2.md` §13 row 10 — the test of the dual gravity term
- `papers/broken-born-checkpoint-v2.md` §15, App. A items 8 and 9 — the forced correction; founding suppositions 8 and 9
- `HANDOFF.md` §2 — the corrected dictionary and the two deaths of the collapse idea
- `notes/broken-born-theory.md` §6 — the derivation, the table, the superseded heuristic, the dual gravity term and the kinetic-energy remark
- `notes/broken-born-theory.md` §0 — the correction announced at the head of the notebook
- `notes/broken-born-theory.md` §4, §9 row 10 — the minisuperspace scope of the ghost accounting; the v0.1 form of row 10
- `notes/broken-born-program-v1.md` §8 — v1's statement of the dictionary
