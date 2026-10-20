"""Diagnose the L=64 hot-start run with the cos(2phi) potential: energy and phase winding vs the cold start."""
import numpy as np, sys
sys.path.insert(0, '.')
def run(L, T, J, h, n_therm, n_meas, seed, start):
    rng = np.random.default_rng(seed)
    phi = rng.uniform(0, 2*np.pi, (L, L)) if start == 'hot' else np.zeros((L, L))
    ii, jj = np.indices((L, L)); masks = [((ii + jj) % 2 == c) for c in (0, 1)]
    step = min(np.pi, 1.5*np.sqrt(T)); beta = 1/T
    def energy():
        return (-J*(np.cos(phi - np.roll(phi, 1, 0)) + np.cos(phi - np.roll(phi, 1, 1))) - h*np.cos(2*phi)).mean()
    def winding():
        d0 = np.angle(np.exp(1j*(np.roll(phi, -1, 0) - phi))).sum(axis=0).mean()/(2*np.pi)
        d1 = np.angle(np.exp(1j*(np.roll(phi, -1, 1) - phi))).sum(axis=1).mean()/(2*np.pi)
        return d0, d1
    def sweep():
        for msk in masks:
            nb = [np.roll(phi, 1, 0), np.roll(phi, -1, 0), np.roll(phi, 1, 1), np.roll(phi, -1, 1)]
            new = phi + rng.uniform(-step, step, phi.shape)
            dE = sum(-J*(np.cos(new - n) - np.cos(phi - n)) for n in nb) - h*(np.cos(2*new) - np.cos(2*phi))
            acc = msk & (rng.random(phi.shape) < np.exp(-beta*np.clip(dE, -50, 50)))
            phi[acc] = new[acc]
    for k in range(n_therm):
        sweep()
    Es, ms = [], []
    for k in range(n_meas):
        sweep(); Es.append(energy()); ms.append(np.cos(phi).mean())
    return np.mean(Es), np.mean(np.abs(ms)), winding()
for start, seed in (('hot', 1064), ('hot', 77), ('cold', 1065)):
    E, am, w = run(64, 0.6, 1.0, 1.0, 6000, 4000, seed, start)
    print(f"L=64 {start} seed={seed}: E/site={E:.5f}  <|m|>={am:.4f}  winding (x,y)=({w[0]:+.2f},{w[1]:+.2f})"); sys.stdout.flush()
