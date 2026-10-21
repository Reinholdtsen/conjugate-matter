---
title: "Safety by range: X and ordinary matter"
weight: 90
status: alive
description: "Ordinary matter feels X at gravitational strength but only within the Yukawa range 1/M_X, so short-range force bounds are safe; how the argument shifted across the Debt-1 notes."
provenance: [D, T]
sources:
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §4"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §8"
  - "papers/broken-born-checkpoint-v2.md §14 item 5"
  - "papers/broken-born-checkpoint-v2.md §14 item 4"
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
---

*This result explains why ordinary matter shows no sign of the [momentum graviton X](/wiki/gravity/momentum-graviton). Standard Model matter couples to the metric g. Reciprocity forces the program's two spin-2 frames to have equal Planck masses, so the metric g contains the massless graviton and X in comparable proportions, and ordinary matter feels both at gravitational strength. X is massive, so the force it carries is a Yukawa force, which dies away beyond a range of order 1/M_X [T]; gravitational-strength forces of such short range are not constrained by experiment. X is safe because of its range, not because ordinary matter is decoupled from it. The argument changed across the Debt-1 calc notes; the current form is calc note #8's [D + T], carried by [checkpoint #11](/wiki/history/documents/checkpoint) §7.5 [D]. It cites no experimental bound and no value of M_X.*

**Status:** Alive — [D + T] in calc note #8 (`notes/debt1a-iv-beta-coefficients.md` §3); [D] in #11 §7.5 — not machine-checked, and no force measurement is cited. Its gravitational-wave side is [Row 6: the exactly massless graviton](/wiki/predictions/massless-graviton); the open quantitative item beside it is [Open: the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement) (OP5).

## The statement

Calc note #8 §3 [D + T] (see [The Debt-1 calc notes](/wiki/history/documents/debt-1-notes)), where SM is the Standard Model:

> "With equal effective Planck masses (forced by the same symmetry), SM matter — coupled to g — sees both eigenstates with comparable strength; safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X, and gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X."

#11 §7.5 [D] carries it in one phrase: "SM couplings gravitational-strength and Yukawa-cut at 1/M_X". The summary in #8 §4 has X coupled "to ordinary matter only at gravitational strength and short range", and #11 §7 closes with momentum space gravitating "massively and invisibly to everything not polarized its way" ([Born's answer](/wiki/gravity/momentum-graviton/borns-answer)).

## Background: Yukawa forces and their range [T]

A force carried by a massless field, such as gravity or electromagnetism, falls off as 1/r² at every distance. A force carried by a field of mass M is cut off: the static potential between two sources falls as e^(−Mr)/r in units where ℏ = c = 1, so beyond the range 1/M, the mediator's reduced Compton wavelength ℏ/(Mc) in ordinary units, the force is exponentially small. This is the Yukawa form, named after Yukawa's theory of the nuclear force, and "Yukawa-cut at 1/M_X" means this cut-off at the range set by X's mass [T].

Searches for new forces between ordinary bodies, among them torsion-balance tests of gravity at short distance, describe a possible extra force by adding a Yukawa term to Newton's potential [T]:

```text
V(r) = −(G m₁ m₂ / r) · (1 + α e^(−r/λ))
```

Here α measures the extra force's strength relative to gravity and λ its range. A force of "gravitational strength" has α of order one. Such experiments compare the force between test masses at their separation, so their sensitivity falls off once λ is much shorter than that separation, where the Yukawa factor has already removed the force [T]. The sources quote no bound of this kind.

## The argument, step by step

1. **Ordinary matter couples to g.** In [the lab notebook](/wiki/history/documents/lab-notebook)'s action the Standard Model is "minimally coupled to g. Nothing is modified. [P4]" (#1 §3), and #8 §3 restates it as "SM matter — coupled to g". The current postulate [P4](/wiki/program/postulates/p4-polarized-matter) has both kinds of matter couple universally to the phase-space metric H.
2. **The metric g contains both spin-2 eigenstates.** The fields of definite mass are the reciprocity-even combination e + f, the massless graviton, and the odd combination e − f, which is X ([spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity)). The frame e of the metric g is half their sum, e = ½(e + f) + ½(e − f), so matter coupled to g couples to both. The equal Planck masses keep the two weights comparable; #8 states the outcome, "comparable strength", without writing the couplings out.
3. **X's force is cut off beyond 1/M_X.** X is massive ([why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)), so "X-mediated forces on the SM are Yukawa-cut at 1/M_X" (#8 §3).
4. **Gravitational-strength forces at such ranges are unconstrained.** #8 §3: "gravitational-strength short-range forces are experimentally unconstrained down to far below any plausible M_X." Read in terms of the mediator's mass, experiments constrain gravitational-strength Yukawa forces only for mediators far lighter than any value of M_X the note regards as plausible, which is to say only at ranges far longer than 1/M_X.

The words "range, not decoupling" mark what the argument does not claim. Ordinary matter is not shielded from X; it couples to X at gravitational strength. In bimetric gravity in general, the massive spin-2 mode's coupling to matter on g weakens when the second metric's Planck mass is made small compared with the first [T], and the literature's stable heavy-spin-2 regime takes exactly that limit ([Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)). Reciprocity's equal Planck masses close that route, and #8 draws the consequence: with comparable couplings, safety has to come from range.

## Scope and caveats

- **No numbers.** #8 cites no experiment and fixes no value of M_X; #11 fixes none either (M_X is "the polarization-breaking scale", calc note #6 §3). The claim is that any plausible M_X lies far above the masses that experiments reach. No `verify/` script checks it.
- **The gravitational-wave side.** Bounds on the graviton mass from gravitational waves concern the massless eigenstate; in #8 §3's words they "apply to the even eigenstate, which is exactly massless". That claim is prediction row 6 ([Row 6](/wiki/predictions/massless-graviton)).
- **Conjugate matter is different.** Conjugate matter χ couples to X through its [dual stress T̃](/wiki/dark-matter/conjugate-matter/dual-stress), and X exchange between conjugate particles is the [gate mechanism](/wiki/dark-matter/conjugate-matter/gate-mechanism) of their self-interaction (#8 §4: X is "coupled to conjugate matter through the dual stress (the gate)"). The safety argument concerns ordinary matter only.
- **τ has its own argument.** The dark-energy field τ is light, so range cannot protect it; the lab notebook's argument is that it is a "(pseudo-)Goldstone: derivatively coupled, no tree-level Yukawa to SM matter" (#1 §4). See [Fifth-force safety of τ](/wiki/cosmology/dark-energy/tau-fifth-force).
- **"Yukawa-cut in momentum."** The paper on conjugate special relativity (#13) cites the checkpoint for a different reading: X "modifies the dual cone only at short range in momentum [D — §7 of the checkpoint]" (§1), and "dual-geometric effects are Yukawa-cut in momentum [D — checkpoint §7]" (§6) ([two causal cones](/wiki/conjugate-relativity/two-causal-cones)). #11 §7.5's derived statement is the cut at 1/M_X on forces between ordinary bodies; the reading in momentum appears otherwise only among the results that exist in the old chat (`HANDOFF.md` §4; [the chat-only page](/wiki/gravity/momentum-graviton/chat-only-results)). The wiki follows #11's wording ([conflicts between sources](/wiki/history/documents/source-conflicts)).

## What remains open

The same paragraph of #8 §3 logs the quantitative question that the range argument leaves:

> "[Parametrics of the χ dual-stress enhancement — why σ₀ can be nuclear-scale while SM couplings stay gravitational — logged as the main open quantitative item.]"

Conjugate matter's self-scattering, with its low-velocity cross-section σ₀, is mediated by the same X that couples to ordinary matter at gravitational strength, and nothing yet explains the gap in strength. #11 lists it as item 5 of §14, "Dual-stress enhancement parametrics [O]", and §8 calls it the "Main open quantitative item" of the conjugate sector. See [Open: the dual-stress enhancement](/wiki/dark-matter/conjugate-matter/dual-stress-enhancement).

The earlier notes had deferred a quantitative check of ordinary-matter safety to the X propagator (#5 §E, "to be verified when the propagator exists [O]"; #6 §4, "quantify with the propagator later"). #8's range argument replaced that plan without a calculation. The X propagator itself is open as part of the gate-shape problem, #11 §14 item 4 ([Open: the gate shape](/wiki/dark-matter/conjugate-matter/gate-shape)).

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
- `notes/debt1a-iii-tuning-test.md` §4 — the mixing-angle form [T]
- `notes/debt1a-ii-X-classification.md` §4 — the unenhanced-dual-stress form
- `notes/debt1a-geometric-core.md` §E — the first, suppressed-dual-stress form [O]
- `notes/broken-born-theory.md` §3 — the Standard Model minimally coupled to g; §4 — τ's separate fifth-force argument; 'Addendum (v0.6)' — "SM safety by Yukawa range"
- `notes/broken-born-program-v1.md` §5 — the superseded v1 statement
- `papers/conjugate-special-relativity.md` §1, §6 — the "short range in momentum" and "Yukawa-cut in momentum" readings
- `HANDOFF.md` §4 — the chat-only results, where the momentum reading appears
