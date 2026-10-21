---
title: "Open: dual kinetic energy versus τ's potential"
weight: 60
status: open
description: "The lab notebook motivates near-constant dark energy as kinetic energy in the dual frame (w̃ = +1 ↦ w = −1) but implements it as τ's potential energy; no document derives the link."
sources:
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §3"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "notes/broken-born-program-v1.md §8"
---

*This open problem is a gap between two explanations of dark energy that stand side by side in the program's [lab notebook](/wiki/history/documents/lab-notebook). The first comes from the [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary): kinetic energy in the conjugate, momentum-space description of the universe ([the conjugate universe](/wiki/program/conjugate-universe)) acts on our expansion like a cosmological constant, so the notebook names it the natural source of a near-constant dark energy. The second is the explanation the program uses: dark energy is the potential energy of the field τ ([hilltop quintessence](/wiki/cosmology/dark-energy/tau-quintessence)), held near the top of its potential. No document derives the second from the first, so the step from the motivation to the identification of dark energy with τ is asserted rather than derived.*

**Status:** Open — untagged; not among #11 §14's open problems — the gap was found by reading #1 §6 and §7 side by side when the sources were inventoried for this wiki, and no document addresses it. Listed on [open problems](/wiki/status/open-problems). It qualifies [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence).

## The question

Is the dark-energy field τ, whose energy the program places in its potential in our frame, the same thing as the kinetic energy in the conjugate frame that the duality dictionary turns into a cosmological constant? The lab notebook moves from the second to the first in one sentence, and no later document returns to the step.

## The first explanation: dual kinetic energy

The [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary) translates a fluid in the conjugate frame, with equation of state w̃, into one acting on our expansion with w_eff = −w̃ [D — corrected en route] (#11 §10). Its first entry is

| Dual-frame content | Acts on our expansion as |
| --- | --- |
| Kinetic/stiff energy (w̃ = +1) | Cosmological constant (w = −1) |

(#1 §6's table; #11 §10, "Dual stiff ↦ Λ").

A stiff fluid, w = +1, is what a uniform scalar field becomes when its energy is all kinetic [T] ([Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)). In its own frame it thins fastest of all fluids; translated across [the constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint), it acts on our expansion as an energy density that does not thin at all.

From this entry the notebook draws its conclusion (#1 §6): "the natural source of a near-constant dark energy is **kinetic energy in the dual frame**." The same paragraph continues: "The obvious candidate for a free-rolling field is the one the symmetry breaking already handed us: τ."

## The second explanation: τ's potential energy

#1 §7 then implements dark energy: "Identify dark energy with the Maslov modulus τ sitting near the top of its cosine potential (hilltop axion quintessence)." The potential is V(τ) = V₀[1 + cos(τ/f)] (#1 §3; #11 §10).

A scalar field near the top of its potential, changing slowly, has w = (½τ̇² − V)/(½τ̇² + V) close to −1, because its potential energy V far exceeds its kinetic energy ½τ̇² [T]. Its dark energy is potential energy, held in our frame. This is the standard hilltop quintessence of [quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence), and it is the form #11 keeps: "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1" (§10).

## The gap

The two explanations differ in two ways at once:

| | Motivation (#1 §6) | Implementation (#1 §7) |
| --- | --- | --- |
| Kind of energy | kinetic (w̃ = +1) | potential (w close to −1) |
| Frame | the conjugate, momentum-space description | ours |

Either explanation alone gives a near-constant dark energy. What is missing is the step that makes them one explanation: a derivation showing that the potential energy of τ in our description is the kinetic energy of a field in the conjugate description, or a statement in the record that the §6 remark is motivation only. The record contains neither. The notebook's own bridge, that τ is "the obvious candidate for a free-rolling field", names τ as a candidate for the dual-frame kinetic energy and then, one section later, places τ's energy in its potential in our frame.

## In the current documents

- **#11 §10** keeps both ingredients as separate statements, "Dual stiff ↦ Λ" in the dictionary and "τ is hilltop quintessence on the Maslov circle" under dark energy, and does not connect them.
- **#9 §8** does the same: "Dual stiff ↦ Λ" in the dictionary bullet and "τ is hilltop quintessence on the Maslov circle" in the dark-energy bullet.
- Neither the root `CLAUDE.md` queue nor #11 §14 lists the gap. It came to light when the lab notebook's sections were read side by side for this wiki, and it is recorded on [conflicts between sources](/wiki/history/documents/source-conflicts) as unresolved.

## What depends on it

On the wiki's reading of the documents, none of the program's derived results depends on the motivation: τ's identification as the Maslov phase ([τ as the Maslov phase of the boundary](/wiki/phase-space/modular-field/maslov-phase)), the [no-phantom bound](/wiki/cosmology/dark-energy/no-phantom-bound) and the [over-constraint](/wiki/cosmology/dark-energy/over-constraint) all start from τ's potential, not from the dual-frame kinetic energy. The gap concerns why dark energy should be τ at all, the explanatory link between the dictionary and the dark-energy sector.

## Related open problems

- Where τ's potential comes from: [Open: the origin of the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential).
- Whether τ's potential can become negative, as the far-future turnaround needs: [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign).

## Sources

- `notes/broken-born-theory.md` §6 — the dictionary table and the kinetic-energy motivation, with τ named as the candidate
- `notes/broken-born-theory.md` §7 — τ as hilltop quintessence
- `notes/broken-born-theory.md` §3 — the potential V₀[1 + cos(τ/f)]
- `papers/broken-born-checkpoint-v2.md` §10 — both statements, unconnected
- `notes/broken-born-program-v1.md` §8 — the same two statements in v1, unconnected
