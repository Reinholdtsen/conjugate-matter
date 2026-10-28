"""Verifier v06: linear modes as eigenvalues of the real generator (van Kampen matrix method).
Linearized Vlasov about a homogeneous Maxwellian, symmetric variable phi = p0^(-1/2) delta f:
    d phi/dt = -i kappa^-1 v_z (kappa^2 - K) phi,  K = p0^1/2 [1 + gt W] p0^1/2
so modes e^{-i Omega t} are eigenvalues of L = kappa^-1 V (kappa^2 - K) (real matrix).
Units: v in sigma, Omega in 1/t_ff = sqrt(4 pi G rho), kappa = k/k_J, r = sigma/v*.
Azimuthal number m about k (= z axis): m = 0 includes gravity; m != 0 is gate only.
Parity: L anticommutes with P_z, so L^2 on P_z-even functions gives Omega^2 (halves the size).
Gaussian gate: m-th azimuthal harmonic of W is exp(-r^2 (z-z')^2/2) exp(-r^2 (rho-rho')^2/2) Ie_m(r^2 rho rho'),
with Ie_m(x) = e^{-x} I_m(x) computed by trapezoid on (1/pi) int_0^pi e^{x(cos t - 1)} cos(m t) dt.
Anchor: gt = 0, m = 0 must reproduce the stellar Jeans growth rate (closed form, v01).
"""
import numpy as np

def Ie(m, x):
    x = np.asarray(x, float)
    nt = int(64 + 40 * np.sqrt(max(1.0, x.max())))
    t = np.linspace(0, np.pi, nt)
    w = np.full(nt, np.pi / (nt - 1)); w[0] *= 0.5; w[-1] *= 0.5
    out = np.zeros_like(x)
    for ti, wi in zip(t, w):
        out += wi * np.exp(x * (np.cos(ti) - 1.0)) * np.cos(m * ti)
    return out / np.pi

def grids(nz, nr, Z, P):
    xz, wz = np.polynomial.legendre.leggauss(nz)
    z, wz = Z * xz, Z * wz
    xr, wr = np.polynomial.legendre.leggauss(nr)
    rho, wr = 0.5 * P * (xr + 1), 0.5 * P * wr
    return z, wz, rho, wr

class Dyn:
    def __init__(self, r, m=0, nz=80, nr=40, Z=7.0, P=7.0):
        z, wz, rho, wr = grids(nz, nr, Z, P)
        pos = z > 0
        zp, wzp = z[pos], wz[pos]
        self.zp = zp
        nzp = len(zp)
        # weights for the half-space (z>0) block: w = wz * 2 pi rho wr
        Wz = np.sqrt(wzp)
        Wr = np.sqrt(2 * np.pi * rho * wr)
        sz = (2 * np.pi) ** -0.25 * np.exp(-zp**2 / 4) * Wz       # sqrt-weight * p0^1/2 (z part)
        sr = (2 * np.pi) ** -0.5 * np.exp(-rho**2 / 4) * Wr       # (rho part)
        # gate pieces
        Az_same = np.exp(-0.5 * r**2 * (zp[:, None] - zp[None, :]) ** 2)
        Az_refl = np.exp(-0.5 * r**2 * (zp[:, None] + zp[None, :]) ** 2)
        Ar = np.exp(-0.5 * r**2 * (rho[:, None] - rho[None, :]) ** 2) * Ie(m, r**2 * rho[:, None] * rho[None, :])
        Ze = sz[:, None] * (Az_same + Az_refl) * sz[None, :]
        Zo = sz[:, None] * (Az_same - Az_refl) * sz[None, :]
        R = sr[:, None] * Ar * sr[None, :]
        self.Kg_e = np.kron(Ze, R)
        self.Kg_o = np.kron(Zo, R)
        # gravity (m = 0 only): u u^T on full space; even part: u_e = sqrt(2) * u restricted
        if m == 0:
            u = np.kron(sz, sr)
            self.ue = u * np.sqrt(2.0)   # even-symmetrized normalization: <1,phi> over both halves
        else:
            self.ue = None
        self.D = np.kron(zp, np.ones(len(rho)))
        self.n = len(self.D)
        self.m = m

    def omegas(self, kap2, gt):
        kap = np.sqrt(kap2)
        Ke = gt * self.Kg_e
        if self.ue is not None:
            Ke = Ke + np.outer(self.ue, self.ue)
        Ko = gt * self.Kg_o
        I = np.eye(self.n)
        Ae = kap2 * I - Ke
        Ao = kap2 * I - Ko
        L2 = (self.D[:, None] * Ao) @ (self.D[:, None] * Ae) / kap2
        w2 = np.linalg.eigvals(L2)
        Om = np.sqrt(w2.astype(complex))
        Om = np.where(Om.imag < 0, -Om, Om)
        return Om

    def growing(self, kap2, gt, tol=1e-6):
        Om = self.omegas(kap2, gt)
        g = Om[Om.imag > tol]
        return g[np.argsort(-g.imag)]

if __name__ == "__main__":
    import time
    from mpmath import mp, findroot, sqrt, pi, exp, erfc
    # Anchor: Jeans
    for kap in [0.5, 0.8]:
        xi = findroot(lambda X: 1 - sqrt(pi) * X * exp(X**2) * erfc(X) - kap**2, 0.5)
        G = float(sqrt(2) * kap * xi)
        D = Dyn(1.2917, m=0, nz=60, nr=30)
        g = D.growing(kap**2, 0.0)
        print(f"anchor gt=0 kappa={kap}: Jeans closed-form Gamma={G:.6f}; L-matrix growing: {np.round(g[:3], 6)}")
