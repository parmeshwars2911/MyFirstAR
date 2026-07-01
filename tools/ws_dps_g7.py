"""
DPS-Monarch International School — Class 7 Science worksheets.

Blueprint chapters: Ch-3 Heat, Ch-6 Acids/Bases/Salts, Ch-9 Life Processes in
Animals, Ch-10 Life Processes in Plants, Ch-12 Time and Motion (NCERT Class 7).

Each chapter gets three printable A4 worksheets — Objective, Subjective and
Olympiad — each with its answer key appended on the last page.

Phase 1 here builds Ch-3 Heat as the sign-off sample; the other chapters follow
the same structure.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from worksheet import build_worksheet, validate_sections, qa_pdf
from assessment import dedup_report, balance_options


def _balanced(sections, seed):
    """Return a copy of the sections with every MCQ section's options balanced
    across A-D (keeps the answer key un-guessable). Non-MCQ sections pass "
    through unchanged."""
    out = []
    for k, sec in enumerate(sections):
        if sec["type"] == "mcq":
            sec = dict(sec)
            sec["items"] = balance_options(sec["items"], seed=seed + k)
        out.append(sec)
    return out

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
OUT = os.path.join(ROOT, "worksheets", "DPS_Monarch_G7_Science")
os.makedirs(OUT, exist_ok=True)

SCHOOL = "DPS-Monarch International School"
GRADE = "Class 7"


# ===========================================================================
# CH-3  HEAT   (temperature, thermometers, transfer of heat)
# ===========================================================================
HEAT_SYLL = ("Hot & cold and temperature, measuring temperature, clinical and "
             "laboratory thermometers, transfer of heat (conduction, "
             "convection, radiation), conductors & insulators, sea & land "
             "breeze, dark/light surfaces.")

HEAT_OBJECTIVE = [
    {"type": "mcq", "marks_line": "1 × 8 = 8", "items": [
        {"q": "The unit in which temperature is usually measured on a "
         "thermometer is the:",
         "options": ["kilogram", "degree Celsius (°C)", "metre", "second"],
         "correct": 1},
        {"q": "The normal temperature of a healthy human body is about:",
         "options": ["37°C", "42°C", "35°C", "100°C"], "correct": 0},
        {"q": "The temperature range of a clinical thermometer is about:",
         "options": ["−10°C to 110°C", "35°C to 42°C", "0°C to 100°C",
                     "0°C to 250°C"], "correct": 1},
        {"q": "Heat always flows on its own from a body at ___ temperature to "
         "a body at ___ temperature.",
         "options": ["lower, higher", "higher, lower", "equal, equal",
                     "zero, high"], "correct": 1},
        {"q": "Which of the following is the best conductor of heat?",
         "options": ["wood", "plastic", "aluminium", "rubber"], "correct": 2},
        {"q": "The other end of a steel spoon kept in a cup of hot tea becomes "
         "hot by the process of:",
         "options": ["convection", "conduction", "radiation", "evaporation"],
         "correct": 1},
        {"q": "A sea breeze blows from the sea towards the land during the:",
         "options": ["night", "day", "midnight", "early hours"], "correct": 1},
        {"q": "The heat of the Sun reaches the Earth through empty space "
         "mainly by:",
         "options": ["conduction", "convection", "radiation", "all three"],
         "correct": 2},
    ]},
    {"type": "fill", "marks_line": "1 × 5 = 5", "items": [
        {"q": "The device used to measure temperature is a ______.",
         "answer": "thermometer"},
        {"q": "A clinical thermometer has a ______ near the bulb that stops "
         "the mercury falling on its own.", "answer": "kink (constriction)"},
        {"q": "Materials that do not allow heat to pass through them easily "
         "are called ______.", "answer": "insulators (poor conductors)"},
        {"q": "In ______, the particles of the medium do not move from their "
         "place while passing on heat.", "answer": "conduction"},
        {"q": "Dark-coloured surfaces are ______ absorbers of heat than "
         "light-coloured surfaces.", "answer": "better (good)"},
    ]},
    {"type": "tf", "marks_line": "1 × 5 = 5", "items": [
        {"q": "Our sense of touch is a reliable way to measure the exact "
         "temperature of an object.", "answer": False},
        {"q": "Water is a poor conductor of heat.", "answer": True},
        {"q": "Convection can take place in solids.", "answer": False},
        {"q": "Woollen clothes keep us warm because the trapped air is a poor "
         "conductor of heat.", "answer": True},
        {"q": "A laboratory thermometer is used to measure the temperature of "
         "the human body.", "answer": False},
    ]},
    {"type": "match", "marks_line": "1 × 4 = 4",
     "colA": ["Clinical thermometer", "Land breeze", "Copper", "Thermos "
              "flask"],
     "colB": ["a good conductor of heat", "reduces heat transfer by all three "
              "modes", "measures body temperature", "blows from land to sea "
              "at night"],
     "pairs": [(0, 2), (1, 3), (2, 0), (3, 1)]},
    {"type": "assertion", "marks_line": "1 × 3 = 3", "items": [
        {"a": "We wear light-coloured clothes in summer.",
         "r": "Light-coloured surfaces reflect most of the heat radiation "
              "falling on them.", "answer": "A"},
        {"a": "The handles of cooking pans are made of plastic or wood.",
         "r": "Plastic and wood are good conductors of heat.", "answer": "C"},
        {"a": "A sea breeze blows during the day.",
         "r": "During the day the land heats up faster than the sea, so the "
              "warm air over the land rises.", "answer": "A"},
    ]},
]

HEAT_SUBJECTIVE = [
    {"type": "short", "title": "Very Short Answer", "marks_line": "1 × 5 = 5",
     "items": [
        {"q": "Name the instrument used to measure temperature.", "marks": 1,
         "lines": 1, "answer": ["A thermometer."]},
        {"q": "State the normal temperature of the human body in °C.",
         "marks": 1, "lines": 1, "answer": ["About 37°C (98.6°F)."]},
        {"q": "Name the mode of heat transfer that does not need a medium.",
         "marks": 1, "lines": 1, "answer": ["Radiation."]},
        {"q": "Give one example of a good conductor of heat.", "marks": 1,
         "lines": 1, "answer": ["Any metal, e.g. copper or aluminium."]},
        {"q": "Why should a clinical thermometer never be used to measure the "
         "temperature of boiling water?", "marks": 1, "lines": 2,
         "answer": ["Its range only goes up to about 42°C, so the boiling "
                    "water would overheat it and the thermometer would "
                    "break."]},
    ]},
    {"type": "short", "title": "Short Answer", "marks_line": "2 × 5 = 10",
     "items": [
        {"q": "Give any two differences between a clinical thermometer and a "
         "laboratory thermometer.", "marks": 2, "lines": 3,
         "answer": ["Clinical: range 35–42°C, has a kink, used for body "
                    "temperature. Laboratory: range about −10°C to 110°C, no "
                    "kink, used for general lab measurements."]},
        {"q": "What is conduction? Give one everyday example.", "marks": 2,
         "lines": 3,
         "answer": ["Conduction is the transfer of heat through a material "
                    "from particle to particle without the particles moving "
                    "along, e.g. a metal spoon getting hot in hot tea."]},
        {"q": "Explain how a sea breeze is set up during the day.", "marks": 3,
         "lines": 3,
         "answer": ["By day the land heats up faster than the sea; the warm "
                    "air over the land rises and the cooler air from over the "
                    "sea moves in to take its place — this is the sea "
                    "breeze."]},
        {"q": "Why are the handles of cooking utensils usually made of wood "
         "or plastic?", "marks": 2, "lines": 2,
         "answer": ["Wood and plastic are poor conductors (insulators) of "
                    "heat, so the handle stays cool and does not burn the "
                    "hand."]},
        {"q": "Why does a person wearing dark clothes feel hotter in the Sun "
         "than one wearing white clothes?", "marks": 2, "lines": 2,
         "answer": ["Dark surfaces absorb most of the heat radiation, while "
                    "white surfaces reflect most of it, so dark clothes feel "
                    "hotter."]},
    ]},
    {"type": "long", "title": "Long Answer", "marks_line": "5 × 3 = 15",
     "items": [
        {"q": "Explain the three modes of heat transfer, giving one example "
         "of each.", "marks": 5, "lines": 6,
         "answer": ["Conduction — heat passes through solids from particle to "
                    "particle (metal spoon in hot tea). Convection — the "
                    "heated liquid/gas itself moves (boiling water, sea "
                    "breeze). Radiation — heat travels without any medium "
                    "(the Sun's heat, warmth near a fire)."]},
        {"q": "Describe a simple activity to show that different solids "
         "conduct heat at different rates.", "marks": 5, "lines": 6,
         "answer": ["Fix small wax balls with equal wax at the ends of rods of "
                    "copper, aluminium, iron and glass. Heat the other ends "
                    "together. The wax ball on the best conductor (copper) "
                    "falls first and the one on glass falls last, showing "
                    "metals conduct heat faster than glass."]},
        {"q": "Explain, with the help of a diagram, the formation of a land "
         "breeze at night.", "marks": 5, "lines": 6,
         "answer": ["At night the land cools faster than the sea. The warmer "
                    "air over the sea rises and the cooler air from over the "
                    "land moves out towards the sea to replace it — this flow "
                    "of air from land to sea is the land breeze. (Diagram: "
                    "arrows from land to sea, warm air rising over the sea.)"]},
    ]},
    {"type": "short", "title": "Higher-Order Thinking (Give Reasons)",
     "marks_line": "2 × 2 = 4", "items": [
        {"q": "A block of ice is wrapped in a woollen blanket. Explain whether "
         "it melts faster or slower, and why.", "marks": 2, "lines": 3,
         "answer": ["It melts slower. Wool (and the air trapped in it) is a "
                    "poor conductor, so it slows the flow of heat from the "
                    "warm surroundings into the ice."]},
        {"q": "Two identical vessels, one black and one white, are filled with "
         "equally hot water. Which cools faster, and why?", "marks": 2,
         "lines": 3,
         "answer": ["The black vessel cools faster, because dark surfaces are "
                    "better emitters (radiators) of heat than white "
                    "surfaces."]},
    ]},
]

HEAT_OLYMPIAD = [
    {"type": "mcq", "title": "Multiple Choice (Higher Order)",
     "marks_line": "1 × 14 = 14", "items": [
        {"q": "Two identical cups of hot water are taken; one is wrapped in a "
         "woollen cloth. After 10 minutes, the water that is hotter is in the:",
         "options": ["bare cup", "cup wrapped in wool", "neither — both are "
                     "equal", "cup that was stirred"], "correct": 1},
        {"q": "On a cold morning an iron bench and a wooden bench are at the "
         "same temperature, yet the iron feels colder. This is because iron:",
         "options": ["is actually colder", "conducts heat away from the hand "
                     "faster", "radiates cold", "is heavier"], "correct": 1},
        {"q": "Heated over the same flame for the same time, water gets "
         "hottest in a:",
         "options": ["shiny white ceramic pot", "dull black metal pot",
                     "shiny silver metal pot", "glass beaker"], "correct": 1},
        {"q": "The temperature of a body is best described as a measure of:",
         "options": ["the total heat energy stored in it", "the average "
                     "degree of hotness of its particles", "its mass",
                     "its volume"], "correct": 1},
        {"q": "The shiny silvered walls of a thermos flask mainly reduce heat "
         "loss by:",
         "options": ["conduction", "convection", "radiation", "all three "
                     "equally"], "correct": 2},
        {"q": "Rods of copper, aluminium, iron and glass of equal size are "
         "heated at one end with a wax ball at the other. The ball that falls "
         "LAST is on the:",
         "options": ["copper rod", "aluminium rod", "iron rod", "glass rod"],
         "correct": 3},
        {"q": "During the day a sea breeze sets in because the air over the "
         "land:",
         "options": ["sinks down", "becomes denser", "gets warmer and rises",
                     "becomes cooler"], "correct": 2},
        {"q": "Loose white cotton clothes are comfortable in summer because "
         "white reflects heat and loose cotton also:",
         "options": ["soaks up sweat and lets air flow (convection)",
                     "conducts heat to the body", "radiates heat inward",
                     "blocks all air"], "correct": 0},
        {"q": "Which arrangement keeps a block of ice from melting the "
         "longest?",
         "options": ["ice in a metal box", "ice wrapped in a woollen blanket",
                     "ice on an open steel plate", "ice on a black tray in "
                     "sunlight"], "correct": 1},
        {"q": "The only mode of heat transfer that can take place through a "
         "vacuum is:",
         "options": ["conduction", "convection", "radiation", "conduction and "
                     "convection"], "correct": 2},
        {"q": "A laboratory thermometer generally has a range of about:",
         "options": ["35°C to 42°C", "−10°C to 110°C", "0°C to 50°C",
                     "100°C to 250°C"], "correct": 1},
        {"q": "The reading of a clinical thermometer does not fall on its own "
         "when taken out of the mouth because:",
         "options": ["mercury is very heavy", "the kink stops the mercury "
                     "flowing back", "it is a digital device", "the glass is "
                     "thick"], "correct": 1},
        {"q": "A patient's temperature is recorded as 40°C. Compared with the "
         "normal body temperature, this shows a fever of:",
         "options": ["3°C above normal", "3°C below normal", "40°C above "
                     "normal", "no fever"], "correct": 0},
        {"q": "In an experiment, equal wax balls on copper, iron and glass "
         "rods fall at 20 s, 45 s and 90 s. The best conductor of heat is:",
         "options": ["copper", "iron", "glass", "all are equal"],
         "correct": 0},
    ]},
    {"type": "assertion", "title": "Assertion–Reason", "marks_line": "1 × 3 = 3",
     "items": [
        {"a": "Metals are used to make cooking utensils.",
         "r": "Metals are good conductors of heat.", "answer": "A"},
        {"a": "On a sunny day, a car with dark-coloured seats becomes hotter "
              "inside than one with light-coloured seats.",
         "r": "Dark surfaces are good absorbers of heat radiation.",
         "answer": "A"},
        {"a": "Birds often fluff up their feathers in cold weather.",
         "r": "The air trapped between the feathers is a good conductor of "
              "heat.", "answer": "C"},
    ]},
]


# ===========================================================================
# BUILD
# ===========================================================================
def _mcq_sets(worksheets):
    """Collect the MCQ items across a chapter's worksheets for dedup."""
    named = {}
    for name, secs in worksheets:
        for sec in secs:
            if sec["type"] == "mcq":
                named.setdefault(name, []).extend(sec["items"])
    return named


