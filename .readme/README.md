# Profile README generator

The SVGs in `assets/` are generated, not drawn by hand. GitHub loads README images under
`Content-Security-Policy: default-src 'none'`, so fonts cannot load inside them: every string is shaped with
HarfBuzz and written as glyph outlines.

```bash
pip install fonttools uharfbuzz
python .readme/fetch_fonts.py
python .readme/build_hero.py      # assets/hero.svg, hero-mobile.svg, link-*.svg
```

`STATIC=1 OUT=<dir>` builds a copy without motion for review captures.
