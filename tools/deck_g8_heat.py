"""
Grade 8 Physics — Chapter: Heat Transfer.
S53 (effects of heat, molecular motion, evaporation, boiling) and
S54 (thermal expansion in solids, liquids and gases; density & temperature).
ICSE Class 8 (Selina) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade08"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Heat Transfer  •  ICSE Class 8 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["orange"])
    states = b.asset("g8ht_states", D.states_of_matter("g8ht_states"))
    hero = b.asset("g8_heat_hero", states)

    b.title("ICSE • Class 8 • Heat", "Heat, Molecules & Change of State",
            "Effects of heat  •  Molecular motion  •  Evaporation  •  Boiling",
            img=hero)
    b.objectives([
        "List the effects of heat on a body",
        "Explain how heat affects molecular motion",
        "Describe how a liquid changes into vapour",
        "Explain evaporation using molecular motion",
        "Describe boiling and explain it by molecular motion",
        "Distinguish evaporation from boiling",
    ])
    b.divider(1, "Part 1", "Heat & Molecular Motion",
              "What heat does to the particles of matter")
    b.cards("EFFECTS", "Effects of Heat", [
        ("Rise in temperature", "Heating usually makes a body hotter."),
        ("Expansion", "Most substances expand on heating."),
        ("Change of state", "Heat can melt a solid or boil a liquid."),
        ("Other changes", "Heat can also speed up reactions and cause "
         "chemical change."),
    ], notes="Survey the effects of heat: temperature rise, expansion, change "
             "of state. These set up the rest of the chapter.")
    b.text_image("MOLECULAR MOTION", "Heat and Molecular Motion",
                 ["All matter is made of tiny moving particles.",
                  "In a solid they vibrate in fixed positions; in a liquid "
                  "they slide past each other; in a gas they fly about "
                  "freely.",
                  "Heating gives the particles more energy, so they move "
                  "faster.",
                  "This faster motion is what we measure as a higher "
                  "temperature."],
                 states, img_side="right", img_w=6.0, img_h=3.0,
                 panel_title="Faster particles = hotter",
                 caption="Solid, liquid and gas particle arrangements",
                 notes="The molecular model: heat = faster particle motion. "
                       "Arrangement differs across the three states.")
    b.cards("THREE WAYS", "The Three Modes of Heat Transfer", [
        ("Conduction", "Heat passes through a solid from particle to particle, "
         "without the particles moving along."),
        ("Convection", "Heat moves through liquids and gases as warm, less "
         "dense fluid rises and cool fluid sinks."),
        ("Radiation", "Heat travels as invisible waves that need no medium — "
         "how the Sun's heat reaches us."),
        ("Hotter to colder", "In every mode, heat always flows from the hotter "
         "body to the colder one."),
    ], notes="The three modes: conduction (solids), convection (fluids), "
             "radiation (no medium). This is the heart of the Heat Transfer "
             "chapter.")
    b.bullets("CONDUCTION", "Conduction — Heat Through Solids", [
        ("How it works", "Heated particles vibrate harder and pass the energy "
         "to their neighbours."),
        ("Good conductors", "Metals like copper and aluminium carry heat "
         "quickly — used for cooking pans."),
        ("Poor conductors (insulators)", "Wood, plastic, air and water carry "
         "heat slowly — used for pan handles and warm clothing."),
        ("Everyday", "A metal spoon in hot tea soon feels hot; a wooden one "
         "does not."),
    ], panel_title="Particle to particle",
       notes="Conduction is mainly in solids. Metals conduct well; wood, "
             "plastic and trapped air are insulators.")
    b.bullets("CONVECTION & RADIATION", "Convection and Radiation", [
        ("Convection currents", "Warm fluid rises, cool fluid sinks, setting up "
         "a circulating current that carries heat."),
        ("Everyday convection", "Land and sea breezes, boiling water and room "
         "heaters all work by convection."),
        ("Radiation", "All hot bodies radiate heat as infrared waves; it needs "
         "no medium and crosses empty space."),
        ("Surfaces", "Dull black surfaces absorb and emit radiation best; "
         "shiny white surfaces reflect it."),
    ], panel_title="Moving fluids and invisible waves",
       notes="Convection: circulating fluid (breezes, heaters). Radiation: "
             "infrared, no medium; black absorbs/emits, shiny reflects.")
    b.cards("CHANGE OF STATE", "The Three Changes of State", [
        ("Melting", "A solid takes in heat and becomes a liquid (ice → "
         "water)."),
        ("Boiling / Evaporation", "A liquid takes in heat and becomes a vapour "
         "(water → steam)."),
        ("Condensation", "A vapour gives out heat and becomes a liquid (steam "
         "→ water)."),
        ("Freezing", "A liquid gives out heat and becomes a solid (water → "
         "ice)."),
    ], notes="The reversible changes of state. Taking in heat moves toward gas; "
             "giving out heat moves toward solid.")
    b.bullets("HEAT vs TEMPERATURE", "Heat is Not the Same as Temperature", [
        ("Heat", "A form of energy that flows from a hotter body to a cooler "
         "one."),
        ("Temperature", "How hot or cold a body is — it decides the direction "
         "of heat flow."),
        ("Different things", "A bucket of warm water holds more heat than a cup "
         "at the same temperature."),
        ("Units", "Heat is measured in joules; temperature in degrees "
         "Celsius."),
    ], panel_title="Energy vs hotness",
       notes="A common confusion: heat is energy (joules); temperature is how "
             "hot (°C). More mass at the same temperature holds more heat.")
    b.bullets("EVAPORATION", "Evaporation", [
        ("What it is", "The slow change of a liquid into vapour from its "
         "surface."),
        ("At any temperature", "It happens at all temperatures, not just at "
         "boiling point."),
        ("Molecular view", "The faster surface molecules escape into the air "
         "as vapour."),
        ("Cooling effect", "Because the fastest molecules leave, the liquid "
         "left behind cools down."),
    ], panel_title="A surface phenomenon",
       notes="Evaporation: surface only, any temperature, fast molecules "
             "escape, causing cooling.")
    b.bullets("BOILING", "Boiling", [
        ("What it is", "The rapid change of a liquid into vapour throughout "
         "the liquid."),
        ("Fixed temperature", "It occurs at a definite temperature, the "
         "boiling point."),
        ("Molecular view", "Enough heat makes molecules everywhere break free "
         "and form bubbles of vapour."),
        ("Constant while boiling", "The temperature stays the same while the "
         "liquid boils."),
    ], panel_title="Throughout the liquid",
       notes="Boiling: throughout the liquid, at a fixed temperature, with "
             "bubbles. Temperature is constant during boiling.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Hotter Particles", "When a substance is heated, its particles "
             "begin to:", ["Move more slowly", "Move faster and with more "
              "energy", "Stop moving", "Disappear"])
    b.quiz_a(1, "B. Move faster and with more energy",
             "Heating gives particles more energy, so they vibrate or move "
             "faster. This increased motion is what a higher temperature "
             "measures.")
    b.quiz_q(2, "Wet Cloth", "A wet cloth left in the breeze dries because of:",
             ["Boiling", "Evaporation from its surface", "Melting",
              "Condensation"])
    b.quiz_a(2, "B. Evaporation from its surface",
             "Water molecules at the cloth's surface escape into the air as "
             "vapour, even at ordinary temperature. This is evaporation, which "
             "needs no boiling.")
    b.quiz_q(3, "Cooling Effect", "Sweating cools our body because, as sweat "
             "evaporates, it:", ["Adds heat to the skin", "Takes heat from "
              "the skin as the fastest molecules escape", "Freezes the skin",
              "Has no effect"])
    b.quiz_a(3, "B. Takes heat from the skin",
             "When sweat evaporates, its most energetic molecules leave, "
             "carrying energy away. The skin loses heat and feels cooler — "
             "evaporation causes cooling.")
    b.quiz_q(4, "During Boiling", "While a pan of water is boiling steadily, "
             "its temperature:", ["Keeps rising", "Stays constant at the "
              "boiling point", "Falls", "Doubles"])
    b.quiz_a(4, "B. Stays constant at the boiling point",
             "Once boiling begins, the added heat goes into turning water into "
             "steam rather than raising the temperature, so the thermometer "
             "holds steady at the boiling point.")
    b.divider(2, "Part 2", "Evaporation vs Boiling",
              "Two ways a liquid becomes vapour")
    b.cards("DIFFERENCES", "Evaporation Compared With Boiling", [
        ("Where", "Evaporation is only at the surface; boiling is throughout "
         "the liquid."),
        ("Temperature", "Evaporation at any temperature; boiling at a fixed "
         "boiling point."),
        ("Speed", "Evaporation is slow and quiet; boiling is fast with "
         "bubbles."),
        ("Cooling", "Evaporation cools the liquid; boiling needs continuous "
         "heating."),
    ], notes="Side-by-side comparison — a very common exam table. Surface vs "
             "throughout, any temp vs fixed, slow vs bubbling.")
    b.cards("FASTER EVAPORATION", "What Speeds Up Evaporation", [
        ("Higher temperature", "Warmer liquid evaporates faster."),
        ("Larger surface area", "Spreading a liquid out makes it evaporate "
         "quicker."),
        ("Moving air / wind", "A breeze carries vapour away, speeding "
         "evaporation."),
        ("Lower humidity", "Dry air takes up vapour faster than damp air."),
    ], notes="Factors that speed evaporation — useful for explaining drying "
             "clothes and puddles.")
    b.cards("COOLING USES", "Cooling by Evaporation Around Us", [
        ("Sweating", "Evaporating sweat draws heat from the skin and cools the "
         "body."),
        ("Earthen pots", "Water seeping through the pores evaporates and keeps "
         "the water inside cool."),
        ("Desert coolers", "A fan blows air over wet pads; evaporation cools "
         "the room."),
        ("Spirit on skin", "Spirit evaporates very fast, feeling cold as it "
         "takes heat from the hand."),
    ], notes="Real-life cooling by evaporation — links the science to everyday "
             "experience.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Effects of heat", "temperature rise, expansion, change of state"),
        ("Molecular motion", "heating makes particles move faster"),
        ("Evaporation", "surface, any temperature, causes cooling"),
        ("Boiling", "throughout, fixed temperature, with bubbles"),
        ("Differences", "surface vs throughout; any temp vs fixed"),
        ("Faster evaporation", "heat, area, wind, dry air"),
    ], notes="Rapid recap; the evaporation-vs-boiling comparison is the key "
             "exam point.")
    b.quiz_intro("Quiz 2", "Final Check — Evaporation & Boiling", 5)
    b.quiz_q(1, "Dry Faster", "Clothes on a washing line dry fastest on a "
             "day that is:", ["Cold and still", "Warm and windy", "Cold and "
              "damp", "Warm and humid"])
    b.quiz_a(1, "B. Warm and windy",
             "Warmth gives the water molecules more energy to escape, and wind "
             "carries the vapour away. Both speed up evaporation, so clothes "
             "dry quickest on a warm, breezy day.")
    b.quiz_q(2, "Surface Only", "Which process happens ONLY at the surface of "
             "a liquid?", ["Boiling", "Evaporation", "Both", "Neither"])
    b.quiz_a(2, "B. Evaporation",
             "Evaporation occurs only at the exposed surface of a liquid. "
             "Boiling, by contrast, happens throughout the whole liquid with "
             "bubbles forming inside it.")
    b.quiz_q(3, "Earthen Pot", "Water stays cool in an earthen pot because "
             "water seeping through the pores:", ["Boils",
              "Evaporates, taking heat from the water inside", "Freezes",
              "Heats up"])
    b.quiz_a(3, "B. Evaporates, taking heat from the water inside",
             "Water that oozes to the outside of the porous pot evaporates, "
             "drawing heat from the water within. This cooling keeps the "
             "stored water refreshingly cool.")
    b.quiz_q(4, "Bubbles", "The bubbles that rise through a liquid during "
             "boiling are made of:", ["Air", "Vapour of the liquid itself",
              "Dust", "Light"])
    b.quiz_a(4, "B. Vapour of the liquid itself",
             "During boiling the liquid turns to vapour throughout, forming "
             "bubbles of its own vapour that rise and burst at the surface.")
    b.quiz_q(5, "Spread It Out", "A puddle of water spread thinly over a wide "
             "area evaporates faster mainly because of its:",
             ["Smaller surface area", "Larger surface area", "Lower "
              "temperature", "Greater depth"])
    b.quiz_a(5, "B. Larger surface area",
             "A bigger surface lets more molecules escape at once, so a thin, "
             "wide puddle evaporates faster than the same water in a deep, "
             "narrow container.")
    b.closing("Heat on the Move",
              "Heat speeds up the tiny particles of matter — enough to set "
              "them free as vapour, whether slowly or in a rolling boil.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["teal"])
    bim = b.asset("g8ht_bimetal", D.bimetallic_strip("g8ht_bimetal"))
    hero = b.asset("g8_heat_hero", bim)

    b.title("ICSE • Class 8 • Heat", "Thermal Expansion",
            "Expansion of solids, liquids & gases  •  Linear expansion  •  "
            "Density & temperature", img=hero)
    b.objectives([
        "Explain thermal expansion using molecular motion",
        "Describe the expansion of solids and linear expansion",
        "Describe the expansion of liquids",
        "Describe the expansion of gases",
        "Explain how density changes with temperature",
        "Give everyday applications of thermal expansion",
    ])
    b.divider(1, "Part 1", "Expansion of Solids, Liquids & Gases",
              "Why things grow when heated")
    b.statement("WHY EXPAND", "Why Substances Expand on Heating",
                "Heating makes the particles of a substance vibrate or move "
                "more, so they push a little further apart and the substance "
                "expands.",
                points=["More heat → more energetic particles → greater "
                        "spacing.",
                        "Gases expand the most, then liquids, then solids.",
                        "On cooling, the particles slow and the substance "
                        "contracts."],
                notes="Molecular explanation of expansion. Order: gases > "
                      "liquids > solids for the same temperature rise.")
    b.text_image("SOLIDS", "Expansion of Solids (Linear Expansion)",
                 ["A solid rod gets a little longer when heated — linear "
                  "expansion.",
                  "Different metals expand by different amounts.",
                  "A bimetallic strip uses this: two metals bonded together "
                  "bend when heated.",
                  "Bimetallic strips switch thermostats on and off."],
                 bim, img_side="right", img_w=6.0, img_h=3.0,
                 panel_title="The bimetallic strip",
                 caption="Unequal expansion makes the strip bend",
                 notes="Linear expansion of solids; the bimetallic strip "
                       "(unequal expansion) is the key application.")
    b.bullets("THREE KINDS", "Solids Expand in Three Ways", [
        ("Linear (length)", "A rod or wire gets longer — the simplest case to "
         "picture."),
        ("Superficial (area)", "A sheet or plate grows in length and breadth, "
         "so its area increases."),
        ("Cubical (volume)", "A block expands in all three directions, so its "
         "volume increases."),
        ("Same cause", "All three come from the particles vibrating more and "
         "pushing apart on heating."),
    ], panel_title="Length, area and volume",
       notes="Solids can expand in length, area or volume. All three arise from "
             "the same molecular cause.")
    b.cards("ALLOWING FOR IT", "Allowing for Expansion of Solids", [
        ("Railway lines", "Gaps are left between rails so they can expand on "
         "hot days."),
        ("Bridges", "Built with expansion joints and rollers at one end."),
        ("Overhead wires", "Strung loosely so they do not snap when they "
         "contract in winter."),
        ("Fitting rims", "A hot iron rim is slipped onto a wheel, then cooled "
         "to grip tightly."),
    ], notes="Engineering allows for solid expansion: rail gaps, bridge "
             "joints, loose wires, shrink-fitting.")
    b.bullets("LIQUIDS & GASES", "Expansion of Liquids and Gases", [
        ("Liquids", "Expand more than solids for the same temperature rise — "
         "used in thermometers."),
        ("Thermometer", "Mercury or coloured alcohol rises up the tube as it "
         "expands."),
        ("Gases", "Expand the most of all, and by a large amount."),
        ("Hot-air balloon", "Heated air expands, becomes lighter, and the "
         "balloon rises."),
    ], panel_title="Liquids expand more, gases most",
       notes="Liquids (thermometers) expand more than solids; gases (hot-air "
             "balloon) expand the most.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Expands Most", "For the same rise in temperature, which "
             "expands the most?", ["A solid", "A liquid", "A gas",
              "All equally"])
    b.quiz_a(1, "C. A gas",
             "Gases expand far more than liquids, and liquids more than "
             "solids, because gas particles are free to move much further "
             "apart when heated.")
    b.quiz_q(2, "Why Gaps?", "Gaps are left between railway rails so that on a "
             "hot day they can:", ["Contract", "Expand without buckling",
              "Conduct better", "Stay cool"])
    b.quiz_a(2, "B. Expand without buckling",
             "Heated metal rails lengthen. The gaps give them room to expand; "
             "without them the rails would press together and buckle out of "
             "shape.")
    b.quiz_q(3, "Thermometer", "A liquid-in-glass thermometer works because "
             "the liquid:", ["Boils as it warms", "Expands and rises up the "
              "tube as it warms", "Changes colour", "Freezes"])
    b.quiz_a(3, "B. Expands and rises up the tube",
             "As the temperature rises, the mercury or alcohol expands and "
             "moves further up the narrow tube. The height of the column shows "
             "the temperature.")
    b.quiz_q(4, "Bimetallic Bend", "A bimetallic strip bends on heating "
             "because its two metals have different:", ["Colours",
              "Amounts of expansion", "Weights", "Melting points"])
    b.quiz_a(4, "B. Amounts of expansion",
             "The two bonded metals expand unequally for the same heating. The "
             "one that expands more forces the strip to curve — used to switch "
             "thermostats.")
    b.divider(2, "Part 2", "Density and Temperature",
              "How heating changes density")
    b.statement("DENSITY", "How Density Changes With Temperature",
                "When a substance is heated it expands, so the same mass now "
                "fills a larger volume — its density falls.",
                formula="Density = mass / volume   (mass fixed, volume up → "
                        "density down)",
                points=["Heating expands the substance, lowering its density.",
                        "The warmer, less dense part tends to rise.",
                        "Cooling does the reverse: volume shrinks, density "
                        "rises."],
                notes="Heating lowers density (same mass, bigger volume). Warm "
                      "fluid rises — the basis of convection.")
    b.cards("USES & CARE", "Where Expansion Helps and Where It Harms", [
        ("Shrink fitting", "A hot metal ring slips onto a wheel, then grips "
         "tightly as it cools and contracts."),
        ("Riveting", "A red-hot rivet is hammered in; on cooling it shrinks and "
         "pulls the plates together."),
        ("Thermostats", "A bimetallic strip bends with temperature to switch a "
         "heater or iron on and off."),
        ("Care needed", "Bridges, rails and pipelines must leave room, or "
         "expansion can buckle and crack them."),
    ], notes="Expansion is both useful (shrink-fitting, riveting, thermostats) "
             "and a hazard to design around (bridges, rails).")
    b.cards("CONSEQUENCES", "Density Changes Around Us", [
        ("Hot-air balloon", "Heated air inside is less dense than the cool air "
         "outside, so the balloon floats up."),
        ("Sea breeze", "Warm, less dense air over land rises and cooler air "
         "flows in from the sea."),
        ("Convection currents", "Warm fluid rises and cool fluid sinks, "
         "carrying heat around."),
        ("Smoke rises", "Hot, low-density smoke and gases rise above the "
         "fire."),
    ], notes="Density-temperature effects: hot-air balloon, sea breeze, "
             "convection. Warm = less dense = rises.")
    b.statement("UNUSUAL WATER", "The Unusual Behaviour of Water",
                "Most liquids shrink steadily as they cool, but water behaves "
                "strangely between 4 °C and 0 °C — it expands instead of "
                "contracting.",
                points=["Water is densest at about 4 °C.",
                        "Cooled below 4 °C it expands, and on freezing it "
                        "expands further.",
                        "So ice is less dense than water and floats — letting "
                        "fish survive under a frozen surface."],
                notes="Anomalous expansion of water: densest at 4 °C, expands "
                      "below that, ice floats. Important for aquatic life.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Why expand", "heated particles push further apart"),
        ("Order", "gases expand most, then liquids, then solids"),
        ("Solids", "linear expansion; allow gaps in rails and bridges"),
        ("Bimetallic strip", "unequal expansion bends it (thermostats)"),
        ("Liquids & gases", "thermometers and hot-air balloons"),
        ("Density", "heating lowers density, so warm fluid rises"),
    ], notes="Rapid recap; the order of expansion and density-temperature link "
             "are the key points.")
    b.quiz_intro("Quiz 2", "Final Check — Expansion & Density", 5)
    b.quiz_q(1, "Balloon Rises", "A hot-air balloon rises because the heated "
             "air inside it is:", ["Heavier than the outside air",
              "Less dense than the cooler outside air", "At higher pressure",
              "Solid"])
    b.quiz_a(1, "B. Less dense than the cooler outside air",
             "Heating expands the air inside, lowering its density. Being "
             "lighter than the surrounding cool air, the balloon experiences "
             "an upthrust and floats upward.")
    b.quiz_q(2, "Density Falls", "When a fixed mass of metal is heated, its "
             "density:", ["Increases", "Decreases", "Stays the same",
              "Becomes zero"])
    b.quiz_a(2, "B. Decreases",
             "The metal expands, so the same mass now occupies a larger "
             "volume. Since density = mass/volume, a bigger volume means a "
             "lower density.")
    b.quiz_q(3, "Tight Lid", "A tight metal lid on a glass jar loosens when "
             "run under hot water because the metal:", ["Shrinks",
              "Expands more than the glass", "Melts", "Gets heavier"])
    b.quiz_a(3, "B. Expands more than the glass",
             "Metal expands more than glass for the same heating. The warmed "
             "lid grows slightly larger than the jar's neck, so it loosens and "
             "turns easily.")
    b.quiz_q(4, "Warm Air", "In a room, the warm air near a heater tends to:",
             ["Sink to the floor", "Rise toward the ceiling", "Stay still",
              "Turn into a solid"])
    b.quiz_a(4, "B. Rise toward the ceiling",
             "Warm air is less dense than the surrounding cooler air, so it "
             "rises. Cooler air sinks to replace it, setting up a convection "
             "current that spreads the heat.")
    b.quiz_q(5, "Best Thermometer Liquid", "A liquid is suitable for a "
             "thermometer mainly because it:", ["Does not expand",
              "Expands noticeably and evenly with temperature",
              "Is a solid", "Is coloured"])
    b.quiz_a(5, "B. Expands noticeably and evenly with temperature",
             "A thermometer liquid must expand by a clear, regular amount as "
             "the temperature rises, so its level gives an accurate reading. "
             "Mercury and alcohol do this well.")
    b.closing("Everything Expands",
              "Heat pushes particles apart — lengthening rails, lifting "
              "balloons and stirring the air into motion.")
    return b


def build():
    for fname, fn in [("G8_S53_Heat_Transfer_1.pptx", deck1),
                      ("G8_S54_Heat_Transfer_2.pptx", deck2)]:
        b = fn()
        issues = b.qa()
        b.save(os.path.join(OUT, fname))
        print(f"=== {fname} === slides: {len(b.prs.slides._sldIdLst)}")
        for i in issues:
            print("   -", i)
        if not issues:
            print("  QA: clean")


if __name__ == "__main__":
    build()
