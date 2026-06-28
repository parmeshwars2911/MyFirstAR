"""
Small icon library for card badges (like the reference deck's coloured tiles).

Each icon is a simple SVG glyph rendered to a transparent PNG in a chosen
colour (default white, to sit on a coloured badge). `pick(text)` maps a card
heading to a relevant icon by keyword so decks get sensible icons for free.
"""
import os
import cairosvg

IMG_DIR = os.path.join(os.path.dirname(__file__), "..", "build", "icons")
os.makedirs(IMG_DIR, exist_ok=True)

# Each entry: SVG body drawn in a 0..100 viewBox, using stroke="C"/fill="C"
# placeholders replaced with the chosen colour. Keep them simple line glyphs.
_S = 'stroke="C" stroke-width="7" fill="none" stroke-linecap="round" stroke-linejoin="round"'
_F = 'fill="C"'

ICONS = {
    "bulb": f'<circle cx="50" cy="40" r="22" {_S}/><line x1="42" y1="70" x2="58" y2="70" {_S}/><line x1="44" y1="80" x2="56" y2="80" {_S}/>',
    "eye": f'<path d="M12 50 Q50 20 88 50 Q50 80 12 50 Z" {_S}/><circle cx="50" cy="50" r="11" {_F}/>',
    "ray": f'<line x1="18" y1="72" x2="82" y2="28" {_S}/><path d="M82 28 L68 30 L74 42 Z" {_F}/>',
    "prism": f'<path d="M50 20 L80 75 L20 75 Z" {_S}/><line x1="50" y1="50" x2="86" y2="44" stroke="C" stroke-width="6"/>',
    "lens": f'<path d="M50 18 Q72 50 50 82 Q28 50 50 18 Z" {_S}/><line x1="10" y1="50" x2="90" y2="50" stroke="C" stroke-width="4" stroke-dasharray="3 5"/>',
    "wave": f'<path d="M12 50 Q27 20 42 50 T72 50 T100 50" {_S}/>',
    "sound": f'<path d="M20 40 L35 40 L50 26 L50 74 L35 60 L20 60 Z" {_F}/><path d="M62 38 Q72 50 62 62" {_S}/><path d="M70 30 Q86 50 70 70" {_S}/>',
    "magnet": f'<path d="M28 24 L28 56 Q28 78 50 78 Q72 78 72 56 L72 24" {_S}/><line x1="28" y1="24" x2="44" y2="24" stroke="C" stroke-width="9"/><line x1="56" y1="24" x2="72" y2="24" stroke="C" stroke-width="9"/>',
    "bolt": f'<path d="M56 12 L30 54 L48 54 L42 88 L72 44 L52 44 Z" {_F}/>',
    "battery": f'<rect x="20" y="36" width="55" height="28" rx="4" {_S}/><rect x="75" y="44" width="8" height="12" {_F}/><line x1="34" y1="44" x2="34" y2="56" stroke="C" stroke-width="6"/><line x1="50" y1="44" x2="50" y2="56" stroke="C" stroke-width="6"/>',
    "thermometer": f'<path d="M44 20 a6 6 0 0 1 12 0 v40 a12 12 0 1 1 -12 0 Z" {_S}/><circle cx="50" cy="72" r="8" {_F}/>',
    "fire": f'<path d="M50 18 Q66 38 58 52 Q74 50 66 74 Q60 86 50 86 Q34 86 32 68 Q30 54 42 48 Q40 34 50 18 Z" {_S}/>',
    "sun": f'<circle cx="50" cy="50" r="18" {_S}/>' + "".join(f'<line x1="{50+28*__import__("math").cos(a)}" y1="{50+28*__import__("math").sin(a)}" x2="{50+38*__import__("math").cos(a)}" y2="{50+38*__import__("math").sin(a)}" stroke="C" stroke-width="6" stroke-linecap="round"/>' for a in [i*0.7854 for i in range(8)]),
    "drop": f'<path d="M50 18 Q74 50 50 82 Q26 50 50 18 Z" {_S}/>',
    "gear": f'<circle cx="50" cy="50" r="16" {_S}/><circle cx="50" cy="50" r="30" stroke="C" stroke-width="7" fill="none" stroke-dasharray="6 9"/>',
    "target": f'<circle cx="50" cy="50" r="30" {_S}/><circle cx="50" cy="50" r="16" {_S}/><circle cx="50" cy="50" r="4" {_F}/>',
    "check": f'<path d="M24 52 L43 70 L78 30" {_S}/>',
    "scale": f'<line x1="50" y1="20" x2="50" y2="78" {_S}/><line x1="26" y1="32" x2="74" y2="32" {_S}/><path d="M16 32 L26 56 L36 32" {_S}/><path d="M64 32 L74 56 L84 32" {_S}/>',
    "plug": f'<path d="M34 24 L34 46 M66 24 L66 46" {_S}/><path d="M26 46 L74 46 L70 66 Q66 74 50 74 Q34 74 30 66 Z" {_S}/><line x1="50" y1="74" x2="50" y2="86" {_S}/>',
    "shield": f'<path d="M50 18 L78 28 V50 Q78 74 50 84 Q22 74 22 50 V28 Z" {_S}/><path d="M38 50 L47 60 L64 40" {_S}/>',
    "atom": f'<circle cx="50" cy="50" r="6" {_F}/><ellipse cx="50" cy="50" rx="34" ry="14" {_S}/><ellipse cx="50" cy="50" rx="34" ry="14" transform="rotate(60 50 50)" {_S}/><ellipse cx="50" cy="50" rx="34" ry="14" transform="rotate(120 50 50)" {_S}/>',
    "mirror": f'<line x1="36" y1="18" x2="36" y2="82" stroke="C" stroke-width="9"/><line x1="36" y1="40" x2="72" y2="26" {_S}/><line x1="36" y1="40" x2="72" y2="60" {_S}/>',
    "book": f'<path d="M50 26 Q34 18 20 24 V74 Q34 68 50 76 Q66 68 80 74 V24 Q66 18 50 26 Z" {_S}/><line x1="50" y1="26" x2="50" y2="76" {_S}/>',
    "ruler": f'<rect x="20" y="38" width="60" height="24" rx="3" {_S}/><line x1="32" y1="38" x2="32" y2="50" stroke="C" stroke-width="5"/><line x1="44" y1="38" x2="44" y2="50" stroke="C" stroke-width="5"/><line x1="56" y1="38" x2="56" y2="50" stroke="C" stroke-width="5"/><line x1="68" y1="38" x2="68" y2="50" stroke="C" stroke-width="5"/>',
    "spark": f'<path d="M50 16 L57 43 L84 50 L57 57 L50 84 L43 57 L16 50 L43 43 Z" {_S}/>',
}

