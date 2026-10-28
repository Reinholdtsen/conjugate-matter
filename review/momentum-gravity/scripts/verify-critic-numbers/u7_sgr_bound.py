"""verify-critic-numbers, claim sgr: Sagittarius-stream bound on a long-range chi-chi attraction
U = -Gt m^2 W(|v - v'|/v*)/|x - x'| with the amplitude gate W = exp(-s^2/2), v* = 120 km/s.

Literature [S, this session]:
  Kesden & Kamionkowski, PRD 74, 083007 (2006) (astro-ph/0608095): DM-DM fifth force = beta^2 x gravity,
  inverse-square, acting between all DM pairs (inside the satellite, inside the host, and between them);
  'a dark-matter force greater than 10% the strength of gravity is already excluded' (2MASS Sgr streams);
  no statistical confidence level; results called 'far from conclusive'.  beta = 0.2 (4%) gives leading/trailing
  < 0.2 versus 0.66 without the force.  PRL 97, 131303 (2006): acceleration difference > ~10% challenged.
  Keselman, Nusser & Peebles, PRD 80, 063517 (2009): symmetric Sgr-like streams possible with a force
  comparable to gravity if the force separates stars from DM first (Sgr then holds little DM now).
  Kesden, PRD 80, 083530 (2009): disputes KNP's initial conditions; repeats the 10% exclusion; leaves a
  very-massive-satellite loophole.
  Sgr now (Vasiliev & Belokurov 2020, MNRAS 497, 4162): Galactocentric (X, Y, Z) = (17.5, 2.5, -6.5) kpc,
  (VX, VY, VZ) = (237.9, -24.3, 209.0) km/s.
Mapping (my reading): the gated force between host DM and satellite DM is eps <W> x gravity, so KK's beta^2
corresponds to eps <W>, with <W> the gate averaged over the host DM velocity distribution relative to Sgr.
Host DM: isotropic Maxwellian, mean at rest, dispersion sigma_h(r) from the isotropic Jeans equation of
the NFW halo in the total potential (a model), compared with stellar-halo values (~100 km/s, [S] via review
snippet).  Satellite internal dispersion 12 km/s (dagger) added in quadrature.
MW potentials (dagger, parameters from memory): three toy models spanning light to heavy halos.
REDUCED-MODEL caveats: rigid static host, no LMC, no dynamical friction or mass loss, test-particle orbit.
"""
import numpy as np

Gk = 4.30091e-6          # kpc (km/s)^2 / Msun
VSTAR = 120.0
KMS_KPC_GYR = 1.0227     # 1 km/s = 1.0227 kpc/Gyr


def gate(V, sig_rel, vs=VSTAR):
    s2 = vs**2 + sig_rel**2
    return (vs**2 / s2) ** 1.5 * np.exp(-V**2 / (2 * s2))


def gate_mc(V, sig_rel, vs=VSTAR, n=400_000, nrun=10):
    out = []
    for k in range(nrun):
        rng = np.random.default_rng(777 + k)
        u = rng.normal(0.0, sig_rel, size=(n, 3))
        u[:, 0] += V
        out.append(np.mean(np.exp(-np.sum(u**2, axis=1) / (2 * vs**2))))
    out = np.array(out)
    return out.mean(), out.std(ddof=1) / np.sqrt(nrun)


