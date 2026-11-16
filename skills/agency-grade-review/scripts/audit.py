#!/usr/bin/env python3
"""Measured gate for the Kraftwrk design skills.

Reads a rendered page (a file or a URL) and reports findings with values, so the
count, contrast, state, flow and worst-case tests in agency-grade-review are
measured and not estimated. It never edits the page it reads.

    python3 scripts/audit.py page.html --root "#home:ios" --root "#site:web" --out report.json

A screen root is a selector, optionally followed by :ios, :android or :web.
Without --root the tool takes every [data-screen] element (platform from its
data-platform attribute), or the whole body as one web surface.

Switches are found in the page itself: every element with
data-set="attribute=value" and an optional data-on="selector" is a switch.
data-theme switches the theme, data-state the state of a screen, data-lang the
language. Every state and language is measured in both themes.

Severity follows agency-grade-review: Blocker, Major, Minor. An Advisory is a
question for the reviewer: answer it with a fix or with the reason it stays.
"""
import argparse, io, json, pathlib, re, sys
from collections import Counter, defaultdict
from playwright.sync_api import sync_playwright

try:
    from PIL import Image
except Exception:  # sampled contrast is skipped without Pillow
    Image = None

HERE = pathlib.Path(__file__).resolve().parent
SRC = (HERE / "measure.js").read_text()
FN = "(args) => {\nconst M = %s;\nreturn M.%s(args);\n}"
SCALE = {11, 12, 14, 16, 18, 20, 22, 24, 28, 32, 36, 45, 57}
IOS = {(34, 41), (28, 34), (22, 28), (20, 25), (17, 22), (16, 21), (15, 20), (13, 18), (12, 16), (11, 13)}
IOS_SIZES = {a for a, _ in IOS}
RADII = {4, 8, 12, 16, 20, 28, 32, 48}
FLOOR = {"ios": 44, "android": 48, "web": 44}
SYSTEM = re.compile(r"^(roboto|sf pro|sf compact|-apple-system|system-ui|blinkmacsystemfont|segoe ui)", re.I)
# Faces generated interfaces reach for first (after Impeccable's detector and new-work lists, November 2026).
SPENT = ["inter", "roboto", "geist", "dm sans", "dm serif", "space grotesk", "space mono", "plus jakarta sans", "fraunces", "playfair display", "newsreader", "instrument sans", "instrument serif", "ibm plex", "outfit", "syne", "lora", "cormorant", "crimson"]
SERIF = ["newsreader", "fraunces", "playfair", "cormorant", "lora", "crimson", "instrument serif", "dm serif", "recoleta", "georgia", "times", "tiempos", "canela"]
BUZZ = re.compile(r"\b(unlock|seamless(ly)?|elevate|supercharge|empower|streamline|world-class|next-generation|cutting-edge|enterprise-grade|game-chang\w+|revolutioni[sz]e|effortless(ly)?|naadloos|moeiteloos|nahtlos)\b", re.I)
LAYOUT = re.compile(r"^(all|width|height|top|left|right|bottom|inset.*|margin.*|padding.*|max-.*|min-.*|flex-basis|flex-grow|grid-template.*|font-size|line-height|letter-spacing|border.*width|gap|row-gap|column-gap)$")
PAINT = re.compile(r"^(filter|backdrop-filter|-webkit-backdrop-filter|clip-path|mask.*|-webkit-mask.*|box-shadow|text-shadow)$")
FREEZE = "*,*::before,*::after{animation:none!important;transition:none!important;scroll-behavior:auto!important}[data-audit-hide],[data-audit-hide] *{color:transparent!important;-webkit-text-fill-color:transparent!important;text-shadow:none!important;text-decoration-color:transparent!important}"
RULES = {
    "colour.contrast": "foundations, Colour: 4.5:1 under 24px, 3:1 from 24px, in both themes and every state",
    "colour.grey-on-colour": "foundations, Colour: secondary text on a coloured ground is a step of that hue, never a neutral grey",
    "type.scale": "typography-craft, Scale: every size on the major second scale, 5 to 7 steps per surface",
    "type.weights": "foundations, Typography: two weights in UI, a third only for display",
    "type.families": "typography-craft, The bar: one workhorse, at most one display face, a mono only for data",
    "type.leading": "typography-craft, Scale: line heights on the 4px grid or the iOS text style's own leading",
    "type.tracking": "typography-craft, Scale: tracking bands for brand faces, platform tracking for system faces",
    "type.measure": "typography-craft, Scale: 45 to 75 characters for reading text, counted in the render",
    "type.minimum": "typography-craft, Rendering: nothing below 11, reading text from 14",
    "type.hierarchy": "typography-craft, Scale: a heading is at least 1.25 times the role below it, or 200 heavier",
    "type.breaks": "typography-craft, Micro-typography: balanced headlines, no one-word last lines",
    "type.micro": "typography-craft, Micro-typography: real quotes, ellipsis and dashes per the copy rules",
    "identity.face": "typography-craft, Choosing typefaces: name the face and its reason; a spent face needs one from the brief",
    "identity.tell": "agency-grade-review, Visual tells: reflexes that read as generated",
    "identity.eyebrow": "product-ui-patterns, Guideline 8: an eyebrow carries a fact the heading does not",
    "space.grid": "foundations, Layout: every spacing value a multiple of 4",
    "space.heading": "foundations, Layout: at least twice as much space above a heading as below it",
    "shape.radius": "foundations, Colour: one radius logic from the Material shape scale",
    "layout.cards": "foundations, Layout: never a card inside a card; never border, shadow and tint together",
    "layout.clipped": "foundations, Components: a truncation rule per element, nothing cut off",
    "target.size": "foundations, Components: 44pt on iOS, 48dp on Android, 44 high on the web (24 is the legal floor)",
    "a11y.name": "foundations, Accessibility: labelled controls, no placeholder as the only label",
    "a11y.headings": "foundations, Accessibility: headings in order",
    "a11y.focus": "foundations, Accessibility: visible focus indicators",
    "a11y.scaling": "foundations, Accessibility: web type in rem, layouts survive 200 percent",
    "motion.property": "foundations, Motion: movement animates transform and opacity; colour may cross-fade; never layout properties",
    "motion.duration": "foundations, Motion: UI motion under 300ms, sheets and full-screen modals up to 400ms",
    "motion.easing": "foundations, Motion: ease-out to enter, never ease-in; overshoot is a brand decision",
    "motion.reduced": "foundations, Accessibility: reduced motion keeps fades and removes movement",
    "motion.rest": "foundations, Motion: content is visible without script or animation",
    "motion.hover": "foundations, Motion: hover only on pointer devices, never moving its own target",
    "web.surfaces": "foundations, Platform conventions (Web): the parts the browser draws take the product's tokens",
    "content.real": "foundations, Content: real content, never lorem ipsum; plain verbs, no generic copy",
    "state.coverage": "foundations, Components: empty, loading and error exist for every container",
}
ORDER = {"Blocker": 0, "Major": 1, "Minor": 2, "Advisory": 3}
FACES = defaultdict(list)
TOLD = set()


