"""Generate 50..900 colour scales in OKLCH, anchored at shade 600.

Usage: python3 tools/color_scale.py <name> <hex> [max_chroma]
Example: python3 tools/color_scale.py primary "#3c667b"
Paste the output into assets/css/schemes/sgrse.css.
"""
import math
import sys


def srgb_to_lin(c):
    return c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4


def lin_to_srgb(c):
    return 12.92 * c if c <= 0.0031308 else 1.055 * c ** (1 / 2.4) - 0.055


def hex_to_oklch(h):
    r, g, b = (srgb_to_lin(int(h[i:i + 2], 16) / 255) for i in (1, 3, 5))
    l = 0.4122214708 * r + 0.5363325363 * g + 0.0514459929 * b
    m = 0.2119034982 * r + 0.6806995451 * g + 0.1073969566 * b
    s = 0.0883024619 * r + 0.2817188376 * g + 0.6299787005 * b
    l, m, s = (x ** (1 / 3) for x in (l, m, s))
    L = 0.2104542553 * l + 0.7936177850 * m - 0.0040720468 * s
    a = 1.9779984951 * l - 2.4285922050 * m + 0.4505937099 * s
    bb = 0.0259040371 * l + 0.7827717662 * m - 0.8086757660 * s
    return L, math.hypot(a, bb), math.atan2(bb, a)


def oklch_to_rgb(L, C, H):
    a, b = C * math.cos(H), C * math.sin(H)
    l = (L + 0.3963377774 * a + 0.2158037573 * b) ** 3
    m = (L - 0.1055613458 * a - 0.0638541728 * b) ** 3
    s = (L - 0.0894841775 * a - 1.2914855480 * b) ** 3
    r = 4.0767416621 * l - 3.3077115913 * m + 0.2309699292 * s
    g = -1.2684380046 * l + 2.6097574011 * m - 0.3413193965 * s
    bl = -0.0041960863 * l - 0.7034186147 * m + 1.7076147010 * s
    return [lin_to_srgb(x) for x in (r, g, bl)]


def in_gamut(rgb):
    return all(-1e-6 <= x <= 1 + 1e-6 for x in rgb)


def to_triplet(L, C, H):
    # reduce chroma until the colour fits into sRGB
    while C > 0 and not in_gamut(oklch_to_rgb(L, C, H)):
        C -= 0.001
    return tuple(round(min(max(x, 0), 1) * 255) for x in oklch_to_rgb(L, C, H))


SHADES = [50, 100, 200, 300, 400, 500, 600, 700, 800, 900]
# absolute OKLCH lightness for the outer shades; 600 is the anchor colour,
# 500 and 700 are interpolated
L_FIXED = {50: 0.975, 100: 0.945, 200: 0.89, 300: 0.82, 400: 0.72,
           800: 0.33, 900: 0.25}
# chroma factor relative to the anchor
CF = [0.10, 0.20, 0.38, 0.62, 0.88, 1.0, 1.0, 0.92, 0.80, 0.65]


def lightness(L600):
    ls = dict(L_FIXED)
    ls[600] = L600
    ls[500] = (ls[400] + L600) / 2
    ls[700] = (L600 + ls[800]) / 2
    return [ls[s] for s in SHADES]


def scale(hexcol, chroma_cap=None):
    L, C, H = hex_to_oklch(hexcol)
    out = []
    for shade, ls, cf in zip(SHADES, lightness(L), CF):
        c = C * cf if chroma_cap is None else min(C * cf, chroma_cap)
        if shade == 600 and chroma_cap is None:
            r, g, b = (int(hexcol[i:i + 2], 16) for i in (1, 3, 5))
            out.append((shade, (r, g, b)))
            continue
        out.append((shade, to_triplet(ls, c, H)))
    return out


if __name__ == '__main__':
    name, hexcol = sys.argv[1], sys.argv[2]
    cap = float(sys.argv[3]) if len(sys.argv) > 3 else None
    print(f'  /* {name}, anchored at 600 = {hexcol} */')
    for shade, (r, g, b) in scale(hexcol, cap):
        print(f'  --color-{name}-{shade}: {r}, {g}, {b};')
