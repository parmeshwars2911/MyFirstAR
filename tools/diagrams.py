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
