# 图形选择、数据口径与验收

## 有序类别曲线模板

`../scripts/plot_ordered_series.py` 接收 UTF-8 CSV，列为 `series,category,value`。
每个 `(series, category)` 必须唯一，所有系列使用相同类别且顺序一致。
输入需已按协议汇总；脚本不计算均值、不补缺失值、不构造置信区间。
类别顺序和系列顺序沿用 CSV 首次出现的顺序，必须核对这是否符合科学含义。

```sh
python3 scripts/plot_ordered_series.py \
  --input /absolute/path/verified.csv \
  --output /absolute/path/fig/history_profile \
  --xlabel 'Observed history length' \
  --ylabel 'Worst-seed tolerance (%)'
```

导出 `history_profile.pdf` 和 `history_profile.png`。模板默认单栏宽度，
只适用于有序类别、最多三个系列、无误差区间的简单折线。
其他尺寸、图型、更多系列、中文字体或真实置信区间需要复制后按任务修改。
复制脚本到项目并记录数据来源和汇总逻辑，不仅保留临时 skill 命令。

先用选定解释器检查 `import seaborn, matplotlib, pandas`。解释器与依赖路径
以当前环境为准，不能假定所有预装运行时都有 seaborn。缺依赖时先寻找项目
环境或已存在解释器；安装操作按用户授权与项目规范执行。

## 常见科学口径

| 问题 | 合适呈现 | 必须说明 |
| --- | --- | --- |
| 随 history bin 的变化 | 有序类别折线 | bin 边界、样本量变化、汇总规则 |
| 模型在独立数据集的结果 | 分组点图或柱图 | metric、分组、seed 口径 |
| 多 seed 稳定性 | seed 点加真实统计区间 | 区间算法、独立单位与置信水平 |
| 退化或失败边界 | 曲线与已定义阈值 | 阈值来源、未达标点、缺失值 |
| 指标分布 | 箱线、小提琴或 ECDF | 样本单位、分布宽度含义 |
| 二维消融 | 热图或分面 | 色条单位、共享范围、缺失值 |

同一图中的 R@10 与 tolerance (%) 等不同量通常分面呈现，避免不必要的双轴。
涉及 paired bootstrap 时，复用实验协议或真实结果，不在绘图代码中临时
发明统计方法。已有 worst-seed 指标使用其真实汇总值；不要把均值误标为 worst-seed。

## 可见性与导出检查

- 同坐标 marker 可用不同大小的空心形状；若嵌套仍无法辨认，改用分面。
  不添加未说明的坐标偏移。
- 曲线的 marker 边缘颜色应与曲线一致，检查白边是否令低值点消失。
- 标签过长时先缩短并解释，或调整比例；不要持续缩小字体。
- PDF 文字应可检索，轴名、负号、希腊字母和数学符号无缺字。
- 在实际论文尺寸下检查 legend、axis、线宽、所有极值点和零值点。
- 至少查看 PNG 预览和编译后 PDF 中的图；只看脚本或文件存在不算验收。
- 表述精度与原数据一致；可视化不能支撑新因果结论或统计等价结论。

完成时注明核验的数据文件、输出路径、统计口径和残留限制。

## 两张支撑图的论文集成示例

当用户要求两张图均留正文时，可让两个独立科学问题各占单栏：
item–text correspondence 说明保留语义证据的作用，history boundary 说明失效范围。
这只是布局示例，不要求不同论文沿用具体实验或页数。

- 对应关系图可在同一单栏内上下排列性能变化与 semantic weight 两个 panel。
  保留真实原值、permutation 均值和误差来源；caption 简短交代干预、发现及 permutation 数。
- history 图保留真实 bin、worst-seed 定义、post-hoc split 和描述性分析限定。
  轴使用 worst-seed 时，正文提到 seed-wise 范围必须明确二者不同。
- 编译后按左栏到右栏检查：引图文字先于图，图先于其收尾结论，下一节不夹在图与解释中间。
- 若精简表格即可腾出空间，不修改已有图片文件；不缩全局字号，不删保留图，不把引用指向尚不存在的 supplement。
