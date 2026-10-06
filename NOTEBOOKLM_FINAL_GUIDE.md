# Final NotebookLM guide: MLiP first midterm

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

### Video 1: Product, goals, requirements, and teams

Checkbox these sources only:
- [ ] NOTEBOOKLM_FINAL_GUIDE.md (this guide)
- [ ] introduction-and-motivation.pdf
- [ ] setting-goals-gathering-requirements.pdf
- [ ] fostering-interdisciplinary-student-teams.pdf
- [ ] making-data-science-systems-work.pdf

Leave all other sources, including all older exams, unchecked.

Paste this entire prompt:

```text
VIDEO 1: Product, goals, requirements, and teams

Act as a clear, practical TA for CMU Machine Learning in Production. I have
basic ML knowledge but missed some lectures. I am preparing for a midterm
that tests applying concepts to a product scenario. Teach the selected
module using only the selected course sources. Aim for a focused 10-12
minute explanation, but prioritize clarity and the essential distinctions
over forcing a duration.

Build a connected explanation: problem -> concept -> mechanism -> worked
example -> limitation -> how to recognize when to use it. Define jargon
before using it. Use readable diagrams, comparison tables, and simple
calculations where appropriate. Explain why each engineering choice matters.

Use one invented food-ordering assistant as the running teaching example:
it interprets requests, recommends menu items, and can place an order through
an API. Clearly label this example and any numerical assumptions as invented.
Keep examples consistent across this module. Distinguish what a model
predicts from what the software enforces and what happens in the world.

For easily confused concepts, show a correct example and a tempting wrong
example, then explain the difference. Include three brief pause-and-answer
questions. State each question before giving its explanation; invite me to
pause. End with a concise concept checklist and three common mistakes.

Use course terminology. Ignore old administrative dates in slides. Do not
invent official exam rules, topic weights, solutions, or claims of guaranteed
exam coverage. If a requested concept is not supported by these sources,
say so. Do not expand into later-semester topics except examples already
needed to explain the selected lecture material.

The selected NOTEBOOKLM_FINAL_GUIDE.md supplies instructions only. Use the
selected lecture PDFs and reading PDFs as factual authority. Focus only on
this video; do not summarize the guide or teach its other modules.

Allowed factual sources: introduction-and-motivation.pdf, setting-goals-gathering-requirements.pdf, fostering-interdisciplinary-student-teams.pdf, making-data-science-systems-work.pdf.

TOPICS TO TEACH:
Teach the system surrounding the model: data, training, inference, user
interface, actions, and feedback. Explain why a good model can belong to a
bad product and why engineers, data scientists, domain experts, and product
stakeholders need shared goals.

Distinguish organizational goals, user outcomes, and model goals. Show how
to operationalize a goal as a metric: population, numerator/denominator,
time window, data needed, and collection mechanism. Explain proxy validity
and why stakeholder goals can conflict. Connect the assigned reading's
view of a system that "works" to these competing perspectives.

Explain behavioral vs quality requirements; world, machine, and shared
phenomena; and REQ, SPEC, ASM. Show a complete example and how a violated
environmental assumption breaks the real-world requirement even when
software follows its specification. Include gathering/validating requirements
with stakeholders.

Finish with teamwork: diagnose groupthink, social loafing, unclear ownership,
and communication failures. Connect each mitigation to its cause. Explain
how AI suggestions can reinforce groupthink. Use a short team disagreement
over model accuracy versus successful customer orders.
```

After viewing, your checkpoint is: **Explain a stakeholder goal, a measurable outcome, REQ/SPEC/ASM, and a teamwork intervention.**

### Video 2: Correctness, risk, and safeguards

Checkbox these sources only:
- [ ] NOTEBOOKLM_FINAL_GUIDE.md (this guide)
- [ ] correctness-and-risk.pdf
- [ ] planning-for-mistakes.pdf

Leave all other sources, including all older exams, unchecked.

Paste this entire prompt:

```text
VIDEO 2: Correctness, risk, and safeguards

Act as a clear, practical TA for CMU Machine Learning in Production. I have
basic ML knowledge but missed some lectures. I am preparing for a midterm
that tests applying concepts to a product scenario. Teach the selected
module using only the selected course sources. Aim for a focused 10-12
minute explanation, but prioritize clarity and the essential distinctions
over forcing a duration.

Build a connected explanation: problem -> concept -> mechanism -> worked
example -> limitation -> how to recognize when to use it. Define jargon
before using it. Use readable diagrams, comparison tables, and simple
calculations where appropriate. Explain why each engineering choice matters.

Use one invented food-ordering assistant as the running teaching example:
it interprets requests, recommends menu items, and can place an order through
an API. Clearly label this example and any numerical assumptions as invented.
Keep examples consistent across this module. Distinguish what a model
predicts from what the software enforces and what happens in the world.

For easily confused concepts, show a correct example and a tempting wrong
example, then explain the difference. Include three brief pause-and-answer
questions. State each question before giving its explanation; invite me to
pause. End with a concise concept checklist and three common mistakes.

Use course terminology. Ignore old administrative dates in slides. Do not
invent official exam rules, topic weights, solutions, or claims of guaranteed
exam coverage. If a requested concept is not supported by these sources,
say so. Do not expand into later-semester topics except examples already
needed to explain the selected lecture material.

The selected NOTEBOOKLM_FINAL_GUIDE.md supplies instructions only. Use the
selected lecture PDFs and reading PDFs as factual authority. Focus only on
this video; do not summarize the guide or teach its other modules.

Allowed factual sources: correctness-and-risk.pdf, planning-for-mistakes.pdf.

TOPICS TO TEACH:
Explain correctness vs measured accuracy, verification vs validation, and
why inductively learned models provide different assurances from software
enforcing an explicit property. Use SQL injection versus prompt injection
only to illustrate the distinction covered in these lectures; avoid an
unrelated security survey.

Teach risk identification: stakeholders and values -> losses -> hazards or
unsafe situations -> causes. Distinguish likelihood, severity, acceptability,
and residual risk. Explain cost/effectiveness and ALARP without pretending
every harm can be reduced to a precise financial number.

Explain the hazard-analysis approaches actually presented, including STPA's
control/unsafe-action perspective and FTA's causal decomposition. Draw a
small fault tree, explain AND and OR gates, and revise it after a mitigation.
Show why selective review leaves an unchecked path. Do not assume component
failures are statistically independent just because there is an AND gate.

Compare human review, less forceful interfaces, confirmation/undo, deterministic
guardrails, doer-checker designs, redundancy, fallback, graceful degradation,
and isolation. For each example state trigger, intervention, remaining failure
path, and whether the claim is risk reduction or a narrowly scoped guarantee.
Explain why a second LLM or a human reviewer is not automatically a guarantee.
```

After viewing, your checkpoint is: **Trace a loss through a fault tree and explain how a concrete safeguard changes the failure path.**

### Video 3: Model evaluation and behavioral testing

Checkbox these sources only:
- [ ] NOTEBOOKLM_FINAL_GUIDE.md (this guide)
- [ ] model-quality.pdf
- [ ] behavioral-model-testing.pdf
- [ ] who-validates-the-validators.pdf

Leave all other sources, including all older exams, unchecked.

Paste this entire prompt:

```text
VIDEO 3: Model evaluation and behavioral testing

Act as a clear, practical TA for CMU Machine Learning in Production. I have
basic ML knowledge but missed some lectures. I am preparing for a midterm
that tests applying concepts to a product scenario. Teach the selected
module using only the selected course sources. Aim for a focused 10-12
minute explanation, but prioritize clarity and the essential distinctions
over forcing a duration.

Build a connected explanation: problem -> concept -> mechanism -> worked
example -> limitation -> how to recognize when to use it. Define jargon
before using it. Use readable diagrams, comparison tables, and simple
calculations where appropriate. Explain why each engineering choice matters.

Use one invented food-ordering assistant as the running teaching example:
it interprets requests, recommends menu items, and can place an order through
an API. Clearly label this example and any numerical assumptions as invented.
Keep examples consistent across this module. Distinguish what a model
predicts from what the software enforces and what happens in the world.

For easily confused concepts, show a correct example and a tempting wrong
example, then explain the difference. Include three brief pause-and-answer
questions. State each question before giving its explanation; invite me to
pause. End with a concise concept checklist and three common mistakes.

Use course terminology. Ignore old administrative dates in slides. Do not
invent official exam rules, topic weights, solutions, or claims of guaranteed
exam coverage. If a requested concept is not supported by these sources,
say so. Do not expand into later-semester topics except examples already
needed to explain the selected lecture material.

The selected NOTEBOOKLM_FINAL_GUIDE.md supplies instructions only. Use the
selected lecture PDFs and reading PDFs as factual authority. Focus only on
this video; do not summarize the guide or teach its other modules.

Allowed factual sources: model-quality.pdf, behavioral-model-testing.pdf, who-validates-the-validators.pdf.

TOPICS TO TEACH:
Teach choosing metrics and baselines from the product's task and error costs.
Define positive class, TP/FP/FN/TN, accuracy, precision, recall, and relevant
regression/ranking or generative evaluation measures in the selected sources.
Use a small numerical example of class imbalance to expose misleading accuracy.
Do not turn this into a review of model-training algorithms.

Explain train/validation/test roles; label leakage; leakage across correlated
examples; preprocessing leakage; and overfitting through repeatedly consulting
the test set, including prompt iteration. Show what to hold out and why.

Compare overall evaluation, input slicing, capability tests, invariants,
metamorphic testing, and property-based testing. Explain boundary values and
equivalence classes, the oracle problem, and generating targeted cases.
Show one existing-data slice, one labeled capability test, and one unlabeled
transformation with a justified input-output relation. Explain their limits.

For open-ended LLM output, teach rubrics and human evaluation, LLM-as-a-judge,
validating the judge against humans, and criteria drift from the reading.
Distinguish checking output format from checking truth or usefulness. Tie
evaluation to regression checks and tracking results across versions.
```

After viewing, your checkpoint is: **Choose a metric/baseline and design a slice, capability test, metamorphic relation, and judge validation.**

### Video 4: Data quality, pipelines, and CI

Checkbox these sources only:
- [ ] NOTEBOOKLM_FINAL_GUIDE.md (this guide)
- [ ] data-quality.pdf
- [ ] automating-and-testing-ml-pipelines.pdf
- [ ] data-cascades.pdf
- [ ] ml-test-score.pdf

Leave all other sources, including all older exams, unchecked.

Paste this entire prompt:

```text
VIDEO 4: Data quality, pipelines, and CI

Act as a clear, practical TA for CMU Machine Learning in Production. I have
basic ML knowledge but missed some lectures. I am preparing for a midterm
that tests applying concepts to a product scenario. Teach the selected
module using only the selected course sources. Aim for a focused 10-12
minute explanation, but prioritize clarity and the essential distinctions
over forcing a duration.

Build a connected explanation: problem -> concept -> mechanism -> worked
example -> limitation -> how to recognize when to use it. Define jargon
before using it. Use readable diagrams, comparison tables, and simple
calculations where appropriate. Explain why each engineering choice matters.

Use one invented food-ordering assistant as the running teaching example:
it interprets requests, recommends menu items, and can place an order through
an API. Clearly label this example and any numerical assumptions as invented.
Keep examples consistent across this module. Distinguish what a model
predicts from what the software enforces and what happens in the world.

For easily confused concepts, show a correct example and a tempting wrong
example, then explain the difference. Include three brief pause-and-answer
questions. State each question before giving its explanation; invite me to
pause. End with a concise concept checklist and three common mistakes.

Use course terminology. Ignore old administrative dates in slides. Do not
invent official exam rules, topic weights, solutions, or claims of guaranteed
exam coverage. If a requested concept is not supported by these sources,
say so. Do not expand into later-semester topics except examples already
needed to explain the selected lecture material.

The selected NOTEBOOKLM_FINAL_GUIDE.md supplies instructions only. Use the
selected lecture PDFs and reading PDFs as factual authority. Focus only on
this video; do not summarize the guide or teach its other modules.

Allowed factual sources: data-quality.pdf, automating-and-testing-ml-pipelines.pdf, data-cascades.pdf, ml-test-score.pdf.

TOPICS TO TEACH:
Teach data quality beyond valid types: schema/shape, ranges, uniqueness,
missingness, units, cross-field consistency, label quality, noise, bias, and
representativeness. Clarify that precision in measurement and classification
precision are different uses of the word. Explain schema enforcement versus
semantic validation, including structured LLM output that is valid but wrong.

Distinguish data/covariate drift, concept drift, and schema drift by explaining
exactly what changes. Give one unambiguous example of each and discuss how
to detect/respond, including limits when labels are unavailable.

Trace a data cascade from collection/organizational decisions into downstream
harm. Explain responsibilities and incentives that prevent the cascade.

Decompose a training/serving pipeline into testable components. Contrast data
checks, model evaluation, and infrastructure tests; unit, integration, and
system tests; stubs/mocks and tests with real dependencies. Give a concrete
interface test with known input and expected output. Explain train-serving
skew, flaky/nondeterministic results, regression checks, and failure-path tests
including retries/timeouts/idempotency where supported by the deck.

Explain CI trigger -> environment -> checks -> results -> release decision;
hosted vs self-hosted runner tradeoffs; and testing monitoring itself. Connect
the ML Test Score's data/model/infrastructure/monitoring categories to examples.
```