# keyword -> icon name (first match wins)
_KEYWORDS = [
    (("lens", "convex", "concave", "magnif"), "lens"),
    (("prism", "deviation", "dispersion"), "prism"),
    (("mirror", "reflect"), "mirror"),
    (("ray", "refract", "incident", "light", "beam", "image", "bend"), "ray"),
    (("eye", "sight", "vision", "retina"), "eye"),
    (("sun", "sky", "sunset", "scatter", "sunrise"), "sun"),
    (("wave", "spectrum", "frequency", "wavelength", "radio", "micro"), "wave"),
    (("sound", "echo", "vibrat", "noise", "music", "audible"), "sound"),
    (("magnet", "field", "pole", "solenoid", "induction"), "magnet"),
    (("current", "electric", "circuit", "ohm", "resist", "charge", "power"), "bolt"),
    (("cell", "battery", "emf", "voltage"), "battery"),
    (("fuse", "plug", "earth", "wiring", "socket", "switch"), "plug"),
    (("safety", "hazard", "precaution", "protect", "danger"), "shield"),
    (("heat", "temperature", "thermal", "calor"), "thermometer"),
    (("boil", "fire", "flame", "melt", "fusion", "vapor", "steam"), "fire"),
    (("water", "liquid", "drop", "depth"), "drop"),
    (("atom", "nucleus", "radio", "isotope", "fission", "fusion"), "atom"),
    (("machine", "lever", "pulley", "gear", "work"), "gear"),
    (("energy", "kinetic", "potential", "bolt"), "bolt"),
    (("measure", "density", "ruler", "unit", "length"), "ruler"),
    (("law", "rule", "principle", "formula", "definition"), "book"),
    (("real life", "real", "use", "application", "around us"), "target"),
    (("balance", "equilibrium", "compare", "vs"), "scale"),
    (("correct", "true", "always", "key"), "check"),
]


def pick(text):
    t = (text or "").lower()
    for keys, name in _KEYWORDS:
        if any(k in t for k in keys):
            return name
    return "spark"


def render(name, color="FFFFFF", size=120):
    name = name if name in ICONS else "spark"
    key = f"{name}_{color}"
    path = os.path.abspath(os.path.join(IMG_DIR, f"{key}.png"))
    if os.path.exists(path):
        return path
    body = ICONS[name].replace("C", "#" + color)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">'
           f'{body}</svg>')
    cairosvg.svg2png(bytestring=svg.encode(), write_to=path,
                     output_width=size, output_height=size)
    return path


def for_heading(text, color="FFFFFF"):
    return render(pick(text), color)


if __name__ == "__main__":
    for n in ICONS:
        print(render(n))
