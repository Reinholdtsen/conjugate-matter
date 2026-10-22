---
title: "The Born length λ"
weight: 100
status: alive
description: "The reference length λ, with its momentum scale ε = ℏ/λ, that position and momentum need in order to share one geometry: why the exchange of the two needs it, the lab notebook's units that scale it out, #13's name for it and its role in the maximum force c̃ = ℏc/λ², and #13's untagged identification of it with the Planck length."
sources:
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md Abstract"
  - "papers/conjugate-special-relativity.md §4"
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
  - "popsci/angle-of-the-mirror.md 'Dividends and daydreams'"
  - "popsci/universes-other-half.md 'A second speed of light'"
  - "review/wiki-build-flags.md item 17"
---

*The Born length λ is a reference length that, together with Planck's constant ℏ, puts position and momentum on a common scale: positions are counted in units of λ and momenta in units of ε = ℏ/λ. A length and a momentum have different units, so a geometry that combines them, or a map that exchanges them such as [Born reciprocity](/wiki/phase-space/reciprocity/born-reciprocity), has a meaning only once some such pair of scales is chosen. The name comes from #13, the program's paper on [conjugate special relativity](/wiki/conjugate-relativity), in which λ fixes the slope of the momentum-space light cone and with it the [maximum force](/wiki/conjugate-relativity/maximum-force), c̃ = ℏc/λ². #13 sets λ equal to the [Planck length](/wiki/gravity/spin-2-fields/planck-units), in one sentence that carries no tag, and the maximum force becomes c⁴/G. The program's [lab notebook](/wiki/history/documents/lab-notebook) writes its phase-space structures in units in which the same pair of scales is 1, without naming λ or giving it a value. The identification with the Planck length is alive but unreviewed: no review round has examined it, no script checks it, and the [checkpoint #11](/wiki/history/documents/checkpoint) does not mention the Born length.*

**Status:** Alive, unreviewed — #13 §1 names λ the Born length and sets it equal to the Planck length, both without a tag; the [Planck closure](/wiki/conjugate-relativity/invariant-length-shell#planck-closure) evaluated at that value is [D] (#13 §4). The need for a reference length when position and momentum share one geometry is [T], written here from general knowledge, and #13 cites Born's hope for a fundamental length from model memory [3†, 4†]. No `verify/` script checks the identification or its numbers, no [blind review](/wiki/method/review) round has covered #13, and #11 v2.2 does not mention the Born length. `HANDOFF.md` §2 lists the maximum force that the identification fixes among the alive results, without the ✓ of a machine-checked item.

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
- **A law of motion can single one out.** A law of motion that is unchanged by one of these maps must contain that map's length, either as a constant of its own or built from its constants. The harmonic oscillator is the standard example: its mass and frequency, with ℏ, give a length that sets the width of its ground state, and in units of that length and of ℏ divided by it the oscillator's evolution is a rigid rotation of phase space, a quarter-period of which is the Fourier transform. That length belongs to one oscillator, and a different oscillator has a different one.

In ordinary quantum mechanics the reference length is therefore a convenience, chosen to suit the system at hand.

### Born's fundamental length

#13 §4 records Born's motive: "This was Born's original hope in 1938: a physics with a fundamental mass and a fundamental length on equal footing." Its tag on the [invariant-length shell](/wiki/conjugate-relativity/invariant-length-shell) speaks of "Born's 1938–49 program of a self-dual physics with both m and λ fundamental [3†, 4†]" ([Born's self-dual program](/wiki/phase-space/reciprocity/born-reciprocity#borns-self-dual-program)). In the terms of the previous section, a fundamental length would be a λ fixed by physical law rather than by a choice of units (the wiki's reading).

The references are #13's [3]† M. Born, "A suggestion for unifying quantum theory and relativity," Proc. R. Soc. Lond. A 165, 291 (1938), and [4]† M. Born, "Reciprocity theory of elementary particles," Rev. Mod. Phys. 21, 463 (1949), both cited from model memory. The [round-3](/wiki/method/review/round-3) referee checked their metadata in another manuscript's reference list and found that the "1938 abstract does not state the rule; primary text paywalled" (`review/round3/referee/audit-notes.md`, Step 1). Whether Born's papers state the hope in these terms is unchecked.

## How the program uses it

### Units in which λ and ε are 1

