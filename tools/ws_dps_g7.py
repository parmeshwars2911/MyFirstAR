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
        {"q": "Heat flows from object A to object B the moment they touch. "
         "This tells us that, before contact, A had a higher:",
         "options": ["mass than B", "temperature than B", "volume than B",
                     "amount of stored heat than B"], "correct": 1},
        {"q": "A nurse reads 39°C on a patient's clinical thermometer. "
         "Compared with normal body temperature, the patient is:",
         "options": ["2°C below normal", "2°C above normal", "exactly normal",
                     "at room temperature"], "correct": 1},
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


def build():
    for ch in CHAPTERS:
        tag = f"{ch['num'].replace('-', '').replace('.', '')}_" \
              f"{ch['chapter'].replace(',', '').replace(' ', '_')}"
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


# ===========================================================================
# CH-6  ACIDS, BASES AND SALTS
# ===========================================================================
ACID_OBJECTIVE = [
    {"type": "mcq", "marks_line": "1 × 8 = 8", "items": [
        {"q": "A solution turns blue litmus red but has no effect on red "
         "litmus. The solution is:",
         "options": ["basic", "acidic", "neutral", "distilled water"],
         "correct": 1},
        {"q": "Turmeric paste on a white cloth turns red where soap is "
         "rubbed. This shows that soap solution is:",
         "options": ["acidic", "basic", "neutral", "salty"], "correct": 1},
        {"q": "Equal volumes of an acid and a base are mixed and the mixture "
         "then changes neither red nor blue litmus. The mixture contains:",
         "options": ["only acid", "only base", "salt and water",
                     "a stronger acid"], "correct": 2},
        {"q": "Which pair correctly matches an acid with its natural source?",
         "options": ["citric acid – vinegar", "acetic acid – lemon",
                     "lactic acid – curd", "tartaric acid – ant sting"],
         "correct": 2},
        {"q": "A gardener adds slaked lime (a base) to a field. The soil was "
         "most likely:",
         "options": ["too basic", "too acidic", "perfectly neutral",
                     "too salty"], "correct": 1},
        {"q": "Rubbing baking soda on an ant's sting relieves the pain "
         "because the baking soda:",
         "options": ["adds more acid", "neutralises the acid injected by the "
                     "ant", "cools the skin by evaporation", "colours the "
                     "skin"], "correct": 1},
        {"q": "Solution P turns red litmus blue, Q turns blue litmus red and R "
         "changes neither. P, Q and R are respectively:",
         "options": ["acidic, basic, neutral", "basic, acidic, neutral",
                     "neutral, basic, acidic", "all neutral"], "correct": 1},
        {"q": "During the neutralisation of an acid by a base, the temperature "
         "of the mixture usually:",
         "options": ["falls sharply", "rises (heat is given out)", "stays "
                     "exactly the same", "drops to zero"], "correct": 1},
    ]},
    {"type": "fill", "marks_line": "1 × 5 = 5", "items": [
        {"q": "An acid turns ______ litmus red.", "answer": "blue"},
        {"q": "Bases turn red litmus ______.", "answer": "blue"},
        {"q": "The reaction between an acid and a base is called ______.",
         "answer": "neutralisation"},
        {"q": "Milk of magnesia, taken to relieve stomach acidity, is a mild "
         "______.", "answer": "base (antacid)"},
        {"q": "China rose indicator turns ______ with an acidic solution.",
         "answer": "dark pink (magenta)"},
    ]},
    {"type": "tf", "marks_line": "1 × 5 = 5", "items": [
        {"q": "All acids are dangerous and are never found in the food we "
         "eat.", "answer": False},
        {"q": "Distilled water has no effect on either red or blue litmus.",
         "answer": True},
        {"q": "A solution that turns china rose indicator green is acidic.",
         "answer": False},
        {"q": "The salt formed on neutralising any acid with any base is "
         "always common salt (sodium chloride).", "answer": False},
        {"q": "Bases generally feel soapy to the touch and taste bitter.",
         "answer": True},
    ]},
    {"type": "match", "marks_line": "1 × 4 = 4",
     "colA": ["Acetic acid", "Formic acid", "Citric acid", "Lactic acid"],
     "colB": ["curd", "vinegar", "lemon and orange", "ant's sting"],
     "pairs": [(0, 1), (1, 3), (2, 2), (3, 0)]},
    {"type": "assertion", "marks_line": "1 × 3 = 3", "items": [
        {"a": "Toothpastes are usually basic in nature.",
         "r": "They neutralise the acids formed in the mouth that cause tooth "
              "decay.", "answer": "A"},
        {"a": "Acidic factory waste is treated with basic substances before "
              "being released into rivers.",
         "r": "The untreated acidic waste would harm the plants and animals "
              "living in the water.", "answer": "A"},
        {"a": "Lemon juice turns blue litmus red.",
         "r": "Lemon juice is basic in nature.", "answer": "C"},
    ]},
]

