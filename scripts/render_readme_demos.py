#!/usr/bin/env python3
"""Render light, diagram-first README animations with actual object motion.

Requires Pillow and Noto Sans CJK SC, or STORYCRAFT_FONT_REGULAR and
STORYCRAFT_FONT_BOLD pointing to local font files. All examples are schematic:
paper labels, interval marks and moving tokens are not measured results.
"""
from functools import lru_cache
from pathlib import Path
import math
import os
import subprocess

from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / "assets"
W, H = 1200, 620
BG, INK, MUTED, FAINT = "#FFFFFF", "#273448", "#68778C", "#D9E1E9"
BLUE, TEAL, ORANGE, VIOLET = "#3C73C4", "#258C80", "#D98A3D", "#8761B2"
FPS = 12.5
TIMES = [0.0] + [1.2 + i / FPS for i in range(76)] + [7.3]
DURATIONS = [1200] + [80] * 76 + [2800]


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
            raise RuntimeError("Noto Sans CJK SC is missing; refusing to render missing glyphs.")
        path = match[1]
    return ImageFont.truetype(path, size)


def progress(t, start, end):
    value = min(1.0, max(0.0, (t-start)/(end-start)))
    return value * value * (3-2*value)


def mix(a, b, fraction):
    return a + (b-a)*fraction


def tint(color, alpha=1.0):
    rgb = tuple(int(color[i:i+2], 16) for i in (1, 3, 5))
    return tuple(round(255+(value-255)*alpha) for value in rgb)


def text(draw, xy, value, size=24, color=INK, bold=False, center=False, alpha=1.0, width=None):
    face = font(size, bold)
    value = str(value)
    length = draw.textlength(value, font=face)
    if width is not None and length > width:
        raise ValueError(f"Text exceeds {width}px: {value}")
    x, y = xy
    if center:
        x -= length/2
    draw.text((x, y), value, font=face, fill=tint(color, alpha), anchor="lt")


def line(draw, points, color=FAINT, width=3, alpha=1.0):
    draw.line(points, fill=tint(color, alpha), width=width, joint="curve")


def circle(draw, center, radius, color, alpha=1.0, fill=None, width=3):
    x, y = center
    draw.ellipse((x-radius, y-radius, x+radius, y+radius),
                 fill=tint(fill, alpha) if fill else None,
                 outline=tint(color, alpha), width=width)


def arrow(draw, start, end, amount=1.0, color=MUTED, alpha=1.0, width=3):
    if amount <= 0:
        return
    x1, y1 = start
    x2, y2 = (mix(x1, end[0], amount), mix(y1, end[1], amount))
    line(draw, (x1, y1, x2, y2), color, width, alpha)
    angle = math.atan2(y2-y1, x2-x1)
    points = [(x2-12*math.cos(angle-offset), y2-12*math.sin(angle-offset))
              for offset in (-0.45, 0.45)]
    line(draw, (*points[0], x2, y2, *points[1]), color, width, alpha)


def base(title, subtitle, zh):
    image = Image.new("RGB", (W, H), BG)
    draw = ImageDraw.Draw(image)
    text(draw, (54, 40), title, 36, INK, True, width=1092)
    text(draw, (54, 99), subtitle, 24, MUTED, width=1092)
    text(draw, (54, 589), "PAPER STORYCRAFT", 15, MUTED, True)
    note = "写作示意 · 不含真实实验结果" if zh else "ILLUSTRATIVE · NO REAL EXPERIMENTAL RESULTS"
    text(draw, (W-54-draw.textlength(note, font=font(15)), 589), note, 15, MUTED)
    return image, draw


def paper(image, cx, cy, label, color=BLUE, angle=0, scale=1.0, alpha=1.0):
    """A recognizable paper glyph, not a UI card."""
    if alpha <= 0:
        return
    glyph = Image.new("RGBA", (120, 148), (255, 255, 255, 0))
    d = ImageDraw.Draw(glyph)
    edge = tint(color, alpha)
    polygon = [(25, 17), (79, 17), (99, 37), (99, 124), (25, 124), (25, 17)]
    d.polygon(polygon, fill=(255, 255, 255, round(255*alpha)))
    d.line(polygon, fill=edge, width=3, joint="curve")
    d.line((79, 17, 79, 37, 99, 37), fill=edge, width=2)
    for y, stop in ((80, 85), (93, 80), (106, 87)):
        d.line((38, y, stop, y), fill=tint(FAINT, alpha), width=3)
    text(d, (61, 48), label, 22, color, True, center=True, alpha=alpha, width=72)
    if scale != 1.0:
        glyph = glyph.resize((round(120*scale), round(148*scale)), Image.Resampling.LANCZOS)
    if angle:
        glyph = glyph.rotate(angle, Image.Resampling.BICUBIC, expand=True)
    image.paste(glyph, (round(cx-glyph.width/2), round(cy-glyph.height/2)), glyph)


