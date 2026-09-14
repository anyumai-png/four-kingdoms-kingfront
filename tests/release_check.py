#!/usr/bin/env python3
from pathlib import Path
import hashlib,json,re,subprocess,tempfile,zipfile
ROOT=Path(__file__).resolve().parents[1]
version=(ROOT/'VERSION').read_text().strip()
subprocess.run(['python3',str(ROOT/'scripts/package_release.py')],check=True,capture_output=True,text=True)
zip_path=ROOT/'releases'/f'four-kingdoms-kingfront-v{version}-cloudflare.zip'
assert zip_path.exists(), zip_path
with tempfile.TemporaryDirectory() as td:
    with zipfile.ZipFile(zip_path) as z:
        names=sorted(z.namelist())
        expected=sorted(['README.md','SHA256SUMS.json','index.html','manifest.webmanifest','service-worker.js','assets/icon-192.png','assets/icon-512.png','assets/apple-touch-icon.png'])
        assert names==expected,(names,expected)
        z.extractall(td)
    t=Path(td)
    sums=json.loads((t/'SHA256SUMS.json').read_text())
    for name,expected_hash in sums.items():
        got=hashlib.sha256((t/name).read_bytes()).hexdigest()
        assert got==expected_hash,(name,got,expected_hash)
    html=(t/'index.html').read_text()
    assert f'window.__KINGFRONT_VERSION__="{version}"' in html
    manifest=json.loads((t/'manifest.webmanifest').read_text())
    assert manifest['name'].startswith('Four Kingdoms')
    assert manifest['display']=='standalone'
    assert manifest['orientation']=='landscape'
    assert len(manifest.get('icons',[]))>=2
    sw=(t/'service-worker.js').read_text()
    assert f'kingfront-v{version}' in sw
    assert 'assets/icon-192.png' in sw
print('release package check PASS',zip_path)
