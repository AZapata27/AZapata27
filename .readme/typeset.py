"""Text-to-outline typesetting for GitHub-safe SVG.

GitHub serves README images with `Content-Security-Policy: default-src 'none'`, so fonts cannot load inside
them. Every string is shaped with HarfBuzz (real kerning) and emitted as glyph outlines; each glyph is defined
once per document and placed with <use>.
"""
import io

import uharfbuzz as hb
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.ttLib import TTFont
from fontTools.varLib import instancer


def ntos(v):
    s = f"{v:.1f}"
    return s[:-2] if s.endswith(".0") else s


class Face:
    def __init__(self, path, axes=None, features=None):
        font = TTFont(path)
        if axes:
            font = instancer.instantiateVariableFont(font, axes)
        buf = io.BytesIO()
        font.save(buf)
        data = buf.getvalue()
        self.tt = TTFont(io.BytesIO(data))
        self.gs = self.tt.getGlyphSet()
        self.upem = self.tt["head"].unitsPerEm
        self.hb = hb.Font(hb.Face(data))
        self.order = self.tt.getGlyphOrder()
        self.features = features or {"kern": True, "liga": True}

    def shape(self, text, size, tracking=0.0):
        if not text:
            return [], 0.0
        b = hb.Buffer()
        b.add_str(text)
        b.guess_segment_properties()
        hb.shape(self.hb, b, self.features)
        s = size / self.upem
        x = 0.0
        out = []
        for info, pos in zip(b.glyph_infos, b.glyph_positions):
            out.append((self.order[info.codepoint], x + pos.x_offset * s, pos.y_offset * s))
            x += pos.x_advance * s + tracking
        return out, (x - tracking if out else 0.0)

    def width(self, text, size, tracking=0.0):
        return self.shape(text, size, tracking)[1]

    def uses(self, bank, text, x, y, size, tracking=0.0, anchor="start"):
        glyphs, w = self.shape(text, size, tracking)
        if anchor == "end":
            x -= w
        elif anchor == "middle":
            x -= w / 2
        out = []
        for name, gx, gy in glyphs:
            ref = bank.ref(self, name, size)
            if ref:
                out.append(f'<use href="#{ref}" x="{ntos(x + gx)}" y="{ntos(y - gy)}"/>')
        return "".join(out)


class GlyphBank:
    """Per-document registry of glyph outlines, emitted once in <defs>."""

    def __init__(self, prefix="g"):
        self.prefix = prefix
        self.items = {}

    def ref(self, face, name, size):
        key = (id(face), name, size)
        if key not in self.items:
            s = size / face.upem
            pen = SVGPathPen(face.gs, ntos=ntos)
            face.gs[name].draw(TransformPen(pen, (s, 0, 0, -s, 0, 0)))
            self.items[key] = (f"{self.prefix}{len(self.items)}", pen.getCommands())
        gid, d = self.items[key]
        return gid if d else None

    def defs(self):
        return "".join(f'<path id="{gid}" d="{d}"/>' for gid, d in self.items.values() if d)


def wrap(face, text, size, max_w, tracking=0.0):
    words, lines, cur = text.split(), [], ""
    for wd in words:
        trial = (cur + " " + wd).strip()
        if face.width(trial, size, tracking) <= max_w or not cur:
            cur = trial
        else:
            lines.append(cur)
            cur = wd
    if cur:
        lines.append(cur)
    return lines
