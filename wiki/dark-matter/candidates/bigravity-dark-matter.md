---
title: "Bigravity dark matter"
weight: 30
status: established
description: "Massive spin-2 fields of bimetric gravity as dark matter (Babichev et al.) — the lineage of the X-condensate candidate."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md ref [23]"
  - "papers/broken-born-checkpoint-v2.md §7"
  - "papers/broken-born-checkpoint-v2.md §14 item 10"
  - "notes/debt1a-ii-X-classification.md §3"
  - "notes/debt1a-ii-X-classification.md §4"
  - "notes/debt1a-ii-X-classification.md §5"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "notes/debt1a-geometric-core.md §C"
  - "notes/broken-born-theory.md 'Addendum (v0.4)'"
  - "notes/broken-born-program-v1.md §10"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/wiki-build-flags.md item 7"
  - "review/wiki-build-flags.md item 5"
  - "review/wiki-build-flags.md item 20"
---

*Bigravity dark matter is the proposal, from the literature on bimetric gravity, that [dark matter](/wiki/dark-matter) is the [massive spin-2](/wiki/gravity/spin-2-fields) particle of a theory with two interacting metrics. In ghost-free bimetric gravity the two metrics combine into a massless graviton, which carries ordinary gravity, and a massive spin-2 field; Babichev and collaborators proposed in 2016 that this heavy field makes up the dark matter. The program's [momentum graviton X](/wiki/gravity/momentum-graviton) is a massive spin-2 field of the same bimetric kind, so this literature is the lineage of the program's [X-condensate candidate](/wiki/dark-matter/candidates/x-condensate). The program cites it only for that lineage, from model memory, and has not yet checked the source.*

