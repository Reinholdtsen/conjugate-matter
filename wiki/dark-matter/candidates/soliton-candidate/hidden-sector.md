---
title: "Obituary: the hidden SU(2) → U(1) proposal"
weight: 30
status: dead
description: "An adjoint Higgs breaks SU(2)_d to U(1)_d, leaving W′±, a massless hidden photon, stable monopoles and a light Dirac doublet ψ: a standard prior-art model, dead as a program-native proposal."
sources:
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §6"
  - "review/skeptic-review-console.html"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'New open items'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "review/round3/referee/audit-notes.md Step 4(c)"
  - "review/round3/referee/audit-notes.md Step 4(d)"
  - "review/round3-adjudication.md 'Rulings'"
  - "review/round3-adjudication.md 'What survives v3'"
  - "review/round3-adjudication.md 'Decisions' 2"
  - "review/round3-preregistration.md 'Predictions'"
  - "papers/broken-born-checkpoint-v2.md §4"
  - "papers/broken-born-checkpoint-v2.md §12"
  - "verify/soliton_obituary.py"
  - "HANDOFF.md §6"
---

*The hidden SU(2) → U(1) proposal was the particle content the soliton manuscript #14 assumed for its dark sector: a hidden copy of a simple gauge force, SU(2)_d, whose Higgs field breaks it down to a single unbroken U(1)_d. The breaking leaves heavy charged W′± bosons, a massless hidden photon, and 't Hooft–Polyakov monopoles that are stable for topological reasons, which were the dark-matter candidate. A light hidden fermion ψ was added because without it the W′± would overclose the universe. #14 identified this sector with the momentum-polarized half of the program's matter, but nothing numerical in the proposal depended on that identification. As a model it is a standard hidden-sector monopole scenario already in the literature; as the program's own proposal it died with the soliton candidate on 2026-10-19.*

**Status:** Dead as a program-native proposal — retired with the candidate (round-3 Decision 2; [round-3 decisions](/wiki/method/review/round-3/decisions)). #14 marked the sector "(postulated)" and listed "the identification of the SU(2)_d sector as the momentum-polarized matter sector" as "Conjectural" (#14 §6). No `verify/` script checks the sector itself; the one result about it that survives, the exclusion of its minimal form, is [V], gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)). Home: [the soliton candidate](/wiki/dark-matter/candidates/soliton-candidate); listed in [the graveyard](/wiki/status/graveyard).

## What was claimed

### The sector

#14 v3 §2, "The sector (postulated).":

> The momentum-polarized matter sector contains a gauge group SU(2)_d with a real adjoint scalar Phi whose expectation value v breaks it to U(1)_d. U(1)_d stays unbroken, so the hidden photon is massless. The charged vectors W'+- have mass g_d v. The sector also contains at least one Dirac fermion psi in the doublet, with U(1)_d charges +-g_d/2 (Sec. 3 shows it is required).

The subscript d marks the hidden ("dark") sector, and g_d is its gauge coupling.

### What each piece is [T]

The content is the textbook case of an SU(2) gauge theory broken by an adjoint scalar, with a fermion doublet added; the explanation here is standard physics [T].

- **The gauge group and its scalar.** SU(2) has three gauge fields, one for each independent rotation of its internal space. The adjoint scalar Φ is a real three-component field that rotates like a vector in that space. Its potential is minimized when Φ has length v, so the vacuum picks a direction.
- **What breaks and what remains.** Rotations about the chosen direction leave Φ unchanged, so one U(1) subgroup survives: U(1)_d, whose gauge field stays massless and is the hidden photon. The other two gauge fields combine into the charged W′± and acquire mass g_d v by the Higgs mechanism.
- **Why there are monopoles.** The vacua, the directions Φ can point with length v, form a sphere, S² = SU(2)/U(1). Far from a localized object, Φ can point radially outward in every direction, wrapping that sphere once, and no continuous change of the field can undo a wrapping. #14 §3: "SU(2)_d -> U(1)_d has pi_2(SU(2)/U(1)) = pi_2(S^2) = Z and supports 't Hooft-Polyakov monopoles [15], stable by topological charge." The integer π₂ counts the wrappings ([the 't Hooft–Polyakov monopole](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole)). Their mass is "M = 4 pi f v/g_d", with f between 1 and about 1.79 (#14 §3; [overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)).
- **The fermion doublet.** ψ transforms as a two-component doublet of SU(2)_d, so its two components carry U(1)_d charges +g_d/2 and −g_d/2, half the W′ charge. It gives the W′± something to decay into, and its charge g_d/2 is the smallest in the sector, which sets the monopoles' magnetic charge by [Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization) ([the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).

