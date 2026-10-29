---
title: "The Born length λ"
weight: 100
status: alive
description: "The reference length λ, with its momentum scale ε = ℏ/λ, that position and momentum need in order to share one geometry: why the exchange of the two needs it, what it does to a phase-space rectangle, #13's name for it and its role in the maximum force c̃ = ℏc/λ², #13's untagged identification of it with the Planck length, the program's action that fixes none, the excluded self-dual length of about 50 μm, and Born's own particle-scale length."
sources:
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md Abstract"
  - "papers/conjugate-special-relativity.md §4"
  - "papers/conjugate-special-relativity.md §6"
  - "papers/conjugate-special-relativity.md §7"
  - "papers/conjugate-special-relativity.md References [3]–[4]"
  - "notes/broken-born-theory.md §2"
  - "notes/broken-born-theory.md §3"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "review/v3-worklog.md 'New open items' O3"
  - "review/round3/referee/audit-notes.md Step 1"
  - "papers/broken-born-checkpoint-v2.md §14"
  - "CLAUDE.md 'Layout'"
  - "CLAUDE.md 'Since the handoff'"
  - "popsci/angle-of-the-mirror.md 'Corollaries and daydreams'"
  - "popsci/universes-other-half.md 'A second speed of light'"
  - "review/wiki-build-flags.md item 17"
  - "papers/phase-space-diameter.md §4"
  - "papers/phase-space-diameter.md §5"
  - "papers/phase-space-diameter.md §6"
  - "papers/phase-space-diameter.md §7"
  - "papers/phase-space-diameter.md §8"
  - "papers/phase-space-diameter.md §9"
  - "verify/phase_space_diameter.py"
  - "review/round5-adjudication.md header"
  - "review/round5-preregistration.md 'Predictions'"
  - "notes/phase-space-diameter-worklog.md 'Status'"
  - "notes/closed-universe.md §4"
  - "notes/closed-universe.md §7"
  - "review/wiki-build-flags.md items 48, 49"
  - "notes/closed-universe.md §5"
---

*The Born length λ is a reference length that, together with Planck's constant ℏ, puts position and momentum on a common scale: positions are counted in units of λ and momenta in units of ε = ℏ/λ. A length and a momentum have different units, so a geometry that combines them, or a map that exchanges them such as [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), has a meaning only once some such pair of scales is chosen. The name comes from #13, the program's paper on [conjugate special relativity](/wiki/conjugate-relativity), in which λ fixes the slope of the momentum-space light cone and with it the [maximum force](/wiki/conjugate-relativity/maximum-force), c̃ = ℏc/λ². #13 sets λ equal to the [Planck length](/wiki/gravity/spin-2-fields/planck-units), in one sentence that carries no tag, and the maximum force becomes c⁴/G. The program's [lab notebook](/wiki/history/documents/lab-notebook) writes its phase-space structures in units in which the same pair of scales is 1, without naming λ or giving it a value. The phase-space-diameter note finds that the program's action singles out no Born length, so that the value is a choice, and it excludes the length that would make the universe's range of scales exactly symmetric under the exchange, about 50 micrometres: as the Born length it would cap every force near 10⁻¹⁷ newtons ([Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)). Born's own reciprocity length, in his papers of 1938 and 1949, was a particle scale. The identification with the Planck length is alive but unreviewed: no review round has examined #13, no script tests the identification, and the [checkpoint #11](/wiki/history/documents/checkpoint) does not mention the Born length.*

