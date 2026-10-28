"""Job queue for the corner N-body runs: at most NPAR concurrent processes, each under
ulimit -v 3000000 and a timeout, single-threaded.  Usage: python batch.py <jobfile> <npar>
Each line of the job file holds the arguments for run_nbody.py."""
import subprocess
import sys
import time
import os

HERE = os.path.dirname(os.path.abspath(__file__))
PY = "/home/paul/git/reinholdtsen/conjugate-matter/.venv/bin/python"
jobs = [l.strip() for l in open(sys.argv[1]) if l.strip() and not l.startswith("#")]
npar = int(sys.argv[2])
running = []
os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
while jobs or running:
    running = [(p, a) for p, a in running if p.poll() is None]
    while jobs and len(running) < npar:
        a = jobs.pop(0)
        tag = a.replace("--", "").replace(" ", "_")
        log = open(os.path.join(HERE, "runs", f"log_{tag}.txt"), "w")
        cmd = (f"ulimit -v 3000000; OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1 timeout 4000 "
               f"{PY} {os.path.join(HERE, 'run_nbody.py')} {a} --quiet")
        p = subprocess.Popen(["bash", "-c", cmd], stdout=log, stderr=subprocess.STDOUT, cwd=HERE)
        running.append((p, a))
        print(time.strftime("%H:%M:%S"), "started:", a, flush=True)
    time.sleep(5)
print(time.strftime("%H:%M:%S"), "all done", flush=True)
