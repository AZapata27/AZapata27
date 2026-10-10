"""Downloads the OFL fonts the generators outline into SVG (Google Fonts repository)."""
import os
import urllib.request

FONTS = {
    "BarlowCondensed-Bold.ttf": "barlowcondensed/BarlowCondensed-Bold.ttf",
    "BarlowCondensed-SemiBold.ttf": "barlowcondensed/BarlowCondensed-SemiBold.ttf",
    "BarlowCondensed-Medium.ttf": "barlowcondensed/BarlowCondensed-Medium.ttf",
    "JetBrainsMono[wght].ttf": "jetbrainsmono/JetBrainsMono%5Bwght%5D.ttf",
}
DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts")

if __name__ == "__main__":
    os.makedirs(DIR, exist_ok=True)
    for name, path in FONTS.items():
        dest = os.path.join(DIR, name)
        if not os.path.exists(dest):
            urllib.request.urlretrieve(f"https://github.com/google/fonts/raw/main/ofl/{path}", dest)
        print(name)
