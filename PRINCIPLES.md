# Paper StoryCraft: Global Principles

> **Scope:** Science, technology, engineering and mathematics (STEM) research, including natural sciences, mathematics, engineering, computing, numerical modeling and technical interdisciplinary studies. See [STEM_GUIDE.md](STEM_GUIDE.md).
>
> **Non-negotiable rule:** Storytelling must clarify the evidence, never manufacture a gap, result, contribution, causal mechanism, or guarantee.

This document governs every `SKILL.md`, workflow, figure, table, and supporting guide in this repository. A reviewer should be able to read the paper in order, understand each newly introduced concept where it appears, and trace every important claim to evidence.

## 1. Priority order

When recommendations conflict, apply the following order:

1. **Scientific correctness:** measurements, data, results, proofs, assumptions, units, citations and study protocols relevant to the STEM field.
2. **Explicit author and venue requirements:** follow actual provided requirements; impose no default conference, year, template, or page limit.
3. **First-pass reviewer comprehension:** no unexplained names, symbols, hidden assumptions, or missing transitions.
4. **Cross-document semantic consistency:** one canonical term for each concept and one clear meaning for each term.
5. **Conciseness and presentation:** improve polish only if the higher priorities remain intact.

A readable paper need not follow one fixed section count, number of experiments, or narrative template.

## 2. Follow the reviewer, not the author's internal implementation

Assume a technically competent reviewer who has **not** participated in the project. At every transition, the reviewer should be able to answer:

- **What is being studied?** Task, object, inputs, outputs, and environment.
- **Why is it a research problem?** Which limitation or unanswered question is demonstrated, rather than merely asserted?
- **What is contributed?** A method, proof, design, instrument, measurement, model, test or finding, and how it differs from the closest alternatives.
- **What directly supports the claim?** Relevant proofs, baselines, calibrated measurements, assumptions, simulations, design tests and competing explanations.
- **What does the evidence permit us to conclude?** Conditions, uncertainty, failure cases, and limits of generalization.

A **reader blocker** occurs whenever the next sentence, equation, arrow, or figure label requires guessing a definition, searching ahead for a necessary explanation, or inferring an unstated comparison. Repair the blocker at the point of use, not with an after-the-fact explanation elsewhere.

## 3. Construct a traceable argument, not an artificial success story

A useful default reasoning chain is:

**Context and object → precise research question → verified gap → design requirement → contribution or test → evidence → interpretation → scope.**

This is a *logical dependency*, not a compulsory paragraph template. Adapt it:

| Paper type | Natural argument | Failure mode to avoid |
| --- | --- | --- |
| Method or algorithm | task bottleneck → design constraint → mechanism → controlled test | presenting modules before the problem |
| Systems | operational need → constraints → design trade-off → measured performance and cost | reporting throughput without workload or hardware |
| Theory | formal question and assumptions → proposition → proof/counterexample → implication | silently changing quantifiers or assumptions |
| Dataset or benchmark | measurement gap → construction → validation → bias and use limits | equating data volume with validity |
| Empirical, replication, negative result | testable claim → discriminating protocol → observations → alternative explanations | mistaking non-significance for equivalence |
| Mechanism or causal study | competing explanations → controlled intervention → result → identification limits | declaring a mechanism necessary from failure to find an alternative |
| Laboratory and field science | measured phenomenon → experiment or observation → analysis → interpretation → limits | describing association as a proven mechanism |
| Numerical science | model assumptions → discretization → solver → convergence/verification → validation | confusing converged simulation with real-world validation |
| Engineering | requirement → constraints → design choice → operational test → failure regime | presenting an architecture without its rationale |

If the results do not support the original narrative, **revise the claim or question**. Do not hide contradictory evidence.

### STEM-specific evidence standards

First identify whether the principal support is a **proof, calibrated observation, experiment, simulation, benchmark, system validation or their justified combination**. Proof-only work does not require p-values, and numerical convergence does not alone establish physical validity. Do not impose one STEM subfield's methods on another. For all work, connect the strongest claim to its specific evidence and scope. See [STEM_GUIDE.md](STEM_GUIDE.md).

## 4. Explain a new concept at its first meaningful appearance

A new term includes author-invented names, specialized uses of ordinary words, modules, abbreviations, metrics, evaluation settings, symbols, mathematical objects, diagram labels, and protocol names.

**Local-definition rule:** in the same sentence, the immediately preceding sentence, or the immediately following sentence, explain enough for the reader to continue. At minimum, indicate:

1. **Type:** object, operation, parameter, assumption, metric, algorithm, or evaluation condition.
2. **Purpose:** what it does, measures, or constrains.
3. **Distinction:** how it differs from likely confusions when relevant.
4. **Scope:** inputs, outputs, units, availability, or assumptions when they affect the claim.

Preferred progression: **intuitive need → plain-language definition → canonical name → operational/formal detail**.

Bad: "We apply RCM to the outputs." The reader cannot tell whether RCM is a model, metric, or procedure.

Better: "To correct shifts in prediction scores across batches, we apply a validation-fitted score calibration step, which we call RCM. RCM transforms each score before the final decision rule." This is an illustrative example, **not a reported result**.

Do not introduce an unexplained acronym with a promise to define it several sections later. Abstracts, captions, and tables are frequently read independently: re-expand an abbreviation there if self-containment requires it, keeping the same definition.

For equations, state what is being computed and why; define variables, dimensions, indices, and constraints near the first display. For plots, decode axes, units, populations, uncertainty displays, and new labels in the figure or caption.

## 5. Maintain a canonical terminology ledger

