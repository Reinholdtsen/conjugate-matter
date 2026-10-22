# Flag 23 audit: is "the cosmological constraint a*a~ = 1 is the |Z| = 1 locus" true under ANY
# reading of a and a~ inside the modular field Z = X + iY?  (steelman pass; d = 1 unless stated)
# Conventions are verify/battery.py's: omega = [[0,1],[-1,0]], eta = [[0,1],[1,0]],
# H_Z = [[Y + X Y^-1 X, X Y^-1], [Y^-1 X, Y^-1]].
# Independent anchors (textbook facts, not the paper's numbers): det of a 2x2 matrix,
# the Moebius action of [[0,1],[-1,0]] on the upper half plane, inversion in the unit circle.
import sympy as sp
import numpy as np

X = sp.symbols('X', real=True)
Y = sp.symbols('Y', positive=True)
Z = X + sp.I*Y
absZ2 = X**2 + Y**2
om = sp.Matrix([[0, 1], [-1, 0]])
eta = sp.Matrix([[0, 1], [1, 0]])
H = sp.Matrix([[Y + X**2/Y, X/Y], [X/Y, 1/Y]])

def simp(e):
    return sp.simplify(sp.factor(sp.simplify(e)))

print("=== 0. Conventions (anchor checks)")
print("det H_Z =", simp(H.det()))
print("(omega^-1 H_Z)^2 + 1 =", simp((om.inv()*H)**2 + sp.eye(2)).tolist())
R = sp.Matrix([[0, 1], [-1, 0]])           # Born rotation rho
rhoZ = -1/Z
Xr, Yr = sp.simplify(sp.re(rhoZ)), sp.simplify(sp.im(rhoZ))
H_rho = sp.Matrix([[Yr + Xr**2/Yr, Xr/Yr], [Xr/Yr, 1/Yr]])
print("rho acts on H_Z as R^T H R and on Z as -1/Z:",
      simp(R.T*H*R - H_rho) == sp.zeros(2, 2))
print("Im(rho Z) =", simp(Yr), "; |rho Z|^2 =", simp(Xr**2 + Yr**2))

print("\n=== 1. The cosmological slice X = 0 (where #11 section 6 puts 'scale-factor duality g -> g^-1')")
H0 = H.subs(X, 0)
print("H_Z(X=0) =", H0.tolist(), "; det =", simp(H0.det()), "; |Z| on the slice =", sp.sqrt(absZ2.subs(X, 0)))
a0, at0 = sp.sqrt(H0[0, 0]), sp.sqrt(H0[1, 1])
print("a = sqrt(g) = sqrt(Y), a~ = sqrt(momentum block) :  a*a~ =", simp(a0*at0),
      "for every Y > 0 ; a~ == 1/a:", simp(at0 - 1/a0) == 0)
print("points of the slice with |Z| = 1:", sp.solve(sp.Eq(Y, 1), Y), "(only Z = i)")

print("\n=== 2. Every reading of (a, a~) inside Z: where does a*a~ = 1 hold, where a = a~?")
u = sp.Matrix([1, 1])/sp.sqrt(2); v = sp.Matrix([1, -1])/sp.sqrt(2)
readings = {
 "R1 flag: a^2 = Im Z, a~^2 = H_pp":                    (Y,                 H[1, 1]),
 "R2 diag blocks: a^2 = H_xx, a~^2 = H_pp":             (H[0, 0],           H[1, 1]),
 "R3 rho-image: a^2 = Im Z, a~^2 = Im(rho Z)":          (Y,                 Yr),
 "R4 modulus: a^2 = |Z|, a~^2 = |rho Z|":               (sp.sqrt(absZ2),    sp.sqrt(Xr**2 + Yr**2)),
 "R5 contrived: a^2 = H_xx, a~^2 = 1/H_pp":             (H[0, 0],           1/H[1, 1]),
 "R6 45-deg basis: a^2 = H_uu, a~^2 = H_vv (u,v = x+-p)": ((u.T*H*u)[0],    (v.T*H*v)[0]),
}
for name, (A2, At2) in readings.items():
    prod2 = simp(A2*At2)            # (a a~)^2
    ratio2 = simp(A2/At2)           # (a/a~)^2
    # test the loci: compare with |Z|^2 = 1 and with X = 0
    prod_is_one_everywhere = simp(prod2 - 1) == 0
    prod_iff_circle = simp((prod2 - 1)) != 0 and sp.simplify((prod2 - 1).subs(Y, sp.sqrt(1 - X**2))) == 0 \
        and sp.simplify((prod2 - 1).subs(X, 0).subs(Y, 2)) != 0
    prod_on_axis = simp((prod2 - 1).subs(X, 0)) == 0
    ratio_iff_circle = sp.simplify((ratio2 - 1).subs(Y, sp.sqrt(1 - X**2))) == 0
    # documents' slice requirements: Im Z = g = a^2 and a~ = 1/a along X = 0
    slice_a2_is_Y = simp(A2.subs(X, 0) - Y) == 0
    slice_dual = simp((A2*At2).subs(X, 0) - 1) == 0
    print(f"{name}\n   (a a~)^2 = {prod2} ; (a/a~)^2 = {ratio2}")
    print(f"   a a~ = 1 everywhere: {prod_is_one_everywhere} | holds on whole axis X=0: {prod_on_axis}"
          f" | a a~ = 1 on circle and fails at Z=2i: {prod_iff_circle} | a = a~ on the circle: {ratio_iff_circle}")
    print(f"   documents' slice requirements: a^2 = Im Z on X=0: {slice_a2_is_Y} ; a~ = 1/a for every Y on X=0: {slice_dual}")

