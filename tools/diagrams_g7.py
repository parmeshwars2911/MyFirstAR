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


# ===========================================================================
# LIGHT — Grade 7 (S37 reflection & plane mirror, S38 images & colour)
# ===========================================================================
# spectrum + additive/subtractive colour swatches
VIO = "#7B2FA0"
INDIGO = "#3F3D9A"
YELLOW = "#F4B400"
CYAN = "#27C2C2"
MAGENTA = "#D81B8C"


def _hatch(x, y0, y1, side=1, step=18, length=16, col=MUT):
    """Hatch marks along a vertical mirror line (back of the mirror)."""
    out = []
    y = y0
    while y < y1:
        out.append(_line(x, y, x + side * length, y - length, col, 2))
        y += step
    return "".join(out)


def plane_mirror_image(key):
    """Object in front of a plane mirror; virtual image equally far behind."""
    vw, vh = 680, 430
    mx = 380                       # mirror line
    ob, im = 210, 550              # object x and image x (equal distance)
    tip = 250
    body = [
        # mirror + hatching on its back (right) side
        _line(mx, 70, mx, 360, INK, 4),
        _hatch(mx, 80, 360, side=1),
        _txt(mx + 60, 64, "plane mirror", MUT, 15),
        # object (solid arrow) and virtual image (dashed arrow)
        _line(ob, 322, ob, tip, ORANGE, 6, marker="arrowO"),
        _txt(ob, 348, "object", ORANGE, 17),
        _line(im, 322, im, tip, PURPLE, 5, dash="7 6", marker="arrowP"),
        _txt(im, 348, "image (virtual)", PURPLE, 16),
        # two incident rays from the object tip to the mirror
        _line(ob, tip, mx, 197, RED, 3, marker="arrowR"),
        _line(ob, tip, mx, 215, RED, 3, marker="arrowR"),
        # reflected rays to the eye
        _line(mx, 197, 180, 140, TEAL, 3, marker="arrowT"),
        _line(mx, 215, 166, 172, TEAL, 3, marker="arrowT"),
        # virtual (back-projected) rays to the image tip, behind the mirror
        _line(mx, 197, im, tip, MUT, 2, dash="5 6"),
        _line(mx, 215, im, tip, MUT, 2, dash="5 6"),
        _eye(176, 152),
        _txt(150, 120, "eye", INK, 15),
        # equal-distance markers
        _line(ob, 388, mx, 388, MUT, 2, dash="4 5"),
        _line(mx, 388, im, 388, MUT, 2, dash="4 5"),
        _txt((ob + mx) / 2, 408, "object distance", MUT, 14),
        _txt((mx + im) / 2, 408, "= image distance", MUT, 14),
        _txt(330, 42, "Image in a plane mirror", INK, 22),
    ]
    return _render(key, _svg("".join(body), vw, vh), 850, 538)


def lateral_inversion(key):
    """A plane mirror swaps left and right — lateral inversion."""
    vw, vh = 620, 380
    mx = 310
    body = [
        _line(mx, 70, mx, 320, INK, 4),
        _hatch(mx, 80, 320, side=1),
        _txt(mx, 58, "mirror", MUT, 15),
        # object letter F on the left
        _txt(190, 250, "F", ORANGE, 150),
        _txt(190, 300, "object", ORANGE, 17),
        # mirror-flipped F on the right (reflected about its own centre)
        f'<g transform="translate(840,0) scale(-1,1)">'
        f'{_txt(420, 250, "F", PURPLE, 150)}</g>',
        _txt(430, 300, "image", PURPLE, 17),
        _txt(310, 40, "Lateral inversion", INK, 22),
        _txt(310, 352, "Left and right are interchanged; top and bottom are "
                       "not", MUT, 16),
    ]
    return _render(key, _svg("".join(body), vw, vh), 800, 490)


def regular_irregular_reflection(key):
    """Parallel rays stay parallel off a smooth surface but scatter off a "
    rough one."""
    vw, vh = 700, 410
    body = [_txt(175, 44, "Regular reflection", INK, 20),
            _txt(525, 44, "Irregular (diffuse) reflection", INK, 18)]
    # ---- left: smooth surface ----
    body.append(_rect(60, 300, 250, 16, fill="#C7CDD6", stroke=INK, sw=2))
    for ix in (120, 185, 250):
        body.append(_line(ix - 52, 232, ix, 300, RED, 3, marker="arrowR"))
        body.append(_line(ix, 300, ix + 52, 232, TEAL, 3, marker="arrowT"))
    body.append(_txt(185, 350, "smooth surface → rays stay parallel",
                     MUT, 14))
    # ---- right: rough surface ----
    bumps = [(380, 300), (410, 286), (440, 304), (470, 282), (500, 300),
             (530, 288), (560, 306), (600, 290)]
    body.append(_polyline(bumps, stroke=INK, sw=3))
    # incident parallel rays + scattered reflected rays
    scatter = [(408, 286, 360, 224), (468, 282, 500, 210),
               (528, 288, 560, 220), (588, 292, 640, 250)]
    for i, (hx, hy, rx, ry) in enumerate(scatter):
        body.append(_line(hx - 48, hy - 64, hx, hy, RED, 3, marker="arrowR"))
        body.append(_line(hx, hy, rx, ry, TEAL, 3, marker="arrowT"))
    body.append(_txt(500, 350, "rough surface → rays scatter every way",
                     MUT, 14))
    return _render(key, _svg("".join(body), vw, vh), 900, 527)


def normal_incidence(key):
    """A ray along the normal reflects straight back on itself (i = r = 0)."""
    vw, vh = 560, 360
    my = 290
    body = [
        _rect(70, my, 420, 16, fill="#C7CDD6", stroke=INK, sw=2),
        _line(280, 90, 280, my, MUT, 2, dash="6 6"),
        _txt(280, 74, "normal", MUT, 15),
        # incident (down) and reflected (up) along the same line, drawn offset
        _line(262, 110, 262, my - 4, RED, 4, marker="arrowR"),
        _line(298, my - 4, 298, 110, TEAL, 4, marker="arrowT"),
        _txt(228, 150, "incident", RED, 15, anchor="end"),
        _txt(332, 150, "reflected", TEAL, 15, anchor="start"),
        _txt(280, 44, "Normal incidence (i = 0°)", INK, 21),
        _txt(280, 340, "The ray strikes head-on and returns along the same "
                       "path", MUT, 15),
    ]
    return _render(key, _svg("".join(body), vw, vh), 720, 463)


