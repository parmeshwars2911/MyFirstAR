"""
Grade 9 Physics — Chapter: Current Electricity.
S113 (sources of DC, current, circuit symbols, simple circuit, conductors/
insulators, open/closed circuits) and S114 (electron flow, direction of
current, work, resistance, efficient use of energy).  ICSE Class 9.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade09"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Current Electricity  •  ICSE Class 9 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    sym = b.asset("g9ce_symbols", D.circuit_symbols("g9ce_symbols"))
    circ = b.asset("g9ce_simple", D.simple_circuit("g9ce_simple"))
    hero = b.asset("g9_circuit_hero", circ)

    b.title("ICSE • Class 9 • Electricity", "Electric Current & Circuits",
            "Sources of current  •  Circuit symbols  •  Simple circuits  •  "
            "Conductors & insulators", img=hero)
    b.objectives([
        "Name sources of direct current",
        "Define electric current and its unit",
        "Recognise the standard circuit symbols",
        "Draw and describe a simple electric circuit",
        "Distinguish conductors from insulators",
        "Distinguish open from closed circuits",
    ])
    b.divider(1, "Part 1", "Current, Sources & Symbols",
              "What current is and how we draw circuits")
    b.statement("CURRENT", "Electric Current",
                "An electric current is a flow of electric charge through a "
                "conductor.",
                formula="Current  I  =  charge Q / time t   (unit: ampere, A)",
                points=["It is driven round a circuit by a source such as a "
                        "cell.",
                        "Measured by an ammeter, connected in series.",
                        "A steady current in one direction is direct current "
                        "(DC)."],
                notes="Define current as flowing charge, I = Q/t, measured in "
                      "amperes by an ammeter in series.")
    b.cards("SOURCES", "Sources of Direct Current", [
        ("Cells & batteries", "Convert chemical energy into electrical energy "
         "(e.g. a torch cell)."),
        ("DC generator (dynamo)", "Converts mechanical energy into a direct "
         "current."),
        ("Solar cells", "Convert sunlight directly into a direct current."),
        ("Always one direction", "All these give direct current — it flows "
         "steadily one way."),
    ], notes="Sources of DC: cells, dynamos, solar cells. DC always flows in "
             "one direction, unlike AC.")
    b.cards("CELL TYPES", "Primary and Secondary Cells", [
        ("Primary cell", "Gives current from a chemical reaction that cannot be "
         "reversed — used up and thrown away (e.g. a dry cell)."),
        ("Secondary cell", "Can be recharged by passing current back through it "
         "(e.g. a car battery, a phone battery)."),
        ("Primary example", "The torch dry cell — cheap and convenient but "
         "not rechargeable."),
        ("Secondary example", "The lead-acid accumulator — stores charge and "
         "is reused many times."),
    ], notes="Primary = single-use (dry cell); secondary = rechargeable "
             "(accumulator/phone battery). A common Class 9 distinction.")
    b.cards("DC vs AC", "Direct and Alternating Current", [
        ("Direct current (DC)", "Flows steadily in one direction — from cells, "
         "batteries and solar cells."),
        ("Alternating current (AC)", "Reverses direction many times each second "
         "— supplied by the mains."),
        ("Mains in India", "AC at 50 hertz — it changes direction 100 times a "
         "second."),
        ("Which for what", "DC suits electronics and torches; AC is easy to "
         "transmit over long distances."),
    ], notes="DC (one direction, cells) vs AC (reversing, mains). Indian mains "
             "is 50 Hz AC.")
    b.text_image("SYMBOLS", "Symbols Used in Circuit Diagrams",
                 ["Circuits are drawn using simple, standard symbols.",
                  "A cell, a battery, a bulb, a switch, a resistor, an "
                  "ammeter and a voltmeter each have their own symbol.",
                  "Wires are shown as straight lines joining the components.",
                  "Using symbols makes circuits quick to draw and easy to "
                  "understand."],
                 sym, img_side="right", img_w=5.4, img_h=4.0,
                 panel_title="A common language for circuits",
                 caption="Standard symbols for circuit components",
                 notes="Go through each symbol. Students must be able to read "
                       "and draw these accurately.")
    b.text_image("SIMPLE CIRCUIT", "A Simple Electric Circuit",
                 ["A simple circuit has a source (cell), connecting wires, a "
                  "switch and a device (bulb).",
                  "When the switch is closed, current flows and the bulb "
                  "lights.",
                  "The current leaves the cell, passes through the bulb and "
                  "returns to the cell.",
                  "It must be a complete, unbroken loop for current to flow."],
                 circ, img_side="left", img_w=5.4, img_h=3.6,
                 panel_title="Cell, switch, bulb, wires",
                 caption="A complete loop lights the bulb",
                 notes="Trace the loop. Emphasise a complete path is essential "
                       "— leads into open/closed circuits.")
    b.cards("EFFECTS", "What an Electric Current Can Do", [
        ("Heating effect", "Current heats a wire — used in heaters, irons and "
         "filament bulbs."),
        ("Lighting effect", "It makes filaments and LEDs glow to give light."),
        ("Magnetic effect", "A current creates a magnetic field — used in "
         "electromagnets and motors."),
        ("Chemical effect", "It can drive chemical changes, as in "
         "electroplating and charging cells."),
    ], notes="The main effects of a current: heating, lighting, magnetic and "
             "chemical. Each underlies everyday devices.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "What Is Current?", "An electric current is best described as "
             "a:", ["Build-up of charge at a point", "Flow of electric charge "
              "through a conductor", "Type of magnet", "Form of light"])
    b.quiz_a(1, "B. Flow of electric charge through a conductor",
             "Current is moving charge. In a metal wire it is a flow of "
             "electrons driven round the circuit by the cell, measured in "
             "amperes.")
    b.quiz_q(2, "Measuring Current", "To measure the current in a circuit, an "
             "ammeter is connected:", ["In parallel with the bulb",
              "In series, in the main circuit", "Across the cell only",
              "Outside the circuit"])
    b.quiz_a(2, "B. In series, in the main circuit",
             "An ammeter must carry the whole current it measures, so it is "
             "connected in series — in the line of the circuit, not across a "
             "component.")
    b.quiz_q(3, "DC Source", "Which of these is NOT a source of direct "
             "current?", ["A torch cell", "A solar cell", "A car battery",
              "The mains socket at home"])
    b.quiz_a(3, "D. The mains socket at home",
             "Cells, batteries and solar cells all give direct current. The "
             "household mains supplies alternating current (AC), which "
             "reverses direction many times a second.")
    b.quiz_q(4, "Read the Symbol", "In a circuit diagram, a small circle with "
             "a cross inside it represents a:", ["Cell", "Switch", "Bulb "
              "(lamp)", "Resistor"])
    b.quiz_a(4, "C. Bulb (lamp)",
             "The crossed circle is the standard symbol for a lamp or bulb. A "
             "cell is two parallel lines of unequal length, and a resistor is "
             "a rectangle.")
    b.quiz_q(5, "Electromagnet", "An electromagnet works because an electric "
             "current produces a:", ["Heating effect only", "Magnetic effect",
              "Chemical effect", "Lighting effect"])
    b.quiz_a(5, "B. Magnetic effect",
             "A current flowing through a coil creates a magnetic field — the "
             "magnetic effect of current. This is what makes an electromagnet "
             "(and electric motors) work.")
    b.divider(2, "Part 2", "Conductors, Insulators & Circuits",
              "What carries current, and complete vs broken loops")
    b.cards("CONDUCTORS", "Conductors and Insulators", [
        ("Conductors", "Let current pass easily — they have free electrons "
         "(e.g. copper, silver, aluminium)."),
        ("Insulators", "Block current — they have almost no free electrons "
         "(e.g. rubber, glass, plastic)."),
        ("In a wire", "A copper core carries the current; a plastic sheath "
         "keeps it in and us safe."),
        ("Special cases", "Some materials (semiconductors) lie in between."),
    ], notes="Free electrons distinguish conductors from insulators. Link to "
             "the copper-core/plastic-sheath of everyday wires.")
    b.cards("OPEN vs CLOSED", "Open and Closed Circuits", [
        ("Closed circuit", "An unbroken loop — current flows and the bulb "
         "lights."),
        ("Open circuit", "A break somewhere (switch off or a loose wire) — no "
         "current flows."),
        ("The switch", "A switch simply opens or closes the circuit to turn a "
         "device off or on."),
        ("Fault finding", "A blown bulb or broken wire leaves the circuit open "
         "and dark."),
    ], notes="Closed = complete = current flows; open = broken = no current. "
             "The switch is just a controlled break.")
    b.bullets("CLOSED CIRCUIT", "Why the Loop Must Be Complete", [
        ("One unbroken path", "Charge can only flow round a continuous "
         "conducting loop."),
        ("Any break stops it", "A single gap anywhere stops the current "
         "everywhere."),
        ("The switch decides", "Closing the switch completes the loop; opening "
         "it breaks the loop."),
        ("Same current throughout", "In a single loop the same current passes "
         "through every part."),
    ], panel_title="No complete loop, no current",
       notes="Reinforce that current needs a complete path; one break stops "
             "the whole circuit.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Current", "flow of charge; I = Q/t; unit ampere; ammeter in series"),
        ("DC sources", "cells, batteries, dynamos, solar cells"),
        ("Symbols", "standard symbols for cell, bulb, switch, meters"),
        ("Simple circuit", "source + wires + switch + device in a loop"),
        ("Conductors/insulators", "free electrons let current pass or not"),
        ("Open/closed", "complete loop flows; a break stops the current"),
    ], notes="Rapid recap; the symbols and the open/closed-circuit idea are "
             "key.")
    b.quiz_intro("Quiz 2", "Final Check — Circuits", 5)
    b.quiz_q(1, "Bulb Won't Light", "A torch bulb does not light when the "
             "switch is on. The most likely reason is:",
             ["Too much current", "A break somewhere, leaving the circuit "
              "open", "The wires are too short", "The bulb is a conductor"])
    b.quiz_a(1, "B. A break, leaving the circuit open",
             "If the bulb stays dark with the switch on, the loop is not "
             "complete — perhaps a flat cell, a blown filament or a loose "
             "wire has left the circuit open.")
    b.quiz_q(2, "Best Conductor", "Which material would you choose to carry "
             "the current in a wire?", ["Rubber", "Glass", "Copper",
              "Plastic"])
    b.quiz_a(2, "C. Copper",
             "Copper is an excellent conductor with many free electrons and is "
             "affordable, so it is used for the current-carrying core of "
             "wires. Rubber, glass and plastic are insulators.")
    b.quiz_q(3, "Job of a Switch", "A switch in a circuit works by:",
             ["Storing charge", "Opening or closing the conducting loop",
              "Producing current", "Measuring voltage"])
    b.quiz_a(3, "B. Opening or closing the conducting loop",
             "A switch is simply a controlled break: closing it completes the "
             "loop so current flows, and opening it breaks the loop so the "
             "device turns off.")
    b.quiz_q(4, "Plastic Coating", "The plastic coating around an electric "
             "wire is there to:", ["Help it conduct better",
              "Insulate the wire, keeping current in and us safe",
              "Make it heavier", "Store charge"])
    b.quiz_a(4, "B. Insulate the wire and keep us safe",
             "Plastic is an insulator. The coating stops the current escaping "
             "the copper core and protects us from electric shock if we touch "
             "the wire.")
    b.quiz_q(5, "Same Current", "In a simple single-loop circuit, the current "
             "in the wire near the cell compared with the current in the bulb "
             "is:", ["Larger", "Smaller", "Exactly the same", "Zero"])
    b.quiz_a(5, "C. Exactly the same",
             "In a single unbroken loop there is only one path, so the same "
             "current flows through every part — the cell, the wires and the "
             "bulb all carry it equally.")
    b.closing("Completing the Circuit",
              "A source, a loop and a switch — the simple ingredients behind "
              "every electric device you use.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    circ = b.asset("g9ce_simple2", D.simple_circuit("g9ce_simple2"))
    hero = b.asset("g9_electron_hero", circ)

    b.title("ICSE • Class 9 • Electricity", "Electron Flow & Resistance",
            "Flow of electrons  •  Direction of current  •  Resistance  •  "
            "Using energy efficiently", img=hero)
    b.objectives([
        "Describe how electrons flow in a conductor",
        "Distinguish electron flow from conventional current direction",
        "Relate current to the work done by the source",
        "Explain electrical resistance",
        "List ways to use electrical energy efficiently",
        "Appreciate social initiatives to save energy",
    ])
    b.divider(1, "Part 1", "Electron Flow & Current Direction",
              "What really moves, and which way we say it goes")
    b.bullets("ELECTRON FLOW", "Flow of Electrons in a Conductor", [
        ("Free electrons", "A metal has loosely held free electrons that can "
         "drift through it."),
        ("The cell drives them", "The cell's energy pushes these electrons "
         "round the circuit."),
        ("From − to +", "Electrons flow from the negative terminal, through "
         "the circuit, to the positive terminal."),
        ("This drift is the current", "The steady drift of electrons "
         "constitutes the electric current."),
    ], panel_title="Free electrons on the move",
       notes="Electrons (negative) drift from − to + through the external "
             "circuit, driven by the cell. This drift IS the current.")
    b.statement("DIRECTION", "Direction of the Electric Current",
                "By convention, the direction of the current is taken to be "
                "the direction in which positive charge would flow — opposite "
                "to the electron flow.",
                points=["Conventional current: from + to − in the external "
                        "circuit.",
                        "Electron flow: from − to +, the opposite way.",
                        "This convention was fixed before the electron was "
                        "discovered."],
                notes="Conventional current (+ to −) is opposite to electron "
                      "flow (− to +). A historical convention students must "
                      "know.")
    b.statement("POTENTIAL DIFFERENCE", "Potential Difference (Voltage)",
                "The potential difference between two points is the work done "
                "in moving unit charge from one point to the other.",
                formula="V  =  work done / charge  =  W / Q   (unit: volt, V)",
                points=["It is the 'push' a cell gives to drive current round "
                        "a circuit.",
                        "Measured with a voltmeter, connected in parallel "
                        "(across a component).",
                        "1 volt means 1 joule of energy is given to each "
                        "coulomb of charge."],
                notes="Introduce p.d. as energy per unit charge (V = W/Q), "
                      "measured by a voltmeter in parallel. The 'push' driving "
                      "the current.")
    b.statement("WORK & ENERGY", "Current, Work and Energy",
                "As charge flows round a circuit, the cell does work on it, "
                "and that energy is delivered to the components.",
                formula="Work done  W  =  V × Q   (volts × coulombs = joules)",
                points=["The cell converts chemical energy into electrical "
                        "energy.",
                        "The bulb converts electrical energy into light and "
                        "heat.",
                        "Energy is transferred, not created or destroyed."],
                notes="The source does work moving charge (W = VQ). Energy is "
                      "transferred from cell to components and transformed.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "What Moves?", "In a copper wire carrying a current, the "
             "particles that actually move are the:", ["Protons",
              "Free electrons", "Whole atoms", "Neutrons"])
    b.quiz_a(1, "B. Free electrons",
             "Only the loosely held free electrons drift through the metal "
             "lattice. The positive ions stay fixed in place, so the current "
             "in a wire is a flow of electrons.")
    b.quiz_q(2, "Which Direction?", "In the wires outside the cell, the "
             "conventional current flows from the:",
             ["Negative to the positive terminal, like the electrons",
              "Positive to the negative terminal, opposite to the electrons",
              "Middle outward", "It does not flow"])
    b.quiz_a(2, "B. Positive to negative, opposite to the electrons",
             "Conventional current is defined as the direction positive charge "
             "would move: from + to − in the external circuit — the opposite "
             "of the actual electron flow.")
    b.quiz_q(3, "Energy Change in a Bulb", "In a glowing bulb, electrical "
             "energy is mainly changed into:", ["Sound and chemical energy",
              "Light and heat", "Magnetic energy only", "Nuclear energy"])
    b.quiz_a(3, "B. Light and heat",
             "The current heats the filament until it glows, converting "
             "electrical energy into light and heat — an energy "
             "transformation, with energy conserved overall.")
    b.quiz_q(4, "Cell's Job", "The cell in a circuit provides the energy to:",
             ["Create electrons", "Do work pushing charge around the circuit",
              "Destroy current", "Cool the wires"])
    b.quiz_a(4, "B. Do work pushing charge around the circuit",
             "The cell converts its chemical energy into electrical energy, "
             "doing work to drive the charge round the loop and deliver energy "
             "to the components.")
    b.quiz_q(5, "Energy Transformation", "In a torch, the overall energy "
             "change is from:", ["Light → chemical → electrical",
              "Chemical (cell) → electrical → light and heat",
              "Electrical → chemical → sound", "Heat → light → chemical"])
    b.quiz_a(5, "B. Chemical → electrical → light and heat",
             "The cell's chemical energy becomes electrical energy, which the "
             "bulb then converts into light and heat — a chain of energy "
             "transformations with energy conserved throughout.")
    b.divider(2, "Part 2", "Resistance & Saving Energy",
              "Opposition to current, and using energy wisely")
    b.statement("RESISTANCE", "Electrical Resistance",
                "Resistance is the opposition that a conductor offers to the "
                "flow of current through it.",
                formula="More resistance  →  less current for the same "
                        "voltage",
                points=["It arises as moving electrons collide with the atoms "
                        "of the conductor.",
                        "Good conductors have low resistance; poor conductors "
                        "have high resistance.",
                        "A long, thin wire resists more than a short, thick "
                        "one.",
                        "The unit of resistance is the ohm (Ω)."],
                notes="Resistance opposes current, from electron-atom "
                      "collisions. Introduce the ohm and the length/thickness "
                      "dependence simply.")
    b.cards("WHAT AFFECTS R", "What Affects a Wire's Resistance", [
        ("Length", "A longer wire has more resistance."),
        ("Thickness", "A thicker (greater area) wire has less resistance."),
        ("Material", "Different materials resist differently — copper resists "
         "less than iron."),
        ("Temperature", "For metals, resistance increases as the wire gets "
         "hotter."),
    ], notes="The factors affecting resistance: length, thickness, material "
             "and temperature — a Class 9 introduction to the idea.")
    b.cards("GROUPING CELLS", "Joining Cells in a Battery", [
        ("In series", "Cells joined + to − add their voltages, giving a higher "
         "total voltage."),
        ("In parallel", "Like cells joined + to + and − to − keep the same "
         "voltage but last longer."),
        ("A battery", "Two or more cells joined together form a battery."),
        ("Choosing", "Series for more voltage; parallel to supply current for "
         "longer."),
    ], notes="Cells in series add voltage; in parallel they keep the voltage "
             "but supply current longer. Several cells make a battery.")
    b.cards("EFFICIENT USE", "Using Electrical Energy Efficiently", [
        ("Switch off", "Turn off lights, fans and chargers when not in use."),
        ("LED lighting", "LEDs give the same light for far less electricity "
         "than old bulbs."),
        ("Star ratings", "Choose appliances with high energy-efficiency "
         "ratings."),
        ("Maintain appliances", "Clean, well-kept appliances waste less "
         "energy."),
    ], notes="Practical efficiency steps. Saving energy lowers bills and "
             "conserves fuel and the environment.")
    b.cards("SOCIAL INITIATIVES", "Saving Energy Together", [
        ("Awareness drives", "Campaigns encourage people to save electricity."),
        ("Efficiency labels", "Star-rating labels help buyers choose "
         "efficient appliances."),
        ("Public lighting", "Switching streetlights to LEDs saves large "
         "amounts of power."),
        ("Renewables", "Communities adopt solar power to reduce demand on the "
         "grid."),
    ], notes="Energy saving is also a social effort: awareness, labelling, "
             "efficient public lighting and renewables.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Electron flow", "free electrons drift from − to +"),
        ("Conventional current", "taken from + to −, opposite to electrons"),
        ("Work", "the cell does work W = V × Q on the charge"),
        ("Resistance", "opposition to current; unit ohm; from collisions"),
        ("Efficient use", "switch off, use LEDs, choose efficient appliances"),
        ("Social effort", "awareness, labels, public LED lighting, "
         "renewables"),
    ], notes="Rapid recap; electron vs conventional direction and resistance "
             "are the key ideas.")
    b.quiz_intro("Quiz 2", "Final Check — Electrons & Resistance", 5)
    b.quiz_q(1, "Higher Resistance", "Which wire of the same material has the "
             "greater resistance?", ["A short, thick wire",
              "A long, thin wire", "They are equal", "A coiled wire only"])
    b.quiz_a(1, "B. A long, thin wire",
             "Resistance increases with length and decreases with thickness, "
             "so a long, thin wire offers the most opposition to the current.")
    b.quiz_q(2, "Why Wires Warm", "A wire carrying a current becomes slightly "
             "warm because the moving electrons:",
             ["Create new energy", "Collide with the atoms of the wire, giving "
              "up energy as heat", "Slow down and stop", "Turn into heat"])
    b.quiz_a(2, "B. Collide with the atoms, giving up heat",
             "As electrons drift through the wire they repeatedly collide with "
             "its atoms, transferring energy that appears as heat — the "
             "resistance of the wire.")
    b.quiz_q(3, "Save the Most", "Replacing all the old filament bulbs in a "
             "house with LEDs will:", ["Increase the bill",
              "Give similar light using much less electricity",
              "Make the rooms darker", "Use more current"])
    b.quiz_a(3, "B. Give similar light using much less electricity",
             "LEDs convert far more of the electrical energy into light and "
             "waste much less as heat, so they provide the same brightness "
             "while using a fraction of the power.")
    b.quiz_q(4, "Electron Direction", "Inside the connecting wires of a "
             "torch, the electrons actually move:",
             ["From the + terminal to the − terminal",
              "From the − terminal to the + terminal",
              "In no particular direction", "Round in tiny circles"])
    b.quiz_a(4, "B. From the − terminal to the + terminal",
             "Electrons are pushed out of the negative terminal, through the "
             "circuit, and back to the positive terminal — opposite to the "
             "conventional current direction.")
    b.quiz_q(5, "Star Rating", "When buying a refrigerator, choosing one with "
             "a higher star rating means it:", ["Looks better",
              "Uses less electricity for the same job", "Is bigger",
              "Runs hotter"])
    b.quiz_a(5, "B. Uses less electricity for the same job",
             "Star ratings show energy efficiency: more stars means the "
             "appliance does the same work using less electrical energy, "
             "saving power and money.")
    b.closing("Electrons at Work",
              "Drifting electrons, a little resistance and wise use — the "
              "small ideas that power and conserve our world.")
    return b


def build():
    for fname, fn in [("G9_S113_Current_Electricity_1.pptx", deck1),
                      ("G9_S114_Current_Electricity_2.pptx", deck2)]:
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
