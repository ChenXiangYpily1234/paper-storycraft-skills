# Paper StoryCraft: copy-ready prompt (English)

Give this prompt and your **actual manuscript excerpt, venue, and evidence** to an assistant able to read files. Load the single relevant Skill when the task requires it; do not load all 13 automatically.

```text
Help me improve the scientific argument rather than merely polishing grammar.

Mode: [audit only / revise supplied paragraphs / linked section rewrite / pre-submission audit]
Section: [abstract / introduction / related work / methods / experiments / discussion / conclusion]
Paper type and audience: [specify; do not assume a Nature submission]
Protected material: [numbers / tables / formulas / figures / LaTeX labels / citations / other]

Identify the research question, real contribution, direct evidence and scope.
Group related work by scientific distinctions, not author chronology. Motivate each
method decision and make experimental comparisons fair and informative.
Foreground supported strengths without needlessly defensive language, but do not
conceal material negative findings or methodological limits.
Verify methods, models, benchmarks and datasets separately. Cite near the named
entity or claim; do not force all citations to sentence endings.

Return only the requested revision and essential verification gaps.
Never claim to have checked a paper, source, PDF or experiment you did not access.
Mark missing evidence or citations unresolved rather than inventing them.
```

Guides: [Principles](../PRINCIPLES.md) · [Editorial playbook](../EDITORIAL_PLAYBOOK.md) · [Citations](../CITATION_GUIDE.md) · [Choose a Skill](../README_EN.md#choose-a-skill)
