"""
Printable worksheet engine (reportlab) for DPS-Monarch, NCERT Class 7 Science.

Builds A4 worksheets from a list of sections. Supported item types let one
worksheet mix Objective, Subjective and Olympiad styles:

  mcq            : {"q","options"[4],"correct"(0-3)[,"why"]}
  fill           : {"q" (use ______ for the blank), "answer"}
  tf             : {"q", "answer"(bool)}
  match          : {"colA":[...], "colB":[...], "pairs":[(iA,iB)...]}
  assertion      : {"a","r","answer"("A"/"B"/"C"/"D")}
  short/long     : {"q","marks","answer":[points...]}  (ruled answer space)

Every worksheet ends with an Answer Key on the last page (per decision).
Use build_worksheet(...) once per worksheet; qa_pdf(...) to spot-check overflow.
"""
import os
import sys

sys.path.insert(0, os.path.dirname(__file__))

from assessment import _pdf_rich          # XML-escape + Unicode superscripts
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT
from reportlab.platypus import (BaseDocTemplate, PageTemplate, Frame,
                                Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)

# Infinity Learn brand palette (from the logo: bright cyan-blue + deep navy)
IL_BLUE = colors.HexColor("#1CA0E0")     # bright cyan-blue
IL_NAVY = colors.HexColor("#0B1E4B")     # deep navy
DARK = IL_NAVY
MUTED = colors.HexColor("#5B667A")
LINE = colors.HexColor("#C9D6E5")

# Official logo, dropped in automatically if present (see LOGO_PATH below).
LOGO_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..",
                                         "assets", "img",
                                         "infinity_learn_logo.png"))


def _styles():
    from reportlab.lib.enums import TA_CENTER
    ss = getSampleStyleSheet()
    return dict(
        eyebrow=ParagraphStyle("eb", parent=ss["Normal"],
                               fontName="Helvetica-Bold", fontSize=10,
                               spaceAfter=3, leading=12, alignment=TA_CENTER),
        title=ParagraphStyle("ti", parent=ss["Normal"],
                             fontName="Helvetica-Bold", fontSize=24,
                             textColor=IL_NAVY, spaceAfter=3, leading=27,
                             alignment=TA_CENTER),
        meta=ParagraphStyle("me", parent=ss["Normal"], fontName="Helvetica",
                            fontSize=10, textColor=MUTED, leading=13,
                            alignment=TA_CENTER),
        syll=ParagraphStyle("sy", parent=ss["Normal"], fontName="Helvetica",
                            fontSize=9.5, textColor=DARK, leading=13),
        sec=ParagraphStyle("se", parent=ss["Normal"],
                           fontName="Helvetica-Bold", fontSize=11.5,
                           textColor=IL_NAVY, spaceBefore=8, spaceAfter=5,
                           leading=14),
        q=ParagraphStyle("q", parent=ss["Normal"], fontName="Helvetica-Bold",
                        fontSize=10.5, textColor=DARK, leading=14,
                        spaceBefore=6, spaceAfter=3),
        opt=ParagraphStyle("o", parent=ss["Normal"], fontName="Helvetica",
                          fontSize=10, textColor=DARK, leading=14,
                          alignment=TA_LEFT),
        key=ParagraphStyle("k", parent=ss["Normal"], fontName="Helvetica",
                          fontSize=9.5, textColor=DARK, leading=14),
        ans=ParagraphStyle("a", parent=ss["Normal"], fontName="Helvetica",
                          fontSize=9.5, textColor=DARK, leading=13,
                          leftIndent=10),
    )


def _ruled(width, n=2, gap=7):
    """n blank ruled lines for hand-written answers."""
    out = []
    for _ in range(n):
        out.append(Spacer(1, gap))
        out.append(HRFlowable(width=width, thickness=0.5, color=LINE))
    out.append(Spacer(1, 4))
    return out


_AR_KEY = ("Choose: (A) both A and R true and R explains A; (B) both true but "
           "R does not explain A; (C) A true, R false; (D) A false, R true.")