ACID_SUBJECTIVE = [
    {"type": "short", "title": "Very Short Answer", "marks_line": "1 × 5 = 5",
     "items": [
        {"q": "Name the acid present in curd.", "marks": 1, "lines": 1,
         "answer": ["Lactic acid."]},
        {"q": "Name the natural indicator obtained from lichen.", "marks": 1,
         "lines": 1, "answer": ["Litmus."]},
        {"q": "Name the two products always formed when an acid reacts with a "
         "base.", "marks": 1, "lines": 1, "answer": ["A salt and water."]},
        {"q": "Name the base present in milk of magnesia.", "marks": 1,
         "lines": 1, "answer": ["Magnesium hydroxide."]},
        {"q": "State the colour of turmeric indicator in a basic solution.",
         "marks": 1, "lines": 1, "answer": ["Red."]},
    ]},
    {"type": "short", "title": "Short Answer", "marks_line": "2 × 5 = 10",
     "items": [
        {"q": "Define neutralisation and write its general word equation.",
         "marks": 2, "lines": 3,
         "answer": ["Neutralisation is the reaction in which an acid and a "
                    "base react to cancel each other's effect: "
                    "acid + base → salt + water (heat is released)."]},
        {"q": "Explain how an antacid relieves indigestion caused by too much "
         "acid in the stomach.", "marks": 3, "lines": 3,
         "answer": ["The stomach makes hydrochloric acid; when there is too "
                    "much, it causes indigestion. An antacid is a mild base "
                    "that neutralises the excess acid and relieves the "
                    "discomfort."]},
        {"q": "A field is found to be too acidic for crops. State what should "
         "be added to it and give the reason.", "marks": 2, "lines": 3,
         "answer": ["Lime (a base, e.g. slaked lime/quick lime) should be "
                    "added to neutralise the excess acid and make the soil "
                    "suitable for crops."]},
        {"q": "Describe how you would use turmeric paper to find out whether a "
         "given solution is basic.", "marks": 2, "lines": 3,
         "answer": ["Put a drop of the solution on turmeric paper. If it turns "
                    "red, the solution is basic; if there is no change it is "
                    "acidic or neutral."]},
        {"q": "Give any two differences between acids and bases.", "marks": 2,
         "lines": 3,
         "answer": ["Acids taste sour and turn blue litmus red; bases taste "
                    "bitter, feel soapy and turn red litmus blue."]},
    ]},
    {"type": "long", "title": "Long Answer", "marks_line": "5 × 3 = 15",
     "items": [
        {"q": "Describe an activity using red and blue litmus to classify "
         "three unknown solutions as acidic, basic or neutral.", "marks": 5,
         "lines": 6,
         "answer": ["Put each solution on both red and blue litmus. If blue "
                    "turns red → acidic; if red turns blue → basic; if neither "
                    "changes → neutral. Record the results for the three "
                    "solutions in a table and classify each."]},
        {"q": "Explain, with three examples, how neutralisation is useful in "
         "everyday life.", "marks": 5, "lines": 6,
         "answer": ["Indigestion — antacid (base) neutralises excess stomach "
                    "acid. Ant/bee sting — baking soda neutralises the acid. "
                    "Soil treatment — lime neutralises acidic soil. Factory "
                    "waste — basic substances neutralise acidic effluent."]},
        {"q": "What are natural indicators? Name any three and state the "
         "colour each shows with an acid and with a base.", "marks": 5,
         "lines": 6,
         "answer": ["Natural indicators are substances from nature that show "
                    "different colours in acids and bases. Litmus: red in "
                    "acid, blue in base. Turmeric: yellow in acid (no change), "
                    "red in base. China rose: dark pink in acid, green in "
                    "base."]},
    ]},
    {"type": "short", "title": "Higher-Order Thinking (Give Reasons)",
     "marks_line": "2 × 2 = 4", "items": [
        {"q": "A liquid changes the colour of neither red nor blue litmus. "
         "What can you conclude about it? Give one example.", "marks": 2,
         "lines": 3,
         "answer": ["It is neutral (neither acidic nor basic), e.g. distilled "
                    "water, common salt solution or sugar solution."]},
        {"q": "Why is a mild base such as baking soda, and not a strong base "
         "like sodium hydroxide, used on an ant's sting?", "marks": 2,
         "lines": 3,
         "answer": ["A strong base is corrosive and would damage the skin; a "
                    "mild base neutralises the acid safely."]},
    ]},
]

ACID_OLYMPIAD = [
    {"type": "mcq", "title": "Multiple Choice (Higher Order)",
     "marks_line": "1 × 14 = 14", "items": [
        {"q": "To tell apart an acid, a base and a neutral solution with "
         "certainty, the least you need is:",
         "options": ["only blue litmus", "both red and blue litmus",
                     "only turmeric", "no indicator at all"], "correct": 1},
        {"q": "A solution turns china rose dark pink and also turns blue "
         "litmus red. The solution is:",
         "options": ["basic", "acidic", "neutral", "both acidic and basic"],
         "correct": 1},
        {"q": "Acid and base of equal strength are mixed till litmus shows no "
         "change. If a little more acid is then added, the mixture will now "
         "turn:",
         "options": ["red litmus blue", "blue litmus red", "china rose green",
                     "no litmus at all"], "correct": 1},
        {"q": "Bubbles of gas form when a pinch of baking soda is dropped into "
         "lemon juice. This shows the baking soda:",
         "options": ["is itself an acid", "reacts with (neutralises) the acid",
                     "is completely neutral", "is only a colouring"],
         "correct": 1},
        {"q": "Which everyday problem is NOT solved by neutralisation?",
         "options": ["relieving an ant sting", "curing acidity/indigestion",
                     "making acidic soil fit for crops", "boiling water for "
                     "tea"], "correct": 3},
        {"q": "Four liquids are tested with turmeric paper; only one turns it "
         "red. That liquid is most likely:",
         "options": ["vinegar", "lemon juice", "a window-cleaner containing "
                     "ammonia", "orange juice"], "correct": 2},
        {"q": "Marble is basic. A marble statue exposed to acid rain for many "
         "years will slowly be:",
         "options": ["made larger", "eaten away (neutralised)", "turned blue",
                     "left unchanged"], "correct": 1},
        {"q": "A wasp's sting is basic (unlike an ant's acidic sting). The "
         "best household remedy for a wasp sting is a mild:",
         "options": ["base such as baking soda", "acid such as vinegar",
                     "neutral liquid such as water", "salt solution"],
         "correct": 1},
        {"q": "A soil sample turns china rose indicator green. To make it "
         "neutral for most crops, one should mix in:",
         "options": ["more lime", "decaying leaves or manure (acidic organic "
                     "matter)", "common salt", "sand"], "correct": 1},
        {"q": "Which statement is ALWAYS true?",
         "options": ["All acids are liquids", "All bases turn red litmus blue",
                     "All salts are acidic", "Neutral solutions turn litmus "
                     "red"], "correct": 1},
        {"q": "Two colourless solutions are mixed; the beaker becomes warm and "
         "the mixture then has no effect on litmus. The two solutions were "
         "probably:",
         "options": ["two acids", "two bases", "an acid and a base",
                     "two neutral solutions"], "correct": 2},
        {"q": "The sour taste of an unripe mango and the sting of a nettle "
         "leaf are both caused by:",
         "options": ["bases", "acids", "salts", "neutral substances"],
         "correct": 1},
        {"q": "Antacids use magnesium or aluminium hydroxide rather than "
         "sodium hydroxide because sodium hydroxide is:",
         "options": ["tasteless", "a strong, corrosive base unsafe to "
                     "swallow", "actually an acid", "completely neutral"],
         "correct": 1},
        {"q": "When hydrochloric acid is neutralised by sodium hydroxide, the "
         "salt formed is:",
         "options": ["calcium carbonate", "sodium chloride (common salt)",
                     "magnesium sulphate", "ammonium chloride"], "correct": 1},
    ]},
    {"type": "assertion", "title": "Assertion–Reason", "marks_line": "1 × 3 = 3",
     "items": [
        {"a": "Baking soda is rubbed on an ant's sting.",
         "r": "The ant injects an acidic liquid, which the basic baking soda "
              "neutralises.", "answer": "A"},
        {"a": "Distilled water does not change the colour of litmus.",
         "r": "Distilled water is neutral.", "answer": "A"},
        {"a": "Curd is not usually stored in brass or copper vessels.",
         "r": "The lactic acid in curd reacts with these metals.",
         "answer": "A"},
    ]},
]