def balance(draw, cx, cy, alpha=1.0, tilt=0.0, color=TEAL):
    line(draw, (cx, cy-42, cx, cy+42), color, 4, alpha)
    line(draw, (cx-35, cy+42, cx+35, cy+42), color, 4, alpha)
    line(draw, (cx-65, cy-28+tilt, cx+65, cy-28-tilt), color, 4, alpha)
    circle(draw, (cx, cy-28), 6, color, alpha, fill=color, width=1)
    for direction in (-1, 1):
        x = cx+direction*51
        y = cy-28-direction*tilt
        line(draw, (x, y, x-24, y+48, x+24, y+48, x, y), color, 2, alpha)
        line(draw, (x-24, y+48, x+24, y+48), color, 4, alpha)


def methods(zh, t):
    title = "Methods｜从模块清单到论证链" if zh else "Methods | From a module list to an argument"
    subtitle = "把“为什么、怎么做、凭什么”连起来。" if zh else "Connect why it is needed, how it works and what supports it."
    image, draw = base(title, subtitle, zh)
    change = progress(t, 1.2, 3.2)
    reveal = progress(t, 2.1, 3.1)
    xs, y = (170, 455, 740, 1025), 278

    # Components visibly converge into the method; the argument grows around it.
    for x, color in zip(xs, (ORANGE, BLUE, TEAL, VIOLET)):
        circle(draw, (x, y), 61, color, reveal, fill="#FAFBFD")
    text(draw, (170, 243), "?", 65, ORANGE, True, center=True, alpha=reveal)
    balance(draw, 740, y+3, reveal)
    line(draw, (992, y-35, 978, y-35, 978, y+35, 992, y+35), VIOLET, 4, reveal)
    line(draw, (1058, y-35, 1072, y-35, 1072, y+35, 1058, y+35), VIOLET, 4, reveal)
    for dx, dy in ((-18, 13), (0, -10), (19, 16)):
        circle(draw, (1025+dx, y+dy), 5, VIOLET, reveal, fill=VIOLET, width=1)

    starts = ((300, 250), (600, 312), (900, 235))
    for i, label in enumerate("ABC"):
        sx, sy = starts[i]
        x = mix(sx, 420+i*35, change)
        py = mix(sy, y, change)
        side = mix(94, 27, change)
        draw.rectangle((x-side/2, py-side/2, x+side/2, py+side/2),
                       fill=tint("#E9F0FB"), outline=tint(BLUE), width=2)
        text(draw, (x, py-mix(18, 8, change)), label, round(mix(36, 16, change)), BLUE, True, center=True)
    if change < 1:
        text(draw, (600, 443), "只有 A、B、C，还看不出研究逻辑。" if zh else
             "A + B + C does not explain the research logic.", 28, MUTED,
             center=True, alpha=1-change, width=1092)

    labels = ("问题", "方法", "证据", "边界") if zh else ("Problem", "Method", "Evidence", "Scope")
    notes = (
        ("具体困难是什么？", ""),
        ("输入 → 操作 → 输出", "交代输出的下游用途"),
        ("公平对照", "指标与不确定性"),
        ("结论限于", "已验证的条件"),
    ) if zh else (
        ("What is the difficulty?", ""),
        ("Input → operation → output", "Show how the output is used"),
        ("Matched controls", "Metrics and uncertainty"),
        ("Limit the conclusion", "to tested conditions"),
    )
    for x, label, note, color in zip(xs, labels, notes, (ORANGE, BLUE, TEAL, VIOLET)):
        text(draw, (x, 367), label, 30, color, True, True, reveal, 255)
        for j, value in enumerate(note):
            text(draw, (x, 416+j*35), value, 23 if zh else 18, INK, center=True, alpha=reveal, width=265)
    for i in range(3):
        arrow(draw, (xs[i]+76, y), (xs[i+1]-76, y),
              progress(t, 3.05+i*0.5, 3.55+i*0.5), MUTED)
    if 4.7 < t < 6.9:
        travel = progress(t, 4.7, 6.9)
        x = mix(xs[0], xs[-1], travel)
        circle(draw, (x, y-95), 8, ORANGE, fill=ORANGE, width=1)
        line(draw, (xs[0], y-95, x, y-95), ORANGE, 2, 0.35)
    text(draw, (600, 530), "模块是方法的一部分，论证还需要问题、证据和边界。" if zh else
         "Modules belong inside a method. The argument also needs evidence and scope.",
         24, INK, center=True, alpha=progress(t, 5.1, 5.8), width=1092)
    return image


