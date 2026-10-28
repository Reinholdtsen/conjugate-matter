"""Run diagnostics.py --one on every finished run not yet analysed, NPAR at a time; loops until no
N-body process remains and every run is analysed."""
import glob, os, subprocess, sys, time, pickle
HERE = os.path.dirname(os.path.abspath(__file__))
PY = "/home/paul/git/reinholdtsen/conjugate-matter/.venv/bin/python"
npar = int(sys.argv[1]) if len(sys.argv) > 1 else 3
legacy = set()
if os.path.exists(os.path.join(HERE, "diag_cache.pkl")):
    legacy = {k[0] for k in pickle.load(open(os.path.join(HERE, "diag_cache.pkl"), "rb"))}
running = {}
while True:
    done = legacy | {os.path.basename(f)[:-4] for f in glob.glob(os.path.join(HERE, "diag_cache", "*.pkl"))}
    todo = [f for f in sorted(glob.glob(os.path.join(HERE, "runs", "run_*.npz")))
            if os.path.basename(f) not in done and f not in running]
    running = {f: p for f, p in running.items() if p.poll() is None}
    while todo and len(running) < npar:
        f = todo.pop(0)
        cmd = f"ulimit -v 3000000; OPENBLAS_NUM_THREADS=1 timeout 3000 {PY} {os.path.join(HERE, 'diagnostics.py')} --one {f}"
        running[f] = subprocess.Popen(["bash", "-c", cmd], cwd=HERE)
        print(time.strftime("%H:%M:%S"), "diag started", os.path.basename(f), flush=True)
    nbody_alive = subprocess.run(["pgrep", "-f", "run_nbody.py"], capture_output=True).returncode == 0
    if not running and not todo and not nbody_alive:
        break
    time.sleep(10)
print(time.strftime("%H:%M:%S"), "diagnostics all done", flush=True)
