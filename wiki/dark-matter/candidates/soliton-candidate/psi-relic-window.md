---
title: "Obituary: the ψ relic window"
weight: 90
status: dead
description: "v3 omitted ψ̄ and the second doublet member and bracketed an exact cross-section by ×10; the recount puts 10% of the dark matter at 45–49 GeV and all of it at 146–158 GeV, and MeV-scale ψ would freeze out during nucleosynthesis."
provenance: [V]
sources:
  - "review/round3-adjudication.md 'Rulings' 4"
  - "review/round3-adjudication.md 'Rulings' 6"
  - "verify/soliton_obituary.py"
  - "review/round3/adjudicator/round3_arb.out"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3-adjudication.md 'Decisions' 1"
---

*The ψ relic window was the range of masses #14 v3 allowed for ψ, the light hidden fermion it added so that the heavy hidden W′± bosons could decay. ψ is itself stable and left over from the early universe, so its mass sets how much of the dark matter it would make up: v3 wanted ψ light enough to be a minor component, so that the monopoles dominate, and heavy enough to have annihilated before nucleosynthesis. The round-3 review found both edges wrong. The upper edge was too high because v3 had left out the antiparticle and the second member of the doublet, a factor of 4, and had bracketed an exactly known annihilation cross-section over a factor of ten; the lower edge was too low because MeV-scale ψ would still be freezing out during nucleosynthesis. The window died with these corrections, and the candidate it served was retired.*

**Status:** Dead — round-3 ruling 4, upheld; the recount is [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). Ruling 6, on the lower edge, was "Accepted, not re-checked". Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); rulings in [round-3 verdict and rulings](/wiki/method/review/round-3/rulings); listed in [the graveyard](/wiki/status/graveyard).

## Key facts

- **What v3 claimed** (#14 §3): "Under H, psi makes up less than 10% of the dark matter for m_psi below 0.1-0.3 TeV, and all of it at 0.3-1 TeV. We take m_psi below about 0.1 TeV, so that the monopoles dominate, and above the MeV scale, so that psi has annihilated before nucleosynthesis." It became requirement (i): "at least one hidden doublet fermion with mass between the MeV scale and ~0.1 TeV" (#14 §6). Why ψ was needed: [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure).
- **Ruling 4** (upheld), on the share of the dark matter (DM) that ψ makes up: "v3 omitted ψ̄ and the second doublet member (a factor of 4), and bracketed an exactly known s-wave σv up to ×10. My recount: 10% of the DM at 45–49 GeV, 100% at 146–158 GeV. The referee's Boltzmann integration gives 28–46 / 96–153 GeV. We agree to within ×1.6, and v3's 0.1–0.3 TeV was wrong."
- **The gate's check**, with "psi, psi-bar, both doublet members; sigma v = pi alpha^2/m^2": `10% of the dark matter at 45-49 GeV  [45.2-48.8]` and `100% at 146-158 GeV  [146.4-158.0]`, both passing. The arbitration run shows the two countings side by side for g\* = 80 and 106.75: "v3 counting" puts all of the dark matter at 297 and 321 GeV and 10% at 92 and 99 GeV; "psi+psibar, two doublet members" puts them at 146 and 158 GeV and at 45 and 49 GeV ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)).
- **The referee's numbers** (audit notes, Step 2) depend on the hidden-to-visible temperature ratio ξ₀: 10% of the dark matter at "28.3 GeV (xi0=1), 34.9 GeV (xi0=0.76), 45.9 GeV (xi0=0.5)" and all of it at "96 GeV (xi0=1), 118 GeV (0.76), 153 GeV (0.5)", verdict "DISCREPANT (factor 3-10 in mass)". The record carries the adjudicator's numbers, which the gate checks.
- **At the colder hidden sector v3 required** (Step 4(a) item 4), v3's "below about 0.1 TeV" would make ψ "~70-100%" of the dark matter (73.1% at 100 GeV for ξ₀ = 0.76) instead of a minor component ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)).
- **Ruling 6** (accepted, not re-checked): "T_f ~ m/20, so the lower mass bound should be ≳ 20–30 MeV." The referee found hidden freeze-out "at T_vis ~ 0.08 MeV for m_psi = 1 MeV, 0.24 MeV for 3 MeV, 0.71 MeV for 10 MeV" — that is, during nucleosynthesis (Step 4(a) item 8).
- **Channels that became moot.** A millicharged ψ, its re-thermalization of the hidden sector, and the supernova and charged-subcomponent limits on it were never evaluated in #14; the adjudication accepted them as a to-do, and strict sector separation (Decision 1) closes the millicharge and re-thermalization channels ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).

## Sources

- `review/round3-adjudication.md` 'Rulings' 4 and 6 — the recount and the lower edge; 'Decisions' 1 — the channels closed
- `verify/soliton_obituary.py` — the gated recount
- `review/round3/adjudicator/round3_arb.out` — both countings side by side
- `review/round3/referee/audit-notes.md` Step 2 — the referee's Boltzmann integration; Step 4(a) — the colder sector and freeze-out during nucleosynthesis
- `notes/knot-dark-matter-standalone.md` §3 — v3's window; §6 — requirement (i)
