---
title: "Row 9: no linear photon dispersion"
weight: 100
status: alive
description: "The correction to the speed of light linear in photon energy is exactly zero, protected by the residual symmetry ρ² in the lab notebook's schematic argument, and the quadratic one is suppressed; Fermi Large Area Telescope bounds from gamma-ray bursts exclude a linear Planck-scale term, and #13 reads them as a test of both light cones."
provenance: [D, T]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 row 9"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §5"
  - "papers/broken-born-checkpoint-v2.md §15"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-theory.md 'Addendum (v0.2, after the clumping notes)'"
  - "notes/broken-born-program-v1.md §9"
  - "papers/conjugate-special-relativity.md §6"
  - "papers/conjugate-special-relativity.md §1"
  - "review/v3-worklog.md 'New open items' O3"
  - "papers/reciprocity-toy-models.md §1"
  - "papers/reciprocity-toy-models.md §2"
  - "verify/toy_coset.py anchors, S2"
  - "review/round4/referee/audit-notes.md Step 2(c), Step 3"
  - "review/wiki-build-flags.md item 1"
  - "review/wiki-build-flags.md item 31"
  - "review/wiki-build-checks/audit/vasileiou2013.txt"
---

*Row 9 predicts that the speed of light in vacuum has no correction proportional to a photon's energy. Some approaches to quantum gravity predict such a linear correction, suppressed only by the [Planck energy](/wiki/gravity/spin-2-fields/planck-units#the-scale-of-quantum-gravity-t); it would make high-energy photons from a distant gamma-ray burst arrive measurably earlier or later than low-energy photons emitted with them, and burst observations with the Fermi Large Area Telescope exclude it [T]. In the program the linear term is exactly zero, protected by the residual symmetry ρ², the half-turn (x, p) → (−x, −p) of [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), and the leading allowed correction is quadratic in the energy and strongly suppressed. The protection argument is a schematic one, made only in [the lab notebook](/wiki/history/documents/lab-notebook) before the polarization became [a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle); no later document restates it. A confirmed linear dispersion would kill the row.*

