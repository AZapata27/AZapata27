"""Builds the profile hero: an Enterprise Integration Patterns route drawing.

The visitor's problem enters an inbound channel, a content-based router sends it to architecture, integration
or AI-native development, an aggregator joins the branches and the result leaves for production. Leadership
and training run as the control bus. Drafting-sheet conventions: border with zone marks, callout bubbles keyed
to the numbered notes, a code detail and a title block that also carries contact and links.

Usage:  python .readme/fetch_fonts.py && python .readme/build_hero.py      (assets/hero*.svg, link-*.svg; en and es)
        STATIC=1 OUT=/tmp/out python .readme/build_hero.py                 (no motion, for review captures)
"""
import os

from typeset import Face, GlyphBank, wrap
from content import TEXT, suffix

HERE = os.path.dirname(os.path.abspath(__file__))
FONTS = os.path.join(HERE, "fonts")
OUT = os.environ.get("OUT") or os.path.join(os.path.dirname(HERE), "assets")
STATIC = bool(os.environ.get("STATIC"))

SHEET = "#FAFAF7"
INK = "#151515"
SOFT = "#4A4F55"       # secondary lettering (contrast > 7:1 on the sheet)
AMBER = "#F2A900"      # messages in flight; the contact row
AMBER_TEXT = "#8A5A00"
BUS = "#1F5FBF"        # control bus; links

BOLD = Face(os.path.join(FONTS, "BarlowCondensed-Bold.ttf"))
SEMI = Face(os.path.join(FONTS, "BarlowCondensed-SemiBold.ttf"))
MED = Face(os.path.join(FONTS, "BarlowCondensed-Medium.ttf"))
MONO = Face(os.path.join(FONTS, "JetBrainsMono[wght].ttf"), {"wght": 500})
MONO_B = Face(os.path.join(FONTS, "JetBrainsMono[wght].ttf"), {"wght": 700})

DEFS = """
  <marker id="arrow" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse">
    <path d="M0 0L10 5L0 10z" fill="#151515"/>
  </marker>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <circle cx="0.8" cy="0.8" r="0.8" fill="#D6D8D4"/>
  </pattern>"""


def t(bank, face, s, x, y, size, color=INK, anchor="start", tracking=0.0):
    return f'<g fill="{color}">{face.uses(bank, s, x, y, size, tracking, anchor)}</g>'


def sheet(w, h, body, bank, title, desc):
    frame = (f'<rect x="14" y="14" width="{w - 28}" height="{h - 28}" fill="none" stroke="{INK}" stroke-width="1.2"/>'
             f'<rect x="28" y="28" width="{w - 56}" height="{h - 56}" fill="none" stroke="{INK}" stroke-width="2.4"/>')
    marks = ""
    cols = max(2, round((w - 56) / 200))
    rows = max(2, round((h - 56) / 180))
    for i in range(cols):
        cx = 28 + (w - 56) * (i + 0.5) / cols
        marks += t(bank, SEMI, str(i + 1), cx, 25, 11, SOFT, "middle") + t(bank, SEMI, str(i + 1), cx, h - 17, 11, SOFT, "middle")
        if i:
            x = 28 + (w - 56) * i / cols
            marks += f'<path d="M{x:.1f} 14V28M{x:.1f} {h - 28}V{h - 14}" stroke="{INK}" stroke-width="1"/>'
    for j in range(rows):
        cy = 28 + (h - 56) * (j + 0.5) / rows + 4
        letter = "ABCDEFGHJK"[j]
        marks += t(bank, SEMI, letter, 21, cy, 11, SOFT, "middle") + t(bank, SEMI, letter, w - 21, cy, 11, SOFT, "middle")
        if j:
            y = 28 + (h - 56) * j / rows
            marks += f'<path d="M14 {y:.1f}H28M{w - 28} {y:.1f}H{w - 14}" stroke="{INK}" stroke-width="1"/>'
    return (f'<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="{w}" '
            f'height="{h}" viewBox="0 0 {w} {h}" role="img" aria-labelledby="t d"><title id="t">{title}</title>'
            f'<desc id="d">{desc}</desc><defs>{DEFS}{bank.defs()}</defs>'
            f'<rect width="{w}" height="{h}" fill="{SHEET}"/>'
            f'<rect x="28" y="28" width="{w - 56}" height="{h - 56}" fill="url(#grid)"/>{frame}{marks}{body}</svg>\n')