class MW:
    def __init__(self, Mb, ab, Md, ad, bd, rho_s, rs, name):
        self.Mb, self.ab, self.Md, self.ad, self.bd, self.rho_s, self.rs, self.name = Mb, ab, Md, ad, bd, rho_s, rs, name

    def acc(self, x):
        R2 = x[0]**2 + x[1]**2
        r = np.sqrt(R2 + x[2]**2)
        a = -Gk * self.Mb / (r * (r + self.ab) ** 2) * x                       # Hernquist
        zb = np.sqrt(x[2]**2 + self.bd**2)
        den = (R2 + (self.ad + zb) ** 2) ** 1.5
        ad_ = -Gk * self.Md / den * np.array([x[0], x[1], x[2] * (self.ad + zb) / zb])   # Miyamoto-Nagai
        Mh = 4 * np.pi * self.rho_s * self.rs**3 * (np.log(1 + r / self.rs) - r / (r + self.rs))
        ah = -Gk * Mh / r**3 * x                                                 # NFW
        return a + ad_ + ah

    def Menc_sph(self, r):
        """spherical approximation of enclosed mass (disk treated as a point mass at large r, adequate for r >~ 15 kpc)"""
        Mh = 4 * np.pi * self.rho_s * self.rs**3 * (np.log(1 + r / self.rs) - r / (r + self.rs))
        return self.Mb * r**2 / (r + self.ab) ** 2 + self.Md * r**3 / (r**2 + (self.ad + self.bd) ** 2) ** 1.5 + Mh

    def vc(self, R):
        x = np.array([R, 0.0, 0.0])
        return np.sqrt(-self.acc(x)[0] * R)

    def rho_h(self, r):
        y = r / self.rs
        return self.rho_s / (y * (1 + y) ** 2)

    def sigma_dm(self, r):
        """isotropic Jeans: sigma^2(r) = (1/rho) int_r^inf rho G M(<r')/r'^2 dr'  (spherical approximation)"""
        rr = np.logspace(np.log10(r), np.log10(r) + 4, 4000)
        integ = self.rho_h(rr) * Gk * self.Menc_sph(rr) / rr**2
        return np.sqrt(np.trapezoid(integ, rr) / self.rho_h(r))

    def m200(self):
        rho_c = 3 * (67.4 / 1000) ** 2 / (8 * np.pi * Gk) * 1e0   # H in km/s/kpc -> Msun/kpc^3
        rgrid = np.logspace(0, 3, 3000)
        M = np.array([self.Menc_sph(r) for r in rgrid])
        dens = M / (4 / 3 * np.pi * rgrid**3)
        i = np.argmin(np.abs(dens - 200 * rho_c))
        return rgrid[i], M[i]


def nfw_rho_s_for_vc(base, vc_target, R0=8.2):
    lo, hi = 1e5, 1e9
    for _ in range(100):
        mid = np.sqrt(lo * hi)
        base.rho_s = mid
        if base.vc(R0) < vc_target:
            lo = mid
        else:
            hi = mid
    return base


models = []
# (1) light halo, disk-heavy (MWPotential2014-like shapes, dagger); (2) KK-like (WD05 MWb masses quoted by KK [S]); (3) heavier halo
m1 = nfw_rho_s_for_vc(MW(0.5e10, 0.6, 6.8e10, 3.0, 0.28, 1e7, 16.0, "light halo, rs=16"), 220.0)
m2 = nfw_rho_s_for_vc(MW(1.19e10, 0.6, 3.52e10, 3.0, 0.3, 1e7, 8.8, "KK-like masses, rs=8.8"), 230.0)
m3 = nfw_rho_s_for_vc(MW(0.9e10, 0.6, 5.0e10, 3.0, 0.28, 1e7, 20.0, "heavier halo, rs=20"), 240.0)
models = [m1, m2, m3]

x0 = np.array([17.5, 2.5, -6.5])
v0 = np.array([237.9, -24.3, 209.0])
print(f"Sgr now: r = {np.linalg.norm(x0):.2f} kpc, |V| = {np.linalg.norm(v0):.1f} km/s (VB20 [S])")
print("gate check, closed form vs MC (V = 317.6, sigma_rel = 120): ", f"{gate(317.6, 120.0):.5f}", "MC %.5f +- %.5f" % gate_mc(317.6, 120.0))

