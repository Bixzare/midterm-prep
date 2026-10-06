"""Create a standalone import guide with complete video prompts and checklists."""
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
source = (ROOT / 'NOTEBOOKLM_PROMPTS.md').read_text(encoding='utf-8')
common = re.search(r'## Shared video prompt.*?```text\n(.*?)```', source, re.S).group(1).strip()
common = common.removesuffix('MODULE BRIEF:').strip()
modules = [
    ('Product, goals, requirements, and teams', ['introduction-and-motivation.pdf', 'setting-goals-gathering-requirements.pdf', 'fostering-interdisciplinary-student-teams.pdf', 'making-data-science-systems-work.pdf'], 'Explain a stakeholder goal, a measurable outcome, REQ/SPEC/ASM, and a teamwork intervention.'),
    ('Correctness, risk, and safeguards', ['correctness-and-risk.pdf', 'planning-for-mistakes.pdf'], 'Trace a loss through a fault tree and explain how a concrete safeguard changes the failure path.'),
    ('Model evaluation and behavioral testing', ['model-quality.pdf', 'behavioral-model-testing.pdf', 'who-validates-the-validators.pdf'], 'Choose a metric/baseline and design a slice, capability test, metamorphic relation, and judge validation.'),
    ('Data quality, pipelines, and CI', ['data-quality.pdf', 'automating-and-testing-ml-pipelines.pdf', 'data-cascades.pdf', 'ml-test-score.pdf'], 'Distinguish three types of drift and give useful data, model, and infrastructure checks.'),
    ('Telemetry and production experiments', ['testing-and-experimenting-in-production.pdf'], 'Specify a telemetry computation, choose an experiment, and interpret statistical evidence correctly.'),
    ('Deployment, scaling, and operations', ['deploying-a-model.pdf', 'scaling-the-system.pdf', 'planning-for-operations.pdf', 'how-engineers-operationalize-ml.pdf'], 'Justify model placement and processing architecture, then explain monitoring and recovery.'),
]
briefs = []
for number in range(1, 7):
    match = re.search(rf'## Module {number} brief:.*?```text\n(.*?)```', source, re.S)
    assert match, number
    briefs.append(match.group(1).strip())

