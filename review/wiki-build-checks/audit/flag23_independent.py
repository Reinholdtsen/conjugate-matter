"""
Independent audit of flag 23 (review/wiki-build-flags.md):
  Is the cosmological constraint a*a~ = 1 "the |Z| = 1 locus" (#11 sec. 6, 10; #5 sec. C;
  #1 v0.3; HANDOFF sec. 2; also #9 sec. 4, 8 and #11 App. A item 6)?

Definitions taken from the sources (not from the flag's check script):
  #5 sec. C / #11 sec. 6 : Z = X + iY (symmetric, Y > 0),
                           H_Z = [[Y + X Y^-1 X, X Y^-1], [Y^-1 X, Y^-1]],  Im Z = Y = g.
  #5 sec. A cor. 3       : momentum metric slaved, g~ = g^-1 (on X = 0).
  #1 sec. 6              : a = x-space scale factor, a~ = p-space scale factor,
                           (a a~)^3 * cell = hbar^3  =>  a a~ = 1.
  #5 sec. C              : rho acts as Z -> -Z^-1 (Mobius action of [[0,1],[-1,0]]).
Independent anchors (textbook, not the paper):
  (A1) Siegel action of Sp(2d,R): M.Z = (A Z + B)(C Z + D)^-1.
  (A2) symplectic matrices have det = 1.
  (A3) in the upper half-plane z -> -1/z = (reflection Re z -> -Re z) o (inversion z -> 1/conj z);
       the inversion's fixed set is |z| = 1.
  (A4) FRW: physical momenta redshift as 1/a (Liouville), so the comoving phase-space cell
       a^3 * a^-3 is constant along the whole history.
"""
import numpy as np
import sympy as sp

rng = np.random.default_rng(12345)
line = "-" * 78


def HZ_num(Z):
    X, Y = Z.real, Z.imag
    Yi = np.linalg.inv(Y)
    return np.block([[Y + X @ Yi @ X, X @ Yi], [Yi @ X, Yi]])


def siegel(M, Z, d):
    A, B, C, D = M[:d, :d], M[:d, d:], M[d:, :d], M[d:, d:]
    return (A @ Z + B) @ np.linalg.inv(C @ Z + D)


def rand_sym(d, s=1.0):
    m = rng.normal(size=(d, d)) * s
    return (m + m.T) / 2


def rand_pos(d):
    a = rng.normal(size=(d, d))
    return a @ a.T + d * np.eye(d)


def rand_sp(d):
    """random Sp(2d,R) element as a product of generators"""
    Id, Zr = np.eye(d), np.zeros((d, d))
    R = np.block([[Zr, Id], [-Id, Zr]])
    M = np.eye(2 * d)
    for _ in range(3):
        B = rand_sym(d, 0.5)
        A = np.eye(d) + 0.3 * rng.normal(size=(d, d))
        M = M @ np.block([[Id, B], [Zr, Id]]) @ np.block([[A, Zr], [Zr, np.linalg.inv(A).T]]) @ R
    return M


print(line)
print("PART 0. Consistency of the sources' parametrization with the textbook Siegel action (A1, A2)")
for d in (1, 2, 3):
    Id, Zr = np.eye(d), np.zeros((d, d))
    om = np.block([[Zr, Id], [-Id, Zr]])
    worst_cov = worst_sp = worst_det = 0.0
    for _ in range(20):
        Z = rand_sym(d) + 1j * rand_pos(d)
        M = rand_sp(d)
        worst_sp = max(worst_sp, np.abs(M.T @ om @ M - om).max())
        H = HZ_num(Z)
        worst_det = max(worst_det, abs(np.linalg.det(H) - 1))
        rhs = M @ H @ M.T
        worst_cov = max(worst_cov, np.abs(HZ_num(siegel(M, Z, d)) - rhs).max() / np.abs(rhs).max())
    R = np.block([[Zr, Id], [-Id, Zr]])
    Z = rand_sym(d) + 1j * rand_pos(d)
    rhoZ = siegel(R, Z, d)
    print(f" d={d}: max|M^T w M - w| = {worst_sp:.1e};  max|det H_Z - 1| = {worst_det:.1e};"
          f"  max rel|H_(M.Z) - M H_Z M^T| = {worst_cov:.1e};  R.Z == -Z^-1: {np.allclose(rhoZ, -np.linalg.inv(Z))}")