def lum(c):
    def f(v):
        v /= 255
        return v / 12.92 if v <= 0.03928 else ((v + 0.055) / 1.055) ** 2.4
    return 0.2126 * f(c[0]) + 0.7152 * f(c[1]) + 0.0722 * f(c[2])


def ratio(a, b):
    x, y = lum(a), lum(b)
    return (max(x, y) + 0.05) / (min(x, y) + 0.05)


def ms(v):
    out = []
    for part in v.split(","):
        part = part.strip()
        out.append(float(part[:-2]) if part.endswith("ms") else float(part[:-1]) * 1000 if part.endswith("s") else 0.0)
    return out or [0.0]


class Report:
    def __init__(self):
        self.items, self.seen, self.tails, self.copies = [], set(), set(), []

    def add(self, sev, rule, where, what):
        key = (rule, where, what)
        if key in self.seen:
            return
        self.seen.add(key)
        # a copy of a screen at another width only reports what differs from the screens before it
        root = next((r for r in self.copies if where == r or where.startswith(r + " ")), None)
        tail = (rule, where[len(root):] if root else where.split(" ", 1)[1] if " " in where else "", what)
        if root and tail in self.tails:
            return
        self.tails.add(tail)
        self.items.append({"severity": sev, "rule": rule, "where": where, "finding": what})


