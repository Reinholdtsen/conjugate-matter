---
title: "Obituary: the hidden SU(2) → U(1) proposal"
weight: 30
status: dead
description: "An adjoint Higgs breaks SU(2)_d to U(1)_d, leaving W′±, a massless hidden photon, stable monopoles and a light Dirac doublet ψ: a standard prior-art model, dead as a program-native proposal."
sources:
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'New open items'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "HANDOFF.md §6"
---

*The hidden SU(2) → U(1) proposal was the particle content #14 assumed for its dark sector: a hidden copy of a simple gauge force, SU(2)_d, whose Higgs field breaks it down to a single unbroken U(1)_d. The breaking leaves heavy charged W′± bosons, a massless hidden photon, and topologically stable 't Hooft–Polyakov monopoles, which were the dark-matter candidate; a light hidden fermion ψ was added because without it the W′± overclose the universe. #14 identified this sector with the momentum-polarized half of the program's matter, but nothing numerical in the proposal depended on that identification. As a model it is a standard hidden-sector monopole scenario already in the literature; as the program's own proposal it died with the soliton candidate on 2026-10-19.*

**Status:** Dead as a program-native proposal — retired with the candidate (round-3 Decision 2; [round-3 decisions](/wiki/method/review/round-3/decisions)). #14 marked the sector "(postulated)" and listed "the identification of the SU(2)_d sector as the momentum-polarized matter sector" as "Conjectural" (#14 §6). No `verify/` script checks the sector itself. Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); listed in [the graveyard](/wiki/status/graveyard).

## Key facts

- **The sector** (#14 §2, "The sector (postulated)."): "The momentum-polarized matter sector contains a gauge group SU(2)_d with a real adjoint scalar Phi whose expectation value v breaks it to U(1)_d. U(1)_d stays unbroken, so the hidden photon is massless. The charged vectors W'+- have mass g_d v. The sector also contains at least one Dirac fermion psi in the doublet, with U(1)_d charges +-g_d/2 (Sec. 3 shows it is required)."
- **Why it has monopoles** (#14 §3): "SU(2)_d -> U(1)_d has pi_2(SU(2)/U(1)) = pi_2(S^2) = Z and supports 't Hooft-Polyakov monopoles [15], stable by topological charge." Their mass is "M = 4 pi f v/g_d" ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)).
- **Why not a mirror Standard Model** (#14 §2): "An exact mirror copy of the Standard Model cannot serve: the electroweak vacuum manifold is S^3, whose pi_2 vanishes, so it has no stable monopoles. The hidden gauge structure must therefore differ from ours." The v3 worklog draws the consequence for the coupling hypothesis: "H relates couplings only, not gauge groups" ([the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).
- **How it got its content.** Round 2 asked the manuscript to "name an explicit candidate group (dual SU(2)→U(1) suffices)" (`HANDOFF.md` §6). The worklog's answer, R6: "SU(2) → U(1) by an adjoint Higgs; π₂(SU(2)/U(1)) = ℤ ['t Hooft 1974; Polyakov 1974]. Hiramatsu et al. (JHEP 12 (2021) 122) study exactly this case with kinetic mixing." Its item O1 then found the adjoint-only version excluded ([W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)), and R6 became "SU(2)_d → U(1)_d with at least one light dark doublet" ([the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)). #14 §6 lists "(iii) an unbroken U(1)_d" among its forced requirements.
- **Why it is dead as the program's** (referee, Step 4(d)): "the hidden-sector content, sector separation, xi and m_psi are all postulated". The referee called the proposal "the standard hidden 't Hooft-Polyakov-monopole scenario", citing Baek–Ko–Park, Khoze–Ro, Murayama–Shu and Liveoak–Maharana–Wells, "with one coupling choice (alpha_d = alpha)", and concluded that "it stands or falls on that literature, independently of Born reciprocity" ([the 'framework does no work' critique](/wiki/program/framework-does-no-work); [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)).
- **What survives.** The model's physics is not refuted: the statement that its minimal, adjoint-only version is excluded survives as a result [V] (#11 §12; [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure)), and the monopole physics it uses is established ([magnetic monopoles](/wiki/electric-magnetic-duality/monopoles)). How the hidden photon would mix with ours is [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing). What died is the program's claim to the sector.

## Sources

- `review/round3-adjudication.md` 'Decisions' 2 — the retirement
- `HANDOFF.md` §6 — round 2's request for an explicit group
- `review/round3/referee/audit-notes.md` Step 4(d) — "the standard hidden 't Hooft-Polyakov-monopole scenario"
- `review/v3-worklog.md` 'Round-2 pending list' (R6), 'New open items' (O1), 'v3 as drafted (2026-10-19)' — how the content was chosen
- `notes/knot-dark-matter-standalone.md` §2 — the sector, the mirror-Standard-Model argument; §3 — the monopoles; §6 — "Conjectural" and requirement (iii)
