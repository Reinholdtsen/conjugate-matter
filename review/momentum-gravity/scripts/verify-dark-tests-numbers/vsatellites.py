"""Satellite, Bullet Cluster and dwarf gate factors (K13-K15), by Monte Carlo (a different method
from a closed form), plus an independent Galactocentric conversion of Sagittarius.

Inputs [S] (checked this session):
  Sgr systemic (del Pino et al. 2021, arXiv:2011.02627, Table 1, with M54): RA 283.909, Dec -30.599 deg,
  D = 25.933 kpc, v_los = 142.71 km/s, pm = (-2.7049, -1.3648) mas/yr; their solar parameters
  R0 = 8.29 kpc, V0 = 239 km/s, (U,V,W)_sun = (11.10, 12.24, 7.25) km/s. Their Table 2 / Sec. V.2: r = 18.11 kpc,
  |V| = 311.1 km/s.
  Eilers et al. 2019: v_c = 229.0 - 1.7 (R - R0) km/s; R0 = 8.122 kpc (dagger).
  Bullet: subcluster mass centroid 2600 km/s (Springel & Farrar 2007) [S]; dispersions main 1163, bullet 472 km/s
  (Benavides et al. DS+, arXiv:2212.00040) [S]; 1250/210 (Barrena 2002 via secondary source).
  Segue 1 sigma = 3.7 km/s (Simon et al. 2011) [S]; classical dSphs 6.6-11.7 km/s (Walker et al. 2009 Table 1) [S].
Gate: W = exp(-u^2/2) (Gaussian) or 1/(1+u^2/2) (rational), u = |dv|/v*.
"""
import numpy as np

rng = np.random.default_rng(12345)
kms_per_masyr_kpc = 4.740470463

def radec_to_gal_matrix():
    # ICRS -> Galactic rotation matrix (standard, dagger)
    return np.array([[-0.0548755604162154, -0.8734370902348850, -0.4838350155487132],
                     [+0.4941094278755837, -0.4448296299600112, +0.7469822444972189],
                     [-0.8676661490190047, -0.1980763734312015, +0.4559837761750669]])

def sgr_galactocentric(R0=8.29, zsun=0.0, vsun=(11.10, 239+12.24, 7.25)):
    ra, dec = np.radians(283.909), np.radians(-30.599)
    D, vlos, pmra, pmdec = 25.933, 142.71, -2.7049, -1.3648
    # ICRS unit vectors
    r_hat = np.array([np.cos(dec)*np.cos(ra), np.cos(dec)*np.sin(ra), np.sin(dec)])
    e_ra = np.array([-np.sin(ra), np.cos(ra), 0.0])
    e_dec = np.array([-np.sin(dec)*np.cos(ra), -np.sin(dec)*np.sin(ra), np.cos(dec)])
    v_icrs = vlos*r_hat+kms_per_masyr_kpc*D*(pmra*e_ra+pmdec*e_dec)
    x_icrs = D*r_hat
    T = radec_to_gal_matrix()
    xg = T@x_icrs; vg = T@v_icrs        # heliocentric Galactic (x to GC, y rotation, z NGP)
    # Galactocentric: x from GC toward... use X = xg - R0 (sun at X=-R0), ignore small zsun tilt
    X = np.array([xg[0]-R0, xg[1], xg[2]+zsun])
    V = vg+np.array(vsun)
    return np.linalg.norm(X), np.linalg.norm(V), X, V

def W_gauss(u): return np.exp(-u*u/2)
def W_rat(u): return 1/(1+u*u/2)

def mc_gate(V, s, vstar, n=400000):
    """<W> for relative velocity = V zhat + Gaussian(0, s^2 I) in 3D."""
    dv = rng.normal(0, s, size=(n, 3)); dv[:, 2] += V
    u = np.linalg.norm(dv, axis=1)/vstar
    return W_gauss(u).mean(), W_rat(u).mean()

def closed_gauss(V, s, vstar):
    q = vstar**2+s**2
    return (vstar**2/q)**1.5*np.exp(-V**2/(2*q))