def sample(page, run):
    """Contrast of a text run against the pixels under it: hide the text, read the render."""
    q = '[data-audit-id="%s"]' % run["id"]
    boxes = page.evaluate("""([q, txt]) => { const el = document.querySelector(q); if (!el) return null; el.setAttribute('data-audit-hide', ''); el.scrollIntoView({block: 'center'});
        const node = [...el.childNodes].find(n => n.nodeType === 3 && n.nodeValue.replace(/\\s+/g, ' ').trim() === txt) || el;
        for (let n = el.parentElement; n && n !== document.body; n = n.parentElement) n.style.setProperty('text-decoration-color', 'transparent', 'important');
        const er = el.getBoundingClientRect(), r = document.createRange(); r.selectNodeContents(node);
        // one box per line: a run that wraps shares its second line with its neighbours
        return [...r.getClientRects()].filter(b => b.width >= 1 && b.height >= 1).map(b => ({x: b.left - er.left, y: b.top - er.top, w: b.width, h: b.height})); }""", [q, run["txt"]])
    if not boxes:
        return None
    try:
        png = page.locator(q).first.screenshot(timeout=4000)
    except Exception:
        return None
    finally:
        page.evaluate("q => { const el = document.querySelector(q); if (!el) return; el.removeAttribute('data-audit-hide'); for (let n = el.parentElement; n && n !== document.body; n = n.parentElement) n.style.removeProperty('text-decoration-color'); }", q)
    im = Image.open(io.BytesIO(png)).convert("RGB")
    fg, a = run["col"][:3], run["col"][3]
    vals = []
    for box in boxes:
        x0, y0, x1, y1 = max(0, int(box["x"])), max(0, int(box["y"])), min(im.width, int(box["x"] + box["w"]) + 1), min(im.height, int(box["y"] + box["h"]) + 1)
        if x1 - x0 < 1 or y1 - y0 < 1:
            continue
        crop = im.crop((x0, y0, x1, y1))
        crop.thumbnail((160, 160))
        raw = crop.tobytes()
        vals += [ratio([fg[i] * a + raw[j + i] * (1 - a) for i in range(3)], raw[j:j + 3]) for j in range(0, len(raw), 3)]
    if not vals:
        return None
    vals.sort()
    return vals[int(len(vals) * 0.02)]


def contrast(page, rep, sel, data, theme, variant, cache, known):
    tag = theme + (", " + variant if variant else "")
    fails = defaultdict(list)
    for r in data["runs"]:
        need = 3.0 if r["large"] else 4.5
        got, how = r["ratio"], "computed"
        c, b = r["col"], r["bg"]
        if r["over"] or got < need:
            # over imagery, or failing on paper: read the pixels under the text before deciding
            if Image is None:
                if r["over"]:
                    rep.add("Advisory", "colour.contrast", sel + " " + r["where"], '"%s" sits over imagery and was not sampled (Pillow is not installed)' % r["s"])
                    continue
            else:
                key = (r["id"], theme, variant)
                if key not in cache:
                    cache[key] = sample(page, r) if len(cache) < 800 else None
                if cache[key] is not None:
                    got, how = cache[key], "sampled"
                elif r["over"]:
                    continue
        elif max(c[:3]) - min(c[:3]) <= 12 and 40 < max(c[:3]) and min(c[:3]) < 235 and c[3] >= 0.99 and max(b) - min(b) >= 40:
            if ("grey", r["id"]) not in known:
                known.add(("grey", r["id"]))
                rep.add("Minor", "colour.grey-on-colour", sel + " " + r["where"], '"%s" is neutral grey rgb(%d, %d, %d) on a coloured ground rgb(%d, %d, %d), %s' % (r["s"], c[0], c[1], c[2], b[0], b[1], b[2], tag))
        if got < need:
            mark = (r["id"], round(got, 1))
            if variant and mark in known:
                continue  # already reported for the default state
            if not variant:
                known.add(mark)
            fails[(round(got, 1), "3" if r["large"] else "4.5", how, bool(r.get("dis")))].append(r)
    for (got, need, how, dis), rs in sorted(fails.items()):
        eg = ", ".join('"%s"' % r["s"][:28] for r in rs[:3])
        sizes = "/".join("%g" % x for x in sorted({r["fs"] for r in rs}))
        note = " (marked disabled or busy: may fail, must read as disabled by other means)" if dis else ""
        rep.add("Advisory" if dis else "Blocker", "colour.contrast", sel, "%d text run%s at %.1f:1, need%s %s:1, %spx, %s, %s: %s%s" % (len(rs), "" if len(rs) == 1 else "s", got, "s" if len(rs) == 1 else "", need, sizes, how, tag, eg, note))


