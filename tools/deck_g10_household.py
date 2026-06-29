"""
Grade 10 Physics — Chapter: Household Circuits.
S91 (transmission & distribution, house wiring, fuse, switches, dual-control),
S92 (earthing, 3-pin plug, colour coding, high-tension wires, safety).
ICSE Class 10 (Selina) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade10"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Household Circuits  •  ICSE Class 10 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    trans = b.asset("g10hc_trans", D.power_transmission("g10hc_trans"))
    plug = b.asset("g10hc_plug1", D.three_pin_plug("g10hc_plug1"))
    hero = b.asset("g10_house_hero", trans)

    b.title("ICSE • Class 10 • Electricity", "Power to Your Home",
            "Transmission & distribution  •  House wiring  •  Fuses  •  "
            "Switches & dual control", img=hero)
    b.objectives([
        "Describe how power reaches a house from the generating station",
        "Outline the wiring of a house from the supply",
        "Explain the purpose and action of a fuse",
        "Explain why a fuse is placed in the live wire",
        "Describe the role of switches in a circuit",
        "Explain a staircase (two-way) dual-control switch",
    ])
    b.divider(1, "Part 1", "From Station to Socket",
              "How electricity is delivered and distributed")
    b.text_image("TRANSMISSION", "Power From the Station",
                 ["Electricity is generated at a power station at a moderate "
                  "voltage.",
                  "A step-up transformer raises it to a very high voltage for "
                  "transmission.",
                  "High voltage means low current, so less energy is wasted as "
                  "heat in the cables.",
                  "Near towns, step-down transformers lower the voltage to a "
                  "safe level for homes (about 230 V)."],
                 trans, img_side="left", img_w=6.2, img_h=2.9,
                 panel_title="Step up, then step down",
                 caption="High-voltage transmission cuts energy loss",
                 notes="The key idea: transmit at high voltage to keep current "
                       "(and I²R losses) low, then step down for safe domestic "
                       "use.")
    b.bullets("DISTRIBUTION", "Power Distribution to a House", [
        ("Mains supply", "Two wires reach the house: live (at 230 V) and "
         "neutral (near 0 V)."),
        ("Electricity meter", "Records the energy used, in kilowatt-hours "
         "(units)."),
        ("Main fuse & switch", "Protect and isolate the whole house supply."),
        ("Distribution board", "Splits the supply into separate circuits for "
         "lights, sockets, etc."),
    ], panel_title="From the meter to the rooms",
       notes="Trace the path inside the house: meter → main switch/fuse → "
             "distribution board → individual circuits.")
    b.bullets("HOUSE WIRING", "How a House Is Wired", [
        ("Separate circuits", "Lights and power sockets are on their own "
         "circuits so a fault in one does not kill the others."),
        ("Everything in parallel", "Appliances are connected in parallel, so "
         "each gets the full 230 V and its own switch."),
        ("Live, neutral, earth", "Three wires run to each socket — live, "
         "neutral and earth."),
        ("Switches in the live", "Switches are placed in the live wire so "
         "that a switched-off appliance is truly safe."),
    ], panel_title="Parallel circuits, three wires",
       notes="Two big ideas: parallel connection (full voltage, independent), "
             "and switches/fuses in the LIVE wire for safety.")
    b.statement("THE FUSE", "The Fuse — a Safety Weak Link",
                "A fuse is a short piece of thin wire that melts and breaks "
                "the circuit if the current becomes dangerously large.",
                formula="Fuse rating  >  normal current,  but limits faults",
                points=["It is made of a metal with a low melting point.",
                        "It is connected in the LIVE wire, so a blown fuse "
                        "isolates the appliance from the live supply.",
                        "Without it, an overload could overheat the wiring and "
                        "start a fire."],
                notes="Fuse = deliberate weak link in the live wire. It melts "
                      "on overload, cutting the live connection.")
    b.cards("MCB", "The Modern Alternative: MCB", [
        ("What it is", "A Miniature Circuit Breaker — an automatic switch that "
         "trips off when the current is too large."),
        ("Reusable", "Unlike a fuse, it is simply switched back on after the "
         "fault is fixed — no wire to replace."),
        ("Fast acting", "It breaks the circuit quickly on an overload or short "
         "circuit."),
        ("In the live wire", "Like a fuse, it is connected in the live wire of "
         "the circuit."),
    ], notes="MCBs are the modern replacement for fuses: automatic, reusable, "
             "still in the live wire.")
    b.cards("OVERLOAD vs SHORT", "Overload and Short Circuit", [
        ("Overload", "Too many appliances draw more current than the wiring is "
         "rated for, so it overheats."),
        ("Short circuit", "Live and neutral touch directly, giving a very large "
         "current through almost no resistance."),
        ("Same protection", "Both make the current shoot up, so the fuse or "
         "MCB cuts the supply."),
        ("Why dangerous", "Either can melt insulation and start a fire if not "
         "interrupted quickly."),
    ], notes="Distinguish overload (too many appliances) from a short circuit "
             "(live-neutral contact). Both trip the fuse/MCB.")
    b.worked("WORKED EXAMPLE", "Choosing a Fuse Rating",
             "A 230 V electric kettle is rated 2300 W. What is the smallest "
             "standard fuse (3 A, 5 A, 13 A) that suits it?",
             ["Normal current  I = P / V = 2300 / 230 = 10 A",
              "The fuse must carry 10 A in normal use without blowing.",
              "So 3 A and 5 A are too small; the 13 A fuse is the right "
              "choice."],
             "Use a 13 A fuse (the next standard value above 10 A)",
             notes="Find the normal current from P = VI, then pick the next "
                   "standard fuse just above it. Too low blows in normal use.")
    b.cards("WHY LIVE WIRE", "Why the Fuse & Switch Go in the Live Wire", [
        ("Fuse in live", "When it blows, the appliance is cut off from the "
         "dangerous live voltage."),
        ("Fuse in neutral?", "Would stop the current, but the appliance would "
         "still be connected to the live wire — unsafe."),
        ("Switch in live", "An 'off' switch then truly disconnects the live "
         "supply."),
        ("Golden rule", "Anything that breaks the circuit for safety goes in "
         "the live wire."),
    ], notes="Drive home the rule. A fuse/switch in the neutral would still "
             "leave the appliance live and dangerous.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Why High Voltage?", "Electricity is transmitted over long "
             "distances at very high voltage mainly to:",
             ["Make the wires glow", "Reduce the current and so cut energy "
              "lost as heat in the cables", "Increase the current",
              "Make it safer to touch"])
    b.quiz_a(1, "B. Reduce current and cut heat loss",
             "Power lost in a cable is I²R. Sending power at high voltage "
             "means a smaller current for the same power, so far less energy "
             "is wasted heating the long transmission lines.")
    b.quiz_q(2, "Fuse Placement", "A fuse is always placed in the live wire "
             "rather than the neutral wire because:",
             ["The live wire is thicker", "A blown fuse then disconnects the "
              "appliance from the live supply, making it safe",
              "Neutral wires cannot melt", "It looks neater"])
    b.quiz_a(2, "B. It disconnects the appliance from the live supply",
             "If the fuse were in the neutral, a blown fuse would stop the "
             "current but leave the appliance still joined to the live wire — "
             "a shock hazard. In the live wire, a blown fuse makes it safe.")
    b.quiz_q(3, "All in Parallel", "Home appliances are connected in parallel "
             "so that each one:", ["Shares the voltage with the others",
              "Receives the full mains voltage and can be switched "
              "separately", "Carries the same current",
              "Has the same resistance"])
    b.quiz_a(3, "B. Gets full voltage and switches separately",
             "Parallel connection puts the full 230 V across every appliance "
             "and gives each its own switch, so they work independently of "
             "one another.")
    b.quiz_q(4, "Choosing a Fuse", "A 230 V appliance normally draws 3 A. The "
             "most suitable fuse for it is:", ["A 1 A fuse", "A 2 A fuse",
              "A 5 A fuse", "A 30 A fuse"])
    b.quiz_a(4, "C. A 5 A fuse",
             "The fuse must be just above the normal current so it carries 3 A "
             "safely but blows on a fault. A 5 A fuse fits; 1–2 A would blow "
             "in normal use and 30 A would never protect it.")
    b.quiz_q(5, "Short vs Overload", "Live and neutral wires accidentally touch "
             "inside an appliance. This is a:", ["Normal load",
              "Short circuit, drawing a very large current",
              "Earth fault that is harmless", "Drop in voltage"])
    b.quiz_a(5, "B. Short circuit, drawing a very large current",
             "With live and neutral in direct contact there is almost no "
             "resistance, so a huge current flows. The fuse or MCB must trip "
             "at once to prevent the wiring overheating.")
    b.divider(2, "Part 2", "Switches & Dual Control",
              "Controlling lights from more than one place")
    b.bullets("SWITCHES", "Switches in a Circuit", [
        ("Job of a switch", "To make (close) or break (open) a circuit, "
         "turning an appliance on or off."),
        ("In the live wire", "Placed in the live wire so the appliance is "
         "isolated from the live supply when off."),
        ("One-way switch", "A simple on/off switch controlling a light from a "
         "single point."),
        ("Need for two-way", "Staircases and long corridors need control from "
         "two places."),
    ], panel_title="Make or break the circuit",
       notes="Define a switch's job and why it sits in the live wire, leading "
             "into the two-way switch.")
    b.statement("DUAL CONTROL", "Two-Way (Staircase) Switches",
                "Two two-way switches let a single light be turned on or off "
                "from two different places — like the top and bottom of a "
                "staircase.",
                points=["Each switch can connect the live wire through one of "
                        "two paths.",
                        "Changing either switch makes or breaks the complete "
                        "circuit.",
                        "So the light's state can be flipped from either "
                        "location."],
                notes="Explain the staircase wiring conceptually: either switch "
                      "toggles the light because each offers two alternative "
                      "paths.")
    b.cards("EVERYDAY", "Where Dual Control Helps", [
        ("Staircases", "Switch the light on going up, off at the top."),
        ("Long corridors", "Control from both ends."),
        ("Bedrooms", "A switch at the door and one by the bed."),
        ("Big halls", "Several entrances, each with control of the lights."),
    ], notes="Relatable examples of two-way switching. Ask students where they "
             "have seen staircase switches.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Transmission", "step up to high voltage to cut I²R losses, then step "
         "down"),
        ("Distribution", "meter → main switch/fuse → distribution board → "
         "circuits"),
        ("House wiring", "appliances in parallel; live, neutral, earth"),
        ("Fuse", "thin low-melting wire in the live; melts on overload"),
        ("Live-wire rule", "fuses and switches go in the live wire"),
        ("Two-way switch", "control one light from two places"),
    ], notes="Rapid recap; the live-wire safety rule is the key takeaway.")
    b.quiz_intro("Quiz 2", "Final Check — Wiring & Switches", 5)
    b.quiz_q(1, "Switch Off, Still Live?", "A lamp is switched off, but its "
             "switch was wrongly fitted in the neutral wire. The lamp is:",
             ["Completely safe", "Off, but its live wire is still connected, "
              "so it is a shock hazard", "Still glowing", "Earthed"])
    b.quiz_a(1, "B. Off but still connected to live — a hazard",
             "A switch in the neutral can turn the lamp off, but the lamp "
             "stays joined to the live wire. Anyone touching a fault could get "
             "a shock. That is why switches go in the live wire.")
    b.quiz_q(2, "Overload", "Too many high-power appliances are plugged into "
             "one circuit. The most likely result is:",
             ["The voltage rises", "The current rises and the fuse blows (or "
              "the wiring overheats)", "The appliances speed up",
              "Nothing happens"])
    b.quiz_a(2, "B. Current rises and the fuse blows",
             "Each appliance adds to the current in the shared wire. The total "
             "can exceed the safe limit, melting the fuse (its job) before the "
             "wiring overheats and causes a fire.")
    b.quiz_q(3, "Staircase Light", "A single light controlled from both the "
             "top and bottom of a staircase uses:",
             ["One ordinary switch", "Two two-way (dual-control) switches",
              "A fuse at each end", "No switch at all"])
    b.quiz_a(3, "B. Two two-way switches",
             "Two-way switches at each end let either one make or break the "
             "circuit, so the light can be toggled from the top or the bottom "
             "of the stairs.")
    b.quiz_q(4, "Meter Reads", "The electricity meter in a house measures the:",
             ["Voltage of the supply", "Current drawn at that instant",
              "Energy used, in kilowatt-hours", "Resistance of the wiring"])
    b.quiz_a(4, "C. Energy used, in kilowatt-hours",
             "The meter totals the electrical energy consumed over time, in "
             "kilowatt-hours (units). The bill is the number of units times "
             "the price per unit.")
    b.quiz_q(5, "Lights vs Sockets", "Why are the lights and the power sockets "
             "of a house put on separate circuits?",
             ["To use more wire", "So a fault or overload in one does not "
              "switch off the other", "To save voltage",
              "Because lights need no current"])
    b.quiz_a(5, "B. A fault in one keeps the other working",
             "Separate circuits (with their own fuses) mean a problem in the "
             "socket circuit will not plunge the lights into darkness, and "
             "each can be rated for its expected current.")
    b.closing("Electricity, Delivered Safely",
              "From a distant turbine to your bedside lamp — transformers, "
              "fuses and careful wiring keep the power flowing safely.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    plug = b.asset("g10hc_plug2", D.three_pin_plug("g10hc_plug2"))
    hero = b.asset("g10_house_hero", plug)

    b.title("ICSE • Class 10 • Electricity", "Earthing, Plugs & Safety",
            "Earthing  •  The three-pin plug  •  Colour coding  •  Electrical "
            "safety", img=hero)
    b.objectives([
        "Explain the purpose of earthing an appliance",
        "Identify the three pins of a plug and their wires",
        "State the colour code of live, neutral and earth wires",
        "Explain why the earth pin is longer and thicker",
        "Describe the danger of high-tension wires",
        "List safety precautions for using electricity",
    ])
    b.divider(1, "Part 1", "Earthing & the Three-Pin Plug",
              "How an appliance is made safe to touch")
    b.statement("EARTHING", "Why We Earth Appliances",
                "Earthing connects the metal body of an appliance to the "
                "ground through the earth wire, so it can never reach a "
                "dangerous voltage.",
                points=["If the live wire touches the metal body, current "
                        "flows safely to earth instead of through a person.",
                        "This large current also blows the fuse, cutting off "
                        "the supply.",
                        "Without earthing, the body would stay live and give a "
                        "shock when touched."],
                notes="Earthing gives a safe, low-resistance path for fault "
                      "current — protecting the user and blowing the fuse.")
    b.text_image("THREE-PIN PLUG", "Inside a Three-Pin Plug",
                 ["The three pins are live (L), neutral (N) and earth (E).",
                  "The earth pin is longer, so it connects first and "
                  "disconnects last.",
                  "It is also thicker to carry a large fault current safely.",
                  "The fuse is fitted in the live wire of the plug."],
                 plug, img_side="right", img_w=4.4, img_h=4.0,
                 panel_title="Live, neutral & earth",
                 caption="Earth pin: longer and thicker; fuse in the live",
                 notes="Walk through the three pins. The longer earth pin "
                       "connects first (safety); the fuse is in the live wire.")
    b.cards("TWO PROTECTIONS", "Fuse and Earthing Do Different Jobs", [
        ("Fuse", "Protects the wiring — it melts to cut off a dangerously "
         "large current."),
        ("Earthing", "Protects the user — it keeps the metal body at earth "
         "potential, safe to touch."),
        ("They work together", "On a fault the earth wire carries a large "
         "current that then blows the fuse."),
        ("Both needed", "A fuse alone leaves the body live until it blows; "
         "earthing makes that instant safe."),
    ], notes="Key distinction: the fuse protects the circuit/wiring, earthing "
             "protects the person. Together they make a fault safe.")
    b.cards("COLOUR CODE", "Colour Coding of Wires", [
        ("Live — brown", "Carries the dangerous 230 V supply (older code: "
         "red)."),
        ("Neutral — blue", "Completes the circuit, near 0 V (older code: "
         "black)."),
        ("Earth — green/yellow", "The safety wire to the ground (older code: "
         "green)."),
        ("Why colours", "So wires are connected to the correct terminals "
         "every time."),
    ], notes="Memorise the modern code: brown live, blue neutral, green/yellow "
             "earth. Wrong connections are dangerous.")
    b.bullets("EARTH PIN", "Why the Earth Pin Is Special", [
        ("Longer", "It makes contact first when plugging in, so the appliance "
         "is earthed before it is live."),
        ("Thicker", "It can safely carry a large fault current to the ground."),
        ("Opens the shutters", "In many sockets the long earth pin pushes "
         "open safety shutters over the live and neutral holes."),
        ("Connected to the body", "Inside the appliance the earth wire is "
         "joined to its metal casing."),
    ], panel_title="First to connect, last to leave",
       notes="The earth pin's length and thickness are favourite exam points: "
             "connects first, carries fault current, opens shutters.")
    b.bullets("HOW WE EARTH", "How a House Is Earthed", [
        ("Earth electrode", "A metal plate or pipe is buried deep in moist "
         "ground near the house."),
        ("Low resistance", "It is surrounded by charcoal and salt to keep the "
         "earth connection low in resistance."),
        ("Earth wire", "A thick wire links the electrode to the earth pins of "
         "all the sockets."),
        ("Why moist soil", "Damp, salted earth conducts well, giving fault "
         "current an easy path to ground."),
    ], panel_title="Plate or pipe earthing",
       notes="Outline plate/pipe earthing: a buried electrode in salted, "
             "charcoal-packed moist soil, linked by a thick earth wire.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Fault to the Body", "The live wire inside a metal toaster "
             "comes loose and touches the casing. If the toaster is properly "
             "earthed, what happens?",
             ["The casing becomes live and dangerous",
              "A large current flows to earth and blows the fuse, cutting the "
              "supply", "Nothing changes", "The toaster runs faster"])
    b.quiz_a(1, "B. Current flows to earth and blows the fuse",
             "Earthing offers a low-resistance path to ground. The fault "
             "current is large, so the fuse melts and disconnects the supply, "
             "leaving the casing safe to touch.")
    b.quiz_q(2, "Colour Check", "In the modern colour code, the wire that is "
             "brown is the:", ["Earth wire", "Neutral wire", "Live wire",
              "Signal wire"])
    b.quiz_a(2, "C. Live wire",
             "The modern code is brown = live, blue = neutral, green/yellow = "
             "earth. The brown live wire carries the dangerous 230 V.")
    b.quiz_q(3, "Longer Pin", "The earth pin of a plug is made longer than the "
             "other two so that:", ["It looks different",
              "The appliance is earthed first, before the live pin makes "
              "contact", "It carries the current", "It fits more tightly"])
    b.quiz_a(3, "B. The appliance is earthed before it goes live",
             "The longer earth pin enters the socket first and leaves last, so "
             "the appliance is safely earthed throughout the moment it is live "
             "— and it often opens the socket's safety shutters too.")
    b.quiz_q(4, "No Earth", "A plastic-bodied hair dryer with no metal parts "
             "is often sold with only two pins (no earth) because:",
             ["Plastic conducts electricity", "Its non-conducting case can "
              "never become live, so earthing is not needed",
              "It uses no current", "Earthing would damage it"])
    b.quiz_a(4, "B. The plastic case can never become live",
             "Earthing protects a conducting (metal) body. A fully insulated "
             "plastic body cannot give a shock even if a wire touches it, so "
             "such 'double-insulated' devices need no earth pin.")
    b.quiz_q(5, "Fuse or Earth?", "Which statement correctly matches each "
             "safety device to its job?",
             ["The fuse protects the user; earthing protects the wiring",
              "The fuse protects the wiring; earthing protects the user",
              "Both protect only the wiring", "Both protect only the user"])
    b.quiz_a(5, "B. Fuse protects the wiring; earthing protects the user",
             "The fuse melts to stop a dangerous current overheating the "
             "wiring. Earthing keeps the metal body at earth potential so it is "
             "safe to touch — and the fault current it carries then blows the "
             "fuse.")
    b.divider(2, "Part 2", "High-Tension Wires & Safety",
              "Respecting the dangers of electricity")
    b.bullets("HIGH TENSION", "High-Tension (HT) Wires", [
        ("Very high voltage", "Transmission lines carry tens of thousands of "
         "volts."),
        ("Bare and high up", "They are uninsulated, so they are strung high on "
         "tall pylons, out of reach."),
        ("Keep away", "Never fly kites or raise poles near them — electricity "
         "can jump (arc) across a gap."),
        ("Warning signs", "Danger boards and wide clearances keep people and "
         "vehicles at a safe distance."),
    ], panel_title="Why HT lines are kept out of reach",
       notes="HT wires are bare and lethal; height and distance are the "
             "safety measures. Stress kite/pole dangers.")
    b.cards("SAFETY", "Safety Precautions With Electricity", [
        ("Dry hands", "Never touch switches or appliances with wet hands — "
         "water conducts electricity."),
        ("Right fuse", "Always use a fuse of the correct rating; never replace "
         "it with thick wire."),
        ("Earth metal appliances", "Connect the earth pin; do not bypass it."),
        ("Repairs off", "Switch off and unplug before repairing or cleaning "
         "an appliance."),
    ], notes="Practical safety rules. Connect each to the physics: water "
             "conducts, correct fuse protects, earthing saves lives.")
    b.bullets("MORE SAFETY", "Good Habits That Save Lives", [
        ("No overloading", "Avoid plugging many high-power appliances into one "
         "socket."),
        ("Good insulation", "Replace frayed or damaged wires and cracked "
         "plugs promptly."),
        ("Three-pin for metal", "Always use an earthed three-pin plug for "
         "metal-bodied appliances."),
        ("Keep water away", "Keep electrical points away from taps, sinks and "
         "bathrooms unless specially protected."),
    ], panel_title="Everyday electrical sense",
       notes="Reinforce habits: no overloading, good insulation, earthing, "
             "water awareness.")
    b.cards("DOUBLE INSULATION", "Double-Insulated Appliances", [
        ("Two layers", "The live parts are insulated, and the whole casing is "
         "a second layer of insulation."),
        ("No earth needed", "Because the case can never become live, no earth "
         "wire is required."),
        ("The symbol", "Marked with a 'square within a square' symbol."),
        ("Examples", "Plastic hair dryers, electric shavers and many power "
         "tools."),
    ], notes="Double insulation is an alternative to earthing for "
             "plastic-bodied devices — two independent layers of insulation.")
    b.bullets("ELECTRIC SHOCK", "If Someone Gets an Electric Shock", [
        "Switch off the mains supply immediately — do not touch the person "
        "while they are still connected.",
        "If you cannot reach the switch, push them away using a dry, "
        "non-conducting object like wood.",
        "Never use your bare hands or anything wet or metal.",
        "Once they are clear, call for medical help and give first aid if "
        "trained.",
    ], panel_title="Cut the supply first",
       notes="Emphasise: isolate the supply before touching the casualty, and "
             "only use dry, insulating materials.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Earthing", "safe path to ground; protects user and blows the fuse"),
        ("Three pins", "live, neutral, earth; fuse in the live wire"),
        ("Colour code", "brown live, blue neutral, green/yellow earth"),
        ("Earth pin", "longer and thicker — connects first, carries fault "
         "current"),
        ("HT wires", "very high voltage, bare, kept high and out of reach"),
        ("Safety", "dry hands, correct fuse, earthing, switch off to repair"),
    ], notes="Rapid recap; the earthing mechanism and colour code are the most "
             "examined points.")
    b.quiz_intro("Quiz 2", "Final Check — Safety", 5)
    b.quiz_q(1, "Wet Hands", "Touching an electric switch with wet hands is "
             "dangerous because:", ["Water repels electricity",
              "Water conducts electricity, lowering your resistance and "
              "allowing a larger shock current", "Switches dislike water",
              "It increases the voltage"])
    b.quiz_a(1, "B. Water conducts, allowing a larger shock current",
             "Wet skin has a much lower resistance than dry skin, so for the "
             "same voltage a far larger and more dangerous current can flow "
             "through the body.")
    b.quiz_q(2, "Thick Wire as Fuse", "Replacing a blown fuse with a thick "
             "copper wire is dangerous because the thick wire:",
             ["Melts too easily", "Will not melt on an overload, so the wiring "
              "can overheat and catch fire", "Carries no current",
              "Increases the voltage"])
    b.quiz_a(2, "B. Won't melt, so the wiring can overheat",
             "A fuse is meant to be the weak link that melts first. A thick "
             "copper wire can carry a huge current without melting, so it "
             "removes the protection and the wiring itself may overheat.")
    b.quiz_q(3, "Kite Warning", "Why must you never fly a kite near "
             "high-tension power lines?", ["The kite may get dirty",
              "Electricity can arc across to a wet string or the kite, giving "
              "a fatal shock", "The lines will fall", "The kite flies too "
              "high"])
    b.quiz_a(3, "B. Electricity can arc across to the string",
             "At tens of thousands of volts, current can jump across a small "
             "air gap to a kite or a damp string, sending a lethal current "
             "down to the person holding it.")
    b.quiz_q(4, "Bird on a Wire", "A bird can sit safely on a single bare "
             "power line because:", ["Its feet are insulated",
              "There is no potential difference across its body — both feet "
              "are on the same wire", "Birds do not conduct", "The wire is "
              "switched off"])
    b.quiz_a(4, "B. No potential difference across its body",
             "Both feet touch the same point, so there is almost no voltage "
             "difference across the bird and almost no current through it. "
             "Touching a second wire or the ground would be fatal.")
    b.quiz_q(5, "Before Repair", "Before repairing an electrical appliance you "
             "should always first:", ["Wet your hands", "Switch off and "
              "unplug it from the mains", "Increase the current",
              "Remove the earth wire"])
    b.quiz_a(5, "B. Switch off and unplug it",
             "Disconnecting the appliance from the live supply removes the "
             "source of danger, so no current can flow through you while you "
             "work on it.")
    b.closing("Stay Safe With Electricity",
              "Earthing, the right fuse and a little caution turn a deadly "
              "force into a everyday convenience.")
    return b


def build():
    for fname, fn in [("G10_S91_Household_Circuits_1.pptx", deck1),
                      ("G10_S92_Household_Circuits_2.pptx", deck2)]:
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
