---
name: title-heading-story
description: Revise paper titles, section headings, figure titles, and table captions to accurately signal research questions, contributions, and evidence boundaries.
---

# Titles and Headings as a Narrative Map

Follow [PRINCIPLES.md](../PRINCIPLES.md). Titles and headings are navigation aids; they should clarify the paper's argument rather than exaggerate its novelty.

## 1. Write the paper title from the actual contribution

Identify the scientific object, distinguishing contribution, and supported scope. Useful strategies vary by type:
- **Method:** task or problem + core methodological innovation.
- **System:** operating goal + architectural or engineering contribution.
- **Theory:** precise problem class + guarantee or new result.
- **Benchmark/dataset:** evaluated construct + artifact or validation contribution.
- **Empirical/replication:** central question + evidence type, without unsupported universality.

A method acronym may appear when meaningful, but should not consume the entire title. Avoid overly broad claims such as "solves", "universal", "optimal", or "first" without proof or comprehensive evidence.

A question-form title must be answered by the study. A declarative title must be true within the specified population, assumptions, and metric.

## 2. Let sections reveal reasoning, not only topics

The reader should be able to scan headings to infer the path from problem to solution/test to evidence and interpretation. A good heading names the specific responsibility of a section.

Avoid headings that make every method subsection sound like a new contribution merely because it is a named component. Prefer operational labels such as "Constructing the Shared Representation" or "Evaluating Distribution Shift" when accurate.

Use consistent scope and specificity across sibling headings. If "Results" means all evaluated settings, avoid a nearby "Analysis" heading that secretly contains an additional primary result.

## 3. Write figure and table titles carefully

- **Figure caption:** identify what is shown, data/setting if necessary, visual conventions, and the key scientific contrast.
- **Table caption:** identify metric, compared objects, evaluation population/denominator, direction of improvement, and important abbreviations or statistical definitions.
- **Section headings:** organize reasoning, not repeat the full caption or an unsupported headline number.

Distinguish measured quantity from interpretation, effect from association, and a comparison outcome from a mechanism claim.

## 4. Canonical naming and first-use rule

Use the same method, module, metric, benchmark, and condition names as body text. Explain an unfamiliar title term through nearby descriptive words when possible. In captions, expand specialized acronyms and decode symbols because visuals are read independently.

Do not substitute one word for another only to avoid repetition: a controller, routing policy, and selection rule might have genuinely different semantics.

## 5. Pressure tests

Ask whether a heading would remain correct if the most favorable example were removed; whether an evaluator could identify its comparison population; whether the terminology agrees with figures and methods; and whether any conclusion exceeds the actual data.

For each suggested title, explain the implicit claim and evidence needed to defend it.

## Headings as STEM reasoning steps

Check whether scanning titles reveals the actual question → method/proof → discriminating test → interpretation. Avoid headings that claim superiority, statistical equivalence, necessity or a formal proof when the corresponding section only supplies descriptive evidence. Use section names that reflect real scientific work, not software module names alone.

## Required outputs

Provide a title/heading diagnosis, several candidate titles when alternatives are useful, a consistent heading tree, caption wording if requested, and a scope/overclaim audit.

**Acceptance:** The heading hierarchy serves as an accurate mini-map of the paper, and each title promises no more than the content delivers.
