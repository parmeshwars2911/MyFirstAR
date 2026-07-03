"""
Figures for the ICSE Class 9 "Pressure in Fluids and Atmospheric Pressure"
decks — one vector diagram per textbook figure (Fig 4.1 – 4.9).

Same contract as diagrams.py: each function returns a PNG path (SVG rasterised
with cairosvg into build/img/). Reuses the shared helpers/palette so the style
matches the rest of the catalog. These are the offline stand-ins for the
Qwen-Image figures; qwen_images.py can later drop AI PNGs into build/qwen/ that
the deck loads in preference to these.
"""
import os
import sys
import math

sys.path.insert(0, os.path.dirname(__file__))
from diagrams import (  # noqa: E402
    _svg, _line, _txt, _arc, _render, _esc,
    INK, MUT, TEAL, ORANGE, PURPLE, RED, BLUE, GLASS, WATER, GREEN, GOLD,
)
from diagrams_extra import (  # noqa: E402
    _circle, _rect, _poly, _ellipse, IRON, WOOD, FLAME,
)

BRICK = "#B4593B"
BRICK_D = "#8E4026"
STEEL = "#AEB8C2"
STEEL_D = "#7C8794"
GROUND = "#E7DFCF"


def _weight_arrow(x, y, label="Thrust = weight"):
    out = _line(x, y, x, y + 46, col=RED, w=4, marker="arrowR")
    out += _txt(x, y - 8, label, col=RED, size=13)
    return out


# ---------------------------------------------------------------------------
# Fig 4.1 — Thrust and pressure (same brick, two orientations)
# ---------------------------------------------------------------------------
def fig_4_1(key):
    vw, vh = 760, 400
    body = _rect(0, 330, vw, 70, fill=GROUND, stroke="none")
    body += _line(0, 330, vw, 330, col=MUT, w=2)
    body += _txt(vw / 2, 34, "Same brick, same weight — different pressure",
                 col=INK, size=18)

    # --- Left: standing on its small end (upright) -> large pressure ---
    x0 = 150
    body += _poly([(x0 - 34, 130), (x0 + 34, 130), (x0 + 34, 330),
                   (x0 - 34, 330)], fill=BRICK, stroke=INK, sw=2)
    body += _poly([(x0 + 34, 130), (x0 + 56, 108), (x0 + 56, 308),
                   (x0 + 34, 330)], fill=BRICK_D, stroke=INK, sw=2)
    body += _poly([(x0 - 34, 130), (x0 - 12, 108), (x0 + 56, 108),
                   (x0 + 34, 130)], fill="#C96B4C", stroke=INK, sw=2)
    body += _line(x0 + 10, 58, x0 + 10, 102, col=RED, w=4, marker="arrowR")
    body += _txt(x0 + 10, 50, "Thrust = weight", col=RED, size=13)
    # small contact -> presses in
    body += _line(x0 - 34, 336, x0 + 34, 336, col=RED, w=6)
    body += _txt(x0 + 10, 372, "small area", col=INK, size=14)
    body += _txt(x0 + 10, 392, "→ large pressure", col=RED, size=14)

    # --- Right: lying flat on its large face -> small pressure ---
    x1 = 540
    body += _poly([(x1 - 96, 268), (x1 + 96, 268), (x1 + 96, 330),
                   (x1 - 96, 330)], fill=BRICK, stroke=INK, sw=2)
    body += _poly([(x1 + 96, 268), (x1 + 118, 250), (x1 + 118, 312),
                   (x1 + 96, 330)], fill=BRICK_D, stroke=INK, sw=2)
    body += _poly([(x1 - 96, 268), (x1 - 74, 250), (x1 + 118, 250),
                   (x1 + 96, 268)], fill="#C96B4C", stroke=INK, sw=2)
    body += _weight_arrow(x1, 214)
    body += _line(x1 - 96, 336, x1 + 96, 336, col=TEAL, w=6)
    body += _txt(x1 + 10, 372, "large area", col=INK, size=14)
    body += _txt(x1 + 10, 392, "→ small pressure", col=TEAL, size=14)
    return _render(key, _svg(body, vw, vh), vw, vh)