# ===========================================================================
# CH-9  LIFE PROCESSES IN ANIMALS  (nutrition, digestion, respiration)
# ===========================================================================
ANIM_OBJECTIVE = [
    {"type": "mcq", "marks_line": "1 × 8 = 8", "items": [
        {"q": "The process by which digested food passes through the "
         "intestinal wall into the blood is called:",
         "options": ["ingestion", "digestion", "absorption", "egestion"],
         "correct": 2},
        {"q": "A cow brings swallowed grass back into its mouth and chews it "
         "again. This partly digested food is called:",
         "options": ["saliva", "cud", "bile", "mucus"], "correct": 1},
        {"q": "In the human body, most of the digested food is absorbed in "
         "the:",
         "options": ["stomach", "small intestine", "large intestine",
                     "mouth"], "correct": 1},
        {"q": "Amoeba captures its food using finger-like extensions called:",
         "options": ["cilia", "pseudopodia", "villi", "flagella"],
         "correct": 1},
        {"q": "The correct order of the steps in animal nutrition is:",
         "options": ["digestion → ingestion → absorption → egestion",
                     "ingestion → digestion → absorption → assimilation → "
                     "egestion", "absorption → ingestion → egestion",
                     "ingestion → egestion → digestion"], "correct": 1},
        {"q": "Bile, which helps in the digestion of fats, is produced by "
         "the:",
         "options": ["pancreas", "liver", "stomach", "small intestine"],
         "correct": 1},
        {"q": "During respiration, the gas taken in and the gas given out are "
         "respectively:",
         "options": ["carbon dioxide and oxygen", "oxygen and carbon dioxide",
                     "oxygen and nitrogen", "carbon dioxide and nitrogen"],
         "correct": 1},
        {"q": "Fish can breathe under water because they possess special "
         "respiratory organs called:",
         "options": ["lungs", "gills", "tracheae", "skin folds"],
         "correct": 1},
    ]},
    {"type": "fill", "marks_line": "1 × 5 = 5", "items": [
        {"q": "The muscular tube that pushes food from the mouth to the "
         "stomach is the ______.", "answer": "oesophagus (food pipe)"},
        {"q": "The finger-like projections on the inner wall of the small "
         "intestine that increase absorption are called ______.",
         "answer": "villi"},
        {"q": "Grass-eating animals digest cellulose with the help of ______ "
         "living in their stomach.", "answer": "bacteria (microbes)"},
        {"q": "In humans, the exchange of gases takes place in the tiny "
         "air-sacs of the lungs called ______.", "answer": "alveoli"},
        {"q": "The removal of undigested food from the body is called ______.",
         "answer": "egestion"},
    ]},
    {"type": "tf", "marks_line": "1 × 5 = 5", "items": [
        {"q": "Digestion of food begins in the stomach.", "answer": False},
        {"q": "Amoeba digests its food inside a food vacuole.",
         "answer": True},
        {"q": "Insects such as the cockroach breathe through gills.",
         "answer": False},
        {"q": "The liver is the largest gland in the human body.",
         "answer": True},
        {"q": "The use of absorbed food by the body cells to release energy is "
         "called egestion.", "answer": False},
    ]},
    {"type": "match", "marks_line": "1 × 4 = 4",
     "colA": ["Liver", "Villi", "Gills", "Saliva"],
     "colB": ["absorption of digested food", "breathing in fish",
              "secretes bile", "begins the digestion of starch"],
     "pairs": [(0, 2), (1, 0), (2, 1), (3, 3)]},
    {"type": "assertion", "marks_line": "1 × 3 = 3", "items": [
        {"a": "The small intestine is very long and lined with villi.",
         "r": "This gives a large surface area for the absorption of digested "
              "food.", "answer": "A"},
        {"a": "Ruminants such as cows can survive on grass alone.",
         "r": "Bacteria in their stomach digest the cellulose in grass.",
         "answer": "A"},
        {"a": "We should chew our food thoroughly before swallowing.",
         "r": "Chewing stops the action of saliva on the food.",
         "answer": "C"},
    ]},
]

