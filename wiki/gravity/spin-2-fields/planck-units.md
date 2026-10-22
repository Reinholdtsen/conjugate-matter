---
title: "Planck units and the two Planck masses"
weight: 12
status: established
description: "The length, time, mass, energy and force built from ℏ, c and G; the Planck mass as the strength with which a spin-2 field couples to matter; its two conventions, M_Pl = G^{−1/2} and the reduced M̄_Pl = M_Pl/√(8π), and the rule that a formula keeps one of them throughout; and where the program's documents use each."
provenance: [T]
sources:
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md §4"
  - "papers/conjugate-special-relativity.md §7"
  - "verify/soliton_obituary.py constants"
  - "verify/soliton_obituary.py 'Anchors'"
  - "verify/soliton_obituary.py 'Kibble normalization (ruling 1)'"
  - "verify/soliton_obituary.py 'Mass and overproduction (ruling 2)'"
  - "review/round3-adjudication.md 'Rulings' 1, 2, 7"
  - "papers/broken-born-checkpoint-v2.md §7.5"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/step2a.out"
  - "review/round3/referee/step4d.out"
  - "review/round3/referee/step4.py"
  - "review/round3/adjudicator/round3_arb.out"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/debt1a-iv-beta-coefficients.md §3"
  - "review/v3-worklog.md 'Round-2 pending list' R7"
  - "notes/broken-born-theory.md §3"
  - "notes/broken-born-theory.md §4"
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md 'Addendum (v0.2, post Debt-3)'"
  - "notes/debt3b-wave-island.md 'What pins g? Two scenarios'"
  - "notes/debt3c-ufd-endpoint.md 'The attractive endpoint: criticality and the drain'"
  - "review/wiki-build-flags.md items 31, 34"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
---

*Planck units are the units of length, time, mass and energy built from three constants of nature: Planck's constant ℏ, the speed of light c and Newton's constant G. The Planck length √(ℏG/c³) and the Planck energy √(ℏc⁵/G) mark the scale at which the quantum behaviour of gravity is expected to matter, and their ratio, c⁴/G, is a force that contains no ℏ. The Planck mass √(ℏc/G) also measures the strength of gravity: a [spin-2 field](/wiki/gravity/spin-2-fields) such as the graviton couples to matter with a strength inversely proportional to it, so the Planck mass appears wherever the coupling of gravity or the expansion rate of the universe enters a formula. It is written in two conventions, M_Pl = G^{−1/2} in units with ℏ = c = 1 and the reduced M̄_Pl = M_Pl/√(8π), which describe the same physics provided that each formula keeps one of them throughout. The program's [conjugate special relativity](/wiki/conjugate-relativity) sets its Born length equal to the Planck length, which makes its maximum force c⁴/G. The review that retired the program's [soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) found that the candidate's reported factor of about 3 between the two conventions [came from mixing them](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization#the-reduced-planck-factor-of-3-was-an-artefact).*

