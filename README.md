<div align="center">

# Paper StoryCraft

### 你的科研有内容，论文却讲不清重点？

**把研究问题、方法设计、实验结果和参考文献，组织成审稿人能追踪的科学论证。**

13 个可组合的 STEM 论文 Skills · 不只是润色英文 · 不编造实验与引用

[**⭐ Star 本项目**](https://github.com/ChenXiangYpily1234/paper-storycraft-skills) · [**⚡ 3 分钟试用**](#3-分钟上手) · [**🎬 看动态示例**](#改写前后有什么不同) · [English](README_EN.md)

[![Skill documentation validation](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/actions/workflows/skill-quality.yml/badge.svg)](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/actions/workflows/skill-quality.yml) [![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)

</div>

---

**你的论文可能并不缺实验，而是缺少清晰的论证路径。** 模块堆得很多，却不知道为什么需要；Related Work 引用了几十篇，仍看不出差别；结果表格很满，却说不清哪条 claim 被真正验证。

Paper StoryCraft 给 AI 助手一套可执行的**写作、重构与审查规则**：先查前提，再组织表达；让方法解释设计原因，让实验对应具体主张，让模型、benchmark、数据集都有可核验的出处。

**觉得有用？[点一个 Star](https://github.com/ChenXiangYpily1234/paper-storycraft-skills)，以后写论文、改 rebuttal 或投稿前检查时可以直接找回来。**

## 改写前后有什么不同？

### 动图 ①：从“堆砌模块和结果”到“问题—设计—证据—边界”

![动态演示：左侧是空泛的模块描述和结论，右侧依次出现研究问题、方法设计、验证证据、适用边界四步](assets/demo-argument-zh.gif)

**原稿的问题不是不够华丽，而是缺少验证链条。** 动图逐步展示四个必要信息槽；其中的方括号是**待真实研究填写的占位符**，不是实验结果。静态版：原句“我们提出 A、B、C，性能更好” → 修改时需解释“针对什么问题、为何需要 A→B→C、用什么对照验证、结论适用于哪里”。

### 动图 ②：方法、模型、数据集的引用应该放在哪里？

![动态演示：引用分别紧跟方法 A、模型 B、数据集 C 的名称，而非堆在整句话末尾](assets/demo-citation-zh.gif)

方法、模型和数据集可以在**首次有意义地提及时紧跟各自的文献**；如果报告具体性能结论，还需引用真正支持该结论的来源。示意中的“方法来源”等文字**不是实际参考文献**。完整标准见 [CITATION_GUIDE.md](CITATION_GUIDE.md)。

### 它和普通语言润色的区别

| 你遇到的情况 | Paper StoryCraft 的处理方式 |
| --- | --- |
| “现有方法都存在明显局限”但没有证据 | 先核查最相关研究，再限定**能够验证的 gap**；不替你捏造创新点 |
| Methods 逐个介绍 A、B、C，却没有逻辑 | 补齐**为什么需要 → 输入 → 操作 → 输出 → 下游用途** |
| 实验写成“每张表都更好” | 对齐**claim → baseline → 数据/预算 → 指标 → 结果 → 替代解释** |
| 引用集中在句末、漏掉 benchmark | 对方法、模型、benchmark、数据集分别溯源；找不到来源就标为待核实 |

> **示例只演示写作结构，不宣称任何真实论文取得了这些效果。** 不提供数据或原文时，这套 Skill 也不能凭空证明新方法更优。

**想马上试效果？** 跳到 [3 分钟上手](#3-分钟上手)，把自己的一个 Related Work 段落交给它。

## 3 分钟上手

**方式 A：直接用仓库文档指导现有 AI 助手**。适合只想改一节论文、无需安装 Skill 的情况。

~~~bash
git clone https://github.com/ChenXiangYpily1234/paper-storycraft-skills.git
cd paper-storycraft-skills
~~~

将论文片段与下面的指令一起交给**能读取本地文件或仓库链接**的 AI 助手：

~~~text
阅读 PRINCIPLES.md、CITATION_GUIDE.md 和 03-related-work/SKILL.md。
请重构我提供的 Related Work：先找最相关工作，再按研究问题和技术机制组织，
比较各方法真实的训练数据、目标和评估条件。方法名出现时可以紧跟引用，
不要机械地把所有文献放句末。模型、benchmark、数据集分别核验来源。
只使用我提供或你确实核实过的文献；缺失来源列清单，不得编造 BibTeX。
保留原始科学结论与已有引用键，输出修改稿和仍需核查的部分。
~~~

**方式 B：把 13 个目录导出为可扫描的 Skills 集合**，适合支持 Agent Skills 文件夹加载的工具：

~~~bash
python scripts/export_skills.py --output ./my-agent-skills
~~~

脚本会复制 13 个 Skill 目录及其公共指南，保留原有相对引用；之后根据**你所使用工具的官方文档**，把生成的目录配置为 Skill 搜索路径。**它不会自动安装到 ChatGPT、Claude 或任何账户，也不会修改其他工具设置。** 若只打算使用一个 Skill，推荐方式 A，避免单独复制后丢失公共指南。

**兼容性提示：** 本次将各 Skill 的 YAML `name` 调整为与目录一致（例如 `05-experiment`），以符合 Agent Skills 的命名规范。若你的工具曾通过旧名称硬编码调用 Skill，请更新名称；原有目录链接保持不变。

### 可以直接复制的任务示例

~~~text
# 先诊断，不重写
阅读 PRINCIPLES.md 和 09-consistency-validation/SKILL.md。
检查这篇论文的 gap、claim–evidence 关系、引用与实验公平性；
按 P0/P1/P2 给出精确位置和修改建议。未经验证的项目标记 NOT CHECKED。
~~~

~~~text
# 实验写作
阅读 05-experiment/SKILL.md。
不要罗列每张表格：为每组实验指出研究问题、对照、指标、主要观察、
可排除和不可排除的解释。保留全部真实数值与统计限定。
~~~

~~~text
# 多章节无损改写
阅读 13-section-revision/SKILL.md。
改写 Methods 与 Experiments，使公式的动机和实验的作用连成一条线；
逐项核对所有 LaTeX 表格、图片路径、caption、label、引用键和数值，
没有证据的地方不补造。报告哪些检查实际执行过。
~~~

## 根据你的问题选择 Skill

**不需要全部运行。** 根据当前痛点选择一个主 Skill；仅在跨章节冲突时引入其他模块。

| 你现在需要解决的问题 | 入口 |
| --- | --- |
| 摘要泛泛而谈、结论没有证据 | [01 · Abstract](01-abstract/SKILL.md) |
| 引言背景多但研究问题迟迟不出现 | [02 · Introduction](02-introduction/SKILL.md) |
| Related Work 成了按作者排列的清单 | [03 · Related Work](03-related-work/SKILL.md) |
| Methods 一上来就是公式/模块，读者不知为何需要 | [04 · Method](04-method/SKILL.md) |
| 实验表格多，却无法对应 claim 和比较条件 | [05 · Experiments](05-experiment/SKILL.md) |
| Discussion 重复 Results，Conclusion 夸大了范围 | [06 · Discussion & Conclusion](06-discussion-conclusion/SKILL.md) |
| 框架图/图注有歧义，或图文不一致 | [07 · Figures](07-figure/SKILL.md) |
| 标题和小标题没有准确提示论文贡献 | [08 · Titles & Headings](08-title-heading/SKILL.md) |
| 投稿前查事实、统计、引用、全稿一致性 | [09 · Consistency Audit](09-consistency-validation/SKILL.md) |
| 制作或修正 LaTeX 科研表格 | [10 · LaTeX Tables](10-latex-table/SKILL.md) |
| 用真实数据制作可复现科研图 | [11 · Research Plots](11-research-plot/SKILL.md) |
| 需要可编辑 PPTX 结构图 | [12 · Editable PPTX Diagrams](12-pptx-visual/SKILL.md) |
| Methods 和 Experiments 要联动重构且不能丢失现有内容 | [13 · Cross-Section Revision](13-section-revision/SKILL.md) |

**怎么组合？** 常见的修稿路径是 **09 诊断 → 02/03 明确定位 → 04/05 重写论证 → 06 收束 → 01 更新摘要 → 09 复核**；这只是可能的依赖顺序，不是固定步骤。图示与表格类 Skill 按需使用。见 [WORKFLOW.md](WORKFLOW.md)。

## 它为什么和通用润色不同？

- **先检查前提，再改写语言：** 不替错误的科学论断寻找漂亮说辞。
- **专名就近解释与引用：** 外部方法、模型、benchmark、数据集来源可追踪；引用不必都堆在句末。见 [CITATION_GUIDE.md](CITATION_GUIDE.md)。
- **把实验当作推理，而非战报：** 要求控制变量、明确统计单位、公平比较和适用边界。
- **审阅与改写分离：** 若只要求审查，不擅自修改论文；已有 LaTeX 内容可按无损修订契约核对。
- **分离“核验过”和“尚未检查”：** 文本一致性、编译成功、原始实验可复现性是不同层次的证据。

总约束在 [PRINCIPLES.md](PRINCIPLES.md)，学科差异见 [STEM_GUIDE.md](STEM_GUIDE.md)，引用规范在 [CITATION_GUIDE.md](CITATION_GUIDE.md)。

## 适用范围与边界

主要适用于数学、计算机、工程、物理、材料、生物、地球与环境科学及其他 STEM 研究；根据理论证明、实验、现场观测、仿真或系统测评采用不同的证据标准。**不预设投稿会议、固定章节数、固定实验数或统一叙事模板。**

它是**Markdown Skill 与工作流指南集合**，并非可自动完成检索、实验或 LaTeX 编译的在线服务。能否加载 Skill、联网核验文献、修改源文件、绘制图像或生成 PPTX，取决于你实际使用的工具及权限。没有原始论文、BibTeX、实验记录或编译环境时，必须报告未验证之处。

## 开发与质量检查

~~~bash
python scripts/check_skills.py
~~~

仓库检查覆盖 Skill 命名/元数据、相对链接、核心指南及 README 入口等**静态约束**。示例场景见 [tests/skill-scenarios.md](tests/skill-scenarios.md)。静态检查不能替代真实模型输出评估、引用真实性核查、原始实验复现或最终 PDF 人工审查。

可参考的设计思路包括 [Anthropic Skills](https://github.com/anthropics/skills)、[Superpowers](https://github.com/obra/superpowers)、[Academic Writing Skills](https://github.com/WenyuChiou/academic-writing-skills)；本项目针对科研论文的**主张—证据—范围**提出独立规则，并非上述项目的官方扩展或性能验证。

## 关注更新与参与

如果你也在写论文、做科研，觉得这套审查规则值得持续完善，欢迎 [**⭐ Star 本仓库**](https://github.com/ChenXiangYpily1234/paper-storycraft-skills)。Star 能让你之后方便找到它；问题反馈和失败案例请通过 Issues 提交。

## 参与与许可

欢迎通过 [Issues](https://github.com/ChenXiangYpily1234/paper-storycraft-skills/issues) 报告错误规则、模糊步骤和可复现的失败案例。请勿上传未获授权的未发表论文或保密实验数据。

项目采用 [MIT License](LICENSE)。相关项目的独立致谢见 [ACKNOWLEDGEMENTS.md](ACKNOWLEDGEMENTS.md)。

**一条原则：可以重写论证的表达，不能重写事实。**
