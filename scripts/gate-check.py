#!/usr/bin/env python3
"""
NFCEH pre-push gates — nfceh.org
Run from the site root:  python3 scripts/gate-check.py
Exit 0 = all critical gates pass. Exit 1 = push must not happen.

Every gate maps to a documented incident or brand rule.
See: Website Best Practices/NFCEH-MIGRATION-PLAYBOOK.md §7
"""
import re
import sys
import pathlib
import subprocess
import tempfile

ROOT = pathlib.Path(__file__).resolve().parent.parent
GA_ID = "G-5YTZMH6E01"
DOMAIN = "https://www.nfceh.org"
SKIP_DIRS = {"scripts", "assets", ".git", ".github"}

CRIT, WARN = [], []


def crit(gate, msg):
    CRIT.append(f"[{gate}] {msg}")


def warn(gate, msg):
    WARN.append(f"[{gate}] {msg}")


def pages():
    out = []
    for p in sorted(ROOT.rglob("*.html")):
        if any(part in SKIP_DIRS for part in p.relative_to(ROOT).parts):
            continue
        out.append(p)
    return out


def rel(p):
    return str(p.relative_to(ROOT))


def visible_text(html):
    """Strip tags/scripts/styles; decode common entities for phrase scanning."""
    html = re.sub(r"<script\b.*?</script>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<style\b.*?</style>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    text = re.sub(r"<[^>]+>", " ", html)
    for ent, ch in (("&rsquo;", "'"), ("&lsquo;", "'"), ("&ldquo;", '"'),
                    ("&rdquo;", '"'), ("&mdash;", "—"), ("&amp;", "&"),
                    ("&nbsp;", " "), ("&middot;", "·"), ("&rarr;", "→")):
        text = text.replace(ent, ch)
    return text


PAGES = pages()
DOCS = {p: p.read_text(encoding="utf-8") for p in PAGES}
TEXTS = {p: visible_text(t) for p, t in DOCS.items()}

# ---------------------------------------------------------------- G1: GA ID
for p, t in DOCS.items():
    ids = set(re.findall(r"G-[A-Z0-9]{6,14}", t))
    if GA_ID not in ids:
        crit("G1-ga", f"{rel(p)}: missing GA tag {GA_ID}")
    strays = ids - {GA_ID}
    if strays:
        crit("G1-ga", f"{rel(p)}: stray GA id(s) {sorted(strays)}")

# ------------------------------------------------------------ G2: canonical
for p, t in DOCS.items():
    m = re.search(r'<link rel="canonical" href="([^"]+)"', t)
    if not m:
        crit("G2-canonical", f"{rel(p)}: missing canonical tag")
    elif not m.group(1).startswith(DOMAIN):
        crit("G2-canonical", f"{rel(p)}: canonical not on {DOMAIN}: {m.group(1)}")

# --------------------------------------------------------------- G3: one h1
for p, t in DOCS.items():
    n = len(re.findall(r"<h1[\s>]", t))
    if n != 1:
        crit("G3-h1", f"{rel(p)}: {n} <h1> tags (must be exactly 1)")

# ------------------------------------------------- G4/G5: nav + footer parity
def hrefs_in(block):
    return re.findall(r'href="([^"]+)"', block) if block else []


nav_ref = foot_ref = None
for p, t in DOCS.items():
    nav = re.search(r'<nav class="primary".*?</nav>', t, re.S)
    foot = re.search(r'<footer class="site-footer">.*?</footer>', t, re.S)
    if not nav:
        crit("G4-nav", f"{rel(p)}: missing primary nav")
        continue
    if not foot:
        crit("G5-footer", f"{rel(p)}: missing site footer")
        continue
    nh, fh = hrefs_in(nav.group(0)), hrefs_in(foot.group(0))
    if nav_ref is None:
        nav_ref, nav_src = nh, rel(p)
    elif nh != nav_ref:
        crit("G4-nav", f"{rel(p)}: nav hrefs differ from {nav_src}")
    if foot_ref is None:
        foot_ref, foot_src = fh, rel(p)
    elif fh != foot_ref:
        crit("G5-footer", f"{rel(p)}: footer hrefs differ from {foot_src}")

# --------------------------------------------- G6: shared stylesheet, no chrome overrides
CHROME_SELECTORS = (".site-header", ".site-footer", "nav.primary", ".nav-toggle",
                    ".header-inner", ".footer-inner")
for p, t in DOCS.items():
    if '<link rel="stylesheet" href="/styles.css">' not in t:
        crit("G6-css", f"{rel(p)}: does not link /styles.css")
    for block in re.findall(r"<style\b[^>]*>(.*?)</style>", t, re.S):
        hit = [s for s in CHROME_SELECTORS if s in block]
        if hit:
            crit("G6-css", f"{rel(p)}: <style> block overrides chrome selectors {hit}")

# ----------------------------------------------- G7: internal links resolve
for p, t in DOCS.items():
    for target in re.findall(r'(?:href|src)="(/[^"#?]*)', t):
        if not target or target == "/":
            continue
        path = target.lstrip("/")
        f = ROOT / path / "index.html" if target.endswith("/") else ROOT / path
        if not f.exists():
            if path.startswith("assets/"):
                warn("G7-links", f"{rel(p)}: asset not yet downloaded: {target} (run download-assets.sh)")
            else:
                crit("G7-links", f"{rel(p)}: broken internal link {target}")

# ------------------------------------------------ G8: target=_blank noopener
for p, t in DOCS.items():
    for tag in re.findall(r"<a [^>]*target=\"_blank\"[^>]*>", t):
        if "noopener" not in tag:
            crit("G8-noopener", f"{rel(p)}: target=_blank without rel=noopener: {tag[:80]}")

# --------------------------------------------------------- G9: inline JS syntax
node = subprocess.run(["which", "node"], capture_output=True, text=True).stdout.strip()
for p, t in DOCS.items():
    for attrs, js in re.findall(r"<script((?:(?!\bsrc=)[^>])*)>(.*?)</script>", t, re.S):
        if not js.strip() or "ld+json" in attrs:
            continue
        if node:
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False) as f:
                f.write(js)
            r = subprocess.run([node, "--check", f.name], capture_output=True, text=True)
            pathlib.Path(f.name).unlink()
            if r.returncode != 0:
                crit("G9-js", f"{rel(p)}: inline JS fails to parse: {r.stderr.strip().splitlines()[-1][:120]}")
        else:
            # heuristic: apostrophe inside a single-quoted string
            if re.search(r"'[^'\n]*\w'\w", js):
                warn("G9-js", f"{rel(p)}: possible apostrophe-in-single-quote (node not available to verify)")

