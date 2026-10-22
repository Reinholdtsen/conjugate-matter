---
title: "Big Bang nucleosynthesis"
weight: 13
status: established
description: "The formation of the light nuclei in the first minutes: neutron–proton freeze-out, the deuterium bottleneck and helium; what the abundances measure, namely the expansion rate (and through it the radiation content and the strength of gravity) and the baryon density; the limits on light particles, late decays and entropy release; and the program's uses, row 10's G_eff step dated before nucleosynthesis and the retired ψ relic window."
provenance: [T]
sources:
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §10"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 10"
  - "review/round3/referee/step4.out item 7"
  - "review/round3/referee/audit-notes.md Step 4(a) item 8"
  - "review/round3/referee/audit-notes.md Step 4(c) item 2"
  - "review/round3-adjudication.md 'Rulings' 3"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "review/round3-adjudication.md 'Rulings' (omitted constraints)"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/v3-worklog.md 'New open items'"
  - "notes/knot-dark-matter-standalone.md §3"
  - "verify/soliton_obituary.py 'Anchors'"
---

*Big Bang nucleosynthesis (BBN) is the formation of the lightest atomic nuclei, mostly helium-4 with small amounts of deuterium, helium-3 and lithium-7, in the first minutes of the hot early universe. Its outcome depends on the expansion rate at the time. Neutrons and protons stop converting into each other once the weak interactions that convert them become slower than the expansion, and nearly every neutron left when nuclei can survive ends up in helium, so the primordial helium abundance measures how fast the universe was expanding in its first minutes. That makes nucleosynthesis a test of two things at that time, the radiation content, counted as the effective number of light species N_eff, and the strength of gravity; it also limits particles that decay or release energy during or after it. The program uses this timing in two places. The [lab notebook](/wiki/history/documents/lab-notebook) dates an optional step in the effective strength of gravity "before BBN" ([row 10](/wiki/predictions/early-universe-step)), and the [round-3 review](/wiki/method/review/round-3) found that the light hidden fermion ψ of the retired [soliton candidate](/wiki/dark-matter/candidates/soliton-candidate/obituary) would, at MeV masses, still have been [freezing out](/wiki/dark-matter/candidates/thermal-freeze-out#freeze-out-in-a-sector-at-its-own-temperature-t) during nucleosynthesis, so the lower edge of its [relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) was wrong.*

**Status:** Established — [T] — textbook early-universe physics, written here from general knowledge, with the references it adds from model memory (†); no `verify/` script checks it. The expansion rate it rests on, H = 1.66√g\* T²/M_Pl, is an anchor of `verify/soliton_obituary.py` [V] ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). The program's uses are the lab notebook's step in G_eff "before BBN" (#1 §6), which is [D] and not machine-checked, and the round-3 referee's finding, from its own executed code, that MeV-scale ψ would freeze out during nucleosynthesis, which ruling 6 accepted without re-checking.

## The epoch [T]

Nucleosynthesis takes place in [the radiation era](/wiki/cosmology/early-universe/radiation-era), when the energy density is dominated by photons, electrons and positrons, and neutrinos, and the temperature T alone fixes the expansion rate ([the expansion rate](/wiki/cosmology/early-universe/radiation-era#the-expansion-rate-t)):

```text
H = 1.66 √g* T²/M_Pl ∝ √(g* G) T²
```

Here g\* counts the relativistic degrees of freedom, M_Pl = G^{−1/2} is the [Planck mass](/wiki/gravity/spin-2-fields/planck-units), and G is Newton's constant. At neutron–proton freeze-out (below) g\* is close to 10.75, the count that `verify/soliton_obituary.py` takes for photons, electrons and positrons, and three neutrino species. Protons and neutrons are a small admixture, far outnumbered by photons. Their number per photon, the baryon-to-photon ratio n_b/n_γ, is the one free parameter of standard nucleosynthesis [T].

The light elements form in three stages [T].

### Neutron–proton freeze-out

At high temperature, weak interactions such as n + ν_e ↔ p + e⁻ and n + e⁺ ↔ p + ν̄_e convert neutrons and protons into each other fast enough to hold their ratio at its equilibrium value, which is set by the neutron–proton mass difference Δm = m_n − m_p [T]:

```text
n/p = exp(−Δm/T)
```

The rate Γ of these reactions falls with temperature much faster than the expansion rate does [T]:

```text
Γ ∝ G_F² T⁵          G_F the Fermi constant of the weak interaction
Γ/H ∝ T³
```

When Γ falls below H, the conversions stop and the ratio freezes at exp(−Δm/T_f). Setting Γ = H gives the freeze-out temperature [T]

```text
T_f ∝ (g* G)^{1/6} G_F^{−2/3}
```

A faster expansion, whether from more radiation or from a larger G, therefore freezes the ratio earlier, at a higher temperature, and leaves more neutrons [T]. The neutrinos are held in contact with the plasma by the same weak interactions and decouple at about the same time [T]. The round-3 referee's script marks this stage at "n/p freeze-out ~0.8 MeV" of visible temperature (`review/round3/referee/step4.out`, item 7).

### Neutron decay and the deuterium bottleneck

After freeze-out the free neutrons decay, n → p + e⁻ + ν̄_e, and the ratio keeps falling until the neutrons are bound into nuclei [T]. The first step is deuterium, p + n → D + γ. The deuteron is weakly bound, and because photons outnumber baryons so heavily, the high-energy tail of the photon distribution breaks deuterons apart as fast as they form until the temperature has fallen well below the deuteron's binding energy [T]. This delay is the deuterium bottleneck. The referee's script marks its end at "BBN D-formation ~0.07 MeV" (`step4.out`, item 7). Nucleosynthesis, in the sense the round-3 record uses, runs between these two markers ([the lower edge of the ψ window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window#the-lower-edge-freeze-out-during-nucleosynthesis)).

### Helium and the traces

Once deuterium survives, nuclear reactions carry it on quickly to helium-4, the most tightly bound of the light nuclei, and nearly every remaining neutron ends up there [T]. A helium-4 nucleus holds two neutrons and two protons, so the fraction of the baryon mass in helium is

```text
Y_p ≈ 2(n/p)/(1 + n/p)        n/p taken when deuterium forms
```

Y_p is the conventional symbol for the primordial helium mass fraction; it is not the yield Y = n/s of [the radiation era](/wiki/cosmology/early-universe/radiation-era#entropy-and-the-yield-y--ns-t). Heavier nuclei barely form: no stable nucleus has five or eight nucleons, so the chain stalls at helium-4, and by the time helium has formed, the falling temperature and density make further fusion slow [T]. What remains besides hydrogen and helium-4 is the unburnt remainder: small amounts of deuterium and helium-3, and traces of lithium-7 [T].

## What the abundances measure [T]

### The expansion rate: radiation and gravity together

Helium measures the expansion rate at freeze-out, and that rate depends on the radiation content and on G only through the product g\*G. With H′ the changed rate and H the standard one at the same temperature [T]:

```text
(H′/H)² = [g* + (7/4)·ΔN_eff] / g*        extra light species, standard G
(H′/H)² = G′/G                             a different G, standard radiation
```

The first line uses the counting of [the radiation era](/wiki/cosmology/early-universe/radiation-era#extra-species-δn_eff): one extra neutrino species at the neutrino temperature, which at freeze-out equals the photon temperature, adds 7/4 to g\* and 1 to N_eff. A measured helium abundance therefore bounds ΔN_eff during nucleosynthesis if G is assumed standard, or the departure of G from its present value if the radiation content is assumed standard; on its own it cannot tell the two apart [T]. A slower expansion, from fewer light species or a weaker G, lowers the helium fraction, and a faster one raises it [T].

### The baryon density

Deuterium is burnt more completely into helium when there are more baryons, so its abundance falls steeply as n_b/n_γ rises, and among the light elements it is the most sensitive measure of the baryon density [T]. The helium fraction depends on n_b/n_γ only weakly, through the time at which the bottleneck ends [T]. [The cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background) (CMB), released much later, measures the baryon density independently, from the heights of its acoustic peaks. For deuterium and helium the two agree, which tests the standard account of the time between the first minutes and recombination [T]. Lithium-7 is the exception: the abundance predicted for the CMB's baryon density is higher than the abundance measured in the atmospheres of old stars, a long-standing discrepancy called the lithium problem, whose resolution is not settled [T].

### Light particles, decays and entropy release

The abundances also limit anything that changes the plasma during or after nucleosynthesis [T].

- **Light particles.** A particle with a mass near the MeV scale that is in equilibrium during nucleosynthesis adds to the radiation density while it is relativistic, and when it annihilates it heats the particles it is in contact with, which changes both the expansion rate and the final N_eff [T]. A hidden sector at its own temperature counts in the same way, weighted by the fourth power of its temperature relative to ours ([a sector at its own temperature](/wiki/cosmology/early-universe/radiation-era#a-sector-at-its-own-temperature)).
- **Decays.** A long-lived particle that decays during or after nucleosynthesis injects energetic photons or hadrons, which can break up deuterium and helium-4 or make other light nuclei, and its products change n_b/n_γ and the radiation content [T]. The observed abundances bound the amount and the lifetime of such particles [T].
- **Entropy release.** A period of early matter domination that ends in decays dilutes everything made before it ([early matter domination](/wiki/cosmology/early-universe/inflation-and-dilution#early-matter-domination)). The decays must be over, and the expansion back to the standard radiation-dominated form, before nucleosynthesis begins [T].

## Nucleosynthesis and the microwave background [T]

Both measure N_eff, at two epochs: helium in the first minutes, the CMB at recombination ([how N_eff is measured](/wiki/cosmology/early-universe/radiation-era#how-n_eff-is-measured-t)). Agreement between the two values, and between the two baryon densities, limits radiation or entropy added between the epochs [T]. The two measurements are also linked inside a CMB fit: helium sets the number of free electrons before recombination and so affects the damping of the CMB anisotropies, and CMB analyses commonly take the helium fraction that nucleosynthesis predicts for the fitted baryon density ([N_eff in the microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#n_eff)) [T].

## How the program uses it

### Row 10: a step in G_eff "before BBN"

The lab notebook adds the dual sector's gravitational term to the minisuperspace form of the Friedmann equation (#1 §6, [D]):

```text
3H²(M_P² + M̃² a⁻⁶) = ρ
```

with M̃ the dual Planck mass ([the program's extension of Friedmann cosmology](/wiki/cosmology/scale-factor-duality/friedmann-cosmology#the-programs-extension-a-second-scale-factor)). The notebook calls the new term "a stiff-like (a⁻⁶) modification of the effective Planck mass, relevant only at early times", and concludes: "It predicts a step in G_eff before BBN and, conditionally on its one knob, a spectral step in the primordial gravitational-wave background" (transcribed from its LaTeX). [Checkpoint #11](/wiki/history/documents/checkpoint) keeps the step in one clause, "the dual Einstein term is an a⁻⁶ step in G_eff" (§10; [the dual gravity term](/wiki/cosmology/scale-factor-duality/duality-dictionary#the-dual-gravity-term)), and as an option in [row 10](/wiki/predictions/early-universe-step): "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff", with "(Knob-bounded; CMB-S4 probes)" (§13).

Helium measures H at freeze-out, and H depends on G as it does on the radiation content (above). In the wiki's reading, that is why the notebook dates the step "before BBN": a change in G still under way during nucleosynthesis would change the helium abundance. The notebook gives neither the step's size nor its time beyond that phrase. The size is set by M̃, which the notebook lists with k̃ as the two optional parameters of the dual geometric sector (#1 §10). The row's other imprint, a negative ΔN_eff from a closed dual space, is a change in the radiation content, which nucleosynthesis also bounds [T]. No document compares either imprint with nucleosynthesis data, and #11 names a microwave-background experiment, CMB-S4, as the row's probe ([the data situation](/wiki/predictions/early-universe-step#the-data-situation)).

### The ψ relic window's lower edge

Version 3 of the withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) added a light hidden fermion ψ so that the heavy hidden W′± bosons could decay ([what the W′ result forced](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure#what-it-forced)), and took its mass "above the MeV scale, so that psi has annihilated before nucleosynthesis" (#14 §3). A species freezes out when the temperature of its own plasma falls to about a twentieth of its mass ([thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out#why-freeze-out-happens-near-t--m20-t)). In a hidden sector colder than ours that happens while the visible plasma is still hotter. The round-3 referee converted the hidden freeze-out to visible temperatures, with the hidden-to-visible temperature ratio after reheating set at ξ₀ = 0.76 (`review/round3/referee/step4.out`, item 7):

```text
m_psi=1 MeV: hidden freeze-out T_h ~ m/20 = 0.05 MeV at T_vis ~ 0.0806 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
m_psi=3 MeV: hidden freeze-out T_h ~ m/20 = 0.15 MeV at T_vis ~ 0.242 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
m_psi=10 MeV: hidden freeze-out T_h ~ m/20 = 0.5 MeV at T_vis ~ 0.707 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
m_psi=30 MeV: hidden freeze-out T_h ~ m/20 = 1.5 MeV at T_vis ~ 2.12 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
```

For 1, 3 and 10 MeV the hidden freeze-out falls between the two markers of nucleosynthesis; for 30 MeV it falls before them. The referee (`review/round3/referee/audit-notes.md`, Step 4(a) item 8): "hidden freeze-out T_h ~ m/20 occurs at T_vis ~ 0.08 MeV for m_psi = 1 MeV, 0.24 MeV for 3 MeV, 0.71 MeV for 10 MeV (step4.out) - i.e. during BBN. Needs m_psi >~ 20-30 MeV. (Moot: excluded anyway, below.)" [Ruling 6](/wiki/method/review/round-3/rulings#rulings-5-and-6-the-colder-hidden-sector-and-nucleosynthesis), "Accepted, not re-checked", records the finding as "MeV-scale ψ freezes out during BBN", with the evidence "T_f ~ m/20, so the lower mass bound should be ≳ 20–30 MeV."

The finding is that the lower edge did not meet v3's own condition, that ψ finish annihilating before nucleosynthesis. No document computes what a later annihilation of ψ would have done to the light elements. The window is dead, and its upper edge had already failed on a miscount of states ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)); so is the candidate it served ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

### Nucleosynthesis limits on a millicharged ψ

If the hidden and visible photons mix kinetically, ψ carries a visible electric charge of about ε times the electron's and is a millicharged particle (MCP) ([a millicharged ψ](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing#i-a-millicharged-ψ)). Among the constraints #14 had not evaluated, the referee cited Vogel and Redondo, JCAP 02 (2014) 029, arXiv:1311.2600, for a nucleosynthesis limit: "exclude MCPs with m_f < 16 MeV for eps > 1.4e-8" (Step 4(c) item 2). The adjudication accepted "SN1987A and BBN limits on millicharged particles" as a to-do, "not individually re-checked" ([supernova and nucleosynthesis limits](/wiki/method/review/round-3/rulings#supernova-sn1987a-and-nucleosynthesis-limits)). [Decision 1](/wiki/method/review/round-3/decisions#decision-1-strict-sector-separation) then took [sector separation](/wiki/program/postulates/p4-polarized-matter) strictly, "ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry", which closed the millicharge channel.

### Radiation from a light hidden fermion

The v3 worklog, in which ψ was first added, noted that light hidden fermions would also count at nucleosynthesis: "If they are lighter than ~MeV they add ΔN_eff at BBN as well (not yet scripted)" (`review/v3-worklog.md`, 'New open items', O1). The worklog left the point unscripted, and #14 v3 placed ψ above the MeV scale.

### Dilution before nucleosynthesis

Round 3 found the soliton candidate's monopoles overproduced, and the literature it cited has hidden monopoles overclose the universe at high breaking scales "unless diluted, e.g. by early matter domination" (ruling 3, from the abstract of Liveoak, Maharana and Wells). Any such dilution would have had to end before nucleosynthesis [T] ([inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution#early-matter-domination)). [Decision 2](/wiki/method/review/round-3/decisions#decision-2-the-soliton-candidate-retired) rejected that route: with a free dilution factor, "The mass would then no longer be a prediction".

## Standard references

- R. A. Alpher, H. Bethe and G. Gamow, Physical Review (1948) †: element formation in a hot early universe. C. Hayashi (1950) †: the neutron–proton ratio set by weak interactions in the hot plasma.
- P. J. E. Peebles (1966) †; R. V. Wagoner, W. A. Fowler and F. Hoyle (1967) †: the primordial helium abundance and the network calculation of the light-element yields.
- G. Steigman, "Primordial nucleosynthesis in the precision cosmology era", Annual Review of Nuclear and Particle Science (2007) †; R. H. Cyburt, B. D. Fields, K. A. Olive and T.-H. Yeh, "Big bang nucleosynthesis: present status", Reviews of Modern Physics (2016) †: reviews of the theory, the observed abundances and the bounds on the expansion rate.
- E. W. Kolb and M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17], cited there for freeze-out; that it also treats nucleosynthesis is stated here from model memory †.
- Vogel and Redondo, JCAP 02 (2014) 029, arXiv:1311.2600: the nucleosynthesis and microwave-background limits on millicharged particles that the round-3 referee cited (Step 4(c) item 2).

None of the † entries is cited in the program's documents for nucleosynthesis; they are given from model memory and are unverified.

## Used by

- [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step) — the step dated "before BBN".
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — MeV-scale ψ freezing out during nucleosynthesis, ruling 6.
- [Round-3 verdict, rulings and citation audit](/wiki/method/review/round-3/rulings) — ruling 6, and the nucleosynthesis limits among the omitted constraints.
- [Kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) — nucleosynthesis limits on a millicharged ψ.
- [Relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance) — hidden freeze-out timed against nucleosynthesis.
- [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) — light hidden fermions below an MeV would add radiation at nucleosynthesis.
- [Inflation, reheating and entropy dilution](/wiki/cosmology/early-universe/inflation-and-dilution) — dilution by decays that must end before nucleosynthesis.
- [The radiation era: thermal history and N_eff](/wiki/cosmology/early-universe/radiation-era) — the expansion rate and N_eff that helium measures.

## Sources

- `notes/broken-born-theory.md` §6 — the minisuperspace equation and the step "before BBN" [D]; §10 — the optional parameters M̃ and k̃. Quotations are transcribed from its LaTeX.
- `papers/broken-born-checkpoint-v2.md` §10 — "the dual Einstein term is an a⁻⁶ step in G_eff"; §13 row 10 — the row and its probe
- `review/round3/referee/step4.out` item 7 — the hidden freeze-out temperatures and the script's markers of nucleosynthesis
- `review/round3/referee/audit-notes.md` Step 4(a) item 8 — freeze-out "during BBN"; Step 4(c) item 2 — the Vogel–Redondo limits
- `review/round3-adjudication.md` 'Rulings' 6 — accepted, not re-checked; 'Rulings' 3 — dilution by early matter domination; the omitted-constraints list — "SN1987A and BBN limits on millicharged particles"; 'Decisions' 1 and 2 — the millicharge channel closed, the dilution route rejected
- `review/v3-worklog.md` 'New open items' (O1) — light hidden fermions at nucleosynthesis, not scripted
- `notes/knot-dark-matter-standalone.md` §3 — ψ "above the MeV scale, so that psi has annihilated before nucleosynthesis" (withdrawn manuscript)
- `verify/soliton_obituary.py` 'Anchors' — the expansion rate H = 1.66√g\* T²/M_Pl; its constant g\* = 10.75 at neutrino decoupling
