---
title: "Obituary: the ψ relic window"
weight: 90
status: dead
description: "v3 omitted ψ̄ and the second doublet member and bracketed an exact cross-section by ×10; the recount puts 10% of the dark matter at 45–49 GeV and all of it at 146–158 GeV, and MeV-scale ψ would freeze out during nucleosynthesis."
provenance: [V]
sources:
  - "review/round3-adjudication.md 'Rulings' 4"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "review/round3-adjudication.md 'Rulings' 13"
  - "review/round3-adjudication.md 'Pre-registration scored'"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "verify/soliton_obituary.py"
  - "review/round3/adjudicator/round3_arb.out"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/step2c_psi.out"
  - "review/round3/referee/step2c_thr.out"
  - "review/round3/referee/step4.out"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/v3-worklog.md 'New open items'"
  - "notes/knot-dark-matter-standalone.md banner"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md §6"
---

*The ψ relic window was the range of masses #14 v3 allowed for ψ, the light hidden fermion it added so that the heavy hidden W′± bosons could decay. ψ is itself stable and left over from the early universe, so its mass sets how much of the [dark matter](/wiki/dark-matter) it makes up: v3 wanted ψ light enough to be a minor component, so that the monopoles dominate, and heavy enough to have annihilated before [nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis). The round-3 review found both edges wrong. The upper edge was too high because v3 had left out the antiparticle and the second member of the doublet, a factor of 4, and had bracketed an exactly known annihilation cross-section over a factor of ten; the lower edge was too low because MeV-scale ψ would still be [freezing out](/wiki/dark-matter/candidates/thermal-freeze-out#freeze-out-in-a-sector-at-its-own-temperature-t) during nucleosynthesis. The window died with these corrections, and the candidate it served was retired.*

**Status:** Dead — round-3 ruling 4, upheld; the recount is [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). Ruling 6, on the lower edge, was "Accepted, not re-checked". Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); rulings in [round-3 verdict and rulings](/wiki/method/review/round-3/rulings); listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

### Why ψ existed

The minimal hidden sector of the withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate), SU(2)_d broken to U(1)_d by an adjoint scalar, is excluded by its own stable charged bosons, which would overclose the universe ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)). v3's repair was a light fermion for them to decay into (§3): "The fix is the Dirac doublet psi: W'+ can decay to a psi pair." #14 §2 describes it: "The sector also contains at least one Dirac fermion psi in the doublet, with U(1)_d charges +-g_d/2 (Sec. 3 shows it is required)" ([Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)).

Being the lightest hidden-charged particle, ψ is in turn stable, and it is a thermal relic of the hidden plasma (§3): "psi is then itself stable by U(1)_d charge and freezes out by annihilating to hidden photons." Under the coupling hypothesis H, ψ's charge g_d/2 equals the electron's, so it annihilates with the strength of ordinary electromagnetism, α ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)). How much ψ survives freeze-out depends on its mass: the annihilation cross-section falls as the mass rises, so a heavier ψ leaves more behind [T] ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)).

### The window

#14 §3 turned this into a mass window with two edges:

> Under H, psi makes up less than 10% of the dark matter for m_psi below 0.1-0.3 TeV, and all of it at 0.3-1 TeV. We take m_psi below about 0.1 TeV, so that the monopoles dominate, and above the MeV scale, so that psi has annihilated before nucleosynthesis.

- **The upper edge** keeps ψ a minor component, so that the monopoles remain the dark matter.
- **The lower edge** has ψ finish annihilating before Big Bang nucleosynthesis (BBN), the formation of the light nuclei in the first minutes [T].

The window became the first of v3's "Requirements forced by consistency (not optional)": "(i) at least one hidden doublet fermion with mass between the MeV scale and ~0.1 TeV" (§6), and §6 lists "the failure of the adjoint-only model and the psi relic window" among the results "Derived within the framework or by standard methods". It also set the test v3 called the most direct: exclusion condition 3, "Exclusion of the millicharged psi window: m_psi from the MeV scale to ~0.1 TeV at visible charge ~ (1e-7 to 1e-6) e" (§5), for a ψ that carries a small visible charge through [kinetic mixing](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing) (§4).

