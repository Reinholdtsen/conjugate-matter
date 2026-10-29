---
title: "Relic abundance mechanisms"
weight: 10
status: established
description: "How a dark-matter density is set, mechanism by mechanism: the yield, summaries of thermal freeze-out and of freeze-out in a hidden sector at its own temperature, cannibal and asymmetric dark matter, freeze-in, and the Sakharov conditions for baryogenesis."
provenance: [T]
sources:
  - "verify/soliton_obituary.py"
  - "review/round3-adjudication.md 'Rulings' 4"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "review/round3-adjudication.md 'Decisions' 1"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "papers/broken-born-checkpoint-v2.md §14 item 7"
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §8"
  - "notes/wave-island.md 'Bonus: the relic-abundance problem solves itself'"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md 'References'"
  - "review/wiki-build-flags.md item 18"
---

*A relic abundance is the amount of a particle species left over from the hot [early universe](/wiki/cosmology/early-universe), and a relic-abundance mechanism is the process that sets that amount. In [thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out), particles annihilate in equilibrium with the hot plasma until the expansion of the universe outruns their annihilation, after which their number per unit volume only dilutes; the weaker the annihilation, the more survive. Other mechanisms set the amount differently: by an excess of particles over antiparticles, as for the baryons of ordinary matter; by slow production that never reaches equilibrium (freeze-in); or, in a sector whose particles can only annihilate among themselves, by number-changing self-interactions that turn rest mass into heat (cannibal dark matter). The program uses this standard physics to argue that [conjugate matter χ](/wiki/dark-matter/conjugate-matter) cannot get its abundance from freeze-out, and [the round-3 review](/wiki/method/review/round-3) used it to compute the relics of [the retired soliton candidate](/wiki/dark-matter/candidates/soliton-candidate)'s [hidden sector](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector).*

**Status:** Established — standard early-universe physics [T], explained here from general knowledge; references the wiki adds are from model memory (†). The program's applications carry their own tags. `verify/soliton_obituary.py` checks its freeze-out code against a standard relic before using it ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).

## What is being set

The density of a species today is quoted as a fraction Ω of the critical density, the density of a spatially flat universe at the present expansion rate [T]. Early-universe calculations predict the product Ω h², where h is the present Hubble rate in a conventional unit: Ω h² is proportional to the physical density itself and does not depend on the measured value of h [T]. The target for dark matter, as the withdrawn manuscript #14 states it, is "Omega h^2 ~ 0.12, with mean rho_DM = 1.26 keV/cm^3" (#14 §3); `verify/soliton_obituary.py` uses Ω h² = 0.120.

