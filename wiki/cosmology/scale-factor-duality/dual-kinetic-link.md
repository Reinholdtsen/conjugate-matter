---
title: "Open: dual kinetic energy versus τ's potential"
weight: 60
status: open
description: "The lab notebook motivates near-constant dark energy as kinetic energy in the dual frame (w̃ = +1 ↦ w = −1) but implements it as τ's potential energy; no document derives the link, and #11 §10 lists it as open, as part of P.R.'s conjecture that conjugate collapse powers our expansion."
sources:
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §3"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md App. A item 9"
  - "CLAUDE.md 'Since the handoff'"
  - "notes/broken-born-program-v1.md §8"
  - "review/wiki-build-flags.md item 27 (addendum)"
---

*This open problem is a gap between two explanations of dark energy that stand side by side in the program's [lab notebook](/wiki/history/documents/lab-notebook). The first comes from the [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary): kinetic energy in the conjugate, momentum-space description of the universe ([the conjugate universe](/wiki/program/conjugate-universe)) acts on our expansion like a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant#dual-kinetic-energy-acts-as-a-λ), so the notebook names it the natural source of a near-constant dark energy. The second is the explanation the program uses: dark energy is the potential energy of the field τ ([hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence)), held near the top of its potential. No document derives the second from the first, so the step from the motivation to the identification of dark energy with τ is asserted rather than derived. The checkpoint lists the same question as open, as part of P.R.'s conjecture that the conjugate universe's collapse drives our acceleration, whose one remaining route is the dual-frame kinetic energy.*

