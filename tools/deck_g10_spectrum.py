"""
Grade 10 Physics — Chapter: Spectrum.
Session 53 (Lesson 1: deviation, dispersion, the visible & EM spectrum) and
Session 54 (Lesson 2: properties/uses of EM radiations, UV/visible/IR,
scattering of light).  ICSE Class 10 (Selina) scope.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))
from engine import Builder, C
import diagrams as D

OUT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "ppt",
                                   "Grade10"))
os.makedirs(OUT, exist_ok=True)
FOOTER = "Spectrum  •  ICSE Class 10 Physics"


def deck1():
    b = Builder(FOOTER, accent=C["purple"])
    prism = b.asset("g10sp_prism", D.prism_refraction("g10sp_prism"))
    disp = b.asset("g10sp_disp", D.dispersion_spectrum("g10sp_disp"))
    em = b.asset("g10sp_em", D.em_spectrum("g10sp_em"))
    hero = b.asset("g10_spectrum_hero", disp)

    b.title("ICSE • Class 10 • Optics", "Spectrum & Dispersion",
            "Deviation by a prism  •  Dispersion of white light  •  The "
            "electromagnetic spectrum", img=hero)
    b.objectives([
        "Describe the deviation produced by a triangular prism",
        "Explain the dispersion of white light into a spectrum",
        "Recall the seven colours and their wavelength/frequency order",
        "Explain why violet deviates more than red",
        "List the members of the electromagnetic spectrum in order",
        "Use the wave relation c = f λ",
    ])
    b.divider(1, "Part 1", "Dispersion of White Light",
              "How a prism splits white light into colours")
    b.text_image("DEVIATION", "Deviation by a Prism",
                 ["A prism has two refracting surfaces inclined at the angle of "
                  "the prism, A.",
                  "Light refracts at both faces and bends toward the base.",
                  "The angle between the incident and emergent directions is "
                  "the angle of deviation, δ.",
                  "Different colours are deviated by different amounts — the "
                  "key to dispersion."],
                 prism, img_side="left", img_w=5.4, img_h=4.0,
                 panel_title="Angle of deviation",
                 caption="Light bends toward the base of the prism",
                 notes="Recall deviation from the refraction chapter, then set "
                       "up the idea that deviation depends on colour — leading "
                       "into dispersion.")
    b.text_image("DISPERSION", "Dispersion of White Light",
                 ["White light is a mixture of seven colours.",
                  "Each colour travels at a slightly different speed in glass, "
                  "so each has a different refractive index.",
                  "The prism therefore deviates each colour by a different "
                  "amount, spreading them out.",
                  "This splitting of white light into its colours is called "
                  "dispersion; the band of colours is the spectrum."],
                 disp, img_side="right", img_w=5.8, img_h=4.0,
                 panel_title="White light → a spectrum",
                 caption="The seven colours: VIBGYOR",
                 notes="Define dispersion. The cause is that refractive index "
                       "depends on colour (wavelength). Mention Newton's prism "
                       "experiment.")
    b.cards("WHY IT SPLITS", "Why the Colours Separate", [
        ("Different speeds", "In glass, violet light travels slowest and red "
         "fastest."),
        ("Different index", "So glass has the highest refractive index for "
         "violet and the lowest for red."),
        ("Different deviation", "Higher index → more bending, so violet is "
         "deviated most and red least."),
        ("In a vacuum", "All colours travel at the same speed c, so there is "
         "no dispersion in vacuum."),
    ], notes="Hammer the chain: speed → refractive index → deviation. Note "
             "there is NO dispersion in vacuum, where all colours share speed "
             "c.")
    b.bullets("THE COLOURS", "VIBGYOR — Wavelength & Frequency", [
        ("Violet", "shortest wavelength (~400 nm), highest frequency, deviated "
         "most."),
        ("Through to Red", "wavelength increases and frequency decreases "
         "across the spectrum."),
        ("Red", "longest visible wavelength (~700 nm), lowest frequency, "
         "deviated least."),
        ("Order", "Violet, Indigo, Blue, Green, Yellow, Orange, Red — "
         "remember VIBGYOR."),
    ], panel_title="From violet to red",
       notes="Anchor the two ends: violet (short λ, high f) and red (long λ, "
             "low f). Everything else lies between.")
    b.cards("NEWTON'S PROOF", "Showing White Light Is Composite", [
        ("Experiment 1", "A single prism spreads white light into the seven "
         "colours — dispersion."),
        ("Experiment 2", "A second, inverted prism recombines those colours "
         "back into white light."),
        ("Experiment 3", "Passing just one colour of the spectrum through "
         "another prism gives no new colours."),
        ("Conclusion", "The colours are already present in white light; the "
         "prism only separates them."),
    ], notes="Newton's three classic experiments. The third (single-colour "
             "test) clinches that the prism does not manufacture colour.")
    b.statement("PURE vs IMPURE", "Pure and Impure Spectrum",
                "In an impure spectrum the colours overlap; in a pure spectrum "
                "each colour is sharply separated.",
                points=["A simple prism alone gives an impure spectrum — "
                        "neighbouring colours overlap.",
                        "Adding lenses to focus each colour to a sharp band "
                        "gives a pure spectrum.",
                        "A pure spectrum needs the colours to be parallel and "
                        "separately focused."],
                notes="Distinguish pure (sharp, focused) from impure "
                      "(overlapping) spectra; a pure spectrum needs lenses plus "
                      "the prism, not the prism alone.")
    b.statement("RECOMBINATION", "White Light Can Be Re-made",
                "A second, inverted prism can recombine the spectrum back into "
                "white light — proving the colours were always in the white "
                "light.",
                points=["A single prism disperses; a matched inverted prism "
                        "recombines.",
                        "This shows the prism does not 'create' colour — it "
                        "only separates what is already there.",
                        "A disc painted with the seven colours (Newton's disc) "
                        "looks white when spun fast."],
                notes="Use Newton's two-prism and spinning-disc demonstrations "
                      "to prove white light is a mixture, not the prism's "
                      "creation.")
    b.statement("ONE COLOUR vs MANY", "Monochromatic and Polychromatic Light",
                "Light of a single wavelength is monochromatic; light made of "
                "many wavelengths is polychromatic.",
                points=["Monochromatic light (e.g. from a sodium lamp) is not "
                        "split by a prism — it has only one colour.",
                        "White light is polychromatic — a mixture of all seven "
                        "colours, so a prism disperses it.",
                        "The visible spectrum is continuous: the colours merge "
                        "smoothly from violet to red."],
                notes="Define monochromatic vs polychromatic. A prism cannot "
                      "disperse monochromatic light — a useful test and a "
                      "common exam point.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Most Deviated", "When white light passes through a glass "
             "prism, which colour emerges closest to the base of the prism "
             "(deviated most)?", ["Red", "Yellow", "Green", "Violet"])
    b.quiz_a(1, "D. Violet",
             "Glass has the highest refractive index for violet (it travels "
             "slowest), so violet bends the most and emerges nearest the "
             "base. Red, with the lowest index, deviates least.")
    b.quiz_q(2, "No Dispersion", "White light passes through a thick glass "
             "slab with parallel sides instead of a prism. The emergent light "
             "is white because:",
             ["Glass cannot disperse light",
              "The colours recombine as they leave the parallel face",
              "White light has only one colour",
              "The slab is too thick"])
    b.quiz_a(2, "B. The colours recombine at the parallel face",
             "A slab does disperse light inside, but because its faces are "
             "parallel the colours bend back and recombine on emerging, so the "
             "output is white (just slightly shifted). A prism's inclined "
             "faces keep them separated.")
    b.quiz_q(3, "Spinning Disc", "Newton's disc, painted with the seven "
             "spectrum colours, appears white when spun rapidly. This shows "
             "that:", ["The colours disappear when moving",
              "White light is a combination of the seven colours",
              "The disc reflects only white light",
              "Fast motion removes colour"])
    b.quiz_a(3, "B. White light is a combination of the colours",
             "The eye blends the rapidly changing colours together. Their "
             "recombination producing white proves white light is a mixture "
             "of all seven colours.")
    b.quiz_q(4, "Monochromatic", "A beam of pure yellow sodium light is passed "
             "through a glass prism. What happens?",
             ["It splits into seven colours",
              "It is deviated but not dispersed (stays one colour)",
              "It disappears", "It turns white"])
    b.quiz_a(4, "B. It is deviated but not dispersed",
             "Sodium light is monochromatic — a single wavelength. The prism "
             "bends (deviates) it, but with only one colour present there is "
             "nothing to split, so no spectrum forms.")
    b.quiz_q(5, "Cause of Dispersion", "Dispersion occurs in glass but not in "
             "vacuum because, in glass, different colours have different:",
             ["Frequencies", "Speeds (and so refractive indices)",
              "Amplitudes", "Energies"])
    b.quiz_a(5, "B. Speeds (and so refractive indices)",
             "In glass each colour travels at a slightly different speed, so "
             "the refractive index differs by colour and each is deviated "
             "differently. In vacuum all colours share speed c, so there is no "
             "dispersion.")
    b.divider(2, "Part 2", "The Electromagnetic Spectrum",
              "Visible light is one small part of a much larger family")
    b.text_image("EM SPECTRUM", "The Electromagnetic Spectrum",
                 ["Visible light is just one small band of a huge family of "
                  "electromagnetic waves.",
                  "In order of increasing frequency: radio, microwave, "
                  "infrared, visible, ultraviolet, X-rays, gamma rays.",
                  "Wavelength decreases and frequency (and energy) increases "
                  "from radio to gamma.",
                  "All of them are electromagnetic waves — only their "
                  "wavelength differs."],
                 em, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="One family, many wavelengths",
                 caption="Radio (long λ) → Gamma (short λ)",
                 notes="Stress that visible light is a tiny slice. Learn the "
                       "order both ways: by increasing frequency and by "
                       "decreasing wavelength.")
    b.cards("WAVELENGTH RANGES", "Each Band by Wavelength and Source", [
        ("Radio (> 0.1 m)", "Made by oscillating circuits/aerials; received by "
         "aerials and tuned circuits."),
        ("Microwave (mm–cm)", "From klystrons/magnetrons and masers; detected "
         "by aerials and crystal detectors."),
        ("Infrared (700 nm–1 mm)", "Emitted by all warm bodies; detected by "
         "thermopiles, blackened thermometers, IR cameras."),
        ("UV → X-ray → Gamma (< 400 nm)", "From the Sun/sparks, X-ray tubes "
         "and radioactive nuclei; detected by photographic plates and "
         "fluorescence/Geiger tubes."),
    ], notes="Selina wants the wavelength range, a source and a means of "
             "detection for each band. Visible sits at 400–700 nm between IR "
             "and UV.")
    b.cards("SHARED PROPERTIES", "What All EM Waves Have in Common", [
        ("Same speed", "All travel at 3 × 10⁸ m/s in vacuum — the speed of "
         "light, c."),
        ("No medium needed", "They are transverse waves that can travel "
         "through a vacuum."),
        ("Carry energy", "Higher frequency means higher energy per wave."),
        ("c = f λ", "For every member, speed = frequency × wavelength."),
    ], notes="These four shared properties are commonly examined. Contrast "
             "with sound, which needs a medium.")
    b.statement("WAVE RELATION", "Speed, Frequency & Wavelength",
                "For any electromagnetic wave, the speed equals the frequency "
                "multiplied by the wavelength.",
                formula="c  =  f × λ        (c = 3 × 10⁸ m/s)",
                points=["If frequency goes up, wavelength goes down (c is "
                        "fixed).",
                        "Gamma rays: very high f, very short λ.",
                        "Radio waves: low f, very long λ."],
                notes="Introduce c = fλ for the numerical that follows. "
                      "Emphasise the inverse relation between f and λ.")
    b.worked("WORKED EXAMPLE", "Using c = f λ",
             "A radio station broadcasts at a frequency of 100 MHz "
             "(1 × 10⁸ Hz). Find the wavelength of the waves. (c = 3 × 10⁸ "
             "m/s)",
             ["c = f × λ   →   λ = c / f",
              "λ = (3 × 10⁸) / (1 × 10⁸)",
              "λ = 3 m"],
             "λ = 3 m — typical of FM radio waves",
             notes="Rearrange c = fλ for λ. Note radio waves are metres long, "
                   "unlike the nanometre wavelengths of light.")
    b.cards("IN NATURE", "Dispersion Around Us", [
        ("Rainbow", "Raindrops act like tiny prisms, dispersing sunlight into "
         "an arc of colours."),
        ("CD / DVD surface", "Fine grooves split white light into a shifting "
         "spectrum of colours."),
        ("Oil film & bubbles", "Thin films break white light into colours by "
         "interference and dispersion."),
        ("Diamond fire", "Strong dispersion inside diamond spreads light into "
         "flashes of colour."),
    ], notes="Connect dispersion to familiar sights. A rainbow is nature's "
             "prism made of raindrops.")
    b.bullets("RAINBOW", "How a Rainbow Forms", [
        "Sunlight enters a raindrop and refracts, dispersing into colours.",
        "The light reflects once off the back of the drop.",
        "It refracts again on leaving, spreading the colours further.",
        "Red appears on the outer edge of the bow and violet on the inner.",
    ], panel_title="Each drop is a tiny prism + mirror",
       notes="Trace the path: refraction → internal reflection → refraction. "
             "The geometry puts red outside and violet inside.")
    b.worked("WORKED EXAMPLE", "Frequency of Light",
             "Yellow light has a wavelength of 600 nm (6 × 10⁻⁷ m) in vacuum. "
             "Find its frequency. (c = 3 × 10⁸ m/s)",
             ["c = f × λ   →   f = c / λ",
              "f = (3 × 10⁸) / (6 × 10⁻⁷)",
              "f = 5 × 10¹⁴ Hz"],
             "f = 5 × 10¹⁴ Hz — visible light has frequencies near 10¹⁴ Hz",
             notes="Rearrange c = fλ for f, keeping powers of ten tidy. Visible "
                   "frequencies are around 10¹⁴ Hz.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Deviation", "a prism bends light toward its base by angle δ"),
        ("Dispersion", "white light splits because index depends on colour"),
        ("VIBGYOR", "violet shortest λ / most deviated; red longest / least"),
        ("Recombination", "an inverted prism re-makes white light"),
        ("EM spectrum", "radio → micro → IR → visible → UV → X-ray → gamma"),
        ("c = f λ", "all EM waves travel at c = 3 × 10⁸ m/s in vacuum"),
    ], notes="Rapid recap; cold-call the order of the EM spectrum.")
    b.quiz_intro("Quiz 2", "Final Check — Spectra & Waves", 5)
    b.quiz_q(1, "Order", "Which list is in order of INCREASING frequency?",
             ["Gamma, X-ray, UV, visible", "Radio, infrared, visible, "
              "ultraviolet", "Visible, infrared, microwave, radio",
              "X-ray, UV, visible, infrared"])
    b.quiz_a(1, "B. Radio, infrared, visible, ultraviolet",
             "Frequency increases from radio waves (lowest) up through "
             "infrared and visible to ultraviolet and beyond. Wavelength does "
             "the opposite — it decreases.")
    b.quiz_q(2, "Find the Wavelength", "An X-ray has a frequency of "
             "3 × 10¹⁸ Hz. Its wavelength is (c = 3 × 10⁸ m/s):",
             ["1 × 10⁻¹⁰ m", "1 × 10¹⁰ m", "9 × 10²⁶ m", "1 × 10⁻²⁶ m"])
    b.quiz_a(2, "A. 1 × 10⁻¹⁰ m",
             "λ = c / f = (3 × 10⁸) / (3 × 10¹⁸) = 1 × 10⁻¹⁰ m. Such tiny "
             "wavelengths are why X-rays can pass between atoms in the body.")
    b.quiz_q(3, "Which Travels Fastest?", "In a vacuum, which travels "
             "fastest — a radio wave, green light, or a gamma ray?",
             ["The radio wave", "Green light", "The gamma ray",
              "They all travel at the same speed"])
    b.quiz_a(3, "D. They all travel at the same speed",
             "All electromagnetic waves travel at c = 3 × 10⁸ m/s in a "
             "vacuum, regardless of frequency. They differ in wavelength and "
             "energy, not speed.")
    b.quiz_q(4, "Highest Energy", "Which of these electromagnetic radiations "
             "carries the most energy per wave?",
             ["Radio waves", "Infrared", "Visible light", "Gamma rays"])
    b.quiz_a(4, "D. Gamma rays",
             "Energy increases with frequency. Gamma rays have the highest "
             "frequency (shortest wavelength) of all, so they carry the most "
             "energy — which is why they are so penetrating and dangerous.")
    b.quiz_q(5, "Same Speed?", "Radio waves have a much longer wavelength than "
             "visible light. In vacuum, the radio waves therefore have a:",
             ["Lower speed", "Higher speed", "Lower frequency",
              "Higher frequency"])
    b.quiz_a(5, "C. Lower frequency",
             "All EM waves share the same speed c in vacuum, so from c = fλ a "
             "longer wavelength must mean a lower frequency. Speed is "
             "unchanged — only f and λ trade off.")
    b.closing("From Rainbows to Gamma Rays",
              "A prism reveals the colours hidden in white light — and visible "
              "light is just one note in a vast electromagnetic symphony.")
    return b


def deck2():
    b = Builder(FOOTER, accent=C["orange"])
    em = b.asset("g10sp_em2", D.em_spectrum("g10sp_em2"))
    scat = b.asset("g10sp_scatter", D.scattering("g10sp_scatter"))
    hero = b.asset("g10_sky_hero", scat)

    b.title("ICSE • Class 10 • Optics", "EM Radiations & Scattering",
            "Uses of each radiation  •  UV, visible & infrared  •  Why the sky "
            "is blue", img=hero)
    b.objectives([
        "State the properties and uses of each EM radiation",
        "Distinguish ultraviolet, visible and infrared radiation",
        "Explain the scattering of light",
        "Explain why the daytime sky is blue",
        "Explain why the sky looks red at sunrise and sunset",
        "Describe everyday consequences of scattering",
    ])
    b.divider(1, "Part 1", "Radiations and Their Uses",
              "What each part of the spectrum does for us")
    b.text_image("OVERVIEW", "Seven Bands, Many Uses",
                 ["Each EM band has properties suited to particular uses.",
                  "Lower-frequency waves (radio, microwave) are used mainly for "
                  "communication.",
                  "Middle bands (infrared, visible) we feel as heat and see as "
                  "light.",
                  "High-frequency waves (UV, X-rays, gamma) carry enough energy "
                  "to be useful — and harmful."],
                 em, img_side="left", img_w=6.0, img_h=3.4,
                 panel_title="Matching use to wavelength",
                 caption="From communication to medical imaging",
                 notes="Frame the band-by-band tour: properties decide uses. "
                       "Energy rises left to right.")
    b.cards("LOW FREQUENCY", "Radio & Microwaves", [
        ("Radio waves", "Carry TV and radio broadcasts and mobile-phone "
         "signals over long distances."),
        ("Microwaves", "Used in microwave ovens (heating water in food) and "
         "in satellite and mobile communication."),
        ("Why for comms?", "Long wavelengths travel far and bend around "
         "obstacles."),
        ("Heating", "Microwaves are absorbed by water molecules, warming "
         "food from within."),
    ], notes="Connect long wavelength to communication. Microwaves: resonance "
             "with water molecules heats food.")
    b.cards("MIDDLE BANDS", "Infrared & Visible Light", [
        ("Infrared", "Felt as heat; used in remote controls, thermal cameras "
         "and night-vision."),
        ("Visible light", "The only band our eyes detect; lets us see and "
         "drives photosynthesis."),
        ("Infrared heating", "Warm objects emit infrared — how we sense heat "
         "from a fire."),
        ("Optical use", "Visible light is used in photography, fibre-optic "
         "signals and illumination."),
    ], notes="Infrared = heat radiation (remotes, thermal imaging). Visible = "
             "the band the eye is tuned to.")
    b.cards("HIGH FREQUENCY", "Ultraviolet, X-rays & Gamma", [
        ("Ultraviolet", "Causes tanning and vitamin D; sterilises water; makes "
         "things fluoresce. Excess causes sunburn."),
        ("X-rays", "Pass through soft tissue but not bone — used to image "
         "fractures and in airport scanners."),
        ("Gamma rays", "Kill cancer cells and sterilise medical equipment; "
         "very penetrating."),
        ("Hazard", "All three are ionising in excess and can damage living "
         "cells."),
    ], notes="High-energy bands: powerful and useful but hazardous. Link "
             "energy (high f) to penetrating, ionising power.")
    b.bullets("DISTINCTION", "Ultraviolet vs Visible vs Infrared", [
        ("Ultraviolet", "shorter wavelength than violet; invisible; high "
         "energy; causes sunburn and fluorescence."),
        ("Visible", "the band 400–700 nm that the eye can see as colours."),
        ("Infrared", "longer wavelength than red; invisible; felt as heat."),
        ("Order of energy", "UV > visible > infrared (energy follows "
         "frequency)."),
    ], panel_title="Three neighbouring bands",
       notes="These three are commonly compared. Anchor by where they sit "
             "around the visible band and by energy order.")
    b.cards("INFRARED IN DETAIL", "Infrared — Source, Property, Detection", [
        ("Source", "Emitted by every warm body — the Sun, fires, our own "
         "skin."),
        ("Property", "Invisible; strong heating effect; longer wavelength than "
         "red light."),
        ("Detection", "A blackened-bulb thermometer, a thermopile or an "
         "infrared camera."),
        ("Uses", "Remote controls, thermal/night-vision cameras, physiotherapy "
         "heat lamps, weather satellites."),
    ], notes="Selina asks for source/property/detection/use of IR. Anchor: hot "
             "bodies emit it; it is the heat radiation just beyond red.")
    b.cards("ULTRAVIOLET IN DETAIL", "Ultraviolet — Source, Property, Detection", [
        ("Source", "The Sun, electric sparks and mercury-vapour (UV) lamps."),
        ("Property", "Invisible; higher energy than visible; causes "
         "fluorescence and affects photographic film."),
        ("Detection", "Photographic plates, or the fluorescence (glow) it "
         "produces in certain materials."),
        ("Uses", "Sterilising water and instruments, detecting forged notes, "
         "producing vitamin D in skin."),
    ], notes="UV source/property/detection/use. Most solar UV is absorbed by "
             "the ozone layer — link to the protection slide.")
    b.cards("X-RAYS IN DETAIL", "X-rays — Source, Property, Detection", [
        ("Source", "Produced in an X-ray tube when fast electrons strike a "
         "metal target."),
        ("Property", "Very penetrating and ionising; pass through flesh but "
         "not bone or metal."),
        ("Detection", "Photographic plates and fluorescent screens."),
        ("Uses", "Imaging bones and teeth, airport security scanning, studying "
         "crystal structures."),
    ], notes="X-ray source/property/detection/use. Penetrating power and the "
             "flesh-vs-bone contrast are the key facts.")
    b.cards("GAMMA RAYS IN DETAIL", "Gamma Rays — Source, Property, Use", [
        ("Source", "Emitted by the nuclei of radioactive atoms."),
        ("Property", "The most penetrating and most energetic EM radiation; "
         "strongly ionising."),
        ("Detection", "Geiger–Müller tube and photographic film."),
        ("Uses", "Killing cancer cells (radiotherapy), sterilising medical "
         "equipment and food, industrial flaw detection."),
    ], notes="Gamma: highest energy, most penetrating, from the nucleus. Tie "
             "uses to its penetrating, cell-killing power.")
    b.cards("PROTECTION", "Living With Radiation Safely", [
        ("Ozone layer", "High in the atmosphere it absorbs most harmful UV "
         "from the Sun, shielding life below."),
        ("Sunscreen & shades", "Block UV to protect skin and eyes from "
         "long-term damage."),
        ("Lead aprons", "Worn during X-ray imaging to stop rays reaching "
         "parts of the body not being scanned."),
        ("Controlled doses", "Gamma and X-ray equipment is shielded and "
         "carefully dosed to limit exposure."),
    ], notes="Tie protection measures to the hazard of high-energy radiation. "
             "The ozone layer is the planet's natural UV shield.")
    b.quiz_intro("Quiz 1", "Check Your Understanding", 5)
    b.quiz_q(1, "Match the Use", "A TV remote control sends a signal to the "
             "television using:", ["Ultraviolet", "Infrared", "X-rays",
              "Radio waves of visible light"])
    b.quiz_a(1, "B. Infrared",
             "Remote controls use infrared, which is invisible to us but "
             "easily produced and detected over short distances. Infrared is "
             "also why we feel heat from warm objects.")
    b.quiz_q(2, "Through the Body", "X-rays are used to photograph broken "
             "bones because they:",
             ["Are reflected by skin", "Pass through soft tissue but are "
              "absorbed by bone", "Are visible to the eye",
              "Cannot pass through the body"])
    b.quiz_a(2, "B. Pass through soft tissue but absorbed by bone",
             "X-rays penetrate soft tissue but are stopped by dense bone, so "
             "bones cast a shadow on the film — producing the familiar X-ray "
             "image of the skeleton.")
    b.quiz_q(3, "Sunburn", "Spending too long in strong sunlight causes "
             "sunburn. The radiation mainly responsible is:",
             ["Infrared", "Visible light", "Ultraviolet", "Radio waves"])
    b.quiz_a(3, "C. Ultraviolet",
             "Ultraviolet has more energy than visible light and damages skin "
             "cells, causing sunburn (and, in excess, skin cancer). Sunscreen "
             "and the ozone layer block much of it.")
    b.quiz_q(4, "Night Vision", "A security camera can 'see' a warm person in "
             "complete darkness. It must be detecting:",
             ["Ultraviolet given off by the person",
              "Infrared (heat) radiation from the person",
              "X-rays from the person", "Visible light only"])
    b.quiz_a(4, "B. Infrared (heat) radiation",
             "Warm bodies emit infrared radiation. A thermal/IR camera detects "
             "this heat radiation, so it works even with no visible light — "
             "the basis of night vision.")
    b.quiz_q(5, "Detecting UV", "Ultraviolet radiation is often detected by "
             "the fact that it:", ["Feels hot on the skin",
              "Makes certain materials fluoresce (glow)",
              "Is easily seen as violet", "Bends around corners"])
    b.quiz_a(5, "B. Makes certain materials fluoresce",
             "UV itself is invisible, but it makes some substances glow with "
             "visible light (fluorescence) and darkens photographic film — both "
             "used to detect it, as in checking banknotes.")
    b.divider(2, "Part 2", "Scattering of Light",
              "Why the sky is blue and sunsets are red")
    b.text_image("SCATTERING", "What Is Scattering?",
                 ["Tiny particles and air molecules redirect light in all "
                  "directions — this is scattering.",
                  "Shorter wavelengths (blue, violet) are scattered much more "
                  "than longer ones (red).",
                  "So blue light is scattered all across the sky.",
                  "Scattering depends strongly on wavelength — blue scatters "
                  "far more than red."],
                 scat, img_side="left", img_w=5.8, img_h=3.6,
                 panel_title="Light redirected by the air",
                 caption="Blue is scattered most by air molecules",
                 notes="Define scattering and the key fact: shorter wavelength "
                       "scatters more. This single idea explains the next two "
                       "slides.")
    b.statement("HOW MUCH?", "Scattering Depends Strongly on Wavelength",
                "The amount of scattering by tiny particles rises very steeply "
                "as the wavelength gets shorter.",
                formula="amount of scattering  ∝  1 / λ⁴",
                points=["Halving the wavelength scatters light about 16 times "
                        "more.",
                        "So blue/violet (short λ) scatter far more than red "
                        "(long λ).",
                        "Scattering of light by fine (colloidal) particles is "
                        "called the Tyndall effect."],
                notes="The 1/λ⁴ rule (Rayleigh) explains why blue dominates the "
                      "sky. Name the Tyndall effect — scattering by colloidal "
                      "particles such as dust, smoke and fine droplets.")
    b.cards("CONSEQUENCES", "Blue Skies and Red Sunsets", [
        ("Why the sky is blue", "Air scatters blue sunlight in all "
         "directions, so the whole sky glows blue."),
        ("Why sunsets are red", "At sunset light travels through more air; "
         "blue is scattered away, leaving red and orange to reach us."),
        ("Why space is black", "With no air to scatter light, the sky away "
         "from the Sun is black to astronauts."),
        ("Danger signals are red", "Red scatters least, so red light travels "
         "furthest through fog — used for stop signs and signals."),
    ], notes="Each consequence follows from 'blue scatters more'. The red "
             "danger-signal point is a favourite application question.")
    b.bullets("MORE EFFECTS", "Scattering Around Us", [
        ("Clouds look white", "Large water droplets scatter all colours "
         "equally, so clouds appear white."),
        ("Why blue, not violet?", "Violet scatters even more, but the Sun "
         "sends less violet and our eyes are less sensitive to it — so the sky "
         "looks blue."),
        ("Reddened Sun", "The rising or setting Sun itself looks red for the "
         "same reason its surroundings do."),
        ("Clear vs hazy", "More dust and particles mean more scattering and a "
         "paler sky."),
    ], panel_title="Everyday sights explained",
       notes="Extend the idea to clouds (all colours scattered → white) and "
             "haze. Reinforces wavelength-dependence.")
    b.recap("WRAP UP", "Quick Recap", [
        ("Radio / microwave", "communication; microwaves also heat food"),
        ("Infrared / visible", "heat we feel; light we see"),
        ("UV / X-ray / gamma", "useful but hazardous high-energy radiation"),
        ("UV vs visible vs IR", "energy order UV > visible > infrared"),
        ("Scattering", "shorter wavelengths scatter more than longer ones"),
        ("Sky & sunset", "blue sky from scattered blue; red sunset as blue is "
         "removed"),
    ], notes="Rapid recap; cold-call a use for each band and the scattering "
             "explanations.")
    b.quiz_intro("Quiz 2", "Final Check — Radiations & Scattering", 5)
    b.quiz_q(1, "Astronaut's Sky", "An astronaut in space, looking away from "
             "the Sun, sees a black sky instead of a blue one because:",
             ["The Sun is switched off", "There is no air to scatter "
              "sunlight", "Space absorbs all blue light",
              "Their visor blocks blue"])
    b.quiz_a(1, "B. There is no air to scatter sunlight",
             "The sky is blue because air scatters blue sunlight toward us. In "
             "space there are no air molecules to scatter light, so the sky "
             "(away from the Sun) looks black.")
    b.quiz_q(2, "Why Red at Sunset", "The setting Sun appears red because, "
             "near the horizon, sunlight:",
             ["Travels through more air, so blue is scattered away",
              "Slows down and turns red", "Reflects off clouds",
              "Changes frequency"])
    b.quiz_a(2, "A. Travels through more air; blue scattered away",
             "At sunset light skims through a long path of atmosphere. Most of "
             "the blue is scattered out before it reaches us, leaving the red "
             "and orange that we see.")
    b.quiz_q(3, "Best for Signals", "Why are danger and stop signals coloured "
             "red rather than blue?",
             ["Red is brighter than blue", "Red is scattered least, so it "
              "travels furthest through fog", "Blue is invisible at night",
              "Red light is faster"])
    b.quiz_a(3, "B. Red is scattered least, travels furthest",
             "Because red has the longest wavelength it is scattered the least "
             "by fog and dust, so it remains visible from a greater distance — "
             "ideal for warnings.")
    b.quiz_q(4, "Sterilising Water", "Some water purifiers use ultraviolet "
             "lamps because UV radiation:",
             ["Is visible and bright", "Has enough energy to kill germs",
              "Heats the water quickly", "Is a type of sound wave"])
    b.quiz_a(4, "B. Has enough energy to kill germs",
             "Ultraviolet carries more energy than visible light — enough to "
             "damage the cells of bacteria and viruses, sterilising the water "
             "without chemicals.")
    b.quiz_q(5, "Clouds", "Clouds usually look white, not blue, because their "
             "water droplets:",
             ["Absorb all blue light", "Scatter all colours of light about "
              "equally", "Reflect only white paint", "Emit their own light"])
    b.quiz_a(5, "B. Scatter all colours about equally",
             "Cloud droplets are much larger than air molecules, so they "
             "scatter every colour by roughly the same amount. The mixture of "
             "all colours scattered together looks white.")
    b.closing("Light Tells a Story",
              "The same scattering that paints the sky blue sets it ablaze at "
              "sunset — physics you can watch every evening.")
    return b


def build():
    for fname, fn in [("G10_S53_Spectrum_1.pptx", deck1),
                      ("G10_S54_Spectrum_2.pptx", deck2)]:
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
