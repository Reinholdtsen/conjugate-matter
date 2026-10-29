"""Combined static operator K = p0^1/2 (1 + gt W) p0^1/2 (gravity + gated, long range).
- Lambda_0(gt, r): top eigenvalue (instability iff (k/k_J)^2 < Lambda_0)
- independent cross-check: secular equation built from the Mehler spectrum (Gaussian gate)
    1 = sum_N C_N / (Lambda - gt Lam_g q^N),  C_N = sum_{n1+n2+n3=N} a_n1^2 a_n2^2 a_n3^2
  a_n = <psi_n | p0_1D^1/2> (1D Hermite-function overlaps, computed by quadrature)
- critical gt at given kappa^2 = (k/k_J)^2
- mode structure: overlap of top eigenvector with the gravity (density) mode, velocity width of delta f
- Calc note #2 comparison
"""
import sys, math
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from static_threshold import top_eigs, Lam_g_closed, q_closed, p0, K_matrix

def hermite_overlaps(r, nmax):
    """a_n = int psi_n(x) g^{1/2}(x) dx, psi_n orthonormal eigenfunctions of the 1D symmetric
    kernel g^1/2(x) w(x-y) g^1/2(y) (Gaussian parameter gam = sqrt(1+4r^2)/4), g^1/2 = (2pi)^-1/4 e^{-x^2/4}.
    Computed by direct quadrature with stable Hermite-function recursion."""
    gam = 0.25*math.sqrt(1 + 4*r*r)
    x = np.linspace(-40, 40, 400001)
    dx = x[1] - x[0]
    y = np.sqrt(2*gam)*x
    # normalized Hermite functions h_n(y) (orthonormal in dy), psi_n(x) = (2 gam)^1/4 h_n(sqrt(2gam) x)
    h0 = np.pi**-0.25*np.exp(-y*y/2)
    h1 = np.sqrt(2.0)*y*h0
    g12 = (2*np.pi)**-0.25*np.exp(-x*x/4)
    a = np.zeros(nmax + 1)
    hm, h = h0, h1
    a[0] = np.sum((2*gam)**0.25*h0*g12)*dx
    a[1] = np.sum((2*gam)**0.25*h1*g12)*dx
    for n in range(1, nmax):
        hp = np.sqrt(2.0/(n + 1))*y*h - np.sqrt(n/(n + 1))*hm
        a[n + 1] = np.sum((2*gam)**0.25*hp*g12)*dx
        hm, h = h, hp
    return a

def secular_top(r, gt, nmax=None):
    q = q_closed(r); Lg = Lam_g_closed(r)
    if nmax is None:
        nmax = int(60 + 40*r)
    a = hermite_overlaps(r, nmax)
    c = a**2
    # C_N for 3D via convolution of 1D weights
    c2 = np.convolve(c, c)[:nmax + 1]
    C3 = np.convolve(c2, c)[:nmax + 1]
    N = np.arange(nmax + 1)
    s = gt*Lg*q**N
    # top root Lambda > max(s) where f(L) = 1 - sum C/(L - s)
    lo = max(s.max(), 0) + 1e-14
    hi = lo + 1 + gt + 10
    f = lambda L: 1 - np.sum(C3/(L - s))
    for _ in range(200):
        mid = 0.5*(lo + hi)
        if f(mid) > 0: hi = mid
        else: lo = mid
    return 0.5*(lo + hi), c.sum(), C3.sum()

def mode_info(r, gt, gate='gauss'):
    ev, v, w, vec = top_eigs(r, gt, 0, gate=gate, nev=2)
    phi = vec[:, 0]            # symmetrized eigenvector on L2(v^2 dv) with weights
    # phi_i = sqrt(w_i) v_i * sqrt(4pi) * phi(v_i)   (normalized)
    # density mode vector: d(v) = sqrt(p0(v)), normalized in L2(d^3v): int p0 d^3v = 1
    d = np.sqrt(4*np.pi*w)*v*np.sqrt(p0(v))
    ovl = abs(np.dot(phi, d))/np.linalg.norm(d)
    # delta f ∝ p0^1/2 phi(v):  phi(v_i) = phi_i/(sqrt(4 pi w_i) v_i)
    phiv = phi/(np.sqrt(4*np.pi*w)*v)
    df = np.sqrt(p0(v))*phiv
    if df.sum() < 0: df = -df
    m0 = np.sum(4*np.pi*w*v**2*df)
    m2 = np.sum(4*np.pi*w*v**4*df)
    vrms = math.sqrt(m2/m0)           # 3D rms speed of the perturbation (Maxwellian: sqrt(3))
    return ev, ovl, vrms

