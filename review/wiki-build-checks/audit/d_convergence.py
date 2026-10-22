# Flag 27 audit, part D: step-size convergence of part B's numbers (halve the step, compare).
import b_turnaround_numerics as b

for hfac in (3e-3, 1.5e-3):
    b.HFAC = hfac
    V0 = b.shoot_V0(1.0, 0.2, 1.0)                       # V0 cos(tau/f), f = 1, tau_i/f = 0.2
    o = b.run(V0, 1.0, 0.2, 1.0)
    print(f"HFAC = {hfac}: V0 cos  V0 = {V0:.6f}, t_turn - t0 = {o['turn']['dt']:.5f}/H0,"
          f" a_turn = {o['turn']['a']:.5f}, V_turn = {o['turn']['V']:+.5f}", flush=True)
    V0d = b.shoot_V0(1.0, 0.2, 0.0)                      # documents' form
    od = b.run(V0d, 1.0, 0.2, 0.0, t_after=50.0)
    print(f"HFAC = {hfac}: doc form V0 = {V0d:.6f}, after 50/H0: min H = {od['minH']:.5e},"
          f" min rho_tot = {od['minrho']:.5e}, |3H^2-rho| = {od['Cabs_last']:.1e}", flush=True)