ANIM_SUBJECTIVE = [
    {"type": "short", "title": "Very Short Answer", "marks_line": "1 × 5 = 5",
     "items": [
        {"q": "Name the projections that increase absorption in the small "
         "intestine.", "marks": 1, "lines": 1, "answer": ["Villi."]},
        {"q": "Name the organ that produces bile.", "marks": 1, "lines": 1,
         "answer": ["The liver."]},
        {"q": "Name the respiratory organ of a fish.", "marks": 1, "lines": 1,
         "answer": ["Gills."]},
        {"q": "What is the partly digested food that ruminants chew again "
         "called?", "marks": 1, "lines": 1, "answer": ["Cud."]},
        {"q": "Name the process by which absorbed food is used by the body "
         "cells.", "marks": 1, "lines": 1, "answer": ["Assimilation."]},
    ]},
    {"type": "short", "title": "Short Answer", "marks_line": "2 × 5 = 10",
     "items": [
        {"q": "Differentiate between ingestion and egestion.", "marks": 2,
         "lines": 3,
         "answer": ["Ingestion is the taking in of food into the body; "
                    "egestion is the removal of undigested food from the "
                    "body."]},
        {"q": "Why is the small intestine long and provided with villi?",
         "marks": 2, "lines": 3,
         "answer": ["Its length and the villi together give a very large "
                    "surface area, so that the maximum digested food can be "
                    "absorbed into the blood."]},
        {"q": "How does an Amoeba obtain and digest its food?", "marks": 3,
         "lines": 3,
         "answer": ["It puts out pseudopodia that surround the food and trap "
                    "it in a food vacuole; the food is digested there and the "
                    "useful part absorbed into the cell."]},
        {"q": "Why can a cow digest grass while a human being cannot?",
         "marks": 2, "lines": 3,
         "answer": ["A cow's stomach holds bacteria that digest the cellulose "
                    "of grass; humans do not have these bacteria, so they "
                    "cannot digest cellulose."]},
        {"q": "Name any two respiratory organs found in different animals and "
         "state one animal that uses each.", "marks": 2, "lines": 3,
         "answer": ["Lungs — humans/mammals; gills — fish; moist skin — "
                    "earthworm; tracheae — insects (any two)."]},
    ]},
    {"type": "long", "title": "Long Answer", "marks_line": "5 × 3 = 15",
     "items": [
        {"q": "Describe the five steps of nutrition in animals, writing one "
         "line about each.", "marks": 5, "lines": 6,
         "answer": ["Ingestion — taking in food; digestion — breaking food "
                    "into simple, soluble substances; absorption — soluble "
                    "food passes into the blood; assimilation — cells use the "
                    "food for energy and growth; egestion — undigested food is "
                    "removed."]},
        {"q": "Trace the path of food through the human alimentary canal, "
         "naming the main organs and the job of each.", "marks": 5, "lines": 6,
         "answer": ["Mouth (chewing + saliva) → oesophagus (pushes food) → "
                    "stomach (churns, acid + juices) → small intestine "
                    "(digestion completed, food absorbed through villi) → "
                    "large intestine (water absorbed) → anus (egestion). Liver "
                    "and pancreas add digestive juices."]},
        {"q": "Explain how the exchange of gases takes place in humans during "
         "breathing.", "marks": 5, "lines": 6,
         "answer": ["Air is breathed in through the nose into the lungs and "
                    "reaches the alveoli. Oxygen from the air passes into the "
                    "blood, and carbon dioxide passes from the blood into the "
                    "alveoli and is breathed out."]},
    ]},
    {"type": "short", "title": "Higher-Order Thinking (Give Reasons)",
     "marks_line": "2 × 2 = 4", "items": [
        {"q": "A person has had part of the small intestine removed. Explain "
         "why they may become weak even though they eat enough food.",
         "marks": 2, "lines": 3,
         "answer": ["A shorter small intestine has less surface for "
                    "absorption, so less digested food enters the blood and "
                    "the body is undernourished."]},
        {"q": "Earthworms breathe through their moist skin. Explain why they "
         "come out of the soil during heavy rain.", "marks": 2, "lines": 3,
         "answer": ["Rain fills the soil spaces with water, leaving little "
                    "air, so the earthworms come to the surface to get "
                    "oxygen."]},
    ]},
]

ANIM_OLYMPIAD = [
    {"type": "mcq", "title": "Multiple Choice (Higher Order)",
     "marks_line": "1 × 14 = 14", "items": [
        {"q": "If the villi of the small intestine were badly damaged, the "
         "process most directly affected would be:",
         "options": ["ingestion", "digestion", "absorption", "egestion"],
         "correct": 2},
        {"q": "A tapeworm lives in the human intestine and soaks up the "
         "already-digested food, having no digestive system of its own. Its "
         "mode of nutrition is:",
         "options": ["autotrophic", "saprotrophic", "parasitic",
                     "insectivorous"], "correct": 2},
        {"q": "The substance in saliva begins the digestion of:",
         "options": ["proteins", "fats", "starch (carbohydrates)",
                     "minerals"], "correct": 2},
        {"q": "Which path correctly traces a bite of bread through the body?",
         "options": ["mouth → stomach → oesophagus → small intestine",
                     "mouth → oesophagus → stomach → small intestine → large "
                     "intestine", "mouth → small intestine → stomach",
                     "stomach → mouth → intestine"], "correct": 1},
        {"q": "A cow's stomach has four chambers while a tiger's has one, "
         "mainly because the cow must digest:",
         "options": ["meat", "cellulose-rich grass", "large amounts of water",
                     "bones"], "correct": 1},
        {"q": "During heavy exercise we breathe faster chiefly to:",
         "options": ["cool the body", "take in more oxygen and remove more "
                     "carbon dioxide", "digest food faster", "absorb more "
                     "water"], "correct": 1},
        {"q": "Amoeba does not need lungs or gills because:",
         "options": ["it does not respire at all", "gases diffuse directly "
                     "across its cell surface", "it lives without oxygen",
                     "it breathes through villi"], "correct": 1},
        {"q": "Which pair of animal and respiratory organ is correct?",
         "options": ["fish – lungs", "earthworm – gills", "cockroach – "
                     "tracheae", "adult frog – gills only"], "correct": 2},
        {"q": "Bile contains no enzyme, yet it helps fat digestion by:",
         "options": ["breaking fat chemically", "breaking large fat drops into "
                     "tiny droplets so enzymes act faster", "absorbing the "
                     "fat", "turning fat solid"], "correct": 1},
        {"q": "If the liver stops making bile, the digestion of ___ will be "
         "most affected:",
         "options": ["starch", "proteins", "fats", "water"], "correct": 2},
        {"q": "The chief job of the large intestine is to:",
         "options": ["digest proteins", "absorb water from the undigested "
                     "food", "produce bile", "carry out breathing"],
         "correct": 1},
        {"q": "A fish taken out of water soon dies because its gills:",
         "options": ["get too cold", "collapse and cannot take oxygen from "
                     "air", "absorb too much oxygen", "freeze solid"],
         "correct": 1},
        {"q": "Animal A has a four-chambered stomach and chews cud; animal B "
         "swallows its prey whole. A and B are respectively:",
         "options": ["tiger and cow", "cow and snake", "snake and cow",
                     "both cows"], "correct": 1},
        {"q": "The main reason humans cannot live on grass like cattle is that "
         "humans lack:",
         "options": ["teeth", "a stomach", "the microbes that digest "
                     "cellulose", "saliva"], "correct": 2},
    ]},
    {"type": "assertion", "title": "Assertion–Reason", "marks_line": "1 × 3 = 3",
     "items": [
        {"a": "The inner wall of the small intestine bears millions of villi.",
         "r": "Villi increase the surface area for the absorption of digested "
              "food.", "answer": "A"},
        {"a": "Earthworms crawl out to the surface during heavy rain.",
         "r": "Waterlogged soil has little air, so they come up to breathe.",
         "answer": "A"},
        {"a": "Fish can breathe while staying under water.",
         "r": "Gills take up the oxygen dissolved in the water.",
         "answer": "A"},
    ]},
]


