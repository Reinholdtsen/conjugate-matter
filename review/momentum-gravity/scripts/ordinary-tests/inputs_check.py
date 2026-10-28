"""Print the derived test inputs used in bounds.py (iron rule: every quoted number printed)."""
import io, contextlib
import numpy as np
with contextlib.redirect_stdout(io.StringIO()):
    import bounds as B
d_r = (B.GM_E_LLR - B.GM_E_RIES) / B.GM_E_LLR; s_r = np.hypot(B.S_LLR, B.S_RIES) / B.GM_E_LLR
d_d = (B.GM_E_LLR - B.GM_E_DUNN) / B.GM_E_LLR; s_d = np.hypot(B.S_LLR, B.S_DUNN) / B.GM_E_LLR
print(f"GM_E(LLR) - GM_E(SLR Ries) = {B.GM_E_LLR-B.GM_E_RIES:+.4f} km3/s2 -> relative {d_r:+.2e} +- {s_r:.2e}")
print(f"GM_E(LLR) - GM_E(SLR Dunn) = {B.GM_E_LLR-B.GM_E_DUNN:+.4f} km3/s2 -> relative {d_d:+.2e} +- {s_d:.2e}")
lo, hi = -(B.GAMMA + 2*B.SGAMMA)/2, -(B.GAMMA - 2*B.SGAMMA)/2
print(f"Cassini: eps*K(u_earth) in [{lo:.3e}, {hi:.3e}] (2 sigma), from gamma_eff - 1 = -2 eps K")
print(f"Double pulsar: |d omegadot/omegadot| < {B.PBDOT_TEST_95/2.5:.2e} (from Pb-dot test 1.3e-4 at 95%, factor 2.5)")
print(f"Eros: M_fly/M_orb - 1 = {B.M_EROS_FLY/B.M_EROS_ORB-1:+.3f} +- {B.S_EROS_FLY/B.M_EROS_ORB:.3f}")
for v in [0.3, 1.0, 1.02, 3.0]:
    print(f"v*={v:5.2f}: K_gauss(Moon)={B.K_of(B.v_moon/v,'gauss'):.4f} K_gauss(LAGEOS)={B.K_of(B.v_lageos/v,'gauss'):.2e}"
          f" | K_lor(Moon)={B.K_of(B.v_moon/v,'lorentz'):.4f} K_lor(LAGEOS)={B.K_of(B.v_lageos/v,'lorentz'):.4f}")
# Mercury beta cross-check in the u<<1 regime: |eps| < (3/2)(v*/c)^2 * 2 sigma[(2+2g-b)/3], sigma from beta-1 = (-4.1 +- 7.8)e-5
c = 299792.458
for v in [1000.0, 3000.0]:
    print(f"u<<1 cross-check via Will 2014 Mercury beta: v*={v}: |eps| < {(1.5*(v/c)**2)*(4.1e-5+2*7.8e-5)/3:.2e}")
# planet-planet coupling: rough size of Jupiter-induced Mars precession needed? (not computed; neglected)