**Status:** Established — literature [T], explained here from general knowledge. The single citation, Babichev et al. [23†], is from model memory and awaits source-checking under [the † literature battery](/wiki/method/literature-battery). The program cites it as the "bigravity-DM lineage" of the X-condensate ([#11](/wiki/history/documents/checkpoint) §12), where DM is dark matter. Nothing on this page is machine-checked.

## The idea

A dark-matter candidate has to do four things [T]: gravitate like ordinary matter, move slowly enough to let structure form (be "cold"), survive for the age of the universe, and be present in the observed amount. A massive spin-2 particle of a bimetric theory meets the first by construction, since it is part of the gravitational sector, and it carries no charge under the forces of the Standard Model (SM) [T]. Bigravity dark matter is the proposal that this particle, the heavy mass eigenstate of a two-metric theory, is the dark matter (Babichev et al. [23†]). Whether it is cold, long-lived and correctly abundant depends on its mass and on how strongly it couples to ordinary matter, and those are fixed by the parameters of the bimetric theory.

## The setting: two interacting metrics [T]

Bimetric gravity has two dynamical metrics, g and f, each with its own [Einstein–Hilbert term](/wiki/gravity/spin-2-fields/general-relativity) and its own [Planck mass](/wiki/gravity/spin-2-fields/planck-units#two-metrics-two-planck-masses), M_g and M_f, and an interaction potential between them; ordinary matter couples to g [T]. A generic interaction brings in an extra mode with negative energy, the Boulware–Deser ghost ([Fierz–Pauli theory](/wiki/gravity/spin-2-fields/fierz-pauli)). The ghost-free potentials are those of [dRGT massive gravity](/wiki/gravity/spin-2-fields/drgt-massive-gravity), which Hassan and Rosen extended to two dynamical metrics ([Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric); [10†, 11†]).

#11 states the uniqueness this way: "The unique consistent structure for massive spin-2 is Fierz–Pauli/dRGT/Hassan–Rosen [9†, 10†, 11†]" (#11 §7.1). [Calc note #6](/wiki/history/documents/debt-1-notes) had written "Massive spin-2 coupled to gravity has exactly one known consistent structure" (#6 §3). The difference in wording, unique versus the one known, is recorded in `review/wiki-build-flags.md` item 7; this page quotes both as written.

Around backgrounds in which the two metrics are proportional, the fluctuations of g and f combine into two mass eigenstates [T]: one massless spin-2 field, which acts as the graviton of ordinary gravity, and one massive spin-2 field with five polarizations. How much of each eigenstate lies along g, and therefore how strongly ordinary matter feels each, is set by the ratio of the two Planck masses [T]. When the second metric's Planck mass is much smaller than the first, the massless eigenstate lies mostly along g, the massive one mostly along f, and the massive eigenstate couples to ordinary matter only weakly [T]. This is the general structure; the parameter choices of the dark-matter proposals are not reported in any program document.

## A coherent oscillation as dark matter [T]

The program's form of the idea is an oscillation, not a gas of particles: "homogeneous oscillations of a massive spin-2 X" (#6 §4), "oscillating massive spin-2" (#11 §12). The mechanism is standard for scalar fields [T]. A massive scalar field displaced from its minimum stays frozen while the expansion rate exceeds its mass, then oscillates with a frequency set by the mass. Averaged over many oscillations its pressure vanishes, so its energy density falls with the cube of the scale factor, like cold, pressureless matter. For a light scalar this is [the misalignment mechanism](/wiki/dark-matter/wave-dark-matter/misalignment-mechanism) of axion dark matter. A spatially uniform oscillation is also coherent: the whole field moves in phase, as a single standing wave rather than a set of independent particles [T]. The X-condensate's profile lists "coherent-field signatures" (#11 §12) without naming them.

A spin-2 field carries a tensor index, so its uniform mode singles out directions in space, and the literature treats homogeneous spin-2 oscillations separately (from model memory: Marzola, Raidal and Urban (2018)†). No program document discusses this.

## The reference

The citation, as #11 gives it:

- [23]† E. Babichev, L. Marzola, M. Raidal, A. Schmidt-May, F. Urban, H. Veermäe, M. von Strauss, "Bigravitational origin of dark matter," Phys. Rev. D 94, 084055 (2016), arXiv:1607.03497.

Flag 20 in `review/wiki-build-flags.md` records a suspected error in this entry, which a verifier of the wiki build found by live search: the title and journal, "Bigravitational origin of dark matter" in Phys. Rev. D 94, 084055, belong to arXiv:1604.08564, while arXiv:1607.03497 is the companion paper "Heavy spin-2 Dark Matter", listed below among the wiki's additions. The flag awaits Paul's ruling and is recorded for the † battery (OP10). The wiki quotes #11 as written.

#11's legend for the mark: "† = cited from model memory — verify before external use". Checking every † reference against its source is #11 §14 item 10, "Literature battery completion; every † reference source-checked [O]" ([Open: the † literature battery (OP10)](/wiki/method/literature-battery)). No document reports what the paper contains beyond its title, so this page does not summarize its production mechanism, its mass range or its parameter choices. Earlier documents name the idea without a reference (#6 §4, [the lab notebook](/wiki/history/documents/lab-notebook)'s addendum v0.4, #9 §10); the register entry is on [references](/wiki/references).

## Where the program meets it

The idea entered the program at the classification of X. Once calc note #6 had shown that X is a massive spin-2 field, it noted: "A new door, deliberately left closed today: homogeneous oscillations of a massive spin-2 X are themselves a dark-matter candidate (cf. bigravity dark matter)" [O] (#6 §4), and listed "X-condensate dark matter (§4)" among what is "Also now open" (#6 §5). The lab notebook's addendum v0.4 called it "massive-X condensate as the dark matter itself (bigravity-DM-style), potentially unifying the dark sector with the geometry". #9 kept it as open problem 7, "[O — direction, deliberately unopened]" (#9 §10). #11 made it a candidate and gave the lineage its reference: "oscillating massive spin-2 (bigravity-DM lineage [23†])" (#11 §12). The candidate's own page follows that history ([the X-condensate candidate](/wiki/dark-matter/candidates/x-condensate)).

## How the program's X differs

The program does not add a second metric; it finds one, and the constraints that come with it fix several of the parameters the general theory leaves free.

- **Where X comes from.** X is the real part of the modular field Z = X + iY, whose imaginary part is the spacetime metric (#5 §C; [the modular field Z](/wiki/phase-space/modular-field/modular-field-z)). Its mass is not put in by hand: "The polarization choice spontaneously breaks the dual diffs; X eats the four Goldstones and emerges massive, M_X = the polarization-breaking scale" (#11 §7.1 [D + T]; [why X must be massive](/wiki/gravity/momentum-graviton/forcing-chain)).
- **Which potentials.** [Reciprocity](/wiki/phase-space/reciprocity/born-reciprocity) restricts the five coefficients βₙ of the Hassan–Rosen potential to the [palindromic branch](/wiki/gravity/palindromic-branch/palindrome) βₙ = β₄₋ₙ, and with a flat vacuum two parameters remain: "Five βₙ → two parameters (M_X ∝ 2(β₁+β₂); one cubic shape)" (#11 §7.5 [D]; flag 5 in `review/wiki-build-flags.md` suspects that the proportionality is meant for M_X²).
- **The Planck masses.** Reciprocity forces "equal effective Planck masses", so that "SM matter — coupled to g — sees both eigenstates with comparable strength; safety is by **range**, not decoupling: X-mediated forces on the SM are Yukawa-cut at 1/M_X" (#8 §3; [spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity); [Yukawa forces](/wiki/gravity/spin-2-fields/yukawa-forces#the-momentum-graviton-x)). The program's X therefore sits away from the regime M_f ≪ M_g described above.
- **Cosmological stability.** For the same reason, the regime in which a heavy spin-2 field has been shown linearly stable at late times ([bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology)) is unavailable. The v3 worklog: reciprocity "forces equal effective Planck masses (M_f = M_g), which rules out the M_f ≪ M_g escape", and whether "a large mass alone is enough at M_f = M_g is open" (item R7; [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)).

No document compares these features with the parameter choices of the bigravity dark-matter literature.

## References

As #11 gives them:

- [23]† Babichev et al. (2016), above: the lineage.
- [9]† C. de Rham, G. Gabadadze, A. J. Tolley, "Resummation of massive gravity" (2011); [10]† and [11]† S. F. Hassan, R. A. Rosen (2012): ghost-free massive and bimetric gravity.
- [22][S] A. Schmidt-May, M. von Strauss, "Recent developments in bimetric theory" (2016): a review of the theory, which #11 cites for its statement on [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem).

Added by the wiki from model memory (†), not cited by any program document:

- E. Babichev, L. Marzola, M. Raidal, A. Schmidt-May, F. Urban, H. Veermäe, M. von Strauss, "Heavy spin-2 Dark Matter" (2016)†: a companion paper on the heavy spin-2 particle as dark matter. Flag 20 identifies it as arXiv:1607.03497, the number #11 attaches to [23].
- L. Marzola, M. Raidal, F. R. Urban, "Oscillating spin-2 dark matter" (2018)†: homogeneous oscillations of a massive spin-2 field.

## Used by

- [The X-condensate candidate](/wiki/dark-matter/candidates/x-condensate) — its lineage, in #11 §12's candidate table.
- [Row 11: particles or condensate](/wiki/predictions/dark-sector-microstructure) — the coherence signatures that would separate a condensate from particles.
- [Open: the † literature battery (OP10)](/wiki/method/literature-battery) — reference [23]† among the citations awaiting source-checking.

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — "bigravity-DM lineage [23†]"; ref [23] — the citation and the legend for †; §7.1 — X forced massive, the uniqueness statement; §7.5 — the two parameters; §14 item 10 — the literature battery
- `notes/debt1a-ii-X-classification.md` §3 — "exactly one known consistent structure"; §4 — "cf. bigravity dark matter"; §5 — the X-condensate listed as open
- `notes/debt1a-iv-beta-coefficients.md` §3 — equal effective Planck masses, safety by range
- `notes/debt1a-geometric-core.md` §C — X as Re Z
- `notes/broken-born-theory.md` 'Addendum (v0.4)' — "bigravity-DM-style"
- `notes/broken-born-program-v1.md` §10 — open problem 7 of #9
- `review/v3-worklog.md` 'Round-2 pending list' — R7, equal Planck masses and late-time stability
- `review/wiki-build-flags.md` item 7 — the wording of the uniqueness statement; item 5 — M_X or M_X² in the two-parameter count; item 20 — the title and arXiv number of reference [23]
