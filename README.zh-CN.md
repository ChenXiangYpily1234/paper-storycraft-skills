# Paper StoryCraft：科研论文故事线构建 Skills

**以证据为基础，让审稿人顺畅理解研究问题、核心创新与结论边界。**

[English](README.md) | [简体中文](README.zh-CN.md) | [英文总纲领](PRINCIPLES.md) | [英文工作流](WORKFLOW.md)

[![GitHub stars](https://img.shields.io/github/stars/ChenXiangYpily1234/paper-storycraft-skills?style=social)](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/stargazers)
![Skills](https://img.shields.io/badge/Skills-12-blue)
![Core language](https://img.shields.io/badge/Core-English-informational)

一篇论文即便技术上正确，也可能让审稿人看不懂：专业术语提前出现却没有解释，方法章节只是模块清单，图示与正文名称不一致，实验也没有直接回答引言提出的问题。

**Paper StoryCraft** 提供 **12 个独立的 Markdown Skill**，帮助研究者围绕可信的科学证据建立一条完整论证链：

**研究背景 → 具体问题 → 可核验的研究缺口 → 方法或研究设计 → 证据 → 有边界的结论。**

适用于机器学习、自然语言处理、计算机视觉、系统、算法、理论、数据科学、推荐、基准评测、复现研究等计算机与相近技术领域。**不预设特定会议、年份、固定页数或实验数量。**

## 统一原则

- **以审稿人为中心：** 假设读者具备学科基础，但不了解作者内部的概念与命名。新内容必须由已解释的内容自然引出。
- **术语首次出现就近解释：** 新模块、方法名、缩写、指标、变量和符号应在本句或紧邻句中说明“是什么、做什么、必要边界是什么”。摘要和图注也应尽量自包含。
- **全文术语一词一义：** 标题、摘要、引言、相关工作、方法、实验、公式、图示、表格和附录使用一致的规范名称。
- **主张—证据—边界闭环：** 每个重要结论要找到实验、定理或可靠引用支撑，明确竞争解释、假设和适用条件。
- **突出真实贡献，而非自我贬低：** 避免流水账和不必要的道歉式措辞，但不能掩盖关键负结果或影响结论的局限性。

所有 Skill 共同遵守 **[PRINCIPLES.md（英文总纲领）](PRINCIPLES.md)**。

## 快速使用

克隆仓库：

```bash
git clone https://github.com/ChenXiangYpily1234/paper-storycraft-skills.git
cd paper-storycraft-skills
```

让能够读取本地文件的 AI 助手读取相应 Markdown，并提供论文、实验数据、引用文件以及（如有）最新编译的 PDF。**克隆仓库并不等于所有 AI 平台都自动注册 Skill**，具体取决于所用工具。

**推荐的全稿诊断提示词：**

```text
请先读取 PRINCIPLES.md、WORKFLOW.md 和
09-consistency-validation/SKILL.md，随后检查我的真实论文材料。

1. 识别核心研究问题、现有工作的真实缺口和具体贡献。
2. 建立主张—证据—适用边界表，指出证据不充分的部分。
3. 检查每个新术语、缩写、数学符号是否在首次出现处解释。
4. 建立覆盖正文、图表、图注与附录的统一术语台账。
5. 检查实验公平性、竞争性解释以及章节之间的逻辑跳跃。
6. 输出 P0/P1/P2/PASS 审查结果，并明确未完成的核验。

不得编造实验、数据、引用、创新点或未经核实的优越性。
```

**单独修改方法章节：**

```text
请读取 PRINCIPLES.md 和 04-method/SKILL.md，
仅重构我提供的 Method 内容。新概念要在第一次出现时解释；
先交代设计动机，再给运算与公式；依实际数据流组织正文；
保留真实公式、数据、引用、标签和科学结论边界。
最后给出修改稿、统一术语台账和待验证问题。
```

**语言说明：** 核心 Skill 和辅助指南统一采用英文编写，但 AI 生成的论文内容应默认保持原稿语言，不会因为 Skill 是英文就强制把中文论文改成英文。

## 12 个 Skill 一览

| Skill | 用途 |
| --- | --- |
| [01 摘要](01-abstract/SKILL.md) | 清楚传达问题、贡献、证据和结论边界 |
| [02 引言](02-introduction/SKILL.md) | 从研究背景循序渐进推导真正的研究问题 |
| [03 相关工作](03-related-work/SKILL.md) | 公正比较最相近文献与实际创新点 |
| [04 方法](04-method/SKILL.md) | 解释设计动机、定义、公式与真实数据流 |
| [05 实验](05-experiment/SKILL.md) | 设计公平对照、统计推断及证据链 |
| [06 讨论与结论](06-discussion-conclusion/SKILL.md) | 解释发现、局限和实际意义 |
| [07 科研图示](07-figure/SKILL.md) | 让图真正承担科学叙事职责 |
| [08 标题与小标题](08-title-heading/SKILL.md) | 让章节结构成为读者理解的导航 |
| [09 一致性审查](09-consistency-validation/SKILL.md) | 核对事实、引用、数值、术语和图表 |
| [10 LaTeX 表格](10-latex-table/SKILL.md) | 组织清楚、不扭曲统计含义的表格 |
| [11 科研绘图](11-research-plot/SKILL.md) | 根据可核验数据生成可复现结果图 |
| [12 可编辑 PPTX 图示](12-pptx-visual/SKILL.md) | 规划并核验论文中的可编辑图示 |

## 推荐工作流

**全稿诊断 → 引言与相关工作 → 方法 → 实验及图表 → 摘要与标题 → 讨论与结论 → 独立终稿审查。**

具体步骤见 [WORKFLOW.md](WORKFLOW.md)。理论论文、系统论文或纯实证研究可以按实际逻辑调整，不需要机械套用结构。

建议的交付物包括：故事线图谱、主张—证据—边界台账、规范术语台账、首次解释阻塞点、修改稿、图表与正文对应表，以及按严重度分级的审查结果。

## 相关项目与致谢

**推荐参考：** [**anti-defensive-writing-en**](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill/blob/main/skills/anti-defensive-writing-en/SKILL.md)，来自 [Adkid-Zephyr/anti-defensive-writing-Skill](https://github.com/Adkid-Zephyr/anti-defensive-writing-Skill)（上游项目采用 MIT 许可证）。

该项目强调：论文应围绕**真实优势和清晰的研究价值**组织，而不是写成实验流水账或频繁自我否定的工作总结。Paper StoryCraft 与之形成互补，额外强调**不能为了叙事效果隐藏重要负结果、混淆对照或省略会改变科学结论的局限性**。本项目是独立的指南集合，并非该项目的官方分支，也没有直接复制上游 Skill 内容。详细说明见 [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md)。

## 使用边界

- Skill 不能替代真实实验、正式文献核验、人工审稿或最终 PDF 检查。
- 不主动设置会议、年份或固定篇幅限制；明确提供的投稿规范优先。
- 表格示例包含符号占位符，绘图脚本要求输入真实且正确汇总的数据。
- 不捆绑第三方 PPTX 商业软件或不允许再分发的工具文档。
- **本仓库尚未声明统一开源许可证。** 被引用的其他项目拥有自己的独立许可证，不代表本仓库自动获得相同许可。

反馈：[GitHub Issues](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/issues)。