# ---------------------------------------------------------------------------
# Fig 4.2 — Liquid pressure increases with depth (three jets)
# ---------------------------------------------------------------------------
def fig_4_2(key):
    vw, vh = 620, 440
    cx, cw = 120, 150          # container left edge, width
    top, bot = 70, 360
    body = _txt(vw / 2, 34, "Deeper hole → water spurts farther",
                col=INK, size=18)
    # container
    body += _rect(cx, top, cw, bot - top, fill=WATER, stroke=INK, sw=3)
    body += _line(cx, top, cx + cw, top, col=BLUE, w=3)
    body += _txt(cx + cw / 2, top - 12, "free surface", col=MUT, size=12)
    # ground line
    body += _line(cx, bot + 4, vw - 20, bot + 4, col=MUT, w=2)
    # three holes with parabolic jets
    holes = [(150, "#3E6F9E"), (240, TEAL), (320, RED)]
    for hy, col in holes:
        body += _circle(cx + cw, hy, 4, fill=INK, stroke="none")
        reach = (hy - top) * 1.15          # deeper -> longer reach
        pts = []
        for i in range(0, 41):
            t = i / 40.0
            x = cx + cw + t * reach
            y = hy + (bot - hy) * (t * t)
            pts.append((round(x, 1), round(y, 1)))
        body += ('<polyline points="' +
                 " ".join(f"{x},{y}" for x, y in pts) +
                 f'" fill="none" stroke="{col}" stroke-width="3"/>')
    body += _txt(cx - 12, 150, "shallow", col=MUT, size=12, anchor="end")
    body += _txt(cx - 12, 320, "deep", col=RED, size=12, anchor="end")
    body += _line(cx - 40, 90, cx - 40, 340, col=INK, w=2, marker="arrow")
    body += _txt(cx - 58, 220, "depth ↑", col=INK, size=13, anchor="middle")
    return _render(key, _svg(body, vw, vh), vw, vh)


# ---------------------------------------------------------------------------
# Fig 4.3 — Pressure at a depth: liquid column PQRS of area A at depth h
# ---------------------------------------------------------------------------
def fig_4_3(key):
    vw, vh = 620, 440
    cx, cw = 110, 400
    top, bot = 90, 380
    body = _txt(vw / 2, 34, "Pressure at a depth h  (P = h ρ g)",
                col=INK, size=18)
    body += _rect(cx, top, cw, bot - top, fill=WATER, stroke=INK, sw=3)
    # free surface XY
    body += _line(cx, top, cx + cw, top, col=BLUE, w=3)
    body += _txt(cx - 8, top + 4, "X", col=INK, size=15, anchor="end")
    body += _txt(cx + cw + 8, top + 4, "Y", col=INK, size=15, anchor="start")
    body += _txt(cx + cw + 30, top + 4, "free surface", col=MUT, size=12,
                 anchor="start")
    # column PQRS (S,R top ; P,Q bottom) at depth h
    colx, colw = 250, 130
    coltop = top
    colbot = 300
    body += _rect(colx, coltop, colw, colbot - coltop, fill="#BFE0EA",
                  stroke=INK, sw=2)
    for lbl, px, py, anc in [("S", colx, coltop, "end"),
                             ("R", colx + colw, coltop, "start"),
                             ("P", colx, colbot, "end"),
                             ("Q", colx + colw, colbot, "start")]:
        body += _circle(px, py, 3, fill=INK, stroke="none")
        dy = -6 if py == coltop else 16
        body += _txt(px + (-8 if anc == "end" else 8), py + dy, lbl, col=INK,
                     size=14, anchor=anc)
    # base surface PQ (area A)
    body += _line(colx, colbot, colx + colw, colbot, col=RED, w=4)
    body += _txt(colx + colw / 2, colbot + 22, "area A", col=RED, size=13)
    # depth h dimension
    hx = colx + colw + 34
    body += _line(hx, coltop, hx, colbot, col=INK, w=2, marker="arrow")
    body += _line(hx, colbot, hx, coltop, col=INK, w=2, marker="arrow")
    body += _txt(hx + 14, (coltop + colbot) / 2, "h", col=INK, size=16,
                 anchor="start")
    body += _txt(cx + cw / 2, bot - 16,
                 "column PQRS of liquid density ρ", col=MUT, size=13)
    return _render(key, _svg(body, vw, vh), vw, vh)


