#!/usr/bin/env python3
"""Create evidence-safe, bilingual animated README examples.

Requires Pillow and Noto Sans CJK (installed in the GitHub rendering workflow).
All papers, labels and comparisons shown in the animation are illustrative.
"""
from functools import lru_cache
from pathlib import Path
import math
import subprocess

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "assets"
OUT.mkdir(parents=True, exist_ok=True)

W, H = 1080, 580
INK, PAPER, MUTE = "#081321", "#EAF6FF", "#99B5CE"
CYAN, VIOLET, AMBER, CORAL = "#5CF3D1", "#B7A0FF", "#FDD17D", "#FF929C"
PALETTE = [CYAN, VIOLET, AMBER, CORAL]


@lru_cache(maxsize=24)
def font(size, bold=False):
    family = "Noto Sans CJK SC:style=Bold" if bold else "Noto Sans CJK SC"
    path = subprocess.check_output(["fc-match", "-f", "%{file}", family], text=True).strip()
    return ImageFont.truetype(path, size)


def put(draw, xy, value, size=20, color=PAPER, bold=False):
    draw.text(xy, str(value), font=font(size, bold), fill=color)


def card(image, rect, fill="#172941", outline="#325477", radius=18):
    d = ImageDraw.Draw(image)
    d.rounded_rectangle(rect, radius=radius, fill=fill, outline=outline, width=2)
    return d


def halo(image, cx, cy, color, radius=22):
    d = ImageDraw.Draw(image)
    for r, width in ((radius + 18, 1), (radius + 9, 2), (radius, 2)):
        d.ellipse((cx-r, cy-r, cx+r, cy+r), outline=color, width=width)


def base(section, title, subtitle, frame):
    image = Image.new("RGB", (W, H), INK)
    # Stable gradient and star-grid: visual interest without flashing frames.
    px = image.load()
    for y in range(H):
        for x in range(W):
            glow = max(0, 1 - math.hypot(x - 950, y - 130) / 650)
            shade = y / H
            px[x, y] = (
                int(8 + 5 * shade + 8 * glow),
                int(18 + 12 * shade + 11 * glow),
                int(34 + 17 * shade + 18 * glow),
            )
    d = ImageDraw.Draw(image)
    for x in range(24, W - 10, 40):
        for y in range(22, H - 14, 40):
            d.ellipse((x, y, x + 2, y + 2), fill="#23415B")
    d.rounded_rectangle((39, 30, 254, 63), radius=12,
                        fill="#123644", outline="#377979", width=1)
    put(d, (54, 35), f"PAPER STORYCRAFT  /  {section}", 15, CYAN, True)
    put(d, (39, 73), title, 35, PAPER, True)
    put(d, (41, 124), subtitle, 17, MUTE)
    d.line((40, 161, 1039, 161), fill="#294860", width=2)
    for i in range(6):
        x = 904 + 23 * i
        d.rounded_rectangle((x, 40, x + 14, 46), radius=3,
                            fill=CYAN if i <= frame else "#38556C")
    put(d, (40, 544), "ILLUSTRATIVE ONLY  ·  NOT RESEARCH EVIDENCE", 14, "#7D99B0")
    return image


def write(frames, filename):
    frames = [im.quantize(colors=48, method=Image.Quantize.FASTOCTREE,
                          dither=Image.Dither.NONE) for im in frames]
    path = OUT / filename
    frames[0].save(path, save_all=True, append_images=frames[1:],
                   loop=0, duration=[700, 920, 920, 920, 1600, 900],
                   optimize=True, disposal=2)
    print(f"{filename}: {path.stat().st_size / 1024:.1f} KiB")