def literature(zh, t):
    title = "Related Work｜从文献清单到机制比较" if zh else "Related Work | Group papers, then compare"
    subtitle = "先按机制归组，再用同一把尺子比较。" if zh else "Group by mechanism, then compare on the same dimensions."
    image, draw = base(title, subtitle, zh)
    colors = (BLUE, TEAL)
    starts = ((190, 245, -12), (355, 310, 10), (520, 235, -8),
              (685, 305, 12), (850, 225, -10), (1015, 290, 8))
    label_alpha = progress(t, 1.8, 3.2)
    for group, x in enumerate((345, 855)):
        label = ("固定数据", "生成数据")[group] if zh else ("Fixed data", "Generated data")[group]
        text(draw, (x, 173), label, 28, colors[group], True, True, label_alpha, 450)
    for i, (sx, sy, angle) in enumerate(starts):
        moving = progress(t, 1.2+i*0.09, 2.8+i*0.09)
        group, within = divmod(i, 3)
        x = mix(sx, 240+group*510+within*105, moving)
        y = mix(sy, 275, moving)
        paper(image, x, y, f"P{i+1:02}", colors[group], angle*(1-moving))
    draw = ImageDraw.Draw(image)
    # Brackets and converging arrows make the grouping and common comparison explicit.
    for x, color in zip((345, 855), colors):
        alpha = progress(t, 3.15, 3.6)
        line(draw, (x-155, 353, x-155, 366, x+155, 366, x+155, 353), color, 3, alpha)
        arrow(draw, (x, 380), (600+(x-600)*0.25, 432), progress(t, 3.6, 4.3), color)
    compare_alpha = progress(t, 3.9, 4.6)
    fields = ("数据", "目标", "信息访问", "评测 / 预算") if zh else ("Data", "Objective", "Access", "Protocol / cost")
    for i, value in enumerate(fields):
        x = 250+i*235
        text(draw, (x, 462), value, 25 if zh else 23, INK, True, True, compare_alpha, 220)
        line(draw, (x-65, 505, x+65, 505), BLUE if i % 2 == 0 else TEAL, 3, compare_alpha)
    # The magnifying glass scans both families, then stops over a possible counterexample.
    lens_alpha = progress(t, 4.8, 5.1)
    lx = mix(450, 960, progress(t, 5.1, 6.5))
    ly = 253
    circle(draw, (lx, ly), 41, ORANGE, lens_alpha, width=4)
    line(draw, (lx+30, ly+30, lx+57, ly+57), ORANGE, 7, lens_alpha)
    text(draw, (600, 540), "核对最强前人工作；研究空白仍需验证。" if zh else
         "Check the strongest prior work. A gap still needs verification.",
         25, ORANGE, True, True, progress(t, 5.8, 6.5), 1092)
    # Stable identities and explicit placeholders prevent fake bibliography claims.
    text(draw, (600, 140), "P01–P06：文献占位符" if zh else "P01–P06: paper placeholders",
         17, MUTED, center=True)
    return image


