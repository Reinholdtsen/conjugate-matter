"""Critic, cross-analysis numbers not computed by any analyst.

(1) A doubly compact Born-reciprocal phase space of Snyder-de Sitter type (observations C46; critic
    b_compact_phase_space.out) has reciprocity length lambda = sqrt(R hbar/kappa) (position sphere R,
    momentum sphere kappa). The program's own bounds on a Born length: #13's maximal force
    hbar c/lambda^2 >= hydrogen Coulomb force (momentum-space C24's criterion) and X's range 37.7 um
    (momentum-space C25's criterion). The momentum-sphere radius each requires, today and at the turnaround.
(2) Range of the conjugate scale factor: atilde ~ 1/R from an inflationary throat (c/H_inf at the
    record's bound scale, minisuperspace C27) to the turnaround (R_max at the closed-conditional DESI DR2+CMB
    floor, g_answer_numbers.out).
(3) Gravity-sector C10: G_eff = 2 G_N for H >> M_X, which includes inflation. At fixed potential V the
    Hubble rate rises by sqrt(2), shifting the throat and the e-fold budget N = ln(R_end H/c) (minisuperspace
    C30) by ln sqrt(2). The tensor-amplitude normalization in bigravity is not computed here.
"""
import math
c = 299792458.0; hbar = 1.054571817e-34; G = 6.67430e-11; eV = 1.602176634e-19
lP = math.sqrt(hbar*G/c**3); EP_eV = math.sqrt(hbar*c**5/G)/eV
Mpc = 3.0856775814913673e22; Gpc = 1e3*Mpc; H0 = 67.4e3/Mpc
alpha = 7.2973525693e-3; a0 = 5.29177210903e-11
F_H = alpha*hbar*c/a0**2
lam13 = math.sqrt(hbar*c/F_H)
lamX = 37.7e-6
print("=== (1) momentum-sphere radius a doubly compact SdS-type phase space would need ===")
print(f"  #13 bound: hbar c/lambda^2 >= F_H = {F_H:.4e} N -> lambda <= {lam13:.4e} m; X-range bound lambda <= {lamX:.3e} m")
for label, R in [('today, |Omega_k| = 1.13e-3 (R0)', c/(H0*math.sqrt(1.13e-3))),
                 ('turnaround floor, R_max = 1.174e5 Gpc', 1.174e5*Gpc)]:
    for nm, lam in [('#13', lam13), ('X range', lamX)]:
        kappa_c_eV = hbar*c*R/lam**2/eV
        print(f"  {label}: lambda <= {nm} bound -> kappa c >= {kappa_c_eV:.3e} eV = {kappa_c_eV/EP_eV:.3e} E_P")
print(f"  (with kappa = m_P c the length is sqrt(R l_P) = {math.sqrt(c/(H0*math.sqrt(1.13e-3))*lP):.3e} m today)")

print("\n=== (2) range of the conjugate scale factor, throat -> turnaround ===")
Einf_GeV = 1.39e16
Mbar_GeV = 2.435e18
H_inf_GeV = Einf_GeV**2/(math.sqrt(3)*Mbar_GeV)
hbarc_GeVm = 1.973269804e-16
R_throat = hbarc_GeVm/H_inf_GeV
Rmax = 1.174e5*Gpc
print(f"  throat c/H_inf = {R_throat:.4e} m = {R_throat/lP:.4e} l_P (minisuperspace C27: 4.3080e-30 m, 2.6654e5 l_P)")
print(f"  atilde(throat)/atilde(turnaround) = R_max/R_throat = {Rmax/R_throat:.3e} (log10 {math.log10(Rmax/R_throat):.2f}) for a bound-scale throat and the floor turnaround; neither radius is bounded above")

print("\n=== (3) G_eff = 2 G_N during inflation ===")
print(f"  H at fixed V rises by sqrt(2) = {math.sqrt(2):.4f}; throat c/H shrinks to {R_throat/math.sqrt(2):.4e} m;"
      f" e-fold budget N = ln(R_end H/c) rises by ln sqrt(2) = {math.log(math.sqrt(2)):.4f}")
