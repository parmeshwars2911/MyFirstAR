"""
Grade 6 (ICSE / Selina Concise Physics) assessment bank + builder.

Chapters (from tools/decks.json):
  - Simple Machines : S30 (Lesson 1), S31 (Lesson 2)
  - Light           : S52 (Lesson 1), S53 (Lesson 2)
  - Magnetism       : S69 (Lesson 1), S70 (Lesson 2)

Each chapter has ONE workout (practice/quiz) deck that covers BOTH of its
concept lessons (20 MCQs + 5 subjective questions). Each concept session AND
each workout has a 10-MCQ homework PDF. Every question is drawn ONLY from the
topics of the session(s) it covers — nothing out of syllabus.

MCQ format     : {"topic","q","options"[4],"correct"(0-3),"why"}
Subjective     : {"topic","q","marks","answer"[points]}
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from engine import C
from assessment import build_workout, build_homework, balance_options

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WK_OUT = os.path.join(ROOT, "workouts", "Grade06")
HW_OUT = os.path.join(ROOT, "homework", "Grade06")
os.makedirs(WK_OUT, exist_ok=True)
os.makedirs(HW_OUT, exist_ok=True)
GRADE = "Class 6"


# ===========================================================================
# SIMPLE MACHINES  (S30 + S31)
# ===========================================================================
SM_WORKOUT_MCQ = [
    {"topic": "Work", "q": "A porter carries a heavy suitcase on his head and "
     "walks 50 m along a level platform at steady speed. The work he does "
     "against gravity is:",
     "options": ["Large and positive", "Zero", "Negative", "Equal to the "
                 "suitcase's weight"], "correct": 1,
     "why": "His supporting force is vertical (up) but the motion is "
            "horizontal, so the displacement in the direction of that force is "
            "zero — hence the work done against gravity is zero."},
    {"topic": "Units", "q": "Which of the following is NOT a unit of work or "
     "energy?",
     "options": ["Joule", "Newton metre", "Watt", "Erg"], "correct": 2,
     "why": "The watt is the unit of power (1 W = 1 J/s), not of work or "
            "energy. Joule, newton-metre and erg are all units of energy."},
    {"topic": "Machine functions", "q": "Which of these is NOT something a "
     "simple machine can do for us?",
     "options": ["Multiply a small effort to move a large load",
                 "Change the direction of the applied force",
                 "Create extra energy to do more work",
                 "Let us apply the effort at a convenient point"],
     "correct": 2,
     "why": "A machine never creates energy — it only transfers and "
            "redistributes the work put into it. Output work can never exceed "
            "input work."},
    {"topic": "Mechanical advantage", "q": "A machine overcomes a load of "
     "600 N using an effort of 150 N. Its mechanical advantage is:",
     "options": ["4", "0.25", "750 N", "450 N"], "correct": 0,
     "why": "MA = Load / Effort = 600 / 150 = 4. It is a ratio of two forces, "
            "so it has no unit."},
    {"topic": "Efficiency", "q": "A machine is supplied 500 J of work and does "
     "400 J of useful work. Its efficiency is:",
     "options": ["125%", "80%", "100 J", "20%"], "correct": 1,
     "why": "Efficiency = (useful work output / work input) x 100 = "
            "(400 / 500) x 100 = 80%."},
    {"topic": "Efficiency", "q": "The efficiency of every real machine is less "
     "than 100% mainly because:",
     "options": ["the load is always too heavy",
                 "some input work is wasted against friction and in moving the "
                 "machine's own parts",
                 "mechanical advantage is always less than one",
                 "the effort is applied in the wrong direction"], "correct": 1,
     "why": "Part of the input work is always used up against friction and in "
            "lifting the machine's own moving parts, so useful output is "
            "always less than the input."},
    {"topic": "Ideal machine", "q": "For an ideal (frictionless) machine, "
     "which relation is true?",
     "options": ["MA > VR", "MA = VR", "MA < VR", "MA = 0"], "correct": 1,
     "why": "An ideal machine has no friction and weightless parts, so its "
            "efficiency is 100% and its mechanical advantage equals its "
            "velocity ratio (MA = VR)."},
    {"topic": "Lever", "q": "The fixed point about which a lever turns is "
     "called the:",
     "options": ["effort arm", "load", "fulcrum", "pivot arm"], "correct": 2,
     "why": "A lever turns about a fixed point called the fulcrum. The other "
            "two points are where the load and the effort act."},
    {"topic": "Lever principle", "q": "A crowbar lifts an 800 N rock. The load "
     "is 20 cm from the fulcrum and the effort is applied 80 cm from it. The "
     "ideal effort needed is:",
     "options": ["200 N", "3200 N", "800 N", "160 N"], "correct": 0,
     "why": "By the principle of the lever, Load x load-arm = Effort x "
            "effort-arm: 800 x 20 = E x 80, so E = 200 N."},
    {"topic": "Levers", "q": "Which of the following is a first-order lever?",
     "options": ["A wheelbarrow", "A pair of scissors", "A pair of sugar "
                 "tongs", "A nutcracker"], "correct": 1,
     "why": "In a pair of scissors the fulcrum (the rivet) lies between the "
            "effort and the load, so it is a first-order lever. The others are "
            "second- or third-order levers."},
    {"topic": "Levers", "q": "The mechanical advantage of a second-order lever "
     "is always:",
     "options": ["less than 1", "equal to 1", "greater than 1", "zero"],
     "correct": 2,
     "why": "In a second-order lever the load lies between the fulcrum and the "
            "effort, so the effort-arm is always longer than the load-arm, "
            "giving MA > 1 (a force multiplier)."},
    {"topic": "Levers", "q": "A pair of forceps (tongs) has a mechanical "
     "advantage less than one. We still use such third-order levers because "
     "they:",
     "options": ["multiply the effort", "give a gain in speed and a wider "
                 "range of movement", "reduce friction", "change the "
                 "direction of the force"], "correct": 1,
     "why": "A third-order lever has its effort between the fulcrum and load, "
            "so MA < 1; it is used because the load end moves faster and over "
            "a larger distance than the effort."},
    {"topic": "Levers", "q": "The human forearm lifting a load held in the "
     "hand acts as a lever of which order?",
     "options": ["First order", "Second order", "Third order", "No order"],
     "correct": 2,
     "why": "The elbow is the fulcrum and the biceps (effort) acts between the "
            "elbow and the load in the hand, so the forearm is a third-order "
            "lever."},
    {"topic": "Pulley", "q": "A single fixed pulley is used to draw water from "
     "a well mainly because it:",
     "options": ["multiplies the effort", "has a mechanical advantage of 2",
                 "lets you pull down to raise the bucket up (changes the "
                 "direction of effort)", "reduces the weight of the water"],
     "correct": 2,
     "why": "A single fixed pulley has an ideal MA of 1; it does not reduce "
            "the effort but lets you apply it in a convenient (downward) "
            "direction."},
    {"topic": "Pulley", "q": "The ideal mechanical advantage of a single "
     "movable pulley is:",
     "options": ["1", "2", "0.5", "4"], "correct": 1,
     "why": "In a single movable pulley the load is shared by two segments of "
            "the rope, so the effort is half the load and the ideal MA is 2."},
    {"topic": "Wheel and axle", "q": "A steering wheel of radius 20 cm turns "
     "an axle of radius 4 cm. Its ideal mechanical advantage is:",
     "options": ["5", "80", "0.2", "16"], "correct": 0,
     "why": "For a wheel and axle, MA = radius of wheel / radius of axle = "
            "20 / 4 = 5."},
    {"topic": "Inclined plane", "q": "A 12 m long ramp rises to a height of "
     "3 m. The ideal mechanical advantage of the ramp is:",
     "options": ["4", "9", "36", "0.25"], "correct": 0,
     "why": "For an inclined plane, MA = length of slope / height = "
            "12 / 3 = 4."},
    {"topic": "Wedge", "q": "A wedge, such as the blade of an axe, is "
     "essentially:",
     "options": ["a single lever", "two inclined planes joined back to back",
                 "a wheel and axle", "a movable pulley"], "correct": 1,
     "why": "A wedge is made of two inclined planes joined along their slopes; "
            "it is used to separate, split or cut, as an axe splits wood."},
    {"topic": "Screw", "q": "A screw can be regarded as:",
     "options": ["an inclined plane wrapped around a cylinder",
                 "a first-order lever", "two pulleys in series",
                 "a flat wedge"], "correct": 0,
     "why": "The thread of a screw is simply an inclined plane wound around a "
            "cylinder; the distance between two threads is its pitch."},
    {"topic": "Care of machines", "q": "Oiling and greasing the moving parts "
     "of a machine raises its efficiency because it:",
     "options": ["increases its mechanical advantage", "reduces the friction "
                 "between the parts", "increases the load it can lift",
                 "creates extra energy"], "correct": 1,
     "why": "Oil reduces friction between moving parts, so less input work is "
            "wasted as heat and the efficiency rises (closer to the ideal)."},
]

SM_WORKOUT_SUBJ = [
    {"topic": "Work", "marks": 3,
     "q": "Define work and state its SI unit. A boy pushes hard against a wall "
          "with a force of 200 N but the wall does not move. How much work "
          "does he do? Give a reason.",
     "answer": [
        "Work is done when a force acts on a body and the body moves in the "
        "direction of the force: Work = Force x distance moved (W = F x s).",
        "SI unit of work is the joule (J); 1 J = 1 N moved through 1 m.",
        "Work done = 0, because the wall does not move (displacement = 0), so "
        "no work is done however large the force applied."]},
    {"topic": "MA, VR & Efficiency", "marks": 4,
     "q": "Define mechanical advantage and velocity ratio. Why is the "
          "efficiency of an actual machine always less than 100%? Write the "
          "relation between efficiency, MA and VR.",
     "answer": [
        "Mechanical advantage (MA) = Load / Effort; it tells how many times a "
        "machine multiplies the effort (no unit).",
        "Velocity ratio (VR) = distance moved by effort / distance moved by "
        "load (no unit).",
        "Efficiency is always < 100% because some input work is always used up "
        "against friction and in moving the machine's own parts, so useful "
        "output < input.",
        "Relation: Efficiency = MA / VR."]},
    {"topic": "Principle of a lever", "marks": 3,
     "q": "State the principle of a lever. A see-saw has a 400 N child sitting "
          "1.5 m from the pivot. Where must a 600 N child sit on the other "
          "side to balance it?",
     "answer": [
        "Principle (law of moments): when a lever is balanced, "
        "Load x load-arm = Effort x effort-arm (anticlockwise moment = "
        "clockwise moment).",
        "400 x 1.5 = 600 x d, so 600 = 600 d.",
        "d = 1.0 m from the pivot on the opposite side."]},
    {"topic": "Orders of levers", "marks": 4,
     "q": "Name the three orders of levers. For each, state the relative "
          "position of the load, effort and fulcrum, and give one example.",
     "answer": [
        "First order: fulcrum lies between the load and the effort — e.g. a "
        "see-saw, a pair of scissors or a crowbar.",
        "Second order: load lies between the fulcrum and the effort — e.g. a "
        "wheelbarrow or a nutcracker (MA always > 1).",
        "Third order: effort lies between the fulcrum and the load — e.g. "
        "forceps, a fishing rod or the human forearm (MA always < 1)."]},
    {"topic": "Inclined plane", "marks": 3,
     "q": "What is an inclined plane? A man rolls a 500 N barrel up a 4 m long "
          "plank onto a platform 1 m high. Find the ideal mechanical "
          "advantage and the ideal effort needed.",
     "answer": [
        "An inclined plane is a sloping flat surface used to raise a load with "
        "less effort applied over a longer distance.",
        "Ideal MA = length of slope / height = 4 / 1 = 4.",
        "Ideal effort = Load / MA = 500 / 4 = 125 N."]},
]

SM_HW_S30 = [
    {"topic": "Work", "q": "Work is said to be done only when:",
     "options": ["a force is applied to a body", "a body moves in the "
                 "direction of the applied force", "a body stays at rest",
                 "energy is stored in a body"], "correct": 1,
     "why": "Work needs both a force and movement in the direction of that "
            "force."},
    {"topic": "Units", "q": "The SI unit of work is the:",
     "options": ["newton", "joule", "watt", "metre"], "correct": 1,
     "why": "Work and energy are measured in joules (J)."},
    {"topic": "Energy", "q": "The capacity of a body to do work is called "
     "its:",
     "options": ["power", "energy", "force", "efficiency"], "correct": 1,
     "why": "Energy is the capacity to do work; it is also measured in "
            "joules."},
    {"topic": "Machine functions", "q": "A machine used to lift a heavy load "
     "with a small effort is acting as a:",
     "options": ["speed multiplier", "force multiplier", "direction changer",
                 "energy source"], "correct": 1,
     "why": "When MA > 1 the machine multiplies the effort, so it acts as a "
            "force multiplier."},
    {"topic": "Mechanical advantage", "q": "Mechanical advantage is defined as "
     "the ratio:",
     "options": ["Effort / Load", "Load / Effort", "Work out / Work in",
                 "Load x Effort"], "correct": 1,
     "why": "MA = Load / Effort."},
    {"topic": "Mechanical advantage", "q": "An effort of 50 N lifts a load of "
     "250 N using a machine. The mechanical advantage is:",
     "options": ["5", "0.2", "300", "200"], "correct": 0,
     "why": "MA = Load / Effort = 250 / 50 = 5."},
    {"topic": "Efficiency", "q": "The efficiency of a machine is the ratio of:",
     "options": ["effort to load", "useful work output to work input",
                 "load-arm to effort-arm", "VR to MA"], "correct": 1,
     "why": "Efficiency = work output / work input (x 100 for a percentage)."},
    {"topic": "Ideal machine", "q": "An ideal machine is one whose efficiency "
     "is:",
     "options": ["50%", "less than 100%", "exactly 100%", "more than 100%"],
     "correct": 2,
     "why": "An ideal machine has no friction or weight in its parts, so no "
            "work is wasted and its efficiency is 100%."},
    {"topic": "Lever", "q": "The fixed point about which a lever turns is the:",
     "options": ["load", "effort", "fulcrum", "arm"], "correct": 2,
     "why": "The fixed turning point of a lever is the fulcrum."},
    {"topic": "Principle of a lever", "q": "On a lever a load of 60 N acts "
     "10 cm from the fulcrum and the effort-arm is 30 cm. The ideal effort "
     "is:",
     "options": ["20 N", "180 N", "6 N", "600 N"], "correct": 0,
     "why": "Load x load-arm = Effort x effort-arm: 60 x 10 = E x 30, so "
            "E = 20 N."},
]

SM_HW_S31 = [
    {"topic": "Pulley", "q": "A pulley is a wheel with a grooved rim over "
     "which passes a:",
     "options": ["chain only", "rope or string", "metal rod", "wooden plank"],
     "correct": 1,
     "why": "A pulley is a grooved wheel that turns as a rope or string runs "
            "over its rim."},
    {"topic": "Pulley", "q": "The ideal mechanical advantage of a single fixed "
     "pulley is:",
     "options": ["2", "1", "0.5", "4"], "correct": 1,
     "why": "A single fixed pulley only changes the direction of the effort, "
            "so its ideal MA is 1."},
    {"topic": "Pulley", "q": "A single fixed pulley is useful because it:",
     "options": ["doubles the effort", "changes the direction of the effort",
                 "creates energy", "removes the load's weight"], "correct": 1,
     "why": "It lets you pull down to raise a load up — a more convenient "
            "direction — without changing the force needed."},
    {"topic": "Pulley", "q": "The ideal mechanical advantage of a single "
     "movable pulley is:",
     "options": ["1", "2", "0.5", "3"], "correct": 1,
     "why": "The load is supported by two rope segments, so the effort is half "
            "the load and the ideal MA is 2."},
    {"topic": "Wheel and axle", "q": "Which of these works as a wheel and "
     "axle?",
     "options": ["a see-saw", "a steering wheel", "a knife", "a ramp"],
     "correct": 1,
     "why": "A steering wheel (large wheel) turns a small axle, so it is a "
            "wheel and axle."},
    {"topic": "Wheel and axle", "q": "In a wheel and axle, the mechanical "
     "advantage equals:",
     "options": ["radius of axle / radius of wheel",
                 "radius of wheel / radius of axle", "length / height",
                 "load x effort"], "correct": 1,
     "why": "MA = radius of wheel / radius of axle (R / r)."},
    {"topic": "Inclined plane", "q": "A plank 5 m long is used to raise a load "
     "to a height of 1 m. The ideal MA of this inclined plane is:",
     "options": ["5", "6", "0.2", "4"], "correct": 0,
     "why": "MA = length / height = 5 / 1 = 5."},
    {"topic": "Wedge", "q": "Which of the following is an example of a wedge?",
     "options": ["a steering wheel", "an axe", "a flagpole pulley",
                 "a see-saw"], "correct": 1,
     "why": "An axe blade is a wedge — two inclined planes joined together — "
            "used to split wood."},
    {"topic": "Screw", "q": "The spiral thread of a screw is an example of:",
     "options": ["a lever", "an inclined plane wrapped around a cylinder",
                 "a pulley", "a wheel and axle"], "correct": 1,
     "why": "A screw is an inclined plane wound around a cylinder."},
    {"topic": "Care of machines", "q": "To keep a machine working efficiently "
     "we should:",
     "options": ["never clean it", "oil its moving parts regularly",
                 "let it rust", "increase the friction"], "correct": 1,
     "why": "Regular oiling reduces friction and prevents rust, keeping "
            "efficiency high."},
]

SM_HW_WORKOUT = [
    {"topic": "Work", "q": "A porter carrying a box on his head walks across a "
     "flat platform. The work he does against gravity is:",
     "options": ["maximum", "zero", "negative", "equal to the box's weight"],
     "correct": 1,
     "why": "The supporting force is vertical but the motion is horizontal, so "
            "the work done against gravity is zero."},
    {"topic": "Units", "q": "Which of these is NOT a unit of energy?",
     "options": ["joule", "watt", "erg", "newton metre"], "correct": 1,
     "why": "The watt is the unit of power, not energy."},
    {"topic": "Mechanical advantage", "q": "A machine lifts a 720 N load with "
     "a 180 N effort. Its mechanical advantage is:",
     "options": ["4", "0.25", "900", "540"], "correct": 0,
     "why": "MA = Load / Effort = 720 / 180 = 4."},
    {"topic": "Efficiency", "q": "A machine has MA = 3 and VR = 4. Its "
     "efficiency is:",
     "options": ["75%", "133%", "12%", "7%"], "correct": 0,
     "why": "Efficiency = MA / VR x 100 = 3/4 x 100 = 75%."},
    {"topic": "Levers", "q": "Which of these is a first-order lever?",
     "options": ["a wheelbarrow", "a crowbar lifting a stone",
                 "sugar tongs", "a nutcracker"], "correct": 1,
     "why": "In a crowbar the fulcrum lies between the effort and the load, so "
            "it is a first-order lever."},
    {"topic": "Levers", "q": "A wheelbarrow is a second-order lever, so its "
     "mechanical advantage is always:",
     "options": ["less than 1", "equal to 1", "greater than 1", "zero"],
     "correct": 2,
     "why": "The load lies between the fulcrum and effort, so the effort-arm "
            "is longer and MA > 1."},
    {"topic": "Levers", "q": "Which of these is a third-order lever?",
     "options": ["a see-saw", "a pair of scissors", "a fishing rod",
                 "a bottle opener"], "correct": 2,
     "why": "In a fishing rod the effort (hand) acts between the fulcrum and "
            "the load (fish), so it is a third-order lever."},
    {"topic": "Pulley", "q": "The ideal mechanical advantage of a single "
     "movable pulley is:",
     "options": ["1", "2", "0.5", "4"], "correct": 1,
     "why": "The effort is half the load, so the ideal MA is 2."},
    {"topic": "Inclined plane", "q": "A 600 N drum is rolled up a 3 m plank to "
     "a height of 1 m. The ideal effort needed is:",
     "options": ["200 N", "1800 N", "600 N", "100 N"], "correct": 0,
     "why": "MA = length/height = 3, so ideal effort = Load / MA = "
            "600 / 3 = 200 N."},
    {"topic": "Wedge", "q": "A nail being driven into wood and an axe "
     "splitting a log both act as:",
     "options": ["levers", "wedges", "pulleys", "a wheel and axle"],
     "correct": 1,
     "why": "Both are wedges — pointed/sloping surfaces that force materials "
            "apart."},
]


# ===========================================================================
# LIGHT  (S52 + S53)
# ===========================================================================
LT_WORKOUT_MCQ = [
    {"topic": "Light", "q": "Light is a form of energy that:",
     "options": ["produces sound", "enables us to see objects",
                 "always heats objects", "can be stored in a box"],
     "correct": 1,
     "why": "Light is the form of energy that produces the sensation of sight "
            "and lets us see things."},
    {"topic": "Luminous bodies", "q": "Which of the following is a luminous "
     "body?",
     "options": ["the Moon", "a burning candle", "a mirror", "a white wall"],
     "correct": 1,
     "why": "A burning candle gives out its own light, so it is luminous. The "
            "others are seen only by reflected light."},
    {"topic": "Non-luminous bodies", "q": "The Moon is a non-luminous body "
     "because it:",
     "options": ["produces no heat", "shines only by reflecting sunlight",
                 "is very far away", "is made of rock"], "correct": 1,
     "why": "The Moon does not make its own light; we see it only because it "
            "reflects sunlight."},
    {"topic": "Transparent", "q": "An object through which you can see clearly "
     "is described as:",
     "options": ["opaque", "translucent", "transparent", "luminous"],
     "correct": 2,
     "why": "A transparent object lets almost all light pass through, so we "
            "can see clearly through it."},
    {"topic": "Translucent", "q": "Frosted (ground) glass is an example of a "
     "____ material.",
     "options": ["transparent", "translucent", "opaque", "luminous"],
     "correct": 1,
     "why": "Frosted glass lets only part of the light pass and scatters it, "
            "so we cannot see clearly through it — it is translucent."},
    {"topic": "Opaque", "q": "Which of these is opaque?",
     "options": ["clear glass", "pure water", "a wooden door", "clean air"],
     "correct": 2,
     "why": "A wooden door does not allow any light to pass through it, so it "
            "is opaque."},
    {"topic": "Beam", "q": "A bunch of light rays travelling together is "
     "called a:",
     "options": ["medium", "beam", "shadow", "spectrum"], "correct": 1,
     "why": "A group of light rays is a beam; a single straight path of light "
            "is a ray."},
    {"topic": "Beam", "q": "The light from a torch spreads out as it travels "
     "away. This is a ____ beam.",
     "options": ["parallel", "convergent", "divergent", "circular"],
     "correct": 2,
     "why": "Rays that spread out from a point form a divergent beam."},
    {"topic": "Rectilinear propagation", "q": "Light travels from one point to "
     "another along:",
     "options": ["a curved path", "a straight line", "a zig-zag path",
                 "any path"], "correct": 1,
     "why": "Light travels in straight lines — this is called rectilinear "
            "propagation."},
    {"topic": "Rectilinear propagation", "q": "The formation of sharp shadows "
     "is evidence that light travels:",
     "options": ["in straight lines", "in circles", "faster in glass",
                 "as sound"], "correct": 0,
     "why": "Sharp shadows form because light cannot bend round the object — "
            "it travels in straight lines."},
    {"topic": "Pinhole camera", "q": "The image formed by a pinhole camera "
     "is:",
     "options": ["virtual and erect", "real and inverted",
                 "virtual and inverted", "real and erect"], "correct": 1,
     "why": "Straight-line rays cross at the pinhole, so the image on the "
            "screen is real and upside-down (inverted)."},
    {"topic": "Pinhole camera", "q": "A pinhole camera forms an image because "
     "light:",
     "options": ["bends at the hole", "travels in straight lines through the "
                 "hole", "is reflected by the hole", "is absorbed by the "
                 "screen"], "correct": 1,
     "why": "Rays travel straight through the tiny hole; rays from the top of "
            "the object reach the bottom of the screen and vice versa."},
    {"topic": "Pinhole camera", "q": "If a pinhole camera is made longer (the "
     "screen is moved further from the hole), the image becomes:",
     "options": ["smaller", "larger", "erect", "coloured"], "correct": 1,
     "why": "A longer camera lets the rays spread more before reaching the "
            "screen, so the image is larger."},
    {"topic": "Shadow", "q": "To form a shadow you need a source of light, a "
     "screen and:",
     "options": ["a mirror", "an opaque object", "a lens", "water"],
     "correct": 1,
     "why": "A shadow is the dark region where an opaque object blocks the "
            "light."},
    {"topic": "Shadow", "q": "An extended source of light forms a shadow with "
     "a fully dark central region called the:",
     "options": ["penumbra", "umbra", "corona", "eclipse"], "correct": 1,
     "why": "The completely dark central part of a shadow is the umbra; the "
            "lighter border is the penumbra."},
    {"topic": "Shadow", "q": "A very small (point) source of light produces a "
     "shadow that is:",
     "options": ["only penumbra", "fully sharp, with only an umbra",
                 "coloured", "always larger than the object"], "correct": 1,
     "why": "A point source casts a sharp shadow consisting only of the "
            "umbra, with no penumbra."},
    {"topic": "Eclipse", "q": "A solar eclipse occurs when:",
     "options": ["the Earth comes between the Sun and the Moon",
                 "the Moon comes between the Sun and the Earth",
                 "the Sun comes between the Earth and the Moon",
                 "clouds cover the Sun"], "correct": 1,
     "why": "In a solar eclipse the Moon lies between the Sun and the Earth, "
            "casting its shadow on the Earth."},
    {"topic": "Eclipse", "q": "A solar eclipse can occur only on a:",
     "options": ["full moon day", "new moon day", "half moon day", "any day"],
     "correct": 1,
     "why": "Only on a new moon day is the Moon between the Sun and the Earth, "
            "so a solar eclipse can happen."},
    {"topic": "Eclipse", "q": "During a lunar eclipse, the shadow that falls "
     "on the Moon is that of the:",
     "options": ["Sun", "Earth", "clouds", "another planet"], "correct": 1,
     "why": "In a lunar eclipse the Earth is between the Sun and the Moon, so "
            "the Earth's shadow falls on the Moon."},
    {"topic": "Eclipse", "q": "A lunar eclipse occurs on a ____ day, when the "
     "Earth lies between the Sun and the Moon.",
     "options": ["new moon", "full moon", "half moon", "cloudy"], "correct": 1,
     "why": "A lunar eclipse happens on a full moon day, when the Earth comes "
            "between the Sun and the Moon."},
]

LT_WORKOUT_SUBJ = [
    {"topic": "Luminous & non-luminous", "marks": 3,
     "q": "What is meant by a luminous body and a non-luminous body? Give one "
          "example of each and explain why we are able to see non-luminous "
          "bodies.",
     "answer": [
        "Luminous body: one that gives out (emits) its own light, e.g. the "
        "Sun, a candle flame or an electric bulb.",
        "Non-luminous body: one that does not give out its own light, e.g. the "
        "Moon, a book or a table.",
        "We see non-luminous bodies because they reflect into our eyes the "
        "light falling on them from a luminous source."]},
    {"topic": "Transparent/translucent/opaque", "marks": 3,
     "q": "Distinguish between transparent, translucent and opaque objects, "
          "giving one example of each.",
     "answer": [
        "Transparent: allows almost all light to pass and we can see clearly "
        "through it, e.g. clear glass or water.",
        "Translucent: allows only part of the light to pass, so we cannot see "
        "clearly through it, e.g. frosted glass or tracing paper.",
        "Opaque: does not allow any light to pass through it, e.g. wood, metal "
        "or stone."]},
    {"topic": "Rectilinear propagation", "marks": 4,
     "q": "What is rectilinear propagation of light? Describe a simple "
          "observation or experiment that proves it.",
     "answer": [
        "Rectilinear propagation means that light travels in a straight line.",
        "Proof: place three cardboards with pinholes in a straight line in "
        "front of a candle; light reaches the eye through all three holes.",
        "If the middle card is shifted sideways, the holes no longer line up "
        "and the light is cut off — showing light travels in straight lines.",
        "Everyday proof: sharp shadows and a straight beam of sunlight through "
        "a small hole also show rectilinear propagation."]},
    {"topic": "Pinhole camera", "marks": 4,
     "q": "Describe a pinhole camera. State three characteristics of the image "
          "it forms and explain why the image is inverted.",
     "answer": [
        "A pinhole camera is a closed box with a tiny hole on one side and a "
        "tracing-paper screen on the opposite side.",
        "The image is (i) real, (ii) inverted (upside-down) and (iii) smaller "
        "(diminished) than the object.",
        "It is inverted because light travels in straight lines: rays from the "
        "top of the object pass through the hole to the bottom of the screen, "
        "and rays from the bottom reach the top."]},
    {"topic": "Eclipses", "marks": 4,
     "q": "Differentiate between a solar eclipse and a lunar eclipse using the "
          "positions of the Sun, Earth and Moon, and state on which day (new "
          "moon / full moon) each occurs.",
     "answer": [
        "Solar eclipse: the Moon comes between the Sun and the Earth and the "
        "Moon's shadow falls on the Earth; it occurs on a new moon day.",
        "Lunar eclipse: the Earth comes between the Sun and the Moon and the "
        "Earth's shadow falls on the Moon; it occurs on a full moon day.",
        "Both happen because light travels in straight lines and is blocked by "
        "an opaque body (the Moon or the Earth)."]},
]

LT_HW_S52 = [
    {"topic": "Light", "q": "Light is a form of:",
     "options": ["matter", "energy", "force", "sound"], "correct": 1,
     "why": "Light is a form of energy that lets us see."},
    {"topic": "Luminous bodies", "q": "Which of these gives out its own "
     "light?",
     "options": ["the Moon", "a mirror", "the Sun", "a book"], "correct": 2,
     "why": "The Sun produces its own light, so it is a luminous body."},
    {"topic": "Non-luminous bodies", "q": "A body that does not give out its "
     "own light is called:",
     "options": ["luminous", "non-luminous", "transparent", "opaque"],
     "correct": 1,
     "why": "Bodies that do not emit their own light are non-luminous."},
    {"topic": "Reflection of light", "q": "We are able to see a book because "
     "it:",
     "options": ["is luminous", "reflects light into our eyes",
                 "produces its own light", "is transparent"], "correct": 1,
     "why": "A book is non-luminous; we see it by the light it reflects into "
            "our eyes."},
    {"topic": "Transparent", "q": "Clear glass and water are examples of ____ "
     "materials.",
     "options": ["opaque", "translucent", "transparent", "luminous"],
     "correct": 2,
     "why": "They let almost all light pass, so we can see clearly through "
            "them — transparent."},
    {"topic": "Opaque", "q": "Through which of these can light NOT pass at "
     "all?",
     "options": ["clear glass", "a metal sheet", "water", "air"], "correct": 1,
     "why": "A metal sheet is opaque — it stops light completely."},
    {"topic": "Translucent", "q": "Oiled or tracing paper, through which light "
     "passes only partly, is:",
     "options": ["transparent", "translucent", "opaque", "luminous"],
     "correct": 1,
     "why": "It lets only some light through and blurs the view — "
            "translucent."},
    {"topic": "Ray", "q": "The straight-line path along which light travels is "
     "called a:",
     "options": ["beam", "ray", "shadow", "medium"], "correct": 1,
     "why": "A single straight path of light is a ray; many rays make a beam."},
    {"topic": "Rectilinear propagation", "q": "Light coming from the Sun "
     "reaches us travelling in:",
     "options": ["curved paths", "straight lines", "zig-zag paths", "circles"],
     "correct": 1,
     "why": "Light travels in straight lines (rectilinear propagation)."},
    {"topic": "Beam", "q": "Rays of light that come together at a point form a "
     "____ beam.",
     "options": ["parallel", "divergent", "convergent", "random"],
     "correct": 2,
     "why": "Rays meeting at a point form a convergent beam."},
]

LT_HW_S53 = [
    {"topic": "Pinhole camera", "q": "The image formed by a pinhole camera "
     "is:",
     "options": ["erect and virtual", "inverted and real", "erect and real",
                 "inverted and virtual"], "correct": 1,
     "why": "The pinhole image is real (formed on a screen) and inverted."},
    {"topic": "Pinhole camera", "q": "A pinhole camera works on the principle "
     "that light:",
     "options": ["bends round corners", "travels in straight lines",
                 "is reflected by air", "travels as sound"], "correct": 1,
     "why": "Straight-line travel of light through the hole forms the inverted "
            "image."},
    {"topic": "Shadow", "q": "A shadow is formed behind an object that is:",
     "options": ["transparent", "translucent", "opaque", "luminous"],
     "correct": 2,
     "why": "Only an opaque object blocks light to form a shadow."},
    {"topic": "Shadow", "q": "Which one is NOT needed to form a shadow?",
     "options": ["a source of light", "an opaque object", "a screen",
                 "a mirror"], "correct": 3,
     "why": "A shadow needs a light source, an opaque object and a screen — "
            "but not a mirror."},
    {"topic": "Shadow", "q": "The completely dark part of a shadow is called "
     "the:",
     "options": ["penumbra", "umbra", "corona", "ray"], "correct": 1,
     "why": "The fully dark central region of a shadow is the umbra."},
    {"topic": "Shadow", "q": "A shadow having both a dark umbra and a lighter "
     "penumbra is formed by:",
     "options": ["a point source", "an extended source", "no source",
                 "a transparent object"], "correct": 1,
     "why": "An extended (large) source produces both an umbra and a "
            "penumbra."},
    {"topic": "Solar eclipse", "q": "During a solar eclipse, the body that "
     "comes in the middle is the:",
     "options": ["Earth", "Moon", "Sun", "a star"], "correct": 1,
     "why": "In a solar eclipse the Moon lies between the Sun and the Earth."},
    {"topic": "Solar eclipse", "q": "A solar eclipse happens on a:",
     "options": ["full moon day", "new moon day", "half moon day", "any day"],
     "correct": 1,
     "why": "A solar eclipse can occur only on a new moon day."},
    {"topic": "Lunar eclipse", "q": "During a lunar eclipse the Moon is "
     "darkened by the shadow of the:",
     "options": ["Sun", "Earth", "clouds", "Moon itself"], "correct": 1,
     "why": "In a lunar eclipse the Earth's shadow falls on the Moon."},
    {"topic": "Lunar eclipse", "q": "A lunar eclipse occurs when ____ lies "
     "between the Sun and the Moon.",
     "options": ["the Earth", "the Moon", "a planet", "a comet"], "correct": 0,
     "why": "A lunar eclipse occurs when the Earth is between the Sun and the "
            "Moon."},
]

LT_HW_WORKOUT = [
    {"topic": "Luminous bodies", "q": "Which pair are both luminous bodies?",
     "options": ["Sun and Moon", "candle flame and electric bulb",
                 "Moon and mirror", "book and table"], "correct": 1,
     "why": "A candle flame and an electric bulb both give out their own "
            "light."},
    {"topic": "Translucent", "q": "We cannot see clearly through a translucent "
     "object because it:",
     "options": ["lets all light pass", "lets only part of the light pass",
                 "lets no light pass", "produces its own light"], "correct": 1,
     "why": "A translucent object passes only some of the light and scatters "
            "it, blurring the view."},
    {"topic": "Beam", "q": "A bundle of light rays travelling together is "
     "called a:",
     "options": ["medium", "beam", "shadow", "pinhole"], "correct": 1,
     "why": "Many rays together form a beam."},
    {"topic": "Rectilinear propagation", "q": "The clearest everyday proof "
     "that light travels in straight lines is the formation of:",
     "options": ["rainbows", "sharp shadows", "echoes", "heat"], "correct": 1,
     "why": "Sharp shadows form because light cannot bend round an opaque "
            "object."},
    {"topic": "Pinhole camera", "q": "The image in a pinhole camera is "
     "diminished and inverted because light:",
     "options": ["spreads out at the hole", "travels in straight lines through "
                 "the hole", "is reflected at the hole", "changes colour"],
     "correct": 1,
     "why": "Straight rays cross at the hole, so top and bottom are swapped "
            "and the image is small and inverted."},
    {"topic": "Pinhole camera", "q": "If the object is brought closer to a "
     "pinhole camera, the image becomes:",
     "options": ["smaller", "larger", "erect", "coloured"], "correct": 1,
     "why": "A nearer object subtends a larger angle at the hole, so its image "
            "is larger."},
    {"topic": "Shadow", "q": "An extended source forms a shadow having:",
     "options": ["only umbra", "only penumbra", "both umbra and penumbra",
                 "no shadow"], "correct": 2,
     "why": "A large source gives a dark umbra surrounded by a lighter "
            "penumbra."},
    {"topic": "Solar eclipse", "q": "On a new moon day, when the Moon lies "
     "between the Sun and the Earth, we may see a:",
     "options": ["lunar eclipse", "solar eclipse", "full moon", "rainbow"],
     "correct": 1,
     "why": "The Moon between the Sun and Earth causes a solar eclipse."},
    {"topic": "Lunar eclipse", "q": "During a lunar eclipse the order of the "
     "three bodies in a line is:",
     "options": ["Sun - Moon - Earth", "Sun - Earth - Moon",
                 "Earth - Sun - Moon", "Moon - Sun - Earth"], "correct": 1,
     "why": "In a lunar eclipse the Earth is in the middle: Sun - Earth - "
            "Moon."},
    {"topic": "Non-luminous bodies", "q": "Which of the following is a "
     "non-luminous body that we see only by reflected light?",
     "options": ["the Sun", "a glowing filament", "the planet Venus",
                 "a candle flame"], "correct": 2,
     "why": "A planet such as Venus gives out no light of its own; we see it "
            "by reflected sunlight."},
]


# ===========================================================================
# MAGNETISM  (S69 + S70)
# ===========================================================================
MG_WORKOUT_MCQ = [
    {"topic": "Natural magnets", "q": "A naturally occurring magnet is an ore "
     "of iron called:",
     "options": ["bauxite", "magnetite (lodestone)", "haematite", "graphite"],
     "correct": 1,
     "why": "Magnetite, also called lodestone, is a natural magnet and an ore "
            "of iron."},
    {"topic": "Discovery of magnets", "q": "Lodestone was first noticed "
     "because it could:",
     "options": ["glow in the dark", "attract pieces of iron",
                 "float on water", "produce electricity"], "correct": 1,
     "why": "The property of lodestone that was first observed was its "
            "attraction of small pieces of iron."},
    {"topic": "Artificial magnets", "q": "Compared with natural magnets, "
     "artificial magnets are:",
     "options": ["weaker and irregular", "stronger and of any desired shape",
                 "unable to attract iron", "always found in nature"],
     "correct": 1,
     "why": "Man-made (artificial) magnets can be made stronger and in any "
            "required shape and size."},
    {"topic": "Magnetic substances", "q": "Which of these is a magnetic "
     "substance?",
     "options": ["copper", "nickel", "brass", "plastic"], "correct": 1,
     "why": "Nickel (like iron, cobalt and steel) is attracted by a magnet, so "
            "it is magnetic."},
    {"topic": "Non-magnetic substances", "q": "Which of these is NOT attracted "
     "by a magnet?",
     "options": ["iron", "cobalt", "aluminium", "steel"], "correct": 2,
     "why": "Aluminium is a non-magnetic substance and is not attracted by a "
            "magnet."},
    {"topic": "Properties of a magnet", "q": "The attracting power of a bar "
     "magnet is greatest:",
     "options": ["at its centre", "at its two poles",
                 "all along its length equally", "only at the north pole"],
     "correct": 1,
     "why": "A magnet's attractive power is concentrated at its poles and is "
            "almost nil at its centre."},
    {"topic": "Directive property", "q": "When a bar magnet is freely "
     "suspended, it always comes to rest pointing:",
     "options": ["east-west", "north-south", "randomly", "straight up"],
     "correct": 1,
     "why": "A freely suspended magnet sets itself in the north-south "
            "direction — its directive property."},
    {"topic": "Law of magnetism", "q": "When the north poles of two magnets "
     "are brought close together, they:",
     "options": ["attract", "repel", "do nothing", "stick together"],
     "correct": 1,
     "why": "Like poles repel each other, so two north poles push apart."},
    {"topic": "Law of magnetism", "q": "Unlike poles of two magnets always:",
     "options": ["repel", "attract", "stay neutral", "lose magnetism"],
     "correct": 1,
     "why": "Unlike poles (a north and a south) attract each other."},
    {"topic": "Properties of a magnet", "q": "If a bar magnet is broken into "
     "two pieces, each piece:",
     "options": ["has only a north pole", "has only a south pole",
                 "is a complete magnet with both N and S poles",
                 "loses all its magnetism"], "correct": 2,
     "why": "Magnetic poles always exist in pairs; each broken piece becomes a "
            "complete magnet with its own north and south poles."},
    {"topic": "Magnetic field", "q": "The region around a magnet in which its "
     "influence (force) can be detected is called its:",
     "options": ["magnetic pole", "magnetic field", "magnetic axis",
                 "neutral point"], "correct": 1,
     "why": "The space around a magnet where its force acts is the magnetic "
            "field."},
    {"topic": "Magnetic field", "q": "Outside a bar magnet, magnetic field "
     "lines are taken to run from:",
     "options": ["south pole to north pole", "north pole to south pole",
                 "pole to centre", "one face to the other"], "correct": 1,
     "why": "By convention, field lines outside a magnet go from the north "
            "pole to the south pole."},
    {"topic": "Care and storage", "q": "Bar magnets are stored in pairs with "
     "unlike poles together and soft-iron pieces across their ends. These "
     "soft-iron pieces are called:",
     "options": ["poles", "keepers", "cores", "coils"], "correct": 1,
     "why": "The soft-iron pieces placed across the poles of stored magnets "
            "are called keepers; they preserve the magnetism."},
    {"topic": "Earth's magnetism", "q": "A freely suspended magnet points "
     "north-south because:",
     "options": ["the Sun pulls it", "the Earth itself behaves like a huge "
                 "magnet", "the wind turns it", "of gravity"], "correct": 1,
     "why": "The Earth acts like a giant bar magnet, so a suspended magnet "
            "aligns with the Earth's field, north-south."},
    {"topic": "Making a magnet", "q": "In the single-touch method, a steel bar "
     "is stroked with one pole of a magnet:",
     "options": ["back and forth many times", "again and again in the same "
                 "direction", "only once in the middle", "while it is hot"],
     "correct": 1,
     "why": "In single-touch the bar is stroked repeatedly in the same "
            "direction with one pole, lifting it well clear between strokes."},
    {"topic": "Electromagnet", "q": "An electromagnet is made by winding a "
     "current-carrying coil around a core of:",
     "options": ["soft iron", "steel", "copper", "wood"], "correct": 0,
     "why": "A soft-iron core is used because it becomes a strong magnet while "
            "current flows and loses its magnetism quickly when it stops."},
    {"topic": "Electromagnet", "q": "An electromagnet is magnetic:",
     "options": ["for ever", "only while current flows through the coil",
                 "only when heated", "only in sunlight"], "correct": 1,
     "why": "An electromagnet is a temporary magnet — it is magnetic only "
            "while current flows and loses its magnetism when switched off."},
    {"topic": "Electromagnet", "q": "The strength of an electromagnet can be "
     "increased by:",
     "options": ["using fewer turns of wire", "decreasing the current",
                 "increasing the number of turns and the current",
                 "using a wooden core"], "correct": 2,
     "why": "More turns of wire and a larger current both make the "
            "electromagnet stronger (a soft-iron core helps too)."},
    {"topic": "Uses of electromagnets", "q": "A crane in a scrapyard lifts and "
     "then drops iron scrap using:",
     "options": ["a permanent steel magnet", "an electromagnet",
                 "a natural lodestone", "a horseshoe magnet"], "correct": 1,
     "why": "An electromagnet can be switched on to lift the iron and off to "
            "drop it — a permanent magnet could not release the load."},
    {"topic": "Demagnetisation", "q": "Which of these will make a magnet LOSE "
     "its magnetism?",
     "options": ["storing it with keepers", "strongly heating or hammering "
                 "it", "keeping it cool and dry", "handling it gently"],
     "correct": 1,
     "why": "Strong heating, hammering or rough handling (and an AC coil) "
            "destroy magnetism; careful storage preserves it."},
]

MG_WORKOUT_SUBJ = [
    {"topic": "Natural & artificial magnets", "marks": 3,
     "q": "What is a natural magnet and an artificial magnet? Give one example "
          "of each and state two ways in which an artificial magnet is better "
          "than a natural one.",
     "answer": [
        "Natural magnet: a magnet found in nature, an ore of iron called "
        "magnetite or lodestone.",
        "Artificial magnet: a man-made magnet such as a bar magnet or "
        "horseshoe magnet, made from steel or iron.",
        "Artificial magnets are stronger and can be made in any desired shape, "
        "size and strength, while natural magnets are weak and irregular."]},
    {"topic": "Properties of a magnet", "marks": 4,
     "q": "State any four properties of a magnet.",
     "answer": [
        "A magnet attracts magnetic materials (iron, cobalt, nickel), most "
        "strongly at its poles.",
        "A freely suspended magnet always sets itself north-south (directive "
        "property).",
        "Like poles repel and unlike poles attract.",
        "Poles always exist in pairs — a single isolated pole cannot be "
        "obtained; breaking a magnet gives two complete magnets."]},
    {"topic": "Magnetic field", "marks": 3,
     "q": "What is a magnetic field? Describe the magnetic field lines of a "
          "bar magnet and state their direction outside the magnet.",
     "answer": [
        "A magnetic field is the region around a magnet where its magnetic "
        "force can be experienced.",
        "It is represented by magnetic field lines (lines of force), which are "
        "most crowded near the poles and never cross one another.",
        "Outside the magnet the field lines run from the north pole to the "
        "south pole."]},
    {"topic": "Electromagnet", "marks": 4,
     "q": "What is an electromagnet? State two ways to increase its strength "
          "and give two uses of electromagnets.",
     "answer": [
        "An electromagnet is a temporary magnet made by passing an electric "
        "current through an insulated coil wound on a soft-iron core; it is "
        "magnetic only while the current flows.",
        "Its strength is increased by (i) increasing the number of turns of "
        "the coil and (ii) increasing the current (a soft-iron core also "
        "helps).",
        "Uses: in electric bells and cranes for lifting iron/scrap; also in "
        "telephones, electric motors and for separating magnetic materials."]},
    {"topic": "Making & destroying magnetism", "marks": 3,
     "q": "State two ways of making a steel bar into a magnet and two ways by "
          "which a magnet can lose its magnetism.",
     "answer": [
        "Making a magnet: (i) the single-touch method — stroking the steel bar "
        "repeatedly in the same direction with one pole of a magnet.",
        "(ii) the electrical method — passing an electric current through a "
        "coil wound around the bar.",
        "Losing magnetism: strong heating and rough handling (hammering or "
        "dropping); also placing it in a coil carrying alternating current or "
        "storing it carelessly."]},
]

MG_HW_S69 = [
    {"topic": "Natural magnets", "q": "A natural magnet is also known as:",
     "options": ["magnetite or lodestone", "graphite", "haematite",
                 "bauxite"], "correct": 0,
     "why": "The natural magnet is the iron ore magnetite, also called "
            "lodestone."},
    {"topic": "Discovery of magnets", "q": "Magnets were first discovered "
     "because lodestone could attract:",
     "options": ["wood", "pieces of iron", "water", "air"], "correct": 1,
     "why": "Lodestone was noticed because it attracted small pieces of iron."},
    {"topic": "Magnetic substances", "q": "Which of the following is a "
     "magnetic material?",
     "options": ["plastic", "iron", "rubber", "glass"], "correct": 1,
     "why": "Iron is attracted by a magnet, so it is a magnetic material."},
    {"topic": "Non-magnetic substances", "q": "Which of these is a "
     "non-magnetic substance?",
     "options": ["cobalt", "nickel", "copper", "iron"], "correct": 2,
     "why": "Copper is not attracted by a magnet, so it is non-magnetic."},
    {"topic": "Properties of a magnet", "q": "A magnet attracts iron most "
     "strongly at its:",
     "options": ["centre", "poles", "sides", "top"], "correct": 1,
     "why": "The poles are the regions of strongest attraction in a magnet."},
    {"topic": "Directive property", "q": "A freely suspended bar magnet comes "
     "to rest in the ____ direction.",
     "options": ["east-west", "north-south", "up-down", "slanting"],
     "correct": 1,
     "why": "It sets itself north-south because of its directive property."},
    {"topic": "Law of magnetism", "q": "Two like poles brought near each other "
     "will:",
     "options": ["attract", "repel", "do nothing", "join"], "correct": 1,
     "why": "Like poles always repel each other."},
    {"topic": "Properties of a magnet", "q": "If you break a bar magnet in "
     "half, you get:",
     "options": ["one N pole and one S pole separately",
                 "two complete magnets", "a piece with no magnetism",
                 "a single pole"], "correct": 1,
     "why": "Each half becomes a complete magnet with both a north and a south "
            "pole."},
    {"topic": "Magnetic field", "q": "The space around a magnet where its "
     "force acts is the magnet's:",
     "options": ["pole", "field", "axis", "keeper"], "correct": 1,
     "why": "This region is the magnetic field of the magnet."},
    {"topic": "Earth's magnetism", "q": "A compass needle always sets itself "
     "north-south because the ____ acts like a giant magnet.",
     "options": ["Sun", "Moon", "Earth", "cloud"], "correct": 2,
     "why": "The Earth behaves like a huge bar magnet, aligning the compass "
            "needle north-south."},
]

MG_HW_S70 = [
    {"topic": "Making a magnet", "q": "In the single-touch method, the steel "
     "bar is stroked with the magnet:",
     "options": ["once only", "repeatedly in the same direction",
                 "back and forth", "while hot"], "correct": 1,
     "why": "The bar is stroked again and again in the same direction with one "
            "pole of the magnet."},
    {"topic": "Electromagnet", "q": "An electromagnet has a core made of:",
     "options": ["steel", "soft iron", "copper", "wood"], "correct": 1,
     "why": "A soft-iron core is used because it magnetises and demagnetises "
            "easily."},
    {"topic": "Electromagnet", "q": "An electromagnet behaves as a magnet:",
     "options": ["permanently", "only while current flows", "only when "
                 "heated", "only in the dark"], "correct": 1,
     "why": "It is a temporary magnet, magnetic only while current flows."},
    {"topic": "Electromagnet", "q": "To make an electromagnet stronger you "
     "should:",
     "options": ["reduce the turns", "increase the number of turns",
                 "reduce the current", "use a wooden core"], "correct": 1,
     "why": "More turns of wire (and more current) make the electromagnet "
            "stronger."},
    {"topic": "Uses of electromagnets", "q": "Which device uses an "
     "electromagnet?",
     "options": ["a see-saw", "an electric bell", "a wooden ruler",
                 "a glass mirror"], "correct": 1,
     "why": "An electric bell works using an electromagnet."},
    {"topic": "Permanent magnets", "q": "A permanent magnet is usually made "
     "of:",
     "options": ["soft iron", "steel", "copper", "aluminium"], "correct": 1,
     "why": "Steel retains its magnetism, so it is used for permanent "
            "magnets."},
    {"topic": "Care and storage", "q": "The soft-iron pieces kept across the "
     "ends of stored magnets are called:",
     "options": ["poles", "keepers", "cores", "coils"], "correct": 1,
     "why": "These soft-iron pieces are keepers; they help preserve the "
            "magnetism."},
    {"topic": "Care and storage", "q": "Bar magnets should be stored in pairs "
     "with their ____ poles next to each other.",
     "options": ["like", "unlike", "north", "south"], "correct": 1,
     "why": "Unlike poles are placed together (with keepers) to preserve "
            "magnetism."},
    {"topic": "Demagnetisation", "q": "Which of these will destroy a magnet's "
     "magnetism?",
     "options": ["careful storage", "strong heating and hammering",
                 "using keepers", "keeping it dry"], "correct": 1,
     "why": "Strong heating and hammering disturb the magnetic arrangement and "
            "destroy magnetism."},
    {"topic": "Demagnetisation", "q": "Placing a magnet inside a coil carrying "
     "____ current is a way to demagnetise it.",
     "options": ["direct", "alternating", "no", "weak"], "correct": 1,
     "why": "An alternating (AC) current in a coil repeatedly reverses the "
            "magnetism and destroys it."},
]

MG_HW_WORKOUT = [
    {"topic": "Natural magnets", "q": "The natural magnet magnetite is an ore "
     "of:",
     "options": ["copper", "iron", "aluminium", "lead"], "correct": 1,
     "why": "Magnetite (lodestone) is an ore of iron."},
    {"topic": "Properties of a magnet", "q": "A bar magnet picks up the most "
     "iron filings at its:",
     "options": ["middle", "two ends (poles)", "front face", "back"],
     "correct": 1,
     "why": "Attraction is strongest at the poles, so most filings cling to "
            "the ends."},
    {"topic": "Law of magnetism", "q": "Which statement is correct?",
     "options": ["Like poles attract", "Unlike poles repel",
                 "Like poles repel and unlike poles attract",
                 "All poles attract"], "correct": 2,
     "why": "The law of magnetism: like poles repel, unlike poles attract."},
    {"topic": "Properties of a magnet", "q": "A single isolated north pole:",
     "options": ["can be made by breaking a magnet", "cannot exist on its "
                 "own", "is found in lodestone", "is the same as a keeper"],
     "correct": 1,
     "why": "Poles always occur in pairs, so a single pole cannot be "
            "isolated."},
    {"topic": "Magnetic field", "q": "Outside a bar magnet, the magnetic field "
     "lines go from:",
     "options": ["S to N", "N to S", "pole to centre", "centre to pole"],
     "correct": 1,
     "why": "By convention field lines run from north to south outside the "
            "magnet."},
    {"topic": "Electromagnet", "q": "An electromagnet loses its magnetism "
     "when:",
     "options": ["the current is switched off", "it is painted", "it is "
                 "cooled", "it is stored"], "correct": 0,
     "why": "Being a temporary magnet, it is magnetic only while current "
            "flows."},
    {"topic": "Electromagnet", "q": "The strength of an electromagnet does NOT "
     "depend on:",
     "options": ["the number of turns", "the current", "the colour of the "
                 "wire", "the core material"], "correct": 2,
     "why": "Strength depends on turns, current and core — not on the colour "
            "of the wire."},
    {"topic": "Uses of electromagnets", "q": "A scrapyard crane uses an "
     "electromagnet rather than a permanent magnet because it can:",
     "options": ["never drop the load", "be switched on to lift and off to "
                 "drop the load", "lift only plastic", "work without "
                 "electricity"], "correct": 1,
     "why": "Switching the current off releases the load — a permanent magnet "
            "could not let go."},
    {"topic": "Care and storage", "q": "To preserve their magnetism, bar "
     "magnets are stored with:",
     "options": ["like poles together and no keepers",
                 "unlike poles together and soft-iron keepers",
                 "their poles heated", "them lying on a radiator"],
     "correct": 1,
     "why": "Unlike poles together with soft-iron keepers keeps the magnetism "
            "from leaking away."},
    {"topic": "Demagnetisation", "q": "Which treatment will weaken or destroy "
     "a magnet?",
     "options": ["keeping it with a keeper", "dropping and hammering it "
                 "repeatedly", "storing it in a dry box", "keeping it away "
                 "from heat"], "correct": 1,
     "why": "Repeated dropping and hammering jolts the magnetic arrangement "
            "and destroys the magnetism."},
]


# ===========================================================================
# BUILD
# ===========================================================================
WORKOUTS = [
    dict(file="G06_Simple_Machines_Workout.pptx", chapter="Simple Machines",
         accent=C["teal"], title="Simple Machines — Workout",
         subtitle="Practice covering Simple Machines Lessons 1 & 2",
         syllabus=[
             ("Simple Machines 1", "Work & energy, machines, principle of a "
              "machine, efficiency, ideal & actual machine, functions, "
              "mechanical advantage, levers, principle of a lever, orders of "
              "levers."),
             ("Simple Machines 2", "Pulley & its MA, wheel and axle, inclined "
              "plane, wedge, screw, care of machines.")],
         mcqs=SM_WORKOUT_MCQ, subj=SM_WORKOUT_SUBJ,
         closing="Re-check every numerical you missed and revise the orders of "
                 "levers and the MA of each machine before the test."),
    dict(file="G06_Light_Workout.pptx", chapter="Light",
         accent=C["orange"], title="Light — Workout",
         subtitle="Practice covering Light Lessons 1 & 2",
         syllabus=[
             ("Light 1", "Light, sources of light, luminous & non-luminous "
              "bodies, transparent/translucent/opaque, ray & beam, rectilinear "
              "propagation and its applications."),
             ("Light 2", "Pinhole camera, shadow (umbra & penumbra), solar and "
              "lunar eclipses.")],
         mcqs=LT_WORKOUT_MCQ, subj=LT_WORKOUT_SUBJ,
         closing="Revise why the pinhole image is inverted and the positions "
                 "of the Sun, Earth and Moon in each eclipse."),
    dict(file="G06_Magnetism_Workout.pptx", chapter="Magnetism",
         accent=C["purple"], title="Magnetism — Workout",
         subtitle="Practice covering Magnetism Lessons 1 & 2",
         syllabus=[
             ("Magnetism 1", "Discovery of magnets, natural & artificial "
              "magnets, magnetic & non-magnetic substances, properties of a "
              "magnet, magnetic field, Earth's magnetism."),
             ("Magnetism 2", "Making a magnet, electromagnets and their uses, "
              "care & storage of magnets, demagnetisation.")],
         mcqs=MG_WORKOUT_MCQ, subj=MG_WORKOUT_SUBJ,
         closing="Revise the properties of a magnet and how an electromagnet "
                 "differs from a permanent magnet before the test."),
]

HOMEWORKS = [
    # (file, chapter, lesson, kind, syllabus, mcqs)
    ("G06_S30_Simple_Machines_1_Homework.pdf", "Simple Machines",
     "Lesson 1", "Concept",
     "Work & energy, machines, principle of a machine, efficiency, ideal & "
     "actual machine, functions of a machine, mechanical advantage, levers, "
     "principle of a lever, orders of levers.", SM_HW_S30),
    ("G06_S31_Simple_Machines_2_Homework.pdf", "Simple Machines",
     "Lesson 2", "Concept",
     "Pulley and its mechanical advantage, wheel and axle, inclined plane, "
     "wedge, screw, care of machines.", SM_HW_S31),
    ("G06_Simple_Machines_Workout_Homework.pdf", "Simple Machines",
     "Workout", "Workout",
     "Whole chapter: work & machines, MA, VR & efficiency, levers and their "
     "orders, pulley, wheel and axle, inclined plane, wedge and screw.",
     SM_HW_WORKOUT),
    ("G06_S52_Light_1_Homework.pdf", "Light", "Lesson 1", "Concept",
     "Light, sources of light, luminous & non-luminous bodies, "
     "transparent/translucent/opaque materials, rays & beams, rectilinear "
     "propagation of light.", LT_HW_S52),
    ("G06_S53_Light_2_Homework.pdf", "Light", "Lesson 2", "Concept",
     "Pinhole camera, shadows (umbra and penumbra), solar and lunar eclipses.",
     LT_HW_S53),
    ("G06_Light_Workout_Homework.pdf", "Light", "Workout", "Workout",
     "Whole chapter: sources of light, types of materials, rays & beams, "
     "rectilinear propagation, pinhole camera, shadows and eclipses.",
     LT_HW_WORKOUT),
    ("G06_S69_Magnetism_1_Homework.pdf", "Magnetism", "Lesson 1", "Concept",
     "Discovery of magnets, natural & artificial magnets, magnetic & "
     "non-magnetic substances, properties of a magnet, magnetic field, Earth's "
     "magnetism.", MG_HW_S69),
    ("G06_S70_Magnetism_2_Homework.pdf", "Magnetism", "Lesson 2", "Concept",
     "Making a magnet, electromagnets and their uses, care & storage of "
     "magnets, demagnetisation.", MG_HW_S70),
    ("G06_Magnetism_Workout_Homework.pdf", "Magnetism", "Workout", "Workout",
     "Whole chapter: natural & artificial magnets, magnetic substances, "
     "properties of a magnet, magnetic field, electromagnets and their uses, "
     "care, storage and demagnetisation.", MG_HW_WORKOUT),
]


def _check(name, mcqs, n):
    assert len(mcqs) == n, f"{name}: expected {n} MCQs, got {len(mcqs)}"
    for i, q in enumerate(mcqs, 1):
        assert len(q["options"]) == 4, f"{name} Q{i}: needs 4 options"
        assert 0 <= q["correct"] <= 3, f"{name} Q{i}: bad correct index"


def build():
    print("== Grade 6 Workout decks ==")
    for sd, w in enumerate(WORKOUTS):
        _check(w["file"], w["mcqs"], 20)
        assert len(w["subj"]) == 5, f"{w['file']}: needs 5 subjective"
        mcqs = balance_options(w["mcqs"], seed=100 + sd)
        path = os.path.join(WK_OUT, w["file"])
        b, issues = build_workout(
            path, chapter=w["chapter"], accent=w["accent"], title=w["title"],
            subtitle=w["subtitle"], syllabus=w["syllabus"], mcqs=mcqs,
            subjectives=w["subj"], closing_msg=w["closing"])
        print(f"  {w['file']}: {len(b.prs.slides._sldIdLst)} slides  "
              f"{'OK' if not issues else 'QA ISSUES: ' + str(issues)}")

    print("== Grade 6 Homework PDFs ==")
    for sd, (fname, chapter, lesson, kind, syll, mcqs) in enumerate(HOMEWORKS):
        _check(fname, mcqs, 10)
        mcqs = balance_options(mcqs, seed=200 + sd)
        path = os.path.join(HW_OUT, fname)
        build_homework(path, grade=GRADE, chapter=chapter, lesson=lesson,
                       kind=kind, syllabus_topics=syll, mcqs=mcqs)
        print(f"  {fname}: 10 MCQs")


if __name__ == "__main__":
    build()