def build_worksheet(out_path, *, school, subject, grade, chapter, kind,
                    max_marks, duration, sections, syllabus="", accent=None,
                    logo_path=None, show_fields=False):
    st = _styles()
    accent = accent or IL_BLUE          # Infinity Learn brand palette
    labels = "ABCD"
    logo = logo_path or LOGO_PATH
    has_logo = bool(logo) and os.path.exists(logo)

    def header_footer(canvas, doc):
        canvas.saveState()
        # brand accent bar
        canvas.setFillColor(accent)
        canvas.rect(0, A4[1] - 6 * mm, A4[0], 6 * mm, stroke=0, fill=1)
        # logo (or reserved placeholder ring) in the top-right corner
        d = 20 * mm
        lx, ly = A4[0] - 15 * mm - d, A4[1] - 9 * mm - d
        if has_logo:
            try:
                canvas.drawImage(logo, lx, ly, d, d, mask="auto",
                                 preserveAspectRatio=True)
            except Exception:
                pass
        else:
            canvas.setStrokeColor(IL_BLUE)
            canvas.setLineWidth(1.1)
            canvas.circle(lx + d / 2, ly + d / 2, d / 2)
            canvas.setFillColor(IL_NAVY)
            canvas.setFont("Helvetica-Bold", 6.5)
            canvas.drawCentredString(lx + d / 2, ly + d / 2 + 1, "Infinity")
            canvas.setFillColor(IL_BLUE)
            canvas.drawCentredString(lx + d / 2, ly + d / 2 - 6, "Learn")
        # footer
        canvas.setFont("Helvetica", 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(16 * mm, 11 * mm, f"{school}  •  {chapter}")
        canvas.drawRightString(A4[0] - 16 * mm, 11 * mm, f"Page {doc.page}")
        canvas.restoreState()

    doc = BaseDocTemplate(
        out_path, pagesize=A4, leftMargin=16 * mm, rightMargin=16 * mm,
        topMargin=18 * mm, bottomMargin=16 * mm,
        title=f"{chapter} {kind} Worksheet", author=school)
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height,
                  id="f")
    doc.addPageTemplates([PageTemplate(id="p", frames=[frame],
                                       onPage=header_footer)])

    story = []
    st["eyebrow"].textColor = accent
    story.append(Paragraph(f"{kind.upper()} WORKSHEET", st["eyebrow"]))
    story.append(Paragraph(chapter, st["title"]))
    story.append(Paragraph(
        f"{subject} &nbsp;·&nbsp; {grade} &nbsp;·&nbsp; Max Marks: "
        f"{max_marks} &nbsp;·&nbsp; Time: {duration}", st["meta"]))
    if show_fields:
        story.append(Paragraph(
            "Name: ____________________________  Roll No: __________  "
            "Date: ____________", st["meta"]))
    story.append(Spacer(1, 4))
    story.append(HRFlowable(width="100%", thickness=1.0, color=accent,
                            spaceBefore=2, spaceAfter=5))
    if syllabus:
        story.append(Paragraph(f"<b>Topics covered:</b> {syllabus}",
                               st["syll"]))
        story.append(Spacer(1, 4))

    key_blocks = []          # (section title, [answer paragraphs])
    sec_letter = ord("A")

    for sec in sections:
        title = sec.get("title") or _default_title(sec["type"])
        marks = sec.get("marks_line", "")
        head = f"Section {chr(sec_letter)} — {title}"
        if marks:
            head += f"  ({marks})"
        story.append(Paragraph(head, st["sec"]))
        if sec.get("instructions"):
            story.append(Paragraph(sec["instructions"], st["meta"]))
        sec_letter += 1

        t = sec["type"]
        keyparas = []
        if t == "mcq":
            for i, it in enumerate(sec["items"], 1):
                flow = [Paragraph(f"{i}. {_pdf_rich(it['q'])}", st["q"])]
                opts = [Paragraph(f"<b>{labels[j]}.</b>&nbsp; "
                                  f"{_pdf_rich(o)}", st["opt"])
                        for j, o in enumerate(it["options"])]
                while len(opts) < 4:
                    opts.append(Paragraph("", st["opt"]))
                tbl = Table([[opts[0], opts[1]], [opts[2], opts[3]]],
                            colWidths=[doc.width / 2 - 2] * 2)
                tbl.setStyle(_grid())
                flow.append(tbl)
                story.append(KeepTogether(flow))
                keyparas.append(Paragraph(
                    f"<b>{i}.</b> {labels[it['correct']]}", st["key"]))
        elif t == "fill":
            for i, it in enumerate(sec["items"], 1):
                story.append(Paragraph(f"{i}. {_pdf_rich(it['q'])}", st["q"]))
                keyparas.append(Paragraph(
                    f"<b>{i}.</b> {_pdf_rich(it['answer'])}", st["key"]))
        elif t == "tf":
            for i, it in enumerate(sec["items"], 1):
                story.append(Paragraph(
                    f"{i}. {_pdf_rich(it['q'])} &nbsp;&nbsp;( True / False )",
                    st["q"]))
                keyparas.append(Paragraph(
                    f"<b>{i}.</b> {'True' if it['answer'] else 'False'}",
                    st["key"]))
        elif t == "match":
            rows = [[Paragraph("<b>Column A</b>", st["opt"]),
                     Paragraph("<b>Column B</b>", st["opt"])]]
            n = max(len(sec["colA"]), len(sec["colB"]))
            for r in range(n):
                a = f"{r + 1}. {sec['colA'][r]}" if r < len(sec["colA"]) else ""
                b = (f"{labels[r].lower()}) {sec['colB'][r]}"
                     if r < len(sec["colB"]) else "")
                rows.append([Paragraph(_pdf_rich(a), st["opt"]),
                             Paragraph(_pdf_rich(b), st["opt"])])
            mt = Table(rows, colWidths=[doc.width / 2 - 2] * 2)
            mt.setStyle(_grid(box=True))
            story.append(mt)
            key = ", ".join(f"{ia + 1}-{labels[ib].lower()}"
                            for ia, ib in sec["pairs"])
            keyparas.append(Paragraph(key, st["key"]))
        elif t == "assertion":
            story.append(Paragraph(_AR_KEY, st["meta"]))
            for i, it in enumerate(sec["items"], 1):
                flow = [Paragraph(f"{i}. <b>Assertion (A):</b> "
                                  f"{_pdf_rich(it['a'])}", st["opt"]),
                        Paragraph(f"&nbsp;&nbsp;&nbsp;<b>Reason (R):</b> "
                                  f"{_pdf_rich(it['r'])}", st["opt"])]
                story.append(KeepTogether(flow))
                story.append(Spacer(1, 3))
                keyparas.append(Paragraph(f"<b>{i}.</b> {it['answer']}",
                                          st["key"]))
        elif t in ("short", "long"):
            for i, it in enumerate(sec["items"], 1):
                m = it.get("marks", 2 if t == "short" else 5)
                story.append(Paragraph(
                    f"{i}. {_pdf_rich(it['q'])} &nbsp;<b>[{m}]</b>", st["q"]))
                for fl in _ruled(doc.width, n=it.get("lines",
                                 2 if t == "short" else 4)):
                    story.append(fl)
                ans = " ".join(it.get("answer", []))
                keyparas.append(Paragraph(
                    f"<b>{i}.</b> {_pdf_rich(ans)}", st["ans"]))
        else:
            raise ValueError(f"unknown section type: {t}")
        key_blocks.append((title, keyparas))

    # ---- answer key (appended) ----
    story.append(Spacer(1, 8))
    story.append(HRFlowable(width="100%", thickness=0.8, color=MUTED,
                            spaceBefore=4, spaceAfter=4))
    st2 = ParagraphStyle("keyhead", fontName="Helvetica-Bold", fontSize=13,
                         textColor=accent, spaceAfter=6)
    story.append(Paragraph("Answer Key", st2))
    for title, paras in key_blocks:
        if not paras:
            continue
        story.append(Paragraph(f"<b>{title}</b>",
                               ParagraphStyle("kt", fontName="Helvetica-Bold",
                                              fontSize=9.5, textColor=DARK,
                                              spaceBefore=5, spaceAfter=2)))
        # objective keys: pack several per row; subjective: one per line
        if len(paras) > 6 and all(len(p.text) < 30 for p in paras):
            cells, row = [], []
            for idx, p in enumerate(paras, 1):
                row.append(p)
                if idx % 5 == 0:
                    cells.append(row)
                    row = []
            if row:
                while len(row) < 5:
                    row.append(Paragraph("", st["key"]))
                cells.append(row)
            kt = Table(cells, colWidths=[doc.width / 5] * 5)
            kt.setStyle(TableStyle([("TOPPADDING", (0, 0), (-1, -1), 1),
                                    ("BOTTOMPADDING", (0, 0), (-1, -1), 1)]))
            story.append(kt)
        else:
            for p in paras:
                story.append(p)

    doc.build(story)
    return out_path


