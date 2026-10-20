"""Referee's own Monte Carlo of E = -J sum cos(phi_i - phi_j) - h sum cos(2 phi_i) on an LxL periodic lattice.
Checkerboard Metropolis, numpy-vectorised. Own seeds (not the manuscript's)."""
import numpy as np, sys, time

def run(L, T, J, h, n_therm, n_meas, seed, start='hot', step=None):
    rng = np.random.default_rng(seed)
    phi = rng.uniform(0, 2*np.pi, (L, L)) if start == 'hot' else np.zeros((L, L))
    ii, jj = np.indices((L, L))
    masks = [((ii + jj) % 2 == c) for c in (0, 1)]
    if step is None:
        step = min(np.pi, 1.5*np.sqrt(T))
    beta = 1.0/T
    def sweep():
        acc = 0
        for msk in masks:
            nb = [np.roll(phi, 1, 0), np.roll(phi, -1, 0), np.roll(phi, 1, 1), np.roll(phi, -1, 1)]
            new = phi + rng.uniform(-step, step, phi.shape)
            dE = np.zeros_like(phi)
            for n in nb:
                dE += -J*(np.cos(new - n) - np.cos(phi - n))
            dE += -h*(np.cos(2*new) - np.cos(2*phi))
            accept = msk & (rng.random(phi.shape) < np.exp(-beta*np.clip(dE, -50, 50)))
            phi[accept] = new[accept]
            acc += accept.sum()
        return acc/(L*L)
    for _ in range(n_therm):
        sweep()
    ms, Ms = [], []
    accs = []
    for _ in range(n_meas):
        accs.append(sweep())
        ms.append(np.mean(np.cos(phi)))
        Ms.append(np.abs(np.mean(np.exp(1j*phi))))
    ms, Ms = np.array(ms), np.array(Ms)
    am = np.mean(np.abs(ms))
    U = 1 - np.mean(ms**4)/(3*np.mean(ms**2)**2)
    # crude binning error
    def berr(x, nb=20):
        b = np.array_split(x, nb); bm = np.array([np.mean(v) for v in b]); return np.std(bm)/np.sqrt(nb)
    return dict(am=am, am_err=berr(np.abs(ms)), U=U, M=np.mean(Ms), M_err=berr(Ms), acc=np.mean(accs))

if __name__ == '__main__':
    t0 = time.time()
    print("Run A: J=h=1, T=0.6 (with cos 2phi potential), hot and cold starts")
    for L in (16, 32, 64):
        for start in ('hot', 'cold'):
            r = run(L, 0.6, 1.0, 1.0, 6000, 20000, seed=1000+L+(start == 'cold'), start=start)
            print(f"  L={L:3d} {start:4s}: <|m|>={r['am']:.4f}+-{r['am_err']:.4f}  Binder U={r['U']:.4f}  acc={r['acc']:.2f}")
        sys.stdout.flush()
    print("Run B: control T=3.0, J=h=1")
    for L in (16, 32, 64):
        r = run(L, 3.0, 1.0, 1.0, 4000, 20000, seed=2000+L)
        print(f"  L={L:3d}: <|m|>={r['am']:.4f}+-{r['am_err']:.4f}   sqrt-scaling check <|m|>*L = {r['am']*L:.3f}")
        sys.stdout.flush()
    print("Run C: exactly symmetric h=0, T=0.6")
    Mv = {}
    for L in (16, 32, 64):
        r = run(L, 0.6, 1.0, 0.0, 10000, 40000, seed=3000+L, start='cold')
        Mv[L] = r['M']
        print(f"  L={L:3d}: <|M|>={r['M']:.4f}+-{r['M_err']:.4f}  acc={r['acc']:.2f}")
        sys.stdout.flush()
    ratio = Mv[64]/Mv[16]
    sw = (64/16)**(-0.6/(4*np.pi*1.0))
    slope = np.polyfit(np.log([16, 32, 64]), np.log([Mv[16], Mv[32], Mv[64]]), 1)[0]
    print(f"  ratio M(64)/M(16) = {ratio:.4f};  spin-wave (64/16)^(-T/4piJ) = {sw:.4f};  fitted exponent {slope:.4f} vs -T/(4 pi J) = {-0.6/(4*np.pi):.4f}")
    print(f"  manuscript's quoted ratio 0.776/0.838 = {0.776/0.838:.4f}")
    print(f"elapsed {time.time()-t0:.0f}s")
