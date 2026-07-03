"""
Extra physics schematics for the Maharashtra board decks (Grades 6-10).

Same contract as diagrams.py: every diagram is authored as an SVG string,
rasterised to PNG with cairosvg into build/img/, and the PNG path is returned.
Reuses the shared SVG helpers/palette from diagrams.py so the visual style
matches the rest of the catalog. New file so diagrams.py / diagrams_extra.py
stay untouched.
"""
import os
import sys
import math

sys.path.insert(0, os.path.dirname(__file__))
from diagrams import (  # noqa: E402
    _svg, _line, _txt, _arc, _render, _esc,
    INK, MUT, TEAL, ORANGE, PURPLE, RED, BLUE, GLASS, WATER, GREEN, GOLD,
)

SKY = "#0B1E4B"
STARFIELD = "#111B33"
FLAME = "#F4801A"
SILVER = "#C9D2DA"


def _circle(cx, cy, r, fill="none", stroke=INK, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def _rect(x, y, w, h, fill="none", stroke=INK, sw=2, rx=0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def _poly(points, fill="none", stroke=INK, sw=2):
    pts = " ".join(f"{x},{y}" for x, y in points)
    return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def _ellipse(cx, cy, rx, ry, fill="none", stroke=INK, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


# ---------------------------------------------------------------------------
# Space Missions
# ---------------------------------------------------------------------------
def satellite_orbit(key):
    """Earth with a satellite in a circular orbit, orbital-velocity arrow."""
    vw, vh = 680, 480
    cx, cy = 300, 260
    earth_r, orbit_r = 80, 165
    body = _ellipse(cx, cy, earth_r, earth_r, fill=BLUE, stroke=INK, sw=2)
    body += _circle(cx, cy, orbit_r, stroke=MUT, sw=2, dash="6,6")
    ang = -20
    sx = cx + orbit_r * math.cos(math.radians(ang))
    sy = cy + orbit_r * math.sin(math.radians(ang))
    body += _rect(sx - 16, sy - 10, 32, 20, fill=SILVER, stroke=INK, sw=2, rx=3)
    body += _line(sx - 16, sy, sx - 34, sy, col=GOLD, w=6)
    body += _line(sx + 16, sy, sx + 34, sy, col=GOLD, w=6)
    tx = sx + orbit_r * 0.32 * math.cos(math.radians(ang + 90))
    ty = sy + orbit_r * 0.32 * math.sin(math.radians(ang + 90))
    body += _line(sx, sy, tx, ty, col=RED, w=3, marker="arrowR")
    body += _txt(tx + 10, ty - 6, "v (orbital", col=RED, size=15,
                anchor="start", bold=False)
    body += _txt(tx + 10, ty + 14, "velocity)", col=RED, size=15,
                anchor="start", bold=False)
    body += _txt(cx, cy + 6, "Earth", col="#FFFFFF", size=18)
    body += _txt(sx, sy - 26, "Satellite", col=INK, size=16, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#EAF1FF"), vw, vh)


def launch_vehicle_stages(key):
    """Multi-stage rocket: payload+nose cone at top, Stage 3 (smallest, fires
    last) below it, down to Stage 1 (largest, fires first) at the base —
    matches the real firing/size order of a launch vehicle."""
    vw, vh = 460, 660
    x = vw / 2
    body = ""
    # (stage label, height, colour) from TOP to BOTTOM
    stages = [("Stage 3", 90, PURPLE), ("Stage 2", 120, TEAL),
             ("Stage 1", 160, ORANGE)]
    nose_y = 70
    body += _poly([(x - 50, nose_y), (x + 50, nose_y), (x, nose_y - 65)],
                 fill="#D9E4F5", stroke=INK, sw=3)
    body += _txt(x, nose_y - 30, "Payload", col=INK, size=15)
    y = nose_y
    for i, (label, h, col) in enumerate(stages):
        body += _rect(x - 55, y, 110, h, fill="#FFFFFF", stroke=col, sw=4, rx=6)
        body += _txt(x, y + h / 2 + 6, label, col=col, size=19)
        y += h
        if i < len(stages) - 1:
            body += _line(x - 70, y + 13, x + 70, y + 13, col=MUT, w=2,
                          dash="5,5")
        y += 26
    flame_y = y - 16
    body += _poly([(x - 30, flame_y), (x + 30, flame_y), (x, flame_y + 55)],
                 fill=FLAME, stroke="none")
    body += _txt(x, vh - 16, "Multi-stage launch vehicle", col=INK, size=17)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def right_hand_thumb_rule(key):
    """Straight current-carrying wire with the circular magnetic field and
    the right-hand-thumb-rule convention (thumb = current, curl = field).
    Field direction is shown correctly: dot = out of the page, cross = into
    the page, on opposite sides of a field loop viewed edge-on."""
    vw, vh = 600, 460
    cx, cy = 300, 240
    body = _txt(cx, 36, "Right-Hand Thumb Rule", col=INK, size=19)
    body += _line(cx, 70, cx, vh - 50, col=INK, w=6, marker="arrow")
    body += _txt(cx + 22, 88, "I (current)", col=INK, size=16, anchor="start",
                bold=False)
    for r in (50, 85, 120):
        body += _ellipse(cx, cy, r, r * 0.34, stroke=TEAL, sw=2.5)
    # field emerges (dot) on the left, goes in (cross) on the right of the loop
    body += _circle(cx - 120, cy, 9, fill="#FFFFFF", stroke=RED, sw=2)
    body += _circle(cx - 120, cy, 2.6, fill=RED)
    body += _txt(cx - 120, cy + 26, "out of page", col=RED, size=12,
                bold=False)
    body += _circle(cx + 120, cy, 9, fill="#FFFFFF", stroke=RED, sw=2)
    body += _line(cx + 114, cy - 6, cx + 126, cy + 6, col=RED, w=2)
    body += _line(cx + 114, cy + 6, cx + 126, cy - 6, col=RED, w=2)
    body += _txt(cx + 120, cy + 26, "into page", col=RED, size=12, bold=False)
    body += _txt(cx, vh - 16, "Field lines circle the wire; thumb points "
                "along the current, curled fingers show the field",
                col=MUT, size=13, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def flemings_rule(key, left=True):
    """Fleming's Left-Hand (motor) or Right-Hand (generator/dynamo) rule —
    three mutually perpendicular fingers labelled F, B, I."""
    vw, vh = 560, 500
    ox, oy = 240, 330
    body = _line(ox, oy, ox + 170, oy, col=BLUE, w=6, marker="arrow")
    body += _txt(ox + 190, oy + 6, "B (field)", col=BLUE, size=16, anchor="start")
    body += _line(ox, oy, ox, oy - 190, col=RED, w=6, marker="arrowR")
    label_top = "F (thrust)" if left else "I (induced current)"
    body += _txt(ox, oy - 208, label_top, col=RED, size=16)
    body += _line(ox, oy, ox - 130, oy + 110, col=GREEN, w=6, marker="arrowT")
    label_diag = "I (current)" if left else "F (motion)"
    body += _txt(ox - 130, oy + 138, label_diag, col=GREEN, size=16)
    title = ("Fleming's Left-Hand Rule (motor effect)" if left else
             "Fleming's Right-Hand Rule (generator effect)")
    body += _txt(vw / 2, 40, title, col=INK, size=18)
    body += _txt(vw / 2, vh - 16,
                "Thumb - First finger - Second finger, mutually perpendicular",
                col=MUT, size=13, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


# ---------------------------------------------------------------------------
# Telescopes (Std 9 — Observing Space)
# ---------------------------------------------------------------------------
def refracting_telescope(key):
    """Two-lens refracting telescope: large objective lens + eyepiece."""
    vw, vh = 640, 380
    axis_y = 190
    body = _line(70, axis_y, 590, axis_y, col=MUT, w=2, dash="5,5")
    # incoming parallel rays from the left
    for dy in (-45, 0, 45):
        body += _line(70, axis_y + dy, 150, axis_y + dy, col=RED, w=2)
    # objective lens (large convex)
    body += _ellipse(160, axis_y, 14, 70, fill=GLASS, stroke=INK, sw=2)
    body += _txt(160, axis_y + 92, "Objective lens", col=INK, size=14)
    body += _txt(160, axis_y + 110, "(large, gathers light)", col=MUT,
                size=12, bold=False)
    # converging rays to intermediate focus then to eyepiece
    for dy in (-45, 0, 45):
        body += _line(174, axis_y + dy, 430, axis_y, col=RED, w=2)
    body += _line(430, axis_y, 470, axis_y - 20, col=RED, w=2)
    body += _line(430, axis_y, 470, axis_y + 20, col=RED, w=2)
    # eyepiece (small convex)
    body += _ellipse(480, axis_y, 10, 42, fill=GLASS, stroke=INK, sw=2)
    body += _txt(500, axis_y + 70, "Eyepiece", col=INK, size=14,
                anchor="start")
    body += _txt(560, axis_y - 55, "eye", col=INK, size=13)
    body += _line(560, axis_y - 40, 560, axis_y - 10, col=INK, w=2)
    body += _txt(vw / 2, 34, "Refracting telescope (lenses)", col=INK,
                size=17)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def reflecting_telescope(key):
    """Newtonian reflecting telescope: concave primary + plane secondary."""
    vw, vh = 620, 400
    body = _txt(vw / 2, 34, "Reflecting telescope (Newtonian)", col=INK,
                size=17)
    # tube
    body += _rect(120, 120, 380, 150, stroke=MUT, sw=2, rx=8)
    # concave primary mirror at the right end
    body += _line(495, 130, 495, 260, col=TEAL, w=8)
    body += _txt(500, 300, "Concave primary mirror", col=INK, size=13,
                anchor="end")
    # incoming parallel rays entering from the left
    for dy in (150, 195, 240):
        body += _line(130, dy, 480, dy, col=RED, w=2)
    # reflected rays converging to the secondary (plane) mirror near the top
    for dy in (150, 195, 240):
        body += _line(480, dy, 300, 150, col=RED, w=2)
    # plane secondary mirror at 45 deg
    body += _line(285, 135, 315, 165, col=PURPLE, w=6)
    body += _txt(300, 120, "Plane secondary", col=PURPLE, size=12)
    # up to eyepiece
    body += _line(300, 150, 300, 90, col=RED, w=2)
    body += _ellipse(300, 80, 26, 9, fill=GLASS, stroke=INK, sw=2)
    body += _txt(300, 62, "Eyepiece", col=INK, size=13)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def radio_telescope(key):
    """Parabolic radio dish reflecting radio waves to a feed at the focus."""
    vw, vh = 560, 420
    cx = 300
    # parabolic dish (arc)
    body = f'<path d="M 150 120 Q {cx} 380 450 120" fill="#E9EEF5" stroke="{INK}" stroke-width="3"/>'
    # incoming parallel radio waves from the top
    for x in (210, 300, 390):
        body += _line(x, 60, x, 150 + (0 if x == 300 else 25), col=BLUE, w=2,
                      dash="6,5")
    # converge to focus (feed)
    fx, fy = cx, 210
    for x in (210, 390):
        body += _line(x, 175, fx, fy, col=BLUE, w=2)
    body += _line(300, 150, fx, fy, col=BLUE, w=2)
    body += _ellipse(fx, fy, 12, 12, fill=GOLD, stroke=INK, sw=2)
    body += _txt(fx + 20, fy, "Receiver / feed", col=INK, size=13,
                anchor="start")
    # support mast
    body += _line(cx, 250, cx, 360, col=MUT, w=5)
    body += _txt(vw / 2, 34, "Radio telescope (parabolic dish)", col=INK,
                size=17)
    body += _txt(vw / 2, 400, "Dish reflects radio waves to the focus",
                col=MUT, size=12, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


# ---------------------------------------------------------------------------
# Reflection (Std 8) — periscope
# ---------------------------------------------------------------------------
def periscope(key):
    """Two plane mirrors at 45 deg in a tube; light in at top, out at bottom."""
    vw, vh = 420, 520
    body = _rect(150, 40, 120, 440, stroke=INK, sw=3, rx=8)
    # top mirror (45 deg)
    body += _line(165, 95, 255, 125, col=TEAL, w=6)
    body += _txt(300, 100, "mirror 1", col=TEAL, size=13, anchor="start")
    # bottom mirror (45 deg, opposite tilt)
    body += _line(165, 425, 255, 395, col=TEAL, w=6)
    body += _txt(300, 430, "mirror 2", col=TEAL, size=13, anchor="start")
    # incoming ray from object (left, into top window)
    body += _line(60, 110, 205, 110, col=RED, w=3, marker="arrowR")
    body += _txt(60, 95, "from object", col=RED, size=12, anchor="start",
                bold=False)
    # down the tube
    body += _line(210, 118, 210, 405, col=RED, w=3)
    # out to the eye (left, bottom)
    body += _line(205, 410, 60, 410, col=RED, w=3, marker="arrowR")
    body += _txt(60, 445, "to eye", col=RED, size=12, anchor="start",
                bold=False)
    body += _txt(vw / 2, 26, "Periscope (two 45 deg mirrors)", col=INK,
                size=15)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


# ---------------------------------------------------------------------------
# Life Cycle of Stars (Std 8)
# ---------------------------------------------------------------------------
def star_life_cycle(key):
    """Flow: nebula -> star -> (low mass) red giant -> white dwarf;
    (high mass) supergiant -> supernova -> neutron star / black hole."""
    vw, vh = 720, 460

    def node(cx, cy, label, col, r=34):
        s = _ellipse(cx, cy, r, r, fill=col, stroke=INK, sw=2)
        return s

    body = ""
    # nebula
    body += node(80, 230, "", MUT, 30)
    body += _txt(80, 285, "Nebula", col=INK, size=13)
    # star (main sequence)
    body += node(210, 230, "", GOLD, 26)
    body += _txt(210, 285, "Star", col=INK, size=13)
    body += _line(112, 230, 182, 230, col=INK, w=2, marker="arrow")
    # branch up: low mass
    body += _line(236, 215, 320, 130, col=INK, w=2, marker="arrow")
    body += node(360, 120, "", RED, 32)
    body += _txt(360, 170, "Red giant", col=INK, size=13)
    body += _line(394, 120, 470, 120, col=INK, w=2, marker="arrow")
    body += node(510, 120, "", "#EAF1FF", 18)
    body += _txt(510, 165, "White dwarf", col=INK, size=13)
    body += _txt(300, 60, "Low-mass star", col=MUT, size=13, bold=False)
    # branch down: high mass
    body += _line(236, 245, 320, 330, col=INK, w=2, marker="arrow")
    body += node(370, 345, "", "#B23A48", 38)
    body += _txt(370, 400, "Supergiant", col=INK, size=13)
    body += _line(408, 345, 470, 345, col=INK, w=2, marker="arrow")
    body += _poly([(500, 320), (512, 340), (534, 342), (516, 356),
                   (522, 378), (500, 366), (478, 378), (484, 356),
                   (466, 342), (488, 340)], fill=ORANGE, stroke=INK, sw=1.5)
    body += _txt(500, 400, "Supernova", col=INK, size=13)
    body += _line(536, 345, 600, 320, col=INK, w=2, marker="arrow")
    body += node(636, 315, "", PURPLE, 14)
    body += _txt(636, 300, "Neutron star", col=INK, size=11)
    body += _line(536, 355, 600, 385, col=INK, w=2, marker="arrow")
    body += node(636, 390, "", INK, 16)
    body += _txt(636, 425, "Black hole", col=INK, size=11)
    body += _txt(360, 300, "High-mass star", col=MUT, size=13, bold=False)
    body += _txt(vw / 2, 28, "Life cycle of a star (depends on its mass)",
                col=INK, size=16)
    return _render(key, _svg(body, vw, vh, bg="#F4F8FF"), vw, vh)


# ===========================================================================
# Grade 7 — Heat, Stars
# ===========================================================================
def heat_transfer_modes(key):
    """Three ways heat travels: conduction, convection, radiation."""
    vw, vh = 780, 360
    body = _txt(vw / 2, 30, "Three ways heat travels", col=INK, size=17)
    # ---- Conduction (metal rod on flame) ----
    body += _rect(40, 150, 180, 20, fill=SILVER, stroke=INK, sw=2, rx=4)
    for i, x in enumerate((70, 110, 150, 190)):
        col = RED if i == 0 else (ORANGE if i == 1 else GOLD)
        body += _circle(x, 160, 6, fill=col, stroke="none")
    body += _poly([(60, 205), (52, 175), (68, 175)], fill=FLAME, stroke="none")
    body += _line(56, 205, 64, 205, col=INK, w=6)
    body += _txt(130, 245, "CONDUCTION", col=RED, size=14)
    body += _txt(130, 268, "through solids", col=MUT, size=12, bold=False)
    # ---- Convection (beaker of water, loop arrows) ----
    cx = 400
    body += _rect(cx - 70, 90, 140, 110, fill=WATER, stroke=INK, sw=2, rx=6)
    body += _poly([(cx, 210), (cx - 8, 226), (cx + 8, 226)],
                  fill=FLAME, stroke="none")
    # rising hot water (centre, red) and sinking cool water (sides, blue)
    body += _line(cx, 188, cx, 120, col=RED, w=3, marker="arrow")
    body += _line(cx + 48, 120, cx + 48, 188, col=BLUE, w=3, marker="arrow")
    body += _line(cx - 48, 120, cx - 48, 188, col=BLUE, w=3, marker="arrow")
    body += _txt(cx, 245, "CONVECTION", col=ORANGE, size=14)
    body += _txt(cx, 268, "in liquids and gases", col=MUT, size=12, bold=False)
    # ---- Radiation (sun rays to hand) ----
    sx = 640
    body += _circle(sx, 130, 26, fill=GOLD, stroke=ORANGE, sw=3)
    for ang in range(0, 360, 45):
        import math as _m
        dx, dy = _m.cos(_m.radians(ang)), _m.sin(_m.radians(ang))
        body += _line(sx + 30 * dx, 130 + 30 * dy,
                      sx + 46 * dx, 130 + 46 * dy, col=ORANGE, w=3)
    body += _line(sx - 20, 165, sx - 60, 205, col=RED, w=3, marker="arrow")
    body += _line(sx + 20, 165, sx + 60, 205, col=RED, w=3, marker="arrow")
    body += _txt(sx, 245, "RADIATION", col=RED, size=14)
    body += _txt(sx, 268, "no medium needed", col=MUT, size=12, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def thermometer(key):
    """Clinical thermometer: bulb, kink, mercury column and scale."""
    vw, vh = 360, 460
    tubx = vw / 2
    # stem
    body = _rect(tubx - 26, 60, 52, 330, fill="#EEF2F6", stroke=INK, sw=2,
                 rx=18)
    # bulb
    body += _circle(tubx, 405, 30, fill=RED, stroke=INK, sw=2)
    # mercury thread up to ~ mid
    body += _rect(tubx - 6, 210, 12, 200, fill=RED, stroke="none")
    body += _circle(tubx, 405, 22, fill=RED, stroke="none")
    # kink (constriction)
    body += _circle(tubx, 360, 9, fill="none", stroke=INK, sw=2)
    body += _line(tubx + 40, 360, tubx + 14, 360, col=INK, w=2, marker="arrow")
    body += _txt(tubx + 46, 364, "kink", col=INK, size=13, anchor="start")
    # scale marks
    for i, y in enumerate(range(110, 340, 30)):
        body += _line(tubx + 26, y, tubx + 38, y, col=INK, w=2)
    body += _txt(tubx + 60, 120, "42°C", col=MUT, size=13, anchor="start")
    body += _txt(tubx + 60, 330, "35°C", col=MUT, size=13, anchor="start")
    body += _txt(tubx, 40, "Clinical thermometer", col=INK, size=16)
    body += _txt(tubx, 450, "bulb", col=MUT, size=13)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def thermos_flask(key):
    """Cross-section of a vacuum (Dewar) flask - stops all three transfers."""
    vw, vh = 420, 460
    cx = vw / 2
    # outer wall
    body = _rect(cx - 120, 60, 240, 360, fill="#DDE3EA", stroke=INK, sw=3,
                 rx=20)
    # vacuum gap
    body += _rect(cx - 98, 82, 196, 316, fill="#FFFFFF", stroke=INK, sw=2,
                  rx=16)
    # silvered inner wall + hot liquid
    body += _rect(cx - 78, 100, 156, 280, fill=WATER, stroke=SILVER, sw=6,
                  rx=12)
    body += _txt(cx, 250, "hot", col="#FFFFFF", size=18)
    body += _txt(cx, 275, "liquid", col="#FFFFFF", size=18)
    # labels
    body += _line(cx - 150, 120, cx - 100, 130, col=INK, w=2, marker="arrow")
    body += _txt(cx - 156, 116, "vacuum", col=INK, size=13, anchor="end")
    body += _txt(cx - 156, 134, "(no conduction/", col=MUT, size=11,
                 anchor="end", bold=False)
    body += _txt(cx - 156, 150, "convection)", col=MUT, size=11,
                 anchor="end", bold=False)
    body += _line(cx + 150, 200, cx + 82, 210, col=INK, w=2, marker="arrow")
    body += _txt(cx + 156, 196, "silvered walls", col=INK, size=13,
                 anchor="start")
    body += _txt(cx + 156, 214, "(no radiation)", col=MUT, size=11,
                 anchor="start", bold=False)
    body += _txt(cx, 40, "Vacuum (Thermos) flask", col=INK, size=16)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def constellation(key):
    """The Great Bear (Saptarshi) - a recognisable star pattern."""
    vw, vh = 620, 400
    body = _rect(0, 0, vw, vh, fill=SKY, stroke="none")
    # scattered faint background stars
    import random as _r
    _r.seed(7)
    for _ in range(60):
        x, y = _r.randint(20, vw - 20), _r.randint(50, vh - 20)
        body += _circle(x, y, _r.choice([1, 1, 2]), fill="#7C8AA5",
                        stroke="none")
    # seven bright stars of the Big Dipper (schematic layout)
    pts = [(120, 300), (200, 285), (275, 300), (330, 250),
           (400, 210), (470, 235), (430, 300)]
    for x, y in pts:
        body += _circle(x, y, 8, fill="#FFF6CC", stroke=GOLD, sw=2)
    for i in range(len(pts) - 1):
        x1, y1 = pts[i]
        x2, y2 = pts[i + 1]
        body += _line(x1, y1, x2, y2, col="#FFE38A", w=2, dash="4 4")
    body += _txt(vw / 2, 40, "A constellation: the Great Bear (Saptarshi)",
                 col="#FFFFFF", size=16)
    body += _txt(120, 335, "a fixed pattern of bright stars", col="#C9D2DA",
                 size=13, anchor="start", bold=False)
    return _render(key, _svg(body, vw, vh, bg=SKY), vw, vh)


def galaxy_types(key):
    """Three shapes of galaxies: spiral, elliptical, irregular."""
    vw, vh = 720, 340
    body = _rect(0, 0, vw, vh, fill=SKY, stroke="none")
    import math as _m
    # spiral
    cx, cy = 150, 190
    for k in range(140):
        t = k / 12.0
        r = 6 + t * 9
        for arm in (0, _m.pi):
            a = t + arm
            body += _circle(cx + r * _m.cos(a), cy + r * _m.sin(a), 2,
                            fill="#BFE0FF", stroke="none")
    body += _circle(cx, cy, 10, fill="#FFF6CC", stroke="none")
    body += _txt(cx, 300, "Spiral", col="#FFFFFF", size=15)
    # elliptical
    ex, ey = 380, 190
    body += _ellipse(ex, ey, 78, 50, fill="#E7D9FF", stroke="none")
    body += _ellipse(ex, ey, 50, 32, fill="#CBB6FF", stroke="none")
    body += _ellipse(ex, ey, 24, 16, fill="#FFF6CC", stroke="none")
    body += _txt(ex, 300, "Elliptical", col="#FFFFFF", size=15)
    # irregular
    import random as _r
    _r.seed(3)
    ix, iy = 600, 185
    for _ in range(80):
        x = ix + _r.randint(-70, 70)
        y = iy + _r.randint(-45, 45)
        body += _circle(x, y, _r.choice([1, 2, 2]), fill="#BFE0FF",
                        stroke="none")
    body += _txt(ix, 300, "Irregular", col="#FFFFFF", size=15)
    body += _txt(vw / 2, 34, "Types of galaxies", col="#FFFFFF", size=17)
    return _render(key, _svg(body, vw, vh, bg=SKY), vw, vh)