# ===========================================================================
# CH-10  LIFE PROCESSES IN PLANTS  (photosynthesis, nutrition, transport)
# ===========================================================================
PLNT_OBJECTIVE = [
    {"type": "mcq", "marks_line": "1 × 8 = 8", "items": [
        {"q": "The process by which green plants make their own food is:",
         "options": ["respiration", "photosynthesis", "transpiration",
                     "digestion"], "correct": 1},
        {"q": "The raw materials needed for photosynthesis are:",
         "options": ["oxygen and glucose", "carbon dioxide and water",
                     "nitrogen and water", "oxygen and water"], "correct": 1},
        {"q": "Photosynthesis takes place mainly in the ___ of a leaf, which "
         "contain chlorophyll:",
         "options": ["roots", "green cells", "flowers", "woody stem"],
         "correct": 1},
        {"q": "The tiny pores on a leaf through which gases are exchanged are "
         "called:",
         "options": ["villi", "stomata", "veins", "xylem"], "correct": 1},
        {"q": "Cuscuta (amarbel) has no green leaves and grows on other "
         "plants, taking food from them. Its nutrition is:",
         "options": ["autotrophic", "parasitic", "saprotrophic",
                     "insectivorous"], "correct": 1},
        {"q": "The pitcher plant traps and digests insects mainly to obtain:",
         "options": ["water", "sunlight", "nitrogen it cannot get from the "
                     "soil", "carbon dioxide"], "correct": 2},
        {"q": "Water and minerals absorbed by the roots are carried upward "
         "through tubes called:",
         "options": ["phloem", "xylem", "stomata", "veins"], "correct": 1},
        {"q": "The loss of water as vapour from the leaves of a plant is "
         "called:",
         "options": ["respiration", "transpiration", "photosynthesis",
                     "absorption"], "correct": 1},
    ]},
    {"type": "fill", "marks_line": "1 × 5 = 5", "items": [
        {"q": "The green pigment in leaves that traps sunlight is called "
         "______.", "answer": "chlorophyll"},
        {"q": "During photosynthesis, plants give out the gas ______.",
         "answer": "oxygen"},
        {"q": "Food made in the leaves is carried to the rest of the plant "
         "through the ______.", "answer": "phloem"},
        {"q": "Fungi that obtain food from dead and decaying matter show "
         "______ nutrition.", "answer": "saprotrophic"},
        {"q": "The alga and the fungus in a lichen live together for mutual "
         "benefit; this relationship is called ______.",
         "answer": "symbiosis (symbiotic nutrition)"},
    ]},
    {"type": "tf", "marks_line": "1 × 5 = 5", "items": [
        {"q": "Photosynthesis can take place only when sunlight is available.",
         "answer": True},
        {"q": "Plants respire only at night.", "answer": False},
        {"q": "Xylem carries food from the leaves to the rest of the plant.",
         "answer": False},
        {"q": "Insectivorous plants are non-green and cannot carry out "
         "photosynthesis.", "answer": False},
        {"q": "Transpiration helps to pull water upward from the roots to the "
         "leaves.", "answer": True},
    ]},
    {"type": "match", "marks_line": "1 × 4 = 4",
     "colA": ["Chlorophyll", "Stomata", "Xylem", "Phloem"],
     "colB": ["transport of food", "traps sunlight", "exchange of gases in "
              "the leaf", "transport of water and minerals"],
     "pairs": [(0, 1), (1, 2), (2, 3), (3, 0)]},
    {"type": "assertion", "marks_line": "1 × 3 = 3", "items": [
        {"a": "Leaves are called the food factories of a plant.",
         "r": "Photosynthesis takes place mainly in the leaves.",
         "answer": "A"},
        {"a": "Insectivorous plants trap and digest insects.",
         "r": "They grow in nitrogen-poor soil and obtain nitrogen from the "
              "insects.", "answer": "A"},
        {"a": "Desert plants such as cactus have very few, spiny leaves.",
         "r": "This increases the loss of water by transpiration.",
         "answer": "C"},
    ]},
]

PLNT_SUBJECTIVE = [
    {"type": "short", "title": "Very Short Answer", "marks_line": "1 × 5 = 5",
     "items": [
        {"q": "Name the green pigment that traps sunlight in a leaf.",
         "marks": 1, "lines": 1, "answer": ["Chlorophyll."]},
        {"q": "Name the gas released during photosynthesis.", "marks": 1,
         "lines": 1, "answer": ["Oxygen."]},
        {"q": "Name the tissue that carries water in a plant.", "marks": 1,
         "lines": 1, "answer": ["Xylem."]},
        {"q": "Name one insectivorous plant.", "marks": 1, "lines": 1,
         "answer": ["Pitcher plant (or Venus flytrap)."]},
        {"q": "What is the loss of water vapour from leaves called?",
         "marks": 1, "lines": 1, "answer": ["Transpiration."]},
    ]},
    {"type": "short", "title": "Short Answer", "marks_line": "2 × 5 = 10",
     "items": [
        {"q": "Write the word equation for photosynthesis.", "marks": 2,
         "lines": 3,
         "answer": ["Carbon dioxide + water --(sunlight, chlorophyll)--> "
                    "glucose (food) + oxygen."]},
        {"q": "Why are green plants called autotrophs?", "marks": 2,
         "lines": 3,
         "answer": ["Because they make their own food from simple substances "
                    "by photosynthesis, instead of taking ready-made food."]},
        {"q": "Give two differences between xylem and phloem.", "marks": 2,
         "lines": 3,
         "answer": ["Xylem carries water and minerals upward from the roots; "
                    "phloem carries the food made in the leaves to all parts "
                    "of the plant."]},
        {"q": "Why do insectivorous plants trap insects even though they are "
         "green?", "marks": 2, "lines": 3,
         "answer": ["They grow in soil poor in nitrogen; they make their own "
                    "food by photosynthesis but trap insects to get the "
                    "nitrogen they need."]},
        {"q": "State two ways in which transpiration is useful to a plant.",
         "marks": 2, "lines": 3,
         "answer": ["It helps pull water and minerals up from the roots, and "
                    "it cools the plant."]},
    ]},
    {"type": "long", "title": "Long Answer", "marks_line": "5 × 3 = 15",
     "items": [
        {"q": "Explain the process of photosynthesis, stating the raw "
         "materials, the conditions needed and the products formed.",
         "marks": 5, "lines": 6,
         "answer": ["In photosynthesis, green leaves use carbon dioxide (from "
                    "air, via stomata) and water (from the soil, via roots and "
                    "xylem) in the presence of sunlight and chlorophyll to "
                    "make glucose (food) and release oxygen."]},
        {"q": "Describe the modes of heterotrophic nutrition in plants "
         "(parasitic, insectivorous, saprotrophic, symbiotic) with one "
         "example of each.", "marks": 5, "lines": 6,
         "answer": ["Parasitic — takes food from a living host (Cuscuta). "
                    "Insectivorous — traps insects for nitrogen (pitcher "
                    "plant). Saprotrophic — feeds on dead/decaying matter "
                    "(mushroom/fungi). Symbiotic — two organisms live together "
                    "for mutual benefit (lichen: alga + fungus)."]},
        {"q": "Explain how water absorbed by the roots reaches the leaves at "
         "the top of a tall tree.", "marks": 5, "lines": 6,
         "answer": ["Root hairs absorb water and minerals from the soil; these "
                    "enter the xylem, which forms continuous tubes up the "
                    "stem. As water evaporates from the leaves (transpiration), "
                    "the pull created draws the water column up the xylem to "
                    "the leaves."]},
    ]},
    {"type": "short", "title": "Higher-Order Thinking (Give Reasons)",
     "marks_line": "2 × 2 = 4", "items": [
        {"q": "A potted plant is kept in a completely dark room for a week but "
         "watered daily. Will it stay healthy? Give a reason.", "marks": 2,
         "lines": 3,
         "answer": ["No. Without light it cannot photosynthesise, so it makes "
                    "no food and becomes weak (and may die)."]},
        {"q": "A cut stem is placed in red-coloured water. Explain why red "
         "streaks appear moving upward but not downward.", "marks": 2,
         "lines": 3,
         "answer": ["The xylem carries water upward from the roots to the "
                    "leaves, so the coloured water rises through the xylem and "
                    "does not go downward."]},
    ]},
]

