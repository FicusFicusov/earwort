"""Copies the parts the two pages share from index.html into intervals.html.

    python3 tools/sync_shared.py

Both pages are single files, so the look (CSS) and the common code (icons, theme, knob, the plant on the screen,
the support dialog) live in both. In each page the shared part of the <style> and of the <script> starts at a
"=== shared ===" banner and ends at the next "=== this page ===" banner. Edit them in index.html, then run this.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SHARED, PAGE = "=== shared ===", "=== this page ==="


def blocks(text, name):
    """[(start, end)] of the shared parts: from the line of a SHARED banner to the line of the next PAGE banner"""
    out, pos = [], 0
    while True:
        s = text.find(SHARED, pos)
        if s < 0:
            break
        e = text.find(PAGE, s)
        if e < 0:
            sys.exit(f"{name}: a shared block without its end")
        out.append((text.rfind("\n", 0, s) + 1, text.rfind("\n", 0, e) + 1))
        pos = e
    if len(out) != 2:
        sys.exit(f"{name}: expected 2 shared blocks (style, script), found {len(out)}")
    return out


def main():
    src = open(os.path.join(ROOT, "index.html"), encoding="utf-8").read()
    path = os.path.join(ROOT, "intervals.html")
    dst = open(path, encoding="utf-8").read()
    parts = [src[a:b] for a, b in blocks(src, "index.html")]
    for (a, b), part in reversed(list(zip(blocks(dst, "intervals.html"), parts))):
        dst = dst[:a] + part + dst[b:]
    open(path, "w", encoding="utf-8").write(dst)
    print("intervals.html: shared style and script copied from index.html")


if __name__ == "__main__":
    main()
