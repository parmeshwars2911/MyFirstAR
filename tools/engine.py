"""
ICSE Physics teaching-deck engine.

Builds 16:9 PowerPoint decks that match the reference template
(Gases & the Gas Laws), with a consistent visual system, quiz Q/A pairs,
worked examples, teaching notes (speaker notes), and built-in QA for overlaps.

Images are never drawn directly on slides: diagrams are produced as SVG,
rasterised to PNG via cairosvg (see diagrams.py), and inserted as pictures.
"""
from pptx import Presentation
from pptx.util import Inches, Pt, Emu
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.enum.shapes import MSO_SHAPE
from pptx.oxml.ns import qn
import copy

# ----------------------------------------------------------------------------
# Design tokens (extracted from the reference deck)
# ----------------------------------------------------------------------------
EMU_IN = 914400
SLIDE_W = 13.333
SLIDE_H = 7.5

C = dict(
    bg_dark="1D2433",
    bg_light="F4F6F8",
    teal="0A9396",
    orange="F4801A",
    purple="6A4C93",
    red="E63946",
    green="2A9D8F",
    blue="2563EB",
    text="1D2433",
    muted="6B7280",
    card="FFFFFF",
    option="EAF1F4",
    answer_bg="E9F5F0",
    gold="FFC300",
    subtitle="CADCFC",
    footer_dark="8FA3C4",
)
ACCENTS = [C["teal"], C["orange"], C["purple"], C["red"], C["blue"], C["green"]]

TITLE_FONT = "Calibri"
LABEL_FONT = "Arial"


def rgb(h):
    return RGBColor.from_string(h)


