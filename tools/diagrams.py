"""
Physics diagram library.

Every diagram is authored as an SVG string, then rasterised to PNG with
cairosvg and saved to build/img/. Slides insert the PNG as a picture — nothing
is ever drawn directly onto the slide. Call with a unique `key` so files are
cached/named deterministically.
"""
import os
import math
import hashlib
import cairosvg

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "build", "img")
os.makedirs(IMG_DIR, exist_ok=True)

# palette (matches deck)
INK = "#1D2433"
MUT = "#6B7280"
TEAL = "#0A9396"
ORANGE = "#F4801A"
PURPLE = "#6A4C93"
RED = "#E63946"
BLUE = "#2563EB"
GLASS = "#CFE8EA"
WATER = "#BFD8F2"
GREEN = "#2A9D8F"
GOLD = "#F4B400"


def _render(key, svg, w=900, h=720):
    path = os.path.abspath(os.path.join(IMG_DIR, f"{key}.png"))
    cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path,
                     output_width=w, output_height=h)
    return path


def _head():
    def mk(name, col):
        return (f'<marker id="{name}" markerWidth="16" markerHeight="16" '
                f'refX="11" refY="5" orient="auto" markerUnits="userSpaceOnUse">'
                f'<path d="M0,0 L13,5 L0,10 Z" fill="{col}"/></marker>')
    return (f'<defs>{mk("arrow", INK)}{mk("arrowR", RED)}'
            f'{mk("arrowT", TEAL)}{mk("arrowP", PURPLE)}'
            f'{mk("arrowO", ORANGE)}</defs>')


def _svg(body, vw=600, vh=480, bg="#FFFFFF"):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {vw} {vh}">'
            f'<rect width="{vw}" height="{vh}" fill="{bg}" rx="14"/>'
            f'{_head()}{body}</svg>')


def _line(x1, y1, x2, y2, col=INK, w=3, dash=None, marker=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{col}" '
            f'stroke-width="{w}"{d}{m}/>')


def _esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;")
            .replace(">", "&gt;"))


def _txt(x, y, s, col=INK, size=22, anchor="middle", bold=True, italic=False):
    s = _esc(s)
    fw = "700" if bold else "400"
    fs = ' font-style="italic"' if italic else ""
    return (f'<text x="{x}" y="{y}" fill="{col}" font-size="{size}" '
            f'font-family="Arial" font-weight="{fw}"{fs} '
            f'text-anchor="{anchor}">{s}</text>')


def _arc(cx, cy, r, a1, a2, col=MUT, w=2):
    x1 = cx + r * math.cos(math.radians(a1))
    y1 = cy - r * math.sin(math.radians(a1))
    x2 = cx + r * math.cos(math.radians(a2))
    y2 = cy - r * math.sin(math.radians(a2))
    large = 1 if abs(a2 - a1) > 180 else 0
    return (f'<path d="M {x1} {y1} A {r} {r} 0 {large} 0 {x2} {y2}" '
            f'fill="none" stroke="{col}" stroke-width="{w}"/>')


# ---------------------------------------------------------------------------
# Refraction at plane surfaces
# ---------------------------------------------------------------------------
def refraction_bending(key, denser_below=True):
    """Ray bends toward / away from normal crossing a boundary."""
    vw, vh = 600, 480
    cx, cy = 300, 240
    top = "#EAF6FF" if denser_below else GLASS
    bot = GLASS if denser_below else "#EAF6FF"
    body = [
        f'<rect x="40" y="60" width="520" height="180" fill="{top}"/>',
        f'<rect x="40" y="240" width="520" height="180" fill="{bot}"/>',
        _line(40, 240, 560, 240, INK, 3),
        _line(cx, 70, cx, 410, MUT, 2, dash="6 6"),  # normal
        # incident ray (top-left to centre)
        _line(140, 110, cx, cy, RED, 4, marker="arrowR"),
    ]
    if denser_below:
        # bends toward normal
        body.append(_line(cx, cy, 380, 400, TEAL, 4, marker="arrowT"))
        body.append(_txt(150, 95, "incident ray", RED, 18))
        body.append(_txt(420, 385, "refracted ray", TEAL, 18))
        body.append(_txt(470, 130, "rarer (air)", MUT, 19))
        body.append(_txt(470, 330, "denser (glass)", MUT, 19))
        body.append(_txt(255, 175, "i", INK, 22, italic=True))
        body.append(_txt(330, 320, "r", INK, 22, italic=True))
        body.append(_txt(300, 455, "Ray bends TOWARD the normal", INK, 20))
    else:
        body.append(_line(cx, cy, 430, 390, TEAL, 4, marker="arrowT"))
        body.append(_txt(150, 95, "incident ray", RED, 18))
        body.append(_txt(450, 375, "refracted ray", TEAL, 18))
        body.append(_txt(470, 130, "denser (glass)", MUT, 19))
        body.append(_txt(470, 330, "rarer (air)", MUT, 19))
        body.append(_txt(255, 175, "i", INK, 22, italic=True))
        body.append(_txt(345, 305, "r", INK, 22, italic=True))
        body.append(_txt(300, 455, "Ray bends AWAY from the normal", INK, 20))
    body.append(_txt(cx, 55, "Normal", MUT, 16))
    return _render(key, _svg("".join(body), vw, vh), 760, 608)


