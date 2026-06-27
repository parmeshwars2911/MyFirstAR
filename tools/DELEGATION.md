# Delegation Brief — second agent

You are building ICSE **Physics** teaching decks alongside another agent who
owns the shared build system and **Grades 9 & 10**. Your job: **Grades 6, 7, 8**
(26 decks). Same repo, same branch `claude/icse-physics-ppt-creation-s2pi82`.

## Hard rules to avoid conflicts
- **Do NOT edit** `tools/engine.py`, `tools/diagrams.py`, `tools/preview.py`,
  `tools/images.py`. They are shared and stable.
- Add any **new diagrams** to a new file `tools/diagrams_extra.py` (same style:
  build an SVG string, rasterise with cairosvg to `build/img/`, return the path).
- Create one deck module per grade: `tools/deck_g06.py`, `tools/deck_g07.py`,
  `tools/deck_g08.py`. Output `.pptx` into `ppt/Grade06/`, `ppt/Grade07/`,
  `ppt/Grade08/`.
- Commit only the files you own + your `ppt/Grade06..08/*.pptx`. Pull before push.

## Read first
- `tools/README.md` — the Builder API, the deck recipe, and the QA workflow.
- `tools/deck_g10_refraction.py` — a complete worked example. **Mirror its
  structure, depth, and tone.** Copy its patterns for quizzes, worked examples
  and notes.

## What each deck must be
- ~**35–40 slides**, 16:9, matching the template (the Builder enforces the look).
- Title → objectives → Part 1 → content → **Quiz 1 (mid, covers Part 1, 3–5 Q)**
  → Part 2 → content → recap → **Quiz 2 (end, whole session, 3–5 Q)** → closing.
- **Every quiz question = two slides**: question, then answer reveal with a "Why".
- A diagram every 2–3 content slides. Use accurate schematics, not decoration.
- **No teacher instructions on any slide.** All teaching guidance goes in the
  `notes=` speaker-notes argument of each layout call.
- Content must match the **ICSE (Selina / Concise Physics)** treatment of the
  listed topics for that grade. Pitch language to the grade (simpler for G6).
- Pick a per-deck accent: G6 `C["teal"]`, G7 `C["orange"]`, G8 `C["purple"]`
  (or vary by chapter; just be consistent within a deck).
- Footer = `"<Chapter Name>  •  ICSE Class <grade> Physics"`.

## Diagrams you'll likely need (build in diagrams_extra.py)
- **Light/Reflection (G6 S52-53, G7 S37-38, G8 S43-44):** reflection law
  (already in `diagrams.py` — reuse), plane-mirror image, pinhole camera,
  shadow/eclipse, refraction bending (reuse), spherical mirror ray diagram.
- **Simple Machines (G6 S30-31):** levers (3 classes), pulley systems,
  inclined plane, wheel & axle, wedge, screw.
- **Magnetism / E&M (G6 S69-70, G7 S76-78, G8 S71-72):** bar-magnet field
  lines, electromagnet (coil), simple circuit symbols, series vs parallel,
  electric bell, fuse / 3-pin plug.
- **Heat (G7 S55-57, G8 S53-54):** thermometer/scales, conduction-convection-
  radiation, thermal expansion (bimetallic strip), states/molecular motion.
- **Sound (G7 S66-67, G8 S61-62):** longitudinal wave (compression/rarefaction),
  wave terms (wavelength/amplitude), reflection/echo, human ear.
- **Energy (G8 S33-34):** PE↔KE conversion (pendulum / falling body),
  energy transformation chains.

## The 26 decks (session #, chapter, lesson, topics)

### Grade 6 — 6 decks
- **S30** Simple Machines — *Simple Machines 1*: Work & energy, machines,
  principle of a machine, efficiency, ideal vs actual machine, functions,
  mechanical advantage, levers, principle of a lever, orders of levers.
- **S31** Simple Machines — *Simple Machines 2*: Pulley, MA of pulley,
  wheel & axle, inclined plane, wedge, screw, care of machines.
