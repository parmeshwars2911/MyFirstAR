"""
Grade 6 Physics teaching decks (ICSE / Selina Concise Physics).

Chapters covered (teach-sessions after day 29 in the planner):
  - Simple Machines : S30 (Lesson 1), S31 (Lesson 2)
  - Light           : S52 (Lesson 1), S53 (Lesson 2)
  - Magnetism       : S69 (Lesson 1), S70 (Lesson 2)

Language is pitched for Class 6. Schematics come from diagrams.py /
diagrams_extra.py (SVG -> PNG); optional real photos are picked up by
b.asset(key, fallback) if generated into assets/img/.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D
import diagrams_extra as DX
import slidekit as SK

# House style for every deck (no footer/branding on slides, neutral title
# eyebrows, icon cards, and quiz answer slides that mirror the question slide
# with the correct option selected). One monkeypatch, no call-site edits.
SK.apply_house_style()

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade06"))
os.makedirs(OUT, exist_ok=True)


# ===========================================================================
# SIMPLE MACHINES
# ===========================================================================
# No footer / branding on slides (per instruction): footer="" and brand="".


def sm_deck1():
    """S30 — Simple Machines 1: work, machines, MA, efficiency, levers."""
    b = Builder("", accent=C["teal"], brand="")
    lever1 = DX.lever("g6sm1_lever1", 1)
    lever2 = DX.lever("g6sm1_lever2", 2)
    lever3 = DX.lever("g6sm1_lever3", 3)
    principle = DX.lever_principle("g6sm1_principle")

    b.title("Mechanics", "Simple Machines — 1",
            "Work and energy  •  What a machine does  •  Mechanical advantage  "
            "•  Efficiency  •  Levers", img=principle)
    b.objectives([
        "Explain what work means in science and give its unit",
        "Say what a machine is and the jobs a machine can do for us",
        "Define mechanical advantage and use MA = load / effort",
        "Explain efficiency and why no real machine is perfect",
        "Tell an ideal machine apart from an actual machine",
        "Identify the three orders (classes) of levers",
    ])

    # ---- Part 1 : Work, energy and machines ----
    b.divider(1, "Part 1", "Work, Energy & Machines",
              "What 'work' really means and how a machine helps")
    b.statement("WORK", "What Is Work?",
                "Work is done only when a force makes a body move in the "
                "direction of the force.",
                formula="Work  =  Force  ×  distance moved   (W = F × d)",
                points=["If you push a wall and it does not move, no work is "
                        "done — there is force but no movement.",
                        "The SI unit of work is the joule (J).",
                        "1 joule of work is done when a force of 1 newton moves "
                        "a body through 1 metre.",
                        "Both a force AND movement in the force's direction are "
                        "needed for work to be done."],
                notes="Start from the everyday meaning of 'work', then sharpen "
                      "it. Use the pushing-a-wall example to show force alone "
                      "is not enough — there must be movement. Keep the unit "
                      "(joule) concrete with the 1 N × 1 m picture.")
    b.cards("ENERGY", "Energy — the Ability to Do Work", [
        ("What energy is", "Energy is the capacity (ability) to do work. A "
         "body that can do work is said to have energy."),
        ("Same unit as work", "Energy is also measured in joules (J), because "
         "doing work transfers energy."),
        ("Everyday energy", "Food gives our muscles energy; petrol gives a car "
         "energy; a stretched rubber band stores energy."),
        ("Work needs energy", "To do work, a body must spend energy. The more "
         "work done, the more energy used."),
    ], notes="Link energy directly to work: anything that can do work has "
             "energy, and both share the joule. Give a few stores of energy "
             "the children already know — food, fuel, a wound spring.")
    b.text_image("MACHINES", "What Is a Machine?",
                 ["A machine is a device that lets us do work more easily or "
                  "more conveniently.",
                  "We apply a small force called the effort; the machine moves "
                  "a large load.",
                  "The effort is the force we put in; the load is the "
                  "resistance the machine overcomes.",
                  "Simple machines like the lever, pulley and ramp are the "
                  "building blocks of bigger machines."],
                 principle, img_side="left", panel_title="Effort and load",
                 caption="A machine turns a small effort into a large load",
                 notes="Define machine in plain terms — it makes our work "
                       "easier. Introduce the two key words effort (input) and "
                       "load (output) here; they recur all session.")
    b.cards("FUNCTIONS", "Four Jobs a Machine Can Do", [
        ("Lift a big load", "It lets a small effort move a large load — a "
         "force multiplier, like a crowbar lifting a rock."),
        ("Change direction", "It can change the direction of the force — a "
         "fixed pulley lets us pull down to lift a load up."),
        ("Change the speed", "It can make something move faster — the wheels "
         "of a bicycle are a speed multiplier."),
        ("Reach a better point", "It can apply the force at a more convenient "
         "place, like the pedals of a bicycle."),
    ], notes="Walk through the four ways machines help. Stress that not every "
             "machine multiplies force — some trade force for speed, some just "
             "change direction or the point of application.")
    b.statement("MECHANICAL ADVANTAGE", "Mechanical Advantage (MA)",
                "Mechanical advantage tells us how many times a machine "
                "multiplies our effort.",
                formula="MA  =  Load  /  Effort",
                points=["MA is just a ratio of two forces, so it has no unit.",
                        "If MA is more than 1, the machine is a force "
                        "multiplier — the load is bigger than the effort.",
                        "If MA is less than 1, we gain speed or distance "
                        "instead of force.",
                        "Example: lifting a 100 N load with a 25 N effort gives "
                        "MA = 100 / 25 = 4."],
                notes="Define MA as load over effort. Make the 'how many times' "
                      "idea concrete with the worked number. Note MA has no "
                      "unit because it is force divided by force.")
    b.statement("EFFICIENCY", "Efficiency of a Machine",
                "Efficiency tells us how much of the work we put in actually "
                "comes out as useful work.",
                formula="Efficiency  =  (useful work output / work input) × 100%",
                points=["Some effort is always wasted against friction and in "
                        "moving the machine's own parts.",
                        "So the useful work we get out is always less than the "
                        "work we put in.",
                        "A real machine therefore always has an efficiency "
                        "less than 100%.",
                        "Oiling the parts reduces friction and raises the "
                        "efficiency."],
                notes="Explain efficiency as the fraction of input work that is "
                      "useful. Connect the 'lost' part to friction and the "
                      "weight of the machine. Lead into the ideal-vs-actual "
                      "comparison next.")
    b.cards("IDEAL vs ACTUAL", "Ideal Machine vs Actual Machine", [
        ("Ideal machine", "An imaginary machine with no friction and "
         "weightless parts. Its efficiency would be 100%."),
        ("Actual machine", "A real machine has friction and its parts have "
         "weight, so its efficiency is always below 100%."),
        ("Where work goes", "In a real machine some input work is wasted "
         "against friction and in lifting the moving parts."),
        ("Getting closer", "Good design and regular oiling cut friction and "
         "make a real machine behave more like an ideal one."),
    ], notes="Contrast the perfect (ideal) machine with real ones. The key "
             "reason real machines fall short is friction plus the weight of "
             "their own parts.")
    b.worked("WORKED EXAMPLE", "Finding Mechanical Advantage",
             "A boy uses a crowbar to lift a stone of weight 200 N by applying "
             "an effort of 50 N. Find the mechanical advantage.",
             ["MA = Load / Effort",
              "Load = 200 N,  Effort = 50 N",
              "MA = 200 / 50",
              "MA = 4"],
             "MA = 4  (the crowbar multiplies the effort 4 times)",
             notes="Identify load and effort first, then substitute into "
                   "MA = load / effort. Reinforce that MA has no unit and that "
                   "MA = 4 means the effort is multiplied four times.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Work & Machines", 4)
    b.quiz_q(1, "Work", "Work is said to be done only when:",
             ["A force is applied", "A body moves in the direction of the "
              "force", "A body is at rest", "Energy is stored"])
    b.quiz_a(1, "B. A body moves in the direction of the force",
             "Work needs both a force and movement in the direction of that "
             "force. Pushing a wall that does not move means no work is done, "
             "however hard you push.")
    b.quiz_q(2, "Units", "The SI unit of work and energy is the:",
             ["Newton", "Joule", "Watt", "Metre"])
    b.quiz_a(2, "B. Joule",
             "Work and energy are both measured in joules (J). One joule is "
             "the work done when a force of one newton moves a body one metre.")
    b.quiz_q(3, "Mechanical Advantage", "Mechanical advantage is the ratio:",
             ["Effort / Load", "Load / Effort", "Work out / Work in",
              "Speed / Force"])
    b.quiz_a(3, "B. Load / Effort",
             "MA = Load / Effort. It tells us how many times a machine "
             "multiplies our effort. Because it is force ÷ force, MA has no "
             "unit.")
    b.quiz_q(4, "Efficiency", "The efficiency of a real machine is always:",
             ["Equal to 100%", "More than 100%", "Less than 100%",
              "Exactly zero"])
    b.quiz_a(4, "C. Less than 100%",
             "Some input work is always wasted against friction and in moving "
             "the machine's own parts, so a real machine can never be 100% "
             "efficient.")

    # ---- Part 2 : Levers ----
    b.divider(2, "Part 2", "Levers",
              "The simplest machine, and its three orders")
    b.text_image("LEVER", "What Is a Lever?",
                 ["A lever is a rigid bar that can turn freely about a fixed "
                  "point.",
                  "The fixed point about which it turns is called the fulcrum.",
                  "The load is the resistance to be overcome; the effort is the "
                  "force we apply.",
                  "A lever is the simplest of all machines."],
                 principle, img_side="right", panel_title="Three points",
                 caption="Every lever has a fulcrum, a load and an effort",
                 notes="Introduce the lever and its three points — fulcrum, "
                       "load, effort. Point each one out on the diagram. These "
                       "labels decide the lever's class later.")
    b.statement("PRINCIPLE OF A LEVER", "The Principle of a Lever",
                "When a lever is balanced, the turning effect of the load "
                "equals the turning effect of the effort.",
                formula="Load × load-arm  =  Effort × effort-arm",
                points=["The load-arm is the distance from the fulcrum to the "
                        "load.",
                        "The effort-arm is the distance from the fulcrum to the "
                        "effort.",
                        "A longer effort-arm lets a smaller effort balance a "
                        "bigger load.",
                        "For a lever, MA = effort-arm / load-arm."],
                notes="State the principle (the law of moments in words). The "
                      "practical message: the longer the effort arm, the less "
                      "effort needed — this is why a long crowbar is so "
                      "helpful.")
    b.text_image("CLASS 1", "First-Order Levers",
                 ["The fulcrum lies between the load and the effort.",
                  "Pressing down on the effort side lifts the load on the other "
                  "side.",
                  "The mechanical advantage can be more than, equal to, or less "
                  "than 1.",
                  "Examples: a seesaw, a pair of scissors, pliers and a "
                  "crowbar."],
                 lever1, img_side="left", img_w=5.6, img_h=4.0,
                 panel_title="F between L and E",
                 caption="Class 1: fulcrum in the middle",
                 notes="Class 1: fulcrum in the middle. Have students mime a "
                       "seesaw. Note the MA can be anything depending on where "
                       "the fulcrum sits.")
    b.text_image("CLASS 2", "Second-Order Levers",
                 ["The load lies between the fulcrum and the effort.",
                  "The effort-arm is always longer than the load-arm.",
                  "So the mechanical advantage is always more than 1 — a force "
                  "multiplier.",
                  "Examples: a wheelbarrow, a nutcracker and a bottle opener."],
                 lever2, img_side="right", img_w=5.6, img_h=4.0,
                 panel_title="L between F and E",
                 caption="Class 2: load in the middle",
                 notes="Class 2: load in the middle. Because the effort arm is "
                       "always longer, these always multiply force (MA > 1). A "
                       "wheelbarrow is the classic example.")
    b.text_image("CLASS 3", "Third-Order Levers",
                 ["The effort lies between the fulcrum and the load.",
                  "The effort-arm is always shorter than the load-arm.",
                  "So the mechanical advantage is always less than 1 — we gain "
                  "speed, not force.",
                  "Examples: the human forearm, sugar tongs and a fishing "
                  "rod."],
                 lever3, img_side="left", img_w=5.6, img_h=4.0,
                 panel_title="E between F and L",
                 caption="Class 3: effort in the middle",
                 notes="Class 3: effort in the middle. Here effort is greater "
                       "than load (MA < 1) but we gain speed and a wider range "
                       "of movement — like the forearm flicking the hand.")
    b.cards("EXAMPLES", "Spotting the Class of a Lever", [
        ("Class 1", "Seesaw, scissors, pliers, beam balance, a crowbar — "
         "fulcrum in the middle."),
        ("Class 2", "Wheelbarrow, nutcracker, bottle opener, lemon squeezer — "
         "load in the middle."),
        ("Class 3", "Forearm, sugar tongs, fishing rod, a broom — effort in "
         "the middle."),
        ("How to decide", "Find the fulcrum, the load and the effort, then see "
         "which one is in the middle."),
    ], notes="Give a quick method: locate F, L and E, then ask which is in the "
             "middle — that names the class. Practise with a few tools held up "
             "in class.")
    b.worked("WORKED EXAMPLE", "Balancing a Lever",
             "On a seesaw, a load of 300 N sits 1 m from the fulcrum. How much "
             "effort is needed 3 m from the fulcrum to balance it?",
             ["Principle: Load × load-arm = Effort × effort-arm",
              "300 × 1 = Effort × 3",
              "300 = Effort × 3",
              "Effort = 300 / 3 = 100 N"],
             "Effort = 100 N  (a longer effort-arm needs less effort)",
             notes="Apply the lever principle. The lesson: tripling the effort "
                   "arm cuts the effort to a third. This is why we sit far from "
                   "the pivot on a seesaw.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Work", "done only when a force moves a body; unit is the joule"),
        ("Machine", "makes work easier — small effort moves a large load"),
        ("Functions", "multiply force or speed, change direction or point"),
        ("MA", "Load / Effort, no unit; efficiency is always below 100%"),
        ("Lever", "rigid bar turning about a fulcrum; load × load-arm = "
         "effort × effort-arm"),
        ("Three classes", "by what lies in the middle: fulcrum, load or "
         "effort"),
    ], notes="Rapid recap. Cold-call students to give each point, especially "
             "the lever principle and how the three classes differ.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Machines & Levers", 4)
    b.quiz_q(1, "Levers", "In a first-order lever, what lies between the load "
             "and the effort?", ["The load", "The effort", "The fulcrum",
                                 "Nothing"])
    b.quiz_a(1, "C. The fulcrum",
             "A first-order (class 1) lever has the fulcrum in the middle, "
             "between the load and the effort — like a seesaw or a pair of "
             "scissors.")
    b.quiz_q(2, "Class 2", "Which of these is a second-order lever?",
             ["A seesaw", "A wheelbarrow", "Sugar tongs", "A fishing rod"])
    b.quiz_a(2, "B. A wheelbarrow",
             "In a wheelbarrow the load sits between the fulcrum (the wheel) "
             "and the effort (your hands), so it is a class 2 lever and always "
             "has MA greater than 1.")
    b.quiz_q(3, "Lever principle", "A load of 100 N is 2 m from the fulcrum. "
             "What effort balances it 4 m from the fulcrum?",
             ["25 N", "50 N", "200 N", "400 N"])
    b.quiz_a(3, "B. 50 N",
             "Load × load-arm = Effort × effort-arm → 100 × 2 = Effort × 4, so "
             "Effort = 200 / 4 = 50 N. The longer effort-arm needs less "
             "effort.")
    b.quiz_q(4, "Class 3", "Why do third-order levers have a mechanical "
             "advantage less than 1?", ["The fulcrum is in the middle",
             "The effort-arm is shorter than the load-arm",
             "They have no fulcrum", "The load is always zero"])
    b.quiz_a(4, "B. The effort-arm is shorter than the load-arm",
             "With the effort in the middle, its arm is always shorter than "
             "the load-arm, so effort must be greater than load (MA < 1). In "
             "return we gain speed and range of movement.")

    b.closing("Work Made Easy",
              "A machine never gives us something for nothing — it just lets a "
              "small effort do a big job in a smarter way.")
    return b


def sm_deck2():
    """S31 — Simple Machines 2: pulley, wheel & axle, inclined plane, wedge,
    screw, and care of machines."""
    b = Builder("", accent=C["teal"], brand="")
    p_fixed = DX.pulley("g6sm2_pulley_fixed", fixed=True)
    p_move = DX.pulley("g6sm2_pulley_move", fixed=False)
    block = DX.block_and_tackle("g6sm2_block")
    incline = DX.inclined_plane("g6sm2_incline")
    wheelaxle = DX.wheel_and_axle("g6sm2_wheelaxle")
    wedge = DX.wedge("g6sm2_wedge")
    screw = DX.screw("g6sm2_screw")

    b.title("Mechanics", "Simple Machines — 2",
            "Pulleys  •  Wheel and axle  •  Inclined plane  •  Wedge  •  "
            "Screw  •  Caring for machines", img=p_fixed)
    b.objectives([
        "Describe a single fixed and a single movable pulley",
        "State the mechanical advantage of each kind of pulley",
        "Explain how a wheel and axle multiplies effort",
        "Use MA = length / height for an inclined plane",
        "Recognise the wedge and the screw as simple machines",
        "List sensible ways to take care of machines",
    ])

    # ---- Part 1 : Pulleys and the wheel & axle ----
    b.divider(1, "Part 1", "Pulleys & the Wheel and Axle",
              "Lifting loads with ropes and wheels")
    b.text_image("PULLEY", "What Is a Pulley?",
                 ["A pulley is a wheel with a grooved rim over which a rope or "
                  "string passes.",
                  "Pulling one end of the rope raises a load tied to the other "
                  "end.",
                  "A pulley fixed to a support is a fixed pulley.",
                  "A pulley whose axle is free to move up and down is a movable "
                  "pulley."],
                 p_fixed, img_side="left", panel_title="A grooved wheel",
                 caption="A single fixed pulley",
                 notes="Introduce the pulley as a grooved wheel and a rope. "
                       "Distinguish fixed (stays put) from movable (rises with "
                       "the load) — this difference decides the MA.")
    b.cards("FIXED PULLEY", "The Single Fixed Pulley", [
        ("How it works", "The wheel is fixed to a beam; you pull down on one "
         "side and the load rises on the other."),
        ("Mechanical advantage", "Its ideal MA is 1 — the effort equals the "
         "load, so it does not reduce the force."),
        ("Why use it then?", "It changes the direction of the force, letting "
         "you pull downward, which is far more convenient."),
        ("Everyday use", "Drawing water from a well and hoisting a flag up a "
         "pole."),
    ], notes="The fixed pulley's whole value is convenience — pulling down is "
             "easier than lifting up, even though MA = 1. Use the well and the "
             "flagpole as examples.")
    b.text_image("MOVABLE PULLEY", "The Single Movable Pulley",
                 ["Here the pulley itself moves up with the load.",
                  "The load is shared by two strands of rope, so the effort is "
                  "only half the load.",
                  "Its ideal mechanical advantage is therefore 2.",
                  "It does not change the direction of the force — you pull "
                  "upward."],
                 p_move, img_side="right", panel_title="MA = 2",
                 caption="A single movable pulley halves the effort",
                 notes="The movable pulley actually reduces effort (MA = 2) "
                       "because two rope strands share the load. Its drawback "
                       "is you must pull upward. This motivates combining "
                       "pulleys.")
    b.text_image("BLOCK & TACKLE", "Combining Pulleys",
                 ["We can combine fixed and movable pulleys into a block and "
                  "tackle.",
                  "The more rope strands that support the load, the greater the "
                  "mechanical advantage.",
                  "A fixed pulley in the set also lets us pull downward "
                  "comfortably.",
                  "Cranes and lifts use such pulley systems to raise very heavy "
                  "loads."],
                 block, img_side="left", img_w=4.6, img_h=4.2,
                 panel_title="Many strands, big MA",
                 caption="Two strands support the load → MA = 2",
                 notes="Explain that combining pulleys multiplies the MA — it "
                       "equals the number of strands supporting the load. This "
                       "is how cranes lift tonnes with a manageable effort.")
    b.statement("WHEEL & AXLE", "The Wheel and Axle",
                "A large wheel is fixed to a smaller axle so that both turn "
                "together; the effort turns the wheel and the load is raised "
                "by the axle.",
                formula="MA  =  radius of wheel (R)  /  radius of axle (r)",
                points=["Because the wheel's radius R is larger than the "
                        "axle's radius r, the MA is greater than 1.",
                        "A small effort on the big wheel raises a large load on "
                        "the small axle.",
                        "Examples: a steering wheel, a screwdriver, a door "
                        "handle and a windlass.",
                        "The bigger the wheel compared with the axle, the "
                        "greater the mechanical advantage."],
                img=wheelaxle,
                notes="Stress that the wheel and axle are rigidly joined and "
                      "turn together. The larger the ratio R/r, the greater the "
                      "force multiplication. Point out everyday examples they "
                      "use daily.")
    b.worked("WORKED EXAMPLE", "Mechanical Advantage of a Wheel & Axle",
             "A wheel of radius 50 cm is fixed to an axle of radius 10 cm. "
             "Find the mechanical advantage.",
             ["MA = radius of wheel / radius of axle = R / r",
              "R = 50 cm,  r = 10 cm",
              "MA = 50 / 10",
              "MA = 5"],
             "MA = 5  (a small effort on the wheel raises 5 times the load)",
             notes="Substitute the two radii into MA = R/r. Reinforce that a "
                   "bigger wheel compared with the axle gives a larger "
                   "mechanical advantage.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Pulleys & Wheels", 4)
    b.quiz_q(1, "Fixed pulley", "The main use of a single fixed pulley is to:",
             ["Halve the effort", "Change the direction of the force",
              "Double the load", "Increase the speed"])
    b.quiz_a(1, "B. Change the direction of the force",
             "A single fixed pulley has MA = 1, so it does not reduce effort. "
             "Its value is that it lets us pull downward to raise a load "
             "upward — much more convenient.")
    b.quiz_q(2, "Movable pulley", "The ideal mechanical advantage of a single "
             "movable pulley is:", ["1", "2", "3", "0.5"])
    b.quiz_a(2, "B. 2",
             "Two strands of rope share the load in a single movable pulley, "
             "so the effort is half the load and the ideal MA is 2.")
    b.quiz_q(3, "Wheel & axle", "In a wheel and axle, the mechanical advantage "
             "is given by:", ["r / R", "R / r", "R × r", "R + r"])
    b.quiz_a(3, "B. R / r",
             "MA = radius of wheel ÷ radius of axle = R / r. As the wheel is "
             "larger than the axle, R/r is greater than 1, so it multiplies "
             "the effort.")
    b.quiz_q(4, "Identify", "A steering wheel is an example of which simple "
             "machine?", ["A lever", "A pulley", "A wheel and axle",
                          "A wedge"])
    b.quiz_a(4, "C. A wheel and axle",
             "Turning the large steering wheel turns the smaller steering "
             "column (axle), so it is a wheel-and-axle machine.")

    # ---- Part 2 : The inclined plane, wedge and screw ----
    b.divider(2, "Part 2", "Inclined Plane, Wedge & Screw",
              "Sloping surfaces that make lifting easier")
    b.statement("INCLINED PLANE", "The Inclined Plane",
                "An inclined plane is a sloping surface used to raise a heavy "
                "load with less effort than lifting it straight up.",
                formula="MA  =  length of slope (l)  /  height (h)",
                points=["The load is pushed or rolled up the slope instead of "
                        "lifted vertically.",
                        "A longer, gentler slope gives a greater mechanical "
                        "advantage.",
                        "You travel a longer distance, but you need a smaller "
                        "effort.",
                        "Examples: a ramp for loading trucks, a staircase and "
                        "winding hill roads."],
                img=incline,
                notes="The trade-off is the key idea: a ramp needs less effort "
                      "but you move through a greater distance. A gentler (and "
                      "so longer) slope means a bigger MA.")
    b.worked("WORKED EXAMPLE", "Mechanical Advantage of a Ramp",
             "A ramp is 8 m long and lifts a load to a height of 2 m. Find its "
             "ideal mechanical advantage.",
             ["MA = length of slope / height = l / h",
              "l = 8 m,  h = 2 m",
              "MA = 8 / 2",
              "MA = 4"],
             "MA = 4  (the effort is one-fourth of lifting straight up)",
             notes="Apply MA = l/h. Remind students the load travels the full "
                   "8 m along the slope, so we trade a longer distance for a "
                   "smaller effort.")
    b.text_image("WEDGE", "The Wedge",
                 ["A wedge is two inclined planes joined back to back to give a "
                  "sharp edge.",
                  "A downward effort on the wedge produces a large sideways "
                  "force that splits or cuts.",
                  "It is used to separate, cut or fasten objects.",
                  "Examples: an axe, a knife, a chisel, a nail and a needle."],
                 wedge, img_side="left", img_w=5.2, img_h=4.0,
                 panel_title="Two inclined planes",
                 caption="A wedge turns a small push into a big splitting force",
                 notes="A wedge is a moving inclined plane (two of them). The "
                       "small downward effort becomes a large sideways force — "
                       "that is how an axe splits wood and a knife cuts.")
    b.text_image("SCREW", "The Screw",
                 ["A screw is an inclined plane wrapped around a cylinder.",
                  "The ridges going round the screw are called the threads.",
                  "Turning the screw makes it move forward into the material — "
                  "rotation becomes straight-line motion.",
                  "Examples: a screw, a bolt and nut, a screw jack and a "
                  "vice."],
                 screw, img_side="right", img_w=5.0, img_h=4.0,
                 panel_title="A wrapped-up ramp",
                 caption="A screw is an inclined plane around a cylinder",
                 notes="Show that the thread is just a ramp wrapped round a "
                       "rod. Each full turn drives the screw forward by the "
                       "thread spacing, giving a large mechanical advantage in "
                       "a screw jack.")
    b.cards("CARE OF MACHINES", "Taking Care of Machines", [
        ("Reduce friction", "Oil and grease the moving parts so they rub less "
         "and the machine works more efficiently."),
        ("Keep them clean", "Dust and dirt increase friction and wear, so keep "
         "machines clean and dry."),
        ("Prevent rust", "Wipe metal parts and keep them dry, or paint them, "
         "to stop rusting."),
        ("Use and store well", "Sharpen cutting edges, handle parts gently and "
         "replace worn-out parts in time."),
    ], notes="Tie care back to efficiency: less friction and rust means more "
             "of our effort does useful work and the machine lasts longer.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Fixed pulley", "MA = 1; only changes the direction of the force"),
        ("Movable pulley", "MA = 2; effort is half the load"),
        ("Wheel & axle", "MA = R / r; a big wheel turns a small axle"),
        ("Inclined plane", "MA = l / h; less effort over a longer distance"),
        ("Wedge & screw", "moving and wrapped inclined planes that cut and "
         "fasten"),
        ("Care", "oil, clean and protect machines to keep them efficient"),
    ], notes="Rapid recap of each machine and its MA. Cold-call students to "
             "match a real tool to its machine type.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Slopes, Wedges & Screws", 4)
    b.quiz_q(1, "Inclined plane", "Using a ramp instead of lifting straight "
             "up means you apply:", ["More effort over a shorter distance",
             "Less effort over a longer distance", "The same effort",
             "No effort at all"])
    b.quiz_a(1, "B. Less effort over a longer distance",
             "An inclined plane trades distance for force: you push a smaller "
             "effort but move the load through a greater distance along the "
             "slope.")
    b.quiz_q(2, "Inclined plane MA", "A ramp is 6 m long and 2 m high. Its "
             "ideal mechanical advantage is:", ["2", "3", "8", "12"])
    b.quiz_a(2, "B. 3",
             "MA = length / height = 6 / 2 = 3. A longer, gentler slope would "
             "give an even greater mechanical advantage.")
    b.quiz_q(3, "Wedge", "A wedge is best described as:",
             ["A wheel and a rope", "Two inclined planes joined together",
              "A bar turning about a fulcrum", "A grooved wheel"])
    b.quiz_a(3, "B. Two inclined planes joined together",
             "A wedge is two inclined planes back to back forming a sharp "
             "edge. A small downward effort gives a large sideways force, as in "
             "an axe or a knife.")
    b.quiz_q(4, "Screw", "A screw is really which simple machine in disguise?",
             ["A lever", "A pulley", "An inclined plane wrapped around a "
              "cylinder", "A wheel and axle"])
    b.quiz_a(4, "C. An inclined plane wrapped around a cylinder",
             "The thread of a screw is an inclined plane coiled around a rod. "
             "Each turn drives the screw forward, giving a large mechanical "
             "advantage.")

    b.closing("Simple Machines, Smarter Work",
              "Levers, pulleys, ramps, wedges and screws all do one thing — "
              "they let a small effort handle a big job.")
    return b


# ===========================================================================
# LIGHT
# ===========================================================================
def light_deck1():
    """S52 — Light 1: light, sources, luminous/non-luminous, transparent/
    translucent/opaque, rays & beams, rectilinear propagation."""
    b = Builder("", accent=C["teal"], brand="")
    recti = DX.rectilinear_propagation("g6l1_recti")
    pinhole = DX.pinhole_camera("g6l1_pinhole")
    shadow = DX.shadow_formation("g6l1_shadow")
    sunbeams = b.asset("g6_sunbeams_photo", recti)

    b.title("Optics", "Light — 1",
            "What light is  •  Sources of light  •  Luminous & non-luminous  •  "
            "How light travels", img=sunbeams)
    b.objectives([
        "Explain that light is a form of energy that lets us see",
        "Name natural and artificial sources of light",
        "Tell luminous bodies apart from non-luminous bodies",
        "Classify objects as transparent, translucent or opaque",
        "Use the terms ray, beam and medium correctly",
        "State that light travels in straight lines and give proofs",
    ])

    # ---- Part 1 : What light is ----
    b.divider(1, "Part 1", "What Light Is",
              "A form of energy, and where it comes from")
    b.statement("LIGHT", "What Is Light?",
                "Light is a form of energy that produces in us the sensation "
                "of sight — it lets us see things.",
                points=["We see an object only when light from it enters our "
                        "eyes.",
                        "Some objects give out their own light; most objects "
                        "are seen by the light they reflect.",
                        "Light travels extremely fast — about 3 × 10⁸ metres "
                        "per second.",
                        "In a dark room with no light, we cannot see anything "
                        "at all."],
                notes="Open by asking why we cannot see in the dark. Establish "
                      "that seeing needs light entering the eye, and that light "
                      "is a form of energy. Keep the speed as an awe-fact.")
    b.cards("SOURCES", "Sources of Light", [
        ("Natural sources", "Light that comes from nature — the Sun, the "
         "stars, lightning, fireflies and glowing deep-sea creatures."),
        ("Artificial sources", "Light made by humans — an electric bulb, a "
         "tube light, a candle, a torch and a kerosene lamp."),
        ("The Sun", "Our most important natural source; almost all light on "
         "Earth comes first from the Sun."),
        ("Hot vs cool light", "Some sources glow because they are very hot "
         "(bulb, flame); others glow without much heat (a firefly)."),
    ], notes="Sort sources into natural and artificial. Stress the Sun's "
             "importance. Mention that not all light needs great heat — the "
             "firefly is a 'cool' light.")
    b.cards("LUMINOUS OR NOT", "Luminous and Non-luminous Bodies", [
        ("Luminous bodies", "Give out their own light — the Sun, stars, a "
         "lit bulb, a burning candle and red-hot iron."),
        ("Non-luminous bodies", "Do not make their own light — a book, a "
         "table, a wall, and most things around us."),
        ("How we see them", "We see non-luminous bodies only by the light "
         "they reflect from a luminous source into our eyes."),
        ("The Moon", "The Moon is non-luminous; it shines only by reflecting "
         "sunlight — it makes no light of its own."),
    ], notes="Define luminous (own light) vs non-luminous (seen by reflected "
             "light). The Moon is the classic trick example — it looks bright "
             "but only reflects the Sun's light.")
    b.cards("LET LIGHT THROUGH?", "Transparent, Translucent & Opaque", [
        ("Transparent", "Let almost all light pass through, so we can see "
         "clearly through them — clear glass, water and air."),
        ("Translucent", "Let only some light pass, and scatter it, so we see "
         "blurred shapes — frosted glass, butter paper, oiled paper."),
        ("Opaque", "Let no light pass through at all — wood, stone, metal and "
         "cardboard. These cast clear shadows."),
        ("Why it matters", "How much light passes decides whether we can see "
         "through an object and whether it makes a sharp shadow."),
    ], notes="Three-way sort by how much light passes. Hold up examples: a "
             "clear bottle (transparent), tracing paper (translucent), a book "
             "(opaque). Link opaque objects to shadows for later.")
    b.bullets("HOW WE SEE", "How We See Things", [
        ("Light leaves a source", "Light starts at a luminous source such as "
         "the Sun or a lamp."),
        ("It falls on the object", "The light travels out and lands on the "
         "object we are looking at."),
        ("It reflects to our eyes", "The object reflects some light, which "
         "travels in a straight line into our eyes."),
        ("The eye senses it", "Our eyes receive the light and the brain lets "
         "us 'see' the object."),
        ("No light, no sight", "In total darkness no light reaches our eyes, "
         "so we cannot see anything."),
    ], panel_title="Source → object → eye",
       notes="Walk the chain source → object → eye. This explains why we see "
             "non-luminous things by reflected light, and why a dark room "
             "leaves us blind even though the objects are still there.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Light & Its Sources", 4)
    b.quiz_q(1, "Light", "Light is best described as:",
             ["A kind of matter", "A form of energy that lets us see",
              "A type of force", "A liquid"])
    b.quiz_a(1, "B. A form of energy that lets us see",
             "Light is a form of energy. We see an object only when light from "
             "it enters our eyes; in complete darkness we cannot see anything.")
    b.quiz_q(2, "Luminous", "Which of these is a luminous body?",
             ["The Moon", "A mirror", "The Sun", "A white wall"])
    b.quiz_a(2, "C. The Sun",
             "The Sun gives out its own light, so it is luminous. The Moon, a "
             "mirror and a wall are non-luminous — they are seen only by "
             "reflected light.")
    b.quiz_q(3, "Materials", "An object you can see through clearly is said to "
             "be:", ["Opaque", "Translucent", "Transparent", "Luminous"])
    b.quiz_a(3, "C. Transparent",
             "Transparent materials such as clear glass and water let almost "
             "all light pass through, so we can see clearly through them.")
    b.quiz_q(4, "Materials", "Frosted (ground) glass is an example of a "
             "material that is:", ["Transparent", "Translucent", "Opaque",
                                   "Luminous"])
    b.quiz_a(4, "B. Translucent",
             "Frosted glass lets only part of the light through and scatters "
             "it, so we see only blurred shapes — that makes it translucent.")

    # ---- Part 2 : How light travels ----
    b.divider(2, "Part 2", "How Light Travels",
              "Rays, beams and straight-line travel")
    b.bullets("KEY TERMS", "Rays, Beams and Medium", [
        ("Ray of light", "The straight-line path along which light travels, "
         "shown by a line with an arrow."),
        ("Beam of light", "A bunch of light rays travelling together."),
        ("Parallel beam", "Rays that travel side by side, like the beam from "
         "a torch far away or the Sun's rays."),
        ("Convergent / divergent", "A convergent beam comes together to a "
         "point; a divergent beam spreads out from a point."),
        ("Medium", "The substance through which light travels, such as air, "
         "water or glass."),
    ], panel_title="The language of light",
       notes="Define ray, beam and medium. Draw a ray with an arrow on the "
             "board, then show parallel, convergent and divergent beams with "
             "your fingers. These words recur in every light chapter.")
    b.cards("BEAMS", "Three Kinds of Beam", [
        ("Parallel beam", "Rays travel side by side and never meet — like the "
         "Sun's rays reaching the Earth or a searchlight."),
        ("Convergent beam", "Rays come together to a single point — like light "
         "passing through a magnifying glass."),
        ("Divergent beam", "Rays spread out from a point — like light "
         "spreading from a small bulb or a candle flame."),
        ("Why it matters", "Lenses and mirrors work by turning one kind of "
         "beam into another."),
    ], notes="Give a clear everyday example of each beam type. Foreshadow that "
             "lenses and mirrors (later grades) change one beam into another.")
    b.text_image("STRAIGHT LINES", "Light Travels in a Straight Line",
                 ["In a single clear medium, light always travels in straight "
                  "lines.",
                  "This is called the rectilinear propagation of light.",
                  "You can check it: light from a lamp is seen through three "
                  "holes only when the holes are in one straight line.",
                  "Move one card sideways and the light is blocked — proof "
                  "that light does not bend around corners."],
                 recti, img_side="left", img_w=5.6, img_h=4.0,
                 panel_title="Rectilinear propagation",
                 caption="The lamp is seen only when the holes line up",
                 notes="Describe the classic three-cardboard experiment. The "
                       "key conclusion: light goes straight, so it is blocked "
                       "the moment the holes no longer line up.")
    b.cards("PROOFS", "Everyday Proofs of Straight-Line Travel", [
        ("Shadows", "An opaque object blocks light and casts a shadow with "
         "the same outline — light cannot bend around it."),
        ("Pinhole images", "A pinhole camera forms an image because rays "
         "travel straight through the hole."),
        ("Eclipses", "Solar and lunar eclipses happen because light from the "
         "Sun travels straight and is blocked."),
        ("Sunbeams", "Straight shafts of sunlight through clouds or trees "
         "show the rays travelling in straight lines."),
    ], notes="List the four everyday proofs; we study shadows, pinhole "
             "cameras and eclipses in detail next lesson. Sunbeams through "
             "trees are the most visible everyday proof.")
    b.text_image("AROUND US", "Seeing Straight-Line Light",
                 ["Shafts of sunlight breaking through clouds or trees are "
                  "straight, never curved.",
                  "A laser pointer makes a perfectly straight bright line.",
                  "Car headlights and a torch send out straight beams.",
                  "Because light goes straight, we cannot see around corners."],
                 sunbeams, img_side="right", img_w=5.4, img_h=3.8,
                 panel_title="Light around us",
                 caption="Sunbeams travel in straight lines",
                 notes="Connect the physics to things students have seen — "
                       "sunbeams, lasers, headlights. End on the everyday "
                       "consequence: we cannot see around a corner.")
    b.statement("FAST!", "The Speed of Light",
                "Light is the fastest thing in the universe — nothing travels "
                "faster than light.",
                formula="Speed of light  ≈  3 × 10⁸ metres per second",
                points=["At this speed light could go around the Earth about "
                        "seven times in one second.",
                        "Sunlight takes about 8 minutes to reach the Earth.",
                        "Light travels fastest in vacuum (empty space) and a "
                        "little slower in air, water or glass."],
                notes="Give a sense of scale: seven times round the Earth in a "
                      "second, 8 minutes from the Sun. Note light slows a "
                      "little in glass or water — a hook for later grades.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Light", "a form of energy that lets us see; travels very fast"),
        ("Sources", "natural (Sun, stars) and artificial (bulb, candle)"),
        ("Luminous / non-luminous", "make own light vs seen by reflected "
         "light"),
        ("Materials", "transparent, translucent or opaque"),
        ("Ray & beam", "straight path of light; a bundle of rays"),
        ("Rectilinear", "light travels in straight lines — shadows, pinhole, "
         "eclipses"),
    ], notes="Rapid recap. Cold-call students for each, especially luminous "
             "vs non-luminous and the meaning of rectilinear propagation.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — How Light Travels", 4)
    b.quiz_q(1, "Propagation", "Light travelling in straight lines is called:",
             ["Reflection", "Rectilinear propagation", "Refraction",
              "Dispersion"])
    b.quiz_a(1, "B. Rectilinear propagation",
             "The straight-line travel of light is called rectilinear "
             "propagation. It is shown by shadows, pinhole images and "
             "eclipses.")
    b.quiz_q(2, "Beams", "A beam of light in which the rays come together to a "
             "point is a:", ["Parallel beam", "Divergent beam",
                             "Convergent beam", "Reflected beam"])
    b.quiz_a(2, "C. Convergent beam",
             "In a convergent beam the rays come together to a point. A "
             "divergent beam spreads out, and a parallel beam stays side by "
             "side.")
    b.quiz_q(3, "Reasoning", "We cannot see around corners because light:",
             ["Travels in straight lines", "Travels in curves",
              "Is too slow", "Is a form of matter"])
    b.quiz_a(3, "A. Travels in straight lines",
             "Since light travels in straight lines and cannot bend around an "
             "obstacle, we cannot see objects hidden around a corner.")
    b.quiz_q(4, "Speed", "The speed of light is about:",
             ["3 × 10³ m/s", "3 × 10⁵ m/s", "3 × 10⁸ m/s", "3 × 10¹⁰ m/s"])
    b.quiz_a(4, "C. 3 × 10⁸ m/s",
             "Light travels at about 3 × 10⁸ metres per second in vacuum — "
             "the fastest speed in the universe. Sunlight takes about 8 "
             "minutes to reach us.")

    b.closing("Light Travels Straight",
              "Light is energy that lets us see — and it always travels in "
              "straight lines, which is why we get shadows, images and "
              "eclipses.")
    return b


def light_deck2():
    """S53 — Light 2: pinhole camera, shadows, eclipses."""
    b = Builder("", accent=C["teal"], brand="")
    pinhole = DX.pinhole_camera("g6l2_pinhole")
    shadow = DX.shadow_formation("g6l2_shadow")
    solar = DX.solar_eclipse("g6l2_solar")
    lunar = DX.lunar_eclipse("g6l2_lunar")
    eclipse_photo = b.asset("g6_solar_eclipse_photo", solar)
    shadow_photo = b.asset("g6_shadow_photo", shadow)

    b.title("Optics", "Light — 2",
            "The pinhole camera  •  Shadows  •  Solar and lunar eclipses",
            img=eclipse_photo)
    b.objectives([
        "Describe how a pinhole camera forms an image",
        "State the nature of the image in a pinhole camera",
        "List the three things needed to form a shadow",
        "Explain the dark umbra and the lighter penumbra",
        "Explain how a solar eclipse forms",
        "Explain how a lunar eclipse forms",
    ])

    # ---- Part 1 : Pinhole camera & shadows ----
    b.divider(1, "Part 1", "Pinhole Camera & Shadows",
              "Making images and shadows with straight light")
    b.text_image("PINHOLE CAMERA", "How a Pinhole Camera Works",
                 ["It is a closed box with a tiny hole on one side and a "
                  "screen on the opposite side.",
                  "Rays from the top of the object travel straight through the "
                  "hole to the bottom of the screen, and vice versa.",
                  "So the rays cross at the hole and the image is turned upside "
                  "down (inverted).",
                  "The image forms only because light travels in straight "
                  "lines."],
                 pinhole, img_side="left", img_w=5.6, img_h=4.0,
                 panel_title="A box with a tiny hole",
                 caption="Rays cross at the hole, so the image is inverted",
                 notes="Trace one ray from the top and one from the bottom of "
                       "the object. Because they cross at the pinhole, the "
                       "image is inverted — a direct result of straight-line "
                       "travel.")
    b.bullets("THE IMAGE", "Nature of the Pinhole Image", [
        ("Inverted", "The image is always upside down compared with the "
         "object."),
        ("Real", "It can be caught on a screen, so it is a real image."),
        ("Coloured", "The image is in the same colours as the object."),
        ("Size depends on distance", "Moving the screen further from the hole "
         "makes the image larger; moving the object closer also enlarges it."),
        ("Small hole", "A small hole gives a sharp but dim image; a large hole "
         "gives a bright but blurred one."),
    ], panel_title="A real, inverted image",
       notes="List the characteristics. Emphasise real + inverted. Explain the "
             "trade-off of hole size: sharpness versus brightness.")
    b.cards("MAKE & USE", "More About the Pinhole Camera", [
        ("Make your own", "Use a closed box with a tiny hole on one side and "
         "a butter-paper screen on the opposite side."),
        ("Bigger image", "The further the screen is from the hole, the larger "
         "(but dimmer) the image becomes."),
        ("One hole only", "Several holes give several overlapping images, one "
         "from each hole."),
        ("Where it helps", "The pinhole idea led to the modern camera and lets "
         "us view the Sun safely by projection."),
    ], notes="Turn the theory into an activity — students can build one from a "
             "shoebox. The projection use is a safe way to watch a solar "
             "eclipse, linking to Part 2.")
    b.statement("SHADOW", "What Makes a Shadow?",
                "A shadow is the dark patch formed when an opaque object blocks "
                "the path of light.",
                points=["Three things are needed: a source of light, an opaque "
                        "object, and a screen or surface.",
                        "The shadow forms on the side of the object away from "
                        "the light.",
                        "A shadow has the same outline (shape) as the object.",
                        "A shadow is always black, whatever the colour of the "
                        "object, because it is simply the absence of light."],
                notes="Stress the three requirements. The key misconception to "
                      "fix: a shadow takes its shape from the object but its "
                      "colour is always black — it is just missing light.")
    b.text_image("UMBRA & PENUMBRA", "Two Parts of a Shadow",
                 ["From a small (point) source the shadow is sharp and fully "
                  "dark.",
                  "From a large (extended) source the shadow has two parts.",
                  "The umbra is the central, fully dark region where all light "
                  "is blocked.",
                  "The penumbra is the lighter border where only part of the "
                  "light is blocked."],
                 shadow, img_side="right", img_w=5.6, img_h=4.0,
                 panel_title="Umbra and penumbra",
                 caption="A point source gives a sharp, fully dark shadow",
                 notes="Contrast point and extended sources. Define umbra "
                       "(full dark) and penumbra (partial). These same words "
                       "describe the shadows in eclipses, coming up next.")
    b.text_image("SHADOWS AROUND US", "Shadows in Daily Life",
                 ["Your shadow is longest in the early morning and late "
                  "evening, when the Sun is low.",
                  "At noon, with the Sun overhead, your shadow is shortest.",
                  "A shadow shows the shape of the object but none of its "
                  "detail or colour.",
                  "Shadow puppets use opaque hands to make shapes on a screen."],
                 shadow_photo, img_side="left", img_w=5.4, img_h=3.8,
                 panel_title="Long and short shadows",
                 caption="Low evening Sun casts a long shadow",
                 notes="Relate shadow length to the Sun's height through the "
                       "day. A nice activity: shadow puppets show that only the "
                       "outline is reproduced.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Images & Shadows", 4)
    b.quiz_q(1, "Pinhole", "The image formed by a pinhole camera is always:",
             ["Upright and real", "Inverted and real",
              "Upright and virtual", "Inverted and virtual"])
    b.quiz_a(1, "B. Inverted and real",
             "Rays cross at the pinhole, so the image is inverted. It can be "
             "caught on a screen, so it is a real image.")
    b.quiz_q(2, "Shadow", "Which three things are needed to form a shadow?",
             ["Source, mirror, screen", "Source, opaque object, screen",
              "Source, lens, screen", "Source, water, screen"])
    b.quiz_a(2, "B. Source, opaque object, screen",
             "A shadow needs a source of light, an opaque object to block the "
             "light, and a screen or surface for the shadow to fall on.")
    b.quiz_q(3, "Shadow colour", "The colour of a shadow is always:",
             ["The colour of the object", "Black",
              "The colour of the light", "White"])
    b.quiz_a(3, "B. Black",
             "A shadow is simply a region where light is blocked, so it is "
             "always black, whatever the colour of the object.")
    b.quiz_q(4, "Umbra", "The fully dark central part of a shadow is the:",
             ["Penumbra", "Umbra", "Corona", "Image"])
    b.quiz_a(4, "B. Umbra",
             "The umbra is the central region where all the light is blocked. "
             "The lighter border, where only some light is blocked, is the "
             "penumbra.")

    # ---- Part 2 : Eclipses ----
    b.divider(2, "Part 2", "Eclipses",
              "When one body's shadow falls on another")
    b.statement("ECLIPSE", "What Is an Eclipse?",
                "An eclipse happens when one heavenly body moves into the "
                "shadow of another, because light from the Sun travels in "
                "straight lines.",
                points=["The Sun, the Earth and the Moon must line up almost "
                        "in a straight line.",
                        "A shadow is cast because the blocking body is opaque.",
                        "There are two kinds: the solar eclipse and the lunar "
                        "eclipse.",
                        "Eclipses are direct, dramatic proof that light travels "
                        "in straight lines."],
                notes="Set up eclipses as large-scale shadows. The essential "
                      "condition is the near-straight-line alignment of Sun, "
                      "Earth and Moon.")
    b.text_image("SOLAR ECLIPSE", "The Solar Eclipse",
                 ["A solar eclipse happens when the Moon comes between the Sun "
                  "and the Earth.",
                  "The Moon's shadow then falls on a small part of the Earth.",
                  "People standing in the dark umbra see a total solar "
                  "eclipse; the Sun is hidden.",
                  "It can only happen on a new-moon day, and the day briefly "
                  "goes dark."],
                 solar, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="Moon between Sun and Earth",
                 caption="The Moon's shadow falls on the Earth",
                 notes="Walk through the line-up: Sun, Moon, Earth. The Moon's "
                       "shadow is small, so only a narrow strip sees totality. "
                       "Warn never to look directly at the Sun.")
    b.text_image("LUNAR ECLIPSE", "The Lunar Eclipse",
                 ["A lunar eclipse happens when the Earth comes between the Sun "
                  "and the Moon.",
                  "The Earth's shadow then falls on the Moon, and the Moon "
                  "darkens.",
                  "It can only happen on a full-moon day.",
                  "Because the Earth's shadow is large, a lunar eclipse lasts "
                  "much longer and is seen from a whole half of the Earth."],
                 lunar, img_side="right", img_w=5.8, img_h=3.6,
                 panel_title="Earth between Sun and Moon",
                 caption="The Earth's shadow falls on the Moon",
                 notes="Contrast with the solar eclipse: now the Earth blocks "
                       "the light. Because Earth is bigger, the lunar eclipse "
                       "lasts longer and is widely visible — and is safe to "
                       "watch.")
    b.cards("SOLAR vs LUNAR", "Comparing the Two Eclipses", [
        ("Who is in the middle", "Solar: the Moon is in the middle. Lunar: "
         "the Earth is in the middle."),
        ("Whose shadow", "Solar: the Moon's shadow on the Earth. Lunar: the "
         "Earth's shadow on the Moon."),
        ("When", "Solar happens on a new-moon day; lunar happens on a "
         "full-moon day."),
        ("How long & safe", "A solar eclipse is brief; a lunar eclipse lasts "
         "longer and is safe to watch with the naked eye."),
    ], notes="Use this side-by-side table to lock in the difference. The most "
             "tested points: who is in the middle and whose shadow falls where.")
    b.cards("FACTS & SAFETY", "Eclipse Facts & Safety", [
        ("Not every month", "The Moon's orbit is slightly tilted, so the three "
         "bodies line up only a few times a year — not at every new or full "
         "moon."),
        ("Solar safety", "Never look at a solar eclipse with bare eyes; use a "
         "proper filter or a pinhole projection."),
        ("Lunar safety", "A lunar eclipse is completely safe to watch directly "
         "with the naked eye."),
        ("Blood moon", "During a total lunar eclipse the Moon can glow "
         "coppery-red — sometimes called a 'blood moon'."),
    ], notes="Clear the common doubt of why eclipses are not monthly (tilted "
             "orbit). Stress solar-viewing safety. The red 'blood moon' is a "
             "memorable hook.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Pinhole camera", "tiny hole; real, inverted image; light goes "
         "straight"),
        ("Shadow", "needs source, opaque object and screen; always black"),
        ("Umbra / penumbra", "fully dark centre and lighter border"),
        ("Solar eclipse", "Moon between Sun and Earth; new-moon day"),
        ("Lunar eclipse", "Earth between Sun and Moon; full-moon day"),
        ("Why", "all because light travels in straight lines"),
    ], notes="Rapid recap; cold-call for each. Finish by tying everything back "
             "to rectilinear propagation.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Eclipses", 4)
    b.quiz_q(1, "Solar eclipse", "A solar eclipse occurs when:",
             ["The Earth is between the Sun and the Moon",
              "The Moon is between the Sun and the Earth",
              "The Sun is between the Earth and the Moon",
              "The Moon is full"])
    b.quiz_a(1, "B. The Moon is between the Sun and the Earth",
             "In a solar eclipse the Moon comes between the Sun and the Earth, "
             "and the Moon's shadow falls on the Earth. It happens on a "
             "new-moon day.")
    b.quiz_q(2, "Lunar eclipse", "A lunar eclipse occurs on a:",
             ["New-moon day", "Full-moon day", "Half-moon day", "Any day"])
    b.quiz_a(2, "B. Full-moon day",
             "A lunar eclipse happens when the Earth comes between the Sun and "
             "the Moon — only possible at full moon, when the Earth's shadow "
             "can fall on the Moon.")
    b.quiz_q(3, "Shadows", "In a lunar eclipse, whose shadow falls on the "
             "Moon?", ["The Moon's own shadow", "The Sun's shadow",
                       "The Earth's shadow", "A cloud's shadow"])
    b.quiz_a(3, "C. The Earth's shadow",
             "During a lunar eclipse the Earth is in the middle, so the "
             "Earth's shadow falls on the Moon and darkens it.")
    b.quiz_q(4, "Duration", "Compared with a solar eclipse, a lunar eclipse:",
             ["Is much shorter", "Lasts longer and is seen from more places",
              "Cannot be seen", "Happens at new moon"])
    b.quiz_a(4, "B. Lasts longer and is seen from more places",
             "The Earth's shadow is large, so a lunar eclipse lasts longer and "
             "is visible from a whole half of the Earth — and it is safe to "
             "watch.")

    b.closing("Shadows in the Sky",
              "Pinhole images, shadows and eclipses are all the same idea — "
              "light travelling in straight lines and being blocked.")
    return b


# ---------------------------------------------------------------------------
# ===========================================================================
# MAGNETISM  (S69, S70)
# ===========================================================================
def mag_deck1():
    """S69 — Magnetism 1: natural/artificial magnets, magnetic materials,
    properties of a magnet, magnetic field, the Earth's magnetism."""
    b = Builder("", accent=C["teal"], brand="")
    field = DX.bar_magnet_field("g6m1_field")
    poles = DX.like_unlike_poles("g6m1_poles")
    earth = DX.earths_magnetism("g6m1_earth")
    magnet_photo = b.asset("g6_bar_magnet_photo", field)

    b.title("Magnetism", "Magnetism — 1",
            "Natural & artificial magnets  •  Magnetic materials  •  "
            "Properties of a magnet  •  The Earth as a magnet", img=magnet_photo)
    b.objectives([
        "Describe how magnets were discovered and name their kinds",
        "Tell magnetic materials apart from non-magnetic ones",
        "List the main properties of a magnet",
        "State the law of magnetic poles and the sure test of magnetism",
        "Explain what a magnetic field is and draw its field lines",
        "Describe the Earth's magnetism and how a compass works",
    ])

    # ---- Part 1 : Magnets and their properties ----
    b.divider(1, "Part 1", "Magnets & Their Properties",
              "What magnets are and how they behave")
    b.statement("MAGNET", "What Is a Magnet?",
                "A magnet is a substance that attracts magnetic materials like "
                "iron and points north–south when hung freely.",
                points=["Magnets were first found as a natural rock called "
                        "lodestone (magnetite) that attracted iron.",
                        "The word 'magnet' comes from Magnesia, the place where "
                        "lodestone was discovered.",
                        "Every magnet has two poles — a north pole and a south "
                        "pole.",
                        "Magnets are used in compasses, fridge doors, "
                        "loudspeakers, motors and many machines."],
                notes="Begin with the story of lodestone — a natural rock that "
                      "pulled iron. Establish the two defining behaviours: it "
                      "attracts iron and it points north–south. These lead into "
                      "the properties later.")
    b.cards("KINDS", "Natural and Artificial Magnets", [
        ("Natural magnets", "Found in nature as lodestone (magnetite). They are "
         "irregular in shape and rather weak."),
        ("Artificial magnets", "Made by people from steel or other materials. "
         "They are stronger and made in useful shapes."),
        ("Common shapes", "Bar magnet, horseshoe (U-shaped) magnet, cylindrical "
         "magnet, magnetic needle and the ring magnet."),
        ("Why artificial?", "We can make them strong, give them any shape and "
         "make them last — so they are far more useful."),
    ], notes="Contrast natural lodestone with artificial magnets. Show or name "
             "the common shapes. Stress why artificial magnets are preferred — "
             "strength and a chosen shape.")
    b.cards("MATERIALS", "Magnetic and Non-magnetic Materials", [
        ("Magnetic materials", "Attracted by a magnet — iron, steel, nickel "
         "and cobalt."),
        ("Non-magnetic materials", "Not attracted — wood, plastic, rubber, "
         "glass, paper, copper and aluminium."),
        ("A simple test", "Bring a magnet close: if the object is pulled "
         "towards it, the material is magnetic."),
        ("In daily life", "Pins and nails (iron) stick to a magnet, but a "
         "wooden pencil or a plastic ruler does not."),
    ], notes="Sort materials into magnetic and non-magnetic. Let students "
             "predict, then test, a few classroom objects. Iron, nickel and "
             "cobalt are the key magnetic metals.")
    b.cards("PROPERTIES", "Properties of a Magnet", [
        ("Attracts iron", "A magnet attracts magnetic materials, and the pull "
         "is strongest at its two poles."),
        ("Points north–south", "A freely suspended magnet always comes to rest "
         "pointing north–south (the directive property)."),
        ("Two poles", "Every magnet has a north and a south pole; break a "
         "magnet and each piece is a new magnet with both poles."),
        ("Poles and forces", "Like poles repel each other and unlike poles "
         "attract each other."),
    ], notes="Run through the four properties. Demonstrate the directive "
             "property with a suspended magnet. The 'break a magnet' idea — you "
             "can never get a single pole — surprises students.")
    b.text_image("LAW OF POLES", "Like Repels, Unlike Attracts",
                 ["Bring two north poles together and they push apart — they "
                  "repel.",
                  "Bring a north pole near a south pole and they pull together "
                  "— they attract.",
                  "Repulsion happens only between two magnets, so repulsion is "
                  "the sure test of magnetism.",
                  "Attraction alone is not a sure test, because a magnet also "
                  "attracts ordinary iron."],
                 poles, img_side="left", img_w=5.6, img_h=3.6,
                 panel_title="The sure test",
                 caption="Like poles repel; unlike poles attract",
                 notes="Drill the law of poles, then the key exam point: only "
                       "repulsion proves an object is a magnet, because both a "
                       "magnet and plain iron will show attraction.")
    b.cards("EVERYDAY MAGNETS", "Magnets in Everyday Life", [
        ("Compass", "A tiny magnet that always points north–south and helps us "
         "find direction."),
        ("Fridge & cupboards", "Small magnets in the door seal hold the door "
         "shut, and fridge magnets stick notes up."),
        ("Sound & motion", "Magnets make loudspeakers, earphones and electric "
         "motors work."),
        ("Sorting & lifting", "Big magnets lift and separate iron and steel in "
         "scrapyards and recycling plants."),
    ], notes="Show how widely magnets are used so the topic feels real. Ask "
             "students to spot magnets at home — the fridge door and "
             "earphones are good starting points.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Magnets & Materials", 4)
    b.quiz_q(1, "Materials", "Which of these is a magnetic material?",
             ["Wood", "Iron", "Plastic", "Glass"])
    b.quiz_a(1, "B. Iron",
             "Iron is attracted by a magnet, so it is a magnetic material. "
             "Wood, plastic and glass are non-magnetic — a magnet does not "
             "attract them.")
    b.quiz_q(2, "Poles", "When the north poles of two magnets are brought "
             "close, they:", ["Attract", "Repel", "Do nothing",
                               "Join together"])
    b.quiz_a(2, "B. Repel",
             "Like poles repel each other. Two north poles are like poles, so "
             "they push apart.")
    b.quiz_q(3, "Sure test", "The sure test of whether an object is a magnet "
             "is:", ["Attraction", "Repulsion", "Its colour", "Its weight"])
    b.quiz_a(3, "B. Repulsion",
             "Only two magnets repel. A magnet also attracts ordinary iron, so "
             "attraction is not a sure test — but repulsion proves the object "
             "is a magnet.")
    b.quiz_q(4, "Poles", "If a bar magnet is broken into two pieces, each "
             "piece will have:", ["Only a north pole", "Only a south pole",
                                  "Both north and south poles", "No poles"])
    b.quiz_a(4, "C. Both north and south poles",
             "You can never get a single pole. Each broken piece becomes a "
             "complete new magnet with its own north and south pole.")

    # ---- Part 2 : Magnetic field and the Earth ----
    b.divider(2, "Part 2", "Magnetic Field & the Earth",
              "The space around a magnet, and our planet's magnetism")
    b.text_image("MAGNETIC FIELD", "The Magnetic Field",
                 ["The magnetic field is the region around a magnet where its "
                  "force can be felt.",
                  "We picture it using magnetic field lines.",
                  "Outside the magnet the field lines run from the north pole "
                  "to the south pole.",
                  "The lines are closest together near the poles, where the "
                  "field is strongest."],
                 field, img_side="right", img_w=5.6, img_h=3.6,
                 panel_title="Field lines",
                 caption="Field lines run from N to S outside the magnet",
                 notes="Define the magnetic field as the region of influence. "
                       "Introduce field lines as a way to picture it. Crowded "
                       "lines near the poles mean a stronger field there.")
    b.bullets("FIELD LINES", "Properties of Magnetic Field Lines", [
        ("Direction", "Outside the magnet they point from the north pole to "
         "the south pole."),
        ("They never cross", "Two field lines never cut across each other."),
        ("Crowding shows strength", "Where the lines are closer together, the "
         "magnetic field is stronger — that is near the poles."),
        ("Closed loops", "Each field line is a closed loop, continuing from S "
         "back to N inside the magnet."),
    ], panel_title="Reading a field pattern",
       notes="List the rules for field lines. The two most tested: lines go N "
             "to S outside, and they never cross. Crowding near the poles = a "
             "stronger field.")
    b.text_image("EARTH", "The Earth Is a Giant Magnet",
                 ["The Earth behaves as if a huge bar magnet lies inside it.",
                  "This is why a freely suspended magnet always points "
                  "north–south.",
                  "The Earth's magnetic south pole lies near the geographic "
                  "north, so a compass needle's north end points north.",
                  "The Earth's magnetism shields us and helps us find "
                  "direction."],
                 earth, img_side="left", img_w=5.0, img_h=4.0,
                 panel_title="Earth's magnetism",
                 caption="A magnetic S-pole lies near the geographic North",
                 notes="Explain that the Earth itself acts like a bar magnet, "
                       "which is why compasses work. Clarify the neat twist: a "
                       "magnetic south pole sits near the geographic north.")
    b.cards("COMPASS", "The Magnetic Compass", [
        ("What it is", "A small magnetised needle, free to turn, that always "
         "settles pointing north–south."),
        ("Why it works", "It lines up with the Earth's magnetic field, just "
         "like any freely suspended magnet."),
        ("Finding direction", "Sailors, pilots and trekkers use it to know "
         "which way is north."),
        ("Keep it away from", "Iron objects and other magnets, which disturb "
         "the needle and give a wrong reading."),
    ], notes="The compass is the everyday use of the directive property. Note "
             "that nearby iron or magnets spoil the reading.")
    b.bullets("PLOTTING THE FIELD", "Mapping a Magnetic Field", [
        ("Use a small compass", "Place a plotting compass near a bar magnet on "
         "paper and mark where its needle points."),
        ("Move and mark", "Move the compass a little, mark again, and join the "
         "marks to trace one field line."),
        ("Build the pattern", "Start from different points to draw the whole "
         "field-line pattern around the magnet."),
        ("Read the strength", "Where your lines come out close together, the "
         "field is strong; where they spread out, it is weak."),
    ], panel_title="Compass-and-paper method",
       notes="Describe the standard practical of plotting field lines with a "
             "small compass. It links the abstract field lines to something "
             "students can actually do and see.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Magnet", "attracts iron and points north–south; first found as "
         "lodestone"),
        ("Materials", "iron, steel, nickel, cobalt are magnetic; most others "
         "are not"),
        ("Properties", "attracts at poles, directive, two inseparable poles"),
        ("Law of poles", "like repel, unlike attract; repulsion is the sure "
         "test"),
        ("Field", "region of force; lines run N to S, never cross"),
        ("Earth", "acts like a giant magnet, so a compass points north"),
    ], notes="Rapid recap. Cold-call for the law of poles and the sure test, "
             "which are the most examined points.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Fields & the Earth", 4)
    b.quiz_q(1, "Field lines", "Outside a magnet, the magnetic field lines run "
             "from:", ["South pole to north pole", "North pole to south pole",
                       "Pole to the middle", "They do not move"])
    b.quiz_a(1, "B. North pole to south pole",
             "By convention, magnetic field lines outside a magnet are drawn "
             "from the north pole to the south pole.")
    b.quiz_q(2, "Field strength", "The magnetic field of a bar magnet is "
             "strongest:", ["At its centre", "At its two poles",
                            "Far away from it", "It is the same everywhere"])
    b.quiz_a(2, "B. At its two poles",
             "The field is strongest at the poles, where the field lines are "
             "most crowded; it is weakest near the middle of the magnet.")
    b.quiz_q(3, "Earth", "A compass needle points north–south because:",
             ["It is blown by the wind", "The Earth acts like a giant magnet",
              "It is made of gold", "It is very light"])
    b.quiz_a(3, "B. The Earth acts like a giant magnet",
             "The Earth behaves like a huge bar magnet, so the compass needle "
             "lines up with the Earth's magnetic field and points north–south.")
    b.quiz_q(4, "Field lines", "Two magnetic field lines can never:",
             ["Be curved", "Cross each other", "Be close together",
              "Point to a pole"])
    b.quiz_a(4, "B. Cross each other",
             "Field lines never cross. If they did, the field would point in "
             "two directions at one place, which is impossible.")

    b.closing("The Pull of Magnets",
              "Magnets attract iron, always seek north and fill the space "
              "around them with an invisible field — even our planet is one.")
    return b


