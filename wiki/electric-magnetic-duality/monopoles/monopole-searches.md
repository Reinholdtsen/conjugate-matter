---
title: "Monopole flux bounds: Parker and MACRO"
weight: 50
status: established
description: "Galactic magnetic fields bound the monopole flux (the Parker and extended Parker bounds), the MACRO experiment searched directly, and how the program should cite them."
provenance: [T]
sources:
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md refs [20]–[22]"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Verified references for v3'"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "HANDOFF.md §6"
---

*The monopole flux bounds are upper limits on how many magnetic monopoles pass through the Galaxy, stated as a flux per square centimetre per second per steradian. The Parker bound comes from the Galaxy's magnetic field: monopoles moving through it would gain energy from the field and drain it faster than the galactic dynamo regenerates it, so the field's survival caps the flux; the extended Parker bound applies the same argument to the weaker seed field of the young Galaxy. Direct searches, among them the Monopole, Astrophysics and Cosmic Ray Observatory whose limit the withdrawn #14 quotes, have found none. The program used these bounds only counterfactually, to show that the retired soliton candidate could not have been magnetically charged under our electromagnetism.*

**Status:** Established — [T] — limits from the literature, cited without tags in [#14](/wiki/dark-matter/candidates/soliton-candidate) as [20] (the Particle Data Group's 2024 monopole review by Milstead and Weinberg; Turner–Parker–Bogdan 1982; Parker 1970), [21] (the final result of the Monopole, Astrophysics and Cosmic Ray Observatory collaboration, 2002) and [22] (Adams et al. 1993). [The round-3 audit](/wiki/method/review/round-3/rulings) checked each figure #14 quotes against its source and found it supported (Step 1).

## Key facts

- **The Parker bound** (#14 §4; round-3 audit, Step 1, on [20]): F < 10⁻¹⁵ cm⁻² sr⁻¹ s⁻¹ for M ≲ 10¹⁷ GeV, as eq. (95.9) of the Particle Data Group's 2024 review gives it. The Turner–Parker–Bogdan abstract quotes F ≲ 10⁻¹⁶ as the "Parker limit", a different figure; #14 follows the Particle Data Group.
- **How to cite it** (`review/v3-worklog.md`, 'Verified references for v3'): for the 10⁻¹⁵ value, cite the Particle Data Group's 2024 review or Turner–Parker–Bogdan, Phys. Rev. D 26, 1296 (1982), "not Parker 1970 alone. That value holds for M ≲ 10¹⁷ GeV."
- **The extended Parker bound** (#14 [22]; worklog, round-2 item R3): Adams, Fatuzzo, Freese, Tarlé, Watkins, Turner, Phys. Rev. Lett. 70, 2511 (1993), abstract: "ℱ ≤ 10⁻¹⁶ (m/10¹⁷ GeV) cm⁻² s⁻¹ sr⁻¹". "Others quote a 1.2×10⁻¹⁶ prefactor", and eq. 95.10 of the Particle Data Group's review adds a low-mass term, which the audit judged "negligible here". The handoff's round-2 summary: with this bound the counterfactual exclusion is "~7 orders, not 5" (`HANDOFF.md` §6).
- **The direct search** (#14 [21]; audit, Step 1): Table 2 of the observatory's final paper gives "<= 2.8e-16 for m >~ 1e10 GeV, beta > 1e-4", that is, F ≤ 2.8×10⁻¹⁶ cm⁻² s⁻¹ sr⁻¹ for masses above about 10¹⁰ GeV and speeds above 10⁻⁴ c; the audit found that it supports #14's 2.8×10⁻¹⁶ exactly.
- **Charge and speed** (worklog R3; audit Step 1). For a monopole of magnetic charge g, with g_D the Dirac charge, the bounds scale as "(g/g_D)⁻² at high mass, (g/g_D)⁻¹ at low mass" (Kobayashi–Perri 2023, arXiv:2307.07553). The Particle Data Group's eq. (95.8) states that a Dirac-charge monopole of M ≳ 10¹¹ GeV is accelerated by the Galactic field to v ~ 10⁻³ c (10¹⁷ GeV/M)^(1/2).
- **The program's use** (#14 §4): counterfactual only. If the candidate's monopoles had carried magnetic charge under our electromagnetism, "The flux at dark-matter density would be F = n v/4 pi ~ 3e-8 /cm^2/s/sr", exceeding the Parker bound "by 7.5 orders of magnitude", the direct-search limit "by eight" and the extended Parker bound "by twelve"; the audit reproduced 7.50, 8.06 and 12.03 (Step 2). "Sector separation is therefore mandatory." The benchmark mass behind these numbers is withdrawn ([benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic)).

## Used by

- [Benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic) — the counterfactual flux that showed why the candidate needed sector separation.
- [Row 8: no monopoles of our sector](/wiki/predictions/monopole-null) — killed by a direct detection, which searches of this kind would provide.

## Sources

- `notes/knot-dark-matter-standalone.md` §4, refs [20]–[22] — the bounds as #14 quotes them, and the counterfactual (withdrawn manuscript).
- `review/round3/referee/audit-notes.md` Step 1, Step 2 — each bound checked against its source; the counterfactual excesses reproduced.
- `review/v3-worklog.md` 'Round-2 pending list' (R3), 'Verified references for v3' — the extended Parker bound, the charge scaling, and how to cite the Parker value.
- `HANDOFF.md` §6 — the round-2 request to cite the extended bound.