The numbers came from the v3 worklog's item O1: "With α_e,d = α it would be all of the dark matter at 0.3–1.0 TeV, and 10% of it at 0.1–0.3 TeV. So it must be lighter than roughly 100–300 GeV to stay subdominant" (`review/v3-worklog.md`, 'New open items').

## How it was tested

[Round 3](/wiki/method/review/round-3) checked the window twice, independently.

- **The referee** wrote its own relic code, validated it on a standard relic ("standard 100 GeV WIMP 2.2e-26 -> Omega h^2 = 0.1145", where a WIMP is a weakly interacting massive particle), and integrated ψ's freeze-out with the hidden sector's own temperature, starting from a hidden-to-visible temperature ratio ξ₀ (`review/round3/referee/audit-notes.md`, Step 2; `step2c_thr.out`).
- **The adjudicator** recounted with the s-wave freeze-out formula in an arbitration script and put the corrected count into [the gate](/wiki/method/verification/the-gate) (`review/round3/adjudicator/round3_arb.out`; [round-3 arbitration](/wiki/method/review/round-3/arbitration)).

## Why it failed

### The upper edge: a miscount of states and an exact cross-section

Ruling 4, upheld, on the share of the dark matter (DM) that ψ makes up:

> v3 omitted ψ̄ and the second doublet member (a factor of 4), and bracketed an exactly known s-wave σv up to ×10. My recount: 10% of the DM at 45–49 GeV, 100% at 146–158 GeV. The referee's Boltzmann integration gives 28–46 / 96–153 GeV. We agree to within ×1.6, and v3's 0.1–0.3 TeV was wrong.

Two separate errors are named.

- **The count of states.** A Dirac fermion has a distinct antiparticle, ψ̄, and a doublet has two members; each of the four freezes out and survives as a relic [T]. v3 counted one. The script counts all four: it multiplies the relic of one species (two spin states) by 4, with the heading "psi, psi-bar, both doublet members; sigma v = pi alpha^2/m^2". Four times the relic at a given mass means the same share of the dark matter is reached at a lower mass.
- **The cross-section.** For a Dirac fermion annihilating into two massless gauge bosons, the low-velocity (s-wave) cross-section is known exactly at leading order, σv = πα²/m², the same as for an electron and positron annihilating into two photons [T]. v3 bracketed it "up to ×10" instead of using it.

The arbitration run shows the two countings side by side, at two values of g\*, the number of [relativistic degrees of freedom](/wiki/cosmology/early-universe/radiation-era) at freeze-out (`review/round3/adjudicator/round3_arb.out`):

```text
g*= 80.00 v3 counting                      : 100% at    297 GeV, 10% at    92 GeV
g*= 80.00 psi+psibar, two doublet members  : 100% at    146 GeV, 10% at    45 GeV
g*=106.75 v3 counting                      : 100% at    321 GeV, 10% at    99 GeV
g*=106.75 psi+psibar, two doublet members  : 100% at    158 GeV, 10% at    49 GeV
```

With the exact σv, the "v3 counting" rows land near the lower ends of v3's ranges, "0.1-0.3 TeV" and "0.3-1 TeV". The corrected rows are the gated values:

```text
PASS  10% of the dark matter at 45-49 GeV  [45.2-48.8]
PASS  100% at 146-158 GeV  [146.4-158.0]
```

### The referee's numbers

The referee's integration depends on the starting temperature ratio ξ₀ (audit notes, Step 2; `step2c_thr.out`):

| ξ₀ | ψ = 10% of the dark matter | ψ = all of it |
| --- | --- | --- |
| 1 | 28.3 GeV | 96.3 GeV |
| 0.76 | 34.9 GeV | 117.8 GeV |
| 0.5 | 45.9 GeV | 153.4 GeV |

Its verdict on v3: "DISCREPANT (factor 3-10 in mass)". The two calculations agree to within ×1.6 (ruling 4), and both put v3's window too high. The record carries the adjudicator's numbers, which the gate checks ([conflicts between sources](/wiki/history/documents/source-conflicts)).

### At the colder sector v3 itself required

