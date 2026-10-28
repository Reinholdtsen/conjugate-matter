"""Verifier extras for Paul's 'two massive bodies' reading (not checked by the program agent):
(1) If the gate acts particle-by-particle (as the record's fiber-overlap gate does: mu is the
    width of each chi quantum, #6 sec. 4), the force between two extended bodies is the gate
    averaged over constituent pairs.  For Gaussian gate W = exp(-u^2/v*^2) and Maxwellian bodies
    (per-axis dispersions s1, s2; bulk relative velocity V):
        <W> = (1 + 2 s^2/v*^2)^(-3/2) exp(-V^2/(v*^2 + 2 s^2)),  s^2 = s1^2 + s2^2.
    Closed form checked here against direct numerical quadrature (independent of the formula).
(2) Narrow-gate 'Jeans' length of a long-range gated attraction of strength beta G (model b) among
    co-movers, lambda_J = 2 pi v*/sqrt(4 pi beta G rho_gate), with Debt 3a's co-moving fraction;
    and the beta needed to bring it down to 1 kpc.  Rough estimate (homogeneous medium, Jeans swindle)."""
import math as m
import numpy as np

vstar = 120.0


def W_avg_formula(V, s):
    return (1 + 2*s**2/vstar**2)**-1.5*m.exp(-V**2/(vstar**2 + 2*s**2))


def W_avg_quad(V, s, n=801):
    # relative velocity u ~ N(V e_z, s^2 I); integrate exp(-|u|^2/v*^2) over a 3D grid (cylindrical symmetry -> 2D)
    span = 8*max(s, vstar)
    z = np.linspace(V - span, V + span, n)
    rho = np.linspace(0, span, n)
    Z, R = np.meshgrid(z, rho, indexing='ij')
    f = np.exp(-(R**2 + Z**2)/vstar**2)*np.exp(-(R**2 + (Z - V)**2)/(2*s**2))/(2*m.pi*s**2)**1.5*2*m.pi*R
    return np.trapezoid(np.trapezoid(f, rho, axis=1), z)


print("(1) particle-level gate averaged over two Maxwellian bodies (v* = 120 km/s)")
print("    s [km/s]  V [km/s]   <W> formula   <W> quadrature   effective gate width sqrt(v*^2+2s^2) [km/s]")
for s in (5.0, 10.0, 50.0, 150.0, 2200.0/m.sqrt(3)):
    for V in (0.0, 100.0, 300.0):
        wf = W_avg_formula(V, s); wq = W_avg_quad(V, s)
        print(f"    {s:8.1f}  {V:7.1f}   {wf:.5e}   {wq:.5e}       {m.sqrt(vstar**2 + 2*s**2):8.1f}")

print()
print("(2) narrow-gate Jeans length of a gated 1/r attraction, strength beta G, among co-movers")
Gpc = 4.30091e-3                 # pc (km/s)^2/Msun
to_Msunpc3 = 1/37.97             # GeV/cm^3 -> Msun/pc^3
for name, rho, sig in (("MW solar circle", 0.4, 155.0), ("MW inner 1 kpc", 10.0, 120.0)):
    frac = min(1.0, (vstar/sig)**3/(2*m.pi)**1.5)
    rg = rho*to_Msunpc3*frac
    lam1 = 2*m.pi*min(sig, vstar)/m.sqrt(4*m.pi*Gpc*rg)
    beta_1kpc = (lam1/1e3)**2
    print(f"    {name:16s}: co-moving fraction {frac:.3f}; lambda_J(beta = 1) = {lam1/1e3:.1f} kpc; beta needed for lambda_J = 1 kpc: {beta_1kpc:.2e}")
print("    dwarfs (sigma < v*): every pair is inside the gate, so the gated term only rescales chi-chi gravity, G -> (1 + beta) G")

print()
print("(3) where the Lagrangian (velocity-gated) form of model b loses its inertia: r* = 2 beta G M/v*^2, eps = 2 beta |Phi|/v*^2 = 1")
GMsun = 1.32712440018e20; AU = 1.495978707e11; kpc = 3.0856775814913673e19
for name, GM in (("Sun", GMsun), ("1e11 Msun (point mass)", 1e11*GMsun), ("1e12 Msun (point mass)", 1e12*GMsun)):
    rstar = 2*GM/(vstar*1e3)**2
    print(f"    {name:24s}: r*/beta = {rstar:.3e} m = {rstar/AU:.4f} AU = {rstar/kpc:.3f} kpc")
print(f"    beta at which eps = 1 for MW-at-Sun (|Phi| ~ v_c^2, v_c = 230): {vstar**2/(2*230**2):.3f}; for chi with co-moving fraction 0.0295: {vstar**2/(2*230**2*0.0295):.2f}")