def save(name, svg):
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(svg)
    print(f"{name}: {len(svg.encode()) / 1024:.0f} KB")


# ---------------------------------------------------------------- EIP symbols (Hohpe & Woolf notation)
def pipe(x, y, w, h=28, vertical=False):
    """Message channel: a pipe with an open end."""
    if vertical:
        return (f'<rect x="{x - h / 2}" y="{y}" width="{h}" height="{w}" rx="{h / 2}" fill="{SHEET}" stroke="{INK}" stroke-width="2"/>'
                f'<ellipse cx="{x}" cy="{y + h / 2}" rx="{h / 2}" ry="{h / 4}" fill="none" stroke="{INK}" stroke-width="1.4"/>')
    return (f'<rect x="{x}" y="{y - h / 2}" width="{w}" height="{h}" rx="{h / 2}" fill="{SHEET}" stroke="{INK}" stroke-width="2"/>'
            f'<ellipse cx="{x + h / 2}" cy="{y}" rx="{h / 4}" ry="{h / 2}" fill="none" stroke="{INK}" stroke-width="1.4"/>')


def router(cx, cy, s=70, vertical=False):
    h = s / 2
    box = f'<rect x="{cx - h}" y="{cy - h}" width="{s}" height="{s}" fill="{SHEET}" stroke="{INK}" stroke-width="2.4"/>'
    if vertical:
        lines = (f'M{cx} {cy - h + 8}V{cy - 4}M{cx} {cy - 4}L{cx - h + 10} {cy + h - 8}M{cx} {cy - 4}V{cy + h - 8}'
                 f'M{cx} {cy - 4}L{cx + h - 10} {cy + h - 8}')
        dot = f'<circle cx="{cx}" cy="{cy - 4}" r="3.5" fill="{INK}"/>'
    else:
        lines = (f'M{cx - h + 8} {cy}H{cx - 4}M{cx - 4} {cy}L{cx + h - 8} {cy - h + 10}M{cx - 4} {cy}H{cx + h - 8}'
                 f'M{cx - 4} {cy}L{cx + h - 8} {cy + h - 10}')
        dot = f'<circle cx="{cx - 4}" cy="{cy}" r="3.5" fill="{INK}"/>'
    return box + f'<path d="{lines}" stroke="{INK}" stroke-width="2" fill="none"/>' + dot


def aggregator(cx, cy, s=70, vertical=False):
    h = s / 2
    box = f'<rect x="{cx - h}" y="{cy - h}" width="{s}" height="{s}" fill="{SHEET}" stroke="{INK}" stroke-width="2.4"/>'
    if vertical:
        lines = (f'M{cx - h + 10} {cy - h + 8}L{cx} {cy + 4}M{cx} {cy - h + 8}V{cy + 4}M{cx + h - 10} {cy - h + 8}L{cx} {cy + 4}'
                 f'M{cx} {cy + 4}V{cy + h - 8}')
    else:
        lines = (f'M{cx - h + 8} {cy - h + 10}L{cx + 4} {cy}M{cx - h + 8} {cy}H{cx + 4}M{cx - h + 8} {cy + h - 10}L{cx + 4} {cy}'
                 f'M{cx + 4} {cy}H{cx + h - 8}')
    return box + f'<path d="{lines}" stroke="{INK}" stroke-width="2" fill="none"/>'


