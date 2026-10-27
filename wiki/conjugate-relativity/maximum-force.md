---
title: "The maximum force c̃ = c⁴/G"
weight: 40
status: alive
description: "c̃ = ℏc/λ² with the Born length set to the Planck length gives c⁴/G ≈ 1.2×10⁴⁴ N, four times the literature's c⁴/4G — a factor #13 leaves open; at the self-dual length of about 50 μm it would be 1.4×10⁻¹⁷ N, which excludes that length."
sources:
  - "CLAUDE.md 'Since the handoff'"
  - "papers/phase-space-diameter.md §7"
  - "papers/phase-space-diameter.md §8.1"
  - "papers/phase-space-diameter.md §9"
  - "papers/phase-space-diameter.md References"
  - "verify/phase_space_diameter.py"
  - "review/round5-adjudication.md 'Verdict'"
  - "review/round5-adjudication.md 'Recommendations to Paul'"
  - "review/round5/manuscript-v1.0.md §8.1"
  - "papers/conjugate-special-relativity.md §1"
  - "papers/conjugate-special-relativity.md References [1]–[2]"
  - "papers/conjugate-special-relativity.md Abstract"
  - "papers/conjugate-special-relativity.md §2"
  - "papers/conjugate-special-relativity.md §4"
  - "papers/conjugate-special-relativity.md §7"
  - "notes/broken-born-theory.md §2"
  - "HANDOFF.md §2"
  - "HANDOFF.md §4"
  - "popsci/angle-of-the-mirror.md 'Dividends and daydreams'"
  - "popsci/universes-other-half.md 'A second speed of light'"
---