intro = '''# Final NotebookLM guide: MLiP first midterm

## Your plan and the role of this guide

Your exam is Friday, October 9, 2026, at 5 p.m., according to your local arrangements. Finish the concept pass by EOD tomorrow, Tuesday, October 6; begin practice papers Wednesday; use Thursday to repair weaknesses and prepare permitted notes.

This is a TA-created study guide, not an official exam scope or answer key. The six concept modules cover the 13 lectures before the public first-midterm boundary and the five associated readings. Follow any newer staff instructions. Older papers illustrate historical question styles; they do not establish current topic coverage.

Import THIS FILE as a NotebookLM source. It contains all instructions, exact source checklists, and complete prompts. No shared-prompt assembly or access to another guide is required. If importing Markdown is unavailable in your interface, paste the file's content as a text source. Local file paths are organizational references; importing this guide does not import its referenced PDFs.

## What to import

You have already imported the readings and papers in exams/older. Keep them. Also import all 13 PDFs from study-resources/slides: the readings and older exams alone do not provide all current lecture content. Import the PDF files, not the README files or text exports.

The complete source inventory is:

| Folder | PDFs |
| --- | --- |
| study-resources/readings | making-data-science-systems-work.pdf; who-validates-the-validators.pdf; ml-test-score.pdf; data-cascades.pdf; how-engineers-operationalize-ml.pdf |
| study-resources/slides | introduction-and-motivation.pdf; setting-goals-gathering-requirements.pdf; fostering-interdisciplinary-student-teams.pdf; correctness-and-risk.pdf; planning-for-mistakes.pdf; model-quality.pdf; behavioral-model-testing.pdf; data-quality.pdf; automating-and-testing-ml-pipelines.pdf; testing-and-experimenting-in-production.pdf; deploying-a-model.pdf; scaling-the-system.pdf; planning-for-operations.pdf |
| exams/older (already imported) | F2019-practice_midterm.pdf; F2019-midterm.pdf; F2019-final_exam.pdf; S2020-midterm.pdf; F2020-midterm_f20.pdf; S2022-midterm-s22.pdf; F2022-midterm-f22.pdf |

Check that imported sources contain readable content and diagrams. If NotebookLM changes a displayed title, use the PDF filename to identify the matching source and rename it if convenient.

## How to use the source checkboxes

Before EVERY generation, clear the previous selection, then check exactly the files listed under that video's checklist, including this guide. Leave every other source unchecked. In particular, leave ALL seven older exam papers unchecked for concept videos 1-6. They can contain different scope or old logistics and you want to encounter practice questions fresh later.

Keep this guide checked to provide learning instructions and the six-module structure. Treat original slides/readings as the factual authority. Do not treat this guide as independent evidence for a course claim. The prompts repeat that rule.

Select the sources for the particular generation if your interface provides source selection there; otherwise use the notebook's source checkboxes before opening customization. Choose an explanatory Video Overview format if offered, and paste that video's entire prompt. Exact controls can vary by account. Requested 10-12 minute lengths and questions are guidance, not guaranteed output behavior. The video itself is not an interactive quiz; pause questions support self-checking, while chat supports interactive practice.

Budget roughly 4-5 focused hours for six videos/explanations, quizzes, and repairs. Work in three blocks: videos 1-2, videos 3-4, videos 5-6. For each: watch, explain the main distinctions aloud for two minutes, quiz for about 15 minutes, and log mistakes. If a video omits a listed concept, ask for a short source-grounded explanation rather than regenerating the whole video. If generation is delayed or limited, paste the video prompt into chat and request a concise illustrated written walkthrough.

## Quick selection map

| Video | Focus | Lectures / readings |
| --- | --- | --- |
| 1 | Product, requirements, teams | Introduction; Goals/Requirements; Teams; Making data science systems work |
| 2 | Correctness and risk | Correctness/Risk; Planning for Mistakes |
| 3 | Evaluation | Model Quality; Behavioral Testing; Who Validates the Validators? |
| 4 | Data and pipelines | Data Quality; Pipelines/CI; Data Cascades; ML Test Score |
| 5 | Production evidence | Testing and Experimenting in Production |
| 6 | Architecture and operation | Deployment; Scaling; Operations; How Engineers Operationalize ML |
| 7 (optional, practice day) | Historical question/answer structure | Two 2022 midterms plus three current lecture decks; exact list below |

## Prompts for the six concept videos

Each prompt below is complete. Copy ONE whole code block into the video customization field. Do not concatenate all six prompts or ask for the whole course in one video.
'''
parts = [intro]
for number, ((title, files, checkpoint), brief) in enumerate(zip(modules, briefs), 1):
    for filename in files:
        assert any((ROOT / 'study-resources' / folder / filename).is_file() for folder in ['slides', 'readings']), filename
    parts += [f'\n### Video {number}: {title}\n\nCheckbox these sources only:\n', '- [ ] NOTEBOOKLM_FINAL_GUIDE.md (this guide)\n']
    parts.extend(f'- [ ] {filename}\n' for filename in files)
    parts += ['\nLeave all other sources, including all older exams, unchecked.\n\nPaste this entire prompt:\n\n```text\n',
              f'VIDEO {number}: {title}\n\n', common,
              '\n\nThe selected NOTEBOOKLM_FINAL_GUIDE.md supplies instructions only. Use the\nselected lecture PDFs and reading PDFs as factual authority. Focus only on\nthis video; do not summarize the guide or teach its other modules.\n\n',
              f'Allowed factual sources: {", ".join(files)}.\n\nTOPICS TO TEACH:\n', brief, '\n```\n\n',
              f'After viewing, your checkpoint is: **{checkpoint}**\n']