def experiments(zh, t):
    title = "Experiments｜从成绩播报到有依据的结论" if zh else "Experiments | Turn a result into a supported claim"
    subtitle = "先对齐比较条件，再看差异，最后限定结论。" if zh else "Match the comparison, show the difference, then bound the claim."
    image, draw = base(title, subtitle, zh)
    xs, y = (215, 600, 985), 295
    # The unsupported phrase physically gives way to the conditions it omitted.
    initial = 1-progress(t, 1.2, 2.2)
    text(draw, (600, 206-55*(1-initial)), "“显著更好！”" if zh else '“Significantly better!”',
         39, ORANGE, True, True, initial, 1092)
    fairness = progress(t, 1.2, 2.7)
    balance(draw, xs[0], y+2, fairness, tilt=24*(1-fairness), color=BLUE)
    # Two study sheets slide into alignment before any comparison is interpreted.
    paper(image, mix(95, 164, fairness), mix(250, 231, fairness), "A", BLUE,
          angle=-10*(1-fairness), scale=0.47, alpha=fairness)
    paper(image, mix(325, 266, fairness), mix(185, 231, fairness), "B", BLUE,
          angle=10*(1-fairness), scale=0.47, alpha=fairness)
    draw = ImageDraw.Draw(image)
    observed = progress(t, 2.9, 4.2)
    span = 82*observed
    line(draw, (xs[1]-span, y, xs[1]+span, y), TEAL, 4, observed)
    for x in (xs[1]-span, xs[1]+span):
        line(draw, (x, y-19, x, y+19), TEAL, 3, observed)
    circle(draw, (xs[1], y), 10, TEAL, observed, fill=TEAL, width=1)
    text(draw, (xs[1], 221), "差异与不确定性" if zh else "Effect + uncertainty",
         23, TEAL, center=True, alpha=observed, width=280)
    scope = progress(t, 4.2, 5.6)
    left, right = xs[2]-78, xs[2]+78
    line(draw, (left+18, y-55, left, y-55, left, y+55, left+18, y+55), VIOLET, 4, scope)
    line(draw, (right-18, y-55, right, y-55, right, y+55, right-18, y+55), VIOLET, 4, scope)
    text(draw, (xs[2], y-12), "已测试" if zh else "TESTED", 26, VIOLET, True, True, scope, 142)
    for x in (left-32, right+32):
        text(draw, (x, y-70), "?", 26, MUTED, center=True, alpha=scope)
    for i, (start, end) in enumerate(((2.7, 3.3), (4.0, 4.8))):
        arrow(draw, (xs[i]+105, y), (xs[i+1]-115, y), progress(t, start, end))
    labels = ("公平比较", "真实差异", "结论范围") if zh else ("Fair comparison", "Actual difference", "Bounded claim")
    notes = (
        ("同协议 · 可比信息与预算", ""),
        ("[真实差异] + [可用不确定性]", ""),
        ("已测条件能支持什么？", "未测条件不外推"),
    ) if zh else (
        ("Matched protocol, access and budget", ""),
        ("[Effect] + [available uncertainty]", ""),
        ("What do tested conditions support?", "Do not extrapolate to untested settings"),
    )
    for x, label, note, color, alpha in zip(xs, labels, notes, (BLUE, TEAL, VIOLET), (fairness, observed, scope)):
        text(draw, (x, 392), label, 29 if zh else 27, color, True, True, alpha, 335)
        for j, value in enumerate(note):
            text(draw, (x, 441+j*32), value, 21 if zh else 17, INK, center=True, alpha=alpha, width=350)
    if 5.5 < t < 6.8:
        x = mix(xs[0]+100, xs[-1]-100, progress(t, 5.5, 6.8))
        circle(draw, (x, y+65), 7, ORANGE, fill=ORANGE, width=1)
    text(draw, (600, 540), "关键反证留在正文；次要细节可入附录。" if zh else
         "Disclose claim-changing evidence in the main text; retain secondary details.",
         24, INK, center=True, alpha=progress(t, 5.8, 6.6), width=1092)
    return image


def write(frames, stem):
    OUT.mkdir(parents=True, exist_ok=True)
    # A shared palette and retained unchanged pixels keep moving diagrams compact.
    sample = Image.new("RGB", (W, H*3))
    for row, index in enumerate((0, len(frames)//2, len(frames)-1)):
        sample.paste(frames[index], (0, row*H))
    palette = sample.quantize(colors=96, method=Image.Quantize.MEDIANCUT)
    indexed = [frame.quantize(palette=palette, dither=Image.Dither.NONE) for frame in frames]
    gif, png = OUT / f"{stem}.gif", OUT / f"{stem}.png"
    indexed[0].save(gif, save_all=True, append_images=indexed[1:],
                    duration=DURATIONS, loop=0, disposal=1, optimize=True)
    frames[-1].save(png, optimize=True)
    print(f"{stem}: {gif.stat().st_size / 1024:.1f} KiB GIF; "
          f"{png.stat().st_size / 1024:.1f} KiB PNG")
    if gif.stat().st_size >= 900_000:
        raise ValueError(f"Animation exceeds the 900 kB README budget: {gif}")


if __name__ == "__main__":
    for language in ("zh", "en"):
        for topic, render in (("argument", methods), ("related-work", literature), ("experiments", experiments)):
            write([render(language == "zh", t) for t in TIMES], f"demo-{topic}-{language}")
