"""
Grade 10 Physics — Chapter: Current Electricity.
S75 (charge, current, p.d., resistance, Ohm's law), S76 (resistance factors,
resistivity, superconductors, EMF & internal resistance), S77 (combinations of
resistors, electrical energy & power, heating effect).  ICSE Class 10 (Selina).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade10"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Current Electricity  •  ICSE Class 10 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    circ = b.asset("g10ce_circ", D.ohm_circuit("g10ce_circ"))
    graph = b.asset("g10ce_graph", D.ohm_graph("g10ce_graph"))
    syms = b.asset("g10ce_syms", D.circuit_symbols("g10ce_syms"))
    hero = b.asset("g10_current_hero", circ)

    b.title("ICSE • Class 10 • Electricity", "Current & Ohm's Law",
            "Charge & current  •  Potential difference  •  Resistance  •  "
            "Ohm's law", img=hero)
    b.objectives([
        "Define electric charge and electric current",
        "Use the relation I = Q / t",
        "Define potential difference and the volt",
        "Define resistance and the ohm",
        "State and apply Ohm's law, V = I R",
        "Describe how Ohm's law is verified experimentally",
    ])
    b.divider(1, "Part 1", "Charge, Current & Potential Difference",
              "The basic quantities of electricity")
    b.bullets("CHARGE", "Electric Charge", [
        ("Two kinds", "positive and negative; like charges repel, unlike "
         "charges attract."),
        ("Unit", "the coulomb (C); the charge on one electron is "
         "1.6 × 10⁻¹⁹ C."),
        ("Current is moving charge", "an electric current is a flow of "
         "charge (electrons in a metal)."),
        ("Conventional current", "taken to flow from + to −, opposite to the "
         "actual electron flow."),
    ], panel_title="What flows in a wire",
       notes="Establish charge and its unit, then the key idea: current is "
             "charge in motion. Note conventional vs electron-flow direction.")
    b.statement("CURRENT", "Electric Current",
                "Electric current is the rate of flow of charge through a "
                "conductor.",
                formula="I  =  Q / t        (1 ampere = 1 coulomb / second)",
                points=["Q is the charge in coulombs, t the time in seconds.",
                        "The SI unit of current is the ampere (A).",
                        "Measured with an ammeter, connected in series."],
                notes="Define current as Q/t. Ammeter in series — a key "
                      "practical point repeated in the experiment slide.")
    b.worked("WORKED EXAMPLE", "Charge and Current",
             "A current of 0.5 A flows through a lamp for 4 minutes. How much "
             "charge passes through it?",
             ["I = Q / t   →   Q = I × t",
              "t = 4 minutes = 240 s",
              "Q = 0.5 × 240 = 120 C"],
             "Q = 120 C of charge flows through the lamp",
             notes="Watch the unit of time — convert minutes to seconds first. "
                   "A very common slip.")
    b.bullets("ELECTRON FLOW", "How Current Flows in a Metal", [
        ("Free electrons", "A metal has countless loosely-held electrons that "
         "move about randomly."),
        ("A cell's push", "Connecting a cell sets up a p.d. that makes the "
         "electrons drift slowly in one direction."),
        ("Slow drift, fast effect", "The drift is slow, but the effect (the "
         "current) is felt almost instantly all along the wire."),
        ("Direction", "Electrons drift from − to +; conventional current is "
         "taken from + to −."),
    ], panel_title="Drift of free electrons",
       notes="Picture the slow electron drift versus the near-instant onset of "
             "current. Reinforce the two 'directions'.")
    b.statement("POTENTIAL DIFFERENCE", "Potential Difference (Voltage)",
                "The potential difference between two points is the work done "
                "to move unit charge from one point to the other.",
                formula="V  =  W / Q        (1 volt = 1 joule / coulomb)",
                points=["It is the 'push' that drives current around a "
                        "circuit.",
                        "Measured with a voltmeter, connected in parallel.",
                        "The SI unit is the volt (V)."],
                notes="Voltage = energy per unit charge. Voltmeter in parallel "
                      "(across the component) — contrast with the ammeter.")
    b.text_image("CIRCUIT SYMBOLS", "Reading a Circuit Diagram",
                 ["Circuits are drawn with standard symbols, not pictures.",
                  "A cell is a long thin line (+) and a short thick line (−); "
                  "several cells make a battery.",
                  "An ammeter (A) goes in series; a voltmeter (V) goes in "
                  "parallel across a component.",
                  "A rheostat is a variable resistor used to change the "
                  "current."],
                 syms, img_side="right", img_w=5.2, img_h=3.8,
                 panel_title="The standard symbols",
                 caption="Cell, battery, bulb, switch, resistor, meters",
                 notes="Go over each symbol. Students must read and draw these "
                       "fluently for the circuit questions that follow.")
    b.cards("CONDUCTORS", "Conductors and Insulators", [
        ("Conductors", "Have free electrons, so they carry current easily — "
         "e.g. copper, silver, aluminium."),
        ("Insulators", "Have almost no free electrons, so they block current — "
         "e.g. rubber, glass, plastic."),
        ("Why copper wires", "Copper is a very good conductor and is "
         "relatively cheap."),
        ("Why plastic coating", "The insulating coat keeps current in the wire "
         "and us safe."),
    ], notes="Free electrons are the difference. Link to everyday wiring: "
             "copper core, plastic sheath.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "How Much Charge?", "A current of 2 A flows for half a minute. "
             "The charge that passes is:", ["1 C", "30 C", "60 C", "4 C"])
    b.quiz_a(1, "C. 60 C",
             "Q = I × t = 2 × 30 s = 60 C. The catch is the time: half a "
             "minute is 30 seconds, not 0.5.")
    b.quiz_q(2, "Meters", "To measure the current through a lamp and the "
             "voltage across it, you connect:",
             ["Ammeter in parallel, voltmeter in series",
              "Both in series", "Ammeter in series, voltmeter in parallel",
              "Both in parallel"])
    b.quiz_a(2, "C. Ammeter in series, voltmeter in parallel",
             "An ammeter measures the current that flows through, so it goes "
             "in series. A voltmeter measures the p.d. across a component, so "
             "it goes in parallel with it.")
    b.quiz_q(3, "Which Way?", "In a metal wire the electric current is "
             "actually carried by electrons moving from − to +. The "
             "'conventional current' is taken to flow:",
             ["In the same direction as the electrons",
              "From + to −, opposite to the electrons",
              "In both directions at once", "It does not flow at all"])
    b.quiz_a(3, "B. From + to −, opposite to the electrons",
             "By convention, current direction is the direction positive "
             "charge would move — from + to −. This is opposite to the actual "
             "electron flow in a metal.")
    b.quiz_q(4, "One Volt", "Saying the p.d. across a bulb is 1 volt means "
             "that:", ["1 ampere flows through it",
              "1 joule of energy is given to each coulomb of charge passing",
              "1 coulomb flows per second", "Its resistance is 1 ohm"])
    b.quiz_a(4, "B. 1 joule is given to each coulomb",
             "1 volt = 1 joule per coulomb. The p.d. tells you how much energy "
             "each unit of charge delivers as it passes through the bulb.")
    b.quiz_q(5, "Energy Delivered", "A charge of 20 C flows through a bulb "
             "across which the p.d. is 6 V. The energy delivered to the bulb "
             "is:", ["3.3 J", "26 J", "120 J", "0.3 J"])
    b.quiz_a(5, "C. 120 J",
             "From V = W/Q, the energy is W = V × Q = 6 × 20 = 120 J. Each "
             "coulomb gives 6 J, and 20 coulombs pass through.")
    b.divider(2, "Part 2", "Resistance & Ohm's Law",
              "How conductors oppose current")
    b.statement("RESISTANCE", "Electrical Resistance",
                "Resistance is the opposition a conductor offers to the flow "
                "of current through it.",
                formula="R  =  V / I        (1 ohm = 1 volt / ampere)",
                points=["A larger resistance means less current for the same "
                        "voltage.",
                        "The SI unit of resistance is the ohm (Ω).",
                        "Resistance arises as electrons collide with the atoms "
                        "of the conductor."],
                notes="Define R = V/I and the ohm. Physical picture: electrons "
                      "colliding with lattice atoms.")
    b.text_image("OHM'S LAW", "Ohm's Law",
                 ["Ohm's law: the current through a conductor is directly "
                  "proportional to the p.d. across it, at constant "
                  "temperature.",
                  "So V / I is constant — that constant is the resistance R.",
                  "A graph of V against I is a straight line through the "
                  "origin.",
                  "Its slope equals the resistance of the conductor."],
                 graph, img_side="right", img_w=4.6, img_h=3.8,
                 panel_title="V = I R",
                 caption="V–I graph is a straight line (Ohmic)",
                 notes="State Ohm's law with the 'constant temperature' "
                       "condition. The straight-line graph is the visual "
                       "signature.")
    b.text_image("EXPERIMENT", "Verifying Ohm's Law",
                 ["Connect the resistor in series with a cell, ammeter and "
                  "rheostat; a voltmeter across the resistor.",
                  "Vary the rheostat to get several pairs of readings of V and "
                  "I.",
                  "Plot V against I — a straight line through the origin "
                  "confirms Ohm's law.",
                  "The slope of the line gives the resistance R."],
                 circ, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="Cell, ammeter, voltmeter, rheostat",
                 caption="Ammeter in series, voltmeter in parallel",
                 notes="Walk through the standard practical. Reinforce meter "
                       "placement and that constant slope proves the law.")
    b.worked("WORKED EXAMPLE", "Applying Ohm's Law",
             "A 12 V battery drives a current of 0.4 A through a resistor. "
             "Find its resistance.",
             ["Ohm's law:  V = I R   →   R = V / I",
              "R = 12 / 0.4",
              "R = 30 Ω"],
             "Resistance R = 30 Ω",
             notes="Straight substitution. Encourage a units check: volts ÷ "
                   "amps = ohms.")
    b.cards("BEYOND OHM", "When Ohm's Law Does Not Hold", [
        ("The condition", "Ohm's law applies only while temperature (and "
         "other physical conditions) stay constant."),
        ("Filament lamp", "It heats up as current rises, so its resistance "
         "climbs and the V–I graph curves."),
        ("Diode", "Conducts well one way and barely the other — a strongly "
         "non-ohmic device."),
        ("Thermistor / LDR", "Resistance changes with temperature or light, so "
         "these too are non-ohmic."),
    ], notes="Ohm's law is not universal. Filament lamps, diodes, thermistors "
             "and LDRs are common non-ohmic examples to remember.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Charge & current", "I = Q / t; current is the rate of flow of charge"),
        ("Potential difference", "V = W / Q; the volt is a joule per coulomb"),
        ("Meters", "ammeter in series, voltmeter in parallel"),
        ("Resistance", "R = V / I; the ohm opposes current"),
        ("Ohm's law", "V = I R at constant temperature"),
        ("V–I graph", "straight line through the origin; slope = R"),
    ], notes="Rapid recap; cold-call the formula and unit for each quantity.")
    b.quiz_intro("Quiz 2", "Final Check — Resistance & Ohm", 5)
    b.quiz_q(1, "Find R", "A torch bulb carries 0.3 A when connected to a 1.5 V "
             "cell. Its resistance is:", ["0.2 Ω", "4.5 Ω", "5 Ω", "1.8 Ω"])
    b.quiz_a(1, "C. 5 Ω",
             "R = V / I = 1.5 / 0.3 = 5 Ω. Keep the volts on top and amps "
             "below.")
    b.quiz_q(2, "Double the Voltage", "A resistor obeys Ohm's law. If the "
             "voltage across it is doubled (temperature unchanged), the "
             "current through it:", ["Stays the same", "Doubles", "Halves",
              "Becomes zero"])
    b.quiz_a(2, "B. Doubles",
             "Since V = IR with R constant, current is proportional to "
             "voltage. Doubling V doubles I — the essence of Ohm's law.")
    b.quiz_q(3, "Reading a Graph", "On a V–I graph for a metal wire, a "
             "steeper straight line means the wire has a:",
             ["Smaller resistance", "Larger resistance", "Zero resistance",
              "Variable resistance"])
    b.quiz_a(3, "B. Larger resistance",
             "The slope of a V–I graph equals the resistance. A steeper line "
             "means more volts are needed per amp — a larger resistance.")
    b.quiz_q(4, "Not Ohmic", "Which of these would NOT give a straight line "
             "through the origin on a V–I graph?",
             ["A length of constant-temperature copper wire",
              "A filament lamp that heats up as current rises",
              "A fixed metal resistor at constant temperature",
              "A standard resistance coil kept cool"])
    b.quiz_a(4, "B. A filament lamp that heats up",
             "As the filament heats, its resistance rises, so the V–I graph "
             "curves rather than staying straight. Ohm's law holds only at "
             "constant temperature.")
    b.quiz_q(5, "Same Charge, Less Time", "Two wires carry the same charge. "
             "Wire X takes 10 s and wire Y takes 20 s. Compared with Y, the "
             "current in X is:", ["Half as large", "The same", "Twice as "
              "large", "Four times as large"])
    b.quiz_a(5, "C. Twice as large",
             "I = Q / t. For the same charge, half the time means double the "
             "current. X (10 s) carries twice the current of Y (20 s).")
    b.closing("Current, Voltage, Resistance",
              "Three quantities, one law: V = I R ties the whole of circuit "
              "physics together.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    graph = b.asset("g10ce_graph2", D.ohm_graph("g10ce_graph2"))
    hero = b.asset("g10_resistance_hero", graph)

    b.title("ICSE • Class 10 • Electricity", "Resistance & Cells",
            "Factors affecting resistance  •  Resistivity  •  EMF & internal "
            "resistance", img=hero)
    b.objectives([
        "Distinguish ohmic and non-ohmic conductors",
        "List the factors that affect the resistance of a wire",
        "Define specific resistance (resistivity) and use R = ρL/A",
        "Choose suitable materials for wires and heating elements",
        "Describe superconductors",
        "Define EMF, terminal voltage and internal resistance of a cell",
    ])
    b.divider(1, "Part 1", "What Resistance Depends On",
              "Why some wires resist more than others")
    b.cards("OHMIC OR NOT", "Ohmic and Non-Ohmic Conductors", [
        ("Ohmic", "Obey Ohm's law: V–I graph is a straight line, e.g. metal "
         "wires at constant temperature."),
        ("Non-ohmic", "Do not obey Ohm's law: V–I graph is curved, e.g. a "
         "filament bulb, a diode."),
        ("Why bulbs curve", "The filament heats up, its resistance rises, so "
         "the graph bends."),
        ("Still useful", "Non-ohmic devices like diodes are vital in "
         "electronics."),
    ], notes="Ohmic = straight line; non-ohmic = curved. The heating filament "
             "is the standard non-ohmic example.")
    b.cards("FACTORS", "What Affects a Wire's Resistance", [
        ("Length", "Resistance is proportional to length — a longer wire has "
         "more resistance."),
        ("Area", "Resistance is inversely proportional to cross-sectional "
         "area — a thicker wire resists less."),
        ("Material", "Different materials have different resistivities."),
        ("Temperature", "For metals, resistance increases as temperature "
         "rises."),
    ], notes="Four factors. Length ↑ → R ↑; area ↑ → R ↓; plus material and "
             "temperature. These feed straight into the resistivity formula.")
    b.statement("RESISTIVITY", "Specific Resistance (Resistivity)",
                "The resistance of a wire depends on its length and area "
                "through the resistivity ρ of its material.",
                formula="R  =  ρ L / A        (ρ in ohm-metre, Ω m)",
                points=["L is the length, A the cross-sectional area.",
                        "Resistivity ρ is a property of the material, not the "
                        "shape.",
                        "Good conductors (copper, silver) have very low "
                        "resistivity."],
                notes="R = ρL/A links the factors quantitatively. Stress ρ "
                      "depends only on material (and temperature), not size.")
    b.worked("WORKED EXAMPLE", "Using R = ρL/A",
             "A wire is 2 m long with cross-sectional area 0.5 mm² "
             "(0.5 × 10⁻⁶ m²) and resistivity 1.0 × 10⁻⁶ Ω m. Find its "
             "resistance.",
             ["R = ρ L / A",
              "R = (1.0 × 10⁻⁶ × 2) / (0.5 × 10⁻⁶)",
              "R = (2.0 × 10⁻⁶) / (0.5 × 10⁻⁶) = 4 Ω"],
             "Resistance R = 4 Ω",
             notes="Keep the powers of ten lined up. The micro-factors cancel, "
                   "leaving a clean number.")
    b.cards("CHOOSING MATERIALS", "The Right Wire for the Job", [
        ("Copper for wiring", "Very low resistivity, so it carries current "
         "with little loss."),
        ("Nichrome for heaters", "High resistivity and a high melting point — "
         "it gets hot without melting."),
        ("Tungsten for filaments", "Very high melting point, so it glows "
         "white-hot in a bulb without breaking."),
        ("Fuse wire", "Low melting point, so it melts and breaks the circuit "
         "if the current is too high."),
    ], notes="Match property to purpose: low ρ to carry current, high ρ + high "
             "m.p. to make heat, low m.p. to make a fuse.")
    b.bullets("SUPERCONDUCTORS", "Superconductors", [
        ("Zero resistance", "Below a very low critical temperature some "
         "materials lose all electrical resistance."),
        ("No energy loss", "Current can flow with no heating and no energy "
         "wasted."),
        ("Uses", "Powerful electromagnets in MRI scanners and maglev trains."),
        ("The catch", "They must be kept extremely cold, which is expensive."),
    ], panel_title="Resistance that drops to zero",
       notes="Superconductors: zero resistance below a critical temperature. "
             "Great for strong magnets, but cooling is the challenge.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Stretch the Wire", "A wire is stretched so that its length "
             "doubles (its volume staying the same, so the area halves). Its "
             "new resistance becomes:", ["Half", "The same", "Double",
              "Four times the original"])
    b.quiz_a(1, "D. Four times the original",
             "R = ρL/A. Doubling the length doubles R, and halving the area "
             "doubles it again — together a factor of 4. A classic stretched-"
             "wire problem.")
    b.quiz_q(2, "Heater Element", "Why is the heating element of an electric "
             "iron made of nichrome rather than copper?",
             ["Copper is too expensive", "Nichrome has high resistivity and a "
              "high melting point, so it heats up without melting",
              "Copper cannot carry current", "Nichrome is a better conductor"])
    b.quiz_a(2, "B. High resistivity and high melting point",
             "A heater needs a wire that resists current strongly (to release "
             "heat) and survives high temperatures. Nichrome does both; copper "
             "conducts too well and would barely warm up.")
    b.quiz_q(3, "Thicker Wire", "Replacing a wire with a thicker one of the "
             "same material and length will:",
             ["Increase its resistance", "Decrease its resistance",
              "Not change its resistance", "Make it an insulator"])
    b.quiz_a(3, "B. Decrease its resistance",
             "Resistance is inversely proportional to cross-sectional area. A "
             "thicker wire gives electrons more room to flow, lowering the "
             "resistance.")
    b.quiz_q(4, "Resistivity", "Two wires, one copper and one iron, have the "
             "same length and thickness. They have different resistances "
             "because they differ in:", ["Length", "Cross-sectional area",
              "Resistivity (material)", "Temperature only"])
    b.quiz_a(4, "C. Resistivity (material)",
             "With length and area equal, the only difference left is the "
             "material's resistivity ρ. Iron has a higher resistivity than "
             "copper, so the iron wire resists more.")
    b.quiz_q(5, "Heating a Metal", "As a metal wire is heated, its resistance:",
             ["Decreases", "Increases", "Stays exactly constant",
              "Falls to zero"])
    b.quiz_a(5, "B. Increases",
             "Heating makes the metal's atoms vibrate more, so the drifting "
             "electrons collide with them more often. The extra opposition "
             "raises the resistance — the reason a filament lamp is non-ohmic.")
    b.divider(2, "Part 2", "Cells: EMF & Internal Resistance",
              "Why a battery's voltage drops when it supplies current")
    b.statement("EMF", "Electromotive Force (EMF)",
                "The EMF of a cell is the energy it gives to each unit of "
                "charge — the p.d. across its terminals when no current is "
                "drawn.",
                formula="EMF (E)  =  energy supplied / charge",
                points=["Measured in volts, like potential difference.",
                        "It is the 'full' voltage of the cell on open "
                        "circuit.",
                        "Driving current through the cell's own materials uses "
                        "up some of this energy."],
                notes="EMF = total energy per charge from the cell. It is the "
                      "open-circuit (no current) voltage.")
    b.statement("TERMINAL VOLTAGE", "Terminal Voltage & Internal Resistance",
                "When a cell supplies current, some voltage is lost inside it "
                "across its own internal resistance r.",
                formula="V  =  E − I r",
                points=["E is the EMF, I the current, r the internal "
                        "resistance.",
                        "V is the terminal voltage available to the external "
                        "circuit.",
                        "The larger the current, the bigger the internal drop "
                        "I r."],
                notes="Terminal voltage V = E − Ir. This is why a car's "
                      "headlights dim when the starter motor draws a big "
                      "current.")
    b.bullets("INTERNAL RESISTANCE", "Internal Resistance of a Cell", [
        ("What it is", "The resistance of the cell's own electrolyte and "
         "electrodes."),
        ("Effect", "It causes the terminal voltage to fall below the EMF when "
         "current flows."),
        ("Open circuit", "With no current (I = 0), the terminal voltage equals "
         "the EMF."),
        ("Old cells", "Internal resistance rises as a cell ages, so it "
         "delivers less voltage."),
    ], panel_title="The resistance inside the cell",
       notes="Internal resistance explains the gap between EMF and terminal "
             "voltage. At I = 0 the two are equal.")
    b.statement("THE CIRCUIT EQUATION", "EMF, Current and Total Resistance",
                "When a cell of EMF E and internal resistance r drives current "
                "through an external resistance R, the EMF is shared between "
                "the two.",
                formula="E  =  I (R + r)        so   I = E / (R + r)",
                points=["I R is the useful p.d. across the external circuit "
                        "(the terminal voltage).",
                        "I r is the p.d. lost inside the cell.",
                        "Adding the internal resistance reduces the current "
                        "the cell can drive."],
                notes="E = I(R + r) is the master equation; it combines Ohm's "
                      "law with internal resistance. Terminal voltage = IR.")
    b.cards("GROUPING CELLS", "Cells in Series and in Parallel", [
        ("In series", "EMFs add (E = E₁ + E₂ + …); used to get a higher "
         "voltage."),
        ("Series resistance", "Internal resistances also add, so a big current "
         "can still be limited."),
        ("In parallel", "Identical cells keep the same EMF but share the "
         "current, lowering effective internal resistance."),
        ("When to use", "Series for higher voltage; parallel to deliver a "
         "larger current for longer."),
    ], notes="Grouping of cells: series adds EMFs (and r); parallel keeps EMF "
             "but cuts internal resistance and shares current.")
    b.worked("WORKED EXAMPLE", "Terminal Voltage",
             "A cell of EMF 1.5 V and internal resistance 0.5 Ω drives a "
             "current of 0.6 A. Find its terminal voltage.",
             ["V = E − I r",
              "V = 1.5 − (0.6 × 0.5)",
              "V = 1.5 − 0.3 = 1.2 V"],
             "Terminal voltage V = 1.2 V",
             notes="Substitute into V = E − Ir. The 0.3 V is 'lost' inside the "
                   "cell across r.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Ohmic / non-ohmic", "straight vs curved V–I graph"),
        ("Factors", "R ∝ length, R ∝ 1/area, plus material & temperature"),
        ("Resistivity", "R = ρL/A; ρ is a property of the material"),
        ("Material choice", "copper to carry, nichrome/tungsten to heat"),
        ("EMF vs terminal V", "V = E − I r"),
        ("Internal resistance", "voltage lost inside the cell when current "
         "flows"),
    ], notes="Rapid recap; the stretched-wire and V = E − Ir ideas are the "
             "exam favourites.")
    b.quiz_intro("Quiz 2", "Final Check — Resistivity & Cells", 5)
    b.quiz_q(1, "Open Circuit", "A voltmeter across a cell reads 1.5 V when no "
             "current is drawn, but only 1.3 V when the cell lights a bulb. "
             "The 1.5 V reading is the cell's:", ["Terminal voltage",
              "Internal resistance", "EMF", "Power"])
    b.quiz_a(1, "C. EMF",
             "With no current there is no internal voltage drop, so the "
             "terminal voltage equals the EMF (1.5 V). Once current flows, "
             "I r is lost inside and the terminal voltage falls to 1.3 V.")
    b.quiz_q(2, "Find r", "Using the cell above (EMF 1.5 V, terminal voltage "
             "1.3 V when the current is 0.5 A), the internal resistance is:",
             ["0.2 Ω", "0.4 Ω", "2.6 Ω", "0.5 Ω"])
    b.quiz_a(2, "B. 0.4 Ω",
             "The lost voltage is E − V = 1.5 − 1.3 = 0.2 V. Since this equals "
             "I r, r = 0.2 / 0.5 = 0.4 Ω.")
    b.quiz_q(3, "Longer Wire", "A uniform wire has resistance 6 Ω. A piece one "
             "third of its length would have resistance:",
             ["18 Ω", "6 Ω", "3 Ω", "2 Ω"])
    b.quiz_a(3, "D. 2 Ω",
             "Resistance is proportional to length. One third of the length "
             "has one third of the resistance: 6 / 3 = 2 Ω.")
    b.quiz_q(4, "Same Material", "Which property is the SAME for a thick "
             "copper wire and a thin copper wire?",
             ["Resistance", "Cross-sectional area", "Resistivity", "Current "
              "they carry"])
    b.quiz_a(4, "C. Resistivity",
             "Resistivity depends only on the material (and temperature), so "
             "both copper wires share it. Their resistances differ because "
             "their areas differ.")
    b.quiz_q(5, "Why Dim?", "A car's headlights dim for a moment when the "
             "engine is started. This is because the starter motor:",
             ["Increases the EMF", "Draws a large current, so the internal "
              "drop I r lowers the terminal voltage", "Cools the battery",
              "Breaks Ohm's law"])
    b.quiz_a(5, "B. Large current → bigger I r drop",
             "The starter draws a huge current, so the voltage lost inside the "
             "battery (I r) jumps. The terminal voltage falls, momentarily "
             "dimming the lights.")
    b.closing("Inside Every Wire and Cell",
              "Resistivity shapes the wire; internal resistance shapes the "
              "cell — together they decide what a circuit can do.")
    return b


def deck3():
    b = Builder(FOOTER, accent=C["orange"])
    combo = b.asset("g10ce_combo", D.resistors_combo("g10ce_combo"))
    hero = b.asset("g10_power_hero", combo)

    b.title("ICSE • Class 10 • Electricity", "Resistor Networks, Energy & Power",
            "Series & parallel  •  Electrical energy & power  •  The kilowatt-"
            "hour  •  Heating effect", img=hero)
    b.objectives([
        "Combine resistors in series and in parallel",
        "Calculate the equivalent resistance of a network",
        "Use electrical energy W = V I t",
        "Use electrical power P = V I = I²R = V²/R",
        "Convert energy to the commercial unit, the kilowatt-hour",
        "Explain the heating effect of an electric current",
    ])
    b.divider(1, "Part 1", "Combining Resistors",
              "Series and parallel networks")
    b.text_image("COMBINATIONS", "Series and Parallel",
                 ["In series, resistors are joined end to end; the same "
                  "current flows through each.",
                  "Series resistances simply add: R = R₁ + R₂ + R₃.",
                  "In parallel, resistors share the same two ends and the same "
                  "voltage.",
                  "For parallel: 1/R = 1/R₁ + 1/R₂ + 1/R₃, giving a smaller "
                  "total than any one."],
                 combo, img_side="left", img_w=6.0, img_h=2.9,
                 panel_title="Two ways to connect",
                 caption="Series adds; parallel reduces the total",
                 notes="Contrast the two: series = same current, voltages add; "
                       "parallel = same voltage, currents add. Parallel total "
                       "is always less than the smallest resistor.")
    b.statement("SERIES", "Resistors in Series",
                "In a series circuit the same current flows through every "
                "resistor and the total resistance is their sum.",
                formula="R  =  R₁ + R₂ + R₃ + …",
                points=["The current is the same everywhere in the series.",
                        "The supply voltage is shared between the resistors.",
                        "Adding a resistor in series increases the total "
                        "resistance."],
                notes="Series: current common, voltages add up to the supply.")
    b.statement("PARALLEL", "Resistors in Parallel",
                "In a parallel circuit every resistor has the same voltage "
                "across it, and the currents through them add up.",
                formula="1/R  =  1/R₁ + 1/R₂ + 1/R₃ + …",
                points=["The voltage is the same across each branch.",
                        "The total current is the sum of the branch currents.",
                        "The combined resistance is LESS than the smallest "
                        "resistor."],
                notes="Parallel: voltage common, currents add. The equivalent "
                      "resistance falls — a frequent point of confusion.")
    b.worked("WORKED EXAMPLE", "Series and Parallel",
             "Two 6 Ω resistors are connected (a) in series and (b) in "
             "parallel. Find the equivalent resistance in each case.",
             ["(a) Series:  R = 6 + 6 = 12 Ω",
              "(b) Parallel:  1/R = 1/6 + 1/6 = 2/6 = 1/3",
              "R = 3 Ω"],
             "Series → 12 Ω;  Parallel → 3 Ω",
             notes="Note the pattern: two equal resistors give 2R in series "
                   "and R/2 in parallel. A handy shortcut to remember.")
    b.worked("WORKED EXAMPLE", "A Mixed Network",
             "Two 6 Ω resistors are joined in parallel, and this combination "
             "is in series with a 4 Ω resistor. Find the total resistance.",
             ["Parallel pair:  1/Rp = 1/6 + 1/6 = 2/6  →  Rp = 3 Ω",
              "Now in series with 4 Ω:  R = Rp + 4",
              "R = 3 + 4 = 7 Ω"],
             "Total resistance = 7 Ω",
             notes="Tackle mixed networks in stages: reduce the parallel part "
                   "first, then add the series resistor.")
    b.cards("BULB BRIGHTNESS", "Brighter in Series or in Parallel?", [
        ("Same bulbs, in series", "They share the supply voltage, so each gets "
         "less and all glow dimly."),
        ("Same bulbs, in parallel", "Each gets the full supply voltage, so each "
         "glows at full brightness."),
        ("If one fails (series)", "The single path breaks and all the bulbs go "
         "out."),
        ("If one fails (parallel)", "Only that branch goes out; the others "
         "keep glowing — why homes use parallel."),
    ], notes="Classic comparison: parallel bulbs are brighter and independent. "
             "Tie to why household wiring is parallel.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Combine Them", "Three 3 Ω resistors are connected in series. "
             "Their total resistance is:", ["1 Ω", "3 Ω", "9 Ω", "6 Ω"])
    b.quiz_a(1, "C. 9 Ω",
             "In series, resistances add: 3 + 3 + 3 = 9 Ω. Series always gives "
             "a total larger than any single resistor.")
    b.quiz_q(2, "Parallel Pair", "Two 4 Ω resistors are connected in parallel. "
             "The equivalent resistance is:", ["8 Ω", "4 Ω", "2 Ω", "0.5 Ω"])
    b.quiz_a(2, "C. 2 Ω",
             "For two equal resistors in parallel the result is half: "
             "4 / 2 = 2 Ω. The parallel total is always smaller than either "
             "resistor.")
    b.quiz_q(3, "Christmas Lights", "In some old light strings, if one bulb "
             "fails the whole string goes dark. The bulbs must be connected "
             "in:", ["Parallel", "Series", "A mixture", "It cannot be told"])
    b.quiz_a(3, "B. Series",
             "In series there is only one path, so a single broken bulb breaks "
             "the whole circuit. In parallel, each bulb has its own path and "
             "the others stay lit.")
    b.quiz_q(4, "Brighter Wiring", "House lights and sockets are wired in "
             "parallel rather than series so that:",
             ["They share one switch", "Each appliance gets the full mains "
              "voltage and can be switched independently",
              "Less copper is needed", "The current is smaller"])
    b.quiz_a(4, "B. Each gets full voltage and works independently",
             "In parallel every appliance receives the same full mains voltage "
             "and can be turned on or off without affecting the others — "
             "essential for a household.")
    b.quiz_q(5, "Reduce the Total", "You have three resistors. To get the "
             "SMALLEST possible total resistance you should connect them:",
             ["All in series", "All in parallel", "Two in series, one in "
              "parallel", "It makes no difference"])
    b.quiz_a(5, "B. All in parallel",
             "Parallel connection always gives an equivalent resistance "
             "smaller than the smallest resistor, because the current has "
             "several paths. Series would give the largest total.")
    b.divider(2, "Part 2", "Electrical Energy & Power",
              "Paying for electricity and the heating effect")
    b.statement("ENERGY", "Electrical Energy",
                "Electrical energy is the work done in driving charge around a "
                "circuit.",
                formula="W  =  V I t        (joules)",
                points=["V is the voltage, I the current, t the time in "
                        "seconds.",
                        "Using V = IR, it can also be written I²Rt or "
                        "(V²/R) t.",
                        "The SI unit of energy is the joule (J)."],
                notes="W = VIt, with the I²Rt and V²t/R forms following from "
                      "Ohm's law. Joule is the SI unit.")
    b.statement("POWER", "Electrical Power",
                "Power is the rate at which electrical energy is used or "
                "supplied.",
                formula="P  =  V I  =  I² R  =  V² / R        (watt)",
                points=["1 watt = 1 joule per second.",
                        "Choose the form that fits the quantities you are "
                        "given.",
                        "The power rating of an appliance (e.g. 60 W) tells "
                        "you its rate of energy use."],
                notes="Three forms of power for different given data. Tie to "
                      "appliance ratings the students see at home.")
    b.worked("WORKED EXAMPLE", "Power and Current",
             "An electric heater is marked 1500 W, 230 V. Find the current it "
             "draws and its resistance.",
             ["P = V I   →   I = P / V = 1500 / 230 ≈ 6.5 A",
              "R = V / I = 230 / 6.5 ≈ 35 Ω",
              "(or R = V² / P = 230² / 1500 ≈ 35 Ω)"],
             "I ≈ 6.5 A,  R ≈ 35 Ω",
             notes="Two routes to R — via I or directly from V²/P. Good chance "
                   "to show the equivalence.")
    b.statement("kWh", "The Kilowatt-Hour",
                "Electricity is sold not in joules but in kilowatt-hours — the "
                "energy used by a 1 kW appliance in 1 hour.",
                formula="Energy (kWh)  =  power (kW) × time (hours)",
                points=["1 kWh = 1000 W × 3600 s = 3.6 × 10⁶ J.",
                        "It is the 'unit' on your electricity bill.",
                        "Cost = number of units × price per unit."],
                notes="The kWh is the commercial 'unit'. Convert to joules "
                      "once so students see the size of it.")
    b.worked("WORKED EXAMPLE", "Cost of Electricity",
             "A 2 kW heater runs for 3 hours each day. At ₹6 per unit (kWh), "
             "find the cost for 30 days.",
             ["Energy per day = 2 kW × 3 h = 6 kWh",
              "Energy in 30 days = 6 × 30 = 180 kWh (units)",
              "Cost = 180 × ₹6 = ₹1080"],
             "Cost for the month = ₹1080",
             notes="Units (kWh) = kW × hours, then multiply by price. A "
                   "real-life calculation students can do at home.")
    b.bullets("HEATING EFFECT", "The Heating Effect of Current", [
        ("Why it heats", "Moving electrons collide with atoms, giving up "
         "energy as heat: H = I²Rt."),
        ("Depends on I²", "Doubling the current quadruples the heat produced."),
        ("Useful", "Heaters, electric irons, geysers, toasters and filament "
         "lamps."),
        ("Unwanted", "Overheated wires waste energy and can cause fires — "
         "hence fuses."),
    ], panel_title="H = I² R t",
       notes="Heating H = I²Rt; the I² dependence is key. Useful in heaters, "
             "a hazard in overloaded wiring.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Series", "R = R₁ + R₂ + …; same current"),
        ("Parallel", "1/R = 1/R₁ + 1/R₂ + …; same voltage, smaller total"),
        ("Energy", "W = V I t (joules)"),
        ("Power", "P = V I = I²R = V²/R (watts)"),
        ("kWh", "units = kW × hours; cost = units × price"),
        ("Heating effect", "H = I²R t; useful in heaters, controlled by fuses"),
    ], notes="Rapid recap; the kWh cost calculation and I²Rt heating are exam "
             "staples.")
    b.quiz_intro("Quiz 2", "Final Check — Energy & Power", 5)
    b.quiz_q(1, "Energy Used", "A 100 W bulb is left on for 10 hours. The "
             "energy it uses, in units (kWh), is:", ["1 unit", "10 units",
              "100 units", "1000 units"])
    b.quiz_a(1, "A. 1 unit",
             "Energy = power × time = 0.1 kW × 10 h = 1 kWh = 1 unit. Convert "
             "the 100 W to 0.1 kW first.")
    b.quiz_q(2, "Double the Current", "If the current through a heating "
             "element is doubled, the heat produced per second becomes:",
             ["Doubled", "Halved", "Four times as great", "Unchanged"])
    b.quiz_a(2, "C. Four times as great",
             "Heat per second = I²R. Because it depends on the square of the "
             "current, doubling I multiplies the heat by 2² = 4.")
    b.quiz_q(3, "Which Heats More?", "Two appliances run on the same mains "
             "voltage. The one with the higher power rating draws:",
             ["Less current and has more resistance",
              "More current and has less resistance",
              "The same current", "No current"])
    b.quiz_a(3, "B. More current and less resistance",
             "At fixed voltage, P = V²/R, so higher power means lower "
             "resistance; and P = VI means it also draws more current. A 2 kW "
             "heater pulls more current than a 60 W bulb.")
    b.quiz_q(4, "Cost", "An air-conditioner of 1.5 kW runs 8 hours a day. At "
             "₹5 per unit, the daily cost is:", ["₹12", "₹60", "₹40", "₹75"])
    b.quiz_a(4, "B. ₹60",
             "Energy = 1.5 kW × 8 h = 12 units. Cost = 12 × ₹5 = ₹60 per day.")
    b.quiz_q(5, "Same Bulb, Half Voltage", "A bulb of fixed resistance is run "
             "at half its normal voltage. The power it now uses is:",
             ["Half", "One quarter", "The same", "Double"])
    b.quiz_a(5, "B. One quarter",
             "P = V²/R with R fixed, so power depends on the square of the "
             "voltage. Half the voltage gives (½)² = ¼ of the power — which is "
             "why a dimmed bulb is much dimmer.")
    b.closing("Powering Everyday Life",
              "Series or parallel, joules or units — the same simple formulae "
              "run every circuit in your home.")
    return b


def build():
    for fname, fn in [("G10_S75_Current_Electricity_1.pptx", deck1),
                      ("G10_S76_Current_Electricity_2.pptx", deck2),
                      ("G10_S77_Current_Electricity_3.pptx", deck3)]:
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