# JSON-LD validity
import json
for p, t in DOCS.items():
    for ld in re.findall(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        try:
            json.loads(ld)
        except json.JSONDecodeError as e:
            crit("G9-jsonld", f"{rel(p)}: invalid JSON-LD: {e}")

# ----------------------------------------------------------- G10: img alt
for p, t in DOCS.items():
    for tag in re.findall(r"<img [^>]*>", t):
        if " alt=" not in tag:
            crit("G10-alt", f"{rel(p)}: <img> missing alt: {tag[:80]}")

# --------------------------------------------------- G11: sitemap <-> pages
smp = ROOT / "sitemap.xml"
if not smp.exists():
    crit("G11-sitemap", "sitemap.xml missing")
else:
    locs = set(re.findall(r"<loc>([^<]+)</loc>", smp.read_text()))
    expected = set()
    for p in PAGES:
        r = rel(p)
        if r == "404.html":
            continue
        url = DOMAIN + "/" if r == "index.html" else DOMAIN + "/" + r.replace("/index.html", "/")
        expected.add(url)
        if url not in locs:
            crit("G11-sitemap", f"page not in sitemap: {url}")
    for loc in locs - expected:
        crit("G11-sitemap", f"sitemap entry has no page on disk: {loc}")

# ------------------------------------------------------------ G12: secrets
SECRET_PATTERNS = [r"ghp_[A-Za-z0-9]{20,}", r"github_pat_[A-Za-z0-9_]{20,}",
                   r"AKIA[0-9A-Z]{16}", r"-----BEGIN [A-Z ]*PRIVATE KEY",
                   r"https://[^/\s\"]+:[^@\s\"]+@github\.com",
                   r"https://gh[a-z]?_[^@\s\"]+@github\.com"]
for p in sorted(ROOT.rglob("*")):
    if p.is_dir() or ".git" in p.parts or p.suffix in {".png", ".jpg", ".jpeg", ".ico", ".pdf", ".webp", ".svg"}:
        continue
    try:
        body = p.read_text(encoding="utf-8", errors="ignore")
    except Exception:
        continue
    for pat in SECRET_PATTERNS:
        if re.search(pat, body):
            crit("G12-secrets", f"{rel(p)}: matches secret pattern {pat}")

# ============================ NFCEH BRAND GATES ============================
# N1: person-first language
for p, txt in TEXTS.items():
    for pat, label in [(r"\bthe homeless\b(?!ness)", '"the homeless"'),
                       (r"\bvagrants?\b", '"vagrant(s)"'),
                       (r"\bstreet people\b", '"street people"')]:
        for m in re.finditer(pat, txt, re.I):
            ctx = txt[max(0, m.start() - 40):m.end() + 40].replace("\n", " ")
            crit("N1-person-first", f'{rel(p)}: banned phrase {label}: "...{ctx.strip()}..."')

# N2: signature phrase
for p, txt in TEXTS.items():
    if re.search(r"\bbuilding together\b", txt, re.I):
        crit("N2-signature", f'{rel(p)}: "Building Together" is not a brand phrase (use "Forward Together")')

# N3: mission statement — END in caps
for p, txt in TEXTS.items():
    for m in re.finditer(r"best practices to (\w+) homelessness", txt):
        if m.group(1) != "END":
            crit("N3-end-caps", f'{rel(p)}: mission statement must use "END" in caps (found "{m.group(1)}")')
    for m in re.finditer(r"to (End|end) homelessness in (America|the United States)", txt):
        if m.group(1) != "END" and "power" in txt[max(0, m.start() - 60):m.start()]:
            warn("N3-end-caps", f'{rel(p)}: hero END-phrase uses "{m.group(1)}" — verify caps where formatting allows')

# N4: retired HOUSE framework
for p, txt in TEXTS.items():
    if re.search(r"HOUSE (model|pathway|framework)|Hear, Offer, Unite", txt):
        crit("N4-house", f"{rel(p)}: references retired HOUSE framework (retired June 2026)")

# N5: WCAG text color
for p, t in DOCS.items():
    for tag in re.findall(r'style="[^"]*"', t):
        if re.search(r"(?<!background-)(?<!border-)color:\s*(#BEE5EA|var\(--blue-light\))", tag, re.I):
            crit("N5-wcag", f"{rel(p)}: light blue used as text color: {tag[:90]}")

# N6: date integrity
for p, txt in TEXTS.items():
    if re.search(r"May 2,? 2026", txt):
        crit("N6-date", f'{rel(p)}: references postponed date "May 2, 2026" (Homelessness Sunday is October 11, 2026)')

# ================================ REPORT ================================
print(f"Checked {len(PAGES)} pages.")
for w in WARN:
    print(f"  WARN  {w}")
if CRIT:
    print(f"\n{len(CRIT)} CRITICAL failure(s) — push blocked:")
    for c in CRIT:
        print(f"  CRIT  {c}")
    sys.exit(1)
print(f"All critical gates passed. ({len(WARN)} warning(s))")
sys.exit(0)
