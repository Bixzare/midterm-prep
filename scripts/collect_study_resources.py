"""Collect public resources linked by the Fall 2026 course; preserve provenance."""
import concurrent.futures
import hashlib
import json
import re
import urllib.request
from html import unescape
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'study-resources'
OUT.mkdir(exist_ok=True)

def get(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'MLiP-study-resource-collector'})
    with urllib.request.urlopen(req, timeout=120) as response:
        return response.read()

def plain(html):
    html = re.sub(r'<(script|style)\b[^>]*>.*?</\1>', '', html, flags=re.S)
    html = re.sub(r'</(?:p|div|li|h[1-6]|tr|section)>|<br\s*/?>', '\n', html)
    html = unescape(re.sub('<[^>]+>', '', html))
    return '\n'.join(line.strip() for line in html.splitlines() if line.strip())

site = get('https://mlip-cmu.github.io/f2026/').decode()
(OUT / 'course-site.html').write_text(site, encoding='utf-8')
(OUT / 'course-site.txt').write_text(plain(site), encoding='utf-8')
exam_readme = get('https://raw.githubusercontent.com/mlip-cmu/f2026/main/exams/README.md').decode()
(OUT / 'exam-instructions.md').write_text(exam_readme, encoding='utf-8')
goals = get('https://raw.githubusercontent.com/mlip-cmu/f2026/main/learning_goals.md').decode()
(OUT / 'learning-goals.md').write_text(goals, encoding='utf-8')
schedule = site.split('id="schedule"', 1)[-1].split('id="resources"', 1)[0]
slide_links = re.findall(r'<a[^>]+href="(https://docs.google.com/presentation/d/[^"#]+)"[^>]*>(.*?)</a>', schedule, re.S)
unique = {}
for url, title in slide_links:
    deck_id = url.split('/d/')[1].split('/')[0]
    unique.setdefault(deck_id, (unescape(url), plain(title)))

def collect_deck(entry):
    deck_id, (url, title) = entry
    name = re.sub(r'[^A-Za-z0-9]+', '-', title).strip('-').lower()
    folder = OUT / 'slides'
    folder.mkdir(exist_ok=True)
    html = get(f'https://docs.google.com/presentation/d/{deck_id}/htmlpresent').decode()
    text = plain(html)
    (folder / f'{name}.txt').write_text(text, encoding='utf-8')
    record = {'title': title, 'url': url, 'text': f'slides/{name}.txt'}
    try:
        data = get(f'https://docs.google.com/presentation/d/{deck_id}/export/pdf')
        if not data.startswith(b'%PDF-'):
            raise ValueError('Not a PDF')
        (folder / f'{name}.pdf').write_bytes(data)
        record.update(pdf=f'slides/{name}.pdf', bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:
        record['pdf_error'] = str(exc)
    print('Collected slides:', title, flush=True)
    return record

records = []
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    for future in concurrent.futures.as_completed([pool.submit(collect_deck, entry) for entry in unique.items()]):
        try:
            records.append(future.result())
        except Exception as exc:
            print('SLIDE ERROR:', repr(exc), flush=True)
(OUT / 'slide-sources.json').write_text(json.dumps(sorted(records, key=lambda r: r['text']), indent=2), encoding='utf-8')

older = []
for branch, paths in {
    'F2019': ['other_material/practice_midterm.pdf', 'other_material/midterm.pdf', 'other_material/final_exam.pdf'],
    'S2020': ['exams/midterm.pdf'],
    'F2020': ['exams/midterm_f20.pdf'],
    'S2021': None, 'S2022': None, 'F2022': None,
}.items():
    if paths is None:
        entries = json.loads(get(f'https://api.github.com/repos/ckaestne/seai/contents/exams?ref={branch}'))
        paths = [e['path'] for e in entries if e['path'].lower().endswith('.pdf')]
    for path in paths:
        filename = f'{branch}-{Path(path).name}'
        url = f'https://raw.githubusercontent.com/ckaestne/seai/{branch}/{path}'
        data = get(url)
        if not data.startswith(b'%PDF-'):
            raise ValueError(f'Not a PDF: {url}')
        target = ROOT / 'exams' / 'older' / filename
        target.parent.mkdir(exist_ok=True)
        target.write_bytes(data)
        older.append({'file': f'older/{filename}', 'source': url, 'bytes': len(data), 'sha256': hashlib.sha256(data).hexdigest()})
        print('Collected older exam:', filename, flush=True)
(ROOT / 'exams' / 'older-sources.json').write_text(json.dumps(older, indent=2), encoding='utf-8')
print(f'Done: {len(records)} decks, {len(older)} older PDFs.', flush=True)