PLNT_OLYMPIAD = [
    {"type": "mcq", "title": "Multiple Choice (Higher Order)",
     "marks_line": "1 × 14 = 14", "items": [
        {"q": "Part of a green leaf is covered with black paper and the plant "
         "is left in sunlight. On testing, the covered part shows no starch "
         "because:",
         "options": ["it had no water", "no light reached it, so no "
                     "photosynthesis", "it had no carbon dioxide", "it had no "
                     "chlorophyll"], "correct": 1},
        {"q": "A destarched plant is kept in sunlight in a jar containing a "
         "chemical that absorbs all the carbon dioxide. Its leaves make no "
         "starch because there is no:",
         "options": ["water", "light", "carbon dioxide for photosynthesis",
                     "oxygen"], "correct": 2},
        {"q": "Which of these is NOT needed for photosynthesis?",
         "options": ["carbon dioxide", "water", "sunlight", "oxygen"],
         "correct": 3},
        {"q": "At midnight, a leaf is mainly:",
         "options": ["taking in CO2 and giving out O2", "taking in O2 and "
                     "giving out CO2", "carrying out photosynthesis", "doing "
                     "nothing at all"], "correct": 1},
        {"q": "Cuscuta is yellow and leafless, so it must live on a host plant "
         "because it lacks:",
         "options": ["roots", "water", "chlorophyll to make its own food",
                     "stomata"], "correct": 2},
        {"q": "Rhizobium bacteria in the root nodules of a pea plant help it "
         "by:",
         "options": ["supplying water", "fixing nitrogen for the plant",
                     "trapping insects", "providing sunlight"], "correct": 1},
        {"q": "A complete ring of bark (with its phloem) is peeled off around "
         "a tree trunk. The tree may die because:",
         "options": ["water can no longer rise up", "the food made in the "
                     "leaves cannot travel down to the roots", "it can no "
                     "longer photosynthesise", "it loses all its leaves at "
                     "once"], "correct": 1},
        {"q": "On a hot, dry, windy day the rate of transpiration in a plant "
         "will:",
         "options": ["decrease", "increase", "stay the same", "fall to zero"],
         "correct": 1},
        {"q": "A plant lit only by green light grows poorly because "
         "chlorophyll:",
         "options": ["absorbs green light strongly", "mostly reflects green "
                     "light and absorbs red and blue", "needs no light at "
                     "all", "is destroyed by green light"], "correct": 1},
        {"q": "The gas bubbles rising from a water plant (Hydrilla) kept in "
         "bright sunlight are mainly:",
         "options": ["carbon dioxide", "oxygen", "nitrogen", "water vapour"],
         "correct": 1},
        {"q": "Which pair is correctly matched?",
         "options": ["xylem – carries food", "phloem – carries water",
                     "stomata – exchange of gases", "chlorophyll – "
                     "transpiration"], "correct": 2},
        {"q": "A mushroom growing on a rotting log obtains its food by:",
         "options": ["photosynthesis", "absorbing food from the dead log "
                     "(saprotrophic)", "trapping insects", "taking it from a "
                     "living plant"], "correct": 1},
        {"q": "If all the stomata of a leaf were sealed with grease, the plant "
         "would soon suffer because it could not:",
         "options": ["absorb water from the soil", "exchange gases or "
                     "transpire", "grow new roots", "make chlorophyll"],
         "correct": 1},
        {"q": "Of two lit plants, one has both surfaces of its leaves smeared "
         "with vaseline. Compared with the other, this plant will transpire:",
         "options": ["more", "much less", "exactly the same", "only at "
                     "night"], "correct": 1},
    ]},
    {"type": "assertion", "title": "Assertion–Reason", "marks_line": "1 × 3 = 3",
     "items": [
        {"a": "Green plants are called the producers of an ecosystem.",
         "r": "They make their own food by photosynthesis, and other "
              "organisms depend on them for food.", "answer": "A"},
        {"a": "Water can rise to the leaves at the top of a very tall tree.",
         "r": "The pull created by transpiration from the leaves draws water "
              "up the xylem.", "answer": "A"},
        {"a": "A pea plant can grow well even in nitrogen-poor soil.",
         "r": "Rhizobium bacteria in its root nodules fix nitrogen for the "
              "plant.", "answer": "A"},
    ]},
]


