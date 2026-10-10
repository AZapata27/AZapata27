"""Builds the sheets under the hero: numbered notes, the parts list (stack) and the language selector.

Usage:  python .readme/build_sheets.py      (assets/notes*.svg, parts*.svg, lang-*.svg; en and es)
"""
import os
import re

from typeset import GlyphBank, wrap
from content import TEXT, suffix
from build_hero import t, save, bubble, DEFS, BOLD, SEMI, MED, MONO, MONO_B, SHEET, INK, SOFT, BUS, HERE

LOGOS = os.path.join(HERE, "logos")
# Marks drawn small or wide in their source files, scaled so every logo reads at the same visual size.
OPTICAL = {"oracle": 0.86, "amazonwebservices": 1.1, "camel": 0.92}
_logo_n = [0]


def sheet(w, h, body, bank, title, desc):
    """Same drafting sheet as the hero, without zone marks."""
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" '
            f'height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d"><title id="t">{title}</title>'
            f'<desc id="d">{desc}</desc><defs>{DEFS}{bank.defs()}</defs>'
            f'<rect width="{w}" height="{h}" fill="{SHEET}"/>'
            f'<rect x="28" y="28" width="{w - 56}" height="{h - 56}" fill="url(#grid)"/>'
            f'<rect x="14" y="14" width="{w - 28}" height="{h - 28}" fill="none" stroke="{INK}" stroke-width="1.2"/>'
            f'<rect x="28" y="28" width="{w - 56}" height="{h - 56}" fill="none" stroke="{INK}" stroke-width="2.4"/>'
            f'{body}</svg>\n')


def logo(name, x, y, size):
    """Brand mark (devicon MIT, simple-icons CC0, official Apache Camel) nested with prefixed ids."""
    k = OPTICAL.get(name, 1.0)
    x, y, size = x + size * (1 - k) / 2, y + size * (1 - k) / 2, size * k
    src = open(os.path.join(LOGOS, name + ".svg"), encoding="utf-8").read()
    root = re.search(r"<svg[^>]*>", src, re.S).group(0)
    vb = re.search(r'viewBox="([^"]+)"', root).group(1)
    fill = re.search(r'\sfill="([^"]+)"', root)
    body = re.sub(r"<\?xml.*?\?>", "", src)
    body = re.sub(r"^.*?<svg[^>]*>", "", body, flags=re.S)
    body = re.sub(r"</svg>\s*$", "", body.strip())
    body = re.sub(r"<title>.*?</title>", "", body)
    _logo_n[0] += 1
    pre = f"L{_logo_n[0]}"
    body = re.sub(r'id="([^"]+)"', lambda m: f'id="{pre}{m.group(1)}"', body)
    body = re.sub(r"url\(#([^)]+)\)", lambda m: f"url(#{pre}{m.group(1)})", body)
    body = re.sub(r'href="#([^"]+)"', lambda m: f'href="#{pre}{m.group(1)}"', body)
    f = f' fill="{fill.group(1)}"' if fill else ""
    return f'<svg x="{x:.1f}" y="{y:.1f}" width="{size:.1f}" height="{size:.1f}" viewBox="{vb}"{f}>{body}</svg>'


# ---------------------------------------------------------------- notes
def notes(lang, mobile=False):
    T = TEXT[lang]
    W = 800 if mobile else 1200
    bank = GlyphBank("nm" if mobile else "n")
    out = [t(bank, BOLD, T["notes_title"], 56, 108 if mobile else 96, 64 if mobile else 48, INK, tracking=1),
           f'<path d="M56 {130 if mobile else 116}H{W - 56}" stroke="{INK}" stroke-width="2"/>']
    size = 27 if mobile else 19
    lh = size * 1.45
    if mobile:
        cols, col_w, gap = 1, W - 112 - 56, 0
    else:
        cols, col_w, gap = 2, (W - 112 - 60) / 2 - 50, 60
    y_col = [180 if mobile else 168] * cols
    for i, (n, title, body) in enumerate(T["notes"]):
        c = 0 if mobile else i % 2
        # Rows stay aligned across both columns whatever the language makes each note's length.
        if not mobile and c == 0:
            y_col = [max(y_col)] * cols
        x = 56 + c * (col_w + 50 + gap)
        y = y_col[c]
        color = BUS if n == 4 else INK
        out.append(bubble(bank, n, x + 18, y - 9, r=18 if mobile else 15, color=color))
        out.append(t(bank, BOLD, title, x + 50, y, size * 1.15, color, tracking=0.8))
        y += lh * 1.25
        for line in wrap(MED, body, size, col_w):
            out.append(t(bank, MED, line, x + 50, y, size, INK))
            y += lh
        y_col[c] = y + (40 if mobile else 30)
    H = int(max(y_col)) + 30
    desc = T["notes_desc_prefix"] + " " + " ".join(f"{n}. {title}: {body}" for n, title, body in T["notes"])
    name = f"notes{'-mobile' if mobile else ''}{suffix(lang)}.svg"
    save(name, sheet(W, H, "".join(out), bank, T["notes_title"].title(), desc))


