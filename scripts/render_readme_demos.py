#!/usr/bin/env python3
"""Render the three bilingual README demonstrations and static reading copies.

Requires Pillow and Noto Sans CJK SC (installed by the rendering workflow).
Set STORYCRAFT_FONT_REGULAR / STORYCRAFT_FONT_BOLD to use local font files.
All tasks, paper labels and comparison fields are explicitly illustrative.
"""
from functools import lru_cache
from pathlib import Path
import os
import subprocess

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "assets"
W, H = 1200, 780
INK, PAPER, MUTE = "#0B1423", "#EDF5FF", "#A1B4CC"
CYAN, VIOLET, AMBER, CORAL = "#62E2C5", "#B6A3F5", "#F1C87C", "#EF9CA6"
PANEL, LINE, QUIET = "#142136", "#344A63", "#7E93AD"
DURATIONS = (1200, 1800, 2200, 2600, 2600, 5000)


@lru_cache(maxsize=64)
def font(size, bold=False):
    variable = "STORYCRAFT_FONT_BOLD" if bold else "STORYCRAFT_FONT_REGULAR"
    path = os.environ.get(variable)
    if not path:
        family = "Noto Sans CJK SC" + (":style=Bold" if bold else ":style=Regular")
        try:
            match = subprocess.check_output(
                ["fc-match", "-f", "%{family}\n%{file}", family], text=True
            ).strip().splitlines()
        except (FileNotFoundError, subprocess.CalledProcessError) as exc:
            raise RuntimeError(
                "Install fontconfig and Noto Sans CJK SC, or set "
                "STORYCRAFT_FONT_REGULAR and STORYCRAFT_FONT_BOLD."
            ) from exc
        if len(match) != 2 or "Noto Sans CJK SC" not in match[0]:
            raise RuntimeError(
                "Noto Sans CJK SC is missing; refusing to render missing Chinese glyphs. "
                "Install fonts-noto-cjk or set the STORYCRAFT_FONT_* paths."
            )
        path = match[1]
    return ImageFont.truetype(path, size)


def put(draw, xy, text, size=22, color=PAPER, bold=False, width=None):
    """Draw top-aligned text, failing instead of silently clipping a label."""
    text = str(text)
    face = font(size, bold)
    if width is not None and draw.textlength(text, font=face) > width:
        raise ValueError(f"Label exceeds {width}px at {size}px: {text}")
    draw.text(xy, text, font=face, fill=color, anchor="lt")


def block(draw, rect, text, size=22, color=PAPER, bold=False, gap=8):
    """Wrap English at spaces and Chinese at characters within a fixed box."""
    left, top, right, bottom = rect
    face = font(size, bold)
    lines = []
    for paragraph in text.split("\n"):
        remaining = paragraph
        while remaining:
            end = 1
            while end <= len(remaining) and draw.textlength(remaining[:end], font=face) <= right-left:
                end += 1
            end -= 1
            if end == 0:
                raise ValueError(f"Text box is too narrow: {text}")
            if end < len(remaining):
                space = remaining.rfind(" ", 0, end+1)
                if space > 0:
                    end = space
            lines.append(remaining[:end].rstrip())
            remaining = remaining[end:].lstrip()
        if not paragraph:
            lines.append("")
    if lines and top + len(lines) * (size+gap) - gap > bottom:
        raise ValueError(f"Text box is too short: {text}")
    for i, line in enumerate(lines):
        put(draw, (left, top+i*(size+gap)), line, size, color, bold, right-left)


def card(draw, rect, fill=PANEL, outline=LINE, radius=16, width=1):
    draw.rounded_rectangle(rect, radius=radius, fill=fill, outline=outline, width=width)


def step_style(stage, number, color=CYAN):
    active = stage >= number
    return (
        "#193541" if active else "#17263A",
        color if active else LINE,
        PAPER if active else MUTE,
    )


