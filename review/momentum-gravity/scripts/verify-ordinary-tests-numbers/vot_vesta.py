# Caveat for the Dawn-Ceres candidate (vot_extra.py): pre-Dawn ephemeris GM of Vesta against Dawn's.
# pre-Dawn (2011 Dawn gravity overview, NTRS 20140010847, via search snippet [S]):
#   Michalak 2000 18.1+-0.7, Standish 2001 17.8+-0.2, Pitjeva 2005 17.84+-0.27, Konopliv 2006 18.03+-0.21 km^3/s^2
# Dawn (Konopliv et al. 2014, Icarus 240): 17.288 km^3/s^2 (dagger: from memory, not retrieved)
pre = {'Michalak 2000': (18.1, 0.7), 'Standish 2001': (17.8, 0.2), 'Pitjeva 2005': (17.84, 0.27), 'Konopliv 2006': (18.03, 0.21)}
dawn = 17.288
for k, (g, s) in pre.items():
    print(f"{k:14s}: GM_Dawn/GM_pre - 1 = {dawn/g - 1:+.4f} +- {dawn*s/g**2:.4f}  ({(dawn/g - 1)/(dawn*s/g**2):+.1f} sigma)")