def _grid(box=False):
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 6),
             ("RIGHTPADDING", (0, 0), (-1, -1), 6),
             ("TOPPADDING", (0, 0), (-1, -1), 2),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 2)]
    if box:
        style.append(("BOX", (0, 0), (-1, -1), 0.5, LINE))
        style.append(("INNERGRID", (0, 0), (-1, -1), 0.4, LINE))
    return TableStyle(style)


def _default_title(t):
    return {
        "mcq": "Multiple Choice Questions",
        "fill": "Fill in the Blanks",
        "tf": "True or False",
        "match": "Match the Columns",
        "assertion": "Assertion–Reason",
        "short": "Short Answer Questions",
        "long": "Long Answer Questions",
    }.get(t, "Questions")


# --- validation + QA helpers ------------------------------------------------
def validate_sections(sections):
    issues = []
    for si, sec in enumerate(sections):
        t = sec["type"]
        if t == "mcq":
            for i, it in enumerate(sec["items"], 1):
                if len(it["options"]) != 4:
                    issues.append(f"sec{si} mcq{i}: !=4 options")
                if not (0 <= it["correct"] <= 3):
                    issues.append(f"sec{si} mcq{i}: bad correct")
                if len(set(o.strip().lower() for o in it["options"])) != 4:
                    issues.append(f"sec{si} mcq{i}: dup options")
        elif t == "match":
            if len(sec["colA"]) != len(sec["colB"]):
                issues.append(f"sec{si} match: column length mismatch")
    return issues


def qa_pdf(path):
    """Return list of (page, text) that overflow the frame width — quick check
    for runaway lines. Uses PyMuPDF text extraction bounds."""
    import fitz
    warns = []
    d = fitz.open(path)
    for pno, page in enumerate(d, 1):
        w = page.rect.width
        for b in page.get_text("blocks"):
            x0, y0, x1, y1 = b[:4]
            if x1 > w - 10:
                warns.append((pno, b[4][:40]))
    return warns