- **S52** Light — *Light 1*: Light, sources of light, luminous & non-luminous
  bodies, key terms, rectilinear propagation and its applications.
- **S53** Light — *Light 2*: Pinhole camera, shadow, eclipses.
- **S69** Magnetism — *Magnetism 1*: Discovery of magnets, natural/artificial
  magnets, magnetic & non-magnetic substances, characteristics & properties of
  a magnet, magnetic field around a magnet, Earth's magnetic field.
- **S70** Magnetism — *Magnetism 2*: Making a magnet, electromagnets, care &
  storage of magnets, demagnetisation.

### Grade 7 — 10 decks
- **S37** Light Energy 1: Light, reflection, plane mirror, terms, laws of
  reflection + verification, normal incidence, image formation by a plane mirror.
- **S38** Light Energy 2: Real vs virtual images, lateral inversion,
  characteristics of plane-mirror image, regular vs irregular reflection, uses
  of a plane mirror, speed of light, colours of white light, primary/secondary
  colours, subtraction of colours.
- **S55** Heat 1: Heat as energy, units of heat, temperature, units & scales of
  temperature, measurement of temperature.
- **S56** Heat 2: Effects of heat, thermal expansion.
- **S57** Heat 3: Three modes of heat transfer, conductors & insulators and
  daily-life applications, convection examples, black/white surfaces, thermos.
- **S66** Sound 1: Sound, production by vibrations, sources, needs a medium,
  longitudinal waves in air.
- **S67** Sound 2: Wave terms, audible/ultrasonic/infrasonic, characteristics
  of sound, speed of sound, reflection & absorption of sound.
- **S76** Electricity and Magnetism 1: Law of magnetism, repulsion is the sure
  test, magnetic field, electromagnet, making one, uses of electromagnets.
- **S77** Electricity and Magnetism 2: Electric bell, magnetic declination,
  uses & sources of electricity, dry cells in a torch, flow in a circuit,
  conductors & insulators.
- **S78** Electricity and Magnetism 3: Charges constitute current, circuit
  symbols & functions, series vs parallel circuits, safety precautions.

### Grade 8 — 10 decks
- **S33** Energy 1: Work, definition & units of work, energy, unit of energy,
  mechanical energy, examples of potential energy.
- **S34** Energy 2: Gravitational PE expression, kinetic energy, PE↔KE
  conversion, different forms of energy, energy transformation examples.
- **S43** Light Energy 1: Speed of light in media, refraction, terms, laws of
  refraction, effects of refraction, early sunrise/late sunset, mirage,
  refraction through a glass block & prism, dispersion.
- **S44** Light Energy 2: Cause of dispersion, spherical mirrors, kinds & terms,
  focus & focal length, ray-diagram rules, real vs virtual image, images by a
  concave mirror, uses of a concave mirror.
- **S53** Heat Transfer 1: Effects of heat, temperature & molecular motion,
  liquid→vapour, evaporation by molecular motion, boiling, evaporation vs
  boiling.
- **S54** Heat Transfer 2: Thermal expansion in solids (linear), in liquids,
  in gases, variation of density with temperature.
- **S61** Sound 1: Nature of sound, propagation, characteristics, frequency &
  time period.
- **S62** Sound 2: Audible range, speed of sound, reflection of sound, human
  ear, music vs noise.
- **S71** Electricity 1: Electrical energy & power in a circuit, transmission
  from station to consumer, supply to a house, colour coding of wires,
  pole-to-board connection, commercial unit of energy (kWh).
- **S72** Electricity 2: Electric fuse & its characteristics, MCB, household
  circuits, earthing, power rating of appliances, household consumption,
  hazards & precautions.

## Done = for every deck
1. `Builder.qa()` prints **no overlaps / off-slide**.
2. `tools/preview.py <deck> build/preview` shows **no red overflow boxes** and
   reads cleanly on spot-checked slides (title, a content slide, a quiz pair).
3. Slide count 35–40, two quizzes, all answer-reveal pairs present, notes on
   every content slide, zero teacher text on slides.