def dispersion_spectrum(key):
    """White light splits into the VIBGYOR spectrum through a prism."""
    vw, vh = 700, 430
    apex = (300, 120)
    bl, br = (215, 330), (385, 330)
    ex = 332                       # exit face x near the lower-right edge
    exit_pt = (ex, 290)
    cols = [("#E63946", 184), ("#F4801A", 200), (YELLOW, 216),
            (GREEN, 232), (BLUE, 248), (INDIGO, 264), (VIO, 280)]
    body = [
        _poly([apex, bl, br], fill=GLASS, stroke=INK, sw=3),
        _txt(300, 250, "prism", MUT, 18),
        # white light in
        _line(70, 200, 246, 222, INK, 5, marker="arrow"),
        _txt(80, 186, "white light", INK, 15, anchor="start"),
    ]
    # fan of coloured rays onto a screen at x = 620
    for col, sy in cols:
        body.append(_line(exit_pt[0], exit_pt[1], 600, sy, col, 3))
        body.append(_rect(600, sy - 7, 40, 14, fill=col, stroke="none"))
    body += [
        _txt(620, 168, "R", MUT, 14),
        _txt(620, 300, "V", MUT, 14),
        _txt(350, 392, "White light is dispersed into seven colours "
                       "(VIBGYOR)", INK, 17),
    ]
    return _render(key, _svg("".join(body), vw, vh), 880, 540)


def _swatch(cx, cy, r, fill, label, lab_col=INK):
    return (_circle(cx, cy, r, fill=fill, stroke=INK, sw=2)
            + _txt(cx, cy + r + 22, label, lab_col, 16))


def colour_addition(key):
    """Primary colours of light add to give secondary colours and white."""
    vw, vh = 680, 430
    body = [_txt(340, 44, "Adding coloured lights (R + G + B)", INK, 21)]
    # primaries
    body += [_swatch(130, 140, 46, "#E63946", "Red"),
             _swatch(340, 140, 46, GREEN, "Green"),
             _swatch(550, 140, 46, BLUE, "Blue")]
    # secondary results as equations
    eqs = [(130, 300, YELLOW, "Red + Green = Yellow"),
           (340, 300, CYAN, "Green + Blue = Cyan"),
           (550, 300, MAGENTA, "Blue + Red = Magenta")]
    for cx, cy, col, lab in eqs:
        body.append(_circle(cx, cy, 38, fill=col, stroke=INK, sw=2))
        body.append(_txt(cx, cy + 60, lab, MUT, 14))
    body.append(_txt(340, 412, "All three together:  Red + Green + Blue  =  "
                               "White light", INK, 15))
    return _render(key, _svg("".join(body), vw, vh), 850, 538)


def colour_subtraction(key):
    """A coloured filter subtracts (absorbs) all colours except its own."""
    vw, vh = 660, 380
    fy = 200
    body = [
        # white light beam into the filter
        _rect(70, fy - 22, 230, 44, fill="#EDEDED", stroke=MUT, sw=1),
        _txt(185, fy + 2, "white light", MUT, 16),
        _line(60, fy, 300, fy, INK, 3, marker="arrow"),
        # the red filter
        _rect(312, 110, 26, 180, fill="#E63946", stroke=INK, sw=2),
        _txt(325, 96, "red filter", "#E63946", 15),
        # red light emerges
        _rect(338, fy - 18, 250, 36, fill="#F7C7CC", stroke="none"),
        _line(338, fy, 590, fy, "#E63946", 4, marker="arrowR"),
        _txt(470, fy - 30, "only red passes", "#E63946", 15),
        # the other colours are absorbed (blocked) at the filter
        _line(150, 130, 312, 150, GREEN, 3),
        _line(150, 270, 312, 250, BLUE, 3),
        _txt(150, 120, "green, blue… absorbed", MUT, 14, anchor="start"),
        _txt(330, 348, "A filter subtracts (absorbs) every colour except the "
                       "one it transmits", MUT, 15),
    ]
    return _render(key, _svg("".join(body), vw, vh), 820, 472)


# ===========================================================================
# HEAT — Grade 7 (S55 temperature, S56 effects/expansion, S57 transfer)
# ===========================================================================
MERCURY = "#C0392B"


def _flame(cx, base_y, h=70, w=44):
    """A small orange flame with its tip at the top, base at base_y."""
    half = w / 2
    return (f'<path d="M {cx} {base_y - h} '
            f'C {cx + half} {base_y - h + 26} {cx + half} {base_y - 8} '
            f'{cx} {base_y} '
            f'C {cx - half} {base_y - 8} {cx - half} {base_y - h + 26} '
            f'{cx} {base_y - h} Z" fill="{FLAME}" stroke="{ORANGE}" '
            f'stroke-width="2"/>'
            f'<path d="M {cx} {base_y - h + 24} '
            f'C {cx + half * 0.5} {base_y - h + 40} {cx + half * 0.5} '
            f'{base_y - 10} {cx} {base_y - 4} '
            f'C {cx - half * 0.5} {base_y - 10} {cx - half * 0.5} '
            f'{base_y - h + 40} {cx} {base_y - h + 24} Z" fill="{GOLD}"/>')


