#!/usr/bin/env python3
"""
Generate sitemap.xml from the pages actually on disk.
Run from anywhere:  python3 scripts/generate-sitemap.py
The sitemap is derived, never hand-edited — gate G11 verifies it matches reality.
"""
import pathlib, datetime

ROOT = pathlib.Path(__file__).resolve().parent.parent
DOMAIN = "https://www.nfceh.org"
SKIP_DIRS = {"scripts", "assets", ".git", ".github"}
EXCLUDE = {"404.html"}

urls = []
for p in sorted(ROOT.rglob("*.html")):
    r = p.relative_to(ROOT)
    if any(part in SKIP_DIRS for part in r.parts) or str(r) in EXCLUDE:
        continue
    if str(r) == "index.html":
        url = DOMAIN + "/"
    elif r.name == "index.html":
        url = f"{DOMAIN}/{r.parent.as_posix()}/"
    else:
        continue  # non-index html outside the convention: not a public URL
    lastmod = datetime.date.fromtimestamp(p.stat().st_mtime).isoformat()
    urls.append((url, lastmod))

# stable ordering: home first, then alphabetical
urls.sort(key=lambda u: (u[0] != DOMAIN + "/", u[0]))

lines = ['<?xml version="1.0" encoding="UTF-8"?>',
         '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for url, lastmod in urls:
    lines.append(f"  <url><loc>{url}</loc><lastmod>{lastmod}</lastmod></url>")
lines.append("</urlset>")
(ROOT / "sitemap.xml").write_text("\n".join(lines) + "\n")
print(f"sitemap.xml written: {len(urls)} URLs")
for url, _ in urls:
    print(" ", url)