def crit_gt(r, kappa2, gate='gauss'):
    """smallest gt with Lambda_0(gt) = kappa2 (kappa2 > 1)"""
    lo, hi = 0.0, 1.0
    while top_eigs(r, hi, 0, gate=gate, nev=1)[0][0] < kappa2:
        hi *= 2
        if hi > 1e9: return np.inf
    for _ in range(50):
        mid = 0.5*(lo + hi)
        if top_eigs(r, mid, 0, gate=gate, nev=1)[0][0] < kappa2: lo = mid
        else: hi = mid
    return 0.5*(lo + hi)

if __name__ == '__main__':
    print("=== A. Lambda_0(gt, r), Gaussian gate: radial Nystrom vs Mehler secular equation ===")
    print(f"{'r':>7} {'gt':>8} {'Nystrom':>14} {'secular':>14} {'sum a^2':>10} {'1+gt*Lam_g':>12} {'gt*Lam_g':>12}")
    for r in [0.25, 1.2917, 4.0, 8.333]:
        for gt in [0.1, 1.0, 10.0, 100.0, 1000.0]:
            ny = top_eigs(r, gt, 0, nev=1)[0][0]
            se, s1, s3 = secular_top(r, gt)
            print(f"{r:7.4f} {gt:8.1f} {ny:14.8f} {se:14.8f} {s1:10.7f} {1+gt*Lam_g_closed(r):12.6f} {gt*Lam_g_closed(r):12.6f}")

    print("\n=== B. Mode structure of the top static mode (Gaussian gate) ===")
    print("overlap = |<phi, density mode>| (1 = pure Jeans/density mode); vrms = 3D rms speed of delta f in sigma (Maxwellian sqrt3 = 1.7321)")
    print(f"{'r':>7} {'gt':>8} {'Lambda_0':>12} {'Lambda_1':>12} {'overlap':>9} {'vrms':>8}  sqrt(3/(2 r)) [narrow-gate width est.]")
    for r in [0.25, 1.2917, 4.0, 8.333]:
        for gt in [0.0, 1.0, 10.0, 100.0, 1000.0, 1e4]:
            ev, ovl, vrms = mode_info(r, gt)
            print(f"{r:7.4f} {gt:8.0f} {ev[0]:12.6f} {ev[1]:12.6e} {ovl:9.5f} {vrms:8.4f}  {math.sqrt(3/(2*r)):.4f}")

    print("\n=== C. Critical gt = Gt/G at given kappa^2 = (k/k_J)^2 > 1 ===")
    print("broad-gate limit: gt_c = kappa^2 - 1 ; narrow-gate limit (stream mode): gt_c -> kappa^2/Lam_g")
    for gate in ['gauss', 'rat2']:
        for r in [0.25, 1.2917, 4.0, 8.333]:
            row = []
            for k2 in [1.1, 2.0, 4.4, 10.0, 25.0]:
                row.append(crit_gt(r, k2, gate))
            print(f"{gate:6s} r={r:7.4f}: gt_c(kappa^2=1.1,2,4.4,10,25) = " + ", ".join(f"{x:.4g}" for x in row)
                  + f"   [kappa^2/Lam_g(gauss) at 4.4: {4.4/Lam_g_closed(r):.4g}; kappa^2-1 at 4.4: 3.4]")

    print("\n=== D. Calc note #2 narrow-gate substitution vs the linearized result (contact range) ===")
    print("3a: g n_gate/(m v*^2) >= 1 with n_gate = n (v*/sigma)^3/(2pi)^1.5   [sigma -> v*]")
    print("exact static: g n Lam(r)/(m sigma^2) >= 1, Lam(r) = top eigenvalue of p0^1/2 W p0^1/2 (gate alone)")
    print("ratio R = (g required, exact)/(g required, 3a narrow form) = (2pi)^-1.5 r^-1 / Lam(r)  [Gaussian W = exp(-s^2/2)]")
    for r in [0.25, 1.2917, 2.0, 4.0, 8.333, 16.0, 32.0]:
        L = Lam_g_closed(r)
        R = (2*np.pi)**-1.5/(r*L)
        Rb = 1/L      # vs 3a broad form g n/(m sigma^2) >= 1
        print(f"r={r:7.4f}: Lam_g={L:.4e}; R(narrow form)={R:.4f}; R(broad form)={Rb:.4f}; (2pi)^-1.5 r^2={(2*np.pi)**-1.5*r*r:.4f}")
