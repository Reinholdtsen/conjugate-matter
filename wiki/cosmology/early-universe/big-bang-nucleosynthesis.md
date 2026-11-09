---
title: "Big Bang nucleosynthesis"
weight: 13
status: established
description: "The formation of the light nuclei in the first minutes: neutron–proton freeze-out, the deuterium bottleneck and helium; what the abundances measure, namely the expansion rate (and through it the radiation content and the strength of gravity) and the baryon density; the limits on light particles, late decays and entropy release; and the program's uses, row 10's G_eff step dated before nucleosynthesis and the ψ relic window of #14's failed soliton model."
provenance: [T]
sources:
  - "notes/broken-born-theory.md §6"
  - "notes/broken-born-theory.md §10"
  - "wiki/papers/broken-born-checkpoint-v2.md §10"
  - "wiki/papers/broken-born-checkpoint-v2.md §13 row 10"
  - "review/round3/referee/step4.out item 7"
  - "review/round3/referee/audit-notes.md Step 4(a) item 8"
  - "review/round3/referee/audit-notes.md Step 4(c) item 2"
  - "review/round3-adjudication.md 'Rulings' 3"
  - "review/round3-adjudication.md 'Rulings' 4"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "review/round3-adjudication.md 'Rulings' (omitted constraints)"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/v3-worklog.md 'New open items'"
  - "notes/knot-dark-matter-standalone.md §3"
  - "verify/soliton_obituary.py 'Anchors'"
  - "review/wiki-build-flags.md item 32"
  - "notes/closed-universe.md §4"
  - "notes/closed-universe.md §7"
  - "review/wiki-build-flags.md items 48, 49"
  - "CLAUDE.md 'Since the handoff'"
---