def glyph(kind, x, y, s=40):
    """Small notation glyph inside a processor box."""
    st = f'stroke="{INK}" stroke-width="1.8" fill="none"'
    if kind == "translator":   # Message Translator: one shape in, another out
        return (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" {st}/>'
                f'<path d="M{x + 7} {y + 12}h10v10h-10zM{x + s - 7} {y + s - 12}l-6 -11l-6 11z" {st}/>'
                f'<path d="M{x + 20} {y + 20}L{x + 26} {y + 20}" {st} marker-end="url(#arrow)"/>')
    if kind == "route":        # Pipes and Filters: filters chained on a pipe
        return (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" {st}/>'
                f'<path d="M{x + 4} {y + s / 2}H{x + s - 4}" {st}/>'
                f'<rect x="{x + 8}" y="{y + s / 2 - 6}" width="9" height="12" fill="{INK}"/>'
                f'<rect x="{x + 23}" y="{y + s / 2 - 6}" width="9" height="12" fill="{INK}"/>')
    # Agent: an endpoint that calls tools (MCP) in a loop
    return (f'<rect x="{x}" y="{y}" width="{s}" height="{s}" {st}/>'
            f'<circle cx="{x + s / 2}" cy="{y + s / 2}" r="7" fill="{INK}"/>'
            f'<path d="M{x + s / 2} {y + 6}A{s / 2 - 6} {s / 2 - 6} 0 1 1 {x + 7} {y + s / 2}" {st} marker-end="url(#arrow)"/>')


def bubble(bank, n, cx, cy, r=13, color=INK):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{SHEET}" stroke="{color}" stroke-width="1.8"/>'
            + t(bank, BOLD, str(n), cx, cy + r * 0.42, r * 1.25, color, "middle"))


def tokens(paths, dur=6.0):
    if STATIC:
        return ""
    out = []
    for i, d in enumerate(paths):
        begin = i * dur / len(paths)
        out.append(f'<g><rect x="-8" y="-6" width="16" height="12" rx="2" fill="{AMBER}" stroke="{INK}" stroke-width="1"/>'
                   f'<path d="M-8 -6L0 1L8 -6" stroke="{INK}" stroke-width="1" fill="none"/>'
                   f'<animateMotion path="{d}" dur="{dur}s" begin="{begin:.2f}s" repeatCount="indefinite"/></g>')
    return "".join(out)


CODE = [
    [("from", INK), ("(", INK), ('"inbound:your-problem"', AMBER_TEXT), (")", INK)],
    [("    .choice()", INK)],
    [("        .when(needs(", INK), ('"architecture"', AMBER_TEXT), (")).to(", INK), ('"design:cloud-native"', AMBER_TEXT), (")", INK)],
    [("        .when(needs(", INK), ('"integration"', AMBER_TEXT), (")).to(", INK), ('"camel:quarkus?kafka"', AMBER_TEXT), (")", INK)],
    [("        .when(needs(", INK), ('"ai"', AMBER_TEXT), (")).to(", INK), ('"agents:mcp?skills"', AMBER_TEXT), (")", INK)],
    [("    .end()", INK)],
    [("    .wireTap(", INK), ('"controlbus:teams"', AMBER_TEXT), (")", INK)],
    [("    .aggregate(allBranches()).to(", INK), ('"outbound:production"', AMBER_TEXT), (");", INK)],
]
CALLOUT_LINES = {2: 1, 3: 2, 4: 3, 6: 4}


def code_block(bank, x, y, size, lh, bubbles_x):
    out = []
    for i, parts in enumerate(CODE):
        cx = x
        for s, col in parts:
            out.append(t(bank, MONO, s, cx, y + i * lh, size, col))
            cx += MONO.width(s, size)
        if i in CALLOUT_LINES:
            out.append(bubble(bank, CALLOUT_LINES[i], bubbles_x, y + i * lh - size * 0.35, r=size * 0.62))
    return "".join(out)


