import runpy, io, contextlib
buf = io.StringIO()
with contextlib.redirect_stdout(buf):
    ns = runpy.run_path("flag6_audit.py")
k, bet, betp, gR, fR, P = ns['k'], ns['bet'], ns['betp'], ns['gR'], ns['fR'], ns['P']
lamg_num, lamf_num, comb = ns['lamg_num'], ns['lamf_num'], ns['comb']
print("k =", repr(k)); print("beta =", [repr(float(b)) for b in bet])
print("lambda_g(k) raw =", repr(float(lamg_num(k, *bet))), " lambda_f(k) raw =", repr(float(lamf_num(k, *bet))))
print("scale of lambda_g terms:", [float(bet[n]*comb(3,n)*k**n) for n in range(4)])
lg1 = sum(betp[n] * comb(3, n) for n in range(5)); lf1 = sum(betp[n] * comb(3, n - 1) for n in range(1, 5))
print("lambda_g'(1) raw =", repr(float(lg1)), " lambda_f'(1) raw =", repr(float(lf1)))
s1 = P(gR, fR, bet); s2 = P(gR, fR / k**2, betp)
print("P1 =", repr(float(s1)), " P2 =", repr(float(s2)), " diff =", repr(float(s1 - s2)))
