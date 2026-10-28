# Top end of the v* range (claims O13, O23): double-pulsar-limited bounds at 2920 and 3000 km/s,
# with the mass-bias factor 2.4666 (masses from omega-dot and s, as Kramer et al. 2021 did) and 2.5.
import sys, importlib.util
spec = importlib.util.spec_from_file_location("vb", "/home/paul/.claude/projects/-home-paul-git-reinholdtsen-conjugate-matter/7156ee3a-6166-4b9e-84c4-fb9703a50211/mg/verify-ordinary-tests-numbers/vot_bounds_lib.py")
vb = importlib.util.module_from_spec(spec); spec.loader.exec_module(vb)
for fac, lab in [(vb.fac_s, "omega-dot+s"), (2.5, "omega-dot+R")]:
    vb.dp_limit = 1.3e-4/fac
    for shape in ['gauss', 'lorentz']:
        for vs in [2920., 3000.]:
            b = vb.bounds(vs, shape)
            k = min(b, key=b.get)
            print(f"{lab:12s} {shape:8s} v* = {vs:6.0f}: strongest {k} {b[k]:.3g}; Mars {b['prec Mars']:.3g}")
