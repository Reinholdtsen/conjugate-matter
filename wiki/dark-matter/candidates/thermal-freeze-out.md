---
title: "Thermal freeze-out"
weight: 15
status: established
description: "How a stable species once in equilibrium with the hot plasma ends with a fixed relic density: the Boltzmann equation, why freeze-out comes near T ~ m/20, the s-wave relic formula exactly as verify/soliton_obituary.py codes it and its anchor, freeze-out in a sector at its own temperature, and the program's uses — particle χ, which the notebook argues cannot freeze out; row 7's expected relic; and the W′ and ψ relics of the retired soliton candidate."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §13 row 7"
  - "papers/broken-born-checkpoint-v2.md §14 item 7"
  - "review/round3-adjudication.md 'Rulings' 4"
  - "review/round3-adjudication.md 'Rulings' 5"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "review/round3-adjudication.md 'Rulings' 10"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Decisions' 3"
  - "review/round3-adjudication.md 'Lessons' 2"
  - "verify/soliton_obituary.py"
  - "review/round3/adjudicator/round3_arb.py"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/step2c_psi.out"
  - "review/round3/referee/step4.out"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/v3-worklog.md 'New open items'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "HANDOFF.md §2"
  - "HANDOFF.md §8"
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §11"
  - "notes/broken-born-theory.md 'Addendum (v0.2)'"
  - "notes/debt3b-wave-island.md 'Bonus: the relic debt closes itself'"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §6"
  - "notes/knot-dark-matter-standalone.md 'References'"
---

*Thermal freeze-out is the standard account of how many particles of a stable species are left over from the hot [early universe](/wiki/cosmology/early-universe) when the species was once in equilibrium with the plasma. While the plasma is hot, the particles are made and annihilated in pairs at equal rates. Once the temperature falls below their mass, their equilibrium number falls exponentially; when annihilation becomes too slow to keep pace with the expansion of the universe, particles stop meeting partners, their number per unit entropy stops changing, and the species has frozen out. Typically this happens when the temperature has fallen to about a twentieth of the mass. The weaker the annihilation, the more particles survive: the relic density is roughly inversely proportional to the annihilation cross-section. The program meets freeze-out in three places. The [lab notebook](/wiki/history/documents/lab-notebook) argues that [particle χ](/wiki/dark-matter/candidates/chi-particles), connected to ordinary matter only by gravity, cannot get its abundance this way, which leaves the ratio of dark to ordinary matter as an open problem, [OP7](/wiki/dark-matter/candidates/polarization-genesis). The standard expectation against which [row 7](/wiki/predictions/direct-detection-null) predicts a permanent null in direct detection is a freeze-out relic coupled to ordinary matter. And the relics of the [hidden sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector) of the [retired soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) are freeze-out relics, computed with the standard formula and recomputed in [round 3](/wiki/method/review/round-3) of blind review: in the sector's minimal version the heavy [W′± would outweigh the observed dark matter 10¹⁶–10¹⁷ times](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure), a result that survives the candidate, and [the mass window of its light fermion ψ](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) was wrong at both edges.*

**Status:** Established — [T] — standard early-universe physics, written here from general knowledge, with the reference the wiki adds marked † (Gondolo and Gelmini 1991†). The relic formula is the one `verify/soliton_obituary.py` codes as "Kolb & Turner eqs. 5.43-5.45", from reference [17] of the withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate), which the round-3 referee resolved but did not check page by page; the script checks the formula on a standard relic before using it ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). The program's uses carry their own tags: the argument that particle χ cannot freeze out is [O] (#1 §5.3), and W′ overclosure is [V] ([checkpoint #11](/wiki/history/documents/checkpoint) §12).

## Equilibrium and departure from it [T]

### The Boltzmann equation

A stable species that interacts with the particles of the hot plasma is created and destroyed in pairs: two of its particles annihilate into lighter ones, and the inverse reaction makes a pair out of the plasma. Its number density n obeys the Boltzmann equation [T]

```text
dn/dt + 3Hn = −⟨σv⟩ (n² − n_eq²)
```

The term 3Hn is dilution by the expansion at the Hubble rate H: with nothing created or destroyed, n falls as a⁻³, where a is the scale factor. On the right, ⟨σv⟩ is the annihilation cross-section σ times the relative velocity v of the two particles, averaged over their thermal motion. The loss term −⟨σv⟩n² is quadratic because annihilation needs two particles to meet; the gain term +⟨σv⟩n_eq² is the inverse reaction, whose rate is fixed by the requirement that the two balance at equilibrium, n = n_eq.