def glass_block(key):
    """Refraction through a rectangular glass block — lateral displacement."""
    body = [
        f'<rect x="150" y="150" width="300" height="210" fill="{GLASS}" '
        f'stroke="{INK}" stroke-width="3"/>',
        _txt(300, 145, "glass slab", MUT, 18),
        # incident
        _line(60, 90, 205, 185, RED, 3.5, marker="arrowR"),
        _line(205, 185, 205, 140, MUT, 2, dash="6 6"),  # normal at entry
        # inside (bent toward normal)
        _line(205, 185, 360, 330, PURPLE, 3.5),
        # normal at exit
        _line(360, 330, 360, 285, MUT, 2, dash="6 6"),
        _line(360, 330, 500, 415, TEAL, 3.5, marker="arrowT"),
        # emergent parallel guide (dashed continuation of incident)
        _line(205, 185, 475, 360, MUT, 2, dash="4 7"),
        _txt(70, 75, "incident ray", RED, 16, anchor="start"),
        _txt(235, 290, "refracted", PURPLE, 15, anchor="start"),
        _txt(395, 405, "emergent ray", TEAL, 16, anchor="start"),
        f'<line x1="475" y1="360" x2="500" y2="415" stroke="{ORANGE}" '
        f'stroke-width="3"/>',
        _txt(515, 388, "lateral shift", ORANGE, 15, anchor="start"),
        _txt(300, 55, "Emergent ray is parallel to the incident ray",
             INK, 19),
    ]
    return _render(key, _svg("".join(body)), 800, 640)


def real_apparent_depth(key):
    """A coin appears raised because of refraction."""
    body = [
        f'<rect x="60" y="180" width="480" height="240" fill="{WATER}" '
        f'stroke="{INK}" stroke-width="2"/>',
        _line(60, 180, 540, 180, INK, 3),
        _txt(300, 160, "water surface", MUT, 18),
        # real coin
        f'<ellipse cx="300" cy="400" rx="34" ry="12" fill="{ORANGE}" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(300, 432, "real position", ORANGE, 16),
        # apparent coin
        f'<ellipse cx="300" cy="320" rx="34" ry="12" fill="none" '
        f'stroke="{RED}" stroke-width="2" stroke-dasharray="5 4"/>',
        _txt(300, 300, "apparent position", RED, 16),
        # rays from coin to eye
        _line(300, 400, 230, 180, TEAL, 3),
        _line(230, 180, 150, 90, TEAL, 3, marker="arrowT"),
        _line(300, 320, 230, 180, RED, 2, dash="5 5"),
        f'<circle cx="135" cy="80" r="16" fill="none" stroke="{INK}" '
        f'stroke-width="2"/>',
        _txt(135, 60, "eye", INK, 16),
        _txt(300, 470, "Real depth  >  Apparent depth", INK, 20),
    ]
    return _render(key, _svg("".join(body), 600, 500), 750, 625)


def prism_refraction(key):
    """White ray deviated through a triangular prism."""
    body = [
        f'<polygon points="300,110 180,360 420,360" fill="{GLASS}" '
        f'stroke="{INK}" stroke-width="3"/>',
        _txt(300, 300, "prism", MUT, 20),
        _line(70, 220, 232, 232, RED, 4, marker="arrowR"),
        _line(232, 232, 360, 300, PURPLE, 4),
        _line(360, 300, 520, 360, TEAL, 4, marker="arrowT"),
        # original direction guide
        _line(232, 232, 470, 250, MUT, 2, dash="5 6"),
        _arc(360, 300, 60, 22, -12, ORANGE, 3),
        _txt(470, 300, "δ", ORANGE, 24, italic=True),
        _txt(450, 280, "angle of", ORANGE, 15, anchor="start"),
        _txt(450, 330, "deviation", ORANGE, 15, anchor="start"),
        _txt(100, 205, "incident", RED, 16, anchor="start"),
        _txt(300, 95, "A", INK, 22),
        _txt(300, 430, "Light bends toward the base of the prism", INK, 19),
    ]
    return _render(key, _svg("".join(body), 600, 470), 760, 595)


