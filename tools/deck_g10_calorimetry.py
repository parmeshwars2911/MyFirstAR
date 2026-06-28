"""
Grade 10 Physics — Chapter: Calorimetry.
S111 (heat vs temperature, heat capacity, specific heat capacity),
S112 (calorimeter, method of mixtures, change of phase: melting),
S113 (boiling, effect of pressure/impurities, latent heat).  ICSE Class 10.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade10"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Calorimetry  •  ICSE Class 10 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["orange"])
    hero = b.asset("g10_heat_hero", None)

    b.title("ICSE • Class 10 • Heat", "Heat & Specific Heat Capacity",
            "Heat vs temperature  •  Heat capacity  •  Specific heat capacity "
            " •  Q = m c ΔT", img=hero)
    b.objectives([
        "Distinguish heat from temperature",
        "List the factors that decide the heat absorbed by a body",
        "Define heat (thermal) capacity",
        "Define specific heat capacity and its unit",
        "Distinguish heat capacity from specific heat capacity",
        "Use the relation Q = m c ΔT",
    ])
    b.divider(1, "Part 1", "Heat and Temperature",
              "Two different ideas that are often confused")
    b.cards("TWO IDEAS", "Heat vs Temperature", [
        ("Heat", "A form of energy that flows from a hotter body to a colder "
         "one. Measured in joules."),
        ("Temperature", "How hot or cold a body is — what decides the "
         "direction of heat flow. Measured in °C or K."),
        ("Energy vs degree", "Heat is total thermal energy; temperature is the "
         "average energy per molecule."),
        ("A big example", "A bucket of warm water holds more heat than a "
         "red-hot spark, though the spark is hotter."),
    ], notes="The bucket-vs-spark example is the clearest way to separate heat "
             "(total energy) from temperature (degree of hotness).")
    b.statement("QUANTITY OF HEAT", "What Decides the Heat Absorbed",
                "The heat needed to warm a body depends on its mass, the "
                "material, and the temperature rise.",
                formula="Q  =  m c ΔT",
                points=["m = mass, c = specific heat capacity, ΔT = "
                        "temperature change.",
                        "More mass or a bigger temperature rise needs more "
                        "heat.",
                        "Different materials need different amounts of heat "
                        "(different c)."],
                notes="Introduce Q = mcΔT and name each term. Everything in "
                      "this chapter is built on this relation.")
    b.cards("DIFFERENCE", "Heat and Temperature Compared", [
        ("Heat flows", "Heat is energy on the move from hot to cold."),
        ("Temperature decides direction", "Heat always flows from higher to "
         "lower temperature."),
        ("Units", "Heat in joules (J); temperature in °C or kelvin (K)."),
        ("Measured by", "Heat by a calorimeter; temperature by a "
         "thermometer."),
    ], notes="Reinforce the distinction with units and instruments. "
             "Temperature difference, not heat content, drives the flow.")
    b.statement("HEAT CAPACITY", "Heat (Thermal) Capacity",
                "The heat capacity of a body is the heat needed to raise its "
                "temperature by 1°C (or 1 K).",
                formula="Heat capacity  =  Q / ΔT  =  m c        (unit: J/°C)",
                points=["It depends on both the mass and the material of the "
                        "body.",
                        "A large body has a large heat capacity.",
                        "Unit: joule per degree Celsius (J/°C) or J/K."],
                notes="Heat capacity is for the whole body (depends on mass). "
                      "Contrast with specific heat capacity next.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Hotter or More Heat?", "A cup of tea at 90°C and a bath of "
             "water at 40°C. Which statement is correct?",
             ["The tea contains more heat energy",
              "The bath contains more heat energy, though the tea is hotter",
              "Both contain the same heat", "Temperature equals heat"])
    b.quiz_a(1, "B. The bath contains more heat, though tea is hotter",
             "Temperature tells you how hot something is; heat depends also on "
             "mass. The large mass of bath water stores far more thermal "
             "energy than the small, hotter cup of tea.")
    b.quiz_q(2, "Direction of Flow", "Two bodies are placed in contact. Heat "
             "flows from one to the other until:", ["Their masses are equal",
              "Their heat capacities are equal",
              "They reach the same temperature", "All heat is destroyed"])
    b.quiz_a(2, "C. They reach the same temperature",
             "Heat flows from the hotter to the colder body. It stops when "
             "both are at the same temperature — thermal equilibrium — "
             "whatever their masses.")
    b.quiz_q(3, "More Heat Needed", "Which needs the MOST heat to warm it by "
             "10°C? (water has a high specific heat capacity)",
             ["1 kg of water", "1 kg of iron", "1 kg of copper",
              "1 kg of sand"])
    b.quiz_a(3, "A. 1 kg of water",
             "For equal masses and equal temperature rise, Q = mcΔT means the "
             "substance with the largest c needs the most heat. Water's "
             "specific heat capacity is far higher than metals or sand.")
    b.quiz_q(4, "Units", "The SI unit in which heat energy is measured is the:",
             ["Degree Celsius", "Kelvin", "Joule", "Watt"])
    b.quiz_a(4, "C. Joule",
             "Heat is a form of energy, so it is measured in joules. Degree "
             "Celsius and kelvin are units of temperature, and the watt is a "
             "unit of power.")
    b.divider(2, "Part 2", "Specific Heat Capacity",
              "The heat 'fingerprint' of a material")
    b.statement("SPECIFIC HEAT", "Specific Heat Capacity",
                "The specific heat capacity of a substance is the heat needed "
                "to raise the temperature of 1 kg of it by 1°C.",
                formula="c  =  Q / (m ΔT)        (unit: J / kg °C)",
                points=["It is a property of the material, not the size of the "
                        "body.",
                        "Water has a very high value: 4200 J/kg °C.",
                        "Metals have low values, so they heat up and cool down "
                        "quickly."],
                notes="Specific heat capacity is PER kilogram — a material "
                      "property. Water's high value is the headline fact.")
    b.cards("DISTINCTION", "Heat Capacity vs Specific Heat Capacity", [
        ("Heat capacity", "For the whole body; depends on mass; unit J/°C."),
        ("Specific heat capacity", "Per kilogram; a material property; unit "
         "J/kg°C."),
        ("Linked by mass", "Heat capacity = mass × specific heat capacity."),
        ("Example", "2 kg of water: c = 4200 J/kg°C, but heat capacity = "
         "8400 J/°C."),
    ], notes="The key link: heat capacity = m × c. One is for the object, the "
             "other for the material.")
    b.bullets("VALUES", "Specific Heat Capacities to Know", [
        ("Water", "4200 J/kg°C — unusually high; stores a lot of heat."),
        ("Ice", "about 2100 J/kg°C — roughly half that of water."),
        ("Aluminium", "about 900 J/kg°C."),
        ("Iron / steel", "about 450–500 J/kg°C — heats up quickly."),
        ("Copper", "about 390 J/kg°C — among the lowest."),
    ], panel_title="Water stands out",
       notes="Students should remember water = 4200. Metals are roughly "
             "ten-times smaller, hence quick to heat and cool.")
    b.worked("WORKED EXAMPLE", "Using Q = m c ΔT",
             "How much heat is needed to raise the temperature of 2 kg of "
             "water from 20°C to 70°C? (c_water = 4200 J/kg°C)",
             ["Q = m c ΔT",
              "ΔT = 70 − 20 = 50°C",
              "Q = 2 × 4200 × 50",
              "Q = 420,000 J = 420 kJ"],
             "Q = 420,000 J (420 kJ)",
             notes="Find ΔT first, then substitute. Encourage a kJ answer for "
                   "a sense of scale.")
    b.worked("WORKED EXAMPLE", "Finding the Temperature Rise",
             "5000 J of heat is given to 0.5 kg of aluminium "
             "(c = 900 J/kg°C). Find its temperature rise.",
             ["Q = m c ΔT   →   ΔT = Q / (m c)",
              "ΔT = 5000 / (0.5 × 900)",
              "ΔT = 5000 / 450 ≈ 11.1°C"],
             "Temperature rise ≈ 11.1°C",
             notes="Rearrange for ΔT. Note the same heat would warm metals far "
                   "more than water, because c is smaller.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Heat", "energy that flows from hot to cold; measured in joules"),
        ("Temperature", "degree of hotness; decides the direction of flow"),
        ("Q = m c ΔT", "heat depends on mass, material and temperature change"),
        ("Heat capacity", "Q/ΔT for the whole body; unit J/°C"),
        ("Specific heat capacity", "per kg material property; unit J/kg°C"),
        ("Water", "very high c = 4200 J/kg°C"),
    ], notes="Rapid recap; Q = mcΔT and the heat-capacity vs specific-heat "
             "distinction are the exam essentials.")
    b.quiz_intro("Quiz 2", "Final Check — Specific Heat", 5)
    b.quiz_q(1, "Heat Needed", "The heat required to raise 3 kg of water by "
             "10°C is (c = 4200 J/kg°C):", ["12,600 J", "42,000 J",
              "126,000 J", "1260 J"])
    b.quiz_a(1, "C. 126,000 J",
             "Q = mcΔT = 3 × 4200 × 10 = 126,000 J. Keep mass, c and ΔT in the "
             "right places.")
    b.quiz_q(2, "Quick to Heat", "Why does a metal spoon in hot soup become "
             "hot far quicker than the soup took to heat up?",
             ["Metal has a very high specific heat capacity",
              "Metal has a low specific heat capacity, so little heat raises "
              "its temperature a lot", "Metal makes its own heat",
              "Soup is colder than the spoon"])
    b.quiz_a(2, "B. Metal has a low specific heat capacity",
             "A small c means only a little heat is needed to raise the metal's "
             "temperature sharply. Water's high c is why the soup took much "
             "longer to warm.")
    b.quiz_q(3, "Heat Capacity", "The heat capacity of 4 kg of a substance of "
             "specific heat capacity 500 J/kg°C is:",
             ["125 J/°C", "2000 J/°C", "504 J/°C", "0.008 J/°C"])
    b.quiz_a(3, "B. 2000 J/°C",
             "Heat capacity = mass × specific heat capacity = 4 × 500 = "
             "2000 J/°C. It is the heat needed to warm the whole 4 kg by 1°C.")
    b.quiz_q(4, "Coastal Climate", "Places near the sea have milder weather "
             "than inland places mainly because water:",
             ["Reflects sunlight", "Has a high specific heat capacity, so it "
              "warms and cools slowly", "Is always cold",
              "Has no specific heat"])
    b.quiz_a(4, "B. High specific heat capacity warms/cools slowly",
             "The sea stores huge amounts of heat without large temperature "
             "swings, moderating the temperature of nearby land — warmer "
             "winters and cooler summers.")
    b.quiz_q(5, "Same Heat, Bigger Rise", "Equal masses of water and oil are "
             "given the same amount of heat. The oil (lower c) will show a:",
             ["Smaller temperature rise", "Greater temperature rise",
              "Equal temperature rise", "Fall in temperature"])
    b.quiz_a(5, "B. Greater temperature rise",
             "For the same heat and mass, ΔT = Q/(mc) is larger when c is "
             "smaller. Oil's lower specific heat capacity means it heats up "
             "more than water for the same energy.")
    b.closing("The Energy It Takes to Warm Things",
              "Q = m c ΔT — three letters that explain everything from a "
              "kettle to the climate by the sea.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["teal"])
    calo = D.calorimeter("g10cal_calo")
    curve = D.heating_curve("g10cal_curve2")
    hero = b.asset("g10_ice_hero", calo)

    b.title("ICSE • Class 10 • Heat", "Calorimetry & Melting",
            "The calorimeter  •  Method of mixtures  •  Change of phase  •  "
            "Melting & fusion", img=hero)
    b.objectives([
        "Describe a calorimeter and its use",
        "State the principle of the method of mixtures",
        "Solve mixing problems using heat lost = heat gained",
        "List consequences of water's high specific heat capacity",
        "Describe the change of phase from solid to liquid",
        "Explain the anomalous expansion of water on freezing",
    ])
    b.divider(1, "Part 1", "Measuring Heat: Method of Mixtures",
              "Using a calorimeter to find specific heat")
    b.text_image("CALORIMETER", "The Calorimeter",
                 ["A calorimeter is a copper vessel used to measure quantities "
                  "of heat.",
                  "Copper is used because of its low specific heat capacity "
                  "and good conduction.",
                  "It has a stirrer to share heat evenly and a thermometer to "
                  "read the temperature.",
                  "An insulating jacket reduces heat loss to the "
                  "surroundings."],
                 calo, img_side="right", img_w=4.6, img_h=3.8,
                 panel_title="Copper vessel, stirrer, thermometer",
                 caption="Lagging cuts heat loss to the surroundings",
                 notes="Explain each part and why copper is chosen. The "
                       "insulation matters for accurate results.")
    b.statement("METHOD OF MIXTURES", "Principle of the Method of Mixtures",
                "When a hot body is mixed with a cold one and no heat escapes, "
                "the heat lost by the hot body equals the heat gained by the "
                "cold one.",
                formula="Heat lost by hot body  =  Heat gained by cold body",
                points=["This is just the conservation of energy applied to "
                        "heat.",
                        "Each side is calculated as Q = m c ΔT.",
                        "It lets us find an unknown specific heat or final "
                        "temperature."],
                notes="The core principle: heat lost = heat gained. Set the two "
                      "mcΔT expressions equal and solve.")
    b.worked("WORKED EXAMPLE", "Method of Mixtures",
             "0.2 kg of water at 80°C is mixed with 0.3 kg of water at 20°C. "
             "Find the final temperature. (c cancels)",
             ["Heat lost by hot water = Heat gained by cold water",
              "0.2 × c × (80 − T) = 0.3 × c × (T − 20)",
              "0.2(80 − T) = 0.3(T − 20)  →  16 − 0.2T = 0.3T − 6",
              "22 = 0.5T  →  T = 44°C"],
             "Final temperature = 44°C",
             notes="Because both are water, c cancels. Set heat lost = heat "
                   "gained and solve for T. Check: 44°C lies between 20 and "
                   "80.")
    b.cards("WATER'S HIGH c", "Consequences of Water's High Specific Heat", [
        ("Coolant", "Water carries away a lot of heat, so it cools car engines "
         "and machinery."),
        ("Mild coastal climate", "The sea warms and cools slowly, moderating "
         "nearby weather."),
        ("Hot-water bottles", "Water stores a lot of heat and releases it "
         "slowly to keep us warm."),
        ("Body temperature", "The water in our bodies helps keep our "
         "temperature steady."),
    ], notes="All these follow from water needing lots of heat to change "
             "temperature. Coolant and climate are the favourites.")
    b.cards("EXAMPLES", "High and Low Heat Capacity", [
        ("Water — high", "Stores lots of heat; used in hot-water bottles and "
         "cooling systems."),
        ("Sand — lower", "Heats up and cools down quickly — beaches are hot by "
         "day, cold at night."),
        ("Land vs sea", "Land (lower capacity) heats faster than the sea, "
         "driving sea breezes."),
        ("Metals — low", "A metal pan heats almost at once; the water in it "
         "takes much longer."),
    ], notes="Contrast high (water) and low (sand, metals) heat capacity with "
             "everyday effects like sea breezes and beach sand.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Why Copper?", "A calorimeter is made of copper mainly "
             "because copper has:", ["A high specific heat capacity",
              "A low specific heat capacity and conducts heat well",
              "A shiny colour", "A high melting point"])
    b.quiz_a(1, "B. Low specific heat capacity and conducts well",
             "A low specific heat capacity means the calorimeter itself "
             "absorbs little heat, and good conduction lets it quickly share "
             "the temperature — both improve the accuracy of measurements.")
    b.quiz_q(2, "Heat Balance", "When a hot metal is dropped into cold water "
             "in an ideal (perfectly insulated) calorimeter:",
             ["The water loses heat to the metal",
              "Heat lost by the metal equals heat gained by the water",
              "Both gain heat", "No heat moves"])
    b.quiz_a(2, "B. Heat lost by metal = heat gained by water",
             "With no heat escaping, energy is conserved: every joule the hot "
             "metal loses is gained by the cooler water until both reach the "
             "same temperature.")
    b.quiz_q(3, "Final Temperature", "Equal masses of water at 30°C and 50°C "
             "are mixed. The final temperature will be:",
             ["30°C", "40°C", "50°C", "80°C"])
    b.quiz_a(3, "B. 40°C",
             "For equal masses of the same liquid, the final temperature is "
             "simply the average: (30 + 50)/2 = 40°C. Heat lost by the hotter "
             "equals heat gained by the cooler.")
    b.quiz_q(4, "Engine Coolant", "Water is used as a coolant in car engines "
             "because it:", ["Boils very easily",
              "Can absorb a large amount of heat for a small temperature rise",
              "Is a metal", "Freezes quickly"])
    b.quiz_a(4, "B. Absorbs a lot of heat for a small temperature rise",
             "Water's high specific heat capacity lets it carry away a great "
             "deal of engine heat while warming only modestly, making it an "
             "excellent coolant.")
    b.quiz_q(5, "Sea Breeze", "During the day a cool breeze blows from the sea "
             "to the land because the land:",
             ["Has a higher specific heat capacity than the sea",
              "Heats up faster than the sea, so warm air rises over it and "
              "cool sea air flows in", "Is colder than the sea",
              "Reflects more sunlight"])
    b.quiz_a(5, "B. Heats up faster than the sea",
             "Land has a lower heat capacity, so it warms quickly in the Sun. "
             "The hot air above it rises, and cooler air from over the slower-"
             "warming sea flows in to replace it — the sea breeze.")
    b.divider(2, "Part 2", "Change of Phase: Melting",
              "Solid to liquid, and water's odd behaviour")
    b.bullets("CHANGE OF PHASE", "Solid, Liquid, Gas", [
        ("Change of phase", "Matter can change between solid, liquid and gas "
         "states when heated or cooled."),
        ("Melting", "Solid → liquid, at the melting point."),
        ("Constant temperature", "During melting the temperature stays the "
         "same even as heat is added."),
        ("Where the heat goes", "The heat breaks the bonds holding the solid "
         "together — latent heat."),
    ], panel_title="Heating can change the state",
       notes="Set up phase change. The key surprise: temperature is constant "
             "during melting; heat goes into breaking bonds.")
    b.text_image("HEATING CURVE", "Heating Curve of Ice",
                 ["Heat ice and its temperature rises until it reaches 0°C.",
                  "At 0°C the temperature stays constant while the ice melts — "
                  "a flat plateau.",
                  "All the heat supplied then goes to melting, not to raising "
                  "temperature.",
                  "Once melted, the water's temperature rises again."],
                 curve, img_side="left", img_w=6.0, img_h=3.6,
                 panel_title="A flat step at the melting point",
                 caption="Temperature is constant while ice melts",
                 notes="Read the first plateau of the curve. Stress the flat "
                       "part: added heat melts the ice without warming it.")
    b.bullets("ANOMALOUS WATER", "Water Expands When It Freezes", [
        ("Most substances shrink", "Almost all liquids contract when they "
         "solidify."),
        ("Water is different", "Water expands as it freezes, so ice is less "
         "dense than water."),
        ("Ice floats", "Because ice is less dense, it floats on water."),
        ("Life under ice", "A floating ice layer insulates the water below, "
         "letting fish survive a frozen winter."),
    ], panel_title="The anomalous expansion of water",
       notes="Water's expansion on freezing is unusual and vital — floating "
             "ice protects aquatic life. Also why pipes burst in winter.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Calorimeter", "copper vessel + stirrer + thermometer + lagging"),
        ("Method of mixtures", "heat lost by hot = heat gained by cold"),
        ("Water's high c", "coolant, mild climates, steady body temperature"),
        ("Melting", "solid → liquid at constant temperature"),
        ("Heating curve", "flat plateau while ice melts"),
        ("Anomalous water", "expands on freezing, so ice floats"),
    ], notes="Rapid recap; method of mixtures and the melting plateau are the "
             "key ideas.")
    b.quiz_intro("Quiz 2", "Final Check — Mixing & Melting", 5)
    b.quiz_q(1, "Where Did Heat Go?", "While ice is melting at 0°C, heat is "
             "still being supplied, yet the thermometer reading does not "
             "change. The heat is being used to:",
             ["Raise the temperature", "Break the bonds and change ice to "
              "water", "Cool the surroundings", "Create new ice"])
    b.quiz_a(1, "B. Break the bonds and change ice to water",
             "During melting the supplied heat (latent heat) goes into "
             "separating the molecules of the solid, not into raising the "
             "temperature — so the reading stays at 0°C until all the ice has "
             "melted.")
    b.quiz_q(2, "Mixing Unequal", "0.1 kg of water at 90°C is added to 0.4 kg "
             "of water at 15°C. The final temperature is closest to:",
             ["52°C", "30°C", "75°C", "15°C"])
    b.quiz_a(2, "B. 30°C",
             "Heat lost = heat gained: 0.1(90 − T) = 0.4(T − 15). So "
             "9 − 0.1T = 0.4T − 6, giving 0.5T = 15, T = 30°C. The larger cold "
             "mass pulls the result down toward 15°C.")
    b.quiz_q(3, "Frozen Pond", "Fish survive in a pond that freezes over "
             "because:", ["Ice sinks and warms the bottom",
              "Ice floats and insulates the water below, which stays liquid",
              "Fish do not need water", "The whole pond freezes solid"])
    b.quiz_a(3, "B. Floating ice insulates the water below",
             "Water expands on freezing, so the ice is less dense and floats. "
             "This ice layer insulates the water beneath, which remains liquid "
             "and lets fish survive the winter.")
    b.quiz_q(4, "Burst Pipes", "Water pipes sometimes burst in very cold "
             "weather because water:", ["Contracts when it freezes",
              "Expands when it freezes, pushing the pipe apart",
              "Evaporates in the pipe", "Becomes heavier"])
    b.quiz_a(4, "B. Expands when it freezes",
             "Unlike most liquids, water expands as it turns to ice. Trapped "
             "in a pipe, the expanding ice exerts a large force that can crack "
             "or burst the pipe.")
    b.quiz_q(5, "Stirrer's Job", "Why does a calorimeter have a stirrer?",
             ["To add heat", "To spread the heat evenly so the thermometer "
              "reads the true temperature", "To cool the water",
              "To measure mass"])
    b.quiz_a(5, "B. To spread heat evenly for a true reading",
             "Stirring mixes the contents so the temperature is uniform "
             "throughout. Then the thermometer reads the genuine common "
             "temperature, improving accuracy.")
    b.closing("Heat That Hides in a Change of State",
              "From mixing hot and cold to melting ice — energy is always "
              "conserved, even when the thermometer stands still.")
    return b


def deck3():
    b = Builder(FOOTER, accent=C["purple"])
    curve = D.heating_curve("g10cal_curve3")
    hero = b.asset("g10_heat_hero", curve)

    b.title("ICSE • Class 10 • Heat", "Boiling & Latent Heat",
            "Boiling  •  Effect of pressure & impurities  •  Latent heat  •  "
            "Specific latent heat", img=hero)
    b.objectives([
        "Describe boiling and read the heating curve of water",
        "Explain the effect of pressure on melting and boiling points",
        "Explain the effect of impurities on melting and boiling points",
        "Define latent heat and specific latent heat",
        "Explain latent heat using the kinetic (molecular) model",
        "State consequences of water's high latent heat of fusion",
    ])
    b.divider(1, "Part 1", "Boiling, Pressure & Impurities",
              "What changes the melting and boiling points")
    b.statement("BOILING", "Vaporisation and Boiling",
                "Boiling is the rapid change of a liquid into vapour "
                "throughout the liquid, at a fixed temperature called the "
                "boiling point.",
                points=["For water at normal pressure the boiling point is "
                        "100°C.",
                        "During boiling the temperature stays constant though "
                        "heat is supplied.",
                        "The heat supplied becomes the latent heat of "
                        "vaporisation."],
                notes="Boiling happens at a fixed temperature, constant while "
                      "heat is added. Distinguish from evaporation (surface, "
                      "any temperature).")
    b.text_image("HEATING CURVE", "Heating Curve of Water",
                 ["Heating water raises its temperature until it reaches "
                  "100°C.",
                  "At 100°C the temperature stays constant while the water "
                  "boils — a second plateau.",
                  "All the heat then goes into turning water into steam.",
                  "The two flat steps (melting and boiling) are where latent "
                  "heat is absorbed."],
                 curve, img_side="right", img_w=6.0, img_h=3.6,
                 panel_title="Two plateaus: melting and boiling",
                 caption="Temperature is constant while water boils",
                 notes="Show both plateaus. The flat sections are latent-heat "
                       "regions — temperature constant, heat still flowing in.")
    b.bullets("PRESSURE", "Effect of Pressure", [
        ("Boiling point rises with pressure", "Higher pressure makes water "
         "boil above 100°C — used in a pressure cooker to cook faster."),
        ("Boiling point falls with low pressure", "On a high mountain, lower "
         "pressure makes water boil below 100°C, so food cooks slowly."),
        ("Melting point of ice falls with pressure", "Extra pressure lowers "
         "the melting point of ice slightly."),
        ("Regelation", "Ice can melt under pressure and re-freeze when the "
         "pressure is removed."),
    ], panel_title="Pressure changes the change-points",
       notes="Pressure raises the boiling point (cooker) but lowers the "
             "melting point of ice (regelation). Mountain cooking is a great "
             "example.")
    b.bullets("IMPURITIES", "Effect of Impurities", [
        ("Lower the melting point", "Salt sprinkled on icy roads makes the ice "
         "melt below 0°C."),
        ("Raise the boiling point", "Dissolving salt makes water boil above "
         "100°C."),
        ("Why salt on roads", "It keeps water liquid below 0°C, clearing ice "
         "in winter."),
        ("Antifreeze", "Added to car radiators to stop the water freezing in "
         "cold weather."),
    ], panel_title="Impurities widen the liquid range",
       notes="Impurities lower the melting point and raise the boiling point — "
             "salt on roads and antifreeze are the standard examples.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Pressure Cooker", "Food cooks faster in a pressure cooker "
             "because the raised pressure inside:",
             ["Lowers the boiling point of water",
              "Raises the boiling point, so the water and steam are hotter",
              "Removes all the water", "Cools the food"])
    b.quiz_a(1, "B. Raises the boiling point, so it gets hotter",
             "Higher pressure pushes the boiling point above 100°C, so the "
             "water and steam reach a higher temperature and cook the food "
             "more quickly.")
    b.quiz_q(2, "Mountain Tea", "On a high mountain, water boils at about "
             "90°C. As a result:", ["Tea is hotter than usual",
              "Food takes longer to cook because the water is not as hot",
              "Water cannot boil at all", "The boiling point is unchanged"])
    b.quiz_a(2, "B. Food cooks more slowly",
             "Lower air pressure at altitude lowers the boiling point, so the "
             "boiling water is cooler than 100°C and cooks food more slowly.")
    b.quiz_q(3, "Salt on Roads", "Salt is spread on icy roads in winter "
             "because it:", ["Raises the melting point of ice",
              "Lowers the melting point, so the ice melts below 0°C",
              "Makes the ice harder", "Warms the road"])
    b.quiz_a(3, "B. Lowers the melting point of ice",
             "Salt is an impurity that lowers the melting point of ice, so it "
             "melts even when the temperature is a little below 0°C, clearing "
             "the road.")
    b.quiz_q(4, "Boiling vs Evaporation", "Which is true of boiling but NOT "
             "of evaporation?", ["It happens only at the surface",
              "It occurs at any temperature", "It happens throughout the "
              "liquid at a fixed temperature", "It cools the liquid"])
    b.quiz_a(4, "C. Throughout the liquid at a fixed temperature",
             "Boiling occurs all through the liquid at one fixed temperature "
             "(the boiling point). Evaporation happens only at the surface and "
             "at any temperature.")
    b.divider(2, "Part 2", "Latent Heat",
              "The hidden heat of a change of state")
    b.statement("LATENT HEAT", "Latent Heat",
                "Latent heat is the heat absorbed or released during a change "
                "of state, WITHOUT any change in temperature.",
                formula="Q  =  m L        (L = specific latent heat, J/kg)",
                points=["'Latent' means hidden — the heat is stored in "
                        "changing the state, not raising the temperature.",
                        "Specific latent heat L is the heat per kilogram for "
                        "the change of state.",
                        "Fusion = solid↔liquid; vaporisation = liquid↔gas."],
                notes="Latent = hidden heat at constant temperature. Q = mL is "
                      "the working formula. Define fusion and vaporisation.")
    b.bullets("VALUES", "Specific Latent Heats of Water", [
        ("Fusion (melting)", "L_fusion of ice ≈ 336,000 J/kg "
         "(3.36 × 10⁵ J/kg)."),
        ("Vaporisation (boiling)", "L_vap of water ≈ 2,260,000 J/kg "
         "(2.26 × 10⁶ J/kg)."),
        ("Why so big", "A lot of energy is needed to fully separate the "
         "molecules."),
        ("Q = m L", "Heat for a change of state = mass × specific latent "
         "heat."),
    ], panel_title="Hidden heat per kilogram",
       notes="Students should know the two values. Vaporisation needs far more "
             "than fusion — molecules must be fully separated.")
    b.bullets("KINETIC MODEL", "Latent Heat and the Molecular Model", [
        ("Melting", "Heat gives molecules enough energy to break free of their "
         "fixed positions, so the solid becomes a liquid."),
        ("No temperature rise", "The energy goes into loosening bonds, not "
         "into faster motion, so the temperature is unchanged."),
        ("Boiling", "Even more energy fully separates the molecules into a "
         "gas."),
        ("On cooling", "The same latent heat is released when a gas condenses "
         "or a liquid freezes."),
    ], panel_title="Where the hidden heat goes",
       notes="Use the molecular picture: latent heat breaks bonds rather than "
             "speeding molecules up — hence constant temperature.")
    b.worked("WORKED EXAMPLE", "Heat to Melt Ice",
             "How much heat is needed to melt 0.5 kg of ice at 0°C into water "
             "at 0°C? (L_fusion = 336,000 J/kg)",
             ["Q = m L",
              "Q = 0.5 × 336,000",
              "Q = 168,000 J"],
             "Q = 168,000 J (168 kJ)",
             notes="Pure phase change at 0°C, so use Q = mL only — no mcΔT "
                   "term because the temperature does not change.")
    b.cards("CONSEQUENCES", "Why Water's Latent Heat of Fusion Matters", [
        ("Ice cools drinks well", "Melting ice absorbs a lot of heat from the "
         "drink, cooling it effectively."),
        ("Ice keeps food cold", "It absorbs heat slowly as it melts, keeping "
         "an ice-box cold for hours."),
        ("Snow melts slowly", "The large latent heat means snow and ice take a "
         "long time to melt in spring."),
        ("Frost protection", "Water released onto crops gives out latent heat "
         "as it freezes, protecting them from frost."),
    ], notes="High latent heat of fusion makes ice a powerful, long-lasting "
             "coolant and explains slow spring thaws.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Boiling", "fixed temperature; constant while heat is supplied"),
        ("Pressure", "raises boiling point (cooker), lowers melting point of "
         "ice"),
        ("Impurities", "lower the melting point, raise the boiling point"),
        ("Latent heat", "heat for a change of state at constant temperature; "
         "Q = m L"),
        ("Values", "fusion 3.36 × 10⁵ J/kg; vaporisation 2.26 × 10⁶ J/kg"),
        ("Kinetic model", "latent heat breaks bonds, not raising temperature"),
    ], notes="Rapid recap; Q = mL and the pressure/impurity effects are the "
             "key exam points.")
    b.quiz_intro("Quiz 2", "Final Check — Latent Heat", 5)
    b.quiz_q(1, "Worse Burn", "Steam at 100°C causes a far worse burn than "
             "water at 100°C because the steam:",
             ["Is hotter than the water",
              "Releases its large latent heat of vaporisation as it condenses "
              "on the skin", "Moves faster", "Contains more salt"])
    b.quiz_a(1, "B. Releases its latent heat as it condenses",
             "Both are at 100°C, but when steam condenses on the skin it gives "
             "up its huge latent heat of vaporisation (2.26 × 10⁶ J/kg) on top "
             "of cooling — delivering much more heat than hot water alone.")
    b.quiz_q(2, "Melt the Ice", "The heat needed to melt 2 kg of ice at 0°C "
             "is (L = 3.36 × 10⁵ J/kg):", ["1.68 × 10⁵ J",
              "6.72 × 10⁵ J", "3.36 × 10⁵ J", "672 J"])
    b.quiz_a(2, "B. 6.72 × 10⁵ J",
             "Q = mL = 2 × 3.36 × 10⁵ = 6.72 × 10⁵ J. No temperature change, "
             "so only the latent-heat term is needed.")
    b.quiz_q(3, "Constant Temperature", "While a pure substance is changing "
             "state, the heat supplied causes:", ["A rise in temperature",
              "No change in temperature, only a change of state",
              "A fall in temperature", "The substance to disappear"])
    b.quiz_a(3, "B. No temperature change, only a change of state",
             "During a change of state the heat is latent — it goes into "
             "rearranging the molecules, not into raising the temperature, so "
             "the thermometer reading stays fixed.")
    b.quiz_q(4, "Best Coolant", "To cool a drink, 100 g of ice at 0°C works "
             "better than 100 g of water at 0°C because the ice:",
             ["Is colder", "Must first absorb its latent heat of fusion to "
              "melt, taking extra heat from the drink", "Is heavier",
              "Floats"])
    b.quiz_a(4, "B. Absorbs latent heat of fusion as it melts",
             "Both start at 0°C, but the ice must absorb a large latent heat "
             "to melt before it can warm up. That extra heat is taken from the "
             "drink, cooling it much more effectively.")
    b.quiz_q(5, "Sea-Breeze Pressure", "Increasing the pressure on a sample of "
             "ice will:", ["Raise its melting point",
              "Lower its melting point slightly so it melts more easily",
              "Have no effect", "Turn it straight to steam"])
    b.quiz_a(5, "B. Lower its melting point slightly",
             "Unusually, increasing the pressure lowers the melting point of "
             "ice (because ice contracts on melting). This is the basis of "
             "regelation, where ice melts under pressure and refreezes after.")
    b.closing("The Hidden Heat of Change",
              "Latent heat keeps temperatures steady through melting and "
              "boiling — the quiet physics behind ice, steam and the weather.")
    return b


def build():
    for fname, fn in [("G10_S111_Calorimetry_1.pptx", deck1),
                      ("G10_S112_Calorimetry_2.pptx", deck2),
                      ("G10_S113_Calorimetry_3.pptx", deck3)]:
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