class Deck:
    def __init__(self, footer, accent=None):
        self.prs = Presentation()
        self.prs.slide_width = Inches(SLIDE_W)
        self.prs.slide_height = Inches(SLIDE_H)
        self.blank = self.prs.slide_layouts[6]
        self.footer = footer
        self.accent = accent or C["teal"]
        self.qa_issues = []
        self.deco = set()  # shape ids of decorative elements QA should ignore

    # -- low level helpers ---------------------------------------------------
    def _slide(self, bg):
        s = self.prs.slides.add_slide(self.blank)
        el = s._element
        # remove any placeholders
        cSld = el.find(qn("p:cSld"))
        bgEl = cSld.makeelement(qn("p:bg"), {})
        bgPr = bgEl.makeelement(qn("p:bgPr"), {})
        fill = bgPr.makeelement(qn("a:solidFill"), {})
        clr = fill.makeelement(qn("a:srgbClr"), {"val": bg})
        fill.append(clr)
        bgPr.append(fill)
        # effectLst required after fill
        bgPr.append(bgPr.makeelement(qn("a:effectLst"), {}))
        bgEl.append(bgPr)
        cSld.insert(0, bgEl)
        return s

    def _box(self, s, x, y, w, h, fill=None, line=None, line_w=1.0,
             shape=MSO_SHAPE.RECTANGLE, shadow=False, radius=None, deco=False):
        sp = s.shapes.add_shape(shape, Inches(x), Inches(y), Inches(w), Inches(h))
        if deco:
            self.deco.add(sp.shape_id)
        if fill is None:
            sp.fill.background()
        else:
            sp.fill.solid()
            sp.fill.fore_color.rgb = rgb(fill)
        if line is None:
            sp.line.fill.background()
        else:
            sp.line.color.rgb = rgb(line)
            sp.line.width = Pt(line_w)
        sp.shadow.inherit = False
        if shape == MSO_SHAPE.ROUNDED_RECTANGLE and radius is not None:
            try:
                sp.adjustments[0] = radius
            except Exception:
                pass
        if shadow:
            self._add_shadow(sp)
        return sp

    def _add_shadow(self, sp):
        spPr = sp._element.spPr
        # remove existing effectLst
        for e in spPr.findall(qn("a:effectLst")):
            spPr.remove(e)
        eff = spPr.makeelement(qn("a:effectLst"), {})
        sh = spPr.makeelement(qn("a:outerShdw"), {
            "blurRad": "88900", "dist": "38100", "dir": "5400000",
            "rotWithShape": "0", "algn": "bl"})
        clr = spPr.makeelement(qn("a:srgbClr"), {"val": "000000"})
        a = spPr.makeelement(qn("a:alpha"), {"val": "16000"})
        clr.append(a)
        sh.append(clr)
        eff.append(sh)
        spPr.append(eff)

    def _text(self, s, x, y, w, h, runs, align=PP_ALIGN.LEFT,
              anchor=MSO_ANCHOR.TOP, wrap=True, space=None, line_spacing=None,
              deco=False):
        """runs: list of paragraphs; each paragraph is a list of run-dicts
        {t, size, bold, color, font, italic}. A plain string => one run."""
        tb = s.shapes.add_textbox(Inches(x), Inches(y), Inches(w), Inches(h))
        if deco:
            self.deco.add(tb.shape_id)
        tf = tb.text_frame
        tf.word_wrap = wrap
        tf.vertical_anchor = anchor
        tf.margin_left = 0
        tf.margin_right = 0
        tf.margin_top = 0
        tf.margin_bottom = 0
        if isinstance(runs, str):
            runs = [[{"t": runs}]]
        for i, para in enumerate(runs):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.alignment = align
            if space is not None:
                p.space_after = Pt(space)
            if line_spacing is not None:
                p.line_spacing = line_spacing
            if isinstance(para, str):
                para = [{"t": para}]
            for rd in para:
                r = p.add_run()
                r.text = rd.get("t", "")
                f = r.font
                f.size = Pt(rd.get("size", 15))
                f.bold = rd.get("bold", False)
                f.italic = rd.get("italic", False)
                f.name = rd.get("font", TITLE_FONT)
                f.color.rgb = rgb(rd.get("color", C["text"]))
        return tb

    def _pic(self, s, path, x, y, w, h):
        return s.shapes.add_picture(path, Inches(x), Inches(y), Inches(w), Inches(h))

    def _notes(self, s, text):
        s.notes_slide.notes_text_frame.text = text

    def _logo_space(self, s):
        """Reserve a clean circular area, top-right, for the brand logo."""
        self._box(s, 11.95, 0.4, 0.95, 0.95, fill=None, line="DDE2E8",
                  line_w=1.25, shape=MSO_SHAPE.OVAL, deco=True)

    def _chrome(self, s, badge, title, accent, n):
        """Top badge + title + reserved logo space (no footer)."""
        self._logo_space(s)
        self._box(s, 0.6, 0.55, 0.28, 0.28, fill=accent)
        self._text(s, 1.0, 0.5, 10.4, 0.35,
                   [[{"t": badge.upper(), "size": 13, "bold": True,
                      "color": accent, "font": LABEL_FONT}]])
        self._text(s, 0.6, 0.85, 10.9, 0.9,
                   [[{"t": title, "size": 30, "bold": True,
                      "color": C["text"], "font": TITLE_FONT}]])

    # -- QA: record bounding boxes for overlap detection ---------------------
    def qa(self):
        """Inspect every slide for overlapping text boxes & off-slide shapes."""
        issues = []
        for idx, s in enumerate(self.prs.slides, 1):
            boxes = []
            for sh in s.shapes:
                if sh.shape_id in self.deco:
                    continue
                has_text = sh.has_text_frame and sh.text_frame.text.strip()
                L = (sh.left or 0) / EMU_IN
                T = (sh.top or 0) / EMU_IN
                W = (sh.width or 0) / EMU_IN
                H = (sh.height or 0) / EMU_IN
                R, B = L + W, T + H
                if L < -0.05 or T < -0.05 or R > SLIDE_W + 0.05 or B > SLIDE_H + 0.05:
                    # only real (text-bearing) content matters here
                    if has_text:
                        issues.append(f"slide {idx}: '{_short(sh)}' off-slide "
                                      f"(L{L:.2f} T{T:.2f} R{R:.2f} B{B:.2f})")
                if has_text:
                    boxes.append((L, T, R, B, _short(sh)))
            # text-vs-text overlap (ignore tiny labels inside badges)
            for i in range(len(boxes)):
                for j in range(i + 1, len(boxes)):
                    a, b = boxes[i], boxes[j]
                    ox = max(0, min(a[2], b[2]) - max(a[0], b[0]))
                    oy = max(0, min(a[3], b[3]) - max(a[1], b[1]))
                    area = ox * oy
                    amin = min((a[2]-a[0])*(a[3]-a[1]), (b[2]-b[0])*(b[3]-b[1]))
                    if area > 0.25 * amin and area > 0.12:
                        issues.append(
                            f"slide {idx}: text overlap '{a[4]}' x '{b[4]}' "
                            f"({area:.2f} in²)")
        self.qa_issues = issues
        return issues

    def save(self, path):
        self.prs.save(path)


