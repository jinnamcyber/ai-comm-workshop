#!/bin/bash
# Re-run Codex jobs one at a time until all exist (max 6 passes), pausing after rate limits.
cd "$(dirname "$0")"
for pass in 1 2 3 4 5 6; do
  PAR=1 python3 run_all.py
  missing=$(python3 -c 'import os,manifest; print(sum(not os.path.exists("raw/"+n+".png") for n in manifest.JOBS))')
  echo "pass $pass missing $missing"
  [ "$missing" = "0" ] && break
  sleep 90
done
echo FINISHED
