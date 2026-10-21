---
title: "Relic abundance mechanisms"
weight: 10
status: established
description: "How a dark-matter density is set: thermal freeze-out, cannibal and asymmetric dark matter, freeze-in, and the Sakharov conditions for baryogenesis."
provenance: [T]
sources:
  - "verify/soliton_obituary.py"
  - "review/round3-adjudication.md 'Rulings' 4"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/v3-worklog.md 'New open items'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §8"
  - "notes/debt3b-wave-island.md 'Bonus: the relic debt closes itself'"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md 'References'"
---

*A relic abundance is the amount of a particle species left over from the hot early universe, and a relic-abundance mechanism is the process that sets that amount. In thermal freeze-out, particles annihilate in equilibrium with the hot plasma until the expansion of the universe outruns their annihilation, after which their number per unit volume only dilutes; the weaker the annihilation, the more survive. Other mechanisms set the amount differently: by an excess of particles over antiparticles, as for the baryons of ordinary matter; by slow production that never reaches equilibrium (freeze-in); or, in a sector whose particles can only annihilate among themselves, by number-changing self-interactions that turn rest mass into heat (cannibal dark matter). The program uses this standard physics to argue that [conjugate matter χ](/wiki/dark-matter/conjugate-matter) cannot get its abundance from freeze-out, and the round-3 review used it to compute the relics of [the retired soliton candidate](/wiki/dark-matter/candidates/soliton-candidate)'s hidden sector.*

**Status:** Established — standard early-universe physics [T], explained here from general knowledge; references the wiki adds are from model memory (†). The program's applications carry their own tags. `verify/soliton_obituary.py` checks its freeze-out code against a standard relic before using it ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).

## What is being set

The density of a species today is quoted as a fraction Ω of the critical density, the density of a spatially flat universe at the present expansion rate [T]. Early-universe calculations predict the product Ω h², where h is the present Hubble rate in a conventional unit: Ω h² is proportional to the physical density itself and does not depend on the measured value of h [T]. The target for dark matter, as the withdrawn manuscript #14 states it, is "Omega h^2 ~ 0.12, with mean rho_DM = 1.26 keV/cm^3" (#14 §3); `verify/soliton_obituary.py` uses Ω h² = 0.120.