parts.append('''
## Interactive quiz after each concept video

Keep EXACTLY the same source checkboxes as the video you just watched. Use this prompt in NotebookLM chat. Change only the video number; the guide contains that video's topic list. This is original conceptual practice, not practice-paper solutions.

```text
Act as my interactive Machine Learning in Production TA. Quiz me on Video
[NUMBER] from NOTEBOOKLM_FINAL_GUIDE.md, using its topic list and only the
selected lecture/reading sources. The guide supplies instructions, not
independent evidence. Ask eight questions ONE AT A TIME and wait for my
answer. Do not give the answer in the question or reveal later answers.

Use five multiple-choice questions with misconception-based distractors
and three short-answer application questions. Use invented product scenarios
and test distinctions, mechanisms, tradeoffs, and limitations. Include a
calculation only if relevant to this module. Do not use past-exam questions.

After each answer, assess it, cite the relevant source section or slide,
and explain the precise misconception briefly. Assess short answers by their
mechanism and scenario connection, not just keywords. If I am wrong, offer
one hint and allow a retry, while recording my first attempt separately.
Ask one clarifying question if my answer is ambiguous. If the source does
not support a confident assessment, say so rather than inventing a rubric.

At the end list first-attempt results, weak concepts, concepts not tested,
and up to three five-minute repair tasks. Do not call this an official grade
or a prediction of my exam score. Re-test weaknesses using different examples.
```

If using a built-in quiz instead of chat, customize its topic with the corresponding video's topic list and choose a challenging difficulty if available. It may not follow the conversational sequence above. Follow up on mistakes in chat.

### Five-minute repair prompt

Keep that module's sources checked. Replace the bracketed concept:

```text
Explain [CONCEPT OR DISTINCTION] using the selected course sources, in at
most 300 words. Give the definition, why it matters, a correct example,
a tempting wrong example, and the decisive distinction. Cite the source.
Then ask one new application question and wait for my answer before giving
feedback. Do not expand into unrelated topics.
```

## End-of-concept-pass audit: do this tomorrow

Checkbox this guide, all 13 lecture PDFs, and all five reading PDFs. Keep ALL older exams unchecked. Allow 25-30 minutes. Use chat, not a seventh concept video:

```text
Audit my conceptual preparation for the first midterm using the six video
topic lists in NOTEBOOKLM_FINAL_GUIDE.md and the selected 13 lecture decks
and five readings. Treat the guide as instructions and original course
materials as evidence. Ignore old administrative dates and later topics.

First compare the six topic lists with the decks' learning goals and key
concepts. Produce a compact coverage table: concept, source/slide or section,
what I must explain or do, and video number. Flag important omissions from
the topic lists and requests not supported by the sources. Cite only references
you can locate. Do not assume a generated video covered a requested concept.

Then ask 12 mixed questions ONE AT A TIME: one conceptual distinction and
one short application question per module. Wait for each answer and provide
source-grounded feedback. Track first-attempt understanding. Finish with
my five most important weaknesses and a short repair list. Explain that
this is a limited diagnostic, not proof of mastery or official exam coverage.
```

## Optional Video 7: using your older exams on practice day

Generate this only AFTER independently attempting selected historical questions. It is optional; prioritize actually writing answers over watching another video. The most recent first-midterm papers are recommended for practice too: import `Midterm 1 S26 MLiP.pdf` and `Midterm 1 F25.pdf` from the main exams folder when you are ready. They are not assumed to be imported yet and are not in the checkbox list below.

For this video using the files you already imported, checkbox ONLY:

- [ ] NOTEBOOKLM_FINAL_GUIDE.md
- [ ] F2022-midterm-f22.pdf
- [ ] S2022-midterm-s22.pdf
- [ ] setting-goals-gathering-requirements.pdf
- [ ] model-quality.pdf
- [ ] planning-for-mistakes.pdf

Leave every other paper unchecked, including F2019-final_exam.pdf. Its role is historical final-exam practice, not the current first-midterm boundary. If a topic in the 2022 papers is absent from these selected current decks, identify the limitation instead of adding it to the assumed current scope.

Paste this complete prompt:

```text
Create a focused TA explanation of how to READ and STRUCTURE answers to
scenario-based Machine Learning in Production questions. Use only the
selected two historical midterms and three current lecture decks. The
selected final guide supplies instructions only.

Identify the actual question forms present in these papers and label their
historical semester. Explain how to extract stakeholders, goals, model tasks,
data constraints, software actions, environmental assumptions, and losses
from a scenario. Demonstrate reading the command verb and respecting the
requested number/type of answers. Where the papers support it, show structures
for a measure with collection/computation, a model-evaluation argument,
requirements reasoning, and a mitigation with a causal mechanism.

Use a NEW invented food-ordering assistant example for worked answers. Do
not solve or reveal answers to the historical paper questions. Contrast a
vague keyword-only response with a concise scenario-grounded response.
Explain why definitions alone may fail to answer an application question.
Show how to check that each requested part has been addressed.

Do not invent an official solution, grading rubric, exam weight, or current
coverage from the old papers. Flag historical topics not supported by the
selected current lecture decks. End with a short self-review checklist and
three pause-and-answer prompts. Aim for 8-10 minutes without sacrificing
clarity to force a length.
```

## Getting feedback on your written practice answer

Select this guide, ONLY the exam you are currently attempting, and the lecture/readings relevant to the question. For example, for a requirements question from F2022, select `F2022-midterm-f22.pdf` and `setting-goals-gathering-requirements.pdf` plus this guide. Select different sources for a different question; do not assume that example covers a whole paper. Add a staff rubric from Slack if available and permitted, clearly identified as such.

```text
I have independently attempted the following question. Read the question
in the selected exam and assess my answer against its wording, scenario,
and selected course sources. Do not claim an official solution or assign
an official mark without an actual staff rubric. If I provided a staff rubric,
distinguish its explicit criteria from your interpretation.

Identify: parts I answered correctly, missing requested parts, incorrect
mechanisms, ignored constraints, vague claims, and any unsupported assumptions.
Cite the course source supporting corrections. Ask me to revise the weakest
part before giving a complete model answer. Keep feedback concise.

Paper and question number: [INSERT]
My answer: [PASTE MY INDEPENDENT ANSWER]
```

## Completion checklist

- [ ] Imported this final guide, 13 current lecture PDFs, and five complete readings.
- [ ] Used the exact source selection for each concept video.
- [ ] Explained each video's checkpoint aloud without looking at the slides.
- [ ] Took the six quizzes and recorded precise misconceptions.
- [ ] Ran the concept audit and repaired essential omissions.
- [ ] Started independent practice papers the following day.
- [ ] Used Thursday for repair and organizing permitted notes.

Do not spend the week optimizing video appearance. Your useful output is an ability to explain concepts and write concrete answers, supported by a short error log. Consult staff announcements for local exam arrangements and current rules.

## Provenance

This guide organizes local resources collected from the public Fall 2026 course: https://mlip-cmu.github.io/f2026/ . The reading and slide manifests in study-resources record original URLs and file hashes; exams/older-sources.json records historical papers. Those manifests do not need to be imported. Existing author preprints can differ from assigned published editions. The guide does not require importing the earlier planning files, README indexes, whole textbook, later lectures, or second-midterm papers.
''')
destination = ROOT / 'NOTEBOOKLM_FINAL_GUIDE.md'
destination.write_text(''.join(parts), encoding='utf-8')
text = destination.read_text(encoding='utf-8')
assert text.count('```') % 2 == 0
assert len(re.findall(r'^### Video [1-6]:', text, re.M)) == 6
assert all(name in text for _, files, _ in modules for name in files)
print(f'Created {destination.name}: six standalone concept prompts, exact checklists, optional historical-practice video, quizzes, and audit.')