def title_block(bank, x, y, w, rows, label_w, size, write_me):
    rh = size * 2.15
    out = [f'<rect x="{x}" y="{y}" width="{w}" height="{rh * len(rows)}" fill="{SHEET}" stroke="{INK}" stroke-width="2"/>']
    for i, (k, v, style) in enumerate(rows):
        top = y + rh * i
        base = top + rh * 0.66
        if style == "talk":
            out.append(f'<rect x="{x}" y="{top}" width="{w}" height="{rh}" fill="{AMBER}"/>')
        if i:
            out.append(f'<path d="M{x} {top}H{x + w}" stroke="{INK}" stroke-width="1"/>')
        out.append(t(bank, SEMI, k, x + 10, base, size * 0.82, INK if style == "talk" else SOFT, tracking=1.2))
        vx = x + label_w + 10
        if style == "talk":
            out.append(t(bank, BOLD, write_me, vx, base + size * 0.08, size * 1.2, INK, tracking=0.6))
            vx += BOLD.width(write_me, size * 1.2, 0.6) + size * 0.7
            out.append(t(bank, MONO, v, vx, base, size * 0.95, INK))
        elif style == "links":
            for item in v.split("|"):
                iw = MONO.width(item, size)
                out.append(t(bank, MONO, item, vx, base, size, BUS))
                out.append(f'<rect x="{vx}" y="{base + size * 0.22:.1f}" width="{iw:.1f}" height="1.3" fill="{BUS}"/>')
                vx += iw + size * 1.6
        else:
            out.append(t(bank, MONO_B if i == 0 else MONO, v, vx, base, size, INK))
    out.append(f'<path d="M{x + label_w} {y}V{y + rh * len(rows)}" stroke="{INK}" stroke-width="1.2"/>')
    return "".join(out)


# ---------------------------------------------------------------- hero, desktop
def hero(lang):
    T = TEXT[lang]
    W, H = 1200, 900
    bank = GlyphBank("e")
    out = []
    out.append(t(bank, BOLD, "ANDRÉS ZAPATA", 60, 108, 62))
    out.append(t(bank, MED, T["subtitle"], 62, 142, 21, SOFT))

    cy = 400
    ys = [256, 400, 544]
    bx0, bx1 = 430, 752
    # Control bus: leadership and trainings steer every stage.
    out.append(f'<path d="M240 186H1140" stroke="{BUS}" stroke-width="2" stroke-dasharray="9 6"/>')
    out.append(t(bank, BOLD, "CONTROL BUS", 240, 176, 17, BUS, tracking=1))
    out.append(t(bank, MONO, T["bus"], 352, 176, 13, BUS))
    out.append(bubble(bank, 4, 1112, 186, color=BUS))
    for x, y2 in [(275, cy - 35), (575, ys[0] - 32), (835, cy - 35)]:
        out.append(f'<path d="M{x} 186V{y2}" stroke="{BUS}" stroke-width="1.4" stroke-dasharray="4 5"/>')

    wires = [f'M210 {cy}H240']
    for y in ys:
        wires.append(f'M310 {cy}H362V{y}H{bx0}')
        wires.append(f'M{bx1} {y}H778V{cy}H800')
    wires.append(f'M870 {cy}H900')
    out.append(f'<path d="{"".join(wires)}" stroke="{INK}" stroke-width="2" fill="none"/>')
    for y in ys:
        out.append(f'<path d="M{bx0 - 22} {y}H{bx0}" stroke="{INK}" stroke-width="2" marker-end="url(#arrow)"/>')
    out.append(f'<path d="M780 {cy}H800" stroke="{INK}" stroke-width="2" marker-end="url(#arrow)"/>')

    out.append(pipe(60, cy, 150))
    out.append(pipe(900, cy, 150))
    out.append(tokens([f'M74 {cy}H362V{y}H778V{cy}H1060' for y in ys]))

    out.append(router(275, cy))
    out.append(aggregator(835, cy))
    out.append(t(bank, MONO, "inbound", 60, cy - 26, 13, SOFT))
    out.append(t(bank, SEMI, T["problem"], 60, cy + 42, 17, INK))
    out.append(t(bank, SEMI, T["router"], 275, cy + 58, 15, SOFT, "middle"))
    out.append(t(bank, SEMI, T["aggregator"], 835, cy + 58, 15, SOFT, "middle"))
    out.append(t(bank, MONO, "outbound", 900, cy - 26, 13, SOFT))
    out.append(t(bank, SEMI, T["production"], 900, cy + 42, 17, INK))
    out.append(f'<rect x="1066" y="{cy - 30}" width="74" height="60" fill="{INK}"/>')
    out.append(f'<path d="M1050 {cy}H1066" stroke="{INK}" stroke-width="2"/>')
    out.append(t(bank, BOLD, "PROD", 1103, cy + 7, 20, SHEET, "middle", tracking=1.5))

    for (title, kind, sub, n), y in zip(T["branches"], ys):
        out.append(f'<rect x="{bx0}" y="{y - 34}" width="{bx1 - bx0}" height="68" fill="{SHEET}" stroke="{INK}" stroke-width="2.4"/>')
        out.append(glyph(kind, bx0 + 12, y - 20))
        out.append(t(bank, BOLD, title, bx0 + 66, y - 3, 23, INK, tracking=0.5))
        out.append(t(bank, MONO, sub, bx0 + 66, y + 20, 12, SOFT))
        out.append(bubble(bank, n, bx1, y - 34))

    dx, dy = 60, 626
    out.append(f'<path d="M{dx} {dy - 20}H{dx + 690}" stroke="{INK}" stroke-width="1.2"/>')
    out.append(t(bank, BOLD, "DETAIL A", dx, dy - 28, 15, INK, tracking=1.2))
    out.append(t(bank, MONO, "Route.java", dx + 82, dy - 28, 13, SOFT))
    out.append(code_block(bank, dx, dy + 6, 13.5, 19, dx + 690))

    out.append(title_block(bank, 800, 606, 340, T["title_rows"], 104, 14, T["write_me"]))
    save(f"hero{suffix(lang)}.svg", sheet(W, H, "".join(out), bank, T["hero_title"], T["hero_desc"]))


