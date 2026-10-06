"""Build resource indexes and fetch openly accessible assigned readings."""
import concurrent.futures
import hashlib
import json
import re
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'study-resources'
def get(url):
    with urllib.request.urlopen(urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'}), timeout=90) as r:
        return r.read()

readings = [
    ('making-data-science-systems-work', 'Making data science systems work', 'https://journals.sagepub.com/doi/pdf/10.1177/2053951720939605'),
    ('who-validates-the-validators', 'Who Validates the Validators?', 'https://arxiv.org/pdf/2404.12272'),
    ('ml-test-score', 'The ML Test Score', 'https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46555.pdf'),
    ('data-cascades', 'Data Cascades in High-Stakes AI', 'https://www.shivanikapania.com/assets/chi2021paper.pdf'),
    ('how-engineers-operationalize-ml', 'How Engineers Operationalize Machine Learning', 'https://arxiv.org/pdf/2403.16795'),
]
def collect(entry):
    name, title, url = entry
    record = dict(title=title, url=url)
    try:
        data = get(url)
        if not data.startswith(b'%PDF-'):
            raise ValueError('Response is not a PDF')
        folder = OUT / 'readings'
        folder.mkdir(exist_ok=True)
        (folder / f'{name}.pdf').write_bytes(data)
        record.update(file=f'readings/{name}.pdf', bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
    except Exception as exc:
        record['download_error'] = str(exc)
    print(title, ':', record.get('file', record.get('download_error')), flush=True)
    return record
with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
    records = list(pool.map(collect, readings))
(OUT / 'reading-sources.json').write_text(json.dumps(records, indent=2), encoding='utf-8')

decks = json.loads((OUT / 'slide-sources.json').read_text())
rows = ['# Midterm study resources', '', 'Collected 2026-10-05 from the [Fall 2026 course site](https://mlip-cmu.github.io/f2026/).', '', 'Start with [the preparation guide](../MIDTERM_PREP.md). PDF exports retain diagrams; searchable text is supplementary and can omit images or distort symbols.', '', '## Lecture slides', '', '| Lecture | Local PDF | Original deck |', '| --- | --- | --- |']
dates = [('Aug 25','Introduction and Motivation'), ('Aug 27','Correctness and Risk'), ('Sep 1','Setting Goals, Gathering Requirements'), ('Sep 3','Planning for Mistakes'), ('Sep 8','Model Quality'), ('Sep 10','Behavioral Model Testing'), ('Sep 15','Fostering Interdisciplinary (Student) Teams'), ('Sep 17','Testing and Experimenting in Production'), ('Sep 22','Deploying a Model'), ('Sep 24','Automating and Testing ML Pipelines'), ('Sep 29','Data Quality'), ('Oct 1','Scaling the System'), ('Oct 6','Planning for Operations')]
for date, title in dates:
    r = next(r for r in decks if r['title'] == title)
    local = f"[PDF]({r['pdf']})" if 'pdf' in r else 'Export unavailable'
    rows.append(f"| {date}: {title} | {local} | [Slides]({r['url'].strip()}) |")
rows.extend(['', '## Assigned readings', '', 'Author preprints may differ from the published edition linked by the course. The SAGE reading may require opening the original link if automated download fails.', '', '| Reading | Local copy | Public source |', '| --- | --- | --- |'])
for r in records:
    local = f"[PDF]({r['file']})" if 'file' in r else 'Download unavailable'
    rows.append(f"| {r['title']} | {local} | [Source]({r['url']}) |")
rows.extend(['', '## Other official resources', '', '- [Free textbook](https://mlip-cmu.github.io/book/): use the chapter pointers in the schedule.', '- [Spring 2026 recordings](https://www.youtube.com/playlist?list=PLDS2JMJnJzdmubSKnanmIwzr08cionWm_): a fallback for missing explanations; topic order can differ.', '- [Official exam instructions](https://github.com/mlip-cmu/f2026/tree/main/exams); [local snapshot](exam-instructions.md).', '- [Learning goals](learning-goals.md): broad course inventory, not an exact Fall 2026 exam scope document.', '- [Pipeline testing examples](https://github.com/mlip-cmu/pipeline-testing).', '- [Data quality examples](https://github.com/mlip-cmu/data-quality).', '- [Scaling examples](https://github.com/mlip-cmu/scaling).', '- [Labs](https://github.com/mlip-cmu/f2026/tree/main/labs) and [assignments](https://github.com/mlip-cmu/f2026/tree/main/assignments).', '', '## Provenance', '', 'slide-sources.json and reading-sources.json record URLs, byte counts, and SHA-256 hashes for downloaded PDFs. course-site.html and course-site.txt preserve the schedule snapshot. Live course updates and staff announcements take precedence.'])
(OUT / 'README.md').write_text('\n'.join(rows)+'\n', encoding='utf-8')
older = json.loads((ROOT / 'exams' / 'older-sources.json').read_text())
rows = ['# Earlier practice papers linked by Fall 2026', '', 'These are from the predecessor course repository, ckaestne/seai. Prefer the more recent first midterms for current preparation.', '', '| File | Source |', '| --- | --- |']
for r in older:
    filename = Path(r['file']).name
    rows.append(f"| [{filename}]({filename}) | [Source]({r['source']}) |")
rows.extend(['', 'The course labels the S2020 paper as Summer 2020. Its GitHub branch is S2020; inspect the paper itself for semester wording.', '', 'The linked Spring 2021 exams directory contains no PDF at collection time. The Fall 2019 final is historical supplementary material, not a first-midterm scope guide.', '', 'See ../older-sources.json for download hashes and byte counts.'])
(ROOT / 'exams' / 'older' / 'README.md').write_text('\n'.join(rows)+'\n', encoding='utf-8')
entries = json.loads(get('https://api.github.com/repos/ckaestne/seai/contents/exams?ref=S2021'))
print('Spring 2021 directory entries:', [(e['name'], e['type']) for e in entries])
