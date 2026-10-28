# Re-run of parts (A) and (C) of vot_dynamics.py with W substituted explicitly before
# differentiation (the generic-W version left a sympy dummy variable unsubstituted).
import sympy as sp
r, l, eps, vs, u, x = sp.symbols('r ell epsilon v_s u x', positive=True)
pr = sp.symbols('p_r', real=True)
shapes = [("Gaussian", lambda y: sp.exp(-y**2)), ("Lorentzian", lambda y: 1/(1 + y**2)),
          ("W = u^2", lambda y: y**2)]
print("(A) Kepler constant from the first-order Hamiltonian H = l^2/2r^2 - (1/r)(1 + eps W(l/(r v*)))")
for name, W in shapes:
    H = l**2/(2*r**2) - (1/r)*(1 + eps*W(l/(r*vs)))
    c1 = sp.symbols('c1')
    eq = sp.series(sp.diff(H, r).subs(l, sp.sqrt(r*(1 + eps*c1))), eps, 0, 2).removeO()
    c1s = sp.solve(sp.expand(eq).coeff(eps, 1), c1)[0]
    Om = sp.diff(H, l).subs(l, sp.sqrt(r*(1 + eps*c1s)))
    kep = sp.series(Om**2*r**3, eps, 0, 2).removeO()
    Kmine = sp.simplify(((kep - 1)/eps).subs(vs, 1/(sp.sqrt(r)*u)))
    Wu = W(u); Kagent = Wu - u*sp.diff(Wu, u)
    print(f"  {name}: K = {sp.factor(Kmine)} ; equals W - uW': {sp.simplify(Kmine - Kagent) == 0}")
print("(C) small-e advance from the epicyclic frequency, Delta omega = 2 pi (Omega/omega_r - 1)")
for name, W in shapes:
    Hf = (pr**2 + l**2/r**2)/2 - (1/r)*(1 + eps*W(sp.sqrt(pr**2 + l**2/r**2)/vs))
    d1 = sp.symbols('d1')
    eqr = sp.series(sp.diff(Hf, r).subs(pr, 0).subs(r, l**2*(1 + eps*d1)), eps, 0, 2).removeO()
    d1s = sp.solve(sp.expand(eqr).coeff(eps, 1), d1)[0]
    rf = l**2*(1 + eps*d1s)
    Hrr = sp.diff(Hf, r, 2).subs(pr, 0).subs(r, rf)
    Hpp = sp.diff(Hf, pr, 2).subs(pr, 0).subs(r, rf)
    Om = sp.diff(Hf, l).subs(pr, 0).subs(r, rf)
    ratio = sp.series(Om/sp.sqrt(Hrr*Hpp), eps, 0, 2).removeO()
    adv = sp.simplify((2*sp.pi*(ratio - 1)/eps).subs(vs, 1/(l*u)))
    Wu = W(u); agent = sp.pi*u*sp.diff(u*sp.diff(Wu, u), u)
    print(f"  {name}: Delta omega/eps = {sp.factor(adv)} ; equals pi u (u W')': {sp.simplify(adv - agent) == 0}")