**Status:** Alive — the protection argument [D, schematic] and the observational statement [T] both come from the lab notebook (#1 §4), and #11's row cites the ρ² protection without restating the argument — not machine-checked; no program document gives a reference for the bound.

## The row

[Checkpoint #11](/wiki/history/documents/checkpoint) §13, row 9:

| Observable | Standard expectation | Program requirement | Killed by |
| --- | --- | --- | --- |
| Photon dispersion | GR none; some QG linear | Linear exactly zero (ρ²-protected); quadratic suppressed | Confirmed linear-in-E dispersion |

GR is [general relativity](/wiki/gravity/spin-2-fields/general-relativity) and QG quantum gravity; E is the photon energy.

## The observable [T]

In vacuum a photon's energy and momentum satisfy E = c|p|, so light of every energy travels at the same speed c. A dispersion relation states how energy depends on momentum, and a medium, or a modification of spacetime at short distances, can make the speed depend on the energy. Corrections from quantum gravity are expected to be suppressed by a large energy scale E_QG, near the Planck energy, and are written as a series in E/E_QG (the wiki's reading of the standard parametrization):

```text
E² = p²c² [1 + ξ₁ (E/E_QG) + ξ₂ (E/E_QG)² + …]
```

The term in ξ₁ is the linear dispersion, the term in ξ₂ the quadratic. A linear term changes the speed of light by a fraction of order E/E_QG, a quadratic term by a fraction of order (E/E_QG)², which is far smaller at any accessible energy.

The test is a race over cosmological distances. A gamma-ray burst emits photons over a wide range of energies within a short interval, and from far away; a speed that depends on energy makes photons of different energies arrive at different times, by an amount that grows with the distance and with the energy difference. Bursts observed by the Large Area Telescope (LAT) of the Fermi Gamma-ray Space Telescope, which records high-energy gamma rays, therefore bound the linear term [T].

## The standard expectation

"GR none; some QG linear" (#11 §13). General relativity, like [special relativity](/wiki/conjugate-relativity/special-relativity), has exact local Lorentz invariance, and photons in vacuum do not disperse [T]. Some approaches to quantum gravity predict an energy-dependent speed of light with a linear term, and the proposal to test this with gamma-ray bursts is G. Amelino-Camelia, J. Ellis, N. E. Mavromatos, D. V. Nanopoulos and S. Sarkar, "Tests of quantum gravity from observations of γ-ray bursts," Nature 393, 763 (1998) (†, cited from memory; no program document cites it). The lab notebook's version of the column: "None (GR); linear in some QG" (#1 §9).

## The program's requirement

### The protection argument

The [lab notebook](/wiki/history/documents/lab-notebook) makes the argument in one paragraph, under the heading "No linear Lorentz violation" (#1 §4; quotations from #1 on this page are transcribed from its LaTeX):

> Corrections to x-sector dispersion require insertions of the symmetry-breaking spurion ⟨J⟩. Under the residual ρ² (a phase-space parity), operators linear in energy are odd and forbidden; the leading allowed corrections are quadratic, E² = p² + m² + ξ p⁴/M_B², and gravitationally suppressed. **[D, schematic]**

Its three steps:

1. **Corrections need the order parameter.** The x-sector is ordinary matter and light, which [P4](/wiki/program/postulates/p4-polarized-matter) couples to the spacetime metric with nothing modified: "Exact at tree level in the x-sector by construction (P4, P5). [D]" (#1 §4). A departure from E = c|p| must come from the broken symmetry, through the vacuum value ⟨J⟩ of the order parameter J = η⁻¹H ([the order parameter: J, η and K](/wiki/symmetry-breaking/order-parameter)). A spurion is a symmetry-breaking quantity treated as if it were a field that transforms under the symmetry, so that the symmetry still decides which terms it can generate ([spontaneous versus explicit breaking](/wiki/symmetry-breaking/spontaneous-symmetry-breaking#spontaneous-versus-explicit-breaking) [T]).
2. **The residual symmetry.** The vacuum leaves ρ² unbroken. In #1 §2 [D], "ρ²: (x,p) → (−x,−p) preserves *all three* structures. The breaking pattern is ℤ₄ → ℤ₂", the unbroken group being ℤ₂ = {1, ρ²}. ρ reverses the sign of the neutral metric η, so ρ² reverses it twice and leaves it, and with it ⟨J⟩, unchanged. Terms generated by ⟨J⟩ must therefore respect ρ², the phase-space parity that reverses both position and momentum.
3. **Linear terms are odd.** "Operators linear in energy are odd and forbidden", so the first allowed correction is quadratic. Its scale is M_B, the mass scale of the notebook's geometric action, S_H = ½M_B²∫√|H| R_B[H], from which "M_P fixed by M_B and the section volume" [D, schematic] (#1 §3). With M_B ~ M_P the quadratic term is suppressed by the square of the Planck mass, which, in the wiki's reading, is what "gravitationally suppressed" means.

The notebook does not show how an operator linear in energy transforms under ρ², and no later document fills in the step. #1 tags the whole argument [D, schematic], a sketch rather than a derivation, and it is not machine-checked.

### What #11 keeps

#11 carries the conclusion in the row, "Linear exactly zero (ρ²-protected); quadratic suppressed", and restates none of the argument; no section of #11 corresponds to #1 §4's consistency checks. The notebook's "gravitationally suppressed" became "suppressed" in v1 and #11 (History, below).

## The argument after P2′

The argument was made under the [original P2](/wiki/program/postulates/original-p2), in which [the symplectic form ω](/wiki/phase-space/reciprocity/symplectic-form) and the neutral metric η are both rigid; under it, as #11 §5 states, "the compatible polarizations are discrete" (a statement queried for d ≥ 2 in flag 1 of `review/wiki-build-flags.md`). The program replaced it with [P2′](/wiki/program/postulates/p2-prime), in which only ω is rigid and η is the order parameter. Since v2.2, from [the toy models](/wiki/symmetry-breaking/toy-models): "with only ω rigid, ρ sits inside a continuous U(1), and the polarization is a Goldstone angle rather than a discrete choice [D][V]" (#11 §4; [the polarization as a Goldstone angle](/wiki/symmetry-breaking/goldstone-angle)). The Goldstone picture governs, and the breaking pattern ℤ₄ → ℤ₂ is superseded ([Superseded: the discrete breaking pattern](/wiki/symmetry-breaking/order-parameter#superseded-the-discrete-breaking-pattern)).

ρ² itself survives in the toy models, for d = 1:

- ρ "is symplectic and squares to −1" (toy note §1), so ρ² = −1, the phase-space parity (x, p) → (−x, −p). "The stabilizer of (1, K₀) in Sp(2,ℝ) is {±1}" (toy note §2): the vacuum of [the coset model](/wiki/symmetry-breaking/toy-models/coset-model) keeps exactly {1, ρ²}.
- [The gate](/wiki/method/verification/the-gate) checks both statements ([the toy-model scripts](/wiki/method/verification/toy-model-scripts)):

```text
PASS  rho is symplectic and is the quarter turn: rho^2 = -1
PASS  the stabilizer of the vacuum (1, K0) in Sp(2,R) is {+1, -1} (so the orbit is 3-dimensional)
```

- With the ρ-preserving potential in the [frozen-H reduction](/wiki/symmetry-breaking/toy-models/coset-model/frozen-h-reduction), the [round-4](/wiki/method/review/round-4) referee found the residual group inside the rotations to be {±1, ±ρ}, which contains ρ² (`review/round4/referee/audit-notes.md`, Step 2(c) and Step 3; [what remains of it](/wiki/symmetry-breaking/order-parameter#superseded-the-discrete-breaking-pattern)). The potential examined was the note's first form, which the same review found unbounded once H moves ([Obituary: the naive ρ-preserving potential](/wiki/symmetry-breaking/toy-models/coset-model/naive-potential#the-residual-symmetry)).

No document applies these statements to row 9, restates the protection argument in the Goldstone picture, or extends it from the toy's d = 1 to phase space over 3+1 dimensions. The row's rationale exists only in #1.

## #13's joint reading

[Conjugate special relativity](/wiki/conjugate-relativity) (#13 §6) adds a reading of the same bounds; #13 tags the bounds [T] and gives the reading no tag of its own:

> "One free consistency check already available: since our massless dispersion E = c|p| *is* the dual null cone, the Fermi-LAT bounds excluding linear photon-dispersion violations [T] constrain both cones at once — every test of our light cone's rigidity has been, unknowingly, a test of theirs."

The dual null cone is the light cone of momentum space ([two causal cones](/wiki/conjugate-relativity/two-causal-cones)). The reading is unsettled. #13 §1 builds its dual cone in time and momentum, with slope the [maximum force c̃](/wiki/conjugate-relativity/maximum-force), while §6's statement, in the v3 worklog's words, "belongs to the 4D Born map (t ↔ E): a cone in (E, p) with slope c". The worklog's instruction: "Before any paper claims more: fix #13's two cones and settle which construction governs (raised by Paul, 2026-10-19)" (`review/v3-worklog.md`, item O3; [Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency#the-photon-dispersion-argument)). The four-dimensional map itself is open ([Open: the four-dimensional Born map and dual dynamics](/wiki/conjugate-relativity/four-dimensional-born-map)). #11's row makes no reference to #13.

## What kills it

"Confirmed linear-in-E dispersion" (#11 §13): an energy-dependent speed of light in vacuum with a term linear in E, established by the arrival times of photons from distant sources or by any other test. A quadratic term at the strength the notebook expects would not kill the row; the row requires it to be suppressed, not absent. v0.1's wording was "Any confirmed linear-in-E dispersion" (#1 §9).

## The data situation

The record's statement of the data is the lab notebook's (#1 §4, [T]):

> Fermi-LAT gamma-ray-burst bounds exclude linear Planck-scale dispersion; quadratic effects at M_B ~ M_P sit ~10 orders below current sensitivity. Consistent.

No program document cites a paper for this statement, and no `verify/` script checks the "~10 orders"; the wiki repeats it as written. Flag 31 in `review/wiki-build-flags.md` records a lead that the figure may be off. The flags' audit retrieved the bound by live search [S], E_QG,2 > 1.3×10¹¹ GeV from the Fermi Large Area Telescope (Vasileiou et al. 2013; `review/wiki-build-checks/audit/vasileiou2013.txt`), and found that the "~10 orders" hold only loosely, as a count of orders in the energy scale, the way such limits are quoted: 8.0–8.6, or 7.3–7.9 with #1's reduced Planck mass. Counted instead in the size of the effect, the reading the audit takes the notebook's "quadratic effects" to suggest, the gap is 14.5–17 orders. The audit rated the flag as depending on that reading; the notebook's "Consistent" survives either way. #13 §6 cites the same bounds, also without a reference. The standard reference for the Fermi bound from a single burst is A. A. Abdo et al., "A limit on the variation of the speed of light arising from quantum gravity effects," Nature 462, 331 (2009) (†, cited from memory; no program document cites it). The program's references register lists the bounds as cited without a reference ([references](/wiki/references)).

The data are consistent with the row: no linear dispersion has been found, and by the notebook's estimate the quadratic term it expects lies far below what current observations reach. #11 §15 names rows 1, 4 and 7 as the program's near-term falsification exposure; row 9 is not among them.

## History of the row

| Version | Requirement | Killed by |
| --- | --- | --- |
| v0.1 (#1 §9) | "Linear term exactly zero (protected by ρ²); quadratic allowed, gravitationally suppressed" | "Any confirmed linear-in-E dispersion" |
| v1 (#9 §9) | "Linear term exactly zero (protected by ρ²); quadratic allowed, suppressed" | "Confirmed linear-in-E dispersion" |
| #11 §13 | "Linear exactly zero (ρ²-protected); quadratic suppressed" | "Confirmed linear-in-E dispersion" |

The substance has not changed since the notebook. v1 dropped "gravitationally" and "Any"; #11's v2.0 shortened the wording, and v2.1 and v2.2 left it unchanged. The notebook's v0.2 addendum, which lists the program's still-live content after [the clumping problem](/wiki/history/main-problems), groups rows 7–9 as "permanent nulls" ('Addendum (v0.2, after the clumping notes)'). The whole table's history is on [the history of the predictions table](/wiki/predictions/table-history).

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 row 9 — the row; §4 — P2′ and the Goldstone-angle refinement [D][V]; §5 — discrete polarizations under strict P2; §15 — the near-term rows
- `notes/broken-born-theory.md` §4 — the protection argument [D, schematic] and the bound [T]; §2 — the breaking pattern ℤ₄ → ℤ₂ [D]; §3 — the scale M_B; §9 — v0.1's row 9; 'Addendum (v0.2, after the clumping notes)' — "permanent nulls". Quotations are transcribed from its LaTeX.
- `notes/broken-born-program-v1.md` §9 — v1's row 9
- `papers/reciprocity-toy-models.md` §1, §2 and `verify/toy_coset.py` (anchors, S2) — ρ² = −1 and the stabilizer {±1} in the coset model [V]
- `review/round4/referee/audit-notes.md` Step 2(c), Step 3 — the residual group {±1, ±ρ} with the potential at frozen H
- `papers/conjugate-special-relativity.md` §6 — the joint test of both cones; §1 — the dual cone in time and momentum
- `review/v3-worklog.md` 'New open items', item O3 — the two dual cones, unsettled
- `review/wiki-build-flags.md` item 1 — discreteness of the polarizations under strict P2; item 31 — the "~10 orders" for the quadratic term, with the audit's live-searched bound and its two readings
- `review/wiki-build-checks/audit/vasileiou2013.txt` — the text of the Fermi Large Area Telescope paper the audit retrieved [S]
