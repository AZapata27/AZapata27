# Profile README generator

`README.md` (English), `README.es.md` (Spanish) and every SVG in `assets/` are generated from `content.py`.
GitHub loads README images under `Content-Security-Policy: default-src 'none'`, so fonts cannot load inside
them: every string is shaped with HarfBuzz and written as glyph outlines.

```bash
pip install fonttools uharfbuzz
python .readme/fetch_fonts.py
python .readme/build_hero.py      # hero drawing and link buttons, en + es
python .readme/build_sheets.py    # notes, parts list, language selector, en + es
python .readme/build_readme.py    # README.md and README.es.md
```

To change a word, edit `content.py` and run the three builders. `STATIC=1 OUT=<dir>` builds a copy without
motion for review captures. Logos in `logos/`: devicon (MIT), simple-icons (CC0), Apache Camel official logo.
