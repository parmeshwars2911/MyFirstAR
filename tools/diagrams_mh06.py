"""
Physics schematics for the Maharashtra board Standard 6 decks.

Same contract as diagrams.py / diagrams_mh.py: each diagram is an SVG string
rasterised to PNG with cairosvg into build/img/, and the PNG path is returned.
Reuses the shared SVG helpers/palette so the visual style matches the rest of
the catalog. New file so the existing diagram modules stay untouched.

Covers the Std 6 physics chapters:
  * Simple Machines  — lever classes, pulley, inclined plane, wedge & screw,
                       wheel and axle
  * Work and Energy  — potential vs kinetic energy, forms of energy,
                       an energy-conversion chain
  * Sound            — vibrating sources, sound needs a medium (bell jar)
  * Light & Shadows  — transparent / translucent / opaque materials
  * Fun with Magnets — making a magnet by stroking, magnetic vs non-magnetic
  * The Universe     — the solar system (planets in order)
"""
import os
import sys
import math

sys.path.insert(0, os.path.dirname(__file__))
from diagrams import (  # noqa: E402
    _svg, _line, _txt, _render,
    INK, MUT, TEAL, ORANGE, PURPLE, RED, BLUE, GLASS, WATER, GREEN, GOLD,
)
from diagrams_mh import _circle, _rect, _poly, _ellipse, SKY, FLAME, SILVER
from diagrams_extra import IRON, WOOD


