---
title: "Safety by range: X and ordinary matter"
weight: 90
status: alive
description: "Ordinary matter feels X at gravitational strength but only within the Yukawa range 1/M_X, so short-range force bounds are safe; how the argument shifted across the Debt-1 notes, and the bound a later note derived from it for the aligned vacuum."
provenance: [D, T]
sources:
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §4"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §14 item 5"
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
  - "papers/phase-space-diameter.md §8.2"
  - "papers/phase-space-diameter.md §9"
  - "verify/phase_space_diameter.py 'Consequences (note §8)'"
  - "review/round5-adjudication.md 'Rulings' R1"
  - "notes/debt1a-iii-tuning-test.md §4"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-geometric-core.md §E"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md 'Addendum (v0.6)'"
  - "notes/broken-born-program-v1.md §5"
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §6"
  - "HANDOFF.md §4"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/wiki-build-flags.md item 29"
  - "review/wiki-build-flags.md item 55"
  - "notes/gate-mechanism.md §2"
  - "notes/gate-mechanism.md §3"
---

*This result explains why ordinary matter shows no sign of the [momentum graviton X](/wiki/gravity/momentum-graviton). Standard Model matter couples to the metric g. [Reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) forces the program's two spin-2 frames to have [equal Planck masses](/wiki/gravity/momentum-graviton/spectrum-and-parity#equal-planck-masses), so the metric g contains the massless graviton and X in comparable proportions, and ordinary matter feels both at gravitational strength. X is massive, so the force it carries is a [Yukawa force](/wiki/gravity/spin-2-fields/yukawa-forces), which dies away beyond a range of order 1/M_X [T]; gravitational-strength forces of such short range are not constrained by experiment. X is safe because of its range, not because ordinary matter is decoupled from it. The argument changed across [the Debt-1 calc notes](/wiki/history/documents/debt-1-notes); the current form is calc note #8's [D + T], carried by [checkpoint #11](/wiki/history/documents/checkpoint) §7.5 [D]. It cites no experimental bound and no value of M_X. The [phase-space-diameter note](/wiki/cosmology/scale-factor-duality/phase-space-diameter) has since supplied a bound, conditional on the aligned vacuum the program's equations assume: torsion balances keep X's range below 37.7 micrometres, so M_X c² > 5.2 meV ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)).*

**Status:** Alive — [D + T] in calc note #8 (`notes/debt1a-iv-beta-coefficients.md` §3); [D] in #11 §7.5 — the argument itself is not machine-checked and cites no force measurement. The bound on X's range that the phase-space-diameter note adds, conditional on the background ratio u = 1, is [D][V][S] (`papers/phase-space-diameter.md` §8.2; `verify/phase_space_diameter.py`, [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script); [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)). Its gravitational-wave side is [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton); the open quantitative item beside it is [Open: the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement) (OP5).

## The statement

Calc note #8 §3 [D + T] (see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)), where SM is the Standard Model:

> "With equal effective Planck masses (forced by the same symmetry), SM matter — coupled to g — sees both eigenstates with comparable strength; safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X, and gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X."

#11 §7.5 [D] carries it in one phrase: "SM couplings gravitational-strength and Yukawa-cut at 1/M_X". The summary in #8 §4 has X coupled "to ordinary matter only at gravitational strength and short range", and #11 §7 closes with momentum space gravitating "massively and invisibly to everything not polarized its way" ([Born's answer](/wiki/gravity/momentum-graviton/borns-answer)).

## Background: Yukawa forces and their range [T]

A force carried by a field of mass M is a Yukawa force: its static potential falls as e^(−Mr)/r in units where ℏ = c = 1, so beyond the range 1/M, ℏ/(Mc) in ordinary units, the force is exponentially small. "Yukawa-cut at 1/M_X" means this cut-off at the range set by X's mass [T]. Searches for new forces between ordinary bodies write a possible extra force as a Yukawa term beside Newton's potential, V(r) = −(G m₁ m₂ / r)(1 + α e^(−r/λ)), with α its strength relative to gravity and λ its range; a force of "gravitational strength" has α of order one. An experiment loses sensitivity once λ is much shorter than the separation of its test masses, where the Yukawa factor has already removed the force [T]. Calc note #8 and #11 quote no bound of this kind; the phase-space-diameter note quotes the torsion-balance limits of Lee et al. 2020 [S] ([laboratory bounds at short range](/wiki/gravity/spin-2-fields/yukawa-forces#laboratory-bounds-at-short-range)). The derivation, the experiments and scattering through a Yukawa mediator are on [Yukawa forces and their range](/wiki/gravity/spin-2-fields/yukawa-forces).

## The argument, step by step

1. **Ordinary matter couples to g.** In [the lab notebook](/wiki/history/documents/lab-notebook)'s action the Standard Model is "minimally coupled to g. Nothing is modified. [P4]" (#1 §3), and #8 §3 restates it as "SM matter — coupled to g". The current postulate [P4](/wiki/program/postulates/p4-polarized-matter) has both kinds of matter couple universally to the phase-space metric H.
2. **The metric g contains both spin-2 eigenstates.** The fields of definite mass are the reciprocity-even combination e + f, the massless graviton, and the odd combination e − f, which is X ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity); on the parities under #11 §6's Z → −Z⁻¹, see flag 39 in `review/wiki-build-flags.md`). The frame e of the metric g is half their sum, e = ½(e + f) + ½(e − f), so matter coupled to g couples to both. The [equal Planck masses](/wiki/gravity/spin-2-fields/planck-units#equal-planck-masses-in-the-bimetric-sector) keep the two weights comparable; #8 states the outcome, "comparable strength", without writing the couplings out. The literature formula that the phase-space-diameter note uses writes them out: matter on g feels the massive field with strength α = (4/3)(M_f u/M_g)² relative to gravity, where M_g and M_f are the two Planck masses and u is the ratio of the two frames' backgrounds. "Only the product M_f u is fixed by the theory, so equal Planck masses give α = 4/3 only if u = 1", the program's aligned vacuum (note §8.2; round-5 ruling R1; [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)).
3. **X's force is cut off beyond 1/M_X.** X is massive ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)), so "X-mediated forces on the SM are Yukawa-cut at 1/M_X" (#8 §3).
4. **Gravitational-strength forces at such ranges are unconstrained.** #8 §3: "gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X." Read in terms of the mediator's mass, experiments constrain gravitational-strength Yukawa forces only for mediators far lighter than any value of M_X the note regards as plausible, which is to say only at ranges far longer than 1/M_X. The phase-space-diameter note finds the statement "consistent with the bound but gave no number" (§8.2): in the aligned vacuum, torsion balances exclude X's force at ranges above 37.7 μm.

