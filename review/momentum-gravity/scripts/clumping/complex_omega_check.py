"""Argument-principle count of growing modes (Im w > eps) of the homogeneous gated+gravity problem
(Gaussian gate), to test that the onset is at w = 0 and that unstable modes are purely growing.
Zeros of the full (truncated) system = zeros of [prod over perpendicular pairs (n,m) of det(1 - lambda_{n+m} T_z)] x D(w)
(even-even block determinants cancel the poles of D; other blocks are decoupled pure-gate modes).
We count:  wind(D) + sum_N mult_ee(N) wind(det B_N)   [gravity-coupled sector]
           sum_N mult_other(N) wind(det B_N)          [decoupled pure-gate blocks]
on (i) the full rectangle Re w in [-X, X], (ii) the right rectangle Re w in [delta, X]."""
import sys, math, time
import numpy as np
sys.path.insert(0, '/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/clumping')
from growth_rates import Gated
from static_threshold import top_eigs

NB = 5   # blocks N = 0..NB-1 tracked explicitly

def evaluate(model, kappa, w):
    tau, ub = model.spectral(kappa, w)
    lam = (model.gt/kappa**2)*model.t0**2*model.q**model.N
    F = np.array([np.sum(ub/(1 - l*tau)) for l in lam])
    Dv = kappa**2 - np.sum(model.A*F)
    lamB = (model.gt/kappa**2)*model.t0**2*model.q**np.arange(NB)
    # log det(1 - lam T) = sum log(1 - lam tau): track as complex numbers via products of normalized factors
    dets = np.array([np.prod(1 - lb*tau) for lb in lamB])
    return Dv, dets

def winding(model, kappa, corners, h0=0.1, maxdphi=0.25):
    """total phase change /2pi of D and of each det B_N along the closed polygon"""
    pts = list(corners) + [corners[0]]
    totD = 0.0
    totB = np.zeros(NB)
    D0, B0 = evaluate(model, kappa, pts[0])
    nev = 1
    for a, b in zip(pts[:-1], pts[1:]):
        Lseg = abs(b - a)
        s = 0.0
        while s < Lseg - 1e-14:
            h = min(h0, Lseg - s)
            while True:
                w = a + (b - a)*(s + h)/Lseg
                D1, B1 = evaluate(model, kappa, w); nev += 1
                dD = np.angle(D1/D0)
                dB = np.angle(B1/B0)
                if max(abs(dD), np.max(np.abs(dB))) < maxdphi or h < 1e-7:
                    break
                h /= 2
            totD += dD; totB += dB
            D0, B0 = D1, B1
            s += h
    return totD/(2*np.pi), totB/(2*np.pi), nev

def mult(N):
    ee = sum(1 for n in range(0, N + 1) if n % 2 == 0 and (N - n) % 2 == 0)
    return ee, (N + 1) - ee

if __name__ == '__main__':
    cases = [(1.2917, 10.0, 2.4), (1.2917, 10.0, 2.2), (1.2917, 100.0, 2.0), (4.0, 1000.0, 10.5)]
    eps, Y, delta = 0.004, 5.0, 0.01
    for r, gt, k2 in cases:
        t1 = time.time()
        model = Gated(r, gt)
        kappa = math.sqrt(k2)
        L0 = top_eigs(r, gt, 0, nev=1)[0][0]
        X = 4*kappa + 4
        full = [complex(-X, eps), complex(X, eps), complex(X, Y), complex(-X, Y)]
        right = [complex(delta, eps), complex(X, eps), complex(X, Y), complex(delta, Y)]
        wDf, wBf, n1 = winding(model, kappa, full)
        wDr, wBr, n2 = winding(model, kappa, right)
        coupled_f = wDf + sum(mult(N)[0]*wBf[N] for N in range(NB))
        other_f = sum(mult(N)[1]*wBf[N] for N in range(NB))
        coupled_r = wDr + sum(mult(N)[0]*wBr[N] for N in range(NB))
        other_r = sum(mult(N)[1]*wBr[N] for N in range(NB))
        print(f"r={r}, gt={gt}, kappa^2={k2} (static Lambda_0={L0:.5f}):")
        print(f"   full rect : wind(D)={wDf:+.4f}, wind(det B_N, N=0..{NB-1})={np.round(wBf,4)} -> coupled zeros={coupled_f:+.4f}, decoupled zeros={other_f:+.4f}  [{n1} evals]")
        print(f"   right rect: wind(D)={wDr:+.4f}, wind(det B_N)={np.round(wBr,4)} -> coupled zeros={coupled_r:+.4f}, decoupled zeros={other_r:+.4f}  [{n2} evals]  ({time.time()-t1:.0f}s)")
        sys.stdout.flush()
