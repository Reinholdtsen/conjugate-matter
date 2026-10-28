"""Full per-test table at the requested v*, and the relative-velocity range each test samples."""
import io
import contextlib
import numpy as np

with contextlib.redirect_stdout(io.StringIO()):
    import bounds as B

print("Relative speeds sampled (km/s):")
for p, (a, P, e, m) in B.planets.items():
    f = np.sqrt((1 + e) / (1 - e))
    print(f"  Sun-{p:8s}: {B.vc[p]/f:7.2f} - {B.vc[p]*f:7.2f}")
f = np.sqrt((1 + B.E_MOON) / (1 - B.E_MOON))
print(f"  Earth-Moon   : {B.v_moon/f:7.3f} - {B.v_moon*f:7.3f}")
print(f"  Earth-LAGEOS : {B.v_lageos:7.3f} (e ~ 0.004)")
f = np.sqrt((1 + B.E_DP) / (1 - B.E_DP))
print(f"  double pulsar: {B.v_dp/f:7.1f} - {B.v_dp*f:7.1f}")
print(f"  Eros         : orbit {B.v_eros_orb*1e3:.1f} m/s, flyby {B.V_EROS_FLY} km/s")
print(f"  Cassini      : photons at c against the Sun-Earth Kepler constant ({B.vc['Earth']:.2f})")

for shape in ['gauss', 'lorentz']:
    print()
    print(f"All tests, W = {'exp(-u^2)' if shape == 'gauss' else '1/(1+u^2)'}: |eps| upper bounds (2 sigma); inf/huge = no constraint")
    names = list(B.all_bounds(1.0, shape).keys())
    vlist = [0.1, 1.0, 10.0, 120.0, 1000.0]
    print(f"{'test':32s}" + "".join(f"{v:>11.1f}" for v in vlist))
    cols = {v: B.all_bounds(v, shape) for v in vlist}
    for nme in names:
        row = ""
        for v in vlist:
            x = cols[v][nme]
            row += f"{x:11.2e}" if np.isfinite(x) and x < 1e3 else f"{'--':>11}"
        print(f"{nme:32s}{row}")
