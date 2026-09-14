#!/usr/bin/env python3
from pathlib import Path
import argparse, difflib, sys
ROOT=Path(__file__).resolve().parents[1]

def render():
    version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
    template=(ROOT/'src/index.template.html').read_text(encoding='utf-8')
    css=(ROOT/'src/styles.css').read_text(encoding='utf-8').rstrip('\n')
    js=(ROOT/'src/game.js').read_text(encoding='utf-8').rstrip('\n')
    out=template.replace('{{STYLES}}',css+'\n').replace('{{SCRIPT}}',js+'\n').replace('{{VERSION}}',version)
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--check',action='store_true')
    args=ap.parse_args()
    generated=render()
    target=ROOT/'index.html'
    version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
    sw_template=(ROOT/'src/service-worker.template.js').read_text(encoding='utf-8')
    generated_sw=sw_template.replace('{{VERSION}}',version)
    sw_target=ROOT/'service-worker.js'
    if args.check:
        failures=[]
        existing=target.read_text(encoding='utf-8') if target.exists() else ''
        if existing != generated:
            failures.append('index.html is not reproducible from src/')
            diff=''.join(difflib.unified_diff(existing.splitlines(True),generated.splitlines(True),fromfile='index.html',tofile='generated'))
            print(diff[:5000],file=sys.stderr)
        existing_sw=sw_target.read_text(encoding='utf-8') if sw_target.exists() else ''
        if existing_sw != generated_sw: failures.append('service-worker.js is not reproducible from src/')
        if failures:
            print('\n'.join(failures),file=sys.stderr); return 1
        print('build check PASS')
        return 0
    target.write_text(generated,encoding='utf-8')
    sw_target.write_text(generated_sw,encoding='utf-8')
    print(f'built {target} and {sw_target} version {version}')
    return 0

if __name__=='__main__':
    raise SystemExit(main())
