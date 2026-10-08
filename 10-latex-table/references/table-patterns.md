# 紧凑表格布局与构建检查

## 压缩顺序

1. 明确每列的作用，缩短重复叙述，详细机制留正文。
2. 为短文本使用 `l/c/r`，不把它们放进过窄的可换行列。
3. 将 panel 内共享的常量放在 panel 标题或短表注中。
4. 统一字号后调整列间距与分配；移除不必要的首尾留白。
5. 仍过宽时合理分 panel、拆表或采用双栏。不能删掉反例、统计限定和单位。

概览表应像地图：`System / Role / Mechanism / Prior`。
同一模型的长定义、引用和 representation-control 的动机放在首次介绍正文。
结果表使用短指标名，正文先定义 R@K、NDCG@K、LCB 等术语。

## Panel 表

例如 Panel A = all users、Panel B = valid outputs，样本数不同就分别列出。
共有 baseline 可放 panel 标题，但不能让读者误以为两个 panel 共享不同的 baseline。
标题可以使用 `\multicolumn{...}{@{}l}{...}`；若该标题太长则缩短措辞。
表头单行不等于表注必须一行。表注自然换行，不改变模板的 caption 样式。

对于只有少数 adapted variants 的 controller 比较，可采用：
`Controller / Access / R@10 / Delta / Bound`。
将 `Label / Imit.` 放在 controller 名后，正文定义训练目标，caption 简短解码。
若大多数行无需 adaptation，避免设置整列破折号。
Panel A 的 lower bound 与 Panel B 的 paired CI 可以共用 `Bound` 列，但需在
caption 写出 one-sided/two-sided、置信水平、各 panel 分母和对照的 R@10。
同一套表头不必在 Panel B 重复。若这些说明已在 caption 中，删除正文紧邻表格的重复解码句。

## 值与统计含义检查

- 重排前后逐项比较 dataset/model/seed/metric/value/unit；相同数值但配错行也是错误。
- 不同 panel 的分母、无效输出处理、paired comparison 的对象不能在压缩时丢失。
- `r_min`、drop (%) 与 difference 是不同量，避免用同一简称。
- 统一数值表示保留真实精度，不将 0.1% 改成 10% 或交换百分比与比例。
- 全 seeds 成立的结论需保留相应规则。置信区间跨零不等于统计等价。
- 仅因 caption 过长，可把已定义的模型背景移回正文；保留必要测量范围。

## LaTeX 模板用法

复制 `../assets/compact_tables.tex` 的目标环境到论文，使用论文实际 label，
确保文档已加载 `booktabs`。不要重复加载会和文档类冲突的 caption 包。
字母占位符没有实验含义，必须替换或删除后才能用于论文。
模板使用 `\small` 以及局部间距设置，不影响正文和其他文档。

## 通用 LaTeX 项目构建与表格验收

1. 先确认当前修订的是作者指定的**最新主文件**与实际构建目录；不要沿用旧版本的路径、标签或构建命令。
2. 查询项目使用的 `latexmk`、`pdflatex + bibtex`、`biber`、`xelatex`、`lualatex` 等实际工作流，以项目配置为准，不默认某一种工具链。
3. 重新构建后检查未解析引用、编译警告、表格超宽、浮动次序、图表编号和 PDF 阅读顺序。
4. 按受影响表格的**实际 PDF 页面**选取检查范围，不预设第几页或多少页；文字抽取不能代替视觉检查。
5. 检查模型、指标及缩写是否在阅读到表格前获得足够背景；必须确保表注可独立提供其必要统计口径。
6. 未获取源码、无法成功编译或未查看页面时，明确记录检查状态，不得声称已经通过。

一个项目*可能*采用如下命令，但必须根据当前构建配置决定是否使用，不可直接套用：

```sh
latexmk -pdf -interaction=nonstopmode -halt-on-error main.tex
```

代码模板中的数值都是格式示意，不得冒充真实论文实验结果。