### Why not a mirror copy of the Standard Model

The simplest hidden sector would be an exact copy of ours. #14 §2 ruled that out:

> An exact mirror copy of the Standard Model cannot serve: the electroweak vacuum manifold is S^3, whose pi_2 vanishes, so it has no stable monopoles. The hidden gauge structure must therefore differ from ours.

In the Standard Model a Higgs doublet breaks SU(2) × U(1) to the U(1) of electromagnetism, and the vacua form a three-sphere. Any way of mapping a sphere surrounding a point into a three-sphere can be shrunk continuously to a single vacuum, so no configuration is topologically trapped [T]. The worklog drew the consequence for #14's coupling hypothesis: "An exact mirror copy of the SM has no stable monopoles (π₂(S³) = 0), so H relates couplings only, not gauge groups" (`review/v3-worklog.md`, 'v3 as drafted (2026-10-19)'; SM is the Standard Model).

### The identification and the separation

Two postulates tied this sector to the program. The first is the identification itself: the opening words of the sector's definition, "The momentum-polarized matter sector contains", place it in the mirror-polarized half of the program's matter content ([P4](/wiki/program/postulates/p4-polarized-matter)). #14 §6 listed that identification as "Conjectural". The second is sector separation, also marked "(postulated)": "No field carries charge under both U(1)_d and our hypercharge" (#14 §2). How weakly the hidden photon may then mix with ours is [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing).

The manuscript described the sector with ordinary physics throughout. #14 §1: "Throughout, the hidden sector is described by ordinary relativistic quantum field theory. Whether the parent framework requires a different kinematics for momentum-polarized matter is an open question that this proposal does not use." The worklog's item O3 had found that #14 and the conjugate-relativity paper #13 were never reconciled on this, and that #13 itself has "two different dual cones" ([the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)); v3's decision was to "keep the dark sector in ordinary kinematics and say so explicitly".

## How it got its content

### v2 named no group

v2 of #14 required only that "the dual sector contains a gauge group G broken to a subgroup H with pi_2(G/H) nonzero", supporting "monopole-class defects classified by pi_2, not knot solitons in the pi_3/Hopfion sense", and listed "the existence and group theory of the dual gauge sector" as conjectural (`review/skeptic-review-console.html`, which embeds v2). Round 2 asked for more: "name an explicit candidate group (dual SU(2)→U(1) suffices)" (`HANDOFF.md` §6; [review rounds 1 and 2](/wiki/method/review/rounds-one-and-two)).

### The worklog's answer and its correction

The worklog's item R6 answered: "SU(2) → U(1) by an adjoint Higgs; π₂(SU(2)/U(1)) = ℤ ['t Hooft 1974; Polyakov 1974]. Hiramatsu et al. (JHEP 12 (2021) 122) study exactly this case with kinetic mixing." (`review/v3-worklog.md`, 'Round-2 pending list').

Its item O1 then computed what that minimal sector does in the early universe ('New open items'). With only the adjoint scalar, "W′± is the lightest dark-charged state, so it is stable", and because the monopoles need a hot hidden plasma to form, the W′± were thermal; their relic density exceeds the observed dark matter many times over. "The minimal model is excluded." The fix: "at least one light dark-charged fermion (a dark doublet) for W′± to decay into", and "R6 becomes "SU(2)_d → U(1)_d with at least one light dark doublet"." The surviving form of that result is [W′ overclosure: the minimal sector is excluded](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure).

### v3

