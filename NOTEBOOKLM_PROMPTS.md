# NotebookLM plan: concepts first, practice papers next

For import, use [NOTEBOOKLM_FINAL_GUIDE.md](NOTEBOOKLM_FINAL_GUIDE.md). It combines each video prompt into one ready-to-paste block and supplies exact source checkboxes, including how to use the older exams you already imported. This file remains the earlier planning reference.

Your confirmed exam time: **Friday, October 9, 2026, at 5 p.m.**, as supplied by you. Finish the first concept pass by the end of Tuesday, October 6; start practice papers Wednesday, October 7. Thursday is available for repairing weaknesses and preparing permitted notes.

This pack groups the 13 pre-midterm lecture decks into six modules. It covers the public preparation boundary identified in [MIDTERM_PREP.md](MIDTERM_PREP.md); staff announcements can add or change coverage. The prompts are teaching instructions, not predictions of exam questions.

## A workflow that fits a busy week

Budget **4-5 focused hours** for the concept pass, including setup, quizzes, and repair. This is a time budget, not a guarantee of mastery. Each module gets roughly 30-35 minutes: video, recall, then questions. Use three blocks of two modules, with breaks between blocks.

Today, if possible, spend 20 minutes creating the notebook, uploading sources, and requesting videos. Tomorrow, work through modules 1-6 in order. Generate later modules while working on the first one if the interface and your account permit it. Video generation time, length, and daily limits vary; a requested duration is guidance, not a guaranteed output length. Do not spend study time repeatedly regenerating a polished video. If generation is unavailable or too slow, use the same topic prompt in chat to request an illustrated written explanation, then take the quiz.

After a video, close it and spend two minutes answering: What problem does this concept solve? What could go wrong? How would I apply it to a new product? Then quiz yourself. Maintain only a short error log: concept / mistake / correction / one example.

At the end, run the coverage audit below. A video is an introduction, not evidence that you can apply everything it mentioned. Correct omissions with short source-grounded explanations.

## Source setup

Use one notebook named `MLiP Midterm 1 - Concepts`. Upload the PDF decks in [study-resources/slides](study-resources/slides). All five assigned reading PDFs are together in [study-resources/readings](study-resources/readings/README.md), including the verified paper copied from Downloads. Upload those five PDFs directly.

Check that each imported source contains readable content; a website title or failed import is not the paper. Prefer original lecture PDFs as factual authority. This prompt pack and my guide are study aids, not instructor materials.

For each video and quiz, select only that module's listed sources. Use the topic brief to focus generation. If you cannot scope sources in the available interface, repeat the allowed filenames in the prompt, or create a notebook for that module. Do not add the broad full-course learning-goals document to this first pass: it includes later topics.

Keep the actual exam papers for a separate practice notebook on Wednesday. This lets you encounter their scenarios and questions fresh. You can still learn application through invented teaching scenarios now.

| Module | Lecture PDFs to select | Reading to select |
| --- | --- | --- |
| 1. Product, goals, requirements, teams | `introduction-and-motivation.pdf`; `setting-goals-gathering-requirements.pdf`; `fostering-interdisciplinary-student-teams.pdf` | `making-data-science-systems-work.pdf` |
| 2. Correctness, risk, safeguards | `correctness-and-risk.pdf`; `planning-for-mistakes.pdf` | None required for this module |
| 3. Model evaluation and behavioral tests | `model-quality.pdf`; `behavioral-model-testing.pdf` | `who-validates-the-validators.pdf` |
| 4. Data, pipelines, CI | `data-quality.pdf`; `automating-and-testing-ml-pipelines.pdf` | `data-cascades.pdf`; `ml-test-score.pdf` |
| 5. Telemetry and production experiments | `testing-and-experimenting-in-production.pdf` | None required for this module |
| 6. Deployment, scale, operations | `deploying-a-model.pdf`; `scaling-the-system.pdf`; `planning-for-operations.pdf` | `how-engineers-operationalize-ml.pdf` |

## Shared video prompt

Paste this into the Video Overview customization instructions, followed by ONE module brief below. Choose an explanatory format if available. Do not expect an interactive video; the questions are pause-and-answer opportunities, with interactive follow-up in chat or quizzes.

```text
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

MODULE BRIEF:
```

## Module 1 brief: product, goals, requirements, teams

```text
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

## Module 2 brief: correctness, risk, safeguards

```text
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