# ---------------------------------------------------------------------------
# Fig 4.4 — Wall of a dam is thicker at the bottom
# ---------------------------------------------------------------------------
def fig_4_4(key):
    vw, vh = 660, 420
    ground = 350
    body = _txt(vw / 2, 32, "A dam wall is built thicker at its base",
                col=INK, size=18)
    # land / ground
    body += _rect(0, ground, vw, vh - ground, fill=WOOD, stroke="none")
    body += _txt(70, ground + 34, "LAND", col=INK, size=14)
    # water on the left
    wtop = 110
    body += _poly([(60, wtop), (300, wtop), (300, ground), (60, ground)],
                  fill=WATER, stroke="none")
    body += _line(60, wtop, 300, wtop, col=BLUE, w=3)
    body += _txt(150, wtop - 10, "WATER", col=INK, size=14)
    # dam: triangle thin at top, thick at bottom
    body += _poly([(300, wtop - 20), (335, wtop - 20), (400, ground),
                   (300, ground)], fill="#C9CDD4", stroke=INK, sw=2)
    # brick hatching
    for yy in range(int(wtop) + 10, ground, 24):
        frac = (yy - wtop) / (ground - wtop)
        rx = 300 + (400 - 300) * frac
        body += _line(300, yy, rx, yy, col=MUT, w=1)
    body += _txt(430, 150, "WALL OF DAM", col=INK, size=13, anchor="start")
    # pressure arrows: short at top, long at bottom
    for i, yy in enumerate(range(int(wtop) + 30, ground, 46)):
        ln = 24 + i * 20
        body += _line(300 - ln, yy, 300, yy, col=RED, w=3, marker="arrowR")
    body += _line(40, wtop + 20, 40, ground - 10, col=RED, w=2,
                  marker="arrow")
    body += _txt(30, (wtop + ground) / 2, "pressure ↑", col=RED, size=12,
                 anchor="middle")
    body += _txt(500, ground - 44, "thickness", col=INK, size=12,
                 anchor="start")
    body += _txt(500, ground - 28, "increases", col=INK, size=12,
                 anchor="start")
    body += _txt(500, ground - 12, "downward", col=INK, size=12,
                 anchor="start")
    return _render(key, _svg(body, vw, vh), vw, vh)


# ---------------------------------------------------------------------------
# Fig 4.5 — Demonstration of Pascal's law (flask with tubes)
# ---------------------------------------------------------------------------
def fig_4_5(key):
    vw, vh = 560, 440
    cx = vw / 2
    body = _txt(cx, 30, "Pascal's law: jets rise to the same height",
                col=INK, size=17)
    # dashed 'same height' line
    same_y = 96
    body += _line(70, same_y, vw - 70, same_y, col=RED, w=2, dash="7 6")
    body += _txt(vw - 64, same_y - 4, "same", col=RED, size=11,
                 anchor="start")
    body += _txt(vw - 64, same_y + 12, "height", col=RED, size=11,
                 anchor="start")
    # flask (round bottom)
    body += _circle(cx, 320, 78, fill=WATER, stroke=INK, sw=3)
    body += _rect(cx - 20, 170, 40, 90, fill=WATER, stroke=INK, sw=3)
    body += _txt(cx, 330, "water", col="#0B3A52", size=13)
    # piston + push
    body += _rect(cx - 26, 150, 52, 22, fill=STEEL, stroke=INK, sw=2)
    body += _rect(cx - 6, 120, 12, 32, fill=STEEL_D, stroke=INK, sw=2)
    body += _line(cx, 108, cx, 138, col=INK, w=4, marker="arrow")
    body += _txt(cx, 100, "PUSH", col=INK, size=13)
    # four side tubes with little jets reaching same_y
    for tx, ty in [(cx - 78, 300), (cx + 78, 300),
                   (cx - 48, 250), (cx + 48, 250)]:
        ang = math.atan2(ty - 320, tx - cx)
        ex = tx + 26 * math.cos(ang)
        ey = ty + 26 * math.sin(ang)
        body += _line(tx, ty, ex, ey, col=INK, w=6)   # tube stub
        body += _line(ex, ey, ex, same_y, col=BLUE, w=3)  # jet up
    body += _txt(cx, 430, "water-tight flask with narrow open tubes",
                 col=MUT, size=12)
    return _render(key, _svg(body, vw, vh), vw, vh)


