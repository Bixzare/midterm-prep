"""Verify downloaded PDFs, recorded hashes, and local index links."""
import hashlib
import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tmp' / 'pdf-tools'))
import pymupdf

count = pages = 0
for folder, name in [('exams', 'sources.json'), ('exams', 'older-sources.json'), ('study-resources', 'slide-sources.json'), ('study-resources', 'reading-sources.json')]:
    for record in json.loads((ROOT / folder / name).read_text(encoding='utf-8-sig')):
        local = record.get('file', record.get('pdf'))
        if not local:
            continue
        path = ROOT / folder / local
        assert hashlib.sha256(path.read_bytes()).hexdigest() == record['sha256'], path
        with pymupdf.open(path) as doc:
            assert len(doc) > 0, path
            pages += len(doc)
        count += 1
errors = []
for filename in ['README.md', 'MIDTERM_PREP.md', 'study-resources/README.md', 'exams/README.md', 'exams/older/README.md']:
    path = ROOT / filename
    for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8-sig')):
        if target.startswith(('http:', 'https:', '#')):
            continue
        if not (path.parent / unquote(target.split('#')[0])).exists():
            errors.append((filename, target))
assert not errors, errors
for path in (ROOT / 'scripts').glob('*.py'):
    compile(path.read_text(encoding='utf-8'), str(path), 'exec')
print(f'Verified {count} PDFs, {pages} pages, recorded checksums, local guide/index links, and script syntax.')
