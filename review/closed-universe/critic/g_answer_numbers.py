"""Critic: the numbers that carry the answer to Paul's 'how big' and 'how small', combining
 - dynamics: a_max = (Omega_m + Omega_d)/|Omega_k| (C5, verified), t_turn = (pi/2)(Omega_m+Omega_d)/|Omega_k|^1.5/H0 (C8);
 - a check on the dynamics grid that Omega_d >= Omega_DE,0 = 1 - Omega_m - Omega_r + |Omega_k| (tau's energy per comoving
   volume does not fall between today and the turnaround), which sharpens momentum-space C1's floor a_max >= Omega_m/|Omega_k|;
 - curvature bounds conditional on closure (95%): DESI DR2+CMB LCDM+K (0.0023 +- 0.0011, published), the critic's
   corridor+K fit (f_corridor_curvature_fit.out: |Omega_K| < 0.00121), the w0wa+K proxy (published 0.0006 +- 0.0013,
   Union3: the loosest), and the cosmic-variance floor |Omega_k| ~ 1e-4 below which closure is unknowable.
Normalization-free outputs: R_max, t_turn, atilde(turn)/atilde(today) = 1/a_max, grain hbar c/R_max, T_CMB(turn).
"""
import csv, math

G = '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/8fc83553-5967-4784-9222-5b4b26b2960e/closed/dynamics/grid.csv'
rows = list(csv.DictReader(open(G)))
Om = 0.315; Or = 9.15e-5
print("=== (1) dynamics grid: Omega_d at the turnaround against Omega_DE,0 ===")
byk = {}
for r in rows:
    Ok = abs(float(r['Omega_k'])); Od = float(r['Od_turn'])
    ODE0 = 1 - Om - Or + Ok
    byk.setdefault(Ok, []).append((Od/ODE0, float(r['a_max'])*Ok/(Om + ODE0), float(r['f']), float(r['w0_target'])))
for Ok in sorted(byk, reverse=True):
    L = byk[Ok]
    print(f"  |Omega_k| = {Ok:.0e}: Omega_d/Omega_DE,0 = {min(x[0] for x in L):.4f} .. {max(x[0] for x in L):.1f};"
          f"  a_max |Omega_k|/(Omega_m + Omega_DE,0) = {min(x[1] for x in L):.4f} .. {max(x[1] for x in L):.1f}")
lo = min(x[0] for L in byk.values() for x in L)
arg = [x for L in byk.values() for x in L if x[0] == lo][0]
print(f"  smallest ratio {lo:.5f} at f = {arg[2]}, w0 = {arg[3]}: Omega_d >= Omega_DE,0 holds on the whole grid -> "
      f"a_max >= (Omega_m + Omega_DE,0)/|Omega_k| ~ (1 + |Omega_k|)/|Omega_k|")

c = 299792458.0; Mpc = 3.0856775814913673e22; Gpc = 1e3*Mpc; H0 = 67.4e3/Mpc
hbarc_eVm = 1.973269804e-7; T0 = 2.7255; Gyr = 3.15576e16
lP = 1.616255e-35
print("\n=== (2) answer numbers at the curvature bounds (closed-conditional 95%) ===")
def gauss_cond(mean, sig):
    Phi = lambda x: 0.5*(1 + math.erf(x/math.sqrt(2)))
    pc = Phi(-mean/sig); lo_, hi_ = 0.0, 0.1
    for _ in range(100):
        mid = 0.5*(lo_ + hi_)
        if (pc - Phi((-mid - mean)/sig))/pc < 0.95: lo_ = mid
        else: hi_ = mid
    return hi_, pc
cases = []
for name, mean, sig in [('DESI DR2+CMB LCDM+K (published)', 0.0023, 0.0011),
                        ('w0wa+K proxy, DR2+CMB+Union3 (published, loosest)', 0.0006, 0.0013)]:
    b, pc = gauss_cond(mean, sig)
    cases.append((name + f' [P(closed) = {pc:.3f}]', b))
cases.insert(1, ('critic corridor+K fit (DESI DR2 BAO + CMB compressed prior)', 0.00121))
cases.append(('cosmic-variance floor (closure unknowable below)', 1e-4))
for name, Ok in cases:
    R0 = c/(H0*math.sqrt(Ok))
    ODE0 = 1 - Om - Or + Ok
    amax = (Om + ODE0)/Ok              # smallest a_max on the thawing grid (Omega_d >= Omega_DE,0)
    Rmax = amax*R0
    tturn = (math.pi/2)*(Om + ODE0)/Ok**1.5/H0/Gyr
    print(f"  {name}: |Omega_k| < {Ok:.5f}")
    print(f"     R0 > {R0/Gpc:.1f} Gpc; a_max > {amax:.0f}; R_max > {Rmax/Gpc:.3e} Gpc = {Rmax/lP:.3e} l_P;"
          f" t_turn > {tturn:.3e} Gyr")
    print(f"     atilde(turn)/atilde(today) = 1/a_max < {1/amax:.3e}; grain hbar c/R_max < {hbarc_eVm/Rmax:.3e} eV;"
          f" T_CMB(turn) < {T0/amax*1e3:.3f} mK")
print("  (no upper bound on R_max or lower bound on the momentum scale: |Omega_k| -> 0 sends both to the flat limit;"
      " a larger Omega_d -- slower thawing -- raises a_max further, up to 145 times the floor on the grid (a_max abs(Omega_k)/(Omega_m + Omega_DE,0) = 1.01-145))")