# ===========================================================================
# Simple Machines
# ===========================================================================
def lever_types(key):
    """Three classes of lever, showing fulcrum (F), load (L) and effort (E)."""
    vw, vh = 760, 470
    body = _txt(vw / 2, 30, "The three classes of lever", col=INK, size=18)
    fulc = "#8A94A6"

    def beam(cx, cy, label, sub, f_at, l_at, e_at):
        s = _rect(cx - 150, cy - 8, 300, 16, fill="#E7ECF2", stroke=INK, sw=2,
                  rx=4)
        # fulcrum triangle
        fx = cx + f_at
        s2 = _poly([(fx - 20, cy + 40), (fx + 20, cy + 40), (fx, cy + 8)],
                   fill=fulc, stroke=INK, sw=2)
        s2 += _txt(fx, cy + 60, "F  (fulcrum)", col=INK, size=13)
        # load box
        lx = cx + l_at
        s2 += _rect(lx - 20, cy - 44, 40, 34, fill=IRON, stroke=INK, sw=2, rx=3)
        s2 += _txt(lx, cy - 56, "L  (load)", col=RED, size=13)
        # effort arrow (down)
        ex = cx + e_at
        s2 += _line(ex, cy - 52, ex, cy - 12, col=GREEN, w=4, marker="arrowR")
        s2 += _txt(ex, cy - 62, "E  (effort)", col=GREEN, size=13)
        s2 += _txt(cx - 200, cy, label, col=INK, size=15, anchor="end")
        s2 += _txt(cx - 200, cy + 20, sub, col=MUT, size=11, anchor="end",
                   bold=False)
        return s + s2

    body += beam(430, 120, "Class 1", "F in the middle", 0, -110, 110)
    body += beam(430, 260, "Class 2", "L in the middle", 130, 0, -120)
    body += beam(430, 400, "Class 3", "E in the middle", -130, 120, 0)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def pulley(key):
    """A single fixed pulley: pull down on one side to raise the load."""
    vw, vh = 460, 520
    cx = vw / 2
    # support beam
    body = _rect(cx - 150, 50, 300, 18, fill="#C9B79C", stroke=INK, sw=2, rx=3)
    # pulley wheel
    wy = 130
    body += _circle(cx, wy, 46, fill="#E7ECF2", stroke=INK, sw=3)
    body += _circle(cx, wy, 8, fill=MUT, stroke=INK, sw=2)
    body += _line(cx, 68, cx, wy - 46, col=MUT, w=4)
    # rope over the wheel
    body += _line(cx - 46, wy, cx - 46, 360, col=ORANGE, w=4)
    body += _line(cx + 46, wy, cx + 46, 300, col=ORANGE, w=4)
    body += f'<path d="M {cx-46} {wy} A 46 46 0 0 1 {cx+46} {wy}" fill="none" stroke="{ORANGE}" stroke-width="4"/>'
    # load on the left
    body += _rect(cx - 78, 360, 64, 60, fill=IRON, stroke=INK, sw=2, rx=4)
    body += _txt(cx - 46, 395, "load", col="#FFFFFF", size=15)
    body += _line(cx - 46, 360, cx - 46, 360, col=ORANGE, w=4)
    # effort (hand pulling down) on the right
    body += _line(cx + 46, 300, cx + 46, 340, col=GREEN, w=5, marker="arrowR")
    body += _txt(cx + 90, 330, "pull down", col=GREEN, size=14, anchor="start")
    body += _txt(cx + 90, 350, "(effort)", col=MUT, size=12, anchor="start",
                 bold=False)
    body += _txt(cx, 30, "A fixed pulley", col=INK, size=17)
    body += _txt(cx, vh - 20, "Changes the direction of the force", col=MUT,
                 size=13, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def inclined_plane(key):
    """A ramp: a smaller effort along the slope raises a load to a height."""
    vw, vh = 620, 420
    # ground
    body = _line(60, 340, 560, 340, col=INK, w=3)
    # ramp triangle
    body += _poly([(90, 340), (520, 340), (90, 130)], fill="#EDE3D4",
                  stroke=INK, sw=3)
    # height marker
    body += _line(78, 130, 78, 340, col=MUT, w=2, dash="5,5")
    body += _txt(60, 235, "height", col=MUT, size=13, anchor="end")
    # box on the ramp
    bx, by = 300, 232
    body += _rect(bx - 26, by - 24, 52, 44, fill=IRON, stroke=INK, sw=2, rx=4)
    body += _txt(bx, by, "load", col="#FFFFFF", size=13)
    # effort arrow up the slope
    body += _line(bx + 34, by - 8, bx + 96, by - 40, col=GREEN, w=5,
                  marker="arrowR")
    body += _txt(bx + 120, by - 44, "effort", col=GREEN, size=14,
                 anchor="start")
    body += _txt(vw / 2, 34, "An inclined plane (ramp)", col=INK, size=17)
    body += _txt(vw / 2, vh - 16,
                 "A small effort along a long slope raises a heavy load",
                 col=MUT, size=13, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def wedge_and_screw(key):
    """Two applications of the inclined plane: a wedge and a screw."""
    vw, vh = 700, 380
    # --- wedge (axe splitting a log) ---
    body = _txt(180, 40, "A wedge", col=INK, size=16)
    body += _rect(90, 150, 180, 90, fill=WOOD, stroke=INK, sw=2, rx=4)
    body += _line(180, 150, 180, 240, col="#7A5230", w=3, dash="6,5")
    # wedge blade
    body += _poly([(160, 70), (200, 70), (180, 150)], fill=SILVER, stroke=INK,
                  sw=2)
    body += _line(140, 130, 120, 150, col=RED, w=3, marker="arrowR")
    body += _line(220, 130, 240, 150, col=RED, w=3, marker="arrowR")
    body += _txt(180, 280, "splits the wood apart", col=MUT, size=13,
                 bold=False)
    # --- screw (inclined plane wrapped round a rod) ---
    sx = 520
    body += _txt(sx, 40, "A screw", col=INK, size=16)
    body += _rect(sx - 26, 90, 52, 190, fill="#D9DEE6", stroke=INK, sw=2, rx=4)
    for i in range(7):
        y = 100 + i * 24
        body += _line(sx - 26, y, sx + 26, y + 12, col=INK, w=3)
    body += _poly([(sx - 26, 90), (sx + 26, 90), (sx, 66)], fill=MUT,
                  stroke=INK, sw=2)
    body += _txt(sx, 300, "a ramp wound round a rod", col=MUT, size=13,
                 bold=False)
    body += _txt(vw / 2, vh - 14, "Both are forms of the inclined plane",
                 col=INK, size=13)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def wheel_and_axle(key):
    """A large wheel fixed to a thin axle: turning the wheel turns the axle."""
    vw, vh = 520, 460
    cx, cy = vw / 2, 210
    # large wheel
    body = _circle(cx, cy, 130, fill="#EDF1F6", stroke=INK, sw=3)
    body += _circle(cx, cy, 118, fill="none", stroke=MUT, sw=1.5)
    # axle (small central drum)
    body += _circle(cx, cy, 34, fill="#C9B79C", stroke=INK, sw=3)
    body += _circle(cx, cy, 6, fill=INK, stroke="none")
    # spokes
    for ang in range(0, 360, 45):
        body += _line(cx + 34 * math.cos(math.radians(ang)),
                      cy + 34 * math.sin(math.radians(ang)),
                      cx + 130 * math.cos(math.radians(ang)),
                      cy + 130 * math.sin(math.radians(ang)),
                      col=MUT, w=2)
    # effort rope on the wheel rim (right)
    body += _line(cx + 130, cy, cx + 130, cy + 150, col=GREEN, w=4)
    body += _line(cx + 130, cy + 110, cx + 130, cy + 150, col=GREEN, w=4,
                  marker="arrowR")
    body += _txt(cx + 130, cy + 175, "effort", col=GREEN, size=14)
    # load rope on the axle (left)
    body += _line(cx - 34, cy, cx - 34, cy + 150, col=RED, w=4)
    body += _rect(cx - 60, cy + 150, 52, 44, fill=IRON, stroke=INK, sw=2, rx=4)
    body += _txt(cx - 34, cy + 176, "load", col="#FFFFFF", size=13)
    body += _txt(cx, 36, "A wheel and axle", col=INK, size=17)
    body += _txt(cx + 90, cy - 90, "wheel", col=INK, size=13)
    body += _txt(cx, cy - 2, "axle", col=INK, size=12)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


# ===========================================================================
# Work and Energy
# ===========================================================================
def potential_kinetic(key):
    """Potential energy (stored) turning into kinetic energy (of motion)."""
    vw, vh = 720, 400
    # --- left: stone held high = potential energy ---
    body = _txt(180, 40, "Potential energy", col=PURPLE, size=16)
    body += _line(70, 320, 300, 320, col=INK, w=3)
    body += _rect(90, 90, 26, 26, fill=IRON, stroke=INK, sw=2, rx=3)
    body += _line(103, 90, 103, 60, col="#B0761F", w=4)
    body += _line(70, 60, 150, 60, col="#B0761F", w=6)
    body += _line(150, 116, 150, 320, col=MUT, w=2, dash="5,5")
    body += _txt(170, 220, "height", col=MUT, size=13, anchor="start")
    body += _txt(180, 350, "stored because of its position", col=MUT, size=12,
                 bold=False)
    # arrow across
    body += _line(320, 205, 400, 205, col=ORANGE, w=5, marker="arrowR")
    body += _txt(360, 190, "falls", col=ORANGE, size=13)
    # --- right: stone falling = kinetic energy ---
    body += _txt(560, 40, "Kinetic energy", col=TEAL, size=16)
    body += _line(430, 320, 660, 320, col=INK, w=3)
    body += _rect(535, 200, 26, 26, fill=IRON, stroke=INK, sw=2, rx=3)
    body += _line(548, 175, 548, 145, col=TEAL, w=4, marker="arrow")
    for dx in (-20, 20):
        body += _line(548 + dx, 250, 548 + dx, 285, col=MUT, w=2, dash="4,4")
    body += _txt(560, 350, "energy of its motion", col=MUT, size=12,
                 bold=False)
    body += _txt(vw / 2, vh - 12,
                 "Mechanical energy = potential energy + kinetic energy",
                 col=INK, size=13)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def energy_forms(key):
    """Six forms of energy as labelled icons."""
    vw, vh = 720, 400
    body = _txt(vw / 2, 34, "Some forms of energy", col=INK, size=18)
    cells = [
        (150, 130, GOLD, "Light"),
        (360, 130, RED, "Heat"),
        (570, 130, PURPLE, "Sound"),
        (150, 280, GREEN, "Chemical"),
        (360, 280, BLUE, "Electrical"),
        (570, 280, TEAL, "Mechanical"),
    ]
    for cx, cy, col, label in cells:
        body += _circle(cx, cy, 44, fill="#FFFFFF", stroke=col, sw=4)
        if label == "Light":
            body += _circle(cx, cy, 16, fill=GOLD, stroke=ORANGE, sw=2)
            for ang in range(0, 360, 45):
                dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
                body += _line(cx + 22 * dx, cy + 22 * dy, cx + 34 * dx,
                              cy + 34 * dy, col=ORANGE, w=3)
        elif label == "Heat":
            body += _poly([(cx, cy + 22), (cx - 16, cy), (cx - 6, cy - 20),
                           (cx + 4, cy - 4), (cx + 14, cy - 22),
                           (cx + 16, cy + 6)], fill=FLAME, stroke="none")
        elif label == "Sound":
            for r in (14, 24, 34):
                body += f'<path d="M {cx-4} {cy-r} A {r} {r} 0 0 1 {cx-4} {cy+r}" fill="none" stroke="{PURPLE}" stroke-width="3"/>'
        elif label == "Chemical":
            body += _rect(cx - 16, cy - 18, 32, 36, fill=GREEN, stroke=INK,
                          sw=2, rx=4)
            body += _rect(cx - 8, cy - 26, 16, 8, fill=INK, stroke="none")
        elif label == "Electrical":
            body += _poly([(cx - 4, cy - 22), (cx - 16, cy + 4), (cx - 2, cy + 4),
                           (cx + 4, cy + 22), (cx + 16, cy - 4), (cx + 2, cy - 4)],
                          fill=GOLD, stroke=INK, sw=1.5)
        else:  # Mechanical
            body += _circle(cx, cy, 20, fill="none", stroke=TEAL, sw=4)
            for ang in range(0, 360, 60):
                dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
                body += _rect(cx + 20 * dx - 3, cy + 20 * dy - 3, 6, 6,
                              fill=TEAL, stroke="none")
        body += _txt(cx, cy + 66, label, col=INK, size=14)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def energy_conversion(key):
    """Hydro chain: stored water -> falling water -> turbine -> electricity."""
    vw, vh = 760, 320
    y = 150

    def box(cx, col, l1, l2):
        s = _rect(cx - 70, y - 46, 140, 92, fill="#FFFFFF", stroke=col, sw=4,
                  rx=10)
        s += _txt(cx, y - 6, l1, col=col, size=14)
        s += _txt(cx, y + 16, l2, col=MUT, size=12, bold=False)
        return s

    body = _txt(vw / 2, 36, "Energy changes from one form to another",
                col=INK, size=17)
    body += box(110, PURPLE, "Potential", "water stored high")
    body += box(320, TEAL, "Kinetic", "water falling")
    body += box(530, ORANGE, "Mechanical", "turbine turns")
    body += box(700, BLUE, "Electrical", "at the generator")
    for x in (185, 395, 605):
        body += _line(x, y, x + 40, y, col=INK, w=3, marker="arrow")
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


# ===========================================================================
# Sound
# ===========================================================================
def vibrating_sources(key):
    """Sound comes from vibration: tuning fork, drum, stretched string."""
    vw, vh = 720, 360
    body = _txt(vw / 2, 34, "Sound is produced by vibrations", col=INK,
                size=18)
    # tuning fork
    body += _rect(120, 120, 16, 90, fill=SILVER, stroke=INK, sw=2, rx=3)
    body += _rect(100, 90, 16, 90, fill=SILVER, stroke=INK, sw=2, rx=3)
    body += _rect(90, 200, 56, 20, fill=MUT, stroke=INK, sw=2, rx=3)
    body += _line(90, 110, 74, 110, col=RED, w=2, marker="arrowR")
    body += _line(142, 110, 158, 110, col=RED, w=2, marker="arrowR")
    body += _txt(118, 260, "tuning fork", col=INK, size=14)
    # drum
    dcx = 360
    body += _ellipse(dcx, 120, 60, 18, fill="#F1E4CE", stroke=INK, sw=2)
    body += _rect(dcx - 60, 120, 120, 90, fill="#D9A24B", stroke=INK, sw=2)
    body += _ellipse(dcx, 210, 60, 18, fill="#C98A34", stroke=INK, sw=2)
    body += _circle(dcx, 90, 6, fill=INK, stroke="none")
    body += _line(dcx, 96, dcx, 112, col=RED, w=2, marker="arrowR")
    body += _txt(dcx, 260, "drum", col=INK, size=14)
    # stretched string
    scx = 600
    body += _line(scx - 60, 110, scx + 60, 110, col="#8A5A20", w=4)
    body += f'<path d="M {scx-60} 150 Q {scx} 120 {scx+60} 150" fill="none" stroke="{PURPLE}" stroke-width="3"/>'
    body += f'<path d="M {scx-60} 150 Q {scx} 180 {scx+60} 150" fill="none" stroke="{PURPLE}" stroke-width="3" stroke-dasharray="5,4"/>'
    body += _txt(scx, 260, "stretched string", col=INK, size=14)
    body += _txt(vw / 2, vh - 16, "As long as it vibrates, we hear the sound",
                col=MUT, size=13, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def sound_needs_medium(key):
    """Bell-jar experiment: as air is pumped out, the bell can't be heard."""
    vw, vh = 520, 480
    cx = vw / 2
    # base + pump
    body = _rect(cx - 140, 380, 280, 30, fill="#C9CED6", stroke=INK, sw=2, rx=4)
    # glass jar (bell jar)
    body += f'<path d="M {cx-110} 380 L {cx-110} 150 Q {cx-110} 90 {cx} 90 Q {cx+110} 90 {cx+110} 150 L {cx+110} 380 Z" fill="{GLASS}" fill-opacity="0.35" stroke="{INK}" stroke-width="3"/>'
    # electric bell hanging inside
    body += _line(cx, 110, cx, 210, col=MUT, w=3)
    body += f'<path d="M {cx-40} 300 Q {cx} 200 {cx+40} 300 Z" fill="#B9873A" stroke="{INK}" stroke-width="2"/>'
    body += _circle(cx, 312, 10, fill="#8A5A20", stroke=INK, sw=2)
    body += _txt(cx, 350, "electric bell", col=INK, size=13)
    # vacuum pump pipe
    body += _line(cx + 110, 360, cx + 175, 360, col=INK, w=6)
    body += _line(cx + 175, 360, cx + 175, 420, col=INK, w=6)
    body += _txt(cx + 175, 445, "to pump", col=MUT, size=12)
    # arrows showing air removed
    body += _line(cx + 120, 340, cx + 165, 340, col=RED, w=3, marker="arrowR")
    body += _txt(vw / 2, 40, "Sound needs a medium", col=INK, size=17)
    body += _txt(vw / 2, 66, "Remove the air and the ringing fades away",
                col=MUT, size=13, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


# ===========================================================================
# Light and the Formation of Shadows
# ===========================================================================
def transparent_opaque(key):
    """Transparent, translucent and opaque materials in front of a light."""
    vw, vh = 760, 380
    body = _txt(vw / 2, 34, "How materials let light through", col=INK,
                size=18)

    def panel(cx, title, sub, opacity, blocked):
        s = _txt(cx, 90, title, col=INK, size=15)
        # light source
        s += _circle(cx - 120, 200, 14, fill=GOLD, stroke=ORANGE, sw=2)
        # material slab
        s += (f'<rect x="{cx - 20}" y="140" width="20" height="120" '
              f'fill="{GLASS}" fill-opacity="{opacity}" stroke="{INK}" '
              f'stroke-width="2"/>')
        # incoming rays
        for dy in (-34, 0, 34):
            s += _line(cx - 106, 200, cx - 20, 200 + dy * 0.4, col=GOLD, w=2)
        # outgoing rays (fewer / none depending on material)
        if blocked == 0:
            for dy in (-34, 0, 34):
                s += _line(cx, 200 + dy * 0.4, cx + 90, 200 + dy * 0.7,
                           col=GOLD, w=2)
        elif blocked == 1:
            s += _line(cx, 200, cx + 90, 200, col=GOLD, w=2, dash="5,4")
        else:
            # opaque -> shadow on a screen
            s += _rect(cx + 78, 150, 10, 100, fill="#3A3F4A", stroke="none")
        s += _txt(cx, 300, sub, col=MUT, size=12, bold=False)
        return s

    body += panel(180, "Transparent", "light passes fully (clear glass)",
                  0.2, 0)
    body += panel(400, "Translucent", "light passes partly (frosted glass)",
                  0.55, 1)
    body += panel(620, "Opaque", "light is blocked → a shadow (wood)",
                  0.95, 2)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


# ===========================================================================
# Fun with Magnets
# ===========================================================================
def making_a_magnet(key):
    """Single-touch method: stroke an iron bar with one pole of a magnet."""
    vw, vh = 620, 360
    body = _txt(vw / 2, 36, "Making a magnet by stroking", col=INK, size=18)
    # iron bar
    body += _rect(120, 210, 360, 40, fill=IRON, stroke=INK, sw=2, rx=4)
    body += _txt(300, 234, "iron bar", col="#FFFFFF", size=14)
    # bar magnet held above, moving left-to-right (shown mid-stroke)
    mx = 300
    body += _rect(mx - 60, 130, 60, 34, fill=RED, stroke=INK, sw=2, rx=3)
    body += _rect(mx, 130, 60, 34, fill=BLUE, stroke=INK, sw=2, rx=3)
    body += _txt(mx - 30, 152, "N", col="#FFFFFF", size=16)
    body += _txt(mx + 30, 152, "S", col="#FFFFFF", size=16)
    # stroking-direction arrow
    body += _line(150, 185, 450, 185, col=GREEN, w=4, marker="arrowR")
    body += _txt(300, 172, "stroke the same way, again and again", col=GREEN,
                 size=13)
    # lift-and-return dashed arrow
    body += f'<path d="M 450 120 Q 300 70 150 120" fill="none" stroke="{MUT}" stroke-width="2" stroke-dasharray="6,5"/>'
    body += _txt(300, 78, "lift and bring back each time", col=MUT, size=12,
                bold=False)
    body += _txt(vw / 2, vh - 16, "The bar slowly becomes a magnet", col=MUT,
                size=13, bold=False)
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


def magnetic_nonmagnetic(key):
    """A magnet attracts magnetic materials but not non-magnetic ones."""
    vw, vh = 720, 400
    body = _txt(vw / 2, 34, "Magnetic and non-magnetic materials", col=INK,
                size=18)
    # magnet in the centre
    cx = vw / 2
    body += _rect(cx - 40, 170, 40, 60, fill=RED, stroke=INK, sw=2, rx=4)
    body += _rect(cx, 170, 40, 60, fill=BLUE, stroke=INK, sw=2, rx=4)
    body += _txt(cx - 20, 205, "N", col="#FFFFFF", size=16)
    body += _txt(cx + 20, 205, "S", col="#FFFFFF", size=16)
    # attracted group (left) with pull arrows
    body += _txt(150, 96, "Attracted", col=GREEN, size=15)
    body += _txt(150, 116, "(magnetic)", col=MUT, size=12, bold=False)
    for i, name in enumerate(("iron nail", "steel pin", "nickel coin")):
        y = 160 + i * 46
        body += _rect(90, y - 16, 120, 30, fill="#DCE2EA", stroke=INK, sw=2,
                      rx=6)
        body += _txt(150, y + 4, name, col=INK, size=13)
        body += _line(214, y, cx - 52, 200, col=GREEN, w=2, marker="arrowR")
    # not attracted group (right)
    body += _txt(590, 96, "Not attracted", col=RED, size=15)
    body += _txt(590, 116, "(non-magnetic)", col=MUT, size=12, bold=False)
    for i, name in enumerate(("plastic", "wood", "copper")):
        y = 160 + i * 46
        body += _rect(530, y - 16, 120, 30, fill="#F1E9DC", stroke=INK, sw=2,
                      rx=6)
        body += _txt(590, y + 4, name, col=INK, size=13)
        body += _line(526, y, cx + 52, 200, col=RED, w=2, dash="5,4")
    return _render(key, _svg(body, vw, vh, bg="#FFFFFF"), vw, vh)


# ===========================================================================
# The Universe
# ===========================================================================
def solar_system(key):
    """The Sun and the eight planets in order (schematic, not to scale)."""
    vw, vh = 820, 340
    body = _rect(0, 0, vw, vh, fill=SKY, stroke="none")
    body += _txt(vw / 2, 34, "The Solar System (not to scale)",
                col="#FFFFFF", size=18)
    # Sun at the left
    sx, sy = 70, 190
    body += _circle(sx, sy, 46, fill=GOLD, stroke=ORANGE, sw=3)
    for ang in range(0, 360, 30):
        dx, dy = math.cos(math.radians(ang)), math.sin(math.radians(ang))
        body += _line(sx + 48 * dx, sy + 48 * dy, sx + 62 * dx, sy + 62 * dy,
                      col=ORANGE, w=2)
    body += _txt(sx, sy + 84, "Sun", col="#FFF6CC", size=14)
    # eight planets
    planets = [
        ("Mercury", 175, 7, "#B7A98F"),
        ("Venus", 235, 11, "#E6C07A"),
        ("Earth", 305, 12, "#5B8DEF"),
        ("Mars", 375, 9, "#C1502E"),
        ("Jupiter", 470, 26, "#D9A566"),
        ("Saturn", 585, 22, "#E4CE92"),
        ("Uranus", 685, 16, "#8FD0DB"),
        ("Neptune", 775, 15, "#4A6FE0"),
    ]
    for name, px, pr, col in planets:
        body += _circle(px, 190, pr, fill=col, stroke="none")
        if name == "Saturn":
            body += _ellipse(px, 190, pr + 12, 5, fill="none", stroke="#CBB88A",
                             sw=2)
        # alternate label height to avoid crowding
        ly = 190 - pr - 14 if planets.index((name, px, pr, col)) % 2 == 0 \
            else 190 + pr + 22
        body += _txt(px, ly, name, col="#D8E2F0", size=12, bold=False)
    return _render(key, _svg(body, vw, vh, bg=SKY), vw, vh)


if __name__ == "__main__":
    # smoke test — render every figure
    for fn in (lever_types, pulley, inclined_plane, wedge_and_screw,
               wheel_and_axle, potential_kinetic, energy_forms,
               energy_conversion, vibrating_sources, sound_needs_medium,
               transparent_opaque, making_a_magnet, magnetic_nonmagnetic,
               solar_system):
        p = fn(f"test_{fn.__name__}")
        print(f"{fn.__name__:24s} -> {p}")
