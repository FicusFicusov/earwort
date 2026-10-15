"""Puts the pixel font into each page as base64, so a page is one self-contained file: it works opened straight
from disk or from a chat, without a server.

    python3 tools/embed.py            (from the repository root: index.html and intervals.html)

The font comes from fonts/earwort-mono.woff2 (tools/build_font.py). It goes between the markers in the page:
    /*FONT*/url(...)/*END_FONT*/
"""
import base64
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGES = ["index.html", "intervals.html"]


def main():
    font = base64.b64encode(open(os.path.join(ROOT, "fonts/earwort-mono.woff2"), "rb").read()).decode("ascii")
    pat = re.compile(re.escape("/*FONT*/") + r".*?" + re.escape("/*END_FONT*/"), re.S)
    for page in PAGES:
        path = os.path.join(ROOT, page)
        text = open(path, encoding="utf-8").read()
        text, n = pat.subn(lambda _: f'/*FONT*/url("data:font/woff2;base64,{font}")/*END_FONT*/', text)
        if n != 1:
            sys.exit(f"{page}: expected one FONT marker, found {n}")
        open(path, "w", encoding="utf-8").write(text)
        print(f"{page}: {os.path.getsize(path)} B (font {len(font)} chars)")


if __name__ == "__main__":
    main()
