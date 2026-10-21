---
title: "Relic abundance mechanisms"
weight: 10
status: established
description: "How a dark-matter density is set: thermal freeze-out, cannibal and asymmetric dark matter, freeze-in, and the Sakharov conditions for baryogenesis."
provenance: [T]
sources:
  - "notes/broken-born-theory.md §5.3"
  - "notes/broken-born-theory.md §8"
  - "notes/knot-dark-matter-standalone.md §3"
  - "verify/soliton_obituary.py"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "review/v3-worklog.md 'New open items'"
  - "review/round3/referee/audit-notes.md Step 4(a)"
---

*A relic abundance is the amount of a particle species left over from the hot early universe, and a relic-abundance mechanism is the process that sets that amount. In thermal freeze-out, particles annihilate in equilibrium with the hot plasma until the expansion of the universe outruns their annihilation, after which their number per unit volume only dilutes; the weaker the annihilation, the more survive. Other mechanisms set the amount differently: by an excess of particles over antiparticles, as for the baryons of ordinary matter; by slow production that never reaches equilibrium (freeze-in); or, in a sector whose particles can only annihilate among themselves, by number-changing self-interactions that turn rest mass into heat (cannibal dark matter). The program uses this standard physics to argue that conjugate matter χ cannot get its abundance from freeze-out, and to compute the relics of the retired soliton candidate's hidden sector.*

**Status:** Established — standard early-universe physics [T], explained here from general knowledge. The program's applications carry their own tags; `verify/soliton_obituary.py` checks its freeze-out code against a textbook value before using it ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).

## Key facts

- **Thermal freeze-out** [T]. A species in equilibrium tracks its equilibrium abundance until its annihilation rate falls below the expansion rate; its comoving number then stays fixed. Freeze-out occurs at a temperature about a twentieth of the mass: the round-3 adjudication uses "T_f ~ m/20" (ruling 6). The program's script codes the s-wave result as "Kolb & Turner eqs. 5.43-5.45" (a textbook the v3 worklog lists as not live-checked), with masses in GeV and σ₀ = σv in GeV⁻²:

  ```text
  Ω h² = 1.07×10⁹ x_f / (√g* M_Pl σ₀)
  x_f  = ln(0.038 g M_Pl m σ₀ / √g*) − ½ ln x_f
  ```

- **The anchor.** The gate first checks the formula on a standard relic: `freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)`, which passes. The earlier script of the v3 worklog gave "Ω h² = 0.108" for the same input. The target is the observed density: #14 §3 requires "Omega h^2 ~ 0.12, with mean rho_DM = 1.26 keV/cm^3".
- **Cannibal and asymmetric dark matter** [T]. The lab notebook applies them to χ [O]: "A sub-GeV, strongly self-coupled, gravitationally-only-connected sector cannot freeze out thermally without cannibalism problems; the abundance must be set asymmetrically — by *polarization-genesis* (§8)" (`notes/broken-born-theory.md` §5.3; [polarization-genesis](/wiki/dark-matter/candidates/polarization-genesis)).
- **Baryogenesis and the Sakharov conditions** [T]. An excess of baryons over antibaryons can arise only with baryon-number violation, C and CP violation (CP: charge conjugation and parity), and a departure from thermal equilibrium. The notebook takes the baryon asymmetry η_B as the template for dark matter: the observed Ω_χ/Ω_b = 5.4 "is an input awaiting a mechanism, exactly as η_B awaited baryogenesis" (#1 §5.3).
- **Freeze-in** [T]. A species coupled too weakly to reach equilibrium is produced slowly from the plasma. In round 3 the referee found that the soliton candidate's hidden fermion ψ, if millicharged at ε = 10⁻⁶, would reach equilibrium by freeze-in from the Standard Model plasma for all masses up to 30 GeV (audit notes, Step 4(a) item 5; [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).
- **Other routes, elsewhere.** A coherent field's abundance is set by [the misalignment mechanism](/wiki/dark-matter/wave-dark-matter/misalignment-mechanism); a topological defect's by [the Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism) and later annihilation ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)).

## Used by

- [Open: polarization-genesis and the 5.4 : 1 ratio](/wiki/dark-matter/candidates/polarization-genesis) — freeze-out fails for particle χ, so its abundance needs an asymmetric mechanism.
- [The χ-particle candidate](/wiki/dark-matter/candidates/chi-particles) and [the X-condensate candidate](/wiki/dark-matter/candidates/x-condensate) — both leave their abundance open.
- [Relic abundance by misalignment on the wave island](/wiki/dark-matter/momentum-clumping/wave-island/misalignment-relic) — the route that sets the abundance of wave χ.
- [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure) — thermal freeze-out of the hidden W′±.
- [Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window) — freeze-out of the hidden fermion ψ, and its timing against nucleosynthesis.
- [The hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history) — relics computed at the wrong hidden temperature.
- [The soliton-obituary script](/wiki/method/verification/soliton-obituary-script) — the freeze-out anchor.

## Sources

- `review/round3-adjudication.md` 'Rulings' 6 — T_f ~ m/20
- `verify/soliton_obituary.py` — the freeze-out formula as coded, and its anchor
- `review/round3/referee/audit-notes.md` Step 4(a) — freeze-in of a millicharged ψ
- `review/v3-worklog.md` 'New open items' — the earlier anchor value, Ω h² = 0.108
- `notes/broken-born-theory.md` §5.3 — why χ cannot freeze out thermally; §8 — polarization-genesis as the baryogenesis analog
- `notes/knot-dark-matter-standalone.md` §3 — the target Ω h² ~ 0.12, and the freeze-out of W′ and ψ
