"""Independent dynamic check: brute-force eigenvalues of the discretized linearized
Vlasov operator for axisymmetric (m=0) perturbations, no factorization of the gate,
no dispersion function. Units: sigma=1, time in t_ff = 1/sqrt(4 pi G rho), kap = k/k_J.

Mode equation (Jeans swindle, gate on canonical momenta, Maxwellian background):
  omega g(v) = kap v_z g(v) - (v_z/kap) p0(v) Int d^3v' [1 + gt W(|v-v'|/v*)] g(v')
(gravity-only, static: kap = 1, the Jeans criterion; cold limit: growth rate 1/t_ff).
Write g = p_perp(v_perp) u(v_z, v_perp), p_perp = exp(-v_perp^2/2)/(2 pi); then the
perpendicular integral becomes Gauss-Laguerre in t = v_perp^2/2, and
  omega u = kap v_z u - (v_z/kap) p_z(v_z) Sum_b [1 + gt Wz Wperp]_ab hz wGL_b u_b ,
with Wperp the azimuthal average exp(-(a^2+b^2)/2vs^2) I0(ab/vs^2) of the 3D Gaussian gate.
The v_z quadrature is the trapezoid rule: for a growing mode the integrand's nearest
singularity is at v_z = omega/kap, so the error falls like exp(-2 pi Im(omega)/(kap hz)).
Anchor: gt = 0 must reproduce the textbook stellar Jeans relation
  kap^2 = 1 - sqrt(pi) xi exp(xi^2) erfc(xi), xi = Gamma/(sqrt2 kap)  (Binney & Tremaine, dagger).
"""
import numpy as np, sys, time
import mpmath as mp

def i0e(x):
    x = np.asarray(x, float)
    out = np.empty_like(x)
    small = x < 600
    out[small] = np.i0(x[small]) * np.exp(-x[small])
    xb = x[~small]
    out[~small] = (1 + 1/(8*xb) + 9/(128*xb**2) + 225/(3072*xb**3)) / np.sqrt(2*np.pi*xb)
    return out

def build(kap, gt, r, Lz=5.5, hz=0.06, npp=10, m=0):
    vs = 1.0 / r
    nz = int(round(2 * Lz / hz)) + 1
    vz = np.linspace(-Lz, Lz, nz); hzz = vz[1] - vz[0]
    t, wgl = np.polynomial.laguerre.laggauss(npp)
    vp = np.sqrt(2 * t)
    pz = np.exp(-vz**2 / 2) / np.sqrt(2 * np.pi)
    Wz = np.exp(-(vz[:, None] - vz[None, :])**2 / (2 * vs**2))
    x = vp[:, None] * vp[None, :] / vs**2
    if m == 0:
        Wp = np.exp(-(vp[:, None] - vp[None, :])**2 / (2 * vs**2)) * i0e(x)
    else:
        raise NotImplementedError
    # K_ab with a=(i,j), b=(i',j'): 1 + gt*Wz[i,i']*Wp[j,j']
    N = nz * npp
    K = gt * np.kron(Wz, Wp)
    if m == 0:
        K += 1.0
    wb = np.kron(np.full(nz, hzz), wgl)          # weights for b
    lhs = np.kron(vz * pz, np.ones(npp))          # v_z p_z for a
    Lm = -(1.0 / kap) * lhs[:, None] * K * wb[None, :]
    Lm[np.diag_indices(N)] += kap * np.kron(vz, np.ones(npp))
    return Lm

def unstable(kap, gt, r, thr=0.02, **kw):
    t0 = time.time()
    Lm = build(kap, gt, r, **kw)
    ev = np.linalg.eigvals(Lm)
    del Lm
    ev = ev[ev.imag > thr]
    ev = ev[np.argsort(-ev.imag)]
    return ev, time.time() - t0

def jeans_closed(kap):
    f = lambda G: 1 - mp.sqrt(mp.pi) * (G/(mp.sqrt(2)*kap)) * mp.exp((G/(mp.sqrt(2)*kap))**2) * mp.erfc(G/(mp.sqrt(2)*kap)) - kap**2
    return float(mp.findroot(f, 0.7))

def fmt(ev):
    return ", ".join(f"{z.real:+.4f}{z.imag:+.5f}i" for z in ev[:6])

if __name__ == '__main__':
    which = sys.argv[1] if len(sys.argv) > 1 else 'anchor'
    if which == 'anchor':
        for kap in [0.5, 0.9]:
            ev, dt = unstable(kap, 0.0, 1.0, hz=0.1, npp=6)
            print(f"Jeans anchor kap={kap}: eig {fmt(ev)}  closed form Gamma={jeans_closed(kap):.8f}  [{dt:.1f}s]")
    elif which == 'mw':
        r = 155/120
        cases = [(4.9348, 56.14, 0.44210), (4.9348, 280.7, 0.56618)]
        for k2, gt, claim in cases:
            for hz, npp in [(0.075, 8), (0.06, 10), (0.05, 12)]:
                ev, dt = unstable(np.sqrt(k2), gt, r, hz=hz, npp=npp)
                print(f"MW kap^2={k2} gt={gt} hz={hz} npp={npp}: unstable {fmt(ev)}  (agent purely growing {claim}) [{dt:.0f}s]")
                sys.stdout.flush()
    elif which == 'odd':
        r = 155/120
        k2 = 19.7392
        for gt, claim, hz in [(240.0, 0.7666, 0.05), (255.0, 0.6866, 0.05), (272.0, 0.4692, 0.035)]:
            ev, dt = unstable(np.sqrt(k2), gt, r, hz=hz, npp=10)
            print(f"MW kap^2={k2} gt={gt} hz={hz}: unstable {fmt(ev)}  (agent purely growing {claim}) [{dt:.0f}s]")
            sys.stdout.flush()
    elif which == 'k30':
        r = 155/120
        ev, dt = unstable(np.sqrt(30.0), 280.7, r, hz=0.045, npp=10)
        print(f"MW kap^2=30 gt=280.7: unstable {fmt(ev)}  (agent 0.7783) [{dt:.0f}s]")
