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
        _txt(370, cy + 78, "image", PURPLE, 15),
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


VIBGYOR = [("Violet", "#7F00FF"), ("Indigo", "#4B0082"), ("Blue", "#0000FF"),
           ("Green", "#00A000"), ("Yellow", "#FFD000"), ("Orange", "#FF7F00"),
           ("Red", "#FF0000")]


def dispersion_spectrum(key):
    """White light splitting into the seven colours through a prism."""
    body = [
        f'<polygon points="320,90 200,360 440,360" fill="{GLASS}" '
        f'stroke="{INK}" stroke-width="3"/>',
        _txt(320, 80, "prism", MUT, 18),
        # incoming white beam (shown grey so it is visible on white)
        _line(60, 205, 262, 232, "#9AA1AB", 5, marker="arrow"),
        # internal ray through the glass
        _line(262, 232, 360, 300, "#9AA1AB", 4),
        _txt(70, 188, "white light", INK, 16, anchor="start"),
    ]
    # fan of coloured rays from exit face; red deviates least, violet most
    ex, ey = 360, 300
    for i, (name, col) in enumerate(reversed(VIBGYOR)):  # red first (top)
        ang = 6 + i * 4.2
        import math as _m
        x2 = ex + 200 * _m.cos(_m.radians(ang))
        y2 = ey + 200 * _m.sin(_m.radians(ang))
        body.append(_line(ex, ey, x2, y2, col, 4))
        body.append(_txt(x2 + 14, y2 + 5, name, col, 13, anchor="start"))
    body.append(_txt(300, 420, "Violet bends most, red bends least — "
                               "dispersion gives a spectrum", INK, 16))
    return _render(key, _svg("".join(body), 640, 460), 860, 619)


def em_spectrum(key):
    """The electromagnetic spectrum as a labelled band, visible part in colour."""
    bands = [("Radio", "#6B7280"), ("Micro-\nwave", "#8B5CF6"),
             ("Infrared", "#E63946"), ("Visible", None),
             ("Ultra-\nviolet", "#7C3AED"), ("X-rays", "#2563EB"),
             ("Gamma", "#0A9396")]
    body = []
    x0, w, y, h = 40, 80, 150, 90
    for i, (name, col) in enumerate(bands):
        x = x0 + i * w
        if name == "Visible":
            # rainbow strip
            for j, (_, c) in enumerate(reversed(VIBGYOR)):
                bw = w / 7
                body.append(f'<rect x="{x + j*bw}" y="{y}" width="{bw+0.5}" '
                            f'height="{h}" fill="{c}"/>')
            body.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
                        f'fill="none" stroke="{INK}" stroke-width="1.5"/>')
        else:
            body.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" '
                        f'fill="{col}" stroke="{INK}" stroke-width="1.5"/>')
        for k, line in enumerate(name.split("\n")):
            body.append(_txt(x + w/2, y - 18 + k*16, line, INK, 13))
    body.append(_line(40, y + h + 18, 40 + 7*w, y + h + 18, INK, 2,
                      marker="arrow"))
    body.append(_txt(60, y + h + 42, "long wavelength", MUT, 13,
                     anchor="start"))
    body.append(_txt(40 + 7*w - 20, y + h + 42, "short wavelength", MUT, 13,
                     anchor="end"))
    body.append(_txt((40 + 7*w)/2 + 20, y + h + 70,
                     "increasing frequency  →", MUT, 13))
    body.append(_txt((40 + 7*w)/2 + 20, 60,
                     "The Electromagnetic Spectrum", INK, 19))
    return _render(key, _svg("".join(body), 640, 330), 980, 505)


def scattering(key):
    """Blue sky and red sunset by scattering of sunlight."""
    body = [
        f'<rect x="0" y="0" width="640" height="240" fill="#BBD6F2" rx="0"/>',
        f'<rect x="0" y="240" width="640" height="120" fill="#E8C9A0"/>',
        f'<circle cx="540" cy="90" r="34" fill="{GOLD}"/>',
        _txt(540, 150, "Sun", MUT, 14),
        # incoming ray
        _line(506, 110, 300, 200, "#FFFFFF", 4, marker="arrow"),
        # scattered blue dots
    ]
    import random
    random.seed(3)
    for _ in range(26):
        x = random.randint(120, 460)
        y = random.randint(60, 220)
        body.append(f'<circle cx="{x}" cy="{y}" r="3" fill="#1E6Fd0"/>')
    body += [
        _txt(220, 50, "Blue scatters most → blue sky", "#0B3D91", 15),
        f'<circle cx="120" cy="300" r="14" fill="none" stroke="{INK}" '
        f'stroke-width="2"/>',
        _txt(120, 335, "observer", INK, 13),
        _txt(320, 350, "At sunset light travels further; blue is scattered "
                       "away, leaving red", INK, 14),
    ]
    return _render(key, _svg("".join(body), 640, 360), 860, 484)


