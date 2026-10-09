---
name: introduction-story
description: Restructure an Introduction so that background, genuine research gap, design requirement, method, evidence, and contributions follow a reviewer-comprehensible argument.
---

# Introduction: From Problem to Evidence

Read [PRINCIPLES.md](../PRINCIPLES.md) before editing. Preserve scientific accuracy, verified citations, experimental boundaries, and canonical terms.

## Diagnose before revising
Identify the existing paragraph functions, central question, claimed gap, closest alternatives, actual contribution, available proof or experiment, and unsupported leaps. Mark sentences that sound academic but convey no actionable information. Distinguish conceptual contribution from an implementation example used to test it.

## A flexible dependency chain
**Concrete context → meaningful problem → what prior evidence does and does not show → requirement for a solution/test → proposed contribution → relevant evaluation → supported finding → scope → contributions.**

This is not a mandatory paragraph template. For a theory paper, proof obligations may replace experimental results. For a dataset paper, construction validity and coverage may be central. For an empirical analysis, an evaluation protocol may be the main contribution.

## Paragraph responsibilities
- **Context:** specify the task, real-world or theoretical setting, and the relevant object. Avoid generic "rapid growth" openings.
- **Problem:** state what is not solved or not established; support the claim with appropriately scoped literature and concrete counterexamples.
- **Gap:** identify what a strong existing baseline, earlier theorem, or common evaluation fails to answer. Never equate "different from our approach" with "deficient."
- **Requirement:** derive a property a proposed method or test must satisfy. This bridges problem and method.
- **Method:** give a simple purpose statement and a clear operational description before internal names or formulas.
- **Evidence:** explain *why* the experimental conditions or proof distinguish competing explanations. Highlight results relevant to the opening question.
- **Contributions:** summarize conceptual, practical, and evidential novelty at a higher level than the preceding result descriptions.

A paragraph should leave a question or requirement that the next paragraph actually answers. Audit connections by deleting generic transition words and testing whether the logic still flows.

## First-use and terminology discipline
Introduce every new mechanism, setting, metric, component, and abbreviation with a nearby functional explanation. Use the canonical name from the terminology ledger afterward. Avoid shifting between synonyms for stylistic variety. Use names of datasets and baselines only when they make the scientific claim more concrete; exhaustive lists belong in the evaluation.

Scope results precisely: "the tested performance is recovered" is not "the system is recovered"; "an independent alternative achieves comparable results" is not "a mechanism inside the original system is replaced." These distinctions apply conditionally when the paper actually studies such claims.

## Literature and evidence discipline
Attach citations to exact supported propositions. Do not cite prior literature as if it had already made the paper's novel conceptual argument. Distinguish end-to-end performance, mechanism identification, causal identification, and generalization; one does not automatically establish the others.

Use meaningful numerical evidence, not all seed-level scores. Keep failure cases visible when they change the main conclusion; move secondary qualifications to the appropriate Results or Limitations section rather than hiding them.

## Revision workflow
1. Write the central research question in ordinary language.
2. Map existing paragraphs to their narrative functions; flag duplicates, missing prerequisites, and overly early terminology.
3. Reorder around logical dependencies; add the minimum missing explanation.
4. Ensure the contribution responds directly to the real gap.
5. Audit transitions, numbers, comparison scopes, citations, and canonical terms against other sections.
6. Pressure-test the argument: could a simpler baseline, extra data, alternative mechanism, or changed evaluation protocol explain the headline result?

## Question-first opening and transitions

A useful STEM opening is **observed performance or phenomenon → tempting inference or limitation → why existing evidence does not settle it → direct research question**. Do not attribute an assumption to an entire field without evidence. Read each pair of adjacent paragraphs and check what question the first leaves and how the next answers it. Replace abstract noun chains with concrete questions. Define new models, datasets and technical terms at first use.

## Deliverables and acceptance
Return a story diagnosis, story spine, paragraph-by-paragraph plan, complete revised Introduction if requested, citation-support notes, and a change log. Preserve actual citation keys, quantitative values, LaTeX references, and limitations unless explicitly authorized to change them.

**Acceptance:** The reader understands the scientific question before unfamiliar jargon, and each next paragraph follows naturally from the previous one.