After viewing, your checkpoint is: **Distinguish three types of drift and give useful data, model, and infrastructure checks.**

### Video 5: Telemetry and production experiments

Checkbox these sources only:
- [ ] NOTEBOOKLM_FINAL_GUIDE.md (this guide)
- [ ] testing-and-experimenting-in-production.pdf

Leave all other sources, including all older exams, unchecked.

Paste this entire prompt:

```text
VIDEO 5: Telemetry and production experiments

Act as a clear, practical TA for CMU Machine Learning in Production. I have
basic ML knowledge but missed some lectures. I am preparing for a midterm
that tests applying concepts to a product scenario. Teach the selected
module using only the selected course sources. Aim for a focused 10-12
minute explanation, but prioritize clarity and the essential distinctions
over forcing a duration.

Build a connected explanation: problem -> concept -> mechanism -> worked
example -> limitation -> how to recognize when to use it. Define jargon
before using it. Use readable diagrams, comparison tables, and simple
calculations where appropriate. Explain why each engineering choice matters.

Use one invented food-ordering assistant as the running teaching example:
it interprets requests, recommends menu items, and can place an order through
an API. Clearly label this example and any numerical assumptions as invented.
Keep examples consistent across this module. Distinguish what a model
predicts from what the software enforces and what happens in the world.

For easily confused concepts, show a correct example and a tempting wrong
example, then explain the difference. Include three brief pause-and-answer
questions. State each question before giving its explanation; invite me to
pause. End with a concise concept checklist and three common mistakes.

Use course terminology. Ignore old administrative dates in slides. Do not
invent official exam rules, topic weights, solutions, or claims of guaranteed
exam coverage. If a requested concept is not supported by these sources,
say so. Do not expand into later-semester topics except examples already
needed to explain the selected lecture material.

The selected NOTEBOOKLM_FINAL_GUIDE.md supplies instructions only. Use the
selected lecture PDFs and reading PDFs as factual authority. Focus only on
this video; do not summarize the guide or teach its other modules.

Allowed factual sources: testing-and-experimenting-in-production.pdf.

TOPICS TO TEACH:
Explain why offline model evaluation cannot establish the whole product's
quality in production. Teach telemetry that measures user outcomes, business
outcomes, model behavior, and service health.

Compare manual labeling, delayed outcomes/wait-and-see, explicit feedback,
and inferred user behavior. For a worked metric show events/fields collected,
identifiers, timestamps, model version, eligible population, denominator,
observation window, computation, missing data, and proxy limitations. Include
two realistic engineering challenges such as joining events, delayed labels,
sampling bias, privacy, or collection overhead.

Compare beta tests, A/B tests, canary releases, shadow execution, and chaos
experiments by purpose, traffic assignment, observations, risk, and rollback.
For A/B tests explain randomization unit, stable assignment, control/treatment,
primary outcome, guardrail measures, and effects of concurrent experiments.

Explain hypotheses, effect size, uncertainty/confidence intervals, statistical
vs practical significance, and p-value interpretation under the null. Explain
why repeated peeking/multiple tests can create false discoveries. Do not claim
a p-value is the probability that the null is true or that a result will replicate.

Finish with a concrete safe rollout and a plan for monitoring and response.
```