def typography(rep, sel, platform, d):
    runs, blocks = d["runs"], d["blocks"]
    if not runs:
        return
    sizes = Counter()
    for r in runs:
        sizes[round(r["fs"], 1)] += r["n"]
    off = [s for s in sizes if not (s in SCALE or (platform == "ios" and s in IOS_SIZES))]
    for s in sorted(off):
        eg = next(r for r in runs if round(r["fs"], 1) == s)
        rep.add("Minor", "type.scale", sel + " " + eg["where"], "%gpx is off the scale (\"%s\")" % (s, eg["s"]))
    if len(sizes) > 7:
        rep.add("Minor", "type.scale", sel, "%d sizes in use: %s" % (len(sizes), ", ".join("%g" % s for s in sorted(sizes))))
    fams = Counter()
    for r in runs:
        fams[r["fam"]] += r["n"]
    plain = [f for f in fams if not re.search(r"mono|code", f, re.I)]
    if len(plain) > 2:
        rep.add("Minor", "type.families", sel, "%d families besides a mono: %s" % (len(plain), ", ".join(plain)))
    weights = defaultdict(Counter)
    for r in runs:
        weights[r["fam"]][r["fw"]] += 1
    for fam, ws in weights.items():
        ui = sorted({r["fw"] for r in runs if r["fam"] == fam and r["fs"] < 28})
        if len(ui) > 2:
            rep.add("Minor", "type.weights", sel, "%s uses %d weights under 28px: %s" % (fam, len(ui), ", ".join(map(str, ui))))
        for w, n in ws.items():
            if n <= 2 and len(ws) > 2:
                eg = next(r for r in runs if r["fam"] == fam and r["fw"] == w)
                rep.add("Minor", "type.weights", sel + " " + eg["where"], "stray weight %s %d on \"%s\"" % (fam, w, eg["s"]))
    lead = Counter()
    for r in runs:
        lh = r["lh"]
        if lh is None:
            lead["%g/normal" % r["fs"]] += 1
        elif lh / r["fs"] > 1.1 and abs(lh / 4 - round(lh / 4)) > 0.01 and not (platform == "ios" and (round(r["fs"]), round(lh)) in IOS):
            lead["%g/%g" % (r["fs"], lh)] += 1
    if lead:
        rep.add("Minor", "type.leading", sel, "line heights off the 4px grid: " + ", ".join("%s (%d)" % kv for kv in lead.most_common(6)))
    seen = set()
    for r in runs:
        key = (r["fs"], r["ls"], r["upper"], r["fam"])
        if key in seen or r["n"] < 2 or SYSTEM.match(r["fam"]) or re.search(r"mono|code", r["fam"], re.I):
            continue
        seen.add(key)
        fs, ls, where = r["fs"], r["ls"], sel + " " + r["where"]
        if ls < -0.045:
            rep.add("Minor", "type.tracking", where, "%gpx at %gem is tighter than -0.04em (\"%s\")" % (fs, ls, r["s"]))
        if r["upper"]:
            if fs <= 14 and ls < 0.036:
                rep.add("Minor", "type.tracking", where, "caps at %gpx with %gem, expected +0.04 to +0.08em (\"%s\")" % (fs, ls, r["s"]))
            elif ls < -0.001:
                rep.add("Minor", "type.tracking", where, "caps with negative tracking %gem (\"%s\")" % (ls, r["s"]))
        else:
            if ls > 0.005:
                rep.add("Minor", "type.tracking", where, "letter-spaced lower case: %gpx at +%gem (\"%s\")" % (fs, ls, r["s"]))
            elif fs >= 36 and ls > -0.015:
                rep.add("Minor", "type.tracking", where, "%gpx on a brand face at %gem, expected -0.02em (\"%s\")" % (fs, ls, r["s"]))
            elif 24 <= fs < 36 and ls > -0.005:
                rep.add("Minor", "type.tracking", where, "%gpx on a brand face at %gem, expected -0.01em (\"%s\")" % (fs, ls, r["s"]))
    for r in runs:
        if r["fs"] < 11:
            rep.add("Major", "type.minimum", sel + " " + r["where"], "%gpx text (\"%s\")" % (r["fs"], r["s"]))
        if r["upper"] and r["n"] >= 80:
            rep.add("Minor", "type.minimum", sel + " " + r["where"], "%d characters set in capitals (\"%s\")" % (r["n"], r["s"]))
        if r["it"] and r["fs"] >= 32 and any(x in r["fam"].lower() for x in SERIF):
            rep.add("Advisory", "identity.tell", sel + " " + r["where"], "italic serif at display size (%s %gpx): the most common generated hero" % (r["fam"], r["fs"]))
    for b in blocks:
        where = sel + " " + b["where"]
        if not b["heading"] and b["lines"] >= 3 and not 45 <= b["cpl"] <= 75:
            rep.add("Minor", "type.measure", where, "%d characters per line over %d lines (\"%s\")" % (b["cpl"], b["lines"], b["s"]))
        if not b["heading"] and b["lines"] >= 2 and b["lh"] and b["fs"] < 24 and b["lh"] / b["fs"] < 1.3:
            rep.add("Minor", "type.leading", where, "%g/%g is tighter than 1.3 on %d lines (\"%s\")" % (b["fs"], b["lh"], b["lines"], b["s"]))
        if b["lines"] >= 2 and b["fill"] <= (0.35 if b["heading"] else 0.25) and b["wrap"] not in ("balance", "pretty"):
            rep.add("Advisory", "type.breaks", where, "last line fills %d percent of the %s (\"%s\")" % (round(b["fill"] * 100), "headline" if b["heading"] else "column", b["s"]))
    body = max((s for s in sizes if s >= 14), key=lambda s: sizes[s], default=None)
    chain = sorted(s for s in sizes if body and s >= body)
    if len(chain) >= 3 and all(b / a < 1.25 for a, b in zip(chain, chain[1:])):
        rep.add("Minor", "type.hierarchy", sel, "no step of 1.25 or more between %s" % ", ".join("%g" % s for s in chain))
    for fam in fams:
        low = fam.lower()
        if any(low.startswith(x) for x in SPENT) and not (platform == "android" and low.startswith("roboto")):
            FACES[fam].append(sel)
    text = " ".join(r["txt"] for r in runs if not r["code"])
    for pat, what in ((r"\w'\w|(^|\s)'\w|\"\w|\w\"", "straight quote or apostrophe"), (r"\.\.\.", "three dots instead of an ellipsis"), (r"\w ?-- ?\w", "double hyphen"), ("[" + chr(0x2014) + chr(0x2013) + "]", "long dash"), (r"lorem ipsum", "lorem ipsum")):
        m = re.search(pat, text, re.I)
        if m:
            near = text[max(0, m.start() - 16): m.end() + 16].strip()
            rep.add("Blocker" if what == "lorem ipsum" else "Minor", "content.real" if what == "lorem ipsum" else "type.micro", sel, "%s near \"%s\"" % (what, near))
    for m in BUZZ.finditer(text):
        rep.add("Minor", "content.real", sel, "generic copy: \"%s\"" % text[max(0, m.start() - 20): m.end() + 20].strip())


