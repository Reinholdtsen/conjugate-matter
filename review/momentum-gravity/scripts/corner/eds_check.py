"""Implementation check of the two linear systems in linear_corner.py: Einstein-de Sitter background
(Om = Om_c = 1, dlnH/dN = -3/2), uniform limit (R = Rv = Ra = 1, J_W = 0), single fluid.  The
asymptotic logarithmic growth rate d ln(dc)/dN from direct RK4 integration of the same right-hand
side is compared with the analytic exponents: K4: p^2 + (1/2 - eps/2) p = (3/2)(1+eps) (dark-tests
growth.py); H: p^2 + p/2 = (3/2)(1+eps)(1+eps/2) (critic c4b, sympy)."""
import numpy as np
for reading in ("K4", "H"):
    for e in (1.0, 3.0, 10.0):
        A = 0.5 * e; b = 0.5 * e if reading == "H" else 0.0
        def rhs(Y):
            dc, th = Y
            return np.array([-(1 + b) * th, -(2 - 1.5 + b - A) * th - 1.5 * (1 + e) * dc])
        Y = np.array([1.0, -1.0]); h = 1e-3; lnd = []
        for i in range(20000):
            k1 = rhs(Y); k2 = rhs(Y + h/2*k1); k3 = rhs(Y + h/2*k2); k4 = rhs(Y + h*k3)
            Y = Y + h/6*(k1 + 2*k2 + 2*k3 + k4)
            nrm = np.abs(Y).max(); Y /= nrm; lnd.append(np.log(nrm))
        rate = np.mean(lnd[-1000:]) / h
        if reading == "K4":
            bb = 0.5 - e/2; p = (-bb + np.sqrt(bb**2 + 6*(1+e))) / 2
        else:
            p = (-0.5 + np.sqrt(0.25 + 6*(1+e)*(1+e/2))) / 2
        print(f"{reading:2s} eps = {e:4.1f}: numerical growth exponent = {rate:.5f}, analytic = {p:.5f}")