def total_internal_reflection(key):
    """Three rays: i<C refracts, i=C grazes, i>C total internal reflection."""
    cx, cy = 300, 250
    body = [
        f'<rect x="40" y="80" width="520" height="170" fill="{GLASS}"/>',
        f'<rect x="40" y="250" width="520" height="150" fill="#EAF6FF"/>',
        _line(40, 250, 560, 250, INK, 3),
        _line(cx, 110, cx, 390, MUT, 2, dash="6 6"),
        # ray 1: small angle -> refracts out
        _line(180, 175, cx, cy, TEAL, 3, marker="arrowT"),
        _line(cx, cy, 360, 330, TEAL, 3, marker="arrowT"),
        # ray 2: critical -> grazes along surface
        _line(150, 215, cx, cy, ORANGE, 3, marker=None),
        _line(cx, cy, 470, 252, ORANGE, 3),
        # ray 3: > critical -> reflects back into glass
        _line(150, 248, cx, cy, RED, 3),
        _line(cx, cy, 430, 150, RED, 3, marker="arrowR"),
        _txt(470, 130, "denser", MUT, 18),
        _txt(470, 360, "rarer", MUT, 18),
        _txt(355, 320, "i < C", TEAL, 16, anchor="start"),
        _txt(420, 250, "i = C", ORANGE, 16, anchor="start"),
        _txt(420, 140, "i > C : T.I.R.", RED, 16, anchor="start"),
        _txt(300, 450, "Beyond the critical angle C, light is totally "
                       "internally reflected", INK, 17),
    ]
    return _render(key, _svg("".join(body), 600, 480), 780, 624)


# ---------------------------------------------------------------------------
# Generic angle/normal reflection (reused by mirrors topic)
# ---------------------------------------------------------------------------
def reflection_law(key):
    cx, cy = 300, 330
    body = [
        f'<rect x="60" y="330" width="480" height="40" fill="#D7DCE3"/>',
        _line(60, 330, 540, 330, INK, 3),
        _line(cx, 110, cx, 330, MUT, 2, dash="6 6"),
        _line(150, 150, cx, cy, RED, 4, marker="arrowR"),
        _line(cx, cy, 450, 150, TEAL, 4, marker="arrowT"),
        _arc(cx, cy, 70, 124, 90, MUT, 2),
        _arc(cx, cy, 70, 90, 56, MUT, 2),
        _txt(238, 205, "i", INK, 22, italic=True),
        _txt(362, 205, "r", INK, 22, italic=True),
        _txt(170, 135, "incident ray", RED, 16, anchor="start"),
        _txt(430, 135, "reflected ray", TEAL, 16, anchor="end"),
        _txt(cx, 100, "normal", MUT, 16),
        _txt(300, 400, "Angle of incidence  i  =  Angle of reflection  r",
             INK, 19),
    ]
    return _render(key, _svg("".join(body), 600, 430), 760, 545)


def _lens_shape(cx, cy, h, convex=True, col=GLASS):
    if convex:
        return (f'<path d="M {cx} {cy-h} Q {cx+34} {cy} {cx} {cy+h} '
                f'Q {cx-34} {cy} {cx} {cy-h} Z" fill="{col}" '
                f'stroke="{INK}" stroke-width="2.5"/>')
    # concave (biconcave)
    return (f'<path d="M {cx-22} {cy-h} Q {cx} {cy-h+18} {cx+22} {cy-h} '
            f'L {cx+22} {cy+h} Q {cx} {cy+h-18} {cx-22} {cy+h} Z" '
            f'fill="{col}" stroke="{INK}" stroke-width="2.5"/>')


