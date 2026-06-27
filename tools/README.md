# ICSE Physics Teaching Decks — Build System

Generates 16:9 PowerPoint teaching decks for **ICSE Physics, Grades 6–10**,
one deck per *teach* session (Workout / CPT / Revision / Term-Test sessions are
skipped — those are Phase 2). Scope for this phase: **only sessions after
day/session 29** in each grade's planner sheet.

The visual system is reverse-engineered from the reference deck
`Gases_and_Gas_Laws_ICSE10.pptx` (colours, fonts, badge/title/footer chrome,
card style, quiz Q/A pairs).

## Files

| File | Purpose |
|------|---------|
| `engine.py` | `Builder` class — all slide layouts + design tokens + QA |
| `diagrams.py` | Physics schematics as **SVG → PNG** (never drawn on the slide) |
| `images.py` | Optional real photos / AI images (Qwen or URL) → `assets/img/` |
| `preview.py` | Render any `.pptx` → PNG per slide for visual QA |
| `decks.json` | The full list of decks to build, per grade, with topics |
| `deck_g10_refraction.py` | Worked example: two complete Grade-10 decks |

## Build & QA workflow

```bash
python3 tools/deck_g10_refraction.py     # builds .pptx into ppt/Grade10/, prints QA
python3 tools/preview.py ppt/Grade10/X.pptx build/preview        # all slides
python3 tools/preview.py ppt/Grade10/X.pptx build/preview 1,4,14 # selected
```
`Builder.qa()` reports text overlaps and off-slide content. The previewer
word-wraps text and draws a **red dashed box** around any text that overflows
its container — both must be clean before a deck is considered done.

## Deck recipe (≈ 35–40 slides)

1. `title(eyebrow, title, subtitle, img)`
2. `objectives([...6 outcomes...])`
3. `divider(1, "Part 1", ...)`
4–N. content slides (mix the layouts below; one diagram every 2–3 slides)
   * `text_image(badge, title, bullets, img, img_side, panel_title, caption, notes)`
   * `cards(badge, title, [(head, body) x2 or x4], notes)`
   * `bullets(badge, title, [str | (head, sub)], panel_title, notes)`
   * `statement(badge, title, statement, formula, points, notes)`
   * `worked(badge, title, problem, [steps], answer, notes)`
* **Quiz 1 (mid)** — covers Part 1 only:
  `quiz_intro("Quiz 1", title, n)` then for each Q a pair:
  `quiz_q(no, topic, question, [A,B,C,D])` + `quiz_a(no, answer, why)`
* `divider(2, "Part 2", ...)` + more content
* `recap(badge, title, [(head, sub)...])`
* **Quiz 2 (end)** — covers the whole session (3–5 questions)
* `closing(title, message)`

Rules baked into the brief:
* 3–5 questions per quiz; **every question = two slides** (question, then
  answer reveal with a "Why").
* **No teacher instructions on slides** — put all teaching guidance in the
  `notes=` argument (speaker notes).
* Accent colour per deck via `Builder(footer, accent=C["teal"|"purple"|...])`.

## Diagrams

`diagrams.py` returns a PNG path. Current catalog:
`refraction_bending`, `glass_block`, `real_apparent_depth`, `prism_refraction`,
`total_internal_reflection`, `reflection_law`, `optical_fibre`,
`reflecting_prism`. Add new schematics here (or in `diagrams_extra.py` to avoid
merge conflicts when working in parallel). Keep them accurate — they are the
teaching content, not decoration.

## Real photos / AI images (optional)

Schematics stay as SVG. For *realistic* pictures (rainbow, prism on a desk,
optical-fibre cable, lab apparatus) use `images.py`:

```bash
export QWEN_API_KEY=...      # from the workspace key CSV; never commit it
python3 tools/images.py manifest.json
```
A layout then prefers the asset automatically:
`img = b.asset("g10_prism_photo", prism_svg)`.

> Note: in a web session whose **network policy blocks general web hosts**, both
> download and Qwen generation return 403 at the egress proxy and the build
> falls back to the SVG diagram. Run the asset step from a session whose policy
> allows the provider host (see code.claude.com/docs networking).
