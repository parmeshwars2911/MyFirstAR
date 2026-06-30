"""
Grade 10 Physics — Thermal Physics (TN board Unit 3).
Built from the supplied chapter PDF, split into two teaching decks:
  Deck 1 (first half)  — temperature, scales, thermal equilibrium, thermal
                         energy & its features, units, and thermal expansion.
  Deck 2 (second half) — the gas laws (Boyle, Charles, Avogadro), real vs
                         ideal gases, and the ideal gas equation PV = RT.
Same house config as the other Grade-10 decks (16:9, no footer, logo space,
two quizzes with mirrored answer reveals, SVG schematics, speaker notes only).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams_thermal as DT

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade10"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Thermal Physics  •  Class 10 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["orange"])
    equil = b.asset("g10tp_equil", DT.thermal_equilibrium("g10tp_equil"))
    exp = b.asset("g10tp_expansion", DT.expansion_types("g10tp_expansion"))
    flask = b.asset("g10tp_realapp", DT.real_apparent_expansion("g10tp_realapp"))

    b.title("Class 10 • Thermal Physics", "Heat & Expansion",
            "Temperature & the kelvin scale  •  Thermal equilibrium  •  "
            "Thermal energy  •  Expansion of substances", img=exp)
    b.objectives([
        "Define temperature and the absolute (kelvin) scale",
        "Convert between Celsius, Kelvin and Fahrenheit",
        "Explain thermal equilibrium and thermal energy",
        "State the characteristic features of heat transfer",
        "Classify the thermal expansion of solids, liquids and gases",
        "Distinguish real expansion from apparent expansion",
    ])
    b.divider(1, "Part 1", "Temperature & Thermal Energy",
              "Hotness, the kelvin scale and the flow of heat")
    b.statement("TEMPERATURE", "What Is Temperature?",
                "Temperature is the degree of hotness of a body — the property "
                "that decides the direction in which heat flows.",
                points=["It tells us whether a body is in thermal equilibrium "
                        "with its surroundings.",
                        "It is a scalar quantity related to the average kinetic "
                        "energy of the molecules.",
                        "SI unit: the kelvin (K); other units are °C and °F."],
                notes="Temperature = degree of hotness and decides heat-flow "
                      "direction. SI unit kelvin; relate to average molecular "
                      "kinetic energy.")
    b.statement("ABSOLUTE SCALE", "The Absolute (Kelvin) Scale",
                "Temperature measured from absolute zero on the kelvin scale is "
                "the absolute or thermodynamic temperature.",
                formula="0 K = −273 °C (absolute zero)   •   a change of 1 °C = "
                        "a change of 1 K",
                points=["Each kelvin is 1/273.16 of the thermodynamic "
                        "temperature of the triple point of water.",
                        "Absolute zero (0 K) is the lowest possible "
                        "temperature.",
                        "Because the degree size is the same, ΔT is identical "
                        "in °C and K."],
                notes="Kelvin scale starts at absolute zero (−273 °C). Same "
                      "degree size as Celsius, so temperature DIFFERENCES are "
                      "equal in both.")
    b.statement("CONVERTING", "Relating the Temperature Scales",
                "The three scales are connected by simple relations.",
                formula="K = °C + 273      •      K = (°F + 460) × 5/9",
                points=["Celsius → Kelvin: add 273.",
                        "Fahrenheit → Kelvin: add 460, then multiply by 5/9.",
                        "0 K corresponds to −273 °C."],
                notes="Give the two conversion relations from the text. Most "
                      "numericals just need K = °C + 273.")
    b.worked("WORKED EXAMPLE", "Celsius to Kelvin",
             "Normal human body temperature is about 37 °C. Express it on the "
             "kelvin scale.",
             ["K = °C + 273",
              "K = 37 + 273",
              "K = 310 K"],
             "Body temperature ≈ 310 K",
             notes="Straight application of K = °C + 273. Remind students "
                   "kelvin values are never negative for real bodies.")
    b.text_image("THERMAL EQUILIBRIUM", "Thermal Equilibrium",
                 ["Two bodies are in thermal equilibrium if there is no net "
                  "flow of heat between them.",
                  "Place a hot and a cold body in contact: heat flows from hot "
                  "to cold.",
                  "The hot body cools and the cold body warms until both reach "
                  "the same temperature.",
                  "At that point they are in thermal equilibrium."],
                 equil, img_side="right", img_w=6.0, img_h=3.2,
                 panel_title="No net heat flow",
                 caption="Heat flows hot → cold until temperatures are equal",
                 notes="Thermal equilibrium = equal temperatures, no net heat "
                       "flow. Build it from the hot-and-cold-block picture.")
    b.statement("THERMAL ENERGY", "Thermal Energy (Heat)",
                "Thermal energy is the form of energy that is transferred "
                "between two bodies because of a difference in their "
                "temperatures.",
                formula="SI unit of heat energy: the joule (J)",
                points=["It is also called heat energy or simply 'heat'.",
                        "The process of transferring it from a hotter to a "
                        "colder body is called heating.",
                        "Heat is a scalar quantity."],
                notes="Thermal energy (heat) flows due to a temperature "
                      "difference; SI unit joule; the transfer is 'heating'.")
    b.cards("KEY FEATURES", "Characteristic Features of Heat Transfer", [
        ("Hot to cold", "Heat always flows from a body at higher temperature "
         "to one at lower temperature."),
        ("Mass unchanged", "The mass of a body is not altered when it is heated "
         "or cooled."),
        ("Heat gained = heat lost", "In any exchange, the heat gained by the "
         "cold body equals the heat lost by the hot body."),
        ("Conservation", "This balance is simply the conservation of energy "
         "applied to heat."),
    ], notes="Three features from the text. 'Heat gained = heat lost' is the "
             "basis of calorimetry problems.")
    b.cards("UNITS OF HEAT", "Units of Heat Energy", [
        ("Joule (J)", "The SI unit of heat energy."),
        ("Calorie", "The heat needed to raise the temperature of 1 g of water "
         "by 1 °C."),
        ("Kilocalorie", "The heat needed to raise the temperature of 1 kg of "
         "water by 1 °C."),
        ("Link", "1 kilocalorie = 1000 calories; the calorie is still used for "
         "food energy."),
    ], notes="Joule (SI), calorie (1 g water, 1 °C) and kilocalorie (1 kg "
             "water, 1 °C). 1 kcal = 1000 cal.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "To Kelvin", "A liquid is at 27 °C. Its temperature on the "
             "kelvin scale is:", ["27 K", "246 K", "300 K", "−246 K"])
    b.quiz_a(1, "C. 300 K",
             "K = °C + 273 = 27 + 273 = 300 K. The kelvin reading is just the "
             "Celsius value plus 273.")
    b.quiz_q(2, "Equilibrium", "Two bodies at different temperatures are placed "
             "in contact. Heat stops flowing between them when they:",
             ["Have equal masses", "Reach the same temperature",
              "Have equal volumes", "Are both frozen"])
    b.quiz_a(2, "B. Reach the same temperature",
             "Heat flows from hot to cold until both bodies are at the same "
             "temperature — thermal equilibrium — after which there is no net "
             "flow, whatever their masses.")
    b.quiz_q(3, "Heat Balance", "When a hot metal is dropped into cool water "
             "(no heat lost to the surroundings):",
             ["The water loses heat to the metal",
              "Heat gained by the water equals heat lost by the metal",
              "Both gain heat", "No heat moves"])
    b.quiz_a(3, "B. Heat gained by water = heat lost by metal",
             "By conservation of energy, every joule the hotter metal loses is "
             "gained by the cooler water until they reach a common "
             "temperature.")
    b.quiz_q(4, "Define a Calorie", "One calorie is the heat needed to raise "
             "the temperature of:", ["1 kg of water by 1 °C",
              "1 g of water by 1 °C", "1 g of any liquid by 1 K",
              "1 litre of water by 10 °C"])
    b.quiz_a(4, "B. 1 g of water by 1 °C",
             "A calorie raises 1 gram of water through 1 °C; a kilocalorie does "
             "the same for 1 kilogram. The SI unit, though, is the joule.")
    b.quiz_q(5, "Absolute Zero", "The lowest possible temperature, 0 K, is "
             "equal to:", ["0 °C", "−100 °C", "−273 °C", "273 °C"])
    b.quiz_a(5, "C. −273 °C",
             "Absolute zero is 0 on the kelvin scale, which corresponds to "
             "−273 °C. No body can be cooled below this temperature.")
    b.divider(2, "Part 2", "Effects of Heat & Expansion",
              "What heat does to matter, and how things expand")
    b.cards("EFFECTS OF HEAT", "What Heat Energy Does to a Body", [
        ("Temperature rises", "Supplying heat usually makes a body hotter."),
        ("Change of state", "Heat can melt a solid or boil a liquid."),
        ("Expansion", "Almost all substances expand when heated."),
        ("Proportional", "The temperature rise is proportional to the heat "
         "supplied, and depends on the mass and nature of the substance."),
    ], notes="The three effects of heat: temperature rise, change of state, "
             "expansion. This chapter focuses on expansion.")
    b.statement("WHY EXPAND", "Thermal Expansion",
                "When a substance is heated, its particles vibrate or move more "
                "and push a little further apart, so the substance expands.",
                points=["For the same temperature rise, gases expand most, then "
                        "liquids, then solids.",
                        "Solids expand least because of their rigid structure.",
                        "On cooling, substances contract again."],
                notes="Molecular cause of expansion. Order: gases > liquids > "
                      "solids for the same temperature rise.")
    b.text_image("EXPANSION OF SOLIDS", "Three Kinds of Expansion in Solids",
                 ["Linear expansion: a change in length (a rod gets longer).",
                  "Superficial expansion: a change in area (a plate grows).",
                  "Cubical expansion: a change in volume (a block grows).",
                  "Each is described by its own coefficient of expansion, "
                  "with unit K⁻¹."],
                 exp, img_side="right", img_w=6.2, img_h=3.4,
                 panel_title="Length, area and volume",
                 caption="Linear, superficial and cubical expansion",
                 notes="Three kinds of solid expansion. Each has a coefficient "
                       "(per kelvin) that differs by material.")
    b.statement("LINEAR EXPANSION", "Linear (Longitudinal) Expansion",
                "When a body is heated, the change in its length per unit "
                "length per degree rise is its coefficient of linear "
                "expansion.",
                formula="ΔL / L₀ = αʟ ΔT        (αʟ in K⁻¹)",
                points=["ΔL = change in length, L₀ = original length.",
                        "ΔT = change in temperature.",
                        "αʟ depends on the material of the rod."],
                notes="Linear expansion ΔL/L₀ = αʟΔT. Define each term; αʟ is a "
                      "material property measured per kelvin.")
    b.statement("AREA & VOLUME", "Superficial and Cubical Expansion",
                "Area and volume expand in the same way, each with its own "
                "coefficient.",
                formula="ΔA / A₀ = αᴀ ΔT        ΔV / V₀ = αᴠ ΔT",
                points=["αᴀ = coefficient of superficial (area) expansion.",
                        "αᴠ = coefficient of cubical (volume) expansion.",
                        "Both have the unit K⁻¹, like the linear coefficient."],
                notes="Same form for area and volume. All three coefficients "
                      "are in K⁻¹.")
    b.cards("VALUES", "Coefficient of Cubical Expansion (per K)", [
        ("Aluminium", "7 × 10⁻⁵"),
        ("Brass / Glass", "6 × 10⁻⁵  /  2.5 × 10⁻⁵"),
        ("Water", "20.7 × 10⁻⁵"),
        ("Mercury", "18.2 × 10⁻⁵ — used in thermometers"),
    ], notes="Representative values from Table 3.1. Liquids (water, mercury) "
             "have much larger coefficients than solids.")
    b.worked("WORKED EXAMPLE", "Linear Expansion of a Rod",
             "A metal rod 2 m long has αʟ = 1.2 × 10⁻⁵ K⁻¹. Find the increase "
             "in its length when heated through 50 °C.",
             ["ΔL = αʟ L₀ ΔT",
              "ΔL = (1.2 × 10⁻⁵) × 2 × 50",
              "ΔL = 1.2 × 10⁻³ m"],
             "ΔL = 1.2 × 10⁻³ m = 1.2 mm",
             notes="Apply ΔL = αʟL₀ΔT. A small but important expansion — why "
                   "rails and bridges are given gaps.")
    b.statement("LIQUIDS & GASES", "Expansion of Liquids and Gases",
                "Liquids and gases also expand on heating — by more than "
                "solids.",
                points=["A liquid expands more than a solid for the same "
                        "temperature rise.",
                        "A gas expands the most of the three.",
                        "Heating a liquid in a container expands both the "
                        "container and the liquid."],
                notes="Liquids expand more than solids; gases most. Heating a "
                      "liquid also expands its container — leading to real vs "
                      "apparent expansion.")
    b.text_image("REAL vs APPARENT", "Real and Apparent Expansion of a Liquid",
                 ["Heated in a container, the container expands first, so the "
                  "liquid level first DIPS to L₂.",
                  "On further heating the liquid itself expands and rises to "
                  "L₃.",
                  "Apparent expansion = L₃ − L₁ (ignores the container).",
                  "Real expansion = L₃ − L₂, and is always greater than the "
                  "apparent expansion."],
                 flask, img_side="left", img_w=5.0, img_h=3.9,
                 panel_title="Real > Apparent",
                 caption="The level dips, then rises past the start",
                 notes="Real vs apparent expansion: container expands first "
                       "(dip to L₂), then liquid rises to L₃. Real = L₃−L₂ > "
                       "apparent = L₃−L₁.")
    b.worked("WORKED EXAMPLE", "Real and Apparent Expansion",
             "A container of capacity 70 ml is filled with liquid to 50 ml and "
             "heated. The level first falls to 48.5 ml, then rises to 51.2 ml. "
             "Find the apparent and real expansion.",
             ["L₁ = 50 ml, L₂ = 48.5 ml, L₃ = 51.2 ml",
              "Apparent expansion = L₃ − L₁ = 51.2 − 50 = 1.2 ml",
              "Real expansion = L₃ − L₂ = 51.2 − 48.5 = 2.7 ml"],
             "Apparent = 1.2 ml,  Real = 2.7 ml  (real > apparent)",
             notes="Worked Example 1 from the chapter. The dip (L₂) is the "
                   "container expanding first; real expansion uses L₂, not L₁.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Temperature", "degree of hotness; SI unit kelvin; 0 K = −273 °C"),
        ("Conversions", "K = °C + 273; K = (°F + 460) × 5/9"),
        ("Thermal equilibrium", "equal temperature, no net heat flow"),
        ("Heat features", "hot→cold; mass unchanged; heat gained = heat lost"),
        ("Solid expansion", "linear ΔL/L₀, area ΔA/A₀, volume ΔV/V₀ = αΔT"),
        ("Liquids", "real = L₃−L₂ > apparent = L₃−L₁"),
    ], notes="Rapid recap; the conversions and the real-vs-apparent result are "
             "the key exam points.")
    b.quiz_intro("Quiz 2", "Final Check — Expansion", 5)
    b.quiz_q(1, "Find ΔL", "A 3 m rod (αʟ = 2 × 10⁻⁵ K⁻¹) is heated through "
             "100 °C. Its increase in length is:",
             ["6 × 10⁻³ m", "6 × 10⁻⁵ m", "0.6 m", "6 m"])
    b.quiz_a(1, "A. 6 × 10⁻³ m",
             "ΔL = αʟ L₀ ΔT = (2 × 10⁻⁵) × 3 × 100 = 6 × 10⁻³ m (6 mm). Multiply "
             "the coefficient, length and temperature change.")
    b.quiz_q(2, "Expands Most", "For the same rise in temperature, which "
             "expands the most?", ["A solid", "A liquid", "A gas",
              "All equally"])
    b.quiz_a(2, "C. A gas",
             "Gases expand far more than liquids, and liquids more than solids, "
             "because gas molecules are free to move much further apart on "
             "heating.")
    b.quiz_q(3, "Real vs Apparent", "When a liquid is heated in a container, "
             "the real expansion of the liquid is:",
             ["Less than the apparent expansion",
              "Equal to the apparent expansion",
              "Greater than the apparent expansion", "Always zero"])
    b.quiz_a(3, "C. Greater than the apparent expansion",
             "The apparent expansion ignores the container's expansion. Adding "
             "back the container's share gives the real expansion, which is "
             "always the larger of the two.")
    b.quiz_q(4, "Why the Dip?", "On heating a liquid in a glass container, its "
             "level first falls slightly before rising. This is because:",
             ["The liquid contracts first",
              "The container expands first, lowering the level",
              "The liquid evaporates", "The thermometer is wrong"])
    b.quiz_a(4, "B. The container expands first",
             "Heat reaches the container first, so it expands and its capacity "
             "grows, dropping the level to L₂. Then the liquid itself expands "
             "and rises to L₃.")
    b.quiz_q(5, "Unit of α", "The coefficient of cubical expansion has the "
             "SI unit:", ["m³", "K⁻¹", "J/kg", "no unit"])
    b.quiz_a(5, "B. K⁻¹",
             "Every coefficient of expansion (linear, superficial or cubical) "
             "is a fractional change per degree, so its unit is per kelvin, "
             "K⁻¹.")
    b.closing("Heat Changes Matter",
              "Heat sets particles moving — raising temperature, changing state "
              "and expanding solids, liquids and gases in measurable ways.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["teal"])
    boyle = b.asset("g10tp_boyle", DT.boyle_graph("g10tp_boyle"))
    charles = b.asset("g10tp_charles", DT.charles_graph("g10tp_charles"))
    piston = b.asset("g10tp_piston", DT.gas_piston("g10tp_piston"))

    b.title("Class 10 • Thermal Physics", "Gas Laws & the Ideal Gas",
            "Boyle's law  •  Charles's law  •  Avogadro's law  •  Real & ideal "
            "gases  •  PV = RT", img=piston)
    b.objectives([
        "State Boyle's law and read its P–V graph",
        "State Charles's law and its link to absolute zero",
        "State Avogadro's law",
        "Distinguish a real gas from an ideal gas",
        "Combine the gas laws into the ideal gas equation",
        "Identify the Boltzmann and universal gas constants",
    ])
    b.divider(1, "Part 1", "The Fundamental Gas Laws",
              "How pressure, volume and temperature are linked")
    b.text_image("GAS PRESSURE", "A Gas Exerts Pressure",
                 ["A gas is made of fast-moving molecules with almost no forces "
                  "between them.",
                  "They constantly collide with the walls of the container.",
                  "These countless collisions produce the gas pressure.",
                  "Pressure (P), volume (V), temperature (T) and amount (n) "
                  "describe the state of a gas."],
                 piston, img_side="right", img_w=5.4, img_h=3.6,
                 panel_title="Collisions make pressure",
                 caption="Molecules bouncing off the walls",
                 notes="Set up the state variables P, V, T, n. Pressure comes "
                       "from molecular collisions — leads into the gas laws.")
    b.statement("BOYLE'S LAW", "Boyle's Law",
                "At constant temperature, the volume of a fixed mass of gas is "
                "inversely proportional to its pressure.",
                formula="P × V = constant      (T, mass constant)",
                points=["Squeeze the gas (volume down) and its pressure rises.",
                        "Let it expand (volume up) and its pressure falls.",
                        "So P₁V₁ = P₂V₂ for the same gas at the same "
                        "temperature."],
                notes="Boyle: at constant T, PV = constant. The P₁V₁ = P₂V₂ "
                      "form is the workhorse for numericals.")
    b.text_image("BOYLE GRAPH", "The Pressure–Volume Graph",
                 ["Plotting pressure against volume gives a smooth curve "
                  "(a rectangular hyperbola).",
                  "As volume increases, pressure decreases.",
                  "Every point on the curve has the same product P × V.",
                  "A different temperature gives a different curve."],
                 boyle, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="PV = constant",
                 caption="P–V curve at constant temperature",
                 notes="Read the hyperbola: P falls as V rises, PV constant "
                       "along it. Each temperature has its own curve.")
    b.worked("WORKED EXAMPLE", "Applying Boyle's Law",
             "A gas occupies 2 litres at a pressure of 1 atmosphere. At the "
             "same temperature it is compressed to 0.5 litre. Find its new "
             "pressure.",
             ["Boyle's law:  P₁V₁ = P₂V₂",
              "1 × 2 = P₂ × 0.5",
              "P₂ = 2 / 0.5"],
             "P₂ = 4 atmospheres",
             notes="Use P₁V₁ = P₂V₂. Quartering the volume's... here volume "
                   "drops to a quarter, so pressure rises four-fold.")
    b.statement("CHARLES'S LAW", "Charles's Law (Law of Volume)",
                "At constant pressure, the volume of a fixed mass of gas is "
                "directly proportional to its absolute (kelvin) temperature.",
                formula="V / T = constant      (P, mass constant)",
                points=["Temperature MUST be in kelvin, not °C.",
                        "Heat a gas at constant pressure and it expands.",
                        "So V₁ / T₁ = V₂ / T₂ for the same gas."],
                notes="Charles: at constant P, V/T = constant, with T in "
                      "KELVIN. Stress the kelvin requirement — a classic slip.")
    b.text_image("CHARLES GRAPH", "Volume–Temperature Graph",
                 ["Plotting volume against temperature gives a straight line.",
                  "Extending the line backwards, it meets the temperature axis "
                  "at −273 °C.",
                  "At this point the volume would become zero — absolute zero.",
                  "This is why the kelvin scale starts at −273 °C."],
                 charles, img_side="right", img_w=5.8, img_h=3.6,
                 panel_title="Straight line to −273 °C",
                 caption="Extrapolating to absolute zero",
                 notes="The V–T line extrapolates to −273 °C (0 K), linking "
                       "Charles's law to the absolute scale of the first deck.")
    b.worked("WORKED EXAMPLE", "Applying Charles's Law",
             "A gas has a volume of 300 cm³ at 27 °C. At constant pressure it "
             "is heated to 127 °C. Find its new volume.",
             ["Convert: T₁ = 27 + 273 = 300 K, T₂ = 127 + 273 = 400 K",
              "Charles's law:  V₁ / T₁ = V₂ / T₂",
              "300 / 300 = V₂ / 400",
              "V₂ = 400 cm³"],
             "New volume = 400 cm³",
             notes="Convert to kelvin FIRST, then apply V₁/T₁ = V₂/T₂. Using "
                   "°C here would give a wrong answer.")
    b.statement("AVOGADRO'S LAW", "Avogadro's Law",
                "At constant pressure and temperature, the volume of a gas is "
                "directly proportional to the number of molecules (amount) of "
                "gas.",
                formula="V / n = constant      (P, T constant)",
                points=["Equal volumes of gases at the same P and T contain "
                        "equal numbers of molecules.",
                        "Avogadro's number N_A = 6.023 × 10²³ per mole.",
                        "It is the number of particles in one mole of any "
                        "substance."],
                notes="Avogadro: V ∝ n at constant P, T. N_A = 6.023 × 10²³ "
                      "/mol — particles per mole.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Boyle Numerical", "A gas at 1 atm occupies 4 L. At constant "
             "temperature it is compressed to 1 L. Its new pressure is:",
             ["0.25 atm", "1 atm", "4 atm", "16 atm"])
    b.quiz_a(1, "C. 4 atm",
             "P₁V₁ = P₂V₂, so 1 × 4 = P₂ × 1, giving P₂ = 4 atm. Reducing the "
             "volume to a quarter multiplies the pressure four-fold.")
    b.quiz_q(2, "Use Kelvin", "Before applying Charles's law (V/T = constant), "
             "the temperature must always be converted to:",
             ["Degrees Celsius", "Degrees Fahrenheit", "Kelvin",
              "Calories"])
    b.quiz_a(2, "C. Kelvin",
             "Charles's law uses the absolute temperature. Using °C (which can "
             "be zero or negative) gives wrong ratios, so temperatures must be "
             "in kelvin.")
    b.quiz_q(3, "Boyle Graph", "At constant temperature, the graph of pressure "
             "against volume for a fixed mass of gas is:",
             ["A straight line through the origin",
              "A curve (rectangular hyperbola)", "A horizontal line",
              "A parabola opening upward"])
    b.quiz_a(3, "B. A curve (rectangular hyperbola)",
             "Because PV is constant, as V rises P must fall in proportion, "
             "tracing a rectangular hyperbola — not a straight line.")
    b.quiz_q(4, "Avogadro", "Equal volumes of oxygen and nitrogen at the same "
             "temperature and pressure contain:",
             ["Equal masses", "Equal numbers of molecules",
              "More oxygen molecules", "More nitrogen molecules"])
    b.quiz_a(4, "B. Equal numbers of molecules",
             "Avogadro's law: at the same P and T, equal volumes hold equal "
             "numbers of molecules — regardless of the gas or its mass.")
    b.quiz_q(5, "Double the Temp", "A fixed mass of gas at constant pressure "
             "has its kelvin temperature doubled. Its volume:",
             ["Halves", "Doubles", "Stays the same", "Becomes zero"])
    b.quiz_a(5, "B. Doubles",
             "By Charles's law V ∝ T (in kelvin). Doubling the absolute "
             "temperature at constant pressure doubles the volume.")
    b.divider(2, "Part 2", "Real, Ideal Gases & PV = RT",
              "From the three laws to the equation of state")
    b.cards("REAL GASES", "Real Gases", [
        ("Definition", "Gases whose molecules attract one another with a "
         "definite intermolecular force."),
        ("In practice", "All actual gases are real gases."),
        ("Behave ideally when", "At very high temperature or very low "
         "pressure, the forces become negligible."),
        ("Then", "A real gas behaves almost like an ideal gas."),
    ], notes="Real gases have intermolecular forces. At high T or low P those "
             "forces are negligible, so they behave nearly ideally.")
    b.cards("IDEAL GASES", "Ideal (Perfect) Gases", [
        ("Definition", "A gas whose molecules do not interact with one another "
         "at all."),
        ("Also called", "A perfect gas."),
        ("Obeys", "Boyle's, Charles's and Avogadro's laws exactly."),
        ("Reality", "No real gas is truly ideal, but many are close at low "
         "pressure / high temperature."),
    ], notes="Ideal gas = no intermolecular forces; obeys all three laws "
             "exactly. A useful idealisation, not a real substance.")
    b.statement("COMBINED LAW", "Combining the Three Laws",
                "Boyle's, Charles's and Avogadro's laws can be combined into a "
                "single relation between P, V, n and T.",
                formula="P V / (n T) = constant      (the combined gas law)",
                points=["From Boyle: PV = constant (T, n fixed).",
                        "From Charles: V/T = constant (P, n fixed).",
                        "From Avogadro: V/n = constant (P, T fixed)."],
                notes="The three laws merge into PV/nT = constant. Each law is "
                      "a special case holding two quantities fixed.")
    b.statement("IDEAL GAS EQUATION", "The Ideal Gas Equation (PV = RT)",
                "Writing the combined-law constant in terms of fundamental "
                "constants gives the equation of state of an ideal gas.",
                formula="PV = μ N_A k_B T  →  PV = RT      (R = N_A k_B)",
                points=["k_B = Boltzmann constant = 1.38 × 10⁻²³ J K⁻¹.",
                        "R = universal gas constant = 8.31 J mol⁻¹ K⁻¹.",
                        "PV = RT is called the equation of state — it describes "
                        "the state of any ideal gas."],
                notes="PV/μN_A T = k_B leads to PV = RT with R = N_A k_B. Name "
                      "the equation of state and the two constants.")
    b.bullets("THE CONSTANTS", "Boltzmann and Universal Gas Constants", [
        ("Boltzmann constant k_B", "1.38 × 10⁻²³ J K⁻¹ — energy per molecule "
         "per kelvin."),
        ("Universal gas constant R", "8.31 J mol⁻¹ K⁻¹ — the same for all "
         "ideal gases."),
        ("They are linked", "R = N_A × k_B (per mole = per molecule × molecules "
         "per mole)."),
        ("Equation of state", "PV = RT relates all the state variables of an "
         "ideal gas."),
    ], panel_title="Two key constants",
       notes="k_B (per molecule) and R (per mole) are linked by Avogadro's "
             "number: R = N_A k_B.")
    b.worked("WORKED EXAMPLE", "Linking the Constants",
             "Show that the universal gas constant R follows from Avogadro's "
             "number and the Boltzmann constant. (N_A = 6.023 × 10²³ mol⁻¹, "
             "k_B = 1.38 × 10⁻²³ J K⁻¹)",
             ["R = N_A × k_B",
              "R = (6.023 × 10²³) × (1.38 × 10⁻²³)",
              "R ≈ 8.31 J mol⁻¹ K⁻¹"],
             "R ≈ 8.31 J mol⁻¹ K⁻¹ — the universal gas constant",
             notes="Multiplying per-molecule k_B by molecules-per-mole N_A "
                   "gives the per-mole constant R. The powers of ten cancel "
                   "neatly.")
    b.cards("REAL vs IDEAL", "Real and Ideal Gases at a Glance", [
        ("Forces", "Real: molecules attract; Ideal: no forces between "
         "molecules."),
        ("Gas laws", "Real: obeyed only approximately; Ideal: obeyed exactly."),
        ("When alike", "A real gas acts ideal at high temperature and low "
         "pressure."),
        ("Existence", "Real gases exist; the ideal gas is a useful model."),
    ], notes="Summary comparison. The key practical point: real ≈ ideal at "
             "high T and low P.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Boyle", "PV = constant at constant T (P₁V₁ = P₂V₂)"),
        ("Charles", "V/T = constant at constant P (T in kelvin)"),
        ("Avogadro", "V/n = constant; N_A = 6.023 × 10²³ /mol"),
        ("Real gas", "has intermolecular forces; ideal at high T, low P"),
        ("Ideal gas", "no forces; obeys all three laws exactly"),
        ("Equation of state", "PV = RT, with R = N_A k_B = 8.31 J mol⁻¹ K⁻¹"),
    ], notes="Rapid recap; the three laws and PV = RT are the key results.")
    b.quiz_intro("Quiz 2", "Final Check — Ideal Gases", 5)
    b.quiz_q(1, "Ideal Assumption", "An ideal gas is one in which the "
             "molecules:", ["Are very large",
              "Exert no force on one another", "Never move",
              "Are all the same colour"])
    b.quiz_a(1, "B. Exert no force on one another",
             "An ideal (perfect) gas is defined as one whose molecules do not "
             "interact — there are no intermolecular forces, so it obeys the "
             "gas laws exactly.")
    b.quiz_q(2, "When Ideal?", "A real gas behaves most like an ideal gas at:",
             ["Low temperature and high pressure",
              "High temperature and low pressure",
              "Low temperature and low pressure", "Its boiling point"])
    b.quiz_a(2, "B. High temperature and low pressure",
             "At high temperature and low pressure the molecules are far apart "
             "and fast-moving, so their weak attractions barely matter and the "
             "gas behaves almost ideally.")
    b.quiz_q(3, "Universal Constant", "The value of the universal gas constant "
             "R is about:", ["1.38 × 10⁻²³ J K⁻¹", "6.023 × 10²³ mol⁻¹",
              "8.31 J mol⁻¹ K⁻¹", "273 J"])
    b.quiz_a(3, "C. 8.31 J mol⁻¹ K⁻¹",
             "R = 8.31 J mol⁻¹ K⁻¹ and is the same for all ideal gases. "
             "1.38 × 10⁻²³ J K⁻¹ is the Boltzmann constant, and 6.023 × 10²³ is "
             "Avogadro's number.")
    b.quiz_q(4, "Equation of State", "Which equation is the ideal gas equation "
             "(equation of state)?", ["PV = RT", "V = IR", "P = hρg",
              "Q = mcΔT"])
    b.quiz_a(4, "A. PV = RT",
             "PV = RT relates the pressure, volume and absolute temperature of "
             "an ideal gas and is called its equation of state. The others are "
             "from electricity, fluids and calorimetry.")
    b.quiz_q(5, "Linking Constants", "The universal gas constant R and the "
             "Boltzmann constant k_B are related by Avogadro's number N_A "
             "through:", ["R = k_B / N_A", "R = N_A × k_B", "R = N_A + k_B",
              "R = N_A − k_B"])
    b.quiz_a(5, "B. R = N_A × k_B",
             "k_B is the constant per molecule and R is per mole, so "
             "multiplying by the molecules-per-mole N_A converts one to the "
             "other: R = N_A k_B ≈ 8.31 J mol⁻¹ K⁻¹.")
    b.closing("The Behaviour of Gases",
              "Three simple laws combine into one equation, PV = RT — the "
              "elegant rule that captures how every ideal gas behaves.")
    return b


def build():
    for fname, fn in [("G10_Thermal_Physics_1.pptx", deck1),
                      ("G10_Thermal_Physics_2.pptx", deck2)]:
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
