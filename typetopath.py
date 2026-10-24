"""Render text to SVG path data so a banner looks identical on every machine."""
import sys
from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
from fontTools.misc.transform import Transform


class Face:
    def __init__(self, path):
        self.font = TTFont(path)
        self.gs = self.font.getGlyphSet()
        self.cmap = self.font.getBestCmap()
        self.upm = self.font["head"].unitsPerEm
        self.hmtx = self.font["hmtx"]

    def advances(self, text):
        total = 0
        for ch in text:
            name = self.cmap.get(ord(ch))
            if not name:
                raise SystemExit(f"missing glyph for {ch!r}")
            total += self.hmtx[name][0]
        return total

    def path(self, text, x, y, size, tracking=0.0):
        """Return (svg path string, advance width) with baseline at y."""
        scale = size / self.upm
        pen_out = []
        cursor = 0.0
        for ch in text:
            name = self.cmap.get(ord(ch))
            if not name:
                raise SystemExit(f"missing glyph for {ch!r}")
            pen = SVGPathPen(self.gs)
            tpen = TransformPen(pen, Transform(scale, 0, 0, -scale, x + cursor * scale, y))
            self.gs[name].draw(tpen)
            d = pen.getCommands()
            if d:
                pen_out.append(d)
            cursor += self.hmtx[name][0] + tracking
        return " ".join(pen_out), cursor * scale

    def width(self, text, size, tracking=0.0):
        scale = size / self.upm
        w = 0.0
        for ch in text:
            name = self.cmap.get(ord(ch))
            w += self.hmtx[name][0]
            w += tracking
        return w * scale


if __name__ == "__main__":
    f = Face(sys.argv[1])
    print("upm", f.upm, "glyphs", len(f.gs))
