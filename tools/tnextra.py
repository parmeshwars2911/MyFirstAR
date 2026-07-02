"""
tnextra - extra slide layouts for the Tamil Nadu (Samacheer Kalvi) decks.

Adds a compact homework-MCQ slide (up to 5 questions per slide, answer key in
the speaker notes) on top of the Builder, using the Builder's own primitives so
the chrome/colours match the rest of the deck. Import and call after mhstyle so
the teaching restyle is also in effect.
"""
from engine import C, ACCENTS
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import MSO_ANCHOR


def _hw_mcq_slide(self, badge, title, items, notes_extra=""):
    """One homework slide with up to 5 MCQs, laid out compactly.
    items: list of dicts {q, opts:[a,b,c,d], ans:'A'}. The answer key goes in
    the speaker notes so pupils attempt the questions first."""
    s = self._slide(C["bg_light"])
    self._chrome(s, badge, title, self.accent, self._next())
    top, card_h = 1.75, 5.45
    self._box(s, 0.6, top, 12.1, card_h, fill=C["card"], shadow=True,
              shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.02)
    n = max(1, len(items))
    row_h = (card_h - 0.3) / n
    y0 = top + 0.15
    letters = ["A", "B", "C", "D"]
    keyparts = []
    for i, it in enumerate(items):
        ry = y0 + i * row_h
        qno = it.get("no", i + 1)
        ac = ACCENTS[i % len(ACCENTS)]
        # number chip
        self._box(s, 0.85, ry + 0.05, 0.34, 0.34, fill=ac,
                  shape=MSO_SHAPE.OVAL)
        self._text(s, 0.85, ry + 0.05, 0.34, 0.34,
                   [[{"t": str(qno), "size": 13, "bold": True,
                      "color": "FFFFFF"}]],
                   align=2, anchor=MSO_ANCHOR.MIDDLE)  # 2 = CENTER
        # question text
        self._text(s, 1.35, ry, 11.1, 0.42,
                   [[{"t": it["q"], "size": 14.5, "bold": True,
                      "color": C["text"]}]], anchor=MSO_ANCHOR.MIDDLE)
        # options on one line (two columns of two)
        opts = it["opts"]
        line = "   ".join(f"({letters[j]}) {opts[j]}" for j in range(len(opts)))
        self._text(s, 1.35, ry + 0.44, 11.1, row_h - 0.5,
                   [[{"t": line, "size": 12.5, "color": C["muted"]}]],
                   anchor=MSO_ANCHOR.TOP, line_spacing=1.0)
        keyparts.append(f"Q{qno}: {it['ans']}")
    self._notes(s, ("Homework MCQs — let pupils attempt first. Answer key: "
                    + ";  ".join(keyparts) + ". " + notes_extra).strip())
    return s


def homework(self, items, badge="HOMEWORK", title="Homework — Quick MCQs",
             per_slide=5):
    """Render `items` (list of {q,opts,ans}) across compact MCQ slides,
    up to `per_slide` questions each. Numbers run continuously 1..N."""
    for k, it in enumerate(items):
        it.setdefault("no", k + 1)
    for start in range(0, len(items), per_slide):
        chunk = items[start:start + per_slide]
        part = f"{title}"
        if len(items) > per_slide:
            part = f"{title}  ({start + 1}–{start + len(chunk)} of {len(items)})"
        _hw_mcq_slide(self, badge, part, chunk)


def apply():
    from engine import Builder
    if getattr(Builder, "_tn_extra", False):
        return
    Builder.hw_mcq_slide = _hw_mcq_slide
    Builder.homework = homework
    Builder._tn_extra = True