# ---------------------------------------------------------------- hero, phone
def hero_mobile(lang):
    T = TEXT[lang]
    W, H = 800, 1860
    bank = GlyphBank("em")
    out = []
    out.append(t(bank, BOLD, "ANDRÉS ZAPATA", 56, 116, 84))
    for i, line in enumerate(T["subtitle_m"]):
        out.append(t(bank, MED, line, 58, 162 + i * 34, 28, SOFT))

    cx = 400
    xs = [160, 400, 640]
    out.append(t(bank, MONO, "inbound", 444, 262, 18, SOFT))
    out.append(t(bank, SEMI, T["problem"], 444, 290, 24, INK))
    out.append(f'<path d="M{cx} 380V400" stroke="{INK}" stroke-width="2.4"/>')
    wires = []
    for x in xs:
        wires.append(f'M{cx} 476V500H{x}V600')
        wires.append(f'M{x} 830V870H{cx}V900')
    out.append(f'<path d="{"".join(wires)}" stroke="{INK}" stroke-width="2.4" fill="none"/>')
    out.append(f'<path d="M{cx} 970V1000" stroke="{INK}" stroke-width="2.4"/>')
    out.append(f'<path d="M64 548H736" stroke="{BUS}" stroke-width="2.4" stroke-dasharray="10 7"/>')
    out.append(t(bank, BOLD, "CONTROL BUS", 64, 538, 22, BUS, tracking=1))
    out.append(t(bank, MONO, T["bus_m"], 222, 538, 16, BUS))
    out.append(bubble(bank, 4, 736, 548, r=16, color=BUS))

    out.append(pipe(cx, 250, 130, h=36, vertical=True))
    out.append(pipe(cx, 1000, 130, h=36, vertical=True))
    out.append(tokens([f'M{cx} 262V500H{x}V870H{cx}V1120' for x in xs]))
    out.append(router(cx, 440, s=72, vertical=True))
    out.append(t(bank, SEMI, T["router"], 450, 446, 20, SOFT))
    out.append(aggregator(cx, 935, s=72, vertical=True))
    out.append(t(bank, SEMI, T["aggregator"], 450, 942, 20, SOFT))
    out.append(t(bank, MONO, "outbound", 444, 1046, 18, SOFT))
    out.append(t(bank, SEMI, T["production"], 444, 1074, 24, INK))
    out.append(f'<rect x="{cx - 50}" y="1140" width="100" height="58" fill="{INK}"/>')
    out.append(f'<path d="M{cx} 1130V1140" stroke="{INK}" stroke-width="2.4"/>')
    out.append(t(bank, BOLD, "PROD", cx, 1178, 26, SHEET, "middle", tracking=1.5))

    for (title, kind, sub, n), x in zip(T["branches"], xs):
        out.append(f'<rect x="{x - 112}" y="600" width="224" height="230" fill="{SHEET}" stroke="{INK}" stroke-width="2.4"/>')
        out.append(glyph(kind, x - 26, 622, s=52))
        words = title.split(" ", 1) if len(title) > 12 else [title]
        for j, wline in enumerate(words):
            out.append(t(bank, BOLD, wline, x, 712 + j * 30, 28, INK, "middle", tracking=0.5))
        for j, sline in enumerate(wrap(MONO, sub.replace(" · ", ", "), 15, 196)):
            out.append(t(bank, MONO, sline, x, 772 + j * 22 + (16 if len(words) > 1 else 0), 15, SOFT, "middle"))
        out.append(bubble(bank, n, x + 112, 600, r=16))

    dy = 1258
    out.append(t(bank, BOLD, "DETAIL A", 56, dy, 22, INK, tracking=1.2))
    out.append(t(bank, MONO, "Route.java", 176, dy, 18, SOFT))
    out.append(f'<path d="M56 {dy + 12}H744" stroke="{INK}" stroke-width="1.4"/>')
    compact = [
        [("from(", INK), ('"inbound:your-problem"', AMBER_TEXT), (")", INK)],
        [("  .choice()", INK)],
        [("  .when(", INK), ('"architecture"', AMBER_TEXT), (")", INK)],
        [("  .when(", INK), ('"integration"', AMBER_TEXT), (")", INK)],
        [("  .when(", INK), ('"ai"', AMBER_TEXT), (")", INK)],
        [("  .wireTap(", INK), ('"controlbus:teams"', AMBER_TEXT), (")", INK)],
        [("  .to(", INK), ('"outbound:production"', AMBER_TEXT), (");", INK)],
    ]
    keyed = {2: 1, 3: 2, 4: 3, 5: 4}
    for i, parts in enumerate(compact):
        x = 56
        y = dy + 48 + i * 30
        for s, col in parts:
            out.append(t(bank, MONO, s, x, y, 20, col))
            x += MONO.width(s, 20)
        if i in keyed:
            out.append(bubble(bank, keyed[i], 728, y - 7, r=13))

    rows = T["title_rows"]
    out.append(title_block(bank, 56, H - 28 - 26 - len(rows) * 34.4, 688, rows, 170, 16, T["write_me"]))
    save(f"hero-mobile{suffix(lang)}.svg", sheet(W, H, "".join(out), bank, T["hero_title"], T["hero_desc"]))


