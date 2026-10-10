"""Writes README.md (English) and README.es.md (Spanish).

Each starts with the language selector so both versions are one click apart from the first line; images use
<picture> so phones get the narrow drawings (the srcset points at main, where the profile page reads them).
"""
import os

from content import TEXT, RAW, suffix

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def pic(name, lang, alt):
    sfx = suffix(lang)
    alt = alt.replace('"', "'")
    return (f'<picture>\n  <source media="(max-width: 600px)" srcset="{RAW}{name}-mobile{sfx}.svg">\n'
            f'  <img src="assets/{name}{sfx}.svg" width="100%" alt="{alt}">\n</picture>\n')


def selector(lang):
    en = "lang-en.svg" if lang == "en" else "lang-en-off.svg"
    es = "lang-es.svg" if lang == "es" else "lang-es-off.svg"
    en_alt = "English (current)" if lang == "en" else "Read in English"
    es_alt = "Español (actual)" if lang == "es" else "Leer en español"
    return ('<p align="right">\n'
            f'  <a href="README.md"><img src="assets/{en}" height="34" alt="{en_alt}"></a>'
            f'<a href="README.es.md"><img src="assets/{es}" height="34" alt="{es_alt}"></a>\n'
            '</p>\n')


def readme(lang):
    T = TEXT[lang]
    notes_alt = T["notes_desc_prefix"] + " " + " ".join(f"{n}, {title.lower()}: {body}" for n, title, body in T["notes"])
    parts_alt = T["parts_desc_prefix"] + " " + " ".join(f"{l.capitalize()}: {c}." for l, _, c in T["stack"])
    md = selector(lang) + "\n"
    md += pic("hero", lang, T["hero_desc"]) + "\n"
    md += pic("notes", lang, notes_alt) + "\n"
    md += pic("parts", lang, parts_alt) + "\n"
    md += "&nbsp;\n\n"
    buttons = []
    for name, label, href, alt in T["buttons"]:
        sfx = suffix(lang) if os.path.exists(os.path.join(ROOT, "assets", f"{name}{suffix(lang)}.svg")) else ""
        buttons.append(f'<a href="{href}"><img src="assets/{name}{sfx}.svg" height="42" alt="{alt}"></a>')
    md += " ".join(buttons) + "\n"
    path = os.path.join(ROOT, "README.md" if lang == "en" else "README.es.md")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(md)
    print(os.path.basename(path))


if __name__ == "__main__":
    for lang in TEXT:
        readme(lang)