The words "range, not decoupling" mark what the argument does not claim. Ordinary matter is not shielded from X; it couples to X at gravitational strength. In [bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) in general, the massive spin-2 mode's coupling to matter on g weakens when the second metric's Planck mass is made small compared with the first [T], and the literature's stable heavy-spin-2 regime takes exactly that limit (`review/v3-worklog.md` item R7: "their viable regime takes **M_f ≪ M_g**"; [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)). Reciprocity's equal Planck masses close that route, and #8 draws the consequence: with comparable couplings, safety has to come from range.

## Scope and caveats

- **Numbers.** #8 cites no experiment and fixes no value of M_X; #11 fixes none either (M_X is "the polarization-breaking scale", calc note #6 §3). The claim is that any plausible M_X lies far above the masses that experiments reach, and no `verify/` script checks the argument itself. The phase-space-diameter note (v1.1 §8.2) puts a number on it. With α = 4/3, the one-sided limit of the torsion-balance experiment of Lee et al. 2020 gives λ_X < 37.7 μm and M_X c² > 5.2 meV [V], conditional on the background ratio u = 1, whose persistence as the universe expands is open [O]. For other u the limit moves, to 57.0 μm at u = 0.5 [V]. The note's summary tags the bound [V][S] (§9), and `verify/phase_space_diameter.py` recomputes it ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)).
- **The gravitational-wave side.** Bounds on the graviton mass from gravitational waves concern the massless eigenstate; in #8 §3's words they "apply to the even eigenstate, which is exactly massless". That claim is prediction row 6 ([Row 6](/wiki/predictions/massless-graviton)).
- **Conjugate matter is different.** [Conjugate matter](/wiki/dark-matter/conjugate-matter) χ couples to X through its [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress), and X exchange between conjugate particles is the [gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism) of their self-interaction (#8 §4: X is "coupled to conjugate matter through the dual stress (the gate)") (not derived, according to flag 55 in `review/wiki-build-flags.md`, pending Paul's ruling; [the gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism#exchanging-x-cannot-produce-the-gate)). The safety argument concerns ordinary matter only.
- **τ has its own argument.** The [dark-energy field τ](/wiki/cosmology/dark-energy/tau-quintessence) is "ultralight", so its protection cannot be range; the lab notebook's argument is that it is a "(pseudo-)Goldstone: derivatively coupled, no tree-level Yukawa to SM matter" (#1 §4; [axion-like fields and pseudo-Goldstone bosons](/wiki/cosmology/dark-energy/axion-like-fields#τ-an-axion-like-dark-energy-field)). See [Fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force).
- **The reading "Yukawa-cut in momentum".** The paper on [conjugate special relativity](/wiki/conjugate-relativity) (#13) cites the checkpoint for a different reading: X "modifies the dual cone only at short range in momentum [D — §7 of the checkpoint]" (§1), and "dual-geometric effects are Yukawa-cut in momentum [D — checkpoint §7]" (§6) ([two causal cones](/wiki/conjugate-relativity/two-causal-cones)). #11 §7.5's derived statement is the cut at 1/M_X on forces between ordinary bodies; the reading in momentum appears otherwise only among the results that exist in the old chat (`HANDOFF.md` §4; [the chat-only page](/wiki/gravity/momentum-graviton/chat-only-results)). The wiki follows #11's wording ([conflicts between sources](/wiki/history/documents/source-conflicts); see flag 29 in `review/wiki-build-flags.md`).

## What remains open

The same paragraph of #8 §3 logs the quantitative question that the range argument leaves:

> "[Parametrics of the χ dual-stress enhancement — why σ₀ can be nuclear-scale while SM couplings stay gravitational — logged as the main open quantitative item.]"

Conjugate matter's self-scattering is mediated by the same X that couples to ordinary matter at gravitational strength, yet its low-velocity cross-section σ₀ has to be large; #11 §8 calls the item the "Main open quantitative item: the dual-stress enhancement (nuclear-scale σ₀ with gravitational SM couplings) [O]". No document explains the gap in strength. #11 lists it as item 5 of §14, "Dual-stress enhancement parametrics [O]". See [Open: the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).

The earlier notes had deferred a quantitative check of ordinary-matter safety to the X propagator (#5 §E, "to be verified when the propagator exists [O]"; #6 §4, "quantify with the propagator later"). #8's range argument replaced that plan without a calculation. #11 §14 item 4 lists the X propagator, on the [momentum fibers](/wiki/phase-space/reciprocity/momentum-fibers#the-x-propagator-on-the-fibers-op4), as part of the open gate-shape problem; `notes/gate-mechanism.md` §3 finds that within #11 §7 a propagator on the fibers has no meaning, because the section condition makes X depend on position only (flag 55) ([Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)).

## Superseded: earlier forms of the safety argument

The argument took four forms in the four Debt-1 calc notes. The first two combined X's short range with a weak coupling of ordinary matter to X through its dual stress; the third required the massless combination to dominate the couplings of ordinary matter; the fourth, current one rests on range alone, with couplings of gravitational strength.

- **Calc note #5 §E [O]:** "SM safety: X is massive and couples to x-polarized matter only through its (suppressed) dual stress; short-range, fifth-force-safe — to be verified when the propagator exists [O]."
- **Calc note #6 §4:** "Massive X ⇒ short-ranged, safe; couplings to x-polarized (SM) matter run through the SM's dual stress, which is unenhanced. [Consistency preserved; quantify with the propagator later.]"
- **Calc note #7 §4 [T]:** "one massless combination (our graviton, coupling to SM stress) and one massive (X); safety requires the massless combination to dominate SM couplings — a parametric check to log". The same sentence adds graviton-mass bounds from gravitational-wave observations, "m_g ≲ 10⁻²³ eV territory", as a check on the mixing angle ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity) covers that reading).
- **Calc note #8 §3 [D + T]:** the statement above. Once reciprocity forces equal Planck masses, ordinary matter "sees both eigenstates with comparable strength", so the massless combination does not dominate its couplings as #7 required, and safety rests on range instead.

The lab notebook's v0.6 addendum records the change as "SM safety by Yukawa range"; the v1 paper (#9 §5 item 6) has "SM couplings to X are gravitational-strength and Yukawa-cut at 1/M_X"; #11 §7.5 keeps that form. The wiki follows #8 as closest to #11 §7.5 ([conflicts between sources](/wiki/history/documents/source-conflicts)).

## Sources

- `notes/debt1a-iv-beta-coefficients.md` §3 — the current argument [D + T] and the open enhancement item; §4 — X coupled to ordinary matter "only at gravitational strength and short range"
- `papers/broken-born-checkpoint-v2.md` §7.5 — the current statement [D]; §7 — the closing summary; §8 — the "Main open quantitative item"; §14 items 4 and 5 — the gate shape and the dual-stress enhancement [O]
- `papers/phase-space-diameter.md` §8.2 — the coupling α = (4/3)(M_f u/M_g)², the premise u = 1, the torsion-balance bound λ_X < 37.7 μm, M_X c² > 5.2 meV, and #8's statement found "consistent with the bound but gave no number" [D][V][S]; §9 — the bound's tags [V][S]
- `verify/phase_space_diameter.py` 'Consequences (note §8)' — the bound recomputed from the experiment's exclusion table [V]
- `review/round5-adjudication.md` 'Rulings' R1 — the background ratio that the first version of the bound dropped
- `notes/debt1a-iii-tuning-test.md` §4 — the mixing-angle form [T]
- `notes/debt1a-ii-X-classification.md` §4 — the unenhanced-dual-stress form
- `notes/debt1a-geometric-core.md` §E — the first, suppressed-dual-stress form [O]
- `notes/broken-born-theory.md` §3 — the Standard Model minimally coupled to g; §4 — τ's separate fifth-force argument; 'Addendum (v0.6)' — "SM safety by Yukawa range"
- `notes/broken-born-program-v1.md` §5 — the superseded v1 statement
- `papers/conjugate-special-relativity.md` §1, §6 — the "short range in momentum" and "Yukawa-cut in momentum" readings
- `HANDOFF.md` §4 — the chat-only results, where the momentum reading appears
- `review/v3-worklog.md` 'Round-2 pending list' — item R7: the stable heavy-spin-2 regime takes M_f ≪ M_g
- `review/wiki-build-flags.md` item 29 — #13's citation of #11 §7 for X's effect being in momentum, which #11 does not state; awaiting Paul's ruling
- `notes/gate-mechanism.md` §2, §3 and `review/wiki-build-flags.md` item 55 — exchanging #11 §7's X cannot produce the gate; no X propagator on the fibers within §7; awaiting Paul's ruling
