"""
Extra physics schematics for Grades 6, 7, 8 (built by the second agent).

Same contract as diagrams.py: every diagram is authored as an SVG string,
rasterised to PNG with cairosvg into build/img/, and the PNG path is returned.
Nothing is ever drawn directly on a slide. The low-level SVG helpers and the
colour palette are reused from diagrams.py so the visual style stays identical.

To avoid merge conflicts this file is *new* and never edits diagrams.py.
"""
import os
import sys
import math

sys.path.insert(0, os.path.dirname(__file__))
from diagrams import (  # noqa: E402  (reuse shared helpers)
    _svg, _line, _txt, _arc, _render, _esc,
    INK, MUT, TEAL, ORANGE, PURPLE, RED, BLUE, GLASS, WATER, GREEN, GOLD,
)

# Extra named colours used by these diagrams
IRON = "#9AA3AD"
COPPER = "#C77B3B"
BRASS = "#D9A441"
SKY = "#EAF6FF"
WOOD = "#D7B377"
FLAME = "#F4801A"


# ---------------------------------------------------------------------------
# small local shape helpers (kept here so diagrams.py is untouched)
# ---------------------------------------------------------------------------
def _circle(cx, cy, r, fill="none", stroke=INK, sw=2, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"{d}/>')


def _rect(x, y, w, h, fill="none", stroke=INK, sw=2, rx=0, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" '
            f'fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>')


def _poly(points, fill="none", stroke=INK, sw=2, dash=None):
    pts = " ".join(f"{x},{y}" for x, y in points)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    return (f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}/>')


def _polyline(points, stroke=INK, sw=2, dash=None, marker=None):
    pts = " ".join(f"{x},{y}" for x, y in points)
    d = f' stroke-dasharray="{dash}"' if dash else ""
    m = f' marker-end="url(#{marker})"' if marker else ""
    return (f'<polyline points="{pts}" fill="none" stroke="{stroke}" '
            f'stroke-width="{sw}"{d}{m}/>')


def _ellipse(cx, cy, rx, ry, fill="none", stroke=INK, sw=2):
    return (f'<ellipse cx="{cx}" cy="{cy}" rx="{rx}" ry="{ry}" fill="{fill}" '
            f'stroke="{stroke}" stroke-width="{sw}"/>')


# ===========================================================================
# SIMPLE MACHINES (Grade 6 — S30, S31)
# ===========================================================================
def lever(key, order=1):
    """Three classes of lever: fulcrum (F), load (L) and effort (E) positions.

    order 1: E ---- F ---- L   (fulcrum between effort and load)
    order 2: F -- L --- E      (load between fulcrum and effort)
    order 3: F -- E --- L      (effort between fulcrum and load)
    """
    vw, vh = 620, 440
    beam_y = 210
    body = []
    if order == 1:
        fx = 310
        body += [
            _rect(90, beam_y, 440, 16, fill="#C7CDD6", stroke=INK, sw=2, rx=4),
            _poly([(fx - 34, beam_y + 70), (fx + 34, beam_y + 70),
                   (fx, beam_y + 16)], fill=PURPLE, stroke=INK, sw=2),
            _line(150, beam_y, 150, beam_y + 130, ORANGE, 6, marker="arrowO"),
            _line(470, beam_y, 470, beam_y + 130, TEAL, 6, marker="arrowT"),
            _txt(150, beam_y + 160, "Load (L)", ORANGE, 20),
            _txt(470, beam_y + 160, "Effort (E)", TEAL, 20),
            _txt(fx, beam_y + 105, "Fulcrum (F)", PURPLE, 20),
            _txt(vw / 2, 60, "Class 1: Fulcrum between load and effort", INK, 22),
            _txt(vw / 2, 92, "e.g. seesaw, scissors, a pair of pliers",
                 MUT, 17),
        ]
    elif order == 2:
        fx = 120
        body += [
            _rect(fx, beam_y, 420, 16, fill="#C7CDD6", stroke=INK, sw=2, rx=4),
            _poly([(fx - 28, beam_y + 70), (fx + 28, beam_y + 70),
                   (fx, beam_y + 16)], fill=PURPLE, stroke=INK, sw=2),
            _line(300, beam_y, 300, beam_y + 130, ORANGE, 6, marker="arrowO"),
            _line(500, beam_y + 16, 500, beam_y - 120, TEAL, 6, marker="arrowT"),
            _txt(300, beam_y + 160, "Load (L)", ORANGE, 20),
            _txt(500, beam_y - 140, "Effort (E)", TEAL, 20),
            _txt(fx, beam_y + 100, "Fulcrum (F)", PURPLE, 20),
            _txt(vw / 2, 60, "Class 2: Load between fulcrum and effort", INK, 22),
            _txt(vw / 2, 92, "e.g. wheelbarrow, nutcracker, bottle opener",
                 MUT, 17),
        ]
    else:
        fx = 120
        body += [
            _rect(fx, beam_y, 420, 16, fill="#C7CDD6", stroke=INK, sw=2, rx=4),
            _poly([(fx - 28, beam_y + 70), (fx + 28, beam_y + 70),
                   (fx, beam_y + 16)], fill=PURPLE, stroke=INK, sw=2),
            _line(300, beam_y + 16, 300, beam_y - 120, TEAL, 6, marker="arrowT"),
            _line(500, beam_y, 500, beam_y + 130, ORANGE, 6, marker="arrowO"),
            _txt(300, beam_y - 140, "Effort (E)", TEAL, 20),
            _txt(500, beam_y + 160, "Load (L)", ORANGE, 20),
            _txt(fx, beam_y + 100, "Fulcrum (F)", PURPLE, 20),
            _txt(vw / 2, 60, "Class 3: Effort between fulcrum and load", INK, 22),
            _txt(vw / 2, 92, "e.g. forearm, tongs, a fishing rod", MUT, 17),
        ]
    return _render(key, _svg("".join(body), vw, vh), 800, 568)


def lever_principle(key):
    """The principle of a lever: load x load-arm = effort x effort-arm."""
    vw, vh = 620, 420
    beam_y = 200
    fx = 310
    body = [
        _rect(70, beam_y, 480, 14, fill="#C7CDD6", stroke=INK, sw=2, rx=4),
        _poly([(fx - 32, beam_y + 64), (fx + 32, beam_y + 64),
               (fx, beam_y + 14)], fill=PURPLE, stroke=INK, sw=2),
        # load arm + effort arm braces
        _line(120, beam_y - 70, fx, beam_y - 70, MUT, 2),
        _line(120, beam_y - 78, 120, beam_y - 62, MUT, 2),
        _line(fx, beam_y - 78, fx, beam_y - 62, MUT, 2),
        _txt((120 + fx) / 2, beam_y - 82, "load arm", MUT, 16),
        _line(fx, beam_y - 70, 500, beam_y - 70, MUT, 2),
        _line(500, beam_y - 78, 500, beam_y - 62, MUT, 2),
        _txt((fx + 500) / 2, beam_y - 82, "effort arm", MUT, 16),
        _line(120, beam_y, 120, beam_y + 120, ORANGE, 6, marker="arrowO"),
        _line(500, beam_y, 500, beam_y + 120, TEAL, 6, marker="arrowT"),
        _txt(120, beam_y + 148, "Load", ORANGE, 19),
        _txt(500, beam_y + 148, "Effort", TEAL, 19),
        _txt(fx, beam_y + 96, "F", PURPLE, 20),
        _txt(vw / 2, 56, "Load x load-arm  =  Effort x effort-arm", INK, 22),
        _txt(vw / 2, 360, "Mechanical advantage  MA = load / effort = "
                          "effort-arm / load-arm", MUT, 17),
    ]
    return _render(key, _svg("".join(body), vw, vh), 800, 542)


def pulley(key, fixed=True):
    """Single fixed or single movable pulley."""
    vw, vh = 520, 480
    cx = 260
    if fixed:
        cy = 150
        body = [
            _rect(120, 60, 280, 18, fill="#9AA3AD", stroke=INK, sw=2),  # support
            _line(cx, 78, cx, 108, INK, 4),                              # hook
            _circle(cx, cy, 48, fill="#E6E9EE", stroke=INK, sw=3),
            _circle(cx, cy, 7, fill=INK),
            # rope: load side (left) and effort side (right)
            _line(cx - 48, cy, cx - 48, 380, ORANGE, 4),
            _line(cx + 48, cy, cx + 48, 360, TEAL, 4),
            _rect(cx - 84, 380, 72, 56, fill=ORANGE, stroke=INK, sw=2, rx=4),
            _txt(cx - 48, 412, "Load", "#FFFFFF", 18),
            _line(cx + 48, 330, cx + 48, 400, TEAL, 6, marker="arrowT"),
            _txt(cx + 48, 430, "Effort", TEAL, 19),
            _txt(vw / 2, 36, "Single fixed pulley", INK, 21),
            _txt(vw / 2, 466, "MA = 1  -  only changes the direction of the "
                              "force", MUT, 16),
        ]
    else:
        cy = 300
        body = [
            _rect(120, 60, 280, 18, fill="#9AA3AD", stroke=INK, sw=2),
            # left rope fixed to support, down to left tangent
            _line(cx - 48, 78, cx - 48, cy, RED, 4),
            _circle(cx - 48, 84, 5, fill=RED),
            _circle(cx, cy, 48, fill="#E6E9EE", stroke=INK, sw=3),
            _circle(cx, cy, 7, fill=INK),
            # right rope up to effort
            _line(cx + 48, cy, cx + 48, 96, TEAL, 4),
            _line(cx + 48, 170, cx + 48, 100, TEAL, 6, marker="arrowT"),
            _txt(cx + 120, 120, "Effort", TEAL, 19),
            # load hangs from pulley axle
            _line(cx, cy + 48, cx, 392, ORANGE, 4),
            _rect(cx - 36, 392, 72, 56, fill=ORANGE, stroke=INK, sw=2, rx=4),
            _txt(cx, 424, "Load", "#FFFFFF", 18),
            _txt(vw / 2, 36, "Single movable pulley", INK, 21),
            _txt(vw / 2, 470, "MA = 2  -  effort needed is half the load",
                 MUT, 16),
        ]
    return _render(key, _svg("".join(body), vw, vh), 620, 572)


def block_and_tackle(key):
    """A simple block and tackle: one fixed + one movable pulley (MA = 2)."""
    vw, vh = 540, 520
    fx, fy = 300, 150            # fixed pulley (top)
    mx, my = 240, 340            # movable pulley (carries the load)
    rr = 42
    body = [
        _rect(120, 70, 300, 16, fill="#9AA3AD", stroke=INK, sw=2),
        # fixed pulley
        _circle(fx, fy, rr, fill="#E6E9EE", stroke=INK, sw=3),
        _circle(fx, fy, 6, fill=INK),
        _line(fx, 86, fx, fy - rr, INK, 4),
        # movable pulley
        _circle(mx, my, rr, fill="#E6E9EE", stroke=INK, sw=3),
        _circle(mx, my, 6, fill=INK),
        # rope segment 1: anchored to beam -> down to left of movable pulley
        _circle(mx - rr, 90, 5, fill=RED),
        _line(mx - rr, 90, mx - rr, my, RED, 3.5),
        # rope segment 2: up from right of movable -> over fixed -> down to effort
        _line(mx + rr, my, fx - rr, fy, TEAL, 3.5),
        _line(fx + rr, fy, fx + rr, 420, TEAL, 3.5),
        _line(fx + rr, 360, fx + rr, 430, TEAL, 6, marker="arrowT"),
        _txt(fx + rr, 458, "Effort", TEAL, 19),
        # load hangs from the movable pulley
        _line(mx, my + rr, mx, 422, ORANGE, 4),
        _rect(mx - 36, 422, 72, 54, fill=ORANGE, stroke=INK, sw=2, rx=4),
        _txt(mx, 453, "Load", "#FFFFFF", 18),
        _txt(vw / 2, 40, "Block and tackle (two pulleys)", INK, 21),
        _txt(vw / 2, 504, "Two rope segments support the load  ->  MA = 2",
             MUT, 16),
    ]
    return _render(key, _svg("".join(body), vw, vh), 600, 578)


def inclined_plane(key):
    """A load pushed up a ramp; MA = length / height."""
    vw, vh = 620, 420
    ax, ay = 90, 350      # bottom-left of base
    bx, by = 520, 350     # bottom-right
    tx, ty = 520, 170     # top (right angle at bottom-right)
    body = [
        _poly([(ax, ay), (bx, by), (tx, ty)], fill=GLASS, stroke=INK, sw=3),
        # height marker (right vertical)
        _line(548, ty, 548, by, MUT, 2),
        _line(540, ty, 556, ty, MUT, 2),
        _line(540, by, 556, by, MUT, 2),
        _txt(572, (ty + by) / 2, "h", INK, 22, italic=True),
        # load box sitting on the slope (mid)
        _rect(250, 232, 60, 46, fill=ORANGE, stroke=INK, sw=2, rx=4),
        _txt(280, 260, "load", "#FFFFFF", 15),
        # effort arrow up the slope
        _line(250, 300, 360, 254, TEAL, 6, marker="arrowT"),
        _txt(300, 322, "Effort", TEAL, 19),
        _txt(300, 372, "length of incline  l", MUT, 17),
        _txt(vw / 2, 56, "Inclined plane (ramp)", INK, 21),
        _txt(vw / 2, 92, "MA = length / height = l / h", MUT, 17),
    ]
    return _render(key, _svg("".join(body), vw, vh), 800, 542)


def wheel_and_axle(key):
    """Effort on the large wheel, load on the small axle; MA = R / r."""
    vw, vh = 560, 480
    cx, cy = 280, 210
    R, r = 120, 44
    body = [
        _rect(120, 70, 320, 14, fill="#9AA3AD", stroke=INK, sw=2),  # support
        _line(cx, 84, cx, cy - R, INK, 3),
        _circle(cx, cy, R, fill="#E6E9EE", stroke=INK, sw=3),
        _circle(cx, cy, r, fill="#CBD2DB", stroke=INK, sw=3),
        _circle(cx, cy, 6, fill=INK),
        # radius lines
        _line(cx, cy, cx + R, cy, MUT, 2, dash="5 5"),
        _line(cx, cy, cx - r, cy, MUT, 2, dash="5 5"),
        _txt(cx + 64, cy - 10, "R", INK, 20, italic=True),
        _txt(cx - 26, cy - 10, "r", INK, 18, italic=True),
        # effort rope on wheel (right), load rope on axle (left)
        _line(cx + R, cy, cx + R, 360, TEAL, 4),
        _line(cx + R, 320, cx + R, 392, TEAL, 6, marker="arrowT"),
        _txt(cx + R, 420, "Effort", TEAL, 19),
        _line(cx - r, cy, cx - r, 372, ORANGE, 4),
        _rect(cx - r - 34, 372, 68, 50, fill=ORANGE, stroke=INK, sw=2, rx=4),
        _txt(cx - r, 402, "Load", "#FFFFFF", 16),
        _txt(vw / 2, 36, "Wheel and axle", INK, 21),
        _txt(vw / 2, 466, "MA = radius of wheel / radius of axle = R / r",
             MUT, 16),
    ]
    return _render(key, _svg("".join(body), vw, vh), 660, 566)


def wedge(key):
    """A wedge driven into a log splits it; two inclined planes back to back."""
    vw, vh = 560, 440
    body = [
        # the wood, already split by the wedge
        _poly([(120, 250), (255, 250), (255, 400), (120, 400)], fill=WOOD,
              stroke=INK, sw=2),
        _poly([(305, 250), (440, 250), (440, 400), (305, 400)], fill=WOOD,
              stroke=INK, sw=2),
        # the wedge (triangle, apex down)
        _poly([(258, 150), (302, 150), (280, 330)], fill=IRON, stroke=INK,
              sw=3),
        # effort down on top of wedge
        _line(280, 90, 280, 150, TEAL, 6, marker="arrowT"),
        _txt(280, 74, "Effort", TEAL, 19),
        # split forces sideways
        _line(255, 300, 190, 300, ORANGE, 5, marker="arrowO"),
        _line(305, 300, 372, 300, ORANGE, 5, marker="arrowO"),
        _txt(150, 290, "split", ORANGE, 15),
        _txt(410, 290, "split", ORANGE, 15),
        _txt(vw / 2, 48, "Wedge", INK, 21),
        _txt(vw / 2, 426, "A small downward effort produces a large sideways "
                          "splitting force", MUT, 15),
    ]
    return _render(key, _svg("".join(body), vw, vh), 700, 550)


def screw(key):
    """A screw is an inclined plane wrapped around a cylinder."""
    vw, vh = 600, 440
    # screw body
    sx, sw_ = 360, 90
    top = 150
    body = [
        # head
        _rect(sx - 30, top - 34, sw_ + 60, 28, fill="#9AA3AD", stroke=INK,
              sw=2, rx=4),
        _line(sx + 10, top - 20, sx + sw_ - 10, top - 20, INK, 3),  # slot
        # shaft
        _rect(sx, top, sw_, 220, fill="#CBD2DB", stroke=INK, sw=2),
    ]
    # thread lines (slanted) across the shaft
    y = top + 18
    while y < top + 210:
        body.append(_line(sx, y, sx + sw_, y - 16, INK, 2))
        y += 24
    body += [
        # rotation arrow + downward motion
        _arc(sx + sw_ / 2, top - 60, 38, 200, -20, TEAL, 4),
        _txt(sx + sw_ / 2, top - 108, "turn", TEAL, 16),
        _line(sx + sw_ + 40, top, sx + sw_ + 40, top + 200, ORANGE, 6,
              marker="arrowO"),
        _txt(sx + sw_ + 78, top + 100, "moves in", ORANGE, 15),
        # inset: inclined plane wrapped around cylinder
        _poly([(70, 330), (250, 330), (250, 250)], fill=GLASS, stroke=INK,
              sw=2),
        _txt(160, 322, "inclined plane", MUT, 14),
        _txt(160, 372, "...wrapped around a rod", MUT, 14),
        _txt(vw / 2, 44, "Screw", INK, 21),
        _txt(vw / 2, 410, "A screw is an inclined plane wrapped around a "
                          "cylinder", MUT, 15),
    ]
    return _render(key, _svg("".join(body), vw, vh), 760, 557)


# ===========================================================================
# LIGHT — Grade 6 (S52, S53)
# ===========================================================================
def _sun(cx, cy, r, col=GOLD):
    out = [_circle(cx, cy, r, fill=col, stroke=INK, sw=2)]
    for a in range(0, 360, 30):
        x1 = cx + (r + 4) * math.cos(math.radians(a))
        y1 = cy + (r + 4) * math.sin(math.radians(a))
        x2 = cx + (r + 16) * math.cos(math.radians(a))
        y2 = cy + (r + 16) * math.sin(math.radians(a))
        out.append(_line(x1, y1, x2, y2, col, 3))
    return "".join(out)


def _eye(cx, cy):
    return ("".join([
        f'<path d="M {cx-26} {cy} Q {cx} {cy-22} {cx+26} {cy} '
        f'Q {cx} {cy+22} {cx-26} {cy} Z" fill="#FFFFFF" stroke="{INK}" '
        f'stroke-width="2"/>',
        _circle(cx, cy, 9, fill=BLUE, stroke=INK, sw=1.5),
        _circle(cx, cy, 4, fill=INK),
    ]))


def rectilinear_propagation(key):
    """Light travels in straight lines — seen through three aligned holes."""
    vw, vh = 660, 420
    ray_y = 220
    body = [_sun(80, ray_y, 26)]
    # three screens with a central hole, in a line
    for i, x in enumerate((220, 350, 480)):
        body.append(_rect(x, 110, 14, 95, fill="#B98A4B", stroke=INK, sw=2))
        body.append(_rect(x, ray_y + 18, 14, 95, fill="#B98A4B", stroke=INK,
                          sw=2))
        body.append(_txt(x + 7, 96, "ABC"[i], INK, 18))
    # straight ray through the holes to the eye
    body.append(_line(106, ray_y, 590, ray_y, RED, 3, dash="8 6",
                      marker="arrowR"))
    body.append(_eye(610, ray_y))
    body += [
        _txt(330, 60, "Light travels in a straight line", INK, 22),
        _txt(330, 392, "The eye sees the lamp only when all three holes line "
                       "up", MUT, 16),
    ]
    return _render(key, _svg("".join(body), vw, vh), 820, 522)


def pinhole_camera(key):
    """A pinhole camera makes a small, inverted image of an object."""
    vw, vh = 660, 440
    ph = (270, 240)        # pinhole
    body = [
        # box
        _rect(270, 140, 270, 200, fill="#EFF2F6", stroke=INK, sw=3),
        _circle(ph[0], ph[1], 4, fill=INK),
        _txt(ph[0] + 4, 130, "pinhole", MUT, 15, anchor="start"),
        # object (upright arrow) on the left
        _line(110, 300, 110, 170, ORANGE, 6, marker="arrowO"),
        _txt(110, 326, "object", ORANGE, 17),
        # rays from object top & bottom through the pinhole onto the screen
        _line(110, 170, ph[0], ph[1], RED, 2),
        _line(ph[0], ph[1], 528, 332, RED, 2),
        _line(110, 300, ph[0], ph[1], TEAL, 2),
        _line(ph[0], ph[1], 528, 150, TEAL, 2),
        # inverted image on the back wall (screen)
        _line(516, 160, 516, 322, PURPLE, 6, marker="arrowP"),
        _txt(516, 350, "inverted image", PURPLE, 15),
        _txt(330, 60, "Pinhole camera", INK, 22),
        _txt(330, 92, "Light travels straight, so the image is upside down",
             MUT, 16),
    ]
    return _render(key, _svg("".join(body), vw, vh), 820, 547)


def shadow_formation(key):
    """A point source casts a sharp shadow because light travels straight."""
    vw, vh = 660, 420
    sx, sy = 90, 215
    bx, by, br = 300, 215, 48
    scr = 568
    # tangent ray end-points on the screen
    top_y = by - br + (by - (by - br)) * 0  # ball top
    # rays from source to ball top/bottom, extended to the screen
    # ball top (bx, by-br), ball bottom (bx, by+br)
    def proj(px, py):
        m = (py - sy) / (px - sx)
        return scr, sy + m * (scr - sx)
    t = proj(bx, by - br)
    bm = proj(bx, by + br)
    body = [
        # screen
        _rect(scr, 70, 16, 300, fill="#E6E9EE", stroke=INK, sw=2),
        # shadow cone (umbra)
        _poly([(bx, by - br), (t[0], t[1]), (bm[0], bm[1]), (bx, by + br)],
              fill="#C9CDD4", stroke="none"),
        # opaque ball
        _circle(bx, by, br, fill="#4A5160", stroke=INK, sw=2),
        # light source
        _sun(sx, sy, 24),
        # grazing rays
        _line(sx, sy, t[0], t[1], GOLD, 2, dash="7 6"),
        _line(sx, sy, bm[0], bm[1], GOLD, 2, dash="7 6"),
        # dark shadow band on the screen
        _line(scr + 8, t[1], scr + 8, bm[1], INK, 10),
        _txt(scr + 40, (t[1] + bm[1]) / 2, "shadow", INK, 17, anchor="start"),
        _txt(bx, by + br + 30, "opaque object", MUT, 16),
        _txt(sx, sy - 44, "light source", MUT, 15),
        _txt(330, 50, "A shadow forms where light is blocked", INK, 21),
    ]
    return _render(key, _svg("".join(body), vw, vh), 820, 522)


def _shadow_cone(sun_c, sun_r, body_c, body_r, reach):
    """Tangent shadow cone behind a body lit from the sun (schematic)."""
    sx, sy = sun_c
    bx, by = body_c
    out = []
    # top and bottom tangent-ish rays: sun edge -> body edge -> beyond
    for sgn in (-1, 1):
        syy = sy + sgn * sun_r
        byy = by + sgn * body_r
        m = (byy - syy) / (bx - sx)
        ex = reach
        ey = syy + m * (ex - sx)
        out.append(_line(sx, syy, ex, ey, GOLD, 2, dash="6 6"))
    return "".join(out)


def solar_eclipse(key):
    """Solar eclipse: the Moon comes between the Sun and the Earth."""
    vw, vh = 680, 380
    sun_c, sun_r = (95, 195), 62
    moon_c, moon_r = (360, 195), 18
    earth_c, earth_r = (560, 195), 46
    # umbra from moon onto earth
    body = [
        _sun(sun_c[0], sun_c[1], sun_r),
        # moon shadow cone (inner crossing lines) onto the earth
        _poly([(moon_c[0], moon_c[1] - moon_r),
               (earth_c[0] - earth_r, earth_c[1]),
               (moon_c[0], moon_c[1] + moon_r)],
              fill="#2B3142", stroke="none"),
        _circle(earth_c[0], earth_c[1], earth_r, fill="#3E78C9", stroke=INK,
                sw=2),
        _circle(moon_c[0], moon_c[1], moon_r, fill="#8A8F99", stroke=INK,
                sw=2),
        _txt(sun_c[0], sun_c[1] + sun_r + 26, "Sun", GOLD, 18),
        _txt(moon_c[0], moon_c[1] - moon_r - 12, "Moon", MUT, 16),
        _txt(earth_c[0], earth_c[1] + earth_r + 26, "Earth", BLUE, 18),
        _txt(340, 44, "Solar eclipse", INK, 22),
        _txt(340, 350, "The Moon comes between the Sun and the Earth", MUT, 16),
    ]
    return _render(key, _svg("".join(body), vw, vh), 860, 480)


def lunar_eclipse(key):
    """Lunar eclipse: the Earth comes between the Sun and the Moon."""
    vw, vh = 680, 380
    sun_c, sun_r = (95, 195), 62
    earth_c, earth_r = (335, 195), 46
    moon_c, moon_r = (560, 195), 20
    body = [
        _sun(sun_c[0], sun_c[1], sun_r),
        # earth's shadow cone reaching the moon
        _poly([(earth_c[0], earth_c[1] - earth_r),
               (640, earth_c[1] - 2), (640, earth_c[1] + 2),
               (earth_c[0], earth_c[1] + earth_r)],
              fill="#2B3142", stroke="none"),
        _circle(earth_c[0], earth_c[1], earth_r, fill="#3E78C9", stroke=INK,
                sw=2),
        _circle(moon_c[0], moon_c[1], moon_r, fill="#5B6270", stroke=INK,
                sw=2),
        _txt(sun_c[0], sun_c[1] + sun_r + 26, "Sun", GOLD, 18),
        _txt(earth_c[0], earth_c[1] + earth_r + 26, "Earth", BLUE, 18),
        _txt(moon_c[0], moon_c[1] - moon_r - 12, "Moon", MUT, 16),
        _txt(340, 44, "Lunar eclipse", INK, 22),
        _txt(340, 350, "The Earth comes between the Sun and the Moon", MUT, 16),
    ]
    return _render(key, _svg("".join(body), vw, vh), 860, 480)


if __name__ == "__main__":
    funcs = [
        lambda: lever("xt_lever1", 1),
        lambda: lever("xt_lever2", 2),
        lambda: lever("xt_lever3", 3),
        lambda: lever_principle("xt_lever_principle"),
        lambda: pulley("xt_pulley_fixed", fixed=True),
        lambda: pulley("xt_pulley_movable", fixed=False),
        lambda: block_and_tackle("xt_block_tackle"),
        lambda: inclined_plane("xt_inclined"),
        lambda: wheel_and_axle("xt_wheel_axle"),
        lambda: wedge("xt_wedge"),
        lambda: screw("xt_screw"),
        lambda: rectilinear_propagation("xt_rectilinear"),
        lambda: pinhole_camera("xt_pinhole"),
        lambda: shadow_formation("xt_shadow"),
        lambda: solar_eclipse("xt_solar"),
        lambda: lunar_eclipse("xt_lunar"),
    ]
    for f in funcs:
        print(f())