def structure(rep, sel, platform, d, allow):
    spacing = {k: v for k, v in d["spacing"].items() if abs(float(k)) not in allow}
    if spacing:
        vals = sorted(spacing.items(), key=lambda kv: -kv[1]["n"])
        rep.add("Minor", "space.grid", sel, "off the 4px grid: " + ", ".join("%spx x%d (%s)" % (k, v["n"], v["eg"]) for k, v in vals[:6]))
    radii = {float(k): v for k, v in d["radii"].items()}
    off = [k for k in radii if k not in RADII]
    if off:
        rep.add("Minor", "shape.radius", sel, "radii off the shape scale: " + ", ".join("%gpx (%s)" % (k, radii[k]["eg"]) for k in sorted(off)))
    if len(radii) > 3:
        rep.add("Minor", "shape.radius", sel, "%d radii in use: %s" % (len(radii), ", ".join("%g" % k for k in sorted(radii))))
    for h in d["rhythm"]:
        if h["above"] <= h["below"]:
            rep.add("Minor", "space.heading", sel + " " + h["where"], "\"%s\" has %g above and %g below" % (h["s"], h["above"], h["below"]))
        elif h["above"] < 2 * h["below"]:
            rep.add("Advisory", "space.heading", sel + " " + h["where"], "\"%s\" has %g above and %g below: less than twice" % (h["s"], h["above"], h["below"]))
    for e in d["eyebrows"]:
        rep.add("Advisory", "identity.eyebrow", sel + " " + e["where"], "eyebrow \"%s\" over \"%s\"%s: does it say something the heading does not?" % (e["s"], e["over"], ", tracked capitals" if e["caps"] else ""))
    if d["cards"]:
        rep.add("Advisory", "layout.cards", sel, "%d containers inside containers, for example %s inside %s" % (len(d["cards"]), d["cards"][0]["where"], d["cards"][0]["inside"]))


def details(rep, sel, platform, d):
    names = {"side-stripe": ("Minor", "a thick coloured border on one side"), "border-shadow-tint": ("Minor", "border, shadow and tint together"), "gradient-text": ("Advisory", "gradient text"), "glow": ("Advisory", "a coloured glow"), "hard-shadow": ("Advisory", "a hard offset shadow"), "stripes": ("Advisory", "repeating stripes: a decision when they encode data, a reflex as decoration")}
    for tid, (sev, what) in names.items():
        hits = [t for t in d["tells"] if t["id"] == tid]
        if hits and (sel, tid) not in TOLD:
            TOLD.add((sel, tid))
            rep.add(sev, "layout.cards" if tid == "border-shadow-tint" else "identity.tell", sel, "%s on %d element%s, for example %s (%s)" % (what, len(hits), "" if len(hits) == 1 else "s", hits[0]["where"], hits[0]["v"]))
    floor = FLOOR[platform]
    for t in d["targets"]:
        low = t["h"] if platform == "web" and t["text"] and t["w"] >= 24 else min(t["w"], t["h"])
        if t["inlineText"] or low >= floor:
            continue
        sev = "Minor" if platform == "web" and low >= 24 else "Major"
        rep.add(sev, "target.size", sel + " " + t["where"], "\"%s\" is %dx%d, floor %d" % (t["name"], t["w"], t["h"], floor))
    for n in d["names"]:
        if sel not in rep.copies:
            rep.add("Major", "a11y.name", sel + " " + n["where"], n["v"])
    lv = d["levels"]
    for a, b in zip(lv, lv[1:]):
        if b > a + 1:
            rep.add("Minor", "a11y.headings", sel, "heading level jumps from h%d to h%d" % (a, b))
    if d["hiddenAtRest"]:
        rep.add("Advisory", "motion.rest", sel, "%d text runs are invisible with animation off, for example \"%s\"" % (len(d["hiddenAtRest"]), d["hiddenAtRest"][0]))


