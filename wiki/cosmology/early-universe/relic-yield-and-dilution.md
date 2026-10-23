---
title: "The relic yield Y = n/s and entropy dilution"
weight: 17
status: established
description: "The number per unit entropy Y = n/s that a relic keeps while the comoving entropy is conserved; its conversion to a density today through s₀; the Kibble yield n/s = p(T_c/M_Pl)³ with p = 104.31; and entropy dilution, in which an entropy release such as the decays that end early matter domination divides every earlier yield: the route round-3 Decision 2 rejected for the retired soliton candidate."
provenance: [T]
sources:
  - "verify/soliton_obituary.py 'Anchors'"
  - "verify/soliton_obituary.py 'Kibble normalization (ruling 1)'"
  - "verify/soliton_obituary.py 'Mass and overproduction (ruling 2)'"
  - "review/round3-adjudication.md 'Verdict'"
  - "review/round3-adjudication.md 'Rulings' 1"
  - "review/round3-adjudication.md 'Rulings' 2"
  - "review/round3-adjudication.md 'Rulings' 3"
  - "review/round3-adjudication.md 'Lessons (now in CLAUDE.md)' 2"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/round3/adjudicator/round3_arb.out"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(c) item 1"
  - "review/round3/referee/step2a.py 'Kibble'"
  - "review/round3/referee/step2a.out 'Kibble'"
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "notes/knot-dark-matter-standalone.md Abstract"
  - "notes/knot-dark-matter-standalone.md §3"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/wiki-build-flags.md items 21, 34"
---

*The yield of a relic is its number of particles per unit of entropy, Y = n/s: the number density n divided by the entropy density s of the hot plasma that filled the early universe. While nothing creates or destroys the particles, both quantities fall in inverse proportion to the volume as the universe expands, so the yield stays fixed, and multiplying it by today's entropy density gives the relic's density now. Entropy dilution is the standard way a yield can still fall after it has been fixed: a large release of entropy into the plasma, such as the decay of heavy particles that dominated the universe for a time (a period called early matter domination), divides every yield fixed before the release by the factor by which the entropy grew. Both entered the [review](/wiki/method/review/round-3) that retired the program's [soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary). Its count of monopoles per unit entropy had dropped a factor of about 4.6×10³ that comes from the expansion rate ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)). Counted correctly, monopoles at the candidate's benchmark mass could make up the [dark matter](/wiki/dark-matter) only with a dilution factor of at least 10³–10⁴ left free, and the program rejected that route because a free factor removes the mass prediction.*

**Status:** Established — [T] — textbook thermal history, written here from general knowledge; references the wiki adds are from model memory (†). The program's uses carry their own tags. The Kibble normalization p = 104.31 and the overproduction at the retired benchmark are [V], gated in `verify/soliton_obituary.py`, whose anchors include the Friedmann coefficient 1.66 and the published normalization "n/s ~ 100 (T_c/M_Pl)^3" ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). No script in `verify/` checks a dilution factor: the dilution figures on this page are overproduction factors read as dilution requirements, by the withdrawn manuscript #14, the round-3 referee and the adjudication.

## Entropy in an expanding universe [T]

### The entropy density

In the [radiation era](/wiki/cosmology/early-universe/radiation-era) the plasma is close to thermal equilibrium at a temperature T, and its entropy density is

```text
s = (2π²/45) g*s T³
```

Here g\*s counts the relativistic degrees of freedom the way g\* does, each bosonic state as 1 and each fermionic state as 7/8, but weights a species at its own temperature T_i by (T_i/T)³ instead of (T_i/T)⁴ [T]. The two counts agree while every species shares one temperature. They separate once the neutrinos, which had already decoupled, end up colder than the photons after electrons and positrons annihilate [T].

### Conservation

