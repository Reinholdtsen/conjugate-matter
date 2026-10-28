"""Static (omega = 0) stability operator for a homogeneous Maxwellian gas with
pair energy  U = -m^2 [G + Gt W(|v-v'|/v*)] / |x-x'|   (Jeans swindle).

Units: velocities in sigma (1D dispersion); wavenumbers in k_J = sqrt(4 pi G rho)/sigma.
Linearized Vlasov, static limit, Maxwellian:  delta_f = -(f0/(m sigma^2)) delta_eps, so
    delta_eps(v) = (k_J/k)^2  Int d^3v' [1 + gt W] p0(v') delta_eps(v')
p0 = normalized Maxwellian, gt = Gt/G.  Symmetrized operator K = p0^1/2 (1 + gt W) p0^1/2.
Instability at wavenumber k  <=>  Lambda_max(K) > (k/k_J)^2.
r = sigma/v*.  Gates (s = |v - v'|/v*):
   gauss : W = exp(-s^2/2)
   rat2  : W = (1 + s^2/2)^-2   (same curvature at s=0, integrable tail ~ s^-4)
   rat1  : W = (1 + s^2/2)^-1   (tail ~ s^-2, not integrable in 3D)
"""
import numpy as np
from numpy.polynomial.legendre import leggauss
import math, sys

# ---------- closed forms (Gaussian gate, Mehler kernel) ----------
def Lam_g_closed(r):
    """top eigenvalue of p0^1/2 W p0^1/2 (gated part alone), Gaussian W"""
    return (0.5 + r**2 + 0.5*np.sqrt(1 + 4*r**2))**-1.5

def q_closed(r):
    """ratio of successive 1D eigenvalues; 3D level N has eigenvalue Lam_g q^N"""
    return 2*r**2/(1 + 2*r**2 + np.sqrt(1 + 4*r**2))

# ---------- angular projections W_l(v,v') = 1/2 Int_{-1}^{1} W P_l(mu) dmu ----------
def _ezil(l, z):
    """exp(-z) i_l(z), modified spherical Bessel of the first kind, stable"""
    z = np.asarray(z, dtype=float)
    out = np.empty_like(z)
    small = z < 0.5
    zs = z[small]
    # power series i_l(z) = sum_k z^(l+2k) / (2^k k! (2l+2k+1)!!)
    ser = np.zeros_like(zs)
    for k in range(0, 12):
        dfact = 1.0
        for j in range(1, 2*l + 2*k + 2, 2):
            dfact *= j
        ser += zs**(l + 2*k)/(2**k*math.factorial(k)*dfact)
    out[small] = np.exp(-zs)*ser
    zl = z[~small]
    e2 = np.exp(-2*zl)
    sh = (1 - e2)/2          # e^-z sinh z
    ch = (1 + e2)/2          # e^-z cosh z
    if l == 0:
        out[~small] = sh/zl
    elif l == 1:
        out[~small] = ch/zl - sh/zl**2
    elif l == 2:
        out[~small] = (3/zl**2 + 1)*sh/zl - 3*ch/zl**2
    else:
        raise ValueError
    return out

def W_l(gate, l, v, vp, vstar):
    V, VP = np.meshgrid(v, vp, indexing='ij')
    if gate == 'gauss':
        d = (V - VP)**2/(2*vstar**2)
        z = V*VP/vstar**2
        return np.exp(-d)*_ezil(l, z)
    A = 1 + (V**2 + VP**2)/(2*vstar**2)
    B = V*VP/vstar**2
    AmB = 1 + (V - VP)**2/(2*vstar**2)
    ApB = 1 + (V + VP)**2/(2*vstar**2)
    eps = B/A
    if gate == 'rat2':
        if l == 0:
            return 1/(AmB*ApB)
        if l == 1:
            out = np.empty_like(A)
            sm = eps < 0.3
            # series (1/A^2) sum_k (2k/(2k+1)) eps^(2k-1)
            e = eps[sm]
            ser = np.zeros_like(e)
            for k in range(1, 40):
                ser += (2*k/(2*k + 1))*e**(2*k - 1)
            out[sm] = ser/A[sm]**2
            Bl, Al = B[~sm], A[~sm]
            out[~sm] = (Al*Bl/(AmB[~sm]*ApB[~sm]) - 0.5*np.log(ApB[~sm]/AmB[~sm]))/Bl**2
            return out
        raise ValueError
    if gate == 'rat1':
        if l == 0:
            x = 2*B/AmB
            with np.errstate(divide='ignore', invalid='ignore'):
                f = np.where(x < 1e-8, 1 - x/2, np.log1p(x)/np.where(x == 0, 1, x))
            return f/AmB
        raise ValueError
    raise ValueError(gate)

