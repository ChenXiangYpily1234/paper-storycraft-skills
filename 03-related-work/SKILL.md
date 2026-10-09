---
name: related-work-story
description: Position a research paper against verifiable closest work, grouping literature by scientific questions and comparison dimensions rather than a citation catalog.
---

# Related Work as Scientific Positioning

Follow [PRINCIPLES.md](../PRINCIPLES.md), especially evidence precision, terminology, and reviewer-first dependencies.

## Purpose and source discipline
The goal is to explain **what is known, which important differences remain, and precisely where this paper fits**. Gather genuine bibliographic records and read primary sources where possible. Do not invent papers, methods, limitations, publication years, or citation keys. Label unverified bibliographic claims.

## Organize by question and mechanism, not just chronology
Useful grouping axes include task definition, available information, modeling or algorithmic principle, supervision, evaluation target, assumptions, computational cost, and deployment constraints. A group must lead to a clear point of comparison; "traditional versus recent" is often too vague.

For theory, organize assumptions, guarantees, problem classes, and known impossibility cases. For systems, organize constraints and architecture trade-offs. For benchmarks, organize construct coverage, collection protocol, and validity. Adapt categories to the actual contribution.

## Identify closest work explicitly
Construct a comparison matrix:

| Closest study | Shared goal | Critical methodological difference | Data/assumption difference | What its evidence shows | What remains unresolved |
| --- | --- | --- | --- | --- | --- |

A claim of novelty must specify **the dimension of novelty**: problem setting, design, objective, evaluation protocol, theorem, or evidence. "Unlike prior work" needs a true comparison, not an assertion. Address strong counterexamples and contemporaneous work fairly.

## Compare at the right evidence level
A previous paper's reported experiment supports the result it measured under its protocol; it does not automatically support all explanations of why it worked. Keep distinctions such as association versus causation, model quality versus mechanism necessity, and implementation change versus method novelty.

Do not say "no work has studied X" unless a sufficiently systematic search justifies it. Safer alternatives specify the precise untested property or mismatch demonstrated by the surveyed literature.

## Paragraph construction
Each paragraph should (1) establish a research category, (2) synthesize representative contributions with verifiable citations, (3) compare the features relevant to the present paper, and (4) lead to the next category or remaining gap. Avoid author-by-author shopping lists that require the reader to infer the scientific meaning.

Introduce unfamiliar technique families with a short description before their labels. Use the terminology ledger so the same comparison object receives the same name in Related Work and Methods.

## Anti-patterns
- Calling every predecessor "limited" without specifying and citing a limitation.
- Cherry-picking weak predecessors while ignoring strong nearby systems.
- Treating different evaluation information or budgets as fair comparisons.
- Conflating older publication date with conceptual inferiority.
- Citing review articles as if they directly prove a narrow method-specific statement.
- Repeating the Introduction verbatim instead of deepening the comparison.

## Position related STEM evidence

Group earlier contributions by what they **establish**: physical measurements, mechanisms, theorem assumptions, computational approaches, simulation accuracy or comparison protocols. Explain the actual difference in questions or evidence rather than listing citations or making a blanket "prior work cannot" claim. A useful progression is existing systems/findings → evaluation or explanation methods → the remaining precise gap.

## Deliverables
Provide a literature grouping plan, a closest-work comparison matrix, revised paragraphs when requested, citation verification gaps, and a novelty-claim risk assessment.

**Acceptance:** A reviewer can identify the closest competing ideas, understand the actual difference, and verify why the new question or contribution is distinct.
