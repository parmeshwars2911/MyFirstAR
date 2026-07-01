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
