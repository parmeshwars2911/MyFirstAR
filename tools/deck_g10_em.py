"""
Grade 10 Physics — Chapter: Electromagnetism.
S101 (magnetic effect of current, field of wire/loop/solenoid, electromagnet),
S102 (force on a conductor, DC motor, electromagnetic induction, AC generator,
transformer).  ICSE Class 10 (Selina) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade10"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Electromagnetism  •  ICSE Class 10 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    wire = b.asset("g10em_wire", D.field_straight_wire("g10em_wire"))
    sol = b.asset("g10em_sol", D.solenoid_field("g10em_sol"))
    hero = b.asset("g10_em_hero", sol)

    b.title("ICSE • Class 10 • Magnetism", "Magnetic Effect of Current",
            "Oersted's experiment  •  Field of a wire, loop & solenoid  •  "
            "The electromagnet", img=hero)
    b.objectives([
        "Describe Oersted's experiment linking current and magnetism",
        "Draw the magnetic field around a straight current-carrying wire",
        "Use the right-hand thumb rule for field direction",
        "Describe the field of a current loop and a solenoid",
        "Explain how an electromagnet is made and strengthened",
        "Compare an electromagnet with a permanent magnet",
    ])
    b.divider(1, "Part 1", "Current Makes Magnetism",
              "Oersted's discovery and the field of a wire")
    b.bullets("OERSTED", "Oersted's Experiment", [
        ("The discovery", "A compass needle near a wire deflects when a "
         "current flows through the wire."),
        ("What it shows", "An electric current produces a magnetic field "
         "around it."),
        ("Reverse the current", "The needle deflects the other way — the field "
         "direction reverses too."),
        ("No current, no effect", "Switch the current off and the needle "
         "returns to north."),
    ], panel_title="Electricity and magnetism are linked",
       notes="Oersted's chance discovery: current creates magnetism. The "
             "needle deflection and its reversal are the key observations.")
    b.text_image("STRAIGHT WIRE", "Field Around a Straight Wire",
                 ["The magnetic field lines form concentric circles around the "
                  "wire.",
                  "The field is stronger close to the wire and weakens with "
                  "distance.",
                  "Right-hand thumb rule: thumb points along the current, "
                  "curled fingers show the field direction.",
                  "Reversing the current reverses the direction of the field "
                  "lines."],
                 wire, img_side="right", img_w=4.8, img_h=3.8,
                 panel_title="Circular field lines",
                 caption="Right-hand thumb rule gives the direction",
                 notes="Field = concentric circles. Demonstrate the right-hand "
                       "rule with your own hand; reversal flips the circles.")
    b.bullets("CURRENT LOOP", "Field Due to a Circular Loop", [
        ("Each part adds up", "Every bit of the loop circles a field; inside "
         "the loop they all add together."),
        ("Straight through the centre", "The field at the centre is "
         "perpendicular to the plane of the loop."),
        ("Like a tiny magnet", "One face of the loop acts as a north pole, the "
         "other as a south pole."),
        ("More turns, stronger", "Many turns side by side make the field much "
         "stronger."),
    ], panel_title="Bending the wire concentrates the field",
       notes="A loop concentrates the field through its centre, behaving like "
             "a small magnet — the stepping stone to the solenoid.")
    b.text_image("SOLENOID", "The Solenoid",
                 ["A solenoid is a long coil of many turns of insulated wire.",
                  "When current flows, its field is just like that of a bar "
                  "magnet, with a N and a S pole.",
                  "The field inside is strong and nearly uniform.",
                  "Reversing the current swaps the north and south poles."],
                 sol, img_side="left", img_w=6.0, img_h=3.6,
                 panel_title="A coil that acts like a bar magnet",
                 caption="Reverse the current to swap the poles",
                 notes="Solenoid = many loops = bar-magnet field. Strong "
                       "uniform field inside; poles reverse with the current.")
    b.statement("ELECTROMAGNET", "Making an Electromagnet",
                "Put a soft-iron core inside a solenoid and it becomes a "
                "powerful, switchable magnet — an electromagnet.",
                points=["The soft-iron core greatly increases the strength of "
                        "the field.",
                        "Stronger with more turns, more current, and a soft-"
                        "iron core.",
                        "It is a magnet only while the current flows."],
                notes="Electromagnet = solenoid + soft-iron core. Strength "
                      "depends on turns, current and the core.")
    b.bullets("STRENGTH", "What Makes an Electromagnet Stronger", [
        ("More current", "A larger current through the coil gives a stronger "
         "magnetic field."),
        ("More turns", "Packing in more turns of wire increases the field."),
        ("Soft-iron core", "A soft-iron core multiplies the strength many "
         "times over."),
        ("Shorter / closer", "Bringing the turns closer together concentrates "
         "the field."),
    ], panel_title="Current, turns and core",
       notes="The three controllable factors: current, number of turns and the "
             "core. These are common one-mark answers.")
    b.cards("ELECTRO vs PERMANENT", "Electromagnet vs Permanent Magnet", [
        ("Switchable", "An electromagnet can be turned on and off; a permanent "
         "magnet is always magnetic."),
        ("Adjustable strength", "Its strength can be changed by varying the "
         "current; a permanent magnet's cannot."),
        ("Reversible poles", "Its poles can be reversed by reversing the "
         "current."),
        ("Very strong", "It can be made far stronger than an ordinary "
         "permanent magnet."),
    ], notes="The four advantages of an electromagnet: switchable, adjustable, "
             "reversible, and can be very strong.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Oersted", "A compass placed under a straight wire deflects "
             "only when:", ["The wire is made of iron",
              "A current flows through the wire", "The wire is very long",
              "The compass is heated"])
    b.quiz_a(1, "B. A current flows through the wire",
             "Oersted showed that a current produces a magnetic field. With no "
             "current there is no field, so the needle stays pointing north; "
             "switch the current on and it deflects.")
    b.quiz_q(2, "Reverse It", "If the current in a solenoid is reversed, its "
             "magnetic poles:", ["Disappear", "Stay the same",
              "Swap over (N becomes S)", "Become stronger"])
    b.quiz_a(2, "C. Swap over (N becomes S)",
             "The direction of the field follows the current. Reversing the "
             "current reverses the field, so the north and south ends of the "
             "solenoid interchange.")
    b.quiz_q(3, "Stronger Magnet", "Which change would NOT make an "
             "electromagnet stronger?", ["Increasing the current",
              "Adding more turns of wire", "Using a soft-iron core",
              "Using a wooden core instead of iron"])
    b.quiz_a(3, "D. Using a wooden core",
             "Wood is non-magnetic, so it adds nothing — far weaker than soft "
             "iron. Strength is increased by more current, more turns and a "
             "soft-iron core.")
    b.quiz_q(4, "Why Soft Iron?", "An electromagnet uses a soft-iron core "
             "rather than steel because soft iron:",
             ["Stays magnetised permanently", "Loses its magnetism as soon as "
              "the current stops, so the magnet can be switched off",
              "Is a good conductor", "Is lighter"])
    b.quiz_a(4, "B. Loses magnetism when the current stops",
             "Soft iron magnetises and demagnetises easily, so the "
             "electromagnet works only while current flows. Steel would keep "
             "its magnetism and could not be switched off.")
    b.divider(2, "Part 2", "Using Electromagnets",
              "From scrapyards to doorbells")
    b.cards("USES", "Uses of Electromagnets", [
        ("Lifting magnets", "Cranes in scrapyards lift and drop heavy iron by "
         "switching the magnet on and off."),
        ("Electric bell", "An electromagnet repeatedly pulls a clapper to "
         "strike the gong."),
        ("Relays", "A small current's electromagnet switches on a much larger "
         "circuit."),
        ("Loudspeakers", "A changing current in a coil moves a cone to make "
         "sound."),
    ], notes="Each use exploits the switchable, controllable magnetism. The "
             "lifting magnet and electric bell are the classic examples.")
    b.bullets("ELECTRIC BELL", "How an Electric Bell Works", [
        "Pressing the switch completes the circuit and the electromagnet is "
        "energised.",
        "It attracts the soft-iron armature, so the hammer strikes the gong.",
        "This movement breaks the circuit at a contact, switching the magnet "
        "off.",
        "A spring pulls the armature back, the contact remakes, and the cycle "
        "repeats rapidly.",
    ], panel_title="A make-and-break circuit",
       notes="The make-and-break action is the heart of the bell: the magnet "
             "switches itself off as the hammer moves, then on again.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Oersted", "a current produces a magnetic field"),
        ("Straight wire", "circular field lines; right-hand thumb rule"),
        ("Loop & solenoid", "concentrate the field; solenoid acts like a bar "
         "magnet"),
        ("Electromagnet", "solenoid + soft-iron core; switchable and strong"),
        ("Advantages", "switchable, adjustable, reversible, very strong"),
        ("Uses", "lifting magnets, electric bell, relays, loudspeakers"),
    ], notes="Rapid recap; the right-hand rule and the electromagnet "
             "advantages are the key recall items.")
    b.quiz_intro("Quiz 2", "Final Check — Fields & Electromagnets", 5)
    b.quiz_q(1, "Field Shape", "The magnetic field lines around a long "
             "straight current-carrying wire are:",
             ["Straight lines along the wire",
              "Concentric circles around the wire",
              "Radial lines pointing outward", "There is no field"])
    b.quiz_a(1, "B. Concentric circles around the wire",
             "The field circles the wire. Closer to the wire the circles are "
             "tighter (stronger field); the right-hand thumb rule gives their "
             "direction.")
    b.quiz_q(2, "Scrapyard Crane", "A scrapyard uses an electromagnet rather "
             "than a permanent magnet to move cars mainly because it can:",
             ["Never lose strength", "Be switched off to drop the load",
              "Work without electricity", "Lift wood and plastic too"])
    b.quiz_a(2, "B. Be switched off to drop the load",
             "The whole point is control: turn the current on to grab the "
             "scrap and off to release it. A permanent magnet could never let "
             "go.")
    b.quiz_q(3, "Doorbell Buzz", "An electric bell rings continuously while "
             "the button is pressed because the circuit:",
             ["Stays permanently closed", "Repeatedly makes and breaks itself "
              "as the hammer moves", "Has no electromagnet",
              "Uses a permanent magnet"])
    b.quiz_a(3, "B. Repeatedly makes and breaks itself",
             "As the armature is attracted, it breaks the contact and the "
             "magnet switches off; a spring returns it, remaking the contact. "
             "This rapid make-and-break keeps the hammer striking.")
    b.quiz_q(4, "More Turns", "Doubling the number of turns on a solenoid "
             "(same current) makes its magnetic field:",
             ["Weaker", "Stronger", "Reverse direction", "Disappear"])
    b.quiz_a(4, "B. Stronger",
             "More turns means more current loops adding their fields "
             "together, so the solenoid's magnetic field becomes stronger.")
    b.quiz_q(5, "Compass Test", "A solenoid hangs freely and comes to rest "
             "pointing north–south. This proves the solenoid:",
             ["Is made of iron", "Behaves like a bar magnet with N and S "
              "poles", "Carries no current", "Is an insulator"])
    b.quiz_a(5, "B. Behaves like a bar magnet",
             "Only a magnet aligns itself north–south in the Earth's field. "
             "Since the current-carrying solenoid does so, it must have north "
             "and south poles like a bar magnet.")
    b.closing("Electricity That Magnetises",
              "A simple coil and a current give us magnets we can switch, "
              "tune and reverse at will.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    motor = b.asset("g10em_motor", D.dc_motor("g10em_motor"))
    emi = b.asset("g10em_emi", D.emi_coil("g10em_emi"))
    hero = b.asset("g10_motor_hero", motor)

    b.title("ICSE • Class 10 • Magnetism", "Motors & Induction",
            "Force on a conductor  •  The DC motor  •  Electromagnetic "
            "induction  •  Generators", img=hero)
    b.objectives([
        "State the force on a current-carrying conductor in a field",
        "Apply Fleming's left-hand rule",
        "Explain how a simple DC motor works",
        "Describe electromagnetic induction",
        "State Faraday's laws of electromagnetic induction",
        "Outline how a generator and a transformer work",
    ])
    b.divider(1, "Part 1", "The Motor Effect",
              "When a current feels a force in a magnetic field")
    b.text_image("MOTOR EFFECT", "Force on a Conductor",
                 ["A current-carrying conductor placed in a magnetic field "
                  "experiences a force.",
                  "The force is largest when the conductor is at right angles "
                  "to the field.",
                  "It is bigger for a stronger field, a larger current or a "
                  "longer conductor.",
                  "Reversing the current — or the field — reverses the "
                  "direction of the force."],
                 motor, img_side="left", img_w=6.0, img_h=3.6,
                 panel_title="Current + field → force",
                 caption="Opposite forces on the two sides of the coil",
                 notes="The motor effect. Force depends on field, current and "
                       "length, and is maximum at 90°. This drives the motor.")
    b.statement("FLEMING", "Fleming's Left-Hand Rule",
                "Fleming's left-hand rule gives the direction of the force on "
                "the conductor.",
                points=["Hold the thumb, first finger and second finger of the "
                        "left hand at right angles.",
                        "First finger → Field, seCond finger → Current, "
                        "thuMb → Motion (force).",
                        "Use it for motors — anything that is made to move."],
                notes="Teach the mnemonic: First=Field, seCond=Current, "
                      "thuMb=Motion. Left hand for motors.")
    b.text_image("DC MOTOR", "The Simple DC Motor",
                 ["A rectangular coil sits between the poles of a magnet.",
                  "Current flows in opposite directions along the two sides, "
                  "so they feel opposite forces.",
                  "This pair of forces makes the coil rotate.",
                  "A split-ring commutator reverses the current every half "
                  "turn, keeping it spinning the same way."],
                 motor, img_side="right", img_w=6.0, img_h=3.6,
                 panel_title="Turning electricity into motion",
                 caption="The commutator keeps the rotation going one way",
                 notes="The commutator is the crucial part — it flips the "
                       "current each half turn so the coil keeps turning "
                       "continuously.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Which Hand?", "To find the direction in which a motor's coil "
             "is pushed, you use:", ["Fleming's right-hand rule",
              "Fleming's left-hand rule", "The right-hand thumb rule",
              "Ohm's law"])
    b.quiz_a(1, "B. Fleming's left-hand rule",
             "The left-hand rule gives the direction of force (motion) on a "
             "current in a field — used for motors. The right-hand rule is for "
             "induced currents in generators.")
    b.quiz_q(2, "No Force", "A current-carrying wire lies exactly parallel to "
             "the magnetic field. The force on it is:",
             ["Maximum", "Zero", "Half the maximum", "Reversed"])
    b.quiz_a(2, "B. Zero",
             "The motor effect is greatest when the wire is at 90° to the "
             "field and zero when it lies along the field. Parallel to the "
             "field, there is no force.")
    b.quiz_q(3, "Reverse Both", "In a motor, both the current AND the magnetic "
             "field are reversed at the same time. The coil now turns:",
             ["The opposite way", "The same way as before", "Twice as fast",
              "It stops"])
    b.quiz_a(3, "B. The same way as before",
             "Reversing the current alone, or the field alone, flips the "
             "force. Reversing both flips it twice — back to the original "
             "direction — so the coil turns the same way.")
    b.quiz_q(4, "Commutator's Job", "The split-ring commutator in a DC motor "
             "is needed to:", ["Increase the voltage",
              "Reverse the current in the coil every half turn so it keeps "
              "rotating one way", "Stop the coil", "Cool the motor"])
    b.quiz_a(4, "B. Reverse the current every half turn",
             "Without it, the coil would stop after a half turn. The "
             "commutator flips the current direction at just the right moment "
             "so the forces keep driving the coil the same way round.")
    b.quiz_q(5, "Speed It Up", "Which change would make a simple DC motor spin "
             "faster?", ["Using a weaker magnet",
              "Increasing the current through the coil",
              "Using fewer turns on the coil", "Removing the commutator"])
    b.quiz_a(5, "B. Increasing the current through the coil",
             "A larger current means a bigger force on each side of the coil, "
             "turning it more strongly and faster. A stronger magnet or more "
             "turns would help too; a weaker magnet or fewer turns would slow "
             "it.")
    b.divider(2, "Part 2", "Electromagnetic Induction",
              "Magnetism making electricity")
    b.text_image("INDUCTION", "Electromagnetic Induction",
                 ["Moving a magnet into or out of a coil makes a current flow "
                  "in the coil.",
                  "No battery is needed — the changing magnetic field "
                  "'induces' the current.",
                  "A galvanometer deflects, showing the induced current.",
                  "Stop moving the magnet and the current stops — only a "
                  "change induces it."],
                 emi, img_side="left", img_w=6.0, img_h=3.6,
                 panel_title="A changing field makes a current",
                 caption="Move the magnet → the galvanometer deflects",
                 notes="Induction is the reverse of the motor effect. Key "
                       "word: CHANGE. A stationary magnet induces nothing.")
    b.statement("FARADAY", "Faraday's Laws of Induction",
                "Faraday summarised electromagnetic induction in two laws.",
                points=["First law: an EMF is induced whenever the magnetic "
                        "field through a coil changes.",
                        "Second law: the size of the induced EMF is greater "
                        "when the field changes faster.",
                        "More turns, a stronger magnet and faster movement all "
                        "increase the induced EMF."],
                notes="Faraday: a change of field induces an EMF; faster change "
                      "(or more turns) gives a bigger EMF.")
    b.cards("BIGGER EMF", "How to Increase the Induced Current", [
        ("Move faster", "A quicker change of the magnetic field induces a "
         "larger EMF."),
        ("More turns", "A coil with more turns gives a bigger induced EMF."),
        ("Stronger magnet", "A more powerful magnet increases the change in "
         "field."),
        ("No movement, no EMF", "If nothing changes, no current is induced."),
    ], notes="The factors that increase induced EMF — all are about a bigger "
             "or faster change of field.")
    b.statement("FLEMING (RIGHT)", "Fleming's Right-Hand Rule",
                "For induction (generators) we use the RIGHT hand to find the "
                "direction of the induced current.",
                points=["Hold thumb, first finger and second finger of the "
                        "RIGHT hand at right angles.",
                        "First finger → Field, thuMb → Motion, seCond finger → "
                        "induced Current.",
                        "Left hand for motors (force); right hand for "
                        "generators (induced current)."],
                notes="Pair this with the left-hand rule: left = motor "
                      "(force), right = generator (induced current). A frequent "
                      "point of confusion.")
    b.cards("GENERATOR & TRANSFORMER", "Two Machines From Induction", [
        ("AC generator", "A coil spun in a magnetic field induces an "
         "alternating current — how power stations make electricity."),
        ("Slip rings", "Connect the spinning coil to the outside circuit, "
         "giving AC."),
        ("Transformer", "Uses a changing current in one coil to induce a "
         "voltage in another."),
        ("Step up / down", "More turns on the output coil step the voltage "
         "up; fewer step it down."),
    ], notes="Generator: motion → electricity (induction). Transformer: "
             "changes AC voltage using two coils and a changing field.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Motor effect", "current in a field feels a force"),
        ("Fleming's left hand", "Field, Current, Motion — for motors"),
        ("DC motor", "opposite forces turn a coil; commutator keeps it going"),
        ("Induction", "a changing field induces a current — no battery"),
        ("Faraday", "EMF appears on change; faster change → bigger EMF"),
        ("Generator & transformer", "make AC, and step voltage up or down"),
    ], notes="Rapid recap; contrast the motor effect (left hand) with "
             "induction (right hand / generators).")
    b.quiz_intro("Quiz 2", "Final Check — Induction & Machines", 5)
    b.quiz_q(1, "Make It Deflect", "A bar magnet is held still inside a coil "
             "connected to a galvanometer. The galvanometer reads zero "
             "because:", ["The magnet is too weak",
              "There is no change in the magnetic field, so no EMF is "
              "induced", "The coil has too few turns",
              "The wire is broken"])
    b.quiz_a(1, "B. No change in field, so no EMF",
             "Induction needs a CHANGING field. A motionless magnet gives a "
             "steady field through the coil, so nothing is induced. Move it "
             "and the needle springs to life.")
    b.quiz_q(2, "Bigger Kick", "Which would give the largest deflection on the "
             "galvanometer?", ["Pushing a weak magnet in slowly",
              "Pushing a strong magnet in quickly",
              "Holding a strong magnet still", "Removing the coil"])
    b.quiz_a(2, "B. A strong magnet pushed in quickly",
             "The induced EMF grows with a stronger magnet and a faster "
             "change. A strong magnet moved quickly maximises both, giving the "
             "biggest deflection.")
    b.quiz_q(3, "Motor or Generator?", "A device that converts electrical "
             "energy into motion is a motor. A device that converts motion "
             "into electrical energy is a:", ["Transformer", "Generator",
              "Resistor", "Fuse"])
    b.quiz_a(3, "B. Generator",
             "A generator does the reverse of a motor: spinning a coil in a "
             "field induces a current, turning mechanical motion into "
             "electrical energy.")
    b.quiz_q(4, "Transformer Needs AC", "A transformer works only with "
             "alternating current because it relies on:",
             ["A steady current", "A continually changing magnetic field to "
              "induce a voltage in the second coil", "A permanent magnet",
              "A commutator"])
    b.quiz_a(4, "B. A continually changing magnetic field",
             "Induction needs change. AC constantly changes, so it keeps the "
             "field through the second coil changing and a voltage is induced. "
             "A steady DC current would induce nothing.")
    b.quiz_q(5, "Step Up", "A transformer has more turns on its output "
             "(secondary) coil than on its input. It will:",
             ["Step the voltage down", "Step the voltage up",
              "Leave the voltage unchanged", "Stop the current"])
    b.quiz_a(5, "B. Step the voltage up",
             "The voltage shares out in proportion to the turns. More turns on "
             "the secondary than the primary means a higher output voltage — a "
             "step-up transformer.")
    b.closing("Motion and Electricity, Two Ways",
              "A current in a field moves a motor; a moving magnet powers a "
              "city — electromagnetism runs the modern world.")
    return b


def build():
    for fname, fn in [("G10_S101_Electromagnetism_1.pptx", deck1),
                      ("G10_S102_Electromagnetism_2.pptx", deck2)]:
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