The lab notebook writes the three phase-space structures in their standard forms, ω = [[0, 1], [−1, 0]], η = [[0, 1], [1, 0]] and H = [[1, 0], [0, 1]], with "units chosen so a reference length λ and momentum ε = ℏ/λ are scaled out" (#1 §2; [the structures ω, η, H](/wiki/phase-space/born-geometry/born-structures)). The same units underlie the generalized metric of [P1](/wiki/program/postulates/p1-arena) and the self-dual point of the modular field: at Z = i the metric is H = 1, the unit metric of these units ([reciprocity as modular inversion](/wiki/phase-space/modular-field/modular-inversion#the-fixed-point-the-self-dual-vacuum-z--i)). #1 gives λ no name and no value, and it does not return to it. #13 uses the same pair of symbols, λ and ε = ℏ/λ, and calls λ the Born length; neither document refers to the other on the point.

### The slope of the momentum cone

In #13 the length's first job is to give the momentum-space light cone a slope ([two causal cones](/wiki/conjugate-relativity/two-causal-cones)). The cone of position space bounds speed by c. The cone of momentum space bounds the rate of change of momentum, which is a force:

```text
|dp/dt| ≤ c̃ = ε/(λ/c) = ℏc/λ²        (#13 §1)
```

c̃ = ε/(λ/c) reads as one unit of momentum ε per light-crossing time λ/c, the time light takes to cross one Born length. Counted in units of λ and ε, the two bounds are the same: in the time λ/c a light signal crosses one unit of length, and the momentum of a body moving at the dual bound changes by one unit of momentum (the wiki's reading of the formula). #13 gives the bound without deriving it from the phase-space metric. The formula contains no free quantity other than λ, so the value of the maximum force is a statement about λ.

### The Planck identification

#13 §1 fixes λ in one sentence: "The only length the gravitational sector supplies is the Planck length, λ² = ℏG/c³, giving"

```text
c̃ = c⁴/G ≈ 1.2 × 10⁴⁴ N        (#13 §1, boxed)
```

The step carries no tag. #13 gives no argument for it beyond the sentence quoted and considers no other length, and a different λ would give a different maximum force ([the Planck identification, step by step](/wiki/conjugate-relativity/maximum-force#the-planck-identification-step-by-step)). The Planck length l_P = √(ℏG/c³) is the one length that can be built from ℏ, G and c, up to a pure number [T]. With λ = l_P, ε is the Planck momentum and λ/c the Planck time, so c̃ is the Planck force, c⁴/G ([the Born length at the Planck length](/wiki/gravity/spin-2-fields/planck-units#the-born-length-at-the-planck-length), that page's reading; [a length and a momentum whose product is ℏ](/wiki/gravity/spin-2-fields/planck-units#a-length-and-a-momentum-whose-product-is-ℏ)). No `verify/` script computes 1.2 × 10⁴⁴ N, although the project's rule asks for executed code behind every asserted number ([the iron rule](/wiki/method/verification/iron-rule)).

### Planck closure

#13 §4 multiplies the maximum force by a length: "The dual rest-energy relation is E = λ c̃ (length × maximum force). At λ = l_P: E = l_P · c⁴/G = √(ℏc⁵/G) — the Planck energy, exactly [D]." The relation is written with a plain λ, in the section that introduces a conjugate quantum's invariant length λ_χ, and the bullet evaluates it at λ = l_P, the value §1 gave the Born length ([what #13 leaves unspecified](/wiki/conjugate-relativity/invariant-length-shell#what-13-leaves-unspecified)). In Planck units it is the Planck length times the Planck force ([Planck closure](/wiki/gravity/spin-2-fields/planck-units#planck-closure)). #13 §7 lists "E(l_P) = E_Planck" among its "Numerical anchors", and no `verify/` script checks it.

### Elsewhere in the documents

- **The phase-space diameter relation.** A conjecture that exists only in the original chat compares a length with a momentum, "D_x = D_p in Planck units" (`HANDOFF.md` §4). The wiki reads those units as the Planck length and the Planck momentum, the pair that #13's identification gives λ and ε ([Planck units in a chat-only conjecture](/wiki/gravity/spin-2-fields/planck-units#planck-units-in-a-chat-only-conjecture); [the phase-space diameter relation (chat-only)](/wiki/cosmology/scale-factor-duality/phase-space-diameter)). The handoff does not mention the Born length.
- **The popular articles.** Neither names the Born length, and both call the Planck value natural: "plugging in the natural scale yields c⁴/G" (#10, 'Dividends and daydreams'), and "The framework's natural value for this limit is c⁴/G" (#12, 'A second speed of light'). They are never a source for a claim's status ([the popular articles](/wiki/history/documents/popular-articles)).

## Not to be confused with

- **λ_χ, the invariant length of a conjugate quantum.** #13 §4 states that "conjugate quanta are characterized by an irreducible extent λ_χ as ours are by mass", and reads μ ~ ℏ/λ_χ as the gate scale of the dark-matter sector, in a sentence whose combination of two gate conventions is flag 17 in `review/wiki-build-flags.md` ([the invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell)). λ_χ labels a particle, as a mass does; the Born length enters c̃, one bound for every trajectory. `HANDOFF.md` §2 writes "invariant length λ", §4 asks "whether invariant length λ and dual charge lock together", and the v3 worklog's item O3 says that "#13 §4 labels conjugate quanta by an invariant length λ instead of a mass": in all three, "invariant length" is #13's term for λ_χ. #13 gives no value for λ_χ.
- **M_B, the lab notebook's mass scale.** #1 §3 writes its geometric action as S_H = ½M_B² ∫ √|H| R_B[H], whose metric block "reproduces the Einstein–Hilbert action with M_P fixed by M_B and the section volume" [D, schematic] ([the geometric action S_H](/wiki/gravity/tuning-test/geometric-action)); #1 is superseded as a reference. #1 contains both λ and M_B and relates them nowhere, and no other document relates them.
- **Other uses of the letter.** The documents also write λ for couplings, gauge parameters and a Yukawa range ([notation](/wiki/notation)).

## What is open

- **The factor of 4.** With λ at the Planck length, c̃ = c⁴/G is four times the conjectured maximum force c⁴/4G of the general-relativity literature ([maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)). #13 §1: "The factor of 4 is not fixed here [O]"; §7 lists "the factor 4" first among its open items. #13 does not say what would fix it ([Open: the factor of 4](/wiki/conjugate-relativity/maximum-force#open-the-factor-of-4)).
- **The value of λ.** No document derives λ from the program's action or tests the identification with the Planck length. The identification is not among #13 §7's open items, #11 §14's open problems or the current queue in the root `CLAUDE.md`; it stands as an untagged step in an unreviewed paper.
- **Born's papers.** Whether Born's 1938 and 1949 papers state the hope for a fundamental length as #13 quotes it awaits the source check of [the † literature battery](/wiki/method/literature-battery) (OP10).

The program's open items are collected in [open problems and the queue](/wiki/status/open-problems).

## Standing

`HANDOFF.md` §2 lists "Maximum force c̃ = c⁴/G as the momentum-space light speed (matches Gibbons–Schiller maximum-force conjecture up to the factor 4)" among its alive results, under a heading that reads "derived, machine-verified where marked ✓"; the item carries no ✓. The root `CLAUDE.md` lists #13 among the current references. #11 v2.2 mentions neither the Born length nor the maximum force, and no blind review round has covered #13. The Born length at the Planck value is therefore alive and unreviewed, with the standing of the maximum force it fixes ([claims that stand](/wiki/status/alive)).

## Sources

- `papers/conjugate-special-relativity.md` §1 — the Born length, ε = ℏ/λ, the bound c̃ = ε/(λ/c) = ℏc/λ², the Planck identification and the boxed value, the open factor of 4; Abstract — "at the Planck value of the Born length"; §4 — Born's hope, λ_χ and the Planck closure [D]; §7 — the numerical anchors and the open list; References [3]†, [4]† — Born 1938 and 1949
- `notes/broken-born-theory.md` §2 — the reference length λ and momentum ε = ℏ/λ scaled out of the standard forms; §3 — the mass scale M_B (superseded as a reference)
- `HANDOFF.md` §2 — the alive listing and "invariant length λ"; §4 — "D_x = D_p in Planck units" and the invariant length and dual charge (chat-only)
- `review/v3-worklog.md` 'New open items', item O3 — the invariant length written λ
- `review/round3/referee/audit-notes.md` Step 1 — the partial check of Born's papers
- `papers/broken-born-checkpoint-v2.md` §14 — the open problems, none of which concerns λ
- `CLAUDE.md` 'Layout' — #13 as a current reference; 'Since the handoff' — the current queue
- `popsci/angle-of-the-mirror.md` 'Dividends and daydreams' and `popsci/universes-other-half.md` 'A second speed of light' — the Planck value called natural (not a status source)
- `review/wiki-build-flags.md` item 17 — the two gate conventions combined in #13 §4's gate-scale sentence