# ---------------------------------------------------------------------------
# Fig 4.6 — Principle of a hydraulic machine (two pistons)
# ---------------------------------------------------------------------------
def fig_4_6(key):
    vw, vh = 700, 400
    body = _txt(vw / 2, 30, "A small force F₁ lifts a large load F₂",
                col=INK, size=18)
    liq_top = 250
    # connecting horizontal vessel
    body += _rect(90, liq_top, 520, 70, fill=WATER, stroke=INK, sw=3)
    # small cylinder (left, narrow) and large cylinder (right, wide)
    body += _rect(120, 150, 70, 120, fill=WATER, stroke=INK, sw=3)
    body += _rect(430, 120, 150, 150, fill=WATER, stroke=INK, sw=3)
    # small piston A + force F1
    body += _rect(122, 150, 66, 20, fill=STEEL, stroke=INK, sw=2)
    body += _line(155, 96, 155, 146, col=RED, w=5, marker="arrowR")
    body += _txt(155, 86, "F₁ (small)", col=RED, size=14)
    body += _txt(155, 300, "A₁ (small area)", col=INK, size=13)
    body += _txt(155, 210, "A", col=INK, size=15)
    # large piston B + force F2
    body += _rect(432, 120, 146, 20, fill=STEEL, stroke=INK, sw=2)
    body += _line(505, 116, 505, 66, col=TEAL, w=8, marker="arrowT")
    body += _txt(505, 54, "F₂ (large)", col=TEAL, size=14)
    body += _txt(505, 300, "A₂ (large area)", col=INK, size=13)
    body += _txt(505, 190, "B", col=INK, size=15)
    # formula
    body += _rect(250, 335, 200, 44, fill="#FBEEE9", stroke=RED, sw=2, rx=8)
    body += _txt(vw / 2, 362, "F₂ / F₁  =  A₂ / A₁", col=RED, size=18)
    return _render(key, _svg(body, vw, vh), vw, vh)


# ---------------------------------------------------------------------------
# Fig 4.7 — Hydraulic (Bramah) press
# ---------------------------------------------------------------------------
def fig_4_7(key):
    vw, vh = 720, 460
    body = _txt(vw / 2, 30, "Hydraulic (Bramah) press", col=INK, size=18)
    # fixed top plate + bale of cotton on large ram (left)
    body += _rect(70, 70, 190, 16, fill="#5A6270", stroke=INK, sw=2)
    body += _txt(165, 64, "FIXED PLATE", col=MUT, size=11)
    body += _rect(110, 92, 110, 60, fill="#EAD9B0", stroke=INK, sw=2)
    body += _txt(165, 126, "bale of cotton", col=INK, size=12)
    # large cylinder Q + ram B
    body += _rect(105, 200, 120, 150, fill=WATER, stroke=INK, sw=3)
    body += _rect(107, 160, 116, 42, fill=STEEL, stroke=INK, sw=2)
    body += _line(165, 158, 165, 200, col=INK, w=2)
    body += _txt(165, 258, "ram B", col=INK, size=13)
    body += _txt(150, 396, "cylinder Q", col=MUT, size=12)
    # small cylinder P + pump plunger A with lever
    body += _rect(470, 210, 60, 130, fill=WATER, stroke=INK, sw=3)
    body += _rect(472, 190, 56, 22, fill=STEEL, stroke=INK, sw=2)
    body += _line(500, 190, 640, 150, col="#5A6270", w=8)   # lever
    body += _circle(500, 190, 5, fill=INK, stroke="none")
    body += _txt(560, 140, "lever / handle", col=INK, size=12, anchor="start")
    body += _txt(500, 262, "plunger A", col="#0B3A52", size=11)
    body += _txt(500, 396, "cylinder P", col=MUT, size=12)
    # connecting pipe R with valves
    body += _rect(165, 350, 335, 22, fill=WATER, stroke=INK, sw=3)
    body += _circle(360, 361, 8, fill="#EAD9B0", stroke=INK, sw=2)
    body += _txt(360, 392, "valve", col=MUT, size=11)
    # reservoir
    body += _rect(560, 300, 120, 70, fill=WATER, stroke=INK, sw=2)
    body += _txt(620, 340, "reservoir", col="#0B3A52", size=12)
    body += _line(560, 361, 530, 361, col=INK, w=3)
    body += _txt(330, 340, "pipe R", col=INK, size=12)
    return _render(key, _svg(body, vw, vh), vw, vh)