def argument_demo(language):
    zh = language == "zh"
    title = ("别再堆模块：让论文形成证据链" if zh else
             "Beyond modules: build a defensible research argument")
    subtitle = ("明确问题 → 解释设计 → 对齐实验 → 限定结论" if zh else
                "Make the question, design, evidence and scope connect")
    stages = [
        ("研究问题", "待核查的具体困难"),
        ("设计逻辑", "A → B → C 的必要作用"),
        ("验证证据", "对照 · 指标 · 不确定性"),
        ("结论边界", "仅覆盖实际验证的条件"),
    ] if zh else [
        ("QUESTION", "specific, sourced difficulty"),
        ("DESIGN", "why A → B → C is needed"),
        ("EVIDENCE", "controls · metrics · uncertainty"),
        ("SCOPE", "only tested conditions"),
    ]
    before = ["我们提出 A、B、C。", "效果比基线更好。", "适用于所有任务。"] if zh else [
        "We introduce modules A, B, C.", "Our method is better.", "It works for all tasks."]
    frames = []
    for stage in range(6):
        im = base("01", title, subtitle, stage)
        d = card(im, (40, 191, 375, 511), "#19253B", "#45506E")
        put(d, (60, 209), "BEFORE  /  原始写法" if zh else
            "BEFORE  /  VAGUE CLAIMS", 18, CORAL, True)
        d.line((61, 247, 350, 247), fill="#3D4C67", width=2)
        for i, sentence in enumerate(before):
            y = 283 + i * 69
            d.rounded_rectangle((60, y, 68, y + 31), radius=4, fill=CORAL)
            put(d, (82, y + 1), sentence, 18, "#D4D9E4")
        d = card(im, (395, 191, 1040, 511), "#112E40", "#377A80")
        put(d, (418, 208), "AFTER  /  论证链" if zh else
            "AFTER  /  ARGUMENT MAP", 18, CYAN, True)
        for i, (label, note) in enumerate(stages):
            y = 256 + i * 59
            active = stage >= i + 1
            color = PALETTE[i]
            if active:
                hot = i == min(stage, 4) - 1
                d.rounded_rectangle((432, y-7, 999, y+42), radius=13,
                    fill="#1B4256" if hot else "#1A374B",
                    outline=color if hot else "#365F77", width=2)
                d.ellipse((448, y+5, 475, y+32), fill=color)
                put(d, (456, y+5), i+1, 16, INK, True)
                put(d, (489, y), label, 20, color, True)
                put(d, (669 if zh else 636, y+2), note, 17)
            else:
                d.rounded_rectangle((432, y-7, 999, y+42), radius=13,
                    fill="#182B3B", outline="#365066", width=1)
                put(d, (452, y+3), f"{i+1:02}", 17, "#57768C", True)
                put(d, (494, y+4), "—  —  —  —  —  —", 16, "#557187")
            if i < 3:
                d.line((463, y+42, 463, y+52), fill=color if
                       stage >= i+2 else "#415B74", width=3)
        if stage >= 4:
            halo(im, 1009, 457, CYAN, 20)
        put(d, (822, 540), f"{min(stage,4)}/4", 16, CYAN, True)
        frames.append(im)
    write(frames, f"demo-argument-{language}.gif")


def related_work_demo(language):
    zh = language == "zh"
    title = ("Related Work：从引文清单到研究地图" if zh else
             "Related Work: turn citations into a research map")
    subtitle = ("按机制分组，同维度比较；研究空白必须经文献核查" if zh else
                "Group by mechanism; compare shared axes; verify the gap")
    frames = []
    for stage in range(6):
        im = base("02", title, subtitle, stage)
        d = card(im, (40, 187, 405, 511), "#18263A", "#47526A")
        put(d, (62, 207), "BEFORE  /  引用流水账" if zh else
            "BEFORE  /  CITATION LIST", 17, CORAL, True)
        put(d, (62, 243), "01 → 02 → 03 → 04 → 05 → 06", 17, "#9EAFC7")
        for i in range(6):
            x = 62 + (i % 2) * 168
            y = 282 + (i // 2) * 60
            d.rounded_rectangle((x, y, x+150, y+45), radius=12,
                fill="#667F91" if stage >= 2 else "#32445D",
                outline="#586C88", width=1)
            put(d, (x+16, y+9), f"Paper {i+1:02}", 16, "#E4E9F4")
        d = card(im, (426, 187, 1040, 511), "#102F40", "#3B8491")
        put(d, (449, 205), "AFTER  /  机制驱动的比较" if zh else
            "AFTER  /  MECHANISM MAP", 17, CYAN, True)
        axis = ("共同比较轴：数据 | 目标函数 | 信息访问" if zh else
                "Shared axes: data | objective | information access")
        put(d, (451, 238), axis, 17, MUTE)
        groups = [
            ("路径 A · 固定数据", CYAN),
            ("路径 B · 生成数据", VIOLET),
        ] if zh else [
            ("FAMILY A · FIXED DATA", CYAN),
            ("FAMILY B · GENERATED DATA", VIOLET),
        ]
        for j, (label, color) in enumerate(groups):
            y = 284 + 97 * j
            active = stage >= j + 1
            d.rounded_rectangle((449, y, 1018, y+77), radius=16,
                fill="#194457" if active else "#1A3043",
                outline=color if active else "#33566B", width=2)
            put(d, (470, y+8), label, 18, color if active else "#7A98AE", True)
            if active:
                for k, x in enumerate((475, 646, 817)):
                    d.rounded_rectangle((x, y+38, x+136, y+64), radius=8,
                        fill="#245265", outline="#456F80", width=1)
                    put(d, (x+16, y+40), f"Study {j*3+k+1:02}", 14)
                if stage >= j+3:
                    halo(im, 990, y+34, color)
            else:
                put(d, (470, y+43), "—  —  —", 16, "#617C90")
        if stage >= 3:
            d.rounded_rectangle((450, 469, 1017, 505), radius=11,
                fill="#3E3446", outline=AMBER, width=2)
            put(d, (467, 476),
                "待验证的研究空白 ≠ “没有人做过”" if zh else
                'OPEN QUESTION ≠ "No prior work exists"',
                16, AMBER, True)
        put(d, (825, 540), f"{min(stage,4)}/4", 16, CYAN, True)
        frames.append(im)
    write(frames, f"demo-related-work-{language}.gif")


if __name__ == "__main__":
    for lang in ("zh", "en"):
        argument_demo(lang)
        related_work_demo(lang)