A convenient way to count a species is its yield Y = n/s, the number density n divided by the entropy density s [T]. Expansion dilutes n and s in the same way, so Y stays fixed once nothing creates or destroys the particles, and the density today is ρ = m·Y·s₀ for a particle of mass m [T]. The script takes s₀ = 2891.2 cm⁻³ ("s_0 ~ 2.9e3 /cm^3" in #14 §3). A relic-abundance mechanism is then a statement of what fixes Y.

## Thermal freeze-out [T]

### Equilibrium and departure from it

A species in contact with the hot plasma is created and destroyed in pairs. Its number density obeys the Boltzmann equation [T]

```text
dn/dt + 3Hn = −⟨σv⟩ (n² − n_eq²)
```

The term 3Hn is dilution by expansion at Hubble rate H. On the right, ⟨σv⟩ is the thermally averaged annihilation cross-section times relative velocity: −⟨σv⟩n² counts annihilations, and +⟨σv⟩n_eq² counts the inverse process, pair creation from the plasma. While the annihilation rate per particle, Γ = n⟨σv⟩, exceeds H, the two terms balance and n tracks its equilibrium value n_eq. Once the temperature T falls below the mass m, n_eq falls as e^{−m/T}, and with it Γ. When Γ drops below H, particles no longer find partners to annihilate with; Y stops changing and the species has frozen out [T].

In the radiation era the expansion rate is H = 1.66 √g\* T²/M_Pl, where g\* counts the relativistic degrees of freedom and M_Pl = 1.22089×10¹⁹ GeV is the (non-reduced) Planck mass. The coefficient 1.66 is the first anchor that `verify/soliton_obituary.py` checks: `Friedmann: H = 1.66 sqrt(g*) T^2/M_Pl`.

### Why freeze-out happens near T ~ m/20

Write x = m/T. Freeze-out happens where n_eq⟨σv⟩ = H. Because n_eq contains the factor e^{−x}, the solution for x is a logarithm of a large ratio, roughly the Planck mass times m⟨σv⟩, and a logarithm changes little when its argument changes by orders of magnitude [T]. So the freeze-out point x_f = m/T_f varies only slowly across species. The round-3 adjudication uses "T_f ~ m/20" (ruling 6), and the script starts its iteration for x_f at 20.

### The s-wave formula as the program codes it

For s-wave annihilation, σv is independent of velocity and is written σ₀. The script codes the standard approximate solution as "Kolb & Turner eqs. 5.43-5.45", with masses in GeV and σ₀ in GeV⁻²:

```text
Ω h² = 1.07×10⁹ x_f / (√g* M_Pl σ₀)
x_f  = ln(0.038 g M_Pl m σ₀ / √g*) − ½ ln x_f
```

Here g is the species' number of internal degrees of freedom and g\* is evaluated at freeze-out. The first line says Ω h² ∝ x_f/σ₀: the relic density is inversely proportional to the annihilation strength, so the weaker the annihilation, the more survive. The mass enters only through the logarithm in x_f. The second line is the freeze-out condition solved for x; x_f appears on both sides, so the script iterates it.

### The anchor

Before the script uses the formula on the hidden sector, it checks it on a standard relic: `freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)`. The check passes; it reports only that it passed, not the value it computed. Two earlier executions on the same input give values: the predecessor script of the v3 worklog gave "Ω h² = 0.108" ('New open items', O1), and the round-3 referee's own relic code gave "standard 100 GeV WIMP 2.2e-26 -> Omega h^2 = 0.1145" (`review/round3/referee/audit-notes.md`, Step 2), where a WIMP is a weakly interacting massive particle. The anchor is independent of the manuscript, a textbook value rather than one of the paper's own numbers ([independent anchors](/wiki/method/verification/independent-anchors)).

## A sector at its own temperature [T]

A hidden sector that has decoupled from the visible plasma keeps its own temperature T_h, which can differ from the visible temperature T. Its species freeze out at T_h ~ m/20, which corresponds to a different visible temperature from the one at which the same mass would freeze out in our plasma. The round-3 referee found that the withdrawn manuscript's hidden fermion ψ, at MeV-scale masses, freezes out during Big Bang nucleosynthesis (BBN): "hidden freeze-out T_h ~ m/20 occurs at T_vis ~ 0.08 MeV for m_psi = 1 MeV, 0.24 MeV for 3 MeV, 0.71 MeV for 10 MeV (step4.out) - i.e. during BBN. Needs m_psi >~ 20-30 MeV" (audit notes, Step 4(a) item 8). The adjudication accepted the point without re-checking it: "T_f ~ m/20, so the lower mass bound should be ≳ 20–30 MeV" (ruling 6). The general treatment is on [the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history).

## Cannibal dark matter [T]

If a sector has no lighter states to annihilate into and no coupling to ordinary matter, pair annihilation cannot reduce its number. Number-changing self-interactions can: in a three-to-two process, three particles scatter into two, and the rest mass of the third becomes kinetic energy of the survivors. Each such process removes a particle and heats the rest, so the sector's temperature falls far more slowly than that of a decoupled nonrelativistic gas, and the abundance it ends with depends on its self-coupling and its initial temperature rather than on any coupling to us [T]. A dark sector that stays warm in this way affects the growth of structure, which constrains the scenario [T].

The program's lab notebook names this as the obstacle for χ: "A sub-GeV, strongly self-coupled, gravitationally-only-connected sector cannot freeze out thermally without cannibalism problems; the abundance must be set asymmetrically — by *polarization-genesis* (§8)" (`notes/broken-born-theory.md` §5.3 [O]). The notebook does not spell out which cannibalism problems it means; the description above is the standard one.

## Asymmetric dark matter and the Sakharov conditions [T]

The baryons of ordinary matter did not freeze out: their annihilation is strong enough that almost none would survive. What survives is an excess of baryons over antibaryons, conventionally written η_B, the baryon asymmetry per photon [T]. Generating such an excess from a symmetric start needs three ingredients, the Sakharov conditions [T]:

1. a process that violates baryon number;
2. violation of C, charge conjugation, and of CP, charge conjugation and parity combined, so that matter and antimatter are produced at different rates;
3. a departure from thermal equilibrium, since in equilibrium the inverse processes erase any excess.

Asymmetric dark matter applies the same idea to dark matter: its density is set by a particle–antiparticle excess in the dark sector, and the symmetric part annihilates away [T]. If the two excesses share an origin, the density ratio becomes Ω_DM/Ω_b = (m_DM n_DM)/(m_p n_b), so a mechanism that fixes the number ratio links the mass of the dark particle to the observed density ratio [T].

The program takes baryogenesis as its template. The notebook writes "The observed Ω_χ/Ω_b = 5.4 is an input awaiting a mechanism, exactly as η_B awaited baryogenesis" (#1 §5.3), and its §8 sketches a mechanism ([Open: polarization-genesis and the 5.4 : 1 ratio](/wiki/dark-matter/candidates/polarization-genesis)).

## Freeze-in [T]

A species coupled too weakly to reach equilibrium is produced slowly by rare decays or scatterings in the plasma, and its abundance grows with the coupling, the reverse of freeze-out [T]. A coupling that is small but not small enough can instead bring the species into equilibrium. That is what the round-3 referee found for the soliton manuscript's ψ, if it carried a small electric charge through kinetic mixing: "with eps = 1e-6 the SM freeze-in of psi reaches equilibrium for all m_psi <= 30 GeV" (audit notes, Step 4(a) item 5; SM is the Standard Model; [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)). Round-3 Decision 1 closed this channel by taking [P4](/wiki/program/postulates/p4-polarized-matter) strictly: kinetic mixing is "ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry", which "closes three failure channels at once", the ψ millicharge among them.

## Coherent fields and defects

Two further routes set the abundance of things that are not thermal particles. A very light field that starts displaced from the minimum of its potential later oscillates coherently, and the oscillation behaves as cold dark matter: [the misalignment mechanism](/wiki/dark-matter/wave-dark-matter/misalignment-mechanism) [T]. Topological defects formed at a phase transition are counted by [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism), with later annihilation reducing the count ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)).

