---
title: "The cosmological constant Λ"
weight: 3
status: established
description: "Λ in Einstein's equations as a constant energy density of empty space with w = −1 exactly: the dark energy of ΛCDM, the acceleration and empty de Sitter future it implies, anti-de Sitter for negative Λ, the standard expectation of rows 4 and 5, and the program's uses — τ in its place, dual kinetic energy acting as a Λ, the bimetric potential's constant terms, and the negative effective Λ the turnaround needs."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §13 rows 4–5"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §7.3"
  - "papers/broken-born-checkpoint-v2.md §7.4"
  - "papers/broken-born-checkpoint-v2.md refs [19], [21], [22]"
  - "CLAUDE.md 'Since the handoff'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §2"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §9"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(c) item 11"
  - "review/wiki-build-flags.md item 6"
  - "review/wiki-build-flags.md item 27"
---

*The cosmological constant Λ is a constant term in Einstein's equations of gravity that acts as an energy density of empty space: the same at every point and at every time, with a pressure equal to minus that density, so that its equation of state w, the ratio of pressure to energy density, is exactly −1. Matter and radiation thin out as the universe expands while this density does not, so a positive Λ comes to dominate, makes the expansion accelerate, and leaves an empty universe expanding exponentially forever, called [de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space); with a negative Λ, the expansion of a universe containing matter halts and reverses. Λ is the dark energy of the standard cosmological model, ΛCDM, a cosmological constant plus cold [dark matter](/wiki/dark-matter), and it is the standard expectation in two rows of the program's prediction table: a constant w = −1 in [row 4](/wiki/predictions/dark-energy-drift), and eternal expansion toward de Sitter space in [row 5](/wiki/predictions/fate-of-expansion). The program assigns the observed dark energy to a field, [τ](/wiki/cosmology/dark-energy/tau-quintessence), in its place, and data that settle on a constant w = −1 would kill that sector. The fits the program cites report evidence that dark energy is weakening, which a constant cannot do; the second data release of the Dark Energy Spectroscopic Instrument also favours an earlier phase with w below −1, which τ cannot have ([DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)). The vacuum energy of quantum fields acts exactly as a Λ does, and why it is not far larger than observed is [a separate, unsolved problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem).*

**Status:** Established — [T] — textbook general relativity and cosmology, written here from general knowledge, with the literature it names marked †; no `verify/` script checks it. The program's uses carry their own tags in [checkpoint #11](/wiki/history/documents/checkpoint): τ in Λ's place (§10, [D + T]), the duality dictionary's "Dual stiff ↦ Λ" (§10, [D — corrected en route]) and the vacuum-energy identity's zero cosmological constant (§7.3, [D][V]); the standard expectations of §13 rows 4 and 5 carry no tag.

## Λ in Einstein's equations [T]

### The constant term

[General relativity](/wiki/gravity/spin-2-fields/general-relativity) relates the curvature of spacetime to its content of energy and momentum through Einstein's field equations. The equations admit one further term, the metric itself multiplied by a constant Λ (Einstein 1917 †). In the mostly-plus sign convention:

```text
G_μν + Λ g_μν = T_μν / M_P²
```