v3 required the hidden sector to be colder than ours, ξ < 0.77, because of dark radiation, but computed ψ's relic at equal temperatures ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)). At ξ₀ = 0.76 the referee's code gives ψ's share of the dark matter as (`step2c_psi.out`):

```text
xi0=0.76: m=30: 7.5%; m=100: 73.1%; m=200: 275.2%; m=300: 600.8%; m=600: 2314.0%; m=1000: 6302.9%
```

So at the temperature ratio v3 required, the upper part of its chosen range did not keep ψ a minor component: "the manuscript's "below about 0.1 TeV" would make psi ~70-100% of DM (step2c_psi.out: 73.1% at 100 GeV, xi0=0.76)" (Step 4(a) item 4).

### The lower edge: freeze-out during nucleosynthesis

v3 put the lower edge at "the MeV scale, so that psi has annihilated before nucleosynthesis". A species freezes out when the temperature of its own plasma falls to about a twentieth of its mass [T]. In a colder hidden sector that happens when the visible plasma is still hotter. The referee's script (`step4.out`, item 7, at ξ₀ = 0.76) gives:

```text
m_psi=1 MeV: hidden freeze-out T_h ~ m/20 = 0.05 MeV at T_vis ~ 0.0806 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
m_psi=3 MeV: hidden freeze-out T_h ~ m/20 = 0.15 MeV at T_vis ~ 0.242 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
m_psi=10 MeV: hidden freeze-out T_h ~ m/20 = 0.5 MeV at T_vis ~ 0.707 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
m_psi=30 MeV: hidden freeze-out T_h ~ m/20 = 1.5 MeV at T_vis ~ 2.12 MeV (BBN D-formation ~0.07 MeV; n/p freeze-out ~0.8 MeV)
```

Nucleosynthesis runs between the freeze-out of the neutron-to-proton ratio and the formation of deuterium [T], which the script marks at about 0.8 MeV and 0.07 MeV of visible temperature. For ψ masses of 1, 3 and 10 MeV the hidden freeze-out falls inside that interval; at 30 MeV it falls before it. The referee (Step 4(a) item 8): "hidden freeze-out T_h ~ m/20 occurs at T_vis ~ 0.08 MeV for m_psi = 1 MeV, 0.24 MeV for 3 MeV, 0.71 MeV for 10 MeV (step4.out) - i.e. during BBN. Needs m_psi >~ 20-30 MeV. (Moot: excluded anyway, below.)" The "below" points, in the wiki's reading, to Step 4(c), where the supernova limit on a millicharged particle covers this mass range.

Ruling 6, "Accepted, not re-checked": "T_f ~ m/20, so the lower mass bound should be ≳ 20–30 MeV."

## Channels that became moot

#14 left the bounds on a millicharged ψ open: "Bounds on millicharged particles in this mass and charge range have not been evaluated here. They are the most direct near-term test of the proposal (exclusion condition 3)" (§4). The round-3 [pre-registration](/wiki/method/review/round-3/preregistration) had named them its first runner-up weakest link: "The unevaluated millicharge bounds on ψ at ε ~ 10⁻⁷–10⁻⁶, MeV–0.1 TeV. They might already exclude part of the window." The referee listed the constraints from the literature (Step 4(c) items 2–5):

