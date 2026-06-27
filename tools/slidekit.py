"""
slidekit - extra slide layouts that build on the shared engine.Builder without
editing engine.py. Two things the brief asked for:

  1. ICONS on feature cards: SK.cards() draws the same card grid as
     engine.cards() but puts a small white pictogram inside each coloured
     badge. Icons are chosen per card (explicit list, or auto-guessed from the
     card text), so existing decks gain icons with almost no edits.

  2. MIRRORED QUIZ ANSWER SLIDES: SK.quiz() emits the question slide AND an
     answer slide that is identical to it (same question, same four options) -
     the only difference is the correct option is shown selected (highlighted
     green with a tick), followed by a short "Why".

Everything is drawn with the Builder's own primitives (b._slide, b._box,
b._text, b._pic, b._chrome, b._next, b._notes) so the look matches the rest of
the deck exactly.
"""
import os
import math
import cairosvg

from engine import C, ACCENTS, LABEL_FONT
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "build", "img")
os.makedirs(IMG_DIR, exist_ok=True)


def _c(a):
    return round(50 + 30 * math.cos(math.radians(a)), 2)


def _s(a):
    return round(50 + 30 * math.sin(math.radians(a)), 2)


def _cr(a, r):
    return round(50 + r * math.cos(math.radians(a)), 2)


def _sr(a, r):
    return round(50 + r * math.sin(math.radians(a)), 2)


