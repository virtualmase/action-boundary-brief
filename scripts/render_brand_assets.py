#!/usr/bin/env python3
"""Render exact static PNG icon and social assets for the Action Boundary Brief."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent.parent
PAPER, INK, COBALT, RUST = '#f4f2e9', '#17202a', '#1746c8', '#ce6545'
SERIF = '/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf'
SANS = '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf'
MONO = '/usr/share/fonts/truetype/dejavu/DejaVuSansMono.ttf'

def font(path, size): return ImageFont.truetype(path, size=size)
def icon(size, path):
    image = Image.new('RGB', (size, size), COBALT); draw = ImageDraw.Draw(image)
    pad, stroke = int(size*.14), max(3, int(size*.075)); y = size//2
    draw.line((pad, y, int(size*.43), y), fill=PAPER, width=stroke)
    draw.line((int(size*.57), y, size-pad, y), fill=PAPER, width=stroke)
    gate = int(size*.18); draw.rectangle((pad, y-gate//2, pad+gate, y+gate//2), fill=PAPER)
    draw.ellipse((int(size*.43), y-gate//2, int(size*.57), y+gate//2), fill=PAPER)
    draw.rectangle((size-pad-gate, y-gate//2, size-pad, y+gate//2), fill=RUST)
    image.save(path, optimize=True)
def og(path):
    image = Image.new('RGB', (1200, 630), PAPER); draw = ImageDraw.Draw(image)
    draw.line((0, 126, 1200, 126), fill='#c3c8c5', width=2); draw.line((95, 0, 95, 630), fill='#c3c8c5', width=2)
    draw.text((95, 84), 'ACTION BOUNDARY BRIEF  /  OPEN-SOURCE SKILL', font=font(MONO, 24), fill=INK)
    draw.text((95, 202), 'Before an AI system acts,', font=font(SERIF, 67), fill=INK)
    draw.text((95, 286), 'name the boundary.', font=font(SERIF, 72), fill=COBALT)
    draw.rectangle((95, 412, 555, 417), fill=RUST)
    y = 515; draw.line((590, y, 1080, y), fill=COBALT, width=5)
    labels = ['INTENT', 'RESOURCE', 'RIGHT', 'PAUSE', 'RECORD']
    for index, label in enumerate(labels):
        x = 600 + index*100; fill = COBALT if index == 2 else PAPER
        draw.rectangle((x, y-37, x+70, y+33), fill=fill, outline=INK, width=3)
        draw.text((x+35, y-6), label, font=font(MONO, 10), anchor='mm', fill=PAPER if index == 2 else INK)
    image.save(path, optimize=True)
for size in (48, 180, 192, 512): icon(size, ROOT / f'favicon-{size}.png')
og(ROOT / 'og-image.png')
