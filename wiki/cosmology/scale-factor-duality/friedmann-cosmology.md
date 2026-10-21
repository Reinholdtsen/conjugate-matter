---
title: "Friedmann cosmology and minisuperspace"
weight: 10
status: established
description: "The FLRW metric, the Friedmann equation written with a lapse, fluids with ρ ∝ a^{−3(1+w)} including the stiff fluid, and cosmological redshift."
provenance: [T]
sources:
  - "notes/broken-born-theory.md §6"
  - "papers/broken-born-checkpoint-v2.md §10"
  - "popsci/universes-other-half.md 'Dark energy as the orientation of the split'"
---

*Friedmann cosmology is the description of a universe that looks the same at every place and in every direction, so that its entire geometry reduces to one function of time, the scale factor a(t), which multiplies the distance between any two distant galaxies. The Friedmann equation ties the expansion rate to the energy density, and each kind of content, whether matter, radiation or a cosmological constant, thins out at its own rate as a grows. Minisuperspace is the name for gravity reduced to this one function, with the freedom to choose the time coordinate kept as a single function called the lapse. The program writes its cosmology in this reduced form and adds a second scale factor for the conjugate universe.*

**Status:** Established — [T] — textbook cosmology, written here from general knowledge; the program's extension of it is derived in `notes/broken-born-theory.md` §6 and summarized in #11 §10.

## Key facts

- **The metric [T].** For a spatially flat universe the Friedmann–Lemaître–Robertson–Walker (FLRW) line element, written with a lapse N(t), is ds² = −N²dt² + a(t)²dx². With N = 1, t is cosmic time and the Hubble rate is H = ȧ/a.
- **The Friedmann equation is a constraint [T].** Reducing the Einstein–Hilbert action to this metric leaves a system with one variable, minisuperspace. The lapse enters without time derivatives, so varying it gives an equation with no second derivatives: the Friedmann equation, H² = 8πGρ/3 for a flat universe, which constrains the expansion rate rather than evolving it and is called the Hamiltonian constraint. The [lab notebook](/wiki/history/documents/lab-notebook) adds conjugate-side fluids by "Entering our Hamiltonian constraint" (#1 §6).
- **Fluids [T].** A fluid whose pressure is p = wρ thins as ρ ∝ a^{−3(1+w)}. The values the program uses (#1 §6) are dust, w = 0; radiation, w = +1/3; a cosmological constant, w = −1, whose density does not thin at all; spatial curvature, which enters the Friedmann equation like a fluid with w = −1/3; and a stiff fluid, w = +1, which "dies as a⁻⁶". A uniform scalar field whose energy is all kinetic is a stiff fluid, which is why #1 §6 labels the w̃ = +1 entry of its table "Kinetic/stiff energy".
- **Redshift [T].** Light emitted when the scale factor was a_e arrives with every wavelength stretched by the expansion since, 1 + z = a₀/a_e. The popular article #12 reads the same fact in the momentum description: "every momentum in the universe is shrinking: the spectrum of the cosmos has been contracting since the beginning". That is its gloss on [the cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint), offered as explanation and not as a source for status.
- **The program's version.** With a second scale factor ã for the conjugate universe and the constraint a·ã = 1, #1 §6 takes "one shared lapse N and dual Planck mass M̃" and obtains the equation below. The dual gravitational sector is "**not** a new fluid and **not** a ghost — ã was never independent — but a stiff-like (a⁻⁶) modification of the effective Planck mass, relevant only at early times" (#1 §6). The equation appears only in the lab notebook and has not been machine-checked.

```text
3H²(M_P² + M̃²a⁻⁶) = ρ
```

## Used by

- [The cosmological constraint a·ã = 1](/wiki/cosmology/scale-factor-duality/cosmological-constraint) — the second scale factor and its reciprocal relation to ours.
- [The duality dictionary w_eff = −w̃](/wiki/cosmology/scale-factor-duality/duality-dictionary) — the shared lapse, the Hamiltonian constraint and ρ ∝ a^{−3(1+w)}.
- [The turnaround as the conjugate bounce](/wiki/cosmology/scale-factor-duality/conjugate-bounce) — a halt and reversal of a(t), read through a·ã = 1.
- [Row 10: an early step in G_eff](/wiki/predictions/early-universe-step) — the a⁻⁶ term in the Friedmann equation.

## Sources

- `notes/broken-born-theory.md` §6 — the shared lapse, "our Hamiltonian constraint", the fluid table and the Friedmann equation with the dual term
- `papers/broken-born-checkpoint-v2.md` §10 — the current statement of the cosmology built on this reduction
- `popsci/universes-other-half.md` 'Dark energy as the orientation of the split' — redshift read as a contracting momentum spectrum (popular article; explanation only)