def mag_deck2():
    """S70 — Magnetism 2: making magnets, electromagnets, care & storage,
    demagnetisation."""
    b = Builder("", accent=C["teal"], brand="")
    stroke = DX.making_magnet_stroke("g6m2_stroke")
    emag = DX.electromagnet("g6m2_emag")
    field = DX.bar_magnet_field("g6m2_field")
    emag_photo = b.asset("g6_electromagnet_photo", emag)

    b.title("Magnetism", "Magnetism — 2",
            "Making a magnet  •  Electromagnets  •  Care & storage  •  "
            "Losing magnetism", img=emag_photo)
    b.objectives([
        "Describe ways of making a magnet",
        "Explain the single-touch (stroking) method",
        "Describe an electromagnet and how to make one stronger",
        "Tell temporary magnets apart from permanent magnets",
        "State how magnets should be stored and cared for",
        "List the ways a magnet can lose its magnetism",
    ])

    # ---- Part 1 : Making magnets ----
    b.divider(1, "Part 1", "Making Magnets",
              "Turning steel and iron into magnets")
    b.cards("HOW TO MAGNETISE", "Ways to Make a Magnet", [
        ("Single touch", "Stroke a steel bar again and again in one direction "
         "with one pole of a magnet."),
        ("Double touch", "Stroke the bar from the middle outwards using two "
         "unlike poles together."),
        ("By induction", "Simply bringing a magnet near a piece of iron makes "
         "the iron a temporary magnet."),
        ("By electricity", "Pass an electric current through a coil wound "
         "around the bar — this makes an electromagnet."),
    ], notes="Introduce the four ways to magnetise. Single touch is the one to "
             "know in detail. Induction is temporary; the electrical method is "
             "the strongest and is used in electromagnets.")
    b.text_image("SINGLE TOUCH", "The Single-Touch Method",
                 ["Place the steel bar flat on the table.",
                  "Stroke it from one end to the other with one pole of a "
                  "magnet.",
                  "Lift the magnet high at the end of each stroke and repeat "
                  "many times in the same direction.",
                  "The bar becomes a magnet; the end where the stroking pole "
                  "leaves it gets the opposite polarity."],
                 stroke, img_side="right", img_w=5.6, img_h=3.4,
                 panel_title="Stroke one way",
                 caption="Stroke in one direction, again and again",
                 notes="Demonstrate the stroking action. Two rules: always "
                       "stroke in the SAME direction, and lift the pole well "
                       "clear between strokes. The finishing end takes the "
                       "polarity opposite to the stroking pole.")
    b.text_image("ELECTROMAGNET", "Making an Electromagnet",
                 ["Wind insulated copper wire into a coil around a soft-iron "
                  "core.",
                  "Connect the ends of the coil to a cell through a switch.",
                  "When current flows, the iron core becomes a strong magnet.",
                  "Switch the current off and the magnetism almost completely "
                  "disappears — it is a temporary magnet."],
                 emag, img_side="left", img_w=5.6, img_h=3.4,
                 panel_title="Coil + iron core",
                 caption="Current in the coil magnetises the iron core",
                 notes="Build the electromagnet step by step. The headline "
                       "idea: its magnetism can be switched on and off with the "
                       "current — that is what makes it so useful.")
    b.cards("STRONGER", "Making an Electromagnet Stronger", [
        ("More turns", "Winding more turns of wire on the coil makes the "
         "electromagnet stronger."),
        ("More current", "Increasing the current through the coil increases "
         "its strength."),
        ("A soft-iron core", "A soft-iron core becomes strongly magnetic and "
         "boosts the field."),
        ("Switchable", "Its magnetism can be turned on and off and even "
         "reversed — a permanent magnet cannot do this."),
    ], notes="Three ways to strengthen: more turns, more current, soft-iron "
             "core. End on the big advantage — it can be switched and reversed.")
    b.cards("TEMPORARY vs PERMANENT", "Temporary and Permanent Magnets", [
        ("Temporary magnets", "Made of soft iron; magnetic only while the "
         "current flows. Used in electromagnets."),
        ("Permanent magnets", "Made of steel; keep their magnetism for a long "
         "time. Used in compasses and fridge magnets."),
        ("Soft iron", "Is easy to magnetise and easy to demagnetise."),
        ("Steel", "Is harder to magnetise but holds its magnetism well."),
    ], notes="Contrast soft iron (temporary, for electromagnets) with steel "
             "(permanent). Tie the choice of material to the job the magnet "
             "must do.")
    b.bullets("INDUCTION", "Magnetism by Induction", [
        ("No touching needed", "Simply bringing a magnet near a piece of iron "
         "turns the iron into a temporary magnet."),
        ("Chains of pins", "A nail clinging to a magnet can itself pick up more "
         "nails, which hang in a chain."),
        ("It is temporary", "Take the magnet away and the induced magnetism "
         "almost completely disappears."),
        ("Why attraction works", "A magnet first induces magnetism in the iron, "
         "and that is what lets it then pull the iron in."),
    ], panel_title="A magnet makes more magnets",
       notes="Demonstrate induction with a chain of pins hanging from one "
             "magnet. The key idea: induction comes first, and that is the "
             "real reason a magnet can attract a piece of iron.")

    # ---- Quiz 1 ----
    b.quiz_intro("Quiz 1", "Quick Check — Making Magnets", 4)
    b.quiz_q(1, "Method", "In the single-touch method, the steel bar is "
             "stroked:", ["In both directions", "In one direction only",
                          "Very gently once", "Without a magnet"])
    b.quiz_a(1, "B. In one direction only",
             "In single touch you stroke the bar repeatedly in the same "
             "direction with one pole, lifting the magnet clear between "
             "strokes.")
    b.quiz_q(2, "Electromagnet", "An electromagnet is made by passing current "
             "through a coil wound on a core of:", ["Steel", "Soft iron",
                                                    "Copper", "Plastic"])
    b.quiz_a(2, "B. Soft iron",
             "A soft-iron core becomes strongly magnetic when current flows and "
             "loses it when the current stops, making a good electromagnet.")
    b.quiz_q(3, "Strength", "Which change makes an electromagnet stronger?",
             ["Fewer turns of wire", "Less current",
              "More turns of wire", "A plastic core"])
    b.quiz_a(3, "C. More turns of wire",
             "More turns of wire (and more current, and a soft-iron core) make "
             "an electromagnet stronger.")
    b.quiz_q(4, "Type", "A permanent magnet is usually made of:",
             ["Soft iron", "Steel", "Copper", "Aluminium"])
    b.quiz_a(4, "B. Steel",
             "Steel is hard to magnetise but holds its magnetism for a long "
             "time, so it is used to make permanent magnets.")

    # ---- Part 2 : Using, keeping and losing magnetism ----
    b.divider(2, "Part 2", "Uses, Care & Demagnetisation",
              "Where electromagnets help, and how magnetism is kept or lost")
    b.cards("USES", "Uses of Electromagnets", [
        ("Lifting cranes", "Powerful electromagnets on cranes lift heavy iron "
         "and steel scrap, then drop it by switching off."),
        ("Electric bell", "An electromagnet makes the hammer strike the gong "
         "again and again."),
        ("Machines", "Electromagnets are used in electric motors, "
         "loudspeakers, telephones and many devices."),
        ("Separating metals", "They pull magnetic metals out of mixed waste "
         "for recycling."),
    ], notes="Connect electromagnets to real machines. The crane (switch on to "
             "lift, off to drop) best shows why a switchable magnet is so "
             "useful.")
    b.bullets("CARE", "Caring For and Storing Magnets", [
        ("Store in pairs", "Keep bar magnets in pairs with unlike poles "
         "together."),
        ("Use keepers", "Place soft-iron pieces (keepers) across the ends to "
         "preserve their magnetism."),
        ("Keep them safe", "Do not drop, hammer or heat magnets — this weakens "
         "them."),
        ("Keep apart", "Store magnets away from watches, mobile phones and "
         "other magnets."),
    ], panel_title="Looking after magnets",
       notes="Explain why magnets need care. Keepers give the field a closed "
             "path and stop the magnet weakening. Heat, shock and stray fields "
             "are the enemies.")
    b.statement("DEMAGNETISATION", "How a Magnet Loses Its Magnetism",
                "A magnet can lose its magnetism if it is treated roughly or "
                "heated — this is called demagnetisation.",
                points=["Heating a magnet strongly and then cooling it makes "
                        "it lose its magnetism.",
                        "Hammering or dropping a magnet again and again weakens "
                        "it.",
                        "Placing it in a coil carrying alternating current (AC) "
                        "removes its magnetism.",
                        "Careless storage near other magnets also makes a "
                        "magnet weaker over time."],
                notes="List the three deliberate ways to demagnetise — heating, "
                      "rough handling, and an AC coil — and tie them back to "
                      "the care rules from the previous slide.")
    b.cards("PERMANENT vs TEMPORARY", "Choosing the Right Magnet", [
        ("Need it to last?", "Use a permanent (steel) magnet — for a compass "
         "or a fridge magnet."),
        ("Need to switch it?", "Use an electromagnet — for a crane or an "
         "electric bell."),
        ("Need it strong?", "An electromagnet can be made very strong with "
         "more turns and more current."),
        ("Keep it safe", "Either kind weakens with heat, shock and careless "
         "storage, so handle with care."),
    ], notes="Wrap the chapter by matching the magnet to the job: permanent "
             "for lasting magnetism, electromagnet for switchable strength.")
    b.bullets("KEEPERS", "Why Magnets Need Keepers", [
        ("Free poles weaken", "Left on their own, the free poles of a magnet "
         "slowly lose their strength."),
        ("Store in pairs", "Place two bar magnets side by side with unlike "
         "poles next to each other."),
        ("Add soft-iron keepers", "Lay small soft-iron bars across the ends to "
         "link the poles together."),
        ("A complete loop", "The keepers give the magnetism a closed path, so "
         "the magnets stay strong for much longer."),
    ], panel_title="Storing bar magnets safely",
       notes="Explain how keepers work: by completing the magnetic loop they "
             "stop the poles weakening. This ties the storage rule back to the "
             "idea of field lines forming closed loops.")

    b.recap("WRAP UP", "Quick Recap", [
        ("Making magnets", "single touch, double touch, induction, electricity"),
        ("Single touch", "stroke one way, lift between strokes"),
        ("Electromagnet", "coil + soft-iron core; magnetism while current "
         "flows"),
        ("Stronger", "more turns, more current, soft-iron core"),
        ("Care", "store in pairs with keepers; avoid heat, shock, stray "
         "fields"),
        ("Demagnetise", "heating, hammering/dropping, an AC coil"),
    ], notes="Rapid recap. Cold-call students for the ways to make a magnet "
             "and the ways to demagnetise one.")

    # ---- Quiz 2 ----
    b.quiz_intro("Quiz 2", "Final Check — Using & Losing Magnetism", 4)
    b.quiz_q(1, "Uses", "A crane in a scrapyard lifts heavy iron using a:",
             ["Permanent magnet", "Wooden hook", "An electromagnet",
              "A plastic clamp"])
    b.quiz_a(1, "C. An electromagnet",
             "A crane uses an electromagnet: switch the current on to lift the "
             "iron, and off to drop it. A permanent magnet could not let go.")
    b.quiz_q(2, "Care", "The soft-iron pieces placed across the ends of stored "
             "magnets are called:", ["Poles", "Keepers", "Cores", "Coils"])
    b.quiz_a(2, "B. Keepers",
             "Keepers are soft-iron pieces placed across the poles of stored "
             "magnets to preserve their magnetism.")
    b.quiz_q(3, "Demagnetise", "Which of these will make a magnet lose its "
             "magnetism?", ["Storing it with keepers",
                            "Strongly heating it", "Keeping it dry",
                            "Handling it gently"])
    b.quiz_a(3, "B. Strongly heating it",
             "Strong heating, repeated hammering or dropping, and an AC coil "
             "all destroy magnetism. Careful storage with keepers preserves "
             "it.")
    b.quiz_q(4, "Electromagnet", "The magnetism of an electromagnet lasts:",
             ["For ever", "Only while current flows", "Only at night",
              "Only when it is hot"])
    b.quiz_a(4, "B. Only while current flows",
             "An electromagnet is a temporary magnet — it is magnetic only "
             "while current flows through its coil, and loses it when switched "
             "off.")

    b.closing("Magnets On Demand",
              "From a stroked steel bar to a switchable electromagnet, we can "
              "make, use and even switch off magnetism whenever we need it.")
    return b


def build():
    jobs = [
        ("G06_S30_Simple_Machines_1.pptx", sm_deck1),
        ("G06_S31_Simple_Machines_2.pptx", sm_deck2),
        ("G06_S52_Light_1.pptx", light_deck1),
        ("G06_S53_Light_2.pptx", light_deck2),
        ("G06_S69_Magnetism_1.pptx", mag_deck1),
        ("G06_S70_Magnetism_2.pptx", mag_deck2),
    ]
    for fname, fn in jobs:
        b = fn()
        issues = b.qa()
        path = os.path.join(OUT, fname)
        b.save(path)
        print(f"\n=== {fname} ===")
        print(f"slides: {len(b.prs.slides._sldIdLst)}")
        if issues:
            print("QA ISSUES:")
            for i in issues:
                print("  -", i)
        else:
            print("QA: no overlaps / off-slide shapes detected")


if __name__ == "__main__":
    build()
