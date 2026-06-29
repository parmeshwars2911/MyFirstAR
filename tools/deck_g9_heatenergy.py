"""
Grade 9 Physics — Chapter: Heat and Energy.
S65 (heat & temperature, thermal & anomalous expansion, energy flow),
S66 (sources of energy, renewable vs non-renewable, solar),
S67 (wind/water/nuclear, energy degradation, greenhouse effect & global
warming).  ICSE Class 9 (Selina) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade09"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Heat and Energy  •  ICSE Class 9 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["orange"])
    anom = b.asset("g9he_anom", D.anomalous_water("g9he_anom"))
    bim = b.asset("g9he_bimetal", D.bimetallic_strip("g9he_bimetal"))
    hero = b.asset("g9_heatenergy_hero", anom)

    b.title("ICSE • Class 9 • Heat", "Heat, Temperature & Expansion",
            "Heat vs temperature  •  Thermal expansion  •  Anomalous "
            "expansion of water  •  Energy flow", img=hero)
    b.objectives([
        "Distinguish heat from temperature",
        "Describe thermal expansion of solids, liquids and gases",
        "Explain the anomalous expansion of water",
        "Describe Hope's experiment",
        "State the consequences of water's anomalous expansion",
        "Outline the flow of energy in an ecosystem",
    ])
    b.divider(1, "Part 1", "Heat, Temperature & Expansion",
              "Energy on the move, and what it does to matter")
    b.cards("TWO IDEAS", "Heat vs Temperature", [
        ("Heat", "A form of energy that flows from a hotter to a colder body; "
         "measured in joules."),
        ("Temperature", "The degree of hotness that decides the direction of "
         "heat flow; measured in °C or K."),
        ("Total vs average", "Heat is total thermal energy; temperature is the "
         "average energy per molecule."),
        ("Different things", "A bucket of warm water holds more heat than a "
         "spark, though the spark is hotter."),
    ], notes="Separate heat (energy) from temperature (hotness). The bucket-"
             "vs-spark example is the clearest.")
    b.cards("EXPANSION", "Thermal Expansion", [
        ("Solids", "Expand the least on heating; rails and bridges are given "
         "gaps to allow for it."),
        ("Liquids", "Expand more than solids; the basis of liquid-in-glass "
         "thermometers."),
        ("Gases", "Expand the most of all for the same temperature rise."),
        ("Why it happens", "Heating makes molecules vibrate more and move "
         "further apart."),
    ], notes="Order of expansion: gases > liquids > solids. Heating increases "
             "molecular separation.")
    b.text_image("APPLICATIONS", "Using and Allowing for Expansion",
                 ["A bimetallic strip bends on heating because two metals "
                  "expand by different amounts.",
                  "It is used in thermostats to switch heating circuits on and "
                  "off.",
                  "Gaps are left between railway lines and in bridges to allow "
                  "for expansion.",
                  "Overhead wires are strung loosely so they do not snap when "
                  "they contract in winter."],
                 bim, img_side="right", img_w=6.0, img_h=3.0,
                 panel_title="The bimetallic strip",
                 caption="Two metals expand differently, so the strip bends",
                 notes="The bimetallic strip is the key application — bending "
                       "from unequal expansion runs thermostats.")
    b.cards("USE & CARE", "Expansion: Where It Helps and Where It Harms", [
        ("Shrink-fitting", "A hot metal rim or ring is slipped on, then grips "
         "tightly as it cools and contracts."),
        ("Thermostats", "A bimetallic strip bends with temperature to switch "
         "an iron or heater on and off."),
        ("Bridges & rails", "Expansion gaps and roller supports stop them "
         "buckling in hot weather."),
        ("Pipes & wires", "Loops in pipes and slack in wires allow for "
         "expansion and contraction."),
    ], notes="Expansion is both useful (shrink-fitting, thermostats) and a "
             "hazard to design around (bridges, rails, pipes).")
    b.text_image("ANOMALOUS WATER", "The Anomalous Expansion of Water",
                 ["Most substances expand steadily as they are heated.",
                  "Water is unusual: between 0°C and 4°C it CONTRACTS as it "
                  "warms.",
                  "Above 4°C it expands normally.",
                  "So water has its maximum density at 4°C."],
                 anom, img_side="left", img_w=5.6, img_h=3.8,
                 panel_title="Densest at 4°C",
                 caption="Water contracts from 0°C to 4°C, then expands",
                 notes="Water's odd behaviour: densest at 4°C. This single "
                       "fact explains why ice floats and ponds freeze top-"
                       "down.")
    b.bullets("HOPE'S EXPERIMENT", "Hope's Experiment", [
        ("The setup", "A tall jar of water is surrounded at the middle by a "
         "freezing mixture."),
        ("Two thermometers", "One near the top and one near the bottom of the "
         "jar."),
        ("What is seen", "The bottom cools to 4°C first; later the top cools "
         "to 0°C and freezes."),
        ("What it proves", "Water at 4°C is densest and sinks, so freezing "
         "starts at the top."),
    ], panel_title="Demonstrating maximum density at 4°C",
       notes="Hope's experiment proves water is densest at 4°C: the 4°C water "
             "sinks, and ice forms at the top.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Hotter or More Heat", "A mug of tea at 80°C and a bucket of "
             "water at 40°C — which holds more heat energy?",
             ["The tea", "The bucket of water", "Both the same",
              "Neither holds heat"])
    b.quiz_a(1, "B. The bucket of water",
             "Temperature tells you how hot something is, but heat depends "
             "also on mass. The large mass of bucket water stores more thermal "
             "energy than the small, hotter mug of tea.")
    b.quiz_q(2, "Gaps in Rails", "Small gaps are left between sections of "
             "railway line so that, on a hot day, the rails can:",
             ["Contract safely", "Expand without buckling", "Conduct "
              "electricity", "Stay cool"])
    b.quiz_a(2, "B. Expand without buckling",
             "Metals expand when heated. The gaps give the rails room to "
             "lengthen on a hot day; without them the rails would push against "
             "each other and buckle.")
    b.quiz_q(3, "Densest Water", "Water has its maximum density at a "
             "temperature of:", ["0°C", "4°C", "10°C", "100°C"])
    b.quiz_a(3, "B. 4°C",
             "Because water contracts from 0°C up to 4°C and then expands, it "
             "is at its densest at 4°C — the heart of its anomalous "
             "behaviour.")
    b.quiz_q(4, "Bimetallic Strip", "A bimetallic strip is able to bend when "
             "heated because the two metals have different:",
             ["Colours", "Amounts of expansion", "Masses", "Melting points"])
    b.quiz_a(4, "B. Amounts of expansion",
             "The two bonded metals expand by different amounts for the same "
             "temperature rise. The one that expands more forces the strip to "
             "curve toward the other — used in thermostats.")
    b.quiz_q(5, "Which Expands Most?", "For the same rise in temperature, "
             "which expands the most?", ["A solid", "A liquid", "A gas",
              "All the same"])
    b.quiz_a(5, "C. A gas",
             "Gases expand far more than liquids, and liquids more than "
             "solids, for the same temperature rise — because gas molecules "
             "are free to move much further apart.")
    b.divider(2, "Part 2", "Consequences & Energy Flow",
              "Why ponds freeze from the top, and how energy moves")
    b.cards("CONSEQUENCES", "Consequences of Anomalous Expansion", [
        ("Ice floats", "Ice is less dense than water, so it floats on the "
         "surface."),
        ("Ponds freeze top-down", "A layer of ice forms on top while water "
         "below stays liquid."),
        ("Aquatic life survives", "The ice insulates the water beneath, so "
         "fish live through winter."),
        ("Pipes burst", "Water expanding as it freezes can crack water "
         "pipes."),
    ], notes="All follow from water being densest at 4°C and ice being less "
             "dense. Life under ice is the headline consequence.")
    b.bullets("ENERGY FLOW", "Energy Flow in an Ecosystem", [
        ("The Sun", "Almost all energy on Earth comes from the Sun."),
        ("Producers", "Green plants capture solar energy by photosynthesis."),
        ("Consumers", "Animals get energy by eating plants or other animals."),
        ("One-way flow", "Energy flows from the Sun → producers → consumers, "
         "and only about 10% passes to each next level."),
    ], panel_title="Sun → plants → animals",
       notes="Energy flows one way through food chains, with large losses at "
             "each step — the 10% rule.")
    b.bullets("THERMODYNAMICS", "Energy Is Conserved but Degrades", [
        ("First law", "Energy can be transformed but never created or "
         "destroyed."),
        ("Always transforming", "In every process energy changes form, e.g. "
         "food energy → movement + heat."),
        ("Degradation", "At each change some energy spreads out as low-grade "
         "heat that cannot be fully reused."),
        ("Why it matters", "This is why no machine is 100% efficient."),
    ], panel_title="Conservation and degradation",
       notes="First law: energy is conserved. But it degrades to useless heat, "
             "limiting efficiency — links to energy degradation in lesson 3.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Heat vs temperature", "energy that flows vs degree of hotness"),
        ("Expansion", "gases > liquids > solids; allowed for in rails/bridges"),
        ("Anomalous water", "contracts 0–4°C; densest at 4°C"),
        ("Hope's experiment", "shows water is densest at 4°C"),
        ("Consequences", "ice floats; ponds freeze top-down; life survives"),
        ("Energy flow", "Sun → producers → consumers; energy degrades"),
    ], notes="Rapid recap; anomalous expansion and its consequences are the "
             "exam favourites.")
    b.quiz_intro("Quiz 2", "Final Check — Water & Energy", 5)
    b.quiz_q(1, "Frozen Pond", "Fish survive in a pond whose surface has "
             "frozen because:", ["Ice sinks and warms the bottom",
              "Ice floats on top and insulates the liquid water below",
              "Fish do not need oxygen", "The whole pond turns solid"])
    b.quiz_a(1, "B. Floating ice insulates the water below",
             "Because ice is less dense it floats, and this surface layer "
             "insulates the water beneath. That water stays liquid (around "
             "4°C), letting fish survive the winter.")
    b.quiz_q(2, "Cooling Water", "A beaker of water at 10°C is cooled. As its "
             "temperature falls toward 4°C, the water:",
             ["Expands", "Contracts and becomes denser", "Boils",
              "Stays the same volume"])
    b.quiz_a(2, "B. Contracts and becomes denser",
             "From 10°C down to 4°C water behaves normally, contracting as it "
             "cools and reaching maximum density at 4°C. Only below 4°C does "
             "it start to expand again.")
    b.quiz_q(3, "Energy Loss", "Only about 10% of the energy at one level of "
             "a food chain reaches the next level. The rest is mostly:",
             ["Created anew", "Lost as heat and used in life processes",
              "Stored forever", "Turned into matter"])
    b.quiz_a(3, "B. Lost as heat and used in life processes",
             "Most energy is used up in respiration, movement and staying "
             "warm, escaping as low-grade heat. Only a small fraction is "
             "stored and passed on — hence short food chains.")
    b.quiz_q(4, "No 100% Machine", "No machine can be 100% efficient because, "
             "in every energy change, some energy:",
             ["Is destroyed", "Degrades into low-grade heat that cannot be "
              "fully reused", "Turns into mass", "Disappears completely"])
    b.quiz_a(4, "B. Degrades into low-grade heat",
             "Energy is conserved, but at each transformation some of it "
             "spreads out as low-grade heat that cannot all be recovered. This "
             "degradation caps the efficiency of every machine.")
    b.quiz_q(5, "Burst Pipe", "Water pipes can burst in freezing weather "
             "because water:", ["Contracts as it freezes",
              "Expands as it freezes", "Evaporates", "Gets heavier"])
    b.quiz_a(5, "B. Expands as it freezes",
             "Unlike most liquids, water expands on freezing. Confined in a "
             "pipe, the growing ice pushes outward with great force and can "
             "split the pipe.")
    b.closing("Heat, Water and Energy",
              "Water's strange expansion keeps fish alive under the ice — and "
              "every joule of energy, though conserved, slowly degrades to "
              "heat.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["teal"])
    hero = b.asset("g9_energy_hero", None)

    b.title("ICSE • Class 9 • Energy", "Sources of Energy",
            "What energy sources are  •  Renewable vs non-renewable  •  Solar "
            "energy  •  Using energy wisely", img=hero)
    b.objectives([
        "Explain what is meant by a source of energy",
        "Classify sources as renewable or non-renewable",
        "Give examples of renewable energy sources",
        "Give examples of non-renewable energy sources",
        "Describe how solar energy is used to make electricity",
        "Explain why energy must be used judiciously",
    ])
    b.divider(1, "Part 1", "Sources of Energy",
              "Where our energy comes from")
    b.cards("SOURCES", "What Is a Source of Energy?", [
        ("Energy source", "Anything from which useful energy can be drawn for "
         "work, heat or electricity."),
        ("The Sun", "The ultimate source of almost all energy on Earth."),
        ("Two kinds", "Sources are either renewable or non-renewable."),
        ("Why it matters", "Our growing demand for energy must be met without "
         "running out or harming the planet."),
    ], notes="Define an energy source and the renewable/non-renewable split, "
             "which the rest of the lesson develops.")
    b.cards("RENEWABLE", "Renewable (Non-Conventional) Sources", [
        ("Solar energy", "Energy from the Sun, captured by solar cells and "
         "heaters."),
        ("Wind energy", "Moving air turns turbines to generate electricity."),
        ("Hydro energy", "Falling or flowing water spins turbines in dams."),
        ("Biomass & others", "Energy from plants, biogas, tides and "
         "geothermal heat."),
    ], notes="Renewable sources are replenished naturally and won't run out. "
             "Note they are also called non-conventional.")
    b.cards("NON-RENEWABLE", "Non-Renewable (Conventional) Sources", [
        ("Coal", "A fossil fuel burnt in power stations; limited and "
         "polluting."),
        ("Petroleum / oil", "Fuels vehicles and industry; formed over "
         "millions of years."),
        ("Natural gas", "A cleaner fossil fuel, but still finite."),
        ("Nuclear fuel", "Uranium releases huge energy, but produces "
         "radioactive waste."),
    ], notes="Non-renewable (conventional) sources are finite and mostly "
             "fossil fuels — they will run out and cause pollution.")
    b.cards("COMPARISON", "Renewable vs Non-Renewable", [
        ("Supply", "Renewables are replenished; non-renewables run out."),
        ("Pollution", "Renewables are generally clean; fossil fuels pollute."),
        ("Availability", "Renewables can be intermittent (sun, wind); fossil "
         "fuels give steady power."),
        ("Future", "The world is shifting toward renewables for "
         "sustainability."),
    ], notes="Side-by-side comparison. Renewables = clean but intermittent; "
             "fossil fuels = reliable but finite and dirty.")
    b.statement("THE SUN'S ENERGY", "The Sun and the Solar Constant",
                "The Sun's enormous energy comes from nuclear fusion, in which "
                "hydrogen nuclei join to form helium, releasing huge energy.",
                formula="Solar constant ≈ 1.4 kW per square metre above the "
                        "atmosphere",
                points=["The solar constant is the solar energy falling per "
                        "second on 1 m² held normal to the Sun's rays.",
                        "Fusion in the Sun's core is the ultimate source of "
                        "almost all our energy.",
                        "Even fossil fuels are sunlight stored by ancient "
                        "plants."],
                notes="The Sun runs on fusion; the solar constant (~1.4 kW/m²) "
                      "measures the energy arriving from it. Ties the whole "
                      "energy story back to the Sun.")
    b.cards("MORE RENEWABLES", "Geothermal, Tidal and Ocean Energy", [
        ("Geothermal", "Heat from hot rocks underground boils water to steam "
         "that drives turbines."),
        ("Tidal energy", "The rise and fall of tides turns generators in a "
         "tidal barrage."),
        ("Wave energy", "The up-and-down motion of sea waves is used to "
         "generate electricity."),
        ("Ocean thermal (OTEC)", "Uses the temperature difference between warm "
         "surface water and cold deep water."),
    ], notes="Additional non-conventional sources Selina lists: geothermal, "
             "tidal, wave and ocean-thermal energy.")
    b.bullets("BIOMASS", "Biomass and Biogas", [
        ("Biomass", "Energy stored in plants and animal waste, released by "
         "burning or processing."),
        ("Biogas", "Rotting organic waste in a digester produces a flammable "
         "gas (mainly methane)."),
        ("Renewable", "Crops and waste are continually produced, so the "
         "supply renews."),
        ("Bonus", "Biogas plants also turn waste into useful fuel and "
         "fertiliser."),
    ], panel_title="Energy from living matter",
       notes="Biomass and biogas are renewable fuels from plant/animal matter "
             "— common in rural India.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Which Is Renewable?", "Which of these is a renewable source "
             "of energy?", ["Coal", "Petroleum", "Wind", "Natural gas"])
    b.quiz_a(1, "C. Wind",
             "Wind is replenished naturally and never runs out, so it is "
             "renewable. Coal, petroleum and natural gas are finite fossil "
             "fuels — non-renewable.")
    b.quiz_q(2, "Ultimate Source", "The ultimate source of almost all the "
             "energy we use on Earth is:", ["Coal", "The Sun", "The wind",
              "The oceans"])
    b.quiz_a(2, "B. The Sun",
             "Sunlight drives the winds, the water cycle and plant growth, and "
             "even fossil fuels are stored ancient sunlight. The Sun is the "
             "ultimate energy source.")
    b.quiz_q(3, "Runs Out", "Fossil fuels are described as non-renewable "
             "because they:", ["Can be remade quickly",
              "Take millions of years to form and are being used up far "
              "faster", "Never run out", "Cause no pollution"])
    b.quiz_a(3, "B. Take millions of years to form and are used up fast",
             "Coal, oil and gas form over millions of years but are consumed "
             "in a tiny fraction of that time, so they cannot be replaced on a "
             "human timescale — hence non-renewable.")
    b.quiz_q(4, "Cleaner Choice", "To reduce air pollution, a country should "
             "generate MORE of its electricity from:",
             ["Coal", "Solar and wind", "Petroleum", "Diesel generators"])
    b.quiz_a(4, "B. Solar and wind",
             "Solar and wind produce electricity without burning fuel, so "
             "they release almost no pollution — unlike coal, oil and diesel, "
             "which dirty the air.")
    b.quiz_q(5, "Biogas Source", "Biogas for cooking is produced from:",
             ["Burning coal", "The decomposition of organic waste in a "
              "digester", "Splitting atoms", "Sunlight on solar cells"])
    b.quiz_a(5, "B. Decomposition of organic waste",
             "Bacteria break down animal dung and plant waste in an "
             "oxygen-free digester, releasing biogas (mostly methane) that can "
             "be burnt for cooking — a renewable fuel.")
    b.divider(2, "Part 2", "Solar Energy & Wise Use",
              "Harnessing the Sun and saving energy")
    b.bullets("SOLAR", "Electricity From Solar Energy", [
        ("Solar cells", "A solar (photovoltaic) cell converts sunlight "
         "directly into electricity."),
        ("Solar panels", "Many cells joined together form a panel that powers "
         "homes and satellites."),
        ("Clean and free", "Once installed, the energy source (sunlight) is "
         "free and pollution-free."),
        ("The catch", "It works only in daylight, so batteries store energy "
         "for later use."),
    ], panel_title="From sunlight to current",
       notes="Solar cells turn light straight into electricity. Clean but "
             "intermittent, so storage matters.")
    b.bullets("SOLAR HEAT", "Other Uses of Solar Energy", [
        ("Solar water heaters", "Sunlight heats water for homes without "
         "electricity."),
        ("Solar cookers", "Concentrate sunlight to cook food."),
        ("Solar furnaces", "Mirrors focus the Sun to reach very high "
         "temperatures."),
        ("Drying", "Crops and clothes are dried using the Sun's heat."),
    ], panel_title="Using the Sun's heat directly",
       notes="Besides electricity, the Sun's heat is used directly for "
             "heating, cooking and drying.")
    b.cards("JUDICIOUS USE", "Using Energy Wisely", [
        ("Save electricity", "Switch off lights and appliances when not "
         "needed; use LED bulbs."),
        ("Efficient appliances", "Choose high-star-rated, energy-efficient "
         "devices."),
        ("Public transport", "Sharing transport saves fuel per person."),
        ("Go renewable", "Prefer clean sources to conserve fossil fuels for "
         "the future."),
    ], notes="Practical conservation steps. Saving energy and shifting to "
             "renewables protect finite resources.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Energy source", "anything we can draw useful energy from"),
        ("Renewable", "solar, wind, hydro, biomass — replenished, clean"),
        ("Non-renewable", "coal, oil, gas, nuclear — finite, polluting"),
        ("Solar cells", "convert sunlight directly into electricity"),
        ("Solar heat", "water heaters, cookers, furnaces, drying"),
        ("Judicious use", "save energy and prefer renewables"),
    ], notes="Rapid recap; the renewable/non-renewable distinction is the key "
             "idea.")
    b.quiz_intro("Quiz 2", "Final Check — Energy Sources", 5)
    b.quiz_q(1, "Solar Cell", "A solar (photovoltaic) cell converts:",
             ["Heat into light", "Sunlight directly into electricity",
              "Electricity into heat", "Wind into electricity"])
    b.quiz_a(1, "B. Sunlight directly into electricity",
             "A photovoltaic cell turns the energy of sunlight straight into "
             "an electric current — no burning and no moving parts.")
    b.quiz_q(2, "Best for Remote Village", "A sunny remote village far from "
             "the power grid could best get electricity from:",
             ["A long power line from a city", "Solar panels with batteries",
              "A coal power station", "Burning more wood"])
    b.quiz_a(2, "B. Solar panels with batteries",
             "Solar panels need no fuel supply or grid connection, and "
             "batteries store power for night-time — ideal for a sunny, remote "
             "place.")
    b.quiz_q(3, "Why Batteries?", "Solar electricity systems include "
             "batteries because solar cells:", ["Are too powerful",
              "Only generate electricity in daylight",
              "Produce heat not light", "Work better at night"])
    b.quiz_a(3, "B. Only generate in daylight",
             "Since solar cells need sunlight, they make no electricity at "
             "night or in poor weather. Batteries store the daytime surplus "
             "for use later.")
    b.quiz_q(4, "Conserve Fuel", "Switching off lights when leaving a room "
             "helps to:", ["Increase pollution", "Conserve energy and reduce "
              "the bill", "Damage the bulb", "Use more coal"])
    b.quiz_a(4, "B. Conserve energy and reduce the bill",
             "Less electricity used means less fuel burnt at the power station "
             "and a smaller bill — a simple but effective way to conserve "
             "energy.")
    b.quiz_q(5, "Not a Fossil Fuel", "Which of the following is NOT a fossil "
             "fuel?", ["Coal", "Petroleum", "Natural gas", "Hydrogen from "
              "water"])
    b.quiz_a(5, "D. Hydrogen from water",
             "Coal, petroleum and natural gas are fossil fuels formed from "
             "ancient organisms. Hydrogen split from water is not a fossil "
             "fuel — it can be a clean, renewable fuel.")
    b.closing("Powering the Future",
              "From sunshine to wind, renewable sources can meet our energy "
              "needs without using up the planet.")
    return b


def deck3():
    b = Builder(FOOTER, accent=C["purple"])
    hero = b.asset("g9_climate_hero", None)

    b.title("ICSE • Class 9 • Energy", "Energy & the Environment",
            "Wind, water & nuclear energy  •  Energy degradation  •  "
            "Greenhouse effect  •  Global warming", img=hero)
    b.objectives([
        "Describe how wind and water energy generate electricity",
        "Outline how nuclear energy is produced",
        "Explain energy degradation",
        "Explain the greenhouse effect",
        "Describe the causes and effects of global warming",
        "Suggest ways to reduce global warming",
    ])
    b.divider(1, "Part 1", "Wind, Water & Nuclear Energy",
              "Three more ways to generate power")
    b.cards("WIND", "Wind Energy", [
        ("How it works", "Moving air turns the blades of a wind turbine, which "
         "drives a generator."),
        ("Wind farms", "Many turbines together form a wind farm."),
        ("Clean & renewable", "It burns no fuel and produces no pollution."),
        ("Limitation", "It works only where winds are strong and steady."),
    ], notes="Wind turns turbines to make electricity — clean but dependent on "
             "the wind.")
    b.cards("WATER", "Water (Hydro) Energy", [
        ("Hydroelectricity", "Water stored behind a dam falls and spins "
         "turbines to make electricity."),
        ("Tidal energy", "The rise and fall of tides drives generators."),
        ("Renewable", "The water cycle constantly replenishes the supply."),
        ("Big projects", "Dams are costly to build and affect local "
         "environments."),
    ], notes="Hydro uses falling/tidal water. Renewable and powerful, but dams "
             "have environmental costs.")
    b.bullets("NUCLEAR", "Nuclear Energy", [
        ("Nuclear fission", "Splitting heavy atoms (like uranium) releases an "
         "enormous amount of energy."),
        ("In a reactor", "The heat boils water to steam, which spins turbines "
         "to generate electricity."),
        ("Very concentrated", "A tiny amount of fuel yields a huge amount of "
         "energy."),
        ("The drawback", "It produces dangerous radioactive waste that must be "
         "stored safely."),
    ], panel_title="Energy from the atom",
       notes="Nuclear fission releases vast energy from little fuel, but "
             "radioactive waste is the major problem.")
    b.bullets("FUSION vs FISSION", "Two Kinds of Nuclear Energy", [
        ("Fission", "A heavy nucleus (uranium) splits into lighter ones, "
         "releasing energy — used in today's reactors."),
        ("Fusion", "Light nuclei (hydrogen) join to form a heavier one, "
         "releasing even more energy — this powers the Sun."),
        ("Fuel and waste", "Fission needs rare uranium and leaves radioactive "
         "waste; fusion's fuel (hydrogen) is abundant and cleaner."),
        ("The challenge", "Controlled fusion needs enormous temperatures and "
         "is still being developed on Earth."),
    ], panel_title="Splitting vs joining nuclei",
       notes="Distinguish fission (splitting, used now) from fusion (joining, "
             "powers the Sun, future clean energy).")
    b.statement("DEGRADATION", "Energy Degradation",
                "Each time energy is used or changed, some of it turns into "
                "low-grade heat that spreads out and cannot be usefully "
                "recovered.",
                points=["Energy is conserved in total, but its usefulness "
                        "falls.",
                        "High-grade energy (electricity, fuel) degrades to "
                        "low-grade heat.",
                        "This is why we must keep finding fresh energy "
                        "sources."],
                notes="Energy degradation: total energy is conserved but its "
                      "quality falls to useless heat. Motivates conservation.")
    b.cards("CONVENTIONAL vs NOT", "Conventional and Non-Conventional Sources", [
        ("Conventional", "Long-used sources: coal, petroleum, natural gas and "
         "hydroelectricity."),
        ("Non-conventional", "Newer, renewable sources: solar, wind, tidal, "
         "geothermal and biogas."),
        ("Why the shift", "Conventional fossil fuels are finite and polluting; "
         "non-conventional ones are cleaner."),
        ("Best mix", "A reliable supply combines several sources to suit the "
         "location."),
    ], notes="Clarify the conventional vs non-conventional terms, which the "
             "syllabus uses alongside renewable/non-renewable.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Turbine Power", "Wind, hydro and most other power stations "
             "make electricity by ultimately:",
             ["Burning the wind", "Turning a generator with a spinning "
              "turbine", "Using solar cells", "Splitting water"])
    b.quiz_a(1, "B. Turning a generator with a spinning turbine",
             "Whether driven by wind, falling water or steam, the common step "
             "is a turbine spinning a generator — turning motion into "
             "electricity by electromagnetic induction.")
    b.quiz_q(2, "Tiny Fuel, Huge Energy", "A very small mass of fuel releasing "
             "an enormous amount of energy is characteristic of:",
             ["Wind energy", "Nuclear energy", "Solar heating",
              "Burning wood"])
    b.quiz_a(2, "B. Nuclear energy",
             "Nuclear fission releases millions of times more energy per "
             "kilogram than burning fuel, so a tiny amount of uranium yields a "
             "huge amount of energy.")
    b.quiz_q(3, "Nuclear Drawback", "The main disadvantage of nuclear power "
             "is:", ["It uses too much fuel", "It produces dangerous "
              "radioactive waste", "It needs strong winds", "It only works at "
              "night"])
    b.quiz_a(3, "B. It produces dangerous radioactive waste",
             "Nuclear reactors leave behind radioactive waste that stays "
             "hazardous for a very long time and must be stored with great "
             "care — its biggest drawback.")
    b.quiz_q(4, "Degraded Energy", "When energy 'degrades', it changes into:",
             ["High-grade electricity", "Low-grade heat that cannot be fully "
              "reused", "New fuel", "Pure light"])
    b.quiz_a(4, "B. Low-grade heat that cannot be fully reused",
             "Degradation turns useful, concentrated energy into spread-out "
             "low-grade heat. The energy still exists but can no longer do "
             "much useful work.")
    b.quiz_q(5, "Hydro vs Nuclear", "Which pair correctly matches the source "
             "to its description?",
             ["Hydro — splits atoms; Nuclear — uses falling water",
              "Hydro — uses falling water; Nuclear — splits atoms",
              "Both split atoms", "Both burn coal"])
    b.quiz_a(5, "B. Hydro uses falling water; Nuclear splits atoms",
             "Hydroelectricity uses falling water to spin turbines, while "
             "nuclear power releases energy by splitting (fissioning) heavy "
             "atoms such as uranium.")
    b.divider(2, "Part 2", "Greenhouse Effect & Global Warming",
              "How our energy use is changing the climate")
    b.text_image("GREENHOUSE", "The Greenhouse Effect",
                 ["Sunlight passes through the atmosphere and warms the "
                  "Earth's surface.",
                  "The warm Earth radiates heat (infrared) back outward.",
                  "Greenhouse gases like carbon dioxide trap some of this "
                  "heat in the atmosphere.",
                  "This natural warming keeps Earth habitable — but too much "
                  "of it is harmful."],
                 b.asset("g9he_greenhouse", D.greenhouse_effect("g9he_greenhouse")),
                 img_side="right", img_w=5.2, img_h=3.8,
                 panel_title="Heat trapped by gases",
                 caption="Greenhouse gases trap outgoing heat",
                 notes="The greenhouse effect: gases trap re-radiated heat. "
                       "Natural and necessary, but enhanced by our emissions.")
    b.bullets("GLOBAL WARMING", "Global Warming", [
        ("The cause", "Burning fossil fuels adds extra carbon dioxide, "
         "strengthening the greenhouse effect."),
        ("Rising temperatures", "Average global temperatures are slowly "
         "rising."),
        ("Melting ice", "Glaciers and polar ice melt, raising sea levels."),
        ("Climate change", "More extreme weather — floods, droughts and "
         "storms."),
    ], panel_title="An enhanced greenhouse effect",
       notes="Extra CO2 from fossil fuels enhances warming, melting ice and "
             "disrupting the climate.")
    b.cards("SOLUTIONS", "Ways to Reduce Global Warming", [
        ("Use renewables", "Switch from fossil fuels to solar, wind and "
         "hydro."),
        ("Save energy", "Use less electricity and fuel, and choose efficient "
         "appliances."),
        ("Plant trees", "Trees absorb carbon dioxide from the air."),
        ("Less, reuse, recycle", "Cut waste and pollution from manufacturing "
         "and transport."),
    ], notes="Solutions centre on cutting CO2: renewables, efficiency, "
             "afforestation and reducing waste.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Wind & water", "spin turbines to generate clean electricity"),
        ("Nuclear", "fission gives huge energy but radioactive waste"),
        ("Degradation", "useful energy turns to low-grade heat"),
        ("Greenhouse effect", "gases trap re-radiated heat; natural but "
         "enhanced"),
        ("Global warming", "extra CO2 → rising temperatures, melting ice"),
        ("Solutions", "renewables, efficiency, trees, reduce waste"),
    ], notes="Rapid recap; the greenhouse effect and ways to cut warming are "
             "the key points.")
    b.quiz_intro("Quiz 2", "Final Check — Climate", 5)
    b.quiz_q(1, "Main Greenhouse Gas", "The greenhouse gas most increased by "
             "burning fossil fuels is:", ["Oxygen", "Nitrogen", "Carbon "
              "dioxide", "Hydrogen"])
    b.quiz_a(1, "C. Carbon dioxide",
             "Burning coal, oil and gas releases large amounts of carbon "
             "dioxide, the chief greenhouse gas responsible for the enhanced "
             "warming of the planet.")
    b.quiz_q(2, "How It Warms", "Greenhouse gases warm the Earth by:",
             ["Blocking sunlight from entering",
              "Letting sunlight in but trapping the heat radiated back out",
              "Cooling the surface", "Producing their own light"])
    b.quiz_a(2, "B. Letting sunlight in but trapping outgoing heat",
             "Sunlight passes through the atmosphere and warms the ground. The "
             "Earth re-radiates infrared heat, which greenhouse gases absorb "
             "and trap — warming the planet.")
    b.quiz_q(3, "Rising Seas", "A major consequence of global warming is "
             "rising sea levels, caused mainly by:",
             ["More rainfall", "Melting glaciers and polar ice plus expanding "
              "warmer water", "Less evaporation", "Stronger winds"])
    b.quiz_a(3, "B. Melting ice and expanding warmer water",
             "Warming melts land ice into the oceans, and warmer water expands "
             "slightly — together raising sea levels and threatening "
             "low-lying coasts.")
    b.quiz_q(4, "Best Action", "Which action would most directly reduce global "
             "warming?", ["Running more coal plants",
              "Replacing fossil-fuel power with solar and wind",
              "Cutting down forests", "Using more petrol cars"])
    b.quiz_a(4, "B. Replacing fossil-fuel power with solar and wind",
             "Solar and wind generate electricity without releasing carbon "
             "dioxide, so switching to them directly cuts the emissions "
             "driving global warming.")
    b.quiz_q(5, "Trees Help", "Planting trees helps fight global warming "
             "because trees:", ["Release carbon dioxide",
              "Absorb carbon dioxide from the air during photosynthesis",
              "Reflect all sunlight", "Produce methane"])
    b.quiz_a(5, "B. Absorb carbon dioxide during photosynthesis",
             "Growing trees take in carbon dioxide and lock the carbon into "
             "wood, lowering the amount of this greenhouse gas in the "
             "atmosphere.")
    b.closing("Energy and Our Planet",
              "The way we make and use energy shapes the climate — choosing "
              "clean sources protects the Earth for the future.")
    return b


def build():
    for fname, fn in [("G9_S65_Heat_and_Energy_1.pptx", deck1),
                      ("G9_S66_Heat_and_Energy_2.pptx", deck2),
                      ("G9_S67_Heat_and_Energy_3.pptx", deck3)]:
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
