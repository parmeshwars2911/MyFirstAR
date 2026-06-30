# Workouts & Homework — Assessment Build System

Generates two student-assessment deliverables from per-session question banks,
reusing the teaching-deck engine so the look matches the concept decks.

| Deliverable | What | Format | Output |
|-------------|------|--------|--------|
| **Workout** | One quiz deck per chapter — **20 MCQs + 5 subjective** | `.pptx` (16:9) | `workouts/Grade<NN>/` |
| **Homework** | One worksheet per teach **and** per workout session — **10 MCQs** + answer key | `.pdf` (A4) | `homework/Grade<NN>/` |

## Files
- `assessment.py` — the engine. `build_workout(...)` (PPT) and
  `build_homework(...)` (PDF), plus `balance_options(...)` which spreads the
  correct answer evenly across A–D and shuffles distractors (deterministic).
  Workout MCQs use **exactly the same question/answer-reveal layout as the
  concept-deck quizzes** (`slidekit.quiz`); subjective questions get a matching
  question slide + model-answer reveal slide.
- `bank_g06.py` — Grade 6 question bank (data) + `build()` driver. One module
  per grade; `bank_g07.py … bank_g10.py` follow the same shape.

## Syllabus rule (strict)
- **Workout** covers all the concept lessons taught in that chapter *before* the
  workout (e.g. Light-1 + Light-2 → one Light workout). Every question is drawn
  only from those lessons.
- **Homework** covers only the topics of its single session (a teach session, or
  the workout's whole-chapter scope). Topics come from `tools/decks.json`.

## Build
```bash
pip install python-pptx cairosvg reportlab      # one-time
python3 tools/bank_g06.py                        # builds all G6 workouts + homework
```
`build()` asserts 20/5/10 counts, 4 options per MCQ and a valid answer index,
and `Builder.qa()` reports any slide overlap / off-slide text (must be clean).

## QA previews (not committed; `build/` is git-ignored)
```bash
python3 tools/preview.py workouts/Grade06/G06_Light_Workout.pptx build/prev 5,6
python3 -c "import fitz; fitz.open('homework/Grade06/G06_S52_Light_1_Homework.pdf')[0].get_pixmap(dpi=110).save('build/hw.png')"
```

## Adding a grade
Copy `bank_g06.py` to `bank_g07.py`, fill the MCQ/subjective banks from that
grade's `decks.json` topics (keep it in-syllabus), set one `WORKOUTS` entry per
chapter and one `HOMEWORKS` entry per session, then run the module.