After viewing, your checkpoint is: **Specify a telemetry computation, choose an experiment, and interpret statistical evidence correctly.**

### Video 6: Deployment, scaling, and operations

Checkbox these sources only:
- [ ] NOTEBOOKLM_FINAL_GUIDE.md (this guide)
- [ ] deploying-a-model.pdf
- [ ] scaling-the-system.pdf
- [ ] planning-for-operations.pdf
- [ ] how-engineers-operationalize-ml.pdf

Leave all other sources, including all older exams, unchecked.

Paste this entire prompt:

```text
VIDEO 6: Deployment, scaling, and operations

Act as a clear, practical TA for CMU Machine Learning in Production. I have
basic ML knowledge but missed some lectures. I am preparing for a midterm
that tests applying concepts to a product scenario. Teach the selected
module using only the selected course sources. Aim for a focused 10-12
minute explanation, but prioritize clarity and the essential distinctions
over forcing a duration.

Build a connected explanation: problem -> concept -> mechanism -> worked
example -> limitation -> how to recognize when to use it. Define jargon
before using it. Use readable diagrams, comparison tables, and simple
calculations where appropriate. Explain why each engineering choice matters.

Use one invented food-ordering assistant as the running teaching example:
it interprets requests, recommends menu items, and can place an order through
an API. Clearly label this example and any numerical assumptions as invented.
Keep examples consistent across this module. Distinguish what a model
predicts from what the software enforces and what happens in the world.

For easily confused concepts, show a correct example and a tempting wrong
example, then explain the difference. Include three brief pause-and-answer
questions. State each question before giving its explanation; invite me to
pause. End with a concise concept checklist and three common mistakes.

Use course terminology. Ignore old administrative dates in slides. Do not
invent official exam rules, topic weights, solutions, or claims of guaranteed
exam coverage. If a requested concept is not supported by these sources,
say so. Do not expand into later-semester topics except examples already
needed to explain the selected lecture material.

The selected NOTEBOOKLM_FINAL_GUIDE.md supplies instructions only. Use the
selected lecture PDFs and reading PDFs as factual authority. Focus only on
this video; do not summarize the guide or teach its other modules.

Allowed factual sources: deploying-a-model.pdf, scaling-the-system.pdf, planning-for-operations.pdf, how-engineers-operationalize-ml.pdf.

TOPICS TO TEACH:
Teach architectural decisions from requirements: latency, throughput,
availability, cost, bandwidth, privacy, offline operation, hardware, model
size, and update frequency. Compare function/library, separate service,
cloud, on-device, and hybrid inference. Recommend a placement for the running
example while stating the tradeoff accepted. Show training and inference as
different workloads. Explain relevant deployment patterns in the sources.

Compare request/response services, batch, stream, and lambda processing by
workload and freshness needs. Clarify that an uploaded video is not automatically
a stream-processing workload. Explain horizontal scaling, replication,
partitioning, and the reliability/consistency tradeoffs covered in the deck.
Show a simple bandwidth/latency or capacity calculation with explicit units.

Explain containers/images/volumes, configuration management, CI vs CD,
orchestration, staged releases, rollback, and dependency failures at a conceptual
level. Distinguish host health, service health, data health, and model health.
Define operational objectives and describe detection -> diagnosis -> response
for a service that is online but returns harmful predictions.

Connect the operations reading's workflow and velocity/visibility/versioning
to specific engineering choices. Focus on mechanisms and judgment rather than
memorizing vendor names or command syntax.
```

After viewing, your checkpoint is: **Justify model placement and processing architecture, then explain monitoring and recovery.**

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