## How the program uses these

- **χ cannot freeze out.** The notebook's argument above, which makes the abundance an asymmetry problem and the ratio 5.4 : 1 an open problem for both remaining candidates (#11 §12, §14 item 7).
- **Wave χ by misalignment.** On [the wave island](/wiki/dark-matter/momentum-clumping/wave-island), very light χ is produced like an axion: "Open problem #5 (cannibalism-safe relic abundance) is moot on the wave island: misalignment is the mechanism" (`notes/debt3b-wave-island.md`, 'Bonus'; [relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)).
- **The hidden W′±.** In the minimal hidden sector of the soliton manuscript, the charged gauge bosons are stable and freeze out: "Standard freeze-out [17] then leaves them at 1e16 to 1e17 times the observed dark-matter density" (#14 §3). The result survives the candidate's retirement and is gated [V] (#11 §12; [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)).
- **The hidden fermion ψ.** Its freeze-out window was recounted in round 3: "v3 omitted ψ̄ and the second doublet member (a factor of 4)", and the corrected count is "10% of the DM at 45–49 GeV, 100% at 146–158 GeV" (ruling 4; DM is dark matter), checked in the script with σv = πα²/m² ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)). The BBN timing and the freeze-in route are the two items above.

## Standard references

The program's documents cite one source for this physics:

- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14 reference [17], unmarked. The v3 worklog lists it as not live-checked ('v3 as drafted (2026-10-19)'); the round-3 referee resolved it as "Front. Phys. 69 (1990), Addison-Wesley" and noted "standard; not checked page-level" (audit notes, Step 1). The script's formula is its eqs. 5.43–5.45.

Added by the wiki from model memory (†):

- P. Gondolo and G. Gelmini (1991)†: the thermal average and the freeze-out calculation done carefully.
- E. D. Carlson, M. E. Machacek and L. J. Hall (1992)†: self-interacting dark matter whose abundance is set by number-changing self-interactions, the cannibal scenario.
- A. D. Sakharov (1967)†: the conditions for generating a baryon asymmetry. The lab notebook's "1966" for the maturity of baryogenesis is not checked against a source ([references](/wiki/references)).
- D. E. Kaplan, M. A. Luty and K. M. Zurek (2009)†: asymmetric dark matter.
- L. J. Hall, K. Jedamzik, J. March-Russell and S. M. West (2010)†: freeze-in.

## Used by

- [Open: polarization-genesis and the 5.4 : 1 ratio](/wiki/dark-matter/candidates/polarization-genesis) — freeze-out fails for particle χ, so its abundance needs an asymmetric mechanism.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) and [the X-condensate candidate](/wiki/dark-matter/candidates/x-condensate) — both leave their abundance open.
- [Relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic) — the route that sets the abundance of wave χ.
- [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) — thermal freeze-out of the hidden W′±.
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — freeze-out of the hidden fermion ψ, and its timing against nucleosynthesis.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — relics computed at the hidden temperature.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — the freeze-out anchor.

## Sources

- `verify/soliton_obituary.py` — the freeze-out formula as coded, its constants, the Friedmann and freeze-out anchors, the W′ and ψ checks
- `review/round3-adjudication.md` 'Rulings' 4 — the ψ recount; 'Rulings' 6 — T_f ~ m/20 and the BBN bound; 'Decisions' 1 — strict sector separation
- `review/round3/referee/audit-notes.md` Step 1 — Kolb and Turner resolved, not page-checked; Step 2 — the referee's anchor value 0.1145; Step 4(a) items 5 and 8 — freeze-in of a millicharged ψ, and hidden freeze-out during BBN
- `review/v3-worklog.md` 'New open items' — the earlier anchor value, Ω h² = 0.108; 'v3 as drafted (2026-10-19)' — Kolb and Turner not live-checked
- `papers/broken-born-checkpoint-v2.md` §4 — P4 taken strictly; §12 — W′ overclosure [V] and the 5.4 : 1 question for both candidates
- `notes/broken-born-theory.md` §5.3 — why χ cannot freeze out thermally; §8 — polarization-genesis as the baryogenesis analog
- `notes/debt3b-wave-island.md` 'Bonus: the relic debt closes itself' — misalignment on the wave island
- `notes/knot-dark-matter-standalone.md` §3 — the target Ω h² ~ 0.12, s₀, and the freeze-out of W′ and ψ; 'References' [17] — Kolb and Turner
