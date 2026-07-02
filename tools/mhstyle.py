"""
mhstyle - a more visual, teaching-friendly restyle of the content layouts,
applied only to the Maharashtra decks (leaves engine.py and the ICSE decks
untouched). Call mhstyle.apply() once after importing Builder.

Design goals (for slides shown on a classroom screen):
  * fewer words competing for attention - keyword HEAD in the accent colour on
    its own line, the detail smaller and muted underneath;
  * bigger type and generous vertical rhythm so nothing reads as a paragraph;
  * a coloured accent tab on every point instead of a plain dot;
  * the full explanation still lives in the speaker notes.

Everything is drawn with the Builder's own primitives so the chrome, colours
and quiz/title slides stay identical to the rest of the deck.
"""
from engine import C, ACCENTS
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR


def _bullets(self, badge, title, items, notes="", panel_title=None):
    """Full-width points card. (head, sub) items render as a bold accent
    heading with a muted detail line; plain strings render large and clean."""
    s = self._slide(C["bg_light"])
    n = self._next()
    self._chrome(s, badge, title, self.accent, n)
    top, card_h = 2.05, 4.5
    self._box(s, 0.7, top, 11.9, card_h, fill=C["card"], shadow=True,
              shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.03)
    y = top + 0.4
    if panel_title:
        self._text(s, 1.15, y, 11.0, 0.5,
                   [[{"t": panel_title, "size": 19, "bold": True,
                      "color": self.accent}]])
        y += 0.72
    inner_h = (top + card_h) - y - 0.25
    norm = [it if isinstance(it, tuple) else (it, None) for it in items]
    row_h = inner_h / max(1, len(norm))
    for i, (head, sub) in enumerate(norm):
        ry = y + i * row_h
        ac = ACCENTS[i % len(ACCENTS)]
        # rounded accent tab
        self._box(s, 1.15, ry + row_h * 0.16, 0.11, row_h * 0.62, fill=ac,
                  shape=MSO_SHAPE.ROUNDED_RECTANGLE, radius=0.5)
        if sub:
            self._text(s, 1.5, ry, 10.7, row_h,
                       [[{"t": head, "size": 17, "bold": True,
                          "color": C["text"]}],
                        [{"t": sub, "size": 13.5, "color": C["muted"]}]],
                       anchor=MSO_ANCHOR.MIDDLE, space=3, line_spacing=1.02)
        else:
            self._text(s, 1.5, ry, 10.7, row_h,
                       [[{"t": head, "size": 17, "color": C["text"]}]],
                       anchor=MSO_ANCHOR.MIDDLE, line_spacing=1.05)
    self._notes(s, notes or f"Teach '{title}'.")
    return s


def _text_image(self, badge, title, bullets, img, img_side="left",
                caption=None, panel_title=None, notes="", img_w=5.2,
                img_h=4.0):
    """Two-column text + image, restyled: larger bullets, more air, and a
    short accent lead-word on each point where the text allows."""
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
    y = 2.35
    if panel_title:
        self._text(s, px + 0.4, 2.3, 5.5, 0.5,
                   [[{"t": panel_title, "size": 18, "bold": True,
                      "color": self.accent}]])
        y = 2.95
    # Pack the points as one flowing text block (auto-fits far better than
    # fixed rows). Font eases down a little if the copy is long, but the copy
    # itself should be kept to short phrases.
    total = sum(len(b) for b in bullets)
    size = 15 if total <= 210 else (14 if total <= 280 else 13)
    paras = []
    for b in bullets:
        paras.append([{"t": "•  ", "size": size, "bold": True,
                       "color": self.accent},
                      {"t": b, "size": size, "color": C["text"]}])
    self._text(s, px + 0.4, y, 5.5, 6.35 - y, paras, space=9,
               line_spacing=1.06)
    self._notes(s, notes or f"Teach '{title}'.")
    return s


def apply():
    """Monkeypatch the Builder content layouts with the more visual versions.
    Safe to call more than once."""
    from engine import Builder
    if getattr(Builder, "_mh_styled", False):
        return
    Builder.bullets = _bullets
    Builder.text_image = _text_image
    Builder._mh_styled = True