# exact solution sets for the two readings that tie a product to a geometric locus
print("\nR2: (a a~)^2 - 1 =", simp(readings['R2 diag blocks: a^2 = H_xx, a~^2 = H_pp'][0]*readings['R2 diag blocks: a^2 = H_xx, a~^2 = H_pp'][1] - 1),
      "  -> zero iff X = 0")
A2, At2 = readings['R6 45-deg basis: a^2 = H_uu, a~^2 = H_vv (u,v = x+-p)']
print("R6: 4 Y^2 [(a a~)^2 - 1] =", sp.factor(sp.expand(4*Y**2*(A2*At2 - 1))),
      "  -> zero iff X^2 + Y^2 = 1")

print("\n=== 3. The circle |Z| = 1 itself (Z = e^{i th})")
th = sp.symbols('theta', positive=True)
Zc = sp.exp(sp.I*th)
print("Im(rho Z) - Im Z on the circle:", sp.simplify(sp.im(-1/Zc) - sp.im(Zc)),
      " -> rho leaves Im Z = g unchanged on the circle (no g -> g^-1 there)")
print("max of Im Z on the circle (theta in (0, pi)):", sp.maximum(sp.sin(th), th, sp.Interval.open(0, sp.pi)),
      " -> Im Z = g = a^2 cannot exceed 1 on the circle")
Hc = H.subs({X: sp.cos(th), Y: sp.sin(th)})
print("H on the circle in the (u,v) = (x+p, x-p)/sqrt2 basis:",
      sp.simplify(sp.Matrix.hstack(u, v).T*Hc*sp.Matrix.hstack(u, v)).tolist())
etap = sp.diag(1, -1)   # neutral metric whose null lines are x +- p
print("(eta'^-1 H)^2 - 1 on the circle, eta' = diag(1,-1):", sp.simplify((etap.inv()*Hc)**2 - sp.eye(2)).tolist())
print("(eta^-1 H)^2 - 1 on the circle, standard eta:", sp.simplify((eta.inv()*Hc)**2 - sp.eye(2)).tolist())
# the pi/4 phase-space rotation (in U(1), fixes Z = i) carries the imaginary axis onto the circle
Aa = sp.symbols('A', positive=True)
Rq = sp.Matrix([[sp.cos(sp.pi/4), -sp.sin(sp.pi/4)], [sp.sin(sp.pi/4), sp.cos(sp.pi/4)]])
Hrot = sp.simplify(Rq.T*sp.diag(Aa, 1/Aa)*Rq)
Yrot = sp.simplify(1/Hrot[1, 1]); Xrot = sp.simplify(Hrot[0, 1]*Yrot)
print("rotate H = diag(A, 1/A) by pi/4: Z =", Xrot, "+ i*", Yrot, "; |Z|^2 =", sp.simplify(Xrot**2 + Yrot**2))
# inversion in the unit circle vs rho
print("inversion 1/conj(Z) on the axis: 1/conj(iY) =", sp.simplify(1/sp.conjugate(sp.I*Y)),
      "; rho(iY) =", sp.simplify(-1/(sp.I*Y)), "; off-axis 1/conj(Z) - rho(Z) =", sp.simplify(1/sp.conjugate(Z) - (-1/Z)))

print("\n=== 4. Matrix case: isotropic cosmology Z = i a^2 * 1_d (d = 4)")
d = 4
for a in [0.5, 1.0, 2.0, 1e3]:
    Yd = a**2*np.eye(d); Xd = np.zeros((d, d)); Yi = np.linalg.inv(Yd)
    Hd = np.block([[Yd + Xd@Yi@Xd, Xd@Yi], [Yi@Xd, Yi]])
    Zd = Xd + 1j*Yd
    print(f"a = {a:g}: det H_Z = {np.linalg.det(Hd):.12f} ; ||Z Zbar - 1|| = {np.linalg.norm(Zd@Zd.conj() - np.eye(d)):.6g} ;"
          f" |det Z| = {abs(np.linalg.det(Zd)):.6g}")
# battery T2's own random off-vacuum point: det H_Z = 1 there, yet it is not on any unit locus
np.random.seed(0)
def randsym(s=1.0):
    m = np.random.randn(d, d)*s; return (m + m.T)/2
def posdef():
    m = np.random.randn(d, d); return m@m.T + d*np.eye(d)
_g = posdef(); _A = posdef(); _B = posdef(); _C = np.random.randn(d, d)*0.3   # replay T1's RNG draws
Xb = randsym(); Yb = posdef(); Yib = np.linalg.inv(Yb)
Hb = np.block([[Yb + Xb@Yib@Xb, Xb@Yib], [Yib@Xb, Yib]])
Zb = Xb + 1j*Yb
print(f"battery T2 point: det H_Z = {np.linalg.det(Hb):.12f} ; ||Z Zbar - 1|| = {np.linalg.norm(Zb@Zb.conj() - np.eye(d)):.4g} ;"
      f" |det Z| = {abs(np.linalg.det(Zb)):.4g}")