def convex_lens_image(key):
    """Object beyond 2F -> real, inverted, diminished image."""
    cx, cy = 300, 240
    body = [
        _line(40, cy, 560, cy, MUT, 2),  # principal axis
        _lens_shape(cx, cy, 110, True),
        # foci and 2F
        _txt(cx - 90, cy + 22, "2F", MUT, 16),
        _txt(cx - 45, cy + 22, "F", MUT, 16),
        _txt(cx + 48, cy + 22, "F", MUT, 16),
        _txt(cx + 95, cy + 22, "2F", MUT, 16),
        f'<circle cx="210" cy="{cy}" r="3" fill="{MUT}"/>',
        f'<circle cx="255" cy="{cy}" r="3" fill="{MUT}"/>',
        f'<circle cx="345" cy="{cy}" r="3" fill="{MUT}"/>',
        f'<circle cx="390" cy="{cy}" r="3" fill="{MUT}"/>',
        # object (upright arrow) at 175
        _line(175, cy, 175, cy - 80, ORANGE, 4, marker="arrowO"),
        _txt(175, cy - 92, "object", ORANGE, 15),
        # ray 1: parallel to axis, then refracts through far focus F (345)
        _line(175, cy - 80, cx, cy - 80, RED, 2.5),
        _line(cx, cy - 80, 410, cy + 115, RED, 2.5),
        # ray 2: straight through optical centre, undeviated
        _line(175, cy - 80, 430, cy + 83, TEAL, 2.5),
        # image (inverted, diminished) where the rays cross, between F and 2F
        _line(370, cy, 370, cy + 45, PURPLE, 4, marker="arrowP"),
        _txt(388, cy + 30, "image", PURPLE, 15, anchor="start"),
        _txt(300, 40, "Object beyond 2F → real, inverted, diminished",
             INK, 17),
    ]
    return _render(key, _svg("".join(body), 600, 460), 820, 629)


def convex_magnifier(key):
    """Object within F -> virtual, erect, magnified (magnifying glass)."""
    cx, cy = 330, 240
    body = [
        _line(40, cy, 560, cy, MUT, 2),
        _lens_shape(cx, cy, 110, True),
        _txt(cx - 55, cy + 22, "F", MUT, 16),
        _txt(cx + 50, cy + 22, "F", MUT, 16),
        f'<circle cx="275" cy="{cy}" r="3" fill="{MUT}"/>',
        f'<circle cx="385" cy="{cy}" r="3" fill="{MUT}"/>',
        # object within F
        _line(295, cy, 295, cy - 55, ORANGE, 4, marker="arrowO"),
        _txt(295, cy - 67, "object", ORANGE, 14),
        # ray parallel -> through F (on same side diverging)
        _line(295, cy - 55, cx, cy - 70, RED, 2.5),
        _line(cx, cy - 70, 520, cy - 30, RED, 2.5, marker="arrowR"),
        # ray through centre
        _line(295, cy - 55, 520, cy + 18, TEAL, 2.5, marker="arrowT"),
        # back-projected virtual rays (dashed) to virtual image
        _line(cx, cy - 70, 120, cy - 130, MUT, 2, dash="5 5"),
        _line(520, cy + 18, 120, cy - 130, MUT, 0),
        # virtual image (large, erect) at 120
        _line(120, cy, 120, cy - 130, PURPLE, 4, marker="arrowP"),
        _txt(120, cy - 142, "virtual image", PURPLE, 14),
        _txt(300, 40, "Object within F → virtual, erect, magnified", INK, 17),
    ]
    return _render(key, _svg("".join(body), 600, 460), 820, 629)


def concave_lens_image(key):
    """Concave lens -> always virtual, erect, diminished."""
    cx, cy = 320, 240
    body = [
        _line(40, cy, 560, cy, MUT, 2),
        _lens_shape(cx, cy, 110, False),
        _txt(cx - 70, cy + 22, "F", MUT, 16),
        _txt(cx + 70, cy + 22, "F", MUT, 16),
        f'<circle cx="250" cy="{cy}" r="3" fill="{MUT}"/>',
        f'<circle cx="390" cy="{cy}" r="3" fill="{MUT}"/>',
        # object
        _line(180, cy, 180, cy - 90, ORANGE, 4, marker="arrowO"),
        _txt(180, cy - 102, "object", ORANGE, 15),
        # ray parallel -> diverges as if from F (near side)
        _line(180, cy - 90, cx, cy - 90, RED, 2.5),
        _line(cx, cy - 90, 520, cy - 40, RED, 2.5, marker="arrowR"),
        _line(cx, cy - 90, 250, cy, MUT, 2, dash="5 5"),
        # ray through centre
        _line(180, cy - 90, 520, cy + 30, TEAL, 2.5, marker="arrowT"),
        # virtual image (diminished, erect)
        _line(245, cy, 245, cy - 48, PURPLE, 4, marker="arrowP"),
        _txt(245, cy - 60, "image", PURPLE, 14),
        _txt(300, 40, "Concave lens → virtual, erect, diminished", INK, 17),
    ]
    return _render(key, _svg("".join(body), 600, 460), 820, 629)


