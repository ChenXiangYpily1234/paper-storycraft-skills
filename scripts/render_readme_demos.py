#!/usr/bin/env python3
"""Render lightweight, illustrative GIFs for the bilingual READMEs.

Animations contain placeholders rather than experimental evidence.
Requires Pillow and Noto Sans CJK fonts; no network access at runtime.
"""
from pathlib import Path
import subprocess
from PIL import Image, ImageDraw, ImageFont

OUT = Path(__file__).resolve().parents[1] / 'assets'
OUT.mkdir(parents=True, exist_ok=True)

BG = '#0C1423'
CARD = '#172237'
CARD2 = '#11313B'
WHITE = '#EDF7FF'
MUTED = '#93A8BC'
ACCENT = '#5DE6BD'
LINE = '#344357'


def font(size, bold=False):
    family = 'Noto Sans CJK SC:style=Bold' if bold else 'Noto Sans CJK SC'
    path = subprocess.check_output(['fc-match', '-f', '%{file}', family], text=True).strip()
    return ImageFont.truetype(path, size)


def text(d, x, y, value, size=24, color=WHITE, bold=False):
    d.text((x, y), value, font=font(size, bold), fill=color, stroke_width=0)


def background(width, height, eyebrow, title, subtitle):
    im = Image.new('RGB', (width, height), BG)
    d = ImageDraw.Draw(im)
    for i in range(0, 17):
        d.rounded_rectangle(
            (width - 195 - i * 17, -170 + i * 12, width + 80, 165 + i * 8),
            radius=36, outline='#132A3B', width=1,
        )
    d.rounded_rectangle((40, 27, 190, 63), radius=16, fill='#193E44')
    text(d, 57, 33, eyebrow, 17, ACCENT, True)
    text(d, 40, 69, title, 37, WHITE, True)
    text(d, 42, 121, subtitle, 19, MUTED)
    return im, d


def save(frames, basename, durations):
    frames = [im.quantize(colors=64, method=Image.Quantize.MEDIANCUT) for im in frames]
    target = OUT / basename
    frames[0].save(
        target, save_all=True, append_images=frames[1:],
        duration=durations, disposal=2, optimize=True, loop=0,
    )
    print(target, f'{target.stat().st_size / 1024:.1f} KiB')


