"""Sun-Earth vs Sun-Moon channel in LLR (order-of-magnitude, scaled from the EIH velocity-cross term).
Sun-Moon relative velocity = v_E + v_ME; expanding eps*W(|v_E + v_ME|/v*) to first order in v_ME gives
  eps * W'(u_E)/(v_E v*) * (v_E . v_ME) * G M_sun m_M / r,
the same structure as the EIH cross term (3/c^2)(v_E . v_ME) G M_sun m_M / r (barycentric frame).
Murphy, Nordtvedt & Turyshev (2007) state LLR fits the gravitomagnetic contributions at a part in a thousand (disputed by Kopeikin).
If that applies, |eps W'(u_E)| c^2 / (3 v_E v*) < 1e-3."""
import numpy as np
c2 = 299792.458**2
vE = 29.784
for shape in ['gauss', 'lorentz']:
    for vs in [3.0, 10.0, 30.0, 120.0, 1000.0]:
        u = vE / vs
        W1 = -2*u*np.exp(-u*u) if shape == 'gauss' else -2*u/(1+u*u)**2
        coef = abs(W1) * c2 / (3 * vE * vs)
        print(f"{shape:7s} v*={vs:7.1f}: our/EIH cross-term coefficient = {coef:.2e} eps -> |eps| < {1e-3/coef:.1e} (if 0.1% holds)")