*Big Bang nucleosynthesis (BBN) is the formation of the lightest atomic nuclei, mostly helium-4 with small amounts of deuterium, helium-3 and lithium-7, in the first minutes of the hot early universe. Its outcome depends on the expansion rate at the time. Neutrons and protons stop converting into each other once the weak interactions that convert them become slower than the expansion, and nearly every neutron left when nuclei can survive ends up in helium, so the primordial helium abundance measures how fast the universe was expanding in its first minutes. That makes nucleosynthesis a test of two things at that time, the radiation content, counted as the [effective number of light species](radiation-era.md#n_eff-counting-light-species-t) N_eff, and the strength of gravity; it also limits particles that decay or release energy during or after it. The program uses this timing in two places. The [lab notebook](../../history/documents/lab-notebook.md) dates an optional step in the effective strength of gravity, G_eff, "before BBN" ([row 10](../../predictions/early-universe-step.md)), and the [round-3 review](../../method/review/round-3/_index.md) found that the light hidden fermion ψ of [#14](../../../notes/knot-dark-matter-standalone.md)'s failed [soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md) would, at MeV masses, still have been [freezing out](../../dark-matter/candidates/thermal-freeze-out.md#freeze-out-in-a-sector-at-its-own-temperature-t) during nucleosynthesis, so the lower edge of its [relic window](../../dark-matter/candidates/soliton-candidate/psi-relic-window.md) was wrong.*

**Status:** Established — [T] — textbook early-universe physics, written here from general knowledge, with the references it adds from model memory (†); no `verify/` script checks it. The expansion rate it rests on, H = 1.66√g\* T²/M_Pl, is an anchor of [`verify/soliton_obituary.py`](../../../verify/soliton_obituary.py) [V] ([the soliton-obituary script](../../method/verification/soliton-obituary-script.md)). The program's uses are the lab notebook's step in G_eff "before BBN" ([#1 §6](../../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary)), which is [D] and not machine-checked, and the round-3 referee's finding, from its own executed code, that MeV-scale ψ would freeze out during nucleosynthesis, which ruling 6 accepted without re-checking.

## The epoch [T]

Nucleosynthesis takes place in [the radiation era](radiation-era.md), when the energy density is dominated by photons, electrons and positrons, and neutrinos, and the temperature T alone fixes the expansion rate ([the expansion rate](radiation-era.md#the-expansion-rate-t)):

```text
H = 1.66 √g* T²/M_Pl ∝ √(g* G) T²
```

Here g\* counts the relativistic degrees of freedom, M_Pl = G^{−1/2} is the [Planck mass](../../gravity/spin-2-fields/planck-units.md), and G is Newton's constant. At neutron–proton freeze-out (below) g\* is close to 10.75, the value [`verify/soliton_obituary.py`](../../../verify/soliton_obituary.py) takes at neutrino decoupling, which counts photons, electrons and positrons, and three neutrino species [T]. Protons and neutrons are a small admixture, far outnumbered by photons. Their number per photon, the baryon-to-photon ratio n_b/n_γ, is the one free parameter of standard nucleosynthesis [T].

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

A faster expansion, whether from more radiation or from a larger G, therefore freezes the ratio earlier, at a higher temperature, and leaves more neutrons [T]. The neutrinos are held in contact with the plasma by weak scattering and annihilation with electrons and positrons, at a rate of the same form, and decouple at about the same time [T]. The round-3 referee's script marks this stage at "n/p freeze-out ~0.8 MeV" of visible temperature ([`review/round3/referee/step4.out`](../../../review/round3/referee/step4.out), item 7).

### Neutron decay and the deuterium bottleneck

After freeze-out the free neutrons decay, n → p + e⁻ + ν̄_e, and the ratio keeps falling until the neutrons are bound into nuclei [T]. The first step is deuterium, p + n → D + γ. The deuteron is weakly bound, and because photons outnumber baryons so heavily, the high-energy tail of the photon distribution breaks deuterons apart as fast as they form until the temperature has fallen well below the deuteron's binding energy [T]. This delay is the deuterium bottleneck. The referee's script marks its end at "BBN D-formation ~0.07 MeV" (`step4.out`, item 7). In the wiki's reading, the round-3 record takes nucleosynthesis to run between these two markers ([the lower edge of the ψ window](../../dark-matter/candidates/soliton-candidate/psi-relic-window.md#the-lower-edge-freeze-out-during-nucleosynthesis)).

### Helium and the traces

Once deuterium survives, nuclear reactions carry it on quickly to helium-4, the most tightly bound of the light nuclei, and nearly every remaining neutron ends up there [T]. A helium-4 nucleus holds two neutrons and two protons, so the fraction of the baryon mass in helium is

```text
Y_p ≈ 2(n/p)/(1 + n/p)        n/p taken when deuterium forms
```

Y_p is the conventional symbol for the primordial helium mass fraction; it is not the [yield Y = n/s](relic-yield-and-dilution.md#the-yield-t) of relic abundances. Heavier nuclei barely form: no stable nucleus has five or eight nucleons, so the chain stalls at helium-4, and by the time helium has formed, the falling temperature and density make further fusion slow [T]. What remains besides hydrogen and helium-4 is small amounts of unburnt deuterium and helium-3, and traces of lithium-7 [T].

## What the abundances measure [T]

### The expansion rate: radiation and gravity together

Helium measures the expansion rate at freeze-out, and that rate depends on the radiation content and on G only through the product g\*G. With H′ the changed rate and H the standard one at the same temperature [T]:

```text
(H′/H)² = [g* + (7/4)·ΔN_eff] / g*        extra light species, standard G
(H′/H)² = G′/G                             a different G, standard radiation
```

The first line uses the counting of [the radiation era](radiation-era.md#extra-species-δn_eff): one extra neutrino species at the neutrino temperature, which at freeze-out equals the photon temperature, adds 7/4 to g\* and 1 to N_eff, the normalization that [`verify/soliton_obituary.py`](../../../verify/soliton_obituary.py) checks as an anchor. A measured helium abundance therefore bounds ΔN_eff during nucleosynthesis if G is assumed standard, or the departure of G from its present value if the radiation content is assumed standard; on its own it cannot tell the two apart [T]. A slower expansion, from fewer light species or a weaker G, lowers the helium fraction, and a faster one raises it [T].

### The baryon density

Deuterium is burnt more completely into helium when there are more baryons, so its abundance falls steeply as n_b/n_γ rises, and among the light elements it gives the most precise measure of the baryon density [T]. The helium fraction depends on n_b/n_γ only weakly, through the time at which the bottleneck ends [T]. [The cosmic microwave background](cosmic-microwave-background.md) (CMB), released much later, measures the baryon density independently, from the heights of its acoustic peaks. For deuterium and helium the two agree, which tests the standard account of the time between the first minutes and recombination [T]. Lithium-7 is the exception: the abundance predicted for the CMB's baryon density is higher than the abundance measured in the atmospheres of old stars, a long-standing discrepancy called the lithium problem, whose resolution is not settled [T].

### Light particles, decays and entropy release

The abundances also limit anything that changes the plasma during or after nucleosynthesis [T].

- **Light particles.** A particle with a mass near the MeV scale that is in equilibrium during nucleosynthesis adds to the radiation density while it is relativistic, and when it annihilates it heats the particles it is in contact with, which changes both the expansion rate and the final N_eff [T]. A hidden sector at its own temperature counts in the same way, weighted by the fourth power of its temperature relative to ours ([a hidden sector at its own temperature](hidden-sector-temperature.md)).
- **Decays.** A long-lived particle that decays during or after nucleosynthesis injects energetic photons or hadrons, which can break up deuterium and helium-4 or make other light nuclei, and its products change n_b/n_γ and the radiation content [T]. The observed abundances bound the amount and the lifetime of such particles [T].
- **Entropy release.** A period of early matter domination that ends in decays dilutes everything made before it ([early matter domination](relic-yield-and-dilution.md#early-matter-domination)). The decays must be over, and the expansion back to the standard radiation-dominated form, before nucleosynthesis begins [T].

## Nucleosynthesis and the microwave background [T]

Both measure N_eff, at two epochs: helium in the first minutes, the CMB at recombination ([how N_eff is measured](radiation-era.md#how-n_eff-is-measured-t)). Agreement between the two values, and between the two baryon densities, limits radiation or entropy added between the epochs [T]. The two measurements are also linked inside a CMB fit: helium sets the number of free electrons before recombination and so affects the damping of the CMB anisotropies, and CMB analyses commonly take the helium fraction that nucleosynthesis predicts for the fitted baryon density ([N_eff in the microwave background](cosmic-microwave-background.md#n_eff)) [T].

## How the program uses it

### Row 10: a step in G_eff "before BBN"

The lab notebook adds the dual sector's gravitational term to the minisuperspace form of the Friedmann equation ([#1 §6](../../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary), [D]):

```text
3H²(M_P² + M̃² a⁻⁶) = ρ
```

with M_P the Planck mass in a convention the notebook does not state, which the wiki reads as the reduced one ([where a document states no convention](../../gravity/spin-2-fields/planck-units.md#where-a-document-states-no-convention)), and M̃ the dual Planck mass ([the program's extension of Friedmann cosmology](../scale-factor-duality/friedmann-cosmology.md#the-programs-extension-a-second-scale-factor)). The notebook calls the new term "a stiff-like (a⁻⁶) modification of the effective Planck mass, relevant only at early times", and concludes: "It predicts a step in G_eff before BBN and, conditionally on its one knob, a spectral step in the primordial gravitational-wave background" (transcribed from its LaTeX). [Checkpoint #11](../../history/documents/checkpoint.md) keeps the step in one clause, "the dual Einstein term is an a⁻⁶ step in G_eff" ([§10](../../papers/broken-born-checkpoint-v2.md#10-cosmology); [the dual gravity term](../scale-factor-duality/duality-dictionary.md#the-dual-gravity-term)), and as an option in [row 10](../../predictions/early-universe-step.md): "Optional a⁻⁶ G_eff step; closed dual curvature ⇒ negative ΔN_eff", with "(Knob-bounded; CMB-S4 probes)" ([§13](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions)). The dual Einstein–Hilbert term behind the a⁻⁶ step is used in [#1 §6](../../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary) under a [D] tag but derived from the geometric action in no document, so the step tests a postulate (flag 49 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [the dual frame](../scale-factor-duality/closed-universe.md#the-dual-frame-what-closure-fixes-and-what-it-does-not)).

Helium measures H at freeze-out, and H depends on G as it does on the radiation content (above). In the wiki's reading, that is why the notebook dates the step "before BBN": a change in G still under way during nucleosynthesis would change the helium abundance. The notebook gives neither the step's size nor its time beyond that phrase. M̃, the term's only parameter, is free; the notebook lists it with k̃, which the wiki reads as the dual curvature, as the two optional parameters of the dual geometric sector ([#1 §10](../../../notes/broken-born-theory.md#10-parameter-count)). The row's other imprint, a negative ΔN_eff from a closed dual space, acts as a change in the radiation content, which nucleosynthesis also bounds [T]. The closed-universe note of 2026-10-27 (computed, not reviewed) finds that a closed universe does not supply a closed dual space: under the slaved block g̃ = g⁻¹ the momentum fibre is flat, k̃ = 0, for any X, so a negative ΔN_eff needs a separate postulate of a curved, compact momentum space, which no document states (flag 48 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md); [a closed Comatter universe](../scale-factor-duality/closed-universe.md#shape-the-momentum-fibre-stays-flat-dv)). No document compares either imprint with nucleosynthesis data ([the data situation](../../predictions/early-universe-step.md#the-data-situation)), and [#11](../../papers/broken-born-checkpoint-v2.md) names a microwave-background experiment, CMB-S4, as the row's probe; whether CMB-S4 is still going ahead is unchecked (flag 32 in [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md)).

### The ψ relic window's lower edge

Version 3 of the withdrawn manuscript [#14](../../dark-matter/candidates/soliton-candidate/_index.md) added a light hidden fermion ψ so that the heavy hidden W′± bosons could decay ([what the W′ result forced](../../dark-matter/candidates/soliton-candidate/w-prime-overclosure.md#what-it-forced)), and took its mass "above the MeV scale, so that psi has annihilated before nucleosynthesis" ([#14 §3](../../../notes/knot-dark-matter-standalone.md#3-the-candidate)). A species freezes out when the temperature of its own plasma falls to about a twentieth of its mass [T] ([thermal freeze-out](../../dark-matter/candidates/thermal-freeze-out.md#why-freeze-out-happens-near-t--m20-t)). In a hidden sector colder than ours, that happens while the visible plasma is still hotter. The round-3 referee converted the hidden freeze-out to visible temperatures, with the hidden-to-visible temperature ratio after reheating set at ξ₀ = 0.76 ([`review/round3/referee/step4.out`](../../../review/round3/referee/step4.out), item 7):

```text
m_psi=1 MeV: hidden freeze-out T_h ~ m/20 = 0.05 MeV at T_vis ~ 0.0806 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
m_psi=3 MeV: hidden freeze-out T_h ~ m/20 = 0.15 MeV at T_vis ~ 0.242 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
m_psi=10 MeV: hidden freeze-out T_h ~ m/20 = 0.5 MeV at T_vis ~ 0.707 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
m_psi=30 MeV: hidden freeze-out T_h ~ m/20 = 1.5 MeV at T_vis ~ 2.12 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
```

For 1, 3 and 10 MeV the hidden freeze-out falls between the two markers of nucleosynthesis; for 30 MeV it falls before them. The referee ([`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md), Step 4(a) item 8): "hidden freeze-out T_h ~ m/20 occurs at T_vis ~ 0.08 MeV for m_psi = 1 MeV, 0.24 MeV for 3 MeV, 0.71 MeV for 10 MeV (step4.out) - i.e. during BBN. Needs m_psi >~ 20-30 MeV. (Moot: excluded anyway, below.)" [Ruling 6](../../method/review/round-3/rulings.md#rulings-5-and-6-the-colder-hidden-sector-and-nucleosynthesis), "Accepted, not re-checked", records the finding as "MeV-scale ψ freezes out during BBN", with the evidence "T_f ~ m/20, so the lower mass bound should be ≳ 20–30 MeV."

The finding is that the lower edge did not meet v3's own condition, that ψ finish annihilating before nucleosynthesis. No document computes what a later annihilation of ψ would have done to the light elements. The window is under review; its upper edge failed independently, on a miscount of states and a bracketed cross-section (ruling 4; [Under review: the ψ relic window](../../dark-matter/candidates/soliton-candidate/psi-relic-window.md)). The model it served, built with ordinary kinematics, failed on its recomputed abundance ([Obituary: #14's superheavy-soliton model](../../dark-matter/candidates/soliton-candidate/obituary.md)); the candidate it modeled, conjugate monopoles localized in momentum, is P.R.'s open conjecture ([Conjecture: magnetic monopoles abundant in momentum space](../../dark-matter/candidates/momentum-space-monopoles.md)).

### Nucleosynthesis limits on a millicharged ψ

If the hidden and visible photons mix kinetically, with mixing parameter ε, ψ carries a visible electric charge of about ε times the electron's and is a millicharged particle (MCP) ([a millicharged ψ](../../dark-matter/candidates/soliton-candidate/kinetic-mixing.md#i-a-millicharged-ψ)). Among the constraints #14 had not evaluated, the referee cited Vogel and Redondo, JCAP 02 (2014) 029, [arXiv:1311.2600](https://arxiv.org/abs/1311.2600), for a nucleosynthesis limit: "exclude MCPs with m_f < 16 MeV for eps > 1.4e-8" (Step 4(c) item 2). The adjudication accepted "SN1987A and BBN limits on millicharged particles" as a to-do, "not individually re-checked" ([supernova and nucleosynthesis limits](../../method/review/round-3/rulings.md#supernova-sn1987a-and-nucleosynthesis-limits)). [Decision 1](../../method/review/round-3/decisions.md#decision-1-strict-sector-separation) then took [sector separation](../../program/postulates/p4-polarized-matter.md) strictly, "ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry", which closed the millicharge channel.

### Radiation from a light hidden fermion

The v3 worklog, in which ψ was first added, noted that light hidden fermions would also count at nucleosynthesis: "If they are lighter than ~MeV they add ΔN_eff at BBN as well (not yet scripted)" ([`review/v3-worklog.md`](../../../review/v3-worklog.md), 'New open items', O1). The worklog left the point unscripted, and #14 v3 placed ψ above the MeV scale.

### Dilution before nucleosynthesis

Round 3 found the monopoles of #14's model overproduced, and the literature it cited has hidden monopoles overclose the universe at high breaking scales "unless diluted, e.g. by early matter domination" (ruling 3, from the abstract of Liveoak, Maharana and Wells). Any such dilution would have had to end before nucleosynthesis [T] ([the relic yield Y = n/s and entropy dilution](relic-yield-and-dilution.md#conditions)). [Decision 2](../../method/review/round-3/decisions.md#decision-2-14s-model-retired) rejected that route: with a free dilution factor, "The mass would then no longer be a prediction".

## Standard references

- R. A. Alpher, H. Bethe and G. Gamow, Physical Review (1948) †: element formation in a hot early universe. C. Hayashi (1950) †: the neutron–proton ratio set by weak interactions in the hot plasma.
- P. J. E. Peebles (1966) †; R. V. Wagoner, W. A. Fowler and F. Hoyle (1967) †: the primordial helium abundance and the network calculation of the light-element yields.
- G. Steigman, "Primordial nucleosynthesis in the precision cosmology era", Annual Review of Nuclear and Particle Science (2007) †; R. H. Cyburt, B. D. Fields, K. A. Olive and T.-H. Yeh, "Big bang nucleosynthesis: present status", Reviews of Modern Physics (2016) †: reviews of the theory, the observed abundances and the bounds on the expansion rate.
- E. W. Kolb and M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14's reference [17], cited there for freeze-out; that it also treats nucleosynthesis is stated here from model memory †.
- Vogel and Redondo, JCAP 02 (2014) 029, [arXiv:1311.2600](https://arxiv.org/abs/1311.2600): the nucleosynthesis and microwave-background limits on millicharged particles that the round-3 referee cited (Step 4(c) item 2).

None of the † entries is cited in the program's documents for nucleosynthesis; they are given from model memory and are unverified.

## Used by

- [Row 10: an early step in G_eff](../../predictions/early-universe-step.md) — the step dated "before BBN".
- [Under review: the ψ relic window](../../dark-matter/candidates/soliton-candidate/psi-relic-window.md) — MeV-scale ψ freezing out during nucleosynthesis, ruling 6.
- [Round-3 verdict, rulings and citation audit](../../method/review/round-3/rulings.md) — ruling 6, and the nucleosynthesis limits among the omitted constraints.
- [Kinetic mixing between sectors](../../dark-matter/candidates/soliton-candidate/kinetic-mixing.md) — nucleosynthesis limits on a millicharged ψ.
- [Relic abundance mechanisms](../../dark-matter/candidates/relic-abundance.md) — hidden freeze-out timed against nucleosynthesis.
- [W′ overclosure: the minimal sector is excluded](../../dark-matter/candidates/soliton-candidate/w-prime-overclosure.md) — light hidden fermions below an MeV would add radiation at nucleosynthesis.
- [Inflation, reheating and entropy dilution](inflation-and-dilution.md) — dilution by decays that must end before nucleosynthesis.
- [The radiation era: thermal history and N_eff](radiation-era.md) — the expansion rate and N_eff that helium measures.

## Sources

- [`wiki/papers/broken-born-checkpoint-v2.md` §10](../../papers/broken-born-checkpoint-v2.md#10-cosmology) — "the dual Einstein term is an a⁻⁶ step in G_eff"; [§13 row 10](../../papers/broken-born-checkpoint-v2.md#13-predictions-and-kill-conditions) — the row and its probe
- [`review/round3-adjudication.md`](../../../review/round3-adjudication.md) 'Rulings' 6 — accepted, not re-checked; 'Rulings' 4 — the upper edge's miscount; 'Rulings' 3 — dilution by early matter domination; the omitted-constraints list — "SN1987A and BBN limits on millicharged particles"; 'Decisions' 1 and 2 — the millicharge channel closed, the dilution route rejected
- [`verify/soliton_obituary.py`](../../../verify/soliton_obituary.py) 'Anchors' — the expansion rate H = 1.66√g\* T²/M_Pl and the one-species normalization of ΔN_eff (7/4); its constant 10.75 for g\* at neutrino decoupling
- [`review/round3/referee/audit-notes.md`](../../../review/round3/referee/audit-notes.md) Step 4(a) item 8 — freeze-out "during BBN"; Step 4(c) item 2 — the Vogel–Redondo limits
- [`review/round3/referee/step4.out`](../../../review/round3/referee/step4.out) item 7 — the hidden freeze-out temperatures and the script's markers of nucleosynthesis
- [`review/v3-worklog.md`](../../../review/v3-worklog.md) 'New open items' (O1) — light hidden fermions at nucleosynthesis, not scripted
- [`notes/broken-born-theory.md` §6](../../../notes/broken-born-theory.md#6-cosmology-i-the-constraint-and-the-corrected-dictionary) — the minisuperspace equation and the step "before BBN" [D]; [§10](../../../notes/broken-born-theory.md#10-parameter-count) — the optional parameters M̃ and k̃. Quotations are transcribed from its LaTeX.
- [`notes/knot-dark-matter-standalone.md` §3](../../../notes/knot-dark-matter-standalone.md#3-the-candidate) — ψ "above the MeV scale, so that psi has annihilated before nucleosynthesis" (withdrawn manuscript)
- [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) item 32 — CMB-S4's status, unchecked
- [`notes/closed-universe.md` §4](../../../notes/closed-universe.md#4-how-small-momentum-space-gets), [§7](../../../notes/closed-universe.md#7-the-dual-frame-what-closure-fixes-and-what-it-does-not); [`review/wiki-build-flags.md`](../../../review/wiki-build-flags.md) items 48 and 49 — a closed universe leaves the momentum fibre flat, and the dual Einstein–Hilbert term behind the a⁻⁶ step is not derived
- [`CLAUDE.md`](../../../CLAUDE.md) 'Since the handoff' — the ψ relic window under review