def row(draw, rect, stage, number, label, detail, color=CYAN, size=22):
    fill, edge, text_color = step_style(stage, number, color)
    card(draw, rect, fill, edge, radius=12, width=2 if stage == number else 1)
    x1, y1, x2, _ = rect
    put(draw, (x1+18, y1+10), label, 17, edge if stage >= number else QUIET, True, x2-x1-36)
    put(draw, (x1+18, y1+36), detail, size, text_color, width=x2-x1-36)


def base(topic, title, subtitle, stage, steps, zh):
    image = Image.new("RGB", (W, H), INK)
    draw = ImageDraw.Draw(image)
    # A fixed, flat background keeps the animation light and avoids flicker.
    draw.rectangle((0, 0, 9, H), fill=CYAN)
    put(draw, (44, 31), "PAPER STORYCRAFT", 20, CYAN, True)
    put(draw, (285, 34), topic, 16, MUTE)
    card(draw, (1040, 27, 1156, 61), "#18343D", "#396D70", radius=10)
    counter = f"{stage:02} / 05" if stage else ("开始" if zh else "START")
    put(draw, (1061, 36), counter, 16, CYAN, True, 85)
    put(draw, (44, 82), title, 34, PAPER, True, 1112)
    put(draw, (44, 134), subtitle, 20, MUTE, width=1112)
    draw.line((44, 164, 1156, 164), fill=LINE, width=1)
    card(draw, (44, 184, 326, 680), PANEL, "#544653")
    card(draw, (348, 184, 1156, 680), "#102735", "#37646A")
    put(draw, (66, 204), "BEFORE / 原始写法" if zh else "BEFORE / DRAFT", 18, CORAL, True, 238)
    put(draw, (370, 204), "AFTER / 论证重构" if zh else "AFTER / REVISED ARGUMENT", 18, CYAN, True, 764)
    for index, label in enumerate(steps, 1):
        x = 44 + (index-1)*224
        color = CYAN if stage >= index else QUIET
        draw.line((x, 706, x+202, 706), fill=color if stage >= index else LINE, width=3)
        put(draw, (x, 717), f"{index:02}  {label}", 16, color, stage == index, 210)
    note = "流程示意 · 不含真实实验结果或已核验文献" if zh else "ILLUSTRATIVE WORKFLOW · NO REAL RESULTS OR VERIFIED REFERENCES"
    put(draw, (44, 753), note, 14, MUTE, width=1112)
    return image, draw


def missing_links(draw, heading, labels, start=443):
    put(draw, (66, start-38), heading, 17, CORAL, True, 238)
    for i, label in enumerate(labels):
        y = start+i*48
        draw.ellipse((67, y+8, 73, y+14), fill=CORAL)
        put(draw, (85, y), label, 19, MUTE, width=219)


def arrow(draw, x, y, active):
    color = CYAN if active else QUIET
    draw.line((x, y, x+17, y), fill=color, width=2)
    draw.line((x+11, y-5, x+17, y, x+11, y+5), fill=color, width=2)


