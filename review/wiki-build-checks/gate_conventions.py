# Source-flag evidence: #1's postulated gate vs #6's overlap form, and what each implies for v*.
import sympy as sp
m, v, mu1, mu6 = sp.symbols('m_chi v_rel mu_1 mu_6', positive=True)
k = m*v/2                                  # #1 §3: k = m_chi v_rel / 2 (CM relative momentum)
dp = m*v                                   # |p1 - p2| = m_chi |v1 - v2| = m_chi v_rel = 2k (frame-independent, equal masses)
gate1 = sp.exp(-k**2/mu1**2)               # #1 §3 amplitude-level gate
gate6 = sp.exp(-dp**2/(2*mu6**2))          # #6 §4 amplitude-level gate e^{-(p1-p2)^2/2mu^2}
print("#6 gate in terms of k:", sp.simplify(gate6.subs(v, 2*sp.Symbol('k')/m)))
print("gate6/gate1 with mu6 = sqrt2*mu1:", sp.simplify((gate6/gate1).subs(mu6, sp.sqrt(2)*mu1)))
# cross-section factor = gate^2 = exp(-v^2/v*^2): solve for v* in each convention
vs = sp.Symbol('v_star', positive=True)
for name, g, mu in (("#1", gate1, mu1), ("#6", gate6, mu6)):
    expo = sp.simplify(sp.log(g**2))       # = -v^2/v*^2
    sol = sp.solve(sp.Eq(expo, -v**2/vs**2), vs)
    print(name, "v* =", sol)