While the plasma stays in equilibrium, the expansion is adiabatic: the entropy in a comoving volume, s a³, does not change, with a the scale factor ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)) [T]. Since s is proportional to g\*s T³, the product g\*s T³ a³ is constant, and the temperature falls as 1/a while g\*s stays fixed. When a species becomes nonrelativistic and annihilates, g\*s drops, and the entropy of the annihilating pairs passes to the particles still in equilibrium with them; the temperature then falls more slowly than 1/a for a while, and the comoving entropy is unchanged [T]. Electron–positron annihilation, which heats the photons but not the already decoupled neutrinos, is the standard example ([the definition of N_eff](/wiki/cosmology/early-universe/radiation-era#definition)). A sector that does not interact with ours conserves its own entropy separately ([a hidden sector at its own temperature](/wiki/cosmology/early-universe/hidden-sector-temperature#separate-entropy-conservation)).

The comoving entropy grows only in processes out of equilibrium: the decay of a species that has dropped out of equilibrium, the conversion of the inflaton's energy into heat at the end of inflation, and a first-order phase transition that releases latent heat after supercooling [T]. These are the subject of [entropy dilution](#entropy-dilution-t) below.

## The yield [T]

### Definition

The number density n of a relic falls as a⁻³ once nothing creates or destroys its particles, and so does s. Their ratio is the yield:

```text
Y = n/s          n ∝ a⁻³ and s ∝ a⁻³   ⇒   Y is constant
```

The entropy is the natural divisor because it is conserved through the steps that change other measures [T]. The ratio n/T³ is not constant while g\*s changes, since the temperature then does not fall exactly as 1/a; the ratio n/n_γ to the photon number density changes when annihilations add photons; the yield is unaffected by either. The ratio n_b/n_γ of baryons to photons used in [Big Bang nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis) is the same kind of quantity normalized to photons: after electron–positron annihilation the photon number density is a fixed multiple of s, so the two ratios differ by a constant factor [T].

The symbol Y for the yield is not the primordial helium mass fraction Y_p ([helium and the traces](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#helium-and-the-traces)).

### From a yield to a density today

The number density today is n₀ = Y s₀, with s₀ the entropy density today, and a relic of mass m has mass density ρ₀ = m Y s₀ [T]. The density is usually quoted as a fraction Ω of the critical density ρ_c, the density of a spatially flat universe at the present expansion rate, and through the product Ω h², which does not depend on the measured value of the Hubble constant ([what is being set](/wiki/dark-matter/candidates/relic-abundance#what-is-being-set)):

```text
ρ₀ = m · Y · s₀          Ω h² = ρ₀ / (ρ_c/h²)
```

The values in the record:

- `verify/soliton_obituary.py` codes `S0 = 2891.2` (cm⁻³) and builds the dark-matter density from Ω h² = 0.120 as `RHO_DM = 0.120*1.05371e-5` (GeV cm⁻³). Its docstring calls its constants "PDG and Planck 2018 values", PDG being the Particle Data Group; flag 34 in `review/wiki-build-flags.md` notes that they are typed into the script, not retrieved.
- The round-3 referee took "s0=2891.2/cm^3 (PDG 2024 astro)" and "Omega_c h^2 = 0.120 (Planck 2018)", and checked the withdrawn manuscript's inputs as "rho_DM = 1.264 keV/cm^3 (OK), s0 ~2.9e3 (OK)" (`review/round3/referee/audit-notes.md`, Step 2).
- #14 itself wrote "mean rho_DM = 1.26 keV/cm^3, s_0 ~ 2.9e3 /cm^3" (§3).

### What fixes a yield

A yield is set by the last process that created or destroyed the particles, and each relic-abundance mechanism is a statement of what fixes Y [T] ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)):

- in [thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out#in-terms-of-the-yield), the yield at which annihilation stops keeping pace with the expansion;
- in [freeze-in](/wiki/dark-matter/candidates/relic-abundance#freeze-in-t), the yield accumulated by slow production that never reaches equilibrium;
- for an [asymmetric relic](/wiki/dark-matter/candidates/relic-abundance#asymmetric-dark-matter-and-the-sakharov-conditions-t), such as the baryons, the excess of particles over antiparticles;
- for [topological defects](/wiki/symmetry-breaking/topological-defects), the number formed per unit entropy at a symmetry-breaking transition: [the Kibble yield](#the-kibble-yield-t).

After that, the yield changes only if particles are destroyed later, for example by monopole–antimonopole annihilation ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem#annihilation-is-not-enough-t)), or if the entropy grows.

## The Kibble yield [T]

[The Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism#the-causal-bound-t) gives at least about one defect per Hubble volume when the universe cools through a symmetry-breaking transition at the temperature T_c: n ≳ H³, where H is the Hubble rate (not the phase-space metric H of [Born geometry](/wiki/phase-space/born-geometry/born-structures)). Dividing by s turns the count into a yield. With the radiation-era expansion rate H = 1.66 √g\* T²/M_Pl ([the expansion rate](/wiki/cosmology/early-universe/radiation-era#the-expansion-rate-t)) and the entropy density above, with g\*s = g\*:

```text
n/s = p (T_c/M_Pl)³          p = (1.66 √g*)³ · 45/(2π² g*)        (one defect per H⁻³)
```

This is the form [checkpoint #11](/wiki/history/documents/checkpoint) writes in §12, "n/s = p (T_c/M_Pl)³" [T]. The yield is fixed at the transition and grows as the cube of T_c/M_Pl: a Hubble volume at a higher temperature contains less entropy, so one defect per Hubble volume is more defects per unit entropy.

The [arbitration](/wiki/method/review/round-3/arbitration) script of round 3 prints the normalization at g\* = 100 (`review/round3/adjudicator/round3_arb.out`):

```text
p, one defect per H^-3, non-reduced M_Pl: 104.31
p, one defect per H^-3, reduced M_Pl:     0.828
```

The two values describe one count in the two conventions for the Planck mass, M_Pl and the reduced M̄_Pl = M_Pl/√(8π) [T] ([two Planck masses](/wiki/cosmology/early-universe/radiation-era#two-planck-masses); [one convention per formula](/wiki/gravity/spin-2-fields/planck-units#one-convention-per-formula)). Counting one defect per sphere of radius H⁻¹, (4π/3)H⁻³, instead of per H⁻³ is an order-one ambiguity of the estimate itself; the referee's script gives "p(one per (4pi/3)H^-3) = 24.90" (`review/round3/referee/step2a.out`). The gate checks p against a published value as one of its anchors, and then checks both conventions [V] (`verify/soliton_obituary.py`):

```text
PASS  one defect per Hubble volume gives n/s ~ 100 (T_c/M_Pl)^3 (Gangui, astro-ph/0110285)  [p = 104.31]
PASS  p = 104.31 with M_Pl  [104.3106]
PASS  p = 0.828 with reduced M_Pl  [0.8279]
```

The count is a minimum. Causality limits how far the field can align, so it bounds the number of defects from below; Kibble–Zurek dynamics near a continuous transition and bubble nucleation in a first-order one both make more [T] ([a floor, not a ceiling](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism#a-floor-not-a-ceiling-t)). Round-3 ruling 3, upheld: "Kibble is a floor, not a ceiling; Kibble–Zurek or bubble counting add more".

## Entropy dilution [T]

### An entropy release divides every earlier yield

Suppose the entropy in a comoving volume grows by a factor D between two times, while the number of relic particles in that volume stays the same. Then

```text
Y_after = Y_before / D          D = (s a³)_after / (s a³)_before
```

Every yield fixed before the release is divided by the same D, and relics made after it are not affected [T]. The dilution does not distinguish between species: dark matter, topological defects and any baryon asymmetry made earlier are all thinned by the same factor.

### Early matter domination

A heavy species that has dropped out of equilibrium and lives long, or a scalar field oscillating about the minimum of its potential, behaves as matter: its energy density falls as a⁻³, while that of radiation falls as a⁻⁴ [T]. Its share of the total therefore grows in proportion to a, and if it lives long enough it dominates, so that the universe expands as in a matter-dominated era. This is early matter domination. When the species decays, its energy becomes radiation that thermalizes, and the comoving entropy grows by the factor D [T].

### How large the factor is

In the simplest case, a species that decays all at once after dominating for a while, D is roughly the ratio of two temperatures: that of the plasma when the species began to dominate, and that of the plasma its decays leave behind [T]. A longer period of domination gives a larger factor. The factor is set by the decaying species' abundance, mass and lifetime (Scherrer and Turner 1985 †); without a specified species, D is a free parameter.

### Conditions

- **Before nucleosynthesis.** The decays must be over, and the expansion back to the standard radiation-dominated form, before [nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#light-particles-decays-and-entropy-release) begins; otherwise the altered expansion rate and the decay products change the light-element abundances [T]. This sets a lower limit on the temperature the decays may leave, and so an upper limit on D for a given start of domination [T].
- **After what it dilutes.** An entropy release thins only what already exists. To dilute monopoles it must follow the transition that formed them, and the plasma it leaves must be colder than the transition temperature; otherwise the symmetry is restored and the defects form again when the plasma cools through T_c [T].
- **Side effects.** A baryon asymmetry made earlier is thinned by the same factor, so the asymmetry must be made afterwards or start larger [T]. The decaying species can itself produce relics in its decays, and their yield is set by the decays rather than diluted by them [T].

### Inflation, the extreme case

[Inflation](/wiki/cosmology/early-universe/inflation-and-dilution#how-it-dilutes-relics) thins a relic present before it by the growth of the volume, a factor e^{3N} for N e-folds of expansion, and reheating at its end creates the entropy of the hot plasma. The yield of a pre-inflationary relic falls so far that fewer than one particle remains in the observable universe [T]. In the terms of this page, reheating is an entropy release that divides the yield of everything made before it by an enormous factor. Relics made after reheating are not affected, which is why a transition that is to leave defects must lie below the reheating temperature ([ordering: which relics survive](/wiki/cosmology/early-universe/inflation-and-dilution#ordering-which-relics-survive)). #14 stated that requirement for its hidden sector: "Inflation must precede the hidden transition, and v must lie below the reheating temperature" (§3), with v the hidden symmetry-breaking scale.

## How much dilution a relic needs

### The overproduction factor

A relic made in excess needs a dilution factor equal to its overproduction factor, the ratio of the density it would have to the density observed. When the yield depends on the relic's mass, setting the density equal to the observed one selects a single mass, and the dilution a heavier relic needs grows with its mass.

For monopoles counted by the Kibble mechanism the growth is steep. #14 §3: "This is a point, not a window. Heavier monopoles are over-produced as (M/M\*)^4 and need that much entropy dilution - about 1e10 at M = 1e16 GeV. Lighter monopoles are under-produced." Here M\* is the mass at which the undiluted abundance equals the dark-matter density. The fourth power has a plain origin: in #14's model the monopole mass M is proportional to the transition temperature (M = 4πf v/g_d with T_c ~ v, #14 §3), the yield grows as T_c³, and the mass density is M times the number density ([the relation](/wiki/dark-matter/candidates/soliton-candidate/overproduction#the-relation)):

```text
ρ₀ ∝ M · (n/s) ∝ M · T_c³ ∝ M⁴          dilution needed at mass M:  D = (M/M*)⁴
```

### The figures in the record

These figures belong to the retired soliton episode, and they moved when round 3 corrected the count:

| Case | Dilution needed | Source |
|---|---|---|
| M = 10¹⁶ GeV, as #14 v3 stated it | "about 1e10" | #14 §3 |
| M = 10¹⁶ GeV against M\* = 3×10¹³ GeV, recomputed | "1.24e10" | audit notes Step 2; `step2a.out` |
| M = 10¹⁶ GeV against the corrected M\* | "2.6e13", "input M\* wrong" | audit notes Step 2 |
| v3's benchmark, 3×10¹³ GeV, at minimum production | 2.1×10³–1.2×10⁴ [V] | ruling 2; #11 §12 |

The referee's script states the corrected M\* it divides by: "with corrected M\*=4.44e+12: 2.573e+13" (`review/round3/referee/step2a.out`), the upper end of the corrected band. The last row is gated as an overproduction factor (`verify/soliton_obituary.py`, 'Mass and overproduction (ruling 2)'):

```text
PASS  M* at minimum production = 2.9-4.4e12 GeV  [2.873e+12-4.441e+12]
PASS  the two Planck conventions agree when p is normalized consistently
PASS  the 3e13 benchmark is overproduced 2.1e3-1.2e4 times  [2.08e+03-1.19e+04]
```

The adjudication reads it as a dilution requirement, "a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3)" (Decision 2). "Far more" refers to realistic production, which makes more monopoles than one per Hubble volume ([realistic production only adds](/wiki/dark-matter/candidates/soliton-candidate/overproduction#realistic-production-only-adds)).

## The literature's version

The published analysis of hidden-sector monopoles has the same structure. Liveoak, Maharana and Wells (2026) bound the symmetry-breaking scale; the round-3 referee quotes their abstract, "for symmetry-breaking scales >~ 100 PeV, the monopole abundance is unacceptably high" (`review/round3/referee/audit-notes.md`, Step 4(c) item 1), and ruling 3 reads it as "hidden monopoles overclose for breaking scales ≳ 100 PeV unless diluted, e.g. by early matter domination". #11 §12 states it as "Hidden-sector monopoles avoid overclosing the universe only for symmetry-breaking scales ≲ 100 PeV, or with a period of early matter domination [29S]", and adds: "Below that scale, annihilation in the hidden plasma sets the abundance." The abstract of Murayama and Shu [28S], as the referee quotes it, gives "dark matter of mass 1-10 PeV" ([topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).

## How the program uses it

### The Kibble normalization: dead

Version 3 of the soliton manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) wrote the Kibble yield as "n/s ~ p (v/M_Pl)^3. One monopole per horizon volume with g\* = 100 gives p ~ 0.023; we take p = 1 as the upper end" (§3). The round-3 referee found the source of the 0.023: "0.0228 = 45/(2pi^2 100) i.e. H^3 without (1.66 sqrt g\*)^3 = 4576" (Step 2), the formula above with the Friedmann prefactor set to one. Ruling 1, upheld: "My code: p = 104.31 with M_Pl, 0.828 with the reduced M_Pl. v3's 0.0228 drops (1.66√g\*)³ ≈ 4.6×10³. My error came from misremembering the formula." The gate prints the dropped factor [V]:

```text
PASS  v3's 0.0228 drops (1.66 sqrt(g*))^3 ~ 4.6e3  [4575.6]
```

The normalization was also used in the wrong direction: v3 took p = 1 as an upper end, where one defect per Hubble volume is the least causality allows (ruling 3). Round-3 lesson 2 records that "v3's Kibble anchor reproduced v2's own number and so tested nothing", and replaced it with anchors independent of the paper, "the Friedmann coefficient 1.66 and n/s ≈ 100 (T_c/M_Pl)³ for one defect per Hubble volume" ([independent anchors](/wiki/method/verification/independent-anchors)). The full record is [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization).

### The benchmark overproduced, and the dilution route rejected

Corrected, the yield fixes M\* at 2.9–4.4×10¹² GeV [V], and v3's benchmark of 3×10¹³ GeV is overproduced 2.1×10³–1.2×10⁴ times [V] ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)). #14's abstract had placed the mass "at about 1e13 to 4e13 GeV with no dilution required". The adjudication's verdict: "Correcting it leaves two routes: a superheavy monopole that needs a named dilution mechanism, or a model at v ≲ 100 PeV that already exists in the literature."

[Decision 2](/wiki/method/review/round-3/decisions#decision-2-the-soliton-candidate-retired) retired the candidate and rejected the dilution route: "Route (b) restores the mass only by adding a free dilution factor of at least 10³–10⁴ (ruling 2), probably far more (ruling 3). The mass would then no longer be a prediction". The reason follows from the scaling above. Without dilution, the requirement that the monopoles make up exactly the observed dark matter fixes one mass, M\*. With D left free, any heavier mass fits by choosing D = (M/M\*)⁴, so the abundance no longer selects a mass. #11 §12: "Superheavy masses survive only with a free dilution factor. That removes the mass prediction, which was the candidate's reason to exist." A named mechanism would tie D to the abundance, mass and lifetime of a specific decaying species [T]; #14 named none, since it claimed no dilution was required. The other route, a breaking scale v ≲ 100 PeV, "works, but it is Murayama–Shu's and Liveoak–Maharana–Wells's model", and Decision 2 noted it as prior art rather than claim it ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). The method pages record the decision as [the declined rescue](/wiki/method/lakatosian-methodology#the-declined-rescue-of-the-soliton-candidate).

### Before round 3

The v3 worklog had already found that the Kibble estimate fixes a single mass and that heavier masses need dilution, at p = 1: "Above it, the abundance scales as (M/M\*)⁴, so the observed density needs entropy dilution of 1.3×10⁶ at 10¹⁵, 1.3×10¹⁰ at the 10¹⁶ benchmark, and 1.3×10¹⁴ at 10¹⁷" (`review/v3-worklog.md`, finding F1). On 2026-10-19 Paul decided to "move the benchmark to M ≈ 3×10¹³, and keep 10¹⁶ with its ~10¹⁰ dilution as a stated alternative", and v3 kept the figure as "about 1e10 at M = 1e16 GeV" (#14 §3). The figures rest on the uncorrected normalization and are superseded ([the worklog's "point, not a window"](/wiki/dark-matter/candidates/soliton-candidate/overproduction#superseded-the-point-not-a-window-of-the-v3-worklog)); the stated alternative became route (b).

### Our own sector's monopoles

Dilution by inflation is the second of the two grounds on which #11 §11.1 killed the founding claim that conjugate-space monopoles explain the null result of monopole searches: "inflationary dilution already accounts for absence [T]" ([Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation); [inflation and our own monopoles](/wiki/cosmology/early-universe/inflation-and-dilution#inflation-and-our-own-monopoles)).

### What the record checks

- **Gated [V].** p = 104.31 and 0.828, the dropped factor, M\* and the overproduction 2.1×10³–1.2×10⁴, in `verify/soliton_obituary.py`.
- **Executed but not gated.** The dilution figures at 10¹⁶ GeV are in the referee's script output (`review/round3/referee/step2a.out`); no script in `verify/` computes a dilution factor, and no document computes one for a named mechanism.
- **Accepted, not re-run.** The "far more" of Decision 2 rests on the referee's Kibble–Zurek estimates, which the adjudicator "did not re-run" (ruling 3). Ruling 3 attributes "1e9–1e12 overproduction" to the referee's integration; flag 21 in `review/wiki-build-flags.md` records that the integration gave 1.1e12–2.2e12 and that the lower end comes from the analytic estimate of Liveoak, Maharana and Wells, 1.2e9–2.2e11. The verdict is unaffected.

## Standard references

- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17], which the round-3 audit resolved as "Front. Phys. 69 (1990), Addison-Wesley" (Step 1); a standard treatment of entropy, yields and entropy production.
- R. J. Scherrer, M. S. Turner, Phys. Rev. D 31, 681 (1985) †: entropy production by decaying particles.
- A. Gangui, astro-ph/0110285: the normalization "n_monop/s ~ 100 (T_c/m_P)^3" for "about one monopole per Hubble volume", as the referee quotes it (Step 1), used as the gate's anchor; not cited in #11.
- H. Murayama, J. Shu (2010), arXiv:0905.1720 [28S], and D. Liveoak, A. Maharana, J. D. Wells (2026), arXiv:2607.20843 [29S]: hidden-sector monopoles and the dilution they need, as #11 cites them.
- Particle Data Group, *Review of Particle Physics* (2024), astrophysical constants: the source of s₀ in the referee's script; the gate script's copy is typed in (flag 34).

The † entry is from model memory and unverified.

## Used by

- [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) — the yield n/s = p (T_c/M_Pl)³ and the dropped (1.66√g\*)³.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — the yield at minimum production and the (M/M\*)⁴ excess that sets the dilution needed.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — "no dilution required" and the free-dilution route, rejected.
- [Round-3 decisions and lessons](/wiki/method/review/round-3/decisions) — Decision 2's route (b) and lesson 2's anchors.
- [Topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art) — early matter domination as the escape above about 100 PeV.
- [Lakatos's methodology of research programmes](/wiki/method/lakatosian-methodology) — the declined rescue by a free dilution factor.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — s₀, the yield normalization and the overproduction, executed.
- [The Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) — one defect per Hubble volume converted to a yield.
- [The monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem) — dilution as the remedy, by inflation or a later entropy release.
- [Relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance) and [thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out) — the yield as what a mechanism fixes.
- [Inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution) — the yield of a pre-inflationary relic, and dilution after reheating.
- [Big Bang nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis) — an entropy release must end before it.

## Sources

- `verify/soliton_obituary.py` 'Anchors', 'Kibble normalization (ruling 1)', 'Mass and overproduction (ruling 2)' — s₀ and the dark-matter density as coded, the published normalization as anchor, p in both conventions, the dropped factor, M\* and the overproduction, executed
- `review/round3-adjudication.md` 'Verdict' — the two routes; 'Rulings' 1–3 — the dropped factor, the overproduction, the floor and the literature; 'Lessons (now in CLAUDE.md)' 2 — the independent anchors; 'Decisions' 2 — the rejected dilution route
- `review/round3/adjudicator/round3_arb.out` — p with M_Pl and with the reduced Planck mass
- `review/round3/referee/audit-notes.md` Step 1 — Kolb–Turner and Gangui; Step 2 — the constants, the source of v3's 0.0228 and the dilution at 10¹⁶ GeV; Step 4(c) item 1 — Murayama–Shu and Liveoak–Maharana–Wells
- `review/round3/referee/step2a.py` 'Kibble' and `review/round3/referee/step2a.out` 'Kibble' — p for both horizon volumes, the missing factor and the dilution figures
- `papers/broken-born-checkpoint-v2.md` §12 — n/s = p (T_c/M_Pl)³, early matter domination [29S] and the free dilution factor; §11.1 — inflationary dilution [T]
- `notes/knot-dark-matter-standalone.md` Abstract, §3 — "no dilution required"; v3's p, its inputs, the ordering requirement and the (M/M\*)⁴ dilution (withdrawn)
- `review/v3-worklog.md` 'Findings neither referee raised' (F1) — the dilution figures and the stated alternative before round 3 (superseded)
- `review/wiki-build-flags.md` item 21 — the attribution of ruling 3's Kibble–Zurek range; item 34 — the script's constants typed in