def canvas(rep, sel, d):
    bgs = Counter(tuple(r["bg"]) for r in d["runs"])
    if bgs:
        r_, g_, b_ = bgs.most_common(1)[0][0]
        if min(r_, g_, b_) >= 209 and r_ > g_ > b_ and r_ - b_ >= 2:
            rep.add("Advisory", "identity.tell", sel, "warm off-white ground rgb(%d, %d, %d): the default tasteful surface, so name the reason it is this product's canvas" % (r_, g_, b_))


def motion(rep, info):
    moving = info["transitions"] or info["animations"]
    rows = []
    for t in info["transitions"]:
        props = [x.strip() for x in t["prop"].split(",")]
        dur = max(ms(t["dur"]))
        rows.append({"element": t["where"], "property": t["prop"], "duration": "%gms" % dur, "easing": t["ease"]})
        bad = [x for x in props if LAYOUT.match(x)]
        paint = [x for x in props if PAINT.match(x)]
        if bad:
            rep.add("Minor", "motion.property", t["where"], "transitions %s" % ", ".join(bad))
        if paint:
            rep.add("Minor", "motion.property", t["where"], "transitions %s: build it from static layers or write the exception down" % ", ".join(paint))
        if dur > 400:
            rep.add("Minor", "motion.duration", t["where"], "%gms on %s" % (dur, t["prop"]))
        elif dur > 300:
            rep.add("Advisory", "motion.duration", t["where"], "%gms on %s: allowed for sheets and full-screen modals only" % (dur, t["prop"]))
        easing(rep, t["where"], t["ease"])
    for a in info["animations"]:
        props = info["keyframes"].get(a["name"], [])
        dur = max(ms(a["dur"] or "0s"))
        rows.append({"element": a["where"], "property": "@keyframes %s: %s" % (a["name"], ", ".join(props)), "duration": "%gms%s" % (dur, " infinite" if "infinite" in (a["iter"] or "") else ""), "easing": a["ease"] or "ease"})
        bad = [x for x in props if LAYOUT.match(x) or PAINT.match(x)]
        if bad:
            rep.add("Minor", "motion.property", a["where"], "@keyframes %s animates %s" % (a["name"], ", ".join(bad)))
        if "infinite" in (a["iter"] or ""):
            rep.add("Advisory", "motion.duration", a["where"], "@keyframes %s loops: it must carry live information and stop when hidden" % a["name"])
        elif dur > 1000:
            rep.add("Advisory", "motion.duration", a["where"], "@keyframes %s runs %gms: a launch moment stays under 1 second" % (a["name"], dur))
        easing(rep, a["where"], a["ease"] or "")
    if moving and not info["reduced"]:
        rep.add("Major", "motion.reduced", "page", "motion is defined and no prefers-reduced-motion rule exists")
    if info["hover"] and info["hoverGuarded"] < info["hover"]:
        rep.add("Minor", "motion.hover", "page", "%d of %d hover rules sit outside @media (hover: hover)" % (info["hover"] - info["hoverGuarded"], info["hover"]))
    for s in info["hoverSelf"][:5]:
        rep.add("Advisory", "motion.hover", s, "the hovered element moves itself: let a child carry the movement")
    miss = [n for n, ok in (("color-scheme", info["colorScheme"] not in ("", "normal")), ("::selection", info["selection"]), ("caret-color", info["caret"] is not False), ("accent-color", info["accentColor"] is not False), ("text-underline-offset", info["underlineOffset"] is not False)) if not ok]
    if miss:
        rep.add("Minor", "web.surfaces", "page", "left on browser defaults: " + ", ".join(miss))
    if not info["focusVisible"]:
        rep.add("Major", "a11y.focus", "page", "no :focus-visible style in any stylesheet")
    return rows


