"""
Thermal Physics schematics (TN board Unit 3) — authored as SVG and rasterised
to PNG via the helpers in diagrams.py. Nothing is drawn directly on a slide.
"""
import sys, os
sys.path.insert(0, os.path.dirname(__file__))
from diagrams import (_svg, _txt, _line, _arc, _render,
                      INK, MUT, TEAL, ORANGE, PURPLE, RED, BLUE, GLASS, WATER,
                      GREEN, GOLD)
import math as _m


def thermal_equilibrium(key):
    """Two bodies (hot, cold) exchanging heat until they reach equal temp."""
    body = [
        _txt(320, 38, "Heat flows from hot to cold until temperatures equalise",
             INK, 16),
        # hot block
        f'<rect x="70" y="110" width="150" height="150" rx="8" fill="#F2B7A0" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(145, 195, "HOT", RED, 24), _txt(145, 285, "higher temp", MUT, 14),
        # cold block
        f'<rect x="420" y="110" width="150" height="150" rx="8" fill="#BFD8F2" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(495, 195, "COLD", BLUE, 22), _txt(495, 285, "lower temp", MUT, 14),
        # heat arrow from hot to cold
        _line(225, 170, 415, 170, RED, 4, marker="arrowR"),
        _txt(320, 150, "heat", RED, 16),
        # equilibrium note
        _txt(320, 235, "→ same", MUT, 15),
        _txt(320, 255, "temperature", MUT, 15),
        _txt(320, 320, "At thermal equilibrium there is NO net flow of heat",
             MUT, 14),
    ]
    return _render(key, _svg("".join(body), 640, 345), 880, 474)


def expansion_types(key):
    """Linear, superficial and cubical expansion of a solid on heating."""
    body = [_txt(330, 34, "Three kinds of thermal expansion of a solid",
                 INK, 16)]
    # 1. Linear — a rod lengthening
    y = 95
    body += [
        f'<rect x="70" y="{y-12}" width="240" height="24" fill="{GLASS}" '
        f'stroke="{INK}" stroke-width="1.5"/>',
        f'<rect x="310" y="{y-12}" width="40" height="24" fill="#F2C9A0" '
        f'stroke="{INK}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        _line(70, y+30, 310, y+30, MUT, 1.5, marker="arrow"),
        _txt(190, y+48, "L₀", MUT, 13),
        _line(310, y+30, 350, y+30, ORANGE, 1.5, marker="arrowO"),
        _txt(330, y+48, "ΔL", ORANGE, 13),
        _txt(470, y-4, "Linear: length grows", INK, 15, anchor="start"),
        _txt(470, y+18, "ΔL / L₀ = αʟ ΔT", PURPLE, 15,
             anchor="start"),
    ]
    # 2. Superficial — a plate growing in area
    y = 200
    body += [
        f'<rect x="120" y="{y-35}" width="120" height="70" fill="#F2C9A0" '
        f'stroke="{INK}" stroke-width="1.5" stroke-dasharray="4 3"/>',
        f'<rect x="120" y="{y-35}" width="95" height="55" fill="{GLASS}" '
        f'stroke="{INK}" stroke-width="1.5"/>',
        _txt(167, y-4, "A₀", INK, 16),
        _txt(470, y-4, "Superficial: area grows", INK, 15, anchor="start"),
        _txt(470, y+18, "ΔA / A₀ = αᴀ ΔT", PURPLE, 15,
             anchor="start"),
    ]
    # 3. Cubical — a cube growing in volume (drawn as a small 3D box)
    y = 305
    def box(x0, y0, s, d, fill, dash=False):
        da = ' stroke-dasharray="4 3"' if dash else ''
        return (
            f'<rect x="{x0}" y="{y0}" width="{s}" height="{s}" fill="{fill}" '
            f'stroke="{INK}" stroke-width="1.5"{da}/>'
            f'<polygon points="{x0},{y0} {x0+d},{y0-d} {x0+s+d},{y0-d} '
            f'{x0+s},{y0}" fill="{fill}" stroke="{INK}" stroke-width="1.5"{da}/>'
            f'<polygon points="{x0+s},{y0} {x0+s+d},{y0-d} {x0+s+d},{y0+s-d} '
            f'{x0+s},{y0+s}" fill="{fill}" stroke="{INK}" '
            f'stroke-width="1.5"{da}/>')
    body += [
        box(150, y-30, 70, 22, "#F2C9A0", dash=True),
        box(140, y-18, 55, 18, GLASS),
        _txt(168, y+12, "V₀", INK, 15),
        _txt(470, y-4, "Cubical: volume grows", INK, 15, anchor="start"),
        _txt(470, y+18, "ΔV / V₀ = αᴠ ΔT", PURPLE, 15,
             anchor="start"),
    ]
    return _render(key, _svg("".join(body), 660, 360), 900, 491)