# ---------------------------------------------------------------------------
# Fig 4.8 — Hydraulic jack lifting a car
# ---------------------------------------------------------------------------
def fig_4_8(key):
    vw, vh = 720, 440
    body = _txt(vw / 2, 30, "Hydraulic jack (car lift)", col=INK, size=18)
    # platform + car on the large piston (left)
    body += _rect(70, 150, 200, 16, fill="#5A6270", stroke=INK, sw=2)
    # simple car
    body += _rect(95, 108, 150, 42, fill=RED, stroke=INK, sw=2, rx=8)
    body += _poly([(120, 108), (140, 84), (200, 84), (215, 108)],
                  fill="#E88", stroke=INK, sw=2)
    body += _circle(130, 152, 14, fill=INK, stroke="none")
    body += _circle(210, 152, 14, fill=INK, stroke="none")
    body += _txt(170, 100, "CAR", col=INK, size=12)
    body += _txt(170, 182, "PLATFORM", col=MUT, size=11)
    # large cylinder Q + piston B
    body += _rect(120, 210, 100, 150, fill=WATER, stroke=INK, sw=3)
    body += _rect(122, 166, 96, 44, fill=STEEL, stroke=INK, sw=2)
    body += _line(170, 190, 170, 174, col=TEAL, w=5, marker="arrowT")
    body += _txt(170, 262, "piston B", col=INK, size=13)
    body += _txt(150, 404, "cylinder Q", col=MUT, size=12)
    # small cylinder P + piston A + lever handle
    body += _rect(470, 250, 54, 110, fill=WATER, stroke=INK, sw=3)
    body += _rect(472, 232, 50, 20, fill=STEEL, stroke=INK, sw=2)
    body += _line(497, 232, 630, 202, col="#5A6270", w=8)
    body += _circle(455, 224, 5, fill=INK, stroke="none")     # fulcrum
    body += _txt(455, 210, "fulcrum", col=MUT, size=11)
    body += _line(612, 210, 612, 246, col=RED, w=4, marker="arrowR")
    body += _txt(612, 198, "effort (handle H)", col=INK, size=12)
    body += _txt(497, 400, "piston A / cylinder P", col=MUT, size=11)
    # connecting tube R with valve V
    body += _rect(170, 360, 330, 22, fill=WATER, stroke=INK, sw=3)
    body += _circle(360, 371, 8, fill="#EAD9B0", stroke=INK, sw=2)
    body += _txt(360, 402, "valve V", col=MUT, size=11)
    body += _txt(300, 350, "tube R (liquid)", col=INK, size=12)
    return _render(key, _svg(body, vw, vh), vw, vh)


# ---------------------------------------------------------------------------
# Fig 4.9 — Hydraulic brake (one wheel)
# ---------------------------------------------------------------------------
def fig_4_9(key):
    vw, vh = 720, 420
    body = _txt(vw / 2, 30, "Hydraulic brake (one wheel)", col=INK, size=18)
    # foot pedal + master cylinder P (right)
    body += _line(600, 90, 660, 130, col="#5A6270", w=8)     # pedal arm
    body += _circle(600, 90, 6, fill=INK, stroke="none")
    body += _txt(662, 120, "foot pedal", col=INK, size=12, anchor="start")
    body += _rect(470, 150, 150, 40, fill=WATER, stroke=INK, sw=3)
    body += _rect(560, 152, 40, 36, fill=STEEL, stroke=INK, sw=2)   # piston A
    body += _line(560, 150, 590, 128, col=INK, w=3)
    body += _txt(545, 210, "master cylinder P (piston A)", col=MUT, size=11)
    # pipe line R
    body += _rect(250, 168, 220, 20, fill=WATER, stroke=INK, sw=3)
    body += _txt(360, 158, "pipe line R (fluid)", col=INK, size=12)
    # wheel: rim (annulus) with brake shoes and wheel cylinder Q
    cx, cy, R = 160, 250, 110
    body += _circle(cx, cy, R, fill="none", stroke=INK, sw=8)     # rim
    body += _circle(cx, cy, R - 20, fill="none", stroke=MUT, sw=2)
    body += _txt(cx, cy + R + 26, "rim of wheel", col=MUT, size=12)
    # wheel cylinder Q at top-centre with two pistons B1,B2 pushing shoes out
    body += _rect(cx - 34, cy - 40, 68, 26, fill=WATER, stroke=INK, sw=2)
    body += _txt(cx, cy - 50, "wheel cylinder Q", col=INK, size=11)
    body += _line(cx - 20, cy - 27, cx - 70, cy - 27, col=RED, w=4,
                  marker="arrowR")
    body += _line(cx + 20, cy - 27, cx + 70, cy - 27, col=RED, w=4)
    # brake shoes (arcs) just inside rim
    body += _arc(cx, cy, R - 14, 100, 170, col="#C46", w=12)
    body += _arc(cx, cy, R - 14, 10, 80, col="#C46", w=12)
    body += _txt(cx, cy + 6, "B₁  B₂", col=INK, size=13)
    body += _txt(cx, cy + 34, "brake shoes", col="#C46", size=11)
    # spring
    body += _txt(cx, cy + 70, "return spring", col=MUT, size=11)
    # connect pipe to wheel cylinder
    body += _line(250, 178, cx, cy - 27, col=INK, w=2, dash="4 4")
    return _render(key, _svg(body, vw, vh), vw, vh)
