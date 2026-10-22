---
title: "The dark-energy over-constraint"
weight: 80
status: alive
description: "With V₀ fixed by Ω_DE, two parameters (f, τᵢ) must fit three observables (w₀, wₐ, t_turn): one built-in consistency test, counted by #11 §15 as a progressive sign, whose third leg is long-horizon and rests on the unresolved sign of V(τ)."
provenance: [D]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "papers/broken-born-checkpoint-v2.md §13 rows 4–5"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §10"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §11"
  - "CLAUDE.md 'Since the handoff'"
---

*The dark-energy over-constraint is a counting argument: the program's dark-energy model has fewer free numbers than the quantities it predicts, so the data can test the model against itself. The model has three free numbers, the height V₀ and scale f of the potential of the dark-energy field [τ](/wiki/cosmology/dark-energy/tau-quintessence) and τ's initial value τᵢ, and the height is fixed by the measured amount of dark energy, which leaves two. Those two must account for three observables: today's equation of state w₀, its rate of change wₐ, and the time of the future [turnaround](/wiki/cosmology/scale-factor-duality/conjugate-bounce), t_turn. One relation among the three is therefore a prediction, which the checkpoint counts among the program's progressive signs. The third observable lies in the far future, and the turnaround it times needs the potential to go negative, which the potential as written never does.*

**Status:** Alive — [D] (#1 §7 item 4), within [checkpoint #11](/wiki/history/documents/checkpoint) §10's [D + T] paragraph — a counting result, not a computation and not machine-checked; no document writes the predicted relation explicitly. Its third leg is long-horizon (#11 §13 [row 5](/wiki/predictions/fate-of-expansion)) and depends on [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign) (flag 27 in `review/wiki-build-flags.md`).

## The statement

#11 §10: "two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint." The v1 paper gives the same count with its premise: "V₀ fixed by Ω_DE, two remaining parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint" (#9 §8).

## The count, step by step

The [lab notebook](/wiki/history/documents/lab-notebook) states the argument in one item (#1 §7 item 4, transcribed from its LaTeX):

> **Parameter economy.** V₀ is fixed by Ω_DE; the observables (w₀, wₐ, t_turn) are then functions of two numbers, (f, τᵢ). Three measurements, two parameters: one over-constraint. **[D]**

Spelled out:

1. **The model's free numbers.** τ has the action S_τ = ∫√−g[½(∂τ)² − V(τ)] with V(τ) = V₀[1 + cos(τ/f)] (#1 §3; [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)). Its evolution is set by three numbers: V₀, the height of the potential; f, its angular scale, which fixes the period 2πf and how sharply the potential curves near its maximum; and τᵢ, the field's initial value, which fixes how close to the maximum it starts. In a thawing model the expansion holds the field nearly still at early times, so its initial velocity is not a separate parameter [T] ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence#thawing-and-freezing-t)); the documents count only τᵢ.
2. **One is fixed by a measurement.** Ω_DE is the measured fraction of the universe's energy density in dark energy today. Matching it fixes the overall height V₀ once f and τᵢ are given [T]. Two free numbers remain, f and τᵢ.
3. **Three observables.** w₀ and wₐ are the present value and the drift of the dark-energy equation of state in the Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a) ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence)). t_turn is the time at which the expansion halts and reverses ([the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)).
4. **One relation.** Three observables that depend on two numbers cannot all be chosen freely. In principle two of them, say w₀ and wₐ, fix f and τᵢ, and the third, t_turn, is then predicted. A measured third value that disagrees with the prediction would count against the model.

The argument is a count of parameters, tagged [D]. No document computes the map from (f, τᵢ) to (w₀, wₐ, t_turn), writes the relation among the three observables, or evaluates t_turn for any values; the over-constraint is a statement that such a relation exists.

## The count in the notebook's table

The notebook's §10 tabulates parameters against phenomena for each sector ([the lab notebook](/wiki/history/documents/lab-notebook); [history of the predictions table](/wiki/predictions/table-history)):

| Sector | Parameters | Phenomena covered |
| --- | --- | --- |
| Dark energy | f, τᵢ (2; V₀ fixed by Ω_DE) | w₀, wₐ, t_turn (3) |

The same table gives the conjugate-matter sector two parameters for five or more phenomena; that row predates the death of [momentum clumping](/wiki/dark-matter/momentum-clumping) and is not carried into #11, which has no full parameter table. Only the dark-energy row survives as a stated over-constraint.

## In the assessment

#11 §15 lists the dark-energy count among the program's progressive signs: "forced convergence onto consistency islands; predictions not previously posed (rows 3, 11); an unsolicited identity (§7.3); one over-constraint (DE sector)", DE being dark energy. #9 §11 lists "one over-constraint in the DE sector" in the same place. #9 §11 states the criterion behind the word, from [Lakatos's methodology of research programmes](/wiki/method/lakatosian-methodology): "Programs that keep predicting novel facts are progressive; programs that only redescribe are degenerating." An over-constraint is a relation among observables that the model cannot adjust to fit, so it counts as a prediction in that sense. See [assessment: a live research program](/wiki/program/assessment).

## Its reach

The three observables are not equally accessible.

- **w₀ and wₐ** are the near-term observables of [row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift), measured from distances by surveys such as the Dark Energy Spectroscopic Instrument (DESI) ([DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi)). On the count above, those two measurements fix f and τᵢ.
- **t_turn** belongs to [row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion), whose kill column reads "(Long horizon; near-term test is row 4)" (#11 §13). The over-constraint therefore has no near-term test of its own.

The third leg also rests on a point the sources leave unresolved. A turnaround needs the vacuum energy to become negative: "Once τ rolls past V = 0, the effective vacuum energy is negative, expansion halts, and slow contraction begins" (#1 §7 item 3). But V₀[1 + cos(τ/f)] is never negative when V₀ > 0, and no document reconciles the two statements ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); flag 27 in `review/wiki-build-flags.md`). Until that conflict is settled, t_turn is not defined for the potential as written.

The near-term legs are also under pressure. The second DESI data release favours a w(z) that crosses below −1 at redshifts above about 0.4, which τ cannot produce ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)); per the root `CLAUDE.md`, "The dark-energy sector is under real pressure ahead of DR3", DR3 being DESI's Data Release 3.

## History

- **v0.1 (#1 §7 item 4; §10).** The count is stated [D] and tabulated.
- **v1 (#9 §8; §11).** The count with its premise, "V₀ fixed by Ω_DE", and the over-constraint among the progressive signs.
- **#11 (§10; §15).** Unchanged in every version from v2.0 to v2.2.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the current statement
- `papers/broken-born-checkpoint-v2.md` §15 — the over-constraint as a progressive sign
- `papers/broken-born-checkpoint-v2.md` §13 rows 4–5 — the near-term and long-horizon tests
- `notes/broken-born-theory.md` §3 — the action and potential; §7 item 4 — the derivation and its tag; item 3 — the turnaround needs negative vacuum energy
- `notes/broken-born-theory.md` §10 — the per-sector parameter count
- `notes/broken-born-program-v1.md` §8 — "V₀ fixed by Ω_DE, two remaining parameters (f, τᵢ) for three observables"; §11 — "one over-constraint in the DE sector"
- `CLAUDE.md` 'Since the handoff' — "under real pressure ahead of DR3"