SIG_SAT = 12.0
results = []
for M in models:
    rv, Mv = M.m200()
    print(f"\n== model: {M.name}: Vc(8.2) = {M.vc(8.2):.1f} km/s, Vc(50) = {M.vc(50.0):.1f}, r200 = {rv:.0f} kpc, M200 = {Mv:.2e} Msun")
    sig_tab_r = np.linspace(8, 120, 113)
    sig_tab = np.array([M.sigma_dm(r) for r in sig_tab_r])
    print("   DM sigma_1D (Jeans): " + ", ".join(f"r={r:.0f}: {M.sigma_dm(r):.0f}" for r in (15, 20, 30, 45, 60)))
    # leapfrog backward 3 Gyr (time in Gyr, velocities converted)
    dt = -1e-4
    x = x0.copy(); v = v0.copy() * KMS_KPC_GYR
    nstep = int(3.0 / abs(dt))
    rs_, Vs_ = [], []
    a = M.acc(x) * KMS_KPC_GYR**2
    for i in range(nstep):
        v = v + 0.5 * dt * a
        x = x + dt * v
        a = M.acc(x) * KMS_KPC_GYR**2
        v = v + 0.5 * dt * a
        rs_.append(np.linalg.norm(x)); Vs_.append(np.linalg.norm(v) / KMS_KPC_GYR)
    rs_ = np.array(rs_); Vs_ = np.array(Vs_)
    print(f"   orbit (3 Gyr back): pericentre {rs_.min():.1f} kpc, apocentre {rs_.max():.1f} kpc")
    sig_h = np.interp(rs_, sig_tab_r, sig_tab)
    for label, sh_override in (("Jeans DM sigma", None), ("stellar-halo sigma = 100", 100.0), ("sigma = 150", 150.0)):
        sh = sig_h if sh_override is None else np.full_like(rs_, sh_override)
        srel = np.sqrt(sh**2 + SIG_SAT**2)
        Wt = gate(Vs_, srel)
        gDM = Gk * (4 * np.pi * M.rho_s * M.rs**3 * (np.log(1 + rs_ / M.rs) - rs_ / (rs_ + M.rs))) / rs_**2
        W_now = gate(np.linalg.norm(v0), np.sqrt((sh_override if sh_override else M.sigma_dm(np.linalg.norm(x0)))**2 + SIG_SAT**2))
        W_tavg = Wt.mean()
        W_gwt = np.sum(Wt * gDM) / np.sum(gDM)
        near_peri = rs_ < np.percentile(rs_, 20)
        W_peri = Wt[near_peri].mean()
        res = dict(model=M.name, sig=label, now=W_now, tavg=W_tavg, gwt=W_gwt, peri=W_peri)
        results.append(res)
        print(f"   {label:26s}: <W> now {W_now:.4f} | time-avg {W_tavg:.4f} | g_DM-weighted {W_gwt:.4f} | "
              f"innermost-20%-of-time {W_peri:.4f}  ->  eps < 0.1/<W>: {0.1/W_now:.2f} | {0.1/W_tavg:.2f} | {0.1/W_gwt:.2f} | {0.1/W_peri:.2f}")

allW = np.array([[r['now'], r['tavg'], r['gwt'], r['peri']] for r in results])
print(f"\nrange over models, dispersions and weightings: <W> in [{allW.min():.4f}, {allW.max():.4f}]  ->  "
      f"eps_max = 0.1/<W> in [{0.1/allW.max():.2f}, {0.1/allW.min():.2f}]")
jeans = np.array([[r['now'], r['tavg'], r['gwt'], r['peri']] for r in results if r['sig'] == 'Jeans DM sigma'])
print(f"Jeans-DM-sigma rows only: eps_max in [{0.1/jeans.max():.2f}, {0.1/jeans.min():.2f}]")
print(f"with KK's 4% detectability level (beta = 0.2) instead of 10%: eps_max in [{0.04/allW.max():.2f}, {0.04/allW.min():.2f}]")
print("in the ordinary-tests convention exp(-v^2/v_a^2) the same bound refers to v_a = sqrt2 x 120 = 169.7 km/s")
