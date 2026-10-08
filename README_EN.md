<div align="center">

# Paper StoryCraft

### Help reviewers follow your research—not guess what you mean.

**12 open-source AI Skills · Research narratives · Terminology consistency · Figures & tables · Evidence checks**

[![GitHub Stars](https://img.shields.io/github/stars/ChenXiangYpily1234/paper-storycraft-skills?style=social)](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/stargazers)
[![MIT License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/Research_Skills-12-blue.svg)](#12-skills-one-coherent-workflow)
[![Language](https://img.shields.io/badge/Core_Skills-English-informational.svg)](PRINCIPLES.md)

[简体中文（默认）](README.md) · **English** · [Global principles](PRINCIPLES.md) · [Workflow](WORKFLOW.md)

**[Quick start](#try-it-in-30-seconds) · [Before / after](#what-changes-a-concrete-example) · [Explore the Skills](#12-skills-one-coherent-workflow) · [⭐ Star this repo](https://github.com/ChenXiangYpily1234/paper-storycraft-skills)**

</div>

---

> **A paper is not a lab log—and editing is not only sentence polishing.**
>
> A reviewer needs to understand **why the question matters, what prior evidence cannot establish, why your method is designed this way, and which conclusions the evidence actually supports.**

Does your manuscript have any of these problems?

- The Introduction contains plenty of background but no **precise question or defensible gap**.
- The Method reads like a list of modules instead of an explanation of **why and how the system works**.
- Abbreviations, symbols, and evaluation metrics appear **before being explained**, then change names.
- Experiments and figures accumulate without mapping to **specific scientific claims**.
- The Abstract, main text, captions, and Conclusion **disagree on terminology or evidence scope**.

**Paper StoryCraft** is a collection of **12 Markdown-based research-writing Skills** that can guide an AI writing or coding assistant through scientific narrative diagnosis and revision. It does not generate new research or magically guarantee acceptance. Its purpose is to make an existing scientific argument **easier to follow, verify, and critique**.

**One argument:** Context → question → demonstrated gap → design rationale → method or test → evidence → qualified conclusion.

Useful for ML, NLP, CV, recommender systems, systems, algorithms, theory, benchmarks, datasets, replication, and adjacent technical fields. **No built-in conference, page-limit, or experiment-count assumptions.**

## What changes? A concrete example

The following examples are **illustrative**, not actual experimental findings.

| Common draft | Reviewer-first revision |
| --- | --- |
| “We propose MAF and achieve significant improvements.” | “Because input sources may differ in reliability, fixed fusion weights may not suit every example. We therefore use **multi-stage adaptive fusion (MAF)**: the procedure estimates the reliability of each input source and uses the estimates to adjust fusion weights. Its effect must be tested in controlled comparisons.” |
| “Experiments prove our method is better.” | State the **actual data, metric, comparator, uncertainty, and resource budget** before interpreting what the evidence establishes. |
| “Router” in a diagram, “Controller” in the text, “Policy” in a table. | Use one **canonical term** if these refer to the same concept; otherwise explain the real difference at first use. |

**The aim is clarity and defensible framing—not bigger claims.**

## Try it in 30 seconds

There is **no extra program required to read the guides**. If your assistant can access repository files, point it to the relevant Markdown. Otherwise, download or clone the repository and supply the files as context.

**1. Get the repository**

```bash
git clone https://github.com/ChenXiangYpily1234/paper-storycraft-skills.git
cd paper-storycraft-skills
```

**2. Copy this prompt for a diagnostic pass**

```text
Read paper-storycraft-skills/PRINCIPLES.md,
paper-storycraft-skills/WORKFLOW.md, and
paper-storycraft-skills/09-consistency-validation/SKILL.md.

Review the manuscript and evidence I provide:
1. State the actual research question, contribution, and supported conclusion.
2. Identify logical jumps, unsupported research gaps, and broken transitions.
3. Flag technical terms, symbols, and acronyms not explained near first use.
4. Create a canonical terminology ledger including figures and captions.
5. Map major claims to evidence, assumptions, and alternative explanations.
6. Provide location-specific P0/P1/P2/PASS findings.

Diagnose before rewriting. Do not invent references, experiments,
numbers, results, or novelty.
```

**3. Apply the relevant Skill**

For example, revise only the Introduction:

```text
Read paper-storycraft-skills/PRINCIPLES.md and
paper-storycraft-skills/02-introduction/SKILL.md.
Revise the Introduction so its question, gap, method motivation,
and evidence form a logical sequence. Explain unfamiliar terms at
first use and preserve actual results, citations, and limitations.
```

> These are **Markdown guides, not a universally auto-installing plugin**. Your assistant must be able to read their contents. The core guides are in English, but revised manuscript text should retain the manuscript's original language unless translation is requested.

## 12 Skills, one coherent workflow

| Area | Skill | What it addresses |
| --- | --- | --- |
| Narrative | [01 Abstract](01-abstract/SKILL.md) | Concise, evidence-aligned research story |
| Narrative | [02 Introduction](02-introduction/SKILL.md) | Concrete problem, justified gap, and motivation |
| Narrative | [03 Related Work](03-related-work/SKILL.md) | Fair closest-work comparison, not citation dumping |
| Narrative | [04 Method](04-method/SKILL.md) | Definitions, rationale, formulas, real data flow |
| Narrative | [05 Experiments](05-experiment/SKILL.md) | Claim-led comparisons, controls, valid interpretation |
| Narrative | [06 Discussion & Conclusion](06-discussion-conclusion/SKILL.md) | Meaning, competing explanations, and boundaries |
| Visuals | [07 Figures](07-figure/SKILL.md) | Diagrams that advance a scientific argument |
| Structure | [08 Titles & Headings](08-title-heading/SKILL.md) | Accurate reader navigation |
| Audit | [09 Consistency Validation](09-consistency-validation/SKILL.md) | Claims, citations, statistics, terminology |
| Tables | [10 LaTeX Tables](10-latex-table/SKILL.md) | Readable, statistically faithful evidence tables |
| Plots | [11 Research Plotting](11-research-plot/SKILL.md) | Reproducible figures from verified data |
| Diagrams | [12 Editable PPTX Visuals](12-pptx-visual/SKILL.md) | Editable visuals aligned with the manuscript |

### One global standard

[**PRINCIPLES.md**](PRINCIPLES.md) governs the 12 Skills:

1. **Reviewer-first:** explain the problem before the unfamiliar terminology.
2. **First-use definitions:** describe every new term, acronym, metric, and symbol in the same or immediately adjacent sentence.
3. **Canonical vocabulary:** use consistent names across title, abstract, text, equations, figures, tables, and appendices.
4. **Evidence-bound claims:** link claims to direct evidence, explicit assumptions, and meaningful alternative explanations.
5. **Strong but honest framing:** highlight genuine contributions without hiding material negative results.

## Where should I start?

| You are facing… | Start here |
| --- | --- |
| A readable but disconnected manuscript | [Global principles](PRINCIPLES.md) + [Introduction](02-introduction/SKILL.md) |
| Method details hide the actual innovation | [Method](04-method/SKILL.md) + [Headings](08-title-heading/SKILL.md) |
| Results do not test the headline claim | [Experiments](05-experiment/SKILL.md) + [Validation](09-consistency-validation/SKILL.md) |
| Attractive figures that fail to explain the work | [Figures](07-figure/SKILL.md) + [Plotting](11-research-plot/SKILL.md) |
| A full paper needing a reviewer-style audit | [Consistency Validation](09-consistency-validation/SKILL.md) |

Typical sequence: **Diagnose → Introduction/Related Work → Method → Experiments/visuals → Abstract/title → Discussion/Conclusion → final independent audit.** Adapt it to the paper type; see [WORKFLOW.md](WORKFLOW.md).

Useful outputs to request include a narrative map, claim–evidence–scope ledger, canonical terminology ledger, revised sections, reviewer questions, and P0/P1/P2/PASS findings. Never mark an unperformed verification as PASS.

## Found this useful? Consider starring the repository

A **Star** makes it easier to find the project later and helps other researchers discover these research-writing guides.

[**⭐ Star Paper StoryCraft**](https://github.com/ChenXiangYpily1234/paper-storycraft-skills) · [Suggest an improvement](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/issues)

Issues and contributions are welcome—especially domain-specific pitfalls, reproducible formatting problems, and new evidence-aware writing checks. Share public examples only; please do not post confidential manuscripts or private data.

## Related project and acknowledgement

[**anti-defensive-writing-en**](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing-en/SKILL.md), from [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill), is a complementary reference for emphasizing real strengths without turning the manuscript into a chronological lab report. Paper StoryCraft is independent and additionally insists on disclosing material negative evidence and limitations. Upstream content is not copied here. See [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).

## Scope and license

These guides do not replace actual experiments, source verification, human peer review, or rendered PDF inspection. Placeholder examples are not scientific results; plotting and table tools require verified underlying data. Proprietary PPTX tools are not included.

Original repository content is licensed under the **[MIT License](LICENSE)** (Copyright © 2026 ChenXiangYpily1234). Linked third-party projects retain their own licenses.

---

<div align="center">

**Make your research understandable. Make every claim defensible.**

[中文 README](README.md) · [Global principles](PRINCIPLES.md) · [Workflow](WORKFLOW.md)

</div>
