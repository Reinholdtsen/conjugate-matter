---
title: "A hidden sector at its own temperature"
weight: 12
status: established
description: "A sector that exchanges no energy with ours keeps its own temperature: the ratio ξ set at reheating, separate entropy conservation and the late ratio T_h/T_ν, dark radiation growing as ξ⁴, freeze-out on the hidden clock, the reheating a colder sector needs and the portals that erase the difference; in the record, the retired soliton candidate's ξ < 0.77, corrected to ξ < 0.760 [V]."
provenance: [T]
sources:
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §6"
  - "notes/knot-dark-matter-standalone.md 'References'"
  - "review/v3-worklog.md 'New open items'"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/round3-adjudication.md 'Rulings' 5"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "review/round3-adjudication.md 'Rulings' (omitted constraints)"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "verify/soliton_obituary.py 'Dark radiation (ruling 5)'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/step2a.py 'Delta N_eff'"
  - "review/round3/referee/step2a.out 'dark radiation'"
  - "review/round3/referee/step2c_psi.py"
  - "review/round3/referee/step4.out item 7"
  - "review/round3/referee/step4c.out"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §8"
  - "review/wiki-build-flags.md items 22, 33"
---

*A hidden sector at its own temperature is a collection of particles and forces that takes no part in the strong, weak or electromagnetic interactions of ordinary matter and, because nothing lets it exchange energy with our plasma, keeps a temperature T_h of its own, which can differ from ours. The ratio of the two temperatures, written ξ, is set when the universe is reheated after [inflation](/wiki/cosmology/early-universe/inflation-and-dilution), or when the two sectors last exchanged energy; afterwards it changes only when the heavy particles of one sector annihilate and their entropy heats the light particles of that sector alone. The ratio fixes how much extra radiation the hidden sector adds in the [radiation era](/wiki/cosmology/early-universe/radiation-era), an excess that grows as ξ⁴ and that [nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis) and [the cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background) measure. It also fixes when, by our clock, the hidden particles freeze out, and it lasts only while no coupling between the sectors, such as a Higgs portal or kinetic mixing, brings the two plasmas into contact. The program met this physics in the review of its [soliton dark-matter candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary), whose [hidden sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) contained a massless hidden photon: the withdrawn manuscript #14 required ξ < 0.77, and [round 3](/wiki/method/review/round-3) corrected the bound to ξ < 0.760. The candidate is dead, and these numbers are kept as its record.*

**Status:** Established — [T] — standard early-universe physics, written here from general knowledge; references the wiki adds are from model memory (†). The program used it only in the record of the retired soliton candidate. There the dark-radiation bound ΔN_eff < 0.286 and the temperature-ratio bound ξ < 0.760 are [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). The round-3 referee's other figures on this page come from executed code in `review/round3/referee/` and are not gated, and the adjudication accepted ruling 6's lower bound on a hidden fermion's mass without re-checking it.

## What a hidden sector is [T]

A hidden sector is a set of particles and forces that carries none of the charges of the Standard Model (SM): its particles neither feel nor exert the strong, weak and electromagnetic forces of ordinary matter. It can have forces of its own, such as a hidden copy of electromagnetism with its own massless photon. Gravity acts on every particle and so always connects the two sectors; any other connection is an added coupling, conventionally called a portal [T]. Two portals appear in the program's record.

