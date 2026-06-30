"""
Grade 7 (ICSE / Selina Concise Physics) assessment bank + builder.

Chapters (from tools/decks.json):
  - Light Energy             : S37 (L1), S38 (L2)
  - Heat                     : S55 (H1), S56 (H2), S57 (H3)
  - Sound                    : S66 (S1), S67 (S2)
  - Electricity & Magnetism  : S76 (1), S77 (2), S78 (3)

One workout (20 MCQ + 5 subjective) per chapter, covering all of that
chapter's concept lessons. One 10-MCQ homework PDF per concept session AND per
workout. Questions are moderate-to-difficult (application / numerical /
reasoning), strictly in syllabus, and deliberately distinct from the
concept-deck quizzes (dedup-checked at build time).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from engine import C
from assessment import build_grade

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
WK_OUT = os.path.join(ROOT, "workouts", "Grade07")
HW_OUT = os.path.join(ROOT, "homework", "Grade07")
CONCEPT_DIR = os.path.join(ROOT, "ppt", "Grade07")
GRADE = "Class 7"


# ===========================================================================
# CHAPTER 1 — LIGHT ENERGY  (S37 + S38)
# ===========================================================================
LE_WK_MCQ = [
    {"topic": "Laws of reflection", "q": "A ray of light is incident on a "
     "plane mirror making an angle of 30° with the mirror surface. The angle "
     "of reflection (measured from the normal) is:",
     "options": ["30°", "60°", "120°", "15°"], "correct": 1,
     "why": "Angle of incidence = 90° − 30° = 60°; by the first law the angle "
            "of reflection equals it, so 60°."},
    {"topic": "Rotation of mirror", "q": "Keeping the incident ray fixed, a "
     "plane mirror is rotated through 10°. The reflected ray turns through:",
     "options": ["5°", "10°", "20°", "40°"], "correct": 2,
     "why": "When a mirror is rotated by an angle, the reflected ray turns "
            "through twice that angle: 2 × 10° = 20°."},
    {"topic": "Two mirrors", "q": "A ray of light reflects off two plane "
     "mirrors fixed at 90° to each other. The final emergent ray is:",
     "options": ["parallel and in the same direction as the incident ray",
                 "parallel but opposite in direction to the incident ray",
                 "perpendicular to the incident ray", "at 45° to it"],
     "correct": 1,
     "why": "Two reflections from mirrors at 90° reverse the ray's direction "
            "(total deviation 180°), so it emerges antiparallel."},
    {"topic": "Image in motion", "q": "An object moves towards a plane mirror "
     "at 2 m/s. The image approaches the object at:",
     "options": ["1 m/s", "2 m/s", "4 m/s", "0"], "correct": 2,
     "why": "The image moves toward the mirror at 2 m/s, so relative to the "
            "object it closes in at 2 + 2 = 4 m/s."},
    {"topic": "Image distance", "q": "A boy stands 1.5 m in front of a plane "
     "mirror. The distance between the boy and his image is:",
     "options": ["1.5 m", "3.0 m", "0.75 m", "6.0 m"], "correct": 1,
     "why": "The image is 1.5 m behind the mirror, so boy-to-image = "
            "1.5 + 1.5 = 3.0 m."},
    {"topic": "Two mirrors", "q": "Two plane mirrors are placed at 60° to each "
     "other. The number of images of an object placed between them is:",
     "options": ["3", "5", "6", "2"], "correct": 1,
     "why": "Number of images = (360/θ) − 1 = (360/60) − 1 = 5."},
    {"topic": "Lateral inversion", "q": "Written normally and held up to a "
     "plane mirror, which word appears unchanged?",
     "options": ["MOM", "AMBULANCE", "BOOK", "TOMATO"], "correct": 0,
     "why": "MOM is a palindrome of vertically symmetric letters, so its "
            "left–right reversed mirror image looks identical."},
    {"topic": "Virtual image", "q": "Which statement about a plane-mirror image "
     "is correct?",
     "options": ["It is real and can be caught on a screen",
                 "It is virtual and formed by rays actually meeting",
                 "It is virtual and formed where reflected rays appear to meet "
                 "behind the mirror", "It is always smaller than the object"],
     "correct": 2,
     "why": "Reflected rays diverge and only appear to meet behind the mirror, "
            "so the image is virtual."},
    {"topic": "Diffuse reflection", "q": "You can see your face in polished "
     "steel but not in a sheet of paper, though both reflect light, because "
     "paper gives:",
     "options": ["no reflection", "regular reflection",
                 "diffuse (irregular) reflection", "total absorption"],
     "correct": 2,
     "why": "A rough surface scatters parallel rays in all directions "
            "(diffuse reflection), so no clear image forms."},
    {"topic": "Periscope", "q": "In a simple periscope, each plane mirror is "
     "fixed at an angle of ___ to the path of light.",
     "options": ["30°", "45°", "60°", "90°"], "correct": 1,
     "why": "Each mirror at 45° turns the light through 90°, so two of them "
            "let you see over an obstacle."},
    {"topic": "Speed of light", "q": "Light takes about 8 minutes to reach "
     "Earth from the Sun. Taking c = 3×10⁸ m/s, the Sun–Earth distance is "
     "about:",
     "options": ["1.44×10¹¹ m", "3×10⁸ m", "2.4×10⁹ m", "1.8×10¹⁰ m"],
     "correct": 0,
     "why": "Distance = speed × time = 3×10⁸ × (8 × 60) = 1.44×10¹¹ m."},
    {"topic": "Colours of light", "q": "When red and green lights of equal "
     "brightness overlap on a white screen, the colour seen is:",
     "options": ["Yellow", "Cyan", "Magenta", "White"], "correct": 0,
     "why": "Red + Green = Yellow, a secondary colour of light."},
    {"topic": "Secondary colours", "q": "Magenta light is produced by adding:",
     "options": ["red and green", "green and blue", "red and blue",
                 "blue and yellow"], "correct": 2,
     "why": "Magenta = Red + Blue."},
    {"topic": "White light", "q": "Red, green and blue spotlights overlap on a "
     "white screen. The overlap region appears:",
     "options": ["black", "white", "grey", "yellow"], "correct": 1,
     "why": "The three primary colours of light add together to give white."},
    {"topic": "Subtraction of colours", "q": "A blue object is viewed in pure "
     "red light. It appears:",
     "options": ["blue", "red", "black", "white"], "correct": 2,
     "why": "A blue object reflects only blue and absorbs red; with no blue "
            "light to reflect, it looks black."},
    {"topic": "Colour filters", "q": "White light passes through a blue filter "
     "and then a yellow filter, one behind the other. The light emerging is:",
     "options": ["white", "green", "practically no light (black)", "red"],
     "correct": 2,
     "why": "The blue filter passes only blue; the yellow filter absorbs blue, "
            "so almost no light gets through."},
    {"topic": "Colour of objects", "q": "A green leaf looks green in white "
     "light because it:",
     "options": ["absorbs green and reflects the rest",
                 "reflects green and absorbs the other colours",
                 "gives out green light of its own",
                 "scatters all colours equally"], "correct": 1,
     "why": "An object's colour is the colour it reflects; the leaf reflects "
            "green and absorbs the others."},
    {"topic": "Image size", "q": "A 4 cm tall candle is placed 10 cm from a "
     "plane mirror. The height of the image and its distance from the mirror "
     "are:",
     "options": ["4 cm, 10 cm", "2 cm, 10 cm", "4 cm, 20 cm", "8 cm, 10 cm"],
     "correct": 0,
     "why": "A plane-mirror image is the same size (4 cm) and as far behind as "
            "the object is in front (10 cm)."},
    {"topic": "Normal incidence", "q": "A ray of light falls along the normal "
     "on a plane mirror. The angle between the incident and reflected rays "
     "is:",
     "options": ["0°", "90°", "180°", "45°"], "correct": 2,
     "why": "At normal incidence the ray retraces its path, so the incident "
            "and reflected rays are opposite — 180° apart."},
    {"topic": "Uses of plane mirrors", "q": "A kaleidoscope produces multiple "
     "symmetrical patterns using:",
     "options": ["a single convex lens", "two or three plane mirrors set at "
                 "an angle", "a glass prism", "a concave mirror"],
     "correct": 1,
     "why": "Plane mirrors inclined at an angle give many images arranged in "
            "symmetric patterns."},
]

LE_WK_SUBJ = [
    {"topic": "Laws of reflection", "marks": 3,
     "q": "State the two laws of reflection of light. A ray strikes a plane "
          "mirror at an angle of incidence of 35°. Find (i) the angle of "
          "reflection and (ii) the angle between the incident and reflected "
          "rays.",
     "answer": [
        "Law 1: the angle of incidence equals the angle of reflection.",
        "Law 2: the incident ray, the reflected ray and the normal at the "
        "point of incidence all lie in the same plane.",
        "(i) Angle of reflection = 35°. (ii) Angle between incident and "
        "reflected rays = 35° + 35° = 70°."]},
    {"topic": "Plane-mirror image", "marks": 4,
     "q": "List four characteristics of the image formed by a plane mirror. "
          "Why can this image never be obtained on a screen?",
     "answer": [
        "It is virtual, erect, the same size as the object and laterally "
        "inverted.",
        "It is formed as far behind the mirror as the object is in front.",
        "It cannot be caught on a screen because the reflected rays only "
        "appear to meet behind the mirror — they do not actually meet, so the "
        "image is virtual."]},
    {"topic": "Regular vs diffuse", "marks": 3,
     "q": "Distinguish between regular and irregular (diffuse) reflection. Why "
          "is the printed page of a book visible from every part of a room?",
     "answer": [
        "Regular reflection: from a smooth, polished surface, parallel rays "
        "are reflected parallel and a clear image forms.",
        "Irregular (diffuse) reflection: from a rough surface, parallel rays "
        "are scattered in many directions and no image forms.",
        "A book page is rough, so it reflects light diffusely in all "
        "directions and is seen from everywhere in the room."]},
    {"topic": "Primary & secondary colours", "marks": 4,
     "q": "Name the three primary colours of light. What is a secondary "
          "colour? Write the three secondary colours with the primaries that "
          "form them, and state what all three primaries together give.",
     "answer": [
        "Primary colours of light: red, green and blue.",
        "A secondary colour is obtained by mixing two primary colours.",
        "Yellow = red + green; cyan = green + blue; magenta = red + blue.",
        "All three primaries together give white light."]},
    {"topic": "Subtraction of colours", "marks": 3,
     "q": "Explain why a red flower appears red in daylight but black when "
          "seen in blue light.",
     "answer": [
        "An opaque object shows the colour it reflects and absorbs the rest.",
        "In white daylight the flower reflects red and absorbs the other "
        "colours, so it looks red.",
        "In blue light there is no red to reflect; the flower absorbs the "
        "blue and reflects nothing, so it appears black."]},
]

LE_HW_S37 = [
    {"topic": "Laws of reflection", "q": "A ray of light makes an angle of 40° "
     "with the surface of a plane mirror. The angle of incidence is:",
     "options": ["40°", "50°", "90°", "80°"], "correct": 1,
     "why": "Angle of incidence is measured from the normal: 90° − 40° = 50°."},
    {"topic": "Laws of reflection", "q": "If the angle of incidence is "
     "increased by 15°, the angle of reflection:",
     "options": ["decreases by 15°", "increases by 15°", "stays the same",
                 "becomes zero"], "correct": 1,
     "why": "By the first law the angle of reflection always equals the angle "
            "of incidence, so it also increases by 15°."},
    {"topic": "Normal incidence", "q": "When a ray falls along the normal on a "
     "plane mirror, the angle of reflection is:",
     "options": ["90°", "45°", "0°", "180°"], "correct": 2,
     "why": "Along the normal the angle of incidence is 0°, so the angle of "
            "reflection is also 0°."},
    {"topic": "Image distance", "q": "When you walk towards a plane mirror at "
     "1 m/s, your image approaches the mirror at:",
     "options": ["0.5 m/s", "1 m/s", "2 m/s", "it stays still"], "correct": 1,
     "why": "The image is always as far behind as the object is in front, so "
            "it approaches the mirror at the same 1 m/s."},
    {"topic": "Verification", "q": "In the experiment to verify the laws of "
     "reflection, the angles are measured from the:",
     "options": ["mirror surface", "normal at the point of incidence",
                 "edge of the paper", "reflected object"], "correct": 1,
     "why": "Both angles are measured between the ray and the normal at the "
            "point of incidence."},
    {"topic": "Virtual image", "q": "A plane-mirror image is described as "
     "virtual because:",
     "options": ["it is smaller than the object", "it can be caught on a "
                 "screen", "the reflected rays only appear to meet behind the "
                 "mirror", "it is laterally inverted"], "correct": 2,
     "why": "The rays do not really meet; they only appear to come from behind "
            "the mirror, so the image is virtual."},
    {"topic": "Terms", "q": "The angle between the incident ray and the "
     "mirror surface is called the:",
     "options": ["angle of incidence", "glancing angle", "angle of "
                 "reflection", "normal angle"], "correct": 1,
     "why": "The angle measured from the mirror surface (not the normal) is "
            "the glancing angle."},
    {"topic": "Regular reflection", "q": "Two parallel rays strike a plane "
     "mirror. After reflection they are:",
     "options": ["parallel", "convergent", "divergent", "perpendicular"],
     "correct": 0,
     "why": "Regular reflection from a smooth mirror keeps parallel rays "
            "parallel."},
    {"topic": "Lateral inversion", "q": "Held up to a plane mirror, the small "
     "letter 'b' appears as:",
     "options": ["b", "d", "p", "q"], "correct": 1,
     "why": "Lateral inversion swaps left and right, turning 'b' into 'd'."},
    {"topic": "Terms", "q": "In reflection, the normal is a line drawn:",
     "options": ["along the mirror surface", "perpendicular to the mirror at "
                 "the point of incidence", "parallel to the incident ray",
                 "through the image"], "correct": 1,
     "why": "The normal is the perpendicular to the mirror at the point where "
            "the ray strikes."},
]

LE_HW_S38 = [
    {"topic": "Real image", "q": "Which of the following forms a real image?",
     "options": ["a plane mirror", "a cinema projector on a screen",
                 "a flat looking-glass", "a periscope"], "correct": 1,
     "why": "A real image can be caught on a screen, as with a cinema "
            "projector."},
    {"topic": "Lateral inversion", "q": "Which capital letter looks exactly "
     "the same as its plane-mirror image?",
     "options": ["B", "A", "P", "R"], "correct": 1,
     "why": "'A' is symmetric about a vertical axis, so its mirror image is "
            "unchanged."},
    {"topic": "Diffuse reflection", "q": "We cannot see our reflection on a "
     "tarred road because its rough surface causes:",
     "options": ["regular reflection", "diffuse reflection", "refraction",
                 "dispersion"], "correct": 1,
     "why": "A rough surface scatters light in all directions (diffuse "
            "reflection), so no image forms."},
    {"topic": "Speed of light", "q": "Light travels at 3×10⁸ m/s. The time it "
     "takes to travel 1 km (1000 m) is:",
     "options": ["3.3×10⁻⁶ s", "3×10¹¹ s", "3.3×10⁻³ s", "300 s"],
     "correct": 0,
     "why": "Time = distance / speed = 1000 / (3×10⁸) ≈ 3.3×10⁻⁶ s."},
    {"topic": "Colour of objects", "q": "An object that reflects all the "
     "colours of white light falling on it appears:",
     "options": ["black", "white", "grey", "red"], "correct": 1,
     "why": "Reflecting all colours together looks white."},
    {"topic": "Colour of objects", "q": "An object that absorbs all the "
     "colours of light falling on it appears:",
     "options": ["white", "black", "blue", "invisible"], "correct": 1,
     "why": "With nothing reflected back to the eye, the object looks black."},
    {"topic": "Secondary colours", "q": "Cyan light is obtained by combining:",
     "options": ["red and green", "green and blue", "red and blue",
                 "red and yellow"], "correct": 1,
     "why": "Cyan = Green + Blue."},
    {"topic": "Colours of light", "q": "Yellow is a ___ colour of light.",
     "options": ["primary", "secondary", "complementary only", "invisible"],
     "correct": 1,
     "why": "Yellow is made by mixing two primaries (red + green), so it is a "
            "secondary colour."},
    {"topic": "Colour filters", "q": "A green glass filter allows to pass "
     "mainly:",
     "options": ["all colours", "green light", "red light", "no light"],
     "correct": 1,
     "why": "A filter transmits its own colour and absorbs the others, so a "
            "green filter passes green."},
    {"topic": "White light", "q": "White light from the Sun is a mixture of:",
     "options": ["three colours", "five colours", "seven colours",
                 "two colours"], "correct": 2,
     "why": "White light splits into seven colours (VIBGYOR)."},
]

LE_HW_WK = [
    {"topic": "Normal incidence", "q": "A ray strikes a plane mirror "
     "perpendicularly. It retraces its path because the angle of incidence "
     "is:",
     "options": ["90°", "0°", "45°", "180°"], "correct": 1,
     "why": "Along the normal the angle of incidence is 0°, so the ray "
            "reflects straight back."},
    {"topic": "Image distance", "q": "An object is 25 cm from a plane mirror. "
     "The image is ___ from the object.",
     "options": ["25 cm", "50 cm", "12.5 cm", "75 cm"], "correct": 1,
     "why": "Image is 25 cm behind the mirror, so object-to-image = "
            "25 + 25 = 50 cm."},
    {"topic": "Two mirrors", "q": "Two plane mirrors face each other parallel "
     "(angle 0°). The number of images formed is:",
     "options": ["one", "two", "infinite", "none"], "correct": 2,
     "why": "Parallel facing mirrors reflect repeatedly, forming an (in "
            "principle) infinite series of images."},
    {"topic": "Lateral inversion", "q": "In a mirror a wall clock appears to "
     "show 9:00. The real time is:",
     "options": ["3:00", "9:00", "6:00", "12:00"], "correct": 0,
     "why": "Lateral inversion reverses left and right, so a mirror reading of "
            "9:00 corresponds to an actual time of 3:00."},
    {"topic": "Diffuse reflection", "q": "Light falling on a white wall is "
     "reflected diffusely, which is why the wall:",
     "options": ["acts as a mirror", "is visible from all directions but "
                 "shows no image", "appears black", "cannot be seen"],
     "correct": 1,
     "why": "Diffuse reflection scatters light everywhere, so the wall is seen "
            "from all sides but forms no image."},
    {"topic": "Real vs virtual", "q": "Which of these is a virtual image?",
     "options": ["the image on a cinema screen", "the image in a bathroom "
                 "mirror", "the image on photographic film", "the image on a "
                 "wall from a pinhole"], "correct": 1,
     "why": "A mirror image cannot be caught on a screen — it is virtual; the "
            "others are real images."},
    {"topic": "Speed of light", "q": "Light from the Moon takes about 1.3 s to "
     "reach Earth. Taking c = 3×10⁸ m/s, the distance is about:",
     "options": ["3.9×10⁸ m", "2.3×10⁸ m", "4×10⁵ m", "1.3×10⁸ m"],
     "correct": 0,
     "why": "Distance = speed × time = 3×10⁸ × 1.3 = 3.9×10⁸ m."},
    {"topic": "Addition of colours", "q": "On a white screen, overlapping blue "
     "and green spotlights give:",
     "options": ["yellow", "cyan", "magenta", "white"], "correct": 1,
     "why": "Blue + Green = Cyan."},
    {"topic": "Subtraction of colours", "q": "A white shirt seen under red "
     "stage lighting appears:",
     "options": ["white", "red", "black", "green"], "correct": 1,
     "why": "A white surface reflects whatever light falls on it, so under red "
            "light it looks red."},
    {"topic": "Colour filters", "q": "A yellow object is viewed through a blue "
     "filter (only blue passes). The object appears:",
     "options": ["yellow", "blue", "black", "green"], "correct": 2,
     "why": "A yellow object reflects red and green but no blue; the blue "
            "filter blocks red and green, so no light reaches the eye and it "
            "looks black."},
]


# ===========================================================================
# CHAPTER 2 — HEAT  (S55 + S56 + S57)
# ===========================================================================
HT_WK_MCQ = [
    {"topic": "Heat vs temperature", "q": "Two iron balls of 1 kg and 2 kg "
     "are at the same temperature of 80°C. Compared with the 1 kg ball, the "
     "2 kg ball contains:",
     "options": ["the same heat energy", "more heat energy", "less heat "
                 "energy", "no heat energy"], "correct": 1,
     "why": "At the same temperature, the body with more mass holds more total "
            "heat (thermal) energy."},
    {"topic": "Units of heat", "q": "The heat needed to raise the temperature "
     "of 10 g of water by 5°C is (specific heat of water = 1 cal/g°C):",
     "options": ["50 cal", "2 cal", "15 cal", "5 cal"], "correct": 0,
     "why": "Q = m × c × ΔT = 10 × 1 × 5 = 50 cal."},
    {"topic": "Units of heat", "q": "Taking 1 cal = 4.2 J, a quantity of "
     "50 cal of heat equals:",
     "options": ["210 J", "11.9 J", "54.2 J", "45.8 J"], "correct": 0,
     "why": "50 × 4.2 = 210 J."},
    {"topic": "Temperature scales", "q": "Normal human body temperature is "
     "37°C. On the Fahrenheit scale this is:",
     "options": ["98.6°F", "69.8°F", "310°F", "66.6°F"], "correct": 0,
     "why": "F = (9/5)×37 + 32 = 66.6 + 32 = 98.6°F."},
    {"topic": "Temperature scales", "q": "A temperature of −13°C expressed in "
     "kelvin is:",
     "options": ["260 K", "286 K", "273 K", "13 K"], "correct": 0,
     "why": "K = °C + 273 = −13 + 273 = 260 K."},
    {"topic": "Temperature scales", "q": "On which scale can a temperature "
     "never be negative?",
     "options": ["Celsius", "Fahrenheit", "Kelvin", "all of them"],
     "correct": 2,
     "why": "0 K (absolute zero) is the lowest possible temperature, so kelvin "
            "values are never negative."},
    {"topic": "Measurement", "q": "Mercury is used in thermometers mainly "
     "because it:",
     "options": ["is cheap", "expands uniformly, is opaque and does not wet "
                 "glass", "boils at a low temperature", "is a good insulator"],
     "correct": 1,
     "why": "Mercury expands regularly, is easily visible and does not stick "
            "to the glass."},
    {"topic": "Measurement", "q": "A clinical thermometer has a constriction "
     "(kink) near the bulb so that:",
     "options": ["mercury rises faster", "the reading does not fall on its "
                 "own before you read it", "it measures lower temperatures",
                 "it shows room temperature"], "correct": 1,
     "why": "The kink stops the mercury slipping back, holding the reading "
            "until the thermometer is shaken."},
    {"topic": "Effects of heat", "q": "Which effect of heat does a mercury "
     "thermometer make use of?",
     "options": ["change of state", "thermal expansion of the liquid",
                 "change in colour", "change in chemical nature"],
     "correct": 1,
     "why": "The mercury expands on heating, and this expansion is read as "
            "temperature."},
    {"topic": "Thermal expansion", "q": "For the same rise in temperature, "
     "arrange the expansion in increasing order:",
     "options": ["gas < liquid < solid", "solid < liquid < gas",
                 "liquid < solid < gas", "solid < gas < liquid"],
     "correct": 1,
     "why": "Solids expand the least and gases the most for the same "
            "temperature rise."},
    {"topic": "Thermal expansion", "q": "A bimetallic strip is used in a "
     "thermostat because, on heating, it:",
     "options": ["melts", "bends and so makes or breaks a circuit",
                 "changes colour", "expands equally on both sides"],
     "correct": 1,
     "why": "The two metals expand by different amounts, so the strip bends "
            "and works as a temperature-operated switch."},
    {"topic": "Thermal expansion", "q": "Overhead telephone and electric "
     "wires are strung with a slight sag in summer so that in winter they:",
     "options": ["look neat", "do not contract and snap", "carry more "
                 "current", "expand"], "correct": 1,
     "why": "Wires contract in cold weather; the sag stops them pulling taut "
            "and breaking."},
    {"topic": "Thermal expansion", "q": "On a hot day, the air sealed inside a "
     "balloon will:",
     "options": ["contract", "expand and may burst the balloon", "stay the "
                 "same", "turn to liquid"], "correct": 1,
     "why": "Gases expand the most on heating, increasing the pressure inside "
            "the balloon."},
    {"topic": "Conduction", "q": "On a cold day a metal railing feels colder "
     "than a wooden one at the same temperature because metal:",
     "options": ["is actually colder", "conducts heat away from your hand "
                 "faster", "is heavier", "radiates more heat"], "correct": 1,
     "why": "Metal is a good conductor, so it carries heat away from your skin "
            "quickly, making it feel colder."},
    {"topic": "Convection", "q": "The freezer (cooling unit) of a refrigerator "
     "is placed at the top because:",
     "options": ["it looks better", "cold air sinks, setting up convection "
                 "currents that cool the whole fridge", "cold air rises",
                 "heat rises from the food"], "correct": 1,
     "why": "Cold, dense air sinks while warm air rises, so convection "
            "circulates and cools the entire fridge."},
    {"topic": "Convection", "q": "At night a breeze blows from the land "
     "towards the sea because:",
     "options": ["the sea cools faster than the land", "the land cools faster "
                 "than the sea, so warmer air over the sea rises", "there is "
                 "no wind at night", "the land heats up at night"],
     "correct": 1,
     "why": "At night the land cools quicker; air over the warmer sea rises "
            "and cooler air flows from land to sea."},
    {"topic": "Radiation", "q": "Heat from the Sun reaches the Earth through "
     "empty space by:",
     "options": ["conduction", "convection", "radiation", "all three"],
     "correct": 2,
     "why": "Only radiation needs no material medium, so it can cross the "
            "vacuum of space."},
    {"topic": "Surfaces", "q": "Cooling fins and the back of a refrigerator "
     "are painted dull black because such surfaces are good:",
     "options": ["reflectors of heat", "emitters of heat radiation",
                 "insulators", "conductors"], "correct": 1,
     "why": "Dull black surfaces are the best emitters (and absorbers) of "
            "radiation, helping the heat escape."},
    {"topic": "Surfaces", "q": "People prefer light-coloured clothes in summer "
     "because light/white surfaces:",
     "options": ["absorb more heat", "reflect most of the heat radiation",
                 "emit more heat", "conduct heat"], "correct": 1,
     "why": "White surfaces reflect most of the heat falling on them, keeping "
            "the body cooler."},
    {"topic": "Thermos flask", "q": "The double walls of a thermos flask are "
     "silvered in order to reduce heat transfer by:",
     "options": ["conduction", "convection", "radiation", "evaporation"],
     "correct": 2,
     "why": "Silvered (shiny) surfaces reflect heat radiation back; the vacuum "
            "between the walls already stops conduction and convection."},
]

HT_WK_SUBJ = [
    {"topic": "Heat vs temperature", "marks": 4,
     "q": "Distinguish between heat and temperature. State the SI unit of "
          "each. How are the Celsius and Kelvin temperatures related?",
     "answer": [
        "Heat is the total thermal (internal) energy of a body and depends on "
        "its mass; temperature is the degree of hotness that decides the "
        "direction of heat flow and does not depend on mass.",
        "SI unit of heat = joule (J); SI unit of temperature = kelvin (K).",
        "Relation: T (in K) = t (in °C) + 273."]},
    {"topic": "Temperature scales", "marks": 3,
     "q": "Convert 50°C into (i) the Fahrenheit scale and (ii) the Kelvin "
          "scale.",
     "answer": [
        "(i) F = (9/5) × 50 + 32 = 90 + 32 = 122°F.",
        "(ii) K = 50 + 273 = 323 K."]},
    {"topic": "Thermal expansion", "marks": 4,
     "q": "Why are gaps left between two rails of a railway track? Arrange the "
          "three states of matter in increasing order of thermal expansion for "
          "the same rise in temperature.",
     "answer": [
        "Gaps are left so the rails have room to lengthen when they expand in "
        "hot weather and do not buckle or bend.",
        "For the same temperature rise, expansion increases in the order: "
        "solids (least) < liquids < gases (most)."]},
    {"topic": "Modes of heat transfer", "marks": 4,
     "q": "Name the three modes of heat transfer and the medium each needs. "
          "Which mode brings the Sun's heat to the Earth, and why?",
     "answer": [
        "Conduction: occurs mainly in solids — heat passes from particle to "
        "particle without the particles moving along.",
        "Convection: occurs in liquids and gases — the heated fluid itself "
        "moves and carries heat.",
        "Radiation: needs no medium at all.",
        "The Sun's heat reaches us by radiation, because the space between is "
        "a vacuum and only radiation can cross empty space."]},
    {"topic": "Thermos flask", "marks": 3,
     "q": "Explain how a vacuum (thermos) flask keeps a hot drink hot, "
          "mentioning how each mode of heat transfer is reduced.",
     "answer": [
        "The vacuum between the double walls stops heat loss by conduction and "
        "convection, as there is no medium to carry the heat.",
        "The silvered walls reflect heat radiation back, reducing loss by "
        "radiation.",
        "The insulating cork/plastic stopper reduces conduction and "
        "convection through the mouth of the flask."]},
]

HT_HW_S55 = [
    {"topic": "Units of heat", "q": "One kilocalorie (1 kcal) of heat is equal "
     "to about:",
     "options": ["4.2 J", "420 J", "4200 J", "42 J"], "correct": 2,
     "why": "1 kcal = 1000 cal, and 1 cal = 4.2 J, so 1 kcal = 4200 J."},
    {"topic": "Heat as energy", "q": "Heat is a form of energy, so it is "
     "measured in the same unit as:",
     "options": ["mass", "work and energy (the joule)", "temperature", "time"],
     "correct": 1,
     "why": "Heat is energy, measured in joules — the same unit as work."},
    {"topic": "Temperature scales", "q": "A temperature of 20°C on the "
     "Fahrenheit scale is:",
     "options": ["68°F", "36°F", "52°F", "93.3°F"], "correct": 0,
     "why": "F = (9/5)×20 + 32 = 36 + 32 = 68°F."},
    {"topic": "Temperature scales", "q": "A temperature of 50°F on the Celsius "
     "scale is:",
     "options": ["10°C", "18°C", "122°C", "82°C"], "correct": 0,
     "why": "C = (F − 32) × 5/9 = (50 − 32) × 5/9 = 10°C."},
    {"topic": "Temperature scales", "q": "The melting point of ice, 0°C, in "
     "kelvin is:",
     "options": ["0 K", "100 K", "273 K", "373 K"], "correct": 2,
     "why": "K = °C + 273 = 0 + 273 = 273 K."},
    {"topic": "Temperature scales", "q": "On the Fahrenheit scale, the melting "
     "point of ice and the boiling point of water are:",
     "options": ["0° and 100°", "32° and 212°", "273° and 373°", "32° and "
                 "100°"], "correct": 1,
     "why": "On the Fahrenheit scale ice melts at 32°F and water boils at "
            "212°F."},
    {"topic": "Measurement", "q": "Besides mercury, the liquid commonly used "
     "in a thermometer for low temperatures is:",
     "options": ["water", "coloured alcohol", "oil", "milk"], "correct": 1,
     "why": "Alcohol has a very low freezing point, so it is used to measure "
            "low temperatures."},
    {"topic": "Measurement", "q": "A clinical thermometer is given a kink "
     "(constriction) so that the reading:",
     "options": ["rises quickly", "does not drop until shaken", "is more "
                 "accurate at 0°C", "shows room temperature"], "correct": 1,
     "why": "The kink prevents mercury flowing back, so the reading stays "
            "until the thermometer is shaken down."},
    {"topic": "Measurement", "q": "Mercury is suitable for a thermometer "
     "partly because it does not stick to glass; this property is that it:",
     "options": ["does not wet glass", "shows capillarity", "conducts heat",
                 "is viscous"], "correct": 0,
     "why": "Mercury does not wet (stick to) glass, so it moves cleanly in the "
            "tube."},
    {"topic": "Heat flow", "q": "A cup of hot tea left on a table cools "
     "because heat flows from the:",
     "options": ["table to the tea", "tea to the cooler surroundings", "air "
                 "to the tea", "tea to nowhere"], "correct": 1,
     "why": "Heat always flows from the hotter body (tea) to the cooler "
            "surroundings."},
]

HT_HW_S56 = [
    {"topic": "Effects of heat", "q": "When a metal ball is heated, which of "
     "these increases?",
     "options": ["its mass", "its size (it expands)", "its colour "
                 "permanently", "its weight"], "correct": 1,
     "why": "Heating makes the ball expand, so its size increases (its mass "
            "stays the same)."},
    {"topic": "Change of state", "q": "On strong heating, ice changes to water "
     "and then to steam. This shows heat causing:",
     "options": ["expansion only", "a change of state", "a change of colour",
                 "a chemical change"], "correct": 1,
     "why": "Solid to liquid to gas is a change of state caused by heat."},
    {"topic": "Thermal expansion", "q": "For the same rise in temperature, "
     "which of these expands the least?",
     "options": ["air", "water", "an iron rod", "alcohol"], "correct": 2,
     "why": "Solids such as iron expand the least; gases the most."},
    {"topic": "Thermal expansion", "q": "A metal lid stuck on a glass jar "
     "opens more easily after running it under hot water because the metal "
     "lid:",
     "options": ["contracts", "expands more than the glass", "melts",
                 "becomes lighter"], "correct": 1,
     "why": "Metal expands more than glass for the same heating, loosening "
            "the lid."},
    {"topic": "Thermal expansion", "q": "A bimetallic strip is made of two "
     "metals that, on heating, expand:",
     "options": ["equally", "by different amounts", "not at all", "only when "
                 "bent"], "correct": 1,
     "why": "The two metals expand by different amounts, so the strip bends."},
    {"topic": "Thermal expansion", "q": "Overhead wires are kept slightly "
     "loose so that they do not snap on a cold day, when they:",
     "options": ["expand", "contract", "melt", "conduct"], "correct": 1,
     "why": "Wires contract in the cold; the slack stops them pulling tight "
            "and breaking."},
    {"topic": "Thermal expansion", "q": "A dented table-tennis ball regains "
     "its shape in hot water because the air inside it:",
     "options": ["contracts", "expands and pushes the dent out", "escapes",
                 "turns to liquid"], "correct": 1,
     "why": "The trapped air expands on heating and pushes the dent out."},
    {"topic": "Thermal expansion", "q": "When a flask completely full of water "
     "is heated, the water level first falls slightly and then rises because:",
     "options": ["water contracts", "the flask expands first, then the water "
                 "expands even more", "water evaporates", "this never "
                 "happens"], "correct": 1,
     "why": "The glass flask warms and expands first, lowering the level; then "
            "the water (which expands more) rises."},
    {"topic": "Thermal expansion", "q": "Bottles of liquid are never filled "
     "right up to the brim because on warming the liquid will:",
     "options": ["contract", "expand and may overflow or burst the bottle",
                 "freeze", "stay the same"], "correct": 1,
     "why": "Liquids expand on heating; the gap leaves room so they do not "
            "overflow."},
    {"topic": "Change of state", "q": "The change of a liquid into vapour on "
     "heating is called:",
     "options": ["melting", "vaporisation", "condensation", "freezing"],
     "correct": 1,
     "why": "Liquid changing to vapour on heating is vaporisation (boiling/"
            "evaporation)."},
]

HT_HW_S57 = [
    {"topic": "Conduction", "q": "Heat passes along a metal spoon dipped in "
     "hot tea mainly by:",
     "options": ["convection", "conduction", "radiation", "evaporation"],
     "correct": 1,
     "why": "In a solid, heat travels by conduction from particle to "
            "particle."},
    {"topic": "Conductors", "q": "Which of the following is the best conductor "
     "of heat?",
     "options": ["wood", "copper", "plastic", "glass"], "correct": 1,
     "why": "Metals such as copper are the best conductors of heat."},
    {"topic": "Insulators", "q": "Woollen clothes keep us warm in winter "
     "because wool:",
     "options": ["produces heat", "traps air and is a poor conductor, so it "
                 "reduces heat loss", "is a good conductor", "reflects heat"],
     "correct": 1,
     "why": "Wool traps air (a poor conductor) and slows the loss of body "
            "heat."},
    {"topic": "Convection", "q": "Convection can take place in:",
     "options": ["solids only", "liquids and gases", "a vacuum", "metals"],
     "correct": 1,
     "why": "Convection needs a fluid that can move, so it occurs in liquids "
            "and gases."},
    {"topic": "Convection", "q": "Ventilators are placed near the ceiling of a "
     "room so that:",
     "options": ["cold air enters", "warm, used air which rises can escape",
                 "light enters", "the room looks bigger"], "correct": 1,
     "why": "Warm air rises by convection and escapes through high "
            "ventilators, drawing in fresh air."},
    {"topic": "Radiation", "q": "We feel the warmth of a fire instantly mainly "
     "because of:",
     "options": ["conduction through air", "convection only", "radiation",
                 "sound"], "correct": 2,
     "why": "The fire's heat reaches us directly by radiation, which travels "
            "without needing the air to move."},
    {"topic": "Surfaces", "q": "The cooling pipes at the back of a "
     "refrigerator are painted black so that they:",
     "options": ["look nice", "radiate (give out) heat efficiently", "absorb "
                 "heat from the room", "conduct electricity"], "correct": 1,
     "why": "Black surfaces are good emitters of radiation, so they give out "
            "the unwanted heat well."},
    {"topic": "Surfaces", "q": "Houses in hot countries are often painted "
     "white because white surfaces:",
     "options": ["absorb heat", "reflect most of the heat and keep the house "
                 "cool", "conduct heat", "radiate heat"], "correct": 1,
     "why": "White reflects most of the incoming radiation, keeping the inside "
            "cooler."},
    {"topic": "Thermos flask", "q": "The stopper of a thermos flask is made of "
     "cork or plastic to reduce heat loss by:",
     "options": ["radiation", "conduction and convection through the mouth",
                 "reflection", "absorption"], "correct": 1,
     "why": "Cork/plastic are poor conductors and close the mouth, cutting "
            "conduction and convection there."},
    {"topic": "Surfaces", "q": "On a sunny day a person in black clothes feels "
     "hotter than one in white clothes because black:",
     "options": ["reflects heat", "absorbs more heat radiation", "conducts "
                 "less", "radiates more"], "correct": 1,
     "why": "Black surfaces absorb most of the radiation falling on them, so "
            "they feel hotter."},
]

HT_HW_WK = [
    {"topic": "Temperature scales", "q": "A temperature of 35°C on the "
     "Fahrenheit scale is:",
     "options": ["95°F", "63°F", "308°F", "67°F"], "correct": 0,
     "why": "F = (9/5)×35 + 32 = 63 + 32 = 95°F."},
    {"topic": "Temperature scales", "q": "Absolute zero, the lowest possible "
     "temperature, is:",
     "options": ["0°C", "0 K", "273 K", "−100°C"], "correct": 1,
     "why": "Absolute zero is 0 K (about −273°C), the lowest temperature "
            "possible."},
    {"topic": "Thermal expansion", "q": "Gaps in railway lines, rollers under "
     "bridges and loops in pipelines all allow for:",
     "options": ["rusting", "thermal expansion and contraction", "bending of "
                 "light", "electric current"], "correct": 1,
     "why": "These provisions give room for materials to expand and contract "
            "with temperature."},
    {"topic": "Thermal expansion", "q": "A device that uses a bimetallic strip "
     "to switch a circuit on and off at a set temperature is a:",
     "options": ["barometer", "thermostat", "galvanometer", "periscope"],
     "correct": 1,
     "why": "A thermostat uses the bending of a bimetallic strip to control "
            "temperature automatically."},
    {"topic": "Conduction", "q": "In conduction, heat travels through a solid "
     "because:",
     "options": ["the particles move from the hot end to the cold end", "heat "
                 "passes from particle to particle without the particles "
                 "moving along", "the solid melts", "radiation occurs"],
     "correct": 1,
     "why": "Particles vibrate and pass energy to their neighbours; they do "
            "not travel along the solid."},
    {"topic": "Convection", "q": "Smoke rises up a chimney because of ___ "
     "currents of hot air.",
     "options": ["conduction", "convection", "radiation", "magnetic"],
     "correct": 1,
     "why": "Hot air is less dense and rises, carrying the smoke up by "
            "convection."},
    {"topic": "Radiation", "q": "Unlike conduction and convection, radiation:",
     "options": ["needs a solid", "needs a liquid", "needs no material "
                 "medium", "cannot pass through air"], "correct": 2,
     "why": "Radiation can travel through a vacuum; it needs no medium."},
    {"topic": "Surfaces", "q": "A shiny silver surface is a ___ absorber and a "
     "___ emitter of heat radiation.",
     "options": ["good, good", "poor, poor", "good, poor", "poor, good"],
     "correct": 1,
     "why": "Polished, shiny surfaces reflect radiation, so they are poor both "
            "at absorbing and at emitting it."},
    {"topic": "Convection", "q": "A room heater warms the air of a room mainly "
     "by radiation and by setting up ___ currents.",
     "options": ["conduction", "convection", "magnetic", "sound"],
     "correct": 1,
     "why": "Warm air rises and cooler air sinks, circulating heat round the "
            "room by convection."},
    {"topic": "Thermos flask", "q": "A thermos flask keeps cold drinks cold as "
     "well as hot drinks hot because it:",
     "options": ["adds heat", "reduces heat transfer in both directions",
                 "only keeps things hot", "produces cold"], "correct": 1,
     "why": "By cutting conduction, convection and radiation it slows heat "
            "flow either way."},
]


# ===========================================================================
# CHAPTER 3 — SOUND  (S66 + S67)
# ===========================================================================
SO_WK_MCQ = [
    {"topic": "Production of sound", "q": "A stretched rubber band twangs when "
     "plucked. The sound stops as soon as the band stops:",
     "options": ["stretching", "vibrating", "glowing", "moving forward"],
     "correct": 1,
     "why": "Sound is produced by a vibrating body; when the vibration stops, "
            "the sound stops."},
    {"topic": "Medium for sound", "q": "An astronaut on the Moon cannot hear "
     "his companion speak directly because the Moon has:",
     "options": ["too much gravity", "no air (no material medium) to carry "
                 "sound", "a very low temperature", "strong magnetism"],
     "correct": 1,
     "why": "Sound needs a material medium; the Moon has practically no air, "
            "so sound cannot travel."},
    {"topic": "Speed in media", "q": "Sound travels fastest through:",
     "options": ["air", "water", "steel (a solid)", "vacuum"], "correct": 2,
     "why": "Particles are closest in solids, so sound travels fastest in "
            "solids such as steel."},
    {"topic": "Longitudinal waves", "q": "In air, a sound wave travels as a "
     "series of:",
     "options": ["crests and troughs", "compressions and rarefactions",
                 "still particles", "colours"], "correct": 1,
     "why": "Sound in air is a longitudinal wave of compressions and "
            "rarefactions."},
    {"topic": "Wave relation", "q": "A sound wave of frequency 170 Hz travels "
     "at 340 m/s. Its wavelength is:",
     "options": ["2 m", "0.5 m", "510 m", "57800 m"], "correct": 0,
     "why": "λ = v / f = 340 / 170 = 2 m."},
    {"topic": "Frequency & period", "q": "A vibrating body has a time period "
     "of 0.005 s. Its frequency is:",
     "options": ["200 Hz", "0.005 Hz", "5 Hz", "2000 Hz"], "correct": 0,
     "why": "f = 1 / T = 1 / 0.005 = 200 Hz."},
    {"topic": "Frequency & period", "q": "A tuning fork of frequency 250 Hz "
     "has a time period of:",
     "options": ["0.004 s", "250 s", "4 s", "0.25 s"], "correct": 0,
     "why": "T = 1 / f = 1 / 250 = 0.004 s."},
    {"topic": "Ultrasonic", "q": "A sound of frequency 30,000 Hz is:",
     "options": ["audible", "infrasonic", "ultrasonic", "subsonic"],
     "correct": 2,
     "why": "Frequencies above 20,000 Hz are ultrasonic."},
    {"topic": "Infrasonic", "q": "A sound of frequency 10 Hz is classified "
     "as:",
     "options": ["audible", "ultrasonic", "infrasonic", "supersonic"],
     "correct": 2,
     "why": "Frequencies below 20 Hz are infrasonic."},
    {"topic": "Pitch", "q": "Two sounds have the same loudness but one is "
     "shriller than the other. The shriller sound differs in its:",
     "options": ["amplitude", "frequency", "speed", "medium"], "correct": 1,
     "why": "Shrillness is pitch, which depends on frequency; a shriller sound "
            "has a higher frequency."},
    {"topic": "Loudness", "q": "If the amplitude of a vibrating string is "
     "doubled while its frequency is unchanged, the sound becomes:",
     "options": ["higher in pitch", "louder", "faster", "softer"],
     "correct": 1,
     "why": "Loudness depends on amplitude; a larger amplitude gives a louder "
            "sound."},
    {"topic": "Quality", "q": "The same musical note played on a flute and on "
     "a violin can be told apart because they differ in:",
     "options": ["pitch", "loudness", "quality (timbre)", "speed"],
     "correct": 2,
     "why": "Quality (timbre) depends on the waveform and lets us identify the "
            "instrument."},
    {"topic": "Speed of sound", "q": "The speed of sound in air increases when "
     "the air becomes:",
     "options": ["colder", "warmer", "drier", "still"], "correct": 1,
     "why": "Sound travels faster in warmer air, as its particles move more "
            "quickly."},
    {"topic": "Echo", "q": "A man shouts towards a cliff and hears the echo "
     "after 3 s. If the speed of sound is 340 m/s, the cliff is:",
     "options": ["510 m away", "1020 m away", "113 m away", "680 m away"],
     "correct": 0,
     "why": "Distance = (speed × time)/2 = (340 × 3)/2 = 510 m."},
    {"topic": "Echo", "q": "To hear a distinct echo, the reflecting surface "
     "must be at least about ___ away (speed of sound 340 m/s):",
     "options": ["1 m", "17 m", "340 m", "0.1 m"], "correct": 1,
     "why": "The ear separates sounds 0.1 s apart, so minimum distance = "
            "(340 × 0.1)/2 ≈ 17 m."},
    {"topic": "Reflection of sound", "q": "An echo is an example of the ___ of "
     "sound.",
     "options": ["absorption", "reflection", "refraction", "production"],
     "correct": 1,
     "why": "An echo is sound heard again after being reflected from a distant "
            "surface."},
    {"topic": "Ultrasound", "q": "Ultrasonic waves are used by ships to find "
     "the depth of the sea because they:",
     "options": ["travel slower", "can be sent as a narrow beam and reflect "
                 "well", "are audible", "need no medium"], "correct": 1,
     "why": "Ultrasound can be sent as a directed beam and is strongly "
            "reflected, making it ideal for SONAR."},
    {"topic": "Ultrasound", "q": "An ultrasonic pulse from a ship returns from "
     "the sea-bed after 4 s. If the speed of sound in water is 1500 m/s, the "
     "depth is:",
     "options": ["3000 m", "6000 m", "375 m", "750 m"], "correct": 0,
     "why": "Depth = (speed × time)/2 = (1500 × 4)/2 = 3000 m."},
    {"topic": "Reflection of sound", "q": "A megaphone makes a voice carry "
     "further by:",
     "options": ["raising its frequency", "stopping the sound spreading out "
                 "and sending it forward as a beam", "absorbing the sound",
                 "slowing the sound"], "correct": 1,
     "why": "A megaphone channels the sound forward and prevents it spreading, "
            "so it carries further."},
    {"topic": "Speed of sound", "q": "You see a lightning flash and hear the "
     "thunder 5 s later. Taking the speed of sound as 340 m/s, the storm is "
     "about:",
     "options": ["1700 m away", "68 m away", "340 m away", "5 m away"],
     "correct": 0,
     "why": "Light arrives almost instantly, so distance ≈ speed of sound × "
            "time = 340 × 5 = 1700 m."},
]

SO_WK_SUBJ = [
    {"topic": "Production & medium", "marks": 3,
     "q": "How is sound produced? Describe the bell-jar experiment and state "
          "what it proves.",
     "answer": [
        "Sound is produced by a vibrating body.",
        "In the bell-jar experiment an electric bell hangs inside a glass jar "
        "joined to a vacuum pump. As the air is pumped out, the sound grows "
        "fainter and finally cannot be heard, though the hammer is seen "
        "striking.",
        "This proves that sound needs a material medium and cannot travel "
        "through a vacuum."]},
    {"topic": "Wave terms", "marks": 4,
     "q": "Define frequency, time period and wavelength. Write the relation "
          "between speed, frequency and wavelength, and find the wavelength of "
          "a 500 Hz sound travelling at 340 m/s.",
     "answer": [
        "Frequency: the number of vibrations made in one second (unit hertz).",
        "Time period: the time for one complete vibration; T = 1/f.",
        "Wavelength: the distance between two consecutive compressions (or "
        "rarefactions).",
        "Relation: v = f × λ, so λ = v/f = 340/500 = 0.68 m."]},
    {"topic": "Audible range", "marks": 3,
     "q": "What are audible, infrasonic and ultrasonic sounds? Give the "
          "frequency limits of the normal audible range.",
     "answer": [
        "Audible sounds: those a normal human ear can hear, of frequency about "
        "20 Hz to 20,000 Hz.",
        "Infrasonic: frequency below 20 Hz (e.g. produced by earthquakes).",
        "Ultrasonic: frequency above 20,000 Hz (e.g. used in SONAR; heard by "
        "bats)."]},
    {"topic": "Characteristics", "marks": 4,
     "q": "Name the three characteristics of a musical sound and state the "
          "property of the wave on which each depends.",
     "answer": [
        "Loudness — depends on the amplitude (larger amplitude → louder).",
        "Pitch (shrillness) — depends on the frequency (higher frequency → "
        "higher pitch).",
        "Quality (timbre) — depends on the waveform; it lets us tell apart the "
        "same note from different instruments."]},
    {"topic": "Echo", "marks": 3,
     "q": "What is an echo? A person claps once and hears the first echo from "
          "a cliff after 2 s. If the speed of sound is 340 m/s, how far is the "
          "cliff?",
     "answer": [
        "An echo is a sound heard again after reflection from a distant hard "
        "surface (heard distinctly when the reflector is about 17 m or more "
        "away).",
        "Distance = (speed × time)/2 = (340 × 2)/2.",
        "= 340 m."]},
]

SO_HW_S66 = [
    {"topic": "Production", "q": "Sound is a form of energy produced by the "
     "___ of a body.",
     "options": ["heating", "vibration", "cooling", "colouring"],
     "correct": 1,
     "why": "A vibrating body produces sound."},
    {"topic": "Sources", "q": "A drum gives out sound when its stretched "
     "membrane is:",
     "options": ["wet", "made to vibrate", "heated", "coloured"], "correct": 1,
     "why": "Striking the drum makes its membrane vibrate, producing sound."},
    {"topic": "Medium", "q": "Sound needs a material medium to travel, so it "
     "can pass through:",
     "options": ["vacuum only", "solids, liquids and gases", "empty space",
                 "only air"], "correct": 1,
     "why": "Sound travels through any material medium — solid, liquid or "
            "gas."},
    {"topic": "Longitudinal waves", "q": "Sound travels through air in the "
     "form of:",
     "options": ["transverse waves", "longitudinal waves", "light waves",
                 "water waves"], "correct": 1,
     "why": "In air, sound is a longitudinal wave."},
    {"topic": "Longitudinal waves", "q": "In a sound wave in air, the region "
     "where the air particles are crowded together is a:",
     "options": ["rarefaction", "compression", "crest", "trough"],
     "correct": 1,
     "why": "Crowded particles form a compression."},
    {"topic": "Longitudinal waves", "q": "The region of a sound wave where air "
     "particles are farthest apart is a:",
     "options": ["compression", "rarefaction", "node", "crest"], "correct": 1,
     "why": "Spread-out particles form a rarefaction."},
    {"topic": "Speed in media", "q": "Sound travels most slowly through:",
     "options": ["steel", "water", "air (a gas)", "iron"], "correct": 2,
     "why": "Particles are farthest apart in a gas, so sound is slowest in "
            "air."},
    {"topic": "Medium", "q": "Two astronauts on the Moon must use radios to "
     "talk because the Moon has no:",
     "options": ["light", "air to carry sound", "gravity", "rocks"],
     "correct": 1,
     "why": "With no air, sound cannot travel between them."},
    {"topic": "Medium", "q": "The sound of a bell hung inside a jar fades as "
     "the jar's air is removed. This shows that sound needs a:",
     "options": ["vacuum", "material medium", "magnet", "battery"],
     "correct": 1,
     "why": "Removing the medium stops the sound, proving a medium is "
            "required."},
    {"topic": "Sources", "q": "Which of the following is a natural source of "
     "sound?",
     "options": ["a guitar", "human vocal cords", "a loudspeaker", "a bell"],
     "correct": 1,
     "why": "Human vocal cords are a natural source; the others are "
            "man-made."},
]

SO_HW_S67 = [
    {"topic": "Frequency", "q": "The unit of frequency is the:",
     "options": ["metre", "hertz", "second", "decibel"], "correct": 1,
     "why": "Frequency is measured in hertz (Hz)."},
    {"topic": "Time period", "q": "A wave of frequency 100 Hz has a time "
     "period of:",
     "options": ["0.01 s", "100 s", "10 s", "0.1 s"], "correct": 0,
     "why": "T = 1/f = 1/100 = 0.01 s."},
    {"topic": "Wave relation", "q": "A sound of wavelength 0.5 m and frequency "
     "660 Hz travels at:",
     "options": ["330 m/s", "1320 m/s", "0.00076 m/s", "660 m/s"],
     "correct": 0,
     "why": "v = f × λ = 660 × 0.5 = 330 m/s."},
    {"topic": "Ultrasonic", "q": "Sounds of frequency above 20,000 Hz are "
     "called:",
     "options": ["infrasonic", "audible", "ultrasonic", "loud"], "correct": 2,
     "why": "Above 20,000 Hz the sound is ultrasonic."},
    {"topic": "Loudness", "q": "If two sounds have the same pitch and quality "
     "but one is louder, the louder one has a greater:",
     "options": ["frequency", "amplitude", "speed", "wavelength"],
     "correct": 1,
     "why": "Loudness depends on amplitude."},
    {"topic": "Quality", "q": "The characteristic that lets us recognise a "
     "friend's voice without seeing them is the ___ of the sound.",
     "options": ["loudness", "pitch", "quality (timbre)", "speed"],
     "correct": 2,
     "why": "Quality (timbre) distinguishes one source of sound from "
            "another."},
    {"topic": "Speed in media", "q": "Sound travels faster in water than in "
     "air because in water the particles are:",
     "options": ["farther apart", "closer together", "heavier", "colder"],
     "correct": 1,
     "why": "Closer particles pass on the vibration faster, so sound is faster "
            "in water."},
    {"topic": "Reflection", "q": "An echo is heard when sound is ___ from a "
     "distant surface.",
     "options": ["absorbed", "reflected", "refracted", "produced"],
     "correct": 1,
     "why": "An echo is reflected sound."},
    {"topic": "Echo", "q": "A girl hears the echo of her shout from a hillside "
     "1 s after shouting. If sound travels at 340 m/s, the hill is:",
     "options": ["340 m away", "170 m away", "680 m away", "34 m away"],
     "correct": 1,
     "why": "Distance = (speed × time)/2 = (340 × 1)/2 = 170 m."},
    {"topic": "Absorption", "q": "Recording studios have soft, padded walls "
     "in order to:",
     "options": ["reflect sound and create echoes", "absorb sound and reduce "
                 "echoes", "make sound louder", "speed up sound"],
     "correct": 1,
     "why": "Soft materials absorb sound, cutting down unwanted echoes."},
]

SO_HW_WK = [
    {"topic": "Speed in media", "q": "Sound is produced by vibrations and "
     "needs a medium; it travels fastest through:",
     "options": ["gases", "liquids", "solids", "vacuum"], "correct": 2,
     "why": "Closely packed particles make solids the fastest medium for "
            "sound."},
    {"topic": "Frequency", "q": "A sound wave with widely spaced rarefactions "
     "and few vibrations per second has a:",
     "options": ["high pitch", "low frequency", "large speed", "short "
                 "wavelength"], "correct": 1,
     "why": "Few vibrations per second means a low frequency (and low "
            "pitch)."},
    {"topic": "Wave relation", "q": "A tuning fork of frequency 425 Hz sounds "
     "in air (v = 340 m/s). Its wavelength is:",
     "options": ["0.8 m", "1.25 m", "144500 m", "2 m"], "correct": 0,
     "why": "λ = v/f = 340/425 = 0.8 m."},
    {"topic": "Ultrasonic", "q": "The silent whistles used to call dogs "
     "usually produce sound that is:",
     "options": ["infrasonic", "ultrasonic", "audible", "no sound at all"],
     "correct": 1,
     "why": "Dog whistles are ultrasonic — above human hearing but heard by "
            "dogs."},
    {"topic": "Loudness", "q": "Beating a drum harder, without changing "
     "anything else, increases the sound's:",
     "options": ["pitch", "loudness", "speed", "frequency"], "correct": 1,
     "why": "Hitting harder increases the amplitude, so the sound is louder."},
    {"topic": "Pitch", "q": "Tightening a guitar string raises its frequency, "
     "so the note becomes:",
     "options": ["softer", "higher in pitch", "louder", "slower"],
     "correct": 1,
     "why": "Higher frequency means higher pitch."},
    {"topic": "Speed of sound", "q": "Thunder is heard 4 s after the lightning "
     "flash. Taking the speed of sound as 340 m/s, the lightning struck "
     "about:",
     "options": ["1360 m away", "85 m away", "340 m away", "680 m away"],
     "correct": 0,
     "why": "Distance ≈ speed of sound × time = 340 × 4 = 1360 m."},
    {"topic": "Ultrasound", "q": "Ultrasound sent into the sea by a ship "
     "returns in 2 s (speed in water 1500 m/s). The sea is ___ deep.",
     "options": ["1500 m", "3000 m", "750 m", "375 m"], "correct": 0,
     "why": "Depth = (speed × time)/2 = (1500 × 2)/2 = 1500 m."},
    {"topic": "Echo", "q": "Echoes are not heard in an ordinary small room "
     "because the walls are:",
     "options": ["too soft", "too close (less than about 17 m)", "too hard",
                 "too cold"], "correct": 1,
     "why": "The reflected sound returns within 0.1 s, so it merges with the "
            "original and no separate echo is heard."},
    {"topic": "Reflection", "q": "A stethoscope carries the sound of the "
     "heartbeat to the doctor's ears mainly by:",
     "options": ["repeated reflection of sound inside its tubes", "refraction",
                 "absorption", "radiation"], "correct": 0,
     "why": "The sound is reflected repeatedly along the tubes, reaching the "
            "ears with little loss."},
]


# ===========================================================================
# CHAPTER 4 — ELECTRICITY AND MAGNETISM  (S76 + S77 + S78)
# ===========================================================================
EM_WK_MCQ = [
    {"topic": "Law of magnetism", "q": "Two suspended magnets are brought "
     "close and they push apart. The two poles facing each other are:",
     "options": ["unlike poles", "like poles", "neutral", "one magnetic and "
                 "one not"], "correct": 1,
     "why": "Repulsion happens only between like poles."},
    {"topic": "Sure test", "q": "A steel bar attracts both ends of a compass "
     "needle but never repels either end. The bar is:",
     "options": ["a magnet", "a piece of unmagnetised iron", "copper",
                 "plastic"], "correct": 1,
     "why": "Only attraction (no repulsion) means it is unmagnetised iron — "
            "repulsion is the sure test of a magnet."},
    {"topic": "Magnetic field", "q": "The magnetic field of a bar magnet is "
     "strongest:",
     "options": ["at the centre", "near the two poles", "far from the magnet",
                 "along the normal"], "correct": 1,
     "why": "The field (and the field lines) are most crowded near the "
            "poles."},
    {"topic": "Electromagnet", "q": "The polarity (N/S) of an electromagnet "
     "can be reversed by:",
     "options": ["heating it", "reversing the direction of the current",
                 "using more turns", "removing the core"], "correct": 1,
     "why": "The direction of the current decides the poles, so reversing it "
            "swaps N and S."},
    {"topic": "Electromagnet", "q": "Which change will make an electromagnet "
     "weaker?",
     "options": ["increasing the current", "increasing the number of turns",
                 "using an air core instead of a soft-iron core", "winding the "
                 "coil tightly"], "correct": 2,
     "why": "A soft-iron core greatly strengthens the magnet; replacing it "
            "with air makes it much weaker."},
    {"topic": "Electromagnet", "q": "An electromagnet is called a temporary "
     "magnet because it:",
     "options": ["is weak", "loses its magnetism when the current stops", "is "
                 "small", "cannot lift iron"], "correct": 1,
     "why": "It is magnetic only while current flows and loses magnetism when "
            "switched off."},
    {"topic": "Uses of electromagnets", "q": "Which device does NOT use an "
     "electromagnet?",
     "options": ["an electric bell", "a scrapyard crane", "a permanent fridge "
                 "magnet", "a loudspeaker"], "correct": 2,
     "why": "A fridge magnet is a permanent magnet, not an electromagnet."},
    {"topic": "Electric bell", "q": "In an electric bell, the soft-iron piece "
     "that is attracted by the electromagnet is the:",
     "options": ["gong", "armature", "contact screw", "cell"], "correct": 1,
     "why": "The electromagnet attracts the soft-iron armature, which carries "
            "the hammer."},
    {"topic": "Declination", "q": "A freely suspended magnetic needle does not "
     "point to the exact geographic north. This shows the geographic and "
     "magnetic norths are:",
     "options": ["the same point", "slightly different", "exactly opposite",
                 "always 90° apart"], "correct": 1,
     "why": "The small angle between them (the declination) shows the two "
            "norths are at slightly different positions."},
    {"topic": "Sources of electricity", "q": "Which of the following converts "
     "chemical energy directly into electrical energy?",
     "options": ["a dynamo", "a solar cell", "an electric cell (battery)",
                 "a generator"], "correct": 2,
     "why": "A cell uses chemical reactions to produce electricity."},
    {"topic": "Sources of electricity", "q": "A solar cell is a source of "
     "electricity that uses:",
     "options": ["chemical reactions", "light energy", "magnetism", "heat "
                 "only"], "correct": 1,
     "why": "A solar cell converts light energy into electrical energy."},
    {"topic": "Cells in series", "q": "Three 1.5 V cells are joined in series "
     "in a torch. The total voltage driving the current is:",
     "options": ["1.5 V", "3.0 V", "4.5 V", "0.5 V"], "correct": 2,
     "why": "Voltages of cells in series add: 1.5 × 3 = 4.5 V."},
    {"topic": "Circuit components", "q": "In a torch circuit, the part that "
     "offers resistance and gives out light and heat is the:",
     "options": ["cell", "switch", "bulb filament", "copper connecting wire"],
     "correct": 2,
     "why": "The thin filament resists the current and glows, giving light and "
            "heat."},
    {"topic": "Conductors & insulators", "q": "The plastic coating around an "
     "electric wire is used because plastic is:",
     "options": ["a good conductor", "a good insulator", "a magnet", "a source "
                 "of current"], "correct": 1,
     "why": "Plastic is an insulator, so the coating prevents shocks and short "
            "circuits."},
    {"topic": "Electric current", "q": "The greater the number of charges "
     "passing a point in the circuit each second, the greater the:",
     "options": ["resistance", "current", "insulation", "length of wire"],
     "correct": 1,
     "why": "Current is the rate of flow of charge, so more charge per second "
            "means a larger current."},
    {"topic": "Circuit symbols", "q": "In a circuit diagram, a small gap "
     "bridged by a movable lever represents a:",
     "options": ["cell", "switch", "bulb", "resistor"], "correct": 1,
     "why": "A switch is drawn as a gap that a lever can close or open."},
    {"topic": "Series & parallel", "q": "In which arrangement is the current "
     "the same through every component?",
     "options": ["a parallel circuit", "a series circuit", "an open circuit",
                 "a short circuit"], "correct": 1,
     "why": "In a series circuit there is only one path, so the same current "
            "flows through every component."},
    {"topic": "Series & parallel", "q": "Two bulbs are connected so that "
     "removing one still leaves the other glowing. They are connected in:",
     "options": ["series", "parallel", "a single loop", "a short circuit"],
     "correct": 1,
     "why": "In parallel each bulb has its own branch, so one keeps working if "
            "the other is removed."},
    {"topic": "Series & parallel", "q": "A string of decorative lights all go "
     "out when a single bulb fails. The bulbs are wired in:",
     "options": ["parallel", "series", "two separate circuits", "a magnetic "
                 "loop"], "correct": 1,
     "why": "In series one broken bulb breaks the only path, so all the lights "
            "go out."},
    {"topic": "Precautions", "q": "Before connecting a new cell into a "
     "circuit, you should make sure the switch is:",
     "options": ["closed", "open (off)", "removed", "wet"], "correct": 1,
     "why": "Making connections with the switch off (open) is a safety "
            "precaution before switching on."},
]

EM_WK_SUBJ = [
    {"topic": "Law of magnetism & sure test", "marks": 3,
     "q": "State the law of magnetism. Why is repulsion, and not attraction, "
          "taken as the sure test of magnetism?",
     "answer": [
        "Law of magnetism: like poles repel and unlike poles attract.",
        "A magnet attracts both an unmagnetised iron piece and the opposite "
        "pole of another magnet, so attraction alone cannot prove magnetism.",
        "Only a true magnet repels the like pole of another magnet, so "
        "repulsion is the sure test."]},
    {"topic": "Electromagnet", "marks": 4,
     "q": "What is an electromagnet? State three ways to increase its strength "
          "and give two uses.",
     "answer": [
        "An electromagnet is a temporary magnet made by passing current "
        "through an insulated coil wound on a soft-iron core; it is magnetic "
        "only while current flows.",
        "Strength is increased by: increasing the current; increasing the "
        "number of turns; and using a soft-iron core.",
        "Uses: electric bells and cranes for lifting iron/scrap (also "
        "loudspeakers, telephones, separating magnetic materials)."]},
    {"topic": "Electric bell", "marks": 3,
     "q": "With reference to an electric bell, name the part that becomes an "
          "electromagnet and explain why the hammer strikes the gong again and "
          "again.",
     "answer": [
        "When current flows, the coil on the soft-iron core becomes an "
        "electromagnet and attracts the soft-iron armature, so the hammer "
        "hits the gong.",
        "This movement breaks the circuit at the contact screw, the "
        "electromagnet loses its magnetism and a spring pulls the armature "
        "back, closing the circuit again.",
        "The making and breaking repeats rapidly, so the hammer strikes the "
        "gong continuously."]},
    {"topic": "Sources & circuit", "marks": 4,
     "q": "Name two sources of electricity and the energy each converts. What "
          "is a closed circuit, and why must a circuit be closed for a bulb to "
          "glow?",
     "answer": [
        "An electric cell converts chemical energy into electrical energy; a "
        "solar cell converts light energy (a generator converts mechanical "
        "energy).",
        "A closed circuit is an unbroken conducting path from one terminal of "
        "the cell, through the components, back to the other terminal.",
        "Current can flow only round a complete path, so the bulb glows only "
        "when the circuit is closed; if it is broken (open), no current flows "
        "and the bulb stays off."]},
    {"topic": "Series vs parallel", "marks": 4,
     "q": "Distinguish between a series and a parallel circuit. Why are the "
          "cells of a torch joined in series, and why are household appliances "
          "joined in parallel?",
     "answer": [
        "Series: components are joined one after another in a single loop; the "
        "same current flows through all, and if one breaks the whole circuit "
        "stops.",
        "Parallel: each component is on its own branch, gets the full voltage "
        "and works independently.",
        "Cells in series add their voltages, giving a larger voltage to light "
        "the torch bulb brightly.",
        "Appliances in parallel each get the full mains voltage and can be "
        "switched on or off independently; if one fails the others keep "
        "working."]},
]

EM_HW_S76 = [
    {"topic": "Law of magnetism", "q": "Two unlike poles of magnets brought "
     "near each other will:",
     "options": ["repel", "attract", "do nothing", "melt"], "correct": 1,
     "why": "Unlike poles attract."},
    {"topic": "Sure test", "q": "A magnet attracts an unmagnetised iron nail, "
     "but a magnet also ___ the like pole of another magnet.",
     "options": ["attracts", "repels", "ignores", "heats"], "correct": 1,
     "why": "A magnet repels the like pole of another magnet — the sure test "
            "of magnetism."},
    {"topic": "Magnetic field", "q": "The space around a magnet where its "
     "force can be felt is the:",
     "options": ["magnetic pole", "magnetic field", "neutral point",
                 "armature"], "correct": 1,
     "why": "This region is the magnetic field."},
    {"topic": "Electromagnet", "q": "An electromagnet is made by winding "
     "insulated wire carrying current around a:",
     "options": ["copper rod", "soft-iron core", "plastic rod", "glass tube"],
     "correct": 1,
     "why": "A soft-iron core makes a strong electromagnet."},
    {"topic": "Electromagnet", "q": "The magnetism of an electromagnet "
     "disappears as soon as:",
     "options": ["it is painted", "the current is switched off", "it is "
                 "cooled", "it is moved"], "correct": 1,
     "why": "It is a temporary magnet, so its magnetism vanishes when the "
            "current stops."},
    {"topic": "Electromagnet", "q": "To make an electromagnet stronger, you "
     "can wind ___ turns of wire.",
     "options": ["fewer", "more", "no", "looser"], "correct": 1,
     "why": "More turns increase the magnetic strength."},
    {"topic": "Uses of electromagnets", "q": "A device that uses an "
     "electromagnet to lift heavy iron scrap is a:",
     "options": ["crane", "crowbar", "pulley", "lever"], "correct": 0,
     "why": "Electromagnetic cranes lift and drop iron scrap."},
    {"topic": "Electromagnet", "q": "The poles of an electromagnet can be "
     "changed by reversing the:",
     "options": ["core", "current direction", "number of turns", "colour"],
     "correct": 1,
     "why": "Reversing the current reverses the N and S poles."},
    {"topic": "Electromagnet", "q": "Which of these can an electromagnet, but "
     "not a permanent magnet, do?",
     "options": ["attract iron", "be switched on and off", "have two poles",
                 "have a magnetic field"], "correct": 1,
     "why": "An electromagnet's magnetism can be switched on and off with the "
            "current."},
    {"topic": "Law of magnetism", "q": "When the like poles of two magnets are "
     "brought together, the force between them is one of:",
     "options": ["attraction", "repulsion", "no force", "gravity"],
     "correct": 1,
     "why": "Like poles repel."},
]

EM_HW_S77 = [
    {"topic": "Electric bell", "q": "The hammer of an electric bell is fixed "
     "to a soft-iron strip called the:",
     "options": ["gong", "armature", "coil", "cell"], "correct": 1,
     "why": "The hammer is carried by the armature."},
    {"topic": "Electric bell", "q": "An electric bell mainly converts "
     "electrical energy into ___ energy.",
     "options": ["light", "sound", "chemical", "magnetic only"], "correct": 1,
     "why": "The ringing bell gives out sound energy."},
    {"topic": "Compass", "q": "A magnetic compass is used to find:",
     "options": ["temperature", "geographic direction (north–south)",
                 "current", "weight"], "correct": 1,
     "why": "A compass needle sets north–south, showing direction."},
    {"topic": "Declination", "q": "The geographic north and the magnetic north "
     "of the Earth are:",
     "options": ["exactly the same", "at slightly different positions",
                 "always 90° apart", "at the equator"], "correct": 1,
     "why": "They differ slightly; the angle between them is the "
            "declination."},
    {"topic": "Sources of electricity", "q": "A dry cell converts ___ energy "
     "into electrical energy.",
     "options": ["light", "chemical", "heat", "sound"], "correct": 1,
     "why": "A dry cell uses chemical reactions to make electricity."},
    {"topic": "Cells in series", "q": "In a torch, two or more cells are "
     "joined end to end (positive to negative). This is a ___ connection.",
     "options": ["parallel", "series", "short", "open"], "correct": 1,
     "why": "Cells joined end to end are in series, adding their voltages."},
    {"topic": "Circuit", "q": "For the torch bulb to glow, the switch must "
     "be:",
     "options": ["open", "closed (on)", "removed", "reversed"], "correct": 1,
     "why": "A closed switch completes the circuit so current flows."},
    {"topic": "Conductors", "q": "Which of these is a good conductor of "
     "electricity?",
     "options": ["rubber", "copper", "glass", "dry wood"], "correct": 1,
     "why": "Copper is a good conductor, used for wires."},
    {"topic": "Insulators", "q": "Which of these is an insulator used to cover "
     "electric wires?",
     "options": ["aluminium", "plastic", "iron", "silver"], "correct": 1,
     "why": "Plastic is an insulator and is used as wire covering."},
    {"topic": "Sources of electricity", "q": "A rooftop solar panel is a "
     "source of electricity that uses energy from the:",
     "options": ["wind", "Sun (light)", "sea", "ground"], "correct": 1,
     "why": "Solar panels use the Sun's light energy."},
]

EM_HW_S78 = [
    {"topic": "Electric current", "q": "An electric current is the flow of "
     "tiny charged particles called:",
     "options": ["atoms", "electrons (charges)", "protons only", "photons"],
     "correct": 1,
     "why": "Current in a metal wire is a flow of electrons (charges)."},
    {"topic": "Current direction", "q": "Conventional current is taken to flow "
     "in the circuit from the ___ terminal of the cell.",
     "options": ["negative", "positive", "central", "earth"], "correct": 1,
     "why": "Conventional current flows from the positive terminal, round the "
            "circuit, to the negative."},
    {"topic": "Circuit symbols", "q": "In a circuit diagram, a small circle "
     "with a cross inside stands for a:",
     "options": ["cell", "lamp (bulb)", "switch", "wire"], "correct": 1,
     "why": "The crossed circle is the symbol for a lamp/bulb."},
    {"topic": "Circuit symbols", "q": "A gap in a circuit diagram bridged by a "
     "movable lever represents a:",
     "options": ["cell", "switch", "bulb", "resistor"], "correct": 1,
     "why": "That symbol is a switch, which opens or closes the circuit."},
    {"topic": "Series & parallel", "q": "Components joined one after another in "
     "a single path are connected in:",
     "options": ["parallel", "series", "a branch", "a short"], "correct": 1,
     "why": "One-after-another in a single path is a series connection."},
    {"topic": "Series & parallel", "q": "In a series circuit, the current "
     "through each component is:",
     "options": ["different", "the same", "zero", "doubled"], "correct": 1,
     "why": "There is only one path, so the same current flows everywhere."},
    {"topic": "Series & parallel", "q": "In a parallel circuit, if one branch "
     "is switched off, the other branches:",
     "options": ["also switch off", "keep working", "burn out", "reverse"],
     "correct": 1,
     "why": "Each branch is independent, so the others keep working."},
    {"topic": "Series & parallel", "q": "If removing one bulb from a string "
     "makes all the others go out, the bulbs were connected in:",
     "options": ["parallel", "series", "two circuits", "a magnet"],
     "correct": 1,
     "why": "In series one break stops the whole circuit."},
    {"topic": "Precautions", "q": "Before switching on a newly made circuit, "
     "you should check that all connections are:",
     "options": ["loose", "tight and correct", "wet", "hot"], "correct": 1,
     "why": "Tight, correct connections prevent sparks and faults."},
    {"topic": "Conductors", "q": "The wires and terminals of a circuit are "
     "made of conductors so that they:",
     "options": ["stop the current", "let the current pass easily", "insulate "
                 "the circuit", "store charge"], "correct": 1,
     "why": "Conductors let current flow easily round the circuit."},
]

EM_HW_WK = [
    {"topic": "Sure test", "q": "The sure test that a given bar is a magnet is "
     "that it shows ___ with the like pole of another magnet.",
     "options": ["attraction", "repulsion", "no effect", "heating"],
     "correct": 1,
     "why": "Repulsion proves it is a magnet; attraction alone does not."},
    {"topic": "Electromagnet", "q": "Reversing the current in an electromagnet "
     "reverses its:",
     "options": ["strength", "poles (N and S)", "core", "number of turns"],
     "correct": 1,
     "why": "Current direction sets the poles, so reversing it swaps them."},
    {"topic": "Uses of electromagnets", "q": "An electromagnet is preferred in "
     "a crane because, unlike a permanent magnet, it can:",
     "options": ["lift wood", "be switched on to grip and off to release the "
                 "load", "work without a core", "never lose magnetism"],
     "correct": 1,
     "why": "Switching the current off releases the load — a permanent magnet "
            "could not."},
    {"topic": "Sources of electricity", "q": "A cell is a source of "
     "electricity that changes ___ energy into electrical energy.",
     "options": ["light", "chemical", "sound", "magnetic"], "correct": 1,
     "why": "A cell converts chemical energy into electrical energy."},
    {"topic": "Cells in series", "q": "Three 2 V cells joined in series give a "
     "total of:",
     "options": ["2 V", "6 V", "0.67 V", "8 V"], "correct": 1,
     "why": "Series voltages add: 2 × 3 = 6 V."},
    {"topic": "Circuit components", "q": "The thin wire inside a bulb that "
     "glows is the:",
     "options": ["terminal", "filament", "switch", "fuse"], "correct": 1,
     "why": "The filament resists the current and glows."},
    {"topic": "Circuit symbols", "q": "In a circuit diagram, a cell is shown "
     "by:",
     "options": ["a circle with a cross", "one long line and one short line",
                 "a zig-zag", "a triangle"], "correct": 1,
     "why": "A cell is drawn as a long thin line (+) and a short thick line "
            "(−)."},
    {"topic": "Series & parallel", "q": "Components on separate branches, each "
     "getting the full voltage, are connected in:",
     "options": ["series", "parallel", "a single loop", "a short circuit"],
     "correct": 1,
     "why": "Separate branches at full voltage is a parallel connection."},
    {"topic": "Series & parallel", "q": "In a series circuit of three bulbs, "
     "removing one bulb makes the others:",
     "options": ["glow brighter", "go out", "stay the same", "reverse"],
     "correct": 1,
     "why": "Removing one bulb breaks the single path, so all go out."},
    {"topic": "Precautions", "q": "A safe precaution before switching on a "
     "circuit is to keep the switch ___ while making the connections.",
     "options": ["closed", "open (off)", "wet", "hot"], "correct": 1,
     "why": "Connecting with the switch open prevents accidental current and "
            "sparks."},
]


# ===========================================================================
# BUILD
# ===========================================================================
WORKOUTS = [
    dict(file="G07_Light_Energy_Workout.pptx", chapter="Light Energy",
         accent=C["orange"], title="Light Energy — Workout",
         subtitle="Practice covering Light Energy Lessons 1 & 2",
         syllabus=[
             ("Light Energy 1", "Reflection of light, plane mirror, terms, "
              "laws of reflection and their verification, normal incidence, "
              "image formation by a plane mirror."),
             ("Light Energy 2", "Real & virtual images, lateral inversion, "
              "characteristics of the image, regular & irregular reflection, "
              "uses of plane mirrors, speed of light, primary & secondary "
              "colours, subtraction of colours.")],
         mcqs=LE_WK_MCQ, subj=LE_WK_SUBJ,
         closing="Revise the laws of reflection, plane-mirror image "
                 "characteristics, and the addition & subtraction of colours."),
    dict(file="G07_Heat_Workout.pptx", chapter="Heat",
         accent=C["red"], title="Heat — Workout",
         subtitle="Practice covering Heat Lessons 1, 2 & 3",
         syllabus=[
             ("Heat 1", "Heat as energy, units of heat, temperature, units & "
              "scales of temperature, measurement of temperature."),
             ("Heat 2", "Effects of heat and thermal expansion of solids, "
              "liquids and gases."),
             ("Heat 3", "Conduction, convection and radiation; conductors & "
              "insulators; black/white surfaces; the thermos flask.")],
         mcqs=HT_WK_MCQ, subj=HT_WK_SUBJ,
         closing="Practise the temperature conversions and revise the three "
                 "modes of heat transfer and the thermos flask."),
    dict(file="G07_Sound_Workout.pptx", chapter="Sound",
         accent=C["blue"], title="Sound — Workout",
         subtitle="Practice covering Sound Lessons 1 & 2",
         syllabus=[
             ("Sound 1", "Production of sound by vibrations, sources of sound, "
              "the need for a medium, longitudinal waves in air."),
             ("Sound 2", "Wave terms, audible/ultrasonic/infrasonic sound, "
              "characteristics of sound, speed of sound, reflection & "
              "absorption of sound.")],
         mcqs=SO_WK_MCQ, subj=SO_WK_SUBJ,
         closing="Revise the wave relation v = f λ, the audible range, and the "
                 "echo/SONAR numericals."),
    dict(file="G07_Electricity_and_Magnetism_Workout.pptx",
         chapter="Electricity and Magnetism", accent=C["purple"],
         title="Electricity & Magnetism — Workout",
         subtitle="Practice covering Electricity & Magnetism Lessons 1, 2 & 3",
         syllabus=[
             ("Electricity & Magnetism 1", "Law of magnetism, repulsion as the "
              "sure test, magnetic field, electromagnet and its uses."),
             ("Electricity & Magnetism 2", "Electric bell, magnetic "
              "declination, sources of electricity, dry cells in a torch, flow "
              "in a circuit, conductors & insulators."),
             ("Electricity & Magnetism 3", "Charges as current, circuit "
              "symbols & functions, series & parallel circuits, safety "
              "precautions.")],
         mcqs=EM_WK_MCQ, subj=EM_WK_SUBJ,
         closing="Revise the sure test of magnetism, the electric bell, and "
                 "the difference between series and parallel circuits."),
]

HOMEWORKS = [
    dict(file="G07_S37_Light_Energy_1_Homework.pdf", chapter="Light Energy",
         lesson="Lesson 1", kind="Concept",
         syllabus="Reflection of light, plane mirror, terms related to "
                  "reflection, laws of reflection and their verification, "
                  "normal incidence, formation of image by a plane mirror.",
         mcqs=LE_HW_S37),
    dict(file="G07_S38_Light_Energy_2_Homework.pdf", chapter="Light Energy",
         lesson="Lesson 2", kind="Concept",
         syllabus="Real & virtual images, lateral inversion, characteristics "
                  "of a plane-mirror image, regular & irregular reflection, "
                  "uses of plane mirrors, speed of light, primary & secondary "
                  "colours, subtraction of colours.",
         mcqs=LE_HW_S38),
    dict(file="G07_Light_Energy_Workout_Homework.pdf", chapter="Light Energy",
         lesson="Workout", kind="Workout",
         syllabus="Whole chapter: reflection and its laws, plane-mirror "
                  "images, regular/diffuse reflection, speed of light, and the "
                  "addition & subtraction of colours.",
         mcqs=LE_HW_WK),
    dict(file="G07_S55_Heat_1_Homework.pdf", chapter="Heat",
         lesson="Lesson 1", kind="Concept",
         syllabus="Heat as a form of energy, units of heat, temperature, units "
                  "& scales of temperature, measurement of temperature.",
         mcqs=HT_HW_S55),
    dict(file="G07_S56_Heat_2_Homework.pdf", chapter="Heat",
         lesson="Lesson 2", kind="Concept",
         syllabus="Effects of heat and thermal expansion of solids, liquids "
                  "and gases.",
         mcqs=HT_HW_S56),
    dict(file="G07_S57_Heat_3_Homework.pdf", chapter="Heat",
         lesson="Lesson 3", kind="Concept",
         syllabus="Three modes of heat transfer (conduction, convection, "
                  "radiation), conductors & insulators, black/white surfaces, "
                  "the thermos flask.",
         mcqs=HT_HW_S57),
    dict(file="G07_Heat_Workout_Homework.pdf", chapter="Heat",
         lesson="Workout", kind="Workout",
         syllabus="Whole chapter: heat and temperature, scales and "
                  "conversions, thermal expansion, and conduction, convection "
                  "and radiation.",
         mcqs=HT_HW_WK),
    dict(file="G07_S66_Sound_1_Homework.pdf", chapter="Sound",
         lesson="Lesson 1", kind="Concept",
         syllabus="Production of sound by vibrations, sources of sound, the "
                  "need for a material medium, longitudinal waves in air.",
         mcqs=SO_HW_S66),
    dict(file="G07_S67_Sound_2_Homework.pdf", chapter="Sound",
         lesson="Lesson 2", kind="Concept",
         syllabus="Wave terms, audible/ultrasonic/infrasonic sound, "
                  "characteristics of sound, speed of sound, reflection & "
                  "absorption of sound.",
         mcqs=SO_HW_S67),
    dict(file="G07_Sound_Workout_Homework.pdf", chapter="Sound",
         lesson="Workout", kind="Workout",
         syllabus="Whole chapter: production and propagation of sound, wave "
                  "terms and v = f λ, classification by frequency, "
                  "characteristics, echoes and SONAR.",
         mcqs=SO_HW_WK),
    dict(file="G07_S76_Electricity_and_Magnetism_1_Homework.pdf",
         chapter="Electricity and Magnetism", lesson="Lesson 1", kind="Concept",
         syllabus="Law of magnetism, repulsion as the sure test, magnetic "
                  "field, electromagnet, making an electromagnet and its "
                  "uses.",
         mcqs=EM_HW_S76),
    dict(file="G07_S77_Electricity_and_Magnetism_2_Homework.pdf",
         chapter="Electricity and Magnetism", lesson="Lesson 2", kind="Concept",
         syllabus="Electric bell, magnetic declination, sources of "
                  "electricity, dry cells in a torch, flow of electricity in a "
                  "circuit, conductors & insulators.",
         mcqs=EM_HW_S77),
    dict(file="G07_S78_Electricity_and_Magnetism_3_Homework.pdf",
         chapter="Electricity and Magnetism", lesson="Lesson 3", kind="Concept",
         syllabus="Charges constituting current, circuit symbols & functions, "
                  "series & parallel circuits, safety precautions before "
                  "switching on.",
         mcqs=EM_HW_S78),
    dict(file="G07_Electricity_and_Magnetism_Workout_Homework.pdf",
         chapter="Electricity and Magnetism", lesson="Workout", kind="Workout",
         syllabus="Whole chapter: magnetism and the sure test, electromagnets "
                  "and their uses, sources of electricity, cells in series, "
                  "circuit symbols, and series & parallel circuits.",
         mcqs=EM_HW_WK),
]


def build():
    return build_grade(grade=GRADE, wk_out=WK_OUT, hw_out=HW_OUT,
                       concept_dir=CONCEPT_DIR, workouts=WORKOUTS,
                       homeworks=HOMEWORKS)


if __name__ == "__main__":
    build()
