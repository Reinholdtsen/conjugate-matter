---
title: "The CPL parametrization w(a) = w₀ + wₐ(1 − a)"
weight: 15
status: established
description: "The two-number Chevallier–Polarski–Linder form of the dark-energy equation of state: a first-order expansion in the scale factor, the meaning and sign of w₀ and wₐ, the pivot form, what two numbers cannot represent, where thawing models and phantom crossings lie in the w₀–wₐ plane, the program's corridor inside the crossing region (flag 43), and how the program states row 4 in its terms."
provenance: [T]
sources:
  - "papers/broken-born-checkpoint-v2.md §10"
  - "papers/broken-born-checkpoint-v2.md §13 row 4"
  - "papers/broken-born-checkpoint-v2.md refs [19], [21]"
  - "CLAUDE.md 'Since the handoff'"
  - "review/round3/referee/audit-notes.md Step 4(c) item 11"
  - "notes/broken-born-theory.md §7"
  - "notes/broken-born-theory.md §9"
  - "notes/broken-born-program-v1.md §8"
  - "notes/broken-born-program-v1.md §9"
  - "review/wiki-build-flags.md item 27"
  - "review/wiki-build-flags.md item 43"
  - "review/wiki-build-flags.md items 27 (addendum), 46"
  - "notes/closed-universe.md §2"
---

*The Chevallier–Polarski–Linder (CPL) parametrization is the standard way to describe, with two numbers, how the equation of state w of dark energy, its pressure divided by its energy density, changes as the universe expands: w(a) = w₀ + wₐ(1 − a), where a is the scale factor, the size of the universe relative to its size today. w₀ is the value of w today and wₐ measures how it has drifted; a [cosmological constant](/wiki/cosmology/dark-energy/cosmological-constant) is the point w₀ = −1, wₐ = 0. Cosmological surveys commonly report their dark-energy results in this form, and the program states its dark-energy requirement in it: a [thawing field](/wiki/cosmology/dark-energy/thawing-and-freezing), with w₀ > −1 and wₐ < 0, that is never phantom, meaning that w never falls below −1. The form is a straight line in the scale factor, an approximation to the true history rather than a physical model. The second data release of the [Dark Energy Spectroscopic Instrument](/wiki/cosmology/dark-energy/desi) (DESI) favours a w that crosses −1, lying below it earlier in cosmic history, at [redshifts](/wiki/cosmology/scale-factor-duality/redshift) above about 0.4, and above it since, and calls that preference "rather independent of parametrization choices". The crossing stands against the program's requirement and puts its dark-energy sector under real pressure. In these terms the favoured shape has w₀ > −1 with w₀ + wₐ < −1, although a CPL fit in that region does not by itself show a crossing, since a line fitted to a field that never falls below −1 can lie there too (flag 43 in `review/wiki-build-flags.md`).*

**Status:** Established — [T] — textbook cosmology, written here from general knowledge, with the literature it names marked † (Chevallier and Polarski 2001 †; Linder 2003 †; Albrecht et al. 2006 †); no `verify/` script checks it. The program's uses of the form are stated in [checkpoint #11](/wiki/history/documents/checkpoint) §10, in a paragraph tagged [D + T], and in §13 row 4; the DESI release they are read against is live-searched [21S]. Where the program's corridor lies relative to that release's crossing is flag 43 in `review/wiki-build-flags.md`, confirmed by two independent checks kept outside [the gate](/wiki/method/verification/the-gate).

## The form [T]

### Why two numbers

