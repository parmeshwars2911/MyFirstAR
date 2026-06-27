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


# ---------------------------------------------------------------------------
def build():
    jobs = [
        ("G06_S30_Simple_Machines_1.pptx", sm_deck1),
        ("G06_S31_Simple_Machines_2.pptx", sm_deck2),
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
