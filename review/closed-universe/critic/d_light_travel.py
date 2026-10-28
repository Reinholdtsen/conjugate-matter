"""Critic, tension (d): light travel, dynamics C20-C25 against momentum-space C41.

C41: dust + curvature from a_v to a_max: conformal time pi - 2 arcsin sqrt(a_v/a_max) (2.78 rad at
     |Omega_k| = 1e-2 with a_v = 1 and a_max = Omega_m/|Omega_k| = 31.5).
Dynamics: integrated histories; chi0 from a radiation bang, chi_turn, chi_crunch.
Checks:
 (1) chi_turn - chi0 (conformal time today -> turnaround) from the dynamics grid, against C41's formula
     with C41's a_max and with each history's own a_max.
 (2) the conformal time an inflationary closed de Sitter phase adds before the radiation era:
     R = cosh(Ht)/H gives eta(t) = 2 arctan(tanh(Ht/2)), so from a throat eta -> pi/2; from a start at
     radius R_i > c/H it is arcsin(c/(H R_i)). Symbolic check plus numbers.
 (3) consequences in the dust-cycloid approximation a = a_max sin^2(eta/2), t/t_turn = (eta - sin eta)/pi,
     for light that starts at the throat: when it reaches the antipode and when it closes the circuit.
"""
import csv, math
import sympy as sp

G = '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/8fc83553-5967-4784-9222-5b4b26b2960e/closed/dynamics/grid.csv'
rows = list(csv.DictReader(open(G)))
print(f"=== (1) dynamics grid: {len(rows)} histories ===")
byk = {}
for r in rows:
    Ok = abs(float(r['Omega_k']))
    dchi = float(r['chi_turn']) - float(r['chi0'])
    amax = float(r['a_max'])
    c41_floor = math.pi - 2*math.asin(math.sqrt(1/(0.315/Ok)))
    c41_own = math.pi - 2*math.asin(math.sqrt(1/amax))
    byk.setdefault(Ok, []).append((dchi, c41_floor, c41_own, (dchi - math.pi)/math.sqrt(Ok), float(r['chi0'])))
for Ok in sorted(byk, reverse=True):
    L = byk[Ok]
    d = [x[0] for x in L]; own = [x[2] for x in L]; u = [x[3] for x in L]
    print(f"  |Omega_k| = {Ok:.0e}: chi_turn - chi0 = {min(d):.4f}..{max(d):.4f} rad "
          f"[(.. - pi)/sqrt|Ok| = {min(u):+.3f}..{max(u):+.3f}];  C41 with a_max = Om/|Ok|: {L[0][1]:.4f};"
          f"  C41 formula with own a_max: {min(own):.4f}..{max(own):.4f}")
print("  -> C41's 2.78 (1e-2) is the dust-from-today value at the V >= 0 floor a_max = 31.5; the integrated histories"
      " (a_max >= 102) give 2.94-3.21 rad there")

print("\n=== (2) conformal time of a closed de Sitter phase ===")
H, tt = sp.symbols('H t', positive=True)
R = sp.cosh(H*tt)/H
eta = 2*sp.atan(sp.tanh(H*tt/2))
print("  d eta/dt - 1/R(t) =", sp.simplify(sp.diff(eta, tt) - 1/R))
print("  eta(t -> oo) =", sp.limit(eta, tt, sp.oo))
for N in [5, 50, 60]:
    # N e-folds after the throat: R_end H = cosh(H t_end) ~ e^N/2 ... solve cosh(x) = e^N
    x = math.acosh(math.exp(N))
    print(f"  {N} e-folds after the throat: eta_end = {2*math.atan(math.tanh(x/2)):.15f} (pi/2 = {math.pi/2:.15f})")
Ri = sp.symbols('R_i', positive=True)
t_i = sp.acosh(H*Ri)/H
expr = sp.simplify(sp.pi/2 - eta.subs(tt, t_i))
for val in [1, 2, 10, 1e3]:
    num = float(expr.subs({H: 1, Ri: val}))
    print(f"  start at R_i = {val} c/H: eta added = {num:.6f}; arcsin(c/(H R_i)) = {math.asin(1/val):.6f}")

print("\n=== (3) light that starts at an inflationary throat (dust-cycloid approximation after inflation) ===")
def t_over_tturn(eta_post):
    return (eta_post - math.sin(eta_post))/math.pi
for label, eta0 in [('radiation bang (dynamics convention)', 0.0), ('throat start', math.pi/2)]:
    e_anti = math.pi - eta0
    e_circ = 2*math.pi - eta0
    print(f"  {label}: antipode at eta_post = {e_anti:.4f} -> a/a_max = {math.sin(e_anti/2)**2:.3f}, "
          f"t/t_turn = {t_over_tturn(e_anti):.3f};  full circuit at eta_post = {e_circ:.4f} -> "
          f"a/a_max = {math.sin(e_circ/2)**2:.3f} {'(collapse)' if e_circ > math.pi else ''}, t/t_turn = {t_over_tturn(e_circ):.3f}")
print("  (radiation-bang values in the dynamics grid: antipode at t/t_turn = 0.76-0.998, circuit near the crunch,"
      " phase-dependent; the throat start adds pi/2 and moves both well away from the turnaround and the crunch)")
