# Scratch checks for the cosmo-sfd wiki batch (not part of verify/).
import sympy as sp
a, w, N, M, Mt, adot = sp.symbols('a wt N M_P Mtilde adot', positive=True)
t = sp.symbols('t')
# 1. Dictionary: E = rho~ a~^3 with rho~ ∝ a~^{-3(1+w~)}, a~ = 1/a; rho_eff = E/a^3
at = 1/a
rho_t = at**(-3*(1+w))
E = sp.simplify(rho_t*at**3)
rho_eff = sp.simplify(E/a**3)
weff = sp.symbols('weff')
sol = sp.solve(sp.Eq(sp.expand_log(sp.log(rho_eff),force=True)/sp.log(a), -3*(1+weff)), weff)
print("E =", E, "; rho_eff =", rho_eff, "; w_eff =", sol)
# 1b. Heuristic: identify densities, rho_eff = rho~
sol2 = sp.solve(sp.Eq(sp.expand_log(sp.log(rho_t),force=True)/sp.log(a), -3*(1+weff)), weff)
print("heuristic (rho_eff = rho~): w_eff =", sol2, "; at w~=0:", [s.subs(w,0) for s in sol2])
# 1c. table exponents of rho_eff
for wt in [1, -1, sp.Rational(-1,3), 0]:
    print("w~ =", wt, " rho_eff ∝", rho_eff.subs(w, wt), " w_eff =", sol[0].subs(w, wt))
# 2. Minisuperspace: a~ adot~^2 with a~ = 1/a
A = sp.Function('A')(t)
expr = (1/A)*sp.diff(1/A, t)**2
print("a~ * (da~/dt)^2 =", sp.simplify(expr))
# L = -3 M^2 a adot^2/N - 3 Mt^2 a~ a~dot^2/N - N rho a^3 ; vary N, set N=1
rho = sp.symbols('rho', positive=True)
L = -3*M**2*a*adot**2/N - 3*Mt**2*adot**2/(a**5*N) - N*rho*a**3
c = sp.simplify(sp.diff(L, N).subs(N, 1))
H = adot/a
print("dL/dN at N=1:", c, "; equals 3H^2(M^2+Mt^2 a^-6) - rho times a^3 ?",
      sp.simplify(c - a**3*(3*H**2*(M**2+Mt**2*a**-6) - rho)) == 0)
# 3. |Z| = 1 vs a·a~ = 1 at d = 1, X = 0
Y = sp.symbols('Y', positive=True)
HZ = sp.diag(Y, 1/Y)   # H_Z at X = 0
print("H_Z(X=0) =", HZ, "; det =", HZ.det(), "; |Z| =", sp.Abs(sp.I*Y))
aa = sp.sqrt(HZ[0,0]); at2 = sp.sqrt(HZ[1,1])
print("with g = a^2 = Y and momentum block = a~^2 = 1/Y: a*a~ =", sp.simplify(aa*at2), "for every Y > 0; |Z| = 1 only at Y = 1")
