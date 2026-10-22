---
title: "W′ overclosure: the minimal sector is excluded"
weight: 80
status: alive
description: "Without a light charged fermion the thermal W′± would outweigh the observed dark matter 10¹⁶–10¹⁷ times, which forced the hidden doublet — a result that survives the candidate."
provenance: [V]
sources:
  - "papers/broken-born-checkpoint-v2.md §12"
  - "review/round3-adjudication.md 'What survives v3'"
  - "verify/soliton_obituary.py"
  - "review/round3/referee/audit-notes.md Step 2"
  - "review/round3/referee/audit-notes.md Step 4(a)"
  - "review/round3/referee/ggww.out"
  - "review/round3-preregistration.md 'Predictions'"
  - "review/v3-worklog.md 'New open items'"
  - "review/v3-worklog.md 'v3 as drafted (2026-10-19)'"
  - "notes/knot-dark-matter-standalone.md §1"
  - "notes/knot-dark-matter-standalone.md §2"
  - "notes/knot-dark-matter-standalone.md §3"
  - "notes/knot-dark-matter-standalone.md §6"
---

*W′ overclosure is the result that the simplest version of the soliton candidate's hidden sector — SU(2)_d broken to U(1)_d by an adjoint Higgs field and nothing else — is excluded by its own heavy charged gauge bosons, the W′±. With no lighter particle carrying hidden charge, the W′± cannot decay. The hot hidden plasma in which the monopoles form also fills the universe with W′±, and after they stop annihilating, their density would exceed the observed [dark matter](/wiki/dark-matter) 10¹⁶ to 10¹⁷ times. #14 v3 therefore added a light hidden fermion ψ for the W′± to decay into. The calculation was done at the withdrawn benchmark mass, but the statement that the minimal sector is excluded survived the candidate's retirement and is machine-checked.*