def real_apparent_expansion(key):
    """Liquid in a bulb-and-capillary flask showing L1, L2, L3 levels."""
    cx = 250
    body = [
        _txt(330, 34, "Real and apparent expansion of a liquid", INK, 16),
        # capillary tube
        f'<rect x="{cx-10}" y="70" width="20" height="180" fill="{GLASS}" '
        f'stroke="{INK}" stroke-width="2"/>',
        # bulb
        f'<circle cx="{cx}" cy="300" r="55" fill="{GLASS}" stroke="{INK}" '
        f'stroke-width="2"/>',
        # coloured liquid in bulb + lower tube
        f'<circle cx="{cx}" cy="300" r="50" fill="{WATER}"/>',
        f'<rect x="{cx-6}" y="150" width="12" height="150" fill="{WATER}"/>',
        # level marks
        _line(cx-10, 150, cx+70, 150, RED, 1.6, dash="4 3"),
        _txt(cx+95, 154, "L₃  (final, risen)", RED, 13, anchor="start"),
        _line(cx-10, 185, cx+55, 185, ORANGE, 1.6, dash="4 3"),
        _txt(cx+95, 189, "L₁  (start)", ORANGE, 13, anchor="start"),
        _line(cx-10, 215, cx+40, 215, BLUE, 1.6, dash="4 3"),
        _txt(cx+95, 219, "L₂  (first dip)", BLUE, 13, anchor="start"),
        # flame
        f'<path d="M {cx-12} 372 Q {cx} 345 {cx+12} 372 Q {cx} 360 {cx-12} 372 '
        f'Z" fill="{ORANGE}"/>',
        # results
        _txt(cx+95, 250, "Real = L₃ − L₂", INK, 14,
             anchor="start"),
        _txt(cx+95, 274, "Apparent = L₃ − L₁", INK, 14,
             anchor="start"),
        _txt(cx+95, 298, "Real > Apparent", MUT, 13, anchor="start"),
    ]
    return _render(key, _svg("".join(body), 660, 400), 860, 521)


def boyle_graph(key):
    """P versus V curve at constant temperature (a rectangular hyperbola)."""
    ox, oy = 110, 320
    body = [
        _txt(320, 34, "Boyle's law: PV = constant  (T constant)", INK, 16),
        _line(ox, oy, 560, oy, INK, 2, marker="arrow"),
        _line(ox, oy, ox, 70, INK, 2, marker="arrow"),
        _txt(545, oy+28, "Volume V", MUT, 14, anchor="end"),
        _txt(ox-60, 90, "Pressure", MUT, 14), _txt(ox-66, 108, "P", MUT, 14),
    ]
    # hyperbola P = k/V
    pts = []
    k = 9000.0
    for i in range(0, 101):
        V = 60 + i * 4.5            # V from 60..510 in graph units
        P = k / (V - 40)            # shifted so curve sits nicely
        x = ox + (V - 60) * 0.92
        y = oy - P
        if 75 <= y <= oy and x <= 555:
            pts.append(f"{x:.1f},{y:.1f}")
    body.append(f'<polyline points="{" ".join(pts)}" fill="none" '
                f'stroke="{PURPLE}" stroke-width="3"/>')
    body += [
        _txt(420, 150, "PV = constant", PURPLE, 15, anchor="start"),
        _txt(320, 360, "Squeeze the gas (V down) and its pressure rises",
             MUT, 13),
    ]
    return _render(key, _svg("".join(body), 640, 380), 840, 499)


def charles_graph(key):
    """V versus T straight line extrapolating to absolute zero (-273 C)."""
    ox, oy = 150, 300
    body = [
        _txt(330, 34, "Charles's law: V / T = constant  (P constant)", INK,
             16),
        _line(ox, oy, 580, oy, INK, 2, marker="arrow"),
        _line(ox, oy, ox, 70, INK, 2, marker="arrow"),
        _txt(560, oy+28, "Temperature (°C)", MUT, 14, anchor="end"),
        _txt(ox-60, 100, "Volume V", MUT, 14),
        # straight line, extrapolated dashed back to -273
        _line(ox, 250, 540, 95, BLUE, 3),
        _line(95, 290, ox, 250, MUT, 2, dash="5 4"),
        f'<circle cx="95" cy="290" r="4" fill="{RED}"/>',
        _txt(95, oy+24, "−273 °C", RED, 13),
        _txt(95, oy+42, "(0 K)", RED, 11),
        _txt(ox, oy+24, "0 °C", MUT, 12),
        _txt(330, 360, "Extrapolating the line meets the axis at absolute zero",
             MUT, 13),
    ]
    return _render(key, _svg("".join(body), 640, 380), 840, 499)


def gas_piston(key):
    """A gas in a cylinder under a piston — molecules bouncing (pressure)."""
    body = [
        _txt(300, 34, "A gas exerts pressure on its container", INK, 16),
        # cylinder
        f'<rect x="120" y="120" width="220" height="230" fill="#FBEFE0" '
        f'stroke="{INK}" stroke-width="3"/>',
        # piston
        f'<rect x="120" y="120" width="220" height="26" fill="#9AA1AB" '
        f'stroke="{INK}" stroke-width="2"/>',
        f'<rect x="220" y="80" width="20" height="44" fill="#9AA1AB" '
        f'stroke="{INK}" stroke-width="2"/>',
        _txt(230, 70, "piston", MUT, 13),
        _line(230, 60, 230, 78, INK, 3, marker="arrow"),
    ]
    # molecules with little velocity arrows
    import random
    random.seed(7)
    for _ in range(11):
        x = random.randint(150, 310); y = random.randint(165, 330)
        ang = random.uniform(0, 2*_m.pi)
        body.append(f'<circle cx="{x}" cy="{y}" r="6" fill="{ORANGE}"/>')
        body.append(_line(x, y, int(x+18*_m.cos(ang)), int(y+18*_m.sin(ang)),
                          RED, 1.5, marker="arrowR"))
    body.append(_txt(300, 380, "Molecules collide with the walls — these "
                               "collisions create pressure", MUT, 13))
    return _render(key, _svg("".join(body), 600, 400), 760, 507)


if __name__ == "__main__":
    for fn in (thermal_equilibrium, expansion_types, real_apparent_expansion,
               boyle_graph, charles_graph, gas_piston):
        print(fn(f"t_{fn.__name__}"))