# ---------------------------------------------------------------- clickable buttons under the drawing
def link(name, label, primary):
    bank = GlyphBank("l")
    size = 30
    w = int(MONO_B.width(label, size)) + 110
    h = 92
    fill = INK if primary else SHEET
    fg = SHEET if primary else INK
    ax = w - 46
    body = (f'<rect width="{w}" height="{h}" fill="{SHEET}"/>'
            f'<rect x="6" y="6" width="{w - 12}" height="{h - 12}" fill="{fill}" stroke="{INK}" stroke-width="3"/>'
            + t(bank, MONO_B, label, 34, h / 2 + 11, size, fg)
            + f'<path d="M{ax} {h / 2}H{ax + 22}M{ax + 13} {h / 2 - 9}L{ax + 22} {h / 2}L{ax + 13} {h / 2 + 9}" '
              f'stroke="{fg}" stroke-width="3" fill="none"/>')
    save(name, f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" '
               f'aria-label="{label}"><defs>{bank.defs()}</defs>{body}</svg>\n')


if __name__ == "__main__":
    for lang in TEXT:
        hero(lang)
        hero_mobile(lang)
        for i, (name, label, _, _) in enumerate(TEXT[lang]["buttons"]):
            out = f"{name}{suffix(lang)}.svg"
            if lang == "en" or label != TEXT["en"]["buttons"][i][1]:
                link(out, label, i == 0)
