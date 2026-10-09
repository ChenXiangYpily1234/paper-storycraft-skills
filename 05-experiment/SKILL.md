---
name: experiment-story
description: Turn experiments into a reproducible chain of questions, controls, findings, competing explanations, and limitations with statistically valid claims.
---

# Experiments as an Evidence-Based Argument

Read [PRINCIPLES.md](../PRINCIPLES.md) first. Use for empirical, numerical and engineering evidence sections in STEM; it is optional for proof-only papers.

## 1. Start from claims, not datasets

Build an evidence matrix **before** reorganizing figures:

| Question/claim | Rival explanation | Needed baseline or control | Metric/statistical unit | Decision criterion | Scope |
| --- | --- | --- | --- | --- | --- |
| Does the proposed change improve the objective? | Gains come from extra data or tuning | Strong, resource-aligned comparator | Relevant task metric | Effect and uncertainty | Tested data and budget |
| Which component contributes? | Effect due to another changed variable | Single-factor ablation if feasible | Metric and cost | Controlled change | Dependency assumptions |
| Does the finding generalize? | Benefit restricted to a subgroup | Cross-domain, scale, or shift evaluation | Appropriate subgroup metric | Variability and consistency | Tested shifts |
| What are operational costs? | Accuracy bought with extra resources | Matched-budget comparison | Latency, memory, throughput, energy | Constraint/Pareto frontier | Hardware/workload |

Select only questions justified by the paper. No fixed number of settings, seeds, charts, or pages is prescribed.

## 2. Explain common settings once, local conditions near each test

Shared protocol: data provenance/version and splits; task definition; primary metric; model access; tuning and runtime budgets; seed policy; statistical test; common implementation. Experiment-specific conditions: candidate pools, access to pretrained representations, adaptation, query/tool budgets, hardware, time windows, data filtering, and failure handling.

Before the first results table, explain what each comparison object is, what information it receives, what it is allowed to do, and why it is appropriate. Define abbreviations in text and make captions independently decodable.

## 3. Verify the actual estimand and metric

State the evaluation unit (sample, user, patient, device, prompt, task, trial, run, seed, or dataset), denominator, aggregation, direction of improvement, filtering/censoring, pairing, and uncertainty procedure.

Do not reuse a convenient formula from a different task without checking it. Accuracy, macro F1, micro F1, Recall@K, NDCG, and retrieval coverage answer different questions. Define new or overloaded metrics locally and consistently.

Separate:
- descriptive means/standard deviations from inferential confidence intervals;
- absolute differences, relative percentage changes, and percentage-point changes;
- independent observations from repeated measures, nested samples, and random seeds;
- failure to reject a difference from formal equivalence or non-inferiority;
- a pre-registered aggregate from the best result chosen post hoc;
- statistical significance from practical importance.

Report statistical units, confidence level, directional or two-sided tests, and multiplicity adjustment where needed. Do not invent p-values, intervals, or missing seeds.

## 4. Controls must discriminate competing explanations

A useful comparison ladder can include a simple baseline, strong contemporary baselines, information/budget-matched controls, targeted ablations, negative controls, and leakage tests. More baselines are not always better; each must serve a scientific role.

Audit **same task, data split, input access, representation priors, pretraining, search space, model capacity, implementation, tuning effort, and training/inference budget**. Where differences are unavoidable, disclose rather than imply full comparability.

If an ablation changes two things, do not assign the outcome to one. If an independent alternative achieves similar performance, do not claim to have removed an internal mechanism from the original model. If a failed test cannot distinguish explanations, the underlying hypothesis remains unresolved.

## 5. Give each experiment subsection a question and answer

Recommended reasoning order:
1. **Question:** What precise claim does this experiment challenge or test?
2. **Setup:** What comparisons and controls make the test informative?
3. **Finding:** What does the primary table or figure actually show?
4. **Interpretation:** What explanation is supported and what alternatives remain?
5. **Boundary:** Where does the result not hold or lack evidence?

