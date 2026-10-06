# Fall 2026 first-midterm preparation

Prepared on October 5, 2026. This is TA-style study advice based on public course materials and past papers, not an instructor-issued prediction or official answer key.

**Updated from your local arrangements:** your exam is Friday, October 9, at 5 p.m. Use the [NotebookLM prompt pack](NOTEBOOKLM_PROMPTS.md) to finish concepts by EOD tomorrow, start practice exams the following day, and reserve Thursday for repairs and notes.

Start with the [resource index](study-resources/README.md), which links all 13 local slide PDFs and their original decks. The [exam index](exams/README.md) contains recent papers; [older practice papers](exams/older/README.md) extend the collection back to 2019.

## What is confirmed, and what still needs checking

The [public Fall 2026 schedule](https://mlip-cmu.github.io/f2026/) lists the Pittsburgh first midterm on Thursday, October 8; **your supplied local exam time is Friday, October 9, at 5 p.m., and takes precedence for this plan**. Planning for Operations is scheduled for October 6. Treat the lectures up to that point as the preparation boundary; this is an inference from the schedule, not a separately published topic-by-topic exam scope.

The [official exam instructions](https://github.com/mlip-cmu/f2026/tree/main/exams) specify 80 minutes, no electronics, and notes on letter-size paper. They make class content, readings, and recitation eligible, emphasizing material students have practiced. The second midterm covers later content.

The [Scaling slides, slide 2](study-resources/slides/scaling-the-system.pdf) clarify that the allowance is **six sheets, handwritten or printed, both sides**. They also say a previous-midterm grading rubric was posted on Slack and suggest using `/breakout` to revisit exercise feedback. Get that rubric and your feedback from Slack before grading your practice answers. Those private materials were not accessible during this review.

Use your supplied Friday 5 p.m. local arrangements. Check Slack announcements and Canvas for room details and updates.

Some source material is stale: the Testing in Production deck retains February/Spring-break logistics; the exams README says a second midterm had not previously existed, although we have recent second-midterm papers. Use current announcements and the Fall schedule for logistics. Do not infer this exam's scope from historical administrative slides.

## What the past papers tell us

I inspected the first-midterm papers from Fall 2024, Spring 2025, Fall 2025, and Spring 2026. Their recurring instruction is to answer in the provided scenario. A technically correct generic definition can still miss the question if it ignores that product's users, constraints, or data.

| Practice paper | Main sections and points | Why use it |
| --- | --- | --- |
| [Spring 2026](exams/Midterm%201%20S26%20MLiP.pdf) | Goals/measurement/telemetry 18; testing 16; risk 14; deployment/scaling 10 | Most recent first midterm; includes slicing, property tests, drift classification, a fault tree, and deployment choices |
| [Fall 2025](exams/Midterm%201%20F25.pdf) | Goals/measurement/telemetry 21; testing 18; risk 18 | Strong LLM/agent context; includes p-value interpretation, prompt leakage, behavioral testing, and CI runner tradeoffs |
| [Spring 2025](exams/Midterm%201%20S25.pdf) | Goals/telemetry 15; model/data quality 15; tradeoffs 12; risk 18; process 5 | Additional deployment and requirements practice; process coverage reflects that offering |
| [Fall 2024](exams/Midterm%201%20F24.pdf) | Goals/telemetry 12; model/data quality 14; tradeoffs 11; risk 14; teamwork 4 | Useful teamwork and design questions |

These are historical point allocations, not predicted Fall 2026 weights. Prioritize the first two papers. Keep second-midterm papers and the 2019 final as later supplementary practice: their topic boundaries differ.

When reading a scenario, first identify: the stakeholder, desired real-world outcome, model task, decision/action using the prediction, possible harm, available data, and deployment constraints. Keep this map beside your answers.

## Review map: turn each lecture into something you can do

The order below follows the Fall schedule. The prompts and checkpoints are my study recommendations, grounded in the linked decks. You do not need to memorize every tool name or every illustrative example to practice these skills.

| Lecture and local slides | What to demonstrate without looking it up | Practice checkpoint |
| --- | --- | --- |
| [Introduction](study-resources/slides/introduction-and-motivation.pdf) | Explain the engineering work surrounding a model and the different concerns of data scientists and software engineers | Sketch a product's data, model, interface, deployment, and evaluation path |
| [Correctness and Risk](study-resources/slides/correctness-and-risk.pdf) | Separate correctness guarantees from measured accuracy; distinguish verification and validation; identify likelihood, severity, and residual risk | Explain why a second LLM checking the first cannot by itself guarantee correctness |
| [Goals and Requirements](study-resources/slides/setting-goals-gathering-requirements.pdf) | Distinguish organizational, user, and model goals; operationalize measures; separate world requirements, software specifications, and environmental assumptions | Give one REQ, one SPEC, and one ASM for a new scenario, and explain their connection |
| [Planning for Mistakes](study-resources/slides/planning-for-mistakes.pdf) | Trace stakeholder losses to hazards and causes; use fault-tree AND/OR reasoning; design safeguards outside model improvement; understand the role of human review and recovery | Draw a loss-causing path and revise it to represent a concrete mitigation |
| [Model Quality](study-resources/slides/model-quality.pdf) | Choose metrics and baselines; explain evaluation validity; prevent leakage and repeated-test-set overfitting | Explain why a high overall accuracy could be useless in an imbalanced application |
| [Behavioral Testing](study-resources/slides/behavioral-model-testing.pdf) | Select slices and capabilities; explain the oracle problem; construct meaningful invariants/metamorphic relations; validate automated evaluators | Give one slice, one targeted capability test, and one transformation with an expected output relation |
| [Teams](study-resources/slides/fostering-interdisciplinary-student-teams.pdf) | Diagnose groupthink, social loafing, and communication problems; propose changes connected to their causes | Explain how visible individual responsibilities and early integration address a specific teamwork failure |
| [Testing in Production](study-resources/slides/testing-and-experimenting-in-production.pdf) | Design telemetry when labels are delayed/unavailable; distinguish proxy signals from truth; compare A/B, shadow, canary, and chaos experiments; interpret statistical evidence | Describe assignment, metric, data collection, risk limits, and decision criteria for one experiment |
| [Deployment](study-resources/slides/deploying-a-model.pdf) | Compare cloud, device, and hybrid placement using latency, cost, privacy, bandwidth, offline use, and update constraints | Rank two important qualities, argue both sides, then recommend a placement for that specific product |
| [Pipelines and Testing](study-resources/slides/automating-and-testing-ml-pipelines.pdf) | Separate tests of model behavior, data, and infrastructure; decompose code; test interfaces and failure paths; explain CI and stubs/mocks | Describe a database-to-preprocessor integration test with known input and expected output |
| [Data Quality](study-resources/slides/data-quality.pdf) | Distinguish schema validity from semantic correctness; handle missingness, inconsistent units, labeling issues, and drift; connect organizational choices to downstream failures | Describe a value that passes type checks yet is wrong, and propose an additional check |
| [Scaling](study-resources/slides/scaling-the-system.pdf) | Choose service, batch, stream, or lambda processing from workload needs; explain distribution, replication, and performance tradeoffs | Separate interactive prediction from periodic historical reprocessing and justify each design |
| [Operations](study-resources/slides/planning-for-operations.pdf) | Explain containers, configuration, deployment automation, monitoring, and incident response; choose operational measures and objectives | Describe how to detect, diagnose, and recover from a healthy server serving a broken model |

Planning for Operations is tomorrow's scheduled lecture as of this guide. Its deck is already available. Review it after the lecture too, because live coverage and examples may change.

## Readings and explanations for missed lectures

Use slides for the current examples and vocabulary. When a slide assumes context you missed, read the corresponding textbook section or watch the matching recording, then return to an exercise. The [free textbook](https://mlip-cmu.github.io/book/) has chapters on goals/requirements (5-7), deployment/pipelines/scaling/operations (10-13), model/data/system quality (15, 16, 18), and production experiments (19). Chapter 21 is a useful teamwork supplement; the schedule's teamwork pointer to chapter 15 appears mismatched, so use the current teamwork deck first.

The [Spring 2026 recording playlist](https://www.youtube.com/playlist?list=PLDS2JMJnJzdmubSKnanmIwzr08cionWm_) is linked by the current course site. It is a fallback explanation source, not a recording of the current Fall lectures. I did not watch or verify every video. Search by topic rather than assuming the lecture numbers match.

There are five assigned readings before the exam. Read the introductions, key findings, and examples; be able to apply one implication of each to a product. These summaries are starting points, not replacements for the papers.

| Reading | Main idea to carry into your answers | Self-check |
| --- | --- | --- |
| [Making data science systems work](study-resources/readings/making-data-science-systems-work.pdf); [published source](https://journals.sagepub.com/doi/pdf/10.1177/2053951720939605) | What counts as a working system is negotiated among stakeholders; business goals and model-quality goals can differ | Could a chatbot succeed at collecting leads while failing at answering questions? What would each stakeholder measure? |
| [Who Validates the Validators?](study-resources/readings/who-validates-the-validators.pdf); [author preprint](https://arxiv.org/abs/2404.12272) | LLM evaluators need human validation too; EvalGen uses human judgments to align evaluator implementations. Evaluation criteria can evolve while people inspect outputs | How would you check a judge's agreement with experts, including important failure categories? |
| [The ML Test Score](study-resources/readings/ml-test-score.pdf); [source](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/46555.pdf) | Production readiness involves tests and monitoring across data, models, infrastructure, and operations; a model score alone is insufficient | Give a concrete data check, model check, infrastructure test, and monitoring check for the same system |
| [Data Cascades](study-resources/readings/data-cascades.pdf); [author copy](https://www.shivanikapania.com/assets/chi2021paper.pdf) | Undervalued data work can compound into downstream system failures; data quality depends on incentives, expertise, and collaboration | Trace a collection or labeling problem through training into a user-facing failure, and identify where to intervene |
| [How Engineers Operationalize ML](study-resources/readings/how-engineers-operationalize-ml.pdf); [author preprint](https://arxiv.org/abs/2403.16795) | Engineers combine data preparation, experimentation, staged evaluation/deployment, and monitoring/response. Velocity, visibility, and versioning must be balanced | Explain how faster releases, observable behavior, and traceable versions help recover from a bad deployment |

All five readings are saved together in [study-resources/readings](study-resources/readings/README.md). The SAGE paper was verified and copied from Downloads after the online download failed. Some other copies are author preprints, which can differ from the assigned published editions.

## Answer patterns worth practicing

These are original teaching examples, not official solutions. Use them to make your answers specific and assessable.

### A measure needs a computation and a collection plan

Suppose an AI scheduling assistant books appointments. A user goal is to obtain an appointment that fits their stated availability. A possible measure is the fraction of bookings that the user reschedules within 24 hours because of an availability conflict.

Log booking ID, user ID or appropriate pseudonymous key, model version, creation time, proposed slot, reschedule time, and reason when available. For bookings created in a weekly cohort, wait until each has completed its 24-hour observation window. Divide availability-related reschedules by eligible bookings in that cohort. State how cancellations, missing reasons, and duplicate events are treated.

This is a proxy for a poor schedule, not direct model accuracy: people also reschedule because their plans change. Do not rename a click or acceptance rate as accuracy without explaining the link. When a prompt forbids explicit feedback, use observable behavior and acknowledge its ambiguity.

### Requirements reasoning separates the world from the interface

For the same assistant:

- REQ: appointments should not conflict with the user's actual availability.
- SPEC: the booking service rejects proposed intervals overlapping calendar intervals marked busy.
- ASM: the calendar's busy intervals accurately represent the user's actual commitments.

Even a correct implementation can fail the real-world requirement when the calendar is incomplete. A useful answer explains that causal connection. Writing 'the model works well' as an assumption is too vague to expose the environmental failure.

### A useful test identifies what is under test

For an appointment model, an evaluation slice could be users with overnight shifts. Filter existing labeled examples by that metadata and compare conflict rates with the overall population, reporting sample counts and uncertainty.

A metamorphic test could reorder the same set of busy intervals while keeping their content unchanged. The set of available slots should remain the same. This checks order independence without needing an exact correct slot for every input. Validate that the transformation preserves the relevant semantics.

An infrastructure integration test could use a fixture calendar API returning a known interval, pass it through the actual parser and timezone conversion, and assert that the normalized interval reaching the booking component is correct. That tests the interface; measuring prediction accuracy would test something different.

### A safeguard needs a trigger, action, and remaining failure path

For an assistant allowed to book appointments, a deterministic booking API can enforce that an explicitly prohibited slot is never booked, assuming every booking uses that API and the prohibition is represented correctly. This is a narrowly scoped enforced property, not a guarantee of a conflict-free life.

A human confirmation step can reduce unwanted bookings, but users can overlook errors. In a fault tree, a harmful booking requiring both an incorrect suggestion and acceptance now also requires the review to fail. If review is selective, show the unchecked route too. Do not erase an entire loss path merely because some cases receive review.

### Deployment answers explain why constraints change the choice

An offline scheduling assistant on a phone may favor local inference for availability without connectivity and reduced transmission of sensitive calendar data. A large centrally updated model may favor cloud inference when the phone cannot run it efficiently. Decide from the scenario's constraints and identify the tradeoff accepted by your recommendation.

For performance estimates, state units and assumptions: upload time is approximately payload bits divided by usable bits/second, plus network and service delays. For a steady arrival rate, average in-flight work is approximately arrival rate multiplied by average time in the system. Burst load and tail latency still need separate attention.

## Common distinctions to put on your notes

| Distinction | Check yourself |
| --- | --- |
| Precision vs recall | Precision = TP/(TP+FP); recall = TP/(TP+FN). Define the positive class before discussing which error matters |
| Accuracy vs correctness | A measured proportion of good predictions is not proof that a specified property always holds |
| Data vs concept vs schema drift | Input distribution changes; input-to-target relation changes; encoding/interface changes. State what changed rather than guessing from the presence of errors |
| Slice vs capability vs metamorphic test | A subset of examples; a targeted behavior; an expected relationship after a semantics-appropriate transformation |
| Model vs data vs infrastructure quality | Prediction behavior; input/label validity; code/interfaces that move, transform, train, and serve |
| A/B vs canary vs shadow | Randomized outcome comparison; limited rollout with monitoring; parallel candidate execution whose outputs do not drive user decisions |
| CI vs deployment | Running checks automatically is distinct from releasing their result; a passing workflow is not automatically a safe release |
| Statistical vs practical significance | A small p-value does not establish a large or useful effect. State the effect size, uncertainty, and business consequence |
| Human review vs guarantee | A reviewer may reduce harm, but can be mistaken, overloaded, or influenced by the model |

For a p-value, practice explaining the probability of a result at least as extreme **under the null hypothesis and test assumptions**. It is not the probability that the null hypothesis is true. These formulas and examples are study aids; the course decks provide the intended context.

## Updated plan for your Friday exam

Follow [the NotebookLM plan](NOTEBOOKLM_PROMPTS.md), which reflects your Friday exam and concepts-first preference. The suggested hours below are an adjustable study budget, not course requirements.

| Day | Work | Evidence that you learned it |
| --- | --- | --- |
| Mon Oct 5: about 20 minutes | Upload NotebookLM sources, organize the six modules, request the first videos, and obtain Slack rubric/feedback | Verify that the sources imported successfully |
| Tue Oct 6: about 4-5 focused hours | Complete six concept modules with video/explanation, recall, quizzes, and coverage audit; repair essential gaps | Explain the concepts in new scenarios and keep a concise error log |
| Wed Oct 7 | Attempt Spring 2026 Midterm 1, then Fall 2025 Midterm 1 as time permits. Use 80 minutes per timed paper and additional time for review | Distinguish vague answers, missing mechanisms/computation, misunderstood constraints, and timing issues |
| Thu Oct 8 | Repair weaknesses revealed by papers; use selected Fall 2024 questions for transfer practice; organize permitted notes | Answer new examples without copying source explanations |
| Fri Oct 9, exam at 5 p.m. | Brief review of error log and note index; follow your local arrangements | Bring permitted printed notes and writing materials |

When checking a practice response, ask: Did I answer the requested task? Name a component or stakeholder from the scenario? Describe a feasible mechanism? Specify data and computation if asked? Explain limitations when relevant? Respect constraints such as no extra data collection or no prompt improvement?

Do not award yourself full credit simply because the answer contains the right keyword. The staff rubric is the strongest available grading reference; my checkpoints are diagnostic advice.

## Organizing the six permitted sheets

Build notes from the mistakes you make while answering questions. Leave enough space to find an item quickly; a dense printout of every slide is hard to use under time pressure.

1. Goals and requirements: goal types, measurement template, REQ/SPEC/ASM, stakeholder prompts.
2. Risk: hazard-analysis steps, FTA gates, mitigation examples, review/fallback limits.
3. Evaluation: metrics, baselines, leakage, slicing, capability and metamorphic testing, judge validation.
4. Production experiments: telemetry patterns, labels/proxies, A/B/shadow/canary, p-value interpretation.
5. Deployment and scale: cloud/device tradeoffs, architecture sketch, workload selection, performance units.
6. Pipelines, data, operations, teams, and reading takeaways: test levels, drift, checks, automation, recovery, collaboration.

The six-sheet organization is my suggestion. It is not an already prepared printable note pack. Verify the latest allowance before printing.

## Collection and limits

There are 13 slide PDFs, five reading PDFs, and seven additional historical PDFs. Every collected PDF opens successfully; provenance manifests record hashes. The original 11 exam PDFs remain intact. The Spring 2021 link contains DOCX/ODT versions rather than a PDF; it is not silently converted or counted as downloaded here. [Original Spring 2021 files](https://github.com/ckaestne/seai/tree/S2021/exams).

The public site cannot reveal private Slack/Canvas additions. Lecture text exports can omit diagrams and distort symbols, so use the PDF when studying formulas, code, and fault trees. Readings and decks were reviewed for preparation pointers; this guide does not claim to reproduce every lecture or provide official solved exams.