**Status:** Alive, unreviewed — #13 §1 names λ the Born length and sets it equal to the Planck length, both without a tag; the [Planck closure](/wiki/conjugate-relativity/invariant-length-shell#planck-closure) evaluated at that value is [D] (#13 §4). The need for a reference length when position and momentum share one geometry is [T], written here from general knowledge, and #13 cites Born's hope for a fundamental length from model memory [3†, 4†]. The phase-space-diameter note (`papers/phase-space-diameter.md` v1.1) adds that the program's action singles out no λ [D] (§5) and excludes the self-dual length √(l_P L) as the Born length [D][V] (§8.1), with every number computed in `verify/phase_space_diameter.py` ([the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)); it also retrieved and read Born's 1938 and 1949 papers [S] (§4). That script computes c⁴/G = 1.21 × 10⁴⁴ N, the arithmetic of #13's value; nothing tests the identification itself. No [blind review](/wiki/method/review) round has covered #13; [round 5](/wiki/method/review/round-5) reviewed the diameter note. #11 v2.3 does not mention the Born length. `HANDOFF.md` §2 lists the maximum force that the identification fixes among the alive results, without the ✓ of a machine-checked item.

## What the Born length is

#13 §1 introduces the length in the bound set by the momentum-space light cone, |dp/dt| ≤ c̃ = ε/(λ/c) = ℏc/λ²:

> "where λ is the Born length and ε = ℏ/λ its conjugate momentum scale."

The Abstract gives the maximum force "at the Planck value of the Born length". The term occurs in no other document of the program. It names a pair of scales:

- **λ**, a length;
- **ε = ℏ/λ**, a momentum, the one that ℏ assigns to the length λ, so that λε = ℏ.

The pair converts lengths into momenta and back, which any statement exchanging the two needs, and in #13 it also fixes c̃, the invariant "speed" of the momentum-space cone, which has the units of a force.

## Why position and momentum need a reference length [T]