def longitudinal_wave(key):
    """Compressions and rarefactions of a sound wave in air (explicit groups)."""
    body = [_txt(320, 40, "A sound wave: compressions (C) and rarefactions (R)",
                 INK, 17)]
    y0, y1 = 90, 250
    centers = [(110, "C", 9, 6), (250, "R", 4, 16), (390, "C", 9, 6),
               (530, "R", 4, 16)]
    for cx, lab, count, gap in centers:
        for k in range(-(count // 2), count // 2 + 1):
            xp = cx + k * gap
            body.append(f'<line x1="{xp}" y1="{y0}" x2="{xp}" y2="{y1}" '
                        f'stroke="{INK}" stroke-width="2"/>')
        col = RED if lab == "C" else BLUE
        body.append(_txt(cx, 285, lab, col, 20))
    body += [
        f'<line x1="110" y1="305" x2="390" y2="305" stroke="{ORANGE}" '
        f'stroke-width="2" marker-end="url(#arrowO)" '
        f'marker-start="url(#arrowO)"/>',
        _txt(250, 335, "one wavelength λ", ORANGE, 15),
    ]
    return _render(key, _svg("".join(body), 640, 360), 880, 495)


def echo_diagram(key):
    """Sound from a source reflecting off a cliff back to the listener."""
    body = [
        f'<rect x="500" y="60" width="120" height="320" fill="#C9B79C" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(560, 210, "cliff", "#6B5A45", 16),
        # person
        f'<circle cx="90" cy="180" r="16" fill="none" stroke="{INK}" '
        f'stroke-width="3"/>',
        f'<line x1="90" y1="196" x2="90" y2="250" stroke="{INK}" '
        f'stroke-width="3"/>',
        _txt(90, 285, "observer", INK, 15),
    ]
    # outgoing arcs
    for r in (60, 95, 130):
        body.append(f'<path d="M {120+r} {130} A {r} {r} 0 0 1 {120+r} {230}" '
                    f'fill="none" stroke="{RED}" stroke-width="2.5"/>')
    # returning arcs
    for r in (55, 90, 125):
        body.append(f'<path d="M {500-r} {135} A {r} {r} 0 0 0 {500-r} {225}" '
                    f'fill="none" stroke="{TEAL}" stroke-width="2.5"/>')
    body += [
        _txt(250, 110, "sound out →", RED, 15),
        _txt(330, 300, "← echo returns", TEAL, 15),
        _txt(320, 360, "Echo heard when the reflected sound returns after "
                       "≥ 0.1 s", INK, 15),
    ]
    return _render(key, _svg("".join(body), 640, 390), 860, 524)


def sound_characteristics(key):
    """Three waveforms: loud vs soft (amplitude), high vs low pitch
    (frequency)."""
    import math as _m

    def wave(x0, y0, w, amp, cycles, col):
        pts = []
        for i in range(0, 121):
            x = x0 + (i / 120) * w
            y = y0 - amp * _m.sin(2 * _m.pi * cycles * i / 120)
            pts.append(f"{x:.1f},{y:.1f}")
        return (f'<polyline points="{" ".join(pts)}" fill="none" '
                f'stroke="{col}" stroke-width="3"/>')
    body = [
        _txt(170, 40, "Amplitude → loudness", INK, 16),
        _txt(490, 40, "Frequency → pitch", INK, 16),
        # loud (big amplitude) vs soft
        wave(40, 110, 260, 45, 3, RED),
        _txt(120, 175, "loud (large amplitude)", RED, 13),
        wave(40, 250, 260, 18, 3, BLUE),
        _txt(120, 300, "soft (small amplitude)", BLUE, 13),
        # high pitch vs low pitch
        wave(360, 110, 260, 32, 6, PURPLE),
        _txt(470, 175, "high pitch (high f)", PURPLE, 13),
        wave(360, 250, 260, 32, 2, GREEN),
        _txt(470, 300, "low pitch (low f)", GREEN, 13),
    ]
    return _render(key, _svg("".join(body), 660, 340), 900, 464)


def resonance_pendulums(key):
    """Coupled pendulums: the one matching the driver's length swings most."""
    body = [
        f'<line x1="60" y1="70" x2="600" y2="70" stroke="{INK}" '
        f'stroke-width="4"/>',
    ]
    lengths = [(120, 120, "A", MUT), (220, 200, "B (driver)", RED),
               (330, 90, "C", MUT), (430, 200, "D", TEAL), (530, 150, "E", MUT)]
    for x, L, lab, col in lengths:
        swing = 0
        if "driver" in lab:
            swing = -26
        if lab == "D":
            swing = 24  # equal length resonates strongly
        bx = x + swing
        body.append(f'<line x1="{x}" y1="70" x2="{bx}" y2="{70+L}" '
                    f'stroke="{col}" stroke-width="2.5"/>')
        body.append(f'<circle cx="{bx}" cy="{70+L}" r="13" fill="{col}"/>')
        body.append(_txt(x, 70 + L + 34 if L < 210 else 70 + L + 30, lab,
                         col, 13))
    body.append(_txt(330, 320, "B drives all; only D (same length) resonates "
                               "and swings widely", INK, 15))
    return _render(key, _svg("".join(body), 660, 360), 900, 491)


def _cell(x, y):
    return (f'<line x1="{x}" y1="{y-16}" x2="{x}" y2="{y+16}" stroke="{INK}" '
            f'stroke-width="4"/>'
            f'<line x1="{x+12}" y1="{y-8}" x2="{x+12}" y2="{y+8}" '
            f'stroke="{INK}" stroke-width="4"/>')


def ohm_circuit(key):
    """Circuit to verify Ohm's law: cell, switch, ammeter (series),
    resistor with a voltmeter across it."""
    L, R, T, B = 90, 550, 90, 330
    body = [
        # wires (rectangle)
        f'<rect x="{L}" y="{T}" width="{R-L}" height="{B-T}" fill="none" '
        f'stroke="{INK}" stroke-width="3"/>',
        # cell on left side
        _cell(L, (T+B)//2),
        _txt(L-26, (T+B)//2+5, "cell", MUT, 15, anchor="end"),
        # switch on bottom
        f'<circle cx="270" cy="{B}" r="4" fill="{INK}"/>',
        f'<line x1="270" y1="{B}" x2="310" y2="{B-18}" stroke="{INK}" '
        f'stroke-width="3"/>',
        f'<circle cx="316" cy="{B}" r="4" fill="{INK}"/>',
        _txt(290, B+28, "switch", MUT, 14),
        # ammeter on top (series)
        f'<circle cx="270" cy="{T}" r="22" fill="#FFFFFF" stroke="{INK}" '
        f'stroke-width="3"/>', _txt(270, T+7, "A", TEAL, 20),
        _txt(270, T-30, "ammeter", MUT, 14),
        # resistor on right side
        f'<rect x="{R-13}" y="160" width="26" height="100" fill="#FFFFFF" '
        f'stroke="{INK}" stroke-width="3"/>',
        _txt(R+20, 215, "R", PURPLE, 18, anchor="start"),
        # voltmeter across the resistor
        f'<circle cx="{R+90}" cy="210" r="22" fill="#FFFFFF" stroke="{INK}" '
        f'stroke-width="3"/>', _txt(R+90, 217, "V", ORANGE, 20),
        _txt(R+90, 250, "voltmeter", MUT, 14),
        f'<line x1="{R}" y1="160" x2="{R+90}" y2="160" stroke="{INK}" '
        f'stroke-width="2"/>',
        f'<line x1="{R+90}" y1="160" x2="{R+90}" y2="188" stroke="{INK}" '
        f'stroke-width="2"/>',
        f'<line x1="{R}" y1="260" x2="{R+90}" y2="260" stroke="{INK}" '
        f'stroke-width="2"/>',
        f'<line x1="{R+90}" y1="260" x2="{R+90}" y2="232" stroke="{INK}" '
        f'stroke-width="2"/>',
    ]
    body.insert(0, _txt(350, 28, "Circuit to verify Ohm's law", INK, 17))
    return _render(key, _svg("".join(body), 700, 380), 900, 489)


def ohm_graph(key):
    """V–I straight line through the origin (Ohm's law)."""
    body = [
        _line(70, 330, 70, 60, INK, 3, marker="arrow"),
        _line(70, 330, 470, 330, INK, 3, marker="arrow"),
        _txt(40, 60, "I", INK, 20), _txt(470, 360, "V", INK, 20),
        _line(70, 330, 430, 90, RED, 4),
        _txt(360, 120, "slope = 1/R", RED, 16, anchor="start"),
        _txt(270, 385, "V ∝ I at constant temperature", INK, 16),
        f'<circle cx="250" cy="210" r="4" fill="{INK}"/>',
    ]
    return _render(key, _svg("".join(body), 520, 410), 660, 520)


def resistors_combo(key):
    """Resistors in series and in parallel, side by side."""
    body = [_txt(170, 40, "Series", INK, 18), _txt(480, 40, "Parallel", INK, 18)]
    # series: three resistors in a line
    y = 130
    xs = 60
    body.append(f'<line x1="{xs}" y1="{y}" x2="{xs+20}" y2="{y}" '
                f'stroke="{INK}" stroke-width="3"/>')
    x = xs + 20
    for i, lab in enumerate(["R1", "R2", "R3"]):
        body.append(f'<rect x="{x}" y="{y-13}" width="50" height="26" '
                    f'fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>')
        body.append(_txt(x+25, y-22, lab, PURPLE, 14))
        x += 50
        body.append(f'<line x1="{x}" y1="{y}" x2="{x+22}" y2="{y}" '
                    f'stroke="{INK}" stroke-width="3"/>')
        x += 22
    body.append(_cell(xs+5, y+90))
    body.append(f'<path d="M{xs} {y} L{xs} {y+90} M{xs} {y+90} L{xs+5} {y+90} '
                f'M{xs+17} {y+90} L{x} {y+90} L{x} {y}" fill="none" '
                f'stroke="{INK}" stroke-width="3"/>')
    body.append(_txt(180, 250, "R = R₁ + R₂ + R₃", PURPLE, 16))
    # parallel: three resistors between two rails
    px1, px2 = 430, 620
    body.append(f'<line x1="{px1}" y1="90" x2="{px2}" y2="90" stroke="{INK}" '
                f'stroke-width="3"/>')
    body.append(f'<line x1="{px1}" y1="200" x2="{px2}" y2="200" '
                f'stroke="{INK}" stroke-width="3"/>')
    for i, bx in enumerate([460, 525, 590]):
        body.append(f'<rect x="{bx-13}" y="120" width="26" height="50" '
                    f'fill="#FFFFFF" stroke="{INK}" stroke-width="3"/>')
        body.append(f'<line x1="{bx}" y1="90" x2="{bx}" y2="120" '
                    f'stroke="{INK}" stroke-width="3"/>')
        body.append(f'<line x1="{bx}" y1="170" x2="{bx}" y2="200" '
                    f'stroke="{INK}" stroke-width="3"/>')
    body.append(_cell(525, 250))
    body.append(f'<path d="M{px1} 90 L{px1} 250 L519 250 M531 250 L{px2} 250 '
                f'L{px2} 200" fill="none" stroke="{INK}" stroke-width="3"/>')
    body.append(_txt(525, 295, "1/R = 1/R₁ + 1/R₂ + 1/R₃", PURPLE, 15))
    return _render(key, _svg("".join(body), 700, 320), 940, 430)


def three_pin_plug(key):
    """A 3-pin plug: live (with fuse), neutral and a longer, thicker earth."""
    body = [
        f'<rect x="180" y="120" width="280" height="300" rx="30" '
        f'fill="#EAEDF1" stroke="{INK}" stroke-width="3"/>',
        _txt(150, 175, "Three-pin", INK, 17, anchor="end"),
        _txt(150, 198, "plug", INK, 17, anchor="end"),
        # earth pin (top, longer & thicker)
        f'<rect x="300" y="40" width="40" height="90" rx="6" fill="#2A9D8F" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(420, 70, "Earth (E)", "#1B7A6E", 15, anchor="start"),
        _txt(420, 92, "green/yellow", MUT, 12, anchor="start"),
        # live pin (bottom-left) with fuse
        f'<rect x="220" y="420" width="34" height="70" rx="5" fill="#8B5A2B" '
        f'stroke="{INK}" stroke-width="2"/>',
        f'<rect x="214" y="300" width="46" height="70" rx="6" fill="#FFE2C2" '
        f'stroke="{INK}" stroke-width="2"/>', _txt(237, 342, "fuse", "#8B5A2B", 12),
        _txt(150, 470, "Live (L)", "#8B5A2B", 15, anchor="end"),
        _txt(150, 492, "brown", MUT, 12, anchor="end"),
        # neutral pin (bottom-right)
        f'<rect x="386" y="420" width="34" height="70" rx="5" fill="#2563EB" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(500, 470, "Neutral (N)", "#1E40AF", 15, anchor="start"),
        _txt(500, 492, "blue", MUT, 12, anchor="start"),
        # internal wires
        f'<line x1="320" y1="130" x2="320" y2="200" stroke="#2A9D8F" '
        f'stroke-width="4"/>',
        f'<line x1="237" y1="300" x2="237" y2="240" stroke="#8B5A2B" '
        f'stroke-width="4"/>',
        f'<line x1="403" y1="420" x2="403" y2="240" stroke="#2563EB" '
        f'stroke-width="4"/>',
        _txt(320, 540, "Earth pin is longer & thicker; fuse goes in the live "
                       "wire", INK, 14),
    ]
    return _render(key, _svg("".join(body), 640, 560), 700, 613)


def power_transmission(key):
    """Generating station → step-up → transmission lines → step-down → home."""
    def box(x, w, label, col):
        return (f'<rect x="{x}" y="150" width="{w}" height="70" rx="8" '
                f'fill="{col}" stroke="{INK}" stroke-width="2"/>'
                + _txt(x + w / 2, 192, label, "#FFFFFF", 14))
    body = [
        box(30, 110, "Power\\nstation", "#6B7280"),
        box(190, 90, "Step-up\\ntransformer", ORANGE),
        box(380, 120, "Transmission\\n(high voltage)", PURPLE),
        box(560, 90, "Step-down\\ntransformer", ORANGE),
        box(720, 80, "Home", TEAL),
    ]
    # fix multi-line labels (svg text doesn't wrap) -> redo labels manually
    body = [
        f'<rect x="30" y="150" width="110" height="70" rx="8" fill="#6B7280" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(85, 180, "Power", "#FFFFFF", 14), _txt(85, 202, "station",
                                                    "#FFFFFF", 14),
        f'<rect x="190" y="150" width="100" height="70" rx="8" fill="{ORANGE}" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(240, 180, "Step-up", "#FFFFFF", 13), _txt(240, 202, "↑ voltage",
                                                       "#FFFFFF", 13),
        f'<rect x="345" y="150" width="150" height="70" rx="8" fill="{PURPLE}" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(420, 180, "Transmission", "#FFFFFF", 13),
        _txt(420, 202, "high voltage", "#FFFFFF", 13),
        f'<rect x="550" y="150" width="100" height="70" rx="8" fill="{ORANGE}" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(600, 180, "Step-down", "#FFFFFF", 13),
        _txt(600, 202, "↓ voltage", "#FFFFFF", 13),
        f'<rect x="705" y="150" width="80" height="70" rx="8" fill="{TEAL}" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(745, 188, "Home", "#FFFFFF", 14),
    ]
    for x in (140, 290, 495, 650):
        body.append(_line(x, 185, x + 50, 185, INK, 3, marker="arrow"))
    body.insert(0, _txt(400, 60, "Power from the station to your home", INK, 18))
    body.append(_txt(400, 280, "Voltage is stepped up for transmission "
                               "(less loss), then stepped down for use",
                     MUT, 14))
    return _render(key, _svg("".join(body), 820, 320), 1000, 390)


def field_straight_wire(key):
    """Concentric magnetic field lines around a current-carrying wire."""
    cx, cy = 300, 230
    body = [
        f'<rect x="60" y="200" width="480" height="60" fill="#F0F2F5"/>',
        _txt(300, 60, "Magnetic field around a straight wire", INK, 17),
        # wire (coming out of the page)
        f'<circle cx="{cx}" cy="{cy}" r="16" fill="#FFFFFF" stroke="{INK}" '
        f'stroke-width="3"/>',
        f'<circle cx="{cx}" cy="{cy}" r="4" fill="{INK}"/>',
        _txt(cx, cy + 60, "current out of page", TEAL, 14),
    ]
    for r in (50, 85, 120):
        body.append(f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="none" '
                    f'stroke="{PURPLE}" stroke-width="2.5"/>')
        # arrowhead on each circle (anticlockwise for current out of page)
        body.append(f'<path d="M {cx+r} {cy-8} L {cx+r-9} {cy} L {cx+r} {cy+8}" '
                    f'fill="none" stroke="{PURPLE}" stroke-width="2.5"/>')
    body.append(_txt(300, 400, "Right-hand thumb = current; curled fingers = "
                               "field direction", MUT, 14))
    return _render(key, _svg("".join(body), 600, 430), 760, 545)


def solenoid_field(key):
    """A current-carrying solenoid behaves like a bar magnet."""
    body = [_txt(320, 50, "A solenoid (electromagnet)", INK, 17)]
    # coils
    x = 150
    for i in range(7):
        body.append(f'<ellipse cx="{x}" cy="200" rx="14" ry="55" fill="none" '
                    f'stroke="{INK}" stroke-width="3"/>')
        x += 45
    # field lines through and around
    for dy in (0,):
        body.append(f'<path d="M150 200 L470 200" stroke="{PURPLE}" '
                    f'stroke-width="3" marker-end="url(#arrowP)"/>')
    body += [
        f'<path d="M470 200 C 560 200 560 90 470 120 C 250 150 200 150 150 200" '
        f'fill="none" stroke="{PURPLE}" stroke-width="2"/>',
        f'<path d="M470 200 C 560 200 560 310 470 280 C 250 250 200 250 150 200" '
        f'fill="none" stroke="{PURPLE}" stroke-width="2"/>',
        _txt(120, 205, "N", RED, 24, anchor="end"),
        _txt(500, 205, "S", BLUE, 24, anchor="start"),
        _txt(320, 380, "Field like a bar magnet; reverse the current to swap "
                       "the poles", MUT, 14),
    ]
    return _render(key, _svg("".join(body), 640, 410), 840, 538)


def dc_motor(key):
    """A current-carrying coil in a magnetic field experiences a turning
    force (simple DC motor)."""
    body = [
        _txt(320, 45, "Force on a coil — the DC motor", INK, 17),
        # magnet poles
        f'<rect x="40" y="120" width="70" height="180" fill="#E63946" '
        f'stroke="{INK}" stroke-width="2"/>', _txt(75, 215, "N", "#FFFFFF", 26),
        f'<rect x="490" y="120" width="70" height="180" fill="#2563EB" '
        f'stroke="{INK}" stroke-width="2"/>', _txt(525, 215, "S", "#FFFFFF", 26),
        # field lines N->S
    ]
    for y in (150, 200, 250):
        body.append(_line(110, y, 490, y, MUT, 1.5, marker="arrow"))
    body += [
        # coil
        f'<rect x="230" y="150" width="140" height="120" fill="none" '
        f'stroke="{PURPLE}" stroke-width="4"/>',
        # forces (up on one side, down on the other)
        _line(230, 150, 230, 95, TEAL, 3, marker="arrowT"),
        _line(370, 270, 370, 325, TEAL, 3, marker="arrowT"),
        _txt(205, 90, "force", TEAL, 13, anchor="end"),
        _txt(395, 330, "force", TEAL, 13, anchor="start"),
        # commutator
        f'<rect x="270" y="285" width="60" height="26" fill="#C8A24B" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(300, 340, "split-ring commutator", MUT, 13),
        _txt(320, 380, "Opposite forces on the two sides turn the coil", MUT,
             14),
    ]
    return _render(key, _svg("".join(body), 640, 400), 860, 538)


def emi_coil(key):
    """Electromagnetic induction: moving a magnet near a coil induces a
    current (shown on a galvanometer)."""
    body = [
        _txt(320, 45, "Electromagnetic induction", INK, 17),
        # coil
    ]
    x = 300
    for i in range(5):
        body.append(f'<ellipse cx="{x}" cy="200" rx="12" ry="50" fill="none" '
                    f'stroke="{INK}" stroke-width="3"/>')
        x += 30
    body += [
        # bar magnet moving toward coil
        f'<rect x="120" y="175" width="110" height="50" fill="#888" '
        f'stroke="{INK}" stroke-width="2"/>',
        f'<rect x="120" y="175" width="55" height="50" fill="#E63946"/>',
        _txt(147, 207, "N", "#FFFFFF", 20), _txt(202, 207, "S", "#FFFFFF", 20),
        _line(150, 130, 250, 130, ORANGE, 3, marker="arrowO"),
        _txt(200, 118, "move", ORANGE, 13),
        # wires to galvanometer
        f'<line x1="300" y1="250" x2="300" y2="330" stroke="{INK}" '
        f'stroke-width="2"/>',
        f'<line x1="420" y1="250" x2="420" y2="330" stroke="{INK}" '
        f'stroke-width="2"/>',
        f'<line x1="300" y1="330" x2="335" y2="330" stroke="{INK}" '
        f'stroke-width="2"/>',
        f'<line x1="385" y1="330" x2="420" y2="330" stroke="{INK}" '
        f'stroke-width="2"/>',
        f'<circle cx="360" cy="330" r="26" fill="#FFFFFF" stroke="{INK}" '
        f'stroke-width="3"/>', _txt(360, 338, "G", TEAL, 20),
        _txt(360, 385, "Moving the magnet induces a current (G deflects)", MUT,
             14),
    ]
    return _render(key, _svg("".join(body), 640, 410), 840, 538)


def heating_curve(key):
    """Temperature vs heat added for ice → water → steam (two plateaus)."""
    body = [
        _line(70, 350, 70, 50, INK, 3, marker="arrow"),
        _line(70, 350, 600, 350, INK, 3, marker="arrow"),
        _txt(40, 50, "Temp", INK, 16), _txt(600, 380, "Heat added →", INK, 15),
        # segments
        # ice warming
        _line(70, 320, 140, 270, RED, 4),
        # melting plateau (0 C)
        _line(140, 270, 260, 270, BLUE, 4),
        # water warming
        _line(260, 270, 360, 130, RED, 4),
        # boiling plateau (100 C)
        _line(360, 130, 500, 130, BLUE, 4),
        # steam warming
        _line(500, 130, 570, 90, RED, 4),
        # dashed level lines
        f'<line x1="70" y1="270" x2="140" y2="270" stroke="{MUT}" '
        f'stroke-width="1" stroke-dasharray="4 4"/>',
        f'<line x1="70" y1="130" x2="360" y2="130" stroke="{MUT}" '
        f'stroke-width="1" stroke-dasharray="4 4"/>',
        _txt(55, 275, "0°C", MUT, 13, anchor="end"),
        _txt(55, 135, "100°C", MUT, 13, anchor="end"),
        # labels
        _txt(200, 258, "melting", BLUE, 13),
        _txt(430, 118, "boiling", BLUE, 13),
        _txt(105, 305, "ice", RED, 12),
        _txt(310, 215, "water", RED, 12),
        _txt(535, 105, "steam", RED, 12),
        _txt(335, 60, "Plateaus: heat goes to latent heat, not temperature",
             INK, 14),
    ]
    return _render(key, _svg("".join(body), 640, 400), 880, 550)


def calorimeter(key):
    """A calorimeter with stirrer, thermometer and insulating jacket."""
    body = [
        # outer insulating jacket
        f'<rect x="120" y="150" width="400" height="240" rx="10" '
        f'fill="#EFE7D8" stroke="{INK}" stroke-width="2"/>',
        _txt(320, 415, "insulating jacket (lagging)", MUT, 13),
        # inner copper vessel
        f'<rect x="200" y="190" width="240" height="190" rx="6" '
        f'fill="#F6C28B" stroke="{INK}" stroke-width="3"/>',
        # liquid
        f'<rect x="206" y="250" width="228" height="124" fill="#BFD8F2"/>',
        _txt(320, 320, "liquid", "#27496D", 15),
        _txt(455, 300, "copper", "#A05A2C", 13, anchor="start"),
        # thermometer
        f'<rect x="270" y="80" width="14" height="200" rx="6" fill="#FFFFFF" '
        f'stroke="{INK}" stroke-width="2"/>',
        f'<circle cx="277" cy="285" r="11" fill="{RED}"/>',
        f'<rect x="273" y="150" width="8" height="130" fill="{RED}"/>',
        _txt(277, 70, "thermometer", MUT, 13),
        # stirrer
        f'<line x1="370" y1="95" x2="370" y2="300" stroke="{INK}" '
        f'stroke-width="3"/>',
        f'<line x1="350" y1="300" x2="390" y2="300" stroke="{INK}" '
        f'stroke-width="3"/>',
        _txt(395, 110, "stirrer", MUT, 13, anchor="start"),
        _txt(320, 50, "Calorimeter (method of mixtures)", INK, 17),
    ]
    return _render(key, _svg("".join(body), 640, 440), 760, 523)


def liquid_pressure(key):
    """A tank with holes at three depths: deeper holes squirt water further,
    showing pressure increases with depth."""
    body = [
        f'<rect x="120" y="80" width="200" height="300" fill="{WATER}" '
        f'stroke="{INK}" stroke-width="3"/>',
        _line(120, 80, 320, 80, INK, 2),
        _txt(220, 60, "water", "#27496D", 16),
    ]
    # three jets from the right wall at increasing depth -> increasing range
    for (y, reach, col) in [(150, 80, TEAL), (240, 150, BLUE), (330, 230, PURPLE)]:
        body.append(f'<path d="M320 {y} Q {320+reach*0.6} {y+10} '
                    f'{320+reach} {y+90}" fill="none" stroke="{col}" '
                    f'stroke-width="3"/>')
        body.append(f'<circle cx="320" cy="{y}" r="3" fill="{INK}"/>')
    body += [
        _txt(560, 380, "Deeper hole → greater pressure → water travels "
                       "further", INK, 14, anchor="end"),
        _txt(360, 150, "shallow", TEAL, 13, anchor="start"),
        _txt(430, 240, "deeper", BLUE, 13, anchor="start"),
        _txt(540, 330, "deepest", PURPLE, 13, anchor="start"),
        _txt(220, 410, "Pressure in a liquid increases with depth", INK, 15),
    ]
    return _render(key, _svg("".join(body), 600, 440), 800, 587)


def hydraulic_press(key):
    """Pascal's law: a small force on a narrow piston gives a large force on a
    wide piston."""
    body = [
        # connected vessel: narrow column (left) + wide column (right)
        f'<path d="M120 220 L120 330 L540 330 L540 220 L420 220 L420 160 '
        f'L320 160 L320 220 L240 220 L240 150 L170 150 L170 220 Z" '
        f'fill="{WATER}" stroke="{INK}" stroke-width="3"/>',
        # small piston (left, NARROW) with small input force
        f'<rect x="168" y="132" width="74" height="20" fill="#9AA1AB" '
        f'stroke="{INK}" stroke-width="2"/>',
        _line(205, 132, 205, 80, RED, 3, marker="arrowR"),
        _txt(205, 68, "small force f", RED, 14),
        _txt(205, 248, "area a", MUT, 12),
        # large piston (right, WIDE) with large output force
        f'<rect x="318" y="142" width="104" height="20" fill="#9AA1AB" '
        f'stroke="{INK}" stroke-width="2"/>',
        _line(370, 142, 370, 78, TEAL, 7, marker="arrowT"),
        _txt(370, 66, "large force F", TEAL, 14),
        _txt(370, 250, "area A", MUT, 12),
        _txt(330, 370, "Same pressure everywhere → a small force lifts a "
                       "big load", INK, 14),
        _txt(330, 398, "f / a  =  F / A   (Pascal's law)", PURPLE, 16),
    ]
    return _render(key, _svg("".join(body), 660, 420), 860, 547)


def barometer(key):
    """A simple mercury barometer measuring atmospheric pressure (76 cm)."""
    body = [
        # trough of mercury
        f'<rect x="120" y="350" width="220" height="50" fill="#B0B0B8" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(230, 420, "mercury trough", MUT, 13),
        # tube
        f'<rect x="200" y="70" width="44" height="285" fill="#B0B0B8" '
        f'stroke="{INK}" stroke-width="2"/>',
        # vacuum at top
        f'<rect x="202" y="72" width="40" height="60" fill="#FFFFFF"/>',
        _txt(222, 105, "vacuum", MUT, 12),
        # mercury column height marker
        f'<line x1="270" y1="132" x2="270" y2="375" stroke="{ORANGE}" '
        f'stroke-width="2" marker-start="url(#arrowO)" '
        f'marker-end="url(#arrowO)"/>',
        _txt(300, 250, "76 cm", ORANGE, 16, anchor="start"),
        # atmospheric pressure arrows on trough
        _line(150, 320, 150, 348, BLUE, 3, marker="arrow"),
        _line(310, 320, 310, 348, BLUE, 3, marker="arrow"),
        _txt(230, 305, "atmospheric pressure", BLUE, 13),
        _txt(230, 55, "Mercury barometer", INK, 16),
    ]
    return _render(key, _svg("".join(body), 460, 450), 600, 587)


def upthrust_balance(key):
    """A spring balance reads less in water — apparent loss of weight =
    upthrust."""
    body = [_txt(320, 40, "Apparent loss in weight = upthrust", INK, 17)]

    def rig(x, reading, water, label):
        out = [
            # spring balance
            f'<rect x="{x-18}" y="70" width="36" height="90" rx="6" '
            f'fill="#FFFFFF" stroke="{INK}" stroke-width="2"/>',
            _txt(x, 120, reading, RED, 16),
            f'<line x1="{x}" y1="160" x2="{x}" y2="200" stroke="{INK}" '
            f'stroke-width="2"/>',
            # block
            f'<rect x="{x-26}" y="200" width="52" height="52" fill="#C8A24B" '
            f'stroke="{INK}" stroke-width="2"/>',
            _txt(x, 300, label, MUT, 14),
        ]
        if water:
            out.insert(0, f'<rect x="{x-90}" y="178" width="180" height="120" '
                          f'fill="{WATER}" stroke="{INK}" stroke-width="2"/>')
            out.insert(1, _txt(x+70, 195, "water", "#27496D", 12))
        return out
    body += rig(180, "5.0 N", False, "in air")
    body += rig(460, "3.0 N", True, "in water")
    body.append(_txt(320, 350, "Block weighs less in water — the water pushes "
                               "up with an upthrust of 2 N", INK, 14))
    return _render(key, _svg("".join(body), 640, 370), 860, 497)


def floatation(key):
    """A floating object: weight balanced by upthrust (weight of displaced
    liquid)."""
    body = [
        f'<rect x="80" y="170" width="440" height="200" fill="{WATER}" '
        f'stroke="{INK}" stroke-width="2"/>',
        _line(80, 170, 520, 170, INK, 2),
        # boat-like block, partly submerged
        f'<path d="M220 130 L380 130 L360 250 L240 250 Z" fill="#C8A24B" '
        f'stroke="{INK}" stroke-width="3"/>',
        _txt(300, 195, "floating body", "#7A5C1E", 14),
        # weight arrow down
        _line(300, 190, 300, 320, RED, 4, marker="arrowR"),
        _txt(300, 340, "Weight (down)", RED, 14),
        # upthrust arrow up
        _line(300, 250, 300, 150, TEAL, 4, marker="arrowT"),
        _txt(300, 110, "Upthrust (up)", TEAL, 14),
        _txt(300, 395, "Floats when Upthrust = Weight = weight of displaced "
                       "liquid", INK, 14),
    ]
    return _render(key, _svg("".join(body), 600, 420), 760, 532)


def anomalous_water(key):
    """Density of water vs temperature, peaking at 4 deg C."""
    import math as _m
    body = [
        _line(70, 320, 70, 50, INK, 3, marker="arrow"),
        _line(70, 320, 520, 320, INK, 3, marker="arrow"),
        _txt(45, 50, "Density", INK, 15), _txt(470, 350, "Temperature (°C)",
                                               INK, 14),
    ]
    # stylised (exaggerated) curve: rises to a peak at 4 deg C then declines
    body.append(
        '<path d="M 90 150 C 100 120 120 110 136 110 '   # 0C -> peak ~4C
        'C 170 110 200 150 260 200 '                      # decline
        'C 330 250 410 280 500 300" '                     # gentle tail
        f'fill="none" stroke="{BLUE}" stroke-width="4"/>')
    body += [
        f'<line x1="136" y1="110" x2="136" y2="320" stroke="{ORANGE}" '
        f'stroke-width="1.5" stroke-dasharray="4 4"/>',
        f'<circle cx="136" cy="110" r="6" fill="{ORANGE}"/>',
        _txt(150, 100, "max density at 4°C", ORANGE, 14, anchor="start"),
        _txt(136, 340, "4", MUT, 13),
        _txt(300, 380, "Water is densest at 4°C — it expands when cooled "
                       "below this", INK, 14),
    ]
    return _render(key, _svg("".join(body), 560, 400), 720, 514)


def greenhouse_effect(key):
    """Sunlight in, Earth re-radiates heat, greenhouse gases trap some."""
    body = [
        f'<rect x="0" y="300" width="600" height="80" fill="#7CB342"/>',
        _txt(300, 350, "Earth's surface", "#2E5A12", 14),
        # gas layer
        f'<rect x="40" y="120" width="520" height="40" fill="#D7E8F5" '
        f'opacity="0.8" stroke="{MUT}" stroke-width="1"/>',
        _txt(300, 110, "greenhouse gases (CO₂)", MUT, 13),
        # sun
        f'<circle cx="80" cy="60" r="30" fill="{GOLD}"/>',
        _txt(80, 110, "Sun", MUT, 13),
        # incoming sunlight (passes through)
        _line(110, 80, 250, 300, GOLD, 4, marker="arrowO"),
        _txt(150, 200, "sunlight in", "#B5701F", 13, anchor="start"),
        # re-radiated heat from earth (some escapes, some trapped)
        _line(330, 300, 360, 160, RED, 3, marker="arrowR"),
        _line(360, 160, 330, 300, RED, 3, marker="arrowR"),  # reflected back
        _line(420, 300, 470, 130, RED, 3, marker=None),
        _line(470, 160, 470, 90, RED, 3, marker="arrowR"),  # some escapes
        _txt(380, 230, "heat radiated", RED, 12, anchor="start"),
        _txt(300, 200, "trapped ↺", RED, 13),
        _txt(300, 405, "Gases trap heat radiated by the Earth, warming the "
                       "planet", INK, 14),
    ]
    return _render(key, _svg("".join(body), 600, 430), 760, 545)


def bimetallic_strip(key):
    """A bimetallic strip bends on heating (two metals expand differently)."""
    body = [
        _txt(300, 45, "Bimetallic strip bends on heating", INK, 16),
        # before
        f'<rect x="80" y="110" width="200" height="16" fill="#D98C3F" '
        f'stroke="{INK}" stroke-width="1.5"/>',
        f'<rect x="80" y="126" width="200" height="16" fill="#9AA1AB" '
        f'stroke="{INK}" stroke-width="1.5"/>',
        _txt(180, 170, "cold — straight", MUT, 13),
        # after (curved): two arcs
        f'<path d="M340 130 Q 450 130 520 220" fill="none" stroke="#D98C3F" '
        f'stroke-width="16"/>',
        f'<path d="M340 146 Q 450 150 512 232" fill="none" stroke="#9AA1AB" '
        f'stroke-width="16"/>',
        _txt(430, 270, "hot — bends toward the metal that expands less",
             MUT, 13),
        _txt(120, 95, "brass", "#B5701F", 12),
        _txt(120, 158, "iron", MUT, 12),
    ]
    return _render(key, _svg("".join(body), 600, 300), 820, 410)


def plane_mirror_image(key):
    """Object in front of a plane mirror forms a virtual image behind it."""
    mx = 300
    body = [
        # mirror (vertical) with hatching on the back
        f'<line x1="{mx}" y1="60" x2="{mx}" y2="360" stroke="{INK}" '
        f'stroke-width="4"/>',
        _txt(mx, 45, "mirror", MUT, 14),
        # object arrow
        _line(160, 300, 160, 200, ORANGE, 4, marker="arrowO"),
        _txt(160, 320, "object", ORANGE, 14),
        # virtual image (dashed) equal distance behind
        _line(440, 300, 440, 200, RED, 3, dash="6 5", marker="arrowR"),
        _txt(440, 320, "virtual image", RED, 14),
        # rays from object top to mirror and to eye
        _line(160, 200, 270, 250, TEAL, 2),
        _line(270, 250, 150, 130, TEAL, 2, marker="arrowT"),
        _line(270, 250, 440, 200, MUT, 1.5, dash="5 5"),  # apparent ray
        f'<circle cx="135" cy="120" r="13" fill="none" stroke="{INK}" '
        f'stroke-width="2"/>', _txt(135, 100, "eye", INK, 12),
        _txt(300, 395, "Image is as far behind as the object is in front "
                       "(virtual, erect, same size)", INK, 14),
    ]
    return _render(key, _svg("".join(body), 600, 420), 760, 532)


def _mirror_arc(cx, cy, r, concave=True):
    if concave:
        return (f'<path d="M {cx} {cy-90} A {r} {r} 0 0 0 {cx} {cy+90}" '
                f'fill="none" stroke="{INK}" stroke-width="5"/>')
    return (f'<path d="M {cx} {cy-90} A {r} {r} 0 0 1 {cx} {cy+90}" '
            f'fill="none" stroke="{INK}" stroke-width="5"/>')


def concave_mirror_image(key):
    """Concave mirror: object beyond C -> real, inverted, diminished image."""
    cy = 220
    mx = 500
    body = [
        _line(60, cy, mx + 10, cy, MUT, 2),       # principal axis
        _mirror_arc(mx, cy, 240, True),
        f'<circle cx="320" cy="{cy}" r="3" fill="{MUT}"/>',  # C
        _txt(320, cy + 22, "C", MUT, 14),
        f'<circle cx="410" cy="{cy}" r="3" fill="{MUT}"/>',  # F
        _txt(410, cy + 22, "F", MUT, 14),
        # object beyond C
        _line(230, cy, 230, cy - 80, ORANGE, 4, marker="arrowO"),
        _txt(230, cy - 92, "object", ORANGE, 13),
        # ray parallel -> through F
        _line(230, cy - 80, mx, cy - 80, RED, 2.5),
        _line(mx, cy - 80, 360, cy + 40, RED, 2.5),
        # ray through C -> reflects back on itself
        _line(230, cy - 80, mx - 40, cy + 55, TEAL, 2.5),
        # image (between C and F): real inverted
        _line(370, cy, 370, cy + 38, PURPLE, 4, marker="arrowP"),
        _txt(372, cy + 58, "image", PURPLE, 13, anchor="start"),
        _txt(300, 40, "Concave mirror: object beyond C → real, inverted, "
                      "diminished", INK, 15),
    ]
    return _render(key, _svg("".join(body), 600, 360), 820, 492)


def convex_mirror_image(key):
    """Convex mirror: always a virtual, erect, diminished image behind."""
    cy = 200
    mx = 470
    body = [
        _line(60, cy, mx + 90, cy, MUT, 2),
        _mirror_arc(mx, cy, 240, False),
        f'<circle cx="{mx+95}" cy="{cy}" r="3" fill="{MUT}"/>',
        _txt(mx + 95, cy + 22, "F", MUT, 13),
        # object
        _line(220, cy, 220, cy - 80, ORANGE, 4, marker="arrowO"),
        _txt(220, cy - 92, "object", ORANGE, 13),
        # ray parallel -> reflects as if from F behind
        _line(220, cy - 80, mx, cy - 80, RED, 2.5),
        _line(mx, cy - 80, 120, cy - 20, RED, 2.5, marker="arrowR"),
        _line(mx, cy - 80, mx + 95, cy, MUT, 1.5, dash="5 5"),
        # ray toward centre -> reflects
        _line(220, cy - 80, mx, cy - 36, TEAL, 2.5),
        _line(mx, cy - 36, 150, cy + 30, TEAL, 2.5, marker="arrowT"),
        # virtual image behind (small, erect)
        _line(mx + 55, cy, mx + 55, cy - 26, PURPLE, 4, marker="arrowP"),
        _txt(mx + 55, cy + 22, "image", PURPLE, 12),
        _txt(300, 40, "Convex mirror: always virtual, erect, diminished",
             INK, 15),
    ]
    return _render(key, _svg("".join(body), 640, 340), 860, 457)


def wave_terms(key):
    """A wave showing wavelength, amplitude, crest and trough."""
    import math as _m
    cx0, mid, amp = 70, 200, 70
    pts = []
    for i in range(0, 481):
        x = cx0 + i
        y = mid - amp * _m.sin(2 * _m.pi * i / 160)
        pts.append(f"{x},{y:.1f}")
    body = [
        _line(cx0, mid, cx0 + 480, mid, MUT, 1.5, dash="5 5"),
        f'<polyline points="{" ".join(pts)}" fill="none" stroke="{BLUE}" '
        f'stroke-width="3.5"/>',
        # wavelength (crest to crest): crest at i=40 and i=200 -> x=110, 270
        f'<line x1="110" y1="110" x2="270" y2="110" stroke="{ORANGE}" '
        f'stroke-width="2" marker-start="url(#arrowO)" '
        f'marker-end="url(#arrowO)"/>',
        _txt(190, 98, "wavelength λ", ORANGE, 14),
        # amplitude (mid to crest) at x=110
        f'<line x1="430" y1="200" x2="430" y2="130" stroke="{RED}" '
        f'stroke-width="2" marker-end="url(#arrowR)"/>',
        _txt(470, 165, "amplitude", RED, 13, anchor="start"),
        _txt(110, 95, "crest", TEAL, 12),
        _txt(190, 295, "trough", PURPLE, 12),
        _txt(300, 360, "Wavelength: crest to crest   •   Amplitude: rest to "
                       "crest", INK, 14),
    ]
    return _render(key, _svg("".join(body), 600, 390), 800, 520)


def circuit_symbols(key):
    """A chart of common circuit symbols."""
    body = [_txt(300, 35, "Common circuit symbols", INK, 17)]
    cells = [
        ("cell", lambda x, y: _cell(x + 30, y) + _line(x, y, x + 30, y, INK, 2)
         + _line(x + 42, y, x + 60, y, INK, 2)),
        ("battery", lambda x, y: _cell(x + 18, y) + _cell(x + 42, y)
         + _line(x, y, x + 18, y, INK, 2) + _line(x + 54, y, x + 60, y, INK, 2)),
        ("bulb", lambda x, y: f'<circle cx="{x+30}" cy="{y}" r="14" '
         f'fill="none" stroke="{INK}" stroke-width="2"/>'
         f'<line x1="{x+20}" y1="{y-10}" x2="{x+40}" y2="{y+10}" '
         f'stroke="{INK}" stroke-width="2"/>'
         f'<line x1="{x+20}" y1="{y+10}" x2="{x+40}" y2="{y-10}" '
         f'stroke="{INK}" stroke-width="2"/>'
         + _line(x, y, x + 16, y, INK, 2) + _line(x + 44, y, x + 60, y, INK, 2)),
        ("switch (open)", lambda x, y: f'<circle cx="{x+18}" cy="{y}" r="3" '
         f'fill="{INK}"/><circle cx="{x+44}" cy="{y}" r="3" fill="{INK}"/>'
         + _line(x, y, x + 18, y, INK, 2) + _line(x + 18, y, x + 42, y - 16, INK, 2)
         + _line(x + 44, y, x + 60, y, INK, 2)),
        ("resistor", lambda x, y: f'<rect x="{x+15}" y="{y-8}" width="30" '
         f'height="16" fill="none" stroke="{INK}" stroke-width="2"/>'
         + _line(x, y, x + 15, y, INK, 2) + _line(x + 45, y, x + 60, y, INK, 2)),
        ("ammeter", lambda x, y: f'<circle cx="{x+30}" cy="{y}" r="14" '
         f'fill="none" stroke="{INK}" stroke-width="2"/>'
         + _txt(x + 30, y + 5, "A", TEAL, 14)
         + _line(x, y, x + 16, y, INK, 2) + _line(x + 44, y, x + 60, y, INK, 2)),
        ("voltmeter", lambda x, y: f'<circle cx="{x+30}" cy="{y}" r="14" '
         f'fill="none" stroke="{INK}" stroke-width="2"/>'
         + _txt(x + 30, y + 5, "V", ORANGE, 14)
         + _line(x, y, x + 16, y, INK, 2) + _line(x + 44, y, x + 60, y, INK, 2)),
        ("wire", lambda x, y: _line(x, y, x + 60, y, INK, 2)),
    ]
    for i, (name, draw) in enumerate(cells):
        col = i % 2
        row = i // 2
        x = 80 + col * 260
        y = 90 + row * 75
        body.append(draw(x, y))
        body.append(_txt(x + 90, y + 5, name, MUT, 14, anchor="start"))
    return _render(key, _svg("".join(body), 600, 420), 760, 532)


def simple_circuit(key):
    """A simple circuit: cell, switch and a bulb in a loop."""
    L, R, T, B = 120, 480, 110, 320
    body = [
        f'<rect x="{L}" y="{T}" width="{R-L}" height="{B-T}" fill="none" '
        f'stroke="{INK}" stroke-width="3"/>',
        _cell(L, (T+B)//2), _txt(L-22, (T+B)//2+5, "cell", MUT, 14,
                                 anchor="end"),
        # bulb on top
        f'<circle cx="300" cy="{T}" r="20" fill="#FFF6CC" stroke="{INK}" '
        f'stroke-width="3"/>',
        f'<line x1="286" y1="{T-14}" x2="314" y2="{T+14}" stroke="{INK}" '
        f'stroke-width="2"/>',
        f'<line x1="286" y1="{T+14}" x2="314" y2="{T-14}" stroke="{INK}" '
        f'stroke-width="2"/>', _txt(300, T-32, "bulb", MUT, 14),
        # switch on bottom
        f'<circle cx="285" cy="{B}" r="4" fill="{INK}"/>'
        f'<circle cx="315" cy="{B}" r="4" fill="{INK}"/>',
        _line(285, B, 312, B-16, INK, 3), _txt(300, B+26, "switch", MUT, 14),
        _txt(300, 70, "A simple electric circuit", INK, 16),
    ]
    return _render(key, _svg("".join(body), 600, 380), 720, 456)


def bar_magnet_field(key):
    """Magnetic field lines of a bar magnet looping from N to S."""
    cy = 230
    nL, nR = 240, 360   # magnet left/right edges
    body = [
        f'<rect x="{nL}" y="{cy-28}" width="120" height="56" fill="#9AA1AB" '
        f'stroke="{INK}" stroke-width="2"/>',
        f'<rect x="{nL}" y="{cy-28}" width="60" height="56" fill="{RED}"/>',
        f'<rect x="300" y="{cy-28}" width="60" height="56" fill="{BLUE}"/>',
        _txt(270, cy+8, "N", "#FFFFFF", 22), _txt(330, cy+8, "S", "#FFFFFF", 22),
        _txt(300, 55, "Field lines loop from North to South outside the magnet",
             INK, 15),
        _txt(300, cy + 175, "Closest at the poles, where the field is "
                            "strongest", MUT, 14),
    ]
    # loops emerge from the N end (left), bulge out around, enter the S end
    for h in (55, 105, 160):
        # top loop
        body.append(
            f'<path d="M {nL} {cy} C {nL-h} {cy-h} {nR+h} {cy-h} {nR} {cy}" '
            f'fill="none" stroke="{PURPLE}" stroke-width="2"/>')
        # right-pointing arrowhead at the apex (N -> S)
        ay = cy - h * 0.72
        body.append(f'<path d="M {300-7} {ay-7} L {300+9} {ay} '
                    f'L {300-7} {ay+7} Z" fill="{PURPLE}"/>')
        # bottom loop (mirror)
        body.append(
            f'<path d="M {nL} {cy} C {nL-h} {cy+h} {nR+h} {cy+h} {nR} {cy}" '
            f'fill="none" stroke="{PURPLE}" stroke-width="2"/>')
        by = cy + h * 0.72
        body.append(f'<path d="M {300-7} {by-7} L {300+9} {by} '
                    f'L {300-7} {by+7} Z" fill="{PURPLE}"/>')
    return _render(key, _svg("".join(body), 600, 460), 800, 614)


def neutral_points(key):
    """A bar magnet in the Earth's field, showing two neutral points."""
    cy = 200
    body = [
        f'<rect x="240" y="{cy-25}" width="120" height="50" fill="#9AA1AB" '
        f'stroke="{INK}" stroke-width="2"/>',
        f'<rect x="240" y="{cy-25}" width="60" height="50" fill="{RED}"/>',
        f'<rect x="300" y="{cy-25}" width="60" height="50" fill="{BLUE}"/>',
        _txt(270, cy+7, "N", "#FFFFFF", 20), _txt(330, cy+7, "S", "#FFFFFF", 20),
        # Earth's uniform field (arrows pointing up = toward geographic north)
    ]
    for x in (120, 480):
        body.append(f'<line x1="{x}" y1="{cy+120}" x2="{x}" y2="{cy-120}" '
                    f'stroke="{TEAL}" stroke-width="2" '
                    f'marker-end="url(#arrowT)"/>')
    body += [
        _txt(120, cy+140, "Earth's field", TEAL, 13),
        # neutral points (on equatorial line, east & west)
        f'<circle cx="180" cy="{cy}" r="7" fill="none" stroke="{RED}" '
        f'stroke-width="2"/>',
        f'<circle cx="420" cy="{cy}" r="7" fill="none" stroke="{RED}" '
        f'stroke-width="2"/>',
        _txt(180, cy-18, "neutral point", RED, 12),
        _txt(420, cy-18, "neutral point", RED, 12),
        _txt(300, 50, "Neutral points: magnet's field cancels Earth's field",
             INK, 15),
        _txt(300, 400, "Net magnetic field is zero at a neutral point", MUT,
             14),
    ]
    return _render(key, _svg("".join(body), 600, 420), 800, 560)


def pendulum_energy(key):
    """A swinging pendulum converting between potential and kinetic energy."""
    px, py = 300, 70   # pivot
    body = [
        f'<circle cx="{px}" cy="{py}" r="5" fill="{INK}"/>',
        f'<line x1="{px}" y1="{py}" x2="{px}" y2="320" stroke="{MUT}" '
        f'stroke-width="1" stroke-dasharray="4 5"/>',
    ]
    # three positions: left top (PE max), bottom (KE max), right top (PE max)
    for (x, y, lab, col, pe, ke) in [
            (150, 250, "max PE", RED, True, False),
            (300, 330, "max KE", TEAL, False, True),
            (450, 250, "max PE", RED, True, False)]:
        body.append(f'<line x1="{px}" y1="{py}" x2="{x}" y2="{y}" '
                    f'stroke="{INK}" stroke-width="1.5" opacity="0.5"/>')
        body.append(f'<circle cx="{x}" cy="{y}" r="18" fill="{col}" '
                    f'stroke="{INK}" stroke-width="2"/>')
        body.append(_txt(x, y + 45, lab, col, 14))
    # swing arrows
    body += [
        f'<path d="M180 290 Q 240 340 290 332" fill="none" stroke="{PURPLE}" '
        f'stroke-width="2" marker-end="url(#arrowP)"/>',
        f'<path d="M310 332 Q 360 340 420 290" fill="none" stroke="{PURPLE}" '
        f'stroke-width="2" marker-end="url(#arrowP)"/>',
        _txt(300, 40, "A swinging pendulum: PE ⇄ KE", INK, 16),
        _txt(300, 390, "At the top: all potential energy.  At the bottom: all "
                       "kinetic energy.", MUT, 14),
    ]
    return _render(key, _svg("".join(body), 600, 420), 800, 560)


def states_of_matter(key):
    """Particle arrangement in solid, liquid and gas."""
    import random
    body = [_txt(330, 40, "Particles in solids, liquids and gases", INK, 16)]
    boxes = [(60, "Solid", "#F4C28B", "tightly packed, vibrate in place"),
             (260, "Liquid", "#BFD8F2", "close but can slide past each other"),
             (460, "Gas", "#D7E8F5", "far apart, move freely & fast")]
    for bx, name, col, desc in boxes:
        body.append(f'<rect x="{bx}" y="80" width="160" height="160" rx="8" '
                    f'fill="{col}" stroke="{INK}" stroke-width="2"/>')
        body.append(_txt(bx + 80, 70, name, INK, 16))
        random.seed(hash(name) % 1000)
        if name == "Solid":
            for r in range(4):
                for c in range(4):
                    cx = bx + 28 + c * 36
                    cy = 108 + r * 36
                    body.append(f'<circle cx="{cx}" cy="{cy}" r="11" '
                                f'fill="{INK}"/>')
        elif name == "Liquid":
            for _ in range(13):
                cx = bx + random.randint(20, 140)
                cy = 100 + random.randint(0, 130)
                body.append(f'<circle cx="{cx}" cy="{cy}" r="11" '
                            f'fill="{INK}"/>')
        else:
            for _ in range(7):
                cx = bx + random.randint(15, 145)
                cy = 95 + random.randint(0, 135)
                body.append(f'<circle cx="{cx}" cy="{cy}" r="10" '
                            f'fill="{INK}"/>')
        body.append(_txt(bx + 80, 262, desc, MUT, 11))
    body.append(_txt(330, 295, "Heating gives particles more energy: they "
                              "vibrate and move faster", MUT, 13))
    return _render(key, _svg("".join(body), 660, 320), 900, 436)


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


def gold_leaf_electroscope(key):
    """A gold-leaf electroscope with leaves diverging when charged."""
    body = [
        _txt(300, 45, "Gold-leaf electroscope (charged)", INK, 17),
        # metal disc / cap
        f'<rect x="220" y="80" width="160" height="18" rx="6" fill="#C9CDD4" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(300, 75, "metal disc", MUT, 13),
        # vertical metal rod
        f'<rect x="294" y="98" width="12" height="150" fill="#C9CDD4" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(445, 210, "metal rod", MUT, 13, anchor="start"),
        _line(438, 207, 312, 200, MUT, 1.2),
        # glass jar
        f'<rect x="170" y="150" width="260" height="250" rx="10" '
        f'fill="{GLASS}" fill-opacity="0.35" stroke="{INK}" stroke-width="2"/>',
        f'<rect x="200" y="130" width="200" height="26" rx="6" fill="#C9CDD4" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(455, 300, "glass jar", MUT, 13, anchor="start"),
        # two diverging gold leaves
        f'<polygon points="300,248 258,362 270,362 300,250" fill="{GOLD}" '
        f'stroke="{INK}" stroke-width="1.5"/>',
        f'<polygon points="300,248 342,362 330,362 300,250" fill="{GOLD}" '
        f'stroke="{INK}" stroke-width="1.5"/>',
        _txt(300, 392, "gold leaves diverge", "#9A7B00", 13),
        # like charges on the leaves
        _txt(252, 320, "–", RED, 26), _txt(348, 320, "–", RED, 26),
        _txt(300, 470, "Like charges on the leaves repel, so they spread apart",
             MUT, 15),
    ]
    return _render(key, _svg("".join(body), 600, 500), 700, 583)


def charge_interaction(key):
    """Like charges repel, unlike charges attract."""
    def ball(cx, cy, sign, col):
        s = (f'<circle cx="{cx}" cy="{cy}" r="34" fill="none" '
             f'stroke="{INK}" stroke-width="2.5"/>')
        s += _txt(cx, cy + 12, sign, col, 34)
        return s
    body = [
        _txt(300, 45, "How charges interact", INK, 18),
        # top row: like charges repel (force arrows point outward)
        ball(210, 140, "+", RED), ball(390, 140, "+", RED),
        _line(170, 140, 110, 140, MUT, 3, marker="arrow"),
        _line(430, 140, 490, 140, MUT, 3, marker="arrow"),
        _txt(300, 200, "Like charges REPEL", INK, 16),
        # bottom row: unlike charges attract (force arrows point inward)
        ball(160, 320, "+", RED), ball(440, 320, "–", BLUE),
        _line(208, 320, 270, 320, MUT, 3, marker="arrow"),
        _line(392, 320, 330, 320, MUT, 3, marker="arrow"),
        _txt(300, 385, "Unlike charges ATTRACT", INK, 16),
        _txt(300, 445, "Two of the same sign push apart; opposite signs pull "
                       "together", MUT, 14),
    ]
    return _render(key, _svg("".join(body), 600, 480), 760, 608)


if __name__ == "__main__":
    # smoke test
    for fn in [refraction_bending, glass_block, real_apparent_depth,
               prism_refraction, total_internal_reflection, reflection_law,
               optical_fibre, reflecting_prism]:
        print(fn(f"test_{fn.__name__}"))