def lens_as_prisms(key):
    """A convex lens behaves like a stack of prisms + central slab."""
    cx, cy = 300, 230
    body = [
        _line(40, cy, 560, cy, MUT, 2),
        # upper prism (base down)
        f'<polygon points="{cx-30},{cy-110} {cx+30},{cy-110} {cx},{cy-50}" '
        f'fill="{GLASS}" stroke="{INK}" stroke-width="2"/>',
        # middle slab
        f'<rect x="{cx-30}" y="{cy-25}" width="60" height="50" '
        f'fill="{GLASS}" stroke="{INK}" stroke-width="2"/>',
        # lower prism (base up)
        f'<polygon points="{cx-30},{cy+110} {cx+30},{cy+110} {cx},{cy+50}" '
        f'fill="{GLASS}" stroke="{INK}" stroke-width="2"/>',
        _line(80, cy - 80, cx - 20, cy - 80, RED, 2.5),
        _line(cx + 10, cy - 70, 470, cy - 8, RED, 2.5, marker="arrowR"),
        _line(80, cy + 80, cx - 20, cy + 80, RED, 2.5),
        _line(cx + 10, cy + 70, 470, cy + 8, RED, 2.5, marker="arrowR"),
        _line(80, cy, 470, cy, TEAL, 2.5, marker="arrowT"),
        _txt(300, 40, "A lens acts like a set of prisms with a central slab",
             INK, 16),
        _txt(480, cy + 4, "F", MUT, 16, anchor="start"),
    ]
    return _render(key, _svg("".join(body), 600, 470), 800, 627)


def optical_fibre(key):
    """Light zig-zagging down a fibre by repeated total internal reflection."""
    body = [
        f'<rect x="40" y="170" width="520" height="140" fill="{GLASS}" '
        f'stroke="{INK}" stroke-width="3"/>',
        _txt(300, 150, "glass fibre core", MUT, 17),
        _line(40, 240, 120, 180, RED, 3, marker="arrowR"),
    ]
    # zig-zag bounces
    pts = [(120, 180), (210, 300), (300, 180), (390, 300), (480, 180),
           (560, 250)]
    cols = [TEAL, TEAL, TEAL, TEAL, TEAL]
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        mk = "arrowT" if i == len(pts) - 2 else None
        body.append(_line(x1, y1, x2, y2, TEAL, 3, marker=mk))
    body.append(_txt(70, 230, "light in", RED, 15, anchor="start"))
    body.append(_txt(300, 360, "Each bounce is a total internal reflection "
                               "(i > C)", INK, 17))
    return _render(key, _svg("".join(body), 600, 400), 800, 533)


def reflecting_prism(key):
    """A 45-45-90 prism turning light through 90 degrees by T.I.R."""
    body = [
        f'<polygon points="160,120 160,360 400,360" fill="{GLASS}" '
        f'stroke="{INK}" stroke-width="3"/>',
        _txt(225, 300, "45°", MUT, 18),
        # incoming horizontal ray hitting hypotenuse
        _line(60, 200, 250, 200, RED, 3.5, marker="arrowR"),
        # T.I.R. at hypotenuse -> downward
        _line(250, 200, 250, 470, TEAL, 3.5, marker="arrowT"),
        _txt(70, 185, "incident", RED, 15, anchor="start"),
        _txt(265, 430, "reflected (90° turn)", TEAL, 15, anchor="start"),
        _txt(300, 90, "45°–45°–90° totally reflecting prism", INK, 17),
        _txt(300, 500, "Light is turned through 90° by T.I.R.", MUT, 16),
    ]
    return _render(key, _svg("".join(body), 600, 540), 620, 558)


if __name__ == "__main__":
    # smoke test
    for fn in [refraction_bending, glass_block, real_apparent_depth,
               prism_refraction, total_internal_reflection, reflection_law,
               optical_fibre, reflecting_prism]:
        print(fn(f"test_{fn.__name__}"))