def easing(rep, where, ease):
    for e in re.split(r",(?![^(]*\))", ease or ""):
        e = e.strip()
        m = re.match(r"cubic-bezier\(([^)]+)\)", e)
        if e == "ease-in" or (m and [round(float(x), 2) for x in m.group(1).split(",")] == [0.42, 0, 1, 1]):
            rep.add("Minor", "motion.easing", where, "ease-in")
        elif m:
            pts = [float(x) for x in m.group(1).split(",")]
            if not (0 <= pts[1] <= 1 and 0 <= pts[3] <= 1):
                rep.add("Advisory", "motion.easing", where, "overshoot %s: a brand decision, written down" % e)
        elif e == "linear":
            rep.add("Advisory", "motion.easing", where, "linear: only for constant motion")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("page", help="an HTML file or a URL")
    ap.add_argument("--root", action="append", default=[], help='screen root, for example "#home:ios"; repeat for more')
    ap.add_argument("--themes", default="light,dark")
    ap.add_argument("--width", type=int, default=1440)
    ap.add_argument("--css", default="", help="extra CSS applied before measuring, for example to undo a presentation zoom")
    ap.add_argument("--skip", default="", help="selector list left out of every measurement, besides [data-system]")
    ap.add_argument("--allow", default="", help="extra spacing values that pass, for example platform insets: 34,59")
    ap.add_argument("--out", help="write the full report as JSON")
    a = ap.parse_args()
    url = a.page if re.match(r"^[a-z]+://", a.page) else pathlib.Path(a.page).resolve().as_uri()
    rep, info, rows, facts = Report(), None, [], {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        for ti, theme in enumerate(a.themes.split(",")):
            page = browser.new_context(viewport={"width": a.width, "height": 1000}, color_scheme=theme, device_scale_factor=1).new_page()
            page.goto(url)
            page.evaluate("() => document.fonts ? document.fonts.ready.then(() => true) : true")
            page.wait_for_timeout(400)
            if ti == 0:
                info = page.evaluate(FN % (SRC, "page"), None)
                rows = motion(rep, info)
            page.add_style_tag(content=FREEZE + a.css)
            sw = page.evaluate("""() => [...document.querySelectorAll('[data-set]')].map(b => { const i = b.dataset.set.indexOf('='); return {attr: b.dataset.set.slice(0, i), val: b.dataset.set.slice(i + 1), on: b.dataset.on || ':root'}; })""")
            if any(s["attr"] == "data-theme" for s in sw):
                page.evaluate("t => document.documentElement.setAttribute('data-theme', t)", theme)
            roots = [(r.rsplit(":", 1) if re.search(r":(ios|android|web)$", r) else [r, "web"]) for r in a.root]
            if not roots:
                roots = page.evaluate("""() => [...document.querySelectorAll('[data-screen]')].filter(e => !e.parentElement.closest('[data-screen]')).map((e, i) => { e.setAttribute('data-audit-root', i); return ['[data-audit-root="' + i + '"]', e.dataset.platform || 'web']; })""") or [["body", "web"]]
            # a screen shown a second time at another width (an inert copy) is measured too
            rep.copies = [sel for sel, _ in roots if page.evaluate("s => { const e = document.querySelector(s); return !!(e && e.closest('[inert]')); }", sel)]
            cache = {}
            for ri, (sel, platform) in enumerate(roots):
                base = page.evaluate(FN % (SRC, "screen"), {"sel": sel, "key": "r%d" % ri, "skip": a.skip})
                if base.get("missing"):
                    rep.add("Major", "state.coverage", sel, "screen root not found")
                    continue
                known = set()
                contrast(page, rep, sel, base, theme, "", cache, known)
                groups = defaultdict(list)
                for s in sw:
                    if s["attr"] != "data-theme" and page.evaluate("([on, sel]) => { const r = document.querySelector(sel); return [...document.querySelectorAll(on)].some(e => e === r || e.contains(r) || r.contains(e)); }", [s["on"], sel]):
                        if s["val"] not in groups[(s["attr"], s["on"])]:
                            groups[(s["attr"], s["on"])].append(s["val"])
                clipped = {(c["where"], c["s"], bool(c.get("edge"))): "" for c in base["clipped"]}
                for (attr, on), vals in groups.items():
                    cur = page.evaluate("([on, attr]) => document.querySelector(on).getAttribute(attr)", [on, attr])
                    for v in vals:
                        if v == cur:
                            continue
                        page.evaluate("([on, attr, v]) => document.querySelectorAll(on).forEach(e => e.setAttribute(attr, v))", [on, attr, v])
                        var = "%s %s" % (attr.replace("data-", ""), v)
                        d = page.evaluate(FN % (SRC, "screen"), {"sel": sel, "key": "r%d" % ri, "skip": a.skip})
                        contrast(page, rep, sel, d, theme, var, cache, known)
                        for c in d["clipped"]:
                            clipped.setdefault((c["where"], c["s"], bool(c.get("edge"))), var)
                        if ti == 0:
                            details(rep, sel, platform, d)
                    page.evaluate("([on, attr, v]) => document.querySelectorAll(on).forEach(e => v === null ? e.removeAttribute(attr) : e.setAttribute(attr, v))", [on, attr, cur])
                if ti:
                    continue
                typography(rep, sel, platform, base)
                structure(rep, sel, platform, base, {float(x) for x in a.allow.split(",") if x} | ({34.0} if platform == "ios" else set()))
                details(rep, sel, platform, base)
                canvas(rep, sel, base)
                for (where, s, edge), var in clipped.items():
                    rep.add("Major" if edge else "Minor", "layout.clipped", sel + " " + where, "\"%s\" %s%s" % (s, "runs off the side of the screen" if edge else "is cut off", " in " + var if var else ""))
                states = [v for (attr, on), vals in groups.items() if attr == "data-state" for v in vals]
                facts[sel] = {"platform": platform, "text runs": len(base["runs"]), "sizes": sorted({round(r["fs"], 1) for r in base["runs"]}), "families": sorted({r["fam"] for r in base["runs"]}), "states": states, "truncated": base["truncated"]}
                if states and not {"empty", "loading", "error"} & set(states):
                    rep.add("Advisory", "state.coverage", sel, "states %s: no empty, loading or error among them" % ", ".join(states))
                # text scaling: double the reader's default size and look again
                page.evaluate("() => { const r = document.documentElement; r.dataset.auditFs = r.style.fontSize; r.style.fontSize = parseFloat(getComputedStyle(r).fontSize) * 2 + 'px'; }")
                big = page.evaluate(FN % (SRC, "screen"), {"sel": sel, "key": "r%d" % ri, "skip": a.skip})
                page.evaluate("() => { const r = document.documentElement; r.style.fontSize = r.dataset.auditFs || ''; }")
                n1, n2 = sum(r["fs"] * r["n"] for r in base["runs"]), sum(r["fs"] * r["n"] for r in big["runs"])
                grew = n2 / n1 if n1 else 1
                facts[sel]["text at 200 percent"] = "x%.2f" % grew
                if grew < 1.5:
                    rep.add("Major", "a11y.scaling", sel, "text grows x%.2f when the reader doubles the default size: the type is set in px" % grew)
                else:
                    for c in big["clipped"]:
                        if (c["where"], c["s"], bool(c.get("edge"))) not in clipped:
                            rep.add("Major", "a11y.scaling", sel + " " + c["where"], "\"%s\" %s at 200 percent" % (c["s"], "runs off the side of the screen" if c.get("edge") else "is cut off"))
                if info.get("accent") and Image is not None:
                    try:
                        im = Image.open(io.BytesIO(page.locator(sel).first.screenshot(timeout=5000))).convert("RGB")
                        im.thumbnail((200, 400))
                        acc = page.evaluate("c => { const e = document.createElement('i'); e.style.color = c; document.body.appendChild(e); const v = getComputedStyle(e).color; e.remove(); return v; }", info["accent"])
                        ar, ag, ab = [float(x) for x in re.findall(r"[\d.]+", acc)[:3]]
                        px = list(im.getdata())
                        share = sum(1 for (r_, g_, b_) in px if abs(r_ - ar) + abs(g_ - ag) + abs(b_ - ab) < 60) / len(px)
                        facts[sel]["accent share"] = "%.1f percent" % (share * 100)
                        if share > 0.05:
                            rep.add("Advisory", "identity.tell", sel, "the accent covers %.1f percent of the screen: above 5 percent it needs to be a brand moment" % (share * 100))
                    except Exception:
                        pass
            page.context.close()
        browser.close()
    for fam, sels in FACES.items():
        rep.add("Advisory", "identity.face", ", ".join(sels), "%s is a face every generated interface reaches for: name the reason from the brief, or the licensed face it stands in for" % fam)
    items = sorted(rep.items, key=lambda i: (ORDER[i["severity"]], i["rule"], i["where"]))
    counts = Counter(i["severity"] for i in items)
    print("%s\n%s" % (a.page, " | ".join("%s %d" % (s, counts.get(s, 0)) for s in ORDER)))
    last = None
    for i in items:
        if i["severity"] != last:
            last = i["severity"]
            print("\n" + last.upper())
        print("  [%s] %s: %s" % (i["rule"], i["where"], i["finding"]))
    print("\nMOTION INVENTORY (start of the motion table)")
    for r in rows:
        print("  %s | %s | %s | %s" % (r["element"], r["property"], r["duration"], r["easing"]))
    print("\nSCREENS")
    for sel, f in facts.items():
        print("  %s: %s" % (sel, "; ".join("%s %s" % (k, v) for k, v in f.items())))
    if a.out:
        pathlib.Path(a.out).write_text(json.dumps({"page": a.page, "counts": counts, "findings": items, "motion": rows, "screens": facts, "rules": RULES}, indent=1))
    sys.exit(1 if counts.get("Blocker") else 0)


if __name__ == "__main__":
    main()