def argument_frame(zh, stage):
    title = "Methods：让每一步都有依据" if zh else "Methods: make every operation earn its place"
    subtitle = "具体困难 → 设计要求 → 操作过程 → 证据与范围" if zh else "Connect a concrete difficulty to a design, its operations, evidence and scope"
    steps = ("明确问题", "解释要求", "展开操作", "对齐证据", "限定范围") if zh else (
        "Question", "Requirement", "Operation", "Evidence", "Scope")
    image, draw = base("01 / METHODS", title, subtitle, stage, steps, zh)
    block(draw, (66, 256, 302, 324), "我们提出三个模块。" if zh else "We introduce three modules.", 24)
    for index, letter in enumerate("ABC"):
        x = 66+index*84
        card(draw, (x, 340, x+68, 395), "#2C2D42", "#745662", radius=12)
        put(draw, (x+24, 355), letter, 26, CORAL, True)
    missing_links(draw, "尚未说清" if zh else "MISSING LINKS", (
        "为什么需要它？", "具体如何处理？", "用什么证据检验？") if zh else (
        "Why is it needed?", "What does it do?", "What would test it?"), start=470)
    block(draw, (66, 625, 302, 664), "假设性示例，非真实方法。" if zh else "Hypothetical method only.", 17, QUIET)
    row(draw, (370, 235, 1134, 304), stage, 1,
        "研究问题 / QUESTION" if zh else "QUESTION / HYPOTHETICAL SETUP",
        "示例假设：含噪观测使估计不稳定（需验证）" if zh else "Suppose noisy observations destabilize an estimate; verify this.")
    row(draw, (370, 316, 1134, 385), stage, 2,
        "设计要求 / REQUIREMENT" if zh else "DESIGN REQUIREMENT",
        "保留可靠信息，同时测量额外的处理代价" if zh else "Retain reliable information and measure the added processing cost.", VIOLET)
    fill, edge, text_color = step_style(stage, 3)
    card(draw, (370, 397, 1134, 505), fill, edge, radius=12, width=2 if stage == 3 else 1)
    put(draw, (388, 407), "方法操作 / OPERATION" if zh else "OPERATION / EXPLICIT DATA FLOW", 17, edge, True, 728)
    nodes = (("输入", "含噪观测"), ("操作", "估计并应用权重"), ("输出", "加权观测"), ("下游用途", "供估计器使用")) if zh else (
        ("INPUT", "Noisy observations"), ("OPERATION", "Infer + apply weights"),
        ("OUTPUT", "Weighted inputs"), ("NEXT USE", "Feed the estimator"))
    for i, (label, value) in enumerate(nodes):
        x = 388+i*186
        put(draw, (x, 438), label, 15, edge if stage >= 3 else QUIET, True, 170)
        put(draw, (x, 470), value, 21 if zh else 17, text_color, width=170)
        if i < 3:
            arrow(draw, x+148, 447, stage >= 3)
    row(draw, (370, 517, 1134, 586), stage, 4,
        "证据检验 / EVIDENCE" if zh else "EVIDENCE / TEST THE PROPOSED MECHANISM",
        "匹配对照 + 去除该操作 + 不确定性与成本" if zh else "Matched controls + remove the operation + uncertainty and cost.", AMBER)
    row(draw, (370, 598, 1134, 667), stage, 5,
        "结论范围 / SCOPE" if zh else "SCOPE / KEEP THE CLAIM WITHIN THE EVIDENCE",
        "只陈述已检验条件下的结论，保留失败情形" if zh else "Limit conclusions to tested conditions and retain failure cases.", CORAL)
    return image


