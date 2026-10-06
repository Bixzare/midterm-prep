"""Extract text for study and render selected source pages for inspection."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'tmp' / 'pdf-tools'))
import pymupdf as fitz

out = ROOT / 'tmp' / 'pdf-inspection'
out.mkdir(parents=True, exist_ok=True)
for path in sorted((ROOT / 'exams').rglob('*.pdf')):
    doc = fitz.open(path)
    text = '\n'.join(f'\n--- PAGE {i+1} ---\n' + p.get_text() for i, p in enumerate(doc))
    (out / (path.stem + '.txt')).write_text(text, encoding='utf-8')
    print(path.name, 'pages=', len(doc), 'text_chars=', len(text))
    if path.name == 'Midterm 1 S26 MLiP.pdf':
        for i in range(len(doc)):
            doc[i].get_pixmap(matrix=fitz.Matrix(1.2, 1.2)).save(out / f'S26-page-{i+1}.png')
    doc.close()
for name, pages in {'scaling-the-system.pdf': [1], 'setting-goals-gathering-requirements.pdf': [49, 50]}.items():
    doc = fitz.open(ROOT / 'study-resources' / 'slides' / name)
    for page in pages:
        if page < len(doc):
            doc[page].get_pixmap(matrix=fitz.Matrix(1.2, 1.2)).save(out / f'{Path(name).stem}-{page+1}.png')
    doc.close()
