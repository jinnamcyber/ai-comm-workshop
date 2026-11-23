#!/usr/bin/env python3
"""Draw every job in manifest.py with Codex (via MV_tools/codex_gen.sh) into raw/. Skips existing. PAR env = parallelism.
Usage: python3 run_all.py [name ...]"""
import os, subprocess, sys, concurrent.futures as cf
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
from manifest import JOBS, style_for
RAW = os.path.join(HERE, 'raw'); os.makedirs(RAW, exist_ok=True)
GEN = os.path.expanduser('~/Documents/Claude/Projects/MV_tools/codex_gen.sh')
def run(name):
    out = os.path.join(RAW, name + '.png')
    if os.path.exists(out): return name + ' (exists)'
    subprocess.run([GEN, RAW, name, JOBS[name] + '\n\n' + style_for(name)])
    return name + (' ok' if os.path.exists(out) else ' FAILED')
names = sys.argv[1:] or list(JOBS)
with cf.ThreadPoolExecutor(int(os.environ.get('PAR', 5))) as ex:
    for r in ex.map(run, names): print(r, flush=True)
print('ALL DONE', flush=True)