CHAPTERS = [
    dict(num="Ch-3", chapter="Heat", subject="Science — Physics",
         syllabus=HEAT_SYLL, objective=HEAT_OBJECTIVE,
         subjective=HEAT_SUBJECTIVE, olympiad=HEAT_OLYMPIAD),
]


def build():
    for ch in CHAPTERS:
        tag = f"{ch['num'].replace('-', '').replace('.', '')}_" \
              f"{ch['chapter'].replace(' ', '_')}"
        jobs = [
            ("Objective", ch["objective"], "45 min", 25),
            ("Subjective", ch["subjective"], "1 hour", 34),
            ("Olympiad", ch["olympiad"], "45 min", 17),
        ]
        # within-chapter dedup across the three worksheets' MCQs
        named = {f"{ch['chapter']} {kind}":
                 [it for sec in secs if sec["type"] == "mcq"
                  for it in sec["items"]]
                 for kind, secs, _, _ in jobs}
        warns = dedup_report(named)
        print(f"== {ch['num']} {ch['chapter']}: dedup ==")
        print("  " + ("clean" if not warns else "; ".join(warns)))

        for ji, (kind, secs, dur, marks) in enumerate(jobs):
            issues = validate_sections(secs)
            if issues:
                print(f"  !! {kind} validation: {issues}")
            secs = _balanced(secs, seed=300 + ji * 17)
            fname = f"G7Sci_{tag}_{kind}.pdf"
            path = os.path.join(OUT, fname)
            build_worksheet(
                path, school=SCHOOL, subject=ch["subject"], grade=GRADE,
                chapter=ch["chapter"], kind=kind,
                max_marks=marks, duration=dur, sections=secs)
            ov = qa_pdf(path)
            print(f"  {fname}: built"
                  + (f"  [overflow: {ov[:2]}]" if ov else "  [clean]"))


if __name__ == "__main__":
    build()