**Status:** Open — [O] in [#11](/wiki/history/documents/checkpoint) §10's paragraph on founding supposition 9; not among #11 §14's open problems — the gap was found by reading #1 §6 and §7 side by side when the sources were inventoried for this wiki, and #11 §10 lists "how this route relates to τ's potential" as open; no document resolves it. Listed on [open problems](/wiki/status/open-problems). It qualifies [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) and [Conjecture: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion).

## The question

Is the dark-energy field τ, whose energy the program places in its potential in our frame, the same thing as the kinetic energy in the conjugate frame that the duality dictionary turns into a cosmological constant? The lab notebook moves from the second to the first in one sentence, and no later document returns to the step.

## The first explanation: dual kinetic energy

The [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary) translates a fluid in the conjugate frame, with [equation of state](/wiki/cosmology/dark-energy/quintessence#dark-energy-and-the-equation-of-state) w̃, the ratio of its pressure to its energy density, into one acting on our expansion with w_eff = −w̃ [D — corrected en route] (#11 §10; as a map of fluid variables, the scale-factor duality of string cosmology with sources, flag 66 in `review/wiki-build-flags.md`, pending). Its first entry is

| Dual-frame content | Acts on our expansion as |
| --- | --- |
| Kinetic/stiff energy (w̃ = +1) | Cosmological constant (w = −1) |

(#1 §6's table; #11 §10, "Dual stiff ↦ Λ").

A stiff fluid, w = +1, is what a uniform scalar field becomes when its energy is all kinetic [T] ([Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)). In its own frame it thins fastest of all fluids; translated across [the constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint), it acts on our expansion as an energy density that does not thin at all.

From this entry the notebook draws its conclusion (#1 §6): "the natural source of a near-constant dark energy is **kinetic energy in the dual frame**." The same paragraph continues: "The obvious candidate for a free-rolling field is the one the symmetry breaking already handed us: τ."

## The second explanation: τ's potential energy

#1 §7 then implements dark energy: "Identify dark energy with the Maslov modulus τ sitting near the top of its cosine potential (hilltop axion quintessence)." The potential is V(τ) = V₀[1 + cos(τ/f)] (#1 §3; #11 §10).

A scalar field near the top of its potential, changing slowly, has w = (½τ̇² − V)/(½τ̇² + V) close to −1, because its potential energy V far exceeds its kinetic energy ½τ̇² [T]. Its dark energy is potential energy, held in our frame. This is the standard [hilltop quintessence](/wiki/cosmology/dark-energy/thawing-and-freezing#hilltop-models) of [quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence), and it is the form #11 keeps: "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1" (§10).

## The gap

The two explanations differ in two ways at once:

| | Motivation (#1 §6) | Implementation (#1 §7) |
| --- | --- | --- |
| Kind of energy | kinetic (w̃ = +1) | potential (w close to −1) |
| Frame | the conjugate, momentum-space description | ours |

Either explanation alone gives a near-constant dark energy. What is missing is the step that makes them one explanation: a derivation showing that the potential energy of τ in our description is the kinetic energy of a field in the conjugate description, or a statement in the record that the §6 remark is motivation only. The record contains neither. The notebook's own bridge, that τ is "the obvious candidate for a free-rolling field", names τ as a candidate for the dual-frame kinetic energy and then, one section later, places τ's energy in its potential in our frame.

## In the current documents

- **#11 §10** keeps both ingredients as separate statements, "Dual stiff ↦ Λ" in the dictionary and "τ is hilltop quintessence on the Maslov circle" under dark energy. A paragraph between them, on P.R.'s founding supposition 9 [O], names the question without answering it: "The corrected dictionary keeps a route: dual stiff ↦ Λ, so a conjugate universe whose contents are kinetic-dominated as it contracts would act on ours as a cosmological constant, and the lab notebook already names "kinetic energy in the dual frame" as "the natural source of a near-constant dark energy" (#1 §6). Whether the contracting conjugate universe is kinetic-dominated, and how this route relates to τ's potential, are open." ([Conjecture: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)).
- **#9 §8** keeps the two statements apart: "Dual stiff ↦ Λ" in the dictionary bullet and "τ is hilltop quintessence on the Maslov circle" in the dark-energy bullet.
- **The root `CLAUDE.md`** lists, among its open items not queued, "for App. A item 9: whether the contracting conjugate universe is kinetic-dominated, and how dual stiff ↦ Λ relates to τ's potential" ('Since the handoff'). #11 §14 does not list the gap. It first came to light when the lab notebook's sections were read side by side for this wiki, and it is recorded on [conflicts between sources](/wiki/history/documents/source-conflicts) as unresolved.

## What depends on it

On the wiki's reading of the documents, none of the program's derived results depends on the motivation: τ's identification as the Maslov phase ([τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase)), the [no-phantom bound](/wiki/cosmology/dark-energy/no-phantom-bound) and the [over-constraint](/wiki/cosmology/dark-energy/over-constraint) all start from τ's potential, not from the dual-frame kinetic energy. The gap concerns why dark energy should be τ at all, the explanatory link between the dictionary and the dark-energy sector.

One conjecture does depend on it. P.R.'s founding supposition 9, "Their collapse is our acceleration", is open only through the dual-frame kinetic energy: two versions failed, and the route that remains is the dictionary's entry dual stiff ↦ Λ (#11 §10, App. A item 9; [Conjecture: conjugate collapse powers our expansion](/wiki/cosmology/scale-factor-duality/collapse-powered-expansion)).

## Related open problems

- Where τ's potential comes from: [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).
- Whether τ's potential can become negative, as the documents' account of the [far-future turnaround](/wiki/cosmology/scale-factor-duality/conjugate-bounce) needs, while flag 27's addendum finds that a closed universe turns around with V ≥ 0: [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign).

## Sources

- `notes/broken-born-theory.md` §6 — the dictionary table and the kinetic-energy motivation, with τ named as the candidate
- `notes/broken-born-theory.md` §7 — τ as hilltop quintessence
- `notes/broken-born-theory.md` §3 — the potential V₀[1 + cos(τ/f)]
- `papers/broken-born-checkpoint-v2.md` §10 — both statements, and the paragraph on founding supposition 9 that lists their relation as open; App. A item 9 — the supposition, open
- `CLAUDE.md` 'Since the handoff' — the same question among the open items, not queued
- `notes/broken-born-program-v1.md` §8 — the same two statements in v1, unconnected
- `review/wiki-build-flags.md` item 27 and its addendum — the sign of the potential, and the turnaround in a closed universe with V ≥ 0