**Status:** Alive — it survives the candidate; the number is conditional on the withdrawn benchmark. [Checkpoint #11](/wiki/history/documents/checkpoint) §12 lists it under "What survives" with [V]. The [round-3](/wiki/method/review/round-3) adjudication lists both "The statement that the minimal adjoint-only sector is excluded" and, among "The benchmark-conditional arithmetic", the "W′ overclosure". Gated in `verify/soliton_obituary.py` ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)).

## Statement

#11 §12, under "What survives":

> The minimal adjoint-only SU(2) → U(1) hidden sector is excluded on its own terms: its stable W′± overclose the universe by 10¹⁶–10¹⁷ at the v3 benchmark [V].

"Overclose" strictly means a relic density above the universe's critical density [T]; the sources measure the W′± relic against the observed dark-matter density instead, and here it exceeds that density 10¹⁶ to 10¹⁷ times. "On its own terms", as the wiki reads it, means that the sector fails through its own content and the hot plasma its monopole production requires, whether or not the monopoles are the dark matter. The numbers are evaluated at the benchmark mass that the candidate's abundance count produced, and that count was wrong ([Obituary: the Kibble normalization](/wiki/dark-matter/candidates/soliton-candidate/kibble-normalization)); the statement of exclusion is listed separately as surviving, and the round-3 referee confirmed the numbers.

## The minimal sector

The withdrawn manuscript [#14](/wiki/dark-matter/candidates/soliton-candidate) postulated a hidden gauge group SU(2)_d with a real scalar Φ in the adjoint (three-component) representation, whose expectation value v breaks SU(2)_d to U(1)_d (§2; [Obituary: the hidden SU(2) → U(1) proposal](/wiki/dark-matter/candidates/soliton-candidate/hidden-sector)). Of the three SU(2) gauge bosons, the one along the direction Φ points in stays massless; it is the hidden photon of U(1)_d. The other two combine into a pair of charged vectors, W′⁺ and W′⁻, which carry charge ±g_d under U(1)_d [T]. #14 §2: "U(1)_d stays unbroken, so the hidden photon is massless. The charged vectors W'+- have mass g_d v." The same breaking supports the candidate's ['t Hooft–Polyakov monopoles](/wiki/electric-magnetic-duality/monopoles/thooft-polyakov-monopole).

The minimal sector has nothing else: no fermion and no further scalar. Charge conservation lets a particle decay only into lighter states with the same total charge, so the lightest particle carrying a given conserved charge cannot decay at all [T]. #14 §3, under the heading "A negative result: the minimal model fails.":

> With only the adjoint scalar, the W'+- are the lightest hidden-charged states and are stable by U(1)_d charge. Kibble production (below) requires a hidden plasma at temperature ~ v, so the W' are thermally populated and freeze out. At the benchmark mass below, m_W' ~ (5-9)e11 GeV. Standard freeze-out [17] then leaves them at 1e16 to 1e17 times the observed dark-matter density, bracketing the annihilation coefficient over a factor of ten. The adjoint-only sector is excluded.

### The masses at the benchmark

The monopole mass is M = 4π f v/g_d, where f runs from 1 in the Bogomolny–Prasad–Sommerfield limit to "about 1.79 at large scalar self-coupling"; under the manuscript's coupling hypothesis H this gives "M ~ (21-37) v" (#14 §3). v3's benchmark M = 3×10¹³ GeV "corresponds to v ~ (0.8-1.4)e12 GeV", and m_W′ = g_d v then lies at (5–9)×10¹¹ GeV. The referee recomputed both from independently chosen constants: "v at 3e13 | (0.8-1.4)e12 | 8.09e11 - 1.446e12 | CONFIRMED" and "m_W' | (5-9)e11 | 4.90e11 - 8.76e11 | CONFIRMED" (`review/round3/referee/audit-notes.md`, Step 2).

The script writes the W′ mass as α_W′ M/f, with α_W′ = g_d²/4π. It is the same quantity: substituting v = M g_d/(4π f) from the mass relation into m_W′ = g_d v gives g_d² M/(4π f).

## Why the W′± are thermal

The monopoles were to be made by the [Kibble mechanism](/wiki/electric-magnetic-duality/monopoles/kibble-mechanism), at the transition where the hidden plasma cools through T ~ v and Φ condenses. A plasma at that temperature contains every hidden species not much heavier than v in equilibrium, the W′± among them [T]. As the plasma cools further, they annihilate into hidden photons until the expansion of the universe outruns the annihilation, and the remainder freezes out ([relic abundance mechanisms](/wiki/dark-matter/candidates/relic-abundance)). The worklog states the link in one line: "Kibble production needs a hot dark plasma at T ~ Λ_c, so the W′± were thermal" (`review/v3-worklog.md`, 'New open items', O1), where Λ_c is the worklog's earlier symbol for the breaking scale.

## Freeze-out and the size of the overclosure

In standard s-wave freeze-out the relic density is inversely proportional to the annihilation cross-section [T]. For annihilation through a gauge coupling α, σv scales as α²/m², so a heavier species annihilates more weakly and leaves more behind; at masses near 10¹² GeV the relic is enormous. The script ([the soliton-obituary script](/wiki/method/verification/soliton-obituary-script)) computes it with the Kolb–Turner freeze-out formula described on [the relic-abundance page](/wiki/dark-matter/candidates/relic-abundance#the-s-wave-formula-as-the-program-codes-it), with these inputs:

```text
σv     = κ π α_W′² / m_W′²        κ = 1 and 10
m_W′   = α_W′ M / f               f = 1 and 1.787,  M = 3×10¹³ GeV
g      = 3 internal states per W′, both charges counted (factor 2)
g*     = 106.75 + 9
target = Ω h² = 0.12
```

Its output, which passes:

```text
PASS  stable W'+- overclose by 1e16-1e17  [9.5e+15-2.0e+17]
```

The check requires the base-10 logarithms of the smallest and largest of the four cases to round to 16 and 17. The spread comes from the two brackets: κ over a factor of ten, and f between its two limits. Before using the formula on the hidden sector, the script checks it on a standard relic, "freeze-out: 100 GeV, sigma v = 2.2e-26 cm^3/s gives Omega h^2 ~ 0.12 (within x2)", an anchor independent of the manuscript ([independent anchors](/wiki/method/verification/independent-anchors)).

## The annihilation coefficient by detailed balance

v3 did not compute the W′⁺W′⁻ annihilation cross-section; it bracketed the coefficient κ between 1 and 10. The round-3 referee computed it, using detailed balance [T]: the cross-sections of a two-body process and of its inverse are related by the ratio of their phase-space and spin-counting factors, so a known pair-production cross-section fixes the annihilation cross-section of the same pair. The referee took the published cross-section for photon–photon production of a W pair, γγ → W⁺W⁻ (hep-ph/9405359 eq. 5.15), and obtained near threshold (`review/round3/referee/ggww.out`):

```text
near threshold: sigma(gg->WW)/beta = 14.9998 pi a^2/M^2 ; sigma v_rel (W+W- -> gg) = 6.6666 pi a^2/M^2
```

Here gg denotes the pair of gauge bosons (hidden photons, in the application to W′), a the coupling and beta the velocity. In the audit table (Step 2) the row reads:

> W' overclosure | 1e16-1e17 (coef x10 bracket) | c=1..10: 9.4e15-1.95e17; with c=6.67 (W+W- -> gg at threshold, own detailed balance of hep-ph/9405359 eq. 5.15; scalar check gives textbook 2.000): 1.3e16-4.0e16 | CONFIRMED (bracket reasonable)

The "scalar check" is the referee's test of the method on scalar pair production, where it reproduced the textbook coefficient 2. On the brackets the referee adds: "annihilation coefficient factor-10 bracket - reasonable (my W'W'->g'g' threshold coefficient 6.67 pi a^2/m^2 lies inside 1-10; extra channels h'h', g'h' push up)". The extra channels h′h′ and g′h′ are final states containing the hidden Higgs boson h′ (the wiki's reading of the labels); they add to the rate. With the computed coefficient the overclosure is "1.3e16-4.0e16", inside the gated range.

## A colder hidden sector

#14 also required the hidden sector to be colder than ours, a temperature ratio ξ below 0.77 (corrected in round 3 to 0.760), so that its massless photon does not add too much radiation ([the hidden sector's thermal history](/wiki/dark-matter/candidates/soliton-candidate/hidden-thermal-history)). The W′ freeze-out had been computed only at equal temperatures; the worklog says so ("Computed at ξ = 1 only. The effect of a colder dark sector on the W′ freeze-out is not scripted"), and the round-3 [pre-registration](/wiki/method/review/round-3/preregistration) named it the second runner-up weakest link: "Thermal-history consistency. The W′ and ψ freeze-out are computed at ξ = 1, but dark radiation requires ξ < 0.77".

The referee recomputed it at the required ratio (Step 4(a) item 4): "W' overclosure survives (xi=0.76: 9.9e15 - 2.9e16, step4b.out)". The exclusion holds in the colder sector as well.

## What it forced

#14 §3 states the repair directly after the negative result: "The fix is the Dirac doublet psi: W'+ can decay to a psi pair." The doublet ψ has U(1)_d charges ±g_d/2 (§2), and, being light, gives the W′± a decay channel into ψ pairs. It became the first of v3's three "Requirements forced by consistency (not optional)": "(i) at least one hidden doublet fermion with mass between the MeV scale and ~0.1 TeV" (§6). The worklog's item O1 lists what the addition brought with it:

- the sector becomes "SU(2)_d → U(1)_d with at least one light dark doublet";
- ψ is itself stable and a thermal relic, so its mass had to keep it a minor component; that mass window was later found wrong at both edges ([Obituary: the ψ relic window](/wiki/dark-matter/candidates/soliton-candidate/psi-relic-window));
- ψ carries a small visible charge if the two photons mix, unless hidden charge conjugation is gauged ([kinetic mixing between sectors](/wiki/dark-matter/candidates/soliton-candidate/kinetic-mixing));
- its plasma is the medium for monopole–antimonopole annihilation, which fed acceptance criterion 3 ([Obituary: the √N topological floor](/wiki/dark-matter/candidates/soliton-candidate/sqrt-n-floor));
- if lighter than about an MeV it would add radiation at nucleosynthesis ("not yet scripted").

It also changed which charge the coupling hypothesis H refers to. The worklog's 'v3 as drafted' section: "The light doublet (O1) makes ψ's charge g_d/2 the smallest dark charge. H matches *that* charge to ours, so α_W′ = 4α ≈ 1/34 and the monopoles' coupling is α_m = 1/α_W′ = 1/(4α) ≈ 34 exactly, by Dirac quantization relative to ψ" ([Obituary: the coupling α_d ≈ 34](/wiki/dark-matter/candidates/soliton-candidate/alpha-d-coupling)).

## Scope

- **Conditional on the benchmark.** The numbers are computed at M = 3×10¹³ GeV, which round 3 found overproduced by the Kibble mechanism ([overproduction at the benchmark](/wiki/dark-matter/candidates/soliton-candidate/overproduction)). The sources evaluate the W′ relic only near this scale: at v3's m_W′ ≈ (5–9)×10¹¹ GeV and, in the worklog, at an earlier stage's 1.2–2.2×10¹¹ GeV. What survives the candidate is the statement that the minimal sector is excluded; no source states the overclosure at other masses.
- **Equal or colder temperatures.** The exclusion holds at ξ = 1 and at ξ = 0.76.
- **Ordinary kinematics.** Like all of #14, the calculation treats the hidden sector with "ordinary relativistic quantum field theory" (§1).

## History

1. **Worklog item O1**, headed "dark W′± fate: fatal to the minimal model, not to the candidate", computed in the predecessor script `knot_numbers.py`. Its anchor then was "100 GeV with σv = 2.2×10⁻²⁶ cm³/s gives Ω h² = 0.108". At that stage (F1 and F2 are the worklog's findings on the mass window and on which coupling sets the monopole mass), "Under F1 and F2, m_W′ = α M\*/f = 1.2–2.2×10¹¹ GeV", and the relic was "0.8–15×10¹⁶ × the observed density, bracketing the annihilation coefficient κ = 1–10 and f = 1–1.787". These stage numbers were never reconciled with #14's; the current record cites #11, the adjudication and the gate ([conflicts between sources](/wiki/history/documents/source-conflicts)).
2. **v3 as drafted** (2026-10-19). The gated check corrected a planned figure before the text was written: "the minimal model overcloses by 10¹⁶–10¹⁷ (not 10¹⁵–10¹⁷)". The abstract states it as the first consistency requirement: "without it, stable hidden W bosons overclose the universe by a factor of 1e16 to 1e17", and §6 lists "the failure of the adjoint-only model" among the results "Derived within the framework or by standard methods".
3. **Round 3** (2026-10-19). The referee confirmed the number (Step 2) and its survival at ξ = 0.76 (Step 4(a)); no ruling touched it ([round-3 verdict and rulings](/wiki/method/review/round-3/rulings)).
4. **After the retirement.** The adjudication lists it among what survives v3, #11 v2.1 §12 carries it with [V], and `verify/soliton_obituary.py`, which replaced the predecessor script, keeps it under the heading "Minimal adjoint-only sector (survives, benchmark-conditional)" ([Obituary: superheavy conjugate solitons](/wiki/dark-matter/candidates/soliton-candidate/obituary)).

## Sources

- `papers/broken-born-checkpoint-v2.md` §12 — the surviving statement, tagged [V]
- `review/round3-adjudication.md` 'What survives v3' — listed as surviving, as a statement and as benchmark-conditional arithmetic
- `verify/soliton_obituary.py` — the gated check, its inputs and its anchor
- `review/round3/referee/audit-notes.md` Step 2 — v, m_W′ and the overclosure recomputed, and the bracket judged; Step 4(a) item 4 — the colder-sector values
- `review/round3/referee/ggww.out` — the coefficient by detailed balance
- `review/round3-preregistration.md` 'Predictions' — the thermal-history runner-up
- `review/v3-worklog.md` 'New open items' (O1) — how it was found and what the fix brought; 'v3 as drafted (2026-10-19)' — the corrected figure and which charge H matches
- `notes/knot-dark-matter-standalone.md` §1 — ordinary kinematics; §2 — the sector; §3 — the argument, the masses and the fix; §6 — requirement (i)