Write results around decisive comparisons, not a verbal recitation of every cell. Main figures and tables must be referenced clearly. Numbers in captions, text, abstract, and conclusion must match.

For multi-stage work, explain whether the evidence chain is **validity → attribution → robustness → cost**, **quality → difficulty → generalization**, or another justified sequence.

## 6. Stress-test statistical and experimental validity

Inspect dataset contamination, test-set selection, candidate leakage, label leakage, filtering bias, hyperparameter selection, subgroup cherry-picking, seed variation, representation advantage, inconsistent input context, and repeated-comparison multiplicity.

For systems evaluations, describe hardware, batch/concurrency, warmup, caching, load, throughput or latency statistic, and sampling window. For tool-using systems, disclose tool access, returned information, action budget, and any training/adaptation. These checks apply **only when the study includes the relevant design**.

For non-inferiority or recovery claims, name the margin, estimand, comparator, pairing, unit, and valid one-sided or interval-based decision criterion. Failure to establish recovery is not proof that the original mechanism is necessary.

## 7. Show negative results and limitations without concealment

Distinguish genuinely worse performance, insufficient power, protocol incompatibility, missing observations, and unsupported extrapolation. Robustness is about scientifically meaningful perturbations (randomness, hyperparameters, distribution, input noise, scale, compute budget), not merely adding many tables.

Keep the decisive protocol, controls, core results, and headline limitations in the main narrative. Supplementary materials may contain full hyperparameters, secondary plots, extra metrics, and per-seed data; do not use them to hide qualifications necessary to judge the claim.

## Evidence hierarchy and anti-stacking revision

If several tables and figures are present, create a **one-exhibit / one-primary-question ledger** with exhibit label, comparator, statistical unit, scope, claim supported and main alternative explanation. Sort experiments by inferential role: task-level performance, direct test of the central hypothesis, explanatory/targeted control, robustness/sensitivity, and failure boundary. Use only categories justified by existing experiments—this is not a required subsection count.

For each block write **question → setup/control → primary observation → bounded interpretation → unresolved rival explanation → bridge**. Avoid repeating the same number as a new finding across the main table, audit table and summary. Explain why successive tests are necessary. A component ablation can support a claim about an alternative's behavior without establishing which internal mechanism the original system used.

If two tables share a nominal model configuration, first check whether they share run provenance, seeds, candidate set, experimental unit, and pairing; never merge distinct evidence sources merely because rounded means agree. High binary agreement under low positive coverage may be driven by joint misses: coverage and conditional informativeness matter.

For an explicit **retain all tables and images** constraint, preserve complete floats, labels, captions and numerical entries; reorganize prose and subsection hierarchy instead. Do not move evidence to an appendix without permission. For a full rewrite, apply [13 Cross-Section Revision](../13-section-revision/SKILL.md).


## Progressive experimental storytelling

A strong sequence is **capability → targeted test of the central claim → ablation or explanatory control → robustness → boundary**, when the evidence supports it. Introduce why each next test follows from the previous result. Do not stack unrelated results as a lab log. Describe independent benchmark summaries, paired statistical tests and component repetitions as distinct evidence sources.

For laboratory work validate the instrument, units, replicates and uncertainty; for engineering validate realistic workloads and costs; for numerical work separate solver convergence from physical validation. Proof-only papers need no experimental section. Define experimental labels and metrics locally, and do not overload the main finding with training hyperparameters before presenting it.

## Required outputs

Deliver a claim-to-experiment matrix, fairness/confound audit by severity, revised evidence sequence, revised paragraphs if requested, precisely scoped conclusions, missing-control recommendations explicitly marked as **proposed**, and a figure/table/text consistency check.

**Acceptance:** For every major claim, a reviewer can identify what was compared, under which protocol, at what statistical unit, and why simpler rival explanations are or are not excluded.
