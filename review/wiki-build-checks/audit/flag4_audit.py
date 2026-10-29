"""Independent audit of flag 4: #7 (notes/tuning-test.md) §2 item 2,
"With Y = 1 + h, X = x: S = 2h + x² + O(3), A = [h, x] + O(3)",
where S = Y + X Y^-1 X - Y^-1 and A = [X, Y^-1] (#7 §2, battery T3).

Steelman question: is there a parametrization / order-counting under which the
source line is exactly right?  Bookkeeping parameter e: h -> e h, x -> e x.
"""
import sympy as sp
import numpy as np

e = sp.symbols('e')

# ---------- Part 1: d = 1 (commuting), exact series --------------------------
h, x, c = sp.symbols('h x c')
print("Part 1: d = 1, Y = 1 + h (linear, as #7 writes it)")
Y = 1 + e*h
X = e*x
S = Y + X*X/Y - 1/Y
ser = sp.expand(sp.series(S, e, 0, 4).removeO())
for k in range(1, 4):
    print(f"  order e^{k}: {sp.factor(ser.coeff(e, k))}")

print("Part 1b: d = 1, family Y = 1 + h + c h^2 (second-order field redefinition)")
Yc = 1 + e*h + c*(e*h)**2
Sc = Yc + X*X/Yc - 1/Yc
serc = sp.expand(sp.series(Sc, e, 0, 3).removeO())
coef_h2 = sp.factor(serc.coeff(e, 2).coeff(h, 2))
print(f"  order e^2 of S: {sp.expand(serc.coeff(e, 2))}")
print(f"  coefficient of h^2 at order e^2: {coef_h2}; zero iff c = {sp.solve(coef_h2, c)}")
print("Part 1c: d = 1, exponential parametrization Y = exp(h)")
Ye = sp.exp(e*h)
Se = Ye + X*X/Ye - 1/Ye
sere = sp.expand(sp.series(Se, e, 0, 4).removeO())
for k in range(1, 4):
    print(f"  order e^{k}: {sp.factor(sere.coeff(e, k))}")

# ---------- Part 2: non-commuting symmetric 2x2 matrices, exact series -------
print("Part 2: d = 2, generic symmetric h, x (non-commuting), Y = 1 + h")
h11, h12, h22, x11, x12, x22 = sp.symbols('h11 h12 h22 x11 x12 x22')
hm = sp.Matrix([[h11, h12], [h12, h22]])
xm = sp.Matrix([[x11, x12], [x12, x22]])
I2 = sp.eye(2)
Ym = I2 + e*hm
Xm = e*xm
Yinv = Ym.inv()
Sm = Ym + Xm*Yinv*Xm - Yinv
Am = Xm*Yinv - Yinv*Xm
def taylor(M, order):
    return M.applyfunc(lambda f: sp.expand(sp.series(f, e, 0, order).removeO()))
S2 = taylor(Sm, 3)
A3 = taylor(Am, 3)
claim_S = sp.expand(2*e*hm + e**2*xm*xm)                  # the source's S through e^2
flag_S = sp.expand(2*e*hm + e**2*(xm*xm - hm*hm))          # the flag's correction
claim_A = sp.expand(e**2*(hm*xm - xm*hm))
print("  S - (2h + x^2) through e^2 == -e^2 h^2 ?",
      sp.simplify((S2 - claim_S) - (-(e**2)*hm*hm)) == sp.zeros(2, 2))
print("  S - (2h + x^2 - h^2) through e^2 == 0 ?",
      sp.simplify(S2 - flag_S) == sp.zeros(2, 2))
print("  A - [h, x] through e^2 == 0 ?  (source's A expansion)",
      sp.simplify(A3 - claim_A) == sp.zeros(2, 2))
S3 = taylor(Sm, 4)
third = sp.expand((S3 - flag_S) / e**3)
pred3 = sp.expand(hm*hm*hm - xm*hm*xm)
print("  order-e^3 remainder equals h^3 - x h x ?", sp.simplify(third - pred3) == sp.zeros(2, 2))

# ---------- Part 3: what the missing term does to Tr(S^2) --------------------
print("Part 3: Tr(S^2) by order (d = 2, exact)")
trS2 = sp.expand(sp.series(sp.expand((S3*S3).trace()), e, 0, 4).removeO())
q2 = sp.expand(trS2.coeff(e, 2))
q3 = sp.expand(trS2.coeff(e, 3))
print("  e^2 coefficient - 4Tr(h^2) =", sp.simplify(q2 - 4*(hm*hm).trace()))
print("  e^3 coefficient - [4Tr(h x^2) - 4Tr(h^3)] =",
      sp.simplify(q3 - (4*(hm*xm*xm).trace() - 4*(hm*hm*hm).trace())))

# ---------- Part 4: numerics, other d and seed than s_expansion.py ----------
print("Part 4: numerics (seed 2026, d = 3 and 6)")
rng = np.random.default_rng(2026)
for d in (3, 6):
    m = rng.standard_normal((d, d)); hn = (m + m.T) / 2
    m = rng.standard_normal((d, d)); xn = (m + m.T) / 2
    Id = np.eye(d)
    for eps in (1e-2, 1e-3, 1e-4):
        Yn = Id + eps*hn; Xn = eps*xn; Yi = np.linalg.inv(Yn)
        Sn = Yn + Xn @ Yi @ Xn - Yi
        r_src = np.linalg.norm(Sn - (2*eps*hn + eps**2*xn@xn)) / eps**2
        r_flag = np.linalg.norm(Sn - (2*eps*hn + eps**2*(xn@xn - hn@hn))) / eps**3
        print(f"  d={d} eps={eps:g}: |S-(2h+x^2)|/eps^2 = {r_src:.6f} "
              f"(|h^2| = {np.linalg.norm(hn@hn):.6f}); |S-(2h+x^2-h^2)|/eps^3 = {r_flag:.6f}")