print(" => H_Z is covariant (H_(M.Z) = M H_Z M^T), det H_Z = 1 everywhere, rho = R acts as Z -> -Z^-1.")

print(line)
print("PART 1. d = 1, symbolic. Z = X + iY.")
X, Y = sp.symbols("X Y", real=True)
Yp = sp.symbols("Y", positive=True)
H = sp.Matrix([[Y + X**2 / Y, X / Y], [X / Y, 1 / Y]])
print(" det H_Z =", sp.simplify(H.det()))
Z = X + sp.I * Y
rho = sp.simplify(-1 / Z)
rho_re, rho_im = sp.simplify(sp.re(rho)), sp.simplify(sp.im(rho))
print(" rho(Z) = -1/Z :  Re =", rho_re, ",  Im =", rho_im)
absZ2 = X**2 + Y**2
print(" |rho(Z)|^2 * |Z|^2 =", sp.simplify((rho_re**2 + rho_im**2) * absZ2))
H0 = H.subs(X, 0)
print(" on the axis X = 0: H_Z =", H0.tolist(), "; rho(iY) = i *", sp.simplify(rho_im.subs(X, 0)),
      " (scale-factor duality g -> 1/g)")

print("\n 1a. The constraint on the vacuum slice X = 0 (source definitions: a^2 = g = Y, a~^2 = g~ = H_pp = 1/Y)")
a = sp.sqrt(Yp)
at = sp.sqrt(1 / Yp)
print("     a*a~ =", sp.simplify(a * at), " for every Y > 0;  det H at X=0 =", sp.simplify(H0.det()))
for yv in (sp.Rational(1, 1000), sp.Rational(1, 4), 1, 4, 1000):
    Hy = H0.subs(Y, yv)
    a_v, at_v = sp.sqrt(Hy[0, 0]), sp.sqrt(Hy[1, 1])       # read off the x- and p-blocks of H
    print(f"       Y = {str(yv):>6}:  a = {float(a_v):9.4f}   a~ = {float(at_v):9.4f}"
          f"   a*a~ = {float(a_v*at_v):.12f}   |Z| = {float(sp.Abs(sp.I*yv)):9.4f}")
sol = sp.solve(sp.Eq(Yp**2, 1), Yp)       # X = 0 substituted into X^2 + Y^2 = 1, with Y > 0
print("     solutions of {X = 0, |Z| = 1, Y > 0}: Y =", sol, " -> the circle meets the axis only at Z = i")

print("\n 1b. Every reading of (a, a~) off the axis that the sources' objects allow")
readings = {
    "(i)   a^2 = Im Z,     a~^2 = H_pp        ": (Y, 1 / Y),
    "(ii)  a^2 = H_xx,     a~^2 = H_pp        ": (Y + X**2 / Y, 1 / Y),
    "(iii) a^2 = Im Z,     a~^2 = Im rho(Z)   ": (Y, rho_im),
    "(iv)  a^2 = |Z|,      a~^2 = |rho(Z)|    ": (sp.sqrt(absZ2), 1 / sp.sqrt(absZ2)),
}
for name, (a2, at2) in readings.items():
    prod2 = sp.simplify(a2 * at2)
    s = sp.solve(sp.Eq(prod2, 1), X) if prod2.has(X) else "identically 1 (all Z)"
    print(f"     {name}: (a a~)^2 = {prod2!s:<22}  a a~ = 1  <=>  X in {s}")
print("     (det reading: (a a~)^2 = det H = 1 on the whole domain, by A2)")
print("     => in no reading is {a a~ = 1} the circle |Z| = 1; it is either the axis X = 0 or the whole domain.")

