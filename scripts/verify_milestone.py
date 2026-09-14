#!/usr/bin/env python3
from pathlib import Path
import subprocess, sys
ROOT=Path(__file__).resolve().parents[1]
steps=[
    ['python3',str(ROOT/'scripts/build.py'),'--check'],
    ['node','--check',str(ROOT/'src/game.js')],
    ['python3',str(ROOT/'tests/browser_regression.py')],
    ['python3',str(ROOT/'tests/monte_carlo.py')],
    ['python3',str(ROOT/'scripts/package_release.py')],
    ['python3',str(ROOT/'tests/release_check.py')],
]
for cmd in steps:
    print('\n==>', ' '.join(cmd), flush=True)
    cp=subprocess.run(cmd,cwd=ROOT)
    if cp.returncode:
        print('MILESTONE VERIFY FAIL:', ' '.join(cmd), file=sys.stderr)
        raise SystemExit(cp.returncode)
print('\nMILESTONE VERIFY PASS')