# ---------------------------------------------------------------------------
# Icon library - white line/solid pictograms on a transparent background.
# Each entry is the inner SVG for a 0..100 viewBox; drawn in white.
# ---------------------------------------------------------------------------
_W = '#FFFFFF'
ICONS = {
    "gear": ('<circle cx="50" cy="50" r="20" fill="none" stroke="%s" '
             'stroke-width="9"/>' % _W
             + "".join(
                 f'<rect x="46" y="6" width="8" height="16" fill="{_W}" '
                 f'transform="rotate({a} 50 50)"/>' for a in range(0, 360, 45))
             + f'<circle cx="50" cy="50" r="7" fill="{_W}"/>'),
    "balance": (f'<line x1="50" y1="18" x2="50" y2="78" stroke="{_W}" '
                f'stroke-width="8"/><line x1="22" y1="30" x2="78" y2="30" '
                f'stroke="{_W}" stroke-width="8"/>'
                f'<path d="M14 30 L30 30 L22 50 Z" fill="{_W}"/>'
                f'<path d="M70 30 L86 30 L78 50 Z" fill="{_W}"/>'
                f'<rect x="34" y="78" width="32" height="8" fill="{_W}"/>'),
    "lever": (f'<line x1="16" y1="48" x2="84" y2="62" stroke="{_W}" '
              f'stroke-width="9" stroke-linecap="round"/>'
              f'<path d="M44 86 L60 86 L52 60 Z" fill="{_W}"/>'),
    "pulley": (f'<circle cx="50" cy="40" r="20" fill="none" stroke="{_W}" '
               f'stroke-width="8"/><circle cx="50" cy="40" r="5" fill="{_W}"/>'
               f'<line x1="30" y1="40" x2="30" y2="84" stroke="{_W}" '
               f'stroke-width="7"/><line x1="70" y1="40" x2="70" y2="80" '
               f'stroke="{_W}" stroke-width="7"/>'
               f'<rect x="22" y="84" width="16" height="12" fill="{_W}"/>'),
    "wheel": (f'<circle cx="50" cy="50" r="30" fill="none" stroke="{_W}" '
              f'stroke-width="8"/><circle cx="50" cy="50" r="7" fill="{_W}"/>'
              + "".join(f'<line x1="50" y1="50" x2="{_c(a)}" '
                        f'y2="{_s(a)}" stroke="{_W}" '
                        f'stroke-width="5"/>' for a in range(0, 360, 60))),
    "ramp": (f'<path d="M14 82 L86 82 L86 30 Z" fill="none" stroke="{_W}" '
             f'stroke-width="8" stroke-linejoin="round"/>'),
    "wedge": (f'<path d="M30 16 L70 16 L50 86 Z" fill="{_W}"/>'),
    "screw": (f'<line x1="50" y1="14" x2="50" y2="86" stroke="{_W}" '
              f'stroke-width="9"/>'
              + "".join(f'<line x1="38" y1="{y}" x2="62" y2="{y-8}" '
                        f'stroke="{_W}" stroke-width="5"/>'
                        for y in range(34, 86, 12))),
    "bulb": (f'<circle cx="50" cy="42" r="24" fill="none" stroke="{_W}" '
             f'stroke-width="8"/><rect x="40" y="64" width="20" height="14" '
             f'fill="{_W}"/><line x1="42" y1="84" x2="58" y2="84" '
             f'stroke="{_W}" stroke-width="7"/>'),
    "sun": (f'<circle cx="50" cy="50" r="18" fill="{_W}"/>'
            + "".join(f'<line x1="{_cr(a, 24)}" '
                      f'y1="{_sr(a, 24)}" '
                      f'x2="{_cr(a, 34)}" '
                      f'y2="{_sr(a, 34)}" stroke="{_W}" '
                      f'stroke-width="7" stroke-linecap="round"/>'
                      for a in range(0, 360, 45))),
    "eye": (f'<path d="M12 50 Q50 18 88 50 Q50 82 12 50 Z" fill="none" '
            f'stroke="{_W}" stroke-width="8"/>'
            f'<circle cx="50" cy="50" r="11" fill="{_W}"/>'),
    "shadow": (f'<circle cx="42" cy="40" r="18" fill="{_W}"/>'
               f'<ellipse cx="60" cy="82" rx="30" ry="8" fill="{_W}" '
               f'opacity="0.65"/>'),
    "camera": (f'<rect x="16" y="32" width="68" height="46" rx="8" '
               f'fill="none" stroke="{_W}" stroke-width="7"/>'
               f'<rect x="38" y="24" width="24" height="12" fill="{_W}"/>'
               f'<circle cx="50" cy="55" r="13" fill="none" stroke="{_W}" '
               f'stroke-width="7"/>'),
    "moon": (f'<path d="M64 18 A34 34 0 1 0 64 82 A26 26 0 1 1 64 18 Z" '
             f'fill="{_W}"/>'),
    "eclipse": (f'<circle cx="44" cy="50" r="26" fill="{_W}"/>'
                f'<circle cx="60" cy="50" r="26" fill="none" stroke="{_W}" '
                f'stroke-width="7"/>'),
    "magnet": (f'<path d="M26 24 L26 56 A24 24 0 0 0 74 56 L74 24" '
               f'fill="none" stroke="{_W}" stroke-width="12"/>'
               f'<rect x="20" y="22" width="12" height="14" fill="{_W}"/>'
               f'<rect x="68" y="22" width="12" height="14" fill="{_W}"/>'),
    "compass": (f'<circle cx="50" cy="50" r="32" fill="none" stroke="{_W}" '
                f'stroke-width="7"/><path d="M50 26 L58 50 L50 74 L42 50 Z" '
                f'fill="{_W}"/>'),
    "bolt": (f'<path d="M56 12 L28 54 L46 54 L40 88 L72 42 L52 42 Z" '
             f'fill="{_W}"/>'),
    "battery": (f'<rect x="18" y="34" width="56" height="32" rx="4" '
                f'fill="none" stroke="{_W}" stroke-width="7"/>'
                f'<rect x="74" y="42" width="8" height="16" fill="{_W}"/>'
                f'<line x1="34" y1="50" x2="44" y2="50" stroke="{_W}" '
                f'stroke-width="6"/><line x1="39" y1="45" x2="39" y2="55" '
                f'stroke="{_W}" stroke-width="6"/>'
                f'<line x1="54" y1="50" x2="64" y2="50" stroke="{_W}" '
                f'stroke-width="6"/>'),
    "circuit": (f'<rect x="20" y="28" width="60" height="44" rx="6" '
                f'fill="none" stroke="{_W}" stroke-width="7"/>'
                f'<rect x="42" y="22" width="16" height="12" fill="{C["bg_light"]}"/>'
                f'<circle cx="50" cy="28" r="6" fill="{_W}"/>'),
    "plug": (f'<line x1="40" y1="14" x2="40" y2="40" stroke="{_W}" '
             f'stroke-width="7"/><line x1="60" y1="14" x2="60" y2="40" '
             f'stroke="{_W}" stroke-width="7"/>'
             f'<rect x="30" y="40" width="40" height="26" rx="6" fill="{_W}"/>'
             f'<line x1="50" y1="66" x2="50" y2="86" stroke="{_W}" '
             f'stroke-width="7"/>'),
    "bell": (f'<path d="M30 66 Q30 30 50 28 Q70 30 70 66 Z" fill="none" '
             f'stroke="{_W}" stroke-width="7" stroke-linejoin="round"/>'
             f'<line x1="24" y1="66" x2="76" y2="66" stroke="{_W}" '
             f'stroke-width="7"/><circle cx="50" cy="74" r="6" fill="{_W}"/>'
             f'<circle cx="50" cy="22" r="5" fill="{_W}"/>'),
    "thermometer": (f'<rect x="42" y="16" width="16" height="50" rx="8" '
                    f'fill="none" stroke="{_W}" stroke-width="7"/>'
                    f'<circle cx="50" cy="74" r="14" fill="{_W}"/>'
                    f'<rect x="46" y="40" width="8" height="34" fill="{_W}"/>'),
    "fire": (f'<path d="M50 12 C66 34 74 40 70 58 A20 20 0 1 1 30 58 '
             f'C28 46 36 44 40 36 C44 46 50 44 50 34 C50 28 48 20 50 12 Z" '
             f'fill="{_W}"/>'),
    "snow": ("".join(f'<line x1="50" y1="14" x2="50" y2="86" stroke="{_W}" '
                     f'stroke-width="7" transform="rotate({a} 50 50)"/>'
                     for a in (0, 60, 120))),
    "wave": (f'<path d="M12 50 Q26 22 40 50 T68 50 T96 50" fill="none" '
             f'stroke="{_W}" stroke-width="8" stroke-linecap="round"/>'),
    "ear": (f'<path d="M36 84 Q30 64 34 50 A18 18 0 1 1 64 44 '
            f'Q60 56 52 58 Q46 60 48 70" fill="none" stroke="{_W}" '
            f'stroke-width="8" stroke-linecap="round"/>'),
    "ruler": (f'<rect x="18" y="34" width="64" height="32" rx="3" '
              f'fill="none" stroke="{_W}" stroke-width="7"/>'
              + "".join(f'<line x1="{x}" y1="34" x2="{x}" y2="48" '
                        f'stroke="{_W}" stroke-width="5"/>'
                        for x in range(30, 80, 12))),
    "force": (f'<line x1="18" y1="50" x2="74" y2="50" stroke="{_W}" '
              f'stroke-width="9" stroke-linecap="round"/>'
              f'<path d="M68 36 L88 50 L68 64 Z" fill="{_W}"/>'),
    "atom": (f'<circle cx="50" cy="50" r="7" fill="{_W}"/>'
             f'<ellipse cx="50" cy="50" rx="34" ry="14" fill="none" '
             f'stroke="{_W}" stroke-width="6"/>'
             f'<ellipse cx="50" cy="50" rx="34" ry="14" fill="none" '
             f'stroke="{_W}" stroke-width="6" transform="rotate(60 50 50)"/>'
             f'<ellipse cx="50" cy="50" rx="34" ry="14" fill="none" '
             f'stroke="{_W}" stroke-width="6" transform="rotate(120 50 50)"/>'),
    "drop": (f'<path d="M50 14 C70 44 74 56 64 70 A18 18 0 1 1 36 70 '
             f'C26 56 30 44 50 14 Z" fill="{_W}"/>'),
    "star": (f'<path d="M50 14 L60 40 L88 40 L65 57 L74 84 L50 67 L26 84 '
             f'L35 57 L12 40 L40 40 Z" fill="{_W}"/>'),
    "check": (f'<path d="M22 52 L42 72 L80 28" fill="none" stroke="{_W}" '
              f'stroke-width="11" stroke-linecap="round" '
              f'stroke-linejoin="round"/>'),
    "book": (f'<path d="M50 28 Q34 20 18 26 L18 74 Q34 68 50 76 '
             f'Q66 68 82 74 L82 26 Q66 20 50 28 Z" fill="none" '
             f'stroke="{_W}" stroke-width="7" stroke-linejoin="round"/>'
             f'<line x1="50" y1="28" x2="50" y2="76" stroke="{_W}" '
             f'stroke-width="6"/>'),
    "target": (f'<circle cx="50" cy="50" r="30" fill="none" stroke="{_W}" '
               f'stroke-width="7"/><circle cx="50" cy="50" r="16" '
               f'fill="none" stroke="{_W}" stroke-width="7"/>'
               f'<circle cx="50" cy="50" r="4" fill="{_W}"/>'),
    "gauge": (f'<path d="M20 70 A34 34 0 0 1 80 70" fill="none" '
              f'stroke="{_W}" stroke-width="8" stroke-linecap="round"/>'
              f'<line x1="50" y1="70" x2="68" y2="44" stroke="{_W}" '
              f'stroke-width="7" stroke-linecap="round"/>'
              f'<circle cx="50" cy="70" r="6" fill="{_W}"/>'),
    "cog": None,  # alias set below
    "dot": (f'<circle cx="50" cy="50" r="16" fill="{_W}"/>'),
}

