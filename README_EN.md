<div align="center">

# Paper StoryCraft

### Great research deserves a sharper scientific story.

**13 evidence-first STEM writing & review Skills** · Clear contribution · Fair comparisons · Verified sources

[![GitHub Stars](https://img.shields.io/github/stars/ChenXiangYpily1234/paper-storycraft-skills?style=social)](https://github.com/ChenXiangYpily1234/paper-storycraft-skills)
[![Docs CI](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/actions/workflows/skill-quality.yml/badge.svg)](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/actions/workflows/skill-quality.yml)
[![MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

**[⭐ Star this repository](https://github.com/ChenXiangYpily1234/paper-storycraft-skills)** · [Animated examples](#what-changes-in-a-revision) · **[Quick start](#quick-start)** · [Choose a Skill](#choose-a-skill) · [简体中文](README.md)



</div>

---

You may have built a genuine method and run extensive experiments, yet your paper can still read like **background notes, a module inventory, and a list of scores**.

Reviewers need clear answers to three questions: **Why this problem? Why this design? What do these experiments establish?**

Paper StoryCraft gives AI assistants an actionable set of research-writing Skills: **clarify the scientific argument before polishing the prose**, without inventing evidence or hiding relevant limitations.

## What changes in a revision?

Two **animated research maps** show how an argument becomes easier to follow. They illustrate a writing workflow, not measured improvements by an AI model.

### ① Research argument: from module lists to an evidence chain

![Animated example: the Methods section is reorganized around a problem, a design requirement, a concrete operation and a testable claim](assets/demo-argument-en.gif)

**Before:** “We introduce modules A, B and C to improve robustness.”

**Better approach:** Describe the **specific input or task difficulty**, derive a design requirement, explain each module's inputs, operations and outputs, and identify the experiment that could test the proposed mechanism. Do not merely expand each module into a longer paragraph.

### ② Related Work: from paper lists to a mechanism map

![Animated example: six hypothetical studies are grouped into mechanism families and compared by shared dimensions, with an open question marked for verification](assets/demo-related-work-en.gif)

**Before:** “Several distillation approaches have been explored (many citations).”

**Better approach:** Group studies by distinctions relevant to the paper, then compare on **shared axes** (e.g., training-data source, objective, information access, evaluation protocol). Include the strongest prior counterexamples fairly. An open question is **not** automatically a verified gap. Method/model/benchmark/dataset attribution remains governed by [CITATION_GUIDE.md](CITATION_GUIDE.md).

### ③ Experiments: from score announcements to defensible claims

**Before:** “Our method significantly outperforms existing baselines.”

**Better approach:** On **[actual dataset/version]** with **[metric and comparable protocol]**, report **[verified difference and uncertainty]** versus **[baseline]**, then distinguish what the experiment establishes from untested generalization.

> **The GIFs and examples are illustrative**, not genuine experimental findings, verified references or behavioral benchmarks. Actual revisions depend on supplied or independently checked manuscript evidence.

**Want to see whether the rules help your manuscript?** Try the copy-ready prompt on one real paragraph rather than relying on the illustration.

## Why not simply copy Nature-writing or anti-defensive rules?

**Strength first, with accountable supplementary evidence.** Inspired by [nature-skills](https://github.com/Yuan1z0825/nature-skills) and [anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill), Paper StoryCraft keeps the main text centered on what the evidence establishes. **Secondary unfavorable metrics, extra baselines, exploratory analyses and detailed seed results may live in appendices or submitted supplements** rather than dominating the narrative. Results that change the headline conclusion must still be disclosed briefly in the main paper and linked to the full evidence. Never conceal a primary endpoint or silently switch metrics. See [EDITORIAL_PLAYBOOK.md](EDITORIAL_PLAYBOOK.md).

## Quick start

**Fastest path: copy the [English quick-start prompt](prompts/quick-start-en.md)** and supply your manuscript excerpt and actual evidence to your assistant. No installation needed to test the rules. [中文版](prompts/quick-start-zh.md).



**Option A — No install: use the files as guidance.** Give your manuscript excerpt and the linked documents to an assistant that can read the repository; clone locally only if direct GitHub access is unavailable.

~~~bash
git clone https://github.com/ChenXiangYpily1234/paper-storycraft-skills.git
cd paper-storycraft-skills
~~~

Provide your manuscript excerpt and the following prompt to an AI assistant **that can actually read local files or repository URLs**:

~~~text
Read PRINCIPLES.md, CITATION_GUIDE.md and 03-related-work/SKILL.md.
Rewrite my Related Work by grouping verified literature by research question
and technical mechanism instead of listing papers in chronological order.
Compare actual objectives, training data and evaluation conditions.
Cite methods next to their names when that best conveys attribution.
Verify sources for models, benchmarks and datasets separately.
Use only literature I provide or you have independently checked.
List unresolved sources; do not invent BibTeX.
Preserve supported conclusions and existing valid citation keys.
Prioritize the strongest verified contribution; secondary unfavorable detail can be placed in authorized supplements, while claim-changing counterevidence remains disclosed in the main text.
Return the revision and all remaining verification gaps.
~~~

**Option B — Export a Skill collection** for a compatible agent that scans Skill folders:

~~~bash
python scripts/export_skills.py --output ./my-agent-skills
~~~

The script copies the 13 Skill directories **and their shared guides**, keeping cross-file links intact. Configure the output as a Skill search directory **according to your particular agent's documentation**. It does not install anything into accounts or change agent settings. For one-off writing help, Option A avoids the problems of copying a single SKILL.md without its dependencies.

**Migration note:** Skill YAML `name` fields now match their folder names (for example, `05-experiment`) to follow the Agent Skills naming specification. If you previously configured old Skill names directly, update those references; directory paths are unchanged.

### Copyable requests

~~~text
# Audit only — don't rewrite
Read PRINCIPLES.md and 09-consistency-validation/SKILL.md.
Audit the paper's research gap, claim–evidence links, citations,
fairness of comparisons, and consistency. Give section locations and
P0/P1/P2 priorities. Mark unavailable checks NOT CHECKED.
~~~

~~~text
# Experiments
Read 05-experiment/SKILL.md. For each experiment, identify the research
question, comparator, metric, key observation and rival explanations.
Retain actual numbers, uncertainty and limitations; don't narrate tables cell by cell.
~~~

~~~text
# Lossless cross-section edit
Read 13-section-revision/SKILL.md. Rewrite Methods and Experiments as one
scientific argument while preserving every LaTeX table, figure path,
caption, label, equation, citation key and result. Inventory what changed
and separate source/PDF/raw-experiment verification statuses.
~~~

## Choose a Skill

**Do not activate all 13 for every task.** Pick the nearest entry point. Combine only where the work genuinely spans sections.

| Problem | Skill |
| --- | --- |
| Abstract is generic or oversells results | [01 · Abstract](01-abstract/SKILL.md) |
| Introduction never reaches a precise question | [02 · Introduction](02-introduction/SKILL.md) |
| Related Work is a bibliography in prose | [03 · Related Work](03-related-work/SKILL.md) |
| Methods lists modules and formulas without rationale | [04 · Method](04-method/SKILL.md) |
| Experiments fail to link claims, controls and metrics | [05 · Experiments](05-experiment/SKILL.md) |
| Discussion repeats results; conclusion exceeds evidence | [06 · Discussion & Conclusion](06-discussion-conclusion/SKILL.md) |
| Scientific diagram or caption is unclear or misleading | [07 · Figures](07-figure/SKILL.md) |
| Titles and headings promise the wrong contribution | [08 · Titles & Headings](08-title-heading/SKILL.md) |
| Paper needs a submission-readiness integrity audit | [09 · Consistency Audit](09-consistency-validation/SKILL.md) |
| LaTeX table needs accurate scientific formatting | [10 · LaTeX Tables](10-latex-table/SKILL.md) |
| Chart needs authentic data and reproducible source | [11 · Research Plots](11-research-plot/SKILL.md) |
| Diagram must be editable in PowerPoint | [12 · Editable PPTX Diagrams](12-pptx-visual/SKILL.md) |
| Adjacent sections need a coordinated lossless rewrite | [13 · Cross-Section Revision](13-section-revision/SKILL.md) |

An optional revision path is **09 diagnose → 02/03 position → 04/05 build argument → 06 interpret → 01 refresh abstract → 09 verify**. This is an example dependency, **not a mandated section order**. See [WORKFLOW.md](WORKFLOW.md).

## Beyond ordinary proofreading

- **Verify the premise before polishing:** reject unsupported claims rather than giving them more confident wording.
- **Explain and cite named entities near first use:** methods, models, benchmarks and datasets have distinct provenance. Citations do not have to sit at sentence endings; see [CITATION_GUIDE.md](CITATION_GUIDE.md).
- **Treat experiments as inference:** check matched protocols, statistical units, uncertainty and alternatives.
- **Keep review separate from editing:** review-only requests do not authorize modifying source files; lossless LaTeX revisions require an artifact inventory.
- **Separate what was checked:** internal textual consistency, successful PDF compilation and empirical reproducibility are different guarantees.

Global principles: [PRINCIPLES.md](PRINCIPLES.md). Consult [STEM_GUIDE.md](STEM_GUIDE.md), [CITATION_GUIDE.md](CITATION_GUIDE.md), and the [EDITORIAL_PLAYBOOK.md](EDITORIAL_PLAYBOOK.md) only as the task requires.

## Scope and limits

Designed for mathematics, computer science, engineering, physical and life sciences, materials, earth/environmental science and other STEM work. Choose proof, experiment, observation, simulation or system validation standards as appropriate. **No default venue, page limit, section count or experiment count is imposed.**

This is a collection of **Markdown Skills and workflows**, not a hosted literature search, experimental platform or LaTeX service. Whether an assistant can load Skills, search scholarly sources, edit source files, render plots or create an editable PPTX depends on its own tools and permissions. Missing source papers, BibTeX, experiment logs or compilation assets must be reported as unverified.

## Development and validation

~~~bash
python scripts/check_skills.py
~~~

Checks cover **static contracts** such as Skill naming/frontmatter, links, shared documentation and README entry points. See [tests/skill-scenarios.md](tests/skill-scenarios.md) for realistic behavioral scenarios. Passing static checks is **not** evidence of model behavior quality, bibliographic accuracy, experimental reproducibility or rendered PDF correctness.

Design references include [Anthropic Skills](https://github.com/anthropics/skills), [Superpowers](https://github.com/obra/superpowers), and [Academic Writing Skills](https://github.com/WenyuChiou/academic-writing-skills). This project is an independent set of research-writing rules, not an official extension or validated benchmark of those projects.

## Contribute and license

Report incorrect rules, vague procedures and reproducible failure cases via [Issues](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/issues). Do not publish unpublished or confidential research material without permission.

Released under the [MIT License](LICENSE). Independent project acknowledgements: [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md).

**Rewrite the argument, not the facts.**