Here g_μν is the metric, G_μν the Einstein tensor built from its curvature, T_μν the stress-energy tensor of matter and radiation, and M_P the [reduced Planck mass](/wiki/gravity/spin-2-fields/planck-units#two-conventions-for-the-planck-mass-t), M_P² = 1/(8πG) with G Newton's constant. The Einstein tensor has zero divergence identically (the contracted Bianchi identity), and so does the metric, whose covariant derivative vanishes; the added term therefore keeps the equations consistent with the conservation of T_μν. In four dimensions, combinations of these two are the only divergence-free symmetric tensors built from the metric and its first two derivatives (Lovelock 1971 †), so Λ is the one constant besides G that equations of this kind can contain. It has the dimensions of a curvature, an inverse length squared.

In the action the term is a constant energy per unit volume of spacetime:

```text
S = ∫ d⁴x √−g (M_P²/2)(R − 2Λ) + S_matter
  = S_EH − ∫ d⁴x √−g ρ_Λ  + S_matter        with  ρ_Λ = M_P² Λ
```

R is the curvature scalar, √−g the volume factor and S_EH the Einstein–Hilbert action ([the field equations](/wiki/gravity/spin-2-fields/general-relativity#the-einsteinhilbert-action-and-the-field-equations-t)). A constant term in the potential energy of any field enters the action in the same way, and so acts on gravity in the same way.

### An energy density of empty space

Moved to the right-hand side, the term reads as one more source of gravity:

```text
G_μν = (T_μν + T^Λ_μν) / M_P²        T^Λ_μν = −ρ_Λ g_μν
```

In the same convention a perfect fluid of energy density ρ, pressure p and four-velocity u has T_μν = (ρ + p)u_μu_ν + p g_μν. T^Λ_μν is therefore a fluid with energy density ρ_Λ and pressure −ρ_Λ. Because it is proportional to the metric, it has the same form in every frame: an observer moving at any velocity measures the same density and pressure, so it singles out no rest frame and no direction, as an energy of empty space must. Its equation of state is

```text
w = p_Λ / ρ_Λ = −1        exactly
```

The vacuum energy of quantum fields has the same form and adds to ρ_Λ; gravity responds only to the sum ([below](#λ-as-vacuum-energy-t)).

### It does not thin

In a homogeneous universe with scale factor a(t), the factor by which distances between distant galaxies have grown, and expansion rate H = ȧ/a, each component that exchanges no energy with the others obeys the continuity equation ([fluids and how they thin](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#fluids-and-how-they-thin-t)):

```text
ρ̇ = −3H(ρ + p)        so that  ρ ∝ a^{−3(1+w)}  for constant w
```

With w = −1 the right-hand side vanishes: ρ_Λ stays constant as space expands, while the density of matter falls as a⁻³. The energy in a volume V that grows with the expansion is then ρ_Λ V, which grows in proportion to V. The first law of thermodynamics, dE = −p dV, gives the same result: with p = −ρ_Λ, the energy rises by ρ_Λ dV when the volume grows by dV.

### The letter Λ

In the program's documents the letter also names other things: the [Lagrangian Grassmannian Λ(d)](/wiki/phase-space/modular-field/lagrangian-grassmannian), the space of ways to split phase space into position and momentum; Λ_wedge, the wedge sector's contribution to the cosmological constant ([below](#cosmological-constants-in-the-bimetric-potential)); an undefined factor in a gravitational condensation rate; a symmetry-breaking scale Λ_c; and the Coulomb logarithm ln Λ. [Notation](/wiki/notation#letters-with-several-meanings) lists them. On this page Λ is the cosmological constant only.

## Acceleration and the de Sitter future [T]

### Acceleration

For a spatially flat universe, with ρ and p now the density and pressure of matter and radiation and Λ written separately, the two Friedmann equations are

```text
H² = ρ/(3M_P²) + Λ/3
ä/a = −(ρ + 3p)/(6M_P²) + Λ/3
```

Matter and radiation, with ρ + 3p > 0, slow the expansion. A positive Λ adds a positive acceleration term, Λ/3, whatever else the universe contains. Written as a fluid, it is the case w = −1 of the condition w < −1/3 for a component that makes the expansion accelerate ([acceleration](/wiki/cosmology/dark-energy/quintessence#acceleration-t)). The acceleration of the expansion found in observations of distant supernovae (Riess et al. 1998 †; Perlmutter et al. 1999 †) is consistent with a small positive Λ [T].

### Toward de Sitter space

In an expanding flat universe with positive Λ, the matter term ρ/(3M_P²) falls at least as fast as a⁻³ while Λ/3 does not, so H² tends to Λ/3. The expansion rate becomes constant and the scale factor grows exponentially, a ∝ e^{Ht}. The limit is [de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space) (de Sitter 1917 †), the spacetime of an empty universe with a positive Λ, whose Hubble rate is set by Λ alone:

```text
H² = Λ/3
```

This is the relation Λ = 3H² that the [round-3](/wiki/method/review/round-3) audit used to turn Higuchi's bound on a massive spin-2 field in de Sitter space into m² ≥ 2H² (`review/round3/referee/audit-notes.md` Step 1; [the Higuchi bound](/wiki/gravity/spin-2-fields/bimetric-cosmology#the-higuchi-bound)). The spacetime itself, its horizon and its use as a background for spin-2 fields are on the de Sitter page.

With a positive Λ, de Sitter space is the end state of standard cosmology: expansion that never stops, toward an empty, exponentially expanding universe, in which every galaxy not gravitationally bound to ours eventually lies beyond the horizon, the distance from which light emitted now can never reach us [T]. #11 §13 row 5 names this standard expectation "Eternal de Sitter".

## A negative Λ: turnaround and collapse [T]

If Λ is negative, so is ρ_Λ. With matter present, the first Friedmann equation, H² = ρ/(3M_P²) + Λ/3, reaches zero when the matter density has fallen to −M_P²Λ, the magnitude of ρ_Λ. At that moment the expansion halts. The second equation then gives a negative ä/a, so the universe begins to contract and ends in collapse. The maximally symmetric spacetime with a negative Λ is anti-de Sitter space (the page on [de Sitter space](/wiki/cosmology/dark-energy/de-sitter-space) describes both).

A field whose potential energy falls below zero and settles at a negative value acts as a negative effective Λ, and the same sequence follows ([recollapse](/wiki/cosmology/dark-energy/quintessence#recollapse-t)); because the vacuum energy changes sign from positive to negative, this sequence is described as a transition to anti-de Sitter space followed by collapse. #11 §10 cites fits of quintessence models with such a potential: "high posterior preference for a future anti-de Sitter transition and collapse in negative-minimum quintessence fits [19S, 20S, 21S]" ([the fits](/wiki/cosmology/dark-energy/quintessence#fits-to-current-data-s)).

## ΛCDM and how surveys test it [T]

### The standard model

The standard cosmological model, ΛCDM, describes a spatially flat universe containing radiation, ordinary matter, cold dark matter and a positive cosmological constant. Its dark energy is Λ, with w = −1 at all times. The matter density, which falls as a⁻³, was larger than ρ_Λ in the past, and Λ's share of the total grows as the universe expands, so an era of decelerating expansion gives way to acceleration [T].

ΛCDM is the cosmological baseline against which the program's documents state their predictions. The [lab notebook](/wiki/history/documents/lab-notebook)'s predictions table compares each of its requirements with the expectation of standard theory, whose cosmology it names as ΛCDM (#1 §9), and its kill condition for dark energy counts a w below −1 only "as an intrinsic equation of state, not an artifact of an assumed ΛCDM background" (#1 §7 item 1, transcribed from its LaTeX).

### Testing for a departure from w = −1

A survey tests Λ by fitting a dark energy whose w may differ from −1 and asking whether the data prefer w = −1. A constant w is the simplest alternative. A changing w is usually summarized by the two-parameter Chevallier–Polarski–Linder (CPL) form w(a) = w₀ + wₐ(1 − a), with a = 1 today, in which Λ is the single point (w₀, wₐ) = (−1, 0) ([what w₀ and wₐ mean](/wiki/cosmology/dark-energy/cpl-parametrization#what-w₀-and-wₐ-mean)).

w is not observed directly. It enters distances and expansion rates through integrals over the expansion history, and it is inferred by fitting a model to them together with the model's other parameters ([from distances to w(z)](/wiki/cosmology/dark-energy/desi#from-distances-to-wz-t)). A w below −1 can therefore appear in a fit because the assumed background model is wrong rather than because the dark energy itself is phantom, with a density that grows as space expands, which is the distinction the program's kill condition draws ([intrinsic against inferred](/wiki/cosmology/dark-energy/phantom-divide#intrinsic-against-inferred)).

## Λ as vacuum energy [T]

Quantum field theory gives the vacuum an energy density: every mode of every field keeps a zero-point energy, and loops of massive particles and phase transitions in the early universe add their own contributions [T]. The vacuum looks the same to every observer, so this energy has the form −ρ_vac g_μν, exactly the form of T^Λ_μν above. Gravity responds only to the total, the constant in the action plus all vacuum contributions, and the two cannot be measured separately [T]. Estimates of the vacuum energy far exceed the value the observed acceleration indicates, and no accepted mechanism explains the gap. That mismatch is [the cosmological-constant problem](/wiki/gravity/spin-2-fields/cosmological-constant-problem), which has its own page.

The program addresses one contribution only: its [vacuum-energy identity](/wiki/gravity/palindromic-branch/vacuum-energy-identity) removes the vacuum energy of its spin-2 interaction potential at the aligned point ([below](#cosmological-constants-in-the-bimetric-potential)), and #11 §7.3 states the limit: "it does **not** by itself address matter-loop vacuum energy, the 'old' cosmological-constant problem, on which bimetric theory is otherwise no better placed than GR [22S]", GR being general relativity.

## The standard expectation in two rows

#11 §13 states each prediction against a standard expectation, and the cosmological constant supplies two of them. DESI is the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi), and DR2 and DR3 are its Data Release 2 and Data Release 3; "DR3+" means DR3 or a later release.

### Row 4: w ≡ −1

| Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- |
| Dark energy w(z) | w ≡ −1 | Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3 | DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) — DR2 already favors a crossing above z ≈ 0.4 (§10) |

"w ≡ −1" is w equal to −1 at every redshift: the cosmological constant of ΛCDM. In the w₀–wₐ plane it is the point (−1, 0), and the row's first kill condition is data that converge on that point: "DR3+ constant −1 (kills τ-sector)". The [handoff](/wiki/history/documents/handoff) states it as "robust constant w = −1 kills the τ sector" (`HANDOFF.md` §2). The second kill condition concerns the other side of −1, a "robust intrinsic w < −1 (kills outright)", the phantom regime ([the phantom divide and the null energy condition](/wiki/cosmology/dark-energy/phantom-divide)).

The standard expectation sits at the edge of the requirement. The bound w ≥ −1 admits w = −1 ([the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound)), but the requirement of a thawing drift, w₀ > −1 and wₐ < 0, excludes a w that stays at −1 ([row 4](/wiki/predictions/dark-energy-drift#what-kills-it)).

### Row 5: eternal de Sitter

| Observable | Standard expectation | Broken-Born requirement | Killed by |
| --- | --- | --- | --- |
| Fate of expansion | Eternal de Sitter | Turnaround = conjugate bounce | (Long horizon; near-term test is row 4) |

With a positive Λ the expansion approaches de Sitter space and never stops ([above](#toward-de-sitter-space)). The program's requirement replaces that future with a turnaround, which needs a negative vacuum energy ([a negative effective Λ](#a-negative-effective-λ-the-turnaround), below; [row 5](/wiki/predictions/fate-of-expansion)).

Both standard expectations are unchanged since the lab notebook's predictions table, where they are rows 5 and 6 (#1 §9), and the v1 paper's, where they are rows 4 and 5 (#9 §9) ([the history of the predictions table](/wiki/predictions/table-history)).

### What current data say

#11 §10 summarizes the fits it cites as "compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ)" [19S, 20S, 21S], weakening dark energy being dark energy whose density falls as space expands, with w above −1. It quotes the paper of DESI's second data release: in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4" [21S]. The round-3 referee, quoting the release, notes that models respecting the null energy condition "can somewhat outperform" the cosmological-constant model but are disfavoured relative to the w₀–wₐ fit (`review/round3/referee/audit-notes.md` Step 4(c) item 11).

In this wiki's reading, the favoured curve departs from the standard expectation in both of its phases: above −1 at low redshift, the phase row 4 requires, and below −1 above z ≃ 0.4, the phase row 4 excludes. The second phase stands against the program's strict w ≥ −1, and the root `CLAUDE.md` states the position: "The dark-energy sector is under real pressure ahead of DR3" ('Since the handoff'; [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing)).

## How the program uses Λ

### τ in its place

The program does not keep Λ as its dark energy. It assigns the observed dark energy to a field: "τ is hilltop quintessence on the Maslov circle, V = V₀[1 + cos(τ/f)], periodicity by topology; strictly w ≥ −1" (#11 §10, [D + T]). τ is the angle that sets how the vacuum divides phase space into position and momentum, V₀ sets the height of its potential and f its angular scale ([τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence)). The lab notebook writes its action as a geometric sector, τ's sector, ordinary matter, conjugate matter and a mixing term, with no cosmological-constant term of its own (#1 §3); dark energy is τ's potential energy.

Near the top of its potential τ is nearly still and its energy is almost all potential energy, so its w is close to −1 and it acts almost as a cosmological constant [T]. It differs from Λ by thawing: as the expansion rate H falls, the field moves away from the maximum, its kinetic energy grows and w rises above −1 ([thawing and freezing](/wiki/cosmology/dark-energy/quintessence#thawing-and-freezing-t)). Row 4 requires that drift to persist in DESI's Data Release 3, and a constant w = −1 in its place would kill the τ sector.

[Calc note #8](/wiki/history/documents/debt-1-notes) drew the consequence of the vacuum-energy identity for this arrangement: "The massive-gravity sector contributes *nothing* to the cosmological constant; dark energy is left entirely to the τ sector, which is precisely the architecture the cosmology chapter had assumed" (`notes/debt1a-iv-beta-coefficients.md` §2). #11 §10: "§7.3 guarantees the wedge sector contributes nothing that competes with τ." The vacuum energy of matter loops, which also acts as a cosmological constant, lies outside that statement (#11 §7.3, quoted above); the identity leaves it where general relativity leaves it.

### Dual kinetic energy acts as a Λ

The [duality dictionary](/wiki/cosmology/scale-factor-duality/duality-dictionary) translates energy in the conjugate, momentum-space description of the universe ([the conjugate universe](/wiki/program/conjugate-universe)) into the form in which it acts on our expansion. Its scale factor is ã, with ã = 1/a by [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint). #11 §10, tagged [D — corrected en route]: "with one shared lapse, a dual-frame fluid contributes w_eff = −w̃ [...]. Dual stiff ↦ Λ; dual Λ ↦ stiff; dual curvature ↦ negative dark radiation; dust ↦ dust". In the lab notebook's derivation (#1 §6, transcribed from its LaTeX), a dual-frame fluid with equation of state w̃ has energy E = ρ̃ã³ ∝ a^{3w̃}, "Entering our Hamiltonian constraint as ρ_eff = E/a³ ∝ a^{−3(1−w̃)}".

The first two entries involve Λ.

- **Dual stiff ↦ Λ.** A stiff fluid, w̃ = +1, is what a uniform field becomes when its energy is all kinetic [T]. Its energy grows as a³, at the same rate as our volume, so the density it contributes here is constant, as a cosmological constant's is ([it does not thin](#it-does-not-thin)). The notebook's table lists "Kinetic/stiff energy (w̃ = +1)" as appearing as a "Cosmological constant (w = −1)" (#1 §6).
- **Dual Λ ↦ stiff.** A cosmological constant on the conjugate side, w̃ = −1, has energy falling as a⁻³ and contributes a density falling as a⁻⁶: a stiff fluid on our side, which matters only at early times.

From the first entry the notebook concluded that "the natural source of a near-constant dark energy is **kinetic energy in the dual frame**" (#1 §6), and it then identified dark energy with τ's potential energy (#1 §7). No document derives the second from the first ([Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link)).

### Cosmological constants in the bimetric potential

The program's gravity sector contains a second, massive spin-2 field, the [momentum graviton X](/wiki/gravity/momentum-graviton), whose interaction with the metric is the potential of [Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric), a theory of two interacting metrics g and f. Two of the potential's five terms have the form of a cosmological constant: the β₀ term is β₀√−g, a cosmological constant for g, and the β₄ term is β₄√−f, one for f [T]. At the aligned point, where the two frames coincide, the whole potential enters the field equation of g as a term proportional to the metric, which acts as a cosmological constant, and a flat vacuum there needs that term to vanish ([the flatness condition](/wiki/gravity/palindromic-branch/vacuum-energy-identity#the-flatness-condition-v1--t)).

Reciprocity forces the coefficients into [the palindrome βₙ = β₄₋ₙ](/wiki/gravity/palindromic-branch/palindrome), and the potential's value V(1) at the aligned point is then exactly twice its tadpole T, the coefficient of its term linear in a small departure from that point. A flat aligned vacuum requires V(1) = T, so both vanish. #11 §7.3, tagged [D][V]: "*the wedge sector contributes zero cosmological constant, by symmetry.*" The wedge sector is that potential written in frame variables ([vielbein formulation and wedge potentials](/wiki/gravity/spin-2-fields/vielbein-formulation)). Flag 6 in `review/wiki-build-flags.md` records that the flatness condition V(1) = T is itself one condition on the coefficients, so "by symmetry" overstates the result. Battery test T5 checks the integer identity behind V(1) = 2T ([the verification battery](/wiki/method/verification/battery)).

The documents name the result after Λ: "V(1) = 2T ⇒ Λ_wedge = 0" (`HANDOFF.md` §3) and "the Λ = 0 property of interchange-symmetric bimetric" (`notes/debt1a-iv-beta-coefficients.md` §2). Whether that property is new is open. The [partially massless point](/wiki/gravity/spin-2-fields/partially-massless-gravity#the-partially-massless-point-of-bimetric-gravity) of bimetric gravity lies, at α = 1, on the same family of potentials but, in #11's words, "sits at Λ ≠ 0 with c undetermined; our flat-aligned-vacuum identity selects a *different* point of the same branch" (#11 §7.4). #11 defines neither letter; in the bimetric literature's usual notation α is the ratio of the two metrics' Planck masses and c the constant of proportionality between the metrics, f = c²g [T] ([Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison)).

### A negative effective Λ: the turnaround

The program's alternative to eternal de Sitter is a turnaround. In the lab notebook, once τ's potential energy is below zero, "the effective vacuum energy is negative, expansion halts, and slow contraction begins" (#1 §7 item 3): τ's potential would act as a negative effective Λ, and the universe would follow the anti-de Sitter sequence described [above](#a-negative-λ-turnaround-and-collapse-t). Through the constraint a·ã = 1 the program reads the turnaround as the conjugate universe's bounce: "The turnaround is the conjugate bounce by constraint identity" (#11 §10; [the turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce)).

The premise is in doubt. The documents write τ's potential as V₀[1 + cos(τ/f)], which is never negative when V₀ > 0, so as written it never supplies a negative effective Λ. Flag 27 in `review/wiki-build-flags.md` records the conflict: "Either the potential carries a negative offset not written down, or the turnaround needs another mechanism." It awaits Paul's ruling. Until then the turnaround, its reading as the conjugate bounce, and the turnaround time counted in [the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint) rest on an unresolved point ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign)).

## History and references [T]

Einstein added the term to his field equations to permit a static universe, and the solution with Λ and no matter bears de Sitter's name. Once the expansion of the universe was established, the term was commonly set to zero, while the vacuum energy of quantum fields came to be recognized as a contribution to it. The accelerating expansion found in observations of distant supernovae restored a positive Λ as the simplest description of dark energy, and it is the dark energy of ΛCDM. No program document cites this literature; the references below are added by the wiki from model memory (†).

- A. Einstein (1917)†: the cosmological term, added to permit a static universe.
- W. de Sitter (1917)†: the solution with a cosmological constant and no matter.
- E. Hubble (1929)†: the expansion of the universe.
- D. Lovelock (1971)†: in four dimensions, the Einstein tensor and the metric are the only divergence-free symmetric tensors built from the metric and its first two derivatives.
- S. Weinberg, "The cosmological constant problem," Rev. Mod. Phys. (1989)†: the classic review of the vacuum-energy problem.
- A. G. Riess et al. (1998)†; S. Perlmutter et al. (1999)†: the accelerating expansion, from distant supernovae.
- S. M. Carroll, "The cosmological constant," Living Rev. Relativ. (2001)†: a review.

## Used by

- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — the standard expectation w ≡ −1 and the kill condition "DR3+ constant −1".
- [Row 5: the fate of the expansion](/wiki/predictions/fate-of-expansion) — the standard expectation "Eternal de Sitter" and the negative effective Λ the turnaround needs.
- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — the observed dark energy assigned to τ in place of Λ; near its hilltop τ acts almost as a cosmological constant.
- [The no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound) — the bound's limiting value is Λ's, and its kill condition sets aside artifacts of an assumed ΛCDM background.
- [The duality dictionary w_eff = −w̃](/wiki/cosmology/scale-factor-duality/duality-dictionary) — dual stiff ↦ Λ, dual Λ ↦ stiff.
- [Open: dual kinetic energy versus τ's potential](/wiki/cosmology/scale-factor-duality/dual-kinetic-link) — conjugate kinetic energy acting as a cosmological constant.
- [The vacuum-energy identity V(1) = 2T](/wiki/gravity/palindromic-branch/vacuum-energy-identity) — the wedge sector contributes zero cosmological constant.
- [Open: the partially-massless comparison (OP2)](/wiki/gravity/palindromic-branch/pm-comparison) — the "Λ = 0" identity against the partially massless point at Λ ≠ 0.
- [The turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce) — a negative vacuum energy and the anti-de Sitter sequence.
- [Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign) — whether τ's potential can act as a negative Λ.

## Sources

- `papers/broken-born-checkpoint-v2.md` §13 rows 4–5 — the standard expectations "w ≡ −1" and "Eternal de Sitter", the requirements and the kill conditions
- `papers/broken-born-checkpoint-v2.md` §10 — τ in place of Λ, the dictionary's "Dual stiff ↦ Λ; dual Λ ↦ stiff", the fits and the anti-de Sitter transition, DR2's crossing, the turnaround as the conjugate bounce, the wedge sector competing with τ; refs [19], [21] — the fits and DESI DR2 Results II (live-searched)
- `papers/broken-born-checkpoint-v2.md` §7.3 — "the wedge sector contributes zero cosmological constant" and the identity's scope; ref [22] (live-searched); §7.4 — the partially massless point "at Λ ≠ 0"
- `CLAUDE.md` 'Since the handoff' — the dark-energy sector "under real pressure ahead of DR3"
- `HANDOFF.md` §2 — "robust constant w = −1 kills the τ sector"; §3 — "V(1) = 2T ⇒ Λ_wedge = 0"
- `notes/debt1a-iv-beta-coefficients.md` §2 — the massive-gravity sector contributes "*nothing* to the cosmological constant"; "the Λ = 0 property of interchange-symmetric bimetric"
- `notes/broken-born-theory.md` §3 — the action, with no cosmological-constant term of its own; §6 — the dictionary's derivation and table; §7 items 1 and 3 — the ΛCDM-background qualifier and the turnaround; §9 rows 5–6 — the v0.1 standard expectations
- `notes/broken-born-program-v1.md` §9 rows 4–5 — the v1 standard expectations
- `review/round3/referee/audit-notes.md` Step 1 — Λ = 3H² in the conversion of Higuchi's bound; Step 4(c) item 11 — models respecting the null energy condition against the cosmological-constant model
- `review/wiki-build-flags.md` item 6 — "by symmetry" and the flatness condition; item 27 — the potential's sign and the turnaround