# aliases -> existing icons
_ALIAS = {
    "cog": "gear", "machine": "gear", "efficiency": "gauge", "speed": "gauge",
    "energy": "bolt", "electric": "bolt", "current": "bolt", "power": "bolt",
    "light": "bulb", "lamp": "bulb", "source": "bulb", "idea": "bulb",
    "rays": "sun", "solar": "sun", "lunar": "moon", "vision": "eye",
    "see": "eye", "image": "camera", "pinhole": "camera", "umbra": "shadow",
    "heat": "fire", "hot": "fire", "boil": "fire", "cold": "snow",
    "expansion": "thermometer", "temperature": "thermometer",
    "sound": "wave", "echo": "wave", "frequency": "wave", "vibration": "wave",
    "hearing": "ear", "magnetic": "magnet", "field": "magnet",
    "electromagnet": "magnet", "earth": "compass", "direction": "compass",
    "circuit": "circuit", "cell": "battery", "fuse": "bolt", "wire": "plug",
    "safety": "plug", "work": "force", "effort": "force", "load": "force",
    "motion": "force", "measure": "ruler", "unit": "ruler", "length": "ruler",
    "water": "drop", "evaporation": "drop", "density": "drop",
    "uses": "star", "use": "star", "example": "star", "fact": "star",
    "rule": "book", "law": "book", "principle": "book", "definition": "book",
    "term": "book", "kind": "book", "objective": "target", "goal": "target",
    "incline": "ramp", "ramp": "ramp", "screw": "screw", "wedge": "wedge",
    "lever": "lever", "pulley": "pulley", "wheel": "wheel", "care": "check",
    "tip": "check", "correct": "check", "atom": "atom", "molecule": "atom",
    "state": "atom", "convection": "fire", "conduction": "thermometer",
    "radiation": "sun", "prism": "eclipse", "dispersion": "eclipse",
    "colour": "eclipse", "color": "eclipse", "mirror": "eye",
    "reflection": "eye", "refraction": "drop", "function": "gear",
    "transmission": "bolt", "household": "plug", "appliance": "plug",
}
ICONS["cog"] = ICONS["gear"]

