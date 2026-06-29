"""
Grade 9 Physics — Chapter: Upthrust in Fluids, Archimedes' Principle and
Floatation.  S53 (buoyancy, upthrust, Archimedes' principle) and
S54 (density, relative density, principle of floatation).  ICSE Class 9.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade09"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Upthrust, Archimedes & Floatation  •  ICSE Class 9 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["teal"])
    up = b.asset("g9up_balance", D.upthrust_balance("g9up_balance"))
    flo = b.asset("g9up_float1", D.floatation("g9up_float1"))
    hero = b.asset("g9_float_hero", up)

    b.title("ICSE • Class 9 • Fluids", "Upthrust & Archimedes",
            "Buoyancy & upthrust  •  Why upthrust acts  •  Archimedes' "
            "principle  •  Float or sink", img=hero)
    b.objectives([
        "Define buoyancy and upthrust",
        "State the characteristic properties of upthrust",
        "Explain why a liquid exerts an upthrust",
        "State that upthrust equals the weight of displaced liquid",
        "State and verify Archimedes' principle",
        "Predict whether a body will float or sink",
    ])
    b.divider(1, "Part 1", "Buoyancy & Upthrust",
              "The upward push of a fluid")
    b.statement("UPTHRUST", "Buoyancy and Upthrust",
                "When a body is placed in a fluid, the fluid exerts an upward "
                "force on it called the upthrust or buoyant force.",
                points=["This is why objects feel lighter in water.",
                        "It acts vertically upward through the centre of the "
                        "displaced fluid.",
                        "It is the reason ships float and balloons rise."],
                notes="Define upthrust as the upward push of a fluid. The "
                      "'lighter in water' experience is the hook.")
    b.text_image("APPARENT WEIGHT", "Apparent Loss of Weight",
                 ["A body weighed in water reads less on a spring balance "
                  "than in air.",
                  "The apparent loss of weight equals the upthrust on the "
                  "body.",
                  "Example: 5 N in air but 3 N in water means a 2 N upthrust.",
                  "The upthrust does not depend on the weight of the body — "
                  "only on the fluid it displaces."],
                 up, img_side="right", img_w=6.0, img_h=3.5,
                 panel_title="Weight lost = upthrust",
                 caption="The balance reads less in water",
                 notes="The apparent-weight-loss experiment defines and "
                       "measures upthrust directly.")
    b.cards("PROPERTIES", "Characteristic Properties of Upthrust", [
        ("Acts upward", "Always vertically upward, opposite to the weight."),
        ("More in denser fluids", "A denser fluid exerts a greater upthrust."),
        ("Depends on volume submerged", "More of the body submerged means more "
         "liquid displaced and more upthrust."),
        ("Independent of the body", "It does not depend on the body's own "
         "weight or material, only on the fluid displaced."),
    ], notes="The key properties. Upthrust depends on the fluid and the "
             "submerged volume, NOT on the object's weight.")
    b.bullets("WHY IT HAPPENS", "Why a Fluid Exerts an Upthrust", [
        ("Pressure rises with depth", "The bottom of a submerged body is "
         "deeper than its top."),
        ("Bigger push from below", "So the upward pressure on the base "
         "exceeds the downward pressure on the top."),
        ("Net upward force", "This pressure difference gives a net upward "
         "force — the upthrust."),
        ("Sideways cancels", "The sideways pressures on the body cancel out."),
    ], panel_title="A pressure difference top to bottom",
       notes="The cause: greater pressure on the lower surface than the upper "
             "one. This pressure difference IS the upthrust.")
    b.worked("WORKED EXAMPLE", "Upthrust From Displaced Water",
             "A body completely immersed in water displaces 250 cm³ of water. "
             "Find the upthrust on it. (density of water = 1 g/cm³, "
             "g = 10 m/s²)",
             ["Mass of water displaced = volume × density = 250 × 1 = 250 g "
              "= 0.25 kg",
              "Weight of displaced water = m g = 0.25 × 10 = 2.5 N",
              "Upthrust = weight of displaced water"],
             "Upthrust = 2.5 N",
             notes="Upthrust = weight of displaced water. Convert grams to kg "
                   "before using g = 10.")
    b.cards("BUOYANCY AROUND US", "Buoyancy in Everyday Life", [
        ("Swimming", "Water's upthrust supports much of our weight, so we feel "
         "light in a pool."),
        ("Lifting in water", "A heavy stone is easy to lift underwater but "
         "heavy once out of it."),
        ("Fish", "Fish adjust a gas-filled swim bladder to rise or sink."),
        ("Life jackets", "Filled with low-density material, they increase "
         "upthrust and keep us afloat."),
    ], notes="Relatable buoyancy examples to cement the concept before the "
             "quiz.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Lighter in Water", "A stone weighs 8 N in air and 5 N when "
             "fully immersed in water. The upthrust on the stone is:",
             ["13 N", "8 N", "3 N", "5 N"])
    b.quiz_a(1, "C. 3 N",
             "Upthrust = apparent loss of weight = weight in air − weight in "
             "water = 8 − 5 = 3 N.")
    b.quiz_q(2, "Why Upthrust?", "A fluid pushes a submerged object upward "
             "because the pressure on the object is:",
             ["The same all over", "Greater on the bottom (deeper) than on "
              "the top", "Greater on the top", "Only sideways"])
    b.quiz_a(2, "B. Greater on the bottom than the top",
             "Pressure increases with depth, so the upward push on the lower "
             "face is greater than the downward push on the upper face. This "
             "difference is the upthrust.")
    b.quiz_q(3, "Denser Liquid", "The same metal block is immersed fully first "
             "in water and then in a denser salt solution. The upthrust is:",
             ["Greater in water", "Greater in the salt solution",
              "The same in both", "Zero in both"])
    b.quiz_a(3, "B. Greater in the salt solution",
             "Fully immersed, the block displaces the same volume in each, but "
             "the denser salt solution weighs more for that volume — so it "
             "exerts a greater upthrust.")
    b.quiz_q(4, "Half Submerged", "As a block is lowered further into water, "
             "the upthrust on it:", ["Decreases",
              "Increases until it is fully submerged, then stays constant",
              "Stays the same throughout", "Becomes zero"])
    b.quiz_a(4, "B. Increases until fully submerged, then constant",
             "Upthrust depends on the volume of liquid displaced. As more of "
             "the block goes under, it displaces more water and the upthrust "
             "grows — until it is fully submerged, after which it no longer "
             "changes.")
    b.cards("THREE CASES", "Sink, Float or Hang Submerged", [
        ("Weight > max upthrust", "The body sinks (its density is greater than "
         "the fluid's)."),
        ("Weight = upthrust submerged", "The body floats fully submerged at any "
         "depth (densities equal)."),
        ("Weight < max upthrust", "The body rises and floats partly out "
         "(its density is less than the fluid's)."),
        ("The deciding factor", "Compare the body's density with the fluid's "
         "density."),
    ], notes="Three outcomes set by the density comparison: denser sinks, equal "
             "stays submerged, lighter floats partly out.")
    b.divider(2, "Part 2", "Archimedes' Principle",
              "Exactly how much upthrust?")
    b.statement("ARCHIMEDES", "Archimedes' Principle",
                "When a body is wholly or partly immersed in a fluid, it "
                "experiences an upthrust equal to the weight of the fluid it "
                "displaces.",
                formula="Upthrust  =  weight of the displaced fluid",
                points=["This puts an exact value on the upthrust.",
                        "Displace more fluid → feel more upthrust.",
                        "It explains floating, sinking and the apparent loss "
                        "of weight."],
                notes="Archimedes' principle quantifies upthrust. Everything "
                      "about floating and sinking follows from it.")
    b.bullets("VERIFICATION", "Verifying Archimedes' Principle", [
        "Weigh a solid in air using a spring balance.",
        "Lower it into an overflow (eureka) can full to the spout, catching "
        "the overflow.",
        "Note the new (smaller) reading while it is immersed.",
        "Weigh the water that overflowed.",
        "The loss in weight equals the weight of the displaced water — "
        "Archimedes' principle confirmed.",
    ], panel_title="The overflow-can experiment",
       notes="Walk through the eureka-can experiment showing loss of weight = "
             "weight of displaced water.")
    b.text_image("FLOAT OR SINK", "Float or Sink?",
                 ["Compare the weight of the body with the maximum upthrust "
                  "(when fully submerged).",
                  "If the upthrust can equal the weight, the body floats.",
                  "If the weight is greater than the largest possible "
                  "upthrust, it sinks.",
                  "A body floats if its average density is less than the "
                  "fluid's."],
                 flo, img_side="left", img_w=5.6, img_h=3.8,
                 panel_title="Weight vs upthrust",
                 caption="Floats when upthrust can balance the weight",
                 notes="The float/sink rule via density: lighter-than-fluid "
                       "floats, denser sinks. Leads into density next lesson.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Upthrust", "the upward (buoyant) force a fluid exerts"),
        ("Apparent loss", "weight in air − weight in fluid = upthrust"),
        ("Cause", "greater pressure on the lower face than the upper face"),
        ("Archimedes", "upthrust = weight of fluid displaced"),
        ("Verification", "eureka can: loss of weight = weight of overflow"),
        ("Float/sink", "floats if average density < fluid density"),
    ], notes="Rapid recap; Archimedes' principle is the central result.")
    b.quiz_intro("Quiz 2", "Final Check — Archimedes", 6)
    b.quiz_q(1, "How Much Upthrust?", "A body displaces 200 g of water when "
             "immersed. The upthrust on it equals the weight of:",
             ["200 g of the body", "200 g of water", "The whole body",
              "The container"])
    b.quiz_a(1, "B. 200 g of water",
             "By Archimedes' principle the upthrust equals the weight of the "
             "displaced fluid — here, the weight of 200 g of water.")
    b.quiz_q(2, "Eureka Can", "In the overflow-can experiment, the weight of "
             "water collected from the spout is found to equal the:",
             ["Weight of the body in air", "Apparent loss in weight of the "
              "body", "Weight of the can", "Volume of the body"])
    b.quiz_a(2, "B. Apparent loss in weight of the body",
             "The water pushed out weighs exactly the same as the apparent "
             "loss in the body's weight — a direct confirmation of Archimedes' "
             "principle.")
    b.quiz_q(3, "Iron vs Ship", "A solid lump of iron sinks, yet a ship made "
             "of iron floats. This is because the ship:",
             ["Is lighter than the iron lump", "Is hollow, so it displaces a "
              "large weight of water for its weight",
              "Is made of special iron", "Has an engine"])
    b.quiz_a(3, "B. Is hollow and displaces a lot of water",
             "The ship's hollow shape lets it push aside a large volume — and "
             "hence weight — of water. When that displaced weight equals the "
             "ship's weight, the upthrust balances it and the ship floats.")
    b.quiz_q(4, "Same Volume", "A block of wood and a block of iron have the "
             "same volume and are fully submerged in water. The upthrust on "
             "them is:", ["Greater on the iron", "Greater on the wood",
              "The same on both", "Zero on the wood"])
    b.quiz_a(4, "C. The same on both",
             "Fully submerged, both displace the same volume of water, so "
             "Archimedes' principle gives them the same upthrust — even though "
             "the iron is far heavier and will sink.")
    b.quiz_q(5, "Floating Balance", "A wooden block floats at rest on water. "
             "The upthrust on it is:", ["Greater than its weight",
              "Less than its weight", "Exactly equal to its weight", "Zero"])
    b.quiz_a(5, "C. Exactly equal to its weight",
             "A floating body is in equilibrium, so the upward upthrust must "
             "exactly balance its downward weight — it sinks just far enough "
             "to displace its own weight of water.")
    b.quiz_q(6, "Will It Stay Submerged?", "A sealed ball has exactly the same "
             "density as water. Released under the surface, it will:",
             ["Shoot to the surface", "Sink to the bottom",
              "Stay floating at whatever depth it is left (fully submerged)",
              "Dissolve"])
    b.quiz_a(6, "C. Stay at whatever depth it is left",
             "When a body's density equals the fluid's, its weight exactly "
             "equals the upthrust while fully submerged. The forces balance at "
             "any depth, so it neither rises nor sinks.")
    b.closing("Why Ships Float",
              "Archimedes' principle — upthrust equals the weight of fluid "
              "displaced — explains everything from a floating cork to a "
              "steel ship.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["purple"])
    flo = b.asset("g9up_float2", D.floatation("g9up_float2"))
    hero = b.asset("g9_density_hero", flo)

    b.title("ICSE • Class 9 • Fluids", "Density & Floatation",
            "Density  •  Relative density  •  Measuring R.D.  •  The principle "
            "of floatation", img=hero)
    b.objectives([
        "Define density and its units",
        "Define relative density",
        "Determine the relative density of a solid",
        "Determine the relative density of a liquid",
        "State the principle of floatation",
        "Explain everyday applications of floatation",
    ])
    b.divider(1, "Part 1", "Density & Relative Density",
              "How heavy a material is for its size")
    b.statement("DENSITY", "Density",
                "Density is the mass of a substance per unit volume.",
                formula="Density  =  mass / volume        (unit: kg/m³ or "
                        "g/cm³)",
                points=["Water has a density of 1000 kg/m³ (1 g/cm³).",
                        "A denser material packs more mass into the same "
                        "volume.",
                        "Density decides whether a material sinks or floats in "
                        "a fluid."],
                notes="Define density = mass/volume. Water's value (1 g/cm³) "
                      "is the reference everything is compared with.")
    b.worked("WORKED EXAMPLE", "Calculating Density",
             "A metal block has a mass of 270 g and a volume of 100 cm³. Find "
             "its density.",
             ["Density = mass / volume",
              "Density = 270 / 100",
              "Density = 2.7 g/cm³"],
             "Density = 2.7 g/cm³ (this is aluminium)",
             notes="Simple substitution. 2.7 g/cm³ identifies aluminium — link "
                   "density to identifying materials.")
    b.statement("RELATIVE DENSITY", "Relative Density",
                "Relative density (R.D.) compares the density of a substance "
                "with the density of water.",
                formula="R.D.  =  density of substance / density of water",
                points=["It is a pure ratio, so it has no unit.",
                        "R.D. = mass of substance / mass of an equal volume of "
                        "water.",
                        "R.D. greater than 1 sinks in water; less than 1 "
                        "floats."],
                notes="Relative density is a unitless ratio against water. "
                      ">1 sinks, <1 floats — a quick float/sink test.")
    b.bullets("R.D. OF A SOLID", "Finding the R.D. of a Solid", [
        "Weigh the solid in air (W₁).",
        "Weigh it again fully immersed in water (W₂).",
        "The loss in weight (W₁ − W₂) equals the weight of water displaced.",
        "R.D. = weight in air / loss of weight in water = W₁ / (W₁ − W₂).",
    ], panel_title="Using the apparent loss of weight",
       notes="The R.D. of a solid comes straight from Archimedes: weight in "
             "air over the loss of weight in water.")
    b.worked("WORKED EXAMPLE", "Relative Density of a Solid",
             "A piece of metal weighs 60 gf in air and 40 gf when fully "
             "immersed in water. Find its relative density.",
             ["Loss of weight in water = 60 − 40 = 20 gf",
              "R.D. = weight in air / loss of weight in water",
              "R.D. = 60 / 20 = 3"],
             "Relative density = 3 (no unit)",
             notes="Apply R.D. = weight in air / loss in water. The answer is "
                   "a pure number, three times as dense as water.")
    b.bullets("R.D. OF A LIQUID", "Finding the R.D. of a Liquid", [
        "Take a solid that sinks in both the liquid and water.",
        "Find its loss of weight in the liquid and its loss of weight in "
        "water.",
        "R.D. of liquid = loss of weight in liquid / loss of weight in "
        "water.",
        "Because the same solid displaces the same volume in each.",
    ], panel_title="Comparing losses of weight",
       notes="For a liquid's R.D., compare the upthrust (loss of weight) it "
             "gives with that of water on the same solid.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 4)
    b.quiz_q(1, "Will It Float?", "A material has a relative density of 0.8. "
             "Placed in water, it will:", ["Sink to the bottom",
              "Float with part above the surface", "Dissolve",
              "Stay fully submerged in the middle"])
    b.quiz_a(1, "B. Float with part above the surface",
             "R.D. less than 1 means the material is less dense than water, so "
             "it floats — sinking just enough to displace its own weight, with "
             "the rest above the surface.")
    b.quiz_q(2, "Find R.D.", "A solid weighs 50 N in air and 40 N in water. "
             "Its relative density is:", ["0.8", "1.25", "5", "10"])
    b.quiz_a(2, "C. 5",
             "R.D. = weight in air / loss of weight = 50 / (50 − 40) = 50/10 = "
             "5. The solid is five times as dense as water.")
    b.quiz_q(3, "No Units", "Relative density has no unit because it is:",
             ["A very small number", "A ratio of two densities",
              "Measured in kg/m³", "Always equal to 1"])
    b.quiz_a(3, "B. A ratio of two densities",
             "R.D. compares a substance's density with water's density. "
             "Dividing one density by another cancels the units, leaving a "
             "pure number.")
    b.quiz_q(4, "Densest Sinks", "Three liquids that do not mix settle in "
             "layers in a jar. The liquid at the very bottom has the:",
             ["Lowest density", "Highest density", "Least mass",
              "Largest volume"])
    b.quiz_a(4, "B. Highest density",
             "The densest liquid sinks below the others, so the bottom layer "
             "is always the one with the greatest density.")
    b.divider(2, "Part 2", "The Principle of Floatation",
              "When and how things float")
    b.statement("FLOATATION", "The Principle of Floatation",
                "A floating body displaces a weight of fluid exactly equal to "
                "its own weight.",
                formula="Weight of body  =  weight of fluid displaced",
                points=["A body floats when it can displace its own weight of "
                        "fluid before being fully submerged.",
                        "It floats higher in a denser fluid (less of it "
                        "submerged).",
                        "This is a special case of Archimedes' principle for a "
                        "floating body."],
                notes="The floatation principle: a floating body displaces its "
                      "own weight of fluid. Denser fluid → floats higher.")
    b.text_image("FORCES", "Balanced Forces on a Floating Body",
                 ["A floating body is in equilibrium: two forces balance.",
                  "Its weight acts downward through its centre of gravity.",
                  "The upthrust acts upward and equals the weight.",
                  "It sinks only until the displaced fluid weighs as much as "
                  "the body."],
                 flo, img_side="right", img_w=5.6, img_h=3.8,
                 panel_title="Weight = Upthrust",
                 caption="Equilibrium of a floating body",
                 notes="Two balanced forces: weight down, upthrust up. The "
                       "body settles at the depth where they are equal.")
    b.statement("HOW MUCH SUBMERGED", "Fraction of a Floating Body Submerged",
                "The fraction of a floating body that lies below the surface "
                "equals the ratio of its density to the fluid's density.",
                formula="submerged fraction  =  ρ(body) / ρ(fluid)",
                points=["Ice (ρ ≈ 0.9) in water floats with about 0.9 of it "
                        "submerged.",
                        "A body of density 0.6 g/cm³ floats with 60% under "
                        "water.",
                        "It follows directly from weight = weight of displaced "
                        "fluid."],
                notes="Submerged fraction = density ratio. This explains the "
                      "iceberg and lets students predict how high a body "
                      "floats.")
    b.worked("WORKED EXAMPLE", "Fraction of Wood Submerged",
             "A block of wood of density 0.6 g/cm³ floats in water "
             "(1.0 g/cm³). What fraction of its volume is under water?",
             ["submerged fraction = ρ(wood) / ρ(water)",
              "= 0.6 / 1.0",
              "= 0.6"],
             "0.6 (60%) of the block is below the surface; 40% shows above",
             notes="Apply submerged fraction = density ratio. 60% under, 40% "
                   "above — a quick check on floatation.")
    b.bullets("LIGHT SOLID", "R.D. of a Solid Lighter Than Water", [
        ("The problem", "A solid that floats cannot simply be weighed fully "
         "immersed — it will not stay under."),
        ("Use a sinker", "Attach a heavy sinker so the solid is dragged fully "
         "under water."),
        ("Weigh in stages", "Find the loss of weight with only the sinker "
         "immersed, then with both immersed."),
        ("Get the R.D.", "The extra loss of weight is the upthrust on the "
         "solid alone, giving its R.D."),
    ], panel_title="The sinker method",
       notes="For a solid lighter than water, a sinker keeps it submerged; the "
             "extra loss of weight gives the upthrust on the solid alone.")
    b.cards("APPLICATIONS", "Applications of Floatation", [
        ("Ships", "A steel ship is hollow, so it displaces a huge weight of "
         "water and floats."),
        ("Submarines", "Fill tanks with water to dive (sink), empty them with "
         "air to surface."),
        ("Hydrometer", "A floating instrument that measures the density of a "
         "liquid by how deep it sinks."),
        ("Hot-air balloons", "Float in air because the hot air inside is less "
         "dense than the cool air outside."),
    ], notes="Each application uses floatation. The submarine's ballast tanks "
             "and the hydrometer are commonly examined.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Density", "mass / volume; water is 1 g/cm³"),
        ("Relative density", "density ÷ density of water; no unit"),
        ("R.D. of solid", "weight in air / loss of weight in water"),
        ("R.D. of liquid", "loss in liquid / loss in water (same solid)"),
        ("Floatation", "a floating body displaces its own weight of fluid"),
        ("Applications", "ships, submarines, hydrometer, balloons"),
    ], notes="Rapid recap; the floatation principle and the R.D. formulae are "
             "the key results.")
    b.quiz_intro("Quiz 2", "Final Check — Density & Floatation", 5)
    b.quiz_q(1, "Floating Weight", "A boat of weight 5000 N floats on a lake. "
             "The weight of water it displaces is:", ["Less than 5000 N",
              "Exactly 5000 N", "More than 5000 N", "Zero"])
    b.quiz_a(1, "B. Exactly 5000 N",
             "By the principle of floatation a floating body displaces a "
             "weight of fluid equal to its own weight — so the boat displaces "
             "exactly 5000 N of water.")
    b.quiz_q(2, "Sea vs River", "A ship floats slightly higher in the sea "
             "than in a river because sea water is:", ["Less dense",
              "Denser, so less of the ship needs to be submerged",
              "Colder", "Saltier but lighter"])
    b.quiz_a(2, "B. Denser, so less needs to be submerged",
             "Sea water is denser than river water, so a smaller submerged "
             "volume displaces the ship's weight. The ship therefore rides a "
             "little higher in the sea.")
    b.quiz_q(3, "Submarine Dives", "A submarine dives by:",
             ["Becoming lighter", "Letting water into its ballast tanks to "
              "increase its weight", "Pumping in air", "Speeding up"])
    b.quiz_a(3, "B. Letting water into its ballast tanks",
             "Flooding the tanks increases the submarine's weight beyond the "
             "upthrust, so it sinks. To surface, compressed air pushes the "
             "water out, making it lighter again.")
    b.quiz_q(4, "Hydrometer", "A hydrometer floats deeper in liquid A than in "
             "liquid B. This shows that liquid A is:",
             ["Denser than B", "Less dense than B", "The same as B",
              "Not a liquid"])
    b.quiz_a(4, "B. Less dense than B",
             "A hydrometer sinks further in a less dense liquid (which gives "
             "less upthrust per unit volume). Sinking deeper in A means A is "
             "the lower-density liquid.")
    b.quiz_q(5, "Iceberg", "About nine-tenths of an iceberg lies below the "
             "water surface because the density of ice (0.9 g/cm³) is:",
             ["Much less than water", "Just below that of water, so most of "
              "it must submerge to displace its weight",
              "Greater than water", "Equal to water"])
    b.quiz_a(5, "B. Just below water, so most must submerge",
             "Ice is only slightly less dense than water (0.9 vs 1.0), so it "
             "must sink until about 90% is underwater to displace a weight of "
             "water equal to its own — leaving just a tenth showing.")
    b.closing("Float, Sink, or Sail",
              "Density and the principle of floatation decide whether "
              "something bobs like a cork or sinks like a stone.")
    return b


def build():
    for fname, fn in [("G9_S53_Upthrust_Archimedes_1.pptx", deck1),
                      ("G9_S54_Upthrust_Archimedes_2.pptx", deck2)]:
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
