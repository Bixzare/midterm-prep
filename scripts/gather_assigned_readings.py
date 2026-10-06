"""Complete the assigned-reading folder using verified Downloads PDFs."""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tmp' / 'pdf-tools'))
import pymupdf

downloads = Path('C:/Users/djibr/Downloads')
source = downloads / 'passi-sengers-2020-making-data-science-systems-work.pdf'
with pymupdf.open(source) as doc:
    text = doc[0].get_text()
    assert 'Making data science systems work' in text, 'Unexpected paper title'
    assert 'Passi' in text and 'Sengers' in text, 'Unexpected paper authors'
    assert len(doc) == 13, 'Unexpected paper length'
    print('Verified missing reading:', source.name, 'pages:', len(doc))
    doc[0].get_pixmap(matrix=pymupdf.Matrix(1, 1)).save(ROOT / 'tmp' / 'pdf-inspection' / 'making-data-science-first-page.png')

dest = ROOT / 'study-resources/readings/making-data-science-systems-work.pdf'
data = source.read_bytes()
if dest.exists() and dest.read_bytes() != data:
    raise RuntimeError('Refusing to overwrite a different existing reading')
dest.write_bytes(data)
manifest_path = ROOT / 'study-resources/reading-sources.json'
manifest = json.loads(manifest_path.read_text(encoding='utf-8'))
record = next(r for r in manifest if r['title'] == 'Making data science systems work')
record.pop('download_error', None)
record.update(file='readings/making-data-science-systems-work.pdf', bytes=len(data),
              sha256=hashlib.sha256(data).hexdigest(), local_source=str(source),
              acquisition='Copied from Downloads; original retained')

matching = [p for p in downloads.glob('*.pdf') if any(term in p.name.lower() for term in
            ['test score', 'valdiators', 'cascades', 'operationalize'])]
for p in matching:
    with pymupdf.open(p) as doc:
        first = ' '.join(doc[0].get_text().split())
        last = ' '.join(doc[-1].get_text().split())
        print(json.dumps({'download': p.name, 'pages': len(doc), 'first_page_excerpt': first[:220], 'last_page_excerpt': last[:100]}, ensure_ascii=False))
    sha = hashlib.sha256(p.read_bytes()).hexdigest()
    same = next((r for r in manifest if r.get('sha256') == sha), None)
    if same:
        same['also_available_in_downloads'] = str(p)

for r in manifest:
    path = ROOT / 'study-resources' / r['file']
    with pymupdf.open(path) as doc:
        r['pages'] = len(doc)
    assert hashlib.sha256(path.read_bytes()).hexdigest() == r['sha256']
manifest_path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False)+'\n', encoding='utf-8')

rows = ['# Assigned readings for the first midterm', '',
        'All five assigned pre-midterm readings are together in this folder. These are complete papers, ready to upload to NotebookLM.', '',
        '| Reading | Local PDF | Pages |', '| --- | --- | --- |']
for r in manifest:
    rows.append(f"| {r['title']} | [PDF]({Path(r['file']).name}) | {r['pages']} |")
rows += ['', '## Sources and copies', '',
         '- Making data science systems work was copied from your Downloads folder after checking its title, authors, and 13-page length. The original remains in Downloads.',
         '- The ML Test Score in Downloads is byte-for-byte identical to the copy already here.',
         '- Downloads also contains segmented copies of the validators, data cascades, and operations papers. Complete copies already exist here, so the split copies were not added as extra NotebookLM sources.',
         '- Some existing online copies are author preprints and can differ from the published editions.',
         '- [reading-sources.json](../reading-sources.json) records public URLs, local provenance, page counts, sizes, and SHA-256 checksums.',
         '', 'Scope: the five readings assigned before Midterm 1 in the public Fall 2026 schedule; later-semester readings are not included.']
(dest.parent / 'README.md').write_text('\n'.join(rows)+'\n', encoding='utf-8')
print('Complete: five verified assigned readings in study-resources/readings.')
