"""Own radial (l=0) Nystrom for the static operator, validated against static_fft3d.out,
then bisection for the critical gate strength at given (k/k_J)^2 and for the halo margins.

l=0 kernel: K0(v,v') = 4 pi v v' sqrt(w w') p0^(1/2)(v) p0^(1/2)(v') [1 + gt Wbar0(v,v')]
Wbar0 = angular average of the gate over the angle between v and v':
  gauss  W=exp(-s^2/2):   exp(-(v-v')^2/2vs^2) * (1-exp(-2vv'/vs^2))/(2vv'/vs^2)
  rat2   W=(1+s^2/2)^-2:  1/(A^2-B^2), A=1+(v^2+v'^2)/(2vs^2), B=vv'/vs^2
  rat1   W=(1+s^2/2)^-1:  ln((A+B)/(A-B))/(2B)
"""
import numpy as np

def nodes(n=400, vmax=10.0):
    x, w = np.polynomial.legendre.leggauss(n)
    v = 0.5 * vmax * (x + 1); w = 0.5 * vmax * w
    return v, w

V, WQ = nodes()

def wbar(gate, vs, v=V):
    a = v[:, None]; b = v[None, :]
    if gate == 'gauss':
        x = a * b / vs**2
        f = np.where(x > 1e-12, -np.expm1(-2 * x) / (2 * np.maximum(x, 1e-300)), 1.0 - x)
        return np.exp(-(a - b)**2 / (2 * vs**2)) * f
    A = 1 + (a**2 + b**2) / (2 * vs**2); B = a * b / vs**2
    if gate == 'rat2':
        return 1.0 / ((A - B) * (A + B))
    if gate == 'rat1':
        return np.where(B > 1e-14, np.log1p(2 * B / np.maximum(A - B, 1e-300)) / (2 * np.maximum(B, 1e-300)), 1.0 / A)
    raise ValueError

sq = np.sqrt(4 * np.pi * V**2 * WQ * (2 * np.pi) ** -1.5 * np.exp(-V**2 / 2))  # sqrt of radial measure * p0
_cache = {}
def mats(gate, r):
    key = (gate, r)
    if key not in _cache:
        Kg = sq[:, None] * wbar(gate, 1.0 / r, V) * sq[None, :]
        _cache[key] = Kg
    return _cache[key]

def lam0(gate, r, gt, grav=True, k=1):
    K = gt * mats(gate, r) + (np.outer(sq, sq) if grav else 0)
    ev = np.linalg.eigvalsh(K)[::-1]
    return ev[:k] if k > 1 else ev[0]

def avgW(gate, r):
    """pair-averaged gate <W> = <a|K_gate|a>, a = sq (normalised: |a|^2 = 1)."""
    return sq @ mats(gate, r) @ sq / (sq @ sq)

def bisect(f, lo, hi, tol=1e-10):
    flo = f(lo); fhi = f(hi)
    if flo * fhi > 0:
        return np.nan
    for _ in range(200):
        mid = np.sqrt(lo * hi) if lo > 0 else 0.5 * (lo + hi)
        fm = f(mid)
        if fm * flo > 0:
            lo, flo = mid, fm
        else:
            hi, fhi = mid, fm
        if hi / lo - 1 < tol:
            break
    return np.sqrt(lo * hi)

def gt_crit(gate, r, kap2):
    return bisect(lambda g: lam0(gate, r, g) - kap2, 1e-6, 1e7)

def gt_crit_revir(gate, r, Q):
    aw = avgW(gate, r)
    f = lambda g: lam0(gate, r, g) - Q * (1 + g * aw)
    gs = np.logspace(-4, 7, 300)
    vals = np.array([f(g) for g in gs])
    pos = np.where(vals > 0)[0]
    if len(pos) == 0:
        return np.inf, vals.max()
    i = pos[0]
    return bisect(f, gs[i - 1], gs[i]), vals.max()