Create and maintain a cross-paper ledger:

| Concept ID | Canonical term | One-sentence meaning | First definition | Allowed abbreviation | Confusable terms | Figures/tables/symbols |
| --- | --- | --- | --- | --- | --- | --- |
| C01 | [single term] | [precise role] | [location] | [if useful] | [terms to distinguish] | [locations] |

Apply it to title, abstract, introduction, related work, method, experiments, discussion, figures, captions, tables, equations, appendices, and supplements.

- **One concept → one default name.** Do not rotate `controller`, `coordinator`, and `agent` merely for stylistic variety if they name one object.
- **Different concepts → different names.** A metric, objective, loss, score, and decision policy are not automatically synonyms.
- Match capitalization, pluralization, method names, symbol formatting, and unit conventions.
- If a technical term appears independently in a caption or abstract, its short local definition must remain semantically identical.
- Track actual changes: text-only renaming is incomplete if diagrams and table headers still use old names.

## 6. Keep a claim–evidence–scope ledger

| Claim | First occurrence | Direct evidence | Competing explanation | Scope/assumptions | Status |
| --- | --- | --- | --- | --- | --- |
| [actual claim] | [location] | [theorem, result, figure, or source] | [confound] | [data, budget, regime] | verified / unresolved / unsupported |

Label material as **verified fact**, **evidence-supported interpretation**, **unverified hypothesis**, or **prediction**. A citation must support the *specific* attached claim. A successful controlled result does not prove universal necessity or optimality; failure to reject a null hypothesis does not establish equivalence.

Before asserting causality, ask whether intervention, identification assumptions, and controls rule out rival explanations. Before asserting superiority, check information access, training data, tuning budget, seeds, and uncertainty.

## 7. Use paragraph-level information dependencies

Give each paragraph one main argumentative job. End a paragraph with a concrete unresolved question or requirement, and begin the next with the corresponding answer or design step. Transitions should remain logical even if words such as "however", "moreover", and "therefore" are removed.

Preserve important negative results; remove redundant restatements, not necessary qualifications. A contribution list should summarize *what is new, what was actually done, and why it matters*, not repeat a results table.

## 8. Make visuals part of the same argument

Before making a visual, write its scientific purpose in one sentence. Check that every panel, arrow, legend mark, symbol, model, and numerical label has a verifiable meaning. Distinguish data flow, control flow, logical dependence, and causal inference. Never use a causal arrow for mere association.

Match diagram terms to the terminology ledger and quantitative displays to the underlying data and statistical unit. Check final manuscript reading size, grayscale legibility, accessible encodings, and caption self-containment.

## 9. Guard the strength of claims

- **Correlation is not causation.** State which relation is actually supported.
- **Failure to demonstrate an effect is not proof of no effect.** Equivalence and non-inferiority require appropriate designs.
- **Recovering performance is not recovering a model.** An independent substitute is not necessarily a component replacement.
- **One benchmark does not prove universal generalization.** State sampling and deployment boundaries.
- **Ablating multiple components is not a single-variable causal test.**
- **A significant p-value is not an effect-size or practical-significance guarantee.**
- **A strong story cannot compensate for missing essential controls.**

### Evidence-to-narrative continuity checks

Read the paper in order: Does the opening clearly show *why this specific question arises*? Does Related Work explain what earlier evidence does and does not establish? Are formulas, proof steps and modules motivated before introduction? Does each next experiment answer a question arising from the prior comparison? Do Results, Discussion and Conclusion perform different functions—**observation, interpretation, direct answer**? Define every newly introduced technical term near first use rather than in a distant appendix.

## 10. Reviewer read-through and acceptance gates

Read the final manuscript **in its actual order**, with no privileged knowledge of the project. Inspect the rendered PDF if available; source-only validation is insufficient for layout claims.

**P0 — Blockers:** factual contradiction, fabricated/unsupported evidence, wrong units, incorrect citation, invalid statistical inference, unresolved first-use definition that changes understanding.

**P1 — Major:** broken problem→method→evidence connection, unfair or underspecified comparisons, inconsistent central terminology, misleading figure/caption.

**P2 — Polish:** local redundancy, navigation, typography, optional shortening.

**PASS — Verified:** report the exact files or evidence checked; never report a check as passed unless performed.

## 11. Standard deliverables

Unless the user narrows the task, provide:

1. A one-paragraph narrative diagnosis and an explicit argument map.
2. The claim–evidence–scope ledger.
3. The terminology ledger and first-use blockers.
4. A revision plan by paragraph or section.
5. Revised content in the manuscript's language, preserving real values, citations, labels, and claims.
6. A figure/table-to-text consistency mapping where relevant.
7. A P0/P1/P2/PASS report with unresolved verifications.

**Final test:** Can a reviewer unfamiliar with the project follow why each new concept appears, what it means, and how the evidence justifies the final claim without guessing?

## 12. Source-preserving revision contract

When the user asks for clearer writing **without removing existing material**, the default is to preserve complete figures and tables (including values, captions, labels and file paths), mathematical statements, assumptions, citations, reported numbers and statistical qualifications. Structural editing does **not** authorize inventing a better-looking result or strengthening causal language.

Before and after revision, inventory and compare exhibits and math, references, numbers and qualifiers, plus the section-to-section argument. Document authorized changes and unresolved conflicts. **Internal numerical consistency, experimental reproducibility and final-PDF correctness are different checks**; report each separately.

For linked framework, method and experimental rewrites, follow [13 Cross-Section Revision](13-section-revision/SKILL.md).