# ---------- radial Nystrom discretization ----------
def grid(vstar, vmax=10.0, order=10, hmax=0.5, frac=0.75):
    h = min(hmax, frac*vstar)
    npan = int(np.ceil(vmax/h))
    x, w = leggauss(order)
    edges = np.linspace(0, vmax, npan + 1)
    a, b = edges[:-1, None], edges[1:, None]
    nodes = (0.5*(b - a)*x[None, :] + 0.5*(a + b)).ravel()
    wts = (0.5*(b - a)*w[None, :]).ravel()
    return nodes, wts

def p0(v):
    return (2*np.pi)**-1.5*np.exp(-v**2/2)

def K_matrix(r, gt, l, gate='gauss', grav=True, **gk):
    vstar = 1.0/r
    v, w = grid(vstar, **gk)
    sq = np.sqrt(4*np.pi*p0(v)*w)*v      # sqrt(4 pi p0 w) v
    M = gt*W_l(gate, l, v, v, vstar)
    if grav and l == 0:
        M = M + 1.0
    M *= sq[:, None]*sq[None, :]
    return v, w, M

def top_eigs(r, gt, l, gate='gauss', grav=True, nev=3, **gk):
    v, w, M = K_matrix(r, gt, l, gate, grav, **gk)
    ev, evec = np.linalg.eigh(M)
    return ev[::-1][:nev], v, w, evec[:, ::-1][:, :nev]

if __name__ == '__main__':
    np.set_printoptions(linewidth=140)
    print("=== 1. Gated part alone (no gravity): numerics vs Mehler closed form ===")
    print("Lam_g(r) = [1/2 + r^2 + sqrt(1+4r^2)/2]^(-3/2); top eigenvalue in sector l = Lam_g q^l")
    print(f"{'r':>6} {'closed l0':>12} {'num l0':>12} {'closed l1':>12} {'num l1':>12} {'closed l2':>12} {'num l2':>12}")
    for r in [0.1, 0.25, 0.5, 1.0, 1.2917, 2.0, 4.0, 8.333]:
        L, q = Lam_g_closed(r), q_closed(r)
        nums = [top_eigs(r, 1.0, l, grav=False, nev=1)[0][0] for l in (0, 1, 2)]
        print(f"{r:6.3f} {L:12.6e} {nums[0]:12.6e} {L*q:12.6e} {nums[1]:12.6e} {L*q*q:12.6e} {nums[2]:12.6e}")

    print("\n=== 2. Convergence check (Gaussian, gt=1, gravity on, l=0) ===")
    for r in [1.2917, 8.333]:
        for frac, order in [(0.75, 10), (0.4, 12)]:
            e = top_eigs(r, 1.0, 0, frac=frac, order=order, nev=1)[0][0]
            print(f"r={r}: frac={frac} order={order}: Lambda_0 = {e:.10f}")

    print("\n=== 3. Gravity alone: Lambda_0 = 1 exactly (Jeans: k_crit = k_J) ===")
    print("gt=0:", top_eigs(1.0, 0.0, 0, nev=2)[0])

    print("\n=== 4. Narrow-gate asymptotics of the gated eigenvalue: Lam_g -> (v*/sigma)^3 * Int d^3s W/(2pi)^1.5 ===")
    print("Gaussian: Int d^3s W = (2pi)^1.5 -> factor 1; rat2: Int = 2^1.5 pi^2 -> factor sqrt(pi) = %.6f" % math.sqrt(math.pi))
    for gate in ['gauss', 'rat2', 'rat1']:
        for r in [0.25, 1.2917, 4.0, 8.333, 16.0]:
            e = top_eigs(r, 1.0, 0, gate=gate, grav=False, nev=1)[0][0]
            print(f"{gate:6s} r={r:7.4f}: Lam_g = {e:.5e}; Lam_g*r^3 = {e*r**3:.5f}; Lam_g*r^2 = {e*r**2:.5f}")