def _short(sh):
    if sh.has_text_frame:
        return sh.text_frame.text.strip().replace("\n", " ")[:28]
    return sh.name


# ----------------------------------------------------------------------------
# High-level slide layouts
# ----------------------------------------------------------------------------
class Builder(Deck):
    def __init__(self, footer, accent=None, brand="Infinity Learn  |  Physics"):
        super().__init__(footer, accent)
        self.brand = brand
        self.n = 0

    def _next(self):
        self.n += 1
        return self.n

    def asset(self, key, fallback):
        """Return a real photo/illustration from assets/img/<key> if one has
        been generated/downloaded and QA-passed, else the SVG diagram path."""
        try:
            from images import find_asset
            return find_asset(key) or fallback
        except Exception:
            return fallback

    # 1. Title -------------------------------------------------------------
    def title(self, eyebrow, title, subtitle, img=None):
        s = self._slide(C["bg_dark"])
        self._box(s, -1.6, 3.4, 5.2, 5.2, fill=self.accent, shape=MSO_SHAPE.OVAL, deco=True)
        self._box(s, 11.0, -1.8, 4.6, 4.6, fill=C["orange"], shape=MSO_SHAPE.OVAL, deco=True)
        self._text(s, 0.8, 1.6, 9.5, 0.5,
                   [[{"t": eyebrow.upper(), "size": 16, "bold": True,
                      "color": C["gold"], "font": LABEL_FONT}]])
        tw = 8.8 if img else 11.5
        tsize = 50 if len(title) <= 22 else (42 if len(title) <= 32 else 36)
        self._text(s, 0.8, 2.0, tw, 1.9,
                   [[{"t": title, "size": tsize, "bold": True,
                      "color": "FFFFFF"}]], anchor=MSO_ANCHOR.BOTTOM)
        self._text(s, 0.8, 4.05, 8.8 if img else 11.0, 1.6,
                   [[{"t": subtitle, "size": 19, "color": C["subtitle"]}]])
        if img:
            self._pic(s, img, 9.9, 2.3, 2.9, 3.0)
        self._next()
        return s

    # 2. Learning objectives ----------------------------------------------
    def objectives(self, items, badge="INTRODUCTION", title="Learning Objectives"):
        s = self._slide(C["bg_light"])
        n = self._next()
        self._chrome(s, badge, title, self.accent, n)
        cols = 2
        cw, ch = 5.85, 1.15
        x0, y0, gx, gy = 0.7, 2.05, 0.2, 0.28
        for i, it in enumerate(items):
            r, c = divmod(i, cols)
            x = x0 + c * (cw + gx)
            y = y0 + r * (ch + gy)
            ac = ACCENTS[i % len(ACCENTS)]
            self._box(s, x, y, cw, ch, fill=C["card"], shadow=True,
                      shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
            self._box(s, x + 0.3, y + 0.32, 0.5, 0.5, fill=ac,
                      shape=MSO_SHAPE.OVAL)
            self._text(s, x + 0.3, y + 0.32, 0.5, 0.5,
                       [[{"t": str(i + 1), "size": 16, "bold": True,
                          "color": "FFFFFF"}]], align=PP_ALIGN.CENTER,
                       anchor=MSO_ANCHOR.MIDDLE)
            self._text(s, x + 1.0, y + 0.18, cw - 1.2, ch - 0.3,
                       [[{"t": it, "size": 14.5, "color": C["text"]}]],
                       anchor=MSO_ANCHOR.MIDDLE)
        self._notes(s, "Open by previewing these objectives so students know "
                       "what they should be able to do by the end of the session.")
        return s

    # 3. Part divider ------------------------------------------------------
    def divider(self, number, eyebrow, title, subtitle):
        s = self._slide(C["bg_dark"])
        n = self._next()
        self._box(s, 9.4, -1.6, 5.4, 5.4, fill=self.accent, shape=MSO_SHAPE.OVAL,
                  deco=True)
        # faint watermark number, lower-right, behind nothing
        self._text(s, 9.3, 3.4, 3.7, 3.0,
                   [[{"t": str(number), "size": 200, "bold": True,
                      "color": "263149"}]], align=PP_ALIGN.RIGHT, deco=True)
        self._text(s, 0.85, 2.35, 7.6, 0.5,
                   [[{"t": eyebrow.upper(), "size": 16, "bold": True,
                      "color": C["gold"], "font": LABEL_FONT}]])
        self._text(s, 0.85, 2.95, 8.2, 1.2,
                   [[{"t": title, "size": 42, "bold": True, "color": "FFFFFF"}]])
        self._text(s, 0.85, 4.5, 8.0, 0.9,
                   [[{"t": subtitle, "size": 18, "color": C["subtitle"]}]])
        return s

    # 4. Feature cards (2 or 4) -------------------------------------------
    def cards(self, badge, title, items, notes=""):
        """items: list of (heading, body). 2 per row."""
        s = self._slide(C["bg_light"])
        n = self._next()
        self._chrome(s, badge, title, self.accent, n)
        cw, chh = 5.7, 1.75
        x0, y0, gx, gy = 0.7, 2.1, 0.4, 0.25
        rows = (len(items) + 1) // 2
        if rows == 1:
            chh = 2.0
        for i, (head, body) in enumerate(items):
            r, c = divmod(i, 2)
            x = x0 + c * (cw + gx)
            y = y0 + r * (chh + gy)
            ac = ACCENTS[i % len(ACCENTS)]
            self._box(s, x, y, cw, chh, fill=C["card"], shadow=True,
                      shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
            self._box(s, x + 0.35, y + 0.32, 0.55, 0.55, fill=ac,
                      shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.3)
            self._text(s, x + 1.1, y + 0.28, cw - 1.4, 0.5,
                       [[{"t": head, "size": 17, "bold": True,
                          "color": C["text"]}]])
            self._text(s, x + 1.1, y + 0.82, cw - 1.4, chh - 1.0,
                       [[{"t": body, "size": 13.5, "color": C["muted"]}]])
        self._notes(s, notes or _auto_notes(title, items))
        return s

    # 5. Text + image two-column ------------------------------------------
    def text_image(self, badge, title, bullets, img, img_side="left",
                   caption=None, panel_title=None, notes="", img_w=5.2,
                   img_h=4.0):
        s = self._slide(C["bg_light"])
        n = self._next()
        self._chrome(s, badge, title, self.accent, n)
        img_x = 0.9 if img_side == "left" else 13.333 - 0.9 - img_w
        img_y = 2.0 + (4.3 - img_h) / 2
        if img:
            self._pic(s, img, img_x, img_y, img_w, img_h)
        if caption:
            self._text(s, img_x, img_y + img_h + 0.06, img_w, 0.3,
                       [[{"t": caption, "size": 11, "italic": True,
                          "color": C["muted"]}]], align=PP_ALIGN.CENTER)
        px = 13.333 - 0.9 - 6.2 if img_side == "left" else 0.9
        self._box(s, px, 2.0, 6.2, 4.3, fill=C["card"], shadow=True,
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)
        if panel_title:
            self._text(s, px + 0.35, 2.25, 5.5, 0.45,
                       [[{"t": panel_title, "size": 18, "bold": True,
                          "color": self.accent}]])
            by = 2.85
        else:
            by = 2.35
        paras = []
        for b in bullets:
            paras.append([{"t": "•  ", "size": 15, "bold": True,
                           "color": self.accent},
                          {"t": b, "size": 15, "color": C["text"]}])
        self._text(s, px + 0.35, by, 5.55, 6.2 - by, paras, space=9,
                   line_spacing=1.05)
        self._notes(s, notes or _auto_notes(title, [(b, "") for b in bullets]))
        return s

    # 6. Bullets full width ------------------------------------------------
    def bullets(self, badge, title, bullets, notes="", panel_title=None):
        s = self._slide(C["bg_light"])
        n = self._next()
        self._chrome(s, badge, title, self.accent, n)
        self._box(s, 0.7, 2.0, 11.9, 4.5, fill=C["card"], shadow=True,
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.03)
        y = 2.3
        if panel_title:
            self._text(s, 1.1, 2.3, 11.0, 0.45,
                       [[{"t": panel_title, "size": 18, "bold": True,
                          "color": self.accent}]])
            y = 2.95
        paras = []
        for b in bullets:
            if isinstance(b, tuple):
                head, sub = b
                paras.append([{"t": "•  ", "size": 16, "bold": True,
                               "color": self.accent},
                              {"t": head + "  ", "size": 16, "bold": True,
                               "color": C["text"]},
                              {"t": sub, "size": 15, "color": C["muted"]}])
            else:
                paras.append([{"t": "•  ", "size": 16, "bold": True,
                               "color": self.accent},
                              {"t": b, "size": 16, "color": C["text"]}])
        self._text(s, 1.1, y, 11.0, 6.3 - y, paras, space=11, line_spacing=1.05)
        self._notes(s, notes or _auto_notes(title, []))
        return s

    # 7. Statement + formula ----------------------------------------------
    def statement(self, badge, title, statement, formula=None, points=None,
                  img=None, notes=""):
        s = self._slide(C["bg_light"])
        n = self._next()
        self._chrome(s, badge, title, self.accent, n)
        self._box(s, 0.7, 2.0, 11.9, 1.5, fill=self.accent,
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
        self._text(s, 1.1, 2.0, 11.1, 1.5,
                   [[{"t": statement, "size": 19, "bold": True,
                      "color": "FFFFFF"}]], anchor=MSO_ANCHOR.MIDDLE)
        y = 3.75
        if formula:
            self._box(s, 0.7, y, 11.9, 1.0, fill="FFF6E9",
                      shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.08)
            self._text(s, 1.1, y, 11.1, 1.0,
                       [[{"t": formula, "size": 24, "bold": True,
                          "color": C["orange"]}]], align=PP_ALIGN.CENTER,
                       anchor=MSO_ANCHOR.MIDDLE)
            y += 1.2
        if img:
            self._pic(s, img, 4.4, y, 4.5, 6.4 - y if 6.4 - y > 1 else 1.6)
        elif points:
            paras = []
            for p in points:
                paras.append([{"t": "•  ", "size": 15, "bold": True,
                               "color": self.accent},
                              {"t": p, "size": 15, "color": C["text"]}])
            self._text(s, 1.1, y + 0.05, 11.0, 6.4 - y, paras, space=9)
        self._notes(s, notes or _auto_notes(title, []))
        return s

    # 8. Worked example ----------------------------------------------------
    def worked(self, badge, title, problem, steps, answer, notes=""):
        s = self._slide(C["bg_light"])
        n = self._next()
        self._chrome(s, badge, title, self.accent, n)
        self._box(s, 0.7, 2.0, 11.9, 1.2, fill="EEF2F7",
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.06)
        self._text(s, 1.1, 2.0, 11.1, 1.2,
                   [[{"t": "Problem.  ", "size": 16, "bold": True,
                      "color": self.accent},
                     {"t": problem, "size": 16, "color": C["text"]}]],
                   anchor=MSO_ANCHOR.MIDDLE)
        self._box(s, 0.7, 3.4, 11.9, 2.9, fill=C["card"], shadow=True,
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.03)
        paras = []
        for st in steps:
            paras.append([{"t": st, "size": 16, "color": C["text"]}])
        self._text(s, 1.1, 3.65, 11.1, 2.0, paras, space=7, line_spacing=1.05)
        self._box(s, 0.7, 5.55, 11.9, 0.65, fill=C["answer_bg"],
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
        self._text(s, 1.1, 5.55, 11.1, 0.65,
                   [[{"t": "Answer:  ", "size": 16, "bold": True,
                      "color": C["green"]},
                     {"t": answer, "size": 16, "bold": True,
                      "color": C["text"]}]], anchor=MSO_ANCHOR.MIDDLE)
        self._notes(s, notes or "Work through this on the board step by step; "
                                "pause after the setup and ask students to "
                                "predict the next line.")
        return s

    # 9. Quiz intro --------------------------------------------------------
    def quiz_intro(self, which, title, count):
        s = self._slide(C["bg_dark"])
        n = self._next()
        self._box(s, 9.6, -1.5, 5.2, 5.2, fill=self.accent, shape=MSO_SHAPE.OVAL, deco=True)
        self._text(s, 0.85, 2.2, 9.0, 0.5,
                   [[{"t": which.upper(), "size": 16, "bold": True,
                      "color": C["gold"], "font": LABEL_FONT}]])
        self._text(s, 0.85, 2.8, 10.5, 1.1,
                   [[{"t": title, "size": 44, "bold": True, "color": "FFFFFF"}]])
        self._text(s, 0.85, 4.1, 10.5, 0.6,
                   [[{"t": f"{count} questions  •  think before the answer "
                          f"reveals on the next slide",
                      "size": 18, "color": C["subtitle"]}]])
        return s

    # 10/11. Quiz question + mirrored answer reveal ------------------------
    def _quiz_slide(self, qno, topic, question, options, reveal=None, why=None):
        """Shared composition for the question slide and its mirrored answer
        slide. When `reveal` (0-based index) is given, the correct option is
        highlighted and a 'Why' panel is shown — same layout as the question."""
        s = self._slide(C["bg_light"])
        n = self._next()
        is_ans = reveal is not None
        badge = "ANSWER REVEALED" if is_ans else "QUIZ QUESTION"
        accent = C["green"] if is_ans else self.accent
        self._chrome(s, badge, f"Q{qno} — {topic}", accent, n)
        # question card (identical on both slides)
        self._box(s, 0.7, 1.95, 11.9, 1.45, fill=C["card"], shadow=True,
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.04)
        self._text(s, 1.1, 1.95, 11.1, 1.45,
                   [[{"t": question, "size": 18, "bold": True,
                      "color": C["text"]}]], anchor=MSO_ANCHOR.MIDDLE)
        # options grid (identical positions on both slides)
        labels = "ABCD"
        for i, opt in enumerate(options):
            r, c = divmod(i, 2)
            x = 0.7 + c * (5.85 + 0.2)
            y = 3.65 + r * (0.95 + 0.18)
            correct = is_ans and i == reveal
            if correct:
                fill, oc, txtcol = C["answer_bg"], C["green"], C["text"]
                self._box(s, x, y, 5.85, 0.95, fill=fill, line=C["green"],
                          line_w=2.0, shape=MSO_SHAPE.ROUNDED_RECTANGLE,
                          radius=0.12)
            else:
                dim = is_ans  # fade the wrong options on the answer slide
                fill = C["option"]
                oc = "B7C2CC" if dim else accent
                txtcol = C["muted"] if dim else C["text"]
                self._box(s, x, y, 5.85, 0.95, fill=fill,
                          shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.12)
            self._box(s, x + 0.3, y + 0.25, 0.45, 0.45, fill=oc,
                      shape=MSO_SHAPE.OVAL)
            self._text(s, x + 0.3, y + 0.25, 0.45, 0.45,
                       [[{"t": ("✓" if correct else labels[i]),
                          "size": 14, "bold": True, "color": "FFFFFF"}]],
                       align=PP_ALIGN.CENTER, anchor=MSO_ANCHOR.MIDDLE)
            self._text(s, x + 0.95, y, 4.7, 0.95,
                       [[{"t": opt, "size": 14.5,
                          "bold": bool(correct), "color": txtcol}]],
                       anchor=MSO_ANCHOR.MIDDLE)
        # why panel (answer slide only)
        if is_ans and why:
            self._box(s, 0.7, 5.95, 11.9, 1.2, fill=C["card"], shadow=True,
                      shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.05)
            self._text(s, 1.1, 6.12, 5.0, 0.35,
                       [[{"t": "WHY", "size": 13, "bold": True,
                          "color": C["green"], "font": LABEL_FONT}]])
            self._text(s, 1.1, 6.5, 11.1, 0.6,
                       [[{"t": why, "size": 14.5, "color": C["text"]}]],
                       line_spacing=1.05)
        return s

    def quiz_q(self, qno, topic, question, options):
        self._cur_quiz = dict(qno=qno, topic=topic, question=question,
                              options=options)
        return self._quiz_slide(qno, topic, question, options)

    def quiz_a(self, qno, answer, why):
        """Mirrors the matching question slide and reveals the answer. `answer`
        starts with the option letter (e.g. 'B. ...'); that letter selects
        which option to highlight, reusing the stored question + options."""
        q = getattr(self, "_cur_quiz", None)
        idx = 0
        if answer and answer[0].upper() in "ABCD":
            idx = "ABCD".index(answer[0].upper())
        if not q or q["qno"] != qno:
            # fallback: no stored question (shouldn't happen) — show answer only
            q = dict(qno=qno, topic="Answer", question=answer,
                     options=[answer])
            idx = 0
        return self._quiz_slide(qno, q["topic"], q["question"], q["options"],
                                reveal=idx, why=why)

    # 12. Recap ------------------------------------------------------------
    def recap(self, badge, title, items, notes=""):
        s = self._slide(C["bg_light"])
        n = self._next()
        self._chrome(s, badge, title, self.accent, n)
        paras = []
        for head, sub in items:
            paras.append([{"t": "✓  ", "size": 16, "bold": True,
                           "color": C["green"]},
                          {"t": head + "  —  ", "size": 16, "bold": True,
                           "color": C["text"]},
                          {"t": sub, "size": 15, "color": C["muted"]}])
        self._box(s, 0.7, 2.0, 11.9, 4.5, fill=C["card"], shadow=True,
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.03)
        self._text(s, 1.1, 2.35, 11.0, 4.0, paras, space=12, line_spacing=1.05)
        self._notes(s, notes or "Use this recap to consolidate; cold-call "
                                "students to state each point in their own words.")
        return s

    # 13. Closing ----------------------------------------------------------
    def closing(self, title, message):
        s = self._slide(C["bg_dark"])
        n = self._next()
        self._box(s, -1.6, 3.4, 5.2, 5.2, fill=self.accent, shape=MSO_SHAPE.OVAL, deco=True)
        self._box(s, 11.0, -1.8, 4.6, 4.6, fill=C["orange"], shape=MSO_SHAPE.OVAL, deco=True)
        self._text(s, 0.8, 2.6, 11.5, 1.2,
                   [[{"t": title, "size": 46, "bold": True, "color": "FFFFFF"}]])
        self._text(s, 0.8, 3.9, 11.0, 1.2,
                   [[{"t": message, "size": 19, "color": C["subtitle"]}]])
        return s


def _auto_notes(title, items):
    base = f"Teach '{title}'. "
    if items:
        base += "Walk through each point with an everyday example and check "
        base += "understanding with a quick question before moving on."
    else:
        base += "Explain clearly, link to prior knowledge, and invite one or "
        base += "two student examples."
    return base