A position is a length and a momentum is a mass times a velocity, so the two cannot be added, compared or exchanged until each is divided by a reference scale of its own kind [T]. The phase-space metric H adds squared position to squared momentum ([P1: the phase-space arena](/wiki/program/postulates/p1-arena#the-generalized-metric-h)), and Born reciprocity, ρ: (x, p) → (p, −x), turns a length into a momentum, so each is a statement about scaled coordinates.

### Scaled coordinates

With a length λ and the momentum ε = ℏ/λ, the scaled coordinates and the exchange read [T]:

```text
ξ = x/λ        π = p/ε        ε = ℏ/λ

ρ:  (ξ, π) → (π, −ξ)

in ordinary units:    x′ = (λ²/ℏ) p        p′ = −(ℏ/λ²) x

[ξ, π] = [x, p]/(λε) = iℏ/(λε) = i
```

The new position is the old momentum converted into a length, and the new momentum is the old position, reversed, converted into a momentum. The conversion factors depend on λ, so each choice of λ gives a different quarter-turn of phase space.

### What kinematics fixes and what it leaves free

Three facts follow [T]:

- **The choice ε = ℏ/λ absorbs ℏ.** In the scaled coordinates the commutator is [ξ, π] = i, so ℏ disappears into the units and one free scale remains, λ ([the canonical commutator](/wiki/phase-space/reciprocity/canonical-commutator)).
- **Kinematics singles out no λ.** The commutator [x, p] = iℏ is unchanged by the map above for every value of λ, because the two conversion factors cancel. Quantum kinematics is invariant under each of these quarter-turns, and the [Fourier transform](/wiki/phase-space/reciprocity/fourier-transform), written in the scaled coordinates of a given λ, implements the corresponding one.
- **A law of motion can single one out.** A law of motion that is unchanged by one of these maps and not by the others must contain that map's length, either as a constant of its own or built from its constants. The harmonic oscillator is the standard example: its mass and frequency, with ℏ, give a length that sets the width of its ground state, and in units of that length and of ℏ divided by it the oscillator's evolution is a rigid rotation of phase space, a quarter-period of which is the Fourier transform. That length belongs to one oscillator, and a different oscillator has a different one.

In ordinary quantum mechanics the reference length is therefore a convenience, chosen to suit the system at hand.

### A rectangle keeps its area and inverts its shape

The phase-space-diameter note applies the map to a rectangle of phase space, a region of extent L in position and P in momentum (§5, [T][V]). The map written above in ordinary units, ρ_λ, sends it to a rectangle of extents (λ²P/ℏ, ℏL/λ²), so

```text
area:           L·P  →  L·P                          for every λ
aspect ratio:   A = (L/λ)/(P/(ℏ/λ)) = ℏL/(λ²P)  →  1/A
self-dual:      A = 1   exactly when   λ² = ℏL/P
```

The aspect ratio is measured in units of λ: a length in units of λ against a momentum in units of ℏ/λ. The note draws two consequences [D][V]:

- every rectangle is self-dual for exactly one λ, the geometric mean of L and ℏ/P;
- reciprocity maps with two Born lengths differ by a squeeze, ρ_{λ₁}ρ_{λ₂}⁻¹ = diag((λ₁/λ₂)², (λ₂/λ₁)²).

In the words of the note's plain-language passage, "square" therefore "means something only once λ is fixed by physics" (§5). For the radiation of today's observable universe, the Born length that would make its rectangle square is 3.7 × 10¹¹ m, about 2.5 au, a number to which the note assigns no mechanism (§7). The gate checks the statements symbolically, for symbolic λ, L and P:

```text
PASS  rho_lambda is symplectic for every lambda (R^T w R = w)
PASS  the area L P is invariant for every lambda
PASS  the aspect ratio A = hbar L/(lambda^2 P) goes to 1/A
PASS  A = 1 iff lambda^2 = hbar L/P
PASS  two Born lengths differ by a squeeze: rho_l1 rho_l2^-1 = diag((l1/l2)^2, (l2/l1)^2)
```

For Gaussian wave packets the map is the Fourier transform's action Z → −1/Z on the packet's shape parameter, which inverts the width ratio Δx/Δp = 1/|Z|; the round packet Z = i is the self-dual shape for the chosen λ ([Gaussian wave packets on the Siegel half-plane](/wiki/phase-space/modular-field/gaussian-states)).

### Born's fundamental length

#13 §4 records Born's motive: "This was Born's original hope in 1938: a physics with a fundamental mass and a fundamental length on equal footing." Its tag on the [invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell) speaks of "Born's 1938–49 program of a self-dual physics with both m and λ fundamental [3†, 4†]" ([Born's self-dual program](/wiki/phase-space/reciprocity/born-reciprocity#borns-self-dual-program)). In the terms of the subsection on what kinematics leaves free, a fundamental length would be a λ fixed by physical law rather than by a choice of units (the wiki's reading).

The references are #13's [3]† M. Born, "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 (1938), and [4]† M. Born, "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 (1949), both cited from model memory. The [round-3](/wiki/method/review/round-3) referee checked their metadata in another manuscript's reference list and found that the "1938 abstract does not state the rule; primary text paywalled" (`review/round3/referee/audit-notes.md`, Step 1).

**What Born's papers say about the length.** The phase-space-diameter note retrieved both papers and read them [S] (§4): the round-5 adjudication records the copies, the 1938 paper as the publisher's own copy archived in the Wayback Machine and the 1949 paper as the American Physical Society's open copy (header), and the worklog records that the quotations were transcribed from the copies' page images and that the 1938 paper was read in full ('Status'). According to the note:

- **1938.** Born pairs the radius a of Einstein's closed universe with the radius b of a hypersphere in momentum space, which gives "an upper limit for momenta". He fixes b from the classical electron radius r₀ by r₀ = h/(πb), so that b c = 2ℏc/r₀ ≈ 1.4 × 10⁸ eV [V], "a particle scale" in the note's words. He declines to connect the two radii, and he leaves open "whether the constant b is universal, or characteristic for each energetically closed system".
- **1949.** Born "splits ħ = ab into a length and a momentum and fixes the length from particle masses".

"Neither paper uses the Planck length" (§4). The note's §5 states the consequence for this page: "Born's own reciprocity length was a particle scale". The quotations and their context are on [Born's self-dual program](/wiki/phase-space/reciprocity/born-reciprocity#borns-self-dual-program). #13's references keep their † mark, and whether #13's description of Born's hope matches Born's text is part of the † literature battery (below).

## How the program uses it

### Units in which λ and ε are 1

The lab notebook writes the three phase-space structures in their standard forms, ω = [[0, 1], [−1, 0]], η = [[0, 1], [1, 0]] and H = [[1, 0], [0, 1]], with "units chosen so a reference length λ and momentum ε = ℏ/λ are scaled out" (#1 §2; [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). The same units underlie the generalized metric of [P1](/wiki/program/postulates/p1-arena) and the self-dual point of the modular field: at Z = i the metric is H = 1, the unit metric of these units ([reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion#the-fixed-point-the-self-dual-vacuum-z--i)). #1 gives λ no name and no value, and it does not return to it. #13 uses the same pair of symbols, λ and ε = ℏ/λ, and calls λ the Born length; neither document refers to the other on the point.

### The program's action fixes no λ

The phase-space-diameter note asks whether the program's own equations fix the Born length, and answers no [D] (§5): "The program's geometric action, built from ω and H, is invariant under the rigid Sp(2d, ℝ) …, which acts transitively on the Siegel domain and so moves the self-dual point Z = i anywhere; the action therefore singles out no Born length" (the omitted citations are #11 §7.1 and calc note #6 §1). The argument ties the Born length to the self-dual point: a different λ puts Z = i at a different point of [the Siegel domain](/wiki/phase-space/modular-field/siegel-domain), two choices differing by the squeeze given above (the wiki's reading). In the note, "a length enters only through reference structures": the reference axes of [the ρ-preserving potential](/wiki/symmetry-breaking/rho-preserving-potential), matter's coupling to the polarization ([P4](/wiki/program/postulates/p4-polarized-matter); [locality from an (H, K)-built coupling](/wiki/symmetry-breaking/matter-coupling)), and #13's dual special relativity, "which sets λ = l_P in one untagged sentence" (§5). The note's summary lists the claim that the program fixes a Born length as answered "no: its action singles out none; #13's λ = l_P is an untagged choice" [D] (§9).

The program also cannot let the length vary from system to system. Freidel, Kowalski-Glikman, Leigh and Minic, whose Born geometry the program builds on, take their cell length to be "not universal but instead … chosen in the context of the system in question" (note §4). The note's §8 says the program cannot do the same: "its reciprocity is one exact symmetry with one Born length."

Calibration: the round-5 pre-registration listed "the program fixes no λ" among the likely weak links, because it rests on program documents the referees could not see. The referees did not raise it (`review/round5-adjudication.md`, 'Pre-registration scored'). Since they did not have those documents, they could check the premises the note takes from them only for consistent use (`review/round5-preregistration.md`).

### The slope of the momentum cone

In #13 the length's first job is to give the momentum-space light cone a slope ([two causal cones](/wiki/conjugate-relativity/two-causal-cones)). The cone of position space bounds speed by c. The cone of momentum space bounds the rate of change of momentum, which is a force:

```text
|dp/dt| ≤ c̃ = ε/(λ/c) = ℏc/λ²        (#13 §1)
```

c̃ = ε/(λ/c) reads as one unit of momentum ε per light-crossing time λ/c, the time light takes to cross one Born length. Counted in units of λ and ε, the two bounds are the same: in the time λ/c a light signal crosses one unit of length, and the momentum of a body moving at the dual bound changes by one unit of momentum (the wiki's reading of the formula). #13 gives the bound without further derivation from the phase-space metric. The formula contains no free quantity other than λ, so the value of the maximum force is a statement about λ.

### The Planck identification

#13 §1 fixes λ in one sentence: "The only length the gravitational sector supplies is the Planck length, λ² = ℏG/c³, giving"

```text
c̃ = c⁴/G ≈ 1.2 × 10⁴⁴ N        (#13 §1, boxed)
```

The step carries no tag. #13 gives no argument for it beyond the sentence quoted and considers no other length, and a different λ would give a different maximum force ([the Planck identification, step by step](/wiki/conjugate-relativity/maximum-force#the-planck-identification-step-by-step)). The Planck length l_P = √(ℏG/c³) is the one length that can be built from ℏ, G and c, up to a pure number [T]. With λ = l_P, ε is the Planck momentum and λ/c the Planck time, so c̃ is the Planck force, c⁴/G ([the Born length at the Planck length](/wiki/gravity/spin-2-fields/planck-units#the-born-length-at-the-planck-length), that page's reading; [a length and a momentum whose product is ℏ](/wiki/gravity/spin-2-fields/planck-units#a-length-and-a-momentum-whose-product-is-ℏ)). The project's rule asks for executed code behind every asserted number ([the iron rule](/wiki/method/verification/iron-rule)). Since the phase-space-diameter note, `verify/phase_space_diameter.py` computes the value, `PASS  c~ = c^4/G = 1.21e44 N at lambda = l_P` (note §8.1, [V]). The check confirms the arithmetic of c⁴/G, not the identification of λ with l_P ([verification confirms arithmetic, not the model](/wiki/method/verification/arithmetic-not-model)).

### Planck closure

#13 §4 multiplies the maximum force by a length: "The dual rest-energy relation is E = λ c̃ (length × maximum force). At λ = l_P: E = l_P · c⁴/G = √(ℏc⁵/G) — the Planck energy, exactly [D]." The relation is written with a plain λ, in the section that introduces a conjugate quantum's invariant length λ_χ, and the bullet evaluates it at λ = l_P, the value §1 gave the Born length ([what #13 leaves unspecified](/wiki/conjugate-relativity/invariant-length-shell#what-13-leaves-unspecified)). In Planck units it is the Planck length times the Planck force ([Planck closure](/wiki/gravity/spin-2-fields/planck-units#planck-closure)). #13 §7 lists "E(l_P) = E_Planck" among its "Numerical anchors", and no `verify/` script checks it.

### The self-dual length, excluded

For a given cosmic length, one Born length makes the universe's whole range of scales symmetric under the exchange. The phase-space-diameter note takes the Fourier box [l_P, L] × [ℏ/L, ℏ/l_P], lengths from the Planck length to a cosmic length L and momenta between the matching bounds, and finds by the rectangle rule above that it maps onto itself under ρ_λ exactly when λ = √(l_P L): 47.1 μm for the Hubble radius c/H₀, 51.8 μm for the de Sitter radius L_Λ and 84.0 μm for the particle horizon [T][V] (§7; [the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box)). The length is prior art: its energy ℏc/λ is the Cohen–Kaplan–Nelson cutoff of effective field theory in a box of size L, and it is the cell length that Freidel, Kowalski-Glikman, Leigh and Minic tie to the vacuum energy (§4, §7 [T][S]).

With one Born length, the note tests the two places such a length could enter (§8):

- **As #13's Born length.** c̃ = ℏc/λ² becomes (c⁴/G)(l_P/L): 1.4 × 10⁻¹⁷ N for L = c/H₀ and 1.2 × 10⁻¹⁷ N for L_Λ. The Coulomb force in the hydrogen ground state, 8.24 × 10⁻⁸ N, exceeds it by 5.8 × 10⁹, and the weight of a kilogram by 6.9 × 10¹⁷; #13's composition law for forces would cap every force near 10⁻¹⁷ N. "The self-dual length cannot be that Born length" [D][V] (§8.1; [the maximum force](/wiki/conjugate-relativity/maximum-force#the-maximum-force-at-the-self-dual-length)).
- **As the range of the momentum graviton X.** In the program's aligned bimetric vacuum, where the ratio u of the two frames' backgrounds is 1, X couples to ordinary matter with Yukawa strength α = 4/3, and torsion balances exclude a force of that strength at 47–84 μm. They bound X's range below 37.7 μm, M_X c² > 5.2 meV [D][V][S] (§8.2; [the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)).

Both identifications are dead, the second in the aligned vacuum. For a background ratio u < 0.67 the 47.1 μm end of the self-dual range would be allowed, and the 84.0 μm end needs u < 0.30 [V]; whether the aligned vacuum persists as the universe expands is open [O] (§8.2; [Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)). Two further remarks of §8.1 bear on λ. In Freidel, Leigh and Minic's metastring, ℏ = λε and Newton's constant is G_N = ρλ/ε, "so λ² = ħG_N/ρ is the Planck length squared up to ρ", a factor set by the dimension and the compactification [S]. And with the Born length at l_P the cosmic Fourier box is far from self-dual: its aspect ratio is L/l_P = 8.5 × 10⁶⁰ for the Hubble radius.

### Elsewhere in the documents

- **The phase-space diameter relation.** A conjecture recorded only in the summary of the original chat compares a length with a momentum: the universe's rectangle in phase space is "square (D_x = D_p in Planck units) exactly at the bounce" (`HANDOFF.md` §4), and the handoff does not mention the Born length. The phase-space-diameter note reads "Planck units" as λ = l_P, "the Born length of the program's dual special relativity" (§6). In those units the radiation of today's observable universe is 5.2 × 10⁹² times longer in position than in momentum, and its rectangle would have been square only at about 4.4 × 10¹⁴ times the Planck temperature, before the radiation existed; the claim is withdrawn [D][V] ([the phase-space diameter relation](/wiki/cosmology/scale-factor-duality/phase-space-diameter); [Obituary: the square rectangle at the bounce](/wiki/cosmology/scale-factor-duality/square-at-the-bounce)).
- **The early-universe term.** The program keeps an optional a⁻⁶ term in the Friedmann equation from a dual Einstein term with its own Planck mass M̃. If reciprocity fixes M̃ = M_P, the note finds the term's step at the self-dual epoch, which depends on λ and on the comoving scale taken as unit: "The step's free parameter becomes the question of the Born length" [D][V] (§8.4). The dual Einstein–Hilbert term behind the a⁻⁶ step is used in #1 §6 under a [D] tag but derived from the geometric action in no document, so the step tests a postulate (flag 49 in `review/wiki-build-flags.md`; [the dual frame](/wiki/cosmology/scale-factor-duality/closed-universe#the-dual-frame-what-closure-fixes-and-what-it-does-not)). The closed-universe note adds that closure fixes the normalization a = R/λ but not the a⁻⁶ coefficient, and that a compact momentum space with k̃ = k would need λ ≤ 1.278×10⁻⁶ m at |Ω_k| = 10⁻² to survive N_eff, nucleosynthesis and the observed momentum range (flag 48).
- **A compact phase space.** A closed position space times a closed momentum space is never a phase space, while the compact Gr̃(2,5) is one; its reciprocity length √(R₀ l_P) = 1.489×10⁻⁴ m at |Ω_k| = 10⁻² fails the same two tests as the self-dual length, and meeting the program's Born-length bounds needs a momentum radius κc of at least 46.5 E_P today ([reciprocity on a closed space](/wiki/phase-space/reciprocity/closed-space-reciprocity#compact-phase-spaces-dv); closed-universe note §5).
- **A lever arm (open).** If matter's polarization follows the vacuum's as the dark-energy field drifts, a rotation of the polarization by θ displaces a particle of momentum p by θλ²p/ℏ: 4.9 × 10⁻⁶⁰ m per radian for an electron with the Bohr momentum at λ = l_P, and 42 m per radian at the self-dual length [V]. "A cosmological drift of τ would then be harmless only for a Born length near the Planck length" (§8.5, a section tagged [O]).
- **The popular articles.** Neither names the Born length, and both call the Planck value natural: "plugging in the natural scale yields c⁴/G" (#10, 'Corollaries and daydreams'), and "The framework's natural value for this limit is c⁴/G" (#12, 'A second speed of light'). They are never a source for a claim's status ([the popular articles](/wiki/history/documents/popular-articles)).

## Not to be confused with

- **λ_χ, the invariant length of a conjugate quantum.** #13 §4 states that "conjugate quanta are characterized by an irreducible extent λ_χ as ours are by mass", and reads μ ~ ℏ/λ_χ as the gate scale of the dark-matter sector, in a sentence whose combination of two gate conventions is flag 17 in `review/wiki-build-flags.md` ([the invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell)). λ_χ labels a particle, as a mass does; the Born length enters c̃, one bound for every trajectory. `HANDOFF.md` §2 writes "invariant length λ", §4 asks "whether invariant length λ and dual charge lock together", and the v3 worklog's item O3 says that "#13 §4 labels conjugate quanta by an invariant length λ instead of a mass": in all three, "invariant length" is #13's term for λ_χ. #13 gives no value for λ_χ.
- **M_B, the lab notebook's mass scale.** #1 §3 writes its geometric action as S_H = ½M_B² ∫ √|H| R_B[H], whose metric block "reproduces the Einstein–Hilbert action with M_P fixed by M_B and the section volume" [D, schematic] ([the geometric action S_H](/wiki/gravity/tuning-test/geometric-action)); #1 is superseded as a reference. #1 contains both λ and M_B and relates them nowhere, and no other document relates them.
- **Other uses of the letter.** The documents also write λ for couplings and gauge parameters, and the wiki writes it for the range of a fifth force ([notation](/wiki/notation)).

## What is open

- **The factor of 4.** With λ at the Planck length, c̃ = c⁴/G is four times the conjectured maximum force c⁴/4G of the general-relativity literature ([maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)). #13 §1: "The factor of 4 is not fixed here [O]"; §7 lists "the factor 4" first among its open items. #13 does not say what would fix it ([Open: the factor of 4](/wiki/conjugate-relativity/maximum-force#open-the-factor-of-4)).
- **The two dual cones.** λ sets the slope c̃ of #13 §1's dual cone, which lies in time and momentum. #13 §6 instead calls E = c|p| "the dual null cone", a cone in energy and momentum with slope c, which the v3 worklog's item O3 assigns to the unbuilt four-dimensional Born map; the item asks to "fix #13's two cones and settle which construction governs" before any paper claims more ([Open: the two dual cones](/wiki/conjugate-relativity/two-cones-inconsistency)).
- **The value of λ.** No document derives λ from the program's action, and the phase-space-diameter note finds that the action singles out none (§5 [D]); it excludes the self-dual length of about 50 μm and leaves the Planck value as #13's untagged choice (§8.1, §9). The note adds that its reformulation of the cosmological constant through the self-dual length "would become a prediction only if the program derived λ, or M_X, from its own dynamics" (§8.6). The identification with the Planck length is not among #13 §7's open items, #11 §14's open problems or the current queue in the root `CLAUDE.md`; it stands as an untagged step in an unreviewed paper.
- **Born's papers.** Born's 1938 and 1949 papers were retrieved and read for the phase-space-diameter note (§4; [above](#borns-fundamental-length)). Born fixed his momentum-space radius from the classical electron radius in 1938 and his reciprocity length from particle masses in 1949, and neither paper uses the Planck length. #11 and #13 still cite both papers from model memory. Checking what they say of Born against his text, like every † citation of #11 and #13, belongs to [the † literature battery](/wiki/method/literature-battery) (OP10), which the root `CLAUDE.md` keeps in the current queue with a note that Born 1938 and 1949 were retrieved for the diameter note.

The program's open items are collected in [open problems and the queue](/wiki/status/open-problems).

## Standing

`HANDOFF.md` §2 lists "Maximum force c̃ = c⁴/G as the momentum-space light speed (matches Gibbons–Schiller maximum-force conjecture up to the factor 4)" among its alive results, under a heading that reads "derived, machine-verified where marked ✓"; the item carries no ✓. The root `CLAUDE.md` lists #13 among the current references. #11 v2.3 mentions neither the Born length nor the maximum force, and no blind review round has covered #13. The phase-space-diameter note, reviewed in round 5 with verdict B, finds that the program's action fixes no λ, excludes the self-dual length as #13's Born length, and leaves the Planck value as an untagged choice. The Born length at the Planck value is therefore alive and unreviewed, with the standing of the maximum force it fixes ([claims that stand](/wiki/status/alive)).

## Sources

- `papers/conjugate-special-relativity.md` §1 — the Born length, ε = ℏ/λ, the bound c̃ = ε/(λ/c) = ℏc/λ², the Planck identification and the boxed value, the open factor of 4; Abstract — "at the Planck value of the Born length"; §4 — Born's hope, λ_χ and the Planck closure [D]; §6 — E = c|p| as "the dual null cone"; §7 — the numerical anchors and the open list; References [3]†, [4]† — Born 1938 and 1949
- `papers/phase-space-diameter.md` §5 — the rectangle under ρ_λ [T][V] and its two consequences [D][V]; "The program fixes no λ" [D]; Born's own length a particle scale; §4 — Born 1938 and 1949, retrieved and read [S], and the contextual cell length of Freidel, Kowalski-Glikman, Leigh and Minic; §6 — "Planck units" read as λ = l_P; §7 — the self-dual length √(l_P L) [T][V] and the Born length that would square today's radiation rectangle; §8.1 — the maximum force at the self-dual length, the metastring's λ², the box at λ = l_P [D][V][S]; §8.2 — X's range [D][V][S]; §8.4, §8.5, §8.6 — the a⁻⁶ step, the lever arm, what would make the reformulation a prediction; §9 — the summary row on the Born length
- `verify/phase_space_diameter.py` — the rectangle checks and every number quoted from the note, among them c⁴/G = 1.21 × 10⁴⁴ N
- `review/round5-adjudication.md` header — the copies of Born's papers retrieved for the note; 'Pre-registration scored' — "the program fixes no λ" not raised by the referees
- `review/round5-preregistration.md` 'Predictions', 'Limitation' — the claim listed as a likely weak link, and the referees' lack of the program documents
- `notes/phase-space-diameter-worklog.md` 'Status' — the Born quotations transcribed from the page images; Born 1938 read in full
- `notes/broken-born-theory.md` §2 — the reference length λ and momentum ε = ℏ/λ scaled out of the standard forms; §3 — the mass scale M_B (superseded as a reference)
- `HANDOFF.md` §2 — the alive listing and "invariant length λ"; §4 — "D_x = D_p in Planck units" and the invariant length and dual charge (chat-only)
- `review/v3-worklog.md` 'New open items', item O3 — the invariant length written λ, and #13's two dual cones
- `review/round3/referee/audit-notes.md` Step 1 — the partial check of Born's papers
- `papers/broken-born-checkpoint-v2.md` §14 — the open problems, none of which concerns λ
- `CLAUDE.md` 'Layout' — #13 as a current reference; 'Since the handoff' — the current queue
- `popsci/angle-of-the-mirror.md` 'Corollaries and daydreams' and `popsci/universes-other-half.md` 'A second speed of light' — the Planck value called natural (not a status source)
- `review/wiki-build-flags.md` item 17 — the two gate conventions combined in #13 §4's gate-scale sentence
- `notes/closed-universe.md` §4, §7; `review/wiki-build-flags.md` items 48 and 49 — a closed universe leaves the momentum fibre flat, and the dual Einstein–Hilbert term behind the a⁻⁶ step is not derived
- `notes/closed-universe.md` §5 — Gr̃(2,5), its reciprocity length and the momentum radius the Born-length bounds need