v3 stated the negative result in its own text: "A negative result: the minimal model fails." and "The fix is the Dirac doublet psi: W'+ can decay to a psi pair." (#14 §3). ψ then became a relic of its own, with a mass window that round 3 overturned ([the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window)), and with ψ included the hidden sector's dark radiation required it to be colder than ours, ξ < 0.77 in v3 ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)). #14 §6 lists among its "Requirements forced by consistency (not optional)": "(i) at least one hidden doublet fermion with mass between the MeV scale and ~0.1 TeV" and "(iii) an unbroken U(1)_d".

## How it was tested

Round 3's referee audited the proposal without access to the program ([review round 3](/wiki/method/review/round-3)). Its conceptual audit asked whether the phase-space framework does any work, and answered no (`review/round3/referee/audit-notes.md`, Step 4(d)):

> the hidden-sector content, sector separation, xi and m_psi are all postulated; Sec. 1 "Kinematics" says the hidden sector is ordinary relativistic QFT. The DM proposal is the standard hidden 't Hooft-Polyakov-monopole scenario (Baek-Ko-Park 2013; Khoze-Ro 2014; Murayama-Shu 2009; LMW 2026) with one coupling choice (alpha_d = alpha), and it stands or falls on that literature, independently of Born reciprocity.

QFT is quantum field theory, DM is dark matter, and LMW is Liveoak–Maharana–Wells. The referee listed Baek–Ko–Park and Khoze–Ro, "both: hidden SU(2)->U(1) monopoles + W' + dark photon", as uncited prior art (Step 4(c) item 10; [topological dark matter in the literature](/wiki/dark-matter/candidates/soliton-candidate/prior-art)). The pre-registration had predicted the same weakness: "The candidate in §2–§4 is a standard hidden-sector monopole model."

The adjudication also accepted, as a to-do not individually re-checked, the referee's list of constraints the sector was never tested against: re-thermalization by ψ, limits on millicharged particles from supernova 1987A and from nucleosynthesis, charged-subcomponent and cosmic-microwave-background bounds, dark acoustic oscillations, the Higgs portal, the reheating mechanism for the temperature ratio, and collective magnetic-plasma effects ('Rulings', omitted constraints). Strict sector separation (Decision 1) later closed the channels that depend on mixing; the rest were not pursued after the candidate was retired.

## Why it died as the program's proposal

The model was not refuted. Its physics is the standard physics above, and its minimal form was excluded by the program's own calculation. What died is the claim that the program had selected it. Round-3 Decision 2, on the low-scale version of the same model: "Route (a), v ≲ 100 PeV, works, but it is Murayama–Shu's and Liveoak–Maharana–Wells's model. Nothing in it depends on Born reciprocity (the referee and the pre-registration agree), so claiming it would add no testable content and would misattribute it." The superheavy version failed on its abundance ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)). #14 had stated as much in advance: its charge-lattice motivation for the sector was used "only as motivation", and "No numerical result below depends on it" (#14 §2). This is the soliton episode's instance of [the 'framework does no work' critique](/wiki/program/framework-does-no-work).

## What survives

- **The exclusion of the minimal sector.** #11 §12: "The minimal adjoint-only SU(2) → U(1) hidden sector is excluded on its own terms: its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V]." The adjudication lists the same: "The statement that the minimal adjoint-only sector is excluded." See [W′ overclosure](/wiki/dark-matter/candidates/soliton-candidate/w-prime-overclosure).
- **The Dirac relation.** "A weakly coupled hidden sector always has strongly coupled monopoles, by Dirac quantization [T]" (#11 §12).
- **The mixing literature.** "The kinetic-mixing literature points (a) and (c)" (adjudication, 'What survives v3'): mixing induced by gravity alone is tiny or absent, and while U(1)_d is unbroken a hidden monopole induces no visible magnetic flux ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).
- **The monopole physics.** 't Hooft–Polyakov monopoles, their topology and their mass formula are established ([magnetic monopoles](/wiki/electric-magnetic-duality/monopoles)).

## Sources

- `review/round3-adjudication.md` 'Decisions' 2 — the retirement and the misattribution argument; 'What survives v3' — the minimal-sector exclusion and the mixing points; 'Rulings' — the omitted constraints
- `papers/broken-born-checkpoint-v2.md` §12 — the survivors, with tags; §4 — P4
- `verify/soliton_obituary.py` — the gated minimal-sector exclusion
- `review/round3/referee/audit-notes.md` Step 4(d) — "the standard hidden 't Hooft-Polyakov-monopole scenario"; Step 4(c) item 10 — the uncited prior art
- `review/round3-preregistration.md` 'Predictions' — the expected weakness
- `review/v3-worklog.md` 'Round-2 pending list' (R6), 'New open items' (O1, O3), 'v3 as drafted (2026-10-19)' — how the content was chosen and corrected
- `notes/knot-dark-matter-standalone.md` §1 — the ordinary kinematics; §2 — the sector, the mirror-Standard-Model argument, sector separation; §3 — the monopoles and the minimal model's failure; §6 — "Conjectural" and the requirements
- `review/skeptic-review-console.html` — v2's unnamed group
- `HANDOFF.md` §6 — round 2's request for an explicit group