print("\n 1c. What |Z| = 1 is, in the sources' objects")
print("     H_xx - H_pp              =", sp.factor(sp.simplify(H[0, 0] - H[1, 1])), "  (zero iff |Z| = 1: a = a~ in reading (ii))")
print("     Im rho(Z) - Im Z         =", sp.factor(sp.simplify(rho_im - Y)), "  (zero iff |Z| = 1: a = a~ in reading (iii))")
print("     rho(Z) - (-conj Z)       =", sp.factor(sp.simplify(rho - (-(X - sp.I * Y))))," (zero iff |Z| = 1: there rho acts as X -> -X)")
inv = 1 / (X - sp.I * Y)                      # inversion in the unit circle, z -> 1/conj(z)
refl_inv = -sp.conjugate(inv)                 # then reflection Re -> -Re
print("     (reflection o inversion)(Z) - rho(Z) =", sp.simplify(refl_inv - rho), "  (anchor A3)")
print("     inversion fixed set: 1/conj(Z) - Z =", sp.factor(sp.simplify(inv - Z)), " -> zero iff |Z| = 1")
print("     => |Z| = 1 is the mirror of the inversion that rho performs on the axis (a <-> 1/a):")
print("        the self-dual locus a = a~, separating |Z| > 1 (a > a~) from |Z| < 1 (a < a~).")

print(line)
print("PART 2. The one reading in which |Z| = 1 is a family with a a~ = 1: a 45-degree-rotated polarization")
th = sp.symbols("theta", positive=True)
Hc = sp.simplify(H.subs({X: sp.cos(th), Y: sp.sin(th)}))
ev = [sp.simplify(e) for e in Hc.eigenvals().keys()]
print(" on Z = e^{i theta}: H =", Hc.tolist())
print(" eigenvalues:", ev, "; product =", sp.simplify(ev[0] * ev[1]))
lam = sp.symbols("lambda")
cp = Hc.charpoly(lam).as_expr()
print(" charpoly(cot(theta/2)) =", sp.simplify(sp.expand_trig(cp.subs(lam, sp.cot(th / 2)).rewrite(sp.tan))),
      "; charpoly(tan(theta/2)) =", sp.simplify(sp.expand_trig(cp.subs(lam, sp.tan(th / 2)).rewrite(sp.tan))),
      " -> eigenvalues are cot(theta/2), tan(theta/2)")
evecs = Hc.eigenvects()
print(" eigenvectors:", [sp.simplify(v[2][0].T / v[2][0][0]).tolist() for v in evecs], " (directions x+p and x-p)")
phi = sp.pi / 4
Mrot = sp.Matrix([[sp.cos(phi), sp.sin(phi)], [-sp.sin(phi), sp.cos(phi)]])
w = sp.simplify((Mrot[0, 0] * sp.I * Yp + Mrot[0, 1]) / (Mrot[1, 0] * sp.I * Yp + Mrot[1, 1]))
print(" the U(1) rotation by pi/4 (stabilizer of i) maps iY to w with |w|^2 =", sp.simplify(sp.Abs(w)**2))
print(" => |Z| = 1 is the image of the vacuum slice X = 0 under a 45-degree rotation of the (x, p) split.")
print("    There Im Z = sin(theta) <= 1 and X = cos(theta) != 0 (except at Z = i), so this reading")
print("    contradicts the sources' 'Im Z = g' and 'X = 0 is the vacuum slice'.")
for tv in (0.3, 1.0, np.pi / 2, 2.5):
    print(f"    theta = {tv:5.3f}: Im Z = {np.sin(tv):.4f}, X = {np.cos(tv):+.4f}, "
          f"eigenvalues = {1/np.tan(tv/2):.4f}, {np.tan(tv/2):.4f}")