A survey of the expansion does not see w directly. It measures distances and expansion rates at a set of redshifts, and w enters them only through integrals over the expansion history ([DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi#from-distances-to-wz-t)). Data of this kind cannot fix a whole function, so a changing w is described by a few parameters. A constant w is the one-parameter description; the CPL form adds a second number for the drift.

### A first-order expansion in the scale factor

The scale factor a is the factor by which distances between distant galaxies have grown, normalized to a = 1 today ([Friedmann cosmology and minisuperspace](/wiki/cosmology/scale-factor-duality/friedmann-cosmology)). Expanding w about today and keeping the first-order term gives

```text
w(a) ≈ w(1) + w′(1)·(a − 1)        with w′ = dw/da

w₀ = w(1)        wₐ = −w′(1)

w(a) = w₀ + wₐ(1 − a)
```

The CPL form takes the truncated expansion as the definition of w at every a (Chevallier and Polarski 2001 †; Linder 2003 †). An earlier two-parameter form, linear in redshift, w = w₀ + w₁z with w₁ a constant, grows without bound at high redshift; the form linear in a stays bounded at high redshift, which Linder (2003 †) gave as a reason to prefer it.

### In redshift

The redshift z of light emitted when the scale factor was a satisfies 1 + z = 1/a. In redshift the form reads

```text
w(z) = w₀ + wₐ · z/(1 + z)
```

Near today w ≈ w₀ + wₐz, so wₐ is also the slope dw/dz at z = 0. In the distant past, as z grows without limit and a tends to 0, w tends to w₀ + wₐ. The form is therefore a straight line in a that joins two values: w₀ + wₐ at a = 0 and w₀ today.

### What w₀ and wₐ mean

- **w₀** is the equation of state today. w₀ = −1 is the value of a cosmological constant; w₀ > −1 means that the dark-energy density is falling as space expands, and w₀ < −1 that it is rising, the phantom behaviour ([the phantom divide and the null energy condition](/wiki/cosmology/dark-energy/phantom-divide)).
- **wₐ** is the drift. Since dw/da = −wₐ, a negative wₐ means that w rises as the universe expands: w was lower in the past and has been rising toward the present. A positive wₐ means that w falls as the universe expands, and wₐ = 0 is a constant w.
- The **cosmological constant** is the single point (w₀, wₐ) = (−1, 0) of the w₀–wₐ plane ([the cosmological constant Λ](/wiki/cosmology/dark-energy/cosmological-constant#testing-for-a-departure-from-w--1)).

### The density it implies

Each component of the universe that exchanges no energy with the others obeys the continuity equation ρ̇ = −3H(ρ + p), with H the expansion rate ([quintessence and the equation of state](/wiki/cosmology/dark-energy/quintessence#expansion-and-the-friedmann-equation-t)). For the CPL w it integrates in closed form:

```text
ρ_DE(a) = ρ_DE,0 · a^{−3(1 + w₀ + wₐ)} · exp[−3wₐ(1 − a)]
```

where ρ_DE is the dark-energy density and ρ_DE,0 its value today. The closed form is one reason the parametrization is convenient in fits. Two properties follow from it.

- **The density keeps its sign.** Both factors are positive for every a > 0, so CPL dark energy with a positive density today never reaches zero or negative density.
- **Early times.** At small a the density scales as a^{−3(1 + w₀ + wₐ)}. If w₀ + wₐ > 0 it grows into the past faster than the matter density, which scales as a⁻³, and the dark energy would overtake the matter at early times. Analyses commonly restrict the parameters to w₀ + wₐ < 0 for that reason.

## The pivot form [T]

In a fit to data, w₀ and wₐ are strongly correlated. The data determine w best at some epoch in the past rather than today, and many pairs (w₀, wₐ) give nearly the same w there, a change in one being offset by a change in the other. The region the data allow in the w₀–wₐ plane is approximately a long, narrow ellipse.

The same straight line can be labelled by its value at another point, a pivot scale factor a_p:

```text
w(a) = w_p + wₐ(a_p − a)        w_p = w₀ + wₐ(1 − a_p)
```

The family of lines is unchanged: w_p is the value of w at a_p, and wₐ is the same drift. What changes is the correlation of the errors. With Var and Cov the variance and covariance of the fitted parameters,

```text
Var(w_p) = Var(w₀) + 2(1 − a_p)·Cov(w₀, wₐ) + (1 − a_p)²·Var(wₐ)
```

This is smallest at 1 − a_p = −Cov(w₀, wₐ)/Var(wₐ), and at that pivot Cov(w_p, wₐ) = 0. The pivot chosen this way is the epoch at which the data determine w best, and there the errors of w_p and wₐ are uncorrelated, which is why the pivot form is called decorrelated. The pivot belongs to the data set, not to the dark energy: different combinations of data have different pivots.

Because the change from (w₀, wₐ) to (w_p, wₐ) preserves areas in the plane, the area of the error ellipse is proportional to σ(w_p)·σ(wₐ), with σ a standard deviation. The Dark Energy Task Force used the inverse of that area as a figure of merit to compare planned surveys (Albrecht et al. 2006 †).

## What two numbers cannot represent [T]

The form is a straight line in a, and that fixes what it can describe.

- **One direction of change.** A CPL w(a) is monotonic. It cannot rise and then fall, oscillate, or change quickly at one particular epoch, since its change is spread evenly over a. A w(a) with such features is represented by the straight line that fits it best over the range of the data.
- **At most one crossing of −1.** A straight line meets the level w = −1 at most once, unless it is the constant −1 of the cosmological constant.
- **The early value is an extrapolation.** w₀ + wₐ is the value of the line at a = 0, the limit of infinite redshift. Dark energy is a small part of the total density at high redshift, so the data constrain w mainly at low redshift, and w₀ + wₐ is fixed by the value and slope fitted there.
- **Curved histories.** A thawing field has w close to −1 for most of the expansion history and rises only late, so its w(a) is curved, not straight. A straight line fitted to it over the redshifts the data cover follows the late rise, and extended back to a = 0 it can pass below −1, although the field itself never goes below −1. For fields with the program's potential, flag 43 in `review/wiki-build-flags.md` reports executed checks of this ([the corridor and DR2's crossing](#the-corridor-and-dr2s-crossing)). The values of (w₀, wₐ) assigned to a given model also depend on the redshift range and precision of the data used to fit it.
- **Density through zero.** The equation of state w = p/ρ has no finite value when the density passes through zero while the pressure does not, and the CPL density keeps its sign at every a. A dark energy whose density turns negative, which a turnaround of a flat universe requires ([recollapse](/wiki/cosmology/dark-energy/quintessence#recollapse-t)), therefore has no CPL description. Extended into the future, a > 1, the form has no physical meaning either: with wₐ < 0 the line rises without bound.

## Thawing models in the w₀–wₐ plane

A thawing field is held near w = −1 by the expansion at early times and starts to change late, so w rises toward the present ([thawing and freezing](/wiki/cosmology/dark-energy/thawing-and-freezing)). With w₀ on the horizontal axis and wₐ on the vertical, its CPL point has w₀ > −1 and wₐ < 0: it lies to the right of the cosmological-constant point and below it, in what this page calls the thawing quadrant. A freezing field, whose w falls toward −1, has w₀ > −1 and wₐ > 0 and lies to the right of that point and above it [T].

Thawing models do not fill their quadrant. When w stays close to −1, the late rise of w has a similar shape for many potentials, so thawing models fall in a narrow band through the point (−1, 0) [T]. The program writes that band as a line, the "thawing corridor wₐ ≈ −1.5(1 + w₀)" (#11 §10). The [lab notebook](/wiki/history/documents/lab-notebook) calls it "the standard thawing corridor" (#1 §7 item 2, transcribed from its LaTeX), and [the v1 paper](/wiki/history/documents/checkpoint) gives the same form (#9 §8). No document gives a reference for the corridor or its slope, and the wiki has not checked the slope against the literature.

The predictions tables of #1 and #9 place the requirement "on the thawing corridor" (#1 §9 row 5; #9 §9 row 4). #11's row 4 keeps only the signs, w₀ > −1 and wₐ < 0 (#11 §13 row 4; [history of the predictions table](/wiki/predictions/table-history)).

The corridor is stated in CPL parameters; in this wiki's reading it therefore describes fitted points, and the limits of the previous section apply to it: the line fitted to a thawing field approximates a curve that itself stays at or above −1. Flag 43 in `review/wiki-build-flags.md` records that every point of the corridor lies in the region, described in the next section, in which a CPL line passes below −1 in the past, and that no document says so ([the corridor and DR2's crossing](#the-corridor-and-dr2s-crossing)).

## A phantom crossing in the w₀–wₐ plane [T]

A CPL w(a) equals −1 at the scale factor a_c where

```text
w₀ + wₐ(1 − a_c) = −1        a_c = 1 + (1 + w₀)/wₐ
```

For w₀ > −1 and wₐ < 0 the crossing lies in the past, 0 < a_c < 1, exactly when w₀ + wₐ < −1. Such a fit has w below −1 at early times and above −1 today: it crosses the phantom divide once, from the phantom side to the ordinary side. The mirror case, w₀ < −1 with w₀ + wₐ > −1, is a crossing in the other direction, into the phantom regime by today.

The thawing quadrant therefore holds two kinds of fit, separated by the line w₀ + wₐ = −1 through the cosmological-constant point: fits with w₀ + wₐ ≥ −1, whose line stays at or above −1 back to a = 0, and fits with w₀ + wₐ < −1, whose line crosses. The signs of w₀ and wₐ alone do not distinguish a thawing drift from a crossing.

A single canonical scalar field, the kind quintessence uses, cannot cross −1 in either direction while its energy density is positive, because its ρ + p is the square of its rate of change ([the phantom divide and the null energy condition](/wiki/cosmology/dark-energy/phantom-divide)). A CPL point in the crossing region describes a line that no such field follows exactly. By the previous sections, a line fitted to a thawing field can itself fall in that region. Flag 43 in `review/wiki-build-flags.md` reports such fits for fields with the program's potential and places the program's corridor in the same region ([the corridor and DR2's crossing](#the-corridor-and-dr2s-crossing)).

## DESI Data Release 2 in these terms

#11 §10 quotes the paper of DESI's second data release (Data Release 2, DR2): in every dataset combination "the favored w(z) shows a phase of w > −1 at low redshifts and a phantom crossing to w < −1 above redshifts z ≃ 0.4", and this preference "is thus rather independent of parametrization choices made in the analysis" [21S]. The shape is the one the CPL plane assigns to w₀ > −1 with w₀ + wₐ < −1. The [round-3](/wiki/method/review/round-3) referee, quoting the release, notes that models respecting the null energy condition "can somewhat outperform" the cosmological-constant model but are disfavoured relative to the w₀–wₐ fit (`review/round3/referee/audit-notes.md` Step 4(c) item 11). The measurement and its route into the program are on [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing).

#11 §10 draws the consequence for the program (DR3 is DESI's Data Release 3):

> The framework's strict w ≥ −1 therefore stands against the direct reading of the data. It survives on two points: non-phantom quintessence fits remain compatible [19S], and w(z) is inferred from distances rather than observed, as [21S] also notes. DR3 is the decisive test (§13, row 4).

The same paragraph summarizes the fits as "compelling evidence for weakening dark energy with phantom behavior less significant (non-phantom compatible at ~2σ)" [19S, 20S, 21S] (#11 §10).

How w is fitted bears on this reading in two ways.

- **The form.** A CPL point in the crossing region does not by itself show that dark energy crossed −1, since a line fitted to a model that never crosses can fall there. The DR2 paper's statement that the preference "is thus rather independent of parametrization choices made in the analysis" says that the crossing shape does not rest on the CPL form alone. Flag 43 in `review/wiki-build-flags.md` applies the first point to the program's own corridor, which lies in the crossing region, and finds the difference from DR2's fits in the slope ([the corridor and DR2's crossing](#the-corridor-and-dr2s-crossing)).
- **Inference.** #11's second point is broader: whatever form is chosen, w(z) is fitted to distances, not observed ([DESI baryon acoustic oscillations](/wiki/cosmology/dark-energy/desi)). The program's kill condition counts only a "robust intrinsic w < −1" (#11 §13 row 4).

In this wiki's reading, both points concern whether the data meet the kill condition; neither is evidence for the program's bound. The root `CLAUDE.md` states the position: "DESI DR2 favors a phantom crossing above z ≈ 0.4, against the framework's strict w ≥ −1 (§10). The dark-energy sector is under real pressure ahead of DR3" ('Since the handoff').

Before the round-3 review the lab notebook read DESI's results by their signs: w₀ > −1, wₐ < 0 "is the *sign pattern DESI reports*" (#1 §7 item 2, transcribed from its LaTeX). That reading is superseded ([the earlier readings of DESI](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing#superseded-the-earlier-readings-of-desi)).

## The corridor and DR2's crossing

No program document places the corridor relative to the crossing region. Flag 43 in `review/wiki-build-flags.md` does, and it awaits Paul's ruling ([pending rulings](/wiki/status/open-problems#pending-rulings)); this section reports what the flag and its audit state, without derivations of its own. The flag calls the region w₀ > −1 with w₀ + wₐ < −1 a quadrant; on this page it is the crossing region.

- **The corridor lies in the crossing region.** On the corridor wₐ = −1.5(1 + w₀), the flag gives w₀ + wₐ + 1 = −(1 + w₀)/2, "which is negative for every w₀ > −1". Every corridor point therefore has w₀ > −1 and w₀ + wₐ < −1, the region in which DR2's fits lie [21S].
- **The documents do not relate the two.** #11 §10 "states the corridor and DR2's crossing in one paragraph without relating them", and the lab notebook "compares signs only" ("the sign pattern DESI reports", #1 §7 item 2).
- **The region comes from the line.** In the flag's words, "The quadrant comes from the straight line, not from the field." Fields with the potential of [τ](/wiki/cosmology/dark-energy/tau-quintessence), the program's dark-energy field, V₀[1 + cos(τ/f)], that never fall below −1, integrated numerically (36 histories in one audit, 88 in the other), give CPL fits in the crossing region under every fitting convention tried, with −wₐ/(1 + w₀) from about 1.4 to 2.4, and up to 3.9 when the matter density is fitted without an anchor from the [cosmic microwave background](/wiki/cosmology/early-universe/cosmic-microwave-background).
- **The slope separates the corridor from DR2.** The slope sets where the line crosses −1. In the flag's figures, the corridor's line crosses at z = 2 for every w₀; DR2's fits cross at z ≈ 0.35–0.50, with −wₐ/(1 + w₀) ≈ 3.0–3.8, from Table 5 of the DR2 paper, which one auditor fetched by live search [S]. The flag's rough Gaussian approximation, built from the pivot values DR2 quotes, puts the corridor line outside DR2's 95% region for two of its dataset combinations, both including cosmic-microwave-background data.

The flag concludes that the pressure described by #11 §10 and the root `CLAUDE.md` stands: "It rests on the crossing redshift (DR2 calls the preference 'rather independent of parametrization choices'), not on the quadrant, which a field that never crosses can also occupy." The flags file states what follows for the program: "This bears on how row 4's pressure is stated, not on whether it exists" ([row 4](/wiki/predictions/dark-energy-drift)). The flag's audit confirmed it by two independent checks, one defending the documents and one recomputing from scratch. Both found the algebra right, the observation absent from every document, and the region shared with the fits of a field that never crosses; the defending check adds that the corridor's slope, not its region, keeps it away from DR2's crossing, and the audit finds #11 §10's defence consistent with this. The auditors' scripts and outputs are in `review/wiki-build-checks/corridor/`, outside the gate.

## How the program uses the form

- **Row 4's requirement.** [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) states the requirement in CPL parameters: "Thawing, w₀ > −1, wₐ < 0, never phantom; drift persists in DESI DR3", with the kill conditions "DR3+ constant −1 (kills τ-sector); robust intrinsic w < −1 (kills outright) — DR2 already favors a crossing above z ≈ 0.4 (§10)" (#11 §13 row 4). In the plane, the requirement's signs, w₀ > −1 and wₐ < 0, are the thawing quadrant, and the first kill condition is data that converge on the cosmological-constant point (−1, 0). The thawing quadrant contains the crossing region, where flag 43 places the corridor ([the corridor and DR2's crossing](#the-corridor-and-dr2s-crossing)). In this wiki's reading, "never phantom" concerns the field's own w, which a CPL line approximates; the [lab notebook](/wiki/history/documents/lab-notebook)'s version of the kill condition counts a w < −1 only "as an intrinsic equation of state, not an artifact of an assumed ΛCDM background" (#1 §7 item 1), ΛCDM being the standard model of a cosmological constant plus cold dark matter ([the no-phantom bound w ≥ −1](/wiki/cosmology/dark-energy/no-phantom-bound)).
- **The field.** The program's dark energy is [τ](/wiki/cosmology/dark-energy/tau-quintessence), a [hilltop quintessence](/wiki/cosmology/dark-energy/thawing-and-freezing#hilltop-models) field, one that starts near the maximum of its potential V₀[1 + cos(τ/f)], where V₀ sets the potential's height and f its angular scale. #11 §10 places τ on the thawing corridor.
- **The over-constraint.** #11 §10 counts "two parameters (f, τᵢ) for three observables (w₀, wₐ, t_turn) — one over-constraint", τᵢ being the field's initial value, with V₀ "fixed by Ω_DE", the fraction of the universe's energy density in dark energy today (#1 §7 item 4). Two of the three observables are CPL parameters. The third, t_turn, the time at which the expansion halts and reverses, is not: a turnaround of a flat universe needs a negative dark-energy density, which the CPL form cannot describe, and V₀[1 + cos(τ/f)] is never negative for V₀ > 0, a conflict that remains unresolved ([Open: the sign of V(τ) and the turnaround](/wiki/cosmology/dark-energy/potential-sign); flag 27 in `review/wiki-build-flags.md`). The flag's addendum (2026-10-27) finds that a closed universe turns around with V ≥ 0, curvature reversing the expansion; there t_turn = (π/2)(Ω_m + Ω_d)|Ω_k|^{−3/2}/H₀ scales as |Ω_k|^{−3/2} at fixed (w₀, wₐ), so the curvature is a third input and the over-constraint moves rather than vanishing (flag 46; [a closed Comatter universe](/wiki/cosmology/scale-factor-duality/closed-universe#the-over-constraint-moves-dv)). In the same note a fit of the w₀wₐ family with free curvature is found to be a poor proxy for the program's model, because its looser bound comes from the phantom crossing that w ≥ −1 forbids ([what the data say](/wiki/cosmology/scale-factor-duality/closed-universe#what-the-data-say)). No program document computes (w₀, wₐ) from (f, τᵢ) ([the dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint)).

## Used by

- [Row 4: thawing dark energy, never phantom](/wiki/predictions/dark-energy-drift) — the requirement w₀ > −1, wₐ < 0, never phantom.
- [τ: hilltop quintessence on the Maslov circle](/wiki/cosmology/dark-energy/tau-quintessence) — τ thaws along the corridor wₐ ≈ −1.5(1 + w₀).
- [The dark-energy over-constraint](/wiki/cosmology/dark-energy/over-constraint) — w₀ and wₐ, two of its three observables.
- [DESI DR2's phantom crossing](/wiki/cosmology/dark-energy/desi-dr2-phantom-crossing) — the favoured shape, w₀ > −1 with w₀ + wₐ < −1 in these terms.

## Sources

- `papers/broken-born-checkpoint-v2.md` §10 — the thawing corridor, the over-constraint, the state of the fits, DR2's crossing and its independence of parametrization, the two points on which the framework survives; §13 row 4 — the requirement and the kill conditions in w₀ and wₐ
- `papers/broken-born-checkpoint-v2.md` refs [19], [21] — the non-phantom fits and DESI DR2 Results II (live-searched)
- `CLAUDE.md` 'Since the handoff' — the dark-energy sector "under real pressure ahead of DR3"
- `review/round3/referee/audit-notes.md` Step 4(c) item 11 — models respecting the null energy condition against the w₀–wₐ fit
- `notes/broken-born-theory.md` §7 items 1, 2 and 4 — the intrinsic-versus-artifact qualification, "the standard thawing corridor" and "the sign pattern DESI reports", V₀ fixed by Ω_DE; §9 row 5 — "on the thawing corridor"
- `notes/broken-born-program-v1.md` §8 — the corridor; §9 row 4 — "on the thawing corridor"
- `review/wiki-build-flags.md` item 27 — the potential as written cannot turn negative, with its addendum on the closed turnaround; item 46 — the over-constraint moved to Ω_k; item 43 — the corridor in the crossing region, the fits of fields that never cross, the slope that separates the corridor from DR2's fits, and the audit's verdict, with the auditors' scripts and outputs in `review/wiki-build-checks/corridor/`
- `notes/closed-universe.md` §2 — t_turn in a closed universe, the over-constraint, and w₀wₐ with free curvature as the wrong proxy
