"""Makes the pages' pixel font: Departure Mono with the music signs it lacks, as a small WOFF2.

    python3 tools/build_font.py DepartureMono-Regular.otf fonts/earwort-mono.woff2

Departure Mono (SIL OFL 1.1, fonts/OFL-DepartureMono.txt) has no sharp, flat, natural, check or cross. They are
drawn here on its own grid (one pixel = 50 units, 7 pixels wide) and added under the font's new name, as the OFL
asks of a modified version (the Reserved Font Name is not used). Then the font is cut down to the characters
the pages use. Needs fontTools and brotli (pip install fonttools brotli).
"""
import sys

from fontTools import subset
from fontTools.pens.t2CharStringPen import T2CharStringPen
from fontTools.ttLib import TTFont

PX = 50
# rows from the top; the bottom row sits on line y0 (in pixels, 0 = the baseline)
GLYPHS = {
    0x266F: ("uni266F", 8, [   # sharp
        "..#.#..",
        "..#.#..",
        ".#####.",
        "..#.#..",
        "..#.#..",
        ".#####.",
        "..#.#..",
        "..#.#..",
        "..#.#..",
        "..#.#..",
    ], -1),
    0x266D: ("uni266D", 8, [   # flat: a tall stem, a small pointed bowl (unlike the letter b)
        ".#.....",
        ".#.....",
        ".#.....",
        ".#.....",
        ".#.....",
        ".#.##..",
        ".##..#.",
        ".#..#..",
        ".###...",
    ], 0),
    0x266E: ("uni266E", 8, [   # natural
        ".#.....",
        ".#.....",
        ".#...#.",
        ".#####.",
        ".#...#.",
        ".#...#.",
        ".#####.",
        ".#...#.",
        ".....#.",
        ".....#.",
    ], -1),
    0x2713: ("uni2713", 8, [   # check
        "......#",
        ".....#.",
        "#...#..",
        ".#.#...",
        "..#....",
    ], 1),
    0x2717: ("uni2717", 8, [   # cross
        ".#...#.",
        "..#.#..",
        "...#...",
        "..#.#..",
        ".#...#.",
    ], 1),
}

KEEP = (
    "U+0020-007E,U+00A0-00FF,U+0131,U+0152-0153,U+2010-2027,U+2030-203A,U+2044,U+20AC,U+2116,U+2122,"
    "U+2153-215E,U+2190-2199,U+21B5,U+2212,U+2248,U+2260,U+2264-2265,U+25A0-25AB,U+25B2,U+25BC,U+2665,"
    "U+2669,U+266D-266F,U+2713,U+2717"
)


def draw(rows, y0, private, gsubrs):
    pen = T2CharStringPen(7 * PX, None)
    top = y0 + len(rows) - 1
    for r, line in enumerate(rows):
        y = top - r
        x = 0
        while x < len(line):            # one rectangle per run of pixels in a row
            if line[x] != "#":
                x += 1
                continue
            x1 = x
            while x1 < len(line) and line[x1] == "#":
                x1 += 1
            pen.moveTo((x * PX, y * PX))
            pen.lineTo((x * PX, (y + 1) * PX))
            pen.lineTo((x1 * PX, (y + 1) * PX))
            pen.lineTo((x1 * PX, y * PX))
            pen.closePath()
            x = x1
    return pen.getCharString(private, gsubrs)


def main(src, dst):
    font = TTFont(src)
    cff = font["CFF "].cff
    top = cff.topDictIndex[0]
    cs = top.CharStrings
    private = cs.charStringsIndex[0].private if cs.charStringsAreIndexed else top.Private
    order = font.getGlyphOrder()
    for code, (name, _, rows, y0) in GLYPHS.items():
        c = draw(rows, y0, private, cff.GlobalSubrs)
        if name in cs.charStrings:
            cs[name] = c
        else:
            cs.charStringsIndex.items.append(c)
            cs.charStrings[name] = len(cs.charStringsIndex.items) - 1
            top.charset.append(name)
            order.append(name)
        lsb = min(line.index("#") for line in rows if "#" in line) * PX
        font["hmtx"].metrics[name] = (7 * PX, lsb)
        for t in font["cmap"].tables:
            if t.isUnicode():
                t.cmap[code] = name
    font.setGlyphOrder(order)
    font["maxp"].numGlyphs = len(order)
    for rec in font["name"].names:      # a modified version under its own name
        if rec.nameID in (1, 3, 4, 6, 16):
            s = rec.toUnicode().replace("Departure Mono", "Earwort Mono").replace("DepartureMono", "EarwortMono")
            rec.string = s
    tmp = dst + ".otf"
    font.save(tmp)
    opts = subset.Options()
    opts.flavor = "woff2"
    opts.layout_features = ["*"]
    opts.name_IDs = ["*"]
    opts.notdef_outline = True
    sub = subset.Subsetter(opts)
    f2 = TTFont(tmp)
    sub.populate(unicodes=subset.parse_unicodes(KEEP))
    sub.subset(f2)
    f2.flavor = "woff2"
    f2.save(dst)
    import os
    os.remove(tmp)
    print(dst, os.path.getsize(dst), "B")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])
