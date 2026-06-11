# nfceh.org — Static Site

Static HTML rebuild of nfceh.org for GitHub Pages. No build step — what's in this
folder is the site.

## Structure

Each page is a folder with an `index.html`, so URLs match the old Wix site
(`/about/`, `/homelessness-sunday/`, etc.). Shared styling lives in `styles.css`.
Google Analytics (G-5YTZMH6E01) is included on every page.

| Path | Page |
|---|---|
| `/` | Home |
| `/about/` | About Us (Vision) |
| `/about/leadership/` | Leadership |
| `/about/participating-churches/` | Participating Churches |
| `/homelessness-sunday/` | Homelessness Sunday |
| `/love-thy-unhoused-neighbor/` | The Church's Role |
| `/learn/` | Resources for Congregations |
| `/blog/` | Blog index |
| `/blog/how-faith-communities-can-help-end-homelessness/` | Cornerstone post |
| `/join/` | Join Us |
| `/donate/` | Donate |
| `/privacy/`, `/accessibility/` | Policies |

## Before launch

1. **Download assets from Wix** (while the Wix plan is still active):
   `bash download-assets.sh` — pulls all images + the Homelessness Sunday flyer
   PDF into `assets/`. Commit them.
2. **Preview locally**: `python3 -m http.server` from this folder, then open
   http://localhost:8000 (links are root-relative, so opening files directly
   won't style correctly).

## Quality gates (run before every push)

- `python3 scripts/gate-check.py` — 12 universal gates (GA ID consistency,
  canonical tags, single h1, nav/footer parity, no chrome overrides, link
  integrity, noopener, JS/JSON-LD syntax, img alt, sitemap match, secrets scan)
  plus 6 NFCEH brand gates (person-first language, "Forward Together" not
  "Building Together", END in caps, no HOUSE references, WCAG text colors,
  October 11 date integrity). Exit 1 = do not push.
- After cloning the repo, run `bash scripts/install-hooks.sh` **once** — every
  `git push` then runs the gates automatically and blocks on failure.
- `sitemap.xml` is generated, never hand-edited: run
  `python3 scripts/generate-sitemap.py` after adding or removing a page.
  Gate G11 fails the push if the sitemap and the file tree disagree.

See `Website Best Practices/NFCEH-MIGRATION-PLAYBOOK.md` §7 for the incident
behind each gate.

## Deploy to GitHub Pages

1. Create a GitHub repo and push the contents of this folder to the `main` branch.
2. Repo Settings → Pages → Source: `main` branch, `/ (root)`.
3. The `CNAME` file (www.nfceh.org) is already included.
4. Run `bash scripts/install-hooks.sh` in the clone to arm the pre-push gates.

## DNS cutover (at the registrar / Wix DNS)

1. `www` CNAME → `<your-github-username>.github.io`
2. Apex `nfceh.org` A records → 185.199.108.153, 185.199.109.153,
   185.199.110.153, 185.199.111.153 (verify current IPs in GitHub Pages docs)
3. Keep any MX records if domain email is set up.
4. In repo Settings → Pages, set custom domain `www.nfceh.org` and enable
   **Enforce HTTPS** once the certificate is issued.
5. Re-verify the domain in Google Search Console (the old Wix meta tag is
   carried over in `index.html`, so verification should persist) and submit
   `https://www.nfceh.org/sitemap.xml`.

## Adding a blog post

1. Copy `blog/how-faith-communities-can-help-end-homelessness/index.html` to
   `blog/<new-slug>/index.html`.
2. Replace title/meta/canonical/JSON-LD and the article content.
3. Add a `.post-card` entry to `blog/index.html`.
4. Run `python3 scripts/generate-sitemap.py` to pick up the new URL.
5. Tag posts by Type: Cornerstone / Educate / Action / Foundational.
6. Run `python3 scripts/gate-check.py` before committing.

## Notes

- Old Wix pages /news, /events, /collections were template filler and were
  intentionally dropped. /blank-2 and /blank-5 are gone; GitHub Pages will
  serve `404.html` for them.
- The HOUSE framework was retired (June 2026); /learn is now Resources.
- Privacy and accessibility pages are real content now (the Wix versions were
  unedited templates).