*The maximum force is the limit that the [momentum-space light cone](/wiki/conjugate-relativity/two-causal-cones) places on how fast momentum can change, as the ordinary light cone limits speed to c: since a rate of change of momentum is a force, the limit is a largest possible force, c̃ = ℏc/λ², where λ is a length that the paper [#13](/wiki/conjugate-relativity) calls the [Born length](/wiki/phase-space/reciprocity/born-length). Setting the Born length equal to the [Planck length](/wiki/gravity/spin-2-fields/planck-units#the-born-length-at-the-planck-length) gives c̃ = c⁴/G, about 1.2 × 10⁴⁴ newtons, which #13 describes as "the scale black holes reach when they collide". The general-relativity literature already contains a [conjectured maximum force](/wiki/conjugate-relativity/maximum-force-conjectures), c⁴/4G; #13's value is larger by a factor of 4, and the factor is open. A maximal force from Born reciprocity is also in the literature, in Low's reciprocal relativity of 2006. The value depends entirely on the Born length: the phase-space-diameter note shows that a Born length of about 50 micrometres, the one length that makes the universe's range of scales exactly symmetric under reciprocity, would put the maximum force near 10⁻¹⁷ newtons, below the force that holds a hydrogen atom together, which excludes that length ([Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)). The result is alive but unreviewed: no review round has examined #13, the note's script checks only the arithmetic of c⁴/G, and the [checkpoint #11](/wiki/history/documents/checkpoint) does not mention it.*

**Status:** Alive, unreviewed — the boxed value carries no tag (#13 §7 lists it under "Numerical anchors"), the identification of the Born length with the Planck length carries none either, and the factor of 4 is [O] — listed alive in `HANDOFF.md` §2 without a machine-check mark; absent from #11 v2.2; #13 never through a [blind review](/wiki/method/review) round. `verify/phase_space_diameter.py` computes c⁴/G = 1.21 × 10⁴⁴ N for the phase-space-diameter note (§8.1, [V]; [the phase-space-diameter script](/wiki/method/verification/phase-space-diameter-script)), which checks the arithmetic and not the identification ([the iron rule](/wiki/method/verification/iron-rule)). The exclusion of the self-dual length as the Born length is the note's [D][V] (§8.1), reviewed in [round 5](/wiki/method/review/round-5).

## The result

#13 §1, boxed:

```text
c̃ = c⁴/G ≈ 1.2 × 10⁴⁴ N
```

The Abstract gives the same value: "a maximum force, c̃ = ℏc/λ², equal to c⁴/G ≈ 1.2 × 10⁴⁴ N at the Planck value of the Born length." c̃ is the invariant speed of the dual cone of [Two causal cones](/wiki/conjugate-relativity/two-causal-cones), the bound |dp/dt| ≤ c̃ on how fast any trajectory can move through momentum space. Since dp/dt is a force, c̃ plays for forces the part that the speed of light c plays for velocities ([Special relativity: the template](/wiki/conjugate-relativity/special-relativity)).

## The Born length

The formula c̃ = ℏc/λ² contains one free length. #13 §1: "λ is the Born length and ε = ℏ/λ its conjugate momentum scale", and c̃ = ε/(λ/c), one unit of momentum ε per light-crossing time λ/c. A length of this kind is needed whenever position and momentum share one geometry; the [lab notebook](/wiki/history/documents/lab-notebook) scales the same pair out of its standard forms without naming λ or fixing its value (#1 §2). Why the exchange of position and momentum needs such a length, Born's hope for a fundamental one, the other uses of λ in the documents, and how it differs from a conjugate quantum's invariant length λ_χ are on [The Born length λ](/wiki/phase-space/reciprocity/born-length).

## The Planck identification, step by step

#13 fixes λ in one sentence and gives the step no tag: "The only length the gravitational sector supplies is the Planck length, λ² = ℏG/c³, giving" the boxed value. The steps are:

1. **The bound.** c̃ = ℏc/λ² (#13 §1).
2. **The identification.** λ is set equal to the Planck length l_P, the length built from ℏ, G and c, so λ² = ℏG/c³ ([Maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)). #13 offers no argument for the step beyond the sentence quoted.
3. **The substitution.** Putting λ² = ℏG/c³ into ℏc/λ² cancels ℏ and leaves c⁴/G, the boxed form. The result contains only c and G. c⁴/G is the Planck energy divided by the Planck length, the quantity known as the Planck force [T].
4. **The number.** #13 gives c⁴/G ≈ 1.2 × 10⁴⁴ N, and §7 lists it among the "Numerical anchors". The iron rule asks for executed code with printed output for every asserted number. `verify/phase_space_diameter.py`, written for the phase-space-diameter note, now computes it: `PASS  c~ = c^4/G = 1.21e44 N at lambda = l_P` (note §8.1).

The value of c̃ therefore rests on the identification in step 2: a different length would give a different maximum force, and #13 considers no alternative. The phase-space-diameter note considers one and excludes it ([below](#the-maximum-force-at-the-self-dual-length)), and it finds that the program's action singles out no Born length, so that #13's λ = l_P is "an untagged choice" (§9; [the program's action fixes no λ](/wiki/phase-space/reciprocity/born-length#the-programs-action-fixes-no-λ)).

## The maximum force at the self-dual length

The phase-space-diameter note (`papers/phase-space-diameter.md` v1.1) finds, for a given cosmic length, one Born length that makes the universe's range of scales exactly symmetric under reciprocity. The Fourier box [l_P, L] × [ℏ/L, ℏ/l_P], all lengths from the Planck length to a cosmic length L with the matching momenta, maps onto itself under the exchange with Born length λ exactly when λ = √(l_P L): 47–84 μm for L between the Hubble radius c/H₀ and the particle horizon [T][V] (§7; [the self-dual cosmic box](/wiki/cosmology/scale-factor-duality/self-dual-cosmic-box)). §8.1 puts that length into c̃ = ℏc/λ² [D][V]:

```text
c̃ = ℏc/λ²

λ = l_P:          c̃ = c⁴/G = 1.21 × 10⁴⁴ N
λ = √(l_P L):     c̃ = (c⁴/G)(l_P/L)
    L = c/H₀:     1.4 × 10⁻¹⁷ N
    L = L_Λ:      1.2 × 10⁻¹⁷ N        (L_Λ the de Sitter radius)
```

The Coulomb force in the hydrogen ground state, 8.24 × 10⁻⁸ N, exceeds the self-dual value by 5.8 × 10⁹, and the weight of a kilogram by 6.9 × 10¹⁷. #13's composition law for forces, F₁ ⊕ F₂ = (F₁ + F₂)/(1 + F₁F₂/c̃²) (§2; [force boosts and force composition](/wiki/conjugate-relativity/force-boosts)), would cap every force near 10⁻¹⁷ N. The note: "The self-dual length cannot be that Born length." The identification is dead ([Obituary: the self-dual length as a program scale](/wiki/cosmology/scale-factor-duality/self-dual-length-obituary)); the same length is also excluded, in the program's aligned bimetric vacuum, as the range of the momentum graviton X ([the laboratory bound on X's range](/wiki/gravity/momentum-graviton/range-bound)).

The gate prints the note's checks, with the hydrogen force anchored to its CODATA atomic unit:

```text
PASS  c~ = c^4/G = 1.21e44 N at lambda = l_P
PASS  at the self-dual length c~ = 1.4e-17 N (c/H0), 1.2e-17 N (L_Lambda); c~/(c^4/G) = l_P/L
PASS  hydrogen Coulomb force 8.24e-8 N (CODATA atomic unit 8.2387234983e-8 N) exceeds it by 5.8e9; 1 kg weight by 6.9e17
```

The exclusion leaves #13's own choice, λ = l_P, where it was: untagged and unreviewed. The note follows the exclusion with Freidel, Leigh and Minic's metastring, in which ℏ = λε and Newton's constant is G_N = ρλ/ε, "so λ² = ħG_N/ρ is the Planck length squared up to ρ", a factor set by the dimension and the compactification [S] (§8.1).

## The reason offered

#13 §1 presents its contribution as an explanation rather than a new value: "The framework's contribution is a reason: a maximum force is the statement that nothing outruns light in the momentum polarization." The plain passage of §1 puts it as "If position and momentum are true equals, there must be a second limit of the same kind governing motion through momentum space." The limit is the speed of the second light cone, the cone of the momentum block g⁻¹ of the phase-space metric. #13 §1 adds that this cone is the causal structure of the slaved geometry, modified at short range by the massive field X ([Two causal cones](/wiki/conjugate-relativity/two-causal-cones#the-slaved-dual-cone-and-x)).

## Comparison with the literature

#13 §1 sets its value beside the general-relativity literature:

> "A maximum force c⁴/4G was conjectured within general relativity as the "maximum tension principle" [1†], with a companion maximum luminosity c⁵/4G approached by binary black-hole mergers; a maximal *acceleration* from a phase-space metric is older still [2†]."

Both values are numbers times c⁴/G, the one force that c and G can form ([Maximum force and maximal acceleration in the literature](/wiki/conjugate-relativity/maximum-force-conjectures)); #13's number is 1 and the conjecture's is 1/4. #13 notes "the conjecture's contested status" in that literature [T]. The documents describe the match in three ways:

- #13 §1: "The factor of 4 is not fixed here [O]".
- `HANDOFF.md` §2: c̃ "matches Gibbons–Schiller maximum-force conjecture up to the factor 4".
- The popular articles: "General relativity already contains a conjectured maximum force of exactly that form" (#10, 'Dividends and daydreams'), and "A maximum force of exactly this form was conjectured within general relativity two decades ago" (#12, 'A second speed of light').

#13's [O] governs. The popular articles are never a source for a claim's status ([The popular articles (#10, #12)](/wiki/history/documents/popular-articles)).

### A maximal force from Born reciprocity

The literature sweep for the phase-space-diameter note found prior art for the idea itself. The note, §8.1: "A maximal force from Born reciprocity is itself in the literature: Low's reciprocal relativity bounds forces by a constant b [S: Low 2006]; the program's own paper cites Gibbons's maximum-tension conjecture and Caianiello's maximal acceleration for the idea [P2, §1, †]." The note's [P2] is #13, whose references [1]† (Gibbons; Schiller) and [2]† (Caianiello) are cited in the passage quoted above. The reference is S. G. Low, "Reciprocal relativity of noninertial frames and the quaplectic group," Found. Phys. 36, 1036 (2006), arXiv:math-ph/0506031 [S]. #13 does not cite it. The round-5 adjudication passes it to Paul as a lead, "Low 2006 is prior art for #13's maximum force" ('Recommendations to Paul'), and the root `CLAUDE.md` lists it among the leads from the note's literature sweep that are not queued ('Since the handoff').

## Open: the factor of 4

#13 leaves the factor of 4 between c⁴/G and c⁴/4G open [O] (§1) and puts "the factor 4" first among §7's open items. Nothing has been computed on it. #13 does not say what would fix the factor, and no other document takes it up: it is not among #11 §14's open problems, the current queue in `CLAUDE.md` or `HANDOFF.md` §8. The item is listed in [Open problems and the queue](/wiki/status/open-problems).

## Where forces approach c̃

#13's plain passage for §1 places the limit at "about 10⁴⁴ newtons, the scale black holes reach when they collide". §2 names comparable-mass black-hole mergers as the one natural process that "operates at F ~ c̃ by construction", and so the one arena where dual-kinematic corrections could be of order unity, flagged and not derived ([Force boosts and force composition](/wiki/conjugate-relativity/force-boosts)). In #13's account every other natural process stays far below the limit, which it gives as the reason force looks exactly additive.

A conjecture from the original chat reads a black hole's horizon in the momentum description as a maximum-force surface: "hovering at horizon requires F → c⁴/G" (`HANDOFF.md` §4, conjecture tier; [Momentum-space black holes (chat-only)](/wiki/conjugate-relativity/momentum-space-black-holes)).

## Planck closure

#13 §4 multiplies the maximum force by a length: "The dual rest-energy relation is E = λ c̃ (length × maximum force). At λ = l_P: E = l_P · c⁴/G = √(ℏc⁵/G) — the Planck energy, exactly [D]." It is the dual counterpart of E = mc² and the second of #13's numerical anchors ([The invariant-length shell and Planck closure](/wiki/conjugate-relativity/invariant-length-shell)).

## Standing

`HANDOFF.md` §2 lists "Maximum force c̃ = c⁴/G as the momentum-space light speed (matches Gibbons–Schiller maximum-force conjecture up to the factor 4)" among the alive results, without the ✓ that marks a machine-checked item. #11 v2.2 mentions neither the maximum force nor #13's dual kinematics, and no blind review round has examined #13. The phase-space-diameter note, which went through round 5 with verdict B, uses the formula c̃ = ℏc/λ² to exclude the self-dual length as the Born length, and its script computes c⁴/G; the adjudication records that every number of the reviewed version, v1.0, reproduced under the referees' own constants and code (`review/round5-adjudication.md`, 'Verdict'), and v1.0's §8.1 gives the same values as v1.1. #13's value at the Planck length is therefore alive and unreviewed, with its arithmetic now scripted and its Born length still an untagged choice ([Conjugate special relativity](/wiki/conjugate-relativity)).

## Sources

- `CLAUDE.md` 'Since the handoff' — the self-dual length unusable as #13's Born length; Low 2006 as a lead, not queued.
- `papers/phase-space-diameter.md` §7 — the self-dual length √(l_P L) [T][V]; §8.1 — c̃ at λ = l_P and at the self-dual length, the hydrogen and kilogram comparisons, the composition-law cap, the metastring's λ², Low 2006 [D][V][S]; §9 — λ = l_P an untagged choice; References — Low 2006 [S].
- `verify/phase_space_diameter.py` — c⁴/G = 1.21 × 10⁴⁴ N, the self-dual values, the hydrogen anchor.
- `review/round5-adjudication.md` 'Verdict' — every number of v1.0 reproduced; 'Recommendations to Paul' — Low 2006 as prior art for #13's maximum force.
- `review/round5/manuscript-v1.0.md` §8.1 — the reviewed text, with the same values of c̃ and the same force comparisons as v1.1.
- `papers/conjugate-special-relativity.md` §1 — the Born length, the Planck identification, the boxed value, the reason, the literature and the open factor of 4; Abstract for "at the Planck value of the Born length"; §2 for the merger arena; §4 for Planck closure; §7 for the numerical anchors and the open list; References [1]†, [2]† — Gibbons and Schiller on the maximum force, Caianiello on maximal acceleration.
- `notes/broken-born-theory.md` §2 — the reference length λ and momentum ε = ℏ/λ.
- `HANDOFF.md` §2 — the alive listing, "up to the factor 4"; §4 for the chat-only horizon reading.
- `popsci/angle-of-the-mirror.md` 'Dividends and daydreams' and `popsci/universes-other-half.md` 'A second speed of light' — "of exactly that form" and "of exactly this form" (not a status source).
