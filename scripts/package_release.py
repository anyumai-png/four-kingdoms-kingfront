#!/usr/bin/env python3
from pathlib import Path
import hashlib, json, shutil, subprocess, zipfile
ROOT=Path(__file__).resolve().parents[1]
version=(ROOT/'VERSION').read_text(encoding='utf-8').strip()
subprocess.run(['python3',str(ROOT/'scripts/build.py'),'--check'],check=True)
release_dir=ROOT/'dist'/f'kingfront-{version}'
if release_dir.exists(): shutil.rmtree(release_dir)
release_dir.mkdir(parents=True)
for name in ['index.html','manifest.webmanifest','service-worker.js','assets/icon-192.png','assets/icon-512.png','assets/apple-touch-icon.png']:
    dest=release_dir/name; dest.parent.mkdir(parents=True,exist_ok=True); shutil.copy2(ROOT/name,dest)
readme=f'''# Four Kingdoms — Kingfront {version}\n\nStatic HTTPS deployment package.\n\nUpload the contents of this folder to Cloudflare Pages or another static HTTPS host.\n\nValidated source checkpoint: {version}\n'''
(release_dir/'README.md').write_text(readme,encoding='utf-8')
checks={}
for p in sorted(release_dir.rglob('*')):
    if p.is_file(): checks[p.relative_to(release_dir).as_posix()]=hashlib.sha256(p.read_bytes()).hexdigest()
(release_dir/'SHA256SUMS.json').write_text(json.dumps(checks,indent=2,sort_keys=True)+"\n",encoding='utf-8')
zip_path=ROOT/'releases'/f'four-kingdoms-kingfront-v{version}-cloudflare.zip'
if zip_path.exists(): zip_path.unlink()
with zipfile.ZipFile(zip_path,'w',zipfile.ZIP_DEFLATED) as z:
    for p in sorted(release_dir.rglob('*')):
        if p.is_file(): z.write(p,p.relative_to(release_dir).as_posix())
print(zip_path)
