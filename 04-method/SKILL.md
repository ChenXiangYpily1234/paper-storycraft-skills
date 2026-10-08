---
name: method-story
description: Explain formal definitions, design rationale, computations, interfaces, and reproducibility in a method section through a coherent, reviewer-followable data or reasoning flow.
---

# Method: Explain Why, Then How

Read [PRINCIPLES.md](../PRINCIPLES.md) first. Use this Skill for algorithms, mathematical methods, systems, multi-stage pipelines, and theoretical constructions. The objective is **technical reproducibility with conceptual comprehension**, not a list of code modules.

## 1. Plan the reader's dependency path

Before editing, write down: the task and its inputs/outputs; what the current approach cannot establish or achieve; the design requirement; the new operation or proof idea; assumptions; intermediate representations; outputs; and the testable implications.

A useful high-level progression is:

**Problem and constraints → essential definitions → core idea → operational steps → properties/trade-offs → links to evaluation.**

Do not assume every paper needs the same subsections. A short algorithm can combine stages; a theory paper may require assumptions and lemmas before a construction.

## 2. Separate problem definition from construction

**Problem definition:** What objects and variables exist? Which information is available? Which predictions, decisions, or guarantees are sought? What constitutes a valid solution?

**Construction:** Which computations, rules, algorithms, models, or proofs actually produce the desired outputs? What is new, and what is inherited from standard tools?

Transition explicitly: "Under these inputs and constraints, the method must ...; we therefore construct ..." Never imply a guarantee merely by announcing a design intent.

## 3. Define concepts where they become necessary

Introduce a real-world or computational object before abstracting it. At first appearance of each variable, supply meaning, type, dimensionality or domain where relevant, and its role in later expressions. Introduce a mathematical set, distribution, or mapping only if it is used and helps make the method unambiguous.

**Near-first-use rule:** in the same sentence or immediately adjacent sentence, state what the new term does, what it operates on, and how it differs from nearby concepts. A symbol glossary in the appendix does not excuse undefined first use.

Examples of questions a reviewer must not have to guess: Is an index a sample, task, timestep, layer, or trial? Is a matrix learned or fixed? Is a score a probability? Is a limit global or per request? Is a comparison system independent or integrated into the target?

## 4. Organize subsections by scientific responsibility

Good subsection questions: How is the input represented? How is the shared state constructed? How does a decision rule use it? Why is calibration needed? Which objective is optimized? What is the theoretical or statistical guarantee?

Avoid copying software file names into section titles when those file boundaries do not correspond to independent scientific ideas. Merge implementation-only variants; split sections that conflate unrelated assumptions, algorithms, and evaluation protocols.

## 5. Follow actual data and control flow

For each stage, identify: **input → operation → output → consumer → reason**. Explain the central novel transformation in greater depth than standard infrastructure.

If a method has multiple branches, define the common interface and shared information first, then each branch's distinct operation and final aggregation. Mark explicitly whether components share parameters or merely share a diagram symbol.

Respect the actual architecture: iterations, feedback, asynchronous operations, parallel branches, backward passes, and stochastic decisions must not be converted into a fictitious one-way chain. Distinguish data flow from control flow in both text and figures.

## 6. Motivate formulas before displaying them

Each major equation must answer: *What is being defined or computed? Why does the method need it here? How does it connect to existing quantities?* Give a short purpose statement, then the formula, then precise explanations of terms and constraints.

A mathematical expression does not replace an intuition; an intuitive sentence does not replace reproducible mathematics. Use equation numbers when the main text refers back to them, not as decoration.

Check notational hygiene:
- Scalar/vector/matrix conventions, capitalization, units, domains, and shape constraints.
- Subscripts for sample, condition, timestep, task, seed, or model.
- Summation/index bounds, probability conditioning, indicator definitions, and normalization.
- Implicit independence assumptions and how random variables are sampled.
- Reused symbols whose meaning changes between sections.
- Edge cases such as empty inputs, ties, missing data, or zero denominators where material.

## 7. Explain specialized operations only when present

**Routing/gating:** identify the available actions, scoring information, selection rule, and tie handling. Do not call a deterministic procedure an adaptive learned policy unless it is.

**Calibration:** identify the error being corrected, the reference population, fitting data, application time, and scope. Score transformation alone does not establish lack of bias.

**Regularization:** explain which behavior the term penalizes and why the direction of optimization is appropriate. One penalty does not automatically prove several benefits.

**Shared/multi-task modules:** state the shared representation, task-specific decision, loss, and aggregation points. Show which information or parameters transfer across tasks.

**Mechanism comparisons:** clarify what is held constant, what is removed, and whether an alternative system is independent rather than an in-model intervention.

## 8. Keep "why" and "how" distinct

A clear micro-structure is: motivation or needed property → exact definition and operation → explanation of how the property might hold or will be tested. A design hypothesis is not an established property; label theoretical guarantees, empirical observations, and conjectures separately.

Prefer concrete verbs such as compute, estimate, select, constrain, aggregate, update, and verify. Replace inflated words such as "empowers" and "deeply captures" unless the paper supplies an operational definition.

## 9. Separate method from experimental instantiation

The Method should define the algorithm, assumptions, model access, and essential properties. Evaluation should specify dataset versions, actual hyperparameters, baselines, training budgets, statistical tests, and observed outcomes.

When a test protocol is itself the contribution, define its scientific question, statistical unit, comparison object, and decision criterion before introducing dense notation. A non-inferiority test is not an ordinary two-sided difference test; a causal identification claim requires more than a controlled metric comparison.

Disclose access to external data, pretrained representations, or extra compute whenever it changes the scientific interpretation of the method.

## 10. Flexible outlines

- **Algorithm:** task formulation → design insight → component computations → objective/solver → inference → complexity or properties.
- **System:** requirements and constraints → architecture interfaces → request lifecycle → trade-offs → failure handling → measured implications.
- **Theory:** assumptions and notation → statement → key lemmas/construction → proof sketch or full proof → counterexamples and boundaries.
- **Multi-task:** shared inputs → common representation/interface → branch-specific objectives and operations → combination and final output.

Choose only sections justified by the actual study.

## 11. Failure checks

| Failure | Repair |
| --- | --- |
| Readers see a module inventory, not a method | Reorder by task and input-to-output transformation |
| Definitions appear long before they are useful | Move them to first necessity and introduce incrementally |
| Formula lacks a purpose statement | Explain the requirement before the formula |
| Shared and branch-specific parameters are ambiguous | State interface, sharing, and update rules |
| Training settings are mistaken for the method | Separate general algorithm from one experimental instance |
| Too many claimed benefits lack proof or comparison | Reclassify as motivation or hypothesis |
| A diagram shows impossible access or fictional links | Match the source algorithm and resource assumptions |

## Required outputs

Provide (1) problem/design/data-flow map, (2) symbol and definition ledger, (3) section/paragraph reordering plan, (4) revised Method when requested, (5) unverified assumptions and reproducibility gaps, and (6) connections to experiments that would discriminate the main claims.

**Acceptance:** A technically trained reviewer can follow one example input through the described computation or reasoning and independently identify the actual innovation, formal assumptions, and evidence requirements.