if __name__ == '__main__':
    print("validation against the 3D grid (static_fft3d.out):")
    for gate, r, gt, ref in [('gauss', 1.2917, 10, 2.3050342), ('gauss', 1.2917, 100, 15.6331715),
                             ('gauss', 0.25, 1, 1.8398329), ('gauss', 4.0, 1e4, 107.742112),
                             ('gauss', 8.333, 1e4, 14.5485486), ('gauss', 1.2917, 281, 42.641968)]:
        print(f"  {gate} r={r} gt={gt}: radial {lam0(gate, r, gt):.7f}  3D {ref}")
    for gate, r in [('gauss', 8.333), ('gauss', 16.0), ('rat2', 8.333), ('rat2', 16.0), ('rat1', 8.333), ('rat1', 16.0)]:
        lg = lam0(gate, r, 1.0, grav=False)
        print(f"  {gate} gate only r={r}: Lam={lg:.5e}, Lam r^3={lg*r**3:.5f}, Lam r^2={lg*r**2:.5f}")
    # rational-gate asymptote check: does Lam r^3 approach sqrt(pi) for rat2?
    print("rat2 asymptote with a finer grid near v=0 (n=800, vmax=8):")
    V, WQ = nodes(800, 8.0)
    sq = np.sqrt(4 * np.pi * V**2 * WQ * (2 * np.pi) ** -1.5 * np.exp(-V**2 / 2)); _cache.clear()
    for r in [16.0, 32.0, 64.0]:
        lg = lam0('rat2', r, 1.0, grav=False)
        lgg = lam0('gauss', r, 1.0, grav=False)
        print(f"  r={r}: rat2 Lam r^3={lg*r**3:.4f} (sqrt(pi)={np.sqrt(np.pi):.4f});  gauss Lam r^3={lgg*r**3:.4f}")
    V, WQ = nodes(); sq = np.sqrt(4 * np.pi * V**2 * WQ * (2 * np.pi) ** -1.5 * np.exp(-V**2 / 2)); _cache.clear()

    print("\ncritical gt at (k/k_J)^2 = 1.1, 2, 4.4, 10, 25:")
    for gate in ['gauss', 'rat2']:
        for r in [0.25, 1.2917, 4.0, 8.333]:
            vals = [gt_crit(gate, r, k2) for k2 in [1.1, 2, 4.4, 10, 25]]
            print(f"  {gate:5s} r={r:7.4f}: " + ", ".join(f"{x:.4g}" for x in vals))
    print("\nhalo margins:")
    Qs = {'dwarf': [(np.pi/3)**2, (2*np.pi/3)**2], 'MW': [np.pi**2/2, 2*np.pi**2, 24.77],
          'cluster': [(np.pi/3)**2, (2*np.pi/3)**2]}
    rs = {'dwarf': 30/120, 'MW': 155/120, 'cluster': 1000/120}
    for env in ['dwarf', 'MW', 'cluster']:
        r = rs[env]
        aw = avgW('gauss', r); lg = lam0('gauss', r, 1.0, grav=False)
        print(f"  {env}: r={r:.4f}  Lam_g={lg:.5e} <W>={aw:.5e} closed (1+2r^2)^-1.5={(1+2*r*r)**-1.5:.5e} Lam_g/<W>={lg/aw:.4f}")
        for Q in Qs[env]:
            out = []
            for gate in ['gauss', 'rat2']:
                g1 = gt_crit(gate, r, Q)
                g2, mx = gt_crit_revir(gate, r, Q)
                out.append(f"{gate}: no-revir {g1:.4g}, revir {g2:.4g}")
            print(f"     Q={Q:.4f}: " + " | ".join(out))
    for r in [64.0]:
        V, WQ = nodes(800, 8.0)
        sq = np.sqrt(4 * np.pi * V**2 * WQ * (2 * np.pi) ** -1.5 * np.exp(-V**2 / 2)); _cache.clear()
        print(f"  r={r}: gauss Lam_g/<W> = {lam0('gauss', r, 1.0, grav=False)/avgW('gauss', r):.4f} (limit 2^1.5={2**1.5:.4f})")
