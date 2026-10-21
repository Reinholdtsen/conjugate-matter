# Check #7 §2 item 2: "With Y = 1 + h, X = x: S = 2h + x² + O(3), A = [h, x] + O(3)."
# S = Y + X Y^-1 X - Y^-1, A = [X, Y^-1]. Expand to second order in a bookkeeping parameter e.
import numpy as np
rng = np.random.default_rng(7)
d = 4
def sym():
    m = rng.standard_normal((d, d)); return (m + m.T) / 2
h, x = sym(), sym()
I = np.eye(d)
print("e, |S - (2eh + e^2 x^2)|/e^2, |S - (2eh + e^2 x^2 - e^2 h^2)|/e^3, |A - e^2[h,x]|/e^3")
for e in [1e-2, 1e-3]:
    Y = I + e*h; X = e*x; Yi = np.linalg.inv(Y)
    S = Y + X@Yi@X - Yi
    A = X@Yi - Yi@X
    r1 = np.linalg.norm(S - (2*e*h + e**2*x@x)) / e**2
    r2 = np.linalg.norm(S - (2*e*h + e**2*x@x - e**2*h@h)) / e**3
    r3 = np.linalg.norm(A - e**2*(h@x - x@h)) / e**3
    print(e, round(r1, 6), round(r2, 6), round(r3, 6))
print("norm of h^2 for comparison:", round(np.linalg.norm(h@h), 6))
# Tr(S^2)/e^2 at quadratic order only needs the linear term 2h:
for e in [1e-3, 1e-4]:
    Y = I + e*h; X = e*x; Yi = np.linalg.inv(Y)
    S = Y + X@Yi@X - Yi
    print("Tr(S^2)/e^2 =", np.trace(S@S)/e**2, " 4Tr(h^2) =", 4*np.trace(h@h))