def argument_demo(lang):
    zh = lang == 'zh'
    title = '从流水账，到有证据的研究论证' if zh else 'From a list of claims to an evidence-led argument'
    subtitle = '演示内容均为占位符 · 请替换为真实论文信息' if zh else 'Illustrative placeholders only · replace with verified findings'
    left = [
        '我们提出三个模块 A、B、C。' if zh else 'We introduce modules A, B, and C.',
        '实验结果表明方法更好。' if zh else 'Our experiments show improvements.',
        '因此方法具有广泛适用性。' if zh else 'The approach generalizes broadly.',
    ]
    right = [
        ('问题', '[证据支持的具体研究缺口]') if zh else ('QUESTION', '[precise, sourced research gap]'),
        ('设计', 'A → B → C 的必要关系') if zh else ('DESIGN', 'why A → B → C is needed'),
        ('证据', '[对照 / 指标 / 真实结果]') if zh else ('EVIDENCE', '[baseline / metric / verified result]'),
        ('边界', '仅支持已测试场景') if zh else ('SCOPE', 'limited to evaluated settings'),
    ]
    frames = []
    for stage in [0, 1, 2, 3, 4, 4]:
        im, d = background(1080, 584, 'PAPER STORYCRAFT', title, subtitle)
        d.rounded_rectangle((40, 177, 516, 495), radius=22, fill=CARD)
        d.rounded_rectangle((535, 177, 1040, 495), radius=22, fill=CARD2)
        text(d, 67, 196, 'BEFORE' if not zh else '修改前  /  BEFORE', 18, '#FAA9A0', True)
        text(d, 563, 196, 'AFTER' if not zh else '修改后  /  AFTER', 18, ACCENT, True)
        d.line((66, 238, 490, 238), fill=LINE, width=2)
        d.line((562, 238, 1014, 238), fill='#2B5661', width=2)
        for i, line in enumerate(left):
            yy = 267 + i * 67
            d.rounded_rectangle((66, yy, 73, yy + 32), radius=3, fill='#B56669')
            text(d, 91, yy, line, 20 if not zh else 22, '#B6C2D3')
        for i, (tag, message) in enumerate(right):
            yy = 260 + i * 53
            unlocked = i < stage
            d.rounded_rectangle(
                (560, yy - 5, 1014, yy + 44), radius=10,
                fill='#1D5153' if unlocked and i == stage - 1 else '#173B44',
            )
            if unlocked:
                text(d, 575, yy + 1, tag, 16, ACCENT, True)
                text(d, 674 if zh else 690, yy + 1, message, 19 if zh else 17, WHITE)
            else:
                text(d, 578, yy + 3, f'{i + 1:02}', 16, '#64898E', True)
                text(d, 677, yy + 3, '— — — — — — —', 18, '#466E73')
        text(
            d, 41, 523,
            '问题  →  设计  →  证据  →  边界' if zh else 'QUESTION  →  DESIGN  →  EVIDENCE  →  SCOPE',
            20, ACCENT, True,
        )
        text(d, 880, 528, f'{min(stage, 4)}/4', 20, MUTED)
        for k in range(4):
            d.rounded_rectangle(
                (929 + k * 21, 540, 943 + k * 21, 549), radius=5,
                fill=ACCENT if k < stage else '#354C5B',
            )
        frames.append(im)
    save(frames, f'demo-argument-{lang}.gif', [650, 800, 800, 800, 1600, 950])


def citation_demo(lang):
    zh = lang == 'zh'
    title = '引用放在专名旁，不必全部挤到句末' if zh else 'Cite names where they appear — not only at sentence ends'
    subtitle = '示意引用位置，并非真实文献条目' if zh else 'Citation-position example only · not bibliographic records'
    labels = (
        (('方法 A', '[方法来源]'), ('模型 B', '[模型来源]'), ('数据集 C', '[数据来源]'))
        if zh else
        (('Method A', '[method source]'), ('Model B', '[model source]'), ('Dataset C', '[dataset source]'))
    )
    frames = []
    for stage in [0, 1, 2, 3, 3]:
        im, d = background(1080, 386, 'SOURCE FIRST', title, subtitle)
        d.rounded_rectangle((40, 176, 1040, 347), radius=20, fill=CARD)
        text(d, 65, 194, 'BEFORE' if not zh else '修改前', 17, '#FAA9A0', True)
        old = (
            '方法 A、模型 B 和数据集 C 的结果更好。[1–3]'
            if zh else 'Method A, Model B and Dataset C performed better. [1–3]'
        )
        text(d, 170, 192, old, 20, '#AEBBC9')
        d.line((65, 242, 1010, 242), fill=LINE, width=2)
        text(d, 65, 263, 'AFTER' if not zh else '修改后', 17, ACCENT, True)
        x = 170
        for i, (name, source) in enumerate(labels):
            if i < stage:
                segment = f'{name} {source}'
                color = ACCENT if i == stage - 1 else WHITE
            else:
                segment = f'{name} (...)'
                color = '#6E8799'
            text(d, x, 263, segment, 18 if zh else 17, color, i == stage - 1)
            x += 292 if zh else 290
        text(
            d, 65, 317,
            '对应来源与具体论断分别核验'
            if zh else 'Verify source attribution and each factual claim separately',
            16, MUTED,
        )
        frames.append(im)
    save(frames, f'demo-citation-{lang}.gif', [900, 1150, 1150, 1800, 900])


if __name__ == '__main__':
    for language in ('zh', 'en'):
        argument_demo(language)
        citation_demo(language)
