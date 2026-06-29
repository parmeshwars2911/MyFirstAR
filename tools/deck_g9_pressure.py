"""
Grade 9 Physics — Chapter: Pressure in Fluids and Atmospheric Pressure.
S39 (thrust & pressure, liquid pressure, laws, Pascal's law) and
S40 (hydraulic machines, atmospheric pressure, barometer, altitude).
ICSE Class 9 (Selina) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade09"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Pressure in Fluids & Atmospheric Pressure  •  ICSE Class 9 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    liq = b.asset("g9pr_liquid", D.liquid_pressure("g9pr_liquid"))
    hyd = b.asset("g9pr_hyd", D.hydraulic_press("g9pr_hyd"))
    hero = b.asset("g9_pressure_hero", liq)

    b.title("ICSE • Class 9 • Fluids", "Pressure in Fluids",
            "Thrust & pressure  •  Pressure in a liquid  •  Laws of liquid "
            "pressure  •  Pascal's law", img=hero)
    b.objectives([
        "Distinguish thrust from pressure",
        "Use the relation pressure = thrust / area",
        "Find the pressure due to a liquid column (P = h ρ g)",
        "State the laws of liquid pressure",
        "Explain everyday consequences of liquid pressure",
        "State Pascal's law and its applications",
    ])
    b.divider(1, "Part 1", "Thrust & Pressure in Liquids",
              "How liquids press on their surroundings")
    b.statement("THRUST & PRESSURE", "Thrust and Pressure",
                "Thrust is the total force acting normally on a surface; "
                "pressure is the thrust acting on each unit of area.",
                formula="Pressure  =  Thrust / Area        (unit: pascal, Pa)",
                points=["Thrust is a force, measured in newtons (N).",
                        "1 pascal = 1 newton per square metre (N/m²).",
                        "The same force gives more pressure on a smaller "
                        "area — why a sharp knife cuts well."],
                notes="Separate thrust (force) from pressure (force per area). "
                      "The sharp-knife / camel-foot examples make area "
                      "intuitive.")
    b.worked("WORKED EXAMPLE", "Pressure From a Force",
             "A box exerts a thrust of 600 N on the floor through a base area "
             "of 1.5 m². Find the pressure on the floor.",
             ["Pressure = Thrust / Area",
              "Pressure = 600 / 1.5",
              "Pressure = 400 Pa"],
             "Pressure = 400 Pa",
             notes="Straight substitution. Note how a smaller base area would "
                   "raise the pressure for the same weight.")
    b.text_image("LIQUID COLUMN", "Pressure in a Liquid",
                 ["A liquid exerts pressure because of its weight.",
                  "The pressure at a depth h is P = h ρ g (depth × density × "
                  "g).",
                  "So pressure increases with depth — deeper water presses "
                  "harder.",
                  "It does not depend on the area or shape of the container."],
                 liq, img_side="right", img_w=5.6, img_h=3.8,
                 panel_title="P = h ρ g",
                 caption="Deeper holes squirt water further",
                 notes="Derive P = hρg from the weight of the column. Stress it "
                       "depends on depth and density, not on the container's "
                       "shape.")
    b.cards("LAWS", "Laws of Liquid Pressure", [
        ("Increases with depth", "The deeper you go, the greater the "
         "pressure."),
        ("Same at the same depth", "At a given depth the pressure is the same "
         "in all directions."),
        ("Acts in all directions", "A liquid presses sideways and upwards, not "
         "just downwards."),
        ("Depends on density", "A denser liquid exerts more pressure at the "
         "same depth."),
    ], notes="The four laws. The 'all directions' and 'same at same depth' "
             "points are commonly tested.")
    b.statement("TOTAL PRESSURE", "Total Pressure at a Depth",
                "The total pressure at a depth in an open liquid is the "
                "atmospheric pressure pushing on the surface plus the pressure "
                "of the liquid column.",
                formula="P_total  =  P_atmospheric  +  h ρ g",
                points=["The liquid column adds hρg to the air pressure above "
                        "it.",
                        "The deeper the point, the larger the hρg term.",
                        "If only the liquid's own pressure is wanted, use just "
                        "h ρ g."],
                notes="Distinguish gauge pressure (hρg) from total/absolute "
                      "pressure (atmospheric + hρg). Exam questions specify "
                      "which they want.")
    b.cards("OWN LEVEL", "Liquids Find Their Own Level", [
        ("Communicating vessels", "Liquid poured into connected vessels "
         "settles at the same height in each."),
        ("Why", "At the joining level the pressure must be equal, and equal "
         "pressure means equal height (same liquid)."),
        ("Whatever the shape", "It is true however wide, narrow or tilted each "
         "vessel is."),
        ("Everyday use", "Water-level tubes, canal locks and a spirit level "
         "all rely on this."),
    ], notes="Communicating vessels: a liquid reaches the same level "
             "everywhere because pressure balances at a common depth.")
    b.cards("CONSEQUENCES", "Consequences of Liquid Pressure", [
        ("Thick dam walls", "Dams are built much thicker at the bottom to "
         "withstand the greater pressure there."),
        ("Deep-sea diving", "Divers need strong suits because pressure grows "
         "rapidly with depth."),
        ("Water tank height", "An overhead tank gives more pressure (and flow) "
         "the higher it is placed."),
        ("Holes in a can", "Water spurts farthest from the lowest hole in a "
         "tin."),
    ], notes="Each consequence follows from 'pressure increases with depth'. "
             "The dam wall is the classic exam example.")
    b.bullets("ALL DIRECTIONS", "Liquids Press in Every Direction", [
        ("Sideways too", "A liquid pushes outward on the walls of its "
         "container, not just downward — water spurts sideways from a hole."),
        ("Upward as well", "Liquid pressure also acts upward, which is why "
         "objects feel an upthrust."),
        ("Equal at one depth", "At a given depth the pressure is the same in "
         "all directions."),
        ("Free surface stays level", "Because pressure balances, the surface "
         "of a still liquid is always horizontal."),
    ], panel_title="Pressure has no preferred direction",
       notes="Reinforce that liquid pressure acts in all directions — leads "
             "naturally to upthrust in the next chapter.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Sharp Knife", "A sharp knife cuts more easily than a blunt "
             "one because, for the same force, the sharp edge gives:",
             ["Less pressure (larger area)", "More pressure (smaller area)",
              "Less thrust", "More thrust"])
    b.quiz_a(1, "B. More pressure (smaller area)",
             "Pressure = thrust / area. A sharp edge has a very small contact "
             "area, so the same force produces a much greater pressure, "
             "letting it cut.")
    b.quiz_q(2, "Dam Design", "The wall of a dam is made much thicker at its "
             "base than at the top because the water pressure:",
             ["Is greatest at the top", "Increases with depth, so it is "
              "greatest at the bottom", "Is the same everywhere",
              "Acts only sideways"])
    b.quiz_a(2, "B. Increases with depth",
             "Liquid pressure rises with depth (P = hρg), so the base of the "
             "dam must resist the greatest pressure — hence it is built "
             "thickest there.")
    b.quiz_q(3, "Which Depth?", "Two tanks hold water. The pressure at the "
             "bottom depends on:", ["The width of the tank",
              "The total amount of water", "The depth of the water (and its "
              "density)", "The shape of the tank"])
    b.quiz_a(3, "C. The depth of the water (and its density)",
             "Liquid pressure depends only on depth, density and g — not on "
             "the shape, width or total volume. Two differently shaped tanks "
             "filled to the same depth have the same bottom pressure.")
    b.quiz_q(4, "Find the Pressure", "The pressure due to a 2 m column of "
             "water (ρ = 1000 kg/m³, g = 10 m/s²) is:",
             ["200 Pa", "2000 Pa", "20,000 Pa", "5000 Pa"])
    b.quiz_a(4, "C. 20,000 Pa",
             "P = h ρ g = 2 × 1000 × 10 = 20,000 Pa. Multiply depth, density "
             "and g.")
    b.quiz_q(5, "Same Level", "A liquid is poured into a set of connected "
             "tubes of different widths and shapes. The liquid settles so "
             "that:", ["It is highest in the narrowest tube",
              "It reaches the same level in every tube",
              "It is highest in the widest tube",
              "Each tube has a different level"])
    b.quiz_a(5, "B. It reaches the same level in every tube",
             "In communicating vessels the pressure must balance at the "
             "joining level, so the same liquid stands at the same height in "
             "each — regardless of the tubes' shapes or widths.")
    b.divider(2, "Part 2", "Pascal's Law",
              "How pressure is transmitted through liquids")
    b.text_image("PASCAL'S LAW", "Transmission of Pressure",
                 ["Pascal's law: pressure applied to an enclosed liquid is "
                  "transmitted equally to every part of it.",
                  "So a small force on a small piston can balance a large "
                  "force on a large piston.",
                  "The pressure (f/a) is the same as (F/A) throughout the "
                  "liquid.",
                  "This multiplies force — the basis of all hydraulic "
                  "machines."],
                 hyd, img_side="left", img_w=6.0, img_h=3.6,
                 panel_title="f / a = F / A",
                 caption="A small force lifts a big load",
                 notes="State Pascal's law. The force is multiplied by the "
                       "ratio of piston areas — hydraulics trade distance for "
                       "force.")
    b.worked("WORKED EXAMPLE", "Hydraulic Force Multiplier",
             "In a hydraulic press a force of 50 N acts on a piston of area "
             "0.01 m². The large piston has area 0.5 m². Find the force it "
             "can exert.",
             ["f / a = F / A   →   F = f × A / a",
              "F = 50 × 0.5 / 0.01",
              "F = 2500 N"],
             "F = 2500 N — the force is multiplied 50 times",
             notes="The area ratio (0.5/0.01 = 50) is the force multiplier. "
                   "Great for showing the power of hydraulics.")
    b.cards("APPLICATIONS", "Applications of Pascal's Law", [
        ("Hydraulic press", "Compresses bales, moulds metal and presses oil "
         "from seeds."),
        ("Hydraulic brakes", "A light push on the brake pedal presses the "
         "brake pads on all wheels."),
        ("Hydraulic lift / jack", "Lifts cars and heavy loads with a small "
         "effort."),
        ("Excavators", "Hydraulic arms move huge buckets of earth."),
    ], notes="Each device transmits pressure to multiply force. Brakes and the "
             "car jack are the everyday examples.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Thrust vs pressure", "thrust is force; pressure = thrust / area (Pa)"),
        ("Liquid pressure", "P = h ρ g; increases with depth"),
        ("Laws", "acts in all directions; same at the same depth"),
        ("Consequences", "thick dam walls, deep-sea pressure"),
        ("Pascal's law", "pressure is transmitted equally; f/a = F/A"),
        ("Applications", "hydraulic press, brakes, lift and jack"),
    ], notes="Rapid recap; P = hρg and Pascal's law are the key results.")
    b.quiz_intro("Quiz 2", "Final Check — Pascal & Hydraulics", 5)
    b.quiz_q(1, "Pascal's Law", "Pascal's law states that pressure applied to "
             "an enclosed liquid is:", ["Lost as heat",
              "Transmitted equally to every part of the liquid",
              "Greatest near the piston", "Reduced with distance"])
    b.quiz_a(1, "B. Transmitted equally to every part",
             "An enclosed liquid passes on the applied pressure undiminished "
             "to all points. This equal transmission is what hydraulic "
             "machines rely on.")
    b.quiz_q(2, "Force Multiplier", "A hydraulic lift has pistons of area "
             "2 cm² and 100 cm². A force of 20 N on the small piston can lift "
             "a load of:", ["20 N", "100 N", "1000 N", "400 N"])
    b.quiz_a(2, "C. 1000 N",
             "F = f × A/a = 20 × 100/2 = 1000 N. The area ratio of 50 "
             "multiplies the force 50 times.")
    b.quiz_q(3, "Brakes", "When you press a car's brake pedal, the braking "
             "force reaches all the wheels because the brake fluid:",
             ["Evaporates", "Transmits the pressure equally to each wheel "
              "cylinder", "Heats up", "Freezes"])
    b.quiz_a(3, "B. Transmits the pressure equally",
             "The enclosed brake fluid obeys Pascal's law, carrying the "
             "pressure from the pedal equally to the cylinders at every wheel "
             "so they brake together.")
    b.quiz_q(4, "No Free Lunch", "A hydraulic jack multiplies force 50 times. "
             "To lift the load, the small piston must move:",
             ["The same distance as the load", "50 times further than the "
              "load rises", "50 times less than the load",
              "It does not move"])
    b.quiz_a(4, "B. 50 times further than the load rises",
             "Energy is conserved: gaining 50× the force costs 50× the "
             "distance. The small piston moves a long way to raise the load a "
             "little — work in equals work out.")
    b.quiz_q(5, "Same Liquid Level", "An enclosed hydraulic system is filled "
             "with oil rather than air because a liquid:",
             ["Is lighter", "Is almost incompressible, so it transmits "
              "pressure without being squashed", "Is cheaper",
              "Flows faster"])
    b.quiz_a(5, "B. Is almost incompressible",
             "A liquid barely compresses, so applied pressure is passed on at "
             "once. A gas would simply compress, absorbing the effort instead "
             "of transmitting it.")
    b.closing("The Power of Pressure",
              "From a dam wall to a car's brakes, understanding fluid pressure "
              "lets us hold back oceans and multiply force at will.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    bar = b.asset("g9pr_baro", D.barometer("g9pr_baro"))
    hyd = b.asset("g9pr_hyd2", D.hydraulic_press("g9pr_hyd2"))
    hero = b.asset("g9_atmosphere_hero", bar)

    b.title("ICSE • Class 9 • Fluids", "Atmospheric Pressure",
            "Hydraulic machines  •  Atmospheric pressure  •  The barometer  •  "
            "Pressure & altitude", img=hero)
    b.objectives([
        "Give examples of hydraulic machines",
        "Explain what atmospheric pressure is",
        "Describe demonstrations of atmospheric pressure",
        "List everyday consequences of atmospheric pressure",
        "Describe how a barometer measures atmospheric pressure",
        "Explain how pressure varies with altitude",
    ])
    b.divider(1, "Part 1", "Hydraulic Machines & the Atmosphere",
              "Multiplying force, and the ocean of air above us")
    b.text_image("HYDRAULICS", "Hydraulic Machines",
                 ["Hydraulic machines use Pascal's law to multiply force.",
                  "A small force on a small piston produces a large force on a "
                  "large piston.",
                  "Examples: hydraulic press, car brakes, jacks and "
                  "excavators.",
                  "They trade a long movement of the small piston for a large "
                  "force on the load."],
                 hyd, img_side="left", img_w=6.0, img_h=3.6,
                 panel_title="Force multipliers",
                 caption="A small effort raises a heavy load",
                 notes="Recap hydraulics from the previous lesson as the lead-"
                       "in, then move to the atmosphere.")
    b.statement("ATMOSPHERIC PRESSURE", "Atmospheric Pressure",
                "The atmosphere is a deep ocean of air whose weight presses on "
                "everything — this is atmospheric pressure.",
                formula="Normal value ≈ 1.013 × 10⁵ Pa (≈ 76 cm of mercury)",
                points=["It acts in all directions, like any fluid pressure.",
                        "We do not feel it because it is balanced by the "
                        "pressure inside our bodies.",
                        "It decreases as we go up, where there is less air "
                        "above."],
                notes="Air has weight, so it presses on us. We don't feel it "
                      "because internal pressure balances it.")
    b.cards("DEMONSTRATIONS", "Showing Atmospheric Pressure Exists", [
        ("Crushing can", "Steam is boiled in a can, then it is sealed and "
         "cooled — the air pressure outside crushes it."),
        ("Magdeburg hemispheres", "Two evacuated hemispheres cannot be pulled "
         "apart, held by air pressure."),
        ("Water in a glass", "A card holds water in an inverted glass — air "
         "pressure pushes up on the card."),
        ("Rubber sucker", "Squeeze out the air and atmospheric pressure holds "
         "the sucker to the wall."),
    ], notes="Classic demonstrations. Each works because air pressure pushes "
             "from outside when the inside pressure is reduced.")
    b.cards("CONSEQUENCES", "Atmospheric Pressure in Daily Life", [
        ("Drinking straw", "Sucking lowers the pressure inside; air pressure "
         "pushes the drink up the straw."),
        ("Syringe", "Pulling the plunger lets atmospheric pressure push liquid "
         "in."),
        ("Dropper", "Releasing the bulb lets air pressure push liquid up into "
         "it."),
        ("Pumps", "Lift and force pumps move water using pressure "
         "differences."),
    ], notes="Everyday uses. Stress the pattern: reduce pressure on one side, "
             "and atmospheric pressure does the pushing.")
    b.bullets("UNITS", "Ways of Stating Atmospheric Pressure", [
        ("Pascal (Pa)", "The SI unit; normal atmospheric pressure ≈ "
         "1.013 × 10⁵ Pa."),
        ("Centimetres of mercury", "Normal pressure supports 76 cm (760 mm) "
         "of mercury."),
        ("Atmosphere (atm)", "1 atm is the average sea-level pressure."),
        ("Bar / millibar", "Weather maps often use millibars; 1 bar ≈ "
         "10⁵ Pa."),
    ], panel_title="One pressure, several units",
       notes="Connect the units students will meet: pascals, cm of mercury, "
             "atmospheres and millibars on weather maps.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "The Straw", "When you drink through a straw, the drink rises "
             "because:", ["You pull the liquid up with suction force",
              "Lowering the pressure inside lets atmospheric pressure push the "
              "drink up", "The straw heats the liquid", "Gravity pushes it "
              "up"])
    b.quiz_a(1, "B. Atmospheric pressure pushes the drink up",
             "Sucking removes air from the straw, lowering the pressure "
             "inside. The greater atmospheric pressure on the drink's surface "
             "then pushes the liquid up the straw.")
    b.quiz_q(2, "Crushing Can", "A sealed can with a little steam inside is "
             "cooled and suddenly crumples because:",
             ["The steam expands", "The steam condenses, lowering the inside "
              "pressure so the atmosphere crushes it", "The metal shrinks a "
              "lot", "Water freezes inside"])
    b.quiz_a(2, "B. Steam condenses, so the atmosphere crushes it",
             "Cooling condenses the steam, drastically lowering the pressure "
             "inside the can. The unbalanced atmospheric pressure outside then "
             "crushes it.")
    b.quiz_q(3, "Why No Squash?", "We are not crushed by the huge atmospheric "
             "pressure on us because:", ["Our skin is very strong",
              "The pressure of fluids inside our bodies balances it",
              "Atmospheric pressure is actually small", "We are too light"])
    b.quiz_a(3, "B. Internal pressure balances it",
             "The pressure of the blood and fluids inside our bodies pushes "
             "outward with equal force, balancing the atmospheric pressure "
             "pushing in — so there is no net squeezing.")
    b.quiz_q(4, "Hydraulic Recap", "Hydraulic machines are able to multiply "
             "force because they use:", ["Atmospheric pressure",
              "Pascal's law — equal transmission of pressure in a liquid",
              "The weight of air", "Magnetism"])
    b.quiz_a(4, "B. Pascal's law",
             "Hydraulics rely on a liquid transmitting pressure equally "
             "(Pascal's law); the larger output piston then turns that "
             "pressure into a much larger force.")
    b.quiz_q(5, "Sucker on Glass", "A rubber sucker sticks firmly to a smooth "
             "wall because:", ["Glue on the sucker holds it",
              "Squeezing out the air lets atmospheric pressure hold it on",
              "It is magnetic", "The wall pulls it"])
    b.quiz_a(5, "B. Atmospheric pressure holds it on",
             "Pressing the sucker drives out the air behind it. With little "
             "pressure inside, the full atmospheric pressure outside presses "
             "it against the wall and holds it there.")
    b.divider(2, "Part 2", "Measuring Atmospheric Pressure",
              "The barometer, altitude and the weather")
    b.text_image("BAROMETER", "The Mercury Barometer",
                 ["A barometer measures atmospheric pressure.",
                  "Atmospheric pressure supports a column of mercury about "
                  "76 cm high in a sealed tube.",
                  "Above the mercury is a vacuum (the Torricellian vacuum).",
                  "Mercury is used because it is very dense — water would need "
                  "a 10 m tube!"],
                 bar, img_side="right", img_w=4.6, img_h=4.0,
                 panel_title="76 cm of mercury",
                 caption="Atmospheric pressure supports the column",
                 notes="Explain the balance: atmospheric pressure on the "
                       "trough equals the pressure of the 76 cm mercury "
                       "column. Mercury's density keeps it compact.")
    b.bullets("MANOMETER", "The Manometer — Measuring Gas Pressure", [
        ("What it is", "A simple U-tube containing a liquid, used to measure "
         "the pressure of an enclosed gas."),
        ("How it reads", "The gas pushes the liquid down one arm; the "
         "difference in levels gives the pressure."),
        ("Above atmospheric", "If the gas arm is lower, the gas pressure is "
         "greater than the atmosphere by hρg."),
        ("Below atmospheric", "If the gas arm is higher, the gas pressure is "
         "less than the atmosphere."),
    ], panel_title="A U-tube pressure gauge",
       notes="The manometer compares an enclosed gas pressure with the "
             "atmosphere via the difference in liquid levels (hρg).")
    b.bullets("ALTITUDE", "Pressure and Altitude", [
        ("Falls with height", "Atmospheric pressure decreases as you go "
         "higher — there is less air above."),
        ("On mountains", "Climbers carry oxygen because the thin air has low "
         "pressure."),
        ("Aircraft cabins", "Planes are pressurised because the outside "
         "pressure is very low at altitude."),
        ("Boiling point", "Water boils below 100°C high up, where pressure is "
         "lower."),
    ], panel_title="Less air above means less pressure",
       notes="Pressure drops with altitude. Link to oxygen on mountains and "
             "lower boiling points high up.")
    b.cards("WEATHER & ALTIMETER", "Using the Barometer", [
        ("Weather forecasting", "A rising barometer suggests fair weather; a "
         "falling one warns of storms or rain."),
        ("Altimeter", "An aneroid barometer marked in height measures "
         "altitude in aircraft."),
        ("Aneroid barometer", "A compact, liquid-free barometer used for "
         "portability."),
        ("Sudden drop", "A sharp fall in pressure often means a storm is "
         "coming."),
    ], notes="A barometer does double duty: forecasting weather (pressure "
             "trends) and, as an altimeter, measuring height.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Hydraulic machines", "use Pascal's law to multiply force"),
        ("Atmospheric pressure", "the weight of the air; ≈ 10⁵ Pa"),
        ("Demonstrations", "crushing can, Magdeburg hemispheres"),
        ("Consequences", "straws, syringes, droppers, pumps"),
        ("Barometer", "atmospheric pressure supports 76 cm of mercury"),
        ("Altitude", "pressure falls with height; barometers forecast weather"),
    ], notes="Rapid recap; the barometer and the altitude relationship are the "
             "key points.")
    b.quiz_intro("Quiz 2", "Final Check — Atmosphere & Barometer", 5)
    b.quiz_q(1, "Why Mercury?", "A barometer uses mercury rather than water "
             "because mercury:", ["Is cheaper", "Is far denser, so the column "
              "is a manageable 76 cm instead of about 10 m", "Is colourless",
              "Boils easily"])
    b.quiz_a(1, "B. Is far denser, so the column is short",
             "Because mercury is about 13.6 times denser than water, "
             "atmospheric pressure supports only 76 cm of it. A water "
             "barometer would need a tube over 10 m tall.")
    b.quiz_q(2, "On a Mountain", "As a climber goes higher up a mountain, the "
             "reading on a barometer they carry will:", ["Increase",
              "Decrease", "Stay exactly the same", "Drop to zero immediately"])
    b.quiz_a(2, "B. Decrease",
             "There is less air above at greater heights, so atmospheric "
             "pressure — and the barometer reading — falls steadily as the "
             "climber ascends.")
    b.quiz_q(3, "Falling Barometer", "A barometer reading that is falling "
             "quickly usually indicates:", ["Fair, dry weather ahead",
              "An approaching storm or rain", "A rise in temperature only",
              "No change in weather"])
    b.quiz_a(3, "B. An approaching storm or rain",
             "Low and falling pressure is associated with unsettled, stormy "
             "weather, which is why a dropping barometer is taken as a warning "
             "of rain.")
    b.quiz_q(4, "Above the Mercury", "The space above the mercury in a "
             "barometer tube contains:", ["Air", "Water vapour",
              "A vacuum", "More mercury"])
    b.quiz_a(4, "C. A vacuum",
             "The tube is filled and inverted so that no air can enter, "
             "leaving a vacuum (the Torricellian vacuum) above the mercury. "
             "Any air there would push the column down and spoil the reading.")
    b.quiz_q(5, "Altimeter", "An aircraft's altimeter is really a barometer "
             "because altitude can be found from:", ["The temperature",
              "How atmospheric pressure decreases with height",
              "The speed of the plane", "The Earth's magnetism"])
    b.quiz_a(5, "B. How pressure decreases with height",
             "Since atmospheric pressure falls in a known way as you climb, a "
             "barometer scaled in metres (an altimeter) can read off the "
             "aircraft's altitude from the pressure.")
    b.closing("An Ocean of Air",
              "We live at the bottom of a sea of air — measuring its pressure "
              "lets us forecast storms and fly safely above the clouds.")
    return b


def build():
    for fname, fn in [("G9_S39_Pressure_in_Fluids_1.pptx", deck1),
                      ("G9_S40_Pressure_in_Fluids_2.pptx", deck2)]:
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