_KEYWORDS = sorted(_ALIAS.keys(), key=len, reverse=True)


def _icon_name(text):
    """Guess the best icon name from a piece of card text."""
    t = (text or "").lower()
    for kw in _KEYWORDS:
        if kw in t:
            return _ALIAS[kw]
    if t in ICONS:
        return t
    return "star"


def icon_png(name):
    """Render (cached) a white pictogram PNG on a transparent background."""
    name = _ALIAS.get(name, name)
    if name not in ICONS:
        name = "star"
    path = os.path.abspath(os.path.join(IMG_DIR, f"icon_{name}.png"))
    if not os.path.exists(path):
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
               f'{ICONS[name]}</svg>')
        cairosvg.svg2png(bytestring=svg.encode("utf-8"), write_to=path,
                         output_width=120, output_height=120)
    return path


# ---------------------------------------------------------------------------
# 1. Feature cards with icons (same geometry as engine.cards)
# ---------------------------------------------------------------------------
def cards(b, badge, title, items, notes="", icons=None):
    s = b._slide(C["bg_light"])
    n = b._next()
    b._chrome(s, badge, title, b.accent, n)
    cw, chh = 5.7, 1.75
    x0, y0, gx, gy = 0.7, 2.1, 0.4, 0.25
    rows = (len(items) + 1) // 2
    if rows == 1:
        chh = 2.0
    for i, item in enumerate(items):
        head, body = item[0], item[1]
        name = (icons[i] if icons and i < len(icons) and icons[i]
                else _icon_name(f"{head} {body}"))
        r, c = divmod(i, 2)
        x = x0 + c * (cw + gx)
        y = y0 + r * (chh + gy)
        ac = ACCENTS[i % len(ACCENTS)]
        b._box(s, x, y, cw, chh, fill=C["card"], shadow=True,
               shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
        b._box(s, x + 0.35, y + 0.32, 0.55, 0.55, fill=ac,
               shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3)
        b._pic(s, icon_png(name), x + 0.45, y + 0.42, 0.35, 0.35)
        b._text(s, x + 1.1, y + 0.28, cw - 1.4, 0.5,
                [[{"t": head, "size": 17, "bold": True, "color": C["text"]}]])
        b._text(s, x + 1.1, y + 0.82, cw - 1.4, chh - 1.0,
                [[{"t": body, "size": 13.5, "color": C["muted"]}]])
    b._notes(s, notes or f"Teach '{title}'.")
    return s


# ---------------------------------------------------------------------------
# 2. Quiz: question slide + mirrored answer slide
# ---------------------------------------------------------------------------
def _quiz_slide(b, qno, topic, question, options, correct=None, why=None):
    s = b._slide(C["bg_light"])
    n = b._next()
    b._chrome(s, "QUIZ QUESTION", f"Q{qno} - {topic}", b.accent, n)
    b._box(s, 0.7, 2.0, 11.9, 1.7, fill=C["card"], shadow=True,
           shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)
    b._text(s, 1.1, 2.0, 11.1, 1.7,
            [[{"t": question, "size": 19, "bold": True, "color": C["text"]}]],
            anchor=MSO_ANCHOR.MIDDLE)
    labels = "ABCD"
    for i, opt in enumerate(options):
        r, c = divmod(i, 2)
        x = 0.7 + c * (5.85 + 0.2)
        y = 4.1 + r * (0.95 + 0.18)
        chosen = (correct is not None and i == correct)
        if chosen:
            b._box(s, x, y, 5.85, 0.95, fill=C["answer_bg"], line=C["green"],
                   line_w=2.5, shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
            b._box(s, x + 0.3, y + 0.25, 0.45, 0.45, fill=C["green"],
                   shape=MSO_SHAPE.OVAL)
        else:
            b._box(s, x, y, 5.85, 0.95, fill=C["option"],
                   shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
            b._box(s, x + 0.3, y + 0.25, 0.45, 0.45, fill=b.accent,
                   shape=MSO_SHAPE.OVAL)
        b._text(s, x + 0.3, y + 0.25, 0.45, 0.45,
                [[{"t": labels[i], "size": 14, "bold": True,
                   "color": "FFFFFF"}]], align=PP_ALIGN.CENTER,
                anchor=MSO_ANCHOR.MIDDLE)
        b._text(s, x + 0.95, y, 4.2, 0.95,
                [[{"t": opt, "size": 14.5,
                   "bold": chosen, "color": C["text"]}]],
                anchor=MSO_ANCHOR.MIDDLE)
        if chosen:
            b._box(s, x + 5.85 - 0.6, y + 0.27, 0.4, 0.4, fill=C["green"],
                   shape=MSO_SHAPE.OVAL)
            b._text(s, x + 5.85 - 0.6, y + 0.22, 0.4, 0.4,
                    [[{"t": "✓", "size": 16, "bold": True,
                       "color": "FFFFFF"}]], align=PP_ALIGN.CENTER,
                    anchor=MSO_ANCHOR.MIDDLE)
    if correct is not None and why:
        b._box(s, 0.7, 6.32, 11.9, 0.62, fill="EEF2F7",
               shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.1)
        b._text(s, 1.0, 6.32, 11.3, 0.62,
                [[{"t": "Why  ", "size": 12.5, "bold": True,
                   "color": C["green"], "font": LABEL_FONT},
                  {"t": why, "size": 12, "color": C["text"]}]],
                anchor=MSO_ANCHOR.MIDDLE)
    return s


def quiz(b, qno, topic, question, options, correct, why):
    """Emit the question slide, then an identical answer slide with the correct
    option selected and a short Why."""
    _quiz_slide(b, qno, topic, question, options)
    _quiz_slide(b, qno, topic, question, options, correct=correct, why=why)