def thermometer_scales(key):
    """A liquid thermometer with the Celsius and Fahrenheit scales."""
    vw, vh = 460, 500
    tube_x, tube_w = 214, 28
    top, bot = 90, 392             # tube ends
    ice_y, steam_y = 360, 132      # lower and upper fixed points
    body = [
        _txt(230, 44, "The thermometer & its scales", INK, 21),
        # tube + bulb
        _rect(tube_x, top, tube_w, bot - top, fill="#FFFFFF", stroke=INK,
              sw=3, rx=14),
        _circle(tube_x + tube_w / 2, bot + 30, 30, fill=MERCURY, stroke=INK,
                sw=3),
        # mercury column up to just above the ice point
        _rect(tube_x + 7, 300, tube_w - 14, bot - 300 + 4, fill=MERCURY,
              stroke="none"),
        _circle(tube_x + tube_w / 2, bot, 14, fill=MERCURY, stroke="none"),
        # fixed-point ticks
        _line(tube_x - 6, steam_y, tube_x, steam_y, INK, 3),
        _line(tube_x - 6, ice_y, tube_x, ice_y, INK, 3),
        _line(tube_x + tube_w, steam_y, tube_x + tube_w + 6, steam_y, INK, 3),
        _line(tube_x + tube_w, ice_y, tube_x + tube_w + 6, ice_y, INK, 3),
        # Celsius (left)
        _txt(150, 70, "Celsius", TEAL, 17),
        _txt(150, steam_y + 6, "100°C", INK, 18, anchor="end"),
        _txt(150, ice_y + 6, "0°C", INK, 18, anchor="end"),
        _txt(150, steam_y + 30, "steam point", MUT, 13, anchor="end"),
        _txt(150, ice_y + 30, "ice point", MUT, 13, anchor="end"),
        # Fahrenheit (right)
        _txt(330, 70, "Fahrenheit", ORANGE, 17),
        _txt(tube_x + tube_w + 14, steam_y + 6, "212°F", INK, 18,
             anchor="start"),
        _txt(tube_x + tube_w + 14, ice_y + 6, "32°F", INK, 18, anchor="start"),
        _txt(230, 470, "0–100 on the Celsius scale; 32–212 on the Fahrenheit "
                       "scale", MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 560, 609)


def thermal_expansion_ball_ring(key):
    """Ball-and-ring: a cold ball passes through the ring, a hot one will "
    not."""
    vw, vh = 680, 410
    body = [_txt(340, 44, "Solids expand on heating", INK, 21)]
    # ---- left: cold ----
    body += [
        _circle(170, 180, 44, fill="none", stroke=IRON, sw=12),  # ring
        _circle(170, 300, 36, fill="#8FA0B5", stroke=INK, sw=2),  # ball below
        _line(170, 224, 170, 264, MUT, 2, dash="5 5", marker="arrow"),
        _txt(170, 96, "cold ball", MUT, 15),
        _txt(170, 366, "fits through the ring", GREEN, 16),
    ]
    # ---- right: hot ----
    body += [
        _circle(510, 200, 44, fill="none", stroke=IRON, sw=12),   # ring
        _circle(510, 150, 40, fill=MERCURY, stroke=INK, sw=2),    # bigger ball
        _flame(510, 290, h=60, w=40),
        _txt(510, 92, "heated ball", MUT, 15),
        _txt(510, 366, "now too big to pass", RED, 16),
    ]
    return _render(key, _svg("".join(body), vw, vh), 880, 530)


def bimetallic_strip(key):
    """Two bonded metals: straight when cold, bent when heated."""
    vw, vh = 660, 420
    body = [_txt(330, 44, "The bimetallic strip", INK, 21)]
    # ---- cold: straight ----
    body += [
        _rect(90, 150, 200, 16, fill=BRASS, stroke=INK, sw=1.5),
        _rect(90, 166, 200, 16, fill=IRON, stroke=INK, sw=1.5),
        _txt(190, 130, "cold — straight", MUT, 15),
        _txt(300, 158, "brass", BRASS, 13, anchor="start"),
        _txt(300, 178, "iron", MUT, 13, anchor="start"),
    ]
    # ---- hot: curls (brass expands more, so it is on the outside) ----
    body += [
        f'<path d="M 380 250 Q 500 250 560 170" fill="none" stroke="{BRASS}" '
        f'stroke-width="14" stroke-linecap="round"/>',
        f'<path d="M 380 264 Q 496 264 552 186" fill="none" stroke="{IRON}" '
        f'stroke-width="14" stroke-linecap="round"/>',
        _flame(440, 330, h=58, w=38),
        _txt(470, 130, "heated — bends toward iron", MUT, 15),
        _txt(330, 392, "Brass expands more than iron, so the strip curves",
             MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 820, 522)


def conduction(key):
    """Heat travels along a metal rod from the hot end — conduction."""
    vw, vh = 680, 380
    rod_y = 200
    body = [
        _txt(340, 44, "Conduction in a metal rod", INK, 21),
        # rod
        _rect(150, rod_y - 14, 420, 28, fill="#C7CDD6", stroke=INK, sw=2,
              rx=4),
        _flame(150, rod_y + 70, h=66, w=44),
        _txt(150, rod_y + 96, "heat", FLAME, 15),
        # heat-flow arrows along the rod
        _line(210, rod_y, 300, rod_y, RED, 4, marker="arrowR"),
        _line(330, rod_y, 420, rod_y, RED, 4, marker="arrowR"),
        _line(450, rod_y, 540, rod_y, RED, 4, marker="arrowR"),
    ]
    # wax-stuck pins hanging below; the nearest has fallen
    for i, x in enumerate((250, 340, 430, 520)):
        if i == 0:
            body.append(_circle(x, rod_y + 70, 7, fill=GOLD, stroke=INK,
                                sw=1.5))  # fallen pin
            body.append(_txt(x, rod_y + 100, "fell first", MUT, 12))
        else:
            body.append(_line(x, rod_y + 14, x, rod_y + 46, MUT, 2))
            body.append(_circle(x, rod_y + 52, 7, fill=GOLD, stroke=INK,
                                sw=1.5))
    body.append(_txt(340, 344, "Heat passes particle to particle from the hot "
                               "end to the cold end", MUT, 14))
    return _render(key, _svg("".join(body), vw, vh), 880, 491)


def convection(key):
    """Convection currents in a beaker of water heated from below."""
    vw, vh = 600, 440
    bx, by, bw, bh = 170, 110, 260, 230   # beaker
    body = [
        _txt(300, 44, "Convection in water", INK, 21),
        # beaker + water
        _rect(bx, by, bw, bh, fill="none", stroke=INK, sw=3),
        _rect(bx + 4, by + 40, bw - 8, bh - 44, fill=WATER, stroke="none"),
        _line(bx, by + 40, bx + bw, by + 40, BLUE, 2),
        _flame(bx + bw / 2, by + bh + 60, h=60, w=44),
        # circulation: up the middle, out at the top, down the sides
        _line(300, by + bh - 20, 300, by + 70, RED, 4, marker="arrowR"),
        _arc(360, by + 70, 60, 180, 60, RED, 3),
        _line(bx + bw - 24, by + 90, bx + bw - 24, by + bh - 30, BLUE, 4,
              marker="arrow"),
        _arc(240, by + 70, 60, 120, 0, BLUE, 3),
        _line(bx + 24, by + bh - 30, bx + 24, by + 90, BLUE, 0),
        _line(bx + 24, by + 90, bx + 24, by + bh - 30, BLUE, 4, marker="arrow"),
        _txt(300, by + 60, "hot water rises", RED, 14),
        _txt(300, by + bh - 6, "cool water sinks", BLUE, 13),
        _txt(300, 414, "Heated water rises, cooler water sinks — a convection "
                       "current", MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 720, 528)


def radiation(key):
    """Heat from the Sun crosses empty space to the Earth — radiation."""
    vw, vh = 680, 360
    sy = 190
    body = [_sun(110, sy, 50), _txt(110, sy + 78, "Sun", GOLD, 17)]
    # wavy heat rays crossing the vacuum
    for off in (-44, 0, 44):
        path = (f'<path d="M 175 {sy + off} q 20 -12 40 0 t 40 0 t 40 0 t 40 0 '
                f't 40 0 t 40 0" fill="none" stroke="{RED}" stroke-width="3" '
                f'marker-end="url(#arrowR)"/>')
        body.append(path)
    body += [
        _circle(590, sy, 46, fill="#3E78C9", stroke=INK, sw=2),
        _txt(590, sy + 76, "Earth", BLUE, 17),
        _txt(360, 86, "empty space (vacuum)", MUT, 15),
        _txt(340, 338, "Radiation needs no medium — heat crosses empty space",
             MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 880, 466)


def thermos_flask(key):
    """Cross-section of a vacuum (thermos) flask and how it cuts heat loss."""
    vw, vh = 560, 480
    cx = 250
    body = [
        _txt(280, 44, "The vacuum (thermos) flask", INK, 20),
        # outer case
        _rect(150, 90, 200, 360, fill="#EFF2F6", stroke=INK, sw=3, rx=18),
        # stopper
        _rect(170, 70, 160, 40, fill=WOOD, stroke=INK, sw=2, rx=6),
        # double silvered glass walls with vacuum between
        _rect(178, 120, 144, 312, fill="#FFFFFF", stroke="#B7C0CC", sw=8,
              rx=12),
        _rect(196, 138, 108, 276, fill=WATER, stroke=INK, sw=2, rx=10),
        _txt(cx, 280, "hot drink", INK, 15),
        # labels with leader lines
        _txt(470, 110, "stopper", MUT, 13, anchor="end"),
        _line(330, 92, 400, 104, MUT, 1.5),
        _txt(540, 220, "vacuum", MUT, 13, anchor="end"),
        _line(322, 250, 470, 224, MUT, 1.5),
        _txt(540, 250, "(stops conduction", MUT, 12, anchor="end"),
        _txt(540, 270, "& convection)", MUT, 12, anchor="end"),
        _txt(120, 300, "silvered", MUT, 13, anchor="start"),
        _txt(120, 320, "walls stop", MUT, 12, anchor="start"),
        _txt(120, 340, "radiation", MUT, 12, anchor="start"),
        _line(150, 310, 186, 300, MUT, 1.5),
        _txt(280, 470, "All three heat paths are blocked", MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 620, 531)


def black_white_surfaces(key):
    """Dull-black surfaces absorb and emit heat better than shiny-white ones."""
    vw, vh = 680, 400
    body = [_sun(340, 86, 34), _txt(340, 40, "Absorbing heat from the Sun",
                                    INK, 20)]
    # rays down to two plates
    for x in (150, 200, 250):
        body.append(_line(x + 40, 120, x, 230, GOLD, 2, dash="6 5",
                          marker="arrow"))
    for x in (430, 480, 530):
        body.append(_line(x, 120, x + 40, 230, GOLD, 2, dash="6 5",
                          marker="arrow"))
    # black plate (left) gets hot; shiny plate (right) stays cooler
    body += [
        _rect(120, 236, 150, 26, fill="#2B2B2B", stroke=INK, sw=2),
        _txt(195, 296, "dull black", INK, 15),
        _txt(195, 320, "gets hot fast", RED, 14),
        _rect(430, 236, 150, 26, fill="#E8ECF1", stroke=INK, sw=2),
        _txt(505, 296, "shiny white", INK, 15),
        _txt(505, 320, "stays cooler", BLUE, 14),
        _txt(340, 376, "Black, dull surfaces are the best absorbers and "
                       "emitters of heat", MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 880, 518)


def states_of_matter(key):
    """Particle arrangement in solids, liquids and gases (molecular motion)."""
    vw, vh = 720, 380
    def grid(x0, y0, cols, rows, dx, dy, jitter=0):
        import random
        random.seed(1)
        out = []
        for r in range(rows):
            for c in range(cols):
                jx = random.randint(-jitter, jitter) if jitter else 0
                jy = random.randint(-jitter, jitter) if jitter else 0
                out.append(_circle(x0 + c * dx + jx, y0 + r * dy + jy, 9,
                                   fill=TEAL, stroke=INK, sw=1.5))
        return "".join(out)
    body = [_txt(360, 40, "States of matter — how the particles sit", INK, 20)]
    # solid
    body += [_rect(60, 110, 180, 180, fill="#F1F5F8", stroke=INK, sw=2, rx=8),
             grid(95, 150, 4, 4, 38, 38, jitter=0),
             _txt(150, 320, "Solid", INK, 17),
             _txt(150, 346, "packed, vibrate in place", MUT, 12)]
    # liquid
    body += [_rect(270, 110, 180, 180, fill="#F1F5F8", stroke=INK, sw=2, rx=8),
             grid(305, 150, 4, 4, 38, 38, jitter=10),
             _txt(360, 320, "Liquid", INK, 17),
             _txt(360, 346, "close, slide past each other", MUT, 12)]
    # gas
    body.append(_rect(480, 110, 180, 180, fill="#F1F5F8", stroke=INK, sw=2,
                      rx=8))
    import random
    random.seed(7)
    for _ in range(8):
        gx = 500 + random.randint(0, 140)
        gy = 130 + random.randint(0, 140)
        body.append(_circle(gx, gy, 9, fill=TEAL, stroke=INK, sw=1.5))
    body += [_txt(570, 320, "Gas", INK, 17),
             _txt(570, 346, "far apart, move freely", MUT, 12),
             # heating arrows between the states
             _line(244, 200, 266, 200, RED, 3, marker="arrowR"),
             _line(454, 200, 476, 200, RED, 3, marker="arrowR"),
             _txt(255, 184, "heat", RED, 11),
             _txt(465, 184, "heat", RED, 11)]
    return _render(key, _svg("".join(body), vw, vh), 900, 475)


# ===========================================================================
# SOUND — Grade 7 (S66 production & medium, S67 wave terms, speed, echo)
# ===========================================================================
def sound_vibration(key):
    """A vibrating tuning fork sends out sound waves into the air."""
    vw, vh = 660, 420
    fx = 250                       # fork centre x
    body = [
        _txt(330, 44, "Sound is made by vibrations", INK, 21),
        # tuning fork (two prongs, joined, with a stem and base)
        _rect(fx - 56, 110, 14, 180, fill="#9AA3AD", stroke=INK, sw=1.5),
        _rect(fx + 42, 110, 14, 180, fill="#9AA3AD", stroke=INK, sw=1.5),
        _rect(fx - 56, 288, 112, 16, fill="#9AA3AD", stroke=INK, sw=1.5),
        _rect(fx - 8, 304, 16, 70, fill="#9AA3AD", stroke=INK, sw=1.5),
        _rect(fx - 26, 374, 52, 12, fill="#7C828B", stroke=INK, sw=1.5),
        # vibration motion lines beside the prongs
        _line(fx - 70, 150, fx - 60, 150, TEAL, 2),
        _line(fx - 74, 200, fx - 60, 200, TEAL, 2),
        _line(fx + 56, 150, fx + 70, 150, TEAL, 2),
        _line(fx + 56, 200, fx + 74, 200, TEAL, 2),
        _txt(fx, 100, "tuning fork", MUT, 14),
    ]
    # spreading sound waves (arcs) on the right
    for r in (80, 116, 152, 188):
        body.append(_arc(fx + 50, 200, r, 60, -60, BLUE, 2.5))
    body += [
        _txt(560, 200, "sound", BLUE, 16),
        _txt(560, 224, "waves", BLUE, 16),
        _txt(330, 404, "The prongs vibrate to and fro, pushing the air around "
                       "them", MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 860, 547)


def longitudinal_wave(key):
    """A sound wave in air: compressions and rarefactions along a spring."""
    vw, vh = 700, 400
    y0, h = 200, 44
    body = [_txt(350, 44, "A sound wave: compressions and rarefactions",
                 INK, 19)]
    # piston / source on the left
    body.append(_rect(54, y0 - h, 26, 2 * h, fill="#9AA3AD", stroke=INK, sw=2))
    body.append(_line(40, y0, 56, y0, INK, 4))
    # coils of the spring, dense in compressions, sparse in rarefactions
    x = 92.0
    while x < 620:
        body.append(_line(x, y0 - h, x, y0 + h, INK, 2))
        t = (x - 92) / 528.0
        sp = 14 - 7 * math.cos(2 * math.pi * 3 * t)
        x += sp
    # label three compressions (dense) and the rarefactions between
    for cx, lab, col in ((92, "C", RED), (268, "C", RED), (444, "C", RED),
                         (180, "R", BLUE), (356, "R", BLUE), (532, "R", BLUE)):
        body.append(_txt(cx, y0 - h - 14, lab, col, 18))
    body += [
        _txt(140, y0 + h + 30, "C = compression   R = rarefaction", MUT, 14,
             anchor="start"),
        # wave direction + particle motion (both horizontal = longitudinal)
        _line(560, y0 + h + 26, 620, y0 + h + 26, INK, 3, marker="arrow"),
        _txt(560, y0 + h + 50, "wave travels →", INK, 13, anchor="start"),
        _line(300, 96, 360, 96, PURPLE, 3, marker="arrow"),
        _line(360, 96, 300, 96, PURPLE, 3, marker="arrow"),
        _txt(330, 80, "particles vibrate along the wave", PURPLE, 13),
    ]
    return _render(key, _svg("".join(body), vw, vh), 900, 514)


def bell_jar(key):
    """The bell-jar experiment: sound fades as air is pumped out — sound "
    needs a medium."""
    vw, vh = 600, 460
    cx = 280
    body = [
        _txt(300, 44, "Sound needs a medium", INK, 21),
        # base plate
        _rect(150, 360, 260, 20, fill="#9AA3AD", stroke=INK, sw=2),
        # glass bell jar (dome)
        f'<path d="M 170 360 L 170 200 A 110 110 0 0 1 390 200 L 390 360 Z" '
        f'fill="#EAF6FF" fill-opacity="0.6" stroke="{INK}" stroke-width="3"/>',
        _txt(cx, 120, "glass jar", MUT, 14),
        # electric bell hanging inside (suspended from the top by threads)
        _line(cx, 150, cx - 22, 210, MUT, 1.5),
        _line(cx, 150, cx + 22, 210, MUT, 1.5),
        f'<path d="M {cx-34} 270 Q {cx-34} 214 {cx} 210 Q {cx+34} 214 {cx+34} '
        f'270 Z" fill="#D9A441" stroke="{INK}" stroke-width="2"/>',
        _circle(cx, 280, 7, fill="#7C828B", stroke=INK, sw=1.5),
        _txt(cx, 320, "electric bell", MUT, 13),
        # outlet tube to the pump
        _rect(390, 332, 70, 16, fill="#C7CDD6", stroke=INK, sw=2),
        _rect(456, 312, 70, 56, fill="#EFF2F6", stroke=INK, sw=2, rx=6),
        _txt(491, 344, "to pump", MUT, 12),
        _txt(300, 432, "As the air is pumped out, the bell is seen but barely "
                       "heard", MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 720, 552)


def wave_terms(key):
    """A wave graph defining wavelength, amplitude, crest and trough."""
    vw, vh = 700, 400
    midy, amp, lam = 210, 70, 150
    x0 = 90
    # sample a sine wave (two full wavelengths)
    pts = []
    x = x0
    while x <= x0 + 2 * lam + 1:
        ang = 2 * math.pi * (x - x0) / lam
        pts.append((round(x, 1), round(midy - amp * math.sin(ang), 1)))
        x += 4
    body = [
        _txt(350, 44, "The parts of a wave", INK, 21),
        _line(60, midy, 640, midy, MUT, 2, dash="5 5"),
        _txt(70, midy - 8, "rest", MUT, 12, anchor="start"),
        _polyline(pts, stroke=BLUE, sw=3),
    ]
    # crest and trough markers (first crest at quarter wavelength)
    c1 = x0 + lam / 4
    body += [
        _txt(c1, midy - amp - 14, "crest", RED, 14),
        _txt(c1 + lam / 2, midy + amp + 24, "trough", PURPLE, 14),
        # amplitude (rest -> crest)
        _line(c1, midy, c1, midy - amp, GREEN, 2, dash="4 4"),
        _txt(c1 + 40, midy - amp / 2, "amplitude", GREEN, 13, anchor="start"),
        # wavelength (crest to crest)
        _line(c1, midy - amp - 30, c1 + lam, midy - amp - 30, INK, 2,
              marker="arrow"),
        _line(c1 + lam, midy - amp - 30, c1, midy - amp - 30, INK, 2,
              marker="arrow"),
        _txt(c1 + lam / 2, midy - amp - 38, "wavelength λ", INK, 14),
        _txt(350, 384, "Frequency = waves per second; time period = time for "
                       "one wave", MUT, 13),
    ]
    return _render(key, _svg("".join(body), vw, vh), 900, 514)


def sound_spectrum(key):
    """The frequency ranges: infrasonic, audible and ultrasonic."""
    vw, vh = 720, 320
    y, h = 150, 70
    body = [_txt(360, 48, "Ranges of sound frequency", INK, 21)]
    segs = [(70, 210, "#BFD8F2", "Infrasonic", "below 20 Hz"),
            (210, 510, "#A8E6CF", "Audible", "20 Hz – 20,000 Hz"),
            (510, 650, "#F6C7B6", "Ultrasonic", "above 20,000 Hz")]
    for x1, x2, col, name, sub in segs:
        body.append(_rect(x1, y, x2 - x1, h, fill=col, stroke=INK, sw=2))
        body.append(_txt((x1 + x2) / 2, y + 30, name, INK, 16))
        body.append(_txt((x1 + x2) / 2, y + 54, sub, MUT, 12))
    body += [
        _txt(210, y + h + 24, "20 Hz", INK, 13),
        _txt(510, y + h + 24, "20 kHz", INK, 13),
        _txt(360, y + h + 60, "Humans hear only the middle (audible) range",
             MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 900, 400)


def echo_reflection(key):
    """An echo: sound travels to a wall and reflects back to the listener."""
    vw, vh = 680, 380
    body = [
        _txt(330, 44, "An echo is reflected sound", INK, 21),
        # listener (head)
        _circle(110, 220, 26, fill="#F2C9A0", stroke=INK, sw=2),
        _txt(110, 280, "listener", MUT, 14),
        # tall wall / cliff on the right
        _rect(560, 90, 40, 250, fill="#B7A98F", stroke=INK, sw=2),
        _txt(580, 76, "wall", MUT, 14),
        # outgoing sound (arcs going right)
        _arc(150, 200, 90, 55, -55, RED, 2.5),
        _arc(150, 200, 130, 55, -55, RED, 2.5),
        _line(180, 180, 545, 160, RED, 3, marker="arrowR"),
        _txt(360, 138, "original sound →", RED, 14),
        # reflected sound (echo) coming back
        _line(545, 240, 180, 250, TEAL, 3, marker="arrowT"),
        _txt(360, 280, "← echo (reflected)", TEAL, 14),
        _txt(330, 352, "The echo returns after the sound bounces off a distant "
                       "surface", MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 880, 492)


# ===========================================================================
# ELECTRICITY & MAGNETISM — Grade 7 (S76 magnets/electromagnet, S77 bell &
# circuits, S78 current, symbols, series/parallel, safety)
# ===========================================================================
NPOLE = "#E63946"
SPOLE = "#2563EB"


def _bar_magnet(x, y, w, h, left="N", right="S"):
    """A bar magnet split into two coloured poles with letters."""
    half = w / 2
    lc = NPOLE if left == "N" else SPOLE
    rc = NPOLE if right == "N" else SPOLE
    return "".join([
        _rect(x, y, half, h, fill=lc, stroke=INK, sw=2),
        _rect(x + half, y, half, h, fill=rc, stroke=INK, sw=2),
        _txt(x + half / 2, y + h / 2 + 8, left, "#FFFFFF", 24),
        _txt(x + half + half / 2, y + h / 2 + 8, right, "#FFFFFF", 24),
    ])


def _bulb_symbol(cx, cy, r=22):
    """Standard lamp symbol: a circle with a cross inside."""
    d = r * 0.7
    return "".join([
        _circle(cx, cy, r, fill="#FFFFFF", stroke=INK, sw=2.5),
        _line(cx - d, cy - d, cx + d, cy + d, INK, 2.5),
        _line(cx - d, cy + d, cx + d, cy - d, INK, 2.5),
    ])


def _cell_symbol(cx, cy, scale=1.0):
    """A single cell: a long thin (+) plate and a short thick (-) plate."""
    g = 7 * scale
    return "".join([
        _line(cx - g, cy - 18 * scale, cx - g, cy + 18 * scale, INK, 2),
        _line(cx + g, cy - 10 * scale, cx + g, cy + 10 * scale, INK, 6),
    ])


def _switch_symbol(cx, cy, closed=False):
    """An open or closed switch: two contacts and a hinged lever."""
    out = [_circle(cx - 22, cy, 4, fill=INK), _circle(cx + 22, cy, 4,
                                                      fill=INK)]
    if closed:
        out.append(_line(cx - 22, cy, cx + 22, cy, INK, 3))
    else:
        out.append(_line(cx - 22, cy, cx + 16, cy - 22, INK, 3))
    return "".join(out)


def bar_magnet_field(key):
    """Field lines of a bar magnet, running from N to S outside the magnet."""
    vw, vh = 700, 440
    mx, my, mw, mh = 250, 195, 200, 56
    cy = my + mh / 2
    body = [
        _txt(350, 44, "Magnetic field of a bar magnet", INK, 21),
        _bar_magnet(mx, my, mw, mh, "N", "S"),
    ]
    # field loops above and below, from the N end (left) to the S end (right)
    for d in (34, 78, 124):
        # top loop
        body.append(
            f'<path d="M {mx} {cy} C {mx - d} {cy - d - 30} '
            f'{mx + mw + d} {cy - d - 30} {mx + mw} {cy}" fill="none" '
            f'stroke="{MUT}" stroke-width="2"/>')
        # bottom loop
        body.append(
            f'<path d="M {mx} {cy} C {mx - d} {cy + d + 30} '
            f'{mx + mw + d} {cy + d + 30} {mx + mw} {cy}" fill="none" '
            f'stroke="{MUT}" stroke-width="2"/>')
        # direction arrowheads near the top and bottom of each loop (N -> S)
        body.append(_line(mx + mw / 2 - 6, cy - d - 18, mx + mw / 2 + 14,
                          cy - d - 18, MUT, 2, marker="arrow"))
        body.append(_line(mx + mw / 2 - 6, cy + d + 18, mx + mw / 2 + 14,
                          cy + d + 18, MUT, 2, marker="arrow"))
    body.append(_txt(350, 410, "Field lines leave the N pole and return to "
                               "the S pole", MUT, 14))
    return _render(key, _svg("".join(body), vw, vh), 900, 566)


def magnet_poles(key):
    """The law of magnetism: like poles repel, unlike poles attract."""
    vw, vh = 700, 420
    body = [_txt(350, 44, "The law of magnetism", INK, 20)]
    # ---- like poles facing (N ... N) repel: arrows point apart ----
    body += [_bar_magnet(120, 110, 150, 44, "S", "N"),
             _bar_magnet(430, 110, 150, 44, "N", "S"),
             _line(322, 132, 288, 132, RED, 4, marker="arrowR"),
             _line(378, 132, 412, 132, RED, 4, marker="arrowR"),
             _txt(350, 188, "Like poles (N–N) repel", RED, 16)]
    # ---- unlike poles facing (N ... S) attract: arrows point together ----
    body += [_bar_magnet(120, 270, 150, 44, "S", "N"),
             _bar_magnet(430, 270, 150, 44, "S", "N"),
             _line(288, 292, 322, 292, GREEN, 4, marker="arrow"),
             _line(412, 292, 378, 292, GREEN, 4, marker="arrow"),
             _txt(350, 348, "Unlike poles (N–S) attract", GREEN, 16),
             _txt(350, 394, "Repulsion is the only sure test of a magnet",
                  MUT, 14)]
    return _render(key, _svg("".join(body), vw, vh), 900, 540)


def electromagnet(key):
    """A solenoid: wire wound continuously around a soft-iron core, wired to a
    cell and a switch. Layered so the front of each turn shows over the core
    and the back of each turn is hidden behind it."""
    vw, vh = 700, 420
    core_x, core_y, core_w, core_h = 226, 196, 248, 34
    cy = core_y + core_h / 2
    rod_t, rod_b = core_y, core_y + core_h
    xs, xe = core_x + 26, core_x + core_w - 26
    turns = 9
    ry = 44
    ct, cb = cy - ry, cy + ry
    pitch = (xe - xs) / (turns - 1)
    body = [_txt(350, 44, "The electromagnet", INK, 21)]
    # 1) back of each turn (hidden by the core)
    for i in range(turns - 1):
        x1 = xs + i * pitch
        x2 = xs + (i + 1) * pitch
        body.append(f'<line x1="{x1}" y1="{cb}" x2="{x2}" y2="{ct}" '
                    f'stroke="{COPPER}" stroke-width="6" '
                    f'stroke-linecap="round"/>')
    # 2) the soft-iron core
    body += [
        _rect(core_x, core_y, core_w, core_h, fill="#B7C0CC", stroke=INK,
              sw=2, rx=4),
        _txt(350, cy + 6, "soft-iron core", "#33373F", 13),
        _txt(core_x - 18, cy + 7, "N", NPOLE, 22),
        _txt(core_x + core_w + 18, cy + 7, "S", SPOLE, 22),
    ]
    # 3) front of each turn (over the core)
    for i in range(turns):
        x = xs + i * pitch
        body.append(f'<path d="M {x} {ct} Q {x + 13} {cy} {x} {cb}" '
                    f'fill="none" stroke="{COPPER}" stroke-width="6" '
                    f'stroke-linecap="round"/>')
    # 4) leads from the two coil ends to a cell + switch (one circuit)
    yb = 350
    body += [
        _line(xs, ct, xs - 30, ct, COPPER, 5),
        _line(xs - 30, ct, xs - 30, yb, COPPER, 5),
        _line(xs - 30, yb, 282, yb, COPPER, 3),
        _cell_symbol(296, yb),
        _line(312, yb, 404, yb, COPPER, 3),
        _switch_symbol(430, yb, closed=True),
        _line(452, yb, xe + 30, yb, COPPER, 3),
        _line(xe + 30, yb, xe + 30, cb, COPPER, 5),
        _line(xe + 30, cb, xe, cb, COPPER, 5),
        _txt(296, yb + 32, "cell", MUT, 13),
        _txt(430, yb + 32, "switch", MUT, 13),
        _txt(350, 408, "Current in the coil turns the iron core into a "
                       "magnet", MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 900, 540)


def electric_bell(key):
    """Schematic of an electric bell."""
    vw, vh = 640, 480
    body = [_txt(320, 40, "The electric bell", INK, 21)]
    # gong (bell dome) top
    body += [
        f'<path d="M 250 120 A 70 70 0 0 1 390 120 Z" fill="#D9A441" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(320, 96, "gong", MUT, 13),
    ]
    # armature: a vertical soft-iron strip with a hammer arm to the gong
    body += [
        _line(300, 150, 300, 300, INK, 5),           # armature strip
        _line(300, 150, 330, 132, INK, 4),           # hammer arm
        _circle(336, 128, 9, fill="#7C828B", stroke=INK, sw=1.5),  # hammer
        _txt(360, 150, "hammer", MUT, 12, anchor="start"),
        _txt(262, 230, "armature", MUT, 12, anchor="end"),
        # spring holding the armature
        _line(300, 300, 270, 320, MUT, 2),
        _txt(250, 330, "spring", MUT, 12, anchor="end"),
    ]
    # electromagnet (two coils on a core) pulling the armature
    body += [
        _rect(330, 250, 70, 70, fill="#B7C0CC", stroke=INK, sw=2, rx=4),
    ]
    # two coils wound on the limbs, drawn as connected winding strokes
    for ex in (348, 382):
        for yy in range(258, 318, 10):
            body.append(_line(ex - 13, yy + 8, ex + 13, yy, COPPER, 3.5))
    body += [
        _txt(430, 285, "electromagnet", MUT, 12, anchor="start"),
        # contact screw touching the armature
        _circle(284, 270, 5, fill=INK),
        _line(220, 270, 284, 270, INK, 3),
        _txt(210, 270, "contact", MUT, 12, anchor="end"),
        _txt(210, 288, "screw", MUT, 12, anchor="end"),
    ]
    # cell + push switch in the circuit at the bottom
    body += [
        _line(220, 270, 220, 410, COPPER, 3),
        _cell_symbol(220, 410),
        _line(220, 428, 320, 428, COPPER, 3),
        _switch_symbol(360, 428, closed=False),
        _line(382, 428, 470, 428, COPPER, 3),
        _line(470, 428, 470, 300, COPPER, 3),
        _line(470, 300, 400, 285, COPPER, 3),
        _txt(220, 446, "cell", MUT, 12),
        _txt(360, 460, "push switch", MUT, 12),
        _txt(320, 474, "Pressing the switch rings the bell repeatedly", MUT,
             13),
    ]
    return _render(key, _svg("".join(body), vw, vh), 720, 540)


def magnetic_declination(key):
    """The angle between geographic north and magnetic north."""
    vw, vh = 600, 440
    ox, oy = 300, 360
    body = [
        _txt(300, 44, "Magnetic declination", INK, 21),
        # geographic (true) north — vertical
        _line(ox, oy, ox, 110, MUT, 3, marker="arrow"),
        _txt(ox + 8, 100, "Geographic North", MUT, 14, anchor="start"),
        # magnetic north — tilted
        _line(ox, oy, ox - 80, 130, NPOLE, 3, marker=None),
        f'<path d="M {ox-80} 130 l 10 6 l -2 -12 Z" fill="{NPOLE}"/>',
        _txt(ox - 88, 120, "Magnetic North", NPOLE, 14, anchor="end"),
        # angle of declination between them
        _arc(ox, oy, 150, 90, 108, INK, 2),
        _txt(ox - 36, 200, "declination", INK, 13, anchor="end"),
        # small compass needle pointing along magnetic north
        _circle(ox, oy, 22, fill="#FFFFFF", stroke=INK, sw=2),
        f'<path d="M {ox} {oy-18} L {ox+6} {oy} L {ox} {oy+18} L {ox-6} {oy} '
        f'Z" fill="{NPOLE}"/>',
        _txt(300, 410, "A compass points to magnetic north, not true north",
             MUT, 14),
    ]
    return _render(key, _svg("".join(body), vw, vh), 740, 543)


def simple_circuit(key):
    """A simple circuit: cell, switch, bulb and connecting wires."""
    vw, vh = 640, 420
    x1, x2, y1, y2 = 150, 490, 130, 330
    body = [
        _txt(320, 44, "A simple electric circuit", INK, 21),
        # wire loop
        _line(x1, y1, x2, y1, INK, 3),
        _line(x2, y1, x2, y2, INK, 3),
        _line(x2, y2, x1, y2, INK, 3),
        _line(x1, y2, x1, y1, INK, 3),
        # switch on the top wire
        _rect(290, y1 - 14, 60, 28, fill="#F4F6F8", stroke="none"),
        _switch_symbol(320, y1, closed=True),
        _txt(320, y1 - 24, "switch", MUT, 13),
        # cell on the bottom wire
        _rect(296, y2 - 22, 48, 44, fill="#F4F6F8", stroke="none"),
        _cell_symbol(320, y2),
        _txt(320, y2 + 36, "cell", MUT, 13),
        # bulb on the right wire
        _rect(x2 - 24, 206, 48, 48, fill="#F4F6F8", stroke="none"),
        _bulb_symbol(x2, 230),
        _txt(x2 + 30, 230, "bulb", MUT, 13, anchor="start"),
        # conventional current arrows (out of + terminal)
        _line(200, y1, 240, y1, RED, 3, marker="arrowR"),
        _txt(220, y1 - 16, "current", RED, 12),
        _line(x2, 280, x2, 310, RED, 3, marker="arrowR"),
        _line(x1, 280, x1, 250, RED, 3, marker="arrowR"),
        _txt(320, 404, "Current flows in a complete loop from the cell, "
                       "through the bulb, and back", MUT, 13),
    ]
    return _render(key, _svg("".join(body), vw, vh), 760, 499)


def circuit_symbols(key):
    """A chart of the common circuit symbols."""
    vw, vh = 720, 420
    body = [_txt(360, 40, "Common circuit symbols", INK, 20)]
    cells = [
        ("cell", lambda x, y: _cell_symbol(x, y)),
        ("battery", lambda x, y: _cell_symbol(x - 12, y) + _cell_symbol(x + 12,
                                                                        y)),
        ("bulb / lamp", lambda x, y: _bulb_symbol(x, y, 18)),
        ("wire", lambda x, y: _line(x - 26, y, x + 26, y, INK, 3)),
        ("open switch", lambda x, y: _switch_symbol(x, y, closed=False)),
        ("closed switch", lambda x, y: _switch_symbol(x, y, closed=True)),
        ("wires joined", lambda x, y: _line(x - 26, y, x + 26, y, INK, 3)
            + _line(x, y, x, y - 22, INK, 3) + _circle(x, y, 5, fill=INK)),
        ("wires crossing", lambda x, y: _line(x - 26, y, x + 26, y, INK, 3)
            + _line(x, y - 22, x, y + 22, INK, 3)),
    ]
    cw, ch = 170, 150
    x0, y0 = 30, 80
    for i, (name, draw) in enumerate(cells):
        r, c = divmod(i, 4)
        x = x0 + c * cw
        y = y0 + r * ch
        body.append(_rect(x, y, cw - 14, ch - 20, fill="#F7F9FB",
                          stroke="#D7DCE3", sw=1.5, rx=8))
        body.append(draw(x + (cw - 14) / 2, y + 44))
        body.append(_txt(x + (cw - 14) / 2, y + ch - 36, name, INK, 14))
    return _render(key, _svg("".join(body), vw, vh), 900, 525)


def series_parallel(key):
    """Two bulbs connected in series and in parallel."""
    vw, vh = 720, 400
    body = [_txt(190, 44, "Series circuit", INK, 18),
            _txt(540, 44, "Parallel circuit", INK, 18)]
    # ---- series (left): one loop, two bulbs in line ----
    sx1, sx2, sy1, sy2 = 60, 320, 110, 320
    body += [
        _line(sx1, sy1, sx2, sy1, INK, 3),
        _line(sx2, sy1, sx2, sy2, INK, 3),
        _line(sx2, sy2, sx1, sy2, INK, 3),
        _line(sx1, sy2, sx1, sy1, INK, 3),
        _cell_symbol(190, sy2),
        _bulb_symbol(150, sy1, 18),
        _bulb_symbol(250, sy1, 18),
        _txt(190, sy2 + 34, "one path for the current", MUT, 12),
    ]
    # ---- parallel (right): two branches ----
    px1, px2, py1, py2 = 430, 660, 110, 320
    midx = (px1 + px2) / 2
    body += [
        _line(px1, py1, px2, py1, INK, 3),
        _line(px2, py1, px2, py2, INK, 3),
        _line(px2, py2, px1, py2, INK, 3),
        _line(px1, py2, px1, py1, INK, 3),
        _cell_symbol(midx, py2),
        # two parallel branches carrying a bulb each
        _line(490, py1, 490, py2, INK, 3),
        _bulb_symbol(490, 200, 18),
        _line(600, py1, 600, py2, INK, 3),
        _bulb_symbol(600, 200, 18),
        _txt(midx, py2 + 34, "separate paths for the current", MUT, 12),
    ]
    return _render(key, _svg("".join(body), vw, vh), 900, 500)


def torch(key):
    """A simple electric torch with two dry cells, a switch and a bulb."""
    vw, vh = 660, 360
    body = [
        _txt(330, 40, "Inside an electric torch", INK, 21),
        # body case
        _rect(120, 130, 380, 110, fill="#EFF2F6", stroke=INK, sw=3, rx=18),
        # reflector + bulb at the front (left)
        _poly([(120, 140), (120, 230), (170, 210), (170, 160)], fill="#DCE3EA",
              stroke=INK, sw=2),
        _bulb_symbol(150, 185, 18),
        _txt(120, 268, "bulb &", MUT, 12),
        _txt(120, 284, "reflector", MUT, 12),
        # two dry cells in series
        _cell_symbol(280, 185, 1.2),
        _cell_symbol(360, 185, 1.2),
        _line(300, 185, 340, 185, INK, 3),
        _line(170, 185, 256, 185, INK, 3),
        _line(384, 185, 470, 185, INK, 3),
        _txt(320, 250, "two dry cells", MUT, 13),
        # switch on top
        _switch_symbol(420, 130, closed=False),
        _txt(440, 110, "switch", MUT, 12, anchor="start"),
        _line(470, 185, 470, 138, INK, 3),
        _txt(330, 330, "Sliding the switch completes the circuit and lights "
                       "the bulb", MUT, 13),
    ]
    return _render(key, _svg("".join(body), vw, vh), 880, 480)


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