# ===========================================================================
# CH-12  TIME AND MOTION  (speed, units, pendulum, graphs, types of motion)
# ===========================================================================
TIME_OBJECTIVE = [
    {"type": "mcq", "marks_line": "1 × 8 = 8", "items": [
        {"q": "A car travels 240 km in 4 hours. Its average speed is:",
         "options": ["60 km/h", "240 km/h", "4 km/h", "96 km/h"],
         "correct": 0},
        {"q": "The SI unit of speed is:",
         "options": ["km/h", "m/s", "metre", "second"], "correct": 1},
        {"q": "A speed of 72 km/h is equal to:",
         "options": ["20 m/s", "72 m/s", "200 m/s", "7.2 m/s"], "correct": 0},
        {"q": "The time taken by a pendulum to complete one full oscillation "
         "is called its:",
         "options": ["frequency", "time period", "speed", "amplitude"],
         "correct": 1},
        {"q": "Which of these is an example of periodic motion?",
         "options": ["a car moving on a straight road", "the pendulum of a "
                     "wall clock", "a stone falling from a roof", "a bus "
                     "starting off"], "correct": 1},
        {"q": "On a distance–time graph, a horizontal line (parallel to the "
         "time axis) shows that the object is:",
         "options": ["moving fast", "moving slowly", "at rest", "speeding "
                     "up"], "correct": 2},
        {"q": "A body that covers equal distances in equal intervals of time "
         "is said to be in:",
         "options": ["non-uniform motion", "uniform motion", "circular "
                     "motion", "no motion"], "correct": 1},
        {"q": "The spinning blades of a moving fan show:",
         "options": ["rectilinear motion", "rotational (circular) motion",
                     "straight-line motion", "no motion"], "correct": 1},
    ]},
    {"type": "fill", "marks_line": "1 × 5 = 5", "items": [
        {"q": "Speed = distance ÷ ______.", "answer": "time"},
        {"q": "The device in a vehicle that measures its speed is the ______.",
         "answer": "speedometer"},
        {"q": "The device that records the total distance travelled by a "
         "vehicle is the ______.", "answer": "odometer"},
        {"q": "One complete to-and-fro movement of a pendulum is called one "
         "______.", "answer": "oscillation"},
        {"q": "If a body covers unequal distances in equal intervals of time, "
         "its motion is ______.", "answer": "non-uniform"},
    ]},
    {"type": "tf", "marks_line": "1 × 5 = 5", "items": [
        {"q": "A body moving with uniform speed covers equal distances in "
         "equal intervals of time.", "answer": True},
        {"q": "km/h is the SI unit of speed.", "answer": False},
        {"q": "The time period of a simple pendulum depends on its length.",
         "answer": True},
        {"q": "On a distance–time graph, a steeper line means a slower speed.",
         "answer": False},
        {"q": "The motion of a child on a swing is periodic.", "answer": True},
    ]},
    {"type": "match", "marks_line": "1 × 4 = 4",
     "colA": ["Speedometer", "Odometer", "Pendulum clock", "metre/second"],
     "colB": ["measures the distance travelled", "SI unit of speed",
              "measures speed", "uses periodic motion to keep time"],
     "pairs": [(0, 2), (1, 0), (2, 3), (3, 1)]},
    {"type": "assertion", "marks_line": "1 × 3 = 3", "items": [
        {"a": "A pendulum clock can be used to measure time.",
         "r": "A given simple pendulum takes the same time for each "
              "oscillation.", "answer": "A"},
        {"a": "On a distance–time graph, a straight slanting line shows "
              "uniform speed.",
         "r": "Equal distances are covered in equal intervals of time.",
         "answer": "A"},
        {"a": "A speed of 36 km/h is slower than a speed of 36 m/s.",
         "r": "1 m/s is greater than 1 km/h.", "answer": "A"},
    ]},
]

TIME_SUBJECTIVE = [
    {"type": "short", "title": "Very Short Answer", "marks_line": "1 × 5 = 5",
     "items": [
        {"q": "State the SI unit of speed.", "marks": 1, "lines": 1,
         "answer": ["Metre per second (m/s)."]},
        {"q": "Name the device used to measure the speed of a vehicle.",
         "marks": 1, "lines": 1, "answer": ["Speedometer."]},
        {"q": "Define the time period of a pendulum.", "marks": 1, "lines": 1,
         "answer": ["The time taken to complete one oscillation."]},
        {"q": "Write the formula for speed.", "marks": 1, "lines": 1,
         "answer": ["Speed = distance ÷ time."]},
        {"q": "Name the type of motion shown by a swinging pendulum.",
         "marks": 1, "lines": 1, "answer": ["Periodic (oscillatory) motion."]},
    ]},
    {"type": "short", "title": "Short Answer", "marks_line": "2 × 5 = 10",
     "items": [
        {"q": "A train covers 150 km in 3 hours. Calculate its speed.",
         "marks": 2, "lines": 3,
         "answer": ["Speed = distance ÷ time = 150 ÷ 3 = 50 km/h."]},
        {"q": "Convert 90 km/h into metres per second.", "marks": 2,
         "lines": 3,
         "answer": ["90 km/h = 90 × (1000/3600) = 90 × 5/18 = 25 m/s."]},
        {"q": "Give two differences between uniform and non-uniform motion.",
         "marks": 2, "lines": 3,
         "answer": ["In uniform motion equal distances are covered in equal "
                    "times (speed constant); in non-uniform motion unequal "
                    "distances are covered in equal times (speed changes)."]},
        {"q": "What is a simple pendulum? Name the factor that decides its "
         "time period.", "marks": 2, "lines": 3,
         "answer": ["A simple pendulum is a small heavy bob hung by a light "
                    "thread from a fixed point. Its time period depends on the "
                    "length of the thread."]},
        {"q": "How can the speed of a body be found from its distance–time "
         "graph?", "marks": 2, "lines": 3,
         "answer": ["By taking the ratio of the distance covered to the time "
                    "taken (the slope of the line): speed = distance ÷ "
                    "time."]},
    ]},
    {"type": "long", "title": "Long Answer", "marks_line": "5 × 3 = 15",
     "items": [
        {"q": "A body covers 60 m in the first 4 s, 40 m in the next 4 s and "
         "80 m in the next 4 s. Is its motion uniform or non-uniform? Find the "
         "total distance, total time and average speed.", "marks": 5,
         "lines": 6,
         "answer": ["Unequal distances in equal times, so the motion is "
                    "non-uniform. Total distance = 60 + 40 + 80 = 180 m; total "
                    "time = 12 s; average speed = 180 ÷ 12 = 15 m/s."]},
        {"q": "Describe how a simple pendulum can be used to measure time, "
         "defining oscillation and time period.", "marks": 5, "lines": 6,
         "answer": ["A pendulum swings to and fro regularly. One complete "
                    "to-and-fro movement is an oscillation, and the time for "
                    "one oscillation is the time period. Since each "
                    "oscillation of a given pendulum takes the same time, "
                    "counting oscillations lets us measure time (as in a "
                    "pendulum clock)."]},
        {"q": "With an example of each, explain the distance–time graph of a "
         "body (i) at rest, (ii) in uniform motion and (iii) in non-uniform "
         "motion.", "marks": 5, "lines": 6,
         "answer": ["At rest — a horizontal line (distance does not change). "
                    "Uniform motion — a straight slanting line (equal "
                    "distances in equal times). Non-uniform motion — a curved "
                    "line (unequal distances in equal times)."]},
    ]},
    {"type": "short", "title": "Higher-Order Thinking (Give Reasons)",
     "marks_line": "2 × 2 = 4", "items": [
        {"q": "Two cars start from the same point in the same direction; car A "
         "at 40 km/h and car B at 60 km/h. How far apart are they after "
         "2 hours?", "marks": 2, "lines": 3,
         "answer": ["A covers 80 km and B covers 120 km, so they are "
                    "120 − 80 = 40 km apart."]},
        {"q": "If the thread of a pendulum is shortened, will each oscillation "
         "take more or less time? Give a reason.", "marks": 2, "lines": 3,
         "answer": ["Less time — the time period decreases when the length of "
                    "the pendulum is reduced."]},
    ]},
]

