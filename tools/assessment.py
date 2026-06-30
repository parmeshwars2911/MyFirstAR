"""
Assessment engine — Workout (quiz) PPTs and Homework PDFs.

Two deliverables are built from the same per-session question banks:

  * build_workout(...)  -> a 16:9 PowerPoint "Workout" deck. Practice MCQs use
    exactly the same question/answer-reveal layout as the teaching-deck quizzes
    (slidekit.quiz), so the look matches the concept decks. 20 MCQs + 5
    subjective (long-answer) questions, each shown as a question slide followed
    by a mirrored answer-reveal / model-answer slide.

  * build_homework(...) -> a print-ready A4 PDF worksheet (reportlab) with 10
    MCQs for a single teach or workout session, plus an answer key.

The MCQ data format (shared by both):
    {"topic": str, "q": str, "options": [a, b, c, d],
     "correct": 0..3, "why": str}
The subjective data format (workout only):
    {"topic": str, "q": str, "marks": int, "answer": [point, point, ...]}

Syllabus discipline: every question must come from the topics of the listed
session(s). Nothing out of syllabus.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from engine import Builder, C, LABEL_FONT
import slidekit as SK
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
import random


# ---------------------------------------------------------------------------
# Option balancing — spread the correct answer evenly across A-D and shuffle
# the distractors, so the answer key is not guessable. Deterministic (seeded)
# so rebuilds are stable. Safe because every "why" refers to the option by
# meaning, never by its letter.
# ---------------------------------------------------------------------------
def balance_options(mcqs, seed=0):
    rnd = random.Random(seed)
    n = len(mcqs)
    targets = [i % 4 for i in range(n)]
    rnd.shuffle(targets)
    out = []
    for q, t in zip(mcqs, targets):
        opts = q["options"]
        correct = opts[q["correct"]]
        others = [o for j, o in enumerate(opts) if j != q["correct"]]
        rnd.shuffle(others)
        new = []
        oi = 0
        for pos in range(4):
            if pos == t:
                new.append(correct)
            else:
                new.append(others[oi])
                oi += 1
        nq = dict(q)
        nq["options"] = new
        nq["correct"] = t
        out.append(nq)
    return out


# ---------------------------------------------------------------------------
# Subjective (long-answer) question + model-answer reveal slides.
# Drawn with the Builder primitives so the chrome matches the rest of the deck.
# ---------------------------------------------------------------------------
def _subjective_q(b, qno, topic, question, marks):
    s = b._slide(C["bg_light"])
    n = b._next()
    b._chrome(s, "SUBJECTIVE QUESTION", f"Q{qno} — {topic}", b.accent, n)
    b._box(s, 0.7, 2.1, 11.9, 2.7, fill=C["card"], shadow=True,
           shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)
    b._text(s, 1.1, 2.35, 11.1, 2.2,
            [[{"t": question, "size": 21, "bold": True, "color": C["text"]}]],
            anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.1)
    # marks chip, bottom-right of the card
    b._box(s, 10.7, 5.05, 1.9, 0.55, fill=b.accent,
           shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.4)
    b._text(s, 10.7, 5.05, 1.9, 0.55,
            [[{"t": f"[ {marks} marks ]", "size": 14, "bold": True,
               "color": "FFFFFF"}]], align=PP_ALIGN.CENTER,
            anchor=MSO_ANCHOR.MIDDLE)
    b._text(s, 0.75, 5.05, 8.0, 0.55,
            [[{"t": "Attempt this in your notebook before the answer reveals.",
               "size": 14, "italic": True, "color": C["muted"]}]],
            anchor=MSO_ANCHOR.MIDDLE)
    b._notes(s, f"Subjective practice on '{topic}'. Give students time to write "
                f"a full answer, then reveal the model points.")
    return s


def _subjective_a(b, qno, topic, question, points, marks):
    s = b._slide(C["bg_light"])
    n = b._next()
    b._chrome(s, "MODEL ANSWER", f"Q{qno} — {topic}", C["green"], n)
    # compact question reminder
    b._box(s, 0.7, 1.95, 11.9, 1.05, fill="EEF2F7",
           shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
    b._text(s, 1.1, 1.95, 11.1, 1.05,
            [[{"t": "Q.  ", "size": 14, "bold": True, "color": C["green"]},
              {"t": question, "size": 14, "color": C["text"]}]],
            anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.02)
    # model-answer card with bullet points
    b._box(s, 0.7, 3.15, 11.9, 3.6, fill=C["card"], shadow=True,
           shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.03)
    paras = []
    for p in points:
        paras.append([{"t": "•  ", "size": 15, "bold": True,
                       "color": C["green"]},
                      {"t": p, "size": 15, "color": C["text"]}])
    b._text(s, 1.1, 3.45, 11.1, 3.1, paras, space=9, line_spacing=1.05)
    b._notes(s, f"Model answer for Q{qno}. Award up to {marks} marks; accept "
                f"equivalent correct wording.")
    return s


# ---------------------------------------------------------------------------
# Workout deck
# ---------------------------------------------------------------------------
def build_workout(out_path, *, chapter, accent, title, subtitle,
                  syllabus, mcqs, subjectives, closing_msg=None):
    """Build a Workout (quiz) deck.

    chapter     : chapter name (used in the title eyebrow)
    syllabus    : list of (lesson_label, topics_string) the workout covers
    mcqs        : list of MCQ dicts (expected 20)
    subjectives : list of subjective dicts (expected 5)
    """
    b = Builder("", accent=accent, brand="")

    # --- title ---
    b.title(chapter, title, subtitle)

    # --- syllabus / scope slide ---
    b.bullets(
        "WORKOUT SCOPE", "What This Workout Covers",
        [(lesson, topics) for lesson, topics in syllabus],
        panel_title="Syllabus for this practice session",
        notes="State the scope up front: every question is drawn only from "
              "these lessons. Nothing outside this syllabus appears.")

    # --- Section A : MCQs ---
    b.divider(1, "Section A", "Multiple-Choice Questions",
              f"{len(mcqs)} questions — choose the single best option")
    b.quiz_intro("Section A", "Multiple-Choice Practice", len(mcqs))
    for i, q in enumerate(mcqs, 1):
        SK.quiz(b, i, q["topic"], q["q"], q["options"], q["correct"], q["why"])

    # --- Section B : Subjective ---
    b.divider(2, "Section B", "Subjective Questions",
              f"{len(subjectives)} long-answer questions — write full answers")
    b.quiz_intro("Section B", "Subjective Practice", len(subjectives))
    for i, q in enumerate(subjectives, 1):
        marks = q.get("marks", 3)
        _subjective_q(b, i, q["topic"], q["q"], marks)
        _subjective_a(b, i, q["topic"], q["q"], q["answer"], marks)

    # --- closing ---
    b.closing("Well Practised!",
              closing_msg or "Review every answer you missed and re-read those "
              "topics in your notes before the test.")

    issues = b.qa()
    b.save(out_path)
    return b, issues


# ---------------------------------------------------------------------------
# Homework PDF (reportlab)
# ---------------------------------------------------------------------------
def build_homework(out_path, *, grade, chapter, lesson, kind, syllabus_topics,
                   mcqs):
    """Build a print-ready A4 homework worksheet with `len(mcqs)` MCQs + key.

    grade           : e.g. "Class 6"
    chapter         : chapter name
    lesson          : lesson / session label
    kind            : "Concept" or "Workout"
    syllabus_topics : one-line string of the topics this homework covers
    mcqs            : list of MCQ dicts (expected 10)
    """
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.units import mm
    from reportlab.lib import colors
    from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
    from reportlab.lib.enums import TA_LEFT
    from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
                                    Paragraph, Spacer, Table, TableStyle,
                                    HRFlowable, KeepTogether)

    ACCENT = colors.HexColor("#" + C["teal"])
    DARK = colors.HexColor("#" + C["bg_dark"])
    MUTED = colors.HexColor("#" + C["muted"])

    styles = getSampleStyleSheet()
    h_eyebrow = ParagraphStyle(
        "eyebrow", parent=styles["Normal"], fontName="Helvetica-Bold",
        fontSize=9, textColor=ACCENT, spaceAfter=2, leading=11)
    h_title = ParagraphStyle(
        "title", parent=styles["Normal"], fontName="Helvetica-Bold",
        fontSize=18, textColor=DARK, spaceAfter=2, leading=21)
    h_meta = ParagraphStyle(
        "meta", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5,
        textColor=MUTED, spaceAfter=1, leading=13)
    h_syll = ParagraphStyle(
        "syll", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5,
        textColor=DARK, leading=13)
    q_style = ParagraphStyle(
        "q", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=10.5,
        textColor=DARK, leading=14, spaceBefore=8, spaceAfter=3)
    opt_style = ParagraphStyle(
        "opt", parent=styles["Normal"], fontName="Helvetica", fontSize=10,
        textColor=colors.HexColor("#222831"), leading=14, alignment=TA_LEFT)
    sec_style = ParagraphStyle(
        "sec", parent=styles["Normal"], fontName="Helvetica-Bold", fontSize=12,
        textColor=ACCENT, spaceBefore=6, spaceAfter=6, leading=15)
    key_style = ParagraphStyle(
        "key", parent=styles["Normal"], fontName="Helvetica", fontSize=9.5,
        textColor=DARK, leading=14)

    def _header_footer(canvas, doc):
        canvas.saveState()
        # top accent bar
        canvas.setFillColor(ACCENT)
        canvas.rect(0, A4[1] - 6 * mm, A4[0], 6 * mm, stroke=0, fill=1)
        # footer
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(18 * mm, 12 * mm,
                          f"{chapter} — {lesson}  •  ICSE {grade} Physics")
        canvas.drawRightString(A4[0] - 18 * mm, 12 * mm,
                               f"Page {doc.page}")
        canvas.restoreState()

    doc = BaseDocTemplate(
        out_path, pagesize=A4,
        leftMargin=18 * mm, rightMargin=18 * mm,
        topMargin=16 * mm, bottomMargin=18 * mm,
        title=f"{chapter} {lesson} Homework", author="Infinity Learn")
    frame = Frame(doc.leftMargin, doc.bottomMargin,
                  doc.width, doc.height, id="main")
    doc.addPageTemplates([PageTemplate(id="all", frames=[frame],
                                       onPage=_header_footer)])

    story = []
    story.append(Paragraph(f"HOMEWORK · {kind.upper()}", h_eyebrow))
    story.append(Paragraph(f"{chapter} — {lesson}", h_title))
    story.append(Paragraph(
        f"ICSE {grade} Physics &nbsp;·&nbsp; {len(mcqs)} MCQs &nbsp;·&nbsp; "
        f"1 mark each &nbsp;·&nbsp; Name: ______________________  "
        f"Date: ____________", h_meta))
    story.append(Spacer(1, 3))
    story.append(HRFlowable(width="100%", thickness=0.7, color=ACCENT,
                            spaceBefore=2, spaceAfter=4))
    story.append(Paragraph(
        f"<b>Syllabus:</b> {syllabus_topics}", h_syll))
    story.append(Spacer(1, 4))
    story.append(Paragraph(
        "<b>Instructions:</b> Each question has one correct option. Tick or "
        "circle the letter of the best answer. Attempt all questions.", h_meta))
    story.append(Spacer(1, 4))

    labels = "ABCD"
    for i, q in enumerate(mcqs, 1):
        flow = [Paragraph(f"{i}. {q['q']}", q_style)]
        # two-column option grid
        opts = [Paragraph(f"<b>{labels[j]}.</b>&nbsp; {opt}", opt_style)
                for j, opt in enumerate(q["options"])]
        # pad to 4
        while len(opts) < 4:
            opts.append(Paragraph("", opt_style))
        tbl = Table([[opts[0], opts[1]], [opts[2], opts[3]]],
                    colWidths=[doc.width / 2.0 - 2, doc.width / 2.0 - 2])
        tbl.setStyle(TableStyle([
            ("VALIGN", (0, 0), (-1, -1), "TOP"),
            ("LEFTPADDING", (0, 0), (-1, -1), 6),
            ("RIGHTPADDING", (0, 0), (-1, -1), 6),
            ("TOPPADDING", (0, 0), (-1, -1), 1),
            ("BOTTOMPADDING", (0, 0), (-1, -1), 1),
        ]))
        flow.append(tbl)
        story.append(KeepTogether(flow))

    # --- answer key ---
    story.append(Spacer(1, 10))
    story.append(HRFlowable(width="100%", thickness=0.7, color=MUTED,
                            spaceBefore=4, spaceAfter=4))
    story.append(Paragraph("Answer Key", sec_style))
    key_cells = []
    for i, q in enumerate(mcqs, 1):
        key_cells.append(f"<b>{i}.</b> {labels[q['correct']]}")
    # arrange answer key in rows of 5
    rows = []
    row = []
    for idx, cell in enumerate(key_cells, 1):
        row.append(Paragraph(cell, key_style))
        if idx % 5 == 0:
            rows.append(row)
            row = []
    if row:
        while len(row) < 5:
            row.append(Paragraph("", key_style))
        rows.append(row)
    ktbl = Table(rows, colWidths=[doc.width / 5.0] * 5)
    ktbl.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 2),
    ]))
    story.append(ktbl)

    doc.build(story)
    return out_path