**Status:** Established — [T] — textbook physics, written here from general knowledge, with the references it adds marked †. The numerical values of the two Planck masses are constants typed into `verify/soliton_obituary.py`, not retrieved (flag 34 in `review/wiki-build-flags.md`); the script's check that the two conventions give the same result once the Kibble normalization is converted consistently passes [V] ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). The program's uses carry their own tags: [#13](/wiki/conjugate-relativity)'s identification of the Born length with the Planck length is untagged and its Planck closure is [D] (#13 §1, §4). Where a document states no convention, the convention given here is the wiki's reading.

## Units from ℏ, c and G [T]

Three constants with dimensions appear in the basic laws of physics: ℏ, Planck's constant divided by 2π, which sets the scale of quantum effects and has the units of energy times time; c, the speed of light; and G, Newton's constant, the strength of gravity in Newton's law F = Gm₁m₂/r². Between them they involve the three independent dimensions of mechanics, length, mass and time, so each of those dimensions can be built from them in exactly one way, up to a pure number that dimensional analysis does not fix [T]. Planck proposed the resulting units in 1899 as units that depend on no particular body or substance (†). With every pure number set to one:

```text
l_P       = √(ℏG/c³)                          the Planck length
t_P       = l_P/c    = √(ℏG/c⁵)               the Planck time
M_Pl      = √(ℏc/G)                           the Planck mass
E_Planck  = M_Pl c²  = √(ℏc⁵/G)               the Planck energy
M_Pl c    = ℏ/l_P    = √(ℏc³/G)               the Planck momentum
```

**Natural units.** Particle physics and cosmology commonly set ℏ = c = 1 [T]. Lengths and times then become inverse energies, masses are quoted as energies, usually in GeV, and, with Boltzmann's constant also set to one, so are temperatures. Newton's constant becomes G = 1/M_Pl², so that M_Pl = G^{−1/2}, and every Planck unit reduces to the one number M_Pl: E_Planck = M_Pl and l_P = t_P = 1/M_Pl. The program's cosmology and its review records write the Planck mass in this form.

### The Planck force c⁴/G

Dividing the Planck energy by the Planck length cancels ℏ, and so does dividing the Planck momentum by the Planck time [T]:

```text
E_Planck / l_P  =  M_Pl c / t_P  =  c⁴/G
```

Up to a pure number, c⁴/G is the only force that can be built from c and G alone, and it is called the Planck force [T]. Because it contains no ℏ, a limit on force of this form is a statement about classical gravity. The maximum-force conjecture of the general-relativity literature, c⁴/4G, is a pure number times it ([maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures#why-c⁴g-is-a-force-t)).

### A length and a momentum whose product is ℏ

The Planck length and the Planck momentum multiply to ℏ: l_P · M_Pl c = ℏ [T]. A wave packet confined to a region one Planck length across has a spread in momentum of order the Planck momentum, by the same reciprocity of widths that ties the duration of a pulse to its bandwidth ([the Fourier transform](/wiki/phase-space/reciprocity/fourier-transform)). Any length λ defines a momentum ℏ/λ in this way; the Planck units are the pair that G fixes.

### The scale of quantum gravity [T]

A particle of mass m carries two lengths. Its reduced Compton wavelength ℏ/(mc) is the scale below which it cannot be localized without creating new particles; its gravitational radius Gm/c² sets, up to a factor of order one, the size of a black hole of that mass. The first shrinks and the second grows as m increases, and they are equal when m = M_Pl, where both equal l_P [T]. At that scale quantum effects and gravitational effects are of the same size, and neither quantum field theory in a fixed spacetime nor general relativity without quantum corrections can be trusted there. That is why the Planck length and the Planck energy are taken as the scale at which a quantum theory of gravity is needed [T]. Corrections from quantum gravity to the propagation of light, for example, are expected to be suppressed by an energy near the Planck energy ([Row 9: no linear photon dispersion](/wiki/predictions/photon-dispersion)).

## The Planck mass as the strength of gravity [T]

### Newton's law

Written with the Planck mass, Newton's law of gravitation reads [T]

```text
F = G m₁m₂/r²  =  (m₁/M_Pl)(m₂/M_Pl) · ℏc/r²
```

Coulomb's law for two elementary charges has the same form, F = α ℏc/r², with α the fine-structure constant. The product (m₁/M_Pl)(m₂/M_Pl) therefore plays for gravity the part that α plays for electromagnetism: a dimensionless coupling. It is tiny for any pair of elementary particles, because their masses lie far below the Planck mass, and that is why gravity is negligible between them [T].

### The coefficient of the curvature term

In [general relativity](/wiki/gravity/spin-2-fields/general-relativity) the Planck mass is the coefficient of the Einstein–Hilbert action, and it fixes how strongly a given stress-energy curves spacetime. With ℏ = c = 1 [T]:

```text
S_EH = (1/16πG) ∫ d⁴x √−g R  =  (M̄_Pl²/2) ∫ d⁴x √−g R
G_μν = 8πG T_μν  =  T_μν / M̄_Pl²
```

Here R is the curvature scalar, G_μν the Einstein tensor, T_μν the stress-energy tensor of matter, and M̄_Pl the reduced Planck mass of the next section. The [general-relativity page](/wiki/gravity/spin-2-fields/general-relativity#the-einsteinhilbert-action-and-the-field-equations-t) writes the action as S_EH ∝ M_P² ∫ d⁴x √−g R, a form that holds in either convention.

### The coupling of a spin-2 field

Close to flat spacetime the metric is the Minkowski metric η_μν plus a small symmetric tensor, the graviton field ([linearized gravity and the graviton](/wiki/gravity/spin-2-fields/general-relativity#linearized-gravity-and-the-graviton-t)). Expanding the Einstein–Hilbert action to second order in that field gives it a kinetic term proportional to M̄_Pl². Rescaling the field by one power of the Planck mass gives the kinetic term the standard normalization of a field h_μν, and the graviton then couples to matter through [T]

```text
g_μν = η_μν + κ h_μν,        κ ∝ 1/M̄_Pl
coupling to matter  ∝  κ h_μν T^μν  ∝  h_μν T^μν / M̄_Pl
```

with the constant of proportionality in κ a matter of convention. Each further power of h, in the graviton's interactions with itself, brings a further factor of κ [T]. In this sense the Planck mass is the strength with which a spin-2 field couples to matter: the larger it is, the weaker the coupling. A single massless spin-2 field coupled in this way to all stress-energy, its own included, rebuilds general relativity ([one massless graviton is general relativity](/wiki/gravity/spin-2-fields/general-relativity#one-massless-graviton-is-general-relativity-t)).

### Two metrics, two Planck masses

[Hassan–Rosen bimetric gravity](/wiki/gravity/spin-2-fields/hassan-rosen-bimetric) has two dynamical metrics, g and f, each with its own Einstein–Hilbert term and therefore its own Planck mass, M_g and M_f [T]. About backgrounds on which the two metrics are proportional, their fluctuations combine into one massless and one massive spin-2 field, and matter coupled to g feels the two in proportions set by the ratio of the two Planck masses [T]. When M_f is much smaller than M_g, the massive field couples to that matter only weakly; that is the regime in which a heavy spin-2 field has been shown to be linearly stable at late times in an expanding universe ([bimetric cosmology and its instabilities](/wiki/gravity/spin-2-fields/bimetric-cosmology)).

### An effective Planck mass

When the coefficient of the curvature term varies, the strength of gravity varies with it: an effective Planck mass M_eff gives an effective Newton's constant G_eff ∝ 1/M_eff² [T]. A different G at the time of nucleosynthesis changes the expansion rate then, and the abundances of the light elements bound it ([Big Bang nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#the-expansion-rate-radiation-and-gravity-together)).

## Two conventions for the Planck mass [T]

### Definitions and values

```text
M_Pl  = √(ℏc/G)        = G^{−1/2}        with ℏ = c = 1      the Planck mass
M̄_Pl  = M_Pl/√(8π)     = (8πG)^{−1/2}    with ℏ = c = 1      the reduced Planck mass
```

The reduced mass absorbs the 8π of Einstein's equations, so the action, the field equations and the Friedmann equation carry no 8π when they are written with it. Work on the thermal history of the early universe commonly quotes M_Pl; work that starts from an action, in inflation, quintessence or supergravity, commonly uses M̄_Pl and often calls it simply the Planck mass [T]. A formula has to be read in the convention its source states, and some sources state none.

In the record the values appear in scripts. `verify/soliton_obituary.py` takes M_Pl = 1.22089×10¹⁹ GeV and M̄_Pl = 2.43536×10¹⁸ GeV (`M_PL`, `M_PL_RED`). The round-3 referee used the same unreduced value and names its source, the Particle Data Group's 2024 astrophysical constants: "MPl=1.220890e19 (PDG 2024 astro)" (`review/round3/referee/audit-notes.md` Step 2). The referee's scripts derive the reduced mass from it, `MPl_red = MPl/sqrt(8*pi)` (`review/round3/referee/step4.py`), whereas the program's script and the adjudicator's arbitration script type both values in. Flag 34 in `review/wiki-build-flags.md` records that the program script's constants are typed in rather than retrieved, and that its docstring's "PDG and Planck 2018 values" drops the caveat of its predecessor that they came from model memory. Planck 2018 there is a data release of the Planck satellite, which mapped the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background); it is not a Planck unit. The withdrawn manuscript #14 used "M_Pl = 1.22e19 GeV" (§3), which the referee checked as "OK" (Step 2).

### The same equations in both conventions

| Quantity | With M_Pl = G^{−1/2} | With M̄_Pl = M_Pl/√(8π) |
| --- | --- | --- |
| Newton's constant | G = 1/M_Pl² | 8πG = 1/M̄_Pl² |
| Einstein–Hilbert action | (M_Pl²/16π) ∫ d⁴x √−g R | (M̄_Pl²/2) ∫ d⁴x √−g R |
| Friedmann equation, flat space | H² = 8πρ/(3M_Pl²) | 3M̄_Pl²H² = ρ |
| Radiation-era expansion rate | H = 1.66 √g\* T²/M_Pl | H = √(π²g\*/90) T²/M̄_Pl |
| Kibble yield n/s = p (T_c/M)³, one defect per Hubble volume, g\* = 100 | p = 104.31 | p = 0.828 |

Here H is the Hubble expansion rate, ρ the energy density, T the temperature, g\* the number of relativistic degrees of freedom, and M the Planck mass in the column's convention. The first three rows are textbook relations [T]. For the radiation-era rows `verify/soliton_obituary.py` codes the coefficients √(8π³g\*/90) and √(π²g\*/90) ([the expansion rate](/wiki/cosmology/early-universe/radiation-era#the-expansion-rate-t)); its first anchor checks that √(8π³/90), rounded to two decimals, is 1.66, a textbook identity independent of every program document, and the arbitration script prints "1.66 check: sqrt(8 pi^3/90) = 1.6602" (`review/round3/adjudicator/round3_arb.out`; [independent anchors](/wiki/method/verification/independent-anchors)). The last row is the script's output, `p = 104.31 with M_Pl` and `p = 0.828 with reduced M_Pl` [V].

### One convention per formula

A formula that combines the expansion rate, or any gravitational coupling, with a power of the Planck mass carries a numerical prefactor that belongs to one convention. The prefactor and the mass go together. Replacing M_Pl by M̄_Pl while keeping the prefactor multiplies the result by a power of √(8π), which changes the physics, not just its notation [T].

The minimum yield of the [Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism#the-causal-bound-t) is an example. One defect per Hubble volume means a number density n ≈ H³ at the transition temperature T_c. Dividing by the entropy density s gives n/s = p (T_c/M)³, where p carries the cube of the Friedmann prefactor of the convention in use ([the Kibble yield as a radiation-era formula](/wiki/cosmology/early-universe/radiation-era#the-kibble-yield-as-a-radiation-era-formula)). Since (T_c/M̄_Pl)³ = (8π)^{3/2} (T_c/M_Pl)³, the two values of p differ by the inverse factor, and n/s is the same number in both. The round-3 referee checked it in one line (`review/round3/referee/step4d.out`):

```text
one per Hubble volume in reduced-Planck convention: n/s = 0.828 (T/MPl_red)^3 ; check = 104.31*(MPl_red/MPl)^3 = 0.828
```

## How the program uses Planck units

### The Born length at the Planck length

#13 bounds the rate of change of momentum by c̃ = ℏc/λ², where λ is the [Born length](/wiki/conjugate-relativity/maximum-force#the-born-length) and ε = ℏ/λ its conjugate momentum scale, so that c̃ = ε/(λ/c) (§1). It fixes λ in one sentence that carries no tag: "The only length the gravitational sector supplies is the Planck length, λ² = ℏG/c³, giving" the boxed value c̃ = c⁴/G ≈ 1.2 × 10⁴⁴ N (§1; [the maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force#the-planck-identification-step-by-step)). In the units above, λ = l_P makes ε the Planck momentum and λ/c the Planck time, so c̃ is the Planck force (the wiki's reading). The conjecture's c⁴/4G is smaller by the factor of 4 that #13 leaves open [O] ([Open: the factor of 4](/wiki/conjugate-relativity/maximum-force#open-the-factor-of-4)). No `verify/` script computes the value 1.2 × 10⁴⁴ N.

### Planck closure

#13 §4 multiplies the maximum force by a length: "The dual rest-energy relation is E = λ c̃ (length × maximum force). At λ = l_P: E = l_P · c⁴/G = √(ℏc⁵/G) — the Planck energy, exactly [D]." In the units above it is the Planck length times the Planck force. #13 §7 lists "E(l_P) = E_Planck" among its numerical anchors, and no `verify/` script checks it ([the invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell#at-the-planck-length)). `HANDOFF.md` §2 lists the maximum force and the Planck closure among its alive results, without the ✓ it uses for machine-verified items, and no [blind review](/wiki/method/review) round has covered #13.

### Equal Planck masses in the bimetric sector

[Calc note #8](/wiki/history/documents/debt-1-notes) §3 [D + T] finds that [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), acting as the exchange of the program's two spin-2 frames, gives the two metrics "equal effective Planck masses (forced by the same symmetry)", M_f = M_g in the notation of the v3 worklog (`review/v3-worklog.md` item R7; [equal Planck masses](/wiki/gravity/momentum-graviton/spectrum-and-parity#equal-planck-masses)). Two consequences follow, each on its own page:

- Ordinary matter, coupled to g, feels the massive field, the [momentum graviton X](/wiki/gravity/momentum-graviton), at gravitational strength. [Checkpoint #11](/wiki/history/documents/checkpoint) §7.5 gives X's couplings to it as "gravitational-strength and Yukawa-cut at 1/M_X" [D] ([Yukawa forces](/wiki/gravity/spin-2-fields/yukawa-forces#the-momentum-graviton-x)), and #8 §3 places their safety in X's short range: "safety is by **range**, not decoupling" ([safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety)).
- The regime in which a heavy spin-2 field has been shown to be linearly stable at late times, M_f ≪ M_g, is excluded, and X's stability in an expanding universe is open ([Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability)).

### The retired soliton candidate

The soliton manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate), withdrawn after [review round 3](/wiki/method/review/round-3), used the Planck mass in two ways, and the review treated them differently. The candidate is dead, and both uses are kept as its record.

**A convention mixed.** Version 3 reported a spread in its monopole mass from the choice of convention: "M\* ~ (0.9-3.7)e13 GeV; the reduced-Planck convention lowers it by a factor of about 3" (#14 §3). It had replaced M_Pl by M̄_Pl in n/s = p (v/M_Pl)³ while keeping p, with v the hidden symmetry-breaking scale. That raises the yield by (8π)^{3/2}. The mass at which the monopoles would make up all the dark matter scales as (M_Pl³/p)^{1/4} ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)), so it falls by (M_Pl/M̄_Pl)^{3/4}. The referee printed that factor, `reduced-Planck 'convention' factor (MPl/MPl_red)^(3/4) = 3.350` (`review/round3/referee/step2a.out`), and judged it "arithmetic OK, but it is a convention artefact, not a physical spread (p must be recomputed consistently)" (audit notes Step 2). [Ruling 2](/wiki/method/review/round-3/rulings#rulings-1-to-3-how-many-monopoles-form), upheld: "The "reduced-Planck factor of 3" was not a convention spread: consistently normalized, the two conventions agree." `verify/soliton_obituary.py` computes the closing mass in both conventions and requires agreement to 1% [V]:

```text
PASS  the two Planck conventions agree when p is normalized consistently
```

The candidate was retired for a separate error in the same formula: v3's p ≈ 0.023 had dropped the Friedmann prefactor (1.66√g\*)³ ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization); [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

**An order of magnitude bracketed.** Where a formula is an estimate with an unknown coefficient of order one, the two masses bracket that coefficient rather than express one quantity two ways (the wiki's reading). v3 estimated the kinetic mixing ε of its hidden photon with ours as ε ~ v/M_\*, from a dimension-five operator suppressed by a heavy scale M_\*: "For an O(1) coefficient at the Planck or reduced Planck scale, epsilon ~ 1e-7 to 1e-6" (#14 §2(b)). The referee reproduced the range with M_\* set to each mass in turn (`review/round3/referee/step2a.out`). The estimate is dead on other grounds. [Ruling 7](/wiki/method/review/round-3/rulings#rulings-7-and-8-the-mixing-operator) found the "O(1) coefficient at the Planck scale" unsupported, since "the literature generates it at one loop from bi-charged states, which sector separation forbids" ([Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator)).

### Where a document states no convention

- **#1 §6 and the dual Planck mass.** The [lab notebook](/wiki/history/documents/lab-notebook) writes 3H²(M_P² + M̃²a⁻⁶) = ρ for its two-scale-factor cosmology, with M̃ the "dual Planck mass", and does not state its convention. Without the dual term, 3H²M_P² = ρ is the ordinary Friedmann equation only when M_P is the reduced mass, which is how the wiki reads it ([the program's extension: a second scale factor](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#the-programs-extension-a-second-scale-factor)). The bracket acts as an effective Planck mass squared, "a stiff-like (a⁻⁶) modification of the effective Planck mass, relevant only at early times" (#1 §6, transcribed from its LaTeX), and its test is the optional step in G_eff of [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step). The page on [quintessence](/wiki/cosmology/dark-energy/quintessence#expansion-and-the-friedmann-equation-t) writes H² = ρ/(3M_P²) with the reduced mass as well.
- **The Debt-3 critical mass.** The [Debt-3 notes](/wiki/history/documents/debt-3-notes) give the mass above which an attractive condensate collapses as M_crit ≈ 3.6 M_P/(m√g) "[T: dilute-boson-star bound, Chavanis-type]" (Debt 3b), with m the particle mass and g its contact coupling, and do not define M_P. The wiki writes M_P = G^{−1/2} there. The coefficient and the conventions for g and M_P have not been checked against the cited paper ([what is unchecked](/wiki/dark-matter/wave-dark-matter/attractive-condensates#what-is-unchecked)), and Debt 3c's numerical form, M_crit ≈ 2.9×10⁻³⁰ (m/eV)^(−7/4) M_⊙ with M_⊙ the mass of the Sun, was evaluated with a Planck mass the notes do not define. The critical mass is part of the record of a dead claim ([Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a)).
- **#1 §4 and photon dispersion.** The notebook's consistency section says that "quadratic effects at M_B ~ M_P sit ~10 orders below current sensitivity" (#1 §4), again without a convention; M_B is the notebook's Born mass scale. The audit of flag 31 counted the gap in both: "8.0–8.6, or 7.3–7.9 with #1's reduced M_P" (`review/wiki-build-flags.md`; [the data situation](/wiki/predictions/photon-dispersion#the-data-situation)).
- **#1 §3 and the Born mass.** In the notebook's v0.1 action the metric block "reproduces the Einstein–Hilbert action with M_P fixed by M_B and the section volume" [D, schematic] (#1 §3). That action is superseded as a reference ([the geometric action S_H and the v0.1 action](/wiki/gravity/tuning-test/geometric-action)).

### Planck units in a chat-only conjecture

The phase-space diameter relation, a result that exists only in the original chat, places the "rectangle square (D_x = D_p in Planck units) exactly at the bounce" (`HANDOFF.md` §4). A length D_x and a momentum D_p can be equal only once each is expressed in a unit of its own kind; in the wiki's reading those units are the Planck length and the Planck momentum, whose product is ℏ. The relation is a conjecture ([the phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter)).

## Symbols in the documents

- **M_Pl** — #11 §12, #14 and the round-3 record, for the unreduced mass; in the scripts `M_PL` and `M_PL_RED`, in the referee's output `MPl` and `MPl_red`. **M̄_Pl** is this wiki's symbol for the reduced mass.
- **M_P** — #1 and the Debt-3 notes, which leave the convention unstated; the wiki's [general-relativity page](/wiki/gravity/spin-2-fields/general-relativity), which writes the action with ∝; and the wiki's minisuperspace and quintessence formulas, where it is the reduced mass. **m_P** is Gangui's symbol, in "n_monop/s ~ 100 (T_c/m_P)^3" as the referee quotes it (`review/round3/referee/audit-notes.md` Step 1).
- **l_P; E_Planck** — #13 §4; #13 §1 writes the Planck length through λ² = ℏG/c³.
- **M_g, M_f; M̃; M_B** — the Planck masses of the two bimetric metrics; #1 §6's dual Planck mass; #1 §3's Born mass scale.

The collision entry is under [one quantity, two conventions](/wiki/notation#one-quantity-two-conventions) on the notation page.

## References

- M. Planck, "Über irreversible Strahlungsvorgänge," Sitzungsberichte der Preußischen Akademie der Wissenschaften (1899) †: the units.
- Particle Data Group, *Review of Particle Physics* (2024), astrophysical constants: the source the round-3 referee names for M_Pl (audit notes Step 2). `verify/soliton_obituary.py` types the same value in.
- K. Hinterbichler, "Theoretical aspects of massive gravity," Rev. Mod. Phys. (2012) †: the normalization of a spin-2 field and its coupling to matter, with the bimetric theories.
- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17]; `verify/soliton_obituary.py` takes from "Kolb & Turner eqs. 5.43-5.45" the [freeze-out formulas](/wiki/dark-matter/candidates/thermal-freeze-out#the-s-wave-formula-as-the-program-codes-it), which it codes with M_Pl ([the radiation era](/wiki/cosmology/early-universe/radiation-era#standard-references)).

## Used by

- [The maximum force c̃ = c⁴/G](/wiki/conjugate-relativity/maximum-force) — the Born length set equal to the Planck length.
- [The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell) — E = l_P · c⁴/G, the Planck energy.
- [Spectrum, parameters and reciprocity parity](/wiki/gravity/momentum-graviton/spectrum-and-parity) — equal Planck masses forced by reciprocity.
- [Safety by range](/wiki/gravity/momentum-graviton/fifth-force-safety) — X couples to ordinary matter at gravitational strength.
- [Open: stability at equal Planck masses](/wiki/gravity/momentum-graviton/equal-planck-mass-stability) — M_f = M_g excludes the known stable regime.
- [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step) — #1 §6's effective Planck mass with the dual term M̃²a⁻⁶.
- [Row 9: no linear photon dispersion](/wiki/predictions/photon-dispersion) — corrections suppressed near the Planck scale, M_B ~ M_P.
- [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) — p in both conventions and the "factor of 3".
- [Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator) — an operator "at the Planck or reduced Planck scale".
- [Obituary: Scenario A and the ultra-faint-dwarf endpoint](/wiki/dark-matter/momentum-clumping/wave-island/scenario-a) — the critical mass 3.6 M_P/(m√g).
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — the two typed-in values and the convention check.

## Sources

- `papers/conjugate-special-relativity.md` §1 — c̃ = ℏc/λ², ε = ℏ/λ, the Planck length λ² = ℏG/c³ and c̃ = c⁴/G ≈ 1.2 × 10⁴⁴ N; §4 — Planck closure [D]; §7 — the numerical anchors and the open factor 4
- `verify/soliton_obituary.py` constants, 'Anchors', 'Kibble normalization (ruling 1)', 'Mass and overproduction (ruling 2)' — the two typed-in values, the coefficient 1.66, p in both conventions and the convention check [V]
- `review/round3-adjudication.md` 'Rulings' 1, 2, 7 — p = 104.31 and 0.828; the "reduced-Planck factor of 3"; the unsupported Planck-scale coefficient
- `papers/broken-born-checkpoint-v2.md` §7.5 — X's gravitational-strength couplings; §12 — the Kibble yield n/s = p (T_c/M_Pl)³ in the soliton obituary
- `review/round3/referee/audit-notes.md` Step 2 — the referee's M_Pl and its source, #14's value checked, the convention artefact; Step 1 — Gangui's m_P
- `review/round3/referee/step2a.out`, `review/round3/referee/step4d.out`, `review/round3/referee/step4.py` — the factor 3.350 and the mixing range; the conversion of p; the reduced mass derived from M_Pl
- `review/round3/adjudicator/round3_arb.out` — "sqrt(8 pi^3/90) = 1.6602" and p in both conventions
- `notes/knot-dark-matter-standalone.md` §2(b), §3 — the estimate "at the Planck or reduced Planck scale"; v3's M_Pl and its "factor of about 3" (withdrawn)
- `notes/debt1a-iv-beta-coefficients.md` §3 — equal effective Planck masses [D + T]
- `review/v3-worklog.md` 'Round-2 pending list' item R7 — M_f = M_g and the excluded M_f ≪ M_g regime
- `notes/broken-born-theory.md` §3, §4, §6, 'Addendum (v0.2, post Debt-3)' — M_P fixed by M_B; M_B ~ M_P in photon dispersion; 3H²(M_P² + M̃²a⁻⁶) = ρ; the critical mass (superseded as a reference; quotations transcribed from its LaTeX)
- `notes/debt3b-wave-island.md` 'What pins g? Two scenarios' and `notes/debt3c-ufd-endpoint.md` 'The attractive endpoint: criticality and the drain' — M_crit ≈ 3.6 M_P/(m√g), M_P undefined
- `review/wiki-build-flags.md` items 31, 34 — the photon-dispersion gap counted in both conventions; the typed-in constants
- `HANDOFF.md` §2 — the maximum force and Planck closure listed alive without a machine-check mark; §4 — "D_x = D_p in Planck units" (chat-only)
