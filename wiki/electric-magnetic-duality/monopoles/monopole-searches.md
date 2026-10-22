---
title: "Monopole flux bounds: Parker and MACRO"
weight: 50
status: established
description: "What a monopole flux limit measures; the Parker bound from the survival of the Galaxy's magnetic field, the extended Parker bound from its seed field, the direct search of the MACRO experiment; how the program should cite them, and the counterfactual it used them for."
provenance: [T]
sources:
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §4"
  - "notes/knot-dark-matter-standalone.md §5"
  - "notes/knot-dark-matter-standalone.md refs [20]–[22]"
  - "review/v3-worklog.md 'Round-2 pending list'"
  - "review/v3-worklog.md 'Findings neither referee raised'"
  - "review/v3-worklog.md 'Verified references for v3'"
  - "review/v3-worklog.md (evidence list)"
  - "review/round3/referee/audit-notes.md Step 1"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/step2a.out 'COUNTERFACTUAL FLUX'"
  - "HANDOFF.md §6"
  - "papers/broken-born-checkpoint-v2.md §11.1"
  - "papers/broken-born-checkpoint-v2.md §13"
---

*The monopole flux bounds are upper limits on how many [magnetic monopoles](/wiki/electric-magnetic-duality/monopoles) pass through the Galaxy, stated as a flux per square centimetre per second per steradian. The Parker bound comes from the Galaxy's magnetic field: monopoles moving through it would gain energy from the field and drain it faster than the galactic dynamo regenerates it, so the field's survival caps the flux; the extended Parker bound applies the same argument to the weaker seed field of the young Galaxy. Direct searches, among them the Monopole, Astrophysics and Cosmic Ray Observatory (MACRO) whose limit the withdrawn #14 quotes, have found none. The program used these bounds only counterfactually, to show that the retired soliton candidate could not have been magnetically charged under our electromagnetism.*