print(line)
print("PART 3. d = 3 (isotropic FRW spatial block) and anisotropic Y, on the axis X = 0")
for av in (1e-3, 0.5, 1.0, 2.0, 1e3):
    Yv = av**2 * np.eye(3)
    Zv = 1j * Yv
    Hv = HZ_num(Zv)
    at_v = np.sqrt(np.linalg.eigvalsh(Hv[3:, 3:]))[0]
    zz = np.abs(Zv @ Zv.conj() - np.eye(3)).max()
    print(f" a = {av:8.3g}: a~ = {at_v:9.4g}, a*a~ = {av*at_v:.12f}, (a a~)^6 = det H = {np.linalg.det(Hv):.6f};"
          f"  |Z Zbar - 1| = {zz:9.3g}, ||Z||op = {np.linalg.norm(Zv, 2):9.4g}, |det Z| = {abs(np.linalg.det(Zv)):9.3g}")
Yv = np.diag([4.0, 0.25, 1.0])
Hv = HZ_num(1j * Yv)
print(" anisotropic Y = diag(4, 1/4, 1): per-direction a_k a~_k =",
      np.round(np.sqrt(np.diag(Hv)[:3] * np.diag(Hv)[3:]), 12),
      "; |Z Zbar - 1| =", np.abs(Yv @ Yv - np.eye(3)).max())
print(" => on the vacuum slice the constraint holds for every scale factor; any matrix reading of")
print("    '|Z| = 1' (Z Zbar = 1, operator norm 1, |det Z| = 1) holds only at a = 1 in the isotropic case.")

print("\n Anchor A4 (FRW, textbook): p_phys = p_comoving / a, so cell volume a^3 * (1/a)^3 =",
      sp.simplify(sp.Symbol('a', positive=True)**3 * (1 / sp.Symbol('a', positive=True))**3),
      "at every a: the constraint is satisfied along the whole history, not at one point.")

print(line)
print("PART 4. Matrix |Z| = 1 (Z Zbar = 1) <=> [X, Y] = 0 and X^2 + Y^2 = 1  (d = 2, numeric)")
Q, _ = np.linalg.qr(rng.normal(size=(2, 2)))
ths = np.array([0.7, 2.1])
Xc, Yc = Q @ np.diag(np.cos(ths)) @ Q.T, Q @ np.diag(np.sin(ths)) @ Q.T
Zc = Xc + 1j * Yc
Hc2 = HZ_num(Zc)
print(" commuting X, Y with X^2+Y^2 = 1: |Z Zbar - 1| =", f"{np.abs(Zc @ Zc.conj() - np.eye(2)).max():.1e}",
      "; |rho(Z) + Zbar| =", f"{np.abs(-np.linalg.inv(Zc) + Zc.conj()).max():.1e}",
      "; |H_xx - H_pp| =", f"{np.abs(Hc2[:2, :2] - Hc2[2:, 2:]).max():.1e}",
      "; X != 0:", not np.allclose(Xc, 0))
Xn, Yn = rand_sym(2), rand_pos(2)
print(" generic X, Y: |[X,Y]| =", f"{np.abs(Xn @ Yn - Yn @ Xn).max():.3f}", "; Im(Z Zbar) = YX - XY =",
      np.allclose(((Xn + 1j * Yn) @ (Xn - 1j * Yn)).imag, Yn @ Xn - Xn @ Yn))

print(line)
print("PART 5. The dictionary (side claim of the flag): w_eff from a dual-frame fluid, a~ = 1/a")
av_, w = sp.symbols("a w_tilde", positive=True)
at_ = 1 / av_
rho_t = at_**(-3 * (1 + w))                       # dual-frame density, comoving in the dual frame
E = rho_t * at_**3                                # energy in a dual comoving volume (with the Jacobian)
rho_eff = E / av_**3                              # entering our Hamiltonian constraint
n = sp.simplify(sp.log(rho_eff).expand(force=True) / sp.log(av_))
print(" with Jacobian:    rho_eff ~ a^(", sp.simplify(n), ")  =>  w_eff =", sp.simplify(-n / 3 - 1))
n2 = sp.simplify(sp.log(rho_t).expand(force=True) / sp.log(av_))
print(" densities equated (no Jacobian): rho_eff ~ a^(", sp.simplify(n2), ")  =>  w_eff =", sp.simplify(-n2 / 3 - 1))
print(line)