- **Supernova cooling.** Chang–Essig–McDermott, arXiv:1803.00993: "For a millicharged particle, we exclude charges between 1e-9 - few x 1e-6 ... for masses <~ 200 MeV" — the referee notes that this "covers the whole stated charge range for m_psi = 1-200 MeV".
- **[Cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background#limits-on-the-retired-candidates-light-fermion) and nucleosynthesis.** Vogel–Redondo, arXiv:1311.2600, a Planck-2013-era analysis, which disfavors millicharged particles "between 14 MeV < m_f < 390 MeV for a wide range of minicharges eps > 1e-7" and from nucleosynthesis excludes those "with m_f < 16 MeV for eps > 1.4e-8".
- **Charged subcomponents of the dark matter.** Bounds from Stebbins–Krnjaic and, from recombination, McDermott–Yu–Zurek; and the cosmic-microwave-background limits on dark matter that scatters off baryons, which "vanish below 0.4% interacting fraction (Boddy et al. 1808.00001); psi up to 10% is not automatically safe".
- **Dark acoustic oscillations.** ψ stays coupled to the bath of hidden photons until late ("For sub-GeV psi this approaches recombination"), and Cyr-Racine et al. limit the fraction of the dark matter that can interact very strongly with dark radiation to at most about 5%.
- **Re-thermalization.** At ε = 10⁻⁶, freeze-in from the Standard Model plasma brings ψ into equilibrium for all masses up to 30 GeV, which undoes the colder hidden sector (Step 4(a) item 5; [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)).

The adjudication accepted the list as a to-do without re-checking it ([omitted constraints](/wiki/method/review/round-3/rulings#omitted-constraints)): "Re-thermalization by ψ at ε ~ 1e-7–1e-6", "SN1987A and BBN limits on millicharged particles", "Charged-subcomponent and CMB bounds" (CMB is the cosmic microwave background) and "Dark acoustic oscillations". Decision 1 then took [sector separation](/wiki/program/postulates/p4-polarized-matter) strictly, which "closes three failure channels at once: ψ millicharge, the monopoles' Witten-effect charge (ruling 9), and re-thermalization of the hidden sector" ([round-3 decisions](/wiki/method/review/round-3/decisions); [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing); [Obituary: Planck-suppressed adjoint mixing](/wiki/dark-matter/candidates/soliton-candidate/dimension-five-operator); [the Witten effect](/wiki/electric-magnetic-duality/monopoles/witten-effect#closed-by-strict-sector-separation)). #14 had anticipated this route: exclusion condition 3 "lapses if hidden charge conjugation is shown to be a gauged symmetry, which sets epsilon = 0" (§5). The window died first, on the counting.

## Verdict and what survives

The window is dead. The withdrawal banner of #14 lists it among the casualties of round 3: "So the mass band, the benchmark's "no dilution required" and the ψ relic window are wrong." The round-3 adjudication scored it as one of the numerical indictments the pre-registration had not expected: "Three survive (p; the ψ window; ξ), plus the ε coefficient", with the comment "All are wrong inputs or model choices in my scripts, not arithmetic slips."

v3 had stated that "All numerical statements in Secs. 2-4 were computed by executed code rather than by hand" (§6). The referee: "the p error (a dropped prefactor of 4576) and the psi window (factor 3-10 in mass) indicate otherwise or a coding error" (Step 4(a) item 9). Ruling 13 upheld the point in substance: "The code checked the arithmetic of a wrong model." The miscount of states passed a gate that tested only arithmetic ([verification checks arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

No source lists anything of the window among the survivors of v3. The recount stays in the gate as arithmetic of a retired model [V], and the W′ result that made ψ necessary survives on its own page. Nothing of the window survives, and the candidate it served is dead ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## Sources

- `review/round3-adjudication.md` 'Rulings' 4 and 6 — the recount and the lower edge; 'Rulings' 13 — code checked the arithmetic of a wrong model; 'Pre-registration scored' — the ψ window among the indictments; 'Decisions' 1 — the channels closed
- `verify/soliton_obituary.py` — the gated recount
- `review/round3/adjudicator/round3_arb.out` — both countings side by side
- `review/round3/referee/audit-notes.md` Step 2 — the referee's integration and validation; Step 4(a) items 4, 5, 8 and 9 — the colder sector, re-thermalization, freeze-out during nucleosynthesis, and the claim of executed code; Step 4(c) items 2–5 — the omitted constraints
- `review/round3/referee/step2c_thr.out`, `review/round3/referee/step2c_psi.out`, `review/round3/referee/step4.out` — the referee's outputs quoted here
- `review/round3-preregistration.md` 'Predictions' — the millicharge runner-up
- `review/v3-worklog.md` 'New open items' (O1) — where the window came from
- `notes/knot-dark-matter-standalone.md` banner — the withdrawal; §2 — ψ's charges; §3 — the window; §4 — the unevaluated millicharge bounds; §5 — exclusion condition 3; §6 — requirement (i) and the claim of executed code
