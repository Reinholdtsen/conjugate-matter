import runpy, numpy as np
ns = runpy.run_path("step2c_psi.py", run_name="lib")
psi, Oc = ns['psi'], ns['Oc']
from scipy.optimize import brentq
for xi0 in [1.0, 0.76, 0.5]:
    f = lambda lm, frac: np.log(psi(np.exp(lm), xi0)/Oc/frac)
    m10 = np.exp(brentq(f, np.log(5), np.log(300), args=(0.1,), xtol=1e-3))
    m100 = np.exp(brentq(f, np.log(20), np.log(1000), args=(1.0,), xtol=1e-3))
    print(f"xi0={xi0}: psi = 10% of DM at m = {m10:.1f} GeV ; psi = 100% of DM at m = {m100:.1f} GeV")