- **The Higgs portal** couples a hidden scalar field to the squared magnitude of our Higgs field, a combination that carries no SM charge and so can couple to a hidden scalar at renormalizable order ([the Higgs portal](/wiki/method/review/round-3/rulings#the-higgs-portal)) [T].
- **Kinetic mixing** multiplies the field strength of a hidden U(1) gauge field by that of our hypercharge field, and gives hidden charged particles a small electric charge ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#the-term-t)) [T].

A hidden sector has a temperature of its own when its internal interactions are fast enough to hold it in thermal equilibrium, which the rest of this page assumes [T]. Particles that were produced and never scattered afterwards would keep whatever momentum distribution their production gave them, and no single temperature would describe them.

The wiki meets two hidden sectors. The program's own is its [conjugate matter](/wiki/dark-matter/conjugate-matter): postulate [P4](/wiki/program/postulates/p4-polarized-matter) places it in the momentum polarization and states that "gauge forces do not cross polarizations" (#11 §4), and the [lab notebook](/wiki/history/documents/lab-notebook) calls it a "gravitationally-only-connected sector" (#1 §5.3). The other is the particle content that the withdrawn soliton manuscript #14 assumed: a hidden SU(2)_d gauge force broken to U(1)_d, with a massless hidden photon, which #14 identified with the momentum-polarized half of the program's matter and which died as a program proposal with that candidate ([Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). Every use of a hidden temperature in the program's record concerns the second.

## How the two temperatures evolve [T]

### The ratio ξ

In the radiation era the relativistic particles of each sector form a gas whose energy density is ρ = (π²/30) g T⁴, with g the sector's own count of relativistic degrees of freedom and T its own temperature ([what the radiation era is](/wiki/cosmology/early-universe/radiation-era#what-the-radiation-era-is-t)) [T]. Two sectors that were once in contact share a temperature until the processes connecting them become slower than the expansion, and from then on each evolves separately. Two sectors that were never in contact, for example because each was filled separately at reheating, never shared one [T]. Either way, the ratio of hidden to visible temperature at an early reference time is written

```text
ξ = T_h / T
```

The program's documents place the reference time after reheating, at a temperature high enough that every species of both sectors is relativistic, the "high" of the formula below: "the two sectors at temperature ratio ξ at high T" (`review/v3-worklog.md`, 'New open items', O2), "a hidden-to-visible temperature ratio xi < 0.77 after reheating" (#14 §6). The round-3 referee writes the starting value of its integrations as ξ₀ (`review/round3/referee/audit-notes.md`, Step 2).

### Separate entropy conservation

While a sector stays close to equilibrium and exchanges no energy with the other, its entropy in a comoving volume is conserved [T]. Each sector's entropy density has the standard form, with that sector's own count and temperature:

```text
s = (2π²/45) g*s T³

s_vis · a³ = constant        s_h · a³ = constant
```

Here a is the scale factor and g\*s is the count of relativistic degrees of freedom weighted for entropy ([the entropy density](/wiki/cosmology/early-universe/relic-yield-and-dilution#the-entropy-density)). The two entropy densities therefore keep a fixed ratio:

```text
s_h / s_vis = (g_h / g_vis) · (T_h / T)³ = constant
```

with g_h and g_vis the entropy counts of the hidden and visible sectors at the moment considered. Each temperature falls as 1/a while its own sector's count stays the same. When a species becomes nonrelativistic and annihilates, its sector's count falls, and its entropy passes to the light species of the same sector, whose temperature then falls more slowly for a while. T_h/T changes only through such steps: a step in the hidden sector raises it, and a step in ours lowers it [T].

The referee's relic code for #14's hidden fermion ψ uses this relation directly. It fixes the entropy ratio at the start as `R = 16*xi0**3/106.75`, with the hidden count 16 of #14's sector, the visible count 106.75 and the starting ratio ξ₀, and recovers T_h from it at each visible temperature (`review/round3/referee/step2c_psi.py`; the wiki's reading of the code).

### The ratio at late times

N_eff, the measure of extra radiation, is defined relative to the neutrinos ([N_eff: counting light species](/wiki/cosmology/early-universe/radiation-era#n_eff-counting-light-species-t)), so the visible end point of the calculation is the neutrino temperature T_ν. The neutrinos decouple while the visible plasma still holds photons, electrons and positrons; after that their temperature falls as 1/a, and the later annihilation of electrons and positrons heats only the photons [T]. Following each sector at constant entropy from the reference time until the hidden sector holds only its light species gives [T]

```text
T_h/T_ν = ξ · [ (g_h(high)/g_h(late)) / (g_vis(high)/g_ν,dec) ]^{1/3}
```

with g_vis(high) = 106.75, the count with every SM particle relativistic, and g_ν,dec = 10.75 at neutrino decoupling, the values `verify/soliton_obituary.py` uses. The factors read in order:

- **ξ**, the starting ratio;
- **(g_h(high)/g_h(late))^{1/3}**, the heating of the hidden sector's light species by the annihilations in that sector;
- **(g_vis(high)/g_ν,dec)^{1/3}**, in the denominator, the heating of our plasma, neutrinos included, by the annihilations in ours before the neutrinos decouple.

Once both the hidden light species and the neutrinos are free and relativistic, both temperatures fall as 1/a, and the ratio stays fixed from then on [T].

The round-3 referee's script evaluates the formula for #14's hidden sector at ξ = 1 and prints "g_h(high)=16.0, g_h(late)=2.0, g_vis(high)=106.75: T_h/T_nu = 0.9305" (`review/round3/referee/step2a.out`). The hidden count of 16 is "SU(2) gauge (3x2) + real adjoint (3) + Dirac doublet (2x4 x 7/8)" (`review/round3/referee/step2a.py`), and the late count of 2 is the two polarizations of the hidden photon.

### The expansion rate

The expansion rate depends on the energy density of both sectors together. In the count g\* that sets the radiation-era expansion rate, H ∝ √g\* T² with H the Hubble rate, a species at its own temperature is weighted by the fourth power of its temperature relative to T ([what the radiation era is](/wiki/cosmology/early-universe/radiation-era#what-the-radiation-era-is-t)), so the hidden sector contributes g_h·(T_h/T)⁴ [T]. At ξ = 1 a hidden sector adds its full count: in the gravitational-wave estimate for #14's hidden transition, the referee evaluated the frequency at g\* = 106.75 and at 122.75 (`review/round3/referee/step2a.out`), the second being, in the wiki's reading, the visible count plus the hidden sector's 16. A colder hidden sector adds less, by the fourth power of the ratio, and when ξ is well below 1 our plasma sets the expansion almost alone [T].

## Dark radiation [T]

### The excess in N_eff

A hidden species that stays relativistic, such as a massless hidden photon, remains radiation for the rest of cosmic history. Its energy density adds to the expansion rate as extra neutrinos would, and it is counted as ΔN_eff, in units of one neutrino species at T_ν [T]. `verify/soliton_obituary.py` codes the count as

```text
ΔN_eff = (4/7) · g · (T_h/T_ν)⁴
```

for g bosonic degrees of freedom, fermionic ones weighted by 7/8 [T] ([extra species: ΔN_eff](/wiki/cosmology/early-universe/radiation-era#extra-species-δn_eff)), and it anchors the function on the defining case before using it: "Delta N_eff: one extra neutrino species at T_nu gives 1" ([independent anchors](/wiki/method/verification/independent-anchors)). For #14's hidden photon at ξ = 1 the referee's script prints "DeltaN_eff = 0.8567" (`review/round3/referee/step2a.out`).

With the same light remnant, a hidden sector that starts with more degrees of freedom heats that remnant more and adds more radiation [T]. The v3 worklog tabulated this for three versions of #14's hidden content, "Minimal", "One light doublet" and "Two light doublets", with ΔN_eff at ξ = 1 of 0.40, 0.86 and 1.39 (`review/v3-worklog.md`, O2, tagged `[NOTE-tier]`; [the worklog's table](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#the-worklogs-table-and-the-corrected-bound)).

### The bound on ξ

Since T_h/T_ν is proportional to ξ, ΔN_eff is proportional to ξ⁴, and an upper bound on extra radiation is an upper bound on the starting ratio [T]:

```text
ξ_max = ( ΔN_eff,max / ΔN_eff(ξ = 1) )^{1/4}
```

This is the form the referee's script codes, `xi_max = (dNmax/dN)**0.25` (`review/round3/referee/step2a.py`). The fourth root damps the effect of the radiation bound on ξ: a change in ΔN_eff,max by some factor moves ξ_max by only the fourth root of that factor [T]. Replacing a remembered bound with the measured one therefore moved #14's requirement only in its second decimal place (below).

N_eff is measured at two epochs ([how N_eff is measured](/wiki/cosmology/early-universe/radiation-era#how-n_eff-is-measured-t)): by Big Bang nucleosynthesis (BBN), through the expansion rate in the first minutes, and by the cosmic microwave background (CMB), through the damping of its small-scale anisotropies and the phase of its acoustic peaks ([N_eff in the microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#n_eff)) [T]. The bound in the program's record is Planck 2018's 95% interval, which #14 §4 writes as "N_eff = 2.99 +- 0.34 at 95%". The referee recorded the source's interval as asymmetric; the difference is flag 22 in `review/wiki-build-flags.md`, and it changes nothing, because only the upper side enters. `verify/soliton_obituary.py` subtracts the SM value from the upper end, `bound = 2.99 + 0.34 - 3.044`, and gates the result [V] ([Planck 2018 and the dark-radiation bound](/wiki/cosmology/early-universe/cosmic-microwave-background#planck-2018-and-the-dark-radiation-bound)):

```text
== Dark radiation (ruling 5)
PASS  95% bound Delta N_eff < 0.286  [0.286]
PASS  xi < 0.760  [0.7601]
```

## Freeze-out on the hidden clock [T]

A species of the hidden sector that its own plasma holds in equilibrium freezes out when the hidden temperature falls to a fraction of its mass: T_h ~ m/20 in the rule of thumb that ruling 6 uses ([why freeze-out happens near T ~ m/20](/wiki/dark-matter/candidates/thermal-freeze-out#why-freeze-out-happens-near-t--m20-t)) [T]. On our clock, that moment comes when the visible temperature is T_h divided by the temperature ratio at that moment. If the hidden sector is then colder than ours, the visible plasma is hotter than T_h, and the freeze-out comes earlier in cosmic time than the freeze-out of the same mass in our plasma [T]. The expansion rate at that moment is set by both sectors together, mostly by ours when the hidden sector is colder, which shifts the freeze-out point and the final [yield](/wiki/cosmology/early-universe/relic-yield-and-dilution#the-yield-t) as well; [thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out#freeze-out-in-a-sector-at-its-own-temperature-t) sets out the three differences from freeze-out in one plasma.

The timing matters when something in the visible plasma is under way at that moment. #14 took its hidden fermion ψ "above the MeV scale, so that psi has annihilated before nucleosynthesis" (#14 §3). The round-3 referee converted ψ's hidden freeze-out to visible temperatures at ξ₀ = 0.76 (`review/round3/referee/step4.out`, item 7) and found (`review/round3/referee/audit-notes.md`, Step 4(a) item 8): "hidden freeze-out T_h ~ m/20 occurs at T_vis ~ 0.08 MeV for m_psi = 1 MeV, 0.24 MeV for 3 MeV, 0.71 MeV for 10 MeV (step4.out) - i.e. during BBN. Needs m_psi >~ 20-30 MeV." [Ruling 6](/wiki/method/review/round-3/rulings#rulings-5-and-6-the-colder-hidden-sector-and-nucleosynthesis), "Accepted, not re-checked", states the consequence: "T_f ~ m/20, so the lower mass bound should be ≳ 20–30 MeV." That figure is not among the checks of `verify/soliton_obituary.py` (flag 33 in `review/wiki-build-flags.md`). The full record is on [the ψ relic window's lower edge](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#the-ψ-relic-windows-lower-edge) and [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window#the-lower-edge-freeze-out-during-nucleosynthesis).

## How the ratio is set: reheating [T]

At the end of inflation the energy that drove it turns into hot particles, which start the radiation era ([reheating](/wiki/cosmology/early-universe/inflation-and-dilution#reheating-t)). If the field that reheats the universe decays into both sectors, and each sector then thermalizes on its own, each sector's temperature follows from the energy it received through ρ = (π²/30) g T⁴ [T]. ξ is therefore set by how the decay divides its energy. A decay that gave each sector energy in proportion to its number of degrees of freedom would give the two sectors equal temperatures; a colder hidden sector needs a decay that sends it a smaller share, or a separate field that reheats it on its own [T]. #14 called its requirement "an assumption about reheating that the framework does not fix" (§4), and the referee wrote that it requires "a two-field (or asymmetric) reheating mechanism for xi" (Step 4(c) item 9).

A colder start also puts a condition on the reheating temperature. A process in the hidden sector that has to happen after inflation needs the hidden plasma to reach the corresponding temperature. For #14 that was the hidden symmetry breaking at the scale v, since its monopoles had to form after inflation: "Inflation must precede the hidden transition, and v must lie below the reheating temperature" (#14 §3). A hidden plasma colder by the factor ξ reaches v only when the visible plasma is at v/ξ, so the visible plasma must be reheated to at least that temperature [T]. The referee (`review/round3/referee/audit-notes.md`, Step 4(c) item 9):

> Reheating: requires visible T_RH >~ v/xi = 1.06e12 - 1.90e12 GeV (step4c.out) and a two-field (or asymmetric) reheating mechanism for xi; a separately reheated hidden sector can carry dark-radiation isocurvature (conditional; not computed).

T_RH is the reheating temperature, and the two values are those `review/round3/referee/step4c.out` prints for the two ends of v3's range of v at ξ = 0.76. Isocurvature here means, in the wiki's reading, a ratio of hidden to visible radiation that varies from place to place, as a separate reheating field that fluctuated during inflation would leave it ([isocurvature](/wiki/cosmology/early-universe/inflation-and-dilution#isocurvature)); the referee did not compute it.

The same conversion sets the [redshift](/wiki/cosmology/scale-factor-duality/redshift#temperatures-and-frequencies-in-the-early-universe) of gravitational waves from a hidden transition. Their frequency today grows in proportion to the visible temperature at the transition, and a hidden transition at v happens when the visible plasma is at v/ξ. Ruling 5 carried the corrected ξ into #14's gravitational-wave band, and the gate checks the new upper end at the withdrawn benchmark; the script's label abbreviates gravitational waves ([the retired candidate's hidden transition](/wiki/cosmology/early-universe/phase-transition-gravitational-waves#the-retired-candidates-hidden-transition)):

```text
PASS  knock-on: GW upper end 3.2e7 Hz at the withdrawn benchmark  [3.17e+07]
```

## How the ratio is lost: portals [T]

A temperature difference between two sectors lasts only while the processes that move energy between them are slower than the expansion. A portal that transfers energy faster than the expansion brings the sectors to a common temperature, ξ = 1, and erases any difference that reheating left [T]. When the hidden sector is the colder one, a portal too weak for that still moves some energy across: it produces hidden particles slowly from the visible plasma, the [freeze-in](/wiki/dark-matter/candidates/relic-abundance#freeze-in-t) route, and warms the hidden sector [T]. A colder hidden sector is therefore a statement about its portals as well as about its reheating.

The referee named two portals for #14's sector, and the adjudication took both as to-do items without re-checking them ([omitted constraints](/wiki/method/review/round-3/rulings#omitted-constraints)).

- **The Higgs portal.** For #14's adjoint scalar Φ the coupling is λ_p |H|² Tr Φ², with H here our Higgs doublet, "allowed by every stated symmetry". Keeping the electroweak scale natural "needs lambda_p <= 2.4e-20 - 7.5e-21", while "equilibration at T~v for lambda_p >~ 5e-2 (rough 2->2 estimate) would set xi=1 -> Delta N = 0.86 (excluded). Technically natural to set small, but unstated" (Step 4(c) item 7).
- **Kinetic mixing.** With mixing parameter ε, the hidden fermion ψ carries a small visible charge, and the SM plasma produces it: "with eps = 1e-6 the SM freeze-in of psi reaches equilibrium for all m_psi <= 30 GeV", after which "The hidden sector is re-thermalised below v and the reheating ratio xi is no longer the operative variable." ΔN_eff is then "set by decoupling at T_d ~ m_psi/4": "T_d < 0.2 GeV -> Delta N >= 0.61 (excluded); T_d = 0.2-30 GeV -> 0.065-0.11 (gamma' only) up to 0.48-0.83 if the psi entropy is dumped after decoupling (step4.out)" (Step 4(a) item 5; [a millicharged ψ](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#i-a-millicharged-ψ)). [Round-3 Decision 1](/wiki/method/review/round-3/decisions#decision-1-strict-sector-separation) closed this channel by taking P4 strictly: kinetic mixing is "ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry", which "closes three failure channels at once", among them "re-thermalization of the hidden sector".

## How the program uses it

### The retired soliton candidate

The [soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) proposed that dark matter is superheavy monopoles of #14's hidden SU(2)_d sector. The unbroken U(1)_d of that sector, "(iii) an unbroken U(1)_d" among #14's requirements (§6), leaves a massless hidden photon, and the photon made the hidden temperature a constraint. #14 §4:

> Dark radiation. The hidden photon is radiation. Suppose the two sectors shared a temperature above v. The hidden sector - the SU(2)_d gauge fields, the adjoint scalar and one psi doublet - then contributes Delta N_eff ~ 0.86 after its heavy states disappear. That is excluded by Planck 2018 (N_eff = 2.99 +- 0.34 at 95%) [23]. The proposal therefore requires the hidden sector to have been reheated to xi < 0.77 of our temperature, an assumption about reheating that the framework does not fix.

The quoted interval is flag 22 in `review/wiki-build-flags.md`. #14 §6 lists "the dark-radiation requirement" among the results "Derived within the framework or by standard methods", "the colder reheating of the hidden sector" among the "Conjectural" claims, and "(ii) a hidden-to-visible temperature ratio xi < 0.77 after reheating" among the "Requirements forced by consistency (not optional)". The v3 worklog had called ξ "a free parameter of the framework" (O2).

Round 3 found the following.

- **The bound.** [Ruling 5](/wiki/method/review/round-3/rulings#rulings-5-and-6-the-colder-hidden-sector-and-nucleosynthesis), "Upheld (minor)": "ξ bound 0.760, not 0.77", because "Using N_eff,SM = 3.044, the 95% bound is ΔN_eff < 0.286" [V], gated as above. The referee's table gives the spread over conventions: "0.760 (N_SM=3.044), 0.759 (3.046); 0.769 only if DeltaN<0.30" (Step 2). #14's 0.77 had come from the worklog's bound of 0.3, "an approximate Planck 2018 value, from memory †" (O2).
- **The ratio not carried through.** v3 required ξ < 0.77 but computed its relics at ξ = 1. The round-3 [pre-registration](/wiki/method/review/round-3/preregistration) had named this its second runner-up weakest link: "Thermal-history consistency. The W′ and ψ freeze-out are computed at ξ = 1, but dark radiation requires ξ < 0.77, and Kibble production with a colder hidden sector is treated only by the ξ^(3/4) scaling." The referee recomputed at the required ratio: "W' overclosure survives (xi=0.76: 9.9e15 - 2.9e16, step4b.out)", while for ψ "10% DM at 35 GeV (xi0=0.76) - the manuscript's "below about 0.1 TeV" would make psi ~70-100% of DM (step2c_psi.out: 73.1% at 100 GeV, xi0=0.76)" (Step 4(a) item 4; DM is dark matter). [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure#a-colder-hidden-sector) survives the change; [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window#at-the-colder-sector-v3-itself-required) does not.
- **The mass.** A colder hidden sector reaches its transition when our plasma is hotter, which changes the monopole count. #14 §4: "A colder hidden sector lowers M\* by xi^(3/4), a factor of 0.8 at the bound"; the referee confirmed "0.822 (xi=0.77), 0.814 (xi=0.76)" (Step 2). After the Kibble correction, the referee's minimum-production mass at ξ = 0.76 is "2.34e12-3.61e12 GeV" (Step 4(a) item 1; [with the colder hidden sector](/wiki/dark-matter/candidates/soliton-candidate/overproduction#with-the-colder-hidden-sector)).
- **Freeze-out during nucleosynthesis.** Ruling 6, in [freeze-out on the hidden clock](#freeze-out-on-the-hidden-clock-t) above.
- **Reheating and portals.** The referee's reheating requirements and the Higgs portal, which the adjudication's to-do list carries as "The reheating mechanism for ξ" and "The Higgs portal", and the millicharge channel closed by Decision 1, in the two sections above.

The candidate is dead ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)), and the numbers above are its record. [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) holds the full account, including #14's choice to treat the hidden sector with ordinary relativistic quantum field theory.

### The conjugate sector

Outside the withdrawn #14 and its review, no program document gives the conjugate sector a temperature or computes its contribution to N_eff (the wiki's search of the papers and notes). The N_eff entry of the predictions tables comes from the geometry of the dual frame, not from a hidden plasma: in [row 10](/wiki/predictions/early-universe-step), the curvature of a closed dual space acts on our expansion as negative dark radiation ([row 10's negative ΔN_eff](/wiki/cosmology/early-universe/radiation-era#row-10-negative-δn_eff-from-a-closed-dual-space)).

The lab notebook's sketch of polarization-genesis, tagged [O, sketched], sets the division between the two kinds of matter at reheating: "at reheating, the heavy Grassmannian moduli (the nine non-Maslov directions) decay; their branching into x- versus p-polarized quanta is set by the vacuum tilt angle" (#1 §8, transcribed from its LaTeX). As for a hidden sector reheated separately, the outcome would be fixed by how a decay at reheating divides its energy between the two kinds of matter, a parallel the documents do not draw ([Open: polarization-genesis and the 5.4 : 1 ratio (OP7)](/wiki/dark-matter/candidates/polarization-genesis); [reheating in polarization-genesis](/wiki/cosmology/early-universe/inflation-and-dilution#reheating-in-polarization-genesis)).

## What is open

Nothing on this page is an open problem of the program: the physics is standard, and its only applications in the record belong to a dead candidate. What was left unchecked is recorded as such.

- **Accepted without re-checking.** The adjudication took the referee's list of omitted constraints "as a to-do; not individually re-checked", including "The reheating mechanism for ξ", "The Higgs portal" and "Re-thermalization by ψ at ε ~ 1e-7–1e-6". Decision 1 closed the third, and Decision 2 then retired the candidate the list was written against ([what became of the list](/wiki/method/review/round-3/rulings#what-became-of-the-list)).
- **Not computed.** The dark-radiation isocurvature of a separately reheated hidden sector, "(conditional; not computed)" (Step 4(c) item 9).
- **Not gated.** Ruling 6's lower bound on ψ's mass rests on the referee's script, was "Accepted, not re-checked", and is not checked by `verify/soliton_obituary.py` (flag 33 in `review/wiki-build-flags.md`).
- **The conjugate sector.** No document addresses the temperature of the program's own conjugate sector (above).

## Standard references

The program's documents cite two sources for this physics:

- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17], which the round-3 referee resolved as "Front. Phys. 69 (1990), Addison-Wesley" and marked "standard; not checked page-level" (audit notes, Step 1). A standard treatment of decoupled species and entropy conservation.
- Planck Collaboration, Astron. Astrophys. 641, A6 (2020), arXiv:1807.06209: #14's reference [23], "Planck 2018 VI" in the round-3 audit, which records its eq. (67b) as "N_eff = 2.99 +0.34 -0.33" (Step 1).

Cited by the round-3 referee:

- Adshead, Ralegankar and Shelton, arXiv:2206.13530: decoupling at "T_d ~ m_psi/4", from its eqs. 2.17–2.19 (Step 4(a) item 5), and the "thermalisation threshold m_th = 4 T_d" (Step 4(c) item 2).

Added by the wiki from model memory (†):

- E. W. Kolb, D. Seckel and M. S. Turner, Nature 314, 415 (1985)†: a hidden ("shadow") sector at a temperature different from ours, and the limits nucleosynthesis places on it.
- J. L. Feng, H. Tu and H.-B. Yu, JCAP 10 (2008) 043†: thermal relics of hidden sectors at their own temperatures.

The † entries are unverified.

## Used by

- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — the soliton candidate's dark radiation, the bound ξ < 0.760 and its inconsistent application.
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — ψ's relic at the hidden temperature, and its freeze-out timed against nucleosynthesis.
- [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) — the exclusion recomputed at ξ = 0.76.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — the closing mass shifted by ξ^(3/4).
- [Kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) — re-thermalization through a millicharged ψ.
- [Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary) — requirement (ii), the colder hidden sector.
- [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings) — rulings 5 and 6, the Higgs portal and the reheating mechanism.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — the gated bounds ΔN_eff < 0.286 and ξ < 0.760.
- [Thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out) and [relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance) — freeze-out in a sector at its own temperature.
- [Inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution), [gravitational waves from phase transitions](/wiki/cosmology/early-universe/phase-transition-gravitational-waves), [Big Bang nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis) and [the cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background) — a hidden sector reheated colder, the visible temperature v/ξ of a hidden transition, ψ's freeze-out during nucleosynthesis, and the dark-radiation bound.

## Sources

- `notes/knot-dark-matter-standalone.md` §4 — the dark-radiation paragraph: ΔN_eff ~ 0.86 at a shared temperature, Planck's interval as #14 wrote it, ξ < 0.77 and the ξ^(3/4) shift of M\*; §3 — ψ "above the MeV scale" and the ordering of inflation and the hidden transition; §6 — the requirement as derived, the colder reheating as conjectural, requirements (ii) and (iii); 'References' [17], [23] — Kolb and Turner, Planck 2018 (withdrawn)
- `review/v3-worklog.md` 'New open items' (O2) — the two-sector setup, the table of three hidden contents, the 0.3 bound from memory †, ξ as a free parameter
- `review/round3-preregistration.md` 'Predictions' — the thermal-history consistency link
- `review/round3-adjudication.md` 'Rulings' 5, 6 — ξ < 0.760 and ΔN_eff < 0.286 with N_eff,SM = 3.044; ψ's freeze-out during nucleosynthesis, accepted, not re-checked; the omitted-constraints list — reheating, the Higgs portal and re-thermalization as unchecked to-dos; 'Decisions' 1 — strict sector separation
- `verify/soliton_obituary.py` 'Dark radiation (ruling 5)' — the ΔN_eff function and its anchor, the bound, ξ and the gravitational-wave knock-on, executed
- `review/round3/referee/audit-notes.md` Step 1 — the Kolb–Turner and Planck references; Step 2 — the shared-temperature ΔN_eff, the spread of the ξ bound, the factor ξ^(3/4); Step 4(a) items 1, 4, 5, 8 — the closing mass at ξ = 0.76, the recomputation at the required ratio, re-thermalization by a millicharged ψ, freeze-out during nucleosynthesis; Step 4(c) items 2, 7, 9 — the decoupling reference, the Higgs portal, reheating and isocurvature
- `review/round3/referee/step2a.py` 'Delta N_eff' and `review/round3/referee/step2a.out` 'dark radiation' — the degrees-of-freedom count, the late ratio, ΔN_eff at ξ = 1 and the bound on ξ; the frequency table at g\* = 106.75 and 122.75
- `review/round3/referee/step2c_psi.py` — the entropy ratio R that fixes the hidden temperature in the relic integration
- `review/round3/referee/step4.out` item 7 — ψ's hidden freeze-out in visible temperatures; `review/round3/referee/step4c.out` — the visible reheating temperatures
- `papers/broken-born-checkpoint-v2.md` §4 — P4, taken strictly since v2.1
- `notes/broken-born-theory.md` §5.3 — the conjugate sector as "gravitationally-only-connected"; §8 — polarization-genesis at reheating [O, sketched]
- `review/wiki-build-flags.md` item 22 — #14's symmetric N_eff interval; item 33 — ruling 6's figure outside the gate
