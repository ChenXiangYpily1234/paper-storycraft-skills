<div align="center">

# Paper StoryCraft

### 论文故事性打造 · 从研究问题到证据闭环

**让读者看懂：为什么做、怎么做、证据说明了什么。**

A Chinese-language skill collection for evidence-grounded research storytelling.

[![GitHub stars](https://img.shields.io/github/stars/ChenXiangYpily1234/paper-storycraft-skills?style=social)](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/stargazers)
![Skills](https://img.shields.io/badge/Skills-12-blue)
![Language](https://img.shields.io/badge/Guides-中文-orange)

[快速上手](#快速上手) · [使用场景](#从你的问题开始) · [Skills 目录](#12-个-skills一条论文故事线) · [完整工作流](WORKFLOW.md)

</div>

---

实验做完了，论文却还是像一份工作记录：引言没把问题引出来，方法像模块清单，实验堆了很多表，读者依然不知道核心贡献是什么。

**Paper StoryCraft 把论文文字、科研图表和最终审查放进同一条论证链：**

> 研究问题 → 现有缺口 → 设计理由 → 方法 → 验证 → 结论与边界

这套 Skills 帮助你组织已有研究，让摘要、正文、图表和结论共同回答一个清楚的问题。说明文档使用中文；修改英文论文时，术语解释与正文保持英文。

## 从你的问题开始

| 你遇到的问题 | 建议从这里开始 |
|---|---|
| “每段都读得懂，连起来却不知道在讲什么。” | [总纲领](总纲领.md) + [引言](02-introduction-story/SKILL.md) |
| “方法写成了模块说明书，设计动机接不上。” | [方法叙事](04-method-story/SKILL.md) |
| “实验很多，但没有直接回答论文的主张。” | [实验叙事](05-experiment-story/SKILL.md) |
| “图很好看，但读者看不出它想证明什么。” | [科研图示](07-figure-story/SKILL.md) + 对应图表 Skill |
| “摘要和标题很宏大，正文证据却撑不住。” | [摘要](01-abstract-story/SKILL.md) + [标题](08-title-heading-story/SKILL.md) |
| “投稿前想检查术语、数字、图注与主张是否一致。” | [终稿一致性审查](09-consistency-validation/SKILL.md) |

## 快速上手

### 1. 获取仓库

```bash
git clone https://github.com/ChenXiangYpily1234/paper-storycraft-skills.git
cd paper-storycraft-skills
```

### 2. 准备论文材料

让能读取本地文件的 AI 助手访问这个目录，并提供待修改的论文文件。涉及结果或引用时，同时提供相关实验数据、评估协议和参考文献。

本仓库以 Markdown 指南为主。可以让助手按路径读取，也可以将相关文件内容作为上下文提供给它；自动注册 Skill 的方式取决于你使用的工具。

### 3. 复制这个提示词，先做诊断

```text
请先读取 paper-storycraft-skills/总纲领.md、WORKFLOW.md
以及 09-consistency-validation/SKILL.md。

待审查论文：[填写论文路径]
证据材料：[填写结果、评估协议、参考文献等路径；缺少的写明]

先诊断论文故事线，不直接修改文件：
1. 用一段话概括中心问题、方法核心与证据支持的结论。
2. 检查“问题 → 缺口 → 设计 → 方法 → 验证 → 结论”是否连贯。
3. 标出首次出现却未解释的术语，以及正文与图表的命名冲突。
4. 建立主张—证据—边界账本，标出尚未验证的内容。
5. 按优先级列出修改建议，并指出应调用哪些子 Skill。

保留真实数值、公式、引用和实验范围；不要编造贡献或结果。
```

完成诊断后，选择一个最需要修改的部分开始：

```text
请读取 paper-storycraft-skills/总纲领.md
和 04-method-story/SKILL.md，按刚才的诊断重构方法章节。

只修改：[填写目标文件或章节]
保持公式、数值、引用、标签和其他章节不变。
让定义、设计理由与方法步骤按读者能跟上的顺序展开。
最后列出主要修改、仍需证据支持的主张和待确认的问题。
```

> 首次使用建议从一个章节开始，检查改写是否忠实于研究，再按 [完整工作流](WORKFLOW.md) 扩展到全文。

## 一次使用，应该得到什么？

按工作流执行时，交付物包括：

- **故事线图谱**：中心问题是什么，各章节如何推进论证。
- **主张—证据—边界账本**：每个结论由什么材料支持，适用范围是什么。
- **术语台账**：同一概念的标准名称、缩写与首次解释位置。
- **修订稿与修改说明**：说明结构调整如何解决阅读阻塞。
- **图表与正文映射**：每张图、每张表回应哪项主张。
- **终稿检查清单**：按 P0 / P1 / P2 / PASS 标记问题，并注明未验证项。

## 12 个 Skills，一条论文故事线

| Skill | 解决的核心问题 |
|---|---|
| [01 · 摘要](01-abstract-story/SKILL.md) | 在有限篇幅内交代问题、贡献、证据与边界 |
| [02 · 引言](02-introduction-story/SKILL.md) | 让背景、研究缺口与方法动机自然衔接 |
| [03 · 相关工作](03-related-work-story/SKILL.md) | 讲清与最相近工作的实际差异 |
| [04 · 方法](04-method-story/SKILL.md) | 把定义、符号、设计理由和数据流讲明白 |
| [05 · 实验](05-experiment-story/SKILL.md) | 让实验逐项回应主张，检查对照与统计推断 |
| [06 · 讨论与结论](06-discussion-conclusion-story/SKILL.md) | 回答研究意义、适用范围与局限 |
| [07 · 科研图示](07-figure-story/SKILL.md) | 让概念图、结构图和证据图承担清楚的论证职责 |
| [08 · 标题与小标题](08-title-heading-story/SKILL.md) | 用标题、图题和表题准确传达内容 |
| [09 · 一致性审查](09-consistency-validation/SKILL.md) | 核对事实、主张、引用、术语与图表 |
| [10 · LaTeX 表格](10-latex-table-story/SKILL.md) | 组织表格证据、解释缩写并检查排版 |
| [11 · 科研结果图](11-research-plot-story/SKILL.md) | 根据真实数据绘图，附绘图脚本与参考模式 |
| [12 · 可编辑 PPTX 图示](12-pptx-visual-story/SKILL.md) | 规划可编辑图示的叙事、图元语义与交付检查 |

所有子 Skill 以 [总纲领](总纲领.md) 为共同入口：首次出现的术语就近解释，同一概念使用同一名称，论证与真实证据对应。

## 推荐使用顺序

**全稿诊断 → 引言与相关工作 → 方法 → 实验与图表 → 摘要与标题 → 讨论与结论 → 终稿审查**

摘要和标题在主要论证稳定后凝练，更容易准确反映论文内容。具体组合与验收步骤见 [WORKFLOW.md](WORKFLOW.md)。

## 使用边界与公开版范围

- Skills 提供写作与检查流程，不能替代真实实验、文献核验或最终 PDF 阅读检查；没有材料支持的内容应明确标为待验证。
- 示例数据、领域案例与布局参考仅用于说明，不能作为你的论文事实。不得为增强故事性编造数字、负结果、统计显著性或创新点。
- 不预设会议、年份、页数或章节模板，应以目标论文与投稿要求为准。
- 公开版保留 LaTeX 表格与结果图辅助资源，以及 PPTX 叙事指南；未包含许可限制再分发的第三方 PPTX 技术手册和脚本。PPTX 编辑、导出与渲染需自行准备合法可用的工具。
- 本仓库未授予统一开源许可。

## 反馈与支持

如果这套 Skills 帮你理清了论文故事线，欢迎 **Star** 收藏，方便下次写作时找到它，也让更多研究者发现这个项目。

遇到难以解决的叙事问题，欢迎 [提交 Issue](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/issues)。请描述论文类型、使用的 Skill、预期结果与实际问题；示例请使用可以公开的片段。

---

<div align="center">

**把研究讲清楚，让证据撑起故事。**

[开始：阅读总纲领](总纲领.md) · [按流程使用](WORKFLOW.md) · [反馈问题](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/issues)

</div>
