# Paper StoryCraft

**Evidence-grounded storytelling Skills for scientific and technical research papers.**

[简体中文](README.md) | **English** | [Global principles](PRINCIPLES.md) | [Workflow](WORKFLOW.md)

[![GitHub stars](https://img.shields.io/github/stars/ChenXiangYpily1234/paper-storycraft-skills?style=social)](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/stargazers)
![Skills](https://img.shields.io/badge/Skills-12-blue)
![Core language](https://img.shields.io/badge/Core-English-informational)

A technically correct paper may still be difficult to review: concepts appear before explanation, the Method is a component inventory, figures use inconsistent names, and the experiments fail to answer the question promised in the Introduction.

**Paper StoryCraft** provides **12 modular Markdown Skills** treating the manuscript as one verifiable scientific argument:

**Context → research question → demonstrated gap → contribution or test → evidence → qualified conclusion.**

The Skills cover research in machine learning, NLP, computer vision, systems, algorithms, theory, data science, recommendation, benchmarks, replication, and related technical fields. Adapt the narrative to the actual contribution; never force a fixed conference, page limit, number of experiments, or empirical improvement story.

## Guiding principles

- **Reviewer-first comprehension:** explain what a concept is, why it is needed, and how it connects to what came before.
- **Explain at first use:** define unfamiliar terms, module names, acronyms, metrics, and symbols in the same or immediately adjacent sentence. Keep captions and abstracts sufficiently self-contained.
- **One concept, one canonical term:** maintain consistent names throughout title, abstract, sections, equations, figures, tables, and appendices.
- **Claim–evidence–scope alignment:** distinguish verified facts, interpretations, assumptions, and uncertainties. Trace each main claim to direct evidence and meaningful limits.
- **Strong yet accurate framing:** lead with the strongest *genuine* contribution rather than a lab diary or unnecessarily apologetic wording, but do not conceal conflicting findings or invent a favorable comparison.

The normative cross-Skill guidance is in **[PRINCIPLES.md](PRINCIPLES.md)**.

## Quick start

Clone the repository:

```bash
git clone https://github.com/ChenXiangYpily1234/paper-storycraft-skills.git
cd paper-storycraft-skills
```

Ask an AI coding or writing assistant to read the relevant Markdown files. Supply the manuscript, actual results, references, and (if available) the latest compiled PDF. **Cloning alone does not register Skills in every AI platform**; integration depends on the tool.

**Full-paper diagnosis prompt:**

```text
Read PRINCIPLES.md, WORKFLOW.md, and
09-consistency-validation/SKILL.md.

Review my actual manuscript and supplied evidence before rewriting.
1. Identify the central scientific question, gap, contribution, and scope.
2. Map important claims to direct results, theorems, or sources.
3. Find first-use terms, symbols, and acronyms needing local explanations.
4. Produce a canonical terminology ledger across text and visuals.
5. Check experiment validity, major alternatives, and contradictions.
6. Report P0 / P1 / P2 / PASS findings, and list what cannot be verified.

Do not fabricate citations, numerical results, experiments, or novelty.
```

**Targeted Method revision prompt:**

```text
Read PRINCIPLES.md and 04-method/SKILL.md.
Revise only the supplied Method section. Explain every new term
at first meaningful use. Present design rationale before operations
and equations, follow actual inputs to outputs, and retain the
manuscript's verified facts, labels, symbols, and evidence limits.
Return the revision, a terminology ledger, and unresolved checks.
```

**Language behavior:** Core instructions are English, but revised manuscript text should use the manuscript's language unless the user requests translation.

## The 12 Skills

| Skill | Focus |
| --- | --- |
| [01 Abstract](01-abstract/SKILL.md) | Research question, contribution, evidence, and scope |
| [02 Introduction](02-introduction/SKILL.md) | Context, verified gap, motivation, and logical progression |
| [03 Related Work](03-related-work/SKILL.md) | Fair, source-grounded positioning |
| [04 Method](04-method/SKILL.md) | Intuition, definitions, formulas, and data flow |
| [05 Experiments](05-experiment/SKILL.md) | Fair controls, statistical claims, and evidence |
| [06 Discussion & Conclusion](06-discussion-conclusion/SKILL.md) | Meaning, alternatives, boundaries |
| [07 Figures](07-figure/SKILL.md) | Scientific visual argument and captions |
| [08 Titles & Headings](08-title-heading/SKILL.md) | Accurate reader navigation |
| [09 Consistency Validation](09-consistency-validation/SKILL.md) | Scientific, terminology, citation, and artifact auditing |
| [10 LaTeX Tables](10-latex-table/SKILL.md) | Faithful, readable tabular evidence |
| [11 Research Plotting](11-research-plot/SKILL.md) | Reproducible plots from actual results |
| [12 Editable PPTX Visuals](12-pptx-visual/SKILL.md) | Scientifically faithful, editable research diagrams |

Each Skill has its own `SKILL.md` metadata and entry point. Plotting and LaTeX table resources are included as examples, not ready-made scientific findings.

### Recommended order

**Diagnosis → Introduction and Related Work → Method → Experiments and visuals → Abstract and title → Discussion/Conclusion → independent final audit.**

Adapt as needed for theoretical or nonexperimental research. See [WORKFLOW.md](WORKFLOW.md).

### Expected outputs

A review can provide a narrative map, claim–evidence–scope ledger, terminology ledger, definition blockers, a section revision, figure/text mapping, and P0/P1/P2/PASS checks. Only checks actually performed may be marked PASS.

## Related project and acknowledgement

**Recommended complementary reference:** [**anti-defensive-writing-en**](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing-en/SKILL.md) from [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill) (MIT-licensed upstream project).

That project's strength-first, anti-defensive framing is useful for avoiding chronological lab-report writing and unnecessary self-deprecation. **Paper StoryCraft is an independent set of guides, not a copy or an officially affiliated fork.** Its additional guardrail is that *material unfavorable results, valid limitations, and alternative explanations must still be disclosed honestly*. We link to the upstream Skill rather than vendoring its content. For attribution and use boundaries, see [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).

## Scope and limitations

- Does not replace experiments, proper peer review, citation verification, or human PDF inspection.
- Does not impose venue/year/page limits; supplied submission requirements take precedence.
- The sample LaTeX values are **symbolic** and the plotting script expects verified aggregated data.
- Third-party PPTX manuals and proprietary utilities are not bundled.
- **No repository-wide license has been added**; refer to the individual upstream project for its separate license. Listing a referenced project does not grant reuse rights over unrelated files in this repository.

Feedback: [GitHub Issues](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/issues).