**Status:** Established — [T] — limits from the literature, cited without tags in [#14](/wiki/dark-matter/candidates/soliton-candidate) as [20] (the Particle Data Group's 2024 monopole review by Milstead and Weinberg; Turner–Parker–Bogdan 1982; Parker 1970), [21] (MACRO's final result, 2002) and [22] (Adams et al. 1993). [The round-3 audit](/wiki/method/review/round-3/rulings) checked each figure #14 quotes against its source and found it supported (Step 1). The explanations below are standard physics written from general knowledge [T]; references added from memory are marked †.

## What a flux limit measures [T]

A population of monopoles of number density n, moving in random directions at speed v, sends F = n v/4π of them through each unit area per unit time per unit solid angle. A limit on the flux F, in cm⁻² s⁻¹ sr⁻¹, is therefore a limit on the product n v. Converting it to a density needs the speed, and the speed depends on the mass. Monopoles bound to the Galaxy move at the speeds of the [dark-matter halo](/wiki/dark-matter/halo-astrophysics), about 10⁻³ c, which is #14's "drifting at ~1e-3 c" (§3). A monopole also gains speed from the Galaxy's magnetic field: the round-3 audit cites eq. (95.8) of the Particle Data Group (PDG) review, by which "a Dirac-charge monopole of M >~ 1e11 GeV is accelerated by the Galactic field to v ~ 1e-3 c (1e17 GeV/M)^(1/2)" (Step 1). Lighter monopoles are accelerated more.

The limits come in two kinds. Astrophysical bounds ask what a flux of monopoles would do to something observed; direct searches count monopoles passing through a detector.

## The Parker bound [T]

The Galaxy carries a large-scale magnetic field, maintained by a dynamo that regenerates it over a characteristic time. A monopole of magnetic charge g moving through a region of field B and size ℓ is accelerated along the field and gains kinetic energy of order gBℓ, and that energy is taken from the field. A flux of monopoles crossing the Galaxy therefore drains the field at a rate proportional to the flux. The field has survived, so the drain cannot exceed the field's energy divided by its regeneration time, and that requirement caps the flux (Parker, 1970).

How the cap depends on mass follows from the same picture [T]. A light monopole is accelerated to a speed set by the field, so each one removes the full energy gBℓ, and the bound does not depend on the mass. A heavy monopole moves at halo speed and is only slightly deflected; some heavy monopoles gain energy from the field and others lose energy to it, the gains and losses partly cancel, and the bound weakens as the mass grows.

The value #14 used is the Particle Data Group's. The round-3 audit read it as "PDG 2024 (Milstead & Weinberg), eq. (95.9): Parker F < 1e-15 cm^-2 sr^-1 s^-1 for M <~ 1e17 GeV" and found that it supports #14's use (Step 1). The abstract of Turner, Parker and Bogdan quotes a different "Parker limit", F ≲ 10⁻¹⁶; the audit's comment: "the manuscript follows PDG; fine".

**How to cite it.** The v3 worklog's literature check settled the citation: "For the 10⁻¹⁵ Parker value, cite PDG 2024 or Turner–Parker–Bogdan, PRD 26, 1296 (1982), not Parker 1970 alone. That value holds for M ≲ 10¹⁷ GeV" (`review/v3-worklog.md`, 'Verified references for v3').

## The extended Parker bound [T]

Adams, Fatuzzo, Freese, Tarlé, Watkins and Turner (1993) applied the argument to an earlier field: the weak seed field of the young Galaxy, before the dynamo amplified it. A weaker field holds less energy and is drained by fewer monopoles, so requiring that the seed survive gives a tighter bound, one that grows in proportion to the monopole mass and so is most restrictive for lighter monopoles. The worklog quotes the abstract (item R3, 'Round-2 pending list'):

```text
ℱ ≤ 10⁻¹⁶ (m/10¹⁷ GeV) cm⁻² s⁻¹ sr⁻¹
```

The same item notes the variants: "Others quote a 1.2×10⁻¹⁶ prefactor, and PDG 2024 Eq. 95.10 adds a low-mass floor." The round-3 audit found the abstract supporting #14's figure exactly, and judged the added term small: "(PDG eq. 95.10 adds a +3e-6 term inside the bracket - negligible here.)" (Step 1). The worklog's literature report read only the abstract of this paper: "Adams et al. 1993 full text (paywalled; abstract only)".

**Charge.** Both Parker bounds are stated for a monopole of the Dirac charge g_D ([Dirac quantization](/wiki/electric-magnetic-duality/monopoles/dirac-quantization)). A larger charge drains more energy per monopole, so the bounds tighten; worklog R3 gives the scaling "(g/g_D)⁻² at high mass, (g/g_D)⁻¹ at low mass [Kobayashi–Perri 2023, arXiv:2307.07553]".

## Direct searches: MACRO [T]

A monopole passing through matter can be detected in two standard ways [T]:

- **Induction.** A monopole passing through a superconducting loop changes the magnetic flux through the loop by an amount fixed by its magnetic charge, and so changes the loop's persistent current by a fixed step, whatever the monopole's speed or mass. For a Dirac monopole the step is set by g_D = 2π/e.
- **Ionization.** A magnetic charge g moving at speed v acts on atomic electrons like an electric charge of size g v (in units with c = 1). Since g_D is large in units of e, g_D/e = 1/(2α), a fast Dirac monopole ionizes matter far more strongly than a singly charged particle at the same speed, and leaves a distinctive track; a slow one deposits much less and needs detectors built for slow particles.

MACRO, the Monopole, Astrophysics and Cosmic Ray Observatory, was a large underground detector at the Gran Sasso laboratory in Italy† that combined several detection techniques to cover a wide range of monopole speeds†. Its final result is #14's reference [21] (M. Ambrosio et al., Eur. Phys. J. C 25, 511 (2002), hep-ex/0207020). The round-3 audit read its Table 2 as "<= 2.8e-16 for m >~ 1e10 GeV, beta > 1e-4", with a global limit of 1.4e-16, and found that it supports #14's 2.8e-16 exactly (Step 1). The limit is F ≤ 2.8×10⁻¹⁶ cm⁻² s⁻¹ sr⁻¹ for masses above about 10¹⁰ GeV and speeds above 10⁻⁴ c (β = v/c). Which line of the table applies depends on the mass: when #14's benchmark moved to 3×10¹³ GeV, the worklog recorded that "the counterfactual MACRO limit is ≤ 2.8×10⁻¹⁶ (m ≳ 10¹⁰ GeV row), not 1.4×10⁻¹⁶ (m ≳ 10¹⁶ GeV row)" (finding F1). The Particle Data Group's review, #14's reference [20], collects the limits of MACRO and of later searches.

The three limits #14 used:

```text
Parker (PDG 2024, eq. 95.9):       F < 10⁻¹⁵ cm⁻² sr⁻¹ s⁻¹             M ≲ 10¹⁷ GeV
extended Parker (Adams et al.):    ℱ ≤ 10⁻¹⁶ (m/10¹⁷ GeV) cm⁻² s⁻¹ sr⁻¹
MACRO final (Table 2):             F ≤ 2.8×10⁻¹⁶ cm⁻² s⁻¹ sr⁻¹         m ≳ 10¹⁰ GeV, β > 10⁻⁴
```

## How the program uses the bounds

### A counterfactual for the soliton candidate

The retired soliton candidate's monopoles were charged only under a hidden U(1), by its postulated [sector separation](/wiki/program/postulates/p4-polarized-matter): "These objects carry no charge under our photon" (#14 §2). The searches on this page could not have seen them. #14 §4 used the bounds to show why that had to be so:

> Not monopoles of our U(1). If these objects carried magnetic charge under our electromagnetism, they would be classic monopoles and excluded. The flux at dark-matter density would be F = n v/4 pi ~ 3e-8 /cm^2/s/sr. That exceeds the Parker bound (~1e-15 for M <~ 1e17 GeV) [20] by 7.5 orders of magnitude, the MACRO limit for m >~ 1e10 GeV (2.8e-16) [21] by eight, and the extended Parker bound 1e-16 (M/1e17 GeV) [22] by twelve. Sector separation is therefore mandatory.

The round-3 referee reproduced the excesses as 7.50, 8.06 and 12.03 orders, and found them larger still at the speed of PDG eq. (95.8), "conclusion strengthened" (Step 2; `review/round3/referee/step2a.out`). The excess over the extended bound is the largest because that bound tightens as the mass falls, and #14's benchmark lay far below 10¹⁷ GeV. The benchmark mass behind these numbers is withdrawn, while the arithmetic survives as benchmark-conditional ([benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic), which gives the full record).

Two corrections reached the counterfactual through review:

- **[Round 2](/wiki/method/review/rounds-one-and-two)** asked for the extended bound. The [handoff](/wiki/history/documents/handoff)'s summary: "extended Parker bound (Adams et al. 1993: F ≲ 10⁻¹⁶(m/10¹⁷ GeV) ⇒ our-U(1) exclusion is ~7 orders, not 5 — cite it)" (`HANDOFF.md` §6). That was at v2's 10¹⁶ GeV benchmark, where worklog R3 gives "Excess at the 10¹⁶ benchmark: 6.98 orders [V]".
- **The literature check** found that kinetic mixing with an unbroken hidden U(1) gives the monopoles no visible magnetic flux, so the bounds stay in v3 only as a reason: "Parker and MACRO stay in v3 only as the reason sector separation is needed: they show what would happen if these objects were monopoles of our U(1)" (worklog, finding L1; [kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing)).

#14 also made a real flux its exclusion condition 2: "Any confirmed magnetic-monopole flux of our U(1) at dark-matter abundance" (§5).

### Our sector's monopoles

The program predicts that no monopole of our own electromagnetism will be found: [row 8](/wiki/predictions/monopole-null) of #11 §13, killed by "Direct detection". The searches on this page are the experiments that would kill it. The program's reason for expecting a null is not its own physics: [#11](/wiki/history/documents/checkpoint) §11.1 attributes the absence to [inflationary dilution](/wiki/cosmology/early-universe/inflation-and-dilution) [T] ([the monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem)). Monopoles of the conjugate sector, if they exist, would interact with ours only by gravity ([conjugate monopoles as ontology](/wiki/electric-magnetic-duality/conjugate-monopoles)), so flux searches of this kind do not test them.

## References

As #14 cites them (without tags; the round-3 audit checked each against its source):

- [20] Particle Data Group, Review of Particle Physics (2024), "Magnetic Monopoles" review (D. Milstead, E. J. Weinberg); M. S. Turner, E. N. Parker, T. J. Bogdan, Phys. Rev. D 26, 1296 (1982); E. N. Parker, Astrophys. J. 160, 383 (1970).
- [21] MACRO Collaboration (M. Ambrosio et al.), Eur. Phys. J. C 25, 511 (2002), hep-ex/0207020.
- [22] F. C. Adams, M. Fatuzzo, K. Freese, G. Tarlé, R. Watkins, M. S. Turner, Phys. Rev. Lett. 70, 2511 (1993).

From the v3 worklog's literature report:

- Kobayashi–Perri, Phys. Rev. D 108, 083005 (2023), arXiv:2307.07553 — the charge scaling of the Parker bounds.

## Used by

- [Benchmark-conditional arithmetic](/wiki/dark-matter/candidates/soliton-candidate/benchmark-arithmetic) — the counterfactual flux that showed why the candidate needed sector separation.
- [Row 8: no monopoles of our sector](/wiki/predictions/monopole-null) — killed by a direct detection, which searches of this kind would provide.
- [The monopole problem](/wiki/electric-magnetic-duality/monopoles/monopole-problem) — the observational side of the absence of monopoles.
- [Obituary: conjugate monopoles explain the null result](/wiki/electric-magnetic-duality/monopole-explanation) — the null result the dead explanation addressed.

## Sources

- `notes/knot-dark-matter-standalone.md` §2, §3, §4, §5, refs [20]–[22] — the bounds as #14 quotes them, the counterfactual, and exclusion condition 2 (withdrawn manuscript).
- `review/round3/referee/audit-notes.md` Step 1, Step 2 — each bound checked against its source, PDG eq. (95.8), and the counterfactual excesses reproduced.
- `review/round3/referee/step2a.out` (the counterfactual-flux block) — the excesses at both speeds.
- `review/v3-worklog.md` 'Round-2 pending list' (R3), 'Findings neither referee raised' (F1, L1), 'Verified references for v3', and the evidence list — the extended Parker bound, the charge scaling, the MACRO row, the counterfactual's role, and how to cite the Parker value.
- `HANDOFF.md` §6 — the round-2 request to cite the extended bound.
- `papers/broken-born-checkpoint-v2.md` §11.1, §13 — the absence of our monopoles attributed to inflation, and row 8.