def related_work_frame(zh, stage):
    title = "Related Work：比较机制，再核验差异" if zh else "Related Work: compare mechanisms, then verify"
    subtitle = "保持文献身份一致，用相同字段比较，检查最强前人反例" if zh else "Keep paper identities stable; compare shared fields; check the strongest prior work"
    steps = ("核对来源", "按机制分组", "同轴比较", "检查反例", "核验空白") if zh else (
        "Sources", "Mechanisms", "Shared axes", "Counterexamples", "Verify the gap")
    image, draw = base("02 / RELATED WORK", title, subtitle, stage, steps, zh)
    block(draw, (66, 252, 304, 326), "按年份逐篇罗列，\n读完仍不知区别。" if zh else "A paper-by-paper list hides the distinctions.", 23)
    for i in range(6):
        x, y = 66+(i % 2)*124, 350+(i//2)*64
        card(draw, (x, y, x+114, y+46), "#263149", CYAN if stage == 1 else LINE, radius=10)
        put(draw, (x+12, y+14), f"Paper {i+1:02}", 18, PAPER, width=90)
    block(draw, (66, 578, 302, 662), "Paper 01–06 均为占位符；不是已核验的真实文献。" if zh else "Paper 01–06 are placeholders, not verified publications.", 18, MUTE)
    groups = (("路线 A · 固定数据", CYAN), ("路线 B · 生成数据", VIOLET)) if zh else (
        ("FAMILY A / FIXED DATA", CYAN), ("FAMILY B / GENERATED DATA", VIOLET))
    for group, (label, color) in enumerate(groups):
        x = 370+group*390
        fill, edge, text_color = step_style(stage, 2, color)
        card(draw, (x, 239, x+374, 329), fill, edge, radius=12, width=2 if stage == 2 else 1)
        put(draw, (x+16, 252), label, 18 if zh else 17, edge, True, 342)
        for k in range(3):
            bx = x+16+k*116
            card(draw, (bx, 287, bx+110, 315), "#223A4B", LINE, radius=7)
            put(draw, (bx+13, 294), f"Paper {group*3+k+1:02}", 16, text_color, width=84)
    # Identical fields in both columns expose what is known and what needs checking.
    x0, x1, x2, x3 = 370, 550, 842, 1134
    fill, edge, text_color = step_style(stage, 3)
    card(draw, (x0, 343, x3, 505), fill, edge, radius=12, width=2 if stage == 3 else 1)
    headers = ("共同比较字段", "路线 A（示意）", "路线 B（示意）") if zh else (
        "SHARED FIELD", "FAMILY A / EXAMPLE", "FAMILY B / EXAMPLE")
    for x, right, label in zip((x0, x1, x2), (x1, x2, x3), headers):
        put(draw, (x+14, 356), label, 17 if zh else 15, edge, True, right-x-28)
    entries = (
        ("训练数据", "固定训练集", "生成训练集"),
        ("目标函数", "[核对损失 / 目标]", "[核对损失 / 目标]"),
        ("信息访问", "[核对参数 / 输出]", "[核对参数 / 输出]"),
        ("评测与预算", "[核对协议 / 资源]", "[核对协议 / 资源]"),
    ) if zh else (
        ("Data", "Fixed training set", "Generated training set"),
        ("Objective", "[Verify loss / target]", "[Verify loss / target]"),
        ("Access", "[Verify weights / outputs]", "[Verify weights / outputs]"),
        ("Eval / budget", "[Verify protocol / cost]", "[Verify protocol / cost]"),
    )
    for i, values in enumerate(entries):
        y = 387+i*30
        draw.line((x0+1, y-9, x3-1, y-9), fill=LINE, width=1)
        for x, right, value in zip((x0, x1, x2), (x1, x2, x3), values):
            put(draw, (x+14, y), value, 20 if zh else 18, text_color, width=right-x-28)
    for x in (x1, x2):
        draw.line((x, 344, x, 504), fill=LINE, width=1)
    row(draw, (370, 517, 1134, 586), stage, 4,
        "最强前人反例 / COUNTEREXAMPLE" if zh else "STRONGEST PRIOR WORK / CHECK BEFORE CLAIMING NOVELTY",
        "最接近的工作是否已经覆盖同一设定？" if zh else "Does the strongest prior work already cover this setup?", VIOLET, size=20)
    row(draw, (370, 598, 1134, 667), stage, 5,
        "仍待核验 / UNVERIFIED" if zh else "UNVERIFIED / AN OPEN QUESTION IS NOT AN ESTABLISHED GAP",
        "有差异不代表已证实新颖性；有反例就收窄主张" if zh else "A difference alone does not establish novelty; check counterexamples.", AMBER, size=20)
    return image


def experiments_frame(zh, stage):
    title = "Experiments：让证据决定结论范围" if zh else "Experiments: let the evidence set the claim"
    subtitle = "公平比较 → 真实观察 → 可支持的解释 → 正文与补充材料" if zh else "Matched comparisons, actual observations, bounded inference and retained evidence"
    steps = ("明确问题", "公平比较", "报告观察", "限制推断", "保留证据") if zh else (
        "Question", "Fair comparison", "Observation", "Inference", "Disclosure")
    image, draw = base("03 / EXPERIMENTS", title, subtitle, stage, steps, zh)
    block(draw, (66, 254, 304, 394), "“我们的方法显著优于现有基线。”" if zh else '“Our method significantly outperforms existing baselines.”', 24)
    put(draw, (66, 406), "未核验的原稿表述" if zh else "UNVERIFIED DRAFT CLAIM", 16, CORAL, True, 238)
    missing_links(draw, "仍需回答" if zh else "QUESTIONS TO ANSWER", (
        "是否公平比较？", "差异有多不确定？", "结论适用于哪里？") if zh else (
        "A fair comparison?", "How uncertain?", "Which conditions?"), start=500)
    block(draw, (66, 646, 304, 670), "不填造实验数字。" if zh else "No invented measurements.", 16, QUIET)
    row(draw, (370, 235, 1134, 304), stage, 1,
        "检验问题 / QUESTION" if zh else "QUESTION / DEFINE WHAT THE EXPERIMENT TESTS",
        "在 [任务 / 数据集] 上，是否改善 [预设指标]？" if zh else "On [task / dataset], does it improve [prespecified metric]?")
    row(draw, (370, 316, 1134, 385), stage, 2,
        "公平比较 / COMPARISON" if zh else "COMPARISON / MAKE THE CONDITIONS COMPARABLE",
        "[实际 baseline] · 同协议 · 可比数据、信息与预算" if zh else "[Actual baseline] + matched protocol, data, access and budget.", VIOLET)
    row(draw, (370, 397, 1134, 466), stage, 3,
        "观察与不确定性 / OBSERVATION" if zh else "OBSERVATION / REPORT THE EFFECT AND AVAILABLE UNCERTAINTY",
        "[真实差异] + [可用区间 / 重复实验变异]" if zh else "[Actual effect] + [available interval / variation across repeats].", AMBER)
    row(draw, (370, 478, 1134, 547), stage, 4,
        "推断边界 / INFERENCE" if zh else "INFERENCE / RETAIN COMPETING EXPLANATIONS",
        "只支持已测试条件；说明仍未排除的解释" if zh else "Stay within tested conditions; state explanations not ruled out.")
    fill, edge, text_color = step_style(stage, 5, CORAL)
    card(draw, (370, 559, 1134, 667), fill, edge, radius=12, width=2 if stage == 5 else 1)
    put(draw, (388, 570), "证据放置 / DISCLOSURE" if zh else "DISCLOSURE / KEEP THE FULL EVIDENCE TRACEABLE", 17, edge, True, 728)
    draw.line((751, 600, 751, 653), fill=LINE, width=1)
    put(draw, (388, 600), "正文" if zh else "MAIN PAPER", 16, edge, True, 345)
    put(draw, (771, 600), "附录 / 补充材料" if zh else "APPENDIX / SUPPLEMENT", 16, edge, True, 345)
    block(draw, (388, 625, 733, 664), "影响核心结论的反证与代价" if zh else "Claim-changing evidence / costs;\nlink to the complete data.", 20 if zh else 15, text_color, gap=5)
    block(draw, (771, 625, 1116, 664), "次要细节保留，并可追溯" if zh else "Retain secondary details\nwith traceable evidence.", 20 if zh else 15, text_color, gap=5)
    return image


def write(frames, stem):
    OUT.mkdir(parents=True, exist_ok=True)
    # One palette across every frame avoids text/color shimmer. Disposal 1 keeps
    # unchanged regions, so a readable hold does not duplicate full-size images.
    sample = Image.new("RGB", (W, H*2))
    sample.paste(frames[0], (0, 0))
    sample.paste(frames[-1], (0, H))
    palette = sample.quantize(colors=128, method=Image.Quantize.MEDIANCUT)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    gif = OUT / f"{stem}.gif"
    indexed[0].save(gif, save_all=True, append_images=indexed[1:],
                    loop=0, duration=DURATIONS, optimize=True, disposal=1)
    png = OUT / f"{stem}.png"
    frames[-1].save(png, optimize=True)
    if gif.stat().st_size >= 300_000:
        raise ValueError(f"Animation exceeds the README size budget: {gif}")
    print(f"{stem}: {gif.stat().st_size / 1024:.1f} KiB GIF, "
          f"{png.stat().st_size / 1024:.1f} KiB PNG")


if __name__ == "__main__":
    for language in ("zh", "en"):
        for topic, render in (("argument", argument_frame),
                              ("related-work", related_work_frame),
                              ("experiments", experiments_frame)):
            write([render(language == "zh", stage) for stage in range(6)],
                  f"demo-{topic}-{language}")