## Module 3 brief: model evaluation and behavioral tests

```text
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

## Module 4 brief: data, pipelines, CI

```text
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

## Module 5 brief: telemetry and production experiments

```text
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

## Module 6 brief: deployment, scale, operations

```text
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

## Interactive quiz prompt: use after EVERY module

Use this in notebook chat for one-at-a-time interaction. Replace the module number and paste its brief. This does not require the Studio quiz generator to honor a conversational sequence. If you prefer built-in quizzes, use its topic customization with the same brief, then follow up on wrong answers in chat. Google documents topic/difficulty customization and source-linked explanations: [official feature guide](https://blog.google/innovation-and-ai/models-and-research/google-labs/notebooklm-student-features/).

```text
Act as my interactive TA for Module [NUMBER]. Use only its selected sources
and the module brief below. Give eight questions, ONE AT A TIME, and wait for
my answer before showing an explanation or the next question.

Use five multiple-choice questions with plausible misconception-based options
and three short-answer questions. Test conceptual distinctions, mechanisms,
tradeoffs, and small invented scenarios. Include simple calculations only
where relevant. Include at least one question about each major part of the
brief across this quiz; tell me which parts the eight questions could not test.
Do not reuse actual past-exam questions or claim an official grading rubric.

After each answer: assess correctness, identify the precise misconception,
explain briefly, and cite the source section/slide supporting your feedback.
For short answers assess the mechanism and scenario connection, not just
keywords. If ambiguous, ask one clarifying question before evaluating.
If wrong or unsupported, give a small hint and let me retry once; keep track
of whether the first attempt was correct. Do not reveal later answers.

At the end give: first-attempt results, weak concepts, untested concepts,
and at most three targeted repair tasks. Re-test weak concepts with new
examples. Do not describe this score as a prediction of my exam performance.

MODULE BRIEF:
```

Use roughly 15 minutes per module quiz. A suggested checkpoint is at least 80% of the tested criteria answered independently plus a sensible short-answer explanation. It is a study heuristic; eight questions do not demonstrate mastery of an entire module. If a module is weak, use a five-minute targeted repair now and log it for Thursday rather than restarting its whole video.

## Repair prompt: replace broad rewatching with one focused explanation

```text
I am confused about [CONCEPT OR DISTINCTION]. Use the selected course sources.
Give a clear explanation in at most 300 words: definition, why it matters,
one correct example, one tempting wrong example, and the key distinction.
Use a small diagram/table if it helps. Cite the supporting source. Then give
one new application question and wait for my answer. Do not explain unrelated
topics or give the answer before I try.
```

## End-of-tomorrow coverage audit

Select all 13 lecture decks and the imported assigned readings. Run this in chat. The aim is to expose omissions in generated videos, not trust a claim that a summary covered everything.

```text
Audit my first-midterm conceptual preparation using the 13 pre-midterm lecture
decks and assigned readings. Ignore old administrative dates and later course
topics. Use the six-module briefs below as a checklist, then examine the decks'
learning goals and key concepts for important omissions in those briefs.

Create a compact table: concept -> source/slide or section -> what I must be
able to explain/do -> module. Flag unsupported requests and omitted concepts.
Use source references that actually exist; say when you cannot locate one.
Do not assume a video addressed a concept simply because it was requested.

Then ask 12 mixed questions ONE AT A TIME: one distinction question and one
short application question from each module. Wait for each answer. Track
first-attempt understanding; use source-grounded corrections. Finish with
the five most important unresolved weaknesses and a short Wednesday/Thursday
repair list. State that this is a limited diagnostic, not an official coverage
or mastery certification.

SIX MODULE BRIEFS:
```

Paste the six briefs after that prompt. Allow 25-30 minutes for the audit, using concise answers. If source-grounded omissions appear, add them to the error log and resolve the essential ones before moving to papers.

## Wednesday's handoff to practice papers

Start with Spring 2026 Midterm 1 and then Fall 2025 Midterm 1, as recommended in [the guide](MIDTERM_PREP.md). Fall 2024, currently open in your editor, remains useful additional practice.

Use a separate notebook for the exam PDF and relevant lecture sources. Attempt the paper yourself first under its permitted conditions, before asking for feedback. Request source-grounded criticism of your own answer; distinguish generated feedback from an official solution. Use the staff rubric from Slack when available. Spend Thursday repairing the error log and organizing permitted notes. Friday's final review should be brief.