A convenient way to count a species is its [yield Y = n/s](/wiki/cosmology/early-universe/relic-yield-and-dilution#the-yield-t), the number density n divided by the entropy density s [T]. Expansion dilutes n and s in the same way, so Y stays fixed once nothing creates or destroys the particles, and the density today is ρ = m·Y·s₀ for a particle of mass m [T]. The script takes s₀ = 2891.2 cm⁻³ ("s_0 ~ 2.9e3 /cm^3" in #14 §3). A relic-abundance mechanism is then a statement of what fixes Y.

## Thermal freeze-out [T]

A species in equilibrium with the hot plasma is made and annihilated in pairs. Once the temperature T falls below its mass m, its equilibrium density falls exponentially, and when annihilation becomes too slow to keep pace with the expansion, it soon ceases and the yield Y stays fixed: the species has frozen out [T]. This typically happens near T ~ m/20, the rule of thumb the round-3 adjudication uses ([ruling 6](/wiki/method/review/round-3/rulings#rulings-5-and-6-the-colder-hidden-sector-and-nucleosynthesis)). The relic density is roughly inversely proportional to the annihilation cross-section, so the weaker the annihilation, the more survive [T]. `verify/soliton_obituary.py` codes the standard solution for s-wave annihilation, whose σv tends to a constant at low velocity, as "Kolb & Turner eqs. 5.43-5.45", and checks it on a standard relic before using it. The Boltzmann equation, the reason for m/20, the formula as coded and its anchor, and the program's uses of freeze-out are on [thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out).

## A sector at its own temperature [T]

A hidden sector that has decoupled from the visible plasma keeps its own temperature T_h, and its species freeze out at T_h ~ m/20, which falls at a different visible temperature from the one at which the same mass would freeze out in our plasma. How the temperature ratio is set, changed and lost, and what it does to dark radiation and to the timing of freeze-out, is on [a hidden sector at its own temperature](/wiki/cosmology/early-universe/hidden-sector-temperature); how freeze-out itself changes in such a sector is on [thermal freeze-out](/wiki/dark-matter/candidates/thermal-freeze-out#freeze-out-in-a-sector-at-its-own-temperature-t). The case in the record is the withdrawn manuscript's hidden fermion ψ, which at MeV-scale masses would freeze out during [Big Bang nucleosynthesis](/wiki/cosmology/early-universe/big-bang-nucleosynthesis#the-ψ-relic-windows-lower-edge) (BBN) (audit notes, Step 4(a) item 8); the adjudication accepted without re-checking that "the lower mass bound should be ≳ 20–30 MeV" ([ruling 6](/wiki/method/review/round-3/rulings#rulings-5-and-6-the-colder-hidden-sector-and-nucleosynthesis); [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)).

## Cannibal dark matter [T]

If a sector has no lighter states to annihilate into and no coupling to ordinary matter, pair annihilation cannot reduce its number. Number-changing self-interactions can: in a three-to-two process, three particles scatter into two, and the rest mass of the third becomes kinetic energy of the survivors. Each such process removes a particle and heats the rest, so the sector's temperature falls far more slowly than that of a decoupled nonrelativistic gas, and the abundance it ends with depends on its self-coupling and its initial temperature rather than on any coupling to us [T]. A dark sector that stays warm in this way affects the growth of structure, which constrains the scenario [T].

The program's [lab notebook](/wiki/history/documents/lab-notebook) names this as the obstacle for χ: "A sub-GeV, strongly self-coupled, gravitationally-only-connected sector cannot freeze out thermally without cannibalism problems; the abundance must be set asymmetrically — by *polarization-genesis* (§8)" (`notes/broken-born-theory.md` §5.3 [O]). The notebook does not spell out which cannibalism problems it means; the description above is the standard one.

## Asymmetric dark matter and the Sakharov conditions [T]

The baryons of ordinary matter did not freeze out: their annihilation is strong enough that almost none would survive. What survives is an excess of baryons over antibaryons, conventionally written η_B, the baryon asymmetry per photon [T]. Generating such an excess from a symmetric start needs three ingredients, the Sakharov conditions [T]:

1. a process that violates baryon number;
2. violation of C, charge conjugation, and of CP, charge conjugation and parity combined, so that matter and antimatter are produced at different rates;
3. a departure from thermal equilibrium, since in equilibrium the inverse processes erase any excess.

Asymmetric dark matter applies the same idea to dark matter: its density is set by a particle–antiparticle excess in the dark sector, and the symmetric part annihilates away [T]. The density ratio is then Ω_DM/Ω_b = (m_DM n_DM)/(m_p n_b); if the two excesses share an origin that fixes the number ratio n_DM/n_b, the observed density ratio fixes the mass of the dark particle [T].

The program takes baryogenesis as its template. The notebook writes "The observed Ω_χ/Ω_b = 5.4 is an input awaiting a mechanism, exactly as η_B awaited baryogenesis" (#1 §5.3), and its §8 sketches a mechanism ([Open: polarization-genesis and the 5.4 : 1 ratio](/wiki/dark-matter/candidates/polarization-genesis)).

## Freeze-in [T]

A species coupled too weakly to reach equilibrium is produced slowly by rare decays or scatterings in the plasma, and its abundance grows with the coupling, the reverse of freeze-out [T]. A coupling that is small but not small enough can instead bring the species into equilibrium. That is what the round-3 referee found for the soliton manuscript's ψ, if it carried a small electric charge through kinetic mixing: "with eps = 1e-6 the SM freeze-in of psi reaches equilibrium for all m_psi <= 30 GeV" (audit notes, Step 4(a) item 5; SM is the Standard Model; [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)). [Round-3 Decision 1](/wiki/method/review/round-3/decisions#decision-1-strict-sector-separation) closed this channel by taking [P4](/wiki/program/postulates/p4-polarized-matter) strictly: kinetic mixing is "ε ≲ 10⁻¹³ from gravity alone, and zero if hidden charge conjugation is a gauged symmetry", which "closes three failure channels at once", the ψ millicharge among them.

## Coherent fields and defects

Two further routes set the abundance of things that are not thermal particles. A very light field that starts displaced from the minimum of its potential later oscillates coherently, and the oscillation behaves as cold dark matter: [the misalignment mechanism](/wiki/dark-matter/wave-dark-matter/misalignment-mechanism) [T]. [Topological defects](/wiki/symmetry-breaking/topological-defects) formed at a phase transition are counted by [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism), with later annihilation reducing the count ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)).

## How the program uses these

- **Particle χ and freeze-out.** The notebook's argument above [O], which makes the abundance an asymmetry problem and the ratio 5.4 : 1 an open problem for both remaining candidates ([#11](/wiki/history/documents/checkpoint) §12, §14 item 7).
- **Wave χ by misalignment.** On [the wave island](/wiki/dark-matter/momentum-clumping/wave-island), very light χ is produced like an [axion](/wiki/cosmology/dark-energy/axion-like-fields#wave-χ-produced-like-an-axion): "Open problem #5 (cannibalism-safe relic abundance) is moot on the wave island: misalignment is the mechanism" (`notes/wave-island.md`, 'Bonus'; [relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic)).
- **The hidden W′±.** In the minimal hidden sector of the soliton manuscript, the charged gauge bosons are stable and freeze out: "Standard freeze-out [17] then leaves them at 1e16 to 1e17 times the observed dark-matter density" (#14 §3). The result survives the candidate's retirement and is gated [V] (#11 §12; [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)).
- **The hidden fermion ψ.** Its freeze-out window was recounted in round 3: "v3 omitted ψ̄ and the second doublet member (a factor of 4)", and the corrected count is "10% of the DM at 45–49 GeV, 100% at 146–158 GeV" (ruling 4; DM is dark matter), checked in the script with σv = πα²/m² ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)). The BBN timing and the freeze-in route are the two items above.

## Standard references

The program's documents cite one source for this physics:

- E. W. Kolb, M. S. Turner, *The Early Universe* (Addison-Wesley, 1990): #14 reference [17], unmarked. The v3 worklog lists it as not live-checked ('v3 as drafted (2026-10-19)'); the round-3 referee resolved it as "Front. Phys. 69 (1990), Addison-Wesley" and noted "standard; not checked page-level" (audit notes, Step 1). The script's formula is its eqs. 5.43–5.45.

Added by the wiki from model memory (†):

- P. Gondolo and G. Gelmini (1991)†: the thermal average and the freeze-out calculation done carefully.
- E. D. Carlson, M. E. Machacek and L. J. Hall (1992)†: self-interacting dark matter whose abundance is set by number-changing self-interactions, the cannibal scenario.
- A. D. Sakharov (1967)†: the conditions for generating a baryon asymmetry. The lab notebook's "1966" for the maturity of baryogenesis is not checked against a source ([references](/wiki/references); `review/wiki-build-flags.md` item 18).
- D. E. Kaplan, M. A. Luty and K. M. Zurek (2009)†: asymmetric dark matter.
- L. J. Hall, K. Jedamzik, J. March-Russell and S. M. West (2010)†: freeze-in.

## Used by

- [Open: polarization-genesis and the 5.4 : 1 ratio](/wiki/dark-matter/candidates/polarization-genesis) — freeze-out fails for particle χ, so its abundance needs an asymmetric mechanism.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) and [the X-condensate candidate](/wiki/dark-matter/candidates/x-condensate) — both leave their abundance open.
- [Relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic) — the route that sets the abundance of wave χ.
- [The classicality theorem and the particle island](/wiki/dark-matter/momentum-clumping/classicality-theorem) — the particle island has no misalignment route, and the notebook rules out thermal freeze-out for it.
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — a hidden species freezing out at its own temperature, timed against nucleosynthesis.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — relics computed at the hidden temperature.
- [Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization) — the monopole yield n/s.
- [Overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction) — the closing mass, from the yield and the present entropy density.
- [Obituary: the √N topological floor (chat-only)](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor) — monopole annihilation as a relic calculation.

## Sources

- `verify/soliton_obituary.py` — Ω h² = 0.120 and s₀; the freeze-out function and its anchor, in summary; the W′ and ψ checks
- `review/round3-adjudication.md` 'Rulings' 4 — the ψ recount; 'Rulings' 6 — T_f ~ m/20 and the BBN bound; 'Decisions' 1 — strict sector separation
- `review/round3/referee/audit-notes.md` Step 1 — Kolb and Turner resolved, not page-checked; Step 4(a) items 5 and 8 — freeze-in of a millicharged ψ, and hidden freeze-out during BBN
- `review/v3-worklog.md` 'v3 as drafted (2026-10-19)' — Kolb and Turner not live-checked
- `papers/broken-born-checkpoint-v2.md` §4 — P4 taken strictly; §12 — W′ overclosure [V] and the 5.4 : 1 question for both candidates; §14 item 7 — the ratio as an open problem
- `notes/broken-born-theory.md` §5.3 — why χ cannot freeze out thermally; §8 — polarization-genesis as the baryogenesis analog
- `notes/wave-island.md` 'Bonus: the relic-abundance problem solves itself' — misalignment on the wave island
- `notes/knot-dark-matter-standalone.md` §3 — the target Ω h² ~ 0.12, s₀, and the freeze-out of W′ and ψ; 'References' [17] — Kolb and Turner
- `review/wiki-build-flags.md` item 18 — the notebook's 1966 date for baryogenesis
