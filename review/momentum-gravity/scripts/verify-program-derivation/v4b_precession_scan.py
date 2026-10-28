"""Verifier scan for P13's 'saturates at about 0.2-0.3 rad per orbit for beta = 0.2' statement.
Same Hamiltonian and integrator as v4_gated_orbits.py (imported); orbits tuned so that the measured
eccentricity is 0.3 (r_p fixed, pericentre speed bisected), then 6 orbits measured."""
import importlib.util
import sys
import numpy as np
spec = importlib.util.spec_from_file_location("v4", __file__.replace("v4b_precession_scan.py", "v4_gated_orbits.py"))
src = open(spec.origin).read()
# reuse only the numerical machinery (skip the top-level runs)
ns = {"np": np}
exec(src.split("print()\nprint(\"bound orbits")[0].split("# ---------------- numerics ----------------")[1], ns)
make_rhs, adaptive, step, radial, ham = ns['make_rhs'], ns['adaptive'], ns['step'], ns['radial'], ns['ham']


def half_orbit_ra(beta, rp, vp):
    f = make_rhs(beta)
    y = np.array([rp, 0.0, 0.0, vp]); h = 1e-3*rp/vp
    prev = radial(f, y); rmax = rp; t = 0
    while True:
        yn, hu, hn = adaptive(f, y, h)
        cur = radial(f, yn); rmax = max(rmax, np.hypot(*yn[:2]))
        if prev > 0 >= cur:
            lo, hi = 0.0, hu
            for _ in range(60):
                mid = 0.5*(lo + hi)
                ym, _ = step(f, y, mid)
                if radial(f, ym) > 0: lo = mid
                else: hi = mid
            ym, _ = step(f, y, 0.5*(lo + hi))
            return np.hypot(*ym[:2])
        y, h, prev = yn, hn, cur
        t += hu
        if t > 1e7:
            return np.inf


def tuned(beta, a_t, e_t):
    rp = a_t*(1 - e_t)
    lo, hi = 0.5*np.sqrt(1/rp), 3*np.sqrt(2/rp)
    for _ in range(60):
        vp = 0.5*(lo + hi)
        ra = half_orbit_ra(beta, rp, vp)
        e = (ra - rp)/(ra + rp) if np.isfinite(ra) else 2
        if e > e_t: hi = vp
        else: lo = vp
    return rp, 0.5*(lo + hi)


def precession(beta, rp, vp, norb=6):
    f = make_rhs(beta)
    y = np.array([rp, 0.0, 0.0, vp]); h = 1e-3*rp/vp
    prev = radial(f, y); peri = [0.0]; rmax = rp
    while len(peri) < norb + 1:
        yn, hu, hn = adaptive(f, y, h)
        cur = radial(f, yn); rmax = max(rmax, np.hypot(*yn[:2]))
        if prev < 0 <= cur:
            lo, hi = 0.0, hu
            for _ in range(60):
                mid = 0.5*(lo + hi)
                ym, _ = step(f, y, mid)
                if radial(f, ym) < 0: lo = mid
                else: hi = mid
            ym, _ = step(f, y, 0.5*(lo + hi))
            peri.append(np.arctan2(ym[1], ym[0]))
        y, h, prev = yn, hn, cur
    return np.mean(np.diff(np.unwrap(peri))), rmax


beta = 0.2
print("beta = 0.2, measured e tuned to 0.30: GM/(a v*^2), dw/orbit (rad), leading-order formula, ratio, peak p at pericentre")
for x in (0.01, 0.03, 0.1, 0.2, 0.3, 0.5, 1.0, 2.0):
    a_t = 1/x
    rp, vp = tuned(beta, a_t, 0.3)
    dw, rmax = precession(beta, rp, vp)
    am = 0.5*(rp + rmax); em = (rmax - rp)/(rmax + rp)
    pred = -4*np.pi*beta/(am*(1 - em**2))
    print(f"  {x:5.2f}  {dw: .4e}  {pred: .4e}  {dw/pred:6.3f}   (a, e) = ({am:.4f}, {em:.4f})  p_peri = {vp:.3f}", flush=True)
