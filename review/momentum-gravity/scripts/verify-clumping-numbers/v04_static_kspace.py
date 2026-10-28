"""Verifier v04: static operator K = u u^T + gt M_u (W *) M_u in FOURIER space (l = 0 sector).
K = B^dag B with B = [<u,.>; gt^(1/2) What^(1/2) F M_u]; the nonzero spectrum of K equals that of
B B^dag = [[1, b^T], [b, gt What^(1/2) (2pi)^-3 P(k-k') What^(1/2)]],  P(q) = exp(-q^2/2).
l=0 radial kernel: gt What(k)^(1/2) What(k')^(1/2) (1/(2 pi^2)) [e^{-(k-k')^2/2} - e^{-(k+k')^2/2}]/2;
b(k) = sqrt(4 pi) k gt^(1/2) What(k)^(1/2) (2pi)^(-3/2) e^{-k^2/2}.  sigma = 1, a = sqrt2/r.
Gates (s = |u|/v*):  gauss  W = exp(-s^2/2)      What = (2pi)^1.5 v*^3 exp(-v*^2 k^2/2)
                     rat2   W = (1+s^2/2)^-2     What = pi^2 a^3 exp(-a k)
                     rat1   W = (1+s^2/2)^-1     What = 2 pi^2 a^2 exp(-a k)/k
                     inv2   W = 2/s^2 (limit)    What = 2 * v*^2 * 2 pi^2 / k
"""
import numpy as np

def What(kind, k, r):
    vs = 1.0 / r
    a = np.sqrt(2.0) * vs
    if kind == 'gauss':
        return (2 * np.pi) ** 1.5 * vs**3 * np.exp(-0.5 * vs**2 * k**2)
    if kind == 'rat2':
        return np.pi**2 * a**3 * np.exp(-a * k)
    if kind == 'rat1':
        return 2 * np.pi**2 * a**2 * np.exp(-a * k) / k
    if kind == 'inv2':
        return 2 * vs**2 * 2 * np.pi**2 / k
    raise ValueError

class KStatic:
    def __init__(self, kind, r, N=None, kmax=None):
        self.kind, self.r = kind, r
        a = np.sqrt(2.0) / r
        if kmax is None:
            if kind == 'gauss':
                kmax = max(12.0, 9.0 * r)
            elif kind == 'inv2':
                kmax = 60.0
            else:
                kmax = max(14.0, 46.0 / a)
        if N is None:
            N = int(min(3000, max(300, 5 * kmax)))
        x, w = np.polynomial.legendre.leggauss(N)
        k = 0.5 * kmax * (x + 1)
        w = 0.5 * kmax * w
        sw = np.sqrt(w)
        Wh = What(kind, k, r)
        sq = np.sqrt(Wh)
        kern = (np.exp(-0.5 * (k[:, None] - k[None, :]) ** 2) - np.exp(-0.5 * (k[:, None] + k[None, :]) ** 2)) / 2
        self.G = (sw * sq)[:, None] * kern / (2 * np.pi**2) * (sw * sq)[None, :]
        self.b1 = np.sqrt(4 * np.pi) * k * sq * (2 * np.pi) ** -1.5 * np.exp(-0.5 * k**2) * sw
        self.k, self.N, self.kmax = k, N, kmax
        self.gate_eigs = np.linalg.eigvalsh(self.G)[::-1]
        self.Lam_g = self.gate_eigs[0]

    def eigs(self, gt):
        M = np.zeros((self.N + 1, self.N + 1))
        M[0, 0] = 1.0
        M[0, 1:] = np.sqrt(gt) * self.b1
        M[1:, 0] = np.sqrt(gt) * self.b1
        M[1:, 1:] = gt * self.G
        return np.linalg.eigvalsh(M)[::-1]

    def top(self, gt):
        return self.eigs(gt)[0]

    def gt_crit(self, kap2):
        lo, hi = 0.0, 1.0
        while self.top(hi) < kap2:
            hi *= 2
        for _ in range(60):
            mid = 0.5 * (lo + hi)
            lo, hi = (mid, hi) if self.top(mid) < kap2 else (lo, mid)
        return 0.5 * (lo + hi)

def closed_gauss(r):
    return (0.5 + r**2 + np.sqrt(1 + 4 * r**2) / 2) ** -1.5

if __name__ == "__main__":
    print("Check 1 (method anchor): Gaussian gate in k-space vs Mehler closed form; gt=0 gives 1")
    for r in [0.25, 1.2917, 8.333]:
        S = KStatic('gauss', r)
        print(f"  r={r}: Lam_g(kspace)={S.Lam_g:.7e}  closed={closed_gauss(r):.7e};  top(gt=0)={S.top(0.0):.8f}; top(gt=10)={S.top(10.0):.8f}")
    print("\nNarrow-gate limits (C4):")
    for kind in ['rat2', 'rat1']:
        for r in [8.333, 16.0]:
            S = KStatic(kind, r)
            S2 = KStatic(kind, r, N=int(S.N * 1.3), kmax=S.kmax * 1.3)
            print(f"  {kind} r={r}: Lam_g={S.Lam_g:.6e} (refined {S2.Lam_g:.6e}); Lam_g r^3={S.Lam_g*r**3:.5f}; Lam_g r^2={S.Lam_g*r**2:.5f}")
    for r in [32.0, 64.0, 128.0]:
        S = KStatic('rat2', r)
        print(f"  rat2 r={r}: Lam_g r^3={S.Lam_g*r**3:.5f}   (claimed limit sqrt(pi)={np.sqrt(np.pi):.5f})")
    for r in [32.0, 64.0, 128.0]:
        S = KStatic('rat1', r)
        print(f"  rat1 r={r}: Lam_g r^2={S.Lam_g*r**2:.5f}")
    S = KStatic('inv2', 1.0)
    print(f"  rat1 limit: Lam r^2 -> top eigenvalue of 2 p0^1/2 |u|^-2 p0^1/2 = {S.Lam_g:.5f}")