if __name__ == "__main__":
    r, v, X, Vv = sgr_galactocentric()
    print("Sgr (del Pino solar params): r = %.2f kpc, |V| = %.1f km/s  [paper: 18.11, 311.1]" % (r, v))
    r2, v2, _, _ = sgr_galactocentric(R0=8.122, zsun=0.0208, vsun=(12.9, 245.6, 7.78))
    print("Sgr (R0=8.122, v_sun=(12.9,245.6,7.78), dagger): r = %.2f kpc, |V| = %.1f km/s" % (r2, v2))
    vc = 229.0-1.7*(18.11-8.122)
    sig = vc/np.sqrt(2)
    print("Eilers v_c(18.11) = %.1f km/s -> isothermal sigma_1D = %.1f km/s" % (vc, sig))
    # isothermal orbit turning points: E = V^2/2 + vc^2 ln r ; L = r v_t
    vr_frac = np.dot(X, Vv)/np.linalg.norm(X)
    vt = np.sqrt(v**2-vr_frac**2)
    Lz = r*vt; En = 0.5*v**2+vc**2*np.log(r)
    import mpmath as _mp
    g = lambda rr: En-vc**2*_mp.log(rr)-Lz**2/(2*rr*rr)
    from mpmath import findroot
    peri = float(findroot(g, 14.0)); apo = float(findroot(g, 48.0))
    Vperi = Lz/peri; Vapo = Lz/apo
    print("isothermal orbit (v_r=%.1f, v_t=%.1f): peri %.1f kpc (V=%.1f), apo %.1f kpc (V=%.1f)" % (vr_frac, vt, peri, Vperi, apo, Vapo))
    s_sat = 12.0
    s = np.sqrt(sig**2+s_sat**2)
    print("\nSgr gate factor <W> (host sigma %.1f + satellite 12 km/s, dagger):" % sig)
    for vs in [120, 200, 300, 1000, 2000]:
        g_mc, r_mc = mc_gate(v, s, vs); g_cf = closed_gauss(v, s, vs)
        print("  v*=%5d: gauss MC %.4f closed %.4f | rational MC %.4f | eps<0.1/<W>: gauss %.3f rational %.3f"
              % (vs, g_mc, g_cf, r_mc, 0.1/g_cf, 0.1/r_mc))
    # time average over the isothermal orbit (radial period average of <W>(V(r)))
    rr = np.linspace(peri*1.0001, apo*0.9999, 20001)
    vr2 = 2*g(rr) if False else 2*np.array([float(g(x)) for x in rr])
    vr2 = np.maximum(vr2, 1e-12)
    dt = 1/np.sqrt(vr2)
    Vr = np.sqrt(vr2+(Lz/rr)**2)
    Wav = np.sum(closed_gauss(Vr, s, 120)*dt)/np.sum(dt)
    print("  orbit-time-averaged Gaussian <W> at v*=120: %.4f (vs %.4f at current V) -> eps < %.3f" % (Wav, closed_gauss(v, s, 120), 0.1/Wav))
    print("\nBullet cluster, V = 2600 km/s:")
    for (sm, ss, lab) in [(1250, 210, "Barrena via secondary"), (1163, 472, "DS+ 2022")]:
        S = np.sqrt(sm**2+ss**2)
        for vs in [120, 1000, 3000]:
            g_mc, r_mc = mc_gate(2600, S, vs)
            print("  %-22s v*=%5d: gauss %.3e (closed %.3e) rational %.3e" % (lab, vs, g_mc, closed_gauss(2600, S, vs), r_mc))
        gm = closed_gauss(0, np.sqrt(2)*sm, 120)
        print("  %-22s within main (pair sigma sqrt2*%d), v*=120: gauss %.3e" % (lab, sm, gm))
    g120 = closed_gauss(2600, np.sqrt(1250**2+210**2), 120)
    print("  Farrar-Rosen 0.4-1.2 x gravity -> eps = %.3e - %.3e at v*=120 (gauss)" % (0.4/g120, 1.2/g120))
    print("\nInternal gate (pairs, sigma_pair = sqrt2 sigma), v*=120 unless noted:")
    for sg in [3.7, 6.6, 10, 11.7, 30, 155, 1000]:
        g_mc, r_mc = mc_gate(0, np.sqrt(2)*sg, 120)
        print("  sigma=%6.1f: gauss MC %.4f closed %.4f rational MC %.4f" % (sg, g_mc, closed_gauss(0, np.sqrt(2)*sg, 120), r_mc))
    print("  v*=30, sigma=10: gauss %.4f" % closed_gauss(0, np.sqrt(2)*10, 30))