The equilibrium density n_eq depends on how the temperature T compares with the mass m [T]:

- for T well above m the species is relativistic, and n_eq grows as T³, as the photon density does;
- for T below m, n_eq ∝ g (mT)^{3/2} e^{−m/T}, with g the species' number of internal states, such as spin states. Typical collisions in the plasma no longer carry the rest energy of a pair, and the equilibrium density falls exponentially.

### In terms of the yield

Dividing by the entropy density s removes the dilution. The yield Y = n/s stays constant when nothing creates or destroys the particles, because s also falls as a⁻³ ([entropy and the yield Y = n/s](/wiki/cosmology/early-universe/radiation-era#entropy-and-the-yield-y--ns-t)). Take x = m/T as the clock, which grows as the universe cools. While the number of relativistic species does not change, T falls as 1/a, and the Boltzmann equation becomes [T]

```text
dY/dx = −(s⟨σv⟩ / (H x)) · (Y² − Y_eq²)

d ln Y / d ln x = −(Γ/H) · (1 − Y_eq²/Y²)        Γ = n⟨σv⟩
```

where Y_eq = n_eq/s and Γ is the rate at which one particle annihilates. The second form compares two rates per unit of ln x [T]. Y is pulled toward Y_eq at a rate set by Γ/H. Below T ~ m the target itself moves: the factor e^{−x} makes Y_eq fall at a rate of about x per unit of ln x. While Γ/H is larger than that, Y follows Y_eq down. Γ falls with the density, exponentially, and H only as T², so Γ/H drops quickly. Once it falls below about x, Y can no longer follow; it departs from Y_eq, and soon after, with Γ/H much less than one, it stops changing. The species has frozen out, and its yield is carried unchanged to the present, where its density is ρ = m·Y·s₀, with s₀ the entropy density today ([what is being set](/wiki/dark-matter/candidates/relic-abundance#what-is-being-set)).

## Why freeze-out happens near T ~ m/20 [T]

Freeze-out is where Γ/H falls to about x. Take a cross-section σ₀ that does not depend on velocity, so that Γ = n_eq σ₀ just before freeze-out, with n_eq as above, and the radiation-era expansion rate H = 1.66 √g\* T²/M_Pl, where g\* is the effective count of internal states of all relativistic species and M_Pl is the [Planck mass](/wiki/gravity/spin-2-fields/planck-units) ([the expansion rate](/wiki/cosmology/early-universe/radiation-era#the-expansion-rate-t)). The condition Γ = xH at T = m/x then takes the form [T]

```text
x_f = ln(C · g M_Pl m σ₀ / √g*) − ½ ln x_f
```

with C a pure number and x_f = m/T_f the freeze-out point. The script's formula has this form, with C = 0.038 (next section). The rougher criterion Γ = H, often quoted, gives +½ ln x_f in place of −½ ln x_f.

x_f is the logarithm of a large dimensionless number, the Planck mass (1.22089×10¹⁹ GeV in the script) times m σ₀ times C and g/√g\*, plus a small correction. A logarithm changes little when its argument changes by orders of magnitude: multiplying σ₀ or m by any factor adds only about the logarithm of that factor to x_f. That is why one rule of thumb serves for many species. The round-3 adjudication writes it "T_f ~ m/20" ([ruling 6](/wiki/method/review/round-3/rulings#rulings-5-and-6-the-colder-hidden-sector-and-nucleosynthesis)), and the script starts its iteration for x_f at 20.

The rule is a typical value, not a constant [T]. For annihilation through a gauge coupling α, σ₀ = κπα²/m² with κ a pure number, and the argument of the logarithm is then proportional to M_Pl α²/m: x_f is larger for a light species and smaller for a heavy one. The script solves for x_f in every case rather than setting it to 20.

## The s-wave formula as the program codes it

For s-wave annihilation, from a state of zero orbital angular momentum, σv tends to a constant at low velocity, written σ₀ [T]. `verify/soliton_obituary.py` codes the standard approximate solution as "Kolb & Turner eqs. 5.43-5.45", with masses in GeV and σ₀ in GeV⁻²:

```text
Ω h² = 1.07×10⁹ x_f / (√g* M_Pl σ₀)
x_f  = ln(0.038 g M_Pl m σ₀ / √g*) − ½ ln x_f
```

Here Ω h² is the relic's fraction Ω of the critical density times h², with h the present Hubble rate in a conventional unit ([what is being set](/wiki/dark-matter/candidates/relic-abundance#what-is-being-set)), g is the species' number of internal states and g\* the effective count of internal states of all relativistic species at freeze-out. The second line is the freeze-out condition of the previous section. Because x_f appears on both sides, the script iterates it, starting at 20 and substituting 100 times. Cross-sections quoted in cm³/s are converted with the script's factor 3.8938×10⁻²⁸ × 2.99792458×10¹⁰: the first number converts GeV⁻² to cm², and the second is the speed of light in cm/s [T].

The first line follows from the yield equation [T]. Annihilation does not stop abruptly at x_f; it continues at a falling rate and lowers Y further. With σ₀ constant, s ∝ T³ and H ∝ T², the coefficient s⟨σv⟩/(Hx) falls as 1/x², and after freeze-out Y_eq is negligible:

```text
dY/dx ≈ −(λ/x²) · Y²        λ = s(m) σ₀ / H(m)

1/Y_∞ − 1/Y(x_f) = λ/x_f
Y_∞ ≈ x_f/λ = x_f H(m) / (s(m) σ₀)
```

where H(m) and s(m) are the expansion rate and entropy density at T = m, and 1/Y(x_f) has been dropped as small next to λ/x_f. Since H(m) grows as m² and s(m) as m³, Y_∞ falls as 1/m at fixed σ₀, and the mass cancels from the density today, m·Y_∞·s₀, except through x_f. Dividing by the critical density gives the first line: the constant 1.07×10⁹, in GeV⁻¹ given the units above, collects the present entropy density, the critical density and the numerical factors of H and s.

Two consequences carry the program's uses [T].

- **Weaker annihilation, more survivors.** At fixed x_f, Ω h² ∝ 1/σ₀.
- **Heavier, more survivors, at fixed coupling.** When the annihilation runs through a gauge coupling α, σ₀ = κπα²/m², with κ fixed by the final states, and Ω h² ∝ x_f m²/(κα²): a heavier species annihilates more weakly and leaves more behind. A Dirac fermion annihilating into two massless gauge bosons has κ = 1 exactly at leading order, σv = πα²/m², as an electron and a positron annihilating into two photons do; this is the cross-section the script uses for ψ. For the W′± it brackets κ between 1 and 10.

### What the formula assumes [T]

The formula is an approximate solution, and its assumptions mark where a fuller treatment is needed.

- **One plasma.** The species is in equilibrium, until freeze-out, with a plasma whose temperature also sets H through g\*. A hidden sector at its own temperature breaks this (next section).
- **Radiation domination and a steady g\*.** H = 1.66 √g\* T²/M_Pl holds in the radiation era, and the solution treats g\* as constant through freeze-out.
- **s-wave annihilation.** σv is the constant σ₀. A cross-section that varies with velocity, such as p-wave annihilation or annihilation enhanced at low velocity by a long-range attraction (Sommerfeld enhancement), changes both lines.
- **One species at a time.** The formula gives the relic of one species with g internal states. A distinct antiparticle, and each member of a multiplet, freezes out alongside it and adds its own relic. The script multiplies by 2 for W′⁺ and W′⁻, and by 4 for ψ, ψ̄ and the two members of the doublet, where v3 of #14 had counted one ([ruling 4](/wiki/method/review/round-3/rulings#ruling-4-the-ψ-relic-window)).

### The anchor

Before the script uses the formula on the hidden sector, it checks it on a standard relic:

```text
PASS  freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)
```

The inputs are m = 100 GeV, g = 2 and g\* = 90, and the check passes when Ω h² lies between 0.06 and 0.24; it prints no value. Two earlier executions with the same mass and cross-section give values. The predecessor script recorded "Ω h² = 0.108" (`review/v3-worklog.md`, 'New open items', O1), and the round-3 referee's own relic code printed "[validation] visible Majorana WIMP 100 GeV, <sv>=2.2e-26: Omega h^2 = 0.1145 (expect ~0.10-0.12)" (`review/round3/referee/step2c_psi.out`; audit notes, Step 2), a WIMP being a weakly interacting massive particle and a Majorana particle its own antiparticle.

The anchor is independent of the manuscript: a textbook relic, not one of the paper's own numbers, as round-3 lesson 2 requires ([independent anchors](/wiki/method/verification/independent-anchors)). It tests the function and its units. It does not test the inputs a later use feeds the function, the count of species, the cross-section and the temperature, and the ψ window failed on such inputs: v3's script had checked its formula on the same relic, getting 0.108, while counting one ψ species where there were four and bracketing a cross-section that is known exactly (ruling 4). Of the numerical findings that survived round 3, this one among them, the adjudication wrote: "All are wrong inputs or model choices in my scripts, not arithmetic slips" ('Pre-registration scored'; [verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

## Freeze-out in a sector at its own temperature [T]

A hidden sector that has decoupled from the visible plasma keeps its own temperature T_h. Its ratio to the visible temperature T, written ξ = T_h/T, is set by the two sectors' histories ([a sector with its own temperature](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#a-sector-with-its-own-temperature)). Freeze-out in such a sector differs in three ways [T].

- **The clock.** A hidden species is held at equilibrium by its own plasma, so n_eq is set by T_h, and the freeze-out point refers to it: T_h ~ m/20 in the rule of thumb.
- **The expansion rate.** H is set by the total energy density of both sectors, mostly the visible plasma's when the hidden sector is colder. At a given T_h the universe therefore expands faster than it would if everything were at T_h, which changes both x_f and the final yield. The formula above, written for one plasma, does not include this.
- **The visible clock.** The same freeze-out falls at a hotter visible temperature, T_h divided by the temperature ratio at that moment. This matters when something in the visible plasma is under way at that time, such as [nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis).

The script's function has no temperature ratio. The round-3 referee's own relic integration, which follows the hidden temperature from a starting ratio ξ₀, is described on [the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window#the-referees-numbers); its results for the program's cases are below.

## Other freeze-outs in the record

The comparison of a reaction rate with the expansion rate appears in the record in two other settings, and the word "freeze-out" has one different sense in the standard physics.

- **The neutron-to-proton ratio.** At the start of nucleosynthesis, the weak reactions that turn neutrons into protons and back become slower than the expansion, and the ratio of the two stops changing [T] ([neutron–proton freeze-out](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#neutronproton-freeze-out)). The round-3 referee's script marks it at "n/p freeze-out ~0.8 MeV" of visible temperature (`review/round3/referee/step4.out`).
- **Monopole annihilation.** A monopole and an antimonopole annihilate when they meet, and #14 asked for "the strong-coupling relic freeze-out calculation of Sec. 3, in the hidden plasma" (§6). Defects differ from a thermal relic in one respect [T]. They form at a phase transition by the [Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) and are far too heavy to be remade from the plasma, so their equation has no n_eq² term. Annihilation can only lower a number set at formation, and it stops once the rate per monopole falls below H ([annihilation is not enough](/wiki/electric-magnetic-duality/monopoles/monopole-problem#annihilation-is-not-enough-t)).
- **Kibble–Zurek dynamics.** Near a continuous phase transition the field's relaxation time grows, and its correlation length freezes at the value it had when the field could no longer follow the cooling [T] ([continuous transitions](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism#continuous-transitions-kibblezurek)). The word is the same, but what freezes is a length set by the dynamics of the transition, not the abundance of a relic.

## How the program uses it

### Particle χ: the route the notebook closes

The lab notebook excludes thermal freeze-out for the program's dark-matter particle [O]:

> A sub-GeV, strongly self-coupled, gravitationally-only-connected sector cannot freeze out thermally without cannibalism problems; the abundance must be set asymmetrically — by *polarization-genesis* (§8). The observed Ω_χ/Ω_b = 5.4 is an input awaiting a mechanism, exactly as η_B awaited baryogenesis. (#1 §5.3)

Ω_b is the baryon density and η_B the baryon asymmetry. In the terms of this page, freeze-out needs a plasma that holds the species at its equilibrium density and an annihilation channel into lighter particles, whose rate sets the relic. [P4](/wiki/program/postulates/p4-polarized-matter#the-strict-reading-since-v21), read strictly since version 2.1 of [checkpoint #11](/wiki/history/documents/checkpoint), states that no gauge force crosses between ordinary matter and [conjugate matter χ](/wiki/dark-matter/conjugate-matter) (#11 §4). χ then has no channel into ordinary particles except through gravity, which is far too weak to hold it in equilibrium with our plasma [T]. Within its own sector, a χ with nothing lighter to annihilate into can lower its number only by number-changing self-interactions, in which several particles scatter into fewer and the lost rest mass heats the rest. That is [cannibal dark matter](/wiki/dark-matter/candidates/relic-abundance#cannibal-dark-matter-t), whose abundance is set by the sector's self-coupling and initial temperature [T]. The notebook does not say which "cannibalism problems" it means ([why the standard route fails for particle χ](/wiki/dark-matter/candidates/polarization-genesis#why-the-standard-route-fails-for-particle-χ)).

The argument has three consequences in the record.

- **An asymmetry is needed.** The notebook's open problem 5 is "Relic abundance without cannibalism: needs the asymmetric mechanism of (4). [O]", item 4 being polarization-genesis (#1 §11). #11 carries the ratio as §14 item 7, "Polarization-genesis: Ω_χ : Ω_b = 5.4 : 1 [O]", and states that "The 5.4 : 1 abundance question (polarization-genesis) applies to both" candidates (§12) ([Open: polarization-genesis and the 5.4 : 1 ratio (OP7)](/wiki/dark-matter/candidates/polarization-genesis); [asymmetric dark matter](/wiki/dark-matter/candidates/relic-abundance#asymmetric-dark-matter-and-the-sakharov-conditions-t)).
- **The wave island escapes it.** Very light χ, on the [wave island](/wiki/dark-matter/momentum-clumping/wave-island), is a coherent field produced by [misalignment](/wiki/dark-matter/wave-dark-matter/misalignment-mechanism), and a field that is never in thermal equilibrium does not freeze out [T]. [Debt 3](/wiki/history/debts) recorded: "Open problem #5 (cannibalism-safe relic abundance) is moot on the wave island: misalignment is the mechanism", while "The 5.4:1 question remains" (`notes/debt3b-wave-island.md`, 'Bonus'). The notebook's addendum v0.2 records the closure: "open problems 3 and 5 close (5 via misalignment production on the wave island)" ([relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)).
- **The candidate is particle χ.** The χ candidate of #11 §12, whose knee has a "sharp tail", is the particle kind ([particle χ and wave χ](/wiki/dark-matter/candidates/chi-particles#particle-χ-and-wave-χ)), on the [particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem). The record applies no misalignment there, and on this wiki's reading the notebook's argument still applies.

### Row 7: the relic the searches expect

Row 7 of the [predictions table](/wiki/predictions) sets the program's permanent null in direct detection against a standard expectation, "WIMP-type signal eventually" (#11 §13). A weakly interacting massive particle (WIMP) is a particle whose annihilation into ordinary particles, at about the strength of the weak interaction, leaves about the observed density by freeze-out [T]. The anchor above is one: the referee calls it a "standard 100 GeV WIMP" (audit notes, Step 2). A particle that annihilates into ordinary particles also scatters off them and can be made from them [T], so detectors and colliders should eventually see it. The program requires instead a "Permanent null (both dark-sector candidates SM-decoupled; P4 strict)", SM being the Standard Model, and is killed by "Any confirmed non-gravitational DM–SM coupling", DM being dark matter (#11 §13 row 7). In this wiki's reading, the coupling whose absence makes the null a prediction is the one whose absence closes freeze-out for particle χ (above).

### The retired candidate's hidden sector

The soliton candidate of #14 v3 consisted of monopoles of a hidden SU(2) → U(1) sector. The monopoles were to form when the hidden plasma cooled through the breaking scale v, and every stable massive particle of that plasma would then freeze out like any thermal relic. v3 computed these relics with standard freeze-out, and round 3 recomputed them, the referee with its own code and the adjudicator, for ψ, with the formula above; the gate script now applies that formula to both the W′ and ψ cases. The candidate is retired; the first result below survives it, and the rest belong to the record of its failure.

- **W′ overclosure [V].** In the minimal sector the charged gauge bosons W′± are the lightest particles with hidden charge, hence stable, and "Kibble production (below) requires a hidden plasma at temperature ~ v, so the W' are thermally populated and freeze out" (#14 §3). Their mass at the withdrawn benchmark is "m_W' ~ (5-9)e11 GeV", and at such masses σv ∝ 1/m² is small: "Standard freeze-out [17] then leaves them at 1e16 to 1e17 times the observed dark-matter density" (#14 §3). The script uses σv = κπα_W′²/m_W′² with κ = 1 and 10, g = 3 and both charges counted, and passes: `PASS  stable W'+- overclose by 1e16-1e17  [9.5e+15-2.0e+17]`. The referee's coefficient from [detailed balance](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure#the-annihilation-coefficient-by-detailed-balance), 6.67 (written c in the audit), gives "1.3e16-4.0e16" (audit notes, Step 2). #11 §12 keeps the result among what survives: the minimal sector "is excluded on its own terms: its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V]" ([W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure#freeze-out-and-the-size-of-the-overclosure)).
- **The ψ relic window (dead).** v3's remedy was a light Dirac doublet ψ for the W′± to decay into, and "psi is then itself stable by U(1)_d charge and freezes out by annihilating to hidden photons" (#14 §3). Because σv falls as 1/m², a heavier ψ leaves more behind, so ψ had to be light to stay a minor component; v3 took "m_psi below about 0.1 TeV". Ruling 4, upheld: "v3 omitted ψ̄ and the second doublet member (a factor of 4), and bracketed an exactly known s-wave σv up to ×10. My recount: 10% of the DM at 45–49 GeV, 100% at 146–158 GeV". The script repeats the recount with σv = πα²/m², four species and g\* = 80 and 106.75: `PASS  10% of the dark matter at 45-49 GeV  [45.2-48.8]` and `PASS  100% at 146-158 GeV  [146.4-158.0]`. The referee's own integration gives "28–46 / 96–153 GeV", and the two agree "to within ×1.6" (ruling 4) ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window#the-upper-edge-a-miscount-of-states-and-an-exact-cross-section)).
- **Freeze-out during nucleosynthesis.** v3's lower edge put ψ "above the MeV scale, so that psi has annihilated before nucleosynthesis" (#14 §3). In the colder hidden sector the referee found that "hidden freeze-out T_h ~ m/20 occurs at T_vis ~ 0.08 MeV for m_psi = 1 MeV, 0.24 MeV for 3 MeV, 0.71 MeV for 10 MeV (step4.out) - i.e. during BBN. Needs m_psi >~ 20-30 MeV" (audit notes, Step 4(a) item 8), BBN being Big Bang nucleosynthesis. Ruling 6 accepted the finding without re-checking it: "T_f ~ m/20, so the lower mass bound should be ≳ 20–30 MeV" ([the lower edge](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window#the-lower-edge-freeze-out-during-nucleosynthesis)).
- **Computed at one temperature.** v3 required the hidden sector to be colder than ours, ξ < 0.77 (0.760 after ruling 5), so that its massless photon does not add too much radiation, yet computed both freeze-outs at ξ = 1. The worklog says so for the W′: "Computed at ξ = 1 only. The effect of a colder dark sector on the W′ freeze-out is not scripted" ('New open items', O1). The round-3 [pre-registration](/wiki/method/review/round-3/preregistration) named "Thermal-history consistency" its second runner-up weakest link. The referee recomputed at the colder ratio: "W' overclosure survives (xi=0.76: 9.9e15 - 2.9e16, step4b.out)", and "psi window computed with hidden temperature (step2c_thr.out): 10% DM at 35 GeV (xi0=0.76)" (audit notes, Step 4(a) item 4) ([applied inconsistently](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history#applied-inconsistently)).
- **Monopole annihilation and the √N floor (dropped).** #14 left the monopoles' own annihilation open: "Whether the Kibble abundance survives requires a dedicated strong-coupling freeze-out calculation in that plasma, not performed here (acceptance criterion 3)" (§3). [The handoff](/wiki/history/documents/handoff) paired the question with a chat-only answer, a "√N topological-charge floor" under the abundance (§2, open item 2), and queued a "√N-floor freeze-out estimate" (§8 item 3). Ruling 10 upheld, at abstract level, the referee's finding that this regime was already worked out: "Annihilation at α_m ≈ 34 is Preskill's Dirac case, already done for hidden sectors". Decision 3 dropped the estimate: "Its premise, Kibble as a ceiling, is inverted (ruling 3)", and "Under decision 2 it has no candidate left to serve" ([Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor); [Decision 3](/wiki/method/review/round-3/decisions#decision-3-the-n-floor-dropped)).

## Standard references

The program's documents cite one source for this physics:

- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14 reference [17], unmarked, cited for the W′ relic ("Standard freeze-out [17]", §3). The v3 worklog lists it as not live-checked, "a textbook, cited for the freeze-out formula" ('v3 as drafted (2026-10-19)'). The round-3 referee resolved it as "Front. Phys. 69 (1990), Addison-Wesley" and noted "standard; not checked page-level" (audit notes, Step 1). The equation numbers 5.43–5.45 are the script's label; the record does not check them against the book.

Added by the wiki from model memory (†):

- P. Gondolo and G. Gelmini (1991)†: the thermal average ⟨σv⟩ and the freeze-out calculation done carefully.

## Used by

- [Open: polarization-genesis and the 5.4 : 1 ratio (OP7)](/wiki/dark-matter/candidates/polarization-genesis) — the notebook closes freeze-out for particle χ, so its abundance needs an asymmetric mechanism.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) — the notebook's argument that particle χ cannot freeze out.
- [The classicality theorem and the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem) — the particle island has neither misalignment nor thermal freeze-out.
- [Relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic) — a field never in equilibrium does not freeze out, so the cannibalism problem does not arise there.
- [Row 7: a permanent null in direct detection](/wiki/predictions/direct-detection-null) — the expected freeze-out relic coupled to ordinary matter, against which the row is set.
- [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) — the s-wave formula applied to the hidden W′±.
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — the formula with σv = πα²/m² and four species, and freeze-out at the hidden temperature during nucleosynthesis.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — relics computed at ξ = 1 although ξ < 0.77 was required.
- [Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) — the dropped estimate of where monopole annihilation stops.
- [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings) — ruling 4's recount and ruling 6's T_f ~ m/20.
- [Round-3 arbitration and the referee's constants](/wiki/method/review/round-3/arbitration) — the s-wave formula in the adjudicator's ψ recount.
- [Independent anchors](/wiki/method/verification/independent-anchors) — a standard freeze-out relic as the anchor of the freeze-out code.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — the freeze-out function and its anchor.

## Sources

- `papers/broken-born-checkpoint-v2.md` §4 — P4 read strictly; §12 — W′ overclosure [V] and the 5.4 : 1 question for both candidates; §13 row 7 — the standard expectation, the null and the kill condition; §14 item 7 — the ratio as an open problem
- `review/round3-adjudication.md` 'Rulings' 4 — the ψ recount and the referee's range; 'Rulings' 5, 6 and 10 — ξ < 0.760, T_f ~ m/20 and the nucleosynthesis bound, annihilation at α_m ≈ 34; 'Pre-registration scored' — "wrong inputs or model choices"; 'Decisions' 3 — the √N-floor estimate dropped; 'Lessons' 2 — an anchor independent of the paper
- `verify/soliton_obituary.py` — the freeze-out function, its inputs and constants, the anchor, the W′ and ψ checks
- `review/round3/adjudicator/round3_arb.py` — the adjudicator's ψ recount with the same formula
- `review/round3/referee/audit-notes.md` Step 1 — Kolb and Turner resolved, not checked page-level; Step 2 — the referee's anchor value 0.1145, the W′ coefficient 6.67; Step 4(a) items 4 and 8 — the colder sector, freeze-out during nucleosynthesis
- `review/round3/referee/step2c_psi.out` — the referee's validation line
- `review/round3/referee/step4.out` — the mark for the freeze-out of the neutron-to-proton ratio
- `review/round3-preregistration.md` 'Predictions' — "Thermal-history consistency" as the second runner-up weakest link
- `review/v3-worklog.md` 'New open items' (O1) — the predecessor's anchor value 0.108, "Computed at ξ = 1 only"; 'v3 as drafted (2026-10-19)' — Kolb and Turner not live-checked
- `HANDOFF.md` §2 — open item 2, the √N floor; §8 — queue item 3, the "√N-floor freeze-out estimate"
- `notes/broken-born-theory.md` §5.3 — why particle χ cannot freeze out [O]; §11 — open problems 4 and 5; 'Addendum (v0.2)' — open problem 5 closed on the wave island
- `notes/debt3b-wave-island.md` 'Bonus: the relic debt closes itself' — misalignment on the wave island
- `notes/knot-dark-matter-standalone.md` §3 — the W′ and ψ freeze-out, the MeV lower edge, the strong-coupling calculation left open; §6 — acceptance criterion 3; 'References' [17] — Kolb and Turner
