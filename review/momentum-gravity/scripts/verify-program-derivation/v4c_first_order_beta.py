"""Independent semi-analytic check of the v4b scan (sign and size of the gated precession at
large GM/(a v*^2)): first order in beta but all orders in p^2.
delta H = -beta exp(-p^2)/r on a Kepler orbit (K = 1), Delaunay: dw/orbit = T dPhi/dG at fixed L,
Phi = <delta H>, time average via the eccentric anomaly.  Units GM = mu = v* = 1."""
import mpmath as mp
mp.mp.dps = 30


def Phi(a, e):
    def f(E):
        r = a*(1 - e*mp.cos(E))
        p2 = 2/r - 1/a
        return -mp.exp(-p2)/r*(1 - e*mp.cos(E))
    return mp.quad(f, [0, mp.pi, 2*mp.pi])/(2*mp.pi)


def dw_first_order(a, e, beta=0.2):
    dPhi_de = mp.diff(lambda ee: Phi(a, ee), e)
    # G = sqrt(a (1 - e^2)) at fixed L = sqrt(a): de/dG = -sqrt(1-e^2)/(sqrt(a) e); T = 2 pi a^(3/2)
    return beta*2*mp.pi*a**1.5*dPhi_de*(-mp.sqrt(1 - e**2)/(mp.sqrt(a)*e))


print("first order in beta (beta = 0.2), e = 0.3: GM/(a v*^2), dw/orbit, leading-order formula -4 pi beta/(a(1-e^2))")
for x in (0.01, 0.1, 0.3, 0.5, 1.0, 2.0):
    a = 1/mp.mpf(x)
    d = dw_first_order(a, mp.mpf('0.3'))
    print(f"  {x:5.2f}  {float(d): .4e}  {float(-4*mp.pi*0.2/(a*(1 - 0.09))): .4e}")
