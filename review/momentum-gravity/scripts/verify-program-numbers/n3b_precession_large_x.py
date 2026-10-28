# Does the gated precession saturate for GM/(a v*^2) >~ 0.1 (P13), or peak and fall as orbits get faster?
import importlib.util, sys
spec = importlib.util.spec_from_file_location("n3", sys.argv[1])
src = open(sys.argv[1]).read().split('print("== precession')[0]   # reuse integrator definitions only
exec(src)
print("GM/(a v*^2)   k_ic   precession/orbit (beta = 0.2, e = 0.3)")
for x in (0.03, 0.1, 0.3, 1.0, 3.0, 10.0):
    m, adv, dH, dL, n = precession(0.2, 1/x, 0.3, 1.2, n_orb=6)
    print(f"{x:8.3f}     1.2    {m: .4e}   (dH/H {dH:.0e})")