TIME_OLYMPIAD = [
    {"type": "mcq", "title": "Multiple Choice (Higher Order)",
     "marks_line": "1 × 14 = 14", "items": [
        {"q": "A cyclist covers 3 km in 10 minutes. His speed is:",
         "options": ["18 km/h", "30 km/h", "0.3 km/h", "3 km/h"],
         "correct": 0},
        {"q": "A car moves at 15 m/s. The distance it covers in 2 minutes is:",
         "options": ["30 m", "1800 m", "450 m", "900 m"], "correct": 1},
        {"q": "A speed of 54 km/h is equal to:",
         "options": ["15 m/s", "54 m/s", "150 m/s", "5.4 m/s"], "correct": 0},
        {"q": "Two stations are 300 km apart. A train leaves at 8:00 a.m. and "
         "arrives at 12:00 noon. Its average speed is:",
         "options": ["75 km/h", "60 km/h", "300 km/h", "25 km/h"],
         "correct": 0},
        {"q": "On a distance–time graph, the line of body P is steeper than "
         "that of body Q. This means:",
         "options": ["P is slower than Q", "P is faster than Q", "both have "
                     "the same speed", "P is at rest"], "correct": 1},
        {"q": "A pendulum takes 40 s to complete 20 oscillations. Its time "
         "period is:",
         "options": ["2 s", "40 s", "20 s", "0.5 s"], "correct": 0},
        {"q": "A bus travels the first 60 km at 60 km/h and the next 60 km at "
         "30 km/h. Its average speed for the whole journey is:",
         "options": ["45 km/h", "40 km/h", "90 km/h", "30 km/h"],
         "correct": 1},
        {"q": "If the length of a pendulum is increased, its time period "
         "will:",
         "options": ["decrease", "increase", "stay the same", "become zero"],
         "correct": 1},
        {"q": "A body that stays at rest for 5 seconds is shown on a "
         "distance–time graph as:",
         "options": ["a slanting straight line", "a horizontal line", "a "
                     "vertical line", "a curve rising steeply"], "correct": 1},
        {"q": "A car's odometer reads 5642 km at the start of a trip and "
         "5792 km at the end, 3 hours later. Its average speed was:",
         "options": ["50 km/h", "150 km/h", "45 km/h", "1934 km/h"],
         "correct": 0},
        {"q": "Which of the following is the fastest?",
         "options": ["36 km/h", "12 m/s", "600 m/min", "1 km/min"],
         "correct": 3},
        {"q": "A runner completes one lap of a 400 m circular track in 50 s. "
         "Her speed is:",
         "options": ["8 m/s", "400 m/s", "50 m/s", "20 m/s"], "correct": 0},
        {"q": "A pendulum clock is running slow. To make it keep correct time, "
         "the length of its pendulum should be:",
         "options": ["increased", "decreased", "kept unchanged", "doubled"],
         "correct": 1},
        {"q": "Two buses start towards each other from towns 240 km apart, at "
         "40 km/h and 60 km/h. They meet after:",
         "options": ["2.4 hours", "4 hours", "6 hours", "3 hours"],
         "correct": 0},
    ]},
    {"type": "assertion", "title": "Assertion–Reason", "marks_line": "1 × 3 = 3",
     "items": [
        {"a": "On a distance–time graph, a horizontal line means the body is "
              "at rest.",
         "r": "For a body at rest the distance does not change with time.",
         "answer": "A"},
        {"a": "A speed of 72 km/h is the same as 20 m/s.",
         "r": "To convert km/h into m/s we multiply by 5/18.", "answer": "A"},
        {"a": "A simple pendulum is used in clocks to measure time.",
         "r": "Each oscillation of a given pendulum takes a different amount "
              "of time.", "answer": "C"},
    ]},
]


# ===========================================================================
# CHAPTER REGISTRY  (all five chapters)
# ===========================================================================
CHAPTERS = [
    dict(num="Ch-3", chapter="Heat", subject="Science — Physics",
         syllabus=HEAT_SYLL, objective=HEAT_OBJECTIVE,
         subjective=HEAT_SUBJECTIVE, olympiad=HEAT_OLYMPIAD),
    dict(num="Ch-6", chapter="Acids, Bases and Salts",
         subject="Science — Chemistry", syllabus="",
         objective=ACID_OBJECTIVE, subjective=ACID_SUBJECTIVE,
         olympiad=ACID_OLYMPIAD),
    dict(num="Ch-9", chapter="Life Processes in Animals",
         subject="Science — Biology", syllabus="",
         objective=ANIM_OBJECTIVE, subjective=ANIM_SUBJECTIVE,
         olympiad=ANIM_OLYMPIAD),
    dict(num="Ch-10", chapter="Life Processes in Plants",
         subject="Science — Biology", syllabus="",
         objective=PLNT_OBJECTIVE, subjective=PLNT_SUBJECTIVE,
         olympiad=PLNT_OLYMPIAD),
    dict(num="Ch-12", chapter="Time and Motion", subject="Science — Physics",
         syllabus="", objective=TIME_OBJECTIVE, subjective=TIME_SUBJECTIVE,
         olympiad=TIME_OLYMPIAD),
]


if __name__ == "__main__":
    build()