# ---------------------------------------------------------------- parts list (the stack)
def parts(lang, mobile=False):
    T = TEXT[lang]
    W = 800 if mobile else 1200
    bank = GlyphBank("pm" if mobile else "p")
    out = [t(bank, BOLD, T["parts_title"], 56, 108 if mobile else 96, 64 if mobile else 48, INK, tracking=1)]
    top = 130 if mobile else 116
    out.append(f'<path d="M56 {top}H{W - 56}" stroke="{INK}" stroke-width="2"/>')
    y = top
    if not mobile:
        item, group, partsl = T["parts_cols"]
        out.append(t(bank, SEMI, item, 66, y + 26, 14, SOFT, tracking=1.2))
        out.append(t(bank, SEMI, group, 130, y + 26, 14, SOFT, tracking=1.2))
        out.append(t(bank, SEMI, partsl, 360, y + 26, 14, SOFT, tracking=1.2))
        y += 40
        out.append(f'<path d="M56 {y}H{W - 56}" stroke="{INK}" stroke-width="1.2"/>')
    for i, (label, names, caption) in enumerate(T["stack"]):
        if mobile:
            y += 46
            out.append(t(bank, MONO_B, f"{i + 1:02d}", 56, y, 22, SOFT))
            out.append(t(bank, BOLD, label, 110, y, 30, INK, tracking=0.8))
            y += 24
            rows = -(-len(names) // 8)
            per = -(-len(names) // rows)
            for j, n in enumerate(names):
                out.append(logo(n, 56 + (j % per) * 80, y + (j // per) * 80, 60))
            y += rows * 80 + 20
            lines = wrap(MONO, caption, 18, W - 112)
            for k, line in enumerate(lines):
                out.append(t(bank, MONO, line, 56, y + k * 28, 18, SOFT))
            y += (len(lines) - 1) * 28 + 26
        else:
            y0 = y
            y += 18
            out.append(t(bank, MONO_B, f"{i + 1:02d}", 66, y + 28, 16, SOFT))
            out.append(t(bank, BOLD, label, 130, y + 30, 22, INK, tracking=0.8))
            for j, n in enumerate(names):
                out.append(logo(n, 360 + j * 62, y, 44))
            lines = wrap(MONO, caption, 13.5, W - 360 - 70)
            for k, line in enumerate(lines):
                out.append(t(bank, MONO, line, 360, y + 70 + k * 20, 13.5, SOFT))
            y += 70 + (len(lines) - 1) * 20 + 22
            out.append(f'<path d="M110 {y0}V{y}M340 {y0}V{y}" stroke="{INK}" stroke-width="1"/>')
        out.append(f'<path d="M56 {y}H{W - 56}" stroke="{INK}" stroke-width="1"/>')
    H = int(y) + 50
    desc = T["parts_desc_prefix"] + " " + " ".join(f"{l.title()}: {c}." for l, _, c in T["stack"])
    name = f"parts{'-mobile' if mobile else ''}{suffix(lang)}.svg"
    save(name, sheet(W, H, "".join(out), bank, T["parts_title"].title(), desc))


# ---------------------------------------------------------------- language selector
def lang_tab(name, label, active):
    """One half of the EN | ES switch: the current language is inked, the other is a drawn outline."""
    bank = GlyphBank("s")
    size = 26
    w = int(MONO_B.width(label, size)) + 64
    h = 68
    fill = INK if active else SHEET
    fg = SHEET if active else INK
    mark = (f'<rect x="20" y="{h / 2 - 5}" width="10" height="10" fill="{fg}"/>' if active else
            f'<rect x="20.5" y="{h / 2 - 4.5}" width="9" height="9" fill="none" stroke="{fg}" stroke-width="2"/>')
    body = (f'<rect width="{w}" height="{h}" fill="{SHEET}"/>'
            f'<rect x="3" y="3" width="{w - 6}" height="{h - 6}" fill="{fill}" stroke="{INK}" stroke-width="3"/>'
            + mark + t(bank, MONO_B, label, 42, h / 2 + 9.5, size, fg))
    save(name, f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
               f'aria-label="{label}"><defs>{bank.defs()}</defs>{body}</svg>\n')


if __name__ == "__main__":
    for lang in TEXT:
        for m in (False, True):
            notes(lang, m)
            parts(lang, m)
    lang_tab("lang-en.svg", "English", True)
    lang_tab("lang-en-off.svg", "English", False)
    lang_tab("lang-es.svg", "Español", True)
    lang_tab("lang-es-off.svg", "Español", False)
